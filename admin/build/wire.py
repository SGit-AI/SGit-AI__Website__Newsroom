#!/usr/bin/env python3
"""The wires: for each wire, three pages that read its vault in the browser, and a snapshot for agents.

    python3 admin/build/wire.py                                        # the pages, from the recorded configs
    python3 admin/build/wire.py --from /path/to/a/clone/of/the/wire/vault   # also refresh wire/snapshot.json
    python3 admin/build/wire.py --from owasp=/path/to/a/clone --from aws=/path/to/a/clone   # the other wires' snapshots

A wire's data is not on this site. It is in an encrypted sgit vault that the wire's agents write to, one config per wire
in admin/build/wire-vault*.json (endpoint, vault id, read key, and the named readers who agreed to a persona of their
name being public). The pages open the vault in the reader's browser with the published read key (wire/vault-reader.js,
vendored from sgit.ai) and draw it (wire/wire.js, shared by every wire). A commit to the vault is on the page within two
minutes, with no release of this site; the site owns the presentation and the vault owns the news. That is the pattern
sgit.ai uses for its own documentation, applied to a feed.

The Industry Wire is wire/ (admin/build/wire-vault.json, no slug); every other wire is wire/<slug>/ (wire-vault.<slug>.json).
All of them follow the same contract (wire/how.html); a vault may add a map (entities and the stories naming them) or a
stack (services and deadlines), which the page draws when they are there.

wire/<slug>/snapshot.json is what was in the vault when this site was last released: the edition, its headlines with
their primary links, each story's edition and dated corrections, the desk's latest release note, and the counts. It is
public data derived from public sources, it is what the pages show when the vault cannot be reached, and it is what an
agent without a browser reads first; the vault itself is one `sgit clone` away with the read key. It is refreshed only
when --from names a clone, so the snapshot's date says when it was taken.
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from page import newsroom_page, write, esc, HOST  # noqa: E402
from md import render, front_matter  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
BUILD = ROOT / "admin/build"
BRIEF = "admin/notes/2026-10-13__the-wire-as-an-inbox.md"
INDUSTRY_ABOUT = ("Once a day, what happened in the five areas this newsroom writes about: building with AI and models, AI business models, "
                  "open source, cybersecurity, and risk, governance and regulation.")


def load_configs():
    """Every wire, the Industry Wire first: admin/build/wire-vault.json and wire-vault.<slug>.json."""
    cfgs = []
    for f in sorted(BUILD.glob("wire-vault*.json")):
        cfg = json.loads(f.read_text(encoding="utf-8"))
        cfg.setdefault("slug", "")
        cfg.setdefault("name", "The Industry Wire")
        cfg["dir"] = "wire/" + (cfg["slug"] + "/" if cfg["slug"] else "")       # the pages' folder, from the site root
        cfg["up"] = "../" * cfg["dir"].count("/")                               # from the pages to the site root
        cfg["rel"] = "../" if cfg["slug"] else ""                               # from the pages to wire/ (the shared code)
        cfg["snapshot"] = ROOT / cfg["dir"] / "snapshot.json"
        # the named readers: people who agreed, on a recorded date, to a persona and a personal brief in a public vault
        cfg["named"] = [x for x in cfg.get("named_readers", []) if isinstance(x, dict) and x.get("persona") and x.get("agreed")]
        cfg["named_names"] = ", ".join(x.get("name", x["persona"]) for x in cfg["named"]) or "nobody yet"
        cfgs.append(cfg)
    cfgs.sort(key=lambda c: (c["slug"] != "", c["slug"]))
    return cfgs


CFGS = load_configs()
EYEBROW = "Industry news, read from a vault · beta"
REACH = json.loads((BUILD / "wire-reach.json").read_text(encoding="utf-8"))     # the organisation routes this site found, per wire
CHARTER_MD = ROOT / "admin/notes/2026-10-13__the-wires-charter.md"
BRIEF_MD = ROOT / "wire/desk-brief.md"


PUB_KEYS = ("endpoint", "vault_id", "read_key", "ref_ttl_s", "clone", "named_readers", "slug", "up", "name")


def config_block(cfg, **extra):
    pub = {k: cfg[k] for k in PUB_KEYS if k in cfg}
    pub.update(extra)
    return f'<script type="application/json" id="wire-config">{json.dumps(pub)}</script>'


def wires_public():
    """Every wire's public config, for the pages that read every vault (day by day)."""
    return [{k: c[k] for k in PUB_KEYS if k in c} for c in CFGS]


def wires_strip(cfg, up=None):
    """The strip naming every wire, with the current one marked, and the pages they share."""
    up = cfg["up"] if up is None else up
    links = "".join(f'<a href="{up}{c["dir"]}index.html"{" aria-current=page" if c is cfg else ""}>{esc(c["name"])}</a>' for c in CFGS)
    shared = f'<a href="{up}wire/days.html">Day by day</a><a href="{up}wire/charter.html">The charter</a><a href="{up}wire/desk-brief.html">For the desks</a>'
    return f'<p class="wires">The wires: {links} · {shared}</p>'


