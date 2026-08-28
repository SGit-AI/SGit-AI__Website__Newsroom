#!/usr/bin/env python3
"""governance/ — the projection.

JSON (the graph, the registers) plus markdown (the prose) in; HTML out. Run from anywhere:

    python3 governance/build/build.py

then `python3 admin/build/chrome.py` to fill in the site nav and footer, then the gates:

    python3 governance/build/gates.py && node admin/build/validate.js

Two decisions worth stating, because they differ from the sibling this pattern is borrowed
from and from the rest of this site:

1. **Markdown is rendered here, at build time, not in the browser.** graphs.sgit.ai renders
   chapters client-side and fails CI if a page lags its source; /documents/ on this site does
   the same. For a NEWS publication that is the wrong trade: this site's own network page
   lists crawler-invisibility of client-assembled pages as an existential risk, and a story
   whose text is not in the HTML is a story search engines and agents cannot read. So the
   prose is baked in, and gates.py re-derives it to prove the page has not drifted.

2. **Every page carries the same disclaimer block.** It is generated, not copied, so it
   cannot rot on one page while being correct on another. The gate checks it is present.
"""
import html
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import floor  # noqa: E402 — same directory; the newsroom floor, state map, role and run pages

ROOT = Path(__file__).resolve().parents[2]
SEC = ROOT / "governance"
DATA = SEC / "data"
CONTENT = SEC / "content"
HOST = "https://newsroom.sgit.ai"


def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


GRAPH = load("graph.json")
STORIES = load("stories.json")
SOURCES = load("sources.json")
ONTOLOGY = load("ontology.json")
TEAM = load("team.json")
DESK = load("desk.json")
WORKFLOW = load("workflow.json")
RESEARCH = load("research.json")

NODES = {n["id"]: n for n in GRAPH["nodes"]}
SRCS = {s["id"]: s for s in SOURCES["sources"]}
VER = STORIES["section_version"]


# ---------------------------------------------------------------- markdown ---
# Deliberately small and deterministic: headings, paragraphs, bold, italic,
# inline code and links. Anything else is a signal the prose is drifting toward
# layout, which belongs in the generator rather than in a story file.
def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
    return t


def md_to_html(src):
    out, para, item, lst = [], [], [], None

    def flush():
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para.clear()

    def flush_item():
        # inline() runs on the WHOLE item, never on a fragment: emphasis that opens on one
        # source line and closes on the next has to survive the wrap.
        if item:
            out.append("<li>" + inline(" ".join(item)) + "</li>")
            item.clear()

    def endlist():
        nonlocal lst
        flush_item()
        if lst:
            out.append(f"</{lst}>")
            lst = None

    for line in src.splitlines():
        s = line.strip()
        bullet = re.match(r"^[-*]\s+(.*)$", s)
        number = re.match(r"^\d+\.\s+(.*)$", s)
        if not s:
            flush()
            endlist()
        elif s.startswith("### "):
            flush()
            endlist()
            out.append(f'<h3>{inline(s[4:])}</h3>')
        elif s.startswith("## "):
            flush()
            endlist()
            slug = re.sub(r"[^a-z0-9]+", "-", s[3:].lower()).strip("-")
            out.append(f'<h2 id="{slug}">{inline(s[3:])}</h2>')
        elif s.startswith("# "):
            flush()
            endlist()
            out.append(f"<h1>{inline(s[2:])}</h1>")
        elif bullet or number:
            flush()
            want = "ul" if bullet else "ol"
            if lst != want:
                endlist()
                out.append(f"<{want}>")
                lst = want
            else:
                flush_item()
            item.append((bullet or number).group(1))
        elif lst:
            item.append(s)          # a wrapped list item, not a new paragraph
        else:
            para.append(s)
    flush()
    endlist()
    return "\n".join(out)


# ------------------------------------------------------------------- shell ---
def page(rel, title, desc, body, crumb):
    """rel is the path under governance/, e.g. 'index.html' or 'stories/x.html'."""
    depth = rel.count("/") + 1          # +1 because every page sits under governance/
    up = "../" * depth
    canonical = f"{HOST}/governance/{rel}"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(title)} &middot; The Governance Wire</title>
<meta name="description" content="{html.escape(desc, quote=True)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="newsroom.sgit.ai">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{html.escape(title, quote=True)}">
<meta property="og:description" content="{html.escape(desc, quote=True)}">
<meta name="twitter:card" content="summary">
<link rel="stylesheet" href="{up}assets/site.css">
</head>
<body>

<nav class="site"><div class="row"></div></nav>

<main class="doc">
<div class="crumb">{crumb}</div>
{body}
</main>

