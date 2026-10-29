/**
 * send.js: the review lane's send page, reviews/send.html (card 091). A reviewer outside the newsroom (ChatGPT,
 * Perplexity, or whoever reads their answer) pastes what the reviewer wrote; the page finds the review records in it
 * (assets/reviews/record.js), checks each against the criteria, the site's status.json and the article's current
 * text, and sends the good ones: sealed here to the lane's public key (sgit's hybrid v2 envelope,
 * assets/vault-pane/inbox.js) and appended to the lane, which this browser can write to and never read.
 *
 * The link is https://newsroom.sgit.ai/reviews/send.html#rv1.<vault id>.<append token>.<public key, SPKI, base64url>.
 * The page remembers it in this browser (localStorage sgit.reviews.link) and takes it out of the address, so that a
 * screenshot or a shared tab does not carry it. The newsroom drains the lane with admin/build/review_lane.mjs.
 *
 * @module review-send
 */
import * as I from '../vault-pane/inbox.js'
import * as R from './record.js'

export const LINK = 'sgit.reviews.link', FROM = 'sgit.reviews.from'
const ls = { get(k) { try { return localStorage.getItem(k) } catch (e) { return null } }, set(k, v) { try { localStorage.setItem(k, v) } catch (e) { /* fine */ } }, del(k) { try { localStorage.removeItem(k) } catch (e) { /* fine */ } } }

/** The link in text (a URL, a fragment, or the code alone): { vault, token, spki, code } or null. */
export function parseLink(text) {
    const m = /rv1\.([a-z0-9]{4,24})\.([0-9a-f]{16,128})\.([A-Za-z0-9_-]{200,3000})/.exec(String(text || ''))
    if (!m) return null
    try { return { vault: m[1], token: m[2], spki: I.unb64url(m[3]), code: m[0] } } catch (e) { return null }
}