def subscribe_block(cfg):
    """Subscribe to this wire alone: the newsletter's lane and envelope, with X-SGit-List naming the wire (wire/subscribe.js)."""
    lst = f"wire:{cfg['slug'] or 'industry'}"
    return f"""<section class="wire-sub" id="subscribe"><b>Subscribe to {esc(cfg["name"])} alone.</b> The desk&rsquo;s release note, by email, when it publishes: one list per wire, kept by the same agent and the same lane as <a href="{cfg["up"]}subscribe/index.html">the newsletter</a>. Your address is encrypted in this browser to that agent&rsquo;s key and dropped into a write-only lane; nothing is stored on this site, and the request carries <code>X-SGit-List: {esc(lst)}</code> so the agent keeps it apart.
<form data-wire-subscribe data-list="{esc(lst)}" data-name="{esc(cfg["name"])}" novalidate>
<input name="email" type="email" autocomplete="email" placeholder="you@example.com" required aria-label="Email">
<input name="website" type="text" tabindex="-1" autocomplete="off" aria-hidden="true">
<button class="btn primary" type="submit">Subscribe</button>
<label class="consent"><input type="checkbox" name="consent"> Keep this address in the subscribe vault and email me {esc(cfg["name"])}&rsquo;s release notes.</label>
<p class="sub-status" aria-live="polite"></p>
<a class="sub-mailto" hidden href="#">Send the same request as an email instead</a>
</form>
<p class="sub-done" hidden>Sent, encrypted. The agent that keeps the list will file it; the first release note after that reaches you by email.</p>
</section>
<script src="{cfg["rel"]}subscribe.js" defer></script>
"""


def snapshot_html(snap):
    if not snap:
        return '<section id="wire-snapshot" class="snapshot" hidden><p>No snapshot has been taken yet.</p></section>'
    beats = "".join(
        f'<h3>{esc(b["label"])}</h3><ol>' + "".join(
            f'<li>{"<a href=%s target=_blank rel=noopener>%s</a>" % (json.dumps(s["primary_url"]), esc(s["headline"])) if s.get("primary_url") else esc(s["headline"])}'
            f' <span class="dim">· {esc(s["date"])}{(" · " + esc(s["publisher"])) if s.get("publisher") else ""}</span></li>'
            for s in b["stories"]) + "</ol>"
        for b in snap["beats"])
    return (f'<section id="wire-snapshot" class="snapshot" hidden><h2>What was in the vault at {esc(snap["release"])}</h2>'
            f'<p class="dim">Edition of {esc(snap["edition"])}: {snap["counts"]["stories"]} stories, {snap["counts"]["sources"]} sources. '
            f'A snapshot, kept for when the vault cannot be reached and for readers without a script; the live edition is the vault.</p>{beats}</section>')


def loader(cfg, kind, **extra):
    return f"""<div id="wire-status" class="wire-status" hidden></div>
<div id="wire-mount" data-wire="{kind}"><p class="dim">Opening the vault&hellip;</p></div>
{config_block(cfg, **extra)}
<script type="module">
import {{ wire }} from '{cfg["rel"]}./wire.js';
wire({{ mount: document.getElementById('wire-mount') }});
</script>
"""


