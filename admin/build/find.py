#!/usr/bin/env python3
"""Findability: desks, controlled tags, series, formats and reading time, derived once for every page (card 064).

    python3 admin/build/find.py

Reads the newsroom's own data (newsroom/wire.json, every article's markdown twin in articles/) and the editor's
input, admin/content/find/find-editorial.json, and writes articles/find.json: for every article its primary and
secondary desk, its controlled tags, its series and position, its format, its words, reading minutes and h2
headings; and the desks, the vocabulary, the series and the format labels themselves. The front page, the desk,
tag and series pages and the cards read this one file. The API will serve the same file.

The derivation is the Newsroom Design Lab's (vaults/newsroom-proto-find/tools/derive_find.py, 11 October 2026),
carried over with its rules intact: each controlled tag belongs to one desk; an article scores 3 for the desk of
its first controlled tag, 2 for its second and 1 for each further one, plus its topics (first 2, others 1, with
the editor's weights); the highest score is the primary desk; an editor override wins and says why. A raw tag the
editor has not mapped is reported, not fatal: the article is placed by its topics and the tag waits in
`unmapped` for the Librarian. The lab's rule was that a new tag fails the build; here the newsroom publishes
several articles a day and a tag must not stop a release.

Reading minutes = words / 230, measured from the markdown twin, from the first h2 to the Threads section.
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WPM = 230


def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def measure(md):
    """words, minutes, h2 headings of an article's markdown twin."""
    text = re.sub(r"^---.*?---\s*", "", md, count=1, flags=re.S)
    heads = re.findall(r"^## (.+?)\s*(?:\{#[^}]*\})?\s*$", text, flags=re.M)
    heads = [h for h in heads if h not in ("Threads",)]
    m = re.search(r"^## ", text, flags=re.M)
    body = text[m.start():] if m else text
    end = body.find("\n## Threads")
    if end > 0:
        body = body[:end]
    body = re.sub(r"```.*?```", " ", body, flags=re.S)
    words = len(re.findall(r"[A-Za-z0-9£$€%'’-]+", body))
    return words, max(1, round(words / WPM)), heads[:24]


