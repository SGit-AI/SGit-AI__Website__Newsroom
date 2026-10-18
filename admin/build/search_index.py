#!/usr/bin/env python3
"""Search: the index the browser searches, built from the pages this site publishes, and the page that searches it.

    python3 admin/build/search_index.py

There is no search server. At release time this script reads every page in sitemap.xml (its <main>, as published),
the article feed (articles/graphs.json: topics, tags, teasers), each article's graph (articles/graphs/<slug>.json: the
core idea and the node labels), the earlier versions of each article (only the paragraphs that are no longer in the
current one), the wire's snapshot (wire/snapshot.json) and this site's own notes (admin/notes/*.md), and writes:

    search/docs.json   one entry per page: address, title, kind, number, date, topics, tags, teaser, graph labels,
                       headings with their anchors; small, loaded first, enough to search titles and tags at once
    search/text.json   the text, in paragraphs, each with its page, the anchor of the section it is in, and the version
                       it comes from when it is no longer in the current article; loaded after, for full-text search
    search/index.html  the page; assets/search/search.js ranks in the browser (BM25 over fields and paragraphs)

Nothing is sent anywhere when a reader searches: the files are fetched from this site like any page and the ranking
runs in the page. The design: admin/notes/2026-10-13__search-in-the-browser.md.
"""
import html as htmlmod
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from page import newsroom_page, write, HOST  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
SKIP_PREFIX = ("search/", "og/", "assets/", "404")
SKIP_CLASSES = {"crumb", "lkit", "athreads", "athreads areviews", "aseries", "aseries-all", "agent", "small dim", "subteaser", "meter-card", "sgm", "note-archive", "archive-note"}
BLOCK = {"p", "li", "blockquote", "figcaption", "dd", "dt", "td", "th", "pre"}
MAX_WORDS = 160


class MainText(HTMLParser):
    """The text of <main>: the h1, the headings with their ids, and the paragraphs under each, skipping chrome."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_main = 0
        self.skip = 0           # depth inside a skipped element
        self.stack = []         # open tags inside main, with whether each started a skip
        self.h1 = ""
        self.heads = []         # (anchor, text, level)
        self.blocks = []        # (anchor, text)
        self.anchor = ""
        self.cur = None         # [tag, parts] for an open heading or block
        self.desc = ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "meta" and a.get("name") == "description":
            self.desc = a.get("content") or ""
        if tag == "main":
            self.in_main += 1
            return
        if not self.in_main:
            return
        if tag in ("br", "img", "hr", "input", "meta", "link", "source", "wbr"):
            return
        cls = a.get("class", "") or ""
        starts_skip = self.skip > 0 or tag in ("script", "style", "nav", "button", "svg", "form", "select", "textarea") or cls in SKIP_CLASSES or any(c in SKIP_CLASSES for c in cls.split())
        if starts_skip:
            self.skip += 1
        self.stack.append((tag, starts_skip))
        if self.skip:
            return
        if tag in ("h1", "h2", "h3", "h4"):
            self.cur = [tag, [], a.get("id", "")]
        elif tag in BLOCK and self.cur is None:
            self.cur = [tag, [], ""]
        elif a.get("id") and tag in ("section", "div", "article", "details"):
            self.anchor = a["id"]

    def handle_endtag(self, tag):
        if tag == "main":
            self.in_main = max(0, self.in_main - 1)
            return
        if not self.in_main or tag in ("br", "img", "hr", "input", "meta", "link", "source", "wbr"):
            return
        while self.stack:
            t, sk = self.stack.pop()
            if sk:
                self.skip -= 1
            if t == tag:
                break
        if self.cur and self.cur[0] == tag and not self.skip:
            text = re.sub(r"\s+", " ", "".join(self.cur[1])).strip()
            if tag == "h1":
                self.h1 = self.h1 or text
            elif tag in ("h2", "h3", "h4"):
                if self.cur[2]:
                    self.anchor = self.cur[2]
                if text:
                    self.heads.append((self.cur[2] or self.anchor, text, int(tag[1])))
            elif text:
                self.blocks.append((self.anchor, text))
            self.cur = None

    def handle_data(self, data):
        if self.in_main and not self.skip and self.cur is not None:
            self.cur[1].append(data)


class VersionDiff(HTMLParser):
    """A version page is a diff from the version before: for each changed or removed paragraph, the text as it read
    before (deletions kept, insertions dropped), with the section it was under."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_p = False
        self.ins = 0
        self.parts = []
        self.anchor = ""
        self.cls = ""
        self.out = []           # (anchor, text before)
        self.frm = ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "p" and (a.get("class") or "") in ("changed", "removed"):
            self.in_p, self.parts, self.cls = True, [], a.get("class")
        elif tag == "p" and (a.get("class") or "") == "diff-same":
            self.in_p, self.parts, self.cls = True, [], "same"
        elif tag == "ins" and self.in_p:
            self.ins += 1

    def handle_endtag(self, tag):
        if tag == "ins" and self.ins:
            self.ins -= 1
        elif tag == "p" and self.in_p:
            text = re.sub(r"\s+", " ", "".join(self.parts)).strip()
            if self.cls == "same":
                ids = re.findall(r"\{#([\w-]+)\}", text)
                if ids:
                    self.anchor = ids[-1]
            elif text:
                self.out.append((self.anchor, text))
            self.in_p = False

    def handle_data(self, data):
        if self.in_p and not self.ins:
            self.parts.append(data)


