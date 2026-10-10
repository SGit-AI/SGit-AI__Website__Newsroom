#!/usr/bin/env python3
"""Import the SGit Newsroom from a checkout of sgit.ai, at the same paths.

    python3 admin/build/sync_newsroom.py --from /path/to/SGit-AI__Website

Until cutover (brief Phase 5) sgit.ai is still the newsroom's publisher: articles keep
arriving there daily, and its generator is a 680 KB build_pages.py that also builds the
rest of sgit.ai. So this site does not re-generate the newsroom. It imports the BUILT
pages and re-points them, which makes "each article's text matches sgit.ai" true by
construction rather than by a check that could drift. Porting the generator is the
cutover step, when this site becomes the publisher.

The brief's own words for the rule this follows: "Before cutover, sync from sgit.ai as
needed. Do not edit moved content on the new side, or the two will drift." Nothing under
the moved paths is edited by hand here. If a page is wrong, it is fixed on sgit.ai and
re-imported.

What changes on the way in, and nothing else:

  1. Relative links resolve to one of three places. A path that moved stays relative. A
     path this site has its own version of (index.html, llms.txt) stays relative and now
     means this site's. Anything else is sgit.ai's, so it becomes https://sgit.ai/<path>:
     an article linking to the sgit docs must still reach the sgit docs.
  2. Absolute https://sgit.ai/<moved path> becomes https://newsroom.sgit.ai/<path>, which
     re-points canonical URLs, og:url, og:image, JSON-LD, the feed and the wire.
  3. sgit.ai's stylesheet arrives as assets/newsroom.css, because assets/site.css is
     already this site's own and 129 pages use it. The page loader is told the new name.
  4. The page loader stops loading assets/site-chat.js: it is sgit.ai's site chat, over
     sgit.ai's own content index, and here it would answer questions about the wrong site.
     Its freshness check is left as it is, naming sgit.ai, so it is inert on this host.
  5. The front page is also written to / (brief: "/articles/index.html becomes both / and
     /articles/index.html"), with its links re-based one level up, and both copies name /
     as their canonical URL.

Scripts, styles, components and /.well-known/sgit-subscribe.json are copied byte for byte.
The brief requires it twice: a published component path never changes, and the subscribe
lane keeps the same public key so subscriptions land in the same vault. The sync refuses
to run if any of them would change.

The record of what was imported (source commit, version, SHA-256 of every source file and
every written file) goes to admin/build/newsroom-sync.json, OUTSIDE the imported tree:
a record about an artefact does not live inside it.

The sync never overwrites a file this site wrote itself. It replaces only what the last
sync wrote, plus the pages named in REPLACES, each of which must already have a dated copy
in archive/ (archive.py makes it). Anything else in the way stops the run.
"""
import argparse
import hashlib
import json
import posixpath
import re
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

ROOT     = Path(__file__).resolve().parents[2]
HOST     = (ROOT / "CNAME").read_text().strip()               # newsroom.sgit.ai
SRC_HOST = "sgit.ai"
RECORD   = ROOT / "admin/build/newsroom-sync.json"

# The moved tree, from the brief's "What moves" table.
MOVED_DIRS = ["articles", "newsroom", "account", "subscribe", "meter", "og", "assets/components"]
# Single files: source path -> path here.
MOVED_FILES = {
    "assets/site.css": "assets/newsroom.css",
    "assets/site.js": "assets/site.js",
    "assets/shots.js": "assets/shots.js",
    "assets/subscribe.js": "assets/subscribe.js",
    ".well-known/sgit-subscribe.json": ".well-known/sgit-subscribe.json",
}
# Paths that exist on both sites, where a link from an imported page means THIS site's copy.
LOCAL_EQUIVALENTS = {"index.html", "index.md", "llms.txt", "llms-full.txt"}
# Pages this site owned before the import and the import now owns. Each must already be
# held, dated, in archive/ (see archive.py SNAPSHOTS) before it may be replaced.
REPLACES = {"index.html", "index.md", "newsroom/index.html"}
# Copied byte for byte and never transformed (see the docstring).
VERBATIM = re.compile(r"\.(js|css|tpl|mjs)$|^\.well-known/")
TEXT     = re.compile(r"\.(html|md|xml|json|txt)$")
FRONT    = ("articles/index.html", "articles/index.md")    # also written to the root

