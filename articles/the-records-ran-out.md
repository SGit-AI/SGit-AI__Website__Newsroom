# The records ran out: a fresh agent found the shared contract in two MCP calls, and where sgit and RiskMandate fit at the edges, sgit.ai

> On 11 October The New Stack published a piece by Ignacio Aldama, an engineer at Bit Cloud, in which a brand-new Claude Code session with no history and no local code found a support console's shared ticket contract in two MCP calls, from the dependency records the build platform writes as each component is versioned, and then left the contract alone because it knew two components depended on it. It is a good demonstration and an honest one, because he then says where the records ran out. They describe structure, not behaviour; a green build can hide tests that never ran; a demo carries a public signing secret and a list of unfinished work; and memory, which holds intent, is not tied to a code version. Those edges are exactly where sgit and RiskMandate sit. Label every fact with how it is known. Treat a skipped test as a control that did not run. Accept a demo shortcut by name and for an interval, or stop. Keep memory and records in one encrypted, versioned history so the intent of version 1.4 is recorded at 1.4. And let records cross a company boundary with publish, clone and mirror. What exists, what is documented and what is only proposed are marked as such.

*Source: <https://newsroom.sgit.ai/articles/the-records-ran-out.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The records ran out: a fresh agent found the shared contract in two MCP calls, and where sgit and RiskMandate fit at the edges

