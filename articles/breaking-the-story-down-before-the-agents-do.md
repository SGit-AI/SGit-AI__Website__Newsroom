# Breaking the story down before the agents do: a reply to Ole Reissmann's session at the News Product Alliance Summit, and what this newsroom already ships to the machines that read it, sgit.ai

> Ole Reissmann, who works on AI and journalism at DER SPIEGEL, led a session at the News Product Alliance Summit in Chicago called "Beyond the Article: Breaking Down Stories So Agents Get Them Right". His diagnosis is one I share: agents read journalism as fragments, stitch a confident summary together, sometimes miss the one thing that matters, and the publisher has almost no say in what comes out. His answer is to do the breakdown ourselves, before the machines do: SPIEGEL built a workflow that pulls out the actors and events, traces sources and claims, and flags allegations the affected party should get to respond to, and tested it for summaries with no human in the loop. He also says that a lot of the layers already exist, they just are not plugged into each other. This is a reply from a newsroom built that way from the start. Every article here is published with a markdown twin, a knowledge graph and a one-line and one-paragraph summary of every section, and the release checks look for them. As of today there are 327 article graphs, with 3,676 nodes, 3,564 edges and 819 quotes, each checked to appear word for word in its article, and summaries for 3,674 sections. The site publishes llms.txt and llms-full.txt for agents, and every article ends with where it came from. The book we are writing keeps a claims register in which every number has an id and a command to rerun it. And today's article on a contractor's agent at the Pentagon put the answers of the company, the department and the vendor next to the allegations. Where SPIEGEL is ahead is the allegation itself as a field, and I would like to add it.

*Source: <https://newsroom.sgit.ai/articles/breaking-the-story-down-before-the-agents-do.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Breaking the story down before the agents do: a reply to Ole Reissmann's session at the News Product Alliance Summit, and what this newsroom already ships to the machines that read it

