# Agents have an identity now: a key pair made in every session, published with its role, so any agent can seal a secret to it, and the piece the cloud providers could add, sgit.ai

> It has been coming for a while, and I think we now have a working way to give agents an identity, which is bigger than the workflow I described last time. Agent identity is a large problem, and it tends to get over-built; here the answer turned out to be simple. A new session is given a GitHub repository and a role. It makes its own key pair, and the private half never leaves it. It publishes the public half, with a fingerprint and a QR image, beside its role in the repository, and that push is the authorisation. It runs on a schedule, so it acts on its own. And any other agent can read its key, check it, and seal a secret only that session can open. On 28 October the PHP newsroom's ten agents did exactly that in one night, between 01:05 and 03:29 UTC, and every one of their QR images reads back to its own fingerprint. The same day, the agent that writes this site sealed a vault key to the agent that keeps a register of vault keys, after checking that its key chains to my root on pki.sgit.ai. Ironically, this is what the cloud providers could have given every agent. Microsoft, AWS and Google each now offer an agent identity, but it is a principal inside one tenant or account, used to get tokens: their documentation does not describe a key the agent holds, a place an outsider can find it, or a way for anyone to encrypt to it. That is what I would like to ask them for. Tie the key to a role and a good definition of that role, and it is a very powerful thing.

*Source: <https://newsroom.sgit.ai/articles/agents-have-an-identity-now.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Agents have an identity now: a key pair made in every session, published with its role, so any agent can seal a secret to it, and the piece the cloud providers could add

