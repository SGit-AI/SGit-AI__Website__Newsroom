#!/usr/bin/env python3
"""The pages of the graph of meaning, under graphs/, written from the derivation's context by fsg_build.build().

Every page answers one question (the grammar's fifth rule): what the newsroom states about one name; what one article
states, as facts and hypotheses; which names have gravity; where the clusters fall against the desks; what the two-way
cut looks like. Nothing here is hand-written HTML: the pages are projections of graphs/data/*.json, which an agent can
read instead.
"""
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

from page import newsroom_page, write, esc, HOST
from fsg import ROOT, SRC, OUT, VERBS, DERIVED_VERBS, CLAIM_KINDS
import md as mdlib

CRUMB = (("The graph of meaning", "graphs/index.html"),)
HEAD = '<link rel="stylesheet" href="{up}graphs/graphs.css">\n'
KIND_ORDER = ("fact", "data-point", "hypothesis", "proposal", "question", "definition", "decision", "limit")
KIND_LABEL = {"fact": "Facts", "data-point": "Data points", "hypothesis": "Hypotheses", "proposal": "Proposals",
              "question": "Questions", "definition": "Definitions", "decision": "Decisions", "limit": "Limits"}
DIMENSIONS = [
    {"no": "0", "name": "The article", "types": "section, paragraph, figure", "verbs": "contains, follows, illustrates",
     "what": "As the owner wrote it: the text, its sections and figures. Not derived here; it is the input.", "new": True,
     "page": None},
    {"no": "1", "name": "The claims", "types": "fact, data-point, hypothesis, proposal, question, definition, decision, limit",
     "verbs": "backs, gives_rise_to, answers, limits, contradicts, supersedes, specifies, and their inverses",
     "what": "What one article states, each claim anchored to its section and a quote. A new dimension: the words are not the article's.",
     "new": True, "page": "claims.html"},
    {"no": "2", "name": "The names and the vocabulary", "types": "13 entity types; concept",
     "verbs": "names / named_in, uses / used_in, defines / defined_in",
     "what": "The things in the world and the newsroom's own ideas that claims are about, one id each across every article. A new dimension: a thing, not a sentence about it. Names and concepts share the verbs, so they are one dimension, not two.",
     "new": True, "page": "names.html"},
    {"no": "3", "name": "The sources", "types": "post, paper, documentation, article, repository, vault, talk, standard, law, news, book, page, video, dataset",
     "verbs": "cites / cited_by", "what": "What the articles rest on outside the newsroom, dated as the article dates it. Its own types and one verb of its own: a dimension, a thin one.",
     "new": True, "page": "sources.html"},
    {"no": "4", "name": "Time", "types": "date", "verbs": "happened_on / dates",
     "what": "The dates the articles turn on. One type, one verb: a dimension by the rule, and the thinnest.", "new": True, "page": "time.html"},
    {"no": "3·", "name": "Gravity, clusters, the cut", "types": "none new: the nodes are the names and concepts of dimension 2",
     "verbs": "shares_articles_with (derived, weighted)", "what": "Queries over dimension 2: which ids two or more articles share, how they cluster when the articles they share are counted, where one cut falls. The vocabulary did not change, so this is dimension 2 at less resolution, not a new one.",
     "new": False, "page": "clusters.html"},
    {"no": "5", "name": "The peaks", "types": "peak", "verbs": "arrives_at / overlooks",
     "what": "The natural places of arrival: a name or idea with high gravity that also bridges clusters. Needed its own words, so the build calls it a dimension, and lists them.",
     "new": True, "page": "peaks.html"},
    {"no": "E", "name": "The editor's layers", "types": "topic, desk, subject, series, section, persona", "verbs": "placed_in / holds",
     "what": "Drawn by hand before the run (six topics, five desks and 44 subjects, eleven series, the sections, the personas). The control the clusters and peaks are scored against.",
     "new": True, "editor": True, "page": "clusters.html#editor"},
]


def up_for(rel):
    return "../" * rel.count("/")


def page(rel, title, description, body, **kw):
    up = up_for(rel)
    kw.setdefault("crumbs", CRUMB)
    kw.setdefault("agent", f"This page is a projection of the JSON under /graphs/data/; read that instead. The grammar and the schema are in /graphs/brief.html.")
    return write(rel, newsroom_page(rel, title, description, body, head=HEAD.format(up=up), **kw))


def chip(ctx, nid, up, cls=""):
    n = ctx["nodes"].get(nid, {})
    g = ctx["grav"].get(nid, {})
    kind = nid.split(":")[0]
    label = esc(n.get("label", nid))
    cnt = g.get("n_articles", 0)
    if cnt >= 2:
        return f'<a class="gm-chip {cls} {"e" if kind == "entity" else ""}" href="{up}graphs/nodes/{node_file(nid)}">{label} <b>{cnt}</b></a>'
    return f'<span class="gm-chip {cls} {"e" if kind == "entity" else ""}">{label}</span>'


def node_file(nid):
    kind, i = nid.split(":", 1)
    return f"{kind}--{i}.html"


def art_link(ctx, slug, up, anchor=None):
    m = ctx["meta"].get(slug, {"title": slug})
    frag = f"#{anchor}" if anchor and anchor != "top" else ""
    return f'<a href="{up}articles/{slug}.html{frag}">{esc(m["title"])}</a>'


def stats(items):
    return '<div class="gm-stats">' + "".join(f'<div class="gm-stat"><div class="n">{esc(str(n))}</div><div class="k">{esc(k)}</div></div>' for n, k in items) + "</div>"


def claim_li(ctx, slug, c, up, show_article=False):
    kind = c["kind"]
    val = ""
    if kind == "data-point" and isinstance(c.get("value"), dict):
        v = c["value"]
        val = f' <span class="v">{esc(fmt_n(v.get("n")))}{(" of " + esc(fmt_n(v["of"]))) if v.get("of") not in (None, "") else ""} {esc(str(v.get("unit", "")))}</span>'
    about = "".join(chip(ctx, a, up) for a in c.get("about", []))
    art = f' <span class="gm-note">in {art_link(ctx, slug, up)}</span>' if show_article else ""
    return (f'<li><span class="gm-kind {kind}">{esc(kind)}</span>{esc(c["text"])}{val}{art}'
            f'<span class="q">“{esc(c["quote"])}” <a href="{up}articles/{slug}.html#{c["section"] if c["section"] != "top" else ""}">§ {esc(c["section"])}</a></span>'
            f'<div class="about gm-chips">{about}</div></li>')


