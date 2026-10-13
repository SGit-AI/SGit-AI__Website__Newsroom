# The Mandate Stack: a multi-agent system in production, layer by layer, sgit.ai

> RiskMandate runs its business with about fifteen agents and one person, four times a day on a schedule and whenever the person sits down with them, with the person's name on every message that leaves. The agent that runs its CRM wrote the briefing this article is built from. The system is described in eight layers, from rented compute and channels, through encrypted vaults as shared memory, domain vaults, semantic graphs over people and policies, a scheduled conductor and written behaviour policies, to a human who holds the one step that cannot be undone. The article follows an input from the outside world through the layers to the person who sends; explains why the vault is an app platform rather than storage, and the loop in which a friction becomes a tool in the same session and the tools compound; names the feedback loop that makes the setup hold, the draft as a release candidate with the recipient closing the loop; and draws two Wardley maps with Mermaid, from the outside and from the inside, showing what the team is turning into a commodity and what it is turning into a product. Every layer is linked to the article or document on this site where it was worked out. The published record of agent projects that stall is kept for the end, each reason mapped to the mechanism that answers it. Everything described is in use.

*Source: <https://newsroom.sgit.ai/articles/the-mandate-stack.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The Mandate Stack: a multi-agent system in production, layer by layer

# The Mandate Stack: a multi-agent system in production, layer by layer

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-06 · updated 2026-10-07 · [article v1.3.0, 5 versions](versions/the-mandate-stack.md) · [sgit.ai v0.6.81](https://sgit.ai/admin/versions.md) · agentsagent-behaviour-policyriskmandatevaultssgitemail-fscrmfractal-semantic-graphsorchestrationgovernancehuman-in-the-loopproductionvault-appscustom-uiwardley-mapsmermaidclaudegoogle-workspacearticle

***Abstract:** RiskMandate runs its business with about fifteen agents and one person, four times a day on a schedule and whenever the person sits down with them, with the person's name on every message that leaves. The agent that runs its CRM wrote the briefing this article is built from. The system is described in eight layers, from rented compute and channels, through encrypted vaults as shared memory, domain vaults, semantic graphs over people and policies, a scheduled conductor and written behaviour policies, to a human who holds the one step that cannot be undone. The article follows an input from the outside world through the layers to the person who sends; explains why the vault is an app platform rather than storage, and the loop in which a friction becomes a tool in the same session and the tools compound; names the feedback loop that makes the setup hold, the draft as a release candidate with the recipient closing the loop; and draws two Wardley maps with Mermaid, from the outside and from the inside, showing what the team is turning into a commodity and what it is turning into a product. Every layer is linked to the article or document on this site where it was worked out. The published record of agent projects that stall is kept for the end, each reason mapped to the mechanism that answers it. Everything described is in use.*

The Mandate Stack as it runs on 6 October 2026, read from the bottom: compute and channels rented from vendors, then the team's own files, graphs, schedule and policies, then one person above a line of their own. The right column says what each layer gives the team. Infographic from the CRM agent's briefing; everything shown is in use.

**Where this comes from.** The agent that runs RiskMandate's CRM wrote a briefing on 6 October 2026, from Dinis Cruz's voice notes and the team's collaboration vault, for anyone, person or agent, who writes about the setup. It describes what runs on that date, and everything in it is in use. This article keeps its structure and its counts and links every layer to the place on this site where it was worked out. [The agent team as it runs](the-agent-team-as-it-runs.md), published the same week, is the roster-level description of the same team; this is the layered one. "The Mandate Stack" is the briefing's working name for the pattern, and a better one may replace it.

## In short

- **This runs.** About fifteen agents and one person run RiskMandate's relationships, research, writing and events, four times a day on a schedule and whenever Dinis sits down with them, in production, today.
- **Eight layers.** Compute and channels are rented. Everything above them is the team's own: encrypted vaults as shared memory, a vault per domain, semantic graphs over people, teams and policies, a conductor, written mandates, and one human at the top.
- **One line.** Many small agents, one written mandate each, everything connected as a graph, one human who sends.
- **The world writes in from the left; nothing leaves without the person on the right.** Email, a web form, other teams' agents and an event extension all enter as data. The only exit is a send by the person whose name is on the message.
- **The vault is an app platform, not storage.** A model that writes good HTML and a vault that serves it give one person a loop: hit a friction, build the tool in the same session, deploy it into the vault, use it, repeat. The tools compound, down to an interface for one person. Without that loop, this would be another project that stalled.
- **The loop is the design.** The agents automate the hard part, capturing, connecting and remembering. The draft the person sees is a release candidate for the whole pipeline. The recipient's reply comes back through the same capture path. Mistakes are traced to captured data, a graph edge or the model, and fixed at the source.
- **Two maps.** Shared memory and the sgit tooling are being pushed toward commodity, on encrypted storage that already is one. The behaviour policies and the graphs are being pulled toward product. That is the team's strategy, drawn.
- **The record, last.** The published record of agent projects that stall is real, and it is kept for the end, each reason mapped to the mechanism here that answers it.

## One that runs

RiskMandate.ai runs its own business with a team of agents and one human, Dinis Cruz. Each agent has a narrow, written mandate, an [Agent Behaviour Policy](https://riskmandate.ai/abp.html). All shared state lives in encrypted, versioned vaults driven by sgit. Everything the team knows about people, organisations and its own work is connected as semantic graphs. The human holds the one step that cannot be undone: nothing goes to the outside world unless Dinis sends it.

The briefing counts about fifteen agents. [The agent team as it runs](the-agent-team-as-it-runs.md), written from the briefs role's field notes in the same week, names twelve roles. Both are the agents' own counts; this article keeps the briefing's and notes the difference. The collaboration vault, by the briefing's count, holds over 620 commits and 9,000 files, and every change any agent has made is in its history.

What the briefing calls the Mandate Stack is this arrangement, described as layers. The layers are not an architecture diagram drawn before the fact. They are the shape the setup had when an agent in it was asked to describe what was running.

## From the outside in

Left to right: the outside world writes in by email, by the subscribe form, through other teams' agents and an event extension; the input passes through the layers as data; the person enters from the right through Claude and Gmail, and is the only exit. From the briefing of 6 October 2026; fictional senders.

Follow one message. A person emails the agents' address. The inbox role, which can read but cannot draft or send, captures it word for word into that person's folder with a hash. It lands in the relationships vault, or in the mission vault it belongs to. Edges are added to the person's graph: who they are, what they care about, which of the team's materials meets it, which does not. On the next scheduled run the drafts role, which never reads raw mail, turns a row in the email register into a Gmail draft. Each step happens inside a written mandate, with the security role checking first and last. The draft waits in Gmail for Dinis.

Other inputs take the same shape. A reader fills in the subscribe form on this site, and the message goes into a vault the form cannot read, encrypted in the browser to the agent's key, through a [write-only lane](https://sgit.ai/docs/briefs/subscribe-lane-agent-brief.md). The newsroom's agent, in another environment, writes through a signed and encrypted lane. The Web Summit browser extension feeds the mission vault. LinkedIn is reached through its own agent and a shared vault channel.

From the right, Dinis enters three ways: in a Claude session with the vault, for research, writing, design and analysis; by email to the agents' address, with a note the next run picks up; and by answering a decision draft in the thread, lettered options and an answer box. Anyone else on the team enters by the same three paths, and a new agent joins in two chat messages. What leaves is what Dinis sends, plus the SG/Send links the roles share, Slack status posts and Drive exports into the agents' own folder. The one exception is the security role's single hold email, to Dinis.

## Layer 1: compute

The agents are Claude sessions. Most run as Cowork sessions in a Claude Teams account, each with its own role and connectors. Some run as Claude Code cloud sessions on a separate account, with access to the vault and nothing else: no email, no calendar, no CRM write. The second kind still joins the team, takes work, reports and leaves a trail. The vault is the interface, not the account.

Why the sessions run in the cloud rather than on a laptop is the subject of [Why my agents do not run on my laptop](why-my-agents-do-not-run-on-my-laptop.md): an operating system has two hard walls, the kernel and the user account, and an agent on a laptop runs inside the one marked you. Why Cowork and Claude Code are treated as different agents with different reach is in [Six agents, one inbox](six-agents-one-inbox.md). What a Claude Code cloud session needs from an administrator before it can reach a vault at all is in [the Team and Enterprise egress how-to](https://sgit.ai/docs/how-to/claude-team-egress.md), and the agent-facing surface of sgit itself, the session pattern of clone, work, commit, push, is in [Working with AI agents](https://sgit.ai/docs/agents.md).

## Layer 2: channels

One Workspace identity, cut into roles. The reader of raw inbound mail has the least power; the roles with more power never read raw mail; the send row has no agent in it. From the briefing of 6 October 2026; agents named by role.

The channels belong to one Google Workspace identity, the agents' published address, reached through connectors. Each channel is split by role rather than given whole to one agent. The inbox role reads, triages, labels and captures every message to or from a known contact word for word into that person's folder. The drafts role creates Gmail drafts only from a row in the email register, formatting only, never content. Decision drafts are how a question reaches Dinis: a draft in the thread with lettered options and an answer box, read back on the next run. Drive holds exports of vault data in one agent-owned folder. Slack carries status. LinkedIn is reached through a separate agent and a shared vault channel. SG/Send provides encrypted, revocable links for sharing. Zapier is a second connector route, tested against Gmail drafts.

The row for sending has no agent in it. One exception exists: on a critical finding the security role sends a single "SECURITY HOLD" email to Dinis.

The rule behind the split, that the account is the blast radius and no agent should hold a whole channel, is worked out in [Six agents, one inbox](six-agents-one-inbox.md), down to what a Workspace administrator can lock per organisational unit. What Gmail and Calendar can and cannot undo, and why a connector should be given a twin before an agent is given the connector, is in [Before you give an agent a connector, give the connector a twin](connector-twin-before-you-deploy-an-agent.md). The attempt to give each agent its own Workspace identity, and the line in Google's terms that stopped it, is in [The identity we wanted to give the agents](the-identity-we-wanted-to-give-the-agents.md).

## Layer 3: shared memory and messaging

The vaults are the team's shared brain. A vault is a folder of plain files, JSON, Markdown and JSONL, encrypted on the client with AES-256-GCM, versioned like git, and synced through a server that does not see plaintext. Every agent session clones the vault, works, commits and pushes. [Git for things you cannot put on GitHub](what-sgit-is.md) is the introduction; [Vault credentials](https://sgit.ai/docs/credentials.md) explains the key classes, and why a read key can be published while a vault key travels only in chat; [the security model](https://sgit.ai/security/index.md) says what the server can and cannot see.

Agents talk to each other through Email-FS, a mail protocol made of files. A message is an `.eml` file with headers for kind, priority and references. Sending writes it to the recipient's mailroom and to the sender's outbox. Moving it from mailroom to inbox is the read receipt; moving it to a done folder is completion. Each agent owns its folders and no other agent writes there. Any agent, model or person with the key can read the whole conversation with `ls` and `cat`. The convention and its history are in [The agent team as it runs](the-agent-team-as-it-runs.md) and [Replicating the agentic inbox](replicating-the-agentic-inbox.md); why a message in that system carries its own graph and is rendered by its own interface is [Custom UIs are not the exception](custom-uis-are-not-the-exception.md).

Append lanes let the outside world write in without a key. A sender gets a write-only slot on a vault: it can add files but cannot list or read anything, including what it wrote. Messages are encrypted to the recipient's public key and signed by the sender. This is how the newsroom agent, in another environment, and the Web Summit browser extension feed vaults they cannot read, and how this site's subscribe form reaches the team. The mechanism is documented in [append-lane messaging](https://sgit.ai/docs/append-lane-messaging.md), [sending messages between vaults](https://sgit.ai/docs/vault-messaging.md) and the [append lanes API](https://sgit.ai/api/append-lanes.md); the site-to-site version, where each site's agent publishes its keys and lane token, is [Agent Contact](https://sgit.ai/docs/agent-contact.md).

That memory lives in files rather than in a model's context, and why that is the right place for it, is the argument of [Memory is not a spectator sport](memory-is-not-a-spectator-sport.md).

## Layer 4: domain vaults

Context is scoped the way tools are. The relationships vault holds one folder per person. The collaboration vault links read-only to it and to the LinkedIn channel vault. A focused project gets its own mission vault with its own owner, policy and key holders: for Web Summit Lisbon 2026 there is a data vault, a discovery inbox and an extension vault, and the set can be shared with a partner without exposing the team vault. The briefing's phrase is least privilege applied to context, not just to tools.

The publishing method behind many vaults from one source, and the near-miss that taught the team to escrow write keys before publishing, is in [Seven vaults, one method](seven-vaults-one-method.md). The branch discipline that lets many sessions share one vault is [the two-branch model](https://sgit.ai/docs/two-branch-model.md). How vaults owned by different parties join through lanes and a typed graph, which is what a mission vault shared with a partner is, is in [A supply chain of vaults](supply-chain-of-vaults.md). Which classes of information the team's vaults hold and which they refuse, public, private-ish and personal, is in the privacy section of [The agent team as it runs](the-agent-team-as-it-runs.md).

## Layer 5: semantic graphs

One person's subgraph in the relationships vault, with a fictional person, organisation and interests. An interest met by one of the team's materials is a reason to send it; an interest with no edge is a gap. Contexts are further graphs laid over the same people. The folder behind the picture is in the lower panel.

The team thinks in graphs, and the vaults are built that way. A record is not a row in a table. It is a node with typed edges to other nodes, and its meaning comes from those connections. The principles carry over from the published work on [fractal semantic graphs](introducing-fractal-semantic-graphs.md) and from [graphs.sgit.ai](https://graphs.sgit.ai/): meaning is found in relationships rather than declared in a schema; confidence comes from how well connected an assertion is; unknowns are drawn as explicit nodes rather than hidden. The risk register as "a graph of graphs" on [risks.sgit.ai](https://risks.sgit.ai/) is the same idea in another domain.

**The CRM is a graph of people, organisations, interests and materials.** As of 3 October the relationships vault held 71 people, 24 organisations, 281 timeline events and 12 campaigns, by the briefing's count. Each person's folder is a small subgraph: the contact record is the node; a graph file holds nodes of kind person, their work, interest and our material, with edges such as wants and met-by; a ledger holds the timeline as an append-only edge list, each line linking the person to a message, meeting, call, task or stage change, with the last line for an id winning; every message is kept word for word with who captured it, how, and a SHA-256 hash; a materials file records every link and vault sent, by whom, when, on which channel; a sources folder, a research file and a case file hold where each fact came from and the story so far; and a README is generated, never hand-written, from all of it. Around the folders sit organisations, campaigns, a shared vocabulary with stages S0 to S7, and an index the interface reads first. Agents and websites are entities in the same graph, so the graph can answer who an external agent's human is and what the team last told it.

**Contexts are layers of graphs over the same people.** The Web Summit crowd, the RiskMandate crowd, early adopters, design partners, friendlies: each is a graph over the same contact nodes with its own campaign, targets and next steps. One person can sit in several. Contexts can be layered on contexts, a sub-group of the Web Summit crowd for investors, because each is another graph over shared nodes rather than a copy of the data. A context can be parked and picked up later without losing anything, because the people, their timelines and their graphs carry on underneath. This is the fractal idea at work: the same structure at every scale. The same move, graphs per bounded context over a shared grammar, is what [If somebody built a company on code review](if-somebody-built-a-company-on-code-review.md) proposes for code, and [Code review as a fractal semantic graph](code-review-as-a-fractal-semantic-graph.md) shows on a real repository.

**What the graph is used for.** Who gets what: an interest with a met-by edge to one of the team's materials is a reason to send it; an interest with no edge is a gap, either something to make or a reason not to email. Article nudges and campaign membership come from these edges, not from a list. Meeting preparation writes itself: a person's subgraph is the brief. "Here is what we know about you": Dinis can show a person their own graph as an honest, correctable picture; the first was sent on 3 October, rendered as a card from that person's graph file, and it is a natural reason to reply. Who has the ball: the ledger gives days since last contact, open tasks by owner and the next step. Stage as a path: known, replied, understands, using is movement along recorded edges, not a field somebody overwrites.

**The rest of the system is graphs too.** The team is a graph: every open Email-FS message is an edge from the agent asking to the agent holding it, and each session's snapshot records the picture before and after. An ABP is a capability graph: each row links an agent to a capability, a verb, object and reach drawn from a vocabulary of 23 primitives, and an instance; edges are marked granted, mandated or both, and the gap and the barrier are properties of those edges. The data-governance register is a graph of custody: each dataset links to who can read it, who has seen it, where it is stored and why it is held. Because all of it is plain files with typed edges in a versioned vault, any agent can traverse it with ordinary tools, and every edge has a history: when a relationship was added, by whom, from what source. The articles on this site are kept the same way, and [the articles as graphs](graphs.md) is that graph, this article included.

## Layer 6: orchestration

One conductor run: open and lock, security, drafts, inbox, briefs, CRM, the event mission, research, dev, security again, a card to Dinis, stop. The order is a design decision. Beside the schedule: emailing the agent, live sessions, joining in two messages. Order from the briefing of 6 October 2026.

The conductor runs four times a day. It opens a run, takes a lock, gives each agent one step in a fixed order, records evidence in a runs folder, briefs Dinis and stops. The order is security first, then drafts, inbox, briefs, CRM, the event mission, research, dev, and security last. Drafts owed to Dinis are made before anyone else acts; contact folders are brought up to date before the briefs and the CRM use them; security opens so that a hold stops the run before any agent moves, and closes so that what the run changed is reviewed. On top of the four scheduled runs, every session Dinis starts with an agent does the same kind of work sooner, so in practice the team is active far more often than the schedule alone would make it.

Dinis can simply email the agent. A note to the agents' address, catalogue this, look at this, map this, is picked up on the next run, filed into the right folder and acted on within the agents' mandates. Because the schedule is regular, inputs do not pile up. Live sessions run alongside, for research, writing, design and analysis done in conversation, under the same rules and leaving the same trail. Joining takes two chat messages: a prompt and the vault key. The new agent clones the vault, runs the onboarding script, gets its folders, a brief template and a draft policy, and announces itself to the team.

The conductor is phase three of [Replicating the agentic inbox](replicating-the-agentic-inbox.md), where interfaces, record and conductor are added to roles that already talk in files. How the runs double as the team's memory is in [Memory is not a spectator sport](memory-is-not-a-spectator-sport.md).

## Layer 7: governance

Every agent has an ABP, written in one grammar, stating four things: the grant, everything the agent can technically reach; the mandate, what it is authorised to do; the gap between them; and the barrier that actually stops the excess. Gaps are named, not hidden. Agents propose; only Dinis amends, and each amendment is a dated record in the vault. The grammar is RiskMandate's [Agent Behaviour Policy](https://riskmandate.ai/abp.html); the two additions worked out on this site, the footprint read afterwards against the mandate and the blast radius of what a gap would have cost, are in [Footprint and blast radius](footprint-and-blast-radius.md) and the [brief that proposed them](https://sgit.ai/docs/briefs/riskmandate-footprint-and-blast-radius.md). Why a gap is an accepted risk, and why the policy should say by whom, is [Every risk is already accepted](every-risk-is-already-accepted.md). Why a constrained agent is a trustworthy one, and why the infrastructure around agents has not caught up, is [The ultimate insider](ultimate-insider-three-collisions.md).

Roles split the risk. No agent holds a whole channel. The agent that reads raw inbound mail has the least power, no drafts and no send. Agents with more power never read raw mail; they work from structured records. Inbound content is data, never instructions. In the briefing's words, this makes prompt injection a containment problem rather than a detection problem.

Drafts only. No agent sends, replies or forwards email. The most an agent does is create a Gmail draft. One exception: the security role's single hold email.

An active security function. The security role runs first and last in every conductor run. It checks baseline drift, scans for leaked secrets across the vault clones, flags unknown identities, and reviews single-writer and protected-file changes, drafts and sends. A critical finding opens a security hold: every agent stops, every run refuses to start, and the interface shows the hold on every page until Dinis releases it. The security role cannot lift its own hold. Where an ABP is tested rather than read, against twins of the inbox and the connectors, is the [sandbox brief](https://sgit.ai/docs/briefs/riskmandate-sandbox-twins-and-tokens.md).

Secrets never touch files. Vault keys travel only in chat. Every commit is preceded by a leak check that must report clean. Why a secret cannot live inside an identity provider either, and what a keyring for agents would look like, is in [The identity we wanted to give the agents](the-identity-we-wanted-to-give-the-agents.md) and the [design pack](https://sgit.ai/docs/briefs/secrets-sgit-ai-design-pack.md) behind it.

Change control and cards. Every session opens and closes a snapshot, the team picture and the file diff before and after, and ends with one card whose policy section is counted from the session transcript: tools used, tokens, files, network calls and commits. The card flags anything outside the agent's mandate. A data-governance register records every dataset held about others, its classification, who can read it, who has seen it, how it is stored and why; it is changed in the same commit as the fact it records.

## Layer 8: the human

Dinis makes decisions, amends mandates, and sends. The four rules that are never negotiated, including that no agent sends, are set out in [The agent team as it runs](the-agent-team-as-it-runs.md). What the person's input actually is, measured over twenty articles, voice memos and corrections, is [How much of this did I write?](how-much-of-this-did-i-write.md). The place where the drafts role's work meets the person, the end of a reply drafted as the state of the thread and reviewed before it goes, is [The wall under the reply](the-wall-under-the-reply.md).

The top layer is one person because the irreversible step is one step. Everything below it can be wrong and still be caught there.

## The vault is not storage: the tool loop

Read, eval, print, loop, applied to a business: a friction, a request in the session, a tool as HTML, deployed into the vault, used and corrected. The loop stops when a piece of work no longer calls for a tool. Below: apps already deployed into vaults on this site.

The layers above could be read as a storage architecture with a CRM on top. That is not what makes them work. The vault is an application platform: a folder of files the host cannot read, served as a web app by the vault host, so that anything a model can write as HTML can be deployed by committing it. [Building vault apps](https://sgit.ai/docs/vault/vault-apps.md) is the contract, and [three surfaces](https://sgit.ai/docs/surfaces.md) is the choice between a page inside the vault, a vault app and a page on a site.

Put that beside a model that writes good interfaces, and one person gets a loop. Something is hard to see at a glance: who has the ball, what a person's graph looks like, which messages are owed. Ask for a view of it, in the same session, from the same files. The model builds the tool as HTML, sized to the one use case. It is committed and pushed, and the next session, on any account, has it. It is used on real work, and what it gets wrong goes back to the start. Read, eval, print, loop, applied to a business rather than to a line of code.

Three things follow. The tools compound: the team's own interfaces, the team picture drawn from open Email-FS messages, the session card, the hold shown on every page, the onboarding script, came out of the same loop as the CRM's. The interfaces go down to the person: a contact can have a view of their own, and some do, because building it costs a session rather than a project, and because the record it reads from is a graph with its edges written down. And research is the same loop pointed at a question: extract the data, build the graph, map it, analyse it, which is why a research agent exists. A data-science agent would join the same way; there is not one today.

The loop has a natural stop. A piece of work is mature when it no longer calls for a tool. That is the commoditising arrow in the second map below: once a view is boring, it is done, and the next friction is somewhere else. Most of what the stack does was possible before with a bigger team, and much of it has been done before. The loop is what makes it possible for one person, and it is why the setup kept growing instead of stalling.

The pattern is already on this site in other clothes. [Custom UIs are not the exception](custom-uis-are-not-the-exception.md) makes the argument for the inbox, where every message gets the interface for its moment. The vaults in the business plans section each carry an app built this way: [the Deck Vault](https://sgit.ai/demos/vaults/deck-vault/index.md), eight web components bundled into one page; [the evidence vault](https://sgit.ai/demos/vaults/how-much-evidence/index.md) behind [How much of this did I write?](how-much-of-this-did-i-write.md); [the connector twin](https://sgit.ai/demos/vaults/connector-twin/index.md) with its replay; [the risk graph explorer](https://sgit.ai/demos/vaults/risk-graph-explorer/index.md); [Kit Bag](https://sgit.ai/demos/vaults/kit-bag/index.md), a browser extension shipped in a vault. The code review navigator in [the review-folder brief](https://sgit.ai/docs/briefs/code-review-graphs-in-the-repository.md) is the same move for repositories. [Twenty sites in fifteen days](nineteen-sites.md) is what the loop did to a network of websites.

## The feedback loop: the draft is pre-production

Nine steps, six of them the agents' on the schedule: capture, graph, research, write, register, format. The draft in Gmail is the release candidate. The send is the person's. The recipient's reply comes back through step one. Below: the three causes a mistake is traced to, and the two levels of error correction. From the briefing of 6 October 2026.

What the agents automate is the hard part, not the send. The scarce work was never pressing send. It was capturing, reading, tagging, connecting and remembering everything about every relationship. The agents do that, inbound processing, capture into contact folders, graph building, research and writing, on a regular schedule. Dinis keeps the step with the lowest volume and the richest feedback.

The draft is a release candidate. When a message arrives in Gmail for Dinis, the whole pipeline has already run: capture, graph, research, writing, register and formatting. Reviewing it is QA on the full system, like checking pre-production before it goes live. It is also where the thinking happens. People often find out what they want to say halfway through saying it. Seeing the message as it would land is when Dinis sharpens the point, changes the ask or rethinks the next step.

Every mistake is traced to its cause. A wrong detail in a message leads back to wrong captured data, a wrong or missing graph edge, or a model error. Because every fact carries its source, capture method and hash, the cause is fixed at the source, not patched in the email. The briefing's observation is that model error is now the rarest of the three causes, because the data the agents work from is solid. That matches what [How much of this did I write?](how-much-of-this-did-i-write.md) found on this site's own corrections, traced memo by memo.

The world closes the loop. Every sent email is tested against reality. If it is wrong, the recipient says so quickly, and the reply comes back through the same capture path into their timeline. The system has error correction at two levels: Dinis before sending, the recipient after. The same two-level shape, a replay of what an agent would have done before it is allowed to do it, and a record of what it did read afterwards, is what [the connector twin](connector-twin-before-you-deploy-an-agent.md) and [Footprint and blast radius](footprint-and-blast-radius.md) describe separately.

The result is control and throughput together. Nothing on the schedule is missed, every follow-up is known, and every outgoing message has been seen by the person whose name is on it.

## Two maps: what is being commoditised, and what is being made

Map one, from the outside. The anchor is a person who writes to the team. What they see, a reply with Dinis's name on it, is custom. What they do not see, the vaults, the sessions, Workspace and encrypted storage, is product or commodity. Rendered with Mermaid wardley-beta from the source below; every placement is a claim.

A Wardley map places each component by how visible it is to the user, vertically, and by how evolved it is, horizontally, from genesis through custom-built and product to commodity. The maps here are drawn in the spirit of [wardley-maps.sgit.ai](https://wardley-maps.sgit.ai/): a map is a claim, not a picture, and the source is published next to the render so the claim can be argued with. The placements are this article's, made from the briefing, and a reader who would put a component elsewhere is probably right about something.

The first map takes the point of view of a person outside the team. What they can see is a reply with Dinis's name on it, the agents' address and the subscribe form. Everything that produces the reply sits below their line of sight: the drafts and inbox roles, the person's folder and graph, the behaviour policies, the conductor and Email-FS, all custom-built. Below those, the vaults, the Claude sessions, Google Workspace and encrypted storage are product or commodity. The shape says what the stack is: a thin custom layer where the relationship is, resting on rented parts.

**Map one, the Mermaid wardley-beta source**

[rendered image](images/ms-map-user.webp)

```
wardley-beta
  title The Mandate Stack from the outside: a person who writes to the team
  anchor "A person who writes to the team" [0.97, 0.60]
  component "A reply with Dinis's name on it" [0.89, 0.38]
  component "The agents' address" [0.87, 0.86]
  component "The subscribe form" [0.82, 0.66]
  component "Drafts role" [0.74, 0.38]
  component "Inbox capture, hashed" [0.68, 0.48]
  component "The person's folder and graph" [0.60, 0.28]
  component "Agent Behaviour Policies" [0.52, 0.20]
  component "Conductor" [0.47, 0.40]
  component "Email-FS" [0.41, 0.34]
  component "Append lanes" [0.45, 0.54]
  component "sgit vaults, shared memory" [0.32, 0.64]
  component "Claude sessions" [0.27, 0.76]
  component "Google Workspace" [0.24, 0.90]
  component "Encrypted storage, S3" [0.12, 0.88]
  "A person who writes to the team" --> "A reply with Dinis's name on it"
  "A person who writes to the team" --> "The agents' address"
  "A person who writes to the team" --> "The subscribe form"
  "A reply with Dinis's name on it" --> "Drafts role"
  "The agents' address" --> "Inbox capture, hashed"
  "The agents' address" --> "Google Workspace"
  "The subscribe form" --> "Append lanes"
  "Drafts role" --> "The person's folder and graph"
  "Inbox capture, hashed" --> "The person's folder and graph"
  "Drafts role" --> "Agent Behaviour Policies"
  "Inbox capture, hashed" --> "Agent Behaviour Policies"
  "Drafts role" --> "Conductor"
  "Inbox capture, hashed" --> "Conductor"
  "Conductor" --> "Email-FS"
  "Conductor" --> "Claude sessions"
  "Email-FS" --> "sgit vaults, shared memory"
  "Append lanes" --> "sgit vaults, shared memory"
  "The person's folder and graph" --> "sgit vaults, shared memory"
  "sgit vaults, shared memory" --> "Encrypted storage, S3"
  "Drafts role" --> "Google Workspace"
```

Map two, from the inside. The anchor is Dinis. The dashed arrows are the movement the team is making: shared memory and the sgit CLI toward commodity, the behaviour policies, the graphs and the custom interfaces from genesis toward product. Everything rests on encrypted storage, which is already a commodity. Rendered with Mermaid wardley-beta from the source below.

The second map takes Dinis's point of view and adds movement. What he sees is a CRM that is current without typing, drafts to review, decision drafts in the thread, and the custom interfaces the tool loop produces. The arrows say what the team is doing to its own components. Shared memory runs on sgit, and sgit runs on encrypted object storage, S3. Each of those is being pushed to the right on purpose, so that a vault is a folder, a push is a command, the host sees ciphertext and sizes, and nothing above them has to know how any of it works. The behaviour policies, the graphs over people and the custom interfaces move the other way, from genesis toward custom and product, because those are the parts the team is building to sell. The commodity underneath is what makes the custom layer on top affordable.

**Map two, the Mermaid wardley-beta source**

[rendered image](images/ms-map-team.webp)

```
wardley-beta
  title The Mandate Stack from the inside: the person running the business, and what is moving
  anchor "Dinis, running the business" [0.97, 0.50]
  component "A CRM that is current without typing" [0.90, 0.30]
  component "Drafts to review and send" [0.87, 0.52]
  component "Decision drafts in the thread" [0.83, 0.40]
  component "Custom UIs per use case" [0.79, 0.26]
  component "Semantic graphs over people" [0.74, 0.24]
  component "Agent Behaviour Policies" [0.68, 0.20]
  component "Security role and hold" [0.63, 0.28]
  component "Conductor" [0.59, 0.42]
  component "Email-FS" [0.52, 0.34]
  component "Mission vaults" [0.46, 0.50]
  component "sgit vaults, shared memory" [0.38, 0.62]
  component "sgit CLI" [0.26, 0.58]
  component "Claude sessions" [0.30, 0.76]
  component "Google Workspace" [0.28, 0.90]
  component "Encrypted storage, S3" [0.14, 0.88]
  evolve "Agent Behaviour Policies" 0.50
  evolve "Semantic graphs over people" 0.42
  evolve "Email-FS" 0.56
  evolve "Custom UIs per use case" 0.44
  evolve "sgit vaults, shared memory" 0.84
  evolve "sgit CLI" 0.80
  "Dinis, running the business" --> "A CRM that is current without typing"
  "Dinis, running the business" --> "Drafts to review and send"
  "Dinis, running the business" --> "Decision drafts in the thread"
  "Dinis, running the business" --> "Custom UIs per use case"
  "Custom UIs per use case" --> "sgit vaults, shared memory"
  "Custom UIs per use case" --> "Claude sessions"
  "A CRM that is current without typing" --> "Semantic graphs over people"
  "Drafts to review and send" --> "Conductor"
  "Decision drafts in the thread" --> "Conductor"
  "Semantic graphs over people" --> "sgit vaults, shared memory"
  "Conductor" --> "Agent Behaviour Policies"
  "Conductor" --> "Security role and hold"
  "Conductor" --> "Email-FS"
  "Conductor" --> "Claude sessions"
  "Security role and hold" --> "Agent Behaviour Policies"
  "Email-FS" --> "sgit vaults, shared memory"
  "Mission vaults" --> "sgit vaults, shared memory"
  "Semantic graphs over people" --> "Mission vaults"
  "sgit vaults, shared memory" --> "sgit CLI"
  "sgit vaults, shared memory" --> "Encrypted storage, S3"
  "Drafts to review and send" --> "Google Workspace"
```

Two notes on reading them, both borrowed from the mapping site. Coordinates are visibility first, evolution second, and transposing them renders without an error and asserts something else. And a component cannot be more evolved than the least evolved thing it depends on, which is why the custom middle of these maps cannot move right until the policies do.

## Why it holds

The briefing gives five reasons the setup holds. Each of them answers something in the record kept for the end of this article.

- **The control surface is small, explicit and versioned.** Trust grows one mandate at a time, and every change to a mandate is visible: a written policy per agent, in one grammar, amended only by the human, with each amendment dated.
- **The human holds the irreversible step.** Everything else can be wrong and still be caught at the draft. This is the pattern the email products shipped and the guides from the model vendors ask for, applied here as a rule rather than a default.
- **Shared state is files, not context windows.** Agents do not need to remember; they read. Any session, on any account, can pick up where another left off. A fixed schedule, one step per agent, and a card per session that counts tools, tokens, files and network calls mean the cost is read rather than guessed.
- **The graph puts meaning on the read path.** Agents do not query raw data and guess. They traverse records whose relationships, sources and vocabulary are written down and shared. A wrong detail is traced to a captured fact, an edge or the model, and fixed where it came from.
- **Everything leaves a trail.** Commits, ledgers, snapshots, cards, run evidence. The system can be audited by the same tools that run it. Roles split the risk, inbound content is data, a security role runs first and last and can stop the team, and secrets never touch files.

None of this makes the setup immune. It says where a failure would have to get through.

## A working name

The briefing calls the pattern the Mandate Stack. The name has to carry three things. The mandate, because the unit of the design is a written policy per agent, not a model or a framework. The stack, because the layers are real and the lower ones are rented while the upper ones are owned. And the human who sends, which the name does not say and the one-line version does: many small agents, one written mandate each, everything connected as a graph, one human who sends. A better name may come. The description is what matters, and it is the description of something that runs.

## What is not in it

Every component named above is in use on the date of writing; that was the briefing's rule and it is this article's. What is not in it is the list of things the team knows it lacks. The things [The agent team as it runs](the-agent-team-as-it-runs.md) lists as not working yet still apply: commit authorship is not signed, so an agent's identity inside a shared vault is its branch rather than a signature; a vault key cannot be revoked, only replaced by a new vault; most barriers are policy-only, enforced by the process they constrain, and a separate permission authority that holds the credentials and decides each action does not exist in this setup. The three wishes in [Why my agents do not run on my laptop](why-my-agents-do-not-run-on-my-laptop.md), an identity, a secret store and a key pair per agent, are the platform-side half of the same list.

And the question underneath stays open: who gives the mandate over a piece of information, and whether the recipient of an email has the authority to hand it to an agent at all. The setup's answer so far is to hold less and to say what it holds. The question gets a document of its own.

## The record, for anyone who asks why this is worth writing down

The reasons the record gives for agent projects failing, each with who said it and when, beside the mechanism in the stack that answers it. The dark panel is the fair reading: the record is of pilots that stall, and the pattern that shipped stops at the draft. Sources in the Sources section.

The complaint is familiar: agents do not behave, agentic workflows do not work, projects are cancelled or never pushed to production. The record supports the complaint, and it is worth being exact about what it says and when.

| When | Who | What was reported |
|---|---|---|
| 25 Jun 2025 | Gartner, prediction | More than 40% of agentic AI projects will be cancelled by the end of 2027, for "escalating costs, unclear business value or inadequate risk controls". About 130 real agentic vendors among thousands; the rest "agent washing". |
| Mar 2025 | S&P Global, survey of more than 1,000 | 42% of companies abandoned most of their AI initiatives, up from 17% the year before. The average organisation scrapped 46% of proofs of concept before production. |
| Aug 2025 | MIT NANDA, report | 95% of organisations "getting zero return" from generative AI. The report's own funnel, read by its critics, puts the success rate of actual pilots nearer a quarter; the figure is the report's word "directional". |
| 30 Sep 2025 | Gartner, survey of 360 IT leaders | 15% considering, piloting or deploying fully autonomous agents. 19% trust vendors' hallucination protection. 74% see agents as a new attack vector. 13% strongly agree they have the governance in place. |
| Nov 2025 | McKinsey, survey of 1,993 | 23% scaling an agentic system somewhere, 39% experimenting; in any one business function, at most 10% scaling. Inaccuracy the most common harm, reported by 30%. |
| Jan 2026 | Deloitte, survey of 3,235 | 25% have moved 40% or more of their AI experiments to production; pilots stretch "to 18 months or more"; 21% report a mature governance model for autonomous agents. |
| Jun 2026 | Forrester, report | 75% say they have adopted agentic AI; "only a small minority" run production deployments beyond "agentish" chatbots. ROI uncertainty, "trapped in pilot mode", governance gaps, a "trust tax". |
| Jul 2026 | KPMG, survey of 2,145 | 49% scaled back or paused agent rollouts because operating costs outran returns. 7% report established ROI. 26% have real-time visibility of what agents cost to run. |
| Sep 2025 | Carnegie Mellon, benchmark | The best agent completes 30% of 175 simulated office tasks end to end. |

The same period has its reversals: Klarna hiring human support staff again in May 2025 after calling its AI support "lower quality"; Taco Bell slowing its drive-through voice AI in August 2025 and keeping people in the loop at busy sites; Commonwealth Bank of Australia reversing 45 redundancies it had attributed to a voice bot; Ford rehiring about 350 quality inspectors in June 2026 after AI inspection missed defects. In each case the company kept the AI and put a person back at the step that mattered.

A fair reading has two more lines. First, agents do reach production: Google Cloud's September 2025 survey of organisations already using generative AI found 52% with agents in production, and LangChain's developer survey, fielded in late 2025, found 57%. The record is of pilots that stall, not of a technology that cannot ship. Second, the pattern that shipped in email is the same everywhere: Gmail's Gemini drafts (May 2025), Outlook's Copilot and its agent mode (April 2026), Superhuman's auto-drafts (July 2026) and Shortwave's triggered drafts (January 2026) all stop at the draft and leave the send to the person. OpenAI's April 2025 guide to building agents tells builders to escalate "high-risk, sensitive, or irreversible actions" to a human; Anthropic's December 2024 note on effective agents says to pause for human feedback at checkpoints and to add complexity only when it demonstrably helps.

The MIT report's own explanation of failure, tools that do not learn from or adapt to workflows, and McKinsey's finding that the organisations seeing value were three times likelier to have redesigned their workflows, are the closest the record comes to describing the setup above from the outside. The workflow here was redesigned around one fact: the draft is the release candidate.

## Threads woven here

- [The agent team as it runs](the-agent-team-as-it-runs.md): the roster-level description of the same team, the four rules, the barriers graded, the three classes of information.
- [Replicating the agentic inbox](replicating-the-agentic-inbox.md): the phases from one session to the team, and the conductor as phase three.
- [Six agents, one inbox](six-agents-one-inbox.md): the account as the blast radius; Cowork and Claude Code as different agents with different reach.
- [Why my agents do not run on my laptop](why-my-agents-do-not-run-on-my-laptop.md): the compute layer, and the three wishes.
- [Footprint and blast radius](footprint-and-blast-radius.md), [Every risk is already accepted](every-risk-is-already-accepted.md) and [The ultimate insider](ultimate-insider-three-collisions.md): the governance layer's vocabulary and its reasons.
- [Before you give an agent a connector, give the connector a twin](connector-twin-before-you-deploy-an-agent.md): the channels layer tested before it is granted.
- [The identity we wanted to give the agents](the-identity-we-wanted-to-give-the-agents.md): why secrets never touch files, and where they cannot live either.
- [Introducing fractal semantic graphs](introducing-fractal-semantic-graphs.md), [Code review as a fractal semantic graph](code-review-as-a-fractal-semantic-graph.md) and [If somebody built a company on code review](if-somebody-built-a-company-on-code-review.md): the graph layer's grammar, and contexts as graphs over a shared one.
- [Memory is not a spectator sport](memory-is-not-a-spectator-sport.md) and [Custom UIs are not the exception](custom-uis-are-not-the-exception.md): memory as files, and a message that carries its own graph.
- [Seven vaults, one method](seven-vaults-one-method.md) and [A supply chain of vaults](supply-chain-of-vaults.md): domain vaults, and vaults owned by different parties joined through lanes.
- [The wall under the reply](the-wall-under-the-reply.md) and [How much of this did I write?](how-much-of-this-did-i-write.md): where the human's review happens, and what the human's input is.
- [Git for things you cannot put on GitHub](what-sgit-is.md), [Vault credentials](https://sgit.ai/docs/credentials.md), [Working with AI agents](https://sgit.ai/docs/agents.md), [the two-branch model](https://sgit.ai/docs/two-branch-model.md), [append-lane messaging](https://sgit.ai/docs/append-lane-messaging.md), [sending messages between vaults](https://sgit.ai/docs/vault-messaging.md), [the append lanes API](https://sgit.ai/api/append-lanes.md), [Agent Contact](https://sgit.ai/docs/agent-contact.md), [the security model](https://sgit.ai/security/index.md) and [the egress how-to](https://sgit.ai/docs/how-to/claude-team-egress.md): the shared-memory and compute layers as documentation.
- [The footprint brief](https://sgit.ai/docs/briefs/riskmandate-footprint-and-blast-radius.md), [the sandbox brief](https://sgit.ai/docs/briefs/riskmandate-sandbox-twins-and-tokens.md), [the subscribe lane brief](https://sgit.ai/docs/briefs/subscribe-lane-agent-brief.md) and [the identity and secrets design pack](https://sgit.ai/docs/briefs/secrets-sgit-ai-design-pack.md): the governance and lane work as briefs to RiskMandate and to secrets.sgit.ai.
- [Building vault apps](https://sgit.ai/docs/vault/vault-apps.md), [three surfaces](https://sgit.ai/docs/surfaces.md) and [the review-folder brief](https://sgit.ai/docs/briefs/code-review-graphs-in-the-repository.md): the contract the tool loop deploys against, and the same loop applied to repositories. [Twenty sites in fifteen days](nineteen-sites.md): the loop applied to websites.
- [The articles as graphs](graphs.md): this site's own records kept the same way. [wardley-maps.sgit.ai](https://wardley-maps.sgit.ai/): maps as claims, and the coordinate contract the two maps follow.

## Sources

- *The Mandate Stack: a briefing on RiskMandate's agentic setup*, v0.3, 6 October 2026, written by the CRM agent (@crm.2) from Dinis Cruz's voice notes and the team's collaboration vault; classified public, no contact data. The layers, the channel table, the folder layout, the run order, the governance rules, the feedback loop and the five reasons are taken from it, as are the counts (about fifteen agents; over 620 commits and 9,000 files; 71 people, 24 organisations, 281 timeline events and 12 campaigns as of 3 October).
- Three voice notes by Dinis Cruz, 6 and 7 October 2026: on the complaint that agentic workflows do not reach production and on the name; on leading with the system, the flow from the outside world, and the maps; and on the vault as an app platform, the tool loop, the schedule of four runs a day, and the source blocks.
- [RiskMandate.ai, the Agent Behaviour Policy](https://riskmandate.ai/abp.html); [graphs.sgit.ai](https://graphs.sgit.ai/); [risks.sgit.ai](https://risks.sgit.ai/); [wardley-maps.sgit.ai](https://wardley-maps.sgit.ai/), whose notes for agents give the coordinate order and the quoting rule the two map sources follow. The maps were rendered with Mermaid 12.1.0's wardley-beta diagram.
- The record: Gartner press releases of [25 June 2025](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027) and [30 September 2025](https://www.gartner.com/en/newsroom/press-releases/2025-09-30-gartner-survey-finds-just-15-percent-of-it-application-leaders-are-considering-piloting-or-deploying-fully-autonomous-ai-agents); S&P Global Market Intelligence, Voice of the Enterprise AI use cases 2025, as reported by [CIO Dive, March 2025](https://www.ciodive.com/news/AI-project-fail-data-SPGlobal/742590/); MIT NANDA, *The GenAI Divide*, as reported by [Fortune, 18 August 2025](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/), with the critique in [Fortune, 21 August 2025](https://fortune.com/2025/08/21/an-mit-report-that-95-of-ai-pilots-fail-spooked-investors-but-the-reason-why-those-pilots-failed-is-what-should-make-the-c-suite-anxious); [McKinsey, The state of AI 2025](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025); [Deloitte, State of AI in the Enterprise 2026](https://www.deloitte.com/au/en/issues/generative-ai/state-of-ai-in-enterprise.html); [Forrester, The state of agentic AI in 2026, June 2026](https://www.forrester.com/blogs/the-state-of-agentic-ai-in-2026-companies-are-chasing-few-are-catching/); KPMG Global AI Pulse Q2 2026, as reported by [PPC Land, July 2026](https://ppc.land/kpmg-finds-49-cut-ai-agent-rollouts-when-costs-outran-value/); [Carnegie Mellon, TheAgentCompany, arXiv 2412.14161, v3 September 2025](https://arxiv.org/abs/2412.14161); [Google Cloud, ROI of AI 2025, September 2025](https://www.googlecloudpresscorner.com/2025-09-04-Google-Cloud-Study-Reveals-52-of-Executives-Say-Their-Organizations-Have-Deployed-AI-Agents%2C-Unlocking-a-New-Wave-of-Business-Value%2C1); [LangChain, State of agent engineering](https://langchain.com/state-of-agent-engineering). Gartner's and S&P's own pages refused automated fetches during research, so their figures were checked against trade-press reproductions of the releases.
- The reversals: Klarna, [Entrepreneur, May 2025](https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/); Taco Bell, [Nation's Restaurant News, August 2025](https://www.nrn.com/restaurant-technology/taco-bell-is-adjusting-its-voice-ai-plans); Commonwealth Bank of Australia, [Bloomberg, 21 August 2025](https://www.bloomberg.com/news/articles/2025-08-21/commonwealth-bank-reverses-job-cuts-decision-over-ai-chatbots); Ford, [Repairer Driven News, July 2026](https://www.repairerdrivennews.com/2026/07/08/ford-rehires-350-engineers-after-ai-fails-at-quality/).
- Draft-and-send as the shipped pattern: [Anthropic, Building effective agents, December 2024](https://www.anthropic.com/research/building-effective-agents); OpenAI, *A practical guide to building agents*, April 2025; [TechCrunch on Superhuman auto-drafts, July 2026](https://techcrunch.com/?p=3139498); [Shortwave changelog, January 2026](https://shortwave.com/changelog); Microsoft Learn on Copilot in Outlook leaving the reply in the compose window for the user to review and send.

*Drafted from a briefing written by the RiskMandate CRM agent (@crm.2, v0.3, 6 October 2026) from Dinis Cruz's voice notes and the team's collaboration vault, and from three voice notes by Dinis Cruz, who is the author of the argument and the person with editorial responsibility, by agent@riskmandate.ai (Claude Fable 5.1, claude-fable-5-1) in the sgit.ai site session, on 6 October 2026. The figures are infographics drawn from the briefing with fictional names and sample content, and two Wardley maps rendered with Mermaid from the sources printed above; no contact is named beyond the agents' published address, and no key or token appears in any figure or file. Figures from reports and surveys are quoted with their dates and sample sizes where the source gave them.*

*© 2026 Dinis Cruz. This article's own text is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You're free to share and adapt it, as long as you give credit. Quoted material and linked sources keep their own licences.*

## Threads

Agents & policyGraphs & knowledge[This article as a graph →](graphs.md#the-mandate-stack)

### Builds on

- [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](the-agent-team-as-it-runs.md) Twelve agents on dedicated accounts, encrypted vaults as the only memory, messages as files, a folder per person, and a mailbox nobody sends from.
- [Why my agents do not run on my laptop: chat, Cowork and Code in the cloud, a vault as the shared drive, and the two walls an operating system has](why-my-agents-do-not-run-on-my-laptop.md) An OS has two hard walls, the kernel and the user; an agent on a laptop runs inside the one marked you, so the agents run in the cloud with a vault as shared drive.
- [Six agents, one inbox: what a real multi-agent setup taught me about access policies](six-agents-one-inbox.md) An access policy for an agent is only as real as its worst row: every rule in a real six-agent setup, graded by how it is enforced today.
- [Before you give an agent a connector, give the connector a twin](connector-twin-before-you-deploy-an-agent.md) An agent with a Gmail or Calendar connector can do things the platform cannot undo; a journal of every call, replayed, shows what it did and what can go back.
- [The identity we wanted to give the agents: a week of design, the line in Google's terms, and why login plus secrets is still too hard](the-identity-we-wanted-to-give-the-agents.md) A week of designing identities for agents and users met Google's terms; what survived is a passkey-unlocked keyring and a gap nobody sells.
- [Git for things you cannot put on GitHub](what-sgit-is.md) sgit is git for files you cannot put on GitHub: encrypted before they leave your machine, versioned like git, stored where the server cannot read a byte.
- [Replicating the agentic inbox: a walkthrough from one Claude session to a team of agents that never press send](replicating-the-agentic-inbox.md) How to copy a working agentic email setup in phases: a mailbox and Claude seat of the agent's own, one session with a policy, then roles talking in files.
- [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](custom-uis-are-not-the-exception.md) Every message has a graph, so it can be shaped for the reader's moment; a custom interface per moment is now how interfaces get made, and each gets a policy.
- [Memory is not a spectator sport: how a web of open sites, graphs and vaults became the memory for sessions like this one](memory-is-not-a-spectator-sport.md) Agentic memory as context management: many published, fractal, provenance-carrying memories rather than one store, shown in the session that wrote the article.
- [Seven vaults, one method](seven-vaults-one-method.md) Publishing seven encrypted vaults in a fortnight produced a method, and every rule in it exists because something went wrong first.
- [A supply chain of vaults: how GenAI, open data and small custom tools could bring the price of food down](supply-chain-of-vaults.md) The food chain is a data problem: one encrypted vault per party, joined by append lanes and a typed graph, could cut the waste that keeps prices high.
- [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](introducing-fractal-semantic-graphs.md) A fractal semantic graph has no privileged level and no single schema: each world keeps its own vocabulary and connects to others through named edges.
- [If somebody built a company on code review: how I would do it, and why it is only now possible](if-somebody-built-a-company-on-code-review.md) A reader's seven questions answered as a company plan: one reader for every layer, review as a science, and the layers as the customer's own.
- [Code review as a fractal semantic graph: source code is already one, and the review should read every layer of it](code-review-as-a-fractal-semantic-graph.md) Source code is layers within layers, each a graph with its own vocabulary; code review should read a change at every one, and a vault shows it done on real code.
- [Footprint and blast radius: what the agent actually did, and what it would have cost](footprint-and-blast-radius.md) Footprint is what an agent actually did, read afterwards from logs and vault history; blast radius is what a row of its reach would cost the business today.
- [Every risk is already accepted. The only question is by whom, and for how long.](every-risk-is-already-accepted.md) A risk exists the moment the exposure does, so somebody is already carrying it; the only questions worth asking are who has accepted it and until when.
- [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](ultimate-insider-three-collisions.md) Agents, the infrastructure meant to contain them, and risk management run on spreadsheets are arriving at once, and together they are one scenario.
- [How much of this did I write? The numbers behind twenty articles in four weeks, and what the input actually was](how-much-of-this-did-i-write.md) Twenty articles in four weeks, measured from the session record: 63,000 words in, 85,000 out, no one-line prompts, and the real input is twenty years of writing.
- [The wall under the reply: end an email with the state of the thread, not the thread](the-wall-under-the-reply.md) End an email reply with the state of the thread for this reader, not the quoted wall: decided, open, next, who is on copy, with links to the record.
- [Twenty sites in fifteen days, and what that did to the writing](nineteen-sites.md) One site became twenty repositories in fifteen days because each argument needed its own version history, and the index now starts from a question.

### Continued by

- [Not a straight line: working for RiskMandate by working on the newsroom, and why the thinking is never wasted](not-a-straight-line.md) Working on the newsroom solved RiskMandate's oldest problem in two days: progress is not a straight line, and the thinking is never wasted.
- [The records ran out: a fresh agent found the shared contract in two MCP calls, and where sgit and RiskMandate fit at the edges](the-records-ran-out.md) A fresh agent found a shared contract in two MCP calls from build records; where the records stopped is exactly where evidence labels and sgit vaults fit.
- [Why I love Wardley maps: the best of ours, how I read one, and a map inside a map inside a map](why-i-love-wardley-maps.md) The best of our Wardley maps with their context, why the technique matters, one map read as a story, and a map inside a map inside a map.
- [One article, five readers: a librarian, a cartographer, a historian, an explainer and a storyteller read the same piece](one-article-five-readers.md) Write the article first, then send five agent readers through it: a catalogue, an ontology and maps, the arc, two minutes, and a deck.
- [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](riskmandate-ten-questions.md) Ten hard questions from a conference, answered in a two-hour interview: what RiskMandate does, what it deliberately is not, and how mature each part is.
- [A locked-down desktop for an agent, by the minute, is still hard to rent](an-agent-desktop-by-the-minute.md) Nine properties a safe agent desktop needs, nine products against them, the macOS day-long lease, and the startup credits that would pay for testing it.
- [Where is the why? A permission prompt asked me to decide, and kept the reason](where-is-the-why.md) A prompt asked for a decision and kept the reason. Read through the policy, the law on uninformed consent, and the fixes that worked: put the why in the prompt.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 34 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=34)

## From the desk

- [The week to 7 October: the agent team, written up from the inside](desk/the-week-to-7-october.md) the week, 2026-10-07
- [Create anywhere, edit your own: a rule learned in the inbox, applied to the newsroom](desk/create-anywhere-edit-your-own.md) thread, 2026-10-07
- [A model that can go in every direction needs someone with a direction](desk/a-model-that-can-go-in-every-direction.md) nugget, 2026-10-07
- [Thinking with a Wardley map](collections/wardley-maps.md) collection, 6 articles
- [What the human brings](collections/what-the-human-brings.md) collection, 4 articles
- [Behaviour policy in practice](collections/behaviour-policy-in-practice.md) collection, 11 articles

**Posting this article on LinkedIn?** The cover is [the-mandate-stack.jpg](banners/the-mandate-stack.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-mandate-stack.html)*
