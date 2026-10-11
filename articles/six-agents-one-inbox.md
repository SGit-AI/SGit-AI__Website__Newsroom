# Six agents, one inbox: what a real multi-agent setup taught me about access policies, sgit.ai

> For the past few weeks I have run agents on dedicated accounts, a Google Workspace seat, a Claude Team seat and a GitHub account per agent, and split the work across six roles: a scheduled reader of the inbox, a mailbox agent that drafts, an inbox agent that sends, a CRM agent, a dev team agent and a site editor. This article is what that setup taught me, and it is mostly about the gap between the policy I wanted and what the tools can enforce. Three findings. The account, not the session, is the blast radius, so a dedicated account per agent is the first real control anyone has, and it turns out to do more than segregate, because it puts each agent in its own organisational unit where Google's compliance rules become per-agent enforcement. The first exception arrived before the first policy was written: the reader that must never reply must reply when the message comes from me, which is an authentication problem, not a permissions one. And the policy I had written on the assumption that the Gmail connector could not send attachments was wrong, because an agent found the attachments field, proved it with a signed PDF, and wrote up how. The vendor's own two documentation pages disagree about whether the connector can send at all. So the article ends with a table of every rule in the setup against how it is enforced today, by identity, by scope, by a compliance rule, by an approval prompt or by nothing but the agent's good behaviour, and with the argument that a policy is only as real as its worst row.

*Source: <https://newsroom.sgit.ai/articles/six-agents-one-inbox.html> · sgit.ai v0.7.51 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Six agents, one inbox: what a real multi-agent setup taught me about access policies

