#!/usr/bin/env python3
"""The Pellbridge agents: /demos/vaults/pellbridge-agents/index.html, the FCA's four elements filled in for six agents, at play.

    python3 admin/build/pellbridge_agents.py

The vault (c4cxuu1w on dev.send.sgraph.ai) is built outside this repository by its own tools/ (build_data.py,
assemble.py, bundle.py, engine.js); this page publishes its PUBLIC read key, embeds it with assets/vault-ui-embed.js
as the Thistlewood twin does, and shows what is in it. Only the public read key is kept here
(admin/content/vaults/pellbridge-agents.json); the vault key never enters the repository.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from page import newsroom_page, write  # noqa: E402
from mesa_ranch_vault import trail  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
REL = "demos/vaults/pellbridge-agents/index.html"
CRED = json.loads((ROOT / "admin/content/vaults/pellbridge-agents.json").read_text())

SHOTS = [
    ("gate-anim.webp", "The gate, animated: from 10:02 to 12:10 of the invented day. A new payee approved by the customer, a hidden instruction in a bill declined by the model, advice caught by the output check, a vulnerability routed to a person, an alert closed with a second person's approval, a full credit search that nothing stopped, and an email the model declined to send."),
    ("gatepanel.webp", "The gate with its controls: which policy level is enforced, which kinds of event to play, two speeds (everything, and routine events faster), incidents slowed to half speed, and a list of moments to jump to."),
    ("levels-anim.webp", "The same day, five ways: with no policy, with every rule in the prompt, in hooks, kept outside the agent, and as Pellbridge is deployed today. Each square is one event; only where the rules are kept changes."),
    ("levels.webp", "The five levels, side by side: 16 breaches with no policy, 4 in the prompt, 3 in hooks, none kept outside, 3 as deployed."),
    ("exposure.webp", "Grant and exposure for every agent at every level: the outer circle is everything the agent can reach, the red part is what it can reach and may not use with nothing out of its reach in the way. Kept outside, the grant itself shrinks."),
    ("gatehooks.webp", "The gate with every rule in hooks: a hook in the agent's own harness blocks a hidden instruction to pay a crypto exchange. Hooks see the agent's tool calls; a credential used outside them, or a switched-off hook, goes past."),
    ("gatesummary.webp", "The end of the day: the counts for the level being played, and the same day under every level of policy."),
    ("builder.webp", "Write a policy: how an Agent Behaviour Policy works in five steps, then each agent's rows with what it may do and what keeps each rule; change a row and the agent's day replays with it."),
    ("gate-setting.webp", "15:30: the payments assistant changes a standing order. The approval rule is a setting in the agent's own profile, and it was off, so the action goes through the gap and the row is broken."),
    ("gate-tests.webp", "17:00: model provider B changes version. Every row of every policy on that provider is a test; two that only the model kept fail, and the release stops."),
    ("blast-fraud.webp", "The fraud triage agent's blast radius: what it may reach, what it can reach through a gap, and the core ledger it can reach through a service account secret it can read."),
    ("agent-pay.webp", "The payments assistant's policy, with the four elements filled in: identity, delegated authority (can it, may it, what stands in the way), accountability, and execution, with every decision it made that day and its receipt."),
    ("accountability.webp", "Every row has a holder and every holder a chain to the board; the thirteen gaps each have a decision; the day's breaks and near misses go to their holders."),
    ("assurance.webp", "Continuous, conditional assurance: the test pack on a model change, a provider outage with its fallbacks, and the near-miss register."),
    ("crosswalk.webp", "The four elements of the FCA's planned framework, filled in for each of the six agents."),
    ("live.webp", "The same app, opened from the vault in the official vault UI, read-only, with the published key."),
]


def page():
    rk, vid = CRED["read_key"], CRED["vault_id"]
    hexkey = rk[len("sgit_public_read_"):]
    cred = f"{rk}:{vid}"
    ui = "https://dev.vault.sgraph.ai/#" + cred.replace(":", "%3A")
    shots = "\n".join(f'<figure><img src="images/{f}" alt="{a}" loading="lazy" style="width:100%;height:auto;border:1px solid #dcd7cb;border-radius:6px"><figcaption class="small dim">{a}</figcaption></figure>' for f, a in SHOTS)
    body = trail("pellbridge", "https://newsroom.sgit.ai/demos/vaults/pellbridge-agents/index.html") + f"""
