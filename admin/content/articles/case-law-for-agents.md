---
title: Case law for agents: principles from the top, precedent from the cases, and how a decision earns its way into code
date: 2026-10-17
author: Dinis Cruz
author_url: about/index.html
summary: The third article in the series on agent decision policies is about the cases nobody predicted. A business will never write down every variation of its decisions, and it should not try. English law has lived with the same problem for centuries, and its answer fits agents well. Parliament writes statutes from principles and objectives; delegated rules must stay within the powers an Act gives them; courts apply both to the facts in front of them; decisions of higher courts bind lower ones; a case whose facts differ in a way that matters is distinguished; and the highest court can depart from its own past decisions when they turn out wrong. For agents, the same shape gives a working loop. Principles and envelopes come from the top. A case the decision policy does not settle goes to a person, who decides with the context to decide well, and the answer is recorded with its facts and reasons. The next case with the same material facts follows that precedent without asking again; one that differs is distinguished, and escalates. Precedents that keep holding are written into the policy, and then compiled into code. That is the maturity curve this site has described before, from a person deciding to a rule that runs without them, but driven by real cases instead of guessed in advance. It needs one thing most agent systems lack: a decision record good enough to serve as a law report.
version: v0.12.97
license: https://creativecommons.org/licenses/by/4.0/
tags: agents, agent-decision-policy, case-law, precedent, common-law, governance, decision-records, maturity-model, series, article
status: published
---

!shot dn-caselaw.webp | images/ | How a decision earns its way into code: from a case at a branch point to a precedent, then to tested code. | process

!trail decision-policy

## In short {#in-short}

- **Nobody can predict every case.** A business that tries to write every decision down in advance will fail, and should not try.
- **English law has the same problem, and an answer.** Statutes set principles; courts decide cases; precedent carries the answers forward.
- **The shape maps onto agents.** Principles and envelopes from the top; escalation for the cases they do not settle; a recorded decision that the next case follows.
- **Distinguishing is the escalation trigger.** A case whose facts differ in a way that matters does not follow the precedent. It goes to a person.
- **Precedent becomes policy, then code.** What keeps holding is written down, then compiled. That is the maturity curve, driven by cases.
- **It needs a law report.** A decision record with the facts, the rule, the decider and the reasons. Most agent systems keep a log, not a report.

## The cases nobody predicted {#problem}

The [second article](/articles/approve-at-altitude.html) argued that you approve at altitude: the board signs off its risk appetite, a function signs off its limits within it, and each level below may narrow the one above but never widen it. That makes the far-out cases visible. It does not answer the ordinary ones in between: the case that is inside every envelope and still not covered by any rule. A refund for an order that arrived late but intact. A memory deletion requested by someone who is not the project owner but is on the project. A release with a failing test that is not quite unrelated to the change.

The business will never predict all of those, and I do not think it should try. A decision policy that tries to list every case becomes a contract nobody reads. What it needs is a way to settle the unpredicted ones and learn from them.

## How English law does it {#law}

England and Wales has lived with this problem for centuries, and I think its answer is a good model. I am not a lawyer, and what follows is the shape, not the detail.

