#!/usr/bin/env python3
"""world-news-day/ — the section gate.

    python3 world-news-day/build/gates.py

Runs before the whole-site gate (`node admin/build/validate.js`), which this section must
also pass.

This section is different from every other one on the site in a way the gate has to answer
for. /portugal/ publishes claims about people from pages those people's event published.
Here we hold 21 complete opinion pieces, written by named editors at named organisations,
under a permission that is prose rather than a licence. The whole value of the section is
that it says, with evidence, what that permission is and is not — so the two things that
would destroy it are:

  1. **republishing the prose** while arguing that the terms for republishing are unclear, and
  2. **overstating the finding** — saying "no licence" where the bytes say "a prose permission
     naming no licence", or reporting a count we did not re-derive.

Every check below exists for one of those two. The counts on the licence page are re-derived
here from the frozen bytes rather than read from the JSON that the page was built from, so a
number can never be published that the evidence does not produce twice.
"""
import gzip
import hashlib
import html as _html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SEC = ROOT / "world-news-day"
DATA = SEC / "data"

errors = []


def load(n):
    return json.loads((DATA / n).read_text(encoding="utf-8"))


register = load("register.json")
corpus = load("corpus.json")
licences = load("licences.json")
ontology = load("ontology.json")
graph = load("graph.json")
lexicon = load("lexicon.json")
affiliations = load("affiliations.json")
contacts = load("contacts.json")
contact_rules = load("contact-rules.json")
corrections = load("corrections.json")
manifest = load("manifest.json")

LATEST = register["snapshots"][-1]
src_by_id = {s["id"]: s for s in register["sources"]}

# Our own pages only. The frozen copies are somebody else's bytes held as evidence; they
# carry no house chrome and never will, and they are stored with a .snapshot extension so
# they are neither served nor indexed as pages of this site.
pages = sorted(p for p in SEC.rglob("*.html") if "sources/frozen/" not in p.as_posix())


def api_rec(slug):
    f = SEC / "sources" / "frozen" / LATEST / "api" / f"{slug}.json"
    return json.loads(f.read_text(encoding="utf-8"))[0]


def prose(rec):
    """The article's own words, minus the permission statement. Must match graph.py exactly,
    or a theme edge re-derives against different text than it was derived from."""
    body = " ".join(_html.unescape(re.sub(r"<[^>]+>", " ", rec["content"]["rendered"])).split())
    cut = body.find("This opinion piece was commissioned")
    return body[:cut] if cut > 0 else body


# --- 1. every frozen file still hashes to what the register says ------------------
# The section rests on this. If a frozen copy has been edited, moved or lost, every count
# on the licence page is unsupported and the build must not ship.
for s in register["sources"]:
    f = SEC / s["frozen"]
    if not f.exists():
        errors.append(f'register: {s["id"]} names a frozen copy that is missing: {s["frozen"]}')
        continue
    actual = hashlib.sha256(f.read_bytes()).hexdigest()
    if actual != s["sha256"]:
        errors.append(f'register: {s["frozen"]} no longer hashes to its registered SHA-256 '
                      f'(registered {s["sha256"][:16]}…, actual {actual[:16]}…) — the frozen copy '
                      f'was modified, which breaks every claim resting on it')
    if s["bytes"] != f.stat().st_size:
        errors.append(f'register: {s["id"]} records {s["bytes"]} bytes, the file is {f.stat().st_size}')
if register["count"] != len(register["sources"]):
    errors.append("register: count disagrees with the list")

# --- 2. the announcement is either held or excluded with a reason — never neither --------
# It is the page that grants the permission and states the terms a third way, and it sits
# behind an intermittent JavaScript-challenge WAF. Until v0.4.2 this gate REQUIRED it to be
# excluded, which encoded a refusal observed twice as a permanent property of the page. It
# now requires only that the section account for it, either way. See data/corrections.json.
held = [s for s in register["sources"] if s["kind"] == "announcement"]
excluded_urls = {x["url"] for x in register.get("excluded", [])}
if not held and not excluded_urls:
    errors.append("register: the announcement is neither held as a source nor recorded as "
                  "excluded — a page this section quotes must be accounted for either way")
if held and licences["the_two_statements"]["on_the_announcement"]:
    ann = " ".join(_html.unescape(re.sub(
        r"<[^>]+>", " ", (SEC / held[0]["frozen"]).read_text(encoding="utf-8", errors="replace"))).split())
    if licences["the_two_statements"]["on_the_announcement"] not in ann:
        errors.append("licences: the announcement's terms are quoted but are not in its frozen "
                      "bytes verbatim — the quotation drifted")
for x in register.get("excluded", []):
    if not x.get("why"):
        errors.append(f'register: excluded "{x["id"]}" gives no reason')
    if any(s["url"] == x["url"] for s in register["sources"]):
        errors.append(f'register: "{x["id"]}" is both excluded and registered as held')

# --- 3. every article traces to two frozen files that are in the register -------------
for a in corpus["articles"]:
    for key in ("source_page", "source_api"):
        if a[key] not in src_by_id:
            errors.append(f'corpus: "{a["slug"]}" names {key} "{a[key]}", which is not registered')
