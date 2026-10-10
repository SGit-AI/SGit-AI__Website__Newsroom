#!/usr/bin/env python3
"""The archive: what this site said before the newsroom ran, kept, dated and labelled.

    python3 admin/build/archive.py --snapshot   # once, before the newsroom import
    python3 admin/build/archive.py              # every release: banners and the index

On 10 October 2026 this site stopped being an argument about a newsroom and became one.
Most of what it published before then was a design, an experiment or the material it was
built from. Much of that has since been overtaken by something that runs. None of it is
deleted.

Archiving a page here means three things, and moving it is not one of them:

  1. It keeps its address. LinkedIn posts, the World News Day vault and other sites link
     to these pages, and a link that breaks is a correction that cannot propagate, which
     is this site's own first argument.
  2. It carries a dated note at the top saying when it was written, why it is in the
     archive and what overtook it. The page below the note is unchanged.
  3. It leaves the main navigation and is listed in /archive/ instead.

The exception is a page whose ADDRESS now means something else: the home page, the
"how it runs" page and the "what is shipped" page. Those are copied, once, into archive/
under the date they were first written, and the copy is what carries the note. SNAPSHOTS
names them. sync_newsroom.py refuses to replace any of them until the copy exists.
"""
import argparse
import html
import posixpath
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

sys.path.insert(0, str(Path(__file__).parent))
from page import newsroom_page, write, HOST  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
ARCHIVED_ON = "10 October 2026"
FROM_VERSION = "v0.5.5"

# Pages whose address now carries something else. Copied once, before the import.
SNAPSHOTS = [
    {"from": "index.html",          "to": "archive/2026-08-22-home.html"},
    {"from": "index.md",            "to": "archive/2026-08-22-home.md"},
    {"from": "newsroom/index.html", "to": "archive/2026-08-23-newsroom-roles-and-operations.html"},
    {"from": "shipped/index.html",  "to": "archive/2026-08-23-what-is-shipped.html"},
]

