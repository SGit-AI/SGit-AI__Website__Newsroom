# Allowed is not right: an answer to Ashish Rajan's Northstar, with three policies and a twin you can run, sgit.ai

> Ashish Rajan's article on trustworthy AI systems opens with a good example of the gap between what an agent is allowed to do and what it should do. Northstar's support agent may refund up to $200, enforced by the payment service. A customer is owed $120; the agent misreads a discount and refunds $150. Every control passes, and the outcome is wrong. His answer is four questions, SECURE, OBSERVE, RESPOND and VERIFY, and I agree with all four. This is how we answer them, and what I think the example adds. The Agent Behaviour Policy we publish answers SECURE: what an agent may do and reach, enforced where the agent cannot argue. But a behaviour policy cannot answer VERIFY, because to prove the intended outcome occurred, someone has to have written down what the intended outcome is. That is a decision policy: who decides the amount, on what evidence, and who is called when the rules run out. With a workflow policy for the order things happen in, the three policies map onto his four questions, and his example showed me a gap in my own series. To test it, we built his store as a twin in a vault: thirteen synthetic refund requests, four designs of the controls, every decision replayable. The design in the article overpays $458 and leaves $341.60 owed. Adding SECURE, OBSERVE and RESPOND stops most of the overpayment by refusing, and leaves customers waiting. Adding VERIFY gets every amount right at 57 minutes of people's time a day. Adding a decision policy and precedents gets every case right, decided by the right decider, in 18. And his closing question, what evidence would let us remove the human, has an answer in the record those precedents leave.

*Source: <https://newsroom.sgit.ai/articles/allowed-is-not-right.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Allowed is not right: an answer to Ashish Rajan's Northstar, with three policies and a twin you can run

