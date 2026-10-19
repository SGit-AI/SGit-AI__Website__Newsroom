#!/usr/bin/env python3
"""The Thistlewood decision twin: /demos/vaults/thistlewood-twin/index.html, Phil Venables' ten questions answered on one graph.

    python3 admin/build/thistlewood_twin.py

The vault (6v7kyxf4 on dev.send.sgraph.ai) is built outside this repository by its own tools/ (build_data.py,
assemble.py, bundle.py, engine.js); this page publishes its PUBLIC read key, embeds it with assets/vault-ui-embed.js
as the Northstar twin does, and shows what is in it. Only the public read key is kept here
(admin/content/vaults/thistlewood-twin.json); the vault key never enters the repository.
"""
import html
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from page import newsroom_page, write  # noqa: E402
from mesa_ranch_vault import trail  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
REL = "demos/vaults/thistlewood-twin/index.html"
CRED = json.loads((ROOT / "admin/content/vaults/thistlewood-twin.json").read_text())

SHOTS = [
    ("overview.webp", "The case: an invented retailer, its expected annual loss computed from the graph, 100 humans and agents, nine of sixteen risks accepted, and Phil Venables' ten questions."),
    ("graph.webp", "The whole company as one graph: the board, business risks, operational and technical risks, recurring causes, controls, processes, systems, suppliers and channels, and the people and agents with the largest reach."),
    ("graph-q9.webp", "Question 9 on the graph, with everything else faded: identity admins and deploy agents reach the secrets store and staff sign-on, and the path runs up to customer personal data exposed and the board."),
    ("graph-q7.webp", "Question 7: warehouse ransomware stops pick, pack and ship, a minimum viable process, through one supplier with no fallback."),
    ("q3.webp", "Question 3: the five most exposed business processes, security and reliability exposure for each, and the three things to do now, with their holders, cost and loss avoided."),
    ("q9.webp", "Question 9 as a table: the humans and agents with the largest blast radius, how much they reach through others, and how many systems each agent can reach beyond its behaviour policy's mandate."),
    ("decisions.webp", "The ledger: every decision the answers propose, by the person who holds it, with the door (fund, fix, accept, revisit), the interval, and the chain to the board."),
    ("evidence.webp", "Evidence and back-test: the answers rest on measured sources, and last year's incidents against the model, cause by cause."),
    ("live.webp", "The same app, opened from the vault in the official vault UI, read-only, with the published key."),
]


