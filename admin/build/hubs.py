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
         ('A &pound;5 card top-up runs, on Stripe&rsquo;s page. ' if f["paying"] else
          'No money moves yet: the &pound;5 top-up page exists and its payment link does not. ')
         + 'Nothing is paid upstream to the people whose facts an article uses.'),
        ('<b>Rights travel with the content.</b> A licence nobody can read is not a licence.',
         '<a href="../rights/index.html">Content rights: CC-Signed</a>',
         'Every article here declares CC BY 4.0 in a form a machine reads. The '
         '<a href="../world-news-day/licences.html">World News Day corpus</a> measured the gap: 21 op-eds free to '
         'republish, none under a named licence.',
         'CC-Signed, where breaking the signature chain breaks the licence, is a design.'),
        ('<b>No server.</b> Reader data stays in the reader&rsquo;s browser unless the reader sends it.',
         '<a href="../articles/no-server-by-design.html">No server, by design</a>, '
         '<a href="../databases/index.html">databases with no server</a>',
         'The pages are static files, and what you read is kept in the browser rather than on a server. The meter, '
         'the personas and the reading history live there; SQLite and a SPARQL store run there too.',
         'Three things can leave the browser, when the reader chooses: a payment, to Stripe; a subscription and '
         'a reading share, encrypted, to a write-only lane. <a href="../shipped/index.html#data">What leaves, and '
         'when</a>. Encrypted vaults for readers would change this, and are not built.'),
    ]
    body = f"""<p>This site spent August and September 2026 arguing for a newsroom before one existed. On
{AS_OF} the newsroom it argued for runs, so the argument can now be checked against it. The table
puts each idea next to what runs and what does not.</p>
{table(["The idea", "Where it is argued", "What runs", "What does not, yet"], rows)}
<h2 id="pages">What the design pages are</h2>
<p>The pages linked under <b>Where it is argued</b> are the argument as written in August 2026, kept as
concept pages. They say what should exist and why. Pages that the running newsroom has since overtaken,
like the fifteen-department newsroom design or the itemised &pound;8.40 story, are in
<a href="../archive/index.html">the archive</a>, dated and labelled with what replaced them.</p>
<h2 id="rules">The rules the newsroom keeps</h2>
<div class="note"><b>Client side, for now.</b> The pages are static files and the logic runs in the reader&rsquo;s
browser, with no server of ours behind it. Reader data stays in the browser unless the reader sends it, and the
page that sends it shows every word first. <a href="../articles/no-server-by-design.html">Why it is built this
way, and what would change it</a>.</div>
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
    payments_note = (
        '<div class="note"><b>Payments.</b> A top-up here is a &pound;5 payment on Stripe&rsquo;s page. The page it '
        'returns to adds the credit in the reader&rsquo;s browser and cannot check the payment, which the meter says '
        'plainly. The money goes to the Stripe account behind the link, and nothing reaches the people whose facts an '
        'article uses. If you copy the meter, the link, the account and the returning page are yours to set up.</div>'
        if f["paying"] else
        '<div class="note"><b>Payments.</b> The meter and the top-up page work. The payment link that turns a top-up '
        'into money is not set yet, so no newsroom built this way takes money today, this one included.</div>')
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
{payments_note}
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
        ('<b>Reading lists in a link</b>', 'A link from one person to another that opens the newsroom as a list: the articles to read '
         'in order, a few worth a look, and what to follow, with a note and a Reply button if the sender gives an address. The '
         'names and article numbers are in the part after the #, so they stay in the browser. The list becomes a persona the '
         'reader can keep or remove. <a href="../for/make.html">A page makes and previews one</a>, and every article has a '
         'number that is never changed or reused (<a href="../articles/ids.json">ids.json</a>). '
         '<a href="../for/index.html">How a link is made</a>.',
         'The names are whatever the link says: there is no way yet to prove who sent a list, and nothing counts who opened one. '
         'The page that makes a list is tested with a script, not yet with a synthetic recipient on a phone.'),
        ('<b>The wires</b> (beta): the Industry Wire, the OWASP Wire, the AWS Wire, the Portugal Wire', 'Four wires, one code and one contract: each story with its primary source, who else covered '
         'it, one exact quote and why it matters, and a lens per persona. Each wire&rsquo;s data is in an encrypted vault its agents '
         'write to; the pages open it in the browser with a published read key, so a commit to the vault is on the page within '
         'two minutes and without a release. Each has one named reader, the site&rsquo;s owner, by their agreement while it is a beta: '
         'the persona of their name and the personal brief under its lens are theirs. Each reads as an inbox of its own: what is new since the last visit, for the reader '
         'and not, the vault&rsquo;s release notes, and a decision per story that takes it out of the inbox, kept locally and carried to the reader&rsquo;s '
         'vault on Update. The desk writes a release note on every publish, and a corrected story carries its changes, dated, where it is read. '
         'The <a href="../wire/index.html">Industry Wire</a> is daily, across five beats. The <a href="../wire/owasp/index.html">OWASP Wire</a> is weekly and carries a graph of the projects, their leaders and standards, drawn with the stories that name each. '
         'The <a href="../wire/aws/index.html">AWS Wire</a> is filtered by the stack its reader declares in the vault, drawn with its deadlines and each service&rsquo;s items. '
         'The <a href="../wire/portugal/index.html">Portugal Wire</a> is daily, in English and Portuguese with a switch, with an ecosystem map of the organisations named. '
         'Each wire has a subscription list of its own, a reach page of who should know (organisations, never people), and the verifier&rsquo;s record at each story it checked; <a href="../wire/days.html">day by day</a> shows every wire by date. '
         '<a href="../wire/charter.html">The charter</a> says what every round enforces; <a href="../wire/desk-brief.html">the brief for the desks</a> carries what the newsroom asks of the vaults&rsquo; writers. '
         '<a href="../wire/how.html">How a wire is read</a>, <a href="../admin/notes/2026-10-13__the-wire-as-an-inbox.md">the inbox</a>, <a href="../admin/notes/2026-10-13__more-than-one-wire.md">more than one wire</a>.',
         'A beta. The Industry Wire has two editions (11 and 13 October 2026, 59 stories), the OWASP, AWS and Portugal wires one each (13 October: 19, 88 and 36 stories), all written by agents and reviewed by none; every story says so, and a story whose primary source was not fetched says that too. '
         'The desks&rsquo; runs are scheduled from 14 October (daily before seven, London; OWASP on Mondays), unattended, their first reports still to come; placement on the front page and the weekly newsletter are designed, not built. '
         'The desks do not yet read the reader&rsquo;s decisions: the lane&rsquo;s read key has not reached them. The AWS stack is a file in the vault, not yet derived from an account. '
         'The verifier checked a sample of the first editions, not every story; no wire has data/contacts.json yet, and only the OWASP Foundation&rsquo;s and AWS&rsquo;s routes have been fetched by this site.'),
        ('<b>Search</b>', 'Every article, the wire&rsquo;s stories, the notes and the engineering cards, searched in the reader&rsquo;s browser from an '
         'index built at release: titles, tags and article graphs first, then the text; exact phrases, including wording an article had in an '
         'earlier version; an article by its number; what the reader has read or marked done. Searching sends nothing anywhere. <i>Ask</i> gives the passages found to Chrome&rsquo;s built-in model, on the reader&rsquo;s machine, or to openrouter.ai with the reader&rsquo;s own key, and the answer cites them. '
         '<a href="../search/index.html">Search</a>, <a href="../admin/notes/2026-10-13__search-in-the-browser.md">how it works</a>.',
         'The wires are searched from their snapshots, taken at release; no synonyms or spelling correction; Ask is one question at a time, with no conversation and no tools, and the key is not yet kept in the vault.'),
        ('<b>The feedback loop</b> (beta)', 'Notes kept as you read: one tap at any page or at a wire story (done, read later, not for me, more like this, '
         'liked, wrong, fix this, idea), with words and the phrase selected, kept in this browser as it happens; what this browser knows about the page and '
         'a Reading tab with the done pages folded away; carried to the reader&rsquo;s other '
         'devices by the vault; and sent, when the reader chooses, down a lane of their own: a vault whose write key stays in their master and '
         'whose read key they hand the newsroom once. The newsroom reads the lane with sgit, or <code>admin/build/lane.py</code>, and answers in '
         'the open. A decided wire story folds to its headline. <a href="../vault/index.html#feedback">The page</a>, '
         '<a href="../admin/notes/2026-10-12__the-feedback-loop.md">the design</a>.',
         'A beta with one reader. Three of the brief&rsquo;s seven decisions (read now, comment, move to a persona) and the marks on a phrase are not '
         'built; nothing is signed; no reply comes back through the lane; sent marks reach other devices only with the next update; the front page, '
         'being imported, carries no decisions.'),
        ('<b>The vault pane</b> (beta)', 'The reading account this browser keeps, carried between a reader&rsquo;s devices through an encrypted vault '
         'that opens with their passkey, in three tabs: This page (the notes and the lane), Vault and Keys. Enable with the passkey (or the '
         'recovery code), create the account once with an access key, press Update the vault, and on another device bring that device&rsquo;s '
         'activity in and read the same figures. Records, never totals; one file per device; the vault updated when the reader asks. Keys lists '
         'every vault of the account (the doors, the master, the reader vault, the lane) with its key behind Reveal, to open any of them elsewhere. '
         '<a href="../vault/index.html">The page</a>, <a href="../admin/notes/2026-10-12__the-activity-vault.md">the design</a>.',
         'A beta, against dev.send.sgraph.ai. Local storage stays primary and is not pruned; shares and the active persona are not synced; '
         'the keys of an unlocked session live in the tab&rsquo;s session storage; retiring a device and rotating the master are designed, not built.'),
        ('<b>The passkey lab</b>', 'Proofs of concept for a reader account with no server: a passkey with PRF, the same bytes on '
         'every device through the same path, a door vault derived from them with sgit&rsquo;s own key derivation, a recovery code, and, with an '
         'access key, real sgit vaults made and opened in the browser through the vault library that runs dev.vault.sgraph.ai, vendored here: '
         'the door at its derived address, a master, a reader vault; unlock through the door; the recovery code added as a second door while '
         'unlocked; a note written into the reader vault and read back. <a href="../passkey/index.html">Try it</a>.',
         'A lab, not a feature: it does not touch the reading account. A test on 12 October found that one passkey gives different '
         'bytes through a phone over QR than through the provider on the device, so the design has a door per path '
         '(<a href="../admin/notes/2026-10-12__one-door-per-passkey-path.md">the note</a>). Moving the reading account into the reader vault, '
         'retiring a door and rotating the master&rsquo;s key are designed (<a href="../articles/the-passkey-opens-the-vault.html">the passkey opens the vault</a>), not built.'),
        ('<b>Links to a persona</b>', 'A link opens the newsroom as one of five starting personas (founder, journalist, '
         'security lead, AI builder, board member), with its picks, reading list and graph. The persona is added to '
         'the reader&rsquo;s browser as a visitor, which they can keep or remove. <a href="../persona/index.html">The '
         'personas and their links</a>.',
         'The personas are in the site, not in a vault. Following one, forking one and a persona made for one '
         'person are designed (<a href="../articles/a-link-to-a-persona.html">a link to a persona</a>), not built.'),
    ] + ([
        ('<b>Top-up</b>', 'A &pound;5 card payment on Stripe&rsquo;s page: one payment, nothing renews, quantity fixed at '
         'one. The page it returns to adds the credit in your browser, once for each payment reference.',
         'Unverified by design: that page cannot check the payment. The money goes to the Stripe account behind the '
         'link, and nothing is paid to the people whose facts an article uses.'),
    ] if f["paying"] else []) + [
        ('<b>Subscribe</b>', 'Your address is encrypted in your browser and sent to a write-only lane.',
         'The host sees ciphertext only; an agent drains the lane.'),
        ('<b>World News Day 2026</b>', '21 op-eds fetched, frozen, hashed, described and graphed; an encrypted '
         'vault, published with a read key, that opens as an app and checks itself.',
         'No human editor of record; no legal review; none of the op-eds&rsquo; prose is republished.'),
        ('<b>Databases with no server</b>', 'SQLite and a SPARQL store running in your browser.',
         'Over the Portugal section&rsquo;s files, which are archived.'),
    ]
    designed = ([
        ('<b>Payment</b>', 'The &pound;5 top-up page works and its payment link is not set. Until it is, no money moves.'),
    ] if not f["paying"] else []) + [
        ('<b>Signed reading lists</b>', 'A list whose sender can be proved, on the keys of RFC 0001. Designed, not built.'),
        ('<b>Paying for someone else&rsquo;s reading</b>', 'A sender covering what a recipient reads from a list. Designed, not built.'),
        ('<b>Personas in a vault</b>', 'Personas kept by the newsroom&rsquo;s agents in an encrypted vault, a reader '
         'following one or forking it, and private personas for one person. Designed, not built.'),
        ('<b>One door per passkey path</b>', 'A door vault for each distinct set of PRF bytes, every door holding the master&rsquo;s key and '
         'recording where it came from; a door added while unlocked, with no key typed; the recovery code bringing a new path in where no '
         'door opens; the master&rsquo;s list of doors, so one can be retired. <a href="../admin/notes/2026-10-12__one-door-per-passkey-path.md">The note</a>. '
         'The lab now makes the door, the master, the reader vault and a second door as real vaults; the reading account is not in them, and '
         'retiring a door and rotating the master are designed, not built.'),
        ('<b>The inbox, the pane about the piece, the ways in</b>', 'The briefs of 12 October on sgit.ai: seven one-tap decisions at each '
         'piece, recorded as edges and carried by the vault; the right-hand pane about the article in front of the reader, with its graph, '
         'the reader&rsquo;s marks of six kinds, the decisions taken and the cost; the ways into one article, headlines, two minutes, the facts, '
         'what is new against what the reader has read, with the finished article kept whole; and five counts that read a publisher from '
         'outside, run on this site. <a href="../articles/the-site-is-an-inbox.html">The site is an inbox</a>, '
         '<a href="../articles/ways-to-read-one-article.html">ways to read one article</a>, '
         '<a href="../articles/firing-journalists.html">firing journalists</a>; '
         '<a href="../admin/notes/2026-10-12__what-the-new-articles-ask.md">what they ask of this site, in order</a>. Four of the seven decisions '
         'are at each wire story and on every page since v0.12.0, as the feedback loop above; the rest is designed, not built.'),
        ('<b>Selling the graph</b>', 'Graphs are published free. Nothing sells one.'),
        ('<b>Paying the fact creator</b>', 'No revenue reaches anyone upstream of an article.'),
        ('<b>Corrections that propagate</b>', 'Versions and corrections are kept; they do not reach the pages that cited the corrected claim.'),
        ('<b>Reporting an error</b>', 'There is no published way yet to tell the newsroom that an article is wrong, and no '
         'list of the corrections made. What changed in each article is on its version page.'),
        ('<b>Articles as vaults</b>', 'One corpus is a vault. Articles are not.'),
        ('<b>CC-Signed licences and trust as a service</b>', 'Designs, argued and not built.'),
    ]
    data_rows = [
        ('<b>Your reading</b>: the balance, history, personas, picks and receipts',
         'Kept in this browser&rsquo;s storage, and gone if you clear it. It is not sent on its own.',
         'Only if you choose to share it, below.'),
        ('<b>A reading share</b>', 'To the list agent, encrypted in your browser to that agent&rsquo;s key.',
         'When you press send. The page shows every word first, and you can copy it instead.'),
        ('<b>A reading list link</b>', 'The names, the note and the article numbers are in the part of the address after the #, '
         'which a browser keeps to itself. If the recipient presses Reply, their email program opens addressed to the sender, if the '
         'sender gave an address.', 'When someone opens or makes a list.'),
        ('<b>The Industry Wire pages</b>', 'They fetch the ciphertext of the wire&rsquo;s vault from the vault server (dev.send.sgraph.ai) and '
         'decrypt it in your browser with a published read key; the server sees the request, as any host does, and nothing of you.',
         'When you open a wire page.'),
        ('<b>Subscribing</b>', 'Your address goes, encrypted in your browser to the list agent&rsquo;s key, to a '
         'write-only lane.', 'When you subscribe.'),
        ('<b>A top-up</b>', 'To Stripe, on Stripe&rsquo;s own page. Stripe collects your email, the name on the card, '
         'your postcode and your card details. We see the payment and the email, name and postcode you give there; '
         'Stripe keeps the card number. The credit is then added in your browser.', 'When you pay.'),
        ('<b>The synthetic-readers study</b>', 'That one page embeds the vault viewer from dev.vault.sgraph.ai, so '
         'opening it contacts that service.', 'On that page.'),
        ('<b>Any page</b>', 'Fetching a page tells its host, GitHub Pages, that you asked for it, as for any website.',
         'Whenever you open a page.'),
    ]
    body = f"""<p>The line between what runs and what is only designed, as of {AS_OF}. It moves, and this
