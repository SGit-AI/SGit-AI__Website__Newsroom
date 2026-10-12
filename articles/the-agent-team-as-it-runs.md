# The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from, sgit.ai

> The walkthrough told you how to build the agentic inbox in phases. This is the stack as it runs today, written up from the agents' own field notes so that it can be referenced and copied: twelve Claude agents on dedicated accounts, each with one focus and a behaviour policy; encrypted vaults the host cannot read, driven by sgit, as the only memory; messages between agents as files in each other's mailroom; a CRM that is one folder per person with provenance on every fact and a hash on every message; a conductor that runs the team four times a day with a security role first and last; and a mailbox the agents draft in but never send from. It then does two things the field notes did not. It names the security and privacy properties as properties, client-side encryption with keys handed out of band, read keys that cannot write, a leak check before every commit, rotation by new vault, a record that is read afterwards against the policy, and a three-way distinction between public, private-ish and personal information in which the team's vaults are built to hold the first two and refuse the third, with rules that can be scoped per customer and written to protect the person on the other end. And it maps every piece of the setup to the idea on this site that it implements, vaults, behaviour policies, fractal semantic graphs, memory as files, so that nothing in it has to be taken on trust. It ends on the question the setup leaves open, who gives the mandate over information, which gets a document of its own.

*Source: <https://newsroom.sgit.ai/articles/the-agent-team-as-it-runs.html> · sgit.ai v0.7.79 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from

# The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-06 · updated 2026-10-06 · [article v1.0.1, 2 versions](versions/the-agent-team-as-it-runs.md) · [sgit.ai v0.6.76](https://sgit.ai/admin/versions.md) · agentsagent-behaviour-policyriskmandatevaultssgitemail-fscrmprovenanceencryptionprivacydata-classesfractal-semantic-graphsclaudegoogle-workspacearticle

***Abstract:** The walkthrough told you how to build the agentic inbox in phases. This is the stack as it runs today, written up from the agents' own field notes so that it can be referenced and copied: twelve Claude agents on dedicated accounts, each with one focus and a behaviour policy; encrypted vaults the host cannot read, driven by sgit, as the only memory; messages between agents as files in each other's mailroom; a CRM that is one folder per person with provenance on every fact and a hash on every message; a conductor that runs the team four times a day with a security role first and last; and a mailbox the agents draft in but never send from. It then does two things the field notes did not. It names the security and privacy properties as properties, client-side encryption with keys handed out of band, read keys that cannot write, a leak check before every commit, rotation by new vault, a record that is read afterwards against the policy, and a three-way distinction between public, private-ish and personal information in which the team's vaults are built to hold the first two and refuse the third, with rules that can be scoped per customer and written to protect the person on the other end. And it maps every piece of the setup to the idea on this site that it implements, vaults, behaviour policies, fractal semantic graphs, memory as files, so that nothing in it has to be taken on trust. It ends on the question the setup leaves open, who gives the mandate over information, which gets a document of its own.*

The whole stack in one line: a phone, twelve sessions, encrypted vaults, a Drafts folder, and people. Below the line, the four properties that make it safe to copy. Infographic from the team's field notes of 6 October 2026; no live data.

**What this is.** The description of a setup that is running, as the agents who run it wrote it down on 6 October 2026, with the pieces they left out added back: why each part is the shape it is, which earlier article argued for it, and what it protects against. It is written to be referenced by somebody setting up the same thing. The step-by-step version is [Replicating the agentic inbox](replicating-the-agentic-inbox.md); the argument about policy rows is [Six agents, one inbox](six-agents-one-inbox.md). This page sits between them: the system, its properties, and its honest gaps. It says nothing about other people's agents. That comparison, and a design for a personal agent built on these properties, is [the next article](a-personal-agent-that-keeps-your-secrets.md).

## In short

