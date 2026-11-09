# RiskMandate and Cloudflare: where agents run, where they are controlled, and why Cloudflare's own Agent Access Model leaves room for a signed record of what each agent was asked to do, sgit.ai

> Cloudflare is two things for agents. It is a place to build and run them (the Agents SDK, sandboxes, a headless browser, models, an AI Gateway, remote MCP servers), and a place to control them (Access in front of MCP servers, a new risk tier per tool called WriteGuard, data loss prevention on prompts, signed identities for agents on the web). This maps both onto RiskMandate's Agent Behaviour Policies, from Cloudflare's documentation and blog, read on 9 November 2026. Cloudflare already has controls at every layer, from what an agent reads to logs a third party can check, and its defaults are open: an MCP portal enables every tool, including new ones. Its own writing makes the case for the missing piece. In August it published an Agent Access Model, "Its default is deny", and said it is "not comfortable saying that multiplayer access control can be built end to end today". In November it wrote that a narrow scope "only says what the Agent was allowed to do. It doesn't say who answers when the Agent gets it wrong". That is the record an Agent Behaviour Policy is: what this agent was asked to do, the gap from what it can reach, the control holding each row, and who signed it off.

*Source: <https://newsroom.sgit.ai/articles/riskmandate-and-cloudflare.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / RiskMandate and Cloudflare: where agents run, where they are controlled, and why Cloudflare's own Agent Access Model leaves room for a signed record of what each agent was asked to do

