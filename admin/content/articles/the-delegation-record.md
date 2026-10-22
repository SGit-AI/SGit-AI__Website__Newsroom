---
title: The delegation record: RiskMandate's go-to-market plan, one workflow taken from an existing business rule to evidence that still holds after a change, starting with our own inbox
date: 2026-10-22
author: Dinis Cruz
author_url: about/index.html
summary: The review of our strategy has converged, and the next step is not another argument about architecture. It is to deliver one chain, once, for one workflow, well enough that a customer can use it to make a decision and wants us to keep it current: an existing business requirement, an approved delegation to an agent, a control that implements it, an observed result, and evidence that is still valid after something changes. What the customer gets at the end is a delegation record in six parts: the business requirement, the agent delegation, the control mapping, the evidence, the remaining gaps, and the conditions that make it invalid. Two refinements make it work. A rule written for people is not yet a delegation to an agent: it has to be extracted, its ambiguities listed, and the delegation approved by its owner. And the approved baseline is never updated from observed behaviour. The plan runs in three stages, immediate value, maintenance value and repeatability, with a deliberately small first customer. And we start with ourselves: pilot zero is our own inbox, where the rule is that the agent drafts and I send, and where, it turns out, Gmail has no permission that allows drafting without also allowing sending.
version: v0.13.37
license: https://creativecommons.org/licenses/by/4.0/
tags: riskmandate, go-to-market, abp, pilots, mandates, article
status: published
---

!shot dl-chain.webp | images/ | The chain to deliver once, end to end: an existing requirement, an approved delegation, an implemented control, an observed result, and evidence that still holds after a change. | concept

## In short {#in-short}

- **Deliver one chain, once.** From an existing rule to evidence after a change.
- **The product is the delegation record.** Six parts a customer can act on.
- **A rule for people is not yet a delegation.** Extract it, list the ambiguities, approve it.
- **The baseline is approved, never learned.** Observed behaviour is evaluated, not adopted.
- **Three stages.** Immediate value, maintenance value, repeatability.
- **A small first customer.** One workflow, one owner, one environment.
- **Pilot zero is our own inbox.** Gmail cannot enforce our own rule.

## From strategy to delivery {#delivery}

Over the last two days we have had a public exchange about RiskMandate's strategy: [an analyst's blueprint](/articles/an-analysts-blueprint-for-riskmandate.html), [drift is the mandate moving](/articles/drift-is-the-mandate-moving.html) and [approved business mandates](/articles/approved-business-mandates.html), each answering an AI-assisted review written in a ChatGPT session. Its latest round says the discussion has moved from "what are you actually proposing?" to "can you deliver this useful result for a customer?", and recommends completing one chain:

existing requirement → approved agent delegation → implemented control → observed result → evidence that remains valid after change.

I agree, and I think that is our go-to-market plan. Not a broader architecture, and not more reviews; one workflow, done end to end, with the gaps visible. One caution I want to keep in front of us: three rounds of an AI review agreeing with a refined position is not market validation. Only a customer's decision is.

## The delegation record {#record}

!shot dl-record.webp | images/ | The delegation record in six parts, business requirement, agent delegation, control mapping, evidence, remaining gaps and change conditions, filled in for pilot zero, our own inbox, as the plan stands; nothing in it has been tested yet. | comparison

The answer to a buyer's question, "what exactly will I have at the end?", is a compact record in six parts:

1. **Business requirement.** The source rule, its version, its owner and its scope.
2. **Agent delegation.** What the agent is given to do under it, with limits and exceptions.
3. **Control mapping.** Which existing system keeps each requirement, or that none can.
4. **Evidence.** What was tested, against which deployment and policy version, and what happened.
5. **Remaining gaps.** What is unsupported or unverified, and the owner's decision about it.
6. **Change conditions.** The events that make the record invalid and need a retest, a restriction or a new approval.

It is the practical form of the coverage explanation, and it sits naturally on what we already have: the behaviour policy holds the delegation and what keeps each rule; the five states we published in [three decisions, mapped](/articles/three-decisions-mapped.html), defined, implemented, enforced, observed and verified, become the evidence column, as long as each state says what was tested and where. We will call it the delegation record, make it the thing we sell, and make keeping it true the thing customers pay for.

## A rule for people is not yet a delegation {#translate}

!shot dl-translate.webp | images/ | A rule for people is not yet a delegation to an agent: refunds up to £100, the amount, one refund, a team lead's approval, eligibility and the process approval, each with the question an agent deployment must also answer. | comparison

The review adds the refinement that makes [approved business mandates](/articles/approved-business-mandates.html) workable. A rule the business already approves was written for a person or a role. Handing it to an agent raises new questions. "Staff may refund up to £100": can the agent execute the refund, or only recommend it? What establishes the amount owed? What limits apply across repeated requests and runs that happen at the same time? Who is the approver for an exception, and what exact action does the approval cover? Which record says the customer is eligible? What change requires the whole thing to be approved again?

So the delegation is made in three visible steps: extract the existing requirement; list the ambiguities and conditions that automation introduces; and get the resulting delegation approved by the requirement's owner. Our customer milestones already ask for a mandate "drafted by the agent and corrected by the customer", and add: "The correction is the elicitation." What we add is the approval as an explicit checkpoint. A model can propose an interpretation; it must not quietly inherit the authority of the original policy.

## The rules we keep {#rules}

Three rules from the review that I want in the product from the first day:

- **The approved baseline is never learned from behaviour.** If repeated behaviour becomes the new normal, the system normalises the drift it was meant to catch; and a new permission is not new authority. A change to authority needs approval; a change in behaviour needs evaluation. That is the line in [drift is the mandate moving](/articles/drift-is-the-mandate-moving.html): drift is the change nobody approved.
- **Obligations, not only permissions.** A rule that blocks every refund respects every limit and still fails a process whose purpose is to reimburse eligible customers. The behaviour policy already has "must" beside yes, ask and no; the pilot will measure that the legitimate work still gets done.
- **One approved case is not a class of cases.** Approving an exception once is different from approving future cases that look like it. Before a precedent from [case law for agents](/articles/case-law-for-agents.html) becomes reusable, it needs its own record: the facts that must match, what prevents reuse, who approved the generalisation, its scope and duration, and how it is withdrawn.

## Three stages {#stages}

!shot dl-stages.webp | images/ | Three stages: immediate value, fix one mismatch and show it from the protected system; maintenance value, make a controlled change and show what it invalidates; repeatability, a related workflow or a second customer, measuring what was reused. | concept

The plan runs in three stages, each testing a different claim:

1. **Immediate value.** Find one consequential mismatch between how the process should run and the controls it actually has. Fix it. Show a legitimate task completing, and a forbidden effect stopped, confirmed by the protected system's own record. The customer should be able to say why their deployment decision is now better supported.
2. **Maintenance value.** In the agreed test environment, make a controlled, realistic change: a permission, an approval condition. Show that the affected requirement is identified, the earlier evidence is marked, and the retest or the decision is triggered. This tests the recurring business far more directly than a second version of a document.
3. **Repeatability.** A related workflow, or a second customer with a related problem. Measure what was reused and what had to be rebuilt: time to clarify the mandate, time to map and implement controls, tests reused, integration work, and upkeep. Then ask whether the customer will pay to maintain or extend it.

Only the third stage tells us what we are building: a valuable service, a software-assisted service, or a software product. Any of the three is a legitimate outcome, and the evidence should decide.

## The first customer {#customer}

Deliberately small: one workflow, one accountable business owner, one supported environment, a few consequential requirements, one working control change, and a clear account of what remains uncovered. A second enforcement target is a later test of portability, not a condition for learning from the first.

The profile: a team with an agent already doing useful work; a concrete concern about one action or decision; existing systems that could enforce the conditions; a business owner willing to define the delegation; and someone able to implement and test the changes. That gives the engagement the best chance of learning about the product, instead of spending it building basic infrastructure. Teams without those controls need a different offer, with a different cost and buyer, and that is fine; it is just not the first one.

## Pilot zero: our own inbox {#pilot-zero}

Before the first customer, we start with ourselves, because we have a real workflow, a real owner, and a known gap. In [answering a draft](/articles/answering-a-draft.html), the inbox agent behind agent@riskmandate.ai reads the mail, researches, drafts and labels, and I read and send every email: 178 of them in its first three and a half weeks. The rule that the agent never sends is, in that article's words, "a rule we keep ourselves, not something the mailbox enforces."

Running the chain on it already found something. Google's documentation lists the Gmail permissions, and creating a draft needs one of three of them; every one also allows sending. `gmail.compose` is described as "Manage drafts and send emails", and `gmail.modify` as "Read, compose, and send emails from your Gmail account". So the mailbox itself cannot keep our rule: there is no permission that lets an agent draft without also letting it send. That is exactly the line the record has to be able to write: this target cannot enforce this requirement.

So pilot zero has a clear plan:

- **The requirement and the delegation** are written: every email is read and sent by me; the agent drafts, labels, and deletes only its own decision drafts.
- **The control mapping** has to find something other than Gmail: a hook in the agent's harness that refuses send calls, which would be a setting; or drafts kept outside Gmail, in a vault, so the agent never holds a permission that can send.
- **The evidence** is a send attempted by the agent, and Gmail's own record that nothing left.
- **The remaining gap**, until then, is an expectation, accepted by me, with every send done by hand.
- **The change conditions** are a new permission or connector, a new agent on the mailbox, or a change to who sends.

Stage 2 is easy to test on it too: add a permission, and see whether the record notices. When it is done, it will be the first public delegation record, and the template for the first customer.

## The brief for the RiskMandate sites {#brief}

This plan changes what the RiskMandate sites should say, and the agent that maintains them is being briefed. In short:

- **Lead with the delegation record**, not with real-time enforcement: one workflow, from an approved business mandate to tested controls and evidence that is kept current.
- **Publish a dated capability table**: available artefacts, working demonstrations, piloted integrations, supported capabilities and plans; and name, in every enforcement example, the component that actually stops the action.
- **Add the translation step to the milestones**: extract the requirement, list the automation ambiguities, approve the delegation.
- **Add the three stages and the first-customer profile** to the customer site, with the six-part record as the template, and pilot zero as the first worked example when it is done.

## What this does not claim {#limits}

- **Nothing here has been delivered yet.** The record for pilot zero is a plan; no row is tested.
- **The review is AI-assisted.** Written in a ChatGPT session; its agreement is not market validation.
- **The Gmail finding is from documentation.** Google's descriptions of its scopes, read on 22 October 2026, not a test.
- **The candidate controls are untested.** A hook is a setting; drafts outside Gmail change the workflow.
- **The first customer is a profile, not a name.** We are looking for them.

## Where this comes from {#sources}

The third round of an AI-assisted review of our strategy, written in a ChatGPT session on 22 October 2026, paraphrased and quoted in short phrases; Google's documentation of the Gmail API scopes and of drafts.create, read the same day; and our own articles. Related: [approved business mandates](/articles/approved-business-mandates.html), [drift is the mandate moving](/articles/drift-is-the-mandate-moving.html), [answering a draft](/articles/answering-a-draft.html), [three decisions, mapped](/articles/three-decisions-mapped.html), [case law for agents](/articles/case-law-for-agents.html), [our first customers](/articles/our-first-customers.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
