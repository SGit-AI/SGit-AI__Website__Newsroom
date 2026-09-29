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


import graph as graphmod      # noqa: E402 — ontology, graph, triples, licence findings
import analysis as analysismod  # noqa: E402 — the aggregate counts
import claims as claimsmod      # noqa: E402 — the fractal layer: every sentence, typed and anchored
import vault as vaultmod        # noqa: E402 — the bundle, and the record of what is in it
import contacts as contactsmod  # noqa: E402 — how to reach them, under published rules
import outreach as outreachmod  # noqa: E402 — the second vault, the one the other agent works in
graphmod.main()
analysismod.main()
claimsmod.main()
contactsmod.build()
outreachmod.main()
vaultmod.main()
graphmod.manifest()   # last: it hashes everything the three steps above wrote, bundle included

REGISTER = load("register.json")
CORPUS = load("corpus.json")
LICENCES = load("licences.json")
ONTOLOGY = load("ontology.json")
GRAPH = load("graph.json")
LEXICON = load("lexicon.json")
AFFILIATIONS = load("affiliations.json")
CLAIMS = load("claims.json")
TERMS = load("terms.json")
CLAIM_RULES = load("claim-rules.json")
CONTACTS = load("contacts.json")
VAULT_AUDIT = load("vault-audit.json")
CONTACT_RULES = load("contact-rules.json")
CORRECTIONS = load("corrections.json")
VAULT = load("vault.json")
OUTREACH = load("outreach-vault.json")
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
    "contacts": {"en": "How to reach them", "pt": "Como contactá-los"},
    "vault":    {"en": "The vault",    "pt": "O cofre"},
    "method":   {"en": "Method",       "pt": "Método"},
}
NAV = [("index.html", "index"), ("licences.html", "licences"), ("corpus.html", "corpus"),
       ("findings.html", "findings"), ("graph.html", "graph"), ("sources.html", "sources"),
       ("contacts.html", "contacts"), ("vault.html", "vault"), ("method.html", "method")]


def esc(x):
    return html.escape(str(x) if x is not None else "")


def ld_json(rel, title, desc):
    """The section's own licence, in the field the corpus leaves empty.

    It would be hard to publish a page arguing that schema.org's `license` property costs one
    line and is worth adding, on a page that does not have one. So every page here carries the
    declaration we say the twenty-one are missing — a named licence with a version and a URL,
    a copyright holder, and `isAccessibleForFree`. The gate fails the build if any page in this
    section loses it. This is the only part of the argument we can make by doing rather than
    by saying."""
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": desc,
        "url": f"{HOST}/world-news-day/{rel}",
        "isPartOf": {"@type": "WebSite", "name": "newsroom.sgit.ai", "url": HOST},
        "publisher": {"@type": "Organization", "name": "newsroom.sgit.ai",
                      "url": HOST, "parentOrganization": {"@type": "Organization",
                                                          "name": "sgit", "url": "https://sgit.ai"}},
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "copyrightHolder": {"@type": "Organization", "name": "newsroom.sgit.ai", "url": HOST},
        "copyrightNotice": "CC BY 4.0. This licence covers this page's own description, counts "
                           "and graph. It does NOT cover the twenty-one op-eds, which are the "
                           "work of their authors and are published at worldnewsday.org under "
                           "terms stated there; none of their prose is reproduced here.",
        "usageInfo": f"{HOST}/world-news-day/licences.html",
        "isAccessibleForFree": True,
        "creator": {"@type": "Organization", "name": "sgit agents",
                    "description": "Researched, extracted and drafted by software agents "
                                   "against frozen, hashed bytes. No human editor of record."},
        "dateModified": LATEST,
    }, ensure_ascii=False, indent=1)


def page(rel, title, desc, body, crumb):
    # Depth-aware, because the section grew a stories/ folder after the first nine pages were
    # written flat and every relative link in the shell was one level short.
    up = "../" * rel.count("/")
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
<link rel="license" href="https://creativecommons.org/licenses/by/4.0/">
<link rel="stylesheet" href="{up}../assets/site.css">
<script type="application/ld+json">
{ld_json(rel, title, desc)}
</script>
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


def masthead(here="", up=""):
    links = "".join(
        f'<a href="{up}{h}" style="font-size:.83rem;color:'
        f'{"#101114;font-weight:600" if h == here else "#5c5f66"}">{esc(LABELS[k]["en"])}</a>'
        for h, k in NAV)
    return ('<div class="ops" style="margin:0 0 1.4rem">'
            '<div class="op" style="border-left-color:#b91c1c">'
            '<b style="color:#b91c1c">World News Day 2026 &middot; beta</b>'
            '<p style="display:flex;gap:1.1rem;flex-wrap:wrap;align-items:center;margin-top:.45rem">'
            + links + "</p></div></div>")


def disclaimer(up=""):
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
        f'<a href="{up}sources.html">The register &rarr;</a> &middot; '
        f'<a href="{up}method.html">The method &rarr;</a></p>'
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
        (f'{CLAIMS["counts"]["by_type"].get("proposal", 0)} of {CLAIMS["counts"]["claims"]:,}',
         "sentences propose doing anything",
         f'{CLAIMS["counts"]["by_type"].get("assertion", 0)} are flat assertions'),
        (f'{TERMS["counts"]["definitions_found"]}', "places anybody says what a word means",
         f'over {CLAIMS["counts"]["claims"]:,} sentences about trust, truth and journalism'),
        (f'{CONTACTS["counts"]["authors_reachable_via_an_organisation"]} of {CONTACTS["counts"]["authors"]}',
         "authors with any published route to reach them",
         "none of it from the corpus, all of it via an organisation"),
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
        ("The fractal layer", "terms.html", f'{CLAIMS["counts"]["claims"]:,} sentences, typed',
         "Each piece is its own graph of claims — assertions, questions, hypotheses, "
         "proposals — connected to the others by a shared vocabulary. Same shape at every "
         "zoom level. And four places in 1,070 sentences where anybody says what a word means."),
        ("The outreach", "contacts.html", "How to reach them",
         "Twenty-three authors at twenty-six organisations, and a corpus that gives you no "
         "route to any of them. What going to their own sites produced, under rules published "
         "before the looking started."),
        ("The evidence", "sources.html", "Every file, every hash",
         f'{REGISTER["count"]} frozen files with their SHA-256, the dated snapshot they belong '
         "to, and what this section has already had to correct about them in public."),
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
<a class="card" href="stories/free-to-republish-is-not-a-licence.html"
   style="display:block;border-left:4px solid #b91c1c;margin-bottom:.8rem">
<span class="tag">The argument, in one piece</span>
<h3 style="font-size:1.25rem">Free to republish is not a licence</h3>
<p>Twenty-one of the most senior people in news gave their work away on the same day. Not one
of them said, in a form a machine can read, on what terms &mdash; and the line that would fix
it is already half-written on every page. Written to be sent to them, and free to republish
under a licence with a name.</p>
<span class="go">Read it &rarr;</span></a>
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
<p class="small dim">Both sentences are now read from frozen, hashed bytes. The
announcement&rsquo;s was not, until v0.4.2: <code>wan-ifra.org</code> sits behind a
JavaScript-challenge firewall that refused two automated attempts, and this section published
that as &ldquo;the one page in the beat a machine cannot read&rdquo;, which was too strong. The
refusal is intermittent; a later attempt returned the page, and the sentence quoted by hand
turned out to be verbatim. <a href="method.html#corrections">What we got wrong, and the rule it
produced &rarr;</a></p>

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
            f'<td><a href="pieces/{esc(a["slug"])}.html"><b>{esc(a["title"])}</b></a> '
            f'<a href="{esc(a["url"])}" class="small dim">original &rarr;</a>'
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
    ann_attempts = SEC / "sources" / "frozen" / LATEST / "announcement-attempts.json"
    tries = json.loads(ann_attempts.read_text(encoding="utf-8")) if ann_attempts.exists() else []
    refused = sum(1 for a in tries if not a["read"])
    exclusions_none = f"""<p>Nothing is excluded from this snapshot: all {REGISTER["count"]}
files are held and hashed, the announcement among them.</p>
<div class="warnbox"><p style="margin-top:0"><b>That is a correction, and it is the most
important thing on this page.</b> Until v0.4.2 this section said the announcement was
&ldquo;the one page in the beat a machine cannot read&rdquo;, on the evidence of two refused
attempts. <code>wan-ifra.org</code> is served through a JavaScript-challenge firewall that
refuses <em>some</em> automated requests: on this capture it refused {refused} attempt(s) and
then returned the full page. A refusal observed twice is a fact about two attempts, not a
property of a page.</p>
<p style="margin-bottom:0">The claim was published more strongly than the evidence supported,
and it was the flattering kind of error &mdash; a finding about somebody else&rsquo;s
infrastructure. Every attempt is now counted and recorded with the size and hash of what came
back. <a href="method.html#corrections">The full correction, and the rule it produced
&rarr;</a></p></div>"""
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

