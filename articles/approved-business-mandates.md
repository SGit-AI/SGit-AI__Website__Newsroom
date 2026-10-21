# Approved business mandates: companies already have behaviour policies, and RiskMandate's job is to turn them into tested controls and keep them true as the deployment changes, sgit.ai

> I gave our answer to the analyst's blueprint back to the ChatGPT session the analysis came from, and asked it to review it. Its review is good, it corrects its own first recommendation, and it gives us a phrase I think is right for what RiskMandate does: turning approved business mandates into tested controls, and keeping the relationship between them accurate as the deployment changes. The words that matter are approved business mandates. Companies already have behaviour policies: delegated authority, approval limits, four-eyes rules, data handling, who may contact a customer and when. They wrote them for people. Our job is to work with them to capture what they already approve, convert it into Agent Behaviour Policies their agentic workflows can understand and enforce, test that each control holds, say plainly where a requirement cannot be enforced yet, and notice when a change to the deployment breaks what was true last month. The review also sharpens things we should accept: a policy described is not a policy delivered; our Cedar work is a demonstration, not a compiler; the Pellbridge bank explains, it does not measure; and the earlier notes were AI-assisted, which I have now said on those pages. It ends with the right next step: one real workflow, a policy the business understands, controls that demonstrably hold, and an honest account of what remains.

*Source: <https://newsroom.sgit.ai/articles/approved-business-mandates.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Approved business mandates: companies already have behaviour policies, and RiskMandate's job is to turn them into tested controls and keep them true as the deployment changes

