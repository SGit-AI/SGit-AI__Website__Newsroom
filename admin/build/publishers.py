#!/usr/bin/env python3
"""For publishers: the page to send someone new to this newsroom, built in every release so it stays current.

    python3 admin/build/publishers.py            write publishers/index.html, index.md, changes.json and versions/
    python3 admin/build/publishers.py --check    say what the page is built from and what would change; write nothing

Until v0.12.113 this page was sgit.ai's, written once on 11 October 2026 and imported by sync_newsroom.py. The site
changed most days after that and the page did not, so it moved here (card 085). It is now two things:

  the editor's text     admin/content/publishers/page.md: front matter (title, eyebrow, description) and markdown,
                        with slots on their own line that the build fills: {{status}}, {{features}}, {{latest}},
                        {{designed}}, {{start_here}}; and inline, {{releases_since_first}}.
  the live parts        the features a publisher can use today, from the register (admin/content/features.json, the
                        entries whose audiences include publishers); the newest articles placed in the publishers'
                        section (sections/publishers.json, so sections.py runs first); and the five to start with,
                        from that section's own file. Nothing in them is listed by hand on this page.

It has a version history like an article's (admin/build/page_versions.py): admin/content/publishers/versions.json
lists the versions of the text, each frozen at publishers/versions/<v>.md; publishers/changes.json records, per
release, what the live parts did; publishers/versions/index.html shows both, and the differences between versions.
Change page.md and the build stops until versions.json has a version for the change.
"""
import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from page import newsroom_page, write, esc, HOST  # noqa: E402
from md import front_matter, render  # noqa: E402
from page_versions import Versions, ledger_html, words, blocks  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
SRC = "admin/content/publishers"
PAGE = "publishers/index.html"
FIRST = "v0.7.1"          # the release of this site when the first version of the page was written, 11 October 2026
LATEST = 6
LATEST_STREAMS = ("paid", "answers", "readers")


def load(p):
    return json.loads((ROOT / p).read_text(encoding="utf-8"))


def releases():
    """Every release of this site, newest first, with its date, from the release history."""
    t = (ROOT / "admin/versions.html").read_text(encoding="utf-8")
    return re.findall(r'<td class="vnum">(v[\d.]+)</td>\s*<td>([^<]*)</td>', t)


def short(d):
    """2026-10-17 -> 17 Oct."""
    try:
        x = date.fromisoformat(d)
    except ValueError:
        return d
    return f"{x.day} {x:%b}"


def since(f, when):
    s = f.get("since") or ""
    if s.startswith("v"):
        return f"{when[s]} ({s})" if s in when else s
    return short(s) if s else "earlier"


def fill(src, ctx):
    out = []
    for line in src.splitlines():
        m = re.fullmatch(r"\{\{(\w+)\}\}", line.strip())
        out.append(ctx[m.group(1)] if m else line)
    text = "\n".join(out)
    left = re.findall(r"\{\{(\w+)\}\}", text)
    for k in left:
        if k not in ctx:
            sys.exit(f"publishers: {SRC}/page.md has a slot {{{{{k}}}}} the build does not fill")
    return re.sub(r"\{\{(\w+)\}\}", lambda m: ctx[m.group(1)], text)


