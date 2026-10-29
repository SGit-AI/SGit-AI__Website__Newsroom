#!/usr/bin/env python3
"""CI owns the version: the number of a release is chosen by the pipeline, never by whoever pushes.

    python3 admin/build/release_stamp.py --pending "one line on what this release does" [--by @newsroom.writer]
        the committer, before its build: version.txt becomes the pending version, and the release note and the
        versions row are written (or added to) under the pending version. Build, commit with a subject that
        carries no number ("@newsroom.writer: ..."), push to dev.

    python3 admin/build/release_stamp.py vX.Y.Z --since vA.B.C [--branch dev|main]
        CI's release job only, once it has picked vX.Y.Z from the tags: every pending version in the served
        tree becomes vX.Y.Z (contents and paths), version.txt says vX.Y.Z, a push that ran no build gets its
        release note and versions row from its commit messages, and the chrome, the engineering pages, the
        sitemap and llms-full are re-stamped. The gate (validate.js) runs next, in the job.

Why: a committer that writes the number has a window between reading the tags and landing its push, and
two agents releasing in the same minute turn that window into a collision (v0.13.103 and v0.13.111 were both
taken while another release was being built, on 27 October 2026). The pipeline is the one place that sees
pushes in order. The scheme is OSBot-Utils' (27 October 2023), as sharness.ai adopted it on 26 October 2026
(https://sharness.ai/articles/ci-owns-the-version.html) and the PHP newsroom's repositories on 27 October;
admin/notes/2026-10-27__ci-owns-the-version.md has the rules.

The pending version is a placeholder shaped like a version, so every generator and check that reads
version.txt works unchanged, and it sorts after every real release, so lists ordered by version put this
release first. It is never tagged and never deployed: the deploy publishes only the commit CI stamped.
"""
import argparse
import datetime
import html
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PENDING = "v999.0.0"
VERSION_FILE = ROOT / "admin/build/version.txt"
VERSIONS = ROOT / "admin/versions.html"
RELEASES = ROOT / "admin/engineering/releases"
# Not stamped: the history, CI's own files, and the build code, which names the pending version on purpose.
SKIP_DIRS = {".git", ".github", "node_modules", ".sg_vault"}
SKIP_PREFIXES = ("admin/build/",)
SEMVER = re.compile(r"^v\d+\.\d+\.\d+$")


def esc(s):
    return html.escape(s, quote=False)


def today():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")


def day_label(d):
    return datetime.date.fromisoformat(d).strftime("%-d %b %Y")


def note_path(v):
    return RELEASES / f"{v}.md"


def write_note(v, line, body, kind="patch"):
    p = note_path(v)
    if p.exists():
        p.write_text(p.read_text(encoding="utf-8").rstrip("\n") + "\n\n" + body.strip() + "\n", encoding="utf-8")
        return False
    p.write_text(f"---\nversion: {v}\ndate: {today()}\nkind: {kind}\nissues: []\n---\n\n# {v}\n\n{body.strip()}\n",
                 encoding="utf-8")
    return True


def add_row(v, line):
    """A row for v at the top of the versions table; a second release note on a pending row is appended to it."""
    t = VERSIONS.read_text(encoding="utf-8")
    m = re.search(rf'    <tr id="{re.escape(v)}">.*?</tr>\n', t, re.S)
    if m:
        row = m.group(0)
        new = row.replace(f' In <a href="../engineering/releases/{v}.html">the release</a>.</td>',
                          f' {esc(line)} In <a href="../engineering/releases/{v}.html">the release</a>.</td>', 1)
        if new != row:
            VERSIONS.write_text(t.replace(row, new, 1), encoding="utf-8")
        return
    row = (f'    <tr id="{v}">\n      <td class="vnum">{v}</td>\n      <td>{day_label(today())}</td>\n'
           f'      <td>{esc(line)} In <a href="../engineering/releases/{v}.html">the release</a>.</td>\n    </tr>\n')
    i = t.index('    <tr id="v')
    VERSIONS.write_text(t[:i] + row + t[i:], encoding="utf-8")


def pending(line, by):
    """The committer's half: mark this work as the next release, whatever number CI gives it."""
    VERSION_FILE.write_text(PENDING + "\n", encoding="utf-8")
    text = f"{by}: {line}" if by else line
    write_note(PENDING, text, text)
    add_row(PENDING, text)
    print(f"release_stamp: version.txt is the pending version; note {note_path(PENDING).relative_to(ROOT)} and its row written")


def served_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        rel_dir = Path(dirpath).relative_to(ROOT).as_posix()
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            rel = f"{rel_dir}/{name}" if rel_dir != "." else name
            if not rel.startswith(SKIP_PREFIXES):
                yield Path(dirpath) / name, rel