<footer class="site"><div class="cols"></div></footer>
</body>
</html>
"""


def masthead(up, here=""):
    """The section's own identity strip, above the page content."""
    nav = [("index.html", "The wire"),
           ("newsroom/index.html", "The floor"),
           ("newsroom/workflow.html", "Workflow"),
           ("graph.html", "The graph"),
           ("sources.html", "Sources"),
           ("research/index.html", "Research"),
           ("method.html", "Method"),
           ("team.html", "The team"),
           ("about.html", "About &amp; limits")]
    links = "".join(
        f'<a href="{up}{h}" style="font-size:.83rem;color:{"#101114;font-weight:600" if h == here else "#5c5f66"}">{l}</a>'
        for h, l in nav)
    return (
        '<div class="ops" style="margin:0 0 1.4rem">'
        '<div class="op" style="border-left-color:#b45309">'
        '<b style="color:#b45309">The Governance Wire &middot; beta</b>'
        '<p style="display:flex;gap:1.1rem;flex-wrap:wrap;align-items:center;margin-top:.45rem">'
        + links + "</p></div></div>")


DISCLAIMER = (
    '<div class="warnbox">'
    '<p style="margin-top:0"><b>Beta, and fully agentic.</b> This publication is produced '
    'end to end by software agents. <b>No human reviews a page before it is published</b> '
    '&mdash; a named human reads it afterwards, as a reader. Treat everything here as a '
    'draft that has passed structural checks and no editorial ones.</p>'
    '<p><b>Nothing here is anchored yet.</b> Every fact reached this graph from another '
    "publication's reading of a primary text, never from the text itself, and is labelled "
    '<code>secondary</code> in the data and on the page. The verification layer this '
    'publication exists to provide is <em>designed and not running</em>.</p>'
    '<p><b>We do not assess named organisations.</b> There is no legal sign-off for this '
    'publication. It reports what bodies have published, and links to it. '
    '<a href="{up}about.html">The full limits &rarr;</a></p>'
    '</div>')


def agent_block(text):
    return f'<div class="agent"><h4>For an agent</h4><p>{text}</p></div>'


def pill(state):
    cls = {"primary": "p-ships", "secondary": "p-argued",
           "planned": "p-absent"}.get(state, "p-argued")
    return f'<span class="pill {cls}">{html.escape(state)}</span>'


def src_link(sid):
    s = SRCS.get(sid)
    if not s:
        return '<span class="dim">this publication</span>'
    return (f'<a href="{html.escape(s["url"])}">{html.escape(s["publisher"])}</a>')


def write(rel, text):
    p = SEC / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    return f"governance/{rel}"