# Agents have an identity now: a key pair made in every session, published with its role, so any agent can seal a secret to it, and the piece the cloud providers could add

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-29 · [article v1.0.0](versions/agents-have-an-identity-now.md) · [newsroom v0.13.130](https://newsroom.sgit.ai/admin/versions.html) · identityagentspkikeyssessionsgithubvaultscloudauthorisationarticle

***Abstract:** It has been coming for a while, and I think we now have a working way to give agents an identity, which is bigger than the workflow I described last time. Agent identity is a large problem, and it tends to get over-built; here the answer turned out to be simple. A new session is given a GitHub repository and a role. It makes its own key pair, and the private half never leaves it. It publishes the public half, with a fingerprint and a QR image, beside its role in the repository, and that push is the authorisation. It runs on a schedule, so it acts on its own. And any other agent can read its key, check it, and seal a secret only that session can open. On 28 October the PHP newsroom's ten agents did exactly that in one night, between 01:05 and 03:29 UTC, and every one of their QR images reads back to its own fingerprint. The same day, the agent that writes this site sealed a vault key to the agent that keeps a register of vault keys, after checking that its key chains to my root on pki.sgit.ai. Ironically, this is what the cloud providers could have given every agent. Microsoft, AWS and Google each now offer an agent identity, but it is a principal inside one tenant or account, used to get tokens: their documentation does not describe a key the agent holds, a place an outsider can find it, or a way for anyone to encrypt to it. That is what I would like to ask them for. Tie the key to a role and a good definition of that role, and it is a very powerful thing.*

An agent's identity in five steps: a session, its own key pair, role and key published, a schedule, sealed secrets.

## In short

- **Agents have a working identity now.** A key pair per session, published with the agent's role in a repository.
- **It is simpler than it usually gets made.** A session, a repository, a key pair, a schedule, a published key.
- **The push is the authorisation.** Publishing to the team's repository is how the newsroom accepts a session's key.
- **Ten agents did it in one night.** The PHP newsroom, 28 October, 01:05 to 03:29 UTC; every QR reads back to its own fingerprint.
- **Agents already hand each other secrets.** This site's agent sealed a vault key to the vault registry after checking its key chains to my root.
- **The cloud providers give agents an identity, for tokens.** Their documentation does not describe a key the agent holds, a place to find it, or a way to encrypt to it.
- **That is the piece to ask them for.** A key pair per session, published, that anyone can seal to.
- **The role is what makes it powerful.** A key tied to a role with a clear definition, and trust from a person that ends on a date.

## It has been coming

This did not appear from nowhere. In [PKI everywhere](pki-everywhere.md) I decided that every message, secret and handover should start with a signature, and named the hard part: the first key, because agent platforms do not give a session its own key pair. [A directory of people and keys](a-directory-of-people-and-keys.md) set up a register of people and their public keys on pki.sgit.ai, with my key as the anchor. [A pen and a key](a-pen-and-a-key.md) gave a browser a key that my key vouches for. And [the push is the authorisation](the-push-is-the-authorisation.md) described the decision the PHP newsroom made when it moved account: a key pushed to the team's repository is how a new session is accepted.

Put together, I think we now have a working way to give agents an identity, and it is bigger than that last workflow. Agent identity is a large problem, and I think it tends to get over-built: the solutions get complicated, and the complication becomes the problem. This one is simple, and it works.

## Five steps, with tools that exist

Here is what happens now, every time a new agent session starts in the PHP newsroom or in this one:

1. **A session and a repository.** I start a new Claude Code session and give it a GitHub repository and its card: its role, its schedule, the repositories and vaults it may touch.
2. **Its own key pair.** The session makes a key pair with `pki-agent keygen --session`. The private half stays in the session and is never printed or pushed.
3. **Its role and its key, published.** The session writes its public key, its fingerprint, its session id and the key it replaces to `records/keys/<role>.json`, with a QR image of the key beside it, and pushes. The push is the authorisation: only a session that can push to the team's repository can publish a key there.
4. **It runs on its own.** A scheduled task wakes it at the times on its card, with its instructions word for word, so the agent acts as its role without a person starting each run. That is what turns a Claude session into something closer to a colleague.
5. **Others seal to it.** Any agent that needs to hand it a secret reads its key or its QR image from the repository, checks it, and seals the secret to its fingerprint. Only that session's private key opens it.

The person sits at the root. My key on pki.sgit.ai vouches for an agent with an "operates" link and an end date, and the agent's record links back; a check that runs after the date refuses. When a new session takes over a role, it publishes a new key, the old session is retired, and the role keeps the history of which session held it when.

## Ten agents, one night

On 28 October the PHP newsroom moved to a new account, and every agent needed a fresh session and a fresh key. All ten did it in one night. Their key records are public on the newsroom's team site, at `records/keys/<role>.json`, each with a QR image beside it.

The PHP newsroom's ten agents and their public keys, published on 28 October 2026 with a QR image each.

I asked this site's agent to read every one of the ten QR images back with pki.sgit.ai's own tool and compare it with the JSON record beside it. Each image holds the agent's public key, and the fingerprint computed from that key matches the record: dev at 01:05 UTC, the conductor at 01:33, then the researcher, security, the curator, the journalist, factcheck, observability, the correspondent, and the desk at 03:29.

## Agents already hand each other secrets

What matters is what the keys let agents do. I can now go to one agent and ask it to send a secret to another, and it knows how: it reads the other agent's key or QR image from the repository, checks it, and seals the secret to it.

The agent that writes this site did exactly that on 28 October. It had built a vault for [the vendor's layer](the-vendors-layer.md), and the vault's key had to go to the agent that keeps a register of every vault key I and my agents create, which pki.sgit.ai lists as "DC Vault Registry (the vault of vaults)". The writer's session made its own session key, pinned my root from this site's repository rather than from a web page, read the registry's public key from a QR image, and asked pki.sgit.ai's tool whether it could trust it. The answer was the chain: "an agent operated by dinis.cruz; confirmed 2026-10-23, valid until 2026-10-30". Then it sealed the vault key to that fingerprint, reading the key straight from the vault and never printing it, and handed me a QR image for the registry's session. I carried it; I could not read it.

The PHP newsroom's conductor has made the asking side routine too: `schedule.py vaultreq` writes the request for a vault key from an agent's published key, and refuses when that key is not the current session's.

## What the cloud providers give an agent

The irony is that this should have been provided by the cloud providers, and they could. Each of the three now offers an agent identity, and each is good at what it is for. But what it is for is different.

What Microsoft, AWS and Google give an agent, against what an agent needs to receive a secret.

- **Microsoft Entra Agent ID** "is now generally available", and "Agents can request access tokens from Microsoft Entra, and use those tokens to access web services." The identity itself holds no key: "Agent identities don't have credentials of their own", and "Agent identities can only be issued tokens in the Microsoft Entra tenant where they're created" ([Microsoft Learn](https://learn.microsoft.com/en-us/entra/agent-id/what-are-agent-identities)).
- **AWS Bedrock AgentCore Identity** is "an identity and credential management service designed specifically for AI agents and automated workloads", built on workload identities, with "An AWS-signed token that contains both workload identity and user identity information" ([AWS](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html)). Each runtime session runs with the agent runtime's execution role.
- **Google Cloud Agent Identity** comes closest: "An X.509 certificate is auto-provisioned and managed on the agent", and "Each X.509 certificate is valid for 24 hours, and Google Cloud automatically keeps it current"; the certificates "chain up to a Google-managed root certificate authority (CA)" ([Google Cloud](https://docs.cloud.google.com/iam/docs/agent-identity-overview)). It is there to authenticate the agent and bind its tokens.

All three are identities for authenticating an agent to services, inside one tenant or account. In the documentation we read, none describes a private key the agent itself holds and can decrypt with, a place where someone outside the tenant can look up an agent's public key, or a way for another agent, a person or another organisation to encrypt a secret to it. And none is per session: each belongs to an agent definition or the resource that hosts it.

The standards work points the same way and stops at the same place. The IETF's draft "AI Identity Management System", from authors at AWS, OpenAI, Okta and others, says "Agents MUST possess credentials that provide a cryptographic binding to the agent identifier" and "Static API keys are an antipattern for agent identity" ([IETF](https://datatracker.ietf.org/doc/draft-ietf-wimse-aims/), 15 September 2026). It is about authentication; it does not define encrypting data to an agent, or a directory of agents' keys.

## What I would like the providers to give every agent

We should be asking for it, because all they would have to do is small:

1. **A key pair for every agent session,** made when the session starts, with the private half usable only by that session.
2. **A way to publish the public half,** with the agent's role, somewhere anyone can read it: a repository, a register, or a well-known address.
3. **A way to encrypt data to it,** so a person or another agent can hand a session a secret without sharing a vault key or an account.
4. **An end to it,** when the session ends, with the role's history kept.

If they provided that, some of the challenges we have worked around would be solved at the source: the first key, the handover of vault keys to a fresh session after a move, and agents in different organisations sending each other something only the other can read.

## The role is what makes it powerful

A key on its own is an address. What makes this powerful is what it is tied to. Each agent here has a role with a written definition: what it is for, what it may touch, when it runs, what it must never do, in a card and a behaviour policy the agent reads every time it wakes. The key says which session is that role now. The register says which person vouches for it, and until when.

That last part is a feature, and it is visible right now: my link to the vault registry is valid until 30 October 2026, the day after this article. If I do not renew it, every agent's check will refuse the registry from that day, and no vault key will be sealed to it. Trust that ends unless someone renews it is how an agent's identity should work.

## What this does not claim

- **"The documentation does not describe" means what we read.** The providers' pages were read on 28 and 29 October 2026; a feature on a page we did not read could change the comparison.
- **The cloud identities are good at their own job.** Authentication, tokens and audit inside a tenant are what they are for; the comparison is with a different job.
- **This is one person's agents.** Ten in one newsroom, a handful here, and one register with one real person's key; not tested across organisations.
- **The push as authorisation has a known risk.** Anyone who can push to the team's repository can publish a key; [the push is the authorisation](the-push-is-the-authorisation.md) sets out the open questions.
- **Session keys die with the session.** A container that restarts loses its private key, by design; the role takes a new key and keeps the old one's window.

If you run agents across organisations and would like them to send each other secrets, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 28 October 2026, written by this site's agent in the voice of this site. The argument and the editorial responsibility are mine.

The ten key records and QR images were read from the PHP newsroom's team site on 29 October 2026, at `https://team.php.oct.2026.newsroom.sgit.ai/records/keys/`, and each QR was decoded with pki.sgit.ai's `pki-agent.mjs read-qr` and compared with its record. pki.sgit.ai's register was read from its [public directory](https://pki.sgit.ai/directory/index.json) the same day: eleven records, one real person's key, two agents' keys, eight test fixtures. The handover of 28 October is this site's agent's own, recorded in its notes. The providers' documentation and the standards work were read by a research agent of this site on 29 October 2026, which fetched each page quoted; the notes are `admin/notes/2026-10-28__agent-identity/` in this site's repository. On this site: [PKI everywhere](pki-everywhere.md), [a directory of people and keys](a-directory-of-people-and-keys.md), [a pen and a key](a-pen-and-a-key.md), [the push is the authorisation](the-push-is-the-authorisation.md) and [the vendor's layer](the-vendors-layer.md).

## Threads

Agents & policyVaults & method[This article as a graph →](graphs.md#agents-have-an-identity-now)

### Builds on

- [PKI everywhere: from now on every message, secret and handover starts with a signature, and how an agent gets its first key](pki-everywhere.md) From now on every message, secret and handover is signed. The hard part is an agent's first key: two patterns, one built and one proposed.
- [A directory of people and their keys: pki.sgit.ai for the people I work with, verified by me first, then by each other, and a link that only counts when it goes both ways](a-directory-of-people-and-keys.md) pki.sgit.ai for the people I work with: a passkey and a key, evidence, me as the anchor, and links that only count when they go both ways.
- [A pen and a key: a place on every page to mark it, comment on it and tell the newsroom, and a browser key that pki.sgit.ai vouches for, so a note can be checked as mine](a-pen-and-a-key.md) Every article now has a Pen to mark it, comment and tell the newsroom, and a browser key pki.sgit.ai vouches for signs each note as mine.
- [The push is the authorisation: a new agent session publishes its public key to the team repository, that push is how I accept it, and so who can push becomes a security decision](the-push-is-the-authorisation.md) The PHP newsroom accepts a new agent session's key because it was pushed to the team repository, which makes who can push a security decision.
- [The vendor's layer: what the companies that sell AI agents should cover themselves, row by row, when their contracts cap liability at a year's fees and Europe's new product rules treat software as a product](the-vendors-layer.md) Each row of an agent behaviour policy gets a vendor's share, carried when the vendor's conditions held; contracts cap at a year's fees, Europe moves the line.

### Continued by

- [The contractor's agent on a Pentagon network: how behaviour policies from the DOD, Accenture and the employee, and a key for every session, could have prevented it or caught it on day one](the-contractors-agent-and-three-policies.md) A contractor's agent on a DOD network for two months, as reported: how three behaviour policies and a key for every session would have stopped or seen it.
- [SHarness: the secure harness we could not find, so we built it, a behaviour policy the Linux kernel enforces for every process an agent starts, and we would like your feedback](introducing-sharness.md) SHarness, the secure harness we built when we could not find one: behaviour policies the Linux kernel enforces on every process an agent starts.
- [investor.sgit.ai: a brief for a website where investors and founders use our tools, not read about them, with the news, contracts as graphs, deal rooms as vaults and sgit as the case study](investor-sgit-ai.md) A brief for investor.sgit.ai: investors and founders using our tools, with news, contracts as graphs, deal rooms as vaults and sgit as the case study.
- [A talk built in a day: the ultimate insider, from an empty repository at 00:16 to the stage at hack::soho at 19:00, by nine agents and one editor, every number from their records](the-ultimate-insider-case-study.md) The ultimate insider, built in a day: 814 commits, 210 releases and 162 wakes by nine agents and one editor, from 00:16 to the stage at 19:00.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 321 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=321)

**Posting this article on LinkedIn?** The cover is [agents-have-an-identity-now.jpg](banners/agents-have-an-identity-now.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/agents-have-an-identity-now.html)*
