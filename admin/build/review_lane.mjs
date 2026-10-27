#!/usr/bin/env node
/* review_lane.mjs: the review lane (card 091), where reviewers outside the newsroom send their reviews.
 *
 *   SG_SEND_ACCESS_TOKEN=<access key> node admin/build/review_lane.mjs create [--to <pki fingerprint>]
 *       make the lane, once: a vault of its own on the vault server, an append lane on it, and a key pair for it.
 *       Writes the PUBLIC half to admin/content/reviews/lane.json (the vault id, the fingerprint, the public key) and
 *       the send link and its QR code (link + QR: what reviewers are given) to --out (default: a folder in the
 *       system's temp directory, never the repository). The lane's secret (the private key, the enum key, the vault
 *       key) is printed nowhere: it is sealed to the editor's key in pki.sgit.ai's register (--to; Dinis Cruz's by
 *       default) as a pki.sgit.ai message link, which only that key opens. The editor keeps it in the environment
 *       as REVIEW_LANE_SECRET for the scheduled run.
 *
 *   REVIEW_LANE_SECRET=<secret> node admin/build/review_lane.mjs drain [--taken <file>] [--mark] [--dry]
 *       open everything waiting in the lane, check every record (assets/reviews/record.js, the same rules as the send
 *       page), write each new one to admin/content/articles/reviews/<slug>/<date>__<reviewer>.json, register a new
 *       reviewer, and print what arrived for the editor. A record already in the repository (same reviewer, article
 *       and text) is not written twice. --taken writes the ids of the messages taken to <file> (default: the system's
 *       temp directory), for mark; --mark marks them processed at once; --dry writes nothing.
 *
 *   REVIEW_LANE_SECRET=<secret> node admin/build/review_lane.mjs mark [--taken <file>]
 *       mark the messages a drain took as processed on the server, so the next drain does not see them again. The
 *       scheduled run calls it after the records are committed and pushed, so a failed push loses nothing.
 *
 * For the test (admin/build/test_review_lane.mjs, against admin/build/vault-mock.mjs): --endpoint <url> talks to another
 * server; create --unsealed writes the secret to --out/secret.txt and lane.json to --out instead of the repository;
 * create --secret-out <file> also writes the secret, unsealed, to <file> (mode 600) for a smoke test; delete it after.
 * drain --into <dir> writes the records and reviewers.json under <dir> instead; --status <file> reads another status.json.
 *
 * The lane is an append lane (https://sgit.ai/api/append-lanes.html): anyone with the link can add a message and
 * nobody can read one without the enum key; every message is sealed in the browser to the lane's public key (sgit's
 * hybrid v2 envelope, the reader inbox's code: assets/vault-pane/inbox.js). The secret is base64 of
 * { v, vault, endpoint, token, enum_key, public, private, fingerprint, vault_key } and comes from the environment only.
 */
import vm from 'vm'
import fs from 'fs'
import os from 'os'
import path from 'path'
import { execFileSync } from 'child_process'
import { pathToFileURL } from 'url'

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..')
const args = process.argv.slice(2), opt = n => { const i = args.indexOf(n); return i >= 0 ? args[i + 1] : null }, has = n => args.includes(n)
const cmd = args[0]
const imp = p => import(pathToFileURL(path.join(ROOT, p)).href)
const I = await imp('assets/vault-pane/inbox.js')
const R = await imp('assets/reviews/record.js')
const INTO = opt('--into') ? path.resolve(opt('--into')) : ROOT
const REVIEWS = path.join(INTO, 'admin/content/articles/reviews')
const REG = path.join(INTO, 'admin/content/reviews/reviewers.json')
const unsealed = has('--unsealed')
const endpoint = opt('--endpoint') || I.ENDPOINT

const linkCode = rec => `rv1.${rec.vault}.${rec.token}.${I.b64url(I.unb64(rec.public))}`
const linkUrl = rec => `https://newsroom.sgit.ai/reviews/send.html#${linkCode(rec)}`

