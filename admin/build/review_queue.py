#!/usr/bin/env python3
"""The review queue: what each scheduled reviewer (ChatGPT, Perplexity) reviews next, one dated batch a day.

    python3 admin/build/review_queue.py              build reviews/queue/ (index.html, brief.md, <id>.json, <id>.md)
    python3 admin/build/review_queue.py --show ID    print ID's queue

Run after admin/build/reviews.py, which it reads the articles and the records from. A scheduled reviewer cannot
clone the repository and may not be able to run anything: it reads https://newsroom.sgit.ai/reviews/queue/<id>.md,
takes today's batch and answers with records (admin/content/reviews/brief.md, the prompt it is given). The editor
keeps the order in admin/content/reviews/queue.json; for each reviewer the queue is, in order:

  1. the editor's priority list, every article to every reviewer;
  2. articles the reviewer reviewed whose text has changed since, with its findings and their answers, to recheck;
  3. the backlog, newest first, never reviewed by this reviewer, dealt in turn between the scheduled reviewers so
     that between them the site is covered sooner (each still gets any article once the others have done it).

Batches are dated from the release that built them, so a reviewer that runs daily between releases still gets a
new batch each day; the lane refuses a second review of the same text (assets/reviews/record.js), so overlap costs
nothing worse than a wasted run.
"""
import argparse
import base64
import datetime
import fnmatch
import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from page import newsroom_page, write  # noqa: E402
from reviews import CRITERIA, CRITERIA_KEYS, answers, articles, e, records, reviewers, subnav  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
CFG = ROOT / "admin/content/reviews/queue.json"
BRIEF = ROOT / "admin/content/reviews/brief.md"
VAULTS = ROOT / "admin/content/reviews/vaults.json"
VAULT_KEYS = ROOT / "admin/content/reviews/keys"
OUT = ROOT / "reviews/queue"
SITE = "https://newsroom.sgit.ai"


def queues(today=None):
    cfg = json.loads(CFG.read_text(encoding="utf-8"))
    today = today or datetime.date.today()
    arts = [a for a in articles() if not any(fnmatch.fnmatch(a["slug"], p) for p in cfg.get("skip", []))]
    by = {a["slug"]: a for a in arts}
    recs, status = records()
    mine = {}                                         # reviewer -> slug -> [(file, record)]
    for f, r in recs:
        mine.setdefault(r["reviewer"], {}).setdefault(r["slug"], []).append((f, r))
    ids = list(cfg["reviewers"])
    out = {}
    for k, rid in enumerate(ids):
        rc = cfg["reviewers"][rid]
        done = mine.get(rid, {})
        current = {s for s, xs in done.items() if s in by and any(r.get("article_hash") == by[s]["hash"] for _, r in xs)}
        items, taken = [], set()

        def add(a, why, recheck=()):
            if a["slug"] in taken or a["slug"] in current:
                return
            taken.add(a["slug"])
            items.append({"slug": a["slug"], "title": a["title"], "date": a["date"], "version": a["version"], "hash": a["hash"],
                          "md": f"{SITE}/articles/{a['slug']}.md", "html": f"{SITE}/articles/{a['slug']}.html",
                          "why": why, "recheck": list(recheck)})
        for p in cfg.get("priority", []):
            if p["slug"] in by:
                add(by[p["slug"]], "The editor's priority. " + p.get("why", ""))
        for s, xs in sorted(done.items()):
            if s in by and s not in current:
                f, r = max(xs, key=lambda x: x[1].get("at") or "")
                ans = answers(status, s, f.name)
                rc_ = [{"finding": x["id"], "issue": x["issue"], "quote": x.get("quote", ""),
                        "answer": (ans.get(x["id"]) or {}).get("status", "open"), "note": (ans.get(x["id"]) or {}).get("note", "")}
                       for x in r.get("findings") or []]
                add(by[s], f"The text has changed since your review of {(r.get('at') or '')[:10]}: recheck your findings, then review the rest.", rc_)
        never = [a for a in arts if a["slug"] not in done]
        mine_first = [a for j, a in enumerate(never) if j % len(ids) == k]
        others = [a for j, a in enumerate(never) if j % len(ids) != k]
        for a in mine_first + others:
            n = sum(1 for xs in mine.values() if a["slug"] in xs)
            add(a, "Never reviewed by you" + (f"; {n} other reviewer{'s' if n != 1 else ''} have" if n else "; never reviewed by anyone") + ".")
        start = max(today, datetime.date.fromisoformat(rc.get("start", today.isoformat())))
        batch, days = int(rc.get("batch", 1)), int(cfg.get("days", 7))
        out[rid] = {"what": f"The review queue for {rid}: one batch a day. Take today's (UTC). The brief: {SITE}/reviews/queue/brief.md; the criteria: {SITE}/reviews/criteria.md.",
                    "reviewer": rid, "built": today.isoformat(), "criteria": CRITERIA, "batch": batch,
                    "brief": f"{SITE}/reviews/queue/brief.md", "criteria_md": f"{SITE}/reviews/criteria.md", "status": f"{SITE}/reviews/status.json",
                    "days": [{"date": (start + datetime.timedelta(days=d)).isoformat(), "articles": items[d * batch:(d + 1) * batch]}
                             for d in range(days) if items[d * batch:(d + 1) * batch]],
                    "remaining": max(0, len(items) - days * batch),
                    "skeleton": skeleton(rid)}
    return cfg, out


