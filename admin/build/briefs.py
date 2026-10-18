#!/usr/bin/env python3
"""The briefs: every brief this site has published about itself, whether it is built, and where to start.

    python3 admin/build/briefs.py            write briefs/index.html and briefs/briefs.json from admin/content/briefs.json
    python3 admin/build/briefs.py --check    check the map (ids unique, dependencies exist, statuses known), write nothing

The map is admin/content/briefs.json: one entry per thing to build, with its sources (articles, notes, cards), its
status as found in the code and the releases (built, partly, not built, superseded), what is built and what remains,
and a session brief an agent can start a session from. An entry's status changes in the release that ships it. The
page groups the entries by area, puts what is open first, and links every source.
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from page import newsroom_page, write, esc, HOST  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "admin/content/briefs.json"
STATUS = {"not built": "Not built", "partly": "Partly built", "built": "Built", "superseded": "Superseded"}
ORDER = {"not built": 0, "partly": 1, "superseded": 2, "built": 3}
AREAS = {
    "reader-features": "Reader features", "reading-account-and-vault": "The reading account and the vault",
    "search-and-graphs": "Search and graphs", "quality-and-review": "Quality and review",
    "editorial-workflow": "Editorial workflow", "wires": "The wires", "agents-and-authors": "Agents and authors",
    "payments": "Payments", "publishing-method": "The publishing method", "other": "Other",
}


def txt(v):
    """A field as text: some entries list their parts."""
    return "; ".join(str(x).rstrip(".") for x in v) + "." if isinstance(v, list) else (v or "")


def check(d):
    errs = []
    ids = [b["id"] for b in d["briefs"]]
    for i, n in Counter(ids).items():
        if n > 1:
            errs.append(f"id {i} appears {n} times")
    for b in d["briefs"]:
        if b["status"] not in STATUS:
            errs.append(f"{b['id']}: unknown status {b['status']!r}")
        if b["area"] not in AREAS:
            errs.append(f"{b['id']}: unknown area {b['area']!r}")
        for x in b.get("depends_on") or []:
            if x not in ids:
                errs.append(f"{b['id']}: depends on unknown {x!r}")
        if b["status"] != "built" and b["status"] != "superseded" and not txt(b.get("session_brief")).strip():
            errs.append(f"{b['id']}: open, but no session brief")
    return errs


def source_link(s, up):
    m = re.match(r"([a-z0-9-]+)(\s.*)?$", s)
    if m and (ROOT / "articles" / f"{m.group(1)}.html").exists():
        return f'<a href="{up}articles/{m.group(1)}.html">{esc(m.group(1))}</a>{esc(m.group(2) or "")}'
    m = re.match(r"(admin/notes/[^\s]+\.md)(\s.*)?$", s)
    if m and (ROOT / m.group(1)).exists():
        return f'<a href="https://{HOST}/{m.group(1)}">{esc(Path(m.group(1)).stem)}</a>{esc(m.group(2) or "")}'
    return esc(s)


def main():
    d = json.loads(SRC.read_text(encoding="utf-8"))
    errs = check(d)
    for e in errs:
        print("briefs: ERROR", e)
    if errs:
        sys.exit(1)
    briefs = d["briefs"]
    st = Counter(b["status"] for b in briefs)
    print(f"briefs: {len(briefs)} entries; " + ", ".join(f"{STATUS[k].lower()} {st.get(k, 0)}" for k in STATUS))
    if "--check" in sys.argv:
        return
    up = "../"
    by_id = {b["id"]: b for b in briefs}
    counts = "".join(
        f'<tr><td><a href="#{a}">{esc(AREAS[a])}</a></td><td class="num">{sum(1 for b in briefs if b["area"] == a)}</td>'
        f'<td class="num">{sum(1 for b in briefs if b["area"] == a and b["status"] in ("not built", "partly"))}</td></tr>'
        for a in AREAS if any(b["area"] == a for b in briefs))
    parts = []
    for a in AREAS:
        items = sorted((b for b in briefs if b["area"] == a), key=lambda b: (ORDER[b["status"]], b["date"]))
        if not items:
            continue
        parts.append(f'<h2 id="{a}">{esc(AREAS[a])}</h2>')
        for b in items:
            deps = ", ".join(f'<a href="#{esc(x)}">{esc(by_id[x]["title"].split(":")[0])}</a>' for x in b.get("depends_on") or [])
            src = "; ".join(source_link(s, up) for s in b["source"])
            body = [f'<p class="dim">Size {esc(b.get("size", ""))} &middot; first briefed {esc(b["date"])} &middot; {src}</p>',
                    f'<p><b>Asked.</b> {esc(txt(b["asked"]))}</p>']
            if b.get("built"):
                body.append(f'<p><b>Built.</b> {esc(txt(b["built"]))}</p>')
            if b.get("remaining"):
                r = b["remaining"]
                body.append('<p><b>Remaining.</b></p><ul>' + "".join(f"<li>{esc(x)}</li>" for x in r) + '</ul>' if isinstance(r, list)
                            else f'<p><b>Remaining.</b> {esc(r)}</p>')
            if deps:
                body.append(f'<p><b>Needs first.</b> {deps}</p>')
            if b.get("session_brief") and b["status"] in ("not built", "partly"):
                body.append(f'<div class="bf-brief"><p class="bf-k">Session brief</p><p>{esc(txt(b["session_brief"]))}</p></div>')
            parts.append(f'<section class="bf-item bf-{b["status"].replace(" ", "-")}" id="{esc(b["id"])}">'
                         f'<h3>{esc(b["title"])} <span class="pill">{esc(STATUS[b["status"]])}</span></h3>' + "".join(body) + '</section>')
    html = f"""<p class="lead">Every brief this site has published about itself, from its articles, its notes and its engineering cards, with whether it is built, what remains, and a session brief an agent can start from.</p>
