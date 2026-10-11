#!/usr/bin/env node
/* test_passkey.mjs: the passkey lab in Chromium, with a virtual authenticator that has PRF.
 *
 *   node admin/build/test_passkey.mjs
 *
 * Drives passkey/index.html as a reader would: the capabilities card, making a passkey (prf.enabled), getting the
 * PRF bytes twice (the same bytes), the door derived from them (an 8-character id, two PBKDF2 keys), the recovery
 * code round trip, the test vectors (the browser agrees with sgit's Python on every value), and the vault server
 * flow against a stand-in server that behaves like dev.send.sgraph.ai's write, list, read and delete, so the whole
 * create-open-delete path runs without an access key. Also: the page stores nothing but the passkey's id, keeps
 * the access key out of storage, and makes no request to any host but its own and the (stood-in) vault server.
 *
 * WebAuthn needs a secure context or localhost, so the page is served as http://localhost, not 127.0.0.1. The
 * virtual authenticator comes from Chromium's WebAuthn CDP domain; PRF needs Chromium 128 or later. Skips (exit 0)
 * when Playwright or Chromium is not available.
 */
import http from 'http'
import fs from 'fs'
import path from 'path'
import { execSync } from 'child_process'

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..')
let chromium
try { ({ chromium } = await import('playwright')) } catch (e) {
    try { const g = execSync('npm root -g').toString().trim(); ;({ chromium } = await import(path.join(g, 'playwright', 'index.mjs'))) }
    catch (e2) { console.log('SKIP: playwright is not installed'); process.exit(0) }
}
const TYPES = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.tpl': 'text/plain', '.webp': 'image/webp', '.jpg': 'image/jpeg', '.svg': 'image/svg+xml' }
const server = http.createServer((req, res) => {
    let f = path.join(ROOT, decodeURIComponent(new URL(req.url, 'http://x').pathname))
    if (f.startsWith(ROOT) && fs.existsSync(f) && fs.statSync(f).isDirectory()) f = path.join(f, 'index.html')
    if (!f.startsWith(ROOT) || !fs.existsSync(f)) { res.writeHead(404); res.end(); return }
    res.writeHead(200, { 'content-type': TYPES[path.extname(f)] || 'application/octet-stream' })
    fs.createReadStream(f).pipe(res)
})
await new Promise(r => server.listen(0, '127.0.0.1', r))
const B = `http://localhost:${server.address().port}/`
let browser
try { browser = await chromium.launch() } catch (e) {
    try { browser = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium' }) }
    catch (e2) { console.log('SKIP: Chromium is not available'); server.close(); process.exit(0) }
}
let failed = 0
const check = (ok, what) => { console.log(`${ok ? 'ok  ' : 'FAIL'} ${what}`); if (!ok) failed++ }
const ctx = await browser.newContext({ viewport: { width: 1200, height: 900 }, permissions: ['clipboard-read', 'clipboard-write'] })
const pg = await ctx.newPage()
const errors = [], hosts = new Set()
pg.on('pageerror', e => errors.push(e.message))
pg.on('console', m => { if (m.type() === 'error' && !/404/.test(m.text())) errors.push(m.text()) })
pg.on('request', r => hosts.add(new URL(r.url()).host))
const wait = ms => pg.waitForTimeout(ms)
const text = id => pg.evaluate(id => (document.getElementById(id) || {}).textContent || '', id)
const kv = async (id, key) => pg.evaluate(([id, key]) => { const r = [...document.querySelectorAll(`#${id} .kv`)].find(x => x.querySelector('.k').textContent.startsWith(key)); return r ? r.querySelector('.v').textContent : null }, [id, key])

// the stand-in vault server: dev.send.sgraph.ai's write, list, read and delete, in a Map
const store = new Map()
const seen = []
await pg.route('https://dev.send.sgraph.ai/**', async route => {
    const req = route.request(), u = new URL(req.url()), m = req.method(), h = req.headers()
    seen.push(`${m} ${u.pathname}`)
    const [, , , op, vault, file] = u.pathname.split('/')
    const json = (status, body) => route.fulfill({ status, contentType: 'application/json', headers: { 'access-control-allow-origin': '*' }, body: JSON.stringify(body) })
    if (op === 'public-info' || op === 'health') return json(store.has(vault) ? 200 : 404, store.has(vault) ? { vault_id: vault, objects: store.get(vault).size } : { detail: 'Public vault not found' })
    if (op === 'list') return store.has(vault) ? json(200, { files: [...store.get(vault).keys()] }) : json(404, { detail: 'Vault not found' })
    if (op === 'write') {
        if (!h['x-sgraph-access-token'] || !h['x-api-key']) return json(401, { detail: 'access token required' })
        if (!/^[0-9a-f]{64}$/.test(h['x-sgraph-vault-write-key'] || '')) return json(403, { detail: 'write key required' })
        if (!/^obj-cas-imm-[0-9a-f]{12}$/.test(file)) return json(400, { detail: 'bad file id' })
        if (!store.has(vault)) store.set(vault, new Map())
        store.get(vault).set(file, req.postDataBuffer())
        return json(200, { ok: true, vault_id: vault, file_id: file, size: req.postDataBuffer().length })
    }
    if (op === 'read') { const v = store.get(vault); if (!v || !v.has(file)) return route.fulfill({ status: 404, headers: { 'access-control-allow-origin': '*' }, body: 'no' }); return route.fulfill({ status: 200, contentType: 'application/octet-stream', headers: { 'access-control-allow-origin': '*' }, body: v.get(file) }) }
    if (op === 'delete') { if (!h['x-sgraph-access-token']) return json(401, { detail: 'access token required' }); const v = store.get(vault); if (v) v.delete(file); return json(200, { ok: true }) }
    return json(404, { detail: 'Not Found' })
})

const cdp = await ctx.newCDPSession(pg)
await cdp.send('WebAuthn.enable', { enableUI: false })
await cdp.send('WebAuthn.addVirtualAuthenticator', { options: { protocol: 'ctap2', transport: 'internal', hasResidentKey: true, hasUserVerification: true, isUserVerified: true, hasPrf: true, automaticPresenceSimulation: true } })
const vectors = JSON.parse(fs.readFileSync(path.join(ROOT, 'passkey/vectors.json'), 'utf8'))

try {
    await pg.goto(B + 'passkey/'); await pg.waitForFunction(() => document.documentElement.getAttribute('data-lab') === 'ready', null, { timeout: 20000 })
    // 0
    check(/present/.test(await kv('poc0-out', 'WebAuthn')) && /yes/.test(await kv('poc0-out', 'Secure context')), 'card 0: WebAuthn present in a secure context (localhost)')
    // 5, which runs on load
    await pg.waitForFunction(() => /agree on every value|value differs/.test(document.getElementById('poc5-out').textContent), null, { timeout: 30000 })
    const t5 = await text('poc5-out')
    check(/agree on every value/.test(t5) && !/✗/.test(t5), 'card 5: the browser and sgit agree on every test vector (HKDF, PBKDF2, file ids, deterministic AES-GCM, object id)')
    check((await kv('poc5-out', 'vault_id') || '').includes(vectors.vault_id), `card 5: the vector's door id is ${vectors.vault_id}`)
    // 1
    await pg.click('#poc1-go'); await pg.waitForFunction(() => /prf\.enabled/.test(document.getElementById('poc1-out').textContent), null, { timeout: 20000 })
    check((await kv('poc1-out', 'prf.enabled')) === 'true', 'card 1: a passkey is made for this host with prf.enabled true')
    check(await pg.evaluate(() => { const s = JSON.parse(localStorage.getItem('sgit.passkey.lab')); return s && typeof s.id === 'string' && !('prfBytes' in s) && Object.keys(localStorage).every(k => k === 'sgit.passkey.lab' || k.startsWith('sgit.meter')) }), 'card 1: the browser keeps the passkey id and nothing else from the lab')
    check(await pg.evaluate(() => document.getElementById('poc1-ladder').hidden), 'card 1: the ladder is hidden when PRF is on')
    // 2, twice
    await pg.click('#poc2-go'); await pg.waitForFunction(() => /fingerprint/.test(document.getElementById('poc2-out').textContent), null, { timeout: 20000 })
    const fp1 = await text('poc2-mine')
    await pg.waitForFunction(() => /Door vault id/.test(document.getElementById('poc3-out').textContent), null, { timeout: 30000 })
    const id1 = await kv('poc3-out', 'Door vault id')
    await pg.click('#poc2-go'); await wait(1500); await pg.waitForFunction(() => /Door vault id/.test(document.getElementById('poc3-out').textContent), null, { timeout: 30000 })
    const fp2 = await text('poc2-mine'), id2 = await kv('poc3-out', 'Door vault id')
    check(/^[0-9a-f]{8}$/.test(fp1) && fp1 === fp2, `card 2: the same passkey gives the same PRF bytes twice (fingerprint ${fp1})`)
    check(/^[a-z0-9]{8}$/.test(id1) && id1 === id2 && id1 !== vectors.vault_id, `card 3: the door id is 8 of [a-z0-9] and stable (${id1})`)
    const read = await kv('poc3-out', 'Read key'), write = await kv('poc3-out', 'Write key')
    check(/\(64 characters\)/.test(read) && /\(64 characters\)/.test(write) && /\d+ ms/.test(read), 'card 3: read and write keys are 32 bytes each, hidden behind a reveal, with the PBKDF2 time shown')
    await pg.evaluate(() => [...document.querySelectorAll('#poc3-out .secret button')].find(b => /Reveal the key/.test(b.textContent)).click())
    const key = await kv('poc3-out', 'The sgit vault key')
    check(new RegExp(`^sgit_private_vault_[0-9a-f]{64}:${id1}`).test(key), 'card 3: the vault key is in sgit\'s format, passphrase:id')
    check(/sgit_public_read_[0-9a-f]{64}:[a-z0-9]{8}/.test(await kv('poc3-out', 'The published form')), 'card 3: the published read-key form is shown')
    // compare box
    await pg.fill('#poc2-other', fp1); await pg.click('#poc2-cmp-go')
    check(/The same/.test(await text('poc2-cmp-out')), 'card 2: comparing the fingerprint from another device says "the same"')
    await pg.fill('#poc2-other', '00000000'); await pg.click('#poc2-cmp-go')
    check(/Different/.test(await text('poc2-cmp-out')), 'card 2: a different fingerprint says so')
    // 4
    await pg.click('#poc4-go'); await wait(800)
    const code = await kv('poc4-out', 'Recovery code'), rdoor = await kv('poc4-out', 'Its door')
    check(/^([A-Z2-7]{4}-){6}[A-Z2-7]{2}$/.test(code) && /^[a-z0-9]{8}$/.test(rdoor) && rdoor !== id1, `card 4: a 26-character recovery code opens a different door (${rdoor})`)
    await pg.fill('#poc4-code', code.toLowerCase()); await pg.click('#poc4-check'); await wait(800)
    check((await text('poc4-check-out')).includes(rdoor), 'card 4: typing the code back gives the same door')
    // 6, against the stand-in server
    check(!(await pg.evaluate(() => document.getElementById('poc6').hidden)), 'card 6 appears once a door exists')
    check(await pg.evaluate(() => document.getElementById('poc6-create').disabled), 'card 6: create is disabled without an access key')
    await pg.click('#poc6-check'); await wait(800)
    check(/no vault at this address yet/.test(await text('poc6-out')), 'card 6: the derived address is empty before the first write')
    await pg.fill('#poc6-access', 'test-access-key-not-real'); await wait(100)
    check(!(await pg.evaluate(() => document.getElementById('poc6-create').disabled)), 'card 6: create is enabled with an access key')
    await pg.click('#poc6-create'); await pg.waitForFunction(() => /The door exists|refused/.test(document.getElementById('poc6-out').textContent), null, { timeout: 10000 })
    check(/The door exists/.test(await text('poc6-out')) && store.has(id1) && store.get(id1).size === 1, 'card 6: the door is created by writing one object with the access key and the write key')
    const [objId, bytes] = [...store.get(id1).entries()][0]
    check(/^obj-cas-imm-[0-9a-f]{12}$/.test(objId) && bytes.length > 12 + 16 + 60, `card 6: the object is content-addressed (${objId}) and is iv + ciphertext + tag`)
    check(!/"kind"|master|sgit_private/.test(bytes.toString('latin1')), 'card 6: what reached the server is ciphertext, not the record')
    await pg.click('#poc6-open'); await pg.waitForFunction(() => /Opened|Nothing opened/.test(document.getElementById('poc6-out').textContent), null, { timeout: 10000 })
    check(/decrypted with the door’s read key/.test(await text('poc6-out')) && /Opened/.test(await text('poc6-out')), 'card 6: the door opens again from the server and decrypts with the read key')
    await pg.click('#poc6-delete'); await wait(800)
    check(/Deleted/.test(await text('poc6-out')) && store.get(id1).size === 0, 'card 6: the file is deleted; the vault id is kept')
    check(await pg.evaluate(() => Object.keys(localStorage).every(k => k === 'sgit.passkey.lab' || k.startsWith('sgit.meter')) && ![...Object.values(localStorage), ...Object.values(sessionStorage)].some(v => /test-access-key/.test(v))), 'the access key is not in storage, and the lab wrote only its one key')
    check(seen.some(s => /^PUT \/api\/vault\/write\//.test(s)) && seen.some(s => /^GET \/api\/vault\/read\//.test(s)) && seen.some(s => /^DELETE \/api\/vault\/delete\//.test(s)), `the calls the server saw: ${[...new Set(seen.map(s => s.split('/').slice(0, 4).join('/')))].join(', ')}`)
    const others = [...hosts].filter(h => !h.startsWith('localhost') && h !== 'dev.send.sgraph.ai')
    check(others.length === 0, `no request to any other host${others.length ? ': ' + others.join(', ') : ''}`)
    // phone width
    const m = await browser.newPage({ viewport: { width: 390, height: 800 } })
    await m.goto(B + 'passkey/'); await m.waitForTimeout(1500)
    check((await m.evaluate(() => document.documentElement.scrollWidth)) <= 390, 'no sideways scroll at 390px')
    check(errors.length === 0, `no page errors${errors.length ? ': ' + errors.join(' | ') : ''}`)
} finally {
    await browser.close()
    server.close()
}
console.log(failed ? `${failed} FAILED` : 'ALL PASSKEY LAB CHECKS PASS')
process.exit(failed ? 1 : 0)
