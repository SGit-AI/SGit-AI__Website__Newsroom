/* newsroom.sgit.ai: the reading strip, v2 (cards 066, 073). Loaded by the nav on every page that carries the
 * meter (admin/build/chrome.py); runs only where the page's <sg-meter view="page"> has a kind that is charged,
 * which is the imported articles, issues, notes and collections.
 *
 * v1 showed one number, the reader's position on the page, which went down when they scrolled up, and the
 * balance, which the bar already shows. v2 measures two things, section by section, and keeps them:
 *
 *   scrolled  how much of each section has passed through the reading band (the middle 70% of the window),
 *             the deepest point reached; it never goes down.
 *   read      how long each section has been in the reading band while this tab is in front, the window has
 *             focus and the reader did something (scroll, key, pointer, touch) in the last IDLE seconds;
 *             a second in the band is shared between the sections in it by how much of the band each fills.
 *             A section counts as read when its time reaches its words at READ_WPM, the top of the normal
 *             range for silent reading of non-fiction (Brysbaert 2019: average 238, range 175 to 300).
 *
 * Both are word-weighted over the page, so a long section counts for more than a short one. They are kept in
 * this browser under sgit.reading.v1, one record per page: its sections, their words, seconds and how far
 * each was scrolled. Nothing is sent anywhere; the vault does not carry it yet. Two tabs on one page add up:
 * each write re-reads the store and adds only what this tab measured since its last write.
 *
 * The meter is not changed: it still charges by the deepest point scrolled (sg-meter-core.js). The chip shows
 * scrolled, read and what this page has cost; the hairline shows scrolled (pale) and read (solid). A tap on the
 * chip opens the page as the reader's own map: each section, how far scrolled, how long read, and the
 * highlights kept in it (assets/reader/highlights.js). The design and the reasons are the article
 * "Scrolled is not read" (articles/scrolled-is-not-read.html).
 */