def build():
    source = (ROOT / SRC / "page.md").read_text(encoding="utf-8")
    meta, body_src = front_matter(source)
    versions = Versions("publishers", SRC)
    current = versions.current(source)
    site = (ROOT / "admin/build/version.txt").read_text().strip()
    ids, feats, sec = load("articles/ids.json"), load("admin/content/features.json"), load("sections/publishers.json")
    sec_src = load("admin/content/sections/publishers.json")
    by = {a["slug"]: a for a in ids["articles"]}
    today = max(a["date"] for a in ids["articles"])
    rel = releases()
    when = {v: short(date(*_iso(d)).isoformat()) for v, d in rel}
    since_first = next((i for i, (v, _) in enumerate(rel) if v == FIRST), len(rel))

    mine = [f for f in feats["features"] if "publishers" in f["audiences"]]
    live = [f for f in mine if f["status"] in ("live", "beta")]
    live.sort(key=lambda f: _order(f, rel))
    designed = [f for f in mine if f["status"] == "designed"]
    labels = feats["status_labels"]

    rows = ["| What | Since | How it works | Try it |", "|---|---|---|---|"]
    for f in live:
        tag = "" if f["status"] == "live" else f" ({labels[f['status']].lower()})"
        links = []
        if f.get("try"):
            links.append(f"[Try it](../{f['try']})")
        if f.get("article"):
            links.append(f"[read about it](../articles/{f['article']}.html)")
        rows.append(f"| **{f['name']}**{tag} | {since(f, when)} | {f['what']} | {' · '.join(links)} |")
    features_md = "\n".join(rows)

    # the streams a publisher reads for the business; the newsroom's own method is counted, and linked, not listed
    placed = {st["id"]: [a["slug"] for a in st["articles"] if a["slug"] in by] for st in sec["streams"]}
    latest = sorted((s for k in LATEST_STREAMS for s in placed.get(k, [])), key=lambda s: (by[s]["date"], by[s]["n"]), reverse=True)[:LATEST]
    week = (date.fromisoformat(today) - timedelta(days=7)).isoformat()
    method_new = [s for s in placed.get("method", []) if by[s]["date"] > week]
    latest_md = "\n".join(
        f"- [{by[s]['title']}](../articles/{s}.html), {short(by[s]['date'])}. {by[s].get('teaser', '')}" for s in latest)
    if method_new:
        latest_md += (f"\n\nAnd {len(method_new)} in the last week on [how this newsroom runs](../sections/publishers/index.html#method), "
                      f"the newest [{by[method_new[0]]['title'].split(':')[0]}](../articles/{method_new[0]}.html).")
    designed_md = "\n".join(
        f"  - **{f['name']}**: {f['what']} [The design](../articles/{f['article']}.html)." for f in designed)
    designed_md += ("\n  - **The larger designs**: [selling the graph](../thesis/index.html), [corrections that reach the pages that "
                    "cited them](../corrections/index.html) and [paying the people whose facts an article uses](../economics/index.html).")
    start_md = "\n".join(
        f"{i}. [**{by[s]['title'].split(':')[0]}**](../articles/{s}.html): {w}" for i, (s, w) in enumerate(sec_src["start_here"], 1) if s in by)
    status_md = (f"*This page: **{current['version']}**, {short(current['date'])} 2026, [every version and what changed](versions/index.html). "
                 f"Built with newsroom.sgit.ai {site}: {len(ids['articles'])} articles, {len(live)} features a publisher can use today, "
                 f"the newest article {short(today)}.*")

    body_md = fill(body_src, {
        "status": status_md, "features": features_md, "latest": latest_md, "designed": designed_md,
        "start_here": start_md, "releases_since_first": str(since_first),
    })
    foot = (f"\n\n*As of {short(today)} 2026, newsroom.sgit.ai {site}. The text is version {current['version']} of this page, "
            f"by {current['by']}; the features, the newest articles and the five to start with are rebuilt from the site's own data in every "
            f"release. The first version was written on sgit.ai on 11 October 2026 by agent@riskmandate.ai, from Dinis Cruz's brief. "
            f"AI-generated, disclosed as Article 50 of the EU AI Act asks. Dinis Cruz has editorial responsibility.*\n")
    body_md += foot

    url = f"https://{HOST}/{PAGE}"
    md = (f"# For publishers: {meta['title']}\n\n> {meta['description']}\n\n"
          f"*Source: <{url}> · newsroom.sgit.ai {site} · this file is generated from the same source as the page "
          f"(`{SRC}/page.md` and the site's data), so the two cannot drift.*\n\n---\n\n"
          f"[Home](../index.md) / For publishers\n\n{meta['eyebrow']}\n\n# {meta['title']}\n\n{body_md}\n\n---\n\n"
          f"*[Site index for agents](../llms.txt) · [HTML version]({url})*\n")

    html_body = render(body_md)
    html_body = html_body.replace('<a href="../index.html">Open newsroom.sgit.ai</a>',
                                  '<a class="pb-open" href="../index.html">Open newsroom.sgit.ai &rarr;</a>')
    html_body += """
<style>
.pb-open{display:inline-block;padding:.45rem .9rem;border-radius:8px;border:1px solid var(--accent);font-weight:600;text-decoration:none}
main.doc table td:nth-child(2){white-space:nowrap}
.agent p{overflow-wrap:anywhere}
</style>"""
    agent = (f"The page for publishers on newsroom.sgit.ai, version {current['version']} of its text, built with site {site}: what is live, "
             f"how to try it in five minutes, what is not done, and how to reach the editor. Markdown twin: https://{HOST}/publishers/index.md. "
             f"Its versions and what changed: https://{HOST}/publishers/versions/index.html; what its live parts did per release: "
             f"https://{HOST}/publishers/changes.json. The features come from https://{HOST}/sections/features.json and the articles from "
             f"https://{HOST}/sections/publishers.json.")
    page = newsroom_page(PAGE, meta["nav_title"], meta["description"], html_body, eyebrow=esc(meta["eyebrow"]),
                         agent=esc(agent), head='<link rel="alternate" type="text/markdown" href="index.md">\n')
    # newsroom_page puts the short title in <h1>; the page's own headline is longer
    page = page.replace(f"<h1>{esc(meta['nav_title'])}</h1>", f"<h1>{esc(meta['title'])}</h1>", 1)

    state = {"features": {f["id"]: f["status"] for f in mine}, "latest": latest, "start_here": [s for s, _ in sec_src["start_here"]]}
    return versions, current, page, md, state, site, today, by, {f["id"]: f for f in feats["features"]}


