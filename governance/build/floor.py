#!/usr/bin/env python3
"""The newsroom floor, the workflow map, the role pages and the research brief.

Imported by build.py. Kept separate because the floor is a different kind of artefact
from the rest of the section: it is an interactive scene rather than a projection of
prose, and mixing it into build.py made both harder to read.

On the scene's shape: it is a point-and-click adventure interface — a room you click
around, a verb bar, a dialogue box. That is a genre convention, and everything in it is
original to this site: our own palette, our own figures drawn as inline SVG, our own
verbs, our own writing. No third-party game's art, wording or interface is reproduced.
"""
import html
import json

# Desk layout on the floor. The room is laid out boustrophedon — left to right along the
# back row, right to left along the middle, left to right along the front — so that walking
# the pipeline in order is a single unbroken route with no doubling back. FLOW is that route,
# drawn in the corridors between the rows, and it is the same seven steps as team.json's
# pipeline. If the pipeline changes and this does not, they disagree, so gate check 13
# compares them.
DESKS = [
    ("librarian",  180, 118, "#0f766e"),
    ("researcher", 470, 118, "#115e59"),
    ("extractor",  760, 118, "#1d4ed8"),
    ("writer",     760, 300, "#b45309"),
    ("editor",     430, 300, "#a16207"),
    ("qa",         430, 470, "#b91c1c"),
    ("publisher",  740, 470, "#5c5f66"),
]

# The corridor route, in the order the pipeline runs. Kept as one path so a token can be sent
# along it: the room shows work moving rather than seven desks sitting still.
FLOW = "M180,190 H880 V372 H140 V554 H740"

# One distinguishing prop per role, drawn rather than lettered, so the figures read at a
# glance without depending on emoji (which render inconsistently and are banned in the
# house style anyway).
PROPS = {
    "librarian":  '<rect x="-9" y="-6" width="7" height="14" rx="1"/><rect x="0" y="-6" width="7" height="14" rx="1"/>',
    "researcher": '<circle cx="-2" cy="-1" r="6" fill="none" stroke-width="2.4"/><path d="M3 4l6 6" stroke-width="2.4" stroke-linecap="round"/>',
    "extractor":  '<circle cx="-7" cy="4" r="3"/><circle cx="6" cy="5" r="3"/><circle cx="0" cy="-6" r="3"/><path d="M-7 4L0-6L6 5" fill="none" stroke-width="1.8"/>',
    "writer":     '<path d="M-8 8L6-6l3 3L-5 11z"/><path d="M-8 8l-1 4 4-1z"/>',
    "editor":     '<rect x="-9" y="-7" width="18" height="14" rx="2" fill="none" stroke-width="2.2"/><path d="M-4 0l3 3 6-6" fill="none" stroke-width="2.4" stroke-linecap="round"/>',
    "qa":         '<path d="M0-9l9 4v6c0 5-4 8-9 9-5-1-9-4-9-9v-6z" fill="none" stroke-width="2.2"/><path d="M-4 0l3 3 6-6" fill="none" stroke-width="2.2" stroke-linecap="round"/>',
    "publisher":  '<path d="M-9-7h18v14h-18z" fill="none" stroke-width="2.2"/><path d="M-5-2h10M-5 2h6" stroke-width="2" stroke-linecap="round"/>',
}


def figure(role, x, y, colour, count, label, step):
    """One desk: a surface, a seated figure, a numbered nameplate and a load badge.

    The number is the role's step in the pipeline, so the order of the room is legible
    without following the route with your eye."""
    prop = PROPS.get(role, "")
    badge = ""
    if count:
        badge = (f'<g transform="translate(52,-46)">'
                 f'<circle r="13" fill="{colour}"/>'
                 f'<text y="5" text-anchor="middle" font-size="15" font-weight="700" fill="#fff">{count}</text>'
                 f"</g>")
    return f"""<g class="desk" data-role="{role}" transform="translate({x},{y})" tabindex="0" role="button"
   aria-label="Step {step}, {html.escape(label)} — {count} item{'s' if count != 1 else ''} on the desk">
  <rect class="hit" x="-86" y="-72" width="172" height="140" fill="transparent" pointer-events="all"/>
  <ellipse cx="0" cy="52" rx="74" ry="15" fill="rgba(28,29,33,.06)"/>
  <g transform="translate(0,-34)" fill="{colour}" stroke="{colour}">
    <circle cx="0" cy="-16" r="13" stroke="none"/>
    <path d="M-19 8c0-11 8-18 19-18s19 7 19 18z" stroke="none"/>
    <g transform="translate(0,-2)" stroke="#fff" fill="#fff" opacity=".95">{prop}</g>
  </g>
  <rect class="plate" x="-78" y="22" width="156" height="30" rx="6" fill="#fff" stroke="#d5d0c2"/>
  <circle cx="-59" cy="37" r="10.5" fill="{colour}"/>
  <text x="-59" y="42" text-anchor="middle" font-size="14" font-weight="700" fill="#fff">{step}</text>
  <text x="12" y="43" text-anchor="middle" font-size="17" font-weight="600" fill="#101114">{html.escape(label)}</text>
  {badge}
</g>"""


