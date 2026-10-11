/**
 * lab.js: the passkey lab. Proofs of concept for "The passkey opens the vault"
 * (articles/the-passkey-opens-the-vault.html), each one a card with a button and what came back.
 *
 *   0. what this browser can do           PublicKeyCredential, getClientCapabilities(), the platform authenticator
 *   1. make a passkey for this site       navigator.credentials.create() with rp.id = this host, a resident key,
 *                                         user verification, and the prf extension; shows prf.enabled and whether
 *                                         the passkey is synced (the BE and BS flags)
 *   2. touch it: the PRF bytes            navigator.credentials.get() with the fixed input; the 32 bytes that are
 *                                         the same on every device the passkey syncs to
 *   3. from the bytes, the door           HKDF to a seed, a passphrase and a vault id, exactly as the article's
 *                                         derivation says; then sgit's own derivation of the read and write keys
 *                                         (PBKDF2-HMAC-SHA256, 600,000 iterations each), timed
 *   4. a recovery code, the second door   26 characters of base32 in place of the PRF bytes
 *   5. test vectors                       the same derivation from a fixed input, compared with what sgit's own
 *                                         code produced in Python (vectors.json)
 *   6. the door on the vault server       with an access key the reader pastes (kept in memory only): check the
 *                                         derived address, create the door by writing its one encrypted file,
 *                                         open it again from the server, delete the file
 *
 * Nothing here touches the reading account. No key is stored anywhere: the access key lives in a variable until
 * the page is closed, and the derived keys are shown only behind a reveal. The page loads no third-party code;
 * every call to the vault server is listed as it happens.
 *
 * The derivation, written out (the article's steps 1 to 6, made exact):
 *   prf input        = SHA-256("newsroom.sgit.ai/door/v1")                      a public constant
 *   door seed        = HKDF-SHA256(ikm = prf bytes, salt = SHA-256("newsroom.sgit.ai"), info = "sgit/door/v1", 32 bytes)
 *   passphrase       = hex( HKDF-SHA256(ikm = seed, salt = empty, info = "sgit/door/v1/passphrase", 32 bytes) )
 *   vault id         = 8 characters of [a-z0-9] drawn from HKDF-SHA256(ikm = seed, salt = empty, info = "sgit/door/v1/id", 64 bytes),
 *                      a byte accepted only when it is below 252 (= 7 × 36), so no character is favoured
 *   vault key        = sgit_private_vault_ + passphrase + ":" + vault id              (sgit's format)
 *   read key         = PBKDF2-HMAC-SHA256(passphrase, "sg-vault-v1:" + vault id, 600000, 32 bytes)        (sgit)
 *   write key        = PBKDF2-HMAC-SHA256(passphrase, "sg-vault-v1:write:" + vault id, 600000, 32 bytes)  (sgit)
 *   recovery door    = the same, with the 16 bytes of the recovery code as the ikm
 *
 * @module passkey-lab
 */

const RP_FOR_DERIVATION = 'newsroom.sgit.ai'        // the constants are the site's, whichever host runs the page
const ALPHABET = 'abcdefghijklmnopqrstuvwxyz0123456789'
const B32 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567'
const te = new TextEncoder(), td = new TextDecoder()
const hex = b => [...new Uint8Array(b)].map(x => x.toString(16).padStart(2, '0')).join('')
const unhex = s => Uint8Array.from(s.match(/../g) || [], h => parseInt(h, 16))
const b64url = b => btoa(String.fromCharCode(...new Uint8Array(b))).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '')
const sha256 = async data => new Uint8Array(await crypto.subtle.digest('SHA-256', typeof data === 'string' ? te.encode(data) : data))
const concat = (...parts) => { const n = parts.reduce((s, p) => s + p.length, 0), out = new Uint8Array(n); let i = 0; for (const p of parts) { out.set(p, i); i += p.length } return out }

