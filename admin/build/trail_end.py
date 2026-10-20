#!/usr/bin/env python3
"""Trail ends: a compact copy of an article's trail at the end of its text, with the next piece marked.

    python3 admin/build/trail_end.py            stamp every article that has a trail
    python3 admin/build/trail_end.py --check    list the articles it would stamp

An article written with `!trail <name>` opens with a row of cards: each piece of the trail, this one marked "you
are here". At the end of the text the reader had only "Continued by", under the meter. This copies the same cards,
smaller, to the end of the article text, just before the meter, and marks the card after this one "next". The cards
are copied from the page's own trail, not rebuilt from trails.json, so trails that sgit.ai publishes work too.

The block is <nav class="trail-end">. summaries.py stops reading an article at it, so it is not part of any section's
text or hash; validate.js and sync_newsroom.py strip it, as they strip the series blocks. series.py calls this after
stamping the series, so every release that stamps series stamps trail ends too.
"""
import argparse
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
END = re.compile(r'<nav class="trail-end"[^>]*>.*?</nav>\n', re.S)
TAG = re.compile(r'<(/?)div\b[^>]*>')


def block(page, start):
    """The balanced <div class="trail">…</div> that starts at `start`."""
    depth = 0
    for m in TAG.finditer(page, start):
        depth += -1 if m.group(1) else 1
        if depth == 0:
            return page[start:m.end()]
    return None


def compact(trail):
    title = re.search(r'<div class="trail-h">(.*?)</div>', trail, re.S)
    row = re.search(r'<div class="trail-row">', trail)
    if not (title and row):
        return None
    cards = trail[row.end():-len("</div></div>")]
    cards = re.sub(r'<span class="trail-d">.*?</span>', "", cards, flags=re.S)
    cards = re.sub(r'<span class="trail-l">.*?</span>(?=</div>)', "", cards, flags=re.S)
    # mark the card after "you are here" as next
    here = cards.find('trail-c here"')
    if here >= 0:
        after = re.compile(r'<(a|div) class="trail-c"').search(cards, here + 1)
        if after:
            i = after.start()
            tag_end = cards.find(">", i) + 1
            cards = (cards[:i] + cards[i:tag_end].replace('class="trail-c"', 'class="trail-c next"')
                     + '<span class="trail-here trail-next">next &rarr;</span>' + cards[tag_end:])
    return (f'<nav class="trail-end" aria-label="Continue the trail: {html.escape(html.unescape(title.group(1)), quote=True)}">'
            f'<div class="trail-end-h"><span class="trail-end-k">Continue the trail</span> {title.group(1)}</div>'
            f'<div class="trail-row">{cards}</div></nav>\n')


def stamp(p, check=False):
    page = p.read_text(encoding="utf-8")
    clean = END.sub("", page)
    i = clean.find('<div class="trail">')
    if i < 0:
        if clean != page and not check:
            p.write_text(clean, encoding="utf-8")
        return False
    t = block(clean, i)
    nav = compact(t) if t else None
    j = clean.find("<sg-meter", i)  # the article's meter: the header has one of its own, before the trail
    if j < 0:
        j = clean.find('<section class="athreads"', i)
    if not nav or j < 0:
        return False
    if check:
        return True
    new = clean[:j] + nav + clean[j:]
    if new != page:
        p.write_text(new, encoding="utf-8")
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    run(a.check)


def run(check=False):
    done = [p.stem for p in sorted((ROOT / "articles").glob("*.html")) if stamp(p, check)]
    if check:
        print("trail_end: " + ", ".join(done))
    else:
        print(f"trail_end: {len(done)} articles with a trail end")
    return done


if __name__ == "__main__":
    main()