async function create() {
    const token = process.env.SG_SEND_ACCESS_TOKEN || process.env.NEWSROOM_ACCESS_KEY || ''
    if (!token) { console.error('review_lane: create needs the vault server access key in SG_SEND_ACCESS_TOKEN (or NEWSROOM_ACCESS_KEY)'); process.exit(2) }
    const VENDOR = path.join(ROOT, 'assets/vendor/sg-vault/v0.2.3')
    for (const f of ['sg-send/sg-send-crypto.js', 'sg-send/sg-send.js', 'sg-vault/sg-vault-crypto.js', 'sg-vault/sg-vault-object-store.js', 'sg-vault/sg-vault-ref-manager.js',
                     'sg-vault/sg-vault-commit.js', 'sg-vault/sg-vault.js', 'sg-vault/sg-vault--file-ops.js', 'sg-vault/sg-vault--folder-ops.js', 'sg-vault/sg-vault--sync.js',
                     'sg-vault/sg-vault--history.js', 'sg-vault/sg-vault--branches.js']) vm.runInThisContext(fs.readFileSync(path.join(VENDOR, f), 'utf8'), { filename: f })
    vm.runInThisContext('globalThis.SGSend = SGSend; globalThis.SGVault = SGVault; globalThis.SGVaultCrypto = SGVaultCrypto; globalThis.SGSendCrypto = SGSendCrypto')
    const NV = await imp('assets/newsroom-vault.js'), DOOR = await imp('assets/door.js')
    const sg = NV.client({ endpoint, token })
    const v = await NV.createVault(sg, { name: 'newsroom-review-lane', description: 'The newsroom.sgit.ai review lane: reviews sent by reviewers outside the newsroom, sealed to its key' })
    const key = v.getVaultKey(), i = key.lastIndexOf(':'), passphrase = key.slice(0, i), vaultId = key.slice(i + 1)
    const keys = await DOOR.sgitKeys(passphrase, vaultId)
    const rec = { ...(await I.newInbox({ vault: vaultId, endpoint, device: 'review_lane.mjs' })), vault_key: NV.vaultKeyString(passphrase, vaultId) }
    await I.configure(rec, { writeKey: keys.writeHex, accessToken: token })
    const pub = { what: 'The review lane (card 091): an append lane where reviewers outside the newsroom send review records, sealed to this key. Public: the vault id, the key fingerprint and the public key. The append link (with its token) is given to each reviewer by the editor; the secret is in the environment as REVIEW_LANE_SECRET.',
                  v: 1, vault: vaultId, endpoint, fingerprint: rec.fingerprint, public: rec.public, created: rec.created }
    const secret = Buffer.from(JSON.stringify({ v: 1, vault: vaultId, endpoint, token: rec.token, enum_key: rec.enum_key, public: rec.public, private: rec.private, fingerprint: rec.fingerprint, vault_key: rec.vault_key, created: rec.created })).toString('base64')
    const out = opt('--out') || fs.mkdtempSync(path.join(os.tmpdir(), 'review-lane-'))
    fs.mkdirSync(out, { recursive: true })
    fs.writeFileSync(unsealed ? path.join(out, 'lane.json') : path.join(ROOT, 'admin/content/reviews/lane.json'), JSON.stringify(pub, null, 1) + '\n')
    fs.writeFileSync(path.join(out, 'send-link.txt'), linkUrl(rec) + '\n')
    fs.writeFileSync(path.join(out, 'send-link-qr.svg'), (await I.qrSvg(linkUrl(rec), { label: 'The newsroom review lane: the link to send reviews' })).svg)
    // the secret, sealed to the editor's key in pki.sgit.ai's register, with pki.sgit.ai's own message code
    if (opt('--secret-out')) fs.writeFileSync(opt('--secret-out'), secret + '\n', { mode: 0o600 })      // for a smoke test by whoever ran create; delete it after
    let sealedLink = ''
    const to = opt('--to') || 'sha256:db7f79fdd87e030a'
    if (!unsealed) {
        const M = await import(pathToFileURL(opt('--pki-message') || path.join(ROOT, 'admin/build/pki-message/message.js')).href)
        const reg = await (await fetch('https://pki.sgit.ai/directory/index.json')).json()
        const r = reg.records.find(x => x.fp === to && x.ok)
        if (!r) throw new Error(`${to} is not in pki.sgit.ai's register`)
        const bundle = r.statements.find(s => s.type === 'identity').body.bundle
        const msg = await M.compose({ to: bundle, subject: 'The newsroom review lane: REVIEW_LANE_SECRET', text: `Keep this as REVIEW_LANE_SECRET in the environment of the scheduled review run.\n\n${secret}\n\nThe link reviewers send with: ${linkUrl(rec)}`, expires: new Date(Date.now() + 30 * 864e5).toISOString() })
        sealedLink = (await M.sealMessage(msg, bundle)).url
        fs.writeFileSync(path.join(out, 'secret-for-the-editor.txt'), sealedLink + '\n')
    } else fs.writeFileSync(path.join(out, 'secret.txt'), secret + '\n')
    console.log(`review_lane: made vault ${vaultId} with an append lane; key ${rec.fingerprint}`)
    console.log(`review_lane: ${unsealed ? out + '/lane.json' : 'admin/content/reviews/lane.json'} holds the public half; the link, its QR code${sealedLink ? ' and the sealed secret' : ''} are in ${out}`)
    return { rec, out, secret }
}

