#!/usr/bin/env python3
"""governance/ — the section gate.

    python3 governance/build/gates.py

Structural, cheap, and impossible to satisfy by writing more confidently. This runs *before*
the whole-site gate (`node admin/build/validate.js`), which the section must also pass.

QA's standing rule, inherited: a failing gate is answered, never silenced. When a new way of
being wrong is found, it becomes a numbered check here before the fix ships. Checks 9 to 13
were written when the newsroom floor, the state map and the run records landed: a room that
draws a workflow, and a run record that names sources it could not reach, are both new ways
to publish something untrue.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build import md_to_html  # noqa: E402  — the same renderer the pages were built with

ROOT = Path(__file__).resolve().parents[2]
SEC = ROOT / "governance"
DATA = SEC / "data"

errors = []


def load(n):
    return json.loads((DATA / n).read_text(encoding="utf-8"))


graph = load("graph.json")
onto = load("ontology.json")
stories = load("stories.json")
sources = load("sources.json")
team = load("team.json")
desk = load("desk.json")
workflow = load("workflow.json")
research = load("research.json")

nodes = {n["id"]: n for n in graph["nodes"]}
src_ids = {s["id"] for s in sources["sources"]}
verbs = {e["verb"] for e in onto["edges"]}
inverses = {e["inverse"] for e in onto["edges"]}
banned = {b["verb"] for b in onto["banned"]}
types = {t["id"] for t in onto["node_types"]}

pages = sorted(SEC.rglob("*.html"))

# --- 1. every node's source resolves, or its origin is declared ---------------
for n in graph["nodes"]:
    if n["type"] not in types:
        errors.append(f'graph: node {n["id"]} has unknown type "{n["type"]}"')
    s = n.get("source")
    if s is None:
        if n.get("asked_by") != "publication":
            errors.append(
                f'graph: node {n["id"]} has no source and does not declare itself as '
                f'originating with the publication (asked_by: "publication")')
    elif s not in src_ids:
        errors.append(f'graph: node {n["id"]} cites source "{s}" which is not in the register')

# --- 2. edge vocabulary ------------------------------------------------------
for e in graph["edges"]:
    if e["verb"] in banned:
        errors.append(f'graph: banned verb "{e["verb"]}" is in use — see ontology.banned')
    elif e["verb"] not in verbs:
        hint = " (that is an inverse; edges are stored in the forward direction)" if e["verb"] in inverses else ""
        errors.append(f'graph: edge verb "{e["verb"]}" is not in the ontology{hint}')
    for end in ("source", "target"):
        if e[end] not in nodes:
            errors.append(f'graph: edge {e["verb"]} has {end} "{e[end]}" which is not a node')

# every declared edge must have a distinct inverse — the inherited grammar rule
for e in onto["edges"]:
    if e["verb"] == e["inverse"]:
        errors.append(f'ontology: "{e["verb"]}" is its own inverse — symmetric edges are banned')

# --- 3. every story's cited nodes exist --------------------------------------
for st in stories["stories"]:
    for nid in st["nodes"] + st.get("questions", []):
        if nid not in nodes:
            errors.append(f'stories: "{st["slug"]}" cites node "{nid}" which is not in the graph')
    md = SEC / "content" / f'{st["slug"]}.md'
    if not md.exists():
        errors.append(f'stories: "{st["slug"]}" has no prose at content/{st["slug"]}.md')

# --- 4. no page may claim an anchor the data does not carry ------------------
anchored = [n["id"] for n in graph["nodes"] if n.get("anchored")]
POSITIVE_ANCHOR = re.compile(r"anchor holds|anchored to a byte range|anchor verified", re.I)
if not anchored:
    for p in pages:
        if POSITIVE_ANCHOR.search(p.read_text(encoding="utf-8")):
            errors.append(f'{p.relative_to(ROOT)}: claims a verified anchor, but no node in the '
                          f'graph has anchored:true')

# --- 5. every story page matches its markdown --------------------------------
for st in stories["stories"]:
    md = SEC / "content" / f'{st["slug"]}.md'
    page = SEC / "stories" / f'{st["slug"]}.html'
    if not (md.exists() and page.exists()):
        continue
    rendered = md_to_html(md.read_text(encoding="utf-8"))
    text = page.read_text(encoding="utf-8")
    for block in rendered.split("\n"):
        if block.strip() and block not in text:
            errors.append(f'stories: {page.relative_to(ROOT)} has drifted from its markdown — '
                          f're-run build.py (first missing block: {block[:70]}…)')
            break

# --- 6. the limitation is on every page --------------------------------------
REQUIRED = [
    ("beta notice", re.compile(r"\bbeta\b", re.I)),
    ("no-human-review statement", re.compile(r"no human review|No human reviews|No human reviewed", re.I)),
    ("secondary-source statement", re.compile(r"secondary", re.I)),
]
for p in pages:
    t = p.read_text(encoding="utf-8")
    for label, pat in REQUIRED:
        if not pat.search(t):
            errors.append(f'{p.relative_to(ROOT)}: missing the {label}')

# --- 7. the register's own claims --------------------------------------------
for s in sources["sources"]:
    if s.get("http") != 200:
        errors.append(f'sources: "{s["id"]}" records HTTP {s.get("http")} — a source that did '
                      f'not resolve when checked cannot stay in the ingested list')
    if s["state"] not in {d["id"] for d in sources["ingestion_states"]}:
        errors.append(f'sources: "{s["id"]}" has unknown state "{s["state"]}"')
    for nid in s.get("supplies", []):
        if nid not in nodes:
            errors.append(f'sources: "{s["id"]}" claims to supply "{nid}", which is not a node')

# --- 8. the team is fully agentic and says so --------------------------------
if team.get("human_in_the_loop") is not False:
    errors.append("team: human_in_the_loop must be false while the pages state that no human "
                  "reviews a page before publication")
for r in team["roles"]:
    rm = SEC / "team" / r["id"] / "role.md"
    if not rm.exists():
        errors.append(f'team: role "{r["id"]}" has no role.md')
    else:
        body = rm.read_text(encoding="utf-8")
        for heading in ("What it owns", "What it refuses", "How to tell when it is wrong"):
            if heading not in body:
                errors.append(f'team/{r["id"]}/role.md: missing the "{heading}" section')

# --- 9. the state machine is closed ------------------------------------------
# A workflow whose exits point at states that do not exist is a diagram, not a machine.
role_ids = {r["id"] for r in team["roles"]}
state_ids = {st["id"] for st in workflow["states"]}
for st in workflow["states"]:
    if st["owner"] not in role_ids:
        errors.append(f'workflow: state "{st["id"]}" is owned by "{st["owner"]}", which is not a role')
    for ex in st["exits"]:
        if ex not in state_ids:
            errors.append(f'workflow: state "{st["id"]}" exits to "{ex}", which is not a state')
    if not st["exits"] and not st.get("terminal"):
        errors.append(f'workflow: state "{st["id"]}" has no exits and is not marked terminal')
    if st.get("blocked") and not st.get("blocked_why"):
        errors.append(f'workflow: state "{st["id"]}" is blocked but does not say why')
lane_states = [sid for lane in workflow["lanes"] for sid in lane["states"]]
for sid in state_ids:
    if sid not in lane_states:
        errors.append(f'workflow: state "{sid}" is in no lane, so it renders nowhere')
for sid in lane_states:
    if sid not in state_ids:
        errors.append(f'workflow: a lane names "{sid}", which is not a state')

# --- 10. the desk matches the machine ----------------------------------------
item_ids = {it["id"] for it in desk["items"]}
for it in desk["items"]:
    if it["state"] not in state_ids:
        errors.append(f'desk: item "{it["id"]}" is in state "{it["state"]}", which is not in the workflow')
    if it["owner"] not in role_ids:
        errors.append(f'desk: item "{it["id"]}" is owned by "{it["owner"]}", which is not a role')
    if it.get("blocked_at") and it["blocked_at"] not in state_ids:
        errors.append(f'desk: item "{it["id"]}" is blocked at "{it["blocked_at"]}", which is not a state')
    if it["state"] not in ("published",) and not it.get("blocked_why"):
        errors.append(f'desk: item "{it["id"]}" is unpublished and does not say why it is not moving')
if desk["pick"]["item"] not in item_ids:
    errors.append(f'desk: the pick names "{desk["pick"]["item"]}", which is not on the desk')
if desk["pick"]["by"] in role_ids:
    errors.append('desk: the pick is attributed to a pipeline role — proposing and choosing are '
                  'deliberately separate, and no role in team.json may hold the decision')
if sum(1 for it in desk["items"] if it.get("picked")) != 1:
    errors.append("desk: exactly one item may carry picked:true")

# --- 11. a run may not launder an unreachable source -------------------------
# The whole point of recording a 403 is that it does NOT become a citation. This check
# makes that structural rather than a matter of the Researcher remembering.
reg_urls = {s["url"] for s in sources["sources"]}
for run in research["runs"]:
    if run["role"] not in role_ids:
        errors.append(f'research: run "{run["id"]}" is attributed to "{run["role"]}", not a role')
    cand_ids = {c["id"] for c in run["candidates"]}
    if run["recommendation"]["candidate"] not in cand_ids:
        errors.append(f'research: run "{run["id"]}" recommends a candidate it did not propose')
    for c in run["candidates"]:
        if not c.get("weakness"):
            errors.append(f'research: candidate "{c["id"]}" is proposed without a weakness')
    for f in run["fetched"]:
        if f["http"] != 200 and f["url"] in reg_urls:
            errors.append(f'research: "{f["url"]}" returned HTTP {f["http"]} and is in the '
                          f'source register — an unreachable source cannot be cited')
        if f["http"] != 200 and "not confirmed dead" not in f["note"].lower() \
                and "blocked" not in f["note"].lower():
            errors.append(f'research: "{f["url"]}" failed to resolve and the note does not '
                          f'distinguish our reach from the state of the page')

# --- 12. every role has a folder page ----------------------------------------
for r in team["roles"]:
    if not (SEC / "team" / r["id"] / "index.html").exists():
        errors.append(f'team: role "{r["id"]}" has no page at team/{r["id"]}/index.html')
for extra in ("newsroom/index.html", "newsroom/workflow.html", "research/index.html"):
    if not (SEC / extra).exists():
        errors.append(f"section: {extra} was not generated")
for run in research["runs"]:
    if not (SEC / "research" / f'{run["date"]}.html').exists():
        errors.append(f'research: run "{run["id"]}" has no page at research/{run["date"]}.html')

# --- 13. the room and the pipeline are the same seven steps ------------------
# The floor draws a route through the desks in a fixed order. If team.json's pipeline is
# reordered and the layout is not, the scene shows a workflow the publication does not run.
from floor import DESKS  # noqa: E402

room = [d[0] for d in DESKS]
pipe = [p["role"] for p in sorted(team["pipeline"], key=lambda x: x["step"])]
if room != pipe:
    errors.append(f"floor: the desk layout runs {room} but the pipeline runs {pipe} — the room "
                  f"would draw a route through a workflow that does not exist")

# --- report ------------------------------------------------------------------
if errors:
    print(f"governance gate: {len(errors)} error(s)")
    for e in errors:
        print("  ✗", e)
    sys.exit(1)

facts = [n for n in graph["nodes"] if n["type"] == "Fact"]
print(f"governance gate: OK — v{stories['section_version']}, {len(pages)} pages, "
      f"{len(graph['nodes'])} nodes / {len(graph['edges'])} edges, "
      f"{len(anchored)}/{len(facts)} facts anchored, "
      f"{len(sources['sources'])} sources all resolving, "
      f"{len(team['roles'])} roles with refusals, "
      f"{len(desk['items'])} items on the desk in {len(workflow['states'])} states, "
      f"{len(research['runs'])} research run(s), "
      f"every page carries the beta and no-human-review notice")