// ------------------------------------------------------------ the crypto, all WebCrypto
export async function hkdf(ikm, salt, info, length) {
    const key = await crypto.subtle.importKey('raw', ikm, 'HKDF', false, ['deriveBits'])
    return new Uint8Array(await crypto.subtle.deriveBits({ name: 'HKDF', hash: 'SHA-256', salt, info: te.encode(info) }, key, length * 8))
}
export async function pbkdf2(passphrase, salt, iterations = 600000) {
    const key = await crypto.subtle.importKey('raw', te.encode(passphrase), 'PBKDF2', false, ['deriveBits'])
    return new Uint8Array(await crypto.subtle.deriveBits({ name: 'PBKDF2', hash: 'SHA-256', salt: te.encode(salt), iterations }, key, 256))
}
export async function hmac(keyBytes, text) {
    const key = await crypto.subtle.importKey('raw', keyBytes, { name: 'HMAC', hash: 'SHA-256' }, false, ['sign'])
    return new Uint8Array(await crypto.subtle.sign('HMAC', key, te.encode(text)))
}
/** sgit's AES-256-GCM: iv (12 bytes) || ciphertext || tag. A given iv makes it deterministic, as sgit's encrypt_deterministic does. */
export async function aesEncrypt(keyBytes, plaintext, iv) {
    const key = await crypto.subtle.importKey('raw', keyBytes, 'AES-GCM', false, ['encrypt'])
    iv = iv || crypto.getRandomValues(new Uint8Array(12))
    const ct = new Uint8Array(await crypto.subtle.encrypt({ name: 'AES-GCM', iv, tagLength: 128 }, key, plaintext))
    return concat(iv, ct)
}
export async function aesDecrypt(keyBytes, data) {
    const key = await crypto.subtle.importKey('raw', keyBytes, 'AES-GCM', false, ['decrypt'])
    return new Uint8Array(await crypto.subtle.decrypt({ name: 'AES-GCM', iv: data.slice(0, 12), tagLength: 128 }, key, data.slice(12)))
}

/** The vault id: 8 characters of [a-z0-9] from an HKDF stream, with rejection sampling and a counter in the info if the stream runs short. */
export async function vaultIdFrom(seed, counter = 0) {
    let out = ''
    for (let round = 0; out.length < 8 && round < 8; round++) {
        const info = 'sgit/door/v1/id' + (counter ? `/${counter}` : '') + (round ? `/${round}` : '')
        for (const b of await hkdf(seed, new Uint8Array(0), info, 64)) {
            if (b < 252) out += ALPHABET[b % 36]
            if (out.length === 8) break
        }
    }
    return out
}

/** The article's derivation: from 32 PRF bytes (or the 16 bytes of a recovery code) to a door's passphrase and vault id. */
export async function doorFrom(ikm, counter = 0) {
    const seed = await hkdf(ikm, await sha256(RP_FOR_DERIVATION), 'sgit/door/v1', 32)
    const passphrase = hex(await hkdf(seed, new Uint8Array(0), 'sgit/door/v1/passphrase', 32))
    const vaultId = await vaultIdFrom(seed, counter)
    return { seed: hex(seed), passphrase, vaultId }
}

/** sgit's derivation from a passphrase and a vault id: read key, write key, and the ids of the ref and the branch index. */
export async function sgitKeys(passphrase, vaultId) {
    const t0 = performance.now()
    const read = await pbkdf2(passphrase, `sg-vault-v1:${vaultId}`)
    const t1 = performance.now()
    const write = await pbkdf2(passphrase, `sg-vault-v1:write:${vaultId}`)
    const t2 = performance.now()
    const ref = hex(await hmac(read, `sg-vault-v1:file-id:ref:${vaultId}`)).slice(0, 12)
    const idx = hex(await hmac(read, `sg-vault-v1:file-id:branch-index:${vaultId}`)).slice(0, 12)
    return { read, write, readHex: hex(read), writeHex: hex(write), refId: 'ref-pid-muw-' + ref, indexId: 'idx-pid-muw-' + idx,
             msRead: Math.round(t1 - t0), msWrite: Math.round(t2 - t1) }
}
export const vaultKeyString = (passphrase, vaultId) => 'sgit_private_' + 'vault_' + passphrase + ':' + vaultId
export const readKeyString = (readHex, vaultId) => 'sgit_public_' + 'read_' + readHex + ':' + vaultId
export const PRF_INPUT_TEXT = `${RP_FOR_DERIVATION}/door/v1`

