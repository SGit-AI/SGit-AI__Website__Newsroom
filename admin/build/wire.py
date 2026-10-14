#!/usr/bin/env python3
"""The Industry Wire: three pages that read the wire's vault in the browser, and a snapshot for agents.

    python3 admin/build/wire.py                                   # the pages, from the recorded config
    python3 admin/build/wire.py --from /path/to/a/clone/of/the/vault   # also refresh wire/snapshot.json

The wire's data is not on this site. It is in an encrypted sgit vault that the wire's agents write to
(admin/build/wire-vault.json: endpoint, vault id, read key). The pages open it in the reader's browser with the
published read key (wire/vault-reader.js, vendored from sgit.ai) and draw it (wire/wire.js). A commit to the
vault is on the page within two minutes, with no release of this site; the site owns the presentation and the
vault owns the news. That is the pattern sgit.ai uses for its own documentation, applied to a daily feed.

wire/snapshot.json is what was in the vault when this site was last released: the edition, its headlines with
their primary links, and the counts. It is public data derived from public sources, it is what the pages show
when the vault cannot be reached, and it is what an agent without a browser reads first; the vault itself is
one `sgit clone` away with the read key. It is refreshed only when --from names a clone, so the snapshot's date
says when it was taken.
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from page import newsroom_page, write, esc, HOST  # noqa: E402
from api import api_url  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
CFG = json.loads((ROOT / "admin/build/wire-vault.json").read_text(encoding="utf-8"))
SNAP = ROOT / "wire/snapshot.json"
HEAD = f'<link rel="stylesheet" href="{api_url("wire/wire.css")}">\n'
EYEBROW = "Industry news, read from a vault · beta"
# the named readers: people who agreed, on a recorded date, to a persona and a personal brief in a public vault
NAMED = [x for x in CFG.get("named_readers", []) if isinstance(x, dict) and x.get("persona") and x.get("agreed")]
NAMED_NAMES = ", ".join(x.get("name", x["persona"]) for x in NAMED) or "nobody yet"


def config_block():
    pub = {k: CFG[k] for k in ("endpoint", "vault_id", "read_key", "ref_ttl_s", "clone", "named_readers") if k in CFG}
    return f'<script type="application/json" id="wire-config">{json.dumps(pub)}</script>'


def snapshot_html(snap, up=""):
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


def loader(kind):
    return f"""<div id="wire-status" class="wire-status" hidden></div>
<div id="wire-mount" data-wire="{kind}"><p class="dim">Opening the vault&hellip;</p></div>
{config_block()}
<script type="module">
import {{ wire }} from '{api_url('wire/wire.js')}';
wire({{ mount: document.getElementById('wire-mount') }});
</script>
"""


def edition_page(snap):
    body = f"""{loader("edition")}
