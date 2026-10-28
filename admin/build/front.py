#!/usr/bin/env python3
"""The front page, in three views, and the purpose page (cards 063, 065).

    python3 admin/build/front.py

Writes index.html (and index.md, its markdown twin) from the newsroom's own data, newsroom/wire.json,
persona/links.json and articles/find.json, and the editor's words in admin/content/front/. The three views
are the Newsroom Design Lab's three directions, carried over: A Broadsheet (a serious paper: one lead,
the desks, the doors), B Briefing (answers first: five items in two sentences, then a door), C Your desk
(the reader's own newsroom: what they read, what it cost, their board). All three are rendered here, in
the page; a stylesheet shows the one named by data-view on <html>, which assets/front/front.js sets from
what this browser remembers before the first paint, Broadsheet when nothing is. Nothing on the page needs
JavaScript except the parts of Your desk that are the reader's own: the statuses, the progress, the
balance and the spend, which front.js fills from the meter's and the pane's local records.

The lead: the editor's, when admin/content/front/front.json names one (`lead` and `highlights`, each a slug
with a kicker and a why); otherwise the newest article leads and the next four are the highlights, with
the teaser standing in for the why. The placement data imported from sgit.ai (wire.front) is not read:
it stopped on 8 October, when the newsroom moved here.

The front page was imported from sgit.ai (articles/index.html written to the root) until v0.12.60.
sync_newsroom.py no longer writes the root copy; articles/index.html stays, as Every article.

The Broadsheet is organised by day and by topic (card 095): the lead and five more with their images, the last
DAYS_SHOWN publishing days in full, and the sections of admin/content/front/sections.json, one topic per article,
each with a page of its own at sections/<id>/index.html (and its .md twin). An article with no row in sections.json,
or a row naming a section that does not exist, stops the build and names the slug.

Also writes about/index.html, "Why this exists", from admin/content/front/purpose.json, which the masthead
links to on every view, and keeps articles/front.json, the compact data the views are built from, for the API.
"""
import datetime as dt
import json
import sys
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).parent))
from page import newsroom_page, write, esc, HOST, meter_block  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
VERSION = (ROOT / "admin/build/version.txt").read_text().strip()
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
NEUTRAL = "newsroom"
DAYS_SHOWN = 5        # publishing days the Broadsheet lists in full
FIVE = 5              # the lead's companions, with their images
SUB_MAX = 150         # a subtitle is cut at a word before this
STATUSES = [("new", "New"), ("reading", "Reading"), ("follow-up", "Follow-up"), ("done", "Done")]


def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def day_long(s):
    d = dt.date.fromisoformat(s)
    return f"{DAYS[d.weekday()]} {d.day} {MONTHS[d.month - 1]} {d.year}"


def day_short(s):
    d = dt.date.fromisoformat(s)
    return f"{d.day} {MONTHS[d.month - 1][:3]}"


def day_mid(s):
    d = dt.date.fromisoformat(s)
    return f"{d.day} {MONTHS[d.month - 1]} {d.year}"


HEAD_MAX = 72


def split_title(t):
    """The headline before the colon, the dek after it; the lab's fmt.title and fmt.dek.

    A headline is capped at HEAD_MAX characters, because a title whose colon comes late (or never) filled the
    front page's lists with whole paragraphs: it ends at a question mark inside the limit if there is one,
    otherwise at the last word that fits, with an ellipsis. The full title is still the article's own."""
    a, b = (t.split(": ", 1) + [""])[:2] if ": " in t else (t, "")
    if len(a) > HEAD_MAX:
        q = a.find("? ")
        if 0 < q < HEAD_MAX:
            a, rest = a[:q + 1], a[q + 2:]
            b = rest + (": " + b if b else "")
        else:
            a = a[:HEAD_MAX].rsplit(" ", 1)[0].rstrip(",;:") + "…"
    return a, (b[0].upper() + b[1:]) if b else ""


def cut(s, n=SUB_MAX):
    """s cut at the last word that fits in n characters, with an ellipsis."""
    if len(s) <= n:
        return s
    return s[:n].rsplit(" ", 1)[0].rstrip(",;:.") + "…"


def month_long(s):
    d = dt.date.fromisoformat(s)
    return f"{MONTHS[d.month - 1]} {d.year}"


def mins(m):
    return f"{m} min" if m else ""


def plural(n, word):
    return f"{n} {word}{'' if n == 1 else 's'}"