def build_floor(page, write, masthead, disclaimer, agent_block, TEAM, DESK, WORKFLOW, RESEARCH):
    up = "../"
    roles = {r["id"]: r for r in TEAM["roles"]}
    states = {s["id"]: s for s in WORKFLOW["states"]}

    # what each role is holding right now
    load = {r["id"]: [] for r in TEAM["roles"]}
    for it in DESK["items"]:
        load.setdefault(it["owner"], []).append(it)

    steps = {p["role"]: p["step"] for p in TEAM["pipeline"]}
    desks = "\n".join(
        figure(rid, x, y, c, len(load.get(rid, [])), roles[rid]["name"], steps[rid])
        for rid, x, y, c in DESKS)

    # the dialogue the scene can speak, built from the same data the rest of the section uses
    lines = {}
    for rid, r in roles.items():
        items = load.get(rid, [])
        held = ("; ".join(f'“{i["title"]}” ({states[i["state"]]["label"].lower()})' for i in items)
                if items else "nothing at the moment")
        blocked = [i for i in items if i.get("blocked_why")]
        lines[rid] = {
            "look": f'{r["name"]}. {r["gravity"]}',
            "talk": (f'“I am holding {held}.” '
                     + (f'“{blocked[0]["blocked_why"]}”' if blocked else
                        "“Nothing is stuck with me right now.”")),
            "hand": (f'“Owns: {r["owns"]}” — work reaches this desk when the state before it '
                     f'has cleared its door.'),
            "gate": f'“I refuse: {r["refuses"]}” Wrong when: {r["wrong_when"]}',
        }

    pick = DESK["pick"]
    run = RESEARCH["runs"][0]

    rows = "".join(
        f'<tr><td><b>{html.escape(i["title"])}</b>'
        + (' <span class="pill p-ships">picked</span>' if i.get("picked") else "")
        + f'</td><td class="small">{html.escape(states[i["state"]]["label"])}</td>'
        f'<td class="small">{html.escape(roles[i["owner"]]["name"])}</td>'
        f'<td class="small">{html.escape(i.get("blocked_why", "—"))}</td></tr>'
        for i in DESK["items"])

    # Counts are derived, never typed. A sentence like "five of six are stuck" is exactly the
    # kind of claim that is true on the day it is written and quietly wrong a week later.
    total = len(DESK["items"])
    stopped = [i for i in DESK["items"] if i.get("blocked_why")]
    at_frozen = [i for i in DESK["items"] if i.get("blocked_at") == "frozen"]
    shipped = [i for i in DESK["items"] if i["state"] == "published"]

    body = f"""{masthead(up, "newsroom/index.html")}
<h1>The newsroom floor</h1>
<p class="lead">Seven desks, none of them a person. <b>Click a verb, then click somebody</b> &mdash;
the room answers from the same data the rest of the section is built on, so what a desk says
about its workload is what <a href="{up}data/desk.json">desk.json</a> actually holds.</p>

{disclaimer.replace("{up}", up)}

<div class="scene" id="scene">
  <div class="sceneframe">
  <svg viewBox="0 0 1100 600" role="img" aria-label="The newsroom floor: seven agent desks, joined by the route work takes through them">
    <defs>
      <marker id="way" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6"
              orient="auto-start-reverse">
        <path d="M0 0L10 5L0 10z" fill="#c9c3b2"/>
      </marker>
      <pattern id="floorTile" width="56" height="56" patternUnits="userSpaceOnUse">
        <rect width="56" height="56" fill="#f6f4ee"/>
        <path d="M56 0v56M0 56h56" stroke="#eae6dc" stroke-width="1"/>
      </pattern>
    </defs>
    <rect width="1100" height="600" fill="url(#floorTile)"/>
    <rect x="0" y="0" width="1100" height="46" fill="#f2f0e9"/>
    <text x="24" y="30" font-size="15" font-weight="700" fill="#8a8d94"
          letter-spacing="2.4">THE GOVERNANCE WIRE &#183; FLOOR</text>
    <path id="flow" d="{FLOW}" fill="none" stroke="#c9c3b2" stroke-width="3"
          stroke-dasharray="9 9" stroke-linecap="round" stroke-linejoin="round"
          marker-end="url(#way)"/>
    <circle class="token" r="7" fill="#b45309" stroke="#fff" stroke-width="2" cx="180" cy="190"/>
    <g transform="translate(975,300)" opacity=".55">
      <rect x="-56" y="-70" width="112" height="150" rx="6" fill="#fff" stroke="#d5d0c2"/>
      <text y="-46" text-anchor="middle" font-size="12" fill="#8a8d94" letter-spacing="1.6">ARCHIVE</text>
      <path d="M-40-30h80M-40-8h80M-40 14h80M-40 36h80" stroke="#e5e1d5" stroke-width="7"/>
    </g>
    {desks}
  </svg>
  </div>
  <p class="hint"><b>The dotted route is the pipeline</b>, in order: the token travels
  librarian &rarr; researcher &rarr; extractor &rarr; writer &rarr; editor &rarr; QA &rarr;
  publisher, which is the same seven steps as <a href="{up}method.html#pipeline">the method</a>.
  On a narrow screen the room is wider than the window &mdash; drag it sideways.
  Every desk is also reachable with <kbd>Tab</kbd> and opened with <kbd>Enter</kbd>.</p>

  <div class="verbs" id="verbs" role="toolbar" aria-label="Actions">
    <button class="vb on" data-verb="look" type="button">Look at</button>
    <button class="vb" data-verb="talk" type="button">Talk to</button>
    <button class="vb" data-verb="hand" type="button">Hand over</button>
    <button class="vb" data-verb="gate" type="button">Ask what they refuse</button>
  </div>
  <div class="say" id="say" aria-live="polite">Pick a verb, then a desk. Start with <b>Talk to</b>
  &mdash; the Researcher has just come back from a run.</div>
  <noscript><p class="hint"><b>The verbs need JavaScript</b>, and it is off. The room, the route
  and the desk loads above are all still real &mdash; and everything the desks would say is on
  this page anyway: what each holds is in the table below, and what each refuses is on its
  <a href="{up}team.html">own role page</a>.</p></noscript>
</div>

<h2 id="pick">Today's decision</h2>
<div class="note">
  <p style="margin-top:0"><b>Picked: “{html.escape(next(i["title"] for i in DESK["items"] if i["id"] == pick["item"]))}”</b>
  &mdash; decided {html.escape(pick["decided"])} by the {html.escape(pick["by"])}, on the Researcher's
  recommendation. {html.escape(pick["note"])}</p>
  <p>The recommendation and the decision are recorded separately on purpose. Proposing is the
  Researcher's job; choosing is not. <a href="{up}research/{run["date"]}.html">The full run &rarr;</a></p>
</div>

<h2 id="desk">What is on the desk</h2>
<div class="tablewrap"><table>
  <thead><tr><th>Item</th><th>State</th><th>With</th><th>Why it is not moving</th></tr></thead>
  <tbody>{rows}</tbody>
</table></div>
<p><b>{len(stopped)} of {total} items are not moving</b>, and {len(shipped)} have shipped.
{len(at_frozen)} of the stopped ones is held at the <em>frozen</em> door specifically &mdash;
the picked story, which cannot be written as a verified reading of anything until a hashed copy
of its sources exists. The rest are stopped for reasons of their own, named in the last column.
<a href="{up}newsroom/workflow.html">The state map shows where each door sits &rarr;</a></p>

<h2 id="how">How this was built</h2>
<p>There is a debrief on this interface written for the agents of the sibling
<code>*.sgit.ai</code> sites, who all publish their teams as a roster and an ordered list:
<a href="{up}../documents/newsroom-floor.html"><b>The newsroom floor &mdash; a point-and-click
UI for agentic work</b></a>. It carries the rule that separates this from a mock-up, the
genre-versus-work position on the adventure-game reference, the four defects we shipped into,
the gate that compares the drawn route to the declared pipeline, and a porting recipe. It also
says what one implementation on one day has <em>not</em> proven.</p>

{agent_block(
    "This floor is a rendering of <code>/governance/data/desk.json</code> and "
    "<code>/governance/data/workflow.json</code> — fetch those rather than parsing the scene. "
    "The seven figures are agent roles, not people. Item states are real and current, and the "
    "counts on this page are derived from that file rather than written into it. The "
    "<code>frozen</code> state carries <code>blocked: true</code> because the fetch-freeze-hash "
    "path is not implemented, which is why every fact in the graph is <code>secondary</code> "
    "and nothing is anchored.")}

<div class="pagenav">
  <a href="{up}index.html">&larr; The wire</a>
  <a href="{up}newsroom/workflow.html">The state map &rarr;</a>
</div>

<style>
.scene{{position:relative;margin:1.6rem 0 2rem}}
.sceneframe{{overflow-x:auto;-webkit-overflow-scrolling:touch;border:1px solid var(--line);
  border-radius:12px;box-shadow:var(--shadow);background:#f6f4ee}}
.scene svg{{width:100%;min-width:720px;height:auto;display:block;background:#f6f4ee;
  border-radius:12px}}
.scene .hint{{margin:.55rem 0 0;font-size:.78rem;color:var(--dim);line-height:1.6}}
.scene kbd{{border:1px solid var(--line2);border-bottom-width:2px;border-radius:4px;
  padding:.05em .35em;font-size:.9em;background:var(--panel2)}}
.token{{offset-path:path("{FLOW}");offset-rotate:0deg;offset-distance:0%;
  animation:round 22s linear infinite}}
@keyframes round{{to{{offset-distance:100%}}}}
@media(prefers-reduced-motion:reduce){{.token{{animation:none}}}}
.desk{{cursor:pointer}}
.desk:hover ellipse,.desk:focus ellipse{{fill:rgba(15,118,110,.18)}}
.desk:focus{{outline:none}}
.desk:focus .plate,.desk.sel .plate{{stroke:var(--accent);stroke-width:2}}
.verbs{{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.9rem}}
.vb{{font-family:var(--sans);font-size:.85rem;font-weight:600;color:var(--fg);background:var(--panel);
  border:1px solid var(--line2);border-radius:8px;padding:.55rem .9rem;min-height:44px;cursor:pointer}}
.vb:hover{{border-color:var(--accent)}}
.vb.on{{background:var(--accent);border-color:var(--accent);color:#fff}}
.say{{margin-top:.75rem;background:var(--term-bg);color:#e6edf3;border-radius:10px;
  padding:1rem 1.15rem;font-family:var(--mono);font-size:.85rem;line-height:1.65;min-height:5.4rem}}
.say b{{color:var(--term-cyan);font-weight:600}}
.say .who{{display:block;color:var(--term-green);margin-bottom:.35rem;letter-spacing:.06em;
  text-transform:uppercase;font-size:.7rem}}
</style>
<script>
(function(){{
  var LINES = {json.dumps(lines, ensure_ascii=False)};
  var NAMES = {json.dumps({r["id"]: r["name"] for r in TEAM["roles"]}, ensure_ascii=False)};
  var verb = 'look', say = document.getElementById('say');
  document.querySelectorAll('.vb').forEach(function(b){{
    b.addEventListener('click', function(){{
      document.querySelectorAll('.vb').forEach(function(x){{ x.classList.remove('on'); }});
      b.classList.add('on'); verb = b.dataset.verb;
      say.innerHTML = 'Now click a desk.';
    }});
  }});
  function speak(el){{
    var r = el.dataset.role, l = LINES[r];
    if (!l) return;
    document.querySelectorAll('.desk').forEach(function(d){{ d.classList.remove('sel'); }});
    el.classList.add('sel');
    say.innerHTML = '<span class="who">' + NAMES[r] + '</span>' + l[verb];
  }}
  document.querySelectorAll('.desk').forEach(function(d){{
    d.addEventListener('click', function(){{ speak(d); }});
    d.addEventListener('keydown', function(e){{
      if (e.key === 'Enter' || e.key === ' ') {{ e.preventDefault(); speak(d); }}
    }});
  }});
}})();
</script>
"""
    return write("newsroom/index.html",
                 page("newsroom/index.html", "The newsroom floor",
                      "Seven agent desks you can click around. What each one says about its workload is read from the same data the section is built on.",
                      body, f'<a href="{up}../index.html">newsroom.sgit.ai</a> / '
                            f'<a href="{up}index.html">governance</a> / floor'))


