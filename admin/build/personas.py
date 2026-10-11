#!/usr/bin/env python3
"""The pages that let a link open the newsroom as a persona, and the list of those links.

    python3 admin/build/personas.py

The five starting personas (Morgan the founder, Rowan the journalist, Sam the security lead, Kai the
AI builder, Jordan the board member) are in the reading meter's config, which is on every page. This
writes, from that config and from the article list, so a persona added to the config gets its page and
its row in the list on the next build:

  persona/index.html          a picker, or, with #<id> after the address, that persona
  persona/<id>/index.html     one page per persona, which is the link to send
  persona/links.json          every link, with the persona's name, its blurb and the articles it
                              starts from, for whoever is writing the email (a person or an agent)

The pages are small. What opens the newsroom as the persona is the meter's landing view (v1.4.0): it
adds the persona to the reader's browser as a visitor, makes it active, and offers Keep and Remove. The
articles each page lists are the persona's own, from the same config, so the list and the picks agree.

This is the first step of articles/a-link-to-a-persona.html, the one that needs no vault: the personas are
in the site, and a link names one. Personas in a vault, following and forking one, and a persona made for
one person are the later steps of that brief and are not here.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from page import newsroom_page, write, esc, HOST  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]


def presets():
    cfg = json.loads(re.search(r'id="sg-meter-config">(\{.*?\})</script>', (ROOT / "index.html").read_text(), re.S).group(1))
    return cfg["personas"]["presets"], cfg["start"], cfg.get("symbol", "£")


def lowered(label):
    return label[0].lower() + label[1:]


def display(p):
    """Morgan, the founder: how the meter names a starting persona (meter.presetName)."""
    return f"{p['name']}, {lowered(p['label'])}"


def articles_of(p, by_slug):
    out = []
    for s in p["articles"]:
        if s not in by_slug:
            sys.exit(f"personas: {p['id']} starts from {s}, which is not an article on this site")
        out.append(by_slug[s])
    return out


def others(p, ps, up):
    return "<ul>" + "".join(
        f'<li><a href="{up}persona/{q["id"]}/">{esc(display(q))}</a> &middot; {esc(q["blurb"].split(":")[0])}</li>'
        for q in ps if q["id"] != p["id"]) + "</ul>"


def persona_page(p, ps, by_slug, start, sym):
    up = "../../"
    arts = articles_of(p, by_slug)
    rows = "".join(
        f'<li><a href="{up}articles/{a["slug"]}.html">{esc(a["title"])}</a><br><span class="dim">{esc(a["teaser"])}</span></li>'
        for a in arts)
    money = f"{sym}{start / 100:.2f}"
    body = f"""<sg-meter view="landing" persona="{p['id']}"></sg-meter>
<noscript><p class="lead">{esc(p['blurb'])}</p></noscript>

<h2>Where {esc(p['name'])} starts</h2>
<p>{len(arts)} articles, the ones this persona is built on. The picks above start from them and move with what you read, keep and put out.</p>
<ul class="starts">{rows}</ul>

<h2>How this link works</h2>
<p>A persona is a reading list with a name, a set of topics and a graph. Opening this page adds {esc(p['name'])} to your personas in this browser, marked as a visitor, and makes it the one you are reading as. Keep it to have it with your others, or remove it; what you have read as yourself is not changed. The persona is stored in this browser, on this device, not on a server.</p>
<p>Pages are priced in pence, against {money} of starting credit that is also kept in this browser, and the meter does not block a page when the credit runs out. <a href="{up}articles/going-live-with-the-reading-meter.html">How the meter works and why it is there</a>.</p>

<h2>Read as someone else</h2>
{others(p, ps, up)}
<p><a href="{up}persona/index.html">All the personas</a>, with a link to copy for each.</p>
"""
    agent = (f"This page opens the newsroom as {display(p)} for a human reader, in their browser, using the reading meter's "
             f"landing view. For the content without a browser, the articles this persona starts from are listed above and in "
             f"https://{HOST}/persona/links.json, which lists every persona link.")
    return newsroom_page(
        f"persona/{p['id']}/index.html",
        f"Read the newsroom as {display(p)}",
        f"{p['blurb']} Opens the SGit Newsroom as {display(p)}, starting from {len(arts)} articles.",
        body, eyebrow="Read as a persona", crumbs=(("Read as a persona", "persona/index.html"),),
        agent=agent)


def picker_page(ps):
    up = "../"
    plain = "".join(f'<li><a href="{up}persona/{p["id"]}/">{esc(display(p))}</a>: {esc(p["blurb"])}</li>' for p in ps)
    body = f"""<sg-meter view="landing"></sg-meter>
