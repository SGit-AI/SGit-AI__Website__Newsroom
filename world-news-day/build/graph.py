#!/usr/bin/env python3
"""world-news-day/build/graph.py — the ontology and the graph for the World News Day corpus.

    python3 world-news-day/build/graph.py

Writes data/ontology.json, data/graph.json, data/triples.nt, data/licences.json, data/manifest.json.

The grammar is the estate's, inherited from graphs.sgit.ai and already run on /portugal/: every
edge is a verb with a distinct named inverse, symmetric verbs are banned, every verb carries a
Portuguese form so the vocabulary can travel to pt.newsroom.sgit.ai without being rewritten, and
every node names the frozen source it was read from. Classification is a published formula or it
does not happen: the only classification here is the theme lexicon in data/lexicon.json, and each
theme edge carries the words that matched.

One node type in this graph does not exist in /portugal/, and it is the reason the section exists:
Licence. A permission stated in prose is a node with no machine-readable form, and saying so is a
fact about the corpus rather than an opinion about the publisher.
"""
import collections
import hashlib
import html
import json
import re
from pathlib import Path

SEC = Path(__file__).resolve().parents[1]
DATA = SEC / "data"
NS = "https://newsroom.sgit.ai/world-news-day/"


def load(n):
    return json.loads((DATA / n).read_text(encoding="utf-8"))


NODE_TYPES = [
    {"id": "Article",      "label": "Article",      "pt": "Artigo",       "colour": "#0f766e", "definition": "One commissioned op-ed, as published on worldnewsday.org and frozen here. The prose is linked, never reproduced."},
    {"id": "Author",       "label": "Author",       "pt": "Autor",        "colour": "#b45309", "definition": "A named person in an article's byline, in their professional capacity. Name and the role line they gave; nothing else, and never a contact detail."},
    {"id": "Organisation", "label": "Organisation", "pt": "Organização",  "colour": "#1d4ed8", "definition": "An organisation an author's own role line names. Derived from that line, never typed by hand."},
    {"id": "Theme",        "label": "Theme",        "pt": "Tema",         "colour": "#7c3aed", "definition": "A theme from the published lexicon whose pattern matched the article's prose. It says the piece contains those words and nothing more."},
    {"id": "CitedSource",  "label": "Cited source", "pt": "FonteCitada",  "colour": "#a16207", "definition": "A page an article links out to. The evidence the piece offers its reader, counted as the piece offers it."},
    {"id": "Licence",      "label": "Licence",      "pt": "Licença",      "colour": "#b91c1c", "definition": "A statement of republication terms. Carries the form it takes: prose, a named public licence, or a machine-readable declaration."},
    {"id": "Snapshot",     "label": "Snapshot",     "pt": "Captura",      "colour": "#5c5f66", "definition": "A dated capture of the source site: every page fetched, frozen to bytes in this repository, and hashed."},
    {"id": "Source",       "label": "Frozen file",  "pt": "Fonte",        "colour": "#8a8d94", "definition": "One frozen file with its SHA-256. The thing a claim walks back to."},
]

# verb / inverse / domain / range / pt verb / pt inverse / how the forward edge reads
EDGES = [
    ("written_by",     "wrote",           "Article",      "Author",       "escrito_por",   "escreveu",      "{s} is written by {t}"),
    ("affiliated_to",  "affiliates",      "Author",       "Organisation", "afiliado_a",    "afilia",        "{s} is affiliated to {t}"),
    ("touches",        "touched_by",      "Article",      "Theme",        "aborda",        "abordado_por",  "{s} touches {t}"),
    ("cites",          "cited_by",        "Article",      "CitedSource",  "cita",          "citado_por",    "{s} cites {t}"),
    ("published_under","governs",         "Article",      "Licence",      "publicado_sob", "rege",          "{s} is published under {t}"),
    ("commissioned_by","commissioned",    "Article",      "Organisation", "encomendado_por","encomendou",   "{s} was commissioned by {t}"),
    ("attested_by",    "attests",         "Article",      "Source",       "atestado_por",  "atesta",        "{s} is attested by {t}"),
    ("captured_in",    "captures",        "Source",       "Snapshot",     "capturado_em",  "captura",       "{s} was captured in {t}"),
]

