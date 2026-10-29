#!/usr/bin/env python3
"""The team: every person, agent, scheduled run and independent reviewer that works on this site, one page each (card 094).

    python3 admin/build/team.py            write team/ (the roster, a page and a markdown twin per member, policies.json)
    python3 admin/build/team.py --check    only the checks; exit 1 on an error

The data is admin/content/team.json (the roster) and, for each member, admin/content/agents/<id>/ROLE.md (what it is, when
it has failed, the rules it works by), policy.json (the files it alone writes, the vaults it may hold) and, where an
agent is being handed over, HANDOVER.md. The pages are drawn from them, the way the PHP story site's team pages are
(php.oct.2026.newsroom.sgit.ai), so a new agent is a row, a role file and a policy, and the counts follow.

Checks, on every build: every member has a role file and a policy whose id is its own; no tracked file is claimed by two
members' `writes` (less `writes_except`); and the files nobody owns are counted, by directory, so the gap is visible.
A policy is a draft until the editor agrees it (`agreed_by_editor`); the page says how many are.
"""
import argparse
import fnmatch
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from md import render  # noqa: E402
from page import esc, newsroom_page, write, HOST  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "admin/content/team.json"
AGENTS = ROOT / "admin/content/agents"
KIND = {"human": "a person", "agent": "an agent", "scheduled": "scheduled runs", "reviewer": "an independent reviewer"}
STATUS = {"active": "active", "idle": "idle between pieces of work", "planned": "planned, not started", "starting": "starting now", "registered": "registered, not started", "occasional": "runs when the editor asks"}
SOURCE_ROOTS = ("admin/build/", "admin/content/", "assets/")
SOURCE_SKIP = ("assets/vendor/", "assets/components/", "admin/build/__pycache__/")


def rx(pattern):
    """A glob as a regular expression: ** crosses directories, * and ? do not."""
    out, i = "", 0
    while i < len(pattern):
        c = pattern[i]
        if pattern[i:i + 3] == "**/":
            out += "(?:.*/)?"; i += 3; continue
        if pattern[i:i + 2] == "**":
            out += ".*"; i += 2; continue
        out += "[^/]*" if c == "*" else "[^/]" if c == "?" else re.escape(c)
        i += 1
    return re.compile("^" + out + "$")


def own_files(m):
    """A member keeps its own role file and handover; its policy is the editor's (dinis-cruz writes every policy.json)."""
    return [f"admin/content/agents/{m['id']}/ROLE.md", f"admin/content/agents/{m['id']}/HANDOVER.md"]


def tracked():
    r = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True)
    return r.stdout.splitlines() if r.returncode == 0 else []


def load():
    team = json.loads(DATA.read_text(encoding="utf-8"))
    for m in team["members"]:
        d = AGENTS / m["id"]
        m["role_md"] = (d / "ROLE.md").read_text(encoding="utf-8") if (d / "ROLE.md").exists() else None
        m["handover_md"] = (d / "HANDOVER.md").read_text(encoding="utf-8") if (d / "HANDOVER.md").exists() else None
        m["policy"] = json.loads((d / "policy.json").read_text(encoding="utf-8")) if (d / "policy.json").exists() else None
    return team


def check(team):
    errors, owners = [], {}
    ids = [m["id"] for m in team["members"]]
    if len(set(ids)) != len(ids):
        errors.append("a member id is used twice")
    groups = {g["id"] for g in team["groups"]}
    for m in team["members"]:
        if m["group"] not in groups:
            errors.append(f"{m['id']}: group {m['group']!r} is not in the roster's groups")
        if m["role_md"] is None:
            errors.append(f"{m['id']}: no admin/content/agents/{m['id']}/ROLE.md")
        if m["policy"] is None:
            errors.append(f"{m['id']}: no admin/content/agents/{m['id']}/policy.json")
        elif m["policy"].get("id") != m["id"]:
            errors.append(f"{m['id']}: its policy.json says id {m['policy'].get('id')!r}")
    files = tracked()
    matchers = {m["id"]: ([rx(p) for p in m["policy"].get("writes", []) + own_files(m)], [rx(p) for p in m["policy"].get("writes_except", [])]) for m in team["members"] if m["policy"]}
    for f in files:
        for mid, (w, x) in matchers.items():
            if any(r.match(f) for r in w) and not any(r.match(f) for r in x):
                owners.setdefault(f, []).append(mid)
    overlaps = {f: o for f, o in owners.items() if len(o) > 1}
    for f, o in sorted(overlaps.items())[:40]:
        errors.append(f"{f} is written by {' and '.join(o)}")
    if len(overlaps) > 40:
        errors.append(f"... and {len(overlaps) - 40} more overlapping files")
    source = [f for f in files if f.startswith(SOURCE_ROOTS) and not f.startswith(SOURCE_SKIP)]
    unowned = [f for f in source if f not in owners]
    by_dir = {}
    for f in unowned:
        k = "/".join(f.split("/")[:3])
        by_dir[k] = by_dir.get(k, 0) + 1
    return errors, {"owned": len(owners), "overlaps": len(overlaps), "source_files": len(source), "unowned": len(unowned),
                    "unowned_by_dir": dict(sorted(by_dir.items(), key=lambda kv: -kv[1])[:12]), "owners": owners}


