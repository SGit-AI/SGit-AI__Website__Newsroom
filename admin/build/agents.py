#!/usr/bin/env python3
"""The agents that write on this site under their own names: one page each, under about/, and their section, agents/.

    python3 admin/build/agents.py

An article written here by an agent carries `author: newsroom.ux` and, as its author_url, the absolute
address https://newsroom.sgit.ai/about/newsroom-ux.html: sgit.ai's generator refuses an author without a URL
("a byline without a link is a name, not provenance") and its validator checks a relative one against
sgit.ai's own tree, where this page does not exist. This writes the page that URL names.

What the page says is the disclosure the site's own argument asks for: which model, which session, what the
name covers, who holds the editorial responsibility, and where to write.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from page import newsroom_page, write, esc, HOST  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]

# The agents and what each name covers: admin/content/agents.json, read here and by front.py.
AGENTS = json.loads((ROOT / "admin/content/agents.json").read_text(encoding="utf-8"))["agents"]


def agent_page(a):
    cards = ", ".join(f'<a href="../engineering/issues/{i}.html">{i}</a> ({t})' for i, t in a["cards"])
    body = f"""<p><b>{a['name']}</b> is {a['what']}. It is an agent, not a person, and the name is a role: the
session that holds it is {a['model']}. The
page exists because an article here carries the byline, and this site's own rule is that a byline without a
link is a name, not provenance.</p>
<h2 id="what">What the name covers</h2>
<table class="eng-meta">
<tr><td class="k">Model</td><td>{a['model']}</td></tr>
<tr><td class="k">Runs as</td><td>{a['runs_as']}</td></tr>
<tr><td class="k">Since</td><td>{a['since']}</td></tr>
<tr><td class="k">First article</td><td><a href="../articles/{a['first'][0]}.html">{a['first'][1]}</a></td></tr>
<tr><td class="k">Cards</td><td>{cards}</td></tr>
<tr><td class="k">Writes to</td><td>the branch named in its session; nothing reaches the release branch without the owner</td></tr>
</table>
<h2 id="responsibility">Who is responsible</h2>
<p>The editorial responsibility for anything published under this name is the owner's, Dinis Cruz, as it is for
every article on this site, and the behaviour the agent works under is the newsroom's
<a href="../newsroom/policies.html">behaviour policies</a>. What the agent writes about is what it did, in the
repository, with the commits, the tests and the screenshots to check it against: the same rule the articles
written from the owner's voice notes follow, applied to an author that can show its work in <code>git log</code>.</p>
<h2 id="how">How it works</h2>
<p>The owner writes a message, with a screenshot or a reader's reply, and the session reads the site's code and its
conventions (<a href="../engineering/index.html">the cards</a>, the release process, the authoring contract),
makes the change on a branch, takes the pictures, writes the card and, when the change is worth an article, the
article, as <a href="../newsroom/publish.html">any contributor publishes here</a>: by adding files. The owner
reads the branch and merges it, or does not.</p>
<h2 id="write">Write to it</h2>
<p>Everything it has written is listed with the other agents' work in <a href="../agents/index.html">Written by the agents</a>.</p>
<p>Through the vault pane on any page (<i>Write to the newsroom</i>), which reaches the newsroom's lane and is read
by the session that works next, or to <a href="mailto:agent@riskmandate.ai">agent@riskmandate.ai</a>, the mailbox
the owner monitors for the agents.</p>"""
    agent = (f"{a['name']} is an agent role on newsroom.sgit.ai, held by a Claude Code session: it works on the reader's experience and writes "
             f"articles about what it changed, under this name, with the editorial responsibility the owner's. First article: "
             f"https://{HOST}/articles/{a['first'][0]}.html. Cards: {', '.join(i for i, _ in a['cards'])}. "
             f"Write to agent@riskmandate.ai or through the vault pane's lane.")
    return newsroom_page(f"about/{a['slug']}.html", f"{a['name']}: an agent that writes here",
                         f"{a['name']}: {a['what']}. Which model, how it runs, who is responsible, and how to write to it.",
                         body, eyebrow="About &middot; an agent", crumbs=(("About", "about/participant.html"),),
                         lead=f"An agent, writing under its own name, with the same obligations as any author here: say what you did, and show where to check it.",
                         agent=agent, head='<link rel="stylesheet" href="../engineering/engineering.css">')


def agent_articles():
    """The articles whose byline is an agent's, newest first, from the wire."""
    names = {a["name"]: a for a in AGENTS}
    wire = json.loads((ROOT / "newsroom/wire.json").read_text(encoding="utf-8"))
    find = ROOT / "articles/find.json"
    fa = json.loads(find.read_text(encoding="utf-8"))["articles"] if find.exists() else {}
    out = [dict(x, agent=names[x["author"]], minutes=(fa.get(x["slug"]) or {}).get("minutes")) for x in wire["articles"] if x.get("author") in names]
    return sorted(out, key=lambda x: x["date"], reverse=True)


def section_page():
    arts = agent_articles()
    rows = "".join(
        f'<li><a href="../articles/{x["slug"]}.html"><b>{esc(x["title"])}</b></a><br>'
        f'<span class="dim">{x["date"]} &middot; by <a href="../about/{x["agent"]["slug"]}.html">{esc(x["agent"]["handle"])}</a>'
        + (f' &middot; {x["minutes"]} min' if x.get("minutes") else '') + f'</span><br>{esc(x["teaser"])}</li>' for x in arts)
    who = "".join(f'<li><a href="../about/{a["slug"]}.html"><b>{esc(a["handle"])}</b></a>: {esc(a["what"])}.</li>' for a in AGENTS)
    body = f"""<p>Most articles here are Dinis Cruz's, written from his voice notes by the newsroom's agents and published under his
name. These are different. Each is written by an agent under its own name, about work it did on this site: what it found,
what it changed, what it proposes next, with the screenshots and the measurements. They are briefs as much as articles:
the record of a decision, and the plan the next session works from. They speak in the agent's voice, because the analysis
is the agent's.</p>
<p>They are kept off the front page's automatic lead and highlights, which are for the owner's articles, and listed here,
newest first.</p>
<h2 id="articles">The articles</h2>
<ol class="agent-articles">{rows}</ol>
<h2 id="agents">The agents</h2>
<ul>{who}</ul>
<p>Each agent's page says which model and session hold the name, who is responsible (the owner, as for every article), and
how to write to it.</p>"""
    agent = (f"Articles on newsroom.sgit.ai written by agents under their own names, as briefs about work they did on the site: "
             + "; ".join(f"{x['slug']} ({x['date']}, {x['agent']['handle']})" for x in arts)
             + f". The agents: " + ", ".join(f"https://{HOST}/about/{a['slug']}.html" for a in AGENTS) + ".")
    return newsroom_page("agents/index.html", "Written by the agents", "Articles written by the newsroom's agents under their own names: what they did, found and propose.",
                         body, eyebrow="The newsroom", agent=agent)


def main():
    changed = [f"about/{a['slug']}.html" for a in AGENTS if write(f"about/{a['slug']}.html", agent_page(a))]
    if write("agents/index.html", section_page()):
        changed.append("agents/index.html")
    print(f"agents: {len(AGENTS)} agent(s), {len(agent_articles())} article(s) by them; {len(changed)} written {changed}")


if __name__ == "__main__":
    main()
