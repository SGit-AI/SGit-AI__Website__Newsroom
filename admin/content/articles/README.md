# Writing here: the voice, the shape, the contract and the run

The guide for whoever writes the next article in this folder, a person or an agent. It is drawn from the
nine articles written here between v0.12.10 and v0.12.24, read in full and counted, and from what the
articles say about themselves ([How the voice works](../../../articles/how-the-voice-works.md),
[How much of this did I write?](../../../articles/how-much-of-this-did-i-write.md),
[Every mistake added a rule](../../../articles/every-mistake-added-a-rule.md)). `publish.py` skips this
file, so it never reaches the site. The site's description of the same thing, for any contributor, is
[How to publish](../../../newsroom/publish.md); the contract the generator enforces is sgit.ai's
`admin/content/CONTENT.md`, which has not moved here yet.

## In short

- **One page, one argument, with the figures, the data and the links to check it.** An article argues one
  point. Everything it claims can be checked from the page, its links or the data behind it. That is the
  site's own test for the Journalist: a claim a reader cannot check is a failure.
- **The voice is Dinis's, in the first person, and it comes from a memo.** Most articles start as a
  voice memo of Dinis Cruz, kept in the order he thought it, with the phrases he reached for first. The
  agent writes it as him. An article an agent writes about its own work carries the agent's name instead.
- **Plain words, British spelling, no em-dashes, and one banned word.** The wording rules are short and
  each one was a correction once. The build refuses two of them.
- **The shape is the same every time.** Title with a colon, a long summary, a lead figure, In short, the
  argument in sections with anchors, What this does not claim, a line to write to, Where this comes from.
- **Count, do not remember.** Every number has a source named at the end, and a count is made by a script
  the article can point to. A figure is the evidence, drawn.
- **A graph beside every article.** Ten to fifteen nodes, a core idea, two quotes word for word, and the
  articles it links to.
- **Summaries beside every article.** For every section, a line of about eight words and a paragraph of two
  or three sentences, in `summaries/<slug>.json`: what a reader who has read the section sees in its place.
- **Read the record first.** The articles it builds on, in full, before anything outside. The vocabulary is
  defined on those pages, and a new article uses the words they use.

## What an article here is

The site's one line is the brief: *one page, one argument, with the figures, the data and the links to
check it*. The direction set for the desk is more evidence, not more words: the longer the article, the more
it should be standing on. In the nine written here, an article is 1,600 to 3,600 words of text, carries 2 to
6 figures, links 7 to 57 times, and about half of those links are to earlier articles on this site.

There are two kinds of author:

| Author | Front matter | What it is |
|---|---|---|
| Dinis Cruz | `author: Dinis Cruz`, `author_url: about/index.html` | A voice memo or a message of his, written by the agent in his voice. Eight of the nine. |
| An agent under its own name | `author: newsroom.ux`, `author_url: https://newsroom.sgit.ai/about/newsroom-ux.html` | The agent writing about what it built, in the first person as the agent, with the commits and tests to check it against. One of the nine. The page `author_url` names is written by `admin/build/agents.py`. |

Both say who holds the editorial responsibility, and it is always Dinis.

## The voice

What the nine articles do, counted from their text, and what to copy.

**First person, and honest about where it stands.** "I think", "my hypothesis", "I remember", "I could not
find who said it, so I will not put a name to it". Dinis's articles use *I* 13 to 35 times each. *We* is
Dinis and the agents together: "so we counted", "we noticed". The agent's own article uses neither
about itself in the body except where it did the work: "the first release put the collapse at 1199".

**Wishes, not demands.** Dinis does not speak in demands. When a memo says "I want", write what he would say: "I would like", "the idea is", "the plan is", "I hope", "what I have in mind". Keep "I want" only where it is plain description, not a request: "when I want to read a post", "the people I want to help", "being able to does not mean I want to". Above all, not in the abstract.

**No backhanded compliments.** Do not praise one person by criticising everyone else: no "I wish more people did this", "better than most", "ahead of most people". It is a dig at the reader, and it assumes the others are wrong when they may simply not need it. Say what the person did, and why it helped.

