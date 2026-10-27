/**
 * record.js: a review record (newsroom-review/v1, admin/content/reviews/criteria.md), found in what a reviewer wrote,
 * checked, and named. Shared by the page that sends reviews (reviews/send.html) and the script that drains the review
 * lane (admin/build/review_lane.mjs), so a record is held to the same rules on both sides (card 091).
 *
 * A reviewer that runs on a schedule (ChatGPT, Perplexity) answers in a chat: some words, then one JSON record per
 * article, in fenced blocks or not. extract() finds every object with "schema": "newsroom-review/v1" in that text;
 * problems() says what is wrong with one, against the site's status.json (the articles, their current hashes and the
 * registered reviewers); fileName() is where it goes:
 *
 *     admin/content/articles/reviews/<slug>/<YYYY-MM-DD>__<reviewer>.json
 *
 * Pure: no page, no network. admin/build/reviews.py --check is still the last word once a record is in the repository.
 *
 * @module record
 */
export const SCHEMA = 'newsroom-review/v1'
export const CRITERIA = ['v1', 'v1.1', 'v1.2']
export const VERDICTS = ['approve', 'approve-with-changes', 'changes-needed', 'comment']
export const KINDS = ['agent', 'editor', 'journalist', 'reader']
export const CHECKS = ['facts', 'voice', 'claims', 'conversions', 'health', 'people']
export const RESULTS = ['pass', 'issues', 'not-checked']
export const SEVERITIES = ['high', 'medium', 'low']
export const VERIFICATION = ['contradicted', 'unsupported', 'inconsistent', 'overstated', 'unverifiable', 'stale', 'style']
export const ID = /^[a-z0-9][a-z0-9.-]{1,60}$/
export const SLUG = /^[a-z0-9][a-z0-9-]{1,120}$/
export const LANE_KIND = 'newsroom-review/lane-v1'
const isObj = x => !!x && typeof x === 'object' && !Array.isArray(x)

// ------------------------------------------------------------ finding records in text
/** Every balanced {...} in text, as strings, outermost only. Strings and escapes are respected. */
function objects(text) {
    const out = []
    let depth = 0, start = -1, inStr = false, esc = false
    for (let i = 0; i < text.length; i++) {
        const c = text[i]
        if (inStr) { if (esc) esc = false; else if (c === '\\') esc = true; else if (c === '"') inStr = false; continue }
        if (c === '"') { if (depth > 0) inStr = true; continue }
        if (c === '{') { if (depth === 0) start = i; depth++ }
        else if (c === '}' && depth > 0) { depth--; if (depth === 0 && start >= 0) { out.push(text.slice(start, i + 1)); start = -1 } }
    }
    return out
}
/**
 * The review records in what a reviewer wrote: a JSON object, a JSON array, or any text with records in it (fenced
 * or not). Returns { records, unreadable } where unreadable counts candidates that mention the schema and do not parse.
 */
export function extract(text) {
    const s = String(text || '').replace(/[“”]/g, '"')
    const records = [], seen = new Set()
    let unreadable = 0
    const take = o => { if (isObj(o) && o.schema === SCHEMA) { const k = JSON.stringify(o); if (!seen.has(k)) { seen.add(k); records.push(o) } } }
    try { const j = JSON.parse(s.trim()); (Array.isArray(j) ? j : [j]).forEach(take); if (records.length) return { records, unreadable } } catch (e) { /* not one JSON value */ }
    for (const chunk of objects(s)) {
        if (!chunk.includes(SCHEMA)) continue
        try { take(JSON.parse(chunk)) } catch (e) { unreadable++ }
    }
    return { records, unreadable }
}

// ------------------------------------------------------------ checking one
const norm = s => String(s || '').replace(/[‘’]/g, "'").replace(/[“”]/g, '"').replace(/\s+/g, ' ').trim()

/**
 * What is wrong with a record: { errors, warnings }. status is the site's reviews/status.json (or null: no article
 * checks); text, when given, is the article's current text, for checking that quotes are in it.
 */
