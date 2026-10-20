/*
 * The newsroom's vault viewer (card 079): the app every reader vault opens with.
 *
 * It lives in a vault of its own, which newsroom.sgit.ai publishes with a public read key. A reader vault links it
 * read-only (newsroom-viewer.link.json and .vault/owner/ro-links.json) and its .vault/app.json makes it the default
 * app; the reader vault's index.html loads this file through the window.sg bridge with sg.loadJs. So the code is
 * shared and the data is each reader's: the viewer reads the reader's records with sg.vfs, in the reader's
 * browser, and nothing it reads leaves the vault app. Self-contained by the vault-app contract: no external
 * resources, styles inline, read-only.
 *
 * window.NewsroomViewer.render({ sg, mount, base = 'activity/', viewer = { id, path } })
 */
(function () {
  'use strict'
  var VERSION = '1.0.0'
  var KINDS = { done: 'Done', 'read-later': 'Read later', 'follow-up': 'Follow up', 'not-for-me': 'Not for me', 'more-like-this': 'More like this',
                liked: 'Liked', wrong: 'Wrong', fix: 'Fix this', idea: 'Idea', note: 'Message' }
  var esc = function (s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c] }) }
  var money = function (p, sym) { return (p < -0.004 ? '−' : '') + (sym || '£') + (Math.abs(p) / 100).toFixed(2) }
  var when = function (at) { return String(at || '').slice(0, 16).replace('T', ' ') }
  var depth = function (d) { return d >= 0.9 ? 'read it all' : d >= 0.6 ? 'most of it' : d >= 0.3 ? 'a third' : d > 0.05 ? 'glanced' : 'opened' }
  var r1 = function (x) { return Math.round(x * 10) / 10 }
  var topupKey = function (t) { return (t.ref && t.ref !== 'undefined' && t.source === 'link') ? 'ref:' + t.ref : 'at:' + t.at + '|' + t.credit + '|' + (t.device || '') }

  async function listDevices(sg, base) {
    // the index the pane writes, then the bridge's list; either may be missing
    try { var idx = JSON.parse(await sg.vfs.readText(base + 'index.json')); if (idx && Array.isArray(idx.devices)) return idx.devices.map(function (d) { return d + '.json' }) } catch (e) {}
    try {
      var l = await sg.vfs.list(base + 'devices')
      return (l || []).map(function (x) { return typeof x === 'string' ? x : (x.name || String(x.path || '').split('/').pop()) }).filter(function (n) { return /\.json$/.test(n) })
    } catch (e) { return [] }
  }
  async function readJson(sg, path) { try { return JSON.parse(await sg.vfs.readText(path)) } catch (e) { return null } }

  /** Every device's file into one view, totals recomputed from the records (the same rules as the pane's sync.js). */
  function consolidate(files, account, aliases) {
    var start = account && isFinite(Number(account.start)) ? Number(account.start) : 0
    var al = (aliases && aliases.aliases) || {}
    var reads = {}, topups = {}, notes = {}, seen = {}, devices = {}
    files.forEach(function (f) {
      var d = f.device || {}, id = al[d.id] || d.id
      var row = devices[id] || (devices[id] = { id: id, label: '', agent: '', last_sync: '', reads: 0, spent: 0, notes: 0, credit: 0, merged: [] })
      if (id === d.id) { row.label = d.label || row.label; row.agent = d.agent || row.agent } else row.merged.push(d.id)
      if (String(d.last_sync || '') > row.last_sync) row.last_sync = d.last_sync
      ;(d.merged_from || []).forEach(function (m) { if (row.merged.indexOf(m) < 0) row.merged.push(m) })
      ;(f.reads || []).forEach(function (e) { var o = reads[e.id]; var s = function (x) { return (x.declined ? 4 : 0) + (x.rating ? 2 : 0) + (x.depth || 0) }; if (!o || s(e) > s(o)) reads[e.id] = Object.assign({}, e, { device: id }); row.reads++; row.spent += e.cost || 0 })
      ;(f.topups || []).forEach(function (t) { topups[topupKey(t)] = t; row.credit += t.credit || 0 })
      ;(f.notes || []).forEach(function (n) { var o = notes[n.id]; var s = function (x) { return (x.sent ? 2 : 0) + (x.text ? 1 : 0) }; if (!o || s(n) > s(o)) notes[n.id] = Object.assign({}, n, { device: id }); row.notes++ })
      Object.keys((f.wire && f.wire.seen) || {}).forEach(function (k) { seen[k] = true })
    })
    var R = Object.keys(reads).map(function (k) { return reads[k] }).sort(function (a, b) { return String(b.at).localeCompare(String(a.at)) })
    var T = Object.keys(topups).map(function (k) { return topups[k] })
    var N = Object.keys(notes).map(function (k) { return notes[k] }).sort(function (a, b) { return String(b.at).localeCompare(String(a.at)) })
    var spent = r1(R.reduce(function (s, e) { return s + (e.cost || 0) }, 0)), credit = r1(T.reduce(function (s, t) { return s + (t.credit || 0) }, 0))
    return { start: start, reads: R, notes: N, devices: Object.keys(devices).map(function (k) { return devices[k] }),
             totals: { reads: R.length, spent: spent, credit: credit, balance: r1(start + credit - spent), notes: N.length, sent: N.filter(function (n) { return n.sent }).length, seen: Object.keys(seen).length } }
  }

  var CSS = '.nv{font:15px/1.55 system-ui,-apple-system,"Segoe UI",sans-serif;color:#1c1d21;max-width:1100px;margin:0 auto}' +
    '.nv h1{font:700 1.5rem/1.2 Georgia,serif;margin:.2rem 0 .3rem}.nv h2{font:700 .72rem/1.4 system-ui;letter-spacing:.14em;text-transform:uppercase;color:#5a5e68;margin:1.6rem 0 .5rem}' +
    '.nv .dim{color:#5a5e68;font-size:.88rem}.nv .tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:.6rem;margin:.8rem 0}' +
    '.nv .tile{border:1px solid #e3e5ea;border-radius:10px;padding:.6rem .8rem;background:#fff}.nv .tile b{display:block;font-size:1.35rem;font-variant-numeric:tabular-nums}.nv .tile span{color:#5a5e68;font-size:.78rem}' +
    '.nv table{width:100%;border-collapse:collapse;font-size:.88rem;background:#fff}.nv th,.nv td{padding:.35rem .5rem;border-bottom:1px solid #eceef2;text-align:left;vertical-align:top}.nv td.n,.nv th.n{text-align:right;font-variant-numeric:tabular-nums}' +
    '.nv .kind{display:inline-block;font-size:.72rem;font-weight:700;padding:.05rem .45rem;border-radius:999px;background:#e8f2ee;color:#0f6b4f}.nv .quote{display:block;color:#5a5e68;font-style:italic;margin-top:.15rem}' +
    '.nv .foot{margin-top:2rem;padding-top:.8rem;border-top:1px solid #e3e5ea}.nv code{font:.82rem ui-monospace,monospace;background:#f1f2f4;padding:0 .25rem;border-radius:4px}.nv .wrap{overflow-x:auto}'

  async function render(opts) {
    var sg = opts.sg, mount = opts.mount, base = opts.base || 'activity/', viewer = opts.viewer || {}
    var account = await readJson(sg, base + 'account.json'), aliases = await readJson(sg, base + 'aliases.json')
    var names = await listDevices(sg, base), files = []
    for (var i = 0; i < names.length; i++) { var f = await readJson(sg, base + 'devices/' + names[i]); if (f && f.device) files.push(f) }
    var c = consolidate(files, account, aliases), sym = (account && account.symbol) || '£'
    var tile = function (v, k) { return '<div class="tile"><b>' + esc(v) + '</b><span>' + esc(k) + '</span></div>' }
    var html = '<style>' + CSS + '</style><div class="nv">' +
      '<h1>Your newsroom vault</h1><p class="dim">What you read on newsroom.sgit.ai, what it cost and what you noted, from every device, read here in the vault itself. ' +
      'This page runs inside your vault app; nothing it reads is sent anywhere.</p>' +
      '<div class="tiles">' + tile(money(c.totals.balance, sym), 'balance') + tile(c.totals.reads, 'pages read') + tile(money(c.totals.spent, sym), 'spent') +
        tile(c.totals.credit ? money(c.totals.credit, sym) : '–', 'topped up') + tile(c.totals.notes, 'notes, ' + c.totals.sent + ' sent') + tile(c.totals.seen, 'wire stories seen') + tile(c.devices.length, 'devices') + '</div>' +
      '<p class="dim">Recomputed from the records, as the pane does it: starting credit ' + money(c.start, sym) + ', plus top-ups, minus what was read and not declined.</p>' +
      '<h2>Devices</h2><div class="wrap"><table><thead><tr><th>Device</th><th class="n">Reads</th><th class="n">Spent</th><th class="n">Top-ups</th><th class="n">Notes</th><th>Last update</th></tr></thead><tbody>' +
      (c.devices.length ? c.devices.map(function (d) { return '<tr><td>' + esc(d.label || d.id) + (d.merged.length ? '<span class="quote">merged from ' + esc(d.merged.join(', ')) + '</span>' : '') + '</td><td class="n">' + d.reads + '</td><td class="n">' + money(r1(d.spent), sym) + '</td><td class="n">' + (d.credit ? money(r1(d.credit), sym) : '–') + '</td><td class="n">' + d.notes + '</td><td>' + esc(when(d.last_sync)) + '</td></tr>' }).join('')
        : '<tr><td colspan="6" class="dim">No device has updated this vault yet.</td></tr>') + '</tbody></table></div>' +
      '<h2>Reading</h2><div class="wrap"><table><thead><tr><th>Page</th><th>When</th><th>How far</th><th class="n">Cost</th></tr></thead><tbody>' +
      (c.reads.slice(0, 40).map(function (e) { return '<tr><td>' + esc(e.title || e.path) + (e.declined ? ' <span class="kind">declined</span>' : '') + '</td><td>' + esc(when(e.at)) + '</td><td>' + depth(e.depth || 0) + '</td><td class="n">' + (e.cost ? r1(e.cost) + 'p' : '–') + '</td></tr>' }).join('') || '<tr><td colspan="4" class="dim">Nothing read yet.</td></tr>') +
      '</tbody></table></div>' + (c.reads.length > 40 ? '<p class="dim">and ' + (c.reads.length - 40) + ' more.</p>' : '') +
      '<h2>Notes</h2>' + (c.notes.length ? '<div class="wrap"><table><tbody>' + c.notes.slice(0, 40).map(function (n) {
        return '<tr><td><span class="kind">' + esc(KINDS[n.kind] || n.kind) + '</span></td><td>' + esc(n.title || n.path) + (n.text ? '<span class="quote" style="font-style:normal;color:#1c1d21">' + esc(n.text) + '</span>' : '') + (n.quote ? '<span class="quote">“' + esc(n.quote.slice(0, 220)) + '”</span>' : '') +
          '</td><td>' + esc(when(n.at)) + (n.sent ? '<span class="quote">sent ' + esc(String(n.sent.at).slice(0, 10)) + '</span>' : '') + '</td></tr>' }).join('') + '</tbody></table></div>' : '<p class="dim">No notes yet.</p>') +
      '<div class="foot dim">This viewer is shared: it lives in a vault of its own' + (viewer.id ? ' (<code>' + esc(viewer.id) + '</code>)' : '') + ', which the newsroom publishes, and your vault links it read-only' + (viewer.path ? ' at <code>' + esc(viewer.path) + '</code>' : '') +
        '. Your records never go into it; it reads them here. Viewer ' + VERSION + '.</div></div>'
    mount.innerHTML = html
    return c
  }

  window.NewsroomViewer = { render: render, consolidate: consolidate, version: VERSION }
})()
