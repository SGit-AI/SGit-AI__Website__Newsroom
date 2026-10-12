/**
 * vault-pane.js: the reader's vault, as a pane on the right of every page.
 *
 * What it does (the design is admin/notes/2026-10-12__the-activity-vault.md, the pieces are the passkey lab's):
 *   - Enable the account on this device: the passkey's PRF bytes derive the door (assets/door.js); the door opens the
 *     master, the master opens the reader vault and gives the access key (assets/newsroom-vault.js). No door at the
 *     address means "no door here for this path yet": create an account (an access key, pasted once, kept in the
 *     master), or type the recovery code to add this path as a door.
 *   - Update the vault: this device's records (reads, top-ups, personas, raw, from the meter's local storage) written
 *     as one file in the reader vault, one commit, published. Only when the reader asks.
 *   - Across your devices: every device's file read, consolidated, totals recomputed (assets/vault-pane/sync.js);
 *     "Bring their activity here" adds other devices' records to this browser's local storage and reloads.
 *   - Every call to the vault server is listed as it happens.
 *
 * Where the keys live: in memory, and for the life of this tab in sessionStorage (so a page change does not ask
 * for the passkey again). Nothing is written to localStorage but this device's id and label. The vault library
 * (assets/vendor/sg-vault, twelve pinned files and one local extension) is loaded from this origin the first time
 * it is needed, not on every page.
 *
 * @module vault-pane
 */
import * as NV from '../newsroom-vault.js'
import { doorFrom, prfBytes, recoveryBytes, recoveryCode, vaultKeyString, PRF_INPUT_TEXT, sha256 } from '../door.js'
import { extract, consolidate, mergeInto, accountFile, PATHS, describe } from './sync.js'

const ROOT = new URL('../../', import.meta.url)                       // assets/vault-pane/ → the site root
const ENDPOINT = 'https://dev.send.sgraph.ai'
const LIB = ['sg-send/sg-send-crypto.js', 'sg-send/sg-send.js', 'sg-vault/sg-vault-crypto.js', 'sg-vault/sg-vault-object-store.js', 'sg-vault/sg-vault-ref-manager.js',
             'sg-vault/sg-vault-commit.js', 'sg-vault/sg-vault.js', 'sg-vault/sg-vault--file-ops.js', 'sg-vault/sg-vault--folder-ops.js', 'sg-vault/sg-vault--sync.js',
             'sg-vault/sg-vault--history.js', 'sg-vault/sg-vault--branches.js'].map(f => `assets/vendor/sg-vault/v0.2.3/${f}`).concat(['assets/vendor/sg-vault/local/sg-vault--create-with-id.js'])
const SESSION = 'sgit.vault.session', LABEL = 'sgit.device-label'
const TOKEN_FILE = { folder: '/.vault', name: 'access-token.json' }    // where the library's readEmbeddedAccessToken() looks

const h = (tag, attrs, ...kids) => {
    const el = document.createElement(tag)
    for (const [k, v] of Object.entries(attrs || {})) { if (v === false || v == null) continue; if (k.startsWith('on')) el.addEventListener(k.slice(2), v); else el.setAttribute(k, v === true ? '' : v) }
    for (const kid of kids.flat()) if (kid != null && kid !== false) el.append(kid instanceof Node ? kid : String(kid))
    return el
}
const row = (k, v) => h('div', { class: 'kv' }, h('span', { class: 'k' }, k), h('span', { class: 'v' }, v))
const err = e => (e && e.name && e.name !== 'Error' ? `${e.name}: ` : '') + String(e && e.message || e)
const money = (p, sym) => `${p < -0.004 ? '−' : ''}${sym || '£'}${(Math.abs(p) / 100).toFixed(2)}`
const secret = (text, label) => {
    const span = h('span', { class: 'mono' }, `•••••••••••• (${text.length} characters)`)
    let shown = false
    const btn = h('button', { type: 'button', class: 'btn', onclick: () => { shown = !shown; span.textContent = shown ? text : `•••••••••••• (${text.length} characters)`; btn.textContent = shown ? 'Hide' : `Reveal ${label}` } }, `Reveal ${label}`)
    const copy = h('button', { type: 'button', class: 'btn', onclick: async () => { try { await navigator.clipboard.writeText(text); copy.textContent = 'Copied' } catch (e) { copy.textContent = 'Could not copy' } setTimeout(() => { copy.textContent = 'Copy' }, 1500) } }, 'Copy')
    return h('span', { class: 'secret' }, span, btn, copy)
}