/** An article's markdown as a reader sees the words: links, emphasis and figure lines reduced to their text. */
export function plain(md) {
    return String(md || '').replace(/^---[\s\S]*?\n---\n/, '').replace(/^!shot .*$/gm, '').replace(/\{#[a-z0-9-]+\}/g, '')
        .replace(/!\[[^\]]*\]\([^)]*\)/g, '').replace(/\[([^\]]+)\]\([^)\s]+\)/g, '$1').replace(/\*\*|__/g, '').replace(/(^|[^*\w])\*([^*\n]+)\*/g, '$1$2').replace(/`/g, '')
}

/** Check what was pasted: [{ record, errors, warnings }], plus how many candidates could not be read. */
export async function checkText(text, { root = '../', fetcher = fetch } = {}) {
    const { records, unreadable } = R.extract(text)
    let status = null
    try { status = await (await fetcher(root + 'reviews/status.json', { cache: 'no-store' })).json() } catch (e) { /* checked again when drained */ }
    const out = []
    const seen = new Set()
    for (const r of records) {
        let art = null
        if (R.SLUG.test(String(r.slug || ''))) { try { const res = await fetcher(root + `articles/${r.slug}.md`); if (res.ok) art = plain(await res.text()) } catch (e) { /* no text check */ } }
        const p = R.problems(r, status, art)
        const k = `${r.reviewer}|${r.slug}`
        if (seen.has(k)) p.errors.push('the same reviewer and article twice in what was pasted')
        seen.add(k)
        if (!status) p.warnings.push('the site\'s status.json could not be read: the article and duplicate checks are left to the newsroom')
        out.push({ record: r, ...p })
    }
    return { items: out, unreadable }
}

/** Seal the records to the link's key and append them as one message. Returns { fingerprint, count }. */
export async function send(link, records, { text = '', from = '' } = {}) {
    if (!globalThis.crypto || !crypto.subtle) throw new Error('this browser cannot encrypt here')
    const fp = await I.fingerprint(link.spki)
    const msg = R.message({ records, text, to: fp, from, via: 'reviews/send.html' })
    const { payload } = await I.seal(link.spki, JSON.stringify(msg))
    await I.append(link, payload)
    return { fingerprint: fp, count: records.length }
}

// ------------------------------------------------------------ the page
const h = (tag, attrs, ...kids) => {
    const el = document.createElement(tag)
    for (const [k, v] of Object.entries(attrs || {})) { if (v === false || v == null) continue; if (k.startsWith('on')) el.addEventListener(k.slice(2), v); else el.setAttribute(k, v === true ? '' : v) }
    for (const kid of kids.flat()) if (kid != null && kid !== false) el.append(kid instanceof Node ? kid : String(kid))
    return el
}

export async function mountSend(box) {
    const fromUrl = parseLink(location.hash)
    if (fromUrl) { ls.set(LINK, fromUrl.code); history.replaceState(null, '', location.pathname + location.search) }
    let link = parseLink(ls.get(LINK) || '')
    box.replaceChildren()
    if (!link) {
        const inp = h('input', { type: 'text', id: 'rv-link', placeholder: 'https://newsroom.sgit.ai/reviews/send.html#rv1…', autocomplete: 'off' })
        box.append(h('p', null, 'This page sends reviews to the newsroom through its review lane, and needs the lane\'s link, which the editor gives each reviewer. Paste it here:'),
            h('label', { for: 'rv-link' }, 'The send link'), inp,
            h('div', { class: 'acts' }, h('button', { class: 'btn primary', type: 'button', onclick: () => {
                const l = parseLink(inp.value)
                if (!l) { inp.setCustomValidity('not a review lane link'); inp.reportValidity(); return }
                ls.set(LINK, l.code); mountSend(box)
            } }, 'Use this link')))
        return
    }
    const fp = await I.fingerprint(link.spki)
    const ta = h('textarea', { id: 'rv-text', rows: '14', placeholder: 'Paste the reviewer\'s whole answer: the records, in fenced json blocks or not.' })
    const from = h('input', { type: 'text', id: 'rv-from', value: ls.get(FROM) || '', placeholder: 'Your name, or the reviewer\'s run (optional)' })
    const result = h('div', { id: 'rv-result', 'aria-live': 'polite' })
    const sendBtn = h('button', { class: 'btn primary', type: 'button', id: 'rv-send', disabled: true }, 'Send')
    let good = []
    const check = async () => {
        result.replaceChildren(h('p', { class: 'dim' }, 'Checking…'))
        sendBtn.disabled = true
        const { items, unreadable } = await checkText(ta.value)
        good = items.filter(x => !x.errors.length).map(x => x.record)
        const rows = items.map(x => h('li', { class: x.errors.length ? 'rv-bad' : 'rv-good' },
            h('b', null, `${x.record.slug || '(no slug)'}`), ` by ${x.record.reviewer || '(no reviewer)'}: ${x.record.verdict || '(no verdict)'}, ${(x.record.findings || []).length} finding(s). `,
            x.errors.length ? h('span', { class: 'rv-err' }, 'Will not be sent: ' + x.errors.join('; ') + '.') : h('span', { class: 'ok' }, 'Ready.'),
            x.warnings.length ? h('ul', { class: 'rv-warns' }, x.warnings.map(w => h('li', null, w))) : null))
        result.replaceChildren(
            items.length ? h('ul', { class: 'rv-list' }, rows) : h('p', { class: 'warn' }, 'No review records found in what was pasted: each record is a JSON object with "schema": "newsroom-review/v1".'),
            unreadable ? h('p', { class: 'warn' }, `${unreadable} block(s) mention the schema and are not valid JSON; fix them and check again.`) : null,
            good.length ? h('p', null, `${good.length} of ${items.length} record(s) ready to send.`) : null)
        sendBtn.disabled = !good.length
    }
    sendBtn.addEventListener('click', async () => {
        sendBtn.disabled = true
        ls.set(FROM, from.value.trim())
        try {
            const r = await send(link, good, { text: ta.value, from: from.value.trim() })
            result.append(h('p', { class: 'ok', id: 'rv-sent' }, `Sent: ${r.count} record(s), sealed to ${r.fingerprint}. The newsroom drains the lane on a schedule and puts each review on the record beside its article.`))
        } catch (e) { result.append(h('p', { class: 'warn', id: 'rv-sent' }, 'Not sent: ' + (e.message || e))); sendBtn.disabled = false }
    })
    box.append(
        h('div', { class: 'kv' }, h('span', { class: 'k' }, 'The lane'), h('span', { class: 'v mono' }, `${link.vault}, sealed to ${fp}`)),
        h('label', { for: 'rv-text' }, 'What the reviewer wrote'), ta,
        h('label', { for: 'rv-from' }, 'From'), from,
        h('div', { class: 'acts' }, h('button', { class: 'btn', type: 'button', id: 'rv-check', onclick: check }, 'Check'), sendBtn,
            h('button', { class: 'btn', type: 'button', onclick: () => { ls.del(LINK); mountSend(box) } }, 'Forget the link')),
        result)
    ta.addEventListener('input', () => { sendBtn.disabled = true })
}
