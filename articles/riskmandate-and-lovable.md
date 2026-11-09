# RiskMandate and Lovable: mapping an Agent Behaviour Policy onto an app builder whose agent writes the code, changes the live database, connects your other systems and publishes, with the controls Lovable already gives and their defaults, sgit.ai

> Lovable's agent does more than write code. In Build mode it applies every change directly, it can change the database your published app uses, configure sign-up rules, call your connected systems, and publish, and with /goal it works for hours without stopping to ask. Lovable gives real controls for all of this: always, ask or never for each backend action; Plan mode; the SQL shown before a breaking migration; a security scan on every publish; workspace policies; a pre-prompt hook; audit logs. And it is certified to AIUC-1, the agent standard insurers read. This maps those controls onto RiskMandate's Agent Behaviour Policies, from Lovable's documentation, read on 9 November 2026. The pattern is the same as at Manus and Cloudflare, with one difference: the defaults. Nine of ten backend permissions default to "Always allow", including changing data and configuring auth, and they are set per user, for every workspace and project. The policy is the record of what each project's agent was asked to do, which of those settings should be "Ask each time" for it, and who signed that off.

*Source: <https://newsroom.sgit.ai/articles/riskmandate-and-lovable.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / RiskMandate and Lovable: mapping an Agent Behaviour Policy onto an app builder whose agent writes the code, changes the live database, connects your other systems and publishes, with the controls Lovable already gives and their defaults