(function () {
  'use strict'
  var tag = document.querySelector('sg-meter[view="page"]')
  if (!tag || !tag.getAttribute('kind') || tag.getAttribute('kind') === 'free') return
  var main = document.querySelector('main')
  if (!main) return

  var READ_WPM = 300, IDLE = 60000, TICK = 1000, SAVE = 5000, KEY = 'sgit.reading.v1', MAX_PAGES = 400
  var BAND_TOP = 0.15, BAND_BOTTOM = 0.85
  var cfg = { storageKey: 'sgit.meter.v1', symbol: '£' }
  try { var el = document.getElementById('sg-meter-config'); if (el) cfg = Object.assign(cfg, JSON.parse(el.textContent)) } catch (e) { /* defaults */ }
  var path = location.pathname.replace(/index\.html$/, '') || '/'

  /* ---- the page as sections ---- */
  function words(t) { var m = String(t || '').match(/[A-Za-z0-9£$€%'’-]+/g); return m ? m.length : 0 }
  var stop = main.querySelector(':scope > sg-meter, :scope > section.athreads, :scope > .athreads, :scope > .agent')
  var kids = Array.prototype.slice.call(main.children)
  var end = stop ? kids.indexOf(stop) : kids.length
  var sections = [], cur = { id: 'top', label: 'The opening', nodes: [] }
  for (var i = 0; i < end; i++) {
    var n = kids[i]
    if (n.tagName === 'H2') { if (cur.nodes.length) sections.push(cur); cur = { id: n.id || ('s' + sections.length), label: n.textContent.trim(), nodes: [n] } }
    else if (!/^(SCRIPT|STYLE|SG-METER)$/.test(n.tagName) && !n.classList.contains('crumb')) cur.nodes.push(n)
  }
  if (cur.nodes.length) sections.push(cur)
  sections.forEach(function (s) { s.words = s.nodes.reduce(function (a, n) { return a + words(n.textContent) }, 0); s.ms = 0; s.seen = 0; s.pending = 0 })
  sections = sections.filter(function (s) { return s.words > 0 })
  if (!sections.length) return
  var total = sections.reduce(function (a, s) { return a + s.words }, 0)
  function bounds(s) {
    var a = s.nodes[0].getBoundingClientRect(), b = s.nodes[s.nodes.length - 1].getBoundingClientRect()
    return { top: a.top, bottom: Math.max(a.bottom, b.bottom) }
  }
  function need(s) { return s.words / READ_WPM * 60000 }

  /* ---- the store ---- */
  function readStore() { try { var s = JSON.parse(localStorage.getItem(KEY) || 'null'); if (s && s.pages) return s } catch (e) { /* fall through */ } return { v: 1, pages: {} } }
  var stored = readStore().pages[path]
  if (stored && stored.sections) stored.sections.forEach(function (r) { sections.forEach(function (s) { if (s.id === r.id) { s.ms = r.ms || 0; s.seen = r.seen || 0 } }) })
  var visit = true
  function save() {
    var st = readStore(), now = new Date().toISOString()
    var rec = st.pages[path] || { title: document.title.replace(/ ?[,·|] ?SGit Newsroom.*$/, ''), first: now, visits: 0, sections: [] }
    if (visit) { rec.visits = (rec.visits || 0) + 1; visit = false }
    var by = {}; (rec.sections || []).forEach(function (r) { by[r.id] = r })
    rec.sections = sections.map(function (s) {
      var r = by[s.id] || { id: s.id, ms: 0, seen: 0 }
      r.label = s.label; r.words = s.words; r.ms = Math.round((r.ms || 0) + s.pending); r.seen = Math.max(r.seen || 0, Math.round(s.seen * 100) / 100)
      s.pending = 0; s.ms = r.ms; s.seen = r.seen
      return r
    })
    rec.words = total; rec.last = now; rec.scrolled = scrolled(); rec.read = read()
    st.pages[path] = rec
    var keys = Object.keys(st.pages)
    if (keys.length > MAX_PAGES) keys.sort(function (a, b) { return String(st.pages[a].last).localeCompare(String(st.pages[b].last)) }).slice(0, keys.length - MAX_PAGES).forEach(function (k) { delete st.pages[k] })
    try { localStorage.setItem(KEY, JSON.stringify(st)) } catch (e) { /* private window: this visit only */ }
    try { window.dispatchEvent(new CustomEvent('sgit-reading', { detail: { path: path, scrolled: rec.scrolled, read: rec.read } })) } catch (e) { /* old browser */ }
  }

  /* ---- the two measures ---- */
  function scrolled() { return sections.reduce(function (a, s) { return a + s.words * s.seen }, 0) / total }
  function read() { return sections.reduce(function (a, s) { return a + s.words * Math.min(1, (s.ms + s.pending) / need(s)) }, 0) / total }
  var lastActive = Date.now()
  ;['scroll', 'keydown', 'pointermove', 'pointerdown', 'wheel', 'touchstart'].forEach(function (ev) { window.addEventListener(ev, function () { lastActive = Date.now() }, { passive: true }) })
  function attended() { return document.visibilityState === 'visible' && document.hasFocus() && Date.now() - lastActive < IDLE }
  function measure(dt) {
    // at the foot of the page the last sections can never rise into the band, so there the band is the whole window
    var vh = window.innerHeight, foot = window.scrollY + vh >= document.documentElement.scrollHeight - 4
    var top = foot ? 0 : vh * BAND_TOP, bottom = foot ? vh : vh * BAND_BOTTOM, band = bottom - top, shares = [], sum = 0
    sections.forEach(function (s) {
      var b = bounds(s), h = Math.max(1, b.bottom - b.top)
      s.seen = Math.max(s.seen, Math.min(1, Math.max(0, (bottom - b.top) / h)))
      var o = Math.max(0, Math.min(bottom, b.bottom) - Math.max(top, b.top))
      shares.push(o); sum += o
    })
    if (dt && sum > 0) sections.forEach(function (s, k) { s.pending += dt * shares[k] / Math.max(sum, band * 0.25) })
  }

  /* ---- what the reader sees ---- */
  var strip = document.createElement('div'); strip.className = 'read-strip'; strip.setAttribute('aria-hidden', 'true')
  strip.innerHTML = '<i class="rs-scrolled"></i><i class="rs-read"></i>'
  var chip = document.createElement('button'); chip.type = 'button'; chip.className = 'read-chip'; chip.setAttribute('aria-expanded', 'false')
  chip.title = 'How much of this page you scrolled and read, and what it cost. Kept in this browser.'
  chip.innerHTML = '<span class="rc-k">Scrolled</span><b class="rc-v" data-k="scrolled">0%</b><span class="rc-k">Read</span><b class="rc-v" data-k="read">0%</b><b class="rc-v rc-cost" data-k="cost">£0.00</b>'
  var panel = document.createElement('div'); panel.className = 'read-map'; panel.hidden = true; panel.setAttribute('role', 'dialog'); panel.setAttribute('aria-label', 'This page, as you read it')
  document.body.appendChild(strip); document.body.appendChild(chip); document.body.appendChild(panel)
  var bars = strip.children, shown = {}
  function money(p) { return (p < -0.004 ? '−' : '') + cfg.symbol + (Math.abs(p) / 100).toFixed(2) }
  function cost() {
    var s = null; try { s = JSON.parse(localStorage.getItem(cfg.storageKey) || 'null') } catch (e) { /* none */ }
    var c = 0; ((s && s.log) || []).forEach(function (e) { if (e.path === path) c += e.cost || 0 })
    return money(c)
  }
  function set(k, v) { if (shown[k] !== v) { shown[k] = v; chip.querySelector('[data-k="' + k + '"]').textContent = v } }
  function paint() {
    var sc = Math.round(scrolled() * 100), rd = Math.round(read() * 100)
    set('scrolled', sc + '%'); set('read', rd + '%'); set('cost', cost())
    if (shown.w1 !== sc) { shown.w1 = sc; bars[0].style.width = sc + '%' }
    if (shown.w2 !== rd) { shown.w2 = rd; bars[1].style.width = rd + '%' }
    if (!panel.hidden) drawMap()
  }
  function mmss(ms) { var s = Math.round(ms / 1000); return Math.floor(s / 60) + ':' + ('0' + s % 60).slice(-2) }
  function esc(t) { return String(t).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c] }) }
  function drawMap() {
    var hl = {}; try { (window.SgitHighlights ? window.SgitHighlights.forPage() : []).forEach(function (h) { hl[h.section] = (hl[h.section] || 0) + 1 }) } catch (e) { /* none */ }
    var rows = sections.map(function (s) {
      var sc = Math.round(s.seen * 100), rd = Math.round(Math.min(1, (s.ms + s.pending) / need(s)) * 100)
      return '<li><a href="#' + esc(s.id) + '" data-to="' + esc(s.id) + '"><span class="rm-l">' + esc(s.label) + '</span>'
        + '<span class="rm-bar" aria-hidden="true"><i style="width:' + sc + '%"></i><i style="width:' + rd + '%"></i></span>'
        + '<span class="rm-n">' + rd + '% read · ' + mmss(s.ms + s.pending) + ' of ' + mmss(need(s)) + (hl[s.id] ? ' · ' + hl[s.id] + ' highlight' + (hl[s.id] === 1 ? '' : 's') : '') + '</span></a></li>'
    }).join('')
    panel.innerHTML = '<div class="rm-h"><b>This page, as you read it</b><button type="button" class="rm-x" aria-label="Close">×</button></div>'
      + '<p class="rm-sum"><b>' + Math.round(scrolled() * 100) + '%</b> scrolled · <b>' + Math.round(read() * 100) + '%</b> read · ' + total.toLocaleString('en-GB') + ' words in ' + sections.length + ' sections · ' + cost() + ' charged</p>'
      + '<ol class="rm-list">' + rows + '</ol>'
      + '<p class="rm-note">Pale: scrolled past. Solid: time in view while this tab was in front and you were active, counted against ' + READ_WPM + ' words a minute. The meter still charges by how far you scrolled. Kept in this browser only.</p>'
    panel.querySelector('.rm-x').onclick = close
  }
  function open() { panel.hidden = false; chip.setAttribute('aria-expanded', 'true'); drawMap() }
  function close() { panel.hidden = true; chip.setAttribute('aria-expanded', 'false') }
  chip.addEventListener('click', function () { panel.hidden ? open() : close() })
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !panel.hidden) { close(); chip.focus() } })

  /* ---- the clock ---- */
  var last = Date.now(), dirty = 0
  function tick() {
    var now = Date.now(), dt = Math.min(now - last, 2 * TICK); last = now
    var on = attended()
    measure(on ? dt : 0)
    if (on) dirty += dt
    paint()
  }
  var ticking = false
  window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(function () { ticking = false; measure(0); paint() }) } }, { passive: true })
  setInterval(tick, TICK)
  setInterval(function () { if (dirty) { dirty = 0; save() } }, SAVE)
  function flush() { tick(); save() }
  document.addEventListener('visibilitychange', function () { if (document.visibilityState === 'hidden') flush(); else last = Date.now() })
  window.addEventListener('pagehide', flush)
  ;['sg:meter.charged', 'sg:meter.rated', 'sg:meter.declined', 'sg:meter.changed'].forEach(function (ev) { document.addEventListener(ev, function () { set('cost', cost()) }) })
  window.addEventListener('sgit-highlights', function () { if (!panel.hidden) drawMap() })
  window.SgitReading = { sections: function () { return sections.map(function (s) { return { id: s.id, label: s.label, words: s.words, ms: s.ms + s.pending, seen: s.seen } }) }, scrolled: scrolled, read: read, save: save, sectionOf: function (node) {
    for (var k = 0; k < sections.length; k++) for (var j = 0; j < sections[k].nodes.length; j++) if (sections[k].nodes[j].contains(node)) return sections[k].id
    return ''
  } }
  measure(0); save(); paint()
})()
