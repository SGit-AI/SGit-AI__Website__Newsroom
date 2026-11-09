# RiskMandate and Manus: mapping an Agent Behaviour Policy onto a general agent that can use your computer, your browser, your logins and 416 connectors, and the controls Manus already gives you, sgit.ai

> Manus is a general AI agent that works in a cloud computer, on your own computer through Manus Studio, in your browser with your logged-in sessions, and across 416 connectors, on schedules and triggers when nobody is watching. It takes the stage at Web Summit's opening night tonight, independent again after China blocked Meta's purchase of it. This is a mapping, from Manus's own documentation, of how RiskMandate and Agent Behaviour Policies can work with it. The short version: Manus already gives you real controls, such as permission modes, session approval, approved senders and trigger conditions, and its documentation is candid about what they leave open, such as "approval modes limit changes, not reading". An Agent Behaviour Policy is the record that lists what a Manus deployment can reach, what the business asked it to do, the gap between the two, and which of those controls holds each row. It can live in four places in Manus: as words the agent reads (a Project instruction or a Skill), as settings, as a gate in front of internal systems (a custom MCP server), and as evidence signed off as a licence to operate. The first two exist in Manus today; the last two are proposals. Nothing here has been run on Manus yet.

*Source: <https://newsroom.sgit.ai/articles/riskmandate-and-manus.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / RiskMandate and Manus: mapping an Agent Behaviour Policy onto a general agent that can use your computer, your browser, your logins and 416 connectors, and the controls Manus already gives you

