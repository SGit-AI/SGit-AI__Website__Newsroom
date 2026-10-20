#!/usr/bin/env node
/**
 * vault_fetch.mjs: a wire's vault as files on disk, read with the site's own reader (wire/vault-reader.js) and its
 * published read key. No sgit client, no package to install: Node's fetch and Web Crypto are enough.
 *
 *   node admin/build/vault_fetch.mjs --out <dir>                 every wire in admin/build/wire-vault*.json
 *   node admin/build/vault_fetch.mjs --out <dir> --wire owasp    one wire (industry for the Industry Wire)
 *
 * Writes <dir>/<slug>/ shaped like a clone for what admin/build/wire.py reads (data/*, docs/*, README.md), plus
 * <dir>/<slug>/.vault-head.json with the commit id and message. Then: python3 admin/build/wire.py --from <dir>/industry
 * --from owasp=<dir>/owasp ... Why it exists: the newsroom's morning routine runs in a fresh container where installing
 * the sgit client from PyPI was refused by the session's permission check ("Code from External", 14 to 16 October 2026);
 * reading a public vault needs no client, only the read key the site already publishes.
 */
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { VaultReader } from '../../wire/vault-reader.js'

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..')
const args = process.argv.slice(2), opt = k => { const i = args.indexOf(k); return i >= 0 ? args[i + 1] : null }
const out = opt('--out'), only = opt('--wire')
if (!out) { console.error('usage: node admin/build/vault_fetch.mjs --out <dir> [--wire <slug|industry>]'); process.exit(2) }
const TOP = ['data', 'docs', 'README.md']           // what wire.py and the snapshot read; briefs/ and pipeline/ are the desk's
const cfgs = fs.readdirSync(path.join(ROOT, 'admin/build')).filter(f => /^wire-vault(\.[a-z0-9-]+)?\.json$/.test(f)).sort()
    .map(f => JSON.parse(fs.readFileSync(path.join(ROOT, 'admin/build', f), 'utf8')))
const SAFE = /^[A-Za-z0-9_.-]+(\/[A-Za-z0-9_.-]+)*$/   // a vault path becomes a file path only when it is plain
let failed = 0
for (const cfg of cfgs) {
    const slug = cfg.slug || 'industry'
    if (only && only !== slug) continue
    try {
        const r = await new VaultReader({ ...cfg, store: null }).init()
        const head = await r.open({ force: true })
        const files = await r.files(TOP.filter(t => !t.includes('.')))
        const dir = path.join(out, slug)
        fs.rmSync(dir, { recursive: true, force: true })
        let n = 0, bytes = 0
        for (const [p, f] of Object.entries(files)) {
            if (!f.blob_id || !(TOP.includes(p) || TOP.some(t => p.startsWith(t + '/'))) || !SAFE.test(p) || p.split('/').includes('..')) continue
            const body = await r.object(f.blob_id)
            const dest = path.join(dir, p)
            fs.mkdirSync(path.dirname(dest), { recursive: true })
            fs.writeFileSync(dest, body)
            n++; bytes += body.length
        }
        fs.writeFileSync(path.join(dir, '.vault-head.json'), JSON.stringify({ vault: cfg.vault_id, commit: head.commitId, message: head.message, fetched_at: new Date().toISOString() }, null, 1) + '\n')
        console.log(`${slug}: vault ${cfg.vault_id}, commit ${String(head.commitId).replace(/^obj-cas-imm-/, '').slice(0, 12)}, ${n} files, ${bytes} bytes -> ${dir}`)
    } catch (e) {
        failed++
        console.error(`${slug}: ${e && e.message || e}`)
    }
}
process.exit(failed ? 1 : 0)
