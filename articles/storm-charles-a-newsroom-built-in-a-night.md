# Storm Charles, a newsroom built in a night: one person, about thirty agents and a weather face over a data room, where every figure carries its source, the time it was read, and whether it is a fact, evidence or our hypothesis, sgit.ai

> When Storm Charles reached Lisbon during Web Summit, and the government's advice led Web Summit to call off its second day, I asked our agents for a new site about it, by voice, at about 21:00 UTC on 10 November. By morning storm-charles.promptugal.news had about 2,000 pages, built by about thirty Claude Code agents, each push live in about forty seconds. It has two faces. In front, a weather page anyone can read: what IPMA warns now, hour by hour, never a forecast of our own. Behind it, a data room: 34 JSON datasets in a catalogue with their hashes, a timeline with permanent row ids, every decision and who made it, every thing mentioned as a node in a graph, and every outside page captured and hashed in a vault. Every line is labelled fact, evidence or hypothesis. On top of the data there are labs that show the same storm a dozen ways (lead times from warning to decision, a replay of what was known when, warned against observed station by station), a graph you query with a question, SQLite running in your browser, other models measured as evals, animated explanations, and a journal that tells how the site was made, including its mistakes and what it cost. It is part of PrompTugal.news, our independent newsroom at Web Summit, and it shows what a newsroom run by agents, steered by a person, can already do.

*Source: <https://newsroom.sgit.ai/articles/storm-charles-a-newsroom-built-in-a-night.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Storm Charles, a newsroom built in a night: one person, about thirty agents and a weather face over a data room, where every figure carries its source, the time it was read, and whether it is a fact, evidence or our hypothesis

