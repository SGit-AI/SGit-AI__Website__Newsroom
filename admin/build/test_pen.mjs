#!/usr/bin/env node
/* test_pen.mjs: the Pen (card 090), and a note signed in a browser and checked by the newsroom against the register.
 *
 *   node admin/build/test_pen.mjs
 *
 * Part one needs node and python: keys made with pki.sgit.ai's own code (assets/vendor/pki/), a note signed the way
 * assets/pen/identity.js signs it, and admin/build/lane.py checking it against a register and a root of the test's own
 * (NEWSROOM_PKI_REGISTER, NEWSROOM_PKI_ROOT): a browser key its root operates is checked and vouched for; the same key
 * with no link from the root is valid and not vouched for; a note changed after it was signed fails; a key that is not
 * in the register is said so. Part two drives an article in Chromium: the Pen's button, a selection kept from the bar
 * at the foot, a comment of the reader's own, a note for the newsroom with its passage, this browser's key made and a
 * note signed with it, the register read (served by the test, never the live site) and the standing shown, and nothing
 * scrolling sideways on a phone. Part two skips when Playwright or Chromium is not available.
 */
import http from 'http'
import fs from 'fs'
import os from 'os'
import path from 'path'
import { execSync, spawnSync } from 'child_process'
import { pathToFileURL } from 'url'

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..')
let failed = 0
const check = (ok, what) => { console.log(`${ok ? 'ok  ' : 'FAIL'} ${what}`); if (!ok) failed++ }

// ------------------------------------------------------------ part one: sign in node, check in python
const K = await import(pathToFileURL(path.join(ROOT, 'assets/vendor/pki/v0.2.25/keys.js')).href)
const D = await import(pathToFileURL(path.join(ROOT, 'assets/vendor/pki/v0.2.25/directory.js')).href)
globalThis.localStorage = { getItem: () => null, setItem() {}, removeItem() {} }       // identity.js reads it at load()
const I = await import(pathToFileURL(path.join(ROOT, 'assets/pen/identity.js')).href)

const vendor = fs.readFileSync(path.join(ROOT, 'assets/vendor/pki/v0.2.25/VENDOR.md'), 'utf8')
for (const f of ['keys.js', 'directory.js']) {
    const got = execSync(`sha256sum ${path.join(ROOT, 'assets/vendor/pki/v0.2.25', f)}`).toString().split(' ')[0]
    check(vendor.includes(got), `the vendored ${f} is byte for byte the one VENDOR.md records`)
}

const today = new Date().toISOString().slice(0, 10)
const later = new Date(Date.now() + 20 * 864e5).toISOString().slice(0, 10)
const root = await K.generate('a root for the test')
const browser = await K.generate('a browser for the test')
const stranger = await K.generate('a key nobody vouches for')
const fpRoot = root.bundle.signing_fingerprint, fpB = browser.bundle.signing_fingerprint
const rec = async (who, sts) => ({ fp: who.bundle.signing_fingerprint, dir: K.dirOf(who.bundle.signing_fingerprint), fixture: false, ok: true, revoked: null, name: who.bundle.label, statements: sts })
const rootRecord = await rec(root, [await D.identityStatement(root, { name: 'the test root' }), await D.linkStatement(root, { to: fpB, method: 'operates', on: today, until: later })])
const browserRecord = await rec(browser, [await D.agentStatement(browser, { name: 'a browser', runtime: 'browser, newsroom.sgit.ai' }), await D.linkStatement(browser, { to: fpRoot, method: 'operated-by', on: today })])
const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'pen-'))
const writeRegister = (name, records) => { const f = path.join(tmp, name); fs.writeFileSync(f, JSON.stringify({ records })); return 'file://' + f }

