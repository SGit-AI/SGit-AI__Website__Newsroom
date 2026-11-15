---
title: The new data lake: many small append-only lanes instead of one big lake, a curator agent that turns their rows into a semantic graph, and a graph that draws its own infographics, as we ran it at Web Summit
date: 2026-11-15
author: Dinis Cruz
author_url: about/index.html
summary: The data lake promised one place for all of a company's data, and often delivered a swamp: a lot of data, little meaning, and nobody sure where a number came from. With agents, I think the next generation looks different. Instead of one big lake, many small lanes: each source appends signed rows and never edits the past. A curator agent reads the lanes and turns rows into a semantic graph of things and links, every one pointing back at the rows it came from. And the graph draws its own pictures: the charts, maps, flows and infographics that people actually read. This is data intelligence that you can audit, and it is how we ran PrompTugal.news and the Storm Charles site in November: a researcher capturing public pages four times a day, a curator mapping them into story candidates, a graph of 877 entities, and observability appended to lanes in a vault. A working demo shows the pattern with made-up data.
version: v0.14.94
license: https://creativecommons.org/licenses/by/4.0/
tags: data-intelligence, data-lake, knowledge-graph, agents, append-only, infographics, demo, article
status: published
---

!shot ndl-flow.webp | images/ | The new data lake: lanes, a curator, a graph, pictures and insight, and what we ran in November in those terms. | flow

## In short {#in-short}

- **The old promise:** one lake for all the data; too often, a swamp nobody trusts.
- **The new shape:** many small append-only lanes, each source signing its rows and never editing the past.
- **A curator agent** turns rows into a semantic graph, every node and link pointing back at its rows.
- **The graph draws its own pictures:** charts, maps, flows and infographics, rebuilt at every release.
- **We ran it in November,** for a newsroom and a storm site.
- **Try it:** [a working demo in a public vault](https://dev.vault.sgraph.ai/#sgit_public_read_334fba5a86c2fa966d833a5d7c01b9d457e7a66b12b2799e4f8b137559507ff9%3Acib1n1ha), with made-up data.

## The swamp problem {#swamp}

My friend in crypto told me how his company started: to do good analysis, they bought the data. Then they found it was too expensive, and built their own infrastructure. That is a common path, and it often ends in the same place as the classic data lake: a great deal of data, and very little meaning.

The problem is not storage. It is that nobody can say, for a given number, where it came from, when, and who changed it. An agent makes this worse if it reads a swamp, and better if it helps build something you can audit.

## Lanes, not a lake {#lanes}

The first change is to stop pouring everything into one place. Each source gets its own lane: the news a researcher agent captured, the prices a pricing agent read, the orders, the support tickets. A lane is append-only: a source adds rows and never edits or deletes the past. Each row is signed, so you know which agent wrote it.

We use this pattern everywhere. Every agent on the Web Summit team had its own lane; PrompTugal.news appended reader counts and agent runs to lanes in an encrypted vault, read in the browser with a published key. Its own page is honest about the weakness, and I like that: the lanes' tokens are public, so rows can be forged or flooded, and only a signed agent run names a key. A lane is a claim, not a fact, until something checks it.

## A curator that makes a graph {#curator}

The second change is who makes sense of the rows. A curator agent reads the lanes and turns rows into a semantic graph: the things that matter to this company, such as a customer, a route, a product or a competitor, and the links between them. Every node and link points back at the rows it came from, so any claim in the graph can be checked.

At PrompTugal.news, a researcher captured public pages into its vault four times a day, and a curator mapped them: 104 captures, grouped by beat, into 64 story candidates, from which journalists wrote 73 articles. The newsroom's graph held 877 entities and 1,026 edges by 15 November, drawn again at every release ([PrompTugal.news, the newsroom we ran](/articles/promptugal-news-the-newsroom-we-ran.html)).

!shot dmo-lake.webp | images/ | The demo's second tab: four lanes, a curator, a graph, the chart it drew, and insights pointing at their rows. | screenshot

## A graph that draws its own pictures {#pictures}

The third change is the last mile. People do not read graphs; they read pictures. So the graph draws them: a chart of what was mentioned this week, a map of where the late deliveries are, a flow of how a story moved, an infographic for the board. They are rebuilt from the graph at every release, so they are never older than the data.

That is how [the Storm Charles site](/articles/storm-charles-a-newsroom-built-in-a-night.html) grew to 2,618 pages in three days, each with its source and the time it was read, and how every figure in this newsroom is made: from data, by code, and checked.

## Insight, with its evidence {#insight}

An insight is a claim with its evidence: late deliveries cluster on one route, and the road news names the same route; a customer's orders fell after a competitor's cheaper list. Because every link in the graph points at its rows, the insight can show its working, and a person can decide whether to act on it.

This is where the data lake and the company brain meet. The lanes and the graph are the brain's memory; the insights are what it says when you ask ([a brain you arrive at](/articles/a-brain-you-arrive-at.html)).

## Try the demo {#demo}

[The demo's second tab](https://dev.vault.sgraph.ai/#sgit_public_read_334fba5a86c2fa966d833a5d7c01b9d457e7a66b12b2799e4f8b137559507ff9%3Acib1n1ha) has four made-up lanes, news, prices, orders and support. Click a lane to see its rows, watch the curator turn them into a graph, and read the chart and the insights it drew, each tagged with the lanes it came from.

## What this does not claim {#limits}

- **The demo's lanes, rows and numbers are made up.**
- **The PrompTugal.news and Storm Charles figures are ours,** from their repositories in November 2026.
- **A signed row proves who wrote it, not that it is true;** that is what the curator and the reviewers are for.

## Where this comes from {#sources}

A conversation with a friend in crypto, 15 November 2026; the PrompTugal.news repository and its live newsroom and observability pages, read 15 November 2026; the Storm Charles repository. Earlier on this site: [PrompTugal.news, the newsroom we ran](/articles/promptugal-news-the-newsroom-we-ran.html), [Storm Charles, a newsroom built in a night](/articles/storm-charles-a-newsroom-built-in-a-night.html), [the team's operating system](/articles/the-teams-operating-system.html), and the two companion articles, [a brain you arrive at](/articles/a-brain-you-arrive-at.html) and [a market for sweets](/articles/a-market-for-sweets.html).