def build_workflow(page, write, masthead, disclaimer, agent_block, WORKFLOW, DESK, TEAM):
    up = "../"
    roles = {r["id"]: r for r in TEAM["roles"]}
    states = {s["id"]: s for s in WORKFLOW["states"]}
    count = {}
    for it in DESK["items"]:
        count[it["state"]] = count.get(it["state"], 0) + 1

    def card(s):
        n = count.get(s["id"], 0)
        blocked = s.get("blocked")
        border = "#b91c1c" if blocked else ("#0f766e" if n else "#d5d0c2")
        bg = "#fffbfb" if blocked else "#ffffff"
        return (
            f'<div class="st" style="border-color:{border};background:{bg}">'
            f'<div class="sth"><b>{html.escape(s["label"])}</b>'
            + (f'<span class="pill p-ships">{n} here</span>' if n else "")
            + (f'<span class="pill p-absent">door shut</span>' if blocked else "")
            + "</div>"
            f'<p class="small dim">{html.escape(roles[s["owner"]]["name"])}</p>'
            f'<p>{html.escape(s["means"])}</p>'
            f'<p class="door"><b>Door:</b> {html.escape(s["door"])}</p>'
            + (f'<p class="blk"><b>Shut:</b> {html.escape(s["blocked_why"])}</p>' if blocked else "")
            + "</div>")

    lanes = ""
    for lane in WORKFLOW["lanes"]:
        cards = "".join(card(states[sid]) for sid in lane["states"])
        lanes += (f'<h3 id="lane-{lane["id"]}">{html.escape(lane["label"])}</h3>'
                  f'<div class="lane">{cards}</div>')

    shut = ' &mdash; <span class="dim small">door shut</span>'
    crows = "".join(
        f'<tr><td><b>{html.escape(s["label"])}</b>{shut if s.get("blocked") else ""}</td>'
        f'<td class="small">{html.escape(roles[s["owner"]]["name"])}</td>'
        f'<td class="num">{count.get(s["id"], 0)}</td></tr>'
        for s in sorted(WORKFLOW["states"], key=lambda x: (x["seq"] == 0, x["seq"])))

    body = f"""{masthead(up, "newsroom/workflow.html")}
<h1>How a story moves</h1>
<p class="lead">From a search result to a published page, in nine states. Each names the one
role that can advance it and <b>the door it has to get through</b> &mdash; the condition the
next role will not take it without. Machine surface:
<a href="{up}data/workflow.json">workflow.json</a>.</p>

{disclaimer.replace("{up}", up)}

<div class="note"><p style="margin-top:0"><b>One door is shut, and nothing has ever passed
it.</b> <em>Frozen</em> requires a hashed byte copy of the source, and that path is not built.
The two stories already on the wire went round it rather than through it, which is why they are
labelled secondary. That single closed door is why nothing in the graph is anchored and why the
staleness detector cannot run. It is one task, and it is the only one that matters.</p></div>

{lanes}

<h2 id="counts">Where today's six items sit</h2>
<div class="tablewrap"><table>
  <thead><tr><th>State</th><th>Owner</th><th>Items</th></tr></thead>
  <tbody>{crows}</tbody>
</table></div>

{agent_block(
    "The workflow is machine-readable at <code>/governance/data/workflow.json</code> and the "
    "current position of every item at <code>/governance/data/desk.json</code>. States are "
    "exclusive — an item is in exactly one. The <code>frozen</code> state carries "
    "<code>blocked: true</code>: no item has ever passed it, so treat every story in this "
    "publication as unanchored and secondary, because it is.")}

<div class="pagenav">
  <a href="{up}newsroom/index.html">&larr; The floor</a>
  <a href="{up}team.html">The team &rarr;</a>
</div>

<style>
.lane{{display:grid;gap:.8rem;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));margin:.6rem 0 1.6rem}}
.st{{border:1px solid var(--line);border-left-width:4px;border-radius:0 10px 10px 0;
  padding:.85rem 1rem;box-shadow:var(--shadow)}}
.st .sth{{display:flex;align-items:center;gap:.5rem;flex-wrap:wrap;margin-bottom:.15rem}}
.st .sth b{{font-size:1rem;color:#101114}}
.st p{{margin:.3rem 0;font-size:.85rem;line-height:1.55;color:#34363c}}
.st .door{{color:#5c5f66}}
.doc td.num{{font-variant-numeric:tabular-nums;text-align:right;font-weight:600}}
.st .blk{{color:#b91c1c}}
</style>
"""
    return write("newsroom/workflow.html",
                 page("newsroom/workflow.html", "How a story moves",
                      "Nine states from search result to published page, each with the door it has to get through — and the one door that is currently shut.",
                      body, f'<a href="{up}../index.html">newsroom.sgit.ai</a> / '
                            f'<a href="{up}index.html">governance</a> / workflow'))


