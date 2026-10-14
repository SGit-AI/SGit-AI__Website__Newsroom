#!/usr/bin/env python3
"""The pages for a reading list in a link: /for/ opens one, /for/make.html makes and previews one.

    python3 admin/build/lists.py

The brief is articles/a-reading-list-in-a-link.html, part one. What is generated here is the two pages;
what runs in them is for/reading-list.js (parse, build, show, open as a persona) and for/make.js (the
page that makes a list), which are source files, tested by admin/build/test_lists.mjs. The numbers they
read are articles/ids.json (admin/build/ids.py).
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from page import METER_JS, newsroom_page, write, esc, HOST  # noqa: E402
from api import api_url  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
CORE = api_url(METER_JS.replace("sg-meter.js", "sg-meter-core.js"))
HEAD = f'<link rel="stylesheet" href="{api_url("for/for.css")}">\n'
SITE = f"https://{HOST}/for/"
EXAMPLE = f"{SITE}#from=Dinis&amp;to=Steve&amp;r=65,60,62&amp;s=66&amp;f=founder"


def ids():
    return json.loads((ROOT / "articles/ids.json").read_text(encoding="utf-8"))


def open_page(d):
    personas = ", ".join(f"<code>{p['id']}</code>" for p in d["personas"])
    rows = [
        ("<code>from</code>, <code>to</code>", "Two first names, shown as &ldquo;For Steve, from Dinis&rdquo;.",
         "Up to 40 characters: letters, spaces, hyphens and apostrophes."),
        ("<code>r</code>", "Articles to read, by number, in the order given.", "Numbers that exist in <a href=\"../articles/ids.json\">articles/ids.json</a>. A list holds 1 to 50 articles, with <code>s</code>."),
        ("<code>s</code>", "Articles worth a look.", "The same numbers. An article in <code>r</code> is not repeated."),
        ("<code>f</code>", "What to follow.", f"A persona ({personas}) or a collection, as <code>c:how-agents-decide</code>. Up to 10."),
        ("<code>n</code>", "A note from the sender, one sentence.", "Up to 240 characters, shown as text."),
        ("<code>e</code>", "The sender&rsquo;s address, for a Reply button.", "An email address. Without it there is no button."),
    ]
    table = ('<div class="tablewrap"><table><thead><tr><th>Field</th><th>What it is</th><th>Rules</th></tr></thead><tbody>'
             + "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a, b, c in rows) + "</tbody></table></div>")
    body = f"""<div id="rl-mount" class="rl-mount"><p class="dim">Opening the list&hellip;</p></div>
<noscript><p>A reading list needs a script to open. The link has the form <code>{SITE}#from=Dinis&amp;to=Steve&amp;r=65,60,62</code>, and the numbers are the articles in <a href="../articles/ids.json">articles/ids.json</a>.</p></noscript>
<script type="module">
import {{ openList }} from '{api_url('for/reading-list.js')}';
openList({{ core: '{CORE}', ids: '../articles/ids.json', root: '../', mount: document.getElementById('rl-mount') }});
</script>

<div id="rl-docs">
<h2 id="link">How a link is made</h2>
<p>Everything is in the part of the link after the <code>#</code>, which a browser keeps to itself and does not send to the server. The page reads it, checks every part, and builds the list in the browser. A person makes one on <a href="make.html">the page that makes a list</a>; an agent can build the same link by hand from the numbers in <a href="../articles/ids.json">articles/ids.json</a>.</p>
<p>For example, <a href="{EXAMPLE}">{EXAMPLE}</a></p>
{table}
<p>Anything malformed is dropped, and the page says what it left out. Names and notes are shown as text and never as markup. Nothing in a link should be private, because a link travels in an email and can be forwarded.</p>

<h2 id="persona">What opens</h2>
<p>The list, with each article&rsquo;s number, title, teaser, price and reading time, and a <b>Start reading</b> button. The list is also added to the reader&rsquo;s personas as a visitor, named for the two people (&ldquo;Steve&rsquo;s list, from Dinis&rdquo;), with its articles as the reading list and the picks that follow from them. It is the active persona while the reader is on the page, and removing it is one tap. Opening a list charges nothing, and the articles are priced as everywhere on the site, from the reader&rsquo;s own credit.</p>

