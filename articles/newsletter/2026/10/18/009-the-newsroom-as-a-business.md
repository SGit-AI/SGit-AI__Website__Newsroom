# Issue 9: The newsroom as a business: who to hire, what a newsroom sells when the article is not the only product, and the bills and keys underneath, SGit Newsroom

> What is a newsroom for when agents can write, and who pays for it? Eight articles from 7 to 12 October answer from the business end. A hiring plan is the clearest statement of a publisher's direction, and firing journalists to hire for traffic moves the centre of gravity to packaging, because the metric is a hiring plan in disguise. The article remains a product, checked line by line against Jonathan Palmer's four outputs, with provenance published rather than kept. Liquid content needs water, which is the journalist's notebook, and local journalism has the most to gain when every use pays back down the chain of claims. Then the machinery: going slow to go fast as the newsroom became a villager project, a wire written by one agent into a vault and drawn by another, a business plan for reading the logs that explain an agent bill, and VoiceDebrief, a product with no server whose commercial model is a property of the key and was stopped by a provider's terms.

*Source: <https://newsroom.sgit.ai/articles/newsletter/2026/10/18/009-the-newsroom-as-a-business.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../../../index.md) / [SGit Newsroom](../../../../index.md) / [Newsletter](../../../index.md) / Issue 9

SGit Newsroom · Issue 9 · 2026-10-18

# The newsroom as a business: who to hire, what a newsroom sells when the article is not the only product, and the bills and keys underneath

