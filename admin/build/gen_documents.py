#!/usr/bin/env python3
"""Generates documents/*.html — the in-page reader for every raw document under briefs/.

Run from anywhere: python3 admin/build/gen_documents.py
Then run chrome.py, which fills in the nav and footer.

The convention, inherited from graphs.sgit.ai, pki.sgit.ai and sg-sentinel.sgit.ai:
**the raw markdown under /briefs/ is the source of truth; the rendered page is
presentation.** Every reader page says so, links the raw file, and renders it
client-side from that same file — so a reader page can never drift from the document
it claims to render.

The markdown parser is **vendored** at assets/vendor/marked.min.js rather than pulled
from a CDN, which is where this site departs from its siblings. They load marked from
jsdelivr; this is the site arguing that an evidence chain should not terminate in a
single third-party resource that could move, change or disappear — so depending on one
in order to read its own source documents would have been the argument refuting itself.
35KB, MIT, attributed in LICENSES.md.

On this site that convention is not just tidy, it is the argument. This is the site
whose central claim is that most articles do not provide evidence, they provide a
link, and the link is never followed. Handing a reader a raw .md file and calling it
"the source" is the lazy version of that failure. The document has to be *readable*
where the reader already is, with its provenance stated, and still one click from the
byte-for-byte original.

Adding a document: drop the .md into briefs/, add a row to DOCS, run this, run
chrome.py, add the page to sitemap.xml, and bump the version.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GH   = "https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/briefs"

# slug, source file, title, kind, the single most important fact in it, why it is on the site
DOCS = [
    ("brief", "00__BRIEF.md", "The brief",
     "Brief · v1.0 · 21 August 2026",
     "Why <code>newsroom</code> and not <code>news</code>: the corpus names this domain to "
     "itself as “the future-of-news stack” 21 times, but the material is overwhelmingly "
     "about how news gets made, proven and paid for — and a site called <em>news</em> is a "
     "research site, while a site called <em>newsroom</em> can become a running newsroom "
     "without a rename.",
     "The document this site was built from. The eight themes, the four numbers, the "
     "ten-step build order and the honesty constraint all come from here — and "
     "<a href=\"../shipped/index.html\">/shipped/</a> exists because of §6."),

    ("thesis-and-themes", "01__thesis-and-themes.md", "The thesis, eight themes and the quote bank",
     "Quote bank · v1.0 · 21 August 2026",
     "Thirty-plus sourced quotations with their originating brief paths, and every citable "
     "figure on this site — the 10,000-hours case, the 242-paper citation network, the "
     "£8.40 story ledger and the x402 rail numbers.",
     "The spine of the site. Every quotation on a rendered page here comes from this "
     "document, with its source path and date attached."),

    ("source-provenance", "02__source-provenance-and-attribution.md", "The provenance contract",
     "Contract · v1.0 · 21 August 2026 · load-bearing",
     "A future-of-news site that loses its own provenance chain has refuted itself on page "
     "one — so <code>first_published</code> is always the ORIGINAL date, never the "
     "republication date, and <code>curation</code> must honestly be one of verbatim / "
     "edited / excerpted / synthesised.",
     "<b>The load-bearing file in the pack.</b> Every provenance block on this site follows "
     "its §1 fields and §2 visible rendering, and the pre-release gate enforces both — see "
     "<a href=\"../admin/index.html#gate\">what the gate checks</a>."),

    ("corpus-index", "03__corpus-index__send-repo.md", "The corpus, tiered by publishability",
     "Index · v1.0 · 21 August 2026",
     "Every news-relevant document in the source repository, tiered: Tier 0 publishable "
     "near-as-is, Tier 1 after de-scoping, Tier 2 cite-don't-republish because it belongs "
     "to a sibling site, and Tier 3 do-not-publish.",
     "The map of what was available and what was deliberately left out. Publishing the "
     "tiering as well as the result is the point — a reader can see what was excluded and "
     "disagree."),

    ("prior-art", "04__prior-art__docs-diniscruz-ai.md", "The prior art: ten published articles",
     "Index · v1.0 · 21 August 2026",
     "Ten core articles totalling 68,846 words were published between February and October "
     "2025 — a year before the design material behind the rest of this site was written, "
     "with every URL, PDF and LinkedIn post resolved live on 21 August 2026.",
     "The evidence that this site is the continuation of a dated, publicly-checkable "
     "thread rather than a launch. It is the source for "
     "<a href=\"../library/index.html\">/library/</a>."),

    ("site-architecture", "05__site-architecture.md", "The proposed site architecture",
     "Architecture · v1.0 · 21 August 2026",
     "A page-by-page information architecture in which <code>/corrections/</code> is built "
     "first, because it carries the most distinctive argument in the corpus and the "
     "10,000-hours story lands it with no technical background required.",
     "The IA this site is built against. Read it next to "
     "<a href=\"../admin/index.html\">/admin/</a> to see what was built, what was merged "
     "into a single hub page, and what is still outstanding as "
     "<a href=\"../admin/comms.html#tasks\">task T1</a>."),

    ("boundaries-and-house-style", "06__boundaries-and-house-style.md",
     "Boundaries, redaction and house style",
     "Conventions · v1.0 · 21 August 2026",
     "The largest risk to this site is not scarcity but duplication — and the Risk Mandate "
     "framing has to be inverted, because the same material published under a "
     "risk-management frame reads as a compliance feature and published here reads as a "
     "thesis about journalism.",
     "The source of <a href=\"../network/index.html\">/network/</a>, and of the redaction "
     "watch-list the gate now enforces so the exclusions are structural rather than a "
     "habit somebody could forget."),

    ("gaps-and-open-questions", "07__gaps-and-open-questions.md", "Gaps, open questions and honest tensions",
     "Gaps · v1.0 · 21 August 2026",
     "Seven open questions published unresolved and six honest tensions named against the "
     "site's own argument — including that provenance is the product <em>and</em> "
     "provenance is expensive, and that a graph which can answer what rests on corrected "
     "claims can also be subpoenaed for it.",
     "Every open question on <a href=\"../network/index.html#open\">/network/</a> and every "
     "outstanding request on <a href=\"../admin/comms.html\">/admin/comms/</a> comes from "
     "this document."),

    ("pack-readme", "README.md", "The pack readme",
     "Readme · v1.0 · 21 August 2026",
     "~110,000 words across three corpora, of which 68,846 are already public and dated — "
     "so this site launches as the continuation of a two-year publicly-checkable thread, "
     "and the provenance chain back to those originals is its first demonstration of its "
     "own thesis.",
     "The pack's own index and tier summary — the quickest way to see the shape of the "
     "whole source set."),

    ("public", "PUBLIC.md", "What was changed before publication",
     "Transparency note",
     "Nine redactions, in three files, each replaced with a visible marker — because the "
     "pack's own watch-list names its subjects in the course of forbidding their "
     "publication, so publishing it verbatim published exactly what it forbids.",
     "The transparency convention this network uses when republishing a source pack. It "
     "is also the record of a real defect on this site: the pack shipped unredacted in "
     "v0.2.0 because the gate exempted <code>briefs/</code>. It no longer does."),

    ("licence", "LICENSE.md", "The pack licence and its scope",
     "Licence · CC BY 4.0",
     "The pack is CC BY 4.0, but that grant does not extend to third-party material quoted "
     "within it, to the <code>docs.diniscruz.ai</code> source articles (CC0 1.0 at source), "
     "or to anything marked Tier 3.",
     "The licence position this site inherits, and the reason every republished section "
     "here states its source licence separately — see "
     "<a href=\"../about/participant.html#licence\">the participant disclosure</a>."),
]

HEAD = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title} &middot; newsroom.sgit.ai</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://newsroom.sgit.ai/documents/{slug}.html">
<meta property="og:type" content="article">
<meta property="og:site_name" content="newsroom.sgit.ai">
<meta property="og:url" content="https://newsroom.sgit.ai/documents/{slug}.html">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta name="twitter:card" content="summary">
<link rel="alternate" type="text/markdown" href="../briefs/{src}" title="The raw markdown, which is the source of truth">
<link rel="stylesheet" href="../assets/site.css">
</head>
<body>

<nav class="site"></nav>

<main class="doc">
<div class="crumb"><a href="../index.html">newsroom.sgit.ai</a> / <a href="index.html">documents</a> / {slug}</div>
<h1>{title}</h1>

<div class="docmeta">
  <span class="k">Kind</span><span class="v">{kind}</span>
  <span class="k">Pack</span><span class="v">newsroom.sgit.ai brief pack v1.0, 21 August 2026</span>
  <span class="k">Licence</span><span class="v">CC BY 4.0 &mdash; see <a href="licence.html">the scope note</a></span>
  <span class="k">Source</span><span class="v"><a href="../briefs/{src}">raw markdown</a> &middot; <a href="{gh}/{src}">view on GitHub</a></span>
</div>

<h2 id="fact">The single most important thing in it</h2>
<p class="lead">{fact}</p>

<h2 id="on-site">Why it is on this site</h2>
<p>{why}</p>

<h2 id="read">Read the document</h2>
<div class="mdread-label">&#128196; Rendered from the <a href="../briefs/{src}">raw markdown</a> &mdash; which is the source of truth. This page is presentation.</div>
<div class="mdread" id="mdread" data-src="../briefs/{src}"><noscript><p class="dim">In-page rendering needs JavaScript &mdash; <a href="../briefs/{src}">open the raw markdown</a>.</p></noscript></div>

<div class="pagenav">
  <a href="index.html">&larr; All documents</a>
  <a href="../briefs/{src}">Raw markdown &rarr;</a>
</div>
</main>

<footer class="site"></footer>
<script src="../assets/vendor/marked.min.js"></script>
<script src="../assets/mdreader.js" defer></script>
</body>
</html>
'''


def strip_tags(s):
    """The fact doubles as the meta description, where markup is not wanted."""
    out, depth = [], 0
    for ch in s:
        if ch == "<":
            depth += 1
        elif ch == ">":
            depth = max(0, depth - 1)
        elif depth == 0:
            out.append(ch)
    return "".join(out)


def main():
    out = ROOT / "documents"
    out.mkdir(exist_ok=True)
    written = []
    for slug, src, title, kind, fact, why in DOCS:
        if not (ROOT / "briefs" / src).exists():
            print(f"  ! briefs/{src} is missing", file=sys.stderr)
            continue
        desc = strip_tags(fact).replace('"', "&quot;").replace("\n", " ").strip()
        (out / f"{slug}.html").write_text(HEAD.format(
            slug=slug, src=src, title=title, kind=kind, fact=fact, why=why,
            desc=desc, gh=GH))
        written.append(f"documents/{slug}.html")
    print(f"gen_documents: {len(written)} reader page(s)")
    for w in written:
        print(f"  · {w}")


if __name__ == "__main__":
    main()
