---
title: Newsrooms on open data: turning the public data feeds behind PrompTugal.news and the Storm Charles site into one data site, a vault per source with an API and its provenance, then building small, focused newsrooms on top, for farmers, investors, the sea, fire, tourism and AI, each run by an agentic team, each a possible company, and why this is exactly where journalism comes in
date: 2026-11-17
author: Dinis Cruz
author_url: about/index.html
summary: When I show people PrompTugal.news, the thing they like most is not the stories. It is the live data: the weather warnings, the fire risk, the flights over Faro, each value with where it came from and when it was read. The Storm Charles site went further, with 34 public datasets in a catalogue, each with its hash, every line labelled fact, evidence or hypothesis. That data is valuable, and today it is spread across sites and repositories. So the next step is to consolidate it: one data site, with a vault per public source, a collector written as code, an API described in OpenAPI, the provenance of every value, and a record of how much of each dataset is code and how much is agents, and what it costs in tokens. Then the interesting part: small, focused newsrooms on top of it, each about one subject, each run by an agentic team, each a possible small company. Agriculture, with weather, fire risk and water. Investors. The sea. Fire and civil protection. Tourism and travel. AI. Research like this is thin today, because journalism has lost the money to do it. I think this is exactly where journalism comes back in.
version: v0.14.143
license: https://creativecommons.org/licenses/by/4.0/
tags: data, open-data, promptugal, newsrooms, journalism, agenticcells, startups, portugal, article
status: published
---

!shot vrt-stack.webp | images/ | Public sources, a vault and an API per source, then focused newsrooms on top, each run by an agentic team. | architecture

## In short {#in-short}

- **The live data is what people like most** when I show PrompTugal.news.
- **Consolidate it:** one data site, a vault per public source, an API, the provenance of every value.
- **Record how much is code and how much is agents,** and what each dataset costs in tokens.
- **Then focused newsrooms on top:** agriculture, investors, the sea, fire, tourism, AI.
- **Each run by an agentic team,** each a possible small company.
- **This is where journalism comes in:** turning public data into information people use.

## What we already have {#have}

More than I realised, when I asked for an inventory today:

- **Live data for 18 places in the Algarve,** collected every hour by code, with no model in the loop: IPMA's warnings, station observations, five-day forecasts, fire risk per municipality, UV and the sea forecast, and flights around Faro airport from an open feed. Every value carries when it was read, the source it came from, and the page a person would open to check it.
- **A data room for the storm:** 34 datasets in a catalogue, each with its size and hash, warnings, forecasts and stations, alert messages, and the decisions of the airport, bridges, metro, ferries, schools and hospitals, every line labelled fact, evidence or hypothesis ([Storm Charles, a newsroom built in a night](/articles/storm-charles-a-newsroom-built-in-a-night.html)).
- **A place file for every town,** kept by its own agent, every source with its link and date, every file signed ([PrompTugal.news by place](/articles/promptugal-news-by-place.html)).
- **APIs:** an OpenAPI 3.1 description, generated with the site, for PrompTugal.news and for each place, with Swagger pages to try them.
- **Our own observability:** each page records a view and a read, encrypted in the browser and written to a private vault.

## One data site {#data}

!shot vrt-source.webp | images/ | One public source, done properly: collector as code, a vault, an API, provenance, and who and what made it. | process

Today this is spread across the PrompTugal.news repository, the storm site and others. The next step is a data site of its own, with a repository behind it, built per public source. For each one:

1. **A collector, written as code,** polite to the source, with its schedule.
2. **A vault** for the dataset, encrypted and versioned, public where the source is public ([how a vault works](/articles/how-a-vault-works.html)).
3. **An API,** described in OpenAPI, with a Swagger page.
4. **The provenance of every value:** source, page, when it was read, by what.
5. **A card** saying who keeps it, how often it changes, and what it costs.

Only public sources, always. And the data site is the layer the newsrooms consume: PrompTugal.news, its town pages, and the focused newsrooms below.

## Code, agents and tokens {#tokens}

