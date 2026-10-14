# Story vault underneath, Reader Skills on top: why local journalism has the most to gain, sgit.ai

> Markus Franz published "The Article Is Only the Beginning" on 7 October 2026, proposing Liquid Utility, journalism that helps people understand, follow and act rather than only read, and six Reader Skills to deliver it, with a bridge closure as the example. He then wrote, under my comment, that his idea and the story vault connect at an architectural level: the story vault answers what we know and why it can be trusted, Reader Skills answer what we can reliably help someone do with it. This article draws that connection. Each of his six skills turns out to be an operation the story graph already supports, and each safeguard he asks for is a property the graph already has: versions for Update, supersede edges for corrections, freshness for "could not check", a flag at the node for protected sources. His bridge is drawn as a graph. And his article adds the piece our monetisation had not mapped: locality, where the trust relationship and the brand are strongest. Local contributors feed local journalists, local stories feed national and international ones, and if every use pays back down the chain of claims it rests on, small payments from many people fund the reporting nearest to them.

*Source: <https://newsroom.sgit.ai/articles/story-vault-meets-reader-skills.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Story vault underneath, Reader Skills on top: why local journalism has the most to gain

# Story vault underneath, Reader Skills on top: why local journalism has the most to gain

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-07 · [article v1.5.0, 6 versions](versions/story-vault-meets-reader-skills.md) · [sgit.ai v0.6.94](https://sgit.ai/admin/versions.md) · journalismlocal-newsliquid-utilityreader-skillsstory-vaultfractal-semantic-graphsprovenancemicropaymentsverificationarticle

***Abstract:** Markus Franz published "The Article Is Only the Beginning" on 7 October 2026, proposing Liquid Utility, journalism that helps people understand, follow and act rather than only read, and six Reader Skills to deliver it, with a bridge closure as the example. He then wrote, under my comment, that his idea and the story vault connect at an architectural level: the story vault answers what we know and why it can be trusted, Reader Skills answer what we can reliably help someone do with it. This article draws that connection. Each of his six skills turns out to be an operation the story graph already supports, and each safeguard he asks for is a property the graph already has: versions for Update, supersede edges for corrections, freshness for "could not check", a flag at the node for protected sources. His bridge is drawn as a graph. And his article adds the piece our monetisation had not mapped: locality, where the trust relationship and the brand are strongest. Local contributors feed local journalists, local stories feed national and international ones, and if every use pays back down the chain of claims it rests on, small payments from many people fund the reporting nearest to them.*

Where the two ideas meet: each of Markus Franz's six Reader Skills as an operation on the story graph, and the property of the graph that makes it dependable. The skills are his; the mapping is ours.

A bridge closes for six weeks. The reporting is clear: what happened, why the repairs are needed, who is responsible. And the parent reading it on Sunday evening still has three questions. Can the children take their usual bus tomorrow? What changes on Monday morning? Will someone tell me if that changes again?

That is the opening of [The Article Is Only the Beginning](https://www.linkedin.com/pulse/article-only-beginning-markus-franz-qzyqe/), published by Markus Franz on 7 October 2026, and it holds two lines worth keeping: *"The article has done its job. You still have a job to do."*

His proposal is called **Liquid Utility**: trusted journalistic knowledge, combined with reusable methods and appropriate tools, to help someone understand, follow or act on what matters to them. He delivers it through six **Reader Skills**, bounded journalistic capabilities a reader can use directly: Understand, Update, Relate, Compare, Follow and Act. It is careful about what it does not claim. A skill is not a safety guarantee. The case for a publisher over a generic assistant has to rest on original access, maintained data, local reporting and editorial accountability, and even then the service has to be demonstrably better at a particular task. And the business test is kept visible: reach, utility, relationship, reciprocity, measured rather than assumed.

I replied under his post that this is close to what I argue in [The future of news is the story vault, not the paywall](future-of-news-story-vault-not-paywall.md). His answer is the reason this article exists:

**Markus Franz, in reply.** "Your Story Vault starts underneath the article: claims, evidence, sources, versions and provenance become the durable asset, while the article is one projection of that graph. Liquid Utility starts from the other end: the reader has a job to do, and journalism should turn trusted knowledge into a capability. [...] Story Vault answers: what do we know, and why can it be trusted? Reader Skills answer: what can we reliably help someone do with it?"

He is right, and the connection is tighter than either article said on its own. This is the drawing of it.

One story, four ways in

Read them in order, or start with the one you need: the idea, the connection, the simulation explained, and the working vault.

[1 · The originalThe Article Is Only the Beginning ↗Markus Franz's proposal: Liquid Utility, six Reader Skills, and a bridge closure as the example.](https://www.linkedin.com/pulse/article-only-beginning-markus-franz-qzyqe/)[you are here2 · The connectionStory vault underneath, Reader Skills on topWhy his skills and the story vault are two halves of one system, and why local journalism has the most to gain.](story-vault-meets-reader-skills.md)[3 · The simulation, explainedThe bridge, followed to the endOne closure from first notice to reopening: the journalism, three readers, the buyers, the money, and two years on.](the-bridge-followed-to-the-end.md)

4 · The vaultThe Mill Street BridgeThe working simulation: 23 views in four themes, the economics, an API, and every assumption written down. Fictional throughout.[The vault's page](https://sgit.ai/demos/vaults/bridge-simulation/index.md)[Open the vault ↗](https://dev.vault.sgraph.ai/#sgit_public_read_cb3838a0e965dc9d5af9009fef6e867dbdf18a8fc615cb3f5f2bee5424639705%3Avk3jlgzb)

## Each Reader Skill is a question the graph can already answer

The story vault keeps what was reported as a graph: claims, each tied to evidence that has been fetched, saved and hashed; sources, with how recently each was checked; versions, where a correction supersedes a claim rather than deleting it. The article is one projection of that graph. The figure at the top puts Markus's six skills on top of it, and each one becomes an operation.

Take his own description of **Update**. He writes that "summarise the latest article" is not enough: the method *"would need to establish the previous information state, retrieve current reporting, separate new facts from repetition, flag corrections and show the sources behind each meaningful change."* Every clause of that is something a versioned graph gives you directly. The previous information state is the version the reader last saw. New facts are new claim nodes. Corrections are supersede edges, dated. The sources behind each change are the edges from each new claim to its evidence. Over a pile of articles, Update is a summarisation problem. Over a story graph, it is a diff.

**Follow** is the same diff, run on a schedule for claims the reader chose. Markus adds a line that matters more than it looks: *"If it cannot check, it should distinguish that from confirming that nothing changed."* That distinction needs freshness, a record of when each source was last checked against what the claim says, and the vault keeps exactly that. **Understand** is a walk from a claim to its sources and the open questions. **Compare** sets two claims or two versions side by side, with the typed edges between them, so that "the council says one date and the operator another" is recorded where a reader meets it. **Act** turns the current claims into a checklist or a reminder, from rules somebody maintains.

**Relate** is the one that changes the privacy story. Markus writes that *"a neighbourhood update should not require an entire personal profile."* In the vault model it does not need one at all. The reader's route is held on the reader's side, and joined to the published graph there; the newsroom serves claims and does not learn which bus a family takes.

The same is true of his safeguards. *"A correction cannot stop at the article while personalised answers continue repeating the old claim"*: in a graph, a correction is a supersede edge, so every skill that read the old claim meets the new one. Source protection must survive the move into reader products: an anonymous source is flagged at the node, and every projection, the article, a licensed extract, a skill's answer, redacts it without anybody having to remember. The thing he calls *Journalism as a Capability System* needs a substrate where the knowledge keeps its qualifications. The story graph is that substrate.

## The bridge, drawn

Markus Franz's bridge, as a story graph: evidence at the bottom, including a resident's photo; the claims a local journalist wrote from it; the article and three Reader Skills as projections; and the reader's own route, joined on the reader's side. Places, dates and hashes are illustrative.

Here is his example as a graph. The council notice, the operator's diversion plan and a resident's photo of the site notice are evidence, each saved and hashed. The local journalist checked the photo against the notice and wrote three claims from them. The article of 9 October is one projection. When the council moves the reopening date on 21 October, nothing is rewritten: a new claim supersedes the old end date. That single edge is, at once, the **Update** a returning reader sees, the **Follow** alert sent to everybody tracking the closure, and the correction. On the reader's side, their route, bus 42 at 08:05 from Elm Street, is joined to the claim about the diversion, and **Relate** answers: from 13 October, that bus stops at Station Road, with the source and when it was checked.

The reader does not need to see any of this, and Markus is right that they should not have to: *"The reader does not need to admire the architecture. The reader needs it to work."* The graph is what makes it work, and what makes the working checkable.

## What his article adds: the job, and the place

My story vault article started from the evidence and asked what a newsroom could sell from it. Markus starts from the person and asks what they need done. The second view brings something into focus that I had thought about and not mapped: **locality**.

Almost everything that touches our day is local. The road we drive, the school run, the high street, the planning application at the end of the street, the bridge. The local paper, or the local reporter, is where a trust relationship and a brand form over years, because they are right about the things we can check ourselves. Journalists save us time, and what they sell is trust. Locally, both are easiest to see: I can tell within a week whether the reporting about my own street was right.

People already pay a little for that, and would pay for more of it if paying were easy and the thing paid for were useful. A pound a month for knowing what changes on my bus route, pence for a check on a planning decision, a small amount each time the reporting saves me an afternoon. Small, from many people, about the things nearest to them, is a large amount in aggregate. Markus is careful here, and so should I be: *"Locality alone is not the advantage. Doing that work reliably could be."* The vault is how the reliability becomes something a reader, or an agent, can verify rather than assume.

## Local is where the facts are found, so let the money flow back to it

The proposal: facts and their evidence travel up from a local contributor to an international wire; every use of them pays back down the same edges. The split is illustrative; the mechanism is the point.

There is a second local element his article opens up, and it is the one I find most interesting commercially. Local journalism has local sources. A resident who photographs the notice. A bus driver who mentions the diversion before it is announced. A parish clerk whose minutes say the repair was deferred twice. In many newsrooms those people are thanked, if they are mentioned at all. In a story graph they are nodes: named, or flagged as anonymous, linked to the claims their evidence supports, and verified by the journalist who checked them.

And stories travel up. The local closure becomes a regional story about every closure on the river this winter, then a national story about ageing bridges, then an international one about infrastructure spending. Each of those cites the level below, or should. Today the money flows the other way and stops at whoever publishes last. In a graph where every claim names who found it, a national story that rests on a local claim can pay for it, per use, in pence, automatically; and a local claim that rests on a resident's photo can pass a share to the resident. The figure shows one illustrative split of one 10p use. The numbers are a proposal. The mechanism is not: *a page that cannot name its source cannot pay it.*

The same edges carry trust upwards. A national story is more credible when the local source under it is named, verified and current, and the **verification API** in the story vault design, a paid answer to "did you report this, and is it still current?", is exactly what Markus picked out in his reply as the maintained capability that moves journalism beyond the static article. Asked by a national desk about a local claim, it is how the local newsroom gets paid for being right.

That gives the loop its shape. Trust in a local brand brings use. Use, through skills that solve a local job, brings payment, in small amounts from many people and in larger ones from the outlets that cite the local work. Payment funds the next local story and the contributors behind it. More, better-sourced claims reinforce the trust, at the local level and at every level above it that cites them. It is the opposite of the hollowing out described in [how news got here](how-news-got-here.md), where the local monopoly went first and the reporting followed.

Two honest notes, as before. Nothing on sgit.ai is wired to a payment rail today; the rails exist, and the design names them, but no contributor has been paid through a graph yet. And none of this works unless the service is better than the alternative for a real task, which is Markus's test and the right one.

## What a publisher could test, with both halves

Markus's advice is to start with *"one maintained topic and one tightly scoped service"*, a local disruption tracker or a "what changed?" service, and to measure it on reach, utility, relationship and reciprocity. I would keep all of that and add three things, one from each layer underneath.

- **Keep the topic as a story vault from day one.** Every claim tied to saved evidence, every correction a supersede edge. The Update and Follow skills are then diffs, not summaries, and their answers can be checked.
- **Record the contributors in the graph from day one.** Name them, or flag them, and link them to what they supported, so that when payment arrives there is somebody to pay.
- **Publish the ledger.** What was used, by whom, and where the money went, so that the reciprocity Markus wants to measure is visible to the readers being asked for it.

One local topic, one vault, one service, one ledger. If it works, the second topic is cheaper, because the methods are reusable, which is his point, and the graph grammar is shared, which is mine.

## Played out in full

The bridge, the readers, the journalism and the money are now a working simulation: [The bridge, followed to the end](the-bridge-followed-to-the-end.md), with its [vault](https://sgit.ai/demos/vaults/bridge-simulation/index.md), which since version 0.2 also counts the costs, the two years of long tail, the stories after it and the trust they build. Three readers, three institutions and an agent use one local story kept as a graph, from the first notice to the reopening, and every payment walks back to the people who found the facts.

Markus ends his article with this line: *"Don't just read our journalism. Use it."* I would add one clause. Use it, and pay the people who found it out.

## Two infographics

ChatGPT made an infographic of this article from its published text, and another of Markus's article, which I posted under his LinkedIn post. Both are worth having, and both are worth reading against their source, so each has a note.

The infographic of this article, made with ChatGPT from its published text. Faithful on the two questions, the graph underneath, the six skills, the safeguards, locality and the place to start; the note below says where it departs.

**Reading it against this article.** It follows the argument closely: what the story vault answers and what Reader Skills answer, the graph underneath with evidence, claims and versions, each skill as an operation on it, the safeguards, locality, facts travelling up and attribution flowing back down, and one topic, one vault, one service, one ledger. It is careful in the right place, marking the micropayments as proposed and not yet implemented, which is what this article says. Three things to know. Its bridge has its own illustrative dates: closed from 7 October and reopening on 20 October, moved earlier from the 27th, where the figure above has the bridge closing on 13 October, the council notice dated 9 October and the reopening moved later, from 24 November to 1 December. Its closing line says "credit the people who found it", where this article says pay them, and paying them is the point. And "Trust turns local information into lasting value", like the words in the margins, is the infographic's own; one of those words is misspelt, "informalton".

The infographic of Markus Franz's article, made with ChatGPT from the article's text and posted under his LinkedIn post, where he replied that he liked "how clearly you visualised the shift from Liquid Content to Liquid Utility". Faithful on the six skills, the layers and the safeguards; the note below says what it adds and what it drops.

**Reading it against Markus's article.** It gets the substance right: the gap, Liquid Utility, the six Reader Skills, the layered system, the safeguards and the advice to start small. Four things to know. The taglines ("Same facts. A more useful tomorrow", "People informed, people empowered, stronger societies", "Real journalism. Greater possibilities") and the line "Trust turns useful services into lasting relationships" are the infographic's, not Markus's. "An AI feature alone is not the advantage. Reliability is" is a fair compression, but his own wording is more careful: the publisher's case *would have to rest* on original access, maintained data, local reporting and accountability, and even then the service must be demonstrably better for a particular task. It drops his qualifiers, that the six skills are a proposed framework rather than a universal taxonomy and that reach, utility, relationship and reciprocity are a hypothesis to measure rather than a funnel. And it leaves out his evidence on search and clicks, and his boundary that "relevant to me" must not become "nothing beyond my immediate interests".

*Drafted from Markus Franz's article and LinkedIn post of 7 October 2026, his reply to my comment, and a voice note by Dinis Cruz, who is the author of the argument and the person with editorial responsibility, by agent@riskmandate.ai (Claude Opus 5.5, claude-opus-5-5) in the sgit.ai site session, on 7 October 2026. Quotations from Markus Franz are from his published article and his public reply, credited and linked; Liquid Utility, Reader Skills and Journalism as a Capability System are his terms. The mapping, the bridge graph, the payment chain and its illustrative split are ours. Places, dates and hashes in the bridge figure are illustrative.*

## Threads

News & evidenceGraphs & knowledge[This article as a graph →](graphs.md#story-vault-meets-reader-skills)

### Builds on

- [The future of news is the story vault, not the paywall](future-of-news-story-vault-not-paywall.md) A story is a graph of claims and evidence and the article is one projection of it; keep the graph in a vault and sell what the article was made from.
- [The reader was always the product: a corrected history of how news got into this mess](how-news-got-here.md) News has sold the reader to advertisers since 1833; the web took the monopoly, the platforms made the reader measurable, and AI took the traffic.
- [The bridge, followed to the end: what one local story is worth when it is kept as a graph](the-bridge-followed-to-the-end.md) A bridge closure simulated on a story vault: newsworthy on 5 days, needed on 57, used by three readers, four buyers and an agent, and paid back to its sources.

### Continued by

- [Ways to read one article: the finished piece stays at the centre, and the reader picks the way in](ways-to-read-one-article.md) The five readers' views arrived as folds inside the long piece; now the reader picks the way in, with a default, and the finished article stays at the centre.
- [The article remains a product: Jonathan Palmer's four outputs for a newsroom with no human readers, checked against one that runs](the-article-remains-a-product.md) Jonathan Palmer's four outputs for a newsroom with no human readers, quoted line by line and checked against newsroom.sgit.ai as it runs, screenshots included.
- [The waiting room knew first: a live local story, and the gap where local information used to be](the-waiting-room-knew-first.md) Staff at two London hospitals said the IT was down; nothing a local could check showed it. A live local story about where local information comes from now.
- [The bridge, followed to the end: what one local story is worth when it is kept as a graph](the-bridge-followed-to-the-end.md) A bridge closure simulated on a story vault: newsworthy on 5 days, needed on 57, used by three readers, four buyers and an agent, and paid back to its sources.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 40 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=40)

## From the desk

- [Local news, kept as evidence](collections/local-news-kept-as-evidence.md) collection, 6 articles

**Posting this article on LinkedIn?** The cover is [story-vault-meets-reader-skills.jpg](banners/story-vault-meets-reader-skills.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/story-vault-meets-reader-skills.html)*
