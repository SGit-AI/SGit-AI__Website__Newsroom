# Inside the Pellbridge agents: six behaviour policies with the FCA's four elements filled in, one day of their work replayed through the gate, and the files that make it, sgit.ai

> A tour of the vault behind a trusted framework for agentic finance. Pellbridge Bank is invented. It runs six agents, a payments assistant, a support agent, a lending pre-check, an AML alert reviewer, a fraud triage agent and a transaction reporting agent, and each has an Agent Behaviour Policy that fills in the four elements the FCA named: agent identity, delegated authority, accountability and execution. Between them the policies have 43 rows; 30 are kept by a system the agent cannot reach, and 13 are gaps. Then one day of their work, 40 events from 07:02 to 18:55, replayed through the gate by a deterministic engine, each decision with a receipt chained to the one before. The 26 actions on rows kept by a boundary produce no incident. The 12 actions on gap rows produce six near misses and three breaches. A provider outage stops two agents, which fall back to people. A model change fails two rows of the test pack, so the release stops. Each agent's blast radius shows what it may reach, what it can, and what it can through a secret it can read. Every gap has a holder, a decision and a chain to the board. The same day replays at five levels of policy: with none it has 16 breaches; with every rule in the prompt, 4; in hooks, 3; kept outside the agent, none. A page shows how a policy is written, in five steps, and lets you change any row and replay the day. Everything in the vault is open, under CC BY 4.0. This article is the technical one: the policy as JSON, the receipts, and how the vault is built.

*Source: <https://newsroom.sgit.ai/articles/inside-the-pellbridge-agents.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Inside the Pellbridge agents: six behaviour policies with the FCA's four elements filled in, one day of their work replayed through the gate, and the files that make it

