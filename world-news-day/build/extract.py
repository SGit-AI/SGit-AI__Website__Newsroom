#!/usr/bin/env python3
"""world-news-day/build/extract.py — the ingestion path for the World News Day 2026 corpus.

    python3 world-news-day/build/extract.py [--fetch]

Same path as /portugal/: fetch -> freeze -> hash -> extract -> diff. The beat is the 21 op-eds
WAN-IFRA commissioned for World News Day (28 September 2026), published on worldnewsday.org and
announced as "free to republish". Two things are frozen per piece: the rendered HTML, and the
WordPress REST record the site serves for it. Without --fetch nothing touches the network and
everything is re-derived from the frozen bytes, which is the test of whether a corpus is anchored.

WHAT THIS SECTION IS FOR. Not to republish the op-eds — they are other people's writing and this
publication links rather than reproduces. It is to answer three questions the pieces themselves
cannot answer, because answering them means reading all 21 at once:

  1. Under what licence, exactly? They say "free to republish" in prose. Prose is not a licence.
  2. In what machine-readable form? A permission a machine cannot read is a permission that does
     not travel.
  3. What do they actually argue, and where do the arguments agree and disagree?

Every claim this section publishes about a piece points at the frozen bytes of that piece, and
the gates re-derive each one on every build.
"""
import argparse
import collections
import hashlib
import html
import json
import re
import subprocess
import time
import urllib.parse
from pathlib import Path

SEC = Path(__file__).resolve().parents[1]
DATA = SEC / "data"
FROZEN = SEC / "sources" / "frozen"
HOST = "https://worldnewsday.org"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"

# The 21, in the order the WAN-IFRA announcement lists them. That order is itself data: it is the
# commissioning organisation's own presentation of its authors.
SLUGS = [
    "the-integrity-dividend-the-value-of-knowing",
    "journalism-our-chaotic-worlds-future",
    "footballs-enduring-controversies-show-why-journalism-matters",
    "media-faces-violence-persecution-and-the-existential-threat-posed-by-ai-and-yet-we-are-still-here",
    "democracy-needs-journalism-in-every-language",
    "indias-students-found-their-voice-this-summer-while-journalists-are-losing-theirs",
    "dystopia-inc-would-you-like-your-news-with-or-without-hallucinations",
    "truth-in-an-ai-world",
    "a-lesson-from-ukraine-newsroom-resilience-makes-press-freedom-real",
    "free-press-needs-alliances-against-censorship-and-fragmentation",
    "thank-goodness-for-the-storytellers-the-ones-who-probe-question-irritate-the-powerful",
    "america-was-the-arsenal-of-democracy-now-its-disarming-the-press",
    "when-information-is-everywhere-and-the-reasons-to-give-up-are-so-many-journalism-matters-even-more",
    "remembering-9-11-as-a-local-news-story",
    "independent-news-media-need-more-than-short-term-funding",
    "nicaragua-reinventing-journalism-in-exile",
    "the-things-i-learned-from-my-daughters-a-central-bank-investigation-and-a-box-of-watermelon-gum",
    "the-role-of-the-news-media-in-fighting-the-climate-crisis",
    "journalism-is-civic-infrastructure-we-need-to-support-it",
    "we-must-make-truth-matter-again",
    "2026-world-news-day-time-to-fight",
]

# The announcement page. Frozen separately because its terms differ from the articles' terms, and
# that difference is one of this section's findings.
ANNOUNCEMENT = "https://wan-ifra.org/2026/09/world-news-day-21-great-op-eds-on-why-journalism-matters/"


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def strip(h):
    h = re.sub(r"<(script|style)\b.*?</\1>", " ", h, flags=re.S | re.I)
    return " ".join(html.unescape(re.sub(r"<[^>]+>", " ", h)).split())


def fetch(date):
    out = FROZEN / date
    (out / "api").mkdir(parents=True, exist_ok=True)
    for s in SLUGS:
        for url, dest in ((f"{HOST}/{s}/", out / f"{s}.snapshot"),
                          (f"{HOST}/wp-json/wp/v2/posts?slug={s}&_embed=1", out / "api" / f"{s}.json")):
            code = subprocess.run(["curl", "-sSL", "-A", UA, "--max-time", "45", "-o", str(dest),
                                   "-w", "%{http_code}", url], capture_output=True, text=True).stdout.strip()
            print(f"  {code}  {dest.relative_to(SEC)}")
            time.sleep(0.3)
    fetch_announcement(out)


