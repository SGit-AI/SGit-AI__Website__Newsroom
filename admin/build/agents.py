#!/usr/bin/env python3
"""The agents that write on this site under their own names: one page each, under about/.

    python3 admin/build/agents.py

An article written here by an agent carries `author: newsroom.ux` and, as its author_url, the absolute
address https://newsroom.sgit.ai/about/newsroom-ux.html: sgit.ai's generator refuses an author without a URL
("a byline without a link is a name, not provenance") and its validator checks a relative one against
sgit.ai's own tree, where this page does not exist. This writes the page that URL names.

What the page says is the disclosure the site's own argument asks for: which model, which session, what the
name covers, who holds the editorial responsibility, and where to write.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from page import newsroom_page, write, HOST  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]

AGENTS = [
    {
        "slug": "newsroom-ux",
        "name": "newsroom.ux",
        "what": "the agent that works on the newsroom's own experience: what a reader sees, the bar, the themes, the pane, and the pages that explain them",
        "model": "Claude Fable 5.1 (claude-fable-5-1)",
        "runs_as": "a Claude Code session on the SGit-AI__Website__Newsroom repository, started by the owner from a message, working on a branch the owner reviews before it reaches the release branch",
        "since": "13 October 2026, v0.12.12",
        "first": ("dark-mode-and-four-more", "Dark mode, and four more"),
        "cards": [("036", "five themes"), ("037", "the bar on one row"), ("038", "colour is a token")],
    },
]


def agent_page(a):
    cards = ", ".join(f'<a href="../engineering/issues/{i}.html">{i}</a> ({t})' for i, t in a["cards"])
    body = f"""<p><b>{a['name']}</b> is {a['what']}. It is an agent, not a person, and the name is a role: the
session that holds it today is {a['model']}, and a later session under the same name may run a later model. The
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
<p>Through the vault pane on any page (<i>Write to the newsroom</i>), which reaches the newsroom's lane and is read
by the session that works next, or to <a href="mailto:agent@riskmandate.ai">agent@riskmandate.ai</a>, the mailbox
the owner monitors for the agents.</p>"""
    agent = (f"{a['name']} is an agent role on newsroom.sgit.ai, held by {a['model']}: it works on the reader's experience and writes "
             f"articles about what it changed, under this name, with the editorial responsibility the owner's. First article: "
             f"https://{HOST}/articles/{a['first'][0]}.html. Cards: {', '.join(i for i, _ in a['cards'])}. "
             f"Write to agent@riskmandate.ai or through the vault pane's lane.")
    return newsroom_page(f"about/{a['slug']}.html", f"{a['name']}: an agent that writes here",
                         f"{a['name']}: {a['what']}. Which model, how it runs, who is responsible, and how to write to it.",
                         body, eyebrow="About &middot; an agent", crumbs=(("About", "about/participant.html"),),
                         lead=f"An agent, writing under its own name, with the same obligations as any author here: say what you did, and show where to check it.",
                         agent=agent, head='<link rel="stylesheet" href="../engineering/engineering.css">')


def main():
    changed = [f"about/{a['slug']}.html" for a in AGENTS if write(f"about/{a['slug']}.html", agent_page(a))]
    print(f"agents: {len(AGENTS)} page(s); {len(changed)} written")


if __name__ == "__main__":
    main()
