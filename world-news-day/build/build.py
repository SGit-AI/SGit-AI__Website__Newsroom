#!/usr/bin/env python3
"""world-news-day/ — the projection.

    python3 world-news-day/build/extract.py --fetch   # fetch, freeze, hash   (network)
    python3 world-news-day/build/build.py             # graph + analysis + pages
    python3 admin/build/chrome.py
    python3 world-news-day/build/gates.py && node admin/build/validate.js

This section holds something no other section on this site holds: twenty-one complete
opinion pieces by the people who run the world's newsrooms, published on the same day,
under a permission that invites republication — and it republishes none of them.

That is the whole design. The pieces are worth reading and they are one click away. What is
missing, and what this section supplies, is everything a machine would need to do anything
with them at scale: a licence with a name, a record of what the terms actually say, a
structured description of each piece, and a graph that connects them. The op-eds are the
industry's argument for why journalism matters. This section is a worked example of the
infrastructure that argument currently lacks.

Pages, in the order they were built:

  index.html     what this is, and the three questions
  licences.html  THE FINDING: what the permission is, in the bytes, and what it is not
  corpus.html    the twenty-one, as a table a machine can also read
  findings.html  the aggregate: what twenty-one editors said together, and did not say
  graph.html     the same thing as a graph, with the vocabulary published
  sources.html   every frozen file, its SHA-256, and the one page we could not fetch
  method.html    how it is built, and what it refuses to do
"""
import html
import importlib.util
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

ROOT = Path(__file__).resolve().parents[2]
SEC = ROOT / "world-news-day"
DATA = SEC / "data"
HOST = "https://newsroom.sgit.ai"
ANNOUNCEMENT = "https://wan-ifra.org/2026/09/world-news-day-21-great-op-eds-on-why-journalism-matters/"


def load(n):
    return json.loads((DATA / n).read_text(encoding="utf-8"))


import graph as graphmod      # noqa: E402 — ontology, graph, triples, licence findings, manifest
import analysis as analysismod  # noqa: E402 — the aggregate counts
graphmod.main()
analysismod.main()
graphmod.manifest()   # last: it hashes everything the two steps above wrote

REGISTER = load("register.json")
CORPUS = load("corpus.json")
LICENCES = load("licences.json")
ONTOLOGY = load("ontology.json")
GRAPH = load("graph.json")
LEXICON = load("lexicon.json")
AFFILIATIONS = load("affiliations.json")
ANALYSIS = load("analysis.json")
MANIFEST = load("manifest.json")
LATEST = REGISTER["snapshots"][-1]
SRC = {s["id"]: s for s in REGISTER["sources"]}

# The panel CSS for the graph instrument is defined once, in the section that first built it.
# Copying it here would mean two copies drifting apart; this way /portugal/ and this section
# are provably the same instrument.
_spec = importlib.util.spec_from_file_location("pt_pages", ROOT / "portugal" / "build" / "pages.py")
_pt = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_pt)
GRAPH_CSS = _pt.GRAPH_CSS

# Labels in both languages from day one. Nothing here is published in Portuguese yet — the
# pt side is what makes pt.newsroom.sgit.ai a switch rather than a rewrite, and the method
# page says plainly that the switch has not been thrown.
LABELS = {
    "index":    {"en": "The corpus",   "pt": "O corpus"},
    "licences": {"en": "The licence",  "pt": "A licença"},
    "corpus":   {"en": "The 21",       "pt": "Os 21"},
    "findings": {"en": "The aggregate", "pt": "O agregado"},
    "graph":    {"en": "The graph",    "pt": "O grafo"},
    "sources":  {"en": "Sources",      "pt": "Fontes"},
    "method":   {"en": "Method",       "pt": "Método"},
}
NAV = [("index.html", "index"), ("licences.html", "licences"), ("corpus.html", "corpus"),
       ("findings.html", "findings"), ("graph.html", "graph"), ("sources.html", "sources"),
       ("method.html", "method")]


def esc(x):
    return html.escape(str(x) if x is not None else "")


def page(rel, title, desc, body, crumb):
    canonical = f"{HOST}/world-news-day/{rel}"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)} &middot; World News Day 2026</title>
<meta name="description" content="{html.escape(desc, quote=True)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="newsroom.sgit.ai">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{html.escape(title, quote=True)}">
<meta property="og:description" content="{html.escape(desc, quote=True)}">
<meta name="twitter:card" content="summary">
<link rel="stylesheet" href="../assets/site.css">
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


def masthead(here=""):
    links = "".join(
        f'<a href="{h}" style="font-size:.83rem;color:'
        f'{"#101114;font-weight:600" if h == here else "#5c5f66"}">{esc(LABELS[k]["en"])}</a>'
        for h, k in NAV)
    return ('<div class="ops" style="margin:0 0 1.4rem">'
            '<div class="op" style="border-left-color:#b91c1c">'
            '<b style="color:#b91c1c">World News Day 2026 &middot; beta</b>'
            '<p style="display:flex;gap:1.1rem;flex-wrap:wrap;align-items:center;margin-top:.45rem">'
            + links + "</p></div></div>")


def disclaimer():
    return (
        '<div class="warnbox">'
        '<p style="margin-top:0"><b>Beta, agent-produced.</b> The fetching, extraction, '
        'classification and drafting here are done by software agents against frozen bytes. '
        'Nothing on this page is a legal opinion, and there has been no legal review. If you '
        'are deciding whether you may republish one of these pieces, read the terms on the '
        'piece itself and ask the publisher &mdash; that is the point we are making.</p>'
        '<p><b>We hold all twenty-one pieces and republish none of them.</b> Every article is '
        'linked to its original on <code>worldnewsday.org</code>. What is published here is '
        'the <em>description</em>: who wrote it, under what terms, what it links to, what '
        'words it contains. The prose belongs to the people who wrote it, and the gate on '
        'this section fails the build if twelve consecutive words of any piece appear on any '
        'page we generate.</p>'
        '<p><b>Every number walks back to bytes we hold.</b> Each page was fetched once, '
        'frozen to a dated snapshot in this repository and hashed with SHA-256. The counts are '
        're-derived from those bytes by a second program before anything ships. '
        '<a href="sources.html">The register &rarr;</a> &middot; '
        '<a href="method.html">The method &rarr;</a></p>'
        '</div>')


def agent_block(t):
    return f'<div class="agent"><h4>For an agent</h4><p>{t}</p></div>'


def write(rel, text):
    p = SEC / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    return f"world-news-day/{rel}"


def art_by_slug():
    return {a["slug"]: a for a in CORPUS["articles"]}


def themes_of(slug):
    nodes = {n["id"]: n for n in GRAPH["nodes"]}
    out = []
    for e in GRAPH["edges"]:
        if e["verb"] == "touches" and e["source"] == "article:" + slug:
            out.append((nodes[e["target"]]["label"], e.get("matched", "")))
    return sorted(out)