class Front:
    def __init__(self):
        self.wire = load("newsroom/wire.json")
        self.find = load("articles/find.json")
        self.links = load("persona/links.json")
        self.front = load("admin/content/front/front.json")
        self.mast = load("admin/content/front/masthead.json")
        self.purpose = load("admin/content/front/purpose.json")
        dv = ROOT / "admin/content/front/developing.json"
        self.developing_stories = json.loads(dv.read_text(encoding="utf-8"))["stories"] if dv.exists() else []
        self.agents = {a["name"]: a for a in load("admin/content/agents.json")["agents"]}
        self.written = {}
        for p in sorted((ROOT / "admin/content/front/personas").glob("*.json")):
            w = json.loads(p.read_text(encoding="utf-8"))
            self.written[w["id"]] = w
        self.articles = []
        for i, a in enumerate(self.wire["articles"]):
            f = self.find["articles"].get(a["slug"], {})
            head, dek = split_title(a["title"])
            self.articles.append({
                "slug": a["slug"], "title": a["title"], "head": head, "dek": dek, "date": a["date"], "index": i,
                "teaser": a["teaser"], "author": a.get("author") or "Dinis Cruz", "topics": a["topics"], "tags": a["tags"],
                "minutes": f.get("minutes") or 0, "format": f.get("format_label") or "Analysis", "desk": f.get("desk"),
                "series": f.get("series") or [],
                "url": f"articles/{a['slug']}.html", "card": f"articles/cards/{a['slug']}.webp",
                "by_agent": a.get("author") in self.agents,
            })
        self.by = {a["slug"]: a for a in self.articles}
        self.desk_label = {d["id"]: d for d in self.find["desks"]}
        dates = sorted(a["date"] for a in self.articles)
        self.edition = {"date": dates[-1], "first": dates[0], "total": len(self.articles),
                        "on_day": sum(1 for a in self.articles if a["date"] == dates[-1])}
        self.sections = self._sections()
        self.lead, self.highlights, self.five = self._placement()
        self.personas = self._personas()

    # ---- sections: one topic per article (card 095) ----
    def _sections(self):
        """The sections of admin/content/front/sections.json with their articles, newest first. The build stops, naming the
        slug, for an article with no row or a row naming a section that is not defined; a row for no article is also an error."""
        src = load("admin/content/front/sections.json")
        secs = {s["id"]: dict(s, articles=[]) for s in src["sections"]}
        bad = []
        for a in self.articles:
            sid = src["articles"].get(a["slug"])
            if sid is None:
                bad.append(f'{a["slug"]}: no row in admin/content/front/sections.json (add one in the commit that publishes it)')
            elif sid not in secs:
                bad.append(f'{a["slug"]}: names the section {sid!r}, which sections.json does not define')
            else:
                a["section"] = sid
                secs[sid]["articles"].append(a)
        bad += [f"{s}: a row in sections.json for no article" for s in src["articles"] if s not in self.by]
        if bad:
            raise SystemExit("front: every article is in exactly one section:\n  " + "\n  ".join(bad))
        for s in secs.values():
            s["articles"].sort(key=lambda a: (a["date"], -a["index"]), reverse=True)
            s["count"] = len(s["articles"])
            s["url"] = f"sections/{s['id']}/index.html"
        return list(secs.values())

    def sec(self, a):
        return next(s for s in self.sections if s["id"] == a["section"])

    def sec_tag(self, a, cls="sec-tag"):
        s = self.sec(a)
        return f'<a class="{cls}" href="{s["url"]}" style="--sec:{esc(s["colour"])}">{esc(s["label"])}</a>'

    def days(self):
        """The last DAYS_SHOWN publishing days, newest first: every article of each, the agents' own too."""
        by_day = {}
        for a in sorted(self.articles, key=lambda a: (a["date"], -a["index"]), reverse=True):
            by_day.setdefault(a["date"], []).append(a)
        return [(d, by_day[d]) for d in sorted(by_day, reverse=True)[:DAYS_SHOWN]]

    # ---- placement ----
    def _placement(self):
        ed = self.front.get("lead")
        newest = sorted((a for a in self.articles if not a["by_agent"]), key=lambda a: (a["date"], -a["index"]), reverse=True)
        if ed and ed.get("slug") in self.by:
            lead = dict(self.by[ed["slug"]], kicker=ed.get("kicker") or "", why=ed.get("why") or "", by="editor")
        else:
            a = newest[0]
            lead = dict(a, kicker=self.desk_label[a["desk"]]["short"] if a["desk"] else "The newest", why=a["teaser"], by="newest")
        highs = []
        for h in (self.front.get("highlights") or []):
            if h.get("slug") in self.by and h["slug"] != lead["slug"]:
                highs.append(dict(self.by[h["slug"]], kicker=h.get("kicker") or "", why=h.get("why") or ""))
        for a in newest:
            if len(highs) >= FIVE:
                break
            if a["slug"] != lead["slug"] and all(x["slug"] != a["slug"] for x in highs):
                highs.append(dict(a, kicker=a["format"], why=a["teaser"]))
        return lead, highs[:4], highs[:FIVE]

    # ---- personas ----
    def _personas(self):
        out = []
        live = {p["id"]: p for p in self.links["personas"]}
        for pid in [NEUTRAL] + [p["id"] for p in self.links["personas"]]:
            w = self.written.get(pid)
            lp = live.get(pid)
            base = lp or w
            if pid == NEUTRAL:
                start = [self.by[s] for s in (w or {}).get("start_here", []) if s in self.by]
                url = "index.html"
            else:
                slugs = (w or {}).get("start_here") or [s["slug"] for s in lp["starts_from"]]
                start = [self.by[s] for s in slugs if s in self.by]
                url = f"persona/{pid}/index.html"
            out.append({
                "id": pid, "neutral": pid == NEUTRAL, "name": base["name"], "label": base["label"],
                "display": base.get("display") or base["name"], "blurb": base["blurb"],
                "door": self.front["door_lines"].get(pid, base["label"]), "url": url,
                "line": (w or {}).get("line") or base["label"],
                "start": start, "minutes": sum(a["minutes"] for a in start), "written": bool(w),
            })
        return out

    # ---- pieces ----
    def newest(self, n, skip=(), where=None, agents=False):
        """The newest n articles; the agents' own are left out unless asked for (they have agents/index.html)."""
        out = [a for a in self.articles if a["slug"] not in skip and (where is None or where(a)) and (agents or not a["by_agent"])]
        out.sort(key=lambda a: (a["date"], -a["index"]), reverse=True)
        return out[:n]

    def desks(self, per, skip=()):
        return [{"desk": d, "articles": self.newest(per, skip, lambda a, d=d: a["desk"] == d["id"]),
                 "start": [self.by[s["slug"]] for s in d["start_here"] if s["slug"] in self.by][:3]} for d in self.find["desks"]]

    def chips(self, a, topic=True):
        d = self.desk_label.get(a["desk"]) if a["desk"] else None
        return ('<span class="chips">'
                f'<span class="chip chip-time">{mins(a["minutes"])}</span>'
                f'<span class="chip chip-format">{esc(a["format"])}</span>'
                + (f'<a class="chip chip-desk" href="desks/{esc(d["id"])}.html">{esc(d["short"])}</a>' if topic and d else '')
                + '</span>')

    def card(self, a, label):
        return (f'<a class="tile" href="{a["url"]}" tabindex="-1" aria-hidden="true">'
                f'<img loading="lazy" src="{a["card"]}" alt="" width="1200" height="630"><span class="tile-label">{esc(label)}</span></a>')

    def doors(self, cls):
        pub = self.front["door_publisher"]
        items = [p for p in self.personas if not p["neutral"]]
        out = "".join(
            f'<li><a class="{cls}" href="{p["url"]}"><span class="door-line">{esc(p["door"])}</span>'
            f'<span class="door-who">{esc(p["display"])}</span>'
            f'<span class="door-n">{plural(len(p["start"]), "piece")} to start &middot; {mins(p["minutes"])}</span></a></li>'
            for p in items)
        out += (f'<li><a class="{cls} door-pub" href="{pub["local"]}"><span class="door-line">{esc(pub["line"])}</span>'
                f'<span class="door-who">{esc(pub["who"])}</span><span class="door-n">{esc(pub["blurb"])}</span></a></li>')
        return out

    def switcher(self):
        v = self.front["views"]
        return ('<div class="view-switch" role="radiogroup" aria-label="Read the front page as">'
                '<span class="view-k">Read it as</span>'
                + "".join(f'<button type="button" class="view-btn" role="radio" aria-checked="{"true" if x["id"] == "broadsheet" else "false"}" '
                          f'data-view="{x["id"]}" title="{esc(x["note"])}"><span class="k">{x["key"]}</span><span class="n">{esc(x["name"])}</span></button>'
                          for x in v["list"])
                + '<button type="button" class="view-me" title="Your desk: what you read, what it cost, your board">'
                  '<span class="bar"><span style="width:0%"></span></span><span data-glance><b>0/0</b> read &middot; <b>&pound;0.00</b> spent</span></button>'
                + '</div>')

    def from_agents(self, cls):
        """The agents' own articles, newest three: briefs about work on the site, in the agent's voice."""
        arts = self.newest(3, where=lambda a: a["by_agent"], agents=True)
        if not arts:
            return ""
        li = "".join(f'<li><a href="{a["url"]}">{esc(a["head"])}</a> <span class="meta">{day_short(a["date"])} &middot; '
                     f'{esc(self.agents[next(x["author"] for x in self.wire["articles"] if x["slug"] == a["slug"])]["handle"])}'
                     f'{" &middot; " + mins(a["minutes"]) if a["minutes"] else ""}</span></li>' for a in arts)
        if cls == "bs":
            return (f'<section class="agents-strip" aria-labelledby="bs-agents-h"><div class="sec-rule"><h2 id="bs-agents-h">From the agents</h2>'
                    f'<span class="sec-side">Briefs written by the newsroom\'s agents in their own voice &middot; <a href="agents/index.html">all of them</a></span></div>'
                    f'<ul class="agents-list">{li}</ul></section>')
        return (f'<section class="bf-block" aria-labelledby="bf-agents-h"><h2 class="bf-sec" id="bf-agents-h">From the agents</h2>'
                f'<ul class="bf-coll">{li}</ul><p class="bf-more"><a href="agents/index.html">Written by the agents &rarr;</a></p></section>')

    # ---- developing stories: a strip in each view, after the broadsheet's masthead (v0.13.52, the editor's call) ----
    def _dev_items(self):
        out = []
        for d in self.developing_stories:
            tf = ROOT / d["tracker"]
            t = json.loads(tf.read_text(encoding="utf-8")) if tf.exists() else {}
            c = t.get("counts") or {}
            out.append(dict(d, version=t.get("version"), sources=c.get("sources"), data_as_of=t.get("data_as_of"),
                            passed=t.get("passed"), total=t.get("total"), checked=t.get("checked_utc"),
                            has_article=d.get("article") in self.by))
        return out

    def developing(self):
        items = self._dev_items()
        if not items:
            return ""
        html = []
        for d in items:
            facts = [f"site v{esc(d['version'])}" if d["version"] else "",
                     f"{d['sources']} sources captured" if d["sources"] else "",
                     f"data as of {esc(d['data_as_of'])}" if d["data_as_of"] else ""]
            links = [f'<a class="dev-go" href="{esc(d["url"])}">{esc(d["label"])} &rarr;</a>']
            if d["has_article"]:
                links.append(f'<a href="articles/{esc(d["article"])}.html">{esc(d["article_label"])}</a>')
            if d.get("passed") is not None:
                links.append(f'<a href="{esc(d["moving_url"])}">{esc(d["moving_label"])}: {d["passed"]} of {d["total"]} checks</a>')
            html.append(f'<section class="dev-strip" aria-label="{esc(d["kicker"])}"><p class="dev-k"><span class="dev-dot"></span>{esc(d["kicker"])}</p>'
                        f'<h2 class="dev-h"><a href="{esc(d["url"])}">{esc(d["title"])}</a></h2><p class="dev-dek">{esc(d["dek"])}</p>'
                        f'<p class="dev-facts">{" &middot; ".join(f for f in facts if f)}</p><p class="dev-links">{" ".join(links)}</p></section>')
        return "\n".join(html)

    # ---- A · Broadsheet: the lead and five, the last five days, the sections (card 095) ----
    def day_band(self, d, arts, first):
        mix = {}
        for a in arts:
            mix[a["section"]] = mix.get(a["section"], 0) + 1
        mix_line = " &middot; ".join(f'{n} {esc(next(s["label"] for s in self.sections if s["id"] == sid))}'
                                    for sid, n in sorted(mix.items(), key=lambda kv: (-kv[1], kv[0])))
        rows = "".join(
            f'<li class="day-item">{self.sec_tag(a)}<span class="day-min">{mins(a["minutes"])}</span>'
            f'<h4 class="day-t"><a href="{a["url"]}">{esc(a["head"])}</a></h4>'
            + (f'<p class="day-dek">{esc(cut(a["dek"] or a["teaser"]))}</p>' if (a["dek"] or a["teaser"]) else '')
            + '</li>' for a in arts)
        return (f'<section class="day{" day-first" if first else ""}" aria-label="{day_long(d)}">'
                f'<header class="day-h"><h3>{day_long(d).rsplit(" ", 1)[0]}'
                f' <span class="day-n">{plural(len(arts), "article")}</span></h3><p class="day-mix">{mix_line}</p></header>'
                f'<ol class="day-list">{rows}</ol></section>')

    def broadsheet(self):
        e, m, lead = self.edition, self.mast, self.lead
        neutral = self.personas[0]
        jump = "".join(f'<a href="#sec-{esc(s["id"])}" style="--sec:{esc(s["colour"])}">{esc(s["label"])}</a>' for s in self.sections)
        five = "".join(
            f'<li class="five-item">{self.card(a, "")}{self.sec_tag(a)}'
            f'<h3 class="five-h"><a href="{a["url"]}">{esc(a["head"])}</a></h3>'
            + (f'<p class="five-dek">{esc(cut(a["dek"] or a["teaser"], 110))}</p>' if (a["dek"] or a["teaser"]) else '')
            + f'<p class="meta">{day_short(a["date"])} &middot; {mins(a["minutes"])}</p></li>' for a in self.five)
        days = "".join(self.day_band(d, arts, i == 0) for i, (d, arts) in enumerate(self.days()))
        n_days = len(self.days())
        sec_cards = "".join(
            f'<article class="sec-card" id="sec-{esc(s["id"])}" style="--sec:{esc(s["colour"])}">'
            f'<h3 class="sec-h"><a href="{s["url"]}">{esc(s["label"])}</a> <span class="sec-n">{s["count"]}</span></h3>'
            f'<p class="sec-scope">{esc(s["scope"])}</p><ol class="sec-news">'
            + "".join(f'<li><a href="{a["url"]}">{esc(a["head"])}</a> <span class="meta">{day_short(a["date"])}</span></li>' for a in s["articles"][:5])
            + f'</ol><p class="sec-all"><a href="{s["url"]}">All {s["count"]} &rarr;</a></p></article>' for s in self.sections)
        colls = "".join(
            f'<li><a href="articles/collections/{c["id"]}.html"><span class="coll-t">{esc(c["title"])}</span></a><p>{esc(c["dek"])}</p>'
            f'<span class="meta">{plural(len(c["articles"]), "article")} &middot; updated {day_short(c["updated"])}</span></li>' for c in self.wire["collections"])
        start = "".join(f'<li><span class="start-n">{i + 1}</span><span><a href="{a["url"]}">{esc(a["head"])}</a> <span class="meta">{mins(a["minutes"])}</span></span></li>'
                        for i, a in enumerate(neutral["start"]))
        nl = self.wire["newsletter"][0]
        nl_url = urlparse(nl["url"]).path.lstrip("/")   # articles/newsletter/2026/10/13/006-....html
        dev = self.developing()
        return f"""<section class="view bs" data-view="broadsheet" aria-label="Broadsheet">
<header class="mast">
  <p class="dateline"><span>{day_long(e["date"])}</span><span class="dl-mid">Edition of {day_mid(e["date"])}</span><span>{plural(e["total"], "article")} since {day_short(e["first"])} 2026</span></p>
  <h1 class="mast-title">{esc(m["title"])}</h1>
  <p class="mast-heart">{esc(m["heart"])}</p>
  <p class="mast-line">{esc(m["line"])}</p>
  <p class="mast-meta">{esc(m["heart_note"])} <a href="about/index.html">Why this exists</a></p>
  <nav class="sec-jump" aria-label="Sections">{jump}</nav>
</header>
<div class="bs-top{" has-rail" if dev else ""}">
  <article class="lead" aria-labelledby="bs-lead-h">
    {self.card(lead, "")}
    {f'<p class="kicker">{esc(lead["kicker"])}</p>' if lead["by"] == "editor" else ""}
    <h2 class="lead-h" id="bs-lead-h"><a href="{lead["url"]}">{esc(lead["head"])}</a></h2>
    <p class="standfirst">{esc(lead["dek"] or lead["teaser"])}</p>
    <p class="byline">{self.sec_tag(lead)} By <b>{esc(lead["author"])}</b> &middot; {day_mid(lead["date"])} &middot; {mins(lead["minutes"])} read &middot; {esc(lead["format"])}</p>
    <p class="why"><b>{"Why it leads." if lead["by"] == "editor" else "In short."}</b> {esc(lead["why"])}</p>
  </article>
  {f'<aside class="rail" aria-label="The running story">{dev}</aside>' if dev else ""}
</div>
<section class="five" aria-labelledby="bs-five-h"><h2 class="vh" id="bs-five-h">Five more</h2><ol class="five-list">{five}</ol></section>
<section class="days" id="days" aria-labelledby="bs-days-h">
  <div class="sec-rule"><h2 id="bs-days-h">The last five days</h2><span class="sec-side"><a href="articles/index.html#all">Every article</a></span></div>
  <p class="sec-dek">Everything published on the {n_days} most recent publishing days, newest first, with the section each one belongs to.</p>
  <div class="day-grid">{days}</div>
</section>
<section class="secs" id="sections" aria-labelledby="bs-secs-h">
  <div class="sec-rule"><h2 id="bs-secs-h">Sections</h2><span class="sec-side">By topic &middot; every article is in exactly one</span></div>
  <p class="sec-dek">{len(self.sections)} centres of gravity. Each shows its five newest; the page of a section has all of them, by month.</p>
  <div class="sec-grid">{sec_cards}</div>
</section>
<div class="bs-pair">
  <section class="news" aria-labelledby="bs-news-h">
    <p class="kicker">{esc(self.front["newsletter"]["kicker"])}</p>
    <h2 id="bs-news-h"><a href="{nl_url}">{esc(split_title(nl["title"])[0])}</a></h2>
    <p>{esc(self.front["newsletter"]["ask"])} Issue {nl["number"]} went out on {day_mid(nl["date"])}.</p>
    <a class="btn primary" href="{self.front["newsletter"]["url"]}">{esc(self.front["newsletter"]["button"])}</a>
  </section>
  <section class="start" aria-labelledby="bs-start-h">
    <div class="sec-rule"><h2 id="bs-start-h">{esc(self.front["start_here_title"])}</h2></div>
    <p class="sec-dek">{esc(self.front["start_here_dek"])}</p>
    <ol class="start-list">{start}</ol>
  </section>
</div>
<section class="colls" aria-labelledby="bs-colls-h">
  <div class="sec-rule"><h2 id="bs-colls-h">Collections</h2><span class="sec-side"><a href="articles/collections/index.html">All collections</a></span></div>
  <ul class="coll-list">{colls}</ul>
</section>
<section class="doors" aria-labelledby="bs-doors-h">
  <div class="sec-rule"><h2 id="bs-doors-h">{esc(self.front["doors_title"])}</h2><span class="sec-side">Your newsroom starts in your browser; <a href="vault/index.html">a vault</a> carries it between devices</span></div>
  <p class="sec-dek">{esc(self.front["doors_dek"])}</p>
  <ul class="door-list">{self.doors("door")}</ul>
  <p class="door-neutral"><a href="persona/index.html"><b>{esc(self.front["door_lines"][NEUTRAL])}.</b> {esc(neutral["blurb"])}</a></p>
</section>
{self.from_agents("bs")}
<p class="bs-foot"><a href="articles/index.html#all">Every article</a> &middot; <a href="desks/index.html">The five desks</a> &middot; <a href="archive/index.html">The archive</a></p>
</section>"""

    # ---- B · Briefing ----
    def briefing(self):
        e, m, lead = self.edition, self.mast, self.lead
        items = [dict(lead, lead=True)] + [dict(h, lead=False) for h in self.highlights]
        total = sum(i["minutes"] for i in items)
        neutral = self.personas[0]
        desks = self.desks(3, [i["slug"] for i in items])
        li = "".join(
            f'<li class="bf-item{" is-lead" if it["lead"] else ""}">'
            f'<p class="bf-label"><span class="bf-num">{i + 1}</span>{"<b>The lead</b> &middot; " if it["lead"] else ""}{esc(it["kicker"])}</p>'
            f'<h2 class="bf-h"><a href="{it["url"]}">{esc(it["head"])}</a></h2>'
            f'<p class="bf-news">{esc(it["teaser"])}</p>'
            + (f'<p class="bf-why"><b>{"Why it matters." if lead["by"] == "editor" else "The newest."} </b>{esc(it["why"])}</p>' if it["lead"] and it["why"] != it["teaser"] else "")
            + self.chips(it) + '</li>' for i, it in enumerate(items))
        doors = "".join(
            f'<li><a class="bf-door{" neutral" if p["neutral"] else ""}" href="{p["url"] if not p["neutral"] else "persona/index.html"}">'
            f'<span class="bf-door-line">{esc(p["door"])}</span><span class="bf-door-who">{esc(p["display"] if not p["neutral"] else "The newsroom")} &middot; {plural(len(p["start"]), "pick")}</span>'
            f'<span class="bf-arrow" aria-hidden="true">&rarr;</span></a></li>' for p in self.personas)
        pub = self.front["door_publisher"]
        doors += (f'<li><a class="bf-door pub" href="{pub["local"]}"><span class="bf-door-line">{esc(pub["line"])}</span>'
                  f'<span class="bf-door-who">{esc(pub["who"])}</span><span class="bf-arrow" aria-hidden="true">&rarr;</span></a></li>')
        desk_html = "".join(
            f'<details class="bf-desk"><summary><span class="bf-desk-t">{esc(dk["desk"]["label"])}</span><span class="bf-desk-n">{dk["desk"]["count"]}</span></summary><ol>'
            + "".join(f'<li><a href="{a["url"]}">{esc(a["head"])}</a> <span class="muted">{mins(a["minutes"])}</span></li>' for a in dk["articles"])
            + f'<li class="more"><a href="desks/{dk["desk"]["id"]}.html">The whole desk &rarr;</a></li></ol></details>' for dk in desks)
        start = "".join(f'<li><span class="bf-num">{i + 1}</span><a href="{a["url"]}">{esc(a["head"])}</a><span class="muted">{mins(a["minutes"])}</span></li>' for i, a in enumerate(neutral["start"]))
        colls = "".join(f'<li><a href="articles/collections/{c["id"]}.html">{esc(c["title"])}</a><span class="muted">{len(c["articles"])}</span></li>' for c in self.wire["collections"])
        return f"""<section class="view bf" data-view="briefing" aria-label="Briefing">
{self.developing()}
<header class="bf-head">
  <p class="bf-brand"><b>{esc(m["title"])}</b> <span>{day_long(e["date"])}</span></p>
  <h1>{esc(self.front["briefing"]["title"])}</h1>
  <p class="bf-heart">{esc(m["heart"])} <span class="bf-line">{esc(m["line"])} <a href="about/index.html">Why this exists</a></span></p>
</header>
<div class="bf-cols">
  <div class="bf-main">
    <p class="bf-dek"><b>{len(items)} items.</b> {esc(self.front["briefing"]["dek"])} The full pieces add up to {mins(total)}.</p>
    <ol class="bf-items">{li}</ol>
    <p class="bf-more"><a href="articles/index.html#all">Every article &rarr;</a></p>
  </div>
  <aside class="bf-side" aria-labelledby="bf-doors-h">
    <h2 class="bf-sec" id="bf-doors-h">Now read it as&hellip;</h2>
    <ul class="bf-doors">{doors}</ul>
  </aside>
</div>
<section class="bf-block" aria-labelledby="bf-desks-h">
  <h2 class="bf-sec" id="bf-desks-h">The five desks <span class="muted">&middot; three each</span></h2>
  <div class="bf-desks">{desk_html}</div>
</section>
{self.from_agents("bf")}
<div class="bf-pair">
  <section class="bf-block" aria-labelledby="bf-start-h">
    <h2 class="bf-sec" id="bf-start-h">{esc(self.front["start_here_title"])} <span class="muted">&middot; {mins(neutral["minutes"])}</span></h2>
    <ol class="bf-start">{start}</ol>
  </section>
  <section class="bf-block" aria-labelledby="bf-coll-h">
    <h2 class="bf-sec" id="bf-coll-h">Collections</h2>
    <ul class="bf-coll">{colls}</ul>
    <div class="bf-news-ask"><p><b>{esc(self.front["newsletter"]["kicker"])}.</b> {esc(self.front["newsletter"]["ask"])}</p><a class="btn primary" href="{self.front["newsletter"]["url"]}">{esc(self.front["newsletter"]["button"])}</a></div>
  </section>
</div>
</section>"""

    # ---- C · Your desk ----
    def desk(self):
        e, m, lead = self.edition, self.mast, self.lead
        neutral = self.personas[0]
        desks = self.desks(3, [lead["slug"]])
        chooser = "".join(
            f'<button type="button" class="dk-who" role="radio" data-persona="{p["id"]}" aria-checked="{"true" if p["neutral"] else "false"}" title="{esc(p["door"])}">'
            f'<span class="avatar{" neutral" if p["neutral"] else ""}" aria-hidden="true">{"N" if p["neutral"] else p["name"][0]}</span>'
            f'<span class="dk-who-t"><b>{"The newsroom" if p["neutral"] else esc(p["name"])}</b><span>{"Everyone" if p["neutral"] else esc(p["label"].replace("The ", ""))}</span></span></button>'
            for p in self.personas)
        picks = "".join(
            f'<li class="dk-row" data-slug="{a["slug"]}" data-path="/{a["url"]}"><span class="dk-i">{i + 1}</span>'
            f'<span class="dk-row-main"><a href="{a["url"]}">{esc(a["head"])}</a>{self.chips(a, topic=False)}</span>'
            f'<span class="dk-st st-new" data-status>New</span></li>' for i, a in enumerate(neutral["start"]))
        board = "".join(f'<li class="b-{sid}"><b data-count="{sid}">0</b><span>{label}</span></li>' for sid, label in STATUSES)
        desk_html = "".join(
            f'<section class="dk-card dk-desk" aria-label="{esc(dk["desk"]["label"])}"><h3><a href="desks/{dk["desk"]["id"]}.html">{esc(dk["desk"]["label"])}</a> <span class="dk-count">{dk["desk"]["count"]}</span></h3><ol>'
            + "".join(f'<li><a href="{a["url"]}">{esc(a["head"])}</a></li>' for a in dk["articles"]) + '</ol></section>' for dk in desks)
        colls = "".join(f'<a class="pill tap" href="articles/collections/{c["id"]}.html">{esc(c["title"])} &middot; {len(c["articles"])}</a>' for c in self.wire["collections"])
        return f"""<section class="view dk" data-view="desk" aria-label="Your desk">
{self.developing()}
<header class="dk-hello">
  <p class="dk-date">{esc(m["title"])} &middot; {day_long(e["date"])}</p>
  <h1>{esc(self.front["doors_title"])}</h1>
  <p class="dk-line">{esc(m["heart"])} {esc(m["line"])}</p>
</header>
<div class="dk-chooser" role="radiogroup" aria-label="Read the newsroom as">{chooser}</div>
<p class="dk-chooser-note muted xs">Pick who you are reading as: the picks below, and the balance chip in the bar, follow. <a href="persona/index.html">Every persona</a> &middot; <a href="account/personas.html">your personas</a></p>
<div class="dk-grid">
  <section class="dk-card dk-picks" aria-labelledby="dk-picks-h">
    <div class="dk-card-h"><h2 id="dk-picks-h">Picks for <span data-persona-name>everyone</span></h2><span class="muted small"><span data-done>0</span> done &middot; <span data-picks-total>{plural(len(neutral["start"]), "pick")} &middot; {mins(neutral["minutes"])}</span></span></div>
    <div class="dk-progress" role="progressbar" aria-label="Start-here progress" aria-valuemin="0" aria-valuemax="{len(neutral["start"])}" aria-valuenow="0"><span style="width:0%"></span></div>
    <ol class="dk-list" data-persona="{NEUTRAL}">{picks}</ol>
    <p class="dk-note muted small">A status follows your reading: opened is Reading, read to the end is Done, and a decision kept in <a href="vault/index.html">the pane</a> (read later, follow up) stands.</p>
  </section>
  <div class="dk-side">
    <section class="dk-card dk-you" aria-labelledby="dk-you-h">
      <div class="dk-card-h"><h2 id="dk-you-h">You</h2><span class="muted xs" data-you-where>in this browser</span></div>
      <ul class="dk-you-grid">
        <li><b data-you="balance">&pound;5.00</b><span>credit left</span></li>
        <li><b data-you="spent">&pound;0.00</b><span>spent so far</span></li>
        <li><b data-you="reads">0</b><span>articles opened</span></li>
        <li><b data-you="notes">0</b><span>notes kept</span></li>
      </ul>
      <p class="dk-you-note muted small">{esc(m["heart_note"])} <a href="account/index.html">Your account</a> &middot; <a href="vault/index.html">Your vault</a></p>
    </section>
    <section class="dk-card" aria-labelledby="dk-board-h">
      <div class="dk-card-h"><h2 id="dk-board-h">Your board</h2><span class="muted xs">the picks above</span></div>
      <ul class="dk-board">{board}</ul>
    </section>
    <section class="dk-card dk-lead" aria-labelledby="dk-lead-h">
      <p class="kicker">{"Today's lead" if lead["by"] == "editor" else "The newest"} &middot; {esc(lead["kicker"])}</p>
      {self.card(lead, self.desk_label[lead["desk"]]["short"] if lead["desk"] else "")}
      <h2 id="dk-lead-h"><a href="{lead["url"]}">{esc(lead["head"])}</a></h2>
      <p class="small">{esc(lead["why"])}</p>
      {self.chips(lead)}
    </section>
  </div>
</div>
<section class="dk-desks" aria-labelledby="dk-desks-h">
  <div class="dk-card-h"><h2 id="dk-desks-h">The five desks</h2><span class="muted small">{plural(e["total"], "article")} &middot; <a href="desks/index.html">every desk</a></span></div>
  <div class="dk-desk-grid">{desk_html}</div>
</section>
<section class="dk-strip" aria-label="Collections and newsletter">
  <div class="dk-colls"><h2 class="dk-mini">Collections</h2><div class="row">{colls}</div></div>
  <div class="dk-news"><h2 class="dk-mini">{esc(self.front["newsletter"]["kicker"])}</h2><p class="small">{esc(self.front["newsletter"]["ask"])}</p><a class="btn" href="{self.front["newsletter"]["url"]}">{esc(self.front["newsletter"]["button"])}</a></div>
</section>
</section>"""

    # ---- the page ----
    def data(self):
        """What front.js needs for Your desk: each persona's picks as paths, and the view list."""
        return {
            "what": "The front page's data for the reader's own view, written by admin/build/front.py. Picks per persona as site paths; the views.",
            "edition": self.edition, "views": self.front["views"]["list"],
            "personas": [{"id": p["id"], "name": p["name"], "neutral": p["neutral"], "label": p["label"],
                          "picks": [{"slug": a["slug"], "path": "/" + a["url"], "head": a["head"], "minutes": a["minutes"], "format": a["format"]} for a in p["start"]]} for p in self.personas],
            "lead": {"slug": self.lead["slug"], "by": self.lead["by"]},
            "highlights": [h["slug"] for h in self.highlights],
        }

    def html(self):
        m = self.mast
        desc = f"{m['heart']} {m['line']}"
        title = f"{m['title']}: {m['heart'].rstrip('.')}"
        data = json.dumps(self.data(), ensure_ascii=False).replace("</", "<\\/")
        agent = (f"The front page of newsroom.sgit.ai, {VERSION}, in three views (Broadsheet, Briefing, Your desk; data-view on html, "
                 f"kept under newsroom.view). Pay for what you read: a reading meter charges a few pence a page from credit in the browser. "
                 f"{self.edition['total']} articles since {self.edition['first']}; the newest is {self.edition['date']}. The lead is "
                 f"{self.lead['slug']} ({'the editor&rsquo;s choice' if self.lead['by'] == 'editor' else 'the newest article'}). Every article: "
                 f"https://{HOST}/articles/index.html; the wire of all of them: https://{HOST}/newsroom/wire.json; findability (desks, tags, series, "
                 f"formats, reading time): https://{HOST}/articles/find.json; personas: https://{HOST}/persona/links.json; this page as markdown: "
                 f"https://{HOST}/index.md.")
        ld = json.dumps({"@context": "https://schema.org", "@type": "WebSite", "name": m["title"], "url": f"https://{HOST}/",
                         "description": desc, "inLanguage": "en", "publisher": {"@type": "Organization", "name": "SGit Newsroom"}}, ensure_ascii=False)
        return f"""<!doctype html>
<html lang="en" data-root="">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="https://{HOST}/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{esc(m["title"])}">
<meta property="og:url" content="https://{HOST}/">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="https://{HOST}/og/default.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{esc(m["title"])}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://{HOST}/og/default.jpg">
<link rel="alternate" type="text/markdown" href="index.md" title="This page as markdown">
<link rel="alternate" type="application/rss+xml" title="SGit Newsroom" href="articles/feed.xml">
<script type="application/ld+json">{ld}</script>
<link rel="stylesheet" href="assets/newsroom.css">
<link rel="stylesheet" href="assets/fonts.css">
<link rel="stylesheet" href="assets/front/front.css">
<script src="assets/front/front.js"></script>
</head>
<body>
<nav class="site"></nav>
<main class="front-views" id="front">
{self.switcher()}
{self.broadsheet()}
{self.briefing()}
{self.desk()}
<div class="agent"><h4>For an agent</h4><p>{agent}</p></div>
</main>
<script type="application/json" id="front-data">{data}</script>
{meter_block("", m["title"])}<footer class="site"></footer>
<script src="assets/site.js" defer></script>
</body>
</html>
"""

    def markdown(self):
        m, e = self.mast, self.edition
        out = [f"# {m['title']}", "", f"**{m['heart']}** {m['line']}", "",
               f"{m['heart_note']}", "",
               f"> newsroom.sgit.ai · site {VERSION} · {plural(e['total'], 'article')} since {e['first']}; the newest is {e['date']}. Three views of this page: Broadsheet, Briefing, Your desk (https://{HOST}/).", "",
               *[l for d in self._dev_items() for l in (f"## {d['kicker']}: {d['title']}", "", f"{d['dek']} [{d['label']}]({d['url']})" + (f", site v{d['version']}, {d['sources']} sources captured, data as of {d['data_as_of']}." if d['version'] else "."), "")],
               f"## The lead", "", f"- [{self.lead['title']}](articles/{self.lead['slug']}.md), {self.lead['date']}, {mins(self.lead['minutes'])}. {self.lead['why']}", "",
               "## Highlights", ""]
        out += [f"- [{h['title']}](articles/{h['slug']}.md), {h['date']}, {mins(h['minutes'])}." for h in self.highlights]
        out += ["", "## The last five days", ""]
        for d, arts in self.days():
            out += [f"### {day_long(d)}", ""] + [f"- [{a['title']}](articles/{a['slug']}.md), {self.sec(a)['label']}, {mins(a['minutes'])}." for a in arts] + [""]
        out += ["## Sections", "", "Every article is in exactly one."]
        out += [f"- [{s['label']}]({s['url'].replace('index.html', 'index.md')}) ({s['count']}): {s['scope']}" for s in self.sections]
        out += ["", "## Who are you reading as?", ""]
        out += [f"- {p['door']}: [{p['display']}]({p['url'].replace('index.html', 'index.md') if p['url'].endswith('index.html') else p['url']}), {plural(len(p['start']), 'piece')} to start." for p in self.personas if not p["neutral"]]
        out += [f"- {self.front['door_publisher']['line']}: [{self.front['door_publisher']['who']}]({self.front['door_publisher']['url']})", "", "## The five desks", ""]
        for dk in self.desks(3):
            out.append(f"### {dk['desk']['label']} ({dk['desk']['count']})")
            out.append(f"{dk['desk']['for_whom']}")
            out += [f"- [{a['title']}](articles/{a['slug']}.md), {a['date']}, {mins(a['minutes'])}." for a in dk["articles"]]
            out.append("")
        out += ["## Collections", ""] + [f"- [{c['title']}](articles/collections/{c['id']}.md): {c['dek']}" for c in self.wire["collections"]]
        out += ["", "## Start here", ""] + [f"{i + 1}. [{a['title']}](articles/{a['slug']}.md), {mins(a['minutes'])}." for i, a in enumerate(self.personas[0]["start"])]
        out += ["", f"Data: [the wire](newsroom/wire.json), [findability](articles/find.json), [personas](persona/links.json), [llms.txt](llms.txt). Written from Dinis Cruz's voice notes by a desk of named agents under published rules; content CC BY 4.0 unless a page states otherwise.", ""]
        return "\n".join(out)

    # ---- one page per section (card 095) ----
    def section_page(self, s):
        up = "../../"
        months = []
        for a in s["articles"]:
            if not months or months[-1][0] != a["date"][:7]:
                months.append((a["date"][:7], []))
            months[-1][1].append(a)
        body = "".join(
            f'<h2 id="m-{mo}">{month_long(mo + "-01")} <span class="dim">{len(arts)}</span></h2><ol class="sp-list">'
            + "".join(f'<li><a href="{up}{a["url"]}">{esc(a["title"])}</a><br><span class="dim">{day_mid(a["date"])} &middot; {mins(a["minutes"])}'
                      f' &middot; {esc(a["format"])}</span></li>' for a in arts) + '</ol>' for mo, arts in months)
        others = " &middot; ".join(f'<a href="../{o["id"]}/index.html">{esc(o["label"])}</a>' for o in self.sections if o["id"] != s["id"])
        body = (f'<p class="dim">{plural(s["count"], "article")}, newest first, by month. Every article on this site is in exactly one section; '
                f'the assignment is <a href="{up}admin/content/front/sections.json">admin/content/front/sections.json</a>.</p>' + body
                + f'<h2 id="others">The other sections</h2><p>{others}</p>'
                + '<style>.sp-list li{margin:.55rem 0}</style>')
        agent = (f"The section {s['label']} of newsroom.sgit.ai: {s['scope']} {s['count']} articles, newest first, by month. "
                 f"Every article is in exactly one section (https://{HOST}/admin/content/front/sections.json). All articles: https://{HOST}/articles/index.html; "
                 f"this page as markdown: https://{HOST}/{s['url'][:-5]}.md.")
        return newsroom_page(s["url"], s["label"], s["scope"], body, eyebrow="A section &middot; by topic",
                             crumbs=(("The front page", "index.html#sections"),), agent=agent)

    def section_markdown(self, s):
        out = [f"# {s['label']}", "", s["scope"], "", f"> {plural(s['count'], 'article')} on newsroom.sgit.ai, newest first. Every article is in exactly one section.", ""]
        mo = None
        for a in s["articles"]:
            if a["date"][:7] != mo:
                mo = a["date"][:7]
                out += [f"## {month_long(mo + '-01')}", ""]
            out.append(f"- [{a['title']}](../../articles/{a['slug']}.md), {a['date']}, {mins(a['minutes'])}.")
        return "\n".join(out) + "\n"

    # ---- the purpose page ----
    def purpose_page(self):
        pu = self.purpose
        parts = []
        for s in pu["sections"]:
            parts.append(f'<h2 id="{esc(s["id"])}">{esc(s["label"])}</h2><p class="lead-in">{esc(s["lede"])}</p>')
            if s["id"] == "for":
                parts.append("<ul>" + "".join(
                    f'<li><a href="../{p["url"]}"><b>{esc(p["door"])}</b></a>: {esc(p["blurb"])}' for p in self.personas if not p["neutral"]) +
                    f'<li><a href="../{self.front["door_publisher"]["local"]}"><b>{esc(self.front["door_publisher"]["line"])}</b></a>: {esc(self.front["door_publisher"]["blurb"])}</li></ul>')
            if s.get("points"):
                parts.append("<ul>" + "".join(f"<li>{esc(p)}</li>" for p in s["points"]) + "</ul>")
            if s.get("disclosure"):
                parts.append(f'<div class="note"><b>{esc(s["disclosure"])}</b> <a href="participant.html">Where we lose: the full disclosure</a>.</div>')
            if s.get("actions"):
                parts.append("<ol>" + "".join(f'<li><b>{esc(a["label"])}.</b> {esc(a["text"])}</li>' for a in s["actions"]) + "</ol>")
        body = (f'<p class="lead">{esc(pu["standfirst"])}</p>' + "".join(parts)
                + f'<p class="dim">The heart line of the front page is <i>{esc(self.mast["heart"])}</i>: {esc(self.mast["heart_note"])}</p>')
        agent = (f"Why newsroom.sgit.ai exists: the agenda (share what Dinis Cruz learns with the evidence attached; solve real problems in the open; "
                 f"build sgit.ai and RiskMandate, which the articles use as evidence), open by default (CC BY 4.0 content, Apache 2.0 code), "
                 f"written from voice notes by named agents under published rules, who it is for (the personas), and what the author wants from a reader: "
                 f"read, rate, say what is missing, put your agents on a problem. Disclosure: https://{HOST}/about/participant.html.")
        return newsroom_page("about/index.html", pu["title"], f"{pu['standfirst']}", body,
                             eyebrow="About &middot; the purpose", crumbs=(), lead="", agent=agent)