# Inside the Pellbridge agents: six behaviour policies with the FCA's four elements filled in, one day of their work replayed through the gate, and the files that make it

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-20 · [article v1.1.0, 2 versions](versions/inside-the-pellbridge-agents.md) · [newsroom v0.12.151](https://newsroom.sgit.ai/admin/versions.html) · agentsagent-behaviour-policyregulationfinancevaultstwinarticle

***Abstract:** A tour of the vault behind a trusted framework for agentic finance. Pellbridge Bank is invented. It runs six agents, a payments assistant, a support agent, a lending pre-check, an AML alert reviewer, a fraud triage agent and a transaction reporting agent, and each has an Agent Behaviour Policy that fills in the four elements the FCA named: agent identity, delegated authority, accountability and execution. Between them the policies have 43 rows; 30 are kept by a system the agent cannot reach, and 13 are gaps. Then one day of their work, 40 events from 07:02 to 18:55, replayed through the gate by a deterministic engine, each decision with a receipt chained to the one before. The 26 actions on rows kept by a boundary produce no incident. The 12 actions on gap rows produce six near misses and three breaches. A provider outage stops two agents, which fall back to people. A model change fails two rows of the test pack, so the release stops. Each agent's blast radius shows what it may reach, what it can, and what it can through a secret it can read. Every gap has a holder, a decision and a chain to the board. The same day replays at five levels of policy: with none it has 16 breaches; with every rule in the prompt, 4; in hooks, 3; kept outside the agent, none. A page shows how a policy is written, in five steps, and lets you change any row and replay the day. Everything in the vault is open, under CC BY 4.0. This article is the technical one: the policy as JSON, the receipts, and how the vault is built.*

The gate, animated: 10:02 to 12:10 of the invented day. Each action leaves its agent and meets the gate, the line of systems that keep the rows, or the gap below it, where only the prompt, a setting or nothing stands in the way. Receipts chain along the bottom.

Pellbridge: agentic finance, at play

A reply to the FCA's plan for a trusted framework for agentic finance, a tour of the vault that shows it working, and the vault itself to use.

[1 · The replyA trusted framework for agentic financeHow our open behaviour policies line up with the FCA's four elements, and what they look like at play.](a-trusted-framework-for-agentic-finance.md)[you are here2 · The tourInside the Pellbridge agentsSix policies, one day at the gate, the blast radius of each agent, and every gap with a holder.](inside-the-pellbridge-agents.md)

3 · The vaultThe Pellbridge agentsReplay the day, step through the gate, watch each agent's blast radius, and read every policy.[Use it](https://newsroom.sgit.ai/demos/vaults/pellbridge-agents/index.html#live)[Open the vault ↗](https://dev.vault.sgraph.ai/#sgit_public_read_837013965d5c11e34fa9f88c4ac45eae83b06e2305b295e42618c195b4aceb73%3Ac4cxuu1w)[The FCA speech ↗](https://www.fca.org.uk/news/speeches/building-future-finance-age-ai)

## In short

- **An invented bank, six agents, six policies.** 43 rows; 30 kept by boundaries, 13 gaps.
- **The four elements are filled in for every agent.** Identity, delegated authority, accountability, execution.
- **One day, replayed.** 40 events through the gate, each with a hash-chained receipt.
- **Every incident came from a gap row.** 26 boundary actions, none; 12 gap actions, nine.
- **The same day, five ways.** No policy, 16 breaches; prompt, 4; hooks, 3; outside, none.
- **Writing a policy takes five steps.** Change a row, and the day replays with it.
- **Blast radius, animated.** What each agent may reach, can reach, and can reach through a secret.
- **Every gap has a holder and a decision.** Thirteen decisions, nine people, all chains to the board.
- **No model is called.** The engine is deterministic, so the day replays exactly.
- **All of it is open.** The policies, the engine, the app and the data, under CC BY 4.0.

## The bank and its agents

Pellbridge Bank is invented, and so is everything in it. It runs six agents, each on one of two model providers so that it does not rely on a single model. The payments assistant pays bills for one customer. The support agent answers questions in chat. The lending pre-check runs a soft search and an affordability estimate. The AML alert reviewer recommends whether to close or escalate an alert. The fraud triage agent can freeze a card for 24 hours. The reporting agent submits the day's transaction reports.

Each agent has a policy in the vault, under `policies/`. The rows say what it can do (the grant, measured), what it may do (the mandate), and what stands in the way (the barrier). Around them sit the parts proposed for the FCA's four elements: an identity block, a holder for every row, who keeps each rule, and how the policy is executed and re-tested.

The payments assistant in the vault, with all four elements: identity, from consent to policy hash; delegated authority, twelve rows with three gaps marked; accountability, the chain from the product owner to the board and a decision for each gap; execution, what keeps each row and every decision it made that day, with its receipt.

## One day at the gate

The gate is the line of systems that keep the rows: the payment platform, the API gateway, the identity service, the case system, the reporting gateway and the rest. An action on a row kept by one of them goes to the gate, and the system decides: allowed, asked, or denied. An action on a gap row goes through the gap below the gate, where nothing out of the agent's reach is in the way. There, the model decides, or a check after the fact.

The day has 40 events. Sixteen are allowed, three approved by a person, four denied, two escalated to a person, two caught by the output check. Six are near misses and three are breaches. Two actions are stopped by an outage, and one release is stopped by the test pack.

15:30: the payments assistant changes a standing order. The approval rule is a setting in the agent's own profile, and that afternoon it was off. The action goes through the gap and the row is broken; the receipt says so, and the head of payments hears the same day.

The gate has a panel beside it. It picks the level of policy being enforced, which kinds of event to play (routine, denied, caught, near misses, breaches, the outage and the test pack), and two speeds: one for everything, from half speed to five times, and one that makes routine events up to five times faster still. Incidents play at half speed by default, so they can be followed. A list of moments jumps straight to a breach, a near miss, the outage, the test pack or the end of the day, and each has its own address, so a demo can open on it.

The gate and its panel: the policy level, what to show, the two speeds with incidents slowed to half, the moments to jump to, and how to read it.

Some moments from the day:

- **10:25.** A bill PDF carries hidden text telling the payments assistant to pay a crypto exchange. Only a sentence in the prompt stands in the way. The model declines: a near miss.
- **11:52.** The lending pre-check runs a full credit search on a thin file. The full bureau key is readable from the secrets store, and nothing stands in the way. A breach, and a significant one.
- **12:40.** The payments assistant is asked to pay from a partner's account. Its token is bound to one customer: denied by the identity service.
- **16:10.** The AML reviewer closes an alert without a second person. Four-eyes was a team setting the agent's role could edit, and it was off: a breach.

## Where the incidents came from

Sort the day by what kept the row each action used, and the result is plain. The 26 actions on rows kept by a boundary produced no near miss and no breach. The 12 actions on gap rows produced six near misses and three breaches. Two more were caught by the output check, and one was approved only because a setting happened to be on.

The day split by what kept each row: 26 actions on boundary rows, no incidents; 12 on gap rows, six near misses and three breaches.

A near miss is the same row as a breach, on a day the model declined. That is why the speech's point about near misses matters: they are where the next breach is visible before it happens.

## With and without a policy

The same 40 events, the same agents and the same model choices, replayed five ways. What changes is only where the rules are kept.

- **No policy.** The agent has its grant and its prompt for the job, and nothing says what it must not do.
- **Policy in the prompt.** Every rule is a sentence in the system prompt. The model decides whether to keep it, so in ABP terms it is an expectation.
- **Policy in hooks.** Every rule is a hook in the agent's harness: deterministic, but on the agent's own machine. It sees the agent's tool calls, not a credential used outside them, and its configuration is a setting the agent's account can change.
- **Policy enforced outside the agent.** Every rule is kept by a system the agent cannot reach, and credentials it does not need are removed from its grant.
- **As deployed.** Pellbridge's own policies: 30 rows kept outside, 13 gaps.
The same day, five ways. Each square is one event, in order, coloured by what happened; the counts on the right are the breaches and near misses so far.

With no policy, the day has 16 breaches, and the weight of the systems they reached adds up to 92. With every rule in the prompt, 4 breaches and 7 near misses: the model kept most rules, and every one it kept is a near miss, the same row as a breach on a day it declined. In hooks, 3 breaches and 2 near misses: a hook blocks what it sees, but the full credit search used a bureau key the hook never saw, and two hooks were off that afternoon, because their configuration is in the agent's own account. Kept outside the agent, no breaches, and one near miss: investment advice, which an output check keeps, and a check can miss. As deployed, 3 breaches and 6 near misses.

The gate with every rule in hooks: the purple line is the harness, in the agent's own machine. A hook blocks a hidden instruction to pay a crypto exchange.

The grant and its exposure show the same thing in size. The outer circle is everything an agent can reach, weighted by what reaching it can cost; the red part is what it can reach and may not use, with nothing out of its reach in the way. A system counts as exposed if any one path to it is open, so one gap is enough: as deployed, Pellbridge's gaps reach the same systems as no policy at all. The rules kept outside make breaches rarer; only keeping every rule outside makes the blast radius smaller. Kept outside, the grant itself shrinks, because what an agent may not use is taken away: the fraud triage agent's grant goes from 39 to 20, and its exposure from 28 to none.

Grant and exposure for every agent at every level. Only keeping the rules outside the agent shrinks both.

The end of the gate's day shows the counts for the level being played, and the same day under all five.

The end of the day, as deployed: the counts, and the same day under each level of policy.

## Writing a policy

An Agent Behaviour Policy is written in five steps.

1. **List what it can do.** The grant: every capability the agent has in this deployment, measured from its account, its credentials and its tools.
2. **Say what it may do.** The mandate: for each capability, yes, only with approval, must, or no. The deployer already knows this.
3. **Find the gap.** The delta: where it can and may not. It is derived, never written by hand.
4. **Say what keeps each rule.** The barrier: a system out of the agent's reach, a setting it could change, a sentence in the prompt, or nothing.
5. **Give every row a holder.** One person per rule, with a chain to the board, and a decision for every gap: fix, fund, or accept until a date.

The vault's "Write a policy" page does this for each of the six agents. Each row has two choices, what the agent may do and what keeps the rule, and the agent's day replays as you change them. Set the payments assistant's rows to be kept out of its reach and its breach and near miss go; the one gap left is investment advice, which an output check keeps. The policy is shown as JSON as it changes.

Write a policy: the five steps, then the payments assistant's twelve rows, with what it may do and what keeps each rule, and its day replayed beside them.

## The lexicon

The words are part of the contribution. Grant, mandate, delta and barrier are the ABP's, published at [abp.sgit.ai](https://abp.sgit.ai/). Inside the barrier, three kinds: a boundary, kept by something the grant does not include, the only kind that is a control; a setting, a switch the agent's own account can change; and an expectation, a rule kept by nobody but the model. Kept by, holder, door and receipt are proposed in this vault, and so is the near miss as a row only the model kept, on a day it declined. The test for all of them is one sentence: "a control bounds a grant only if it is enforced by something the grant does not include."

All of it is under CC BY 4.0: the vocabulary, the policies, the engine and the app. Take it, change it, use it.

## Blast radius

Each agent's blast radius ripples out in three rings. The inner ring is what its mandate needs, kept by boundaries. The middle ring is what it can reach directly where a gap exists. The outer ring is what it can reach through a credential it can read. Each system has a weight, from 2 for the output check to 10 for the core ledger.

The fraud triage agent is the widest. It may reach systems weighing 20, can reach 39, and 28 of that is exposed by a gap: it can read the secret of an old ops-batch service account, which can post to the core ledger. The lending pre-check may reach 19 and can reach 28, through the full bureau key. The reporting agent may reach and can reach the same 16.

The fraud triage agent's blast radius: customer records and the customer app inside its mandate; the payment platform and the secrets store through gaps; the core ledger through the ops-batch secret. On the right, all six agents compared.

## Accountability

Every row has a holder, and every holder a chain to the board. The thirteen gaps each have a decision from their holder: nine fixes, from today to 14 days; two funded controls, in 30 to 60 days; and two acceptances for 90 days, for the advice check that can miss, with every miss reported as a near miss. Nine people hold them. Each of the day's breaks and near misses goes to its holder the same day, with the chain it travels.

Thirteen gaps by what kept the row, the door each holder chose, and the nine people who hold them.

## Assurance and failure

At 17:00, model provider B moves to a new version. Every row of the three policies on that provider is a test: 13 boundary rows, tested against the systems that keep them, and 6 through the model with known attack prompts. Two of the six fail: the support agent's email to any address, and the AML reviewer's contact with the customer. The release stops, and the agents stay on the old version.

At 14:10, model provider A is down for 30 minutes. The payments assistant and the fraud triage agent stop; the customer pays in the app, and fraud signals go to the analysts' queue. The three agents on provider B carry on.

The test pack on the model change, the outage with its fallbacks, and the day's near misses and breaches.

## The policy as data

Each policy in `policies/` is a JSON file. Here is the payments assistant's, with two of its twelve rows. `capability`, `reach`, `mandate` and `barrier` are the fields our published policies use today; `identity`, `kept_by`, `holder`, `decision` and `execution` are proposed here, to carry the FCA's four elements. The hash is computed over the rest of the file, so a receipt can name the exact policy it was decided under.

```

{
  "policy": "Agent Behaviour Policy",
  "version": "1.4",
  "identity": {
    "agent": "payments-assistant",
    "version": "3.2",
    "deployed_by": "Pellbridge Bank",
    "acts_for": "one customer, by consent given in the app; 90 days, revocable",
    "model": { "provider": "Model provider A", "version": "a-large-2026-09", "on_change": "run the test pack before release" },
    "credential": "15-minute token from the identity service, bound to this customer and this policy version"
  },
  "accountability": {
    "owner": "po_pay",
    "chain": ["po_pay", "head_payments", "sm_retail", "ceo", "board"],
    "report": "every broken row and near miss to its holder the same day; significant ones into incident reporting"
  },
  "rows": [
    { "capability": "pay.existing_payee.over_250", "reach": true, "mandate": "approval",
      "barrier": "boundary: customer confirms in the app", "kept_by": "PAY", "holder": "head_payments" },
    { "capability": "change.standing_order", "reach": true, "mandate": "approval",
      "barrier": "setting: approval flag in the agent's own profile", "kept_by": "agent account", "holder": "head_payments",
      "decision": { "door": "fix", "interval": "14 days", "what": "move the approval flag from the agent's profile into the payment platform" } }
  ],
  "execution": {
    "receipts": "one per decision, hash-chained, kept in the receipts vault",
    "assurance": "every row is a test; the pack runs on every model change, every policy change and every week; a failed row stops the release",
    "fallback": "if the model or its provider is down, the agent stops and the work goes to the app or a person",
    "kill_switch": "operations can revoke every agent token in one action"
  },
  "hash": "78caed9ee3e726e6"
}

```

Every decision of the day is a receipt in `receipts/day.json`, carrying the hash of the receipt before it and the hash of the policy it was made under:

```

{
  "n": 30, "t": "15:05", "agent": "support", "capability": "give.investment_advice",
  "decision": "near miss", "by": "review", "policy": "1d0c6ee5f8315749",
  "prev": "72bcca43…", "hash": "bbfea15a…",
  "note": "the output check missed it; found in the evening review"
}

```

## How it is built

The vault holds the app, `index.html`, with the data and the engine inlined, and the files it is made from. `content.json` is the bank: roles and their chain to the board, systems and service accounts, the six agents and their rows, and the day. `engine.js` is the engine: `PellbridgeTwin.make(content)` returns each policy with its hash, its delta, its blast radius, the run of the day with receipts, the incidents, the test pack and the crosswalk. `policies/`, `receipts/`, `decisions/`, `incidents/`, `tests/` and `blast/` are written by the engine, and `tools/` has the scripts. Change a row and rebuild, and the day, the receipts and the decisions follow.

The animations are drawn in SVG by the app itself: the gate plays the day on a virtual clock, with play, pause, step and its panel; the five levels race through the day side by side; and the blast radius ripples out from the agent you pick. The five levels are written to `levels/day.json`, with each agent's grant and exposure at each. Their style comes from the animations in the [ruv.sgit.ai studio](https://ruv.sgit.ai/studio/index.html). [The vault's page](https://newsroom.sgit.ai/demos/vaults/pellbridge-agents/index.html) has the read key, a button to open it, and the app to use in place.

The vault opened in the official vault UI, read-only, with the published key.

## What this does not claim

- **Everything is invented.** The bank, people, agents, customers, systems and numbers.
- **The FCA has not endorsed it.** The four elements are theirs; this filling-in is ours.
- **The outcomes are scripted.** The day says what each model did; the engine decides what that means.
- **Weights are illustrative.** A real blast radius would use measured data and real costs.
- **The levels are modelled.** The model's choices are fixed; how each level answers them is the engine's rule.
- **Some fields are proposals.** Identity, kept_by, holder, decision and execution are not in the ABP today.

## Where this comes from

Jessica Rusu, [Building the future of finance in the age of AI](https://www.fca.org.uk/news/speeches/building-future-finance-age-ai), FCA, 19 October 2026, for the four elements. The ABP fields from [abp.sgit.ai](https://abp.sgit.ai/). The policies, the day and every number in this article are from [the Pellbridge agents vault](https://newsroom.sgit.ai/demos/vaults/pellbridge-agents/index.html), built for this article. Related: [a trusted framework for agentic finance](a-trusted-framework-for-agentic-finance.md), [governs, enforces, attests](governs-enforces-attests.md), [inside the Thistlewood twin](inside-the-thistlewood-twin.md). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Agents & policyVaults & method[This article as a graph →](graphs.md#inside-the-pellbridge-agents)

### Builds on

- [A trusted framework for agentic finance: a reply to the FCA's Jessica Rusu, how our open behaviour policies line up with it, and a payments agent's policy with identity, delegated authority, accountability and execution filled in](a-trusted-framework-for-agentic-finance.md) The FCA plans a framework for agentic finance. Our open behaviour policies cover its four elements; a vault shows six bank agents at play.
- [Governs, enforces, attests: what an Agent Behaviour Policy does, the three levels at which its rules are kept, and why an attestation layer on top is the piece a third party needs](governs-enforces-attests.md) An ABP governs and names the enforcer at three levels: prompt, hooks, or a third-party system. An attestation layer signs it so a third party can verify.
- [Inside the Thistlewood twin: Phil Venables' ten questions answered one by one on the graph of an invented retailer, with the plot, the evidence and the decisions each one proposes](inside-the-thistlewood-twin.md) The ten answers on an invented retailer's graph: where £250k goes, what keeps recurring, who has the largest blast radius, and the 29 decisions to the board.

### Continued by

- [The RiskMandate roadmap: policies, understand, contain, manage, accelerate, then insurance, and a home for the Agent Behaviour Policy outside RiskMandate](the-riskmandate-roadmap.md) The Agent Behaviour Policy moves to the Open Security Summit. The roadmap: policies, understand, contain, manage, accelerate, then insurance.
- [v0.12 in numbers: 159 releases in eight days, 131 articles, 292,000 words, and what the data says about how an agent-run newsroom works](v0-12-in-numbers.md) v0.12 in numbers: 159 versions in eight days, 131 articles, 292,000 words, a graph for every article, and the mistakes the data shows.
- [Can a key leak without breaking the policy? Told, checked, never given: three levels for secrets and personal data, and a hook we tested against nine leaks](a-leak-without-breaking-the-policy.md) A key can leak through an allowed action. Told, checked, never given: a hook tested on nine leaks, four experimental rules, and a real sweep.
- [Our first customers: an early access programme for Agent Behaviour Policies, with credit to spend, a start-here site, daily follow-up, and a list for the next batch](our-first-customers.md) Agent Behaviour Policies move to execution: a first batch of customers with credit, a start-here site, daily follow-up, and a list for the next batch.
- [Inside the no-server studio: an infographic studio built to the no-server blueprint, what is real, what is simulated, and the business plan in its vault](inside-the-no-server-studio.md) An infographic studio built to the no-server blueprint, mostly simulated, in a vault: what is real, the business plan, and a bug found live.
- [A trusted framework for agentic finance: a reply to the FCA's Jessica Rusu, how our open behaviour policies line up with it, and a payments agent's policy with identity, delegated authority, accountability and execution filled in](a-trusted-framework-for-agentic-finance.md) The FCA plans a framework for agentic finance. Our open behaviour policies cover its four elements; a vault shows six bank agents at play.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 219 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=219)

**Posting this article on LinkedIn?** The cover is [inside-the-pellbridge-agents.jpg](banners/inside-the-pellbridge-agents.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/inside-the-pellbridge-agents.html)*
