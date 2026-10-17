#!/usr/bin/env node
/* test_vault_open.mjs: the vault, opened (cards 077, 078, 079), in Chromium against the mock of the vault API.
 *
 *   node admin/build/test_vault_open.mjs
 *
 * The shared viewer is published into the mock by admin/build/viewer_vault.mjs; device A reads, makes the account
 * and updates, and the update links the viewer into the reader vault and makes it the vault's app (the link file, the
 * owner record with the viewer's read key, .vault/app.json, index.html). The entry page then runs in a stand-in for
 * the vault app's host, reading the viewer's code from the viewer vault opened with the owner record alone, and
 * renders the account. The Calls tab names the calls and decrypts a commit, a tree and a ref. Device B (the same
 * passkey, a cleared browser) is offered A as the same kind of browser, adds itself as a new device, updates, and
 * merges both into one: one row, the same totals, B's browser now filed as A, the alias in the vault. The browse page
 * lists the files, opens one, lists the commits and the tree at one, keeps the master's files behind Reveal, and
 * hands the SG/Vault app (a stand-in at its origin) the reader vault's READ key and nothing else.
 * Skips (exit 0) when Playwright or Chromium is missing.
 */
import http from 'http'
import fs from 'fs'
import os from 'os'
import path from 'path'
import { execSync, spawn } from 'child_process'
import { startMock } from './vault-mock.mjs'

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..')
let chromium
try { ({ chromium } = await import('playwright')) } catch (e) {
    try { const g = execSync('npm root -g').toString().trim(); ;({ chromium } = await import(path.join(g, 'playwright', 'index.mjs'))) }
    catch (e2) { console.log('SKIP: playwright is not installed'); process.exit(0) }
}
const types = { '.html': 'text/html', '.js': 'text/javascript', '.mjs': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.webp': 'image/webp', '.png': 'image/png', '.svg': 'image/svg+xml', '.md': 'text/markdown', '.woff2': 'font/woff2' }
const server = http.createServer((req, res) => {
    let p = decodeURIComponent(new URL(req.url, 'http://x').pathname)
    if (p.endsWith('/')) p += 'index.html'
    const f = path.join(ROOT, p)
    if (!f.startsWith(ROOT) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { res.writeHead(404); res.end(); return }
    res.writeHead(200, { 'content-type': types[path.extname(f)] || 'application/octet-stream' }); res.end(fs.readFileSync(f))
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
const mock = await startMock()

// the shared viewer, published into the mock by its own publisher
const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'nr-viewer-'))
// asynchronously: the mock answers from this process, so a synchronous child would wait for it for ever
const pub = await new Promise(resolve => {
    const c = spawn(process.execPath, [path.join(ROOT, 'admin/build/viewer_vault.mjs'), '--endpoint', mock.base, '--out', path.join(tmp, 'viewer.json')], { env: { ...process.env, NEWSROOM_ACCESS_KEY: mock.token } })
    let stdout = '', stderr = ''; c.stdout.on('data', d => { stdout += d }); c.stderr.on('data', d => { stderr += d })
    const timer = setTimeout(() => c.kill(), 180000)
    c.on('close', status => { clearTimeout(timer); resolve({ status, stdout, stderr }) })
})
const viewer = pub.status === 0 ? JSON.parse(fs.readFileSync(path.join(tmp, 'viewer.json'), 'utf8')) : null
check(viewer && /^sgit_public_read_[0-9a-f]{64}$/.test(viewer.read_key) && !/sgit_private/.test(pub.stdout + JSON.stringify(viewer)) && (pub.stderr.match(/sgit_private_vault_/g) || []).length === 1, `viewer_vault.mjs publishes the viewer, records only its public read key, and shows the new vault key once, on stderr (${viewer ? viewer.vault_id : pub.stderr.slice(0, 200)})`)

const ctx = await browser.newContext({ viewport: { width: 1400, height: 950 } })
const pg = await ctx.newPage()
const errors = [], hosts = new Set()
pg.on('pageerror', e => errors.push(e.message))
pg.on('request', r => { try { hosts.add(new URL(r.url()).host) } catch (e) { /* fine */ } })
await ctx.route('https://dev.send.sgraph.ai/**', async route => {
    const req = route.request(), u = new URL(req.url()), m = req.method()
    const headers = {}
    for (const [k, v] of Object.entries(req.headers())) if (!/^(host|origin|referer|content-length|connection|accept-encoding)$/i.test(k) && !k.startsWith(':')) headers[k] = v
    const data = req.postDataBuffer()
    const r = await fetch(mock.base + u.pathname + u.search, { method: m, headers, body: data && m !== 'GET' && m !== 'HEAD' ? data : undefined })
    const out = {}; r.headers.forEach((v, k) => { if (!/^(content-length|transfer-encoding|connection)$/i.test(k)) out[k] = v })
    await route.fulfill({ status: r.status, headers: out, body: Buffer.from(await r.arrayBuffer()) })
})
// the site's record of the viewer, as the publisher would commit it, for the endpoint the page uses
await ctx.route('**/admin/content/vaults/vault-viewer.json', route => route.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify({ ...viewer, remote: 'https://dev.send.sgraph.ai' }) }))
// a stand-in for the SG/Vault app at its own origin: it completes the embed handshake and keeps the key it is handed
const stub = `<!doctype html><script>addEventListener('message', function (e) { if (e.data && e.data.sg === 'vault-open') { window.__got = e.data; parent.postMessage({ sg: 'vault-ready', fileCount: 7 }, '*') } }); parent.postMessage({ sg: 'vault-embed-ready' }, '*')</script><p>stand-in</p>`
await ctx.route('https://dev.vault.sgraph.ai/**', route => route.fulfill({ status: 200, contentType: 'text/html', body: stub }))
const cdp = await ctx.newCDPSession(pg)
await cdp.send('WebAuthn.enable', { enableUI: false })
await cdp.send('WebAuthn.addVirtualAuthenticator', { options: { protocol: 'ctap2', transport: 'internal', hasResidentKey: true, hasUserVerification: true, isUserVerified: true, hasPrf: true, automaticPresenceSimulation: true } })

