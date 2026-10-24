/**
 * pen.js: the Pen, a panel for what a reader does with a page (card 090). Loaded by the nav on every page that
 * carries the meter, beside the vault pane, the reading strip and highlights; it runs where the page is charged
 * (the articles, issues, notes and collections), where those run.
 *
 * Reading has three moments: you read, you mark the page, and you process what you marked ("Reading with a pen").
 * The site had the first and pieces of the second (highlights, the vault pane's notes); the Pen puts the second and
 * the start of the third in one place, on the right, open while reading:
 *
 *   Capture   what is selected in the article, kept the moment it is selected, so a tap on a phone or an iPad (where
 *             the system's Copy and Look Up menu sits over the selection) never loses it. A bar at the foot of the
 *             window offers Keep, Comment and Tell the newsroom while something is selected.
 *   Mine      the marks on this page, private: highlights (sgit.highlights.v1, drawn by assets/reader/highlights.js)
 *             with a comment of the reader's own. Never sent anywhere.
 *   The newsroom   notes about this page for the newsroom: fix this, wrong, idea, liked, or words alone, with the
 *             passage they are about. They are the vault pane's own records (assets/vault-pane/notes.js), so they
 *             travel with the reader's vault and go to the newsroom down the reader's lane when they press Send.
 *   Signed    with a key, a note is signed by this browser (assets/pen/identity.js), and the newsroom can check that
 *             against pki.sgit.ai's public register: a key its owner vouches for, judged from a pinned root.
 *
 * Everything from the page or a note is written with textContent. Nothing here talks to a server except the GET of
 * the public register when the Signed section is opened.
 */
import * as N from '../vault-pane/notes.js'

const tag = document.querySelector('sg-meter[view="page"]')
const main = document.querySelector('main')
if (tag && tag.getAttribute('kind') && tag.getAttribute('kind') !== 'free' && main) start()

