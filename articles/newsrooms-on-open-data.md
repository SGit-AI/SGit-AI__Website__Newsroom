# Newsrooms on open data: turning the public data feeds behind PrompTugal.news and the Storm Charles site into one data site, a vault per source with an API and its provenance, then building small, focused newsrooms on top, for farmers, investors, the sea, fire, tourism and AI, each run by an agentic team, each a possible company, and why this is exactly where journalism comes in, sgit.ai

> When I show people PrompTugal.news, the thing they like most is not the stories. It is the live data: the weather warnings, the fire risk, the flights over Faro, each value with where it came from and when it was read. The Storm Charles site went further, with 34 public datasets in a catalogue, each with its hash, every line labelled fact, evidence or hypothesis. That data is valuable, and today it is spread across sites and repositories. So the next step is to consolidate it: one data site, with a vault per public source, a collector written as code, an API described in OpenAPI, the provenance of every value, and a record of how much of each dataset is code and how much is agents, and what it costs in tokens. Then the interesting part: small, focused newsrooms on top of it, each about one subject, each run by an agentic team, each a possible small company. Agriculture, with weather, fire risk and water. Investors. The sea. Fire and civil protection. Tourism and travel. AI. Research like this is thin today, because journalism has lost the money to do it. I think this is exactly where journalism comes back in.

*Source: <https://newsroom.sgit.ai/articles/newsrooms-on-open-data.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Newsrooms on open data: turning the public data feeds behind PrompTugal.news and the Storm Charles site into one data site, a vault per source with an API and its provenance, then building small, focused newsrooms on top, for farmers, investors, the sea, fire, tourism and AI, each run by an agentic team, each a possible company, and why this is exactly where journalism comes in

