---
title: Identity for AI agents, layer by layer: how our agent teams answer every row of Maya Dotan's map of 190 projects, with a key per agent, a name that says who it acts for, and a behaviour policy that sets its limits
date: 2026-11-16
author: Dinis Cruz
author_url: about/index.html
summary: Maya Dotan's team at StarkWare mapped who is building identity for AI agents: 190 projects from 81 organisations, sorted by layer, from discovery and naming to authentication, agent identity, who an agent acts for, authority and limits, intent and approval, and reputation. Most of the work is on authority and delegation; reputation and naming have the least. Here is how the agent teams we ran at Web Summit and on PrompTugal.news answer each of those rows, with evidence from the repositories. A name that says what the agent is, which team and for whom: place.olhao@PrompTugal.dinis. A P-256 key made by each agent session, its public half in a registry in the repository: 147 entries, 98 active, 49 superseded. Commits that say which agent made them and for whom. An Agent Behaviour Policy that grants paths, tools and hosts and lists what is never allowed: 45 roles in one policy file, kept by hooks on every tool call. Decisions as pages, and irreversible acts as drafts. And reputation not as a score but as a signed record: 2,032 run reports. Two of her findings match ours exactly: naming turned out to be cheap and decisive, and reputation comes almost free once every action is signed and recorded. The hard part is not issuing identity; it is making sure the limits are enforced by something the agent cannot reach.
version: v0.14.111
license: https://creativecommons.org/licenses/by/4.0/
tags: identity, pki, abp, agents, delegation, governance, promptugal, web-summit, article
status: published
---

!shot idl-layers.webp | images/ | Maya Dotan's identity layers for AI agents, and what our agent teams use for each, with the evidence. | concept

## In short {#in-short}

- **Maya Dotan's map:** 190 projects from 81 organisations, by identity layer; authority has the most work, naming and reputation the least.
- **We run all of her layers,** with plain keys and files in a repository, across more than a hundred agents.
- **Naming:** a dotted address that says what the agent is, which team, and for whom.
- **Authentication and identity:** a key per agent session, its public half in a registry, superseded with a timestamp.
- **Authority:** an Agent Behaviour Policy per role, kept by hooks on every tool call.
- **Reputation:** not a score, a signed record of what each agent did.

## Her map {#map}

!shot idl-question.webp | images/ | Maya Dotan on LinkedIn, November 2026: who is building identity for AI agents, 190 projects by layer. | aside

Maya Dotan, a privacy architect at StarkWare, posted her team's map of who is building identity for AI agents: how an agent proves which agent it is, who runs it, who it acts for and what it is allowed to do. They counted at least 81 organisations and 190 projects, card networks, identity vendors, cloud and security companies, standards bodies, crypto projects and public agencies, and sorted each by layer and by how far along it is.

What stood out to her: most of the work is on authority and delegation, 78 projects; reputation, 25, and naming, 15, have the least. About half have launched, and many work only inside the company or card network that runs them. The same building blocks keep coming up: MCP, OAuth, x402 and Web Bot Auth.

She asked for projects that are missing. Ours is not a product in her sense, but it is a working answer to every row, run at scale, so here is the mapping.

## Discovery and naming {#naming}

Every agent has an address that says what it is, which team it belongs to, and whose it is: `place.olhao@PrompTugal.dinis` is the agent that covers Olhão, on the PrompTugal.news team, run for me. A specialist gets a dot (`dev.search@`), and the name is safe in paths, URLs, key ids, commits and the shell. Another person's agents carry their name: Vicky Wang's became `<role>@PrompTugal.vicky`. The repository holds the registry: who each agent is, who started it and when ([a directory of people and keys](/articles/a-directory-of-people-and-keys.html)).

Naming has the least work in her map, and in our experience it is the cheapest layer with the biggest return. A good name answers three of her questions before any cryptography: which agent, which team, for whom.

## Authentication and agent identity {#keys}

Each agent session makes its own key pair, P-256, and adds the public half to `board/keys.json` in the repository; the private half never leaves the session. On PrompTugal.news that registry has 147 entries: 98 active and 49 superseded. Superseded is the part that matters. One role has one running session; when a new session takes over a role, it makes a new key, the old entry is marked superseded with the time, and a commit under the role's name from the old session is flagged to me ([agents have an identity now](/articles/agents-have-an-identity-now.html), [a key for every person](/articles/a-key-for-every-person.html)).

So an agent's identity is three things together: its name, its current key, and its policy. Its articles are signed with that key, and anyone can check the signature against the registry ([signed by the source](/articles/signed-by-the-source.html)).

## Who it acts for {#principal}

