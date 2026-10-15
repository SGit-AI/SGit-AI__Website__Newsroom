#!/usr/bin/env python3
"""The Mesa Ranch observation desk: /demos/vaults/mesa-ranch-desk/index.html, a working observation desk in a vault of its own.

    python3 admin/build/mesa_ranch_vault.py

The vault (hn1s3h6q on dev.send.sgraph.ai) is built outside this repository by its own tools/ (build_data.py,
assemble.py, bundle.py); this page publishes its PUBLIC read key, embeds it with assets/vault-ui-embed.js as
sgit.ai's vault pages do, and shows what is in it. Only the public read key is kept here
(admin/content/vaults/mesa-ranch-desk.json); the vault key never enters the repository.
"""
import html
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from page import newsroom_page, write  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
REL = "demos/vaults/mesa-ranch-desk/index.html"
CRED = json.loads((ROOT / "admin/content/vaults/mesa-ranch-desk.json").read_text())

SHOTS = [
    ("index.webp", "The cover, one of seventeen pages: the menu on the left groups them as the deck does, the synthetic campus is drawn in pen and ink with orange markers, and details open on the right."),
    ("atlas.webp", "An atlas of events: twelve families around the buildout; Power and utilities is open in the panel on the right, each event with its definition, its observable signal and how often it was seen."),
    ("ontology.webp", "A domain ontology: six entities and six relationships, each entity a pen-and-ink vignette; click one and the observations that changed it open on the right."),
    ("observations.webp", "Every observation adds to what the newsroom knows: the four headline folders and the full history; the selected observation, its comparison and its records open on the right."),
    ("fractal-campus.webp", "The fractal semantic graph, level 1: the campus opens into the twelve event families; the number on each node is how many more it opens into."),
    ("fractal.webp", "Level 2: Power and utilities opens into its seven event types; the breadcrumb leads back to the question."),
    ("rings.webp", "Every level at once: the question at the centre, then families, event types, observations and records in rings; orange lines are evidence."),
    ("knowledge.webp", "The knowledge graph, in time: the ontology instantiated, played one observation at a time; here at the acquisition, with the new relationship in orange."),
    ("evidence.webp", "Records to observations: sixteen synthetic records on the left, seventeen observations on the right, and the evidence between them."),
    ("chain.webp", "The delta chain: observations on a time axis by the entity they change, with an arc to the earlier observation each was compared with."),
    ("workflow.webp", "Observations anchor the AI workflow: observe, compare, check, report, update, stepped through one cycle, with the graph growing at each step."),
    ("community.webp", "The community impact tracker: jobs, water, power, land and public commitments, with the article and alerts they produced."),
]


def trail(name, here_href):
    """The same row of cards the article generator renders for `!trail <name>`, from admin/content/trails.json,
    with this page's card marked. Images are set as backgrounds: this page is the newsroom's own, not a vault."""
    t = json.loads((ROOT / "admin/content/trails.json").read_text())[name]
    up = "../../../"
    rel = lambda h: h if h.startswith("http") else up + h.lstrip("/")
    cards = []
    for it in t["items"]:
        here = it["href"] == here_href
        img = f'<span class="trail-img" style="background-image:url({html.escape(rel(it["image"]), quote=True)})"></span>' if it.get("image") else ""
        body = (f'<span class="trail-k">{html.escape(it["label"])}</span><span class="trail-t">{html.escape(it["title"])}</span>'
                f'<span class="trail-d">{html.escape(it["line"])}</span>')
        links = "".join(f'<a href="{html.escape(rel(l["href"]), quote=True)}"' + (' target="_blank" rel="noopener"' if l.get("external") else "")
                        + f'>{html.escape(l["text"])}{" &#8599;" if l.get("external") else ""}</a>' for l in it.get("links", []))
        badge = '<span class="trail-here">you are here</span>' if here else ""
        cards.append(f'<div class="trail-c{" here" if here else ""}">{badge}<a href="{html.escape(rel(it["href"]), quote=True)}">{img}</a>'
                     f'<div class="trail-b">{body}{f"<span class=trail-l>{links}</span>" if links else ""}</div></div>')
    return (f'<div class="trail"><div class="trail-h">{html.escape(t["title"])}</div><p class="trail-n">{html.escape(t["note"])}</p>'
            f'<div class="trail-row">{"".join(cards)}</div></div>')


