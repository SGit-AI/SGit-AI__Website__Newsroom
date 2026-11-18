---
title: From a feed to meaning: what the Storm Charles site did with public data that our new data site does not do yet, finding a source, reading its terms, writing parsers, keeping provenance, drawing it and saying what it means, three source sites to show it hourly, for the weather, the sea and fire risk, and the relay of briefs from this newsroom to the agents that will build them
date: 2026-11-18
author: Dinis Cruz
author_url: about/index.html
summary: Comparing the Storm Charles site with our new data site, data.promptugal.news, shows the difference between collecting data and understanding it. In a night, the storm site found its sources, read their terms, wrote parsers and converters, kept every value with its source and time, labelled each line fact, evidence or hypothesis, drew it a dozen ways, the lead time from warning to decision, warned against observed, a replay, and then said what it meant. The data site, built yesterday from my brief, does the first half very well: nine public sources, IPMA's warnings, observations, forecasts, fire risk, sea and UV, MeteoAlarm and flights around Faro, collected by code, served as JSON with an API and an OpenAPI description, each value with its provenance. It does not yet draw it, explain it, or show anyone how to use it; and when I checked this morning, the "hourly" data had last been read at 02:28, six hours earlier. So here is the next step: three source sites, website cells each built on one feed that changes through the day, the weather and its warnings, the sea, and fire risk, each rebuilt every hour, each with its charts, a plain "what changed", and a page on how to use the data. It is a working example of connecting any data with any data. And the way this brief travels is itself the example: from this newsroom, to PrompTugal's conductor, to the conductor on another account, to the agent that runs the data; and to the AgentiCCells team that will build the sites.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: data, open-data, promptugal, storm-charles, agenticcells, integration, briefs, article
status: published
---

!shot ftm-ladder.webp | images/ | From a feed to meaning, in seven steps: what the storm site did, and the steps the data site has reached. | process

## In short {#in-short}

- **The storm site went from a feed to meaning** in a night.
- **The data site does the first half well:** nine sources, collected by code, an API, provenance.
- **It does not yet draw, explain or teach,** and its hourly data had stopped at 02:28.
- **Next: three source sites,** the weather and warnings, the sea, fire risk.
- **Each rebuilt every hour,** with charts, "what changed" and how to use the data.
- **The brief's own route is the example:** newsroom, conductor, conductor, data agent, site team.

## Two sites, two halves {#halves}

I asked for a comparison of the two sites, and the difference is clear.

The Storm Charles site, built overnight during Web Summit, did something I still find remarkable ([Storm Charles, a newsroom built in a night](/articles/storm-charles-a-newsroom-built-in-a-night.html), [after the storm](/articles/after-the-storm.html)). For each source it went the whole way:

1. **Found the source:** IPMA, MeteoAlarm, the transport operators, the airport.
2. **Read its terms,** and stopped where they said stop: it dropped one flight feed over its licence and stopped republishing the Lisbon Metro.
3. **Wrote parsers and converters,** as code, polite to the source.
4. **Kept provenance:** every value with its source and the time it was read, 34 datasets with their hashes.
5. **Labelled it:** fact, evidence or hypothesis, never a hypothesis presented as a fact.
6. **Drew it:** the lead time from warning to decision, warned against observed station by station, a replay of what was known when, flights against the wind.
7. **Said what it meant,** in a journal and in stories, with its mistakes.