By [Dinis Cruz](https://sgit.ai/about/index.md), written with the [Journalist](../../../../../newsroom/roles/journalist.md)

***Abstract:** What is a newsroom for when agents can write, and who pays for it? Eight articles from 7 to 12 October answer from the business end. A hiring plan is the clearest statement of a publisher's direction, and firing journalists to hire for traffic moves the centre of gravity to packaging, because the metric is a hiring plan in disguise. The article remains a product, checked line by line against Jonathan Palmer's four outputs, with provenance published rather than kept. Liquid content needs water, which is the journalist's notebook, and local journalism has the most to gain when every use pays back down the chain of claims. Then the machinery: going slow to go fast as the newsroom became a villager project, a wire written by one agent into a vault and drawn by another, a business plan for reading the logs that explain an agent bill, and VoiceDebrief, a product with no server whose commercial model is a property of the key and was stopped by a provider's terms.*

What is a newsroom for when agents can write, and who pays for it? The last three issues were about the reader's vault, who answers for an agent, and sovereignty. This one is about the business: who a publisher should hire, what it should sell when the article is not its only product, and the engineering, the bills and the keys underneath. Eight articles from 7 to 12 October, two of them from 7 October, the day of the first issue, and not covered until now. It follows [issue 8, sovereignty is the ability to move](https://newsroom.sgit.ai/articles/newsletter/2026/10/18/008-sovereignty-is-the-ability-to-move.html).

The newsroom as a business, in six pictures, one from each of six of the articles

## Who to hire

[Firing journalists is the worst thing a publication can do](https://newsroom.sgit.ai/articles/firing-journalists.html) starts from Press Gazette's tracker, at least 3,434 journalism job cuts in the UK and US in 2025, and is about what those decisions say rather than what they cost. A hiring plan is the clearest statement a publisher makes about where its centre of gravity is going. Fire the people who make original content and hire for traffic, and the centre moves to packaging; packaging is measured by engagement, and engagement optimised for is clickbait whether anyone meant it or not. The opposite cut is as bad: journalists with no engineers have content nothing enables. The line I would put to a board:

>

The metric is a hiring plan in disguise.

## What a newsroom sells

[The article remains a product](https://newsroom.sgit.ai/articles/the-article-remains-a-product.html) answers Jonathan Palmer, who asked on LinkedIn what a news business would look like with no human readers tomorrow, and listed four outputs besides the article: structured intelligence, continuous intelligence, provenance and verification, and embedded distribution. Each is checked against the newsroom as it ran, what runs and what is only designed: a graph beside every article, versions read from git, 21 World News Day op-eds frozen and hashed in a vault with its read key printed, and a markdown twin and an llms.txt for agents. Where we differ is the word proprietary:

>

Provenance that only the publisher can check is not provenance.

[Liquid content needs water](https://newsroom.sgit.ai/articles/liquid-content-needs-water.html), from 7 October, answers FT Strategies' primer on liquid content. I agree with most of it, and push in one place: what makes content liquid is the reporting, the notebook, the calls and the documents kept with their sources as a graph, and the experienced journalist at the centre with tools they have not had, not a reinvention of newsroom norms:

>

If content is to be liquid, it needs water in it, and the water is not the format.

[Story vault underneath, Reader Skills on top](https://newsroom.sgit.ai/articles/story-vault-meets-reader-skills.html) draws the connection Markus Franz saw between his six Reader Skills and the story vault: each skill is an operation the story graph already supports, Update is a diff rather than a summary, and a correction is an edge. His article added locality, where trust and brand are strongest. Facts travel up from a local contributor to a national story, and every use can pay back down the same edges, which only works if the claim knows where it came from:

>

A page that cannot name its source cannot pay it.

## The machinery underneath

[Go slow to go fast](https://newsroom.sgit.ai/articles/explorer-to-villager-newsroom.html) is the moment the newsroom stopped being an explorer project. It was live and taking money, and the application that bills and personalises sat in the same repository as the articles: about 2,700 lines of reader code, 433 lines of tests the one workflow never ran, two diverging copies of the meter. The brief is six phases, a pure refactoring first, with the same behaviour and the same bugs proved by hashing what the live site serves, and features waiting until the fifth:

>

Going slow now is what lets me keep going fast without the fear that each new feature breaks something a reader has paid for.

Six phases, from mapping to the explorer's return; until phase five no behaviour changes, not a feature and not a fix.

[Two agents, one vault](https://newsroom.sgit.ai/articles/two-agents-one-vault.html) is the Industry Wire: forty stories written into an encrypted vault by one agent, in a session the newsroom never saw, and drawn in the reader's browser by the newsroom, which holds only the read key. A commit to the vault is on the page within two minutes, with no release of the site, and every story carries "ai-generated, unreviewed" because the vault says so. The vault is the interface between two agents that never share a session:

>

Neither can do the other's job, because neither has the other's key.

## Bills and keys

[Agentic cost is an engineering problem](https://newsroom.sgit.ai/articles/agentic-cost-is-an-engineering-problem.html) is a business plan for somebody to build: a service that installs nothing, reads the invoices, logs and prompts a company already has, draws every agent's footprint, writes the behaviour policy each agent was in fact running under, and returns two lists, what to stop paying for and what to build. No customer has been read yet. The gaps count too:

>

Not being able to do the analysis is the first result of the analysis, and it is the one most companies need first.

[The key is the billing system](https://newsroom.sgit.ai/articles/the-key-is-the-billing-system.html) is the state of VoiceDebrief, a product I am involved in: a voice note to a transcript, a translation and a debrief in one pass, in the browser, on the user's own key, with no server and nothing stored. The commercial model was a capped key handed to a user who paid, with the provider metering it. OpenRouter's docs describe exactly that mechanism, and its terms forbid using it to resell access, the same shape as the licence that stopped a Mac being leased for less than a day:

>

The product was possible; the licence was the blocker.

What each provider's terms and docs said in October 2026 about a capped key in a user's hand, and the four routes left.

## The eight articles

### Who to hire, and what to sell

The centre of gravity, the four outputs, and where the water comes from.

- [**Firing journalists is the worst thing a publication can do: what a hiring decision says about where a publisher is going, and who to hire instead**](../../../../firing-journalists.md). A hiring decision is a direction of travel: fire the journalists and the centre of gravity moves to packaging, where the metric makes clickbait by construction.
- [**The article remains a product: Jonathan Palmer's four outputs for a newsroom with no human readers, checked against one that runs**](../../../../the-article-remains-a-product.md). Jonathan Palmer's four outputs for a newsroom with no human readers, quoted line by line and checked against newsroom.sgit.ai as it runs, screenshots included.
- [**Liquid content needs water: liquefy the journalist's notebook, not the finished product**](../../../../liquid-content-needs-water.md). A reply to FT Strategies on liquid content: the water is the reporting, so liquefy the journalist's notebook, keep the writing theirs, and pay per use.
- [**Story vault underneath, Reader Skills on top: why local journalism has the most to gain**](../../../../story-vault-meets-reader-skills.md). Markus Franz's Reader Skills on top, the story vault underneath: each skill is a graph query, and local stories can pay back down their chain of sources.

### The machinery

Going slow to go fast, and a wire one agent writes and another draws.

- [**Go slow to go fast: moving the newsroom from an explorer project to a villager one, with the brief to do it**](../../../../explorer-to-villager-newsroom.md). The newsroom is live and charging. Move the reader code to its own repo, same bytes and same bugs, then map, test, review and refactor before new features.
- [**Two agents, one vault: the Industry Wire is written into an encrypted vault by one agent and drawn by newsroom.sgit.ai, which holds only the read key**](../../../../two-agents-one-vault.md). One agent writes the Industry Wire into an encrypted vault; newsroom.sgit.ai holds only the read key and draws it, so a commit reaches the page with no release.

### Bills and keys

Reading the logs that explain an agent bill, and a product whose key is its billing system.

- [**Agentic cost is an engineering problem: a business plan for a service that reads the logs a company already has and finds the money, then the engineering**](../../../../agentic-cost-is-an-engineering-problem.md). A business plan: read the logs a company already has, draw each agent's footprint, twin and policy, and find the money first and the engineering second.
- [**The key is the billing system: VoiceDebrief, a product with no server, the one thing it cannot sell, and who could let it**](../../../../the-key-is-the-billing-system.md). VoiceDebrief runs with no server on the user's own key; the one thing it cannot sell is a capped key, and this maps who could allow it and what to ask them.

*This is issue 9 of the SGit Newsroom newsletter, also published on LinkedIn in [Deterministic GenAI](https://www.linkedin.com/newsletters/deterministic-genai-7174563523795005440/). Every article it links to is on [newsroom.sgit.ai](https://newsroom.sgit.ai/articles/index.html), with its sources and its data. To get the next issue by email, [subscribe at newsroom.sgit.ai/subscribe](https://newsroom.sgit.ai/subscribe/).*

**Posting this issue on LinkedIn?** The cover is [009-the-newsroom-as-a-business.jpg](../../../../banners/009-the-newsroom-as-a-business.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page. Its images copy with it.

[← All issues](../../../index.md)


---

*[Site index for agents](../../../../../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/newsletter/2026/10/18/009-the-newsroom-as-a-business.html)*