def version_before(path):
    """(the version the diff starts from, [(anchor, text as it read before)])."""
    v = VersionDiff()
    raw = path.read_text(encoding="utf-8", errors="replace")
    v.feed(raw)
    m = re.search(r"From (v\d+\.\d+\.\d+)", raw)
    return (m.group(1) if m else ""), v.out


def parse(path):
    p = MainText()
    p.feed(path.read_text(encoding="utf-8", errors="replace"))
    title = p.h1
    if not title:
        m = re.search(r"<title>(.*?)</title>", path.read_text(encoding="utf-8", errors="replace"), re.S)
        title = htmlmod.unescape(m.group(1)).strip() if m else path.stem
    return title, p.desc, p.heads, p.blocks


def chunks_of(blocks):
    """Paragraphs merged within a section up to MAX_WORDS, so a one-line paragraph does not stand alone."""
    out, cur_a, cur = [], None, []
    for anchor, text in blocks:
        words = len(text.split())
        if cur and (anchor != cur_a or sum(len(t.split()) for t in cur) + words > MAX_WORDS):
            out.append((cur_a, " ".join(cur)))
            cur = []
        cur_a = anchor
        cur.append(text)
        if words >= MAX_WORDS:
            out.append((cur_a, " ".join(cur)))
            cur = []
    if cur:
        out.append((cur_a, " ".join(cur)))
    return out


def norm(t):
    return re.sub(r"\s+", " ", re.sub(r"[^\w]+", " ", t.lower())).strip()


def kind_of(rel, slugs):
    if rel.startswith("articles/"):
        name = rel[len("articles/"):]
        if name.endswith(".html") and "/" not in name and name[:-5] in slugs:
            return "article"
        for pre, k in (("newsletter/", "newsletter"), ("desk/", "desk"), ("collections/", "collection"), ("views/", "view"), ("decks/", "deck"), ("versions/", "version")):
            if name.startswith(pre):
                return k
        return "page"
    for pre, k in (("wire/", "wire"), ("engineering/", "engineering"), ("archive/", "archive"), ("admin/", "admin"), ("passkey/", "lab"), ("vault/", "vault"), ("account/", "account"), ("newsroom/", "newsroom")):
        if rel.startswith(pre):
            return k
    return "page"


def site_pages():
    xml = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    for loc in re.findall(r"<loc>(.*?)</loc>", xml):
        rel = re.sub(r"^https?://[^/]+/", "", loc)
        rel = rel + "index.html" if (not rel or rel.endswith("/")) else rel
        if rel.startswith(SKIP_PREFIX) or not rel.endswith(".html"):
            continue
        if (ROOT / rel).exists():
            yield rel


