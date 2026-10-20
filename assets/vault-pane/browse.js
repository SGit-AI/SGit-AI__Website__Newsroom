/**
 * browse.js: your vaults, opened (card 079). The page vault/browse.html.
 *
 * With the session the vault pane keeps for this tab (the door it opened with your passkey), this page opens the
 * door, the master, the reader vault and the lane, here, with the same library, and shows what each holds: the files
 * and folders, any file's contents, and the commits, with the files as they were at each. The door and the master
 * hold keys: their files open only behind Reveal. The reader vault can also be opened in the SG/Vault app, read-only,
 * by handing its READ key to that app over its embed protocol: the vault browser there, and App Mode, where it opens
 * with the newsroom's shared viewer once that is linked. Nothing is written from this page.
 *
 * @module vault-browse
 */
import * as NV from '../newsroom-vault.js'
import { loadLibrary, ENDPOINT } from './vault-pane.js'
import { mountEmbed } from './sg-embed.js'

const SESSION = 'sgit.vault.session'
const h = (tag, attrs, ...kids) => {
    const el = document.createElement(tag)
    for (const [k, v] of Object.entries(attrs || {})) { if (v === false || v == null) continue; if (k.startsWith('on')) el.addEventListener(k.slice(2), v); else el.setAttribute(k, v === true ? '' : v) }
    for (const kid of kids.flat()) if (kid != null && kid !== false) el.append(kid instanceof Node ? kid : String(kid))
    return el
}
const put = (el, ...kids) => el.replaceChildren(...kids.flat().filter(k => k != null && k !== false))
const err = e => String(e && e.message || e)
const when = ms => ms ? new Date(ms).toISOString().slice(0, 16).replace('T', ' ') : ''
const kb = n => n > 2048 ? `${Math.round(n / 1024)} KB` : `${n} B`
const pretty = t => { try { return JSON.stringify(JSON.parse(t), null, 1) } catch (e) { return t } }
const session = () => { try { return JSON.parse(sessionStorage.getItem(SESSION) || 'null') } catch (e) { return null } }

