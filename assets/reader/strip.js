/* newsroom.sgit.ai: the reading strip, v4 (cards 066, 073, 081, 084). Loaded by the nav on every page that carries the
 * meter (admin/build/chrome.py); runs only where the page's <sg-meter view="page"> has a kind that is charged,
 * which is the imported articles, issues, notes and collections.
 *
 * It measures two things, section by section, and keeps them in this browser (sgit.reading.v1):
 *
 *   scrolled  how much of each section has passed through the reading band (the middle 70% of the window),
 *             the deepest point reached; it never goes down on its own.
 *   read      how long each section has been in the reading band while this tab is in front, the window has
 *             focus and the reader did something (scroll, key, pointer, touch) in the last IDLE seconds;
 *             a second in the band is shared between the sections in it by how much of the band each fills.
 *             A section counts as read when its time reaches its words at READ_WPM, the top of the normal
 *             range for silent reading of non-fiction (Brysbaert 2019: average 238, range 175 to 300).
 *             v4 adds a second way to read (card 084): PACE. The text that passes the reading line while the
 *             reader scrolls counts as read when it passes no faster than PACE_WPM words a minute; a reader who
 *             scrolls slowly through an article, either way, has read it. The reading line runs from the top of
 *             the page when scrolled to the top to its foot when scrolled to the foot, so a slow scroll from top
 *             to bottom passes every word. The pace is held by a budget: words are earned at PACE_WPM while the
 *             reader is attended (as above), up to PACE_CAP (about eight seconds of it: reading a screen and then
 *             scrolling is the time measure's; this one is for the steady scroll), and spent as text passes the
 *             line. A movement that
 *             passes more text than the budget holds is faster than reading: none of it counts and the budget is
 *             spent, so a fast scroll counts nothing, not a share. A jump of more than a window (a link, a key)
 *             counts nothing either. A section's read is the larger of its time and its pace, never the sum.
 *
 * Both are word-weighted over the page. Two tabs on one page add up: each write re-reads the store and adds only
 * what this tab measured since its last write.
 *
 * v3 puts the reader in control (card 081): PAUSE stops all measuring, on every page, until resumed (it is kept
 * under sgit.reading.paused, so a reload or another article stays paused); RESET sets the page back to unread;
 * each section can be MARKED read or unread by hand. The numbers are the reader's, so the reader can correct
 * them. Since v0.12.99 the meter charges by the share read (sg-meter v1.5.0), from the sgit-reading event this
 * dispatches on every save: a reset is sent with reset:true, and the meter refunds the page down to its minimum.
 *
 * The chip shows scrolled, read and what this page cost, and a mark that says whether it is measuring (a dot)
 * or paused (two bars). A tap opens the page as the reader's own map: each section, how far scrolled, how long
 * read, the highlights in it, a control to mark it, and the controls for the page. How what was read is shown
 * on the page itself (a line in the margin, faded, folded to a paragraph or a line, or hidden) is folds.js.
 * The design and the reasons: the articles "Scrolled is not read" and "Your reading, your controls".
 */
