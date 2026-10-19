---
title: A trusted framework for agentic finance: a reply to the FCA's Jessica Rusu, how our open behaviour policies line up with it, and a payments agent's policy with identity, delegated authority, accountability and execution filled in
date: 2026-10-19
author: Dinis Cruz
author_url: about/index.html
summary: Jessica Rusu, the FCA's chief data, information and intelligence officer, said today that the FCA will work with industry, other regulators and frontier labs on a trusted framework for agentic finance, with clear approaches to agent identity, delegated authority, accountability and execution. Most of what she asks of firms is something we have been writing about and publishing openly here: Agent Behaviour Policies that put what an agent can do beside what it may do, a holder for every risk with a chain to the board, rules kept by something the agent cannot reach, breaks and near misses reported, and policies as graphs. This is a crosswalk from her points to that work, and a worked example: the behaviour policy of an invented bank's payments agent, with all four elements filled in, twelve rows, three of them gaps, each gap with a holder and a decision. It is all CC BY. The FCA, or anyone building the framework, could adopt it, or write their own; if theirs is a graph too, the two can be connected with edges, without either side adopting the other's schema.
version: v0.12.139
license: https://creativecommons.org/licenses/by/4.0/
tags: agents, agent-behaviour-policy, regulation, finance, accountability, graphs, article
status: published
---

!shot fc-crosswalk.webp | images/ | The FCA's points from the speech, against our open work that covers the same ground. Blue: the four elements of the framework the FCA proposes. Teal: the governance themes. Orange: how the two sides could connect. Aligned with, not endorsed by. | comparison

## In short {#in-short}

- **The FCA is building a framework for agentic finance.** Agent identity, delegated authority, accountability and execution.
- **Most of it is what we have been publishing.** Behaviour policies, risk acceptance, enforcement levels, near misses, graphs.
- **Delegated authority is the gap between can and may.** That is what an Agent Behaviour Policy writes down.
- **Accountability needs a holder per rule.** With a chain to the board, as in our risk acceptance work.
- **Execution is who keeps each rule.** The prompt, a hook, or a system the agent cannot reach.
- **A worked example: a payments agent.** Twelve rows, all four elements filled in, three gaps with holders.
- **It is open, CC BY.** Adopt it, or write your own as a graph, and the two connect.

## What the FCA said {#speech}

