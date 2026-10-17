/* newsroom.sgit.ai: showing what has been read (card 082). Loaded by the nav after the reading strip
 * (assets/reader/strip.js), on every page it runs on; uses window.SgitReading.
 *
 * Six ways to show, on the page itself, the sections the reader has already read, chosen by the reader and kept in
 * this browser (sgit.reading.view):
 *
 *   full       nothing changes
 *   margin     a line in the left margin of each section: solid when read, lighter when part read, faint grey when
 *              only scrolled past (the default)
 *   fade       read sections are faded, part-read ones a little; hover or focus brings them back
 *   para       a read section is folded to its heading and a paragraph of what it said
 *   line       a read section is folded to one line: its heading and about eight words
 *   hide       read sections are hidden; consecutive ones collapse into one marker that says how many and opens them
 *
 * Every folded section has Show, which opens it where it is. The paragraph and the line are the article's own
 * section summaries (articles/summaries/<slug>.json, admin/build/summaries.py), written with the article.
 *
 * WHEN. Never while the reader is reading forward: the page is theirs, at their pace. The views switch on in two
 * cases: the reader comes back to an article they had read some of before (the record is in sgit.reading.v1), or
 * they scroll back up by more than half a window after having gone down at least a window. Once on, they stay on
 * for the visit. A section on screen is never folded or unfolded by the clock; it changes only when it is off
 * screen, or when the reader asks (a mark, a reset, a change of view). When a fold changes the height of the
 * page above what the reader is looking at, the scroll position is corrected so the words in view do not move.
 *
 * A bar at the top of the window comes with them: how many sections are read, the six views, Pause and Reset.
 * It can be closed. Nothing is sent anywhere.
 */