if corpus["count"] != len(corpus["articles"]):
    errors.append("corpus: count disagrees with the list")
if corpus["total_words"] != sum(a["words"] for a in corpus["articles"]):
    errors.append("corpus: total_words disagrees with the articles")
if len({a["slug"] for a in corpus["articles"]}) != len(corpus["articles"]):
    errors.append("corpus: two articles share a slug")
if sorted(a["order_in_announcement"] for a in corpus["articles"]) != list(range(1, len(corpus["articles"]) + 1)):
    errors.append("corpus: the announcement order is not a clean 1..n — that order is data and "
                  "must survive the extractor intact")

# --- 4. the prose is NOT republished ------------------------------------------------
# The section's whole posture. We hold 21 complete opinion pieces and publish none of them.
# Checked where it can actually be enforced: against our own generated pages, by taking
# runs of words from each frozen article and looking for them. A 12-word run is long enough
# that a coincidence is implausible and short enough to catch a paragraph lifted "as an
# illustration". The permission statement itself is exempt: quoting the terms verbatim is
# the finding, and a reader cannot check our reading of them against anything else.
RUN = 12
# Two bounded exemptions, both for the same reason: the quotation IS the claim, and a reader
# cannot check our reading of it against anything else.
#
#   1. the permission statement — the licence finding is a reading of that sentence;
#   2. each author's role line, exactly as data/affiliations.json records it — the affiliation
#      claim is a reading of that line, and the gate already checks every one of them against
#      the frozen bytes verbatim in check 10b.
#
# Nothing else is exempt, the exempt strings are enumerated rather than pattern-matched, and
# together they are under 400 words of the corpus's 20,060. An exemption that could grow by
# accident would be the end of this rule.
permission_words = set()
for v in licences["the_statement"]:
    permission_words.add(" ".join(v["text"].lower().split()))
permission_words.add(" ".join(licences["the_two_statements"]["on_the_announcement"].lower().split()))
for r in affiliations["people"]:
    permission_words.add(" ".join(r["role_as_printed"].lower().split()))
_exempt_words = sum(len(x.split()) for x in permission_words)
if _exempt_words > 400:
    errors.append(f"gate: the quotation exemption now covers {_exempt_words} words of the "
                  f"corpus. It is bounded at 400 on purpose — an exemption that grows by "
                  f"accident is how a no-republication rule stops being one")
page_text = {p: " ".join(re.sub(r"<[^>]+>", " ", p.read_text(encoding="utf-8")).lower().split())
             for p in pages}
for a in corpus["articles"]:
    words = prose(api_rec(a["slug"])).lower().split()
    runs = [" ".join(words[i:i + RUN]) for i in range(0, max(1, len(words) - RUN), 7)]
    for p, t in page_text.items():
        for r in runs:
            if r and r in t and not any(r in perm for perm in permission_words):
                errors.append(f'{p.relative_to(ROOT)}: reproduces {RUN} consecutive words of '
                              f'"{a["title"]}" ("{r[:60]}…") — this section links to the pieces '
                              f'and republishes none of them')
                break
# and nothing long leaks into the data either: a node carrying a paragraph is a reproduction
# with extra steps. The licence statement and the author's own role line are the two fields
# that are quoted on purpose, and both are bounded.
for a in corpus["articles"]:
    for k, v in a.items():
        if not isinstance(v, str):
            continue
        cap = {"licence_statement": 400, "bio_line": 500}.get(k, 200)
        if len(v) > cap:
            errors.append(f'corpus: "{a["slug"]}" field "{k}" is {len(v)} chars (cap {cap}) — '
                          f'the corpus records what a piece IS, never what it says')

# --- 5. the permission statement is in the bytes, verbatim ----------------------------
# Every claim on the licence page is a claim about this sentence. It is quoted, so it is
# checked against the article it is quoted from, one article at a time.
for a in corpus["articles"]:
    rec = api_rec(a["slug"])
    body = " ".join(_html.unescape(re.sub(r"<[^>]+>", " ", rec["content"]["rendered"])).split())
    if a["licence_statement"] and a["licence_statement"] not in body:
        errors.append(f'corpus: the permission statement recorded for "{a["slug"]}" is not in '
                      f'its frozen bytes verbatim — the quotation drifted')
    if not a["licence_statement"]:
        errors.append(f'corpus: "{a["slug"]}" carries no permission statement, but the section '
                      f'claims all {corpus["count"]} do')
variants = {" ".join(a["licence_statement"].split()) for a in corpus["articles"]}
if len(variants) != licences["counts"]["distinct_prose_statements"]:
    errors.append(f'licences: counts.distinct_prose_statements says '
                  f'{licences["counts"]["distinct_prose_statements"]}, the bytes give {len(variants)}')
for v in licences["the_statement"]:
    got = sum(1 for a in corpus["articles"] if " ".join(a["licence_statement"].split()) == " ".join(v["text"].split()))
    if got != v["articles"]:
        errors.append(f'licences: variant {v["variant"]} is claimed on {v["articles"]} articles, '
                      f'the bytes give {got}')

