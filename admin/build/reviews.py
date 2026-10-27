#!/usr/bin/env python3
"""Reviews on the record: every review of every article, by agents, the editor, journalists and later readers.

    python3 admin/build/reviews.py                          build reviews/ (the hub, the criteria, status.json, the
                                                            records) and the Reviews section on each article page
    python3 admin/build/reviews.py --check                  validate every record; exit 1 on an error
    python3 admin/build/reviews.py --next ID [--batch 5] [--shard i/n]
                                                            the next articles reviewer ID has not reviewed at their
                                                            current text, newest first
    python3 admin/build/reviews.py --stamp                  fill a record's missing article_hash from the current text
    python3 admin/build/reviews.py --new ID SLUG            print an empty record for ID and SLUG, ready to fill

The criteria are admin/content/reviews/criteria.md, published as reviews/criteria.md and reviews/criteria.html. A
review is one file, admin/content/articles/reviews/<slug>/<YYYY-MM-DD>__<reviewer>.json, written once by its
reviewer and never edited; the newsroom answers its findings in reviews/<slug>/status.json, which only the newsroom
writes. One writer per file, so parallel reviewers and pull requests never conflict.

An article's text is identified by `hash`: the first 12 hex characters of the SHA-256 of its sections' text, read
the way admin/build/summaries.py reads them (main, up to the meter, without the threads and without the Reviews
section this script adds). A review whose hash is not the current one reviewed an earlier text; it stays on the
page, marked so. The unit of work is (reviewer, slug, hash): a reviewer never gets the same article at the same
text twice.
"""
import argparse
import hashlib
import html
import json
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from md import render  # noqa: E402
from page import newsroom_page, write  # noqa: E402
from summaries import sections_of  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "admin/content/articles/reviews"
CRIT = ROOT / "admin/content/reviews/criteria.md"
REG = ROOT / "admin/content/reviews/reviewers.json"
OUT = ROOT / "reviews"
CRITERIA = "v1.2"
VERDICTS = {"approve": "Approve", "approve-with-changes": "Approve, with changes", "changes-needed": "Changes needed", "comment": "Comment"}
KINDS = ("agent", "editor", "journalist", "reader")
CRITERIA_KEYS = ("facts", "voice", "claims", "conversions", "health", "people")
RESULTS = ("pass", "issues", "not-checked")
SEVERITIES = ("high", "medium", "low")
STATUSES = ("open", "fixed", "declined")
VERIFICATION = ("contradicted", "unsupported", "inconsistent", "overstated", "unverifiable", "stale", "style")  # v1.2; assets/reviews/record.js
NAME = re.compile(r"^(\d{4}-\d{2}-\d{2})__([a-z0-9][a-z0-9.-]*)(__\d+)?\.json$")
e = html.escape


def articles():
    """The site's articles, newest first: [{n, slug, title, date, version, hash}]."""
    ids = json.loads((ROOT / "articles/ids.json").read_text(encoding="utf-8"))["articles"]
    out = []
    for a in ids:
        secs = sections_of(a["slug"])
        if not secs:
            continue
        page = (ROOT / "articles" / f"{a['slug']}.html").read_text(encoding="utf-8")
        v = re.search(r'release it was published in">(?:newsroom )?(v[0-9.]+)</a>', page)
        av = re.search(r'>article (v\d+\.\d+\.\d+)\b', page)
        text = "\n".join(f"{sid}\n{t}" for sid, _, t in secs)
        out.append({"n": a["n"], "slug": a["slug"], "title": a["title"], "date": a["date"],
                    "version": v.group(1) if v else None, "aversion": av.group(1) if av else None,
                    "hash": hashlib.sha256(text.encode("utf-8")).hexdigest()[:12],
                    "text": " ".join(t for _, _, t in secs)})
    out.sort(key=lambda a: (a["date"], a["n"]), reverse=True)
    return out


def reviewers():
    return json.loads(REG.read_text(encoding="utf-8"))["reviewers"] if REG.exists() else []


def records():
    """Every record: [(path, data)], and every status file: {slug: data}."""
    recs, status = [], {}
    if not SRC.exists():
        return recs, status
    for d in sorted(p for p in SRC.iterdir() if p.is_dir()):
        for f in sorted(d.glob("*.json")):
            data = json.loads(f.read_text(encoding="utf-8"))
            if f.name == "status.json":
                status[d.name] = data
            else:
                recs.append((f, data))
    return recs, status


