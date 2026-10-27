#!/usr/bin/env node
/* test_review_lane.mjs: the review lane end to end (card 091), against admin/build/vault-mock.mjs, never the real server.
 *
 * review_lane.mjs create makes a vault, its append lane and a key pair on the mock, and writes the send link; the send
 * page, reviews/send.html, opened on that link in a browser, takes a pasted answer with two records, refuses the one
 * that repeats a review already on the record, seals the other and appends it; review_lane.mjs drain opens the lane,
 * checks the record again and writes it where the reviews live (in a scratch copy, never the repository), --mark
 * marks it processed, and a second drain finds nothing. Also: the record checks in assets/reviews/record.js, and the
 * vendored pki message code against its VENDOR.md.
 */
import http from 'http'
import fs from 'fs'
import os from 'os'
import path from 'path'
import { execSync, spawn } from 'child_process'
import { pathToFileURL } from 'url'

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..')
let failed = 0
const check = (ok, what) => { console.log(`${ok ? 'ok  ' : 'FAIL'} ${what}`); if (!ok) failed++ }
const R = await import(pathToFileURL(path.join(ROOT, 'assets/reviews/record.js')).href)
const { startMock } = await import(pathToFileURL(path.join(ROOT, 'admin/build/vault-mock.mjs')).href)

// ------------------------------------------------------------ part one: the record checks, in node
const status = JSON.parse(fs.readFileSync(path.join(ROOT, 'reviews/status.json'), 'utf8'))
const ipo = status.articles.find(a => a.slug === 'the-ipo-filing-and-the-agents')
// a review on the record that is still of the article's current text (an article corrected after its review no longer is)
const [four, onRecord] = status.articles.flatMap(a => (a.reviews || []).filter(r => r.current).map(r => [a, r]))[0] || []
if (!four) { console.log('FAIL no review on the record is of an article\'s current text, so the repeat cannot be tested'); process.exit(1) }
const checks = Object.fromEntries(R.CHECKS.map(k => [k, { result: 'not-checked', notes: '' }]))
const good = { schema: R.SCHEMA, criteria: 'v1.2', slug: ipo.slug, article_version: ipo.version, article_hash: ipo.hash, reviewer: 'perplexity', kind: 'agent', model: 'a test model',
               run_by: 'test_review_lane.mjs', at: '2026-10-28T06:00:00Z', verdict: 'approve-with-changes', summary: 'A test review.', checks: { ...checks, facts: { result: 'issues', notes: '' } },
               findings: [{ id: 'f1', criterion: 'facts', severity: 'medium', section: 'in-short', quote: 'Anthropic filed to go public on 26 October.', issue: 'A test finding.', verification: 'unsupported', evidence: 'https://example.org/, read 28 October 2026', suggestion: 'A test fix.' }],
               verified: [], not_checked: [] }
const repeat = { ...good, slug: four.slug, article_hash: four.hash, article_version: four.version, reviewer: onRecord.reviewer, findings: [] }
const answer = `Batch 2026-10-28 for perplexity: 2 articles.\n\n\`\`\`json\n${JSON.stringify(good, null, 2)}\n\`\`\`\n\nAnd:\n\n\`\`\`json\n${JSON.stringify(repeat, null, 2)}\n\`\`\`\n\`\`\`json\n{"schema": "newsroom-review/v1", "slug": oops}\n\`\`\`\n`
const ex = R.extract(answer)
check(ex.records.length === 2 && ex.unreadable === 1, `extract finds the two records in an answer with words round them, and counts the broken one (${ex.records.length}, ${ex.unreadable})`)
check(R.problems(good, status).errors.length === 0, 'a good record has no errors')
check(R.problems(repeat, status).errors.some(e => /already reviewed this text/.test(e)), 'a second review of the same text by the same reviewer is an error')
check(R.problems({ ...good, findings: [{ ...good.findings[0], verification: 'wrong' }] }, status).errors.some(e => /verification/.test(e)), 'an unknown verification is an error')
check(R.problems({ ...good, verdict: 'approve', findings: [{ ...good.findings[0], severity: 'high' }] }, status).errors.some(e => /changes-needed/.test(e)), 'approve with a high finding is an error')
check(R.fileName(good) === '2026-10-28__perplexity.json', 'the file name is <date>__<reviewer>.json')

const vendor = fs.readFileSync(path.join(ROOT, 'admin/build/pki-message/VENDOR.md'), 'utf8')
for (const f of ['message.js', 'keys.js']) check(vendor.includes(execSync(`sha256sum ${path.join(ROOT, 'admin/build/pki-message', f)}`).toString().split(' ')[0]), `the vendored ${f} is the one VENDOR.md records`)