# What is in the archive, in the order the archive lists it. A path ending in / is a whole
# section. `now` is what overtook it: (label, path from the site root, or a full URL).
GROUPS = [
    ("What this site said before the newsroom ran", [
        {"path": "archive/2026-08-22-home.html", "title": "The home page, 22 August to 10 October 2026",
         "written": "22 August 2026",
         "what": "The front page while this site was an argument: the thesis, the four things that ran, and a strip of release news.",
         "why": "The front page is now the newsroom's.",
         "now": [("The front page", "index.html")]},
        {"path": "archive/2026-08-23-what-is-shipped.html", "title": "What is shipped, what is argued (August 2026)",
         "written": "23 August 2026",
         "what": "The line between what ran and what was only argued, drawn when nothing ran.",
         "why": "It said nothing on this site was running. That stopped being true; the line is redrawn at the same address.",
         "now": [("What runs, what is designed", "shipped/index.html")]},
        {"path": "archive/2026-08-23-newsroom-roles-and-operations.html", "title": "The newsroom: roles and operations, as designed",
         "written": "23 August 2026",
         "what": "The newsroom as a design: the roles people and agents would hold, and how work would move between them.",
         "why": "The newsroom now runs, with six roles working under written behaviour policies, a board and a public log.",
         "now": [("How it runs", "newsroom/index.html")]},
    ]),
    ("The instances, as they ran", [
        {"path": "governance/", "title": "The Governance Wire",
         "written": "28 August 2026",
         "what": "A fully agentic publication over what regulators publish: seven agent roles, a graph, a source register and a point-and-click newsroom floor.",
         "why": "It made one research run, on 28 August 2026, and its verification layer was designed and never built. Its method now runs in the World News Day corpus and the newsroom.",
         "now": [("The AI governance stack, as a graph", "articles/the-ai-governance-stack-as-a-graph.html"),
                 ("How it runs", "newsroom/index.html")]},
        {"path": "portugal/", "title": "Portugal Startups",
         "written": "13 September 2026",
         "what": "The Portuguese startup ecosystem from primary sources, built around Startup Summit Lisbon 2026: frozen and hashed sources, a graph of 329 nodes, three stories, a named human editor.",
         "why": "The event is over, and the beat has its own site, which took the method and the evidence from here.",
         "now": [("pt.newsroom.sgit.ai", "https://pt.newsroom.sgit.ai/")]},
        {"path": "pt-newsroom/", "title": "pt.newsroom.sgit.ai: the home-page designs",
         "written": "13 September 2026",
         "what": "Four home-page directions for the Portuguese-language newsroom, and the one chosen, drawn with real data.",
         "why": "The site they were drawn for now exists.",
         "now": [("pt.newsroom.sgit.ai", "https://pt.newsroom.sgit.ai/")]},
        {"path": "mvps/index.html", "title": "The MVPs: publication instances",
         "written": "25 August 2026",
         "what": "The small publications the design material named in April and May 2026, as specified.",
         "why": "Some were built, differently; the rest are the record of what was planned. What can be copied today is on the replication page.",
         "now": [("Replicate this newsroom", "replicate/index.html")]},
        {"path": "mvps/portugal.html", "title": "The Portugal instance, as specified",
         "written": "25 August 2026",
         "what": "A bilingual daily on a knowledge-graph backbone, eleven agent roles and a thirty-day plan.",
         "why": "It was built differently, as Portugal Startups and then as its own site.",
         "now": [("pt.newsroom.sgit.ai", "https://pt.newsroom.sgit.ai/")]},
    ]),
    ("Design pages the newsroom has overtaken", [
        {"path": "provenance/show-your-work.html", "title": "Show your work",
         "written": "23 August 2026",
         "what": "Fifteen newsroom departments, each a public page.",
         "why": "The newsroom that runs shows its work with six roles, their policies, a board and a run log.",
         "now": [("How it runs", "newsroom/index.html")]},
        {"path": "provenance/a-worked-story.html", "title": "A worked story: &pound;8.40",
         "written": "23 August 2026",
         "what": "One story's production cost, sources and time, itemised as a design.",
         "why": "The newsroom now publishes what its own articles actually took.",
         "now": [("How much of this did I write?", "articles/how-much-of-this-did-i-write.html")]},
        {"path": "economics/paying-the-fact-creator.html", "title": "Contextual validation, not truth",
         "written": "23 August 2026",
         "what": "The long form of the economics argument, with the 60/25/10/5 upstream split worked through.",
         "why": "The concept page keeps the argument. The split has never been tested; the reading meter has.",
         "now": [("Paying the fact creator", "economics/index.html"),
                 ("Pay after you read", "articles/pay-after-you-read.html")]},
        {"path": "economics/rails.html", "title": "The payment rails",
         "written": "23 August 2026",
         "what": "x402 and the other machine-payment rails, as they stood in August 2026.",
         "why": "Market facts with a date on them. The newsroom took another route: a reading meter in the browser, with a card top-up planned.",
         "now": [("Going live with the reading meter", "articles/going-live-with-the-reading-meter.html")]},
        {"path": "corrections/242-papers.html", "title": "242 papers",
         "written": "23 August 2026",
         "what": "A second worked case for the corrections argument: one biomedical belief, 242 papers, 675 citations.",
         "why": "The design keeps one worked case, the 10,000-hours claim.",
         "now": [("The claim that would not die", "corrections/the-claim-that-would-not-die.html")]},
        {"path": "corrections/staleness-in-the-wild.html", "title": "Staleness in the wild",
         "written": "23 August 2026",
         "what": "The EU AI Act's consolidated text, dated two years behind the law, as observed in August 2026.",
         "why": "A dated observation, and the Governance Wire's lead story, which is archived with it.",
         "now": [("Corrections must propagate", "corrections/index.html")]},
        {"path": "corrections/agenda-is-context.html", "title": "Agenda is context",
         "written": "23 August 2026",
         "what": "An essay on disclosing an agenda rather than dismissing a claim for having one.",
         "why": "This site's own disclosure is the participant page, which stays.",
         "now": [("Where we lose: the disclosure", "about/participant.html")]},
    ]),
    ("The material this site was built from", [
        {"path": "documents/", "title": "The brief pack and the research briefs",
         "written": "21 August to 14 September 2026",
         "what": "What this site was asked to be in August 2026, before any of it ran, and the briefs written for pt.newsroom.",
         "why": "It is the origin record. The markdown sources stay in briefs/ in the repository.",
         "now": [("The design, and what runs", "design/index.html")]},
        {"path": "library/index.html", "title": "The library: 2025 to 2026",
         "written": "23 August 2026 (the articles: February to October 2025)",
         "what": "Ten articles, 68,846 words, published at docs.diniscruz.ai in 2025.",
         "why": "Where the ideas started. The live argument is now the newsroom's articles.",
         "now": [("Every article", "articles/index.html")]},
        {"path": "economics/micro-and-nano-payments.html", "title": "Micro and nano payments (2025)",
         "written": "23 August 2026 (the article: 2 April 2025)",
         "what": "The longest treatment of paying for news in pence, written fifteen months before any payment rail for it existed.",
         "why": "Prior art. The newsroom's reading meter is what that argument became.",
         "now": [("A meter in the browser", "articles/a-meter-in-the-browser.html")]},
    ]),
]

