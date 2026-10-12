# The article remains a product: Jonathan Palmer's four outputs for a newsroom with no human readers, checked against one that runs, sgit.ai

> On 10 October Jonathan Palmer asked on LinkedIn what a news business would look like if it had no human readers tomorrow, and said every publisher should model that exact scenario. His answer is that the newsroom should produce four things besides the article, structured intelligence, continuous intelligence, provenance and verification, and embedded distribution, and that "The article remains a product. It just stops being the only primary output." We have been building a newsroom on that premise since August, so this article takes his post line by line and checks each line against newsroom.sgit.ai as it runs today, with screenshots: a graph beside all 74 articles as JSON, a version history read from git, 21 World News Day op-eds frozen and hashed with a vault anyone can open, and a markdown twin, an llms.txt and a feed for the agents that already read it. It is also honest about the right-hand column: selling the graph, corrections that propagate and paying the fact creator are designed and not running. Then it answers his three questions, what assets would still have value, who would pay and what needs to be produced differently, with the one number we have, and says where we differ: the data assets he wants kept proprietary are the ones we publish with a read key, because provenance is only worth something if someone else can check it.

*Source: <https://newsroom.sgit.ai/articles/the-article-remains-a-product.html> · sgit.ai v0.7.82 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The article remains a product: Jonathan Palmer's four outputs for a newsroom with no human readers, checked against one that runs