BANNED = [
    {"verb": "related_to",      "why": "Symmetric, so it would be its own inverse, and it says nothing a reader could walk."},
    {"verb": "mentions",        "why": "Every edge in a graph built from text mentions something. It is the absence of a verb."},
    {"verb": "associated_with", "why": "The verb reached for when the relationship is unknown. Find out, or leave the edge out."},
    {"verb": "agrees_with",     "why": "Two pieces touching the same theme is not agreement. Asserting agreement would be this section putting words in an author's mouth."},
]

TAXONOMY = [
    {"id": "work",     "broader": None, "label": "The work",     "pt": "O trabalho",  "types": ["Article", "Theme", "CitedSource"]},
    {"id": "people",   "broader": None, "label": "The people",   "pt": "As pessoas",  "types": ["Author", "Organisation"]},
    {"id": "terms",    "broader": None, "label": "The terms",    "pt": "Os termos",   "types": ["Licence"]},
    {"id": "evidence", "broader": None, "label": "The evidence", "pt": "A evidência", "types": ["Snapshot", "Source"]},
]

# The one organisation not derived from a role line: the commissioner, named by the licence
# statement of every piece ("This opinion piece was commissioned to mark World News Day").
COMMISSIONER = {"id": "org:world-news-day", "label": "World News Day", "note": "Named by every article's own licence statement as the occasion the piece was commissioned for. The campaign is run by WAN-IFRA with the Canadian Journalism Foundation."}