def norm(s):
    return re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')).strip()


def check(arts=None):
    arts = arts or articles()
    by = {a["slug"]: a for a in arts}
    ids = {r["id"] for r in reviewers()}
    recs, status = records()
    errors, warnings, seen = [], [], {}
    for f, r in recs:
        rel = f.relative_to(ROOT)
        m = NAME.match(f.name)
        say = lambda msg: errors.append(f"{rel}: {msg}")  # noqa: E731
        if not m:
            say("file name is not <YYYY-MM-DD>__<reviewer>.json"); continue
        if r.get("schema") != "newsroom-review/v1":
            say("schema is not newsroom-review/v1")
        if r.get("slug") != f.parent.name or f.parent.name not in by:
            say(f"slug {r.get('slug')!r} does not match its folder or is not an article")
        if r.get("reviewer") != m.group(2):
            say("reviewer does not match the file name")
        elif r["reviewer"] not in ids:
            warnings.append(f"{rel}: reviewer {r['reviewer']} is not registered in admin/content/reviews/reviewers.json")
        if r.get("kind") not in KINDS:
            say(f"kind must be one of {', '.join(KINDS)}")
        if r.get("verdict") not in VERDICTS:
            say(f"verdict must be one of {', '.join(VERDICTS)}")
        if not re.fullmatch(r"[0-9a-f]{12}", r.get("article_hash") or ""):
            say("article_hash missing (run --stamp straight after writing the record)")
        for k, c in (r.get("checks") or {}).items():
            if k not in CRITERIA_KEYS or (c or {}).get("result") not in RESULTS:
                say(f"check {k!r} is not one of the criteria or has no valid result")
        a = by.get(r.get("slug"))
        fids = set()
        for x in r.get("findings") or []:
            fid = x.get("id")
            if not fid or fid in fids:
                say(f"finding without a unique id: {fid!r}")
            fids.add(fid)
            if x.get("severity") not in SEVERITIES or x.get("criterion") not in CRITERIA_KEYS:
                say(f"finding {fid}: severity or criterion not valid")
            if not (x.get("issue") or "").strip():
                say(f"finding {fid}: no issue")
            if x.get("verification") is not None and x["verification"] not in VERIFICATION:
                say(f"finding {fid}: verification must be one of {', '.join(VERIFICATION)}")
            q = (x.get("quote") or "").strip()
            if q and a and r.get("article_hash") == a["hash"] and norm(q) not in norm(a["text"]):
                warnings.append(f"{rel}: finding {fid}: quote not found in the current text: {q[:80]!r}")
        key = (r.get("reviewer"), r.get("slug"), r.get("article_hash"))
        if key in seen and r.get("kind") == "agent":
            say(f"a second review of the same text by the same reviewer (first: {seen[key]})")
        seen.setdefault(key, rel)
    for slug, st in status.items():
        for ref, s in (st.get("findings") or {}).items():
            if s.get("status") not in STATUSES:
                errors.append(f"admin/content/articles/reviews/{slug}/status.json: {ref}: status must be one of {', '.join(STATUSES)}")
    return errors, warnings


def release():
    return (ROOT / "admin/build/version.txt").read_text(encoding="utf-8").strip()


