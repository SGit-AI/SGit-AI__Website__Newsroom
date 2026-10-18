# Case law for agents: principles from the top, precedent from the cases, and how a decision earns its way into code, sgit.ai

> The third article in the series on agent decision policies is about the cases nobody predicted. A business will never write down every variation of its decisions, and it should not try. English law has lived with the same problem for centuries, and its answer fits agents well. Parliament writes statutes from principles and objectives; delegated rules must stay within the powers an Act gives them; courts apply both to the facts in front of them; decisions of higher courts bind lower ones; a case whose facts differ in a way that matters is distinguished; and the highest court can depart from its own past decisions when they turn out wrong. For agents, the same shape gives a working loop. Principles and envelopes come from the top. A case the decision policy does not settle goes to a person, who decides with the context to decide well, and the answer is recorded with its facts and reasons. The next case with the same material facts follows that precedent without asking again; one that differs is distinguished, and escalates. Precedents that keep holding are written into the policy, and then compiled into code. That is the maturity curve this site has described before, from a person deciding to a rule that runs without them, but driven by real cases instead of guessed in advance. It needs one thing most agent systems lack: a decision record good enough to serve as a law report.

*Source: <https://newsroom.sgit.ai/articles/case-law-for-agents.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Case law for agents: principles from the top, precedent from the cases, and how a decision earns its way into code

