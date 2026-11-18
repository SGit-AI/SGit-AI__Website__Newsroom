# From a feed to meaning: what the Storm Charles site did with public data that our new data site does not do yet, finding a source, reading its terms, writing parsers, keeping provenance, drawing it and saying what it means, three source sites to show it hourly, for the weather, the sea and fire risk, and the relay of briefs from this newsroom to the agents that will build them, sgit.ai

> Comparing the Storm Charles site with our new data site, data.promptugal.news, shows the difference between collecting data and understanding it. In a night, the storm site found its sources, read their terms, wrote parsers and converters, kept every value with its source and time, labelled each line fact, evidence or hypothesis, drew it a dozen ways, the lead time from warning to decision, warned against observed, a replay, and then said what it meant. The data site, built yesterday from my brief, does the first half very well: nine public sources, IPMA's warnings, observations, forecasts, fire risk, sea and UV, MeteoAlarm and flights around Faro, collected by code, served as JSON with an API and an OpenAPI description, each value with its provenance. It does not yet draw it, explain it, or show anyone how to use it; and when I checked this morning, the "hourly" data had last been read at 02:28, six hours earlier. So here is the next step: three source sites, website cells each built on one feed that changes through the day, the weather and its warnings, the sea, and fire risk, each rebuilt every hour, each with its charts, a plain "what changed", and a page on how to use the data. It is a working example of connecting any data with any data. And the way this brief travels is itself the example: from this newsroom, to PrompTugal's conductor, to the conductor on another account, to the agent that runs the data; and to the AgentiCCells team that will build the sites.

*Source: <https://newsroom.sgit.ai/articles/from-a-feed-to-meaning.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / From a feed to meaning: what the Storm Charles site did with public data that our new data site does not do yet, finding a source, reading its terms, writing parsers, keeping provenance, drawing it and saying what it means, three source sites to show it hourly, for the weather, the sea and fire risk, and the relay of briefs from this newsroom to the agents that will build them

