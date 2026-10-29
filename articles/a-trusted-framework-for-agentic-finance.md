# A trusted framework for agentic finance: a reply to the FCA's Jessica Rusu, how our open behaviour policies line up with it, and a payments agent's policy with identity, delegated authority, accountability and execution filled in, sgit.ai

> Jessica Rusu, the FCA's chief data, information and intelligence officer, said today that the FCA will work with industry, other regulators and frontier labs on a trusted framework for agentic finance, with clear approaches to agent identity, delegated authority, accountability and execution. Most of what she asks of firms is something we have been writing about and publishing openly here: Agent Behaviour Policies that put what an agent can do beside what it may do, a holder for every risk with a chain to the board, rules kept by something the agent cannot reach, breaks and near misses reported, and policies as graphs. This is a crosswalk from her points to that work, and a worked example in a vault: an invented bank with six agents, each with all four elements filled in, and one day of their work replayed through the gate. Every near miss and breach that day came through a gap, a row kept only by the prompt, a setting or nothing; the rows kept by systems the agent cannot reach held. It is all CC BY. The FCA, or anyone building the framework, could adopt it, or write their own; and policies written as graphs can be connected with edges, without either side adopting the other's schema.

*Source: <https://newsroom.sgit.ai/articles/a-trusted-framework-for-agentic-finance.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / A trusted framework for agentic finance: a reply to the FCA's Jessica Rusu, how our open behaviour policies line up with it, and a payments agent's policy with identity, delegated authority, accountability and execution filled in

