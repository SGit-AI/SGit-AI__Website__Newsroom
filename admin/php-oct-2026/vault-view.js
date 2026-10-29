/**
 * vault-view.js: the PHP evidence vault, read live in this page with its public read key (card 089).
 *
 * The SG/App vault browser reads a whole vault before it shows anything, and this one is 1,800 files and half a
 * gigabyte of captures. This view reads only what is asked for, with the reader the wire already uses
 * (wire/vault-reader.js): the head pointer, the manifest (sources/index.json), and, when a source is opened,
 * that source's own subtree, its notes, the app's thumbnail of each capture, and the full screenshot or the
 * text on request. Everything is decrypted in the browser; the read key cannot write.
 *
 * Mounts on <div id="vault-view" data-config="...json">; draws as text nodes and elements, never innerHTML
 * from vault content, except the notes, which go through the reader's own markdown renderer (it escapes).
 */
import { VaultReader, markdown } from '../../wire/vault-reader.js'

const el = (tag, attrs = {}, ...kids) => {
    const n = document.createElement(tag)
    for (const [k, v] of Object.entries(attrs)) {
        if (k === 'class') n.className = v
        else if (k.startsWith('on')) n.addEventListener(k.slice(2), v)
        else if (v !== null && v !== undefined) n.setAttribute(k, v)
    }
    for (const k of kids.flat()) if (k !== null && k !== undefined) n.append(k instanceof Node ? k : document.createTextNode(String(k)))
    return n
}
const kb = n => n >= 1e6 ? `${(n / 1e6).toFixed(1)} MB` : `${Math.max(1, Math.round(n / 1e3))} KB`

