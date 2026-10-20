---
title: PKI everywhere: from now on every message, secret and handover starts with a signature, and how an agent gets its first key
date: 2026-10-20
author: Dinis Cruz
author_url: about/index.html
summary: This is a strategic decision. From now on, every message, every secret and every transmission of data we make should be signed, and in some cases encrypted, with public key cryptography. Everything starts with a PKI handshake, including our first customers and the workflows we build for them. We are at a level of maturity where this is possible: pki.sgit.ai now has a register of people and their public keys, and since its v0.2.1 a workflow for an agent to get a key its operator confirms, with trust that runs both ways and has an end date. The hard part is the first key. As far as we found, no major agent platform gives an individual agent session its own key pair; what exists signs at the level of the platform. So there are two patterns, and we need both. In the first, the agent makes a key only it knows, sends the public half over an append lane, and a person compares fingerprints and approves it: that proves who is here now. In the second, the agent asks a central workflow, a person approves as a second step, and the agent receives an identity key that is made and held centrally: logged, revocable, and the same in the next session. A central store of the keys that give agents their identity is fine, and the agent can always make its own keys for its own work.
version: v0.12.155
license: https://creativecommons.org/licenses/by/4.0/
tags: pki, keys, agents, identity, security, sgit, article
status: published
---

!shot ke-patterns.webp | images/ | How an agent gets its first key: two patterns. A, the agent's own key, confirmed by a person comparing fingerprints, is built at pki.sgit.ai. B, an identity key issued and held centrally after a second-step approval, is proposed. | concept

## In short {#in-short}

- **Sign everything, encrypt where it matters.** Every message, secret and handover, from now on.
- **Everything starts with a PKI handshake.** Including our first customers and their workflows.
- **We are ready.** A register of people and keys, and an agent workflow, are live at pki.sgit.ai.
- **The hard part is the first key.** Agent platforms do not give a session its own key pair.
- **Pattern A: the agent's own key.** Made in the session, confirmed by a person, trusted both ways for a time.
- **Pattern B: an issued identity key.** Approved as a second step, held centrally, the same next session.
- **We need both.** One proves who is here now; the other gives an identity that lasts.

## The decision {#decision}

I think we are now at a level of maturity where we can push the idea that we should be using PKI everywhere. Every message, every secret, every transmission of data: signed, so we know who sent it and that it was not changed, and encrypted where it should be read only by the person or agent it is for.

It applies to everything. Our [first customers](/articles/our-first-customers.html) will start with a PKI handshake. So will the workflows we build for them, the sessions I run, and the agents in them. The aim is that "who said this?" always has an answer that can be checked, not one that has to be trusted.

This is not new for us in principle. [Secrets on public keys](/articles/secrets-on-public-keys.html) argued for giving every person, browser and agent a key pair and to stop sharing keys altogether. [Handing secrets to agents](/articles/handing-secrets-to-agents.html) tested it end to end: the agent makes its own key pair, the owner encrypts and signs, and the secret goes through a one-time drop. [sgit in a CI pipeline](/articles/sgit-in-a-ci-pipeline.html) gave every job its own key pair. What is new is that it is now the default, not the experiment.

## Why now: pki.sgit.ai {#pki}