<h2 id="excluded">What we could not read, and what we got wrong about it</h2>
{excluded or exclusions_none}

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
        ("The announcement is either held as a source or excluded with a reason, never neither, and where its terms are quoted they are in its frozen bytes verbatim",
         "until v0.4.2 this gate REQUIRED it to be excluded, which encoded two refused attempts as a property of the page"),
        ("Every published contact address re-derives from the frozen bytes and passes the published rules, and none contains an author’s name", ""),
        ("Every correction names a version, the claim and what it says now, and the withdrawn claim appears nowhere without the correction beside it", ""),
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
    def corr_block(c):
        opt = ""
        for label, key in (("It now says", "it_now_says"),
                           ("What changed downstream", "what_changed_downstream"),
                           ("How it was caught", "how_it_was_caught"),
                           ("What it cost", "what_it_cost")):
            if c.get(key):
                opt += f'<p><b>{label}:</b> {esc(c[key])}</p>'
        where = ", ".join(f"<code>{esc(w)}</code>" for w in c["where"])
        return (
            '<div class="note" style="border-left-color:#b91c1c">'
            f'<p style="margin-top:0"><b>{esc(c["id"])}</b> &mdash; wrong in '
            f'<code>{esc(c["wrong_in"])}</code>, fixed in <code>{esc(c["fixed_in"])}</code></p>'
            f'<p><b>We said:</b> &ldquo;{esc(c["we_said"])}&rdquo;</p>'
            f'<p><b>What was wrong:</b> {esc(c["what_was_wrong"])}</p>'
            + opt
            + f'<p><b>The rule it produced:</b> {esc(c["the_rule_it_produced"])}</p>'
            + f'<p class="small dim" style="margin-bottom:0">Carried on: {where}</p></div>')

    corr = "".join(corr_block(c) for c in CORRECTIONS["corrections"])

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

<h2 id="corrections">What this section got wrong</h2>
<p>This publication argues that <a href="../corrections/index.html">a correction which does not
reach what it disproved is not a correction</a>. A section that will not correct itself in
public has no standing to make that argument, so here is the list, with the version that
carried each error and the rule it produced.</p>
{corr}
<p class="small dim">Machine surface: <a href="data/corrections.json"><code>data/corrections.json</code></a>.
The gate checks that every correction names a version, the claim and what it says now &mdash;
and that the withdrawn claim appears nowhere in this section without the correction beside it.</p>

<h2 id="withheld">The pages we fetched and did not keep</h2>
<p>Everything else this section fetches is frozen. A few pages are not, and the rule is
published in <a href="data/contact-rules.json"><code>data/contact-rules.json</code></a>: <b>a
page carrying ten or more addresses of named people is a staff directory, and its bytes are not
retained.</b> The URL, the retrieval time, the SHA-256 of what came back and the counts are
recorded; the file is kept neither in this repository nor in the vault bundle.</p>
<p>The case it exists for is the Globe and Mail, whose contact page publishes the direct
address of seventy-nine named journalists. That page is public, so this is not secrecy. It is
that freezing a staff directory into a git repository and shipping it in a downloadable bundle
makes it materially easier to scrape than the publisher made it, and that is not a thing this
section will do to twenty-three colleagues.</p>
<p><b>It costs something, and the cost is stated rather than hidden:</b> for a page held this
way the count is an assertion about bytes we no longer have, not a number a reader can
re-derive from this repository. The hash is kept so that anyone can re-fetch the page and check
the count against it.</p>
<p class="small dim">A second, smaller storage rule: organisation pages that <em>are</em> kept
are stored gzipped, because a home page is one to two megabytes of script bundle and eleven
megabytes of that is payload rather than evidence. The SHA-256 recorded is of the
<b>original</b> bytes; the gate decompresses and re-verifies it, so the anchoring is exactly as
strong and the repository is a fifth of the size.</p>

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


# ------------------------------------------------------------------ vault ---
def vault_records():
    """The two vaults, in the order they are listed. Newest last here because the corpus one
    is the reason the other exists."""
    audit = {a["name"]: a for a in VAULT_AUDIT["audited"]}
    return [
        {"slug": "corpus", "n": 1, "name": "World News Day 2026 · the corpus",
         "rec": VAULT, "audit": audit.get("corpus", {}),
         "category": "Record",
         "what": "Twenty-one commissioned op-eds frozen and hashed, every derived dataset, "
                 "the build code and the gate that checks it — and not a word of the prose "
                 "republished",
         "one_thing": "A corpus somebody else published, described precisely enough that the "
                      "description is useful on its own, and anchored well enough that you can "
                      "check every number in it without us.",
         "published": LATEST},
        {"slug": "outreach", "n": 2, "name": "World News Day 2026 · the outreach",
         "rec": OUTREACH, "audit": audit.get("outreach", {}),
         "category": "Record",
         "what": "The append-only working vault the agent at riskmandate.ai collaborates in: "
                 "targets, a protocol, and an action log with a closed verb list",
         "one_thing": "A second provenance chain for the things we DO, kept apart from the "
                      "evidence of what somebody else published, because they fail in "
                      "different ways.",
         "published": LATEST},
    ]


def credential_block(v, up=""):
    """sgit.ai's convention, and it is the right one: the key in the open, three ways to use
    it, and a plain sentence saying what it cannot do."""
    rec, a = v["rec"], v["audit"]
    key, vid = rec.get("read_key"), rec.get("vault_id")
    if not (rec.get("pushed") and key and vid):
        return ('<div class="warnbox"><p style="margin:0"><b>Not published.</b> This vault has '
                'no read key on it yet.</p></div>')
    return (
        '<div class="note" style="border-left-color:#0f766e">'
        '<p style="margin-top:0"><b>Open it yourself. The key is the whole credential.</b> '
        'No account, nothing to install, and no write capability in it.</p>'
        f'<p style="font-family:var(--mono);font-size:.76rem;word-break:break-all">'
        f'{esc(key)}:{esc(vid)}</p>'
        f'<p class="small">In the official UI: '
        f'<a href="{esc(a.get("open_in_ui", ""))}">open it read-only in a new tab &rarr;</a> '
        f'&middot; From the CLI: <code>sgit clone {esc(key)}:{esc(vid)}</code></p>'
        '<p class="small dim" style="margin-bottom:0">A read key is derived one-way from the '
        'vault key and cannot become write access. The vault key is in no file in this '
        'repository and never will be; the whole-site gate fails the build on anything shaped '
        'like one.</p></div>')