const note = (id, text) => ({ id, at: new Date().toISOString(), kind: 'fix', path: '/articles/a-newsroom-for-one.html', n: 290, quote: 'What I had not thought through is who opens these links.', text, title: 'A newsroom for one' })
const signed = async (n, who) => ({ ...n, signed: await I.sign(n, { bundle: who.bundle, private: who.private }) })
const lane = path.join(tmp, 'lane'); fs.mkdirSync(path.join(lane, 'notes'), { recursive: true })
const notes = [await signed(note('n-good', 'This is mine, signed.'), browser), await signed(note('n-stranger', 'Signed by a key nobody vouches for.'), stranger)]
const tampered = await signed(note('n-changed', 'The words as signed.'), browser); tampered.text = 'The words changed afterwards.'
notes.push(tampered, note('n-plain', 'Not signed at all.'))
for (const n of notes) fs.writeFileSync(path.join(lane, 'notes', `${n.id}.json`), JSON.stringify(n))
check(await I.verify(notes[0], browser.bundle) && !(await I.verify(tampered, browser.bundle)), 'identity.js verifies its own signature, and refuses a note changed after signing')

const runLane = (register, rootFp) => {
    const r = spawnSync('python3', [path.join(ROOT, 'admin/build/lane.py'), '--dir', lane, '--no-fetch', '--json'], { env: { ...process.env, NEWSROOM_PKI_REGISTER: register, NEWSROOM_PKI_ROOT: rootFp }, encoding: 'utf8' })
    if (r.status !== 0) { console.log(r.stderr); return {} }
    return Object.fromEntries(JSON.parse(r.stdout).map(n => [n.id, n._signed || '']))
}
let got = runLane(writeRegister('both.json', [rootRecord, browserRecord]), fpRoot)
check(/^signed and checked: .*operated by the root until/.test(got['n-good']), `lane.py: a key the root operates, in date: checked and vouched for (${got['n-good']})`)
check(/NOT in the register/.test(got['n-stranger']), 'lane.py: a key that is not in the register is said so')
check(/SIGNATURE FAILS/.test(got['n-changed']), 'lane.py: a note changed after it was signed fails')
check(got['n-plain'] === '', 'lane.py: a note that was not signed is left as it is')
got = runLane(writeRegister('no-link.json', [await rec(root, [rootRecord.statements[0]]), browserRecord]), fpRoot)
check(/a valid signature, but not vouched for: the root has not linked to it/.test(got['n-good']), 'lane.py: with no "operates" from the root, the signature is valid and not vouched for')
const lapsed = await rec(root, [rootRecord.statements[0], await D.linkStatement(root, { to: fpB, method: 'operates', on: '2026-01-01', until: '2026-01-31' })])
got = runLane(writeRegister('lapsed.json', [lapsed, browserRecord]), fpRoot)
check(/has ended/.test(got['n-good']), 'lane.py: an "operates" link past its end date no longer vouches')

