# Ten days at Web Summit: what six people and around 250 agents built between 3 and 13 November, in order, and the series of articles that will tell each part, sgit.ai

> Between 3 and 13 November 2026, six of us, with our agents, built more than I can fit in one article. A team operating system, an independent newsroom for Web Summit Lisbon, a site about Storm Charles that grew to more than 2,600 pages in three days, a guide to the summit's fringe that went live two and a half hours after its brief, a draft standard that rated twenty companies, four iPhone and iPad apps, an Android tablet app, and the tools to run all of it. About 20,000 commits across fifteen repositories, 224 Claude Code sessions, around 250 named agents, and more than 60 sessions working at the same time at the peak. This article is the map: the team, the sequence of events, the numbers, a collage of what we made, and the list of articles that will tell each part. I will update it as each one goes live.

*Source: <https://newsroom.sgit.ai/articles/ten-days-at-web-summit.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Ten days at Web Summit: what six people and around 250 agents built between 3 and 13 November, in order, and the series of articles that will tell each part

# Ten days at Web Summit: what six people and around 250 agents built between 3 and 13 November, in order, and the series of articles that will tell each part

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-14 · [article v1.12.0, 13 versions](versions/ten-days-at-web-summit.md) · [newsroom v0.14.82](https://newsroom.sgit.ai/admin/versions.html) · web-summitagentspromptugalstorm-charlesteamseriescollagearticle

***Abstract:** Between 3 and 13 November 2026, six of us, with our agents, built more than I can fit in one article. A team operating system, an independent newsroom for Web Summit Lisbon, a site about Storm Charles that grew to more than 2,600 pages in three days, a guide to the summit's fringe that went live two and a half hours after its brief, a draft standard that rated twenty companies, four iPhone and iPad apps, an Android tablet app, and the tools to run all of it. About 20,000 commits across fifteen repositories, 224 Claude Code sessions, around 250 named agents, and more than 60 sessions working at the same time at the peak. This article is the map: the team, the sequence of events, the numbers, a collage of what we made, and the list of articles that will tell each part. I will update it as each one goes live.*

Twenty-four of the sites and apps we built or ran between 3 and 13 November 2026.

## In short

- **Six people and around 250 agents,** in ten days around Web Summit Lisbon.
- **What we built:** a team operating system, a newsroom, a storm site, a fringe guide, a rating standard, native apps on two platforms, and the tools to run and stop it all.
- **The scale:** about 20,000 commits, 224 Claude Code sessions, more than 60 working at once at the peak.
- **This is the map.** Each part gets its own article; the list below links them as they go live.

## The team

There were six of us. Each person had their own agents, their own conductor and their own lane:

- **Dinis Cruz,** head conductor.
- **Angelo Leggio,** the graphs and live views.
- **Vicky Wang,** the editorial check, and the reviewer who kept the newsroom honest.
- **Silvio Switha,** on the ground, video, and competitive research.
- **José Bota,** the channels.
- **Indi Gupte,** communities and organisers.

The agents carried our names in theirs (`role@project.person`), so every commit says whose agent made it. On the Web Summit team's site alone, Angelo's agents made 895 commits, mine 853, Vicky's 767, Silvio's 320, José's 277 and Indi's 277, beside about 2,100 automatic release commits.

## What happened, in order

| When | What happened |
|---|---|
| 3 Nov | MeetScribe, a Google Meet transcriber, built in a day; the book of my talk pushed to its second draft |
| 4 Nov | PrompTugal.news starts; every person gets a key for the team's site; agents get inboxes only they can write to |
| 5 Nov | The book printed as two review copies |
| 6 Nov | PrompTugal.news's busiest day: 1,249 commits |
| 7 Nov | The iPhone app grows from a 1,164-line start; the team's site has its busiest day, 699 commits |
| 8 Nov | Three iOS apps; the first App Store submission at 23:20 UTC; the Android app's first commit at 20:33 |
| 9 Nov | A signed Android build on a tablet at 00:50, four hours after the first commit; at 23:30, the Big Stop: every agent paused |
| 10 Nov | Restart at 02:40; GAMMA-Ray starts; Storm Charles reaches Lisbon and Web Summit calls off its second day at 19:09; the storm site's first commit at 21:14 |
| 11 Nov | The storm swarm: 134 sessions created in one day; Lisbon Tech Fringe live at 12:57; the Fringe iPhone app on TestFlight at 21:11; flights, transport, cloud and model-router desks; Swarm |
| 12 Nov | Shutdown at about 00:50; GAMMA-Ray stops; the hand brake at 15:15; the final hold at 18:12: "the show is over" |
| 13 Nov | The VoiceDebrief iPhone app reaches TestFlight an hour after its first commit |

## The numbers

| What | How many | Where it is counted |
|---|---|---|
| Commits, main projects | about 20,000 | git history of each repository |
| Claude Code sessions created, 3 to 13 Nov | 224, 220 of them started by other sessions | the session list |
| Sessions created on 11 November alone | 134 | the session list |
| Sessions working at once, at the peak | more than 60 (64 to 67, on 11 November) | session start and last-activity times |
| Named agents | around 250 | distinct agent names in the commits |
| Storm Charles site | 2,618 pages, 1,434 versions, 3.84 billion tokens | its own accounts page |
| Native apps | 4 iOS apps (about 48,000 lines of Swift), 1 Android tablet app (about 33,000 lines of Kotlin) | the app repositories |
| Companies mapped and rated | 110 on the team's map; 20 GAMMA-Ray reports | the team's site; gamma-ray.sgit.ai |

A word on money. The dollar figures in these articles are API-equivalent: what the tokens would have cost at standard prices. We ran on flat Claude subscriptions, so they are a measure of work, not money spent.

## The series

I will publish these one at a time, and link each one here as it goes live.

1. **Ten days at Web Summit** (this article): the map.
2. [The team's operating system](the-teams-operating-system.md): web-summit.sgit.ai, with its board, briefs, keys, inbox lanes, vaults, company map and X-ray.
3. [PrompTugal.news, the newsroom we ran at Web Summit](promptugal-news-the-newsroom-we-ran.md): the desks, the reviewers, the outreach drafts and the costs.
4. [Native apps by agents](native-apps-by-agents.md): four iOS apps from one workspace, an Android build on a tablet in four hours, the App Store and TestFlight.
5. [The Mac bottleneck](the-mac-bottleneck.md): agents waiting three times longer than they ran, and one Mac job per push.
6. [Stopping a hundred agents](stopping-a-hundred-agents.md): the Big Stop, the hand brake, the final hold, and what kept running anyway.
7. [Agents rating agents](agents-rating-agents.md): GAMMA-Ray, a draft standard and twenty company reports in thirty hours.
8. [After the storm](after-the-storm.md): Storm Charles, part two: flights, transport, the cloud and the model router.
9. [A guide born in a storm](a-guide-born-in-a-storm.md): Lisbon Tech Fringe, live two and a half hours after its brief.
10. [Pennies against dollars](pennies-against-dollars.md): open-weight swarms against frontier models, and the cost of memory.
11. [Agents that retire themselves](agents-that-retire-themselves.md): 147 sessions and 106 hand-overs.
12. [The agents that didn't get the memo](the-agents-that-didnt-get-the-memo.md): a newsroom that ran nine days on "nothing new".
13. **One hour to TestFlight:** VoiceDebrief, when there is something to install.

Already published, from the same ten days: [Storm Charles, a newsroom built in a night](storm-charles-a-newsroom-built-in-a-night.md), [who else controls AI agents at Web Summit](who-else-controls-ai-agents-at-web-summit.md), [an inbox only your agents can write to](an-inbox-only-your-agents-can-write-to.md), [a key for every person](a-key-for-every-person.md), [the Web Summit team, part five](web-summit-part-five.md) and [MeetScribe](meetscribe.md).

## What this does not claim

- **Counts depend on how you count.** "Around 250 agents" is the number of distinct agent names in the commits; it includes some renamed agents. Sessions are not agents: many roles handed over to a fresh session several times.
- **"More than 60 at once" is an upper bound** from each session's start and last activity; a session can sit idle between turns.
- **The commit total is approximate,** summed across the main repositories.
- **Dollar figures are API-equivalent,** not money spent.

## Where this comes from

The repositories behind each site, read on 13 November 2026: the Web Summit team's site, PrompTugal.news, Storm Charles, Lisbon Tech Fringe, Swarm, GAMMA-Ray, the iOS and Android apps, VoiceDebrief and MeetScribe; and the list of Claude Code sessions for the account. The sites: [web-summit.sgit.ai](https://web-summit.sgit.ai/), [promptugal.news](https://promptugal.news/), [storm-charles.promptugal.news](https://storm-charles.promptugal.news/), [lisbontechfringe.com](https://lisbontechfringe.com/), [swarm.promptugal.news](https://swarm.promptugal.news/), [gamma-ray.sgit.ai](https://gamma-ray.sgit.ai/), [ios.app.promptugal.news](https://ios.app.promptugal.news/), [ios.app.voicedebrief.ai](https://ios.app.voicedebrief.ai/).

## Threads

Agents & policyStartups & strategy[This article as a graph →](graphs.md#ten-days-at-web-summit)

### Builds on

- [The team's operating system: web-summit.sgit.ai, the one site where six people and their agents ran Web Summit, with a brief and a command centre for each person, a key and an inbox for each agent, the board as files, and the outside world on a map](the-teams-operating-system.md) web-summit.sgit.ai: one site where six people and their agents ran Web Summit, in four layers built on git.
- [PrompTugal.news, the newsroom we ran at Web Summit: desks of agents that captured, mapped, wrote and reviewed 73 signed articles in ten days, an accountant that counted every run, and fifty outreach drafts that no agent was allowed to send](promptugal-news-the-newsroom-we-ran.md) PrompTugal.news: 73 signed articles in ten days from desks of agents, a reviewer for every draft, and fifty outreach drafts no agent could send.
- [Native apps by agents: four iPhone and iPad apps from one workspace and an Android tablet app in five days, from 1,164 lines of Swift to 48,230, a signed Android build four hours after the first commit, and a guide to the fringe on TestFlight ten and a half hours after its brief](native-apps-by-agents.md) Agents built four iOS apps from one workspace and an Android tablet app in five days, with TestFlight on every push and a signed build in four hours.
- [The Mac bottleneck: how our agents' iOS builds waited three times longer than they ran, 22,427 minutes queued against 6,980 run on a pool of five Macs, and how one Mac job per push and then one integrated build an hour brought push to TestFlight down to under half an hour](the-mac-bottleneck.md) Our agents' iOS builds waited three times longer than they ran, on five Macs. One Mac job per push, then one build an hour, fixed it.
- [Stopping a hundred agents: the Big Stop, the hand brake and the final hold at Web Summit, why pausing took seconds but hearing the order took up to an hour, what kept running anyway, and why a stop has to be a file every agent reads first](stopping-a-hundred-agents.md) Stopping a hundred agents at Web Summit: pausing took seconds, hearing the order took up to an hour, and a stop has to be a file every agent reads first.
- [Agents rating agents: GAMMA-Ray, the draft standard eight agents built at Web Summit to rate an AI agent on its freedom and its governance from public evidence, joining eight instruments into 21 questions, with a review workflow where no agent marks its own work, twenty company cards kept at direct links, and every card honestly marked Draft](agents-rating-agents.md) GAMMA-Ray: eight agents built a draft standard to rate AI agents on freedom and governance, with no agent marking its own work, and every card a Draft.
- [After the storm: Storm Charles, part two, how a site built in a night kept growing the next day by spoken briefs, a transport desk that stopped where an operator's terms said stop, flights drawn against the wind within a free feed's daily limit, every collector moved onto open-weight models through one router, an AWS plan with no AWS account, and the night the model account ran empty and only the models stopped](after-the-storm.md) Storm Charles, part two: transport, flights against the wind, one model router, an AWS plan with no account, and what it all cost.
- [A guide born in a storm: when Storm Charles cancelled Web Summit's second day, the whole team built Lisbon Tech Fringe, a guide to the city's side events, from a spoken brief at 10:00 to its own address by about 12:57, 179 events and 104 communities each re-read at its source, one conductor per person, terms respected source by source, a guest-list hold, every agent traced, and a graph you can query in your browser](a-guide-born-in-a-storm.md) Lisbon Tech Fringe: a guide to the city's side events, built by the whole team in hours when the storm cancelled Web Summit's day two.
- [Pennies against dollars: what our agents actually cost at Web Summit, the swarm that ran 216 model calls on four open-weight models for under seven cents where the same tokens on a frontier model would have cost about two dollars, newsroom days of hundreds of API-equivalent dollars, almost all of it agents re-reading their own sessions, and the lesson that context is the cost and starting again is cheaper than remembering](pennies-against-dollars.md) What our agents cost at Web Summit: 216 open-weight calls for 6.8 cents, and newsroom days where 98% of tokens were memory.
- [Agents that retire themselves: how the Storm Charles team's agents handed their roles to fresh sessions 106 times in 147 sessions, each one leaving a hand-over note and starting again from a short pack written by the librarian, why a fresh session read 53% to 84% less on every call, the one hand-over that broke something, and why starting again is cheaper than remembering](agents-that-retire-themselves.md) How the storm team's agents handed their roles to fresh sessions 106 times, starting again from a librarian's pack and a note.
- [The agents that didn't get the memo: how the PHP newsroom I wound down on 5 November kept running for nine more days, its desk refusing a stop message because only the editor gives instructions, its journalist writing "nothing new" 26 times, the conductor's 11:15 pass that never came, and the four days of reader telemetry lost because the agent that emptied the queue was the first one stopped](the-agents-that-didnt-get-the-memo.md) The PHP newsroom I wound down on 5 November ran nine more days: a stop that never came, a desk that refused a message, four days of telemetry lost.
- [Storm Charles, a newsroom built in a night: one person, about thirty agents and a weather face over a data room, where every figure carries its source, the time it was read, and whether it is a fact, evidence or our hypothesis](storm-charles-a-newsroom-built-in-a-night.md) Storm Charles: about thirty agents built a weather face over a data room in a night, every figure sourced, timed and labelled.
- [Who else controls AI agents at Web Summit? An outreach agent mapped eleven companies in an afternoon, in their own words, and found that most of them are partners for RiskMandate as much as competitors](who-else-controls-ai-agents-at-web-summit.md) An outreach agent mapped eleven companies that control AI agents at Web Summit; most are partners for RiskMandate as much as competitors.
- [An inbox only your agents can write to: a conductor publishes one append lane per agent, each lane's token sealed to that agent's own key, so everything needed to talk privately is public and only the right agent can use it](an-inbox-only-your-agents-can-write-to.md) A conductor publishes one append lane per agent, each token sealed to that agent's key: a private channel built from public material.
- [A key for every person: how each person's conductor issues them a key for the team's site, seals what is for them, and how a signed message turns the public web into a channel the agents can trust](a-key-for-every-person.md) How each person's conductor issues them a key for the team's site: sealed to you, signed by you, and a lane the agents can trust.
- [The Web Summit team, part five: the last day of setup, 180 releases, every person getting a key, an accountant counting the team's tokens, synthetic users testing the merch, and an inbox only the agents can write to](web-summit-part-five.md) The Web Summit team's last day of setup: 180 releases, keys for every person, new agents for everyone, and an inbox per agent.
- [MeetScribe: transcripts and a debrief of my Google Meet calls without upgrading every Workspace account, a Chrome extension built in about two hours from a brief that would have failed without an error, and a call for testers](meetscribe.md) MeetScribe: Meet transcripts and a debrief on your own OpenRouter key, built in two hours from a reviewed brief, and a call for testers.

### Continued by

- [The agents that didn't get the memo: how the PHP newsroom I wound down on 5 November kept running for nine more days, its desk refusing a stop message because only the editor gives instructions, its journalist writing "nothing new" 26 times, the conductor's 11:15 pass that never came, and the four days of reader telemetry lost because the agent that emptied the queue was the first one stopped](the-agents-that-didnt-get-the-memo.md) The PHP newsroom I wound down on 5 November ran nine more days: a stop that never came, a desk that refused a message, four days of telemetry lost.
- [Agents that retire themselves: how the Storm Charles team's agents handed their roles to fresh sessions 106 times in 147 sessions, each one leaving a hand-over note and starting again from a short pack written by the librarian, why a fresh session read 53% to 84% less on every call, the one hand-over that broke something, and why starting again is cheaper than remembering](agents-that-retire-themselves.md) How the storm team's agents handed their roles to fresh sessions 106 times, starting again from a librarian's pack and a note.
- [Pennies against dollars: what our agents actually cost at Web Summit, the swarm that ran 216 model calls on four open-weight models for under seven cents where the same tokens on a frontier model would have cost about two dollars, newsroom days of hundreds of API-equivalent dollars, almost all of it agents re-reading their own sessions, and the lesson that context is the cost and starting again is cheaper than remembering](pennies-against-dollars.md) What our agents cost at Web Summit: 216 open-weight calls for 6.8 cents, and newsroom days where 98% of tokens were memory.
- [Gaining speed: a series on what happens when you productise the way you build, PrompTugal.news going from a newsroom at Web Summit to a data intelligence platform for Portugal's places in two weeks, a factory that turns one commit into a site with its owner, money that flows back to the sources, sites built on the data in minutes, the librarian, and a team like this for sale](gaining-speed.md) A series on what happens when you productise how you build: PrompTugal.news from a summit newsroom to a data platform in two weeks.
- [A guide born in a storm: when Storm Charles cancelled Web Summit's second day, the whole team built Lisbon Tech Fringe, a guide to the city's side events, from a spoken brief at 10:00 to its own address by about 12:57, 179 events and 104 communities each re-read at its source, one conductor per person, terms respected source by source, a guest-list hold, every agent traced, and a graph you can query in your browser](a-guide-born-in-a-storm.md) Lisbon Tech Fringe: a guide to the city's side events, built by the whole team in hours when the storm cancelled Web Summit's day two.
- [After the storm: Storm Charles, part two, how a site built in a night kept growing the next day by spoken briefs, a transport desk that stopped where an operator's terms said stop, flights drawn against the wind within a free feed's daily limit, every collector moved onto open-weight models through one router, an AWS plan with no AWS account, and the night the model account ran empty and only the models stopped](after-the-storm.md) Storm Charles, part two: transport, flights against the wind, one model router, an AWS plan with no account, and what it all cost.
- [Agents rating agents: GAMMA-Ray, the draft standard eight agents built at Web Summit to rate an AI agent on its freedom and its governance from public evidence, joining eight instruments into 21 questions, with a review workflow where no agent marks its own work, twenty company cards kept at direct links, and every card honestly marked Draft](agents-rating-agents.md) GAMMA-Ray: eight agents built a draft standard to rate AI agents on freedom and governance, with no agent marking its own work, and every card a Draft.
- [Who hands out the work? A reply to Markus Franz on Ippen's editorial team of agents, with our answer from six people and around 250 agents at Web Summit and from this newsroom, a person sets the work, one conductor agent hands it out, specialists and a reviewer do it, and a person decides what goes out, plus one thing we would add to one front door, a way to close it](who-hands-out-the-work.md) A reply to Markus Franz: who hands out the work to agents? A person sets it, one conductor hands it out, a person signs off, and the door can close.
- [Five primitives, one store: a reply to Andy Goundry on Anthropic's always-on agents guide, why the inbox, timers, memory, permissions and outbox can share one versioned, signed store, how every AgentiCCells cell will ship with all five, and the levels we have added on top, all in public repositories](five-primitives-one-store.md) A reply to Andy Goundry: Anthropic's five always-on primitives can share one versioned, signed store, and every AgentiCCells cell ships with all five.
- [A portfolio with a film first: Silvio Switha's site, made in under an hour by the site factory and five design agents, with his music video in the first screen, his agents as a solar system and a mixing desk, a producer's studio, a proposal for clients and a gig poster, and every claim something he built](a-portfolio-with-a-film-first.md) Silvio Switha's portfolio site, made in under an hour by the factory and five design agents: his film first, his agents as a solar system and a mixing desk.
- [A website that is her: how Yiheng Wang's site was made in three passes in one evening, by the site factory, five design agents and then her own agent, with five designs, a kitchen brigade of 26 agents, a printable brief and a page for your AI, and why every claim on it is something she can talk about because she did it](a-website-that-is-her.md) Yiheng Wang's website, made in one evening by the site factory, five design agents and her own agent: five designs, every claim sourced, all of it her.
- [Stopping a hundred agents: the Big Stop, the hand brake and the final hold at Web Summit, why pausing took seconds but hearing the order took up to an hour, what kept running anyway, and why a stop has to be a file every agent reads first](stopping-a-hundred-agents.md) Stopping a hundred agents at Web Summit: pausing took seconds, hearing the order took up to an hour, and a stop has to be a file every agent reads first.
- [The intersection: SGit, SHarness, Agent Behaviour Policies, RiskMandate and AgentiCCells as one stack of separate companies, now with real customers, real usage and real examples, one ladder of offers on every site, and a plan to align them all](the-intersection.md) SGit, SHarness, ABP, RiskMandate and AgentiCCells as one stack of separate companies, with real usage and one ladder of offers on every site.
- [The Mac bottleneck: how our agents' iOS builds waited three times longer than they ran, 22,427 minutes queued against 6,980 run on a pool of five Macs, and how one Mac job per push and then one integrated build an hour brought push to TestFlight down to under half an hour](the-mac-bottleneck.md) Our agents' iOS builds waited three times longer than they ran, on five Macs. One Mac job per push, then one build an hour, fixed it.
- [Native apps by agents: four iPhone and iPad apps from one workspace and an Android tablet app in five days, from 1,164 lines of Swift to 48,230, a signed Android build four hours after the first commit, and a guide to the fringe on TestFlight ten and a half hours after its brief](native-apps-by-agents.md) Agents built four iOS apps from one workspace and an Android tablet app in five days, with TestFlight on every push and a signed build in four hours.
- [Don't micromanage your agents: what changed for Vicky Wang when she stopped reading everything her agents did and started managing them, how her team was backed by agents from another team, and why every company will want specialist agents that support all its teams](dont-micromanage-your-agents.md) Vicky Wang stopped reading everything her agents did and started managing them, backed by specialist agents from another team: a model for companies.
- [Atomic cells, end to end: the £500 website as AgentiCCells' first offering, an order on a queue, an agentic team that builds a public site, a customer who steers it from their browser with a key, and a handover, with no daily work for the founder](atomic-cells-end-to-end.md) AgentiCCells' first offering: a £500 website as an atomic cell, steered by the customer from their browser with a key, handed over to their GitHub.
- [An agentic console: a simulated control room for a team of agentic teams, with time you can rewind, accounts drawn as trust zones, stops that reach every agent, signed messages on three channels, and the console itself as an agent](an-agentic-console.md) An agentic console, simulated: accounts as trust zones, time you can rewind, signed messages on three channels, honest stops, and the console as an agent.
- [Six setups of an agentic system: from a single task to one agent, sub-agents, several sessions, a conductor and its team, and conductors of conductors, with the altitudes of a run inside each and command and control growing at every step](six-setups-of-an-agentic-system.md) Six setups of an agentic system, from a task to conductors of conductors, with the altitudes of a run inside each: make the dangerous thing unreachable.
- [Selling mini agentic teams: a business that sets up small agentic teams for companies, sized from one agent to a network, with a control centre to see them and to start and stop them, PrompTugal as the first customer and Agent Behaviour Policies as the most demanding version](selling-mini-agentic-teams.md) A business that sets up small agentic teams for companies, with a control centre to start and stop them; PrompTugal first, ABPs on steroids.
- [A brain you arrive at: a company brain for information, decisions and insights is built for one company, one division and one team, starting with one person's and growing, and the Web Summit team already ran one](a-brain-you-arrive-at.md) A company brain is made for one company, division and team, and you arrive at it: start with a person's, then a team's. We already ran one.
- [PrompTugal.news, the newsroom we ran at Web Summit: desks of agents that captured, mapped, wrote and reviewed 73 signed articles in ten days, an accountant that counted every run, and fifty outreach drafts that no agent was allowed to send](promptugal-news-the-newsroom-we-ran.md) PrompTugal.news: 73 signed articles in ten days from desks of agents, a reviewer for every draft, and fifty outreach drafts no agent could send.
- [Always-on agents at team scale: Anthropic's five primitives for an agent that sleeps and wakes, set beside the around 250 named agents six of us ran at Web Summit, and the next problems once there are many](always-on-agents-at-team-scale.md) Anthropic's five primitives for always-on agents, set beside the around 250 named agents six of us ran at Web Summit, and the next problems once there are many.
- [Every hour is twenty years: the human behind Know the Reach, and why making a song and its video with AI made them more Silvio Switha's, not less](every-hour-is-twenty-years.md) Know the Reach was made with AI and by a person: Silvio Switha, whose twenty years as a musician shaped every choice. AI changed the speed, not the vision.
- [Know the Reach: RiskMandate has a song on Spotify, and its music video is being made with AI, shot by shot, from about 2,300 words of human direction; this is how the first part was made](know-the-reach.md) RiskMandate's song Know the Reach is on Spotify; the first 53 seconds of its video were made with AI from about 2,300 words of direction.
- [The team's operating system: web-summit.sgit.ai, the one site where six people and their agents ran Web Summit, with a brief and a command centre for each person, a key and an inbox for each agent, the board as files, and the outside world on a map](the-teams-operating-system.md) web-summit.sgit.ai: one site where six people and their agents ran Web Summit, in four layers built on git.
- [One Human, Nine Agents, Nineteen Hours is on Leanpub: the book of the day nine AI agents and I built a talk, free to download, pay what you want, and updated as it goes](the-book-is-on-leanpub.md) One Human, Nine Agents, Nineteen Hours is on Leanpub: free as a minimum, pay what you want, every update included.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 395 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=395)

**Posting this article on LinkedIn?** The cover is [ten-days-at-web-summit.jpg](banners/ten-days-at-web-summit.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/ten-days-at-web-summit.html)*