# ------------------------------------------------------------------ index ---
def build_index():
    C = LICENCES["counts"]
    E = ANALYSIS["evidence"]
    stat = [
        (f'{CORPUS["count"]}', "op-eds, fetched and frozen on one day",
         f'{CORPUS["total_words"]:,} words held, none republished'),
        (f'{C["carrying_a_named_public_licence"]}', "carry a named public licence",
         "no Creative Commons, no version, no URL"),
        (f'{C["whose_ld_json_declares_a_licence"]} of {C["with_ld_json"]}',
         "declare the terms in their JSON-LD", "the structured data is already there"),
        (f'{E["with_no_outbound_link_at_all"]} of {E["articles"]}',
         "offer the reader no link at all", f'{E["total_links"]} links across the whole corpus'),
        (f'{E["distinct_domains"]}', "distinct domains cited between them",
         "exactly none reached by two pieces"),
        (f'{REGISTER["count"]}', "frozen files, each with its SHA-256",
         f'{len(REGISTER.get("excluded", []))} page we could not fetch at all'),
    ]
    proof = "".join(f'<div class="n"><b>{esc(a)}</b><span>{esc(b)}</span><em>{esc(c)}</em></div>'
                    for a, b, c in stat)
    cards = [
        ("The finding", "licences.html", "Under what licence, exactly?",
         "Twenty-one pieces, twenty-one prose permissions, two wordings, and no licence with a "
         "name. What the sentence actually permits, what it leaves open, and the one line of "
         "JSON that would fix it."),
        ("The corpus", "corpus.html", "The twenty-one",
         "Every piece: who wrote it, where they work, how long it is, what it links to, what "
         "it is about. Linked to the original, never reproduced."),
        ("The aggregate", "findings.html", "What they said together",
         "Twenty-one of the most powerful voices in news, asked the same question in the same "
         "week. What they all reached for, what only two mentioned, and what none of them "
         "gave their readers."),
        ("The graph", "graph.html", f'{GRAPH["counts"]["nodes"]} nodes, {GRAPH["counts"]["edges"]} edges',
         "The same corpus as a graph you can walk: articles, authors, organisations, themes, "
         "cited sources, licences and the frozen files underneath. Every verb has a named "
         "inverse and a Portuguese form."),
        ("The evidence", "sources.html", "Every file, every hash",
         f'{REGISTER["count"]} frozen files with their SHA-256, the dated snapshot they belong '
         "to, and the page that answered an automated reader with a redirect and no body."),
        ("The method", "method.html", "How this is built, and what it refuses",
         "Fetch, freeze, hash, extract, derive, gate. The published lexicon. The four things "
         "this section will not do, enforced by a program rather than a promise."),
    ]
    cardhtml = "".join(
        f'<a class="card" href="{h}"><span class="tag">{esc(t)}</span><h3>{esc(ttl)}</h3>'
        f'<p>{esc(p)}</p><span class="go">Open &rarr;</span></a>' for t, h, ttl, p in cards)

    body = f"""{masthead("index.html")}
<h1>Twenty-one op-eds, one permission, no licence</h1>
<p class="lead">For World News Day on 28 September 2026, WAN-IFRA and the Canadian Journalism
Foundation published twenty-one commissioned opinion pieces by editors, publishers and
directors from Manila to Managua, and made them <b>free to republish</b>. That is a generous
act, and an unusual one. This section takes it seriously enough to ask what it actually
amounts to for anyone &mdash; a newsroom, a translator, an archive, a machine &mdash; who
wants to act on it.</p>

<p>We fetched all twenty-one, froze the bytes, hashed them, and asked three questions.</p>

<div class="altitudes">
  <div class="alt"><div class="num">Question one</div><h3>Under what licence?</h3>
  <p>&ldquo;Free to republish&rdquo; is a permission. A licence is a permission with a name, a
  version and an address, so that a machine can find it and a lawyer can read it. Which of
  these is on the pieces?</p><a class="go" href="licences.html">The answer, in the bytes &rarr;</a></div>
  <div class="alt a2"><div class="num">Question two</div><h3>In what form?</h3>
  <p>Twenty thousand words of licensed material is a corpus. Is any of it published in a form
  a machine can consume &mdash; a licence field, a feed, a manifest, a graph?</p>
  <a class="go" href="licences.html#machine">What is already there &rarr;</a></div>
  <div class="alt a3"><div class="num">Question three</div><h3>What do they argue?</h3>
  <p>Twenty-one of the industry&rsquo;s most senior people answered the same question in the
  same week. Counted together, what did they reach for &mdash; and what did none of them
  say?</p><a class="go" href="findings.html">The aggregate &rarr;</a></div>
</div>

<div class="proof">{proof}</div>

{disclaimer()}

<h2 id="finding">The short version</h2>
<div class="claim">Every one of the twenty-one pieces grants permission to republish. Not one
of them grants it under a licence with a name. The permission exists only as a sentence at
the foot of the prose &mdash; in two slightly different wordings &mdash; and the announcement
that points to the pieces states the terms a third way, differently again.</div>

<p>That gap is not pedantry. A newsroom in S&atilde;o Paulo that wants to translate one of
these pieces has to read a sentence, interpret &ldquo;faithful to the original meaning&rdquo;,
and hope. An archive that wants to keep them has nothing to record in its rights field. A
machine that wants to know whether it may index, translate or train on them finds no
statement at all, because <b>every one of the twenty-one already ships structured data and not
one of them uses it to say this</b>. The generosity is real. The infrastructure for it is
missing, and it is one line of JSON long.</p>

<h2 id="start">Where to start</h2>
<div class="cards">{cardhtml}</div>

<h2 id="notours">Whose work this is</h2>
<p>The op-eds are not ours and are not reproduced here. They were commissioned by
<a href="https://worldnewsday.org/">World News Day</a>, a campaign run by
<a href="https://wan-ifra.org/">WAN-IFRA</a> with the Canadian Journalism Foundation, and every
one of them is a click away from <a href="corpus.html">the corpus page</a>. Read them there.
What this section adds is the layer underneath: the terms, the structure, the graph and the
evidence trail &mdash; the things this publication has argued for since its
<a href="../thesis/index.html">first page</a>, applied to somebody else&rsquo;s corpus rather
than our own.</p>

{agent_block(
    'Everything on this page is derived from four files you should fetch instead of parsing '
    'HTML: <code>data/corpus.json</code> (the twenty-one, described), '
    '<code>data/licences.json</code> (the terms, counted), <code>data/analysis.json</code> '
    '(the aggregate) and <code>data/graph.json</code> with <code>data/ontology.json</code> '
    '(the same thing as a typed graph, plus <code>data/triples.nt</code> as N-Triples). '
    '<code>data/register.json</code> maps every claim to a frozen file and its SHA-256. '
    '<b>The prose of the op-eds is deliberately not in any of them</b> — follow the '
    '<code>url</code> on each article to the publisher.')}
"""
    return write("index.html", page(
        "index.html", "World News Day 2026: the corpus",
        "Twenty-one commissioned op-eds, free to republish under no named licence. Fetched, "
        "frozen, hashed, described and graphed — and not republished.",
        body, '<a href="../index.html">newsroom.sgit.ai</a> / world news day'))