def page():
    rk, vid = CRED["read_key"], CRED["vault_id"]
    hexkey = rk[len("sgit_public_read_"):]
    cred = f"{rk}:{vid}"
    ui = "https://dev.vault.sgraph.ai/#" + cred.replace(":", "%3A")
    shots = "\n".join(f'<figure><img src="images/{f}" alt="{a}" loading="lazy" style="width:100%;height:auto;border:1px solid #dcd7cb;border-radius:6px"><figcaption class="small dim">{a}</figcaption></figure>' for f, a in SHOTS)
    body = trail("thistlewood", "https://newsroom.sgit.ai/demos/vaults/thistlewood-twin/index.html") + f"""
<div class="note"><b>Everything in this vault is synthetic.</b> Thistlewood Retail is invented, and so are its people, agents, suppliers, systems, incidents and every number. The ten questions are from Phil Venables, <a href="https://www.philvenables.com/post/a-cisos-ideal-management-tool" rel="noopener" target="_blank">A CISO's Ideal Management Tool</a> (19 October 2026). No model is called: the engine is a small deterministic program, so every answer replays exactly. <a href="../../../articles/ten-questions-one-graph.html">The reply</a> makes the argument; <a href="../../../articles/inside-the-thistlewood-twin.html">the tour</a> walks through the answers.</div>

<div class="note"><b>Open it yourself. The key is the whole credential.</b><br>
Read key: <code style="word-break:break-all">{cred}</code><br>
In the official UI: <a href="{ui}" rel="noopener" target="_blank">open it read-only in a new tab</a> ·
From the CLI: <code style="word-break:break-all">sgit clone {cred}</code><br>
<span class="small dim">Published deliberately under the <code>sgit_public_read_</code> prefix, and derived one-way from a vault key that is not in this repository. Read back with this key before it was published: the same files, the same app.</span></div>

<p style="margin:18px 0 6px"><a href="{ui}" rel="noopener" target="_blank" style="display:inline-block;background:#0f766e;color:#fff;font-weight:800;font-size:20px;text-decoration:none;padding:14px 26px;border-radius:10px">Open the twin, full screen →</a> <a href="#live" style="margin-left:14px">or use it here, below</a></p>
<p class="small dim">Opens in the vault's own app, read-only, with the published key: the case, the graph, the ten questions, the risk register from the board to the bytes, the decision ledger, and the evidence and back-test.</p>

<h2 id="live">Use it here</h2>
<p class="small dim" style="margin:.2rem 0 .9rem">Open the graph and pick a question: everything the answer did not use fades out. Or open the ten questions, one by one, with their evidence and the decisions they propose.</p>
<div class="sgv-uiembed" data-vault="{vid}" data-readkey="{hexkey}" data-app="1"></div>
<script>
(function () {{
  ['vault-ui-embed.js'].forEach(function (f) {{
    fetch('../../../assets/' + f).then(function (r) {{ if (!r.ok) throw new Error(r.status); return r.text(); }}).then(function (t) {{ (0, eval)(t); }}).catch(function (e) {{ console.error('[vaults] ' + f + ' failed to load:', e); }});
  }});
}}());
</script>

<h2 id="answers">The ten answers, in one line each</h2>
<table>
<tr><th>#</th><th>Question</th><th>What the graph says</th></tr>
""" + "\n".join(f"<tr><td>{a['n']}</td><td>{html.escape(a['title'])}</td><td>{html.escape(a['summary'])}</td></tr>" for a in json.loads((ROOT / "admin/content/vaults/thistlewood-answers.json").read_text())) + f"""
</table>
<p class="small dim">All figures are in thousands of pounds, from the twin's own engine, on an invented company.</p>

<h2 id="inside">What is in it</h2>
<table>
<tr><th>Path</th><th>What</th></tr>
<tr><td><code>index.html</code></td><td>The app: the case, the graph, the ten questions, board to bytes, the decisions and the evidence; the data and the engine inlined.</td></tr>
<tr><td><code>content.json</code></td><td>The graph: roles, channels, suppliers, systems, processes, risks, controls, incidents, events, scenarios and 100 identities with their privileges.</td></tr>
<tr><td><code>engine.js</code></td><td>The deterministic engine: <code>ThistlewoodTwin.make(content).ask(n)</code> answers question n and returns the rows, the nodes it used, its evidence and its proposed decisions.</td></tr>
<tr><td><code>answers/</code></td><td>Each answer as the engine produced it.</td></tr>
<tr><td><code>decisions/</code></td><td>29 proposed decisions, one file each, with holder, door, interval and the chain to the board.</td></tr>
<tr><td><code>graph/</code></td><td>Computed risk totals and the back-test.</td></tr>
<tr><td><code>tools/</code></td><td>The scripts that build all of it. Change the graph, rebuild, and every answer follows.</td></tr>
</table>

<h2 id="tour">A tour</h2>
{shots}
"""
    return newsroom_page(REL, "The Thistlewood decision twin: ten questions, one graph, in a vault",
                         "Phil Venables' ten acid-test questions for a CISO's management tool, answered as queries on one graph of an invented retailer: every answer with the part of the graph it came from, its evidence and the decisions it proposes, in an sgit vault you can open.",
                         body, eyebrow="A vault", crumbs=(("Replicate", "replicate/index.html"),),
                         lead="Ten questions, one graph, every answer traced to the board, in a vault you can open.", wide=True)


if __name__ == "__main__":
    changed = write(REL, page())
    print(f"thistlewood_twin: {REL} {'written' if changed else 'unchanged'}")
