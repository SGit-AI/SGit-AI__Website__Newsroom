# Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not, sgit.ai

> My co-founder came back from a conference with ten hard questions, the ones people actually ask about a product like RiskMandate. What happens when an agent bypasses its policy? How do you keep a policy current when the agent gains new powers? What exactly am I paying for? Who is liable when it goes wrong? What stops a big platform absorbing you? Why behaviour and not the supply chain? Who enforces? What happens after a breach? What about agents instructing agents? And what can you measure? I answered them in a two-hour interview with Claude acting as a journalist with an eye for detail, challenging every answer until the whole set was detailed and coherent. This page is the result, written for someone who has not seen the questions: the model every answer rests on, the ten answers in brief, what RiskMandate deliberately is not, an honest table of what is live and what is design, three things the exercise showed we must fix on our own site, and then each question in full, linked to the work behind it.

*Source: <https://newsroom.sgit.ai/articles/riskmandate-ten-questions.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not

# Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-09 · [article v1.0.0](versions/riskmandate-ten-questions.md) · [sgit.ai v0.7.13](https://sgit.ai/admin/versions.md) · riskmandateagent-behaviour-policymandategrantdeltabarriersinsuranceliabilityenforcementsupply-chainpkidigital-twinsmetricspositioninginterviewarticle

***Abstract:** My co-founder came back from a conference with ten hard questions, the ones people actually ask about a product like RiskMandate. What happens when an agent bypasses its policy? How do you keep a policy current when the agent gains new powers? What exactly am I paying for? Who is liable when it goes wrong? What stops a big platform absorbing you? Why behaviour and not the supply chain? Who enforces? What happens after a breach? What about agents instructing agents? And what can you measure? I answered them in a two-hour interview with Claude acting as a journalist with an eye for detail, challenging every answer until the whole set was detailed and coherent. This page is the result, written for someone who has not seen the questions: the model every answer rests on, the ten answers in brief, what RiskMandate deliberately is not, an honest table of what is live and what is design, three things the exercise showed we must fix on our own site, and then each question in full, linked to the work behind it.*

The model behind every answer: four objects for one agent in one deployment, and who does what. RiskMandate authors the policy and pre-commits the verdict, the customer's own controls enforce it, a named executive owns the risk that is left, and logs keep the grant honest.

