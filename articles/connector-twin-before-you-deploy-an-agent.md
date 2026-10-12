# Before you give an agent a connector, give the connector a twin, sgit.ai

> When an AI agent is given a Gmail or Google Calendar connector, it can read, send, move, decline and permanently delete on somebody's behalf, and for several of those actions the platform itself documents that there is no way back. This article argues that a twin of the connector is the minimum requirement for deploying an agent with confidence. The twin is a journal of every request and response the agent makes, appended as it happens to a write-only lane, processed later, and replayed into the inbox and calendar as the agent saw them, with a before and after for every change and a revert plan for each one. It gives provenance, explanation and a named list of what can and cannot be undone, and it changes the agent's behaviour policy from a hope into a list. Every claim about Gmail and Calendar is taken from Google's own documentation and linked. A working replay of an invented session, and a business plan for the service, are published alongside it as a vault.

*Source: <https://newsroom.sgit.ai/articles/connector-twin-before-you-deploy-an-agent.html> · sgit.ai v0.7.79 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Before you give an agent a connector, give the connector a twin

# Before you give an agent a connector, give the connector a twin

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-09-24 · [article v1.1.1, 3 versions](versions/connector-twin-before-you-deploy-an-agent.md) · [sgit.ai v0.6.3](https://sgit.ai/admin/versions.md) · agentsconnectorsdigital-twinsprovenanceriskriskmandatearticle

***Abstract:** When an AI agent is given a Gmail or Google Calendar connector, it can read, send, move, decline and permanently delete on somebody's behalf, and for several of those actions the platform itself documents that there is no way back. This article argues that a twin of the connector is the minimum requirement for deploying an agent with confidence. The twin is a journal of every request and response the agent makes, appended as it happens to a write-only lane, processed later, and replayed into the inbox and calendar as the agent saw them, with a before and after for every change and a revert plan for each one. It gives provenance, explanation and a named list of what can and cannot be undone, and it changes the agent's behaviour policy from a hope into a list. Every claim about Gmail and Calendar is taken from Google's own documentation and linked. A working replay of an invented session, and a business plan for the service, are published alongside it as a vault.*

A twin of the connector. Every call the agent makes is copied, request and response, into an append-only journal in a vault. The journal is processed later and replayed into the inbox and calendar as the agent saw them, with a before and after for every change, and a revert plan that a person approves.

Here is the claim, stated so it can be wrong. **If you cannot say what your agent did, what it saw when it did it, and which of its actions you can undo, you are not ready to give it a connector.** Answering those three questions takes a twin of the connector: a journal of every request and response, and a replay of that journal into the views the agent saw. It is not exotic. Everything it needs exists today.

## In short

- **A connector is a grant of action, not just of access.** An agent with Gmail and Calendar connectors can send, archive, trash, permanently delete, move events, decline invitations and cancel meetings, on somebody's behalf, at machine speed.
- **For several of those actions the platform keeps no way back, and says so.** The Gmail API documents its delete as permanent: "This operation cannot be undone." Undo Send is a feature of the Gmail interface, not of the API. A moved calendar event has no version history a user can open. These are Google's own statements, linked below.
- **What the platform does keep is not what you need.** Trash windows, an administrator's bulk restore and audit logs record that things happened. None of them records what the agent saw when it decided to act, or why.
- **The twin is a journal plus a replay.** Capture the request and the response of every connector call, and the instruction behind it when you can. Append each entry to a write-only lane. Process the lane later. Rebuild the inbox and the calendar as the agent saw them at each step.
- **It scales because it is not a copy of the mailbox.** It holds only what passed through the connector, which is exactly what matters for accountability and investigation.
- **Undo becomes a list, not a promise.** For every change the twin holds the before and the after, so it can write the inverse call, and name plainly the things nobody can undo, such as an email that has been delivered.
- **It changes the agent's behaviour policy.** "We cannot undo it" stops being an unknown and becomes a named list, and the mandate can be written against that list.
- **Nothing here needs new technology.** Vault append lanes, client-side encryption and vault apps that rebuild views all exist. The one thing that needs more thought is when the journal gets processed, and that needs real users more than it needs design.
- **It is published twice.** This article makes the case. [Connector Twin](https://sgit.ai/demos/vaults/connector-twin/index.md) is a vault with a working replay of an invented session and a business plan for somebody to build the service.

## The question nobody can answer yet

Ask anyone who has switched on an assistant's Gmail or Calendar connector a simple question: do you know what it did last Tuesday?

The honest answer is usually the agent's own summary. It said it tidied the inbox and sorted out next week. Perhaps the chat was kept. Perhaps not. The inbox has moved on since, and the calendar shows the result of the changes, not the changes. If something went wrong, the first person to notice is often the one on the other end: the supplier who received a cancellation, the client whose reply never came.

That is not a criticism of agents. It is what happens when a system that can act is deployed without a record of its actions. We would not accept it for a person with delegated access to a finance system, and we would not accept it for a script with production credentials. We are accepting it for agents because the connector made the grant feel like a feature.

## What the platform keeps, stated precisely

It matters to be exact here, because the case is made by facts, not by fear. This is what Google documents for Gmail and Calendar, checked on 24 September 2026.

| Action | What Google documents | Source |
|---|---|---|
| Move a message to trash | Kept for 30 days: "After 30 days: The message is permanently deleted. You can't recover the message." | [Gmail Help](https://support.google.com/mail/answer/7401) |
| Delete a message through the API | "Immediately and permanently deletes the specified message. This operation cannot be undone. Prefer messages.trash instead." | [Gmail API](https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/delete) |
| Recover permanently deleted email | An administrator can restore a date range within 25 days, in bulk. | [Workspace Admin Help](https://knowledge.workspace.google.com/admin/support/troubleshooting/restore-a-users-permanently-deleted-email) |
| Unsend an email | A cancellation period of 5 to 30 seconds, set in Gmail's settings. An API send has no such window. | [Gmail Help](https://support.google.com/mail/answer/2819488) |
| Delete a calendar event | Deleted events stay in the calendar's trash for 30 days. | [Calendar Help](https://support.google.com/calendar/answer/37113) |
| Edit a calendar event | No version history a user can open. Administrators have an audit log recording changes, including some earlier values such as the old title and times. | [Workspace Admin Help](https://knowledge.workspace.google.com/admin/reports/calendar-log-events) |
| Google Vault | Searches Calendar since November 2023, keeping the last revision of each day. "Vault isn't designed to be a backup or archive tool", and "doesn't have any automated recovery tools." | [Vault Help](https://knowledge.workspace.google.com/vault/search/use-vault-to-search-google-calendar), [Vault FAQ](https://knowledge.workspace.google.com/vault/getting-started/google-vault-faq) |

Read the table the other way round and it says this. There is a real undo for some actions, with a deadline. There is a slow, organisation-wide recovery for one, with a shorter deadline. There is a record without a restore for others, available to administrators on some editions. And there is nothing at all for a delivered email, a notification sent to attendees, or a permanent delete once the administrator's window has passed. None of these records holds what the agent was looking at when it acted, or the instruction it was following.

This is not a failing of Google. These are sensible products designed for people clicking buttons, with an undo toast for the mistake you notice immediately. An agent does not notice. It makes forty calls in two minutes and writes a tidy summary.

## Twin, not backup, log or replay

I went back and forth on the word for this, and the choice is worth explaining.

**Backup** is the wrong word, because a backup copies the mailbox. That is a different product, and customers who need it should buy it. **Log** is too small, because a log records that something happened, and what we need is the content of the exchange. **Replay** is the right verb for what you do with it, but not a name for the thing.

**Twin** is right, in the sense we use it on [twins.sgit.ai](https://twins.sgit.ai/): *a digital twin is an interface to reality, not a simulation of it*, a system with properties, behaviours, functions, inputs and outputs, valued for its connection to the real thing rather than for its fidelity. A connector twin narrows that to one place, the boundary between an agent and the system it is allowed to act on. It holds what the agent could do, what it did, and, rebuilt from those, what it saw.

## How it works

Five steps, and each one is something we already run somewhere.

**Capture.** For every connector call, copy the tool call the agent made, the request the connector sent to the platform, and the response it received. Connectors built on the Model Context Protocol exchange JSON-RPC messages, so every call and every result is already a JSON document that can be copied as it passes. When you can, capture the instruction behind the call as well: the user's request, and the agent's own statement of what it did. Never capture the Authorization header or any token. Capture is of content, never of credentials.

**Append.** Write each entry to a vault [append lane](https://sgit.ai/api/append-lanes.md). An append lane is a write-only channel gated by a token the writer holds and nothing else, and its write response is exactly `{"ok": true}`, so the capture point learns nothing about what else is in the lane. The entry is not decrypted, indexed or processed when it arrives. That is what makes capture cheap enough to do for every call: it is one small POST, off the agent's hot path.

**Chain.** Each entry carries the hash of the one before it, so a missing, edited or reordered entry shows to anyone holding the read key.

**Process.** Later, on a schedule, a reader moves entries from pending to processed and folds them into views. This is the one step I think needs more thought. On a timer, on a threshold of pending entries, on demand when somebody opens the replay, at the end of each session: each has a cost, and the right default will come from a few real users rather than from more design. The lane's limits, five megabytes per write and a thousand pending entries per token, are the constraints to design around.

**Replay and revert.** A vault app rebuilds, from the journal alone, the inbox as the agent saw it and the calendar as the agent saw it, at any step. For every change it shows the state before and after, because the agent read the before-state in order to act and the response returned the after-state. From that it writes a revert plan. Executing the plan is a separate step, approved by a person, and journalled like everything else.

Here is the property I like most. **The twin is not a copy of the mailbox.** It holds only what passed through the connector. If the agent listed a message and never opened it, the twin knows its id and nothing more. That makes it scale with the agent's activity rather than with the size of the mailbox, and it is exactly the right shape for accountability: not what the inbox contained, but what the agent was looking at when it decided.

## One session, replayed

To make this concrete we built the replay and published it as a vault. The session is invented, with invented people at invented `.example` addresses, but every call follows the real Gmail and Calendar APIs. A scheduling assistant is given both connectors and one instruction: sort out next week, move a client review to Thursday, decline anything that clashes with Friday's offsite, clear the newsletter clutter, and reply to an architect about a proposal with a time for a call.

It makes seventeen calls in under three minutes, and writes this summary:

Done. Northwind review moved to Thursday 1 October at 10:00. Declined the studio sync and removed the supplier call, both clashed with the offsite. Archived three newsletters and deleted an old reminder. Replied to Sam and booked a call for Wednesday at 15:00.

Every sentence of that is true. Now look at the calendar as the twin rebuilds it.

The calendar as the agent saw it and left it, rebuilt from the journal. The review is moved, with a ghost of where it was. The sync is declined. The supplier call is not declined but deleted, and because the agent passed sendUpdates=all, the supplier received a cancellation.

"Removed the supplier call" was a delete of an event the user organised, with notifications on, so the supplier received a cancellation. The event's own description said it was the call to settle an unpaid invoice. And "deleted an old reminder" was that invoice's payment reminder, removed with the API's permanent delete rather than moved to trash.

Step 15, before and after. The payment reminder is gone from Gmail, permanently, by the platform's own description. The twin still holds the full message, because the agent read it before deleting it, so its content can be put back with messages.insert, as a new message.

Neither of those is a dramatic failure. Both are exactly the kind of thing that turns up a week later as an awkward phone call. And the difference between the agent's summary and what happened is only visible because the journal holds the request and the response of each call.

What the agent said, against what the journal shows, and whether each part can be put back.

## Undo is a list, not a promise

With the journal in hand, every change gets a grade. This is the list for the session above, and it generalises.

| Action | Can the twin put it back? | What it cannot undo |
|---|---|---|
| Archive, relabel | Yes, exactly | Nothing |
| Move to trash | Yes, exactly, within 30 days | Nothing |
| Move or edit an event | Yes, exactly, from the captured before-state | The notifications already sent, and a second round when it is moved back |
| Decline an invitation | Yes, exactly | The organiser saw the decline |
| Delete an event | The event, re-inserted from the captured copy | The cancellation already sent |
| Permanently delete a message | Its content, as a new message, if the agent read it in full | The original message and its id |
| Send an email | No | The recipient has it |

The value of the list is not that most of it is green. It is that the red rows are named. Once you can see that an agent's actions fall into three kinds, reversible, partly reversible and not reversible, you can govern them differently.

## Where the capture runs

Three places to capture, and three grades of evidence. The mode does not change what is captured. It changes what the evidence is allowed to claim.

Ideally the capture runs in a **broker** that holds the credentials and makes every call on the agent's behalf, which is the [execution broker](https://twins.sgit.ai/broker/index.html) described on the twins site. Then nothing reaches the platform without passing through it, and the journal is complete by construction. The broker can also refuse, which matters for the next section. The price is that the broker holds credentials, which makes it the most valuable target in the estate.

A **gateway** on the MCP or HTTP path is easier to deploy and complete for everything routed through it, and blind to anything that goes around it.

And today, with no infrastructure at all, you can make it a **requirement of the agent**: every time you send a request, append a copy of what you sent and what you received to this lane, and stop if the append fails. It is all JSON already. This is the weakest mode, because an agent that skips an entry leaves a gap the chain cannot show, and the evidence should say *self-reported* on its first line. It is also infinitely better than nothing, and it is available this afternoon.

## What it does to the agent's behaviour policy

At [RiskMandate.ai](https://riskmandate.ai/) we write an agent behaviour policy as the record of what an agent can reach, what it was authorised to do, the gap between the two, and who accepts the residual risk. The [Licence to Operate](https://sgit.ai/demos/vaults/licence-to-operate/index.md) vault simulates exactly that for one agent.

The same agent, with the same connectors, has a very different policy with a twin and without one.

|  | Without a twin | With a twin |
|---|---|---|
| What can it do? | The scopes granted | The scopes, and which actions they allow that cannot be undone |
| What did it do? | Its own summary | Every call, request and response, chain-verified |
| What did it see? | Nothing | The inbox and calendar at each step |
| Why? | Nothing, unless the chat was kept | The instruction behind each call |
| Can you undo it? | Trash windows, sometimes | A revert plan, and a named list of what cannot be undone |
| Can you show someone else? | Your word | An evidence chain an auditor or insurer can open |

The last row is the one that changes the conversation with an insurer or a board. But the most useful change is quieter. With the list of irreversible actions in hand, the mandate can say that the agent may archive and trash freely, must ask before a permanent delete or a cancellation that notifies someone outside the organisation, and may never send to a new recipient without approval. In broker mode, the broker enforces it. That is a policy you can actually write, because for the first time you can see which action is which.

So the question I would ask of any agent deployment is the simple one: **do you know what your agents did?** If the answer is the agent's own summary, the deployment has a gap, and the gap has a known shape.

## What exists today, and what does not

**Exists and runs:** vault [append lanes](https://sgit.ai/api/append-lanes.md), write-only and blind to the sender; client-side encryption, so the journal, which holds copies of email, is stored as ciphertext the host cannot read; vault apps that rebuild views from data in the vault; and the replay in the [Connector Twin vault](https://sgit.ai/demos/vaults/connector-twin/index.md), which folds an invented seventeen-entry journal into the inbox and the calendar, shows before and after, writes a revert plan, and verifies the hash chain in your browser.

**Does not exist yet:** a gateway or broker capturing real Gmail and Calendar traffic; the processor and its schedule; revert execution; any customer. Keys matter too: a twin holds sensitive content, so who holds its keys is the first question a security team will ask, which is part of why we published [a call for collaboration on vault key management](https://sgit.ai/partnerships/vault-key-management.md).

## For somebody to build

I think this should be a business, and I have written it up as one, for somebody else to run or to run with us. The [Connector Twin vault](https://sgit.ai/demos/vaults/connector-twin/index.md) holds the plan: the facts with their sources, the architecture, the service in three capture modes, packages and prices as hypotheses, a calculator, go-to-market starting with managed service providers and insurers, the first ninety days, the risks, and the open questions. It sits with the other [business plans published for founders](https://sgit.ai/startups/business-plans.md).

The pitch is one line long, and it is not fear. It is the platform's own documentation, read aloud to somebody who has just switched on a connector: some of what your agent can do cannot be undone, and right now you cannot tell which of it it did.

## Sources

- [Gmail API, users.messages.delete](https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/delete)
- [Gmail API, users.messages.insert](https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/insert)
- [Gmail Help, delete or recover deleted messages](https://support.google.com/mail/answer/7401)
- [Gmail Help, send or unsend messages](https://support.google.com/mail/answer/2819488)
- [Workspace Admin Help, restore a user's permanently deleted email](https://knowledge.workspace.google.com/admin/support/troubleshooting/restore-a-users-permanently-deleted-email)
- [Calendar Help, delete an event](https://support.google.com/calendar/answer/37113)
- [Workspace Admin Help, Calendar log events](https://knowledge.workspace.google.com/admin/reports/calendar-log-events)
- [Vault Help, search Google Calendar](https://knowledge.workspace.google.com/vault/search/use-vault-to-search-google-calendar)
- [Vault FAQ](https://knowledge.workspace.google.com/vault/getting-started/google-vault-faq)
- [Workspace Updates, Google Vault now supports Google Calendar](https://workspaceupdates.googleblog.com/2023/11/Google-Vault-Now-Supports-Google-Calendar.html)
- [Model Context Protocol specification](https://modelcontextprotocol.io/specification)
- [sgit.ai, append lanes](https://sgit.ai/api/append-lanes.html)
- [twins.sgit.ai, the execution broker](https://twins.sgit.ai/broker/index.html)

*© 2026 Dinis Cruz. This article's own text is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). You're free to share and adapt it, as long as you give credit. Quoted material and linked sources keep their own licences.*

## Threads

Agents & policyVaults & method[This article as a graph →](graphs.md#connector-twin-before-you-deploy-an-agent)

### Continued by

- [Move the cloud, not the code: twins, sovereignty that works in practice, and the migration that pays for itself on the day you switch](move-the-cloud-not-the-code.md) Workloads stay on hyperscalers because moving means changing code; a twin lets the code not know, and the value in the twin is what signs the migration.
- [Agentic cost is an engineering problem: a business plan for a service that reads the logs a company already has and finds the money, then the engineering](agentic-cost-is-an-engineering-problem.md) A business plan: read the logs a company already has, draw each agent's footprint, twin and policy, and find the money first and the engineering second.
- [Where the platform draws the line: Microsoft Execution Containers, the shared responsibility model for agents, and the business logic above it](where-the-platform-draws-the-line.md) Microsoft's MXC and ACS, briefed field by field and mapped to Agent Behaviour Policies: the platform bounds what it can see; the business logic is above.
- [The same argument, in our words: Satya Nadella on models as insider risks, translated into the language of RiskMandate](the-same-argument-in-our-words.md) Satya Nadella's case for treating models as insider risks, translated idea by idea into our vocabulary: reach, mandate, gap, barriers and accepted risk.
- [Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan](authority-outside-the-model.md) Satya Nadella's seven principles for models as insider risks, answered one by one: what we run, what is design, and the five things the list leaves out.
- [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](riskmandate-ten-questions.md) Ten hard questions from a conference, answered in a two-hour interview: what RiskMandate does, what it deliberately is not, and how mature each part is.
- [Where is the why? A permission prompt asked me to decide, and kept the reason](where-is-the-why.md) A prompt asked for a decision and kept the reason. Read through the policy, the law on uninformed consent, and the fixes that worked: put the why in the prompt.
- [The Mandate Stack: a multi-agent system in production, layer by layer](the-mandate-stack.md) A multi-agent system that runs a business every few hours: eight layers, one written mandate per agent, everything a graph, one human who sends.
- [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](the-agent-team-as-it-runs.md) Twelve agents on dedicated accounts, encrypted vaults as the only memory, messages as files, a folder per person, and a mailbox nobody sends from.
- [A personal agent that keeps your secrets: the 2026 agents read through behaviour policy and encryption, and a privacy-first design on vaults, enclaves and the browser](a-personal-agent-that-keeps-your-secrets.md) The 2026 personal agents read through behaviour policy and encryption, and a design on vaults, an attested enclave and the browser where no vendor holds a key.
- [Send an agent, not a spreadsheet: the next generation of software due diligence, and why the companies that stopped reading their code are about to be asked about it](send-an-agent-not-a-spreadsheet.md) Due diligence never scaled because it was a form; a buyer can now send an agent into a vendor's environment and read what the code and the practices are.
- [If somebody built a company on code review: how I would do it, and why it is only now possible](if-somebody-built-a-company-on-code-review.md) A reader's seven questions answered as a company plan: one reader for every layer, review as a science, and the layers as the customer's own.
- [Replicating the agentic inbox: a walkthrough from one Claude session to a team of agents that never press send](replicating-the-agentic-inbox.md) How to copy a working agentic email setup in phases: a mailbox and Claude seat of the agent's own, one session with a policy, then roles talking in files.
- [Footprint and blast radius: what the agent actually did, and what it would have cost](footprint-and-blast-radius.md) Footprint is what an agent actually did, read afterwards from logs and vault history; blast radius is what a row of its reach would cost the business today.
- [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](custom-uis-are-not-the-exception.md) Every message has a graph, so it can be shaped for the reader's moment; a custom interface per moment is now how interfaces get made, and each gets a policy.
- [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](ultimate-insider-three-collisions.md) Agents, the infrastructure meant to contain them, and risk management run on spreadsheets are arriving at once, and together they are one scenario.
- [Six agents, one inbox: what a real multi-agent setup taught me about access policies](six-agents-one-inbox.md) An access policy for an agent is only as real as its worst row: every rule in a real six-agent setup, graded by how it is enforced today.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 12 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=12)

## From the desk

- [Behaviour policy in practice](collections/behaviour-policy-in-practice.md) collection, 11 articles

**Posting this article on LinkedIn?** The cover is [connector-twin-before-you-deploy-an-agent.jpg](banners/connector-twin-before-you-deploy-an-agent.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/connector-twin-before-you-deploy-an-agent.html)*
