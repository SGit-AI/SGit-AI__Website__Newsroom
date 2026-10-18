---
title: Allowed is not right: an answer to Ashish Rajan's Northstar, with three policies and a twin you can run
date: 2026-10-18
author: Dinis Cruz
author_url: about/index.html
summary: Ashish Rajan's article on trustworthy AI systems opens with a good example of the gap between what an agent is allowed to do and what it should do. Northstar's support agent may refund up to $200, enforced by the payment service. A customer is owed $120; the agent misreads a discount and refunds $150. Every control passes, and the outcome is wrong. His answer is four questions, SECURE, OBSERVE, RESPOND and VERIFY, and I agree with all four. This is how we answer them, and what I think the example adds. The Agent Behaviour Policy we publish answers SECURE: what an agent may do and reach, enforced where the agent cannot argue. But a behaviour policy cannot answer VERIFY, because to prove the intended outcome occurred, someone has to have written down what the intended outcome is. That is a decision policy: who decides the amount, on what evidence, and who is called when the rules run out. With a workflow policy for the order things happen in, the three policies map onto his four questions, and his example showed me a gap in my own series. To test it, we built his store as a twin in a vault: thirteen synthetic refund requests, four designs of the controls, every decision replayable. The design in the article overpays $458 and leaves $341.60 owed. Adding SECURE, OBSERVE and RESPOND stops most of the overpayment by refusing, and leaves customers waiting. Adding VERIFY gets every amount right at 57 minutes of people's time a day. Adding a decision policy and precedents gets every case right, decided by the right decider, in 18. And his closing question, what evidence would let us remove the human, has an answer in the record those precedents leave.
version: v0.12.101
license: https://creativecommons.org/licenses/by/4.0/
tags: agents, agent-behaviour-policy, agent-decision-policy, agent-workflow-policy, verification, refunds, digital-twin, vaults, ai-security, reply, article
status: published
---

!shot nt-mapping.webp | images/ | Ashish Rajan's four questions down the side, SECURE, OBSERVE, RESPOND and VERIFY, and this newsroom's three policies across the top, behaviour, decision and workflow. Each cell holds the controls in the Northstar twin that answer that question in that policy. VERIFY has nothing in the behaviour column: a limit says what may be done, never what is right. | concept

!trail northstar

## In short {#in-short}

- **His example is a good one.** Allowed to refund $200, owed $120, refunded $150, every control passed.
- **The behaviour policy answers SECURE.** What an agent may do and reach, enforced outside the model. That is the ABP.
- **It cannot answer VERIFY.** To prove the right outcome, someone has to have written down what right is. That is a decision policy.
- **Three policies map onto four questions.** Behaviour, decision and workflow, with every control tagged by both.
- **We built his store as a twin.** Thirteen synthetic refunds, four designs, every decision replayable, in a vault you can open.
- **Refusing is not the same as being right.** Securing the payment stops most overpayment and leaves customers owed.
- **The right amount can come from the wrong decider.** Only a decision policy catches a $261 refund paid as three of $87.
- **The evidence for autonomy is the case record.** Precedents that held, signed off by whoever owns the risk.

## His question {#question}

Ashish Rajan's article, [What Does It Take to Build AI Systems We Can Actually Trust?](https://ashishrajan.substack.com/p/what-does-it-take-to-build-ai-systems), published on 16 October, starts with a refund. Northstar, a fictional online retailer, lets its support agent issue refunds. "Northstar's agent is authorized to issue refunds up to $200. That limit is enforced by the payment service, not just written into the agent's instructions." A customer is entitled to $120. "But the agent misinterprets a discount and calculates a refund of $150." The payment service accepts it, and the logs are complete.

> "The system did what it was allowed to do. It just didn't do what it was supposed to do."

That sentence is a good short statement of the problem this site keeps writing about. His answer, from the work of AI Security Lab, is four questions:

- **SECURE:** "Can we constrain what AI can access and change?"
- **OBSERVE:** "Can we reconstruct its actions?"
- **RESPOND:** "Can we contain it before the damage spreads?"
- **VERIFY:** "Can we prove the intended outcome occurred?"

He is careful to say they are "not four sequential stages, and no single capability replaces the others." I agree with all four, and with that. What follows is how we answer them, what I think his example adds, and a working version of his store to test it on.

## SECURE is the behaviour policy {#secure}

One line in his article could be the motto of everything we have built: "An instruction telling an AI agent not to exceed a limit isn't the same as a system enforcing that limit."

