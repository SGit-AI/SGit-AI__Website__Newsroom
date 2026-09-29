#!/usr/bin/env python3
"""world-news-day/ — audit and describe the published vaults, the way sgit.ai does.

    python3 world-news-day/build/vault_audit.py          (network: clones with the READ keys)

The method is not ours. sgit.ai publishes thirty-seven vaults and writes down how, at
https://sgit.ai/demos/vaults/publishing.md — seven steps, two absolute rules, and a table of
the mistakes each rule came out of. This is that method applied to our two, so that a reader
who knows one estate's vault pages can read the other's without learning anything new.

The two rules everything else serves, in their words:

    Read keys yes, vault keys never.   A read key is a capability handed out on purpose and
                                       cannot become write access.
    Audit before the key, not after.   Revocation is not retroactive. Anyone who fetches the
                                       objects keeps them.

What this does, and every bit of it is done with the PUBLISHED read key and no token, because
that is the credential a reader has:

  1. classifies both credentials — a read key is 64 hex characters after the prefix, and
     anything else before the colon is a passphrase, which means write;
  2. clones each vault with its read key alone;
  3. derives the facts — files, plaintext size, commits, HEAD, top-level layout — rather than
     describing them from the repository, because the repository is not what was published;
  4. scans every text file in the clone for credential shapes, addresses and private keys,
     and records what it ruled out as well as what it found;
  5. runs the negative control: the same clone with an all-zeros read key must fail.

Writes data/vault-audit.json. The pages are built from it, so a page cannot claim an audit
that did not run.
"""
import gzip
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

SEC = Path(__file__).resolve().parents[1]
DATA = SEC / "data"
UI = "https://dev.vault.sgraph.ai/#"