# From a feed to meaning: what the Storm Charles site did with public data that our new data site does not do yet, finding a source, reading its terms, writing parsers, keeping provenance, drawing it and saying what it means, three source sites to show it hourly, for the weather, the sea and fire risk, and the relay of briefs from this newsroom to the agents that will build them

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-18 · [article v1.0.0](versions/from-a-feed-to-meaning.md) · [newsroom v999.0.0](https://newsroom.sgit.ai/admin/versions.html) · dataopen-datapromptugalstorm-charlesagenticcellsintegrationbriefsarticle

***Abstract:** Comparing the Storm Charles site with our new data site, data.promptugal.news, shows the difference between collecting data and understanding it. In a night, the storm site found its sources, read their terms, wrote parsers and converters, kept every value with its source and time, labelled each line fact, evidence or hypothesis, drew it a dozen ways, the lead time from warning to decision, warned against observed, a replay, and then said what it meant. The data site, built yesterday from my brief, does the first half very well: nine public sources, IPMA's warnings, observations, forecasts, fire risk, sea and UV, MeteoAlarm and flights around Faro, collected by code, served as JSON with an API and an OpenAPI description, each value with its provenance. It does not yet draw it, explain it, or show anyone how to use it; and when I checked this morning, the "hourly" data had last been read at 02:28, six hours earlier. So here is the next step: three source sites, website cells each built on one feed that changes through the day, the weather and its warnings, the sea, and fire risk, each rebuilt every hour, each with its charts, a plain "what changed", and a page on how to use the data. It is a working example of connecting any data with any data. And the way this brief travels is itself the example: from this newsroom, to PrompTugal's conductor, to the conductor on another account, to the agent that runs the data; and to the AgentiCCells team that will build the sites.*

From a feed to meaning, in seven steps: what the storm site did, and the steps the data site has reached.

## In short

- **The storm site went from a feed to meaning** in a night.
- **The data site does the first half well:** nine sources, collected by code, an API, provenance.
- **It does not yet draw, explain or teach,** and its hourly data had stopped at 02:28.
- **Next: three source sites,** the weather and warnings, the sea, fire risk.
- **Each rebuilt every hour,** with charts, "what changed" and how to use the data.
- **The brief's own route is the example:** newsroom, conductor, conductor, data agent, site team.

## Two sites, two halves

I asked for a comparison of the two sites, and the difference is clear.

The Storm Charles site, built overnight during Web Summit, did something I still find remarkable ([Storm Charles, a newsroom built in a night](storm-charles-a-newsroom-built-in-a-night.md), [after the storm](after-the-storm.md)). For each source it went the whole way:

1. **Found the source:** IPMA, MeteoAlarm, the transport operators, the airport.
2. **Read its terms,** and stopped where they said stop: it dropped one flight feed over its licence and stopped republishing the Lisbon Metro.
3. **Wrote parsers and converters,** as code, polite to the source.
4. **Kept provenance:** every value with its source and the time it was read, 34 datasets with their hashes.
5. **Labelled it:** fact, evidence or hypothesis, never a hypothesis presented as a fact.
6. **Drew it:** the lead time from warning to decision, warned against observed station by station, a replay of what was known when, flights against the wind.
7. **Said what it meant,** in a journal and in stories, with its mistakes.

The new data site, [data.promptugal.news](https://data.promptugal.news/), built yesterday from my brief ([newsrooms on open data](newsrooms-on-open-data.md)), does steps one to four very well. It reads nine public sources: IPMA's weather warnings, station observations, daily forecasts, fire risk for 278 municipalities, the sea forecast and the UV index; MeteoAlarm's alert feed; flights around Faro; and the storm's own archive. Each is collected by code, kept in a vault, served as plain JSON with an API and an OpenAPI description, and each card quotes the source's reuse terms. It has no articles and no opinion, by design.

What it does not do yet is steps five to seven: label, draw and explain. And it has a more basic problem. When I checked at 08:50 this morning, every source said "hourly" and every one had last been read at 02:28. Six hours of nothing; the weather and travel sites that read from it showed yesterday evening's data.

## Why this matters

Two reasons. The first is that this data is already useful: a farmer needs fire risk, a fisherman the sea, a hotel the warnings, and almost nobody turns IPMA's JSON into something they can use. The second is that it shows exactly what I mean when I say we can connect any data with any data ([any data, with any data](any-data-with-any-data.md)): find a source, map it, parse it, transform it, keep it with its provenance, and produce something a person understands. The storm site did that in a night. We should do it every hour, in public, and show people how.

## Three source sites

Three source sites on the data site, each rebuilt hourly: warnings and weather, the sea, fire risk.

So the proposal is a website cell per source, or per small group of sources that change through the day ([the website cell](the-website-cell.md)). Each reads from the data site, never from the source directly, and each is rebuilt every hour. Some of the drawing can also live on the data site itself, beside each source, the way the storm site drew its own datasets; the source sites go further, one subject each, for the people who need it.

- **Warnings and weather now:** IPMA's warnings and MeteoAlarm's messages, with the station observations. A map of what is in force; a timeline of warnings issued and lifted; and, the storm site's best idea, warned against observed: what the warning said, and what the stations then measured.
- **The sea:** the sea forecast for the twelve coastal places, with the rough-sea warnings and the UV index. Wave heights over the next days, place by place, for fishing, sailing, surfing and the ports.
- **Fire risk:** the daily risk for 278 municipalities, today and the next two days. A map that changes colour, what moved up or down since yesterday, and the places at the highest level.

Flights around Faro could be a fourth, as the storm site showed; at night it is mostly empty, so it suits a page that shows the day, not the hour.

## What each site has

What each source site carries: the data now, charts, what changed, provenance, and how to use the data.

- **The data now,** with its source and when it was read, and plainly "not a warning service".
- **Charts and a map,** made by code from the data, the same every hour.
- **What changed:** a short, labelled note, fact or hypothesis, written only when something did change; an agent writes it, code decides whether to call it.
- **How to use the data:** the address, a one-line request, a few lines of JavaScript, and a prompt for Claude, so a reader can take the same feed into their own site or agent.
- **How it is made:** which parts are code, which are agents, and what it costs, hour by hour ([who wrote it, who steered it, who signs it](who-steered-this.md)).

## The hourly chain

The sites only work if the hour holds. The chain I want:

1. **At a quarter past,** the data site's collectors read every source, as code.
2. **By half past,** each source site rebuilds from the data site's latest files, as code.
3. **Only when something changed,** an agent writes the "what changed" note and a person can review it.
4. **Every step logs** what it read, when, and whether it worked, so a missed hour is visible within the hour, not six hours later.

Mostly code, so mostly free: the tokens go into the note, and only when there is something to say ([spend fewer tokens](spend-fewer-tokens.md)).

## How this brief travels

How this brief travels: newsroom, two conductors, the data agent, and the site team.

The way this brief reaches the agents that will act on it is itself a good example of what we do. I write it here, in the newsroom, in public. This newsroom's writer sends it to PrompTugal.news's conductor; that conductor relays it to the conductor running PrompTugal's work on another account; and that conductor gives it to the agent that runs the data site. The part about the source sites goes to the AgentiCCells conductor, whose team builds websites. Each hop is a message between sessions, each agent records what it received and what it did, and the data itself moves between them through vaults and public files. No person copies anything; I steer, and I approve.

## What this does not claim

- **The source sites are a proposal;** none is built yet.
- **The six-hour gap** is what I saw at 08:50 on 18 November; it may be fixed by the time you read this.
- **None of these sites is a warning service;** IPMA and ANEPC are.

## Where this comes from

[data.promptugal.news](https://data.promptugal.news/) and its [catalogue](https://data.promptugal.news/api/v1/index.json), read at 08:50 UTC on 18 November 2026; [weather.promptugal.news](https://weather.promptugal.news/) and [travel.promptugal.news](https://travel.promptugal.news/), read the same morning; the Storm Charles site and repository, as in [after the storm](after-the-storm.md). Earlier on this site: [Storm Charles, a newsroom built in a night](storm-charles-a-newsroom-built-in-a-night.md), [newsrooms on open data](newsrooms-on-open-data.md), [any data, with any data](any-data-with-any-data.md), [the website cell](the-website-cell.md), [who wrote it, who steered it, who signs it](who-steered-this.md), [spend fewer tokens](spend-fewer-tokens.md).

## Threads

Agents & policyStartups & strategy[This article as a graph →](graphs.md#from-a-feed-to-meaning)

### Builds on

- [Storm Charles, a newsroom built in a night: one person, about thirty agents and a weather face over a data room, where every figure carries its source, the time it was read, and whether it is a fact, evidence or our hypothesis](storm-charles-a-newsroom-built-in-a-night.md) Storm Charles: about thirty agents built a weather face over a data room in a night, every figure sourced, timed and labelled.
- [After the storm: Storm Charles, part two, how a site built in a night kept growing the next day by spoken briefs, a transport desk that stopped where an operator's terms said stop, flights drawn against the wind within a free feed's daily limit, every collector moved onto open-weight models through one router, an AWS plan with no AWS account, and the night the model account ran empty and only the models stopped](after-the-storm.md) Storm Charles, part two: transport, flights against the wind, one model router, an AWS plan with no account, and what it all cost.
- [Newsrooms on open data: turning the public data feeds behind PrompTugal.news and the Storm Charles site into one data site, a vault per source with an API and its provenance, then building small, focused newsrooms on top, for farmers, investors, the sea, fire, tourism and AI, each run by an agentic team, each a possible company, and why this is exactly where journalism comes in](newsrooms-on-open-data.md) Turning PrompTugal.news's public data feeds into one data site, then small focused newsrooms on top, each run by an agentic team.
- [Any data, with any data: why I am now comfortable saying we can connect any data source with any other, the nine steps from access to a vault, a key and a map on the other side, how each owner keeps control, where the person stays in charge, and why connecting two, five, fifty or a hundred datasets should be something an agentic cell sells](any-data-with-any-data.md) Why we can now connect any data source with any other: nine steps, owners keep control, a person approves every key, sold as cells.
- [The website cell: what we now sell, a GitHub repository fully set up with a live site on its own address, a CLAUDE.md and a behaviour policy, five designs by a team of agents, and then the site is yours to change with your own Claude, what it should cost, how it compares with Wix, Squarespace, Framer, Lovable and a freelancer, who already sells something close to it, and where to find buyers and partners](the-website-cell.md) The website cell mapped: a repository fully set up, five designs by agents, owned with your own Claude; price, competitors, partners.
- [Who wrote it, who steered it, who signs it: the provenance model PrompTugal.news adopted today, a type label, five axes and a ladder from "published by an agent" to "on the record", applied to seven articles on this site, and what the ladder cannot see yet, how much of the author is in a piece, the brief, the corrections and months of background](who-steered-this.md) PrompTugal.news's provenance model, a label, five axes and a ladder, applied to seven articles here, and the two measures it misses.
- [Spend fewer tokens: an agentic team's token bill is mostly a design choice, and the levers are files as memory, caching what repeats, code instead of models where you can, the right model for each step, no copy and paste, static outputs, and counting it all](spend-fewer-tokens.md) An agentic team's token bill is mostly a design choice: files as memory, caching, code where you can, the right model per step, static outputs, counting.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 470 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=470)

**Posting this article on LinkedIn?** The cover is [from-a-feed-to-meaning.jpg](banners/from-a-feed-to-meaning.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/from-a-feed-to-meaning.html)*