ENTRIES = [e for _, es in GROUPS for e in es]
START, END = "<!--archived-->", "<!--/archived-->"


def entry_for(rel):
    for e in ENTRIES:
        p = e["path"]
        if rel == p or (p.endswith("/") and rel.startswith(p)):
            return e
    return None


def href(target, up):
    return target if target.startswith("http") else up + target


def note(e, rel):
    up = "../" * rel.count("/")
    now = " &middot; ".join(f'<a href="{href(h, up)}">{l}</a>' for l, h in e["now"])
    return (f'{START}<div class="archived-note" role="note" style="max-width:1100px;margin:1rem auto 0;'
            f'padding:.75rem 1rem;border:1px solid #d6c79c;border-left:4px solid #b08d2c;background:#fbf7ea;'
            f'border-radius:6px;font-size:.9rem;line-height:1.55;color:#33301f">'
            f'<b>In the archive since {ARCHIVED_ON}.</b> Written {e["written"]}. {e["why"]} '
            f'The page is kept at the address it was published at, unchanged below this note. '
            f'<b>Now:</b> {now} &middot; <a href="{up}archive/index.html">the archive</a></div>{END}')


def stamp(path, rel, e):
    t = path.read_text(encoding="utf-8")
    # The note goes in with a newline before it, so it comes out with that newline too, or
    # every release would leave one more blank line behind on every archived page.
    t = re.sub(r"\n?" + re.escape(START) + r".*?" + re.escape(END), "", t, flags=re.S)
    if e:
        m = re.search(r'<nav class="site">.*?</nav>', t, re.S)
        if not m:
            raise SystemExit(f"archive: {rel} has no site nav to place the note after")
        t = t[:m.end()] + "\n" + note(e, rel) + t[m.end():]
    if t != path.read_text(encoding="utf-8"):
        path.write_text(t, encoding="utf-8")
        return True
    return False


# --- snapshots ------------------------------------------------------------------------

