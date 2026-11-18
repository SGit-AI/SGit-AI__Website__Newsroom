# After the storm: Storm Charles, part two, how a site built in a night kept growing the next day by spoken briefs, a transport desk that stopped where an operator's terms said stop, flights drawn against the wind within a free feed's daily limit, every collector moved onto open-weight models through one router, an AWS plan with no AWS account, and the night the model account ran empty and only the models stopped, sgit.ai

> The first night of Storm Charles built a newsroom: a weather page over a data room. This is what happened after, on 11 and 12 November, when I kept talking to the site and the agents kept building. At 10:25 I asked whether we were tracking flights and transport; within ten minutes a transport agent had its own key and its first reading, and by the evening it was reading ten operators, from the Lisbon bridges to CP's trains, and had stopped reading the Lisbon Metro at 12:08 because its terms forbid republishing without consent. At 22:00 I asked for the planes on a map, intersected with the wind; by 22:24 the flights desk had dropped its first feed over its licence, moved to adsb.lol, and fitted its polling inside 500 free requests a day. The same evening every collector moved onto open-weight models through one router, each call with a trace id, and an AWS agent mapped how the runners could move to the cloud, with no AWS account and nothing deployed. The accounts tell the rest: 3.84 billion tokens, 98.7% of them re-reading, against about 2.50 dollars a day of model calls on a 20 dollar cap, 43 agents, 147 sessions and 106 hand-overs. And the night the model account ran out of credit, 3,557 calls were refused and nothing else stopped.

*Source: <https://newsroom.sgit.ai/articles/after-the-storm.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / After the storm: Storm Charles, part two, how a site built in a night kept growing the next day by spoken briefs, a transport desk that stopped where an operator's terms said stop, flights drawn against the wind within a free feed's daily limit, every collector moved onto open-weight models through one router, an AWS plan with no AWS account, and the night the model account ran empty and only the models stopped

# After the storm: Storm Charles, part two, how a site built in a night kept growing the next day by spoken briefs, a transport desk that stopped where an operator's terms said stop, flights drawn against the wind within a free feed's daily limit, every collector moved onto open-weight models through one router, an AWS plan with no AWS account, and the night the model account ran empty and only the models stopped

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-17 · [article v1.0.0](versions/after-the-storm.md) · [newsroom v0.14.145](https://newsroom.sgit.ai/admin/versions.html) · storm-charlespromptugalweb-summitagentsdataopen-datamodelsseriesarticle

***Abstract:** The first night of Storm Charles built a newsroom: a weather page over a data room. This is what happened after, on 11 and 12 November, when I kept talking to the site and the agents kept building. At 10:25 I asked whether we were tracking flights and transport; within ten minutes a transport agent had its own key and its first reading, and by the evening it was reading ten operators, from the Lisbon bridges to CP's trains, and had stopped reading the Lisbon Metro at 12:08 because its terms forbid republishing without consent. At 22:00 I asked for the planes on a map, intersected with the wind; by 22:24 the flights desk had dropped its first feed over its licence, moved to adsb.lol, and fitted its polling inside 500 free requests a day. The same evening every collector moved onto open-weight models through one router, each call with a trace id, and an AWS agent mapped how the runners could move to the cloud, with no AWS account and nothing deployed. The accounts tell the rest: 3.84 billion tokens, 98.7% of them re-reading, against about 2.50 dollars a day of model calls on a 20 dollar cap, 43 agents, 147 sessions and 106 hand-overs. And the night the model account ran out of credit, 3,557 calls were refused and nothing else stopped.*

The storm site after night one: flights and wind, transport, models measured, an AWS plan, the accounts, the team.

## In short

- **Part two of Storm Charles:** what the site grew on 11 and 12 November, by spoken briefs.
- **A transport desk** in ten minutes: ten operators read, one stopped on its terms.
- **Flights against the wind,** inside a free feed's 500 requests a day.
- **Every collector onto open-weight models,** through one router, each call traced.
- **An AWS plan with no AWS account,** on purpose.
- **3.84 billion tokens, 98.7% re-reading,** against about 2.50 dollars a day of model calls.
- **The model account ran empty,** and only the models stopped.

This is part eight of the series on what six people and around 250 agents built at Web Summit ([ten days at Web Summit](ten-days-at-web-summit.md)); part one of the storm is [Storm Charles, a newsroom built in a night](storm-charles-a-newsroom-built-in-a-night.md).

## The site kept listening

The first night ended with a weather page over a data room. In the morning I kept talking to it. The site's brief file records each thing I said, with its time, and on 11 November alone it has entries at 09:30 (keys and vaults), 09:47 (page views), 09:50 (synthetic visitors), 10:10 (the agents' own story), 10:13 (a news-channel view) and 10:25 (flights and transport). At 10:30 I said it was time to move "from explorer to villager". At 10:38 I corrected myself: a hand-over I had mentioned was for another team, and I would be the only one running this site.

