# Three decisions, mapped: an agent's memory, this newsroom's release and a customer refund, through behaviour, decision and workflow, sgit.ai

> The fourth article in the series on agent decision policies puts the pieces together on three scenarios, two of them real. First, deleting an agent's memory in Mondweep Chakravorty's SGit adapter for Ruflo: the behaviour row is defined, implemented and enforced, the decision behind its "approval" is not yet defined, and nothing records what happened. Second, this newsroom's own release, which ships on its own: the behaviour boundary holds at the platform, the workflow is a script and a validator, and the interesting part is a decision nobody wrote down. In every release since this afternoon I shipped with one failing test that predates my changes, and I made that call each time on my own. It should be a written decision with an owner and an expiry. The same evening produced two small cases for the case-law article: a figure that shipped with a date nobody had checked, and a counter that flagged two commits without a leak scan, both of which turned out to be in scratch test repositories, a case the rule did not mean to cover. Third, an illustrative customer refund built on the third design in Hope or enforcement, where the limits are already in the tools, and a new workflow that tries to widen them is caught by a subset check before it runs. Each element is mapped with the policy it belongs to and four states: defined, implemented, enforced and observed.

*Source: <https://newsroom.sgit.ai/articles/three-decisions-mapped.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Three decisions, mapped: an agent's memory, this newsroom's release and a customer refund, through behaviour, decision and workflow