The pieces are in place. [pki.sgit.ai](https://pki.sgit.ai/) is a register of people and their public keys, live since 19 October. Each record is a set of signed statements: who the person is, the evidence for it (a website, a GitHub account, a DNS record, a key), the links to other records, an inbox, and revocations. Its rule for links is the one from [a directory of people and keys](/articles/a-directory-of-people-and-keys.html): a link exists only when both records hold one. If I say I know you, that is my claim; you still have to say you know me.

Since v0.2.1 it also has a workflow for agents, in four commands. The agent makes a key, names its operator, and submits its public key, which is sealed into the operator's inbox, an append lane. Then the trust step, in the site's words: "The agent prints its fingerprint in its own session, where the operator is watching; the vault shows the fingerprint of the record that arrived; the operator compares the two." Once confirmed, the operator's record links to the agent with an end date, 30 days by default, and the agent's record links back. A session key is confirmed for a week. That is the two-way model, and I think it is a really powerful one: trust is a pair of statements, each signed by the party making it, and it expires.

It is early. As of today the register has one agent key, waiting for its operator, and no confirmed links yet. The site is clear that "Operated is not authorised": a confirmed agent has an identity, not permission. Permission is what an [Agent Behaviour Policy](https://abp.sgit.ai/) writes down.

## The first key {#first}

The interesting problem is how an agent gets its first key. Agents today are not given one. As far as we found, what the platforms offer signs at the level of the platform or the service, not the session: OpenAI's ChatGPT agent signs its web requests with HTTP message signatures under `Signature-Agent: chatgpt.com`, with keys published by chatgpt.com; the A2A protocol says agent cards "MAY be digitally signed"; MCP's authorisation is OAuth, which identifies a client. None of them gives a new Claude session, or a new ChatGPT session, a key pair of its own.

pki.sgit.ai calls the underlying problem [the bootstrap trap](https://pki.sgit.ai/bootstrap/index.html): "Creating a key is easy. Getting it recognised requires an identity you do not yet have". It is, in its words, "a loop, not a missing feature", and "the hardest part of agent identity is not cryptography but authority choreography". The way out of the loop is a person. So the question is the choreography: in what order, through which lane, with whom approving.

## Pattern A: the agent's own key {#own}

The untrusted party, say a new Claude session, makes a key pair. The private key is known only to that session. It is ephemeral: when the session ends, the key ends, and a new session makes a new one. The session sends its public key to another agent or workflow over an append lane, where it can be written but not changed, and a person verifies it on the other side by comparing fingerprints.

This is what pki.sgit.ai has built, and what it recommends for sessions: "nobody but the session ever holds it". It proves who is here now. Its limit is the same as its strength: nothing outlives the session, so the next session starts again, and the record of what the last one did is tied to a key that no longer exists.

## Pattern B: an issued identity key {#issued}

The second pattern starts the same way. The agent makes a session key pair and uses it to send a request, signed, to a central workflow. Then a person approves, as a second step, from another device: this agent, this job, this long. The workflow makes an identity key pair, keeps it, and sends it to the agent encrypted to the session's public key, so only that session can open it.

This has real advantages. Every key is issued, so every key is logged. The identity survives the session, so the next session can continue the work under the same name, and its history stays connected. Revoking one key in one place ends that identity everywhere. And it is fine to have a central repository of private keys, as long as what it holds is clear: the keys that give agents their identity, issued and revocable, not the agents' own secrets. The agent can always make another key for its own work.

pki.sgit.ai names the cost honestly. A key that lasts has to be kept somewhere, and "whoever sets the secret holds the key in custody". In pattern B the custodian is the central workflow, on purpose. That is a choice, made in the open, with the custodian named, and I think it is the right one for identities that need to last. For a session that only needs to prove it is here, pattern A is better.

## How the two fit {#fit}

They are not alternatives. Pattern A comes first in both: every session makes its own key. Pattern B is what a session asks for when it needs an identity that lasts. The rest of the industry is moving the same way for workloads: SPIFFE gives workloads short-lived identities, rotated "frequently and automatically"; Sigstore's Fulcio issues signing certificates "valid for 10 minutes" against an OpenID Connect identity; Let's Encrypt has offered six-day certificates since January 2026. Short-lived keys, issued by a workflow, after something has vouched for the requester. For agents, the thing that vouches is a person.

What we need to figure out now are the workflows: which lanes, which approvals, how long each kind of key lives, and what a customer's first handshake looks like. That is the next piece of work, and every workflow we build from here starts with it.

## What this does not claim {#limits}

- **Pattern B is proposed.** Pattern A is built; the issued identity key is not.
- **The register is new.** One agent key, no confirmed links, as of today.
- **Identity is not permission.** That is what a behaviour policy is for.
- **Platform support may change.** This is what we found on 20 October 2026.
- **Not every message needs encrypting.** Signing is the default; encryption where it should be private.

## Where this comes from {#sources}

A voice memo of 20 October 2026. [pki.sgit.ai](https://pki.sgit.ai/), its [article on keys for agents](https://pki.sgit.ai/articles/keys-for-agents.md) and its [bootstrap trap](https://pki.sgit.ai/bootstrap/index.html), read on 20 October 2026. OpenAI on [ChatGPT agent's signed requests](https://help.openai.com/en/articles/11845367); the [A2A specification](https://a2a-protocol.org/latest/specification/); [MCP authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization); [SPIFFE concepts](https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/); [Sigstore's Fulcio](https://docs.sigstore.dev/certificate_authority/overview/); [Let's Encrypt on six-day certificates](https://letsencrypt.org/2026/01/15/6day-and-ip-general-availability.html). Related: [secrets on public keys](/articles/secrets-on-public-keys.html), [handing secrets to agents](/articles/handing-secrets-to-agents.html), [a directory of people and keys](/articles/a-directory-of-people-and-keys.html), [sgit in a CI pipeline](/articles/sgit-in-a-ci-pipeline.html), [the editor's channel](/articles/the-editors-channel.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