def edition_page(cfg, snap):
    counts = (snap or {}).get("counts", {})
    latest = (snap or {}).get("latest_release") or {}
    meta = (snap or {}).get("wire") or {}
    up, name, named = cfg["up"], cfg["name"], cfg["named_names"]
    current = (f"The current edition is of {esc(snap['edition'])}: {esc(snap['kind'])}. " if snap and snap.get("edition") and snap.get("kind") else "")
    about = cfg.get("about") or INDUSTRY_ABOUT
    history = ("The first edition, of 11 October, was a week&rsquo;s catch-up; the editions since add what happened and keep the earlier stories, so the page is the whole wire so far, not one day of it."
               if not cfg["slug"] else "Each edition adds what happened and keeps the earlier stories, so the page is the whole wire so far, not one edition of it.")
    extras = ""
    if counts.get("map_entities"):
        extras += (f"<p><b>The map.</b> The vault carries a graph of {counts['map_entities']} entities (<code>data/map.json</code>: each with its aliases, its facts, its leaders and the standards it maps to), and the page draws it under the bar: "
                   "each entity with the stories whose named entities match it, so a story is read beside what it is about. Nothing is computed beyond that match; the facts are the vault&rsquo;s.</p>\n")
    if counts.get("stack_services"):
        extras += (f"<p><b>The stack.</b> The vault carries the {counts['stack_services']} services its named reader runs (<code>data/stack.json</code>: each with its aliases, what to watch it for, and {counts.get('deadlines', 0)} dated deadlines), "
                   "and the join turns each service into a concern, so under that reader&rsquo;s lens a story reaches them when it names a service they run and is withheld, with the reason, when it does not. "
                   "The page draws the deadlines at the top of the edition with the days left, and each service with the items that touched it. To change what reaches the reader, the desk edits the file in the vault; nothing on this site changes.</p>\n")
    body = f"""{wires_strip(cfg)}
{loader(cfg, "edition")}
<noscript><p>The edition is read from an encrypted vault in your browser, which needs a script. Below is what the vault held at the last release of this site.</p></noscript>
{snapshot_html(snap)}
<h2 id="about">What this is</h2>
<div class="note"><b>A beta.</b> {esc(name)} is an experiment run in the open: agents find and write the stories, an encrypted vault holds them, and this page draws them. It has one named reader, {esc(named)}, who runs this site and has agreed to be one while the wire is a beta; the persona of that name and the personal brief under its lens are theirs, and they are public like everything else in the vault. Expect gaps, repeats and stories whose primary source was never fetched, each marked as such, and expect the shape of the edition to change.</div>
<p>{about} For every story: where it came from, who else covered it, one exact quote with its source, and why it matters. The stories are found, grouped and written by agents, from a registry of sources with a licence tier each (<a href="sources.html">the sources</a>), and every story says what it is: <em>ai-generated, unreviewed</em> until a person has reviewed it. {current}{history}</p>
<p><b>Corrections propagate.</b> When the desk fetches a primary source it could not reach, or finds a story wrong, it corrects the story in the vault and records the correction, dated, in the story&rsquo;s own <code>changes</code>; this page draws them under the story, in blue, for as long as the vault keeps them, and the edition&rsquo;s header carries the desk&rsquo;s note of what was corrected. The vault&rsquo;s release notes name the stories added and updated in each publish, and the page flags them <em>Updated</em>. A corrected story is corrected where it is read, which is <a href="{up}corrections/index.html">the argument this site makes</a> of every publication.</p>
<p><b>Read it as an inbox.</b> The bar above the stories says what is new since your last visit, how much of it is for you and how much is not under the lens you read as, and what the wire&rsquo;s desk says changed in the vault: its release notes, one per publish (<code>data/releases.json</code>), newest first since your last visit. At each story, one tap: <em>Done</em>, <em>Read later</em>, <em>Follow up</em>, <em>Not for me</em>, <em>More like this</em> or <em>Wrong</em>; the story leaves your inbox, and the filters bring it back. Your decisions and what you have seen are kept in this browser first and reach your own vault when you press <em>Update the vault</em>; until then the bar and the Vault button say what is only here. Each wire keeps its own inbox, its own visit and its own lens. <a href="{up}{BRIEF}">How it works</a>.</p>
<p><b>Read as someone.</b> The same stories reach different readers. Choose a persona and the edition shows what reached them, through which concern, and what was withheld, with the reason. That join is recorded in the vault by the wire&rsquo;s own code (<code>pipeline/join.py</code>), not computed here; the page shows the record. If you are reading this site as one of its personas, the lens follows it.</p>
{extras}<p><b>Who should know.</b> <a href="reach.html">The reach page</a> lists who this wire concerns and how to reach them, by organisation route only, under <a href="{up}world-news-day/data/contact-rules.json">the contact rules</a> this site publishes: what this site found on the organisations&rsquo; own contact pages, and what the vault carries. <a href="{up}wire/charter.html">The charter</a> says what every agent in the chain enforces; <a href="{up}wire/days.html">day by day</a> shows every wire&rsquo;s releases and stories by date.</p>
{subscribe_block(cfg)}<p><b>Where it comes from.</b> The data is not on this site. It is in an encrypted vault that the wire&rsquo;s agents write to, and this page opens it in your browser with a published read key: {esc(cfg["vault_id"])} on {esc(cfg["endpoint"].replace("https://", ""))}. A commit to the vault is on this page within two minutes, with no release of the site. Anyone can read the whole vault, and its history, with <code>{esc(cfg["clone"])}</code>. <a href="how.html">How the wire works</a> has the contract and the wire&rsquo;s own documents, read from the same vault.</p>
"""
    agent = (f"{name} on newsroom.sgit.ai ({cfg['dir']}), one of {len(CFGS)} wires that share one code and one contract. "
             "The edition page reads as an inbox: what is new since the reader's last visit, for them and not under their lens, the vault's release notes (data/releases.json, wire-releases/v1"
             + (f", latest {latest['id']}: '{latest.get('title', '')}' at {latest.get('at', '')}), " if latest.get("id") else "), ")
             + f"and one decision per story kept as a note in the reader's browser and carried to their own vault on Update ({BRIEF}). "
             "Corrections propagate: a corrected story carries its changes[] ({at, what}) under the story and the edition's header carries the desk's corrections note; stories named updated by a release or by brief.updated_in_edition are flagged Updated. "
             f"The data is in a public-read sgit vault, not on this site: vault {cfg['vault_id']} on {cfg['endpoint']}, read key "
             f"{cfg['read_key']} (read-only, published on purpose). Clone it with `{cfg['clone']}` and read data/bundle.json (beats, stories, sources, personas, "
             f"brief, docs" + (", map" if counts.get("map_entities") else "") + (", stack" if counts.get("stack_services") else "") + "), data/deliveries.json (story × persona: reached or withheld, with the reason) and docs/*.md. "
             f"https://{HOST}/{cfg['dir']}snapshot.json holds the headlines, primary links, corrections and the latest release note as of this site's last release. "
             f"The wire is a beta; its named reader ({named}) agreed to be one, and the persona and personal brief of that name in the vault are theirs. Every story is marked ai-generated, unreviewed until a person reviews it"
             + (f"; {counts['primary_not_fetched']} of the {counts['stories']} stories in the edition of {snap['edition']} have a primary source the research agent did not fetch, and those stories say so"
                if snap and "primary_not_fetched" in counts else "")
             + (f"; {counts['corrected']} stories carry a dated correction from the desk." if counts.get("corrected") else "."))
    lead = (f"{meta.get('description') or about} Each story with where it came from and who else covered it, corrected where it is read, live from the wire's vault. A beta, with one named reader by their agreement."
            if cfg["slug"] else
            "What happened in building with AI, AI business, open source, cybersecurity and governance: each story with where it came from and who else covered it, corrected where it is read, live from the wire's vault. A beta, with one named reader by their agreement.")
    return newsroom_page(cfg["dir"] + "index.html", name,
                         f"{name}, in beta, read live from an encrypted vault that agents keep: every story with its primary source, who else covered it, one exact quote and why it matters, corrected where it is read, and a lens per persona showing what reached them and why.",
                         body, eyebrow=EYEBROW, crumbs=(() if not cfg["slug"] else (("The Industry Wire", "wire/index.html"),)),
                         lead=esc(lead) if cfg["slug"] else lead, agent=agent, head=f'<link rel="stylesheet" href="{cfg["rel"]}wire.css">\n', wide=True)


