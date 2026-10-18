#!/usr/bin/env python3
"""The graph of meaning: every article read as facts, hypotheses, data points, names and sources, joined across the newsroom.

    python3 admin/build/fsg.py --sections <slug>          print an article's section anchors and headings (for whoever writes its file)
    python3 admin/build/fsg.py --check [<slug> ...]       validate admin/content/graphs/articles/<slug>.json (all of them with no slug)
    python3 admin/build/fsg.py --registry                 print the two registries (concepts and entities) as id, label, aliases
    python3 admin/build/fsg.py --baseline                 the counts before the first run, written as the brief article's data file
    python3 admin/build/fsg.py --report                   the emergence report: counts, shared nodes, gravity, clusters (stdout and graphs/data/report.json)
    python3 admin/build/fsg.py                            build: validate, merge, derive the layers, write graphs/ (pages and JSON twins)

The source of truth is one file per article, admin/content/graphs/articles/<slug>.json, written by the Cartographer
(an agent, under its own name) from the article's markdown twin, and checked here against it: every claim carries a
verbatim quote that must be found in the article, every name resolves to the entity registry or declares itself new,
every concept to the concept registry or declares itself new. The grammar is graphs.sgit.ai's, in short: every edge is
a verb with a named inverse, the generic association edge is banned, properties carry data and never meaning, supersede
and never delete, render the answer to a question and never the whole graph. The standing brief, the schema and the
rules are in admin/content/graphs/README.md; the first run's expectations are the article "The graph of meaning: a
brief" and what came of them is "The graph of meaning, drawn".
"""
import argparse
import html as _html
import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "admin/content/graphs"
ART_SRC = SRC / "articles"
REG = SRC / "registry"
OUT = ROOT / "graphs"

CLAIM_KINDS = ("fact", "data-point", "hypothesis", "proposal", "question", "limit", "definition", "decision")
ENTITY_TYPES = ("person", "organisation", "product", "model", "standard", "law", "place", "event", "site",
                "publication", "repository", "vault", "role")
REF_KINDS = ("post", "paper", "documentation", "article", "repository", "vault", "talk", "standard", "law", "news",
             "book", "page", "video", "dataset")
# Claim-to-claim verbs the Cartographer may write, each with its inverse. Everything else is derived here.
VERBS = {
    "backs": "backed_by",              # a data point or fact backs a claim
    "gives_rise_to": "arises_from",    # a fact gives rise to a hypothesis, a proposal or a question
    "answers": "answered_by",          # a claim answers a question
    "limits": "limited_by",            # a limit limits a claim
    "contradicts": "contradicted_by",  # two claims cannot both hold
    "supersedes": "superseded_by",     # a later claim replaces an earlier one (never delete)
    "specifies": "specified_by",       # a part of a proposal specifies the proposal
}
DERIVED_VERBS = {
    "states": "stated_in",            # article -> claim
    "names": "named_in",              # claim -> entity
    "uses": "used_in",                # claim -> concept
    "cites": "cited_by",              # claim -> reference
    "defines": "defined_in",          # article -> concept
    "builds_on": "built_on_by",       # article -> article (the links the text makes)
    "happened_on": "dates",           # claim -> date
    "placed_in": "holds",             # article -> desk / topic / section (the editor's layers)
}
BANNED = ("relates_to", "relates-to", "related_to", "relates", "related")
LADDER = re.compile(r"\brungs?\b", re.I)


def load(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def norm(s):
    """Text as compared: straight quotes, one space, no case change (a quote is word for word)."""
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("–", "-").replace("—", "-").replace(" ", " ")
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def twin_text(slug):
    """The article's words, from its markdown twin: front matter and the Threads tail removed, links unwrapped."""
    p = ROOT / "articles" / f"{slug}.md"
    if not p.exists():
        return None
    t = p.read_text(encoding="utf-8")
    t = re.split(r"^## Threads\s*$", t, maxsplit=1, flags=re.M)[0]
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", t)
    t = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"[*_`>#]+", "", t)
    return norm(t)


def sections_of(slug):
    """[(anchor, heading)] from the published page's h2 ids, plus 'top' for the opening."""
    p = ROOT / "articles" / f"{slug}.html"
    if not p.exists():
        return []
    h = p.read_text(encoding="utf-8")
    out = [("top", "The opening, before the first heading")]
    for m in re.finditer(r'<h2 id="([^"]+)"[^>]*>(.*?)</h2>', h, re.S):
        out.append((m.group(1), norm(_html.unescape(re.sub(r"<[^>]+>", "", m.group(2))))))
    return out