def audit_block(v):
    a = v["audit"].get("audit", {})
    if not a.get("ran"):
        return ('<p class="dim">The audit did not run: '
                f'{esc(a.get("why", "no reason recorded"))}.</p>')
    n = a["negative_control"]
    cleared = "".join(
        f'<tr><td class="small"><code>{esc(f["file"])}</code></td>'
        f'<td class="small"><code>{esc(f["match"])}</code></td>'
        f'<td class="small dim">{esc(f["verdict"])}</td></tr>'
        for f in a["findings"])
    return (
        f'<p><b>What was checked, and when.</b> On {esc(a["at"][:10])}, the published vault at '
        f'<code>{esc(v["audit"]["derived"]["head"] or "HEAD")}</code>. The credential '
        f'classified as <b>{esc(v["audit"]["credential"]["verdict"])}</b>. A clone made with '
        f'that key <em>alone</em> — no token — was scanned file by file: '
        f'{a["text_files_scanned"]} text files, against {len(a["patterns"])} patterns '
        f'(vault-key shapes, every <code>sgit_</code> prefix, AWS and OpenAI key shapes, '
        f'bearer tokens, private-key blocks, and email addresses).</p>'
        f'<p><b>What was found: {a["hits"]} hits, {a["cleared"]} cleared, '
        f'<b style="color:{"#b91c1c" if a["unexplained"] else "#0f766e"}">{a["unexplained"]} '
        f'unexplained</b>.</b> Ruling a hit out is the work, so every one carries the rule that '
        f'cleared it. A scanner that reports hits and no verdicts has moved the job to the '
        f'reader.</p>'
        + (f'<details><summary class="small">Every hit, with its verdict</summary>'
           f'<div class="tablewrap"><table><thead><tr><th>File</th><th>Match</th>'
           f'<th>Verdict</th></tr></thead><tbody>{cleared}</tbody></table></div></details>'
           if cleared else '<p class="small dim">No pattern fired.</p>')
        + f'<p><b>The negative control.</b> The same clone attempted with '
          f'{esc(n["attempted_with"])} <b>{"fails, as it must" if n["failed_as_required"] else "SUCCEEDED, which it must not"}</b>'
          f' — exit code {n["exit_code"]}. A wrong key cannot even find the vault index, '
          f'because the index address is derived from the key.</p>'
        + '<p class="small dim">What a clean scan means: nothing matching those patterns is in '
          'the <em>current</em> files of the published vault. It is not a statement about its '
          'history, and not a promise that nothing sensitive sits in a file matching no '
          'pattern.</p>')


def derived_block(v):
    d = v["audit"].get("derived")
    if not d:
        return ""
    return (
        '<p>From a read-key clone, read-only, no token, no repository — because the repository '
        'is not what was published:</p><ul>'
        f'<li><b>Files:</b> {d["file_count"]} &middot; <b>plaintext size:</b> '
        f'{d["bytes"] / 1048576:.2f} MB</li>'
        f'<li><b>Commits:</b> {d["commits"]} &middot; <b>HEAD:</b> '
        f'<code>{esc(d["head"] or "—")}</code></li>'
        f'<li><b>Top level:</b> ' + ", ".join(f"<code>{esc(x)}</code>" for x in d["top_level"]) + '</li>'
        f'<li><b>Opens as a page:</b> {"yes, <code>_page.json</code> at the root" if d["has_page_json"] else "no"}'
        f' &middot; <b>README:</b> {"yes" if d["has_readme"] else "no"}</li>'
        '</ul>')


# ------------------------------------------------------------ vault index ---
def build_vault_index():
    rows = "".join(
        f'<tr><td style="font-family:var(--mono);color:var(--dim2)">{v["n"]}</td>'
        f'<td><a href="vaults/{esc(v["slug"])}.html"><b>{esc(v["name"])}</b></a> '
        f'<code class="dim small">{esc(v["rec"].get("vault_id") or "—")}</code></td>'
        f'<td class="small">{esc(v["what"])}</td>'
        f'<td class="small">{esc(v["category"])}</td>'
        f'<td class="small" style="font-family:var(--mono)">'
        f'{v["audit"].get("derived", {}).get("file_count", "—")}</td>'
        f'<td class="small" style="font-family:var(--mono);white-space:nowrap">'
        f'{v["audit"].get("derived", {}).get("bytes", 0) / 1048576:.2f} MB</td>'
        f'<td class="small dim" style="white-space:nowrap">{esc(v["published"])}</td></tr>'
        for v in vault_records())
    mb = VAULT["bytes"] / 1_048_576

    body = f"""{masthead("vault.html")}
<h1>Published vaults</h1>
<p class="lead">Two encrypted vaults you can open in your browser right now. <b>Every read key
here was published on purpose</b>, and a read key is the whole credential: no account, nothing
to install, no write capability in it. Each row opens a page with what the vault does, the
audit that was run before the key was published, and the facts derived from the key itself.</p>

{disclaimer()}

<div class="tablewrap"><table>
<thead><tr><th>#</th><th>Vault</th><th>What it is</th><th>Category</th><th>Files</th>
<th>Size</th><th>Published</th></tr></thead>
<tbody>{rows}</tbody></table></div>

<h2 id="method">The method is not ours</h2>
<p><a href="https://sgit.ai/demos/vaults/index.md">sgit.ai publishes thirty-seven vaults</a>
and writes down how, in
<a href="https://sgit.ai/demos/vaults/publishing.md">seven steps for another agent to
follow</a>. These two are published the same way, so that a reader who knows one estate&rsquo;s
vault pages can read the other&rsquo;s without learning anything new. The two rules everything
else serves, in their words:</p>
<div class="split"><table>
<thead><tr><th class="run">Read keys yes, vault keys never</th>
<th class="rent">Audit before the key, not after</th></tr></thead>
<tbody><tr>
<td>A read key is a capability handed out on purpose and cannot become write access. A vault
key is read <em>and</em> write; publishing one hands the vault to anybody.</td>
<td>Revocation is not retroactive. Anyone who fetches the objects keeps them, so an audit
that happens after publication has not happened.</td>
</tr></tbody></table></div>
<p>We reimplemented the checks rather than importing them, so that the code that classifies a
credential and the code that scans a clone can be read beside the result:
<a href="https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/main/world-news-day/build/vault_audit.py"><code>build/vault_audit.py</code></a>.
Every audit on these pages is its output, so a page cannot claim an audit that did not run.</p>

<h2 id="zip">Or skip the tooling entirely</h2>
<div class="dl">
  <div>
    <b>world-news-day/vault.zip</b>
    <p>The corpus vault&rsquo;s contents as one file, built deterministically from the frozen
    bytes: the same input produces the same bundle, hash for hash, so the digest below is a
    fact about the contents rather than a record of when the build ran.</p>
    <p class="small dim" style="font-family:var(--mono);word-break:break-all">SHA-256
    {esc(VAULT["sha256"])}</p>
  </div>
  <a class="dlbtn" href="vault.zip">Download<span>{mb:.2f} MB &middot; {VAULT["count"]} files</span></a>
</div>

{agent_block(
    'Fetch <code>data/vault.json</code> and <code>data/outreach-vault.json</code> for the two '
    'published vaults (id, public read key, remote), and <code>data/vault-audit.json</code> '
    'for what was derived and scanned with those keys — file counts, sizes, commit depth, '
    'HEAD, every pattern hit and the rule that cleared it, and the negative control. '
    '<b>Only <code>sgit_public_read_</code> keys appear anywhere in this section</b>; a vault '
    'key is write access and is in no file here.')}
"""
    return write("vault.html", page(
        "vault.html", "Published vaults",
        "Two encrypted vaults, both open with a published read-only key: the World News Day "
        "corpus, and the append-only outreach vault. With the audit run before each key was "
        "published, and the facts derived from the key itself.",
        body, '<a href="../index.html">newsroom.sgit.ai</a> / '
              '<a href="index.html">world news day</a> / vaults'))