# Six agents, one inbox: what a real multi-agent setup taught me about access policies

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-09-29 · updated 2026-10-02 · [article v1.2.1, 4 versions](versions/six-agents-one-inbox.md) · [sgit.ai v0.6.19](https://sgit.ai/admin/versions.md) · agentsconnectorsaccess-policiesnon-human-identitygmailgithubriskmandatesecurityarticle

***Abstract:** For the past few weeks I have run agents on dedicated accounts, a Google Workspace seat, a Claude Team seat and a GitHub account per agent, and split the work across six roles: a scheduled reader of the inbox, a mailbox agent that drafts, an inbox agent that sends, a CRM agent, a dev team agent and a site editor. This article is what that setup taught me, and it is mostly about the gap between the policy I wanted and what the tools can enforce. Three findings. The account, not the session, is the blast radius, so a dedicated account per agent is the first real control anyone has, and it turns out to do more than segregate, because it puts each agent in its own organisational unit where Google's compliance rules become per-agent enforcement. The first exception arrived before the first policy was written: the reader that must never reply must reply when the message comes from me, which is an authentication problem, not a permissions one. And the policy I had written on the assumption that the Gmail connector could not send attachments was wrong, because an agent found the attachments field, proved it with a signed PDF, and wrote up how. The vendor's own two documentation pages disagree about whether the connector can send at all. So the article ends with a table of every rule in the setup against how it is enforced today, by identity, by scope, by a compliance rule, by an approval prompt or by nothing but the agent's good behaviour, and with the argument that a policy is only as real as its worst row.*

Six roles, two identities, one policy table. Each agent runs on its own Workspace, Claude and GitHub accounts. The cells say what each agent may do with mail, code and vaults; the colour says how the rule is enforced today: by the identity boundary, by a compliance rule an admin set, by an approval prompt, or by nothing but the agent doing as it was told.

Here is the claim, stated so it can be wrong. **An access policy for an agent is only as real as its worst row.** Write the policy as a table, one row per rule, and add a column for how each rule is enforced. If the column says *the agent has been told*, that row is a hope, and the policy is exactly as strong as that hope on the day something goes wrong. This article is about filling in that column for a setup I actually run, and about three things I did not expect to find.

## In short

- **The account is the blast radius.** Every session an agent opens through a connector runs as the account that authorised it, with everything that account can reach. The first real control is therefore not a policy at all: a dedicated Workspace seat, a dedicated Claude seat and a dedicated GitHub account per agent, so that the worst a session can do is bounded by what its account can see.
- **Dedicated accounts do more than segregate.** An account of its own puts each agent in its own organisational unit, and Google Workspace applies its Gmail compliance rules per unit. Restrict delivery, attachment compliance and scope limits on third-party apps then become per-agent enforcement rather than per-organisation settings. That is the part I had not understood before I ran it.
- **The first exception arrived before the first policy.** The scheduled reader that must never reply must reply when the message came from me. "Never" became "never, unless" on day one, and the "unless" is an authentication problem, which the [PKI and append-lane work](https://sgit.ai/docs/append-lane-messaging.md) already addresses.
- **A policy written from the documentation was wrong.** I had assumed the Gmail connector could not send attachments. An agent found that `create_draft` and `update_draft` accept an `attachments` array, proved it with a 17 KB signed PDF that arrived intact, and wrote it up. The vendor's own documentation says on one page that the connector is read-only and on another that it can send, reply and forward. The only way to know what a connector can do is to try.
- **Enforcement is a ladder, and most rules sit on the bottom step.** Identity boundaries and cryptographic keys enforce themselves. Compliance rules enforce at the platform. Approval prompts enforce at the human. Everything else is the agent doing as it was told. The table at the end grades every rule in the setup.
- **Cowork and Claude Code are different agents with different reach.** In this setup the Cowork agent has no GitHub connector and cannot open the repository at all, while the Claude Code agent can edit the site. Two products from the same vendor, on the same seat, with different blast radii. That is useful, once you know it.
- **The twin argument holds.** The attachment finding is the [connector twin](connector-twin-before-you-deploy-an-agent.md) article's case proven on my own inbox: replay what the agent can actually do before you write down what it may do.

## The setup, and what it costs

The agents run for two identities: the agent for RiskMandate, and the agent for my own domain. I am not going to print their addresses, for the obvious reason, but the shape is the same for both and it is copyable. Each identity has a dedicated Google Workspace account, which is about £7 a month, a seat on a Claude Team plan, and a GitHub account of its own. Nothing the agent does runs as me. Everything it does runs as an account whose mailbox, drive, repositories and connectors I chose.

That sounds like an obvious thing to do. It is the thing almost nobody does, because connectors are designed to be switched on by a person for that person, and the whole appeal is that the agent can see what you see. The research on [nhi.sgit.ai](https://nhi.sgit.ai/) said this plainly when it scored the shared-drive options in August: *"Everything available runs on your identity, the only granularity is segregation rather than scoping, and nothing supports per-agent keys."* Its conclusion, that the practitioner answer is *"a shared drive dedicated to the agent"*, is what the dedicated account generalises. If segregation is the only granularity you can buy, buy it at the account level, where it covers mail, files, code and connectors at once.

Six roles share those two identities, and the split follows what each one is allowed to touch:

| Role | What it does | Runs where |
|---|---|---|
| **The reader** | A scheduled session that reads the inbox, works out what each message wants, and writes a tagged list of what needs to happen | Scheduled Claude session |
| **The mailbox** | Operations and management on the mailbox itself: labels, threads, filing, drafting replies | Cowork |
| **The inbox** | The one role allowed to send, and only from drafts the mailbox agent prepared | Cowork |
| **The CRM** | Customers, workflows and tasks, built on what the reader tagged | Cowork |
| **The dev team** | The vaults, the vault UI and the tooling behind them | Cowork, sgit |
| **The site editor** | Edits and publishes the websites | Claude Code |

The point of six roles rather than one is not neatness. It is that each role gets a policy short enough to check, and the policies differ in the one place that matters: who may send.

## Finding one: the account does more than segregate

I expected the dedicated account to bound what an agent could see. What I did not expect was how much it lets an administrator enforce, because Google Workspace's Gmail controls are set per organisational unit, and an account of its own can be a unit of its own.

Three settings turned out to matter, all under Apps, Google Workspace, Gmail, Compliance in the Admin console, and all applied to a unit rather than the organisation:

- **[Restrict delivery](https://knowledge.workspace.google.com/admin/gmail/advanced/restrict-email-messages-to-authorized-addresses-or-domains-only)** limits a unit to sending and receiving mail only with authorised addresses and domains; anything else *"returned to the sender with a bounce message that describes the policy."* For the reader, whose only legitimate correspondent is me, a delivery restriction to my own domain means that even if it sends, it can only reach me.
- **[Attachment compliance](https://knowledge.workspace.google.com/admin/gmail/advanced/filter-messages-with-attachments)** acts on messages *"based on file type, file name, or message size"*, for outbound mail specifically if you choose, and can reject the message, quarantine it for review, or *"remove attachments"* and let the text through. For every agent that has no business sending files, an outbound rule that strips attachments turns a policy into a property of the mail system.
- **[Scope limits on third-party apps](https://workspaceupdates.googleblog.com/2024/12/configure-third-party-apps-by-select-api-scopes-general-availability.html)**, under Security, API Controls, since December 2024, let an admin *"limit third-party app access to specific OAuth 2.0 scopes for Google APIs, like Drive or Gmail."* This is the sharpest tool and the one with a catch, which the next finding explains.

None of these is new. What is new is having an account per agent to point them at. On a shared identity you cannot restrict delivery for the agent without restricting it for yourself. On a dedicated one you can, and the rule is enforced by Google, not by the agent.

The same move works for code. A dedicated GitHub account is given access to exactly the repositories that agent should touch, either by installing the [Claude GitHub App](https://claude.com/docs/connectors/github) on those repositories alone, or with a [fine-grained personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens), which GitHub describes as able to be *"limited to only access specific repositories"* with *"specific, fine-grained permissions"* and an expiry. The site editor's account sees the website repository and nothing else. That is the first time I have been able to say that about an agent with a GitHub connector, and it is worth the price of the seat by itself.

## Finding two: the exception arrived before the policy

The reader's policy was going to be the simplest: read, classify, write a list, touch nothing else. In particular, never send.

It lasted until the first scheduled run. Some of the messages that land in that inbox are from me, and some of what I send it are instructions: do this, file that, reply to them with this. For those, a reader that only writes a list is wasting the one thing a scheduled agent is for. So the rule became: never reply, unless the message came from me, in which case act on it.

Two things follow, and both are bigger than the reader. First, this is how policies actually get written: from the workflow, one exception at a time, not from principles handed down before anyone has run anything. The list of exceptions *is* the policy, and it is only complete once the workflow has run for a while. Second, "unless it came from me" is not a permissions question. Anyone can put my address in a From header. The exception is only safe if the agent can verify that a message came from me, which is a signature check, and the machinery for that is the one the [append-lane messaging](https://sgit.ai/docs/append-lane-messaging.md) work built for agents talking to each other: per-session keys, a pinned registry of who holds which key, a signature over the message. The reader needs the same registry with one more entry in it, mine.

There is also a cheap partial enforcement for this rule, and it comes from finding one. Put the reader in a unit whose delivery is restricted to my domain, and the failure mode of a spoofed instruction is that the reader sends its reply to me, because that is the only place it can send anything. That does not make the policy right. It makes the worst row bounded.

## Finding three: the policy written from the documentation was wrong

When the Gmail policies were first mapped, one assumption was that an agent could not attach files to mail through the Claude connector. There was no "attach a file" call, the documentation did not mention attachments beyond reading their metadata, and so the policy did not bother to forbid what seemed impossible.

On 27 September an agent working in Cowork needed to send a signed letter and found the way. The debrief it wrote is short and worth quoting: *"The connector has no 'attach a file from disk' call, but `create_draft` and `update_draft` both accept an `attachments` array. Each item carries the file inline as base64."* It shrank a 1.4 MB scanned PDF to 17 KB, base64-encoded it, put it in the draft, verified the MIME structure with `get_draft` in raw format, and I sent the draft by hand. It arrived intact, with Gmail's *"One attachment · Scanned by Gmail"* label and a preview. The debrief also records the gotchas an agent would trip over: a later `update_draft` without the field silently removes the attachments, so attach last; the message and thread ids change on every update but the draft id does not; the bytes pass through the tool call as text, so the practical limit is the size of a call, not Gmail's 25 MB.

I want to be precise about what that finding is and is not. It is not a bypass. The agent used a documented field of a documented call. It is a policy that was written from an assumption about capability, and the assumption was wrong, and the only way it could have been found wrong was by an agent trying to do the thing. That is the [connector twin](connector-twin-before-you-deploy-an-agent.md) argument exactly: before you write down what an agent may do, replay what it can do.

And the vendor's documentation would not have settled it, because the vendor's documentation disagrees with itself. On 29 September 2026, [one Anthropic page](https://claude.com/docs/connectors/google/gmail) says of the Gmail connector: *"Claude reads and searches email only; it can't create, send, or modify messages,"* and lists under limitations *"Claude can't create, send, or modify emails."* [Another](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors) says it can *"Draft emails with proper formatting and context,"* *"Send, reply to, and forward emails from Gmail,"* and that *"By default, Claude asks for your approval before each of these actions. On Team and Enterprise plans, owners decide whether members can allow these actions to run without asking each time."* The debrief proves the second page is closer to the truth, at least for drafts. Neither page mentions the attachments field. I do not say this to criticise the documentation, which is trying to describe a product that changes monthly. I say it because a policy that cites the documentation as its enforcement has cited a moving target.

Here is the catch I promised in finding one. The Gmail API's [scopes](https://developers.google.com/workspace/gmail/api/auth/scopes) put drafting and sending in the same grant: `gmail.compose` is *"Manage drafts and send emails,"* and `gmail.modify` is *"Read, compose, and send emails."* There is no scope that allows drafts and forbids sending. So the Workspace admin's scope limit, the sharpest tool in the box, cannot express the one rule the mailbox agent most needs, *drafts only*. That rule has to be enforced one step down the ladder, by a delivery restriction on the unit, or by an approval prompt, or by the agent doing as it was told.

## Where the reach differs: Cowork and Claude Code

One more thing the setup made visible. The same seat runs two products, and they do not reach the same things.

The Cowork agent, in this setup, has no GitHub connector and cannot open the repository at all, even though the connector is listed in the catalogue and the account has access to the repository on GitHub. The Claude Code agent, on the same seat, opens the repository and edits the site. Whether that is a deliberate boundary or a gap in the product does not matter for the policy; what matters is that it is a real boundary today, and the site editor role is defined around it. The Claude Code agent is the only one that can change the websites, and the only thing its GitHub account can see is the website repositories.

The two products also differ in what an administrator can control. On a Team plan an Owner enables or disables a connector for the whole organisation, and in Cowork there is one further switch, whether members may set *"Always allow"* for *"write-capable connector tools."* Per-tool control, where a specific action can be set to *"Always allow," "Needs approval," or "Blocked"*, exists only in the [Enterprise plan's role-based permissions](https://support.claude.com/en/articles/13930458-set-up-role-based-permissions-on-enterprise-plans). So on a Team plan, *never send* can be a prompt that a person has to click through, and on Enterprise it can be a block. That difference belongs in the enforcement column too.

## The table

Where a rule is enforced, from the top of the ladder down. Identity and keys enforce themselves. Compliance rules enforce at the platform, per organisational unit. Approval prompts enforce at the person. Below that, a rule is the agent doing as it was told. Every rule in the table sits on one of these steps, and the policy is as strong as its lowest.

Here is the policy for the setup, one rule per row, with the column that matters. *Enforced* means the platform or the cryptography prevents the action. *Admin rule* means a Workspace or GitHub setting an administrator applied to the agent's own account or unit. *Approval* means a person is asked before the action runs. *Told* means the agent has been instructed and nothing else stands in the way.

| Rule | Reader | Mailbox | Inbox | CRM | Dev team | Site editor | How it is enforced today |
|---|---|---|---|---|---|---|---|
| Sees only its own account's mail, files and repos | yes | yes | yes | yes | yes | yes | **Enforced**: dedicated accounts |
| Reads mail | yes | yes | yes | yes | no | no | **Admin rule**: connector enabled per seat; Workspace scope limits per unit |
| Creates drafts | no | yes | no | no | no | no | **Approval** on Team, **Blocked** per tool on Enterprise; no scope separates drafts from sending |
| Sends mail | no | no | yes, from drafts only | no | no | no | **Admin rule**: Restrict delivery on every other unit; **Approval** for the inbox agent |
| Sends attachments | no | no | only when a person attached them | no | no | no | **Admin rule**: outbound attachment compliance strips or rejects |
| Replies to a message from me | yes, if verified | no | no | no | no | no | **Told**, until the signature registry has my key; delivery restriction bounds the failure |
| Reads repositories | no | no | no | no | its own | the site's | **Enforced**: GitHub App installed per repository, or a fine-grained token |
| Writes to repositories | no | no | no | no | its own | the site's | **Enforced**: token permissions; Cowork has no GitHub connector here |
| Reads vaults | tagged list | yes | no | yes | yes | yes | **Enforced**: a read key per vault per agent |
| Writes to vaults | no | no | no | yes, CRM vault | yes | no | **Enforced**: the vault key, held only by the writer |
| Acts outside its role | no | no | no | no | no | no | **Told** |

Read the last column top to bottom and the shape of the problem is clear. The rows that touch identity, code and vaults are enforced, because accounts, repositories and keys are boundaries the platform or the mathematics maintains. The rows that touch mail are admin rules and approvals, which is good, and better than I expected before I understood organisational units. And two rows are *told*. One of them, the reply-to-me rule, has a known fix and a bounded failure. The other, *acts outside its role*, is the row every agent policy in the world shares, and no setting anywhere enforces it. It is the reason the [connector twin](connector-twin-before-you-deploy-an-agent.md) exists: if you cannot prevent it, you must at least be able to see it afterwards.

**Follow-up, 2 October 2026.** The step-by-step version of this setup, in phases from one Claude session to the roles described here, is now its own article: [Replicating the agentic inbox](replicating-the-agentic-inbox.md). This page stays the argument about the policy rows; that one is the walkthrough.

## What I would tell somebody starting this

1. **Buy the segregation.** A Workspace seat per agent is £7 a month. It is the only control that covers mail, files, code and connectors at once, and it is the precondition for every admin rule below.
2. **Put each agent in its own organisational unit.** Then restrict delivery for every agent that should not correspond with the world, and strip outbound attachments for every agent that should not send files. These are settings, not hopes.
3. **Give each agent its own GitHub account and install the app per repository.** The site editor sees the site. Nothing else sees anything.
4. **Write the policy as a table, with the enforcement column.** Fill the column honestly. Anything that says *told* is where your next incident comes from, and where your next piece of tooling should go.
5. **Replay before you write.** Have an agent try the things the policy assumes it cannot do. Mine found attachments in an afternoon. The documentation would not have told you.
6. **Expect the exception on day one.** Write the policy from the workflow, and treat the growing list of exceptions as the policy maturing rather than failing.
7. **Journal everything anyway.** For the rows that say *told*, the twin is the only control there is.

## What exists today, and what does not

The setup described here runs: the accounts, the roles, the scheduled reader, the drafting and sending split, the dedicated GitHub account for the site editor. The Workspace compliance rules exist and are documented, and I have linked the documentation rather than restating it. The attachment finding is proven and written up. The append-lane signature registry exists for agent-to-agent messages.

What does not exist yet: my own key in that registry, so the reader's exception is still enforced by instruction; a broker that would let *drafts only* be a block rather than a prompt on a Team plan; and any way to enforce *acts outside its role*. The policy table above is the honest state of a real setup on 29 September 2026, and I would rather publish it with its two *told* rows than pretend they are something else.

## Sources

- The attachment debrief, written by the agent that proved it, 27 September 2026, quoted above; the signed PDF and the addresses are not published
- [nhi.sgit.ai, Shared drives for agents, scored 16 August 2026](https://nhi.sgit.ai/research/shared-drives.html)
- [Google Workspace Admin Help, Restrict email messages to authorized addresses or domains only](https://knowledge.workspace.google.com/admin/gmail/advanced/restrict-email-messages-to-authorized-addresses-or-domains-only)
- [Google Workspace Admin Help, Filter messages with attachments (attachment compliance)](https://knowledge.workspace.google.com/admin/gmail/advanced/filter-messages-with-attachments)
- [Google Workspace Updates, Configure third-party apps by select API scopes, general availability (3 December 2024)](https://workspaceupdates.googleblog.com/2024/12/configure-third-party-apps-by-select-api-scopes-general-availability.html)
- [Gmail API, choose Gmail API scopes](https://developers.google.com/workspace/gmail/api/auth/scopes)
- [Anthropic, Gmail connector documentation (read-only statement)](https://claude.com/docs/connectors/google/gmail)
- [Anthropic Help Center, Use Google Workspace connectors (send, reply and forward statement)](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors)
- [Anthropic Help Center, Set up role-based permissions on Enterprise plans](https://support.claude.com/en/articles/13930458-set-up-role-based-permissions-on-enterprise-plans)
- [Anthropic Help Center, Use Claude Cowork on Team and Enterprise plans](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans)
- [Anthropic, GitHub integration documentation](https://claude.com/docs/connectors/github)
- [GitHub Docs, Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
- [On this site: Before you give an agent a connector, give the connector a twin](connector-twin-before-you-deploy-an-agent.md)
- [On this site: Append-lane messaging between agents, with per-session keys and a pinned registry](https://sgit.ai/docs/append-lane-messaging.md)
- [On this site: Licence to Operate, an agent behaviour policy simulated for one agent](https://sgit.ai/demos/vaults/licence-to-operate/index.md)

*© 2026 Dinis Cruz. This article's own text is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). You're free to share and adapt it, as long as you give credit. Quoted material and linked sources keep their own licences.*

## Threads

Agents & policy[This article as a graph →](graphs.md#six-agents-one-inbox)

### Builds on

- [Before you give an agent a connector, give the connector a twin](connector-twin-before-you-deploy-an-agent.md) An agent with a Gmail or Calendar connector can do things the platform cannot undo; a journal of every call, replayed, shows what it did and what can go back.
- [Replicating the agentic inbox: a walkthrough from one Claude session to a team of agents that never press send](replicating-the-agentic-inbox.md) How to copy a working agentic email setup in phases: a mailbox and Claude seat of the agent's own, one session with a policy, then roles talking in files.

### Continued by

- [The same argument, in our words: Satya Nadella on models as insider risks, translated into the language of RiskMandate](the-same-argument-in-our-words.md) Satya Nadella's case for treating models as insider risks, translated idea by idea into our vocabulary: reach, mandate, gap, barriers and accepted risk.
- [A Mac of the agent's own: a business plan for agent desktops, what Apple's licence allows, and three behaviour policies](a-mac-of-the-agents-own.md) A business plan for a Mac of the agent's own: what Apple's licence allows, a desktop built from vaults per run, and three behaviour policies for one agent.
- [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](riskmandate-ten-questions.md) Ten hard questions from a conference, answered in a two-hour interview: what RiskMandate does, what it deliberately is not, and how mature each part is.
- [Zoom into an agent's behaviour policy and you find the business logic](the-behaviour-policy-is-the-business-logic.md) Below the first rules, an agent's behaviour policy is the business: functions, processes, clients, values. Layered, owned, counted, and where vendors plug in.
- [An open AI governance framework, and what its licence let us build](ai-baseline-control-framework.md) Twenty open AI governance controls under CC BY-SA, why the licence matters, and the same day's conversion into a graph, a database and a walk down to EU law.
- [Where is the why? A permission prompt asked me to decide, and kept the reason](where-is-the-why.md) A prompt asked for a decision and kept the reason. Read through the policy, the law on uninformed consent, and the fixes that worked: put the why in the prompt.
- [The Mandate Stack: a multi-agent system in production, layer by layer](the-mandate-stack.md) A multi-agent system that runs a business every few hours: eight layers, one written mandate per agent, everything a graph, one human who sends.
- [Why my agents do not run on my laptop: chat, Cowork and Code in the cloud, a vault as the shared drive, and the two walls an operating system has](why-my-agents-do-not-run-on-my-laptop.md) An OS has two hard walls, the kernel and the user; an agent on a laptop runs inside the one marked you, so the agents run in the cloud with a vault as shared drive.
- [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](the-agent-team-as-it-runs.md) Twelve agents on dedicated accounts, encrypted vaults as the only memory, messages as files, a folder per person, and a mailbox nobody sends from.
- [A personal agent that keeps your secrets: the 2026 agents read through behaviour policy and encryption, and a privacy-first design on vaults, enclaves and the browser](a-personal-agent-that-keeps-your-secrets.md) The 2026 personal agents read through behaviour policy and encryption, and a design on vaults, an attested enclave and the browser where no vendor holds a key.
- [Send an agent, not a spreadsheet: the next generation of software due diligence, and why the companies that stopped reading their code are about to be asked about it](send-an-agent-not-a-spreadsheet.md) Due diligence never scaled because it was a form; a buyer can now send an agent into a vendor's environment and read what the code and the practices are.
- [If somebody built a company on code review: how I would do it, and why it is only now possible](if-somebody-built-a-company-on-code-review.md) A reader's seven questions answered as a company plan: one reader for every layer, review as a science, and the layers as the customer's own.
- [The identity we wanted to give the agents: a week of design, the line in Google's terms, and why login plus secrets is still too hard](the-identity-we-wanted-to-give-the-agents.md) A week of designing identities for agents and users met Google's terms; what survived is a passkey-unlocked keyring and a gap nobody sells.
- [The wall under the reply: end an email with the state of the thread, not the thread](the-wall-under-the-reply.md) End an email reply with the state of the thread for this reader, not the quoted wall: decided, open, next, who is on copy, with links to the record.
- [Memory is not a spectator sport: how a web of open sites, graphs and vaults became the memory for sessions like this one](memory-is-not-a-spectator-sport.md) Agentic memory as context management: many published, fractal, provenance-carrying memories rather than one store, shown in the session that wrote the article.
- [Replicating the agentic inbox: a walkthrough from one Claude session to a team of agents that never press send](replicating-the-agentic-inbox.md) How to copy a working agentic email setup in phases: a mailbox and Claude seat of the agent's own, one session with a policy, then roles talking in files.
- [Footprint and blast radius: what the agent actually did, and what it would have cost](footprint-and-blast-radius.md) Footprint is what an agent actually did, read afterwards from logs and vault history; blast radius is what a row of its reach would cost the business today.
- [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](custom-uis-are-not-the-exception.md) Every message has a graph, so it can be shaped for the reader's moment; a custom interface per moment is now how interfaces get made, and each gets a policy.
- [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](ultimate-insider-three-collisions.md) Agents, the infrastructure meant to contain them, and risk management run on spreadsheets are arriving at once, and together they are one scenario.

[All articles](index.md) · [All graphs](graphs.md)

## From the desk

- [Create anywhere, edit your own: a rule learned in the inbox, applied to the newsroom](desk/create-anywhere-edit-your-own.md) thread, 2026-10-07
- [Behaviour policy in practice](collections/behaviour-policy-in-practice.md) collection, 11 articles

**Posting this article on LinkedIn?** The cover is [six-agents-one-inbox.jpg](banners/six-agents-one-inbox.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/six-agents-one-inbox.html)*