# --------------------------------------------------------------- licences ---
def build_licences():
    C = LICENCES["counts"]
    M = LICENCES["machine_readability"]
    T = LICENCES["the_two_statements"]
    rows = [
        ("Pieces in the corpus", C["articles"], ""),
        ("…carrying a prose permission to republish", C["carrying_a_prose_permission"],
         "a sentence at the foot of the article"),
        ("…distinct wordings of that sentence", C["distinct_prose_statements"],
         "20 pieces carry one, 1 piece carries the other"),
        ("…carrying a <b>named public licence</b>", C["carrying_a_named_public_licence"],
         "nothing with a name, a version and a URL"),
        ("…mentioning Creative Commons anywhere in the page", C["carrying_a_creative_commons_reference"], ""),
        ("…carrying <code>rel=&quot;license&quot;</code> on any link", C["carrying_rel_license"],
         "the HTML mechanism, unused"),
        ("…carrying a copyright notice naming a holder", C["carrying_a_copyright_notice"],
         "no © line, and no &ldquo;all rights reserved&rdquo; either"),
        ("…shipping schema.org JSON-LD", C["with_ld_json"],
         "already generated, on every page"),
        ("…whose JSON-LD declares the terms", C["whose_ld_json_declares_a_licence"],
         "the field exists; nothing is in it"),
    ]
    # A zero is the finding on every row it appears on, so it is coloured as one.
    count_rows = "".join(
        f'<tr><td>{lbl}</td><td style="font-family:var(--mono);font-size:1.05rem;'
        f'color:{"#b91c1c" if n == 0 else "#0f766e"}"><b>{n}</b></td>'
        f'<td class="small dim">{note}</td></tr>'
        for lbl, n, note in rows)

    variants = "".join(
        f'<div class="note" style="border-left-color:#b91c1c"><p style="margin-top:0">'
        f'<b>Wording {v["variant"]}</b> &mdash; on {v["articles"]} of the {C["articles"]} pieces</p>'
        f'<p style="margin-bottom:0;font-family:var(--serif);font-size:1.02rem">&ldquo;{esc(v["text"])}&rdquo;</p></div>'
        for v in LICENCES["the_statement"])

    does = "".join(f"<li>{esc(b)}</li>" for b in LICENCES["what_the_statement_does_and_does_not_do"])
    types = ", ".join(f"<code>{esc(t)}</code>" for t in M["json_ld_types_present"] if t)
    unused = ", ".join(f"<code>{esc(f)}</code>" for f in M["schema_org_fields_available_and_unused"])

    body = f"""{masthead("licences.html")}
<h1>The licence that is not there</h1>
<p class="lead">Every one of the twenty-one op-eds says you may republish it. Not one of them
says so under a licence. This page is the difference between those two sentences, counted in
the bytes.</p>

{disclaimer()}

<h2 id="what">What is actually on the pieces</h2>
<p>At the foot of every article, after the prose and before the author&rsquo;s role line,
there is one sentence. It is the only statement of terms anywhere on the page. It appears in
two wordings across the corpus, which differ in the occasion they name:</p>
{variants}
<p class="small dim">Quoted in full, twice, because this is the one text on which every other
claim on this page depends, and a reader cannot check our reading of it against anything
else. Both wordings are in the frozen bytes verbatim; <a href="method.html#gates">the gate</a>
fails the build if they stop matching.</p>

<h2 id="count">The count</h2>
<p>Each number below is derived from the frozen HTML by <code>build/graph.py</code> and then
derived again, by a different program with different patterns, in
<code>build/gates.py</code>. A number that only one program can produce is an assertion; a
number two programs produce from the same bytes is a finding.</p>
<div class="tablewrap"><table>
<thead><tr><th>Of the twenty-one</th><th>Count</th><th>Note</th></tr></thead>
<tbody>{count_rows}</tbody>
</table></div>

<h2 id="does">What that sentence does and does not do</h2>
<ul>{does}</ul>

<h2 id="two">Two statements, one corpus</h2>
<p>The same organisation states the terms twice, in two places, and the two do not say the
same thing.</p>
<div class="split"><table>
<thead><tr><th class="run">On each article</th><th class="rent">On the announcement page</th></tr></thead>
<tbody><tr>
<td>&ldquo;{esc(T["on_the_articles"])}&rdquo;</td>
<td>&ldquo;{esc(T["on_the_announcement"])}&rdquo;</td>
</tr>
<tr><td><b class="yes">Requires: in full.</b> Says nothing about credit.</td>
<td><b class="no">Requires: appropriate credit.</b> Says nothing about in full.</td></tr>
</tbody></table>
<p class="cap">A republisher who follows one is not following the other. Neither is wrong;
there simply is no single text that says what the terms are.</p></div>
<p class="small dim">The announcement page could not be fetched by an automated reader at all
&mdash; it answered with HTTP 307 and no body, from two user-agents, while rendering normally
for a browser. Its wording is recorded here as read by a person, and no other claim in this
section rests on it. <a href="sources.html#excluded">The full record of that refusal &rarr;</a></p>

<h2 id="machine">The machine-readable form that is nearly there</h2>
<p>This is the part that is genuinely frustrating, because almost all of the work is already
done.</p>
<p>Every one of the twenty-one pages already ships schema.org structured data as JSON-LD,
generated automatically by the site&rsquo;s SEO plugin. The types present across the corpus
are {types}. schema.org has carried a <code>license</code> property since 2015, alongside
{unused}. <b>{C["whose_ld_json_declares_a_licence"]} of {C["with_ld_json"]} use any of
them.</b></p>
<p>The record is being generated on every page already. Adding the terms to it is a line:</p>
<pre class="shell"><span class="d">// in the Article node that is already on every one of the 21 pages</span>
<span class="cy">"license"</span>: <span class="g">"https://creativecommons.org/licenses/by/4.0/"</span>,
<span class="cy">"copyrightHolder"</span>: {{ <span class="cy">"@type"</span>: <span class="g">"Organization"</span>, <span class="cy">"name"</span>: <span class="g">"World News Day"</span> }},
<span class="cy">"isAccessibleForFree"</span>: <span class="y">true</span></pre>
<p><b>And the structured data that is there is not reliable.</b> The REST record for each
piece carries an author field. On {M["structured_author_field_disagrees_with_the_printed_byline"]}
of the {C["articles"]} it does not name the people the page itself prints: one gives the CMS
account name <code>329976pwpadmin</code> instead of a person, and one names an author the
byline does not. A machine-readable field that is wrong twice in twenty-one is worse than no
field at all, because nothing on the page tells a reader which to believe. It is why the
bylines in <a href="corpus.html">the corpus</a> are read from the prose.</p>

<p>There is more that is nearly there. <code>worldnewsday.org</code> serves the entire corpus
as structured JSON at <code>/wp-json/wp/v2/posts</code> &mdash; every piece, with its title,
author field, dates, categories and full body, in a form any program can read. It is open,
undocumented and unadvertised: a machine-consumable edition exists <em>by accident of the
platform</em> rather than by a decision to publish one. It carries no licence field either.
And the taxonomy is a single category (<code>Story</code>) and a single tag
(<code>2026</code>) across all twenty-one, which is why the themes in
<a href="findings.html">the aggregate</a> had to be derived here rather than read from the
source.</p>

<h2 id="fix">What would close the gap</h2>
<ol>
<li><b>Name the licence.</b> &ldquo;Republish or translate in full, faithful to the original
meaning&rdquo; is close to <b>CC BY-ND 4.0</b> with a translation permission, and
&ldquo;with appropriate credit&rdquo; is <b>CC BY 4.0</b>. Either is a URL, a version and a
body of case law instead of a sentence to interpret. Publishing the wrong-shaped named
licence is still better than publishing none, and the licences are designed to be read by
the people this corpus is aimed at.</li>
<li><b>Put it in the JSON-LD.</b> One <code>license</code> line in a record that is already
generated makes twenty thousand words of deliberately open material discoverable, indexable
and usable as open material, by every machine that reads the page.</li>
<li><b>Say it once.</b> One canonical statement of the terms, linked from every piece and
from the announcement, instead of two wordings on the articles and a third on the page that
points to them.</li>
</ol>

<h2 id="notsaying">What this page is not saying</h2>
<p>It is not saying the permission is fake, grudging or unusable. It is the opposite of
those things: twenty-one commissioned pieces, given away, in a year when almost nobody in
this industry gives anything away. The generosity is the story. <b>The finding is about the
form, not the existence</b> &mdash; and the form is what decides whether the generosity
reaches a translator in Manila, a local paper in Ohio, an archive in Lisbon or a model that
will summarise all twenty-one for somebody who will never see the originals.</p>
<p>It is also not saying that this is unusual. It is completely usual. That is why it is
worth counting: the gap between &ldquo;we want this to spread&rdquo; and &ldquo;here is the
machine-readable statement that lets it spread&rdquo; is where most of the open content on
the internet currently falls, and closing it costs an afternoon.</p>

{agent_block(
    'Fetch <code>data/licences.json</code> rather than parsing this page: it carries the '
    'counts, both prose wordings, the seven-point reading of what the sentence does and does '
    'not do, the machine-readability finding and the two-statement comparison, as data. '
    'Every count in it is re-derived from the frozen HTML by <code>build/gates.py</code> '
    'before the build ships. <b>Do not treat this page as a licence</b> — it is a description '
    "of somebody else&rsquo;s terms, and the terms are on the articles themselves.")}
"""
    return write("licences.html", page(
        "licences.html", "The licence that is not there",
        "Twenty-one op-eds, all free to republish, none under a named licence: what the "
        "permission actually says, in two wordings, and the one line of JSON-LD that would "
        "make it machine-readable.",
        body, '<a href="../index.html">newsroom.sgit.ai</a> / '
              '<a href="index.html">world news day</a> / the licence'))


