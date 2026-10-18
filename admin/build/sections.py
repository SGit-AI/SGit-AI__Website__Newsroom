#!/usr/bin/env python3
"""Sections: the newsroom as one audience reads it, kept current by rule.

    python3 admin/build/sections.py              write sections/index.html, and for each section sections/<id>/index.html
                                                 and sections/<id>.json; print each stream's count and the near misses
    python3 admin/build/sections.py --check      print the placement and the near misses, write nothing

A section is defined by one file, admin/content/sections/<id>.json: who it is for, the editor's words, the pieces to
start with, and streams with rules. The rules are written against articles/find.json (admin/build/find.py), so a new
article is placed by the desk and controlled tags find.py gives it, with no list to keep by hand. Streams are tried in
order and an article goes in the first that matches; a stream's rule is a list of clauses (any one may match), and a
clause is a set of conditions (all must hold):

    desk_any     the article's first or second desk is one of these
    desk         its first desk is one of these
    tags_any     it has one of these controlled tags
    tags_all     it has all of these
    formats      its format is one of these          format_not   it is none of these
    series       it is in one of these series
    slugs        it is one of these articles      slugs_not    it is none of these (the editor's exceptions)

Each placed article keeps the clause that placed it, shown on the page as "placed because", so a wrong placement can be
traced to its rule. Near misses (an article on a desk the section draws from, with no stream) are printed at build so
the rules can be tuned. Features come from admin/content/features.json: a feature appears when its audiences include
the section's id.
"""
import json
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from page import newsroom_page, write, esc, HOST  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "admin/content/sections"


def load(p):
    return json.loads((ROOT / p).read_text(encoding="utf-8"))


def holds(cond, f, slug):
    tags, desks = set(f.get("tags") or []), {f.get("desk"), f.get("desk2")}
    checks = {
        "desk_any": lambda v: bool(desks & set(v)),
        "desk": lambda v: f.get("desk") in v,
        "tags_any": lambda v: bool(tags & set(v)),
        "tags_all": lambda v: set(v) <= tags,
        "formats": lambda v: f.get("format") in v,
        "format_not": lambda v: f.get("format") not in v,
        "series": lambda v: bool({s.get("id") if isinstance(s, dict) else s for s in (f.get("series") or [])} & set(v)),
        "slugs": lambda v: slug in v,
        "slugs_not": lambda v: slug not in v,
    }
    for k, v in cond.items():
        if k not in checks:
            raise SystemExit(f"sections: unknown condition {k!r}")
        if not checks[k](v):
            return False
    return True


def why(cond, f):
    parts = []
    for k, v in cond.items():
        if k in ("tags_any", "tags_all"):
            hit = [t for t in v if t in (f.get("tags") or [])]
            parts.append("tagged " + ", ".join(hit))
        elif k in ("desk_any", "desk"):
            parts.append("on the " + ", ".join(d for d in v if d in (f.get("desk"), f.get("desk2"))) + " desk")
        elif k == "formats":
            parts.append(f"format {f.get('format')}")
        elif k == "series":
            parts.append("in a series")
        elif k == "slugs":
            parts.append("chosen by the editor")
    return "; ".join(parts)


def place(sec, find):
    fa = find["articles"]
    placed, members = {s["id"]: [] for s in sec["streams"]}, {}
    out = {s for s, _ in sec.get("exclude", [])}
    for slug, f in fa.items():
        if slug in out:
            continue
        for st in sec["streams"]:
            hit = next((c for c in st["rule"] if holds(c, f, slug)), None)
            if hit is not None:
                placed[st["id"]].append((slug, why(hit, f)))
                members[slug] = st["id"]
                break
    desks = {d for st in sec["streams"] for c in st["rule"] for d in c.get("desk_any", []) + c.get("desk", [])}
    near = sorted(s for s, f in fa.items() if s not in members and s not in out and f.get("desk") in desks)
    return placed, members, near


