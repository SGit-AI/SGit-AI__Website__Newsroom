#!/usr/bin/env python3
"""SGit × Ruflo, step by step: /demos/videos/sgit-ruflo-poc/index.html, an interactive walkthrough of Mondweep
Chakravorty's video "SGit × Ruflo | Working Proof of Concept".

    python3 admin/build/sgit_ruflo_video.py

The data is admin/content/videos/sgit-ruflo-poc.json, taken from the analysis vault's data/timeline.json, its
step-by-step page and its architecture addendum (every number traces to the timeline or a frame). The images in
demos/videos/sgit-ruflo-poc/images/ are frames of the video, used with its author's permission, and the stage
diagrams, pre-rendered from the addendum's Mermaid sources, so the page loads no external font, script or image.
Three articles tell the same run in prose; the trail `sgit-ruflo` joins all four pieces.
"""
import html
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from page import newsroom_page, write  # noqa: E402
from mesa_ranch_vault import trail  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
REL = "demos/videos/sgit-ruflo-poc/index.html"
HERE = "https://newsroom.sgit.ai/demos/videos/sgit-ruflo-poc/index.html"
D = json.loads((ROOT / "admin/content/videos/sgit-ruflo-poc.json").read_text())
UP = "../../../"
A1, A2, A3 = (UP + "articles/what-if-an-agent-loses-its-workspace.html", UP + "articles/when-is-the-vault-actually-used.html",
              UP + "articles/the-policy-guards-the-door.html")
TERM = {1: "01-pinned-runtime", 2: "02-define-mandate", 3: "03-store-facts", 4: "04-enforce-abp", 5: "05-encrypted-checkpoint",
        6: "06-approval-means-stop", 7: "07-remove-original", 8: "08-restore-fresh-process", 9: "09-ruflo-reads-memory",
        10: "10-negative-control", 11: "11-reject-altered-ciphertext", 12: "12-what-run-proves"}
e = html.escape


def mmss(s):
    s = int(round(s))
    return f"{s // 60}:{s % 60:02d}"


def yt(s):
    return f'{D["youtube"]}?t={int(round(s))}'