# --------------------------------------------------------------- the pages ---
def build_index():
    up = ""
    facts = [n for n in GRAPH["nodes"] if n["type"] == "Fact"]
    qs = [n for n in GRAPH["nodes"] if n["type"] == "Question"]
    anchored = [n for n in GRAPH["nodes"] if n.get("anchored")]
    primary = [s for s in SOURCES["sources"] if s["state"] == "primary"]

    cards = []
    for st in STORIES["stories"]:
        qn = len(st.get("questions", []))
        cards.append(
            '<div class="card">'
            f'<span class="tag">{html.escape(st["kicker"])}</span>'
            f'<h3><a href="stories/{st["slug"]}.html">{html.escape(st["title"])}</a></h3>'
            f'<p>{html.escape(st["standfirst"])}</p>'
            f'<p class="dim small" style="margin-top:.6rem">'
            f'{html.escape(st["published"])} &middot; {len(st["nodes"])} nodes &middot; '
            f'{qn} open question{"s" if qn != 1 else ""} &middot; {pill(st["state"])}</p>'
            "</div>")

    body = f"""{masthead(up, "index.html")}
<h1>{html.escape(STORIES["masthead"])}</h1>
<p class="lead">{html.escape(STORIES["beat"])}. A graph, verification and linking layer over
what regulatory bodies publish &mdash; not a source of new claims. <b>Everything below is
somebody else's published material, linked back to them, with our structure on top.</b></p>

{DISCLAIMER.replace("{up}", up)}

<div class="proof">
  <div class="n"><b>{len(GRAPH["nodes"])}</b><span>nodes in the graph</span></div>
  <div class="n"><b>{len(GRAPH["edges"])}</b><span>typed edges</span></div>
  <div class="n"><b>{len(qs)}</b><span>open questions</span></div>
  <div class="n"><b>{len(anchored)} of {len(facts)}</b><span>facts anchored to source bytes</span></div>
</div>

<h2 id="stories">The wire</h2>
<div class="cards">
{"".join(cards)}
</div>

<h2 id="newsroom">The newsroom</h2>
<p>Not the output &mdash; the room. Seven agent desks, the state a story has to move through to
reach the wire, and the Researcher's runs published whether or not anything came of them.</p>
<div class="cards">
  <div class="card"><span class="tag">Scene</span>
    <h3><a href="newsroom/index.html">The floor</a></h3>
    <p>Click a verb, then a desk. Each role answers from the same data the rest of the section
    is built on, including what it is holding and why it is stuck.</p></div>
  <div class="card"><span class="tag">State</span>
    <h3><a href="newsroom/workflow.html">How a story moves</a></h3>
    <p>Nine states from search result to published page, each with the door it has to get
    through. <b>One of those doors is shut</b>, and it is the reason nothing here is anchored.</p></div>
  <div class="card"><span class="tag">Runs</span>
    <h3><a href="research/index.html">Research runs</a></h3>
    <p>What was searched, what resolved, what was actually read, and what our own network could
    not reach. Candidates proposed with their weaknesses attached.</p></div>
  <div class="card"><span class="tag">Roles</span>
    <h3><a href="team.html">The team</a></h3>
    <p>Seven roles, none of them a person, each with a folder, a centre of gravity and a list of
    what it refuses to do under pressure.</p></div>
</div>

<h2 id="state">Where this actually is</h2>
<p>The honest position, stated before anything else on the page can imply otherwise:</p>
<div class="tablewrap"><table>
  <thead><tr><th>Capability</th><th>State</th><th>What that means here</th></tr></thead>
  <tbody>
    <tr><td>Typed graph over the beat</td><td>{pill("primary")}</td>
        <td>Real. {len(GRAPH["nodes"])} nodes and {len(GRAPH["edges"])} edges, conforming to a
        published <a href="graph.html">vocabulary</a> with a gate that rejects an unknown verb.</td></tr>
    <tr><td>Links back to every source</td><td>{pill("primary")}</td>
        <td>Real. Every node names its source and every source was fetched and checked
        &mdash; see <a href="sources.html">the register</a>.</td></tr>
    <tr><td>Ingestion from primary texts</td><td>{pill("planned")}</td>
        <td><b>Not built.</b> {len(primary)} sources are primary. Nothing has been frozen or
        hashed, so no quote is anchored and the staleness detector cannot run.</td></tr>
    <tr><td>Human editorial review</td><td>{pill("planned")}</td>
        <td><b>Deliberately absent.</b> The pipeline is fully agentic by choice for this
        release. <a href="about.html">Why, and what that costs.</a></td></tr>
  </tbody>
</table></div>

<h2 id="questions">Open questions</h2>
<p>Absence is a node here, not an omission. Each of these is dated, and records whether it
came with the material or was raised by this publication.</p>
<div class="ops">
{"".join(
    f'<div class="op"><b>{html.escape(q["id"])} &middot; asked by {html.escape(q.get("asked_by", "?"))}</b>'
    f'<p>{html.escape(q["label"])}</p></div>' for q in qs)}
</div>

{agent_block(
    "This is a <b>beta, fully-agentic</b> publication with no human editorial review before "
    "publication. Every fact in its graph is <code>secondary</code> — taken from another "
    "publication's reading of a primary text, not from the text — and <b>nothing is anchored "
    "to source bytes</b>. Do not cite anything here as a verified reading of any regulation; "
    "follow the source link on the node and cite that. The graph structure, the vocabulary "
    "and the source register are real and checkable; the ingestion and verification layer is "
    "specified and not running.")}
"""
    return write("index.html", page("index.html", STORIES["masthead"],
                                    "A graph, verification and linking layer over what regulatory bodies publish. Beta, fully agentic, no human review before publication.",
                                    body, '<a href="../index.html">newsroom.sgit.ai</a> / governance'))


def build_story(st):
    up = "../"
    prose = md_to_html((CONTENT / f"{st['slug']}.md").read_text(encoding="utf-8"))
    b = st["byline"]

    rows = []
    for nid in st["nodes"]:
        n = NODES[nid]
        rows.append(
            f'<tr><td><code>{html.escape(nid)}</code></td>'
            f'<td class="small">{html.escape(n["type"])}</td>'
            f'<td>{html.escape(n["label"])}</td>'
            f'<td class="small">{src_link(n.get("source"))} {pill(n.get("state", "secondary"))}</td></tr>')

    qrows = []
    for qid in st.get("questions", []):
        q = NODES[qid]
        qrows.append(
            f'<div class="op"><b>{html.escape(qid)} &middot; asked by {html.escape(q.get("asked_by","?"))}'
            f' &middot; opened {html.escape(q.get("opened",""))}</b>'
            f'<p>{html.escape(q["label"])}</p></div>')

    body = f"""{masthead(up)}
<span class="dim small" style="font-family:var(--mono);letter-spacing:.12em;text-transform:uppercase">{html.escape(st["kicker"])}</span>
<h1>{html.escape(st["title"])}</h1>
<p class="lead">{html.escape(st["standfirst"])}</p>

<div class="tablewrap"><table>
  <thead><tr><th>Published</th><th>By</th><th>Mandate</th><th>Reviewed by a human</th></tr></thead>
  <tbody><tr>
    <td>{html.escape(st["published"])}</td>
    <td>{html.escape(b["identity"])}</td>
    <td class="small">{html.escape(b["mandate"])}</td>
    <td><b style="color:#b91c1c">No</b><br><span class="dim small">{html.escape(b["underwriter_note"])}</span></td>
  </tr></tbody>
</table></div>

{DISCLAIMER.replace("{up}", up)}

{prose}

<h2 id="nodes">What this story stands on</h2>
<p>Every sentence above traces to one of these. If a claim in the prose is not here, that is a
defect in the story rather than a fact about the world.</p>
<div class="tablewrap"><table>
  <thead><tr><th>Node</th><th>Type</th><th>Statement</th><th>Source</th></tr></thead>
  <tbody>{"".join(rows)}</tbody>
</table></div>

<h2 id="open">Open questions from this story</h2>
<div class="ops">{"".join(qrows)}</div>

{agent_block(
    f"This story is a projection of {len(st['nodes'])} graph nodes, every one of them "
    "<code>secondary</code> and none anchored to source bytes. <b>No human reviewed it before "
    "publication.</b> Cite the sources in the table, not this page. Its open questions are "
    "genuinely open — do not treat the absence of an answer here as evidence that none exists.")}

<div class="pagenav">
  <a href="{up}index.html">&larr; The wire</a>
  <a href="{up}graph.html">The graph &rarr;</a>
</div>
"""
    return write(f"stories/{st['slug']}.html",
                 page(f"stories/{st['slug']}.html", st["title"], st["standfirst"], body,
                      f'<a href="{up}../index.html">newsroom.sgit.ai</a> / '
                      f'<a href="{up}index.html">governance</a> / {html.escape(st["slug"])}'))