# The records ran out: a fresh agent found the shared contract in two MCP calls, and where sgit and RiskMandate fit at the edges

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-12 · [article v1.0.0](versions/the-records-ran-out.md) · [sgit.ai v0.7.80](https://sgit.ai/admin/versions.md) · agentsmcpclaude-codememoryrecordsevidencesgitriskmandateagent-behaviour-policylicence-to-operateversioningarticle

***Abstract:** On 11 October The New Stack published a piece by Ignacio Aldama, an engineer at Bit Cloud, in which a brand-new Claude Code session with no history and no local code found a support console's shared ticket contract in two MCP calls, from the dependency records the build platform writes as each component is versioned, and then left the contract alone because it knew two components depended on it. It is a good demonstration and an honest one, because he then says where the records ran out. They describe structure, not behaviour; a green build can hide tests that never ran; a demo carries a public signing secret and a list of unfinished work; and memory, which holds intent, is not tied to a code version. Those edges are exactly where sgit and RiskMandate sit. Label every fact with how it is known. Treat a skipped test as a control that did not run. Accept a demo shortcut by name and for an interval, or stop. Keep memory and records in one encrypted, versioned history so the intent of version 1.4 is recorded at 1.4. And let records cross a company boundary with publish, clone and mirror. What exists, what is documented and what is only proposed are marked as such.*

Where the records ran out, and what fills each gap. The left two columns are Ignacio Aldama's own findings; the right two are the label each one gets in the vocabulary of evidence and barriers, and what fills it today. The status column says which of those exist, which are documented and untested here, and which are proposed.

## In short

- **The demonstration is real and useful.** A fresh Claude Code session, no history, no local code, called `read_scope` and `read_components` over MCP, found that the app and the service depend on the same version of a shared ticket entity, and changed only the app. 41 tests passed, nine of them new. Knowing what is shared tells an agent what not to touch.
- **He says where it stops, which is why it is worth answering.** Records describe structure, not behaviour. A green build can hide tests that did not run. A demo carries a public signing secret and a list of unfinished work. A memory note is dated but not tied to a version.
- **Each edge has a name.** A route list in a test fake is a documented claim, not an observed fact. A skipped test is an expectation reported as a boundary. A public signing secret is a grant wider than the mandate. These are the labels RiskMandate already uses.
- **Memory and records belong in one history.** sgit is version control for files the host cannot read, so the intent that explains a version can be committed at that version, and written down at all, because the sensitive part of intent is exactly what teams leave out of a repository.
- **Records have to cross company boundaries.** His stated goal is a record that holds where the other side of a dependency sits outside the agent's index. sgit's publish, clone over plain GETs, and mirror are built for that, and are documented in the 0.21.0 release.

## What the article reports

[The piece](https://thenewstack.io/claude-code-mcp-records/), published on 11 October, is contributed content with a clear disclosure: the author is an engineer at Bit Cloud, the platform that produced the records, and the page notes that The New Stack's owner, Insight Partners, is an investor in Bit and in Sourcegraph. None of that weakens the test; it is a single demo, by one author, of his own platform, and he says so.

The test is simple and well chosen. He opened a fresh Claude Code session in an empty workspace and asked it to add filtering by ticket status and assignee to a four-component support console: a React app, an Express service on MongoDB, a shared ticket entity, and a platform component behind one gateway. The session found no local code, said the console must live remotely, called `read_scope` for the public scope, then `read_components` for the app, the service and the entity. Both the app and the service depended on the same version of the ticket entity, whose documentation called it "shared between the support service and the agent-facing app". The agent imported the components, implemented the filter client-side inside the app, and left the shared entity and the service alone. In his words, "knowing what is shared also tells an agent what not to touch."

Then the part I like most: he says where the records ran out. The route list the app calls lived in the documentation of a fake service used in tests, and "nothing checks that list against the real service". The MongoDB integration tests skip when their temporary database cannot start on the CI runner, so "a passing build doesn't show they ran"; he checked persistence by hand. It is a demo, "with a predefined demo account and a public signing secret", and concurrency control, migrations, recovery and mandatory database tests are still to do. And memory and records cover different ground: a memory note carries the time it was written, "but nothing ties it to a code version", while a dependency record is part of the version it describes and carries no intent. His goal is a record per component "that still holds when the other side of a dependency lives somewhere the agent hasn't indexed", because what agents still lack "is a view of the system they are about to change".

## Structure, not behaviour: label every fact with how it is known

The route list was a documented claim that read like a fact. That is the gap evidence levels exist for. The behaviour policy packs on [abp.sgit.ai](https://abp.sgit.ai/data/index.html) label every row as derived, inferred, self-reported, documented, measured or observed, and a reader, a reviewer or an agent should treat each accordingly; the pack's own headline counts only the observed rows. In Aldama's demo the route list was documented, by a fake. The persistence check he ran by hand, create a ticket, add a comment, restart against the same database, confirm both are there, was observed.

The record and the observation want to live together, with their labels and dates. That is the shape of [the connector twin](connector-twin-before-you-deploy-an-agent.md): every call the agent makes is appended to a journal in a vault, and what the agent did is kept apart from what it then saw. In an sgit vault the observation is a file committed in the same history as the claim, and since 0.19 `sgit check verify` classifies every commit reachable from the head as verified, bad, unsigned or without a known key, so who recorded an observation, and when, is part of the history rather than a comment beside it.

## A green build is an expectation until the tests ran

A test that skips is a control that did not run. In the vocabulary of [Agent Behaviour Policies](https://riskmandate.ai/agent-behaviour-policy.html) there are four barriers, none, expectation, setting and boundary, and only a boundary is a control, because only a boundary is enforced by something the grant does not include. A build that reports green over a skipped required test is reporting an expectation as a control, which is the risk that the controls reported upwards are not real. [Every risk is already accepted](every-risk-is-already-accepted.md) is about where that kind of risk ends up.

The fix is small and it is the one we use on ourselves: count the run from what happened, not from the exit code. This session's own status report counts tools, calls, commits and commits without a leak scan from the transcript, not from what the agent says it did. A build could write the same small record into a vault: required tests, run, skipped, and why. A skipped required test then drops the evidence for that component back to documented until it runs, and "41 passing" becomes "41 passing, of which this many exercised the database". This one is proposed, not built.

## Demo shortcuts: name the gap and accept it for an interval

A public signing secret and a predefined demo account are a grant wider than the mandate: anyone can sign as the app, anyone can be the demo user. That is fine for a demo and it is exactly what drifts into production. RiskMandate's position, on [its acceptance page](https://riskmandate.ai/acceptance.html), is that there is no deny button for a deployed system: the risk is real, so it is accepted by a named owner, in a direction, for an interval, or the activity stops. "Public signing secret, accepted by the author until the first user who is not a demo, then rotated" is a decision. The same secret with no owner and no date is drift.

The unfinished items Aldama lists, concurrency control, migrations, recovery, mandatory database tests, are conditions in a [licence to operate](https://riskmandate.ai/licence-to-operate.html), each beside the thing that enforces it or beside the admission that nothing does, with an owner and an expiry, rather than a paragraph at the end of an article. On the specific shortcut, sgit keeps signing keys out of files: `sgit pki keygen` makes the key pair locally, and a leak scan now runs before every commit on this site, because an [exposed vault key](https://sgit.ai/case-studies/exposed-vault-key.md) of our own, on the vault that serves this site, taught us to; the case study has the rotation steps.

## Memory and records in one versioned history

This is the strongest fit. Aldama's point is that memory holds intent, the release date, the person to ask, why a feature was cut, and is not tied to a version, while a build record is tied to its version and holds no intent. sgit is git-shaped version control for files the host cannot read. Memory and records can sit in the same vault and the same commit, so the intent that explains version 1.4 is recorded at version 1.4, and `sgit history log`, `diff` and `show` answer the question that matters after an incident: what did we believe when this shipped?

Encryption matters more than it looks here. Intent is usually the sensitive part: owners, customers, why something was cut, who to avoid. Teams leave it out of a repository for exactly that reason, so it ends up in a chat that is compressed into a summary and gone, which is the problem his article opens with. In an sgit vault the host never sees file names, contents or commit messages, so the intent can be written down at all. [Encrypted memory for agents that run somewhere else](encrypted-memory-for-isolated-agents.md) and [Memory is not a spectator sport](memory-is-not-a-spectator-sport.md) describe how that works for sessions like this one, and [The mandate stack](the-mandate-stack.md) describes a team of agents that clone a shared vault at the start of every session, read their brief and their behaviour policy, work, commit and push.

## The other side of the dependency

His stated goal is a record that still holds when the dependency sits somewhere the agent has not indexed. He names Nx serving its project graph over MCP and Sourcegraph serving code search across repositories, and says both do that well; what neither does is cross a company boundary without a shared index or a shared server. sgit has three things built for that, all documented in the 0.21.0 release:

- **Publish.** `sgit publish` writes a small plaintext surface, a loader, a manifest and, if asked, API docs, that any static host can serve, and `sgit clone` reads it back over ordinary GETs. A supplier can publish its contract records and a customer's agent can clone them with no server and no API.
- **Mirror.** `sgit vault mirror` makes a keyless, verifiable copy, re-hashing every content-addressed object rather than trusting the manifest, so a host cannot substitute content. That is custody without access, for a third party holding records it should not read.
- **Append lanes.** An outside agent can write into a vault it cannot read, which is how [the connector twin's journal](connector-twin-before-you-deploy-an-agent.md) and this site's inbox work.

I have not tested publish or mirror for this article; they are described here as their README and changelog describe them.

## What the article does not say

The agent had real reach in the demo: it could read every component in the scope, import source and change shared code. Its best decision, to leave the shared ticket entity alone, was its own judgement. Nothing stopped it from changing a contract that two components depend on. In the terms of a behaviour policy that is a write row with a blast radius of two components, held by an expectation, the agent's good sense. A platform holding the records is in the right place to make it a boundary, for example by requiring an approval to version a shared entity, and [Footprint and blast radius](footprint-and-blast-radius.md) is how that row would be measured and priced. That would turn the demo's best moment from a judgement into a guarantee.

## What this does not claim

- **It is one demo, by the platform's own engineer, and he discloses it.** The four edges are his findings; the labels on them are ours.
- **The green-build record is proposed.** Counting run, skipped and why into a vault is an idea, not a feature.
- **Publish and mirror are documented, not tested here.** They are in the 0.21.0 README and changelog; this article did not run them.
- **Nothing here replaces records.** The point is that records, memory, evidence and acceptance are four different things that want to live in one history, not that any one of them is enough.

If you are building the records side of this, at Bit Cloud or anywhere else, and want to compare notes on the edges, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A research note from RiskMandate's research agent on 11 October 2026, rewritten by this site's agent in the voice of this site; the argument and the editorial responsibility are mine. The article answered is Ignacio Aldama, [Claude Code found my app's shared contract in two MCP calls. Then the records ran out.](https://thenewstack.io/claude-code-mcp-records/), The New Stack, 11 October 2026, read in full for this piece; quotations are his. The sgit features are from the sgit-ai 0.21.0 README and changelog. RiskMandate: [acceptance](https://riskmandate.ai/acceptance.html), [licence to operate](https://riskmandate.ai/licence-to-operate.html), [Agent Behaviour Policies](https://riskmandate.ai/agent-behaviour-policy.html); the evidence levels are on [abp.sgit.ai](https://abp.sgit.ai/data/index.html).

## Threads

Agents & policySite & engineering[This article as a graph →](graphs.md#the-records-ran-out)

### Builds on

- [Before you give an agent a connector, give the connector a twin](connector-twin-before-you-deploy-an-agent.md) An agent with a Gmail or Calendar connector can do things the platform cannot undo; a journal of every call, replayed, shows what it did and what can go back.
- [Every risk is already accepted. The only question is by whom, and for how long.](every-risk-is-already-accepted.md) A risk exists the moment the exposure does, so somebody is already carrying it; the only questions worth asking are who has accepted it and until when.
- [Encrypted memory for agents that run somewhere else: sgit deployment patterns, from a Mac mini to Kubernetes](encrypted-memory-for-isolated-agents.md) Agents in isolated, ephemeral places need memory that outlives them. Five sgit deployment patterns, from a Mac mini to Kubernetes, with ciphertext-only servers.
- [Memory is not a spectator sport: how a web of open sites, graphs and vaults became the memory for sessions like this one](memory-is-not-a-spectator-sport.md) Agentic memory as context management: many published, fractal, provenance-carrying memories rather than one store, shown in the session that wrote the article.
- [The Mandate Stack: a multi-agent system in production, layer by layer](the-mandate-stack.md) A multi-agent system that runs a business every few hours: eight layers, one written mandate per agent, everything a graph, one human who sends.
- [Footprint and blast radius: what the agent actually did, and what it would have cost](footprint-and-blast-radius.md) Footprint is what an agent actually did, read afterwards from logs and vault history; blast radius is what a row of its reach would cost the business today.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 93 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=93)

**Posting this article on LinkedIn?** The cover is [the-records-ran-out.jpg](banners/the-records-ran-out.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-records-ran-out.html)*
