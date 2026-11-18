# RiskMandate and Kosmoy: two answers to "who controls the agents?", Kosmoy's self-hosted control plane for regulated enterprises, with an AI gateway, guardrails, a model router, observability and a Kubernetes sandbox for every agent run, and RiskMandate's open behaviour policies, written per agent, checked by hooks and bounded by SHarness, where they overlap, where they differ, and why they fit together, sgit.ai

> I was asked how RiskMandate compares with Kosmoy, so I read Kosmoy's site properly. Kosmoy, from Milan, sells what it calls the AI management platform for regulated enterprises: an inventory of every AI use case, model, agent and MCP server; an AI gateway that is "one policy point for every AI call", with guardrails, role-based access, routing between small and frontier models, cost tracking and logging; and the Action Capsule, a Kubernetes sandbox for each agent run, with admission before it starts, run-scoped credentials, an egress allow-list and a kill switch. It runs single-tenant in the customer's own cluster, is priced by proposal, and names Banca d'Italia and Leonardo as customers. RiskMandate starts from the other end: a written behaviour policy for each agent, what it can reach, what it was authorised to do, the gap between them, and what stands in the way, published as an open standard, checked on every call by hooks, and, at the strongest, bounded by SHarness at the kernel; sold from £500 for one agent to £20,000 for an estate, with every price on the page and every claim linked to our own agents' records. Kosmoy is the enforcement plant; RiskMandate is the policy and the evidence. The obvious fit: an Agent Behaviour Policy is exactly what Kosmoy's gateway and capsules could enforce.

*Source: <https://newsroom.sgit.ai/articles/riskmandate-and-kosmoy.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / RiskMandate and Kosmoy: two answers to "who controls the agents?", Kosmoy's self-hosted control plane for regulated enterprises, with an AI gateway, guardrails, a model router, observability and a Kubernetes sandbox for every agent run, and RiskMandate's open behaviour policies, written per agent, checked by hooks and bounded by SHarness, where they overlap, where they differ, and why they fit together

