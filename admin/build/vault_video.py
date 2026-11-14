#!/usr/bin/env python3
"""Videos from a vault, inside an article: the `!video` line.

    python3 admin/build/vault_video.py        list the !video lines in admin/content/articles and check their cards

An article's markdown can carry a line

    !video <vault card> <folder in the vault> | <caption>

where <vault card> names admin/content/vaults/<card>.json (vault id, public read key, remote) and the folder holds
a video cut by admin/writer/tools/video-cut.sh (manifest.json, poster.jpg, init.mp4, seg-NNN.m4s). The article
renderer is sgit.ai's and leaves the line as a paragraph. admin/build/sync_newsroom.py calls html_text() and md_text()
as it imports each page under articles/ (item 14 there), so the change is part of the import and its recorded hashes:
the paragraph becomes the player's figure, the player's stylesheet and scripts are added once to the page, and in the
markdown twin the line becomes the caption and a link to watch it in the vault. The player decrypts
the video in the reader's browser, piece by piece (assets/vault-video/vault-video.js). Running it twice changes
nothing the second time.
"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VAULTS = ROOT / "admin" / "content" / "vaults"
e = html.escape

PARA = re.compile(r'<p>!video (\S+) (\S+)(?: \| (.*?))?</p>', re.S)
LINE = re.compile(r'^!video (\S+) (\S+)(?: \| (.*))?$', re.M)
ASSETS = ('assets/vault-video/vault-video.css', 'assets/vendor/sgit-ai/2026-11-05/vault-embed.js',
          'assets/vault-video/vault-video.js')


def card(name):
    f = VAULTS / f"{name}.json"
    if not f.exists():
        sys.exit(f"vault_video: no vault card admin/content/vaults/{name}.json")
    return json.loads(f.read_text())


def app_url(c):
    return f"https://dev.vault.sgraph.ai/#{c['read_key']}%3A{c['vault_id']}"


def figure(m):
    c, path, cap = card(m.group(1)), m.group(2), (m.group(3) or '').strip()
    watch = f'<a href="{e(app_url(c), quote=True)}">watch it in the vault</a>'
    return (f'<figure class="vault-video" data-endpoint="{e(c["remote"], quote=True)}" data-vault="{e(c["vault_id"], quote=True)}" '
            f'data-key="{e(c["read_key"], quote=True)}" data-path="{e(path, quote=True)}">'
            f'<figcaption>{cap + " · " if cap else ""}{watch}</figcaption></figure>')


def html_text(s, rel):
    """The page's HTML with every !video paragraph made a player; rel is the page's path from the site root."""
    if '<p>!video ' not in s:
        return s
    s = PARA.sub(figure, s)
    up = '../' * rel.count('/')
    if 'vault-video/vault-video.css' not in s:
        s = s.replace('</head>', f'<link rel="stylesheet" href="{up}{ASSETS[0]}">\n</head>', 1)
    if 'vault-video/vault-video.js' not in s:
        s = s.replace('</body>', f'<script defer src="{up}{ASSETS[1]}"></script>\n'
                                 f'<script defer src="{up}{ASSETS[2]}"></script>\n</body>', 1)
    return s


def md_text(s):
    """The markdown twin with every !video line made a caption and a link to the vault."""
    if '!video ' not in s:
        return s
    def line(m):
        c, cap = card(m.group(1)), (m.group(3) or 'A video').strip()
        return f"*Video: {cap}* [Watch it in the vault]({app_url(c)})"
    return LINE.sub(line, s)


def main():
    """A check: list the articles whose markdown carries a !video line, and the vault card each names."""
    for f in sorted((ROOT / 'admin' / 'content' / 'articles').glob('*.md')):
        for m in LINE.finditer(f.read_text(encoding='utf-8')):
            card(m.group(1))
            print(f"{f.name}: {m.group(1)} {m.group(2)}")


if __name__ == '__main__':
    main()
