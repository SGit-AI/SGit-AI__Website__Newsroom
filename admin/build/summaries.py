#!/usr/bin/env python3
"""Section summaries: a line and a paragraph for every section of every article (card 083).

    python3 admin/build/summaries.py                 build articles/summaries/<slug>.json for every article
    python3 admin/build/summaries.py --dump DIR      write each article's sections as text, for whoever writes summaries
    python3 admin/build/summaries.py --stamp         add the section hash to authored summaries that lack one
    python3 admin/build/summaries.py --check         report coverage and stale summaries, write nothing

An article is read as the reading strip reads it (assets/reader/strip.js): `main`'s children up to the meter's
element or the threads; the part before the first h2 is the section "top" (the opening), and every h2 starts a
section named by its id. A section's text is its words with the markup taken out.

Each section has three ways to be shown when the reader has read it (assets/reader/folds.js): the whole text, a
paragraph, or a line. The line is about eight words and says what the section says, not what it is about; the
paragraph is two or three sentences, at most about 60 words. They are written with the article, by whoever writes
it (the newsroom's agents), in admin/content/articles/summaries/<slug>.json:

    { "slug": "...", "by": "newsroom.ux",
      "sections": { "in-short": { "line": "...", "para": "...", "hash": "3f2a9c1e0b7d" }, ... } }

`hash` is the first 12 hex characters of the SHA-256 of the section's text when the summary was written. If the
section changes, the hash no longer matches and the summary is served marked stale, so an article corrected after
it was summarised says so instead of summarising words that are gone. A section with no authored summary gets an
extract: its first sentence cut to about eight words for the line, its first sentences up to about 60 words for the
paragraph, marked "by": "extract". Extracts are a floor, not the goal; --check counts them.
"""
import argparse
import hashlib
import html as _html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "admin/content/articles/summaries"
OUT = ROOT / "articles/summaries"
LINE_WORDS, PARA_WORDS = 9, 60


def text_of(fragment):
    t = re.sub(r"<(script|style)\b.*?</\1>", " ", fragment, flags=re.S)
    t = re.sub(r"<figure\b.*?</figure>", " ", t, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", _html.unescape(t)).strip()


def words(t):
    return len(re.findall(r"[A-Za-z0-9£$€%'’-]+", t))


def sections_of(slug):
    """The article's sections as the strip sees them: [(id, label, text)]."""
    p = ROOT / "articles" / f"{slug}.html"
    if not p.exists():
        return []
    page = p.read_text(encoding="utf-8")
    m = re.search(r"<main\b[^>]*>(.*)</main>", page, re.S)
    if not m:
        return []
    body = m.group(1)
    cut = [i for i in (body.find("<sg-meter"), body.find('<nav class="trail-end"'), body.find('<section class="athreads"'), body.find('<div class="agent"')) if i >= 0]
    if cut:
        body = body[:min(cut)]
    body = re.sub(r'<p class="crumb">.*?</p>', " ", body, flags=re.S)
    body = re.sub(r'<p class="rvstatus[^"]*">.*?</p>', " ", body, flags=re.S)  # reviews.py's line, after the text (v0.13.113)
    parts = re.split(r'(<h2\b[^>]*>.*?</h2>)', body, flags=re.S)
    out = [["top", "The opening", parts[0]]]
    for i in range(1, len(parts), 2):
        h = parts[i]
        idm = re.search(r'\bid="([^"]+)"', h)
        out.append([idm.group(1) if idm else f"s{len(out) - 1}", text_of(h), parts[i + 1] if i + 1 < len(parts) else ""])
    res = []
    for sid, label, frag in out:
        t = text_of(frag)
        if sid == "top":
            t = re.sub(r"^.*?\bAbstract:\s*", "", t) if "Abstract:" in t else t
        if words(t) > 0:
            res.append((sid, label, t))
    return res


def digest(t):
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:12]


def sentences(t):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"“‘(])", t) if s.strip()]