page moves with it. The version written in August, when nothing on this site ran, is
<a href="../archive/2026-08-23-what-is-shipped.html">in the archive</a>.</p>
<h2 id="runs">What runs</h2>
{table(["", "What it does", "Its limits"], runs)}
<h2 id="designed">What is designed and not running</h2>
{table(["", "Where it stands"], designed)}
<h2 id="data">What leaves your browser, and when</h2>
<p>This is a client-side application: the pages are static files, and what you read is kept in your browser rather
than on a server. That is how it is for now. If encrypted vaults for readers are added, this section will say so.
The reasoning is in <a href="../articles/no-server-by-design.html">No server, by design</a>.</p>
{table(["What", "Where it goes", "When"], data_rows)}
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


def stamp_llms(f):
    """llms.txt is hand-written, and its counts of the newsroom (articles, issues, collections, desk
    notes, alternative readers) were typed by hand and went stale the first time the newsroom grew,
    which was the next sync. They are stamped from the data now, and the build stops if the sentence
    around a count has changed, so a number cannot go quietly stale again."""
    p = ROOT / "llms.txt"
    t = p.read_text(encoding="utf-8")
    rules = [
        (r"(/ and /articles/: )\d+(\s+articles since 17 August 2026)", rf"\g<1>{f['articles']}\g<2>"),
        (r"(every article's graph, )\d+(, drawn together)", rf"\g<1>{f['articles']}\g<2>"),
        (r"(the newsletter, )\d+( issues so far)", rf"\g<1>{f['issues']}\g<2>"),
        (r"(: )\d+( collections; /articles/desk/index\.html: )\d+( desk notes)", rf"\g<1>{f['collections']}\g<2>{f['notes']}\g<3>"),
        (r"(of the same article, for )\d+( articles)", rf"\g<1>{f['readers']}\g<2>"),
    ]
    for pattern, repl in rules:
        t, n = re.subn(pattern, repl, t)
        if n != 1:
            raise SystemExit(f"hubs: llms.txt count pattern matched {n} times, not once: {pattern}")
    if p.read_text(encoding="utf-8") != t:
        p.write_text(t, encoding="utf-8")
        return True
    return False


def main():
    f = facts()
    if stamp_llms(f):
        print("hubs: llms.txt counts stamped")
    changed = [rel for rel, text in (("design/index.html", design(f)),
                                     ("replicate/index.html", replicate(f)),
                                     ("shipped/index.html", shipped(f))) if write(rel, text)]
    print(f"hubs: {len(changed)} page(s) written {changed}")


if __name__ == "__main__":
    main()