<noscript><p>The edition is read from an encrypted vault in your browser, which needs a script. Below is what the vault held at the last release of this site.</p></noscript>
{snapshot_html(snap)}
<h2 id="about">What this is</h2>
<div class="note"><b>A beta.</b> The wire is an experiment run in the open: agents find and write the stories, an encrypted vault holds them, and this page draws them. It has one named reader, {esc(NAMED_NAMES)}, who runs this site and has agreed to be one while the wire is a beta; the persona of that name and the personal brief under its lens are theirs, and they are public like everything else in the vault. Expect gaps, repeats and stories whose primary source was never fetched, each marked as such, and expect the shape of the edition to change.</div>
<p>Once a day, what happened in the five areas this newsroom writes about: building with AI and models, AI business models, open source, cybersecurity, and risk, governance and regulation. For every story: where it came from, who else covered it, one exact quote with its source, and why it matters. The stories are found, grouped and written by agents, from a registry of sources with a licence tier each (<a href="sources.html">the sources</a>), and every story says what it is: <em>ai-generated, unreviewed</em> until a person has reviewed it. The edition of 11 October is a first pass, a week&rsquo;s catch-up, and says so.</p>
<p><b>Read it as an inbox.</b> The bar above the stories says what is new since your last visit, how much of it is for you and how much is not under the lens you read as, and what the wire&rsquo;s desk says changed in the vault. At each story, one tap: <em>Done</em>, <em>Read later</em>, <em>Follow up</em>, <em>Not for me</em>, <em>More like this</em> or <em>Wrong</em>; the story leaves your inbox, and the filters bring it back. Your decisions and what you have seen are kept in this browser first and reach your own vault when you press <em>Update the vault</em>; until then the bar and the Vault button say what is only here. <a href="../admin/notes/2026-10-13__the-wire-as-an-inbox.md">How it works</a>.</p>
<p><b>Read as someone.</b> The same stories reach different readers. Choose a persona and the edition shows what reached them, through which concern, and what was withheld, with the reason. That join is recorded in the vault by the wire&rsquo;s own code (<code>pipeline/join.py</code>), not computed here; the page shows the record. If you are reading this site as one of its personas, the lens follows it.</p>
<p><b>Where it comes from.</b> The data is not on this site. It is in an encrypted vault that the wire&rsquo;s agents write to, and this page opens it in your browser with a published read key: {esc(CFG["vault_id"])} on {esc(CFG["endpoint"].replace("https://", ""))}. A commit to the vault is on this page within two minutes, with no release of the site. Anyone can read the whole vault, and its history, with <code>{esc(CFG["clone"])}</code>. <a href="how.html">How the wire works</a> has the design, the workflows and the daily run, read from the same vault.</p>
"""
    agent = ("The edition page reads as an inbox: what is new since the reader's last visit, for them and not under their lens, the vault's release notes (data/releases.json when present), "
             "and one decision per story kept as a note in the reader's browser and carried to their own vault on Update (admin/notes/2026-10-13__the-wire-as-an-inbox.md). "
             f"The Industry Wire's data is in a public-read sgit vault, not on this site: vault {CFG['vault_id']} on {CFG['endpoint']}, read key "
             f"{CFG['read_key']} (read-only, published on purpose). Clone it with `{CFG['clone']}` and read data/bundle.json (beats, stories, sources, personas, "
             f"brief, docs), data/deliveries.json (story × persona: reached or withheld, with the reason) and docs/*.md. https://{HOST}/wire/snapshot.json holds the "
             f"headlines and primary links as of this site's last release. The wire is a beta; its named reader ({NAMED_NAMES}) agreed to be one, and the persona and "
             "personal brief of that name in the vault are theirs. Every story is marked ai-generated, unreviewed until a person reviews it"
             + (f"; {snap['counts']['primary_not_fetched']} of the {snap['counts']['stories']} stories in the edition of {snap['edition']} have a primary "
                "source the research agent did not fetch, and those stories say so." if snap and "primary_not_fetched" in snap.get("counts", {}) else "."))
    return newsroom_page("wire/index.html", "The Industry Wire",
                         "A daily wire of industry news across five beats, in beta, read live from an encrypted vault that agents keep: every story with its primary source, who else covered it, one exact quote and why it matters, and a lens per persona showing what reached them and why.",
                         body, eyebrow=EYEBROW,
                         lead="What happened this week in building with AI, AI business, open source, cybersecurity and governance: each story with where it came from and who else covered it, read live from the wire's vault. A beta, with one named reader by their agreement.",
                         agent=agent, head=HEAD, wide=True)


def sources_page():
    body = f"""{loader("sources")}
