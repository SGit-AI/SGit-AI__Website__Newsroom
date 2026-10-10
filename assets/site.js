/* sgit.ai, shared behaviour (loaded via the SG bridge: sg.loadJs / sg.vfs.readText) */
(function () {
  'use strict';

  /* terminal tabs (landing) */
  var tabs = document.querySelectorAll('.ttab');
  if (tabs.length) {
    var cap = document.getElementById('tcap');
    tabs.forEach(function (t) {
      t.addEventListener('click', function () {
        tabs.forEach(function (x) { x.classList.remove('active'); });
        document.querySelectorAll('.tbody .pane').forEach(function (p) { p.classList.remove('active'); });
        t.classList.add('active');
        var pane = document.getElementById(t.getAttribute('data-pane'));
        if (pane) pane.classList.add('active');
        if (cap) cap.textContent = t.getAttribute('data-cap') || '';
      });
    });
  }

  /* copy-to-clipboard buttons */
  document.querySelectorAll('[data-copy]').forEach(function (btn) {
    var label = btn.querySelector('.cp');
    btn.addEventListener('click', function () {
      var done = function (ok) {
        if (label) { label.textContent = ok ? 'copied!' : 'copy'; setTimeout(function () { label.textContent = 'copy'; }, 1600); }
      };
      try {
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(btn.getAttribute('data-copy')).then(function () { done(true); }, function () { done(false); });
        } else { done(false); }
      } catch (e) { done(false); }
    });
  });

  /* reveal-on-scroll */
  var revs = document.querySelectorAll('.rev');
  if (revs.length) {
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (es, o) {
        es.forEach(function (e) {
          if (e.isIntersecting) { e.target.classList.add('in'); o.unobserve(e.target); }
        });
      }, { threshold: 0.06 });
      revs.forEach(function (r) { io.observe(r); });
    } else {
      revs.forEach(function (r) { r.classList.add('in'); });
    }
  }
})();

/* Nav interaction. Two separate jobs, and only one of them needs JavaScript on desktop:
   hover and :focus-within open a dropdown in CSS alone. This handles the rest —
   the phone menu button, and the fact that a finger has no hover. */
(function () {
  'use strict';
  var nav = document.querySelector('nav.site');
  if (!nav) return;
  var toggle = nav.querySelector('.nav-toggle');
  if (toggle) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }
  // On a touch screen the dropdown has no hover to open it: the first tap on a group
  // label opens the menu, a second follows the link. Only where a dropdown is actually
  // drawn, in the collapsed phone menu the children are already visible.
  document.addEventListener('click', function (e) {
    var link = e.target.closest && e.target.closest('nav.site .ni-has > .nl');
    var open = nav.querySelector('.ni-has.open');
    if (open && (!link || link.parentNode !== open)) open.classList.remove('open');
    if (!link || !window.matchMedia || !window.matchMedia('(hover: none)').matches) return;
    var item = link.parentNode, sub = item.querySelector('.sub');
    if (sub && window.getComputedStyle(sub).position === 'absolute'
            && !item.classList.contains('open')) {
      e.preventDefault();
      item.classList.add('open');
    }
  });
}());
