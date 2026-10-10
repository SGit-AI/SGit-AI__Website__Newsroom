#!/usr/bin/env python3
"""The single definition of this site's nav and footer, and the tool that applies it.

Run from anywhere: python3 admin/build/chrome.py

Every page is hand-written static HTML — that stays true, because a human should be
able to open any file and edit it. What is NOT hand-maintained is the chrome: the nav
row (including the version badge that validate.js requires to agree everywhere) and
the footer columns. Those are defined once here and rewritten in place across the
tree, which is what stops the site from drifting as it grows.

Adding a page: add it to NAV or FOOTER if it belongs there, write the file with any
nav/footer block at all, then run this. The block contents are replaced; the `here`
state is set from the page's own path.
"""
import re
import sys
from pathlib import Path

ROOT    = Path(__file__).resolve().parents[2]
VERSION = (ROOT / "admin/build/version.txt").read_text().strip()
GH      = "https://github.com/SGit-AI/SGit-AI__Website__Newsroom"
PARENT  = "https://sgit.ai"
PARENT_TITLE = ("sgit.ai — the parent project: the vault layer and the shipped CLI. "
                "This site is the future-of-news stack: provenance, corrections, "
                "and paying the fact creator")

# The nav, two levels. Each entry is (label, own page, [(sub-label, href), ...], (path prefixes)).
#
#   · A group label is always a link to a real page, never a menu-only stub.
#   · `prefixes` decides the "here" state, so a page not itself in the nav still
#     lights up the group it belongs to.
#
# Since v0.6.0 the order is the reader's, not the argument's: the newsroom first, then the
# reader's own account (what they read, what it costs, the newsroom it builds for them), then
# how the newsroom runs, then the design it comes from, then how to build one yourself. The
# one instance still running as its own section, World News Day, keeps its group because
# the people its outreach writes to land on it. Everything this site published before the
# newsroom ran is in the archive, which is dated and kept at its original addresses
# (admin/build/archive.py).
NAV = [
    ("Newsroom", "index.html", [
        ("Front page", "index.html"),
        ("Newsletter", "articles/newsletter/index.html"),
        ("Every article", "articles/index.html#all"),
        ("Collections", "articles/collections/index.html"),
        ("From the desk", "articles/desk/index.html"),
        ("As graphs", "articles/graphs.html"),
        ("Subscribe", "subscribe/index.html"),
    ], ("articles/", "subscribe/")),
    ("Account", "account/index.html", [
        ("Your reading account", "account/index.html"),
        ("Your newsroom", "account/newsroom.html"),
        ("A newsroom designed for you", "account/share.html"),
        ("Your personas", "account/personas.html"),
        ("Top up", "account/top-up.html"),
    ], ("account/",)),
    ("How it runs", "newsroom/index.html", [
        ("How the newsroom runs", "newsroom/index.html"),
        ("The roles", "newsroom/index.html#roles"),
        ("Behaviour policies", "newsroom/policies.html"),
        ("How to publish", "newsroom/publish.html"),
        ("The board", "newsroom/board.html"),
        ("The run log", "newsroom/log.html"),
    ], ("newsroom/",)),
    ("Design", "design/index.html", [
        ("The design, and what runs", "design/index.html"),
        ("The thesis: sell the graph", "thesis/index.html"),
        ("Corrections must propagate", "corrections/index.html"),
        ("Provenance is the product", "provenance/index.html"),
        ("Paying the fact creator", "economics/index.html"),
        ("Content rights: CC-Signed", "rights/index.html"),
        ("Databases with no server", "databases/index.html"),
        ("What runs, what is designed", "shipped/index.html"),
    ], ("design/", "thesis/", "corrections/", "provenance/", "economics/", "rights/",
        "databases/", "shipped/")),
    ("Replicate", "replicate/index.html", [
        ("Replicate this newsroom", "replicate/index.html"),
        ("SG Meter: the reading meter", "meter/index.html"),
        ("The meter's security model", "meter/security.html"),
        ("Seed companies", "mvps/seed-companies.html"),
        ("How this site is built", "admin/index.html"),
    ], ("replicate/", "meter/", "mvps/seed-companies.html")),
    ("World News Day", "world-news-day/index.html", [
        ("The corpus", "world-news-day/index.html"),
        ("Free to republish is not a licence", "world-news-day/stories/free-to-republish-is-not-a-licence.html"),
        ("The licence that is not there", "world-news-day/licences.html"),
        ("The twenty-one", "world-news-day/corpus.html"),
        ("The aggregate", "world-news-day/findings.html"),
        ("The vocabulary", "world-news-day/terms.html"),
        ("The graph", "world-news-day/graph.html"),
        ("Sources", "world-news-day/sources.html"),
        ("How to reach them", "world-news-day/contacts.html"),
        ("Published vaults", "world-news-day/vault.html"),
        ("The vault, opened", "world-news-day/vaults/corpus.html"),
        ("Method", "world-news-day/method.html"),
    ], ("world-news-day/",)),
    ("Archive", "archive/index.html", [
        ("The archive", "archive/index.html"),
        ("The first home page (Aug 2026)", "archive/2026-08-22-home.html"),
        ("The Governance Wire (Aug 2026)", "governance/index.html"),
        ("Portugal Startups (Sep 2026)", "portugal/index.html"),
        ("The brief pack (Aug 2026)", "documents/index.html"),
        ("The library: prior art (2025)", "library/index.html"),
    ], ("archive/", "governance/", "portugal/", "pt-newsroom/", "documents/", "library/",
        "mvps/index.html", "mvps/portugal.html")),
    ("About", "about/participant.html", [
        ("Where we lose: the disclosure", "about/participant.html"),
        ("The network", "network/index.html"),
        ("Release history", "admin/versions.html"),
        ("Admin &amp; engineering", "admin/index.html"),
        ("Comms: tasks &amp; requests", "admin/comms.html"),
    ], ("about/", "network/", "admin/")),
]