Jessica Rusu, the FCA's chief data, information and intelligence officer, spoke today at Bloomberg's UK Policy Series, under the title [Building the future of finance in the age of AI](https://www.fca.org.uk/news/speeches/building-future-finance-age-ai). The FCA's page says it is the drafted version and may differ from what was delivered; the quotations below are from that page.

Her starting point is that "Adoption is not coming. It is here." A joint survey with the Bank of England, due next week, shows 86% of firms using AI. The FCA is putting six of the seven recommendations of the Mills Review into live work, and she was clear about the style: "Our response to the review is not to consult, study and report progress."

She shared good and poor practice under three themes: putting the consumer first, knowing who is accountable, and operational resilience. On accountability, firms need "clear accountability, risk-based controls, human oversight, escalation triggers, and senior managers personally accountable for AI systems", and some firms "retrofit governance after technology has already been deployed". Her verdict on that: "That is the wrong way around." On resilience: stress-test, plan for failure, keep fallbacks, and understand supplier concentration, "including reliance on a single model".

Then agents. Incident reporting "must extend to significant AI failures and near-misses". Assurance has to change, because "A system that is safe at deployment may behave differently at scale, under stress or as the models beneath it change. Agentic systems therefore require continuous, conditional assurance." And the commitment I am replying to: "The FCA will work with industry, fellow regulators and frontier labs to develop a trusted framework for agentic finance, including clear approaches to agent identity, delegated authority, accountability and execution."

She ended with "Let's build it together." This is my contribution to that.

## Four elements we have been writing about {#four}

Reading the speech, I recognised almost every point. Not because anyone copied anything, but because the problem forces the same answers on anyone who looks at it closely.

- **Delegated authority** is the gap between what an agent can do and what it may do. That is the core of an [Agent Behaviour Policy](/articles/what-can-your-agent-reach.html): the grant (everything it can do, measured), the mandate (what it was authorised to do), the delta between them, and the barrier, what actually stands in the way of each capability. It is published openly at [abp.sgit.ai](https://abp.sgit.ai/), under CC BY.
- **Execution** is how each rule is kept. In [governs, enforces, attests](/articles/governs-enforces-attests.html) I described three levels: in the prompt, which is a hope; in hooks, which are deterministic but sit on the agent's own machine; or by a third-party system that does the blocking, which is the level we recommend. The test, from the ABP: "A control bounds a grant only if it is enforced by something the grant does not include." [Policy as code needs a policy first](/articles/policy-as-code-needs-a-policy-first.html) adds the question most frameworks miss: for every rule that is code, who can change that code.
- **Accountability** is a holder for every rule. Our work on [risk acceptance](/articles/every-risk-is-already-accepted.html) says every risk is already being carried, so the only questions are who has accepted it and until when; every holder has a boss, and every path ends at the board. [The policy draws the liability line](/articles/the-policy-draws-the-liability-line.html) is the same idea for agents: without a written policy, nobody can point to what the agent was told not to do.
- **Agent identity** is the one we have written least about, and the speech is right to put it first. In the ABP it is implicit: a policy is for one agent in one deployment. The attestation layer in [governs, enforces, attests](/articles/governs-enforces-attests.html) makes it explicit: what was assured, at which policy version, signed so a third party can check it without taking the operator's word.

The themes line up too. Governance written before deployment is [a policy beside the prompt](/articles/a-policy-beside-the-prompt.html), which also proposes a breach report the same day for every broken row and every near miss. Continuous assurance is a versioned policy whose rows are re-tested, with a receipt for every decision. Resilience and single points of failure are graph questions, which the [Thistlewood twin](/articles/ten-questions-one-graph.html) answers for an invented retailer.

## A worked example: a payments agent {#example}

The speech mentions the AI Lab seeing firms build "agent-led payments", so here is one. An invented bank deploys an agent that pays bills for one customer: it reads their accounts, pays existing payees, and asks the customer before anything unusual. Everything below is invented and illustrative; the vocabulary is the ABP's.

!shot fc-abp-rows.webp | images/ | Delegated authority and execution: the payments agent's twelve rows. For each capability, can it (grant), may it (mandate), what stands in the way (barrier), who keeps the rule, and who holds it. Three rows, in orange, are the delta. | concept

### Delegated authority: grant, mandate, delta {#authority}

The customer delegated a narrow job. The agent may read their own accounts and pay existing payees up to £250 on its own. Above £250, or to a new payee, it needs the customer to confirm in the bank's app. It must not pay more than £1,000 a month, open credit, act for another customer, or change its own limits. It must route the customer to a person when a vulnerability signal appears, which is the FCA's own example of good practice.

What it can do, measured, is larger. It can change standing orders, and the approval that should guard that is a flag in the agent's own profile, which its token can edit. It can pay a crypto exchange, and the only thing against it is a sentence in the system prompt. And it can write anything, including what reads as investment advice, which the bank is not offering through this agent; an output check catches most of it and hands the conversation to an adviser, but it can miss.

Those three are the delta. Nine rows are clean: either the agent cannot do the thing at all, or something outside its reach keeps the limit.

### Execution: who keeps each rule {#execution}

Eight of the twelve rows are kept by systems the agent cannot reach: the payment platform checks limits and asks the customer, the API gateway scopes reads, the identity service binds the token to one customer. Two are kept by hooks in the bank's harness. One is kept by a setting the agent could flip, and one by the prompt. In ABP terms, only the first eight are boundaries; a setting is not a control, and an expectation is a hope.

Every decision the platform makes, allow, ask or deny, writes a receipt with the row and the policy version, kept in a vault, encrypted and versioned. The rows are also a test pack. They run on every model change, every policy change and every week, and a failed row stops the release. That is my reading of "continuous, conditional assurance": not a review at deployment, but a policy that is re-proven every time something under it moves.

!shot fc-abp-frame.webp | images/ | Around the rows: the agent's identity, the chain of holders to the board, and how the rules are kept, recorded, re-tested and failed safely. Identity and holders are not in the ABP today; they are proposed here. | architecture

### Agent identity {#identity}

The identity block says who the agent is and on whose behalf it acts: its name and version; the firm that deploys it, under its own authorisation; the customer, by consent given in the app, for 90 days, revocable; the model provider and version, so that a change re-runs the tests; a 15-minute token from the bank's identity service bound to this customer and this policy; and the policy version with its hash. A counterparty, another agent, or a supervisor sees a signed attestation of that block, not the agent's own claim about itself.

### Accountability {#accountability}

Every row has one holder. The head of payments holds six of them, the product owner two, and the heads of advice, support, lending and operations one each. Each holder has a chain to the board through the senior manager whose responsibilities cover retail payments. The three gaps each get a decision from their holder, with a door and an interval: the standing-order flag is accepted for 30 days while it moves into the platform; the crypto block is funded, to land within 60 days; the advice check stays, and every miss is reported as a near miss. Nobody accepts on somebody else's behalf, and their boss sees each decision arrive.

Every broken row and every near miss goes to its holder the same day; the significant ones go into the firm's incident reporting, which is where the speech says they belong. If the model or its provider is down, the agent stops and the customer pays in the app, and operations can revoke every agent token in one action. No payment depends on the agent being there.

### The same policy, as data {#data}

Here is one row with the frame around it. The `capability`, `reach`, `mandate` and `barrier` fields are the ones our published policies use today; `identity`, `kept_by`, `holder` and `decision` are proposed here, to carry the FCA's four elements.

```json
{
  "policy": "Agent Behaviour Policy",
  "version": "1.4",
  "identity": {
    "agent": "payments-assistant 3.2",
    "deployed_by": "the bank",
    "acts_for": { "customer": "one", "consent": "in the app", "days": 90, "revocable": true },
    "model": { "provider": "recorded", "version": "recorded", "on_change": "re-run the test pack" },
    "credential": "15-minute token, bound to this customer and this policy version"
  },
  "accountability": {
    "owner": "product owner",
    "chain": ["product owner", "head of payments", "senior manager, retail payments", "the board"],
    "report": "every broken row and near miss to its holder the same day"
  },
  "rows": [
    {
      "capability": "change.standing_order",
      "reach": true,
      "mandate": "approval",
      "barrier": "setting: the approval flag is in the agent's own profile",
      "kept_by": "the agent's account",
      "holder": "head of payments",
      "decision": { "door": "accept", "days": 30, "while": "the flag moves to the payment platform" }
    }
  ]
}
```

## Adopt it, or write your own as a graph {#graphs}

All of this is open. The ABP, its vocabulary and its examples are at [abp.sgit.ai](https://abp.sgit.ai/) under CC BY, and every article here carries the same licence. I [open source what I build](/articles/open-source-so-you-keep-it.html) so that it can be used, and this is a case where I would like it to be.

So the FCA, or anyone working on the framework with them, could adopt it as it is, or take parts of it. Or they could write their own, in their own words. That is fine too, as long as it is a graph. The FCA is already moving that way: the speech mentions the Handbook API, launched in August, which gives firms machine-readable rules, and work on machine-readable data collection. Once the regulator's expectations and a firm's policies are both graphs, nobody has to adopt anybody's schema. The work is the edges: this element of the framework is shown by that identity block, is bounded by these rows, is held by that person, is kept by that system. That is what [fractal semantic graphs](https://sgit.ai/articles/introducing-fractal-semantic-graphs.html) are for, and why I think [the graph companies](/articles/the-graph-companies.html) will include the regulated ones.

!shot fc-connect.webp | images/ | Two policy graphs connected by edges. On the left, a regulator's graph in its own vocabulary, hypothetical here; on the right, a firm's behaviour policies. Neither adopts the other's schema; the edges do the work. | concept

It also works in the other direction. The FCA is building its own agents, including a market first responder agent. Those agents could carry a behaviour policy too, published, so that firms can see what the regulator's agents can reach and what they are for.

## What this does not claim {#limits}

- **The FCA has not endorsed any of this.** The crosswalk is my reading of a speech; "aligned with" is my claim, not theirs.
- **The speech is the drafted version.** The page says it may differ from what was delivered.
- **The bank and its agent are invented.** The rows, limits, holders and numbers are illustrative.
- **Two fields are proposals.** Identity and holders are not in the ABP today; kept by and decision are new here too.
- **The framework does not exist yet.** The FCA said it will develop it with others; this is offered into that work.

## Where this comes from {#sources}

Jessica Rusu, [Building the future of finance in the age of AI](https://www.fca.org.uk/news/speeches/building-future-finance-age-ai), FCA, 19 October 2026, drafted version, read that day; the quotations are from it. The ABP: [abp.sgit.ai](https://abp.sgit.ai/), version 0.12.1, read 19 October 2026, including the barrier model and the quoted test. Our earlier work: [what can your agent reach](/articles/what-can-your-agent-reach.html), [governs, enforces, attests](/articles/governs-enforces-attests.html), [policy as code needs a policy first](/articles/policy-as-code-needs-a-policy-first.html), [a policy beside the prompt](/articles/a-policy-beside-the-prompt.html), [the policy draws the liability line](/articles/the-policy-draws-the-liability-line.html), [every risk is already accepted](/articles/every-risk-is-already-accepted.html), [ten questions, one graph](/articles/ten-questions-one-graph.html) and [the graph companies](/articles/the-graph-companies.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
