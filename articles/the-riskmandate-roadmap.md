# The RiskMandate roadmap: policies, understand, contain, manage, accelerate, then insurance, and a home for the Agent Behaviour Policy outside RiskMandate, sgit.ai

> This is a proposed roadmap for RiskMandate, and two decisions. The first is about governance. On 8 October RiskMandate's two founders decided to propose the Agent Behaviour Policy to OWASP as an open project, because a description of what an agent can do should not belong to the company that sells it. It was not the right fit for an OWASP project, so the policy will move to the Open Security Summit instead, as a hosted project: the point is the same, that the policy is governed outside the RiskMandate organisation, which today is mostly The Cyber Boardroom. The second is the roadmap: five stages of development, then insurance. Policies, then understand, then contain, then manage, then accelerate, and then insurance. We are in the first stage: creating the policies and the flows, with our first customers, whose programme is now running at customers.riskmandate.ai. The later stages we will start as they are needed, as we get more customers and users and the offering matures. This is the plan; the stages after the first are a first reading, to be refined with the people using it.

*Source: <https://newsroom.sgit.ai/articles/the-riskmandate-roadmap.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The RiskMandate roadmap: policies, understand, contain, manage, accelerate, then insurance, and a home for the Agent Behaviour Policy outside RiskMandate

# The RiskMandate roadmap: policies, understand, contain, manage, accelerate, then insurance, and a home for the Agent Behaviour Policy outside RiskMandate

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-20 · [article v1.1.0, 2 versions](versions/the-riskmandate-roadmap.md) · [newsroom v0.13.3](https://newsroom.sgit.ai/admin/versions.html) · riskmandateagent-behaviour-policyroadmapgovernanceopen-sourcearticle

***Abstract:** This is a proposed roadmap for RiskMandate, and two decisions. The first is about governance. On 8 October RiskMandate's two founders decided to propose the Agent Behaviour Policy to OWASP as an open project, because a description of what an agent can do should not belong to the company that sells it. It was not the right fit for an OWASP project, so the policy will move to the Open Security Summit instead, as a hosted project: the point is the same, that the policy is governed outside the RiskMandate organisation, which today is mostly The Cyber Boardroom. The second is the roadmap: five stages of development, then insurance. Policies, then understand, then contain, then manage, then accelerate, and then insurance. We are in the first stage: creating the policies and the flows, with our first customers, whose programme is now running at customers.riskmandate.ai. The later stages we will start as they are needed, as we get more customers and users and the offering matures. This is the plan; the stages after the first are a first reading, to be refined with the people using it.*

The RiskMandate roadmap: five stages of development, policies, understand, contain, manage and accelerate, then insurance. We are in the first, writing the policies and the flows with our first customers.

## In short

- **The policy needs a home outside RiskMandate.** Governed by more people than us.
- **It will be hosted by the Open Security Summit.** OWASP was not the right fit.
- **The roadmap has five stages, then insurance.** Policies, understand, contain, manage, accelerate.
- **We are in the first stage.** Creating the policies and the flows.
- **Our first customers are where it happens.** Their programme is live at customers.riskmandate.ai.
- **Later stages start as they are needed.** With more customers, more users and a more mature offering.
- **Everything stays open.** CC BY 4.0 for the policies and pages, Apache 2.0 for the code.

## A home outside RiskMandate

On 8 October, RiskMandate's two founders decided to propose the Agent Behaviour Policy to OWASP as an open project, with RiskMandate as its sponsor. The reason is on [the proposal's page](https://riskmandate.ai/owasp/): "A description of what an agent can do should not belong to the company that sells it." A format that the buyer, the vendor, the reviewer and the insurer all write in has to be one that none of them owns.

It was not the right fit for an OWASP project. The reason for proposing it has not changed, so we are going to give it another home: the [Open Security Summit](agent-behaviour-policies-move-to-the-open-security-summit.md), as its first hosted project. What that means, fundamentally, is that we want the governance of the Agent Behaviour Policy to happen outside the RiskMandate organisation, which at the moment is predominantly [The Cyber Boardroom](https://thecyberboardroom.com/). The vocabulary, the schema and the published policies are already open, under CC BY 4.0 and Apache 2.0, at [abp.sgit.ai](https://abp.sgit.ai/); the new home is where decisions about them will be made, by people who are not only us.

RiskMandate stays what it is: a company that sells services on the policy, from the pack to a policy a professional signs, as [its pricing page](https://riskmandate.ai/pricing.html) sets out. The line between the two is the one the OWASP proposal drew, and it still holds: the policy is shared; the work done with it can be sold.

## Five stages, then insurance

The roadmap maps five stages of development, and then insurance. Each stage builds on the one before. The meanings below are how I read each stage today; they will be refined with the people who use them.

- **Policies.** Write the Agent Behaviour Policy for each agent: what it can reach (the grant), what it was authorised to do (the mandate), the gap between them (the delta), and what stands in the way (the barrier). This is the stage we are in.
- **Understand.** See what each agent actually does, measured against its policy: its receipts, its footprint against its blast radius, and its near misses, the rows only the model kept.
- **Contain.** Move each rule out of the agent's reach, from a sentence in the prompt, to a hook in its harness, to a system the agent cannot touch. [The Pellbridge agents](inside-the-pellbridge-agents.md) showed the same day with 16 breaches and with none, depending only on where the rules were kept.
- **Manage.** A holder for every rule, a decision for every gap, and a test pack run on every change of model or policy. This is the work in [every risk is already accepted](https://newsroom.sgit.ai/articles/every-risk-is-already-accepted.html), applied to agents.
- **Accelerate.** With the rules kept and managed, give agents more to do, and faster. Control is what makes it safe to say yes.
- **Insurance.** Evidence of what contains each agent is what an insurer needs to cover it. It is the top of the ladder RiskMandate already publishes, from the [policy](https://riskmandate.ai/), to a [licence to operate](https://riskmandate.ai/licence-to-operate.html), to [insurable](https://riskmandate.ai/insurance.html).

## Where we are: the policies

If you look at the execution, we are in stage one: really sorting out the policies, and the flows that produce them. That is what [our first customers](our-first-customers.md) are for, and their programme now runs as a site of its own, at [customers.riskmandate.ai](https://customers.riskmandate.ai/).

Its milestones are the first stage, step by step. A customer starts with credit and names one agent; then its grant is measured, its mandate is written in the customer's own words, and the delta gives a first finding. Then comes the part of the policy the agent's harness can hold as hooks, and finally the usage moment: the point where the policy became worth something to that customer, and what a fair price would be. Seven steps in all, from S0 to S6, each done when the thing it names exists.

On its own count, at v0.1.1, the first batch has three customers, two of them started, and 3 of the 21 milestone steps done. No first policy has been written yet, and none of the £10 of credit has been used. That is where a roadmap should start: with the numbers on the page.

## The later stages, as they are needed

The stages after the first are not a schedule. We will start each one as we get more customers and more users, and as the offering matures: when a customer needs to understand what their agents did, or to contain one, that is when that stage begins, with them. Some of the pieces already exist in what we have published, from the hooks and the test packs to the insurance pages. What the roadmap adds is the order, and the name of the plan.

## What this does not claim

- **The hosting is proposed.** The charter and the steering group come first.
- **OWASP has not endorsed anything.** The project was not a fit for it.
- **The stage meanings are a first reading.** Only the first stage is under way.
- **The roadmap has no dates.** Each stage starts when customers need it.
- **The counts are the customer site's own.** Read from it on 20 October 2026.

## Where this comes from

A voice memo of 20 October 2026. RiskMandate's [OWASP proposal page](https://riskmandate.ai/owasp/), its [pricing](https://riskmandate.ai/pricing.html), [licence to operate](https://riskmandate.ai/licence-to-operate.html) and [insurance](https://riskmandate.ai/insurance.html) pages, and [customers.riskmandate.ai](https://customers.riskmandate.ai/) at v0.1.1, its home page and [milestones](https://customers.riskmandate.ai/milestones/), read the same day. Related: [our first customers](our-first-customers.md), [inside the Pellbridge agents](inside-the-pellbridge-agents.md), [a leak without breaking the policy](a-leak-without-breaking-the-policy.md), [free to copy, paid at the source](free-to-copy-paid-at-the-source.md). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Agents & policyStartups & strategy[This article as a graph →](graphs.md#the-riskmandate-roadmap)

### Builds on

- [Agent Behaviour Policies move to the Open Security Summit: the first hosted project of a community interest company, with RiskMandate as a founding contributor](agent-behaviour-policies-move-to-the-open-security-summit.md) The Agent Behaviour Policy moves to the Open Security Summit CIC as its first hosted project, with a charter and an independent steering majority to come.
- [Inside the Pellbridge agents: six behaviour policies with the FCA's four elements filled in, one day of their work replayed through the gate, and the files that make it](inside-the-pellbridge-agents.md) Six invented bank agents with the FCA's four elements filled in, one day replayed through the gate: every incident came from a gap row.
- [Our first customers: an early access programme for Agent Behaviour Policies, with credit to spend, a start-here site, daily follow-up, and a list for the next batch](our-first-customers.md) Agent Behaviour Policies move to execution: a first batch of customers with credit, a start-here site, daily follow-up, and a list for the next batch.
- [Can a key leak without breaking the policy? Told, checked, never given: three levels for secrets and personal data, and a hook we tested against nine leaks](a-leak-without-breaking-the-policy.md) A key can leak through an allowed action. Told, checked, never given: a hook tested on nine leaks, four experimental rules, and a real sweep.
- [Free to copy, paid at the source: why an official website can charge per use for open policies and hooks, and why we will have them reviewed, audited and signed](free-to-copy-paid-at-the-source.md) Open policies and hooks, free to copy, can still earn per use at the official source, if others review them and we sign them.

### Continued by

- [Agent Behaviour Policies move to the Open Security Summit: the first hosted project of a community interest company, with RiskMandate as a founding contributor](agent-behaviour-policies-move-to-the-open-security-summit.md) The Agent Behaviour Policy moves to the Open Security Summit CIC as its first hosted project, with a charter and an independent steering majority to come.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 230 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=230)

**Posting this article on LinkedIn?** The cover is [the-riskmandate-roadmap.jpg](banners/the-riskmandate-roadmap.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-riskmandate-roadmap.html)*