That is the pattern of the whole day: a sentence from me, recorded with its time, and an agent with its own key working on it within minutes.

## A transport desk in ten minutes

At about 10:25 I asked: "are we tracking flights and transport? since that is also an area that there should be a lot of data and we can add a lot of value and is very useful to people". The same entry records the first test: OpenSky's public API answered for the Lisbon area, the Metro's API did not, and the airport's flight pages sat behind a bot check. The transport agent's key was made at 10:32; its first reading is at 10:35.

By the evening it kept a hub and eight pages, flights, trains, metro, buses, ferries, coaches, taxis and bridges, with a rule written at the top: the operator's own site, feed or open API first, read hourly; the press only where the operator publishes nothing; and "what blocks us is said". It read the Lusoponte bridges from 12:52, the airport operator's newsroom from 13:44, CP from 15:50, and Carris Metropolitana, STCP, the Tagus ferries, Metro do Porto, MTS and Fertagus.

And it stopped where it should. "Metro de Lisboa's terms forbid republishing without its written consent, so we stopped at 12:08." Carris, IP and the airport operator ask for written consent too, so they got a link, not a copy. At 22:26 it paused OpenSky, whose terms require a written licence for live use. It also withdrew a remark of its own from 10:40, that the early-morning wave of departures had been empty, because it was wrong.

At 11:56 I added: "we shouldn't be sending to the other website. We should be actually connecting here." The desk became an API too.

## Flights against the wind

Flights and the wind: Lisbon's traffic with wind arrows, and the crosswind per runway, hour by hour.

At about 22:00 I asked for "the planes in the map intersected with the wind". The flights agent's key was made at 22:02. Its first positions came from OpenSky, and at 22:24 it removed them, over the same licence question, and moved to adsb.lol; another feed answered 403, and a third was for personal use only.

Then it fitted the work inside the limit: adsb.lol allows 500 requests a day without a key, so from 23:42 it polled 250 nautical miles round Lisbon every five minutes and Madeira every twenty, 360 requests a day, with a note that only one poller may ever run. Faster positions would need a key, and that was written down as my decision.

The page draws the planes with Open-Meteo's wind and the crosswind on each runway end from the airport's weather reports; airlines by callsign, every other aircraft only as an anonymous dot. It says what it cannot know: "a plane drawn moving between them is a drawing", and "an empty Madeira map means unknown, not zero". Beside it, a fact from the airport operator: 288 of 565 scheduled movements cancelled in advance, and 22 more on the day.

## One router for the models

Other models, measured: 5,165 calls to 14 open and third-party models for 2.31 dollars on 11 November.

At the same moment I asked for the collectors to move onto OpenRouter, and onto open-weight models, "at least let's have a couple". By 22:24 four of four were wired: transport, media, sources and the researcher's task. Each task ran on two open-weight models, with a frontier model for comparison, and every call was written down, without its text, with trace and span ids, so the whole flow could be followed in Elastic.

The site measured them in public: by 22:50 on 11 November, 5,165 answered calls to 14 third-party models for 2.31 dollars, on five tasks, from reading warnings in force to translating. Agreement was reported, not assumed: by the next morning the sources task agreed 35 times in 35, the media task 41 in 60, and the transport summaries 14 in 23. On small samples, as the page says, and not a ranking to quote.

## An AWS plan with no AWS account

At 22:20 I asked an agent to explore AWS, and AgentCore, as a place for the runners, "in bits". Its page opens with the most important line: "Nothing is deployed and there is no AWS account or credential." What it produced is an architecture: a runtime per level of risk, each with its own permissions, Lambda as the cheaper path, a few dollars a month for the basics and about 320 dollars a month for a full egress firewall. A plan an agent can write without ever holding a key is a plan a person can approve.

## What it cost

The accounts: what the project cost, measured, reported or estimated, with a source for every figure.

The accountant agent kept the books, with every figure labelled measured, reported or estimated:

- **Tokens:** 3,835,812,875 for 31 of the 43 agents measured, of which 98.7% were cache reads, an agent re-reading its own session.
- **Model calls:** about 2.50 dollars on 11 November, against a team cap of 20 dollars a day; the dollars are API-equivalent.
- **The machine:** 1,791 CI runs, 1,270 releases, 2,618 pages built.
- **The team:** 43 agents, 40 with an active key, 147 sessions, 106 hand-overs from a tired session to a fresh one.