function start() {
    const HL = 'sgit.highlights.v1', OPEN = 'sgit.pen.open', CTX = 32, MIN = 3, MAX = 600
    const path = location.pathname.replace(/index\.html$/, '') || '/'
    const title = ((main.querySelector('h1') || {}).textContent || document.title).trim()
    const number = (() => { for (const p of document.querySelectorAll('p.small')) { const m = /Article No\. (\d+)/.exec(p.textContent || ''); if (m) return Number(m[1]) } return null })()
    const stop = main.querySelector(':scope > sg-meter, :scope > section.athreads, :scope > .athreads, :scope > .agent')
    const KINDS = [['fix', 'Fix this'], ['wrong', 'Wrong'], ['idea', 'Idea'], ['liked', 'Liked'], ['note', 'Just words']]
    let ident = null, identMod = null                         // loaded on first use: the vendored key code is not small

    // ------------------------------------------------------------ small helpers
    const h = (t, a, ...kids) => {
        const el = document.createElement(t)
        for (const [k, v] of Object.entries(a || {})) { if (v == null || v === false) continue; if (k.startsWith('on')) el.addEventListener(k.slice(2), v); else el.setAttribute(k, v === true ? '' : v) }
        for (const k of kids.flat()) if (k != null && k !== false) el.append(k instanceof Node ? k : String(k))
        return el
    }
    // replaceChildren() writes a null as the text "null"; the parts below leave out what does not apply as null
    const put = (el, ...kids) => el.replaceChildren(...kids.flat().filter(k => k != null && k !== false))
    const clip = (s, n) => { s = String(s || ''); return s.length > n ? s.slice(0, n - 1) + '…' : s }
    const when = iso => { try { return new Date(iso).toLocaleString('en-GB', { day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit' }) } catch (e) { return iso } }
    function inArticle(node) {
        const el = node && (node.nodeType === 1 ? node : node.parentElement)
        if (!el || !main.contains(el)) return false
        if (el.closest('.read-map, .read-chip, .hl-btn, .vault-pane, .pen, .pen-bar, .agent, sg-meter, .athreads, nav, footer')) return false
        if (stop && (stop === el || (stop.compareDocumentPosition(el) & Node.DOCUMENT_POSITION_FOLLOWING))) return false
        return true
    }
    function textIndex() {
        const nodes = []; let text = ''
        const w = document.createTreeWalker(main, NodeFilter.SHOW_TEXT, { acceptNode: n => inArticle(n) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT })
        for (let n = w.nextNode(); n; n = w.nextNode()) { nodes.push({ node: n, start: text.length }); text += n.data }
        return { text, nodes }
    }
    const offsetOf = (ix, node, off) => { const x = ix.nodes.find(e => e.node === node); return x ? x.start + off : -1 }
    const hlRead = () => { try { const s = JSON.parse(localStorage.getItem(HL) || 'null'); if (s && Array.isArray(s.items)) return s } catch (e) { /* fall through */ } return { v: 1, items: [] } }
    const hlWrite = s => {
        try { localStorage.setItem(HL, JSON.stringify(s)) } catch (e) { /* private window */ }
        try { window.dispatchEvent(new CustomEvent('sgit-highlights', { detail: { path } })) } catch (e) { /* old browser */ }
        if (window.SgitHighlights) window.SgitHighlights.draw()
    }
    const marks = () => hlRead().items.filter(x => x.path === path)
    const notesHere = () => N.forPage(path).filter(x => !x.story)

    // ------------------------------------------------------------ the selection, kept as soon as it is made
    let sel = null                                               // { exact, prefix, suffix, section, range }
    let selWait = 0
    document.addEventListener('selectionchange', () => { clearTimeout(selWait); selWait = setTimeout(readSelection, 160) })
    function readSelection() {
        const s = document.getSelection()
        if (!s || s.isCollapsed || !s.rangeCount) { if (!bar.matches(':hover')) hideBar(); return }
        const r = s.getRangeAt(0), t = s.toString().replace(/\s+/g, ' ').trim()
        if (t.length < MIN || t.length > MAX || !inArticle(r.startContainer) || !inArticle(r.endContainer)) return
        const ix = textIndex(), a = offsetOf(ix, r.startContainer, r.startOffset), b = offsetOf(ix, r.endContainer, r.endOffset)
        if (a < 0 || b <= a) return
        sel = { exact: ix.text.slice(a, b), prefix: ix.text.slice(Math.max(0, a - CTX), a), suffix: ix.text.slice(b, b + CTX),
                section: window.SgitReading && window.SgitReading.sectionOf ? window.SgitReading.sectionOf(r.startContainer) : '', range: r.cloneRange() }
        showBar()
        if (isOpen()) drawCapture()
    }
    const clearSelection = () => { sel = null; try { document.getSelection().removeAllRanges() } catch (e) { /* fine */ } hideBar(); if (isOpen()) drawCapture() }

    // ------------------------------------------------------------ the bar at the foot, while something is selected
    // At the foot, not beside the words: on an iPad the system's own menu sits over the selection, and covers anything there.
    const bar = h('div', { class: 'pen-bar', role: 'toolbar', 'aria-label': 'What to do with the selected words', hidden: true },
        h('span', { class: 'pen-bar-mark', 'aria-hidden': 'true' }, '✎'),
        h('button', { type: 'button', onclick: () => keepMark('') }, 'Keep'),
        h('button', { type: 'button', onclick: () => { open(); focusComment() } }, 'Comment'),
        h('button', { type: 'button', onclick: () => { open(); focusNewsroom() } }, 'Tell the newsroom'),
        h('button', { type: 'button', class: 'pen-x', 'aria-label': 'Close', onclick: clearSelection }, '×'))
    for (const b of bar.querySelectorAll('button')) b.addEventListener('mousedown', e => e.preventDefault())   // keep the selection on a click
    document.body.append(bar)
    function showBar() { bar.hidden = false }
    function hideBar() { bar.hidden = true }

    // ------------------------------------------------------------ the button in the bar of the site, and the panel
    const btn = h('button', { type: 'button', class: 'pen-btn', 'aria-expanded': 'false', title: 'The Pen: mark this page, comment on it, and tell the newsroom' },
        h('span', { class: 'pen-ico', 'aria-hidden': 'true' }, '✎'), 'Pen', h('span', { class: 'n', hidden: true }))
    const tools = document.querySelector('nav.site .nav-tools')
    const vaultBtn = tools && tools.querySelector('.vault-btn')
    if (tools) tools.insertBefore(btn, vaultBtn || tools.querySelector('.theme-pick'))
    const panel = h('aside', { class: 'pen', 'aria-label': 'The Pen: this page', hidden: true })
    document.body.append(panel)
    btn.addEventListener('click', () => isOpen() ? close() : open())
    document.addEventListener('keydown', e => { if (e.key === 'Escape' && isOpen()) close() })
    const isOpen = () => !panel.hidden
    function open() { panel.hidden = false; btn.setAttribute('aria-expanded', 'true'); document.documentElement.classList.add('pen-open'); try { sessionStorage.setItem(OPEN, '1') } catch (e) { /* fine */ } draw() }
    function close() { panel.hidden = true; btn.setAttribute('aria-expanded', 'false'); document.documentElement.classList.remove('pen-open'); try { sessionStorage.removeItem(OPEN) } catch (e) { /* fine */ } }
    function count() { const n = marks().length + notesHere().length; const c = btn.querySelector('.n'); c.textContent = String(n); c.hidden = !n }

    const parts = { capture: h('section', { class: 'pen-sec' }), mine: h('section', { class: 'pen-sec' }), news: h('section', { class: 'pen-sec' }), signed: h('section', { class: 'pen-sec pen-signed' }) }
    panel.append(
        h('header', { class: 'pen-head' },
            h('div', {}, h('p', { class: 'pen-kicker' }, '✎ The Pen'), h('p', { class: 'pen-title' }, clip(title, 110))),
            h('button', { type: 'button', class: 'pen-close', 'aria-label': 'Close the Pen', onclick: close }, '×')),
        parts.capture, parts.mine, parts.news, parts.signed,
        h('p', { class: 'pen-foot' }, 'Your marks stay in this browser. Notes for the newsroom go only when you send them, down your own lane. ',
            h('a', { href: new URL('articles/reading-with-a-pen.html', document.documentElement.dataset.root ? new URL(document.documentElement.dataset.root, location.href) : location.href).href }, 'Why a pen'), '.'))

    function draw() { drawCapture(); drawMine(); drawNews(); drawSigned(); count() }

    // ------------------------------------------------------------ capture
    function drawCapture() {
        put(parts.capture, 
            h('h3', {}, 'Selected'),
            sel ? h('blockquote', { class: 'pen-quote' }, clip(sel.exact, 280)) : h('p', { class: 'pen-hint' }, 'Select words in the article and they appear here. On an iPad or a phone, select, then use the ✎ bar at the foot of the screen.'),
            sel ? h('div', { class: 'pen-acts' },
                h('button', { type: 'button', class: 'pen-b primary', onclick: () => keepMark('') }, 'Keep it'),
                h('button', { type: 'button', class: 'pen-b', onclick: focusComment }, 'Keep, with a comment'),
                h('button', { type: 'button', class: 'pen-b', onclick: focusNewsroom }, 'Tell the newsroom'),
                h('button', { type: 'button', class: 'pen-b ghost', onclick: clearSelection }, 'Clear')) : null)
    }
    function keepMark(comment) {
        if (!sel) return null
        const m = { id: Date.now().toString(36) + Math.random().toString(36).slice(2, 6), at: new Date().toISOString(), path, title,
                    exact: sel.exact, prefix: sel.prefix, suffix: sel.suffix, section: sel.section || '', note: String(comment || '').trim(), by: 'pen' }
        const s = hlRead(); s.items.push(m); hlWrite(s)
        clearSelection(); draw()
        return m
    }
    function focusComment() {
        if (!sel) return
        const m = keepMark('')
        draw()
        const ta = parts.mine.querySelector(`textarea[data-id="${m.id}"]`)
        if (ta) { ta.scrollIntoView({ block: 'nearest' }); ta.focus() }
    }
    function focusNewsroom() {
        if (sel) composeQuote = sel.exact
        drawNews()
        const ta = parts.news.querySelector('textarea')
        if (ta) { parts.news.scrollIntoView({ block: 'nearest' }); ta.focus() }
    }

    // ------------------------------------------------------------ mine: the marks, private
    function goTo(m) {
        if (!window.CSS || !main) return
        const ix = textIndex(); let at = ix.text.indexOf(m.exact)
        if (m.prefix) { const p = ix.text.indexOf(m.prefix + m.exact); if (p >= 0) at = p + m.prefix.length }
        if (at < 0) return
        const node = ix.nodes.filter(x => x.start <= at).pop()
        if (node && node.node.parentElement) node.node.parentElement.scrollIntoView({ behavior: 'smooth', block: 'center' })
    }
    function drawMine() {
        const ms = marks()
        put(parts.mine, 
            h('h3', {}, 'Your marks on this page ', h('span', { class: 'pen-tag' }, 'private')),
            ms.length ? h('ol', { class: 'pen-list' }, ms.map(m => h('li', {},
                h('blockquote', { class: 'pen-quote', onclick: () => goTo(m), title: 'Go to it' }, clip(m.exact, 240)),
                h('textarea', { 'data-id': m.id, rows: '2', placeholder: 'A comment of your own: only you see it', onchange: ev => { const s = hlRead(); const x = s.items.find(i => i.id === m.id); if (x) { x.note = ev.target.value.trim(); hlWrite(s) } } }, m.note || ''),
                h('div', { class: 'pen-acts' },
                    h('button', { type: 'button', class: 'pen-b sm', onclick: () => goTo(m) }, 'Go to it'),
                    h('button', { type: 'button', class: 'pen-b sm', onclick: () => { composeQuote = m.exact; composeText = m.note || ''; drawNews(); focusNewsroom() } }, 'Tell the newsroom'),
                    h('button', { type: 'button', class: 'pen-b sm ghost', onclick: () => { const s = hlRead(); s.items = s.items.filter(i => i.id !== m.id); hlWrite(s); draw() } }, 'Remove')))))
                : h('p', { class: 'pen-hint' }, 'Nothing marked yet. A mark is a highlight on the page, with a comment if you want one; it stays in this browser.'))
    }

    // ------------------------------------------------------------ the newsroom: notes, with the passage, signed when there is a key
    let composeQuote = '', composeText = '', composeKind = 'fix'
    function drawNews() {
        const ns = notesHere()
        const waiting = ns.filter(x => !x.sent && !x.device)
        const ta = h('textarea', { rows: '3', placeholder: 'What should the newsroom know about this page?', oninput: ev => { composeText = ev.target.value } }, composeText)
        const kinds = h('div', { class: 'pen-kinds', role: 'radiogroup', 'aria-label': 'What kind of note' },
            KINDS.map(([k, label]) => h('button', { type: 'button', role: 'radio', 'aria-checked': k === composeKind ? 'true' : 'false', class: 'pen-chip', onclick: () => { composeKind = k; drawNews() } }, label)))
        put(parts.news, 
            h('h3', {}, 'Tell the newsroom'),
            kinds,
            composeQuote ? h('div', { class: 'pen-about' }, h('span', {}, 'About: '), h('q', {}, clip(composeQuote, 200)), h('button', { type: 'button', class: 'pen-x', 'aria-label': 'Not about a passage', onclick: () => { composeQuote = ''; drawNews() } }, '×')) : null,
            ta,
            h('div', { class: 'pen-acts' },
                h('button', { type: 'button', class: 'pen-b primary', onclick: keepNote }, ident ? 'Keep, signed' : 'Keep for the newsroom'),
                waiting.length ? h('button', { type: 'button', class: 'pen-b', onclick: sendNow }, `Send ${waiting.length} now`) : null),
            ns.length ? h('ol', { class: 'pen-list pen-notes' }, ns.map(x => h('li', {},
                h('p', { class: 'pen-meta' }, h('b', {}, N.kindLabel(x.kind)), ` · ${when(x.at)} · `, x.sent ? h('span', { class: 'ok' }, 'sent') : 'not sent yet', x.signed ? h('span', { class: 'pen-sig', title: `signed by ${x.signed.signer}` }, ' · signed') : null),
                x.quote ? h('q', {}, clip(x.quote, 200)) : null,
                x.text ? h('p', {}, x.text) : null,
                x.sent ? null : h('button', { type: 'button', class: 'pen-b sm ghost', onclick: () => { N.remove(x.id); draw() } }, 'Remove')))) : null,
            h('p', { class: 'pen-hint' }, 'Kept here and in your vault; sent to the newsroom, down your own lane, when you press Send. With a key (below), each note is signed as you.'))
    }
    async function keepNote() {
        const text = composeText.trim()
        if (!text && !composeQuote && composeKind === 'note') return
        const rec = N.keep({ kind: composeKind, text, quote: composeQuote, path, title, n: number })
        if (!rec) return
        if (ident) {
            try {
                const signed = await identMod.sign(rec, ident)
                const store = N.read(); const x = store.notes.find(n => n.id === rec.id)
                if (x && signed) { x.signed = signed; N.write(store) }
            } catch (e) { /* kept unsigned; said below */ }
        }
        const fromSelection = sel && composeQuote && composeQuote === sel.exact
        composeText = ''; composeQuote = ''
        if (fromSelection) clearSelection()
        draw()
    }
    function sendNow() {
        // the lane, the vault and the send are the vault pane's; open it where it sends
        try { window.dispatchEvent(new CustomEvent('sgit-vault-open', { detail: { tab: 'page' } })) } catch (e) { /* fine */ }
    }

    // ------------------------------------------------------------ signed: who holds the pen
    let regState = null                                          // { loading } | { st } | { error }
    async function loadIdentity() {
        if (!identMod) identMod = await import('./identity.js')
        ident = identMod.load()
        return identMod
    }
    function drawSigned() {
        const fp = ident && identMod.fingerprintOf(ident)
        const head = h('h3', {}, 'Signed as you')
        if (!identMod) {
            put(parts.signed, head, h('p', { class: 'pen-hint' }, 'Notes are sent unsigned. A key for this browser, vouched for by your key on pki.sgit.ai, signs each note as yours.'),
                h('div', { class: 'pen-acts' }, h('button', { type: 'button', class: 'pen-b', onclick: async () => { await loadIdentity(); drawSigned(); drawNews(); checkRegister() } }, 'Show the key')))
            return
        }
        if (!ident) {
            const name = h('input', { type: 'text', value: '', placeholder: 'Your name, as on pki.sgit.ai', 'aria-label': 'Your name' })
            const dev = h('input', { type: 'text', value: deviceGuess(), 'aria-label': 'This browser' })
            const op = h('input', { type: 'text', value: identMod.ROOT, class: 'mono', 'aria-label': 'Your fingerprint on pki.sgit.ai' })
            const msg = h('p', { class: 'pen-hint' })
            put(parts.signed, head,
                h('p', { class: 'pen-hint' }, 'This browser has no key. Make one here: it is a key pair of this browser\'s own, and it counts as yours once your key on pki.sgit.ai says it operates it, with an end date.'),
                h('label', { class: 'pen-f' }, 'Your name', name), h('label', { class: 'pen-f' }, 'This browser', dev), h('label', { class: 'pen-f' }, 'Your fingerprint on pki.sgit.ai', op),
                h('div', { class: 'pen-acts' }, h('button', { type: 'button', class: 'pen-b primary', onclick: async ev => {
                    if (!name.value.trim()) { msg.textContent = 'A name first.'; return }
                    ev.target.disabled = true; msg.textContent = 'Making the key: a few seconds…'
                    try { ident = await identMod.make({ name: name.value, device: dev.value, operator: op.value.trim() }); regState = null; drawSigned(); drawNews(); checkRegister() }
                    catch (e) { msg.textContent = 'Could not make the key: ' + (e.message || e); ev.target.disabled = false }
                } }, 'Make this browser\'s key')), msg)
            return
        }
        const sub = JSON.stringify(identMod.submission(ident), null, 1)
        const st = regState && regState.st
        put(parts.signed, head,
            h('p', {}, h('b', {}, ident.bundle.label), h('br'), h('span', { class: 'mono' }, fp)),
            h('p', { class: `pen-standing ${st ? (st.ok ? 'ok' : 'wait') : ''}` },
                !regState ? 'Not checked yet.' : regState.loading ? 'Reading the register at pki.sgit.ai…' : regState.error ? `The register could not be read: ${regState.error}` :
                st.ok ? `Your notes are signed as you: ${st.text}.` : `Not vouched for yet: ${st.text}.`),
            st && !st.ok ? h('ol', { class: 'pen-steps' },
                h('li', {}, 'Send the submission below to pki.sgit.ai, so the register holds this browser\'s record.'),
                h('li', {}, `On pki.sgit.ai, from your own key, link to ${fp} with "operates" and an end date.`),
                h('li', {}, 'Check again here.')) : null,
            h('details', { class: 'pen-sub' }, h('summary', {}, 'The submission for the register'), h('textarea', { readonly: true, rows: '6', class: 'mono' }, sub),
                h('div', { class: 'pen-acts' }, h('button', { type: 'button', class: 'pen-b sm', onclick: () => copy(sub) }, 'Copy'), h('a', { class: 'pen-b sm', href: identMod.keyLink(ident), target: '_blank', rel: 'noopener' }, 'This key on pki.sgit.ai'))),
            h('div', { class: 'pen-acts' },
                h('button', { type: 'button', class: 'pen-b sm', onclick: () => checkRegister(true) }, 'Check the register'),
                h('button', { type: 'button', class: 'pen-b sm ghost', onclick: () => { if (confirm('Forget this browser\'s key? Notes already signed keep their signatures.')) { identMod.forget(); ident = null; regState = null; drawSigned(); drawNews() } } }, 'Forget the key')))
    }
    async function checkRegister(fresh = false) {
        if (!ident) return
        regState = { loading: true }; drawSigned()
        try { regState = { st: await identMod.standing(identMod.fingerprintOf(ident), await identMod.register({ fresh })) } }
        catch (e) { regState = { error: e.message || String(e) } }
        drawSigned()
    }
    const copy = text => { try { navigator.clipboard.writeText(text) } catch (e) { /* fine */ } }
    function deviceGuess() {
        const ua = navigator.userAgent
        const os = /iPad/.test(ua) || (/Macintosh/.test(ua) && navigator.maxTouchPoints > 1) ? 'iPad' : /iPhone/.test(ua) ? 'iPhone' : /Android/.test(ua) ? 'Android' : /Mac/.test(ua) ? 'Mac' : /Windows/.test(ua) ? 'Windows' : 'Linux'
        const br = /Firefox\//.test(ua) ? 'Firefox' : /Edg\//.test(ua) ? 'Edge' : /Chrome\//.test(ua) ? 'Chrome' : /Safari\//.test(ua) ? 'Safari' : 'a browser'
        return `${br} on ${os}`
    }

    // ------------------------------------------------------------ keeping up
    window.addEventListener(N.EVENT, () => { if (isOpen()) { drawNews() } count() })
    window.addEventListener('storage', e => { if (e.key === HL || e.key === N.STORE) { if (isOpen()) draw(); else count() } })
    if (localStorage.getItem('sgit.pen.identity.v1')) loadIdentity().then(() => { if (isOpen()) { drawSigned(); drawNews() } }).catch(() => {})
    count()
    try { if (sessionStorage.getItem(OPEN) === '1') open() } catch (e) { /* fine */ }
    window.SgitPen = { open, close, selection: () => sel && sel.exact, keepMark, keepNote: async (kind, text, quote) => { composeKind = kind; composeText = text || ''; composeQuote = quote || ''; await keepNote() } }
}
