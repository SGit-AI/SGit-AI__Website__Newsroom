#!/usr/bin/env python3
"""The Mesa Ranch observation desk: /demos/vaults/mesa-ranch-desk/index.html, a working observation desk in a vault of its own.

    python3 admin/build/mesa_ranch_vault.py

The vault (hn1s3h6q on dev.send.sgraph.ai) is built outside this repository by its own tools/ (build_data.py,
assemble.py, bundle.py); this page publishes its PUBLIC read key, embeds it with assets/vault-ui-embed.js as
sgit.ai's vault pages do, and shows what is in it. Only the public read key is kept here
(admin/content/vaults/mesa-ranch-desk.json); the vault key never enters the repository.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from page import newsroom_page, write  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
REL = "demos/vaults/mesa-ranch-desk/index.html"
CRED = json.loads((ROOT / "admin/content/vaults/mesa-ranch-desk.json").read_text())

SHOTS = [
    ("s1.webp", "The cover: the headline in the deck's type, the synthetic campus drawn in pen and ink with orange markers on the power station, the halls, the water tower, the town and the reservoir."),
    ("s3-after.webp", "Journalism is delta science: the After view, with the four documents the records add: Permissions, Resources, Ownership and Commitments, each opening its record."),
    ("s5-power.webp", "An atlas of events: twelve families around the buildout, with types and observations per family; Power and utilities is open, with each event's definition, observable signal and the observations that matched it."),
    ("s6.webp", "A domain ontology: Campus, Building, Construction work, Source record, Company and Project, with the six relationships; clicking an entity lists the observations that changed it."),
    ("s7.webp", "Every observation adds to what the newsroom knows: the four headline folders and the full history, each with subject, change, time, event type and evidence."),
    ("s8.webp", "Observations anchor the AI workflow: observe, compare, check, report, update, stepped through one cycle from the vault, the investor presentation that moved the first phase to 2028."),
    ("s10.webp", "The community impact tracker: jobs, water, power, land and public commitments, each a claim, a change or an open question with its record; beside it the article and the alerts they produced."),
    ("s11.webp", "Your advantage is how you observe: the closing slide, how to make one for your own beat, and what is in the vault."),
]


def page():
    rk, vid = CRED["read_key"], CRED["vault_id"]
    hexkey = rk[len("sgit_public_read_"):]
    cred = f"{rk}:{vid}"
    ui = "https://dev.vault.sgraph.ai/#" + cred.replace(":", "%3A")
    shots = "\n".join(f'<figure><img src="images/{f}" alt="{a}" loading="lazy" style="width:100%;height:auto;border:1px solid #d8cfbd;border-radius:6px"><figcaption class="small dim">{a}</figcaption></figure>' for f, a in SHOTS)
    body = f"""
<div class="note"><b>Everything in this vault is synthetic.</b> The campus, the county, the companies, the agencies' names and all sixteen records are invented. The vault is modelled on the data-center example in Francesco Marconi's INMA talk, <em>When journalism becomes intelligence</em>, and describes no real organisation. The real project the slides drew on is described in public reporting linked from <a href="../../../articles/journalism-becomes-intelligence.html">the article</a>.</div>

<div class="note"><b>Open it yourself. The key is the whole credential.</b><br>
Read key: <code style="word-break:break-all">{cred}</code><br>
In the official UI: <a href="{ui}" rel="noopener" target="_blank">open it read-only in a new tab</a> ·
From the CLI: <code style="word-break:break-all">sgit clone {cred}</code><br>
<span class="small dim">Published deliberately under the <code>sgit_public_read_</code> prefix, and derived one-way from a vault key that is not in this repository. Read back with this key before it was published: 43 files, the same <code>index.html</code>.</span></div>

<h2 id="live">See it live, here</h2>
<p class="small dim" style="margin:.2rem 0 .9rem">The vault opens as an app: eleven sections that follow the eleven slides, each working on the vault's own data. Every marker, folder, record id and observation id opens the record behind it.</p>
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
<tr><td><code>index.html</code></td><td>The desk: inlined CSS and JS; every illustration drawn as SVG in the browser, in the deck's pen-and-ink style; the data inlined as a fallback.</td></tr>
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
