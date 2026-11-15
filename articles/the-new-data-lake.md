# The new data lake: many small append-only lanes instead of one big lake, a curator agent that turns their rows into a semantic graph, and a graph that draws its own infographics, as we ran it at Web Summit, sgit.ai

> The data lake promised one place for all of a company's data, and often delivered a swamp: a lot of data, little meaning, and nobody sure where a number came from. With agents, I think the next generation looks different. Instead of one big lake, many small lanes: each source appends signed rows and never edits the past. A curator agent reads the lanes and turns rows into a semantic graph of things and links, every one pointing back at the rows it came from. And the graph draws its own pictures: the charts, maps, flows and infographics that people actually read. This is data intelligence that you can audit, and it is how we ran PrompTugal.news and the Storm Charles site in November: a researcher capturing public pages four times a day, a curator mapping them into story candidates, a graph of 877 entities, and observability appended to lanes in a vault. A working demo shows the pattern with made-up data.

*Source: <https://newsroom.sgit.ai/articles/the-new-data-lake.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The new data lake: many small append-only lanes instead of one big lake, a curator agent that turns their rows into a semantic graph, and a graph that draws its own infographics, as we ran it at Web Summit

# The new data lake: many small append-only lanes instead of one big lake, a curator agent that turns their rows into a semantic graph, and a graph that draws its own infographics, as we ran it at Web Summit

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-15 · [article v1.0.0](versions/the-new-data-lake.md) · [newsroom v0.14.94](https://newsroom.sgit.ai/admin/versions.html) · data-intelligencedata-lakeknowledge-graphagentsappend-onlyinfographicsdemoarticle

***Abstract:** The data lake promised one place for all of a company's data, and often delivered a swamp: a lot of data, little meaning, and nobody sure where a number came from. With agents, I think the next generation looks different. Instead of one big lake, many small lanes: each source appends signed rows and never edits the past. A curator agent reads the lanes and turns rows into a semantic graph of things and links, every one pointing back at the rows it came from. And the graph draws its own pictures: the charts, maps, flows and infographics that people actually read. This is data intelligence that you can audit, and it is how we ran PrompTugal.news and the Storm Charles site in November: a researcher capturing public pages four times a day, a curator mapping them into story candidates, a graph of 877 entities, and observability appended to lanes in a vault. A working demo shows the pattern with made-up data.*

The new data lake: lanes, a curator, a graph, pictures and insight, and what we ran in November in those terms.

## In short

- **The old promise:** one lake for all the data; too often, a swamp nobody trusts.
- **The new shape:** many small append-only lanes, each source signing its rows and never editing the past.
- **A curator agent** turns rows into a semantic graph, every node and link pointing back at its rows.
- **The graph draws its own pictures:** charts, maps, flows and infographics, rebuilt at every release.
- **We ran it in November,** for a newsroom and a storm site.
- **Try it:** [a working demo in a public vault](https://dev.vault.sgraph.ai/#sgit_public_read_334fba5a86c2fa966d833a5d7c01b9d457e7a66b12b2799e4f8b137559507ff9%3Acib1n1ha), with made-up data.

## The swamp problem

My friend in crypto told me how his company started: to do good analysis, they bought the data. Then they found it was too expensive, and built their own infrastructure. That is a common path, and it often ends in the same place as the classic data lake: a great deal of data, and very little meaning.

The problem is not storage. It is that nobody can say, for a given number, where it came from, when, and who changed it. An agent makes this worse if it reads a swamp, and better if it helps build something you can audit.

## Lanes, not a lake

The first change is to stop pouring everything into one place. Each source gets its own lane: the news a researcher agent captured, the prices a pricing agent read, the orders, the support tickets. A lane is append-only: a source adds rows and never edits or deletes the past. Each row is signed, so you know which agent wrote it.

We use this pattern everywhere. Every agent on the Web Summit team had its own lane; PrompTugal.news appended reader counts and agent runs to lanes in an encrypted vault, read in the browser with a published key. Its own page is honest about the weakness, and I like that: the lanes' tokens are public, so rows can be forged or flooded, and only a signed agent run names a key. A lane is a claim, not a fact, until something checks it.

## A curator that makes a graph

The second change is who makes sense of the rows. A curator agent reads the lanes and turns rows into a semantic graph: the things that matter to this company, such as a customer, a route, a product or a competitor, and the links between them. Every node and link points back at the rows it came from, so any claim in the graph can be checked.

At PrompTugal.news, a researcher captured public pages into its vault four times a day, and a curator mapped them: 104 captures, grouped by beat, into 64 story candidates, from which journalists wrote 73 articles. The newsroom's graph held 877 entities and 1,026 edges by 15 November, drawn again at every release ([PrompTugal.news, the newsroom we ran](promptugal-news-the-newsroom-we-ran.md)).

The demo's second tab: four lanes, a curator, a graph, the chart it drew, and insights pointing at their rows.

## A graph that draws its own pictures

The third change is the last mile. People do not read graphs; they read pictures. So the graph draws them: a chart of what was mentioned this week, a map of where the late deliveries are, a flow of how a story moved, an infographic for the board. They are rebuilt from the graph at every release, so they are never older than the data.

That is how [the Storm Charles site](storm-charles-a-newsroom-built-in-a-night.md) grew to 2,618 pages in three days, each with its source and the time it was read, and how every figure in this newsroom is made: from data, by code, and checked.

## Insight, with its evidence

An insight is a claim with its evidence: late deliveries cluster on one route, and the road news names the same route; a customer's orders fell after a competitor's cheaper list. Because every link in the graph points at its rows, the insight can show its working, and a person can decide whether to act on it.

This is where the data lake and the company brain meet. The lanes and the graph are the brain's memory; the insights are what it says when you ask ([a brain you arrive at](a-brain-you-arrive-at.md)).

## Try the demo

[The demo's second tab](https://dev.vault.sgraph.ai/#sgit_public_read_334fba5a86c2fa966d833a5d7c01b9d457e7a66b12b2799e4f8b137559507ff9%3Acib1n1ha) has four made-up lanes, news, prices, orders and support. Click a lane to see its rows, watch the curator turn them into a graph, and read the chart and the insights it drew, each tagged with the lanes it came from.

## What this does not claim

- **The demo's lanes, rows and numbers are made up.**
- **The PrompTugal.news and Storm Charles figures are ours,** from their repositories in November 2026.
- **A signed row proves who wrote it, not that it is true;** that is what the curator and the reviewers are for.

## Where this comes from

A conversation with a friend in crypto, 15 November 2026; the PrompTugal.news repository and its live newsroom and observability pages, read 15 November 2026; the Storm Charles repository. Earlier on this site: [PrompTugal.news, the newsroom we ran](promptugal-news-the-newsroom-we-ran.md), [Storm Charles, a newsroom built in a night](storm-charles-a-newsroom-built-in-a-night.md), [the team's operating system](the-teams-operating-system.md), and the two companion articles, [a brain you arrive at](a-brain-you-arrive-at.md) and [a market for sweets](a-market-for-sweets.md).

## Threads

Graphs & knowledgeVaults & method[This article as a graph →](graphs.md#the-new-data-lake)

### Builds on

- [PrompTugal.news, the newsroom we ran at Web Summit: desks of agents that captured, mapped, wrote and reviewed 73 signed articles in ten days, an accountant that counted every run, and fifty outreach drafts that no agent was allowed to send](promptugal-news-the-newsroom-we-ran.md) PrompTugal.news: 73 signed articles in ten days from desks of agents, a reviewer for every draft, and fifty outreach drafts no agent could send.
- [Storm Charles, a newsroom built in a night: one person, about thirty agents and a weather face over a data room, where every figure carries its source, the time it was read, and whether it is a fact, evidence or our hypothesis](storm-charles-a-newsroom-built-in-a-night.md) Storm Charles: about thirty agents built a weather face over a data room in a night, every figure sourced, timed and labelled.
- [A brain you arrive at: a company brain for information, decisions and insights is built for one company, one division and one team, starting with one person's and growing, and the Web Summit team already ran one](a-brain-you-arrive-at.md) A company brain is made for one company, division and team, and you arrive at it: start with a person's, then a team's. We already ran one.
- [The team's operating system: web-summit.sgit.ai, the one site where six people and their agents ran Web Summit, with a brief and a command centre for each person, a key and an inbox for each agent, the board as files, and the outside world on a map](the-teams-operating-system.md) web-summit.sgit.ai: one site where six people and their agents ran Web Summit, in four layers built on git.
- [A market for sweets: the opposite of a market for lemons, a semantic graph for one financial decision that gives the buyer the evidence, an agent that gathers and weighs but never trades, and the judo move of leaving the trade to others](a-market-for-sweets.md) The opposite of a market for lemons: a semantic graph for one financial decision, an agent that gathers but never trades, and the person decides.

### Continued by

- [A market for sweets: the opposite of a market for lemons, a semantic graph for one financial decision that gives the buyer the evidence, an agent that gathers and weighs but never trades, and the judo move of leaving the trade to others](a-market-for-sweets.md) The opposite of a market for lemons: a semantic graph for one financial decision, an agent that gathers but never trades, and the person decides.
- [A brain you arrive at: a company brain for information, decisions and insights is built for one company, one division and one team, starting with one person's and growing, and the Web Summit team already ran one](a-brain-you-arrive-at.md) A company brain is made for one company, division and team, and you arrive at it: start with a person's, then a team's. We already ran one.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 405 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=405)

**Posting this article on LinkedIn?** The cover is [the-new-data-lake.jpg](banners/the-new-data-lake.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-new-data-lake.html)*