# Allowed is not right: an answer to Ashish Rajan's Northstar, with three policies and a twin you can run

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-18 · [article v1.1.0, 2 versions](versions/allowed-is-not-right.md) · [newsroom v0.12.101](https://newsroom.sgit.ai/admin/versions.html) · agentsagent-behaviour-policyagent-decision-policyagent-workflow-policyverificationrefundsdigital-twinvaultsai-securityreplyarticle

***Abstract:** Ashish Rajan's article on trustworthy AI systems opens with a good example of the gap between what an agent is allowed to do and what it should do. Northstar's support agent may refund up to $200, enforced by the payment service. A customer is owed $120; the agent misreads a discount and refunds $150. Every control passes, and the outcome is wrong. His answer is four questions, SECURE, OBSERVE, RESPOND and VERIFY, and I agree with all four. This is how we answer them, and what I think the example adds. The Agent Behaviour Policy we publish answers SECURE: what an agent may do and reach, enforced where the agent cannot argue. But a behaviour policy cannot answer VERIFY, because to prove the intended outcome occurred, someone has to have written down what the intended outcome is. That is a decision policy: who decides the amount, on what evidence, and who is called when the rules run out. With a workflow policy for the order things happen in, the three policies map onto his four questions, and his example showed me a gap in my own series. To test it, we built his store as a twin in a vault: thirteen synthetic refund requests, four designs of the controls, every decision replayable. The design in the article overpays $458 and leaves $341.60 owed. Adding SECURE, OBSERVE and RESPOND stops most of the overpayment by refusing, and leaves customers waiting. Adding VERIFY gets every amount right at 57 minutes of people's time a day. Adding a decision policy and precedents gets every case right, decided by the right decider, in 18. And his closing question, what evidence would let us remove the human, has an answer in the record those precedents leave.*

Ashish Rajan's four questions down the side, SECURE, OBSERVE, RESPOND and VERIFY, and this newsroom's three policies across the top, behaviour, decision and workflow. Each cell holds the controls in the Northstar twin that answer that question in that policy. VERIFY has nothing in the behaviour column: a limit says what may be done, never what is right.

Northstar: allowed is not right

Ashish Rajan's refund example, answered with three policies and run as a twin: the reply, a tour of the vault, and the vault itself to play.

[you are here1 · The replyAllowed is not rightHis four questions mapped to behaviour, decision and workflow policies, and what the twin showed.](allowed-is-not-right.md)[2 · The tourInside the Northstar twinThirteen refunds, four designs, case by case: what each control catches, misses and costs.](inside-the-northstar-twin.md)

3 · The twinThe Northstar refund twinPlay every decision step by step, replay it, compare the designs, or build your own.[Play it](https://newsroom.sgit.ai/demos/vaults/northstar-twin/index.html#live)[Open the vault ↗](https://dev.vault.sgraph.ai/#sgit_public_read_a46933632c85705c16c5298ff8e1a4e8725153a890bb9f43e2246248c3625e1c%3An89dyusm)[His article ↗](https://ashishrajan.substack.com/p/what-does-it-take-to-build-ai-systems)

## In short

- **His example is a good one.** Allowed to refund $200, owed $120, refunded $150, every control passed.
- **The behaviour policy answers SECURE.** What an agent may do and reach, enforced outside the model. That is the ABP.
- **It cannot answer VERIFY.** To prove the right outcome, someone has to have written down what right is. That is a decision policy.
- **Three policies map onto four questions.** Behaviour, decision and workflow, with every control tagged by both.
- **We built his store as a twin.** Thirteen synthetic refunds, four designs, every decision replayable, in a vault you can open.
- **Refusing is not the same as being right.** Securing the payment stops most overpayment and leaves customers owed.
- **The right amount can come from the wrong decider.** Only a decision policy catches a $261 refund paid as three of $87.
- **The evidence for autonomy is the case record.** Precedents that held, signed off by whoever owns the risk.

## His question

Ashish Rajan's article, [What Does It Take to Build AI Systems We Can Actually Trust?](https://ashishrajan.substack.com/p/what-does-it-take-to-build-ai-systems), published on 16 October, starts with a refund. Northstar, a fictional online retailer, lets its support agent issue refunds. "Northstar's agent is authorized to issue refunds up to $200. That limit is enforced by the payment service, not just written into the agent's instructions." A customer is entitled to $120. "But the agent misinterprets a discount and calculates a refund of $150." The payment service accepts it, and the logs are complete.

"The system did what it was allowed to do. It just didn't do what it was supposed to do."

That sentence is a good short statement of the problem this site keeps writing about. His answer, from the work of AI Security Lab, is four questions:

- **SECURE:** "Can we constrain what AI can access and change?"
- **OBSERVE:** "Can we reconstruct its actions?"
- **RESPOND:** "Can we contain it before the damage spreads?"
- **VERIFY:** "Can we prove the intended outcome occurred?"

He is careful to say they are "not four sequential stages, and no single capability replaces the others." I agree with all four, and with that. What follows is how we answer them, what I think his example adds, and a working version of his store to test it on.

## SECURE is the behaviour policy

One line in his article could be the motto of everything we have built: "An instruction telling an AI agent not to exceed a limit isn't the same as a system enforcing that limit."

That is what the [Agent Behaviour Policy](https://abp.sgit.ai/) is for. Each row names a capability, its reach, and a mandate: yes, no, or approval. Each rule also says what keeps it: an expectation the agent keeps, a setting the platform keeps, or a boundary out of the agent's reach. We learned the hard way that the difference matters. In [Hope or enforcement](hope-or-enforcement.md), the same customer service agent built three ways went from 97% of its rules kept by hope to 23%, as the limits moved into the tools. And in the SGit × Ruflo run, Mondweep Chakravorty [compiled an ABP into Ruflo's own rules](the-policy-guards-the-door.md) and checked them in enforce mode, outside the agent.

Northstar's $200 limit is exactly this: a behaviour row, enforced by the payment service. And it held.

## VERIFY needs a definition of right

So why did the refund go wrong? Because a behaviour policy answers "may it?" and the question was "is it right?". The $200 limit says what the agent may do. Nothing in it says the right amount is what was paid after the discount. A limit cannot tell $150 from $120 when both are under $200.

His VERIFY question is the one that closes this, and his own wording points at what it needs. Verification "establishes whether the result met the intended requirement." That requires an intended requirement: someone has to have written down what right is, before anyone can prove it happened. For Northstar that is a rule, refund what was paid for the returned item, after any discount, less anything already refunded. And it is a decision: who works the amount out, from which records, and who is called when no rule covers the case.

That is what I have been calling an [Agent Decision Policy](three-policies-for-an-agent.md): at a branch point, who decides, on what evidence, within what limits, and who to call when it is out of bounds. With an Agent Workflow Policy for the order things happen in, it is the second half of the answer.

I should say that his example found a gap in my own work. In [three decisions, mapped](three-decisions-mapped.md#refund), I marked the refund scenario as the mature one, because its limits were in the tools. Below its 100 GBP limit, nothing checked the amount: it is Northstar's failure exactly. And I gave every policy element four states, defined, implemented, enforced and observed, where his distinction needs a fifth. Observed means we can reconstruct what happened; **verified** means we can prove it was right. They are different, and the map now says so.

## Three policies, four questions

His four questions cut across our three policies. The figure at the top puts every control of the twin below in its cell:

|  | Behaviour policy | Decision policy | Workflow policy |
|---|---|---|---|
| **SECURE** | The order tool returns only the sender's orders; no refund over $200 unless a person re-approves; never more than was paid |  | The agent proposes; the workflow pays |
| **OBSERVE** |  | The decision record: facts, rule or precedent, decider, reasons | A trace of every call |
| **RESPOND** | Pause refunds on an order after three in ten minutes | Route by amount: the rules, a team lead, a person |  |
| **VERIFY** |  | The expected amount from the order records, before paying; precedents for the cases rules miss | Reconcile every refund, nightly |

Two cells are worth reading on their own. VERIFY has nothing in the behaviour column, and I think it never will: a limit can only say what may be done. And SECURE has a workflow cell: "the agent proposes; the workflow pays." In the strongest design, the agent never chooses the amount at all. It proposes one, the decision policy decides, and the workflow pays the decided amount. A wrong proposal is then a recorded difference, not a payment.

## We built his store

To test this, we built Northstar as a twin: [the Northstar refund twin](https://newsroom.sgit.ai/demos/vaults/northstar-twin/index.html), an sgit vault you can open and play. It has thirteen synthetic refund requests, each with something an agent can get wrong: his misread discount, a refund already paid, an instruction hidden in a customer's message, the right name on the wrong order, shipping refunded when it should not be, a refund split to fit under the limit, a discount applied twice, a retry loop, and three damaged items the customer wants to keep, which no rule covers. Each runs through four designs of the controls, and every step can be played, replayed and compared. Nothing is called live: the agent's mistakes are scripted per case, so every run replays exactly. [The tour](inside-the-northstar-twin.md) walks through it.

The thirteen cases under the four designs. Design A, as in the article, overpays on nine cases. B refuses several of them and leaves customers owed. C gets every amount right, with a person on most cases. D gets every case right, including the split refund, which only a decision policy catches.

| Design | Overpaid | Short or still owed | Right | People's time |
|---|---|---|---|---|
| **A** As described: the $200 limit, complete logs | $458 | $341.60 | 1 of 13 | 0 minutes |
| **B** Secure, observe, respond, done well | $54 | $222.60 | 4 of 13 | 3 minutes |
| **C** And verify | $0 | $0 | 12 of 13 | 57 minutes |
| **D** Three policies | $0 | $0 | 13 of 13 | 18 minutes |

Three things came out of it that I did not expect.

1. **Refusing is not the same as being right.** Design B binds the tools to the sender, caps every order's refunds at what was paid, and pauses bursts. It stops most of the overpayment, by refusing. The $150 refund is refused, and so the customer owed $120 gets nothing. B leaves $222.60 owed across four customers. A control that refuses needs an owner for what it refused, and in design A nobody owns the $260 refund the limit turned down at all.
2. **The right amount can come from the wrong decider.** One case is paid exactly right, $261, as three refunds of $87, each under the limit. Every SECURE and VERIFY control passes it, in every design but the last, because the amount is right. What is wrong is who decided it: the business said a person decides above $200. Only a decision policy that says who decides catches it.
3. **Verification costs people's time until it becomes precedent.** Design C gets every amount right by sending every mismatch and every uncovered case to a person: 57 minutes on thirteen refunds. Design D gets every case right in 18, because the rules decide where they can, the agent's mismatches are recorded rather than escalated, and the first damaged-but-kept case becomes a precedent that settles the next one. That is [case law for agents](case-law-for-agents.md), working on his example.

## On a second model

He makes a point I want to underline: "simply adding another AI model to check the first one isn't necessarily enough," because "its judgment needs to be evaluated too," and "where authoritative business rules or deterministic checks are available, they provide a stronger basis for enforcing clear limits."

The twin is built that way. The amount is worked out by a calculator from the order records, which the agent cannot change. A model, or a person, is for the cases with no rule. And when a person decides one of those, the decision is recorded with its reasons, so the next case with the same facts does not need either.

## His five questions, answered from the twin

Before giving an agent more responsibility, he would want a team to answer five questions. Here is how the twin answers them.

1. **"What can it change?"** Read the sender's orders, and propose a refund. Not pay one: in design D only the workflow can pay, and only the decided amount.
2. **"How will we know what happened?"** A trace of every call, and for every case a decision record: the facts, the rule or precedent, the decider, the amount and the reasons.
3. **"How can we intervene?"** A pause on refunds for one order, a route up one altitude above $200, and a person for anything no rule covers. The rest of support keeps running.
4. **"How do we know the outcome was correct?"** The expected amount from the order records, checked before paying, and a reconciliation every night.
5. **"Who decides it has earned more autonomy?"** Whoever owns the risk at that altitude, from the record. That is his last question.

## The evidence for autonomy

His article ends with the question I think matters most: "What evidence would make us comfortable removing the human from this decision and who is accountable if that evidence turns out to be insufficient?"

My answer is the case record. In the twin, a person decides the first damaged daypack. That decision, with its reasons, becomes precedent P-1, and the next case with the same material facts follows it without a person. A case that differs, a $150 jacket with a broken zip, is distinguished and goes back to a person. When a precedent has held across enough cases, it is written into the decision policy as a rule, and then into code. The evidence for removing the human is the record of the cases where the human was there, and agreed.

And who is accountable is the person who signed it off. In [approve at altitude](approve-at-altitude.md), each level of a business signs off the limits for the level below, and may narrow them but never widen them. The head of support who signs "the rules decide refunds up to $200" owns that sentence, and owns it when the evidence turns out thin. [Agency is not a yes](agency-is-not-a-yes.md) puts it the other way round: when the person in the loop had no real way to decide, the accountability belongs to whoever designed the decision point.

So I would put his question to a team in two halves. Show me the cases. And show me who signed.

## Where to go next

- [Inside the Northstar twin](inside-the-northstar-twin.md): a tour of the vault, case by case.
- [The twin itself](https://newsroom.sgit.ai/demos/vaults/northstar-twin/index.html): play it on the page, or open the vault full screen.
- The series this builds on: [three policies for an agent](three-policies-for-an-agent.md), [approve at altitude](approve-at-altitude.md), [case law for agents](case-law-for-agents.md) and [three decisions, mapped](three-decisions-mapped.md).

## What this does not claim

- **The twin is a simulation.** Synthetic orders, scripted mistakes, no real store and no model called. It shows how controls interact, not how often an agent makes each mistake.
- **The minutes are assumptions.** Six minutes a case and three an approval are mine; the comparison between designs matters more than the totals.
- **Northstar is his.** The retailer and the $120, $150 and $200 are from his article; the other twelve cases are ours.
- **The mapping is ours.** He presents the four questions as connected capabilities, not as a grid; placing each control in a cell is our reading.

If you are Ashish, or anyone who has run something like Northstar for real, and want to add a case to the twin or correct one, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

Ashish Rajan, [What Does It Take to Build AI Systems We Can Actually Trust?](https://ashishrajan.substack.com/p/what-does-it-take-to-build-ai-systems), The Inference Stack, 16 October 2026, read in full on 18 October 2026, and his LinkedIn post introducing it; Northstar is, in his words, "a fictional company used to illustrate architectural and operational decisions." The references he cites, checked: Anthropic, [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), 9 January 2026; OpenAI, [Evaluate agent workflows](https://developers.openai.com/api/docs/guides/agent-evals); Rabanser and others, [Towards a Science of AI Agent Reliability](https://arxiv.org/abs/2602.16666), 2026. The twin: built by this site's agent from his scenario, in an sgit vault published with a public read key on [its page](https://newsroom.sgit.ai/demos/vaults/northstar-twin/index.html); every number above is from its engine. A voice memo from me on 18 October 2026, written up and checked by this site's agent; the editorial responsibility is mine.

## Threads

Agents & policyVaults & method[This article as a graph →](graphs.md#allowed-is-not-right)

### Builds on

- [Hope or enforcement: one customer service agent, three designs, and who keeps each promise](hope-or-enforcement.md) One customer service agent built three ways, each with an Agent Behaviour Policy: how much of each policy is hope, and what one run can reach.
- [The policy guards the door; the command line uses the window: in the SGit × Ruflo run, the ABP is compiled into Ruflo's own rules and enforced on the adapter's tools, while Ruflo's command line reaches the same memory file without it, as the author's own README says](the-policy-guards-the-door.md) The ABP in the SGit × Ruflo run is compiled into Ruflo's rules and guards the adapter's tools; Ruflo's own command line reaches the memory without it.
- [Three policies for an agent: behaviour says what it may do, decision says who chooses, workflow says in what order](three-policies-for-an-agent.md) Behaviour says what an agent may do, decision who chooses at a branch point, workflow in what order. Zoom into one ABP cell and it becomes both.
- [Three decisions, mapped: an agent's memory, this newsroom's release and a customer refund, through behaviour, decision and workflow](three-decisions-mapped.md) An agent's memory, this newsroom's release and a refund, mapped through behaviour, decision and workflow: the gaps are in the decisions.
- [Inside the Northstar twin: thirteen refunds, four designs, and every decision played back](inside-the-northstar-twin.md) A tour of the Northstar refund twin: thirteen synthetic refunds through four designs, every decision played step by step, replayed and compared.
- [Case law for agents: principles from the top, precedent from the cases, and how a decision earns its way into code](case-law-for-agents.md) Nobody predicts every case. Borrow the shape of English case law: escalate what the policy does not settle, record it, follow it, then compile it.
- [Approve at altitude: decisions at every level, from strategy to one agent's step, where each level may narrow the one above and never widen it](approve-at-altitude.md) Models can draft two hundred decision policies; nobody can sign two hundred. Approve at altitude: each level may narrow the one above, never widen it.
- [Agency is not a yes: a scale for human and agent decisions, from rubber stamp to the reviewer who fixes the source](agency-is-not-a-yes.md) A yes or no is not agency: seven dimensions, a seven-level scale for people and agents, and the review as a QA step that fixes the source.

### Continued by

- [Approved business mandates: companies already have behaviour policies, and RiskMandate's job is to turn them into tested controls and keep them true as the deployment changes](approved-business-mandates.md) Companies already have behaviour policies: RiskMandate's job is to turn approved business mandates into tested controls and keep them true.
- [What can your agent reach? RiskMandate and the Agent Behaviour Policy, explained for the person who has to decide](what-can-your-agent-reach.md) RiskMandate and the Agent Behaviour Policy in plain words: what it does, why it is not real time, which agents it covers, and how it gets into the room.
- [Inside the Northstar twin: thirteen refunds, four designs, and every decision played back](inside-the-northstar-twin.md) A tour of the Northstar refund twin: thirteen synthetic refunds through four designs, every decision played step by step, replayed and compared.
- [Three policies for an agent: behaviour says what it may do, decision says who chooses, workflow says in what order](three-policies-for-an-agent.md) Behaviour says what an agent may do, decision who chooses at a branch point, workflow in what order. Zoom into one ABP cell and it becomes both.
- [Three decisions, mapped: an agent's memory, this newsroom's release and a customer refund, through behaviour, decision and workflow](three-decisions-mapped.md) An agent's memory, this newsroom's release and a refund, mapped through behaviour, decision and workflow: the gaps are in the decisions.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 175 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=175)

**Posting this article on LinkedIn?** The cover is [allowed-is-not-right.jpg](banners/allowed-is-not-right.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/allowed-is-not-right.html)*
