#!/usr/bin/env python3
"""portugal/ — the section gate.

    python3 portugal/build/gates.py

Runs before the whole-site gate (`node admin/build/validate.js`), which this section must
also pass. QA's standing rule, inherited: a failing gate is answered, never silenced.

The checks here are shaped by what makes THIS section different from /governance/. That one
publishes claims about regulations from secondary sources; this one publishes claims about
**named people and named companies** from primary sources it hashed itself. So the gate has
two jobs the sibling's does not: prove the anchoring is real, and prove the publication is
not saying something about a person that no source supports.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build import md_to_html  # noqa: E402 — the same renderer the pages were built with

ROOT = Path(__file__).resolve().parents[2]
SEC = ROOT / "portugal"
DATA = SEC / "data"

errors = []


def load(n):
    return json.loads((DATA / n).read_text(encoding="utf-8"))


event = load("event.json")
people = load("people.json")
orgs = load("orgs.json")
sources = load("sources.json")
changes = load("changes.json")
checks = load("checks.json")
team = load("team.json")
stories = load("stories.json")
notice = load("notice.json")
sessions = load("sessions.json")
coverage = load("coverage.json")
ontology = load("ontology.json")
graph = load("graph.json")

# Our own generated pages only. The frozen copies under sources/ are somebody else's
# bytes held as evidence — they carry no beta notice and never will, and checking them
# against our house rules would be checking the wrong thing. They are also stored with a
# .snapshot extension so they are neither served nor indexed as pages of this site.
pages = sorted(p for p in SEC.rglob("*.html") if "sources/frozen/" not in p.as_posix())
src_by_id = {s["id"]: s for s in sources["sources"]}


def org_id(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") or "unnamed"


# --- 1. every frozen file exists and still hashes to what the register says ----
# The whole section rests on this one check. If a frozen copy has been edited, moved or
# lost, every claim built on it is unsupported and the build must not ship.
for s in sources["sources"]:
    f = SEC / s["frozen"]
    if not f.exists():
        errors.append(f'sources: {s["id"]} names a frozen copy that is missing: {s["frozen"]}')
        continue
    actual = hashlib.sha256(f.read_bytes()).hexdigest()
    if actual != s["sha256"]:
        errors.append(f'sources: {s["frozen"]} no longer hashes to its registered SHA-256 '
                      f'(registered {s["sha256"][:16]}…, actual {actual[:16]}…) — the frozen '
                      f'copy was modified, which breaks every claim resting on it')
    if s["state"] != "primary":
        errors.append(f'sources: {s["id"]} is not primary — every source in this section is a '
                      f'byte copy we hold, so anything else is a bug in the extractor')

# --- 2. every person and org traces to a source that exists -------------------
for p in people["people"]:
    for field in ("id", "name", "role", "org", "page"):
        if not p.get(field):
            errors.append(f'people: {p.get("id", "?")} is missing required field "{field}"')
    if p.get("page") and not p["page"].startswith("https://startupsummit.io/speakers/"):
        errors.append(f'people: {p["id"]} has a source page outside the event speaker namespace')

known_orgs = {o["id"] for o in orgs["orgs"]}
for p in people["people"]:
    if p.get("org") and org_id(p["org"]) not in known_orgs:
        errors.append(f'orgs: speaker {p["id"]} is listed under "{p["org"]}", which has no row '
                      f'on the organisations page — the derived list is out of step')

derived = set()
for o in orgs["orgs"]:
    for pid in o["people"]:
        derived.add(pid)
        if pid not in {x["id"] for x in people["people"]}:
            errors.append(f'orgs: "{o["id"]}" claims speaker "{pid}", who is not in people.json')
if derived != {p["id"] for p in people["people"] if p.get("org")}:
    errors.append("orgs: the derived organisation index does not cover exactly the speakers "
                  "who carry an organisation — it was edited by hand rather than derived")

# --- 3. counts on the pages match the data ------------------------------------
if people["count"] != len(people["people"]):
    errors.append(f'people: count says {people["count"]}, list has {len(people["people"])}')
if orgs["count"] != len(orgs["orgs"]):
    errors.append(f'orgs: count says {orgs["count"]}, list has {len(orgs["orgs"])}')
if sources["count"] != len(sources["sources"]):
    errors.append("sources: count disagrees with the register")

# --- 4. no removal is given a reason ------------------------------------------
# The editor role refuses this absolutely. A name leaving a published list has innocent
# explanations that are indistinguishable from outside, and attaching a motive to a named
# individual on this evidence is the most harmful thing this section could do.
MOTIVE = re.compile(
    r"\b(withdrew|withdrawn|pulled out|dropped out|backed out|cancelled on|was removed for|"
    r"quit|resigned|fell out|snubbed|no.showed|no-showed)\b", re.I)
for c in changes["changes"]:
    if c.get("reason_known"):
        errors.append(f'changes: {c["from"]}->{c["to"]} claims a known reason; no source states one')
    for r in c["removed"]:
        if r.get("why") or r.get("reason"):
            errors.append(f'changes: a reason is recorded for the removal of {r["name"]} — '
                          f'the source does not state one and this section does not guess')
for p in pages:
    t = p.read_text(encoding="utf-8")
    m = MOTIVE.search(t)
    if m:
        errors.append(f'{p.relative_to(ROOT)}: uses "{m.group(0)}" — this section publishes the '
                      f'diff and leaves the reason blank; that word implies one')

# --- 5. targets are never reported as results ---------------------------------
# "targeting 2,000+ founders" is a plan. Reporting it as attendance is the single most
# common way an event preview goes wrong, and it is a whole-section refusal.
for p in pages:
    t = " ".join(p.read_text(encoding="utf-8").split())
    for bad in [r"2,000\+? (?:founders|attendees|people) (?:attended|will attend|are attending)",
                r"(?:attracted|drew|brought together) 2,000",
                r"150\+? confirmed speakers"]:
        m = re.search(bad, t, re.I)
        if m and "targeting" not in t[max(0, m.start() - 60):m.start()]:
            errors.append(f'{p.relative_to(ROOT)}: "{m.group(0)}" reports a target as a result')

# --- 6. every organisation anchor a speaker row points at actually exists ------
orgs_page = SEC / "summit" / "orgs.html"
if orgs_page.exists():
    have = set(re.findall(r'<tr id="([^"]+)"', orgs_page.read_text(encoding="utf-8")))
    ppl_page = SEC / "summit" / "people.html"
    if ppl_page.exists():
        for anchor in set(re.findall(r'orgs\.html#([^"]+)"', ppl_page.read_text(encoding="utf-8"))):
            if anchor not in have:
                errors.append(f'people page links to orgs.html#{anchor}, which is not an id there')

# --- 7. the posture is stated, and matches the data ---------------------------
if team.get("human_in_the_loop") is not True:
    errors.append("team: human_in_the_loop must be true — every page states that a named editor "
                  "of record reviews before publication")
if not team.get("editor_of_record", {}).get("name"):
    errors.append("team: no editor of record is named, but the pages claim one")
REQUIRED = [
    ("beta notice", re.compile(r"\bbeta\b", re.I)),
    ("editor-of-record statement", re.compile(re.escape(team["editor_of_record"]["name"]), re.I)),
    ("frozen-and-hashed statement", re.compile(r"frozen|hashed|SHA-256", re.I)),
]
for p in pages:
    t = p.read_text(encoding="utf-8")
    for label, pat in REQUIRED:
        if not pat.search(t):
            errors.append(f'{p.relative_to(ROOT)}: missing the {label}')

# --- 8. no page claims a capability this section does not have ----------------
# Portuguese is structural and not published; saying otherwise would be the exact failure
# the original brief's two source briefs disagreed about.
PT_OVERCLAIM = re.compile(r"\b(bilingual publication|published in Portuguese|"
                          r"available in Portuguese|Portuguese edition)\b", re.I)
for p in pages:
    t = p.read_text(encoding="utf-8")
    m = PT_OVERCLAIM.search(t)
    if m and "not" not in t[max(0, m.start() - 40):m.start()].lower():
        errors.append(f'{p.relative_to(ROOT)}: claims "{m.group(0)}" — nothing here is published '
                      f'in Portuguese; the labels are structural only')

# --- 9. stories trace to sources, and their pages match their markdown --------
for st in stories["stories"]:
    for sid in st["stands_on"]:
        if sid not in src_by_id:
            errors.append(f'stories: "{st["slug"]}" stands on "{sid}", which is not in the register')
    md = SEC / "content" / f'{st["slug"]}.md'
    page_f = SEC / "stories" / f'{st["slug"]}.html'
    if not md.exists():
        errors.append(f'stories: "{st["slug"]}" has no prose at content/{st["slug"]}.md')
        continue
    if page_f.exists():
        rendered = md_to_html(md.read_text(encoding="utf-8"))
        text = page_f.read_text(encoding="utf-8")
        for block in rendered.split("\n"):
            if block.strip() and block not in text:
                errors.append(f'stories: {page_f.relative_to(ROOT)} has drifted from its markdown '
                              f'— re-run build.py (first missing: {block[:60]}…)')
                break

# --- 10. biographies are not republished --------------------------------------
# The section links rather than reproduces. A bio string leaking into the data would be a
# silent change of posture, so it is a build failure rather than a style note.
for p in people["people"]:
    for k, v in p.items():
        if isinstance(v, str) and len(v) > 160:
            errors.append(f'people: {p["id"]} field "{k}" is {len(v)} chars — biographies are '
                          f'linked, never reproduced, and nothing on a node should be this long')

# --- 11. no contact detail for any natural person, anywhere in the data ---------
# Article 24(4) of Lei 58/2019 bars disclosing addresses and contact details of individuals
# unless already generally known. The dev brief of 13 September is explicit that this has to
# be enforced where the data is PARSED, not where it is rendered: a contact detail that
# reaches the data and is merely hidden by a template is one careless loop away from being
# published. So the check runs against the JSON, not against the pages.
#
# event.json is exempt for one field only — the venue's street address, which is a building
# operated by an organisation and is on every ticket. It is not a natural person's address.
CONTACT = {
    "email": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    "phone": re.compile(r"\+\d[\d ()\u2011-]{7,}\d"),
    "postal": re.compile(r"\b(?:Rua|Avenida|Av\.|Travessa|Largo|Praceta)\s+[A-Z]"),
}
PERSONAL_FILES = ["people.json", "orgs.json", "changes.json", "checks.json", "stories.json"]
for name in PERSONAL_FILES:
    text = (DATA / name).read_text(encoding="utf-8")
    for kind, pat in CONTACT.items():
        m = pat.search(text)
        if m:
            errors.append(f'{name}: contains what looks like a personal {kind} '
                          f'("{m.group(0)[:40]}") — contact details are refused at extraction '
                          f'time, not hidden at render time. See the notice page')

# The notice's own promise must match the controller it names, or it points nowhere.
if not notice.get("controller", {}).get("contact"):
    errors.append("notice: no contact for the controller — the objection route reaches nobody")
if notice["lawful_basis"]["basis"].lower() != "legitimate interests":
    errors.append("notice: the lawful basis changed; the pages and the balancing test say "
                  "legitimate interests and the journalistic route is expressly not claimed")

# --- 12. every page that names individuals links to the notice -----------------
# A notice nobody can find from the page that named them is not a measure, it is a file.
NAMES_PEOPLE = ["summit/people.html", "summit/changes.html", "summit/orgs.html"]
for rel in NAMES_PEOPLE:
    f = SEC / rel
    if not f.exists():
        continue
    t = f.read_text(encoding="utf-8")
    if "notice.html" not in t:
        errors.append(f'{rel}: names individuals and does not link to the data-protection '
                      f'notice — Article 14(5)(b) is earned by making the information findable')
if not (SEC / "notice.html").exists():
    errors.append("section: notice.html was not generated, but pages name individuals")

# --- 13. the graph conforms to its ontology --------------------------------------
# Inherited grammar: every edge is a verb with a distinct named inverse; no banned verb;
# every node is a declared type and names a frozen source. A plausible edge is
# indistinguishable from a true one once it is in the file, so the file is checked.
verbs = {e["verb"] for e in ontology["edges"]}
inverses = {e["inverse"] for e in ontology["edges"]}
banned = {b["verb"] for b in ontology["banned"]}
types = {t["id"] for t in ontology["node_types"]}
for e in ontology["edges"]:
    if e["verb"] == e["inverse"]:
        errors.append(f'ontology: "{e["verb"]}" is its own inverse — symmetric edges are banned')
    if not e.get("pt", {}).get("verb") or not e.get("pt", {}).get("inverse"):
        errors.append(f'ontology: "{e["verb"]}" has no Portuguese — every verb carries pt from day one')
    if e["verb"] in banned:
        errors.append(f'ontology: "{e["verb"]}" is both declared and banned')
for t in ontology["node_types"]:
    if not t.get("pt"):
        errors.append(f'ontology: type "{t["id"]}" has no Portuguese label')
gnode = {n["id"]: n for n in graph["nodes"]}
domain_range = {(e["verb"], e["domain"], e["range"]) for e in ontology["edges"]}
for n in graph["nodes"]:
    if n["type"] not in types:
        errors.append(f'graph: node {n["id"]} has unknown type "{n["type"]}"')
    if not n.get("source"):
        errors.append(f'graph: node {n["id"]} names no source — a node with no way back to bytes is a drawing')
    elif n["source"] not in src_by_id:
        errors.append(f'graph: node {n["id"]} names source "{n["source"]}", which is not in the register')
for e in graph["edges"]:
    if e["verb"] in banned:
        errors.append(f'graph: banned verb "{e["verb"]}" is in use')
    elif e["verb"] not in verbs:
        hint = " (that is an inverse; edges are stored forwards)" if e["verb"] in inverses else ""
        errors.append(f'graph: edge verb "{e["verb"]}" is not in the ontology{hint}')
    if e["source"] not in gnode or e["target"] not in gnode:
        errors.append(f'graph: edge {e["id"]} has an endpoint that is not a node')
    elif (e["verb"], gnode[e["source"]]["type"], gnode[e["target"]]["type"]) not in domain_range \
            and e["verb"] in verbs:
        errors.append(f'graph: {e["verb"]} from {gnode[e["source"]]["type"]} to {gnode[e["target"]]["type"]} '
                      f'is outside the verb\'s declared domain/range')
if graph["counts"]["nodes"] != len(graph["nodes"]) or graph["counts"]["edges"] != len(graph["edges"]):
    errors.append("graph: counts disagree with the lists")
for pk in graph["packs"]:
    if pk["nodes"] != sum(1 for n in graph["nodes"] if n["pack"] == pk["id"]):
        errors.append(f'graph: pack "{pk["id"]}" count is stale')
# every person on the current list is in the graph, and every graph person is either on the
# list or explicitly marked as no longer listed — nobody appears by accident
listed = {"person:" + p["id"] for p in people["people"]}
for n in graph["nodes"]:
    if n["type"] == "Person" and n["id"] not in listed and not n.get("no_longer_listed"):
        errors.append(f'graph: {n["id"]} is not on the published list and is not marked no_longer_listed')
    if n["type"] == "Person" and n.get("no_longer_listed") and n.get("reason") is not None:
        errors.append(f'graph: {n["id"]} carries a reason for leaving the list — the source states none')

# --- 14. every session title is in the frozen agenda, verbatim ---------------------
# sessions.json is transcribed by hand from the frozen agenda. A transcription is a claim,
# so it is checked against the bytes it claims to come from.
agenda_f = SEC / "sources" / "frozen" / sessions["source"].replace("/", "/", 1).split("/")[0] / "agenda.snapshot"
if agenda_f.exists():
    import html as _html
    at = " ".join(_html.unescape(re.sub(r"<[^>]+>", " ", agenda_f.read_text(errors="replace"))).split())
    for sn in sessions["sessions"]:
        if sn["title"] not in at:
            errors.append(f'sessions: "{sn["title"]}" is not in the frozen agenda verbatim — the transcription drifted')
        if sn["stage"] and sn["stage"] not in {st["id"] for st in sessions["stages"]}:
            errors.append(f'sessions: "{sn["id"]}" is on stage "{sn["stage"]}", which is not declared')
else:
    errors.append(f"sessions: the agenda snapshot {agenda_f} is missing")

# --- 15. coverage is frozen before it is cited, and never reproduced ----------------
for c in coverage["items"]:
    if c["source"] not in src_by_id:
        errors.append(f'coverage: "{c["id"]}" cites source "{c["source"]}", which is not in the register')
    if len(c.get("what_it_says", "")) > 600:
        errors.append(f'coverage: "{c["id"]}" summary is {len(c["what_it_says"])} chars — that is a reproduction, not a summary')
    if re.search(r'["“][^"”]{60,}["”]', c.get("what_it_says", "")):
        errors.append(f'coverage: "{c["id"]}" summary contains a long quotation — link, do not reproduce')
for x in coverage.get("excluded", []):
    if any(s["url"] == x["url"] for s in sources["sources"]):
        errors.append(f'coverage: "{x["id"]}" is excluded and also in the register')

# --- report -------------------------------------------------------------------
if errors:
    print(f"portugal gate: {len(errors)} error(s)")
    for e in errors:
        print("  ✗", e)
    sys.exit(1)

ch = changes["changes"][-1] if changes["changes"] else None
print(f"portugal gate: OK — v{stories['section_version']}, {len(pages)} pages, "
      f"{people['count']} speakers / {orgs['count']} orgs, "
      f"{sources['count']} frozen files across {len(sources['snapshots'])} snapshots, "
      f"every SHA-256 re-verified, "
      + (f"last diff +{len(ch['added'])}/-{len(ch['removed'])}, " if ch else "")
      + f"editor of record {team['editor_of_record']['name']} on every page")