def build(sec, find, ids, feats, today):
    by = {a["slug"]: a for a in ids["articles"]}
    fa = find["articles"]
    placed, members, near = place(sec, find)
    for st in placed.values():
        st.sort(key=lambda x: (by[x[0]]["date"], by[x[0]]["n"]), reverse=True)
    sid, up = sec["id"], "../../"
    new_since = (today - timedelta(days=sec.get("new_days", 7))).isoformat()
    labels = {st["id"]: st["label"] for st in sec["streams"]}

    def meta(slug):
        f = fa.get(slug, {})
        return f'{by[slug]["date"]} &middot; {f.get("minutes", "")} min &middot; {esc(f.get("format_label", ""))}'

    def new(slug):
        return ' <span class="sx-new">new</span>' if by[slug]["date"] >= new_since else ""

    start = "".join(
        f'<li class="sx-card"><a href="{up}articles/{s}.html"><img src="{up}og/{s}.jpg" alt="" loading="lazy" width="1200" height="630"></a>'
        f'<div><a href="{up}articles/{s}.html"><b>{esc(by[s]["title"].split(":")[0])}</b></a>{new(s)}<br>'
        f'<span class="dim">{meta(s)}</span><p>{esc(w)}</p></div></li>'
        for s, w in sec["start_here"] if s in by)
    latest = sorted(members, key=lambda s: (by[s]["date"], by[s]["n"]), reverse=True)[:sec.get("latest", 10)]
    latest_html = "".join(
        f'<li><a href="{up}articles/{s}.html">{esc(by[s]["title"])}</a>{new(s)}<br>'
        f'<span class="dim">{meta(s)} &middot; {esc(labels[members[s]])}</span></li>' for s in latest)
    live = [f for f in feats["features"] if sid in f["audiences"] and f["status"] in ("live", "beta")]
    designed = [f for f in feats["features"] if sid in f["audiences"] and f["status"] == "designed"]
    st_lab = feats["status_labels"]

    def since(f):
        return f' &middot; since {esc(f["since"])}' if f.get("since") else ""

    feat_html = "".join(
        f'<li class="sx-feat"><b>{esc(f["name"])}</b> <span class="pill">{esc(st_lab[f["status"]])}{since(f)}</span>'
        f'<p>{esc(f["what"])}</p><p class="dim">{esc(f["why"])}</p><p>'
        + (f'<a href="{up}{esc(f["try"])}">Try it</a>' if f.get("try") else "")
        + (f' &middot; <a href="{up}articles/{esc(f["article"])}.html">Read about it</a>' if f.get("article") else "")
        + '</p></li>' for f in live)
    designed_html = "".join(
        f'<li><b>{esc(f["name"])}</b>: {esc(f["what"])} <a href="{up}articles/{esc(f["article"])}.html">The design</a></li>' for f in designed)
    streams_html = []
    for st in sec["streams"]:
        rows = placed[st["id"]]
        streams_html.append(
            f'<h2 id="{esc(st["id"])}">{esc(st["label"])} <span class="dim">{len(rows)}</span></h2><p>{esc(st["about"])}</p><ol class="sx-list">'
            + "".join(f'<li><a href="{up}articles/{s}.html">{esc(by[s]["title"])}</a>{new(s)}<br><span class="dim">{meta(s)}</span>'
                      f'<br><span class="sx-why">Placed because: {esc(w)}</span></li>' for s, w in rows) + '</ol>')
    links = "".join(f'<li><a href="{up}{esc(h)}">{esc(t)}</a>: {esc(w)}</li>' for h, t, w in sec.get("links", []))
    ov = sec.get("overview")
    n_new = sum(1 for s in members if by[s]["date"] >= new_since)
    body = f"""<p class="lead">{esc(sec["for_whom"])}</p>
<p>{esc(sec["intro"])}</p>
<p class="dim">{len(members)} articles in this section, {n_new} in the last {sec.get("new_days", 7)} days; {len(live)} features you can use today. Built {today.isoformat()}.{f' <a href="{up}{esc(ov["href"])}">{esc(ov["label"])}</a>.' if ov else ''}</p>
<nav class="sx-toc"><a href="#start">Start here</a> <a href="#latest">Latest</a> <a href="#features">Features</a> {" ".join(f'<a href="#{esc(st["id"])}">{esc(st["label"])}</a>' for st in sec["streams"])} <a href="#how">How this page stays current</a></nav>
<h2 id="start">Start here</h2><p>Five pieces, chosen by the editor, for a first visit.</p>
<ol class="sx-start">{start}</ol>
<h2 id="latest">Latest</h2><p>The newest pieces in this section, placed as they were published.</p>
<ol class="sx-list">{latest_html}</ol>
<h2 id="features">What you can use today</h2><p>Features of this site a publisher can try, and copy; each with when it shipped and the article that explains it.</p>
<ul class="sx-feats">{feat_html}</ul>
{f'<h3 id="next">Designed, not running yet</h3><ul>{designed_html}</ul>' if designed else ''}
{"".join(streams_html)}
<h2 id="more">More for publishers</h2><ul>{links}</ul>
<h2 id="how">How this page stays current</h2>
<p>Nothing on this page is listed by hand except the five to start with. Every article is placed by the desk and the controlled subjects the newsroom's findability step gives it (<a href="{up}articles/find.json">articles/find.json</a>), against the rules in this section's file; each article says which rule placed it. Features come from the site's register of what it can do, updated in the release that ships each one. The rules, the placement and the features are also <a href="{up}sections/{esc(sid)}.json">one JSON file</a>.</p>
<style>
.sx-toc{{display:flex;flex-wrap:wrap;gap:.3rem .9rem;margin:1rem 0;font-size:.92rem}}
.sx-start{{list-style:none;padding:0;display:grid;gap:1rem;grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}}
.sx-card{{border:1px solid var(--line);border-radius:10px;overflow:hidden;background:var(--panel);min-width:0}}
.sx-card img{{width:100%;height:auto;display:block;aspect-ratio:1200/630;object-fit:cover}}
.sx-card div{{padding:.7rem .9rem}} .sx-card p{{margin:.4rem 0 0}}
.sx-list li{{margin:.55rem 0}} .sx-why{{font-size:.85rem;color:var(--muted, #6b6b6b)}}
.sx-new{{font-size:.72rem;font-weight:600;text-transform:uppercase;letter-spacing:.05em;padding:.05rem .4rem;border-radius:999px;border:1px solid currentColor;margin-left:.3rem}}
.sx-feats{{list-style:none;padding:0;display:grid;gap:.9rem;grid-template-columns:repeat(auto-fit,minmax(260px,1fr))}}
.agent p{{overflow-wrap:anywhere}}
.sx-feat{{border:1px solid var(--line);border-radius:10px;padding:.8rem 1rem;background:var(--panel);min-width:0}} .sx-feat p{{margin:.35rem 0}}
</style>"""
    agent = (f"The {sec['title']} section of newsroom.sgit.ai: {sec['for_whom']} {len(members)} articles placed by rule into "
             f"{len(sec['streams'])} streams, {len(live)} live features, five to start with. Machine-readable: https://{HOST}/sections/{sid}.json; "
             f"the placement data: https://{HOST}/articles/find.json; the features: https://{HOST}/sections/features.json.")
    page = newsroom_page(f"sections/{sid}/index.html", sec["title"], sec["for_whom"], body, eyebrow="A section",
                         crumbs=(("Sections", "sections/index.html"),), agent=agent, wide=True)
    data = {"id": sid, "title": sec["title"], "built": today.isoformat(), "for_whom": sec["for_whom"],
            "start_here": [{"slug": s, "why": w} for s, w in sec["start_here"]],
            "latest": latest,
            "streams": [{"id": st["id"], "label": st["label"], "rule": st["rule"],
                         "articles": [{"slug": s, "date": by[s]["date"], "placed_because": w} for s, w in placed[st["id"]]]} for st in sec["streams"]],
            "features": [f["id"] for f in live + designed], "near_misses": near,
            "excluded": [{"slug": s, "why": w} for s, w in sec.get("exclude", [])]}
    return page, data, placed, near