def registry():
    c = load(REG / "concepts.json")["concepts"]
    e = load(REG / "entities.json")["entities"]
    cid = {x["id"]: x for x in c}
    eid = {x["id"]: x for x in e}
    return cid, eid


def article_files():
    return sorted(ART_SRC.glob("*.json"))


# ---------------------------------------------------------------- check


def check_file(path, cid, eid, verbose=True):
    errs, warns = [], []
    slug = path.stem
    try:
        g = load(path)
    except Exception as ex:  # noqa: BLE001
        return [f"{slug}: not valid JSON ({ex})"], []
    if g.get("slug") != slug:
        errs.append(f"{slug}: slug {g.get('slug')!r} does not match the file name")
    text = twin_text(slug)
    if text is None:
        errs.append(f"{slug}: no markdown twin at articles/{slug}.md")
        return errs, warns
    anchors = {a for a, _ in sections_of(slug)}
    raw = path.read_text(encoding="utf-8")
    if "—" in raw:
        errs.append(f"{slug}: an em-dash in the file")
    for m in LADDER.finditer(raw):
        errs.append(f"{slug}: the ladder word at offset {m.start()}")
    for b in BANNED:
        if f'"{b}"' in raw:
            errs.append(f"{slug}: the banned verb {b!r}")

    ents = {x.get("id"): x for x in g.get("entities", [])}
    cons = {x.get("id"): x for x in g.get("concepts", [])}
    refs = {x.get("id"): x for x in g.get("references", [])}
    for x in g.get("entities", []):
        if not re.fullmatch(r"[a-z0-9][a-z0-9\-\.]*", x.get("id", "")):
            errs.append(f"{slug}: entity id {x.get('id')!r} is not kebab-case")
        if x["id"] in eid:
            if x.get("new"):
                errs.append(f"{slug}: entity {x['id']} is in the registry but marked new")
        else:
            if not x.get("new"):
                errs.append(f"{slug}: entity {x['id']!r} is not in the registry and not marked new")
            if x.get("type") not in ENTITY_TYPES:
                errs.append(f"{slug}: new entity {x['id']} has type {x.get('type')!r}; one of {ENTITY_TYPES}")
            if not x.get("name"):
                errs.append(f"{slug}: new entity {x['id']} has no name")
        if not x.get("role"):
            warns.append(f"{slug}: entity {x['id']} has no role (how the article uses it)")
    for x in g.get("concepts", []):
        if not re.fullmatch(r"[a-z0-9][a-z0-9\-]*", x.get("id", "")):
            errs.append(f"{slug}: concept id {x.get('id')!r} is not kebab-case")
        if x["id"] in cid:
            if x.get("new"):
                errs.append(f"{slug}: concept {x['id']} is in the registry but marked new")
        else:
            if not x.get("new"):
                errs.append(f"{slug}: concept {x['id']!r} is not in the registry and not marked new")
            if not x.get("means") or not x.get("label"):
                errs.append(f"{slug}: new concept {x['id']} needs a label and a one-line means")
    for x in g.get("references", []):
        if not re.fullmatch(r"r\d\d", x.get("id", "")):
            errs.append(f"{slug}: reference id {x.get('id')!r} should be r01, r02, ...")
        if not str(x.get("url", "")).startswith(("http://", "https://")):
            errs.append(f"{slug}: reference {x.get('id')} has no URL")
        if x.get("kind") not in REF_KINDS:
            errs.append(f"{slug}: reference {x.get('id')} has kind {x.get('kind')!r}; one of {REF_KINDS}")
        d = x.get("date", "")
        if d != "undated" and not re.fullmatch(r"\d{4}(-\d{2}(-\d{2})?)?", str(d)):
            errs.append(f"{slug}: reference {x.get('id')} date {d!r} is not YYYY, YYYY-MM, YYYY-MM-DD or undated")
    claims = g.get("claims", [])
    if not 8 <= len(claims) <= 45:
        errs.append(f"{slug}: {len(claims)} claims; the brief asks for 12 to 35, and the file must have 8 to 45")
    ids = Counter(c.get("id") for c in claims)
    for i, n in ids.items():
        if n > 1:
            errs.append(f"{slug}: claim id {i} appears {n} times")
    kinds = Counter()
    for c in claims:
        ci = c.get("id", "?")
        if not re.fullmatch(r"c\d\d", ci):
            errs.append(f"{slug}: claim id {ci!r} should be c01, c02, ...")
        if c.get("kind") not in CLAIM_KINDS:
            errs.append(f"{slug}: claim {ci} has kind {c.get('kind')!r}; one of {CLAIM_KINDS}")
        kinds[c.get("kind")] += 1
        if not c.get("text") or len(c["text"].split()) > 45:
            errs.append(f"{slug}: claim {ci} text missing or over 45 words")
        if c.get("section") not in anchors:
            errs.append(f"{slug}: claim {ci} section {c.get('section')!r} is not an anchor of the page ({', '.join(sorted(anchors))})")
        q = norm(c.get("quote", ""))
        nq = len(q.split())
        if nq < 5 or nq > 40:
            errs.append(f"{slug}: claim {ci} quote is {nq} words; 5 to 40")
        elif q not in text:
            errs.append(f"{slug}: claim {ci} quote is not in the article word for word: {q[:80]!r}")
        for a in c.get("about", []):
            if ":" not in a:
                errs.append(f"{slug}: claim {ci} about {a!r} needs concept: or entity:")
                continue
            kind, i = a.split(":", 1)
            if kind == "concept" and i not in cons:
                errs.append(f"{slug}: claim {ci} is about concept {i!r}, not listed in the file's concepts")
            elif kind == "entity" and i not in ents:
                errs.append(f"{slug}: claim {ci} is about entity {i!r}, not listed in the file's entities")
            elif kind not in ("concept", "entity"):
                errs.append(f"{slug}: claim {ci} about {a!r}: concept: or entity:")
        for r in c.get("refs", []):
            if r not in refs:
                errs.append(f"{slug}: claim {ci} cites {r!r}, not in references")
        if c.get("kind") == "data-point":
            v = c.get("value")
            if not isinstance(v, dict) or "n" not in v:
                errs.append(f"{slug}: data point {ci} needs value {{n, of?, unit, as_of?}}")
            elif not isinstance(v["n"], (int, float)):
                errs.append(f"{slug}: data point {ci} value.n must be a number")
        elif c.get("value"):
            warns.append(f"{slug}: claim {ci} carries a value but is a {c.get('kind')}; make it a data-point?")
    for e in g.get("edges", []):
        if e.get("verb") not in VERBS:
            errs.append(f"{slug}: edge verb {e.get('verb')!r}; one of {sorted(VERBS)}")
        for k in ("from", "to"):
            if e.get(k) not in ids:
                errs.append(f"{slug}: edge {e} names claim {e.get(k)!r} that is not in the file")
    for d in g.get("dates", []):
        if not re.fullmatch(r"\d{4}(-\d{2}(-\d{2})?)?", str(d.get("date", ""))):
            errs.append(f"{slug}: date {d.get('date')!r} is not YYYY, YYYY-MM or YYYY-MM-DD")
        if not d.get("what"):
            errs.append(f"{slug}: date {d.get('date')} has no what")
    if kinds.get("data-point", 0) == 0:
        warns.append(f"{slug}: no data point; an article here usually counts something")
    if kinds.get("limit", 0) == 0:
        warns.append(f"{slug}: no limit; every article has a What this does not claim section")
    used = {a for c in claims for a in c.get("about", [])}
    for i in cons:
        if f"concept:{i}" not in used:
            warns.append(f"{slug}: concept {i} is listed but no claim is about it")
    for i in ents:
        if f"entity:{i}" not in used:
            warns.append(f"{slug}: entity {i} is listed but no claim is about it")
    if verbose and not errs:
        print(f"  ok  {slug}: {len(claims)} claims ({', '.join(f'{k} {n}' for k, n in kinds.most_common())}), "
              f"{len(ents)} entities, {len(cons)} concepts, {len(refs)} references, {len(g.get('edges', []))} edges, "
              f"{sum(1 for x in g.get('entities', []) if x.get('new'))}+{sum(1 for x in g.get('concepts', []) if x.get('new'))} new")
    return errs, warns