# ----------------------------------------------------------------- corpus ---
def build_corpus():
    org_of = {r["author"]: r["organisations"] for r in AFFILIATIONS["people"]}

    rows = []
    for a in sorted(CORPUS["articles"], key=lambda x: x["order_in_announcement"]):
        th = themes_of(a["slug"])
        src = SRC[a["source_page"]]
        def who(b):
            orgs = org_of.get(b, [])
            tail = (" &mdash; " + ", ".join(esc(o) for o in orgs)) if orgs else \
                   ' <span style="font-style:italic">&mdash; no current organisation in the role line</span>'
            return f'{esc(b)}<span class="dim small">{tail}</span>'

        authors = " &middot; ".join(who(b) for b in a["byline"])
        links = (f'<b>{len(a["outbound_links"])}</b> &rarr; '
                 + ", ".join(f"<code>{esc(re.sub(r'^www.', '', d))}</code>" for d in sorted({re.sub(r"^www\.", "", x) for x in a["outbound_domains"]}))
                 ) if a["outbound_links"] else '<b style="color:#b91c1c">0</b> <span class="dim">— none</span>'
        rows.append(
            f'<tr id="{esc(a["slug"])}">'
            f'<td style="font-family:var(--mono);color:var(--dim2)">{a["order_in_announcement"]}</td>'
            f'<td><a href="{esc(a["url"])}"><b>{esc(a["title"])}</b></a>'
            f'<div class="small" style="margin-top:.25rem">{authors}</div></td>'
            f'<td class="small" style="white-space:nowrap">{esc(a["published"][:10])}<br>'
            f'<span class="dim">{a["words"]:,} words</span></td>'
            f'<td class="small">{links}</td>'
            f'<td class="small">{", ".join(esc(t) for t, _ in th)}</td>'
            f'<td class="small" style="white-space:nowrap">'
            f'<a href="{esc(a["source_page"].replace(LATEST + "/", "sources/frozen/" + LATEST + "/"))}">page</a> &middot; '
            f'<a href="{esc(a["source_api"].replace(LATEST + "/", "sources/frozen/" + LATEST + "/"))}">json</a><br>'
            f'<code class="dim" style="font-size:.65rem">{esc(src["sha256"][:12])}…</code></td>'
            f"</tr>")

    body = f"""{masthead("corpus.html")}
<h1>The twenty-one</h1>
<p class="lead">In the order the announcement lists them &mdash; that order is itself data, so
it survives the extractor. Each title links to the piece on <code>worldnewsday.org</code>, and
the last column links to the exact bytes we hold for it. <b>The prose is not here.</b> Read
them at the publisher; this is the description.</p>

{disclaimer()}

<div class="tablewrap"><table>
<thead><tr><th>#</th><th>Piece, and who wrote it</th><th>Published</th>
<th>Links it offers</th><th>Themes, derived</th><th>Frozen</th></tr></thead>
<tbody>{"".join(rows)}</tbody>
</table></div>

<p class="small dim">The organisation shown after each name is taken from the role line the
piece itself prints under the byline, never looked up anywhere else, and
<a href="method.html#transcription">transcribed by hand rather than derived</a> &mdash; a
regular expression over that prose had an author working at &ldquo;Philippines&rdquo;. Two of
the twenty-three role lines name only former posts, and those say so rather than guessing. The themes are the
published lexicon in <a href="method.html#lexicon"><code>data/lexicon.json</code></a> run over
the article&rsquo;s own prose: a theme means the piece contains those words, and nothing more
than that. The links column counts <code>&lt;a&gt;</code> tags in the article body &mdash; the
evidence the piece offers its own reader &mdash; and nothing was fetched from them.</p>

<h2 id="shape">The shape of it</h2>
<div class="proof">
<div class="n"><b>{ANALYSIS["shape"]["total_words"]:,}</b><span>words in the corpus</span>
<em>{ANALYSIS["shape"]["shortest"]}–{ANALYSIS["shape"]["longest"]} per piece</em></div>
<div class="n"><b>{ANALYSIS["people"]["named_authors"]}</b><span>named authors</span>
<em>{ANALYSIS["people"]["pieces_with_more_than_one_byline"]} pieces have more than one byline</em></div>
<div class="n"><b>{ANALYSIS["people"]["organisations_named_in_role_lines"]}</b><span>organisations named in role lines</span>
<em>broadcasters, wires, dailies, NGOs, regulators</em></div>
<div class="n"><b>{ANALYSIS["shape"]["published_between"][0]} → {ANALYSIS["shape"]["published_between"][1]}</b>
<span>published across three days</span><em>for World News Day, 28 September</em></div>
</div>

{agent_block(
    'The machine surface for this table is <code>data/corpus.json</code>: one record per piece '
    'with its order in the announcement, slug, canonical URL, publication and modification '
    'dates, word count, byline as a list, the role line as printed, the permission statement '
    'verbatim, categories, tags, every outbound link, the schema.org types present, and the '
    'two frozen files it was built from. <b>The article body is deliberately absent.</b> '
    'Follow <code>url</code> to the publisher, who owns it and who has asked to be credited.')}
"""
    return write("corpus.html", page(
        "corpus.html", "The twenty-one",
        "Every World News Day 2026 op-ed described: author, organisation, length, the links it "
        "offers its reader, the themes it touches, and the SHA-256 of the bytes we hold.",
        body, '<a href="../index.html">newsroom.sgit.ai</a> / '
              '<a href="index.html">world news day</a> / the twenty-one'))


# --------------------------------------------------------------- findings ---
def build_findings():
    E = ANALYSIS["evidence"]
    S = ANALYSIS["shape"]
    P = ANALYSIS["people"]
    top = ANALYSIS["themes"][0]["articles"] or 1
    theme_rows = "".join(
        f'<tr><td>{esc(t["label"])}</td>'
        f'<td style="width:42%"><span style="display:inline-block;height:.62rem;border-radius:3px;'
        f'background:{"#b91c1c" if t["articles"] <= 3 else "#0f766e"};'
        f'width:{max(2, round(100 * t["articles"] / top))}%"></span></td>'
        f'<td style="font-family:var(--mono);white-space:nowrap">{t["articles"]} of {CORPUS["count"]}</td>'
        f'<td class="small dim"><code>{esc(next(e["pattern"] for e in LEXICON["entries"] if e["id"] == t["id"])[:58])}</code></td></tr>'
        for t in ANALYSIS["themes"])

    together = "".join(f'<li>{esc(p["a"])} <span class="dim">+</span> {esc(p["b"])} '
                       f'<span class="dim small">&mdash; {p["articles"]} pieces</span></li>'
                       for p in ANALYSIS["themes_together"][:8])
    apart = "".join(f'<li>{esc(p["a"])} <span class="dim">+</span> {esc(p["b"])}</li>'
                    for p in ANALYSIS["themes_never_together"])

    link_rows = "".join(
        f'<tr><td class="small"><a href="corpus.html#{esc(r["slug"])}">{esc(r["title"])}</a></td>'
        f'<td style="font-family:var(--mono);color:{"#b91c1c" if r["links"] == 0 else "#0f766e"}">'
        f'<b>{r["links"]}</b></td>'
        f'<td class="small dim">{", ".join(f"<code>{esc(d)}</code>" for d in r["domains"]) or "—"}</td></tr>'
        for r in E["per_article"])

    orgs = ", ".join(esc(o) for o in P["organisations"])
    refuses = "".join(f"<li>{esc(r)}</li>" for r in ANALYSIS["refuses"])

    # The mapping the section exists to make. Each row is their sentence and our page — and
    # the point of the table is that the argument is shared and the infrastructure is not.
    MAP = [
        ("Trust is the industry’s core asset and it is eroding.",
         f'{ANALYSIS["themes"][2]["articles"]} of {CORPUS["count"]} pieces reach for trust and credibility.',
         "Trust is not a brand. It is a walkable chain from a claim to the evidence under it.",
         "../thesis/index.html", "The thesis: sell the graph"),
        ("Misinformation spreads faster than corrections.",
         f'{next(t["articles"] for t in ANALYSIS["themes"] if t["id"] == "misinformation")} of {CORPUS["count"]} pieces say so.',
         "A correction that does not reach what it disproved is not a correction. This is the "
         "one mechanism nobody in the corpus proposes.",
         "../corrections/index.html", "Corrections must propagate"),
        ("AI is taking journalism’s work without paying for it.",
         f'{next(t["articles"] for t in ANALYSIS["themes"] if t["id"] == "ai")} of {CORPUS["count"]} pieces raise AI; '
         f'{next(t["articles"] for t in ANALYSIS["themes"] if t["id"] == "copyright")} mention copyright or licensing.',
         "You cannot be paid for a fact whose provenance nobody can check, and you cannot "
         "license what you have not made machine-readable.",
         "../economics/index.html", "Paying the fact creator"),
        ("Readers cannot tell what is true.",
         f'{ANALYSIS["themes"][0]["articles"]} of {CORPUS["count"]} pieces are about truth and facts.',
         "Provenance is the product: the chain, not the byline, is what a reader checks.",
         "../provenance/index.html", "Provenance is the product"),
        ("Journalism needs a sustainable business model.",
         f'{next(t["articles"] for t in ANALYSIS["themes"] if t["id"] == "business-model")} of {CORPUS["count"]} pieces.',
         "The unit that can be sold is the verified fact and its chain, not the page view or "
         "the paywalled article.",
         "https://sgit.ai/", "sgit.ai — the story vault, not the paywall"),
        ("The industry must work together across borders.",
         f'{next(t["articles"] for t in ANALYSIS["themes"] if t["id"] == "collaboration")} of {CORPUS["count"]} pieces.',
         "Collaboration between newsrooms needs a shared, checkable substrate. This section is "
         "one: a corpus somebody else published, described so anyone can build on it.",
         "../network/index.html", "The network: sibling boundaries"),
    ]
    map_rows = "".join(
        f'<tr><td><b>{esc(a)}</b><div class="small dim" style="margin-top:.2rem">{esc(b)}</div></td>'
        f'<td>{esc(c)}<div style="margin-top:.35rem"><a class="small" href="{esc(h)}">{esc(l)} &rarr;</a></div></td></tr>'
        for a, b, c, h, l in MAP)

    body = f"""{masthead("findings.html")}
<h1>What twenty-one editors said, counted</h1>
<p class="lead">Twenty-one of the most senior people in news were asked the same question in
the same week and answered it in public. Read one at a time these are opinion pieces. Counted
together they are a picture of what this industry currently believes is worth saying &mdash;
and, more usefully, of what it does not say.</p>

{disclaimer()}

<div class="note"><p style="margin-top:0"><b>What a count here is, and is not.</b></p>
<ul style="margin-bottom:0">{refuses}</ul></div>

<h2 id="themes">What they reach for</h2>
<p>Twenty published patterns, run over each article&rsquo;s own prose. A theme means the
piece contains those words. It does not mean the author cares about the subject, and its
absence does not mean they do not &mdash; a nine-hundred-word piece has room for four ideas.
The patterns are <a href="method.html#lexicon">published in full</a> so you can disagree with
them precisely.</p>
<div class="tablewrap"><table>
<thead><tr><th>Theme</th><th>Share of the corpus</th><th>Count</th><th>Pattern</th></tr></thead>
<tbody>{theme_rows}</tbody>
</table></div>

<div class="claim">In a corpus where {next(t["articles"] for t in ANALYSIS["themes"] if t["id"] == "ai")} of
{CORPUS["count"]} pieces raise artificial intelligence, and where the word
&ldquo;scraping&rdquo; sits under most of the anxiety,
{next(t["articles"] for t in ANALYSIS["themes"] if t["id"] == "copyright")} mention copyright
or licensing at all. The pieces are themselves published without a licence.</div>

<h3>Reached for together</h3>
<ul>{together}</ul>
<h3>Never in the same piece</h3>
<p class="small dim">Of the pairs where both themes appear somewhere in the corpus, these
never appear in the same article:</p>
<ul>{apart}</ul>

<h2 id="evidence">What they give the reader</h2>
<p>This is the count this publication exists to make, and here it is over the people making
the case for trusting journalism, in the week they made it.</p>
<div class="proof">
<div class="n"><b>{E["with_no_outbound_link_at_all"]} of {E["articles"]}</b>
<span>offer the reader no link at all</span><em>not one anchor in the article body</em></div>
<div class="n"><b>{E["total_links"]}</b><span>links across the whole corpus</span>
<em>median per piece: {E["median_links_per_article"]}</em></div>
<div class="n"><b>{E["most_links_in_one_piece"]}</b><span>in the single most-linked piece</span>
<em>more than a third of the corpus total</em></div>
<div class="n"><b>{E["distinct_domains"]}</b><span>distinct domains cited between them</span>
<em>{len(E["domains_reached_by_more_than_one_piece"])} of them reached by two pieces</em></div>
</div>
<p>Twenty-three domains, and <b>no two of the twenty-one pieces point at the same one</b>.
At the level of the institution rather than the hostname there is exactly one overlap:
{", ".join(f"<code>{esc(d)}</code>" for d in E["institutions_reached_by_more_than_one_piece"]) or "none"}.
There is no shared evidence base here. Twenty-one arguments about why the public should trust
journalism, and the reader is asked to take almost all of it on the author&rsquo;s word.</p>
<p class="small dim">That is not an accusation, and it is not unusual: an 800-word commissioned
op-ed is not a piece of investigative reporting and nobody promised footnotes. It is the
ordinary form, which is the point &mdash; <a href="../thesis/index.html">this site&rsquo;s
first page</a> has argued since 2025 that the ordinary form gives a reader nothing to walk.
Here is the measurement, on the best-resourced writers in the industry.</p>
<details><summary class="small">Every piece, by the number of links it offers</summary>
<div class="tablewrap"><table>
<thead><tr><th>Piece</th><th>Links</th><th>Where to</th></tr></thead>
<tbody>{link_rows}</tbody></table></div></details>

<h2 id="who">Who is speaking</h2>
<p>{P["named_authors"]} named authors across {P["articles"]} pieces
({P["pieces_with_more_than_one_byline"]} carry more than one byline), at
{P["organisations_named_in_role_lines"]} organisations as their own role lines name them:</p>
<p class="small">{orgs}.</p>

<h2 id="maps">How this maps to what we have published</h2>
<p>The striking thing about reading twenty-one of these at once is not disagreement. It is
that the diagnosis is shared, precisely, across continents and business models &mdash; and
that almost nobody proposes a mechanism. The corpus says <em>trust is eroding, truth is
contested, AI is taking the work, the model is broken</em>. It is a diagnosis this publication
has been making since its first page. The difference is what comes next.</p>
<div class="tablewrap"><table>
<thead><tr><th>What the corpus says</th><th>What we have argued, and where</th></tr></thead>
<tbody>{map_rows}</tbody>
</table></div>
<div class="claim">Nobody in the corpus proposes a mechanism by which a correction reaches
what it disproved, a fact carries its provenance, or the person who did the original work
gets paid when a machine uses it. The pieces are the argument for why journalism matters.
The missing half is the infrastructure that would let a machine act on it &mdash; and the
twenty-one pieces are themselves a worked example of the gap, published without a licence
a machine can read.</div>

{agent_block(
    'Fetch <code>data/analysis.json</code>: theme frequencies with the pattern that produced '
    'each one, co-occurrence pairs, the per-article link counts and the cited-domain overlap, '
    'plus the explicit list of what this analysis refuses to infer. Cross-reference '
    '<code>data/graph.json</code> for the same facts as typed edges. Every count is re-derived '
    'from frozen bytes by <code>build/gates.py</code>. <b>No sentiment, stance or agreement is '
    'modelled anywhere in this section</b>, and <code>agrees_with</code> is a banned verb in '
    'the ontology — if you need those, derive them yourself and say that you did.')}
"""
    return write("findings.html", page(
        "findings.html", "The aggregate",
        "Twenty-one World News Day op-eds counted together: what they all reach for, what only "
        "two mention, how many give the reader no link at all, and how the diagnosis maps to "
        "what this publication has argued.",
        body, '<a href="../index.html">newsroom.sgit.ai</a> / '
              '<a href="index.html">world news day</a> / the aggregate'))