This connects to the provenance work ([who wrote it, who steered it, who signs it](/articles/who-steered-this.html)). For every dataset and every page made from it, I want to see how much is code, how much is agents, and how much is checked by a person; and how many tokens it spends.

That matters commercially. The collectors already run with no model at all. If most of the analysis is code that runs, with an agent only where judgement is needed, the cost per update is close to nothing. The storm site's own accounts show where tokens actually go: about 2,069 million session tokens, 98.7% of them re-reading, while its third-party model calls cost about a dollar by 03:00. Our rule is to write code for what repeats and use a model only where judgement is needed ([spend fewer tokens](/articles/spend-fewer-tokens.html)). A data newsroom built that way is cheap to run.

## Focused newsrooms {#verticals}

!shot vrt-verticals.webp | images/ | Six focused newsrooms on the same data: who reads them, what they join, what they could sell. | table

Once the data is in one place, with the news from PrompTugal.news beside it, we can build small newsrooms that each care about one thing. Sub-brands, each on its own address, each run by an agentic team ([the cell is the unit](/articles/the-cell-is-the-unit.html)):

- **Agriculture:** weather, fire risk, UV, rainfall and drought, joined to the news of each municipality. For farmers, co-operatives and insurers: what this week means for this valley.
- **Investors:** companies, funding and public records, from the Web Summit work onwards, with exchange rates and regional news. For investors and founders: who is building what, here.
- **The sea:** sea forecasts, ports and weather, for fishing, sailing and the ports.
- **Fire and civil protection:** fire risk per municipality, warnings and what was decided, the storm site made permanent, for councils, schools and residents.
- **Tourism and travel:** flights, weather, the sea, events and transport, for hotels, guides and visitors.
- **AI:** agents rated against standards, from GAMMA-Ray, and the news of the field, for the people deciding what to adopt ([agents rating agents](/articles/agents-rating-agents.html)).

Each one reads the same data site, adds the sources its subject needs, and publishes with the same provenance. And each is a possible small company: a few people, an agentic team, one subject, and readers who pay by the read, or businesses that pay for alerts and briefings ([paid by the read](/articles/paid-by-the-read.html)).

## Why this is journalism {#journalism}

The information these readers need mostly exists, in public, as raw data, and almost nobody turns it into something they can use. A farmer does not read IPMA's fire-risk JSON; a hotel does not join flights to the sea forecast. Doing that work, finding what matters, checking it, saying where it came from, used to be journalism's job, and the money for it has gone. I think agentic teams, with code doing the repeating work and people steering, make it affordable again. That is where journalism comes back in.

## What happens next {#next}

I have briefed PrompTugal.news's conductor agent to start the consolidation: a separate repository and site for the data, a vault per public source, APIs, and the provenance and cost records. And to check that our observability is still collecting visits on every site, because I want a daily debrief of who reads what. The focused newsrooms come after the data site exists.

## What this does not claim {#limits}

- **The data site and the focused newsrooms are plans,** not built yet.
- **The token figures are the storm site's own,** from its accounts.
- **Each source's terms decide what can be republished;** public is not always free to reuse.

## Where this comes from {#sources}

My own thinking, 17 November 2026, and an inventory of the PrompTugal.news repository the same day: its live collector, place files, OpenAPI generator, observability and the accountant's reports; the storm site as described in its brief and in [Storm Charles, a newsroom built in a night](/articles/storm-charles-a-newsroom-built-in-a-night.html). The public sources: [IPMA open data](https://api.ipma.pt/) and an open flight feed. Earlier on this site: [PrompTugal.news by place](/articles/promptugal-news-by-place.html), [how a vault works](/articles/how-a-vault-works.html), [who wrote it, who steered it, who signs it](/articles/who-steered-this.html), [spend fewer tokens](/articles/spend-fewer-tokens.html), [the cell is the unit](/articles/the-cell-is-the-unit.html), [agents rating agents](/articles/agents-rating-agents.html), [paid by the read](/articles/paid-by-the-read.html).