# What a scan looks for. Ruling hits out is the work, so every pattern that fires is recorded
# with its verdict rather than silently dropped.
SCAN = [
    ("vault key (uuid form)", r"[A-Za-z0-9_-]{20,}:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"),
    ("sgit private vault key", r"sgit_private_vault_[A-Za-z0-9_-]{8,}\s*:\s*[A-Za-z0-9]{4,}"),
    ("sgit private read key", r"sgit_private_read_[0-9a-f]{16,}"),
    ("AWS access key id", r"\bAKIA[0-9A-Z]{16}\b"),
    ("OpenAI-shaped key", r"\bsk-[A-Za-z0-9]{20,}\b"),
    ("bearer token", r"\bBearer\s+[A-Za-z0-9._~+/-]{20,}"),
    ("private key block", r"-----BEGIN (?:RSA |EC |OPENSSH |PGP )?PRIVATE KEY-----"),
    ("email address", r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
]
TEXTY = {".md", ".json", ".txt", ".py", ".js", ".html", ".nt", ".sh", ".yml", ".yaml", ".csv"}


def classify(credential):
    """sgit.ai's step 1, reimplemented rather than imported so it can be read here.

    Two eras: by PREFIX for keys new enough to carry one, and by SHAPE for everything older.
    A read key is 64 hex characters; anything else before the colon is a passphrase, and a
    passphrase means write."""
    head, _, tail = credential.partition(":")
    if head.startswith("sgit_public_read_"):
        body = head[len("sgit_public_read_"):]
        ok = bool(re.fullmatch(r"[0-9a-f]{64}", body))
        return ("read-only, published on purpose" if ok else "malformed public read key"), ok
    if head.startswith("sgit_private_read_"):
        return "read-only, but declared PRIVATE — do not publish this spelling", False
    if head.startswith(("sgit_private_vault_", "sgit_vk1_")):
        return "WRITE credential — stop", False
    if re.fullmatch(r"[0-9a-f]{64}", head):
        return "read-only by shape (no prefix; older vault)", True
    return "not a recognised credential, or a passphrase — treat as WRITE", False


def run(args, cwd=None, timeout=900):
    return subprocess.run(["sgit"] + args, cwd=cwd, capture_output=True, text=True,
                          timeout=timeout)


def derive(read_key, vault_id, work):
    """Step 4: the facts, from the read key, read-only, no token, no repository."""
    dest = work / vault_id
    r = run(["clone", f"{read_key}:{vault_id}", str(dest)])
    if r.returncode != 0:
        return None, (r.stdout + r.stderr)[-2000:]
    files, total = [], 0
    for p in sorted(dest.rglob("*")):
        if p.is_file() and ".sg_vault" not in p.parts:
            files.append(p.relative_to(dest).as_posix())
            total += p.stat().st_size
    head = None
    for line in r.stdout.splitlines():
        if "HEAD:" in line:
            head = line.split("HEAD:")[1].strip()
    log = run(["history", "log", "--json"], cwd=dest)
    commits = None
    try:
        commits = len(json.loads(log.stdout))
    except Exception:
        m = re.findall(r"obj-cas-imm-[0-9a-f]+", log.stdout)
        commits = len(set(m)) or None
    top = sorted({f.split("/")[0] + ("/" if "/" in f else "") for f in files})
    return {
        "dest": dest, "files": files, "file_count": len(files), "bytes": total,
        "head": head, "commits": commits, "top_level": top,
        "has_page_json": "_page.json" in files,
        "has_readme": "README.md" in files,
    }, None


def _second_level(host):
    parts = host.lower().replace("www.", "").split(".")
    if len(parts) >= 3 and len(parts[-1]) == 2 and parts[-2] in {"co", "com", "org", "net", "gov", "ac"}:
        return parts[-3]
    return parts[-2] if len(parts) >= 2 else parts[0]


def verdict_for(kind, match):
    """Ruling a hit out is the work, and the verdict is published beside it.

    A scanner that reports twenty-five hits and no verdicts has moved the job to the reader.
    Every address in these vaults is an organisation's ROLE address, published on purpose
    under the rule in data/contact-rules.json — so the audit says which rule cleared it, and
    anything the rule does not clear is marked UNEXPLAINED and stops the publication."""
    if kind != "email address":
        return "UNEXPLAINED — a credential shape has no business in a published vault", False
    rules = json.loads((DATA / "contact-rules.json").read_text(encoding="utf-8"))
    local, _, dom = match.lower().partition("@")
    if local in set(rules["role_local_parts"]) or local == _second_level(dom):
        return ("published on purpose: an organisation's role address, cleared by the rule in "
                "data/contact-rules.json"), True
    return "UNEXPLAINED — not a role address; no personal address may be in these vaults", False


def scan(dest):
    """Step 3: open the vault with the credential a reader has, and read every text file."""
    findings, checked = [], 0
    for p in sorted(dest.rglob("*")):
        if not p.is_file() or ".sg_vault" in p.parts:
            continue
        if p.suffix.lower() not in TEXTY:
            continue
        checked += 1
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        for label, pat in SCAN:
            for m in re.finditer(pat, text):
                why, cleared = verdict_for(label, m.group(0))
                findings.append({"file": p.relative_to(dest).as_posix(), "kind": label,
                                 "match": m.group(0)[:60], "verdict": why,
                                 "cleared": cleared})
    return findings, checked


def negative_control(vault_id, work):
    """The check that proves the key is doing the work. A wrong key cannot even find the
    vault's index, because the index address is derived from the key."""
    zeros = "sgit_public_read_" + "0" * 64
    r = run(["clone", f"{zeros}:{vault_id}", str(work / f"negative-{vault_id}")], timeout=300)
    return {"attempted_with": "an all-zeros read key", "exit_code": r.returncode,
            "failed_as_required": r.returncode != 0,
            "message": (r.stderr or r.stdout).strip().splitlines()[-1][:200]
                       if (r.stderr or r.stdout).strip() else ""}


def main():
    vaults = [
        ("corpus", json.loads((DATA / "vault.json").read_text(encoding="utf-8")),
         "The twenty-one op-eds as frozen bytes, every derived dataset, the build code and "
         "the gate that checks them. Finished on the day it was made."),
        ("outreach", json.loads((DATA / "outreach-vault.json").read_text(encoding="utf-8")),
         "The working vault the agent at riskmandate.ai collaborates in: who is being "
         "contacted, through which published route, and what happened. Append-only."),
    ]
    out, work = [], Path(tempfile.mkdtemp(prefix="wnd-audit-"))
    try:
        for name, rec, what in vaults:
            key, vid = rec["read_key"], rec["vault_id"]
            verdict, publishable = classify(f"{key}:{vid}")
            entry = {"name": name, "vault_id": vid, "read_key": key, "what": what,
                     "credential": {"verdict": verdict, "publishable": publishable},
                     "open_in_ui": f"{UI}{key}%3A{vid}",
                     "clone_command": f"sgit clone {key}:{vid}"}
            if not publishable:
                entry["audit"] = {"ran": False,
                                  "why": "the credential did not classify as read-only"}
                out.append(entry)
                continue
            facts, err = derive(key, vid, work)
            if facts is None:
                entry["audit"] = {"ran": False, "why": f"clone failed: {err}"}
                out.append(entry)
                continue
            findings, checked = scan(facts["dest"])
            entry["derived"] = {k: v for k, v in facts.items() if k != "dest"}
            entry["audit"] = {
                "ran": True,
                "at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "method": "cloned with the published read key alone, no token, and every "
                          "text file read",
                "text_files_scanned": checked,
                "patterns": [p[0] for p in SCAN],
                "findings": findings,
                "hits": len(findings),
                "cleared": sum(1 for f in findings if f["cleared"]),
                "unexplained": sum(1 for f in findings if not f["cleared"]),
                "negative_control": negative_control(vid, work),
            }
            out.append(entry)
    finally:
        shutil.rmtree(work, ignore_errors=True)

    doc = {
        "id": "wnd-vault-audit", "version": "0.1.0",
        "method": "https://sgit.ai/demos/vaults/publishing.md",
        "method_note": "The method is sgit.ai's, reimplemented here rather than imported so "
                       "that it can be read beside the result. Two rules it exists to serve: "
                       "read keys yes and vault keys never; and audit BEFORE publishing the "
                       "key, because revocation is not retroactive.",
        "audited": out,
        "unexplained_total": sum(e.get("audit", {}).get("unexplained", 0) for e in out),
        "ruling_hits_out_is_the_work": "A scanner that reports hits and no verdicts has moved "
                                       "the job to the reader. Every hit here carries the rule "
                                       "that cleared it, or is marked UNEXPLAINED — and an "
                                       "unexplained finding is a reason not to publish, which "
                                       "the section gate enforces.",
        "what_a_clean_scan_means": "That nothing matching these patterns is in the current "
                                   "files of the published vault. It is not a statement about "
                                   "the vault's history, and it is not a promise that nothing "
                                   "sensitive is in a file that matches no pattern.",
    }
    (DATA / "vault-audit.json").write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n",
                                           encoding="utf-8")
    for e in out:
        a = e.get("audit", {})
        if a.get("ran"):
            print(f"  {e['name']:9} {e['vault_id']}  {e['derived']['file_count']} files, "
                  f"{e['derived']['bytes'] / 1048576:.2f} MB, {e['derived']['commits']} commits; "
                  f"{a['text_files_scanned']} text files scanned, {a['hits']} hits "
                  f"({a['cleared']} cleared, {a['unexplained']} unexplained); "
                  f"negative control {'passed' if a['negative_control']['failed_as_required'] else 'FAILED'}")
        else:
            print(f"  {e['name']:9} {e['vault_id']}  audit did not run: {a.get('why')}")
    return doc


if __name__ == "__main__":
    main()