# RiskMandate and Lovable: mapping an Agent Behaviour Policy onto an app builder whose agent writes the code, changes the live database, connects your other systems and publishes, with the controls Lovable already gives and their defaults

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-09 · [article v1.0.0](versions/riskmandate-and-lovable.md) · [newsroom v999.0.0](https://newsroom.sgit.ai/admin/versions.html) · riskmandateabplovableagentsvibe-codingsupabaseaiuc-1controlsarticle

***Abstract:** Lovable's agent does more than write code. In Build mode it applies every change directly, it can change the database your published app uses, configure sign-up rules, call your connected systems, and publish, and with /goal it works for hours without stopping to ask. Lovable gives real controls for all of this: always, ask or never for each backend action; Plan mode; the SQL shown before a breaking migration; a security scan on every publish; workspace policies; a pre-prompt hook; audit logs. And it is certified to AIUC-1, the agent standard insurers read. This maps those controls onto RiskMandate's Agent Behaviour Policies, from Lovable's documentation, read on 9 November 2026. The pattern is the same as at Manus and Cloudflare, with one difference: the defaults. Nine of ten backend permissions default to "Always allow", including changing data and configuring auth, and they are set per user, for every workspace and project. The policy is the record of what each project's agent was asked to do, which of those settings should be "Ask each time" for it, and who signed that off.*

Eight of Lovable's controls for its agent, what each holds, and what stays open.

## In short

- **Lovable's agent can change production:** code applied directly, the live database, auth settings, connected systems, and publishing.
- **Lovable has controls for each:** permissions per backend action, Plan mode, migration approval, scans, publish blocks, workspace policies, a pre-prompt hook, audit logs.
- **The defaults are open:** nine of ten backend permissions are "Always allow", set per user for every workspace.
- **Lovable is certified to AIUC-1;** that covers the platform, not what your project's agent was asked to do.
- **An Agent Behaviour Policy is that record,** and turns the right settings to "Ask each time" for each project.
- **Nothing here has been run on Lovable by us.** This is a mapping from its documentation, read on 9 November 2026.

## Why Lovable

I have written about Lovable twice: [from Lovable to your own newsroom](from-lovable-to-your-own-newsroom.md), on moving its apps to GitHub Pages, and [Lovable with SHarness](lovable-with-sharness.md), on keeping an app builder's code inside a policy. This time the question is the agent itself.

Lovable is where a lot of people build their first app, and in August it [raised $400 million](https://lovable.dev/blog/series-c) "at a $13.3 billion valuation". Many of those builders are not engineers, which is the point of Lovable, and it is also why the agent's defaults matter more here than on a developer platform.

## What Lovable's agent can reach

From [Lovable's documentation](https://docs.lovable.dev/llms.txt):

- **Three modes.** [Build mode](https://docs.lovable.dev/features/agent-mode.md) is Lovable's "autonomous execution mode", and "All changes are applied directly to your project". [Plan mode](https://docs.lovable.dev/features/plan-mode.md) "never modifies your code". [Chat mode](https://docs.lovable.dev/features/chat-mode.md) is "Read-only for your project, not for connected tools."
- **Long runs.** With [/goal](https://docs.lovable.dev/features/goal-runs.md), "Lovable doesn't pause to ask questions about the work", and a goal can take hours.
- **The backend.** [Lovable Cloud](https://docs.lovable.dev/features/cloud.md), built on Supabase, adds a database, storage, authentication and functions, and database edits apply to "the same database your published app uses".
- **Connectors.** Shared connectors to services such as Stripe, Shopify, Salesforce, HubSpot or Google Workspace, used by the app, and personal MCP connectors used in chat. For shared ones, "Access mirrors the connected account."
- **Secrets,** encrypted and injected into functions; and Stripe keys, where the form accepts "a restricted key (`rk_...`) or a secret key (`sk_...`), in test or live mode".
- **Browser testing,** where the agent clicks through the app, and **publishing**, where "Lovable asks for approval before publishing unless you have set the publish tool to auto-approve."

## The defaults

Lovable Cloud's ten backend permissions and their defaults; three of them change production without asking.

This is the part of the documentation I would show any team using Lovable. Each backend action has three settings: "Always allow", "Ask each time" and "Never allow". Lovable's own [table of defaults](https://docs.lovable.dev/features/cloud.md) sets nine of the ten to "Always allow", among them:

- **Modify database:** schema and policy changes through SQL migrations.
- **Change data:** add, update or delete data in your tables.
- **Configure auth:** for example, sign-up policies.

The one exception is the right one: breaking migrations, such as dropping or renaming a table, default to "Never allow", and with "Ask each time" "Lovable shows you the SQL and asks for your approval".

Two things make these defaults matter more. They are saved per user and "apply in every workspace and project", so they are not set per project or per agent. And on a team, the organisation cannot set them for its members; each person's choice follows them.

None of this is hidden. It is a sensible default for someone building alone on a weekend. It is a gap for a business whose Lovable app holds customer data.

## The controls, and what they leave open

- **Plan mode** puts a person's yes before any code. But it is optional, and Build mode and /goal run without it.
- **Connector approvals** ask before writes to other systems. But "Tools the server marks as read-only run without asking", and "Always allow all tools from this connection" is one click that stays.
- **The security scan** "runs automatically every time you publish", including a check for tables without row-level security. Lovable is candid that scans "cannot guarantee complete security". **Blocking publishing on critical issues** is available on every plan, but its default is "Disabled, except on new Enterprise workspaces", and "Passing it does not prove that your app is secure."
- **Workspace policies** on Enterprise can require approval before public apps, connectors or sensitive data. But "Policies have no test mode."
- **Secrets and connector credentials** are write-only: no person can read them back. But the agent and the app still use them, and a full live Stripe key is accepted.
- **The pre-prompt hook** on Business and Enterprise can refuse a message: "Any `deny` blocks submission." **Audit logs** on Enterprise record events such as "Prompt sent". Both see prompts, not each action the agent takes.

## The platform is certified; the project is not

In July Lovable announced it was the ["first AI coding agent platform to achieve AIUC-1"](https://lovable.dev/blog/aiuc-1), the agent standard I wrote about when [reviewing the AI insurance stack](underwriting-the-agent-economy-reviewed.md). Its enterprise page lists "SOC 2 Type II, ISO 27001:2022, AIUC-1, GDPR, DPA".

That is real, and it is about Lovable. It cannot say what your project's agent was asked to do, or whether the settings on your account match it. Lovable's own history shows why both levels are needed: in April it reported that "Between February 3, 2026 and April 20, 2026 public project chat history and source code could potentially be accessed by any Lovable user" with a project link, that earlier reports "were closed without being escalated", and that it "shipped a fix within two hours" once they were. A platform certificate and a fast fix are the platform's side. The project's side is a record of its own reach, mandate and gaps.

## Read, set, gate, attest

On Lovable, each layer has pieces; the strong ones are on paid tiers and the defaults are open.

1. **Read:** the policy in the project's knowledge, so every message starts with it. Exists; soft.
2. **Set:** the backend permissions the policy marks as needing a person go to "Ask each time"; connector rights; the publish block on; restricted project access. Exists; per user, not per agent.
3. **Gate:** Plan approval, the SQL shown before a migration, workspace policies, and the pre-prompt hook, which could check a prompt against the policy before it is sent. Exists; policies and the hook are on paid tiers. Using the hook for a policy is proposed.
4. **Attest:** audit logs exported to a SIEM, scan results at each publish, AIUC-1 for the platform. Prompts are logged; each agent action is in the project's timeline, not the audit log.

## What RiskMandate could offer Lovable users

- **A policy per Lovable project,** with reach read from its actual settings: which permissions are "Always allow", which connectors are shared and as whom, whether the publish block is on.
- **A settings checklist from the policy:** for a project with customer data, "Change data" and "Configure auth" to "Ask each time", the publish block on, restricted Stripe keys only.
- **A pre-prompt hook from the policy,** refusing prompts that ask for what the mandate excludes. Proposed, not built.
- **The policy next to the certificate:** AIUC-1 for the platform, the Agent Behaviour Policy for the project, both for the insurer.

## What this does not claim

- **We have not run any of this on Lovable.** It is a mapping from Lovable's documentation, read on 9 November 2026.
- **Status:** Lovable's documentation labels few features as beta; where it says nothing, we have not assumed more.
- **The incident is described in Lovable's own words** from its post of 22 April 2026.
- **RiskMandate has no relationship with Lovable.**

## Where this comes from

Lovable's documentation, read 9 November 2026: [the index](https://docs.lovable.dev/llms.txt), [Build mode](https://docs.lovable.dev/features/agent-mode.md), [Plan mode](https://docs.lovable.dev/features/plan-mode.md), [Chat mode](https://docs.lovable.dev/features/chat-mode.md), [goal runs](https://docs.lovable.dev/features/goal-runs.md), [Lovable Cloud](https://docs.lovable.dev/features/cloud.md), [database](https://docs.lovable.dev/features/database.md), [account settings](https://docs.lovable.dev/introduction/lovable-account-settings.md), [chat connectors](https://docs.lovable.dev/integrations/chat-connectors.md), [connector security](https://docs.lovable.dev/integrations/security.md), [Stripe](https://docs.lovable.dev/integrations/stripe.md), [security](https://docs.lovable.dev/features/security.md), [privacy and security settings](https://docs.lovable.dev/features/privacy-and-security-settings.md), [workspace policies](https://docs.lovable.dev/features/workspace-policies.md), [publishing](https://docs.lovable.dev/features/publish.md), [audit logs](https://docs.lovable.dev/features/audit-logs.md), [the pre-prompt hook](https://docs.lovable.dev/api-reference/hooks/message-before-submit-v1.md), [Lovable for enterprise](https://docs.lovable.dev/introduction/lovable-for-enterprise.md). Lovable's blog: [AIUC-1](https://lovable.dev/blog/aiuc-1) (22 July 2026), [Series C](https://lovable.dev/blog/series-c) (12 August 2026), [its response to the April 2026 incident](https://lovable.dev/blog/our-response-to-the-april-2026-incident) (22 April 2026). [RiskMandate](https://riskmandate.ai/). Earlier on this site: [Lovable with SHarness](lovable-with-sharness.md), [from Lovable to your own newsroom](from-lovable-to-your-own-newsroom.md), [RiskMandate and Manus](riskmandate-and-manus.md), [RiskMandate and Cloudflare](riskmandate-and-cloudflare.md), [underwriting the agent economy, reviewed](underwriting-the-agent-economy-reviewed.md).

## Threads

Agents & policyStartups & strategy[This article as a graph →](graphs.md#riskmandate-and-lovable)

### Builds on

- [From Lovable to your own newsroom: a brief for José Bota and his agent, to put every app on GitHub Pages under his own domain, and publish each one as an article](from-lovable-to-your-own-newsroom.md) From Lovable to your own newsroom: a brief for José Bota and his agent, every app on GitHub Pages under his own domain, each an article.
- [Lovable with SHarness, and the trojanised Claude Code extension: how to keep an app builder's code and an editor's extensions inside a policy, and what SHarness can and cannot stop today](lovable-with-sharness.md) Lovable with SHarness, and the trojanised Claude Code extension: where a policy boundary has to sit, and what SHarness can stop today.
- [Underwriting the agent economy, reviewed: the cliff notes of the AI insurance stack, the companies already selling AI agent cover, and what agent behaviour policies add to it](underwriting-the-agent-economy-reviewed.md) A review of the AI insurance stack blueprint, the companies selling agent cover, and what agent behaviour policies add to it.
- [RiskMandate and Manus: mapping an Agent Behaviour Policy onto a general agent that can use your computer, your browser, your logins and 416 connectors, and the controls Manus already gives you](riskmandate-and-manus.md) How an Agent Behaviour Policy maps onto Manus: its reach, the controls it already gives you, and the gap between them.
- [RiskMandate and Cloudflare: where agents run, where they are controlled, and why Cloudflare's own Agent Access Model leaves room for a signed record of what each agent was asked to do](riskmandate-and-cloudflare.md) Cloudflare runs agents and controls them; its own writing leaves room for a signed record of what each agent was asked to do.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 391 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=391)

**Posting this article on LinkedIn?** The cover is [riskmandate-and-lovable.jpg](banners/riskmandate-and-lovable.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/riskmandate-and-lovable.html)*