<p>{len(briefs)} briefs: {st.get("not built", 0)} not built, {st.get("partly", 0)} partly built, {st.get("built", 0)} built, {st.get("superseded", 0)} superseded. Status is taken from the code, the releases, the cards and the notes, not from what the articles say about themselves; first audited {esc(d["audited"])}. Each entry changes in the release that ships it. Why this exists: <a href="{up}articles/the-briefs-so-far.html">the briefs so far</a>.</p>
<div class="tbl"><table><thead><tr><th>Area</th><th>Briefs</th><th>Open</th></tr></thead><tbody>{counts}</tbody></table></div>
<p class="dim">Open is not built or partly built. Within each area, open briefs come first, oldest first. Data: <a href="briefs.json">briefs.json</a>.</p>
{"".join(parts)}
<style>
.bf-item{{border:1px solid var(--line);border-radius:10px;padding:.8rem 1rem;margin:.9rem 0;background:var(--panel);min-width:0}}
.bf-item h3{{margin:.1rem 0 .4rem;font-size:1.05rem}} .bf-item p{{margin:.4rem 0}} .bf-item p,.bf-item li{{overflow-wrap:anywhere}}
.bf-built,.bf-superseded{{opacity:.75}}
.bf-brief{{border-left:3px solid var(--accent, #0f766e);padding:.2rem .8rem;margin:.6rem 0 .2rem}} .bf-k{{font-size:.78rem;text-transform:uppercase;letter-spacing:.05em;color:var(--muted, #6b6b6b)}}
.tbl{{overflow-x:auto}} td.num{{text-align:right;font-variant-numeric:tabular-nums}}
</style>"""
    agent = (f"The map of every brief newsroom.sgit.ai has published about itself: {len(briefs)} entries, {st.get('not built', 0)} not built and "
             f"{st.get('partly', 0)} partly built, each with a session brief to start from. Machine-readable: https://{HOST}/briefs/briefs.json.")
    w = write("briefs/index.html", newsroom_page("briefs/index.html", "The briefs", "Every brief this site has published about itself, whether it is built, and where to start.",
                                                html, eyebrow="How it runs", agent=agent))
    (ROOT / "briefs" / "briefs.json").write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"briefs: page {'written' if w else 'unchanged'}")


if __name__ == "__main__":
    main()
