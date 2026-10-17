/**
 * sg-embed.js: open a vault in the SG/Vault app, in a frame, by its embed protocol, from code (card 079).
 *
 * The same handshake as the site's imported assets/vault-ui-embed.js (sgit.ai's, which this site must not edit):
 * load the app with ?embed=1&parent=<origin>, wait for {sg:'vault-embed-ready'} from THAT frame, then post
 * {sg:'vault-open', key, mode} with the target origin pinned to the app's origin. The key is a READ key,
 * sgit_rk1_<64 hex>:<vault id>: it is handed over postMessage, never put in an address or in the page's markup,
 * and the app keeps it in memory. vault-ready and vault-error come back and drive the status line.
 *
 * @module sg-embed
 */
export const ORIGIN = 'https://dev.vault.sgraph.ai'

/** Mount one surface ('app' or 'vault') into `host`; returns { frame, done } where done resolves on ready or error. */
export function mountEmbed(host, { vaultId, readKeyHex, mode = 'app', label = '' }) {
    if (!/^[0-9a-f]{64}$/.test(String(readKeyHex)) || !vaultId) throw new Error('a read key (64 hex) and a vault id are needed')
    const cred = `sgit_rk1_${readKeyHex}:${vaultId}`
    const note = document.createElement('p'); note.className = 'dim sgv-embed-note'; note.textContent = 'Handshaking with the SG/Vault app…'
    const frame = document.createElement('iframe')
    frame.className = 'sgv-embed-frame'; frame.title = `The SG/Vault app (${mode === 'app' ? 'App Mode' : 'vault browser'}), opened read-only`
    frame.style.cssText = 'width:100%;height:760px;border:1px solid var(--line, #e3e5ea);border-radius:10px;background:var(--panel, #fff)'
    const head = document.createElement('div'); head.className = 'sgv-embed-label'; head.textContent = label || (mode === 'app' ? 'App Mode: the vault’s own app' : 'The vault browser: files, SGit, settings')
    host.append(head, note, frame)
    let resolve; const done = new Promise(r => { resolve = r })
    const timer = setTimeout(() => { note.textContent = 'The SG/Vault app did not answer the handshake.'; resolve({ ok: false, error: 'timeout' }) }, 15000)
    const onMsg = e => {
        if (e.origin !== ORIGIN || e.source !== frame.contentWindow) return
        const d = e.data || {}
        if (d.sg === 'vault-embed-ready') { e.source.postMessage({ sg: 'vault-open', key: cred, mode }, ORIGIN); note.textContent = 'Handshake complete: the read key was handed over postMessage. Opening…' }
        else if (d.sg === 'vault-ready') { clearTimeout(timer); note.textContent = `Opened read-only over the embed protocol; the key never appeared in an address and was not stored${d.fileCount ? `; ${d.fileCount} files decrypted in the frame` : ''}.`; resolve({ ok: true }) }
        else if (d.sg === 'vault-error') { clearTimeout(timer); note.textContent = `The vault did not open: ${d.message || 'unknown error'}`; resolve({ ok: false, error: d.message }) }
    }
    window.addEventListener('message', onMsg)
    frame.src = `${ORIGIN}/en-gb/${mode === 'vault' ? 'vault' : 'app'}/?embed=1&parent=${encodeURIComponent(location.origin)}`
    return { frame, done }
}
