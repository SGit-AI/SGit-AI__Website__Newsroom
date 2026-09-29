#!/usr/bin/env python3
"""world-news-day/ — push the two vaults to SG/Send.

    python3 world-news-day/build/publish_vaults.py --token <sg-send-token>

NOT part of the ordinary build. It is the only step in this section that needs a credential
and the only one that talks to the vault server, so it is run deliberately, by hand, and
never from CI.

What it does:

  1. materialises the corpus vault from vault.zip (the same bytes the site serves),
  2. materialises the outreach vault from world-news-day/outreach/,
  3. `sgit init --existing` / `commit` / `push` for each,
  4. derives each vault's PUBLIC READ KEY and writes it into the section's data files,
  5. leaves the VAULT KEYS where sgit put them, in the working copy's .sg_vault/ outside
     this repository, and never reads, prints, copies or transmits them.

The distinction in step 4 and 5 is the whole safety model, so it is worth stating plainly:

  · a READ KEY (`sgit_public_read_…`) is derived one-way from the vault key, grants read and
    only read, and is meant to be published. It goes in data/*.json and onto the page.
  · a VAULT KEY (`sgit_private_vault_…:<id>`) is write access to everything in the vault. This
    script never prints one, never copies one, and never puts one in a variable it logs: the
    key stays in the working copy sgit created, outside this repository, for a person to read
    directly. If one ever reaches the tree, `admin/build/validate.js` fails the build by name
    — that tripwire was widened at v0.4.4 because it had been written against a key format
    sgit does not issue.

Re-running is safe: an existing working copy is reused, and an unchanged vault produces an
empty commit that sgit skips.
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

SEC = Path(__file__).resolve().parents[1]
DATA = SEC / "data"
REMOTE = "https://dev.send.sgraph.ai"
WORK = Path(os.environ.get("WND_VAULT_WORK", "/tmp/wnd-vaults"))


def run(args, cwd, token=None):
    cmd = ["sgit"] + (["--token", token] if token else []) + args
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=900)
    if r.returncode != 0:
        print(r.stdout[-3000:])
        print(r.stderr[-3000:], file=sys.stderr)
        raise SystemExit(f"sgit {' '.join(args)} failed in {cwd}")
    return r.stdout


def read_key_for(vault_key):
    from sgit_ai.crypto.Vault__Crypto import Vault__Crypto
    c = Vault__Crypto()
    passphrase, vault_id = c.parse_vault_key(vault_key)
    return c.format_read_key(c.derive_read_key(passphrase, vault_id).hex(), public=True), vault_id


def read_key_only(d):
    """Derive the vault's PUBLIC READ KEY from its working copy, and return only that.

    The vault key is needed to derive it and is used for exactly that, in memory, inside this
    function. It is not returned, not logged, not stored. What comes back is the one-way
    derivative that is safe to publish."""
    secret = None
    for rel in ("local/vault_key", "vault_key", "local/key", "key"):
        f = d / ".sg_vault" / rel
        if f.exists():
            secret = f.read_text().strip()
            break
    if secret is None:
        for rel in ("local/config.json", "config.json"):
            cfg = d / ".sg_vault" / rel
            if cfg.exists():
                c = json.loads(cfg.read_text())
                secret = c.get("vault_key") or c.get("key")
                if secret:
                    break
    if not secret:
        raise SystemExit(f"cannot find the vault key under {d}/.sg_vault — look yourself; "
                         f"this script will not go hunting for a credential")
    return read_key_for(secret)


def materialise(dest, fill):
    """Put the current contents in place WITHOUT destroying .sg_vault.

    The first version only filled a directory that had no vault in it yet, so a re-run pushed
    the same bytes for ever: the corpus vault was created before the fractal layer existed and
    silently stayed that way through two releases, while its page advertised files it did not
    contain. Caught by cloning the published vault with the published read key and running the
    gate inside it — which is the check the vault's own README tells a reader to run."""
    keep = dest / ".sg_vault"
    dest.mkdir(parents=True, exist_ok=True)
    for item in dest.iterdir():
        if item == keep:
            continue
        shutil.rmtree(item) if item.is_dir() else item.unlink()
    fill(dest)


def fill_corpus(dest):
    with zipfile.ZipFile(SEC / "vault.zip") as z:
        z.extractall(dest)