(function () {
  'use strict'
  var R = window.SgitReading
  if (!R) return
  var main = document.querySelector('main')
  var KEY = 'sgit.reading.view', MODES = ['full', 'margin', 'fade', 'para', 'line', 'hide']
  var ls = {
    get: function (k) { try { return localStorage.getItem(k) } catch (e) { return null } },
    set: function (k, v) { try { localStorage.setItem(k, v) } catch (e) { /* private window */ } }
  }
  var asked = (function () { try { return new URLSearchParams(location.search).get('fold') } catch (e) { return null } })()
  var mode = MODES.indexOf(asked) >= 0 ? asked : (MODES.indexOf(ls.get(KEY)) >= 0 ? ls.get(KEY) : 'margin')
  var why0 = '', active = false, maxY = 0, dismissed = false, opened = {}, summaries = null, applied = {}

  /* ---- the summaries ---- */
  var slug = (location.pathname.match(/\/articles\/([^/]+)\.html$/) || [])[1]
  if (slug) fetch('summaries/' + slug + '.json').then(function (r) { return r.ok ? r.json() : null }).then(function (d) {
    if (!d) return
    summaries = {}; d.sections.forEach(function (s) { summaries[s.id] = s })
    if (active) apply(true)
  }).catch(function () { /* no summaries: the heading alone */ })

  function esc(t) { return String(t).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c] }) }
  function inView(nodes) {
    var vh = window.innerHeight
    for (var i = 0; i < nodes.length; i++) { var r = nodes[i].getBoundingClientRect(); if (r.height && r.bottom > 0 && r.top < vh) return true }
    return false
  }
  // keep the words in view where they are: remember the first visible element and its top, and restore it after
  function anchor() {
    var els = main.querySelectorAll(':scope > *'), vh = window.innerHeight
    for (var i = 0; i < els.length; i++) { var r = els[i].getBoundingClientRect(); if (r.height && r.bottom > 60 && r.top < vh) return { el: els[i], top: r.top } }
    return null
  }
  function restore(a) {
    if (!a || !a.el.isConnected || !a.el.getClientRects().length) return
    var d = a.el.getBoundingClientRect().top - a.top
    if (Math.abs(d) > 1) window.scrollBy({ top: d, behavior: 'instant' })
  }

  /* ---- drawing one section ---- */
  function clear(s) {
    s.nodes.forEach(function (n) { n.classList.remove('rf-m', 'rf-read', 'rf-part', 'rf-skim', 'rf-fade', 'rf-fade-part', 'rf-gone'); n.removeAttribute('data-rf') })
    var f = document.querySelector('.rf-fold[data-for="' + s.id + '"]'); if (f) f.remove()
    R.fold(s.id, false)
  }
  function foldBlock(s, kind) {
    var sum = summaries && summaries[s.id]
    var label = s.id === 'top' ? 'The opening' : s.label
    var d = document.createElement('div')
    d.className = 'rf-fold rf-' + kind; d.setAttribute('data-for', s.id)
    var body = kind === 'para' ? (sum ? '<p class="rf-p">' + esc(sum.para) + '</p>' : '')
      : kind === 'line' ? (sum ? '<span class="rf-l">' + esc(sum.line) + '</span>' : '') : ''
    d.innerHTML = '<span class="rf-tick" aria-hidden="true">✓</span><span class="rf-h">' + esc(label) + '</span>' + body
      + '<button type="button" class="rf-show" data-show="' + esc(s.id) + '">Show</button>'
    return d
  }
  function draw(s) {
    clear(s)
    if (!active || mode === 'full') return
    var st = s.state
    if (st === 'unread') return
    var keep = s.id === 'top' ? s.nodes.filter(function (n) { return n.tagName === 'H1' }) : []
    var rest = s.nodes.filter(function (n) { return keep.indexOf(n) < 0 })
    var foldable = st === 'read' && !opened[s.id] && (mode === 'para' || mode === 'line' || mode === 'hide')
    if (foldable) {
      rest.forEach(function (n) { n.classList.add('rf-gone') })
      R.fold(s.id, true)
      if (mode !== 'hide') { var b = foldBlock(s, mode); var at = rest[0]; at.parentNode.insertBefore(b, at) }
      return
    }
    rest.forEach(function (n) {
      if (mode === 'fade' && (st === 'read' || st === 'part')) n.classList.add(st === 'read' ? 'rf-fade' : 'rf-fade-part')
      else { n.classList.add('rf-m', st === 'read' ? 'rf-read' : st === 'part' ? 'rf-part' : 'rf-skim') }
    })
  }
  // in Hidden, runs of hidden sections share one marker
  function markers() {
    document.querySelectorAll('.rf-hidden-run').forEach(function (x) { x.remove() })
    if (!active || mode !== 'hide') return
    var secs = R.sections(), run = []
    function flush() {
      if (!run.length) return
      var m = document.createElement('div'); m.className = 'rf-fold rf-hidden-run'
      m.innerHTML = '<span class="rf-tick" aria-hidden="true">✓</span><span class="rf-h">' + run.length + ' section' + (run.length === 1 ? '' : 's') + ' you have read: ' + run.map(function (s) { return esc(s.id === 'top' ? 'The opening' : s.label) }).join(' · ') + '</span><button type="button" class="rf-show" data-show="' + run.map(function (s) { return esc(s.id) }).join(' ') + '">Show</button>'
      var first = run[0].nodes.filter(function (n) { return n.classList.contains('rf-gone') })[0]
      if (first) first.parentNode.insertBefore(m, first)
      run = []
    }
    secs.forEach(function (s) { if (applied[s.id] === 'gone' && mode === 'hide') run.push(s); else flush() })
    flush()
  }
  // force: redraw even if nothing changed; skipInView: leave sections on screen as they are (the clock, and switching on
  // after a scroll up). A section left alone is drawn when it is off screen.
  function apply(force, skipInView) {
    var a = anchor()
    R.sections().forEach(function (s) {
      var key = active ? mode + ':' + (opened[s.id] ? 'open' : s.state) : 'off'
      if (!force && applied[s.id + ':k'] === key) return
      if ((!force || skipInView) && inView(s.nodes)) return     // never under the reader's eyes
      draw(s)
      applied[s.id + ':k'] = key
      applied[s.id] = s.nodes.some(function (n) { return n.classList.contains('rf-gone') }) ? 'gone' : 'shown'
    })
    markers()
    restore(a)
    bar()
    try { window.dispatchEvent(new CustomEvent('sgit-folds', { detail: { mode: mode, active: active } })) } catch (e) { /* old browser */ }
  }

  /* ---- when ---- */
  function activate(why) { if (active) return; active = true; why0 = why; document.documentElement.setAttribute('data-read-view', mode); apply(true, why === 'up'); bar(why) }
  // the deepest point is followed on every scroll event and on the clock, since a browser may coalesce scroll events
  function watch() {
    var y = window.scrollY
    if (y > maxY) maxY = y
    if (!active && maxY >= window.innerHeight && y < maxY - window.innerHeight * 0.5) activate('up')
  }
  window.addEventListener('scroll', watch, { passive: true })
  setInterval(watch, 500)
  if (R.returning) {
    var any = R.sections().some(function (s) { return s.state === 'read' || s.state === 'part' })
    if (any) { if (document.readyState === 'complete') activate('return'); else window.addEventListener('load', function () { activate('return') }) }
  }
  window.addEventListener('sgit-reading-change', function () { if (active) apply(true); else bar() })
  setInterval(function () { if (active) apply(false) }, 2000)

  /* ---- the bar at the top ---- */
  var topbar = document.createElement('div'); topbar.className = 'read-bar'; topbar.hidden = true; topbar.setAttribute('role', 'region'); topbar.setAttribute('aria-label', 'What you have read on this page')
  document.body.appendChild(topbar)
  function navBottom() { var n = document.querySelector('nav.site'); if (!n) return 0; var r = n.getBoundingClientRect(); return Math.max(0, Math.round(r.bottom)) }
  function bar(why) {
    why = why || why0
    if (!active || dismissed) { topbar.hidden = true; return }
    var secs = R.sections(), done = secs.filter(function (s) { return s.state === 'read' }).length, p = R.paused()
    topbar.innerHTML = '<span class="rb-t"><b>' + done + ' of ' + secs.length + '</b> sections read' + (why === 'return' ? ', from your last visit' : '') + '</span>'
      + R.viewPicker('rv-bar')
      + '<button type="button" class="rb-b" data-act="pause" aria-pressed="' + p + '">' + (p ? 'Resume' : 'Pause') + '</button>'
      + '<button type="button" class="rb-b" data-act="reset">Reset</button>'
      + '<button type="button" class="rb-x" aria-label="Close this bar">×</button>'
    topbar.style.top = navBottom() + 'px'
    topbar.hidden = false
  }
  window.addEventListener('scroll', function () { if (!topbar.hidden) topbar.style.top = navBottom() + 'px' }, { passive: true })
  topbar.addEventListener('click', function (e) {
    var t = e.target.closest('button'); if (!t) return
    if (t.classList.contains('rb-x')) { dismissed = true; topbar.hidden = true; return }
    if (t.dataset.view) return setMode(t.dataset.view)
    if (t.dataset.act === 'pause') { R.setPaused(!R.paused()); return bar() }
    if (t.dataset.act === 'reset') { opened = {}; R.reset(); return }
  })
  main.addEventListener('click', function (e) {
    var t = e.target.closest('.rf-show'); if (!t) return
    t.getAttribute('data-show').split(' ').forEach(function (id) { opened[id] = true })
    apply(true)
  })

  function setMode(m) {
    if (MODES.indexOf(m) < 0) return
    mode = m; ls.set(KEY, m); document.documentElement.setAttribute('data-read-view', m)
    if (!active) activate('choice'); else apply(true)
  }
  window.SgitFolds = { mode: function () { return mode }, setMode: setMode, active: function () { return active }, activate: activate, apply: function () { apply(true) } }
})()
