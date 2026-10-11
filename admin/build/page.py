#!/usr/bin/env python3
"""One page shell for the pages this site writes in the newsroom's look.

The newsroom pages are imported from sgit.ai and styled by assets/newsroom.css. A page this
site writes itself (the design hub, the archive, how to replicate it) uses the same
stylesheet and the same few classes, so a reader moving from an article to a design page
does not change websites on the way. The classes are the ones the imported pages use:
main.doc, p.crumb, p.eyebrow, p.lead, div.note, .tablewrap, nav.fsub.

The nav and footer are left empty here and filled by chrome.py, like every page.
"""
import html as _html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HOST = (ROOT / "CNAME").read_text().strip()


def esc(s):
    return _html.escape(s, quote=True)


# SG Meter, the reading meter, at a versioned path that never changes. v1.4.0 is this site's own build (see sync_newsroom.py, item 11).
METER_JS = "assets/components/sg-meter/v1/v1.4/v1.4.0/sg-meter.js"


def meter_config():
    """The meter's config, taken from the imported front page so it is written once and is the
    same on every page. None until the newsroom has been imported."""
    front = ROOT / "index.html"
    if not front.exists():
        return None
    m = re.search(r'<script type="application/json" id="sg-meter-config">(.*?)</script>',
                  front.read_text(encoding="utf-8"), re.S)
    return m.group(1) if m else None


def meter_block(up, title):
    """The balance chip in the nav is the meter, and a page only gets one if it loads the meter.
    A page this site writes is declared kind="free": nothing is charged for it, and the reader's
    balance is still on screen, so it does not vanish when they follow a link from an article
    (a synthetic reader took it for lost credit on the Replicate page). What a page of this
    kind costs is one attribute, and is a decision for the editor, not for a template."""
    cfg = meter_config()
    if cfg is None:
        return ""
    assert (ROOT / METER_JS).exists(), f"{METER_JS} is not on disk; run admin/build/sync_newsroom.py"
    return (f'<sg-meter view="page" kind="free" date="" topics="" title="{esc(title)}, SGit Newsroom" quiet></sg-meter>\n'
            f'<script type="application/json" id="sg-meter-config">{cfg}</script>\n'
            f'<script>\nimport(\'{up}{METER_JS}\')\n'
            f" .catch(function (e) {{ console.error('[sg-meter] component failed to load:', e); }});\n</script>\n")


def newsroom_page(rel, title, description, body, *, eyebrow="", crumbs=(), lead="", agent=""):
    """rel is the page's path from the site root; crumbs is ((label, path-from-root), ...)."""
    up = "../" * rel.count("/")
    canonical = f"https://{HOST}/" + ("" if rel == "index.html" else rel)
    trail = " / ".join([f'<a href="{up}index.html">Home</a>']
                       + [f'<a href="{up}{href}">{label}</a>' for label, href in crumbs]
                       + [esc(title)])
    return f"""<!doctype html>
<html lang="en" data-root="{up}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)} &middot; newsroom.sgit.ai</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="newsroom.sgit.ai">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:image" content="https://{HOST}/og/default.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="{up}assets/newsroom.css">
</head>
<body>
<nav class="site"></nav>
<main class="doc">
 <p class="crumb">{trail}</p>
 {f'<p class="eyebrow">{eyebrow}</p>' if eyebrow else ''}
 <h1>{esc(title)}</h1>
 {f'<p class="lead">{lead}</p>' if lead else ''}
{body}
<div class="agent">
  <h4>For an agent</h4>
  <p>{agent}</p>
</div>
</main>
{meter_block(up, title)}<footer class="site"></footer>
<script src="{up}assets/site.js" defer></script>
</body>
</html>
"""


def _unchromed(text):
    text = re.sub(r'<nav class="site">.*?</nav>', '<nav class="site"></nav>', text, count=1, flags=re.S)
    return re.sub(r'<footer class="site">.*?</footer>', '<footer class="site"></footer>', text, count=1, flags=re.S)


def write(rel, text):
    """Write a generated page, unless the file on disk already says the same thing. The page
    on disk carries the nav and footer chrome.py stamped; the page generated here carries
    empty blocks. Comparing them raw would rewrite every page on every build and leave
    chrome.py to put the chrome back, which is churn, not change."""
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.exists() and _unchromed(p.read_text(encoding="utf-8")) == _unchromed(text):
        return False
    p.write_text(text, encoding="utf-8")
    return True
