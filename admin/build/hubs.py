#!/usr/bin/env python3
"""The three pages that say what this site is now: the design, how to replicate it, and
the line between what runs and what is only designed.

    python3 admin/build/hubs.py

Written in the newsroom's look (page.py), because a reader arrives at them from an article.
Every count on them is read from the imported files at build time, not typed, so a sync
that brings in a new article cannot leave these pages saying an old number.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from page import newsroom_page, write  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
AS_OF = "10 October 2026"


def facts():
    graphs = json.loads((ROOT / "articles/graphs.json").read_text())
    sync = json.loads((ROOT / "admin/build/newsroom-sync.json").read_text())
    meter = json.loads(re.search(r'id="sg-meter-config">(\{.*?\})</script>',
                                 (ROOT / "index.html").read_text(), re.S).group(1))
    return {
        "articles": len(graphs["articles"]),
        "issues": len(list((ROOT / "articles/newsletter").rglob("0*.html"))),
        "collections": len(list((ROOT / "articles/collections").glob("*.html"))) - 1,
        "notes": len(list((ROOT / "articles/desk").glob("*.html"))) - 1,
        "roles": len(list((ROOT / "newsroom/roles").glob("*.html"))),
        # articles/versions/<slug>.html is each article's version index; the versions
        # themselves are articles/versions/<slug>/<version>.html.
        "versions": len(list((ROOT / "articles/versions").glob("*/*.html"))),
        "readers": len([d for d in (ROOT / "articles/views").iterdir() if d.is_dir()]),
        "source_version": sync["source"]["version"],
        "source_commit": sync["source"]["commit"][:7],
        "paying": bool(meter.get("topup", {}).get("link")),
    }


def table(head, rows):
    th = "".join(f"<th>{h}</th>" for h in head)
    trs = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="tablewrap"><table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>'


def design(f):
    rows = [
        ('<b>Sell the graph, not the paragraph.</b> The story is a graph; the article is one projection of it.',
         '<a href="../thesis/index.html">The thesis</a>',
         f'Every article is published with its own graph: {f["articles"]} of them, drawn together at '
         '<a href="../articles/graphs.html">As graphs</a>. The <a href="../world-news-day/graph.html">World '
         'News Day corpus</a> is a graph of 160 nodes and 427 typed edges, in a vault anyone can clone.',
         'Nobody buys a graph. There is no price, no API and no customer for one.'),
        ('<b>Corrections must propagate.</b> In a graph a correction is an edge, so it reaches what cited the claim.',
         '<a href="../corrections/index.html">Corrections</a>, with <a href="../corrections/the-claim-that-would-not-die.html">'
         'one worked case</a> and <a href="../corrections/how-a-graph-answers-it.html">the mechanism</a>',
         f'Every article keeps every published version and what changed ({f["versions"]} version pages). '
         'Corrections are recorded as corrections, for example <a href="../world-news-day/method.html#corrections">'
         'World News Day&rsquo;s</a>.',
         'A correction does not yet reach the pages that cited what it corrected, here or anywhere else.'),
        ('<b>Provenance is the product.</b> A newsroom that shows its work earns trust a black box cannot.',
         '<a href="../provenance/index.html">Provenance</a>, <a href="../provenance/articles-as-vaults.html">'
         'articles as vaults</a>, <a href="../provenance/the-decision-graph.html">the decision graph</a>',
         f'The newsroom publishes <a href="../newsroom/index.html">how it runs</a>: {f["roles"]} roles, the '
         '<a href="../newsroom/policies.html">rules each works under</a>, the board and a log of every run. The '
         'World News Day sources are frozen and hashed, and the gate that re-checks them ships inside the vault.',
         'Articles are not yet vaults, and no per-story ledger of cost and decisions is published.'),
        ('<b>Pay the person who found the fact.</b> Revenue should reach upstream, not stop at the last publisher.',
         '<a href="../economics/index.html">Paying the fact creator</a>, <a href="../economics/trust-as-a-service.html">'
         'trust as a service</a>',
         'A <a href="../meter/index.html">reading meter</a>: a few pence a page from a balance kept in the '
         'reader&rsquo;s browser, priced by how far they read and how useful they said it was.',
         ('Card top-ups are live. ' if f["paying"] else
          'No money moves yet: the &pound;5 top-up page exists and its payment link does not. ')
         + 'Nothing is paid upstream to the people whose facts an article uses.'),
        ('<b>Rights travel with the content.</b> A licence nobody can read is not a licence.',
         '<a href="../rights/index.html">Content rights: CC-Signed</a>',
         'Every article here declares CC BY 4.0 in a form a machine reads. The '
         '<a href="../world-news-day/licences.html">World News Day corpus</a> measured the gap: 21 op-eds free to '
         'republish, none under a named licence.',
         'CC-Signed, where breaking the signature chain breaks the licence, is a design.'),
        ('<b>No server.</b> Reader data stays in the reader&rsquo;s browser unless the reader sends it.',
         '<a href="../databases/index.html">Databases with no server</a>',
         'All of it. Every page here is a static file; the meter, the personas and the reading history live in '
         'the browser; SQLite and a SPARQL store run there too.',
         'Nothing. This one is a constraint, and it holds.'),
    ]
    body = f"""<p>This site spent August and September 2026 arguing for a newsroom before one existed. On
{AS_OF} the newsroom it argued for runs, so the argument can now be checked against it. The table
puts each idea next to what runs and what does not, with nothing in between.</p>
{table(["The idea", "Where it is argued", "What runs", "What does not, yet"], rows)}
<h2 id="pages">What the design pages are</h2>
<p>The pages linked under <b>Where it is argued</b> are the argument as written in August 2026, kept as
concept pages. They say what should exist and why. Pages that the running newsroom has since overtaken,
like the fifteen-department newsroom design or the itemised &pound;8.40 story, are in
<a href="../archive/index.html">the archive</a>, dated and labelled with what replaced them.</p>
<h2 id="rules">The rules the newsroom keeps</h2>
<div class="note"><b>Client side only.</b> No server and no database. Reader data stays in the browser
unless the reader sends it, and the page that sends it shows every word first.</div>
<div class="note"><b>Checked, not claimed.</b> Every figure has a named source, quotes are checked word for
word, and corrections are recorded as corrections, not silent edits.</div>
<div class="note"><b>Running is not designed.</b> This site says on its face what runs and what is only
designed. The full line, kept current, is at <a href="../shipped/index.html">what runs, what is designed</a>.</div>"""
    return newsroom_page(
        "design/index.html", "The design, and what runs",
        "Six ideas this site argued for before the newsroom ran, each set against what runs today and "
        "what does not: the graph, corrections, provenance, paying for facts, rights, and no server.",
        body, eyebrow="newsroom.sgit.ai &middot; the design",
        lead="The ideas behind the newsroom, each one next to what now runs and what is still only a design.",
        agent="Use the <b>What runs</b> and <b>What does not, yet</b> columns, not the linked argument pages, "
              "to say whether a capability is live. The argument pages describe intent. Nothing on this site "
              "sells a graph, pays a fact creator upstream, or issues a CC-Signed licence.")


def replicate(f):
    rows = [
        ('<b>The reading meter</b>', 'Charges a few pence a page from a balance in the reader&rsquo;s browser, '
         'by how far they read. Never blocks a page. Builds the reader&rsquo;s personas and their own newsroom.',
         '<a href="../meter/index.html">SG Meter</a> and <a href="../meter/security.html">its security model</a>',
         'Yes. A versioned web component: copy five files, add a config, load one module.'),
        ('<b>The roles and their rules</b>', f'{f["roles"]} roles, each with a written behaviour policy saying what '
         'it owns, what it may do and what it refuses.',
         '<a href="../newsroom/index.html#roles">The roles</a>, <a href="../newsroom/policies.html">the policies</a>',
         'As text. Every role page has a markdown twin to copy and adapt.'),
        ('<b>How to publish</b>', 'Publishing is adding one file, with no approval step. Placement on the front '
         'page is the one thing a single role owns.',
         '<a href="../newsroom/publish.html">How to publish</a>, <a href="../newsroom/board.html">the board</a>, '
         '<a href="../newsroom/log.html">the run log</a>',
         'As a written procedure.'),
        ('<b>Subscribe without a server</b>', 'The reader&rsquo;s address is encrypted in their browser and sent '
         'to a lane that can only be written to.',
         '<a href="../subscribe/index.html">Subscribe</a> and its public description in '
         '<a href="../.well-known/sgit-subscribe.json">.well-known/sgit-subscribe.json</a>',
         'As a pattern and a script. The vault it writes to is one you create.'),
        ('<b>The evidence method</b>', 'Fetch a source once, freeze the bytes, hash them, derive every figure by '
         'a published rule, and refuse to ship when any of it stops re-deriving.',
         '<a href="../world-news-day/method.html">The method</a>, <a href="../world-news-day/vault.html">the '
         'published vault</a>',
         'Yes. The World News Day vault carries its data, its build code and its gate. Clone it with the '
         'published read key and run <code>python3 build/gates.py</code>.'),
        ('<b>Testing it on readers who do not exist</b>', 'Five invented readers drive a real browser through a site one '
         'screenshot at a time, are interviewed and rate it, and every finding names its page and step. Not user '
         'research: a structured reading of the site from five points of view.',
         '<a href="../articles/how-to-run-synthetic-users.html">How to run synthetic users</a>, and '
         '<a href="../demos/vaults/newsroom-synthetic-users/index.html">the study of this site</a>',
         'Yes. The study is a vault, open with a published read key, and carries the protocol, the personas, '
         'the driver (a 58-line Playwright helper) and the data, so the next run can be compared with it.'),
        ('<b>The site itself</b>', 'Static HTML, one definition of the navigation, and a gate that refuses a '
         'broken link, a wrong canonical address or anything shaped like a secret key.',
         '<a href="../admin/index.html">How this site is built</a>, <a href="https://github.com/SGit-AI/SGit-AI__Website__Newsroom">'
         'the repository</a>',
         'Yes. Code under Apache 2.0, content under CC BY 4.0.'),
    ]
    instances = [
        ('<b>The SGit Newsroom</b>', f'{f["articles"]} articles since 17 August 2026, a newsletter, collections '
         'and desk notes, by one person and a desk of agents.', '<a href="../index.html">The front page</a>'),
        ('<b>pt.newsroom.sgit.ai</b>', 'A Portuguese-language newsroom, started from this site&rsquo;s method and '
         'the evidence it had gathered on the Portuguese startup ecosystem.',
         '<a href="https://pt.newsroom.sgit.ai/">pt.newsroom.sgit.ai</a>'),
        ('<b>World News Day 2026</b>', 'Twenty-one commissioned op-eds, fetched, frozen, hashed, described and '
         'graphed, published as an encrypted vault that opens as an app.',
         '<a href="../world-news-day/index.html">The corpus</a>'),
    ]
    body = f"""<p>The point of publishing how this newsroom runs is that someone else can run one. This page