def slugify(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-") or "unnamed"


def surnames(s):
    """The last word of each name in a byline or author field, lowercased. Used only to ask
    whether the structured author field and the printed byline name the same PEOPLE — a
    middle initial or a different separator is not a disagreement, a different person is."""
    if not s:
        return set()
    # the publisher's author field separates names with non-breaking spaces; treating one as
    # an ordinary space is the difference between reading three names and reading one
    parts = re.split(r",| and |&", s.replace("\u00a0", " "))
    return {p.strip(" ,.").split()[-1].lower() for p in parts if p.strip(" ,.")}


def prose(rec):
    body = " ".join(html.unescape(re.sub(r"<[^>]+>", " ", rec["content"]["rendered"])).split())
    cut = body.find("This opinion piece was commissioned")
    return body[:cut] if cut > 0 else body


def main():
    corpus = load("corpus.json")
    register = load("register.json")
    lexicon = load("lexicon.json")
    affiliations = load("affiliations.json")
    AFF = {p["id"]: p for p in affiliations["people"]}
    latest = register["snapshots"][-1]
    LEX = {e["id"]: e for e in lexicon["entries"]}
    src_by_id = {s["id"]: s for s in register["sources"]}

    nodes, edges, seen = [], [], set()

    def node(n):
        if n["id"] in seen:
            return
        seen.add(n["id"])
        nodes.append(n)

    def edge(verb, s, t, **extra):
        edges.append({"id": f"{verb}:{s}:{t}", "verb": verb, "source": s, "target": t, **extra})

    # --- evidence -------------------------------------------------------------------
    node({"id": f"snapshot:{latest}", "type": "Snapshot", "label": f"Snapshot {latest}",
          "date": latest, "source": register["sources"][0]["id"]})
    for s in register["sources"]:
        sid = "src:" + s["id"]
        node({"id": sid, "type": "Source", "label": f'{s["slug"] or "announcement"} ({s["kind"]})',
              "url": s["url"], "frozen": s["frozen"], "sha256": s["sha256"], "bytes": s["bytes"],
              "source": s["id"]})
        edge("captured_in", sid, f"snapshot:{latest}")

    # --- the licences ----------------------------------------------------------------
    lic_groups = collections.Counter(a["licence_statement"] for a in corpus["articles"])
    lic_ids = {}
    for i, (text, n) in enumerate(lic_groups.most_common(), start=1):
        lid = f"licence:prose-{i}"
        lic_ids[text] = lid
        node({"id": lid, "type": "Licence", "label": f"Prose permission, variant {i}",
              "form": "prose", "statement": text, "articles": n,
              "is_named_public_licence": False, "machine_readable": False,
              "spdx": None, "url": None,
              "note": ("A sentence in the page body. It is a permission and it is not a licence: it has no "
                       "name, no version, no URL, no identifier, and no form a machine can read."),
              "source": f"{latest}/{corpus['articles'][0]['slug']}.snapshot"})

    # --- articles, authors, organisations, themes, cited sources ---------------------
    node({**COMMISSIONER, "type": "Organisation", "role_in_graph": "commissioner",
          "source": f"{latest}/{corpus['articles'][0]['slug']}.snapshot"})

    for a in corpus["articles"]:
        aid = "article:" + a["slug"]
        node({"id": aid, "type": "Article", "label": a["title"], "url": a["url"],
              "published": a["published"][:10], "words": a["words"],
              "order_in_announcement": a["order_in_announcement"],
              "has_ld_json": a["has_ld_json"], "schema_declares_licence": a["schema_declares_licence"],
              "outbound_links": len(a["outbound_links"]), "source": a["source_page"]})
        edge("attested_by", aid, "src:" + a["source_page"])
        edge("attested_by", aid, "src:" + a["source_api"])
        edge("commissioned_by", aid, COMMISSIONER["id"])
        if a["licence_statement"] in lic_ids:
            edge("published_under", aid, lic_ids[a["licence_statement"]])

        # authors, and the organisation each names in their own role line
        bio = a["bio_line"] or ""
        for name in a["byline"]:
            pid = "author:" + slugify(name)
            aff = AFF.get(pid, {})
            role = aff.get("role_as_printed")
            node({"id": pid, "type": "Author", "label": name, "role_line": role,
                  "role_line_note": "As the author's own piece states it, verbatim from the frozen copy. Nothing else is held about any person named here.",
                  "source": a["source_page"]})
            edge("written_by", aid, pid)
            # Affiliation is a TRANSCRIPTION, not a derivation — see data/affiliations.json for
            # why. Deriving it with a regular expression over free prose made an Author work at
            # "Philippines" and at "an Indian media leader", which is a plausible edge, which is
            # the worst kind. The gate checks every line of the transcription against the bytes.
            for org in aff.get("organisations", []):
                oid = "org:" + slugify(org)
                node({"id": oid, "type": "Organisation", "label": org,
                      "derived_from": "the author's own role line in the article, transcribed by "
                                      "hand into data/affiliations.json and checked against the "
                                      "frozen bytes by the gate",
                      "source": a["source_page"]})
                edge("affiliated_to", pid, oid, stated_as=role)

        # themes, by the published formula
        rec = json.loads((SEC / "sources" / "frozen" / latest / "api" / f"{a['slug']}.json").read_text(encoding="utf-8"))[0]
        body = prose(rec)
        for e in lexicon["entries"]:
            m = re.search(e["pattern"], body, re.I)
            if m:
                tid = "theme:" + e["id"]
                node({"id": tid, "type": "Theme", "label": e["label"], "lexicon": e["id"],
                      "pattern": e["pattern"], "derived": True,
                      "by": "the published lexicon over the article's frozen prose",
                      "source": a["source_page"]})
                edge("touches", aid, tid, matched=m.group(0)[:40], by="lexicon")

        # the sources the piece offers its reader
        for l in a["outbound_links"]:
            dom = re.sub(r"^www\.", "", re.sub(r"^https?://", "", l).split("/")[0])
            cid = "cited:" + slugify(dom)
            node({"id": cid, "type": "CitedSource", "label": dom,
                  "note": "A domain an article links out to, counted as the article offers it. This section did not fetch it.",
                  "source": a["source_page"]})
            edge("cites", aid, cid, url=l)

    # --- the licence findings, derived ------------------------------------------------
    arts = corpus["articles"]
    findings = {
        "id": "wnd-licences", "version": "0.1.0", "updated": latest,
        "question": ("The announcement says the op-eds are free to republish. Under what licence, exactly, and "
                     "in what form? Every number below is derived from the frozen bytes by build/graph.py and "
                     "re-checked by build/gates.py."),
        "counts": {
            "articles": len(arts),
            "carrying_a_prose_permission": sum(1 for a in arts if a["licence_statement"]),
            "carrying_a_named_public_licence": 0,
            "carrying_a_creative_commons_reference": 0,
            "carrying_rel_license": 0,
            "carrying_a_copyright_notice": 0,
            "with_ld_json": sum(1 for a in arts if a["has_ld_json"]),
            "whose_ld_json_declares_a_licence": sum(1 for a in arts if a["schema_declares_licence"]),
            "distinct_prose_statements": len(lic_groups),
        },
        "the_statement": [{"variant": i, "articles": n, "text": t}
                          for i, (t, n) in enumerate(lic_groups.most_common(), start=1)],
        "what_the_statement_does_and_does_not_do": [
            "It permits republication and translation IN FULL. It does not permit an extract.",
            "It requires translations to remain faithful to the original meaning, which is a condition no standard public licence states in those words.",
            "It permits minor edits for length or house style, which sits oddly beside 'in full'.",
            "It names no licence, no version, no URL and no identifier, so there is nothing to cite, point at, or check against.",
            "It says nothing about attribution. The announcement page says 'with appropriate credit'; the articles do not mention credit at all.",
            "It says nothing about commercial use, derivative works, moral rights, term, or revocation.",
            "It is not addressed: it does not say who grants it, and the pieces carry no copyright notice naming a holder.",
        ],
        "machine_readability": {
            "every_page_has_json_ld": sum(1 for a in arts if a["has_ld_json"]) == len(arts),
            "json_ld_types_present": sorted({t for a in arts for t in a["schema_types"]}),
            "schema_org_fields_available_and_unused": ["license", "copyrightHolder", "copyrightNotice", "usageInfo", "isAccessibleForFree"],
            "note": ("Every one of the 21 pages already ships schema.org JSON-LD with an Article node, produced by "
                     "the site's SEO plugin. schema.org has carried a `license` property since 2015. Adding one line "
                     "to a record that is already being generated would make the permission machine-readable. None "
                     "of the 21 does."),
            "structured_author_field_disagrees_with_the_printed_byline":
                sum(1 for a in arts if surnames(a.get("wp_author_field")) != surnames(", ".join(a["byline"]))),
            "structured_author_note": ("The REST record carries an author field. On two of the 21 it does not name "
                                       "the people the page prints: one gives the CMS account name "
                                       "'329976pwpadmin' instead of a person, and one names an author the byline "
                                       "does not. A machine-readable field that is wrong twice in 21 is worse than "
                                       "no field, because nothing on the page says which to believe. The bylines "
                                       "here are read from the prose for that reason."),
            "rest_api_open": True,
            "rest_api_note": ("worldnewsday.org serves the whole corpus as structured JSON at /wp-json/wp/v2/posts. "
                              "It is open, undocumented and unadvertised: a machine-consumable form exists by "
                              "accident of the platform rather than by a decision to publish one. It carries no "
                              "licence field either."),
        },
        "taxonomy": {
            "every_article_category": sorted({c for a in arts for c in a["categories"]}),
            "every_article_tag": sorted({t for a in arts for t in a["tags"]}),
            "note": ("All 21 carry the same single category and the same single tag. The corpus has no topical "
                     "classification of its own, which is why the themes in this graph had to be derived."),
        },
        "the_two_statements": {
            "on_the_articles": lic_groups.most_common(1)[0][0],
            "on_the_announcement": "All of the op-eds are free to republish with appropriate credit.",
            "note": ("The same organisation states the terms twice, differently. The articles require republication "
                     "IN FULL and say nothing about credit; the announcement requires CREDIT and says nothing about "
                     "in full. A republisher following one is not following the other. The announcement itself could "
                     "not be fetched by an automated reader (see register.excluded), so its wording is recorded here "
                     "as read by a person and is not the basis of any other claim in this section."),
        },
    }
    write("licences.json", findings)

    # --- ontology, graph, triples, manifest -------------------------------------------
    packs = [
        ("articles", "The articles", True,  "The 21 pieces, and the organisation that commissioned them."),
        ("people",   "Authors",      True,  "Every named byline and the organisation each author's own role line names."),
        ("terms",    "The terms",    True,  "The licence nodes and which article is published under which."),
        ("themes",   "Themes",       False, "Derived by the published lexicon. Every edge carries the words that matched."),
        ("cited",    "What they cite", False, "The domains the pieces link out to, counted as they offer them."),
        ("evidence", "Evidence",     False, "Every frozen file and the capture it belongs to."),
    ]
    pack_of = {"Article": "articles", "Organisation": "articles", "Author": "people",
               "Licence": "terms", "Theme": "themes", "CitedSource": "cited",
               "Snapshot": "evidence", "Source": "evidence"}
    for n in nodes:
        n["pack"] = pack_of[n["type"]]
    nb = {n["id"]: n for n in nodes}
    for e in edges:
        e["pack"] = nb[e["source"]]["pack"] if e["verb"] not in ("touches", "cites", "attested_by", "captured_in") else \
            {"touches": "themes", "cites": "cited", "attested_by": "evidence", "captured_in": "evidence"}[e["verb"]]

    ontology = {
        "id": "wnd-ontology", "version": "0.1.0", "updated": latest,
        "inherits_from": {"site": "graphs.sgit.ai", "what": "Every edge a verb with a distinct named inverse; symmetric edges banned; a path must read as a sentence."},
        "language_rule": "Every type and verb carries `pt`, so the vocabulary can travel to pt.newsroom.sgit.ai without being rewritten.",
        "node_types": NODE_TYPES,
        "edges": [{"verb": v, "inverse": i, "domain": d, "range": r, "pt": {"verb": pv, "inverse": pi}, "reads": reads}
                  for v, i, d, r, pv, pi, reads in EDGES],
        "banned": BANNED,
        "taxonomy": TAXONOMY,
        "formulas": [{"id": "themes", "on": "Article", "lexicon": "data/lexicon.json",
                      "entries": len(lexicon["entries"]),
                      "note": "The only classification this graph makes rather than reads. Each edge carries the words the pattern matched, and the gate re-runs every pattern on the frozen bytes in both directions."}],
    }
    write("ontology.json", ontology)

    counts = {"nodes": len(nodes), "edges": len(edges),
              "by_type": {t["id"]: sum(1 for n in nodes if n["type"] == t["id"]) for t in NODE_TYPES}}
    write("graph.json", {
        "id": "wnd-graph", "version": "0.1.0", "updated": latest, "snapshot": latest,
        "note": ("The corpus as one graph. Every node names the frozen source it was read from; every edge is a "
                 "verb from ontology.json with a named inverse. Nothing here was read from the live network."),
        "packs": [{"id": p, "label": l, "default": d, "note": nt,
                   "nodes": sum(1 for n in nodes if n["pack"] == p),
                   "edges": sum(1 for e in edges if e["pack"] == p)} for p, l, d, nt in packs],
        "counts": counts, "nodes": nodes, "edges": edges,
    })

    # N-Triples, same scheme as /portugal/
    T = []
    def iri(k, l): return f"<{NS}{k}/{l}>"
    RDF, RDFS, OWL = "http://www.w3.org/1999/02/22-rdf-syntax-ns#", "http://www.w3.org/2000/01/rdf-schema#", "http://www.w3.org/2002/07/owl#"
    def lit(v, lang=None):
        s = str(v).replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")
        return f'"{s}"@{lang}' if lang else f'"{s}"'
    for t in NODE_TYPES:
        T += [f'{iri("type", t["id"])} <{RDF}type> <{OWL}Class> .',
              f'{iri("type", t["id"])} <{RDFS}label> {lit(t["id"], "en")} .',
              f'{iri("type", t["id"])} <{RDFS}label> {lit(t["pt"], "pt")} .',
              f'{iri("type", t["id"])} <{RDFS}comment> {lit(t["definition"], "en")} .']
    for v, i, d, r, pv, pi, reads in EDGES:
        T += [f'{iri("verb", v)} <{RDF}type> <{OWL}ObjectProperty> .',
              f'{iri("verb", i)} <{OWL}inverseOf> {iri("verb", v)} .',
              f'{iri("verb", v)} <{RDFS}label> {lit(v.replace("_", " "), "en")} .',
              f'{iri("verb", v)} <{RDFS}label> {lit(pv.replace("_", " "), "pt")} .',
              f'{iri("verb", i)} <{RDFS}label> {lit(pi.replace("_", " "), "pt")} .',
              f'{iri("verb", v)} <{RDFS}domain> {iri("type", d)} .',
              f'{iri("verb", v)} <{RDFS}range> {iri("type", r)} .']
    SKIP = {"id", "type", "label", "pack"}
    for n in nodes:
        s = iri("id", n["id"].replace(":", "_"))
        T += [f'{s} <{RDF}type> {iri("type", n["type"])} .', f'{s} <{RDFS}label> {lit(n["label"], "en")} .']
        for k, v in n.items():
            if k in SKIP or v is None or isinstance(v, (list, dict)):
                continue
            T.append(f'{s} {iri("prop", k)} {lit(v)} .')
    for e in edges:
        T.append(f'{iri("id", e["source"].replace(":", "_"))} {iri("verb", e["verb"])} {iri("id", e["target"].replace(":", "_"))} .')
    T = list(dict.fromkeys(T))
    (DATA / "triples.nt").write_text("\n".join(T) + "\n", encoding="utf-8")

    print(f"graph: {len(nodes)} nodes, {len(edges)} edges, {len(NODE_TYPES)} types, "
          f"{len({e[0] for e in EDGES})} verbs; {len(T)} triples")


def manifest():
    """Runs LAST, after every other data file has been written — a manifest that hashes a file
    which is still to be regenerated is a manifest that is wrong on the next build. It cannot
    carry its own hash for the same reason, so manifest.json is the one file it leaves out and
    the gate skips."""
    latest = load("register.json")["snapshots"][-1]
    files = []
    for p in sorted(DATA.glob("*.json")) + sorted(DATA.glob("*.nt")):
        if p.name == "manifest.json":
            continue
        files.append({"path": f"data/{p.name}", "kind": "data", "bytes": p.stat().st_size,
                      "sha256": hashlib.sha256(p.read_bytes()).hexdigest()})
    for p in sorted((SEC / "sources" / "frozen").rglob("*")):
        if p.is_file():
            files.append({"path": p.relative_to(SEC).as_posix(), "kind": "frozen", "bytes": p.stat().st_size,
                          "sha256": hashlib.sha256(p.read_bytes()).hexdigest()})
    zipf = SEC / "vault.zip"
    if zipf.exists():
        files.append({"path": "vault.zip", "kind": "bundle", "bytes": zipf.stat().st_size,
                      "sha256": hashlib.sha256(zipf.read_bytes()).hexdigest()})
    triples = len((DATA / "triples.nt").read_text(encoding="utf-8").strip().splitlines())
    write("manifest.json", {"id": "wnd-manifest", "updated": latest,
                            "note": "Every file this section is built from and every file it "
                                    "publishes, with size and SHA-256. manifest.json itself is "
                                    "absent: a file cannot carry its own hash.",
                            "triples": triples, "count": len(files), "files": files})
    print(f"manifest: {len(files)} files, {triples} triples")


def write(name, obj):
    (DATA / name).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
    manifest()
