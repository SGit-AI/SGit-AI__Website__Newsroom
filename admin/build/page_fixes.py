#!/usr/bin/env python3
"""Fix the page: /demos/fixes/index.html, bookmarklets and a page API for this newsroom.

    python3 admin/build/page_fixes.py

The API is assets/page-fixes/v0/v0.1/v0.1.0/page-fixes.js (window.__tools.page, after 'tool:ready'), described by
api.json beside it. This page loads it, lets a reader try every fix, and offers each one as a bookmarklet that
loads the same file on any newsroom page and calls it. The bookmarklets' href is set at runtime from data-bm,
because a javascript: URL is not a link this site serves and the validator rightly reads hrefs as links.
"""
import html
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from page import newsroom_page, write  # noqa: E402

REL = "demos/fixes/index.html"
API = "assets/page-fixes/v0/v0.1/v0.1.0/page-fixes.js"
ABS = "https://newsroom.sgit.ai/" + API
e = html.escape

FIXES = [
    ("reading", "Reading mode", "Only the text, in one column: no menu, no strip, no chips, no footer."),
    ("bigger", "Bigger text", "Everything at 125%."),
    ("contrast", "High contrast", "Black on white, links blue and underlined."),
    ("spacing", "Text spacing", "Line, letter, word and paragraph spacing at the values WCAG 1.4.12 says a page must survive."),
    ("outline", "Outline", "A box of the page's headings, to jump around."),
    ("markdown", "Markdown", "The same page as its markdown twin, which every article here has."),
]


def bookmarklet(name):
    return ("javascript:(()=>{const F='" + name + "',U='" + ABS + "',t=window.__tools&&window.__tools.page;"
            "if(t){t.toggle(F);return}const s=document.createElement('script');s.src=U;"
            "s.onload=()=>window.__tools.page.toggle(F);document.head.appendChild(s)})()")


SELF_CONTAINED = ("javascript:(()=>{const s=document.createElement('style');s.textContent='header,nav,aside,footer,"
                  "[role=banner],[role=complementary],iframe{display:none!important}main,article{max-width:42rem!important;"
                  "margin:0 auto!important}';document.head.appendChild(s)})()")