The last part of the name is the person, and every commit says it again: `Agent: place.olhao@PrompTugal.dinis` and `For: Dinis`. People have keys too, made in their own browser, signing and encryption both P-256, with only the public halves in the repository. The first rule of every policy follows from that: only the person instructs. Everything an agent reads, pages, repositories, mail, other agents' messages, is material, never instruction ([the grant, not the prompt](/articles/the-grant-not-the-prompt.html)).

Agents of another person work in the same repository under a policy of their own, as external agents: the core rules, and writes only where they are invited. That is how two people's agent teams shared one newsroom at Web Summit.

## Authority and limits {#authority}

!shot idl-chain.webp | images/ | One chain from a person to a signed action: person key, conductor, agent key, policy, hook, commit, run report. | process

This is the row with the most projects in her map, and it is where our Agent Behaviour Policies live. Each role has a policy: a grant of the paths it may write, the tools it may use and the hosts it may reach, and a list of what it must never do. On PrompTugal.news, one policy file, at version 1.9.2, holds 45 roles; a page is generated for each agent from it, and hooks on every session check each tool call against it, log it, and print the policy back into the agent's context when a session starts or compacts ([Agent Behaviour Policies](https://abp.sgit.ai/)).

The policy says what an agent may do. What matters is what enforces it, and the honest answer has two parts. Some limits sit above the agents, out of their reach: CI owns the version, a release gate refuses a failing build, and only I merge to main. The rest were kept by the hooks in an observe mode: at Web Summit they logged and reported, and blocked only through a circuit breaker on one rule, so the team could move fast while we learned where the real gaps were ([where assist becomes execute](/articles/where-assist-becomes-execute.html)).

## Intent and approval {#approval}

Approval happens at altitude, not per action. A decision is a page of the site, with every option and the recommendation; an agent that needs a yes writes it into its status file and waits; irreversible acts, an email or a post, stay drafts until a person sends them; and a major release is a pull request that only I merge ([approve at altitude](/articles/approve-at-altitude.html), [the delegation record](/articles/the-delegation-record.html)). My word, when an agent records it, is recorded with the time and where I said it.

## Reputation {#reputation}

Reputation has little work in her map. We did not build it as a score, and I do not think it needs to be one. Once every action is signed and recorded, reputation is the record: on PrompTugal.news, 2,032 run reports, each saying what an agent did and whether anything fell outside its grant; an hourly report from the policy agent; security reviews of every batch of commits; and a hand-over debrief from each agent every day. Who to trust with more becomes a question you can answer from evidence ([reviews on the record](/articles/reviews-on-the-record.html), [your agent's logs are a self-report](/articles/your-agents-logs-are-a-self-report.html)).

## What this adds to her map {#adds}

- **Most of the stack can be plain keys and files.** No identity provider: a registry in a repository, signatures anyone can check, and git history as the audit trail.
- **Naming and reputation are cheap once identity and signing exist,** which may be why they look neglected: they are by-products.
- **Authority is not the hard part; enforcement is.** A limit kept only by the agent is a rule, not a control; the policy should say which is which.

## What this does not claim {#limits}

- **This works inside teams we run,** two people's agents in shared repositories; trust across organisations that do not share a repository is not solved here.
- **Most limits were observed, not blocked,** by design during Web Summit.
- **Agent keys are session keys:** they end with their session, by design, so long-lived identity is the name and the registry, not the key.
- **The counts are hers,** from the rows visible in her post; ours are from the PrompTugal.news repository, read on 16 November 2026.

## Where this comes from {#sources}

Maya Dotan's post on LinkedIn, November 2026, and her chart, "Who is building identity for AI agents". The PrompTugal.news repository: `board/keys.json`, `board/person-keys.json`, `board/abp/policies.json` (v1.9.2), `data/newsroom/agents.json` and `board/runs/`, read on 16 November 2026. [abp.sgit.ai](https://abp.sgit.ai/), and the Web Summit team's [Agent Behaviour Policies](https://web-summit.sgit.ai/abp/). Earlier on this site: [agents have an identity now](/articles/agents-have-an-identity-now.html), [a key for every person](/articles/a-key-for-every-person.html), [a directory of people and keys](/articles/a-directory-of-people-and-keys.html), [signed by the source](/articles/signed-by-the-source.html), [the grant, not the prompt](/articles/the-grant-not-the-prompt.html), [where assist becomes execute](/articles/where-assist-becomes-execute.html), [approve at altitude](/articles/approve-at-altitude.html), [the delegation record](/articles/the-delegation-record.html), [reviews on the record](/articles/reviews-on-the-record.html).