def sources_page(cfg):
    body = f"""{loader(cfg, "sources")}
<noscript><p>The registry is read from the wire&rsquo;s vault in your browser, which needs a script. Anyone can read it with <code>{esc(cfg["clone"])}</code>: it is <code>data/sources.json</code>.</p></noscript>
<h2 id="tiers">The tiers</h2>
<p>The wire&rsquo;s sources policy (<a href="how.html#docs/SOURCES-POLICY.md">in the vault</a>) gives each source a tier that decides what the wire may keep and show. <b>Tier A</b> is an open licence or public domain: the full text may be frozen, kept and shown. <b>Tier B</b> is quote and link: the bytes are frozen as evidence, and the public page carries a quote of 25 words or fewer with a link. <b>Tier C</b> is link only: headline, address and date, never the text. A source becomes <em>verified</em> when a person has opened its licence page; until then its tier is provisional. Outlets that keep appearing in coverage are proposed as sources, and a person confirms the tier.</p>
"""
    agent = f"The source registry of {cfg['name']}: data/sources.json in vault {cfg['vault_id']} ({cfg['clone']}). Each source has beats, a tier (A open licence, B quote and link, C link only), a licence and whether a person has verified it."
    return newsroom_page(cfg["dir"] + "sources.html", f"{cfg['name']}: the sources",
                         f"The registry of sources {cfg['name']} polls, with the licence tier that decides what may be kept and shown, read live from the wire's vault.",
                         body, eyebrow=EYEBROW, crumbs=((cfg["name"], cfg["dir"] + "index.html"),),
                         lead="Where the wire looks, and what each source's licence allows it to keep.", agent=agent, head=f'<link rel="stylesheet" href="{cfg["rel"]}wire.css">\n', wide=True)