def fmt_n(n):
    if isinstance(n, (int, float)):
        if isinstance(n, float) and not n.is_integer():
            return f"{n:,.2f}".rstrip("0").rstrip(".")
        return f"{int(n):,}"
    return str(n)


# ---------------------------------------------------------------- the hub


def hub(ctx):
    r = ctx["report"]
    up = ""
    s = r["shared"]
    body = stats([(r["articles"], "articles read a second time"), (f'{r["claims"]:,}', "claims, anchored to a quote"),
                  (s["ids_with_gravity"], "names and ideas in two or more articles"), (f'{s["claims_joined_share"]:.0%}', "of claims join another article"),
                  (r["references"]["distinct"], f'outside sources, {r["references"]["domains"]} domains'), (r["clusters"]["n"], "clusters, computed"),
                  (len(r["peaks"]["all"]), "peaks listed"), (f'{r["edges_total"]:,}', "typed edges, every verb with its inverse")])
    body += "<h2 id=\"dimensions\">The dimensions</h2><p>A layer is a new dimension when it needs its own types and verbs. The same vocabulary seen from further away is the same dimension at less resolution, and the build says so rather than inventing a level.</p>"
    body += '<ol class="gm-ladder">'
    for d in DIMENSIONS:
        cls = ' class="editor"' if d.get("editor") else ""
        link = f' <a href="{d["page"]}">open</a>' if d.get("page") else ""
        jump = "" if d["new"] else '<p class="jump">not a new dimension: same types and verbs as the layer below, less resolution</p>'
        body += (f'<li{cls}><span class="no">{esc(d["no"])}</span><b>{esc(d["name"])}</b>{link}<p>{esc(d["what"])}</p>'
                 f'<span class="vocab">types: {esc(d["types"])}<br>verbs: {esc(d["verbs"])}</span>{jump}</li>')
    body += "</ol>"
    body += ("<h2 id=\"pages\">The pages</h2><ul>"
             '<li><a href="map.html">The map</a>: the names and ideas with gravity, laid out and cut in two, and turned in three dimensions.</li>'
             '<li><a href="peaks.html">The peaks</a>: where readers arrive, by gravity and bridging.</li>'
             '<li><a href="clusters.html">The clusters, against the editor\'s layers</a>: what emerged, scored against the desks, topics, sections and personas.</li>'
             '<li><a href="claims.html">The claims</a>: every hypothesis and question in the newsroom, and the shape of the facts.</li>'
             '<li><a href="names.html">The names</a> and <a href="concepts.html">the vocabulary</a>: who and what the articles are about, with their gravity.</li>'
             '<li><a href="sources.html">The sources</a> and <a href="time.html">the dates</a>.</li>'
             '<li><a href="births.html">The births</a>: when each idea first appeared, and how many each article added.</li>'
             '<li><a href="articles/index.html">Every article as facts and hypotheses</a>: one page per article.</li>'
             '<li><a href="brief.html">The standing brief</a>: the grammar, the schema, the rules, the run.</li>'
             '<li><a href="report.html">The emergence report</a>: every number of this run, as the second article scored them.</li>'
             "</ul>")
    body += ("<h2 id=\"data\">The data</h2><p>Every page here is a projection of these files, which an agent can read instead: "
             '<a href="data/report.json">report.json</a> (the numbers), <a href="data/map.json">map.json</a> (the nodes with gravity, their layout, cluster and side), '
             '<a href="data/claims.json">claims.json</a>, <a href="data/names.json">names.json</a>, <a href="data/sources.json">sources.json</a>, '
             '<a href="data/time.json">time.json</a>, <a href="data/edges.json">edges.json</a> (the whole join as typed edges with inverses). '
             'The source files are one per article in the repository, <code>admin/content/graphs/articles/&lt;slug&gt;.json</code>, with the registries beside them.</p>'
             f'<p class="gm-note">Run {esc(r["run"])}, built {esc(r["built"])}, in {r["seconds"]} seconds. The articles that set and scored the expectations: '
             '<a href="../articles/the-graph-of-meaning-a-brief.html">The graph of meaning: a brief</a> and <a href="../articles/the-graph-of-meaning-drawn.html">The graph of meaning, drawn</a>.</p>')
    return page("graphs/index.html", "The graph of meaning", "Every article read a second time as facts, hypotheses, data points, names and sources, joined across the newsroom under one grammar; the dimensions, the clusters, the peaks and the map.",
                body, eyebrow="The newsroom as one graph", crumbs=(), lead="Every article here has a graph of its argument. This is the second reading: what each article states, who and what it names, what it rests on, joined across all of them under one grammar, with the layers above computed rather than drawn.",
                agent="Start with /graphs/data/report.json for the numbers and /graphs/data/edges.json for the whole join; the schema of a source file is in /graphs/brief.html.")


# ---------------------------------------------------------------- claims


def claims_page(ctx):
    r = ctx["report"]; gs = ctx["gs"]; up = "../"
    rel = "graphs/claims.html"
    kinds = r["claim_kinds"]
    body = stats([(f'{r["claims"]:,}', "claims"), (r["claims_per_article"], "per article")] + [(kinds.get(k, 0), KIND_LABEL[k].lower()) for k in KIND_ORDER])
    body += "<h2 id=\"verbs\">The verbs between claims</h2><p>Within an article, the Cartographer joins claims only where the article makes the connection. " + ", ".join(f"<code>{esc(v)}</code> {n}" for v, n in r["claim_verbs"].items()) + f". Every verb has its inverse: " + ", ".join(f"<code>{esc(v)}</code> / <code>{esc(i)}</code>" for v, i in VERBS.items()) + ".</p>"
    for kind, intro in (("hypothesis", "Every hypothesis the owner states as his own: the sentences that begin, in the article, with I think, my hypothesis, I expect."),
                        ("question", "Every question an article leaves open.")):
        items = [(s, c) for s, g in gs.items() for c in g["claims"] if c["kind"] == kind]
        items.sort(key=lambda x: (ctx["meta"].get(x[0], {}).get("date", ""), x[0]))
        body += f'<h2 id="{kind}">{KIND_LABEL[kind]} ({len(items)})</h2><p>{intro}</p><ul class="gm-claims">'
        body += "".join(claim_li(ctx, s, c, up, show_article=True) for s, c in items)
        body += "</ul>"
    # data points: the largest 40 by n, as a table
    dps = [(s, c) for s, g in gs.items() for c in g["claims"] if c["kind"] == "data-point" and isinstance(c.get("value"), dict)]
    body += f'<h2 id="data">Data points ({len(dps)})</h2><p>Every number the articles give that matters to their argument, with its unit and the article\'s date for it. The forty with the most articles behind what they are about, then the rest on each article\'s page.</p>'
    dps.sort(key=lambda x: -max([ctx["grav"].get(a, {}).get("n_articles", 0) for a in x[1].get("about", [])] or [0]))
    body += '<div class="tablewrap"><table class="gm"><thead><tr><th>Value</th><th>Of</th><th>Unit</th><th>As of</th><th>Claim</th><th>Article</th></tr></thead><tbody>'
    for s, c in dps[:40]:
        v = c["value"]
        body += f'<tr><td class="n">{esc(fmt_n(v.get("n")))}</td><td class="n">{esc(fmt_n(v["of"])) if v.get("of") not in (None, "") else ""}</td><td>{esc(str(v.get("unit", "")))}</td><td>{esc(str(v.get("as_of", "")))}</td><td>{esc(c["text"])}</td><td>{art_link(ctx, s, up, c["section"])}</td></tr>'
    body += "</tbody></table></div>"
    body += '<p>The facts, definitions, decisions, proposals and limits are on <a href="articles/index.html">each article\'s page</a> and in <a href="data/claims.json">claims.json</a>.</p>'
    return page(rel, "The claims: facts, data points, hypotheses and the rest", f"{r['claims']:,} claims from {r['articles']} articles, each anchored to a quote: every hypothesis and question, the data points, and the verbs between claims.",
                body, eyebrow="Dimension 1", lead="What the articles state, read as claims of eight kinds. Each is anchored to its section and a quote the validator found in the article word for word.")


