#!/usr/bin/env python3
"""A number for every article, kept in articles/ids.json.

    python3 admin/build/ids.py                       # refresh from the imported newsroom
    python3 admin/build/ids.py --from <sgit.ai checkout>   # also number articles not yet imported

A link to a reading list (/for/) names articles by number: `r=61,44,70`. The number is the contract
between the newsroom and anyone who builds links to it, a person or an agent, so it has three rules:

  1. Numbers are assigned once, in the order articles were first published, starting at 1. A new article
     takes the next number. The order is the article's date, then the order the source repository first
     added it, then its address, so two articles of one day are numbered in the order they were committed.
  2. A number is never changed and never reused. The file only grows. An article that is withdrawn keeps its
     number and its entry, marked "withdrawn": true, and the page that opens a list says so.
  3. Everything else in an entry (title, teaser, topics, the personas whose starting list holds it, the
     reading time) is display text, refreshed on every build from the imported pages. Only "n" and "slug"
     are the contract.

admin/build/sync_newsroom.py calls assign() before it writes a page, so each article carries its number
the first time it is imported. validate.js check 12 reads the file and fails the release if a number is
missing, repeated, moved, or reused.
"""
import argparse
import json
import math
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HOST = (ROOT / "CNAME").read_text().strip()
FILE = ROOT / "articles/ids.json"
WHAT = ("A stable number for every article on newsroom.sgit.ai, assigned once in the order the articles were first "
        "published and never changed or reused. A link to a reading list names articles by these numbers "
        "(https://%s/for/#r=61,44,70). Only n and slug are the contract; every other field is display text, "
        "refreshed on each build. Written by admin/build/ids.py." % HOST)
WORDS_PER_MINUTE = 220
FIELDS = ["n", "slug", "title", "date", "minutes", "teaser", "topics", "personas", "url", "withdrawn"]


def load():
    return json.loads(FILE.read_text(encoding="utf-8")) if FILE.exists() else {}


def source_rank(src, slugs):
    """The order the source repository first added each article, as an index into its history."""
    if not src:
        return {}
    try:
        order = subprocess.run(["git", "-C", str(src), "rev-list", "--reverse", "HEAD"],
                               capture_output=True, text=True, check=True).stdout.split()
        pos = {c: i for i, c in enumerate(order)}
        rank = {}
        for s in slugs:
            first = subprocess.run(["git", "-C", str(src), "log", "--reverse", "--diff-filter=A", "--format=%H",
                                    "--", f"articles/{s}.md"], capture_output=True, text=True).stdout.split()
            if first:
                rank[s] = pos.get(first[0], 0)
        return rank
    except (OSError, subprocess.CalledProcessError):
        return {}


def assign(src=None):
    """Number every article in the source's graphs.json that has no number yet. Returns {slug: n}."""
    graphs_file = (Path(src) if src else ROOT) / "articles/graphs.json"
    articles = json.loads(graphs_file.read_text(encoding="utf-8"))["articles"]
    doc = load()
    have = {e["slug"]: e for e in doc.get("articles", [])}
    new = [a for a in articles if a["slug"] not in have]
    if new:
        rank = source_rank(src, [a["slug"] for a in new])
        new.sort(key=lambda a: (a["date"], rank.get(a["slug"], 0), a["slug"]))
        top = max([e["n"] for e in have.values()] + [doc.get("next", 1) - 1, 0])
        for a in new:
            top += 1
            have[a["slug"]] = {"n": top, "slug": a["slug"], "title": a["title"], "date": a["date"]}
    live = {a["slug"] for a in articles}
    for slug, e in have.items():
        if slug in live:
            e.pop("withdrawn", None)
        else:
            e["withdrawn"] = True
    entries = sorted(have.values(), key=lambda e: e["n"])
    doc = {**doc, "what": WHAT, "next": max(e["n"] for e in entries) + 1 if entries else 1, "articles": entries}
    FILE.parent.mkdir(parents=True, exist_ok=True)
    FILE.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return {e["slug"]: e["n"] for e in entries}


def minutes_for(slug):
    """Reading time from the word count sgit.ai records on the article's version page."""
    p = ROOT / f"articles/versions/{slug}.md"
    if p.exists():
        m = re.search(r"\| \*\*v[\d.]+\*\* \| [\d-]+ \| [^|]+ \| ([\d,]+) \|", p.read_text(encoding="utf-8"))
        if m:
            return max(1, math.ceil(int(m.group(1).replace(",", "")) / WORDS_PER_MINUTE))
    return None


def collections():
    out = []
    for p in sorted((ROOT / "articles/collections").glob("*.html")):
        if p.stem == "index":
            continue
        m = re.search(r"<h1>(.*?)</h1>", p.read_text(encoding="utf-8"), re.S)
        out.append({"slug": p.stem, "title": re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else p.stem})
    return out


def presets():
    cfg = json.loads(re.search(r'id="sg-meter-config">(\{.*?\})</script>', (ROOT / "index.html").read_text(encoding="utf-8"), re.S).group(1))
    return cfg["personas"]["presets"]


def refresh(src=None):
    """assign(), then fill every entry's display fields from the imported newsroom."""
    assign(src)
    doc = load()
    graphs = {a["slug"]: a for a in json.loads((ROOT / "articles/graphs.json").read_text(encoding="utf-8"))["articles"]}
    pre = presets()
    entries = []
    for e in doc["articles"]:
        a = graphs.get(e["slug"])
        if a:
            e = {**e, "title": a["title"], "date": a["date"], "teaser": a["teaser"], "topics": a["topics"],
                 "personas": [p["id"] for p in pre if e["slug"] in p["articles"]],
                 "minutes": minutes_for(e["slug"]), "url": f"https://{HOST}/articles/{e['slug']}.html"}
        entries.append({k: e[k] for k in FIELDS if k in e})
    doc["articles"] = entries
    doc["count"] = sum(1 for e in doc["articles"] if not e.get("withdrawn"))
    doc["collections"] = collections()
    doc["topics"] = [{"id": t["id"], "label": t["label"]} for t in json.loads((ROOT / "articles/graphs.json").read_text(encoding="utf-8"))["topics"]]
    doc["personas"] = [{"id": p["id"], "name": p["name"], "label": p["label"]} for p in pre]
    order = ["what", "count", "next", "personas", "topics", "collections", "articles"]
    doc = {k: doc[k] for k in order}
    text = json.dumps(doc, indent=1, ensure_ascii=False) + "\n"
    if not FILE.exists() or FILE.read_text(encoding="utf-8") != text:
        FILE.write_text(text, encoding="utf-8")
        return True
    return False


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--from", dest="src", help="a checkout of sgit.ai, to number articles before they are imported")
    args = ap.parse_args()
    changed = refresh(args.src)
    doc = load()
    print(f"ids: {doc['count']} articles numbered 1-{doc['next'] - 1}, {len(doc['collections'])} collections"
          + (" (articles/ids.json written)" if changed else ""))


if __name__ == "__main__":
    sys.exit(main())
