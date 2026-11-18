# Ten days to a data platform: how PrompTugal.news went from a newsroom at Web Summit to twelve public data sources, a register of 92 sources read and not read, a dozen sites on its own domain and two cyber-threat feeds cleared to run, with a security agent on every change, and why each step made the next one cheaper, sgit.ai

> The first commit of PrompTugal.news was at 00:08 on 4 November: a newsroom for Web Summit. Two weeks and 6,790 commits later it is a data platform for Portugal's places. The storm site went live just after midnight on 11 November. On 15 November we gave every place its own agent: Portugal, the Algarve and each of its towns, with a behaviour policy each. On 17 November, one decision about the site factory let us create a data site, and then five more sites in one request: weather, travel, civic, startups and the data itself. Today, 18 November, the team added an events site, a register of 92 sources with the reason we do or do not read each, three new data sources, a library, video and webcam sites, and a cyber-threat site whose first two feeds, the known exploited vulnerabilities and the CVE list, were cleared to run by the security agent. Every change now passes a security review before and after. This is part one of the series, the timeline, and the point of it: each step made the next one cheaper, so the speed keeps growing.

*Source: <https://newsroom.sgit.ai/articles/ten-days-to-a-data-platform.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Ten days to a data platform: how PrompTugal.news went from a newsroom at Web Summit to twelve public data sources, a register of 92 sources read and not read, a dozen sites on its own domain and two cyber-threat feeds cleared to run, with a security agent on every change, and why each step made the next one cheaper