<noscript><p>The registry is read from the wire&rsquo;s vault in your browser, which needs a script. Anyone can read it with <code>{esc(CFG["clone"])}</code>: it is <code>data/sources.json</code>.</p></noscript>
<h2 id="tiers">The tiers</h2>
<p>The wire&rsquo;s sources policy (<a href="how.html#docs/SOURCES-POLICY.md">in the vault</a>) gives each source a tier that decides what the wire may keep and show. <b>Tier A</b> is an open licence or public domain: the full text may be frozen, kept and shown. <b>Tier B</b> is quote and link: the bytes are frozen as evidence, and the public page carries a quote of 25 words or fewer with a link. <b>Tier C</b> is link only: headline, address and date, never the text. A source becomes <em>verified</em> when a person has opened its licence page; until then its tier is provisional. Outlets that keep appearing in coverage are proposed as sources, and a person confirms the tier.</p>
"""
    agent = f"The source registry of the Industry Wire: data/sources.json in vault {CFG['vault_id']} ({CFG['clone']}). Each source has beats, a tier (A open licence, B quote and link, C link only), a licence and whether a person has verified it."
    return newsroom_page("wire/sources.html", "The wire's sources",
                         "The registry of sources the Industry Wire polls, with the licence tier that decides what may be kept and shown, read live from the wire's vault.",
                         body, eyebrow=EYEBROW, crumbs=(("The Industry Wire", "wire/index.html"),),
                         lead="Where the wire looks, and what each source's licence allows it to keep.", agent=agent, head=HEAD, wide=True)


def how_page():
    reads = ", ".join(f"<code>{esc(r)}</code>" for r in CFG["reads"])
    body = f"""<h2 id="site">How this site reads the vault</h2>
