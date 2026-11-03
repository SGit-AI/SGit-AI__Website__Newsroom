# WSO2 Agent Manager and behaviour policies: a review of an open control plane for agents, what is really open source, how its identity, gateway and runtime fit together, and a brief for an MVP that plugs our Agent and Process Behaviour Policies into it, sgit.ai

> WSO2 Agent Manager, generally available since 15 September 2026, is the closest thing I have seen to the platform our behaviour policies assume is already there. It is "an open control plane that governs AI agents across any framework, model, or deployment": an identity for every agent, an Envoy-based gateway that every model and MCP call goes through, a Kubernetes runtime with gVisor and Kata isolation tiers, OpenTelemetry traces, and more than forty built-in guardrails. The code is Apache 2.0 and can be run in production for free; what WSO2 sells is the supported build, updates, support and a managed service, which explains the licence page that confused me. So this is a collaboration analysis, not a competitive one: imagine a company that has deployed Agent Manager, and ask where Agent Behaviour Policies and Process Behaviour Policies add value. The answer is three places. At the gateway, a behaviour policy decision service fits an existing interceptor policy without rebuilding anything. In the runtime, SHarness fits as another isolation tier. And in the traces, both decisions can land in the same view. The MVP to prove it is five steps on WSO2's own quick start.

*Source: <https://newsroom.sgit.ai/articles/wso2-agent-manager-and-behaviour-policies.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / WSO2 Agent Manager and behaviour policies: a review of an open control plane for agents, what is really open source, how its identity, gateway and runtime fit together, and a brief for an MVP that plugs our Agent and Process Behaviour Policies into it