def how_page(cfg):
    reads = ", ".join(f"<code>{esc(r)}</code>" for r in cfg["reads"])
    up, named = cfg["up"], cfg["named_names"]
    others = ", ".join(f'<a href="{up}{c["dir"]}how.html">{esc(c["name"])}</a>' for c in CFGS if c is not cfg)
    body = f"""<h2 id="site">How this site reads the vault</h2>
<p>The wire&rsquo;s data lives in an encrypted sgit vault that its agents write to, with the key that writes it held by them and not by this site. This site holds the vault&rsquo;s <b>read key</b>, published on purpose, and each wire page opens the vault in your browser: it derives the address of the vault&rsquo;s head pointer, fetches ciphertext from <code>{esc(cfg["endpoint"])}</code>, decrypts it with Web Crypto, walks the commit&rsquo;s tree and reads {reads}. Nothing from the vault is run; it is drawn as text, and the documents are rendered from their markdown by a renderer that escapes. The pointer is re-checked at most every two minutes, so a commit by the wire&rsquo;s agents is on the page within that, with no release of this site. Objects that cannot change are cached in the browser for good. {esc(cfg["name"])} is one of {len(CFGS)} wires on this site ({others}); they share one code (<code>wire/wire.js</code>), one contract, and one config each (<code>admin/build/wire-vault{("." + cfg["slug"]) if cfg["slug"] else ""}.json</code>).</p>
<div class="note"><b>The contract between the vault and this site.</b> Everything in the vault is public, including its history: a published read key cannot be withdrawn from anyone who has fetched the objects, so nothing private goes in it, not frozen tier-B bytes, not a reader&rsquo;s feedback, and not a brief meant for one person unless that person has agreed to it being public; those need a vault of their own. The wire&rsquo;s one named reader so far, {esc(named)}, has agreed while the wire is a beta, and the agreement is recorded with the date in the wire&rsquo;s config, which is also what tells the page to offer that lens. The pages rely on <code>data/bundle.json</code> having <code>beats</code>, <code>stories</code>, <code>sources</code>, <code>personas</code> and <code>brief</code> (edition, window, kind, status, editor_note, lead, threads, beats), on each story carrying <code>id</code>, <code>beat</code>, <code>headline</code>, <code>date</code>, <code>summary</code>, <code>quote</code>, <code>quote_source_url</code>, <code>primary</code>, <code>coverage</code>, <code>entities</code>, <code>why_it_matters</code>, <code>personas</code>, <code>confidence</code>, <code>status</code> and <code>primary_fetched</code>, and on <code>data/deliveries.json</code> rows of <code>story</code>, <code>persona</code>, <code>status</code>, <code>connections</code> and <code>withheld_reason</code>. When the vault has <code>data/releases.json</code> (<code>wire-releases/v1</code>: releases newest first, each with <code>id</code>, <code>at</code>, <code>edition</code>, <code>title</code>, <code>summary</code>, and the story ids <code>added</code>, <code>updated</code> and <code>withdrawn</code>), the edition shows the releases since the reader&rsquo;s last visit; the desk writes it on every publish (its runbook&rsquo;s step 11), as <a href="{up}{BRIEF}">the brief</a> asked, and the page still stands when it is missing. Three more fields are drawn when they are there and nothing breaks when they are not: a story&rsquo;s <code>changes</code>, a list of <code>{{at, what}}</code> that the desk appends to when it corrects the story, drawn under the story; the brief&rsquo;s <code>corrections</code>, the desk&rsquo;s note of what the edition corrected, in the edition&rsquo;s header; and the brief&rsquo;s <code>updated_in_edition</code>, story ids flagged <em>Updated</em> like the ids a release names. A story&rsquo;s <code>edition</code>, when it is not the current one, is said in the story&rsquo;s meta line. A vault that describes itself in <code>wire</code> (<code>id</code>, <code>title</code>, <code>beats</code>, <code>personal_persona</code>) offers every persona but the personal one as a public lens; without it the page offers the Industry Wire&rsquo;s six. A <code>map</code> (<code>title</code>, <code>intro</code>, <code>entities</code> each with <code>id</code>, <code>name</code>, <code>kind</code>, <code>aliases</code>, <code>facts</code>, <code>leaders</code>, <code>standards</code>, <code>notes</code>) is drawn as a list of entities, each with the stories whose <code>entities</code> values match its name or an alias. A <code>stack</code> (<code>persona</code>, <code>what</code>, <code>services</code> each with <code>id</code>, <code>name</code>, <code>aliases</code>, <code>runtime</code>, <code>watch</code>; <code>extra_concerns</code>; <code>deadlines</code> each with <code>what</code>, <code>date</code>, <code>then</code>, <code>source</code>; <code>later</code>) is drawn as the deadlines in the edition&rsquo;s header and each service with the items whose delivery to the stack&rsquo;s persona connects through the service&rsquo;s id. When the vault carries the verifier&rsquo;s records, <code>data/factcheck-&lt;date&gt;.json</code> (<code>wire-factcheck/v1</code> as <a href="{up}wire/desk-brief.html">the brief for the desks</a> asks: <code>checked_by</code>, <code>method</code>, <code>results</code> rows of <code>story</code>, <code>quote</code>, <code>date</code>, <code>version</code>, <code>independence</code>, <code>verdict</code>, <code>fix</code>, and <code>not_checked</code>), each row is drawn at its story and the file&rsquo;s words in the edition&rsquo;s header; a file with a prose <code>result</code> alone is drawn in the header as it is. When it carries <code>data/contacts.json</code>, the reach page draws it under the contact rules. A story&rsquo;s <code>status</code> is shown as written, so <em>ai-generated, unreviewed</em> stays on the page until the vault says otherwise. The commit message of the head is shown on every wire page.</div>
<p>To read it without this site: <code>{esc(cfg["clone"])}</code>. The read key is <code>{esc(cfg["read_key"])}</code>.</p>
<h2 id="docs">The wire&rsquo;s own documents</h2>
<p>Read from the vault as committed: the architecture, the sources policy, the workflows where the vault has them, and the runbook that the wire&rsquo;s agent starts from.</p>
{loader(cfg, "how")}
<noscript><p>The documents are read from the vault in your browser, which needs a script; they are <code>docs/*.md</code> and <code>pipeline/RUNBOOK.md</code> in the vault.</p></noscript>
"""
    agent = (f"How newsroom.sgit.ai reads {cfg['name']}'s vault ({cfg['vault_id']} on {cfg['endpoint']}, read key {cfg['read_key']}): the head pointer, the commit, the tree, "
             "then data/bundle.json, data/deliveries.json, data/releases.json and docs/*.md, decrypted in the browser and drawn as text. The contract the pages rely on is on this page: "
             "the required fields, the release file the desk writes on every publish, the optional changes[], corrections and updated_in_edition the page draws when present, and the optional wire, map and stack. "
             f"The vault's own documents are in it: `{cfg['clone']}`. The other wires on this site follow the same contract.")
    return newsroom_page(cfg["dir"] + "how.html", f"How {cfg['name'][0].lower() + cfg['name'][1:]} works",
                         f"How this site reads {cfg['name']}'s vault in the browser with a published read key, the contract the pages rely on, and the wire's own documents: architecture, sources policy and the runbook.",
                         body, eyebrow=EYEBROW, crumbs=((cfg["name"], cfg["dir"] + "index.html"),),
                         lead="The data is in a vault the agents write to; this site holds the read key and draws it. Here is how, what the pages rely on, and the wire's own documents, read from the same vault.",
                         agent=agent, head=f'<link rel="stylesheet" href="{cfg["rel"]}wire.css">\n', wide=True)