def _iso(d):
    """'18 Oct 2026' -> (2026, 10, 18)."""
    x = date.fromisoformat(d) if re.fullmatch(r"\d{4}-\d\d-\d\d", d) else None
    if x is None:
        from datetime import datetime
        x = datetime.strptime(d.strip(), "%d %b %Y").date()
    return x.year, x.month, x.day


def _order(f, rel):
    """Newest first by the release it shipped in, or its date; entries with no date last."""
    s = f.get("since") or ""
    if s.startswith("v"):
        idx = next((i for i, (v, _) in enumerate(rel) if v == s), len(rel))
        return idx
    if s:
        d = date(*_iso(s))
        return next((i for i, (_, rd) in enumerate(rel) if date(*_iso(rd)) <= d), len(rel))
    return len(rel)


def versions_page(versions, current, site, ledger, by, feats):
    table, diffs = versions.history_html()
    body = f"""<p class="lead">The page for publishers has a version history, the way every article on this site has one. Its text changes when the editor decides it should, and every version is kept as it was published, with what changed. Its live parts, the features and the newest articles, change on their own in every release; those changes are recorded too.</p>
<p>The current text is <b>{esc(current["version"])}</b>, of {esc(current["date"])}. <a href="../index.html">The page as it is now</a>.</p>
<h2 id="versions">The versions of the text</h2>
{table}
<p class="dim">A change to the text is the next minor version; a rewrite is the next major, the editor's call. The build will not publish a changed text without a new version: <code>admin/content/publishers/versions.json</code> records the sha256 of the source each version was built from. Each version is frozen as markdown, live parts included, by the release that made it, and never rewritten.</p>
<h2 id="changes">What changed between them</h2>
{diffs}
<h2 id="live">What the live parts did, release by release</h2>
<p>The features table, the newest for publishers and the five to start with are rebuilt in every release from the site's own data. When one of them changes, the release is recorded here and in <a href="../changes.json">publishers/changes.json</a>.</p>
{ledger_html(ledger, feats, by, "../../")}
<style>
.pv-blk{{margin:.5rem 0;padding:.45rem .7rem;border-left:3px solid var(--line);background:var(--panel);overflow-wrap:anywhere}}
.pv-k{{font-size:.72rem;font-weight:600;text-transform:uppercase;letter-spacing:.05em;opacity:.75;margin-right:.3rem}}
.pv-blk del{{background:var(--danger-bg)}} .pv-blk ins{{background:var(--info-bg);text-decoration:underline}}
.pv-ledger li{{margin:.4rem 0}} .agent p{{overflow-wrap:anywhere}}
</style>"""
    agent = (f"The version history of https://{HOST}/publishers/index.html: {len(versions.entries)} versions of its text, each at "
             f"https://{HOST}/publishers/versions/<version>.md, the current one {current['version']}; what its live parts did per release "
             f"at https://{HOST}/publishers/changes.json. Built with site {site}.")
    return newsroom_page("publishers/versions/index.html", "Versions of the page for publishers",
                         "Every version of the page for publishers, what changed between them, and what its live parts did in each release.",
                         body, eyebrow="A page's history", crumbs=(("For publishers", "publishers/index.html"),), agent=esc(agent))


def main():
    check = "--check" in sys.argv
    versions, current, page, md, state, site, today, by, feats = build()
    print(f"publishers: text {current['version']} ({words(chr(10).join(blocks(md))):,} words), site {site}; "
          f"{len(state['features'])} features in the register for publishers, {len(state['latest'])} newest articles")
    if check:
        missing = [s for s in versions.missing() if s != versions.snapshot(current)]
        if missing:
            sys.exit(f"publishers: frozen versions missing: {missing}")
        return
    written = []
    if write(PAGE, page):
        written.append(PAGE)
    p = ROOT / "publishers/index.md"
    if not p.exists() or p.read_text(encoding="utf-8") != md:
        p.write_text(md, encoding="utf-8")
        written.append("publishers/index.md")
    if versions.freeze(current, md):
        written.append(versions.snapshot(current))
    missing = versions.missing()
    if missing:
        sys.exit(f"publishers: frozen versions missing, and only the current one can be frozen now: {missing}")
    ledger, changed = versions.ledger(state, site, today,
                                      "What the live parts of https://newsroom.sgit.ai/publishers/index.html did, per release: features "
                                      "added, removed or changed status in the register, articles that came into or left the newest for publishers, "
                                      "and changes to the five to start with. Written by admin/build/publishers.py; `state` is what it "
                                      "compares the next release against.")
    if changed:
        written.append("publishers/changes.json")
    if write("publishers/versions/index.html", versions_page(versions, current, site, ledger, by, feats)):
        written.append("publishers/versions/index.html")
    print(f"publishers: {len(written)} file(s) written {written}")


if __name__ == "__main__":
    main()
