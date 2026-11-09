---
title: RiskMandate and Cloudflare: where agents run, where they are controlled, and why Cloudflare's own Agent Access Model leaves room for a signed record of what each agent was asked to do
date: 2026-11-09
author: Dinis Cruz
author_url: about/index.html
summary: Cloudflare is two things for agents. It is a place to build and run them (the Agents SDK, sandboxes, a headless browser, models, an AI Gateway, remote MCP servers), and a place to control them (Access in front of MCP servers, a new risk tier per tool called WriteGuard, data loss prevention on prompts, signed identities for agents on the web). This maps both onto RiskMandate's Agent Behaviour Policies, from Cloudflare's documentation and blog, read on 9 November 2026. Cloudflare already has controls at every layer, from what an agent reads to logs a third party can check, and its defaults are open: an MCP portal enables every tool, including new ones. Its own writing makes the case for the missing piece. In August it published an Agent Access Model, "Its default is deny", and said it is "not comfortable saying that multiplayer access control can be built end to end today". In November it wrote that a narrow scope "only says what the Agent was allowed to do. It doesn't say who answers when the Agent gets it wrong". That is the record an Agent Behaviour Policy is: what this agent was asked to do, the gap from what it can reach, the control holding each row, and who signed it off.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: riskmandate, abp, cloudflare, agents, mcp, zero-trust, ai-gateway, controls, article
status: published
---

!shot cfm-controls.webp | images/ | Eight of Cloudflare's controls for agents, what each holds, and what stays open. | comparison

## In short {#in-short}

- **Cloudflare is where agents run and where they are controlled,** often in the same account.
- **It has controls at every layer:** MCP portals and Access policies, approvals in the Agents SDK, WriteGuard's risk tiers, spend and rate caps, sandbox bindings, data loss prevention, signed agent identities.
- **The defaults are open,** and several of the strongest controls are in beta.
- **Cloudflare's own writing names the gap:** a scope says what an agent may do, not what it was asked to do, or who answers when it gets it wrong.
- **An Agent Behaviour Policy is that record,** and Cloudflare's logs are what it can be checked against.
- **Nothing here has been run on Cloudflare by us.** This is a mapping from its documentation and blog, read on 9 November 2026.

## Two roles in one account {#two-roles}

I wrote a month ago about [Cloudflare as Lego blocks](/articles/cloudflare-as-lego-blocks.html), the pieces a non-specialist can build with. For agents, those pieces split in two.

