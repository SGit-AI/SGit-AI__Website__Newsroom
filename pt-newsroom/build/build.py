#!/usr/bin/env python3
"""pt-newsroom/build/build.py — renders the chosen home-page design for pt.newsroom.sgit.ai as
a page on this site, from the design sources in pt-newsroom/design/.

    python3 pt-newsroom/build/build.py && python3 admin/build/chrome.py && node admin/build/validate.js

The sources are the artboards drawn on 13 September 2026 (Main.dc = 1440px, MainPhone.dc =
390px), kept verbatim with a `.dc` extension so the site validator does not treat them as
pages. This script takes each artboard's stylesheet and markup, scopes the stylesheet under
`.mock` so it cannot restyle the site chrome around it, swaps the Google Fonts link for the
vendored faces in assets/fonts.css, and writes one page carrying both frames. Nothing in the
design is edited here: a change to the design is a change to the .dc file.
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SEC = ROOT / "pt-newsroom"
HOST = "https://" + (ROOT / "CNAME").read_text().strip()


def parse(dc):
    s = dc.read_text(encoding="utf-8")
    style = re.search(r"<helmet>(.*?)</helmet>", s, re.S).group(1)
    css = "\n".join(re.findall(r"<style>(.*?)</style>", style, re.S))
    body = re.search(r"</helmet>\s*(.*?)\s*</x-dc>", s, re.S).group(1)
    return css, body


def scope(css, prefix):
    """Prefix every selector with `prefix`; `body` becomes the prefix itself."""
    out = []
    for block in re.split(r"(?<=\})", css):
        block = block.strip()
        if not block or "{" not in block:
            continue
        sel, rest = block.split("{", 1)
        sels = []
        for one in sel.split(","):
            one = one.strip()
            if not one:
                continue
            sels.append(prefix if one == "body" else f"{prefix} {one}")
        out.append(", ".join(sels) + "{" + rest)
    return "\n".join(out)


def main():
    css_d, body_d = parse(SEC / "design" / "Main.dc")
    css_p, body_p = parse(SEC / "design" / "MainPhone.dc")
    scoped = scope(css_d, ".mock-desk") + "\n" + scope(css_p, ".mock-phone")
    # the frames: the design is fixed-width on purpose, so on a narrow screen it scrolls
    # sideways inside its frame rather than reflowing into something that was not designed
    frame_css = """
.mockwrap{max-width:min(1560px,97vw);margin:0 auto;padding:0 1.1rem}
.mockframe{overflow-x:auto;border:1px solid var(--line2);border-radius:6px;background:#f7f4ec;box-shadow:var(--shadow)}
.mockframe.phone{width:390px;max-width:100%;margin:0}
.mocklabel{font-family:var(--mono);font-size:.68rem;letter-spacing:.12em;text-transform:uppercase;color:var(--dim);margin:1.6rem 0 .5rem}
.mock-desk .A, .mock-phone .A{font-family:"Newsreader",Georgia,"Times New Roman",serif}
"""
    canonical = f"{HOST}/pt-newsroom/index.html"
    title = "pt.newsroom.sgit.ai: the home page, as designed"
    desc = ("The chosen home-page design for the Portuguese-language newsroom, rendered as a page: a broadsheet "
            "drawn with the Portugal section's real data of 13 September 2026, at 1440px and at 390px.")
    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(title)} &middot; newsroom.sgit.ai</title>
<meta name="description" content="{html.escape(desc, quote=True)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="newsroom.sgit.ai">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{html.escape(title, quote=True)}">
<meta property="og:description" content="{html.escape(desc, quote=True)}">
<meta name="twitter:card" content="summary">
<link rel="stylesheet" href="../assets/site.css">
<link rel="stylesheet" href="../assets/fonts.css">
<style>
{scoped}
{frame_css}
</style>
</head>
<body>

<nav class="site"><div class="row"></div></nav>

<main class="doc" style="max-width:min(1560px,97vw)">
<div class="crumb"><a href="../index.html">newsroom.sgit.ai</a> / pt-newsroom</div>
<h1>pt.newsroom.sgit.ai: the home page, as designed</h1>
<p class="lead">The site does not exist yet. This is its front page as chosen on 13 September 2026 &mdash;
a classic broadsheet, natively Portuguese, drawn with <a href="../portugal/index.html">the Portugal
section&rsquo;s</a> real data of that day &mdash; rendered here as a page so the agent that builds the site,
and anyone else, can see it at full size rather than as a picture. The brief that commissions the site is
<a href="../documents/pt-newsroom.html">here</a>; its section 16 records the design system.</p>

<div class="note"><p style="margin-top:0"><b>What this page is, and is not.</b> It is a rendering of the design
sources (<code>pt-newsroom/design/Main.dc</code> and <code>MainPhone.dc</code>) with nothing edited. The
copy on it &mdash; the three stories, the 60&rarr;64 speaker diff, the seven press pages, the programme &mdash;
was true on 13 September and is not updated; take the structure, not the numbers. The links inside the
mock-up go nowhere on purpose. Three of the four directions drawn that day were not chosen and are not
published. The two typefaces, Newsreader and IBM Plex Mono, are vendored under <code>assets/fonts/</code>
(SIL Open Font Licence) rather than fetched from a third party, for the same reason the rest of the site
vendors its code.</p></div>
</main>

<div class="mockwrap">
  <p class="mocklabel">Desktop &middot; 1440px &middot; scrolls sideways on a narrower screen</p>
  <div class="mockframe desk mock-desk">
{body_d}
  </div>
  <p class="mocklabel">Phone &middot; 390px</p>
  <div class="mockframe phone mock-phone">
{body_p}
  </div>
</div>

<main class="doc" style="max-width:min(1560px,97vw)">
<div class="agent"><h4>For an agent</h4><p>This page renders the chosen home-page design for pt.newsroom.sgit.ai,
a site that does not exist yet. The design sources are <code>/pt-newsroom/design/Main.dc</code> and
<code>/pt-newsroom/design/MainPhone.dc</code> (plain HTML artboards); the design system &mdash; colours,
faces, the order of the page, what is deliberately not on it &mdash; is section 16 of
<code>/documents/pt-newsroom.html</code>, the commissioning brief. The copy on the mock-up is the Portugal
section&rsquo;s data of 13 September 2026 and is not maintained: read <code>/portugal/data/</code> for
current facts. Nothing here is a claim about the world; it is a picture of a page.</p></div>
</main>

<footer class="site"><div class="cols"></div></footer>
</body>
</html>
"""
    (SEC / "index.html").write_text(page, encoding="utf-8")
    print(f"pt-newsroom: index.html written from Main.dc + MainPhone.dc ({len(page):,} bytes)")


if __name__ == "__main__":
    main()
