#!/usr/bin/env python3
"""Series: articles that belong together, found by tag, with a thin bar at the top of each and the full list at the foot.

    python3 admin/build/series.py            stamp the bar and the list on every article in a series
    python3 admin/build/series.py --check    validate admin/content/series.json and list each series' members

A series is one entry in admin/content/series.json: {id, title, tag, note}. Its members are every article whose
front matter carries the tag, in the order they were first published (their article number), so a new article joins
by being tagged and nothing here is edited by hand. The bar sits under the byline, before the abstract, so it is not
part of the article's text; the list sits at the foot, after the meter and before the Reviews section, so neither
summaries.py nor reviews.py reads it. Runs after reviews.py. validate.js and sync_newsroom.py strip both blocks.
"""
import argparse
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "admin/content/series.json"
ART = ROOT / "admin/content/articles"
e = html.escape
BAR = re.compile(r'<nav class="aseries"[^>]*>.*?</nav>\n', re.S)
LIST = re.compile(r'<section class="aseries-all"[^>]*>.*?</section>\n', re.S)


def front(p):
    t = p.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", t, re.S)
    fm = {}
    for line in (m.group(1).splitlines() if m else []):
        k, _, v = line.partition(":")
        fm[k.strip()] = v.strip()
    return fm


def series():
    return json.loads(SRC.read_text(encoding="utf-8"))["series"] if SRC.exists() else []


def members(s, ids):
    out = []
    for a in ids:
        p = ART / f"{a['slug']}.md"
        if not p.exists():
            continue
        fm = front(p)
        tags = [t.strip() for t in fm.get("tags", "").split(",")]
        if s["tag"] in tags and fm.get("status", "published") == "published":
            out.append({"n": a["n"], "slug": a["slug"], "title": a["title"], "short": a["title"].split(":")[0],
                        "summary": fm.get("summary", "")})
    out.sort(key=lambda a: a["n"])
    return out


def first_sentence(t, n=28):
    s = re.split(r"(?<=[.!?])\s", t, maxsplit=1)[0]
    w = s.split()
    return " ".join(w[:n]) + ("…" if len(w) > n else "")


def bar(s, ms, here):
    i = next(k for k, m in enumerate(ms) if m["slug"] == here)
    nxt = ms[i + 1] if i + 1 < len(ms) else None
    prv = ms[i - 1] if i > 0 else None
    bits = [f'<a href="#series"><b>{e(s["title"])}</b></a> <span class="dim">{i + 1} of {len(ms)}</span>']
    if prv:
        bits.append(f'<a href="{e(prv["slug"])}.html" rel="prev">&larr; {e(prv["short"])}</a>')
    if nxt:
        bits.append(f'<a href="{e(nxt["slug"])}.html" rel="next">{e(nxt["short"])} &rarr;</a>')
    return f'<nav class="aseries" aria-label="Series: {e(s["title"])}">' + " &middot; ".join(bits) + "</nav>\n"


def full(s, ms, here):
    rows = []
    for k, m in enumerate(ms, 1):
        cur = m["slug"] == here
        t = e(m["short"])
        link = f'<b>{t}</b> <span class="dim">(you are here)</span>' if cur else f'<a href="{e(m["slug"])}.html">{t}</a>'
        cls = ' class="here"' if cur else ""
        rows.append(f'<li{cls}><span class="aseries-n">{k}</span> {link}<br>'
                    f'<span class="dim">{e(first_sentence(m["summary"]))}</span></li>')
    return (f'<section class="aseries-all" id="series">\n <h2>{e(s["title"])}</h2>\n'
            f' <p class="dim">{e(s["note"])} Every article tagged <span class="chip">{e(s["tag"])}</span> joins this list, '
            f'in the order it was published.</p>\n <ol>{"".join(rows)}</ol>\n</section>\n')


def stamp(slug, top, foot):
    p = ROOT / "articles" / f"{slug}.html"
    if not p.exists():
        return False
    page = p.read_text(encoding="utf-8")
    new = LIST.sub("", BAR.sub("", page))
    m = re.search(r'(</h1>\n <p class="small dim">By .*?</p>\n)', new, re.S)
    if not m:
        print(f"series: {slug}: no byline to put the bar under")
        return False
    new = new[:m.end()] + top + new[m.end():]
    j = new.find('<section class="athreads areviews"')
    if j < 0:
        j = new.rfind("</main>")
    new = new[:j] + foot + new[j:]
    if new != page:
        p.write_text(new, encoding="utf-8")
        return True
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    ids = json.loads((ROOT / "articles/ids.json").read_text(encoding="utf-8"))["articles"]
    errors, n = [], 0
    for s in series():
        for k in ("id", "title", "tag", "note"):
            if not s.get(k):
                errors.append(f"series {s.get('id', '?')}: missing {k}")
        ms = members(s, ids)
        if a.check:
            print(f"series {s['id']}: {len(ms)} articles: " + ", ".join(m["slug"] for m in ms))
            continue
        if len(ms) < 2:
            continue
        for m in ms:
            n += stamp(m["slug"], bar(s, ms, m["slug"]), full(s, ms, m["slug"]))
    if errors:
        for x in errors:
            print("series: ERROR", x)
        sys.exit(1)
    if not a.check:
        print(f"series: {len(series())} series, {n} pages stamped")


if __name__ == "__main__":
    main()