def skeleton(rid):
    return {"schema": "newsroom-review/v1", "criteria": CRITERIA, "slug": "", "article_version": "", "article_hash": "",
            "reviewer": rid, "kind": "agent", "model": "", "run_by": "", "at": "", "verdict": "", "summary": "",
            "checks": {k: {"result": "not-checked", "notes": ""} for k in CRITERIA_KEYS},
            "findings": [{"id": "f1", "criterion": "facts", "severity": "", "section": "", "quote": "", "issue": "", "verification": "",
                          "evidence": "", "source_passage": "", "method": "", "suggestion": ""}],
            "verified": [], "not_checked": []}


def md_of(q):
    lines = [f"# Review queue: {q['reviewer']}", "",
             f"Built {q['built']}, criteria {q['criteria']}. One batch a day: take **today's** (UTC). Read the brief first: {q['brief']}",
             f"(the criteria: {q['criteria_md']}). Answer with one record per article, each in its own fenced json block.", ""]
    for d in q["days"]:
        lines += [f"## {d['date']}", ""]
        for a in d["articles"]:
            lines += [f"- **{a['title']}** (`{a['slug']}`), published {a['date']}, text `{a['hash']}` at {a['version']}",
                      f"  - read: {a['md']} (and the page, which is canonical: {a['html']})",
                      f"  - article_hash: `{a['hash']}`, article_version: `{a['version']}`",
                      f"  - why: {a['why']}"]
            for x in a["recheck"]:
                lines.append(f"  - recheck {x['finding']} ({x['answer']}): {x['issue']}" + (f" Newsroom: {x['note']}" if x["note"] else ""))
        lines.append("")
    lines += [f"{q['remaining']} more after these." if q["remaining"] else "Nothing after these.", "",
              "The empty record, to fill (one per article):", "", "```json", json.dumps(q["skeleton"], indent=1), "```", ""]
    return "\n".join(lines)