def page():
    rk, vid = CRED["read_key"], CRED["vault_id"]
    hexkey = rk[len("sgit_public_read_"):]
    cred = f"{rk}:{vid}"
    ui = "https://dev.vault.sgraph.ai/#" + cred.replace(":", "%3A")
    shots = "\n".join(f'<figure><img src="images/{f}" alt="{a}" loading="lazy" style="width:100%;height:auto;border:1px solid #d8cfbd;border-radius:6px"><figcaption class="small dim">{a}</figcaption></figure>' for f, a in SHOTS)
    body = trail("mesa-ranch", "https://newsroom.sgit.ai/demos/vaults/mesa-ranch-desk/index.html") + f"""
<div class="note"><b>Everything in this vault is synthetic.</b> The campus, the county, the companies, the agencies' names and all sixteen records are invented. The vault is modelled on the data-center example in Francesco Marconi's INMA talk, <em>When journalism becomes intelligence</em>, and describes no real organisation. The real project the slides drew on is described in public reporting linked from <a href="../../../articles/journalism-becomes-intelligence.html">the article</a>; <a href="../../../articles/inside-the-mesa-ranch-desk.html">the tour</a> walks through every page.</div>

<div class="note"><b>Open it yourself. The key is the whole credential.</b><br>
Read key: <code style="word-break:break-all">{cred}</code><br>
In the official UI: <a href="{ui}" rel="noopener" target="_blank">open it read-only in a new tab</a> ·
From the CLI: <code style="word-break:break-all">sgit clone {cred}</code><br>
<span class="small dim">Published deliberately under the <code>sgit_public_read_</code> prefix, and derived one-way from a vault key that is not in this repository. Read back with this key before it was published: 63 files, the same pages.</span></div>

<p style="margin:18px 0 6px"><a href="{ui}" rel="noopener" target="_blank" style="display:inline-block;background:#e2492f;color:#fff;font-weight:800;font-size:20px;text-decoration:none;padding:14px 26px;border-radius:10px">Open the vault, full screen →</a> <a href="#live" style="margin-left:14px">or see it here, below</a></p>
<p class="small dim">Opens in the vault's own app, read-only, with the published key: seventeen pages, a menu on the left, details on the right.</p>

<h2 id="live">See it live, here</h2>
<p class="small dim" style="margin:.2rem 0 .9rem">The vault opens as an app of seventeen pages: the eleven slides, each working on the vault's own data, and five graph pages. Every marker, folder, record, observation and node opens its details on the right.</p>
<div class="sgv-uiembed" data-vault="{vid}" data-readkey="{hexkey}" data-app="1"></div>
<script>
(function () {{
  ['vault-ui-embed.js'].forEach(function (f) {{
    fetch('../../../assets/' + f).then(function (r) {{ if (!r.ok) throw new Error(r.status); return r.text(); }}).then(function (t) {{ (0, eval)(t); }}).catch(function (e) {{ console.error('[vaults] ' + f + ' failed to load:', e); }});
  }});
}}());
</script>

<h2 id="inside">What is in it</h2>
<table>
<tr><th>Path</th><th>What</th></tr>
<tr><td><code>index.html</code> and 16 more pages</td><td>The desk, one page per menu item; inlined CSS and JS; every illustration and graph drawn as SVG in the browser, in the deck's pen-and-ink style; the data inlined as a fallback.</td></tr>
<tr><td><code>instances.json</code>, <code>compares.json</code></td><td>The knowledge graph, each relationship with the observation that made it, and the delta chain.</td></tr>
<tr><td><code>atlas/</code></td><td>12 event families and 78 event types, each with a definition and an observable signal.</td></tr>
<tr><td><code>ontology.json</code></td><td>Six entities, their attributes and six relationships. An event changes a state or relationship in this model.</td></tr>
<tr><td><code>records/</code></td><td>16 synthetic source records: an air permit and its application, a public notice, minutes, an abatement application, statements, building registrations, a deed, an investor presentation, oversize-load permits.</td></tr>
<tr><td><code>observations.json</code></td><td>17 observations, each a subject, a change, a time and its evidence, matched to an event type.</td></tr>
<tr><td><code>tracker.json</code>, <code>outputs.json</code></td><td>The community impact tracker and the article and alerts it produced.</td></tr>
<tr><td><code>tools/</code></td><td>The scripts that build all of it. Replace the families, entities and records with your own beat; the app does not change.</td></tr>
</table>

<h2 id="tour">A tour</h2>
{shots}
"""
    return newsroom_page(REL, "The Mesa Ranch observation desk: journalism as intelligence, in a vault",
                         "A working observation desk for one synthetic data-center buildout, built from Francesco Marconi's INMA deck: an atlas of 78 event types, an ontology, 16 synthetic records, 17 observations and a community impact tracker, in an sgit vault you can open.",
                         body, eyebrow="A vault", crumbs=(("Replicate", "replicate/index.html"),),
                         lead="The method in the slides, working, on synthetic records, in a vault you can open.", wide=True)


if __name__ == "__main__":
    changed = write(REL, page())
    print(f"mesa_ranch_vault: {REL} {'written' if changed else 'unchanged'}")
