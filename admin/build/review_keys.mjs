#!/usr/bin/env node
/* review_keys.mjs: keys for the review desk and the security agent, and sealing a secret to the editor (card 092).
 *
 *   node admin/build/review_keys.mjs make <role> --out <dir>       role: newsroom-desk | newsroom-security
 *       a key pair for the role, with pki.sgit.ai's own code (assets/vendor/pki/v0.2.25): the PUBLIC bundle to
 *       admin/content/reviews/keys/<role>.json; to --out, the register submission (the key's agent identity and an
 *       "operated-by" link to the editor's root key, for the editor to file on pki.sgit.ai and answer with
 *       "operates") and the private half sealed to the editor's key as a pki.sgit.ai message link. The private half
 *       is printed nowhere; the editor keeps it in the environment as NEWSROOM_DESK_KEY or NEWSROOM_SECURITY_KEY.
 *       --keys <dir> writes the bundle elsewhere and --unsealed seals nothing (the test).
 *       --secret-out <file> also writes it unsealed (mode 600), for a smoke test by whoever ran it; delete it after.
 *
 *   node admin/build/review_keys.mjs seal --subject <s> --out <file> < secret
 *       seal what is on stdin to the editor's key (--to; Dinis Cruz's root by default) as a pki.sgit.ai message link,
 *       and its QR code beside it (<file without .txt>.svg) when it fits one code (message.js MAX_QR_CHARS).
 *
 * The private half is base64 of { v, role, signing_fingerprint, fingerprint, sign, encrypt } (PKCS#8, base64), the
 * shape admin/build/review_vault.py signs with.
 */
import fs from 'fs'
import path from 'path'
import { pathToFileURL } from 'url'

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..')
const imp = p => import(pathToFileURL(path.join(ROOT, p)).href)
const K = await imp('assets/vendor/pki/v0.2.25/keys.js')
const D = await imp('assets/vendor/pki/v0.2.25/directory.js')
const M = await imp('admin/build/pki-message/message.js')
const args = process.argv.slice(2), opt = n => { const i = args.indexOf(n); return i >= 0 ? args[i + 1] : null }
const EDITOR = opt('--to') || 'sha256:db7f79fdd87e030a'
const ROLES = {
    'newsroom-desk': { name: '@newsroom.desk, the review desk of newsroom.sgit.ai', about: 'Signs what the newsroom writes into its reviewers\' vaults (the brief, the queue, the answers), so a reviewer follows only what the newsroom signed.', env: 'NEWSROOM_DESK_KEY' },
    'newsroom-security': { name: '@newsroom.security, the security agent of newsroom.sgit.ai', about: 'Signs its verdict on everything in the reviewers\' vaults before the review desk may take any of it.', env: 'NEWSROOM_SECURITY_KEY' },
}

async function editorBundle() {
    const reg = await (await fetch(process.env.NEWSROOM_PKI_REGISTER || 'https://pki.sgit.ai/directory/index.json')).json()
    const r = reg.records.find(x => x.fp === EDITOR && x.ok)
    if (!r) throw new Error(`${EDITOR} is not in pki.sgit.ai's register`)
    return r.statements.find(s => s.type === 'identity').body.bundle
}
export async function sealToEditor(text, subject, toBundle = null) {
    const bundle = toBundle || await editorBundle()
    const msg = await M.compose({ to: bundle, subject, text, expires: new Date(Date.now() + 30 * 864e5).toISOString() })
    return (await M.sealMessage(msg, bundle)).url
}
/** The sealed link, and its QR code beside it (<file>.svg): one code, scanned by a phone that holds the editor's key. */
export async function writeSealed(file, url) {
    fs.writeFileSync(file, url + '\n')
    if (url.length > M.MAX_QR_CHARS + 40) { console.log(`review_keys: ${path.basename(file)} is ${url.length} characters, too long for one QR code`); return }
    const I = await imp('assets/vault-pane/inbox.js')
    fs.writeFileSync(file.replace(/\.txt$/, '') + '.svg', (await I.qrSvg(url, { cell: 4, label: 'A secret sealed to the editor\'s key on pki.sgit.ai' })).svg)
}

const cmd = args[0]
if (cmd === 'make') {
    const role = args[1], R = ROLES[role]
    if (!R) { console.error(`review_keys: role is one of ${Object.keys(ROLES).join(', ')}`); process.exit(2) }
    const out = opt('--out'); if (!out) { console.error('review_keys: --out <dir> (outside the repository)'); process.exit(2) }
    fs.mkdirSync(out, { recursive: true })
    const id = await K.generate(R.name)
    const today = new Date().toISOString().slice(0, 10)
    const statements = [
        await D.agentStatement(id, { name: R.name, about: R.about, runtime: 'scheduled Claude Code sessions on the SGit-AI__Website__Newsroom repository', session: false }),
        await D.linkStatement(id, { to: EDITOR, method: 'operated-by', on: today }),
    ]
    const pub = path.join(opt('--keys') ? path.resolve(opt('--keys')) : path.join(ROOT, 'admin/content/reviews/keys'), `${role}.json`)
    fs.mkdirSync(path.dirname(pub), { recursive: true })
    fs.writeFileSync(pub, JSON.stringify(id.bundle, null, 1) + '\n')
    fs.writeFileSync(path.join(out, `${role}__submission.json`), JSON.stringify(D.submission(statements), null, 1) + '\n')
    // only the signing half: the role signs and never decrypts, and so the sealed secret fits one QR code
    const secret = Buffer.from(JSON.stringify({ v: 1, role, signing_fingerprint: id.bundle.signing_fingerprint, sign: K.b64(id.private.sign) })).toString('base64')
    if (opt('--secret-out')) fs.writeFileSync(opt('--secret-out'), secret + '\n', { mode: 0o600 })
    if (!args.includes('--unsealed')) {
        const link = await sealToEditor(`${R.env}=${secret}`, `${R.env}, ${role} ${id.bundle.signing_fingerprint}`)
        await writeSealed(path.join(out, `${role}__for-the-editor.txt`), link)
    }
    console.log(`review_keys: ${role} is ${id.bundle.signing_fingerprint}; public bundle ${pub}; the submission and the sealed private half are in ${out}`)
} else if (cmd === 'seal') {
    const text = fs.readFileSync(0, 'utf8').trim()
    if (!text || !opt('--out')) { console.error('review_keys: seal --subject <s> --out <file> < secret'); process.exit(2) }
    await writeSealed(opt('--out'), await sealToEditor(text, opt('--subject') || 'a secret from the newsroom'))
    console.log(`review_keys: sealed to ${EDITOR}, in ${opt('--out')}`)
} else { console.error('usage: review_keys.mjs make <role> --out <dir> | seal --subject <s> --out <file> < secret'); process.exitCode = 2 }