def main():
    check = "--check" in sys.argv
    find, ids, feats = load("articles/find.json"), load("articles/ids.json"), load("admin/content/features.json")
    today = max(date.fromisoformat(a["date"]) for a in ids["articles"])
    secs = [json.loads(p.read_text(encoding="utf-8")) for p in sorted(SRC.glob("*.json"))]
    changed, cards = [], []
    for sec in secs:
        page, data, placed, near = build(sec, find, ids, feats, today)
        counts = ", ".join(f"{k} {len(v)}" for k, v in placed.items())
        print(f"sections: {sec['id']}: {counts}; {len(near)} near miss(es)" + (f": {', '.join(near)}" if near else ""))
        if check:
            continue
        if write(f"sections/{sec['id']}/index.html", page):
            changed.append(sec["id"])
        p = ROOT / "sections" / f"{sec['id']}.json"
        p.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        cards.append(f'<li><a href="{esc(sec["id"])}/index.html"><b>{esc(sec["title"])}</b></a>: {esc(sec["for_whom"])} '
                     f'<span class="dim">{sum(len(v) for v in placed.values())} articles</span></li>')
    if check:
        return
    (ROOT / "sections" / "features.json").write_text(json.dumps(feats, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    body = (f'<p class="lead">A section is the newsroom as one audience reads it: what to start with, what is new, the features they can use, '
            f'and every article placed for them by rule, so the section keeps itself current as the site changes.</p><ul>{"".join(cards)}</ul>'
            f'<p class="dim">The sections are defined in <code>admin/content/sections/</code> and built by <code>admin/build/sections.py</code> '
            f'from <a href="../articles/find.json">articles/find.json</a> and the <a href="features.json">features register</a>. '
            f'The five <a href="../desks/index.html">desks</a> place every article; a section draws on them for one audience.</p>')
    if write("sections/index.html", newsroom_page("sections/index.html", "Sections", "The newsroom as one audience reads it.", body,
                                                  eyebrow="The newsroom", agent=f"Sections of newsroom.sgit.ai: {', '.join(s['title'] for s in secs)}. "
                                                  f"Each has a machine-readable twin at https://{HOST}/sections/<id>.json.")):
        changed.append("index")
    print(f"sections: {len(secs)} section(s); {len(changed)} page(s) written {changed}")


if __name__ == "__main__":
    main()