def initials(name):
    w = re.findall(r"[A-Za-z0-9]+", name.replace("@", "").replace("newsroom.", ""))
    return ("".join(x[0] for x in w[:2]) or "?").upper()


def link_to(m, up="../"):
    return f'<a href="{up}team/{esc(m["id"])}.html">{esc(m["handle"])}</a>'


def card_links(cards, up="../"):
    return ", ".join(f'<a href="{up}engineering/issues/{esc(c)}.html">{esc(c)}</a>' for c in cards) or "none recorded"


def code_list(items, empty="none"):
    return "<br>".join(f"<code>{esc(x)}</code>" for x in items) if items else empty


def member_page(team, m, stats):
    p = m["policy"] or {}
    g = next(x for x in team["groups"] if x["id"] == m["group"])
    owned = sorted(f for f, o in stats["owners"].items() if m["id"] in o)
    byline = f'<a href="../{esc(m["byline"])}">{esc(m["byline"])}</a>' if m.get("byline") else "none (it writes no articles under this name)"
    agreed = "agreed by the editor" if p.get("agreed_by_editor") else "a draft: not yet agreed by the editor"
    rows = [("Kind", KIND[m["kind"]]), ("Status", STATUS.get(m["status"], m["status"])), ("Group", f'<a href="index.html#{esc(g["id"])}">{esc(g["title"])}</a>'),
            ("Since", esc(m["since"] or "not started")), ("Byline page", byline), ("Cards", card_links(m["cards"]))]
    table = "".join(f'<tr><td class="k">{k}</td><td>{v if k in ("Group", "Byline page", "Cards") else esc(v)}</td></tr>' for k, v in rows)
    scope = f"""<h2 id="scope">What it writes, and what it may hold</h2>
<p>Its policy, {esc(agreed)}. {esc(p.get('note', ''))}</p>
<table class="eng-meta">
<tr><td class="k">Writes (it alone)</td><td>{code_list(p.get('writes', []), 'no files in this repository')}</td></tr>
<tr><td class="k">Except</td><td>{code_list(p.get('writes_except', []))}</td></tr>
<tr><td class="k">Appends to</td><td>{code_list(p.get('appends', []))}</td></tr>
<tr><td class="k">May hold</td><td>{code_list(p.get('vaults_may_hold', []), 'nothing')}</td></tr>
<tr><td class="k">Never holds</td><td>{code_list(p.get('never_holds', []), 'nothing named')}</td></tr>
<tr><td class="k">Files it owns now</td><td>{len(owned)} tracked file(s){' (the build checks that no other member claims one)' if owned else ''}</td></tr>
</table>
<p class="dim">The policy is <a href="../admin/content/agents/{esc(m['id'])}/policy.json">policy.json</a>; <a href="{esc(m['id'])}.md">this page as markdown</a>.</p>"""
    handover = ""
    if m["handover_md"]:
        handover = '<h2 id="handover">Handover</h2>\n' + render(re.sub(r"^# .*\n", "", m["handover_md"], count=1))
    body = f"""<p class="lead">{esc(m['line'])}</p>
<table class="eng-meta">{table}</table>
<h2 id="role">The role</h2>
{render(m['role_md'] or '')}
{scope}
{handover}
<p><a href="index.html">&larr; The whole team</a></p>"""
    agent = (f"{m['handle']} is {KIND[m['kind']]} on newsroom.sgit.ai ({STATUS.get(m['status'], m['status'])}). Role and policy as data: admin/content/agents/{m['id']}/ROLE.md and policy.json; "
             f"the roster is admin/content/team.json and every policy is at https://{HOST}/team/policies.json. This page as markdown: https://{HOST}/team/{m['id']}.md.")
    return newsroom_page(f"team/{m['id']}.html", f"{m['handle']}: {m['name'] if m['name'].lstrip('@') != m['handle'].lstrip('@') else KIND[m['kind']]}"[:90],
                         f"{m['handle']} on newsroom.sgit.ai: {m['line']}", body, eyebrow=f"Team &middot; {esc(g['title'])}",
                         crumbs=(("Team", "team/index.html"),), agent=agent, head='<link rel="stylesheet" href="../engineering/engineering.css">\n')