# ---------------------------------------------------------------- names, concepts, node pages


def names_page(ctx):
    r = ctx["report"]; up = "../"; grav = ctx["grav"]; nodes = ctx["nodes"]
    ents = [(i, g) for i, g in grav.items() if i.startswith("entity:")]
    ents.sort(key=lambda x: (-x[1]["n_articles"], nodes[x[0]]["label"]))
    body = stats([(len(ents), "names a claim is about"), (sum(1 for _, g in ents if g["n_articles"] >= 2), "in two or more articles"),
                  (r["registry"]["entities"], "in the registry after the merge")] + [(n, t) for t, n in list(r["entity_types"].items())[:5]])
    body += "<p>A name is a thing in the world: a person, an organisation, a product, a model, a standard, a law, a place, an event, a site, a publication, a repository, a vault or a role. One id each across the newsroom; a name in two or more articles has gravity and a page of its own. A private person is never here.</p>"
    bytype = defaultdict(list)
    for i, g in ents:
        bytype[nodes[i].get("type", "")].append((i, g))
    for t, items in sorted(bytype.items(), key=lambda x: -len(x[1])):
        body += f'<h2 id="{esc(t)}">{esc(t.capitalize())} ({len(items)})</h2><div class="gm-chips">' + "".join(chip(ctx, i, up) for i, _ in items) + "</div>"
    return page("graphs/names.html", "The names: who and what the articles are about", f"{len(ents)} names across {r['articles']} articles, by type, with how many articles each is in.",
                body, eyebrow="Dimension 2: names", lead="Every name a claim is about, by type, sized by the articles it is in. A name with gravity opens to what the newsroom states about it.")


def concepts_page(ctx):
    r = ctx["report"]; up = "../"; grav = ctx["grav"]; nodes = ctx["nodes"]; cid = ctx["cid"]
    cons = [(i, g) for i, g in grav.items() if i.startswith("concept:")]
    cons.sort(key=lambda x: (-x[1]["n_articles"], nodes[x[0]]["label"]))
    subjects = {s for m in ctx["meta"].values() for s in m.get("subjects", [])}
    body = stats([(len(cons), "concepts a claim is about"), (sum(1 for _, g in cons if g["n_articles"] >= 2), "with gravity"),
                  (r["registry"]["concepts"], "in the registry after the merge"),
                  (len(r["merge"]["concepts"]["added"]) if r.get("merge") else 0, "added by this run"),
                  ((len(r["merge"]["concepts"]["merged"]) + int(r["merge"]["concepts"].get("merged_count_first_build", 0))) if r.get("merge") else 0, "merged into an existing id")])
    body += "<p>A concept is an idea the newsroom argues with, in its own words: the behaviour policy, the vault, hope or enforcement, the one-way door. The registry started from the editor's 44 controlled subjects and the house terms; the run added what the articles use and the registry did not have.</p>"
    body += '<div class="tablewrap"><table class="gm"><thead><tr><th>Concept</th><th class="n">Articles</th><th class="n">Claims</th><th>First used</th><th>Means</th><th>Controlled subject?</th></tr></thead><tbody>'
    for i, g in cons:
        cidv = i.split(":", 1)[1]
        c = cid.get(cidv, {})
        isub = "yes" if cidv in subjects else ("" if g["n_articles"] < 3 else "candidate for the Librarian")
        name = f'<a href="nodes/{node_file(i)}">{esc(nodes[i]["label"])}</a>' if g["n_articles"] >= 2 else esc(nodes[i]["label"])
        body += f'<tr><td>{name}</td><td class="n">{g["n_articles"]}</td><td class="n">{g["claims"]}</td><td>{esc(g["first_date"] or "")}</td><td class="gm-note">{esc(c.get("means", ""))}</td><td>{isub}</td></tr>'
    body += "</tbody></table></div>"
    if r.get("merge"):
        m = r["merge"]["concepts"]
        if m["merged"]:
            body += "<h2 id=\"merged\">Merged by the run</h2><p>A new id a reader proposed that named an idea the registry already had, folded in with the proposed id kept as an alias.</p><ul>"
            body += "".join(f'<li><code>{esc(x["from"])}</code> into <code>{esc(x["into"])}</code> ({esc(x["label"])}), from {len(x["in"])} article(s)</li>' for x in m["merged"])
            body += "</ul>"
    return page("graphs/concepts.html", "The vocabulary: the newsroom's own ideas, with their gravity", f"{len(cons)} concepts, {sum(1 for _, g in cons if g['n_articles'] >= 2)} in two or more articles; which are controlled subjects and which are candidates.",
                body, eyebrow="Dimension 2: the vocabulary", lead="The ideas the newsroom argues with, one id each, with how many articles use each, when it first appeared, and whether the editor's classification already knows it.")


