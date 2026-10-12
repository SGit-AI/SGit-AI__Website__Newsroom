#!/usr/bin/env python3
"""The newsroom's end of the feedback loop: read a reader's lane with its read key and print the notes.

    NEWSROOM_LANE_KEY=sgit_public_read_<hex>:<id> python3 admin/build/lane.py          # clone or pull, then the digest
    python3 admin/build/lane.py --dir /path/to/a/clone                                   # a clone made already: no network
    python3 admin/build/lane.py --json                                                   # the notes as JSON, newest first

The lane is a vault the reader made from the vault pane (assets/vault-pane/vault-pane.js, "Send to the newsroom"):
one file per note under notes/, each a tap at a piece (read later, not for me, more like this, liked, wrong, fix
this, idea), the words they added, the phrase they had selected, the page, the article number, the persona and the
device. The reader holds the write key in their master vault and hands the newsroom the read key, so this script can
only read. The key comes from the environment (NEWSROOM_LANE_KEY) or from stdin with --key -, never from a file in
this repository, and it is never printed. The clone lives under the system temp directory by vault id unless --dir
says otherwise; a second run pulls. Design: admin/notes/2026-10-12__the-feedback-loop.md.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from collections import OrderedDict
from pathlib import Path

KINDS = {"read-later": "Read later", "not-for-me": "Not for me", "more-like-this": "More like this", "liked": "Liked",
         "wrong": "Wrong", "fix": "Fix this", "idea": "Idea", "note": "Note"}
KEY_RE = re.compile(r"^sgit_public_read_[0-9a-f]{64}:([a-z0-9]{4,24})$")


def sgit(args, cwd=None, stdin=None):
    cmd = ["sgit"] + args
    base = os.environ.get("SGIT_DEFAULT_BASE_URL")
    if base and args and args[0] in ("clone",):
        cmd += ["--base-url", base]
    return subprocess.run(cmd, cwd=cwd, input=stdin, capture_output=True, text=True, timeout=600)


def fetch(key: str, into: Path):
    """Clone the lane into `into` with the read key on stdin, or pull if it is there already. Returns a short status."""
    if (into / ".sg_vault").exists():
        r = sgit(["pull"], cwd=into)
        if r.returncode != 0:
            raise SystemExit("sgit pull failed: " + (r.stderr or r.stdout).strip().splitlines()[-1])
        return "pulled"
    into.parent.mkdir(parents=True, exist_ok=True)
    r = sgit(["clone", "-", str(into)], stdin=key + "\n")
    if r.returncode != 0:
        raise SystemExit("sgit clone failed: " + (r.stderr or r.stdout).strip().splitlines()[-1])
    return "cloned"


def load(clone: Path):
    notes = []
    for f in sorted((clone / "notes").glob("*.json")) if (clone / "notes").is_dir() else []:
        try:
            n = json.loads(f.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if isinstance(n, dict) and n.get("id") and n.get("at"):
            notes.append(n)
    notes.sort(key=lambda n: str(n.get("at", "")), reverse=True)
    return notes


def digest(notes, host="https://newsroom.sgit.ai"):
    """The notes grouped by page, newest page first, each note on one line; wire stories named by id."""
    if not notes:
        return "No notes in the lane yet.\n"
    pages = OrderedDict()
    for n in notes:
        pages.setdefault(n.get("path", "?"), []).append(n)
    out = [f"{len(notes)} note(s) in the lane, {len(pages)} page(s), newest first.\n"]
    for path, ns in pages.items():
        first = ns[0]
        head = (first.get("title") or path)
        if first.get("n"):
            head = f"No. {first['n']} · {head}"
        out.append(f"## {head}\n   {host}{path}\n")
        for n in ns:
            line = f"   - {KINDS.get(n.get('kind'), n.get('kind', '?'))}"
            if n.get("story"):
                line += f" · story {n['story']}"
            line += f" · {str(n.get('at', ''))[:16].replace('T', ' ')} · {n.get('persona') or 'me'}"
            if n.get("device"):
                line += f" · {n['device']}"
            if n.get("quote"):
                q = n["quote"]
                line += f'\n     “{q if len(q) <= 240 else q[:240] + "…"}”'
            if n.get("text"):
                line += f"\n     {n['text']}"
            out.append(line)
        out.append("")
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--dir", help="the clone's directory (made if missing); default: <tmp>/newsroom-lanes/<vault id>")
    ap.add_argument("--key", help="the read key, or - to read it from stdin; default: NEWSROOM_LANE_KEY in the environment")
    ap.add_argument("--json", action="store_true", help="print the notes as JSON instead of the digest")
    ap.add_argument("--no-fetch", action="store_true", help="read the clone as it is, no clone or pull")
    args = ap.parse_args()
    key = ""
    if not args.no_fetch:
        key = (sys.stdin.readline().strip() if args.key == "-" else (args.key or os.environ.get("NEWSROOM_LANE_KEY", ""))).strip()
        if not key and not (args.dir and (Path(args.dir) / ".sg_vault").exists()):
            raise SystemExit("no read key: set NEWSROOM_LANE_KEY, or pass --key -, or name a clone with --dir")
        if key and not KEY_RE.match(key):
            raise SystemExit("that is not a public read key (sgit_public_read_<64 hex>:<vault id>); a vault key would give write access and is not wanted here")
    vault_id = KEY_RE.match(key).group(1) if key else None
    clone = Path(args.dir) if args.dir else Path(tempfile.gettempdir()) / "newsroom-lanes" / (vault_id or "lane")
    status = "read as is"
    if not args.no_fetch:
        if key:
            status = fetch(key, clone)
        else:
            r = sgit(["pull"], cwd=clone)
            status = "pulled" if r.returncode == 0 else "pull failed, read as is"
    notes = load(clone)
    if args.json:
        print(json.dumps(notes, indent=1, ensure_ascii=False))
    else:
        print(f"lane {vault_id or clone.name}: {status}, {clone}\n")
        print(digest(notes), end="")


if __name__ == "__main__":
    main()
