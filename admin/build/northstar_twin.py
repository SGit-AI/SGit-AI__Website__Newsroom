#!/usr/bin/env python3
"""The Northstar refund twin: /demos/vaults/northstar-twin/index.html, the refund in Ashish Rajan's article as a store you can run.

    python3 admin/build/northstar_twin.py

The vault (n89dyusm on dev.send.sgraph.ai) is built outside this repository by its own tools/ (build_data.py,
assemble.py, bundle.py, engine.js); this page publishes its PUBLIC read key, embeds it with assets/vault-ui-embed.js
as the Mesa Ranch desk does, and shows what is in it. Only the public read key is kept here
(admin/content/vaults/northstar-twin.json); the vault key never enters the repository.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from page import newsroom_page, write  # noqa: E402
from mesa_ranch_vault import trail  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
REL = "demos/vaults/northstar-twin/index.html"
CRED = json.loads((ROOT / "admin/content/vaults/northstar-twin.json").read_text())

SHOTS = [
    ("overview.webp", "The case: the scenario from the article, the thirteen requests, and the four designs side by side: overpaid, short or still owed, right, and the minutes people spent."),
    ("play-a.webp", "Play and replay: N-1001, the $150 refund, in design A. Every step is tagged with its pillar and its policy; on the right, what the agent did against what the records say, the ledger, and the trace."),
    ("split-d.webp", "N-1008 in design D: the right amount, $261, proposed as three refunds under the limit. The decision policy routes anything over $200 to a team lead, and the workflow pays one decided amount."),
    ("compare.webp", "Compare the designs: every case under A, B, C and D, with the totals: $458 overpaid in A, $0 in C and D; 57 person-minutes in C, 18 in D."),
    ("policies.webp", "The three policies: the behaviour policy's rows, the decision table for who decides the amount, and the workflow's eight steps with the controls at each."),
    ("casebook.webp", "The casebook: N-1010 goes to a person and becomes precedent P-1; N-1011 follows it; N-1012 is distinguished and goes to a person again."),
]


def page():
    rk, vid = CRED["read_key"], CRED["vault_id"]
    hexkey = rk[len("sgit_public_read_"):]
    cred = f"{rk}:{vid}"
    ui = "https://dev.vault.sgraph.ai/#" + cred.replace(":", "%3A")
    shots = "\n".join(f'<figure><img src="images/{f}" alt="{a}" loading="lazy" style="width:100%;height:auto;border:1px solid #dcd7cb;border-radius:6px"><figcaption class="small dim">{a}</figcaption></figure>' for f, a in SHOTS)
    body = trail("northstar", "https://newsroom.sgit.ai/demos/vaults/northstar-twin/index.html") + f"""
<div class="note"><b>Everything in this vault is synthetic.</b> Northstar is the fictional retailer in Ashish Rajan's article, <a href="https://ashishrajan.substack.com/p/what-does-it-take-to-build-ai-systems" rel="noopener" target="_blank">What Does It Take to Build AI Systems We Can Actually Trust?</a> (16 October 2026). Every order, person and amount here is invented for this twin. No model is called: the agent's mistakes are scripted per case, so every run replays exactly. <a href="../../../articles/allowed-is-not-right.html">The reply</a> makes the argument; <a href="../../../articles/inside-the-northstar-twin.html">the tour</a> walks through the cases.</div>

<div class="note"><b>Open it yourself. The key is the whole credential.</b><br>
Read key: <code style="word-break:break-all">{cred}</code><br>
In the official UI: <a href="{ui}" rel="noopener" target="_blank">open it read-only in a new tab</a> ·
From the CLI: <code style="word-break:break-all">sgit clone {cred}</code><br>
<span class="small dim">Published deliberately under the <code>sgit_public_read_</code> prefix, and derived one-way from a vault key that is not in this repository. Read back with this key before it was published: 45 files, the same app.</span></div>

<p style="margin:18px 0 6px"><a href="{ui}" rel="noopener" target="_blank" style="display:inline-block;background:#0f766e;color:#fff;font-weight:800;font-size:20px;text-decoration:none;padding:14px 26px;border-radius:10px">Open the twin, full screen →</a> <a href="#live" style="margin-left:14px">or play it here, below</a></p>
<p class="small dim">Opens in the vault's own app, read-only, with the published key: the case, play and replay, the comparison, the three policies, the casebook and the four questions.</p>