(function () {
  'use strict'
  var tag = document.querySelector('sg-meter[view="page"]')
  if (!tag || !tag.getAttribute('kind') || tag.getAttribute('kind') === 'free') return
  var main = document.querySelector('main')
  if (!main) return

  var READ_WPM = 300, PACE_WPM = 450, PACE_CAP = 60, IDLE = 60000, TICK = 1000, SAVE = 5000, KEY = 'sgit.reading.v1', PAUSE_KEY = 'sgit.reading.paused', MAX_PAGES = 400
  var BAND_TOP = 0.15, BAND_BOTTOM = 0.85
  var cfg = { storageKey: 'sgit.meter.v1', symbol: '£' }
  try { var el = document.getElementById('sg-meter-config'); if (el) cfg = Object.assign(cfg, JSON.parse(el.textContent)) } catch (e) { /* defaults */ }
  var path = location.pathname.replace(/index\.html$/, '') || '/'
  var ls = {
    get: function (k) { try { return localStorage.getItem(k) } catch (e) { return null } },
    set: function (k, v) { try { if (v == null) localStorage.removeItem(k); else localStorage.setItem(k, v) } catch (e) { /* private window */ } }
  }

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
  sections.forEach(function (s) { s.words = s.nodes.reduce(function (a, n) { return a + words(n.textContent) }, 0); s.ms = 0; s.seen = 0; s.pending = 0; s.paced = 0; s.mark = '' })
  sections = sections.filter(function (s) { return s.words > 0 })
  if (!sections.length) return
  var total = sections.reduce(function (a, s) { return a + s.words }, 0)
  function bounds(s) {
    var shown = s.nodes.filter(function (n) { return n.offsetParent !== null || n.getClientRects().length })
    if (!shown.length) return null
    var a = shown[0].getBoundingClientRect(), b = shown[shown.length - 1].getBoundingClientRect()
    return { top: a.top, bottom: Math.max(a.bottom, b.bottom) }
  }
  function need(s) { return s.words / READ_WPM * 60000 }
  function readOf(s) { return Math.min(1, Math.max((s.ms + s.pending) / need(s), s.paced / s.words)) }

  /* ---- the store ---- */
  function readStore() { try { var s = JSON.parse(ls.get(KEY) || 'null'); if (s && s.pages) return s } catch (e) { /* fall through */ } return { v: 1, pages: {} } }
  var stored = readStore().pages[path]
  if (stored && stored.sections) stored.sections.forEach(function (r) { sections.forEach(function (s) { if (s.id === r.id) { s.ms = r.ms || 0; s.seen = r.seen || 0; s.paced = Math.min(s.words, r.pw || 0); s.mark = r.mark || '' } }) })
  var returning = !!(stored && stored.sections && stored.sections.some(function (r) { return (r.ms || 0) > 0 || (r.pw || 0) > 0 || r.mark }))
  var visit = true
  // write the page's record: by default adding what this tab measured; `absolute` sets sections outright (a reset, a mark)
  function save(absolute, extra) {
    var st = readStore(), now = new Date().toISOString()
    var rec = st.pages[path] || { title: document.title.replace(/ ?[,·|] ?SGit Newsroom.*$/, ''), first: now, visits: 0, sections: [] }
    if (visit) { rec.visits = (rec.visits || 0) + 1; visit = false }
    var by = {}; (rec.sections || []).forEach(function (r) { by[r.id] = r })
    rec.sections = sections.map(function (s) {
      var r = by[s.id] || { id: s.id, ms: 0, seen: 0 }
      r.label = s.label; r.words = s.words
      if (absolute && absolute[s.id]) { var a = absolute[s.id]; r.ms = Math.round(a.ms); r.seen = a.seen; r.pw = a.pw || 0; if (a.mark) { r.mark = a.mark; r.marked = now } else { delete r.mark; delete r.marked } }
      else { r.ms = Math.round((r.ms || 0) + s.pending); r.seen = Math.max(r.seen || 0, Math.round(s.seen * 100) / 100); r.pw = Math.min(s.words, Math.max(r.pw || 0, Math.round(s.paced))) }
      if (!r.pw) delete r.pw
      s.pending = 0; s.ms = r.ms; s.seen = r.seen; s.paced = r.pw || 0; s.mark = r.mark || ''
      return r
    })
    rec.words = total; rec.last = now; rec.scrolled = scrolled(); rec.read = read()
    st.pages[path] = rec
    var keys = Object.keys(st.pages)
    if (keys.length > MAX_PAGES) keys.sort(function (a, b) { return String(st.pages[a].last).localeCompare(String(st.pages[b].last)) }).slice(0, keys.length - MAX_PAGES).forEach(function (k) { delete st.pages[k] })
    ls.set(KEY, JSON.stringify(st))
    try { window.dispatchEvent(new CustomEvent('sgit-reading', { detail: Object.assign({ path: path, scrolled: rec.scrolled, read: rec.read }, extra || {}) })) } catch (e) { /* old browser */ }
  }

  /* ---- the two measures ---- */
  function scrolled() { return sections.reduce(function (a, s) { return a + s.words * s.seen }, 0) / total }
  function read() { return sections.reduce(function (a, s) { return a + s.words * readOf(s) }, 0) / total }
  var lastActive = Date.now()
  ;['scroll', 'keydown', 'pointermove', 'pointerdown', 'wheel', 'touchstart'].forEach(function (ev) { window.addEventListener(ev, function () { lastActive = Date.now() }, { passive: true }) })
  function paused() { return ls.get(PAUSE_KEY) === '1' }
  function attended() { return !paused() && document.visibilityState === 'visible' && document.hasFocus() && Date.now() - lastActive < IDLE }
  function measure(dt) {
    if (paused()) return
    // at the foot of the page the last sections can never rise into the band, so there the band is the whole window
    var vh = window.innerHeight, foot = window.scrollY + vh >= document.documentElement.scrollHeight - 4
    var top = foot ? 0 : vh * BAND_TOP, bottom = foot ? vh : vh * BAND_BOTTOM, band = bottom - top, shares = [], sum = 0
    sections.forEach(function (s) {
      var b = s.folded ? null : bounds(s)
      if (!b) { shares.push(0); return }
      var h = Math.max(1, b.bottom - b.top)
      s.seen = Math.max(s.seen, Math.min(1, Math.max(0, (bottom - b.top) / h)))
      var o = Math.max(0, Math.min(bottom, b.bottom) - Math.max(top, b.top))
      shares.push(o); sum += o
    })
    if (dt && sum > 0) sections.forEach(function (s, k) { s.pending += dt * shares[k] / Math.max(sum, band * 0.25) })
  }
  // the reading line, in page coordinates, and the text that passed it since the last look
  var budget = 0, lastLine = null, lastH = 0
  function pace() {
    var vh = window.innerHeight, H = document.documentElement.scrollHeight, y = window.scrollY
    var at = y + vh * Math.min(1, Math.max(0, y / Math.max(1, H - vh)))
    var from = lastLine; lastLine = at
    if (from == null || H !== lastH || paused()) { lastH = H; return }    // the page changed height (an image, a fold): start again from here
    var a = Math.min(from, at), b = Math.max(from, at)
    if (b - a < 1 || b - a > vh) return                                 // nothing passed, or a jump
    var passed = [], words = 0
    sections.forEach(function (s) {
      if (s.folded) return
      var r = bounds(s); if (!r) return
      var top = r.top + y, h = Math.max(1, r.bottom - r.top), o = Math.min(b, top + h) - Math.max(a, top)
      if (o > 0) { passed.push([s, o / h * s.words]); words += o / h * s.words }
    })
    // faster than the pace: none of it counts, and the budget is spent
    if (words > budget) { budget = 0; return }
    budget -= words
    // a section passed at a reading pace all but its last few words (the line meets its edges at an angle) is passed
    passed.forEach(function (x) { var s = x[0]; if (s.paced < s.words) { s.paced = Math.min(s.words, s.paced + x[1]); if (s.paced >= s.words * 0.95) s.paced = s.words; dirty += 1 } })
  }

  /* ---- the reader's controls ---- */
  function setPaused(on) { ls.set(PAUSE_KEY, on ? '1' : null); last = Date.now(); budget = 0; lastLine = null; paint(true); emitChange({ pause: true }) }
  function resetPage() {
    var abs = {}; sections.forEach(function (s) { s.pending = 0; abs[s.id] = { ms: 0, seen: 0, pw: 0 } })
    save(abs, { reset: true }); paint(true); emitChange()
  }
  function markSection(id, how) {
    var abs = {}
    sections.forEach(function (s) {
      if (s.id !== id) return
      s.pending = 0
      abs[s.id] = how === 'read' ? { ms: Math.ceil(need(s)), seen: 1, pw: s.words, mark: 'read' } : { ms: 0, seen: s.seen, pw: 0, mark: 'unread' }
    })
    save(abs); paint(true); emitChange()
  }
  function emitChange(more) { try { window.dispatchEvent(new CustomEvent('sgit-reading-change', { detail: Object.assign({ path: path }, more || {}) })) } catch (e) { /* old browser */ } }

  /* ---- what the reader sees ---- */
  var strip = document.createElement('div'); strip.className = 'read-strip'; strip.setAttribute('aria-hidden', 'true')
  strip.innerHTML = '<i class="rs-scrolled"></i><i class="rs-read"></i>'
  var chip = document.createElement('button'); chip.type = 'button'; chip.className = 'read-chip'; chip.setAttribute('aria-expanded', 'false')
  chip.title = 'How much of this page you scrolled and read, and what it cost. Kept in this browser. Tap for the controls.'
  chip.innerHTML = '<b class="rc-s" data-k="state" aria-hidden="true"></b><span class="rc-k">Scrolled</span><b class="rc-v" data-k="scrolled">0%</b><span class="rc-k">Read</span><b class="rc-v" data-k="read">0%</b><b class="rc-v rc-cost" data-k="cost">£0.00</b>'
  var panel = document.createElement('div'); panel.className = 'read-map'; panel.hidden = true; panel.setAttribute('role', 'dialog'); panel.setAttribute('aria-label', 'This page, as you read it')
  document.body.appendChild(strip); document.body.appendChild(chip); document.body.appendChild(panel)
  var bars = strip.children, shown = {}
  function money(p) { return (p < -0.004 ? '−' : '') + cfg.symbol + (Math.abs(p) / 100).toFixed(2) }
  function cost() {
    var s = null; try { s = JSON.parse(ls.get(cfg.storageKey) || 'null') } catch (e) { /* none */ }
    var c = 0; ((s && s.log) || []).forEach(function (e) { if (e.path === path) c += e.cost || 0 })
    return money(c)
  }
  function set(k, v) { if (shown[k] !== v) { shown[k] = v; chip.querySelector('[data-k="' + k + '"]').textContent = v } }
  function paint(force) {
    var sc = Math.round(scrolled() * 100), rd = Math.round(read() * 100), p = paused()
    var done = rd >= 100
    set('scrolled', sc + '%'); set('read', rd + '%'); set('cost', cost()); set('state', p ? '‖' : done ? '✓' : '●')
    if (shown.p !== p || shown.done !== done) { shown.p = p; shown.done = done; chip.classList.toggle('is-paused', p); chip.classList.toggle('is-done', done && !p); chip.setAttribute('aria-label', (p ? 'Measuring paused. ' : done ? 'Read in full. ' : '') + 'Scrolled ' + sc + '%, read ' + rd + '%') }
    if (shown.w1 !== sc) { shown.w1 = sc; bars[0].style.width = sc + '%' }
    if (shown.w2 !== rd) { shown.w2 = rd; bars[1].style.width = rd + '%' }
    if (!panel.hidden && (force || !panel.contains(document.activeElement))) drawMap()
  }
  function mmss(ms) { var s = Math.round(ms / 1000); return Math.floor(s / 60) + ':' + ('0' + s % 60).slice(-2) }
  function esc(t) { return String(t).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c] }) }
  function stateOf(s) { var r = readOf(s); return r >= 0.9 ? 'read' : r >= 0.3 ? 'part' : s.seen >= 0.5 ? 'skimmed' : 'unread' }
  // the Settings tab: how what was read is shown (folds.js), for every article and for this one, and measuring
  function settings() {
    var F = window.SgitFolds, p = paused()
    var out = '<div class="rm-set">'
    if (F) {
      var all = F.allMode(), mine = F.pageMode(), name = {}
      F.views.forEach(function (v) { name[v[0]] = v[1] })
      out += '<h3 class="rm-k">Show what you have read, on every article</h3>'
        + '<div class="rv-list" role="radiogroup" aria-label="Show what you have read, on every article">' + F.views.map(function (v) {
          return '<button type="button" role="radio" class="rv-opt" data-view="' + v[0] + '" data-scope="all" aria-checked="' + (v[0] === all) + '"><b>' + esc(v[1]) + '</b><span>' + esc(v[2]) + '</span></button>'
        }).join('') + '</div>'
        + '<h3 class="rm-k">On this article</h3>'
        + '<div class="rv-pick" role="radiogroup" aria-label="Show what you have read, on this article">'
        + '<button type="button" role="radio" data-view="" data-scope="page" aria-checked="' + !mine + '">As every article (' + esc(name[all]) + ')</button>'
        + F.views.map(function (v) { return '<button type="button" role="radio" data-view="' + v[0] + '" data-scope="page" aria-checked="' + (v[0] === mine) + '">' + esc(v[1]) + '</button>' }).join('')
        + '</div>'
    }
    out += '<h3 class="rm-k">Measuring</h3>'
      + '<div class="rm-ctl"><button type="button" class="rm-btn" data-act="pause" aria-pressed="' + p + '">' + (p ? 'Resume measuring' : 'Pause measuring') + '</button></div>'
      + '<p class="rm-note">A section counts as read by the time it was in view while this tab was in front and you were active, against ' + READ_WPM + ' words a minute, or by scrolling past it no faster than ' + PACE_WPM + ' words a minute, whichever is more. Pause holds on every page until you resume. All of it is kept in this browser only; these settings too.</p>'
    return out + '</div>'
  }
  var tab = 'sections'
  function drawMap() {
    var hl = {}; try { (window.SgitHighlights ? window.SgitHighlights.forPage() : []).forEach(function (h) { hl[h.section] = (hl[h.section] || 0) + 1 }) } catch (e) { /* none */ }
    var p = paused()
    var rows = sections.map(function (s) {
      var sc = Math.round(s.seen * 100), rd = Math.round(readOf(s) * 100), st = stateOf(s)
      return '<li class="rm-' + st + '"><div class="rm-row"><a href="#' + esc(s.id) + '" data-to="' + esc(s.id) + '"><span class="rm-l">' + esc(s.label) + '</span>'
        + '<span class="rm-bar" aria-hidden="true"><i style="width:' + sc + '%"></i><i style="width:' + rd + '%"></i></span>'
        + '<span class="rm-n">' + rd + '% read · ' + mmss(s.ms + s.pending) + ' of ' + mmss(need(s)) + (s.paced / s.words > (s.ms + s.pending) / need(s) + 0.01 ? ' · by pace' : '') + (s.mark ? ' · marked ' + s.mark + ' by you' : '') + (hl[s.id] ? ' · ' + hl[s.id] + ' highlight' + (hl[s.id] === 1 ? '' : 's') : '') + '</span></a>'
        + (st === 'read' ? '<button type="button" class="rm-mark" data-mark="unread" data-id="' + esc(s.id) + '" title="Mark this section unread: its time goes back to zero">Unread</button>'
                         : '<button type="button" class="rm-mark" data-mark="read" data-id="' + esc(s.id) + '" title="Mark this section read">Read</button>')
        + '</div></li>'
    }).join('')
    var head = '<div class="rm-h"><div class="rm-tabs" role="tablist" aria-label="The reading panel">'
      + '<button type="button" role="tab" data-tab="sections" aria-selected="' + (tab === 'sections') + '">This page</button>'
      + '<button type="button" role="tab" data-tab="settings" aria-selected="' + (tab === 'settings') + '">Settings</button>'
      + '</div><button type="button" class="rm-x" aria-label="Close">×</button></div>'
    if (tab === 'settings') { panel.innerHTML = head + settings(); return }
    panel.innerHTML = head
      + '<div class="rm-ctl"><button type="button" class="rm-btn" data-act="pause" aria-pressed="' + p + '">' + (p ? 'Resume measuring' : 'Pause measuring') + '</button>'
      + '<button type="button" class="rm-btn" data-act="reset" title="Set every section of this page back to unread">Reset this page</button></div>'
      + (p ? '<p class="rm-paused">Paused on every page until you resume. Nothing is measured, so nothing more is charged.</p>' : '')
      + '<p class="rm-sum"><b>' + Math.round(scrolled() * 100) + '%</b> scrolled · <b>' + Math.round(read() * 100) + '%</b> read · ' + total.toLocaleString('en-GB') + ' words in ' + sections.length + ' sections · ' + cost() + ' charged</p>'
      + '<ol class="rm-list">' + rows + '</ol>'
      + '<p class="rm-note">Pale: scrolled past. Solid: read, by time in view or by scrolling past at a reading pace (Settings says how). The meter charges for the share you read, and a reset refunds it down to the minimum. Kept in this browser only.</p>'
  }
  panel.addEventListener('click', function (e) {
    var t = e.target.closest('button')
    if (!t) return
    if (t.classList.contains('rm-x')) return close()
    if (t.dataset.act === 'pause') return setPaused(!paused())
    if (t.dataset.act === 'reset') return resetPage()
    if (t.dataset.mark) return markSection(t.dataset.id, t.dataset.mark)
    if (t.dataset.tab) { tab = t.dataset.tab; drawMap(); var f = panel.querySelector('[data-tab="' + tab + '"]'); if (f) f.focus(); return }
    if (t.dataset.scope && window.SgitFolds) { window.SgitFolds.setMode(t.dataset.view, t.dataset.scope); drawMap(); var g = panel.querySelector('[data-scope="' + t.dataset.scope + '"][data-view="' + t.dataset.view + '"]'); if (g) g.focus() }
  })
  function open(t) { if (t === 'settings' || t === 'sections') tab = t; panel.hidden = false; chip.setAttribute('aria-expanded', 'true'); drawMap() }
  function close() { panel.hidden = true; chip.setAttribute('aria-expanded', 'false') }
  chip.addEventListener('click', function () { panel.hidden ? open() : close() })
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !panel.hidden) { close(); chip.focus() } })

  /* ---- the clock ---- */
  var last = Date.now(), dirty = 0
  function tick() {
    var now = Date.now(), dt = Math.min(now - last, 2 * TICK); last = now
    var on = attended()
    measure(on ? dt : 0)
    if (on) { dirty += dt; budget = Math.min(PACE_CAP, budget + dt / 60000 * PACE_WPM) }
    if (on) pace(); else lastLine = null
    paint()
  }
  var ticking = false
  window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(function () { ticking = false; measure(0); if (attended()) pace(); else lastLine = null; paint() }) } }, { passive: true })
  setInterval(tick, TICK)
  setInterval(function () { if (dirty) { dirty = 0; save() } }, SAVE)
  function flush() { tick(); save() }
  document.addEventListener('visibilitychange', function () { if (document.visibilityState === 'hidden') flush(); else last = Date.now() })
  window.addEventListener('pagehide', flush)
  window.addEventListener('storage', function (e) { if (e.key === PAUSE_KEY) paint(true) })
  ;['sg:meter.charged', 'sg:meter.rated', 'sg:meter.declined', 'sg:meter.changed'].forEach(function (ev) { document.addEventListener(ev, function () { set('cost', cost()) }) })
  window.addEventListener('sgit-highlights', function () { if (!panel.hidden) drawMap() })
  window.addEventListener('sgit-folds', function () { if (!panel.hidden) drawMap() })
  window.SgitReading = {
    path: path, returning: returning, need: function (id) { var s = find(id); return s ? need(s) : 0 },
    sections: function () { return sections.map(function (s) { return { id: s.id, label: s.label, words: s.words, ms: Math.round(s.ms + s.pending), paced: Math.round(s.paced), seen: s.seen, read: readOf(s), state: stateOf(s), mark: s.mark, nodes: s.nodes } }) },
    scrolled: scrolled, read: read, save: save, paused: paused, setPaused: setPaused, reset: resetPage, mark: markSection, open: open,
    paced: function (id) { var s = find(id); return s ? s.paced : 0 },
    fold: function (id, on) { var s = find(id); if (s) s.folded = !!on },
    sectionOf: function (node) {
      for (var k = 0; k < sections.length; k++) for (var j = 0; j < sections[k].nodes.length; j++) if (sections[k].nodes[j].contains(node)) return sections[k].id
      return ''
    }
  }
  function find(id) { for (var k = 0; k < sections.length; k++) if (sections[k].id === id) return sections[k]; return null }
  measure(0); save(); paint()
})()
