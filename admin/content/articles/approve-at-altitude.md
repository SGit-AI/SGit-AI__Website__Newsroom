---
title: Approve at altitude: decisions at every level, from strategy to one agent's step, where each level may narrow the one above and never widen it
date: 2026-10-17
author: Dinis Cruz
author_url: about/index.html
summary: The second article in the series on agent decision policies is about scale. Language models make it cheap to write decision policies, five, a hundred, two hundred of them, and no business owner can sign off two hundred. The answer is the fractal. Decisions and workflows exist at every altitude, strategic, business, product, technical and the single run, and each altitude bounds the one below. So you approve at altitude: the board signs off its risk appetite once, the head of a function signs off a budget and a licence to operate within it, a team signs off its workflow within that, and each level inherits everything above it. The scaling rule is one sentence: a lower level may narrow the level above it, never widen it. For that to be checkable, every policy declares an envelope: money, blast radius, the data and people in scope, reversibility, and how long it lasts. Where the envelope is numbers and lists, the check that a child fits inside its parent is mechanical and can run in CI; where it is words, a model can flag the likely conflicts for a person. This is how a business that cannot predict every decision can still find the ones far outside what it is willing to risk, and it is how English law already treats delegated powers: secondary legislation that goes beyond the Act that allows it is ultra vires, and a court can quash it.
version: v0.12.97
license: https://creativecommons.org/licenses/by/4.0/
tags: agents, agent-decision-policy, agent-behaviour-policy, risk-appetite, governance, fractal-semantic-graphs, delegation, scaling, series, article
status: published
---

!shot dn-altitude.webp | images/ | One envelope, automatic refunds, followed down five altitudes from the board's risk appetite to one agent's run. | concept

!trail decision-policy

## In short {#in-short}

- **Writing policies is now cheap; signing them is not.** A model can draft two hundred decision policies; no owner can approve two hundred.
- **Decisions live at every altitude.** Strategic, business, product, technical, and the single run. Each has its own decisions and workflows.
- **Approve at altitude.** Each level signs off once, and everything below inherits it.
- **Narrow, never widen.** A lower level may tighten the level above it. It may not loosen it.
- **Every policy declares an envelope.** Money, blast radius, data and people in scope, reversibility, duration.
- **The check is mostly mechanical.** Numbers and lists compare in CI; words are flagged by a model for a person.
- **The law got here first.** Delegated legislation that exceeds its parent Act is ultra vires.

## The scaling problem {#problem}

The [first article](/articles/three-policies-for-an-agent.html) separated three policies: behaviour, decision and workflow. If you take it seriously, there are a lot of decision policies. Every branch point that touches money, people, irreversibility or a business risk earns one.

Language models make that possible. Give one the workflows of a team and it will draft decision policies for every branch point in an afternoon: five, a hundred, two hundred. That is new, and useful, and it moves the bottleneck. The bottleneck is now sign-off. A head of support can read and approve five decision policies properly. Not two hundred. And a sign-off without the time to read is the rubber stamp this site describes in [agency is not a yes](/articles/agency-is-not-a-yes.html): liability, not agency.

So the question is how to approve a large number of decisions without anyone reading most of them.

## Decisions at every altitude {#altitudes}

The answer is the shape this site keeps coming back to: a fractal semantic graph, the same kind of structure at every level. Decisions are not one flat list. They sit at altitudes:

| Altitude | Who signs off | Example decision |
|---|---|---|
| **Strategic** | The board | What we are willing to risk, and for what |
| **Business** | The head of a function | A budget and a licence to operate for a whole area |
| **Product** | A team | How a workflow routes a case, and who approves what |
| **Technical** | An engineer | The limits a tool enforces |
| **Run** | Nobody, or the agent | What one agent does in one task |

Each altitude has decisions and workflows of its own. The board's workflow is the annual plan; one agent's workflow is the five steps of one refund. The labels will vary by organisation, and so will the number of levels. What matters is that each level is bounded by the one above it.

## Approve at altitude {#approve}

That gives the scaling rule. **You sign off at an altitude, and everything below inherits it.**

The board does not approve the refund tool. It approves a risk appetite. The UK Corporate Governance Code already puts it there: Principle O asks the board to "determine the nature and extent of the principal risks the company is willing to take in order to achieve its long-term strategic objectives". ISO Guide 73 calls the same thing risk appetite: the "amount and type of risk that an organization is willing to pursue or retain". And the FRC's guidance asks boards for a formal schedule of matters reserved for their decision, to give "clarity to all over where responsibility for decision-making lies". Approving at altitude is that, carried down to agents. The head of support does not approve each workflow. They approve the limits their function works within: how much the agents may refund on their own in a day, above what amount a person decides. A team approves its workflow within those limits. The engineer builds the tool within the team's workflow. And one agent's run happens inside all of it.

Each sign-off is small, because each level only has to read its own level. Two hundred decision policies at the bottom are fine, as long as every one of them fits inside the few that were read and approved above it.

## Narrow, never widen {#narrow}

The rule that makes inheritance safe is one sentence:

> **A lower level may narrow the level above it. It may never widen it.**

A team may say "a person decides above 50 GBP" when the business said 100. It may not say 200. An agent's run may touch one customer when the workflow allows one. It may not touch two.

