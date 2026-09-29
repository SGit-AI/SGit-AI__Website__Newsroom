#!/usr/bin/env python3
"""The news strip on the front page: what changed here lately.

    python3 admin/build/gen_news.py

Derived from admin/versions.html, which is the release record, so the front page cannot
claim an update that did not ship. Every entry is a version, its date and its headline —
the first bold sentence of the release note, which is written to be that headline.

Why this exists: the front page described a design for months while four sections quietly
started running. A reader arriving cold had no way to see that the site moves, or how
recently. A release record nobody is shown is a changelog; a release record on the front
page is news.
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
N = 6
START = "<!-- NEWS:START -->"
END = "<!-- NEWS:END -->"


def releases():
    t = (ROOT / "admin/versions.html").read_text(encoding="utf-8")
    out = []
    for m in re.finditer(
            r'<td class="vnum">(v[\d.]+)</td>\s*<td>([^<]+)</td>\s*<td><b>(.*?)</b>', t, re.S):
        # Strip tags: a release headline in versions.html carries links that are relative to
        # /admin/, and pasting them into a page at the site root broke every one of them.
        # A headline is text; the card links to the release note.
        head = " ".join(re.sub(r"<[^>]+>", "", m.group(3)).split())
        ver, date = m.group(1), m.group(2).strip()
        out.append((ver, date, head))
        if len(out) >= N:
            break
    return out


def block(rows):
    items = "".join(
        f'<a class="card" href="admin/versions.html#{html.escape(v)}">'
        f'<span class="tag">{html.escape(v)} &middot; {html.escape(d)}</span>'
        f'<p style="margin-top:.4rem;color:#34363c">{h}</p></a>'
        for v, d, h in rows)
    return (
        f'{START}\n'
        '<section class="band" id="news" style="padding-top:2.2rem;padding-bottom:2.2rem">\n'
        '  <h2>What changed lately</h2>\n'
        '  <p class="blurb">This site ships most days, and every release is tagged, gated and '
        'recorded. The newest six:</p>\n'
        f'  <div class="cards">{items}</div>\n'
        '  <p class="inner" style="text-align:center;margin-top:1.2rem">'
        '<a href="admin/versions.html">The full release history &rarr;</a></p>\n'
        '</section>\n'
        f'{END}')


def main():
    rows = releases()
    if not rows:
        raise SystemExit("gen_news: no releases parsed from admin/versions.html")
    f = ROOT / "index.html"
    t = f.read_text(encoding="utf-8")
    new = block(rows)
    if START in t and END in t:
        t = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: new, t, flags=re.S)
    else:
        anchor = '<section class="band alt" id="runs">'
        if anchor not in t:
            raise SystemExit("gen_news: cannot find where to put the news section")
        t = t.replace(anchor, new + "\n\n" + anchor, 1)
    f.write_text(t, encoding="utf-8")

    md = ROOT / "index.md"
    m = md.read_text(encoding="utf-8")
    lines = "\n".join(f"- **{v}** ({d}) — {re.sub(r'<[^>]+>', '', h)}" for v, d, h in rows)
    sec = f"## What changed lately\n\n{lines}\n\n[The full release history →](https://newsroom.sgit.ai/admin/versions.html)\n"
    if "## What changed lately" in m:
        m = re.sub(r"## What changed lately\n.*?(?=\n## )", sec + "\n", m, flags=re.S)
    else:
        m = m.replace("## What runs on this site", sec + "\n## What runs on this site", 1)
    md.write_text(m, encoding="utf-8")
    print(f"news: {len(rows)} releases, newest {rows[0][0]}")


if __name__ == "__main__":
    main()