def main():
    f = Front()
    changed = []
    if write("index.html", f.html()):
        changed.append("index.html")
    md = f.markdown()
    p = ROOT / "index.md"
    if not p.exists() or p.read_text(encoding="utf-8") != md:
        p.write_text(md, encoding="utf-8")
        changed.append("index.md")
    if write("about/index.html", f.purpose_page()):
        changed.append("about/index.html")
    for s in f.sections:
        if write(s["url"], f.section_page(s)):
            changed.append(s["url"])
        p = ROOT / s["url"].replace("index.html", "index.md")
        md_s = f.section_markdown(s)
        if not p.exists() or p.read_text(encoding="utf-8") != md_s:
            p.write_text(md_s, encoding="utf-8")
            changed.append(str(p.relative_to(ROOT)))
    data = json.dumps(f.data(), indent=1, ensure_ascii=False) + "\n"
    p = ROOT / "articles/front.json"
    if not p.exists() or p.read_text(encoding="utf-8") != data:
        p.write_text(data, encoding="utf-8")
        changed.append("articles/front.json")
    print(f"front: edition {f.edition['date']}, lead {f.lead['slug']} ({f.lead['by']}), {len(f.personas)} personas, "
          f"{len(f.find['desks'])} desks; {len(changed)} written {changed}")


if __name__ == "__main__":
    main()
