#!/usr/bin/env python3
"""YouTube videos inside an article, played only when the reader asks: the `!youtube` line.

    python3 admin/build/youtube_embed.py        list the !youtube lines in admin/content/articles and check their posters

An article's markdown can carry a line

    !youtube <video id> <poster file in admin/content/articles/images> | <caption>

The article renderer is sgit.ai's and leaves the line as a paragraph. admin/build/sync_newsroom.py calls html_text()
and md_text() as it imports each page under articles/ (item 15 there). In the page, the paragraph becomes a figure
with our own poster image, a play button marked YouTube, and a caption with a plain link to the video. Nothing is
fetched from YouTube or Google when the page opens: no iframe, no thumbnail, no script. Only when the reader presses
play does assets/youtube/youtube.js put a youtube-nocookie.com player in place of the poster; from then on, what
happens is between the reader and YouTube. In the markdown twin, the line becomes the caption and a link.
Running it twice changes nothing the second time.
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
IMAGES = ROOT / "admin" / "content" / "articles" / "images"
e = html.escape

ID = r'([A-Za-z0-9_-]{11})'
PARA = re.compile(r'<p>!youtube ' + ID + r' (\S+?\.(?:webp|jpg|jpeg|png))(?: \| (.*?))?</p>', re.S)
LINE = re.compile(r'^!youtube ' + ID + r' (\S+)(?: \| (.*))?$', re.M)
ASSETS = ('assets/youtube/youtube.css', 'assets/youtube/youtube.js')


def watch(vid):
    return f"https://www.youtube.com/watch?v={vid}"


def figure(m):
    vid, poster, cap = m.group(1), m.group(2), html.unescape((m.group(3) or '').strip())
    label = cap or 'A video on YouTube'
    return (f'<figure class="yt-embed" data-yt="{vid}" data-title="{e(label, quote=True)}">'
            f'<button type="button" class="yt-play" aria-label="{e("Play on YouTube: " + label, quote=True)}">'
            f'<img src="images/{e(poster, quote=True)}" alt="{e(label, quote=True)}" loading="lazy" width="1280" height="720">'
            f'<span class="yt-button" aria-hidden="true"><svg viewBox="0 0 68 48" width="68" height="48">'
            f'<path d="M66.5 7.7a8.5 8.5 0 0 0-6-6C55.2.3 34 .3 34 .3s-21.2 0-26.5 1.4a8.5 8.5 0 0 0-6 6C.1 13 .1 24 .1 24s0 11 1.4 16.3a8.5 8.5 0 0 0 6 6C12.8 47.7 34 47.7 34 47.7s21.2 0 26.5-1.4a8.5 8.5 0 0 0 6-6C67.9 35 67.9 24 67.9 24s0-11-1.4-16.3z" fill="#f00"/>'
            f'<path d="M45 24 27 14v20z" fill="#fff"/></svg></span>'
            f'<span class="yt-label" aria-hidden="true">YouTube</span></button>'
            f'<figcaption>{e(cap) + " · " if cap else ""}<a href="{watch(vid)}">watch it on YouTube</a>. '
            f'<span class="yt-note">Nothing loads from YouTube until you press play.</span></figcaption></figure>')


def html_text(s, rel):
    """The page's HTML with every !youtube paragraph made a click-to-play figure; rel is the page's path from the site root."""
    if '<p>!youtube ' not in s:
        return s
    s = PARA.sub(figure, s)
    up = '../' * rel.count('/')
    if 'youtube/youtube.css' not in s:
        s = s.replace('</head>', f'<link rel="stylesheet" href="{up}{ASSETS[0]}">\n</head>', 1)
    if 'youtube/youtube.js' not in s:
        s = s.replace('</body>', f'<script defer src="{up}{ASSETS[1]}"></script>\n</body>', 1)
    return s


def md_text(s):
    """The markdown twin with every !youtube line made a caption and a link."""
    if '!youtube ' not in s:
        return s
    return LINE.sub(lambda m: f"*Video: {(m.group(3) or 'A video on YouTube').strip()}* [Watch it on YouTube]({watch(m.group(1))})", s)


def main():
    """A check: list the articles whose markdown carries a !youtube line, and that each poster exists."""
    bad = 0
    for f in sorted((ROOT / 'admin' / 'content' / 'articles').glob('*.md')):
        for m in LINE.finditer(f.read_text()):
            ok = (IMAGES / m.group(2)).exists()
            bad += not ok
            print(f"{f.stem}: {m.group(1)} poster {m.group(2)} {'ok' if ok else 'MISSING'}")
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