FOOTER = [
    ("The newsroom", [
        ("&#8594; The front page", "index.html"),
        ("Every article", "articles/index.html#all"),
        ("The newsletter", "articles/newsletter/index.html"),
        ("Collections", "articles/collections/index.html"),
        ("From the desk", "articles/desk/index.html"),
        ("As graphs", "articles/graphs.html"),
        ("Subscribe", "subscribe/index.html"),
        ("The feed", "articles/feed.xml"),
    ]),
    ("Your account", [
        ("Your reading account", "account/index.html"),
        ("Your newsroom", "account/newsroom.html"),
        ("Your personas", "account/personas.html"),
        ("Top up", "account/top-up.html"),
    ]),
    ("How it runs", [
        ("How the newsroom runs", "newsroom/index.html"),
        ("Behaviour policies", "newsroom/policies.html"),
        ("How to publish", "newsroom/publish.html"),
        ("The board", "newsroom/board.html"),
        ("The run log", "newsroom/log.html"),
    ]),
    ("The design", [
        ("The design, and what runs", "design/index.html"),
        ("The thesis: sell the graph", "thesis/index.html"),
        ("Corrections must propagate", "corrections/index.html"),
        ("Provenance is the product", "provenance/index.html"),
        ("Paying the fact creator", "economics/index.html"),
        ("What runs, what is designed", "shipped/index.html"),
    ]),
    ("Build your own", [
        ("Replicate this newsroom", "replicate/index.html"),
        ("SG Meter: the reading meter", "meter/index.html"),
        ("World News Day 2026: the corpus", "world-news-day/index.html"),
        ("The method: fetch, freeze, hash", "world-news-day/method.html"),
        ("Seed companies", "mvps/seed-companies.html"),
    ]),
    ("Site", [
        ("The archive", "archive/index.html"),
        ("The network", "network/index.html"),
        ("Release history", "admin/versions.html"),
        ("Admin &amp; engineering", "admin/index.html"),
        ("Where we lose", "about/participant.html"),
        ("llms.txt", "llms.txt"),
    ]),
]

BLURB = ("The SGit Newsroom: one page, one argument, with the figures, the data and the links "
         "to check it. Articles by Dinis Cruz, written from his voice notes by an agent working "
         "as the newsroom; the roles and the rules they work under are public. The method is "
         "published so that anyone can run a newsroom like it. Part of the "
         "<a href=\"https://sgit.ai\" style=\"display:inline;padding:0\"><b>sgit.ai</b></a> "
         "network. All content CC BY 4.0 unless a page states otherwise.")