def rebase(url, src, dest, remap):
    if not url or url.startswith(("#", "//")) or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", url) \
            or re.search(r"['+{}<>$\s]", url):
        return url
    parts = urlsplit(url)
    if not parts.path:
        return url
    target = posixpath.normpath(posixpath.join(posixpath.dirname(src), parts.path))
    if target.startswith(".."):
        return url
    target = remap.get(target, target)
    new = posixpath.relpath(target, posixpath.dirname(dest) or ".")
    return urlunsplit(("", "", new, parts.query, parts.fragment))


def snapshot():
    remap = {s["from"]: s["to"] for s in SNAPSHOTS}
    done = 0
    for s in SNAPSHOTS:
        src, dest = ROOT / s["from"], ROOT / s["to"]
        if dest.exists():
            continue
        t = src.read_text(encoding="utf-8")
        if "data-root=" in t[:400]:
            raise SystemExit(f"archive: {s['from']} is already the imported page; the page this site "
                             f"wrote there is in git history at {FROM_VERSION}, not on disk")
        if s["from"].endswith(".html"):
            t = re.sub(r'\b(href|src|data-src)="([^"]*)"',
                       lambda m: f'{m.group(1)}="{rebase(m.group(2), s["from"], s["to"], remap)}"', t)
            t = re.sub(r'(<link rel="canonical" href=")[^"]*(")', rf'\1https://{HOST}/{s["to"]}\2', t, count=1)
            t = re.sub(r'(<meta property="og:url" content=")[^"]*(")', rf'\1https://{HOST}/{s["to"]}\2', t, count=1)
        else:
            t = re.sub(r'(\]\()([^)\s]+)', lambda m: m.group(1) + rebase(m.group(2), s["from"], s["to"], remap), t)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(t, encoding="utf-8")
        done += 1
        print(f"  snapshot {s['from']} -> {s['to']}")
    print(f"archive --snapshot: {done} copied, {len(SNAPSHOTS) - done} already held")


# --- the archive index ----------------------------------------------------------------

def title_of(rel):
    p = ROOT / rel
    if not p.exists():
        return None
    m = re.search(r"<title>(.*?)</title>", p.read_text(encoding="utf-8"), re.S)
    return re.sub(r"\s*(&middot;|·).*$", "", m.group(1)).strip() if m else None


def index_page():
    rows_by_group = []
    for heading, es in GROUPS:
        rows = []
        for e in es:
            p = e["path"]
            if p.endswith("/"):
                pages = sorted(x for x in (ROOT / p).rglob("*.html")
                               if "summit-archive" not in x.parts)
                link = f'../{p}index.html'
                count = f'<br><span class="small dim">{len(pages)} pages</span>'
            else:
                link, count = f"../{p}", ""
            now = "<br>".join(f'<a href="{href(h, "../")}">{l}</a>' for l, h in e["now"])
            rows.append(f'<tr><td><a href="{link}"><b>{e["title"]}</b></a>{count}</td>'
                        f'<td>{e["written"]}</td><td>{e["what"]}</td><td>{e["why"]}</td><td>{now}</td></tr>')
        rows_by_group.append(
            f'<h2>{heading}</h2>\n<div class="tablewrap"><table>'
            f'<thead><tr><th>Page</th><th>Written</th><th>What it was</th><th>Why it is here</th><th>Now</th></tr></thead>'
            f'<tbody>{"".join(rows)}</tbody></table></div>')
    total = sum(len([x for x in (ROOT / e["path"]).rglob("*.html") if "summit-archive" not in x.parts])
                if e["path"].endswith("/") else 1 for e in ENTRIES)
    body = f"""<div class="note"><b>Nothing here was deleted, and nothing here moved.</b> Every page keeps
the address it was published at, so the links into it still work, and each one carries a dated note
saying why it is here and what overtook it. The page below that note is as it was. {total} pages are
in the archive; the newsroom and the design pages that still stand are not.</div>
{chr(10).join(rows_by_group)}
<p class="small dim">The archive was made in release {FROM_VERSION} &rarr; the next, on {ARCHIVED_ON}.
Every earlier state of every page is in the <a href="https://github.com/SGit-AI/SGit-AI__Website__Newsroom">repository</a>
history, and every release is in the <a href="../admin/versions.html">release history</a>.</p>"""
    return newsroom_page(
        "archive/index.html", "The archive",
        "What this site said before the newsroom ran: the first home page, the designs the running "
        "newsroom has overtaken, the instances as they ran, and the material it was built from. Dated, "
        "labelled, and kept at their original addresses.",
        body, eyebrow="newsroom.sgit.ai &middot; the record",
        lead="Between 22 August and 10 October 2026 this site argued for a newsroom, specified it, and "
             "tried parts of it. Then the newsroom ran. This is what it said on the way, kept, dated, and "
             "labelled with what overtook each part.",
        agent="Pages listed here are historical. Each states its own date and what overtook it in a note "
              "at the top. Do not describe anything on an archived page as current, running or planned "
              "without checking the page it points to under <b>Now</b>. The current line between what "
              "runs and what is designed is at <a href=\"../shipped/index.html\">/shipped/</a>.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--snapshot", action="store_true", help="copy the replaced pages into archive/ (once)")
    args = ap.parse_args()
    if args.snapshot:
        snapshot()
        return
    missing = [e["path"] for e in ENTRIES if not (ROOT / e["path"]).exists()]
    if missing:
        raise SystemExit(f"archive: listed but not on disk: {', '.join(missing)}")
    changed = []
    for path in sorted(ROOT.rglob("*.html")):
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith((".git/", "briefs/")) or "vault-app" in path.parts or rel == "archive/index.html":
            continue
        e = entry_for(rel)
        t = path.read_text(encoding="utf-8")
        if e is None and START not in t:
            continue
        if stamp(path, rel, e):
            changed.append(rel)
    if write("archive/index.html", index_page()):
        changed.append("archive/index.html")
    stamped = sum(1 for p in ROOT.rglob("*.html") if START in p.read_text(encoding="utf-8", errors="ignore"))
    print(f"archive: {stamped} pages carry the archive note; {len(changed)} file(s) updated")


if __name__ == "__main__":
    main()