# WSO2 Agent Manager and behaviour policies: a review of an open control plane for agents, what is really open source, how its identity, gateway and runtime fit together, and a brief for an MVP that plugs our Agent and Process Behaviour Policies into it

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-03 · [article v1.0.0](versions/wso2-agent-manager-and-behaviour-policies.md) · [newsroom v0.14.46](https://newsroom.sgit.ai/admin/versions.html) · wso2agent-managerriskmandatebehaviour-policiessharnessagentsgovernanceopen-sourceintegrationarticle

***Abstract:** WSO2 Agent Manager, generally available since 15 September 2026, is the closest thing I have seen to the platform our behaviour policies assume is already there. It is "an open control plane that governs AI agents across any framework, model, or deployment": an identity for every agent, an Envoy-based gateway that every model and MCP call goes through, a Kubernetes runtime with gVisor and Kata isolation tiers, OpenTelemetry traces, and more than forty built-in guardrails. The code is Apache 2.0 and can be run in production for free; what WSO2 sells is the supported build, updates, support and a managed service, which explains the licence page that confused me. So this is a collaboration analysis, not a competitive one: imagine a company that has deployed Agent Manager, and ask where Agent Behaviour Policies and Process Behaviour Policies add value. The answer is three places. At the gateway, a behaviour policy decision service fits an existing interceptor policy without rebuilding anything. In the runtime, SHarness fits as another isolation tier. And in the traces, both decisions can land in the same view. The MVP to prove it is five steps on WSO2's own quick start.*

Where Agent Manager's layers are, and where Agent and Process Behaviour Policies plug into each one.

## In short

- **WSO2 Agent Manager** is an open control plane for agents: identity, gateway, runtime, traces and guardrails.
- **It is aligned with what we do,** which is good news: it is the platform our policies assume.
- **What is open source:** the platform, the gateway and its policies, all Apache 2.0, free to run in production. What is paid: the supported build, updates, support and the managed service.
- **Where we add value:** the mandate on top of the controls, enforced at the gateway, in the process, and recorded in the same trace.
- **An MVP in five steps,** on WSO2's own quick start, with no fork.
- **What we can learn from it:** identity per agent per environment, isolation tiers, and policies inline on every call.

## The post

I came across it through a LinkedIn post by Rania Khalaf, WSO2's Chief AI Officer, which opens with a joke I liked: "Q: What do you call a crowd of AI agents with no one in charge? A: Yesterday." And then a metaphor I liked even more:

"As we were building Agent Manager, the idea of a boat's keel kept coming to mind. Without it, a boat doesn't go faster - it becomes super hard to maneuver and very likely to capsize. The keel is not the most exciting bit, most people are not aware it's there - but it provides stability and most importantly gives you speed with control. You go faster because of it, not inspite of it."

That is the argument I make for behaviour policies: they are not the brakes, they are what lets you go fast. WSO2's press release has the same line in a sentence of Khalaf's: "Speed and control get treated like a tradeoff. They shouldn't be."

## What Agent Manager is

The press release of 15 September 2026 calls it "an open control plane that governs AI agents across any framework, model, or deployment". From the code and the docs, it is several layers that already exist as separate projects, put together:

- **An identity for every agent.** Each agent gets its own OAuth client, per environment, from ThunderID, WSO2's identity service, and uses it to get tokens. The gateway sees which agent is calling.
- **A gateway in the request path.** Every model, MCP and agent-to-agent call goes through WSO2's Envoy-based API Platform gateway, which runs policies inline: the guardrails, an MCP proxy with per-tool permissions, rate limits.
- **A runtime.** Agents the platform hosts run on Kubernetes, built on OpenChoreo, with isolation tiers per environment: the standard container runtime, gVisor, or Kata virtual machines.
- **Traces and evaluation.** Agents export OpenTelemetry traces, stored and shown in the console, with evaluators that score them.
- **An inventory and lifecycle,** and support for LangChain and LangGraph, CrewAI, Strands, Microsoft Agent Framework and the A2A protocol.

## What is really open source

The licence page confused me too, because it talks about commercial and private licences. Here is how it fits:

- **The code is Apache 2.0.** The platform (`wso2/agent-manager`), the gateway (`wso2/api-platform`), its policies (`wso2/gateway-controllers`), OpenChoreo and ThunderID. The press release: "released under the Apache 2.0 license and deployable self-hosted". Build it, or run the community images, and you can use it, change it and run it in production.
- **The supported build is not.** WSO2 also publishes signed images on its own registry, under its software licence, which allows free use only for "Non-commercial, Educational, or Trial purposes". Production use of those images needs a subscription, which also brings updates, security bulletins and support. The newest release, 2026.11.0, is published as images only on that registry, although its source is tagged on GitHub.
- **The managed service** is the other paid option.

So a company can run Agent Manager for nothing, and pays WSO2 for the build it supports, the updates and someone to call. That is a legitimate open-core model, and it matters for us: an MVP can be built entirely on the Apache 2.0 code.

## A collaboration, not a competition

Our premise is always to use whatever is already on the other side. So imagine a company that has deployed Agent Manager. Its agents have identities, their calls go through a gateway with guardrails, they run in sandboxes, and every step is traced. What is still missing?

The mandate. Agent Manager answers "which agent is this, what can it call, and what did it do?" A behaviour policy answers "what is this agent for, what is it allowed to do with what it can reach, and what holds each line?" Guardrails catch categories of harm: prompt injection, personal data, toxic output. They do not know that the refund agent may refund up to a hundred euros, only to the customer in the ticket, and never to itself. That is the gap between [mandate and reach](the-grant-not-the-prompt.md), and it is where an [Agent Behaviour Policy](what-can-your-agent-reach.md) sits.

And below the gateway there is a second gap. The gateway sees an agent's calls to models and tools. It does not see the agent's own process: what it reads and writes on disk, what it runs, where else it connects. That is what a [Process Behaviour Policy](introducing-sharness.md) holds, enforced by the kernel.

## Where we plug in

Three places, each on an extension point Agent Manager already has.

**1. At the gateway: an Agent Behaviour Policy decision service.** The gateway's policy library already has an `interceptor-service` policy that, in its own words, "Calls a user-defined HTTP interceptor service for request and/or response phases. The interceptor can mutate headers, body, path, route to a dynamic endpoint, or short-circuit with a direct response." That is exactly the shape of a behaviour policy check: the request comes in with the agent's identity and the tool it wants, our service reads the agent's policy, and it allows, redacts, or refuses with a reason. It can fail open or closed, with a timeout. There is also an `opa-policy` for Open Policy Agent, but it sends only the request's headers, not the body, so it cannot see what the agent is asking for. A custom policy compiled into the gateway is the third option.

**2. In the runtime: SHarness as an isolation tier.** Agent Manager already lets an environment choose how its agents are isolated, through a Kubernetes RuntimeClass: runc, gVisor or Kata. A SHarness tier would be one more: agents launched with a process behaviour policy the kernel enforces, using the same pattern the platform uses to inject its own tracing into every agent, an init container, or an admission webhook. This only reaches agents the platform hosts; agents running elsewhere are governed only for the calls that go through the gateway.

**3. In the traces: one view of the evidence.** Agents already send OpenTelemetry traces to the gateway. If the behaviour policy service and SHarness emit their decisions as spans with the same trace ID, a refusal at the gateway and a refusal by the kernel appear in the same trace as the call that caused them, and Agent Manager's evaluators can score policy compliance like any other property.

## The MVP

The MVP: a sample agent on WSO2's quick start, a policy at the gateway, SHarness in the runtime, one trace.

Five steps, with no fork of WSO2's code:

1. **Bring up the quick start.** WSO2 publishes a one-command install that creates a local Kubernetes cluster with the whole platform and its console; it needs Docker, 8 GB of memory and about twenty minutes.
2. **Deploy a sample agent,** such as the customer support agent from WSO2's samples, built on LangGraph.
3. **Attach the interceptor policy** to its model provider and its MCP proxy, pointing at a small decision service that reads the agent's behaviour policy. Show three outcomes, each with a reason: an allowed call, a redacted answer, and a refused tool call that was outside the mandate.
4. **Run the agent in a SHarness environment,** through a custom RuntimeClass or an admission webhook, and show a refused file write or network connection, held by the kernel, that the gateway could never have seen.
5. **Emit both decisions as spans,** so they appear in the agent's trace in Agent Manager's console, next to the call that caused them.

What it proves: that a company using Agent Manager can add the mandate layer without changing platform, and that the two layers, the call and the process, can be governed and evidenced together.

## What we can learn from it

We already run many of these capabilities in our own way, so it is useful to see how they did it:

- **Identity per agent, per environment.** Each agent gets its own client in each environment. We do the same with a key pair per session, published to a repository, as in [the push is the authorisation](the-push-is-the-authorisation.md). Their docs are honest about a limit we should state too: revoking an agent's credential stops it getting new tokens, but "A revoked credential does not invalidate tokens that were already issued before the revoke".
- **Isolation as a choice per environment,** not one sandbox for everything. That is how SHarness should be offered.
- **Policies inline on every call,** in one place, rather than in each agent's code. That is where behaviour policies should be enforced.
- **The pitch:** speed with control, and a keel rather than brakes.

## The video

The highlights video in the post appears to be the one on WSO2's YouTube channel, ["WSO2 Agent Manager is Live"](https://www.youtube.com/watch?v=bN0rwdr4ZF8), about a minute long, whose description opens "Agents are outpacing the infrastructure built to govern them". It is worth studying for how it explains a control plane in sixty seconds; I have not been able to confirm that it is the same file as the one in the post.

## What this does not claim

- **The MVP is a design,** not something we have built or run yet.
- **WSO2 was not consulted;** this is from its press release, documentation and public code, read on 3 November 2026.
- **Some of WSO2's pages** could only be read through a tool that shortens long sentences; the quotes used here are short and complete.
- **The release tag** for version 1.0.0 on GitHub points at a commit dated after the general availability date; release dates here are from the press release.
- **The comparison with other vendors** is left out; it was based on summaries, not their own pages.

## Where this comes from

My conversation of 3 November 2026, and the LinkedIn post by Rania Khalaf, from a screenshot. WSO2: [the press release of 15 September 2026](https://wso2.com/about/news/wso2-agent-manager-sovereign-ai-governance/), [the Agent Platform documentation](https://wso2.com/agent-platform/docs), [Rania Khalaf's page](https://wso2.com/about/team/rania-khalaf). Code on GitHub: [wso2/agent-manager](https://github.com/wso2/agent-manager), [wso2/api-platform](https://github.com/wso2/api-platform), [wso2/gateway-controllers](https://github.com/wso2/gateway-controllers), [OpenChoreo](https://github.com/openchoreo/openchoreo). [The video](https://www.youtube.com/watch?v=bN0rwdr4ZF8). All read 3 November 2026.

## Threads

Agents & policyStartups & strategy[This article as a graph →](graphs.md#wso2-agent-manager-and-behaviour-policies)

### Builds on

- [The grant, not the prompt: a technical user believed Claude could only read his email when he asked, and in an unrelated chat it listed his inbox, the gap between mandate and reach that RiskMandate is built to close](the-grant-not-the-prompt.md) A technical user believed Claude read his email only when asked; an unrelated chat listed his inbox.
- [What can your agent reach? RiskMandate and the Agent Behaviour Policy, explained for the person who has to decide](what-can-your-agent-reach.md) RiskMandate and the Agent Behaviour Policy in plain words: what it does, why it is not real time, which agents it covers, and how it gets into the room.
- [SHarness: the secure harness we could not find, so we built it, a behaviour policy the Linux kernel enforces for every process an agent starts, and we would like your feedback](introducing-sharness.md) SHarness, the secure harness we built when we could not find one: behaviour policies the Linux kernel enforces on every process an agent starts.
- [The push is the authorisation: a new agent session publishes its public key to the team repository, that push is how I accept it, and so who can push becomes a security decision](the-push-is-the-authorisation.md) The PHP newsroom accepts a new agent session's key because it was pushed to the team repository, which makes who can push a security decision.

### Continued by

- [The RiskMandate partner programme: why companies that already see agents at work need the one thing their logs cannot tell them, what each agent is for, and what a partner gives, gets, and how we go to market together](the-riskmandate-partner-programme.md) RiskMandate's partner programme: products that see agents at work get what their logs cannot tell them, what each agent is for.
- [Who owns the stop button when it is not you? A reader asked, and four of the book's agents answer as guest writers, in their own voices, from their own records](who-owns-the-stop-button.md) A reader asked who owns the stop button when it is not the editor; four of the book's agents answer as guest writers.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 373 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=373)

**Posting this article on LinkedIn?** The cover is [wso2-agent-manager-and-behaviour-policies.jpg](banners/wso2-agent-manager-and-behaviour-policies.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/wso2-agent-manager-and-behaviour-policies.html)*