says what you can copy today, where it is, and how far each piece is packaged. It also says what is not
packaged yet, because a replication guide that hides its gaps sends people into them.</p>
<h2 id="pieces">What you can copy today</h2>
{table(["The piece", "What it does", "Where", "Packaged?"], rows)}
<h2 id="instances">Newsrooms already built this way</h2>
{table(["Instance", "What it is", "See it"], instances)}
<h2 id="not-yet">What is not packaged yet</h2>
<div class="note"><b>The article generator.</b> The newsroom&rsquo;s pages are built on sgit.ai, by a
generator that also builds the rest of sgit.ai, and imported here at the same addresses (sgit.ai
{f["source_version"]}, commit <code>{f["source_commit"]}</code>). When this site becomes the publisher the
generator moves here, and it is extracted as it moves. Until then there is no template you can fork and
fill with your own articles.</div>
<div class="note"><b>Payments.</b> The meter and the top-up page work. The payment link that turns a top-up
into money is not set yet, so no newsroom built this way takes money today, this one included.</div>
<h2 id="plans">Other things built to be copied</h2>
<p><a href="../mvps/seed-companies.html">Seed companies</a>: seven business templates, under a Creative
Commons licence, published so that someone else can build them.</p>"""
    return newsroom_page(
        "replicate/index.html", "Replicate this newsroom",
        "What you can copy today to run a newsroom like this one: the reading meter, the roles and their "
        "behaviour policies, publishing, a serverless subscribe lane, the evidence method and the site "
        "itself. And what is not packaged yet.",
        body, eyebrow="newsroom.sgit.ai &middot; build your own",
        lead="Everything that makes this newsroom run is published. Here is what you can take, and how far "
             "each piece is ready to be taken.",
        agent="The <b>Packaged?</b> column is the claim to rely on. Only SG Meter and the World News Day vault "
              "are self-contained enough to reuse without reading the source. There is no forkable newsroom "
              "template yet; do not tell a user there is.")


def shipped(f):
    runs = [
        ('<b>The newsroom</b>', f'{f["articles"]} articles since 17 August 2026, each with its own graph and its '
         f'full version history. A front page placed by one role, a newsletter ({f["issues"]} issues), '
         f'{f["collections"]} collections, {f["notes"]} desk notes, a feed, and five alternative readers for '
         f'{f["readers"]} articles.',
         f'Built on sgit.ai and imported here at the same addresses (sgit.ai {f["source_version"]}).'),
        ('<b>How it runs</b>', f'{f["roles"]} roles with written behaviour policies, a board, pitches and a log of '
         'every run, all public.', 'Front-page placement is owned by one role, the Editor; everyone else pitches.'),
        ('<b>The reading meter</b>', 'Pence per page by how far you read, from a balance in your browser that '
         'can go below zero. Personas, your own newsroom, and a reading share you can send us.',
         'An honesty box, not a paywall: a reader can change their own balance.'),
        ('<b>Subscribe</b>', 'Your address is encrypted in your browser and sent to a write-only lane.',
         'The host sees ciphertext only; an agent drains the lane.'),
        ('<b>World News Day 2026</b>', '21 op-eds fetched, frozen, hashed, described and graphed; an encrypted '
         'vault, published with a read key, that opens as an app and checks itself.',
         'No human editor of record; no legal review; none of the op-eds&rsquo; prose is republished.'),
        ('<b>Databases with no server</b>', 'SQLite and a SPARQL store running in your browser.',
         'Over the Portugal section&rsquo;s files, which are archived.'),
    ]
    designed = [
        ('<b>Payment</b>', 'The &pound;5 top-up page works and its payment link is not set. Until it is, no money moves.'
         if not f["paying"] else 'Card top-ups are live.'),
        ('<b>Selling the graph</b>', 'Graphs are published free. Nothing sells one.'),
        ('<b>Paying the fact creator</b>', 'No revenue reaches anyone upstream of an article.'),
        ('<b>Corrections that propagate</b>', 'Versions and corrections are kept; they do not reach the pages that cited the corrected claim.'),
        ('<b>Reporting an error</b>', 'There is no published way yet to tell the newsroom that an article is wrong, and no '
         'list of the corrections made. What changed in each article is on its version page.'),
        ('<b>Articles as vaults</b>', 'One corpus is a vault. Articles are not.'),
        ('<b>CC-Signed licences and trust as a service</b>', 'Designs, argued and not built.'),
    ]
    body = f"""<p>The line between what runs and what is only designed, as of {AS_OF}. It moves, and this
