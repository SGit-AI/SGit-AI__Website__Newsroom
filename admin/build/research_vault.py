#!/usr/bin/env python3
"""Research, delivered as a vault: /demos/vaults/corvane-research/index.html, a synthetic research firm's assessment
of a synthetic AI-enabled product, in a vault of its own.

    python3 admin/build/research_vault.py

The vault is built outside this repository by its own tools/ (build_data.py, assemble.py, bundle.py); this page
publishes its PUBLIC read key, embeds it with assets/vault-ui-embed.js, and shows what is in it. Only the public
read key is kept here (admin/content/vaults/corvane-research.json); the vault key never enters the repository.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from page import newsroom_page, write  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
REL = "demos/vaults/corvane-research/index.html"
CRED = json.loads((ROOT / "admin/content/vaults/corvane-research.json").read_text())

SHOTS = [
    ("index.webp", "The cover: the question, the answer with four conditions, and the four numbers that carry it: insurability B to D, reach 4 to 6 systems, three rules resting on hope, B again with the conditions."),
    ("product.webp", "The product before and after AI: in red, what the agent added to the product's reach, most of it written by people outside the company."),
    ("policy.webp", "Two behaviour policies: every rule with the barrier that holds it, from boundary to hope; click a rule and the findings that tested it open on the right."),
    ("run.webp", "The evaluation run: six agent workers under one written mandate, their tasks and minutes, and the claims QA rejected."),
    ("findings.webp", "Six findings, each with its severity and its evidence."),
    ("graph.webp", "The fractal graph: the question, opened level by level into vendor, product, agent and buyer, capabilities, rules, findings, evidence and the worker that made it."),
    ("taxonomy.webp", "One taxonomy, or a graph: a category tree with a rating field, beside the 43-node graph this vault holds."),
    ("rating.webp", "Licence to operate and insurability: B before the agent, D after, B with four conditions; the grade is the firm's judgement over facts in the vault."),
    ("briefings.webp", "One finding, six readers: the same research written for the CISO, the CFO, counsel, procurement, the board and an underwriter."),
    ("calc.webp", "The cost calculator: the add-on against the expected loss, with every input editable."),
    ("feedback.webp", "The client writes back: an append lane of comments, votes and flags."),
    ("business.webp", "The business model: the vault, a live evaluation, briefings, a portfolio subscription and a branded app."),
]


def page():
    rk, vid = CRED["read_key"], CRED["vault_id"]
    hexkey = rk[len("sgit_public_read_"):]
    cred = f"{rk}:{vid}"
    ui = "https://dev.vault.sgraph.ai/#" + cred.replace(":", "%3A")
    shots = "\n".join(f'<figure><img src="images/{f}" alt="{a}" loading="lazy" style="width:100%;height:auto;border:1px solid #d7d3c8;border-radius:6px"><figcaption class="small dim">{a}</figcaption></figure>' for f, a in SHOTS)
    body = f"""
<div class="note"><b>Everything in this vault is synthetic.</b> Corvane Research, Tallyfern, Harbourline Group and every person, finding, timing and price in it are invented, to show how a company that sells research could deliver it as a vault. None of it describes a real company or product. <a href="../../../articles/research-delivered-as-a-vault.html">The article</a> explains the idea.</div>

<div class="note"><b>Open it yourself. The key is the whole credential.</b><br>
Read key: <code style="word-break:break-all">{cred}</code><br>
In the official UI: <a href="{ui}" rel="noopener" target="_blank">open it read-only in a new tab</a> ·
From the CLI: <code style="word-break:break-all">sgit clone {cred}</code><br>
<span class="small dim">Published deliberately under the <code>sgit_public_read_</code> prefix, and derived one-way from a vault key that is not in this repository. Read back with this key before it was published: 52 files, the same pages.</span></div>

<p style="margin:18px 0 6px"><a href="{ui}" rel="noopener" target="_blank" style="display:inline-block;background:#0f766e;color:#fff;font-weight:800;font-size:20px;text-decoration:none;padding:14px 26px;border-radius:10px">Open the vault, full screen →</a> <a href="#live" style="margin-left:14px">or see it here, below</a></p>
<p class="small dim">Opens in the vault's own app, read-only: thirteen pages, a menu on the left, details on the right.</p>

<h2 id="live">See it live, here</h2>
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
<tr><td><code>index.html</code> and 12 more pages</td><td>The app, one page per menu item; CSS and JS inlined; the graph drawn in the browser; the data inlined as a fallback.</td></tr>
<tr><td><code>findings/</code>, <code>evidence/</code></td><td>6 findings and 8 pieces of evidence, each with the agent worker that made it.</td></tr>
<tr><td><code>policy/</code></td><td>The product's behaviour policy before and after its AI agent, every rule with its barrier.</td></tr>
<tr><td><code>run/ledger.json</code></td><td>The evaluation run: the mandate, six workers, their tasks and minutes, and the claims QA rejected.</td></tr>
<tr><td><code>graph.json</code></td><td>The fractal graph, 43 nodes in six levels.</td></tr>
<tr><td><code>briefings/</code></td><td>Six briefings, one per reader.</td></tr>
<tr><td><code>lane/</code></td><td>The client's append lane: comments, votes and flags.</td></tr>
<tr><td><code>tools/</code></td><td>The scripts that build all of it.</td></tr>
</table>

<h2 id="tour">A tour</h2>
{shots}
"""
    return newsroom_page(REL, "Research, delivered as a vault: Corvane Research on Tallyfern Pay",
                         "A synthetic research firm's assessment of a synthetic AI-enabled product, with and without its agent: two behaviour policies, an evaluation run, findings with evidence, a fractal graph, six briefings, a calculator and the client's append lane, in an sgit vault you can open.",
                         body, eyebrow="A vault", crumbs=(("Replicate", "replicate/index.html"),),
                         lead="Vendor research as a living vault instead of a PDF, on synthetic data.", wide=True)


if __name__ == "__main__":
    changed = write(REL, page())
    print(f"research_vault: {REL} {'written' if changed else 'unchanged'}")
