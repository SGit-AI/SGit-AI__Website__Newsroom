#!/usr/bin/env python3
"""The run ledger: every scheduled run of the wires, what it cost and what it did, kept in admin/build/wire-runs.json.

    python3 admin/build/runs_ledger.py add <row.json>     add (or replace) runs; the file is one row or a list of rows
    python3 admin/build/runs_ledger.py check              validate the ledger and print its totals

A row is assembled by the accountant (@newsroom.accountant) from two records the platform keeps for every session: the
session's usage (get_session: cost_usd and the token counts) and its final result event (list_events with kinds
["result"]: modelUsage per model, num_turns, duration_ms, subagent_stats, permission_denials). The owner asked on
16 October 2026 that "every run that happens should be capturing the cost, the tokens, and everything that happens with it".

    {"task": "industry" | "aws" | "owasp" | "portugal" | "newsroom" | "dinis" | "ruv" | "accountant" | ...,
     "trigger": "trig_...", "fired_at": ISO, "finished_at": ISO, "duration_s": n,
     "models": {"claude-sonnet-5-5": {"cost_usd", "input", "output", "cache_read", "cache_write", "thinking"}, ...},
     "cost_usd": n, "turns": n, "subagents": n,
     "refused": n, "refused_kinds": ["pip install", "sgit clone", ...],
     "outcome": "published" | "nothing new" | "blocked" | "failed", "release": "2026-10-16.1" | null,
     "added": n | null, "updated": n | null}

What is never kept: a session's free text or a refused command's arguments (they can carry a vault key), and the
session id itself (a short hash of it is kept, to replace a row rather than add it twice). The ledger is public, as
the costs page is: the owner's spend, to the cent, beside what it bought.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LEDGER = ROOT / "admin/build/wire-runs.json"
TASKS = re.compile(r"^[a-z][a-z0-9-]{1,30}$")
ISO = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?Z$")
OUTCOMES = {"published", "nothing new", "blocked", "failed", "running"}
KINDS = {"pip install", "sgit clone", "sgit push", "sgit commit", "git push", "web fetch", "other"}
KEYISH = re.compile(r"sgit_|sk-or-|[0-9a-z]{20,}:[0-9a-z]{6,}|ghp_|github_pat_")
USAGE = ("cost_usd", "input", "output", "cache_read", "cache_write", "thinking")


def load():
    if LEDGER.exists():
        return json.loads(LEDGER.read_text(encoding="utf-8"))
    return {"schema": "wire-runs/v1", "kept_by": "newsroom.accountant", "runs": [], "sessions": []}


def clean(row):
    """A row as the ledger keeps it, or a ValueError saying why not."""
    if not TASKS.match(str(row.get("task", ""))):
        raise ValueError(f"task: {row.get('task')!r}")
    for k in ("fired_at", "finished_at"):
        if row.get(k) is not None and not ISO.match(str(row[k])):
            raise ValueError(f"{k}: {row.get(k)!r}")
    if row.get("outcome") not in OUTCOMES:
        raise ValueError(f"outcome: {row.get('outcome')!r}")
    models = {}
    for m, u in (row.get("models") or {}).items():
        if not re.match(r"^claude-[a-z0-9-]+$", m):
            raise ValueError(f"model: {m!r}")
        models[m] = {k: (round(float(u.get(k) or 0), 6) if k == "cost_usd" else int(u.get(k) or 0)) for k in USAGE}
    out = {
        "id": row.get("id") or hashlib.sha256(str(row.get("session") or f"{row['task']}|{row.get('fired_at')}").encode()).hexdigest()[:12],
        "task": row["task"], "trigger": row.get("trigger") if re.match(r"^trig_[A-Za-z0-9]+$", str(row.get("trigger") or "")) else None,
        "fired_at": row.get("fired_at"), "finished_at": row.get("finished_at"),
        "duration_s": round(float(row.get("duration_s") or 0), 1),
        "models": models,
        "cost_usd": round(float(row.get("cost_usd") if row.get("cost_usd") is not None else sum(u["cost_usd"] for u in models.values())), 6),
        "turns": int(row.get("turns") or 0), "subagents": int(row.get("subagents") or 0),
        "refused": int(row.get("refused") or 0), "refused_kinds": sorted({k for k in (row.get("refused_kinds") or []) if k in KINDS}),
        "outcome": row["outcome"],
        "release": row.get("release") if re.match(r"^\d{4}-\d{2}-\d{2}\.\d+$", str(row.get("release") or "")) else None,
        "added": row.get("added") if isinstance(row.get("added"), int) else None,
        "updated": row.get("updated") if isinstance(row.get("updated"), int) else None,
        "note": str(row.get("note") or "")[:200] or None,
    }
    if KEYISH.search(json.dumps(out)):
        raise ValueError("the row carries something shaped like a key; it is not kept")
    return out


def add(rows):
    led = load()
    by_id = {r["id"]: r for r in led["runs"]}
    for row in rows if isinstance(rows, list) else [rows]:
        r = clean(row)
        by_id[r["id"]] = r
    led["runs"] = sorted(by_id.values(), key=lambda r: (str(r.get("fired_at") or ""), r["task"]))
    LEDGER.write_text(json.dumps(led, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return led


def main(argv):
    if len(argv) >= 3 and argv[1] == "add":
        led = add(json.loads(Path(argv[2]).read_text(encoding="utf-8")))
    elif len(argv) == 2 and argv[1] == "check":
        led = load()
        for r in led["runs"]:
            clean(r)
    else:
        print(__doc__.split("\n\n")[1]); return 2
    print(f"{len(led['runs'])} runs, ${sum(r['cost_usd'] for r in led['runs']):.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