URL_ATTR = re.compile(r'\b(href|src|data-src|action|poster)="([^"]*)"')
MD_LINK  = re.compile(r'(\]\()([^)\s]+)((?:\s+"[^"]*")?\))')
ABS_SRC  = re.compile(r'https?://(?:www\.)?sgit\.ai/([^\s"\'<>)\]]*)')


def sha(data):
    return hashlib.sha256(data).hexdigest()


# chrome.py stamps this site's nav, footer and version onto every page after the import, so
# the bytes on disk are never the bytes the sync wrote. The record therefore hashes the
# CONTENT: the same file with those three blocks emptied. validate.js check 11 applies the
# identical normalisation and compares, which is what makes "do not edit moved content on
# the new side" a gate rather than a request. Keep the two in step.
NORMALISE = [
    (re.compile(r'<nav class="site">[\s\S]*?</nav>'), '<nav class="site"></nav>'),
    (re.compile(r'<footer class="site">[\s\S]*?</footer>'), '<footer class="site"></footer>'),
    (re.compile(r'<span class="llmschip-m">[^<]*</span>'), '<span class="llmschip-m"></span>'),
    (re.compile(r'\u00b7 site v\d+\.\d+\.\d+ \u00b7'), '\u00b7 site \u00b7'),
]


def content_sha(data, path):
    if not path.endswith((".html", ".md")):
        return sha(data)
    text = data.decode("utf-8")
    for pattern, repl in NORMALISE:
        text = pattern.sub(repl, text, count=1)
    return sha(text.encode("utf-8"))


def moved_target(path):
    """Where a source-site path lives here, or None when it did not move."""
    path = path.lstrip("/")
    if path in MOVED_FILES:
        return MOVED_FILES[path]
    for d in MOVED_DIRS:
        if path == d or path.startswith(d + "/"):
            return path
    return None


def resolve(src_file, url):
    """The site-root path a relative URL in src_file points at, or None if it is not a
    same-site relative reference (a scheme, protocol-relative, fragment-only, or empty)."""
    if not url or url.startswith(("#", "//")) or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", url):
        return None
    parts = urlsplit(url)
    if not parts.path:
        return None
    base = "" if parts.path.startswith("/") else posixpath.dirname(src_file)
    joined = posixpath.normpath(posixpath.join(base, parts.path.lstrip("/")))
    if joined.startswith(".."):
        return None
    if parts.path.endswith("/") and not joined.endswith("/"):
        joined += "/"
    return joined, parts


def relative(from_file, to_path):
    rel = posixpath.relpath(to_path.rstrip("/") or ".", posixpath.dirname(from_file) or ".")
    return rel + ("/" if to_path.endswith("/") and rel != "." else "")


def rewrite_url(url, src_file, dest_file):
    # An attribute value with a quote, a plus or a brace in it is script building markup
    # ('<a href="' + url + '">'), not a URL. Rewriting it would rewrite the code.
    if re.search(r"['+{}<>$\\\s]", url):
        return url
    r = resolve(src_file, url)
    if r is None:
        return url
    path, parts = r
    bare = path.rstrip("/")
    target = moved_target(bare)
    if target is not None:
        new = relative(dest_file, target + ("/" if path.endswith("/") else ""))
    elif bare in LOCAL_EQUIVALENTS:
        new = relative(dest_file, bare)
    else:
        return urlunsplit(("https", SRC_HOST, "/" + path, parts.query, parts.fragment))
    return urlunsplit(("", "", new, parts.query, parts.fragment))


