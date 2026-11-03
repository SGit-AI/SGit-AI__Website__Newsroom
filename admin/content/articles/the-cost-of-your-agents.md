---
title: The cost of your agents: a first RiskMandate partner integration, where a company that reads agent logs and token spend meets the behaviour policy that says what each agent is for, and together they can say whether the spend is right
date: 2026-11-03
author: Dinis Cruz
author_url: about/index.html
summary: Imagine a company whose product reads an organisation's agent logs, conversations and token usage, and uses models to explain what the agents did and what it cost. It sees every token. What it cannot see is what each agent is for, so it cannot say whether a large bill is waste or the job. That is exactly what a behaviour policy holds. An agent that reads millions of tokens may be doing its research correctly; another that spends forty thousand tokens on a support ticket has an engineering problem. This is a case study for the first integration of the RiskMandate partner programme, with an invented partner, Tallyline, and the newsroom's invented bank, Pellbridge, whose six agents already have behaviour policies. Each policy gains a cost row; Tallyline reads a month of logs; every agent gets a verdict against its mandate. At Anthropic's published prices, Pellbridge's agents cost about $9,320 a month, and the findings that respect each mandate bring it to about $3,400. The most expensive agent per task stays expensive, because its mandate says so. The value proposition is one question: do you understand the cost of your agents? A working version is in a vault.
version: v0.14.50
license: https://creativecommons.org/licenses/by/4.0/
tags: riskmandate, partners, token-costs, finops, behaviour-policies, agents, integration, vaults, article
status: published
---

!shot pmo-overview.webp | images/ | The worked example: every Pellbridge agent judged against its mandate, this month's cost and with the findings applied. | screenshot

## In short {#in-short}