export function problems(r, status = null, text = null) {
    const errors = [], warnings = []
    if (!isObj(r)) return { errors: ['not a JSON object'], warnings }
    if (r.schema !== SCHEMA) errors.push(`schema is not ${SCHEMA}`)
    if (!CRITERIA.includes(r.criteria)) warnings.push(`criteria ${JSON.stringify(r.criteria)}: the current criteria are ${CRITERIA[CRITERIA.length - 1]}`)
    if (!SLUG.test(String(r.slug || ''))) errors.push('slug missing or not an article slug')
    if (!ID.test(String(r.reviewer || ''))) errors.push('reviewer id missing or not <vendor>-<product> in lower case')
    if (!KINDS.includes(r.kind)) errors.push(`kind must be one of ${KINDS.join(', ')}`)
    if (!VERDICTS.includes(r.verdict)) errors.push(`verdict must be one of ${VERDICTS.join(', ')}`)
    if (!/^\d{4}-\d{2}-\d{2}T/.test(String(r.at || ''))) errors.push('at is not an ISO date and time (2026-10-27T09:00:00Z)')
    if (!String(r.summary || '').trim()) errors.push('no summary')
    if (!String(r.model || '').trim()) warnings.push('no model: say which model, as the vendor names it')
    if (!isObj(r.checks)) errors.push('no checks')
    else for (const k of CHECKS) {
        const c = r.checks[k]
        if (!isObj(c) || !RESULTS.includes(c.result)) errors.push(`check ${k}: result must be one of ${RESULTS.join(', ')}`)
    }
    if (isObj(r.checks)) for (const k of Object.keys(r.checks)) if (!CHECKS.includes(k)) errors.push(`check ${k} is not one of the criteria`)
    const ids = new Set()
    for (const [i, f] of (Array.isArray(r.findings) ? r.findings : []).entries()) {
        const at = `finding ${f && f.id ? f.id : i + 1}`
        if (!isObj(f)) { errors.push(`${at}: not an object`); continue }
        if (!f.id || ids.has(f.id)) errors.push(`${at}: no id, or the id is used twice`)
        ids.add(f.id)
        if (!CHECKS.includes(f.criterion)) errors.push(`${at}: criterion must be one of ${CHECKS.join(', ')}`)
        if (!SEVERITIES.includes(f.severity)) errors.push(`${at}: severity must be high, medium or low`)
        if (!String(f.issue || '').trim()) errors.push(`${at}: no issue`)
        if (f.verification != null && !VERIFICATION.includes(f.verification)) errors.push(`${at}: verification must be one of ${VERIFICATION.join(', ')}`)
        if (!String(f.evidence || '').trim() && f.criterion === 'facts') warnings.push(`${at}: a facts finding with no evidence`)
        if (text && f.quote && !norm(text).includes(norm(f.quote))) warnings.push(`${at}: the quote is not in the article's current text: "${String(f.quote).slice(0, 80)}"`)
    }
    if (r.findings != null && !Array.isArray(r.findings)) errors.push('findings is not a list')
    if ((r.verdict === 'approve') && (r.findings || []).some(f => f && f.severity === 'high')) errors.push('verdict approve with a high finding: the criteria say changes-needed')
    if (status) {
        const a = (status.articles || []).find(x => x.slug === r.slug)
        if (!a) errors.push(`no article ${r.slug} on the site`)
        else {
            if (!r.article_hash) warnings.push(`no article_hash: it will be stamped with the current one, ${a.hash}`)
            else if (r.article_hash !== a.hash) warnings.push(`article_hash ${r.article_hash} is not the current text (${a.hash}): it will be shown as a review of an earlier text`)
            if ((a.reviews || []).some(x => x.reviewer === r.reviewer && x.hash && x.hash === (r.article_hash || a.hash))) errors.push(`${r.reviewer} has already reviewed this text of ${r.slug}`)
        }
        if (!(status.reviewers || []).some(x => x.id === r.reviewer)) warnings.push(`${r.reviewer} is not a registered reviewer yet: it will be registered with its first review`)
    }
    return { errors, warnings }
}

/** Where a record goes in the repository: <slug>/<YYYY-MM-DD>__<reviewer>.json (the caller adds __2 when taken). */
export const fileName = r => `${String(r.at).slice(0, 10)}__${r.reviewer}.json`
export const pathOf = r => `admin/content/articles/reviews/${r.slug}/${fileName(r)}`

/** The message the send page seals into the lane: the records, and the text they came from, kept for provenance. */
export function message({ records, text = '', to, from = '', via = '' }) {
    return { kind: LANE_KIND, to, sent_at: new Date().toISOString(), from, via, records, text: String(text).slice(0, 400000) }
}
export function messageProblems(msg, fp) {
    const out = []
    if (!isObj(msg)) return ['not a message']
    if (msg.kind !== LANE_KIND) out.push(`not a review-lane message (${String(msg.kind || 'no kind').slice(0, 40)})`)
    if (msg.to !== fp) out.push('addressed to another key')
    if (!Array.isArray(msg.records) || !msg.records.length) out.push('no records in it')
    return out
}