// ------------------------------------------------------------ part two: the Pen in a browser
let chromium
try { ({ chromium } = await import('playwright')) } catch (e) {
    try { const g = execSync('npm root -g').toString().trim(); ;({ chromium } = await import(path.join(g, 'playwright', 'index.mjs'))) }
    catch (e2) { console.log('SKIP the browser tests: playwright is not installed'); finish() }
}
const TYPES = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.webp': 'image/webp', '.jpg': 'image/jpeg', '.svg': 'image/svg+xml' }
const server = http.createServer((req, res) => {
    let f = path.join(ROOT, decodeURIComponent(new URL(req.url, 'http://x').pathname))
    if (f.startsWith(ROOT) && fs.existsSync(f) && fs.statSync(f).isDirectory()) f = path.join(f, 'index.html')
    if (!f.startsWith(ROOT) || !fs.existsSync(f)) { res.writeHead(404); res.end(); return }
    res.writeHead(200, { 'content-type': TYPES[path.extname(f)] || 'application/octet-stream' })
    fs.createReadStream(f).pipe(res)
})
await new Promise(r => server.listen(0, '127.0.0.1', r))
const B = `http://127.0.0.1:${server.address().port}/`
let br
try { br = await chromium.launch() } catch (e) {
    try { br = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium' }) }
    catch (e2) { console.log('SKIP the browser tests: Chromium is not available'); server.close(); finish() }
}
const errors = []
const ARTICLE = 'articles/a-newsroom-for-one.html'
try {
    const ctx = await br.newContext({ viewport: { width: 1280, height: 900 } })
    let served = { records: [] }
    // the last route added is tried first: everything off this machine is refused, except the register, served here
    await ctx.route(/^(?!http:\/\/127\.0\.0\.1).*/, r => r.abort())
    await ctx.route('https://pki.sgit.ai/**', r => r.fulfill({ status: 200, contentType: 'application/json', headers: { 'access-control-allow-origin': '*' }, body: JSON.stringify(served) }))
    const pg = await ctx.newPage()
    pg.on('pageerror', e => errors.push(e.message))
    const wait = ms => pg.waitForTimeout(ms)
    await pg.goto(B + ARTICLE); await wait(1200)
    check(!!(await pg.$('nav.site .nav-tools .pen-btn')), 'an article has the Pen in the bar')
    // select a sentence of the article
    const quote = 'What I had not thought through is who opens these links.'
    await pg.evaluate(q => {
        const w = document.createTreeWalker(document.querySelector('main'), NodeFilter.SHOW_TEXT)
        for (let n = w.nextNode(); n; n = w.nextNode()) { const i = n.data.indexOf(q); if (i >= 0) { const r = document.createRange(); r.setStart(n, i); r.setEnd(n, i + q.length); const s = getSelection(); s.removeAllRanges(); s.addRange(r); return } }
    }, quote); await wait(500)
    check(await pg.evaluate(() => !document.querySelector('.pen-bar').hidden), 'selecting words shows the bar at the foot')
    await pg.evaluate(() => [...document.querySelectorAll('.pen-bar button')].find(b => b.textContent === 'Keep').click()); await wait(300)
    let hl = await pg.evaluate(() => JSON.parse(localStorage.getItem('sgit.highlights.v1') || '{"items":[]}').items)
    check(hl.length === 1 && hl[0].exact === quote && hl[0].by === 'pen' && hl[0].path === '/' + ARTICLE, 'Keep keeps the passage as a highlight, anchored by its words')
    await pg.click('.pen-btn'); await wait(300)
    check(await pg.evaluate(() => !document.querySelector('aside.pen').hidden && document.documentElement.classList.contains('pen-open')), 'the button opens the Pen on the right')
    check(await pg.evaluate(q => [...document.querySelectorAll('.pen .pen-quote')].some(b => b.textContent === q), quote), 'the mark is listed in the Pen, marked private')
    await pg.fill('.pen textarea[data-id]', 'My own note on this line.'); await pg.evaluate(() => document.querySelector('.pen textarea[data-id]').dispatchEvent(new Event('change'))); await wait(200)
    hl = await pg.evaluate(() => JSON.parse(localStorage.getItem('sgit.highlights.v1')).items)
    check(hl[0].note === 'My own note on this line.', 'a comment of the reader\'s own is kept on the mark')
    // tell the newsroom about the mark
    await pg.evaluate(() => [...document.querySelectorAll('.pen .pen-b')].find(b => b.textContent === 'Tell the newsroom').click()); await wait(200)
    await pg.evaluate(() => [...document.querySelectorAll('.pen .pen-chip')].find(b => b.textContent === 'Idea').click()); await wait(100)
    await pg.fill('.pen-sec:nth-of-type(3) textarea', 'An unsigned idea.'); await wait(100)
    await pg.evaluate(() => [...document.querySelectorAll('.pen .pen-b')].find(b => b.textContent === 'Keep for the newsroom').click()); await wait(300)
    let ns = await pg.evaluate(() => JSON.parse(localStorage.getItem('sgit.notes.v1') || '{"notes":[]}').notes)
    check(ns.length === 1 && ns[0].kind === 'idea' && ns[0].quote === quote && ns[0].text === 'An unsigned idea.' && ns[0].path === '/' + ARTICLE && !ns[0].signed, 'a note for the newsroom is a vault-pane note, with its passage, unsigned without a key')
    // a key for this browser
    await pg.evaluate(() => [...document.querySelectorAll('.pen .pen-b')].find(b => b.textContent === 'Show the key').click()); await wait(800)
    await pg.fill('.pen-signed input[aria-label="Your name"]', 'A tester')
    await pg.evaluate(() => [...document.querySelectorAll('.pen .pen-b')].find(b => /Make this browser/.test(b.textContent)).click())
    await pg.waitForFunction(() => /Not vouched for yet|signed as you|could not be read/.test(document.querySelector('.pen-signed').textContent), null, { timeout: 60000 })
    const id = await pg.evaluate(() => JSON.parse(localStorage.getItem('sgit.pen.identity.v1')))
    check(id && /^sha256:[0-9a-f]{16}$/.test(id.bundle.signing_fingerprint) && id.statements.length === 2 && id.statements[1].body.method === 'operated-by' && id.statements[1].body.to === 'sha256:db7f79fdd87e030a', 'the browser\'s key: its identity and an "operated-by" link to the pinned root')
    let said = await pg.evaluate(() => document.querySelector('.pen-standing').textContent)
    check(/Not vouched for yet: .*not in the register/.test(said) && !!(await pg.$('.pen-steps')), `before the register holds it, the Pen says so and lists the steps (${said})`)
    // a signed note
    await pg.fill('.pen-sec:nth-of-type(3) textarea', 'A signed fix.')
    await pg.evaluate(() => [...document.querySelectorAll('.pen .pen-b')].find(b => b.textContent === 'Keep, signed').click()); await wait(600)
    ns = await pg.evaluate(() => JSON.parse(localStorage.getItem('sgit.notes.v1')).notes)
    const s = ns.find(n => n.text === 'A signed fix.')
    check(!!(s && s.signed && s.signed.signer === id.bundle.signing_fingerprint), 'with a key, the note is signed by this browser')
    check(await pg.evaluate(async n => { const I = await import('/assets/pen/identity.js'); return I.verify(n, JSON.parse(localStorage.getItem('sgit.pen.identity.v1')).bundle) }, s), 'the signature checks against the browser\'s public key')
    // the register holds the browser's record now (served by the test, from the Pen's own submission)
    const sub = await pg.evaluate(() => JSON.parse(document.querySelector('.pen-sub textarea').value))
    check(sub.kind === 'pki.sgit.ai/submission/v1' && sub.record === id.bundle.signing_fingerprint && sub.statements.length === 2, 'the submission is in the register\'s own format')
    served = { records: [{ fp: sub.record, dir: sub.record.replace(':', '-'), fixture: false, ok: true, revoked: null, name: 'A tester', statements: sub.statements }] }
    await pg.evaluate(() => { sessionStorage.clear(); [...document.querySelectorAll('.pen .pen-b')].find(b => b.textContent === 'Check the register').click() }); await wait(1500)
    said = await pg.evaluate(() => document.querySelector('.pen-standing').textContent)
    check(/not confirmed by an operator: it names .* as its operator/.test(said), `in the register, named but not yet linked back: the Pen reads the register's own words (${said})`)
    // a phone
    const m = await br.newPage({ viewport: { width: 390, height: 844 } })
    m.on('pageerror', e => errors.push(e.message))
    await m.goto(B + ARTICLE); await m.waitForTimeout(1000)
    await m.evaluate(() => { const p = document.querySelector('main p'); const r = document.createRange(); r.selectNodeContents(p.firstChild || p); getSelection().removeAllRanges(); getSelection().addRange(r) }); await m.waitForTimeout(400)
    check(await m.evaluate(() => document.documentElement.scrollWidth <= 390), 'no sideways scroll at 390px with the bar showing')
    await m.evaluate(() => document.querySelector('.pen-btn') && document.querySelector('.pen-btn').click()); await m.waitForTimeout(300)
    check(await m.evaluate(() => document.documentElement.scrollWidth <= 390), 'no sideways scroll at 390px with the Pen open')
    check(errors.length === 0, `no page errors${errors.length ? ': ' + errors.join(' | ') : ''}`)
} finally {
    await br.close()
    server.close()
    fs.rmSync(tmp, { recursive: true, force: true })
}
finish()

function finish() {
    console.log(failed ? `${failed} FAILED` : 'ALL PEN CHECKS PASS')
    process.exit(failed ? 1 : 0)
}