def fill_outreach(dest):
    for item in (SEC / "outreach").iterdir():
        tgt = dest / item.name
        shutil.copytree(item, tgt) if item.is_dir() else shutil.copy2(item, tgt)


def publish(name, dest, token, message):
    fresh = not (dest / ".sg_vault").exists()
    if fresh:
        # No per-vault `remote add`: the remote lives in the user's sgit config, and adding it
        # here creates .sg_vault before init runs, which then refuses with "init is only
        # available outside a vault".
        p = subprocess.run(["sgit", "--token", token, "init", "--existing", "."],
                           cwd=dest, capture_output=True, text=True, input="y\n" * 5, timeout=900)
        if p.returncode != 0:
            print(p.stdout[-3000:]); print(p.stderr[-3000:], file=sys.stderr)
            raise SystemExit(f"sgit init failed for {name}")
    run(["commit", message], dest, token)
    out = run(["push"], dest, token)
    read_key, vault_id = read_key_only(dest)
    commit = None
    for line in out.splitlines():
        if "obj-cas-imm-" in line:
            commit = line.strip().split()[-1]
    return {"vault_id": vault_id, "read_key": read_key, "commit": commit,
            "remote": REMOTE, "working_copy": str(dest)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--token", required=True)
    a = ap.parse_args()
    WORK.mkdir(parents=True, exist_ok=True)

    corpus_dir, outreach_dir = WORK / "wnd-corpus", WORK / "wnd-outreach"
    materialise(corpus_dir, fill_corpus)
    materialise(outreach_dir, fill_outreach)

    v = json.loads((DATA / "vault.json").read_text(encoding="utf-8"))
    c = publish("corpus", corpus_dir, a.token,
                f'world news day 2026: the corpus, {v["count"]} files, snapshot {v["snapshot"]}')
    o = publish("outreach", outreach_dir, a.token,
                "world news day 2026: the outreach vault at handover — nothing sent")

    v.update({"pushed": True, "vault_id": c["vault_id"], "read_key": c["read_key"],
              "commit": c["commit"], "remote": c["remote"],
              "why_not_pushed": None,
              "read_key_note": "A read key is derived one-way from the vault key and grants "
                               "read and only read. The vault key is write access to "
                               "everything and is published nowhere, in any file, ever."})
    (DATA / "vault.json").write_text(json.dumps(v, indent=2, ensure_ascii=False) + "\n",
                                     encoding="utf-8")

    st = json.loads((SEC / "outreach" / "state.json").read_text(encoding="utf-8"))
    (DATA / "outreach-vault.json").write_text(json.dumps({
        "id": "wnd-outreach-vault",
        "what": "The working vault handed to the agent at riskmandate.ai: who is being "
                "contacted, through which published route, what was said and what came back. "
                "Separate from the corpus vault on purpose — that one is a finished record of "
                "what somebody else published, this one is an append-only record of what we "
                "do about it.",
        "pushed": True,
        "vault_id": o["vault_id"], "read_key": o["read_key"], "commit": o["commit"],
        "remote": o["remote"],
        "contents": "README.md, protocol.md, brief.md, targets/ (one per organisation), "
                    "actions/ (append-only, with its JSON schema), drafts/, state.json, "
                    "evidence.md",
        "targets": st["targets"], "by_state": st["by_state"],
        "actions_recorded": st["actions_recorded"],
        "the_read_key_is_read_only": "Published deliberately. Write access is a separate key "
                                     "that is not in this repository and never will be.",
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print("\n" + "=" * 72)
    print("PUSHED. The two PUBLIC READ keys are now in data/vault.json and")
    print("data/outreach-vault.json, and will be published on the pages.")
    print()
    print("  corpus    " + c["vault_id"] + "   read: " + c["read_key"])
    print("  outreach  " + o["vault_id"] + "   read: " + o["read_key"])
    print()
    print("The two VAULT KEYS — write access — were NOT read, printed or copied by this")
    print("script. sgit wrote each one into its own working copy, outside this repository:")
    print()
    print("  " + c["working_copy"] + "/.sg_vault/")
    print("  " + o["working_copy"] + "/.sg_vault/")
    print()
    print("Read them there yourself and put them somewhere safe. They are the only way to")
    print("write to these vaults, and there is no password reset.")
    print("=" * 72)


if __name__ == "__main__":
    main()