def build_graph_page():
    up = ""
    by_type = {}
    for n in GRAPH["nodes"]:
        by_type.setdefault(n["type"], []).append(n)

    tsec = []
    for t in ONTOLOGY["node_types"]:
        items = by_type.get(t["id"], [])
        rows = "".join(
            f'<tr><td><code>{html.escape(n["id"])}</code></td><td>{html.escape(n["label"])}</td>'
            f'<td class="small">{src_link(n.get("source"))} {pill(n.get("state","secondary"))}</td></tr>'
            for n in items)
        if not items:
            unused = next((u for u in GRAPH.get("unused_node_types", []) if u["type"] == t["id"]), None)
            rows = ('<tr><td colspan="3" class="small dim">No instances. '
                    + html.escape(unused["why"] if unused else "None yet.") + "</td></tr>")
        tsec.append(
            f'<h3 id="t-{t["id"].lower()}">{html.escape(t["label"])} '
            f'<span class="dim small" style="font-weight:400">&mdash; {len(items)}</span></h3>'
            f'<p class="small dim">{html.escape(t["definition"])}</p>'
            f'<div class="tablewrap"><table><thead><tr><th>Node</th><th>Label</th><th>Source</th></tr></thead>'
            f"<tbody>{rows}</tbody></table></div>")

    erows = "".join(
        f'<tr><td><code>{html.escape(e["verb"])}</code></td><td><code>{html.escape(e["inverse"])}</code></td>'
        f'<td class="small">{html.escape(e["domain"])} &rarr; {html.escape(e["range"])}</td>'
        f'<td class="small">{html.escape(e["sentence"])}</td>'
        f'<td>{pill("primary") if e["origin"] == "inherited" else pill("secondary")}</td></tr>'
        for e in ONTOLOGY["edges"])

    used = sorted({e["verb"] for e in GRAPH["edges"]})
    frows = "".join(
        f'<div class="op"><b>{html.escape(f["id"])}</b><p><code>{html.escape(f["expression"])}</code><br>'
        f'{html.escape(f["note"])}</p></div>' for f in ONTOLOGY["formulas"])
    brows = "".join(
        f'<tr><td><code>{html.escape(b["verb"])}</code></td><td>{html.escape(b["why"])}</td></tr>'
        for b in ONTOLOGY["banned"])

    body = f"""{masthead(up, "graph.html")}
<h1>The graph</h1>
<p class="lead">Every node and every edge this publication currently holds, with the
vocabulary they conform to. <b>The machine surfaces are
<a href="data/graph.json">graph.json</a> and <a href="data/ontology.json">ontology.json</a></b>
&mdash; this page is a projection of them and cannot say anything they do not.</p>

{DISCLAIMER.replace("{up}", up)}

<h2 id="vocabulary">The edge vocabulary</h2>
<p>Every edge is a verb with a distinct, meaningfully-named inverse. Four are inherited
unchanged from <a href="{ONTOLOGY["inherits_from"]["page"]}">the established set</a> at
{html.escape(ONTOLOGY["inherits_from"]["site"])}; the rest are proposed here for this beat
and are marked as such, because a borrowed word carries its meaning with it and a new one
does not.</p>
<div class="tablewrap"><table>
  <thead><tr><th>Verb</th><th>Inverse</th><th>Domain &rarr; range</th><th>Reads as</th><th>Origin</th></tr></thead>
  <tbody>{erows}</tbody>
</table></div>
<p class="small dim">In use in the current graph: {", ".join(f"<code>{html.escape(v)}</code>" for v in used)}.</p>

<h2 id="banned">Banned</h2>
<div class="tablewrap"><table>
  <thead><tr><th>Verb</th><th>Why</th></tr></thead><tbody>{brows}</tbody>
</table></div>

<h2 id="formulas">Classification is a formula</h2>
<p>A node type is not a label somebody applied; it is a query anybody can argue with. Change a
formula and everything it touches reclassifies at once &mdash; which is a correction, and is
published as one.</p>
<div class="ops">{frows}</div>

<h2 id="nodes">The nodes</h2>
{"".join(tsec)}

{agent_block(
    "Fetch <code>/governance/data/graph.json</code> and <code>/governance/data/ontology.json</code> "
    "rather than parsing this page. Every node carries <code>source</code>, <code>state</code> and "
    "<code>anchored</code>; in this release <b>every node is <code>secondary</code> and "
    "<code>anchored</code> is false throughout</b>. An edge verb outside the ontology is a build "
    "failure, not a variant — the gate rejects it.")}

<div class="pagenav">
  <a href="index.html">&larr; The wire</a>
  <a href="sources.html">The source register &rarr;</a>
</div>
"""
    return write("graph.html", page("graph.html", "The graph",
                                    "Every node and edge the publication holds, and the vocabulary they conform to.",
                                    body, '<a href="../index.html">newsroom.sgit.ai</a> / <a href="index.html">governance</a> / graph'))