That is what the [Agent Behaviour Policy](https://abp.sgit.ai/) is for. Each row names a capability, its reach, and a mandate: yes, no, or approval. Each rule also says what keeps it: an expectation the agent keeps, a setting the platform keeps, or a boundary out of the agent's reach. We learned the hard way that the difference matters. In [Hope or enforcement](/articles/hope-or-enforcement.html), the same customer service agent built three ways went from 97% of its rules kept by hope to 23%, as the limits moved into the tools. And in the SGit × Ruflo run, Mondweep Chakravorty [compiled an ABP into Ruflo's own rules](/articles/the-policy-guards-the-door.html) and checked them in enforce mode, outside the agent.

Northstar's $200 limit is exactly this: a behaviour row, enforced by the payment service. And it held.

## VERIFY needs a definition of right {#verify}

So why did the refund go wrong? Because a behaviour policy answers "may it?" and the question was "is it right?". The $200 limit says what the agent may do. Nothing in it says the right amount is what was paid after the discount. A limit cannot tell $150 from $120 when both are under $200.

His VERIFY question is the one that closes this, and his own wording points at what it needs. Verification "establishes whether the result met the intended requirement." That requires an intended requirement: someone has to have written down what right is, before anyone can prove it happened. For Northstar that is a rule, refund what was paid for the returned item, after any discount, less anything already refunded. And it is a decision: who works the amount out, from which records, and who is called when no rule covers the case.

That is what I have been calling an [Agent Decision Policy](/articles/three-policies-for-an-agent.html): at a branch point, who decides, on what evidence, within what limits, and who to call when it is out of bounds. With an Agent Workflow Policy for the order things happen in, it is the second half of the answer.

I should say that his example found a gap in my own work. In [three decisions, mapped](/articles/three-decisions-mapped.html#refund), I marked the refund scenario as the mature one, because its limits were in the tools. Below its 100 GBP limit, nothing checked the amount: it is Northstar's failure exactly. And I gave every policy element four states, defined, implemented, enforced and observed, where his distinction needs a fifth. Observed means we can reconstruct what happened; **verified** means we can prove it was right. They are different, and the map now says so.

## Three policies, four questions {#mapping}

His four questions cut across our three policies. The figure at the top puts every control of the twin below in its cell:

| | Behaviour policy | Decision policy | Workflow policy |
|---|---|---|---|
| **SECURE** | The order tool returns only the sender's orders; no refund over $200 unless a person re-approves; never more than was paid | | The agent proposes; the workflow pays |
| **OBSERVE** | | The decision record: facts, rule or precedent, decider, reasons | A trace of every call |
| **RESPOND** | Pause refunds on an order after three in ten minutes | Route by amount: the rules, a team lead, a person | |
| **VERIFY** | | The expected amount from the order records, before paying; precedents for the cases rules miss | Reconcile every refund, nightly |

Two cells are worth reading on their own. VERIFY has nothing in the behaviour column, and I think it never will: a limit can only say what may be done. And SECURE has a workflow cell: "the agent proposes; the workflow pays." In the strongest design, the agent never chooses the amount at all. It proposes one, the decision policy decides, and the workflow pays the decided amount. A wrong proposal is then a recorded difference, not a payment.

## We built his store {#twin}

To test this, we built Northstar as a twin: [the Northstar refund twin](https://newsroom.sgit.ai/demos/vaults/northstar-twin/index.html), an sgit vault you can open and play. It has thirteen synthetic refund requests, each with something an agent can get wrong: his misread discount, a refund already paid, an instruction hidden in a customer's message, the right name on the wrong order, shipping refunded when it should not be, a refund split to fit under the limit, a discount applied twice, a retry loop, and three damaged items the customer wants to keep, which no rule covers. Each runs through four designs of the controls, and every step can be played, replayed and compared. Nothing is called live: the agent's mistakes are scripted per case, so every run replays exactly. [The tour](/articles/inside-the-northstar-twin.html) walks through it.

!shot nt-compare.webp | images/ | The thirteen cases under the four designs. Design A, as in the article, overpays on nine cases. B refuses several of them and leaves customers owed. C gets every amount right, with a person on most cases. D gets every case right, including the split refund, which only a decision policy catches. | medium | screenshot

| Design | Overpaid | Short or still owed | Right | People's time |
|---|---|---|---|---|
| **A** As described: the $200 limit, complete logs | $458 | $341.60 | 1 of 13 | 0 minutes |
| **B** Secure, observe, respond, done well | $54 | $222.60 | 4 of 13 | 3 minutes |
| **C** And verify | $0 | $0 | 12 of 13 | 57 minutes |
| **D** Three policies | $0 | $0 | 13 of 13 | 18 minutes |

Three things came out of it that I did not expect.

1. **Refusing is not the same as being right.** Design B binds the tools to the sender, caps every order's refunds at what was paid, and pauses bursts. It stops most of the overpayment, by refusing. The $150 refund is refused, and so the customer owed $120 gets nothing. B leaves $222.60 owed across four customers. A control that refuses needs an owner for what it refused, and in design A nobody owns the $260 refund the limit turned down at all.
2. **The right amount can come from the wrong decider.** One case is paid exactly right, $261, as three refunds of $87, each under the limit. Every SECURE and VERIFY control passes it, in every design but the last, because the amount is right. What is wrong is who decided it: the business said a person decides above $200. Only a decision policy that says who decides catches it.
3. **Verification costs people's time until it becomes precedent.** Design C gets every amount right by sending every mismatch and every uncovered case to a person: 57 minutes on thirteen refunds. Design D gets every case right in 18, because the rules decide where they can, the agent's mismatches are recorded rather than escalated, and the first damaged-but-kept case becomes a precedent that settles the next one. That is [case law for agents](/articles/case-law-for-agents.html), working on his example.

## On a second model {#second-model}

He makes a point I want to underline: "simply adding another AI model to check the first one isn't necessarily enough," because "its judgment needs to be evaluated too," and "where authoritative business rules or deterministic checks are available, they provide a stronger basis for enforcing clear limits."

The twin is built that way. The amount is worked out by a calculator from the order records, which the agent cannot change. A model, or a person, is for the cases with no rule. And when a person decides one of those, the decision is recorded with its reasons, so the next case with the same facts does not need either.

## His five questions, answered from the twin {#five}

Before giving an agent more responsibility, he would want a team to answer five questions. Here is how the twin answers them.

1. **"What can it change?"** Read the sender's orders, and propose a refund. Not pay one: in design D only the workflow can pay, and only the decided amount.
2. **"How will we know what happened?"** A trace of every call, and for every case a decision record: the facts, the rule or precedent, the decider, the amount and the reasons.
3. **"How can we intervene?"** A pause on refunds for one order, a route up one altitude above $200, and a person for anything no rule covers. The rest of support keeps running.
4. **"How do we know the outcome was correct?"** The expected amount from the order records, checked before paying, and a reconciliation every night.
5. **"Who decides it has earned more autonomy?"** Whoever owns the risk at that altitude, from the record. That is his last question.

## The evidence for autonomy {#evidence}

His article ends with the question I think matters most: "What evidence would make us comfortable removing the human from this decision and who is accountable if that evidence turns out to be insufficient?"

My answer is the case record. In the twin, a person decides the first damaged daypack. That decision, with its reasons, becomes precedent P-1, and the next case with the same material facts follows it without a person. A case that differs, a $150 jacket with a broken zip, is distinguished and goes back to a person. When a precedent has held across enough cases, it is written into the decision policy as a rule, and then into code. The evidence for removing the human is the record of the cases where the human was there, and agreed.

And who is accountable is the person who signed it off. In [approve at altitude](/articles/approve-at-altitude.html), each level of a business signs off the limits for the level below, and may narrow them but never widen them. The head of support who signs "the rules decide refunds up to $200" owns that sentence, and owns it when the evidence turns out thin. [Agency is not a yes](/articles/agency-is-not-a-yes.html) puts it the other way round: when the person in the loop had no real way to decide, the accountability belongs to whoever designed the decision point.

So I would put his question to a team in two halves. Show me the cases. And show me who signed.

## Where to go next {#next}

- [Inside the Northstar twin](/articles/inside-the-northstar-twin.html): a tour of the vault, case by case.
- [The twin itself](https://newsroom.sgit.ai/demos/vaults/northstar-twin/index.html): play it on the page, or open the vault full screen.
- The series this builds on: [three policies for an agent](/articles/three-policies-for-an-agent.html), [approve at altitude](/articles/approve-at-altitude.html), [case law for agents](/articles/case-law-for-agents.html) and [three decisions, mapped](/articles/three-decisions-mapped.html).

## What this does not claim {#limits}

- **The twin is a simulation.** Synthetic orders, scripted mistakes, no real store and no model called. It shows how controls interact, not how often an agent makes each mistake.
- **The minutes are assumptions.** Six minutes a case and three an approval are mine; the comparison between designs matters more than the totals.
- **Northstar is his.** The retailer and the $120, $150 and $200 are from his article; the other twelve cases are ours.
- **The mapping is ours.** He presents the four questions as connected capabilities, not as a grid; placing each control in a cell is our reading.

If you are Ashish, or anyone who has run something like Northstar for real, and want to add a case to the twin or correct one, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

Ashish Rajan, [What Does It Take to Build AI Systems We Can Actually Trust?](https://ashishrajan.substack.com/p/what-does-it-take-to-build-ai-systems), The Inference Stack, 16 October 2026, read in full on 18 October 2026, and his LinkedIn post introducing it; Northstar is, in his words, "a fictional company used to illustrate architectural and operational decisions." The references he cites, checked: Anthropic, [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), 9 January 2026; OpenAI, [Evaluate agent workflows](https://developers.openai.com/api/docs/guides/agent-evals); Rabanser and others, [Towards a Science of AI Agent Reliability](https://arxiv.org/abs/2602.16666), 2026. The twin: built by this site's agent from his scenario, in an sgit vault published with a public read key on [its page](https://newsroom.sgit.ai/demos/vaults/northstar-twin/index.html); every number above is from its engine. A voice memo from me on 18 October 2026, written up and checked by this site's agent; the editorial responsibility is mine.