def take_snapshot(cfg, clone: Path):
    b = json.loads((clone / "data/bundle.json").read_text(encoding="utf-8"))
    rel = clone / "data/releases.json"
    releases = json.loads(rel.read_text(encoding="utf-8")) if rel.exists() else {}
    by_id = {s["id"]: s for s in b["stories"]}
    brief = b["brief"]
    beats = brief.get("beats") or [{"id": x["id"], "label": x["label"], "stories": [s["id"] for s in b["stories"] if s["beat"] == x["id"]]} for x in b["beats"]]
    meta = b.get("wire") if isinstance(b.get("wire"), dict) else {}
    stack = b.get("stack") if isinstance(b.get("stack"), dict) else {}
    wmap = b.get("map") if isinstance(b.get("map"), dict) else {}
    snap = {
        "what": f"{cfg['name']} as it was in its vault when this site was last released: headlines and primary links, each story's edition and dated corrections, the desk's latest release note. "
                f"The live edition is the vault ({cfg['vault_id']}); this file is the fallback and the index for agents.",
        "release": (ROOT / "admin/build/version.txt").read_text().strip(),
        "vault": cfg["vault_id"], "endpoint": cfg["endpoint"], "clone": cfg["clone"],
        "wire": {k: meta[k] for k in ("id", "title", "cadence", "description", "personal_persona") if k in meta} if meta else {"title": cfg["name"]},
        "edition": brief.get("edition"), "window": brief.get("window"), "kind": brief.get("kind"), "status": brief.get("status"),
        "counts": {"stories": len(b["stories"]), "sources": len(b.get("sources", [])), "personas": len(b.get("personas", [])),
                   "primary_not_fetched": sum(1 for s in b["stories"] if s.get("primary_fetched") is False),
                   "corrected": sum(1 for s in b["stories"] if s.get("changes")),
                   "map_entities": len(wmap.get("entities", []) or []), "stack_services": len(stack.get("services", []) or []), "deadlines": len(stack.get("deadlines", []) or [])},
        # the desk's latest release note (data/releases.json, wire-releases/v1), so an agent without a browser knows what last changed
        "latest_release": next(({k: r.get(k) for k in ("id", "at", "edition", "title", "summary", "added", "updated", "withdrawn")}
                                for r in sorted(releases.get("releases", []), key=lambda r: str(r.get("at", "")), reverse=True) if r.get("id")), None),
        "threads": [{"id": t.get("id"), "title": t.get("title"), "stories": t.get("stories", [])} for t in brief.get("threads", [])],
        "beats": [{"id": bt["id"], "label": bt.get("label", bt["id"]),
                   "stories": [{"id": sid, "headline": by_id[sid]["headline"], "date": by_id[sid].get("date", ""),
                                "primary_url": (by_id[sid].get("primary") or {}).get("url", ""), "publisher": (by_id[sid].get("primary") or {}).get("publisher", ""),
                                "status": by_id[sid].get("status", ""),
                                **({"edition": by_id[sid]["edition"]} if by_id[sid].get("edition") else {}),
                                **({"changes": [{"at": c.get("at", ""), "what": c.get("what", "")} for c in by_id[sid]["changes"]]} if by_id[sid].get("changes") else {})}
                               for sid in (bt.get("stories") or []) if sid in by_id]} for bt in beats],
    }
    if stack.get("deadlines"):
        snap["deadlines"] = [{k: d.get(k, "") for k in ("what", "date", "then", "source")} for d in sorted(stack["deadlines"], key=lambda d: str(d.get("date", "")))]
    text = json.dumps(snap, indent=1, ensure_ascii=False) + "\n"
    if not cfg["snapshot"].exists() or cfg["snapshot"].read_text(encoding="utf-8") != text:
        cfg["snapshot"].parent.mkdir(parents=True, exist_ok=True)
        cfg["snapshot"].write_text(text, encoding="utf-8")
        return True
    return False


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--from", dest="clones", action="append", default=[], metavar="[SLUG=]PATH",
                    help="a clone of a wire's vault, to refresh its snapshot; PATH alone is the Industry Wire, SLUG=PATH another wire")
    args = ap.parse_args()
    clones = {}
    for spec in args.clones:
        slug, _, path = spec.rpartition("=") if "=" in spec else ("", "", spec)
        clones[slug] = Path(path)
    unknown = set(clones) - {c["slug"] for c in CFGS}
    if unknown:
        raise SystemExit(f"wire: no config for {sorted(unknown)}; the wires are {[c['slug'] or '(industry)' for c in CFGS]}")
    changed = []
    for cfg in CFGS:
        if cfg["slug"] in clones and take_snapshot(cfg, clones[cfg["slug"]]):
            changed.append(cfg["dir"] + "snapshot.json")
        snap = json.loads(cfg["snapshot"].read_text(encoding="utf-8")) if cfg["snapshot"].exists() else None
        for rel, text in ((cfg["dir"] + "index.html", edition_page(cfg, snap)), (cfg["dir"] + "sources.html", sources_page(cfg)), (cfg["dir"] + "how.html", how_page(cfg)), (cfg["dir"] + "reach.html", reach_page(cfg))):
            if write(rel, text):
                changed.append(rel)
        print(f"wire {cfg['dir']}: vault {cfg['vault_id']}, snapshot {'of ' + snap['edition'] if snap else 'none'}")
    for rel, text in (("wire/days.html", days_page()), ("wire/charter.html", charter_page()), ("wire/desk-brief.html", brief_page())):
        if write(rel, text):
            changed.append(rel)
    print(f"wire: {len(CFGS)} wires; {len(changed)} written {changed}")