**No negative framing.** Do not raise an accusation nobody made in order to deny it ("not because anyone copied anything", "the numbers are not invented"), and do not put conditions on how others may do things ("that is fine too, as long as it is a graph"). Say the positive thing directly: what is true, and what it makes possible ("once both are graphs, nobody has to adopt anybody's schema" is fine: it says what graphs enable). Everything here is open source anyway.

**No judging the reader.** Do not imply the reader, or anyone else, missed something or did not look hard enough: no "anyone who looks at it closely", "what most frameworks miss", "if you pay attention", and no grading of other people's work ("is right to"). It reads as arrogant. Say what the thing is, and let the reader judge.

**A memo's order, kept.** The article follows the path the thinking took, including the turn that looks
like a tangent and is the connection: a Google executive remembered in the middle of a point about email,
the OWASP Wire at the end of an article about an iPhone. Do not reorganise the memo into someone else's
outline. Do weave the five topics into one argument with a beginning and an end.

**Plain words for concrete things.** The file, the commit, the button, the pane, the lane, the branch, the
tab. "The agents draft every email and I send every one." "A fix is a new version, the next reader gets
the fixed page." Prefer the thing to the abstraction, and when an abstraction is needed, use the one the
corpus already has: reach, mandate, footprint, blast radius, hope or enforcement, a behaviour policy, a
one-way door, explorer and villager and town planner, the record, the lethal trifecta. Each is defined on a
page here; link to it the first time.

**Sentences.** The average is 20 to 23 words; the longest in an article runs to 50 or 70. The rhythm is a
long sentence that stacks its parts with commas and semicolons, then a short one that lands: "An article
can be corrected tomorrow. An email cannot." Lists inside a sentence are joined by commas or set off by a
colon, never by an em-dash. The nine articles use 10 to 43 semicolons each and no em-dash.

**The move the argument makes.** Say what the other side gets right before adding what is missing: "The
post's record of 2026 is mostly right ... and I want to add the piece I think is missing". Turn the
question round: "not whether there is a human in the loop; which outputs need one". Then the test, with
its origin named: Bezos's doors, the SRE book's 70%. Then where Dinis actually is, with the counts:
fourteen releases in a day, every email still waits.

**Named sources, dated; private people unnamed.** A public post is named and linked with its date. A private
message is "someone shaping a roundtable in London", paraphrased, "and its author is not named". A person
mentioned in passing is "the person it was written for; she is not named". A memory is a memory: "attributed
here to my memory, not to a name".

**What it does not say.** No praise for the work ("great" is the strongest word, and it is for a thing, not
for us). No model names in the text; the agent's page carries the model, the article does not. No
"obviously" where the point is the argument. No claim about the world that the article cannot back: not
"nobody has", "the first to", "never scaled".

## Who is speaking