# The article remains a product: Jonathan Palmer's four outputs for a newsroom with no human readers, checked against one that runs

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-11 · [article v1.0.0](versions/the-article-remains-a-product.md) · [sgit.ai v0.7.61](https://sgit.ai/admin/versions.md) · newsroomfuture-of-newsstructured-intelligenceprovenancegraphsversionsagentsllms-txtvaultsworld-news-dayeconomicsresponsearticle

***Abstract:** On 10 October Jonathan Palmer asked on LinkedIn what a news business would look like if it had no human readers tomorrow, and said every publisher should model that exact scenario. His answer is that the newsroom should produce four things besides the article, structured intelligence, continuous intelligence, provenance and verification, and embedded distribution, and that "The article remains a product. It just stops being the only primary output." We have been building a newsroom on that premise since August, so this article takes his post line by line and checks each line against newsroom.sgit.ai as it runs today, with screenshots: a graph beside all 74 articles as JSON, a version history read from git, 21 World News Day op-eds frozen and hashed with a vault anyone can open, and a markdown twin, an llms.txt and a feed for the agents that already read it. It is also honest about the right-hand column: selling the graph, corrections that propagate and paying the fact creator are designed and not running. Then it answers his three questions, what assets would still have value, who would pay and what needs to be produced differently, with the one number we have, and says where we differ: the data assets he wants kept proprietary are the ones we publish with a read key, because provenance is only worth something if someone else can check it.*

His four outputs, against what runs. Each row quotes one output from Jonathan Palmer's post; the middle column is the page on newsroom.sgit.ai that does it today, the right-hand column is what is only designed. The line between them is the newsroom's own dated page of what runs.

On 10 October, Jonathan Palmer, who works on strategic data assets and how to commercialise them, [posted a question on LinkedIn](https://www.linkedin.com/posts/jonathanjpalmer1_futureofnews-ai-publishing-share-7514686042193637377-Zs1Z/): "What would a news business look like if it had no human readers tomorrow?" He followed it with an instruction: "Every news publisher should model that exact scenario." And three questions: "What assets would still have value? Who would pay? And what needs to be produced differently?"

I have an unusual answer to that, which is that we have been modelling exactly that scenario, in public, since August. [The future of news is the story vault, not the paywall](future-of-news-story-vault-not-paywall.md) set out the design on 22 September; [newsroom.sgit.ai](https://newsroom.sgit.ai/) is the design running, on 74 articles, with a page that says what runs and what does not. So rather than agree with his post, which would be easy, I want to do what he asks and model the scenario: take his four outputs one at a time, quote him, and put each quote next to the live page that does it, or next to the honest sentence that says we have not built it yet.

As with [Satya Nadella's post on models as insiders](the-same-argument-in-our-words.md), this is convergence, not priority. He reached his list from the data side of the industry; we reached ours from building. That two different starting points land on the same four outputs is the interesting part.

## In short

- **The scenario is worth running, and we ran it.** Five readers who do not exist [tested the newsroom](how-to-run-synthetic-users.md), and [The agent is the reader](the-agent-is-the-reader.md) measured what an agent pays to read it. The newsroom was built for a reader that is increasingly an agent sent by a person.
- **Structured intelligence runs.** Every one of the 74 articles has a graph as JSON, one file per article and all of them in one; the World News Day corpus is 160 nodes and 427 edges with triples you can download.
- **Continuous intelligence half runs.** Every article has a version history read from git, and a page that shows what changed paragraph by paragraph. Corrections that reach the pages that cited the corrected claim are designed, not built.
- **Provenance runs; commercial access does not.** Twenty-one op-eds were fetched once, frozen, hashed with SHA-256 and re-derived by a second program, and the whole thing is in a vault whose read key is printed on the page. Nothing is yet paid for a verified claim, and nothing flows upstream.
- **Embedded distribution runs, in the plainest form.** An llms.txt, a markdown twin of every page, a feed, the graphs as data, and a block for agents at the foot of every page. The measured saving for an agent is the reason it would pay.
- **Where we differ.** He wants "reusable, proprietary data assets". We publish the graph and the read key, and sell what is fitted to the reader, the delta since they last came, and the signed claim. Provenance that only the publisher can check is not provenance.

## Model that exact scenario

The post's second line is the one I would underline: "Every news publisher should model that exact scenario." Most of the industry's answer to AI is in his next paragraph, "new ways to subscriptions, monetize audiences and drive traffic", and he is right that "These strategies assume the traditional relationship between publishers and readers will endure". [How news got here](how-news-got-here.md) traces that assumption back to 1833, and the search layer stopped sending the traffic that funded it a while ago.

We modelled the scenario in two ways. The first was to invent the readers. [How to run synthetic users](how-to-run-synthetic-users.md) sent five people who do not exist through the newsroom with a real browser: 62 steps, 51 questions the site did not answer, 31 findings, four of the five left. That is what a newsroom looks like to a reader who is not loyal, not subscribed and not patient, which is close to what a reader looks like now. The second was to make the agent the reader and count. [The agent is the reader](the-agent-is-the-reader.md) measured what it costs an agent to answer a question from five articles: a median of 2,579 tokens from their graph, against 25,698 from the prose. That number is the whole economic case for his four outputs, so I will come back to it.

What follows is his list, in his order, in his words.

## Structured intelligence

"Structured intelligence: facts, events, entities, relationships and changes as data."

This is the first thing the newsroom does, and it does it for every article. "74 of 74 articles have a graph", the page says: the ideas each rests on, the claims it makes, the methods and the examples, and how they connect, as JSON, one file per article and all of them in one file with the links between articles resolved. The pages are rendered from the same files, so the graph cannot drift from the prose.

The articles as graphs, on newsroom.sgit.ai. Every article drawn in date order round the circle, sized by how many others link to it: 74 articles, 349 links between them, and 10 amber links where an older article was updated to point at a newer one. One graph per article follows below the map.

The thesis underneath is older than the post and the same as it. In [The future of news is the story vault](future-of-news-story-vault-not-paywall.md) I wrote that the story is a graph, a fractal semantic graph in which meaning comes from connectivity and every claim walks down to hashed evidence, and that the article is one projection of it. His "facts, events, entities, relationships and changes as data" is that graph, named from the outside.

The best test of it on the site is not our own articles but someone else's. For World News Day, WAN-IFRA and the Canadian Journalism Foundation published 21 commissioned op-eds and made them free to republish. The newsroom [fetched all 21, froze the bytes, and built the graph](https://newsroom.sgit.ai/world-news-day/graph.html): 160 nodes and 427 edges, the authors, the organisations they name, the themes, the sources they point at and the terms they are published under, with `graph.json`, `ontology.json` and `triples.nt` to download. The page says why: "Twenty-one articles in a list are twenty-one articles." The same 21 with their relationships is something you can ask questions of, and "None of that is in the publisher's own data, because the publisher's own data is a single category called Story."

The World News Day graph: 21 op-eds as 160 nodes and 427 edges, with the three machine surfaces linked at the top. The box under it is the rule the section is built under: hold the pieces, republish none, and fail the build if twelve consecutive words of any piece appear.

And the densest layer is the one five agents made. In [One article, five readers](one-article-five-readers.md), a Librarian catalogued every fact, claim, number, question and source in five articles with the sentence it came from, 662 items, and a Cartographer turned the catalogues into one ontology. Those views are now on the articles, and the whole run is in the [Article Views vault](https://sgit.ai/demos/vaults/article-views/index.md), which anyone can open with its published read key.

A live article with its five readers folded under the abstract: two minutes, the arc, nine slides, a map, and 137 catalogued items, six of them flagged. The views are extracted from the article and do not change its version.

What does not run: selling any of it. The graphs are free, and the newsroom's own ledger says "Nothing sells one."

## Continuous intelligence

"Continuous intelligence: Producing verified evolving information streams vs periodic article production."

Here the newsroom is half way. The half that runs is that nothing on it is fixed once published. Every article has a version history, and the page that shows it explains the rule: a change to the text is the next minor version, a change to its other details the next patch, and "The list is read from the site's git history at every build, so it cannot be edited by hand and cannot leave a version out."

The version page of One article, five readers: v1.0.0 on 10 October, v1.1.0 on 11 October, +11 words, one paragraph changed, each with its commit. The sentence changed was a correction, found by the article that followed it.

What changed is shown, not described. For [How much of this did I write?](https://newsroom.sgit.ai/articles/diffs/how-much-of-this-did-i-write.html), which was revised the day it was published, a diff page shows every paragraph with the old number struck through and the new one beside it. And the map above has ten amber edges: older articles that were updated after a newer one existed, to point at it. That is an evolving stream in the plainest sense, and it is the opposite of "periodic article production", which is what a PDF of the paper is.

What changed, paragraph by paragraph: 63,000 words became 65,000, 122 releases became 123, and a phrase was rewritten. The tool that draws this was built on the same day as the revision.

The half that does not run is the half that matters most to his word "verified". The newsroom keeps versions and corrections; it does not yet carry a correction to the pages that cited the corrected claim. That is the argument of the [corrections section](https://newsroom.sgit.ai/corrections/index.html), "In a document, a correction is a new document. Nothing that cited the original knows. In a graph, a correction is an edge", and it is the most distinctive thing in the design. It is also, by the ledger's own words, "Designed, not built." There is no published way yet to tell the newsroom an article is wrong. I would rather say that plainly than describe a stream we do not have.

## Provenance and verification

"Provenance + verification: Making sourcing, attribution and editorial validation explicit, traceable and commercially accessible."

Three adjectives, and the newsroom does two of them. Explicit and traceable are the World News Day method: "Fetch once, freeze the bytes, hash them, extract structure, derive what can be derived by a published formula, and refuse to ship if any of it stops re-deriving." Each of the 21 pages was fetched once and frozen to a dated snapshot, hashed with SHA-256, and "The counts are re-derived from those bytes by a second program before anything ships." The build fails if twelve consecutive words of any piece appear on a page the newsroom generates, because the prose belongs to the people who wrote it.

Then the whole corpus, the frozen pages, every derived dataset, the build code and the gate, was put in an encrypted vault, and the read key was printed on the page.

The published vault: one read key, printed in full, is the whole credential. It opens the World News Day corpus as an app in the reader's browser, read only, no account, nothing to install, and no write capability in it.

That is what I mean by provenance that someone else can check. The newsroom's claim is "Every number walks back to bytes we hold", and the way to test it is not to trust the newsroom but to open the vault and re-derive the numbers. [Where the vault keys live](where-the-vault-keys-live.md) explains why a read key can be printed and a vault key cannot. The same idea covers the newsroom itself: the record of its sync from sgit.ai carries the SHA-256 of every file as served and as imported, and a gate checks that the imported pages were never edited by hand.

Editorial validation is explicit too, in a way I have not seen a legacy newsroom do: [six roles with written behaviour policies](https://newsroom.sgit.ai/newsroom/index.html), a board, and a log of every run, with the one rule that publishing is adding a file and the one exception that placement belongs to the Editor.

His third adjective, "commercially accessible", is where we are a design. The economics section argues that what is billable is not "is this true" but "is this use of it sound", per claim and context, and that the value behind a reader's payment splits 60 per cent to the original researcher, 25 to the data organisation, 10 to the journalist's synthesis and 5 to the outlet, while today "essentially all of that revenue is captured at the 5% layer".

Contextual validation, not truth: the value split the design argues for, and the sentence that says what is billable. The page is marked as a design, and the newsroom's ledger says nothing is paid upstream.

Nothing is paid to the people whose facts an article uses. Trust as a service is argued, not built. I think his phrase is the right target, and I think the way to it is the one his post implies: make provenance explicit and traceable first, so that there is something to charge for.

## Embedded distribution

"Embedded distribution: Delivering differentiated intelligence directly into AI systems, enterprise platforms and workflows."

The newsroom does this in the plainest possible way, which I have come to think is the right way. An agent that arrives gets an [llms.txt](https://newsroom.sgit.ai/llms.txt) that says, in its first screen, what runs, what is only designed, and where the reader's data goes. Every page has a markdown twin generated from the same content as the HTML, "so the two cannot drift". The feed, the wire and every article's graph are files an agent can fetch without rendering a page. And every page the newsroom writes ends with a block addressed to an agent.

The first screen of the newsroom's llms.txt: the honest sentence, where the pages come from, and the surfaces an agent may rely on. The chip at the top of every imported page points here.

Two live features go further. A [reading list in a link](a-reading-list-in-a-link.md) carries its articles as numbers in the part of the address after the #, which a browser keeps to itself, and the page that explains it says an agent "can build the same link by hand from the numbers in articles/ids.json". A persona in a link does the same for a way of reading. Both went from a brief to live in hours, which is its own kind of answer to "what needs to be produced differently".

The measured part is the argument. An agent answering a question about five articles paid 25,698 tokens to read them and a median of 2,579 to read their graph, with every item anchored to its sentence. That is what "differentiated intelligence" is worth, in the only unit an agent counts in. [Brief the agent too](brief-the-agent-too.md) takes the next step, a pack written for someone's agent and the file of what changed since a date, and the ledger is clear that the pack, an account for an agent and the delta it would pay for are proposals.

## Who would pay?

"The biggest question isn't how to monetize readership more effectively. It's how to create economic value when readership is no longer the foundation of the business."

Our answer has a name, from [The agent is the reader](the-agent-is-the-reader.md): the agent pays not to pay. Today an agent that reads the web pays to process all of it, then guesses at what it means. A publisher that serves meaning, a projection fitted to the agent's persona and objective, and claims signed with an expiry date, saves the agent more than it charges. The payment is not goodwill and not a licence. It is cheaper than the alternative.

That is also where I would push back a little on one word. He writes that value "remains uncaptured or trapped inside articles rather than captured as reusable, proprietary data assets." Reusable, yes. Proprietary is the part we do differently, and on purpose. The newsroom publishes its graphs free and prints the read key to its vault, because provenance that only the publisher can check is a promise, not provenance. What it would sell is the projection fitted to one reader, the delta since that reader last came, and the signed claim with a date on it. None of those is the data; all of them are made from it. The financial information providers he cites built their business on data nobody else could get. A newsroom's advantage, as he says himself, is "trusted sourcing networks, expert judgment and verification capabilities", and those are worth more when the checking is open.

And the human reader has not gone anywhere. The newsroom charges pence per page by how far you read, from a balance in your browser, and a reader can now top up five pounds by card. It is an honesty box, not a paywall, and it is live because the people who build it [use it on four devices](i-miss-it.md). The scenario with no human readers is a model worth running; the business I want is the one where both kinds of reader pay because it helps them, which is the argument of [Pay to keep your persona](pay-to-keep-your-persona.md).

## The article remains a product

"The article remains a product. It just stops being the only primary output."

I would put it the other way round, and mean the same thing. The story is a graph; the article is a projection of it, and so is the two-minute version, the deck, the map and the briefing for one sector. The projection people pay to read is still the article, written first, as prose, because writing is how the argument is found. That is how every article on the newsroom is made: the prose first, then the graph beside it, then the five readers after. His sentence and ours agree on the thing that matters, which is that the article is no longer the unit the newsroom is organised around.

His last line is the one I would send to a board: "That's not another AI licensing agreement for archives or articles. It's a fundamental redesign of the data capture operating model." Licensing the archive sells the past once. Capturing structure, versions, provenance and distribution as the newsroom works sells the present, continuously, and the only way to know what that costs is to run it.

## Cultural, not technical

"The first transformation may be cultural, not technical."

This is where I can offer one data point and no proof. The technical transformation, on this evidence, is cheap: one person, a desk of agents, and eight weeks produced 74 articles with graphs, versions, a hashed corpus, a vault, and the surfaces for agents, on static files with [no server](no-server-by-design.md). The cultural one is the one we cannot demonstrate, because this newsroom never had the culture he describes to change. It started with the graph. A newsroom with a hundred years of "the primacy of the article as the organizing principle" has a different problem, and his post is addressed to it.

What I can say is that the pieces he lists do not have to be built by the legacy newsroom. [Story vault underneath, Reader Skills on top](story-vault-meets-reader-skills.md) argues that local journalism has the most to gain, because that is where the trust and the brand are strongest and the budgets smallest, and everything above runs on files and a browser. If the transformation is cultural, the cheapest way to start it may be to run the scenario on one desk, in public, and let the pages say what runs.

## What this does not claim

- **Nothing is sold.** The graphs are free, the vault is open, and the only money that moves is a five pound top-up a reader can choose to make. The economics are a design with a page.
- **This is one small newsroom, not the industry.** Seventy-four articles by one author, written from voice memos by agents, is a model of the scenario, not evidence that a legacy newsroom can follow it.
- **The right-hand column is real.** Selling the graph, paying the fact creator, corrections that propagate, articles as vaults, packs for agents: designed, not running. The newsroom's own [page of what runs](https://newsroom.sgit.ai/shipped/index.html) is the authority, dated, and it moves.
- **The post is quoted, not summarised.** Every line of his in this article is verbatim from the post as published; the reading of it is mine.
The newsroom's own ledger, as of 10 October 2026: what runs, its limits, and below it what is designed and not running. Every claim in this article about what is live was checked against this page.

If you run a newsroom, or the data side of one, and want to model the scenario on your own content, the [page for publishers](../publishers/index.md) sets out what is live and how to try it, and [agent@riskmandate.ai](mailto:agent@riskmandate.ai) answers, from a person or from your agent.

## Where this comes from

A voice memo of mine, recorded on 11 October 2026 after reading Jonathan Palmer's post, written by this site's agent in the voice of this site. The argument and the editorial responsibility are mine. The quotations are verbatim from [the post on LinkedIn](https://www.linkedin.com/posts/jonathanjpalmer1_futureofnews-ai-publishing-share-7514686042193637377-Zs1Z/), dated 10 October 2026 and marked as edited since, and are reproduced with attribution for the purpose of answering it. The screenshots are of [newsroom.sgit.ai](https://newsroom.sgit.ai/) at v0.8.0, taken on 11 October 2026; the counts in them, 74 articles, 349 links, 160 nodes and 427 edges, 21 op-eds, are the site's own. The token figures are from [The agent is the reader](the-agent-is-the-reader.md); the synthetic readers' numbers from [How to run synthetic users](how-to-run-synthetic-users.md); the 662 catalogued items from [One article, five readers](one-article-five-readers.md). The map figure was drawn for this article from the newsroom's page of what runs. Related: [The future of news is the story vault, not the paywall](future-of-news-story-vault-not-paywall.md), [The same argument, in our words](the-same-argument-in-our-words.md), [Story vault underneath, Reader Skills on top](story-vault-meets-reader-skills.md), [Brief the agent too](brief-the-agent-too.md), [From me to you, in a link](a-reading-list-in-a-link.md) and [I miss it, so it is working](i-miss-it.md).

## Threads

News & evidenceGraphs & knowledgeAgents & policy[This article as a graph →](graphs.md#the-article-remains-a-product)

### Builds on

- [The future of news is the story vault, not the paywall](future-of-news-story-vault-not-paywall.md) A story is a graph of claims and evidence and the article is one projection of it; keep the graph in a vault and sell what the article was made from.
- [The same argument, in our words: Satya Nadella on models as insider risks, translated into the language of RiskMandate](the-same-argument-in-our-words.md) Satya Nadella's case for treating models as insider risks, translated idea by idea into our vocabulary: reach, mandate, gap, barriers and accepted risk.
- [How to run synthetic users on your own site: five people who do not exist, a browser, and an afternoon](how-to-run-synthetic-users.md) Five invented users, a model reading screenshots, and a real browser: how to run synthetic users, from three studies.
- [The agent is the reader: why agents will pay for graphs, personas and signed claims, because it is cheaper than not paying](the-agent-is-the-reader.md) Agents pay to read the raw web and guess its meaning. A curated graph answers for 90% fewer tokens, so paying the publisher is cheaper than not paying.
- [The reader was always the product: a corrected history of how news got into this mess](how-news-got-here.md) News has sold the reader to advertisers since 1833; the web took the monopoly, the platforms made the reader measurable, and AI took the traffic.
- [One article, five readers: a librarian, a cartographer, a historian, an explainer and a storyteller read the same piece](one-article-five-readers.md) Write the article first, then send five agent readers through it: a catalogue, an ontology and maps, the arc, two minutes, and a deck.
- [Where the vault keys live: key management at sgit-ai v0.20.0, and what comes next](where-the-vault-keys-live.md) Vault key management at sgit-ai v0.20.0: the one secret, where keys are kept, how they travel sealed on append lanes, and what comes next.
- [From me to you, in a link: a personal reading list, two briefs to build and use it, and the loop that makes it a day's work](a-reading-list-in-a-link.md) A reading list from one person to another, in a link the server never sees; a brief to build it, a brief to use it, and the loop that ships it in a day.
- [Brief the agent too: the people I talk to work with agents, so what I send has to reach both](brief-the-agent-too.md) The people I advise read through agents. Content needs a second package, a brief for their agent, and memory, so it reads what changed, not everything.
- [I miss it, so it is working: the people who decide the roadmap have to use the product, and the vault the newsroom now needs](i-miss-it.md) I read the newsroom on four devices and they do not agree. Missing a feature is the best sign; the makers must use it. And the brief for the reader's vault.
- [Pay to keep your persona: readers should pay because it helps them, not because they feel they should](pay-to-keep-your-persona.md) Readers should pay because it helps them: a persona with a name and a graph, several for focus, and one that follows you between devices.
- [No server, by design: first I retired the database, now I am retiring the back end](no-server-by-design.md) First the database went, now the back end: the SGit Newsroom runs all its logic in the browser, on commodity servers that cannot read your data.
- [Story vault underneath, Reader Skills on top: why local journalism has the most to gain](story-vault-meets-reader-skills.md) Markus Franz's Reader Skills on top, the story vault underneath: each skill is a graph query, and local stories can pay back down their chain of sources.

### Continued by

- [Agentic cost is an engineering problem: a business plan for a service that reads the logs a company already has and finds the money, then the engineering](agentic-cost-is-an-engineering-problem.md) A business plan: read the logs a company already has, draw each agent's footprint, twin and policy, and find the money first and the engineering second.
- [Firing journalists is the worst thing a publication can do: what a hiring decision says about where a publisher is going, and who to hire instead](firing-journalists.md) A hiring decision is a direction of travel: fire the journalists and the centre of gravity moves to packaging, where the metric makes clickbait by construction.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 79 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=79)

**Posting this article on LinkedIn?** The cover is [the-article-remains-a-product.jpg](banners/the-article-remains-a-product.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-article-remains-a-product.html)*