def node_pages(ctx):
    n = 0
    up = "../../"
    gs, grav, nodes, meta = ctx["gs"], ctx["grav"], ctx["nodes"], ctx["meta"]
    ids = ctx["ids"]; C = ctx["C"]; pos = {i: k for k, i in enumerate(ids)}
    for nid, g in grav.items():
        if g["n_articles"] < 2:
            continue
        nd = nodes[nid]
        kind, i = nid.split(":", 1)
        by_art = defaultdict(list)
        for slug in g["articles"]:
            for c in gs[slug]["claims"]:
                if nid in c.get("about", []):
                    by_art[slug].append(c)
        kinds = Counter(c["kind"] for cs in by_art.values() for c in cs)
        body = stats([(g["n_articles"], "articles"), (g["claims"], "claims about it"), (len(g["desks"]), "desks")] + [(v, KIND_LABEL[k].lower()) for k, v in kinds.most_common(4)])
        if kind == "concept" and nd.get("means"):
            body += f"<p><b>Means:</b> {esc(nd['means'])}</p>"
        if kind == "entity":
            body += f"<p><b>Type:</b> {esc(nd.get('type', ''))}</p>"
        if g.get("defined_in"):
            body += "<p><b>Defined in:</b> " + ", ".join(art_link(ctx, s, up) for s in g["defined_in"]) + "</p>"
        # neighbours: shares articles with
        if nid in pos:
            k = pos[nid]
            nb = sorted(((int(C[k, j]), ids[j]) for j in np.nonzero(C[k])[0] if C[k, j] >= 2), reverse=True)[:16]
            if nb:
                body += '<h2 id="with">Shares articles with</h2><div class="gm-chips">' + "".join(f'<a class="gm-chip" href="{node_file(j)}">{esc(nodes[j]["label"])} <b>{w}</b></a>' for w, j in nb) + "</div>"
        body += '<h2 id="claims">What the newsroom states about it, by article</h2>'
        for slug in g["articles"]:
            m = meta.get(slug, {})
            body += f'<h3>{art_link(ctx, slug, up)} <span class="gm-note">{esc(m.get("date", ""))}</span></h3><ul class="gm-claims">'
            body += "".join(claim_li(ctx, slug, c, up) for c in by_art[slug])
            body += "</ul>"
        rel = f"graphs/nodes/{node_file(nid)}"
        title = nd["label"]
        if page(rel, title, f"What {g['n_articles']} articles state about {title}: {g['claims']} claims, each with its quote.", body,
                eyebrow="A concept of the newsroom's vocabulary" if kind == "concept" else f"A name: {nd.get('type', '')}",
                crumbs=CRUMB + (("The vocabulary" if kind == "concept" else "The names", "graphs/concepts.html" if kind == "concept" else "graphs/names.html"),),
                lead=f"Everything the newsroom states about {esc(title)}, in {g['n_articles']} articles, each claim with the sentence it rests on."):
            n += 1
    return n


# ---------------------------------------------------------------- sources, time


def sources_page(ctx):
    r = ctx["report"]["references"]; up = "../"
    refs = json.loads((OUT / "data" / "sources.json").read_text(encoding="utf-8"))["references"]
    body = stats([(r["distinct"], "distinct sources"), (r["citations"], "citations"), (r["domains"], "domains"), (f'{r["dated_to_day_share"]:.0%}', "dated to the day")]
                 + [(n, k) for k, n in list(r["kinds"].items())[:4]])
    body += "<h2 id=\"domains\">By domain</h2><div class=\"gm-chips\">" + "".join(f'<span class="gm-chip">{esc(d)} <b>{n}</b></span>' for d, n in r["top_domains"]) + "</div>"
    multi = [x for x in refs if len(x["articles"]) >= 2]
    body += f'<h2 id="shared">Sources two or more articles cite ({len(multi)})</h2><div class="tablewrap"><table class="gm"><thead><tr><th>Source</th><th>By</th><th>Date</th><th>Kind</th><th class="n">Articles</th></tr></thead><tbody>'
    for x in multi:
        body += f'<tr><td><a href="{esc(x["url"])}">{esc(x["label"])}</a><br><span class="gm-note">{esc(x["domain"])}</span></td><td>{esc(x.get("by", ""))}</td><td>{esc(str(x.get("date", "")))}</td><td>{esc(str(x.get("ref_kind", "")))}</td><td class="n">{len(x["articles"])}</td></tr>'
    body += "</tbody></table></div>"
    body += f'<p>All {r["distinct"]} sources, with the articles that cite each, are in <a href="data/sources.json">sources.json</a>; each article\'s own are on <a href="articles/index.html">its page</a>.</p>'
    return page("graphs/sources.html", "The sources: what the articles rest on outside the newsroom", f"{r['distinct']} outside sources across {r['domains']} domains, {r['dated_to_day_share']:.0%} dated to the day, and the ones several articles share.",
                body, eyebrow="Dimension 3", lead="Every outside source an article cites, with the date the article gives it. Articles on this site are not sources; they are builds-on edges.")


def time_page(ctx):
    r = ctx["report"]["dates"]; up = "../"
    dates = json.loads((OUT / "data" / "time.json").read_text(encoding="utf-8"))["dates"]
    body = stats([(r["distinct"], "distinct dates"), (sum(len(v) for v in dates.values()), "dated events"), (len(r["by_month"]), "months")])
    months = r["by_month"]
    mx = max(months.values()) if months else 1
    body += '<h2 id="months">Dates by month</h2><div class="tablewrap"><table class="gm"><tbody>'
    for m, n in months.items():
        body += f'<tr><td>{esc(m)}</td><td class="n">{n}</td><td><span style="display:inline-block;height:12px;background:var(--accent);width:{int(300 * n / mx)}px"></span></td></tr>'
    body += "</tbody></table></div>"
    body += '<h2 id="all">Every date</h2><div class="tablewrap"><table class="gm"><thead><tr><th>Date</th><th>What</th><th>Article</th></tr></thead><tbody>'
    for d, items in dates.items():
        for it in items:
            body += f'<tr><td class="n">{esc(d)}</td><td>{esc(it["what"])}</td><td>{art_link(ctx, it["article"], up)}</td></tr>'
    body += "</tbody></table></div>"
    return page("graphs/time.html", "The dates the articles turn on", f"{r['distinct']} distinct dates from the articles, with what happened and which article says so.",
                body, eyebrow="Dimension 4", lead="Every date an article turns on, as the article gives it. One type, one verb: the thinnest dimension, and the one that orders the rest.")


# ---------------------------------------------------------------- clusters, peaks, births