# ------------------------------------------------------------- vault pages ---
def build_vault_pages():
    up = "../"
    built = []
    DETAIL = {
        "corpus": {
            "in_it": [
                ("data/", "The corpus described, the licence finding, the affiliations "
                          "transcription, the aggregate, the published lexicons, the ontology, "
                          "the graph and the same graph as N-Triples. The article prose is in "
                          "none of them."),
                ("sources/frozen/", "The twenty-one pages as served and the records the "
                                    "publisher's own REST API returns for them, plus the "
                                    "announcement — every one hashed and registered."),
                ("build/", "Everything that produced the above, including the gate. The gate "
                           "runs inside this vault: it detects the layout and names the four "
                           "checks it skips, which are about the website's pages rather than "
                           "the data."),
                ("_page.json", "What you see when the vault is opened, rather than whichever "
                               "file sorts first — which was MANIFEST.json, a list of hashes."),
            ],
            "demonstrates": [
                ("A corpus described without being republished",
                 "20,060 words held, none reproduced. The gate fails the build if twelve "
                 "consecutive words of any piece appear on a generated page, with two "
                 "enumerated exemptions under 400 words in total."),
                ("Counts that two programs produce from the same bytes",
                 "Every licence count is derived by build/graph.py and re-derived by "
                 "build/gates.py with different patterns. A number one program can produce is "
                 "an assertion."),
                ("Classification as a published formula",
                 "Themes, claim types and role addresses all come from pattern files in "
                 "data/, and the gate re-runs every pattern on the frozen bytes in both "
                 "directions."),
                ("A vault that verifies itself",
                 "MANIFEST.json carries the SHA-256 of every file; build/gates.py re-derives "
                 "every published count. Both work from a read-key clone with no repository."),
            ],
            "says_about_itself": [
                "Agent-produced, with no human editor of record and no legal review.",
                "The evidence is a dated snapshot. A later capture would be a new dated folder "
                "beside it, and the difference between them would be a story.",
                "Our description is CC BY 4.0. The twenty-one op-eds are not ours and are not "
                "relicensed; their terms are on their own pages.",
                "No sentiment, stance or agreement is modelled. `agrees_with` is a banned verb "
                "in the ontology.",
                "One claim in this section has already been corrected in public, about the "
                "publisher of this very corpus.",
            ],
        },
        "outreach": {
            "in_it": [
                ("targets/", "One file per organisation: who writes from it, the established "
                             "route, the frozen pages the route came from with their hashes, "
                             "and why there is no route where there is none."),
                ("actions/", "Append-only, with a JSON schema and a closed list of verbs. "
                             "Deliberately empty at handover."),
                ("protocol.md", "The rules of engagement, in full. It binds the collaborating "
                                "agent as tightly as the gates bind us."),
                ("brief.md", "What we are asking for, what we are not asking for, and the "
                             "tone. Three small asks, all on the publisher's side."),
                ("evidence.md", "How to verify any claim in here against the corpus vault."),
            ],
            "demonstrates": [
                ("A second provenance chain, kept apart on purpose",
                 "The corpus vault is finished and safe to hand to anyone including the people "
                 "it describes. This one holds who we are contacting and what we plan to say. "
                 "Different claims, different failure modes, different audiences."),
                ("An agent bound by a protocol it did not write",
                 "No personal contact detail for any natural person; every action names what "
                 "it stands on by hash or URL; append, never edit; escalate rather than commit "
                 "the newsroom to anything."),
                ("Rules enforced before the vault is pushed",
                 "The section gate scans this vault's contents for any address that is not an "
                 "organisation's role address, by the same published two-part rule the "
                 "contacts map uses."),
                ("Generated, not kept by hand",
                 "build/outreach.py writes the whole thing from the same frozen bytes as "
                 "everything else, so anyone can rebuild it and diff rather than trust it."),
            ],
            "says_about_itself": [
                "Nothing has been sent. The action log is empty at handover and says so.",
                "Silence is data: a no-response is recorded explicitly rather than left as an "
                "absent file.",
                "A wrong action is corrected by a new action naming it. The original stays.",
                "The collaborating agent may draft, send through published routes and record. "
                "It may not commit the newsroom to anything or publish to the site.",
            ],
        },
    }
    for v in vault_records():
        d = DETAIL[v["slug"]]
        rec = v["rec"]
        in_it = "".join(f'<tr><td><code>{esc(a)}</code></td><td class="small">{esc(b)}</td></tr>'
                        for a, b in d["in_it"])
        dem = "".join(f'<tr><td><b>{esc(a)}</b></td><td class="small">{esc(b)}</td></tr>'
                      for a, b in d["demonstrates"])
        says = "".join(f"<li>{esc(x)}</li>" for x in d["says_about_itself"])
        other = "outreach" if v["slug"] == "corpus" else "corpus"

        body = f"""{masthead("", up)}
<p class="eyebrow">Published vault {v["n"]} of 2</p>
<h1>{esc(v["name"])}</h1>
<p class="lead">{esc(v["what"])}.</p>
<p><b>Why this one.</b> {esc(v["one_thing"])}</p>

{credential_block(v, up)}

{disclaimer(up)}

<h2 id="in-it">What is in it</h2>
<div class="tablewrap"><table>
<thead><tr><th>Path</th><th>What it holds</th></tr></thead><tbody>{in_it}</tbody></table></div>

<h2 id="demonstrates">What it demonstrates</h2>
<div class="tablewrap"><table>
<thead><tr><th>Mechanism</th><th>How</th></tr></thead><tbody>{dem}</tbody></table></div>

<h2 id="itself">What the vault says about itself</h2>
<ul>{says}</ul>

<h2 id="audit">The audit, honestly</h2>
{audit_block(v)}

<h2 id="derived">Derived facts</h2>
{derived_block(v)}

<h2 id="notes">Notes</h2>
<p><b>Where this sits.</b> Beside <a href="{esc(other)}.html">the {esc(other)} vault</a>, and
in the same convention as <a href="https://sgit.ai/demos/vaults/index.md">sgit.ai&rsquo;s
published vaults</a>, whose <a href="https://sgit.ai/demos/vaults/publishing.md">method</a>
this follows. <b>Write-key status:</b> held outside this repository, not escrowed anywhere it
can be published. A vault whose write key is lost is frozen &mdash; readable forever, never
correctable &mdash; so that status is worth stating where a reader will see it.</p>
<p><a href="{up}vault.html">&larr; All published vaults</a></p>

{agent_block(
    'The machine surface for this page is <code>' + up + 'data/'
    + ("vault.json" if v["slug"] == "corpus" else "outreach-vault.json")
    + '</code> for the credential and '
    '<code>' + up + 'data/vault-audit.json</code> for the audit and the derived facts — '
    'both produced by <code>build/vault_audit.py</code> from the published read key alone. '
    '<b>The key on this page grants read and only read.</b>')}
"""
        built.append(write(f"vaults/{v['slug']}.html", page(
            f"vaults/{v['slug']}.html", v["name"],
            v["what"] + ".",
            body, f'<a href="{up}../index.html">newsroom.sgit.ai</a> / '
                  f'<a href="{up}index.html">world news day</a> / '
                  f'<a href="{up}vault.html">vaults</a> / {esc(v["slug"])}')))
    return built


