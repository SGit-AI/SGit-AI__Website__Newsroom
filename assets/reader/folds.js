/* newsroom.sgit.ai: showing what has been read (cards 082, 084). Loaded by the nav after the reading strip
 * (assets/reader/strip.js), on every page it runs on; uses window.SgitReading.
 *
 * Six ways to show, on the page itself, the sections the reader has already read. The choice is a setting: one for
 * every article (sgit.reading.view), and any article can have its own (sgit.reading.views, by path). Both are set
 * in the Settings tab of the reading chip's panel and kept in this browser; ?fold=<view> tries one for a visit.
 *
 *   full       nothing changes
 *   margin     a line beside each section the reader has reached, from a pale tint when started to the solid accent
 *              when read, changing smoothly as they read; a tick when a section is read in full (the default)
 *   fade       read sections are faded; hover or focus brings them back
 *   para       a read section is folded to its heading and a paragraph of what it said
 *   line       a read section is folded to one line: its heading and about eight words
 *   hide       read sections are hidden; consecutive ones collapse into one marker that says how many and opens them
 *
 * Every folded section has Show, which opens it where it is. The paragraph and the line are the article's own
 * section summaries (articles/summaries/<slug>.json, admin/build/summaries.py), written with the article.
 *
 * LIVE. The margin is the only view that changes while the reader reads: a colour, never a size, so nothing moves.
 *
 * PASSES. The other five change the page only in a pass: when the reader comes back to an article they had read
 * some of, when they scroll back up by more than half a window (after going down at least a window the first
 * time), or when they ask (a view chosen, Show, a mark, a reset). Reading forward never starts one. A pass started
 * by scrolling leaves the sections on screen as they are; one on arriving changes them all, before reading starts. Only a section read in full is faded or folded, so a
 * section the reader is part way through is never faded under their eyes.
 *
 * STILLNESS. A pass that changes the height of the page waits until the page is still: no scroll, wheel or touch
 * for STILL ms and no finger down, because a scroll still in motion (a smooth wheel, a trackpad, a phone's
 * momentum) runs towards a position fixed when it started and a correction under it fights it. When still, which
 * sections are on screen is decided first, for all of them; then the first element on screen is noted, the change
 * made, and the scroll corrected by what that element moved, with the browser's own scroll anchoring off for that
 * frame so the two corrections do not add up. Before card 084 the sections on screen were asked one at a time,
 * while the ones above were already folding: the one in view moved up, was folded too, and took the words the
 * reader was on with it, thousands of pixels in one frame. Nothing is sent anywhere.
 */