def build_sources():
    up = ""
    srows = "".join(
        f'<tr><td><a href="{html.escape(s["url"])}">{html.escape(s["title"])}</a><br>'
        f'<span class="dim small">{html.escape(s["publisher"])} &middot; checked '
        f'{html.escape(s["checked"])} &middot; HTTP {s["http"]}</span></td>'
        f'<td>{pill(s["state"])}</td>'
        f'<td class="small">{html.escape(s["note"])}</td></tr>'
        for s in SOURCES["sources"])

    prows = "".join(
        f'<tr><td><b>{html.escape(p["class"])}</b></td>'
        f'<td class="small">{html.escape(p["why"])}</td>'
        f'<td class="small">{html.escape(p["blocked_on"])}</td></tr>'
        for p in SOURCES["planned"])

    drows = "".join(
        f'<tr><td>{pill(d["id"])}</td><td class="small">{html.escape(d["definition"])}</td></tr>'
        for d in SOURCES["ingestion_states"])

    body = f"""{masthead(up, "sources.html")}
<h1>The source register</h1>
<p class="lead">Where every fact came from, and whether anybody read the original. <b>The
register exists so a reader never has to ask.</b> Machine surface:
<a href="data/sources.json">sources.json</a>.</p>

{DISCLAIMER.replace("{up}", up)}

<h2 id="states">Three states</h2>
<div class="tablewrap"><table>
  <thead><tr><th>State</th><th>Means</th></tr></thead><tbody>{drows}</tbody>
</table></div>

<h2 id="ingested">Ingested</h2>
<p>Every URL below was fetched and its status recorded on the date shown. <b>None is
primary</b> &mdash; every one is another publication's reading of a text, which is the single
most important limitation of this release.</p>
<div class="tablewrap"><table>
  <thead><tr><th>Source</th><th>State</th><th>Note</th></tr></thead><tbody>{srows}</tbody>
</table></div>

<h2 id="planned">In scope, not ingested</h2>
<p>The classes this beat is meant to watch. Official publications and news issued by
regulatory bodies are the centre of it: dated, attributable, and issued by the body with
authority over the text.</p>
<div class="tablewrap"><table>
  <thead><tr><th>Class</th><th>Why it matters</th><th>Blocked on</th></tr></thead><tbody>{prows}</tbody>
</table></div>

{agent_block(
    "Every source here was fetched and its HTTP status recorded on the stated date. "
    "<b>No source is <code>primary</code>:</b> nothing has been frozen, hashed or anchored, so "
    "no claim on this site is a verified reading of a regulation. To verify anything, follow "
    "the source link and read the original. The <code>planned</code> table is scope, not "
    "capability — none of those classes is being ingested today.")}

<div class="pagenav">
  <a href="graph.html">&larr; The graph</a>
  <a href="method.html">The method &rarr;</a>
</div>
"""
    return write("sources.html", page("sources.html", "The source register",
                                      "Where every fact came from, and whether anybody read the original.",
                                      body, '<a href="../index.html">newsroom.sgit.ai</a> / <a href="index.html">governance</a> / sources'))