/** A recovery code: 128 bits as 26 characters of base32, shown in groups of 4 to be written down. */
export function recoveryCode(bytes) {
    bytes = bytes || crypto.getRandomValues(new Uint8Array(16))
    let bits = '', out = ''
    for (const b of bytes) bits += b.toString(2).padStart(8, '0')
    for (let i = 0; i < 26; i++) out += B32[parseInt(bits.slice(i * 5, i * 5 + 5).padEnd(5, '0'), 2)]
    return { bytes, code: out, shown: out.match(/.{1,4}/g).join('-') }
}
export function recoveryBytes(code) {
    const s = String(code || '').toUpperCase().replace(/[^A-Z2-7]/g, '')
    if (s.length !== 26) return null
    let bits = ''
    for (const ch of s) bits += B32.indexOf(ch).toString(2).padStart(5, '0')
    const out = new Uint8Array(16)
    for (let i = 0; i < 16; i++) out[i] = parseInt(bits.slice(i * 8, i * 8 + 8), 2)
    return out
}

/** sgit's generate_vault_key(): 24 characters and 8 characters of [a-z0-9], random. The master vault's key is made this way. */
export function randomVaultKey() {
    const pick = n => { const r = crypto.getRandomValues(new Uint8Array(n * 2)); let s = ''; for (const b of r) { if (b < 252 && s.length < n) s += ALPHABET[b % 36] } return s.length === n ? s : pick(n) }
    return { passphrase: pick(24), vaultId: pick(8) }
}

/** The authenticator data flags byte: UP, UV, BE (backup eligible: the passkey can sync), BS (backed up: it has). */
export function flagsOf(authData) {
    const f = new Uint8Array(authData)[32]
    return { up: !!(f & 1), uv: !!(f & 4), be: !!(f & 8), bs: !!(f & 16) }
}

// ------------------------------------------------------------ the page
function h(tag, attrs, ...kids) {
    const el = document.createElement(tag)
    for (const [k, v] of Object.entries(attrs || {})) {
        if (v === false || v == null) continue
        if (k.startsWith('on')) el.addEventListener(k.slice(2), v)
        else el.setAttribute(k, v === true ? '' : v)
    }
    for (const kid of kids.flat()) if (kid != null && kid !== false) el.append(kid instanceof Node ? kid : String(kid))
    return el
}
const row = (k, v, cls) => h('div', { class: 'kv' }, h('span', { class: 'k' }, k), h('span', { class: `v ${cls || ''}` }, v))
const secret = (text, label) => {
    const span = h('span', { class: 'mono' }, '•'.repeat(Math.min(24, text.length)) + ` (${text.length} characters)`)
    let shown = false
    const btn = h('button', { type: 'button', class: 'btn sm', onclick: () => { shown = !shown; span.textContent = shown ? text : '•'.repeat(Math.min(24, text.length)) + ` (${text.length} characters)`; btn.textContent = shown ? 'Hide' : `Reveal ${label || ''}`.trim() } }, `Reveal ${label || ''}`.trim())
    const copy = h('button', { type: 'button', class: 'btn sm', onclick: async () => { try { await navigator.clipboard.writeText(text); copy.textContent = 'Copied' } catch (e) { copy.textContent = 'Could not copy' } setTimeout(() => { copy.textContent = 'Copy' }, 1500) } }, 'Copy')
    return h('span', { class: 'secret' }, span, ' ', btn, ' ', copy)
}
const err = e => (e && e.name ? `${e.name}: ` : '') + String(e && e.message || e)