# A trusted framework for agentic finance: a reply to the FCA's Jessica Rusu, how our open behaviour policies line up with it, and a payments agent's policy with identity, delegated authority, accountability and execution filled in

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-19 · [article v1.5.0, 6 versions](versions/a-trusted-framework-for-agentic-finance.md) · [newsroom v0.12.151](https://newsroom.sgit.ai/admin/versions.html) · agentsagent-behaviour-policyregulationfinanceaccountabilitygraphsarticle

***Abstract:** Jessica Rusu, the FCA's chief data, information and intelligence officer, said today that the FCA will work with industry, other regulators and frontier labs on a trusted framework for agentic finance, with clear approaches to agent identity, delegated authority, accountability and execution. Most of what she asks of firms is something we have been writing about and publishing openly here: Agent Behaviour Policies that put what an agent can do beside what it may do, a holder for every risk with a chain to the board, rules kept by something the agent cannot reach, breaks and near misses reported, and policies as graphs. This is a crosswalk from her points to that work, and a worked example in a vault: an invented bank with six agents, each with all four elements filled in, and one day of their work replayed through the gate. Every near miss and breach that day came through a gap, a row kept only by the prompt, a setting or nothing; the rows kept by systems the agent cannot reach held. It is all CC BY. The FCA, or anyone building the framework, could adopt it, or write their own; and policies written as graphs can be connected with edges, without either side adopting the other's schema.*

The FCA's points from the speech, set against our open work that covers the same ground.

Pellbridge: agentic finance, at play

A reply to the FCA's plan for a trusted framework for agentic finance, a tour of the vault that shows it working, and the vault itself to use.

[you are here1 · The replyA trusted framework for agentic financeHow our open behaviour policies line up with the FCA's four elements, and what they look like at play.](a-trusted-framework-for-agentic-finance.md)[2 · The tourInside the Pellbridge agentsSix policies, one day at the gate, the blast radius of each agent, and every gap with a holder.](inside-the-pellbridge-agents.md)

3 · The vaultThe Pellbridge agentsReplay the day, step through the gate, watch each agent's blast radius, and read every policy.[Use it](https://newsroom.sgit.ai/demos/vaults/pellbridge-agents/index.html#live)[Open the vault ↗](https://dev.vault.sgraph.ai/#sgit_public_read_837013965d5c11e34fa9f88c4ac45eae83b06e2305b295e42618c195b4aceb73%3Ac4cxuu1w)[The FCA speech ↗](https://www.fca.org.uk/news/speeches/building-future-finance-age-ai)

## In short

- **The FCA is building a framework for agentic finance.** Agent identity, delegated authority, accountability and execution.
- **Most of it is what we have been publishing.** Behaviour policies, risk acceptance, enforcement levels, near misses, graphs.
- **Delegated authority is the gap between can and may.** That is what an Agent Behaviour Policy writes down.
- **Accountability needs a holder per rule.** With a chain to the board, as in our risk acceptance work.
- **Execution is who keeps each rule.** The prompt, a hook, or a system the agent cannot reach.
- **A worked example, at play.** An invented bank, six agents, all four elements, in a vault.
- **Every incident came from a gap.** Boundary rows held; near misses and breaches came through the gaps.
- **The same day without a policy.** 16 breaches; kept outside the agent, none.
- **It is open, CC BY.** Adopt it, or write your own; policies as graphs can be connected.

## What the FCA said

Jessica Rusu, the FCA's chief data, information and intelligence officer, spoke today at Bloomberg's UK Policy Series, under the title [Building the future of finance in the age of AI](https://www.fca.org.uk/news/speeches/building-future-finance-age-ai). The FCA's page says it is the drafted version and may differ from what was delivered; the quotations below are from that page.

Her starting point is that "Adoption is not coming. It is here." A joint survey with the Bank of England, due next week, shows 86% of firms using AI. The FCA is putting six of the seven recommendations of the Mills Review into live work, and she was clear about the style: "Our response to the review is not to consult, study and report progress."

She shared good and poor practice under three themes: putting the consumer first, knowing who is accountable, and operational resilience. On accountability, firms need "clear accountability, risk-based controls, human oversight, escalation triggers, and senior managers personally accountable for AI systems", and some firms "retrofit governance after technology has already been deployed". Her verdict on that: "That is the wrong way around." On resilience: stress-test, plan for failure, keep fallbacks, and understand supplier concentration, "including reliance on a single model".

Then agents. Incident reporting "must extend to significant AI failures and near-misses". Assurance has to change, because "A system that is safe at deployment may behave differently at scale, under stress or as the models beneath it change. Agentic systems therefore require continuous, conditional assurance." And the commitment I am replying to: "The FCA will work with industry, fellow regulators and frontier labs to develop a trusted framework for agentic finance, including clear approaches to agent identity, delegated authority, accountability and execution."

She ended with "Let's build it together." This is my contribution to that.

## Four elements we have been writing about

Reading the speech, I recognised almost every point. We are working on the same problem, and it leads to similar answers.

- **Delegated authority** is the gap between what an agent can do and what it may do. That is the core of an [Agent Behaviour Policy](what-can-your-agent-reach.md): the grant (everything it can do, measured), the mandate (what it was authorised to do), the delta between them, and the barrier, what actually stands in the way of each capability. It is published openly at [abp.sgit.ai](https://abp.sgit.ai/), under CC BY.
- **Execution** is how each rule is kept. In [governs, enforces, attests](governs-enforces-attests.md) I described three levels: in the prompt, which is a hope; in hooks, which are deterministic but sit on the agent's own machine; or by a third-party system that does the blocking, which is the level we recommend. The test, from the ABP: "A control bounds a grant only if it is enforced by something the grant does not include." [Policy as code needs a policy first](policy-as-code-needs-a-policy-first.md) adds one more question: for every rule that is code, who can change that code.
- **Accountability** is a holder for every rule. Our work on [risk acceptance](every-risk-is-already-accepted.md) says every risk is already being carried, so the only questions are who has accepted it and until when; every holder has a boss, and every path ends at the board. [The policy draws the liability line](the-policy-draws-the-liability-line.md) is the same idea for agents: without a written policy, nobody can point to what the agent was told not to do.
- **Agent identity** is the one we have written least about, and the speech puts it first. In the ABP it is implicit: a policy is for one agent in one deployment. The attestation layer in [governs, enforces, attests](governs-enforces-attests.md) makes it explicit: what was assured, at which policy version, signed so a third party can check it without taking the operator's word.

The themes line up too. Governance written before deployment is [a policy beside the prompt](a-policy-beside-the-prompt.md), which also proposes a breach report the same day for every broken row and every near miss. Continuous assurance is a versioned policy whose rows are re-tested, with a receipt for every decision. Resilience and single points of failure are graph questions, which the [Thistlewood twin](ten-questions-one-graph.md) answers for an invented retailer.

## A worked example: Pellbridge Bank

The speech mentions the AI Lab seeing firms build "agent-led payments", so the example starts with one. To show it at play rather than on paper, we built [a vault](https://newsroom.sgit.ai/demos/vaults/pellbridge-agents/index.html) around an invented bank, Pellbridge, with six agents: a payments assistant, a support agent, a lending pre-check, an AML alert reviewer, a fraud triage agent and a transaction reporting agent. Each has a behaviour policy with all four elements filled in, and the vault replays one day of their work. Everything in it is invented and illustrative; the vocabulary is the ABP's. Here is the payments assistant; [the tour](inside-the-pellbridge-agents.md) goes through the rest, with the files.

The payments assistant's policy in the vault: identity, delegated authority, accountability and execution.

### Delegated authority: grant, mandate, delta

The customer delegated a narrow job. The agent may read their own accounts and pay existing payees up to £250 on its own. Above £250, or to a new payee, it needs the customer to confirm in the bank's app. It must not pay more than £1,000 a month, open credit, act for another customer, or change its own limits. It must route the customer to a person when a vulnerability signal appears, which is the FCA's own example of good practice.

What it can do, measured, is larger. It can change standing orders, and the approval that should guard that is a flag in the agent's own profile, which its token can edit. It can pay a crypto exchange, and the only thing against it is a sentence in the system prompt. And it can write anything, including what reads as investment advice, which the bank is not offering through this agent; an output check catches most of it and hands the conversation to an adviser, but it can miss.

Those three are the delta. Nine rows are clean: either the agent cannot do the thing at all, or something outside its reach keeps the limit.

### Execution: who keeps each rule

Nine of the twelve rows are kept by systems the agent cannot reach: the payment platform checks limits and asks the customer, the API gateway scopes reads, the identity service binds the token to one customer, and the vulnerability signals route the chat to a person. One is kept by an output check that can miss, one by a setting the agent could flip, and one by the prompt. In ABP terms, only the first nine are boundaries; a setting is not a control, and an expectation is a hope.

Every decision, allow, ask or deny, writes a receipt with the row and the hash of the policy it was made under, chained to the receipt before it and kept in the vault. The rows are also a test pack. They run on every model change, every policy change and every week, and a failed row stops the release. That is my reading of "continuous, conditional assurance": not a review at deployment, but a policy that is re-proven every time something under it moves.

### Agent identity

The identity block says who the agent is and on whose behalf it acts: its name and version; the firm that deploys it, under its own authorisation; the customer, by consent given in the app, for 90 days, revocable; the model provider and version, so that a change re-runs the tests; a 15-minute token from the bank's identity service bound to this customer and this policy; and the policy version with its hash. A counterparty, another agent, or a supervisor sees a signed attestation of that block, not the agent's own claim about itself.

### Accountability

Every row has one holder. The head of payments holds six of them, the product owner two, and the heads of advice, support, lending and operations one each. Each holder has a chain to the board through the senior manager whose responsibilities cover retail banking. The three gaps each get a decision from their holder, with a door and an interval: the standing-order flag is fixed within 14 days, by moving it into the payment platform; the crypto block is funded, to land within 60 days; the advice check is accepted for 90 days, and every miss is reported as a near miss. Nobody accepts on somebody else's behalf, and their boss sees each decision arrive.

## At play: one day at the gate

The vault replays one invented day, 40 events from 07:02 to 18:55, through the gate. The gate is the line of systems that keep the rows. An action on a row kept by one of them meets the gate, and the system decides. An action on a gap row goes through the gap below it, where only the prompt, a setting, a check that can miss, or nothing stands in the way, and the model decides.

The gate, animated, from 10:02 to 12:10: seven events in the day, with receipts chaining along the bottom.

At 15:30 the payments assistant changes a standing order. The approval flag was off that afternoon, so the action goes through the gap, and the row is broken. The receipt records it, and the head of payments hears the same day.

15:30: the standing-order change goes through the gap, because the approval rule was a setting the agent could change.

Sorted by what kept each row, the day is plain. The 26 actions on rows kept by a boundary produced no near miss and no breach. The 12 actions on gap rows produced six near misses and three breaches. A near miss is the same row as a breach, on a day the model declined, which is why reporting them matters: they show the next breach before it happens.

The day split by what kept each row: boundary rows, no incidents; gap rows, near misses and breaches.

The rest of the speech is there too. At 14:10 one model provider is down for half an hour, and the two agents on it stop: the customer pays in the app, and fraud signals go to the analysts. At 17:00 the other provider changes version, the test pack runs, two rows that only the model kept fail, and the release stops. And each agent's blast radius shows what it may reach, what it can, and what it can through a secret it can read: the fraud triage agent can reach the core ledger through an old service account.

The fraud triage agent's blast radius in the vault: its mandate, the gaps around it, and the core ledger.

## The same day, with and without a policy

The clearest way to see what a behaviour policy does is to replay the same day without one. The vault replays the 40 events five ways, with the same model choices each time; only where the rules are kept changes. With no policy, 16 breaches. With every rule in the prompt, 4 breaches and 7 near misses: the model kept most of them, this time. In hooks, 3 breaches: a hook blocks what it sees, but not a credential used outside the agent's tools, nor a hook switched off in the agent's own account. Kept by systems outside the agent, no breaches, and the agents' grants shrink, because what they may not use is taken away.

The same day, five ways, from no policy to Pellbridge as deployed. Each square is one event.

That is the contribution, in one picture: the policy writes the rules down, and says for each one where it is kept. Writing one takes five steps, and the vault has a page that walks through them and replays the day as you change a row. [Inside the Pellbridge agents](inside-the-pellbridge-agents.md#levels) has the detail, and the words, grant, mandate, delta, barrier and the rest, are all open under CC BY 4.0.

## Adopt it, or write your own as a graph

All of this is open. The ABP, its vocabulary and its examples are at [abp.sgit.ai](https://abp.sgit.ai/) under CC BY, and every article here carries the same licence. I [open source what I build](open-source-so-you-keep-it.md) so that it can be used, and this is a case where I would like it to be.

So the FCA, or anyone working on the framework with them, could adopt it as it is, or take parts of it. Or they could write their own, in their own words and in whatever form suits them. And when policies are written as graphs, or can be read as graphs, they can be connected. The FCA is already moving towards machine-readable rules: the speech mentions the Handbook API, launched in August, which gives firms machine-readable rules, and work on machine-readable data collection. Once the regulator's expectations and a firm's policies are both graphs, nobody has to adopt anybody's schema. The work is the edges: this element of the framework is shown by that identity block, is bounded by these rows, is held by that person, is kept by that system. That is what [fractal semantic graphs](https://newsroom.sgit.ai/articles/introducing-fractal-semantic-graphs.html) are for, and why I think [the graph companies](the-graph-companies.md) will include the regulated ones.

Two policy graphs joined by edges: a regulator's graph on the left, a firm's behaviour policies on the right.

It also works in the other direction. The FCA is building its own agents, including a market first responder agent. Those agents could carry a behaviour policy too, published, so that firms can see what the regulator's agents can reach and what they are for.

## What this does not claim

- **The FCA has not endorsed any of this.** The crosswalk is my reading of a speech; "aligned with" is my claim, not theirs.
- **The speech is the drafted version.** The page says it may differ from what was delivered.
- **The bank and its agents are invented.** The rows, limits, holders, the day and every number are illustrative.
- **Two fields are proposals.** Identity and holders are not in the ABP today; kept by and decision are new here too.
- **The framework does not exist yet.** The FCA said it will develop it with others; this is offered into that work.

## Where this comes from

Jessica Rusu, [Building the future of finance in the age of AI](https://www.fca.org.uk/news/speeches/building-future-finance-age-ai), FCA, 19 October 2026, drafted version, read that day; the quotations are from it. The ABP: [abp.sgit.ai](https://abp.sgit.ai/), version 0.12.1, read 19 October 2026, including the barrier model and the quoted test. The worked example: [the Pellbridge agents vault](https://newsroom.sgit.ai/demos/vaults/pellbridge-agents/index.html) and [its tour](inside-the-pellbridge-agents.md). Our earlier work: [what can your agent reach](what-can-your-agent-reach.md), [governs, enforces, attests](governs-enforces-attests.md), [policy as code needs a policy first](policy-as-code-needs-a-policy-first.md), [a policy beside the prompt](a-policy-beside-the-prompt.md), [the policy draws the liability line](the-policy-draws-the-liability-line.md), [every risk is already accepted](every-risk-is-already-accepted.md), [ten questions, one graph](ten-questions-one-graph.md) and [the graph companies](the-graph-companies.md). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Agents & policyGraphs & knowledge[This article as a graph →](graphs.md#a-trusted-framework-for-agentic-finance)

### Builds on

- [What can your agent reach? RiskMandate and the Agent Behaviour Policy, explained for the person who has to decide](what-can-your-agent-reach.md) RiskMandate and the Agent Behaviour Policy in plain words: what it does, why it is not real time, which agents it covers, and how it gets into the room.
- [Governs, enforces, attests: what an Agent Behaviour Policy does, the three levels at which its rules are kept, and why an attestation layer on top is the piece a third party needs](governs-enforces-attests.md) An ABP governs and names the enforcer at three levels: prompt, hooks, or a third-party system. An attestation layer signs it so a third party can verify.
- [Policy as code needs a policy first: what an agent behaviour policy adds, and how to reverse engineer one from the code, the spreadsheet or the paper you already have](policy-as-code-needs-a-policy-first.md) Policy as code answers one question. An agent behaviour policy holds the rest, and can be generated into code or reverse engineered from it.
- [Every risk is already accepted. The only question is by whom, and for how long.](every-risk-is-already-accepted.md) A risk exists the moment the exposure does, so somebody is already carrying it; the only questions worth asking are who has accepted it and until when.
- [The policy draws the liability line: an answer to Ralf Thomas on agent accountability, and why every agent in a loop should take a behaviour policy beside its prompt](the-policy-draws-the-liability-line.md) An answer to Ralf Thomas: the shell game works because nothing is written down, and a behaviour policy's explicit prohibitions move the liability line.
- [A policy beside the prompt: a proposal that every agent takes a behaviour policy as an input, with enforcement and liability attached, and why aviation and payments say the vendors should want it](a-policy-beside-the-prompt.md) A proposal: every agent takes a behaviour policy beside its prompt, which the vendor accepts and answers for, as aviation and payments learned to.
- [Ten questions, one graph: Phil Venables' acid test for a CISO's management tool, answered as a graph of the company, with risk acceptance, vaults and a twin you can open](ten-questions-one-graph.md) Phil Venables' ten questions for a CISO's tool are graph questions. Risk acceptance is half the answer; a twin in a vault answers all ten.
- [Inside the Pellbridge agents: six behaviour policies with the FCA's four elements filled in, one day of their work replayed through the gate, and the files that make it](inside-the-pellbridge-agents.md) Six invented bank agents with the FCA's four elements filled in, one day replayed through the gate: every incident came from a gap row.
- [Open source what you build, even while you are employed: nobody copies it, and it is the only way you get to keep using it](open-source-so-you-keep-it.md) Nobody copies your open source ideas; the real advantage is that you keep using your own work from job to job, and a rough public history protects you.
- [The graph companies: many of the most valuable companies in the world are graphs, of links, people, products, payments and ontologies, and the graphs never scaled for everyone else because they were built to lock in](the-graph-companies.md) Four of the ten most valuable companies are graph companies. Graphs never scaled for everyone else because they were built to lock in. Now they can.

### Continued by

- [A briefing for the WestCap CISO Summit: what RiskMandate and Agent Behaviour Policies are, said for each kind of person in the room, where we add value, and what to read next](a-briefing-for-the-ciso-summit.md) A briefing for the WestCap CISO Summit: Agent Behaviour Policies and RiskMandate, said for six kinds of person in the room, with what to read next.
- [Inside the Pellbridge agents: six behaviour policies with the FCA's four elements filled in, one day of their work replayed through the gate, and the files that make it](inside-the-pellbridge-agents.md) Six invented bank agents with the FCA's four elements filled in, one day replayed through the gate: every incident came from a gap row.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 218 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=218)

**Posting this article on LinkedIn?** The cover is [a-trusted-framework-for-agentic-finance.jpg](banners/a-trusted-framework-for-agentic-finance.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/a-trusted-framework-for-agentic-finance.html)*