def main():
    wire = load("newsroom/wire.json")
    ed = load("admin/content/find/find-editorial.json")
    arts = wire["articles"]
    slugs = [a["slug"] for a in arts]
    by = {a["slug"]: a for a in arts}
    desk_ids = [d["id"] for d in ed["desks"]]
    desk_label = {d["id"]: d["label"] for d in ed["desks"]}

    # ---- the catalogue: words, minutes, headings, from the twins ----
    cat = {}
    for a in arts:
        twin = ROOT / "articles" / f"{a['slug']}.md"
        if twin.exists():
            w, mins, heads = measure(twin.read_text(encoding="utf-8"))
            cat[a["slug"]] = {"words": w, "minutes": mins, "headings": heads}
        else:
            cat[a["slug"]] = {"words": None, "minutes": None, "headings": [], "missing": True}

    # ---- tags ----
    raw = Counter(t for a in arts for t in a["tags"])
    mapping = {}
    for t in ed["tags"]:
        for r in t["absorbs"]:
            if r in mapping:
                raise SystemExit(f"find: raw tag {r} absorbed twice")
            mapping[r] = t["id"]
    rejected = {}
    for reason, lst in ed["rejected"].items():
        for r in lst:
            if r in mapping or r in rejected:
                raise SystemExit(f"find: raw tag {r} both kept and rejected")
            rejected[r] = reason
    unmapped = sorted(r for r in raw if r not in mapping and r not in rejected)
    tag_desk = {t["id"]: t["desk"] for t in ed["tags"]}
    full_tags, art_tags = {}, {}
    for a in arts:
        seen = []
        for r in a["tags"]:
            c = mapping.get(r)
            if c and c not in seen:
                seen.append(c)
        full_tags[a["slug"]] = seen
        art_tags[a["slug"]] = seen[:5]
    products = {a["slug"]: [r for r in a["tags"] if rejected.get(r) == "product"] for a in arts}

    # ---- desks ----
    assign = {}
    for a in arts:
        s = {d: 0 for d in desk_ids}
        for i, c in enumerate(full_tags[a["slug"]]):
            s[tag_desk[c]] += 3 if i == 0 else 2 if i == 1 else 1
        for i, tp in enumerate(a["topics"]):
            if tp not in ed["topic_desk"]:
                continue
            d, w = ed["topic_desk"][tp]
            s[d] += w if i == 0 else max(1, w - 1)
        ranked = sorted(desk_ids, key=lambda d: (-s[d], desk_ids.index(d)))
        ov = ed["desk_overrides"].get(a["slug"])
        primary = ov[0] if ov else ranked[0]
        rest = [d for d in ranked if d != primary and s[d] > 0]
        secondary = rest[0] if rest else None
        top, runner = s[ranked[0]], s[ranked[1]]
        assign[a["slug"]] = {
            "primary": primary, "secondary": secondary, "scores": s,
            "debatable": bool(ov) or (top > 0 and runner >= 0.8 * top),
            "by": "override" if ov else "rule",
            "why": ov[1] if ov else f"Highest score: {desk_label[primary]} {s[primary]}" + (f", next {desk_label[ranked[1]]} {runner}" if runner else ""),
        }

    # ---- series ----
    series_out, by_art = [], {}
    for sr in ed["series"]:
        parts = []
        for i, (slug, why) in enumerate(sr["parts"]):
            if slug not in by:
                raise SystemExit(f"find: series {sr['id']} names unknown article {slug}")
            parts.append({"slug": slug, "position": i + 1, "why": why})
            by_art.setdefault(slug, []).append([sr["id"], i + 1, len(sr["parts"])])
        dc = Counter(assign[p["slug"]]["primary"] for p in parts)
        first_desk = assign[parts[0]["slug"]]["primary"]
        desk = sorted(dc, key=lambda d: (-dc[d], d != first_desk, desk_ids.index(d)))[0]
        mins = sum((cat.get(p["slug"]) or {}).get("minutes") or 0 for p in parts)
        series_out.append({"id": sr["id"], "title": sr["title"], "dek": sr["dek"], "found": sr["found"], "desk": desk,
                           "minutes": mins, "first": by[parts[0]["slug"]]["date"], "last": by[parts[-1]["slug"]]["date"], "parts": parts})

    # ---- formats ----
    fm = ed["formats"]
    formats = {}
    for a in arts:
        f = rule = None
        if a["slug"] in fm["overrides"]:
            f, rule = fm["overrides"][a["slug"]][0], "override: " + fm["overrides"][a["slug"]][1]
        if not f:
            for t, lab in fm["tag_rules"]:
                if t in a["tags"]:
                    f, rule = lab, f'raw tag "{t}"'
                    break
        if not f:
            hay = (a["title"] + " " + a["teaser"]).lower()
            for cue, lab in fm["title_rules"]:
                if cue in hay:
                    f, rule = lab, f'title or teaser says "{cue.strip()}"'
                    break
        if not f:
            f, rule = "analysis", "default"
        formats[a["slug"]] = {"format": f, "by": rule}

    for d in ed["desks"]:
        for slug, _ in ed["start_here"][d["id"]]:
            if slug not in by:
                raise SystemExit(f"find: start here {d['id']} names unknown {slug}")

    counts = Counter(assign[s]["primary"] for s in slugs)
    sec = Counter(assign[s]["secondary"] for s in slugs if assign[s]["secondary"])
    fmt_counts = Counter(formats[s]["format"] for s in slugs)
    label_of = {l["id"]: l["label"] for l in fm["labels"]}
    out = {
        "what": "Findability for newsroom.sgit.ai, derived by admin/build/find.py from newsroom/wire.json, the articles' markdown twins and admin/content/find/find-editorial.json. Desks by audience, a controlled vocabulary, series in reading order, a format and a reading time per article. Edit the editorial file, not this one.",
        "generated_from": ["newsroom/wire.json", "articles/<slug>.md", "admin/content/find/find-editorial.json"],
        "rule": {
            "desks": "Each controlled tag belongs to one desk. An article scores 3 for the desk of its first controlled tag, 2 for its second and 1 for each further one, plus its topics (first 2, others 1; Graphs & knowledge counts for Vaults, Site & engineering for Building). The highest score is the primary desk, the runner-up the secondary. An editor override replaces the rule and says why. A call is debatable when the runner-up scores at least 80% of the winner, or when it was overridden.",
            "tags": "Near-duplicates and plurals merge into one subject. Format words become the format label. Our own products are never subject tags. Tags that apply to most of the newsroom are rejected: the desk does that job. A raw tag the editor has not mapped is listed under unmapped and waits for the Librarian.",
            "series": "Two or more articles that tell one story in order; each later part builds on an earlier one.",
            "formats": "An editor override; else a raw format tag; else a cue in the title or teaser; else Analysis.",
            "minutes": f"words / {WPM}, measured on the markdown twin from the first h2 to Threads.",
        },
        "desks": [dict(d, start_here=[{"slug": s, "why": w} for s, w in ed["start_here"][d["id"]]], count=counts[d["id"]],
                       secondary_count=sec[d["id"]], series=[x["id"] for x in series_out if x["desk"] == d["id"]]) for d in ed["desks"]],
        "topics_today": {t["id"]: sum(1 for a in arts if t["id"] in a["topics"]) for t in wire["topics"]},
        "vocabulary": [{"id": t["id"], "label": t["label"], "desk": t["desk"], "scope": t["scope"],
                        "absorbs": [[r, raw.get(r, 0)] for r in t["absorbs"]],
                        "count": sum(1 for s in slugs if t["id"] in art_tags[s])} for t in ed["tags"]],
        "rejected": [[r, raw[r], rejected[r]] for r in sorted(rejected, key=lambda r: (-raw.get(r, 0), r)) if r in raw],
        "rejected_why": ed["rejected_why"],
        "unmapped": [[r, raw[r]] for r in unmapped],
        "series": series_out,
        "formats": {"labels": fm["labels"], "counts": {l["id"]: fmt_counts[l["id"]] for l in fm["labels"]}},
        "raw_tags": {"distinct": len(raw), "uses": sum(raw.values()), "singletons": sum(1 for c in raw.values() if c == 1)},
        "articles": {s: {
            "desk": assign[s]["primary"], "desk2": assign[s]["secondary"], "debatable": assign[s]["debatable"], "desk_by": assign[s]["by"], "desk_why": assign[s]["why"],
            "tags": art_tags[s], "products": products[s],
            "series": by_art.get(s, []),
            "format": formats[s]["format"], "format_label": label_of.get(formats[s]["format"], formats[s]["format"]), "format_by": formats[s]["by"],
            "words": cat[s]["words"], "minutes": cat[s]["minutes"], "headings": cat[s]["headings"],
        } for s in slugs},
    }
    p = ROOT / "articles/find.json"
    text = json.dumps(out, indent=1, ensure_ascii=False) + "\n"
    changed = not p.exists() or p.read_text(encoding="utf-8") != text
    if changed:
        p.write_text(text, encoding="utf-8")
    missing = [s for s in slugs if cat[s].get("missing")]
    print("find: desks " + " ".join(f"{d}={counts[d]}" for d in desk_ids)
          + f" · {len(ed['tags'])} controlled tags from {len(raw)} raw ({len(unmapped)} unmapped) · {len(series_out)} series · "
          f"{len(slugs)} articles" + (f", {len(missing)} without a twin" if missing else "") + f"; articles/find.json {'written' if changed else 'unchanged'}")
    if unmapped:
        print("find: unmapped raw tags for the Librarian: " + ", ".join(f"{r} ({raw[r]})" for r in unmapped))


if __name__ == "__main__":
    main()
