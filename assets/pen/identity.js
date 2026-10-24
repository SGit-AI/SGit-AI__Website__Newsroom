/**
 * identity.js: who is holding the pen. A key for this browser, vouched for in pki.sgit.ai's register, that signs the
 * notes its owner sends to the newsroom (card 090).
 *
 * The register at pki.sgit.ai already has the pattern: an agent's key is OPERATED by a person when the person's record
 * links to it with method "operates" and an end date, and the agent's record links back with "operated-by". A browser
 * here does the same. It makes its own key pair (pki.sgit.ai's code, vendored unedited in assets/vendor/pki/), signs
 * two statements, its identity (kind "agent", runtime "browser, newsroom.sgit.ai") and a link to its owner's key
 * ("operated-by"), and hands them over as a submission, the register's own format. Once the register holds them and
 * the owner has signed "operates" back on pki.sgit.ai, a note this browser signs is checked by anyone, in any browser,
 * against the public register:
 *
 *   signed note   { signer, at, sig } on the note; sig is ECDSA P-256 over the canonical JSON (keys.js canon, the
 *                 register's own) of { v, kind: "newsroom.sgit.ai/note/v1", id, at, note_kind, path, n, quote, text, signer }
 *   trusted       the register read and checked in the browser (readRecord, graph), then trustFrom(signer) from a
 *                 PINNED root, Dinis Cruz's master key, never from whatever the register's anchors file says
 *
 * The private halves are kept in this browser's storage, as pki.sgit.ai's own browser account keeps its keys before a
 * vault holds them. The key is worth what its "operates" link says, and that link has an end date: losing a browser
 * means letting the link lapse, or withdrawing it on pki.sgit.ai, not rotating anything here.
 *
 * Nothing here talks to a server except the GET of the register (public, served with CORS by pki.sgit.ai).
 *
 * @module identity
 */
import * as K from '../vendor/pki/v0.2.25/keys.js'
import * as D from '../vendor/pki/v0.2.25/directory.js'

export const REGISTER = 'https://pki.sgit.ai/directory/index.json'
export const ROOT = 'sha256:db7f79fdd87e030a'              // Dinis Cruz's master key: the register's anchor, pinned here
export const NOTE_KIND = 'newsroom.sgit.ai/note/v1'
const STORE = 'sgit.pen.identity.v1', CACHE = 'sgit.pen.register.v1', CACHE_MS = 10 * 60 * 1000
const today = () => new Date().toISOString().slice(0, 10)
const ls = {
    get(k) { try { return JSON.parse(localStorage.getItem(k) || 'null') } catch (e) { return null } },
    set(k, v) { try { if (v == null) localStorage.removeItem(k); else localStorage.setItem(k, JSON.stringify(v)) } catch (e) { /* private window */ } },
}

// ------------------------------------------------------------ this browser's key
/** The identity this browser holds, or null: { bundle, private: { encrypt, sign } (bytes), name, operator, statements, created }. */
export function load() {
    const s = ls.get(STORE)
    if (!s || !s.bundle) return null
    return { ...s, private: { encrypt: K.unb64(s.private.encrypt), sign: K.unb64(s.private.sign) } }
}
export const fingerprintOf = id => id && id.bundle.signing_fingerprint

/**
 * Make this browser's key and its two statements. name is who holds it ("Dinis Cruz"); device says which browser;
 * operator is the key that will vouch for it (by default the pinned root). RSA-4096 takes a few seconds.
 */
export async function make({ name, device = '', operator = ROOT }) {
    if (!K.FP.test(operator)) throw new Error('the operator is not a fingerprint (sha256: and 16 hex)')
    const label = `${String(name).trim()}, newsroom.sgit.ai${device ? ', ' + device : ''}`
    const id = await K.generate(label)
    const statements = [
        await D.agentStatement(id, { name: label, about: 'A browser key: it signs the notes its owner sends to newsroom.sgit.ai from the Pen.', runtime: 'browser, newsroom.sgit.ai', session: false }),
        await D.linkStatement(id, { to: operator, method: 'operated-by', on: today() }),
    ]
    const saved = { bundle: id.bundle, private: { encrypt: K.b64(id.private.encrypt), sign: K.b64(id.private.sign) }, name: String(name).trim(), device, operator, statements, created: new Date().toISOString() }
    ls.set(STORE, saved)
    return load()
}
export function forget() { ls.set(STORE, null) }

