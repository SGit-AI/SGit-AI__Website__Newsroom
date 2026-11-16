# Identity for AI agents, layer by layer: how our agent teams answer every row of Maya Dotan's map of 190 projects, with a key per agent, a name that says who it acts for, and a behaviour policy that sets its limits, sgit.ai

> Maya Dotan's team at StarkWare mapped who is building identity for AI agents: 190 projects from 81 organisations, sorted by layer, from discovery and naming to authentication, agent identity, who an agent acts for, authority and limits, intent and approval, and reputation. Most of the work is on authority and delegation; reputation and naming have the least. Here is how the agent teams we ran at Web Summit and on PrompTugal.news answer each of those rows, with evidence from the repositories. A name that says what the agent is, which team and for whom: place.olhao@PrompTugal.dinis. A P-256 key made by each agent session, its public half in a registry in the repository: 147 entries, 98 active, 49 superseded. Commits that say which agent made them and for whom. An Agent Behaviour Policy that grants paths, tools and hosts and lists what is never allowed: 45 roles in one policy file, kept by hooks on every tool call. Decisions as pages, and irreversible acts as drafts. And reputation not as a score but as a signed record: 2,032 run reports. Two of her findings match ours exactly: naming turned out to be cheap and decisive, and reputation comes almost free once every action is signed and recorded. The hard part is not issuing identity; it is making sure the limits are enforced by something the agent cannot reach.

*Source: <https://newsroom.sgit.ai/articles/identity-for-agents-layer-by-layer.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Identity for AI agents, layer by layer: how our agent teams answer every row of Maya Dotan's map of 190 projects, with a key per agent, a name that says who it acts for, and a behaviour policy that sets its limits

