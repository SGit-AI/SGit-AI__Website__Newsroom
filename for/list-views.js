/**
 * list-views.js: a reading list as the recipient sees it, in five views, with what they have read on it.
 *
 * reading-list.js parses the link and makes the list a persona; this draws it. For many people a list in an email
 * is the first page of the newsroom they ever open, so the page says what it is (the side column) and shows the list
 * the way the newsroom already knows it, rather than as a column of links:
 *
 *   Cards      each article as its card picture, its one-line teaser, and a bar of its sections, filled as read
 *   Headlines  one line per article: its headline and its one-liner
 *   Sections   every section of every article as its one-line summary, ticked as it is read; a section is a link
 *   Pictures   the figures of the articles, captioned, grouped by article
 *   Graph      the list as a path: each article with its main ideas, the links between the articles, and the
 *              articles beyond the list that they point to
 *
 * What was read comes from this browser only: the reading strip's records (sgit.reading.v1, section by section), the
 * meter's log (sgit.meter.v1: what each page cost, a page declined) and the reader's notes (sgit.notes.v1, through
 * assets/vault-pane/notes.js: done, read later, not for me), the same records the reader's vault carries between
 * devices. Nothing is fetched about the reader and nothing is sent. The page redraws when another tab reads an
 * article on the list (the storage event), so a reader who reads in a new tab comes back to the list up to date.
 *
 * The data for the views is the site's own, published per article: articles/summaries/<slug>.json (a line per
 * section), articles/graphs/<slug>.json (the ideas, the links, the figures) and articles/cards/<slug>.webp.
 * Everything from the link or the data is written with textContent or as SVG text nodes, never as markup.
 *
 * @module list-views
 */
import { h, titleFor, replyLink } from './reading-list.js'

const SVG = 'http://www.w3.org/2000/svg'
const READ_WPM = 300
export const VIEWS = [
    { id: 'cards', label: 'Cards', about: 'The articles as cards, with what you have read of each' },
    { id: 'headlines', label: 'Headlines', about: 'One line per article' },
    { id: 'sections', label: 'Sections', about: 'Every section as one line, ticked as you read it' },
    { id: 'pictures', label: 'Pictures', about: 'The figures of the articles' },
    { id: 'graph', label: 'Graph', about: 'The list as a path, its ideas and where it leads' },
]
const VIEW_KEY = 'newsroom.list.view'
const DECIDE = [
    { kind: 'done', label: 'Done', title: 'Read it, done with it' },
    { kind: 'read-later', label: 'Later', title: 'Come back to this one' },
    { kind: 'not-for-me', label: 'Not for me', title: 'This one did not need to reach me' },
]