# Breaking the story down before the agents do: a reply to Ole Reissmann's session at the News Product Alliance Summit, and what this newsroom already ships to the machines that read it

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-30 · [article v1.0.0](versions/breaking-the-story-down-before-the-agents-do.md) · [newsroom v0.14.5](https://newsroom.sgit.ai/admin/versions.html) · newsagentsstructured-journalismknowledge-graphssummariesprovenanceright-of-replyarticle

***Abstract:** Ole Reissmann, who works on AI and journalism at DER SPIEGEL, led a session at the News Product Alliance Summit in Chicago called "Beyond the Article: Breaking Down Stories So Agents Get Them Right". His diagnosis is one I share: agents read journalism as fragments, stitch a confident summary together, sometimes miss the one thing that matters, and the publisher has almost no say in what comes out. His answer is to do the breakdown ourselves, before the machines do: SPIEGEL built a workflow that pulls out the actors and events, traces sources and claims, and flags allegations the affected party should get to respond to, and tested it for summaries with no human in the loop. He also says that a lot of the layers already exist, they just are not plugged into each other. This is a reply from a newsroom built that way from the start. Every article here is published with a markdown twin, a knowledge graph and a one-line and one-paragraph summary of every section, and the release checks look for them. As of today there are 327 article graphs, with 3,676 nodes, 3,564 edges and 819 quotes, each checked to appear word for word in its article, and summaries for 3,674 sections. The site publishes llms.txt and llms-full.txt for agents, and every article ends with where it came from. The book we are writing keeps a claims register in which every number has an id and a command to rerun it. And today's article on a contractor's agent at the Pentagon put the answers of the company, the department and the vendor next to the allegations. Where SPIEGEL is ahead is the allegation itself as a field, and I would like to add it.*

Ole Reissmann's post after his session at the News Product Alliance Summit in Chicago.

## In short

- **Ole Reissmann's diagnosis is right.** Agents read journalism as fragments and stitch together a confident summary that can miss the one thing that matters.
- **His answer is right too:** break the story down ourselves, before the machines do, as structured data that keeps the reporting intact.
- **This newsroom was built that way.** Every article ships with a markdown twin, a graph and a summary of every section, and the release checks look for them.
- **The numbers today:** 327 graphs, 3,676 nodes, 3,564 edges, 819 quotes checked word for word, and 3,674 summarised sections.
- **Sources and claims are traced:** every article ends with where it came from, and the book's claims register gives every number an id.
- **The allegation is where SPIEGEL is ahead.** We put the other side's answer next to the claim; a field for it is what I would add.
- **The layers can be plugged together** when one pipeline owns them: the article, the graph, the summaries and the sources are released as one thing.

## The problem, in his words

Ole Reissmann leads work on AI and journalism at DER SPIEGEL. After his session in Chicago he wrote: "AI agents are reading our journalism. They just aren't reading it the way we wrote it. They fire off a bunch of queries, grab a few fragments, and stitch together a summary that sounds confident. Sometimes they miss the one thing that actually matters. And we get basically zero say in what comes out the other end."

That is the problem in four sentences, and it is why I started this newsroom the way I did. An article written for a person to read from top to bottom is a poor input for a machine that reads a fragment. The answer is not to stop writing articles. It is to publish, next to the article, the structure the article already has: who did what, what is claimed, on what evidence, and what each part says in one line.

## His answer: do the breakdown first

"So what if we did the breakdown ourselves? Before the machines get to it?" SPIEGEL built an LLM workflow that "pulls out the actors and events, traces sources and claims, and flags allegations the affected party should get to respond to. The output is structured data that keeps reporting intact." And it is not a whiteboard idea: "We tested it at SPIEGEL, for summaries, fully automated, no humans in the loop."

I like three things about this. It starts with the newsroom's own judgement rather than the agent's. It treats sources and claims as first-class, which is where trust lives. And the allegation and the right to respond are in it from the start, which is the part of journalism an agent is most likely to flatten.

## What this newsroom already ships

Every article on this site is released with four things beside it, and the release checks look for them: an article without a graph and a teaser fails the search test, and a section without a summary is flagged before the commit.

What every article here ships for the machines that read it, with the counts on 30 October 2026.

- **A markdown twin.** Every page has its markdown, so an agent never has to scrape HTML; there are 329 article pages and 329 twins.
- **A knowledge graph** of the article: a teaser, its core idea, nodes of six kinds (concept, claim, method, artefact, example, question), edges of eight relations, its links, and quotes that a script checks appear word for word in the article. Across 327 articles: 3,676 nodes, 3,564 edges and 819 quotes; 986 of the nodes are claims.
- **A summary of every section,** in one line and in one paragraph, keyed by the section's anchor, so a reader or an agent can take any part at the depth it needs. 3,674 sections are summarised; a check marks a summary stale when its section changes after it was written.
- **Where it came from:** every article ends with its sources, dated, and what it does not claim.

And for agents as a whole, the site publishes `llms.txt` and `llms-full.txt`, a search index built at release time, and a reader API with a map of what it serves. The argument behind it is economic as well as editorial: a curated graph answers an agent's question for fewer tokens than the raw page, so serving the structure is cheaper for everyone than letting the agent guess.

## Actors, events, sources and claims

Two pieces of what Ole Reissmann describes are where our work has gone furthest.

**Sources and claims.** On the book we are writing, a researcher agent keeps a claims register: every number in the draft carries an id, and an appendix gives a command to rerun each one from the record. The draft's 294 pages cite claims C001 to C042. In [Sources and their shadows](sources-and-shadows.md) we went further, recording for every reference its licence, its access, its links, its quotes and its history, and reading an article we cannot open through what others say about it. I did exactly that today with WIRED's story about a contractor's agent on a Pentagon network, and the shadow showed where the outlets disagreed.

**Actors and events.** [The wire as a graph](the-wire-as-a-graph.md) is the design for the news itself: a story as a short narrative in which every name is a link to a person, a company, an event or a place with a long-lived id, and every sentence is a claim with its evidence, typed as a fact, an observation, a statement by a party, or our analysis. That is the same breakdown SPIEGEL describes, designed for a wire that runs on a schedule.

## The allegation and the right to respond

This is where SPIEGEL is ahead, and where I would like to learn from it.

We do the practice: every article here puts a party's answer next to a claim about them when there is one, and says what it does not claim. [On the record](on-the-record.md) and [signed by the source](signed-by-the-source.md) go further, proposing that experts and sources sign their position on an article with their own keys, and can withdraw it.

But we do not yet mark an allegation as a kind of thing in the graph. Our node kinds include claim; an allegation is a claim about a party, with a status: put to them or not, answered or not, and the answer itself. Made a field, it would let an agent that summarises the story carry the answer with the allegation, instead of dropping it. That is the one thing I would add to our graphs after reading Ole Reissmann's post, and I would rather align with what SPIEGEL has built than invent a second shape.

## Plugging the layers together

"A lot of the layers already exist. They just aren't plugged into each other." I agree, and I think the reason is that they are usually separate projects: the CMS, the tagging, the summaries, the API, each owned by a different team. Here they are one pipeline. The article, its graph, its summaries and its sources are written by the same agent, checked by the same build and released as one commit. That is easier in a newsroom of one editor and a team of agents than in SPIEGEL's, but the principle carries: the breakdown has to be released with the story, or it will drift from it.

On MCP and publishers' own tools, our reader API is a start rather than an answer. I would like to compare notes: what an agent asks for first, what it pays for, and how the right of reply travels with the fragment it takes away.

## What this does not claim

- **I have not seen SPIEGEL's workflow.** Everything about it here is from Ole Reissmann's public post; I may be describing it too simply.
- **Our counts are from this site's files on 30 October 2026,** taken before this article and the IAM reply were added.
- **Our summaries and graphs are written by an agent** and checked by scripts for form, quotes and staleness, not for judgement; their judgement is reviewed when an article is reviewed.
- **The allegation field is a proposal;** it is not in our graphs yet.

## Where this comes from

- Ole Reissmann's post on LinkedIn after the News Product Alliance Summit in Chicago, shared with me as screenshots on 30 October 2026; the quotations are copied from it.
- This site's own files: `articles/graphs/` (327 graphs), `admin/content/articles/summaries/`, `llms.txt`, `newsroom-api/`, `admin/writer/tools/graph.py` and `admin/build/summaries.py`; the book's claims register in [SGit-AI/SGit-AI__Website__Book__The-Ultimate-Insider](https://github.com/SGit-AI/SGit-AI__Website__Book__The-Ultimate-Insider) (`claims/`).
- Related: [the wire as a graph](the-wire-as-a-graph.md), [sources and their shadows](sources-and-shadows.md), [on the record](on-the-record.md), [signed by the source](signed-by-the-source.md).

## Threads

News & evidenceGraphs & knowledge[This article as a graph →](graphs.md#breaking-the-story-down-before-the-agents-do)

### Builds on

- [Sources and their shadows: the licence, the access, the links and the quotes of every reference, how a paywalled article can be seen through what others say about it, and paying the sources we use](sources-and-shadows.md) Each reference's licence, access, links and quotes, reading a paywalled article through its shadow, and paying the sources we use.
- [The wire as a graph: start from what the reader sees, give every story and every name a long-lived ID, link every phrase of a short narrative, and a brief for the desks](the-wire-as-a-graph.md) Design the wire from what the reader sees: every name a link with a long-lived ID, every sentence a claim, stories of stories, folders by gravity.
- [On the record: signed opinions from experts, paid when readers value them, and a share for the people whose ideas an article uses](on-the-record.md) Experts go on the record with signed opinions, readers pay for the ones they value, and the people whose ideas an article uses get a share.
- [Signed by the source: asking the people and companies we quote to sign that we represent them correctly, why that is cheaper than every reader checking, and how readers go on the record too](signed-by-the-source.md) Ask the people and companies we quote to sign that we represent them fairly: one signature instead of every reader checking.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 330 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=330)

**Posting this article on LinkedIn?** The cover is [breaking-the-story-down-before-the-agents-do.jpg](banners/breaking-the-story-down-before-the-agents-do.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/breaking-the-story-down-before-the-agents-do.html)*