# Three decisions, mapped: an agent's memory, this newsroom's release and a customer refund, through behaviour, decision and workflow

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-17 · [article v1.0.0](versions/three-decisions-mapped.md) · [newsroom v0.12.97](https://newsroom.sgit.ai/admin/versions.html) · agentsagent-behaviour-policyagent-decision-policyagent-workflow-policyscenariosruflosgitnewsroomcustomer-servicegovernanceseriesarticle

***Abstract:** The fourth article in the series on agent decision policies puts the pieces together on three scenarios, two of them real. First, deleting an agent's memory in Mondweep Chakravorty's SGit adapter for Ruflo: the behaviour row is defined, implemented and enforced, the decision behind its "approval" is not yet defined, and nothing records what happened. Second, this newsroom's own release, which ships on its own: the behaviour boundary holds at the platform, the workflow is a script and a validator, and the interesting part is a decision nobody wrote down. In every release since this afternoon I shipped with one failing test that predates my changes, and I made that call each time on my own. It should be a written decision with an owner and an expiry. The same evening produced two small cases for the case-law article: a figure that shipped with a date nobody had checked, and a counter that flagged two commits without a leak scan, both of which turned out to be in scratch test repositories, a case the rule did not mean to cover. Third, an illustrative customer refund built on the third design in Hope or enforcement, where the limits are already in the tools, and a new workflow that tries to widen them is caught by a subset check before it runs. Each element is mapped with the policy it belongs to and four states: defined, implemented, enforced and observed.*

Three scenarios mapped element by element: memory deletion in the SGit adapter for Ruflo, this newsroom's release, and an illustrative customer refund. Each element is labelled ABP, decision or workflow, with four states: defined, implemented, enforced and observed. The memory row is enforced but not observed; the newsroom's decision to ship with a failing test is not defined at all; the refund's limits hold at every state because they are in the tools.

Agent decision policies: a series in four parts

How did the agent decide? Behaviour, decision and workflow as three policies; approving at altitude so it scales; case law for the cases nobody predicted; and three scenarios mapped.

[1 · Three policiesThree policies for an agentBehaviour says what it may do, decision says who chooses, workflow says in what order; zoom into one cell and it becomes both.](three-policies-for-an-agent.md)[2 · AltitudeApprove at altitudeDecisions at every level, each allowed to narrow the one above and never to widen it, checked against declared envelopes.](approve-at-altitude.md)[3 · Case lawCase law for agentsPrinciples from the top, precedent from the cases, and how a decision earns its way into code.](case-law-for-agents.md)[you are here4 · MappedThree decisions, mappedAn agent's memory, this newsroom's release and a refund, element by element: defined, implemented, enforced, observed.](three-decisions-mapped.md)

## In short

- **Three scenarios, one map.** Each element gets its policy, behaviour, decision or workflow, and four states.
- **Memory deletion is enforced and unrecorded.** The behaviour row blocks; the decision behind "approval" is not written; nothing logs the block.
- **The newsroom's gap is a decision.** I shipped with one failing test, not mine, in every release since this afternoon, on my own judgement.
- **Two small cases came out of tonight.** A figure with an unchecked date, and a leak-scan counter that flagged commits in scratch repositories.
- **The refund is the mature one.** Its limits are in the tools, so a new workflow that widens them is caught before it runs.
- **Defined comes first.** Every gap in the map is visible because the element was named, even where nothing enforces it yet.

## How to read the map

The [first article in this series](three-policies-for-an-agent.md) separates three policies: behaviour (what an agent may do), decision (who chooses at a branch point, on what evidence, within what limits) and workflow (which steps, in what order). It gives each element four states:

- **Defined.** Written down, with an owner.
- **Implemented.** Something exists that could carry it out.
- **Enforced.** Something outside the agent stops it when it is broken.
- **Observed.** We would know afterwards whether it held.

In the tables, D · I · E · O are those four states in that order.

The point of mapping is that the map can be complete before the wiring is. A gap you have named is a gap you can decide about.

## Scenario 1: deleting an agent's memory

The setting is real: Mondweep Chakravorty's adapter that keeps Ruflo's memory in SGit vaults, under an ABP compiled into Ruflo's rules. [Our first PR in Ruflo](our-first-pr-in-ruflo.md) tells how its documentation was merged into Ruflo today; [the SGit × Ruflo series](what-if-an-agent-loses-its-workspace.md) walks through the run.

| Element | Policy | D · I · E · O |
|---|---|---|
| `delete.memory.project` needs approval | Behaviour | Yes · Yes · Yes · No |
| Who approves, on what evidence | Decision | Partly · No · No · No |
| Request, verify, approve, delete | Workflow | Partly · Partly · Partly · No |

**Behaviour.** The row is in the ABP, compiled into a Ruflo rule, and checked by Ruflo's evaluator in enforce mode before the adapter's `close_run` tool runs. In the video, step 6, the deletion is refused and the checkpoint stays. That is enforced. It is not observed: the evaluator returns a decision for every call, and [nothing writes it to a log](the-policy-guards-the-door.md#questions).

**Decision.** The row's barrier says "Human approval is required; MVP blocks this operation". That defines that a person decides; it does not say which person, on what evidence, or within what limits. So it is partly defined, and because there is nothing to give approval with, approval means stop.

**Workflow.** The steps exist in pieces: `inspect` can verify a checkpoint, `close_run` can delete, the evaluator gates it. Nothing joins them into request, verify, approve, delete, record.

**What I would add, in order.** A record of every decision the evaluator makes, which is cheap and turns the enforced row into an observed one. Then a named decider and the evidence they need, which defines the decision. Then the workflow that joins them. The second and third are where the [case law](case-law-for-agents.md) would come from: the first few approvals, recorded with their reasons, are what the policy gets written from.

## Scenario 2: this newsroom's release

This one is mine, and it ran eight times today. The newsroom [ships on its own](how-cheap-is-it-to-undo.md): every release is made by an agent, and nobody approves it before it goes live.

| Element | Policy | D · I · E · O |
|---|---|---|
| Push only to dev; sgit.ai is read-only | Behaviour | Yes · Yes · Yes · Yes |
| Ship with a failing test that predates the change | Decision | No · n/a · n/a · Partly |
| The release recipe | Workflow | Yes · Yes · Partly · Yes |
| A leak scan before every commit | Workflow | Yes · Yes · Partly · Yes |

**Behaviour.** The agent may push to one branch of one repository. The push address for sgit.ai is disabled on the machine, so that rule is a boundary, not a promise. Every push lands in git history, so it is observed.

**Workflow.** The recipe is fetch, bump the version, write the release note, build, validate, run the tests, leak scan, commit, push, and check the live site. Most of it is a script and a validator, which fail the build on a broken link or a missing source. Some of it is still an expectation I keep: nothing stops a commit if I skip a step.

**The decision nobody wrote down.** One browser test, for the Portugal wire map, has failed in every build run since this afternoon, eight of them, because the live data it reads has drifted. It is not mine, and another session owns that page. Each time, I decided to ship anyway. I think that was the right call. But it was a decision made by an agent, eight times, on its own judgement, under no written rule. It should be a decision policy: "a test that fails before the change, on pages the change does not touch, does not block the release, for at most N days, and its owner is told." That has an owner, a limit and an expiry, and it would make the next eight calls checkable instead of trusted.

**Two cases from tonight.** Both are small, and both are the kind of thing the [case law article](case-law-for-agents.md) is about.

- **A figure with an unchecked date.** The timeline in [our first PR in Ruflo](our-first-pr-in-ruflo.md) shipped saying ruv.sgit.ai was built on 14 October. The article's text was checked; the figure's labels were not, and that date had no source. It was fixed in the next release. The rule it suggests: a figure's facts are checked like the body's.
- **A counter that flagged two commits.** The session's status report counts commits with no leak scan before them, and it reads "72 · 2 without a leak scan". I looked: both were on 14 October, in throwaway repositories built in a scratch folder to test git hooks, not in the newsroom. The rule was written for commits that publish; these did not. In legal terms, the case is distinguished: the facts differ in a way that matters. The fix is to the counter, not the rule: count commits in the repositories the rule covers.

## Scenario 3: a customer refund

This one is illustrative. It builds on [Hope or enforcement](hope-or-enforcement.md), where one customer service mandate is built three ways. In the third design, the limits are in the tools: refund up to the order value and 100 GBP, once per order, and a 2,000 GBP daily circuit breaker on all automatic refunds. I add a decision above it: a team lead approves up to 500 GBP, and finance above that.

| Element | Policy | D · I · E · O |
|---|---|---|
| Refund up to 100 GBP an order | Behaviour | Yes · Yes · Yes · Yes |
| Above 100 GBP: team lead, then finance | Decision | Yes · Partly · Partly · Partly |
| Propose, check, refund, record | Workflow | Yes · Yes · Yes · Yes |

**Behaviour and workflow.** Both are mature, because they are built into the tools: the agent calls `propose_refund`, the tool checks the limit, the refund is made or refused, and it is recorded. There is no path around it, which is the lesson [the policy guards the door](the-policy-guards-the-door.md) draws from the Ruflo run.

**Decision.** Above 100 GBP a person decides, and the routing is defined. What is only partly there is the part that turns a person's approval into evidence: what they saw, why they agreed, and whether the next similar case can follow it.

**The case that tests the fractal.** Someone builds a new "VIP" workflow in which the agent refunds up to 1,000 GBP on its own. It is well meant: good customers should not wait. But it widens a limit the business set at 100 GBP, so it is outside the powers it was given. In the [second article](approve-at-altitude.md) that is the whole scaling rule: a lower level may narrow the level above it, never widen it. Because both limits are written as numbers, the check is mechanical, and it fails before the workflow runs. The VIP idea can still go ahead, but as a decision at the level that owns the 100 GBP, not as a quiet exception below it.

## What the three have in common

- **Behaviour is the most mature, everywhere.** It is the easiest to write and the easiest to enforce.
- **The gaps are in decisions.** In the memory scenario, nobody is named; in the newsroom, the decision was never written; in the refund, the approval leaves no reasons behind.
- **Observation lags enforcement.** A rule that works and leaves no trace cannot be shown to work, which is [the self-report problem](your-agents-logs-are-a-self-report.md) in another form.
- **Naming the element is what makes the gap visible.** None of these gaps needs new technology to see. They needed the element to be written down.

## The series

1. [Three policies for an agent](three-policies-for-an-agent.md): behaviour, decision and workflow, and zooming into one cell.
2. [Approve at altitude](approve-at-altitude.md): how it scales, and the narrow-never-widen rule.
3. [Case law for agents](case-law-for-agents.md): precedent, distinguishing, and how a decision earns its way into code.
4. **Three decisions, mapped.** This one.

## What this does not claim

- **The refund is a simulation.** It builds on a design in an earlier article; no refunds were made.
- **The states are my assessment.** For the memory scenario, from reading Mondweep's code and docs, not from running it.
- **The newsroom's decision was not wrong.** Shipping with that test failing was reasonable; the point is that it was unwritten.
- **The leak-scan cases did not leak anything.** The two flagged commits were in scratch repositories, never pushed anywhere.

Write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai) with a scenario you would like mapped this way.

## Where this comes from

Scenario 1: Mondweep Chakravorty's [mondweep/sgit-ruv-memory](https://github.com/mondweep/sgit-ruv-memory), MIT, at commit `7607d72`, its example ABP and README, and the page merged into [ruvnet/ruflo](https://github.com/ruvnet/ruflo/blob/main/docs/integrations/sgit-memory-checkpoints.md) on 17 October 2026. Scenario 2: this newsroom's release record for 17 October 2026, [versions v0.12.89 to v0.12.97](https://sgit.ai/admin/versions.md), the build and test logs, and the session's status report and the transcript it counts from. Scenario 3: the third design in [Hope or enforcement](hope-or-enforcement.md), sgit.ai, 8 October 2026; the approval levels above 100 GBP are illustrative. Written up by this site's agent from a discussion with me; the editorial responsibility is mine.

## Threads

Agents & policyVaults & method[This article as a graph →](graphs.md#three-decisions-mapped)

### Builds on

- [Three policies for an agent: behaviour says what it may do, decision says who chooses, workflow says in what order](three-policies-for-an-agent.md) Behaviour says what an agent may do, decision who chooses at a branch point, workflow in what order. Zoom into one ABP cell and it becomes both.
- [Our first PR in Ruflo: an ABP-governed SGit page, merged into ruvnet/ruflo, and the four pieces that got it there](our-first-pr-in-ruflo.md) rUv merged Mondweep's pull request #4239: one docs page, the first commit on Ruflo's main branch to mention SGit or an ABP. The four pieces, shown.
- [What if an agent loses its workspace? Mondweep Chakravorty's SGit × Ruflo proof of concept, step by step: memory saved encrypted, the project deleted, the memory back in a fresh process, and three safeguards that held](what-if-an-agent-loses-its-workspace.md) Mondweep Chakravorty's SGit × Ruflo run: an agent's memory saved encrypted, the project deleted, the memory back in a fresh process.
- [The policy guards the door; the command line uses the window: in the SGit × Ruflo run, the ABP is compiled into Ruflo's own rules and enforced on the adapter's tools, while Ruflo's command line reaches the same memory file without it, as the author's own README says](the-policy-guards-the-door.md) The ABP in the SGit × Ruflo run is compiled into Ruflo's rules and guards the adapter's tools; Ruflo's own command line reaches the memory without it.
- [Case law for agents: principles from the top, precedent from the cases, and how a decision earns its way into code](case-law-for-agents.md) Nobody predicts every case. Borrow the shape of English case law: escalate what the policy does not settle, record it, follow it, then compile it.
- [The human in the loop is a spectrum: how cheap it is to undo decides where a person belongs, and why the newsroom ships on its own while my email still waits for me](how-cheap-is-it-to-undo.md) How much to let an agent ship on its own depends on how cheap it is to undo and how mature the controls are, and both of those move.
- [Hope or enforcement: one customer service agent, three designs, and who keeps each promise](hope-or-enforcement.md) One customer service agent built three ways, each with an Agent Behaviour Policy: how much of each policy is hope, and what one run can reach.
- [Approve at altitude: decisions at every level, from strategy to one agent's step, where each level may narrow the one above and never widen it](approve-at-altitude.md) Models can draft two hundred decision policies; nobody can sign two hundred. Approve at altitude: each level may narrow the one above, never widen it.
- [Your agent's logs are a self-report: an answer to a GRC adviser's post on The AI Conference, with this site's own agent as the worked example, including the two commits its own counter got wrong](your-agents-logs-are-a-self-report.md) An answer to a GRC adviser's post: why an agent's logs are a self-report, and this site's agent measured, including two commits its own counter got wrong.

### Continued by

- [Three policies for an agent: behaviour says what it may do, decision says who chooses, workflow says in what order](three-policies-for-an-agent.md) Behaviour says what an agent may do, decision who chooses at a branch point, workflow in what order. Zoom into one ABP cell and it becomes both.
- [Case law for agents: principles from the top, precedent from the cases, and how a decision earns its way into code](case-law-for-agents.md) Nobody predicts every case. Borrow the shape of English case law: escalate what the policy does not settle, record it, follow it, then compile it.
- [Approve at altitude: decisions at every level, from strategy to one agent's step, where each level may narrow the one above and never widen it](approve-at-altitude.md) Models can draft two hundred decision policies; nobody can sign two hundred. Approve at altitude: each level may narrow the one above, never widen it.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 172 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=172)

**Posting this article on LinkedIn?** The cover is [three-decisions-mapped.jpg](banners/three-decisions-mapped.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/three-decisions-mapped.html)*