(function () {
  'use strict'
  var R = window.SgitReading
  if (!R) return
  var main = document.querySelector('main')
  var KEY = 'sgit.reading.view', PAGES_KEY = 'sgit.reading.views', MAX_PAGES = 400, STILL = 700
  var VIEWS = [
    ['full', 'Full', 'Nothing changes: the page stays as it was written.'],
    ['margin', 'Margin line', 'A line beside each section you reach, pale when you start it and solid when you have read it, with a tick. It changes as you read; nothing moves.'],
    ['fade', 'Faded', 'Sections you have read in full are faded when you come back to them or scroll back up. Never the one you are reading.'],
    ['para', 'Paragraph', 'Sections you have read fold to their heading and a short paragraph of what they said, when you come back or scroll back up.'],
    ['line', 'Line', 'Sections you have read fold to their heading and one line.'],
    ['hide', 'Hidden', 'Sections you have read are hidden, with one marker for each run of them that opens them again.']
  ]
  var MODES = VIEWS.map(function (v) { return v[0] })
  var ls = {
    get: function (k) { try { return localStorage.getItem(k) } catch (e) { return null } },
    set: function (k, v) { try { if (v == null) localStorage.removeItem(k); else localStorage.setItem(k, v) } catch (e) { /* private window */ } }
  }
  function valid(m) { return MODES.indexOf(m) >= 0 ? m : '' }
  function pages() { try { var p = JSON.parse(ls.get(PAGES_KEY) || '{}'); return p && typeof p === 'object' ? p : {} } catch (e) { return {} } }
  var asked = valid((function () { try { return new URLSearchParams(location.search).get('fold') } catch (e) { return null } })())
  var allMode = valid(ls.get(KEY)) || 'margin', pageMode = valid(pages()[R.path])
  var mode = asked || pageMode || allMode
  var active = false, maxY = 0, opened = {}, summaries = null, applied = {}, want = null

  /* ---- the summaries ---- */
  var slug = (location.pathname.match(/\/articles\/([^/]+)\.html$/) || [])[1]
  if (slug) fetch('summaries/' + slug + '.json').then(function (r) { return r.ok ? r.json() : null }).then(function (d) {
    if (!d) return
    summaries = {}; d.sections.forEach(function (s) { summaries[s.id] = s })
    if (active && (mode === 'para' || mode === 'line')) ask('user')
  }).catch(function () { /* no summaries: the heading alone */ })

  function esc(t) { return String(t).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c] }) }
  function label(s) { return s.id === 'top' ? 'The opening' : s.label }
  function inView(nodes) {
    var vh = window.innerHeight
    for (var i = 0; i < nodes.length; i++) { var r = nodes[i].getBoundingClientRect(); if (r.height && r.bottom > 0 && r.top < vh) return true }
    return false
  }
  // the parts of a section that a view changes: all of it, but the article's title stays in the opening
  function parts(s) { return s.id === 'top' ? s.nodes.filter(function (n) { return n.tagName !== 'H1' }) : s.nodes }

  /* ---- stillness ---- */
  // the page's own correction (restore) is not the reader moving it; and the position is also polled, since a
  // browser may not deliver a scroll event for every change
  var lastMove = 0, touching = false, selfY = null, polledY = window.scrollY
  function moved() { lastMove = Date.now() }
  function scrolled() { var y = window.scrollY; if (selfY !== null && Math.abs(y - selfY) < 1) return; selfY = null; moved() }
  window.addEventListener('scroll', scrolled, { passive: true })
  ;['wheel', 'touchmove'].forEach(function (ev) { window.addEventListener(ev, moved, { passive: true }) })
  window.addEventListener('touchstart', function () { touching = true; moved() }, { passive: true })
  ;['touchend', 'touchcancel'].forEach(function (ev) { window.addEventListener(ev, function () { touching = false; moved() }, { passive: true }) })
  function still() { return !touching && Date.now() - lastMove >= STILL }

  // keep the words in view where they are: the first element on screen that the views do not draw, and its top
  function anchor() {
    var els = main.querySelectorAll(':scope > *'), vh = window.innerHeight
    for (var i = 0; i < els.length; i++) {
      if (els[i].classList.contains('rf-fold')) continue
      var r = els[i].getBoundingClientRect(); if (r.height && r.bottom > 60 && r.top < vh) return { el: els[i], top: r.top }
    }
    return null
  }
  function restore(a) {
    if (!a || !a.el.isConnected || !a.el.getClientRects().length) return
    var d = a.el.getBoundingClientRect().top - a.top
    if (Math.abs(d) > 0.5) { window.scrollBy({ top: d, behavior: 'instant' }); selfY = polledY = window.scrollY }
  }

  /* ---- the margin, live ---- */
  var lit = {}
  function unlight(s) { parts(s).forEach(function (n) { n.classList.remove('rf-m', 'rf-done', 'rf-first'); n.style.removeProperty('--rf-p') }); delete lit[s.id] }
  function live() {
    R.sections().forEach(function (s) {
      if (mode !== 'margin' || (s.seen <= 0 && s.read <= 0)) { if (lit[s.id]) unlight(s); return }
      var done = s.read >= 0.999, p = done ? 100 : Math.round(s.read * 20) * 5, key = p + (done ? 'd' : '')
      if (lit[s.id] === key) return
      lit[s.id] = key
      parts(s).forEach(function (n, k) { n.classList.add('rf-m'); n.classList.toggle('rf-done', done); n.classList.toggle('rf-first', k === 0); n.style.setProperty('--rf-p', p + '%') })
    })
  }

  /* ---- a pass: fade, fold or hide what was read ---- */
  function clear(s) {
    parts(s).forEach(function (n) { n.classList.remove('rf-fade', 'rf-gone') })
    var f = main.querySelector('.rf-fold[data-for="' + s.id + '"]'); if (f) f.remove()
    R.fold(s.id, false)
  }
  function foldBlock(s, kind) {
    var sum = summaries && summaries[s.id]
    var d = document.createElement('div')
    d.className = 'rf-fold rf-' + kind; d.setAttribute('data-for', s.id)
    var body = kind === 'para' ? (sum ? '<p class="rf-p">' + esc(sum.para) + '</p>' : '')
      : kind === 'line' ? (sum ? '<span class="rf-l">' + esc(sum.line) + '</span>' : '') : ''
    d.innerHTML = '<span class="rf-tick" aria-hidden="true">✓</span><span class="rf-h">' + esc(label(s)) + '</span>' + body
      + '<button type="button" class="rf-show" data-show="' + esc(s.id) + '">Show</button>'
    return d
  }
  function draw(s) {
    clear(s)
    if (!active || mode === 'full' || mode === 'margin' || s.state !== 'read' || opened[s.id]) return
    var rest = parts(s)
    if (mode === 'fade') { rest.forEach(function (n) { n.classList.add('rf-fade') }); return }
    rest.forEach(function (n) { n.classList.add('rf-gone') })
    R.fold(s.id, true)
    if (mode !== 'hide') rest[0].parentNode.insertBefore(foldBlock(s, mode), rest[0])
  }
  // in Hidden, runs of hidden sections share one marker
  function markers() {
    main.querySelectorAll('.rf-hidden-run').forEach(function (x) { x.remove() })
    if (!active || mode !== 'hide') return
    var run = []
    function flush() {
      if (!run.length) return
      var m = document.createElement('div'); m.className = 'rf-fold rf-hidden-run'
      m.innerHTML = '<span class="rf-tick" aria-hidden="true">✓</span><span class="rf-h">' + run.length + ' section' + (run.length === 1 ? '' : 's') + ' you have read: ' + run.map(function (s) { return esc(label(s)) }).join(' · ') + '</span><button type="button" class="rf-show" data-show="' + run.map(function (s) { return esc(s.id) }).join(' ') + '">Show</button>'
      var first = parts(run[0]).filter(function (n) { return n.classList.contains('rf-gone') })[0]
      if (first) first.parentNode.insertBefore(m, first)
      run = []
    }
    R.sections().forEach(function (s) { if (applied[s.id] === 'gone') run.push(s); else flush() })
    flush()
  }
  // why: 'user' (a choice, Show, a mark) and 'return' (on arriving, before the reader has started) change every
  // section; 'scroll' leaves the sections on screen as they are
  function pass(why) {
    var root = document.documentElement, before = root.style.overflowAnchor
    root.style.overflowAnchor = 'none'
    var a = anchor(), secs = R.sections()
    // what is on screen is decided before anything changes: folding a section above moves the one in view up and
    // off screen, and asked one by one it would be folded too, with the words the reader was on (the first cause
    // of the jump, card 084)
    var onScreen = secs.map(function (s) { return why === 'scroll' && inView(s.nodes) })
    secs.forEach(function (s, i) {
      var key = active ? mode + ':' + (opened[s.id] ? 'open' : s.state) : 'off'
      if (applied[s.id + ':k'] === key) return
      if (onScreen[i]) return     // never under the reader's eyes
      draw(s)
      applied[s.id + ':k'] = key
      applied[s.id] = parts(s).some(function (n) { return n.classList.contains('rf-gone') }) ? 'gone' : 'shown'
    })
    markers()
    restore(a)
    requestAnimationFrame(function () { root.style.overflowAnchor = before })
    try { window.dispatchEvent(new CustomEvent('sgit-folds', { detail: { mode: mode, active: active } })) } catch (e) { /* old browser */ }
  }
  // a pass is asked for, and made when the page is still; a user's ask outranks a scroll's
  function ask(why) { if (want !== 'user') want = why }
  function due() {
    if (!want || !still()) return
    var why = want; want = null
    if (why !== 'user' && (mode === 'full' || mode === 'margin')) return
    active = true; maxY = window.scrollY
    pass(why)
  }

  /* ---- when ---- */
  function watch() {
    var y = window.scrollY
    if (y > maxY) maxY = y
    // the first time after going down at least a window; after that, from the deepest point since the last pass
    if (y < maxY - window.innerHeight * 0.5 && (active || maxY >= window.innerHeight)) { ask('scroll'); maxY = y }
  }
  window.addEventListener('scroll', watch, { passive: true })
  setInterval(function () { var y = window.scrollY; if (y !== polledY) { polledY = y; if (selfY === null || Math.abs(y - selfY) >= 1) moved() } watch(); due() }, 250)
  setInterval(live, 1000)
  if (R.returning && R.sections().some(function (s) { return s.state === 'read' })) {
    if (document.readyState === 'complete') ask('return'); else window.addEventListener('load', function () { ask('return') })
  }
  window.addEventListener('sgit-reading-change', function (e) { live(); if (active && !(e.detail && e.detail.pause)) ask('user') })
  main.addEventListener('click', function (e) {
    var t = e.target.closest('.rf-show'); if (!t) return
    t.getAttribute('data-show').split(' ').forEach(function (id) { opened[id] = true })
    ask('user'); due()
  })

  /* ---- the setting ---- */
  // scope 'all': every article; scope 'page': this article only, and '' takes it back to every article's
  function setMode(m, scope) {
    if (scope === 'page') {
      var p = pages(); if (valid(m)) p[R.path] = m; else delete p[R.path]
      var keys = Object.keys(p); if (keys.length > MAX_PAGES) keys.slice(0, keys.length - MAX_PAGES).forEach(function (k) { delete p[k] })
      ls.set(PAGES_KEY, Object.keys(p).length ? JSON.stringify(p) : null); pageMode = valid(m)
    } else {
      if (!valid(m)) return
      allMode = m; ls.set(KEY, m)
    }
    var next = pageMode || allMode
    if (next === mode) return
    mode = next; document.documentElement.setAttribute('data-read-view', mode)
    live(); active = true; ask('user'); due()
  }
  document.documentElement.setAttribute('data-read-view', mode)
  live()
  window.SgitFolds = {
    views: VIEWS, mode: function () { return mode }, allMode: function () { return allMode }, pageMode: function () { return pageMode },
    setMode: setMode, active: function () { return active }, still: still, pass: function () { ask('user'); due() }
  }
})()
