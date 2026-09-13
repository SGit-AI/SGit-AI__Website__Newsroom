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