**Where agents run.** The [Agents SDK](https://developers.cloudflare.com/agents/) gives each agent "a durable identity, local SQL storage, real-time connections, scheduled work, and recoverable execution", each one a Durable Object. Around it: [Workflows](https://developers.cloudflare.com/workflows/) that persist "for minutes, hours, or even weeks"; a [Sandbox](https://developers.cloudflare.com/sandbox/) where "Your Worker decides which application APIs and data the code receives, and whether the code can reach the public Internet"; [Browser Run](https://developers.cloudflare.com/browser-run/), formerly Browser Rendering; Workers AI; [AI Gateway](https://developers.cloudflare.com/ai-gateway/), where "Each log can include the prompt, response, provider, timestamp, status, token usage, cost, duration, and user agent"; and remote MCP servers with Cloudflare's own OAuth provider.

**Where agents are controlled.** Cloudflare One puts [Access in front of MCP servers](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/), to "vet, authorize, and audit every interaction between users and MCP servers"; an AI security report shows which AI apps people use, each "Unreviewed", "In Review", "Unapproved" or "Approved"; Gateway and DLP inspect prompts; [AI Security for Apps](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/), formerly Firewall for AI, detects "prompt injection attacks, PII exposure in prompts, and prompts about unsafe topics"; and [Web Bot Auth](https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/) gives agents a signed identity when they visit other people's sites.

A business can build an agent on the first half and govern it with the second, which is rare.

## The controls, and what they leave open {#controls}

Each control below is a barrier an Agent Behaviour Policy can record; each "but" is a gap it should list.

- **MCP server portals** let admins choose "the specific tools and prompt templates" for each use, and Access logs "the individual requests made using the tools in the portal". But "all of its tools and prompts are available to portal users by default", and after a sync "new tools and prompts are automatically enabled". Reach grows unless someone curates it.
- **Workers OAuth scopes:** the user consents to scopes. But Cloudflare's own example code says of them: "Advertised, not enforced: check them in the handler." Enforcement is code in each server.
- **Approvals in the Agents SDK:** "Human-in-the-loop (HITL) patterns add approval or input at different layers of an Agent", with `waitForApproval()` and Code Mode's `requiresApproval`. But the developer decides which actions wait, and Code Mode is labelled experimental.
- **AI Gateway spend and rate limits** block requests over a cap "with a `429` response". But they cap how much, not what.
- **Sandbox bindings and egress** decide which APIs, data and internet the code gets: the strongest technical barrier on reach. But nothing records why each binding was granted.
- **DLP and AI Security for Apps** inspect what goes into and out of models. But they see only traffic routed through them, such as endpoints labelled `cf-llm`.
- **Web Bot Auth and verified bots** prove which agent is knocking. But identity is who it is, not what it may do.

## Joe's agent {#joe}

!shot cfm-joe.webp | images/ | Cloudflare's WriteGuard example: the agent acts with Joe's permissions, so its reach is Joe's reach. | concept

Cloudflare's [WriteGuard post](https://blog.cloudflare.com/mcp-portal-writeguard-private-beta/) of 5 August opens with a story I would put in front of any board. Bug tickets start closing at noon, moved to Done by Joe. "By 4 p.m., thousands of tickets have been closed, all by Joe." Joe is a good engineer, and not a thousand-tickets-an-hour engineer: it was his agent.

WriteGuard, in private beta, is Cloudflare's answer: "Every tool gets a risk tier, an enabled or disabled state, and a labeling configuration", and it "adds MCP client and session context to the human identity", so the audit event "includes the server, tool, risk tier, outcome, user, client, and duration". By design it does not give agents their own accounts: Joe's agent works with Joe's permissions.

That is a sensible engineering choice, and it is exactly why the policy matters. If the agent's reach is its human's reach, the only place its narrower job is written down is the policy: triage today's tickets, close none without a person. The gap between the two is what closed thousands of tickets.

## Cloudflare's own case for a mandate {#case}

Two Cloudflare posts say this more directly than I could.

The [Agent Access Model](https://blog.cloudflare.com/the-agent-access-model/), 5 August, is a framework rather than a product. Its aim is to "make the agent's capability smaller, so there is less to judge in the first place". "A task's scope is declared when the agent is dispatched". "Its default is deny". And, candidly: "We are not comfortable saying that multiplayer access control can be built end to end today."

[Trusted agent delegation](https://blog.cloudflare.com/trusted-agent-delegation/), 5 November, goes further. Agents "ask for, and get, permission to do everything". "A scope of "everything" tells the Site nothing. And even a narrow scope only says what the Agent was allowed to do. It doesn't say who answers when the Agent gets it wrong". And on asking a person to click approve: it "proves some human is present at that moment", "and nothing more".

A declared task scope, a default of deny, and someone who answers: those are the mandate, the barriers and the sign-off of an Agent Behaviour Policy. Cloudflare has built most of the enforcement points. The policy is the document that says, for each agent, which of them to switch on and why, and who signed it.

## Read, set, gate, attest {#layers}

!shot cfm-layers.webp | images/ | On Cloudflare, every layer has pieces already; the missing one is the record they are checked against. | architecture

Using the four layers from [the Manus mapping](/articles/riskmandate-and-manus.html):

1. **Read:** the policy in the agent's instructions, in an Agents SDK agent or a portal's prompt templates. Exists; soft.
2. **Set:** portal tool lists, Access policies per tool, Gateway caps, sandbox bindings and egress. Exists; the defaults are open, so the policy says what to close.
3. **Gate:** `waitForApproval`, `requiresApproval` and WriteGuard's tiers on write tools. Exists in the SDK; WriteGuard is in private beta.
4. **Attest:** Access request logs, AI Gateway logs and WriteGuard's audit events. The evidence exists; what is missing is a signed mandate to check it against.

Unlike Manus, where the gate and the evidence were proposals, on Cloudflare they are mostly there. That makes the policy more useful, not less: it is the part that turns logs into a yes or a no.

## What RiskMandate could offer Cloudflare users {#offer}

- **A policy per agent built on Cloudflare,** with reach read from what is actually configured: portal tools, Access policies, bindings, Gateway limits.
- **Templates for the common shapes:** an Agents SDK agent with a sandbox; a team's MCP portal; a coding agent signed in through `cloudflared`, which "authenticates under your user identity".
- **A check of open defaults:** every portal tool enabled, new tools auto-enabled, scopes not enforced in a handler.
- **A gate from the policy:** the rows marked "needs a person" become the actions that call `waitForApproval`, or the tools WriteGuard marks as high risk. Proposed, not built.

## What this does not claim {#limits}

- **We have not run any of this on Cloudflare.** It is a mapping from documentation and blog posts read on 9 November 2026.
- **Status is as each page states it;** several pages give none, and WriteGuard and identity-aware AI Gateway are in beta.
- **Joe is Cloudflare's example;** the "triage, close none without a person" mandate is ours, to show the shape.
- **RiskMandate has no relationship with Cloudflare,** beyond being a customer for its domains.

## Where this comes from {#sources}

Cloudflare's documentation, read 9 November 2026: [Agents](https://developers.cloudflare.com/agents/), [human-in-the-loop](https://developers.cloudflare.com/agents/concepts/agentic-patterns/human-in-the-loop/), [MCP authorization](https://developers.cloudflare.com/agents/model-context-protocol/protocol/authorization/), [MCP governance](https://developers.cloudflare.com/agents/model-context-protocol/protocol/governance/), [MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/), [authenticating agents to Access](https://developers.cloudflare.com/cloudflare-one/access-controls/authenticate-agents/), [Workflows](https://developers.cloudflare.com/workflows/), [Sandbox](https://developers.cloudflare.com/sandbox/), [Browser Run](https://developers.cloudflare.com/browser-run/), [AI Gateway](https://developers.cloudflare.com/ai-gateway/), [AI Security for Apps](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/), [Web Bot Auth](https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/). Cloudflare's blog: [WriteGuard](https://blog.cloudflare.com/mcp-portal-writeguard-private-beta/) and [the Agent Access Model](https://blog.cloudflare.com/the-agent-access-model/) (5 August 2026), [trusted agent delegation](https://blog.cloudflare.com/trusted-agent-delegation/) (5 November 2026). [RiskMandate](https://riskmandate.ai/). Earlier on this site: [Cloudflare as Lego blocks](/articles/cloudflare-as-lego-blocks.html), [RiskMandate and Manus](/articles/riskmandate-and-manus.html), [governs, enforces, attests](/articles/governs-enforces-attests.html), [are hooks the sweet spot?](/articles/are-hooks-the-sweet-spot.html).