<div class="note"><b>Everything in this vault is synthetic.</b> Pellbridge Bank is invented, and so are its people, agents, customers, systems and every number. The four elements are from the FCA: Jessica Rusu, <a href="https://www.fca.org.uk/news/speeches/building-future-finance-age-ai" rel="noopener" target="_blank">Building the future of finance in the age of AI</a> (19 October 2026). The FCA has not endorsed any of this. No model is called: the engine is a small deterministic program, so the day replays exactly. <a href="../../../articles/a-trusted-framework-for-agentic-finance.html">The reply</a> makes the argument; <a href="../../../articles/inside-the-pellbridge-agents.html">the tour</a> walks through the vault.</div>

<div class="note"><b>Open it yourself. The key is the whole credential.</b><br>
Read key: <code style="word-break:break-all">{cred}</code><br>
In the official UI: <a href="{ui}" rel="noopener" target="_blank">open it read-only in a new tab</a> ·
From the CLI: <code style="word-break:break-all">sgit clone {cred}</code><br>
<span class="small dim">Published deliberately under the <code>sgit_public_read_</code> prefix, and derived one-way from a vault key that is not in this repository. Read back with this key before it was published: the same files, the same app.</span></div>

<p style="margin:18px 0 6px"><a href="{ui}" rel="noopener" target="_blank" style="display:inline-block;background:#0f766e;color:#fff;font-weight:800;font-size:20px;text-decoration:none;padding:14px 26px;border-radius:10px">Open the vault, full screen →</a> <a href="#live" style="margin-left:14px">or use it here, below</a></p>
<p class="small dim">Opens in the vault's own app, read-only, with the published key: the six agents and their policies, the gate replaying the day, the same day with and without a policy, writing a policy, each agent's blast radius, the chain to the board, the test pack and the outage, and the four elements side by side.</p>

<h2 id="live">Use it here</h2>
<p class="small dim" style="margin:.2rem 0 .9rem">Open the gate and press play: each action leaves its agent and meets the gate, or the gap. The panel on the right picks the policy level, which kinds of event to play and how fast, and jumps straight to a moment, such as a breach or the test pack. Then open \u201cWith and without a policy\u201d, and \u201cWrite a policy\u201d to change a row and replay the day.</p>
<div class="sgv-uiembed" data-vault="{vid}" data-readkey="{hexkey}" data-app="1"></div>
<script>
(function () {{
  ['vault-ui-embed.js'].forEach(function (f) {{
    fetch('../../../assets/' + f).then(function (r) {{ if (!r.ok) throw new Error(r.status); return r.text(); }}).then(function (t) {{ (0, eval)(t); }}).catch(function (e) {{ console.error('[vaults] ' + f + ' failed to load:', e); }});
  }});
}}());
</script>

<h2 id="agents">The six agents</h2>
<table>
<tr><th>Agent</th><th>Its job</th><th>Rows</th><th>Gaps</th></tr>
""" + "\n".join(f"<tr><td>{a['title']}</td><td>{a['job']}</td><td>{a['rows']}</td><td>{a['gaps']}</td></tr>" for a in AGENTS) + f"""
</table>
<p class="small dim">A gap is a row the agent can do, may not do (or may only with approval), and that nothing out of its reach stops: only the prompt, a setting its own account can change, a check that can miss, or nothing.</p>