def cmd_check(slugs):
    cid, eid = registry()
    files = [ART_SRC / f"{s}.json" for s in slugs] if slugs else article_files()
    errs, warns = [], []
    for f in files:
        if not f.exists():
            errs.append(f"{f.stem}: no file at {f.relative_to(ROOT)}")
            continue
        e, w = check_file(f, cid, eid)
        errs += e
        warns += w
    for w in warns:
        print("  warn", w)
    for e in errs:
        print("  FAIL", e)
    print(f"fsg: {len(files)} files, {len(errs)} errors, {len(warns)} warnings")
    # Every check is a line of the run's record, so the first-pass failures can be counted afterwards.
    import datetime
    log = SRC / "runs" / f"{datetime.date.today().isoformat()}-checks.tsv"
    log.parent.mkdir(exist_ok=True)
    with log.open("a", encoding="utf-8") as fh:
        for f in files:
            fe = [e for e in errs if e.startswith(f.stem + ":")]
            fw = [w for w in warns if w.startswith(f.stem + ":")]
            fh.write(f"{datetime.datetime.now(datetime.UTC).strftime('%H:%M:%S')}\t{f.stem}\t{len(fe)}\t{len(fw)}\t"
                     f"{sum(1 for e in fe if 'word for word' in e)}\n")
    return 1 if errs else 0


