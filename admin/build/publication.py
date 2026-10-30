#!/usr/bin/env python3
"""The publication's own pages: the imprint, the editorial standards, corrections, withdrawals and complaints.

    python3 admin/build/publication.py

Each page is a markdown file in admin/content/publication/ with front matter (slug, title, description,
eyebrow, agent) and is written to about/<slug>.html in the newsroom's page frame, rendered with md.py, so the
words live in one place and the page is rebuilt with the rest of the site. Added on 30 October 2026, when the
editor decided the newsroom becomes an official publication (admin/notes/2026-10-30__official-publication/).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from page import newsroom_page, write  # noqa: E402
from md import front_matter, render  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "admin/content/publication"


def main():
    changed = []
    for f in sorted(SRC.glob("*.md")):
        meta, body = front_matter(f.read_text(encoding="utf-8"))
        rel = f"about/{meta['slug']}.html"
        html = newsroom_page(rel, meta["title"], meta["description"], render(body),
                             eyebrow=meta.get("eyebrow", "The publication"), crumbs=(("The publication", "about/imprint.html"),),
                             agent=meta.get("agent", meta["description"]))
        if write(rel, html):
            changed.append(rel)
    print(f"publication: {len(list(SRC.glob('*.md')))} pages" + (f"; wrote {', '.join(changed)}" if changed else "; unchanged"))


if __name__ == "__main__":
    main()