// reviewers.json as it is kept by hand: one reviewer to a line
const regsText = regs => `{\n "what": ${JSON.stringify(regs.what)},\n "reviewers": [\n${regs.reviewers.map(r => '  ' + JSON.stringify(r).replace(/","/g, '", "').replace(/":"/g, '": "')).join(',\n')}\n ]\n}\n`

const TAKEN = opt('--taken') || path.join(os.tmpdir(), 'review-lane-taken.json')
function secretRec() {
    const raw = opt('--secret-file') ? fs.readFileSync(opt('--secret-file'), 'utf8').trim() : (process.env.REVIEW_LANE_SECRET || '').trim()
    if (!raw) { console.error(`review_lane: ${cmd} needs REVIEW_LANE_SECRET in the environment`); process.exit(2) }
    let rec
    try { rec = JSON.parse(Buffer.from(raw, 'base64').toString('utf8')) } catch (e) { console.error('review_lane: REVIEW_LANE_SECRET is not the base64 JSON create made'); process.exit(2) }
    if (opt('--endpoint')) rec.endpoint = endpoint
    return rec
}
async function mark(rec, taken) {
    const byLane = new Map(); for (const t of taken) { if (!byLane.has(t.inbox)) byLane.set(t.inbox, []); byLane.get(t.inbox).push(t.file_id) }
    for (const [inbox, ids] of byLane) await I.markProcessed(rec, inbox, ids)
    console.log(`review_lane: ${taken.length} message(s) marked processed`)
}