# Case law for agents: principles from the top, precedent from the cases, and how a decision earns its way into code

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-17 · [article v1.0.0](versions/case-law-for-agents.md) · [newsroom v0.12.97](https://newsroom.sgit.ai/admin/versions.html) · agentsagent-decision-policycase-lawprecedentcommon-lawgovernancedecision-recordsmaturity-modelseriesarticle

***Abstract:** The third article in the series on agent decision policies is about the cases nobody predicted. A business will never write down every variation of its decisions, and it should not try. English law has lived with the same problem for centuries, and its answer fits agents well. Parliament writes statutes from principles and objectives; delegated rules must stay within the powers an Act gives them; courts apply both to the facts in front of them; decisions of higher courts bind lower ones; a case whose facts differ in a way that matters is distinguished; and the highest court can depart from its own past decisions when they turn out wrong. For agents, the same shape gives a working loop. Principles and envelopes come from the top. A case the decision policy does not settle goes to a person, who decides with the context to decide well, and the answer is recorded with its facts and reasons. The next case with the same material facts follows that precedent without asking again; one that differs is distinguished, and escalates. Precedents that keep holding are written into the policy, and then compiled into code. That is the maturity curve this site has described before, from a person deciding to a rule that runs without them, but driven by real cases instead of guessed in advance. It needs one thing most agent systems lack: a decision record good enough to serve as a law report.*

How a decision earns its way into code. A case arrives at a branch point. If a rule settles it, or a recorded precedent with the same material facts matches, it is resolved and recorded. If not, or if the facts differ in a way that matters, it is distinguished and escalated to a person with the context to decide. The decision is recorded with its reasons and becomes a precedent that the next matching case follows. A precedent that holds case after case is written into the policy, then compiled into deterministic, tested code.

Agent decision policies: a series in four parts

How did the agent decide? Behaviour, decision and workflow as three policies; approving at altitude so it scales; case law for the cases nobody predicted; and three scenarios mapped.

[1 · Three policiesThree policies for an agentBehaviour says what it may do, decision says who chooses, workflow says in what order; zoom into one cell and it becomes both.](three-policies-for-an-agent.md)[2 · AltitudeApprove at altitudeDecisions at every level, each allowed to narrow the one above and never to widen it, checked against declared envelopes.](approve-at-altitude.md)[you are here3 · Case lawCase law for agentsPrinciples from the top, precedent from the cases, and how a decision earns its way into code.](case-law-for-agents.md)[4 · MappedThree decisions, mappedAn agent's memory, this newsroom's release and a refund, element by element: defined, implemented, enforced, observed, verified.](three-decisions-mapped.md)

## In short

- **Nobody can predict every case.** A business that tries to write every decision down in advance will fail, and should not try.
- **English law has the same problem, and an answer.** Statutes set principles; courts decide cases; precedent carries the answers forward.
- **The shape maps onto agents.** Principles and envelopes from the top; escalation for the cases they do not settle; a recorded decision that the next case follows.
- **Distinguishing is the escalation trigger.** A case whose facts differ in a way that matters does not follow the precedent. It goes to a person.
- **Precedent becomes policy, then code.** What keeps holding is written down, then compiled. That is the maturity curve, driven by cases.
- **It needs a law report.** A decision record with the facts, the rule, the decider and the reasons. Most agent systems keep a log, not a report.

## The cases nobody predicted

The [second article](approve-at-altitude.md) argued that you approve at altitude: the board signs off its risk appetite, a function signs off its limits within it, and each level below may narrow the one above but never widen it. That makes the far-out cases visible. It does not answer the ordinary ones in between: the case that is inside every envelope and still not covered by any rule. A refund for an order that arrived late but intact. A memory deletion requested by someone who is not the project owner but is on the project. A release with a failing test that is not quite unrelated to the change.

The business will never predict all of those, and I do not think it should try. A decision policy that tries to list every case becomes a contract nobody reads. What it needs is a way to settle the unpredicted ones and learn from them.

## How English law does it

England and Wales has lived with this problem for centuries, and I think its answer is a good model. I am not a lawyer, and what follows is the shape, not the detail.

- **Statutes set principles and objectives.** Parliament writes Acts. They cannot list every case either, and courts read them in the light of their purpose. In a narrow set of cases, set out in Pepper v Hart in 1992, a court may even read what the minister said in Parliament to find what a provision was for.
- **Delegated rules stay within their powers.** An Act can give a minister the power to make detailed rules. A rule that goes beyond that power is ultra vires and can be quashed, as the employment tribunal fees order was in 2017. That is the narrow-never-widen rule from the [second article](approve-at-altitude.md#narrow).
- **Courts decide cases, and the decisions bind.** A court applies the law to the facts in front of it, and gives its reasons. Decisions of higher courts bind lower ones: as the Open University's introduction to the subject puts it, "if the precedent is from a more senior court than the court hearing the new case, then the precedent tends to be binding."
- **A case that differs is distinguished.** In the same source's words: "If a court decides that the facts in an earlier case are similar, but not similar enough, then this is called distinguishing." The precedent does not apply, and the court decides afresh.
- **Precedent can be corrected.** In 1966 the House of Lords declared, in a Practice Statement, that it could depart from its own previous decisions. The Supreme Court treats that as applying to itself. A wrong answer is not locked in forever; it can be overruled, by a court with the authority to do it.

Scotland's legal system is different, a mixed one, and so are many others. I use England and Wales because it is the one I know and the one where precedent works most like what I am proposing.

## The same shape for agents

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

## How a decision earns its way into code

This is where it connects to what this site has written about who makes a decision. [Agency is not a yes](agency-is-not-a-yes.md) put the top of its scale at delegation: "The cases you keep approving unchanged become rules that run without you, as code under a behaviour policy." [Hooks are kernel code](hooks-are-kernel-code.md) gave a scale for where a rule runs, from the prompt to off the machine.

Case law is the mechanism that moves a decision up both scales:

1. **A person decides.** The first time, with the context to decide, and the record of why.
2. **Precedent decides.** The next matching cases follow it. A person sees them afterwards, not before.
3. **The policy decides.** After the precedent has held across enough cases, it is written into the decision policy as a rule, signed off at the altitude that owns it.
4. **Code decides.** The rule is compiled: a test, a check in CI, a limit in a tool, a gate in front of the agent. It is now deterministic, and it is where the mission-critical decisions should end up.

Each step is earned by cases, not assumed in advance. That is the difference from writing every rule up front: the rules that reach code are the ones reality kept asking for.

## What a decision record needs

A court's judgment is useful because it records enough to be followed. Most agent systems keep a log of what happened; a precedent needs more:

- **The facts that mattered.** Not the whole context, but the facts the decision turned on, so the next case can be compared.
- **The rule it was decided under.** Which decision policy, at which altitude, and which envelope.
- **Who decided, with what authority.** A named person, or the precedent or rule that settled it.
- **The outcome.** What was allowed or refused, and what the agent then did.
- **The reasons.** Why, in a sentence or two. This is the part that makes it a precedent rather than a statistic.

Without that, a system cannot distinguish a case, because it does not know which facts the earlier decision turned on. It is also the gap this site keeps finding: in the [SGit × Ruflo run](the-policy-guards-the-door.md#questions), every policy decision is computed and none is written down. A decision that leaves no record is a [self-report](your-agents-logs-are-a-self-report.md) at best.

## Two small cases from tonight

The [fourth article](three-decisions-mapped.md#newsroom) maps this newsroom's own release, and the same evening produced two small cases that show the loop at work.

- **A new rule from one case.** A figure shipped with a date nobody had checked, while the text around it had been checked. The fix was a new version. The precedent is that a figure's facts are checked like the body's. One case was enough here, because the rule is cheap and the principle above it, "verify every fact", already covered it.
- **A case distinguished.** The session's status report counted two commits with no leak scan before them. Both were in throwaway repositories, built to test git hooks, that never published anything. The rule exists to stop a key reaching a published repository; these facts differ in exactly the way that matters. The case is distinguished, the rule stands, and the counter should count only the repositories the rule covers.

Neither needed a person to escalate to, because I was there to decide. In a system with many agents, each would have gone up one altitude, and come back as a precedent.

## Where the analogy stops

- **Courts are slow on purpose.** A precedent in law takes years and an argument from both sides. A precedent for an agent can be set in a minute by one person. That is its strength and its risk.
- **Precedent can carry a bias forward.** A wrong decision followed a thousand times is a thousand wrong decisions. The ability to overrule, at the right altitude, matters more for agents than for courts, because the volume is higher.
- **Nobody argues the other side.** Courts hear both parties. A person approving an agent's case usually hears only the agent. One answer is to ask a second agent for the case against, which is a review, not a court.
- **"Material facts" is a judgement.** Deciding whether a case is distinguished is itself a decision. A model can propose; at first, a person should decide.

## The series

1. [Three policies for an agent](three-policies-for-an-agent.md): behaviour, decision and workflow.
2. [Approve at altitude](approve-at-altitude.md): narrow, never widen.
3. **Case law for agents.** This one.
4. [Three decisions, mapped](three-decisions-mapped.md): the scenarios.

## What this does not claim

- **It is not legal advice, or a summary of English law.** It borrows the shape of precedent, from introductory sources, for a different purpose.
- **It is a proposal.** No agent system I know of keeps decision records as precedents in this way; the loop is untested.
- **The two cases are small.** They show the loop's shape, not that it works at scale.

If you are a lawyer and the analogy is wrong somewhere that matters, I would like to know: [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo from me on 17 October 2026, written up and checked by this site's agent; the editorial responsibility is mine. Precedent and distinguishing: the Open University's [Judicial decision making](https://www.open.edu/openlearn/society-politics-law/law/judicial-decision-making/content-section-9.2), sections 8.2 and 8.3. Delegated powers: [R (UNISON) v Lord Chancellor](https://caselaw.nationalarchives.gov.uk/uksc/2017/51) [2017] UKSC 51, 26 July 2017. Departing from precedent: the Practice Statement (Judicial Precedent) [1966] 1 WLR 1234, as described by the Supreme Court in [Knauer v Ministry of Justice](https://caselaw.nationalarchives.gov.uk/uksc/2016/9) [2016] UKSC 9, paragraph 20. Purpose and Hansard: Pepper v Hart [1993] AC 593, decided on 26 November 1992, and its three conditions as restated in [R (O) v Secretary of State for the Home Department](https://caselaw.nationalarchives.gov.uk/uksc/2022/3) [2022] UKSC 3. Scotland's mixed system: the Attorney General's speech [Two jurisdictions, a shared inheritance](https://www.gov.uk/government/speeches/two-jurisdictions-a-shared-inheritance), 9 June 2014. Related on this site: [agency is not a yes](agency-is-not-a-yes.md), [hooks are kernel code](hooks-are-kernel-code.md), [your agent's logs are a self-report](your-agents-logs-are-a-self-report.md).

## Threads

Agents & policy[This article as a graph →](graphs.md#case-law-for-agents)

### Builds on

- [Approve at altitude: decisions at every level, from strategy to one agent's step, where each level may narrow the one above and never widen it](approve-at-altitude.md) Models can draft two hundred decision policies; nobody can sign two hundred. Approve at altitude: each level may narrow the one above, never widen it.
- [Agency is not a yes: a scale for human and agent decisions, from rubber stamp to the reviewer who fixes the source](agency-is-not-a-yes.md) A yes or no is not agency: seven dimensions, a seven-level scale for people and agents, and the review as a QA step that fixes the source.
- [Hooks are kernel code: a maturity model, the first ten hooks mapped, and a brief for a hooks site and feed where you pay for state, never to run](hooks-are-kernel-code.md) Hooks are small code with kernel reach: a maturity model, the first ten hooks mapped, and a brief for a hooks site where you pay for state, never to run.
- [The policy guards the door; the command line uses the window: in the SGit × Ruflo run, the ABP is compiled into Ruflo's own rules and enforced on the adapter's tools, while Ruflo's command line reaches the same memory file without it, as the author's own README says](the-policy-guards-the-door.md) The ABP in the SGit × Ruflo run is compiled into Ruflo's rules and guards the adapter's tools; Ruflo's own command line reaches the memory without it.
- [Your agent's logs are a self-report: an answer to a GRC adviser's post on The AI Conference, with this site's own agent as the worked example, including the two commits its own counter got wrong](your-agents-logs-are-a-self-report.md) An answer to a GRC adviser's post: why an agent's logs are a self-report, and this site's agent measured, including two commits its own counter got wrong.
- [Three decisions, mapped: an agent's memory, this newsroom's release and a customer refund, through behaviour, decision and workflow](three-decisions-mapped.md) An agent's memory, this newsroom's release and a refund, mapped through behaviour, decision and workflow: the gaps are in the decisions.
- [Three policies for an agent: behaviour says what it may do, decision says who chooses, workflow says in what order](three-policies-for-an-agent.md) Behaviour says what an agent may do, decision who chooses at a branch point, workflow in what order. Zoom into one ABP cell and it becomes both.

### Continued by

- [Inside the Northstar twin: thirteen refunds, four designs, and every decision played back](inside-the-northstar-twin.md) A tour of the Northstar refund twin: thirteen synthetic refunds through four designs, every decision played step by step, replayed and compared.
- [Allowed is not right: an answer to Ashish Rajan's Northstar, with three policies and a twin you can run](allowed-is-not-right.md) Ashish Rajan's Northstar refund: allowed to refund $200, owed $120, paid $150. His four questions mapped to three policies, and tested on a twin.
- [Three policies for an agent: behaviour says what it may do, decision says who chooses, workflow says in what order](three-policies-for-an-agent.md) Behaviour says what an agent may do, decision who chooses at a branch point, workflow in what order. Zoom into one ABP cell and it becomes both.
- [Three decisions, mapped: an agent's memory, this newsroom's release and a customer refund, through behaviour, decision and workflow](three-decisions-mapped.md) An agent's memory, this newsroom's release and a refund, mapped through behaviour, decision and workflow: the gaps are in the decisions.
- [Approve at altitude: decisions at every level, from strategy to one agent's step, where each level may narrow the one above and never widen it](approve-at-altitude.md) Models can draft two hundred decision policies; nobody can sign two hundred. Approve at altitude: each level may narrow the one above, never widen it.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 171 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=171)

**Posting this article on LinkedIn?** The cover is [case-law-for-agents.jpg](banners/case-law-for-agents.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/case-law-for-agents.html)*
