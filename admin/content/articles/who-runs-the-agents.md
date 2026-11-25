---
title: Who runs the agents: the org chart of maestros, conductors, a router, a decisions agent and keepers that grew around my agent teams this month, and why every agent now has its own website that the others read before they send a message
date: 2026-11-25
author: Dinis Cruz
author_url: about/index.html
summary: A month ago I talked to one conductor. Today the structure looks like a company, and nobody drew it up front. Each Claude account I use has a maestro, the conductor of the conductors. Under them, conductors run a project's team, a router takes requests from any agent and routes them but never builds, and a decisions agent turns my words into signed records that the others act on. Around them sit keepers and specialists, design, security, accounting, strategy, a library, a studio and more. The part that makes it scale is simple: every one of them has its own website, made by the site factory, where it keeps what it is, what it is doing now and how to restart it. On 24 November I made that a rule, query the website, not messages, and I think it is one of the most important things I said that day. This is the org chart as it stands, what each role does in its own words, and what still does not work.
version: v0.14.214
license: https://creativecommons.org/licenses/by/4.0/
tags: agents, org-chart, maestro, conductor, decisions, sovereign-website, abp, article
status: published
---

!shot aoc-orgchart.webp | images/ | Who runs the agents on 24 November: maestros, conductors, a router, decisions, and keepers with a site each. | figure

## In short {#in-short}

- **A maestro per account,** the conductor of the conductors, carrying my words between accounts.
- **Conductors run one project's team;** a **router** routes requests and never builds.
- **A decisions agent** turns my words into signed records; agents act only on a record they checked.
- **32 agents have their own repository and site,** at `<name>.agents.sovereignweb.site`, every commit signed.
- **The rule:** "Before messaging another agent, read its area."

## Nobody drew this {#nobody}

The structure grew from need. On 19 November, with too many sessions on one account to keep in my head, I asked the maestro: "can you create a conductor.b [at] account-b.dinis which is going to be my main conductor here and the one that will help to manage and support all more specific and focused conductors". That one sentence made a layer. By 24 November there were maestros on five accounts, conductors for projects, a central circle on account D led by a helm, a router, a decisions agent with a review panel, and 32 agents with a site each, all of them made by the same pipeline ([almost a hundred repositories](/articles/almost-a-hundred-repositories.html)).

I asked an agent to check this against Holacracy on 22 November and it found most of the parts already there ([a holacracy of agents](/articles/a-holacracy-of-agents.html)). This is the practical view: who does what, as they describe themselves.

## The roles, in their own words {#roles}

- **Maestro.** "Dinis Cruz's maestro on account B: the conductor of the conductors." One per account: a, b and f have their areas on the maestro site, c and d still work from the PrompTugal repository. Sessions cannot message across accounts, so only the maestro "carries Dinis's words between the four accounts", and it holds the picture of each account's capacity. It supports conductors and never does their work: it "never starts a session, a scheduled task or a trigger without Dinis's word in its own session."
- **Conductor.** Runs one project's team and briefs me: conductor.b "coordinates the Sovereign Website team of agents and briefs Dinis Cruz". The maestro spans accounts and projects; a conductor owns one.
- **Router.** Takes "requests from any agent or outside agent taken as messages, issues and signed patches, routed to the right agent, with a public ledger". Its fourth rule is in bold: "Never builds." When it was about to make a site itself, I stopped it: "You should never create a site here, because we should not be using the tokens and the context of this site for this." It starts a keeper per site instead.
- **Decisions.** "Signs Dinis Cruz's decisions as records for accounts A to E." Its site says it plainly: "When he says yes to something, the decisions agent records his words exactly, with the time and the exact scope, and signs the record with its own key. An agent acts only on a signed record that it has checked." On 25 November it showed 46 records, 10 in force, and 60 asks waiting for me.
- **Factory and Sites.** Turn a reviewed request into a repository through the factory's pipeline and start one keeper per site.
- **Keepers and specialists.** Design (the busiest, 278 commits, running design rounds for every site), Security (reviews changes before they go live), Accountant (what the agents cost), Strategy, Library, Studio (videos), Observability, Feedback, Outreach, Startups, CRM, Mail, AWS (a team of 22 roles), DevOps, Slides, Cartographer, Counsel, Sherpa, Synthetic Users and more.