# RiskMandate and Cloudflare: where agents run, where they are controlled, and why Cloudflare's own Agent Access Model leaves room for a signed record of what each agent was asked to do

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-09 · [article v1.0.0](versions/riskmandate-and-cloudflare.md) · [newsroom v0.14.72](https://newsroom.sgit.ai/admin/versions.html) · riskmandateabpcloudflareagentsmcpzero-trustai-gatewaycontrolsarticle

***Abstract:** Cloudflare is two things for agents. It is a place to build and run them (the Agents SDK, sandboxes, a headless browser, models, an AI Gateway, remote MCP servers), and a place to control them (Access in front of MCP servers, a new risk tier per tool called WriteGuard, data loss prevention on prompts, signed identities for agents on the web). This maps both onto RiskMandate's Agent Behaviour Policies, from Cloudflare's documentation and blog, read on 9 November 2026. Cloudflare already has controls at every layer, from what an agent reads to logs a third party can check, and its defaults are open: an MCP portal enables every tool, including new ones. Its own writing makes the case for the missing piece. In August it published an Agent Access Model, "Its default is deny", and said it is "not comfortable saying that multiplayer access control can be built end to end today". In November it wrote that a narrow scope "only says what the Agent was allowed to do. It doesn't say who answers when the Agent gets it wrong". That is the record an Agent Behaviour Policy is: what this agent was asked to do, the gap from what it can reach, the control holding each row, and who signed it off.*

Eight of Cloudflare's controls for agents, what each holds, and what stays open.

## In short

- **Cloudflare is where agents run and where they are controlled,** often in the same account.
- **It has controls at every layer:** MCP portals and Access policies, approvals in the Agents SDK, WriteGuard's risk tiers, spend and rate caps, sandbox bindings, data loss prevention, signed agent identities.
- **The defaults are open,** and several of the strongest controls are in beta.
- **Cloudflare's own writing names the gap:** a scope says what an agent may do, not what it was asked to do, or who answers when it gets it wrong.
- **An Agent Behaviour Policy is that record,** and Cloudflare's logs are what it can be checked against.
- **Nothing here has been run on Cloudflare by us.** This is a mapping from its documentation and blog, read on 9 November 2026.

## Two roles in one account

I wrote a month ago about [Cloudflare as Lego blocks](cloudflare-as-lego-blocks.md), the pieces a non-specialist can build with. For agents, those pieces split in two.

**Where agents run.** The [Agents SDK](https://developers.cloudflare.com/agents/) gives each agent "a durable identity, local SQL storage, real-time connections, scheduled work, and recoverable execution", each one a Durable Object. Around it: [Workflows](https://developers.cloudflare.com/workflows/) that persist "for minutes, hours, or even weeks"; a [Sandbox](https://developers.cloudflare.com/sandbox/) where "Your Worker decides which application APIs and data the code receives, and whether the code can reach the public Internet"; [Browser Run](https://developers.cloudflare.com/browser-run/), formerly Browser Rendering; Workers AI; [AI Gateway](https://developers.cloudflare.com/ai-gateway/), where "Each log can include the prompt, response, provider, timestamp, status, token usage, cost, duration, and user agent"; and remote MCP servers with Cloudflare's own OAuth provider.

**Where agents are controlled.** Cloudflare One puts [Access in front of MCP servers](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/), to "vet, authorize, and audit every interaction between users and MCP servers"; an AI security report shows which AI apps people use, each "Unreviewed", "In Review", "Unapproved" or "Approved"; Gateway and DLP inspect prompts; [AI Security for Apps](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/), formerly Firewall for AI, detects "prompt injection attacks, PII exposure in prompts, and prompts about unsafe topics"; and [Web Bot Auth](https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/) gives agents a signed identity when they visit other people's sites.

A business can build an agent on the first half and govern it with the second, which is rare.

## The controls, and what they leave open

Each control below is a barrier an Agent Behaviour Policy can record; each "but" is a gap it should list.

- **MCP server portals** let admins choose "the specific tools and prompt templates" for each use, and Access logs "the individual requests made using the tools in the portal". But "all of its tools and prompts are available to portal users by default", and after a sync "new tools and prompts are automatically enabled". Reach grows unless someone curates it.
- **Workers OAuth scopes:** the user consents to scopes. But Cloudflare's own example code says of them: "Advertised, not enforced: check them in the handler." Enforcement is code in each server.
- **Approvals in the Agents SDK:** "Human-in-the-loop (HITL) patterns add approval or input at different layers of an Agent", with `waitForApproval()` and Code Mode's `requiresApproval`. But the developer decides which actions wait, and Code Mode is labelled experimental.
- **AI Gateway spend and rate limits** block requests over a cap "with a `429` response". But they cap how much, not what.
- **Sandbox bindings and egress** decide which APIs, data and internet the code gets: the strongest technical barrier on reach. But nothing records why each binding was granted.
- **DLP and AI Security for Apps** inspect what goes into and out of models. But they see only traffic routed through them, such as endpoints labelled `cf-llm`.
- **Web Bot Auth and verified bots** prove which agent is knocking. But identity is who it is, not what it may do.

## Joe's agent

Cloudflare's WriteGuard example: the agent acts with Joe's permissions, so its reach is Joe's reach.

Cloudflare's [WriteGuard post](https://blog.cloudflare.com/mcp-portal-writeguard-private-beta/) of 5 August opens with a story I would put in front of any board. Bug tickets start closing at noon, moved to Done by Joe. "By 4 p.m., thousands of tickets have been closed, all by Joe." Joe is a good engineer, and not a thousand-tickets-an-hour engineer: it was his agent.

WriteGuard, in private beta, is Cloudflare's answer: "Every tool gets a risk tier, an enabled or disabled state, and a labeling configuration", and it "adds MCP client and session context to the human identity", so the audit event "includes the server, tool, risk tier, outcome, user, client, and duration". By design it does not give agents their own accounts: Joe's agent works with Joe's permissions.

That is a sensible engineering choice, and it is exactly why the policy matters. If the agent's reach is its human's reach, the only place its narrower job is written down is the policy: triage today's tickets, close none without a person. The gap between the two is what closed thousands of tickets.

## Cloudflare's own case for a mandate

Two Cloudflare posts say this more directly than I could.

The [Agent Access Model](https://blog.cloudflare.com/the-agent-access-model/), 5 August, is a framework rather than a product. Its aim is to "make the agent's capability smaller, so there is less to judge in the first place". "A task's scope is declared when the agent is dispatched". "Its default is deny". And, candidly: "We are not comfortable saying that multiplayer access control can be built end to end today."

[Trusted agent delegation](https://blog.cloudflare.com/trusted-agent-delegation/), 5 November, goes further. Agents "ask for, and get, permission to do everything". "A scope of "everything" tells the Site nothing. And even a narrow scope only says what the Agent was allowed to do. It doesn't say who answers when the Agent gets it wrong". And on asking a person to click approve: it "proves some human is present at that moment", "and nothing more".

A declared task scope, a default of deny, and someone who answers: those are the mandate, the barriers and the sign-off of an Agent Behaviour Policy. Cloudflare has built most of the enforcement points. The policy is the document that says, for each agent, which of them to switch on and why, and who signed it.

## Read, set, gate, attest

On Cloudflare, every layer has pieces already; the missing one is the record they are checked against.

Using the four layers from [the Manus mapping](riskmandate-and-manus.md):

1. **Read:** the policy in the agent's instructions, in an Agents SDK agent or a portal's prompt templates. Exists; soft.
2. **Set:** portal tool lists, Access policies per tool, Gateway caps, sandbox bindings and egress. Exists; the defaults are open, so the policy says what to close.
3. **Gate:** `waitForApproval`, `requiresApproval` and WriteGuard's tiers on write tools. Exists in the SDK; WriteGuard is in private beta.
4. **Attest:** Access request logs, AI Gateway logs and WriteGuard's audit events. The evidence exists; what is missing is a signed mandate to check it against.

Unlike Manus, where the gate and the evidence were proposals, on Cloudflare they are mostly there. That makes the policy more useful, not less: it is the part that turns logs into a yes or a no.

## What RiskMandate could offer Cloudflare users

- **A policy per agent built on Cloudflare,** with reach read from what is actually configured: portal tools, Access policies, bindings, Gateway limits.
- **Templates for the common shapes:** an Agents SDK agent with a sandbox; a team's MCP portal; a coding agent signed in through `cloudflared`, which "authenticates under your user identity".
- **A check of open defaults:** every portal tool enabled, new tools auto-enabled, scopes not enforced in a handler.
- **A gate from the policy:** the rows marked "needs a person" become the actions that call `waitForApproval`, or the tools WriteGuard marks as high risk. Proposed, not built.

## What this does not claim

- **We have not run any of this on Cloudflare.** It is a mapping from documentation and blog posts read on 9 November 2026.
- **Status is as each page states it;** several pages give none, and WriteGuard and identity-aware AI Gateway are in beta.
- **Joe is Cloudflare's example;** the "triage, close none without a person" mandate is ours, to show the shape.
- **RiskMandate has no relationship with Cloudflare,** beyond being a customer for its domains.

## Where this comes from

Cloudflare's documentation, read 9 November 2026: [Agents](https://developers.cloudflare.com/agents/), [human-in-the-loop](https://developers.cloudflare.com/agents/concepts/agentic-patterns/human-in-the-loop/), [MCP authorization](https://developers.cloudflare.com/agents/model-context-protocol/protocol/authorization/), [MCP governance](https://developers.cloudflare.com/agents/model-context-protocol/protocol/governance/), [MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/), [authenticating agents to Access](https://developers.cloudflare.com/cloudflare-one/access-controls/authenticate-agents/), [Workflows](https://developers.cloudflare.com/workflows/), [Sandbox](https://developers.cloudflare.com/sandbox/), [Browser Run](https://developers.cloudflare.com/browser-run/), [AI Gateway](https://developers.cloudflare.com/ai-gateway/), [AI Security for Apps](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/), [Web Bot Auth](https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/). Cloudflare's blog: [WriteGuard](https://blog.cloudflare.com/mcp-portal-writeguard-private-beta/) and [the Agent Access Model](https://blog.cloudflare.com/the-agent-access-model/) (5 August 2026), [trusted agent delegation](https://blog.cloudflare.com/trusted-agent-delegation/) (5 November 2026). [RiskMandate](https://riskmandate.ai/). Earlier on this site: [Cloudflare as Lego blocks](cloudflare-as-lego-blocks.md), [RiskMandate and Manus](riskmandate-and-manus.md), [governs, enforces, attests](governs-enforces-attests.md), [are hooks the sweet spot?](are-hooks-the-sweet-spot.md).

## Threads

Agents & policySite & engineering[This article as a graph →](graphs.md#riskmandate-and-cloudflare)

### Builds on

- [Cloudflare as Lego blocks: what a non-specialist can build on it in October 2026, and an sgit vault in 83 lines](cloudflare-as-lego-blocks.md) Cloudflare's developer platform as the smallest free blocks a non-specialist can use, and an sgit vault on it: no code read-only, 83 lines read-write.
- [RiskMandate and Manus: mapping an Agent Behaviour Policy onto a general agent that can use your computer, your browser, your logins and 416 connectors, and the controls Manus already gives you](riskmandate-and-manus.md) How an Agent Behaviour Policy maps onto Manus: its reach, the controls it already gives you, and the gap between them.
- [Governs, enforces, attests: what an Agent Behaviour Policy does, the three levels at which its rules are kept, and why an attestation layer on top is the piece a third party needs](governs-enforces-attests.md) An ABP governs and names the enforcer at three levels: prompt, hooks, or a third-party system. An attestation layer signs it so a third party can verify.
- [Are hooks the sweet spot? Moving an agent's rules from hope into hooks, rule by rule, until enforcement moves off the machine](are-hooks-the-sweet-spot.md) One agent's eleven rules, moved from the prompt into hooks and tested: four fully, two mostly, three partly, two not at all, and a gap in the leak scan.

### Continued by

- [RiskMandate and Lovable: mapping an Agent Behaviour Policy onto an app builder whose agent writes the code, changes the live database, connects your other systems and publishes, with the controls Lovable already gives and their defaults](riskmandate-and-lovable.md) Lovable's agent can change production; its controls are real, its defaults open, and a policy says what each project's agent may do.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 390 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=390)

**Posting this article on LinkedIn?** The cover is [riskmandate-and-cloudflare.jpg](banners/riskmandate-and-cloudflare.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/riskmandate-and-cloudflare.html)*
