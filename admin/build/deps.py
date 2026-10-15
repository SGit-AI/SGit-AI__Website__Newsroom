#!/usr/bin/env python3
"""What this site still takes from sgit.ai, by kind (card 062).

    python3 admin/build/deps.py

The owner's rule of 15 October 2026: the newsroom must be self-contained; the one thing it may point at
outside itself is a vault, from the page that has one. This scans the published tree (html, md, css, js,
json, txt, xml) for references to sgit.ai and its network, sorts them by kind, and writes
admin/notes/sgit-ai-dependencies.md so each release can show the count going down. Nothing here changes
a page. The kinds, in the order they will go:

  generator   pages imported from sgit.ai's build (admin/build/newsroom-sync.json): the articles, the
              account, the personas. Goes when the generator is ported here.
  network     links to sgit.ai's own pages and the network sites (pt.newsroom, graphs, pki, nhi, docs.diniscruz).
  words       "sgit.ai" and "the sgit project" in prose: a name, not a link (the disclosure, the kit, the method).
  vault       links to a vault (store.sgit.ai, vaults.sgit.ai, a sgit clone line). ALLOWED: the one dependency that stays.
  own         newsroom.sgit.ai and api.newsroom.sgit.ai: this site's own addresses, not a dependency; counted, not reported.
"""
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "admin/notes/sgit-ai-dependencies.md"
EXT = {".html", ".md", ".css", ".js", ".mjs", ".json", ".txt", ".xml"}
SKIP = ("admin/build/newsroom-sync.json", "admin/notes/sgit-ai-dependencies.md", "llms-full.txt", "search/text.json", "search/docs.json",
        "node_modules/", ".git/", "admin/engineering/", "admin/content/", "articles/versions/", "world-news-day/", "documents/",
        # the archive (admin/build/archive.py): dated pages kept at their addresses, not the running newsroom
        "archive/", "library/", "briefs/", "governance/", "portugal/", "mvps/", "pt-newsroom/")
VAULT = re.compile(r"https?://(store|vaults?|hub)\.sgit\.ai|sgit (clone|read|open) sgit_public_read_|sgit_public_read_[0-9a-f]{8}")
OWN = re.compile(r"https?://(api\.|pt\.)?newsroom\.sgit\.ai|newsroom\.sgit\.ai")
NET = re.compile(r"https?://(www\.)?(sgit\.ai|graphs\.sgit\.ai|pki\.sgit\.ai|nhi\.sgit\.ai|pt\.newsroom\.sgit\.ai|docs\.diniscruz\.ai)(/[^\s\"'<)]*)?")
WORDS = re.compile(r"\bsgit\.ai\b|\bthe sgit project\b")


def main():
    record = json.loads((ROOT / "admin/build/newsroom-sync.json").read_text(encoding="utf-8"))
    imported = set(record["files"])
    kinds = defaultdict(Counter)       # kind -> file -> n
    targets = Counter()                # network link target -> n
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file() or p.suffix not in EXT:
            continue
        rel = p.relative_to(ROOT).as_posix()
        if any(rel.startswith(s) or ("/" + s) in ("/" + rel) for s in SKIP):
            continue
        try:
            t = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if rel in imported:
            kinds["generator"][rel] += 1
        for m in VAULT.finditer(t):
            kinds["vault"][rel] += 1
        t2 = VAULT.sub(" ", OWN.sub(" ", t))
        for m in NET.finditer(t2):
            kinds["network"][rel] += 1
            targets[(m.group(2) + (m.group(3) or "/")).split("#")[0][:80]] += 1
        t3 = NET.sub(" ", t2)
        for m in WORDS.finditer(t3):
            kinds["words"][rel] += 1
    own_pages = sum(1 for k in kinds["network"] if k not in imported)
    lines = ["# What this site still takes from sgit.ai", "",
             "Written by `admin/build/deps.py`; do not edit. The rule: the newsroom is self-contained, and the one link it keeps "
             "outside itself is to a vault, from the page that has one. The counts below are the work left, by kind, in the "
             "order it will go.", "",
             "| kind | files | references | what it is |", "|---|---:|---:|---|",
             f"| generator | {len(kinds['generator'])} | | pages imported from sgit.ai's build; goes when the generator is ported here |",
             f"| network | {len(kinds['network'])} | {sum(kinds['network'].values())} | links to sgit.ai's pages and the network sites ({own_pages} files this site writes itself) |",
             f"| words | {len(kinds['words'])} | {sum(kinds['words'].values())} | sgit.ai or the sgit project named in prose: the disclosure, the kit, the method |",
             f"| vault | {len(kinds['vault'])} | {sum(kinds['vault'].values())} | links to a vault: the one dependency that stays |",
             "", "## Network links, by target", ""]
    lines += [f"- {n} × `{tg}`" for tg, n in targets.most_common(40)]
    lines += ["", "## Network links in pages this site writes itself", "",
              "The pages this site can fix now (an imported page is fixed in the generator, when it moves here).", ""]
    lines += [f"- `{rel}` ({n})" for rel, n in sorted(kinds["network"].items(), key=lambda x: (-x[1], x[0])) if rel not in imported][:80]
    lines += ["", "## Words, in pages this site writes itself", ""]
    lines += [f"- `{rel}` ({n})" for rel, n in sorted(kinds["words"].items(), key=lambda x: (-x[1], x[0])) if rel not in imported][:60]
    lines.append("")
    text = "\n".join(lines)
    changed = not OUT.exists() or OUT.read_text(encoding="utf-8") != text
    if changed:
        OUT.write_text(text, encoding="utf-8")
    print("deps: " + " · ".join(f"{k} {len(kinds[k])} files/{sum(kinds[k].values())} refs" for k in ("generator", "network", "words", "vault"))
          + f" · own pages with network links {own_pages}; {OUT.relative_to(ROOT)} {'written' if changed else 'unchanged'}")


if __name__ == "__main__":
    main()