<noscript><p>These need a script to open the newsroom as a persona. The links go to a page for each, which lists the articles it starts from:</p><ul>{plain}</ul></noscript>

<h2>Send someone a link</h2>
<p>Each persona has an address of its own, such as <code>https://{HOST}/persona/founder/</code>, and <b>Copy link</b> on a card copies it. The same persona can be named after a <code>#</code>, as in <code>https://{HOST}/persona/#founder</code>. The part after the <code>#</code> stays in the reader&rsquo;s browser; the page it opens is the same static page. The full list, with each persona&rsquo;s name, description and starting articles, is <a href="links.json">links.json</a>.</p>
<p>To send someone particular articles instead, with a note, <a href="{up}for/make.html">make a reading list</a>.</p>
<p>This is the first step of <a href="{up}articles/a-link-to-a-persona.html">a link to a persona</a>. The personas are the five starting ones in the reading meter, which are also on <a href="{up}account/personas.html">your personas</a>.</p>
"""
    agent = (f"Persona links, with each persona's name, description and starting articles, are in https://{HOST}/persona/links.json. "
             f"A link is https://{HOST}/persona/&lt;id&gt;/ or https://{HOST}/persona/#&lt;id&gt;; the ids are "
             + ", ".join(p["id"] for p in ps) + ".")
    return newsroom_page(
        "persona/index.html", "Read the newsroom as someone",
        "Pick a persona and the SGit Newsroom opens with picks, a reading list and a graph for it. Each persona has a link you can send.",
        body, eyebrow="Read as a persona",
        lead="Pick the person you are, or the one you want to see the newsroom as. It opens with picks, a reading list and a graph for that persona, and each one has a link you can send.",
        agent=agent)


def links(ps, by_slug, version):
    return {
        "what": "Links that open the SGit Newsroom as a persona. A person or an agent writing to someone can pick the persona "
                "closest to them and send its url. Written by admin/build/personas.py from the reading meter's config.",
        "site": f"https://{HOST}/",
        "release": version,
        "picker": f"https://{HOST}/persona/",
        "how": f"https://{HOST}/articles/a-link-to-a-persona.html",
        "reading_lists": f"https://{HOST}/for/make.html",
        "note": "Opening a link adds the persona to the reader's browser as a visitor, which they can keep or remove. "
                "The persona is stored in their browser, and the link does not identify them.",
        "personas": [{
            "id": p["id"],
            "name": p["name"],
            "label": p["label"],
            "display": display(p),
            "blurb": p["blurb"],
            "url": f"https://{HOST}/persona/{p['id']}/",
            "fragment_url": f"https://{HOST}/persona/#{p['id']}",
            "topics": sorted(p["topics"], key=lambda t: -p["topics"][t]),
            "starts_from": [{"slug": a["slug"], "title": a["title"], "url": a["url"]} for a in articles_of(p, by_slug)],
        } for p in ps],
    }


def main():
    ps, start, sym = presets()
    graphs = json.loads((ROOT / "articles/graphs.json").read_text())
    by_slug = {a["slug"]: a for a in graphs["articles"]}
    version = (ROOT / "admin/build/version.txt").read_text().strip()
    pages = [("persona/index.html", picker_page(ps))] + [(f"persona/{p['id']}/index.html", persona_page(p, ps, by_slug, start, sym)) for p in ps]
    changed = [rel for rel, text in pages if write(rel, text)]
    text = json.dumps(links(ps, by_slug, version), indent=2, ensure_ascii=False) + "\n"
    f = ROOT / "persona/links.json"
    if not f.exists() or f.read_text(encoding="utf-8") != text:
        f.write_text(text, encoding="utf-8")
        changed.append("persona/links.json")
    print(f"personas: {len(ps)} personas, {len(changed)} file(s) written {changed}")


if __name__ == "__main__":
    main()
