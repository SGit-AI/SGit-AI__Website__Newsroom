#!/usr/bin/env python3
"""Review drafts: an article the editor has not approved yet, served at a page nothing links to.

    python3 admin/build/drafts.py            write drafts/<slug>.html from admin/content/drafts/<slug>.md
    python3 admin/build/drafts.py --check    list what it would write, write nothing

An article in admin/content/articles/ goes through sgit.ai's generator, and the newest one leads the front
page, so a draft cannot wait there. A draft lives in admin/content/drafts/ instead, with the same front
matter (title, date, author, summary) and `status: review`. This writes it as drafts/<slug>.html with the
newsroom's chrome and `noindex, nofollow`: it is in git and at a stable address to send to a reviewer, it is
not on the home page, the article list, the feeds or the site's search (search_index.py skips drafts/), and
search engines are asked not to index it. Its figures are in drafts/images/. The sitemap lists it, because
validate.js wants every page there.

The markdown is the subset the drafts use: `## Heading {#id}`, paragraphs, `- ` and `1. ` lists, `> ` notes,
pipe tables, **bold**, `code`, [links](url), and the articles' `!shot file | images/ | caption | kind` line.
When the editor approves a draft, it moves to admin/content/articles/ with `status: published`, gets its
summaries and graph, and its figures move to admin/content/articles/images/; delete the draft and its page.
"""
import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from page import newsroom_page, write  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "admin/content/drafts"
ROBOTS = '<meta name="robots" content="noindex, nofollow">\n'


def front_matter(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    fm = dict(re.findall(r"^(\w+): (.*)$", m.group(1), re.M))
    return fm, text[m.end():]


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    return re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", lambda m: f'<a href="{html.escape(m.group(2))}">{m.group(1)}</a>', s)


def shot(line):
    file, folder, caption = [p.strip() for p in line[len("!shot "):].split("|")[:3]]
    return (f'<figure class="shot shot--in"><img src="{folder}{file}" alt="{html.escape(caption)}" loading="lazy">'
            f'<figcaption>{inline(caption)}</figcaption></figure>')


def render(md):
    out, para, items, kind = [], [], [], None

    def flush():
        nonlocal para, items, kind
        if para:
            out.append(f"<p>{inline(' '.join(para))}</p>")
        if items:
            out.append(f"<{kind}>" + "".join(f"<li>{inline(i)}</li>" for i in items) + f"</{kind}>")
        para, items, kind = [], [], None

    lines = md.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if not line:
            flush()
        elif line.startswith("## "):
            flush()
            m = re.match(r"## (.*?)(?: \{#([a-z0-9-]+)\})?$", line)
            out.append(f'<h2 id="{m.group(2)}">{inline(m.group(1))}</h2>' if m.group(2) else f"<h2>{inline(m.group(1))}</h2>")
        elif line.startswith("!shot "):
            flush()
            out.append(shot(line))
        elif line.startswith("> "):
            flush()
            out.append(f'<blockquote><p>{inline(line[2:])}</p></blockquote>')
        elif line.startswith("| "):
            flush()
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            head, body = rows[0], [r for r in rows[2:]]
            out.append("<table><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>"
                       + "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in body) + "</tbody></table>")
            continue
        elif re.match(r"(- |\d+\. )", line):
            k = "ul" if line.startswith("- ") else "ol"
            if para or (kind and kind != k):
                flush()
            kind = k
            items.append(re.sub(r"^(- |\d+\. )", "", line))
        elif items:
            items[-1] += " " + line.strip()
        else:
            para.append(line.strip())
        i += 1
    flush()
    return "\n".join(out)


def main(check=False):
    written = []
    for src in sorted(SRC.glob("*.md")):
        fm, md = front_matter(src.read_text(encoding="utf-8"))
        slug = fm.get("slug") or src.stem
        rel = f"drafts/{slug}.html"
        body = render(md)
        agent = (f"A review draft by {html.escape(fm.get('author', 'the editor'))}, not yet approved: it is not linked from the home "
                 f"page or the article list and asks not to be indexed. Its source is admin/content/drafts/{src.name}; "
                 "when it is approved it becomes an article at /articles/.")
        page = newsroom_page(rel, fm["title"], fm.get("summary", ""), body, eyebrow=f"Review draft &middot; {html.escape(fm.get('date', ''))}",
                             crumbs=(), agent=agent, head=ROBOTS)
        if check:
            written.append(rel)
        elif write(rel, page):
            written.append(rel)
    print(f"drafts: {len(list(SRC.glob('*.md')))} draft(s), {len(written)} written {written}")


if __name__ == "__main__":
    main("--check" in sys.argv)