# Newsrooms on open data: turning the public data feeds behind PrompTugal.news and the Storm Charles site into one data site, a vault per source with an API and its provenance, then building small, focused newsrooms on top, for farmers, investors, the sea, fire, tourism and AI, each run by an agentic team, each a possible company, and why this is exactly where journalism comes in

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-17 · [article v1.0.0](versions/newsrooms-on-open-data.md) · [newsroom v0.14.143](https://newsroom.sgit.ai/admin/versions.html) · dataopen-datapromptugalnewsroomsjournalismagenticcellsstartupsportugalarticle

***Abstract:** When I show people PrompTugal.news, the thing they like most is not the stories. It is the live data: the weather warnings, the fire risk, the flights over Faro, each value with where it came from and when it was read. The Storm Charles site went further, with 34 public datasets in a catalogue, each with its hash, every line labelled fact, evidence or hypothesis. That data is valuable, and today it is spread across sites and repositories. So the next step is to consolidate it: one data site, with a vault per public source, a collector written as code, an API described in OpenAPI, the provenance of every value, and a record of how much of each dataset is code and how much is agents, and what it costs in tokens. Then the interesting part: small, focused newsrooms on top of it, each about one subject, each run by an agentic team, each a possible small company. Agriculture, with weather, fire risk and water. Investors. The sea. Fire and civil protection. Tourism and travel. AI. Research like this is thin today, because journalism has lost the money to do it. I think this is exactly where journalism comes back in.*

Public sources, a vault and an API per source, then focused newsrooms on top, each run by an agentic team.

## In short

- **The live data is what people like most** when I show PrompTugal.news.
- **Consolidate it:** one data site, a vault per public source, an API, the provenance of every value.
- **Record how much is code and how much is agents,** and what each dataset costs in tokens.
- **Then focused newsrooms on top:** agriculture, investors, the sea, fire, tourism, AI.
- **Each run by an agentic team,** each a possible small company.
- **This is where journalism comes in:** turning public data into information people use.

## What we already have

More than I realised, when I asked for an inventory today:

- **Live data for 18 places in the Algarve,** collected every hour by code, with no model in the loop: IPMA's warnings, station observations, five-day forecasts, fire risk per municipality, UV and the sea forecast, and flights around Faro airport from an open feed. Every value carries when it was read, the source it came from, and the page a person would open to check it.
- **A data room for the storm:** 34 datasets in a catalogue, each with its size and hash, warnings, forecasts and stations, alert messages, and the decisions of the airport, bridges, metro, ferries, schools and hospitals, every line labelled fact, evidence or hypothesis ([Storm Charles, a newsroom built in a night](storm-charles-a-newsroom-built-in-a-night.md)).
- **A place file for every town,** kept by its own agent, every source with its link and date, every file signed ([PrompTugal.news by place](promptugal-news-by-place.md)).
- **APIs:** an OpenAPI 3.1 description, generated with the site, for PrompTugal.news and for each place, with Swagger pages to try them.
- **Our own observability:** each page records a view and a read, encrypted in the browser and written to a private vault.

## One data site

One public source, done properly: collector as code, a vault, an API, provenance, and who and what made it.

Today this is spread across the PrompTugal.news repository, the storm site and others. The next step is a data site of its own, with a repository behind it, built per public source. For each one:

1. **A collector, written as code,** polite to the source, with its schedule.
2. **A vault** for the dataset, encrypted and versioned, public where the source is public ([how a vault works](how-a-vault-works.md)).
3. **An API,** described in OpenAPI, with a Swagger page.
4. **The provenance of every value:** source, page, when it was read, by what.
5. **A card** saying who keeps it, how often it changes, and what it costs.

Only public sources, always. And the data site is the layer the newsrooms consume: PrompTugal.news, its town pages, and the focused newsrooms below.

## Code, agents and tokens

This connects to the provenance work ([who wrote it, who steered it, who signs it](who-steered-this.md)). For every dataset and every page made from it, I want to see how much is code, how much is agents, and how much is checked by a person; and how many tokens it spends.

That matters commercially. The collectors already run with no model at all. If most of the analysis is code that runs, with an agent only where judgement is needed, the cost per update is close to nothing. The storm site's own accounts show where tokens actually go: about 2,069 million session tokens, 98.7% of them re-reading, while its third-party model calls cost about a dollar by 03:00. Our rule is to write code for what repeats and use a model only where judgement is needed ([spend fewer tokens](spend-fewer-tokens.md)). A data newsroom built that way is cheap to run.

## Focused newsrooms

Six focused newsrooms on the same data: who reads them, what they join, what they could sell.

Once the data is in one place, with the news from PrompTugal.news beside it, we can build small newsrooms that each care about one thing. Sub-brands, each on its own address, each run by an agentic team ([the cell is the unit](the-cell-is-the-unit.md)):

- **Agriculture:** weather, fire risk, UV, rainfall and drought, joined to the news of each municipality. For farmers, co-operatives and insurers: what this week means for this valley.
- **Investors:** companies, funding and public records, from the Web Summit work onwards, with exchange rates and regional news. For investors and founders: who is building what, here.
- **The sea:** sea forecasts, ports and weather, for fishing, sailing and the ports.
- **Fire and civil protection:** fire risk per municipality, warnings and what was decided, the storm site made permanent, for councils, schools and residents.
- **Tourism and travel:** flights, weather, the sea, events and transport, for hotels, guides and visitors.
- **AI:** agents rated against standards, from GAMMA-Ray, and the news of the field, for the people deciding what to adopt ([agents rating agents](agents-rating-agents.md)).

Each one reads the same data site, adds the sources its subject needs, and publishes with the same provenance. And each is a possible small company: a few people, an agentic team, one subject, and readers who pay by the read, or businesses that pay for alerts and briefings ([paid by the read](paid-by-the-read.md)).

## Why this is journalism

The information these readers need mostly exists, in public, as raw data, and almost nobody turns it into something they can use. A farmer does not read IPMA's fire-risk JSON; a hotel does not join flights to the sea forecast. Doing that work, finding what matters, checking it, saying where it came from, used to be journalism's job, and the money for it has gone. I think agentic teams, with code doing the repeating work and people steering, make it affordable again. That is where journalism comes back in.

## What happens next

I have briefed PrompTugal.news's conductor agent to start the consolidation: a separate repository and site for the data, a vault per public source, APIs, and the provenance and cost records. And to check that our observability is still collecting visits on every site, because I want a daily debrief of who reads what. The focused newsrooms come after the data site exists.

## What this does not claim

- **The data site and the focused newsrooms are plans,** not built yet.
- **The token figures are the storm site's own,** from its accounts.
- **Each source's terms decide what can be republished;** public is not always free to reuse.

## Where this comes from

My own thinking, 17 November 2026, and an inventory of the PrompTugal.news repository the same day: its live collector, place files, OpenAPI generator, observability and the accountant's reports; the storm site as described in its brief and in [Storm Charles, a newsroom built in a night](storm-charles-a-newsroom-built-in-a-night.md). The public sources: [IPMA open data](https://api.ipma.pt/) and an open flight feed. Earlier on this site: [PrompTugal.news by place](promptugal-news-by-place.md), [how a vault works](how-a-vault-works.md), [who wrote it, who steered it, who signs it](who-steered-this.md), [spend fewer tokens](spend-fewer-tokens.md), [the cell is the unit](the-cell-is-the-unit.md), [agents rating agents](agents-rating-agents.md), [paid by the read](paid-by-the-read.md).

## Threads

Startups & strategyAgents & policy[This article as a graph →](graphs.md#newsrooms-on-open-data)

### Builds on

- [Storm Charles, a newsroom built in a night: one person, about thirty agents and a weather face over a data room, where every figure carries its source, the time it was read, and whether it is a fact, evidence or our hypothesis](storm-charles-a-newsroom-built-in-a-night.md) Storm Charles: about thirty agents built a weather face over a data room in a night, every figure sourced, timed and labelled.
- [PrompTugal.news by place: one publication for Portugal, the Algarve and every Algarve town, each place on its own subdomain from the start, each site a lens on one shared semantic graph, and one test for every story, does it connect to AI](promptugal-news-by-place.md) PrompTugal.news goes local: Portugal, the Algarve and every Algarve town, each on its own subdomain, each a lens on one graph, every story tied to AI.
- [How a vault works: an encrypted store that acts like a database, where a server that is fully compromised leaks nothing, one mutable file lets every other object be cached for ever, and a web page can open a file in four requests or run a whole app in a sandbox](how-a-vault-works.md) How an sgit vault acts like a database on a server that cannot read: one key-derived mutable file, everything else immutable.
- [Who wrote it, who steered it, who signs it: the provenance model PrompTugal.news adopted today, a type label, five axes and a ladder from "published by an agent" to "on the record", applied to seven articles on this site, and what the ladder cannot see yet, how much of the author is in a piece, the brief, the corrections and months of background](who-steered-this.md) PrompTugal.news's provenance model, a label, five axes and a ladder, applied to seven articles here, and the two measures it misses.
- [Spend fewer tokens: an agentic team's token bill is mostly a design choice, and the levers are files as memory, caching what repeats, code instead of models where you can, the right model for each step, no copy and paste, static outputs, and counting it all](spend-fewer-tokens.md) An agentic team's token bill is mostly a design choice: files as memory, caching, code where you can, the right model per step, static outputs, counting.
- [The cell is the unit: positioning AgentiCCells around small, focused cells, each with an objective, a deliverable and a behaviour policy, each with a page that sells it, a free recipe and three ways to get help, a catalogue that grows one need at a time, in each industry's own words, and why we should run our own work in cells first](the-cell-is-the-unit.md) The cell is the unit of AgentiCCells: one focused job with an objective, a deliverable and a behaviour policy, each with a page that sells it.
- [Agents rating agents: GAMMA-Ray, the draft standard eight agents built at Web Summit to rate an AI agent on its freedom and its governance from public evidence, joining eight instruments into 21 questions, with a review workflow where no agent marks its own work, twenty company cards kept at direct links, and every card honestly marked Draft](agents-rating-agents.md) GAMMA-Ray: eight agents built a draft standard to rate AI agents on freedom and governance, with no agent marking its own work, and every card a Draft.
- [Paid by the read: a proposal to news editors who want more revenue from the journalism they already make, without another subscription, the evidence on micropayments and why it mostly failed, the meter that charges by how much of a page was read and runs in the reader's browser, free for any publisher, a revenue share when PrompTugal.news carries a newsroom's stories with their source, and the associations we should be talking to in the UK and Portugal](paid-by-the-read.md) A proposal to news editors: earn from the read, not the subscription, with free client-side code, a revenue share and the associations.

### Continued by

- [From a feed to meaning: what the Storm Charles site did with public data that our new data site does not do yet, finding a source, reading its terms, writing parsers, keeping provenance, drawing it and saying what it means, three source sites to show it hourly, for the weather, the sea and fire risk, and the relay of briefs from this newsroom to the agents that will build them](from-a-feed-to-meaning.md) What the Storm Charles site did with public data that our data site does not yet, and three hourly source sites to show it.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 460 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=460)

**Posting this article on LinkedIn?** The cover is [newsrooms-on-open-data.jpg](banners/newsrooms-on-open-data.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/newsrooms-on-open-data.html)*
