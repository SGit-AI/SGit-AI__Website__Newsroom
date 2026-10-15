/* newsroom.sgit.ai: the front page's behaviour (card 063). Plain script, loaded in <head> on purpose.
 *
 * 1. Before the first paint: which of the three views to show. The reader's last choice is kept in this
 *    browser under newsroom.view; a ?view= in the address wins for that visit (and is remembered), which is
 *    how a link can open the Briefing or Your desk directly, and how an A/B test sends readers to one view.
 *    An unknown value is Broadsheet. The stylesheet shows the view data-view on <html> names, so setting it
 *    here, synchronously, means no flash of the wrong page. Without JavaScript the attribute is never set,
 *    the stylesheet shows Broadsheet and hides the switcher: the page is complete, not broken.
 *
 * 2. After the DOM: the switcher (a radio group: click, arrows, Home/End), and the reader's own numbers,
 *    read from the meter's and the pane's local records (the same localStorage the reading meter and the
 *    vault pane keep, assets/components/sg-meter and assets/vault-pane/notes.js), never written here:
 *      · the You card: credit left, spent so far, articles opened, notes kept
 *      · the picks: a status each (New; Reading, opened; Done, read to the end or decided done in the pane;
 *        Follow-up, decided read-later or follow-up in the pane), the progress bar, the board counts
 *      · the active persona: the meter's active persona picks whose picks are shown; the chooser can
 *        change it (the meter's own visit/setActive, through its module, so the balance chip follows)
 *      · the glance in the switcher row: the same progress and spend, on every view, so the reader sees
 *        there is a user area before they know what a vault is
 *    Everything refreshes on the meter's and the pane's events. Nothing is sent anywhere.
 */