def build():
    feed = json.loads((ROOT / "articles/graphs.json").read_text(encoding="utf-8"))
    by_slug = {a["slug"]: a for a in feed["articles"]}
    ids = {a["slug"]: a["n"] for a in json.loads((ROOT / "articles/ids.json").read_text(encoding="utf-8"))["articles"]}
    docs, text = [], []
    current_paras = {}

    def add_doc(d, blocks, extra_chunks=()):
        i = len(docs)
        d["i"] = i
        docs.append(d)
        for anchor, t in chunks_of(blocks):
            text.append([i, anchor or "", t])
        for anchor, t, ver in extra_chunks:
            text.append([i, anchor or "", t, ver[0], ver[1]])     # [doc, anchor, text, version, the page that shows the change]
        return i

    for rel in site_pages():
        k = kind_of(rel, by_slug)
        if k == "version":
            continue                                    # versions are folded into their article, below
        title, desc, heads, blocks = parse(ROOT / rel)
        d = {"u": rel, "t": title, "k": k, "x": desc[:300], "h": [[a, h] for a, h, lvl in heads if a][:40]}
        if k == "article":
            slug = rel[len("articles/"):-5]
            a = by_slug.get(slug, {})
            g = {}
            try:
                g = json.loads((ROOT / f"articles/graphs/{slug}.json").read_text(encoding="utf-8"))
            except (OSError, ValueError):
                g = {}
            d.update({"n": ids.get(slug), "d": a.get("date", ""), "x": a.get("teaser") or desc[:300], "tp": a.get("topics", []), "tg": a.get("tags", []),
                      "g": " · ".join([g.get("core_idea", "")] + [nd.get("label", "") for nd in g.get("nodes", [])])[:1500]})
            current_paras[slug] = {norm(t) for _, t in blocks}
            # the earlier versions: each version page is a diff; what a changed or removed paragraph said before,
            # when it is no longer in the article, is kept with the version it read that way in and the page that shows the change
            extra, seen = [], set()
            vdir = ROOT / "articles/versions" / slug
            for vf in sorted(vdir.glob("v*.html")) if vdir.is_dir() else []:
                frm, before = version_before(vf)
                for anchor, t in before:
                    n = norm(t)
                    if len(n.split()) < 6 or n in current_paras[slug] or n in seen:
                        continue
                    seen.add(n)
                    extra.append((anchor, t, [frm or vf.stem, f"articles/versions/{slug}/{vf.name}"]))
            add_doc(d, blocks, extra)
        else:
            add_doc(d, blocks)

    # the wires' stories, from the snapshots this site keeps (the live editions are in the vaults): wire/snapshot.json and wire/<slug>/snapshot.json
    for snap in sorted([ROOT / "wire/snapshot.json"] + list((ROOT / "wire").glob("*/snapshot.json"))):
        if not snap.exists():
            continue
        s = json.loads(snap.read_text(encoding="utf-8"))
        page = snap.parent.relative_to(ROOT).as_posix() + "/index.html"
        wname = (s.get("wire") or {}).get("title") or "The Industry Wire"
        for b in s.get("beats", []):
            for st in b.get("stories", []):
                add_doc({"u": f"{page}#{st['id']}", "t": st["headline"], "k": "story", "d": st.get("date", ""),
                         "x": f"{b.get('label', '')} · {st.get('publisher', '')} · {wname}, edition of {s.get('edition', '')}", "tg": [b.get("id", "")]},
                        [(st["id"], f"{c.get('at', '')}: {c['what']}") for c in st.get("changes", []) if c.get("what")]       # a correction is searchable text at the story
                        + ([(st["id"], st["headline_pt"])] if st.get("headline_pt") else []))                                     # and a headline in the wire's other language

    # this site's own notes, which are markdown only
    for md in sorted((ROOT / "admin/notes").glob("*.md")):
        raw = md.read_text(encoding="utf-8")
        title = (re.search(r"^#\s+(.*)$", raw, re.M) or [None, md.stem])[1]
        blocks, anchor = [], ""
        for para in re.split(r"\n\s*\n", raw):
            para = para.strip()
            m = re.match(r"^(#{2,4})\s+(.*)$", para)
            if m:
                anchor = re.sub(r"[^a-z0-9]+", "-", m.group(2).lower()).strip("-")[:60]
                continue
            if para.startswith("#") or para.startswith("```") or para.startswith("|"):
                continue
            t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", para)
            t = re.sub(r"[*_`>]", "", t)
            blocks.append((anchor, re.sub(r"\s+", " ", t)))
        add_doc({"u": f"admin/notes/{md.name}", "t": title.strip(), "k": "note", "d": md.name[:10], "x": "", "h": []}, blocks)

    version = (ROOT / "admin/build/version.txt").read_text().strip()
    meta = {"v": 1, "site": HOST, "release": version, "docs": len(docs), "chunks": len(text),
            "what": "The search index of newsroom.sgit.ai, built at release time from the published pages; ranked in the reader's browser."}
    return meta, docs, text