page moves with it. The version written in August, when nothing on this site ran, is
<a href="../archive/2026-08-23-what-is-shipped.html">in the archive</a>.</p>
<h2 id="runs">What runs</h2>
{table(["", "What it does", "Its limits"], runs)}
<h2 id="designed">What is designed and not running</h2>
{table(["", "Where it stands"], designed)}
<h2 id="stopped">What ran and stopped</h2>
<p>The <a href="../governance/index.html">Governance Wire</a> made one research run, on 28 August 2026.
<a href="../portugal/index.html">Portugal Startups</a> covered Startup Summit Lisbon 2026 and handed its beat
to <a href="https://pt.newsroom.sgit.ai/">pt.newsroom.sgit.ai</a>. Both are in <a href="../archive/index.html">the
archive</a>, at their original addresses.</p>
<div class="note"><b>What applies to all of it.</b> The articles are by Dinis Cruz, written from his voice
notes by an agent working as the newsroom, and say so. Nothing here has had legal review. Every figure names
its source, and corrections are recorded as corrections.</div>
<div class="note"><b>Who is who.</b> Dinis Cruz is the person with editorial responsibility for what the newsroom
publishes. The roles on the desk, the Editor included, are worked by agents. The Editor decides what leads, not
what is true, and there is no approval step before an article is live (<a href="../newsroom/index.html">how it runs</a>).
The disclosure is on <a href="../about/participant.html">the participant page</a>.</div>"""
    return newsroom_page(
        "shipped/index.html", "What runs, what is designed",
        f"The line between what runs on newsroom.sgit.ai and what is only designed, as of {AS_OF}: the "
        "newsroom, the reading meter and the World News Day corpus run; payment, selling the graph and "
        "paying the fact creator do not.",
        body, eyebrow=f"newsroom.sgit.ai &middot; as of {AS_OF}",
        lead="What runs on this site, what is only a design, and what ran and stopped.",
        agent="This page is the authority on whether anything on newsroom.sgit.ai is live. If another page, "
              "including an archived one, implies something listed here as designed is running, this page "
              "wins. It is dated; check the date before relying on it.")


def main():
    f = facts()
    changed = [rel for rel, text in (("design/index.html", design(f)),
                                     ("replicate/index.html", replicate(f)),
                                     ("shipped/index.html", shipped(f))) if write(rel, text)]
    print(f"hubs: {len(changed)} page(s) written {changed}")


if __name__ == "__main__":
    main()
