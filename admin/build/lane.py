#!/usr/bin/env python3
"""The newsroom's end of the feedback loop: read a reader's lane with its read key and print the notes.

    NEWSROOM_LANE_KEY=sgit_public_read_<hex>:<id> python3 admin/build/lane.py          # clone or pull, then the digest
    python3 admin/build/lane.py --dir /path/to/a/clone                                   # a clone made already: no network
    python3 admin/build/lane.py --json                                                   # the notes as JSON, newest first

The lane is a vault the reader made from the vault pane (assets/vault-pane/vault-pane.js, "Send to the newsroom"):
one file per note under notes/, each a tap at a piece (done, read later, follow up, not for me, more like this,
liked, wrong, fix this, idea) or a message written to the newsroom, the words they added, the phrase they had selected, the page, the article number, the persona and the
device. The reader holds the write key in their master vault and hands the newsroom the read key, so this script can
only read. The key comes from the environment (NEWSROOM_LANE_KEY) or from stdin with --key -, never from a file in
this repository, and it is never printed. The clone lives under the system temp directory by vault id unless --dir
says otherwise; a second run pulls. Design: admin/notes/2026-10-12__the-feedback-loop.md.

A note sent from the Pen with a key (assets/pen/identity.js, card 090) carries `signed: {signer, at, sig}`. Each one is
checked here against pki.sgit.ai's public register: the signature against the signer's signing key in its record, and
the signer against a pinned root, Dinis Cruz's master key: the root itself, or a key the root operates, in date, that
links back ("operates" and "operated-by", the register's two-way rule). The digest marks each note signed and checked,
signed and not vouched for, or signed and failing; --no-register skips the check.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import base64
import urllib.request
from datetime import date
from collections import OrderedDict
from pathlib import Path

KINDS = {"done": "Done", "read-later": "Read later", "follow-up": "Follow up", "not-for-me": "Not for me",
         "more-like-this": "More like this", "liked": "Liked", "wrong": "Wrong", "fix": "Fix this", "idea": "Idea",
         "note": "Message"}
# The register and the pinned root; the two environment variables exist for admin/build/test_pen.mjs, which checks
# signatures against a register and a root of its own and never reaches the live site.
REGISTER = os.environ.get("NEWSROOM_PKI_REGISTER", "https://pki.sgit.ai/directory/index.json")
ROOT = os.environ.get("NEWSROOM_PKI_ROOT", "sha256:db7f79fdd87e030a")   # Dinis Cruz's master key (assets/pen/identity.js pins the same)
NOTE_KIND = "newsroom.sgit.ai/note/v1"
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


def canon(v):
    """The register's canonical JSON (keys.js canon, jq -cS): keys sorted, compact, non-ASCII as itself."""
    return json.dumps(v, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def payload_of(note, signer):
    """What a Pen signature covers, field for field as assets/pen/identity.js payloadOf builds it."""
    return {"v": 1, "kind": NOTE_KIND, "id": note.get("id"), "at": note.get("at"), "note_kind": note.get("kind") or "note",
            "path": note.get("path") or "", "n": note.get("n"), "quote": note.get("quote") or "", "text": note.get("text") or "", "signer": signer}


def read_register(url=REGISTER):
    with urllib.request.urlopen(url, timeout=30) as r:
        return {rec["fp"]: rec for rec in json.load(r).get("records", []) if rec.get("ok") and not rec.get("fixture") and not rec.get("revoked")}


def _links(rec):
    return [s["body"] for s in rec.get("statements", []) if s.get("type") == "link"]


def vouched(records, signer, today=None):
    """(ok, words): the signer is the root, or the root links to it with "operates" in date and it links back."""
    today = today or date.today().isoformat()
    if signer == ROOT:
        return True, "the root key itself"
    root, rec = records.get(ROOT), records.get(signer)
    if not rec:
        return False, "not in the register"
    ops = [l for l in _links(root or {}) if l.get("to") == signer and l.get("method") == "operates"]
    back = any(l.get("to") == ROOT and l.get("method") == "operated-by" for l in _links(rec))
    live = [l for l in ops if (l.get("until") or "9999-12-31") >= today]
    if live and back:
        return True, f"operated by the root until {max(l.get('until') or '' for l in live) or 'no end date'}"
    if ops and back:
        return False, "the root's link to it has ended"
    return False, "the root has not linked to it" if back else "it does not name the root as its operator"


def check_signatures(notes, records):
    """Mark each signed note in place: note['_signed'] = 'checked: <name>, <why>' or the reason it fails."""
    try:
        from cryptography.hazmat.primitives import hashes, serialization
        from cryptography.hazmat.primitives.asymmetric import ec, utils
        from cryptography.exceptions import InvalidSignature
    except ImportError:
        for n in notes:
            if n.get("signed"):
                n["_signed"] = "signed; not checked (python cryptography is not installed)"
        return
    for n in notes:
        s = n.get("signed")
        if not isinstance(s, dict):
            continue
        rec = records.get(s.get("signer"))
        bundle = (next((st["body"] for st in rec["statements"] if st.get("type") == "identity"), {}) if rec else {}).get("bundle") or {}
        if not bundle.get("sign"):
            n["_signed"] = f"signed by {s.get('signer')}: NOT in the register, so not checked"
            continue
        try:
            raw = base64.b64decode(s.get("sig", ""))
            der = utils.encode_dss_signature(int.from_bytes(raw[:32], "big"), int.from_bytes(raw[32:], "big"))
            key = serialization.load_pem_public_key(bundle["sign"].encode())
            key.verify(der, (canon(payload_of(n, s["signer"])) + "\n").encode(), ec.ECDSA(hashes.SHA256()))
        except (InvalidSignature, ValueError, KeyError, TypeError):
            n["_signed"] = f"signed by {rec.get('name') or s.get('signer')}: the SIGNATURE FAILS (changed after it was signed, or not theirs)"
            continue
        ok, why = vouched(records, s["signer"])
        n["_signed"] = f"signed and checked: {rec.get('name') or s['signer']}, {why}" if ok else f"signed by {rec.get('name') or s['signer']}, a valid signature, but not vouched for: {why}"


def digest(notes, host="https://newsroom.sgit.ai"):
    """The messages first (every note with words, newest first), then the notes grouped by page, each on one line;
    a wire story is named by its id and its headline."""
    if not notes:
        return "No notes in the lane yet.\n"
    when = lambda n: str(n.get("at", ""))[:16].replace("T", " ")
    pages = OrderedDict()
    for n in notes:
        pages.setdefault(n.get("path", "?"), []).append(n)
    said = [n for n in notes if n.get("text")]
    out = [f"{len(notes)} note(s) in the lane, {len(pages)} page(s), {len(said)} with words; newest first.\n"]

    def page_title(path):
        ns = pages.get(path, [])
        own = next((n for n in ns if not n.get("story") and n.get("title")), None)
        head = own["title"] if own else ("The Industry Wire" if path.startswith("/wire/") else path)
        num = next((n.get("n") for n in ns if n.get("n")), None)
        return f"No. {num} · {head}" if num else head

    if said:
        out.append(f"## Messages ({len(said)})\n")
        for n in said:
            where = f"story {n['story']}: {n.get('title') or ''} on " if n.get("story") else ""
            out.append(f"   - {when(n)} · {KINDS.get(n.get('kind'), n.get('kind', '?'))} · {where}{page_title(n.get('path', '?'))}, {host}{n.get('path', '')}")
            if n.get("quote"):
                q = n["quote"]
                out.append(f'     “{q if len(q) <= 240 else q[:240] + "…"}”')
            out.append(f"     {n['text']}")
            if n.get("_signed"):
                out.append(f"     [{n['_signed']}]")
        out.append("")
    for path, ns in pages.items():
        out.append(f"## {page_title(path)}\n   {host}{path}\n")
        for n in ns:
            line = f"   - {KINDS.get(n.get('kind'), n.get('kind', '?'))}"
            if n.get("story"):
                line += f" · story {n['story']}" + (f": {n['title']}" if n.get("title") else "")
            line += f" · {when(n)} · {n.get('persona') or 'me'}"
            if n.get("device"):
                line += f" · {n['device']}"
            if n.get("quote"):
                q = n["quote"]
                line += f'\n     “{q if len(q) <= 240 else q[:240] + "…"}”'
            if n.get("text"):
                line += f"\n     {n['text']}"
            if n.get("_signed"):
                line += f"\n     [{n['_signed']}]"
            out.append(line)
        out.append("")
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--dir", help="the clone's directory (made if missing); default: <tmp>/newsroom-lanes/<vault id>")
    ap.add_argument("--key", help="the read key, or - to read it from stdin; default: NEWSROOM_LANE_KEY in the environment")
    ap.add_argument("--json", action="store_true", help="print the notes as JSON instead of the digest")
    ap.add_argument("--no-fetch", action="store_true", help="read the clone as it is, no clone or pull")
    ap.add_argument("--no-register", action="store_true", help="do not read pki.sgit.ai's register to check signed notes")
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
    if any(n.get("signed") for n in notes) and not args.no_register:
        try:
            check_signatures(notes, read_register())
        except OSError as e:
            for n in notes:
                if n.get("signed"):
                    n["_signed"] = f"signed; the register could not be read ({e})"
    if args.json:
        print(json.dumps(notes, indent=1, ensure_ascii=False))
    else:
        print(f"lane {vault_id or clone.name}: {status}, {clone}\n")
        print(digest(notes), end="")


if __name__ == "__main__":
    main()
