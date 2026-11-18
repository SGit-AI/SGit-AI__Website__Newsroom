---
title: Ten days to a data platform: how PrompTugal.news went from a newsroom at Web Summit to twelve public data sources, a register of 92 sources read and not read, a dozen sites on its own domain and two cyber-threat feeds cleared to run, with a security agent on every change, and why each step made the next one cheaper
date: 2026-11-18
author: Dinis Cruz
author_url: about/index.html
summary: The first commit of PrompTugal.news was at 00:08 on 4 November: a newsroom for Web Summit. Two weeks and 6,790 commits later it is a data platform for Portugal's places. The storm site went live just after midnight on 11 November. On 15 November we gave every place its own agent: Portugal, the Algarve and each of its towns, with a behaviour policy each. On 17 November, one decision about the site factory let us create a data site, and then five more sites in one request: weather, travel, civic, startups and the data itself. Today, 18 November, the team added an events site, a register of 92 sources with the reason we do or do not read each, three new data sources, a library, video and webcam sites, and a cyber-threat site whose first two feeds, the known exploited vulnerabilities and the CVE list, were cleared to run by the security agent. Every change now passes a security review before and after. This is part one of the series, the timeline, and the point of it: each step made the next one cheaper, so the speed keeps growing.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: promptugal, data, timeline, agents, security, series, article
status: published
---

!shot tdp-timeline.webp | images/ | Two weeks of PrompTugal.news: newsroom, storm, place agents, the data site, five sites, events. | timeline

## In short {#in-short}

- **4 November:** the first commit, a newsroom for Web Summit.
- **11 November:** the storm site, built overnight.
- **15 November:** an agent for every place, each with a behaviour policy.
- **17 November:** the data site, then five sites in one request.
- **18 November:** events, a register of 92 sources, three new data sources, a library, and cyber-threat feeds cleared.
- **Each step made the next one cheaper.**

Part one of [gaining speed](/articles/gaining-speed.html).

## A newsroom for a week {#newsroom}

PrompTugal.news began at 00:08 on 4 November, an independent newsroom for Web Summit, "from Portugal for Europe" ([PrompTugal.news, the newsroom we ran at Web Summit](/articles/promptugal-news-the-newsroom-we-ran.html)). The reading meter, which charges readers for the share of a page they read, was live the next morning. On 6 November the agents made more than 1,200 commits in a day.

## The storm, and then the places {#storm}

When Storm Charles reached Lisbon, the newsroom built its own incident site overnight: live from 00:13 on 11 November, with a data room behind a weather page ([Storm Charles, a newsroom built in a night](/articles/storm-charles-a-newsroom-built-in-a-night.html)). It was the first time the team turned public data into something people used, and it set the pattern.

After the summit, the newsroom went local. At 21:44 on 15 November the brief gave every place its own agent, Portugal, the Algarve and each of its towns, and ten minutes later the behaviour policies for 21 place agents were published ([PrompTugal.news by place](/articles/promptugal-news-by-place.html)). The site now covers 36 places.

## A data site, then five {#five}

On 17 November I briefed a data site: one place for every public source, collected by code, with an API and the provenance of every value ([newsrooms on open data](/articles/newsrooms-on-open-data.html)). The repository and address were created by the factory at 18:48 and the site was live a minute later. At 18:59 a single request to the factory created four more, weather, travel, civic and startups: five sites in an evening. By the evening the data site read nine sources, IPMA's warnings, observations, forecasts, fire risk, sea and UV, MeteoAlarm, and flights around Faro.

## Today {#today}

Today the speed shows in a single day:

- **An events site,** created by the factory at 14:29, with 141 events read from official agendas and 109 found through discovery, each with its legal basis ([whose event is it?](/articles/whose-event-is-it.html)).
- **A register of 92 sources,** 18 read and 74 not, each with the terms or robots.txt quoted and the date read, and requests on the record drafted for the ones we do not read.
- **Three new data sources:** public contracts from Portal BASE, the councils' and theatres' event agendas, and public posts from Bluesky and Mastodon. Twelve in all.
- **New sites:** signals, a library, videos, live webcams and cyber, created by the factory between 14:43 and 17:48.
- **Cyber-threat feeds:** CISA's catalogue of known exploited vulnerabilities and the CVE list were cleared to run by the security agent; sources that allow only non-commercial use wait for my decision.
- **A licence on every value:** every piece of data the sites serve now carries a link to its licence.

## Security on every change {#security}

The speed is safe because of the structure around it. Every wake of every agent now runs a security review before the work and after it, with an application-security review on any code change and a published threat model for each automation; the security agent sweeps all of PrompTugal's repositories every hour, and keeps a public log at [promptugal.news/security/](https://promptugal.news/security/). The team runs on 72 behaviour policies, one per agent, new agents starting relaxed and tightened as their work is mapped ([what can your agent reach?](/articles/what-can-your-agent-reach.html)). And there is a rule about people: public office, public life and people publishing under their own name may be named and linked; private information never.

## Why it keeps speeding up {#why}

!shot tdp-commits.webp | images/ | Commits per day on PrompTugal.news, 4 to 18 November: the newsroom, the storm, the places, the platform. | chart

The commits do not show it: the busiest day was 6 November, during the summit. What changed is how much each commit buys. Each step left something behind that the next one used. The storm left a way of collecting public data with its provenance. The place agents left a structure per town. The data site left an API the other sites read. The factory left the ability to create a site in a minute. And the behaviour policies and the security passes left a way to add agents without losing control. So the cost of the next site, the next source, the next agent keeps falling, and the work gets faster, not slower, as it grows.

## What this does not claim {#limits}

- **Some of today's sites are placeholders** or first versions, and say so.
- **The cyber feeds are cleared, not yet collecting.**
- **Commit counts are a measure of activity,** not of value.

## Where this comes from {#sources}

The PrompTugal.news repository (git history, briefs and guidance), read on 18 November 2026; [data.promptugal.news](https://data.promptugal.news/) and its [catalogue](https://data.promptugal.news/api/v1/index.json) (v0.1.41) and [register of sources](https://data.promptugal.news/sources/); [events.promptugal.news](https://events.promptugal.news/); [promptugal.news/security/](https://promptugal.news/security/); the AgentiCCells factory's request records. Earlier on this site: [gaining speed](/articles/gaining-speed.html), [PrompTugal.news, the newsroom we ran at Web Summit](/articles/promptugal-news-the-newsroom-we-ran.html), [Storm Charles, a newsroom built in a night](/articles/storm-charles-a-newsroom-built-in-a-night.html), [PrompTugal.news by place](/articles/promptugal-news-by-place.html), [newsrooms on open data](/articles/newsrooms-on-open-data.html), [whose event is it?](/articles/whose-event-is-it.html), [what can your agent reach?](/articles/what-can-your-agent-reach.html).