def stamp_pending(new):
    """Every pending version in the served tree becomes the release's number: contents, then paths."""
    token, changed, moved = PENDING.encode(), 0, 0
    stamped = []
    for p, rel in list(served_files()):
        b = p.read_bytes()
        if token in b:
            p.write_bytes(b.replace(token, new.encode()))
            changed += 1
            stamped.append(rel)
    rerecord(stamped)
    for p, rel in sorted(served_files(), key=lambda x: -len(x[1])):
        if PENDING in p.name:
            p.rename(p.with_name(p.name.replace(PENDING, new)))
            moved += 1
    for dirpath, dirnames, _ in sorted(os.walk(ROOT), key=lambda x: -len(x[0])):
        for d in dirnames:
            if PENDING in d and d not in SKIP_DIRS:
                (Path(dirpath) / d).rename(Path(dirpath) / d.replace(PENDING, new))
                moved += 1
    return changed, moved


SYNC_RECORD = ROOT / "admin/build/newsroom-sync.json"


def rerecord(stamped):
    """The import record keeps a hash of every page the sync wrote, and the gate refuses a page edited after it
    ("imported from sgit.ai and edited here"). A page the sync wrote with the pending version is edited by this
    stamp and nothing else, so its hash is recorded again, the way the sync itself would have recorded it."""
    if not stamped or not SYNC_RECORD.exists():
        return
    sys.path.insert(0, str(ROOT / "admin/build"))
    from sync_newsroom import content_sha
    record = json.loads(SYNC_RECORD.read_text(encoding="utf-8"))
    n = 0
    for rel in stamped:
        entry = record.get("files", {}).get(rel)
        if entry is not None:
            entry["sha256"] = content_sha((ROOT / rel).read_bytes(), rel)
            n += 1
    if n:
        SYNC_RECORD.write_text(json.dumps(record, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"release_stamp: {n} imported page(s) re-recorded after the stamp")


def git(*a):
    return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True, check=True).stdout


def unreleased_messages(since):
    """The pushes this release carries that ran no build: their subjects and first paragraphs, oldest first."""
    rng = f"{since}..HEAD" if since else "HEAD"
    out = []
    for c in git("rev-list", "--reverse", "--no-merges", rng).split():
        if git("log", "-1", "--format=%an", c).strip() == "GitHub Actions":
            continue
        subject = git("log", "-1", "--format=%s", c).strip()
        subject = re.sub(r"^site v\d+\.\d+\.\d+:\s*", "", subject)
        body = git("log", "-1", "--format=%b", c).strip().split("\n\n")[0]
        body = "\n".join(l for l in body.splitlines() if not re.match(r"^[A-Z][A-Za-z-]+: ", l))
        out.append((subject, body.replace("\n", " ").strip()))
    return out


def dev_releases(new):
    """The dev releases a major on main carries: every vA.(B-1).N tag after vA.(B-1).0, with its subject."""
    a, b, _ = (int(x) for x in new[1:].split("."))
    out = []
    for t in git("tag", "-l", f"v{a}.{b - 1}.*").split():
        if not SEMVER.match(t) or t.endswith(".0"):
            continue
        subj = re.sub(r"^site v\d+\.\d+\.\d+:\s*", "", git("log", "-1", "--format=%s", t).strip())
        out.append((t, subj))
    return sorted(out, key=lambda x: int(x[0].rsplit(".", 1)[1]))


def release(new, since, branch):
    if not SEMVER.match(new) or new == PENDING:
        sys.exit(f"release_stamp: {new!r} is not a release number")
    if VERSION_FILE.read_text().strip() == new:
        sys.exit(f"release_stamp: version.txt already says {new}")
    changed, moved = stamp_pending(new)
    print(f"release_stamp: the pending version became {new} in {changed} file(s), {moved} path(s)")
    if not note_path(new).exists():
        msgs = unreleased_messages(since)
        if branch == "main":
            rels = dev_releases(new)
            line = (f"The major release {new}: {len(rels)} releases from dev, {rels[0][0]} to {rels[-1][0]}."
                    if rels else f"The major release {new}.")
            body = line + "\n\n" + "\n".join(f"- {v}: {subj}" for v, subj in rels)
            write_note(new, line, body, kind="major")
        else:
            line = "; ".join(s for s, _ in msgs) or "A release with no change of its own."
            body = "\n\n".join(f"{s}" + (f" {b}" if b else "") for s, b in msgs) or line
            write_note(new, line, body)
        add_row(new, line)
        print(f"release_stamp: wrote the note and the row for {new} from {len(msgs)} commit message(s)")
    VERSION_FILE.write_text(new + "\n", encoding="utf-8")
    for step in ("engineering", "chrome", "gen_sitemap", "gen_llms_full"):
        subprocess.run([sys.executable, f"admin/build/{step}.py"], cwd=ROOT, check=True)
    print(f"release_stamp: {new} stamped")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("version", nargs="?")
    ap.add_argument("--pending", metavar="LINE")
    ap.add_argument("--by", default="")
    ap.add_argument("--since", default="")
    ap.add_argument("--branch", default="dev")
    a = ap.parse_args()
    if a.pending:
        pending(a.pending, a.by)
    elif a.version:
        release(a.version, a.since, a.branch)
    else:
        ap.error("give a version (CI) or --pending LINE (the committer)")


if __name__ == "__main__":
    main()