SEND_BODY = """<div id="send-mount" class="send-box"><p class="dim">Loading&hellip;</p></div>
<noscript><p>Sending needs a script: this page checks and encrypts in your browser and sends nothing without one.</p></noscript>
<script type="module">
import { mountSend } from '../assets/reviews/send.js';
mountSend(document.getElementById('send-mount'));
</script>
<h2 id="what">What this page does</h2>
<ul>
<li><b>It finds the records</b> in whatever is pasted: a scheduled reviewer's whole answer, with its words around them, fenced or not. A record is a JSON object with <code>"schema": "newsroom-review/v1"</code>, as <a href="criteria.html#the-record">the criteria</a> describe it.</li>
<li><b>It checks each one</b> before anything is sent: the fields, the article and its current text, whether each quote is in it, and whether this reviewer has already reviewed this text. A record with an error is not sent; a warning is sent, and shown to the newsroom.</li>
<li><b>It seals them here</b> to the lane's public key (RSA-OAEP and AES-256-GCM, sgit's hybrid envelope) and appends them to the review lane, an append lane on a vault of the newsroom's. The vault server sees ciphertext, a size and a time.</li>
<li><b>This browser can add and cannot read.</b> Anyone with the link can send; nobody with it can read what was sent, not even this page.</li>
<li><b>The newsroom drains the lane</b> on a schedule, checks every record again, puts it on the record beside its article and answers each finding. What to review next is in <a href="queue/index.html">the review queue</a>.</li>
</ul>"""