- **The question for a customer:** do you understand the cost of your agents?
- **A cost tool sees what each agent spent;** a behaviour policy says what each agent is for.
- **Together they can say whether the spend is right,** agent by agent, with a reason.
- **The worked example:** an invented partner, Tallyline, and the invented Pellbridge Bank; prices as published.
- **About $9,320 a month, to about $3,400,** without touching what the business needs.
- **Expensive is not the same as wrong:** the AML reviewer stays expensive, because that is its job.
- **The integration is small:** mandates one way, findings the other, logs stay with the customer.
- **[Open the vault](https://dev.vault.sgraph.ai/#sgit_public_read_d199351130f22f55c1a25ab849266a962163b136b218729f95d316255988244a%3Arxxgqjen)** to see it working.

## The partner {#partner}

Here is a kind of company RiskMandate should work with, invented for this article and called Tallyline: it reads an organisation's agent logs and conversations, with permission, and uses models to understand what happened: what the agents did, how they decided, and what it cost. One thing it is very good at, and that has value straight away, is cost: tokens, models, threads, caching, the advice that brings a bill down.

The need is real and growing. Menlo Ventures estimated that "companies spent $37 billion on generative AI in 2025", and in the FinOps Foundation's 2026 survey, "98% of respondents now manage AI spend (up from 63% in 2025 and 31% in 2024)". Many teams are not token efficient: they load whole pages into every turn, keep threads running for hours, and never cache. We try hard to be: short threads, compression we control, markdown, a repository as memory, and [a hook that shows what every session costs](/articles/the-tokens-hook.html).

## What a cost tool cannot see {#cannot-see}

Tallyline can tell you that an agent spent a million tokens. It cannot tell you whether that is right. For a research agent that is supposed to read everything and produce a report, a million tokens is the job. For an agent that answers a customer's question about a payment, a thousand tokens is plenty, and five thousand is a smell that something is wrong with the engineering.

That missing piece is business context, and it is what an [Agent Behaviour Policy](/articles/what-can-your-agent-reach.html) holds: the mandate, what the business wants this agent to do. The FinOps Foundation's guidance on AI says the same in its own words: "Measure the use case, not the token. Track cost per successful outcome." You can only measure the use case if someone has written down what the use case is.

So the policies RiskMandate writes for a customer gain a cost row: the unit of work (a ticket, an alert, an application), the tokens a unit should take, the models allowed, whether it should run live or in batch. In the past we used behaviour policies to stop a process doing something it should not, as in [SHarness](/articles/introducing-sharness.html). Here the same policy is used to understand: it gives the cost tool the expectation to measure against.

## The worked example {#example}

[Pellbridge Bank](/articles/inside-the-pellbridge-agents.html), invented for this newsroom, already has six agents with behaviour policies. For this example each policy gained a cost row, and Tallyline read a synthetic month of their work, priced at Anthropic's published rates of 3 November 2026.

| Agent | Tokens a unit (mandate) | A month | Verdict |
|---|---|---|---|
| Payments assistant | 3k (4k) | $83 | within |
| Support agent | 41k (8k) | $5,460 | over |
| Lending pre-check | 18k (20k) | $459 | within |
| AML alert reviewer | 310k (400k) | $1,980 | within |
| Fraud triage | 1.2k (2k) | $360 | within |
| Transaction reporting | 4.1M a run (5M) | $306 | within, the wrong way |
| Marketing summariser | 22k (none) | $672 | no mandate |

Three of these are the point.

!shot pmo-support.webp | images/ | The support agent: five times its mandate per ticket, and nothing in its purpose needs it. | screenshot

- **The support agent is waste.** Forty-one thousand tokens per ticket against a mandate of eight thousand. Tallyline found why: it loads the whole sixty-page help centre into every turn, its threads run past thirty turns, and its fixed instructions are never cached. Done the way the mandate describes, three help sections, closed threads, cached instructions, it costs about $927 a month instead of $5,460.
- **The AML reviewer is expensive, and right.** At $1.32 an alert it is the most expensive agent per task, because it reads twelve months of transactions and the customer's file: that is the job, and its mandate says so. A cost tool alone would flag it. The mandate says leave the work alone, and Tallyline's finding, to cache the history it re-reads at each step, takes it from $1,980 to $743 a month with the same answer. Cache reads on Anthropic's current models cost "0.05x" the input price.
- **The marketing summariser has no mandate.** Tallyline found it in the logs; no behaviour policy names it. Nobody has said what it is for, so nobody can say whether $672 a month is right. It goes back to RiskMandate as a policy to write, with an owner.

And transaction reporting is within its tokens but run one call at a time, when its mandate expects the Batch API, which Anthropic prices at "a 50 percent discount on both input and output tokens". Half its cost, for no change in what it does.

Together: about $9,320 a month, to about $3,400, and every cut has a reason a business owner can read.

## How the two products fit {#fit}

!shot pmo-integration.webp | images/ | How it fits: mandates one way, findings the other, and the logs stay in the customer's environment. | screenshot

1. **The customer writes or confirms each agent's policy,** with cost rows, in RiskMandate.
2. **RiskMandate publishes the mandates** through an API Tallyline reads. No logs go to RiskMandate.
3. **Tallyline reads the logs** in the customer's environment, with permission.
4. **Tallyline compares usage with each mandate** and gives every agent a verdict, with findings and savings.
5. **Findings come back as evidence.** A cost row moves from an Expectation to a measured row; a repeated breach becomes a control, such as a budget the gateway enforces; and the evidence is what an [insurer would price](/articles/a-payout-for-every-row.html).
6. **Agents with no mandate come back to RiskMandate** as policies to write.

The handover is small on purpose: a mandate file per agent one way, a finding per agent the other. Both are in the vault, as JSON.

## Go to market, together {#gtm}

The value proposition is one question: do you understand the cost of your agents? The answer comes powered by RiskMandate and the partner.

- **First 30 days:** one design partner customer with agents in production and a cost question; run the joint report on a month of their logs.
- **Days 30 to 60:** publish the case study, with their permission, and run a session for heads of platform and FinOps.
- **Days 60 to 90:** a packaged offer: a two-week review at a fixed price, then a monthly service per agent, shared between the partners.

The prices in the vault are marked illustrative. This is the first integration of [the RiskMandate partner programme](/articles/the-riskmandate-partner-programme.html), which describes what any partner gets and gives.

## What this does not claim {#limits}

- **Tallyline and Pellbridge are invented,** and so is the month of usage; the prices are Anthropic's published rates on 3 November 2026.
- **The savings assume the findings work as described;** a real review measures them.
- **There is no published figure for how much AI spend is wasted** that I could verify, so none is used.
- **The integration is a design;** neither product has been connected.
- **Model tokenisers change:** Anthropic notes that its newer models produce "approximately 30% more tokens for the same text".

## Where this comes from {#sources}

My conversation of 3 November 2026, in this site's repository under `admin/notes/2026-11-03__partner-programme/`. [Anthropic's pricing](https://platform.claude.com/docs/en/about-claude/pricing). [The FinOps Foundation on what FinOps is](https://www.finops.org/introduction/what-is-finops/) and [FinOps for AI](https://www.finops.org/wg/finops-for-ai-overview/); [the State of FinOps 2026](https://data.finops.org/). [Menlo Ventures, the state of generative AI in the enterprise](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/). The worked example: [the vault](https://dev.vault.sgraph.ai/#sgit_public_read_d199351130f22f55c1a25ab849266a962163b136b218729f95d316255988244a%3Arxxgqjen), `sgit clone sgit_public_read_d199351130f22f55c1a25ab849266a962163b136b218729f95d316255988244a:rxxgqjen cost-of-your-agents`. All read 3 November 2026.