export function mountBrowse(root) {
    const st = { vaults: null, pick: 'reader', open: new Set(['/', '/activity']), file: null, commit: null }
    const waitForSession = () => {
        put(root, h('div', { class: 'note', id: 'browse-locked' }, h('p', {}, 'Your vault is not open in this tab. Open it in the pane on the right, with your passkey, and this page opens with it.'),
            h('p', {}, h('button', { type: 'button', class: 'btn', onclick: () => window.dispatchEvent(new CustomEvent('sgit-vault-open', { detail: { tab: 'vault' } })) }, 'Open the vault pane'))))
    }
    window.addEventListener('sgit-vault-session', () => { if (!st.vaults) start() })
    async function start() {
        const rec = session(); if (!rec || !rec.door) return waitForSession()
        put(root, h('p', { class: 'dim', id: 'browse-opening' }, 'Opening your door, master, reader vault and lane, here in this page…'))
        try {
            await loadLibrary()
            const sg = NV.client({ endpoint: ENDPOINT, token: rec.token || '' })
            const u = await NV.unlock({ sgSend: sg, door: rec.door })
            let lane = null; try { const L = await NV.openLane({ sgSend: sg, master: u.master }); lane = L && L.lane } catch (e) { lane = null }
            st.vaults = { reader: u.reader, lane, master: u.master, door: u.door }
            draw()
        } catch (e) { put(root, h('p', { class: 'warn' }, `Your vaults could not be opened here: ${err(e)}`)) }
    }
    const NAMES = { reader: ['Reader vault', 'your reads, notes and devices, one file per device'], lane: ['The lane', 'the notes you sent to the newsroom'],
                    master: ['Master vault', 'the keys of the others: opens behind Reveal'], door: ['This door', 'the master’s key: opens behind Reveal'] }
    const secret = () => st.pick === 'master' || st.pick === 'door'

    function draw() {
        const v = st.vaults[st.pick]
        const tabs = h('div', { class: 'browse-tabs', role: 'tablist' }, ...Object.keys(NAMES).filter(k => st.vaults[k]).map(k =>
            h('button', { type: 'button', role: 'tab', class: 'browse-tab', id: `browse-${k}`, 'aria-selected': String(k === st.pick), onclick: () => { st.pick = k; st.file = null; st.commit = null; draw() } },
                h('b', {}, NAMES[k][0]), h('span', { class: 'mono' }, st.vaults[k].vaultId || st.vaults[k]._vaultId))))
        const files = h('div', { class: 'browse-files', id: 'browse-files' }, h('p', { class: 'dim' }, 'Reading the tree…'))
        const view = h('div', { class: 'browse-view', id: 'browse-view' }, h('p', { class: 'dim' }, 'Pick a file to see what is in it.'))
        const hist = h('div', { class: 'browse-history', id: 'browse-history' }, h('p', { class: 'dim' }, 'Reading the commits…'))
        put(root, tabs, h('p', { class: 'dim' }, NAMES[st.pick][1] + '.'),
            h('div', { class: 'browse-grid' }, h('section', {}, h('h3', {}, st.commit ? `Files at ${st.commit.id.slice(0, 20)}…` : 'Files, as published now'), files), h('section', {}, h('h3', {}, 'The file'), view), h('section', {}, h('h3', {}, 'Commits'), hist)),
            st.pick === 'reader' ? appSection() : null)
        drawFiles(v, files, view); drawHistory(v, hist, files, view)
    }

    /** The tree: folders open on click; a file opens in the view. At a commit, the tree as it was. */
    async function drawFiles(v, box, view) {
        try {
            const walk = async (path, depth) => {
                const out = []
                let entries
                if (st.commit) entries = (await v.listTreeAt(st.commit.id, path.replace(/^\//, ''))).map(e => ({ name: e.name, type: e.dir ? 'folder' : 'file', size: e.size }))
                else { await NV.ensureLoaded(v, path); entries = v.listFolder(path) || [] }
                entries.sort((a, b) => (a.type === b.type ? a.name.localeCompare(b.name) : a.type === 'folder' ? -1 : 1))
                for (const e of entries) {
                    const full = (path === '/' ? '' : path) + '/' + e.name
                    if (e.type === 'folder') {
                        const isOpen = st.open.has(full)
                        out.push(h('li', { class: 'folder', style: `padding-left:${depth * .9}rem` }, h('button', { type: 'button', class: 'tree-btn', 'data-path': full, onclick: () => { if (isOpen) st.open.delete(full); else st.open.add(full); drawFiles(v, box, view) } }, `${isOpen ? '▾' : '▸'} ${e.name}/`)))
                        if (isOpen) out.push(...await walk(full, depth + 1))
                    } else {
                        out.push(h('li', { class: 'file' + (st.file === full ? ' on' : ''), style: `padding-left:${depth * .9}rem` }, h('button', { type: 'button', class: 'tree-btn', 'data-path': full, onclick: () => { st.file = full; drawFiles(v, box, view); showFile(v, full, view) } }, e.name), h('span', { class: 'dim' }, ' ' + kb(e.size || 0))))
                    }
                }
                return out
            }
            const items = await walk('/', 0)
            put(box, items.length ? h('ul', { class: 'tree' }, ...items) : h('p', { class: 'dim' }, 'This vault is empty.'), st.commit ? h('p', {}, h('button', { type: 'button', class: 'btn', onclick: () => { st.commit = null; st.file = null; draw() } }, 'Back to now')) : null)
        } catch (e) { put(box, h('p', { class: 'warn' }, `The tree could not be read: ${err(e)}`)) }
    }

    async function showFile(v, path, view) {
        put(view, h('p', { class: 'dim' }, `Opening ${path}…`))
        try {
            const parts = path.split('/').filter(Boolean), name = parts.pop(), folder = '/' + parts.join('/')
            const bytes = st.commit ? new Uint8Array(await v.readFileAt(st.commit.id, path.replace(/^\//, ''))) : new Uint8Array(await v.getFile(folder, name))
            let text = null; try { text = new TextDecoder('utf-8', { fatal: true }).decode(bytes) } catch (e) { text = null }
            const pre = h('pre', { class: 'browse-pre', id: 'browse-content' }, text == null ? `${bytes.length} bytes, not text` : pretty(text).slice(0, 200000))
            const head = h('p', {}, h('b', { class: 'mono' }, path), h('span', { class: 'dim' }, ` · ${kb(bytes.length)}${st.commit ? ' · at ' + st.commit.id.slice(0, 20) + '…' : ''}`))
            const what = /\.link\.json$/.test(name) ? h('p', { class: 'dim' }, 'A link to another vault: the vault app shows it as a folder, read-only, with the key in .vault/owner/ro-links.json.') : null
            if (secret()) put(view, head, h('p', { class: 'warn' }, 'This vault holds keys. A key opens a vault to whoever holds it.'), h('button', { type: 'button', class: 'btn', id: 'browse-reveal', onclick: () => put(view, head, pre) }, 'Reveal'))
            else put(view, head, what, pre)
        } catch (e) { put(view, h('p', { class: 'warn' }, `It could not be read: ${err(e)}`)) }
    }

    async function drawHistory(v, box, files, view) {
        try {
            const log = await v.logCommits({ limit: 40 })
            put(box, h('ol', { class: 'commits', id: 'browse-commits' }, ...log.map(c => h('li', { class: st.commit && st.commit.id === c.id ? 'on' : '' },
                h('button', { type: 'button', class: 'tree-btn', 'data-commit': c.id, onclick: () => { st.commit = c; st.file = null; draw() } }, c.message || '(no message)'),
                h('span', { class: 'dim' }, ` ${when(c.timestamp_ms)} · `), h('span', { class: 'mono dim' }, c.id.slice(0, 20))))),
                log.length >= 40 ? h('p', { class: 'dim' }, 'The latest 40.') : null)
        } catch (e) { put(box, h('p', { class: 'warn' }, `The commits could not be read: ${err(e)}`)) }
    }

    /** The reader vault in the SG/Vault app: its read key handed over the embed protocol, on a press. */
    function appSection() {
        const host = h('div', { class: 'sgv-host', id: 'browse-embed' })
        const go = app => async () => {
            const v = st.vaults.reader, hex = await NV.readKeyHex(v)
            host.replaceChildren()
            const id = v.vaultId || v._vaultId
            if (app) await mountEmbed(host, { vaultId: id, readKeyHex: hex, mode: 'app' }).done
            mountEmbed(host, { vaultId: id, readKeyHex: hex, mode: 'vault' })
        }
        return h('section', { class: 'browse-app' }, h('h3', {}, 'In the SG/Vault app'),
            h('p', { class: 'dim' }, 'The same reader vault, opened by the SG/Vault app at dev.vault.sgraph.ai. A press hands it this vault’s READ key, over its embed protocol: never in an address, never stored, and it cannot write. App Mode opens the vault with its app, the newsroom’s shared viewer, once the vault links it (the next Update does that); the vault browser shows its files, its SGit history and its settings.'),
            h('div', { class: 'acts' }, h('button', { type: 'button', class: 'btn primary', id: 'browse-open-app', onclick: go(true) }, 'Open it in the SG/Vault app'), h('button', { type: 'button', class: 'btn', id: 'browse-open-files', onclick: go(false) }, 'The vault browser only')),
            host)
    }

    start()
}