const wait = ms => pg.waitForTimeout(ms)
const text = sel => pg.evaluate(sel => { const e = document.querySelector(sel); return e ? e.textContent : '' }, sel)
const paneText = () => text('#sgit-vault-pane')
const until = (re, ms = 90000) => pg.waitForFunction(re => new RegExp(re).test((document.getElementById('sgit-vault-pane') || {}).textContent || ''), re, { timeout: ms })
const readArticle = async rel => { await pg.goto(B + rel); await pg.waitForSelector('.vault-btn', { timeout: 20000 }); await pg.evaluate(() => window.scrollTo(0, document.body.scrollHeight)); await wait(900); await pg.evaluate(() => window.scrollTo(0, 0)); await wait(300) }
const openTab = async tab => { if (!(await pg.evaluate(() => document.documentElement.classList.contains('vault-open')))) await pg.click('.vault-btn'); await wait(300); await pg.click(`#vault-tab-${tab}`); await wait(250) }
const shot = async (name, sel) => { if (!process.env.SHOTS) return; const el = sel ? await pg.$(sel) : null; await (el || pg).screenshot({ path: path.join(process.env.SHOTS, name) }) }   // SHOTS=<dir>: the cards' screenshots
const inVault = fn => pg.evaluate(async src => {          // read the account's vaults with the session, as an app would not: the test's own eyes
    const NV = await import('/assets/newsroom-vault.js'); const s = JSON.parse(sessionStorage.getItem('sgit.vault.session'))
    const sg = NV.client({ endpoint: 'https://dev.send.sgraph.ai', token: s.token })
    const u = await NV.unlock({ sgSend: sg, door: s.door, cloneBranch: 'nr-test-eyes' + Math.random().toString(36).slice(2, 6) })
    return (new Function('NV', 'u', 'sg', 'return (async () => {' + src + '})()'))(NV, u, sg)
}, fn)

