---
title: Starting AgentiCCells: a company that sets up small agentic teams, cells, in the customer's own environment, with a control centre, everything open and no state on our side; how it was named, researched, reviewed and set up in a day
date: 2026-11-15
author: Dinis Cruz
author_url: about/index.html
summary: Today, after a morning of articles about company brains, data lakes, decisions, mini agentic teams and an agentic console, I started a company to sell them: AgentiCCells. It sets up small agentic teams, cells, installed in the customer's own environment, with a control centre where they see their agents and can start and stop them. Everything it releases is open, code under open-source licences and everything else under Creative Commons, which is the CC in the name, and it keeps no state on its side. Two research briefs compiled with Perplexity mapped more than thirty vendors and found the gap: plenty of people sell frameworks, hosting, single agents and fixed-price workflow builds, but nobody packages conductors of conductors, Agent Behaviour Policies and a control centre, all open, as a service. This newsroom reviewed the positioning, what is strong and what to fix, and I bought three domains: agenticcells.ai for the company, agenticcells.com to redirect, and agenticcells.app for customers' sites. DNS is moving to AWS Route 53, the website repository exists, and a bootstrap brief is ready for the company's first agentic team, on its own Claude account.
version: v0.14.98
license: https://creativecommons.org/licenses/by/4.0/
tags: agenticcells, company, agentic-teams, open-source, positioning, market-map, domains, article
status: published
---

!shot acc-day.webp | images/ | A company in a day: ideas, research, review, the name, the domains, DNS and the repository, and a brief for its team. | timeline

## In short {#in-short}

- **A new company: AgentiCCells,** at agenticcells.ai. It sets up small agentic teams, cells, for companies.
- **Installed in the customer's environment,** with a control centre to see the agents and start and stop them.
- **Everything open, no state on our side:** we sell the setup, the guidance and the trust.
- **The research:** two briefs with Perplexity, a market map of more than thirty vendors, and a clear gap.
- **The review:** what is strong, what to fix, and four decisions I still have to make.
- **Set up in a day:** three domains, DNS on Route 53, a GitHub repository, and a brief for its first agentic team.

## Where it came from {#origin}

It came out of today's thread. In the morning I wrote, with this newsroom, about [a brain you arrive at](/articles/a-brain-you-arrive-at.html), [the new data lake](/articles/the-new-data-lake.html), [a market for sweets](/articles/a-market-for-sweets.html) and [decide, then buy](/articles/decide-then-buy.html). Then about the business itself: [selling mini agentic teams](/articles/selling-mini-agentic-teams.html), [six setups of an agentic system](/articles/six-setups-of-an-agentic-system.html), and [an agentic console](/articles/an-agentic-console.html) to control them.

The argument of those articles is simple. Setting up a small agentic team that does real work is a skill very few people have yet; it took me months. A customer will only buy one if they can see it and control it. And everything we use is open, so what is worth paying for is the setup, the guidance and the trust. That needed a company.

## The name {#name}

**AgentiCCells** is Agent, CC and Cells.

- **Agent** is what we set up.
- **CC** is Creative Commons: everything we release is open, code under MIT or Apache, everything else under CC.
- **Cells** are the deliverable: the smallest self-contained unit that runs inside the customer's own organism, their accounts, their git, their runtimes.

The brand is always plural, AgentiCCells, because the singular, AgentCell, is another company's. And the CC has a second reading that our audience will notice first: Claude Code, which is much of the stack. That double meaning can work for us, but the name should not lean on it, and before the CC goes into a logo, Creative Commons' trademark policy needs checking.

## What it sells {#sells}

Atomic agentic cells, installed in your environment, with a control centre. The first proposal for the sizes is the ladder from [selling mini agentic teams](/articles/selling-mini-agentic-teams.html): £500 for one agent, £1,500 for a few sessions, £5,000 for a team, £20,000 for a network, each with the control centre.

Four properties define it:

- **No state on our side.** We hold no customer data, sessions or infrastructure; everything runs in the customer's environment.
- **Every cell is atomic:** valuable on its own and removable without breaking the rest.
- **Everything we release is open,** so anyone could rebuild what we deliver, and that is the point.
- **Cheaper than doing it yourself:** we compress months of learning into a setup.

## The research {#research}

!shot acc-market.webp | images/ | The market map: six segments that sell parts of an agentic brain, and the gap that none of them packages. | infographic

I asked Perplexity for two briefs. The first is a market map of who sells and deploys open-source agentic brains, from single agents to swarms: framework vendors that open-source their stack and sell the platform around it, swarm platforms, the runtime and tools layer, done-for-you agencies, marketplaces of ready-made agents, and the big systems integrators. The second is a positioning brief for AgentiCCells against that map.

What the map shows, as the briefs report it:

- **The cheap end is crowded.** Agencies building n8n workflows start at about 250 dollars, and marketplaces sell single agents from about 49 dollars a month.
- **The control-centre layer is filling in fast,** with several open-source control planes appearing. The plane will become a commodity; the setup and the policies stay hard.
- **The gap is at the top:** nobody in the map packages conductors of conductors, Agent Behaviour Policies and a control centre, all open source, installed in the customer's environment. The £5,000 to £20,000 tier has no direct competitor, and the RiskMandate angle, every policy with an agent to look after it, has none at all.

The briefs draw on the vendors' own pages and third-party write-ups, and they say so; any vendor fact or price needs checking before we rely on it.

## The review {#review}

I asked this newsroom what it thought of the idea and the positioning. Its view, which I agree with:

**What is strong.** The product is the setup, the control centre and the policies, with the software free: the same logic as [decide, then buy](/articles/decide-then-buy.html). The gap is real. "No state on our side" is the most distinctive promise, very hard for a platform to copy, and it fits sgit's encrypted vaults and a console that can run on the customer's own device. And cells are a good metaphor for the fractal: a cell grows into a team, a team into a network.

**What to fix.**

- **Pricing.** The brief said "pay per consumption", but if we keep no state, there is nothing of ours to meter. What we really sell is fixed-price cells, perhaps with support packs: finite packs, never rent.
- **Commissions.** Earning referral fees from runtimes and model hosts would give us a reason to steer customers, which undoes the trust a decision business depends on. Drop them, or publish them on every recommendation.
- **Where the console runs.** "No state" invites the question: in the customer's account and vault, or on their device, with support access as a key they seal to us and can revoke.
- **RiskMandate and AgentiCCells.** Agent Behaviour Policies are the same offering on steroids, so it has to be clear who sells them. The cleanest split is that RiskMandate owns the policies and AgentiCCells installs them as a partner.

Those are the decisions I still have to make, and the bootstrap brief tells the new team not to make them for me.

## Setting it up {#setup}

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

It is the same method that ran [the Web Summit team](/articles/the-teams-operating-system.html), applied to a company of our own: AgentiCCells is, in a sense, its own first customer.

## What this does not claim {#limits}

- **The prices are a first proposal,** and the four decisions above are open.
- **The market map's vendor facts and prices are as the research briefs report them,** from vendors' own pages and third-party write-ups, compiled with Perplexity on 15 November 2026.
- **The company is a day old:** a name, domains, a repository and a brief, not yet a service anyone has bought.

## Where this comes from {#sources}

Two research briefs compiled with Perplexity on 15 November 2026: Open-Source Agentic Brains, Vendor Market Map, and AgentiCCells, Positioning Brief; this newsroom's review of them; and my own setup of the domains, DNS and repository the same day. Earlier on this site: [selling mini agentic teams](/articles/selling-mini-agentic-teams.html), [six setups of an agentic system](/articles/six-setups-of-an-agentic-system.html), [an agentic console](/articles/an-agentic-console.html), [decide, then buy](/articles/decide-then-buy.html), [a brain you arrive at](/articles/a-brain-you-arrive-at.html), [the team's operating system](/articles/the-teams-operating-system.html).