<p>The wire&rsquo;s data lives in an encrypted sgit vault that its agents write to, with the key that writes it held by them and not by this site. This site holds the vault&rsquo;s <b>read key</b>, published on purpose, and each wire page opens the vault in your browser: it derives the address of the vault&rsquo;s head pointer, fetches ciphertext from <code>{esc(CFG["endpoint"])}</code>, decrypts it with Web Crypto, walks the commit&rsquo;s tree and reads {reads}. Nothing from the vault is run; it is drawn as text, and the documents are rendered from their markdown by a renderer that escapes. The pointer is re-checked at most every two minutes, so a commit by the wire&rsquo;s agents is on the page within that, with no release of this site. Objects that cannot change are cached in the browser for good.</p>
<div class="note"><b>The contract between the vault and this site.</b> Everything in the vault is public, including its history: a published read key cannot be withdrawn from anyone who has fetched the objects, so nothing private goes in it, not frozen tier-B bytes, not a reader&rsquo;s feedback, and not a brief meant for one person unless that person has agreed to it being public; those need a vault of their own. The wire&rsquo;s one named reader so far, {esc(NAMED_NAMES)}, has agreed while the wire is a beta, and the agreement is recorded with the date in <code>admin/build/wire-vault.json</code>, which is also what tells the page to offer that lens. The pages rely on <code>data/bundle.json</code> having <code>beats</code>, <code>stories</code>, <code>sources</code>, <code>personas</code> and <code>brief</code> (edition, window, kind, status, editor_note, lead, threads, beats), on each story carrying <code>id</code>, <code>beat</code>, <code>headline</code>, <code>date</code>, <code>summary</code>, <code>quote</code>, <code>quote_source_url</code>, <code>primary</code>, <code>coverage</code>, <code>entities</code>, <code>why_it_matters</code>, <code>personas</code>, <code>confidence</code>, <code>status</code> and <code>primary_fetched</code>, and on <code>data/deliveries.json</code> rows of <code>story</code>, <code>persona</code>, <code>status</code>, <code>connections</code> and <code>withheld_reason</code>. When the vault has <code>data/releases.json</code> (<code>wire-releases/v1</code>: releases newest first, each with <code>id</code>, <code>at</code>, <code>edition</code>, <code>title</code>, <code>summary</code>, and the story ids <code>added</code>, <code>updated</code> and <code>withdrawn</code>), the edition shows the releases since the reader&rsquo;s last visit; the file is optional, and <a href="../admin/notes/2026-10-13__the-wire-as-an-inbox.md">the brief</a> says how to write it. A story&rsquo;s <code>status</code> is shown as written, so <em>ai-generated, unreviewed</em> stays on the page until the vault says otherwise. The commit message of the head is shown on every wire page.</div>
<p>To read it without this site: <code>{esc(CFG["clone"])}</code>. The read key is <code>{esc(CFG["read_key"])}</code>.</p>
<h2 id="docs">The wire&rsquo;s own documents</h2>
<p>Read from the vault as committed: the architecture, the workflows, the sources policy, the UI options, the inspiration, and the runbook that the daily agent starts from.</p>
{loader("how")}
<noscript><p>The documents are read from the vault in your browser, which needs a script; they are <code>docs/*.md</code> and <code>pipeline/RUNBOOK.md</code> in the vault.</p></noscript>
"""
    agent = (f"How newsroom.sgit.ai reads the Industry Wire's vault ({CFG['vault_id']} on {CFG['endpoint']}, read key {CFG['read_key']}): the head pointer, the commit, the tree, "
             "then data/bundle.json, data/deliveries.json and docs/*.md, decrypted in the browser and drawn as text. The contract the pages rely on is on this page. "
             f"The vault's own documents (architecture, workflows, sources policy, runbook) are in it: `{CFG['clone']}`.")
    return newsroom_page("wire/how.html", "How the wire works",
                         "How this site reads the Industry Wire's vault in the browser with a published read key, the contract the pages rely on, and the wire's own documents: architecture, workflows, sources policy and the daily runbook.",
                         body, eyebrow=EYEBROW, crumbs=(("The Industry Wire", "wire/index.html"),),
                         lead="The data is in a vault the agents write to; this site holds the read key and draws it. Here is how, what the pages rely on, and the wire's own design documents, read from the same vault.",
                         agent=agent, head=HEAD, wide=True)


def take_snapshot(clone: Path):
    b = json.loads((clone / "data/bundle.json").read_text(encoding="utf-8"))
    by_id = {s["id"]: s for s in b["stories"]}
    brief = b["brief"]
    beats = brief.get("beats") or [{"id": x["id"], "label": x["label"], "stories": [s["id"] for s in b["stories"] if s["beat"] == x["id"]]} for x in b["beats"]]
    snap = {
        "what": "The Industry Wire as it was in its vault when this site was last released: headlines and primary links only. "
                f"The live edition is the vault ({CFG['vault_id']}); this file is the fallback and the index for agents.",
        "release": (ROOT / "admin/build/version.txt").read_text().strip(),
        "vault": CFG["vault_id"], "endpoint": CFG["endpoint"], "clone": CFG["clone"],
        "edition": brief.get("edition"), "window": brief.get("window"), "kind": brief.get("kind"), "status": brief.get("status"),
        "counts": {"stories": len(b["stories"]), "sources": len(b.get("sources", [])), "personas": len(b.get("personas", [])),
                   "primary_not_fetched": sum(1 for s in b["stories"] if s.get("primary_fetched") is False)},
        "threads": [{"id": t.get("id"), "title": t.get("title"), "stories": t.get("stories", [])} for t in brief.get("threads", [])],
        "beats": [{"id": bt["id"], "label": bt.get("label", bt["id"]),
                   "stories": [{"id": sid, "headline": by_id[sid]["headline"], "date": by_id[sid].get("date", ""),
                                "primary_url": (by_id[sid].get("primary") or {}).get("url", ""), "publisher": (by_id[sid].get("primary") or {}).get("publisher", ""),
                                "status": by_id[sid].get("status", "")}
                               for sid in (bt.get("stories") or []) if sid in by_id]} for bt in beats],
    }
    text = json.dumps(snap, indent=1, ensure_ascii=False) + "\n"
    if not SNAP.exists() or SNAP.read_text(encoding="utf-8") != text:
        SNAP.write_text(text, encoding="utf-8")
        return True
    return False


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--from", dest="clone", help="a clone of the wire's vault, to refresh wire/snapshot.json")
    args = ap.parse_args()
    changed = []
    if args.clone and take_snapshot(Path(args.clone)):
        changed.append("wire/snapshot.json")
    snap = json.loads(SNAP.read_text(encoding="utf-8")) if SNAP.exists() else None
    for rel, text in (("wire/index.html", edition_page(snap)), ("wire/sources.html", sources_page()), ("wire/how.html", how_page())):
        if write(rel, text):
            changed.append(rel)
    print(f"wire: vault {CFG['vault_id']}, snapshot {'of ' + snap['edition'] if snap else 'none'}; {len(changed)} written {changed}")


if __name__ == "__main__":
    main()
