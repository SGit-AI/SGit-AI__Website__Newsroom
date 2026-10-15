#!/usr/bin/env python3
"""The accountant: what the wires' pictures cost, on one page and in one file, from every ledger the pipeline writes.

    (called by admin/build/wire.py; also) python3 admin/build/accountant.py

The owner asked (14 October 2026) for an accountant in the mix: "really capture the cost of all these runs, and the cost per
edition and the cost per work... and provide visibility on this". The role is @newsroom.accountant: it writes nothing of its
own and spends nothing; it reads what admin/build/infographics.py recorded (wire/<slug>/infographics/<edition>/ledger.json,
one row per image with OpenRouter's own cost, and the cumulative ledger beside it, with the key's budget as OpenRouter last
reported it) and sums it every way a reader might ask: by wire, by edition, by month, by model, by kind (a hero, a card),
and per piece of work (what a card costs, what a hero costs, what an edition cost, what a story's picture cost). The page is
wire/costs.html; the data is wire/costs.json (wire-costs/v1), so an agent can read it without the page.

What is not here: the cost of the desks' runs (their models and tokens are in their own sessions, not in any vault) and the
cost of this site's own sessions. The page says so, so that "what it costs" is read as what it is: the pictures, to the cent.
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from page import esc  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
ROLE = "newsroom.accountant"


def load(f: Path):
    try:
        return json.loads(f.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def gather(cfgs):
    """Every wire's ledgers, read; the sums; the latest key budget any run recorded."""
    wires, by_month, by_model, by_kind, budget = [], {}, {}, {}, None
    for cfg in cfgs:
        root = ROOT / cfg["dir"] / "infographics"
        total = load(root / "ledger.json") if (root / "ledger.json").exists() else None
        editions = []
        for f in sorted(root.glob("*/ledger.json")) if root.exists() else []:
            led = load(f) or {}
            rows = [e for e in led.get("images", []) if isinstance(e, dict)]
            done = [e for e in rows if e.get("status") == "done"]
            for e in done:
                m = str(e.get("at") or "")[:7] or "unknown"
                for table, key in ((by_month, m), (by_model, str(e.get("model") or "unknown")), (by_kind, str(e.get("kind") or "unknown"))):
                    r = table.setdefault(key, {"images": 0, "cost_usd": 0.0, "duration_s": 0.0})
                    r["images"] += 1; r["cost_usd"] = round(r["cost_usd"] + (e.get("cost_usd") or 0), 6); r["duration_s"] = round(r["duration_s"] + (e.get("duration_s") or 0), 1)
            heroes = [e for e in done if e.get("kind") == "hero"]
            cards = [e for e in done if e.get("kind") == "card"]
            editions.append({
                "edition": led.get("edition") or f.parent.name, "updated": led.get("updated"),
                "images": len(done), "failed": sum(1 for e in rows if e.get("status") == "failed"), "cost_usd": round(sum(e.get("cost_usd") or 0 for e in done), 6),
                "duration_s": round(sum(e.get("duration_s") or 0 for e in done), 1),
                "heroes": len(heroes), "cards": len(cards),
                "hero_cost_usd": round(sum(e.get("cost_usd") or 0 for e in heroes), 6), "card_cost_usd": round(sum(e.get("cost_usd") or 0 for e in cards), 6),
                "stopped": led.get("stopped"),
                "rows": [{k: e.get(k) for k in ("id", "kind", "model", "model_wanted", "cost_usd", "duration_s", "at", "file", "status")} for e in rows],
            })
        if total and isinstance(total.get("key_budget"), dict):
            b = total["key_budget"]
            if not budget or str(b.get("at") or "") > str(budget.get("at") or ""):
                budget = b
        wires.append({"slug": cfg["slug"] or "industry", "name": cfg["name"], "dir": cfg["dir"], "editions": editions,
                      "images": sum(e["images"] for e in editions), "cost_usd": round(sum(e["cost_usd"] for e in editions), 6),
                      "failed": sum(e["failed"] for e in editions)})
    images = sum(w["images"] for w in wires)
    cost = round(sum(w["cost_usd"] for w in wires), 6)
    heroes, cards = by_kind.get("hero", {}), by_kind.get("card", {})
    per_work = {
        "hero_usd": round(heroes["cost_usd"] / heroes["images"], 4) if heroes.get("images") else None,
        "card_usd": round(cards["cost_usd"] / cards["images"], 4) if cards.get("images") else None,
        "edition_usd": round(cost / sum(len(w["editions"]) for w in wires), 4) if any(w["editions"] for w in wires) else None,
        "image_usd": round(cost / images, 4) if images else None,
        "seconds_per_image": round(sum(r["duration_s"] for r in by_kind.values()) / images, 1) if images else None,
    }
    return {
        "schema": "wire-costs/v1", "kept_by": ROLE, "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "what": "What the wires' pictures cost: every image the pipeline made (admin/build/infographics.py), with OpenRouter's own cost per image, summed by wire, edition, month, model and kind, and per piece of work. Not here: the desks' own runs and this site's sessions.",
        "total": {"images": images, "cost_usd": cost, "failed": sum(w["failed"] for w in wires)},
        "per_work": per_work, "by_month": dict(sorted(by_month.items())), "by_model": dict(sorted(by_model.items(), key=lambda kv: -kv[1]["cost_usd"])), "by_kind": by_kind,
        "key_budget": budget, "wires": wires,
    }