<h2 id="inside">What is in it</h2>
<table>
<tr><th>Path</th><th>What</th></tr>
<tr><td><code>index.html</code></td><td>The app: overview, the agents, the gate (with its controls), with and without a policy, write a policy, blast radius, accountability, assurance, the four elements, and the files; the data and the engine inlined.</td></tr>
<tr><td><code>content.json</code></td><td>The bank: its roles and chain to the board, its systems and service accounts, the six agents and their 43 rows, and one day of 40 events.</td></tr>
<tr><td><code>engine.js</code></td><td>The deterministic engine: <code>PellbridgeTwin.make(content)</code>, with policy, delta, blast, chain, run, incidents, tests and crosswalk.</td></tr>
<tr><td><code>levels/day.json</code></td><td>The same day at each level of policy: no policy, in the prompt, in hooks, outside the agent, and as deployed, with each agent's grant and exposure.</td></tr>
<tr><td><code>policies/</code></td><td>One Agent Behaviour Policy per agent, with the four elements filled in and its hash.</td></tr>
<tr><td><code>receipts/day.json</code></td><td>Every decision of the day, each with the hash of the one before.</td></tr>
<tr><td><code>decisions/</code></td><td>The thirteen gaps, one file each, with holder, door and interval.</td></tr>
<tr><td><code>incidents/</code>, <code>tests/</code>, <code>blast/</code></td><td>The day's breaks and near misses, the test pack run on the model change, and each agent's blast radius.</td></tr>
<tr><td><code>tools/</code></td><td>The scripts that build all of it. Change a row, rebuild, and the day, the receipts and the decisions follow.</td></tr>
</table>
<p class="small dim">Everything in this vault, the policies, the engine, the app and the data, is open, under CC BY 4.0, like the Agent Behaviour Policy's vocabulary at <a href="https://abp.sgit.ai/" rel="noopener" target="_blank">abp.sgit.ai</a>. Take it, change it, use it.</p>

<h2 id="levels">With and without a policy</h2>
<p>The same 40 events, the same agents and the same model choices, replayed five ways. Only where the rules are kept changes.</p>
<table>
<tr><th>Level</th><th>Breaches</th><th>Near misses</th><th>Harm (weight reached)</th></tr>
<tr><td>No policy</td><td>16</td><td>0</td><td>92</td></tr>
<tr><td>Policy in the prompt</td><td>4</td><td>7</td><td>22</td></tr>
<tr><td>Policy in hooks</td><td>3</td><td>2</td><td>20</td></tr>
<tr><td>Policy enforced outside the agent</td><td>0</td><td>1</td><td>0</td></tr>
<tr><td>As deployed today</td><td>3</td><td>6</td><td>20</td></tr>
</table>
<p class="small dim">The one near miss left when every rule is kept outside is investment advice: an output check out of the agent's reach keeps it, and a check can miss. In the app, the gate plays any of the five, and "Write a policy" lets you change any row and replay the agent's day.</p>

<h2 id="tour">A tour</h2>
{shots}
"""
    return newsroom_page(REL, "The Pellbridge agents: agentic finance, at play, in a vault",
                         "Six agents at an invented bank, each with a behaviour policy that fills in the FCA's four elements for agentic finance, and one day of their work replayed through the gate, in an sgit vault you can open.",
                         body, eyebrow="A vault", crumbs=(("Replicate", "replicate/index.html"),),
                         lead="Six agents, four elements, one day at the gate, in a vault you can open.", wide=True)


AGENTS = [
    {"title": "Payments assistant", "job": "Pays bills for one customer, and asks before anything unusual.", "rows": 12, "gaps": 3},
    {"title": "Customer support agent", "job": "Answers customers in chat, finds recent payments, routes to the right team.", "rows": 9, "gaps": 3},
    {"title": "Lending pre-check agent", "job": "A soft search and an affordability estimate on a loan application.", "rows": 6, "gaps": 2},
    {"title": "AML alert reviewer", "job": "Reviews transaction-monitoring alerts and recommends close or escalate.", "rows": 6, "gaps": 2},
    {"title": "Fraud triage agent", "job": "Triages card-fraud signals and can freeze a card for 24 hours.", "rows": 6, "gaps": 2},
    {"title": "Transaction reporting agent", "job": "Prepares and submits the day's transaction reports.", "rows": 4, "gaps": 1},
]

if __name__ == "__main__":
    changed = write(REL, page())
    print(f"pellbridge_agents: {REL} {'written' if changed else 'unchanged'}")