# Ten days to a data platform: how PrompTugal.news went from a newsroom at Web Summit to twelve public data sources, a register of 92 sources read and not read, a dozen sites on its own domain and two cyber-threat feeds cleared to run, with a security agent on every change, and why each step made the next one cheaper

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-18 · [article v1.0.0](versions/ten-days-to-a-data-platform.md) · [newsroom v999.0.0](https://newsroom.sgit.ai/admin/versions.html) · promptugaldatatimelineagentssecurityseriesarticle

***Abstract:** The first commit of PrompTugal.news was at 00:08 on 4 November: a newsroom for Web Summit. Two weeks and 6,790 commits later it is a data platform for Portugal's places. The storm site went live just after midnight on 11 November. On 15 November we gave every place its own agent: Portugal, the Algarve and each of its towns, with a behaviour policy each. On 17 November, one decision about the site factory let us create a data site, and then five more sites in one request: weather, travel, civic, startups and the data itself. Today, 18 November, the team added an events site, a register of 92 sources with the reason we do or do not read each, three new data sources, a library, video and webcam sites, and a cyber-threat site whose first two feeds, the known exploited vulnerabilities and the CVE list, were cleared to run by the security agent. Every change now passes a security review before and after. This is part one of the series, the timeline, and the point of it: each step made the next one cheaper, so the speed keeps growing.*

Two weeks of PrompTugal.news: newsroom, storm, place agents, the data site, five sites, events.

## In short

- **4 November:** the first commit, a newsroom for Web Summit.
- **11 November:** the storm site, built overnight.
- **15 November:** an agent for every place, each with a behaviour policy.
- **17 November:** the data site, then five sites in one request.
- **18 November:** events, a register of 92 sources, three new data sources, a library, and cyber-threat feeds cleared.
- **Each step made the next one cheaper.**

Part one of [gaining speed](gaining-speed.md).

## A newsroom for a week

PrompTugal.news began at 00:08 on 4 November, an independent newsroom for Web Summit, "from Portugal for Europe" ([PrompTugal.news, the newsroom we ran at Web Summit](promptugal-news-the-newsroom-we-ran.md)). The reading meter, which charges readers for the share of a page they read, was live the next morning. On 6 November the agents made more than 1,200 commits in a day.

## The storm, and then the places

When Storm Charles reached Lisbon, the newsroom built its own incident site overnight: live from 00:13 on 11 November, with a data room behind a weather page ([Storm Charles, a newsroom built in a night](storm-charles-a-newsroom-built-in-a-night.md)). It was the first time the team turned public data into something people used, and it set the pattern.

After the summit, the newsroom went local. At 21:44 on 15 November the brief gave every place its own agent, Portugal, the Algarve and each of its towns, and ten minutes later the behaviour policies for 21 place agents were published ([PrompTugal.news by place](promptugal-news-by-place.md)). The site now covers 36 places.

## A data site, then five

On 17 November I briefed a data site: one place for every public source, collected by code, with an API and the provenance of every value ([newsrooms on open data](newsrooms-on-open-data.md)). The repository and address were created by the factory at 18:48 and the site was live a minute later. At 18:59 a single request to the factory created four more, weather, travel, civic and startups: five sites in an evening. By the evening the data site read nine sources, IPMA's warnings, observations, forecasts, fire risk, sea and UV, MeteoAlarm, and flights around Faro.

## Today

Today the speed shows in a single day:

- **An events site,** created by the factory at 14:29, with 141 events read from official agendas and 109 found through discovery, each with its legal basis ([whose event is it?](whose-event-is-it.md)).
- **A register of 92 sources,** 18 read and 74 not, each with the terms or robots.txt quoted and the date read, and requests on the record drafted for the ones we do not read.
- **Three new data sources:** public contracts from Portal BASE, the councils' and theatres' event agendas, and public posts from Bluesky and Mastodon. Twelve in all.
- **New sites:** signals, a library, videos, live webcams and cyber, created by the factory between 14:43 and 17:48.
- **Cyber-threat feeds:** CISA's catalogue of known exploited vulnerabilities and the CVE list were cleared to run by the security agent; sources that allow only non-commercial use wait for my decision.
- **A licence on every value:** every piece of data the sites serve now carries a link to its licence.

## Security on every change

The speed is safe because of the structure around it. Every wake of every agent now runs a security review before the work and after it, with an application-security review on any code change and a published threat model for each automation; the security agent sweeps all of PrompTugal's repositories every hour, and keeps a public log at [promptugal.news/security/](https://promptugal.news/security/). The team runs on 72 behaviour policies, one per agent, new agents starting relaxed and tightened as their work is mapped ([what can your agent reach?](what-can-your-agent-reach.md)). And there is a rule about people: public office, public life and people publishing under their own name may be named and linked; private information never.

## Why it keeps speeding up

Commits per day on PrompTugal.news, 4 to 18 November: the newsroom, the storm, the places, the platform.

The commits do not show it: the busiest day was 6 November, during the summit. What changed is how much each commit buys. Each step left something behind that the next one used. The storm left a way of collecting public data with its provenance. The place agents left a structure per town. The data site left an API the other sites read. The factory left the ability to create a site in a minute. And the behaviour policies and the security passes left a way to add agents without losing control. So the cost of the next site, the next source, the next agent keeps falling, and the work gets faster, not slower, as it grows.

## What this does not claim

- **Some of today's sites are placeholders** or first versions, and say so.
- **The cyber feeds are cleared, not yet collecting.**
- **Commit counts are a measure of activity,** not of value.

## Where this comes from

The PrompTugal.news repository (git history, briefs and guidance), read on 18 November 2026; [data.promptugal.news](https://data.promptugal.news/) and its [catalogue](https://data.promptugal.news/api/v1/index.json) (v0.1.41) and [register of sources](https://data.promptugal.news/sources/); [events.promptugal.news](https://events.promptugal.news/); [promptugal.news/security/](https://promptugal.news/security/); the AgentiCCells factory's request records. Earlier on this site: [gaining speed](gaining-speed.md), [PrompTugal.news, the newsroom we ran at Web Summit](promptugal-news-the-newsroom-we-ran.md), [Storm Charles, a newsroom built in a night](storm-charles-a-newsroom-built-in-a-night.md), [PrompTugal.news by place](promptugal-news-by-place.md), [newsrooms on open data](newsrooms-on-open-data.md), [whose event is it?](whose-event-is-it.md), [what can your agent reach?](what-can-your-agent-reach.md).

## Threads

Startups & strategyAgents & policy[This article as a graph →](graphs.md#ten-days-to-a-data-platform)

### Builds on

- [Gaining speed: a series on what happens when you productise the way you build, PrompTugal.news going from a newsroom at Web Summit to a data intelligence platform for Portugal's places in two weeks, a factory that turns one commit into a site with its owner, money that flows back to the sources, sites built on the data in minutes, the librarian, and a team like this for sale](gaining-speed.md) A series on what happens when you productise how you build: PrompTugal.news from a summit newsroom to a data platform in two weeks.
- [PrompTugal.news, the newsroom we ran at Web Summit: desks of agents that captured, mapped, wrote and reviewed 73 signed articles in ten days, an accountant that counted every run, and fifty outreach drafts that no agent was allowed to send](promptugal-news-the-newsroom-we-ran.md) PrompTugal.news: 73 signed articles in ten days from desks of agents, a reviewer for every draft, and fifty outreach drafts no agent could send.
- [Storm Charles, a newsroom built in a night: one person, about thirty agents and a weather face over a data room, where every figure carries its source, the time it was read, and whether it is a fact, evidence or our hypothesis](storm-charles-a-newsroom-built-in-a-night.md) Storm Charles: about thirty agents built a weather face over a data room in a night, every figure sourced, timed and labelled.
- [PrompTugal.news by place: one publication for Portugal, the Algarve and every Algarve town, each place on its own subdomain from the start, each site a lens on one shared semantic graph, and one test for every story, does it connect to AI](promptugal-news-by-place.md) PrompTugal.news goes local: Portugal, the Algarve and every Algarve town, each on its own subdomain, each a lens on one graph, every story tied to AI.
- [Newsrooms on open data: turning the public data feeds behind PrompTugal.news and the Storm Charles site into one data site, a vault per source with an API and its provenance, then building small, focused newsrooms on top, for farmers, investors, the sea, fire, tourism and AI, each run by an agentic team, each a possible company, and why this is exactly where journalism comes in](newsrooms-on-open-data.md) Turning PrompTugal.news's public data feeds into one data site, then small focused newsrooms on top, each run by an agentic team.
- [Whose event is it? Why Luma, Eventbrite, Meetup and Partiful will not let a site like PrompTugal.news show the public events their organisers want seen, what their terms actually say, who owns an event listing, what UK, EU and Portuguese law allows, what organisers expect, and how PrompTugal.news now collects events with a legal basis and the evidence for every one](whose-event-is-it.md) Why Luma, Eventbrite, Meetup and Partiful block sites like ours, who owns an event listing, what the law allows, and how we collect now.
- [What can your agent reach? RiskMandate and the Agent Behaviour Policy, explained for the person who has to decide](what-can-your-agent-reach.md) RiskMandate and the Agent Behaviour Policy in plain words: what it does, why it is not real time, which agents it covers, and how it gets into the room.

### Continued by

- [The librarian: my favourite agent, and why a data platform needs a library at its heart, a catalogue of everything PrompTugal.news has read, each item with its source, licence, evidence and links, a graph of how it all connects, an invitation to real librarians, and the next shelves, official sources and the law](the-librarian.md) The librarian, my favourite agent: a library at the heart of the data platform, every item catalogued, sourced and linked.
- [Sites on the data: what happens when a data platform meets a factory that makes a site in minutes, a page that draws IPMA's data six ways, an invented holiday-homes company whose bookings are simulated and whose weather, sea and events are real, demos for weather, events and cyber, and how each experiment, a new industry, a new view, a new idea, is now a site published in ten or twenty minutes](sites-on-the-data.md) When a data platform meets a site factory, every idea becomes a site: IPMA six ways, and holiday homes with real weather and events.
- [Gaining speed: a series on what happens when you productise the way you build, PrompTugal.news going from a newsroom at Web Summit to a data intelligence platform for Portugal's places in two weeks, a factory that turns one commit into a site with its owner, money that flows back to the sources, sites built on the data in minutes, the librarian, and a team like this for sale](gaining-speed.md) A series on what happens when you productise how you build: PrompTugal.news from a summit newsroom to a data platform in two weeks.
- [A team like this, for sale: what we sell is not the platform, it is the agentic team that built it, its roles, its behaviour policies, its security passes and its speed, with the code open and the data public, and who I want to talk to now that PrompTugal.news is a working data platform and not an experiment](a-team-like-this.md) What we sell is not the open platform but a team like the one that built it, and who I want to talk to now.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 478 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=478)

**Posting this article on LinkedIn?** The cover is [ten-days-to-a-data-platform.jpg](banners/ten-days-to-a-data-platform.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/ten-days-to-a-data-platform.html)*