/** The submission pki.sgit.ai takes for its register (people.mjs add checks every signature before a reviewed commit). */
export const submission = id => D.submission(id.statements)

/** A key link: pki.sgit.ai's k1 form, a public key anyone can seal to and compare (message.js keyCode). Not secret. */
export function keyLink(id) {
    const der = p => K.unpem(p).der
    return `https://pki.sgit.ai/send/#k1.${K.b64url(der(id.bundle.encrypt))}.${K.b64url(der(id.bundle.sign))}.${K.b64url(K.utf8(id.bundle.label || ''))}`
}

// ------------------------------------------------------------ signing a note
/** The bytes a note's signature covers: the register's canonical JSON of what the note says, and who says it. */
export function payloadOf(note, signer) {
    return { v: 1, kind: NOTE_KIND, id: note.id, at: note.at, note_kind: note.kind || 'note', path: note.path || '', n: note.n == null ? null : note.n,
             quote: note.quote || '', text: note.text || '', signer }
}
const bytesOf = p => K.utf8(K.canon(p) + '\n')

/** Sign a note with this browser's key: returns { signer, at, sig } to keep on the note, or null with no key. */
export async function sign(note, id = load()) {
    if (!id) return null
    const signer = fingerprintOf(id)
    return { signer, at: new Date().toISOString(), sig: K.b64(await K.signBytes(id.private.sign, bytesOf(payloadOf(note, signer)))) }
}

/** Check a signed note against a bundle's signing key (from the register, or this browser's own). */
export async function verify(note, bundle) {
    const s = note && note.signed
    if (!s || !bundle || s.signer !== bundle.signing_fingerprint) return false
    let raw; try { raw = K.unb64(s.sig) } catch (e) { return false }
    return K.verifyBytes(bundle.sign, raw, bytesOf(payloadOf(note, s.signer)))
}

// ------------------------------------------------------------ the register
/** The register, read and every record checked in this browser; cached for ten minutes in this tab's session. */
export async function register({ fresh = false } = {}) {
    let doc = null
    try { const c = JSON.parse(sessionStorage.getItem(CACHE) || 'null'); if (!fresh && c && Date.now() - c.t < CACHE_MS) doc = c.doc } catch (e) { /* fine */ }
    if (!doc) {
        const r = await fetch(REGISTER, { cache: 'no-store' })
        if (!r.ok) throw new Error(`the register answered ${r.status}`)
        doc = await r.json()
        try { sessionStorage.setItem(CACHE, JSON.stringify({ t: Date.now(), doc })) } catch (e) { /* too big, or private */ }
    }
    const records = await Promise.all((doc.records || []).map(r => D.readRecord(r.statements, { dir: r.fp, fixture: r.fixture })))
    return { doc, records, g: D.graph(records, { anchors: [ROOT] }) }
}

/**
 * What the register says about a signer, judged from the pinned root: { ok, level, text, name, until?, bundle? }.
 * ok means the signer is the root itself, verified by it, a persona of it, or a key it operates in date.
 */
export async function standing(fp, reg = null) {
    reg = reg || await register()
    const rec = reg.g.people.get(fp)
    const s = D.standing(reg.g, fp)
    const t = D.trustFrom(reg.g, fp, ROOT)
    return { ok: !!t.ok, level: s.level, text: t.ok ? t.why : s.text, name: rec ? rec.name : '', until: t.until || s.until || '', bundle: rec ? rec.bundle : null,
             chain: (t.chain || []).map(x => D.nameOf(reg.g, x)) }
}

/** A note's signature, checked end to end: the signature against the signer's key in the register, and the signer's standing. */
export async function check(note, reg = null) {
    if (!note || !note.signed) return { signed: false }
    reg = reg || await register()
    const st = await standing(note.signed.signer, reg)
    const good = st.bundle ? await verify(note, st.bundle) : false
    return { signed: true, valid: good, ...st }
}
