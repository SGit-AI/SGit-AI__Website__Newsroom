/* newsroom.sgit.ai: the reading strip (card 061). Loaded by the nav on every page that carries the meter
 * (admin/build/chrome.py); runs only where the page's <sg-meter view="page"> has a kind that is charged,
 * which is the imported articles, issues, notes and collections. Draws a hairline that fills as the reader
 * scrolls through <main> (or the body), and a chip with how far they are, what this page cost and the
 * balance left, from the meter's own records (localStorage, the key in #sg-meter-config). Refreshes on the
 * meter's events. Reads only; the meter does the charging and the depth. */
(function () {
  'use strict'
  var tag = document.querySelector('sg-meter[view="page"]')
  if (!tag || !tag.getAttribute('kind') || tag.getAttribute('kind') === 'free') return
  var cfg = { storageKey: 'sgit.meter.v1', symbol: '£', start: 500 }
  try { var el = document.getElementById('sg-meter-config'); if (el) cfg = Object.assign(cfg, JSON.parse(el.textContent)) } catch (e) { /* defaults */ }
  var links = cfg.links || {}, up = (document.documentElement.getAttribute('data-root') || '')
  var strip = document.createElement('div'); strip.className = 'read-strip'; strip.setAttribute('aria-hidden', 'true'); strip.innerHTML = '<i></i>'
  var chip = document.createElement('a'); chip.className = 'read-chip'; chip.href = up + (links.account || 'account/index.html'); chip.title = 'Your reading account: what you read, what it cost'
  document.body.appendChild(strip); document.body.appendChild(chip)
  var fill = strip.firstChild, path = location.pathname, pct = 0, shown = false
  function money(p) { return (p < -0.004 ? '−' : '') + cfg.symbol + (Math.abs(p) / 100).toFixed(2) }
  function state() { try { return JSON.parse(localStorage.getItem(cfg.storageKey) || 'null') } catch (e) { return null } }
  function numbers() {
    var s = state(), cost = 0, log = (s && s.log) || []
    for (var i = 0; i < log.length; i++) if (log[i].path === path) cost += log[i].cost || 0
    var balance = s ? s.balance : cfg.start
    chip.innerHTML = '<b class="pct">' + pct + '%</b><span class="sep">·</span><b>' + money(cost) + '</b> <span class="hide-sm">this page</span><span class="sep">·</span><b>' + money(balance) + '</b> left'
  }
  function measure() {
    var main = document.querySelector('main') || document.body, r = main.getBoundingClientRect()
    var top = r.top + window.scrollY, h = Math.max(1, r.height - window.innerHeight)
    var p = Math.round(100 * Math.min(1, Math.max(0, (window.scrollY - top + 0) / h)))
    if (r.height <= window.innerHeight) p = 100
    if (p !== pct) { pct = p; fill.style.width = p + '%'; numbers() }
    if (!shown && window.scrollY > 120) { shown = true; chip.classList.add('on') }
  }
  var ticking = false
  window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(function () { ticking = false; measure() }) } }, { passive: true })
  window.addEventListener('resize', measure)
  ;['sg:meter.changed', 'sg:meter.charged', 'sg:meter.rated', 'sg:meter.toppedup', 'sg:meter.declined'].forEach(function (ev) { document.addEventListener(ev, numbers) })
  numbers(); measure()
})()