const ls = {
    get(k) { try { return localStorage.getItem(k) } catch (e) { return null } },
    set(k, v) { try { localStorage.setItem(k, v) } catch (e) { /* private window */ } },
    json(k) { try { return JSON.parse(localStorage.getItem(k) || 'null') } catch (e) { return null } },
}
const when = d => { try { return new Date(`${d}T00:00:00Z`).toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric', timeZone: 'UTC' }) } catch (e) { return d } }
const short = t => String(t || '').split(/:\s/)[0]
const clip = (t, n) => t.length > n ? t.slice(0, n - 1).replace(/\s+\S*$/, '') + '…' : t
const pct = x => `${Math.round(x * 100)}%`
const svg = (tag, attrs, ...kids) => {
    const el = document.createElementNS(SVG, tag)
    for (const [k, v] of Object.entries(attrs || {})) if (v != null) el.setAttribute(k, v)
    for (const k of kids.flat()) if (k != null) el.append(k instanceof Node ? k : document.createTextNode(String(k)))
    return el
}

// ------------------------------------------------------------ the data
/** Each article's sections and graph, fetched once; an article whose files fail is shown without them. */
export async function loadExtras(entries, root) {
    const get = u => fetch(u).then(r => r.ok ? r.json() : null).catch(() => null)
    const out = new Map()
    await Promise.all(entries.map(async e => {
        const [sum, graph] = await Promise.all([get(`${root}articles/summaries/${e.slug}.json`), get(`${root}articles/graphs/${e.slug}.json`)])
        out.set(e.slug, { sections: (sum && sum.sections) || [], graph })
    }))
    return out
}

/** The path the strip, the meter and the notes key an article by: its address on this site. */
export const pathOf = (root, slug) => new URL(`${root}articles/${slug}.html`, location.href).pathname

/**
 * What this browser knows about each article on the list: its sections with how much of each was read, the share of
 * the article read (by words), what it cost, and the reader's decision. pure apart from reading local storage.
 */
export function readingOf(entries, extras, root, notes) {
    const strip = (ls.json('sgit.reading.v1') || {}).pages || {}
    let meter = null
    try { const c = JSON.parse(document.getElementById('sg-meter-config').textContent); meter = ls.json(c.storageKey || 'sgit.meter.v1') } catch (e) { meter = ls.json('sgit.meter.v1') }
    const log = (meter && meter.log) || []
    const out = new Map()
    for (const e of entries) {
        const path = pathOf(root, e.slug)
        const rec = strip[path] || null
        const byId = new Map(((rec && rec.sections) || []).map(r => [r.id, r]))
        const secs = ((extras.get(e.slug) || {}).sections || []).map(s => {
            const r = byId.get(s.id)
            const words = (r && r.words) || s.words || 1
            const need = words / READ_WPM * 60000
            const read = r ? Math.min(1, Math.max((r.ms || 0) / need, (r.pw || 0) / words)) : 0
            return { id: s.id, label: s.label, line: s.line, words, read }
        })
        const total = secs.reduce((a, s) => a + s.words, 0)
        // the record's own total when it has no sections to go by (a page read before the sections were kept)
        const read = total && byId.size ? secs.reduce((a, s) => a + s.words * s.read, 0) / total : Math.min(1, (rec && rec.read) || 0)
        const reads = log.filter(x => x.path === path)
        const decision = notes ? notes.decisionFor(path) : null
        const status = decision && decision.kind === 'not-for-me' ? 'aside'
            : decision && decision.kind === 'done' ? 'done'
            : read >= 0.9 ? 'read' : read > 0.02 ? 'reading' : 'unread'
        out.set(e.slug, {
            path, sections: secs, read, status, decision: decision ? decision.kind : null, visits: (rec && rec.visits) || 0,
            cost: Math.round(reads.reduce((a, x) => a + (x.cost || 0), 0) * 10) / 10, declined: reads.some(x => x.declined),
            next: (secs.find(s => s.read < 0.9) || secs[0] || {}).id || 'top',
        })
    }
    return out
}

const STATUS = { unread: 'Not read yet', reading: 'Reading', read: 'Read', done: 'Done', aside: 'Set aside' }
const statusText = r => r.status === 'reading' ? `${pct(r.read)} read` : STATUS[r.status]
const sectionHref = (root, slug, id) => `${root}articles/${slug}.html${id && id !== 'top' ? '#' + encodeURIComponent(id) : ''}`

// ------------------------------------------------------------ small parts
/** A bar of the article's sections, each as wide as its words, filled as far as it was read. */
function sectionBar(r, root, slug, big) {
    if (!r.sections.length) return h('div', { class: 'lv-bar empty' }, h('i', { style: `width:${pct(r.read)}` }))
    return h('div', { class: `lv-bar${big ? ' big' : ''}`, role: 'img', 'aria-label': `${pct(r.read)} of this article read, by section` },
        r.sections.map(s => h('a', {
            class: `lv-seg${s.read >= 0.9 ? ' done' : ''}`, href: sectionHref(root, slug, s.id), style: `flex:${s.words} 1 0`,
            title: `${s.label}: ${s.line || ''} (${pct(s.read)} read)`,
        }, h('i', { style: `width:${pct(s.read)}` }))))
}

function pill(r) { return h('span', { class: `lv-pill s-${r.status}` }, statusText(r)) }

function decisions(r, e, o) {
    if (!o.notes) return null
    return h('span', { class: 'lv-decide', role: 'group', 'aria-label': 'What you think of this one' },
        DECIDE.map(d => h('button', {
            type: 'button', class: 'lv-d', 'aria-pressed': r.decision === d.kind ? 'true' : 'false', title: d.title,
            onclick: () => o.decide(e, r, d.kind),
        }, d.label)))
}

function meta(e, r, o) {
    const bits = [`No. ${e.n}`, when(e.date), e.minutes ? `${e.minutes} min` : null,
        r.cost > 0 ? `${o.money(r.cost)} spent of ${o.money(o.price(e))}` : `${o.money(o.price(e))} to read to the end`]
    return h('p', { class: 'rl-meta' }, bits.filter(Boolean).join(' · '))
}

/** A card's first line, as the front page dates its cards: the place in the list, the date, the minutes. */
function dateline(e, group, i) {
    return h('p', { class: 'lv-date' }, [group === 'look' ? 'Worth a look' : `${i + 1}`, when(e.date), e.minutes ? `${e.minutes} min` : null].filter(Boolean).join(' · '))
}

// ------------------------------------------------------------ the views
function cardsView(list, o) {
    return h('ol', { class: 'lv-cards rl-items' }, list.map(({ e, r, group, i }) => h('li', { class: `rl-item lv-card s-${r.status}${group === 'look' ? ' look' : ''}` },
        // the picture is the card's argument: it opens at full size, so it can be read and zoomed
        h('a', { class: 'lv-img', href: `${o.root}articles/cards/${e.slug}.webp`, title: 'The picture, full size' },
            h('img', { src: `${o.root}articles/cards/${e.slug}.webp`, alt: `The picture for ${short(e.title)}`, loading: 'lazy', width: '720', height: '378' })),
        h('div', { class: 'lv-body' },
            dateline(e, group, i),
            h('a', { class: 'rl-t', href: sectionHref(o.root, e.slug, r.status === 'reading' ? r.next : null) }, e.title),
            h('p', { class: 'rl-teaser' }, e.teaser || ''),
            r.read > 0 ? sectionBar(r, o.root, e.slug) : null,
            h('div', { class: 'lv-foot' }, pill(r), decisions(r, e, o))))))
}

function headlinesView(list, o) {
    return h('ol', { class: 'lv-heads rl-items' }, list.map(({ e, r, group, i }) => h('li', { class: `rl-item lv-head s-${r.status}${group === 'look' ? ' look' : ''}` },
        h('span', { class: 'lv-num' }, group === 'look' ? '+' : String(i + 1)),
        h('div', { class: 'lv-hl' },
            h('a', { class: 'rl-t', href: sectionHref(o.root, e.slug, null), title: e.title }, short(e.title)),
            h('span', { class: 'lv-one' }, e.teaser || '')),
        h('div', { class: 'lv-hr' }, h('span', { class: 'lv-min' }, [when(e.date), e.minutes ? `${e.minutes} min` : null].filter(Boolean).join(' · ')),
            r.status !== 'unread' ? pill(r) : null, r.read > 0 ? sectionBar(r, o.root, e.slug) : null))))
}

function sectionsView(list, o) {
    return h('ol', { class: 'lv-secs rl-items' }, list.map(({ e, r, group, i }) => h('li', { class: `rl-item lv-sec s-${r.status}${group === 'look' ? ' look' : ''}` },
        h('div', { class: 'lv-sec-h' },
            h('span', { class: 'lv-num' }, group === 'look' ? '+' : String(i + 1)),
            h('div', {}, h('a', { class: 'rl-t', href: sectionHref(o.root, e.slug, null) }, e.title), meta(e, r, o)),
            h('div', { class: 'lv-hr' }, pill(r), decisions(r, e, o))),
        r.sections.length
            ? h('details', { class: 'lv-lines-d', open: r.read > 0 || i === 0 && group === 'read' ? true : null },
                h('summary', {}, `${r.sections.length} sections, one line each`),
                h('ol', { class: 'lv-lines' }, r.sections.map(s => h('li', { class: s.read >= 0.9 ? 'done' : s.read > 0.02 ? 'part' : '' },
                    h('span', { class: 'lv-tick', 'aria-hidden': 'true', style: `--r:${Math.round(s.read * 100)}` }),
                    h('a', { href: sectionHref(o.root, e.slug, s.id) }, h('b', {}, s.label), ' ', s.line || ''),
                    h('span', { class: 'lv-pc' }, s.read > 0.02 ? pct(s.read) : `${Math.max(1, Math.round(s.words / 238))} min`)))))
            : h('p', { class: 'rl-teaser' }, e.teaser || ''))))
}

function picturesView(list, o) {
    const groups = list.map(({ e, r, group, i }) => {
        const figs = (((o.extras.get(e.slug) || {}).graph || {}).figures || []).filter(f => f.file)
        return h('li', { class: `rl-item lv-pics s-${r.status}` },
            h('div', { class: 'lv-sec-h' },
                h('span', { class: 'lv-num' }, group === 'look' ? '+' : String(i + 1)),
                h('div', {}, h('a', { class: 'rl-t', href: sectionHref(o.root, e.slug, null) }, short(e.title)), h('p', { class: 'lv-date' }, `${when(e.date)} · ${figs.length || 'no'} figure${figs.length === 1 ? '' : 's'}${r.status !== 'unread' ? ' · ' + statusText(r) : ''}`))),
            h('div', { class: 'lv-gallery' },
                (figs.length ? figs : [{ file: null }]).map(f => f.file
                    ? h('a', { class: 'lv-fig', href: `${o.root}articles/images/${f.file}`, title: f.caption || '' },
                        h('img', { src: `${o.root}articles/images/${f.file}`, alt: f.caption || '', loading: 'lazy' }),
                        h('span', {}, f.caption || ''))
                    : h('a', { class: 'lv-fig', href: sectionHref(o.root, e.slug, null) },
                        h('img', { src: `${o.root}articles/cards/${e.slug}.webp`, alt: '', loading: 'lazy' }), h('span', {}, e.teaser || '')))))
    })
    return h('ol', { class: 'rl-items lv-picsall' }, groups)
}

/**
 * The graph: the articles in reading order along a path, each a circle filled as far as it was read, with its main
 * ideas around it; an arc where one article on the list links to another; and below, the articles beyond the list
 * that two or more on it link to (or, failing that, the most linked), as the places to go next.
 */
function graphView(list, o) {
    const wrap = h('div', { class: 'lv-graph' })
    const draw = () => {
        const W = Math.max(320, Math.min(1400, wrap.clientWidth || 900))
        const narrow = W < 640
        const n = list.length
        const ideasOn = o.ideas !== false
        const slugs = new Set(list.map(x => x.e.slug))
        const pos = new Map()
        const R = narrow ? 24 : 30
        let H
        const perRow = Math.min(n, 8)
        // room above the row for the arcs: as much as the widest link needs, and none when nothing links
        const idx = new Map(list.map((x, i) => [x.e.slug, i]))
        let span = 0
        for (const { e } of list) for (const t of ((((o.extras.get(e.slug) || {}).graph || {}).links || {}).articles) || [])
            if (idx.has(t) && t !== e.slug) span = Math.max(span, Math.abs(idx.get(t) % perRow - idx.get(e.slug) % perRow))
        const stepX = (W - 160) / Math.max(1, perRow - 1)
        const TOP = narrow ? 30 : span ? 50 + Math.min(110, span * stepX / 3) : 40
        const rowH = narrow ? (ideasOn ? 140 : 84) : 2 * R + (ideasOn ? 170 : 90)
        if (narrow) {             // a column: one article per row, its title and ideas to the right
            list.forEach((x, i) => pos.set(x.e.slug, { x: 56, y: TOP + R + i * rowH }))
            H = TOP + n * rowH
        } else {                  // a row across the width, a second row when the list is long
            const rows = Math.ceil(n / perRow)
            list.forEach((x, i) => {
                const row = Math.floor(i / perRow), k = i % perRow, cols = Math.min(perRow, n - row * perRow)
                const step = (W - 160) / Math.max(1, perRow - 1)
                const xx = cols === 1 && n === 1 ? W / 2 : 80 + k * step
                pos.set(x.e.slug, { x: xx, y: TOP + row * (rowH + 40) })
            })
            H = TOP + (rows - 1) * (rowH + 40) + rowH
        }
        // what lies beyond the list: articles that the list links to and that are not on it
        const beyond = new Map()
        for (const { e } of list) {
            const links = ((((o.extras.get(e.slug) || {}).graph || {}).links || {}).articles) || []
            for (const s of links) if (!slugs.has(s) && o.bySlug.has(s)) beyond.set(s, [...(beyond.get(s) || []), e.slug])
        }
        let further = [...beyond.entries()].sort((a, b) => b[1].length - a[1].length || o.bySlug.get(b[0]).n - o.bySlug.get(a[0]).n)
        further = (further.some(f => f[1].length > 1) ? further.filter(f => f[1].length > 1) : further).slice(0, narrow ? 4 : 6)
        const fy = H + 30
        if (further.length) H = fy + (narrow ? 20 + further.length * 40 : 100)
        further.forEach(([s], i) => pos.set(s, narrow ? { x: 44, y: fy + 30 + i * 40 } : { x: further.length === 1 ? W / 2 : 80 + i * ((W - 160) / Math.max(1, further.length - 1)), y: fy + 34 }))

        const g = svg('svg', { viewBox: `0 0 ${W} ${H}`, width: W, height: H, role: 'img', 'aria-label': `The ${n} articles of this list as a graph`, class: 'lv-svg' })
        const defs = svg('defs', {}, svg('marker', { id: 'lv-arrow', viewBox: '0 0 10 10', refX: '9', refY: '5', markerWidth: '7', markerHeight: '7', orient: 'auto-start-reverse' },
            svg('path', { d: 'M0,0 L10,5 L0,10 z', class: 'lv-arrowhead' })))
        g.append(defs)
        // the reading path
        const pts = list.map(x => pos.get(x.e.slug))
        if (pts.length > 1) {
            let d = `M${pts[0].x},${pts[0].y}`
            for (let i = 1; i < pts.length; i++) { const a = pts[i - 1], b = pts[i]; d += narrow ? ` L${b.x},${b.y}` : ` C${(a.x + b.x) / 2},${a.y} ${(a.x + b.x) / 2},${b.y} ${b.x},${b.y}` }
            g.append(svg('path', { d, class: 'lv-path' }))
        }
        // links between articles on the list, one arc per pair whichever way it points
        const pairs = new Map()
        for (const { e } of list) {
            const links = ((((o.extras.get(e.slug) || {}).graph || {}).links || {}).articles) || []
            for (const s of links) if (slugs.has(s) && s !== e.slug) {
                const k = [e.slug, s].sort().join('|')
                pairs.set(k, pairs.has(k) ? { ...pairs.get(k), both: true } : { from: e.slug, to: s, both: false })
            }
        }
        for (const { from, to, both } of pairs.values()) {
            const a = pos.get(from), b = pos.get(to)
            const sameRow = Math.abs(a.y - b.y) < 1
            const d = narrow ? `M${a.x - R - 6},${a.y} C6,${a.y} 6,${b.y} ${b.x - R - 6},${b.y}`
                : sameRow ? `M${a.x},${a.y - R - 6} Q${(a.x + b.x) / 2},${a.y - R - 6 - Math.min(TOP - R - 16, 24 + Math.abs(b.x - a.x) / 3)} ${b.x},${b.y - R - 6}`
                : `M${a.x},${a.y - R - 6} C${a.x},${Math.min(a.y, b.y) - 90} ${b.x},${Math.min(a.y, b.y) - 90} ${b.x},${b.y - R - 6}`
            g.append(svg('path', { d, class: 'lv-link', 'marker-end': 'url(#lv-arrow)', 'marker-start': both ? 'url(#lv-arrow)' : null },
                svg('title', {}, `${short(o.bySlug.get(from).title)} ${both ? 'and' : 'links to'} ${short(o.bySlug.get(to).title)}${both ? ' link to each other' : ''}`)))
        }
        // ideas: up to three per article, claims and methods first
        // each article's title, wrapped to the room it has: two lines on a phone, three across a row
        const titleLines = new Map(list.map(({ e }) => {
            const max = narrow ? Math.max(18, Math.floor((W - 56 - R - 24) / 7.4)) : Math.max(14, Math.floor(((n > 1 ? (W - 160) / Math.max(1, Math.min(n, 8) - 1) : W)) / 7.6))
            const lines = []; let cur = ''
            for (const w of short(e.title).split(' ')) { if ((cur + ' ' + w).trim().length > max && cur) { lines.push(cur); cur = w } else cur = (cur + ' ' + w).trim() }
            if (cur) lines.push(cur)
            const keep = lines.slice(0, narrow ? 2 : 3)
            if (lines.length > keep.length) keep[keep.length - 1] = clip(keep[keep.length - 1] + ' ' + lines.slice(keep.length).join(' '), max)
            return [e.slug, keep]
        }))
        // an idea's label fits the gap between two articles: about 6.5 pixels a character at the size drawn
        const gap = narrow ? W - 100 : n > 1 ? (W - 160) / Math.max(1, Math.min(n, 8) - 1) : W
        const maxIdea = Math.max(14, Math.min(40, Math.floor(gap / 6.8)))
        if (ideasOn) for (const { e } of list) {
            const gr = (o.extras.get(e.slug) || {}).graph
            if (!gr || !gr.nodes) continue
            const rank = { claim: 0, method: 1, concept: 2, question: 3, example: 4 }
            const ideas = [...gr.nodes].sort((a, b) => (rank[a.kind] ?? 5) - (rank[b.kind] ?? 5)).slice(0, 2)
            const c = pos.get(e.slug)
            // each idea wrapped onto two lines at most, rather than cut mid-word
            let y = narrow ? c.y - 14 + titleLines.get(e.slug).length * 15 + 8 : c.y + R + 78
            if (!narrow) g.append(svg('line', { x1: c.x - 14, y1: y - 17, x2: c.x + 14, y2: y - 17, class: 'lv-idea-l' }))
            for (const nd of ideas) {
                const lines = []; let cur = ''
                for (const w of nd.label.split(' ')) { if ((cur + ' ' + w).trim().length > maxIdea && cur) { lines.push(cur); cur = w } else cur = (cur + ' ' + w).trim() }
                if (cur) lines.push(cur)
                const keep = lines.slice(0, 2)
                if (lines.length > 2) keep[1] = clip(keep[1] + ' ' + lines.slice(2).join(' '), maxIdea)
                const x = narrow ? c.x + R + 14 : c.x
                const t = svg('text', { x, y: y + 4, 'text-anchor': narrow ? 'start' : 'middle' })
                keep.forEach((l, k) => t.append(svg('tspan', { x, dy: k ? 14 : 0 }, l)))
                g.append(svg('g', { class: `lv-idea k-${nd.kind}` }, svg('title', {}, `${nd.label}: ${nd.summary || ''}`), t))
                y += 14 * keep.length + (narrow ? 4 : 7)
            }
        }
        // the articles on the list
        list.forEach(({ e, r, group }, i) => {
            const c = pos.get(e.slug)
            const circ = 2 * Math.PI * (R + 5)
            const a = svg('a', { href: sectionHref(o.root, e.slug, r.status === 'reading' ? r.next : null), class: `lv-node s-${r.status}${group === 'look' ? ' look' : ''}` },
                svg('title', {}, `${e.title} — ${statusText(r)}`),
                svg('circle', { cx: c.x, cy: c.y, r: R + 5, class: 'lv-ring-bg' }),
                r.read > 0 ? svg('circle', { cx: c.x, cy: c.y, r: R + 5, class: 'lv-ring', 'stroke-dasharray': `${circ * r.read} ${circ}`, transform: `rotate(-90 ${c.x} ${c.y})` }) : null,
                svg('circle', { cx: c.x, cy: c.y, r: R, class: 'lv-dot' }),
                svg('text', { x: c.x, y: c.y + 5, 'text-anchor': 'middle', class: 'lv-dot-t' }, group === 'look' ? '+' : String(i + 1)))
            const lines = titleLines.get(e.slug)
            const ly0 = narrow ? c.y - (ideasOn ? 14 : 4) : 0
            const ly = narrow ? ly0 : c.y + R + 24
            const t = svg('text', { x: narrow ? c.x + R + 14 : c.x, y: ly, 'text-anchor': narrow ? 'start' : 'middle', class: 'lv-node-t' })
            lines.slice(0, 3).forEach((l, k) => t.append(svg('tspan', { x: narrow ? c.x + R + 14 : c.x, dy: k ? 15 : 0 }, l)))
            if (narrow && !ideasOn) t.append(svg('tspan', { x: c.x + R + 14, dy: 16, class: 'lv-node-s' }, statusText(r)))
            a.append(t)
            g.append(a)
        })
        if (further.length) {
            g.append(svg('line', { x1: 10, x2: W - 10, y1: fy - 4, y2: fy - 4, class: 'lv-out' }))
            g.append(svg('text', { x: narrow ? 14 : 20, y: fy + 12, class: 'lv-further-h' }, narrow ? 'Where these lead' : 'Where these lead: articles beyond the list that they link to'))
            for (const [s, from] of further) {
                const e = o.bySlug.get(s), c = pos.get(s)
                const label = short(e.title)
                g.append(svg('a', { href: `${o.root}articles/${s}.html`, class: 'lv-far' },
                    svg('title', {}, `${e.title} — linked from ${from.length} on this list`),
                    svg('circle', { cx: c.x, cy: c.y, r: 9 }),
                    svg('text', { x: narrow ? c.x + 18 : c.x, y: narrow ? c.y + 4 : c.y + 26, 'text-anchor': narrow ? 'start' : 'middle' },
                        label.length > 30 ? label.slice(0, 29) + '…' : label),
                    svg('text', { x: narrow ? c.x + 18 : c.x, y: narrow ? c.y + 19 : c.y + 41, 'text-anchor': narrow ? 'start' : 'middle', class: 'lv-far-n' },
                        `linked from ${from.length} on this list`)))
            }
        }
        wrap.replaceChildren(g)
    }
    const legend = h('p', { class: 'lv-legend' },
        h('span', { class: 'k k-path' }, 'reading order'), h('span', { class: 'k k-link' }, 'one links to another'),
        h('span', { class: 'k k-ring' }, 'ring: how much you have read'), h('span', { class: 'k k-idea' }, 'its main ideas'),
        h('label', { class: 'lv-ideas' }, h('input', { type: 'checkbox', checked: o.ideas !== false ? true : null, onchange: ev => { o.setIdeas(ev.target.checked) } }), ' Show ideas'))
    const holder = h('div', { class: 'lv-graph-holder' }, legend, wrap)
    queueMicrotask(draw)
    requestAnimationFrame(draw)
    if (typeof ResizeObserver === 'function') { let w = 0; new ResizeObserver(() => { if (Math.abs(wrap.clientWidth - w) > 40) { w = wrap.clientWidth; draw() } }).observe(wrap) }
    // the same articles as links, for a screen reader and for the order the tests read
    holder.append(h('ol', { class: 'rl-items lv-sr' }, list.map(({ e }) => h('li', { class: 'rl-item' }, h('a', { class: 'rl-t', href: sectionHref(o.root, e.slug, null) }, e.title)))))
    return holder
}

// ------------------------------------------------------------ the hero and the side
function ring(share, size = 96) {
    const r = size / 2 - 7, c = 2 * Math.PI * r
    return svg('svg', { viewBox: `0 0 ${size} ${size}`, width: size, height: size, class: 'lv-big-ring', 'aria-hidden': 'true' },
        svg('circle', { cx: size / 2, cy: size / 2, r, class: 'lv-ring-bg' }),
        // at nothing read there is no arc at all: a round cap on a zero-length line draws a stray dot
        share > 0 ? svg('circle', { cx: size / 2, cy: size / 2, r, class: 'lv-ring', 'stroke-dasharray': `${c * share} ${c}`, transform: `rotate(-90 ${size / 2} ${size / 2})` }) : null,
        svg('text', { x: size / 2, y: size / 2 + 7, 'text-anchor': 'middle', class: 'lv-big-t' }, `${Math.round(share * 100)}%`))
}

/**
 * The top of the list, as a masthead and a letter: a dateline, an italic kicker, the two names, the sender's note
 * signed, and what to do first. The numbers (a ring, read, time left, spent) appear once the reader has started;
 * before that, a list of zeros says nothing, so one line says what the list holds and what it costs.
 */
function hero(p, rows, o) {
    const live = rows.filter(x => !x.e.withdrawn)
    const words = x => Math.max(1, (x.e.minutes || 1))
    const counted = live.filter(x => x.r.status !== 'aside')
    const share = counted.length ? counted.reduce((a, x) => a + words(x) * (x.r.status === 'done' ? 1 : x.r.read), 0) / counted.reduce((a, x) => a + words(x), 0) : 0
    const by = k => live.filter(x => x.r.status === k).length
    const left = counted.reduce((a, x) => a + (x.r.status === 'done' ? 0 : (x.e.minutes || 0) * (1 - x.r.read)), 0)
    const minutes = live.reduce((a, x) => a + (x.e.minutes || 0), 0)
    const spent = live.reduce((a, x) => a + x.r.cost, 0)
    const all = live.reduce((a, x) => a + o.price(x.e), 0)
    const next = live.find(x => x.group === 'read' && !['read', 'done', 'aside'].includes(x.r.status)) || live.find(x => !['read', 'done', 'aside'].includes(x.r.status))
    const started = live.some(x => x.r.read > 0.02 || x.r.decision)
    const reply = replyLink(p)
    const nextHref = next ? sectionHref(o.root, next.e.slug, next.r.status === 'reading' ? next.r.next : null) : null
    const newest = live.map(x => x.e.date).sort().pop()
    const nRead = rows.filter(x => x.group === 'read').length, nLook = rows.filter(x => x.group === 'look').length
    const about = minutes >= 50 ? `about ${Math.round(minutes / 60 * 2) / 2 === 1 ? 'an hour' : `${Math.round(minutes / 60 * 2) / 2} hours`}` : `${minutes} minutes`
    return h('header', { class: 'rl-head lv-hero' },
        h('p', { class: 'lv-dateline' },
            h('span', {}, `A reading list · ${live.length} article${live.length === 1 ? '' : 's'} · ${about}`),
            h('span', {}, [p.from ? `from ${p.from}` : null, newest ? `newest ${when(newest)}` : null].filter(Boolean).join(' · '))),
        h('div', { class: 'lv-hero-main' },
            h('p', { class: 'lv-kicker' }, p.to ? `Chosen for ${p.to}` : 'Chosen for you'),
            h('h1', { class: 'rl-title' }, titleFor(p)),
            p.note ? h('blockquote', { class: 'rl-note' }, p.note) : null,
            p.note && p.from ? h('p', { class: 'lv-sign' }, `— ${p.from}`) : null,
            h('p', { class: 'rl-actions' },
                next ? h('a', { class: 'rl-btn primary', href: nextHref }, started ? `Continue: ${clip(short(next.e.title), 46)}` : 'Start reading') : h('span', { class: 'lv-alldone' }, 'You have read everything on this list.'),
                reply),
            started ? null : h('p', { class: 'lv-sub' },
                `${nRead} to read${nLook ? `, ${nLook} worth a look` : ''}. Free to start: you pay a few pence per article, after you read it, from £5.00 of credit kept in your browser.`)),
        started ? h('div', { class: 'lv-hero-stats', 'aria-label': 'Your progress on this list' },
            ring(share),
            h('dl', {},
                h('div', {}, h('dt', {}, 'Read'), h('dd', {}, `${by('read') + by('done')} of ${counted.length}`, h('small', {}, `${by('reading') ? `${by('reading')} started` : ''}${by('aside') ? `${by('reading') ? ' · ' : ''}${by('aside')} set aside` : ''}`))),
                h('div', {}, h('dt', {}, 'Time left'), h('dd', {}, `${Math.round(left)} min`)),
                h('div', {}, h('dt', {}, 'Spent'), h('dd', {}, o.money(Math.round(spent)), h('small', {}, `of about ${o.money(all)} for all of it`))))) : null)
}

/** The side: what the reader is looking at in one sentence, the newsroom in four short steps, the list as a persona, and more. */
export function aside(p, o) {
    const from = p.from || 'the sender'
    const steps = [
        ['Read', 'Pay a few pence, after you read, from £5 free credit.'],
        ['Come back', 'What you read is remembered here, section by section.'],
        ['Keep the list', 'It is one of your personas now. Nothing is sent anywhere.'],
        ['Reply', `Tell ${from} what landed, and what did not.`],
    ]
    const anim = h('ol', { class: 'lv-how' }, steps.map(([t, d], i) => h('li', { style: `--i:${i}` },
        h('span', { class: 'lv-how-n' }, String(i + 1)), h('div', {}, h('b', {}, t), h('p', {}, d)))))
    const links = [
        ['What this newsroom is, for publishers', 'publishers/index.html'],
        ['Who is speaking: me, or an agent?', 'articles/who-is-speaking.html'],
        ['How paying for what you read works', 'articles/pay-after-you-read.html'],
        ['The front page', 'index.html'],
        ['Your reading account', 'account/index.html'],
    ]
    return h('aside', { class: 'lv-side', 'aria-label': 'About this page' },
        h('section', { class: 'lv-card-side' },
            h('h2', {}, 'What am I looking at?'),
            h('p', {}, `Articles ${p.from ? `${p.from} chose` : 'chosen'} for ${p.to || 'you'} from the SGit Newsroom, a small publication written in the open, every source linked and every version kept.`),
            anim),
        o.personaBar || null,
        o.follow || null,
        h('section', { class: 'lv-card-side' },
            h('h2', {}, 'To find out more'),
            h('ul', { class: 'lv-links' }, links.map(([t, u]) => h('li', {}, h('a', { href: `${o.root}${u}` }, t))))))
}

// ------------------------------------------------------------ the page
/**
 * The list page. o: { root, price, money, bySlug: Map, extras: Map, notes (module or null), personaBar: node,
 * follow: node, ignored: node }. Returns { el, refresh } where refresh() redraws with the reading as it is now.
 */
export function renderListPage(p, o) {
    const entries = [...p.read.map((e, i) => ({ e, group: 'read', i })), ...p.look.map((e, i) => ({ e, group: 'look', i }))]
    const live = entries.filter(x => !x.e.withdrawn)
    let view = VIEWS.some(v => v.id === ls.get(VIEW_KEY)) ? ls.get(VIEW_KEY) : 'cards'
    let ideas = ls.get('newsroom.list.ideas') !== '0'
    let filter = 'all'
    const root = h('section', { class: 'rl lv', 'aria-label': titleFor(p) })
    const body = h('div', { class: 'lv-main' })
    const side = aside(p, o)

    const refresh = () => {
        const reading = readingOf(live.map(x => x.e), o.extras, o.root, o.notes)
        const rows = entries.map(x => ({ ...x, r: x.e.withdrawn ? { status: 'unread', read: 0, sections: [], cost: 0 } : reading.get(x.e.slug) }))
        const shown = rows.filter(x => !x.e.withdrawn).filter(x => filter === 'all' || (filter === 'unread' ? !['read', 'done', 'aside'].includes(x.r.status) : ['read', 'done'].includes(x.r.status)))
        const opts = {
            ...o, ideas, setIdeas: v => { ideas = v; ls.set('newsroom.list.ideas', v ? '1' : '0'); refresh() },
            decide: (e, r, kind) => {
                const cur = o.notes.decisionFor(r.path)
                if (cur && cur.kind === kind) o.notes.remove(cur.id)
                else o.notes.keep({ kind, path: r.path, title: e.title, n: e.n, quote: '' })
                refresh()
            },
        }
        const tabs = h('div', { class: 'lv-bar-views', role: 'tablist', 'aria-label': 'How to see this list' },
            VIEWS.map(v => h('button', { type: 'button', role: 'tab', 'aria-selected': v.id === view ? 'true' : 'false', title: v.about, class: 'lv-tab', onclick: () => { view = v.id; ls.set(VIEW_KEY, view); refresh() } }, v.label)),
            h('span', { class: 'lv-filter' },
                ['all', 'unread', 'read'].map(f => h('button', { type: 'button', class: 'lv-f', 'aria-pressed': f === filter ? 'true' : 'false', onclick: () => { filter = f; refresh() } },
                    f === 'all' ? 'All' : f === 'unread' ? 'Still to read' : 'Read'))))
        const views = { cards: cardsView, headlines: headlinesView, sections: sectionsView, pictures: picturesView, graph: graphView }
        const gone = rows.filter(x => x.e.withdrawn)
        body.replaceChildren(...[
            hero(p, rows, o),
            h('p', { class: 'lv-intro' }, `${p.from ? `${p.from} picked` : 'Picked'} these for ${p.to || 'you'}. Tap one to read; your progress shows here. What this page is, and how it works, is at the foot.`),
            tabs,
            shown.length ? views[view](shown, opts) : h('p', { class: 'lv-none' }, filter === 'unread' ? 'Nothing left to read on this list.' : 'Nothing read yet. Start with the first one.'),
            gone.length ? h('p', { class: 'rl-ignored' }, h('b', {}, 'No longer published: '), gone.map(x => `article ${x.e.n}`).join(', '), '.') : null,
            o.ignored || null,
            h('p', { class: 'rl-foot' }, 'The names and the note are whatever the link says. What you have read is kept in this browser, and in your own vault if you open one; nothing about this list or your reading has been sent anywhere.')].filter(Boolean))
    }
    refresh()
    root.append(h('div', { class: 'lv-layout' }, body, side))
    return { el: root, refresh }
}