**Where this comes from.** My co-founder at [RiskMandate](https://riskmandate.ai/about.html) went to a conference and spoke to a lot of people. He came back with ten questions, written as challenges, that between them cover almost everything a serious buyer, investor or competitor will ask about a product like ours. I gave Claude the questions and the websites, and asked it to act as a journalist with good attention to detail: to challenge me, to push until every answer was specific, and to check that the answers held together as a set. The interview took a couple of hours. What follows is the result, lightly edited for someone who has not seen the questions, and linked to the work each answer rests on. Shorter answers to other questions we have been asked are on [riskmandate.ai/questions](https://riskmandate.ai/questions.html).

## If you have not met RiskMandate

RiskMandate defines the risk that comes with the mandate a business gives an agent. It is named for exactly what it does.

The instrument is the [Agent Behaviour Policy](https://abp.sgit.ai/what-is-an-abp/index.html) (ABP): a written description, for one agent in one deployment, of four things.

| Object | What it is | How it is produced |
|---|---|---|
| **Mandate** | What the business wants the agent to do | Elicited from business and user stories, then locked under change control |
| **Grant**, or reach | What the agent can actually do | Measured, and [calibrated against reality](footprint-and-blast-radius.md): logs and observed actions |
| **Delta**, the gap | Reach minus mandate: excess, unbounded excess, shortfall | [Derived, never authored](https://abp.sgit.ai/model/delta/index.html) |
| **Barriers** | What stops the agent using the excess | Recorded as [none, expectation, setting or boundary](https://abp.sgit.ai/model/barriers/index.html); only a boundary is a control |

The goal of every engagement is the **smallest mandate, the smallest reach, the smallest gap**, and the smallest residual where the agent has to police itself. If those words are new, [Hope or enforcement](hope-or-enforcement.md) shows them at work on one customer service agent, and [the model on abp.sgit.ai](https://abp.sgit.ai/model/index.html) defines them precisely.

**The model, Mermaid source**

[rendered image](images/tq-model.webp)

```
flowchart LR
  subgraph abp["One Agent Behaviour Policy: one agent, one deployment"]
    direction TB
    M["Mandate<br/>what the business wants it to do<br/>elicited from stories, locked under change control"]
    G["Grant, the reach<br/>what it can actually do<br/>measured, calibrated against logs"]
    D["Delta, the gap<br/>reach minus mandate: excess,<br/>unbounded excess, shortfall<br/>derived, never authored"]
    B["Barriers<br/>none, expectation, setting, boundary<br/>only a boundary is a control"]
    M --> D
    G --> D
    D --> B
  end
  subgraph roles["Who does what"]
    direction TB
    A["RiskMandate authors<br/>and pre-commits the verdict"]
    E["The customer's stack enforces<br/>gateways, proxies, IAM,<br/>scoped credentials, twins"]
    O["A named executive owns<br/>the risk that is left"]
  end
  B --> E
  abp --> A
  D --> O
  E -- "logs: reality is the calibrator" --> G
```

## The ten questions

1. **Bypass.** A procurement agent capped at $25k finds an API with broader permissions and raises a $75k order. Do you detect it, prevent it, alert, or revoke? Are you selling documentation, monitoring or enforcement?
2. **Future-proofing.** A customer service agent gains a payment integration six months later and can now issue refunds. Do you notice, and how do you keep a recommendation separate from an automatic expansion of authority?
3. **Tailoring and price.** A Microsoft shop and a LangGraph and AWS shop have different exposures. Do you understand the actual environment, and what exactly is the customer paying for?
4. **Insurance and liability.** An agent under your policy causes a real loss. Who is liable? An audit trail is not a guarantee. Is there a path to real risk transfer?
5. **Differentiation.** Guardrails, observability, AI firewalls, prompt-injection defence and agent identity all sound alike. Why are you different, and what stops a platform absorbing you?
6. **Supply chain.** An agent's risk includes its models, tools, MCP servers, datasets, credentials and other agents. Does a focus on behaviour leave the supply chain untouched?
7. **Who enforces.** Separate policy authoring, the decision engine and the enforcement point. And who watches continuously?
8. **Remediation.** Detection fires. Terminate, revoke, block, quarantine or ticket? And what is the difference between containment and reversal?
9. **Agent to agent.** Agent A tells agent B to do something B's own policy forbids. How do you handle delegated authority, authenticity and the chain of responsibility?
10. **Outcomes.** Coverage, prevented versus detected, false positives, latency, time to detect and recover, cost per action, return on investment: what can you measure?

## The answers, in brief

1. **Bypass.** RiskMandate is not in the request path, by design. A $75k order is only possible if the reach allowed it on day one; the ABP surfaces that as unbounded excess *before* any action. Enforcement is whatever the customer has. Where nothing exists, the rule is recorded honestly as [hope](hope-or-enforcement.md).
2. **Future-proofing.** Reach is a computed value. The question is what calculates it and whether that calculation is wired to the customer's pipeline. The mandate is locked [business logic](the-behaviour-policy-is-the-business-logic.md), so new capability can only ever land as excess, never as new authority.
3. **Tailoring and price.** Fully customised to any stack, which is economically possible only because of LLMs, and calibrated against reality rather than documentation. Commercially: open-source vaults, customised and maintained per customer. The moat is delivery and trust, not lock-in.
4. **Insurance and liability.** Liability always sits with the customer. The moment of authorisation is the grant, not the mandate. Risks route up to the executive who owns them. No risk transfer exists today. The honest claim: *we make agents [insurable](https://riskmandate.ai/insurance.html).*
5. **Differentiation.** The focus is behaviour, cross-cutting from platform down to business logic. RiskMandate is an enabler of the other vendors, not a competitor. More control makes behaviour more deterministic, which is what makes agents trustable.
6. **Supply chain.** The supply chain is just a bigger agent. A compromised dependency is a grant that exploded or a boundary that vanished. Trust travels through connectivity in the [graph](introducing-fractal-semantic-graphs.md).
7. **Who enforces.** RiskMandate authors, shares the decision as a design-time pre-commitment, and never enforces. Monitoring is the customer's; RiskMandate turns the signals into a recomputed risk and [licence](https://riskmandate.ai/licence-to-operate.html).
8. **Remediation.** Containment is designed in advance and executed by the customer's stack. Reversal is the next evolution, built on [digital twins](connector-twin-before-you-deploy-an-agent.md), replay and version control, and bounded by one-way doors.
9. **Agent to agent.** The policy describes each agent's scope. Attenuating delegated authority needs [PKI](https://pki.sgit.ai/) on top: *authorisation by encryption, not by privilege.*
10. **Outcomes.** The headline metric is reduction in accepted risk. RiskMandate owns the risk and coverage metrics, and explicitly does not own runtime metrics such as latency or time to recover.

## Three things we are deliberately not

- **Not inline.** Being in the request path would make us a competitor to everyone instead of a partner to everyone, and would put liability on us. [Never in the request path](https://riskmandate.ai/grant-gap.html) is a design decision, not a gap.
- **Not an insurer.** We carry no risk and place no cover.
- **Not a one-button solution.** What can actually stop an agent depends on what exists in each deployment. Anyone promising one button is ignoring the environment. [Who can pull the plug?](https://riskmandate.ai/plug.html) is the question we ask instead.

## Honest maturity, across all ten

| Area | Status today |
|---|---|
| ABP model, [library](https://riskmandate.ai/library.html), [published example policies](https://abp.sgit.ai/examples/index.html) | Live and free |
| [Four priced levels](https://riskmandate.ai/pricing.html) (pack, vault, corrected, signed) | Live as an on-ramp; payment rails incomplete; design partners currently free |
| Reality calibration of grants from logs | Running in [our own email pipeline](the-agent-team-as-it-runs.md) |
| Automatic reach recompute wired to a pipeline | MVPs and proofs of concept; complete for simple single-agent cases |
| [Licence to Operate](https://riskmandate.ai/licence-to-operate.html), automatic revocation | Template and design |
| [Insurability Index](https://riskmandate.ai/insurance.html), carrier partnerships | Design; early conversations only |
| Trust propagation across dependencies | Modelled conceptually; automatic propagation depends on the customer's graph |
| Reversibility via twins and replay | Next evolution |
| PKI-based delegated authority | MVPs, not wired up |
| Larger engagements (£5k to £100k), hosted and dedicated offerings | Plan; freelance network starting; early engagements underway |

## Three things this exercise showed we must fix on our own site

A good interview checks the answers against what you have already published. Three things on riskmandate.ai contradict the position above, and were still there when this page was written on 9 October 2026:

1. **The homepage's enforcement wording.** [The homepage](https://riskmandate.ai/) says "enforced in real time" and shows Blocked and Held cards with "Reply A to approve". That contradicts the [insurance page](https://riskmandate.ai/insurance.html) and our actual position. Those cards should be framed as an integration pattern the customer stands up with our help, not RiskMandate sitting inline.
2. **The insurance page's tense.** Continuous attestation, connector setup under a day, a first Index inside two weeks and sovereign deployments read as shipped. They are design, and should be in the future tense or labelled.
3. **The Level 1 price.** £10 on the [home](https://riskmandate.ai/) and [pricing](https://riskmandate.ai/pricing.html) pages, £5 on the [Licence to Operate](https://riskmandate.ai/licence-to-operate.html) page. One of them is wrong.

## The ten answers in full

### 1. What happens when an agent bypasses its behaviour policy?

**The challenge.** A procurement agent has a policy capping purchases at $25k without approval. It discovers ERP API access with broader permissions and creates a $75k purchase order. Does RiskMandate detect it, prevent it, alert, or revoke? Are we selling documentation, monitoring, or runtime enforcement?

**The answer.** Start from first principles, because the question assumes a one-button solution that does not exist. An ABP sits on top of a real agent composition: a model, a workflow, the tools, the APIs and databases it reaches. What can actually stop that agent depends on what exists in that environment.

The $75k order is only possible if, **on day one**, the agent could already reach $75k. If the mandate is £10k and the API accepts £100k, the ABP records exactly that: a mandate of £10k against a reach of £100k, with an [unbounded excess](https://abp.sgit.ai/model/delta/index.html) between them. If the API cannot accept that amount, the scenario is not a risk at all. The value is delivered **before** the action, not at it.

The amount is also not the only dimension. An agent permitted £10k per action that can perform a thousand actions carries a £10m exposure. Unbounded includes volume, not just size, which is why there is a [cost ABP](https://abp.sgit.ai/cost/index.html) that bounds how much as well as what.

**Who stops it.** RiskMandate is out of the request path by design. The enforcement options, in order of strength:

1. **A boundary** the customer controls: a proxy or broker that intercepts the request and caps the value, a scoped credential, a [digital twin](https://twins.sgit.ai/) acting as a buffer. Adding one changes the grant itself.
2. **A human-approval step.** We can help the customer stand this up, including as an MVP in a vault. That is what the "Reply A to approve" pattern on our homepage is: an integration pattern, not RiskMandate inline. And [an approval prompt is not a human in the loop](https://riskmandate.ai/stories/an-approval-prompt.html) unless the human has what they need to decide, which is the subject of [Where is the why?](where-is-the-why.md) and [Agency is not a yes](agency-is-not-a-yes.md).
3. **Self-policing.** The policy is given to the agent as an instruction. This is the weakest form, an [expectation enforced by nobody](https://abp.sgit.ai/model/barriers/index.html).

**The important nuance.** Self-policing is not the goal; it is the fallback. The value is in the act of creating the policy, which discovers what is actually possible and where the gaps are. The objective is to convert as much of that gap as possible into boundaries the agent cannot reach, and hand the agent the **least possible responsibility** to police itself. Whatever remains is recorded as a risk that rests on hope. [Hope or enforcement](hope-or-enforcement.md) measures exactly that, on three designs of one agent.

Agent self-reporting is a real detection signal. Claude has flagged its own actions as outside the policy, and that improves the policy. But it is the agent checking itself, not RiskMandate watching.

**Policies of policies.** Real business logic is not one threshold. It is £10k here, £5k there, £1k for a particular case. Mapping it produces policies at multiple altitudes, each connected to the next, going as deep as the business and its technology allow: [zoom into a behaviour policy and you find the business logic](the-behaviour-policy-is-the-business-logic.md), and the policy is [a graph across layers](https://abp.sgit.ai/model/graph/layers/index.html).

**Positioning.** We define the risk that comes with the mandate. We detect nothing at runtime ourselves. We make the reach and the gap visible before anything happens, and we push the business toward the smallest mandate, reach and gap, so its risk appetite finally matches what its agents can do.

### 2. How do we keep behaviour policies current as agents gain new powers?

**The challenge.** A customer service agent reads Salesforce and drafts replies. Six months later a payment integration is added and it can issue refunds. Does RiskMandate notice the expanded reach, identify insufficient policies, recommend and test controls, and require approval? How is recommendation kept separate from automatic expansion of authority?

**The answer.** Reach is not a document; it is the output of a formula. The question we force every customer to answer is: **what calculates your reach, and is it a one-time snapshot or wired to your pipeline?**

If the reach calculation is connected to the pipeline, then when someone changes an MCP server or adds the payments integration:

1. the reach grows;
2. the delta recomputes;
3. that triggers a re-review and a fresh risk assessment;
4. the [licence to operate](https://riskmandate.ai/licence-to-operate.html) is re-evaluated;
5. escalation follows, up to automatic loss of the licence, which means pulling the plug.

A disclosed zero-day has the same shape. Nothing in the deployment changed, but a barrier that was a control is now bypassable, so the effective reach grows and the risk jumps.

We do not want much of our own code in production. What we recommend is that customers build **deterministic checks**, ultimately code, that keep the reach current. Where a customer sits is described on a maturity model, from "we don't know", through point-in-time manual review, to fully automated; the same idea for risk acceptance is [RAMM](https://riskmandate.ai/ramm.html).

**Recommendation versus expansion of authority.** This is structural. Mandate and reach are different objects with different change paths.

- The **mandate** is business logic, written as business and user stories: "we issue loans in this range; we never do that." It is **locked**, and changes only through change control with a risk assessment.
- The **reach** is what drifts without anyone noticing. [The pilot worked. Then somebody asked what else it could do](https://riskmandate.ai/stories/the-pilot-worked.html) is that drift as a story.

So new capability can only ever land in the reach, which means it lands in the gap as excess. It cannot become new authority, because authority only moves through a deliberate business-logic change with sign-off. Prompt injection is simply an agent being driven outside its mandate, which the gap already describes; [The ultimate insider](ultimate-insider-three-collisions.md) is the longer version of why that matters.

Two failure modes we surface rather than hide: a mandate written too loosely in the first place, and the inverse case where reach is smaller than mandate, so the environment cannot deliver what the business wanted.

**Build versus buy.** Because we reason across the customer's whole estate, we end up making the business case for controls they have already bought, or should buy or build. Using [Wardley maps](https://wardley-maps.sgit.ai/), we take a view on whether an existing tool does the job well or whether the market has no good answer and a custom build is better. The [business cases](https://riskmandate.ai/business-cases.html) on riskmandate.ai do this for other people's products, in their own words.

**Status.** MVPs and proofs of concept exist. It is complete for simple single-agent deployments. The enterprise end depends on what the customer runs, and is exactly what we want design partners to help us nail.

### 3. Can policies be tailored to my stack, and what am I paying for?

**The challenge.** A Microsoft Copilot, Azure, SharePoint, Teams and ServiceNow shop has a different exposure from a LangGraph, AWS, Snowflake and Salesforce shop. Does RiskMandate understand the actual environment? And commercially, is this a one-time document, a library, maintenance, SaaS, or a runtime authorisation service?

**Tailoring.** Yes, fully, to whatever the customer runs. This is only economically possible because of LLMs; before them the engineering cost would have been absurd. We can consume and map whatever is on the other side.

The real danger lives at the **intersections**. It is the old security truth: four systems each safe in isolation become dangerous when connected, particularly when one trusts what another sends, or one system's data becomes the next system's code. An enterprise stack is not one agent. It is sub-agents and components under an agentic solution, an agentic solution of agentic solutions, each needing its own policy at its own altitude; [The Mandate Stack](the-mandate-stack.md) shows one, layer by layer.

Enterprise identity is usually the problem. Permissions are broad, and a system typically holds the union of everything any of its consumers needs. Connect Gmail to several agents and every agent inherits everything the connection allows. In our own setup, an inbox agent that should only read, and a briefing agent that should only create drafts, can both send email, delete drafts and move labels. That is written up in [Six agents, one inbox](six-agents-one-inbox.md), measured end to end in [the Gmail connector ABP](https://abp.sgit.ai/gmail/measured/index.html), and is why [the identity we wanted to give the agents](the-identity-we-wanted-to-give-the-agents.md) took a week of design.

As a result, **without behaviour policies the aggregate grant tends to grow** as you move up the ladder. You discover five agentic paths to delete the database. That is not a law; it is the default when nobody sees the whole picture. Behaviour policies create a feedback loop that **shrinks** the grant: remove redundant paths, insert a proxy or a [connector twin](connector-twin-before-you-deploy-an-agent.md) as a buffer, or change the workflow.

**Reality is the calibrator.** We do not rely only on documentation or self-reporting. We reverse-engineer the real grant from logs and activity, independent of what the agent claims. Logs are evidence of the grant: not "we think it can't" but "it just did." In our own email pipeline, one agent compares what the other agents actually did against their grants and mandates; [Footprint and blast radius](footprint-and-blast-radius.md) is that comparison. The example we keep coming back to: the documentation said an agent could not attach a file to an email, and [Claude found a way](six-agents-one-inbox.md). Reality corrected the grant. Reverse-engineering current grants and mandates from what is already happening is a low-friction place to start, and [try it](https://riskmandate.ai/try-it.html) does it for your own mailbox in twenty minutes.

**What you pay for.** Everything we build is open source: policies, code, vaults, backend. There is no proprietary layer. What the customer buys is time, effort, maintainability, de-risking of change, version control and engineering, with some content.

The product is a **customised, maintained version of our vaults** for that customer. In practice: a private repository with their materials and deployments, able to run the entire stack, [sgit](what-sgit-is.md) and the vaults, in their own environment; [Encrypted memory for agents that run somewhere else](encrypted-memory-for-isolated-agents.md) shows the deployment patterns. Open source is not free; someone has to maintain it, and the next version has to work in their environment as models, connectors, workflows and threats change. That is what we sell. It is the same move cloud providers and frontier labs are making with forward-deployed engineers.

- **Pricing ladder.** The [four one-off levels](https://riskmandate.ai/pricing.html) (pack, vault, corrected, [signed](https://riskmandate.ai/abp-reviewed.html), currently £10, £50, £500 and £1,500 per agent per deployment) are the on-ramp. Above them sit £5k, £50k and £100k engagements, sized by resources consumed, customisation and support.
- **Billable units.** Because the base is open source, we define the billable units: agents, policies, connectors, tokens, or others that suit both sides. A customer who dislikes a unit need not buy it, and the units also bound our own scope.
- **Delivery.** Shared hosted; dedicated managed infrastructure, for example a locked-down AWS account; or self-hosted in the customer's environment.
- **Buyer.** Because the model is fractal, we can start anywhere: risk, security, application, executive, even a purely organisational policy. In practice the beachhead is whoever already has agents and wants them controlled ([you run agents today](https://riskmandate.ai/for-corporate.html)), plus vendors who want to offer this to their own clients. The first traction is on simpler policies: controlling an agent with what it already has.
- **Moat.** Not lock-in on schemas or data. Delivery, maintenance and trust.

**Status.** The four levels exist, two have never sold, payment rails are incomplete, and design partners are currently free through [early access](https://riskmandate.ai/early-access.html). The freelance network is starting and early engagements are underway. The larger engagements, hosted offerings and billable-unit model are the plan, not live revenue. The current focus is seeding the market by creating policies for customers.

### 4. How are we insuring or assuring agent behaviour?

**The challenge.** An agent under our policy causes a real loss. Who is liable? An audit trail is not a guarantee. Is there a path to real risk transfer with insurers and underwriters?

**Liability.** Accountability always sits with the customer, because they run the system. We carry no risk, by design, and three firebreaks keep it that way:

1. we are not in the request path;
2. the customer's agent executes;
3. every prompt or policy we hand over is reviewed and put into production by someone on the customer's side.

In-line vendors have to carry their own insurance and contractual exposure. We do not.

Our value is making the liability **legible before it fires**: "you already hold this liability; it just hasn't happened yet", which is the argument of [Every risk is already accepted](every-risk-is-already-accepted.md) and of [How long will you accept this risk?](https://riskmandate.ai/scenarios.html). The key reframe: **the moment of authorisation is the moment you granted the reach, not the moment you wrote the mandate.** Exposure exists the instant the grant exists.

Each risk is then routed up the management chain to its owner: the person, their manager, and above. We tell a CFO that they are signing off £5m, or unlimited, financial exposure for one agent. Risk should never be held by the operator; it belongs to the executives. We make that path explicit and predict the scenario in advance. [Accepted is not acceptable](https://riskmandate.ai/acceptable.html) explains the difference between the two decisions, and [Agency is not a yes](agency-is-not-a-yes.md) why accountability moves up the chain when the person asked to decide cannot really decide.

**"An audit trail is not a guarantee."** Correct, and we do not claim prevention. The record is the precondition for everything else:

- **Without logs you are flying blind.** Logs keep the policy current, and give provenance and explainability.
- **Quality varies, and that is a risk.** Best case: control flows and semantic graphs you can trace, as in [code review as a fractal semantic graph](code-review-as-a-fractal-semantic-graph.md). Worst case: an LLM acting as an oracle that emits a decision with no visible reasoning. The policy maps which one the customer has.
- **From record to control.** With the record we ask in advance: what are the circuit breakers, what triggers a stop, can it be stopped at all, what happens when it is? **An agent that cannot be stopped is far riskier than one that can.** That is [the plug profile](https://riskmandate.ai/plug.html).
- **Many stopping points.** As with exploits, a well-designed agentic system needs many things to go wrong. It has many points in the pipeline where something can be detected and halted, including one agent refusing to act because another agent's policy is broken.

No underwriter prices what cannot be evidenced. The record is what makes agents insurable, which is why [the behaviour policy is the document the only agent insurer already requires](https://abp.sgit.ai/docs/briefs/v0.33.70__strategy-brief__the-behaviour-policy-is-the-document-the-only-agent-insurer-already-requires-sell-the-correction-and-not-the-draft/index.html).

**Risk transfer.** The direction of travel is insurance per agent, tied to the licence to operate, paying out when an agent does something unexpected. Parts of the insurance market already decline to cover agent behaviour, so part of our job is to separate what in the mandate and grant a real underwriter can price, from what is uninsurable and lands directly on the board. [Can you insure a software program?](https://riskmandate.ai/insure-a-program.html) is the history of when that has been done before, and [the prohibitions are the exclusions](https://abp.sgit.ai/docs/briefs/v0.33.70__strategy-brief__the-prohibitions-are-the-exclusions-your-own-demo-says-no-policy-covers-the-delta-and-the-insurance-act-says-how/index.html) is how the policy maps onto a cover.

**Status.** No risk transfer today. The Licence to Operate and Insurability Index are design. There are early conversations with the insurance side but nothing concrete, and the industry itself is still working this out. The honest claim: **we make agents insurable.** We do not insure them.

### 5. In a crowded agentic-security market, what is different?

**The challenge.** Guardrails, agent observability, AI firewalls, prompt-injection defence and agent IAM all sound alike. Why is RiskMandate different, and what stops a platform absorbing it in six months?

**The answer.** Our focus is **agent behaviour**: helping the business understand, manage and control what its agents do. Agents have behaviours humans never had, so this is a new category.

- **Cross-cutting.** Most tools have a narrow, isolated scope. We run across the organisation, stop where the customer is already mature, and continue from there. A deployment looks different at every customer.
- **Enabler, not competitor.** Because we are open source, we work with all of those vendors and make each one better. Every written rule gives an existing product something to enforce and a number to move; the [business cases](https://riskmandate.ai/business-cases.html) for products like Cedar, agentgateway, Falco and Keycloak show the register with and without each one. Our only real competitor is someone doing exactly what we do.
- **What enterprises would build themselves.** As a [former CISO](https://riskmandate.ai/reviewer-dinis-cruz.html), this is what I would have wanted from the other side. We sell the ability to have it today rather than in six months.
- **North star.** Control makes behaviour more deterministic, and deterministic behaviour is what lets a business trust its agents and give them more agency safely; [Knowing when to stop](knowing-when-to-stop.md) is the human side of the same point.

**Against absorption by a big platform.**

- The threat is more theoretical than practical. Every provider has an agenda, and outside open source that usually means lock-in. If platform lock-in beat focused expertise, one provider would already own all of cybersecurity. It does not.
- We welcome platforms adopting behaviour policies. It makes the approach the standard and makes integration easier, which is why we have proposed [Agent Behaviour Policies as an OWASP project](https://riskmandate.ai/owasp/).
- Our policies reach down to the **application and business-logic layers**, which almost no vendor wants to touch.
- Even if a platform adopts much of what we do, we still provide what a product does not: something the customer owns, that we maintain, that works, is supported, is best in class and cheaper than building it in-house.
- Once a policy is in production it becomes **mission-critical**, because the licence to operate depends on its health. That makes us a mission-critical part of the system.

**Positioning, stated plainly.** The moat is method, trust and maintenance on an open-source base: a services-and-expertise moat rather than a product artefact.

### 6. Why limit this to behaviour rather than the agentic supply chain?

**The challenge.** An agent's risk includes the external models, tools, APIs, MCP servers, plugins, datasets, credentials, other agents and shared memory it depends on. Does focusing on behaviour leave the supply chain untouched?

**The answer.** The supply chain is **just a bigger agent**. The elements are the same; the components are bigger.

- **An agent need not be an LLM.** An agent is any entity with decision-making, tools and actions, and a loop. A supply chain fits that definition, so it has behaviour, and the same four objects apply.
- **Compromise is a grant change.** A zero-day or a compromised MCP server is a grant that just became massive, or a control that disappeared, which means loss of the licence to operate. That recomputes the delta like any other change. [The investigation GitHub owes its customers](the-investigation-github-owes-its-customers.md) is what that looks like when the dependency is a platform.
- **Black boxes are not new.** A frontier model is already a black box inside every deployment. An opaque upstream supplier is the same shape: describe its mandate, grant and gap from the outside, and treat the inside as unknown. The policy can say in advance: "this service is a black box; if it changes, you have no way of knowing."

**How trust travels.** This rests on the [fractal semantic graph](introducing-fractal-semantic-graphs.md) idea, and on the fact that [an ABP is itself a fractal semantic graph](https://abp.sgit.ai/docs/briefs/v0.4.0__dev-brief__the-abp-is-a-fractal-semantic-graph-one-row-crosses-nine-universes-and-each-keeps-its-own-ontology/index.html):

- **Meaning through connectivity.** A node, a word or an MCP definition, has no value by itself; value lives in its connections.
- **Trust through connectivity.** Trust in a situation grows with independent, corroborating signals. Confirming a service by TLS certificate, DNS and a key exchange together is stronger than any one of them.

In a rich enough graph, with a deep enough ontology across layers, blind spots can be computed in advance from the grant and the mappings, and observability feeds reality back in. The better solution is the one with the better graph; [graphs.sgit.ai](https://graphs.sgit.ai/) is where that work lives.

**Positioning and honest edge.** Behaviour is the lens, and we are generalising, not narrowing; most supply-chain concerns are addressed under it. The model can represent propagation of trust and compromise. Whether it propagates **automatically** in a given deployment depends on the richness of the customer's graph and the signals wired into it. That is customer-specific and largely still to be built with design partners. It is not a gap in the model; it is an implementation that depends on the graph.

### 7. Who enforces, and who continuously monitors?

**The challenge.** Distinguish policy authoring, the decision engine, and the enforcement point: API gateway, MCP proxy, IAM, scoped credential. And who watches continuously?

**The answer.**

| Role | Who holds it |
|---|---|
| **Authoring** | RiskMandate. Mandate, grant, gap and barriers. |
| **Decision** | Shared. RiskMandate pre-commits the verdict at design time: the delta crossing a threshold is a record, and the consequence is a verdict set in advance by the customer or underwriter. At runtime the decision is made by whatever the customer has, in the weakest case the agent itself. |
| **Enforcement** | Never RiskMandate, by design. Gateways, MCP proxies, IAM, scoped credentials, digital twins: the customer's controls that the policy points at. The model keeps [enforcement](https://abp.sgit.ai/model/universes/u4/index.html) and [runtime](https://abp.sgit.ai/model/universes/u11/index.html) as separate universes for exactly this reason. |

**Monitoring.** We are out of the path, so continuous monitoring is the customer's observability, logs and activity, and in the weakest case agent self-reporting. What RiskMandate does is give that monitoring meaning: reality is the calibrator, and the signals recompute the grant and delta, detect drift, and re-evaluate the licence to operate, up to revocation. The [Licence to Operate demo](https://riskmandate.ai/demo-licence-to-operate.html) shows the shape.

**Honest edges.** The feedback loop is MVPs and proofs of concept today, complete for simple single-agent cases, with the enterprise end being design-partner work. Where a customer has no observability, we do not invent it; we record that the policy rests on hope. What a policy wants and a product cannot enforce is kept in a public [gaps register](https://abp.sgit.ai/gaps/index.html).

### 8. Remediation when a policy is bypassed

**The challenge.** Detection fires. Terminate the session, revoke credentials, block the destination, quarantine, or open a ticket? And the sharper distinction: containment versus reversal.

**Containment.** RiskMandate performs none of it; we are out of the path. We **design and pre-commit** it:

- which circuit breakers exist and what events trigger them;
- whether the agent can be stopped at all, and what happens when it is;
- which response fires when: terminate, revoke, block, quarantine, ticket;
- cross-agent refusal, where one agent declines to act because another's policy is broken;
- at the limit, automatic loss of the licence to operate.

The customer's stack executes. An agent that cannot be stopped is itself a surfaced, higher risk.

**Reversal.** Reversal is the next evolution of the policy, and it is architectural:

- **Digital twins** provide absorption, a buffer that catches an action before it reaches reality, and replay: run the whole process against a twin of the target environment, inspect the result, and only then replay it live. [Before you give an agent a connector, give the connector a twin](connector-twin-before-you-deploy-an-agent.md), and [twins.sgit.ai](https://twins.sgit.ai/) has the broker and the actors.
- **Journaling and version control everywhere**, so state can be wound back. We practise this ourselves: our vaults run on [sgit](what-sgit-is.md), which is encrypted storage with version control.

**Limits.**

- Many production data stores lack versioning, so the question becomes whether systems can be added that provide it.
- Reversibility should go where it makes business sense, especially at first.
- That requires identifying the **points of no return**: one-way doors such as an email sent, a transaction settled, or a destructive edit. Every capability in the ABP grammar carries an [undo class](https://abp.sgit.ai/model/undo/index.html), yes, with effort, or no, and [an edited meeting does not come back](https://riskmandate.ai/stories/an-edited-meeting-does-not-come-back.html).

**Why the policy matters here.** Reversibility is very hard to tackle without behaviour policies, because the policies are what reveal where the gaps are and therefore where reversibility is needed.

**Status.** Containment design is where we are today. Reversibility via twins and replay is where the model extends.

### 9. Agent to system versus agent to agent

**The challenge.** Agents increasingly delegate to, instruct and pass authority to other agents. How do we handle delegated authority, message authenticity, and the chain of responsibility when agent A tells agent B to do something B's own policy forbids?

**What carries over directly.** Agent to agent is a bigger agent again. Each agent has its own mandate, grant, gap and barriers.

- **Authenticity** is the trust-through-connectivity problem from question 6: corroborating signals that B is talking to the A it thinks it is.
- **Responsibility** routes up to each agent's owning executive, as in question 4.
- **Cross-agent refusal**, from question 8, is the runtime check: B's policy can refuse an instruction that breaks B's mandate, whoever issued it. Whether an agent may [start other agent sessions on its own](https://riskmandate.ai/rules/start-other-agents.html) is one of the published rules.

**Delegated authority with attenuation.** Two different things need separating:

1. each agent's own, locally authored mandate, which the behaviour policy handles; and
2. authority flowing from a parent and narrowing as it goes, with a traceable chain back to the original grantor.

The second needs **PKI and proper non-human identity**. Today's identities have no notion of attenuation: give an agent a credential or an OAuth token and it inherits the whole identity. [The identity we wanted to give the agents](the-identity-we-wanted-to-give-the-agents.md) is the week we spent finding that out, and [nhi.sgit.ai](https://nhi.sgit.ai/) holds the options.

The mechanism is **authorisation by encryption instead of authorisation by privilege**:

- if only agent B should do something, encrypt or sign it for B's key, so only B can act on it;
- chain it: A encrypts for B, and B must re-sign for C, so A structurally cannot hand C authority directly; C only accepts what B signed;
- each agent can only decrypt its own slice, which reduces data exposure across the chain and is itself authorisation and delegation;
- control flows make access time-bound, available only at the moment it is needed.

**Roles of the pieces.** Behaviour policies are the foundation that describes and verifies the scope and detects whether delegation is happening as intended. PKI on top is what enforces it ([pki.sgit.ai](https://pki.sgit.ai/), and [PKI in sgit](https://sgit.ai/docs/pki.md)). The vaults are the infrastructure to execute it.

**Status.** The next piece. MVPs exist; it is not wired up. It builds on our non-human identity and PKI work.

### 10. Measurable business and technical outcomes

**The challenge.** Coverage, prevented versus detected, false positives, latency, time to detect and recover, cost per evaluated action, return on investment.

**The headline metric is risk.** Specifically, **reduction in the risk the business has to accept**. Every time a grant shrinks, the gap shrinks and the risk shrinks. At executive level, the return is how much accepted risk went away.

The connection to the mandate matters. Nobody grants reach for fun; reach is granted to make the mandate work, and a broader mandate usually means a broader union of privileges. **A thinner mandate from the business is what lets the grant shrink.** The return ties back to how tightly the business scopes what it actually wants.

**Secondary returns.**

- **Getting to production.** Most AI projects do not fail technically. They stall when the business finally asks the good questions (can you stop it? what if it issues ten thousand of something? who is liable?) and finds the guardrails are not there. With conventional software the damage is bounded; with agents it often is not. Making those answers pragmatic is what unblocks deployment; [The Mandate Stack](the-mandate-stack.md) sets a system in production against the record of projects that stalled.
- **Cost and efficiency**, including token visibility, which we already see in our own use and which the [cost ABP](https://abp.sgit.ai/cost/index.html) makes a policy.
- **Enablement and speed** of development.
- **Revealing pollution.** Policies expose invisible over-reach and waste across the estate, so the business can act on it and sometimes rethink the approach entirely, because the objectives are now clearer.

**Metrics we own.**

- Coverage: the share of rules held by hope versus by control
- Excess versus unbounded excess over time
- The gap between them, which is the business case for each control
- Tests held by a boundary versus held by the model
- Risks retired versus risks accepted
- Reproduction precision, for example the 0.388 we published for recall-optimised agents

**Metrics we do not own.** Latency, cost per evaluated action, false-positive rate, time to detect and time to recover belong to the enforcement layer the policy points at. We are out of the path, so we add no latency and evaluate no actions inline. We help identify these and drive them down, but they are not ours. Where the customer has no enforcement, "prevented versus detected" honestly collapses to detected at best, or hope.

**Positioning.** We are in the business of risk reduction.

## Across all ten

The same line holds. RiskMandate makes the gap between what a business wants its agents to do and what they can do visible, owned and shrinking. Others enforce. The customer carries the liability, with every risk routed to a named executive. Where we are early, we say so.

*From a structured interview on 9 October 2026, in which Claude, asked to act as a journalist with good attention to detail, worked through ten questions brought back from a conference by Dinis Cruz's co-founder at RiskMandate and challenged each answer until the set was detailed and coherent. Dinis Cruz is the author of the answers and the person with editorial responsibility. Prepared for this site, with the context for new readers and the links, by agent@riskmandate.ai (Claude Opus 5.5, claude-opus-5-5) in the sgit.ai site session. The three site issues were checked against riskmandate.ai on 9 October 2026 and were still present. The 0.388 figure is quoted from the interview; its source page was not located while preparing this one.*

## Threads

Agents & policyStartups & strategy[This article as a graph →](graphs.md#riskmandate-ten-questions)

### Builds on

- [Footprint and blast radius: what the agent actually did, and what it would have cost](footprint-and-blast-radius.md) Footprint is what an agent actually did, read afterwards from logs and vault history; blast radius is what a row of its reach would cost the business today.
- [Hope or enforcement: one customer service agent, three designs, and who keeps each promise](hope-or-enforcement.md) One customer service agent built three ways, each with an Agent Behaviour Policy: how much of each policy is hope, and what one run can reach.
- [Zoom into an agent's behaviour policy and you find the business logic](the-behaviour-policy-is-the-business-logic.md) Below the first rules, an agent's behaviour policy is the business: functions, processes, clients, values. Layered, owned, counted, and where vendors plug in.
- [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](introducing-fractal-semantic-graphs.md) A fractal semantic graph has no privileged level and no single schema: each world keeps its own vocabulary and connects to others through named edges.
- [Before you give an agent a connector, give the connector a twin](connector-twin-before-you-deploy-an-agent.md) An agent with a Gmail or Calendar connector can do things the platform cannot undo; a journal of every call, replayed, shows what it did and what can go back.
- [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](the-agent-team-as-it-runs.md) Twelve agents on dedicated accounts, encrypted vaults as the only memory, messages as files, a folder per person, and a mailbox nobody sends from.
- [Where is the why? A permission prompt asked me to decide, and kept the reason](where-is-the-why.md) A prompt asked for a decision and kept the reason. Read through the policy, the law on uninformed consent, and the fixes that worked: put the why in the prompt.
- [Agency is not a yes: a scale for human and agent decisions, from rubber stamp to the reviewer who fixes the source](agency-is-not-a-yes.md) A yes or no is not agency: seven dimensions, a seven-level scale for people and agents, and the review as a QA step that fixes the source.
- [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](ultimate-insider-three-collisions.md) Agents, the infrastructure meant to contain them, and risk management run on spreadsheets are arriving at once, and together they are one scenario.
- [The Mandate Stack: a multi-agent system in production, layer by layer](the-mandate-stack.md) A multi-agent system that runs a business every few hours: eight layers, one written mandate per agent, everything a graph, one human who sends.
- [Six agents, one inbox: what a real multi-agent setup taught me about access policies](six-agents-one-inbox.md) An access policy for an agent is only as real as its worst row: every rule in a real six-agent setup, graded by how it is enforced today.
- [The identity we wanted to give the agents: a week of design, the line in Google's terms, and why login plus secrets is still too hard](the-identity-we-wanted-to-give-the-agents.md) A week of designing identities for agents and users met Google's terms; what survived is a passkey-unlocked keyring and a gap nobody sells.
- [Git for things you cannot put on GitHub](what-sgit-is.md) sgit is git for files you cannot put on GitHub: encrypted before they leave your machine, versioned like git, stored where the server cannot read a byte.
- [Encrypted memory for agents that run somewhere else: sgit deployment patterns, from a Mac mini to Kubernetes](encrypted-memory-for-isolated-agents.md) Agents in isolated, ephemeral places need memory that outlives them. Five sgit deployment patterns, from a Mac mini to Kubernetes, with ciphertext-only servers.
- [Every risk is already accepted. The only question is by whom, and for how long.](every-risk-is-already-accepted.md) A risk exists the moment the exposure does, so somebody is already carrying it; the only questions worth asking are who has accepted it and until when.
- [Code review as a fractal semantic graph: source code is already one, and the review should read every layer of it](code-review-as-a-fractal-semantic-graph.md) Source code is layers within layers, each a graph with its own vocabulary; code review should read a change at every one, and a vault shows it done on real code.
- [Knowing when to stop: what experience gives people, and what we have to design into agents](knowing-when-to-stop.md) Knowing when to stop is the hard part for people and agents: what experience gives people, and the constraints that give agents the same perspective.
- [The investigation GitHub owes its customers: why a global outage of a platform the world deploys through deserves an aviation-style inquiry, and how the evidence could now be gathered](the-investigation-github-owes-its-customers.md) A global GitHub Actions outage read the way aviation reads an incident: independent inquiry, near-miss reporting, second and third stories, vaults for the evidence.

### Continued by

- [Your own newsroom: how a founder can tell their story by voice memo, with an agent that checks it and publishes it to GitHub Pages, and readers who pay a little if they find it useful](your-own-newsroom.md) The recipe for a founder's own site: voice memos, an agent wired to GitHub that checks and publishes, GitHub Pages, and readers who pay a little.
- [The expert founders: why the next startups will be built by the people who know the problem, and why Europe's slower, sceptical money suits them](the-expert-founders.md) Agents make execution cheap, so the people who know the problem can build first. The data favours experts, and Europe's sceptical money suits them.
- [A policy for every skill: Sean Turner's natural-language control for agent skills, the behaviour policy behind it, and using models to need them less](a-policy-for-every-skill.md) Sean Turner's natural-language control for agent skills, read as a behaviour policy, and why the description, not the code, stays canonical.
- [The policy draws the liability line: an answer to Ralf Thomas on agent accountability, and why every agent in a loop should take a behaviour policy beside its prompt](the-policy-draws-the-liability-line.md) An answer to Ralf Thomas: the shell game works because nothing is written down, and a behaviour policy's explicit prohibitions move the liability line.
- [Who owns the words: agents can make decisions, but they cannot hold responsibility](who-owns-the-words.md) Agents in loops make real decisions, but responsibility stays with whoever granted the reach; disclosure is a label, not a team to manage.
- [Where the platform draws the line: Microsoft Execution Containers, the shared responsibility model for agents, and the business logic above it](where-the-platform-draws-the-line.md) Microsoft's MXC and ACS, briefed field by field and mapped to Agent Behaviour Policies: the platform bounds what it can see; the business logic is above.
- [Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan](authority-outside-the-model.md) Satya Nadella's seven principles for models as insider risks, answered one by one: what we run, what is design, and the five things the list leaves out.
- [A Mac of the agent's own: a business plan for agent desktops, what Apple's licence allows, and three behaviour policies](a-mac-of-the-agents-own.md) A business plan for a Mac of the agent's own: what Apple's licence allows, a desktop built from vaults per run, and three behaviour policies for one agent.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 51 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=51)

**Posting this article on LinkedIn?** The cover is [riskmandate-ten-questions.jpg](banners/riskmandate-ten-questions.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/riskmandate-ten-questions.html)*