def fetch_announcement(out, attempts=6):
    """The announcement, which sits behind a JavaScript-challenge WAF that answers SOME requests
    with a 307 and a 1.3 KB challenge instead of the page.

    Until v0.4.2 this was tried twice, refused twice, and published as "the one page in the beat
    a machine cannot read". That was too strong, and the correction is in data/corrections.json:
    the challenge is INTERMITTENT, and a seventh attempt returned the page. A refusal observed
    twice is evidence about two attempts, not a property of a page — so the attempts are counted
    now, each one recorded with the size and hash of whatever came back, and the loop stops at
    the first real page rather than at the first refusal."""
    log = []
    for i in range(attempts):
        r = subprocess.run(["curl", "-sSL", "-A", UA, "--max-time", "45",
                            "-o", str(out / "announcement.snapshot"),
                            "-w", "%{http_code}", ANNOUNCEMENT], capture_output=True, text=True)
        code = r.stdout.strip()
        f = out / "announcement.snapshot"
        size = f.stat().st_size if f.exists() else 0
        log.append({"attempt": i + 1, "http": code, "bytes": size,
                    "sha256": sha(f) if size else None,
                    "read": bool(code == "200" and size > 3000)})
        print(f"  {code}  announcement.snapshot ({size} bytes, attempt {i + 1})")
        if code == "200" and size > 3000:
            break
        time.sleep(2)
    (out / "announcement-attempts.json").write_text(
        json.dumps(log, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def snapshots():
    return sorted(d for d in FROZEN.iterdir() if d.is_dir())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fetch", action="store_true")
    ap.add_argument("--date", default=time.strftime("%Y-%m-%d"))
    a = ap.parse_args()
    if a.fetch:
        print(f"fetching {a.date}…")
        fetch(a.date)

    snaps = snapshots()
    if not snaps:
        raise SystemExit("no snapshots under world-news-day/sources/frozen/<date>/")
    latest = snaps[-1]
    today = latest.name

    # ---- the register -------------------------------------------------------------
    register = []
    for s in SLUGS:
        for rel, url, kind in ((f"{s}.snapshot", f"{HOST}/{s}/", "page"),
                               (f"api/{s}.json", f"{HOST}/wp-json/wp/v2/posts?slug={s}&_embed=1", "api")):
            f = latest / rel
            if not f.exists():
                continue
            register.append({"id": f"{today}/{rel}", "slug": s, "kind": kind, "url": url,
                             "frozen": f"sources/frozen/{today}/{rel}", "sha256": sha(f),
                             "bytes": f.stat().st_size,
                             "retrieved": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(f.stat().st_mtime)),
                             "publisher": "World News Day (WAN-IFRA / Canadian Journalism Foundation)"})
    ann = latest / "announcement.snapshot"
    excluded = []
    if ann.exists() and ann.stat().st_size > 3000:
        register.append({"id": f"{today}/announcement", "slug": None, "kind": "announcement",
                         "url": ANNOUNCEMENT, "frozen": f"sources/frozen/{today}/announcement.snapshot",
                         "sha256": sha(ann), "bytes": ann.stat().st_size,
                         "retrieved": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(ann.stat().st_mtime)),
                         "publisher": "WAN-IFRA"})
    else:
        excluded.append({"id": f"{today}/announcement", "url": ANNOUNCEMENT,
                         "why": ("wan-ifra.org is served through a JavaScript-challenge WAF that answers "
                                 "some automated requests with HTTP 307 and a 1.3 KB challenge page reading "
                                 "'Javascript is required' instead of the article. It is intermittent, and "
                                 "on this build every attempt was refused. No claim in this section stands "
                                 "on the announcement alone. See data/corrections.json: an earlier version "
                                 "of this section said the page could not be read by a machine at all, "
                                 "which was too strong.")})

    # ---- the corpus ----------------------------------------------------------------
    LIC_RE = re.compile(r"(This opinion piece was commissioned[^.]*\.)\s*(Free to republish.*?)(?:$|\s*$)", re.S)
    articles = []
    for order, s in enumerate(SLUGS, start=1):
        rec = json.load(open(latest / "api" / f"{s}.json", encoding="utf-8"))[0]
        page = (latest / f"{s}.snapshot").read_text(encoding="utf-8", errors="replace")
        body = strip(rec["content"]["rendered"])

        # the licence statement, verbatim, and the bio block that precedes it
        cut = body.find("This opinion piece was commissioned")
        licence = body[cut:].strip() if cut > 0 else None
        head_and_bio = body[:cut] if cut > 0 else body
        # The byline ends at the first sentence-ending period — but not at the period after an
        # initial. "By Charles M. Sennott." gave "Charles M" until v0.4.0, which published a
        # person's name wrongly, so the period must not be preceded by a lone capital letter.
        byline = re.match(r"By\s+(.+?)(?<![A-Z])\.(?:\s|$)", head_and_bio)
        names = []
        if byline:
            raw = byline.group(1).replace(" ", " ")
            names = [n.strip(" ,.") for n in re.split(r",| and |&", raw) if n.strip(" ,.")]
        # the bio sentence(s): the tail of the body before the licence
        bio = head_and_bio[-320:].strip() if cut > 0 else None

        raw_html = rec["content"]["rendered"]
        links = [l for l in re.findall(r'href="(https?://[^"]+)"', raw_html) if "worldnewsday.org" not in l]
        y = rec.get("yoast_head_json") or {}
        graph = (y.get("schema") or {}).get("@graph", []) if isinstance(y.get("schema"), dict) else []
        types = []
        for g in graph:
            t = g.get("@type") if isinstance(g, dict) else None
            types.append(t if isinstance(t, str) else "+".join(t or []))

        articles.append({
            "order_in_announcement": order,
            "slug": s,
            "id": rec["id"],
            "title": html.unescape(rec["title"]["rendered"]),
            "url": rec["link"],
            "published": rec["date"],
            "modified": rec["modified"],
            "words": len(body.split()),
            "byline": names,
            "wp_author_field": (rec.get("author_info") or {}).get("display_name"),
            "bio_line": bio,
            "licence_statement": licence,
            "categories": re.findall(r">([^<]+)</a>", rec.get("category_info") or ""),
            "tags": re.findall(r">([^<]+)</a>", rec.get("tags_info") or ""),
            "outbound_links": links,
            "outbound_domains": sorted({urllib.parse.urlparse(l).netloc for l in links}),
            "schema_types": types,
            "has_ld_json": "application/ld+json" in page,
            "schema_declares_licence": any(
                k in json.dumps(g).lower() for g in graph if isinstance(g, dict)
                for k in ('"license"', '"copyrightholder"', '"copyrightnotice"', '"usageinfo"')),
            "source_page": f"{today}/{s}.snapshot",
            "source_api": f"{today}/api/{s}.json",
        })

    write("registo.json" if False else "register.json", {
        "id": "wnd-register", "version": "0.1.0", "updated": today,
        "note": ("Every byte this section stands on. Two frozen files per op-ed — the rendered page and "
                 "the WordPress REST record the site serves for it — plus the announcement where it could "
                 "be fetched. The SHA-256 of each is re-verified on every build, so a frozen file that "
                 "changed on disk fails the build rather than quietly changing what a claim rests on."),
        "host": HOST, "snapshots": [d.name for d in snaps], "count": len(register),
        "sources": register, "excluded": excluded,
    })
    write("corpus.json", {
        "id": "wnd-corpus", "version": "0.1.0", "updated": today, "snapshot": today,
        "note": ("The 21 op-eds WAN-IFRA commissioned for World News Day 2026, as structured data. "
                 "THE PROSE IS NOT REPUBLISHED HERE: each record carries the title, the byline, the "
                 "author's own role line, the licence statement verbatim, the links the piece cites, and "
                 "counts — all read from the frozen copy. To read a piece, follow its url."),
        "count": len(articles), "total_words": sum(a["words"] for a in articles),
        "articles": articles,
    })
    print(f"extract: {len(register)} frozen files, {len(articles)} articles, "
          f"{sum(a['words'] for a in articles):,} words, {len(excluded)} excluded")


def write(name, obj):
    DATA.mkdir(parents=True, exist_ok=True)
    (DATA / name).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