CSS = """<style>
.rf-board{display:grid;grid-template-columns:repeat(12,1fr);gap:5px;margin:1rem 0 .5rem}
.rf-board a{display:flex;flex-direction:column;justify-content:space-between;min-height:84px;padding:6px;border-radius:6px;text-decoration:none;font-weight:700;font-size:1.05rem;line-height:1.1}
.rf-board a{min-width:0;overflow-wrap:break-word;hyphens:auto}
.rf-board a small{font-weight:500;font-size:.68rem;line-height:1.15}
.rf-pass{background:#2F7A4E;color:#fff}.rf-blocked{background:#B23A1E;color:#fff}.rf-info{background:var(--panel);color:var(--fg);border:1px solid var(--line)}
.rf-key{display:flex;flex-wrap:wrap;gap:.3rem 1.1rem;font-size:.85rem;color:var(--dim);margin:.2rem 0 1rem}
.rf-key i{display:inline-block;width:.8rem;height:.8rem;border-radius:2px;margin-right:.35rem;vertical-align:-.1rem}
.rf-steps{list-style:none;margin:1rem 0;padding:0}
.rf-step{display:grid;grid-template-columns:2.6rem 1fr;gap:0 .9rem;padding-bottom:2.2rem;position:relative}
.rf-step::before{content:"";position:absolute;left:1.3rem;top:2.8rem;bottom:0;width:2px;background:var(--line)}
.rf-step:last-child::before{display:none}
.rf-num{width:2.6rem;height:2.6rem;border-radius:50%;display:grid;place-items:center;font-weight:700;background:var(--panel);border:1px solid var(--line)}
.rf-step.pass .rf-num{background:#2F7A4E;color:#fff;border-color:#2F7A4E}.rf-step.blocked .rf-num{background:#B23A1E;color:#fff;border-color:#B23A1E}
.rf-step h3{margin:.35rem 0 .2rem}
.rf-when{font-size:.86rem;color:var(--dim);margin:0 0 .4rem}
.rf-chip{display:inline-block;font-size:.8rem;font-weight:700;padding:2px 9px;border-radius:999px;border:1px solid var(--line);margin-left:.3rem}
.rf-step.pass .rf-chip{color:#2F7A4E;border-color:#2F7A4E}.rf-step.blocked .rf-chip{color:#B23A1E;border-color:#B23A1E}
.rf-roles{display:flex;flex-wrap:wrap;gap:6px;margin:.5rem 0}
.rf-roles span{font-size:.8rem;padding:2px 8px;border-radius:5px;border:1px solid}
.rf-r{background:#DCE6FA;border-color:#2B4C9B!important;color:#1d356f}.rf-a{background:#F7E3CF;border-color:#9A4F14!important;color:#6d370c}.rf-v{background:#D3EEE2;border-color:#2F7A4E!important;color:#1f5535}
.rf-off{background:transparent;border-style:dashed!important;border-color:var(--line)!important;color:var(--dim)}
.rf-stage img{max-width:560px;display:block;margin:.4rem auto}
.rf-step img,.rf-fig img{width:100%;height:auto;border:1px solid var(--line);border-radius:6px;background:#fff}
.rf-step details{margin:.5rem 0;border:1px solid var(--line);border-radius:8px;padding:.4rem .7rem;background:var(--panel)}
.rf-step summary{cursor:pointer;font-weight:600}
.rf-step pre{white-space:pre-wrap;word-break:break-word;font-size:.82rem;background:var(--term-bg,#111);color:#e8e8e8;padding:.6rem .7rem;border-radius:6px;margin:.5rem 0}
.rf-shown,.rf-inf{font-size:.9rem;margin:.35rem 0}
.rf-inf{font-style:italic;color:var(--dim)}
.rf-inf b,.rf-shown b{font-style:normal}
body.rf-hide-inf .rf-inf,body.rf-hide-inf .rf-dash{display:none}
.rf-links{font-size:.88rem;margin:.4rem 0 0;display:flex;flex-wrap:wrap;gap:.3rem 1rem}
.rf-ctl{display:flex;flex-wrap:wrap;gap:.6rem 1.4rem;align-items:center;background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:.6rem .9rem;margin:1rem 0;font-size:.92rem}
.rf-ctl label{cursor:pointer}
.rf-gloss{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:8px;margin:1rem 0}
.rf-gloss div{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:.5rem .7rem;font-size:.88rem}
.rf-matrix{width:100%;border-collapse:separate;border-spacing:0 4px;font-size:.88rem}
.rf-matrix td,.rf-matrix th{padding:5px 7px;text-align:left;vertical-align:top}
.rf-matrix td.on{font-weight:700}
.rf-poster{display:block;position:relative;text-decoration:none;margin:1rem 0}
.rf-poster span{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);background:#B23A1E;color:#fff;font-weight:800;font-size:1.15rem;padding:.7rem 1.3rem;border-radius:10px;box-shadow:0 4px 18px rgba(0,0,0,.3)}
@media (max-width:640px){.rf-board{grid-template-columns:repeat(4,1fr)}.rf-matrix .rf-what{display:none}}
</style>"""


def role_spans(st):
    out = []
    for k, cls, name in (("ruflo", "rf-r", "Ruflo"), ("abp", "rf-a", "ABP"), ("vault", "rf-v", "Vault")):
        v = st[k]
        off = v in ("–", "Not on path", "Not yet", "Not involved", "Not touched", "Named only", "Nothing written")
        out.append(f'<span class="{"rf-off" if off else cls}">{name}: {e(v)}</span>')
    return '<div class="rf-roles">' + "".join(out) + "</div>"


def step_block(s, slide):
    n, st = s["n"], s["stage"]
    frm, to = slide["video_from_s"], slide["video_to_s"]
    links = [f'<a href="{yt(frm)}" target="_blank" rel="noopener">Watch it at {mmss(frm)} &#8599;</a>',
             f'<a href="{A1}#step-{n}">In the walkthrough article</a>']
    if n in (5, 8, 11):
        links.append(f'<a href="{A2}#step-{n}">Why the vault matters here</a>')
    else:
        links.append(f'<a href="{A2}#answers">Where this sits in the architecture</a>')
    if n in (3, 9, 10):
        links.append(f'<a href="{A3}#paths">The path the policy does not see</a>')
    inferred = st["inferred"]
    inf_html = "" if inferred.strip().rstrip(".") in ("None", "Nothing important; the call is direct") else \
        f'<p class="rf-inf"><b>Inferred:</b> {e(inferred)}</p>'
    return f"""<li class="rf-step {s['cls']}" id="step-{n}">
<div class="rf-num" aria-hidden="true">{n}</div>
<div>
<h3>{e(s['title'])} <span class="rf-chip">{e(s['verdict'])}</span></h3>
<p class="rf-when">Video {mmss(frm)}–{mmss(to)} · run clock {e(slide.get('run_elapsed') or '')}</p>
<a href="images/slide-{TERM[n]}.webp"><img src="images/slide-{TERM[n]}.webp" alt="Step {n} of 12, the video's frame: {e(s['title'])}" loading="lazy"></a>
<p>{e(s['what'])}</p>
{role_spans(st)}
<details><summary>Command and output</summary>
<pre>$ {e(slide.get('command') or '')}</pre>
<pre>{e(slide.get('result') or '')}</pre>
<a href="images/term-{TERM[n]}.webp"><img src="images/term-{TERM[n]}.webp" alt="Step {n}: the terminal panel" loading="lazy"></a>
</details>
<details><summary>How the parts fit</summary>
<p>{e(st['intro'])}</p>
<a class="rf-stage" href="images/stage-{n:02d}.webp"><img src="images/stage-{n:02d}.webp" alt="Step {n}: which parts ran. Solid arrows are on screen; dashed are inferred." loading="lazy"></a>
<p><b>{e(st['takeaway'])}</b></p>
<p class="rf-shown"><b>Shown on screen:</b> {e(st['shown'])}</p>
{inf_html}
</details>
<p class="rf-links">{' · '.join(links)}</p>
</div></li>"""