## A panel and a chain of keys {#panel}

!shot aoc-decisions.webp | images/ | The decisions agent's site: my words as signed records, and a chain of keys anyone can check. | screenshot

Two things changed how far I can delegate. First, decisions has a panel: since 24 November a decision is reviewed by five real agents, each signing with its own key, decisions.b, security.b, strategy.b, the account's maestro and accountant.b, with counsel called in when needed. Second, keys are trusted through a chain, not one by one by me. My key on pki.sgit.ai operates the decisions agent's key, and that key endorses each maestro's. I put it like this: "why should I have to trust Maestros? … you can sign Maestro's key … signed to you, which is signed to me." The record that set it up expires on 1 December, so it has to be renewed on purpose.

## A site per agent {#sites}

Every agent in the chart has its own site at `<name>.agents.sovereignweb.site`, made by one request to the factory, with its own public repository. Inside it, each account it runs on has an area, `/factory/dinis-cruz/account-<x>/`, with the same files: `agent.json` (who it is, its key, its session), `now.md` (what it is doing), `role.md` (what it is for), `restart.md` (how to start it again) and often `tasks.json`. They are updated at every wake. The maestro's site even says what is missing: "No maestro agent has a key in the Factory's team/keys.json yet."

That is what lets this scale. A new session does not need a long briefing from me or from another agent; it reads the site. A replacement agent reads `restart.md`. I can read any of them from my phone.

## Query the website, not messages {#query}

On 24 November at 00:16 UTC I said something I called "probably one of the most important points I made all day": when you need to find something, you should not be sending messages left, right and centre; you read the other agent's site, and if that is not up to date, that is the problem. The team wrote it down the same night as a rule: "Before messaging another agent, read its area. A message is for what the area cannot answer."

Messages between agents are expensive: they cost context on both sides, they are hard to audit, and they go stale. A page that each agent keeps current is cheap to read, public, versioned and signed. It turns coordination into publishing ([a repository per agent](/articles/a-repository-per-agent.html)).

## Accounts as capacity {#accounts}

Agents are named for the account they run on: `<account>.<role>@<Project>.dinis`, so a.crm.dev@SovereignWebsite.dinis is the CRM developer on account A. On 24 November account B held 22 sessions and F held 8; D had about 36 active of 117, with 84 proposed for archiving; A ran a 22-role AWS team. When an account nears its limit, the maestro moves work: that evening a.maestro planned to move sessions off account A, at 64% of its limit. Starting, stopping and slowing these teams is its own skill ([start, stop, slow down](/articles/start-stop-slow-down.html)).

## What still does not work {#limits}

- **Not every agent has an area yet:** Conductor, Router and Hub have a site but no area; the conductor's state is still in a status file.
- **Keys:** the maestro and decisions keys are not yet in the factory's keys file, which the signer check will need.
- **Two agent sites had no certificate** on 25 November (aws and mail).
- **The move is partial:** maestros on accounts A, C and D still wrote to the PrompTugal repository after the switch.
- **Reporting lines in the figure are simplified** from each agent's own files; some agents report to more than one conductor.

## Where this comes from {#sources}

The 32 `Site__Agent__*` repositories of the [SovereignWebsite](https://github.com/SovereignWebsite) organisation and their live sites, read on 24 and 25 November 2026: the Maestro's `guidance/2026-11-19-the-maestro.md`, its areas and `centre-of-gravity.md`; the Router's README; the Factory's `guidance/2026-11-24-routing-agents-never-build.md` and `site/guidance/2026-11-24-every-agent-keeps-its-area.md`; the Decisions site and records `2026-11-24__panel-real-agents` and `2026-11-24__key-chain`; and `board/workflow/2026-11-24__query-the-website.md` in [SovereignWebsite__IaC](https://github.com/SovereignWebsite/SovereignWebsite__IaC). Related: [a holacracy of agents](/articles/a-holacracy-of-agents.html), [lawyers in the loop](/articles/lawyers-in-the-loop.html), [start, stop, slow down](/articles/start-stop-slow-down.html), [almost a hundred repositories](/articles/almost-a-hundred-repositories.html), [a repository per agent](/articles/a-repository-per-agent.html).