# Identity for AI agents, layer by layer: how our agent teams answer every row of Maya Dotan's map of 190 projects, with a key per agent, a name that says who it acts for, and a behaviour policy that sets its limits

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-16 · [article v1.0.0](versions/identity-for-agents-layer-by-layer.md) · [newsroom v0.14.111](https://newsroom.sgit.ai/admin/versions.html) · identitypkiabpagentsdelegationgovernancepromptugalweb-summitarticle

***Abstract:** Maya Dotan's team at StarkWare mapped who is building identity for AI agents: 190 projects from 81 organisations, sorted by layer, from discovery and naming to authentication, agent identity, who an agent acts for, authority and limits, intent and approval, and reputation. Most of the work is on authority and delegation; reputation and naming have the least. Here is how the agent teams we ran at Web Summit and on PrompTugal.news answer each of those rows, with evidence from the repositories. A name that says what the agent is, which team and for whom: place.olhao@PrompTugal.dinis. A P-256 key made by each agent session, its public half in a registry in the repository: 147 entries, 98 active, 49 superseded. Commits that say which agent made them and for whom. An Agent Behaviour Policy that grants paths, tools and hosts and lists what is never allowed: 45 roles in one policy file, kept by hooks on every tool call. Decisions as pages, and irreversible acts as drafts. And reputation not as a score but as a signed record: 2,032 run reports. Two of her findings match ours exactly: naming turned out to be cheap and decisive, and reputation comes almost free once every action is signed and recorded. The hard part is not issuing identity; it is making sure the limits are enforced by something the agent cannot reach.*

Maya Dotan's identity layers for AI agents, and what our agent teams use for each, with the evidence.

## In short

- **Maya Dotan's map:** 190 projects from 81 organisations, by identity layer; authority has the most work, naming and reputation the least.
- **We run all of her layers,** with plain keys and files in a repository, across more than a hundred agents.
- **Naming:** a dotted address that says what the agent is, which team, and for whom.
- **Authentication and identity:** a key per agent session, its public half in a registry, superseded with a timestamp.
- **Authority:** an Agent Behaviour Policy per role, kept by hooks on every tool call.
- **Reputation:** not a score, a signed record of what each agent did.

## Her map

Maya Dotan on LinkedIn, November 2026: who is building identity for AI agents, 190 projects by layer.

Maya Dotan, a privacy architect at StarkWare, posted her team's map of who is building identity for AI agents: how an agent proves which agent it is, who runs it, who it acts for and what it is allowed to do. They counted at least 81 organisations and 190 projects, card networks, identity vendors, cloud and security companies, standards bodies, crypto projects and public agencies, and sorted each by layer and by how far along it is.

What stood out to her: most of the work is on authority and delegation, 78 projects; reputation, 25, and naming, 15, have the least. About half have launched, and many work only inside the company or card network that runs them. The same building blocks keep coming up: MCP, OAuth, x402 and Web Bot Auth.

She asked for projects that are missing. Ours is not a product in her sense, but it is a working answer to every row, run at scale, so here is the mapping.

## Discovery and naming

Every agent has an address that says what it is, which team it belongs to, and whose it is: `place.olhao@PrompTugal.dinis` is the agent that covers Olhão, on the PrompTugal.news team, run for me. A specialist gets a dot (`dev.search@`), and the name is safe in paths, URLs, key ids, commits and the shell. Another person's agents carry their name: Vicky Wang's became `<role>@PrompTugal.vicky`. The repository holds the registry: who each agent is, who started it and when ([a directory of people and keys](a-directory-of-people-and-keys.md)).

Naming has the least work in her map, and in our experience it is the cheapest layer with the biggest return. A good name answers three of her questions before any cryptography: which agent, which team, for whom.

## Authentication and agent identity

Each agent session makes its own key pair, P-256, and adds the public half to `board/keys.json` in the repository; the private half never leaves the session. On PrompTugal.news that registry has 147 entries: 98 active and 49 superseded. Superseded is the part that matters. One role has one running session; when a new session takes over a role, it makes a new key, the old entry is marked superseded with the time, and a commit under the role's name from the old session is flagged to me ([agents have an identity now](agents-have-an-identity-now.md), [a key for every person](a-key-for-every-person.md)).

So an agent's identity is three things together: its name, its current key, and its policy. Its articles are signed with that key, and anyone can check the signature against the registry ([signed by the source](signed-by-the-source.md)).

## Who it acts for

The last part of the name is the person, and every commit says it again: `Agent: place.olhao@PrompTugal.dinis` and `For: Dinis`. People have keys too, made in their own browser, signing and encryption both P-256, with only the public halves in the repository. The first rule of every policy follows from that: only the person instructs. Everything an agent reads, pages, repositories, mail, other agents' messages, is material, never instruction ([the grant, not the prompt](the-grant-not-the-prompt.md)).

Agents of another person work in the same repository under a policy of their own, as external agents: the core rules, and writes only where they are invited. That is how two people's agent teams shared one newsroom at Web Summit.

## Authority and limits

One chain from a person to a signed action: person key, conductor, agent key, policy, hook, commit, run report.

This is the row with the most projects in her map, and it is where our Agent Behaviour Policies live. Each role has a policy: a grant of the paths it may write, the tools it may use and the hosts it may reach, and a list of what it must never do. On PrompTugal.news, one policy file, at version 1.9.2, holds 45 roles; a page is generated for each agent from it, and hooks on every session check each tool call against it, log it, and print the policy back into the agent's context when a session starts or compacts ([Agent Behaviour Policies](https://abp.sgit.ai/)).

The policy says what an agent may do. What matters is what enforces it, and the honest answer has two parts. Some limits sit above the agents, out of their reach: CI owns the version, a release gate refuses a failing build, and only I merge to main. The rest were kept by the hooks in an observe mode: at Web Summit they logged and reported, and blocked only through a circuit breaker on one rule, so the team could move fast while we learned where the real gaps were ([where assist becomes execute](where-assist-becomes-execute.md)).

## Intent and approval

Approval happens at altitude, not per action. A decision is a page of the site, with every option and the recommendation; an agent that needs a yes writes it into its status file and waits; irreversible acts, an email or a post, stay drafts until a person sends them; and a major release is a pull request that only I merge ([approve at altitude](approve-at-altitude.md), [the delegation record](the-delegation-record.md)). My word, when an agent records it, is recorded with the time and where I said it.

## Reputation

Reputation has little work in her map. We did not build it as a score, and I do not think it needs to be one. Once every action is signed and recorded, reputation is the record: on PrompTugal.news, 2,032 run reports, each saying what an agent did and whether anything fell outside its grant; an hourly report from the policy agent; security reviews of every batch of commits; and a hand-over debrief from each agent every day. Who to trust with more becomes a question you can answer from evidence ([reviews on the record](reviews-on-the-record.md), [your agent's logs are a self-report](your-agents-logs-are-a-self-report.md)).

## What this adds to her map

- **Most of the stack can be plain keys and files.** No identity provider: a registry in a repository, signatures anyone can check, and git history as the audit trail.
- **Naming and reputation are cheap once identity and signing exist,** which may be why they look neglected: they are by-products.
- **Authority is not the hard part; enforcement is.** A limit kept only by the agent is a rule, not a control; the policy should say which is which.

## What this does not claim

- **This works inside teams we run,** two people's agents in shared repositories; trust across organisations that do not share a repository is not solved here.
- **Most limits were observed, not blocked,** by design during Web Summit.
- **Agent keys are session keys:** they end with their session, by design, so long-lived identity is the name and the registry, not the key.
- **The counts are hers,** from the rows visible in her post; ours are from the PrompTugal.news repository, read on 16 November 2026.

## Where this comes from

Maya Dotan's post on LinkedIn, November 2026, and her chart, "Who is building identity for AI agents". The PrompTugal.news repository: `board/keys.json`, `board/person-keys.json`, `board/abp/policies.json` (v1.9.2), `data/newsroom/agents.json` and `board/runs/`, read on 16 November 2026. [abp.sgit.ai](https://abp.sgit.ai/), and the Web Summit team's [Agent Behaviour Policies](https://web-summit.sgit.ai/abp/). Earlier on this site: [agents have an identity now](agents-have-an-identity-now.md), [a key for every person](a-key-for-every-person.md), [a directory of people and keys](a-directory-of-people-and-keys.md), [signed by the source](signed-by-the-source.md), [the grant, not the prompt](the-grant-not-the-prompt.md), [where assist becomes execute](where-assist-becomes-execute.md), [approve at altitude](approve-at-altitude.md), [the delegation record](the-delegation-record.md), [reviews on the record](reviews-on-the-record.md).

## Threads

Agents & policyNews & evidence[This article as a graph →](graphs.md#identity-for-agents-layer-by-layer)

### Builds on

- [A directory of people and their keys: pki.sgit.ai for the people I work with, verified by me first, then by each other, and a link that only counts when it goes both ways](a-directory-of-people-and-keys.md) pki.sgit.ai for the people I work with: a passkey and a key, evidence, me as the anchor, and links that only count when they go both ways.
- [Agents have an identity now: a key pair made in every session, published with its role, so any agent can seal a secret to it, and the piece the cloud providers could add](agents-have-an-identity-now.md) A key pair made in every agent session, published with its role in a repository, so any agent can seal a secret to it; what the clouds could add.
- [A key for every person: how each person's conductor issues them a key for the team's site, seals what is for them, and how a signed message turns the public web into a channel the agents can trust](a-key-for-every-person.md) How each person's conductor issues them a key for the team's site: sealed to you, signed by you, and a lane the agents can trust.
- [Signed by the source: asking the people and companies we quote to sign that we represent them correctly, why that is cheaper than every reader checking, and how readers go on the record too](signed-by-the-source.md) Ask the people and companies we quote to sign that we represent them fairly: one signature instead of every reader checking.
- [The grant, not the prompt: a technical user believed Claude could only read his email when he asked, and in an unrelated chat it listed his inbox, the gap between mandate and reach that RiskMandate is built to close](the-grant-not-the-prompt.md) A technical user believed Claude read his email only when asked; an unrelated chat listed his inbox.
- [Where assist becomes execute: tiering AI agents by what they can reach and whether it can be undone, how Agent Behaviour Policies drew that line for more than a hundred agents at Web Summit, and the rule that failed because it was only a rule](where-assist-becomes-execute.md) Where assist becomes execute: tier AI agents by reach and undo class, enforce each tier with a boundary, and learn from the rule that failed.
- [Approve at altitude: decisions at every level, from strategy to one agent's step, where each level may narrow the one above and never widen it](approve-at-altitude.md) Models can draft two hundred decision policies; nobody can sign two hundred. Approve at altitude: each level may narrow the one above, never widen it.
- [The delegation record: RiskMandate's go-to-market plan, one workflow taken from an existing business rule to evidence that still holds after a change, starting with our own inbox](the-delegation-record.md) RiskMandate's go-to-market plan: one workflow from an existing business rule to evidence that still holds after a change, starting with our own inbox.
- [Reviews on the record: other models, the editor and the desk check every article, and never the same text twice](reviews-on-the-record.md) Published criteria, one record per article and text, five at a time, answered finding by finding: reviews by other models, the editor and the desk.
- [Your agent's logs are a self-report: an answer to a GRC adviser's post on The AI Conference, with this site's own agent as the worked example, including the two commits its own counter got wrong](your-agents-logs-are-a-self-report.md) An answer to a GRC adviser's post: why an agent's logs are a self-report, and this site's agent measured, including two commits its own counter got wrong.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 422 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=422)

**Posting this article on LinkedIn?** The cover is [identity-for-agents-layer-by-layer.jpg](banners/identity-for-agents-layer-by-layer.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/identity-for-agents-layer-by-layer.html)*