// ------------------------------------------------------------ the meter's config and state, read as the meter reads them
function meterCfg() {
    let cfg = {}
    try { const el = document.getElementById('sg-meter-config'); if (el) cfg = JSON.parse(el.textContent) } catch (e) { cfg = {} }
    return { storageKey: cfg.storageKey || 'sg.meter.v1', start: cfg.start == null ? 500 : cfg.start, symbol: cfg.symbol || '£' }
}
const readState = key => { try { return JSON.parse(localStorage.getItem(key) || 'null') } catch (e) { return null } }

// ------------------------------------------------------------ the session: keys for the life of this tab
const session = {
    get() { try { return JSON.parse(sessionStorage.getItem(SESSION) || 'null') } catch (e) { return null } },
    set(v) { try { if (v) sessionStorage.setItem(SESSION, JSON.stringify(v)); else sessionStorage.removeItem(SESSION) } catch (e) { /* no storage: memory only */ } },
}
let libLoading = null
function loadLibrary() {
    if (typeof SGVault !== 'undefined' && typeof SGVault.createWithId === 'function') return Promise.resolve()
    if (libLoading) return libLoading
    libLoading = (async () => {
        for (const f of LIB) await new Promise((res, rej) => { const s = document.createElement('script'); s.src = new URL(f, ROOT).href; s.onload = res; s.onerror = () => rej(new Error(`could not load ${f}`)); document.head.append(s) })
    })()
    return libLoading
}