def build_method():
    up = ""
    steps = "".join(
        f'<li><span class="when">Step {p["step"]} &middot; {html.escape(p["role"])}</span>'
        f'<span class="what">{html.escape(p["does"])}</span></li>'
        for p in TEAM["pipeline"])

    body = f"""{masthead(up, "method.html")}
<h1>The method</h1>
<p class="lead"><b>We do not report facts. We link, type and check other people's.</b> Every
claim this publication carries was published by somebody else; what is added is a typed graph
over it, a link back to it, and a record of whether anyone read the original.</p>

{DISCLAIMER.replace("{up}", up)}

<h2 id="layer">What the layer actually adds</h2>
<div class="cards">
  <div class="card"><span class="tag">Linking</span><h3>A path back to the original</h3>
    <p>Every node names a source, and every source in the register was fetched with its status
    recorded. Nothing is asserted without somewhere to go and check it.</p></div>
  <div class="card"><span class="tag">Typing</span><h3>Claims become structure</h3>
    <p>A statement becomes a Fact with edges to the Provision it sits in and the Questions it
    raises. Structure is what lets a correction find everything downstream of it.</p></div>
  <div class="card"><span class="tag">Verification</span><h3>Designed, not running</h3>
    <p>Freezing a source, hashing it and anchoring quotes to byte offsets is the step that turns
    a link into a check. <b>This release does not do it</b>, and every page says so.</p></div>
  <div class="card"><span class="tag">Absence</span><h3>What is missing is counted</h3>
    <p>An unanswered question is a node with an identifier and an opening date &mdash; including
    when the missing thing is ours, as with the four questions we could not carry across.</p></div>
</div>

<h2 id="pipeline">Seven steps, seven roles</h2>
<p>One role per step, each with its own centre of gravity and its own refusals. Nobody in this
list is a person. The same seven steps are the route drawn through
<a href="newsroom/index.html">the newsroom floor</a>, and a gate compares the two so the room
cannot draw a workflow the publication does not run.</p>
<ul class="timeline">{steps}</ul>
<p>What a step means in practice &mdash; what has to be true before the next role will take the
work &mdash; is <a href="newsroom/workflow.html">the state map</a>. There are nine states and
one of them is currently shut.</p>

<h2 id="prose">Why the prose is baked into the page</h2>
<p>The sibling site this pattern comes from renders markdown in the browser and fails its build
if a page lags its source. This section renders at build time instead, for a reason specific to
news: <a href="../network/index.html#risks">this site lists crawler-invisibility of
client-assembled pages as an inherited existential risk</a>, and a story whose text is not in
the HTML is a story an agent or a search engine cannot read. The gate re-derives every story
page from its markdown and fails if the two have drifted, so the guarantee is kept without
paying that cost.</p>

<h2 id="gates">What the gate checks</h2>
<p>Structural, cheap, and impossible to satisfy by writing more confidently. Full list in
<code>governance/build/gates.py</code>; the section also passes the whole-site gate. Checks 9
to 13 arrived with the newsroom itself &mdash; a room that draws a workflow is a new way of
being wrong, and each of them is a mistake that was possible before it was written.</p>
<div class="tablewrap"><table>
  <thead><tr><th>#</th><th>Check</th><th>Why it exists</th></tr></thead>
  <tbody>
    <tr><td>1</td><td>Every node's source resolves to a register entry, or its origin is declared</td>
        <td>A fact with nowhere to go back to is the failure this whole publication is about</td></tr>
    <tr><td>2</td><td>Every edge verb exists in the ontology; no banned verb appears</td>
        <td>A plausible edge is indistinguishable from a true one once it is in the file</td></tr>
    <tr><td>3</td><td>Every story's cited node ids exist</td>
        <td>Prose that cites a node the graph does not have is prose nobody can check</td></tr>
    <tr><td>4</td><td>No page claims an anchor the data does not carry</td>
        <td>Showing a verification state that does not exist would be the worst thing here</td></tr>
    <tr><td>5</td><td>Every story page matches its markdown</td>
        <td>The projection cannot drift from its source</td></tr>
    <tr><td>6</td><td>Beta notice and no-human-review statement on every page</td>
        <td>The limitation must not rot on one page while being correct on another</td></tr>
    <tr><td>7</td><td>Every registered source returned 200 when it was checked</td>
        <td>A URL nobody could reach is not a citation</td></tr>
    <tr><td>8</td><td>The team is declared fully agentic, and every role states its refusals</td>
        <td>The refusals stand where an editor would; a role without them is decorative</td></tr>
    <tr><td>9</td><td>The state machine is closed: every exit names a real state, every
        non-terminal state has one, every blocked state says why</td>
        <td>A workflow whose exits go nowhere is a diagram, not a machine</td></tr>
    <tr><td>10</td><td>Every desk item sits in a real state with a real owner, nothing
        unpublished is silent about why it is not moving, and the pick is not held by a
        pipeline role</td>
        <td>Proposing and choosing are separate on purpose, and a stalled story with no stated
        blocker is indistinguishable from a forgotten one</td></tr>
    <tr><td>11</td><td>A URL that failed to resolve cannot appear in the source register, and
        its note must distinguish our reach from the state of the page</td>
        <td>Two Council pages return 403 to us. That is a fact about our network, and it must
        never quietly become a fact about them</td></tr>
    <tr><td>12</td><td>Every role has a page; the floor, the state map and the run pages exist</td>
        <td>A roster that links to nothing is a list</td></tr>
    <tr><td>13</td><td>The desk layout on the floor runs the same seven steps, in the same
        order, as the pipeline</td>
        <td>Reorder the pipeline and the room would keep drawing a route through a workflow
        nobody runs</td></tr>
  </tbody>
</table></div>

{agent_block(
    "This publication adds structure and links over other organisations' published material; "
    "it originates no claims of its own. The verification step (freeze, hash, anchor) is "
    "specified and <b>not implemented</b>, so treat every claim as an unverified pointer to a "
    "source rather than a checked reading of it. The pipeline is fully agentic with no human "
    "review at any step.")}

<div class="pagenav">
  <a href="sources.html">&larr; Sources</a>
  <a href="team.html">The team &rarr;</a>
</div>
"""
    return write("method.html", page("method.html", "The method",
                                     "We do not report facts. We link, type and check other people's — and the verification step is designed, not running.",
                                     body, '<a href="../index.html">newsroom.sgit.ai</a> / <a href="index.html">governance</a> / method'))