PARTNOTE = ('&#9888; Participant disclosure: published by the sgit project, which is '
            'building the stack this site argues for. '
            '<a href="{up}about/participant.html" style="display:inline;padding:0">'
            'Read the disclosure</a>.')
PARTNOTE_SELF = '&#9888; Participant disclosure: published by the sgit project. You are on the disclosure page.'
# Inline on purpose: the newsroom stylesheet sets footer links to display:block, which put
# each site of the network on its own line with a stray separator between them.
_NET = 'style="display:inline;padding:0"'
NETLINE = (f'<a href="https://sgit.ai" {_NET}><b>&#8593; sgit.ai</b></a> &middot; '
           f'<a href="https://pt.newsroom.sgit.ai" {_NET}>&#8593; pt.newsroom.sgit.ai</a> &middot; '
           f'<a href="https://graphs.sgit.ai" {_NET}>&#8593; graphs.sgit.ai</a> &middot; '
           f'<a href="https://pki.sgit.ai" {_NET}>&#8593; pki.sgit.ai</a> &middot; '
           f'<a href="https://nhi.sgit.ai" {_NET}>&#8593; nhi.sgit.ai</a> &middot; '
           f'<a href="https://docs.diniscruz.ai" {_NET}>&#8593; docs.diniscruz.ai</a> &mdash; the prior art')


def newsroom_style(text):
    """A page in the newsroom's look: imported from sgit.ai (its <html> carries data-root),
    or written here on assets/newsroom.css. Its nav must not load nav.js, because site.js
    already wires the same menu button, and two handlers on one toggle open and close it in
    the same click."""
    return 'data-root="' in text[:600] or "assets/newsroom.css" in text


def md_twin_of(text):
    m = re.search(r'<link rel="alternate" type="text/markdown" href="([^"]+)"', text)
    return m.group(1) if m else None


def nav_html(rel, up, newsroom=False, meter=False):
    groups = []
    for label, own, subs, prefixes in NAV:
        active = rel == own or any(rel.startswith(pre) for pre in prefixes)
        links = "\n".join(
            f'      <a class="sl{" here" if href == rel else ""}" href="{up}{href}">{text}</a>'
            for text, href in subs)
        groups.append(
            f'    <div class="ni ni-has">\n'
            f'      <a class="nl{" here" if active else ""}" href="{up}{own}">{label}'
            f'<span class="caret">&#9662;</span></a>\n'
            f'      <div class="sub">\n{links}\n      </div>\n'
            f'    </div>')
    rows = "\n".join(groups)
    # The "part of sgit.ai" link is the legacy look's. In the newsroom look it is the item that
    # pushes the row onto two lines at 1440px, and the footer's network line already says it.
    parent = ('' if newsroom else
              f'  <a class="parent" href="{PARENT}" title="{PARENT_TITLE}">&#8593; part of <b>sgit.ai</b></a>\n')
    return (f'<nav class="site"><div class="row">\n'
            f'  <a class="brand" href="{up}index.html">newsroom<span>.sgit.ai</span></a>\n'
            + parent +
            f'  <a class="ver" href="{up}admin/versions.html" title="Site release history">{VERSION}</a>\n'
            + (f'  <sg-meter class="meter-nav" view="balance"></sg-meter>\n' if meter else '')
            + f'  <button class="nav-toggle" type="button" aria-expanded="false" aria-label="Menu">Menu</button>\n'
            f'  <div class="nav-items">\n{rows}\n  </div>\n'
            f'  <a class="gh" href="{GH}">&#9733; GitHub</a>\n'
            + ('' if newsroom else f'  <script src="{up}assets/nav.js" defer></script>\n')
            + '</div></nav>')