// ------------------------------------------------------------ the pane
export function mount() {
    if (document.getElementById('sgit-vault-pane')) return
    const cfg = meterCfg()
    const deviceId = NV.deviceBranch()
    let label = ''; try { label = localStorage.getItem(LABEL) || '' } catch (e) { /* fine */ }
    const body = h('div', { class: 'body' })
    const fill = (...kids) => body.replaceChildren(...kids.flat().filter(k => k != null && k !== false))   // replaceChildren would print a null as text
    const log = h('ul', { class: 'log', hidden: true })
    const pane = h('aside', { id: 'sgit-vault-pane', class: 'vault-pane', 'aria-label': 'Your vault' },
        h('div', { class: 'head' }, h('h2', {}, 'Your vault'), h('button', { type: 'button', class: 'btn close', onclick: () => toggle(false) }, 'Close')),
        h('p', { class: 'dim' }, 'The reading account this browser keeps, carried between your devices through an encrypted vault that opens with your passkey. Local storage stays the place it lives; the vault is updated when you ask.'),
        body,
        h('h3', {}, 'Calls to the vault server'), log)
    document.body.append(pane)
    const state = { drawn: false, vaults: null, consolidated: null, busy: false, sg: null }
    const buttons = [...document.querySelectorAll('.vault-btn')]
    const toggle = open => {
        const on = open == null ? !document.documentElement.classList.contains('vault-open') : open
        document.documentElement.classList.toggle('vault-open', on)
        for (const b of buttons) b.setAttribute('aria-expanded', String(on))
        if (on && !state.drawn) draw()
    }
    for (const b of buttons) b.addEventListener('click', () => toggle())
    if (location.hash === '#vault' || document.documentElement.hasAttribute('data-vault-open')) toggle(true)

    const say = (line, cls) => { log.prepend(h('li', { class: cls || '' }, `${new Date().toISOString().slice(11, 19)} ${line}`)); log.hidden = false; while (log.children.length > 60) log.lastChild.remove() }
    const origFetch = window.fetch.bind(window)
    window.fetch = async (input, init) => {
        const u = String(input instanceof Request ? input.url : input)
        if (!u.startsWith(ENDPOINT + '/')) return origFetch(input, init)
        const method = (init && init.method) || (input instanceof Request ? input.method : 'GET')
        const r = await origFetch(input, init)
        say(`${method} ${u.slice(ENDPOINT.length).replace(/\/obj-cas-imm-[0-9a-f]{12}/g, '/obj-cas-imm-…')} → ${r.status}`, r.ok || r.status === 404 ? '' : 'warn')
        return r
    }

    const setButtons = () => { for (const b of buttons) { b.classList.toggle('on', !!session.get()); const d = b.querySelector('.dot'); if (d) d.title = session.get() ? 'enabled on this device' : 'not enabled on this device' } }
    setButtons()

    async function client(token) { await loadLibrary(); if (!state.sg) state.sg = NV.client({ endpoint: ENDPOINT, token: token || '' }); if (token) state.sg.token = token; return state.sg }

    /** Open everything from a session record { door:{passphrase,vaultId}, path } : the door, the master (and its access key), the reader vault. */
    async function openAll(rec) {
        const sg = await client(rec.token || '')
        const u = await NV.unlock({ sgSend: sg, door: rec.door })
        let token = rec.token || ''
        if (!token) { try { const t = await NV.readJson(u.master, `${TOKEN_FILE.folder}/${TOKEN_FILE.name}`); token = t && t.token || '' } catch (e) { token = '' } }
        if (token) sg.token = token
        state.vaults = { ...u, token }
        session.set({ ...rec, token })
        setButtons()
        return state.vaults
    }

    async function draw() {
        state.drawn = true
        const rec = session.get()
        if (!rec) return drawLocked()
        fill(h('p', { class: 'dim' }, 'Opening your vault…'))
        try { await openAll(rec); await drawUnlocked() }
        catch (e) { session.set(null); setButtons(); drawLocked(h('p', { class: 'warn' }, `The vault could not be opened from the saved session: ${err(e)}. Enable it again.`)) }
    }

    function drawLocked(note) {
        const device = h('input', { type: 'text', value: label, maxlength: 40, placeholder: 'this device, e.g. "my laptop"' })
        device.addEventListener('change', () => { label = device.value.trim(); try { localStorage.setItem(LABEL, label) } catch (e) { /* fine */ } })
        fill(
            note || null,
            h('h3', {}, 'On this device'),
            row('Device', h('span', { class: 'mono' }, deviceId)),
            h('label', {}, 'A label for it', device),
            h('div', { class: 'acts' },
                h('button', { type: 'button', class: 'btn primary', id: 'vault-enable', onclick: enable }, 'Enable with your passkey'),
                h('button', { type: 'button', class: 'btn', id: 'vault-recover', onclick: () => drawRecover() }, 'I have a recovery code')),
            h('p', { class: 'dim' }, 'Your passkey gives this page 32 bytes that derive the address and key of a small door vault; the door holds the key of your master vault; the master holds your reader vault and your access key. Nothing is stored to be found, and nothing leaves this browser but ciphertext. ', h('a', { href: new URL('vault/index.html', ROOT).href }, 'How it works'), '.'),
        )
    }

    async function withBusy(btnId, fn) {
        const b = btnId && document.getElementById(btnId); if (b) b.disabled = true
        state.busy = true
        try { return await fn() } finally { state.busy = false; if (b) b.disabled = false }
    }

    async function enable() {
        await withBusy('vault-enable', async () => {
            const status = h('p', { class: 'dim' }, 'Waiting for your passkey…')
            body.prepend(status)
            let prf
            try { prf = await prfBytes() }
            catch (e) {
                if (e.code === 'ENOPRF') { status.replaceWith(h('p', { class: 'warn' }, 'The passkey signed but gave no PRF bytes: this provider cannot be a door here. The recovery code is the way in on this device.')); return }
                status.replaceWith(h('div', { class: 'warn' }, h('p', {}, `No passkey answered (${err(e)}). If you have none for this site yet, make one:`),
                    h('div', { class: 'acts' }, h('button', { type: 'button', class: 'btn primary', onclick: makePasskey }, 'Make a passkey for this site'))))
                return
            }
            status.textContent = 'Deriving the door from the bytes…'
            const door = await doorFrom(prf.bytes)
            try {
                status.textContent = 'Opening the door, the master and the reader vault…'
                await openAll({ door, path: prf.path, credId: prf.credId })
                await drawUnlocked()
            } catch (e) {
                if (e.code === 'ENOVAULT') drawNoDoor(door, prf)
                else status.replaceWith(h('p', { class: 'warn' }, err(e)))
            }
        })
    }

    async function makePasskey() {
        try {
            await navigator.credentials.create({ publicKey: {
                challenge: crypto.getRandomValues(new Uint8Array(32)), rp: { id: location.hostname, name: 'SGit Newsroom' },
                user: { id: crypto.getRandomValues(new Uint8Array(16)), name: 'reader', displayName: 'A reader of the SGit Newsroom' },
                pubKeyCredParams: [{ type: 'public-key', alg: -7 }, { type: 'public-key', alg: -257 }],
                authenticatorSelection: { residentKey: 'required', userVerification: 'required' },
                extensions: { prf: { eval: { first: await sha256(PRF_INPUT_TEXT) } } }, timeout: 120000,
            } })
            drawLocked(h('p', { class: 'ok' }, 'A passkey was made for this site. Now enable the vault with it.'))
        } catch (e) { drawLocked(h('p', { class: 'warn' }, `The passkey was not made: ${err(e)}`)) }
    }

    function drawNoDoor(door, prf) {
        const access = h('input', { type: 'password', autocomplete: 'off', placeholder: 'kept in memory, then inside your master vault' })
        const code = h('input', { type: 'text', autocomplete: 'off', placeholder: 'XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XX' })
        fill(
            h('p', { class: 'warn', id: 'vault-nodoor' }, `No door here for this path yet (${door.vaultId}, ${prf.path}). Either this is your first device, or your account was made through another path.`),
            h('h3', {}, 'First device: create the account'),
            h('p', { class: 'dim' }, 'Three vaults are made: this door, a master and a reader vault. The access key is the thing a reader buys; it is written into the master so no other device needs it typed.'),
            h('label', {}, 'Access key', access),
            h('div', { class: 'acts' }, h('button', { type: 'button', class: 'btn primary', id: 'vault-create', onclick: () => createAccount(door, prf, access.value.trim()) }, 'Create the account')),
            h('h3', {}, 'Another device of an existing account'),
            h('p', { class: 'dim' }, 'Type the recovery code once: it opens the recovery door, the master comes with its access key, and this path gets a door of its own.'),
            h('label', {}, 'Recovery code', code),
            h('div', { class: 'acts' }, h('button', { type: 'button', class: 'btn', id: 'vault-join', onclick: () => joinWithCode(code.value, door, prf) }, 'Add this device with the code')),
            h('div', { class: 'acts' }, h('button', { type: 'button', class: 'btn', onclick: () => drawLocked() }, 'Back')),
        )
    }

    function drawRecover() {
        const code = h('input', { type: 'text', autocomplete: 'off', placeholder: 'XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XX' })
        fill(
            h('h3', {}, 'Open with the recovery code'),
            h('p', { class: 'dim' }, 'The code derives the recovery door, which holds the same master key. Use it on a device whose passkey cannot be a door, or to add a passkey path afterwards.'),
            h('label', {}, 'Recovery code', code),
            h('div', { class: 'acts' }, h('button', { type: 'button', class: 'btn primary', id: 'vault-join', onclick: () => joinWithCode(code.value, null, null) }, 'Open'), h('button', { type: 'button', class: 'btn', onclick: () => drawLocked() }, 'Back')),
        )
    }

    async function createAccount(door, prf, token) {
        if (!token) { body.prepend(h('p', { class: 'warn' }, 'An access key is needed to create the vaults.')); return }
        await withBusy('vault-create', async () => {
            const status = h('p', { class: 'dim' }, 'Creating three vaults: six key derivations and three first commits…'); body.prepend(status)
            try {
                const sg = await client(token)
                const a = await NV.createAccount({ sgSend: sg, door, record: { kind: 'passkey', path: prf.path, credential_id: prf.credId, device: label || deviceId } })
                await NV.writeFile(a.master, TOKEN_FILE.folder, TOKEN_FILE.name, JSON.stringify({ token }))
                await NV.writeFile(a.master, '/', 'recovery.json', JSON.stringify({ v: 1, note: 'the recovery code is shown once and kept by the reader; this file records only that one exists', made: new Date().toISOString() }))
                await NV.publish(a.master)
                const rc = recoveryCode()
                const rdoor = await doorFrom(rc.bytes)
                await NV.addDoor({ sgSend: sg, master: a.master, door: rdoor, record: { kind: 'recovery', device: label || deviceId } })
                const cfgNow = meterCfg()
                await NV.writeFile(a.reader, '/activity', 'account.json', JSON.stringify(accountFile(cfgNow, deviceId), null, 1))
                await NV.publish(a.reader)
                state.vaults = { door: a.door, master: a.master, reader: a.reader, doors: a.doors, record: a.record, token }
                session.set({ door, path: prf.path, credId: prf.credId, token }); setButtons()
                await drawUnlocked(h('div', { class: 'warn', id: 'vault-recovery-shown' }, h('p', {}, h('b', {}, 'Your recovery code, shown once. Write it down: '), h('span', { class: 'mono' }, rc.shown)), h('p', { class: 'dim' }, 'It opens a second door to the same master, for a device with no passkey and for the day the passkey is gone. The page does not keep it.')))
            } catch (e) { status.replaceWith(h('p', { class: 'warn' }, e.code === 'EEXISTS' ? 'A vault already exists at this door: enable again to open it.' : err(e))) }
        })
    }

    async function joinWithCode(codeText, door, prf) {
        const bytes = recoveryBytes(codeText)
        if (!bytes) { body.prepend(h('p', { class: 'warn' }, 'That is not a 26-character recovery code.')); return }
        await withBusy('vault-join', async () => {
            const status = h('p', { class: 'dim' }, 'Opening the recovery door…'); body.prepend(status)
            try {
                const rdoor = await doorFrom(bytes)
                const u = await openAll({ door: rdoor, path: 'recovery' })
                if (door && prf) {
                    status.textContent = 'Adding this passkey path as a door…'
                    if (!u.token) throw new Error('The master holds no access key, so a door cannot be written from here; create the account again with one.')
                    const sg = await client(u.token)
                    await NV.addDoor({ sgSend: sg, master: u.master, door, record: { kind: 'passkey', path: prf.path, credential_id: prf.credId, device: label || deviceId } })
                    session.set({ door, path: prf.path, credId: prf.credId, token: u.token })
                }
                await drawUnlocked(h('p', { class: 'ok' }, door ? 'This device now has a door of its own; the code is not needed here again.' : 'Opened with the recovery code.'))
            } catch (e) { status.replaceWith(h('p', { class: 'warn' }, e.code === 'ENOVAULT' ? 'No account answers to that code.' : err(e))) }
        })
    }

    async function drawUnlocked(note) {
        const v = state.vaults, cfgNow = meterCfg(), st = readState(cfgNow.storageKey)
        const local = st ? { reads: (st.log || []).length, own: (st.log || []).filter(e => !e.device || e.device === deviceId).length, balance: st.balance } : null
        const device = h('input', { type: 'text', value: label, maxlength: 40, placeholder: 'this device, e.g. "my laptop"' })
        device.addEventListener('change', () => { label = device.value.trim(); try { localStorage.setItem(LABEL, label) } catch (e) { /* fine */ } })
        const across = h('div', { id: 'vault-across' }, h('p', { class: 'dim' }, 'Reading the devices’ files…'))
        fill(
            note || null,
            h('h3', {}, 'This device'),
            row('Device', h('span', {}, h('span', { class: 'mono' }, deviceId), label ? ` · ${label}` : '')),
            h('label', {}, 'Label', device),
            row('Door', h('span', { class: 'mono' }, `${v.door.vaultId}${session.get() && session.get().path ? ' · ' + session.get().path : ''}`)),
            row('Master', h('span', { class: 'mono' }, v.master.vaultId)),
            row('Reader vault', v.reader ? h('span', {}, h('span', { class: 'mono' }, v.reader.vaultId), ' ', secret(NV.prefixedKey(v.reader), 'the key')) : 'none'),
            row('Access key', v.token ? 'in the master vault, in memory here' : 'none: writes will fail'),
            local ? row('Here', `${local.own} read(s) of this device, ${local.reads - local.own} brought in, balance ${money(local.balance, cfgNow.symbol)}`) : row('Here', 'no reading account in this browser yet'),
            h('div', { class: 'acts' },
                h('button', { type: 'button', class: 'btn primary', id: 'vault-sync', disabled: !v.token || !v.reader, onclick: sync }, 'Update the vault'),
                h('button', { type: 'button', class: 'btn', id: 'vault-refresh', onclick: () => refreshAcross() }, 'Check the vault'),
                h('button', { type: 'button', class: 'btn', onclick: () => { session.set(null); state.vaults = null; setButtons(); drawLocked(h('p', { class: 'dim' }, 'Forgotten on this device; the vault is unchanged.')) } }, 'Forget on this device')),
            h('div', { id: 'vault-sync-out' }),
            h('h3', {}, 'Across your devices'), across,
        )
        await refreshAcross()
    }

    async function readAll() {
        const v = state.vaults
        const names = (await NV.listFiles(v.reader, PATHS.devicesFolder).catch(() => [])).filter(n => n.endsWith('.json'))
        const files = []
        for (const n of names) { try { files.push(await NV.readJson(v.reader, `${PATHS.devicesFolder}/${n}`)) } catch (e) { /* a bad file is left out */ } }
        const account = await NV.readJson(v.reader, PATHS.account).catch(() => null)
        state.consolidated = consolidate(files, account || { start: meterCfg().start })
        return state.consolidated
    }

    async function refreshAcross() {
        const across = document.getElementById('vault-across'); if (!across) return
        try {
            const v = state.vaults
            if (v.reader) { try { await v.reader.pull() } catch (e) { /* unpushed local commits, or nothing new */ } }
            const c = await readAll(), sym = meterCfg().symbol
            const others = c.devices.filter(d => d.id !== deviceId)
            across.replaceChildren(
                c.devices.length ? h('table', {}, h('thead', {}, h('tr', {}, h('th', {}, 'Device'), h('th', { class: 'n' }, 'Reads'), h('th', { class: 'n' }, 'Spent'), h('th', { class: 'n' }, 'Top-ups'), h('th', {}, 'Last sync'))),
                    h('tbody', {}, ...c.devices.map(d => h('tr', { class: d.id === deviceId ? 'me' : '' }, h('td', {}, d.label || d.id, d.id === deviceId ? ' (here)' : ''), h('td', { class: 'n' }, d.reads), h('td', { class: 'n' }, money(d.spent, sym)), h('td', { class: 'n' }, d.credit ? money(d.credit, sym) : '–'), h('td', {}, String(d.last_sync || '').slice(0, 16).replace('T', ' ')))),
                        h('tr', { class: 'total' }, h('td', {}, `All, ${c.devices.length} device(s)`), h('td', { class: 'n' }, c.totals.reads), h('td', { class: 'n' }, money(c.totals.spent, sym)), h('td', { class: 'n' }, money(c.totals.credit, sym)), h('td', {}, `balance ${money(c.totals.balance, sym)}`))))
                    : h('p', { class: 'dim' }, 'No device has updated the vault yet.'),
                h('p', { class: 'dim' }, `Totals are recomputed from the records: starting credit ${money(c.start, sym)}, plus top-ups, minus what was read and not declined. The vault holds records, never totals.`),
                others.length ? h('div', { class: 'acts' }, h('button', { type: 'button', class: 'btn', id: 'vault-merge', onclick: merge }, `Bring ${others.length === 1 ? 'that device’s' : 'their'} activity here`)) : null,
            )
        } catch (e) { across.replaceChildren(h('p', { class: 'warn' }, `The devices’ files could not be read: ${err(e)}`)) }
    }

    async function sync() {
        await withBusy('vault-sync', async () => {
            const out = document.getElementById('vault-sync-out'); out.replaceChildren(h('p', { class: 'dim' }, 'Writing this device’s records as one commit, then publishing…'))
            try {
                const v = state.vaults, cfgNow = meterCfg(), st = readState(cfgNow.storageKey)
                if (!st) throw new Error('There is no reading account in this browser yet: open an article first.')
                try { await v.reader.pull() } catch (e) { /* fine */ }
                const prev = await NV.readJson(v.reader, PATHS.device(deviceId)).catch(() => null)
                const file = extract(st, { id: deviceId, label, agent: (navigator.userAgentData && navigator.userAgentData.platform) || navigator.platform || '' }, prev)
                await NV.writeFile(v.reader, PATHS.devicesFolder, `${deviceId}.json`, JSON.stringify(file, null, 1))
                if (!(await NV.readJson(v.reader, PATHS.account).catch(() => null))) await NV.writeFile(v.reader, '/activity', 'account.json', JSON.stringify(accountFile(cfgNow, deviceId), null, 1))
                await NV.publish(v.reader)
                out.replaceChildren(h('p', { class: 'ok', id: 'vault-synced' }, `Updated: ${describe(file)}, as one commit, published. Sync ${file.device.syncs} from this device.`))
                await refreshAcross()
            } catch (e) { out.replaceChildren(h('p', { class: 'warn' }, `The vault was not updated: ${err(e)}`)) }
        })
    }

    async function merge() {
        await withBusy('vault-merge', async () => {
            const cfgNow = meterCfg(), st = readState(cfgNow.storageKey) || { v: 3, created: new Date().toISOString(), balance: cfgNow.start, spent: 0, reads: 0, declined: 0, paused: false, log: [], topups: [], cart: [], sessions: [], active: 'me', personas: [{ id: 'me', name: '', created: new Date().toISOString(), on: [], off: [] }] }
            const c = state.consolidated || await readAll()
            const m = mergeInto(st, c, deviceId)
            try { localStorage.setItem(cfgNow.storageKey, JSON.stringify(m.state)) } catch (e) { document.getElementById('vault-across').prepend(h('p', { class: 'warn' }, 'This browser’s storage refused the write.')); return }
            try { sessionStorage.setItem('sgit.vault.merged', JSON.stringify({ at: Date.now(), added: m.added })) } catch (e) { /* fine */ }
            location.reload()
        })
    }

    // after a merge, say what arrived
    try {
        const m = JSON.parse(sessionStorage.getItem('sgit.vault.merged') || 'null')
        if (m && Date.now() - m.at < 10000) { sessionStorage.removeItem('sgit.vault.merged'); toggle(true); setTimeout(() => body.prepend(h('p', { class: 'ok', id: 'vault-merged' }, `Brought in: ${m.added.reads} read(s), ${m.added.topups} top-up(s), ${m.added.personas} persona(s). The meter now shows the consolidated figures.`)), 50) }
    } catch (e) { /* fine */ }
}

if (typeof document !== 'undefined') {
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mount); else mount()
}
