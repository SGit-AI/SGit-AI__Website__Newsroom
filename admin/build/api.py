#!/usr/bin/env python3
"""The reader code's home, pinned: api.newsroom.sgit.ai.

    python3 admin/build/api.py               # check every page against the pin; exit 1 on a problem
    python3 admin/build/api.py --repoint     # rewrite every page's reader-file references to the pinned release, in place
    python3 admin/build/api.py --rerecord    # recompute newsroom-sync.json's content hashes under the normaliser

Since site v0.13.0 the code a reader runs (the meter, the reading lists, subscribe, the vault layer, search,
the wire reader, the vendored vault library, the passkey lab) is not in this repository. It lives in
SGit-AI/SGit-AI__Website__Newsroom__API and is served from https://api.newsroom.sgit.ai/<release>/<path>, at
the same paths it had here. This site pins one release (admin/build/api.json) and keeps a copy of that
release's manifest (admin/build/api-manifest.json: every path with its SHA-256). Every page this site writes
or imports loads the reader code from that host, never from a relative path, and never unversioned. A rollback
is a change to api.json and a run of --repoint.

The move's brief: https://newsroom.sgit.ai/articles/explorer-to-villager-newsroom.html, refreshed in the API
repository's briefs/. Its rule for the move is that the live site serves the same bytes before and after,
proved by hash: scripts, styles and JSON raw; pages with the chrome and the version stamps normalised, which
is what validate.js check 11 already did for imported pages. The move adds one normalisation: a reader-file
reference, relative (as before) or on the API host (as after), reads as API/<path>. NORMALISE below is that
rule; sync_newsroom.py appends it to its own list and validate.js mirrors it. Keep the three in step.

What the reader's browser does not notice: localStorage belongs to the page's origin, so the meter's state
stays on newsroom.sgit.ai whichever host serves the script; the meter fetches the article feed and the contact
file from the page's origin (cfg.root), which is unchanged; every address (the Stripe return page, /for/#…,
/persona/<id>/) stays.
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PIN_FILE = ROOT / "admin/build/api.json"
MANIFEST_FILE = ROOT / "admin/build/api-manifest.json"

PIN = json.loads(PIN_FILE.read_text(encoding="utf-8"))
HOST = PIN["host"].rstrip("/")          # https://api.newsroom.sgit.ai
RELEASE = PIN["release"]                # vX.Y.Z, the one release this site loads
assert re.fullmatch(r"v\d+\.\d+\.\d+", RELEASE), f"api.json: release {RELEASE!r} is not vX.Y.Z"


def api_url(path):
    """The pinned, versioned URL of a reader file."""
    return f"{HOST}/{RELEASE}/{path.lstrip('/')}"


def manifest():
    return json.loads(MANIFEST_FILE.read_text(encoding="utf-8"))


def served_paths():
    return {f["path"] for f in manifest()["files"]}


# The reader files, by path from the site root: what tools/served.json in the API repository lists, as prefixes.
_PATH = (r"(assets/(?:components|vault-pane|search|vendor/sg-vault)/[^\"'\s<>]+"
         r"|assets/(?:subscribe\.js|newsroom-vault\.js|door\.js)(?:\?[^\"'\s<>]*)?"
         r"|for/(?:reading-list|make)\.js|for/for\.css"
         r"|wire/(?:wire|vault-reader)\.js|wire/wire\.css"
         r"|passkey/(?:lab\.js|lab\.css|vectors\.json))")
# A page in for/, wire/ or passkey/ named its own files without a directory.
SAME_DIR = {"reading-list.js": "for/", "make.js": "for/", "for.css": "for/",
            "wire.js": "wire/", "wire.css": "wire/", "vault-reader.js": "wire/",
            "lab.js": "passkey/", "lab.css": "passkey/", "vectors.json": "passkey/"}
_SAME = r"(" + "|".join(re.escape(k) for k in SAME_DIR) + r")"


def is_reader_path(path):
    """A site-root path that the API host serves (a file of the move)."""
    return bool(re.fullmatch(_PATH, path.lstrip("/")))

_REL = r"(?:\./|(?:\.\./)+)?"                       # '../', '../../', './' or nothing (a page at the root)
_API = re.escape(HOST) + r"/v\d+\.\d+\.\d+/"        # any release of the host

# The normaliser: three quoted forms of a reader-file reference, each read as "API/<path>".
NORMALISE = [
    (re.compile(r"([\"'])" + _API + _PATH + r"\1"), r"\1API/\2\1"),
    (re.compile(r"([\"'])" + _REL + _PATH + r"\1"), r"\1API/\2\1"),
    (re.compile(r"([\"'])(?:\./)?" + _SAME + r"\1"), lambda m: f"{m.group(1)}API/{SAME_DIR[m.group(2)]}{m.group(2)}{m.group(1)}"),
]


def normalise(text):
    for pattern, repl in NORMALISE:
        text = pattern.sub(repl, text)
    return text


# The repoint: the same three forms, rewritten to the pinned release. Only in real tags (href, src and the
# other URL attributes) and in <script> bodies: a code sample is text and stays as it is, as the sync's rule.
REAL_TAG = re.compile(r"<[a-zA-Z][^<>]*>")
URL_ATTR = re.compile(r"""\b(href|src|data-src|action|poster|data-dir|data-trail-img)=(["'])([^"']*)\2""")
SCRIPT = re.compile(r"(<script\b[^>]*>)([\s\S]*?)(</script>)")
QUOTED = re.compile(r"""(["'])([^"'\n]*)\1""")
_FULL_REL = re.compile(_REL + _PATH)
_FULL_SAME = re.compile(r"(?:\./)?" + _SAME)
_FULL_API = re.compile(_API + _PATH)


def repoint_ref(s):
    """One quoted string: a reader-file reference becomes its pinned URL; anything else is returned as it is."""
    m = _FULL_API.fullmatch(s) or _FULL_REL.fullmatch(s)
    if m:
        return api_url(m.group(1))
    m = _FULL_SAME.fullmatch(s)
    if m:
        return api_url(SAME_DIR[m.group(1)] + m.group(1))
    return s


def repoint(text):
    def tag(m):
        return URL_ATTR.sub(lambda a: f"{a.group(1)}={a.group(2)}{repoint_ref(a.group(3))}{a.group(2)}", m.group(0))
    text = REAL_TAG.sub(tag, text)

    def body(m):
        return m.group(1) + QUOTED.sub(lambda q: q.group(1) + repoint_ref(q.group(2)) + q.group(1), m.group(2)) + m.group(3)
    return SCRIPT.sub(body, text)


def pages():
    for p in sorted(ROOT.rglob("*.html")):
        parts = p.relative_to(ROOT).parts
        if ".git" in parts or "summit-archive" in parts or "vault-app" in parts or "node_modules" in parts:
            continue          # copies as served, and the app that renders inside a vault: not this site's pages
        yield p


def check():
    """Every reader-file reference on every page is the pinned release of the host, and a path the manifest has."""
    served = served_paths()
    problems = []
    pat_api = re.compile(r"([\"'])" + re.escape(HOST) + r"/(v\d+\.\d+\.\d+)/" + _PATH + r"\1")
    for p in pages():
        rel = p.relative_to(ROOT).as_posix()
        text = p.read_text(encoding="utf-8")
        if repoint(text) != text:
            problems.append(f"{rel}: loads a reader file by a relative path, or from another release; run --repoint")
        for m in pat_api.finditer(text):
            path = m.group(3).split("?")[0]
            if m.group(2) != RELEASE:
                problems.append(f"{rel}: {m.group(2)}/{path} is not the pinned release {RELEASE}")
            elif path not in served:
                problems.append(f"{rel}: {path} is not in the pinned release's manifest")
    return problems


def rerecord():
    """newsroom-sync.json records the content hash of every imported file. After a repoint the pages' bytes
    changed by the one rule the normaliser sets aside, so the hashes are recomputed under it; a verbatim
    file that moved to the API host is no longer imported and leaves the record."""
    sys.path.insert(0, str(Path(__file__).parent))
    from sync_newsroom import RECORD, content_sha  # noqa: E402  (its NORMALISE includes ours)
    record = json.loads(RECORD.read_text(encoding="utf-8"))
    dropped, changed = [], 0
    for rel in list(record["files"]):
        f = ROOT / rel
        if not f.exists():
            if _FULL_REL.fullmatch(rel):
                dropped.append(rel); del record["files"][rel]; continue
            sys.exit(f"api: {rel} is in the sync record and missing, and it is not a reader file; re-run the sync")
        got = content_sha(f.read_bytes(), rel)
        if got != record["files"][rel]["sha256"]:
            record["files"][rel]["sha256"] = got; changed += 1
    record["counts"]["files"] = len(record["files"])
    record["counts"]["verbatim"] = sum(1 for r in record["files"] if re.search(r"\.(js|css|tpl|mjs)$|^\.well-known/", r))
    RECORD.write_text(json.dumps(record, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"api: sync record: {changed} hash(es) recomputed, {len(dropped)} reader file(s) left the import")
    for d in dropped:
        print(f"  - {d}")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--repoint", action="store_true", help="rewrite every page's reader-file references to the pinned release")
    ap.add_argument("--rerecord", action="store_true", help="recompute the sync record's content hashes under the normaliser")
    a = ap.parse_args()
    print(f"api: {HOST}/{RELEASE}/ ({len(served_paths())} files in the pinned manifest)")
    if a.repoint:
        n = 0
        for p in pages():
            text = p.read_text(encoding="utf-8")
            out = repoint(text)
            if out != text:
                p.write_text(out, encoding="utf-8"); n += 1
        print(f"api: {n} page(s) repointed to {RELEASE}")
    if a.rerecord:
        rerecord()
    problems = check()
    if problems:
        print(f"api: {len(problems)} problem(s)")
        for x in problems[:30]:
            print("  ✗ " + x)
        if len(problems) > 30:
            print(f"  … and {len(problems) - 30} more")
        sys.exit(1)
    print("api: every page loads the reader code from the pinned release")


if __name__ == "__main__":
    main()