Every article is in one of three voices, and the byline shows which (v0.12.109;
[who is speaking](https://newsroom.sgit.ai/articles/who-is-speaking.html)):

- **Dinis, through an agent.** Almost every article: his memo or message, written up in his voice by the newsroom's
  agents, under his name, with the editorial responsibility his. *I* is Dinis. The byline adds *with the newsroom's
  agents*, and the sources end with who wrote it up.
- **An agent, in its own voice.** An agent writing about work it did, in the first person as the agent, with the
  commits and tests to check it against: `author: newsroom.<name>` and its page as `author_url`. The byline carries
  an agent mark. *I* is the agent; the editorial responsibility is still Dinis's.
- **Dinis, alone.** Written and published by him with no agent. None yet; it will need its own mark.

Never claim Dinis did something an agent did, or the reverse. *We* is Dinis and the agents, only where they did the
thing together.

## Revising published articles

Changing an article after it is published is normal and expected: when a fact changes, a source moves, a reviewer
finds something, or the understanding improves, the article is updated. Dinis's words: what matters is getting it
right. Every change is kept, because the build replays each article's history into its version pages, where any two
versions can be compared. So: change the article in its source, say why in the release notes (which article, what
changed, and why), restamp the section summaries the change made stale, and answer any review finding it fixes. The
one limit is the articles imported from sgit.ai: they are changed there, or moved here first.

## The wording rules

Seven rules, each learned when a word jarred, kept in the session's behaviour policy so it does not come
back. The first two are enforced by sgit.ai's validator at build time, so an article that breaks them does
not publish.

1. **No em-dashes.** A comma, a colon, a semicolon or a full stop does the job. The build fails on one.
2. **The ladder word.** One word for a step of a ladder is banned from every article, and the build fails on
   it, spelled r-u-n-g. The articles say "layer", "level" or "tier" instead, and the site refers to it only as "the
   ladder word".
3. **No absolutes you cannot back.** "Nobody has", "never scaled", "the first to". If it is true, show the
   count; if it is a feeling, say whose.
4. **"Great", not "perfect".** And not "massively".
5. **British English, and they/them** for anyone whose pronouns you do not know. Colour, behaviour,
   organisation, licence, programme. The only American spellings in the nine are inside code.
6. **Plainer words.** "Retire" rather than "get rid of". Short words where they exist.
7. **Not "prose" for the finished article.** It is the article, the piece, the finished article; "prose" is
   kept for what a renderer does to a markdown file.
8. **No superlative self-claims.** Not "the clearest example I have seen", "the best case study I can think
   of", "one of the clearest statements", "the best brief ever written". They claim more than an article can
   show and they cost it credibility. Say "a good example", "a useful test", or show why it matters.
   `admin/build/wording.py` flags them, and the leak scan fails a commit that adds one; a phrase reviewed and
   kept (a ranking inside a stated set) goes in `admin/build/wording-allow.txt`.
9. **Name people; not "the owner".** When an agent writes about who asked, decided or said something, it names
   them: "Dinis asked for five themes", "my last article ended with a question for Dinis". Use a role, *the editor*
   or *the publisher*, only where the role is the point. As more people join, the record should say who said what.

And three the desk keeps:

- **A quote is word for word.** The validator checks a quoted sentence against its source and fails the build
  if it differs. Quote less and exactly, with the date.
- **A number is counted, not remembered.** The Journalist's rule. Say at the end what counted it.
- **A byline without a link is a name, not provenance.** Every author has an `author_url`, and every source a
  link.

## The shape

Every article here has the same parts, in this order. The anchors are part of the contract: `{#in-short}`,
`{#limits}` and `{#sources}` are read by the build, and the body sections take short ones of their own.

```
---
title: <hook>: <the argument in one line>
date: YYYY-MM-DD
author: Dinis Cruz
author_url: about/index.html
summary: <220 to 360 words, first person, the whole argument with its numbers>
version: vX.Y.Z              # the site release that publishes it; stays as first published
time: HH:MM                  # optional, UTC: orders articles published the same day until the file is committed
license: https://creativecommons.org/licenses/by/4.0/
tags: <ten or so, kebab-case, the last one "article">
status: published
---

!shot <aa>-<name>.webp | images/ | <caption> | <kind>

> **What came next.** [<later article>](/articles/<slug>.html) <one line on what it adds>.   (only when there is one)

## In short {#in-short}
- **<the claim, in bold, as a sentence.>** <the number or the reason that backs it.>
  (six to ten of these; the first is the finding, the last is what was built or proposed)

## <The argument, in sections> {#<anchor>}
  (six to thirteen sections; a figure where the evidence is; the last of them is the proposal,
   the questions for the room, or where things stand)

## What this does not claim {#limits}
- **<a limit, in bold.>** <why, and what would change it.>
  (five to nine)

If you <are in the reader's position>, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}
<the origin; the responsibility line; every source, linked and dated; what the counts were made from>
```

**Links inside the site are root-relative**, `/articles/<slug>.html`, never `../articles/`: the build rewrites each for the page it lands on, and the pages also render inside a vault, where a leading slash would escape the app. That is rule 2 of sgit.ai's `CONTENT.md`.

**The title** is the hook, a colon, and the argument: 17 to 34 words. It names a mechanism, not a topic:
"The policy draws the liability line", "Every link points back", "How cheap is it to undo?". The part after
the colon is a sentence a reader could quote as the point. The slug is the hook, lower case, hyphenated,
and never changes once published: the address is the contract, and a retitle keeps the slug (v0.12.24 did
exactly that).

**The summary** is the abstract and the LinkedIn post: 220 to 360 words, first person, the whole argument
with its numbers, the origin ("Someone shaping a roundtable in London asked me this week ...") and the
place Dinis has got to. Written so that a reader who stops there has the article.

**The lead figure** comes first, before In short. Its caption describes the figure in full, as a sentence
or three, so the caption stands on its own in the markdown twin and for a reader who cannot see it.

**What came next** is a blockquote under the lead figure, added by the release that publishes the later
article, in the same commit, as [Every link points back](every-link-points-back.md) proposes. When you
publish an article that continues an earlier one, add the note to the earlier one.

**In short** is six to ten bullets. Each opens with the claim in bold, as a sentence with a full stop, and
follows with the figure or the reason. The first bullet is the finding; the last is what was built, what
is proposed, or how far Dinis has got.

**The body** is six to thirteen sections, each with a plain heading that says what it argues ("Email is a
one-way door, and still an explorer") and a short anchor. The order is the memo's. A figure sits where its
evidence is used, not at the top of the section for decoration. A table is used when the figure would be a
table. A numbered list is used for a proposal with parts or questions for a room.

**What this does not claim** is five to nine bullets, each a limit in bold with its reason: what is one
person's record, what was counted by words and could miss things, what is a proposal and not built, what the
law has not yet done, what is paraphrased. It is the section that lets the rest be confident.

**The line to write to** closes the limits section: one sentence naming who the article is for and the
address, `agent@riskmandate.ai`.

**Where this comes from** names the origin first: "A voice memo of mine on 13 October 2026, prompted by
..., written by this site's agent in the voice of this site. The argument and the editorial responsibility
are mine." Where there was no memo, say so: "There was no voice memo: this article was assembled by this
site's agent from my published positions". Then every outside source, linked, with its date and, for a
quote, the words quoted. Then what the counts were made from: the git log, a script over the article
sources, a file by name.

**A revision is a republish, not a story.** When an article changes, write the latest version as if it were
being published for the first time: the summary, In short and body say what is true now, with no "what
changed" section, no "the first version said" and no narrative of how the article evolved. The reader wants
the current article; the evolution is one click away, in the article's version history and its diff pages,
and the release note in `admin/engineering/releases/` says what moved and why. Where this comes from still
names who supplied or checked a fact (a review, a re-measurement), as provenance of the facts, not as a
history of the text. A fact that matters to the reader stays in, said plainly (a bug that was fixed, a
feature not yet released); the fact that an earlier version got it wrong does not.

## Figures

A figure is declared on one line, where it belongs in the text:

```
!shot <aa>-<name>.webp | images/ | <caption> | <kind>
```

- The trailing kind is carried on the figure as `data-kind`, and into the article's graph with the file, the URL and the caption. sgit.ai's `CONTENT.md` documents the three-field form; the fourth field is the kind.
- `<aa>` is a two-letter prefix per article (`cu-` for *How cheap is it to undo*, `hl-` for *The human in
  the loop*, `lb-` for *Every link points back*), so the folder reads by article.
- The file is in `images/`, 1,400 pixels wide, lossy webp, 40 to 70 KB. Screenshots of the site are the one
  exception and keep their real width.
- The caption stands alone: it says what the figure shows, what each axis or column is, and what to read off
  it. Two to four sentences.
- The kind is one of those in use: `comparison` (a table or a side by side), `architecture`, `decision`,
  `diagram`, `timeline`, `playbook`, `screenshot`, `collage`.

Figures are drawn, not generated: each is a small web page in the site's colours (Newsprint's warm
off-white and teal, the same type as the pages) rendered to an image by a headless browser, so a figure is
text that can be corrected rather than a picture that has to be redrawn. The renderer is not in either
repository; the figures are drawn in the session that writes the article. The way the four figures of
*Four frameworks, one agent* were made: one HTML file per figure sharing a small stylesheet in the site's
tokens, a body 1,400 pixels wide, rendered with Playwright's Chromium as a full-page screenshot clipped to
that width, and converted to webp at quality 82 with Pillow. The figure is where the evidence is: the counts as a chart, the two workflows as a table,
the decision as two axes, the six steps as a timeline. A figure that only decorates is left out.

A screenshot of the site is taken from the built site at a named width, and its caption says the width and
the theme.

**Sizes.** A figure fills the column unless its line gives a size before the kind:
`!shot <file> | images/ | <caption> | small|narrow|medium | <kind>` (42%, 62% or 78% of the column; full width on a
phone). Give one to any figure narrower than the column (about 915 pixels) or taller than it is wide, or its text
comes out larger than the article's own. The size applies to the image only: the caption always keeps the column's
full width. `python3 admin/build/figures.py` lists figures that probably need a size.

## Series

Articles that belong together, like the ones about the Generation Z Developers book, form a series by tag. A series is one entry in `admin/content/series.json` (id, title, tag, note); every article whose `tags` include the series' tag joins it, in publication order, and `admin/build/series.py` stamps a thin bar under its byline (the series, its place in it, the previous and next articles) and the full list at its foot. To add an article to a series, add the tag; nothing else is edited by hand.

Pieces that belong together as a reply, a tour and a vault form a trail: `!trail <name>` under the top figure renders a row of cards from `admin/content/trails.json`, this one marked "you are here". `admin/build/trail_end.py`, which `series.py` runs, copies the same cards, smaller, to the end of the text, just before the meter, and marks the next piece, so the reader who finishes an article sees where to go next. Nothing is written by hand for it.

## The graph

Beside every article, `graphs/<slug>.json`, read by the card, the threads, the wire and the desk:

```json
{
  "slug": "<slug>",
  "teaser": "<one sentence, under 30 words, for the card and the lists>",
  "topics": ["<one or two of: agents-and-policy, site-and-engineering, vaults-and-method, graphs-and-knowledge, startups-and-strategy>"],
  "core_idea": "<the argument in one long sentence>",
  "nodes": [ {"id": "<short>", "label": "<three to five words>", "kind": "<claim|concept|method|example|artefact|question>", "summary": "<one sentence>"} ],
  "edges": [ {"from": "<id>", "to": "<id>", "rel": "<leads-to|produces|example-of|depends-on|extends|answers|contrasts|compared-with>"} ],
  "links": { "articles": ["<slugs this article links to>"], "pages": [], "sites": ["<outside URLs cited>"] },
  "quotes": [ {"text": "<a sentence from the article, word for word>", "why": "<why it is the one to keep>"} ]
}
```

The nine graphs have 10 to 15 nodes, as many edges, and two quotes each. Node kinds in use, most used first:
claim, example, method, artefact, concept, question. The edges tell the argument's order: the example that
leads to the test, the test that produces the axes, the two cases that contrast. The quotes are the two
sentences a desk note or the newsletter would lift, and they must match the article exactly, because the
build checks a `!quote` against them.

## The summaries

Beside every article, `summaries/<slug>.json` (since v0.12.99, card 083). A reader who has read a section can
have it folded to a paragraph or a line, or hidden (`assets/reader/folds.js`), so every section needs both:

```json
{ "slug": "<slug>", "by": "<the writing agent, e.g. newsroom.writer>",
  "sections": { "top": { "line": "...", "para": "..." }, "<h2 anchor>": { "line": "...", "para": "..." } } }
```

- **The sections are the page's:** `top` is the opening (the abstract), then one per `##` heading, keyed by its
  `{#anchor}`. `python3 admin/build/summaries.py --dump <dir>` writes each article's sections as the page
  shows them, with their text, once the article is published.
- **line:** 6 to 9 words, saying what the section SAYS, not what it is about ("A prompt cannot report usage; a
  hook can", not "On token usage"); no full stop.
- **para:** two or three sentences, 30 to 60 words, with the section's point and its specifics (the figures,
  the names, the conclusion), so a reader who read it a week ago remembers it.
- The wording rules apply: no em-dash, no ladder word, British spelling; the article's own voice.
- After the article is published, `python3 admin/build/summaries.py --stamp` records each section's hash, so a
  later correction to a section marks its summary stale instead of leaving it summarising words that are gone;
  `python3 admin/build/summaries.py --check` reports what is missing, extracted or stale. A section with no
  written summary gets an extract (its first sentence), which is a floor, not the goal.

## Before writing

1. **Read the record first.** The articles the new one builds on, in full, with their graphs, before searching
   outside. The terms are defined there, and a new article links each the first time it uses it, as
   `/articles/<slug>.html`. Dinis's articles link 7 to 14 earlier articles each.
2. **Then outside, and date everything.** A source is linked and dated in the text or at the end; a figure
   from it is quoted with its exact words.
3. **Count with a script, and keep it.** The link counts in *Every link points back* came from a parser over
   the article sources; the release counts from `git log`. Data an article was written from goes in
   `data/<slug>__<name>.json` and the sources section names it.
4. **Keep the memo's phrases.** When Dinis said it in a way he would use, use that. The article is his.
5. **Say what was not done.** If part of the brief is a proposal, the limits say so; if a count could miss
   things, say how.

## The run

An article is a release. The steps, as the last nine did them:

1. Write `<slug>.md`, `graphs/<slug>.json`, `summaries/<slug>.json`, the figures in `images/`, and any data in `data/`.
2. Bump `admin/build/version.txt` to the next patch, add the row at the top of `admin/versions.html`, and
   write `admin/engineering/releases/vX.Y.Z.md` with the title prefixed `@newsroom.writer:` and a paragraph
   on what the article argues, its sources and its figures. An article release names no card
   (`issues: []`); a change to the site does.
3. Add the *What came next* note to the article this one continues, if there is one.
4. `python3 admin/build/publish.py --from <checkout of SGit-AI/SGit-AI__Website> --node-modules <dir with
   sharp and playwright>`. It replays this folder's history into a temporary clone, runs sgit.ai's
   generator and validator there (the em-dash, the ladder word, the links, the graph limits, the quotes),
   and imports the result. Nothing is pushed to sgit.ai. A slug sgit.ai already has stops the run.
5. Steps 4 to 8 of the release process in the root `README.md`: `summaries.py --stamp` then `summaries.py`, `ids.py`, `hubs.py`, `agents.py`,
   `personas.py`, `lists.py`, `passkey_lab.py`, `drafts.py`, `wire.py`, `api_map.py`, `archive.py`, `engineering.py`,
   `chrome.py`, `gen_sitemap.py`, `gen_llms_full.py`, then `node admin/build/validate.js`. Running them
   twice changes nothing.
6. Commit as `site vX.Y.Z: @newsroom.writer: <title>` and push the branch. Dinis reads the article after
   it is live, and a correction is a new version, with its diff page.

The newsletter is written the same way, in `../newsletter/NNN-YYYY-MM-DD.md`, in the format of sgit.ai's
newsroom README and with its directives (`!quote`, `!figure`, `!collage`, `!list`), and the same `publish.py`
publishes it.

## The checklist

Before the release, read the article once as Dinis would and once as the validator would.

- The title has the hook, the colon, and the argument; the slug is the hook.
- The summary stands alone, in the first person, with the numbers.
- The lead figure is first; every figure has a two-letter prefix, a caption that stands alone, and a kind.
- In short: six to ten, bold claim then its backing; the last says what was built or proposed.
- Every section has an anchor; the last body section is the proposal or where things stand.
- What this does not claim: five to nine; the write-to line closes it.
- Where this comes from: the origin, the responsibility line, every source dated, what counted the numbers.
- No em-dash; no ladder word; no "perfect", "massively", "prose"; British spelling; no model name in the
  text; no absolute without a count; no private person named.
- No superlative self-claim ("the clearest I have seen"): `python3 admin/build/wording.py FILE` is clean.
- Every quote is word for word; every earlier article the argument rests on is linked the first time.
- The graph has the slug, a teaser, one or two topics, the core idea, 10 to 15 nodes, the edges, the links
  and two exact quotes.
- The summaries have a line and a paragraph for every section, and `summaries.py --check` shows no extract for
  this article.
- The earlier article this one continues carries its *What came next* note.
- The version is bumped once, the release file and the row exist, and the validator passes.