def page():
    rows = "\n".join(
        f'<tr><td><b>{e(t)}</b><br><span class="small dim">{e(d)}</span></td>'
        f'<td><button type="button" class="pf-try" data-fix="{n}">Try it here</button></td>'
        f'<td><a class="pf-bm" data-bm="{e(bookmarklet(n), quote=True)}" title="Drag me to your bookmarks bar">{e(t)}</a></td></tr>'
        for n, t, d in FIXES)
    body = f"""
<style>
.pf-bm{{display:inline-block;padding:.35rem .7rem;border:2px dashed var(--accent,#0F766E);border-radius:8px;text-decoration:none;font-weight:700;cursor:grab}}
.pf-try{{padding:.35rem .7rem;border-radius:8px;border:1px solid var(--line);background:var(--panel);cursor:pointer}}
.pf-try[aria-pressed="true"]{{background:#0F766E;color:#fff;border-color:#0F766E}}
table.pf td{{vertical-align:middle;padding:.5rem .4rem}}
pre.pf{{white-space:pre-wrap;word-break:break-all;font-size:.82rem}}
</style>

<p>Every site has things a reader would change if they could: a menu they do not need while reading, text too small, too little contrast, no outline. This page is a working example of letting them, on this newsroom. It is the companion to <a href="../../articles/fix-the-page-yourself.html">Fix the page yourself</a>, which makes the case.</p>

<h2 id="try">Try them here, or take them with you</h2>
<p>Press <b>Try it here</b> to apply a fix to this page. To use it on any page of this newsroom, drag the dashed button to your browser's bookmarks bar, open an article, and click the bookmark. Click it again to undo. What you turn on is remembered for this site, in your browser, and nothing leaves it.</p>
<table class="pf">
<tr><th>Fix</th><th>Here</th><th>Bookmarklet</th></tr>
{rows}
</table>
<p><button type="button" class="pf-try" id="pf-reset">Reset everything</button></p>

<h2 id="api">The API underneath</h2>
<p>Every bookmarklet is one line, because the work is in a page API. It loads once, and then anything can call it: a bookmarklet, the console, a test, or an agent driving the browser.</p>
<pre class="pf">window.__tools.page.list()               // the fixes, and which are on
window.__tools.page.toggle('reading')    // flip one
window.__tools.page.apply('bigger', true)
window.__tools.page.reset()</pre>
<p>It follows the convention the SGraph tools use: the API lives at <code>window.__tools</code>, announces itself with a <code>tool:ready</code> event, and is described by an <a href="../../{API.replace('page-fixes.js', 'api.json')}">api.json</a>. The file itself is <a href="../../{API}">{e(API.split('/')[-1])}</a>, about 150 lines, versioned and immutable at its path, so a bookmarklet that loads it keeps working. For Playwright, or an agent:</p>
<pre class="pf">await page.addScriptTag({{ url: '{ABS}' }});
await page.waitForFunction(() =&gt; window.__tools?.page);
await page.evaluate(() =&gt; window.__tools.page.apply('reading'));</pre>

<h2 id="bookmarklet">What a bookmarklet is</h2>
<p>A bookmark whose address is a line of JavaScript instead of a web page. Click it and the line runs on the page you are on, with nothing installed. This is the one that toggles reading mode:</p>
<pre class="pf">{e(bookmarklet('reading'))}</pre>
<p>And this one needs no file at all: a generic reading mode for any site, in one line. It is what you can do without the site's help, and it shows the limit: it guesses at the site's structure, and it gets it wrong where the site does not use the usual tags.</p>
<p><a class="pf-bm" data-bm="{e(SELF_CONTAINED, quote=True)}">Reading mode, anywhere</a></p>
<pre class="pf">{e(SELF_CONTAINED)}</pre>

<h2 id="limits">What this does not do yet</h2>
<ul>
<li><b>Other sites can refuse it.</b> A site whose Content Security Policy blocks inline or outside scripts will block the loader, and sometimes the bookmarklet itself. That is the argument of the article: a site should offer these primitives itself.</li>
<li><b>It is not an extension.</b> A browser extension with Chrome's <code>activeTab</code> permission would run only on the tab you click it on, with no install warning; that is the next step.</li>
<li><b>Six fixes, one site.</b> It is a start, and the list is meant to grow from what readers ask for.</li>
</ul>

<script>
(function () {{
  document.querySelectorAll('.pf-bm').forEach(function (a) {{ a.setAttribute('href', a.getAttribute('data-bm')); }});
  function sync() {{
    var t = window.__tools && window.__tools.page; if (!t) return;
    t.list().forEach(function (f) {{ var b = document.querySelector('.pf-try[data-fix="' + f.name + '"]'); if (b) b.setAttribute('aria-pressed', f.on ? 'true' : 'false'); }});
  }}
  window.addEventListener('page-fixes:change', sync);
  window.addEventListener('tool:ready', sync);
  document.querySelectorAll('.pf-try[data-fix]').forEach(function (b) {{
    b.addEventListener('click', function () {{ window.__tools && window.__tools.page && window.__tools.page.toggle(b.getAttribute('data-fix')); sync(); }});
  }});
  document.getElementById('pf-reset').addEventListener('click', function () {{ window.__tools && window.__tools.page && window.__tools.page.reset(); sync(); }});
  fetch('../../{API}').then(function (r) {{ if (!r.ok) throw new Error(r.status); return r.text(); }})
    .then(function (t) {{ (0, eval)(t); sync(); }})
    .catch(function (err) {{ console.error('[fixes] page-fixes.js failed to load:', err); }});
}}());
</script>
"""
    agent = ("This page loads a page API at window.__tools.page (see api.json beside page-fixes.js): list(), apply(name, on), "
             "toggle(name), reset(). The fixes are reading, bigger, contrast, spacing, outline and markdown. An agent can apply "
             "them on any newsroom page by loading the same file; they are CSS in the reader's browser and change nothing on the site.")
    return newsroom_page(REL, "Fix the page: bookmarklets and a page API",
                         "Six fixes a reader can apply to any page of this newsroom, from reading mode to WCAG text spacing: try them here, take them as bookmarklets, or call them from code.",
                         body, eyebrow="A tool", lead="Six fixes for any page of this newsroom, as buttons, as bookmarklets, and as a JS API.",
                         agent=agent)


if __name__ == "__main__":
    changed = write(REL, page())
    print(f"page_fixes: {REL} {'written' if changed else 'unchanged'}")