<h2 id="live">Play it here</h2>
<p class="small dim" style="margin:.2rem 0 .9rem">Pick a design, pick a case, press Play. Step back and forward, show every step, or run the whole day. Under the designs, tick any controls to build your own.</p>
<div class="sgv-uiembed" data-vault="{vid}" data-readkey="{hexkey}" data-app="1"></div>
<script>
(function () {{
  ['vault-ui-embed.js'].forEach(function (f) {{
    fetch('../../../assets/' + f).then(function (r) {{ if (!r.ok) throw new Error(r.status); return r.text(); }}).then(function (t) {{ (0, eval)(t); }}).catch(function (e) {{ console.error('[vaults] ' + f + ' failed to load:', e); }});
  }});
}}());
</script>

<h2 id="results">The four designs, on the same thirteen cases</h2>
<ul>
<li><b>A, as described:</b> a $200 limit in the payment service, and complete logs.</li>
<li><b>B, secure, observe, respond:</b> tools bound to the sender, a cap at what was paid, a pause on bursts.</li>
<li><b>C, and verify:</b> an expected amount from the records before paying, and a nightly reconciliation.</li>
<li><b>D, three policies:</b> the agent proposes, a decision policy decides, the workflow pays, and precedents settle the cases rules miss.</li>
</ul>
<table>
<tr><th></th><th>Overpaid</th><th>Owed</th><th>Right</th><th>Min</th></tr>
<tr><td><b>A</b></td><td>$458</td><td>$341.60</td><td>1 of 13</td><td>0</td></tr>
<tr><td><b>B</b></td><td>$54</td><td>$222.60</td><td>4 of 13</td><td>3</td></tr>
<tr><td><b>C</b></td><td>$0</td><td>$0</td><td>12 of 13</td><td>57</td></tr>
<tr><td><b>D</b></td><td>$0</td><td>$0</td><td>13 of 13</td><td>18</td></tr>
</table>
<p class="small dim">"Owed" is what customers were still owed at the end of the day. "Right" means the right amount, to the right order, decided by the right decider. Min is minutes of a person's time on escalations: 6 minutes a case, 3 an approval. All numbers are from the twin's own engine, on synthetic cases.</p>

<h2 id="inside">What is in it</h2>
<table>
<tr><th>Path</th><th>What</th></tr>
<tr><td><code>index.html</code></td><td>The app: the case, play and replay, the comparison, the three policies, the casebook, the four questions; the data and the engine inlined.</td></tr>
<tr><td><code>content.json</code></td><td>Customers, orders, the thirteen cases, Northstar's refund rules, people's decisions, the ten controls, the four designs and the three policies.</td></tr>
<tr><td><code>engine.js</code></td><td>The deterministic engine: <code>NorthstarTwin.make(content).run(controls)</code> runs the cases in order and returns every step and outcome.</td></tr>
<tr><td><code>policies/</code></td><td>The behaviour, decision and workflow policies on their own.</td></tr>
<tr><td><code>cases/</code>, <code>orders/</code></td><td>One file per refund request and per order.</td></tr>
<tr><td><code>runs/</code></td><td>Every step of every case under each design, as the engine produced them.</td></tr>
<tr><td><code>tools/</code></td><td>The scripts that build all of it. Change the cases, the rules or the controls, and rebuild.</td></tr>
</table>

<h2 id="tour">A tour</h2>
{shots}
"""
    return newsroom_page(REL, "The Northstar refund twin: allowed is not right, in a vault",
                         "The refund in Ashish Rajan's article as a store you can run: thirteen synthetic refund requests, four designs of the controls, the three policies, every decision played step by step, replayed and compared, in an sgit vault you can open.",
                         body, eyebrow="A vault", crumbs=(("Replicate", "replicate/index.html"),),
                         lead="Thirteen refunds, four designs, every decision replayable, in a vault you can open.", wide=True)


if __name__ == "__main__":
    changed = write(REL, page())
    print(f"northstar_twin: {REL} {'written' if changed else 'unchanged'}")