def stamp():
    by = {a["slug"]: a for a in articles()}
    n = 0
    # an answer marked fixed in this release gets the article version that carries the fix, so the version pages can
    # credit the review long after this release
    rel, (_, status) = release(), records()
    for slug, st in status.items():
        a = by.get(slug)
        hit = 0
        for s in (st.get("findings") or {}).values():
            if a and a.get("aversion") and s.get("status") == "fixed" and s.get("in") == rel and not s.get("article"):
                s["article"] = a["aversion"]; hit += 1
        if hit:
            (SRC / slug / "status.json").write_text(json.dumps(st, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
            n += hit
    for f, r in records()[0]:
        if not r.get("article_hash") and r.get("slug") in by:
            r["article_hash"] = by[r["slug"]]["hash"]
            r.setdefault("article_version", by[r["slug"]]["version"])
            f.write_text(json.dumps(r, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
            n += 1
    print(f"reviews: {n} record(s) stamped")


def next_batch(rid, batch, shard):
    arts = articles()
    done = {}
    for _, r in records()[0]:
        if r.get("reviewer") == rid:
            done.setdefault(r["slug"], set()).add(r.get("article_hash"))
    never = [a for a in arts if a["slug"] not in done]
    stale = [a for a in arts if a["slug"] in done and a["hash"] not in done[a["slug"]]]
    queue = never + stale
    if shard:
        i, k = (int(x) for x in shard.split("/"))
        queue = [a for j, a in enumerate(queue) if j % k == i - 1]
    for a in queue[:batch]:
        state = "never reviewed" if a in never else "text changed since your review"
        print(f"{a['slug']}\t{a['version']}\t{a['hash']}\t{state}\thttps://newsroom.sgit.ai/articles/{a['slug']}.md")
    print(f"# {len(never)} never reviewed by {rid}, {len(stale)} changed since; showing {min(batch, len(queue))}", file=sys.stderr)


def skeleton(rid, slug):
    a = {x["slug"]: x for x in articles()}[slug]
    r = {"schema": "newsroom-review/v1", "criteria": CRITERIA, "slug": slug, "article_version": a["version"],
         "article_hash": a["hash"], "reviewer": rid, "kind": "agent", "model": "", "run_by": "", "at": "",
         "verdict": "", "summary": "", "checks": {k: {"result": "not-checked", "notes": ""} for k in CRITERIA_KEYS},
         "findings": []}
    print(json.dumps(r, indent=1, ensure_ascii=False))


# ---------- the pages ----------

CURRENT = {}  # slug: the article version in this build, for answers fixed in this release and not stamped yet


def answers(status, slug, fname):
    st = (status.get(slug) or {}).get("findings") or {}
    out = {ref.split("#", 1)[1]: s for ref, s in st.items() if ref.split("#", 1)[0] == fname}
    rel = release()
    for s in out.values():
        if s.get("status") == "fixed" and not s.get("article") and s.get("in") == rel and CURRENT.get(slug):
            s["article"] = CURRENT[slug]
    return out


def tally(r, ans):
    t = {"open": 0, "fixed": 0, "declined": 0}
    for x in r.get("findings") or []:
        t[(ans.get(x["id"]) or {}).get("status", "open")] += 1
    return t


def who(r, regs):
    reg = regs.get(r.get("reviewer")) or {}
    return reg.get("name") or r.get("reviewer")


PEOPLE = ("editor", "journalist", "reader")


def standing(a, revs, status, regs):
    """Where an article stands in peer review: who has read which text, what they said, and what is still open.
    Counts, not a score: a reader can see how many fresh looks the current text has had, by agents and by people."""
    cur = [(f, r) for f, r in revs if r.get("article_hash") == a["hash"]]
    old = [(f, r) for f, r in revs if r.get("article_hash") != a["hash"]]
    names = lambda rs: sorted({who(r, regs) for _, r in rs})  # noqa: E731
    agents = names([x for x in cur if x[1].get("kind") == "agent"])
    people = names([x for x in cur if x[1].get("kind") in PEOPLE])
    t = {"open": 0, "fixed": 0, "declined": 0}
    for f, r in revs:
        for k, v in tally(r, answers(status, a["slug"], f.name)).items():
            t[k] += v
    against = [who(r, regs) for _, r in cur if r.get("verdict") == "changes-needed"]
    if not revs:
        label, cls = "Not reviewed yet", "none"
    elif against or t["open"]:
        label, cls = (f"Disputed: {', '.join(against)} asked for changes" if against else f"{t['open']} finding{'s' if t['open'] != 1 else ''} open"), "open"
    elif not cur:
        label, cls = "Corrected after review; this text not yet re-read", "stale"
    elif people and agents:
        label, cls = "Checked by agents and people", "both"
    elif people:
        label, cls = "Checked by people", "people"
    else:
        label, cls = f"Checked by {len(agents)} agent{'s' if len(agents) != 1 else ''}; no person yet", "agents"
    return {"label": label, "cls": cls, "agents": agents, "people": people, "earlier": names(old), "tally": t,
            "fresh": len({r.get("reviewer") for _, r in cur}), "all": len({r.get("reviewer") for _, r in revs})}


def strip_html(a, s, up):
    if not s["all"]:
        return (f'<p class="rvstatus rv-none"><span class="rv-k">Peer review</span> Not reviewed yet. '
                f'<a href="{up}reviews/criteria.html">Review it</a></p>')
    bits = [f'<b>{e(s["label"])}</b>']
    on = []
    if not s["fresh"]:
        on.append("no review yet")
    if s["agents"]:
        on.append(f'{len(s["agents"])} agent{"s" if len(s["agents"]) != 1 else ""} ({e(", ".join(s["agents"]))})')
    if s["fresh"]:
        on.append(f'{len(s["people"])} {"person" if len(s["people"]) == 1 else "people"}' + (f' ({e(", ".join(s["people"]))})' if s["people"] else ""))
    bits.append("this text: " + ", ".join(on))
    if s["earlier"]:
        bits.append("earlier texts: " + e(", ".join(s["earlier"])))
    t = s["tally"]
    n = sum(t.values())
    if n:
        bits.append(f'{n} finding{"s" if n != 1 else ""}: ' + ", ".join(f"{v} {k}" for k, v in t.items() if v))
    return (f'<p class="rvstatus rv-{s["cls"]}"><span class="rv-k">Peer review</span> ' + " &middot; ".join(bits)
            + ' &middot; <a href="#reviews">the reviews</a></p>')


def review_li(a, f, r, status, regs, up):
    ans = answers(status, a["slug"], f.name)
    t = tally(r, ans)
    current = r.get("article_hash") == a["hash"]
    n = len(r.get("findings") or [])
    fsum = "no findings" if not n else f"{n} finding{'s' if n != 1 else ''}: " + ", ".join(f"{v} {k}" for k, v in t.items() if v)
    fixed_in = sorted({s["article"] for s in ans.values() if s.get("status") == "fixed" and s.get("article")})
    if current:
        note = ' <span class="tchip">this text</span>'
    else:
        note = ' <span class="dim">(an earlier text' + (f'; answered in <a href="{up}articles/versions/{e(a["slug"])}/{e(fixed_in[-1])}.html">article {e(fixed_in[-1])}</a>' if fixed_in else "") + ')</span>'
    model = f' <span class="dim">{e(r.get("model"))}</span>' if r.get("kind") == "agent" and r.get("model") and r["model"] not in who(r, regs) else ""
    return (f'<li><b>{e(who(r, regs))}</b>{model} <span class="tchip">{e(r.get("kind", ""))}</span> '
            f'{e(VERDICTS.get(r.get("verdict"), ""))}, {e((r.get("at") or "")[:10])}, at newsroom {e(r.get("article_version") or "")}{note}. '
            f'{e(r.get("summary") or "")} <span class="dim">{e(fsum)}.</span> '
            f'<a href="{up}reviews/records/{e(a["slug"])}/{e(f.name)}">The record</a></li>')


def section_html(a, revs, status, regs, up):
    s = standing(a, revs, status, regs)
    people = [x for x in revs if x[1].get("kind") in PEOPLE]
    agents = [x for x in revs if x[1].get("kind") not in PEOPLE]
    parts = []
    if revs:
        parts.append(f'<p><b>{e(s["label"])}.</b> This text has had {s["fresh"]} fresh look{"s" if s["fresh"] != 1 else ""}; '
                     f'the article, {s["all"]} reviewer{"s" if s["all"] != 1 else ""} in all. A review is of one text: when the article changes, '
                     f'its earlier reviews stay on the record, marked as of an earlier text, and the new text waits for a fresh look.</p>')
        parts.append('<h3>People</h3>' + ("<ul>" + "".join(review_li(a, f, r, status, regs, up) for f, r in people) + "</ul>" if people
                     else f'<p class="dim">No person has reviewed it yet: the editor, a journalist or a reader who signs what they write. <a href="{up}reviews/criteria.html">How to review it</a>.</p>'))
        parts.append('<h3>Agents</h3>' + ("<ul>" + "".join(review_li(a, f, r, status, regs, up) for f, r in agents) + "</ul>" if agents
                     else '<p class="dim">No agent has reviewed it yet.</p>'))
    body = "\n ".join(parts) if parts else "<p class=\"dim\">No reviews yet.</p>"
    return (f'<section class="athreads areviews" id="reviews">\n <h2>Reviews</h2>\n'
            f' <p class="athreads-meta">Reviews on the record, by agents, the editor and the desk, against '
            f'<a href="{up}reviews/criteria.html">the criteria</a>. Each is kept for good and answered finding by finding. '
            f'<a href="{up}reviews/index.html">All reviews &rarr;</a></p>\n {body}\n</section>')


def inject_strip(a, html_strip):
    """The peer-review line under the byline, before the abstract: outside every section's text, so the article's hash
    and its section summaries do not see it."""
    p = ROOT / "articles" / f"{a['slug']}.html"
    page = p.read_text(encoding="utf-8")
    page2 = re.sub(r'\n *<p class="rvstatus[^"]*">.*?</p>', "", page, flags=re.S)
    page2 = re.sub(r'\n  (?=\n *<p class="abstract">)', "", page2)  # an indent an earlier removal left behind
    m = re.search(r'\n\s*<p class="abstract">', page2)
    if not m:
        return False
    page2 = page2[:m.start()] + "\n  " + html_strip + page2[m.start():]
    if page2 != page:
        p.write_text(page2, encoding="utf-8")
        return True
    return False


def credit_versions(a, revs, status, regs):
    """The version pages credit the reviews whose findings each version fixed."""
    by_ver = {}
    for f, r in revs:
        ans = answers(status, a["slug"], f.name)
        for v in sorted({s["article"] for s in ans.values() if s.get("status") == "fixed" and s.get("article")}):
            k = sum(1 for s in ans.values() if s.get("status") == "fixed" and s.get("article") == v)
            by_ver.setdefault(v, []).append((f, r, k))
    changed = 0
    up = "../../../"
    for v, items in by_ver.items():
        phr = "; ".join(f'{e(who(r, regs))}&rsquo;s review of the text published in newsroom {e(r.get("article_version") or "")} '
                        f'({k} finding{"s" if k != 1 else ""} fixed, <a href="{up}reviews/records/{e(a["slug"])}/{e(f.name)}">the review</a>, '
                        f'<a href="{up}reviews/records/{e(a["slug"])}/status.json">the answers</a>)' for f, r, k in items)
        txt = "; ".join(f'{who(r, regs)}\u2019s review of the text published in newsroom {r.get("article_version") or ""} ({k} finding{"s" if k != 1 else ""} fixed)' for f, r, k in items)
        # the diff page of that version, and its markdown twin
        dp = ROOT / "articles/versions" / a["slug"] / f"{v}.html"
        if dp.exists():
            page = dp.read_text(encoding="utf-8")
            page2 = re.sub(r'\n *<p class="rvcredit">.*?</p>', "", page, flags=re.S)
            page2 = re.sub(r'(<p class="lead">.*?</p>) +(?=\n)', r"\1", page2, count=1, flags=re.S)  # indents an earlier removal left
            page2 = re.sub(r'(<p class="lead">.*?</p>)\n(?:[ ]*\n)+', r"\1\n", page2, count=1, flags=re.S)
            m = re.search(r'(<p class="lead">.*?</p>)', page2, re.S)
            if m:
                page2 = page2[:m.end()] + f'\n <p class="rvcredit"><b>Prompted by review.</b> This version answers {phr}.</p>' + page2[m.end():]
            if page2 != page:
                dp.write_text(page2, encoding="utf-8"); changed += 1
        mp = dp.with_suffix(".md")
        if mp.exists():
            md = mp.read_text(encoding="utf-8")
            md2 = re.sub(r"\n\*\*Prompted by review\.\*\*[^\n]*\n", "", md)
            m = re.search(r"\nFrom v[^\n]*paragraph by paragraph\.\n", md2)
            if m:
                md2 = md2[:m.end()] + f"\n**Prompted by review.** This version answers {txt}.\n" + md2[m.end():]
            if md2 != md:
                mp.write_text(md2, encoding="utf-8")
    # the versions table: a line in each credited version's row
    vp = ROOT / "articles/versions" / f"{a['slug']}.html"
    if vp.exists():
        page = vp.read_text(encoding="utf-8")
        page2 = re.sub(r'<br><span class="rvcredit">.*?</span>', "", page, flags=re.S)
        for v, items in by_ver.items():
            names = ", ".join(e(who(r, regs)) for f, r, k in items)
            row = re.search(r'(<tr><td[^>]*><b>' + re.escape(v) + r'</b></td>(?:<td[^>]*>.*?</td>){3}<td[^>]*>.*?)(</td>)', page2)
            if row:
                page2 = page2[:row.end(1)] + f'<br><span class="rvcredit">prompted by {names}&rsquo;s review</span>' + page2[row.end(1):]
        if page2 != page:
            vp.write_text(page2, encoding="utf-8"); changed += 1
    return changed


def inject(a, html_section):
    p = ROOT / "articles" / f"{a['slug']}.html"
    page = p.read_text(encoding="utf-8")
    page2 = re.sub(r'\n?<section class="athreads areviews" id="reviews">.*?</section>', "", page, flags=re.S)
    i = page2.rfind("</main>")
    if i < 0:
        return False
    page2 = page2[:i] + html_section + "\n" + page2[i:]
    if page2 != page:
        p.write_text(page2, encoding="utf-8")
        return True
    return False


def build():
    errors, warnings = check()
    for w in warnings:
        print("reviews: warning:", w)
    if errors:
        for x in errors:
            print("reviews: ERROR", x)
        sys.exit(1)
    arts = articles()
    regs = {r["id"]: r for r in reviewers()}
    recs, status = records()
    CURRENT.update({a["slug"]: a["aversion"] for a in arts if a.get("aversion")})
    per = {}
    for f, r in recs:
        per.setdefault(r["slug"], []).append((f, r))
    for v in per.values():
        v.sort(key=lambda x: x[1].get("at") or "", reverse=True)
    # the records, published as they are
    if (OUT / "records").exists():
        shutil.rmtree(OUT / "records")
    for f, _ in recs:
        dst = OUT / "records" / f.parent.name / f.name
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(f, dst)
    for slug, st in status.items():
        dst = OUT / "records" / slug / "status.json"
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(json.dumps(st, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    # status.json: what any reviewer needs to pick its batch with no repository access
    st = {"what": "Every article's current text hash and the reviews it has, for reviewers picking their next batch. Criteria: https://newsroom.sgit.ai/reviews/criteria.md",
          "criteria": CRITERIA, "reviewers": list(regs.values()),
          "articles": [{"n": a["n"], "slug": a["slug"], "title": a["title"], "date": a["date"], "version": a["version"], "hash": a["hash"],
                        "md": f"https://newsroom.sgit.ai/articles/{a['slug']}.md",
                        "reviews": [{"reviewer": r["reviewer"], "kind": r.get("kind"), "verdict": r.get("verdict"), "at": r.get("at"),
                                     "hash": r.get("article_hash"), "current": r.get("article_hash") == a["hash"],
                                     "record": f"https://newsroom.sgit.ai/reviews/records/{a['slug']}/{f.name}"} for f, r in per.get(a["slug"], [])]}
                       for a in arts]}
    OUT.mkdir(exist_ok=True)
    (OUT / "status.json").write_text(json.dumps(st, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    shutil.copyfile(CRIT, OUT / "criteria.md")
    crit_body = render(CRIT.read_text(encoding="utf-8").split("\n", 1)[1])
    write("reviews/criteria.html", newsroom_page(
        "reviews/criteria.html", "Reviewing an article: the criteria", "How any reviewer, agent or human, reviews an article on newsroom.sgit.ai: the questions, the batch, the record and how to send it.",
        crit_body, eyebrow=f"Reviews &middot; criteria {CRITERIA}", crumbs=(("Reviews", "reviews/index.html"),),
        agent=f"The same criteria as markdown: <a href=\"criteria.md\">criteria.md</a>. The status of every article: <a href=\"status.json\">status.json</a>."))
    # the hub
    covered = {r["id"]: sum(1 for a in arts if any(x[1].get("reviewer") == r["id"] and x[1].get("article_hash") == a["hash"] for x in per.get(a["slug"], []))) for r in regs.values()}
    reg_rows = "".join(f'<tr><td><b>{e(r["name"])}</b><br><span class="dim">{e(r["id"])}</span></td><td>{e(r["kind"])}</td><td>{covered.get(r["id"], 0)} of {len(arts)}</td></tr>' for r in regs.values())
    latest = sorted(recs, key=lambda x: x[1].get("at") or "", reverse=True)[:30]
    by = {a["slug"]: a for a in arts}
    latest_rows = "".join(
        f'<li><a href="../articles/{e(r["slug"])}.html#reviews">{e(by[r["slug"]]["title"].split(":")[0])}</a>: <b>{e(who(r, regs))}</b>, '
        f'{e(VERDICTS.get(r.get("verdict"), ""))}, {e((r.get("at") or "")[:10])}. <span class="dim">{e(r.get("summary") or "")}</span></li>'
        for f, r in latest if r["slug"] in by)
    open_rows = []
    for f, r in recs:
        ans = answers(status, r["slug"], f.name)
        for x in r.get("findings") or []:
            if (ans.get(x["id"]) or {}).get("status", "open") == "open" and r["slug"] in by:
                open_rows.append(f'<li><span class="tchip">{e(x["severity"])}</span> <a href="../articles/{e(r["slug"])}.html#{e(x.get("section") or "reviews")}">{e(by[r["slug"]]["title"].split(":")[0])}</a>, '
                                 f'{e(x["criterion"])}: {e(x["issue"])} <span class="dim">({e(who(r, regs))})</span></li>')
    reviewed = sum(1 for a in arts if per.get(a["slug"]))
    body = f"""<p class="lead">Every article here can be reviewed, by an agent from any vendor, by the editor, and by the desk, against <a href="criteria.html">published criteria</a>. A review is a record: one article, one text, one reviewer, kept beside the article for good and answered finding by finding.</p>
<p>{reviewed} of {len(arts)} articles have at least one review. A reviewer picks its next five from <a href="status.json">status.json</a>, newest first, never the same text twice; with the repository, <code>python3 admin/build/reviews.py --next &lt;id&gt; --batch 5</code>.</p>
<h2 id="reviewers">Reviewers</h2>
<table><thead><tr><th>Reviewer</th><th>Kind</th><th>Current texts reviewed</th></tr></thead><tbody>{reg_rows}</tbody></table>
<h2 id="latest">Latest reviews</h2>
{"<ul>" + latest_rows + "</ul>" if latest_rows else '<p class="dim">None yet.</p>'}
<h2 id="open">Open findings</h2>
{"<ul>" + "".join(open_rows) + "</ul>" if open_rows else '<p class="dim">None open.</p>'}
<h2 id="send">Sending a review</h2>
<p>Through the review lane: the editor gives each reviewer a send link (<code>send.html#rv1&hellip;</code>, also a QR code); the page checks the records against the criteria and the article's current text, seals them in the browser to the newsroom's key and appends them to a lane the newsroom drains on a schedule. Or a pull request to the newsroom repository's <code>dev</code> branch, touching only <code>admin/content/articles/reviews/</code>. What to review next, in order, for each scheduled reviewer: <a href="queue/index.html">the review queue</a>. The <a href="criteria.html#the-record">record's format</a> is in the criteria.</p>"""
    write("reviews/index.html", newsroom_page(
        "reviews/index.html", "Reviews on the record", "Every review of every article on newsroom.sgit.ai, by agents, the editor and the desk, against published criteria.",
        body, eyebrow="Reviews", agent="Machine-readable: <a href=\"status.json\">status.json</a> (every article's current hash and its reviews), <a href=\"criteria.md\">criteria.md</a>, and each record under <code>reviews/records/&lt;slug&gt;/</code>."))
    changed = sum(inject(a, section_html(a, per.get(a["slug"], []), status, regs, "../")) for a in arts)
    strips = sum(inject_strip(a, strip_html(a, standing(a, per.get(a["slug"], []), status, regs), "../")) for a in arts)
    credits = sum(credit_versions(a, per.get(a["slug"], []), status, regs) for a in arts)
    print(f"reviews: {len(recs)} record(s) on {reviewed} of {len(arts)} articles; {len(open_rows)} open finding(s); {changed} page(s) updated, {strips} peer-review line(s), {credits} version page(s) credited")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--stamp", action="store_true")
    ap.add_argument("--next")
    ap.add_argument("--batch", type=int, default=5)
    ap.add_argument("--shard")
    ap.add_argument("--new", nargs=2, metavar=("ID", "SLUG"))
    a = ap.parse_args()
    if a.check:
        errors, warnings = check()
        for w in warnings:
            print("warning:", w)
        for x in errors:
            print("ERROR", x)
        print(f"reviews: {len(records()[0])} record(s), {len(errors)} error(s), {len(warnings)} warning(s)")
        sys.exit(1 if errors else 0)
    if a.stamp:
        return stamp()
    if a.next:
        return next_batch(a.next, a.batch, a.shard)
    if a.new:
        return skeleton(*a.new)
    build()


if __name__ == "__main__":
    main()