async function main() {
    const root = document.getElementById('vault-view')
    if (!root) return
    const cfg = JSON.parse(root.dataset.config)
    const status = el('p', { class: 'vv-status' }, 'Opening the vault in your browser…')
    root.replaceChildren(status)
    let reader
    try {
        reader = await new VaultReader({ endpoint: cfg.remote, vault_id: cfg.vault_id, read_key: cfg.read_key, ref_ttl_s: 60 }).init()
        await reader.open()
    } catch (e) {
        status.textContent = `The vault could not be opened here: ${e.message}. Clone it instead, with the command above.`
        return
    }

    // the tree, one level at a time, only where asked
    const level = async treeId => {
        const t = await reader.objectJson(treeId), out = {}
        await Promise.all((t.entries || []).map(async e => {
            const name = await reader.decryptB64(e.name_enc)
            out[name] = e.tree_id ? { tree_id: e.tree_id } : { blob_id: e.blob_id, size: parseInt(await reader.decryptB64(e.size_enc) || '0', 10) }
        }))
        return out
    }
    const walk = async (treeId, prefix = '', out = {}) => {
        const l = await level(treeId)
        await Promise.all(Object.entries(l).map(async ([name, v]) => v.tree_id ? walk(v.tree_id, `${prefix}${name}/`, out) : (out[prefix + name] = v)))
        return out
    }
    const top = await level(reader.commit.tree_id)
    const sourcesTree = await level(top.sources.tree_id)
    const appTree = top.app ? await level(top.app.tree_id) : {}
    const shotsTree = appTree.shots ? await level(appTree.shots.tree_id) : {}
    const blobText = async b => new TextDecoder().decode(await reader.object(b.blob_id))
    const blobUrl = async (b, type) => URL.createObjectURL(new Blob([await reader.object(b.blob_id)], { type }))
    const manifest = JSON.parse(await blobText(sourcesTree['index.json']))

    status.replaceChildren(
        'Read live from the vault at ', el('code', {}, reader.head.replace('obj-cas-imm-', '')),
        ` (“${reader.message.slice(0, 90)}${reader.message.length > 90 ? '…' : ''}”): ${manifest.length} sources. `,
        `${reader.stats.fetch} objects fetched, ${kb(reader.stats.bytesNet)}; open a source to read its notes and captures.`)

    // filters
    const kinds = [...new Set(manifest.map(s => s.kind || 'other'))].sort()
    const writers = [...new Set(manifest.map(s => s.added_by || 'unknown'))].sort()
    const q = el('input', { type: 'search', placeholder: 'Filter by slug, publisher or title', class: 'vv-q', 'aria-label': 'Filter the sources' })
    const kindSel = el('select', { 'aria-label': 'Kind' }, el('option', { value: '' }, 'every kind'), kinds.map(k => el('option', { value: k }, k)))
    const whoSel = el('select', { 'aria-label': 'Writer' }, el('option', { value: '' }, 'every writer'), writers.map(k => el('option', { value: k }, k)))
    const count = el('span', { class: 'vv-count' })
    const list = el('div', { class: 'vv-list' })
    root.append(el('div', { class: 'vv-bar' }, q, kindSel, whoSel, count), list)

    const draw = () => {
        const t = q.value.trim().toLowerCase()
        const rows = manifest.filter(s => (!kindSel.value || (s.kind || 'other') === kindSel.value) && (!whoSel.value || (s.added_by || 'unknown') === whoSel.value)
            && (!t || [s.slug, s.publisher, s.title, s.url].join(' ').toLowerCase().includes(t)))
        count.textContent = `${rows.length} of ${manifest.length}`
        list.replaceChildren(...rows.map(s => {
            const body = el('div', { class: 'vv-body' })
            const d = el('details', { class: 'vv-src', id: `vv-${s.slug}` },
                el('summary', {}, el('span', { class: `vv-st vv-${s.status || ''}` }, s.status || ''), ' ', el('b', {}, s.title || s.slug),
                    el('span', { class: 'vv-meta' }, ` ${s.publisher || ''} · ${s.kind || ''} · ${(s.captures || []).length} capture(s) · ${s.added_by || ''}`)),
                body)
            d.addEventListener('toggle', () => { if (d.open && !body.dataset.loaded) { body.dataset.loaded = '1'; openSource(s, body) } }, { once: false })
            return d
        }))
    }
    const openSource = async (s, body) => {
        body.replaceChildren(el('p', { class: 'vv-dim' }, 'Reading this source from the vault…'))
        try {
            const files = await walk(sourcesTree[s.slug].tree_id)
            const kids = [el('p', {}, el('a', { href: s.url, rel: 'noopener' }, s.url), el('span', { class: 'vv-dim' }, ` · published ${s.published || 'not stated'} · `), el('code', {}, s.slug))]
            if (files['notes.md']) { const n = el('div', { class: 'vv-notes' }); n.innerHTML = markdown(await blobText(files['notes.md'])); kids.push(n) }
            const caps = [...new Set(Object.keys(files).filter(f => f.startsWith('captures/')).map(f => f.split('/')[1]))].sort()
            const shots = shotsTree[s.slug] ? await level(shotsTree[s.slug].tree_id) : {}
            for (const c of caps) {
                const f = n => files[`captures/${c}/${n}`]
                const prov = f('provenance.json') ? JSON.parse(await blobText(f('provenance.json'))) : {}
                const box = el('div', { class: 'vv-cap' }, el('p', { class: 'vv-cap-h' }, el('b', {}, prov.started_utc || c), ` · HTTP ${prov.status ?? '?'}`, prov.error ? ` · ${prov.error}` : ''))
                const thumb = shots[`${c}.thumb.webp`]
                if (thumb) box.append(el('img', { class: 'vv-thumb', alt: `The top of the page as captured at ${prov.started_utc || c}`, src: await blobUrl(thumb, 'image/webp') }))
                const acts = el('p', { class: 'vv-acts' })
                const shot = f('screenshot.png'), text = f('text.txt'), out = el('div', { class: 'vv-out' })
                if (shot) acts.append(el('button', { type: 'button', onclick: async ev => { ev.target.disabled = true; out.replaceChildren(el('img', { class: 'vv-full', alt: `Full-page screenshot, ${prov.started_utc || c}`, src: await blobUrl(shot, 'image/png') })) } }, `Full screenshot (${kb(shot.size)})`))
                if (text) acts.append(el('button', { type: 'button', onclick: async ev => { ev.target.disabled = true; out.replaceChildren(el('pre', { class: 'vv-text' }, (await blobText(text)).slice(0, 20000))) } }, `Text (${kb(text.size)})`))
                const hashes = el('details', { class: 'vv-hashes' }, el('summary', {}, 'sha256 of each file'),
                    el('ul', {}, Object.entries(prov.files || {}).map(([n, h]) => el('li', {}, el('code', {}, n), ' ', el('code', { class: 'vv-h' }, h)))))
                box.append(acts, out, hashes)
                kids.push(box)
            }
            if (!caps.length) kids.push(el('p', { class: 'vv-dim' }, 'No capture in this source; see its notes.'))
            body.replaceChildren(...kids)
        } catch (e) { body.replaceChildren(el('p', { class: 'vv-dim' }, `Could not read this source: ${e.message}`)) }
    }
    for (const c of [q, kindSel, whoSel]) c.addEventListener('input', draw)
    draw()
    const hash = location.hash.match(/^#vv-(.+)$/)
    if (hash) { const d = document.getElementById(`vv-${decodeURIComponent(hash[1])}`); if (d) { d.open = true; d.scrollIntoView() } }
}

main()
