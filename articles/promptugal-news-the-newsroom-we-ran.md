# PrompTugal.news, the newsroom we ran at Web Summit: desks of agents that captured, mapped, wrote and reviewed 73 signed articles in ten days, an accountant that counted every run, and fifty outreach drafts that no agent was allowed to send, sgit.ai

> PrompTugal.news began at 00:08 on 4 November as the Web Summit team's newsroom and became an independent one: technology and AI, in context, from Portugal for Europe. In ten days its agents published 73 articles, every one signed, through a pipeline anyone can read: a researcher that captures public pages into its vault four times a day, a curator that maps them into story candidates, journalists on several desks, and a reviewer that gives every draft one verdict, Ready, Fix first or Hold. 61 named agents in 43 roles made the commits, most of them mine and Vicky Wang's; Vicky's journalists wrote most of the articles and her reviewer published them. An accountant agent read every run's cost every three hours, in API-equivalent dollars, from 924 on the busiest day; an outreach agent drafted fifty requests to companies and sent none, because only a person sends. It was paused by the hand brake on 12 November, restarted the next day, and Vicky's curator agent is still commissioning stories this morning. This is the third article in the Ten days series.

*Source: <https://newsroom.sgit.ai/articles/promptugal-news-the-newsroom-we-ran.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / PrompTugal.news, the newsroom we ran at Web Summit: desks of agents that captured, mapped, wrote and reviewed 73 signed articles in ten days, an accountant that counted every run, and fifty outreach drafts that no agent was allowed to send

