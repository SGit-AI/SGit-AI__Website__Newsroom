#!/usr/bin/env python3
"""The desks: one page per desk, and the index of the five (card 059).

    python3 admin/build/desks.py

Reads articles/find.json (admin/build/find.py) and newsroom/wire.json and writes desks/index.html and
desks/<id>.html. A desk is an audience, not a topic: who it is for, where to start (the editor's three,
with a reason each), its series in reading order, every article on it newest first with its format and
reading time, and the subjects its articles carry. Nothing here is hand-written: the words are the
editor's in admin/content/find/find-editorial.json, the placement is find.py's.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from page import newsroom_page, write, esc, HOST  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]


def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def mins(m):
    return f"{m} min" if m else ""


def plural(n, w):
    return f"{n} {w}{'' if n == 1 else 's'}"


def main():
    find, wire = load("articles/find.json"), load("newsroom/wire.json")
    by = {a["slug"]: a for a in wire["articles"]}
    fa = find["articles"]
    series = {s["id"]: s for s in find["series"]}
    changed = []

    def row(slug, why=""):
        a, f = by[slug], fa[slug]
        return (f'<li><a href="../articles/{slug}.html"><b>{esc(a["title"])}</b></a> '
                f'<span class="dim">{a["date"]} &middot; {mins(f["minutes"])} &middot; {esc(f["format_label"])}</span>'
                + (f'<br><span class="why">{esc(why)}</span>' if why else f'<br>{esc(a["teaser"])}') + '</li>')

    for d in find["desks"]:
        arts = sorted((s for s in fa if fa[s]["desk"] == d["id"]), key=lambda s: by[s]["date"], reverse=True)
        also = sorted((s for s in fa if fa[s]["desk2"] == d["id"]), key=lambda s: by[s]["date"], reverse=True)
        tags = [v for v in find["vocabulary"] if v["desk"] == d["id"] and v["count"]]
        body = [f'<p class="lead">{esc(d["for_whom"])}</p>',
                f'<p class="dim">{plural(d["count"], "article")} on this desk, {len(also)} more that touch it. '
                f'Placed by rule from the subjects and topics of each article (<a href="../articles/find.json">articles/find.json</a>); the editor can override a call, and says why.</p>',
                '<h2 id="start">Start here</h2><p>Three pieces, in order, for a first visit to this desk.</p>',
                '<ol class="start">' + "".join(row(s["slug"], s["why"]) for s in d["start_here"]) + '</ol>']
        if d["series"]:
            body.append('<h2 id="series">Series</h2><p>Two or more articles that tell one story in order.</p>')
            for sid in d["series"]:
                s = series[sid]
                body.append(f'<h3 id="series-{esc(sid)}">{esc(s["title"])} <span class="dim">&middot; {plural(len(s["parts"]), "part")} &middot; {mins(s["minutes"])}</span></h3>'
                            f'<p>{esc(s["dek"])}</p><ol>' + "".join(row(p["slug"], p["why"]) for p in s["parts"]) + '</ol>')
        body.append(f'<h2 id="all">Every article on this desk</h2><ol class="all">' + "".join(row(s) for s in arts) + '</ol>')
        if also:
            body.append('<h2 id="also">Also touching this desk</h2><p class="dim">Placed on another desk first; this one second.</p><ul>'
                        + "".join(f'<li><a href="../articles/{s}.html">{esc(by[s]["title"])}</a> <span class="dim">on {esc(next(x["label"] for x in find["desks"] if x["id"] == fa[s]["desk"]))}</span></li>' for s in also) + '</ul>')
        if tags:
            body.append('<h2 id="subjects">Subjects on this desk</h2><p class="dim">The controlled vocabulary: each subject belongs to one desk.</p><p>'
                        + " ".join(f'<span class="pill">{esc(t["label"])} &middot; {t["count"]}</span>' for t in tags) + '</p>')
        agent = (f"The {d['label']} desk of newsroom.sgit.ai: {d['for_whom']} {d['count']} articles placed here by rule, "
                 f"{len(d['series'])} series, three to start with. The data: https://{HOST}/articles/find.json (desks, vocabulary, series, "
                 f"formats and reading time for every article). Every desk: https://{HOST}/desks/index.html.")
        if write(f"desks/{d['id']}.html", newsroom_page(f"desks/{d['id']}.html", f"{d['label']}: the desk", d["for_whom"],
                                                        "\n".join(body), eyebrow="A desk", crumbs=(("The five desks", "desks/index.html"),), agent=agent)):
            changed.append(f"desks/{d['id']}.html")

    cards = "".join(
        f'<section class="desk-card"><h2 id="{esc(d["id"])}"><a href="{esc(d["id"])}.html">{esc(d["label"])}</a> <span class="dim">{d["count"]}</span></h2>'
        f'<p>{esc(d["for_whom"])}</p><p class="dim">Start with:</p><ol>'
        + "".join(f'<li><a href="../articles/{s["slug"]}.html">{esc(by[s["slug"]]["title"])}</a> <span class="dim">{mins(fa[s["slug"]]["minutes"])}</span></li>' for s in d["start_here"])
        + f'</ol><p><a href="{esc(d["id"])}.html">The whole desk &rarr;</a></p></section>' for d in find["desks"])
    body = (f'<p class="lead">A desk is an audience, not a topic: the people a piece is for, and the question they bring. '
            f'Every article is placed on one desk first and, when it touches another, a second.</p>'
            f'<div class="desk-cards">{cards}</div>'
            f'<h2 id="how">How an article finds its desk</h2><p>{esc(find["rule"]["desks"])}</p>'
            f'<p class="dim">{plural(len(find["vocabulary"]), "controlled subject")}, {plural(len(find["series"]), "series")}, '
            f'{len(find["unmapped"])} raw tags still waiting for the Librarian. The data: <a href="../articles/find.json">articles/find.json</a>.</p>'
            '<style>.desk-cards{display:grid;gap:1rem;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));margin:1.2rem 0}'
            '.desk-card{border:1px solid var(--line);border-radius:10px;padding:1rem 1.1rem;background:var(--panel)}'
            '.desk-card h2{margin:0 0 .5rem;font-size:1.25rem}.desk-card ol{padding-left:1.2rem}.desk-card p{margin:.4rem 0}</style>')
    agent = (f"The five desks of newsroom.sgit.ai, each an audience: " + "; ".join(f"{d['label']} ({d['count']})" for d in find["desks"])
             + f". The data: https://{HOST}/articles/find.json.")
    if write("desks/index.html", newsroom_page("desks/index.html", "The five desks", "Every article placed by the reader it is for.",
                                               body, eyebrow="The newsroom", agent=agent)):
        changed.append("desks/index.html")
    print(f"desks: {len(find['desks'])} desks; {len(changed)} written {changed}")


if __name__ == "__main__":
    main()