def reach_page(cfg):
    routes = [r for r in REACH.get("routes", []) if r.get("wire", "") == cfg["slug"]]
    up = cfg["up"]
    body = f"""{wires_strip(cfg)}
<p>Who the stories of {esc(cfg["name"])} concern, and how to reach them, so that they can be told this wire exists and sent what it found. <b>By organisation route only</b>, under <a href="{up}world-news-day/data/contact-rules.json">the contact rules</a> this site already publishes: a role address from the organisation&rsquo;s own contact page, one hop, the page&rsquo;s bytes hashed when fetched; never a person&rsquo;s address, never a directory, never a guess. Everything here is public, so anyone can check who was told. The routes this site found are recorded in <code>admin/build/wire-reach.json</code>; the desk adds its own to the vault as <code>data/contacts.json</code> under the same rules, and this page draws both, with what the vault already carries: the map&rsquo;s entities with their public pages and repositories, and the sources&rsquo; sites.</p>
{loader(cfg, "reach", reach=routes)}
<noscript><p>The vault is read in your browser, which needs a script. The routes this site found are in <code>admin/build/wire-reach.json</code>.</p></noscript>
"""
    agent = (f"Who {cfg['name']} concerns and how to reach them, by organisation route only, under the contact rules at world-news-day/data/contact-rules.json: "
             f"{len(routes)} route(s) this site found (admin/build/wire-reach.json: organisation, the contact page fetched and hashed, the role addresses the page publishes, and what it says each is for), "
             f"data/contacts.json from the vault when the desk adds it, the map's entities with pages and repositories, and the sources' sites. Never a personal address. The charter: wire/charter.html.")
    return newsroom_page(cfg["dir"] + "reach.html", f"{cfg['name']}: who should know",
                         f"Who the stories of {cfg['name']} concern and how to reach them, by organisation route only, under this site's published contact rules.",
                         body, eyebrow=EYEBROW, crumbs=((cfg["name"], cfg["dir"] + "index.html"),),
                         lead="Who should be told, and the route to tell them: organisations, never people, from their own published contact pages.",
                         agent=agent, head=f'<link rel="stylesheet" href="{cfg["rel"]}wire.css">\n', wide=True)


