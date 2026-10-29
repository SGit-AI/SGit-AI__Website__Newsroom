#!/usr/bin/env python3
"""Publish the articles written here: the first step of the cutover, where this site becomes the publisher.

    python3 admin/build/publish.py --from /path/to/SGit-AI__Website [--node-modules DIR] [--check]

Articles are now written in this repository, not on sgit.ai:

    admin/content/articles/<slug>.md              the article (sgit.ai's authoring contract, CONTENT.md)
    admin/content/articles/graphs/<slug>.json     its semantic graph
    admin/content/articles/images/<name>.webp     its figures
    admin/content/articles/data/<slug>__*.json    the data it was written from, when there is some
    admin/content/newsletter/NNN-YYYY-MM-DD.md     a newsletter issue (sgit.ai's newsroom README has the format)

The generator has not moved yet: it is sgit.ai's 680 KB build_pages.py, which also builds the rest of
sgit.ai. Until it is ported, this script borrows it without touching sgit.ai. It never writes to the
checkout it is given, and nothing is pushed anywhere:

  1. Clone the sgit.ai checkout into a temporary directory (a local clone, so its history comes too).
  2. Replay this repository's history of admin/content/articles/ into the clone, one commit per commit
     here, with the same author date and subject, then lay the working tree on top. sgit.ai's generator
     reads an article's first-publish time and its versions (v1.0.0, v1.1.0 and the diff pages) from
     git, so replaying the history keeps both true for articles written here.
  3. Run the generator there: build, link-preview cards, banners, build, banners, validate. Its validator
     enforces the contract (no em-dash, the ladder word, links that resolve, graph limits) on our articles
     exactly as it did on sgit.ai.
  4. Import the result with sync_newsroom.py --from <the clone>, naming the slugs written here
     (--authored), so their bylines name this site's release, and recording the source as sgit.ai's
     commit plus this repository's article sources (--source-meta).

A slug written here that already exists on sgit.ai stops the run: the two would fight for one page. So does
a newsletter issue whose number sgit.ai already has.
The temporary clone is deleted at the end unless --keep is given.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT    = Path(__file__).resolve().parents[2]
CONTENT = "admin/content/articles"
NEWSLETTER = "admin/content/newsletter"                 # -> sgit.ai's admin/content/newsroom/newsletter/
# Folded history: sources whose published version pages start from the current text. For each path
# listed, the replay writes the working tree's version at every past commit, so the site shows one
# version and no diff page repeats what was removed. The repository's git history is untouched and
# keeps every version. Use only for text the owner decides must not be on the site, such as a name
# published before its owner agreed. Each entry records why.
FOLDS = ROOT / "admin/build/history-folds.json"
# Where each kind of source lands in the sgit.ai tree.
TARGETS = (("images/", "articles/images/"), ("data/", "articles/data/"), ("graphs/", CONTENT + "/graphs/"), ("", CONTENT + "/"))


def run(cmd, cwd, env=None, quiet=False, tolerate=False):
    r = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True)
    if r.returncode != 0 and tolerate:
        print(f"    {' '.join(cmd)} stopped (expected before the cards exist); the next build must pass")
        return r.stdout
    if r.returncode != 0:
        sys.stdout.write(r.stdout[-4000:]); sys.stderr.write(r.stderr[-4000:])
        sys.exit(f"publish: {' '.join(cmd)} failed in {cwd}")
    if not quiet:
        tail = [l for l in r.stdout.splitlines() if l.strip()][-2:]
        for l in tail:
            print("   ", l)
    return r.stdout


def git(*a, cwd=ROOT):
    return run(["git", *a], cwd, quiet=True)


def target(rel):
    """admin/content/articles/<rest> or admin/content/newsletter/<issue> here -> its path in the sgit.ai tree."""
    if rel.startswith(NEWSLETTER + "/"):
        return "admin/content/newsroom/newsletter/" + rel[len(NEWSLETTER) + 1:]
    rest = rel[len(CONTENT) + 1:]
    for prefix, dest in TARGETS:
        if rest.startswith(prefix):
            return dest + rest[len(prefix):]


def sources():
    out = []
    for base in (ROOT / CONTENT, ROOT / NEWSLETTER):
        if base.exists():
            out += [p.relative_to(ROOT).as_posix() for p in base.rglob("*") if p.is_file() and p.name != "README.md"]
    return sorted(out)


def authored_slugs(files):
    return sorted(Path(f).stem for f in files if f.startswith(CONTENT + "/") and f.count("/") == 3 and f.endswith(".md"))


PENDING = b"v999.0.0"   # admin/build/release_stamp.py: the version a work commit carries until CI numbers it


def settle_pending(path, body):
    """An article written in a work commit says `version: <pending>`, and CI's release commit changes that line
    to the number it picked. Replayed as is, that second commit would be a change to the article's details, a
    patch version (v1.0.1) of every new article. So a past commit's pending version reads as the number the
    article has now; while it is still pending, it stays pending, and CI stamps the pages."""
    if PENDING not in body or not path.endswith(".md") or not (ROOT / path).exists():
        return body
    m = re.search(rb"^version: (v\d+\.\d+\.\d+)\s*$", (ROOT / path).read_bytes(), re.M)
    return body.replace(PENDING, m.group(1)) if m else body


def replay(clone):
    """One commit in the clone for each commit here that touched the article sources."""
    log = git("log", "--reverse", "--format=%H%x09%aI%x09%an%x09%ae%x09%s", "--", CONTENT, NEWSLETTER).splitlines()
    folds = json.loads(FOLDS.read_text())["paths"] if FOLDS.exists() else {}
    for line in log:
        sha, date, name, email, subject = line.split("\t", 4)
        changed = git("diff-tree", "--no-commit-id", "--name-status", "-r", "--root", sha, "--", CONTENT, NEWSLETTER).splitlines()
        for row in changed:
            status, *paths = row.split("\t")
            path = paths[-1]
            if path.endswith("README.md") or not target(path):
                continue
            dest = clone / target(path)
            if status.startswith("D"):
                dest.unlink(missing_ok=True)
                continue
            if status.startswith("R"):
                (clone / target(paths[0])).unlink(missing_ok=True)
            dest.parent.mkdir(parents=True, exist_ok=True)
            if path in folds and (ROOT / path).exists():
                dest.write_bytes((ROOT / path).read_bytes())          # folded: the current text at every commit
                continue
            body = subprocess.run(["git", "show", f"{sha}:{path}"], cwd=ROOT, capture_output=True).stdout
            dest.write_bytes(settle_pending(path, body))
        run(["git", "add", "-A"], clone, quiet=True)
        env = dict(os.environ, GIT_AUTHOR_DATE=date, GIT_COMMITTER_DATE=date, GIT_AUTHOR_NAME=name,
                   GIT_AUTHOR_EMAIL=email, GIT_COMMITTER_NAME=name, GIT_COMMITTER_EMAIL=email)
        run(["git", "commit", "-q", "--allow-empty", "-m", f"newsroom {sha[:8]}: {subject}"], clone, env=env, quiet=True)
    return len(log)


TRAILS = ROOT / "admin/content/trails.json"


def merge_trails(clone):
    """Add the trails written here to sgit.ai's admin/content/trails.json in the clone, so `!trail <name>` in an
    article written here renders the same row of cards the generator renders for sgit.ai's own trails. A trail
    has one publisher: a name sgit.ai already uses is refused, never overwritten."""
    if not TRAILS.exists():
        return
    ours = json.loads(TRAILS.read_text())
    dest = clone / "admin/content/trails.json"
    theirs = json.loads(dest.read_text()) if dest.exists() else {}
    clash = sorted(set(ours) & set(theirs))
    if clash:
        sys.exit(f"publish: trail {', '.join(clash)} also exists on sgit.ai; a trail has one publisher")
    theirs.update(ours)
    dest.write_text(json.dumps(theirs, indent=1, ensure_ascii=False) + "\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--from", dest="src", required=True, help="a checkout of SGit-AI/SGit-AI__Website (read only)")
    ap.add_argument("--node-modules", help="a node_modules with sharp and playwright, for the cards and banners")
    ap.add_argument("--check", action="store_true", help="build and validate, but do not import")
    ap.add_argument("--keep", action="store_true", help="keep the temporary clone and print where it is")
    args = ap.parse_args()
    src = Path(args.src).resolve()
    if not (src / "admin/build/build_pages.py").exists():
        sys.exit(f"publish: {src} is not a checkout of the sgit.ai website")

    files = sources()
    slugs = authored_slugs(files)
    if not slugs:
        sys.exit(f"publish: no articles in {CONTENT}/")
    theirs = {Path(f).name[:3] for f in run(["git", "ls-files", "--", "admin/content/newsroom/newsletter/"], src, quiet=True).split()}
    dup = sorted(Path(f).name for f in files if f.startswith(NEWSLETTER + "/") and Path(f).name[:3] in theirs)
    if dup:
        sys.exit(f"publish: {', '.join(dup)}: sgit.ai already has an issue with that number")
    upstream = run(["git", "ls-files", "--", f"{CONTENT}/*.md"], src, quiet=True).split()
    clash = sorted(set(slugs) & {Path(f).stem for f in upstream})
    if clash:
        sys.exit(f"publish: {', '.join(clash)} also exist on sgit.ai; a slug has one publisher")
    for f in files:                                            # a figure must not replace one of sgit.ai's
        if run(["git", "ls-files", "--", target(f)], src, quiet=True).strip():
            sys.exit(f"publish: {f} would replace sgit.ai's {target(f)}; give it another name")

    tmp = Path(tempfile.mkdtemp(prefix="newsroom-publish-"))
    clone = tmp / "site"
    print(f"1/4 clone sgit.ai {run(['git', 'rev-parse', '--short', 'HEAD'], src, quiet=True).strip()}")
    run(["git", "clone", "-q", "--no-hardlinks", str(src), str(clone)], tmp, quiet=True)
    run(["git", "checkout", "-q", run(["git", "rev-parse", "HEAD"], src, quiet=True).strip()], clone, quiet=True)
    run(["git", "config", "user.email", "newsroom@sgit.ai"], clone, quiet=True)
    run(["git", "config", "user.name", "newsroom publish"], clone, quiet=True)

    n = replay(clone)
    for f in files:                                            # the working tree, uncommitted: "this release"
        dest = clone / target(f)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / f, dest)
    merge_trails(clone)
    print(f"2/4 replayed {n} commit(s) of {CONTENT}/ and the working tree: {', '.join(slugs)}")

    print("3/4 generate and validate")
    if args.node_modules:
        (clone / "node_modules").symlink_to(Path(args.node_modules).resolve())
    # The first build writes the graphs the card maker reads, and refuses a new article whose card does not
    # exist yet; so with the cards to make, it may stop, and the second build is the gate. A new issue's cover
    # is first drawn by the last banner pass, and an issue page shows its cover and its LinkedIn box only when
    # the cover exists, so a third build follows it.
    # Since v0.13.7 the second and third builds run only when they have something to pick up: the first build
    # stopped, or the pass before them added a card or a banner. Most releases add no card and no cover, and
    # each build is about 80 seconds of a release's time.
    DRAWN = ("og", "articles/cards", "articles/banners")

    def drawn():
        """Which cards and banners exist. The pages link to a card and show a cover only when the file exists,
        and never read what is in it; and a redrawn image is not byte for byte the same, so contents would
        trigger a build every time."""
        return {str(f.relative_to(clone)) for d in DRAWN if (clone / d).exists()
                for f in (clone / d).rglob("*") if f.is_file()}

    # Seed the clone with the cards and banners this site already has from its last release, so the first
    # build can pass when no article is new, and links each article's card rather than the default; the passes
    # below redraw them, and any they add still trigger the builds that pick them up (v0.13.7).
    seeded = 0
    for d in DRAWN:
        if (ROOT / d).exists():
            for f in (ROOT / d).rglob("*"):
                dest = clone / f.relative_to(ROOT)
                if f.is_file() and not dest.exists():
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(f, dest)
                    seeded += 1
    print(f"    seeded {seeded} card(s) and banner(s) from the last release")

    if not args.node_modules:
        print("    no --node-modules: link-preview cards and banners are not made")
        run(["python3", "admin/build/build_pages.py"], clone)
    else:
        first = subprocess.run(["python3", "admin/build/build_pages.py"], cwd=clone, capture_output=True, text=True)
        if first.returncode != 0:
            print("    python3 admin/build/build_pages.py stopped (expected before the cards exist); the next build must pass")
        before = drawn()
        run(["node", "admin/build/make_og_cards.mjs"], clone)
        run(["node", "admin/build/make_banners.mjs"], clone)
        if first.returncode != 0 or drawn() != before:
            run(["python3", "admin/build/build_pages.py"], clone)
            before = drawn()
            run(["node", "admin/build/make_banners.mjs"], clone)
            if drawn() != before:
                run(["python3", "admin/build/build_pages.py"], clone)
            else:
                print("    no banner added: the third build is not needed")
        else:
            print("    no card or banner added: the second and third builds are not needed")
    run(["node", "admin/build/validate.js"], clone)

    if args.check:
        print(f"4/4 --check: not imported{'; the clone is at ' + str(clone) if args.keep else ''}")
    else:
        meta = {
            "repository": "https://github.com/SGit-AI/SGit-AI__Website",
            "commit": run(["git", "rev-parse", "HEAD"], src, quiet=True).strip(),
            "commit_date": run(["git", "log", "-1", "--format=%cs"], src, quiet=True).strip(),
            "subject": run(["git", "log", "-1", "--format=%s"], src, quiet=True).strip(),
            "version": "",
            "generated_with": "sgit.ai's build_pages.py, by admin/build/publish.py",
            "authored_here": {f: hashlib.sha256((ROOT / f).read_bytes()).hexdigest() for f in files},
        }
        meta_file = tmp / "source-meta.json"
        meta_file.write_text(json.dumps(meta, indent=1))
        print("4/4 import")
        run(["python3", "admin/build/sync_newsroom.py", "--from", str(clone), "--authored", ",".join(slugs),
             "--source-meta", str(meta_file)], ROOT)
    if args.keep:
        print(f"    kept: {clone}")
    else:
        shutil.rmtree(tmp)


if __name__ == "__main__":
    main()