# ------------------------------------------------------------------ graph ---
def build_graph_page():
    packs = "".join(
        f'<label><input type="checkbox" name="pack-{esc(p["id"])}"{" checked" if p["default"] else ""}> '
        f'<b>{esc(p["label"])}</b> <span class="small dim">({p["nodes"]})</span></label>'
        for p in GRAPH["packs"])
    types = "".join(
        f'<label><input type="checkbox" name="type-{esc(t["id"])}" checked>'
        f'<span class="swatch" style="background:{esc(t["colour"])}"></span>{esc(t["label"])} '
        f'<span class="small dim">&middot; {esc(t["pt"])} &middot; {GRAPH["counts"]["by_type"].get(t["id"], 0)}</span></label>'
        for t in ONTOLOGY["node_types"])
    verb_count = {}
    for e in GRAPH["edges"]:
        verb_count[e["verb"]] = verb_count.get(e["verb"], 0) + 1
    all_verbs = sorted({e["verb"] for e in ONTOLOGY["edges"]})
    # attested_by is off by default for the same reason as in /portugal/: every node carries
    # its source in the detail pane already, and 42 spokes into one snapshot hide the corpus.
    OFF = {"attested_by", "captured_in"}
    verbs_ctl = "".join(
        f'<label><input type="checkbox" name="verb-{esc(v)}"{"" if v in OFF else " checked"}> '
        f'<code>{esc(v)}</code> <span class="small dim">{verb_count.get(v, 0)}</span></label>'
        for v in all_verbs)
    verbopts = "".join(f'<option value="{esc(v)}">{esc(v)}</option>' for v in all_verbs)
    typeopts = "".join(f'<option value="type:{esc(t["id"])}">{esc(t["label"].lower())}</option>'
                       for t in ONTOLOGY["node_types"])

    def step(i, first):
        stop = '<option value="stop">— stop here —</option>'
        return (f'<div class="gqrow"><span class="gqn">{i}</span>'
                f'<select name="q-verb{i}">{"" if first else stop}<option value="any">any edge</option>{verbopts}{stop if first else ""}</select>'
                f'<select name="q-dir{i}"><option value="out">forwards</option><option value="in">backwards</option><option value="any">either way</option></select>'
                f'<select name="q-node{i}"><option value="any">anything</option>{typeopts}</select></div>')

    erows = "".join(
        f'<tr><td><code>{esc(e["verb"])}</code><br><span class="dim small">{esc(e["pt"]["verb"])}</span></td>'
        f'<td><code>{esc(e["inverse"])}</code><br><span class="dim small">{esc(e["pt"]["inverse"])}</span></td>'
        f'<td class="small">{esc(e["domain"])} &rarr; {esc(e["range"])}</td>'
        f'<td class="small">{esc(e["reads"].replace("{s}", "A").replace("{t}", "B"))}</td>'
        f'<td style="font-family:var(--mono);font-size:.8rem">{verb_count.get(e["verb"], 0)}</td></tr>'
        for e in ONTOLOGY["edges"])
    brows = "".join(f'<tr><td><code>{esc(b["verb"])}</code></td><td class="small">{esc(b["why"])}</td></tr>'
                    for b in ONTOLOGY["banned"])
    trows = "".join(
        f'<tr><td><span class="swatch" style="background:{esc(t["colour"])}"></span>'
        f'<b>{esc(t["label"])}</b> <span class="dim small">&middot; {esc(t["pt"])}</span></td>'
        f'<td class="small">{esc(t["definition"])}</td>'
        f'<td style="font-family:var(--mono);font-size:.8rem">{GRAPH["counts"]["by_type"].get(t["id"], 0)}</td></tr>'
        for t in ONTOLOGY["node_types"])
    presets = [
        ("The corpus: articles, authors, organisations", {"packs": ["articles", "people"]}),
        ("What they are about", {"packs": ["articles", "themes"]}),
        ("What they cite", {"packs": ["articles", "cited"]}),
        ("The terms every piece is published under", {"packs": ["articles", "terms"]}),
        ("The evidence underneath", {"packs": ["articles", "evidence"]}),
        ("Organisations whose author wrote about AI",
         {"packs": ["articles", "people", "themes"], "start": "type:Organisation",
          "steps": [{"verb": "affiliated_to", "dir": "in", "node": "type:Author"},
                    {"verb": "wrote", "dir": "out", "node": "type:Article"},
                    {"verb": "touches", "dir": "out", "node": "Artificial intelligence"}]}),
        ("Everything", {"packs": [p["id"] for p in GRAPH["packs"]]}),
    ]
    preset_html = "".join(
        f'<a href="#" class="altib" data-preset=\'{json.dumps(pre)}\'>{esc(label)}</a>'
        for label, pre in presets)

    body = f"""{masthead("graph.html")}
<h1>The graph</h1>
<p class="lead">{GRAPH["counts"]["nodes"]} nodes, {GRAPH["counts"]["edges"]} edges, twenty-one
op-eds. <b>Start with the articles and their authors, and switch the other blocks on one at a
time.</b> Click a node to open it, double-click to centre on it, shift-click two to read the
path between them as a sentence &mdash; in English or in Portuguese. Machine surfaces:
<a href="data/graph.json">graph.json</a> &middot;
<a href="data/ontology.json">ontology.json</a> &middot;
<a href="data/triples.nt">triples.nt</a>.</p>

{disclaimer()}

<div class="note"><p style="margin-top:0"><b>Why a graph at all.</b> Twenty-one articles in a
list are twenty-one articles. The same twenty-one with their authors, the organisations those
authors name, the themes their prose contains, the sources they point at and the terms they
are published under is a thing you can ask questions of: <em>which organisations have someone
writing about AI</em>, <em>which pieces cite nothing</em>, <em>which themes never occur
together</em>. None of that is in the publisher&rsquo;s own data, because the publisher&rsquo;s
own data is a single category called <code>Story</code>.</p>
<p style="margin-bottom:0"><b>The instrument is borrowed, on purpose.</b> This is the same
engine and control panel as <a href="../portugal/graph.html">/portugal/</a> and
<a href="https://graphs.sgit.ai/v1/altitudes/graph.html">graphs.sgit.ai</a> &mdash; packs
instead of levels, otherwise the same thing. A reader who has used one should not have to
learn another.</p></div>

<div class="gwrap">
  <form id="gcfg" class="gcfg">
    <fieldset><legend>Find</legend>
      <input type="search" name="search" placeholder="title, author, organisation&hellip;" aria-label="Filter nodes">
    </fieldset>
    <fieldset><legend>Packs &middot; blocks of nodes</legend>{packs}
      <p class="small dim">Switch a block on and its nodes and edges join the graph.</p></fieldset>
    <fieldset><legend>Types</legend>{types}</fieldset>
    <fieldset><legend>Edges</legend>{verbs_ctl}
      <p class="small dim"><code>attested_by</code> and <code>captured_in</code> are off by
      default: every node names its frozen source in the detail pane anyway, and 42 spokes
      into one snapshot hide the corpus.</p></fieldset>
    <fieldset><legend>Colour by</legend>
      <label><input type="radio" name="colour" value="type" checked> what kind of node</label>
      <label><input type="radio" name="colour" value="pack"> which pack</label>
      <label><input type="radio" name="colour" value="class"> taxonomy class</label>
    </fieldset>
    <fieldset><legend>Labels</legend>
      <label><input type="radio" name="labels" value="inside"> inside the node</label>
      <label><input type="radio" name="labels" value="below" checked> below the node</label>
      <label><input type="radio" name="labels" value="none"> none</label>
      <label class="grange">wrap at <output id="out-wrap">18</output> chars
        <input type="range" name="wrap" min="10" max="46" step="2" value="18"></label>
      <label class="grange">cut at <output id="out-maxlen">30</output> chars
        <input type="range" name="maxlen" min="12" max="90" step="2" value="30"></label>
      <label><input type="radio" name="edgeLabels" value="none" checked> no edge labels</label>
      <label><input type="radio" name="edgeLabels" value="verb"> name the edges</label>
      <label><input type="radio" name="lang" value="en" checked> verbs in English</label>
      <label><input type="radio" name="lang" value="pt"> verbos em portugu&ecirc;s</label>
    </fieldset>
    <fieldset><legend>Size by</legend>
      <label><input type="radio" name="size" value="degree" checked> how connected</label>
      <label><input type="radio" name="size" value="fixed"> uniform</label>
    </fieldset>
    <fieldset><legend>Layout</legend>
      <label><input type="radio" name="layout" value="force" checked> force</label>
      <label><input type="radio" name="layout" value="bands"> bands, by taxonomy class</label>
      <label><input type="radio" name="layout" value="concentric"> concentric</label>
      <label><input type="radio" name="layout" value="grid"> grid</label>
      <label class="grange">iterations <output id="out-iterations">2000</output>
        <input type="range" name="iterations" min="300" max="12000" step="300" value="2000"></label>
      <label><input type="checkbox" name="stabilise"> cool slowly (settles further)</label>
      <button type="button" id="grelayout">Re-run layout</button>
      <button type="button" id="gstable">Run until settled</button>
    </fieldset>
    <fieldset><legend>Explore from one place</legend>
      <label class="grange">radius <output id="out-radius">0</output> hops
        <input type="range" name="radius" min="0" max="4" step="1" value="0"></label>
      <p class="small dim">0 shows everything. Above 0, only what is within that many hops of the centred node.</p>
      <button type="button" id="gcollapse">Collapse selection</button>
      <button type="button" id="gexpandall">Expand all groups</button>
    </fieldset>
    <fieldset><legend>Keep this view</legend>
      <button type="button" id="gpng">Save PNG</button>
      <button type="button" id="gsave">Save view (.json)</button>
      <button type="button" id="gload">Load view</button>
      <input type="file" id="gfile" accept="application/json" hidden>
    </fieldset>
    <fieldset><legend>Screen</legend>
      <button type="button" id="gwide">Hide the panels</button>
      <button type="button" id="gfull">Full screen</button>
      <button type="button" id="gfit">Fit to screen</button>
      <button type="button" id="greset">Clear</button>
      <p class="small dim" id="gstats"></p>
    </fieldset>
  </form>
  <div class="gmid">
    <div id="cy"></div>
    <div class="gresize-v" data-gresize="v" title="Drag to make the graph taller"></div>
  </div>
  <div class="gresize-h" data-gresize="h" title="Drag to resize the panel"></div>
  <aside id="gdetail" class="gdetail"></aside>
</div>
<p class="small dim" id="gnote"></p>
<p class="small dim" id="ginventory"></p>

<h2 id="presets">Start here</h2>
<p class="small">Each button sets the packs and, where it makes sense, runs a query.</p>
<p>{preset_html}</p>

<h2 id="query">Query the paths</h2>
<p>Tracing answers <em>how do these two connect?</em> This answers <b>show me every route
shaped like this</b>: a start filter, then up to three edge-and-node steps, walked
breadth-first with a bound &mdash; and it says when it hit the bound, because a query that
silently truncates is worse than one that refuses.</p>
<form id="gq" class="gq">
  <div class="gqrow"><label>Start at
    <select name="q-start">{typeopts}<option value="any">anything</option></select></label></div>
  {step(1, True)}{step(2, False)}{step(3, False)}
  <div class="gqrow"><button type="button" id="gqrun" class="altib">Run the query</button></div>
</form>
<div id="gqout" class="gqout"></div>

<h2 id="types">The types</h2>
<div class="tablewrap"><table>
<thead><tr><th>Type</th><th>What a node of this type is</th><th>Count</th></tr></thead>
<tbody>{trows}</tbody></table></div>

<h2 id="vocabulary">The vocabulary</h2>
<p>Every edge is a verb with a distinct, named inverse, and every verb carries its Portuguese.
Walked forwards a path uses the verb; walked backwards it uses the inverse; either way it is a
sentence. Inherited from <a href="https://graphs.sgit.ai/">graphs.sgit.ai</a>&rsquo;s edge grammar
&mdash; {esc(ONTOLOGY["inherits_from"]["what"])}, and shared with <a href="../portugal/graph.html">/portugal/</a> so the two
sections can be read by the same reader and, eventually, joined.</p>
<div class="tablewrap"><table>
  <thead><tr><th>Verb</th><th>Inverse</th><th>Domain &rarr; range</th><th>Reads as</th><th>In use</th></tr></thead>
  <tbody>{erows}</tbody>
</table></div>
<h3>Banned</h3>
<p>A verb that is banned is banned in the code, not in a style guide: the gate fails the build
if one appears. <code>agrees_with</code> is this section&rsquo;s own addition, and the reason
is on the right.</p>
<div class="tablewrap"><table><thead><tr><th>Verb</th><th>Why</th></tr></thead><tbody>{brows}</tbody></table></div>
<h3>The one formula</h3>
<p>{esc(ONTOLOGY["formulas"][0]["note"])} The {ONTOLOGY["formulas"][0]["entries"]} patterns are
<a href="method.html#lexicon">published in full</a>.</p>

{agent_block(
    'Fetch <code>data/graph.json</code> and <code>data/ontology.json</code> rather than parsing '
    'this page; <code>data/triples.nt</code> is the same graph as N-Triples with '
    '<code>owl:inverseOf</code> on every verb and <code>@en</code>/<code>@pt</code> labels. '
    'Every node names the frozen file it came from. <b>This page also publishes an API</b>: '
    'after the <code>tool:ready</code> event, <code>window.__graph</code> exposes read methods '
    '(<code>get_graph</code>, <code>get_nodes</code>, <code>get_node</code>, '
    '<code>get_edges</code>, <code>get_ontology</code>, <code>search</code>) and view methods '
    '(<code>set_packs</code>, <code>explore</code>, <code>select_node</code>, '
    '<code>set_layout</code>, <code>set_language</code>, <code>fit_graph</code>, '
    '<code>graph_snapshot</code>, <code>reset_view</code>). Nothing writes.')}

{GRAPH_CSS}
<script src="../assets/vendor/cytoscape.min.js"></script>
<script src="../assets/portugal-graph.js" defer></script>
"""
    return write("graph.html", page(
        "graph.html", "The graph",
        f'{GRAPH["counts"]["nodes"]} nodes and {GRAPH["counts"]["edges"]} typed edges: '
        "twenty-one op-eds, their authors, organisations, themes, cited sources, licence terms "
        "and the frozen files underneath.",
        body, '<a href="../index.html">newsroom.sgit.ai</a> / '
              '<a href="index.html">world news day</a> / the graph'))


