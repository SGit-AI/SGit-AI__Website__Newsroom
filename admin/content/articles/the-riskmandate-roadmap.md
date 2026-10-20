---
title: The RiskMandate roadmap: policies, understand, contain, manage, accelerate, then insurance, and a foundation to govern the Agent Behaviour Policy
date: 2026-10-20
author: Dinis Cruz
author_url: about/index.html
summary: This is a proposed roadmap for RiskMandate, and two decisions. The first is about governance. On 8 October RiskMandate's two founders decided to propose the Agent Behaviour Policy to OWASP as an open project, because a description of what an agent can do should not belong to the company that sells it. OWASP has said no. So we will set up a foundation for it instead: the point is the same, that the policy is governed outside the RiskMandate organisation, which today is mostly The Cyber Boardroom. The second is the roadmap: five stages of development, then insurance. Policies, then understand, then contain, then manage, then accelerate, and then insurance. We are in the first stage: creating the policies and the flows, with our first customers, whose programme is now running at customers.riskmandate.ai. The later stages we will start as they are needed, as we get more customers and users and the offering matures. This is the plan; the stages after the first are a first reading, to be refined with the people using it.
version: v0.13.2
license: https://creativecommons.org/licenses/by/4.0/
tags: riskmandate, agent-behaviour-policy, roadmap, governance, open-source, article
status: published
---

!shot rr-roadmap.webp | images/ | The RiskMandate roadmap: five stages of development, policies, understand, contain, manage and accelerate, then insurance. We are in the first, writing the policies and the flows with our first customers. | concept

## In short {#in-short}

- **OWASP has said no to the project.** So the Agent Behaviour Policy gets a foundation instead.
- **The foundation is about governance.** The policy is governed outside the RiskMandate organisation.
- **The roadmap has five stages, then insurance.** Policies, understand, contain, manage, accelerate.
- **We are in the first stage.** Creating the policies and the flows.
- **Our first customers are where it happens.** Their programme is live at customers.riskmandate.ai.
- **Later stages start as they are needed.** With more customers, more users and a more mature offering.
- **Everything stays open.** CC BY 4.0 for the policies and pages, Apache 2.0 for the code.

## A foundation, now that OWASP has said no {#foundation}

On 8 October, RiskMandate's two founders decided to propose the Agent Behaviour Policy to OWASP as an open project, with RiskMandate as its sponsor. The reason is on [the proposal's page](https://riskmandate.ai/owasp/): "A description of what an agent can do should not belong to the company that sells it." A format that the buyer, the vendor, the reviewer and the insurer all write in has to be one that none of them owns.

OWASP has said no to the project. The reason for proposing it has not changed, so we are going to set up a foundation for it. What that means, fundamentally, is that we want the governance of the Agent Behaviour Policy to happen outside the RiskMandate organisation, which at the moment is predominantly [The Cyber Boardroom](https://thecyberboardroom.com/). The vocabulary, the schema and the published policies are already open, under CC BY 4.0 and Apache 2.0, at [abp.sgit.ai](https://abp.sgit.ai/); the foundation is where decisions about them will be made, by people who are not only us.

RiskMandate stays what it is: a company that sells services on the policy, from the pack to a policy a professional signs, as [its pricing page](https://riskmandate.ai/pricing.html) sets out. The line between the two is the one the OWASP proposal drew, and it still holds: the policy is shared; the work done with it can be sold.

## Five stages, then insurance {#roadmap}

The roadmap maps five stages of development, and then insurance. Each stage builds on the one before. The meanings below are how I read each stage today; they will be refined with the people who use them.

- **Policies.** Write the Agent Behaviour Policy for each agent: what it can reach (the grant), what it was authorised to do (the mandate), the gap between them (the delta), and what stands in the way (the barrier). This is the stage we are in.
- **Understand.** See what each agent actually does, measured against its policy: its receipts, its footprint against its blast radius, and its near misses, the rows only the model kept.
- **Contain.** Move each rule out of the agent's reach, from a sentence in the prompt, to a hook in its harness, to a system the agent cannot touch. [The Pellbridge agents](/articles/inside-the-pellbridge-agents.html) showed the same day with 16 breaches and with none, depending only on where the rules were kept.
- **Manage.** A holder for every rule, a decision for every gap, and a test pack run on every change of model or policy. This is the work in [every risk is already accepted](https://newsroom.sgit.ai/articles/every-risk-is-already-accepted.html), applied to agents.
- **Accelerate.** With the rules kept and managed, give agents more to do, and faster. Control is what makes it safe to say yes.
- **Insurance.** Evidence of what contains each agent is what an insurer needs to cover it. It is the top of the ladder RiskMandate already publishes, from the [policy](https://riskmandate.ai/), to a [licence to operate](https://riskmandate.ai/licence-to-operate.html), to [insurable](https://riskmandate.ai/insurance.html).

## Where we are: the policies {#now}

If you look at the execution, we are in stage one: really sorting out the policies, and the flows that produce them. That is what [our first customers](/articles/our-first-customers.html) are for, and their programme now runs as a site of its own, at [customers.riskmandate.ai](https://customers.riskmandate.ai/).

Its milestones are the first stage, step by step. A customer starts with credit and names one agent; then its grant is measured, its mandate is written in the customer's own words, and the delta gives a first finding. Then comes the part of the policy the agent's harness can hold as hooks, and finally the usage moment: the point where the policy became worth something to that customer, and what a fair price would be. Seven steps in all, from S0 to S6, each done when the thing it names exists.

On its own count, at v0.1.1, the first batch has three customers, two of them started, and 3 of the 21 milestone steps done. No first policy has been written yet, and none of the £10 of credit has been used. That is where a roadmap should start: with the numbers on the page.

## The later stages, as they are needed {#later}

The stages after the first are not a schedule. We will start each one as we get more customers and more users, and as the offering matures: when a customer needs to understand what their agents did, or to contain one, that is when that stage begins, with them. Some of the pieces already exist in what we have published, from the hooks and the test packs to the insurance pages. What the roadmap adds is the order, and the name of the plan.

## What this does not claim {#limits}

- **The foundation is a decision, not an entity.** It does not exist yet.
- **OWASP has not endorsed anything.** It said no to the project.
- **The stage meanings are a first reading.** Only the first stage is under way.
- **The roadmap has no dates.** Each stage starts when customers need it.
- **The counts are the customer site's own.** Read from it on 20 October 2026.

## Where this comes from {#sources}

A voice memo of 20 October 2026. RiskMandate's [OWASP proposal page](https://riskmandate.ai/owasp/), its [pricing](https://riskmandate.ai/pricing.html), [licence to operate](https://riskmandate.ai/licence-to-operate.html) and [insurance](https://riskmandate.ai/insurance.html) pages, and [customers.riskmandate.ai](https://customers.riskmandate.ai/) at v0.1.1, its home page and [milestones](https://customers.riskmandate.ai/milestones/), read the same day. Related: [our first customers](/articles/our-first-customers.html), [inside the Pellbridge agents](/articles/inside-the-pellbridge-agents.html), [a leak without breaking the policy](/articles/a-leak-without-breaking-the-policy.html), [free to copy, paid at the source](/articles/free-to-copy-paid-at-the-source.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
