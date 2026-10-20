#!/usr/bin/env node
/* viewer_vault.mjs: publish the newsroom's vault viewer (card 079), the app every reader vault opens with.
 *
 *   NEWSROOM_ACCESS_KEY=<access key> node admin/build/viewer_vault.mjs                    # make the viewer vault, once
 *   NEWSROOM_ACCESS_KEY=<…> NEWSROOM_VIEWER_VAULT_KEY=<its vault key> node admin/build/viewer_vault.mjs   # publish a new version
 *   node admin/build/viewer_vault.mjs --mock                                              # the same, against the mock (the test)
 *
 * The viewer's source is vault/vault-app/ (viewer.js, index.html, README.md, demo/, and vault-app.json, which goes
 * in as .vault/app.json). This script writes those files into the viewer vault as one publish, derives the vault's
 * read key, and records the vault id and that PUBLIC read key in admin/content/vaults/vault-viewer.json, which the
 * vault pane reads to link the viewer into each reader vault. The vault key and the access key come from the
 * environment and are never written to a file; on the first run the new vault key is printed once, to stderr, to
 * be kept by whoever runs it (as NEWSROOM_VIEWER_VAULT_KEY for the next run).
 * Options: --endpoint <url> (default https://dev.send.sgraph.ai), --out <file> (default the json above), --mock.
 */
import vm from 'vm'
import fs from 'fs'
import path from 'path'

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..')
const SRC = path.join(ROOT, 'vault/vault-app')
const args = process.argv.slice(2), opt = n => { const i = args.indexOf(n); return i >= 0 ? args[i + 1] : null }
const MOCK = args.includes('--mock')
const OUT = opt('--out') || path.join(ROOT, 'admin/content/vaults/vault-viewer.json')
const VENDOR = path.join(ROOT, 'assets/vendor/sg-vault/v0.2.3')
const ORDER = ['sg-send/sg-send-crypto.js', 'sg-send/sg-send.js', 'sg-vault/sg-vault-crypto.js', 'sg-vault/sg-vault-object-store.js', 'sg-vault/sg-vault-ref-manager.js',
               'sg-vault/sg-vault-commit.js', 'sg-vault/sg-vault.js', 'sg-vault/sg-vault--file-ops.js', 'sg-vault/sg-vault--folder-ops.js', 'sg-vault/sg-vault--sync.js',
               'sg-vault/sg-vault--history.js', 'sg-vault/sg-vault--branches.js']
for (const f of ORDER) vm.runInThisContext(fs.readFileSync(path.join(VENDOR, f), 'utf8'), { filename: f })
vm.runInThisContext(fs.readFileSync(path.join(ROOT, 'assets/vendor/sg-vault/local/sg-vault--create-with-id.js'), 'utf8'), { filename: 'sg-vault--create-with-id.js' })
vm.runInThisContext('globalThis.SGSend = SGSend; globalThis.SGVault = SGVault; globalThis.SGVaultCrypto = SGVaultCrypto; globalThis.SGSendCrypto = SGSendCrypto')
const NV = await import(path.join(ROOT, 'assets/newsroom-vault.js'))

let mock = null, endpoint = opt('--endpoint') || 'https://dev.send.sgraph.ai', token = process.env.NEWSROOM_ACCESS_KEY || ''
if (MOCK) { const { startMock } = await import('./vault-mock.mjs'); mock = await startMock(); endpoint = mock.base; token = mock.token }
if (!token) { console.error('viewer_vault: NEWSROOM_ACCESS_KEY is not set: making or updating a vault needs the access key, from the environment, never a file'); process.exit(2) }

// every file of the viewer, as it goes into the vault
const files = []
const walk = (dir, rel = '') => { for (const e of fs.readdirSync(dir, { withFileTypes: true })) { const r = rel + '/' + e.name; if (e.isDirectory()) walk(path.join(dir, e.name), r); else files.push(r) } }
walk(SRC)
const target = r => r === '/vault-app.json' ? '/.vault/app.json' : r

try {
    const sg = NV.client({ endpoint, token })
    const key = process.env.NEWSROOM_VIEWER_VAULT_KEY || ''
    const v = key ? await NV.openVault(sg, key, { cloneBranch: 'nr-viewer-publisher' }) : await NV.createVault(sg, { name: 'newsroom-viewer', description: 'The newsroom.sgit.ai vault viewer: the app every reader vault opens with, linked read-only.' })
    let wrote = 0
    for (const r of files) {
        const t = target(r), parts = t.split('/').filter(Boolean), name = parts.pop(), folder = '/' + parts.join('/')
        const text = fs.readFileSync(path.join(SRC, r), 'utf8')
        const now = await NV.readText(v, t).catch(() => null)
        if (now === text) continue
        await NV.writeFile(v, folder, name, text); wrote++
    }
    if (wrote) await NV.publish(v)
    const hex = await NV.readKeyHex(v)
    const version = (/var VERSION = '([^']+)'/.exec(fs.readFileSync(path.join(SRC, 'viewer.js'), 'utf8')) || [])[1] || ''
    const rec = { vault_id: v.vaultId || v._vaultId, read_key: 'sgit_public_' + 'read_' + hex, remote: endpoint, viewer_version: version, published: new Date().toISOString().slice(0, 10),
                  note: 'The newsroom vault viewer (card 079). The read key is public on purpose: every reader vault links this vault read-only. Source: vault/vault-app/; publisher: admin/build/viewer_vault.mjs.' }
    fs.mkdirSync(path.dirname(OUT), { recursive: true })
    fs.writeFileSync(OUT, JSON.stringify(rec, null, 1) + '\n')
    console.log(`viewer_vault: ${key ? 'updated' : 'made'} ${rec.vault_id} at ${endpoint}, ${wrote} file(s) written of ${files.length}; viewer ${version}; ${path.relative(ROOT, OUT)} records its public read key`)
    if (!key && !MOCK) console.error(`\nKeep this vault key; it is shown once and written nowhere. Pass it as NEWSROOM_VIEWER_VAULT_KEY to publish a new version:\n  ${NV.prefixedKey(v)}\n`)
} finally { if (mock) await mock.close() }