def clusters_page(ctx):
    r = ctx["report"]; up = "../"; nodes = ctx["nodes"]; meta = ctx["meta"]; desks = ctx["desks"]; topics = ctx["topics"]
    cl = r["clusters"]
    body = stats([(cl["n"], "clusters"), (cl["modularity"], "modularity"), (r["shared"]["ids_with_gravity"], "nodes clustered"), (r["articles"], "articles placed by their claims")])
    body += ("<p>The clusters are computed, not drawn: the names and ideas in two or more articles, joined by how many articles they share (normalised so that a name every article uses does not pull everything to itself), grouped by a Louvain pass. "
             "An article's home cluster is where most of what its claims are about sits. Below, each cluster with its members and the desks and topics its articles carry; then the editor's layers scored against them.</p>")
    for c in cl["list"]:
        body += f'<h2 id="c{c["id"]}">Cluster {c["id"]}: {esc(c["label"])}</h2>'
        body += f'<p class="gm-note">{c["n_members"]} nodes · {c["n_articles_home"]} articles call it home · {c["articles_touched"]} articles touch it · desks of those: ' + ", ".join(f"{esc(d)} {n}" for d, n in c["desks"].items()) + "</p>"
        body += '<div class="gm-chips">' + "".join(chip(ctx, m, up) for m in c["members"][:40]) + (f'<span class="gm-chip">and {c["n_members"] - 40} more</span>' if c["n_members"] > 40 else "") + "</div>"
        if c["articles_home"]:
            body += "<details><summary>The articles at home here</summary><ul>" + "".join(f"<li>{art_link(ctx, s, up)}</li>" for s in c["articles_home"]) + "</ul></details>"
    body += '<h2 id="editor">The editor\'s layers, scored</h2><p>For each desk, topic, section and persona: how its articles fall across the clusters. A layer whose articles sit in one or two clusters is confirmed by the join; one spread across many is where the editor and the claims disagree.</p>'
    def purity_table(title, pur, labels, key):
        out = f"<h3>{esc(title)}</h3><div class=\"tablewrap\"><table class=\"gm\"><thead><tr><th>{esc(title)}</th><th class=\"n\">Articles</th><th class=\"n\">In top {key}</th><th>Across clusters</th></tr></thead><tbody>"
        for d, v in sorted(pur.items(), key=lambda x: -x[1]["articles"]):
            lab = labels.get(d, {}).get("label", d) if isinstance(labels.get(d), dict) else d
            out += f'<tr><td>{esc(str(lab))}</td><td class="n">{v["articles"]}</td><td class="n">{v.get("top" + key, v.get("top1", 0)):.0%}</td><td>' + ", ".join(f"c{c} {n}" for c, n in v["clusters"].items()) + "</td></tr>"
        return out + "</tbody></table></div>"
    body += purity_table("Desk", r["purity"]["desks"], desks, "2")
    body += purity_table("Topic", r["purity"]["topics"], topics, "2")
    if r["purity"]["sections"]:
        body += purity_table("Section stream", r["purity"]["sections"], {}, "1")
    if r["purity"]["personas"]:
        body += purity_table("Persona", r["purity"]["personas"], {}, "2")
    body += "<h2 id=\"hubs\">The constant companions</h2><p>Names and ideas in more than a quarter of all articles. They are the frame every article is written in, and they are why the weights are normalised before clustering.</p><div class=\"gm-chips\">" + "".join(chip(ctx, h["id"], up) for h in r["hubs"]) + "</div>"
    return page("graphs/clusters.html", "The clusters, against the editor's layers", f"{cl['n']} clusters of the names and ideas with gravity, computed from the articles they share, and the five desks, six topics, sections and personas scored against them.",
                body, eyebrow="Dimension 2 at less resolution, and the editor's layers", lead="What emerged when the articles that share a name or an idea were counted, beside what the editor drew by hand before the run.")


def peaks_svg(peaks, nodes):
    rows = peaks[:24]
    if not rows:
        return ""
    w, rh, left = 760, 22, 260
    h = rh * len(rows) + 30
    mx = max(p["articles"] for p in rows) or 1
    out = [f'<svg class="gm-map gm-ridge" viewBox="0 0 {w} {h}" role="img" aria-label="The peaks, by articles and clusters touched">']
    for k, p in enumerate(rows):
        y = 10 + k * rh
        bw = int((w - left - 60) * p["articles"] / mx)
        cls = "bar e" if p["kind"] == "entity" else "bar"
        out.append(f'<text x="{left - 8}" y="{y + 15}" text-anchor="end">{esc(p["label"][:38])}</text>'
                   f'<rect class="{cls}" x="{left}" y="{y + 4}" width="{bw}" height="{rh - 8}" rx="3"></rect>'
                   f'<text class="n" x="{left + bw + 6}" y="{y + 15}">{p["articles"]} · {p["clusters_touched"]}</text>')
    out.append(f'<text class="cap" x="{left}" y="{h - 4}">bars: articles; after the dot: clusters touched. teal: an idea; amber: a name.</text></svg>')
    return "".join(out)


def peaks_page(ctx):
    r = ctx["report"]; up = "../"; nodes = ctx["nodes"]
    pk = r["peaks"]
    body = ("<p>A peak is where people arrive: a name or an idea many articles share, that also bridges clusters. Score is articles times clusters touched (through the names and ideas it shares articles with). "
            "Teal bars are ideas, amber bars are names. The constant companions, in more than a quarter of articles, are listed apart on the clusters page: they are the frame, not a destination.</p>")
    body += peaks_svg(pk["all"], nodes)
    body += '<h2 id="all">The peaks, in order</h2><div class="tablewrap"><table class="gm"><thead><tr><th>#</th><th>Peak</th><th>Kind</th><th class="n">Articles</th><th class="n">Claims</th><th class="n">Clusters touched</th><th>Home cluster</th><th>First used</th><th>Desks</th></tr></thead><tbody>'
    for k, p in enumerate(pk["all"], 1):
        body += f'<tr><td class="n">{k}</td><td><a href="nodes/{node_file(p["id"])}">{esc(p["label"])}</a></td><td>{esc(p["kind"] + (" · " + p["type"] if p.get("type") else ""))}</td><td class="n">{p["articles"]}</td><td class="n">{p["claims"]}</td><td class="n">{p["clusters_touched"]}</td><td>c{p["cluster"]}</td><td>{esc(p["first_date"] or "")}</td><td class="gm-note">' + ", ".join(f"{esc(d)} {n}" for d, n in list(p["desks"].items())[:3]) + "</td></tr>"
    body += "</tbody></table></div>"
    body += "<h2 id=\"concepts\">Peaks among the ideas</h2><div class=\"gm-chips\">" + "".join(chip(ctx, p["id"], up) for p in pk["concepts"]) + "</div>"
    body += "<h2 id=\"entities\">Peaks among the names</h2><div class=\"gm-chips\">" + "".join(chip(ctx, p["id"], up) for p in pk["entities"]) + "</div>"
    return page("graphs/peaks.html", "The peaks: where readers arrive", f"The {len(pk['all'])} names and ideas with the most gravity that also bridge the clusters, scored and listed.",
                body, eyebrow="Dimension 5", lead="The natural places of arrival in the newsroom, found by gravity and bridging rather than chosen: a company, a standard, an idea, an area.")