<h2 id="not">What this does not do</h2>
<p>It has no accounts, no endpoint on a server, and nothing that counts who opened a link or when. The names are whatever the link says: there is no way yet to prove who sent a list, and a signed list is a later step, on the keys of <a href="../articles/rfc-0001-public-key-cryptography-for-sgit.html">RFC 0001</a>. The sender learns anything from the reply, if there is one. This is the first step of <a href="../articles/a-reading-list-in-a-link.html">From me to you, in a link</a>.</p>
</div>
"""
    agent = (f"A reading list is a link of the form {SITE}#from=Dinis&to=Steve&r=65,60,62&s=66&f=founder, with the article numbers from "
             f"https://{HOST}/articles/ids.json. Fields: from, to (names, up to 40 characters), r (articles to read, in order), s (worth a look), "
             "f (a persona id or c:<collection>), n (a note of up to 240 characters), e (the sender's address). A list holds 1 to 50 articles. "
             "Build the link with the page at /for/make.html or by hand, open it on the live site to check it, and draft the email for the person to send: "
             "an agent drafts, the person sends.")
    return newsroom_page("for/index.html", "A reading list",
                         "A reading list from one person to another, in a link: the articles to read, a few worth a look, and what to follow. It opens as a persona the reader can keep or remove.",
                         body, eyebrow="From me to you, in a link",
                         lead="A link that says: from me, for you, here is what to read.", agent=agent, head=HEAD)


def make_page(d):
    body = f"""<div id="mk-mount" data-site="{SITE}"><p class="dim">Loading the articles&hellip;</p></div>
<noscript><p>Making a list needs a script. A link has the form <code>{SITE}#from=Dinis&amp;to=Steve&amp;r=65,60,62</code>, with the numbers from <a href="../articles/ids.json">articles/ids.json</a>; <a href="index.html#link">the fields are described here</a>.</p></noscript>
<script type="module">
import {{ makeList }} from '{api_url('for/make.js')}';
makeList({{ core: '{CORE}', ids: '../articles/ids.json', root: '../', site: '{SITE}', mount: document.getElementById('mk-mount') }});
</script>

<h2 id="how">What this page does</h2>
<p>It runs in your browser and sends nothing. The list you make is kept in this page&rsquo;s own address after the <code>#</code>, in the same form as the link it makes, so you can bookmark a list in progress, and the preview reads the link back with the parser the recipient&rsquo;s page uses, so it shows what they will see, including anything the page would leave out. <b>Open as the recipient</b> opens the real page in a new tab.</p>
<p>The link carries two first names, a note if you write one, and article numbers. It does not carry anything the sender would not want forwarded, so keep it that way. How a link is built is on <a href="index.html#link">the page that opens one</a>, and the numbers are in <a href="../articles/ids.json">articles/ids.json</a>.</p>
"""
    agent = (f"This page makes a reading list link in the browser: choose articles by number, name two people, copy the link, preview it as the recipient sees it. "
             f"To build a link without a browser, use the format at https://{HOST}/for/#link and the numbers in https://{HOST}/articles/ids.json. "
             "Open the link on the live site to check it before anything is sent; an agent drafts the email and the person sends it.")
    return newsroom_page("for/make.html", "Make a reading list",
                         "Choose the articles, name two people and copy a link that opens the newsroom as a reading list for them. The preview shows what they will see.",
                         body, eyebrow="From me to you, in a link",
                         lead="Choose the articles, name the two people, and copy the link. The preview is what they will see.",
                         agent=agent, wide=True, head=HEAD)


def main():
    d = ids()
    changed = [rel for rel, text in (("for/index.html", open_page(d)), ("for/make.html", make_page(d))) if write(rel, text)]
    print(f"lists: {len(changed)} page(s) written {changed}")


if __name__ == "__main__":
    main()