def build_team():
    up = ""
    cards = "".join(
        f'<div class="card"><span class="tag">{html.escape(r["id"])}</span>'
        f'<h3>{html.escape(r["name"])}</h3>'
        f'<p><b>{html.escape(r["gravity"])}</b></p>'
        f'<p style="margin-top:.5rem"><b>Owns</b> &mdash; {html.escape(r["owns"])}</p>'
        f'<p><b>Refuses</b> &mdash; {html.escape(r["refuses"])}</p>'
        f'<p><b>Wrong when</b> &mdash; {html.escape(r["wrong_when"])}</p>'
        f'<p class="dim small" style="margin-top:.55rem">'
        f'<a href="team/{r["id"]}/index.html"><b>The {html.escape(r["name"])}\u2019s desk &rarr;</b></a>'
        f' &middot; <a href="team/{r["id"]}/role.md">role.md</a></p>'
        "</div>" for r in TEAM["roles"])

    opens = "".join(
        f'<div class="op"><b>{html.escape(o["id"])}</b><p>{html.escape(o["what"])}</p></div>'
        for o in TEAM["open"])

    body = f"""{masthead(up, "team.html")}
<h1>The agentic team</h1>
<p class="lead">{html.escape(TEAM["roles"][0]["gravity"].split(",")[0])} &mdash; and six other
centres of gravity. <b>Seven roles, none of them a person.</b> The shape is borrowed from
<a href="{TEAM["inherits_from"]["page"]}">{html.escape(TEAM["inherits_from"]["site"])}</a>;
the definitions are written for this beat, because a generic newsroom role would refuse
nothing in particular.</p>

{DISCLAIMER.replace("{up}", up)}

<div class="note"><p style="margin-top:0"><b>Why each role states what it refuses.</b> A
centre of gravity tells you what an agent is for; a refusal tells you what it will not do
under pressure. In a pipeline with no human reviewer the refusals are the only thing standing
where a duty editor would normally stand, so they are written as rules rather than judgement
calls &mdash; a rule survives an agent having a bad day.</p></div>

<h2 id="roles">Seven roles</h2>
<p>Each has a folder and a page of its own: the definition in full, the doors it is the only
role that can open, and whatever is sitting on its desk right now &mdash; read from
<a href="data/desk.json">desk.json</a> at build time, so a role page cannot describe a
workload the newsroom does not have.</p>
<div class="cards">{cards}</div>

<h2 id="open">What the team does not yet have</h2>
<div class="ops">{opens}</div>

{agent_block(
    "Seven agent roles, no humans, no human review before publication. Each role's full "
    "definition is a markdown file at <code>/governance/team/&lt;role&gt;/role.md</code> and the "
    "roster is machine-readable at <code>/governance/data/team.json</code>. The Researcher's "
    "centre of gravity — no claim without a source somebody fetched — is currently "
    "<b>aspirational</b>: the ingestion path it describes does not exist.")}

<div class="pagenav">
  <a href="method.html">&larr; The method</a>
  <a href="about.html">About &amp; limits &rarr;</a>
</div>
"""
    return write("team.html", page("team.html", "The agentic team",
                                   "Seven roles, none of them a person, each with a centre of gravity and a list of what it refuses.",
                                   body, '<a href="../index.html">newsroom.sgit.ai</a> / <a href="index.html">governance</a> / team'))