def births_page(ctx):
    r = ctx["report"]["births"]; up = "../"; nodes = ctx["nodes"]
    npa = r["new_per_article"]
    body = stats([(len(r["list"]), "ideas and names with gravity"), (r["last30_new_avg"], "new ids per article, last 30"), (r["last30_new_with_gravity_avg"], "of which with gravity")]
                 + [(n, f"born in {m}") for m, n in r["by_month"].items()])
    # chart: new per article over the sequence
    w, h, pad = 760, 220, 30
    n = len(npa); mx = max((x["new"] for x in npa), default=1) or 1
    bw = max(1.0, (w - 2 * pad) / max(1, n))
    svg = [f'<svg class="gm-map gm-births" viewBox="0 0 {w} {h}" role="img" aria-label="New ids per article, in publication order">']
    for k, x in enumerate(npa):
        hh = (h - 2 * pad) * x["new"] / mx
        hg = (h - 2 * pad) * x["new_with_gravity"] / mx
        svg.append(f'<rect class="g" x="{pad + k * bw:.1f}" y="{h - pad - hh:.1f}" width="{max(1, bw - 1):.1f}" height="{hh:.1f}"><title>{esc(x["slug"])}: {x["new"]} new, {x["new_with_gravity"]} with gravity</title></rect>'
                   f'<rect x="{pad + k * bw:.1f}" y="{h - pad - hg:.1f}" width="{max(1, bw - 1):.1f}" height="{hg:.1f}"></rect>')
    svg.append(f'<text x="{pad}" y="{h - 8}">{esc(npa[0]["date"] if npa else "")}</text><text x="{w - pad}" y="{h - 8}" text-anchor="end">{esc(npa[-1]["date"] if npa else "")}</text>'
               f'<text x="{pad}" y="{pad - 10}">grey: ids new to the newsroom in this article; teal: of those, ones a later article also used (gravity). tallest: {mx}</text></svg>')
    body += "<h2 id=\"chart\">What each article added</h2><p>In publication order. An id is new to the article that first used it; most of what the newest articles use was already there.</p>" + "".join(svg)
    body += '<h2 id="list">The births, in order</h2><div class="tablewrap"><table class="gm"><thead><tr><th>First used</th><th>Idea or name</th><th class="n">Articles since</th><th>Born in</th></tr></thead><tbody>'
    for b in r["list"]:
        body += f'<tr><td class="n">{esc(b["first_date"] or "")}</td><td><a href="nodes/{node_file(b["id"])}">{esc(b["label"])}</a></td><td class="n">{b["articles"]}</td><td>{art_link(ctx, b["first"], up) if b["first"] else ""}</td></tr>'
    body += "</tbody></table></div>"
    return page("graphs/births.html", "The births: when each idea first appeared", "Every name and idea with gravity by the article that first used it, and how many new ids each article added, in order.",
                body, eyebrow="Time, applied to the vocabulary", lead="The Historian's measure for the whole newsroom: which article brought which idea, and how the rate of new ideas has fallen as the vocabulary filled.")


# ---------------------------------------------------------------- the map


def map_svg(ctx, width=900, height=620, labels=28, coords="cut", which="side2"):
    """A static picture of the two-way cut: x is each node's rank along the Fiedler vector (the cut's own axis), y its
    force-layout coordinate; coloured by side, sized by articles, a lobe round each side, the strongest ties drawn."""
    ids, C, W, side, pos, X3, grav, nodes = (ctx[k] for k in ("ids", "C", "W", "side", "pos", "X3", "grav", "nodes"))
    if which == "side2":
        side = ctx["side2"]
    n = len(ids)
    if n == 0:
        return ""
    if coords == "spectral":
        xy = X3[:, :2].copy()
    elif coords == "cut":
        xy = np.column_stack([ctx["xr"], pos[:, 1]])
    else:
        xy = pos.copy()
    lo, hi = xy.min(axis=0), xy.max(axis=0)
    xy = (xy - lo) / np.where(hi - lo == 0, 1, hi - lo)
    pad = 40
    px = pad + xy[:, 0] * (width - 2 * pad)
    py = pad + xy[:, 1] * (height - 2 * pad)
    arts = np.array([grav[i]["n_articles"] for i in ids], dtype=float)
    rad = 2.5 + 2.2 * np.sqrt(arts)
    out = [f'<svg class="gm-map" id="gm-static" viewBox="0 0 {width} {height}" role="img" aria-label="The names and ideas with gravity, cut in two">']
    for s in (0, 1):
        idx = np.nonzero(side == s)[0]
        if len(idx) < 3:
            continue
        cx, cy = px[idx].mean(), py[idx].mean()
        rx, ry = px[idx].std() * 1.6 + 16, py[idx].std() * 1.6 + 16
        out.append(f'<ellipse class="lobe" cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}"></ellipse>')
    thr = np.quantile(W[W > 0], 0.85) if (W > 0).any() else 1
    for a in range(n):
        for b in range(a + 1, n):
            if W[a, b] >= thr:
                out.append(f'<line class="edge{" strong" if side[a] != side[b] else ""}" x1="{px[a]:.1f}" y1="{py[a]:.1f}" x2="{px[b]:.1f}" y2="{py[b]:.1f}"></line>')
    order = np.argsort(-arts)
    for k in order[::-1]:
        out.append(f'<circle class="node s{int(side[k])}" cx="{px[k]:.1f}" cy="{py[k]:.1f}" r="{rad[k]:.1f}"><title>{esc(nodes[ids[k]]["label"])}: {int(arts[k])} articles</title></circle>')
    for rank, k in enumerate(order[:labels]):
        cls = "lbl big" if rank < 10 else "lbl"
        out.append(f'<text class="{cls}" x="{px[k] + rad[k] + 3:.1f}" y="{py[k] + 4:.1f}">{esc(nodes[ids[k]]["label"][:30])}</text>')
    out.append(f'<text class="cap" x="{pad}" y="{height - 12}">teal: one side of the cut; amber: the other; grey: the frame, in more than a quarter of articles, left out of the cut. size: articles. strong teal lines: ties that cross the cut.</text></svg>')
    return "".join(out)