// the secret's hand-over, as create does it: composed, sealed to a key, and opened only by that key
const K = await import(pathToFileURL(path.join(ROOT, 'admin/build/pki-message/keys.js')).href)
const M = await import(pathToFileURL(path.join(ROOT, 'admin/build/pki-message/message.js')).href)
const editor = await K.generate('an editor for the test'), other = await K.generate('someone else')
const sealed = (await M.sealMessage(await M.compose({ to: editor.bundle, subject: 'REVIEW_LANE_SECRET', text: 'the secret', expires: new Date(Date.now() + 864e5).toISOString() }), editor.bundle)).url
const code = M.parseCode(sealed)
check(/^https:\/\/pki\.sgit\.ai\/m\/#m1\./.test(sealed) && code && code.to === editor.bundle.signing_fingerprint, 'the secret goes to the editor as a pki.sgit.ai m1 link addressed to the key')
check((await M.openMessage(code.enc, [editor])).msg.text === 'the secret', 'the editor\'s key opens it')
let opened = null; try { opened = await M.openMessage(code.enc, [other]) } catch (e) { /* refused */ }
check(!opened, 'another key does not')

// ------------------------------------------------------------ part two: create, send in a browser, drain
const mock = await startMock()
const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'review-lane-'))
const into = path.join(tmp, 'repo'); fs.mkdirSync(path.join(into, 'admin/content/reviews'), { recursive: true })
fs.copyFileSync(path.join(ROOT, 'admin/content/reviews/reviewers.json'), path.join(into, 'admin/content/reviews/reviewers.json'))
const lane = (...a) => new Promise(resolve => {                       // async, so the mock in this process keeps answering
    const p = spawn('node', [path.join(ROOT, 'admin/build/review_lane.mjs'), ...a], { env: { ...process.env, SG_SEND_ACCESS_TOKEN: mock.token, REVIEW_LANE_SECRET: '' } })
    let out = ''; p.stdout.on('data', d => out += d); p.stderr.on('data', d => out += d)
    p.on('close', code => resolve({ code, out }))
})
let chromium, br, server
try {
    const out = path.join(tmp, 'out')
    let r = await lane('create', '--unsealed', '--endpoint', mock.base, '--out', out)
    check(r.code === 0 && fs.existsSync(path.join(out, 'send-link.txt')), `create makes the lane on the mock${r.code ? ': ' + r.out : ''}`)
    const link = fs.readFileSync(path.join(out, 'send-link.txt'), 'utf8').trim()
    const pub = JSON.parse(fs.readFileSync(path.join(out, 'lane.json'), 'utf8'))
    const secret = JSON.parse(Buffer.from(fs.readFileSync(path.join(out, 'secret.txt'), 'utf8').trim(), 'base64').toString())
    check(/^https:\/\/newsroom\.sgit\.ai\/reviews\/send\.html#rv1\.[a-z0-9]+\.[0-9a-f]{32}\.[A-Za-z0-9_-]+$/.test(link), 'the send link is reviews/send.html#rv1.<vault>.<token>.<key>')
    check(!JSON.stringify(pub).includes(secret.private) && !JSON.stringify(pub).includes(secret.enum_key) && !JSON.stringify(pub).includes(secret.token), 'lane.json, the public half, holds no private key, no enum key and no append token')
    check(/<svg[^>]+role="img"/.test(fs.readFileSync(path.join(out, 'send-link-qr.svg'), 'utf8')), 'the link\'s QR code is an SVG')

    try { ({ chromium } = await import('playwright')) } catch (e) {
        const g = execSync('npm root -g').toString().trim(); ({ chromium } = await import(path.join(g, 'playwright', 'index.mjs')))
    }
    const TYPES = { '.html': 'text/html', '.js': 'text/javascript', '.mjs': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.md': 'text/markdown' }
    server = http.createServer((req, res) => {
        let f = path.join(ROOT, decodeURIComponent(new URL(req.url, 'http://x').pathname))
        if (f.startsWith(ROOT) && fs.existsSync(f) && fs.statSync(f).isDirectory()) f = path.join(f, 'index.html')
        if (!f.startsWith(ROOT) || !fs.existsSync(f)) { res.writeHead(404); res.end(); return }
        res.writeHead(200, { 'content-type': TYPES[path.extname(f)] || 'application/octet-stream' }); fs.createReadStream(f).pipe(res)
    })
    await new Promise(ok => server.listen(0, '127.0.0.1', ok))
    const B = `http://127.0.0.1:${server.address().port}/`
    try { br = await chromium.launch() } catch (e) { br = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' }) }
    const ctx = await br.newContext({ viewport: { width: 1200, height: 900 } })
    // the last route added is tried first: off this machine everything is refused, except the vault server, sent to the mock
    await ctx.route(/^(?!http:\/\/127\.0\.0\.1).*/, rt => rt.abort())
    await ctx.route('https://dev.send.sgraph.ai/**', async rt => {
        const q = rt.request(), u = new URL(q.url())
        const res = await fetch(mock.base + u.pathname + u.search, { method: q.method(), headers: q.headers(), body: q.method() === 'GET' ? undefined : q.postDataBuffer() })
        await rt.fulfill({ status: res.status, headers: Object.fromEntries(res.headers), body: Buffer.from(await res.arrayBuffer()) })
    })
    const pg = await ctx.newPage()
    const errors = []; pg.on('pageerror', e => errors.push(e.message))
    await pg.goto(link.replace('https://newsroom.sgit.ai/', B)); await pg.waitForSelector('#rv-text', { timeout: 20000 })
    check(!pg.url().includes('#'), 'the page takes the link out of the address')
    check(await pg.evaluate(() => /^rv1\./.test(localStorage.getItem('sgit.reviews.link') || '')), 'and remembers it in this browser')
    check((await pg.textContent('.send-box .kv')).includes(secret.fingerprint), 'it names the key it seals to')
    await pg.fill('#rv-text', answer); await pg.click('#rv-check')
    await pg.waitForSelector('#rv-result .rv-list', { timeout: 20000 })
    const res = await pg.textContent('#rv-result')
    check(/1 of 2 record\(s\) ready to send/.test(res), 'Check: one record ready, of two')
    check(/already reviewed this text/.test(res), 'Check: the repeat of a review on the record will not be sent, and says why')
    check(/1 block\(s\) mention the schema and are not valid JSON/.test(res), 'Check: the broken block is reported')
    check(!/quote is not in the article/.test(res), 'Check: the quote is found in the article\'s text')
    await pg.click('#rv-send'); await pg.waitForSelector('#rv-sent', { timeout: 30000 })
    check(/^Sent: 1 record/.test(await pg.textContent('#rv-sent')), 'Send: sealed and appended')
    check(errors.length === 0, `no page errors${errors.length ? ': ' + errors.join(' | ') : ''}`)
    const m = await br.newPage({ viewport: { width: 390, height: 800 } })
    await m.goto(B + 'reviews/send.html'); await m.waitForSelector('#rv-link', { timeout: 20000 })
    check(await m.evaluate(() => document.documentElement.scrollWidth <= 390), 'no sideways scroll at 390px, and with no link remembered the page asks for one')

    const secretFile = path.join(out, 'secret.txt')
    r = await lane('drain', '--endpoint', mock.base, '--secret-file', secretFile, '--into', into, '--dry')
    check(r.code === 0 && /1 message\(s\) in the lane; 1 record\(s\) would be written, 0 rejected/.test(r.out), `drain --dry: one message, one record, nothing written${r.code ? ': ' + r.out : ''}`)
    check(!fs.existsSync(path.join(into, 'admin/content/articles/reviews')), 'drain --dry writes nothing')
    const takenFile = path.join(tmp, 'taken.json')
    r = await lane('drain', '--endpoint', mock.base, '--secret-file', secretFile, '--into', into, '--taken', takenFile)
    const written = path.join(into, 'admin/content/articles/reviews', ipo.slug, '2026-10-28__perplexity.json')
    check(r.code === 0 && fs.existsSync(written), `drain writes the record where the reviews live${r.code ? ': ' + r.out : ''}`)
    const rec = JSON.parse(fs.readFileSync(written, 'utf8'))
    check(rec.article_hash === ipo.hash && rec.received && rec.received.via === 'the review lane' && rec.findings[0].quote === good.findings[0].quote, 'the record is as sent, with where it came from')
    check(/\[medium\] facts\/unsupported/.test(r.out) && /once the records are committed and pushed/.test(r.out), 'drain prints the findings for the editor, and says to mark after the push')
    r = await lane('drain', '--endpoint', mock.base, '--secret-file', secretFile, '--into', into, '--dry')
    check(/1 message\(s\) in the lane; 0 record\(s\) would be written, 1 rejected/.test(r.out), 'before mark, the message is still there, and its record, already in the repository, is not written twice')
    r = await lane('mark', '--endpoint', mock.base, '--secret-file', secretFile, '--taken', takenFile)
    check(r.code === 0 && /1 message\(s\) marked processed/.test(r.out), `mark marks what the drain took${r.code ? ': ' + r.out : ''}`)
    r = await lane('drain', '--endpoint', mock.base, '--secret-file', secretFile, '--into', into)
    check(r.code === 0 && /0 message\(s\) in the lane/.test(r.out), 'a second drain finds nothing')
} finally {
    if (br) await br.close()
    if (server) server.close()
    await mock.close()
    fs.rmSync(tmp, { recursive: true, force: true })
}
console.log(failed ? `${failed} FAILED` : 'ALL REVIEW LANE CHECKS PASS')
process.exit(failed ? 1 : 0)