def build_about():
    up = ""
    body = f"""{masthead(up, "about.html")}
<h1>About, and the limits</h1>
<p class="lead"><b>The Governance Wire is a beta.</b> It is produced end to end by software
agents, it has had no legal review, and the verification layer that gives it its reason to
exist is specified but not running. This page is the list of everything a reader should hold
against it.</p>

<h2 id="what">What it is</h2>
<p>A publication covering {html.escape(STORIES["beat"]).lower()}. It originates no facts.
Everything it carries was published by another organisation &mdash; regulators, supervisory
bodies, standards bodies, and for now the sibling sites of this network. What it adds is a
<b>graph, verification and linking layer</b>: typed structure over other people's material, a
path back to the original, and a record of whether anybody read that original.</p>
<div class="claim">If a claim here is interesting, follow its source link and cite that.
This publication is a finding aid, not an authority.</div>

<h2 id="limits">The limits, in order of how much they should worry you</h2>
<div class="ops">
  <div class="op"><b>1 &middot; No human reviews anything before it publishes</b>
    <p>Deliberate for this release. Seven agent roles run the pipeline; a named human reads the
    output afterwards, as a reader, and can pull anything that has gone off. That is a real
    safety model but it is a <em>detection</em> model, not a <em>prevention</em> one: a mistake
    is public before it is caught.</p></div>
  <div class="op"><b>2 &middot; Nothing is anchored</b>
    <p>Every fact is <code>secondary</code>. No primary artefact has been fetched, frozen or
    hashed, so no quote is pinned to a byte range and the staleness detector described in
    <a href="method.html">the method</a> cannot run. The verification layer is the product, and
    in this release it is a design.</p></div>
  <div class="op"><b>3 &middot; No legal sign-off</b>
    <p>There is none. The publication therefore <b>does not assess, score or characterise any
    named organisation</b>, and the editor role refuses it structurally rather than case by
    case. Reporting what a body itself published, with a link, is the whole permitted
    surface.</p></div>
  <div class="op"><b>4 &middot; The seed is small and second-hand</b>
    <p>{len(GRAPH["nodes"])} nodes drawn from {len(SOURCES["sources"])} sources, none of them a
    regulator. It is enough to prove the structure and nothing like enough to cover a beat.</p></div>
  <div class="op"><b>5 &middot; It reports on a field it is part of</b>
    <p>A publication about the governance of autonomous systems, written by autonomous systems.
    Either the strongest demonstration available or the most obvious conflict, depending
    entirely on whether it holds itself to what it reports against &mdash; which is why the
    agent roles, their refusals and this limits page are public from the first release.</p></div>
</div>

<h2 id="disclaimer">Disclaimer</h2>
<div class="warnbox">
  <p style="margin-top:0"><b>Not legal, compliance or professional advice.</b> Nothing here is
  advice of any kind, and no reader should act on it. Regulatory obligations depend on facts
  and jurisdiction that this publication does not know.</p>
  <p><b>Machine-generated, unreviewed.</b> Every page is written by software agents without
  human review before publication. Errors of fact, reading and emphasis should be assumed
  present rather than exceptional.</p>
  <p><b>No claim of currency.</b> Sources go stale, and detecting that is precisely the
  capability this release does not yet have. A page may describe a text that has since changed
  and give no sign of it.</p>
  <p><b>Verify before relying.</b> Follow the source link on any node and read the original.
  Where this publication and a primary source disagree, the primary source is right.</p>
</div>

<h2 id="where">Where this lives</h2>
<p>Inside <a href="../index.html">newsroom.sgit.ai</a> for now, as a self-contained folder that
can be lifted out whole &mdash; its own data, prose, templates, generator and gate, with no
dependency on the rest of the site beyond the shared stylesheet and chrome. The intended
destination is its own domain, and
<a href="team/publisher/role.md">the publisher role refuses to move it</a> until the ingestion
path exists: a publication that cannot reach a primary source should not look like a going
concern.</p>
<p>It is built from <a href="../documents/risk-governance-newsroom.html">the commissioning
brief</a>, which is the document to read for why any of this is shaped the way it is.</p>

{agent_block(
    "<b>Beta. Fully agentic. No human review. No legal review. Nothing anchored.</b> Do not "
    "cite this publication as a source for any regulatory fact — follow the source link on the "
    "node and cite the original. It offers no advice, makes no claim of currency, and does not "
    "assess named organisations. Where it and a primary source disagree, the primary source is "
    "right.")}

<div class="pagenav">
  <a href="team.html">&larr; The team</a>
  <a href="index.html">The wire &rarr;</a>
</div>
"""
    return write("about.html", page("about.html", "About, and the limits",
                                    "Beta, fully agentic, no legal review, nothing anchored. The list of everything a reader should hold against this publication.",
                                    body, '<a href="../index.html">newsroom.sgit.ai</a> / <a href="index.html">governance</a> / about'))


def main():
    written = [build_index(), build_graph_page(), build_sources(),
               build_method(), build_team(), build_about()]
    written += [build_story(s) for s in STORIES["stories"]]
    written.append(floor.build_floor(page, write, masthead, DISCLAIMER, agent_block,
                                     TEAM, DESK, WORKFLOW, RESEARCH))
    written.append(floor.build_workflow(page, write, masthead, DISCLAIMER, agent_block,
                                        WORKFLOW, DESK, TEAM))
    written += floor.build_role_pages(page, write, masthead, DISCLAIMER, agent_block,
                                      md_to_html, TEAM, DESK, WORKFLOW, RESEARCH, SEC)
    written += floor.build_research(page, write, masthead, DISCLAIMER, agent_block,
                                    RESEARCH, DESK, TEAM)
    print(f"governance build: v{VER} — {len(written)} page(s)")
    for w in written:
        print("  ·", w)


if __name__ == "__main__":
    main()