# ---------------------------------------------------------------- sources ---
def build_sources():
    by_slug = art_by_slug()
    rows = []
    for s in REGISTER["sources"]:
        a = by_slug.get(s["slug"])
        rows.append(
            f'<tr><td class="small"><a href="{esc(s["frozen"])}"><code>{esc(s["id"])}</code></a></td>'
            f'<td class="small">{esc(s["kind"])}</td>'
            f'<td class="small">{esc(a["title"]) if a else "&mdash;"}</td>'
            f'<td class="small" style="white-space:nowrap">{s["bytes"]:,} B</td>'
            f'<td class="small"><code style="font-size:.68rem">{esc(s["sha256"])}</code></td>'
            f'<td class="small"><a href="{esc(s["url"])}">original</a></td></tr>')
    excluded = "".join(
        f'<div class="note" style="border-left-color:#b91c1c"><p style="margin-top:0">'
        f'<b>{esc(x["id"])}</b> &mdash; <a href="{esc(x["url"])}">{esc(x["url"])}</a></p>'
        f'<p style="margin-bottom:0">{esc(x["why"])}</p></div>'
        for x in REGISTER.get("excluded", []))
    WHAT = {
        "data/register.json": "every frozen file, its URL, retrieval time, size and SHA-256, "
                              "plus what could not be fetched and why",
        "data/corpus.json": "the twenty-one described: order, byline, role line, dates, words, "
                            "terms, links, schema types — and no article prose",
        "data/licences.json": "the licence finding: the counts, both wordings, and the "
                              "two-statement comparison",
        "data/analysis.json": "the aggregate: theme frequencies, co-occurrence, the link counts",
        "data/lexicon.json": "the twenty published theme patterns — the only classification here",
        "data/affiliations.json": "where each author works, transcribed by hand from the role "
                                  "line their own piece prints, and checked against it",
        "data/ontology.json": "the types, the verbs with their inverses and Portuguese forms, "
                              "and the banned verbs",
        "data/graph.json": "the graph itself: nodes, edges and packs",
        "data/triples.nt": "the same graph as N-Triples, with owl:inverseOf on every verb",
        "data/manifest.json": "every file in this section with its hash",
    }
    dat = "".join(
        f'<tr><td><a href="{esc(f["path"])}"><code>{esc(f["path"])}</code></a></td>'
        f'<td class="small dim">{esc(WHAT.get(f["path"], ""))}</td>'
        f'<td class="small" style="white-space:nowrap">{f.get("bytes", 0):,} B</td></tr>'
        for f in MANIFEST["files"] if f["path"].startswith("data/"))

    body = f"""{masthead("sources.html")}
<h1>Sources</h1>
<p class="lead">{REGISTER["count"]} files, fetched once on {esc(LATEST)}, frozen to bytes in
this repository and hashed with SHA-256. Every number anywhere in this section walks back to
one of these rows. The build re-verifies every hash before it ships, so a frozen copy cannot
be edited without the build failing.</p>

{disclaimer()}

<h2 id="why">Why bytes, and not a link</h2>
<p>A link is a promise about the future. The page it points at can be edited, paywalled,
redirected or deleted, and when it is, every claim resting on it quietly becomes
unverifiable &mdash; usually without anyone noticing. So this section does not read
<code>worldnewsday.org</code> at publish time. It read it once, kept the bytes, and publishes
against those. The snapshot is dated; a later one would be a new dated folder beside it, and
the difference between them would itself be a story.</p>
<p>Two files are held for each piece: the page as served, and the record the site&rsquo;s own
REST API returns for it. The second is the more interesting one, and the reason
<a href="licences.html#machine">the machine-readability finding</a> is as sharp as it is.</p>

<h2 id="excluded">The page we could not read</h2>
{excluded}
<p class="small dim">This is recorded rather than tidied away because it is a finding in its
own right. The announcement that grants the permission, points at the twenty-one pieces and
states the terms a third way is the one page in this beat that an automated reader cannot
reach. Everything in this section that touches its wording says so on the page.</p>

<h2 id="register">The register</h2>
<div class="tablewrap"><table>
<thead><tr><th>Frozen file</th><th>Kind</th><th>Piece</th><th>Size</th><th>SHA-256</th><th>Live</th></tr></thead>
<tbody>{"".join(rows)}</tbody>
</table></div>

<h2 id="data">What this section publishes</h2>
<p>The derived files, all of them plain JSON beside the pages, all of them re-derivable from
the frozen bytes by running <code>build/build.py</code> with no network:</p>
<div class="tablewrap"><table>
<thead><tr><th>File</th><th>What it is</th><th>Size</th></tr></thead>
<tbody>{dat}</tbody>
</table></div>

{agent_block(
    '<code>data/register.json</code> is the index: every frozen file with its URL, retrieval '
    'time, byte count and SHA-256, plus an <code>excluded</code> array recording what could '
    'not be fetched and why. <code>data/manifest.json</code> lists every file this section '
    'publishes with its hash. Both are stable surfaces — build a mirror against them. The '
    'frozen copies carry a <code>.snapshot</code> extension so that third-party bytes held as '
    'evidence are never served or indexed as pages of this site.')}
"""
    return write("sources.html", page(
        "sources.html", "Sources",
        f'{REGISTER["count"]} frozen files with their SHA-256 hashes, the dated snapshot they '
        "belong to, and the one page that refused an automated reader.",
        body, '<a href="../index.html">newsroom.sgit.ai</a> / '
              '<a href="index.html">world news day</a> / sources'))


