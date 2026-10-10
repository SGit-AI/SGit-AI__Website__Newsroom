#!/usr/bin/env python3
"""sitemap.xml, from the tree.

    python3 admin/build/gen_sitemap.py

The sitemap was kept by hand while the site had 130 pages. The newsroom import brought 312
more, and validate.js already fails the build when the sitemap and the tree disagree in
either direction, so keeping it by hand would only have meant failing the build by hand.
It lists every page the gate checks, with the same two exclusions (summit-archive/ holds
copies, vault-app/ renders inside a vault), and dates each from the last commit that
touched it, or today for a page not yet committed.
"""
import datetime
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HOST = (ROOT / "CNAME").read_text().strip()


def last_dates():
    out = subprocess.run(["git", "-C", str(ROOT), "log", "--format=>%cs", "--name-only"],
                         capture_output=True, text=True).stdout
    dates, current = {}, None
    for line in out.splitlines():
        if line.startswith(">"):
            current = line[1:]
        elif line and line not in dates:
            dates[line] = current
    return dates


def main():
    today = datetime.date.today().isoformat()
    dates = last_dates()
    pages = sorted(p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*.html")
                   if not ({".git", "node_modules", ".sg_vault", "summit-archive", "vault-app"} & set(p.parts)))
    # The home page first, then the rest in path order.
    pages.sort(key=lambda p: (p != "index.html", p))
    rows = "\n".join(f"  <url><loc>https://{HOST}/{p}</loc><lastmod>{dates.get(p, today)}</lastmod></url>"
                     for p in pages)
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + rows + "\n</urlset>\n")
    target = ROOT / "sitemap.xml"
    if not target.exists() or target.read_text() != xml:
        target.write_text(xml)
    print(f"sitemap: {len(pages)} pages")


if __name__ == "__main__":
    main()