def page(meta):
    body = """<div id="search-mount" class="search">
<form class="search-box" role="search" action="index.html" method="get">
  <label for="search-q" class="sr">Search the newsroom</label>
  <input id="search-q" name="q" type="search" autocomplete="off" spellcheck="false" placeholder="Search articles, the wire, notes: words, &quot;a phrase&quot;, or an article number">
  <button type="submit" class="btn primary">Search</button>
</form>
<div class="search-filters" id="search-filters" role="group" aria-label="Show"></div>
<p class="search-status dim" id="search-status">Loading the index&hellip;</p>
<ol class="search-results" id="search-results"></ol>
</div>
<noscript><p>Search runs in your browser, which needs a script. The index is <a href="docs.json">docs.json</a> and <a href="text.json">text.json</a>; every page also has a <code>.md</code> twin, and <a href="../llms.txt">llms.txt</a> maps the site.</p></noscript>
<script type="module">
import { mountSearch } from '../assets/search/search.js';
import { mountAsk } from '../assets/search/ask.js';
const el = document.getElementById('search-mount');
mountSearch(el); mountAsk(el);
</script>
<h2 id="how">How it works</h2>
<p>There is no search server. When this site is released, a script reads every page it publishes, each article&rsquo;s graph and tags, the earlier versions of each article, the wire&rsquo;s headlines and the site&rsquo;s own notes, and writes two files: <a href="docs.json">docs.json</a>, one entry per page with its title, tags, graph and headings, and <a href="text.json">text.json</a>, the text in paragraphs. This page fetches them like any other file and ranks them here, in your browser: a title, a tag or a node of an article&rsquo;s graph counts for more than a word in the text. Searching sends nothing anywhere. Quotes find an exact phrase; a number on its own finds that article; a sentence that has since been changed is found in the earlier version it is from. Pages you have read, and pages you marked done, say so, from your own records. <a href="../admin/notes/2026-10-13__search-in-the-browser.md">The design</a>.</p>
<h2 id="ask">Asking</h2>
<p><i>Ask</i> searches the question the same way, takes the best paragraph of each of the top pages (up to eight, the current wording only), numbers them and gives them to a model with one instruction: answer only from them, cite them by number, and say so when they do not hold the answer. The answer comes with the passages under it, each linked to its page and section, so every claim can be checked where it came from; <i>What the model is given</i> shows exactly what was sent.</p>
<p>The model is <b>Chrome&rsquo;s built-in model</b> when your browser has it (the Prompt API): it runs on your machine, with no key, and nothing is sent anywhere. Otherwise it is <b>your own OpenRouter key</b>, pasted under <i>How questions are answered</i>: kept in this tab unless you ask to keep it in this browser, sent to openrouter.ai with the question and the passages, and nowhere else; this site has no server to send it to. With neither, <i>Ask</i> shows the passages alone. A question can be a link: <code>?q=&hellip;&amp;ask=1</code> asks on arrival.</p>
"""
    agent = (f"Search on newsroom.sgit.ai runs in the reader's browser. The index is https://{HOST}/search/docs.json (one entry per page: u address, t title, k kind, n article number, "
             "d date, x teaser, tp topics, tg tags, g the article graph's core idea and node labels, h headings with anchors) and https://" + HOST + "/search/text.json "
             "(paragraphs: [doc index, anchor, text] and, for text that is only in an earlier version of an article, [doc index, anchor, text, version, the version page that shows the change]). Built at release time by admin/build/search_index.py from the published pages; "
             f"{meta['docs']} documents and {meta['chunks']} paragraphs at {meta['release']}. An agent can fetch the two files and rank them itself, or read /llms.txt and the .md twins. Ask on the page (assets/search/ask.js) gives a model the top passages, numbered, with the instruction to answer only from them and cite them: Chrome's built-in model (LanguageModel) on the reader's machine, or the reader's own OpenRouter key, sent to openrouter.ai only.")
    return newsroom_page("search/index.html", "Search",
                         "Search every article, the wire's stories and the site's notes, in your browser: titles, tags, article graphs and full text, with exact phrases and earlier versions; and ask a question, answered from the passages found by Chrome's built-in model or your own OpenRouter key.",
                         body, eyebrow="Search · in your browser", lead="Every article, the wire and the notes, searched in your browser; and asked, with Chrome’s built-in model or your own OpenRouter key, answered from the passages found.",
                         agent=agent, head='<link rel="stylesheet" href="../assets/search/search.css"><link rel="stylesheet" href="../assets/search/ask.css">', wide=True)


def main():
    meta, docs, text = build()
    changed = []
    dj = json.dumps({**meta, "docs": docs}, ensure_ascii=False, separators=(",", ":")) + "\n"
    tj = json.dumps({"v": 1, "release": meta["release"], "chunks": text}, ensure_ascii=False, separators=(",", ":")) + "\n"
    if write("search/docs.json", dj):
        changed.append("search/docs.json")
    if write("search/text.json", tj):
        changed.append("search/text.json")
    if write("search/index.html", page(meta)):
        changed.append("search/index.html")
    kinds = {}
    for d in docs:
        kinds[d["k"]] = kinds.get(d["k"], 0) + 1
    print(f"search: {meta['docs']} documents ({', '.join(f'{v} {k}' for k, v in sorted(kinds.items(), key=lambda x: -x[1]))}), {meta['chunks']} paragraphs; "
          f"docs.json {len(dj.encode()) // 1024} KB, text.json {len(tj.encode()) // 1024} KB; {len(changed)} written")


if __name__ == "__main__":
    main()