def index_page(team, stats, errors):
    ms = team["members"]
    kinds = {k: sum(1 for m in ms if m["kind"] == k) for k in KIND}
    agreed = sum(1 for m in ms if (m["policy"] or {}).get("agreed_by_editor"))
    active = sum(1 for m in ms if m["status"] == "active")
    parts = []
    for g in team["groups"]:
        rows = ""
        for m in (x for x in ms if x["group"] == g["id"]):
            rows += (f'<tr><td><span class="tchip">{esc(initials(m["name"]))}</span></td><td><b>{link_to(m, "../")}</b><br><span class="dim">{esc(KIND[m["kind"]])}</span></td>'
                     f'<td>{esc(m["line"])}</td><td>{esc(STATUS.get(m["status"], m["status"]))}</td></tr>')
        parts.append(f'<h3 id="{esc(g["id"])}">{esc(g["title"])}</h3><p class="dim">{esc(g["about"])}</p>'
                     f'<div class="tablewrap"><table><thead><tr><th></th><th>Member</th><th>What it does</th><th>Status</th></tr></thead><tbody>{rows}</tbody></table></div>')
    related = "".join(f'<li><a href="{esc(r["url"] if r["url"].startswith("http") else "../" + r["url"])}">{esc(r["title"])}</a>: {esc(r["about"])}</li>' for r in team.get("related", []))
    gaps = ", ".join(f"<code>{esc(d)}</code> {n}" for d, n in stats["unowned_by_dir"].items())
    body = f"""<p class="lead">This site is run by one editor and a team of agents, with independent reviewers from other vendors checking the work. Every member has a page: what it is, when it has failed, the rules it works by, the files it alone writes, and the keys it may and may not hold.</p>
<p>{len(ms)} members: {kinds['human']} person, {kinds['agent']} agents, {kinds['scheduled']} set of scheduled runs and {kinds['reviewer']} independent reviewers; {active} active. The roster is data: <a href="../admin/content/team.json">team.json</a>, with a <code>ROLE.md</code> and a <code>policy.json</code> for each.</p>
<h2 id="members">Who is on it</h2>
{''.join(parts)}
<h2 id="related">Other teams</h2>
<ul>{related}</ul>
<h2 id="kept">How it is kept true</h2>
<p>Each member's <code>policy.json</code> lists the files it alone writes. On every build, <code>admin/build/team.py</code> checks them against every tracked file: <b>{stats['overlaps']} files are claimed by two members</b> (the build fails if there is one). {stats['unowned']} of {stats['source_files']} source files (the builders, the content and the assets) belong to nobody{(': ' + gaps) if gaps else ''}. <b>{agreed} of {len(ms)} policies are agreed by the editor</b>; the rest are drafts, written by @newsroom.dev from each member's commits, cards and builders on 28 October 2026, so they say what the work shows, not what anyone was told to do. Where a draft is wrong, the editor corrects <code>policy.json</code> and the build re-checks it.</p>
<p>A new agent is a row in the roster, a role file and a policy; the pages, the counts and the checks follow. Independent review has its own section: <a href="../reviews/index.html">how outside reviewers check the newsroom</a>, with <a href="../reviews/vaults.html">their vaults and keys</a>.</p>"""
    agent = (f"The roster: https://{HOST}/team/policies.json (members, their policies, the overlap check and the unowned-file count) and admin/content/team.json. "
             f"One page per member at https://{HOST}/team/&lt;id&gt;.html and as markdown at /team/&lt;id&gt;.md. To add a member: a row in team.json and admin/content/agents/&lt;id&gt;/ROLE.md and policy.json, then python3 admin/build/team.py.")
    return newsroom_page("team/index.html", "The team", "Who works on newsroom.sgit.ai: the editor, the agents, the scheduled runs and the independent reviewers, each with a role, a policy and the keys it may hold.",
                         body, eyebrow="How it runs", lead="", crumbs=(), agent=agent, head='<link rel="stylesheet" href="../engineering/engineering.css">\n')


def md_of(m):
    out = [f"# {m['handle']}", "", f"*{KIND[m['kind']]}; {STATUS.get(m['status'], m['status'])}. {m['line']}*", "", m["role_md"] or ""]
    if m["handover_md"]:
        out += ["", m["handover_md"]]
    return "\n".join(out).strip() + "\n"


def build():
    team = load()
    errors, stats = check(team)
    for e in errors:
        print("team: ERROR", e)
    if errors:
        sys.exit(1)
    out = ROOT / "team"
    out.mkdir(exist_ok=True)
    for f in out.glob("*.md"):
        f.unlink()
    write("team/index.html", index_page(team, stats, errors))
    for m in team["members"]:
        write(f"team/{m['id']}.html", member_page(team, m, stats))
        (out / f"{m['id']}.md").write_text(md_of(m), encoding="utf-8")
    pol = {"what": "Every member's policy, the overlap check and the count of files nobody owns, as build.py found them. Written by admin/build/team.py.",
           "overlaps": stats["overlaps"], "source_files": stats["source_files"], "unowned": stats["unowned"], "unowned_by_dir": stats["unowned_by_dir"],
           "agreed_by_editor": sum(1 for m in team["members"] if (m["policy"] or {}).get("agreed_by_editor")),
           "members": [{k: m[k] for k in ("id", "handle", "name", "kind", "group", "status", "line", "since", "cards")} | {"policy": m["policy"]} for m in team["members"]]}
    (out / "policies.json").write_text(json.dumps(pol, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"team: {len(team['members'])} members; {stats['overlaps']} overlapping file(s); {stats['unowned']} of {stats['source_files']} source files unowned")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    if a.check:
        errors, stats = check(load())
        for e in errors:
            print("team: ERROR", e)
        print(f"team: {stats['overlaps']} overlap(s), {stats['unowned']} of {stats['source_files']} source files unowned")
        sys.exit(1 if errors else 0)
    build()


if __name__ == "__main__":
    main()
