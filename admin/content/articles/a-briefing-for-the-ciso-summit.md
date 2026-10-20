---
title: A briefing for the WestCap CISO Summit: what RiskMandate and Agent Behaviour Policies are, said for each kind of person in the room, where we add value, and what to read next
date: 2026-10-20
author: Dinis Cruz
author_url: about/index.html
summary: My business partner is at the WestCap CISO Summit in New York this week, from 20 to 22 October, where security leaders, investors and founders meet. This page does two jobs. It is a briefing for him, and it is a place for the people he meets to come and see what we do. The summit's main day has panels on securing AI use and AI governance, on preparing for an AI attack, and on using AI to secure a company. Our work sits right across them. An Agent Behaviour Policy is a written description, for one agent in one deployment, of everything it can do, what it was authorised to do, the difference between the two, and what actually stands in the way. RiskMandate is where we sell one, from £10 for the pack to £1,500 for one a professional signs, with early users helped at no cost in exchange for telling us where it is wrong. The idea at the centre is one sentence: a control bounds a grant only if it is enforced by something the grant does not include. Below, that idea is said six ways, for CISOs, for AI governance and audit, for incident response and red teams, for AI-for-defence vendors, for investors and for founders, each with the articles and vaults to read first. Everything here is open, under CC BY 4.0.
version: v0.12.155
license: https://creativecommons.org/licenses/by/4.0/
tags: agents, agent-behaviour-policy, riskmandate, ciso, security, governance, article
status: published
---

!shot wc-rooms.webp | images/ | One idea, six rooms: the same point said for each kind of person at the summit, with the article to read first. | concept

## In short {#in-short}

- **The summit is about modern defence, and AI runs through it.** Governance, AI attacks, AI for defence.
- **An Agent Behaviour Policy writes down what an agent can do and may do.** And what actually stands in the way.
- **Only a rule kept out of the agent's reach is a control.** That one sentence is the test.
- **RiskMandate sells the policy for the agent you run.** Four levels, £10 to £1,500, paid once.
- **Early users get help at no cost.** In exchange for telling us where it is wrong.
- **The idea, said for six kinds of person.** With the articles and vaults to read first.
- **Everything is open.** Policies, vocabulary and code, under CC BY 4.0 and Apache 2.0.

## The summit {#summit}