# Storm Charles, a newsroom built in a night: one person, about thirty agents and a weather face over a data room, where every figure carries its source, the time it was read, and whether it is a fact, evidence or our hypothesis

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-11 · [article v1.1.0, 2 versions](versions/storm-charles-a-newsroom-built-in-a-night.md) · [newsroom v0.14.75](https://newsroom.sgit.ai/admin/versions.html) · storm-charlespromptugalweb-summitagentsdataprovenancegraphsnewsroomjournalismarticle

***Abstract:** When Storm Charles reached Lisbon during Web Summit, and the government's advice led Web Summit to call off its second day, I asked our agents for a new site about it, by voice, at about 21:00 UTC on 10 November. By morning storm-charles.promptugal.news had about 2,000 pages, built by about thirty Claude Code agents, each push live in about forty seconds. It has two faces. In front, a weather page anyone can read: what IPMA warns now, hour by hour, never a forecast of our own. Behind it, a data room: 34 JSON datasets in a catalogue with their hashes, a timeline with permanent row ids, every decision and who made it, every thing mentioned as a node in a graph, and every outside page captured and hashed in a vault. Every line is labelled fact, evidence or hypothesis. On top of the data there are labs that show the same storm a dozen ways (lead times from warning to decision, a replay of what was known when, warned against observed station by station), a graph you query with a question, SQLite running in your browser, other models measured as evals, animated explanations, and a journal that tells how the site was made, including its mistakes and what it cost. It is part of PrompTugal.news, our independent newsroom at Web Summit, and it shows what a newsroom run by agents, steered by a person, can already do.*

Twelve of the site's data-driven pages, each drawn from its own published JSON, on 11 November.

## In short

- **A storm, a summit and a site.** Storm Charles hit Lisbon during Web Summit; on the government's advice Web Summit called off its second day. That evening I asked our agents for a site about it.
- **Built in a night:** about 2,000 pages by morning, about thirty agents, each push live in about forty seconds.
- **Two faces:** a weather page anyone can read in front, and a data room behind it where every figure has a source, a time and a label.
- **Data-driven all the way down:** 34 datasets with hashes, a timeline with permanent ids, a graph of 496 things and 705 links, SQLite in your browser, an API for agents.
- **Many ways to see one storm:** labs for lead times, replays, lanes and stations; stories checked against the data on every build; animated explanations.
- **It tells on itself:** a journal of how it was made, what went wrong, what waited on me, and what it cost.
- **Not a warning service.** It says so on every page: follow IPMA, ANEPC and your local authorities.

## The size of it

Storm Charles in numbers at 10:18 UTC on 11 November, about thirteen hours after its first commit.

Thirteen hours after the first commit, at 10:18 UTC on 11 November, the site's own pages counted:

| What | How many |
|---|---|
| Pages on the site | 2,097 |
| Agents | 35, 30 with an active key, 71 sessions |
| Versions tagged | 517, from 744 pipeline runs |
| Push to served | 36 seconds median, 90% within 51 |
| JSON datasets | 34, each with size and sha256 |
| Graph | 496 things, 705 links |
| Entities | 215 nodes, 435 edges |
| Board cards | 444 jobs, asks, questions and conflicts |
| Model calls as evals | 1,291, 14 models, under one dollar |
| Tokens in agent sessions | 2,069 million, 98.7% re-reading |

The largest section is the evidence, 585 pages of captured outside pages, then the board with 447 and the entities with 230. The pipeline had failed 6 of its 744 runs; 203 were replaced by a newer push before they finished, which is what a busy team pushing small changes looks like.

## What happened

Storm Charles was named by IPMA, Portugal's weather service, on 9 November. On 10 November IPMA issued a red wind warning for the Lisbon district for the next day, the government declared an alert situation for mainland Portugal, IPMA raised rain to red, and at 17:53 UTC the Prime Minister recommended suspending Web Summit on Wednesday. At 19:09 UTC Web Summit published its decision: Day 2 would not take place, and Day 3 "aims to proceed as planned".

Each of those lines is on the site with the source it was read from and the time it was read. That is the point of it.

## How it started

The incident was first kept on another of the team's sites. At about 21:00 UTC I named a repository and a domain and said, in a voice memo, what I wanted: a separate repository that pushes "super fast", with its speed measured; "a data source for a lot of agencies and a lot of people about what is actually going on"; two things at once, a news site that should "look like CNN" and a site for agents with raw datasets and an API; everything a signal; and agents that run "until the storm is over".

The conductor's first commit, at 21:14:33, was the whole first site. Then I came back six more times before 03:00, each time after looking at what was live: more agents and visibility into every one at 23:40; a Studio for animated explanations at 00:30; a Wikipedia agent at 01:28; at 02:10, two faces, every word linked, every outside page captured, a section per source; at 02:50, a model budget, an accountant, a reporter and a journalist on the project itself. All of it is in [the brief](https://storm-charles.promptugal.news/BRIEF.html), close to my words.

Commits per hour through the night, and when I gave direction, from the site's own journal.

The site's journal counts it: one agent until 23:35, eight by midnight, twenty-two by 02:36, and 193 commits in the hour I asked for two faces. By 02:36 there had been 318 commits and 187 tagged versions, and the gate built 1,078 pages in 2.9 seconds.

## Two faces over one data room

The weather face, the labs and the API all read from one data room, where every value has a source, a time and a label.

**The weather face** is the home page. It is meant to read like a weather channel, for anyone: the red warning in force in Lisbon now, what is also in force, IPMA's communiqué, and today hour by hour, with the government's and the schools' decisions in the same strip. It makes no forecast and gives no advice of its own.

**The data room** is everything behind it, and the front reads only from it. It holds:

- **A catalogue of 34 datasets,** each with its size and sha256: IPMA's warnings and their changes, its forecasts and stations, MeteoAlarm's alert messages, the decisions of the airport, the bridges, the Metro, the ferries, schools, hospitals and Web Summit, and the public signals.
- **A timeline** with a permanent id for every row, and **a decisions log** where each decision is written down before anyone acts.
- **Entities:** every thing a page mentions is a node with an address, 215 nodes and 435 edges when I read it.
- **Evidence:** every outside page the agents read is captured as it was served, hashed, and kept in an encrypted vault, then shown on our own page of it, decrypted in your browser, with a check that it matches the hash on record.

And three labels, everywhere. **Fact:** read from the body that decides or warns, on its own channel. **Evidence:** reported by someone else, and it names who. **Hypothesis:** our analysis, with its reasons, "never a fact". A reader's panel colours any page by those labels, so you can see what a page is made of.

## Many ways to see one storm

The Labs are the part I enjoy most: small experiments, each on its own page, each reading only the site's published JSON, and each saying what it shows badly. Clicking any mark opens the row behind it, with its source and the time it was read.

- **Lead times:** for every decision, how long after the warning it came, and how long before its effect. Shortest notice first.
- **What was known when:** a replay. Press play and IPMA's warnings for Lisbon change as they did, with the decisions appearing at the minute they were made.
- **Who spoke when, in lanes:** bodies that warn and decide, carriers of official data, Web Summit, the press, our team, and our analysis, each on its own line.
- **Warned against observed:** each IPMA station's rain and wind against the warning in force for its district.
- **What followed from a warning:** pick a warning and see the decisions that came after it, step by step.

Beside them: **stories**, where every sentence carries its label and the timeline rows it rests on, and is checked against the data room on every build; **the graph**, where you start from a question ("who decided what, on whose warning?") and what you see is its answer; **an ontology** of eight kinds of thing and nine verbs, each with its inverse, with no generic "related to" edge; and **a query page** that starts SQLite in your browser over the graph's tables, ten tables and about two thousand rows, with nothing uploaded. It follows [fractal semantic graphs](introducing-fractal-semantic-graphs.md): any node opens into its own graph, down to the last source.

## The team, the evidence and the record

The team, the board, the accounts, a captured page, meteorology, stories, the journal, the design and the labels.

The site shows its own machinery as plainly as the storm:

- **The team page** counts the last hour: 67 pushes, 55 deployed, a median of 40 seconds from push to served, 31 agents, and a list of what I can unblock, most blocking first.
- **The board** has every job, ask, question and conflict, by agent, with the ones waiting on me counted.
- **Meteorology** maps the whole field in five layers: what observes the atmosphere, the models, the open data, the warning services, and the sites people read, with 106 weather sites researched.
- **Research** follows the media, Bluesky and Wikipedia in several languages, with each Wikipedia page captured as it stood.
- **Models:** third-party and open-weight models are called through one wrapper as measured evals, 1,291 answered calls and 14 models on 11 November, every call costed, against a cap of 20 dollars a day.
- **The Studio** explains with small animated characters: what compression is, in seven chapters and forty scenes; how a fact gets onto the site; one warning, opened three times.
- **The design** has gone through dozens of rounds, each kept on the site, with one stylesheet and five themes.

## It tells on itself

The journal is written by one of the agents for "someone arriving cold: a journalist, an editor, an engineer, an investor". Its argument is the one I would make: "One person, speaking, was enough to steer about thirty agents through a night, because three things were fixed before the crowd arrived: every agent owns its own folders, every push is small and goes through one gate, and a push is on the live site in about half a minute." And it says what that did not fix: "the person". By 02:55, thirty-six cards on the board were waiting on me.

It corrects itself in public: an early count of what waited on me was wrong, because every agent's address ends in ".dinis", and the page says so at the top. And [what it cost](https://storm-charles.promptugal.news/journal/what-it-cost.html) is the plainest account of agent economics I have read: about one dollar in third-party model calls by 03:00, an empty provider account that stopped every call five minutes after I raised the cap, and 2,069 million tokens in the agents' own sessions, 98.7% of them an agent reading its own session again. "What an agent costs is set less by what it writes than by how long it has been remembering."

## Part of PrompTugal.news

Storm Charles is a section of [PrompTugal.news](https://promptugal.news/), the independent newsroom we are running at Web Summit Lisbon: what is on now and next, the news, the companies and the people, every fact sourced. When the storm turned into the summit's main story, it needed its own site, its own repository and its own agents, and it got them in an evening. The same team keeps both, and the same rules hold: sources on everything, labels on everything, and a person who sends every message that leaves the repositories.

It also builds on what we have worked out here: a behaviour policy for every agent, vaults for evidence, and the graph thinking from this newsroom.

## What this does not claim

- **It is not a warning service,** and neither is this article. For warnings, follow IPMA, ANEPC and your local authorities.
- **The figures are the site's own,** as its pages and journal stated them when I read them on the morning of 11 November; they move by the minute.
- **The site is a night old,** and says what does not exist yet: among other things, no agent signs with its own key, and I had no key of my own on the site.
- **The people on the Web Summit team are not named here.**

## Where this comes from

[storm-charles.promptugal.news](https://storm-charles.promptugal.news/), read on 11 November 2026 between 09:30 and 10:00 UTC: the home page, [the brief](https://storm-charles.promptugal.news/BRIEF.html), the data room's dashboard, timeline, decisions, graph, ontology, query and entities, the labs, stories, research, models, studio, team, board, accounts, design and help pages, the journal's [a storm, one person, one night](https://storm-charles.promptugal.news/journal/a-storm-one-person-one-night.html) and [what it cost](https://storm-charles.promptugal.news/journal/what-it-cost.html), [the data catalogue](https://storm-charles.promptugal.news/api/v1/index.json) and [llms.txt](https://storm-charles.promptugal.news/llms.txt). [PrompTugal.news](https://promptugal.news/). Web Summit's [event update](https://websummit.com/blog/web-summit/important-event-update-2026/), as the site records it. Earlier on this site: [introducing fractal semantic graphs](introducing-fractal-semantic-graphs.md), [the Web Summit team, part five](web-summit-part-five.md), [who else controls AI agents at Web Summit](who-else-controls-ai-agents-at-web-summit.md).

## Threads

News & evidenceAgents & policy[This article as a graph →](graphs.md#storm-charles-a-newsroom-built-in-a-night)

### Builds on

- [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](introducing-fractal-semantic-graphs.md) A fractal semantic graph has no privileged level and no single schema: each world keeps its own vocabulary and connects to others through named edges.
- [The Web Summit team, part five: the last day of setup, 180 releases, every person getting a key, an accountant counting the team's tokens, synthetic users testing the merch, and an inbox only the agents can write to](web-summit-part-five.md) The Web Summit team's last day of setup: 180 releases, keys for every person, new agents for everyone, and an inbox per agent.
- [Who else controls AI agents at Web Summit? An outreach agent mapped eleven companies in an afternoon, in their own words, and found that most of them are partners for RiskMandate as much as competitors](who-else-controls-ai-agents-at-web-summit.md) An outreach agent mapped eleven companies that control AI agents at Web Summit; most are partners for RiskMandate as much as competitors.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 392 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=392)

**Posting this article on LinkedIn?** The cover is [storm-charles-a-newsroom-built-in-a-night.jpg](banners/storm-charles-a-newsroom-built-in-a-night.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/storm-charles-a-newsroom-built-in-a-night.html)*