def map_page(ctx):
    r = ctx["report"]; up = "../"
    cut = r["cut"]
    body = ("<p>The names and ideas in two or more articles, joined by the articles they share. In the picture below, left to right is the cut's own axis: every node's place along the Fiedler vector of the graph, which is what divides it in two, with the bridges in the middle; up and down is a force layout. The colours are the cut made without the frame, the names and ideas in more than a quarter of all articles, which are drawn grey. "
            "The interactive map under it is the same data, drawn in the page from <a href=\"data/map.json\">map.json</a> with no library: the cut axis, a force layout or the spectral one, coloured by side or by cluster, hover for a name and click for its page; and a turn in three dimensions on a canvas.</p>")
    body += map_svg(ctx)
    body += '<div class="gm-legend">'
    for h in cut["sides"]:
        body += f'<span><i class="s{h["side"]}"></i>side {h["side"]}: {h["articles"]} articles ({h["share"]:.0%}), {h["n_members"]} nodes; desks ' + ", ".join(f"{esc(d)} {n}" for d, n in list(h["desks"].items())[:3]) + "</span>"
    body += "</div>"
    body += "<h2 id=\"sides\">The two sides</h2>"
    for h in cut["sides"]:
        body += f'<h3>Side {h["side"]}</h3><div class="gm-chips">' + "".join(chip(ctx, m, up) for m in h["members"][:36]) + "</div>"
    c2 = r["cut_without_hubs"]
    body += f'<h2 id="without">The cut without the constant companions</h2><p>The same cut with the {c2["hubs_removed"]} names and ideas in more than a quarter of all articles taken out first (the owner, the voice memo, the vault, the behaviour policy and the rest of the frame). It agrees with the full cut on {c2["agreement_with_full_cut"]:.0%} of nodes, and reads more plainly:</p>'
    for h in c2["sides"]:
        body += f'<p><b>Side {h["side"]}</b>, {h["articles"]} articles ({h["share"]:.0%}), desks ' + ", ".join(f"{esc(d)} {n}" for d, n in list(h["desks"].items())[:3]) + ": " + ", ".join(esc(t) for t in h["top"]) + ".</p>"
    body += "<h2 id=\"bridges\">The bridges</h2><p>Nodes whose ties fall most evenly on both sides of the cut, weighted by how many articles they are in.</p><div class=\"gm-chips\">" + "".join(chip(ctx, b["id"], up) for b in cut["bridges"]) + "</div>"
    body += ('<h2 id="live">The map, live</h2>'
             '<div class="gm-controls"><span>Layout:</span><button data-layout="cut" aria-pressed="true">The cut axis</button><button data-layout="force" aria-pressed="false">Force</button><button data-layout="spectral" aria-pressed="false">Spectral</button>'
             '<span>Colour:</span><button data-colour="side2" aria-pressed="true">The cut, without the frame</button><button data-colour="side" aria-pressed="false">The cut, with it</button><button data-colour="cluster" aria-pressed="false">Clusters</button>'
             '<span>Labels:</span><button data-labels="30" aria-pressed="true">Top 30</button><button data-labels="all" aria-pressed="false">All</button></div>'
             '<svg class="gm-map" id="gm-live" viewBox="0 0 900 620" role="img" aria-label="The map, interactive"></svg>'
             '<div class="gm-pick" id="gm-pick">Hover a node for its name and articles; click to open what the newsroom states about it.</div>'
             '<h2 id="three">The same graph, turned</h2><p>A force layout in three dimensions, so the depth of a cluster is visible rather than inferred. It turns on its own; drag to turn it yourself.</p>'
             '<div class="gm-controls"><button id="gm-spin" aria-pressed="true">Turning</button><span id="gm-3d-note">colour: the cut</span></div>'
             '<canvas class="gm-canvas" id="gm-3d" width="900" height="560"></canvas>'
             '<script src="map.js" defer></script>')
    return page("graphs/map.html", "The map: the newsroom's names and ideas, cut in two", "The names and ideas with gravity, laid out from the articles they share, cut in two by the graph's own structure, and turned in three dimensions.",
                body, eyebrow="Dimension 2, drawn", lead="One picture of the whole: every name and idea two or more articles share, placed by the articles they share, and cut in two by the graph itself rather than by a hand.", wide=True)


# ---------------------------------------------------------------- articles' facts pages


def article_pages(ctx):
    gs, meta = ctx["gs"], ctx["meta"]
    n = 0
    up = "../../"
    index = []
    for slug in sorted(gs, key=lambda s: (meta.get(s, {}).get("date", ""), s), reverse=True):
        g = gs[slug]; m = meta.get(slug, {"title": slug, "date": ""})
        kinds = Counter(c["kind"] for c in g["claims"])
        body = stats([(len(g["claims"]), "claims"), (len(g["entities"]), "names"), (len(g["concepts"]), "concepts"), (len(g.get("references", [])), "outside sources"), (len(g.get("edges", [])), "edges between claims")])
        body += f'<p>The article: {art_link(ctx, slug, up)} ({esc(m["date"])}). Every claim below is the article\'s own, in plain words, with the sentence it rests on and a link to its section.</p>'
        for k in KIND_ORDER:
            items = [c for c in g["claims"] if c["kind"] == k]
            if not items:
                continue
            body += f'<h2 id="{k}">{KIND_LABEL[k]} ({len(items)})</h2><ul class="gm-claims">' + "".join(claim_li(ctx, slug, c, up) for c in items) + "</ul>"
        if g.get("edges"):
            byid = {c["id"]: c for c in g["claims"]}
            body += "<h2 id=\"edges\">How the claims connect</h2><ul>"
            for e in g["edges"]:
                a, b = byid.get(e["from"]), byid.get(e["to"])
                if a and b:
                    body += f'<li><b>{esc(e["from"])}</b> <code>{esc(e["verb"])}</code> <b>{esc(e["to"])}</b>: {esc(a["text"][:90])} … {esc(e["verb"].replace("_", " "))} … {esc(b["text"][:90])}</li>'
            body += "</ul>"
        body += "<h2 id=\"about\">Names and ideas</h2><div class=\"gm-chips\">" + "".join(chip(ctx, f"entity:{x['id']}", up) for x in g["entities"]) + "".join(chip(ctx, f"concept:{x['id']}", up) for x in g["concepts"]) + "</div>"
        if g.get("references"):
            body += "<h2 id=\"sources\">Outside sources</h2><ul>" + "".join(f'<li><a href="{esc(x["url"])}">{esc(x.get("title") or x["url"])}</a>{(", " + esc(x["by"])) if x.get("by") else ""}, {esc(str(x.get("date", "")))} ({esc(str(x.get("kind", "")))})</li>' for x in g["references"]) + "</ul>"
        if g.get("dates"):
            body += "<h2 id=\"dates\">Dates</h2><ul>" + "".join(f'<li><b>{esc(x["date"])}</b> {esc(x["what"])}</li>' for x in g["dates"]) + "</ul>"
        rel = f"graphs/articles/{slug}.html"
        if page(rel, f"As facts and hypotheses: {m['title']}", f"{len(g['claims'])} claims from the article, each with its quote: " + ", ".join(f"{v} {KIND_LABEL[k].lower()}" for k, v in kinds.most_common()),
                body, eyebrow="One article, as its claims", crumbs=CRUMB + (("Every article", "graphs/articles/index.html"),),
                lead=f"The article read a second time: {len(g['claims'])} claims, {len(g['entities'])} names, {len(g['concepts'])} ideas, {len(g.get('references', []))} outside sources.",
                agent=f"The source file is admin/content/graphs/articles/{slug}.json in the repository; the article itself is /articles/{slug}.md."):
            n += 1
        index.append((slug, m, kinds))
    body = "<p>One page per article: what it states, as facts, data points, hypotheses, proposals, questions, definitions, decisions and limits, each with the sentence it rests on.</p><div class=\"tablewrap\"><table class=\"gm\"><thead><tr><th>Date</th><th>Article</th><th class=\"n\">Claims</th><th class=\"n\">Data</th><th class=\"n\">Hyp.</th><th class=\"n\">Limits</th></tr></thead><tbody>"
    for slug, m, kinds in index:
        body += f'<tr><td class="n">{esc(m["date"])}</td><td><a href="{slug}.html">{esc(m["title"])}</a></td><td class="n">{sum(kinds.values())}</td><td class="n">{kinds.get("data-point", 0)}</td><td class="n">{kinds.get("hypothesis", 0)}</td><td class="n">{kinds.get("limit", 0)}</td></tr>'
    body += "</tbody></table></div>"
    if page("graphs/articles/index.html", "Every article as facts and hypotheses", f"{len(index)} articles, each read a second time as its claims.", body, eyebrow="Dimension 1, by article",
            lead="The view the owner asked for first: an article as only its facts, hypotheses, data points and connections, one page each."):
        n += 1
    return n