export async function lab(opts) {
    const $ = id => document.getElementById(id)
    const S = { cred: null, prf: null, door: null, keys: null, recovery: null, access: '', log: [] }
    const stored = (() => { try { return JSON.parse(localStorage.getItem('sgit.passkey.lab') || 'null') } catch (e) { return null } })()
    const remember = v => { try { localStorage.setItem('sgit.passkey.lab', JSON.stringify(v)) } catch (e) { /* fine */ } }

    // 0 ---------------------------------------------------------------- capabilities
    const out0 = $('poc0-out')
    const can = !!window.PublicKeyCredential
    const caps = can && PublicKeyCredential.getClientCapabilities ? await PublicKeyCredential.getClientCapabilities().catch(() => null) : null
    const uvpaa = can && PublicKeyCredential.isUserVerifyingPlatformAuthenticatorAvailable ? await PublicKeyCredential.isUserVerifyingPlatformAuthenticatorAvailable().catch(() => null) : null
    out0.replaceChildren(
        row('Secure context', window.isSecureContext ? 'yes' : 'no: WebAuthn needs https, or localhost', window.isSecureContext ? 'ok' : 'bad'),
        row('WebAuthn (PublicKeyCredential)', can ? 'present' : 'missing', can ? 'ok' : 'bad'),
        row('Relying party id this page uses', location.hostname),
        row('A platform authenticator that verifies the user (Touch ID, Face ID, Windows Hello, a screen lock)', uvpaa == null ? 'unknown' : uvpaa ? 'available' : 'not available', uvpaa ? 'ok' : ''),
        row('getClientCapabilities()', caps ? Object.entries(caps).map(([k, v]) => `${k}: ${v}`).join(' · ') : 'not implemented in this browser (Chrome 133+, Safari 17.4+)'),
        row('PRF, as the browser reports it', caps && typeof caps['extension:prf'] === 'boolean' ? String(caps['extension:prf']) : 'the browser does not say (some report null here); the passkey will, when it is made (prf.enabled)'),
        stored ? row('A passkey from this lab, in this browser', `made ${stored.made.slice(0, 16).replace('T', ' ')}, credential ${stored.id.slice(0, 12)}…, PRF ${stored.prf ? 'on' : 'off'}`) : null,
    )

    // 1 ---------------------------------------------------------------- create
    const out1 = $('poc1-out'), ladder = $('poc1-ladder')
    $('poc1-go').addEventListener('click', async () => {
        out1.replaceChildren(h('p', { class: 'dim' }, 'Waiting for the browser’s passkey prompt…')); ladder.hidden = true
        try {
            const prfInput = await sha256(PRF_INPUT_TEXT)
            const userId = crypto.getRandomValues(new Uint8Array(16))
            const cred = await navigator.credentials.create({ publicKey: {
                challenge: crypto.getRandomValues(new Uint8Array(32)),
                rp: { id: location.hostname, name: 'SGit Newsroom (passkey lab)' },
                user: { id: userId, name: 'reader', displayName: 'A reader of the SGit Newsroom' },
                pubKeyCredParams: [{ type: 'public-key', alg: -7 }, { type: 'public-key', alg: -257 }],
                authenticatorSelection: { residentKey: 'required', requireResidentKey: true, userVerification: 'required' },
                extensions: { prf: { eval: { first: prfInput } }, credProps: true },
                timeout: 120000,
            } })
            const ext = cred.getClientExtensionResults()
            const authData = cred.response.getAuthenticatorData ? cred.response.getAuthenticatorData() : null
            const flags = authData ? flagsOf(authData) : null
            const transports = cred.response.getTransports ? cred.response.getTransports() : []
            S.cred = { id: cred.id, rawId: cred.rawId, userId, prf: !!(ext.prf && ext.prf.enabled), flags, transports, attachment: cred.authenticatorAttachment }
            remember({ id: cred.id, userId: hex(userId), made: new Date().toISOString(), prf: S.cred.prf })
            out1.replaceChildren(
                row('Credential id', h('span', { class: 'mono' }, cred.id)),
                row('User handle (random, made by this page; it syncs with the passkey)', h('span', { class: 'mono' }, hex(userId))),
                row('Authenticator', `${cred.authenticatorAttachment || 'unknown attachment'}${transports.length ? ` · transports: ${transports.join(', ')}` : ''}`),
                row('Resident (discoverable) credential', ext.credProps && 'rk' in ext.credProps ? String(ext.credProps.rk) : 'required; the browser did not report it'),
                flags ? row('Synced?', `backup eligible ${flags.be ? 'yes' : 'no'} · backed up ${flags.bs ? 'yes' : 'no'}: ${flags.be ? 'this passkey can travel to other devices through its provider' : 'this passkey is bound to this device'}`, flags.be ? 'ok' : 'warn') : null,
                row('prf.enabled', String(S.cred.prf), S.cred.prf ? 'ok' : 'bad'),
                h('p', { class: 'dim' }, S.cred.prf ? 'The authenticator can produce the PRF bytes. Go to 2.' : 'No PRF bytes from this authenticator, so no door can be derived from it. The ladder below is what the page would offer.'),
            )
            ladder.hidden = S.cred.prf
        } catch (e) { out1.replaceChildren(h('p', { class: 'warn' }, err(e))) }
    })

    // 2 ---------------------------------------------------------------- get PRF
    const out2 = $('poc2-out')
    const prfText = $('poc2-input'); prfText.value = PRF_INPUT_TEXT
    $('poc2-go').addEventListener('click', async () => {
        out2.replaceChildren(h('p', { class: 'dim' }, 'Waiting for the gesture…'))
        try {
            const inputText = prfText.value.trim() || PRF_INPUT_TEXT
            const prfInput = await sha256(inputText)
            const a = await navigator.credentials.get({ publicKey: {
                challenge: crypto.getRandomValues(new Uint8Array(32)), rpId: location.hostname, userVerification: 'required',
                allowCredentials: [], extensions: { prf: { eval: { first: prfInput } } }, timeout: 120000,
            } })
            const ext = a.getClientExtensionResults()
            const flags = flagsOf(a.response.authenticatorData)
            if (!ext.prf || !ext.prf.results || !ext.prf.results.first) throw new Error('The authenticator signed, and returned no PRF bytes (prf.results.first is empty). This is the “Chrome’s own store” case in the article.')
            const bytes = new Uint8Array(ext.prf.results.first)
            S.prf = { bytes, inputText, credId: a.id, userHandle: a.response.userHandle ? hex(a.response.userHandle) : '' }
            const fp = hex(bytes).slice(0, 8)
            out2.replaceChildren(
                row('PRF input (SHA-256 of the text; public)', h('span', { class: 'mono' }, hex(prfInput))),
                row('The 32 PRF bytes', secret(hex(bytes), 'the bytes')),
                row('Their fingerprint, to compare between devices', h('b', { class: 'mono big' }, fp)),
                row('Credential used', h('span', { class: 'mono' }, a.id)),
                row('User handle', h('span', { class: 'mono' }, S.prf.userHandle || 'none returned')),
                row('Flags', `user present ${flags.up} · verified ${flags.uv} · backup eligible ${flags.be} · backed up ${flags.bs}`),
                h('p', { class: 'dim' }, 'Open this page on another device where the same passkey is available (the same Google or Apple account, or the same hardware key), press the same button, and the fingerprint, the credential id and the user handle are the same. Different input text gives different bytes from the same passkey.'),
            )
            $('poc2-compare').hidden = false
            $('poc2-mine').textContent = fp
            await derive()
        } catch (e) { out2.replaceChildren(h('p', { class: 'warn' }, err(e))) }
    })
    $('poc2-cmp-go').addEventListener('click', () => {
        const other = $('poc2-other').value.trim().toLowerCase(), mine = $('poc2-mine').textContent
        $('poc2-cmp-out').textContent = !other ? '' : other === mine ? 'The same: the two devices derived the same door.' : 'Different: either another passkey, another input, or a provider that does not sync this one.'
    })

    // 3 ---------------------------------------------------------------- derive
    const out3 = $('poc3-out')
    async function derive(ikm, label) {
        ikm = ikm || (S.prf && S.prf.bytes)
        if (!ikm) { out3.replaceChildren(h('p', { class: 'dim' }, 'No PRF bytes yet: do 2 first, or use the test vector in 5.')); return }
        out3.replaceChildren(h('p', { class: 'dim' }, 'Deriving: HKDF three times, then PBKDF2 twice at 600,000 iterations…'))
        const door = await doorFrom(ikm)
        const keys = await sgitKeys(door.passphrase, door.vaultId)
        S.door = door; S.keys = keys; S.doorFrom = label || 'the passkey'
        out3.replaceChildren(
            row('From', S.doorFrom),
            row('Door seed (HKDF of the bytes, salted with the site’s name)', secret(door.seed, 'the seed')),
            row('Door passphrase (64 hex characters)', secret(door.passphrase, 'the passphrase')),
            row('Door vault id (8 of a–z 0–9, rejection-sampled)', h('b', { class: 'mono big' }, door.vaultId)),
            row('The sgit vault key', secret(vaultKeyString(door.passphrase, door.vaultId), 'the key')),
            row('Read key (PBKDF2, 600,000 iterations)', h('span', {}, secret(keys.readHex, 'the read key'), ` ${keys.msRead} ms`)),
            row('Write key (PBKDF2, 600,000 iterations)', h('span', {}, secret(keys.writeHex, 'the write key'), ` ${keys.msWrite} ms`)),
            row('The published form of the read key', h('span', { class: 'mono' }, readKeyString(keys.readHex, door.vaultId))),
            row('Where sgit would keep this vault’s ref and branch index', h('span', { class: 'mono' }, `${keys.refId} · ${keys.indexId}`)),
            h('p', { class: 'dim' }, `Nothing above was stored. Open the page again on any device with the passkey and the same values come out; that is why the door's key lives nowhere. Two derivations took ${keys.msRead + keys.msWrite} ms on this device; a cold unlock needs up to six.`),
        )
        $('poc6').hidden = false
        $('poc6-id').textContent = door.vaultId
    }
    $('poc3-go').addEventListener('click', () => derive())

    // 4 ---------------------------------------------------------------- recovery code
    const out4 = $('poc4-out')
    $('poc4-go').addEventListener('click', async () => {
        const rc = recoveryCode()
        S.recovery = rc
        const door = await doorFrom(rc.bytes)
        out4.replaceChildren(
            row('Recovery code (shown once in the real flow; here as often as you like)', h('b', { class: 'mono big' }, rc.shown)),
            row('Its door’s vault id', h('b', { class: 'mono' }, door.vaultId)),
            row('Its door’s passphrase', secret(door.passphrase, 'the passphrase')),
            h('p', { class: 'dim' }, 'A different door to the same master: the real flow writes the master vault’s key into both. Type the code back below to see the same door come out.'),
        )
    })
    $('poc4-check').addEventListener('click', async () => {
        const b = recoveryBytes($('poc4-code').value)
        if (!b) { $('poc4-check-out').textContent = 'That is not 26 characters of base32.'; return }
        const door = await doorFrom(b)
        $('poc4-check-out').textContent = `That code opens door ${door.vaultId}.`
        if (!S.prf && $('poc4-use').checked) await derive(b, 'the recovery code')
    })

    // 5 ---------------------------------------------------------------- test vectors
    const out5 = $('poc5-out')
    try {
        const v = await fetch(opts.vectors, { cache: 'no-store' }).then(r => r.json())
        const ikm = await sha256(v.input_text)
        const door = await doorFrom(ikm)
        const keys = await sgitKeys(door.passphrase, door.vaultId)
        const plaintext = te.encode(v.door_record_plaintext)
        const iv = (await hmac(keys.read, v.door_record_plaintext)).slice(0, 12)         // sgit's encrypt_deterministic: iv = HMAC(key, plaintext)[:12]
        const ct = await aesEncrypt(keys.read, plaintext, iv)
        const objId = 'obj-cas-imm-' + hex(await sha256(ct)).slice(0, 12)
        const got = { prf_hex: hex(ikm), seed: door.seed, passphrase: door.passphrase, vault_id: door.vaultId, read_key: keys.readHex, write_key: keys.writeHex,
                      ref_file_id: keys.refId, branch_index_file_id: keys.indexId, door_record_ct_hex: hex(ct), door_record_object_id: objId }
        const rows = Object.keys(got).map(k => row(k, h('span', { class: `mono ${got[k] === v[k] ? 'ok' : 'bad'}` }, `${got[k] === v[k] ? '✓' : '✗'} ${String(got[k]).slice(0, 40)}${String(got[k]).length > 40 ? '…' : ''}`)))
        const all = Object.keys(got).every(k => got[k] === v[k])
        out5.replaceChildren(
            h('p', { class: all ? 'ok' : 'warn' }, all ? 'The browser and sgit agree on every value.' : 'A value differs: the browser and the command line would open different vaults.'),
            row('Fake PRF bytes = SHA-256 of', v.input_text), ...rows,
            h('p', { class: 'dim' }, `The expected values were made by admin/build/passkey_vectors.py with sgit-ai ${v.sgit_version}'s own Vault__Crypto for the read and write keys, the file ids and the deterministic encryption, and the HKDF steps written out in Python. ${v.note}`),
        )
        S.vector = { ikm, door, keys }
        $('poc5-use').hidden = false
    } catch (e) { out5.replaceChildren(h('p', { class: 'warn' }, `The test vectors could not be loaded: ${err(e)}`)) }
    $('poc5-use-go').addEventListener('click', () => S.vector && derive(S.vector.ikm, 'the test vector (not a real passkey)'))

    // 6 ---------------------------------------------------------------- the server
    const out6 = $('poc6-out'), log = $('poc6-log')
    const access = $('poc6-access'), server = $('poc6-server')
    access.addEventListener('input', () => { S.access = access.value.trim(); for (const b of ['poc6-create', 'poc6-delete']) $(b).disabled = !S.access })
    window.addEventListener('pagehide', () => { S.access = ''; access.value = '' })
    const say = (line, cls) => { log.prepend(h('li', { class: cls || '' }, `${new Date().toISOString().slice(11, 19)} ${line}`)); log.hidden = false }
    const call = async (method, path, headers, body) => {
        const url = server.value.replace(/\/$/, '') + path
        say(`${method} ${url}`)
        const r = await fetch(url, { method, headers, body })
        say(`  ${r.status} ${r.statusText}`, r.ok ? 'ok' : 'warn')
        return r
    }
    const authHeaders = extra => ({ 'x-sgraph-access-token': S.access, 'X-API-Key': S.access, ...extra })
    const need = () => { if (!S.door || !S.keys) throw new Error('Derive a door first (3, or the test vector in 5).') }
    $('poc6-check').addEventListener('click', async () => {
        try {
            need()
            const id = S.door.vaultId
            const r = await call('GET', `/api/vault/public-info/${id}`)
            const t = await r.text()
            out6.replaceChildren(row(`Door ${id} on the server`, r.status === 404 ? 'no vault at this address yet (404), which is what a first run expects' : `${r.status}: ${t.slice(0, 200)}`))
            const l = await call('GET', `/api/vault/list/${id}`)
            const lt = await l.text()
            out6.append(row('Its objects', l.ok ? lt.slice(0, 300) : `${l.status}: ${lt.slice(0, 160)}`))
        } catch (e) { out6.replaceChildren(h('p', { class: 'warn' }, err(e))) }
    })
    $('poc6-create').addEventListener('click', async () => {
        try {
            need(); if (!S.access) throw new Error('Paste an access key first.')
            const id = S.door.vaultId
            const master = randomVaultKey()
            const record = { kind: 'door', v: 1, opens: 'master', master: vaultKeyString(master.passphrase, master.vaultId), made: new Date().toISOString(), by: S.doorFrom, lab: 'newsroom.sgit.ai/passkey' }
            const ct = await aesEncrypt(S.keys.read, te.encode(JSON.stringify(record)))
            const objId = 'obj-cas-imm-' + hex(await sha256(ct)).slice(0, 12)
            const r = await call('PUT', `/api/vault/write/${id}/${objId}`, authHeaders({ 'Content-Type': 'application/octet-stream', 'x-sgraph-vault-write-key': S.keys.writeHex }), ct)
            const t = await r.text()
            if (!r.ok) throw new Error(`The server refused the write: ${r.status} ${t.slice(0, 200)}`)
            S.written = { objId, master }
            out6.replaceChildren(
                h('p', { class: 'ok' }, `The door exists: vault ${id} now holds one object, written with the access key and the door’s write key, encrypted in this browser under the door’s read key.`),
                row('Object', h('span', { class: 'mono' }, `${objId} (${ct.length} bytes: 12 of iv, the ciphertext, 16 of tag)`)),
                row('Inside it, encrypted: the master vault’s key (made at random, as sgit does)', secret(record.master, 'the master key')),
                row('The server said', h('span', { class: 'mono' }, t.slice(0, 160))),
                h('p', { class: 'dim' }, 'The master vault itself is not created by this lab. Press “Open it from the server” to do what a new device would do.'),
            )
        } catch (e) { out6.replaceChildren(h('p', { class: 'warn' }, err(e))) }
    })
    $('poc6-open').addEventListener('click', async () => {
        try {
            need()
            const id = S.door.vaultId
            const l = await call('GET', `/api/vault/list/${id}`)
            if (!l.ok) throw new Error(`No vault to open at ${id} (${l.status}).`)
            const listed = await l.json()
            const names = (Array.isArray(listed) ? listed : (listed.files || listed.objects || listed.items || [])).map(x => typeof x === 'string' ? x : (x.file_id || x.id || x.name || x.key || JSON.stringify(x)))
            const objs = names.map(n => String(n).split('/').pop()).filter(n => n.startsWith('obj-cas-imm-'))
            out6.replaceChildren(row(`Objects in ${id}`, objs.length ? objs.join(', ') : `none that look like objects (${names.length} entries)`))
            let opened = 0
            for (const o of objs.slice(0, 10)) {
                const r = await call('GET', `/api/vault/read/${id}/${o}`)
                if (!r.ok) continue
                const data = new Uint8Array(await r.arrayBuffer())
                try {
                    const rec = JSON.parse(td.decode(await aesDecrypt(S.keys.read, data)))
                    opened++
                    out6.append(row(`${o}: decrypted with the door’s read key`, h('span', {}, `a ${rec.kind} record made ${String(rec.made || '').slice(0, 16)} by ${rec.by || '?'}; it holds `, rec.master ? secret(rec.master, 'the master key') : 'nothing')))
                } catch (e) { out6.append(row(o, 'does not decrypt with this door’s key (not a door record, or another key)', 'warn')) }
            }
            out6.append(h('p', { class: opened ? 'ok' : 'dim' }, opened ? `Opened: this is what any device with the passkey can do, with nothing stored and no account.` : 'Nothing opened.'))
        } catch (e) { out6.replaceChildren(h('p', { class: 'warn' }, err(e))) }
    })
    $('poc6-delete').addEventListener('click', async () => {
        try {
            need(); if (!S.access) throw new Error('Paste an access key first.')
            if (!S.written) throw new Error('Nothing written by this page in this session.')
            const r = await call('DELETE', `/api/vault/delete/${S.door.vaultId}/${S.written.objId}`, authHeaders({ 'x-sgraph-vault-write-key': S.keys.writeHex }))
            out6.replaceChildren(h('p', { class: r.ok ? 'ok' : 'warn' }, r.ok ? `Deleted ${S.written.objId}. The vault id stays registered to this door’s write key; it is never destroyed, because a destroyed id can never be used again and this one is derived.` : `The server answered ${r.status}.`))
            if (r.ok) S.written = null
        } catch (e) { out6.replaceChildren(h('p', { class: 'warn' }, err(e))) }
    })
    $('poc6-open').disabled = false
    document.documentElement.setAttribute('data-lab', 'ready')
}