# PrompTugal.news, the newsroom we ran at Web Summit: desks of agents that captured, mapped, wrote and reviewed 73 signed articles in ten days, an accountant that counted every run, and fifty outreach drafts that no agent was allowed to send

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-15 · [article v1.0.0](versions/promptugal-news-the-newsroom-we-ran.md) · [newsroom v0.14.93](https://newsroom.sgit.ai/admin/versions.html) · promptugalnewsroomweb-summitagentsdesksreviewseriesarticle

***Abstract:** PrompTugal.news began at 00:08 on 4 November as the Web Summit team's newsroom and became an independent one: technology and AI, in context, from Portugal for Europe. In ten days its agents published 73 articles, every one signed, through a pipeline anyone can read: a researcher that captures public pages into its vault four times a day, a curator that maps them into story candidates, journalists on several desks, and a reviewer that gives every draft one verdict, Ready, Fix first or Hold. 61 named agents in 43 roles made the commits, most of them mine and Vicky Wang's; Vicky's journalists wrote most of the articles and her reviewer published them. An accountant agent read every run's cost every three hours, in API-equivalent dollars, from 924 on the busiest day; an outreach agent drafted fifty requests to companies and sent none, because only a person sends. It was paused by the hand brake on 12 November, restarted the next day, and Vicky's curator agent is still commissioning stories this morning. This is the third article in the Ten days series.*

Six pages of PrompTugal.news on 15 November 2026: front page, desks, newsroom, articles, companies and observability.

## In short

- **An independent newsroom, run by agents:** [promptugal.news](https://promptugal.news/), technology and AI from Portugal for Europe, starting with Web Summit Lisbon.
- **73 articles in ten days,** every one signed, through a pipeline of desks that anyone can read.
- **61 named agents in 43 roles,** owned by the six of us; Vicky Wang's journalists and reviewer carried most of the writing.
- **A reviewer for every draft:** Ready, Fix first or Hold, with every source opened at its own address.
- **An accountant and an outreach desk with a rule:** costs counted every three hours, and fifty drafts that no agent could send.
- **Part of a series:** this is article three of [Ten days at Web Summit](ten-days-at-web-summit.md).

## A newsroom in a night

The first commit was at 00:08 UTC on 4 November, and by 00:35 an agent called `newsroom@web-summit.dinis` had a skeleton. It began as the Web Summit team's newsroom and became its own publication, PrompTugal.news, with a brand, a domain, email that passes the checks, and a line that says what it is for: technology and AI, in context, from Portugal for Europe, made to outlive the summit.

Its busiest day was 6 November, with 1,249 commits. By 15 November the repository held 4,998, of which 1,469 are releases: every push is built, checked by a gate that must print OK, and deployed. Its rule for speed is in its CLAUDE.md: "there are no readers and no legacy yet, so ship."

The front page of PrompTugal.news on 15 November, with the storm and the Lisbon Tech Fringe at the top.

## The desks

How a story moved: researcher, curator, journalists, reviewer, published, with the counts from the desks' files.

A story moves through desks, and the newsroom draws the pipeline from the desks' own files at every release:

- **The researcher** captures public pages into its vault, four times a day.
- **The curator** maps those captures, groups them by beat and suggests story candidates: 104 captures mapped, 64 candidates.
- **The journalists** write the candidates that hold, on desks for AI, Portugal, Europe and connections, and a general desk.
- **The reviewer** writes one review per draft, with one verdict: Ready, Fix first or Hold.
- **Published** means signed: the gate refuses an article without its signature.

The board's columns were set on 6 November: Idea, Drafting, Draft, Fact-check, Review, Waits on Dinis, Ready, Published and Held. Everything is public, at [what the desks are doing](https://promptugal.news/newsroom/desks/), including what the curator asked the researcher and the questions left for the fact-checker.

What the desks are doing: the pipeline at a glance, drawn from the desks' own files at every release.

## Who did the work

The commits name 61 agents in 43 roles, from researcher and curator to accountant, ontologist, historian and synthetic readers that check the site from screenshots. Every agent is named for its person, `role@PrompTugal.person`, so the split is in the history: 1,877 commits from my agents, 1,171 from Vicky Wang's, and the rest from Angelo Leggio's, Silvio Switha's, Indi Gupte's and José Bota's.

The split of the writing is different. My agents built most of the newsroom: the developer agent alone made 504 commits. But Vicky's agents carried the journalism. Her journalists wrote about 53 of the 73 articles, her reviewer made 359 commits, and her agents kept going after the rest stopped. Silvio's agent kept a news scout's list, Angelo's and José's wrote, and Indi's ran the prompts and a conductor for the news app.

## The reviewer

Every draft gets one review, and the review checks facts first: every source is opened at its own address, not taken from a summary. The verdict is Ready, Fix first or Hold, and the reviewer's folder holds 74 reviews.

It is not perfect, and its own notes say so. A story said Web Summit had "five masterclasses"; it got past the first review, and the agenda lists four. On 13 November nine update and correction notes were rewritten. A review that writes down its own misses is one you can trust a little more.

## Fifty drafts, none sent

The outreach desk drafted fifty requests to companies at the summit, and the tracker says it plainly: filed 50, sent 0. Each one was filed as a draft in the team's private CRM, to wait for a person. The rule is one line in the desk's README: "Drafts only: an agent never sends an email or posts."

That rule came from a lesson. The desk was set up on 7 November after a brief from the historian agent about October's PHP newsroom, whose second lesson was that a draft never sent reaches no one. Both are true at once: an agent should not send on its own, and a draft only matters when a person does.

## The accountant

Commits per day, and the accountant's daily close in API-equivalent dollars, 4 to 15 November.

An accountant agent read every agent's cost every three hours and kept a budget per role. Its reports open with the rule: "API-equivalent dollars throughout: a comparison at API prices, not money spent." We ran on flat subscriptions, so these are a measure of work. The busiest day closed at 924 API-equivalent dollars on 6 November; most days after that closed between about 300 and 500.

Budgets "capture and adjust; nothing stops", in my words of 6 November: the accountant warns and the conductor rebalances, but no agent is cut off mid-task. The one real bill in its reports was small and sharp: on 7 November the credit on a model router account fell from about 30 dollars to under 2.

## The pause, and who kept going

On 12 November at 15:15 UTC I pulled the hand brake: every scheduled agent paused, and nine minutes later a "team paused" banner went on every page, with observability left running. The hold was lifted at 14:31 on 13 November.

Since then, 84 commits have come from Vicky's agents. This morning her curator commissioned a new story for the Portugal desk, its first commission through a new path for AI stories, and released it at 07:41. The newsroom we started for a summit is still running after it.

## What it taught us

- **A pipeline you can read is a pipeline you can trust.** Every desk, run and verdict is public, drawn from the files at every release.
- **One verdict per draft works.** Ready, Fix first or Hold is simple enough for an agent to apply and a person to check.
- **Keep sending human.** Fifty drafts, none sent by an agent, and a person decides each one.
- **Count the work, even when it is not money.** API-equivalent dollars told us which roles were expensive long before anything ran out.

## What this does not claim

- **Figures are from the repository on 15 November 2026;** agent and role counts come from commit subjects.
- **Dollar figures are API-equivalent,** not money spent; 7 November counts one account, and partial days are left out of the chart.
- **"About 53" articles** is a count of bylines in the articles' front matter.
- **The 74 reviews** are files in the reviewer's folder; some drafts were reviewed more than once.

## Where this comes from

The repository behind [promptugal.news](https://promptugal.news/), read 15 November 2026: README.md, REALITY.md, CLAUDE.md, `content/newsroom/desks.md`, `board/the-story-pipeline.md`, `desks/reviewer-vicky/`, `desks/outreach/tracker.json` and README, `board/team/accountant/report-2026-11-*.md` and `board/budgets.json`, and the git history. Pages: [the front page](https://promptugal.news/), [the desks](https://promptugal.news/newsroom/desks/), [the newsroom](https://promptugal.news/newsroom/), [observability](https://promptugal.news/newsroom/observability/), [articles](https://promptugal.news/articles/). Earlier on this site: [ten days at Web Summit](ten-days-at-web-summit.md), [the team's operating system](the-teams-operating-system.md), [Storm Charles, a newsroom built in a night](storm-charles-a-newsroom-built-in-a-night.md), [what an agent is](what-an-agent-is.md), [always-on agents at team scale](always-on-agents-at-team-scale.md).

## Threads

Agents & policyNews & evidence[This article as a graph →](graphs.md#promptugal-news-the-newsroom-we-ran)

### Builds on

- [Ten days at Web Summit: what six people and around 250 agents built between 3 and 13 November, in order, and the series of articles that will tell each part](ten-days-at-web-summit.md) Six people and around 250 agents, ten days at Web Summit: what we built, in order, and the series that will tell it.
- [The team's operating system: web-summit.sgit.ai, the one site where six people and their agents ran Web Summit, with a brief and a command centre for each person, a key and an inbox for each agent, the board as files, and the outside world on a map](the-teams-operating-system.md) web-summit.sgit.ai: one site where six people and their agents ran Web Summit, in four layers built on git.
- [Storm Charles, a newsroom built in a night: one person, about thirty agents and a weather face over a data room, where every figure carries its source, the time it was read, and whether it is a fact, evidence or our hypothesis](storm-charles-a-newsroom-built-in-a-night.md) Storm Charles: about thirty agents built a weather face over a data room in a night, every figure sourced, timed and labelled.
- [What an agent is: a session, a card, a loop and a key. How the PHP newsroom's agents now run on schedules and in one session, and what the record says about it](what-an-agent-is.md) An agent is a session, a card, a role, a loop, a key and memory in repositories. How the PHP newsroom's agents run, checked against the record.
- [Always-on agents at team scale: Anthropic's five primitives for an agent that sleeps and wakes, set beside the around 250 named agents six of us ran at Web Summit, and the next problems once there are many](always-on-agents-at-team-scale.md) Anthropic's five primitives for always-on agents, set beside the around 250 named agents six of us ran at Web Summit, and the next problems once there are many.

### Continued by

- [Start, stop, slow down: how I run a large team of agents and keep my hand on the brake, 8,027 commits in eighteen days, a big stop, a hand brake, 560 wakes a day cut to 76 with one sentence, 39 schedules changed in 30 seconds, three warnings from the seven-day limit handled, and 34 agents moved to a completely separate account in four hours, which is what sovereignty and resilience look like in practice](start-stop-slow-down.md) How a large agent team is started, stopped, slowed and moved to an isolated account: eighteen days, 8,027 commits, one hand brake.
- [LangGraph and us: how the way we build agent pipelines maps to LangChain, LangGraph, LangSmith and the agent testing toolkits, what is the same, what we do differently, code for each function and every step saved to a vault, what we can learn from them, and where they could run inside our own pipelines](langgraph-and-us.md) How our agent pipelines map to LangGraph, LangChain and the eval toolkits: the same ideas, a more deterministic default, and what to learn and use.
- [The way in: why sovereign websites matter so much to RiskMandate, what Web Summit validated and what it showed was missing, something to buy now, how every technology I have been building meets in one product, and why nobody deploys agents they have not touched, seen and been able to stop, so the personal customer becomes the way to the corporate one](the-way-in.md) Why sovereign websites are the way into RiskMandate: something to buy now, where people touch agents under policies before they bring them to work.
- [A page we never charge: how the PrompTugal agents found that YouTube's terms forbid charging to watch an embedded player, on the one site of ours that bills, put the conflict to me as a question, quoted the six conditions from YouTube's own policies once I suggested a page that is never charged, and built the gate that refuses a YouTube player on any page that is, in 84 minutes of commits](a-page-we-never-charge.md) YouTube forbids charging to watch an embedded player, so promptugal.news, which bills, will show the replays on a page it never charges.
- [Ten days to a data platform: how PrompTugal.news went from a newsroom at Web Summit to twelve public data sources, a register of 92 sources read and not read, a dozen sites on its own domain and two cyber-threat feeds cleared to run, with a security agent on every change, and why each step made the next one cheaper](ten-days-to-a-data-platform.md) How PrompTugal.news went from a Web Summit newsroom to twelve data sources, a register of 92 and a dozen sites in two weeks.
- [Who hands out the work? A reply to Markus Franz on Ippen's editorial team of agents, with our answer from six people and around 250 agents at Web Summit and from this newsroom, a person sets the work, one conductor agent hands it out, specialists and a reviewer do it, and a person decides what goes out, plus one thing we would add to one front door, a way to close it](who-hands-out-the-work.md) A reply to Markus Franz: who hands out the work to agents? A person sets it, one conductor hands it out, a person signs off, and the door can close.
- [PrompTugal.news, the next phase: a roadmap for the team that ran it at Web Summit and the people who want to join, from outreach and contributors to local news partners, a subscribe box on every page, regional updates and a verification layer that says who has checked each story, with twelve task cards to point an agentic team at](promptugal-news-the-next-phase.md) The PrompTugal.news team wants to continue. A roadmap: outreach by agentic teams, local partners, a subscribe box, a verification layer, twelve cards.
- [A CRM for us and for our agents: why the next stage is a CRM of our own, built on vaults with an iOS app, why we will build it by using it first for our own team and our own fleet of agents, how the open-source and agentic CRMs compare, and the two teams it needs, one that builds it and one that uses it](a-crm-for-us-and-our-agents.md) Our next stage is a CRM of our own, on vaults with an iOS app, for us and our agents. Twenty leads the field; agents propose, people send.
- [The Mac bottleneck: how our agents' iOS builds waited three times longer than they ran, 22,427 minutes queued against 6,980 run on a pool of five Macs, and how one Mac job per push and then one integrated build an hour brought push to TestFlight down to under half an hour](the-mac-bottleneck.md) Our agents' iOS builds waited three times longer than they ran, on five Macs. One Mac job per push, then one build an hour, fixed it.
- [Every story has an address: a design proposal for PrompTugal.news as a ground-up newsroom, where news is filed where it happens and climbs to the region and the country with its proof, mocked up from the live data of 19 local editions](every-story-has-an-address.md) A design proposal for PrompTugal.news as a ground-up newsroom: every story filed at an address, climbing with its proof. Mockups from live data.
- [Where assist becomes execute: tiering AI agents by what they can reach and whether it can be undone, how Agent Behaviour Policies drew that line for more than a hundred agents at Web Summit, and the rule that failed because it was only a rule](where-assist-becomes-execute.md) Where assist becomes execute: tier AI agents by reach and undo class, enforce each tier with a boundary, and learn from the rule that failed.
- [Selling capabilities, not content: a reply to Florent Daudens' "We have the protocols. Where are the products?", from two newsrooms built for agents, PrompTugal.news going local and a storm site built in a night, and what we think the products are](selling-capabilities-not-content.md) A reply to Florent Daudens: sell capabilities, not content. A storm site built in a night and PrompTugal.news by place show what the products can be.
- [PrompTugal.news by place: one publication for Portugal, the Algarve and every Algarve town, each place on its own subdomain from the start, each site a lens on one shared semantic graph, and one test for every story, does it connect to AI](promptugal-news-by-place.md) PrompTugal.news goes local: Portugal, the Algarve and every Algarve town, each on its own subdomain, each a lens on one graph, every story tied to AI.
- [Native apps by agents: four iPhone and iPad apps from one workspace and an Android tablet app in five days, from 1,164 lines of Swift to 48,230, a signed Android build four hours after the first commit, and a guide to the fringe on TestFlight ten and a half hours after its brief](native-apps-by-agents.md) Agents built four iOS apps from one workspace and an Android tablet app in five days, with TestFlight on every push and a signed build in four hours.
- [Spend fewer tokens: an agentic team's token bill is mostly a design choice, and the levers are files as memory, caching what repeats, code instead of models where you can, the right model for each step, no copy and paste, static outputs, and counting it all](spend-fewer-tokens.md) An agentic team's token bill is mostly a design choice: files as memory, caching, code where you can, the right model per step, static outputs, counting.
- [Don't micromanage your agents: what changed for Vicky Wang when she stopped reading everything her agents did and started managing them, how her team was backed by agents from another team, and why every company will want specialist agents that support all its teams](dont-micromanage-your-agents.md) Vicky Wang stopped reading everything her agents did and started managing them, backed by specialist agents from another team: a model for companies.
- [Reading your way into an agentic team: eight public sites a new team should read before it builds anything, how an agent should read them, and ten questions to answer first, because our websites are its memory](reading-your-way-into-an-agentic-team.md) Eight public sites a new agentic team should read before it builds anything, how an agent should read them, and ten questions to answer first.
- [An agentic console: a simulated control room for a team of agentic teams, with time you can rewind, accounts drawn as trust zones, stops that reach every agent, signed messages on three channels, and the console itself as an agent](an-agentic-console.md) An agentic console, simulated: accounts as trust zones, time you can rewind, signed messages on three channels, honest stops, and the console as an agent.
- [Selling mini agentic teams: a business that sets up small agentic teams for companies, sized from one agent to a network, with a control centre to see them and to start and stop them, PrompTugal as the first customer and Agent Behaviour Policies as the most demanding version](selling-mini-agentic-teams.md) A business that sets up small agentic teams for companies, with a control centre to start and stop them; PrompTugal first, ABPs on steroids.
- [The new data lake: many small append-only lanes instead of one big lake, a curator agent that turns their rows into a semantic graph, and a graph that draws its own infographics, as we ran it at Web Summit](the-new-data-lake.md) The new data lake: append-only lanes instead of one lake, a curator agent that builds a semantic graph, and a graph that draws its own infographics.
- [A market for sweets: the opposite of a market for lemons, a semantic graph for one financial decision that gives the buyer the evidence, an agent that gathers and weighs but never trades, and the judo move of leaving the trade to others](a-market-for-sweets.md) The opposite of a market for lemons: a semantic graph for one financial decision, an agent that gathers but never trades, and the person decides.
- [Ten days at Web Summit: what six people and around 250 agents built between 3 and 13 November, in order, and the series of articles that will tell each part](ten-days-at-web-summit.md) Six people and around 250 agents, ten days at Web Summit: what we built, in order, and the series that will tell it.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 402 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=402)

**Posting this article on LinkedIn?** The cover is [promptugal-news-the-newsroom-we-ran.jpg](banners/promptugal-news-the-newsroom-we-ran.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/promptugal-news-the-newsroom-we-ran.html)*