The new data site, [data.promptugal.news](https://data.promptugal.news/), built yesterday from my brief ([newsrooms on open data](/articles/newsrooms-on-open-data.html)), does steps one to four very well. It reads nine public sources: IPMA's weather warnings, station observations, daily forecasts, fire risk for 278 municipalities, the sea forecast and the UV index; MeteoAlarm's alert feed; flights around Faro; and the storm's own archive. Each is collected by code, kept in a vault, served as plain JSON with an API and an OpenAPI description, and each card quotes the source's reuse terms. It has no articles and no opinion, by design.

What it does not do yet is steps five to seven: label, draw and explain. And it has a more basic problem. When I checked at 08:50 this morning, every source said "hourly" and every one had last been read at 02:28. Six hours of nothing; the weather and travel sites that read from it showed yesterday evening's data.

## Why this matters {#why}

Two reasons. The first is that this data is already useful: a farmer needs fire risk, a fisherman the sea, a hotel the warnings, and almost nobody turns IPMA's JSON into something they can use. The second is that it shows exactly what I mean when I say we can connect any data with any data ([any data, with any data](/articles/any-data-with-any-data.html)): find a source, map it, parse it, transform it, keep it with its provenance, and produce something a person understands. The storm site did that in a night. We should do it every hour, in public, and show people how.

## Three source sites {#sources}

!shot ftm-cells.webp | images/ | Three source sites on the data site, each rebuilt hourly: warnings and weather, the sea, fire risk. | architecture

So the proposal is a website cell per source, or per small group of sources that change through the day ([the website cell](/articles/the-website-cell.html)). Each reads from the data site, never from the source directly, and each is rebuilt every hour. Some of the drawing can also live on the data site itself, beside each source, the way the storm site drew its own datasets; the source sites go further, one subject each, for the people who need it.

- **Warnings and weather now:** IPMA's warnings and MeteoAlarm's messages, with the station observations. A map of what is in force; a timeline of warnings issued and lifted; and, the storm site's best idea, warned against observed: what the warning said, and what the stations then measured.
- **The sea:** the sea forecast for the twelve coastal places, with the rough-sea warnings and the UV index. Wave heights over the next days, place by place, for fishing, sailing, surfing and the ports.
- **Fire risk:** the daily risk for 278 municipalities, today and the next two days. A map that changes colour, what moved up or down since yesterday, and the places at the highest level.

Flights around Faro could be a fourth, as the storm site showed; at night it is mostly empty, so it suits a page that shows the day, not the hour.

## What each site has {#each}

!shot ftm-site.webp | images/ | What each source site carries: the data now, charts, what changed, provenance, and how to use the data. | concept

- **The data now,** with its source and when it was read, and plainly "not a warning service".
- **Charts and a map,** made by code from the data, the same every hour.
- **What changed:** a short, labelled note, fact or hypothesis, written only when something did change; an agent writes it, code decides whether to call it.
- **How to use the data:** the address, a one-line request, a few lines of JavaScript, and a prompt for Claude, so a reader can take the same feed into their own site or agent.
- **How it is made:** which parts are code, which are agents, and what it costs, hour by hour ([who wrote it, who steered it, who signs it](/articles/who-steered-this.html)).

## The hourly chain {#chain}

The sites only work if the hour holds. The chain I want:

1. **At a quarter past,** the data site's collectors read every source, as code.
2. **By half past,** each source site rebuilds from the data site's latest files, as code.
3. **Only when something changed,** an agent writes the "what changed" note and a person can review it.
4. **Every step logs** what it read, when, and whether it worked, so a missed hour is visible within the hour, not six hours later.

Mostly code, so mostly free: the tokens go into the note, and only when there is something to say ([spend fewer tokens](/articles/spend-fewer-tokens.html)).

## How this brief travels {#relay}

!shot ftm-relay.webp | images/ | How this brief travels: newsroom, two conductors, the data agent, and the site team. | diagram

The way this brief reaches the agents that will act on it is itself a good example of what we do. I write it here, in the newsroom, in public. This newsroom's writer sends it to PrompTugal.news's conductor; that conductor relays it to the conductor running PrompTugal's work on another account; and that conductor gives it to the agent that runs the data site. The part about the source sites goes to the AgentiCCells conductor, whose team builds websites. Each hop is a message between sessions, each agent records what it received and what it did, and the data itself moves between them through vaults and public files. No person copies anything; I steer, and I approve.

## What this does not claim {#limits}

- **The source sites are a proposal;** none is built yet.
- **The six-hour gap** is what I saw at 08:50 on 18 November; it may be fixed by the time you read this.
- **None of these sites is a warning service;** IPMA and ANEPC are.

## Where this comes from {#sources-used}

[data.promptugal.news](https://data.promptugal.news/) and its [catalogue](https://data.promptugal.news/api/v1/index.json), read at 08:50 UTC on 18 November 2026; [weather.promptugal.news](https://weather.promptugal.news/) and [travel.promptugal.news](https://travel.promptugal.news/), read the same morning; the Storm Charles site and repository, as in [after the storm](/articles/after-the-storm.html). Earlier on this site: [Storm Charles, a newsroom built in a night](/articles/storm-charles-a-newsroom-built-in-a-night.html), [newsrooms on open data](/articles/newsrooms-on-open-data.html), [any data, with any data](/articles/any-data-with-any-data.html), [the website cell](/articles/the-website-cell.html), [who wrote it, who steered it, who signs it](/articles/who-steered-this.html), [spend fewer tokens](/articles/spend-fewer-tokens.html).