# RiskMandate and Kosmoy: two answers to "who controls the agents?", Kosmoy's self-hosted control plane for regulated enterprises, with an AI gateway, guardrails, a model router, observability and a Kubernetes sandbox for every agent run, and RiskMandate's open behaviour policies, written per agent, checked by hooks and bounded by SHarness, where they overlap, where they differ, and why they fit together

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-18 · [article v1.0.0](versions/riskmandate-and-kosmoy.md) · [newsroom v999.0.0](https://newsroom.sgit.ai/admin/versions.html) · riskmandatekosmoyagent-governancebehaviour-policiesai-gatewaycomparisonarticle

***Abstract:** I was asked how RiskMandate compares with Kosmoy, so I read Kosmoy's site properly. Kosmoy, from Milan, sells what it calls the AI management platform for regulated enterprises: an inventory of every AI use case, model, agent and MCP server; an AI gateway that is "one policy point for every AI call", with guardrails, role-based access, routing between small and frontier models, cost tracking and logging; and the Action Capsule, a Kubernetes sandbox for each agent run, with admission before it starts, run-scoped credentials, an egress allow-list and a kill switch. It runs single-tenant in the customer's own cluster, is priced by proposal, and names Banca d'Italia and Leonardo as customers. RiskMandate starts from the other end: a written behaviour policy for each agent, what it can reach, what it was authorised to do, the gap between them, and what stands in the way, published as an open standard, checked on every call by hooks, and, at the strongest, bounded by SHarness at the kernel; sold from £500 for one agent to £20,000 for an estate, with every price on the page and every claim linked to our own agents' records. Kosmoy is the enforcement plant; RiskMandate is the policy and the evidence. The obvious fit: an Agent Behaviour Policy is exactly what Kosmoy's gateway and capsules could enforce.*

RiskMandate and Kosmoy, side by side: what each is, where it enforces, how it is sold, and what is open.

## In short

- **Kosmoy is a control plane:** inventory, an AI gateway, guardrails, routing, observability, a sandbox per agent run.
- **RiskMandate is a policy:** written per agent, open, checked by hooks, bounded by SHarness.
- **Kosmoy enforces at the gateway and the pod;** RiskMandate says what should be enforced, and shows the evidence.
- **Kosmoy is for regulated enterprises,** self-hosted, priced by proposal.
- **RiskMandate starts at £500 for one agent,** prices and evidence public.
- **They fit together:** a behaviour policy is what a gateway and a sandbox could enforce.

## What Kosmoy is

[Kosmoy](https://www.kosmoy.com/) calls itself "the AI management platform": "AI Gateway, LLM Gateway & AI Governance Platform for the Enterprise", "built for regulated enterprises". From its own pages, it has four layers:

- **An inventory** of AI use cases, models, agents and MCP servers, each with a risk tier and an owner.
- **Monitoring and observability:** cost, usage, feedback, evaluations and red teaming.
- **Governance through an AI gateway,** "one policy point for every AI call", across model, MCP and agent-to-agent traffic, with an OpenAI-compatible API, guardrails for toxic language, personal data, prompt injection and policy compliance, role-based access, cost tracking, logging, and a router that sends "simple prompts to small models, hard ones to frontier models".
- **Action control:** the [Action Capsule](https://kosmoy.com/platform/action-capsule/), a container that runs one model, agent task or MCP server in a standard Kubernetes pod, with default-deny networking, an in-pod proxy that allows only listed hosts, paths and methods, Linux sandboxing (namespaces, cgroups, seccomp, Landlock), "every run is admitted before it executes", credentials issued for the run and revoked after it, and a kill switch that "stops the process itself". A mission control supervises the fleet.

It runs single-tenant in the customer's own Kubernetes, on Azure, AWS, Google Cloud, on premises or air-gapped, with "no mandatory vendor-hosted control plane". It publishes no list price: each proposal is scoped by the layers, the workloads, the deployment boundary and the support. Its site names Banca d'Italia and Leonardo as customers, and its head office is in Milan. I found no statement that its own software is open source; its terms are a self-hosted subscription agreement.

## What RiskMandate is

[RiskMandate](https://riskmandate.ai/) starts from a document, not a platform: an Agent Behaviour Policy for each agent. It says what the agent can actually reach, the grant; what it was authorised to do, the mandate; the gap between them; and the barrier that stands in the way ([what can your agent reach?](what-can-your-agent-reach.md)). The standard is open, and the strength is chosen in order:

- **A behaviour policy,** written down and given to the agent: "not the strongest control, but a lot of value for the money, today".
- **Hooks,** the rule checked on every call outside the model's say-so: in our test, a rule as a line in the prompt held 3 of 12 attacks; with a hook, 12 of 12.
- **A boundary,** SHarness, the rule enforced by something the agent cannot reach, the Linux kernel ([introducing SHarness](introducing-sharness.md)).

It is sold on a ladder with the prices on the page: £500 for a policy for one agent, £1,500 worked through with you, £5,000 for your agents mapped and controlled, £20,000 for an engagement. And its evidence is our own: 191 behaviour policies written for our agents, 2,262 agent runs each reported against its policy, 2,980 actions logged as outside a grant, and the one rule that failed and became a barrier ([stopping a hundred agents](stopping-a-hundred-agents.md)).

## Where they overlap

Both answer the same question, who controls the agents, and both agree on the answer's shape: know what each agent can reach, decide what it may do, put something in the way, record everything, and be able to stop it. Kosmoy's capsule and SHarness are close cousins: both use what the Linux kernel already offers to bound a process the agent cannot argue with. Kosmoy's "no model lock-in" and RiskMandate's "no lock-in" are the same promise from different directions.

## Where they differ

Where each one works: the policy and its evidence, the hook, the gateway, the sandbox, the kernel.

- **The starting point.** Kosmoy starts from infrastructure: put every call through a gateway and every run in a capsule. RiskMandate starts from the agent: write down what this one should do, then enforce it as strongly as it needs.
- **Who it is for, first.** Kosmoy is for a regulated enterprise with a platform team and Kubernetes. RiskMandate is for anyone running an agent, from one to hundreds, and for the people who answer for them.
- **How it is sold.** Kosmoy: a scoped proposal and a proof of concept. RiskMandate: fixed prices, from £500, and sixteen policy templates free.
- **What is open.** RiskMandate's standard, policies and code are open source. Kosmoy's own components, as far as its site says, are not.
- **The evidence.** RiskMandate's claims link to our own agents' records, run by run. Kosmoy's site describes its controls and names its customers; I have not used it, so this comparison is from its own pages.

## Why they fit together

Kosmoy's gateway is "one policy point for every AI call"; its capsule admits a run only after a pre-flight check. Neither says what the policy should be for a given agent: that is the customer's to write. An Agent Behaviour Policy is exactly that document, per agent, in a public grammar, with its gap and its barrier named. A company could write its policies with RiskMandate and enforce them with Kosmoy's gateway and capsules; the policy says, the plant enforces, and the run reports show whether it held. That is the fit I would explore first, before any comparison of features.

## What this does not claim

- **Kosmoy is described from its own website,** read on 18 November 2026; I have not used it, and I have not spoken to the company.
- **RiskMandate is ours,** so read this as a founder's comparison.
- **Neither is a certification;** Kosmoy names the EU AI Act's audit areas, and does not claim a certificate.

## Where this comes from

[kosmoy.com](https://www.kosmoy.com/), its [Action Capsule](https://kosmoy.com/platform/action-capsule/) and [pricing](https://kosmoy.com/pricing/) pages, read on 18 November 2026; [riskmandate.ai](https://riskmandate.ai/) (v1.41.23), read the same day. Earlier on this site: [what can your agent reach?](what-can-your-agent-reach.md), [introducing SHarness](introducing-sharness.md), [stopping a hundred agents](stopping-a-hundred-agents.md).

## Threads

Agents & policy[This article as a graph →](graphs.md#riskmandate-and-kosmoy)

### Builds on

- [What can your agent reach? RiskMandate and the Agent Behaviour Policy, explained for the person who has to decide](what-can-your-agent-reach.md) RiskMandate and the Agent Behaviour Policy in plain words: what it does, why it is not real time, which agents it covers, and how it gets into the room.
- [SHarness: the secure harness we could not find, so we built it, a behaviour policy the Linux kernel enforces for every process an agent starts, and we would like your feedback](introducing-sharness.md) SHarness, the secure harness we built when we could not find one: behaviour policies the Linux kernel enforces on every process an agent starts.
- [Stopping a hundred agents: the Big Stop, the hand brake and the final hold at Web Summit, why pausing took seconds but hearing the order took up to an hour, what kept running anyway, and why a stop has to be a file every agent reads first](stopping-a-hundred-agents.md) Stopping a hundred agents at Web Summit: pausing took seconds, hearing the order took up to an hour, and a stop has to be a file every agent reads first.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 472 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=472)

**Posting this article on LinkedIn?** The cover is [riskmandate-and-kosmoy.jpg](banners/riskmandate-and-kosmoy.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/riskmandate-and-kosmoy.html)*