def build_role_pages(page, write, masthead, disclaimer, agent_block, md_to_html,
                     TEAM, DESK, WORKFLOW, RESEARCH, SEC):
    """One folder, one page, per role — the shape borrowed from the sibling site's
    making-a-book team. The prose is role.md; everything around it is read from the
    same data the floor and the state map read, so a role page cannot describe a
    workload the desk does not have."""
    up = "../../"
    roles = TEAM["roles"]
    states = {s["id"]: s for s in WORKFLOW["states"]}
    steps = {p["role"]: p for p in TEAM["pipeline"]}
    written = []

    for i, r in enumerate(roles):
        rid = r["id"]
        md = (SEC / "team" / rid / "role.md").read_text(encoding="utf-8")
        # the h1 and the gravity line are rendered by the page shell above the prose,
        # so they are dropped here rather than printed twice
        keep = [ln for ln in md.splitlines()
                if not ln.startswith("# ") and not ln.startswith("**Centre of gravity:**")]
        prose = md_to_html("\n".join(keep).strip())

        holds = [it for it in DESK["items"] if it["owner"] == rid]
        owns_states = [s for s in WORKFLOW["states"] if s["owner"] == rid]
        step = steps.get(rid)

        hold_rows = "".join(
            f'<tr><td><b>{html.escape(it["title"])}</b>'
            + (' <span class="pill p-ships">picked</span>' if it.get("picked") else "")
            + f'</td><td class="small">{html.escape(states[it["state"]]["label"])}</td>'
            f'<td class="small">{html.escape(it.get("blocked_why", "&mdash;"))}</td></tr>'
            for it in holds) or (
            '<tr><td colspan="3" class="small dim">Nothing on this desk today.</td></tr>')

        shut_pill = '<span class="pill p-absent">shut</span>'
        open_pill = '<span class="pill p-ships">open</span>'
        door_rows = "".join(
            f'<tr><td><b>{html.escape(s["label"])}</b></td>'
            f'<td class="small">{html.escape(s["door"])}</td>'
            f'<td>{shut_pill if s.get("blocked") else open_pill}</td></tr>'
            for s in owns_states) or (
            '<tr><td colspan="3" class="small dim">This role holds no door in the state map.</td></tr>')

        prev_r = roles[i - 1] if i else None
        next_r = roles[i + 1] if i + 1 < len(roles) else None
        nav = []
        if prev_r:
            nav.append(f'<a href="{up}team/{prev_r["id"]}/index.html">&larr; {html.escape(prev_r["name"])}</a>')
        else:
            nav.append(f'<a href="{up}team.html">&larr; The team</a>')
        if next_r:
            nav.append(f'<a href="{up}team/{next_r["id"]}/index.html">{html.escape(next_r["name"])} &rarr;</a>')
        else:
            nav.append(f'<a href="{up}newsroom/index.html">The floor &rarr;</a>')

        body = f"""{masthead(up, "team.html")}
<span class="dim small" style="font-family:var(--mono);letter-spacing:.12em;text-transform:uppercase">Role {i + 1} of {len(roles)}</span>
<h1>{html.escape(r["name"])}</h1>
<p class="lead">{html.escape(r["gravity"])}</p>

{disclaimer.replace("{up}", up)}

<div class="tablewrap"><table>
  <thead><tr><th>Owns</th><th>Refuses</th><th>Wrong when</th></tr></thead>
  <tbody><tr>
    <td>{html.escape(r["owns"])}</td>
    <td>{html.escape(r["refuses"])}</td>
    <td>{html.escape(r["wrong_when"])}</td>
  </tr></tbody>
</table></div>

{prose}

<h2 id="desk">On this desk today</h2>
<div class="tablewrap"><table>
  <thead><tr><th>Item</th><th>State</th><th>Why it is not moving</th></tr></thead>
  <tbody>{hold_rows}</tbody>
</table></div>
<p class="small dim">Read from <a href="{up}data/desk.json">desk.json</a> at build time.
<a href="{up}newsroom/index.html">See the whole floor &rarr;</a></p>

<h2 id="doors">Doors this role holds</h2>
<p>A door is the condition the next role will not take the work without. This role is the only
one that can open these.</p>
<div class="tablewrap"><table>
  <thead><tr><th>State</th><th>Door</th><th>Now</th></tr></thead>
  <tbody>{door_rows}</tbody>
</table></div>
{"<p>In the seven-step pipeline this role is <b>step " + str(step["step"]) + "</b>: " + html.escape(step["does"]) + "</p>" if step else ""}

<h2 id="folder">The folder</h2>
<p>The role folder is <code>governance/team/{html.escape(rid)}/</code>. It holds
<a href="role.md">role.md</a> and nothing else yet. The inherited shape has three more
directories, and stating what is missing is cheaper than implying it exists:</p>
<div class="tablewrap"><table>
  <thead><tr><th>Path</th><th>Holds</th><th>State</th></tr></thead>
  <tbody>
    <tr><td><code>role.md</code></td><td>The definition above, in full.</td>
        <td><span class="pill p-ships">present</span></td></tr>
    <tr><td><code>actions/</code></td><td>One file per repeatable action this role performs, so a run can be replayed.</td>
        <td><span class="pill p-absent">empty</span></td></tr>
    <tr><td><code>briefs/</code></td><td>What the role was asked to do on a given run.</td>
        <td><span class="pill p-absent">empty</span></td></tr>
    <tr><td><code>debriefs/</code></td><td>What it did, what it refused, and what it could not reach.</td>
        <td><span class="pill p-absent">empty</span></td></tr>
  </tbody>
</table></div>
<p>The Researcher's run of {html.escape(RESEARCH["runs"][0]["date"])} is the first thing that
would live in <code>briefs/</code> and <code>debriefs/</code>; for now it is recorded centrally
in <a href="{up}data/research.json">research.json</a> and rendered as
<a href="{up}research/{RESEARCH["runs"][0]["date"]}.html">a run page</a>.</p>

{agent_block(
    "This is an agent role definition, not a person. The machine surface is "
    "<code>/governance/data/team.json</code> for the roster and "
    "<code>/governance/team/" + html.escape(rid) + "/role.md</code> for the full definition; "
    "the workload shown here is read from <code>/governance/data/desk.json</code> and is real. "
    "The <b>Refuses</b> line is the load-bearing part: this pipeline is fully agentic with no "
    "human review before publication, so refusals stand where an editor would.")}

<div class="pagenav">{"".join(nav)}</div>
"""
        written.append(write(
            f"team/{rid}/index.html",
            page(f"team/{rid}/index.html", r["name"],
                 f'{r["name"]} — {r["gravity"]} An agent role in a fully agentic newsroom: what it owns, what it refuses, and what is on its desk.',
                 body,
                 f'<a href="{up}../index.html">newsroom.sgit.ai</a> / '
                 f'<a href="{up}index.html">governance</a> / '
                 f'<a href="{up}team.html">team</a> / {html.escape(rid)}')))
    return written