- **Statutes set principles and objectives.** Parliament writes Acts. They cannot list every case either, and courts read them in the light of their purpose. In a narrow set of cases, set out in Pepper v Hart in 1992, a court may even read what the minister said in Parliament to find what a provision was for.
- **Delegated rules stay within their powers.** An Act can give a minister the power to make detailed rules. A rule that goes beyond that power is ultra vires and can be quashed, as the employment tribunal fees order was in 2017. That is the narrow-never-widen rule from the [second article](/articles/approve-at-altitude.html#narrow).
- **Courts decide cases, and the decisions bind.** A court applies the law to the facts in front of it, and gives its reasons. Decisions of higher courts bind lower ones: as the Open University's introduction to the subject puts it, "if the precedent is from a more senior court than the court hearing the new case, then the precedent tends to be binding."
- **A case that differs is distinguished.** In the same source's words: "If a court decides that the facts in an earlier case are similar, but not similar enough, then this is called distinguishing." The precedent does not apply, and the court decides afresh.
- **Precedent can be corrected.** In 1966 the House of Lords declared, in a Practice Statement, that it could depart from its own previous decisions. The Supreme Court treats that as applying to itself. A wrong answer is not locked in forever; it can be overruled, by a court with the authority to do it.

Scotland's legal system is different, a mixed one, and so are many others. I use England and Wales because it is the one I know and the one where precedent works most like what I am proposing.

## The same shape for agents {#mapping}

| In English law | For agents |
|---|---|
| An Act of Parliament | The principles and envelope at the top: risk appetite, budget, licence to operate |
| Delegated legislation, within its powers | Decision and workflow policies at lower altitudes, inside their parent's envelope |
| A court deciding a case | A person deciding an escalated case, with the context to decide well |
| The judgment, with reasons | The decision record: facts, rule applied, decider, outcome, reasons |
| Binding precedent | The next case with the same material facts follows it, without escalating |
| Distinguishing | Facts that differ in a way that matters: the case escalates |
| The hierarchy of courts | Altitude: a precedent set higher up binds the levels below |
| Departing from a precedent | A precedent that turns out wrong is overruled, at the altitude that set it |

The loop in the figure is the whole of it. A case arrives at a branch point. If a rule in the decision policy settles it, it is resolved. If a recorded precedent with the same material facts matches, it is resolved the same way, and recorded. If neither, or if the facts differ in a way that matters, it goes to a person. Their decision, with the facts and the reasons, becomes a precedent. The next matching case follows it.

## How a decision earns its way into code {#maturity}

This is where it connects to what this site has written about who makes a decision. [Agency is not a yes](/articles/agency-is-not-a-yes.html) put the top of its scale at delegation: "The cases you keep approving unchanged become rules that run without you, as code under a behaviour policy." [Hooks are kernel code](/articles/hooks-are-kernel-code.html) gave a scale for where a rule runs, from the prompt to off the machine.

Case law is the mechanism that moves a decision up both scales:

1. **A person decides.** The first time, with the context to decide, and the record of why.
2. **Precedent decides.** The next matching cases follow it. A person sees them afterwards, not before.
3. **The policy decides.** After the precedent has held across enough cases, it is written into the decision policy as a rule, signed off at the altitude that owns it.
4. **Code decides.** The rule is compiled: a test, a check in CI, a limit in a tool, a gate in front of the agent. It is now deterministic, and it is where the mission-critical decisions should end up.

Each step is earned by cases, not assumed in advance. That is the difference from writing every rule up front: the rules that reach code are the ones reality kept asking for.

## What a decision record needs {#record}

A court's judgment is useful because it records enough to be followed. Most agent systems keep a log of what happened; a precedent needs more:

- **The facts that mattered.** Not the whole context, but the facts the decision turned on, so the next case can be compared.
- **The rule it was decided under.** Which decision policy, at which altitude, and which envelope.
- **Who decided, with what authority.** A named person, or the precedent or rule that settled it.
- **The outcome.** What was allowed or refused, and what the agent then did.
- **The reasons.** Why, in a sentence or two. This is the part that makes it a precedent rather than a statistic.

Without that, a system cannot distinguish a case, because it does not know which facts the earlier decision turned on. It is also the gap this site keeps finding: in the [SGit × Ruflo run](/articles/the-policy-guards-the-door.html#questions), every policy decision is computed and none is written down. A decision that leaves no record is a [self-report](/articles/your-agents-logs-are-a-self-report.html) at best.

## Two small cases from tonight {#tonight}

The [fourth article](/articles/three-decisions-mapped.html#newsroom) maps this newsroom's own release, and the same evening produced two small cases that show the loop at work.

- **A new rule from one case.** A figure shipped with a date nobody had checked, while the text around it had been checked. The fix was a new version. The precedent is that a figure's facts are checked like the body's. One case was enough here, because the rule is cheap and the principle above it, "verify every fact", already covered it.
- **A case distinguished.** The session's status report counted two commits with no leak scan before them. Both were in throwaway repositories, built to test git hooks, that never published anything. The rule exists to stop a key reaching a published repository; these facts differ in exactly the way that matters. The case is distinguished, the rule stands, and the counter should count only the repositories the rule covers.

Neither needed a person to escalate to, because I was there to decide. In a system with many agents, each would have gone up one altitude, and come back as a precedent.

## Where the analogy stops {#limits-of-analogy}

- **Courts are slow on purpose.** A precedent in law takes years and an argument from both sides. A precedent for an agent can be set in a minute by one person. That is its strength and its risk.
- **Precedent can carry a bias forward.** A wrong decision followed a thousand times is a thousand wrong decisions. The ability to overrule, at the right altitude, matters more for agents than for courts, because the volume is higher.
- **Nobody argues the other side.** Courts hear both parties. A person approving an agent's case usually hears only the agent. One answer is to ask a second agent for the case against, which is a review, not a court.
- **"Material facts" is a judgement.** Deciding whether a case is distinguished is itself a decision. A model can propose; at first, a person should decide.

## The series {#series}

1. [Three policies for an agent](/articles/three-policies-for-an-agent.html): behaviour, decision and workflow.
2. [Approve at altitude](/articles/approve-at-altitude.html): narrow, never widen.
3. **Case law for agents.** This one.
4. [Three decisions, mapped](/articles/three-decisions-mapped.html): the scenarios.

## What this does not claim {#limits}

- **It is not legal advice, or a summary of English law.** It borrows the shape of precedent, from introductory sources, for a different purpose.
- **It is a proposal.** No agent system I know of keeps decision records as precedents in this way; the loop is untested.
- **The two cases are small.** They show the loop's shape, not that it works at scale.

If you are a lawyer and the analogy is wrong somewhere that matters, I would like to know: [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo from me on 17 October 2026, written up and checked by this site's agent; the editorial responsibility is mine. Precedent and distinguishing: the Open University's [Judicial decision making](https://www.open.edu/openlearn/society-politics-law/law/judicial-decision-making/content-section-9.2), sections 8.2 and 8.3. Delegated powers: [R (UNISON) v Lord Chancellor](https://caselaw.nationalarchives.gov.uk/uksc/2017/51) [2017] UKSC 51, 26 July 2017. Departing from precedent: the Practice Statement (Judicial Precedent) [1966] 1 WLR 1234, as described by the Supreme Court in [Knauer v Ministry of Justice](https://caselaw.nationalarchives.gov.uk/uksc/2016/9) [2016] UKSC 9, paragraph 20. Purpose and Hansard: Pepper v Hart [1993] AC 593, decided on 26 November 1992, and its three conditions as restated in [R (O) v Secretary of State for the Home Department](https://caselaw.nationalarchives.gov.uk/uksc/2022/3) [2022] UKSC 3. Scotland's mixed system: the Attorney General's speech [Two jurisdictions, a shared inheritance](https://www.gov.uk/government/speeches/two-jurisdictions-a-shared-inheritance), 9 June 2014. Related on this site: [agency is not a yes](/articles/agency-is-not-a-yes.html), [hooks are kernel code](/articles/hooks-are-kernel-code.html), [your agent's logs are a self-report](/articles/your-agents-logs-are-a-self-report.html).