def extract(t):
    ss = sentences(t) or [t]
    first = re.sub(r"\s*\([^)]*\)", "", ss[0])
    w = first.split()
    line = " ".join(w[:LINE_WORDS]).rstrip(",;:") + ("…" if len(w) > LINE_WORDS else "")
    para, n = [], 0
    for s in ss:
        k = len(s.split())
        if para and n + k > PARA_WORDS:
            break
        para.append(s); n += k
    p = " ".join(para)
    if len(p.split()) > PARA_WORDS + 20:
        p = " ".join(p.split()[:PARA_WORDS]) + "…"
    return line, p


def slugs():
    return [a["slug"] for a in json.loads((ROOT / "newsroom/wire.json").read_text(encoding="utf-8"))["articles"]]


def authored(slug):
    p = SRC / f"{slug}.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def build(check=False):
    if not check:
        OUT.mkdir(parents=True, exist_ok=True)
    stats = {"articles": 0, "sections": 0, "authored": 0, "stale": 0, "extract": 0}
    stale_list, changed = [], 0
    for slug in slugs():
        secs = sections_of(slug)
        if not secs:
            continue
        a = authored(slug) or {"sections": {}}
        rows = []
        for sid, label, t in secs:
            h = digest(t)
            s = a["sections"].get(sid)
            if s and s.get("line") and s.get("para"):
                st = bool(s.get("hash")) and s["hash"] != h
                rows.append({"id": sid, "label": label, "words": words(t), "line": s["line"], "para": s["para"], "by": a.get("by", "editor"), **({"stale": True} if st else {})})
                stats["authored"] += 1
                if st:
                    stats["stale"] += 1; stale_list.append(f"{slug}#{sid}")
            else:
                line, para = extract(t)
                rows.append({"id": sid, "label": label, "words": words(t), "line": line, "para": para, "by": "extract"})
                stats["extract"] += 1
        stats["articles"] += 1; stats["sections"] += len(rows)
        if check:
            continue
        doc = {"slug": slug, "what": "The sections of this article, each with a line and a paragraph, for showing what the reader has already read. Built by admin/build/summaries.py from admin/content/articles/summaries/.",
               "sections": rows}
        p = OUT / f"{slug}.json"
        text = json.dumps(doc, ensure_ascii=False, indent=1) + "\n"
        if not p.exists() or p.read_text(encoding="utf-8") != text:
            p.write_text(text, encoding="utf-8"); changed += 1
    print(f"summaries: {stats['articles']} articles, {stats['sections']} sections: {stats['authored']} authored "
          f"({stats['stale']} stale), {stats['extract']} extracts" + ("" if check else f"; {changed} written"))
    if stale_list:
        print("summaries: stale (the section changed after it was summarised): " + ", ".join(stale_list[:30]))
    return stats


def dump(d):
    d = Path(d); d.mkdir(parents=True, exist_ok=True)
    n = 0
    for slug in slugs():
        secs = sections_of(slug)
        if not secs:
            continue
        (d / f"{slug}.json").write_text(json.dumps({"slug": slug, "sections": [{"id": s, "label": l, "words": words(t), "hash": digest(t), "text": t} for s, l, t in secs]},
                                                   ensure_ascii=False, indent=1), encoding="utf-8")
        n += 1
    print(f"summaries: {n} articles dumped to {d}")


def stamp():
    n = 0
    for p in sorted(SRC.glob("*.json")):
        a = json.loads(p.read_text(encoding="utf-8"))
        cur = {sid: digest(t) for sid, _, t in sections_of(a["slug"])}
        changed = False
        for sid, s in a["sections"].items():
            if not s.get("hash") and sid in cur:
                s["hash"] = cur[sid]; changed = True
        if changed:
            p.write_text(json.dumps(a, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"); n += 1
    print(f"summaries: {n} authored file(s) stamped")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--dump"); ap.add_argument("--stamp", action="store_true"); ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    if a.dump:
        dump(a.dump)
    elif a.stamp:
        stamp()
    else:
        build(check=a.check)