English law has a name for the second case. An Act of Parliament can delegate the power to make rules, statutory instruments, to a minister. Those rules have the force of law, but only within the power the Act gave. A rule that goes beyond it is ultra vires, outside the powers, and a court can quash it. On 26 July 2017 the Supreme Court did that to the order that introduced employment tribunal fees, in R (UNISON) v Lord Chancellor. The Act gave the Lord Chancellor the power to set fees, but not fees that prevented access to justice; the court held the order "unlawful ab initio", from the start, and said it "must be quashed". That is narrow-never-widen, enforced by the courts for a long time before agents. The [third article](/articles/case-law-for-agents.html) follows the analogy further.

## The envelope {#envelope}

For the rule to be checkable, every policy has to say what its bounds are. I would call that its envelope, and give it the same fields at every altitude:

| Field | Example at the business level | Example at the run level |
|---|---|---|
| **Money** | Automatic refunds at most 2,000 GBP a day | This refund, up to 100 GBP |
| **Blast radius** | Customers of this shop | One customer |
| **Data in scope** | Orders and contact history | This customer's orders |
| **People in scope** | Customers; not employees | The sender only |
| **Reversibility** | One-way doors need a person | A refund is a one-way door |
| **Duration** | Reviewed each quarter | This task |

The point is that the fields are the same at every level. That is what makes the levels comparable, and comparison is what lets the check run without a person.

## The check {#check}

With envelopes declared, "does this lower policy contradict the one above?" becomes a question with an answer.

- **Where the envelope is numbers and lists, it is mechanical.** 1,000 GBP is more than 100 GBP. "Customers and employees" is wider than "customers". That check is deterministic, needs no model, and can run in CI on every change to a policy, the way this site's validator runs on every release.
- **Where the envelope is words, a model can flag.** "Only for complaints about delivery" against "any complaint" is a judgement. A model can read both and say which conflicts are likely, and a person decides. That is the right use for a model here: it widens what a person can review, it does not replace the review.

This is also how you find what nobody predicted. The business will never write down every variation of its decisions. It does not have to. A decision far outside its risk appetite shows up as an envelope that does not fit inside its parent's, whoever wrote it and however well meant. The illustrative case in the figure is a "VIP" workflow that refunds up to 1,000 GBP without a person. It may be a good idea. But it has to be decided at the level that owns the 100 GBP limit, not slipped in below it.

## Where kill switches and escalation sit {#kill}

The same structure says where the controls belong.

- **A kill switch sits at the altitude whose envelope it protects.** The 2,000 GBP daily circuit breaker belongs to the business level: it stops all automatic refunds, not one agent.
- **Escalation goes up one altitude.** A case outside a team's workflow goes to whoever owns the team's limits, not straight to the board.
- **A licence to operate is an envelope with a name.** It is what a function has been allowed to do, signed off once, and checkable from below.

## What this does not solve {#not}

- **Somebody still has to write the top.** A risk appetite that says nothing measurable cannot be checked against. The mechanical check is only as good as the numbers at the top.
- **Envelopes can be gamed.** A team can split one large refund into several small ones. The envelope needs aggregate limits, like the daily breaker, not only per-case ones.
- **Altitude is not hierarchy.** The levels follow what is decided, not the org chart; the person who owns a limit may not be the most senior.
- **Words stay hard.** The model's flags are suggestions; the decision is a person's.

## The series {#series}

1. [Three policies for an agent](/articles/three-policies-for-an-agent.html): behaviour, decision and workflow.
2. **Approve at altitude.** This one.
3. [Case law for agents](/articles/case-law-for-agents.html): what happens with the cases nobody predicted.
4. [Three decisions, mapped](/articles/three-decisions-mapped.html): the scenarios, including the refund in the figure.

## What this does not claim {#limits}

- **It is a proposal.** No decision-policy format with envelopes exists yet; the fields above are mine.
- **The numbers are illustrative.** The tool's limits come from the third design in [Hope or enforcement](/articles/hope-or-enforcement.html); the levels above them are made up for the example.
- **The legal parallel is an analogy.** Courts and CI are different things; the article borrows the shape, not the authority.

Write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai) if you sign off decisions at one of these altitudes and the shape does not match how you work.

## Where this comes from {#sources}

A voice memo from me on 17 October 2026, written up and checked by this site's agent; the editorial responsibility is mine. The UNISON judgment: [R (UNISON) v Lord Chancellor](https://caselaw.nationalarchives.gov.uk/uksc/2017/51) [2017] UKSC 51, 26 July 2017, paragraph 119. The UK Corporate Governance Code: the [2024 edition](https://www.frc.org.uk/documents/6709/UK_Corporate_Governance_Code_2024_a2hmQmY.pdf), Principle O; the words quoted are the same in the 2018 edition. ISO Guide 73:2009, Risk management: Vocabulary, the definition of risk appetite. The FRC's [Guidance on Board Effectiveness](https://www.frc.org.uk/documents/4722/Guidance_on_Board_Effectiveness_MmfcOrz.pdf), July 2018, paragraph 28. The refund limits: [Hope or enforcement](/articles/hope-or-enforcement.html), sgit.ai, 8 October 2026. Related on this site: [agency is not a yes](/articles/agency-is-not-a-yes.html), [commander's intent is a behaviour policy](/articles/commanders-intent-is-a-behaviour-policy.html), [code review as a fractal semantic graph](/articles/code-review-as-a-fractal-semantic-graph.html).