- **Twelve agents, one focus each, and one thing none of them can do.** Every agent is a Claude session on a dedicated account with a written brief and an Agent Behaviour Policy it reads before it works. Eleven of the twelve policies forbid the same thing: sending.
- **The only memory is encrypted vaults.** Collaboration, CRM and LinkedIn are each a vault, driven by the sgit command line. Files are encrypted on the agent's side before they leave; the host stores ciphertext and never holds a key. Keys are given to each session out of band and are never written into a file.
- **Agents talk in files.** A message between agents is an email file dropped into the recipient's mailroom folder in the shared vault. The recipient moves it to its inbox, acts, and files it as done. Nothing calls anything.
- **Memory is one folder per person.** The CRM is plain JSON and Markdown: a record, an append-only ledger, every message word for word with provenance and a hash, meeting notes, a graph of interests against what has been made that meets them, and a generated summary nobody edits by hand.
- **A conductor runs the team four times a day**, one step per agent of up to twelve minutes, with a security role first and last. A run that dies leaves a lock, and the next run notices.
- **The properties are the point.** Identity and encryption are strong barriers by construction. The record detects. The policy text is weak and the setup says so. The vaults are built to hold public and private-ish information and to refuse personal information, and the rules can be scoped to one customer or written to protect the person on the other end of the email.
- **Nothing here is new to this site.** Every piece implements an idea already argued for: dedicated accounts, behaviour policies, vaults the host cannot read, messages as files, fractal graphs, memory with provenance, the footprint read afterwards. This page maps each piece to its argument.

## The picture

The person talks to the agents from a phone: voice notes, screenshots, chat, and decisions as one tap on a card. The agents work in their own cloud sessions. They keep everything as files in vaults they encrypt before anything leaves, and they leave email as drafts in a mailbox of their own. The person reads the drafts and presses send. Replies come back to the same mailbox and are captured into the CRM with provenance and a hash. A conductor runs every agent once, four times a day, and writes a debrief.

| On 6 October 2026 |  |
|---|---|
| Agents | 12 |
| Scheduled runs | 4 a day on weekdays |
| People in the CRM | 71 |
| Emails an agent sent on its own | 0 |

That last row is the one the whole design is organised around.

## Accounts: the account is the blast radius

Nothing the agents use belongs to the person. Each identity is separate, so a mistake stays inside one account.

- **A dedicated Google Workspace** for the company, with a mailbox for the agents on the company's domain. The agents never touch the person's own inbox, which has years of history in it; theirs was empty on day one and holds only what people have since sent to it.
- **A dedicated Claude Team account.** Each agent is a session in it, with only the connectors it needs. The connectors are enabled by the organisation owner and connected by the agent's account, so the grants live there and nowhere else.
- **Encrypted vaults** on the SG/Send platform, driven by sgit. Files are encrypted on the agent's side before they leave, and the server only holds ciphertext. The keys are handed to each session by the person, out of band, and never written into a file.
- **A separate personal agent** for the person's private life, on the person's own domain, with its own mailbox, lane and vault. Personal matters do not enter the team vault.
Four separate identities, and the boundaries between them that hold by construction. A session running as one account cannot reach what another holds; a vault key handed to one session does not open another vault. The strongest barriers in the setup cost a few pounds a month each. Fictional detail; no address beyond the agents' published one.

This is the first control because it is the one that does not depend on anyone behaving. A policy can ask an agent not to look; an account boundary means there is nothing there to see. [Six agents, one inbox](six-agents-one-inbox.md) is the long version, including what a Workspace administrator can lock per organisational unit once each agent is a unit of its own.

## The agents

Each agent is a role with one focus, a written brief, and an Agent Behaviour Policy. The names are short and lowercase; the detail is in each policy.

| Agent | Focus | Cannot |
|---|---|---|
| @inbox | Everything coming in: triage, summaries, labels, filing replies into the CRM | send |
| @drafts | Everything going out, as Gmail drafts, from a registered email file | send; change what an email says |
| @crm | Contacts, campaigns, the email register, relationship decisions | send |
| @briefs | Research, dossiers, email text, meeting briefs and debriefs | send; touch Zapier |
| @abp | The policy vocabulary and each agent's policy | send; publish |
| @dev | Tools, the vault UI, the postmaster, the run setup | send |
| @security | Checks first and last in every run; reports, never fixes | send, except one hold email |
| @conductor | The scheduled run: one step per agent, a debrief at the end | change scheduled tasks |
| @webSummit | Event planning: who, when, why | send; book |
| @zapier | An experimental channel (WhatsApp, Discord) through Zapier | go live without approval |
| @linkedin | LinkedIn conversations, in a vault of their own | post |
| @newsroom | A sibling site's team, working from outside this one | read this team's vault |

The roster on 6 October 2026, grouped by what each role touches: the mailbox, the memory, the running of the team, the world outside. The last column is the row that does the work, and it is the same word in eleven of twelve rows.

The split into roles is not neatness. Each role gets a policy short enough to check, and the policies differ in the one place that matters: who touches the mailbox, and how. Every account has the same reach to the mailbox. One role reads it, one role writes drafts into it, and none sends from it.

## How they talk: email, but as files

