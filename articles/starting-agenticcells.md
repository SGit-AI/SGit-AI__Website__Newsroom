# Starting AgentiCCells: a company that sets up small agentic teams, cells, in the customer's own environment, with a control centre, everything open and no state on our side; how it was named, researched, reviewed and set up in a day, sgit.ai

> Today, after a morning of articles about company brains, data lakes, decisions, mini agentic teams and an agentic console, I started a company to sell them: AgentiCCells. It sets up small agentic teams, cells, installed in the customer's own environment, with a control centre where they see their agents and can start and stop them. Everything it releases is open, code under open-source licences and everything else under Creative Commons, which is the CC in the name, and it keeps no state on its side. Two research briefs compiled with Perplexity mapped more than thirty vendors and found the gap: plenty of people sell frameworks, hosting, single agents and fixed-price workflow builds, but nobody packages conductors of conductors, Agent Behaviour Policies and a control centre, all open, as a service. This newsroom reviewed the positioning, what is strong and what to fix, and I bought three domains: agenticcells.ai for the company, agenticcells.com to redirect, and agenticcells.app for customers' sites. DNS is moving to AWS Route 53, the website repository exists, and a bootstrap brief is ready for the company's first agentic team, on its own Claude account.

*Source: <https://newsroom.sgit.ai/articles/starting-agenticcells.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Starting AgentiCCells: a company that sets up small agentic teams, cells, in the customer's own environment, with a control centre, everything open and no state on our side; how it was named, researched, reviewed and set up in a day