def cmd_baseline():
    """The counts the brief article was written from, saved as the article's data file."""
    from urllib.parse import urlparse
    j = load(ROOT / "articles/graphs.json")
    arts = j["articles"]
    labels, kinds, rels, ids, sites, tags = Counter(), Counter(), Counter(), Counter(), Counter(), Counter()
    n = e = 0
    for a in arts:
        g = a["graph"]
        for nd in g.get("nodes", []):
            labels[nd["label"].lower()] += 1; kinds[nd["kind"]] += 1; ids[nd["id"]] += 1; n += 1
        for ed in g.get("edges", []):
            rels[ed["rel"]] += 1; e += 1
        for s in g.get("links", {}).get("sites", []):
            sites[urlparse(s).netloc] += 1
        for t in a.get("tags", []):
            tags[t] += 1
    find = load(ROOT / "articles/find.json")
    words = 0
    for a in arts:
        t = twin_text(a["slug"])
        words += len(t.split()) if t else 0
    out = {
        "what": "The newsroom's graphs before the first run of the graph of meaning, counted on 2026-10-18 by admin/build/fsg.py --baseline over articles/graphs.json, articles/find.json and the markdown twins.",
        "articles": len(arts), "nodes": n, "edges": e, "nodes_per_article": round(n / len(arts), 1),
        "node_kinds": dict(kinds.most_common()), "edge_relations": dict(rels.most_common()),
        "distinct_labels": len(labels), "labels_in_more_than_one_article": sum(1 for c in labels.values() if c > 1),
        "most_shared_labels": labels.most_common(12),
        "tags": len(tags), "tags_used_once": sum(1 for c in tags.values() if c == 1),
        "controlled_subjects": len(find["vocabulary"]), "unmapped_tags": len(find["unmapped"]),
        "desks": len(find["desks"]), "series": len(find["series"]), "formats": len(find["formats"]["labels"]),
        "topics_today": find["topics_today"],
        "outside_citations": sum(sites.values()), "outside_domains": len(sites), "top_domains": sites.most_common(12),
        "words": words,
    }
    dest = ROOT / "admin/content/articles/data/the-graph-of-meaning-a-brief__baseline.json"
    dest.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=1, ensure_ascii=False))
    print("written", dest.relative_to(ROOT))


def cmd_sections(slug):
    for a, h in sections_of(slug):
        print(f"{a:28s} {h}")
    t = twin_text(slug)
    print(f"\n{len(t.split())} words in the twin")


def cmd_registry():
    cid, eid = registry()
    print(f"# {len(cid)} concepts")
    for i, c in cid.items():
        print(f"concept:{i:36s} {c['label']}" + (f"  (also: {', '.join(c.get('aliases', []))})" if c.get("aliases") else ""))
    print(f"\n# {len(eid)} entities")
    for i, e in eid.items():
        print(f"entity:{i:36s} {e['type']:13s} {e['name']}" + (f"  (also: {', '.join(e.get('aliases', []))})" if e.get("aliases") else ""))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sections")
    ap.add_argument("--check", nargs="*")
    ap.add_argument("--registry", action="store_true")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--baseline", action="store_true")
    a = ap.parse_args()
    if a.baseline:
        return cmd_baseline()
    if a.sections:
        return cmd_sections(a.sections)
    if a.check is not None:
        return cmd_check(a.check)
    if a.registry:
        return cmd_registry()
    try:
        from fsg_build import build  # noqa: E402  (the derivation, in its own file)
    except ImportError:
        sys.exit("fsg: the derivation (admin/build/fsg_build.py) is not here yet; --check, --sections and --registry work")
    return build(report_only=a.report)


if __name__ == "__main__":
    sys.exit(main() or 0)
