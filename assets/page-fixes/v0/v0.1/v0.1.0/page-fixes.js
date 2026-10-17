/* page-fixes v0.1.0: small fixes a reader applies to the page in front of them, exposed as a JS API.

   window.__tools.page            the API, after the 'tool:ready' event with detail.name 'page'
     .list()                      the fixes this page offers: [{ name, title, on }]
     .apply(name, on = true)      turn a fix on or off; returns the list
     .toggle(name)                flip it
     .reset()                     every fix off, and forget them for this site
     .meta                        { name, version, site }

   Fixes are CSS, plus two small helpers (an outline of the headings, and the page's markdown twin where a site
   has one). A site can declare its own selectors in SITES, so its reading mode removes exactly its chrome; any
   other site gets a generic one. Which fixes are on is remembered per site in localStorage, and reapplied the
   next time this file loads on that site. Nothing leaves the page.

   Load it once and call it, from a bookmarklet, the console, a test or an agent:
     window.__tools.page.toggle('reading')
   The file is immutable at this path: a change is a new version, so a bookmarklet that loads it keeps working. */
(function () {
  if (window.__tools && window.__tools.page) return;
  var VERSION = '0.1.0', host = location.host, KEY = 'page-fixes:' + host;

  // Per-site chrome to remove in reading mode. Anything not listed falls back to GENERIC.
  var SITES = {
    'newsroom.sgit.ai': 'nav.site, .llmschip, footer.site, .vault-pane, .read-strip, .read-chip, .read-map, .hl-btn, ' +
                        '.trail, #threads, aside.lkit, .subteaser, .agent, .crumb'
  };
  var GENERIC = 'header, nav, aside, footer, [role="banner"], [role="navigation"], [role="complementary"], ' +
                '[role="contentinfo"], iframe';

  var FIXES = {
    reading:  { title: 'Reading mode: only the text, in one column',
                css: function () {
                  return (SITES[host] || GENERIC) + ',[data-page-fixes-hidden]{display:none!important}' +
                    'main,article,[role="main"]{max-width:42rem!important;margin:0 auto!important;padding:1rem!important}'; },
                // On a site with no entry in SITES, also hide whatever floats over the text: fixed and sticky boxes.
                on: function () { if (SITES[host]) return; [].slice.call(document.querySelectorAll('body *')).forEach(function (el) {
                  var pos = getComputedStyle(el).position;
                  if ((pos === 'fixed' || pos === 'sticky') && el.id !== 'page-fixes-outline') el.setAttribute('data-page-fixes-hidden', '');
                }); },
                off: function () { [].slice.call(document.querySelectorAll('[data-page-fixes-hidden]')).forEach(function (el) {
                  el.removeAttribute('data-page-fixes-hidden'); }); } },
    bigger:   { title: 'Bigger text', css: function () { return 'html{font-size:125%!important}'; } },
    contrast: { title: 'High contrast: black on white, links underlined',
                css: function () { return '*{background:#fff!important;color:#000!important;border-color:#000!important}' +
                                          'a,a *{color:#00c!important;text-decoration:underline!important}'; } },
    spacing:  { title: 'Text spacing, as WCAG 1.4.12 asks it to survive',
                css: function () { return '*{line-height:1.5!important;letter-spacing:.12em!important;word-spacing:.16em!important}' +
                                          'p{margin-bottom:2em!important}'; } },
    outline:  { title: 'An outline of the headings, to jump around', css: function () { return ''; },
                on: function () { outline(true); }, off: function () { outline(false); } },
    markdown: { title: 'Open the page as markdown, where the site publishes a twin', css: function () { return ''; },
                once: function () {
                  var u = location.pathname.replace(/\.html$/, '.md');
                  if (u === location.pathname) u = location.pathname.replace(/\/?$/, '/index.md');
                  location.href = u; } }
  };

  var on = {};
  try { on = JSON.parse(localStorage.getItem(KEY) || '{}'); } catch (e) { on = {}; }

  function save() { try { localStorage.setItem(KEY, JSON.stringify(on)); } catch (e) {} }

  function render() {
    var el = document.getElementById('page-fixes-style');
    if (!el) { el = document.createElement('style'); el.id = 'page-fixes-style'; document.head.appendChild(el); }
    el.textContent = '#page-fixes-outline{display:block!important}\n' + Object.keys(on).filter(function (k) { return on[k] && FIXES[k]; })
      .map(function (k) { return FIXES[k].css(); }).join('\n');
  }

  function outline(show) {
    var box = document.getElementById('page-fixes-outline');
    if (!show) { if (box) box.remove(); return; }
    if (box) return;
    box = document.createElement('div');
    box.id = 'page-fixes-outline';
    box.setAttribute('aria-label', 'Outline of this page');
    box.style.cssText = 'position:fixed;top:1rem;right:1rem;max-height:80vh;overflow:auto;z-index:2147483647;' +
      'background:#fff;color:#000;border:2px solid #000;border-radius:8px;padding:.6rem .8rem;font:14px/1.4 system-ui;max-width:18rem';
    var hs = [].slice.call(document.querySelectorAll('h1, h2, h3'));
    hs.forEach(function (h, i) {
      if (!h.id) h.id = 'page-fixes-h' + i;
      var a = document.createElement('a');
      a.href = '#' + h.id; a.textContent = h.textContent.trim().slice(0, 80);
      a.style.cssText = 'display:block;color:#00c;margin:.15rem 0;padding-left:' + (h.tagName === 'H3' ? '1rem' : '0');
      box.appendChild(a);
    });
    document.body.appendChild(box);
  }

  function apply(name, value) {
    var f = FIXES[name];
    if (!f) throw new Error('page-fixes: no fix called ' + name + '; try list()');
    if (f.once) { f.once(); return list(); }
    var v = value === undefined ? true : !!value;
    on[name] = v;
    if (v && f.on) f.on();
    if (!v && f.off) f.off();
    save(); render();
    window.dispatchEvent(new CustomEvent('page-fixes:change', { detail: { name: name, on: v } }));
    return list();
  }

  function list() {
    return Object.keys(FIXES).map(function (k) { return { name: k, title: FIXES[k].title, on: !!on[k] }; });
  }

  var API = {
    meta: { name: 'page-fixes', version: VERSION, site: host },
    list: list,
    apply: apply,
    toggle: function (name) { return apply(name, !on[name]); },
    reset: function () {
      Object.keys(on).forEach(function (k) { if (FIXES[k] && FIXES[k].off) FIXES[k].off(); });
      on = {}; save(); render(); return list();
    }
  };

  // Reapply what this reader turned on for this site last time.
  Object.keys(on).forEach(function (k) { if (on[k] && FIXES[k] && FIXES[k].on) FIXES[k].on(); });
  render();

  window.__tools = window.__tools || {};
  window.__tools.page = API;
  window.dispatchEvent(new CustomEvent('tool:ready', { detail: { name: 'page' } }));
})();