# Starting AgentiCCells: a company that sets up small agentic teams, cells, in the customer's own environment, with a control centre, everything open and no state on our side; how it was named, researched, reviewed and set up in a day

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-15 · [article v1.0.0](versions/starting-agenticcells.md) · [newsroom v999.0.0](https://newsroom.sgit.ai/admin/versions.html) · agenticcellscompanyagentic-teamsopen-sourcepositioningmarket-mapdomainsarticle

***Abstract:** Today, after a morning of articles about company brains, data lakes, decisions, mini agentic teams and an agentic console, I started a company to sell them: AgentiCCells. It sets up small agentic teams, cells, installed in the customer's own environment, with a control centre where they see their agents and can start and stop them. Everything it releases is open, code under open-source licences and everything else under Creative Commons, which is the CC in the name, and it keeps no state on its side. Two research briefs compiled with Perplexity mapped more than thirty vendors and found the gap: plenty of people sell frameworks, hosting, single agents and fixed-price workflow builds, but nobody packages conductors of conductors, Agent Behaviour Policies and a control centre, all open, as a service. This newsroom reviewed the positioning, what is strong and what to fix, and I bought three domains: agenticcells.ai for the company, agenticcells.com to redirect, and agenticcells.app for customers' sites. DNS is moving to AWS Route 53, the website repository exists, and a bootstrap brief is ready for the company's first agentic team, on its own Claude account.*

A company in a day: ideas, research, review, the name, the domains, DNS and the repository, and a brief for its team.

## In short

- **A new company: AgentiCCells,** at agenticcells.ai. It sets up small agentic teams, cells, for companies.
- **Installed in the customer's environment,** with a control centre to see the agents and start and stop them.
- **Everything open, no state on our side:** we sell the setup, the guidance and the trust.
- **The research:** two briefs with Perplexity, a market map of more than thirty vendors, and a clear gap.
- **The review:** what is strong, what to fix, and four decisions I still have to make.
- **Set up in a day:** three domains, DNS on Route 53, a GitHub repository, and a brief for its first agentic team.

## Where it came from

It came out of today's thread. In the morning I wrote, with this newsroom, about [a brain you arrive at](a-brain-you-arrive-at.md), [the new data lake](the-new-data-lake.md), [a market for sweets](a-market-for-sweets.md) and [decide, then buy](decide-then-buy.md). Then about the business itself: [selling mini agentic teams](selling-mini-agentic-teams.md), [six setups of an agentic system](six-setups-of-an-agentic-system.md), and [an agentic console](an-agentic-console.md) to control them.

The argument of those articles is simple. Setting up a small agentic team that does real work is a skill very few people have yet; it took me months. A customer will only buy one if they can see it and control it. And everything we use is open, so what is worth paying for is the setup, the guidance and the trust. That needed a company.

## The name

**AgentiCCells** is Agent, CC and Cells.

- **Agent** is what we set up.
- **CC** is Creative Commons: everything we release is open, code under MIT or Apache, everything else under CC.
- **Cells** are the deliverable: the smallest self-contained unit that runs inside the customer's own organism, their accounts, their git, their runtimes.

The brand is always plural, AgentiCCells, because the singular, AgentCell, is another company's. And the CC has a second reading that our audience will notice first: Claude Code, which is much of the stack. That double meaning can work for us, but the name should not lean on it, and before the CC goes into a logo, Creative Commons' trademark policy needs checking.

## What it sells

Atomic agentic cells, installed in your environment, with a control centre. The first proposal for the sizes is the ladder from [selling mini agentic teams](selling-mini-agentic-teams.md): £500 for one agent, £1,500 for a few sessions, £5,000 for a team, £20,000 for a network, each with the control centre.

Four properties define it:

- **No state on our side.** We hold no customer data, sessions or infrastructure; everything runs in the customer's environment.
- **Every cell is atomic:** valuable on its own and removable without breaking the rest.
- **Everything we release is open,** so anyone could rebuild what we deliver, and that is the point.
- **Cheaper than doing it yourself:** we compress months of learning into a setup.

## The research

The market map: six segments that sell parts of an agentic brain, and the gap that none of them packages.

I asked Perplexity for two briefs. The first is a market map of who sells and deploys open-source agentic brains, from single agents to swarms: framework vendors that open-source their stack and sell the platform around it, swarm platforms, the runtime and tools layer, done-for-you agencies, marketplaces of ready-made agents, and the big systems integrators. The second is a positioning brief for AgentiCCells against that map.

What the map shows, as the briefs report it:

- **The cheap end is crowded.** Agencies building n8n workflows start at about 250 dollars, and marketplaces sell single agents from about 49 dollars a month.
- **The control-centre layer is filling in fast,** with several open-source control planes appearing. The plane will become a commodity; the setup and the policies stay hard.
- **The gap is at the top:** nobody in the map packages conductors of conductors, Agent Behaviour Policies and a control centre, all open source, installed in the customer's environment. The £5,000 to £20,000 tier has no direct competitor, and the RiskMandate angle, every policy with an agent to look after it, has none at all.

The briefs draw on the vendors' own pages and third-party write-ups, and they say so; any vendor fact or price needs checking before we rely on it.

## The review

I asked this newsroom what it thought of the idea and the positioning. Its view, which I agree with:

**What is strong.** The product is the setup, the control centre and the policies, with the software free: the same logic as [decide, then buy](decide-then-buy.md). The gap is real. "No state on our side" is the most distinctive promise, very hard for a platform to copy, and it fits sgit's encrypted vaults and a console that can run on the customer's own device. And cells are a good metaphor for the fractal: a cell grows into a team, a team into a network.

**What to fix.**

- **Pricing.** The brief said "pay per consumption", but if we keep no state, there is nothing of ours to meter. What we really sell is fixed-price cells, perhaps with support packs: finite packs, never rent.
- **Commissions.** Earning referral fees from runtimes and model hosts would give us a reason to steer customers, which undoes the trust a decision business depends on. Drop them, or publish them on every recommendation.
- **Where the console runs.** "No state" invites the question: in the customer's account and vault, or on their device, with support access as a key they seal to us and can revoke.
- **RiskMandate and AgentiCCells.** Agent Behaviour Policies are the same offering on steroids, so it has to be clear who sells them. The cleanest split is that RiskMandate owns the policies and AgentiCCells installs them as a partner.

Those are the decisions I still have to make, and the bootstrap brief tells the new team not to make them for me.

## Setting it up

**Three domains,** checked free and bought on the same day, for about 190 dollars in all:

- **agenticcells.ai** for the company, registered for two years.
- **agenticcells.com** to redirect to it, because it is the one people type.
- **agenticcells.app** for our customers' sites while they get their own domain: `company-x.agenticcells.app`. Keeping customer content on its own domain protects the brand's cookies and reputation, the way github.io does for GitHub; .app only ever loads over HTTPS; and in time it can go on the Public Suffix List, so customers' subdomains are separate sites to the browser.

**DNS on AWS Route 53:** a hosted zone per domain, the registrar's nameservers replaced with Route 53's, and records as data in the repository. The company site will be on GitHub Pages, from [AgentiCCell/AgentiCCell__Website](https://github.com/AgentiCCell/AgentiCCell__Website). Each customer site will be a single CNAME record, never a wildcard, verified in our GitHub organisation, and deleted the day a customer leaves, so no subdomain can be taken over.

**A brief for the first agentic team.** The company's agents will run on their own Claude account, separate from this one. Their bootstrap brief covers:

- **What the company is,** and the four decisions left open, which the team must not make for me.
- **The rules every agent follows:** only I instruct; never send, post or move money; never commit a secret; keep no customer data.
- **A roster of nine roles,** each with an Agent Behaviour Policy: what it may reach, what it was asked to do, what it may not do.
- **Nine first board items,** from writing the reality file to a live site, a tested customer-site pipeline, and the team's own console.
- **The DNS steps, the website's structure,** and both research briefs.

It is the same method that ran [the Web Summit team](the-teams-operating-system.md), applied to a company of our own: AgentiCCells is, in a sense, its own first customer.

## What this does not claim

- **The prices are a first proposal,** and the four decisions above are open.
- **The market map's vendor facts and prices are as the research briefs report them,** from vendors' own pages and third-party write-ups, compiled with Perplexity on 15 November 2026.
- **The company is a day old:** a name, domains, a repository and a brief, not yet a service anyone has bought.

## Where this comes from

Two research briefs compiled with Perplexity on 15 November 2026: Open-Source Agentic Brains, Vendor Market Map, and AgentiCCells, Positioning Brief; this newsroom's review of them; and my own setup of the domains, DNS and repository the same day. Earlier on this site: [selling mini agentic teams](selling-mini-agentic-teams.md), [six setups of an agentic system](six-setups-of-an-agentic-system.md), [an agentic console](an-agentic-console.md), [decide, then buy](decide-then-buy.md), [a brain you arrive at](a-brain-you-arrive-at.md), [the team's operating system](the-teams-operating-system.md).

## Threads

Startups & strategyAgents & policy[This article as a graph →](graphs.md#starting-agenticcells)

### Builds on

- [A brain you arrive at: a company brain for information, decisions and insights is built for one company, one division and one team, starting with one person's and growing, and the Web Summit team already ran one](a-brain-you-arrive-at.md) A company brain is made for one company, division and team, and you arrive at it: start with a person's, then a team's. We already ran one.
- [The new data lake: many small append-only lanes instead of one big lake, a curator agent that turns their rows into a semantic graph, and a graph that draws its own infographics, as we ran it at Web Summit](the-new-data-lake.md) The new data lake: append-only lanes instead of one lake, a curator agent that builds a semantic graph, and a graph that draws its own infographics.
- [A market for sweets: the opposite of a market for lemons, a semantic graph for one financial decision that gives the buyer the evidence, an agent that gathers and weighs but never trades, and the judo move of leaving the trade to others](a-market-for-sweets.md) The opposite of a market for lemons: a semantic graph for one financial decision, an agent that gathers but never trades, and the person decides.
- [Decide, then buy: deciding what to buy and buying it are two different businesses, one for explorers and villagers and one for town planners, and an open path with a better deal beats locking the customer in](decide-then-buy.md) Deciding what to buy and buying it are two businesses: custom explorer work and commodity town planner work. Give an open path and a better deal.
- [Selling mini agentic teams: a business that sets up small agentic teams for companies, sized from one agent to a network, with a control centre to see them and to start and stop them, PrompTugal as the first customer and Agent Behaviour Policies as the most demanding version](selling-mini-agentic-teams.md) A business that sets up small agentic teams for companies, with a control centre to start and stop them; PrompTugal first, ABPs on steroids.
- [Six setups of an agentic system: from a single task to one agent, sub-agents, several sessions, a conductor and its team, and conductors of conductors, with the altitudes of a run inside each and command and control growing at every step](six-setups-of-an-agentic-system.md) Six setups of an agentic system, from a task to conductors of conductors, with the altitudes of a run inside each: make the dangerous thing unreachable.
- [An agentic console: a simulated control room for a team of agentic teams, with time you can rewind, accounts drawn as trust zones, stops that reach every agent, signed messages on three channels, and the console itself as an agent](an-agentic-console.md) An agentic console, simulated: accounts as trust zones, time you can rewind, signed messages on three channels, honest stops, and the console as an agent.
- [The team's operating system: web-summit.sgit.ai, the one site where six people and their agents ran Web Summit, with a brief and a command centre for each person, a key and an inbox for each agent, the board as files, and the outside world on a map](the-teams-operating-system.md) web-summit.sgit.ai: one site where six people and their agents ran Web Summit, in four layers built on git.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 410 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=410)

**Posting this article on LinkedIn?** The cover is [starting-agenticcells.jpg](banners/starting-agenticcells.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/starting-agenticcells.html)*