# RiskMandate and Manus: mapping an Agent Behaviour Policy onto a general agent that can use your computer, your browser, your logins and 416 connectors, and the controls Manus already gives you

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-09 · [article v1.0.0](versions/riskmandate-and-manus.md) · [newsroom v0.14.71](https://newsroom.sgit.ai/admin/versions.html) · riskmandateabpmanusagentsweb-summitmcpbrowser-agentscontrolsarticle

***Abstract:** Manus is a general AI agent that works in a cloud computer, on your own computer through Manus Studio, in your browser with your logged-in sessions, and across 416 connectors, on schedules and triggers when nobody is watching. It takes the stage at Web Summit's opening night tonight, independent again after China blocked Meta's purchase of it. This is a mapping, from Manus's own documentation, of how RiskMandate and Agent Behaviour Policies can work with it. The short version: Manus already gives you real controls, such as permission modes, session approval, approved senders and trigger conditions, and its documentation is candid about what they leave open, such as "approval modes limit changes, not reading". An Agent Behaviour Policy is the record that lists what a Manus deployment can reach, what the business asked it to do, the gap between the two, and which of those controls holds each row. It can live in four places in Manus: as words the agent reads (a Project instruction or a Skill), as settings, as a gate in front of internal systems (a custom MCP server), and as evidence signed off as a licence to operate. The first two exist in Manus today; the last two are proposals. Nothing here has been run on Manus yet.*

Where Manus can act, the control it gives you, and what stays open, from its documentation.

## In short

- **Manus is a general agent with wide reach:** a cloud computer per task, your own computer, your browser with your logins, 416 connectors, and automations that run with nobody watching.
- **It already has real controls,** and its documentation says plainly what they leave open.
- **An Agent Behaviour Policy is the missing record:** what this Manus deployment can reach, what it was asked to do, the gap, and which control holds each row.
- **The policy can live in four places:** read (instruction or Skill), set (Manus settings), gate (a custom MCP server), attest (evidence and sign-off).
- **Read and set exist in Manus today;** gate and attest are proposals.
- **Nothing here has been run on Manus yet.** This is a mapping from its documentation, read on 9 November 2026.

## Why Manus, and why now

Manus is on Web Summit's opening night in Lisbon tonight: its co-founder and chief product officer, Tao Zhang, is scheduled to appear, as [Tech Times reported](https://www.techtimes.com/articles/330276/20261109/web-summit-2026-opens-tonight-manus-ai-blocked-meta-beijing-takes-lisbon-stage.htm) this morning. RiskMandate's stand is on Thursday.

It has had an unusual year. Meta announced it would buy Manus for about $2 billion in December 2025; China's National Development and Reform Commission [blocked the deal on 27 April 2026](https://www.cnbc.com/2026/04/27/meta-manus-china-blocks-acquisition-ai-startup.html); and in October Manus [raised more than $500 million](https://www.cnbc.com/2026/10/08/manus-fund-raise-meta-muse-tencent.html) in its first round since, saying it had resumed independent operations.

For RiskMandate, Manus is interesting for a simpler reason: it is the agent with the most reach that an ordinary business can switch on in an afternoon. A product that writes down what an agent can reach, and what it was asked to do, should be able to do that for Manus.

## What Manus can reach

From [the Manus documentation](https://manus.im/docs/llms.txt):

- **A cloud sandbox per task.** Manus "operates in a complete sandbox environment" with "a virtual computer with internet access, a persistent file system", and can install software.
- **Your own computer,** through [Manus Studio](https://manus.im/docs/features/desktop.md), the desktop app: your files in a folder you choose, your terminal (Python, Node.js, Git), your apps through Computer Use, your GPU, and Remote Control from your phone.
- **Your browser, with your logins,** through [Browser Operator](https://manus.im/docs/features/browser-operator.md), an extension that works "using your existing logins and sessions"; or a [Cloud Browser](https://manus.im/docs/features/cloud-browser.md) you log your accounts into.
- **416 connectors:** 13 app connectors, 369 MCP connectors and 34 API key connectors, plus [custom MCP servers](https://manus.im/docs/integrations/custom-mcp.md) for internal systems.
- **Automations:** [schedules and triggered tasks](https://manus.im/docs/automations.md) that start from a time or an event, such as a new GitHub pull request, a Shopify refund or an invoice email.
- **Mail Manus:** tasks started by [forwarding an email](https://manus.im/docs/features/mail-manus.md) to a bot address.
- **Projects and Skills:** a [Project](https://manus.im/docs/features/projects.md) gives every task a master instruction and a knowledge base; a [Skill](https://manus.im/docs/features/skills.md) is a `SKILL.md` with scripts, loaded with a slash command.

That is a long list of reach, and each item is a row in an Agent Behaviour Policy.

## The controls Manus already gives you

This is the part I did not expect. Manus documents its controls clearly, and says what they do not cover.

- **Permission modes in Manus Studio.** Three modes: "Ask for approval", "Approve for me" (the default, where an automatic review approves safe actions and "blocks high-risk actions, such as sending private keys to the internet"), and "Full access". In the two approval modes, network access, changes outside the workspace and a change of folder need approval.
- **A plain statement of the gap.** The same page says: "Approval modes limit changes, not reading." Commands "can still read other files that your user account can open". And: "Manus plans and decides each step in the Manus cloud. The commands run on your computer."
- **Session approval in the browser.** For Browser Operator, "You must authorize every session", and "All actions are logged".
- **Approved senders for email.** "Only emails from pre-approved sender addresses can trigger tasks."
- **Conditions and test runs for automations,** and cookies cleared when a collaborator joins a task with logins.

Each of these is what an Agent Behaviour Policy calls a barrier: something that actually stands between a capability and its misuse. And each of those honest sentences is what a policy calls the gap: what the agent can do that nobody asked it to.

## A policy for one Manus deployment

A sample policy for a Manus task that researches prospects every morning: reach, mandate, gap and barrier.

Take an invented but ordinary deployment: a Manus task that runs every morning at 08:00, reads prospect replies in Gmail, looks people up on LinkedIn through Browser Operator, and adds notes to the CRM.

The policy lists what it can reach (send email, everything your LinkedIn session can do, edit and delete deals, run with nobody watching, read instructions inside forwarded email), what the business actually asked for (read replies, read public profiles, add notes), and the gap between them. Then, for each row of the gap, the barrier: a Manus setting where one exists, an instruction where only words hold it, and "open" where nothing does.

That last column is the useful one. It turns "we use Manus" into a list a CISO, a CTO and an insurer can all read, with the open rows visible.

## Four places the policy lives

Read, set, gate, attest: from words the agent reads to evidence a third party can check.

1. **Read.** The policy goes in the Project's master instruction, so every task in that Project starts with it, and as a Skill the agent loads. This is the [policy beside the prompt](a-policy-beside-the-prompt.md). It exists in Manus today, and it is soft: a model can drift from its instructions.
2. **Set.** Each barrier the policy names is a Manus setting that is on or off: the permission mode, the approved senders, which connectors are connected, the trigger conditions. RiskMandate records which are on, and the policy is re-checked when one changes.
3. **Gate.** For internal systems, a custom MCP server sits between Manus and the system and checks each call against the policy. Manus's own documentation lists, among the uses of custom MCP servers, "Approval workflows before data updates". This is a proposal: we have not built one for Manus. It is the same move as [moving rules into hooks](are-hooks-the-sweet-spot.md), and the same idea as [SHarness](introducing-sharness.md) for the commands an agent runs.
4. **Attest.** Manus logs browser actions and keeps the task history. That record could be the evidence that the policy held, and the policy, signed off, the licence to operate for that deployment. Also a proposal: we have not seen the logs' format.

Each step moves a rule further from what the model says and closer to what the system does, which is the point of [governs, enforces, attests](governs-enforces-attests.md).

## What RiskMandate could offer Manus users

- **Templates per Manus surface:** Manus in the cloud only; Manus Studio on a laptop; Browser Operator with the user's logins; an automation that runs unattended. Each starts with the reach the documentation describes.
- **The policy as a Manus Skill.** Manus imports Skills from GitHub, and RiskMandate's templates are already published under CC BY 4.0, so a template could be one import away. Proposed, not built.
- **The five-minute try in Manus.** On riskmandate.ai the try runs in Claude or ChatGPT: ask for something the agent should not do on its own, add a sentence saying it must not, start again and compare. The same three steps should work in a Manus task. Untested.
- **A policy for each Manus Project** at one of RiskMandate's one-off prices, from £10 for the pack to £1,500 with two sessions and a professional sign-off, the gap measured on the actual connectors and settings.

## What this does not claim

- **Nothing here has been run on Manus.** The mapping is from its public documentation, read on 9 November 2026; behaviour may differ.
- **The deployment is invented,** to show the shape of a policy.
- **"Gate" and "attest" are proposals;** "read" and "set" use features Manus documents today.
- **This says nothing about the safety of Manus as a product.** Its controls are described as its documentation describes them.
- **RiskMandate has no relationship with Manus.**

## Where this comes from

The Manus documentation, read 9 November 2026: [the index](https://manus.im/docs/llms.txt), [Manus Studio](https://manus.im/docs/features/desktop.md), [Browser Operator](https://manus.im/docs/features/browser-operator.md), [Cloud Browser](https://manus.im/docs/features/cloud-browser.md), [Connectors](https://manus.im/docs/integrations/connectors.md), [Custom MCP Servers](https://manus.im/docs/integrations/custom-mcp.md), [Automations](https://manus.im/docs/automations.md), [Mail Manus](https://manus.im/docs/features/mail-manus.md), [Projects](https://manus.im/docs/features/projects.md), [Skills](https://manus.im/docs/features/skills.md) and [Manus Collab](https://manus.im/docs/features/collab.md); [manus.im](https://manus.im/). The news: [CNBC, 27 April 2026](https://www.cnbc.com/2026/04/27/meta-manus-china-blocks-acquisition-ai-startup.html), [CNBC, 8 October 2026](https://www.cnbc.com/2026/10/08/manus-fund-raise-meta-muse-tencent.html), [Tech Times, 9 November 2026](https://www.techtimes.com/articles/330276/20261109/web-summit-2026-opens-tonight-manus-ai-blocked-meta-beijing-takes-lisbon-stage.htm). [RiskMandate](https://riskmandate.ai/). Earlier on this site: [a policy beside the prompt](a-policy-beside-the-prompt.md), [governs, enforces, attests](governs-enforces-attests.md), [are hooks the sweet spot?](are-hooks-the-sweet-spot.md), [SHarness](introducing-sharness.md), [who else controls AI agents at Web Summit](who-else-controls-ai-agents-at-web-summit.md).

## Threads

Agents & policyStartups & strategy[This article as a graph →](graphs.md#riskmandate-and-manus)

### Builds on

- [A policy beside the prompt: a proposal that every agent takes a behaviour policy as an input, with enforcement and liability attached, and why aviation and payments say the vendors should want it](a-policy-beside-the-prompt.md) A proposal: every agent takes a behaviour policy beside its prompt, which the vendor accepts and answers for, as aviation and payments learned to.
- [Are hooks the sweet spot? Moving an agent's rules from hope into hooks, rule by rule, until enforcement moves off the machine](are-hooks-the-sweet-spot.md) One agent's eleven rules, moved from the prompt into hooks and tested: four fully, two mostly, three partly, two not at all, and a gap in the leak scan.
- [SHarness: the secure harness we could not find, so we built it, a behaviour policy the Linux kernel enforces for every process an agent starts, and we would like your feedback](introducing-sharness.md) SHarness, the secure harness we built when we could not find one: behaviour policies the Linux kernel enforces on every process an agent starts.
- [Governs, enforces, attests: what an Agent Behaviour Policy does, the three levels at which its rules are kept, and why an attestation layer on top is the piece a third party needs](governs-enforces-attests.md) An ABP governs and names the enforcer at three levels: prompt, hooks, or a third-party system. An attestation layer signs it so a third party can verify.
- [Who else controls AI agents at Web Summit? An outreach agent mapped eleven companies in an afternoon, in their own words, and found that most of them are partners for RiskMandate as much as competitors](who-else-controls-ai-agents-at-web-summit.md) An outreach agent mapped eleven companies that control AI agents at Web Summit; most are partners for RiskMandate as much as competitors.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 389 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=389)

**Posting this article on LinkedIn?** The cover is [riskmandate-and-manus.jpg](banners/riskmandate-and-manus.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/riskmandate-and-manus.html)*