def footer_html(rel, up, twin=None):
    partnote = PARTNOTE_SELF if rel == "about/participant.html" else PARTNOTE.format(up=up)
    if twin is None and rel == "index.html":
        twin = "index.md"
    md_twin  = f' &middot; <a href="{twin}">this page as markdown</a>' if twin else ""
    cols = "\n".join(
        "  <div>\n"
        f"    <h4>{head}</h4>\n"
        + "\n".join(f'    <a href="{l if l.startswith("http") else up + l}">{t}</a>' for t, l in links)
        + "\n  </div>"
        for head, links in FOOTER)
    return (f'<footer class="site"><div class="cols">\n'
            f'  <div>\n'
            f'    <div class="brandline">newsroom<span>.sgit.ai</span></div>\n'
            f'    <p>{BLURB}</p>\n'
            f'    <p class="netline">{NETLINE}</p>\n'
            f'    <p class="partnote">{partnote}</p>\n'
            f'    <p class="verline">site <a href="{up}admin/versions.html">{VERSION}</a> &middot; '
            f'<a href="{up}admin/index.html">engineering</a>{md_twin}</p>\n'
            f'  </div>\n{cols}\n</div></footer>')


def stamp_text_twins():
    """The version also appears in llms.txt and index.md, and validate.js enforces that
    it agrees. Own it here rather than hand-editing it every release."""
    out = []
    llms = ROOT / "llms.txt"
    if llms.exists():
        t = llms.read_text()
        t2, n = re.subn(r"Site version: v\d+\.\d+\.\d+", f"Site version: {VERSION}", t, count=1)
        if n and t2 != t:
            llms.write_text(t2)
            out.append("llms.txt")
    md = ROOT / "index.md"
    if md.exists():
        # index.md is markdown, so the separator is a literal U+00B7, not an HTML entity.
        # Getting that wrong makes this a silent no-op and the version stamp never lands;
        # the mismatch below is reported rather than swallowed for exactly that reason.
        t = md.read_text()
        t2, n = re.subn(r"\u00b7 site v\d+\.\d+\.\d+ \u00b7", f"\u00b7 site {VERSION} \u00b7", t, count=1)
        if n and t2 != t:
            md.write_text(t2)
            out.append("index.md")
    return out


def main():
    changed = []
    for path in sorted(ROOT.rglob("*.html")):
        if ".git" in path.parts:
            continue
        # An archive holds pages AS THEY WERE SERVED at a version, with that version's nav,
        # footer and badge. Restamping them with today's chrome would destroy the only thing an
        # archive is for, and it silently did exactly that the first time briefs/summit-archive/
        # existed. Copies of pages are not pages.
        if "summit-archive" in path.parts:
            continue
        # world-news-day/vault-app/ is the app that ships inside the encrypted vault. It has no
        # nav or footer by design — it renders in the SG/Send host from the vault's bytes, not
        # on this domain — so stamping site chrome into it would corrupt it.
        if "vault-app" in path.parts:
            continue
        rel  = path.relative_to(ROOT).as_posix()
        up   = "../" * (len(path.relative_to(ROOT).parts) - 1)
        text = path.read_text()
        before = text
        styled = newsroom_style(text)
        meter  = "sg-meter.js" in text
        text, n_nav  = re.subn(r'<nav class="site">.*?</nav>', lambda _: nav_html(rel, up, styled, meter),
                               text, count=1, flags=re.S)
        text, n_foot = re.subn(r'<footer class="site">.*?</footer>',
                               lambda _: footer_html(rel, up, md_twin_of(text)),
                               text, count=1, flags=re.S)
        # The agent chip on an imported page carries the release that built it. Here that is
        # this site's release, and llms.txt is this site's, so the stamp is this site's too.
        text = re.sub(r'<span class="llmschip-m">[^<]*</span>',
                      f'<span class="llmschip-m">{VERSION}</span>', text, count=1)
        if not n_nav or not n_foot:
            missing = " and ".join(x for x in (("nav" if not n_nav else ""),
                                               ("footer" if not n_foot else "")) if x)
            print(f"  ! {rel}: missing {missing} block", file=sys.stderr)
        if text != before:
            path.write_text(text)
            changed.append(rel)
    changed += stamp_text_twins()
    print(f"chrome: {VERSION} applied — {len(changed)} file(s) updated")
    for c in changed:
        print(f"  · {c}")


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        sys.stdout = None