The [WestCap CISO Summit](https://luma.com/rym6b377) runs from 20 to 22 October in New York, where, in the organisers' words, "security leaders, investors and founders meet to share the ideas shaping modern defense". Tuesday is for WestCap and its portfolio companies, on business-risk alignment, business process mapping and operational security. Wednesday is the main event, at Chelsea Piers, with five panels: rewiring the hacker pipeline; securing AI use and AI governance; preparing for an AI attack; using AI to secure your company; and industrialised abuse at mobile scale. Thursday is a startup Shark Tank, where six cybersecurity startups pitch.

Three of Wednesday's five panels are about AI, and the companies on them are a good map of the room: compliance and attestation (Drata, Schellman), data and AI security (Bedrock Data), supply chain security (Socket), risk consultancy and incident response (Control Risks, Kroll, Sygnia), offensive security (Bishop Fox), AI-native defence (Nebulock), application delivery and security (F5), and a model provider (OpenAI).

## What we do, in three sentences {#what}

An Agent Behaviour Policy is, in the words of [abp.sgit.ai](https://abp.sgit.ai/), "a written description, for one agent in one deployment, of everything it can do, what it was authorised to do, the difference between the two, and what actually stands in the way". RiskMandate, at [riskmandate.ai](https://riskmandate.ai/), writes that policy for the agent you actually run: "Give agents access. Not free rein." The test at the centre of it is one sentence: "A control bounds a grant only if it is enforced by something the grant does not include."

The words matter. The grant is everything the agent can do, measured. The mandate is what it was authorised to do, asked of the person who deployed it. The delta is the difference, derived, never written by hand. The barrier is what stands in the way of each capability: nothing, a sentence in the prompt, a setting the agent's own account can change, or a boundary kept by a system out of its reach. Only the last is a control. The site puts the point well: "Your agent can do three hundred and forty things is a shrug. Your agent can do three hundred and forty things and you authorised twelve is a finding."

## Said for each kind of person {#rooms}

### CISOs and security leaders {#cisos}

The question is the one they already have to answer: what can each agent reach, and what actually stops it? A policy answers it per agent, in one document the CEO, the CTO and the CISO can all stand behind. Start with [what can your agent reach?](/articles/what-can-your-agent-reach.html), the explainer written for the person who has to decide. Then [hope or enforcement](/articles/hope-or-enforcement.html), one agent built three ways, with [its vault](https://sgit.ai/demos/vaults/hope-or-enforcement/index.html); [every risk is already accepted](/articles/every-risk-is-already-accepted.html), with the [risk acceptance vault](https://sgit.ai/demos/vaults/risk-acceptance/index.html); and [who are you protecting against?](/articles/who-are-you-protecting-against.html), six threat tiers, with [its vault](https://sgit.ai/demos/vaults/threat-sized-security/index.html). [Ten questions, one graph](/articles/ten-questions-one-graph.html) takes Phil Venables' ten questions for a CISO's management tool and answers them as a graph, with [the Thistlewood twin](https://newsroom.sgit.ai/demos/vaults/thistlewood-twin/index.html).

### AI governance, compliance and audit {#governance}

For the people who attest: an agent's logs are a self-report, and a rule the agent can change is a setting, not a control. [Your agent's logs are a self-report](/articles/your-agents-logs-are-a-self-report.html) is our answer to an ISO 42001 lead auditor. [Four frameworks, one agent](/articles/four-frameworks-one-agent.html) maps the OECD principles, the NIST AI RMF, Japan's guidelines and the EU AI Act onto one agent's policy. [Policy as code needs a policy first](/articles/policy-as-code-needs-a-policy-first.html) is about who can change the code that keeps a rule. And this week's [trusted framework for agentic finance](/articles/a-trusted-framework-for-agentic-finance.html) lines our work up with the four elements the FCA has named: agent identity, delegated authority, accountability and execution, with [the Pellbridge agents](https://newsroom.sgit.ai/demos/vaults/pellbridge-agents/index.html), six bank agents replayed through one day with and without a policy.

### Incident response and red teams {#ir}

For the people who arrive afterwards: the incidents we have mapped are reach beyond mandate, and the policy is the map of where to look. [Attacks rewritten as mandates](/articles/attacks-rewritten-as-mandates.html) takes a published list of 28 supply-chain incidents and rewrites each one that way. [Footprint and blast radius](/articles/footprint-and-blast-radius.html) separates what an agent touched from what it could have, and [what each vendor's hooks can see, stop and change](/articles/agent-hooks-october-2026.html) is the field guide to where an agent can be stopped. For skills and plugins, [a skill behaviour policy](/articles/skill-behaviour-policy.html).

### AI for defence {#defence}

For the companies building agents to defend: those agents have a grant too, and a lot of it. [A policy beside the prompt](/articles/a-policy-beside-the-prompt.html) proposes that every agent takes a behaviour policy as an input, next to its prompt, which the vendor accepts and enforces as far as it can. [Are hooks the sweet spot?](/articles/are-hooks-the-sweet-spot.html) walks rules out of the prompt and into hooks, one by one, and [three policies for an agent](/articles/three-policies-for-an-agent.html) separates behaviour, decisions and workflows, with [the Northstar twin](https://newsroom.sgit.ai/demos/vaults/northstar-twin/index.html).

### Investors {#investors}

For the people deciding where the money goes: liability needs a line, and the line is what each agent was told not to do, written down, and what keeps it. [The policy draws the liability line](/articles/the-policy-draws-the-liability-line.html) makes the case, and [ten questions about RiskMandate](/articles/riskmandate-ten-questions.html) answers the questions an investor asks, from what stops a big platform absorbing it to who is liable.

### Founders {#founders}

For the people pitching on Thursday: [can you sell it?](/articles/can-you-sell-it.html) is my advice to start selling what you have now, however rough, because selling is how you learn. And [our first customers](/articles/our-first-customers.html) is what we are doing ourselves this month.

## Where we add value {#value}

Most of the room sells something that acts at runtime: a gateway, an agent, a scanner, an audit. An Agent Behaviour Policy is what those are configured from. In abp.sgit.ai's words: "Not a guardrail. It is what guardrails are compiled from." So it sits alongside them, not against them: it tells a gateway which rules to keep, an auditor what to test, an incident responder where to look, and an insurer what contains the agent. It describes and does not judge, and, again from the site, "A policy cannot be dangerous. A deployment can."

It is also open. The vocabulary and the policies are CC BY 4.0, and the code is Apache 2.0, so anyone in the room can use it, including in their own products.

## Next steps {#next}

- **Read the explainer.** [What can your agent reach?](/articles/what-can-your-agent-reach.html), then one article from your section above.
- **Pick one agent.** The policy is per agent, per deployment; one is enough to start.
- **Join early access.** At [riskmandate.ai](https://riskmandate.ai/early-access.html), early users name an agent, and we build its policy and correct it with them, at no cost, "in exchange for telling us where it is wrong".
- **Or buy a level.** The [pricing page](https://riskmandate.ai/pricing.html) has four, from £10 for the pack to £1,500 for one a professional signs, per agent, per deployment, paid once.
- **Talk to us.** Through [the contact page](https://riskmandate.ai/contact.html), or to my business partner, in New York this week.

## What this does not claim {#limits}

- **We are not part of the summit's programme.** This is a briefing, not a session.
- **No speaker is quoted.** The panels and companies are from the public agenda.
- **The fit is our reading.** Each company's own site says what it does.
- **Two of the four levels had not been sold by mid-September.** The pricing page says so.
- **The vaults are illustrative.** Their banks, retailers and numbers are invented.

## Where this comes from {#sources}

The [summit's page](https://luma.com/rym6b377), read on 20 October 2026. [riskmandate.ai](https://riskmandate.ai/) and its [pricing](https://riskmandate.ai/pricing.html) and [early access](https://riskmandate.ai/early-access.html) pages, and [abp.sgit.ai](https://abp.sgit.ai/), read the same day. The articles and vaults linked in each section. Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
