#!/usr/bin/env python3
"""The no-server studio: /demos/vaults/no-server-studio/index.html, an MVP of the no-server startup, in a vault.

    python3 admin/build/no_server_studio.py

The vault (iozssz56 on dev.send.sgraph.ai) is built outside this repository by its own tools/ (assemble.py,
bundle.py, synthetic_users.mjs, studio.js and components/); this page publishes its PUBLIC read key, embeds it with
assets/vault-ui-embed.js as the Pellbridge vault does, and shows what is in it. Only the public read key is kept here
(admin/content/vaults/no-server-studio.json); the vault key never enters the repository.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from page import newsroom_page, write  # noqa: E402
from mesa_ranch_vault import trail  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
REL = "demos/vaults/no-server-studio/index.html"
CRED = json.loads((ROOT / "admin/content/vaults/no-server-studio.json").read_text())

SHOTS = [
    ("studio.webp", "The studio: pick a sample or paste your own document, choose a layout and a theme, and the browser draws the infographic. With no model connected, a deterministic extractor stands in for it."),
    ("studio-night.webp", "The same engine, another document, the big-numbers layout and the night theme."),
    ("gallery.webp", "Every sample document in every layout, drawn live by the engine, and what you kept this session."),
    ("flow.webp", "The eight steps of the blueprint, walked in simulation: a passkey, a provider, credit bought at the provider, a cap, a generation that spends it, and what the studio would earn if providers paid a share."),
    ("plan.webp", "The business plan, for somebody to build: three businesses, packages and prices as hypotheses, go-to-market, ninety days, a calculator, risks as acceptances and open questions."),
    ("checklist.webp", "The blueprint's twelve steps, marked for this MVP, each with its evidence."),
    ("mobile.webp", "The studio on a phone."),
    ("live.webp", "The studio opened from its vault in the official vault UI, read-only, with the published key. The host reports no AI key for a public read, so the studio stays in simulation."),
]


def page():
    rk, vid = CRED["read_key"], CRED["vault_id"]
    hexkey = rk[len("sgit_public_read_"):]
    cred = f"{rk}:{vid}"
    ui = "https://dev.vault.sgraph.ai/#" + cred.replace(":", "%3A")
    shots = "\n".join(f'<figure><img src="images/{f}" alt="{a}" loading="lazy" style="width:100%;height:auto;border:1px solid #dcd7cb;border-radius:6px"><figcaption class="small dim">{a}</figcaption></figure>' for f, a in SHOTS)
    body = trail("no-server", "https://newsroom.sgit.ai/demos/vaults/no-server-studio/index.html") + f"""
<div class="note"><b>Most of this vault is simulated, on purpose.</b> The sample documents, the prices, the credit and every number in the business plan are invented or hypotheses. With no model connected, the studio uses a deterministic extractor in place of a model, so every feature works and every result replays. <a href="../../../articles/the-no-server-startup.html">The blueprint</a> makes the argument; <a href="../../../articles/inside-the-no-server-studio.html">the tour</a> says what is real and what is simulated.</div>

<div class="note"><b>Open it yourself. The key is the whole credential.</b><br>
Read key: <code style="word-break:break-all">{cred}</code><br>
In the official UI: <a href="{ui}" rel="noopener" target="_blank">open it read-only in a new tab</a> ·
From the CLI: <code style="word-break:break-all">sgit clone {cred}</code><br>
<span class="small dim">Published deliberately under the <code>sgit_public_read_</code> prefix, and derived one-way from a vault key that is not in this repository. Read back with this key before it was published: the same 46 files, the same studio.</span></div>

<p style="margin:18px 0 6px"><a href="{ui}" rel="noopener" target="_blank" style="display:inline-block;background:#0f766e;color:#fff;font-weight:800;font-size:20px;text-decoration:none;padding:14px 26px;border-radius:10px">Open the studio, full screen →</a> <a href="#live" style="margin-left:14px">or use it here, below</a></p>
<p class="small dim">Opens in the vault's own app, read-only: the studio, the gallery, the flow, the business plan with its calculator, and the checklist.</p>

<h2 id="live">Use it here</h2>
<p class="small dim" style="margin:.2rem 0 .9rem">Pick a document or paste your own, then try the layouts and themes. Open the flow and press each step. Open the business plan and change the calculator's numbers.</p>
<div class="sgv-uiembed" data-vault="{vid}" data-readkey="{hexkey}" data-app="1"></div>
<script>
(function () {{
  ['vault-ui-embed.js'].forEach(function (f) {{
    fetch('../../../assets/' + f).then(function (r) {{ if (!r.ok) throw new Error(r.status); return r.text(); }}).then(function (t) {{ (0, eval)(t); }}).catch(function (e) {{ console.error('[vaults] ' + f + ' failed to load:', e); }});
  }});
}}());
</script>

<h2 id="real">What is real, and what is simulated</h2>
<table>
<tr><th>Part</th><th>In this vault</th></tr>
<tr><td>The product</td><td>Real: one HTML file, seven native web components, no framework, no build step, no server.</td></tr>
<tr><td>Drawing the infographic</td><td>Real: the browser draws it as SVG, in four layouts and three themes.</td></tr>
<tr><td>Writing its content</td><td>Simulated by default, with a deterministic extractor. Inside the vault, the studio asks the host for a model through <code>sg.llm</code>; on a public read there is no key, so it says so and stays in simulation.</td></tr>
<tr><td>Your own key</td><td>Written and checked in code, not yet run against a live key: OpenRouter's OAuth when the studio is served as its own page, or a pasted key, held in memory only.</td></tr>
<tr><td>Passkey, credit, cap, revenue share</td><td>Simulated, in the flow, with invented money.</td></tr>
<tr><td>Synthetic users</td><td>Real: three personas walked the studio in a headless browser before it was published, and all their checks passed.</td></tr>
</table>

<h2 id="inside">What is in it</h2>
<table>
<tr><th>Path</th><th>What</th></tr>
<tr><td><code>index.html</code></td><td>The studio: seven web components, the engine and the data, inlined.</td></tr>
<tr><td><code>content.json</code></td><td>Sample documents, layouts, themes, the flow, the checklist and the business plan.</td></tr>
<tr><td><code>studio.js</code></td><td>The engine: <code>extract</code> (simulation), <code>prompt</code> and <code>parse</code> (a model), <code>render</code> (SVG).</td></tr>
<tr><td><code>components/</code></td><td>The seven components, one file each.</td></tr>
<tr><td><code>gallery/</code></td><td>Every sample in every layout, as SVG.</td></tr>
<tr><td><code>plan/</code></td><td>The business plan, for somebody to build, and the checklist.</td></tr>
<tr><td><code>tests/</code></td><td>What the three synthetic users saw.</td></tr>
<tr><td><code>tools/</code></td><td>The scripts that build all of it.</td></tr>
</table>

<h2 id="tour">A tour</h2>
{shots}
"""
    return newsroom_page(REL, "The no-server studio: an MVP of the no-server startup, in a vault",
                         "An infographic studio built to the no-server blueprint: one HTML file of native web components, your own model or a simulation, and a business plan for somebody to build, in an sgit vault you can open.",
                         body, eyebrow="A vault", crumbs=(("Replicate", "replicate/index.html"),),
                         lead="A product with no server of ours, mostly simulated, in a vault you can open.", wide=True)


if __name__ == "__main__":
    changed = write(REL, page())
    print(f"no_server_studio: {REL} {'written' if changed else 'unchanged'}")