# --- 6. every licence count re-derives from the frozen HTML ---------------------------
# Not read back from the JSON the page was built from — re-derived here, from the bytes, by
# a second implementation. A published number that only one program can produce is an
# assertion; a number two programs produce from the same bytes is a finding.
CC = re.compile(r"creativecommons\.org|creative commons|\bCC[ -]?BY\b", re.I)
RELLIC = re.compile(r'rel=["\'][^"\']*\blicense\b', re.I)
COPYR = re.compile(r"All Rights Reserved|©\s*20\d\d|&copy;\s*20\d\d|\(c\)\s*20\d\d", re.I)
LDJSON = re.compile(r'<script[^>]+type=["\']application/ld\+json["\']', re.I)
recount = {"creativecommons": 0, "rel_license": 0, "copyright_notice": 0, "ld_json": 0,
           "ld_json_licence": 0}
for a in corpus["articles"]:
    t = (SEC / "sources" / "frozen" / a["source_page"]).read_text(encoding="utf-8", errors="replace")
    if CC.search(t):
        recount["creativecommons"] += 1
    if RELLIC.search(t):
        recount["rel_license"] += 1
    if COPYR.search(t):
        recount["copyright_notice"] += 1
    if LDJSON.search(t):
        recount["ld_json"] += 1
    for blk in re.findall(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>', t, re.S | re.I):
        if re.search(r'"(license|usageInfo|copyrightNotice)"\s*:', blk):
            recount["ld_json_licence"] += 1
            break
C = licences["counts"]
for key, claimed, label in [
    ("creativecommons", C["carrying_a_creative_commons_reference"], "a Creative Commons reference"),
    ("rel_license", C["carrying_rel_license"], 'rel="license"'),
    ("copyright_notice", C["carrying_a_copyright_notice"], "a copyright notice"),
    ("ld_json", C["with_ld_json"], "JSON-LD"),
    ("ld_json_licence", C["whose_ld_json_declares_a_licence"], "a licence field in its JSON-LD"),
]:
    if recount[key] != claimed:
        errors.append(f'licences: the page says {claimed} of {corpus["count"]} carry {label}; '
                      f're-deriving from the frozen HTML gives {recount[key]}')
if C["articles"] != corpus["count"] or C["carrying_a_prose_permission"] != corpus["count"]:
    errors.append("licences: the article counts disagree with the corpus")
if C["carrying_a_named_public_licence"] != 0 and not licences.get("named_licence_evidence"):
    errors.append("licences: a named public licence is claimed with nothing pointing at it")
# The finding is "no formal licence", never "no permission". Saying the second would be
# false and would misrepresent an organisation that did in fact grant one.
for p in pages:
    t = " ".join(re.sub(r"<[^>]+>", " ", p.read_text(encoding="utf-8")).split())
    m = re.search(r"\b(no permission to republish|cannot be republished|not free to republish|"
                  r"refuse[sd]? permission)\b", t, re.I)
    if m:
        errors.append(f'{p.relative_to(ROOT)}: says "{m.group(0)}" — the permission is real and '
                      f'generous; the finding is about its FORM, not its existence')

# --- 7. every theme edge re-derives from the frozen bytes, in both directions ----------
# The one classification this section makes rather than reads. The published pattern is run
# again on the frozen prose: no match, no edge; every match, an edge. A theme that survives
# only because it is in the JSON is an opinion with a node id.
LEX = {e["id"]: e for e in lexicon["entries"]}
gnode = {n["id"]: n for n in graph["nodes"]}
theme_edges = [e for e in graph["edges"] if e["verb"] == "touches"]
for e in theme_edges:
    tn = gnode.get(e["target"])
    if not tn or tn.get("lexicon") not in LEX:
        errors.append(f'themes: edge {e["id"]} points at a node with no lexicon entry')
        continue
    if not e.get("matched"):
        errors.append(f'themes: edge {e["id"]} carries no matched words — a derived edge must '
                      f'show the words it is derived from')
for a in corpus["articles"]:
    aid = "article:" + a["slug"]
    body = prose(api_rec(a["slug"]))
    have = {gnode[e["target"]]["lexicon"] for e in theme_edges if e["source"] == aid}
    for lid, le in LEX.items():
        hit = re.search(le["pattern"], body, re.I)
        if hit and lid not in have:
            errors.append(f'themes: lexicon "{lid}" matches "{a["slug"]}" and the graph has no '
                          f'edge — a theme left out by hand')
        if not hit and lid in have:
            errors.append(f'themes: the graph gives "{a["slug"]}" theme "{lid}" and the pattern '
                          f'does not match its frozen prose — the edge would be invented')
for e in lexicon["entries"]:
    try:
        re.compile(e["pattern"])
    except re.error as ex:
        errors.append(f'lexicon: "{e["id"]}" is not a valid pattern: {ex}')
    if not e.get("note") and not lexicon.get("note"):
        errors.append(f'lexicon: "{e["id"]}" has no note saying what a match does and does not mean')

# --- 8. the graph conforms to its ontology --------------------------------------------
# Inherited grammar: every edge is a verb with a distinct named inverse, every verb carries
# a pt form, no banned verb is in use, every node is a declared type and names a frozen
# source. A plausible edge is indistinguishable from a true one once it is in the file.
verbs = {e["verb"] for e in ontology["edges"]}
inverses = {e["inverse"] for e in ontology["edges"]}
banned = {b["verb"] for b in ontology["banned"]}
types = {t["id"] for t in ontology["node_types"]}
for e in ontology["edges"]:
    if e["verb"] == e["inverse"]:
        errors.append(f'ontology: "{e["verb"]}" is its own inverse — symmetric edges are banned')
    if not e.get("pt", {}).get("verb") or not e.get("pt", {}).get("inverse"):
        errors.append(f'ontology: "{e["verb"]}" has no Portuguese — every verb carries pt from '
                      f'day one, or the vocabulary does not travel to pt.newsroom')
    if e["verb"] in banned:
        errors.append(f'ontology: "{e["verb"]}" is both declared and banned')
    if e["domain"] not in types or e["range"] not in types:
        errors.append(f'ontology: "{e["verb"]}" has a domain or range that is not a declared type')
for t in ontology["node_types"]:
    if not t.get("pt"):
        errors.append(f'ontology: type "{t["id"]}" has no Portuguese label')
    if not t.get("definition"):
        errors.append(f'ontology: type "{t["id"]}" has no definition — an undefined type is a colour')
if len(inverses) != len(ontology["edges"]):
    errors.append("ontology: two verbs share an inverse")
domain_range = {(e["verb"], e["domain"], e["range"]) for e in ontology["edges"]}
for n in graph["nodes"]:
    if n["type"] not in types:
        errors.append(f'graph: node {n["id"]} has unknown type "{n["type"]}"')
    if not n.get("source"):
        errors.append(f'graph: node {n["id"]} names no source — a node with no way back to bytes '
                      f'is a drawing')
    elif n["source"] not in src_by_id:
        errors.append(f'graph: node {n["id"]} names source "{n["source"]}", which is not registered')
for e in graph["edges"]:
    if e["verb"] in banned:
        errors.append(f'graph: banned verb "{e["verb"]}" is in use')
    elif e["verb"] not in verbs:
        hint = " (that is an inverse; edges are stored forwards)" if e["verb"] in inverses else ""
        errors.append(f'graph: edge verb "{e["verb"]}" is not in the ontology{hint}')
    if e["source"] not in gnode or e["target"] not in gnode:
        errors.append(f'graph: edge {e["id"]} has an endpoint that is not a node')
    elif e["verb"] in verbs and \
            (e["verb"], gnode[e["source"]]["type"], gnode[e["target"]]["type"]) not in domain_range:
        errors.append(f'graph: {e["verb"]} from {gnode[e["source"]]["type"]} to '
                      f'{gnode[e["target"]]["type"]} is outside the verb\'s declared domain/range')
if graph["counts"]["nodes"] != len(graph["nodes"]) or graph["counts"]["edges"] != len(graph["edges"]):
    errors.append("graph: counts disagree with the lists")
for pk in graph["packs"]:
    if pk["nodes"] != sum(1 for n in graph["nodes"] if n["pack"] == pk["id"]):
        errors.append(f'graph: pack "{pk["id"]}" node count is stale')
    if pk["edges"] != sum(1 for e in graph["edges"] if e["pack"] == pk["id"]):
        errors.append(f'graph: pack "{pk["id"]}" edge count is stale')
# every article in the corpus is in the graph, and every Article node is in the corpus
slugs = {a["slug"] for a in corpus["articles"]}
gart = {n["id"].split(":", 1)[1] for n in graph["nodes"] if n["type"] == "Article"}
if gart != slugs:
    errors.append("graph: the Article nodes are not exactly the corpus — "
                  f'{sorted(gart - slugs) or sorted(slugs - gart)}')

# --- 9. nobody is given an opinion they did not write ----------------------------------
# The banned verb that is specific to this corpus. Two pieces touching the same theme is not
# agreement, and this section will not put words in a named editor's mouth. Checked on the
# pages as well as in the graph, because the sentence is the more likely place for it.
AGREE = re.compile(r"\b(agree[s]? with|endorses|backs|sides with|shares the view of|"
                   r"aligned with|in agreement with)\b", re.I)
for p in pages:
    t = " ".join(re.sub(r"<[^>]+>", " ", p.read_text(encoding="utf-8")).split())
    for m in AGREE.finditer(t):
        window = t[max(0, m.start() - 120):m.start()].lower()
        if "banned" in window or "does not" in window or "we do not" in window or "never" in window:
            continue
        errors.append(f'{p.relative_to(ROOT)}: "{m.group(0)}" — an alignment claim about a named '
                      f'author. This section reports shared vocabulary and nothing further')
        break

# --- 10. authors and organisations come from the pieces, not from anywhere else ---------
# Every Author node is a byline the piece printed; every Organisation an author's own role
# line named. The gate re-reads the bylines rather than trusting the node list.
bylines = set()
for a in corpus["articles"]:
    for b in a["byline"]:
        bylines.add(b)
for n in graph["nodes"]:
    if n["type"] == "Author" and n["label"] not in bylines:
        errors.append(f'graph: author "{n["label"]}" is not a byline on any article in the corpus')
    if n["type"] == "Organisation" and not n.get("derived_from") and n["id"] != "org:world-news-day":
        errors.append(f'graph: organisation {n["id"]} does not say where it came from')

# --- 10b. every affiliation is a transcription that survives being checked ---------------
# This is the one place in the section where a human wrote something down rather than a
# program deriving it, and the reason is on the file: derivation produced an Author who works
# at "Philippines". A transcription is a claim, so it is checked against the bytes it claims
# to come from, in both directions, one line at a time.
bio_of = {a["slug"]: a["bio_line"] or "" for a in corpus["articles"]}
aff_by_id = {}
for r in affiliations["people"]:
    aff_by_id[r["id"]] = r
    if r["author"] not in bylines:
        errors.append(f'affiliations: "{r["author"]}" is not a byline anywhere in the corpus')
    if r["stated_in"] not in bio_of:
        errors.append(f'affiliations: "{r["author"]}" cites article "{r["stated_in"]}", which is not in the corpus')
        continue
    if r["role_as_printed"] not in bio_of[r["stated_in"]]:
        errors.append(f'affiliations: the role line transcribed for "{r["author"]}" is not in '
                      f'{r["stated_in"]} verbatim — the transcription drifted from the bytes')
    for org in r["organisations"]:
        if org not in r["role_as_printed"]:
            errors.append(f'affiliations: "{org}" is not inside the role line printed for '
                          f'"{r["author"]}" — an organisation may only come from that line')
    if not r["organisations"] and not r.get("no_current_organisation_named"):
        errors.append(f'affiliations: "{r["author"]}" has no organisation and no reason given')
if affiliations["count"] != len(affiliations["people"]):
    errors.append("affiliations: count disagrees with the list")
if {p["id"] for p in affiliations["people"]} != {n["id"] for n in graph["nodes"] if n["type"] == "Author"}:
    errors.append("affiliations: the file and the graph do not name the same authors")
# and the graph holds exactly the edges the file states — no more, no fewer
stated = {(r["id"], "org:" + re.sub(r"[^a-z0-9]+", "-", o.lower()).strip("-"))
          for r in affiliations["people"] for o in r["organisations"]}
built = {(e["source"], e["target"]) for e in graph["edges"] if e["verb"] == "affiliated_to"}
if stated != built:
    errors.append(f'affiliations: the graph\'s affiliated_to edges are not the transcription — '
                  f'{sorted(built - stated) or sorted(stated - built)}')

# --- 10c. the structured author field is counted, not assumed --------------------------
def _surnames(s):
    if not s:
        return set()
    return {x.strip(" ,.").split()[-1].lower()
            for x in re.split(r",| and |&", s.replace("\u00a0", " ")) if x.strip(" ,.")}


disagree = sum(1 for a in corpus["articles"]
               if _surnames(a.get("wp_author_field")) != _surnames(", ".join(a["byline"])))
claimed = licences["machine_readability"].get("structured_author_field_disagrees_with_the_printed_byline")
if claimed != disagree:
    errors.append(f'licences: the page says the structured author field disagrees with the '
                  f'printed byline on {claimed} pieces; re-deriving gives {disagree}')

# --- 11. no contact detail for any natural person reaches the data ----------------------
# The same rule as /portugal/: enforced where the data is parsed, not where it is rendered.
# These are 40-odd named journalists; a mail address that reaches a JSON file is one careless
# loop away from being published, and the contacts work this section will do next belongs on
# organisations, not on individuals.
CONTACT = {
    "email": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    "phone": re.compile(r"\+\d[\d ()‑-]{9,}\d"),
}
for name in ["corpus.json", "graph.json", "licences.json"]:
    text = (DATA / name).read_text(encoding="utf-8")
    for kind, pat in CONTACT.items():
        m = pat.search(text)
        if m:
            errors.append(f'{name}: contains what looks like a personal {kind} '
                          f'("{m.group(0)[:40]}") — refused at extraction time, not hidden at '
                          f'render time')

# --- 12. the manifest is complete and current -------------------------------------------
for f in manifest["files"]:
    p = SEC / f["path"]
    if not p.exists():
        errors.append(f'manifest: lists {f["path"]}, which does not exist')
        continue
    if f.get("sha256") and hashlib.sha256(p.read_bytes()).hexdigest() != f["sha256"]:
        errors.append(f'manifest: {f["path"]} no longer hashes to its recorded SHA-256')
if manifest["count"] != len(manifest["files"]):
    errors.append("manifest: count disagrees with the list")

# --- 12b. this section declares its own licence in the field it says the corpus is missing --
# The argument on the licence page is that schema.org's `license` property costs one line and
# is worth adding. Publishing that on a page that does not have one would be the cheapest kind
# of hypocrisy, so every page here carries the declaration, and losing it fails the build.
for p in pages:
    t = p.read_text(encoding="utf-8")
    blocks = re.findall(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>', t, re.S | re.I)
    if not blocks:
        errors.append(f'{p.relative_to(ROOT)}: no JSON-LD — this section asks the corpus to '
                      f'publish machine-readable terms and must do it itself')
        continue
    try:
        rec = json.loads(blocks[0])
    except json.JSONDecodeError as ex:
        errors.append(f'{p.relative_to(ROOT)}: its JSON-LD does not parse ({ex})')
        continue
    for field in ("license", "copyrightHolder", "copyrightNotice", "usageInfo", "isAccessibleForFree"):
        if not rec.get(field) and rec.get(field) is not False:
            errors.append(f'{p.relative_to(ROOT)}: its JSON-LD has no "{field}"')
    if not str(rec.get("license", "")).startswith("https://creativecommons.org/licenses/"):
        errors.append(f'{p.relative_to(ROOT)}: its declared licence is not a named public '
                      f'licence with a URL — which is the whole finding of this section')
    # and the notice must keep saying what the licence does NOT cover, or it reads as a claim
    # over twenty-one pieces that are not ours
    if "op-eds" not in str(rec.get("copyrightNotice", "")):
        errors.append(f'{p.relative_to(ROOT)}: its copyright notice does not say that the '
                      f'licence covers our description and not the op-eds')
    if 'rel="license"' not in t:
        errors.append(f'{p.relative_to(ROOT)}: no rel="license" link — the HTML mechanism this '
                      f'section counts as unused on all 21')


# --- 12c. the contacts map obeys its own published rules -------------------------------
# A contacts list is where a publication does damage if it is careless, so every address is
# re-derived from the frozen bytes and re-tested against the published rules here. An address
# that only exists in contacts.json is an address somebody typed.
ROLE = set(contact_rules["role_local_parts"])


def _second_level(host):
    parts = host.lower().replace("www.", "").split(".")
    if len(parts) >= 3 and len(parts[-1]) == 2 and parts[-2] in {"co", "com", "org", "net", "gov", "ac"}:
        return parts[-3]
    return parts[-2] if len(parts) >= 2 else parts[0]


MAILRE = re.compile(r"\b([A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,})\b")
author_words = {w.lower() for r in affiliations["people"] for w in r["author"].split() if len(w) > 2}
for o in contacts["organisations"]:
    blob = ""
    for f in o.get("frozen", []):
        path = SEC / f["path"]
        if not path.exists():
            errors.append(f'contacts: {o["org"]} names {f["path"]}, which is missing')
            continue
        raw = gzip.decompress(path.read_bytes()) if path.suffix == ".gz" else path.read_bytes()
        if hashlib.sha256(raw).hexdigest() != f["sha256"]:
            errors.append(f'contacts: {f["path"]} no longer hashes to its recorded SHA-256 '
                          f'(the hash is of the original bytes, decompressed)')
        blob += raw.decode("utf-8", "replace")
    for a in o["addresses"]:
        local, _, dom = a.partition("@")
        if a not in blob.lower():
            errors.append(f'contacts: "{a}" is published for {o["org"]} and is not in the '
                          f'frozen bytes — an address nobody can check is an address somebody typed')
        if local not in ROLE and local != _second_level(o.get("domain", "")):
            errors.append(f'contacts: "{a}" is published and its local part is not a role name '
                          f'from data/contact-rules.json')
        if _second_level(dom) != _second_level(o.get("domain", "")):
            errors.append(f'contacts: "{a}" is published for {o["org"]} but is not on its domain')
        if local.lower() in author_words or any(w in local.lower() for w in author_words):
            errors.append(f'contacts: "{a}" contains an author\'s name — this section publishes '
                          f'no personal contact detail for any natural person')
    if o["addresses"] and not o.get("established"):
        errors.append(f'contacts: {o["org"]} has published addresses and no established site')
    if not o.get("established") and not o.get("why_none"):
        errors.append(f'contacts: {o["org"]} is unestablished and gives no reason')
    for which, rec in (o.get("bytes_not_retained") or {}).items():
        if rec["not_role_addresses"] < contact_rules["bytes_not_retained_rule"]["threshold"]:
            errors.append(f'contacts: {o["org"]} withheld {which} bytes with only '
                          f'{rec["not_role_addresses"]} personal addresses — below the published '
                          f'threshold, so the rule was not what decided it')
        if not rec.get("sha256"):
            errors.append(f'contacts: {o["org"]} withheld {which} bytes without recording a hash '
                          f'— then nobody can re-fetch and check the count')
C = contacts["counts"]
if C["role_addresses_published"] != sum(len(o["addresses"]) for o in contacts["organisations"]):
    errors.append("contacts: the published-address count is stale")
if C["organisations"] != len(contacts["organisations"]):
    errors.append("contacts: the organisation count is stale")
if contacts["from_the_corpus_alone"]["carrying_an_author_contact"] != 0:
    errors.append("contacts: the corpus is claimed to carry an author contact; nothing in this "
                  "section supports that")
# no frozen file that the rule says must not be retained is in the tree after all
for o in contacts["organisations"]:
    for which in (o.get("bytes_not_retained") or {}):
        base = o["slug"] + ("" if which == "home" else "-contact") + ".snapshot"
        for cand in (base, base + ".gz"):
            if (SEC / "sources" / "frozen" / LATEST / "orgs" / cand).exists():
                errors.append(f'contacts: {cand} was withheld by the rule and is in the tree anyway')

# --- 12d. corrections name a version, a claim and what it says now ----------------------
# This publication argues that a correction which does not reach what it disproved is not a
# correction. A section that records one without saying where it was wrong has not made one.
for c in corrections["corrections"]:
    for field in ("id", "wrong_in", "fixed_in", "we_said", "what_was_wrong", "the_rule_it_produced"):
        if not c.get(field):
            errors.append(f'corrections: "{c.get("id", "?")}" has no "{field}"')
    if not c.get("where"):
        errors.append(f'corrections: "{c.get("id", "?")}" does not say which pages carried the error')
if corrections["count"] != len(corrections["corrections"]):
    errors.append("corrections: count disagrees with the list")
# and the corrected claim must be gone from the pages it was on
GONE = re.compile(r"the one page in the beat a machine cannot read|"
                  r"HTTP 307 and no body", re.I)
# Quoting the withdrawn claim in order to withdraw it is the correction, not the error. The
# check is that the claim never appears WITHOUT the correction around it.
MENDED = re.compile(r"correct|we got wrong|too strong|until v0\.4|withdrawn|no longer", re.I)
for p in pages:
    body = p.read_text(encoding="utf-8")
    for m in GONE.finditer(body):
        if not MENDED.search(body[max(0, m.start() - 700):m.end() + 700]):
            errors.append(f'{p.relative_to(ROOT)}: repeats a claim corrected in '
                          f'data/corrections.json with no correction beside it — a correction '
                          f'that does not reach the page that made the claim is not a correction')
            break

# --- 12e. the agent surface's copy of the bundle hash is not stale -----------------------
# llms.txt names the vault's size and hash. A hash one build out of date tells a reader their
# download is corrupt, which is worse than publishing none.
vault = load("vault.json")
llms = (ROOT / "llms.txt").read_text(encoding="utf-8")
if vault["sha256"] not in llms:
    errors.append("llms.txt does not carry the current vault.zip SHA-256 — run build.py, which "
                  "stamps it, rather than editing it by hand")
zipf = SEC / "vault.zip"
if zipf.exists() and hashlib.sha256(zipf.read_bytes()).hexdigest() != vault["sha256"]:
    errors.append("vault.zip does not hash to what data/vault.json records")

# --- 12f. what is published about the vaults is a READ key, never a vault key ------------
# The safety model of this section in one check. A read key is a one-way derivative that
# grants read and only read; a vault key is write access to everything. They are both strings
# in a JSON file, which is precisely why this is a gate and not a habit.
outreach_vault = load("outreach-vault.json")
for name, rec in (("vault.json", vault), ("outreach-vault.json", outreach_vault)):
    blob = json.dumps(rec)
    if "sgit_private_vault_" in blob or re.search(r"sgit_private_read_", blob):
        errors.append(f'{name}: contains a PRIVATE key — only sgit_public_read_ keys are ever '
                      f'published, and a vault key is write access to everything')
    k = rec.get("read_key")
    if rec.get("pushed"):
        if not k or not str(k).startswith("sgit_public_read_"):
            errors.append(f'{name}: says the vault is pushed but publishes no public read key')
        if not rec.get("vault_id"):
            errors.append(f'{name}: says the vault is pushed and names no vault id')
    elif k:
        errors.append(f'{name}: publishes a read key for a vault it says is not pushed')
if outreach_vault.get("actions_recorded", 0) != len(list((SEC / "outreach" / "actions").glob("*.json"))) - 1:
    # _schema.json is not an action; every other file in actions/ is
    errors.append("outreach-vault: the action count disagrees with the files in outreach/actions/")
for f in (SEC / "outreach").rglob("*"):
    if f.is_file():
        body = f.read_text(encoding="utf-8", errors="replace")
        for m in CONTACT["email"].finditer(body):
            local, _, dom = m.group(0).partition("@")
            # the same two-part rule the contacts map publishes: a role local part, OR the
            # site's own name (anj@anj.org.br is the association, not a person)
            if local in ROLE or local == _second_level(dom):
                continue
            errors.append(f'outreach/{f.relative_to(SEC / "outreach")}: carries what looks like '
                          f'a personal address ("{m.group(0)}") — the protocol in that vault '
                          f'forbids it and this gate enforces it before the vault is pushed')
            break

# --- 12g. every claim anchor is in the bytes, short, and correctly typed ------------------
# The fractal layer is where this section would most easily start republishing prose, so the
# anchors are checked twice over: each must be IN the frozen sentence it points at, and each
# must be well under the twelve-word run the section refuses. And because the type is a
# published formula, every one of the 1,070 classifications is re-derived here.
claims = load("claims.json")
claim_rules = load("claim-rules.json")
terms_doc = load("terms.json")
LIMIT = claim_rules["anchor_limit_words"]
if LIMIT >= RUN:
    errors.append(f"claim-rules: the anchor limit ({LIMIT} words) is not below the "
                  f"{RUN}-word run this section refuses — the two rules must not touch")
prose_cache = {}
for a in corpus["articles"]:
    prose_cache[a["slug"]] = prose(api_rec(a["slug"]))
SENT = re.compile(r'(?<=[.!?])\s+(?=[A-Z"\u201c\u2018])')
by_article_claims = {}
for c in claims["claims"]:
    by_article_claims.setdefault(c["article"], []).append(c)
    if len(c["anchor"].split()) > LIMIT:
        errors.append(f'claims: {c["id"]} has a {len(c["anchor"].split())}-word anchor, over '
                      f'the published limit of {LIMIT}')
    text = prose_cache.get(c["article"])
    if text is None:
        errors.append(f'claims: {c["id"]} names an article not in the corpus')
        continue
    if c["anchor"] not in text:
        errors.append(f'claims: the anchor for {c["id"]} is not in the frozen prose verbatim')
    if c["offset"] is not None and not text[c["offset"]:].startswith(c["anchor"]):
        errors.append(f'claims: {c["id"]} does not start at the offset it records')
# re-derive every classification from the bytes, with the published rules, in published order
RULES = claim_rules["rules"]
for slug, text in prose_cache.items():
    pos, n = 0, 0
    for s in SENT.split(text):
        s = s.strip()
        if not s:
            continue
        pos = text.find(s, pos) + len(s)
        if len(s.split()) < 4:
            continue
        n += 1
        want = next((r["id"] for r in RULES if re.search(r["pattern"], s, re.I)), "assertion")
        got = next((c for c in by_article_claims.get(slug, []) if c["n"] == n), None)
        if got is None:
            errors.append(f'claims: {slug} sentence {n} has no claim node')
        elif got["type"] != want:
            errors.append(f'claims: {slug} claim {n} is typed "{got["type"]}"; re-running the '
                          f'published rules on the frozen bytes gives "{want}"')
    if len(by_article_claims.get(slug, [])) != n:
        errors.append(f'claims: {slug} has {len(by_article_claims.get(slug, []))} claims and '
                      f'the frozen prose gives {n} sentences')
if claims["counts"]["claims"] != len(claims["claims"]):
    errors.append("claims: the count is stale")
for kind, n in claims["counts"]["by_type"].items():
    if n != sum(1 for c in claims["claims"] if c["type"] == kind):
        errors.append(f'claims: the count for "{kind}" is stale')
# a "definition" must be the subject of its own sentence, and a divergence between two pieces
# by the same author is a repetition — saying otherwise would manufacture a finding
for d in terms_doc["defined_by_more_than_one_piece"]:
    authors = [set(a["byline"]) for a in corpus["articles"] if a["slug"] in d["articles"]]
    same = all(x & authors[0] for x in authors[1:])
    if d["same_author"] != same:
        errors.append(f'terms: "{d["term"]}" is marked same_author={d["same_author"]} and the '
                      f'bylines say {same}')
for t_ in terms_doc["terms"]:
    for slug in t_["defined_in"]:
        if slug not in prose_cache:
            errors.append(f'terms: "{t_["term"]}" is defined in an article not in the corpus')

# --- 13. every page states what this section is and is not -------------------------------
REQUIRED = [
    ("beta notice", re.compile(r"\bbeta\b", re.I)),
    ("frozen-and-hashed statement", re.compile(r"frozen|hashed|SHA-256", re.I)),
    ("link-not-republish statement",
     re.compile(r"republish(?:es)? none of them|we (?:do not|don.t) republish|"
                r"not republished here|the prose is linked, never reproduced", re.I)),
]
for p in pages:
    t = p.read_text(encoding="utf-8")
    for label, pat in REQUIRED:
        if not pat.search(t):
            errors.append(f'{p.relative_to(ROOT)}: missing the {label}')
    if "worldnewsday.org" not in t and p.name != "index.html":
        errors.append(f'{p.relative_to(ROOT)}: never names the publisher it is built from')

# --- report -------------------------------------------------------------------------------
if errors:
    print(f"world-news-day gate: {len(errors)} error(s)")
    for e in errors:
        print("  ✗", e)
    sys.exit(1)

print(f"world-news-day gate: OK — {len(pages)} pages, {corpus['count']} articles "
      f"({corpus['total_words']:,} words held, none republished), "
      f"{register['count']} frozen files re-hashed, {len(register.get('excluded', []))} excluded, "
      f"{len(theme_edges)} theme edges re-derived in both directions, "
      f"{graph['counts']['nodes']} nodes / {graph['counts']['edges']} edges conform, "
      f"licence counts re-derived from the bytes by a second implementation")
