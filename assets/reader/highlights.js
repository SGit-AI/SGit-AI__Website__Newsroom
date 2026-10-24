/* newsroom.sgit.ai: highlights (card 074). Loaded by the nav beside the reading strip, on every page that carries
 * the meter; runs where the page is charged (articles, issues, notes, collections).
 *
 * Select words in the article and a small Highlight button appears beside them; tap it and the passage is marked
 * and kept. Tap a marked passage and the button offers to remove it. That is the whole gesture.
 *
 * A highlight is kept in this browser under sgit.highlights.v1, the way the W3C Web Annotation model anchors a
 * quote: the exact words, up to 32 characters before them and 32 after (TextQuoteSelector), the section it sits
 * in, and when. Anchoring by quote, not by position, means a highlight survives a corrected typo elsewhere in
 * the article; a passage that was rewritten is reported as unanchored, not silently dropped.
 *
 * It is drawn with the CSS Custom Highlight API (CSS.highlights, ::highlight(sgit-highlight)), which styles
 * ranges of text without changing the DOM: the imported article stays byte for byte what was published. A
 * browser without the API keeps the highlight and lists it in the reading map; it just cannot paint it.
 *
 * Nothing is sent anywhere. The vault does not carry highlights yet; the next step (in the article "Scrolled is
 * not read") is a highlight kind in the pane's notes, so they travel with the rest of the reading account.
 */