Agents do not call each other. They write messages as `.eml` files into each other's mailroom folder inside the shared vault, a convention the team calls Email-FS lite. The recipient moves a message to its inbox, acts, and files it as done. Every message has a sender, a recipient, a kind (request, update, notice) and references to the files it is about.

```

mail/
  mailroom/<agent>/NNN-subject.eml   new, unread; anyone may add
  <agent>/inbox/  done/  outbox/      each agent's own folders
  <agent>/ABP.md                      its policy, read before work
  <agent>/issues/open/ …              its task list
conductor/agents.json                 the run order
runs/index.jsonl                      every run, with each step's outcome
security/findings.jsonl               what the checks found

```

Email as the message format is deliberate. Any mail tool and any agent can read it; a thread has references built in; and a person can open the folder and understand what was asked without learning a schema. The vault keeps every version, so the conversation between the agents is a record from the first message, and it can be read later with a read key by someone who holds no write credential. The shape is the one described in [append-lane messaging](https://sgit.ai/docs/append-lane-messaging.md), and [Agent Contact](https://sgit.ai/docs/agent-contact.md) is the same idea between sites rather than within a team.

**The conductor** runs the team four times a day on weekdays. Security opens; then drafts, inbox, briefs, CRM, events, ABP and dev each get one step of up to twelve minutes; then security closes. Each step is a sub-agent that reads its state, does one kind of work, writes its state, and stops. Late mail waits for the next run. Nothing loops. A run that dies leaves a lock, and the next run notices and says so.

### One agent's session, start to end

1. **Check for a security hold.** If one is open, stop before anything else.
2. **Open a change snapshot**, so the team can see what this session changed.
3. **Pull the vaults** with sgit. Always commit before pulling: the team reports that a pull overwrites uncommitted edits in the local working tree, which two agents learned by losing work. The two-branch model's guarantee is about other agents' committed work, which a pull cannot clobber; the local uncommitted tree is a different matter, and the behaviour is reported by the team here rather than yet filed against the CLI.
4. **Deliver the mailroom**, read the messages, do the work. Write only in your own folders and new mailroom files.
5. **Run the leak check** before every commit. No key, token or password may be in any file.
6. **Commit, pull, push**, one commit per cycle.
7. **End with a card.** A script reads the session transcript afterwards and counts tools, tokens, files and network calls, then flags anything outside the agent's policy. The snapshot is closed with the card attached.
Left: the mailroom convention and a message as a file. Right: the seven steps of a session and the card that ends it. Along the bottom, the four rules that are never negotiated. Fictional paths and counts.

The card is the footprint, measured after the fact from the record, which is what [Footprint and blast radius](footprint-and-blast-radius.md) proposed. The first one the team ran flagged two writes as outside the mandate; on inspection the policy allowed them and the script had misread it. Both findings were useful, and both are in the record.

## The CRM: memory is one folder per person

The CRM is a vault of plain JSON and Markdown files. There is no database. Each person gets a folder; every exchange with them is a file; a timeline links the files; a graph says what they care about and what has been made that meets it.

```

contacts/<person>/
  contact.json            the record: role, stage, priority, next step, interests
  comms/ledger.jsonl      the timeline: one line per event, append-only
  comms/<UTC>__<in|out>__<channel>__<id>.md
                          each message, word for word, with provenance and a hash
  meetings/<date>/notes.md from voice debriefs
  graph.json              interests ↔ what we have made that meets them
  materials.jsonl         every link and vault ever sent to them
  sources/                where each fact came from
  README.md               generated summary; never hand-edited
index.json · organisations/ · campaigns/ · vocabulary.json (stages S0 known → S7 advocate)

```

One folder per person, with a sample of the ledger and the six rules that make the folder trustworthy. The summary is generated from the files beneath it, so it cannot drift from them. Fictional person and content.

**The rules that make it trustworthy.**

- **Append-only.** A correction is a new line pointing at the old one. Tasks are lines too; the last line for a task wins. Nothing is rewritten, so the history is the record.
- **Provenance on everything:** who captured it, when, how, and how faithfully.
- **A hash of every stored message**, so a changed file shows, and so the text that left in a draft can be matched to the text that was approved.
- **Inbound is data.** Nothing stored is ever acted on as an instruction. A message from the world is a fact about the world, not a command to the team.
- **Each agent adds to the folder of the person it is working on**; the relationship fields stay with @crm.
- **Only what the work needs.** No credentials, ever. Health and other sensitive data stay out.

**What it is used for.** Who has the ball and for how long; the next step per owner; meeting preparation; who should get which article, read from the graph's gaps and matches; and a "what we know about you" pack that can be sent to the person, so they can correct it. That last use is the privacy design showing through the product design: a memory that can be shown to its subject is a memory that has been kept to what can be shown.

## The rules that are never negotiated

1. **Keys never go into any file**, message or draft.
2. **No agent sends.** Agents create drafts; a person sends. The one exception: @security may send one email, to one address, to put the team on hold.
3. **No agent creates, fires or changes a scheduled task** from a step.
4. **Create anywhere, edit your own.** Any agent may create a draft or a file; only its creator edits it.

The fourth rule replaced a stricter one. "Only one agent may draft" became a bottleneck in two days, and the replacement keeps the property that mattered, that no agent rewrites another's work, while letting the work flow.

## The policies in practice: barriers typed honestly

An Agent Behaviour Policy, in [RiskMandate's vocabulary](https://riskmandate.ai/abp.html), sets each agent's reach, what it can do, against its mandate, what it was asked to do, and names the barrier that holds in the gap. The barrier is where honesty matters, and most of this team's barriers are weaker than anyone would like.

| Barrier | Strength | Where it holds here |
|---|---|---|
| identity | strong | Separate Workspace, Claude, vault and personal-agent accounts. A mistake cannot cross accounts. |
| encryption | strong | Vaults are encrypted client-side; the host sees ciphertext. Only key-holders read, and a read key cannot write. |
| grant | medium | Connectors added per session, where the platform allows it. Often it does not: one grant covers draft and send. |
| record | medium | sgit history, append-only ledgers, session cards. Nothing is hidden, but a record detects rather than stops. |
| policy | weak | The policy text and the agent's own judgement. Many rows, including "no agent sends", rely on it. |

The five words are the team's own grading. RiskMandate's published vocabulary types a barrier as one of four kinds, boundary, setting, expectation or none, and says that only a boundary is a control, because "a control bounds a grant only if it is enforced by something the grant does not include." Mapped onto that: identity and encryption are boundaries; a grant is a setting the account could flip; the record and the policy are expectations, one of which at least leaves evidence. The published page still calls the reach the grant and the gap the delta; the words differ, the structure does not.

The five barriers graded, and the six things the policies caught or showed in the first weeks. Reading the table top to bottom: what touches identity and keys is enforced; what touches mail is a prompt, a setting or a hope.

**What the policies caught, or showed.**

- **A connector appeared mid-session**, giving reach to thousands of apps through Zapier. Three agents flagged it as outside their policy before using it.
- **Calendar invites have no draft state.** An agent that can create an event can invite anyone, at once. "A person sends" cannot be written for calendars, so whoever grants the calendar accepts that risk, and the policy now says so.
- **A discarded Gmail draft is gone**, with no log the agent can read. The record has a hole where the platform has one.
- **Gmail drafts strip images.** The workaround on offer was to send pictures through Zapier: a 9,000-app reach to send one picture. Workarounds are where permissions grow, and this one was refused.
- **Mistakes get recorded too.** One agent made an accidental calendar call. It failed and nothing was sent, and the agent logged the attempt against its own policy.

The honest column is the one that says *policy*. Those rows are where the next incident comes from and where the next piece of tooling goes, which is why [Every risk is already accepted](every-risk-is-already-accepted.md) insists the policy say who accepted each gap and for how long.

## The security properties, as properties

The field notes describe mechanisms. It is worth restating them as properties, each with what it protects against, because that is the form in which somebody else can check whether their copy has them.

| Property | Mechanism | What it protects against |
|---|---|---|
| The host cannot read the memory | Every file, filename, commit message and branch name is encrypted on the agent's side before it leaves: AES-256-GCM with per-file keys derived by HKDF-SHA256, the key hierarchy rooted in a vault key that never travels to the server. The same primitives run in the browser, byte for byte, under a versioned contract with test vectors. | A breach, a subpoena or an insider at the host yields ciphertext. What the host does see, and the [security model page](https://sgit.ai/security/index.md) says so, is the vault id, object sizes, timing and volume. |
| A reader cannot write | A read key is derived one way from the vault key and cannot be turned back into it. Readers get read keys. | A leaked read key caps the damage at disclosure of what that vault holds. |
| A writer can be given only a slot | An append lane is a write-only token: the holder can add a message and cannot read, list or change anything. | A form on a public page or a sibling team can report in without being able to read the record. |
| Keys never touch a file | Keys are handed to each session out of band; the leak check refuses any commit containing a key shape, including other people's; the security role scans for them first and last in every run. | The commonest leak, a key in a log or a capture. |
| A leaked write key means a new vault | History holds what redaction removes, so rotation is a fresh vault seeded from the current files, the old one frozen. | The false comfort of a redacted file whose history still holds the secret. |
| The account is the blast radius | Dedicated Workspace, Claude and personal-agent accounts; vault keys per session. | A compromised or confused agent reaches one account's worth of things. |
| No agent sends | Drafts only, with the hash of each draft on record; one named exception with one recipient and a hold behind it. | An agent, or whoever is driving it through a poisoned message, speaking for the person. |
| The team can be stopped | The hold file: while it is open, the conductor refuses to open a run, every step refuses to start, and every interface shows it. Only a person releases it. | An incident that outruns the people. |
| Inbound is data | Nothing stored is acted on as an instruction. | Prompt injection through the mailbox or a connected document. |
| Everything is read afterwards | sgit history, append-only ledgers, the session card against the policy. | Not knowing what happened; the near miss going unrecorded. |

Two of these are stronger than they look and two are weaker. The host's blindness is a property of the mathematics, not of a promise, and it holds against the host's own staff. The one-way read key is the reason the team can publish read keys on purpose. The leak check and the hold are only as good as the scripts that run them, which is why the tool that checks the team is held to the team's own standard, in the way [the review brief](https://sgit.ai/docs/briefs/code-review-graphs-in-the-repository.md) asks for. And "no agent sends" is, on today's platform, a prompt and a policy rather than a block, which the barriers table above says plainly.

Three limits the platform's own [limitations page](https://sgit.ai/docs/limitations.md) states, and which apply to this team: commit authorship is not yet signed, so in a shared vault an agent's identity comes from its branch rather than a signature; there is no key revocation, so rotating a read key protects future commits and not the objects someone already fetched; and the lane that would let two vaults message each other without a person in between is not wired end to end, which is why that row appears under what is not working.

## The privacy properties: three classes of information

The second thing the field notes did not say in so many words is the distinction the setup runs on. Information is handled in three classes, and the class decides where it may live.

Public, private-ish, personal. The team's vaults are built to hold the first two and refuse the third, and the rules can be scoped per customer or written to protect the person on the other end. The question in the black bar gets its own document.

**Public** is what the person or the organisation has already published, or would publish without a second thought: articles, talks, published vaults and their read keys, public profiles and roles, what has been made and sent to people. It may live in any team vault, on the sites, in the CRM's materials and graph.

**Private-ish** is the working record of a professional relationship: not secret, not for broadcast. Correspondence sent to the agents' mailbox, the stage and next step, who has the ball, meeting notes from voice debriefs. It lives in the CRM vault, one folder per person, with provenance and a hash, readable only by key-holders, and correctable by the person through the "what we know about you" pack.

**Personal** is health, family, finances, private life: anything confidential enough that a leak would hurt the person rather than embarrass the team. It is not captured, even when it arrives in a message. Credentials of any kind are never stored. Personal matters belong to the separate personal agent, on the other side of the account wall. The policy says so, the security role's checks look for it, and the recipient's privacy outranks the team's completeness.

Most of what a company agent handles is public or nearly so. Holding to that is what bounds the worst case before any encryption is counted: the worst a leaked read key to the CRM vault could disclose is the working record of professional relationships, and nothing that would hurt the people in it.

Two things follow from the way the setup is built, and both are available to anyone who copies it.

**Rules can be per customer.** Because the policy is a file per agent and the memory is a folder per person, a rule can be scoped to one relationship: what may be kept about this organisation, who on the team may read it, what must never be summarised onward, how long it is held. A customer who asks for a tighter rule gets a line in a file, not a product roadmap.

**Rules can protect the recipient.** The same mechanism writes rules in the other direction: what the person on the other end of the email would expect, rather than what the team would find useful. "Capture only what the work needs" is a rule about their privacy, enforced on our side. So is "inbound is data". So is the pack that shows them what is held.

## The logic: files, graphs and a state machine

Why is it this shape? Three ideas, each argued for earlier on this site, and the setup is what they look like when run together.

**Files, not a database.** Every piece of state is a file in a vault: a message, a policy, a ledger line, a run record, a finding. Files can be encrypted one at a time, versioned, diffed, read with a read key, hashed, and understood by a person with no tooling. A database would have given the team one query language and taken away all of that. The interfaces the team built on top, a card for the phone, a board of who is waiting on whom, were each built in an afternoon because the data was already files, which is the argument of [Custom UIs are not the exception](custom-uis-are-not-the-exception.md).

**Graphs inside graphs.** The CRM's `graph.json` is a small [fractal semantic graph](introducing-fractal-semantic-graphs.md): a person's interests as nodes, the things made that meet them as nodes, and typed edges between them, so that "who should get this article" is a query and not a memory. Zoom out and the same grammar describes the team: agents, the files they own, the messages between them, the policies that bind them. Zoom in and a message's references are edges to the files it is about. One grammar at every level is what lets one set of tools and one set of checks serve all of them, and it is why the memory can be shown to the person it is about: a graph with provenance on every node is a graph that can be audited by its subject. [Memory is not a spectator sport](memory-is-not-a-spectator-sport.md) is the argument for memory as files with provenance built in; the CRM is that argument with 71 folders.

**Claude as a state machine.** Each role reads its state from files, does one kind of work, writes its state back as files, and stops. It does not converse; it runs a step. This is what makes the conductor possible, and it is what makes the footprint readable: a step that reads and writes files leaves exactly the record its files are. The walkthrough article introduced the idea; the conductor is the idea on a schedule.

Every piece of the setup, and the writing on this site that argued for it, in four colours: policy and control, vaults and keys, graphs and memory, record and interfaces. Nothing in the setup has to be taken on trust; each piece has an argument and the argument has a page.

## Build your own: the first week

1. **Accounts.** A separate Workspace mailbox for your agent, a separate Claude account, and one vault. Never connect your own inbox.
2. **One agent, one policy.** An inbox agent that reads, labels and drafts. Write its policy before you connect anything: reach, mandate, gap, barriers, with the barriers typed honestly.
3. **Your memory.** A folder per person for your first twenty people, then a ledger line for every email, call and meeting. Decide now which class of information you will not hold.
4. **Voice debriefs.** Two minutes after each call; your agent turns them into notes and tasks.
5. **Then split roles**, inbox, drafts, CRM, and let them talk through files as above. Add a schedule last, and a security role before the schedule.

The detailed phases, with the Workspace and Claude Team settings that cost time, are in [Replicating the agentic inbox](replicating-the-agentic-inbox.md). For the policy itself, [RiskMandate.ai](https://riskmandate.ai/) has the vocabulary and a workshop that writes a first one in a few minutes.

## What is not working yet

The field notes end with this list and so does this article, because a description of a running system that leaves it out is a brochure.

- **Two registers disagree** on how many emails have been sent, so the dashboards under-count until the registers are reconciled.
- **Messaging between vaults still needs a person** to paste text, because the encrypted lane between them needs re-keying.
- **One agent, @dev, holds most of the open work**, and much of it needs a live session rather than a scheduled step.
- **There is no daily brief channel to the person.** WhatsApp got the account suspended in testing, and Discord failed twice.
- **Most barriers are policy-only.** The platform does not let the team remove send tools per agent, so "no agent sends" is a prompt and a promise. The property that would make it a block, a separate permission authority that holds the credentials and decides each action, does not exist in this setup yet.

## The question this leaves open

Something a person sent to one of us was sent to a person. It was not sent to a team of agents, and it was not sent to whatever those agents might pass it to next: another agent, a summary, a dashboard, another organisation. The setup's answer so far is to hold less and to say what it holds, which is what the three classes do. It is not an answer to the question underneath, which is who gives the mandate over a piece of information, and whether the recipient of an email has the authority to hand it to an agent at all. That question is bigger than this setup and gets a document of its own. What this page can say is that the mechanisms to enforce whatever the answer turns out to be, a policy per agent, a rule per relationship, provenance on every fact and a memory that can be shown to its subject, are already running.

## Threads woven here

- [Replicating the agentic inbox](replicating-the-agentic-inbox.md): the phases, from one session to the team described here.
- [Six agents, one inbox](six-agents-one-inbox.md): the account as the blast radius, and what an administrator can lock per organisational unit.
- [Footprint and blast radius](footprint-and-blast-radius.md): the session card is this article's footprint, read afterwards against the mandate.
- [Before you give an agent a connector, give the connector a twin](connector-twin-before-you-deploy-an-agent.md): test the reach before writing the mandate; the attachments finding is the case in point.
- [Every risk is already accepted](every-risk-is-already-accepted.md): the weak rows in the barriers table are accepted risks, and the policy should say by whom.
- [Introducing fractal semantic graphs](introducing-fractal-semantic-graphs.md) and [Memory is not a spectator sport](memory-is-not-a-spectator-sport.md): the grammar of the CRM's graph, and memory as files with provenance.
- [The wall under the reply](the-wall-under-the-reply.md): the ledger is the state of a relationship the way the reply tail is the state of a thread.
- [The identity we wanted to give the agents](the-identity-we-wanted-to-give-the-agents.md): why the agents have Workspace identities, and where secrets must not live.
- [Vault credentials](https://sgit.ai/docs/credentials.md), [append-lane messaging](https://sgit.ai/docs/append-lane-messaging.md) and [Agent Contact](https://sgit.ai/docs/agent-contact.md): the key classes, the write-only lane, and messages between agents and sites.
- [Code review graphs in the repository](https://sgit.ai/docs/briefs/code-review-graphs-in-the-repository.md): the tool that checks the team is held to the team's standard.

## Sources

- The team's field notes, *How our agent team works, and how to build your own*, written by the briefs role on 6 October 2026 for Dinis Cruz, from which the roster, the folder layouts, the session steps, the barrier grades, the findings and the list of what is not working are taken. The counts are the notes' counts on that date.
- [RiskMandate.ai, the Agent Behaviour Policy](https://riskmandate.ai/abp.html): reach, mandate, gap, barriers.
- The sgit documentation on this site for the crypto stack and the key classes: [What is sgit](https://sgit.ai/docs/what-is-sgit.md), [Vault credentials](https://sgit.ai/docs/credentials.md), [Limitations](https://sgit.ai/docs/limitations.md).

*Drafted from the team's field notes and a voice memo by Dinis Cruz, who is the author of the argument and the person with editorial responsibility, by agent@riskmandate.ai (Claude Fable 5.1, claude-fable-5-1) in the sgit.ai site session, on 6 October 2026. The figures are infographics drawn from the notes with fictional names, paths and sample content; no contact is named beyond the agents' published address, and no key or token appears in any figure or file.*

*© 2026 Dinis Cruz. This article's own text is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You're free to share and adapt it, as long as you give credit. Quoted material and linked sources keep their own licences.*

## Threads

Agents & policyVaults & method[This article as a graph →](graphs.md#the-agent-team-as-it-runs)

### Builds on

- [Replicating the agentic inbox: a walkthrough from one Claude session to a team of agents that never press send](replicating-the-agentic-inbox.md) How to copy a working agentic email setup in phases: a mailbox and Claude seat of the agent's own, one session with a policy, then roles talking in files.
- [Six agents, one inbox: what a real multi-agent setup taught me about access policies](six-agents-one-inbox.md) An access policy for an agent is only as real as its worst row: every rule in a real six-agent setup, graded by how it is enforced today.
- [A personal agent that keeps your secrets: the 2026 agents read through behaviour policy and encryption, and a privacy-first design on vaults, enclaves and the browser](a-personal-agent-that-keeps-your-secrets.md) The 2026 personal agents read through behaviour policy and encryption, and a design on vaults, an attested enclave and the browser where no vendor holds a key.
- [Footprint and blast radius: what the agent actually did, and what it would have cost](footprint-and-blast-radius.md) Footprint is what an agent actually did, read afterwards from logs and vault history; blast radius is what a row of its reach would cost the business today.
- [Every risk is already accepted. The only question is by whom, and for how long.](every-risk-is-already-accepted.md) A risk exists the moment the exposure does, so somebody is already carrying it; the only questions worth asking are who has accepted it and until when.
- [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](custom-uis-are-not-the-exception.md) Every message has a graph, so it can be shaped for the reader's moment; a custom interface per moment is now how interfaces get made, and each gets a policy.
- [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](introducing-fractal-semantic-graphs.md) A fractal semantic graph has no privileged level and no single schema: each world keeps its own vocabulary and connects to others through named edges.
- [Memory is not a spectator sport: how a web of open sites, graphs and vaults became the memory for sessions like this one](memory-is-not-a-spectator-sport.md) Agentic memory as context management: many published, fractal, provenance-carrying memories rather than one store, shown in the session that wrote the article.
- [Before you give an agent a connector, give the connector a twin](connector-twin-before-you-deploy-an-agent.md) An agent with a Gmail or Calendar connector can do things the platform cannot undo; a journal of every call, replayed, shows what it did and what can go back.
- [The wall under the reply: end an email with the state of the thread, not the thread](the-wall-under-the-reply.md) End an email reply with the state of the thread for this reader, not the quoted wall: decided, open, next, who is on copy, with links to the record.
- [The identity we wanted to give the agents: a week of design, the line in Google's terms, and why login plus secrets is still too hard](the-identity-we-wanted-to-give-the-agents.md) A week of designing identities for agents and users met Google's terms; what survived is a passkey-unlocked keyring and a gap nobody sells.

### Continued by

- [From a spreadsheet to a folder per person: how to run your contacts the way our agents do, with Google Drive, Gmail and the Claude app, before you touch a vault](from-a-spreadsheet-to-a-folder-per-person.md) A walkthrough from a spreadsheet CRM to one Drive folder per person, worked by Claude under a six-line policy, with five exercises, before any vault is needed.
- [Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan](authority-outside-the-model.md) Satya Nadella's seven principles for models as insider risks, answered one by one: what we run, what is design, and the five things the list leaves out.
- [A Mac of the agent's own: a business plan for agent desktops, what Apple's licence allows, and three behaviour policies](a-mac-of-the-agents-own.md) A business plan for a Mac of the agent's own: what Apple's licence allows, a desktop built from vaults per run, and three behaviour policies for one agent.
- [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](riskmandate-ten-questions.md) Ten hard questions from a conference, answered in a two-hour interview: what RiskMandate does, what it deliberately is not, and how mature each part is.
- [How I work with Claude: one session per topic, agents with names, and memory you curate](how-i-work-with-claude.md) A practical guide from a year of daily use: one Claude session per topic, named agents with a role.md, curated memory, vaults, and policy before connectors.
- [Encrypted memory for agents that run somewhere else: sgit deployment patterns, from a Mac mini to Kubernetes](encrypted-memory-for-isolated-agents.md) Agents in isolated, ephemeral places need memory that outlives them. Five sgit deployment patterns, from a Mac mini to Kubernetes, with ciphertext-only servers.
- [Knowing when to stop: what experience gives people, and what we have to design into agents](knowing-when-to-stop.md) Knowing when to stop is the hard part for people and agents: what experience gives people, and the constraints that give agents the same perspective.
- [Agency is not a yes: a scale for human and agent decisions, from rubber stamp to the reviewer who fixes the source](agency-is-not-a-yes.md) A yes or no is not agency: seven dimensions, a seven-level scale for people and agents, and the review as a QA step that fixes the source.
- [Hope or enforcement: one customer service agent, three designs, and who keeps each promise](hope-or-enforcement.md) One customer service agent built three ways, each with an Agent Behaviour Policy: how much of each policy is hope, and what one run can reach.
- [Every mistake added a rule: complexity, agents, and the way back to shipping](every-mistake-added-a-rule.md) When every agent mistake adds a rule, complexity wins: map the process, move each piece right as a small shipped component, and keep the rigour for the work.
- [Where is the why? A permission prompt asked me to decide, and kept the reason](where-is-the-why.md) A prompt asked for a decision and kept the reason. Read through the policy, the law on uninformed consent, and the fixes that worked: put the why in the prompt.
- [The Mandate Stack: a multi-agent system in production, layer by layer](the-mandate-stack.md) A multi-agent system that runs a business every few hours: eight layers, one written mandate per agent, everything a graph, one human who sends.
- [Why my agents do not run on my laptop: chat, Cowork and Code in the cloud, a vault as the shared drive, and the two walls an operating system has](why-my-agents-do-not-run-on-my-laptop.md) An OS has two hard walls, the kernel and the user; an agent on a laptop runs inside the one marked you, so the agents run in the cloud with a vault as shared drive.
- [The deck I could not download: an author-first home for presentations, as a business plan somebody else can build](the-deck-i-could-not-download.md) One download offered as a subscription, an author paid nothing, and a design for the service the author would have chosen: vaults, keys, seven roles, 85% to the author.
- [A personal agent that keeps your secrets: the 2026 agents read through behaviour policy and encryption, and a privacy-first design on vaults, enclaves and the browser](a-personal-agent-that-keeps-your-secrets.md) The 2026 personal agents read through behaviour policy and encryption, and a design on vaults, an attested enclave and the browser where no vendor holds a key.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 32 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=32)

## From the desk

- [The week to 7 October: the agent team, written up from the inside](desk/the-week-to-7-october.md) the week, 2026-10-07
- [Create anywhere, edit your own: a rule learned in the inbox, applied to the newsroom](desk/create-anywhere-edit-your-own.md) thread, 2026-10-07
- [What the human brings](collections/what-the-human-brings.md) collection, 4 articles
- [Behaviour policy in practice](collections/behaviour-policy-in-practice.md) collection, 11 articles

**Posting this article on LinkedIn?** The cover is [the-agent-team-as-it-runs.jpg](banners/the-agent-team-as-it-runs.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-agent-team-as-it-runs.html)*