# --------------------------------------------------------------- contacts ---
def build_contacts():
    C = CONTACTS["counts"]
    F = CONTACTS["from_the_corpus_alone"]

    def cell(o):
        if o["addresses"]:
            return ", ".join(f'<a href="mailto:{esc(a)}"><code>{esc(a)}</code></a>' for a in o["addresses"])
        if o.get("bytes_not_retained"):
            n = sum(v["not_role_addresses"] for v in o["bytes_not_retained"].values())
            return (f'<span style="color:#b45309">{n} addresses found, every one a named '
                    f'person &mdash; <a href="method.html#withheld">bytes not retained</a></span>')
        if o.get("contact_page"):
            return '<span class="dim">no role address on the page</span>'
        return '<span class="dim">&mdash;</span>'

    def route(o):
        bits = []
        if o.get("contact_page"):
            bits.append(f'<a href="{esc(o["contact_page"])}">contact page</a>')
        elif o.get("site"):
            bits.append(f'<a href="{esc(o["site"])}">site</a>')
        for li in o.get("linkedin", []):
            bits.append(f'<a href="{esc(li)}">LinkedIn</a>')
        for pr in o.get("linkedin_people", []):
            bits.append(f'<a href="{esc(pr["url"])}">{esc(pr["author"])} on LinkedIn</a>')
        if o.get("why_none"):
            bits.append(f'<span class="dim small">{esc(o["why_none"])}</span>')
        return "<br>".join(bits) or '<span class="dim">&mdash;</span>'

    rows = "".join(
        f'<tr><td><b>{esc(o["org"])}</b>'
        + (f'<div class="small dim" style="margin-top:.2rem">{", ".join(esc(a) for a in o["authors"])}</div>'
           if o["authors"] else "")
        + f'</td><td class="small">{cell(o)}</td><td class="small">{route(o)}</td>'
        + f'<td class="small dim">{esc(o.get("established") or "not established")}</td></tr>'
        for o in sorted(CONTACTS["organisations"],
                        key=lambda x: (not x["addresses"], not x.get("contact_page"), x["org"])))

    def author_row(a):
        orgs = ", ".join(esc(o) for o in a["organisations"]) or '<span class="dim">&mdash;</span>'
        route = ('<b style="color:#0f766e">via the organisation</b>' if a["reachable"]
                 else '<span style="color:#b91c1c">no published route</span>')
        return (f'<tr><td>{esc(a["author"])}</td><td class="small">{orgs}</td>'
                f'<td class="small">{route}</td></tr>')

    arows = "".join(author_row(a) for a in CONTACTS["authors"])

    refuses = "".join(f"<li>{esc(r)}</li>" for r in CONTACTS["refuses"])
    roles = ", ".join(f"<code>{esc(r)}</code>" for r in CONTACT_RULES["role_local_parts"])

    body = f"""{masthead("contacts.html")}
<h1>How to reach them</h1>
<p class="lead">Twenty-three people wrote these pieces, at {C["organisations"] - 1} organisations.
If you want to answer them &mdash; and this section exists partly because we do &mdash; you
need a route. <b>The corpus gives you none.</b> This page is what going to the organisations&rsquo;
own sites produced, under rules published before the looking started.</p>

{disclaimer()}

<div class="claim">Not one of the {F["pieces"]} pages offers a way to reach its author or its
publisher. No contact address, no author URL in the structured record, no press line. Twenty-one
pieces asking the public to value journalism, published to be spread, and the corpus carries no
route back to the people who wrote them.</div>

<h2 id="rules">The rules, published before the looking</h2>
<p>A contacts list is exactly where a publication does damage if it is careless, so the method
is fixed in <a href="data/contact-rules.json"><code>data/contact-rules.json</code></a> and
enforced by the gate:</p>
<ol>
<li><b>Organisations, not people.</b> Every address here is an organisation&rsquo;s own
published role address, from that organisation&rsquo;s own site. No personal email, no direct
line, for anybody. Individual routing is <em>via the organisation</em>.</li>
<li><b>A role address is a published formula.</b> An address is published only if its local
part is one of these, or is the site&rsquo;s own name: {roles}. Everything else found is
counted and dropped. <b>{C["addresses_found_and_dropped"]} were dropped</b> to publish
{C["role_addresses_published"]}.</li>
<li><b>One hop.</b> The home page, then the one link the site itself labels as contact. Both
frozen and hashed. No directory, no third-party database, no guessed address.</li>
<li><b>The domain has to be established.</b> Four published tests; a page that passes none is
kept as a candidate and nothing is published from it. <em>News Corp Australasia</em> fails all
four because the site says News Corp Austral<b>ia</b> &mdash; close is not the same, and a
contacts list is where close is dangerous.</li>
<li><b>LinkedIn, only as the organisation offers it.</b> A company page linked from an
organisation&rsquo;s own frozen page is a route and is published. A personal profile is
published <em>only</em> where the profile slug is an author of this corpus, letter for letter.
{C["linkedin_profiles_found_and_dropped"]} personal profiles were found and dropped, and
<b>{C["author_profiles_established"]} passed</b> &mdash; including a near miss: one page links
<code>/in/annalamentillo</code>, and an author of this corpus is Anna Mae Lamentillo. Probably
the same person. <em>Probably</em> is not a standard for publishing somebody&rsquo;s profile as
theirs, and three of the four profiles on that same page belong to people with nothing to do
with the organisation &mdash; a site template&rsquo;s stock photos. Publishing those as that
newsroom&rsquo;s staff would have been a fabrication.</li>
<li><b>A page that is a staff directory is not retained.</b> Ten or more addresses of named
people on one page and we keep the URL, the hash and the counts but not the bytes.
<a href="method.html#withheld">Why, and what it costs &rarr;</a></li>
</ol>
<div class="note"><p style="margin-top:0"><b>What this page will not do</b></p>
<ul style="margin-bottom:0">{refuses}</ul></div>

<h2 id="orgs">The organisations</h2>
<div class="proof">
<div class="n"><b>{C["with_an_established_site"]} of {C["organisations"]}</b><span>organisations with an established site</span><em>the rest are candidates or nothing</em></div>
<div class="n"><b>{C["with_a_contact_page"]}</b><span>publish a contact page</span><em>the route that actually works</em></div>
<div class="n"><b>{C["role_addresses_published"]}</b><span>role addresses publishable</span><em>from {C["addresses_found_and_dropped"] + C["role_addresses_published"]} addresses seen</em></div>
<div class="n"><b>{C["with_a_linkedin_page"]}</b><span>link their own LinkedIn page</span><em>{C["linkedin_profiles_found_and_dropped"]} personal profiles dropped</em></div>
<div class="n"><b>{C["authors_reachable_via_an_organisation"]} of {C["authors"]}</b><span>authors with a published route</span><em>all of them via an organisation</em></div>
</div>
<div class="tablewrap"><table>
<thead><tr><th>Organisation, and who writes from it</th><th>Role address</th><th>Route</th><th>How the site was established</th></tr></thead>
<tbody>{rows}</tbody>
</table></div>

<h2 id="authors">The authors</h2>
<p class="small dim">Route only. No personal contact detail for any named person appears
anywhere in this section&rsquo;s data, and the gate refuses one where the data is parsed rather
than hiding it where the page is rendered.</p>
<div class="tablewrap"><table>
<thead><tr><th>Author</th><th>Organisation, from their own role line</th><th>Route</th></tr></thead>
<tbody>{arows}</tbody>
</table></div>

<h2 id="ifyouarehere">If you are one of the twenty-one</h2>
<p>Then you are the reader this page was built for, and three things are worth saying plainly.</p>
<p><b>The finding is not a criticism of your piece.</b> It is about the infrastructure under it:
a permission with no licence name, terms stated three different ways, and a corpus with no route
back to its authors. None of that is your doing and all of it is fixable in an afternoon.</p>
<p><b>Everything here is checkable, and wrong things get corrected in public.</b> Every number
walks back to bytes we froze and hashed; <a href="vault.html">the vault</a> is one download.
This section has already corrected itself once, in public, about the publisher of this very
corpus &mdash; <a href="method.html#corrections">what we got wrong &rarr;</a>.</p>
<p><b>If something here is wrong about you or your organisation, say so and it changes.</b> The
repository is open and every page is generated from data files you can read. Corrections are
recorded with the version that carried the error, not quietly edited away.</p>

{agent_block(
    'Fetch <code>data/contacts.json</code> and <code>data/contact-rules.json</code>. The first '
    'carries, per organisation, the authors who write from it, the established site and how it '
    'was established, the frozen pages with their hashes, the role addresses that passed the '
    'rules, and the count of what was dropped; the second carries the rules themselves. '
    '<b>There is no personal contact detail anywhere in this section, by design</b> — do not '
    'infer one, and do not treat an organisation address as a way to reach an individual '
    'without saying that is what you are doing.')}
"""
    return write("contacts.html", page(
        "contacts.html", "How to reach them",
        "Twenty-three authors, twenty-six organisations, and what a corpus published to be "
        "spread gives you to reach them with: nothing. Role addresses and contact routes found "
        "under published rules, with everything dropped counted.",
        body, '<a href="../index.html">newsroom.sgit.ai</a> / '
              '<a href="index.html">world news day</a> / how to reach them'))