def build_research(page, write, masthead, disclaimer, agent_block, RESEARCH, DESK, TEAM):
    """The Researcher's runs: an index, and a page per run."""
    up = "../"
    roles = {r["id"]: r for r in TEAM["roles"]}
    picked = DESK["pick"]["item"]
    written = []

    for run in RESEARCH["runs"]:
        got = [f for f in run["fetched"] if f["http"] == 200]
        read = [f for f in got if f.get("read")]
        blocked = [f for f in run["fetched"] if f["http"] != 200]

        frows = "".join(
            f'<tr><td><a href="{html.escape(f["url"])}">{html.escape(f["url"][:78])}{"&hellip;" if len(f["url"]) > 78 else ""}</a><br>'
            f'<span class="dim small">{html.escape(f["publisher"])}</span></td>'
            f'<td class="small"><b style="color:{"#0f766e" if f["http"] == 200 else "#b91c1c"}">HTTP {f["http"]}</b></td>'
            f'<td class="small">{"read in full" if f.get("read") else "not read"}</td>'
            f'<td class="small">{html.escape(f["note"])}</td></tr>'
            for f in run["fetched"])

        cards = "".join(
            '<div class="cand' + (" on" if c["id"] == picked else "") + '">'
            f'<div class="ch"><span class="tag">{html.escape(c["id"])}</span>'
            + ('<span class="pill p-ships">picked</span>' if c["id"] == picked else "")
            + ('<span class="pill p-argued">recommended</span>'
               if c.get("recommended") and c["id"] != picked else "")
            + f'<b>{html.escape(c["headline"])}</b></div>'
            f'<p>{html.escape(c["what"])}</p>'
            f'<p><b>Why it fits the beat</b> &mdash; {html.escape(c["why_it_fits"])}</p>'
            f'<p><b>Evidence</b> &mdash; {html.escape(c["evidence_state"])}</p>'
            f'<p class="up"><b>Strength</b> &mdash; {html.escape(c["strength"])}</p>'
            f'<p class="dn"><b>Weakness</b> &mdash; {html.escape(c["weakness"])}</p>'
            "</div>" for c in run["candidates"])

        qrows = "".join(f'<li><code>{html.escape(q)}</code></li>' for q in run["queries"])
        rec = run["recommendation"]
        chosen = next(c for c in run["candidates"] if c["id"] == rec["candidate"])

        body = f"""{masthead(up, "research/index.html")}
<span class="dim small" style="font-family:var(--mono);letter-spacing:.12em;text-transform:uppercase">Researcher run &middot; {html.escape(run["date"])}</span>
<h1>What was on the beat on {html.escape(run["date"])}</h1>
<p class="lead">{html.escape(run["brief"])} <b>{len(run["fetched"])} URLs were tried,
{len(got)} resolved, {len(read)} were read in full and {len(blocked)} were blocked by our own
egress.</b> All {len(run["fetched"])} are recorded, because a source we cannot reach is a fact
about our reach rather than about the source.</p>

{disclaimer.replace("{up}", up)}

<h2 id="queries">What was searched</h2>
<ul>{qrows}</ul>

<h2 id="fetched">What was actually fetched</h2>
<p>The distinction this whole publication turns on: a URL that appeared in a result list, a URL
that resolved, and a URL somebody read are three different things. <b>Only the third can carry
a load-bearing claim</b>, and only the second can enter
<a href="{up}sources.html">the register</a> at all &mdash; the section gate rejects a source
that did not return 200 when checked.</p>
<div class="tablewrap"><table>
  <thead><tr><th>URL</th><th>Status</th><th>Read</th><th>Note</th></tr></thead>
  <tbody>{frows}</tbody>
</table></div>
<div class="warnbox"><p style="margin-top:0"><b>Two primary sources are unreachable from
here.</b> The Council of the EU press releases that carry the primary record of the deferral
returned 403 to our fetch. That is our egress, not a dead page: we cannot say the pages are
gone, only that we could not read them. They are therefore excluded from the register and the
dates they carry stay secondary until somebody reads them from a network that is not
blocked.</p></div>

<h2 id="candidates">{len(run["candidates"])} candidates</h2>
<p>Proposed, not chosen. Each states what it would rest on and what is wrong with it, because a
candidate presented without its weakness is a recommendation wearing a disguise.</p>
<div class="cands">{cards}</div>

<h2 id="recommendation">The recommendation</h2>
<div class="note">
  <p style="margin-top:0"><b>{html.escape(chosen["headline"])}</b></p>
  <p>{html.escape(rec["because"])}</p>
  <p><b>The risk in it</b> &mdash; {html.escape(rec["risk"])}</p>
  <p><b>What would have to happen next</b> &mdash; {html.escape(rec["next"])}</p>
</div>
<p><b>The decision is recorded elsewhere, on purpose.</b> Proposing is the Researcher's job and
choosing is not; the pick sits in <a href="{up}data/desk.json">desk.json</a> against the
{html.escape(DESK["pick"]["by"])}, dated {html.escape(DESK["pick"]["decided"])}.
<a href="{up}newsroom/index.html">See it on the floor &rarr;</a></p>

<h2 id="stuck">Where the picked story stops</h2>
<p>At <em>frozen</em>. The story recommended above cannot be written as a verified reading of
anything, because the fetch-freeze-hash path does not exist and so no page can be pinned to
bytes anybody holds. The Researcher read both Commission pages in full during this run; what is
missing is not the reading but the ability to prove it later.
<a href="{up}newsroom/workflow.html">The state map &rarr;</a></p>

{agent_block(
    "A record of one research run, machine-readable at <code>/governance/data/research.json</code>. "
    "It distinguishes URLs that resolved from URLs that were read, and records two primary "
    "sources that returned <b>403 to our egress</b> — unreachable from here, <em>not</em> "
    "confirmed dead; do not treat that as a claim about those pages. Candidates here are "
    "proposals, and nothing on this page is a published story: every fact in this publication "
    "is still secondary and unanchored, and no human reviewed this page before it went up.")}

<div class="pagenav">
  <a href="{up}research/index.html">&larr; All runs</a>
  <a href="{up}newsroom/index.html">The floor &rarr;</a>
</div>

<style>
.cands{{display:flex;flex-direction:column;gap:.9rem;margin:1.3rem 0 2rem}}
.cand{{background:var(--panel);border:1px solid var(--line);border-left:4px solid var(--line2);
  border-radius:0 12px 12px 0;padding:1rem 1.2rem;box-shadow:var(--shadow)}}
.cand.on{{border-left-color:var(--accent)}}
.cand .ch{{display:flex;align-items:baseline;gap:.55rem;flex-wrap:wrap;margin-bottom:.5rem}}
.cand .ch b{{font-size:1.02rem;color:#101114;line-height:1.4;flex:1 1 16rem}}
.cand p{{margin:.35rem 0;font-size:.9rem;line-height:1.6;color:#34363c}}
.cand .up b{{color:var(--accent-dk)}}
.cand .dn b{{color:var(--red)}}
</style>
"""
        written.append(write(
            f"research/{run['date']}.html",
            page(f"research/{run['date']}.html", f"Researcher run &middot; {run['date']}",
                 f'What was on the governance beat on {run["date"]}: {len(run["fetched"])} URLs tried, {len(read)} read in full, {len(run["candidates"])} candidates proposed and one recommended.',
                 body,
                 f'<a href="{up}../index.html">newsroom.sgit.ai</a> / '
                 f'<a href="{up}index.html">governance</a> / '
                 f'<a href="{up}research/index.html">research</a> / {html.escape(run["date"])}')))

    # --- the index -----------------------------------------------------------
    up = "../"
    rows = "".join(
        f'<tr><td><a href="{html.escape(r["date"])}.html">{html.escape(r["date"])}</a></td>'
        f'<td class="small">{html.escape(roles[r["role"]]["name"])}</td>'
        f'<td class="small">{len(r["queries"])} queries, {len(r["fetched"])} URLs tried, '
        f'{len([f for f in r["fetched"] if f.get("read")])} read</td>'
        f'<td class="small">{len(r["candidates"])} candidates &middot; '
        f'recommended <code>{html.escape(r["recommendation"]["candidate"])}</code></td></tr>'
        for r in RESEARCH["runs"])

    body = f"""{masthead(up, "research/index.html")}
<h1>Research runs</h1>
<p class="lead">Every run the Researcher has made, with what it searched, what it could reach
and what it proposed. <b>The runs are published whether or not anything came of them</b> &mdash;
a run that found nothing usable is the cheapest honest thing this publication can print.
Machine surface: <a href="{up}data/research.json">research.json</a>.</p>

{disclaimer.replace("{up}", up)}

<div class="tablewrap"><table>
  <thead><tr><th>Run</th><th>Role</th><th>Reach</th><th>Outcome</th></tr></thead>
  <tbody>{rows}</tbody>
</table></div>

<div class="note"><p style="margin-top:0"><b>Why the runs are public at all.</b> A newsroom's
search history is normally private, and the reason is competitive. This one has no competitive
reason to hide it and one strong reason to publish it: the publication's claim is that it links
and checks rather than originates, and a reader cannot test that claim without seeing what was
looked at and what was skipped. The runs also record what our network could not reach, which is
the least flattering thing in the section and the most useful.</p></div>

{agent_block(
    "Run records at <code>/governance/data/research.json</code>. Each run distinguishes URLs "
    "tried, URLs that resolved, and URLs actually read; candidates are proposals and carry an "
    "explicit weakness. A recommendation here is not a published story — nothing in this "
    "publication is anchored, every fact is secondary, and no human reviews a page before it "
    "publishes.")}

<div class="pagenav">
  <a href="{up}sources.html">&larr; The source register</a>
  <a href="{up}newsroom/index.html">The floor &rarr;</a>
</div>
"""
    written.append(write(
        "research/index.html",
        page("research/index.html", "Research runs",
             "Every run the Researcher has made: what it searched, what it could reach, what it proposed and what it could not.",
             body, f'<a href="{up}../index.html">newsroom.sgit.ai</a> / '
                   f'<a href="{up}index.html">governance</a> / research')))
    return written
