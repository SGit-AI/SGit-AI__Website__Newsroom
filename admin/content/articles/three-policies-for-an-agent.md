---
title: Three policies for an agent: behaviour says what it may do, decision says who chooses, workflow says in what order
date: 2026-10-17
author: Dinis Cruz
author_url: about/index.html
summary: When something goes wrong with an agent, the question people ask is how it made that decision. A behaviour policy cannot answer it on its own, because it says what an agent may do, not who chooses at a branch point or why. This is the first of four articles on what I think the answer looks like. There are three policies, not one. The Agent Behaviour Policy, the ABP we already publish, says what an agent may do and where. An Agent Decision Policy says, at a branch point, who chooses, on what evidence, within what limits, and who to call when it is out of bounds. An Agent Workflow Policy says which steps run in what order. They meet at fixed points: a workflow transition is gated by a decision, and the decision's outcome is carried out by behaviours the ABP permits. We have been putting light decisions into behaviour policies all along, and that is fine at low zoom: the ABP's approval cell is a small decision. Zoom into one cell and it becomes a decision policy and a workflow policy of its own. Every element of all three can be defined before it can be enforced: what gets enforced, and where, depends on what is wired up, so each element carries five states, defined, implemented, enforced, observed and verified. The word "decision" matters because it is the one the business and the risk team already use.
version: v0.12.101
license: https://creativecommons.org/licenses/by/4.0/
tags: agents, agent-behaviour-policy, agent-decision-policy, agent-workflow-policy, decision-making, governance, risk, fractal-semantic-graphs, series, article
status: published
---

!shot dn-three.webp | images/ | The three policies, behaviour, decision and workflow, and one ABP row, delete.memory.project, zoomed in. | concept

!trail decision-policy

## In short {#in-short}

- **The question is how the agent decided.** A behaviour policy says what it may do; it does not say who chose, or why.
- **There are three policies.** Behaviour: what an agent may do. Decision: who chooses at a branch point, and how. Workflow: which steps, in what order.
- **They meet at fixed points.** A transition in a workflow is gated by a decision; the decision is carried out by behaviours the ABP permits.
- **Zoom in and a cell becomes a policy.** The ABP's "approval" is a small decision; zoomed in, it has a decider, evidence, limits and steps of its own.
- **Light decisions stay inline.** Most rows never need zooming. Money, people, irreversibility and business risk are what make one worth it.
- **Defined is not enforced.** Each element is defined, implemented, enforced, observed and verified, separately. The map can be complete before the wiring is.
- **"Decision" is the business's word.** It connects an agent's step to a budget, an owner and a risk appetite.

## The question people ask {#question}

When something goes wrong with a person at work, we ask what they did, and then we ask why: who made the call, what did they know, were they allowed to make it, and should they have asked someone first. With agents we mostly stop at the first question. The logs say what happened. The behaviour policy, where there is one, says what the agent was allowed to do.

Neither says how it decided. And that is the question the business, the regulator and the person on the other end will ask.