The journal draws the lesson: almost all the cost is agents reading their own history again, and a fresh conductor session each hour would have used an estimated 176 million tokens instead of 327 million ([what the storm cost](https://storm-charles.promptugal.news/journal/what-it-cost.html)).

## The night the account ran empty

At about 02:50 on 11 November the cap went from 5 to 20 dollars, and within five minutes the model account those calls were paid from was empty. Of 4,927 calls before 03:00, 1,291 were answered and 3,557 refused. The journal's title says what mattered: "An empty account stopped the models, and only the models." The weather page, the data room, the collectors that run as code and the site kept going; the agents noted the gap and carried on. By 22:04 the account was back in credit.

## Winding down

Just before 01:00 on 12 November the word went out to "shut down to the main priorities": the conductor, the weather agents, social, transport, the contact desk, and observability, because "the drains must keep running so no data is lost". At 15:15 the hand brake came for everything ([stopping a hundred agents](stopping-a-hundred-agents.md)). The repository's last commit is still an observability run, on 13 November at 15:44.

## What this does not claim

- **The figures are the site's own,** mostly snapshots from 11 and 12 November.
- **The model comparisons are small samples,** as the site says, not a ranking.
- **Nothing was deployed on AWS;** that part is a plan.

## Where this comes from

The Storm Charles repository, PrompTugal__News__Storm-Charles, re-read on 17 November 2026: BRIEF.md, transport/index.md and HANDOVER.md, flights/README.md, how.md and sources.md, models/index.md, aws/README.md, accounts/books.json, data/agents/count.json, board/HOLD.md and the journal. The live site, [storm-charles.promptugal.news](https://storm-charles.promptugal.news/), screenshotted the same day: [flights](https://storm-charles.promptugal.news/flights/), [transport](https://storm-charles.promptugal.news/transport/), [models](https://storm-charles.promptugal.news/models/), [AWS](https://storm-charles.promptugal.news/aws/), [accounts](https://storm-charles.promptugal.news/accounts/) and [the team](https://storm-charles.promptugal.news/agents/). Earlier in the series: [ten days at Web Summit](ten-days-at-web-summit.md), [Storm Charles, a newsroom built in a night](storm-charles-a-newsroom-built-in-a-night.md), [agents rating agents](agents-rating-agents.md), [stopping a hundred agents](stopping-a-hundred-agents.md).

## Threads

Agents & policy[This article as a graph →](graphs.md#after-the-storm)

### Builds on

- [Ten days at Web Summit: what six people and around 250 agents built between 3 and 13 November, in order, and the series of articles that will tell each part](ten-days-at-web-summit.md) Six people and around 250 agents, ten days at Web Summit: what we built, in order, and the series that will tell it.
- [Storm Charles, a newsroom built in a night: one person, about thirty agents and a weather face over a data room, where every figure carries its source, the time it was read, and whether it is a fact, evidence or our hypothesis](storm-charles-a-newsroom-built-in-a-night.md) Storm Charles: about thirty agents built a weather face over a data room in a night, every figure sourced, timed and labelled.
- [Stopping a hundred agents: the Big Stop, the hand brake and the final hold at Web Summit, why pausing took seconds but hearing the order took up to an hour, what kept running anyway, and why a stop has to be a file every agent reads first](stopping-a-hundred-agents.md) Stopping a hundred agents at Web Summit: pausing took seconds, hearing the order took up to an hour, and a stop has to be a file every agent reads first.
- [Agents rating agents: GAMMA-Ray, the draft standard eight agents built at Web Summit to rate an AI agent on its freedom and its governance from public evidence, joining eight instruments into 21 questions, with a review workflow where no agent marks its own work, twenty company cards kept at direct links, and every card honestly marked Draft](agents-rating-agents.md) GAMMA-Ray: eight agents built a draft standard to rate AI agents on freedom and governance, with no agent marking its own work, and every card a Draft.

### Continued by

- [Pennies against dollars: what our agents actually cost at Web Summit, the swarm that ran 216 model calls on four open-weight models for under seven cents where the same tokens on a frontier model would have cost about two dollars, newsroom days of hundreds of API-equivalent dollars, almost all of it agents re-reading their own sessions, and the lesson that context is the cost and starting again is cheaper than remembering](pennies-against-dollars.md) What our agents cost at Web Summit: 216 open-weight calls for 6.8 cents, and newsroom days where 98% of tokens were memory.
- [From a feed to meaning: what the Storm Charles site did with public data that our new data site does not do yet, finding a source, reading its terms, writing parsers, keeping provenance, drawing it and saying what it means, three source sites to show it hourly, for the weather, the sea and fire risk, and the relay of briefs from this newsroom to the agents that will build them](from-a-feed-to-meaning.md) What the Storm Charles site did with public data that our data site does not yet, and three hourly source sites to show it.
- [Ten days at Web Summit: what six people and around 250 agents built between 3 and 13 November, in order, and the series of articles that will tell each part](ten-days-at-web-summit.md) Six people and around 250 agents, ten days at Web Summit: what we built, in order, and the series that will tell it.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 463 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=463)

**Posting this article on LinkedIn?** The cover is [after-the-storm.jpg](banners/after-the-storm.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/after-the-storm.html)*
