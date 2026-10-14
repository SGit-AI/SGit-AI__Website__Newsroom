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
  6. The site's name in the metadata (tab title, og:title, og:site_name, JSON-LD) becomes
     the SGit Newsroom, and the front page takes the newsroom's own title and description.
     The words of an article are never touched.
  7. Figures and card thumbnails are found by their data-dir, data-shot and data-trail-img, the
     way assets/shots.js finds them, and every image file they point at that is outside the
     moved tree is copied to the same path (the "dependencies" in the record, each with the
     pages that need it). Without this, 51 figures in 10 articles and the 66 thumbnails on the
     front page at / showed "screenshot unavailable" in v0.6.0 and v0.6.1.
  8. Two version labels are made unambiguous. The edition line's release number is this site's
     own, and an article byline's "site v0.7.36", which names the sgit.ai release the article was
     published in, says "sgit.ai v0.7.36".
  9. The reading meter's top-up link, if admin/build/newsroom-meter.json sets one, is written into
     the meter config of every imported page, on this side only. See that file for what the link is
     and how to switch it off.
  10. Wording this site changes on named pages (admin/build/newsroom-text.json), each a recorded
     rule that stops the import if sgit.ai's text under it moves. The record lists them.
  11. Every page loads this site's own build of the reading meter, v1.4.0, from the API host
     (api.py: https://api.newsroom.sgit.ai/<release>/assets/components/sg-meter/v1/v1.4/v1.4.0/),
     instead of sgit.ai's v1.3.1 that the page names by a relative path.
     v1.4.0 is v1.3.1 without "Pause the meter" and "Start again", and with the view that lets a
     link open the newsroom as a named persona. Only the dynamic import() of the component is
     re-pointed; code samples on the docs page are text and stay as they are. If sgit.ai moves to
     another version, the import stops: v1.4.0 has to be re-based on it deliberately.
  12. Each article carries its number ("No. 65"), small, under "All articles / All graphs", with a link to make a
     reading list starting from it. The numbers are assigned once and never change (admin/build/ids.py,
     articles/ids.json); the import calls it before it writes a page. The line is added to the article's page
     and to its markdown twin, and the import stops if the place it goes is not there exactly once.
  13. Articles written here (admin/content/articles/, published by admin/build/publish.py) name
     this site's release in their byline, "newsroom v0.12.9", linked to this site's release history,
     because this site published them; sgit.ai's generator only rendered them.
  14. The reader code is not imported at all since v0.13.0: the components, assets/subscribe.js and
     every other file of the move live in SGit-AI__Website__Newsroom__API and are served from
     api.newsroom.sgit.ai at a pinned release (admin/build/api.json). A link or a loader on an imported
     page that names one of them (the subscribe page's fetch of subscribe.js, the docs page's links to
     the component files) is re-pointed at that host; the normaliser below reads either form the same.

Scripts, styles and /.well-known/sgit-subscribe.json are copied byte for byte.
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

sys.path.insert(0, str(Path(__file__).parent))
import ids  # noqa: E402

ROOT     = Path(__file__).resolve().parents[2]
HOST     = (ROOT / "CNAME").read_text().strip()               # newsroom.sgit.ai
THIS_VERSION = (ROOT / "admin/build/version.txt").read_text().strip()
sys.path.insert(0, str(Path(__file__).parent))
import api as API  # noqa: E402  (the reader code's host and pinned release: admin/build/api.json, api-manifest.json)

# Settings this site applies to the meter's config on import (admin/build/newsroom-meter.json).
# A live Stripe Payment Link has no underscore in it; a test-mode link is buy.stripe.com/test_...
# and must never reach a public page, so anything else than that shape stops the import.
METER_FILE = ROOT / "admin/build/newsroom-meter.json"
LIVE_LINK  = re.compile(r"^https://buy\.stripe\.com/[A-Za-z0-9]+$")


# The reading meter this site runs (item 11 in the docstring). sgit.ai's pages name METER_BASED_ON; the pages
# written here name METER_OURS. A component path is published and immutable, so a change is a new path.
METER_PATH     = "assets/components/sg-meter/v1/"
METER_BASED_ON = "v1.3/v1.3.1"
METER_OURS     = "v1.4/v1.4.0"
METER_IMPORT   = re.compile(r"(import\(\s*['\"])(?:\./|(?:\.\./)+)?" + re.escape(METER_PATH) + r"(v\d+\.\d+/v\d+\.\d+\.\d+)(/sg-meter\.js)")
# item 14: the subscribe page fetches subscribe.js as text and runs it; it comes from the API host too
SUBSCRIBE_FETCH = re.compile(r"(fetch\(\s*['\"])(?:\./|(?:\.\./)+)?assets/subscribe\.js")

TEXT_FILE = ROOT / "admin/build/newsroom-text.json"
APPLIED = set()


def text_overrides():
    return json.loads(TEXT_FILE.read_text())["overrides"] if TEXT_FILE.exists() else []


def apply_text_overrides(text, dest_file, kind):
    for o in text_overrides():
        if dest_file not in o["files"]:
            continue
        find = o["find"][kind] if isinstance(o["find"], dict) else o["find"]
        n = text.count(find)
        if n != 1:
            sys.exit(f"sync: {dest_file}: the text this site overrides ({o['id']}) is in the page {n} times, "
                     f"not once. sgit.ai changed it, so this rule is stale: update or delete it in "
                     f"admin/build/newsroom-text.json")
        text = text.replace(find, o["with"][kind])
        APPLIED.add((o["id"], dest_file))
    return text


AUTHORED = set()      # slugs of the articles this site wrote itself (item 13), from --authored
NUMBERS = {}          # slug -> article number, filled by main() from admin/build/ids.py
NUMBER_HTML = '<p class="small dim"><a href="index.html">All articles</a> &middot; <a href="graphs.html">All graphs</a></p>'
NUMBER_MD   = "[All articles](index.md) \u00b7 [All graphs](graphs.md)"


def numbered(text, dest_file, kind):
    m = re.fullmatch(r"articles/([^/]+)\.(html|md)", dest_file)
    if not m or m.group(1) not in NUMBERS:
        return text
    n = NUMBERS[m.group(1)]
    anchor = NUMBER_HTML if kind == "html" else NUMBER_MD
    if text.count(anchor) != 1:
        sys.exit(f"sync: {dest_file}: the place an article's number goes is in the page {text.count(anchor)} times, not "
                 f"once. sgit.ai changed the foot of its articles, so this rule is stale (item 12 in the docstring)")
    if kind == "html":
        line = (f'\n <p class="small dim">Article No. {n} &middot; '
                f'<a href="../for/make.html#r={n}">start a reading list with it</a></p>')
    else:
        line = f"\n\nArticle No. {n} \u00b7 [start a reading list with it](https://{HOST}/for/make.html#r={n})"
    return text.replace(anchor, anchor + line)


def own_meter(text, dest_file):
    def swap(m):
        if m.group(2) != METER_BASED_ON:
            sys.exit(f"sync: {dest_file} loads the reading meter at {m.group(2)}, and this site's build "
                     f"({METER_OURS}) is based on {METER_BASED_ON}. sgit.ai moved the component, so re-base "
                     f"{METER_PATH}{METER_OURS}/ on it before importing")
        return m.group(1) + API.api_url(METER_PATH + METER_OURS + "/sg-meter.js")
    out = METER_IMPORT.sub(swap, text)
    if out != text:
        assert METER_PATH + METER_OURS + "/sg-meter.js" in API.served_paths(), f"{METER_OURS} is not in the pinned API release"
    return SUBSCRIBE_FETCH.sub(lambda m: m.group(1) + API.api_url("assets/subscribe.js"), out)


def topup_link():
    link = json.loads(METER_FILE.read_text()).get("topup_link", "") if METER_FILE.exists() else ""
    if link and not LIVE_LINK.match(link):
        sys.exit(f"sync: topup_link {link!r} is not a live Stripe Payment Link (https://buy.stripe.com/<id>); "
                 f"a test-mode link has test_ in it and is refused")
    return link
SRC_HOST = "sgit.ai"
RECORD   = ROOT / "admin/build/newsroom-sync.json"

# The moved tree, from the brief's "What moves" table.
MOVED_DIRS = ["articles", "newsroom", "account", "subscribe", "meter", "og",
              # assets/components left this list in v0.13.0: the reader code is served from the API host (item 14)
              # ...except the frozen meter versions, published artefacts this site keeps serving byte for byte
              # until phase 4 of the move; validate.js check 13 holds them to the API release's bytes
              "assets/components/sg-meter/v1/v1.0", "assets/components/sg-meter/v1/v1.1",
              "assets/components/sg-meter/v1/v1.2", "assets/components/sg-meter/v1/v1.3",
              # Not in the brief's list: a vault page, which stays on sgit.ai as a rule. This one is
              # the study of this site by five synthetic readers, and Dinis asked for it here.
              "demos/vaults/newsroom-synthetic-users",
              # Also not in the brief's list: sgit.ai's page for publishers (11 October), which is about this
              # site, is written to be forwarded, and so belongs at the same address here. Its links to the
              # rest of sgit.ai become absolute, as for every imported page.
              "publishers"]
# Single files: source path -> path here.
MOVED_FILES = {
    "assets/site.css": "assets/newsroom.css",
    "assets/site.js": "assets/site.js",
    "assets/shots.js": "assets/shots.js",
    # "assets/subscribe.js" left this list in v0.13.0: served from the API host (item 14)
    # The live-vault embed on the synthetic-users study page: mounts the official vault viewer in an
    # iframe from dev.vault.sgraph.ai. Loaded by a script that builds the file name at run time,
    # so no static reader of the page finds it. Copied byte for byte like every script here.
    "assets/vault-ui-embed.js": "assets/vault-ui-embed.js",
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

REAL_TAG = re.compile(r"<[a-zA-Z][^<>]*>")
# data-dir and data-trail-img are read by assets/shots.js, which sets img.src from them at runtime
# (sgit.ai's authoring contract forbids a declarative <img src>). They are URLs as much as href is,
# and v0.6.0 and v0.6.1 did not treat them as such: 117 images were missing and nothing said so.
URL_ATTR = re.compile(r'\b(href|src|data-src|action|poster|data-dir|data-trail-img)="([^"]*)"')
FIGURE_TAG = re.compile(r'<figure\b[^>]*\bclass="[^"]*\bshot\b[^"]*"[^>]*>')
TRAIL_TAG  = re.compile(r'<[a-zA-Z][^<>]*\sdata-trail-img="([^"]+)"[^<>]*>')
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
    (re.compile(r'<span>newsroom\.sgit\.ai &middot; v\d+\.\d+\.\d+</span>'),
     '<span>newsroom.sgit.ai &middot; </span>'),
]


def content_sha(data, path):
    if not path.endswith((".html", ".md")):
        return sha(data)
    text = data.decode("utf-8")
    for pattern, repl in NORMALISE:
        text = pattern.sub(repl, text, count=1)
    text = API.normalise(text)       # a reader-file reference, relative or on the API host, reads the same (api.py)
    return sha(text.encode("utf-8"))


# Image files that pages in the moved tree point at but that live outside it, found by
# find_dependencies() before anything is transformed. They are copied to the same path, and a
# link to one stays relative, exactly as if its folder had been in the brief's list.
DEPENDENCY_FILES, DEPENDENCY_DIRS = set(), set()


def register_dependencies(deps):
    DEPENDENCY_FILES.clear(); DEPENDENCY_FILES.update(deps)
    DEPENDENCY_DIRS.clear(); DEPENDENCY_DIRS.update(posixpath.dirname(p) for p in deps)


def moved_target(path):
    """Where a source-site path lives here, or None when it did not move."""
    path = path.lstrip("/")
    if path in DEPENDENCY_FILES or path in DEPENDENCY_DIRS:
        return path
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
    if API.is_reader_path(bare):      # item 14: the reader code is on the API host
        return API.api_url(bare) + (f"?{parts.query}" if parts.query else "") + (f"#{parts.fragment}" if parts.fragment else "")
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
    if API.is_reader_path(path.rstrip("/")):
        return API.api_url(path) + tail[len(path):]
    target = moved_target(path.rstrip("/"))
    if target is None:
        return m.group(0)
    rest = tail[len(path):]
    return f"https://{HOST}/{target}{'/' if path.endswith('/') and target else ''}{rest}"


# The site's NAME, as distinct from its address. An imported page names sgit.ai as its site in
# the tab title, og:title, og:site_name and JSON-LD, which is what a search result or a link
# preview shows. Here the site is the SGit Newsroom. Only these metadata slots change; the
# words of an article never do.
TITLE_SUFFIXES = [(", sgit.ai articles", ", SGit Newsroom"), (", sgit.ai desk", ", SGit Newsroom desk"),
                  (", sgit.ai", ", SGit Newsroom")]
FRONT_TITLE = "SGit Newsroom"
FRONT_DESCRIPTION = "One page, one argument, with the figures, the data and the links to check it."


def rename(title):
    for old, new in TITLE_SUFFIXES:
        if title.endswith(old):
            return title[:-len(old)] + new
    return title


def retitle(text, front):
    # Only the page's own title is replaced on the front page, and JSON-LD is only touched
    # inside its ld+json block. A first version replaced every "name" on the front page, which
    # renamed the reader personas in the meter's config and the author to "SGit Newsroom".
    m = re.search(r'<title>(.*?)</title>', text, re.S)
    own = m.group(1) if m else None

    def slot(m):
        value = m.group(2)
        return m.group(1) + (FRONT_TITLE if front and value == own else rename(value)) + m.group(3)

    def ld(block):
        b = re.sub(r'("(?:name|headline)": ")([^"]*)(")', slot, block.group(0))
        # The article says which site it is part of. It was sgit.ai, with the canonical address
        # already moved here, so a crawler read an article of newsroom.sgit.ai as part of sgit.ai.
        b = b.replace('"isPartOf": {"@type": "WebSite", "name": "sgit.ai", "url": "https://sgit.ai"}',
                      f'"isPartOf": {{"@type": "WebSite", "name": "SGit Newsroom", "url": "https://{HOST}"}}')
        if front:
            b = re.sub(r'("description": ")[^"]*(")', rf'\1{FRONT_DESCRIPTION}\2', b, count=1)
        return b

    text = re.sub(r'(<title>)(.*?)(</title>)', slot, text, count=1, flags=re.S)
    text = re.sub(r'(<meta (?:property="og:title"|name="twitter:title"|property="og:image:alt") content=")([^"]*)(")',
                  slot, text)
    text = re.sub(r'(<meta property="og:site_name" content=")sgit\.ai(")', r'\1SGit Newsroom\2', text)
    # The meter records the page's title in the reader's reading history, kept in their browser.
    text = re.sub(r'(<sg-meter\b[^>]*\btitle=")([^"]*)(")', slot, text)
    text = re.sub(r'<script type="application/ld\+json">.*?</script>', ld, text, flags=re.S)
    if front:
        text = re.sub(r'(<meta (?:name="description"|property="og:description") content=")[^"]*(")',
                      rf'\1{FRONT_DESCRIPTION}\2', text)
    return text


def attr(tag, name):
    m = re.search(rf'\s{name}="([^"]*)"', tag)
    return m.group(1) if m else None


def image_refs(src_file, text):
    """Source-site paths of every figure and card thumbnail on a page, resolved the way
    assets/shots.js resolves them: relative to the page, with data-dir defaulting to images/."""
    out = []
    for m in FIGURE_TAG.finditer(text):
        shot, base = attr(m.group(0), "data-shot"), attr(m.group(0), "data-dir")
        base = "images/" if base is None else base
        if not shot or re.match(r"^([a-z]+:)?//|^[a-z]+:", base + shot):
            continue
        out.append(posixpath.normpath(posixpath.join(posixpath.dirname(src_file), base, shot)))
    for m in TRAIL_TAG.finditer(text):
        if re.match(r"^([a-z]+:)?//|^data:|^https?:", m.group(1)):
            continue
        out.append(posixpath.normpath(posixpath.join(posixpath.dirname(src_file), m.group(1))))
    return [p for p in out if not p.startswith("..")]


def find_dependencies(src, pages):
    """Image files the moved pages point at that are not in the moved tree, and the references
    that resolve to nothing even on sgit.ai (a bug there, reported here and not hidden)."""
    deps, unresolved = {}, {}
    for s, d in pages:
        if not s.endswith(".html"):
            continue
        for target in image_refs(s, (src / s).read_text(encoding="utf-8")):
            if not (src / target).is_file():
                unresolved.setdefault(target, set()).add(d)
            elif moved_target(target) is None:
                deps.setdefault(target, set()).add(d)
    return deps, unresolved


def transform(text, src_file, dest_file, kind):
    text = ABS_SRC.sub(rewrite_abs, text)
    if kind == "html":
        # Attributes of real tags only. A code sample on a page is escaped (&lt;script src="/x"&gt;)
        # and is something a reader copies; rewriting the attribute-shaped text inside it changed
        # SG Meter's install instructions on the first run of this script.
        text = REAL_TAG.sub(
            lambda t: URL_ATTR.sub(lambda m: f'{m.group(1)}="{rewrite_url(m.group(2), src_file, dest_file)}"',
                                   t.group(0)), text)
        depth = dest_file.count("/")
        text = re.sub(r'(<html[^>]*\bdata-root=")[^"]*(")', lambda m: m.group(1) + "../" * depth + m.group(2), text, count=1)
        # The page loader: sgit.ai's stylesheet has a different name here and its site chat
        # does not come across. Its freshness check is deliberately left naming sgit.ai, so
        # it does nothing here: the page carries sgit.ai's release number, and comparing that
        # with this site's would reload every page against the wrong version.
        text = text.replace("'assets/site.css'", "'assets/newsroom.css'")
        text = text.replace("js(sg,'assets/site-chat.js');", "")
        # The edition line's last item named the sgit.ai release that built the page. Here it names
        # this site's own release, the one in the nav and the footer, restamped by chrome.py: five
        # readers counted three version numbers for one site, and "edition from sgit.ai v0.7.39"
        # was one of them, added by this script in v0.6.0.
        text = re.sub(r'<span>sgit\.ai &middot; v\d+\.\d+\.\d+</span>',
                      f'<span>{HOST} &middot; {THIS_VERSION}</span>', text)
        # A byline's "site v0.7.36" is the sgit.ai release the article was published in, and links
        # to sgit.ai's release history. On sgit.ai "site" meant the site you were reading; here it
        # means somebody else's, so the label says whose.
        m_own = re.fullmatch(r"articles/([^/]+)\.html", dest_file)
        if m_own and m_own.group(1) in AUTHORED:
            text = re.sub(r'<a href="https://sgit\.ai/admin/versions\.html" title="The site release'
                          r' it was published in">site (v\d+\.\d+\.\d+)</a>',
                          r'<a href="../admin/versions.html" title="The newsroom release it was published in">newsroom \1</a>',
                          text)
        text = re.sub(r'(<a href="https://sgit\.ai/admin/versions\.html" title=")The site release'
                      r'( it was published in">)site (v\d+\.\d+\.\d+</a>)',
                      r'\1The sgit.ai release\2sgit.ai \3', text)
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
        # The top-up link is this site's own: sgit.ai keeps the simulated cart, and a link that
        # returns to newsroom.sgit.ai must only be on pages served from newsroom.sgit.ai, because a
        # reader's credit lives in the browser storage of the origin they return to.
        text = own_meter(text, dest_file)
        link = topup_link()
        if link:
            text = re.sub(r'("topup": \{"amount": \d+, "link": )""', lambda m: m.group(1) + json.dumps(link), text)
        text = retitle(text, front=(src_file == "articles/index.html"))
        if src_file == "articles/index.html":
            # One front page at two addresses names one canonical address: the root.
            text = re.sub(r'(<link rel="canonical" href=")[^"]*(")', rf'\1https://{HOST}/\2', text, count=1)
            text = re.sub(r'(<meta property="og:url" content=")[^"]*(")', rf'\1https://{HOST}/\2', text, count=1)
        text = numbered(text, dest_file, "html")
        text = apply_text_overrides(text, dest_file, "html")
    elif kind == "md":
        text = MD_LINK.sub(lambda m: m.group(1) + rewrite_url(m.group(2), src_file, dest_file) + m.group(3), text)
        m_own = re.fullmatch(r"articles/([^/]+)\.md", dest_file)
        if m_own and m_own.group(1) in AUTHORED:
            text = re.sub(r'\[site (v\d+\.\d+\.\d+)\]\(https://sgit\.ai/admin/versions\.md\)',
                          rf'[newsroom \1](https://{HOST}/admin/versions.html)', text)
        text = re.sub(r'\[site (v\d+\.\d+\.\d+)\]\((https://sgit\.ai/admin/versions\.md)\)',
                      r'[sgit.ai \1](\2)', text)
        # The same ambiguity in the line every twin opens with: "site v0.7.40" is the sgit.ai release
        # that generated the file, not this site's. (index.md gets this site's own stamp appended.)
        text = re.sub(r'\u00b7 site (v\d+\.\d+\.\d+) \u00b7 this file is generated',
                      lambda m: f'\u00b7 sgit.ai {m.group(1)} \u00b7 this file is generated', text)
        text = numbered(text, dest_file, "md")
        text = apply_text_overrides(text, dest_file, "md")
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
    ap.add_argument("--authored", default="", help="comma-separated slugs of articles written here (publish.py)")
    ap.add_argument("--source-meta", help="a JSON file that replaces the record's source (publish.py)")
    args = ap.parse_args()
    AUTHORED.update(x for x in args.authored.split(",") if x)
    src = Path(args.src).resolve()
    if not (src / "articles/index.html").exists() or not (src / "admin/build/build_pages.py").exists():
        sys.exit(f"sync: {src} is not a checkout of the sgit.ai website")

    NUMBERS.update(ids.assign(src))
    previous = json.loads(RECORD.read_text())["files"] if RECORD.exists() else {}
    files, problems = {}, []
    moved = plan(src)
    # Before anything is transformed: which image files do the moved pages point at that are not
    # in the moved tree? They are copied, so a link to one can stay relative.
    deps, unresolved = find_dependencies(src, moved)
    register_dependencies(deps)
    for s, d in moved + [(t, t) for t in sorted(deps)]:
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
        if s in deps:
            files[d]["needed_by"] = sorted(deps[s])

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

    for o in text_overrides():
        missed = [f for f in o["files"] if (o["id"], f) not in APPLIED]
        if missed:
            sys.exit(f"sync: the text rule {o['id']} names files it did not reach: {missed}")
    for target, pages in sorted(unresolved.items()):
        print(f"  ! sgit.ai itself points at {target} and the file is not there ({len(pages)} page(s)); "
              f"it fails there too, and is not fixed here", file=sys.stderr)
    changed = [d for d, f in files.items()
               if not (ROOT / d).exists() or content_sha((ROOT / d).read_bytes(), d) != f["sha256"]]
    if args.check:
        print(f"sync --check: {len(changed)} file(s) would change, {len(stale)} would be removed")
        for d in changed:
            print(f"  ~ {d}")
        for d in stale:
            print(f"  - {d}")
        return

    for d in changed:
        p = ROOT / d
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(files[d]["_out"])
    for d in stale:
        (ROOT / d).unlink(missing_ok=True)

    meta = json.loads(Path(args.source_meta).read_text()) if args.source_meta else source_meta(src)
    record = {
        "what": "The SGit Newsroom, imported from sgit.ai's built pages at the same paths. "
                "Written by admin/build/sync_newsroom.py; do not edit the imported files by hand.",
        "sha256": "sha256_source is the file as sgit.ai serves it. sha256 is the file as imported, "
                  "with the site nav, the site footer, the agent-chip stamp and the index.md version "
                  "line emptied, because chrome.py restamps those on every release. validate.js "
                  "check 11 recomputes it for every file listed here.",
        "source": meta,
        "host": HOST,
        "text_overrides": [{"id": o["id"], "files": o["files"], "why": o["why"]} for o in text_overrides()],
        "counts": {
            "files": len(files),
            "pages": sum(1 for d in files if d.endswith(".html")),
            "articles": sum(1 for d in files if re.fullmatch(r"articles/[^/]+\.html", d)
                            and d not in ("articles/index.html", "articles/graphs.html")),
            "verbatim": sum(1 for f in files.values() if f["sha256"] == f["sha256_source"]),
            "dependencies": len(deps),
            "text_overrides": len(text_overrides()),
            "unresolved_on_sgit_ai": len(unresolved),
        },
        "files": {d: {k: v for k, v in f.items() if k != "_out"} for d, f in sorted(files.items())},
    }
    RECORD.write_text(json.dumps(record, indent=1, ensure_ascii=False) + "\n")
    c = record["counts"]
    print(f"sync: sgit.ai {meta['version']} ({meta['commit'][:7]}) -> {HOST}: "
          f"{c['files']} files, {c['pages']} pages, {c['articles']} articles; "
          f"{c['dependencies']} dependency images; "
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