def matrix():
    rows = []
    for s in D["steps"]:
        st = s["stage"]
        cells = []
        for k, cls in (("ruflo", "rf-r"), ("abp", "rf-a"), ("vault", "rf-v")):
            v = st[k]
            off = v in ("–", "Not on path", "Not yet", "Not involved", "Not touched", "Named only", "Nothing written")
            cells.append(f'<td class="{"" if off else "on " + cls}">{e(v)}</td>')
        rows.append(f'<tr><td><a href="#step-{s["n"]}">{s["n"]}</a></td><td class="rf-what">{e(s["title"])}</td>{"".join(cells)}</tr>')
    return ('<table class="rf-matrix"><tr><th>Step</th><th class="rf-what">What happens</th><th>Ruflo</th><th>ABP</th><th>Vault</th></tr>'
            + "".join(rows) + "</table>")


def page():
    slides = {s["n"]: s for s in D["slides"]}
    board = "".join(f'<a class="rf-{s["cls"]}" href="#step-{s["n"]}">{s["n"]}<small>{e(s["verdict"])}</small></a>' for s in D["steps"])
    steps = "\n".join(step_block(s, slides[s["n"]]) for s in D["steps"])
    body = trail("sgit-ruflo", HERE) + f"""
<a class="rf-poster" href="{D['youtube']}" target="_blank" rel="noopener"><img src="images/slide-00-intro.webp" alt="The video's opening slide: What if an agent loses its workspace?" style="width:100%;height:auto;border-radius:8px;border:1px solid var(--line)"><span>&#9654; Watch the video, {mmss(D['duration_s'])} &#8599;</span></a>

<p>Mondweep Chakravorty's video replays a real terminal run in twelve steps. Ruflo stores two facts. An adapter governed by an Agent Behaviour Policy saves Ruflo's memory as an encrypted checkpoint of SGit objects. The original project is deleted. A fresh process restores the checkpoint, and Ruflo reads both facts back exactly. Along the way three safeguards are tested, and all three hold. This page lets you step through it; <a href="{A1}">the walkthrough article</a> tells the same story in prose, <a href="{A2}">the architecture article</a> asks when the vault is actually used, and <a href="{A3}">the third</a> looks at the one path the policy does not see.</p>

<h2 id="board">The run at a glance</h2>
<div class="rf-board">{board}</div>
<p class="rf-key"><span><i style="background:#2F7A4E"></i>Worked</span><span><i style="background:#B23A1E"></i>Safeguard refused it, as intended</span><span><i style="background:var(--panel);border:1px solid var(--line)"></i>Setup or summary</span></p>
<p class="small dim">Not tested, and said so on screen: recall by meaning. Embeddings were switched off.</p>

<h2 id="words">Six words you will see</h2>
<div class="rf-gloss">
<div><b>Ruflo</b>: rUv's open-source agent orchestration (MIT). Here only its memory commands and its memory file are used.</div>
<div><b>MCP</b>: the Model Context Protocol, a standard way for an agent to call tools. Here, a local server with three tools.</div>
<div><b>ABP</b>: an Agent Behaviour Policy. Here, four rows saying what may be done in the project, and what needs approval.</div>
<div><b>Checkpoint</b>: a saved recovery copy of Ruflo's memory database.</div>
<div><b>SGit</b>: an encrypted, versioned store. Here the checkpoint is kept as encrypted SGit objects on the same machine.</div>
<div><b>Fresh process</b>: a brand-new server process, so nothing from before survives in its memory.</div>
</div>

<div class="rf-ctl"><b>Reading options</b>
<label><input type="checkbox" id="rf-inf" checked> Show what is inferred, not only what is on screen</label>
<label><input type="checkbox" id="rf-open"> Open every step's details</label></div>

<h2 id="steps">The run, step by step</h2>
<p class="small dim">Each picture is the video's frame just before the slide changes, so the terminal output is complete. Tap one to enlarge it. Times link to that moment in the video.</p>
<ol class="rf-steps">
{steps}
</ol>

<h2 id="matrix">Who does what, per step</h2>
<p>Ruflo's command line, the ABP and the vault, step by step. The vault is written or read in three steps: 5, 8 and 11. <a href="{A2}">When is the vault actually used?</a> explains why that is the honest answer, not a criticism.</p>
{matrix()}

<h2 id="map">How the parts fit</h2>
<figure class="rf-fig"><a href="images/map.webp"><img src="images/map.webp" alt="The component map: the test script, Ruflo, the ABP adapter with the SGit library, and the machine's disk" loading="lazy"></a>
<figcaption class="small dim">Blue is Ruflo, amber the ABP adapter, green SGit and the vault, grey plain files; dashed boxes were not used. Solid arrows are on screen; dashed are inferred.</figcaption></figure>
<figure class="rf-fig"><a href="images/where.webp"><img src="images/where.webp" alt="Where the video's vault lives: on one machine, with no vault server used" loading="lazy"></a>
<figcaption class="small dim">Where the vault lives: one machine. Encryption happens there and the ciphertext stays there, so it survives the project being deleted, not the machine being lost.</figcaption></figure>

<h2 id="outcome">The outcome</h2>
<figure class="rf-fig"><a href="images/slide-13-outcome.webp"><img src="images/slide-13-outcome.webp" alt="The video's outcome slide" loading="lazy"></a></figure>
<p>On screen: both facts recovered exactly; unauthorised access blocked; unapproved deletion blocked; an altered checkpoint rejected. Still to validate, in the video's own words: recall by meaning, real-world value, and installation and ongoing reliability.</p>

<div class="provenance">
  <b>First published {D['published']}</b>: the video <a href="{D['youtube']}">"{e(D['title'])}"</a> by Mondweep Chakravorty, member of the #Ruflo-Federation (<a href="https://www.linkedin.com/in/mondweepchakravorty/">LinkedIn</a>), published here with his agreement.
  <p class="dim small" style="margin:.4em 0 0">Analysis: {e(D['analysis'])}. The frames are his and are not covered by this site's CC BY 4.0 licence; the diagrams, the board and the text are this site's. Curation: AI-written analysis of a third-party video, every number traced to the video's timeline or a frame, with what is inferred labelled as inferred.</p>
</div>

<script>
(function () {{
  var inf = document.getElementById('rf-inf'), op = document.getElementById('rf-open');
  inf.addEventListener('change', function () {{ document.body.classList.toggle('rf-hide-inf', !inf.checked); }});
  op.addEventListener('change', function () {{ document.querySelectorAll('.rf-step details').forEach(function (d) {{ d.open = op.checked; }}); }});
  if (location.hash) {{ var t = document.querySelector(location.hash); if (t) t.querySelectorAll && t.querySelectorAll('details').forEach(function (d) {{ d.open = true; }}); }}
}}());
</script>
"""
    agent = ("This page is a walkthrough of a recorded run, not a live system. Every number on it comes from the video's "
             "timeline or a frame. Keep what is shown on screen apart from what is inferred, as the page does: the video shows "
             "no vault server, push or clone; Ruflo's hive-mind and its own policy engine were not used; recall by meaning was "
             "not tested. The frames belong to Mondweep Chakravorty. The three articles linked at the top tell the same run in prose.")
    return newsroom_page(REL, "SGit × Ruflo, step by step",
                         "An interactive walkthrough of Mondweep Chakravorty's video: Ruflo's memory saved as an encrypted SGit checkpoint, the project deleted, and the memory restored in a fresh process, with three safeguards tested.",
                         body, eyebrow="A video, step by step", crumbs=(),
                         lead="What if an agent loses its workspace? Twelve steps, each with its frame, its command and output, and which parts ran.",
                         agent=agent, head=CSS)


if __name__ == "__main__":
    changed = write(REL, page())
    print(f"sgit_ruflo_video: {REL} {'written' if changed else 'unchanged'}")
