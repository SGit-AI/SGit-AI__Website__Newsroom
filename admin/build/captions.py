#!/usr/bin/env python3
"""Figure captions are short: what the image is, in at most LIMIT characters.

    python3 admin/build/captions.py                 every article and draft over the limit, with the count
    python3 admin/build/captions.py FILE.md ...     only these files
    python3 admin/build/captions.py --check         exit 1 if any caption is over the limit (validate.js does the same)

A caption is the third field of a `!shot` or `!frames` line, and it is also the image's alt text. It describes the
image; the numbers and the argument belong in the article's text. Long captions overflowed the page beside a figure
and could not be carried into a LinkedIn article or newsletter, so the editor set a limit on 27 October 2026. The
limit is below the 250 characters a third-party guide gives for a photo credit in LinkedIn's publisher (no
official LinkedIn figure was found).
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LIMIT = 120
SHOT = re.compile(r"^!(shot|frames)\s+(.+)$", re.M)


def long_captions(path):
    out = []
    text = path.read_text(encoding="utf-8")
    for m in SHOT.finditer(text):
        parts = [x.strip() for x in m.group(2).split("|")]
        cap = parts[2] if len(parts) > 2 else ""
        if len(cap) > LIMIT:
            line = text.count("\n", 0, m.start()) + 1
            out.append((line, len(cap), cap))
    return out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    files = [Path(a) for a in args] or sorted((ROOT / "admin/content/articles").glob("*.md")) + sorted((ROOT / "admin/content/drafts").glob("*.md"))
    n = 0
    for f in files:
        for line, k, cap in long_captions(f):
            n += 1
            print(f"{f.relative_to(ROOT) if f.is_absolute() else f}:{line}: {k} characters (limit {LIMIT}): {cap[:90]}...")
    print(f"captions: {n} over {LIMIT} characters")
    if "--check" in sys.argv and n:
        sys.exit(1)


if __name__ == "__main__":
    main()
