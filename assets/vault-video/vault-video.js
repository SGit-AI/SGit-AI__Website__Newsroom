// A video played straight out of a public vault, on a newsroom page.
//
// Adapted (Apache-2.0) from PrompTugal.news's assets/vault-video/vault-video.js (journalist@PrompTugal.dinis,
// 10 November 2026), the pattern Dinis Cruz pointed the newsroom to on 14 November 2026.
//
// <figure class="vault-video" data-endpoint data-vault data-key data-path> carries the vault's public read key and the
// folder of the video in the vault. The folder holds manifest.json, poster.jpg and the video as 2-second fragmented-MP4
// pieces (init.mp4, seg-NNN.m4s), made by admin/writer/tools/video-cut.sh. Each piece is a small encrypted object,
// fetched from the vault's read API and decrypted here with Web Crypto by SGVaultEmbed.Reader
// (assets/vendor/sgit-ai/2026-11-05/vault-embed.js). Only the poster is fetched before the reader presses play. Played
// through Media Source Extensions where the browser has them, starting after the first piece; otherwise the pieces are
// joined into one Blob first. Vault strings reach the page as text only.
(() => {
    'use strict'
    const boxes = [...document.querySelectorAll('figure.vault-video')]
    if (!boxes.length || !window.SGVaultEmbed) return
    const dec = new TextDecoder()
    const el = (tag, attrs = {}, kids = []) => {
        const e = document.createElement(tag)
        for (const [k, v] of Object.entries(attrs)) { if (k === 'text') e.textContent = v; else e.setAttribute(k, v) }
        e.append(...kids); return e
    }
    const mb = n => (n / 1048576).toFixed(1) + ' MB'
    const readers = {}   // one opened reader per vault, shared by every video on the page

    for (const box of boxes) mountOne(box).catch(err => {
        const s = box.querySelector('.vv-status'); if (s) s.textContent = 'The video could not be opened from the vault: ' + (err && err.message || err)
    })

    function reader(cfg) {
        const k = cfg.endpoint + '|' + cfg.vault_id
        if (!readers[k]) readers[k] = new window.SGVaultEmbed.Reader(cfg).init().then(R => R.open())
        return readers[k]
    }

    async function mountOne(box) {
        const cfg = { endpoint: box.dataset.endpoint, vault_id: box.dataset.vault, read_key: box.dataset.key.replace(/^sgit_public_read_/, '') }
        const dir = box.dataset.path.replace(/\/$/, '') + '/'
        const status = el('p', { class: 'vv-status', text: 'Opening the vault ' + cfg.vault_id + ': deriving ids, fetching ciphertext, decrypting…' })
        const video = el('video', { controls: '', playsinline: '', preload: 'none' })
        const play = el('button', { type: 'button', class: 'vv-play', 'aria-label': 'Play the video' }, [el('span', { text: '▶' })])
        const stage = el('div', { class: 'vv-stage' }, [video, play])
        box.prepend(stage, status)

        const R = await reader(cfg)
        const man = JSON.parse(dec.decode(await R.readBytes(dir + 'manifest.json')))
        if (man.width && man.height) stage.style.aspectRatio = man.width + ' / ' + man.height
        if (R.files[dir + 'poster.jpg']) {
            try { video.poster = URL.createObjectURL(new Blob([await R.readBytes(dir + 'poster.jpg')], { type: 'image/jpeg' })) } catch { }
        }
        const files = [man.init, ...man.segments.map(s => s.file)]
        const total = man.total_bytes || 0
        const secs = Math.round(man.duration), mins = Math.floor(secs / 60)
        status.textContent = `From vault ${cfg.vault_id}, decrypted in your browser: ${mins}:${String(secs % 60).padStart(2, '0')}, ${files.length} encrypted pieces, ${mb(total)}. Press play.`

        let started = false
        const start = () => {
            if (started) return; started = true; play.remove()
            ;(canMSE(man.mime) ? viaMSE : viaBlob)(R, dir, files, man, video, status, total)
                .catch(e => { status.textContent = 'Playback failed: ' + (e && e.message || e) })
        }
        play.addEventListener('click', start)
        video.addEventListener('play', () => { if (!started) { video.pause(); start() } }, { once: true })
    }

    function canMSE(mime) {
        const MS = window.ManagedMediaSource || window.MediaSource
        return !!(MS && MS.isTypeSupported && MS.isTypeSupported(mime))
    }

    // fetch the pieces a few at a time, hand them over in order; a piece refused for a moment is asked again
    async function* pieces(R, dir, files, onBytes) {
        const ahead = 4, queue = []
        let next = 0
        const read = async (p, tries = 0) => {
            try { return await R.readBytes(p) } catch (e) {
                if (tries >= 4 || !/HTTP (429|5\d\d)/.test(String(e && e.message))) throw e
                await new Promise(r => setTimeout(r, 1000 * 2 ** tries)); return read(p, tries + 1)
            }
        }
        const take = () => { const f = files[next++]; queue.push(read(dir + f).then(b => { onBytes(b.length); R.mem.delete && R.mem.delete(R.files[dir + f]); return b })) }
        while (next < files.length && queue.length < ahead) take()
        while (queue.length) { const b = await queue.shift(); if (next < files.length) take(); yield b }
    }

    async function viaMSE(R, dir, files, man, video, status, total) {
        const Managed = !!window.ManagedMediaSource, MS = window.ManagedMediaSource || window.MediaSource
        const ms = new MS()
        if (Managed) video.disableRemotePlayback = true
        video.src = URL.createObjectURL(ms)
        await new Promise(r => ms.addEventListener('sourceopen', r, { once: true }))
        ms.duration = man.duration
        const sb = ms.addSourceBuffer(man.mime)
        const appended = b => new Promise((res, rej) => { sb.addEventListener('updateend', res, { once: true }); sb.addEventListener('error', rej, { once: true }); sb.appendBuffer(b) })
        let got = 0, n = 0
        for await (const b of pieces(R, dir, files, x => { got += x })) {
            await appended(b); n++
            status.textContent = `Streaming from the vault, decrypted in your browser: ${n} of ${files.length} pieces (${mb(got)} of ${mb(total)}).`
            if (n === 2) video.play().catch(() => { })
        }
        ms.endOfStream()
        status.textContent = `Played from vault ${R.vaultId}: all ${files.length} pieces fetched and decrypted in your browser (${mb(got)}).`
    }

    async function viaBlob(R, dir, files, man, video, status, total) {
        const parts = []; let got = 0
        for await (const b of pieces(R, dir, files, x => { got += x; status.textContent = `Fetching and decrypting from the vault: ${mb(got)} of ${mb(total)}…` })) parts.push(b)
        video.src = URL.createObjectURL(new Blob(parts, { type: 'video/mp4' }))
        status.textContent = `Played from vault ${R.vaultId}: all ${files.length} pieces fetched and decrypted in your browser (${mb(got)}).`
        video.play().catch(() => { })
    }
})()