# ----------------------------------------------------------------- method ---
def build_method():
    lex = "".join(
        f'<tr><td><b>{esc(e["label"])}</b><br><code class="dim small">{esc(e["id"])}</code></td>'
        f'<td class="small"><code>{esc(e["pattern"])}</code></td>'
        f'<td style="font-family:var(--mono);font-size:.8rem">'
        f'{next(t["articles"] for t in ANALYSIS["themes"] if t["id"] == e["id"])}</td></tr>'
        for e in LEXICON["entries"])
    gates = [
        ("Every frozen file still hashes to its registered SHA-256",
         "the one check the whole section rests on"),
        ("The page that could not be fetched is recorded as excluded, never as held", ""),
        ("Every article traces to two registered frozen files, and the announcement order is intact", ""),
        ("No twelve consecutive words of any op-ed appear on any page we generate",
         "the permission statement itself is the one exemption, because quoting the terms IS the finding"),
        ("The permission statement recorded for each piece is in its frozen bytes verbatim", ""),
        ("Every licence count re-derives from the frozen HTML, by a second implementation",
         "different patterns, different program, same bytes"),
        ("No page understates the permission the publisher gave",
         "it is real and generous; the finding is about its form, not its existence"),
        ("Every theme edge re-derives from the frozen prose, in both directions",
         "no match, no edge — and every match must have an edge, so a theme cannot be dropped by hand either"),
        ("The graph conforms to its ontology: declared types, named inverses, a Portuguese form "
         "on every verb, no banned verb, nothing outside a verb's domain and range", ""),
        ("No page claims that any author agrees with any other",
         "agrees_with is banned; shared vocabulary is not agreement"),
        ("Every author is a byline the piece printed, and every affiliation is transcribed from "
         "a role line that is still in the bytes, with nothing in the graph that the file does "
         "not state and nothing in the file the graph does not build",
         "checked in both directions, one line at a time"),
        ("The count of pieces whose structured author field disagrees with the printed byline "
         "re-derives", ""),
        ("No email address or phone number for any natural person reaches the data",
         "refused where the data is parsed, not hidden where it is rendered"),
        ("The manifest is complete and every file in it hashes to its recorded value", ""),
        ("Every page states that this is beta, that the bytes are frozen and hashed, and that "
         "we republish none of the prose", ""),
    ]
    def gate_row(a, b):
        note = f'<div class="small dim" style="margin-top:.2rem">{esc(b)}</div>' if b else ""
        return f"<tr><td>{esc(a)}{note}</td></tr>"

    grows = "".join(gate_row(a, b) for a, b in gates)

    body = f"""{masthead("method.html")}
<h1>Method</h1>
<p class="lead">Fetch once, freeze the bytes, hash them, extract structure, derive what can be
derived by a published formula, and refuse to ship if any of it stops re-deriving. Everything
on this page is a description of code you can read in
<a href="https://github.com/SGit-AI/SGit-AI__Website__Newsroom/tree/main/world-news-day/build">world-news-day/build/</a>.</p>

{disclaimer()}

<h2 id="path">The path</h2>
<div class="ops">
<div class="op"><b>1 &middot; fetch</b><p><code>build/extract.py --fetch</code> reads the
twenty-one URLs once, with a browser user-agent, and writes each response to a dated folder.
It takes two files per piece: the page as served, and the record from the site&rsquo;s own
WordPress REST API. Without <code>--fetch</code> nothing touches the network, so anyone who
clones this repository rebuilds the whole section from the bytes already in it.</p></div>
<div class="op"><b>2 &middot; freeze</b><p>Every response is written with a
<code>.snapshot</code> extension. Third-party bytes held as evidence must never be served or
indexed as pages of this site, and an extension is a stronger guarantee of that than a
convention.</p></div>
<div class="op"><b>3 &middot; hash</b><p>Each file is hashed with SHA-256 into
<code>data/register.json</code> with its URL, retrieval time and size. The gate re-computes
every hash on every build. An edited frozen copy fails the build.</p></div>
<div class="op"><b>4 &middot; extract</b><p><code>build/extract.py</code> reads the frozen REST
records into <code>data/corpus.json</code>: order, title, dates, word count, byline, the role
line as printed, the permission statement verbatim, categories, tags, outbound links, and
which schema.org types the page carries. <b>The article body is not written to any file this
section publishes.</b></p></div>
<div class="op"><b>5 &middot; derive</b><p><code>build/graph.py</code> builds the ontology, the
graph and the licence findings; <code>build/analysis.py</code> builds the aggregate counts.
The only classification either makes rather than reads is the theme lexicon below, and every
theme edge carries the words that matched it.</p></div>
<div class="op"><b>6 &middot; gate</b><p><code>build/gates.py</code> re-derives the lot from
the frozen bytes and exits non-zero on any disagreement, then
<code>admin/build/validate.js</code> checks the section as part of the whole site. No tag, no
publish.</p></div>
</div>

<h2 id="lexicon">The lexicon</h2>
<p>{esc(LEXICON["note"])}</p>
<p>These {len(LEXICON["entries"])} patterns are the only classification in this section. They
are published here in full so that you can disagree with them precisely rather than in
general &mdash; a theme edge says <em>this piece contains these words</em> and says nothing
else at all. The gate runs every pattern again on the frozen prose, in both directions: a
theme in the graph whose pattern no longer matches fails the build, and so does a pattern
that matches an article which has no edge for it.</p>
<div class="tablewrap"><table>
<thead><tr><th>Theme</th><th>Pattern, against the article&rsquo;s own prose</th><th>Matches</th></tr></thead>
<tbody>{lex}</tbody>
</table></div>

<h2 id="transcription">The one thing written by hand</h2>
<p>Everything in this section is derived by a program except one file:
<a href="data/affiliations.json"><code>data/affiliations.json</code></a>, which records where
each of the twenty-three authors works.</p>
<p>It was derived by a program first, and the program was wrong in the way that matters. A
role line is free prose &mdash; <em>&ldquo;Founder: Paraluman News, The Philippines&rdquo;</em>,
<em>&ldquo;is an Indian media leader. She is the co-founder&hellip;&rdquo;</em> &mdash; and a
one-line pattern over it produced an author who works at &ldquo;Philippines&rdquo;, another at
&ldquo;an Indian media leader&rdquo;, and a third at a summit. Every one of those is
<b>plausible</b>, which is the worst thing an edge in a graph can be: once it is in the file,
nothing distinguishes it from a true one.</p>
<p>So the twenty-three lines were read and written out by hand, and the gate checks each one
against the bytes in both directions: the role line must appear in that article verbatim,
every organisation must appear inside that role line verbatim, the file and the graph must
name the same authors, and the graph must hold exactly the affiliation edges the file states
&mdash; no more and no fewer. Two role lines name only former posts; those record no
organisation and say why, because this section holds nobody&rsquo;s employment history.</p>

<h2 id="gates">What the gate checks</h2>
<div class="tablewrap"><table><tbody>{grows}</tbody></table></div>

<h2 id="refuses">What this section refuses to do</h2>
<ol>
<li><b>Republish the prose.</b> Even though the terms permit it. We are describing somebody
else&rsquo;s corpus and arguing that its terms should be machine-readable; republishing it
while doing so would confuse the two acts, and the pieces are better read where their authors
put them.</li>
<li><b>Score, rank or rate anyone.</b> Twenty-one named people at twenty-one named
organisations. A count of words is not a measure of a person, and this publication originates
no assessment of any of them.</li>
<li><b>Assert agreement.</b> Two pieces touching the same theme is not agreement.
<code>agrees_with</code> is a banned verb in the ontology, enforced by the gate.</li>
<li><b>Give legal advice.</b> The reading of the permission on
<a href="licences.html">the licence page</a> is a careful reading by people who are not
lawyers, published so it can be corrected. If you are deciding whether you may republish one
of these pieces: read the terms on the piece and ask the publisher.</li>
</ol>

<h2 id="pt">The Portuguese</h2>
<p>Every node type and every verb in this section carries a Portuguese form, and nothing here
is published in Portuguese. That is deliberate and it is stated rather than implied: the
second language is a switch to be thrown at <a href="../pt-newsroom/index.html">pt.newsroom</a>,
not a retrofit to be done later. Carrying <code>pt</code> from the first commit is what makes
it a switch.</p>

<h2 id="rebuild">Rebuilding this</h2>
<pre class="shell"><span class="d"># from a clone, with no network access at all:</span>
<span class="g">python3</span> world-news-day/build/build.py
<span class="g">python3</span> admin/build/chrome.py
<span class="g">python3</span> world-news-day/build/gates.py <span class="d">&amp;&amp;</span> <span class="g">node</span> admin/build/validate.js

<span class="d"># to take a new dated snapshot (this is the only step that uses the network):</span>
<span class="g">python3</span> world-news-day/build/extract.py --fetch</pre>

{agent_block(
    'The build is deterministic and offline by default: <code>build.py</code> reads only the '
    'frozen bytes under <code>sources/frozen/</code> and writes only <code>data/*.json</code> '
    'and the pages. <code>build/gates.py</code> is the executable specification of everything '
    'this section claims — read it rather than trusting this page, and note that it '
    're-implements the licence counts independently of the code that produced them.')}
"""
    return write("method.html", page(
        "method.html", "Method",
        "Fetch once, freeze, hash, extract, derive by published formula, and refuse to ship if "
        "any of it stops re-deriving — plus the twenty theme patterns, in full.",
        body, '<a href="../index.html">newsroom.sgit.ai</a> / '
              '<a href="index.html">world news day</a> / method'))


def main():
    built = [build_index(), build_licences(), build_corpus(), build_findings(),
             build_graph_page(), build_sources(), build_method()]
    print(f"world-news-day: {len(built)} pages")
    for b in built:
        print("  ·", b)


if __name__ == "__main__":
    main()