(function () {
  'use strict'
  var tag = document.querySelector('sg-meter[view="page"]')
  if (!tag || !tag.getAttribute('kind') || tag.getAttribute('kind') === 'free') return
  var main = document.querySelector('main')
  if (!main) return
  var KEY = 'sgit.highlights.v1', CTX = 32, MIN = 3, MAX = 600, NAME = 'sgit-highlight'
  var path = location.pathname.replace(/index\.html$/, '') || '/'
  var stop = main.querySelector(':scope > sg-meter, :scope > section.athreads, :scope > .athreads, :scope > .agent')

  function inArticle(node) {
    var el = node && (node.nodeType === 1 ? node : node.parentElement)
    if (!el || !main.contains(el)) return false
    if (el.closest('.read-map, .read-chip, .hl-btn, .vault-pane, .agent, sg-meter, .athreads, nav, footer')) return false
    if (stop && (stop.compareDocumentPosition(el) & Node.DOCUMENT_POSITION_FOLLOWING || stop === el)) return false
    return true
  }

  /* ---- the store ---- */
  function readStore() { try { var s = JSON.parse(localStorage.getItem(KEY) || 'null'); if (s && Array.isArray(s.items)) return s } catch (e) { /* fall through */ } return { v: 1, items: [] } }
  function writeStore(s) { try { localStorage.setItem(KEY, JSON.stringify(s)) } catch (e) { /* private window */ } try { window.dispatchEvent(new CustomEvent('sgit-highlights', { detail: { path: path } })) } catch (e) { /* old browser */ } }
  function forPage() { return readStore().items.filter(function (h) { return h.path === path }) }

  /* ---- the text of the article, as one string with a map back to its nodes ---- */
  function textIndex() {
    var nodes = [], text = '', w = document.createTreeWalker(main, NodeFilter.SHOW_TEXT, { acceptNode: function (n) { return inArticle(n) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT } })
    for (var n = w.nextNode(); n; n = w.nextNode()) { nodes.push({ node: n, start: text.length }); text += n.data }
    return { text: text, nodes: nodes }
  }
  function offsetOf(ix, node, off) { for (var i = 0; i < ix.nodes.length; i++) if (ix.nodes[i].node === node) return ix.nodes[i].start + off; return -1 }
  function pointAt(ix, pos) {
    for (var i = ix.nodes.length - 1; i >= 0; i--) if (ix.nodes[i].start <= pos) return { node: ix.nodes[i].node, offset: Math.min(pos - ix.nodes[i].start, ix.nodes[i].node.data.length) }
    return null
  }
  function anchor(ix, h) {
    var best = -1, bestScore = -1, from = 0
    for (;;) {
      var at = ix.text.indexOf(h.exact, from)
      if (at < 0) break
      var score = 0
      if (h.prefix && ix.text.slice(Math.max(0, at - h.prefix.length), at) === h.prefix) score += 2
      if (h.suffix && ix.text.slice(at + h.exact.length, at + h.exact.length + h.suffix.length) === h.suffix) score += 2
      if (score > bestScore) { best = at; bestScore = score }
      from = at + 1
    }
    if (best < 0) return null
    var a = pointAt(ix, best), b = pointAt(ix, best + h.exact.length)
    if (!a || !b) return null
    var r = document.createRange(); r.setStart(a.node, a.offset); r.setEnd(b.node, b.offset)
    return r
  }

  /* ---- drawing ---- */
  var ranges = []
  function draw() {
    var ix = textIndex()
    ranges = forPage().map(function (h) { return { h: h, r: anchor(ix, h) } })
    if (window.CSS && CSS.highlights && window.Highlight) {
      var live = ranges.filter(function (x) { return x.r }).map(function (x) { return x.r })
      if (live.length) CSS.highlights.set(NAME, new Highlight(...live)); else CSS.highlights.delete(NAME)
    }
  }

  /* ---- the button ---- */
  var btn = document.createElement('button'); btn.type = 'button'; btn.className = 'hl-btn'; btn.hidden = true
  document.body.appendChild(btn)
  var pendingSel = null, pendingRemove = null
  function place(rect) {
    btn.hidden = false
    var x = Math.min(window.innerWidth - btn.offsetWidth - 8, Math.max(8, rect.left + rect.width / 2 - btn.offsetWidth / 2))
    // on a touch screen the system's own menu (Copy, Look Up) sits above the selection and covers anything there,
    // so the button goes below it; with a mouse, above, where the eye already is
    var touch = window.matchMedia && window.matchMedia('(pointer: coarse)').matches
    var y = touch ? rect.bottom + 14 : rect.top - btn.offsetHeight - 8
    if (!touch && y < 56) y = rect.bottom + 8
    if (touch && y > window.innerHeight - btn.offsetHeight - 70) y = rect.top - btn.offsetHeight - 60
    btn.style.left = Math.round(x) + 'px'; btn.style.top = Math.round(y) + 'px'
  }
  function hide() { btn.hidden = true; pendingSel = null; pendingRemove = null; pendingRange = null }
  function onSelect() {
    var s = document.getSelection()
    if (!s || s.isCollapsed || !s.rangeCount) { if (pendingSel) hide(); return }
    var r = s.getRangeAt(0), t = s.toString().replace(/\s+/g, ' ').trim()
    if (t.length < MIN || t.length > MAX || !inArticle(r.startContainer) || !inArticle(r.endContainer)) { if (pendingSel) hide(); return }
    pendingSel = r.cloneRange(); pendingRemove = null
    btn.textContent = 'Highlight'; btn.className = 'hl-btn'
    place(r.getBoundingClientRect())
  }
  var selWait = 0
  document.addEventListener('selectionchange', function () { clearTimeout(selWait); selWait = setTimeout(onSelect, 180) })
  btn.addEventListener('mousedown', function (e) { e.preventDefault() })
  btn.addEventListener('click', function () {
    if (pendingRemove) {
      var st = readStore(); st.items = st.items.filter(function (h) { return h.id !== pendingRemove.id }); writeStore(st)
      hide(); draw(); return
    }
    if (!pendingSel) return
    var ix = textIndex(), a = offsetOf(ix, pendingSel.startContainer, pendingSel.startOffset), b = offsetOf(ix, pendingSel.endContainer, pendingSel.endOffset)
    if (a < 0 || b <= a) { hide(); return }
    var exact = ix.text.slice(a, b)
    var h = { id: Date.now().toString(36) + Math.random().toString(36).slice(2, 6), at: new Date().toISOString(), path: path,
              title: (document.querySelector('main h1') || {}).textContent || document.title,
              exact: exact, prefix: ix.text.slice(Math.max(0, a - CTX), a), suffix: ix.text.slice(b, b + CTX),
              section: window.SgitReading ? window.SgitReading.sectionOf(pendingSel.startContainer) : '' }
    var st = readStore(); st.items.push(h); writeStore(st)
    try { document.getSelection().removeAllRanges() } catch (e) { /* fine */ }
    hide(); draw()
  })
  /* a tap on a marked passage offers to remove it */
  main.addEventListener('click', function (e) {
    var s = document.getSelection(); if (s && !s.isCollapsed) return
    var hit = null
    for (var i = 0; i < ranges.length && !hit; i++) {
      var r = ranges[i].r; if (!r) continue
      var rects = r.getClientRects()
      for (var j = 0; j < rects.length; j++) { var q = rects[j]; if (e.clientX >= q.left && e.clientX <= q.right && e.clientY >= q.top && e.clientY <= q.bottom) { hit = ranges[i]; break } }
    }
    if (!hit) { if (pendingRemove) hide(); return }
    pendingRemove = hit.h; pendingSel = null; pendingRange = hit.r
    btn.textContent = 'Remove highlight'; btn.className = 'hl-btn hl-remove'
    place(hit.r.getBoundingClientRect())
  })
  // the button follows its passage as the page scrolls, and goes when the passage leaves the window
  var pendingRange = null
  window.addEventListener('scroll', function () {
    if (btn.hidden) return
    var r = pendingSel || pendingRange
    if (!r) return hide()
    var q = r.getBoundingClientRect()
    if (q.bottom < 0 || q.top > window.innerHeight) hide(); else place(q)
  }, { passive: true })
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !btn.hidden) hide() })
  window.addEventListener('storage', function (e) { if (e.key === KEY) draw() })

  window.SgitHighlights = { forPage: forPage, draw: draw, unanchored: function () { return ranges.filter(function (x) { return !x.r }).map(function (x) { return x.h }) } }
  if (document.readyState === 'complete') draw(); else window.addEventListener('load', draw)
})()