try {
    // ---- A: read, make the account, update: the update links the viewer
    await readArticle('articles/the-passkey-opens-the-vault.html')
    await openTab('vault')
    check(!(await pg.$('#sgit-vault-pane input[type=text]')) && /Open with your passkey/.test(await paneText()), 'locked: the two ways in, and nothing to name first')
    await pg.click('#vault-enable'); await until('No passkey answered|No door here|Opening')
    if (/No passkey answered/.test(await paneText())) { await pg.click('#sgit-vault-pane button:has-text("Make a passkey for this site")'); await until('A passkey was made'); await pg.click('#vault-enable') }
    await until('No door here for this path yet')
    await pg.fill('#sgit-vault-pane input[type=password]', mock.token)
    await pg.click('#vault-create'); await until('Your recovery code|was not|Error', 120000)
    const deviceA = await pg.evaluate(() => localStorage.getItem('sgit.device-branch'))
    await pg.waitForSelector('#vault-sync', { timeout: 60000 })
    await pg.click('#vault-sync'); await until('Updated:|not updated', 120000)
    check(/newsroom’s viewer is now this vault’s app/i.test(await text('#vault-synced')), `the update links the shared viewer and makes it the vault's app (${(await text('#vault-synced')).trim().slice(0, 140)})`)
    const inst = await inVault(`
        const link = await NV.readJson(u.reader, '/newsroom-viewer.link.json'), ro = await NV.readJson(u.reader, '/.vault/owner/ro-links.json')
        const app = await NV.readJson(u.reader, '/.vault/app.json'), entry = await NV.readText(u.reader, '/index.html'), idx = await NV.readJson(u.reader, '/activity/index.json')
        return { link, ro, app, entry, idx }`)
    const rec = inst.ro && inst.ro[inst.link && inst.link.ref_id]
    check(inst.link && inst.link.vault_id === viewer.vault_id && inst.link.type === 'vault' && !JSON.stringify(inst.link).match(/[0-9a-f]{64}|read_key/), 'the link file names the viewer vault and carries no key')
    check(rec && rec.vault_id === viewer.vault_id && /^ref-pid-muw-[0-9a-f]{12}$/.test(rec.ref_file_id) && Buffer.from(rec.read_key, 'base64').toString('hex') === viewer.read_key.slice(-64), 'the owner record holds the viewer’s read key and ref file id, in the vault UI’s format')
    check(inst.app && inst.app.entry === 'index.html' && inst.app.present === true && inst.app.newsroom && inst.app.newsroom.viewer === viewer.vault_id && inst.entry.includes('newsroom-viewer/viewer.js') && inst.idx.devices.includes(deviceA), 'the vault’s app is the entry page that loads the viewer; the index lists the device files')
    // the entry page in a stand-in for the vault app's host: window.sg reads the reader vault, and the viewer's code from the viewer vault opened with the owner record alone
    const shown = await pg.evaluate(async ({ entry, rec }) => {
        const NV = await import('/assets/newsroom-vault.js'); const s = JSON.parse(sessionStorage.getItem('sgit.vault.session'))
        const sg = NV.client({ endpoint: 'https://dev.send.sgraph.ai', token: '' })
        const u = await NV.unlock({ sgSend: NV.client({ endpoint: 'https://dev.send.sgraph.ai', token: s.token }), door: s.door, cloneBranch: 'nr-test-host' })
        const child = await SGVault.openReadOnly(sg, rec.vault_id, rec.read_key, rec.ref_file_id)
        window.__fakeSg = { vfs: { readText: async p => { const t = p.startsWith('newsroom-viewer/') ? await NV.readText(child, '/' + p.slice(16)) : await NV.readText(u.reader, '/' + p); if (t == null) throw Object.assign(new Error('ENOENT ' + p), { code: 'ENOENT' }); return t } } }
        const f = document.createElement('iframe'); f.style.width = '1100px'; f.style.height = '900px'; document.body.append(f)
        f.srcdoc = entry.replace('<body>', '<body><script>window.sg = { vfs: parent.__fakeSg.vfs, loadJs: async function (p) { var s = document.createElement("script"); s.textContent = await parent.__fakeSg.vfs.readText(p); document.head.append(s) } }<\/script>')
        for (let i = 0; i < 100; i++) { await new Promise(r => setTimeout(r, 150)); const d = f.contentDocument; if (d && d.querySelector('.nv .tiles')) return d.querySelector('#app').textContent }
        return f.contentDocument ? f.contentDocument.body.textContent : ''
    }, { entry: inst.entry, rec })
    check(/Your newsroom vault/.test(shown) && /pages read/.test(shown) && /shared/.test(shown) && /£4\.\d\d/.test(shown) && !/could not be read/.test(shown), `the entry page loads the viewer from the linked vault and renders the account (${shown.replace(/\s+/g, ' ').slice(0, 120)}…)`)

    // ---- the Calls tab: named, and decrypted on a press
    await openTab('calls')
    const kinds = await pg.evaluate(() => [...document.querySelectorAll('#calls-list .badge')].map(b => b.textContent))
    check(kinds.length > 5 && kinds.includes('object') && kinds.includes('ref'), `the Calls tab names each call (${kinds.length}: ${[...new Set(kinds)].join(', ')})`)
    const decoded = await pg.evaluate(async () => {
        const seen = new Set()
        for (let i = 0; i < 60; i++) {
            const rows = [...document.querySelectorAll('#calls-list > li.call')]; if (i >= rows.length) break
            rows[i].querySelector('.call-h').click()
            for (let k = 0; k < 40; k++) { await new Promise(r => setTimeout(r, 60)); const r2 = document.querySelectorAll('#calls-list > li.call')[i]; if (r2 && !/Decoding…/.test(r2.textContent)) break }
            const r3 = document.querySelectorAll('#calls-list > li.call')[i]
            for (const p of r3.querySelectorAll('.call-item > p b')) seen.add(p.textContent)
            for (const it of r3.querySelectorAll('.call-item')) if (it.querySelector('p b') && it.querySelector('p b').textContent === 'a commit' && !window.__commitText) window.__commitText = it.textContent
            r3.querySelector('.call-h').click(); await new Promise(r => setTimeout(r, 40))
            if (seen.has('a commit') && seen.has('a tree (a folder listing)') && seen.has('a ref (which commit is current)')) break
        }
        return { kinds: [...seen], commit: window.__commitText || '' }
    })
    if (process.env.SHOTS) { await pg.evaluate(() => document.documentElement.classList.add('vault-wide')); await openTab('calls'); await pg.evaluate(async () => { for (const li of document.querySelectorAll('#calls-list > li.call')) { li.querySelector('.call-h').click(); for (let k = 0; k < 30; k++) { await new Promise(r => setTimeout(r, 60)); if (!/Decoding…/.test(li.textContent)) break } const l2 = document.querySelector(`#calls-list > li.call[data-n="${li.dataset.n}"]`); if (l2 && /a commit/.test(l2.textContent)) { l2.scrollIntoView(); return } if (l2) l2.querySelector('.call-h').click(); await new Promise(r => setTimeout(r, 40)) } }); await wait(400); await shot('078-calls.png', '#sgit-vault-pane'); await pg.evaluate(() => document.documentElement.classList.remove('vault-wide')) }
    check(decoded.kinds.includes('a commit') && decoded.kinds.includes('a tree (a folder listing)') && decoded.kinds.includes('a ref (which commit is current)'), `opened, a call shows what it carried, decrypted: ${decoded.kinds.join(', ')}`)
    check(/message/.test(decoded.commit) && /tree/.test(decoded.commit) && /obj-cas-imm-/.test(decoded.commit), `a commit shows its message, its tree and its parents (${decoded.commit.replace(/\s+/g, ' ').slice(0, 120)})`)

    // ---- device B: the same passkey, a cleared browser; the chooser suggests A; B adds itself, updates
    await pg.evaluate(() => { localStorage.clear(); sessionStorage.clear() })
    await readArticle('articles/a-link-to-a-persona.html')
    await openTab('vault')
    await pg.click('#vault-enable'); await until('Which device is this|No door here|Error', 120000)
    const sug = await pg.evaluate(() => { const c = document.querySelector('#vault-devices label.device.suggested'); return c ? { text: c.textContent, checked: c.querySelector('input').checked } : null })
    check(sug && sug.checked && /same kind of browser/.test(sug.text) && sug.text.includes(deviceA), `the chooser offers A first, as the same kind of browser, already picked (${sug && sug.text.replace(/\s+/g, ' ').slice(0, 90)})`)
    await shot('077-chooser.png', '#sgit-vault-pane')
    check(/Continue as /.test(await text('#vault-choose')), `the button says where this browser goes: “${(await text('#vault-choose')).trim()}”`)
    await pg.fill('#vault-new-label', 'iPad 2')
    check(/Continue as a new device: iPad 2/.test(await text('#vault-choose')), 'typing a name picks a new device, and the button says so')
    await pg.click('#vault-choose'); await pg.waitForSelector('#vault-merged', { timeout: 60000 }); await until('in the master vault, in memory here', 60000)
    const deviceB = await pg.evaluate(() => localStorage.getItem('sgit.device-branch'))
    await readArticle('articles/sixteen-notes-i-did-not-want-to-lose.html')
    await openTab('vault'); await pg.waitForSelector('#vault-sync', { timeout: 60000 })
    await pg.click('#vault-sync'); await until('Updated:|not updated', 120000)
    await until('All, 2 device', 60000)
    const totalBefore = await pg.evaluate(() => [...document.querySelectorAll('#vault-across tr.total td')].map(td => td.textContent.trim()))

    // ---- merge both into one
    await pg.check(`#vault-across input[data-merge="${deviceA}"]`); await pg.check(`#vault-across input[data-merge="${deviceB}"]`)
    await pg.waitForSelector('#vault-merge-into', { timeout: 10000 })
    check(/Merge 2 devices/.test(await text('#vault-merge-bar')) && /nothing is deleted/.test(await text('#vault-merge-bar')), 'picking two devices offers the merge, and says nothing is deleted')
    await pg.selectOption('#vault-merge-into', deviceA); await pg.fill('#vault-merge-label', 'Laptop')
    await pg.evaluate(() => document.getElementById('vault-across').scrollIntoView()); await shot('077-merge.png', '#sgit-vault-pane')
    await pg.click('#vault-merge-devices'); await pg.waitForSelector('#vault-devices-merged', { timeout: 120000 }); await until('All, 1 device', 60000)
    const totalAfter = await pg.evaluate(() => [...document.querySelectorAll('#vault-across tr.total td')].map(td => td.textContent.trim()))
    check(totalAfter[2] === totalBefore[2] && totalAfter[3] === totalBefore[3] && totalAfter[6] === totalBefore[6], `one row, and the same reads, spend and balance (${totalBefore.slice(2).join(' / ')} → ${totalAfter.slice(2).join(' / ')})`)
    check((await pg.evaluate(() => localStorage.getItem('sgit.device-branch'))) === deviceA && /Laptop \(here\)/.test(await text('#vault-across')), 'this browser was one of the merged devices: it is filed as the merged one now, under its new name')
    const al = await inVault(`return { aliases: await NV.readJson(u.reader, '/activity/aliases.json'), files: await NV.listFiles(u.reader, '/activity/devices') }`)
    check(al.aliases && al.aliases.aliases[deviceB] === deviceA && al.aliases.merges.length === 1 && al.files.length === 1 && al.files[0] === deviceA + '.json', 'the vault records the alias and the merge, and holds one device file')

    // ---- the browse page
    await pg.goto(B + 'vault/browse.html'); await pg.waitForSelector('#browse-files .tree', { timeout: 60000 })
    check(await pg.evaluate(() => !!document.querySelector('#browse-files [data-path="/activity"]') && !!document.querySelector('#browse-files [data-path="/newsroom-viewer.link.json"]')), 'the browse page lists the reader vault’s files, the viewer’s link among them')
    await pg.click('#browse-files [data-path="/activity/devices"]'); await pg.waitForSelector(`#browse-files [data-path="/activity/devices/${deviceA}.json"]`, { timeout: 30000 })
    await pg.click(`#browse-files [data-path="/activity/devices/${deviceA}.json"]`); await pg.waitForSelector('#browse-content', { timeout: 30000 })
    check(/"reads"/.test(await text('#browse-content')) && /"merged_from"/.test(await text('#browse-content')), 'a file opens: the merged device’s file, its reads and what it was merged from')
    await pg.evaluate(() => { document.documentElement.classList.remove('vault-open'); window.scrollTo(0, document.getElementById('browse-mount').offsetTop - 20) }); await shot('079-browse.png', '#browse-mount')
    const nCommits = await pg.evaluate(() => document.querySelectorAll('#browse-commits li').length)
    check(nCommits >= 5, `the commits are listed (${nCommits})`)
    await pg.click('#browse-commits li:last-child .tree-btn'); await pg.waitForFunction(() => /Files at/.test(document.querySelector('.browse-grid').textContent), null, { timeout: 30000 })
    check(/Files at/.test(await text('.browse-grid')), 'a commit opens the tree as it was then')
    await pg.click('#browse-master'); await pg.waitForSelector('#browse-files .tree', { timeout: 30000 })
    await pg.click('#browse-files [data-path="/reader.json"]'); await pg.waitForSelector('#browse-reveal', { timeout: 30000 })
    check(!(await pg.$('#browse-content')) && /holds keys/.test(await text('#browse-view')), 'the master’s files open only behind Reveal')
    await pg.click('#browse-reader'); await pg.waitForSelector('#browse-open-app', { timeout: 30000 })
    await pg.click('#browse-open-app'); await pg.waitForFunction(() => /Opened read-only/.test((document.getElementById('browse-embed') || {}).textContent || ''), null, { timeout: 30000 }).catch(async e => { console.log('EMBED TEXT:', await text('#browse-embed'), '| errors:', errors.join(' || '), '| has SGVaultEmbed:', await pg.evaluate(() => typeof window.SGVaultEmbed), '| frames:', pg.frames().map(f => f.url().slice(0, 80)).join(' , ')); throw e })
    const handed = await (async () => { for (const f of pg.frames()) { if (f.url().startsWith('https://dev.vault.sgraph.ai')) { const k = await f.evaluate(() => window.__got && window.__got.key).catch(() => null); if (k) return k } } return '' })()
    const readerHex = await inVault(`return { id: u.reader.vaultId || u.reader._vaultId, hex: await NV.readKeyHex(u.reader) }`)
    check(handed === `sgit_rk1_${readerHex.hex}:${readerHex.id}`, `the SG/Vault app is handed the reader vault’s read key, and nothing else (${handed.slice(0, 18)}…:${readerHex.id})`)

    // ---- hygiene
    const others = [...hosts].filter(x => !x.startsWith('localhost') && x !== 'dev.send.sgraph.ai' && x !== 'dev.vault.sgraph.ai')
    check(others.length === 0, `no request to any other host${others.length ? ': ' + others.join(', ') : ''}`)
    check(await pg.evaluate(() => !Object.values(localStorage).concat(Object.values(sessionStorage).filter(v => !/door/.test(v))).some(v => /sgit_private|mock-/.test(v))), 'no vault key or access key in local storage, nor in session storage outside the session record')
    check(errors.length === 0, `no page errors${errors.length ? ': ' + errors.slice(0, 3).join(' | ') : ''}`)
} finally {
    await browser.close(); server.close(); await mock.close(); fs.rmSync(tmp, { recursive: true, force: true })
}
console.log(failed ? `${failed} FAILED` : 'ALL VAULT-OPENED CHECKS PASS')
process.exit(failed ? 1 : 0)