def days_page():
    cfg = CFGS[0]
    body = f"""{wires_strip(None, up="../")}
{loader({"slug": "days", "up": "../", "rel": "", "name": "Day by day"}, "days", wires=wires_public())}
<noscript><p>The vaults are read in your browser, which needs a script. Each wire&rsquo;s snapshot (<code>snapshot.json</code> beside its page) has the headlines and dates as of this site&rsquo;s last release.</p></noscript>
<h2 id="about">What this is</h2>
<p>Every wire on this site, day by day: the releases the desks published that day, with what each added and updated, and the stories dated that day, by source, with the licence tier of each. It is read live from every wire&rsquo;s vault, so it shows what happened as the desks record it, not as this site last released. A day with no stories is not shown; a story with no date is not shown, which is why the contract asks for one on every story.</p>
"""
    agent = (f"Every wire of newsroom.sgit.ai day by day, read live from {len(CFGS)} vaults ({', '.join(c['vault_id'] for c in CFGS)} on {cfg['endpoint']}): the releases published each day (data/releases.json) and the stories dated each day (data/bundle.json), by source and tier. "
             f"The snapshots beside each wire's page hold the same as of this site's last release.")
    return newsroom_page("wire/days.html", "The wires, day by day",
                         "Every wire on this site day by day: the releases the desks published and the stories dated each day, by source, read live from the vaults.",
                         body, eyebrow=EYEBROW, crumbs=(("The Industry Wire", "wire/index.html"),),
                         lead="What happened, and when: every wire's releases and stories by the day they are dated, read live from the vaults.",
                         agent=agent, head='<link rel="stylesheet" href="wire.css">\n', wide=True)


def md_page(rel, src: Path, title, description, lead, agent):
    meta, body_md = front_matter(src.read_text(encoding="utf-8"))
    body_md = "\n".join(line for line in body_md.splitlines() if not line.startswith("# "))     # the page carries the h1
    if src.is_relative_to(ROOT / "admin/notes"):
        body_md = body_md.replace("](../../", "](../")      # a note's links are written from admin/notes/; the page sits at wire/
    body = f"""{wires_strip(None, up="../")}
<div class="eng-body md-doc">{render(body_md)}</div>
<p class="dim">The source of this page is <a href="{"../" + src.relative_to(ROOT).as_posix()}">{esc(src.name)}</a>, rendered at release; the markdown is the record.</p>
"""
    return newsroom_page(rel, title, description, body, eyebrow=EYEBROW, crumbs=(("The Industry Wire", "wire/index.html"),), lead=lead, agent=agent,
                         head='<link rel="stylesheet" href="wire.css">\n<link rel="stylesheet" href="../engineering/engineering.css">\n', wide=False)


def charter_page():
    return md_page("wire/charter.html", CHARTER_MD, "The wires: a charter",
                   "The charter of the wires on newsroom.sgit.ai: facts first and analysis on top, corrections that propagate, three rounds of agents and what each enforces, what is never done, and public by default.",
                   "What every agent in the chain enforces, from the desk that writes a vault to the newsroom that draws it and the verifier that checks it, and what a reader can hold the wires to.",
                   "The charter of the wires (the Industry Wire, the OWASP Wire, the AWS Wire and any wire under the same contract): facts first, analysis marked as the desk's; corrections propagate to the story; three rounds (the desk writes and runs its gate, the newsroom reads with a published key and draws as written, an independent verifier checks every story and writes data/factcheck-<date>.json); what is never done (no claim without a source, no quote outside its source, no personal contact detail, nothing private in a public vault, no silent correction, no status upgraded on this side); public by default; one named reader by agreement. Source: admin/notes/2026-10-13__the-wires-charter.md.")


def brief_page():
    return md_page("wire/desk-brief.html", BRIEF_MD, "For the desks: the brief from the newsroom",
                   "The standing brief from newsroom.sgit.ai to the desks that write the wires' vaults: the schedule, the reader's lane, the verifier on every run, one list per wire, a Portugal wire, who should know, and the release note on every publish.",
                   "What the newsroom asks of the desks that write the vaults, dated, newest first; a desk reads it at the start of every run.",
                   "The standing brief for the desks that write the wires' vaults, read at the start of every run from https://newsroom.sgit.ai/wire/desk-brief.md: run at seven each morning (London); read the reader's lane once given its read key; a verifier on every run writing wire-factcheck/v1 to data/factcheck-<date>.json with one row per story; one subscription list per wire (X-SGit-List: wire:<slug> on the subscribe lane); a Portugal wire under the same contract; data/contacts.json under the published contact rules; a date on every story and an at on every release; a release note on every publish. The markdown is the record.")


if __name__ == "__main__":
    main()