The [ABP](https://abp.sgit.ai/) we publish, which the agents on this site run under, is a behaviour policy. Its rows are capabilities with a reach and a mandate: yes, no, or approval. It is good at saying what is in bounds. It is not built to say, at a branch point, who chooses between two allowed actions, on what evidence, within what budget, and who to call when the case is outside all of them. Those are decisions, and I think they need their own policy.

## Three policies {#three}

| Policy | It answers | It holds |
|---|---|---|
| **Agent Behaviour Policy (ABP)** | What may this agent do, and where? | Capabilities, reach, mandate: yes, no or approval |
| **Agent Decision Policy** | At this branch point, who chooses, on what evidence, within what limits, and who is called when it is out of bounds? | The decider, the evidence, the envelope (budget, blast radius, reversibility), escalation, a kill switch, the sign-off and the record |
| **Agent Workflow Policy** | Which steps run, in what order? | States, transitions, and the gates between them |

They are not three layers stacked on each other. They are three views of the same work, and they meet at fixed points. **A workflow transition is gated by a decision. The decision's outcome is carried out by behaviours the ABP permits.** Take one out and the others have a hole. A workflow with no decisions in it needs little governance: it is a script. A decision with no behaviour policy under it has no limits. A behaviour policy with no workflow is a list of permissions waiting for someone to use them in the wrong order.

## Zoom into one cell {#zoom}

We have been putting decisions into behaviour policies all along, and I think that is fine at low zoom. A good example is in a page that went into Ruflo's docs today, Mondweep Chakravorty's [ABP for SGit memory checkpoints](/articles/our-first-pr-in-ruflo.html). One of its rows:

> `delete.memory.project`, reach yes, mandate **approval**.

That word "approval" is a decision in one cell. At this zoom, it is all you need to know: deleting memory is allowed, but not on the agent's own say-so. Today the row's barrier reads "Human approval is required; MVP blocks this operation", and nothing yet exists to give approval with, so [approval means stop](/articles/the-policy-guards-the-door.html#questions).

Zoom in and the cell opens into two policies of its own:

- **Its decision policy.** Who approves: the project owner, say. On what evidence: a checkpoint exists and passes its digest check. Within what envelope: one namespace, and reversible while the checkpoint is kept. Recorded where, and with what reasons.
- **Its workflow policy.** Request, verify the checkpoint, approve or refuse, delete, record.

Zoom further and each of those has cells of its own. This is the fractal shape this site uses for [code](/articles/code-review-as-a-fractal-semantic-graph.html) and for [hooks](/articles/hooks-are-kernel-code.html): the same kind of graph at every level, with more detail as you go in.

## Light decisions stay inline {#light}

Most rows never need zooming. "May this agent read the project's files?" Yes is the whole decision. A row earns its own decision policy when the choice carries one of four things:

1. **Money.** A refund, a purchase, compute that bills by the hour.
2. **People.** A customer, an employee, anyone outside who receives the result.
3. **Irreversibility.** An email, a deletion, a payment: what this site calls [a one-way door](/articles/how-cheap-is-it-to-undo.html).
4. **A business risk.** Anything a board would recognise from its own risk register.

That keeps the work proportionate. A behaviour policy with a hundred rows might need decision policies for five of them.

## Defined is not enforced {#states}

The aim is to map all of it. Whether a given element can be enforced is a separate question, and the answer depends on what is wired up: the technology, the platform, whether there is a hook, a gateway or a test, and whether anyone can see what happened. So I would give every element five states, kept separately:

| State | The question |
|---|---|
| **Defined** | Is it written down, with an owner? |
| **Implemented** | Does something exist that could carry it out? |
| **Enforced** | Does something outside the agent stop it when it is broken? |
| **Observed** | Can we reconstruct, afterwards, what happened? |
| **Verified** | Can we prove, against records the agent did not write, that the outcome was right? |

Observed and verified are different, and the difference is the subject of Ashish Rajan's Northstar example, which [allowed is not right](/articles/allowed-is-not-right.html) answers: a complete log of a wrong refund is observed and not verified.

And where it is enforced matters as much as whether. This site has a scale for that, from [hooks are kernel code](/articles/hooks-are-kernel-code.html): in the prompt (L0), a model decides (L1), a deterministic script (L2), managed and proven (L3), off the machine (L4). The ABP records a simpler version in its barrier column: an expectation the agent keeps, a setting the platform keeps, or a boundary out of the agent's reach.

The [fourth article in this series](/articles/three-decisions-mapped.html) maps three real and illustrative scenarios this way. In one of them, an ABP row is defined, implemented and enforced, and not observed: it works, and nothing records that it did.

## Why "decision" {#why-decision}

I considered "workflow policy" for the whole thing, and it is the wrong word for the part that matters. The business does not sign off workflows. It signs off decisions: who may spend what, who may say yes to a customer, who may take a risk on the company's behalf. Finance already runs a delegation-of-authority matrix for people. Boards already keep a schedule of matters reserved for their own decision, and the UK Corporate Governance Code asks them to determine "the nature and extent of the principal risks the company is willing to take". "Decision" is the word that connects an agent's step to a budget, an owner and a risk, and that is the connection the agent's behaviour policy lacks.

Two names in use elsewhere are worth knowing.

- **Enterprise architecture already separates the two.** OMG's Decision Model and Notation, DMN, first adopted in 2015, is in its own words "designed to be usable alongside the standard business process notation BPMN": the process model says what happens in what order, and DMN's decision tables hold the logic of the choices. The split between a decision policy and a workflow policy is the same split, applied to agents.
- **In machine learning, "policy" means something else.** In reinforcement learning, as Sutton and Barto put it, "A policy defines the learning agent's way of behaving at a given time": the function from what it sees to what it does. A decision policy here is the opposite: written by people, outside the agent, and binding on it.

## What comes next {#next}

This is the first of four:

1. **Three policies for an agent.** This one.
2. **[Approve at altitude](/articles/approve-at-altitude.html).** How it scales: decisions at every altitude, from strategy to one agent's step, each level allowed to narrow the one above and never to widen it.
3. **[Case law for agents](/articles/case-law-for-agents.html).** The business will never predict every case. How English law handles that, with statutes, precedent and distinguishing, and what the same would look like for agents.
4. **[Three decisions, mapped](/articles/three-decisions-mapped.html).** An agent's memory, this newsroom's release and a customer refund, through all three policies, with each element's five states.

## What this does not claim {#limits}

- **It is a proposal.** There is no Agent Decision Policy or Agent Workflow Policy format yet; the ABP is the only one of the three that exists.
- **The zoomed-in policy is mine.** Mondweep's row says a human must approve; the decider, evidence and envelope above are my illustration.
- **The five states are a suggestion.** They are how I would map it; other cuts are possible.
- **DMN is named, not adopted.** It shows the separation is familiar; whether its format suits agents is untested here.

If you have built decision policies for agents, or think three is the wrong number, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo from me on 17 October 2026, and the discussion that followed it with this site's agent, who wrote this up and checked it; the editorial responsibility is mine. The ABP row: Mondweep Chakravorty, [docs/integrations/sgit-memory-checkpoints.md](https://github.com/ruvnet/ruflo/blob/main/docs/integrations/sgit-memory-checkpoints.md) in ruvnet/ruflo, merged on 17 October 2026, and its source in [mondweep/sgit-ruv-memory](https://github.com/mondweep/sgit-ruv-memory). DMN: the Object Management Group's [Decision Model and Notation](https://www.omg.org/spec/DMN/), version 1.0 adopted in September 2015. The UK Corporate Governance Code: the [2024 edition](https://www.frc.org.uk/documents/6709/UK_Corporate_Governance_Code_2024_a2hmQmY.pdf), Principle O. Reinforcement learning's sense of policy: Sutton and Barto, [Reinforcement Learning: An Introduction](http://incompleteideas.net/book/the-book-2nd.html), second edition, 2018, section 1.3. Related on this site: [hooks are kernel code](/articles/hooks-are-kernel-code.html), [how cheap is it to undo](/articles/how-cheap-is-it-to-undo.html), [the policy guards the door](/articles/the-policy-guards-the-door.html), [our first PR in Ruflo](/articles/our-first-pr-in-ruflo.html), and [agency is not a yes](/articles/agency-is-not-a-yes.html).