def rewrite_abs(m):
    tail = m.group(1)
    path = urlsplit("/" + tail).path.lstrip("/")
    target = moved_target(path.rstrip("/"))
    if target is None:
        return m.group(0)
    rest = tail[len(path):]
    return f"https://{HOST}/{target}{'/' if path.endswith('/') and target else ''}{rest}"


def transform(text, src_file, dest_file, kind):
    text = ABS_SRC.sub(rewrite_abs, text)
    if kind == "html":
        text = URL_ATTR.sub(lambda m: f'{m.group(1)}="{rewrite_url(m.group(2), src_file, dest_file)}"', text)
        depth = dest_file.count("/")
        text = re.sub(r'(<html[^>]*\bdata-root=")[^"]*(")', lambda m: m.group(1) + "../" * depth + m.group(2), text, count=1)
        # The page loader: sgit.ai's stylesheet has a different name here and its site chat
        # does not come across. Its freshness check is deliberately left naming sgit.ai, so
        # it does nothing here: the page carries sgit.ai's release number, and comparing that
        # with this site's would reload every page against the wrong version.
        text = text.replace("'assets/site.css'", "'assets/newsroom.css'")
        text = text.replace("js(sg,'assets/site-chat.js');", "")
        # The edition line names the site and release that produced the edition.
        text = re.sub(r'<span>sgit\.ai &middot; (v\d+\.\d+\.\d+)</span>',
                      rf'<span>{HOST} &middot; edition from sgit.ai \1</span>', text)
        if dest_file != src_file:
            # Script-string paths (the dynamic imports and fetches), re-based to the new depth.
            # A re-based path that loses its ../ must gain ./ : import('assets/x.js') is a bare
            # module specifier and the browser refuses it, where import('./assets/x.js') loads.
            def script_path(m):
                p = rewrite_url(m.group(2) + m.group(3), src_file, dest_file)
                if not p.startswith(("../", "./", "/", "http")):
                    p = "./" + p
                return m.group(1) + p + m.group(1)
            text = re.sub(r"""(['"])((?:\.\./)+)((?:assets|articles|newsroom|account|subscribe|meter|og)/[^'"]*)\1""",
                          script_path, text)
        if src_file == "articles/index.html":
            # One front page at two addresses names one canonical address: the root.
            text = re.sub(r'(<link rel="canonical" href=")[^"]*(")', rf'\1https://{HOST}/\2', text, count=1)
            text = re.sub(r'(<meta property="og:url" content=")[^"]*(")', rf'\1https://{HOST}/\2', text, count=1)
    elif kind == "md":
        text = MD_LINK.sub(lambda m: m.group(1) + rewrite_url(m.group(2), src_file, dest_file) + m.group(3), text)
    return text


def source_meta(src):
    def git(*args):
        return subprocess.run(["git", "-C", str(src), *args], capture_output=True, text=True).stdout.strip()
    version = (src / "version.txt").read_text().strip() if (src / "version.txt").exists() else ""
    return {
        "repository": "https://github.com/SGit-AI/SGit-AI__Website",
        "commit": git("rev-parse", "HEAD"),
        "commit_date": git("log", "-1", "--format=%cs"),
        "subject": git("log", "-1", "--format=%s"),
        "version": version,
    }