def build():
    cfg, qs = queues()
    OUT.mkdir(parents=True, exist_ok=True)
    regs = {r["id"]: r for r in reviewers()}
    for rid, q in qs.items():
        (OUT / f"{rid}.json").write_text(json.dumps(q, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        (OUT / f"{rid}.md").write_text(md_of(q), encoding="utf-8")
    (OUT / "brief.md").write_text(BRIEF.read_text(encoding="utf-8"), encoding="utf-8")
    # the reviewers' vaults (card 092): their public read keys, and the desk's and the security agent's public keys
    vaults = json.loads(VAULTS.read_text(encoding="utf-8")) if VAULTS.exists() else {"reviewers": {}, "roles": {}}
    (ROOT / "reviews/vaults.json").write_text(json.dumps(vaults, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    (ROOT / "reviews/keys").mkdir(exist_ok=True)
    for f in sorted(VAULT_KEYS.glob("*.json")) if VAULT_KEYS.exists() else []:
        shutil.copyfile(f, ROOT / "reviews/keys" / f.name)
    from md import render
    brief = BRIEF.read_text(encoding="utf-8").split("\n", 1)[1]
    cols = []
    for rid, q in qs.items():
        rows = "".join(f'<tr><td>{e(d["date"])}</td><td>' + "<br>".join(
            f'<a href="../../articles/{e(a["slug"])}.html">{e(a["title"])}</a> <span class="dim">{e(a["hash"])}</span>'
            + (f' <span class="tchip">recheck {len(a["recheck"])}</span>' if a["recheck"] else "") for a in d["articles"]) + "</td></tr>"
            for d in q["days"])
        cols.append(f'<h3 id="{e(rid)}">{e((regs.get(rid) or {}).get("name", rid))} <span class="dim">{e(rid)}</span></h3>\n'
                    f'<p>{q["batch"]} a day. As <a href="{e(rid)}.md">markdown</a> and <a href="{e(rid)}.json">JSON</a>; {q["remaining"]} more after this week.</p>\n'
                    f'<div class="tablewrap"><table><thead><tr><th>Day</th><th>Articles</th></tr></thead><tbody>{rows}</tbody></table></div>')
    prio = "".join(f'<li><a href="../../articles/{e(p["slug"])}.html">{e(p["slug"])}</a>: {e(p.get("why", ""))}</li>' for p in cfg.get("priority", []))
    body = subnav("reviews/queue/index.html", "../../") + f"""<p>Reviewers outside the newsroom, ChatGPT and Perplexity first, run on their own schedules and take one batch a day from here. Each answers with records against <a href="../criteria.html">the criteria</a>, written to its own public vault (below) or sent through the review lane, which the newsroom drains on its own schedule and answers finding by finding on <a href="../index.html">the reviews page</a>.</p>
<h2 id="priority">The editor's priority</h2>
<p>Every reviewer gets these first, so each is checked by more than one vendor. Then each reviewer's own findings to recheck where the text changed, then the backlog, newest first, dealt between the reviewers in turn.</p>
<ol>{prio}</ol>
<h2 id="this-week">This week</h2>
{"".join(cols)}
<h2 id="vaults">The reviewers' vaults</h2>
<p>A reviewer that runs sgit takes its batch from its own public vault, where the review desk writes the same queue, signed. The vaults, their read keys and the keys that sign: <a href="../vaults.html">Vaults and keys</a>.</p>
<h2 id="brief">The brief</h2>
<p>The prompt each scheduled reviewer is given, word for word; also as <a href="brief.md">brief.md</a>.</p>
<div class="note">{render(brief)}</div>"""
    write("reviews/queue/index.html", newsroom_page(
        "reviews/queue/index.html", "The review queue", "What ChatGPT, Perplexity and any scheduled reviewer reviews next on newsroom.sgit.ai, one dated batch a day, and the brief they run on.",
        body, eyebrow=f"Reviews &middot; criteria {CRITERIA}", crumbs=(("Reviews", "reviews/index.html"),),
        lead="What each scheduled reviewer reviews next, one batch a day, and the brief it runs on.",
        agent="Your queue is reviews/queue/&lt;your id&gt;.md (or .json): take today's batch (UTC). The brief: reviews/queue/brief.md. The criteria: reviews/criteria.md. Answer with one newsroom-review/v1 record per article, each in a fenced json block; it reaches the newsroom through the review lane's send page, reviews/send.html."))
    write("reviews/send.html", newsroom_page(
        "reviews/send.html", "Send a review", "Send a review of a newsroom.sgit.ai article through the review lane: paste the reviewer's answer, check the records, and seal them to the newsroom's key.",
        subnav("reviews/send.html", "../") + SEND_BODY, eyebrow="Reviews &middot; the review lane", crumbs=(("Reviews", "reviews/index.html"),),
        head='<link rel="stylesheet" href="../assets/vault-pane/send.css">\n<link rel="stylesheet" href="../assets/reviews/send.css">\n',
        lead="Paste what a reviewer wrote. This page finds the review records in it, checks each one, and sends the good ones to the newsroom, sealed here to its key.",
        agent="reviews/send.html is the sending side of the review lane (assets/reviews/send.js, assets/reviews/record.js, assets/vault-pane/inbox.js). The link, in the fragment, is rv1.&lt;vault id&gt;.&lt;append token, hex&gt;.&lt;RSA-OAEP 3072 public key, SPKI, base64url&gt;; the page keeps it in localStorage sgit.reviews.link and removes it from the address. It wraps the checked records as {kind: 'newsroom-review/lane-v1', to: &lt;key fingerprint&gt;, sent_at, from, via, records, text}, seals it with sgit's hybrid envelope v2 and POSTs {append_token, payload} to https://dev.send.sgraph.ai/api/vault/append/write/&lt;vault id&gt;. The newsroom drains it with admin/build/review_lane.mjs drain."))
    vaults_page(vaults, regs)
    counts = ", ".join(f"{rid} {sum(len(d['articles']) for d in q['days'])}" for rid, q in qs.items())
    print(f"review_queue: article(s) queued for the week: {counts}")


def k1(bundle):
    """pki.sgit.ai's key link for a public bundle (message.js keyCode): anyone can seal to it and compare it. Public."""
    der = lambda pem: base64.b64decode("".join(l for l in pem.strip().splitlines() if not l.startswith("-----")))  # noqa: E731
    b = lambda x: base64.urlsafe_b64encode(x).decode().rstrip("=")  # noqa: E731
    return f"https://pki.sgit.ai/send/#k1.{b(der(bundle['encrypt']))}.{b(der(bundle['sign']))}.{b(bundle.get('label', '').encode())}"


def qr(text, label, title, note=""):
    return (f'<div class="rv-qr"><h4>{title}</h4><div data-qr="{e(text)}" data-qr-label="{e(label)}"></div>'
            + (f'<details><summary>The text</summary><p><code>{e(text)}</code></p></details>' if len(text) > 200 else f'<p><code>{e(text)}</code></p>')
            + f'{note}</div>')


def vaults_page(vaults, regs):
    """reviews/vaults.html: every public part of independent review, with QR codes, and what is private, and where (card 093)."""
    lane = json.loads((ROOT / "admin/content/reviews/lane.json").read_text(encoding="utf-8")) if (ROOT / "admin/content/reviews/lane.json").exists() else None
    keys = {n: json.loads((VAULT_KEYS / f"{n}.json").read_text()) for n in ("newsroom-desk", "newsroom-security") if (VAULT_KEYS / f"{n}.json").exists()}
    rows = []
    for rid, v in vaults.get("reviewers", {}).items():
        rows.append(f'<h3 id="{e(rid)}">{e((regs.get(rid) or {}).get("name", rid))} <span class="dim">{e(rid)}</span></h3>'
                    f'<p>Vault <code>{e(v["vault_id"])}</code> on {e(v.get("endpoint", ""))}, since {e(v.get("created", ""))}. The reviewer\'s own key: '
                    f'{"<code>" + e(v["reviewer_key"]) + "</code>, pinned" if v.get("reviewer_key") else "not pinned yet (its reviews are held until the editor confirms its fingerprint)"}. '
                    f'Its queue: <a href="queue/{e(rid)}.md">queue/{e(rid)}.md</a>.</p>'
                    '<div class="rv-qrs">' + qr(f'sgit clone {v["read_key"]}', f"The read key of {rid}'s vault", "Read it: the public read key",
                                                '<p class="dim">Anyone can clone it read-only: every file and every version.</p>') + '</div>')
    krows = []
    for n, b in keys.items():
        role = {"newsroom-desk": "@newsroom.desk, the review desk: signs the brief, the queue and the answers in every vault",
                "newsroom-security": "@newsroom.security, the security agent: signs its verdict on every file in every vault"}[n]
        krows.append(qr(k1(b), f"The key link of {n}", f"{e(role.split(':')[0])} <span class=\"dim\">{e(b['signing_fingerprint'])}</span>",
                        f'<p>{e(role.split(": ", 1)[1])}. <a href="keys/{n}.json">The bundle</a> (for <code>sgit pki import</code>), '
                        f'<a href="keys/{n}__submission.json">its register submission</a> (an agent identity, operated by the editor\'s key <code>sha256:db7f79fdd87e030a</code>).</p>'))
    lane_html = (f'<p>The review lane, for reviewers without a vault: vault <code>{e(lane["vault"])}</code>, its messages sealed to <code>{e(lane["fingerprint"])}</code>; '
                 f'the public half is <a href="../admin/content/reviews/lane.json">lane.json</a>. Its send link is given to each reviewer, not published: anyone holding it can add to the lane (never read it), and a public one would invite noise.</p>') if lane else ""
    retired = "".join(f'<li><b>{e(x["what"])} <code>{e(x["id"])}</code></b> ({e(x["made"])}): {e(x["why"])}</li>' for x in vaults.get("retired", []))
    roles = "".join(f"<li><b>{e(k)}</b>: {e(t)}</li>" for k, t in vaults.get("roles", {}).items())
    body = subnav("reviews/vaults.html", "../") + f"""<p>Everything a reviewer, or anyone checking on one, needs to find: each reviewer's vault and its read key, the keys that sign, where the verdicts are, and what is private and who holds it. Scan a code, or copy the text under it: they are the same.</p>
<h2 id="vaults">The reviewers' vaults</h2>
<p>One vault per reviewer from outside the newsroom. <b>Each is public on purpose</b>: anyone can see what the reviewer was asked and what it wrote. So nothing private goes in, from either side; the reviewer is told so first, the security agent looks for it in everything the reviewer writes, and the desk will not publish it.</p>
{"".join(rows) or '<p class="dim">None yet.</p>'}
<h2 id="keys">The keys that sign</h2>
<p>A reviewer follows only what verifies against the review desk's key, taken from this page, never from its vault; and the desk takes only what the security agent's signed verdict cleared. Two agents, two keys: the one that checks cannot take, and the one that takes cannot clear. The links open on pki.sgit.ai, where anyone can compare a key or seal a message to it.</p>
<div class="rv-qrs">{"".join(krows)}</div>
<p>The verdicts are on the repository's <a href="https://github.com/SGit-AI/SGit-AI__Website__Newsroom/tree/{e('review-gate')}/gate">review-gate branch</a>, one signed file per reviewer, once the first scheduled run has pushed one. Machine-readable: <a href="vaults.json">vaults.json</a>.</p>
<h2 id="roles">Who does what</h2>
<p>Each has a page with its role, its rules and the keys it may hold: <a href="../team/newsroom-reviews.html">@newsroom.reviews</a>, <a href="../team/newsroom-security.html">@newsroom.security</a>, <a href="../team/newsroom-vault.html">@newsroom.vault</a>, <a href="../team/openai-chatgpt.html">ChatGPT</a>, and <a href="../team/index.html">the rest of the team</a>.</p>
<ul>{roles}</ul>
<h2 id="private">What is private, and where it is</h2>
<p>Only the keys that write or sign. None of them is on this site or in the repository: each was sealed on pki.sgit.ai to the editor's key, and is kept in the environment of the agent that uses it.</p>
<div class="tablewrap"><table><thead><tr><th>Secret</th><th>What it does</th><th>Who holds it</th></tr></thead><tbody>
<tr><td>A reviewer's vault key</td><td>writes to its vault</td><td>the reviewer, and the review desk (<code>REVIEW_VAULT_KEY__&lt;ID&gt;</code>)</td></tr>
<tr><td>An SG/Send access token</td><td>lets a write reach the vault server</td><td>the reviewer, and the review desk</td></tr>
<tr><td>A reviewer's own signing key</td><td>signs what it writes</td><td>the reviewer only, in its own environment</td></tr>
<tr><td>The review desk's private key</td><td>signs the brief, the queue and the answers</td><td>@newsroom.desk (<code>NEWSROOM_DESK_KEY</code>)</td></tr>
<tr><td>The security agent's private key</td><td>signs the verdicts</td><td>@newsroom.security (<code>NEWSROOM_SECURITY_KEY</code>)</td></tr>
<tr><td>The review lane's secret</td><td>lists and opens what was sent to the lane</td><td>the newsroom's lane run (<code>REVIEW_LANE_SECRET</code>)</td></tr>
</tbody></table></div>
<h2 id="lane">The review lane</h2>
{lane_html}
<h2 id="retired">Retired</h2>
<p>Kept here so that nothing that was once published goes unexplained.</p>
<ul>{retired or '<li class="dim">Nothing.</li>'}</ul>
<script type="module" src="../assets/reviews/qr.js"></script>"""
    write("reviews/vaults.html", newsroom_page(
        "reviews/vaults.html", "Vaults and keys", "The public vaults of newsroom.sgit.ai's outside reviewers, their read keys as QR codes, the keys of the review desk and the security agent, and what is private and who holds it.",
        body, eyebrow="Reviews &middot; independent review", crumbs=(("Reviews", "reviews/index.html"),),
        head='<link rel="stylesheet" href="../assets/reviews/send.css">\n',
        lead="Each outside reviewer's public vault, the keys that sign what goes in and out of it, and the few secrets, named, with who holds them.",
        agent="Machine-readable: reviews/vaults.json (each reviewer's vault id and public read key, the roles, the retired vaults and keys) and reviews/keys/ (the review desk's and the security agent's public bundles, in the shape sgit pki export writes, and their pki.sgit.ai register submissions). A reviewer pins reviews/keys/newsroom-desk.json from this site and follows only vault files whose .sig verifies against it."))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--show")
    a = ap.parse_args()
    if a.show:
        print(md_of(queues()[1][a.show]))
        return
    build()


if __name__ == "__main__":
    main()