(function () {
  'use strict'
  var VIEWS = ['broadsheet', 'briefing', 'desk'], KEY = 'newsroom.view', NOTES = 'sgit.notes.v1'
  var html = document.documentElement
  var store = {
    get: function (k) { try { return localStorage.getItem(k) } catch (e) { return null } },
    set: function (k, v) { try { localStorage.setItem(k, v) } catch (e) { /* private window: this visit only */ } },
    json: function (k) { try { return JSON.parse(localStorage.getItem(k) || 'null') } catch (e) { return null } }
  }

  /* ---- 1. the view, before paint ---- */
  var asked = (function () { try { return new URLSearchParams(location.search).get('view') } catch (e) { return null } })()
  var view = VIEWS.indexOf(asked) >= 0 ? asked : store.get(KEY)
  if (VIEWS.indexOf(view) < 0) view = VIEWS[0]
  html.setAttribute('data-view', view)
  if (asked === view) store.set(KEY, view)

  function setView(v, why) {
    if (VIEWS.indexOf(v) < 0) return
    html.setAttribute('data-view', v)
    store.set(KEY, v)
    var btns = document.querySelectorAll('.view-btn')
    for (var i = 0; i < btns.length; i++) btns[i].setAttribute('aria-checked', btns[i].getAttribute('data-view') === v ? 'true' : 'false')
    if (why === 'tap') { var sec = document.querySelector('.view[data-view="' + v + '"] h1'); if (sec) sec.setAttribute('tabindex', '-1') }
    try { document.dispatchEvent(new CustomEvent('newsroom:view', { detail: { view: v } })) } catch (e) { /* old browser */ }
  }

  /* ---- the records this browser keeps ---- */
  function cfg() {
    try { var el = document.getElementById('sg-meter-config'); if (el) return JSON.parse(el.textContent) } catch (e) { /* fall through */ }
    return { storageKey: 'sgit.meter.v1', symbol: '£', start: 500 }
  }
  function money(c, p) { var neg = p < -0.004; return (neg ? '−' : '') + (c.symbol || '£') + (Math.abs(p) / 100).toFixed(2) }
  function meterState(c) { return store.json(c.storageKey || 'sgit.meter.v1') }
  function notes() { var s = store.json(NOTES); return s && s.notes && s.notes.length ? s.notes : [] }
  var DECIDED = { 'done': 'done', 'read-later': 'follow-up', 'follow-up': 'follow-up' }
  function decision(ns, path) {
    for (var i = 0; i < ns.length; i++) { var n = ns[i]; if (n.path === path && !n.story && DECIDED[n.kind]) return DECIDED[n.kind] }
    return ''
  }
  function statusOf(s, ns, path) {
    var d = decision(ns, path)
    if (d) return d
    var log = (s && s.log) || [], depth = -1
    for (var i = 0; i < log.length; i++) if (log[i].path === path) depth = Math.max(depth, log[i].depth || 0)
    return depth < 0 ? 'new' : depth >= 0.9 ? 'done' : 'reading'
  }
  var LABEL = { 'new': 'New', 'reading': 'Reading', 'follow-up': 'Follow-up', 'done': 'Done' }

  function data() {
    try { var el = document.getElementById('front-data'); return el ? JSON.parse(el.textContent) : null } catch (e) { return null }
  }
  function activePersona(s, d) {
    if (!s || !d) return d ? d.personas[0] : null
    var ap = null
    for (var i = 0; i < (s.personas || []).length; i++) if (s.personas[i].id === s.active) ap = s.personas[i]
    var pid = ap && ap.preset ? ap.preset : 'newsroom'
    for (var j = 0; j < d.personas.length; j++) if (d.personas[j].id === pid) return d.personas[j]
    return d.personas[0]
  }
  function esc(t) { return String(t).replace(/[&<>"]/g, function (ch) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[ch] }) }

  /* ---- 2. the reader's own numbers ---- */
  function fill() {
    var c = cfg(), s = meterState(c), ns = notes(), d = data()
    var balance = s ? s.balance : c.start, spent = s ? s.spent : 0, reads = s ? (s.reads || (s.log || []).length) : 0
    var all = document.querySelectorAll('[data-you]')
    for (var i = 0; i < all.length; i++) {
      var k = all[i].getAttribute('data-you')
      all[i].textContent = k === 'balance' ? money(c, balance) : k === 'spent' ? money(c, spent) : k === 'reads' ? String(reads) : k === 'notes' ? String(ns.length) : all[i].textContent
    }
    var where = document.querySelector('[data-you-where]')
    if (where) where.textContent = store.get('sgit.vault.last-sync') ? 'in this browser and your vault' : 'in this browser'

    var p = activePersona(s, d)
    var list = document.querySelector('.dk-list')
    if (p && list) {
      var name = document.querySelector('[data-persona-name]')
      if (name) name.textContent = p.neutral ? 'everyone' : p.name
      var who = document.querySelectorAll('.dk-who')
      for (var w = 0; w < who.length; w++) who[w].setAttribute('aria-checked', who[w].getAttribute('data-persona') === p.id ? 'true' : 'false')
      var rows = '', mins = 0
      for (var r = 0; r < p.picks.length; r++) {
        var a = p.picks[r]; mins += a.minutes || 0
        rows += '<li class="dk-row" data-slug="' + esc(a.slug) + '" data-path="' + esc(a.path) + '"><span class="dk-i">' + (r + 1) + '</span>'
          + '<span class="dk-row-main"><a href="' + esc(a.path.replace(/^\//, '')) + '">' + esc(a.head) + '</a>'
          + '<span class="chips"><span class="chip chip-time">' + (a.minutes ? a.minutes + ' min' : '') + '</span><span class="chip chip-format">' + esc(a.format) + '</span></span></span>'
          + '<span class="dk-st st-new" data-status>New</span></li>'
      }
      if (list.getAttribute('data-persona') !== p.id) { list.innerHTML = rows; list.setAttribute('data-persona', p.id) }
      var total = document.querySelector('[data-picks-total]'); if (total) total.textContent = p.picks.length + ' picks · ' + mins + ' min'
    }
    var counts = { 'new': 0, 'reading': 0, 'follow-up': 0, 'done': 0 }, items = document.querySelectorAll('.dk-row')
    for (var j = 0; j < items.length; j++) {
      var st = statusOf(s, ns, items[j].getAttribute('data-path')), tag = items[j].querySelector('[data-status]')
      counts[st]++
      if (tag) { tag.className = 'dk-st st-' + st; tag.textContent = LABEL[st] }
    }
    for (var key in counts) { var b = document.querySelector('[data-count="' + key + '"]'); if (b) b.textContent = String(counts[key]) }
    var done = counts.done, n = items.length, pct = n ? Math.round(100 * done / n) : 0
    var dn = document.querySelector('[data-done]'); if (dn) dn.textContent = String(done)
    var bar = document.querySelector('.dk-progress')
    if (bar) { bar.setAttribute('aria-valuenow', String(done)); bar.setAttribute('aria-valuemax', String(n)); bar.firstElementChild.style.width = pct + '%' }
    var glance = document.querySelector('.view-me')
    if (glance) {
      glance.querySelector('.bar span').style.width = pct + '%'
      glance.querySelector('[data-glance]').innerHTML = '<b>' + done + '/' + n + '</b> read · <b>' + esc(money(c, spent)) + '</b> spent · <b>' + esc(money(c, balance)) + '</b> left'
    }
  }

  function readAs(pid) {
    // the same module instance the balance chip runs on: the URL must match the meter's own import, so it is
    // resolved against the page, not this script (a dynamic import in a classic script resolves relative to the script)
    if (!document.getElementById('sg-meter-config')) return
    var path = new URL('assets/components/sg-meter/v1/v1.4/v1.4.1/sg-meter-core.js', document.baseURI).href
    import(path).then(function (m) {
      if (pid === 'newsroom') m.meter.setActive('me'); else m.meter.visit(pid)
      fill()
    }).catch(function (e) { console.error('[front] could not change persona:', e) })
  }

  document.addEventListener('DOMContentLoaded', function () {
    var btns = document.querySelectorAll('.view-btn'), group = document.querySelector('.view-switch')
    for (var i = 0; i < btns.length; i++) btns[i].addEventListener('click', function (e) { setView(e.currentTarget.getAttribute('data-view'), 'tap') })
    if (group) group.addEventListener('keydown', function (e) {
      var keys = { ArrowLeft: -1, ArrowUp: -1, ArrowRight: 1, ArrowDown: 1, Home: 0, End: 0 }
      if (!(e.key in keys) || !e.target.classList.contains('view-btn')) return
      e.preventDefault()
      var i = VIEWS.indexOf(html.getAttribute('data-view')), next = e.key === 'Home' ? 0 : e.key === 'End' ? VIEWS.length - 1 : (i + keys[e.key] + VIEWS.length) % VIEWS.length
      setView(VIEWS[next], 'tap')
      var b = document.querySelector('.view-btn[data-view="' + VIEWS[next] + '"]'); if (b) b.focus()
    })
    var me = document.querySelector('.view-me')
    if (me) me.addEventListener('click', function () { setView('desk', 'tap'); var h = document.querySelector('.dk-you'); if (h) h.scrollIntoView({ block: 'nearest' }) })
    var who = document.querySelectorAll('.dk-who[data-persona]')
    for (var w = 0; w < who.length; w++) who[w].addEventListener('click', function (e) { e.preventDefault(); readAs(e.currentTarget.getAttribute('data-persona')) })
    fill()
    var again = function () { fill() }
    ;['sg:meter.changed', 'sg:meter.charged', 'sg:meter.rated', 'sg:meter.persona', 'sg:meter.toppedup', 'sg:meter.restored'].forEach(function (ev) { document.addEventListener(ev, again) })
    window.addEventListener('sgit-notes', again)
    window.addEventListener('storage', again)
  })
})()