def stamp_llms():
    """The agent surface names the bundle's size and hash. Those change whenever the corpus or
    the code does, and a hash that is one build stale is worse than no hash at all — it tells a
    reader their download is corrupt. So it is stamped here rather than typed, and the section
    gate fails the build if the two ever disagree."""
    f = ROOT / "llms.txt"
    text = f.read_text(encoding="utf-8")
    line = (f'/world-news-day/vault.zip, {VAULT["count"]} files,\n'
            f'    {VAULT["bytes"] / 1048576:.2f} MB, SHA-256 {VAULT["sha256"]}')
    new = re.sub(r"/world-news-day/vault\.zip, \d+ files,\n\s*[\d.]+ MB, SHA-256 [0-9a-f]{64}",
                 line.replace("\\", "\\\\"), text, count=1)
    if new != text:
        f.write_text(new, encoding="utf-8")
        return "llms.txt"
    return None


# ------------------------------------------------------------------ story ---
# A minimal markdown renderer, the same shape as /portugal/'s. The prose lives in
# content/<slug>.md so that the thing we ask people to read is a file they can read without
# this site, and the numbers in it are TOKENS filled from the data at build time — an article
# whose figures are typed is an article whose figures go stale on the next capture.
def md_to_html(src):
    out, para, lst = [], [], None

    def flush():
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para.clear()

    def endlist():
        nonlocal lst
        if lst:
            out.append(f"</{lst}>")
            lst = None

    for line in src.splitlines():
        s = line.rstrip()
        if s.startswith("    ") and s.strip():
            flush(); endlist()
            out.append(f'<pre class="shell">{esc(s.strip())}</pre>')
        elif not s.strip():
            flush(); endlist()
        elif s.startswith("## "):
            flush(); endlist()
            slug = re.sub(r"[^a-z0-9]+", "-", s[3:].lower()).strip("-")
            out.append(f'<h2 id="{slug}">{inline(s[3:])}</h2>')
        elif re.match(r"^\d+\. ", s):
            flush()
            if lst != "ol":
                endlist(); out.append("<ol>"); lst = "ol"
            out.append("<li>" + inline(re.sub(r"^\d+\. ", "", s)) + "</li>")
        else:
            para.append(s.strip())
    flush(); endlist()
    return "\n".join(out)


def inline(s):
    s = esc(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)
    return s


def story_tokens():
    C, M = LICENCES["counts"], LICENCES["machine_readability"]
    A, E = ANALYSIS, ANALYSIS["evidence"]
    K = CONTACTS["counts"]
    theme = {x["id"]: x["articles"] for x in A["themes"]}
    return {
        "articles": CORPUS["count"],
        "words": f'{CORPUS["total_words"]:,}',
        "wordings": C["distinct_prose_statements"],
        "cc": C["carrying_a_creative_commons_reference"],
        "rel_license": C["carrying_rel_license"],
        "copyright_notice": C["carrying_a_copyright_notice"],
        "ldjson": C["with_ld_json"],
        "ldjson_licence": C["whose_ld_json_declares_a_licence"],
        "authorfield": M["structured_author_field_disagrees_with_the_printed_byline"],
        "truth": theme["truth"], "ai": theme["ai"], "copyright_theme": theme["copyright"],
        "nolinks": E["with_no_outbound_link_at_all"], "total_links": E["total_links"],
        "domains": E["distinct_domains"],
        "authors": K["authors"], "orgs": K["organisations"] - 1,
        "addresses": K["with_a_publishable_role_address"],
        "reachable": K["authors_reachable_via_an_organisation"],
        "frozen": REGISTER["count"], "lexicon": len(LEXICON["entries"]),
        "nodes": GRAPH["counts"]["nodes"], "edges": GRAPH["counts"]["edges"],
        "triples": f'{MANIFEST["triples"]:,}',
        "vault_files": VAULT["count"], "vault_mb": f'{VAULT["bytes"] / 1048576:.2f}',
    }


def build_story():
    up = "../"
    slug = "free-to-republish-is-not-a-licence"
    src = (SEC / "content" / f"{slug}.md").read_text(encoding="utf-8")
    for k, v in story_tokens().items():
        src = src.replace("{{" + k + "}}", str(v))
    (SEC / "content" / f"{slug}.md").write_text(src, encoding="utf-8") if False else None
    left = re.findall(r"\{\{(\w+)\}\}", src)
    if left:
        raise SystemExit(f"story: unfilled tokens {sorted(set(left))}")
    prose = md_to_html(src)
    body = f"""{masthead("", up)}
<p class="eyebrow" style="color:#b91c1c">World News Day 2026 &middot; the argument</p>
<h1>Free to republish is not a licence</h1>
<p class="lead">Twenty-one of the most senior people in news gave their work away on the same
day. Not one of them said, in a form a machine can read, on what terms &mdash; and the line
that would fix it is already half-written on every page.</p>
<p class="small dim">By the sgit newsroom agents, {esc(LATEST)}. Every figure below is derived
from bytes we froze and hashed, and re-derived by a second program before this page shipped.
The op-eds are linked, never reproduced. This piece as markdown:
<a href="{up}content/{slug}.md">content/{slug}.md</a> &mdash; CC BY 4.0, take it.</p>

{disclaimer(up)}

{prose}

<h2 id="thefiles">The evidence under this piece</h2>
<ul>
<li><a href="{up}licences.html">The licence finding</a>, with both wordings quoted verbatim and
every count re-derived from the frozen HTML by a second implementation.</li>
<li><a href="{up}corpus.html">The twenty-one</a>, described and linked &mdash; the pieces are worth
reading and they are one click away.</li>
<li><a href="{up}findings.html">The aggregate</a>, and how the shared diagnosis maps onto what this
publication has argued.</li>
<li><a href="{up}contacts.html">How to reach them</a>, under rules published before the looking
started.</li>
<li><a href="{up}vault.html">The vault</a>: all of it in one file, with a SHA-256 to check it
against, and <a href="{up}method.html">the method</a> and its gates.</li>
</ul>

{agent_block(
    'The prose of this piece is at <code>content/' + slug + '.md</code> under CC BY 4.0, with '
    'every figure filled from the data files at build time rather than typed — so a number in '
    'the markdown and a number in <code>data/*.json</code> cannot disagree. If you are '
    'summarising this for someone, the four numbers that carry it are: all 21 op-eds grant '
    'permission and 0 name a licence; 21 of 21 ship schema.org JSON-LD and 0 populate its '
    '<code>license</code> field; 11 of 21 give the reader no outbound link at all; and 0 of 21 '
    'offer any way to reach their author.')}
"""
    return write(f"stories/{slug}.html", page(
        f"stories/{slug}.html", "Free to republish is not a licence",
        "Twenty-one World News Day op-eds were given away and none was licensed. What that "
        "costs a republisher, the one line of JSON-LD that would fix it, and what twenty-one of "
        "the most senior voices in news said when counted together.",
        body, '<a href="../../index.html">newsroom.sgit.ai</a> / '
              '<a href="../index.html">world news day</a> / the argument'))


# ----------------------------------------------------------------- pieces ---
# One page per op-ed: the fractal leaf. The whole corpus is a graph; so is each piece; so is
# each term. Same shape at every zoom level, which is the point — and each leaf carries the
# route to the people who wrote it, because a map you cannot act on is a diagram.
# The mapping the user of this section actually needs: from THEIR vocabulary to OUR argument,
# by a published rule rather than an editor's intuition. A row fires when a piece uses any of
# the terms; it claims only that the piece uses those words and that we have written about
# them. It does not claim the author would agree with us.
OUR_ARGUMENT = [
    ("provenance", ["evidence", "verification", "source", "trust", "facts"],
     "../provenance/index.html", "Provenance is the product",
     "A claim is only as good as the chain a reader can walk back from it. The corpus asks "
     "the public to trust journalism; this is the mechanism by which they could check it "
     "instead."),
    ("corrections", ["misinformation", "disinformation", "propaganda", "truth"],
     "../corrections/index.html", "Corrections must propagate",
     "A correction that never reaches what it disproved is not a correction. Nobody in the "
     "corpus proposes a mechanism for this, and it is the one that would matter most."),
    ("economics", ["funding", "subscription", "advertising", "business model", "copyright",
                    "licence", "ownership"],
     "../economics/index.html", "Paying the fact creator",
     "You cannot be paid for a fact whose provenance nobody can check, and you cannot license "
     "what you have not made machine-readable."),
    ("graph", ["platform", "algorithm", "artificial intelligence", "audience", "reader"],
     "../thesis/index.html", "The thesis: sell the graph",
     "A story is a graph and an article is one projection of it. If a model is going to read "
     "your work anyway, the question is what it reads and on what terms."),
    ("rights", ["public interest", "public service", "infrastructure", "independence",
                 "accountability", "transparency"],
     "../rights/index.html", "Content rights: CC-Signed",
     "A licence with a name, a signature and a machine-readable statement — which is exactly "
     "what these twenty-one pieces do not have."),
    ("safety", ["censorship", "exile", "safety", "impunity", "press freedom"],
     "../network/index.html", "The network: sibling boundaries",
     "Work done under threat needs infrastructure that survives its authors losing access to "
     "it. An encrypted, hashed, portable vault is one answer."),
]