# Approved business mandates: companies already have behaviour policies, and RiskMandate's job is to turn them into tested controls and keep them true as the deployment changes

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-21 · [article v1.1.0, 2 versions](versions/approved-business-mandates.md) · [newsroom v0.13.35](https://newsroom.sgit.ai/admin/versions.html) · riskmandatestrategyabpmandatesassurancearticle

***Abstract:** I gave our answer to the analyst's blueprint back to the ChatGPT session the analysis came from, and asked it to review it. Its review is good, it corrects its own first recommendation, and it gives us a phrase I think is right for what RiskMandate does: turning approved business mandates into tested controls, and keeping the relationship between them accurate as the deployment changes. The words that matter are approved business mandates. Companies already have behaviour policies: delegated authority, approval limits, four-eyes rules, data handling, who may contact a customer and when. They wrote them for people. Our job is to work with them to capture what they already approve, convert it into Agent Behaviour Policies their agentic workflows can understand and enforce, test that each control holds, say plainly where a requirement cannot be enforced yet, and notice when a change to the deployment breaks what was true last month. The review also sharpens things we should accept: a policy described is not a policy delivered; our Cedar work is a demonstration, not a compiler; the Pellbridge bank explains, it does not measure; and the earlier notes were AI-assisted, which I have now said on those pages. It ends with the right next step: one real workflow, a policy the business understands, controls that demonstrably hold, and an honest account of what remains.*

Companies already have behaviour policies: delegated authority, four-eyes, data handling, spending limits, communications and advice rules, each written for people, turned into an Agent Behaviour Policy row with its mandate and what keeps it. Illustrative rows.

## In short

- **The review corrected its own first recommendation.** Integrate existing enforcement first.
- **The phrase that matters: approved business mandates.** Companies already have them.
- **Our job is to convert them.** Into behaviour policies an agent's workflow can enforce.
- **And keep them true.** As connectors, permissions and approvers change.
- **Say when a rule cannot be enforced.** Never weaken it silently.
- **Some corrections we accept.** Described is not delivered; a demo is not a benchmark.
- **The next proof is one real workflow.** With the gaps shown.

## Where this came from

The notes we answered in [an analyst's blueprint for RiskMandate](an-analysts-blueprint-for-riskmandate.md) and [drift is the mandate moving](drift-is-the-mandate-moving.md) came from one of our power users, and were written in a ChatGPT session. I should have said that on those pages, and they now do: it is AI-assisted analysis, useful, but not independent market validation. So I gave our answer back to the same session and asked it to review it. The review is careful: it says it read our response and followed its references, and that it has not run our code or tested a customer deployment.

Its first move is to correct itself. Building tool-call interception as the first priority "should not have been an automatic first priority"; integrate existing enforcement points first, and build an owned interceptor only where a validated requirement makes it necessary. What it keeps is just as important: start with one workflow and a handful of policies, and keep the emphasis on consequential actions, sequences, prevention and evidence.

## Approved business mandates

The line I like most in the review is its description of where our strongest opportunity sits: "turning approved business mandates into tested controls, and keeping the relationship between them accurate as the deployment changes."

The words that matter are approved business mandates. Companies already have behaviour policies. They are just written for people. A refund over £50 needs a team lead. A second person closes an anti-money-laundering alert. Statements go only to the address on file. Purchase orders over a threshold need finance. Nobody contacts a customer under review. Staff do not give investment advice. Every one of those is a mandate the business has already approved, with an owner, and most have a system that already keeps them for people.

So our job is not to invent policy. It is to work with a company to capture what it already approves, and convert it into [Agent Behaviour Policies](what-can-your-agent-reach.md) that its agentic workflows can understand and enforce: the capability, what the agent may do, and what keeps the rule. That is also what the FCA's four elements ask for, as [the Pellbridge agents](inside-the-pellbridge-agents.md) showed: delegated authority is a matrix the bank already has.

## From the mandate to tested controls, and back

From an approved mandate to tested controls, and back: specify the mandate; find what the environment supports; generate the configurations, or say why not; verify that prohibited actions stop and legitimate work continues; and maintain the evidence as the deployment changes.

The review proposes five responsibilities, and they fit what we do as a loop:

1. **Specify the mandate.** Purpose, limits, exceptions, approval and ownership, in the business's words, approved by its holder. This is our milestones' "the mandate, in the customer's words".
2. **Find what the environment supports.** The controls available, the context they lack, and the routes nothing covers. This is the grant, measured.
3. **Generate the configurations, or say why not.** Hooks, gateway rules, application settings; and, as the review puts it, a translator that can say "This target cannot enforce this requirement with the information and controls currently available." Silently weakening a rule to make it deployable would undermine the whole point.
4. **Verify.** Prohibited actions stop and legitimate work still completes, confirmed by the protected system's own record, not just ours.
5. **Maintain the evidence.** A connector update adds an action, a permission change opens another path, a process needs a new approver: detect the change, and take the decision back to its holder. That is [drift](drift-is-the-mandate-moving.md), and it is the recurring work.

## The output that matters

A coverage explanation: for each requirement, what implements it, the evidence that it holds, and what remains, such as an approval that must be invalidated if the content changes, or a session rule that does not yet follow a task into another agent. Illustrative rows.

The review suggests the most valuable output may be a coverage explanation: for each important requirement, what implements it, the evidence, and the remaining limitation. I agree, and it is close to what a behaviour policy row already holds: the barrier says what keeps the rule. What the review adds, usefully, is the last two columns: the evidence that it holds in this deployment, and what it still does not cover. A buyer can decide from that table whether to deploy, what to fix, and what exposure remains.

## What we accept

The review is direct about the gaps, and most of it is right:

- **Described is not delivered.** A capability gap does not by itself recognise a dangerous sequence. To stop a support agent sending the wrong customer's data, the system has to know which customer the task is for, what was read, what is in the output, and who receives it. A policy can state that rule well and still be unenforceable today.
- **Capability, authorisation and observation are three things.** A mandate is what was authorised; it is not evidence of what the agent did.
- **Our Cedar work is a demonstration.** Five rules, written for an article, evaluated against fourteen requests. It shows intentions can be encoded; it is not a compiler, and it assumed the business facts were available. I have corrected the earlier page, which said more than that.
- **Pellbridge explains; it does not measure.** An invented bank and a deterministic replay can show how controls change a scenario, not real incident rates.
- **A control's strength depends on the deployment.** A hook can be strong if its configuration is protected; a gateway can leave an unprotected route. The question is always what this control guarantees here.
- **Proxies are not inherently a single point of failure.** They add a dependency unless deployed redundantly; I have changed our earlier wording.
- **An owner is accountability, not reduction.** Naming who holds a risk does not make it smaller.
- **Receipts need an assurance model.** Rebuilding a timeline, re-evaluating recorded inputs against a pinned policy, and reproducing an execution are different kinds of replay, and a consistent record can still miss an action that bypassed the collector.

## The market is closer than we said

The review also corrects the first note's claim that cross-step behaviour is open ground, and it is right. From the vendors' own pages:

- **Noma Security** says "Legitimate actions can combine into dangerous behavior", and that it can "enforce policy through AI gateways, MCP gateways, agent hooks, agent SDKs, and direct APIs, using the infrastructure already in your environment." That is close to both the first note's thesis and ours.
- **AWS AgentCore Policy** has session-history rules, such as "Deny external API calls after sensitive data was accessed in this session", and is honest about their scope: the session ID comes from the caller, so a count-based limit "counts only the events recorded for that session", and "Starting a new session begins a new count".
- **Endor Labs** says plainly of its coding-agent controls: "It is not a sandbox, firewall, or hardened security boundary." In Codex, "an Ask Permission policy cannot pause a tool call, so the call proceeds."
- **Cedar** puts the responsibility where it belongs: "It is the responsibility of users of Cedar to correctly define policies that implement their authorization model and provide Cedar with all the relevant data to arrive at a decision."

Those last three are exactly the kind of fact a coverage explanation exists to surface: what each control actually guarantees in this deployment. A session rule that resets with a new session is fine for a cooperative agent and not a business-wide limit; an approval policy that cannot pause is not an approval. Knowing that, and saying it before a customer relies on it, is useful work no single enforcement product has a reason to do about the others.

## The first customer, and the first pilot

The review sharpens who to start with: an agent already doing useful work; a concrete action that worries someone; existing controls that could enforce the rule; a named business owner; an engineer able to make changes; and a deployment decision that is currently blocked. And it suggests several customers with a related problem, for example agents that read sensitive information and prepare communications, rather than several unrelated ones, so we learn whether the second one is easier than the first.

Its acceptance criteria for a first pilot are the right ones, and I would adopt them: the owner approves a precise mandate; a legitimate task completes without needless interruption; a prohibited task is stopped and the protected system confirms nothing happened; an approval cannot be reused for a changed recipient or payload; other routes, direct API, another tool, a delegated agent, are blocked or marked uncovered; restarts and delegation are tested; missing context has a defined behaviour; a deployment change triggers a review; a second target produces the same outcomes or reports what it cannot do; and someone pays to keep it going.

## Where I still see it our way

A few points I would keep, with the review's caveats:

- **A broad remit is a position, not yet an advantage.** Agreed; customers have to feel it. But the remit is why the coverage explanation is possible: it spans controls no single vendor owns.
- **Maturity is not simple.** The review is right that a mature company may struggle to coordinate strong controls, and an immature one may lack people to implement anything. Both are customers, for different reasons.
- **Insurance stays an outcome to validate.** The question to ask a broker is the review's: which specific evidence changes your decision, and how would you verify it?
- **Open source earns trust, not revenue.** The recurring value is maintaining integrations, detecting changes, testing translations and keeping evidence current.

## Room to grow

Room to grow: capture the process and its approved rules, then the behaviour policy, both the focus now; and, already explored in published articles, the decision policy, the workflow policy, and approval at altitude with precedent.

One thing the review does not see, because it read only this exchange, is that we have already gone further than the behaviour policy in our published work. That matters, because it is part of our strength: we can evolve with a customer into more advanced cases, or give them the tools to evolve on their own.

- **[Three policies for an agent](three-policies-for-an-agent.md).** The behaviour policy says what an agent may do. An Agent Decision Policy says, at a branch point, who chooses, on what evidence and within what limits. An Agent Workflow Policy says in what order things happen, with which checks between the steps.
- **[Allowed is not right](allowed-is-not-right.md) and [the Northstar twin](inside-the-northstar-twin.md).** A refund that every control allowed and was still wrong, played through four designs, which is the sequence problem the review raises, worked on an example.
- **[Approve at altitude](approve-at-altitude.md).** Decisions at every level, from strategy to one agent's step, where each level may narrow the one above and never widen it, so an owner signs off once instead of two hundred times.
- **[Case law for agents](case-law-for-agents.md).** Principles from the top and precedent from the cases, for the decisions nobody predicted.
- **[Three decisions, mapped](three-decisions-mapped.md).** All three policies on real scenarios, including this newsroom's own release.

We are in the product-market-fit phase, and we do not know every direction this will go. So the order matters. The focus now, especially for RiskMandate, is the first step: getting people to use the behaviour policies, and learning the best way to do it. Start by capturing an existing business process and the rules it already approves, then write the policies around it. The decision and workflow policies are the evolution path, already explored and published, for the customers whose cases need them.

## What changes now

- **The earlier notes are marked as AI-assisted.** Done, on both pages.
- **The Cedar and proxy wording is corrected.** Done.
- **A dated capability table on riskmandate.ai.** Available artefacts, working demonstrations, piloted integrations, supported capabilities and plans, with each enforcement example naming the component that actually stops the action. That is for the Risk Mandate site's own agent.
- **One real workflow.** A policy the business understands, controls that demonstrably hold, and an honest account of the gaps.

## What this does not claim

- **The review is AI-assisted.** Written in a ChatGPT session at my request; quoted in short phrases and paraphrased.
- **The rows and tables are illustrative.** No customer has a coverage explanation yet.
- **Vendor descriptions are their own.** Read from their pages, not tested.
- **Nothing here is a pilot result.** The pilot is the next step.
- **The advanced policies are explored, not deployed.** Decision and workflow policies are in published articles, not yet in a customer's workflow.

## Where this comes from

A review of our answer, written in a ChatGPT session on 21 October 2026, at my request, after it read [an analyst's blueprint for RiskMandate](an-analysts-blueprint-for-riskmandate.md). The vendors' pages, read the same day: Noma Security's agent behaviour runtime control; AWS AgentCore Policy's temporal and session-based policies; Endor Labs' agent governance documentation; and Cedar's security guidance. Related: [drift is the mandate moving](drift-is-the-mandate-moving.md), [inside the Pellbridge agents](inside-the-pellbridge-agents.md), [commander's intent is a behaviour policy](commanders-intent-is-a-behaviour-policy.md), [the RiskMandate roadmap](the-riskmandate-roadmap.md), [our first customers](our-first-customers.md). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Agents & policyStartups & strategy[This article as a graph →](graphs.md#approved-business-mandates)

### Builds on

- [An analyst's blueprint for RiskMandate: what the companies at the WestCap CISO Summit suggest we build, the vendors already moving, and our answer](an-analysts-blueprint-for-riskmandate.md) An analyst's blueprint for RiskMandate from the WestCap CISO Summit, the vendors already moving, and our answer.
- [Drift is the mandate moving: an analyst's case for policy and behavioural drift as RiskMandate's thesis, and why a versioned behaviour policy is what drift is measured against](drift-is-the-mandate-moving.md) An analyst's case for drift as RiskMandate's thesis, and the versioned behaviour policy that drift is measured against.
- [What can your agent reach? RiskMandate and the Agent Behaviour Policy, explained for the person who has to decide](what-can-your-agent-reach.md) RiskMandate and the Agent Behaviour Policy in plain words: what it does, why it is not real time, which agents it covers, and how it gets into the room.
- [Inside the Pellbridge agents: six behaviour policies with the FCA's four elements filled in, one day of their work replayed through the gate, and the files that make it](inside-the-pellbridge-agents.md) Six invented bank agents with the FCA's four elements filled in, one day replayed through the gate: every incident came from a gap row.
- [Three policies for an agent: behaviour says what it may do, decision says who chooses, workflow says in what order](three-policies-for-an-agent.md) Behaviour says what an agent may do, decision who chooses at a branch point, workflow in what order. Zoom into one ABP cell and it becomes both.
- [Allowed is not right: an answer to Ashish Rajan's Northstar, with three policies and a twin you can run](allowed-is-not-right.md) Ashish Rajan's Northstar refund: allowed to refund $200, owed $120, paid $150. His four questions mapped to three policies, and tested on a twin.
- [Inside the Northstar twin: thirteen refunds, four designs, and every decision played back](inside-the-northstar-twin.md) A tour of the Northstar refund twin: thirteen synthetic refunds through four designs, every decision played step by step, replayed and compared.
- [Approve at altitude: decisions at every level, from strategy to one agent's step, where each level may narrow the one above and never widen it](approve-at-altitude.md) Models can draft two hundred decision policies; nobody can sign two hundred. Approve at altitude: each level may narrow the one above, never widen it.
- [Case law for agents: principles from the top, precedent from the cases, and how a decision earns its way into code](case-law-for-agents.md) Nobody predicts every case. Borrow the shape of English case law: escalate what the policy does not settle, record it, follow it, then compile it.
- [Three decisions, mapped: an agent's memory, this newsroom's release and a customer refund, through behaviour, decision and workflow](three-decisions-mapped.md) An agent's memory, this newsroom's release and a refund, mapped through behaviour, decision and workflow: the gaps are in the decisions.
- [Commander's intent is a behaviour policy: Sondera's argument in our words, the business layer above it, and five of our rules compiled to Cedar and tested](commanders-intent-is-a-behaviour-policy.md) Sondera's commander's intent and our behaviour policies are one idea: twelve terms joined, the business layer above, and five rules tested in Cedar.
- [A proposed roadmap for RiskMandate: policies, understand, risk acceptance, contain, manage and insure, a spectrum of trust we would walk with each customer](the-riskmandate-roadmap.md) A proposed strategy for RiskMandate, a spectrum of trust: policies, understand, risk acceptance, contain, manage, insure.
- [Our first customers: an early access programme for Agent Behaviour Policies, with credit to spend, a start-here site, daily follow-up, and a list for the next batch](our-first-customers.md) Agent Behaviour Policies move to execution: a first batch of customers with credit, a start-here site, daily follow-up, and a list for the next batch.

### Continued by

- [An analyst's blueprint for RiskMandate: what the companies at the WestCap CISO Summit suggest we build, the vendors already moving, and our answer](an-analysts-blueprint-for-riskmandate.md) An analyst's blueprint for RiskMandate from the WestCap CISO Summit, the vendors already moving, and our answer.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 254 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=254)

**Posting this article on LinkedIn?** The cover is [approved-business-mandates.jpg](banners/approved-business-mandates.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/approved-business-mandates.html)*