# ---------------------------------------------------------------- brief and report


def brief_page(ctx):
    text = (SRC / "README.md").read_text(encoding="utf-8")
    text = text.replace("](../../../articles/", "](../articles/")
    html = mdlib.render(text.split("\n", 1)[1])      # the h1 is the page title
    return page("graphs/brief.html", "The graph of meaning: the standing brief", "The brief for every run: the purpose, the grammar, the file beside each article, the rules, the run, and what to expect.",
                html, eyebrow="The brief", lead="The text every run reads first, kept in the repository beside the files it describes as admin/content/graphs/README.md.")


def report_page(ctx):
    r = ctx["report"]
    body = "<p>Every number of this run, as <code>admin/build/fsg.py</code> computed it, and the file it comes from: <a href=\"data/report.json\">report.json</a>. The article that scores the predictions against these: <a href=\"../articles/the-graph-of-meaning-drawn.html\">The graph of meaning, drawn</a>.</p>"
    def table(title, rows):
        return f"<h2>{esc(title)}</h2><div class=\"tablewrap\"><table class=\"gm\"><tbody>" + "".join(f"<tr><td>{esc(str(k))}</td><td class=\"n\">{esc(str(v))}</td></tr>" for k, v in rows) + "</tbody></table></div>"
    body += table("The claims", [("articles", r["articles"]), ("claims", r["claims"]), ("per article", r["claims_per_article"])] + [(KIND_LABEL[k], f'{v} ({r["claim_kind_shares"][k]:.0%})') for k, v in r["claim_kinds"].items()] + [("edges between claims", r["claim_edges"])])
    s = r["shared"]
    body += table("The join", [("ids with gravity (2+ articles)", s["ids_with_gravity"]), ("of which concepts", s["concepts"]), ("of which names", s["entities"]), ("claims about a shared id", f'{s["claims_joined"]} ({s["claims_joined_share"]:.0%})'), ("nodes in the join", r["nodes_total"]), ("typed edges", r["edges_total"]), ("concepts used", r["concepts_used"]), ("names used", r["entities_used"])])
    body += table("The sources", [("distinct", r["references"]["distinct"]), ("citations", r["references"]["citations"]), ("domains", r["references"]["domains"]), ("dated to the day", f'{r["references"]["dated_to_day"]} ({r["references"]["dated_to_day_share"]:.0%})')] + [(d, n) for d, n in r["references"]["top_domains"][:8]])
    body += table("The clusters", [("clusters", r["clusters"]["n"]), ("modularity", r["clusters"]["modularity"])] + [(f'c{c["id"]}: {c["label"]}', f'{c["n_members"]} nodes, {c["n_articles_home"]} articles') for c in r["clusters"]["list"]])
    body += table("The cut", [(f'side {h["side"]}: ' + ", ".join(h["top"][:5]), f'{h["articles"]} articles ({h["share"]:.0%})') for h in r["cut"]["sides"]] + [("bridges", ", ".join(b["label"] for b in r["cut"]["bridges"][:8]))])
    body += table("Desk purity (share of a desk's articles in its top one / top two clusters)", [(d, f'{v["top1"]:.0%} / {v["top2"]:.0%}') for d, v in r["purity"]["desks"].items()])
    body += table("Births", [(f"born in {m}", n) for m, n in r["births"]["by_month"].items()] + [("new ids per article, last 30", r["births"]["last30_new_avg"]), ("of which with gravity", r["births"]["last30_new_with_gravity_avg"])])
    body += table("The first pass of the validator", [(k, v) for k, v in r["first_pass"].items()])
    if r.get("merge"):
        m = r["merge"]
        from fsg_build import merged_count
        body += table("The merge", [("concepts added", len(m["concepts"]["added"])), ("concepts merged into a registry id", merged_count(m, "concepts")), ("names added", len(m["entities"]["added"])), ("names merged into a registry id", merged_count(m, "entities")), ("files rewritten", m["files_rewritten"])])
    return page("graphs/report.html", "The emergence report", "Every number of the run, from report.json.", body, eyebrow="The run, counted", lead=f"Run {esc(r['run'])}, built {esc(r['built'])}.")


def write_pages(ctx):
    n = 0
    for fn in (hub, claims_page, names_page, concepts_page, sources_page, time_page, clusters_page, peaks_page, births_page, map_page, brief_page, report_page):
        if fn(ctx):
            n += 1
    n += node_pages(ctx)
    n += article_pages(ctx)
    return n