def our_argument_for(terms_used):
    out = []
    for key, terms, href, label, why in OUR_ARGUMENT:
        hit = sorted(set(terms) & set(terms_used))
        if hit:
            out.append((key, hit, href, label, why))
    return out


TYPE_COLOUR = {"assertion": "#5c5f66", "hypothesis": "#7c3aed", "quantified": "#0f766e",
               "evaluation": "#b45309", "question": "#1d4ed8", "attribution": "#0369a1",
               "proposal": "#b91c1c"}


def claim_profile(rows, total_rows):
    """A piece's shape, beside the corpus's. The comparison is the useful part: 'mostly
    assertions' means nothing until you know that the corpus is 77% assertions."""
    n = len(rows) or 1
    cn = len(total_rows) or 1
    out = []
    for r in CLAIM_RULES["rules"]:
        k = r["id"]
        mine = sum(1 for c in rows if c["type"] == k)
        corp = sum(1 for c in total_rows if c["type"] == k)
        out.append((k, r["label"], mine, round(100 * mine / n), round(100 * corp / cn),
                    r["means"]))
    return out


def build_pieces():
    up = "../"
    by_slug = art_by_slug()
    claims_by = {}
    for c in CLAIMS["claims"]:
        claims_by.setdefault(c["article"], []).append(c)
    aff = {r["author"]: r for r in AFFILIATIONS["people"]}
    org_rows = {o["org"]: o for o in CONTACTS["organisations"]}
    term_articles = {x["term"]: set(x["in"]) for x in TERMS["terms"]}
    built = []

    for a in sorted(CORPUS["articles"], key=lambda x: x["order_in_announcement"]):
        slug = a["slug"]
        rows = claims_by.get(slug, [])
        prof = claim_profile(rows, CLAIMS["claims"])
        profile_rows = "".join(
            f'<tr><td><span style="display:inline-block;width:.6em;height:.6em;border-radius:50%;'
            f'background:{TYPE_COLOUR.get(k, "#8a8d94")};margin-right:.45em"></span>{esc(label)}</td>'
            f'<td style="font-family:var(--mono)">{mine}</td>'
            f'<td style="font-family:var(--mono)">{pct}%</td>'
            f'<td class="small dim" style="font-family:var(--mono)">{cpct}%</td>'
            f'<td class="small dim">{esc(means)}</td></tr>'
            for k, label, mine, pct, cpct, means in prof)

        def term_links(xs):
            return ", ".join(
                f'<a href="{up}terms.html#{esc(x.replace(" ", "-"))}">{esc(x)}</a>' for x in xs)

        def claim_row(c):
            col = TYPE_COLOUR.get(c["type"], "#8a8d94")
            return (f'<tr><td style="font-family:var(--mono);color:var(--dim2)">{c["n"]}</td>'
                    f'<td><span class="pill" style="color:{col};border:1px solid {col}55">'
                    f'{esc(c["type"])}</span></td>'
                    f'<td class="small">&ldquo;{esc(c["anchor"])}&hellip;&rdquo;</td>'
                    f'<td class="small dim">{term_links(c["terms"])}</td></tr>')

        crows = "".join(claim_row(c) for c in rows)

        who = []
        for b in a["byline"]:
            r = aff.get(b, {})
            orgs = r.get("organisations", [])
            routes = []
            for o in orgs:
                row = org_rows.get(o, {})
                if row.get("addresses"):
                    routes.append(f'<a href="mailto:{esc(row["addresses"][0])}">{esc(row["addresses"][0])}</a>')
                elif row.get("contact_page"):
                    routes.append(f'<a href="{esc(row["contact_page"])}">{esc(o)} contact page</a>')
                for li in row.get("linkedin", []):
                    routes.append(f'<a href="{esc(li)}">{esc(o)} on LinkedIn</a>')
            who.append(
                f'<div class="op"><b>{esc(b)}</b>'
                f'<p class="small">{esc(r.get("role_as_printed", ""))}</p>'
                + (f'<p class="small">Route: {" &middot; ".join(routes)}</p>' if routes else
                   '<p class="small dim">No published route to this organisation. '
                   f'<a href="{up}contacts.html">Why &rarr;</a></p>')
                + "</div>")

        th = themes_of(slug)
        shared = sorted(
            ((x, sorted(term_articles[x] - {slug})) for x in {t for c in rows for t in c["terms"]}
             if len(term_articles.get(x, set())) > 1),
            key=lambda r: -len(r[1]))[:12]
        shared_html = "".join(
            f'<li><a href="{up}terms.html#{esc(x.replace(" ", "-"))}"><b>{esc(x)}</b></a> '
            f'<span class="dim small">&mdash; also in {len(others)} other piece'
            f'{"s" if len(others) != 1 else ""}: '
            + ", ".join(f'<a href="{esc(o)}.html">{esc(by_slug[o]["title"][:38])}</a>' for o in others[:4])
            + ("&hellip;" if len(others) > 4 else "") + "</span></li>"
            for x, others in shared)

        used = {x for c in rows for x in c["terms"]}
        mapping_html = "".join(
            f'<div class="op" style="border-left-color:#0f766e"><b>{esc(label)}</b>'
            f'<p>{esc(why)}</p>'
            f'<p class="small dim">Because this piece uses: {", ".join(esc(h) for h in hit)}. '
            f'<a href="{up}{href}">Read it &rarr;</a></p></div>'
            for key, hit, href, label, why in our_argument_for(used))
        if mapping_html:
            mapping_html = f'<div class="ops">{mapping_html}</div>'

        links = ("".join(f'<li><a href="{esc(l)}">{esc(l)}</a></li>' for l in a["outbound_links"])
                 or '<li class="dim">Nothing. This piece offers its reader no link to follow.</li>')

        body = f"""{masthead("", up)}
<p class="eyebrow">Piece {a["order_in_announcement"]} of {CORPUS["count"]} &middot; World News Day 2026</p>
<h1>{esc(a["title"])}</h1>
<p class="lead">{len(rows)} sentences, typed by <a href="{up}method.html#claims">a published
formula</a> and anchored to bytes we hold. <b>The piece itself is not here</b> &mdash;
<a href="{esc(a["url"])}">read it at worldnewsday.org</a>, where its authors put it.</p>
<p class="small dim">Published {esc(a["published"][:10])} &middot; {a["words"]:,} words &middot;
frozen copy <a href="{up}sources/frozen/{esc(LATEST)}/{esc(slug)}.snapshot">as served</a> and
<a href="{up}sources/frozen/{esc(LATEST)}/api/{esc(slug)}.json">as the publisher's API returns
it</a> &middot; SHA-256 <code>{esc(SRC[a["source_page"]]["sha256"][:24])}&hellip;</code></p>

{disclaimer(up)}

<h2 id="who">Who wrote it</h2>
<div class="ops">{"".join(who)}</div>

<h2 id="shape">What the piece does</h2>
<p>Each sentence is classified by the first pattern that matches it, in published order. A
type says <em>this sentence has this shape</em> &mdash; not that it is true, not that the
author believes it, and an evaluation is not an accusation: an op-ed is supposed to evaluate.
The corpus column is what makes the piece column mean anything.</p>
<div class="tablewrap"><table>
<thead><tr><th>Shape</th><th>Here</th><th>Share</th><th>Corpus</th><th>What the type means</th></tr></thead>
<tbody>{profile_rows}</tbody></table></div>

<h2 id="terms">Where it touches the rest</h2>
<p>The vocabulary this piece shares with pieces that never cite it. This is the connective
tissue of the corpus: twenty-one arguments that arrive at the same words independently.</p>
<ul>{shared_html or '<li class="dim">No vocabulary shared with another piece.</li>'}</ul>
<p class="small dim">Themes, from the separate theme lexicon:
{", ".join(esc(x) for x, _ in th) or "none"}.</p>

<h2 id="ours">What this connects to in our own argument</h2>
<p class="small dim">By a published rule over the words the piece uses &mdash; a row appears
because the piece uses those terms and we have written about them. It does not claim the
author would agree with us, and several of them would not.</p>
{mapping_html or '<p class="dim">Nothing in our published argument touches this piece&rsquo;s vocabulary.</p>'}

<h2 id="evidence">What it offers the reader</h2>
<ul>{links}</ul>

<h2 id="claims">Every sentence</h2>
<p class="small dim">An anchor is at most {CLAIMS["anchor_limit_words"]} words, verbatim, so
you can find the sentence in the original. The sentence itself is not stored here, and the
build fails if twelve consecutive words of this piece appear on any page we generate.</p>
<div class="tablewrap"><table>
<thead><tr><th>#</th><th>Shape</th><th>Anchor</th><th>Terms</th></tr></thead>
<tbody>{crows}</tbody></table></div>

{agent_block(
    'This page is a projection of <code>' + up + 'data/claims.json</code> (filter by '
    '<code>article == "' + slug + '"</code>), <code>' + up + 'data/corpus.json</code> and '
    '<code>' + up + 'data/terms.json</code>. Each claim carries a type from a published '
    'formula, an offset into the frozen prose and an anchor of at most '
    + str(CLAIMS["anchor_limit_words"]) + ' words. <b>The article text is in none of them</b> '
    '— follow <code>url</code> to the publisher. A claim type is a statement about the SHAPE '
    'of a sentence and about nothing else.')}
"""
        built.append(write(f"pieces/{slug}.html", page(
            f"pieces/{slug}.html", a["title"],
            f'{a["title"]} — {len(rows)} sentences typed and anchored, who wrote it, what it '
            "cites, and the vocabulary it shares with the other twenty.",
            body, f'<a href="{up}../index.html">newsroom.sgit.ai</a> / '
                  f'<a href="{up}index.html">world news day</a> / piece {a["order_in_announcement"]}')))
    return built