def plan(src):
    """(source path, destination path) for every file that moves."""
    out = []
    for d in MOVED_DIRS:
        for p in sorted((src / d).rglob("*")):
            if p.is_file():
                rel = p.relative_to(src).as_posix()
                out.append((rel, rel))
    for s, d in MOVED_FILES.items():
        if (src / s).is_file():
            out.append((s, d))
    for s in FRONT:
        out.append((s, s.split("/", 1)[1]))           # articles/index.html -> index.html
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--from", dest="src", required=True, help="a checkout of SGit-AI/SGit-AI__Website")
    ap.add_argument("--check", action="store_true", help="report what would change, write nothing")
    args = ap.parse_args()
    src = Path(args.src).resolve()
    if not (src / "articles/index.html").exists() or not (src / "admin/build/build_pages.py").exists():
        sys.exit(f"sync: {src} is not a checkout of the sgit.ai website")

    previous = json.loads(RECORD.read_text())["files"] if RECORD.exists() else {}
    files, problems = {}, []
    for s, d in plan(src):
        raw = (src / s).read_bytes()
        kind = Path(s).suffix.lstrip(".")
        if VERBATIM.search(s) or not TEXT.search(s):
            out = raw
        else:
            out = transform(raw.decode("utf-8"), s, d, kind).encode("utf-8")
        if d == "index.md":
            version = (ROOT / "admin/build/version.txt").read_text().strip()
            out += (f"\n\n---\n\n*{HOST} \u00b7 site {version} \u00b7 the front page, imported from "
                    f"sgit.ai. This site's own index is [llms.txt](llms.txt).*\n").encode("utf-8")
        if VERBATIM.search(s) and out != raw:
            problems.append(f"{d}: a verbatim file would change")
        files[d] = {"from": s, "sha256_source": sha(raw), "sha256": content_sha(out, d),
                    "_out": out}

    # Never overwrite or delete a file this site wrote itself.
    for d in files:
        p = ROOT / d
        if p.exists() and d not in previous:
            if d in REPLACES:
                snap = archive_holds(d)
                if not snap:
                    problems.append(f"{d}: this site's own page; archive it first (python3 admin/build/archive.py --snapshot)")
            else:
                problems.append(f"{d}: exists and was not written by a previous sync; refusing to overwrite")
    stale = [d for d in previous if d not in files]
    if problems:
        for p in problems:
            print("  ✗ " + p, file=sys.stderr)
        sys.exit(f"sync: {len(problems)} problem(s), nothing written")

    changed = [d for d, f in files.items()
               if not (ROOT / d).exists() or content_sha((ROOT / d).read_bytes(), d) != f["sha256"]]
    if args.check:
        print(f"sync --check: {len(changed)} file(s) would change, {len(stale)} would be removed")
        return

    for d in changed:
        p = ROOT / d
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(files[d]["_out"])
    for d in stale:
        (ROOT / d).unlink(missing_ok=True)

    meta = source_meta(src)
    record = {
        "what": "The SGit Newsroom, imported from sgit.ai's built pages at the same paths. "
                "Written by admin/build/sync_newsroom.py; do not edit the imported files by hand.",
        "sha256": "sha256_source is the file as sgit.ai serves it. sha256 is the file as imported, "
                  "with the site nav, the site footer, the agent-chip stamp and the index.md version "
                  "line emptied, because chrome.py restamps those on every release. validate.js "
                  "check 11 recomputes it for every file listed here.",
        "source": meta,
        "host": HOST,
        "counts": {
            "files": len(files),
            "pages": sum(1 for d in files if d.endswith(".html")),
            "articles": sum(1 for d in files if re.fullmatch(r"articles/[^/]+\.html", d)
                            and d not in ("articles/index.html", "articles/graphs.html")),
            "verbatim": sum(1 for f in files.values() if f["sha256"] == f["sha256_source"]),
        },
        "files": {d: {k: v for k, v in f.items() if k != "_out"} for d, f in sorted(files.items())},
    }
    RECORD.write_text(json.dumps(record, indent=1, ensure_ascii=False) + "\n")
    c = record["counts"]
    print(f"sync: sgit.ai {meta['version']} ({meta['commit'][:7]}) -> {HOST}: "
          f"{c['files']} files, {c['pages']} pages, {c['articles']} articles; "
          f"{len(changed)} written, {len(stale)} removed, {c['verbatim']} byte-identical to source")


def archive_holds(path):
    try:
        sys.path.insert(0, str(Path(__file__).parent))
        import archive
        return any(s["from"] == path and (ROOT / s["to"]).exists() for s in archive.SNAPSHOTS)
    except Exception:
        return False


if __name__ == "__main__":
    main()