def usd(x):
    return "—" if x is None else f"${x:,.2f}" if x >= 1 else f"${x:.3f}"


def bar(x, mx):
    w = 0 if not mx or x is None else max(2, round(100 * x / mx))
    return f'<span class="bar" aria-hidden="true"><i style="width:{w}%"></i></span>'


def costs_html(data, cfgs, strip, newsroom_page, eyebrow):
    t, pw, b = data["total"], data["per_work"], data.get("key_budget")
    tiles = "".join(f'<div class="tile"><b>{esc(v)}</b><span>{esc(k)}</span></div>' for k, v in (
        ("spent on pictures", usd(t["cost_usd"])), ("images made", f'{t["images"]}'), ("a hero costs", usd(pw["hero_usd"])), ("a card costs", usd(pw["card_usd"])),
        ("an edition costs", usd(pw["edition_usd"])), ("seconds per image", "—" if pw["seconds_per_image"] is None else f'{pw["seconds_per_image"]}')))
    if b:
        tiles += f'<div class="tile"><b>{esc(usd(b.get("remaining_usd")))}</b><span>left on the key of {esc(usd(b.get("limit_usd")))}, as OpenRouter said at {esc(str(b.get("at") or "")[:16].replace("T", " "))} UTC</span></div>'
    mx_w = max([w["cost_usd"] for w in data["wires"]] + [0])
    wires_rows = "".join(f'<tr><td><a href="../{esc(w["dir"])}index.html">{esc(w["name"])}</a></td><td class="n">{len(w["editions"])}</td><td class="n">{w["images"]}</td><td class="n">{w["failed"]}</td><td class="n">{esc(usd(w["cost_usd"]))}</td><td>{bar(w["cost_usd"], mx_w)}</td></tr>' for w in data["wires"])
    months = data["by_month"]; mx_m = max([r["cost_usd"] for r in months.values()] + [0])
    month_rows = "".join(f'<tr><td>{esc(m)}</td><td class="n">{r["images"]}</td><td class="n">{esc(usd(r["cost_usd"]))}</td><td>{bar(r["cost_usd"], mx_m)}</td></tr>' for m, r in months.items())
    models = data["by_model"]
    model_rows = "".join(f'<tr><td><code>{esc(m)}</code></td><td class="n">{r["images"]}</td><td class="n">{esc(usd(r["cost_usd"]))}</td><td class="n">{esc(usd(r["cost_usd"] / r["images"]))}</td><td class="n">{round(r["duration_s"] / r["images"], 1)} s</td></tr>' for m, r in models.items())
    eds = [(w, e) for w in data["wires"] for e in w["editions"]]
    mx_e = max([e["cost_usd"] for _, e in eds] + [0])
    ed_rows = "".join(
        f'<tr><td>{esc(w["name"])}</td><td><a href="../{esc(w["dir"])}infographics/{esc(e["edition"])}/ledger.json">{esc(e["edition"])}</a></td>'
        f'<td class="n">{e["heroes"]} + {e["cards"]}</td><td class="n">{e["failed"]}</td><td class="n">{esc(usd(e["cost_usd"]))}</td><td class="n">{esc(usd(e["card_cost_usd"] / e["cards"]) if e["cards"] else "—")}</td>'
        f'<td>{bar(e["cost_usd"], mx_e)}</td><td class="dim">{esc(e["stopped"] or "")}</td></tr>' for w, e in sorted(eds, key=lambda x: x[1]["edition"], reverse=True))
    image_rows = "".join(
        f'<tr><td>{esc(w["name"])}</td><td>{esc(e["edition"])}</td><td><code>{esc(str(r.get("id") or ""))}</code></td><td>{esc(str(r.get("kind") or ""))}</td><td><code>{esc(str(r.get("model") or r.get("model_wanted") or ""))}</code></td>'
        f'<td class="n">{esc(usd(r.get("cost_usd")) if r.get("status") == "done" else str(r.get("status") or ""))}</td><td class="n">{esc("" if r.get("duration_s") is None else f"{r["duration_s"]} s")}</td><td class="dim">{esc(str(r.get("at") or "")[:16].replace("T", " "))}</td></tr>'
        for w, e in sorted(eds, key=lambda x: x[1]["edition"], reverse=True) for r in e["rows"])
    body = f"""{strip}
<div class="tiles" id="costs-tiles">{tiles}</div>
<p>Every figure here is OpenRouter&rsquo;s own, asked per image after the generation (<code>GET /api/v1/generation</code>), never an estimate; the ledgers the pipeline writes beside the images are the record, and this page only adds them up. The data is <a href="costs.json">costs.json</a>. Not counted: the desks&rsquo; own runs (their models and tokens are in their sessions, not in any vault) and this site&rsquo;s sessions. Kept by <b>@{esc(ROLE)}</b>, a role of the morning routine that writes nothing of its own and spends nothing.</p>
<h2 id="wires">By wire</h2>
<table class="costs"><thead><tr><th>Wire</th><th class="n">Editions</th><th class="n">Images</th><th class="n">Failed</th><th class="n">Cost</th><th></th></tr></thead><tbody>{wires_rows}</tbody>
<tfoot><tr><td>All</td><td class="n">{sum(len(w["editions"]) for w in data["wires"])}</td><td class="n">{t["images"]}</td><td class="n">{t["failed"]}</td><td class="n">{esc(usd(t["cost_usd"]))}</td><td></td></tr></tfoot></table>
<h2 id="editions">By edition</h2>
<p>Hero + cards per edition; a run stops at its cap (forty images or two dollars, in the routine) and says so.</p>
<table class="costs"><thead><tr><th>Wire</th><th>Edition</th><th class="n">Hero + cards</th><th class="n">Failed</th><th class="n">Cost</th><th class="n">Per card</th><th></th><th>Stopped</th></tr></thead><tbody>{ed_rows}</tbody></table>
<h2 id="months">By month</h2>
<table class="costs"><thead><tr><th>Month</th><th class="n">Images</th><th class="n">Cost</th><th></th></tr></thead><tbody>{month_rows}</tbody></table>
<h2 id="models">By model</h2>
<p>The model that answered, as the tool returned it, with the mean cost and time per image. The bake-off&rsquo;s table of 10 October said 0.039 for a card on Nano Banana 2.1 and 0.176 for a hero on GPT-5.4 Image 2; the first live run (14 October) found Nano Banana rate-limited upstream and Gemini 3.1 Flash Image misspelling headlines, so the cards go to Gemini 3 Pro Image.</p>
<table class="costs"><thead><tr><th>Model</th><th class="n">Images</th><th class="n">Cost</th><th class="n">Per image</th><th class="n">Per image</th></tr></thead><tbody>{model_rows}</tbody></table>
<h2 id="images">Every image</h2>
<details><summary>{t["images"] + t["failed"]} rows: wire, edition, story, kind, model, cost, seconds, when</summary>
<table class="costs small"><thead><tr><th>Wire</th><th>Edition</th><th>Story</th><th>Kind</th><th>Model</th><th class="n">Cost</th><th class="n">Time</th><th>When (UTC)</th></tr></thead><tbody>{image_rows}</tbody></table></details>
<h2 id="how">How this is kept</h2>
<p>The pipeline (<code>admin/build/infographics.py</code>) writes a ledger per edition (<code>wire-infographics/v1</code>: per image the key, the kind, the model asked for and the one that answered, the generation id, the seconds, OpenRouter&rsquo;s cost, the prompt&rsquo;s hash and file, the status or the error) and a cumulative one per wire (<code>wire-infographics-total/v1</code>, by month and edition, with the key&rsquo;s budget as OpenRouter last reported it: the limit, what is spent, what is left; never the key). This page is rebuilt at every release by <code>admin/build/accountant.py</code> from those files alone. The owner caps a run at forty images and two dollars; the routine runs it after the desks publish, with the key in its environment and nowhere else.</p>
"""
    agent = (f"What the wires' pictures cost, from the ledgers admin/build/infographics.py writes: {t['images']} images for {usd(t['cost_usd'])} across {len(data['wires'])} wires; "
             f"a hero about {usd(pw['hero_usd'])}, a card about {usd(pw['card_usd'])}, an edition about {usd(pw['edition_usd'])}. The data is wire/costs.json (wire-costs/v1). Kept by @{ROLE}.")
    head = '<link rel="stylesheet" href="wire.css">\n<style>.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:.6rem;margin:0 0 1rem}.tile{padding:.7rem .8rem;border:1px solid var(--line);border-radius:10px;background:var(--panel)}.tile b{display:block;font:700 1.5rem/1.2 var(--serif);color:var(--fg)}.tile span{font-size:.78rem;color:var(--dim)}table.costs{width:100%;border-collapse:collapse;font-size:.88rem;margin:0 0 1.2rem}table.costs th,table.costs td{padding:.35rem .5rem;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}table.costs .n{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}table.costs tfoot td{font-weight:700}table.costs.small{font-size:.78rem}.bar{display:inline-block;width:100%;min-width:60px;height:.6rem;background:var(--panel2);border-radius:3px;overflow:hidden}.bar i{display:block;height:100%;background:var(--accent)}</style>\n'
    return newsroom_page("wire/costs.html", "What the wires cost",
                         "What the wires' pictures cost, to the cent: every image, edition, wire and month from the pipeline's ledgers, with OpenRouter's own figures and the key's budget.",
                         body, eyebrow=eyebrow, crumbs=(("The Industry Wire", "wire/index.html"),),
                         lead="Every picture the wires made and what it cost, by wire, edition, month and model, from OpenRouter's own figures; and what a hero, a card and an edition cost.",
                         agent=agent, head=head, wide=True)


def pages(cfgs, strip, newsroom_page, eyebrow):
    """(rel, text) pairs for wire.py to write: the JSON and the page."""
    data = gather(cfgs)
    return (("wire/costs.json", json.dumps(data, indent=1, ensure_ascii=False) + "\n"), ("wire/costs.html", costs_html(data, cfgs, strip, newsroom_page, eyebrow)))


if __name__ == "__main__":
    import wire as W
    from page import newsroom_page, write
    for rel, text in pages(W.CFGS, W.wires_strip(None, up="../"), newsroom_page, W.EYEBROW):
        print(rel, "written" if write(rel, text) else "unchanged")