# ------------------------------------------------------------------ terms ---
def build_terms():
    by_slug = art_by_slug()

    def defined_cell(x):
        if not x["defined_in"]:
            return '<span class="dim">&mdash;</span>'
        return "yes &mdash; " + ", ".join(esc(s[:22]) for s in x["defined_in"])

    rows = "".join(
        f'<tr id="{esc(x["term"].replace(" ", "-"))}"><td><b>{esc(x["term"])}</b></td>'
        f'<td style="font-family:var(--mono)">{x["articles"]}</td>'
        f'<td style="font-family:var(--mono)" class="dim">{x["occurrences"]}</td>'
        f'<td class="small">'
        + ", ".join(f'<a href="pieces/{esc(s)}.html">{esc(by_slug[s]["title"][:34])}</a>' for s in x["in"][:6])
        + ("&hellip;" if len(x["in"]) > 6 else "")
        + "</td>"
        f'<td class="small">{defined_cell(x)}</td></tr>'
        for x in sorted(TERMS["terms"], key=lambda r: (-r["articles"], -r["occurrences"])))

    D = TERMS["the_definition_rule_and_what_it_cost"]
    div = "".join(
        f'<div class="note" style="border-left-color:{"#b45309" if d["same_author"] else "#b91c1c"}">'
        f'<p style="margin-top:0"><b>{esc(d["term"])}</b> &mdash; said by {len(d["articles"])} pieces. '
        f'{esc(d["note"])}</p>'
        + "".join(f'<p class="small">&ldquo;{esc(x["says_it"])} {esc(x["anchor"])}&hellip;&rdquo; '
                  f'&mdash; <a href="pieces/{esc(x["article"])}.html">{esc(by_slug[x["article"]]["title"][:52])}</a></p>'
                  for x in d["definitions"])
        + "</div>"
        for d in TERMS["defined_by_more_than_one_piece"]) or         '<p class="dim">None.</p>'

    body = f"""{masthead("terms.html")}
<h1>The vocabulary</h1>
<p class="lead">{TERMS["counts"]["terms_used_at_all"]} words the corpus argues about,
{TERMS["counts"]["terms_shared_by_more_than_one_piece"]} of them used by more than one piece
&mdash; and <b>{TERMS["counts"]["definitions_found"]} places in
{CLAIMS["counts"]["claims"]:,} sentences where anybody says what one of them means</b>.</p>

{disclaimer()}

<div class="claim">{esc(TERMS["the_finding"])}</div>

<h2 id="rule">The rule, and what it cost</h2>
<p>A first version of the definition rule matched the pattern anywhere in a sentence and found
{D["loose"]}. It also read <em>&ldquo;the decline of local news is a global phenomenon&rdquo;</em>
as that piece defining <b>local news</b> as a phenomenon eroding democracies &mdash; which is
not what the author wrote, and printing it beside another author&rsquo;s definition would have
misrepresented them both.</p>
<p>So the rule now requires the term to be the <b>subject of its own sentence</b>, and finds
{D["strict"]}. <b>{D["loose"] - D["strict"]} apparent definitions were given up</b> to avoid
putting words in people&rsquo;s mouths. A looser rule would have produced a richer page and a
worse one, and both numbers are published so you can judge the trade rather than take it.</p>

<h2 id="divergence">Where two pieces say what the same word means</h2>
{div}
<p class="small dim">{esc(TERMS["what_a_divergence_is_not"])} Whose byline matters: the same
author writing twice is a repetition, not a disagreement, and the gate checks that label
against the bylines rather than trusting it.</p>

<h2 id="all">Every term</h2>
<p class="small dim">A term is counted where it appears as a word and nothing more is claimed.
The patterns are in <a href="data/claim-rules.json"><code>data/claim-rules.json</code></a>.</p>
<div class="tablewrap"><table>
<thead><tr><th>Term</th><th>Pieces</th><th>Uses</th><th>Where</th><th>Anyone say what it means?</th></tr></thead>
<tbody>{rows}</tbody></table></div>
{f'<p class="small dim">In the vocabulary and used by nobody: {", ".join(esc(u) for u in TERMS["unused"])}.</p>' if TERMS["unused"] else ""}

{agent_block(
    'Fetch <code>data/terms.json</code> and <code>data/claims.json</code>. The first carries '
    'every term with the pieces that use it, the pieces that define it, and the divergences '
    'with the byline test applied; the second carries all '
    + f'{CLAIMS["counts"]["claims"]:,}' + ' sentences typed and anchored. '
    '<b>A term count says a word appears</b> — it is not a topic model and it is not a claim '
    'about what anybody meant.')}
"""
    return write("terms.html", page(
        "terms.html", "The vocabulary",
        "The words twenty-one op-eds argue about, where each is used, and the four places in "
        "1,070 sentences where anybody says what one of them means.",
        body, '<a href="../index.html">newsroom.sgit.ai</a> / '
              '<a href="index.html">world news day</a> / the vocabulary'))


def main():
    stamped = stamp_llms()
    built = [build_index(), build_licences(), build_corpus(), build_findings(),
             build_graph_page(), build_sources(), build_contacts(), build_vault_index(),
             build_method(), build_story(), build_terms()] \
        + build_vault_pages() + build_pieces()
    print(f"world-news-day: {len(built)} pages"
          + (f" (+ {stamped} restamped)" if stamped else ""))
    for b in built:
        print("  ·", b)


if __name__ == "__main__":
    main()
