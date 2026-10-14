#!/usr/bin/env python3
"""Engineering: the issues and the releases, rendered from admin/engineering/ (see its README).

    python3 admin/build/engineering.py

Reads admin/engineering/issues/{open,blocked,done}/NNN-slug.md and admin/engineering/releases/vX.Y.Z.md (markdown with
front matter, the Issues-FS-lite layout: the folder is the status) and writes:

    engineering/index.html            the board: open, blocked, done; the releases
    engineering/issues/NNN.html       one page per card
    engineering/releases/vX.Y.Z.html  one page per release, with its cards
    engineering/issues.json           a derived index for agents (a cache, never the source: the files are)
    engineering/engineering.css

The files are the source of truth; walk them, do not read the index to find a card.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from page import newsroom_page, write, esc, HOST  # noqa: E402
from md import render, front_matter  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "admin/engineering"
STATUSES = ("open", "blocked", "done")
KINDS = {"bug": "Bug", "story": "Story", "task": "Task"}
CSS = """/* the engineering pages */
.eng-board h2 { margin-top: 1.6rem; }
.eng-board table { width: 100%; border-collapse: collapse; font-size: .92rem; }
.eng-board th, .eng-board td { text-align: left; padding: .45rem .5rem; border-bottom: 1px solid var(--line, #e3e5ea); vertical-align: top; }
.eng-board th { font-size: .72rem; letter-spacing: .1em; text-transform: uppercase; color: var(--dim, #5a5e68); }
.eng-board td.id, .eng-meta td.k { font-family: var(--mono, ui-monospace, monospace); white-space: nowrap; }
.eng-tag { display: inline-block; padding: 0 .5em; border-radius: 999px; font-size: .74rem; font-weight: 600; background: var(--mute-bg, #eef1f4); color: var(--text, #3a3d45); white-space: nowrap; }
.eng-tag.bug { background: var(--danger-bg, #fdecec); color: var(--danger-ink, #8a0a0a); } .eng-tag.story { background: var(--tint-solid, #e6f4ee); color: var(--accent, #0f6b4f); } .eng-tag.task { background: var(--info-bg, #e8eefc); color: var(--info-ink, #1d4ed8); }
.eng-tag.open { background: var(--warn-bg, #fff4e0); color: var(--warn-ink, #8a5a0a); } .eng-tag.blocked { background: var(--danger-bg, #fdecec); color: var(--danger-ink, #8a0a0a); } .eng-tag.done { background: var(--fg, #1c1d21); color: var(--bg, #fff); }
.eng-tag.urgent { background: var(--danger-ink, #8a0a0a); color: #fff; } .eng-tag.high { background: var(--danger-bg, #fdecec); color: var(--danger-ink, #8a0a0a); }
.eng-meta { width: 100%; border-collapse: collapse; font-size: .9rem; margin: .8rem 0 1.4rem; }
.eng-meta td { padding: .3rem .5rem; border-bottom: 1px solid var(--line, #e3e5ea); vertical-align: top; }
.eng-meta td.k { color: var(--dim, #5a5e68); width: 9rem; }
.eng-body pre { background: #14161a; color: #e6e8ec; padding: .8rem 1rem; border-radius: 8px; overflow: auto; font-size: .82rem; line-height: 1.5; }
.eng-body pre code.lang-gherkin { color: #a6e3c3; }
.eng-body img { max-width: 100%; height: auto; border: 1px solid var(--line, #e3e5ea); border-radius: 8px; margin: .4rem 0; }
.eng-body blockquote { border-left: 3px solid var(--line2, #cfd2d8); margin: .6rem 0; padding: .1rem 0 .1rem .9rem; color: var(--text, #34363c); }
"""


def load_issues():
    issues = []
    for status in STATUSES:
        for f in sorted((SRC / "issues" / status).glob("*.md")):
            meta, body = front_matter(f.read_text(encoding="utf-8"))
            if not meta.get("id"):
                raise SystemExit(f"engineering: {f} has no id in its front matter")
            meta.update(status=status, slug=f.stem, body=body, path=str(f.relative_to(ROOT)))
            issues.append(meta)
    ids = [i["id"] for i in issues]
    dup = {x for x in ids if ids.count(x) > 1}
    if dup:
        raise SystemExit(f"engineering: duplicate issue ids {sorted(dup)}")
    return sorted(issues, key=lambda i: i["id"])


def load_releases():
    rels = []
    for f in sorted((SRC / "releases").glob("v*.md")):
        meta, body = front_matter(f.read_text(encoding="utf-8"))
        meta.update(body=body, slug=f.stem, path=str(f.relative_to(ROOT)))
        if isinstance(meta.get("issues"), str):
            meta["issues"] = [x.strip() for x in meta["issues"].strip("[]").split(",") if x.strip()]
        rels.append(meta)
    vkey = lambda r: tuple(int(x) for x in re.findall(r"\d+", r.get("version", "0")))  # noqa: E731
    return sorted(rels, key=vkey, reverse=True)


def tag(text, cls=""):
    return f'<span class="eng-tag {esc(cls)}">{esc(text)}</span>'


def first_heading(body):
    m = re.search(r"^#\s+(.*)$", body, re.M)
    return m.group(1).strip() if m else ""


def rel_link(version, up, known):
    """A release named by a card: a link when the release file exists, else the version as planned."""
    if not version:
        return "<span class=dim>–</span>"
    if version in known:
        return f'<a href="{up}releases/{esc(version)}.html">{esc(version)}</a>'
    return f"{esc(version)} <span class=dim>(planned)</span>"


def issue_rows(issues, up, known=()):
    rows = "".join(
        f'<tr><td class="id"><a href="{up}issues/{esc(i["id"])}.html">{esc(i["id"])}</a></td>'
        f'<td>{tag(KINDS.get(i.get("kind", ""), i.get("kind", "")), i.get("kind", ""))}</td>'
        f'<td>{tag(i.get("priority", ""), i.get("priority", ""))}</td>'
        f'<td><a href="{up}issues/{esc(i["id"])}.html">{esc(i.get("title", i["slug"]))}</a></td>'
        f'<td>{rel_link(i.get("release", ""), up, known)}</td>'
        f'<td>{tag(i["status"], i["status"])}</td></tr>'
        for i in issues)
    return ('<div class="tablewrap"><table><thead><tr><th>Id</th><th>Kind</th><th>Priority</th><th>Title</th><th>Release</th><th>Status</th></tr></thead>'
            f"<tbody>{rows}</tbody></table></div>")


def board(issues, releases):
    by = {s: [i for i in issues if i["status"] == s] for s in STATUSES}
    known = {r.get("version") for r in releases}
    sections = []
    for s, label, note in (("open", "Open", "asked and not yet done, newest first"), ("blocked", "Blocked", "waiting on something named in the card"), ("done", "Done", "with an outcome appended, and screenshots where they help")):
        items = sorted(by[s], key=lambda i: i["id"], reverse=(s != "done"))
        sections.append(f'<h2 id="{s}">{label} <span class="dim">({len(items)}: {note})</span></h2>' + (issue_rows(items, "", known) if items else "<p class=dim>None.</p>"))
    rel_rows = "".join(
        f'<tr><td class="id"><a href="releases/{esc(r["slug"])}.html">{esc(r.get("version", r["slug"]))}</a></td><td>{esc(r.get("date", ""))}</td>'
        f'<td>{tag(r.get("kind", "patch"))}</td><td>{len(r.get("issues", []))}</td><td><a href="releases/{esc(r["slug"])}.html">{esc(first_heading(r["body"]) or r["slug"])}</a></td></tr>'
        for r in releases)
    body = f"""<p>The work on this site, tracked as files in the repository (<code>admin/engineering/</code>), the way <a href="https://issues-fs.sgit.ai/lite/index.html">Issues-FS-lite</a> does it: one markdown card per issue with front matter, three folders (open, blocked, done) whose path is the status, and one file per release naming the cards it carries. Each card says what is asked or what happens, the scenario in Gherkin, a mock-up before it is built, and the outcome and screenshots after. Every change to the site is connected to a card, and <a href="../admin/versions.html">the release history</a> names the ids. Where a card came from is in its <em>source</em>: the owner&rsquo;s feedback through the vault pane&rsquo;s lane, a screenshot, a note in chat, a brief on sgit.ai, a test.</p>
<div class="eng-board">
{''.join(sections)}
<h2 id="releases">Releases <span class="dim">({len(releases)})</span></h2>
<div class="tablewrap"><table><thead><tr><th>Version</th><th>Date</th><th>Kind</th><th>Cards</th><th>What it says</th></tr></thead><tbody>{rel_rows}</tbody></table></div>
</div>
<p class="dim">For agents: <a href="issues.json">issues.json</a> is a derived index of the cards; the files under <code>admin/engineering/issues/</code> are the source, and <code>admin/engineering/README.md</code> is the convention.</p>
"""
    agent = (f"Engineering on newsroom.sgit.ai: issues and releases as files (admin/engineering/, Issues-FS-lite layout: issues/open|blocked|done/NNN-slug.md with front matter id, title, kind, priority, created, source, release, estimated_effort; releases/vX.Y.Z.md with version, date, kind, issues). "
             f"{len(by['open'])} open, {len(by['blocked'])} blocked, {len(by['done'])} done; {len(releases)} release(s). The derived index is https://{HOST}/engineering/issues.json; walk the files for the truth. A version row in admin/versions.html names the ids it answers.")
    return newsroom_page("engineering/index.html", "Engineering: issues and releases",
                         "The work on this site as files: issues with scenarios, mock-ups and outcomes, in open, blocked and done; the releases that carry them; every change connected to a card.",
                         body, eyebrow="Engineering", crumbs=(("About", "about/participant.html"),),
                         lead="What is asked, what is broken, what shipped, and in which release: one card per issue, as files in the repository, rendered here.",
                         agent=agent, head='<link rel="stylesheet" href="engineering.css">', wide=True)


def issue_page(i, releases):
    rel = next((r for r in releases if r.get("version") == i.get("release")), None)
    meta_rows = [("Id", i["id"]), ("Status", tag(i["status"], i["status"])), ("Kind", tag(KINDS.get(i.get("kind", ""), i.get("kind", "")), i.get("kind", ""))),
                 ("Priority", tag(i.get("priority", ""), i.get("priority", ""))), ("Created", esc(i.get("created", ""))), ("Source", esc(i.get("source", ""))),
                 ("Release", rel_link(i.get("release", ""), "../", {r.get("version") for r in releases}) if i.get("release") else "not planned yet"),
                 ("Effort", esc(i.get("estimated_effort", ""))), ("File", f'<code>{esc(i["path"])}</code>')]
    if i.get("blocked_on"):
        meta_rows.append(("Blocked on", esc(i["blocked_on"])))
    body_md = re.sub(r"^#\s+.*\n", "", i["body"], count=1)      # the title is the page's h1
    body = ('<table class="eng-meta">' + "".join(f'<tr><td class="k">{esc(k)}</td><td>{v}</td></tr>' for k, v in meta_rows) + "</table>"
            f'<div class="eng-body">{render(body_md)}</div>'
            '<p class="dim"><a href="../index.html">Back to the board</a>.</p>')
    agent = f"Issue {i['id']} on newsroom.sgit.ai: {i.get('title', '')}. Status {i['status']}, kind {i.get('kind', '')}, priority {i.get('priority', '')}, release {i.get('release') or 'unplanned'}. Source file {i['path']}."
    return newsroom_page(f"engineering/issues/{i['id']}.html", f"{i['id']}: {i.get('title', i['slug'])}",
                         f"Issue {i['id']} ({i.get('kind', '')}, {i['status']}): {i.get('title', '')}", body,
                         eyebrow=f"Engineering · {i['status']}", crumbs=(("About", "about/participant.html"), ("Engineering", "engineering/index.html")),
                         lead=i.get("title", ""), agent=agent, head='<link rel="stylesheet" href="../engineering.css">')


def release_page(r, issues):
    cards = [i for i in issues if i["id"] in r.get("issues", [])]
    missing = [x for x in r.get("issues", []) if x not in {i["id"] for i in issues}]
    if missing:
        raise SystemExit(f"engineering: release {r.get('version')} names cards that do not exist: {missing}")
    body_md = re.sub(r"^#\s+.*\n", "", r["body"], count=1)
    body = (f'<table class="eng-meta"><tr><td class="k">Version</td><td>{esc(r.get("version", ""))} · <a href="../../admin/versions.html#{esc(r.get("version", ""))}">the version row</a></td></tr>'
            f'<tr><td class="k">Date</td><td>{esc(r.get("date", ""))}</td></tr><tr><td class="k">Kind</td><td>{tag(r.get("kind", "patch"))}</td></tr>'
            f'<tr><td class="k">File</td><td><code>{esc(r["path"])}</code></td></tr></table>'
            f'<div class="eng-body">{render(body_md)}</div>'
            f'<h2 id="cards">The cards ({len(cards)})</h2><div class="eng-board">{issue_rows(cards, "../", {r["version"]})}</div>'
            '<p class="dim"><a href="../index.html">Back to the board</a>.</p>')
    agent = f"Release {r.get('version')} of newsroom.sgit.ai on {r.get('date')}: {len(cards)} card(s): {', '.join(i['id'] + ' ' + i.get('title', '') for i in cards)}."
    return newsroom_page(f"engineering/releases/{r['slug']}.html", f"{r.get('version', r['slug'])}: {first_heading(r['body']).split(':', 1)[-1].strip()}",
                         f"Release {r.get('version')}: the cards it carries and what it says.", body,
                         eyebrow="Engineering · release", crumbs=(("About", "about/participant.html"), ("Engineering", "engineering/index.html")),
                         lead=first_heading(r["body"]), agent=agent, head='<link rel="stylesheet" href="../engineering.css">')


def main():
    issues, releases = load_issues(), load_releases()
    changed = []
    if write("engineering/engineering.css", CSS):
        changed.append("engineering/engineering.css")
    if write("engineering/index.html", board(issues, releases)):
        changed.append("engineering/index.html")
    for i in issues:
        if write(f"engineering/issues/{i['id']}.html", issue_page(i, releases)):
            changed.append(f"engineering/issues/{i['id']}.html")
    for r in releases:
        if write(f"engineering/releases/{r['slug']}.html", release_page(r, issues)):
            changed.append(f"engineering/releases/{r['slug']}.html")
    index = {"what": "A derived index of the engineering cards on newsroom.sgit.ai; the files under admin/engineering/issues/ are the source.",
             "counts": {s: sum(1 for i in issues if i["status"] == s) for s in STATUSES},
             "issues": [{k: i.get(k, "") for k in ("id", "title", "kind", "priority", "status", "created", "release", "estimated_effort", "blocked_on", "path")} | {"url": f"https://{HOST}/engineering/issues/{i['id']}.html"} for i in issues],
             "releases": [{"version": r.get("version"), "date": r.get("date"), "kind": r.get("kind", "patch"), "issues": r.get("issues", []), "url": f"https://{HOST}/engineering/releases/{r['slug']}.html"} for r in releases]}
    if write("engineering/issues.json", json.dumps(index, indent=1, ensure_ascii=False) + "\n"):
        changed.append("engineering/issues.json")
    for i in issues:
        for m in re.finditer(r"\]\((\.\./shots/[^)]+)\)", i["body"]):
            if not (ROOT / "engineering/shots" / Path(m.group(1)).name).exists():
                print(f"engineering: {i['id']} refers to a screenshot not yet taken: {m.group(1)}")
    counts = ", ".join(f"{sum(1 for i in issues if i['status'] == s)} {s}" for s in STATUSES)
    print(f"engineering: {len(issues)} cards ({counts}), {len(releases)} release(s); {len(changed)} written")


if __name__ == "__main__":
    main()