async function drain() {
    const rec = secretRec()
    const status = JSON.parse(fs.readFileSync(opt('--status') || path.join(ROOT, 'reviews/status.json'), 'utf8'))
    const items = await I.list(rec).then(async entries => {
        const out = []
        const byLane = new Map()
        for (const e of entries) { if (!byLane.has(e.inbox)) byLane.set(e.inbox, []); byLane.get(e.inbox).push(e) }
        for (const [inbox, es] of byLane) {
            const files = await I.fetchFiles(rec, inbox, es.map(e => e.file_id))
            const content = new Map(files.map(f => [f.file_id, f.content]))
            for (const e of es) {
                const it = { inbox, file_id: e.file_id, msg: null, problems: [] }
                try { it.msg = JSON.parse(await I.unseal(I.unb64(rec.private), content.get(e.file_id))); it.problems = R.messageProblems(it.msg, rec.fingerprint) }
                catch (err) { it.problems.push(String(err.message || err)) }
                out.push(it)
            }
        }
        return out
    })
    const regs = JSON.parse(fs.readFileSync(REG, 'utf8'))
    const known = new Set(regs.reviewers.map(r => r.id))
    const taken = [], rejected = [], written = []
    const seen = new Set((status.articles || []).flatMap(a => (a.reviews || []).map(x => `${x.reviewer}|${a.slug}|${x.hash}`)))
    if (fs.existsSync(REVIEWS)) for (const d of fs.readdirSync(REVIEWS)) {          // what is in the repository and not yet built
        if (!fs.statSync(path.join(REVIEWS, d)).isDirectory()) continue
        for (const f of fs.readdirSync(path.join(REVIEWS, d))) if (f.endsWith('.json') && f !== 'status.json') {
            try { const x = JSON.parse(fs.readFileSync(path.join(REVIEWS, d, f), 'utf8')); seen.add(`${x.reviewer}|${x.slug}|${x.article_hash}`) } catch (e) { /* reviews.py --check reports it */ }
        }
    }
    for (const it of items) {
        if (it.problems.length) { rejected.push({ file: it.file_id, why: it.problems }); taken.push(it); continue }
        for (const r of it.msg.records) {
            const a = (status.articles || []).find(x => x.slug === r.slug)
            const p = R.problems(r, status)
            const k = `${r.reviewer}|${r.slug}|${r.article_hash || (a && a.hash)}`
            if (seen.has(k)) p.errors.push('a second review of the same text by the same reviewer (already in the repository or in this drain)')
            if (p.errors.length) { rejected.push({ file: it.file_id, slug: r.slug, reviewer: r.reviewer, why: p.errors }); continue }
            seen.add(k)
            if (!r.article_hash && a) { r.article_hash = a.hash; r.article_version = r.article_version || a.version }
            if (!r.criteria) r.criteria = 'v1.2'
            r.received = { via: 'the review lane', file: it.file_id, sent_at: it.msg.sent_at || '', from: it.msg.from || '' }
            let name = R.fileName(r), n = 1
            const dir = path.join(REVIEWS, r.slug)
            while (fs.existsSync(path.join(dir, name))) name = R.fileName(r).replace(/\.json$/, `__${++n}.json`)
            written.push({ path: path.relative(ROOT, path.join(dir, name)), r, warnings: p.warnings })
            if (!has('--dry')) { fs.mkdirSync(dir, { recursive: true }); fs.writeFileSync(path.join(dir, name), JSON.stringify(r, null, 1) + '\n') }
            if (!known.has(r.reviewer)) {
                known.add(r.reviewer)
                regs.reviewers.push({ id: r.reviewer, name: r.reviewer, kind: r.kind, about: `Registered by the review lane with its first review (${String(r.at).slice(0, 10)}); its record names the model.` })
                if (!has('--dry')) fs.writeFileSync(REG, regsText(regs))
            }
        }
        taken.push(it)
    }
    // what arrived, for the editor
    console.log(`review_lane: ${items.length} message(s) in the lane; ${written.length} record(s) ${has('--dry') ? 'would be written' : 'written'}, ${rejected.length} rejected`)
    for (const w of written) {
        const f = w.r.findings || []
        const sev = s => f.filter(x => x.severity === s).length
        console.log(`\n## ${w.r.slug}: ${w.r.reviewer}, ${w.r.verdict} (${f.length} finding(s): ${sev('high')} high, ${sev('medium')} medium, ${sev('low')} low)\n   ${w.path}\n   ${w.r.summary}`)
        for (const x of f) console.log(`   - [${x.severity}] ${x.criterion}${x.verification ? '/' + x.verification : ''} ${x.section ? '#' + x.section : ''}: ${x.issue}`)
        for (const m of w.warnings) console.log(`   ! ${m}`)
    }
    for (const x of rejected) console.log(`\nREJECTED ${x.file}${x.slug ? ` (${x.reviewer} on ${x.slug})` : ''}: ${x.why.join('; ')}`)
    if (written.length && !has('--dry') && INTO === ROOT) {
        try { execFileSync('python3', [path.join(ROOT, 'admin/build/reviews.py'), '--check'], { stdio: 'inherit' }) } catch (e) { console.log('review_lane: reviews.py --check found problems; fix or remove the records above before committing') }
    }
    const ids = taken.map(t => ({ inbox: t.inbox, file_id: t.file_id }))
    if (!has('--dry')) fs.writeFileSync(TAKEN, JSON.stringify(ids) + '\n')
    if (has('--mark') && taken.length) await mark(rec, ids)
    else if (taken.length && !has('--dry')) console.log(`review_lane: once the records are committed and pushed: node admin/build/review_lane.mjs mark --taken ${TAKEN}`)
    return { items, written, rejected }
}

if (cmd === 'create') await create()
else if (cmd === 'drain') await drain()
else if (cmd === 'mark') { const ids = fs.existsSync(TAKEN) ? JSON.parse(fs.readFileSync(TAKEN, 'utf8')) : []; if (ids.length) await mark(secretRec(), ids); else console.log('review_lane: nothing to mark') }
else { console.error('usage: review_lane.mjs create | drain [--taken <file>] [--mark] [--dry] | mark [--taken <file>]   (see the top of this file)'); process.exitCode = 2 }
