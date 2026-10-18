#!/usr/bin/env python3
"""Figure sizes: flag figures that will show with oversized lettering, so they get a size.

    python3 admin/build/figures.py            list figures in admin/content/articles that probably need a size
    python3 admin/build/figures.py FILE...    only these articles

An article's figures fill the column (about 915 px wide on a laptop) unless the `!shot` line gives a size: small,
narrow or medium (42%, 62% or 78% of the column; full width on a phone). A figure drawn or captured narrower than the
column, or taller than it is wide, is stretched to fill it, and its text comes out larger than the article's own. This
lists those that have no size, with a suggestion. The caption always keeps the column's full width, whatever the size.
It is a warning, not a gate: a tall figure can be meant to be read at full width.
"""
import glob
import os
import re
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ART = os.path.join(ROOT, "admin", "content", "articles")
COLUMN = 915
SIZES = ("small", "narrow", "medium")


def suggest(w, h):
    tall = h / w
    if w < 600 or tall > 2.0:
        return "small"
    if w < COLUMN or tall > 1.25:
        return "narrow"
    if tall > 1.05:
        return "medium"
    return ""


def main(files):
    files = files or sorted(glob.glob(os.path.join(ART, "*.md")))
    n = 0
    for f in files:
        for line in open(f, encoding="utf-8"):
            if not line.startswith("!shot "):
                continue
            parts = [p.strip() for p in line[6:].split("|")]
            if len(parts) >= 4 and parts[3] in SIZES:
                continue
            path = os.path.join(os.path.dirname(f), parts[1], parts[0])
            if not os.path.exists(path):
                continue
            w, h = Image.open(path).size
            s = suggest(w, h)
            if s:
                n += 1
                print(f"{os.path.basename(f)}: {parts[0]} is {w}x{h}; suggest '{s}'")
    print(f"figures: {n} figure(s) without a size that would be stretched")


if __name__ == "__main__":
    main(sys.argv[1:])
