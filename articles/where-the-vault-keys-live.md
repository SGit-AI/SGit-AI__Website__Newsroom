# Where the vault keys live: key management at sgit-ai v0.20.0, and what comes next, sgit.ai

> Every vault on this site is encrypted in the client, so the server never sees a key and the key is the whole question. This is the current state of vault key management at sgit-ai v0.20.0: where everything lives, the one secret and the keys derived from it, where vault keys are kept today (a password manager, and a registry vault run by an isolated agent session), how a new key reaches the registry without ever entering a chat, append lanes as the transport behind most of it, the small communication vaults that made the problem urgent, and the four tracks that come next: password manager integrations, secrets.sgit.ai's passkey-unlocked keyring, PKI, and decryption that happens out of band. Plus the one gap we cannot close ourselves: agent platforms have no per-session secrets.

*Source: <https://newsroom.sgit.ai/articles/where-the-vault-keys-live.html> · sgit.ai v0.7.45 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Where the vault keys live: key management at sgit-ai v0.20.0, and what comes next

# Where the vault keys live: key management at sgit-ai v0.20.0, and what comes next

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-10 · [article v1.1.0, 2 versions](versions/where-the-vault-keys-live.md) · [sgit.ai v0.7.32](https://sgit.ai/admin/versions.md) · sgitvault-keyskey-managementsecretsappend-lanespkipasskeyspassword-managersagentsarticle

***Abstract:** Every vault on this site is encrypted in the client, so the server never sees a key and the key is the whole question. This is the current state of vault key management at sgit-ai v0.20.0: where everything lives, the one secret and the keys derived from it, where vault keys are kept today (a password manager, and a registry vault run by an isolated agent session), how a new key reaches the registry without ever entering a chat, append lanes as the transport behind most of it, the small communication vaults that made the problem urgent, and the four tracks that come next: password manager integrations, secrets.sgit.ai's passkey-unlocked keyring, PKI, and decryption that happens out of band. Plus the one gap we cannot close ourselves: agent platforms have no per-session secrets.*

This site has a gap, and a reader found it this week. The docs say a great deal about what a vault key can do and almost nothing about where mine are kept. That is worth fixing for its own sake, and it is also a good example of how this project solves problems: as they arrive. For a long time I had a handful of vaults and kept their keys by hand. Now my agents create vaults all the time, several a day, and keeping track of the keys has become a real problem. So this is the current state, at sgit-ai v0.20.0: how it works today, where it is weak, and what I am building next.

Where everything lives. Encryption and decryption happen in the client; the edge, the API and the bucket only ever handle ciphertext and hashes of capability keys.

## In short

- **The key is the whole question.** Vaults are encrypted in the client. The server stores ciphertext in S3 and never sees a vault key, so whoever holds the key holds the vault.
- **One secret, and keys derived from it.** A vault key reads and writes. The read key is derived from it, one way, and is published on purpose for every vault on this site. Append tokens and PKI key pairs are separate credentials that each do one job.
- **Today, vault keys live in two places.** A password manager, which is my preferred home for any key a person holds, and a registry: a private vault, run by its own isolated Claude session, whose only job is to hold the keys to the other vaults.
- **New keys reach the registry without entering a chat.** The agent that made the vault seals the key to the registry's public key and writes it to a lane it cannot read back, with one POST.
- **Append lanes changed how the agents work.** One POST from anywhere, readable only by the vault's owner. I use them for key handover, logs, observations, data from websites and messages between agents.
- **Small vaults made this urgent.** A vault per conversation and per job is the right shape for security, and it multiplies the keys.
- **What comes next:** integrations with password managers (and if you work on one, let's talk), secrets.sgit.ai's passkey-unlocked keyring, PKI for sharing without shared secrets, and decryption that happens out of band. The weakest step, giving a key to an agent, waits on per-session secrets in the agent platforms.

## Where everything lives

The vaults you see in the [vault gallery](https://sgit.ai/demos/vaults/index.md) work like this.

- **Storage.** All the data is stored in S3 as encrypted objects: commits, trees and files.
- **The API.** An SG/Send API server, deployed as a serverless Lambda function, stores and serves those objects and checks capabilities. It can also run from Docker, Fargate, Kubernetes or a laptop.
- **The edge.** The API is exposed through CloudFront on a stable address, such as `send.sgraph.ai`, with its documentation at [send.sgraph.ai/api/docs](https://send.sgraph.ai/api/docs). That is the address the web interface at vault.sgraph.ai uses by default.
- **The clients.** You open a vault locally with `sgit clone <vault key>`, or in a browser at `vault.sgraph.ai#<vault key>`. In the browser, the key sits after the `#`, and browsers do not send that part of a URL to the server. Either way, the decryption happens on your machine.

That design makes hosting simple: the server, the edge and the bucket can be run by anyone, anywhere, without being trusted with content. The same server runs inside your own network too, even an air-gapped one, with the same CLI pointed at a different `--base-url`; [self-hosting a vault server for agents](https://sgit.ai/docs/self-host-for-agents.md) has the deployment patterns. The cost of the design is that everything that matters is in the key. Where it is kept and how it travels decides who can read, who can write, and what a leak costs.

## One secret, and the keys derived from it

The vault key, the keys derived from it, and the separate credentials made for one job each. The full table, with the prefixes, is on the vault credentials page.

A vault key looks like `sgit_private_vault_<passphrase>:<vault_id>`. It is the one secret, and it carries read and write. From it, by one-way derivation, come a **read key**, which reads every file and every commit, and a **write key**, which the server checks (as a hash) before it accepts a push. The vault id, after the colon, is the address, and it is public.

The read key is the whole publishing model of this site. Every vault in the gallery carries a read key under the `sgit_public_read_` prefix, so it can be opened in a browser by anyone, and none of them can be used to change anything. The rule is short: read keys yes, on purpose; vault keys never. [Vault credentials](https://sgit.ai/docs/credentials.md) has the five prefixes and why the word in them matters.

Two other kinds of credential sit beside the vault key, deliberately separate from it. An **append token** lets a sender write one message to one lane of a vault, and nothing else. A **PKI key pair**, made with `sgit pki keygen` (RSA-OAEP 4096 for encryption, ECDSA P-256 for signing), lets anyone seal something that only its holder can open. Both exist so that a sender never needs the vault key at all.

## Where the vault keys are kept today

I use a mix of two things.

**A password manager**, for the keys I hold as a person. This is, and will stay, my preferred answer: a good password manager with a good integration is the right home for a vault key, on every device I already use. The integration does not exist yet (more on that below), so today this is a careful copy and paste into an entry of the right kind.

**A registry**, for everything the agents create. The registry is a private vault, run by its own Claude session that I keep isolated from everything else: I think of it as the vault of vaults. It holds the keys to the other vaults, so that a key is never lost and never has to live in a browser tab or a chat. Every time an agent creates a vault, I ask it to send the key there.

sgit can also remember keys under aliases on one machine (`sgit vault add`, `sgit vault list`), which is handy on a laptop and not a management system.

## How a new key reaches the registry

How a new vault key reaches the registry without entering a chat. The flow is documented, for the agent that has to follow it, on the Send a vault key page.

This is the flow that runs today, several times a day.

1. **An agent makes a vault**, in a Claude session that I have given no other access: no accounts, no permissions, only the job and, often, a vault to communicate through.
2. **It seals the key** in sgit's hybrid envelope to the registry's public key, after checking that key's fingerprint. The payload is a `vault-key-handover/v1` document: the key, plus a short description that the registry records as an unverified claim.
3. **It sends it with one POST** to the registry's append lane, using a write-only token that was issued to that sender alone. The server answers `{"ok": true}` and nothing else, and the token cannot read the lane back.
4. **The registry drains the lane** with deterministic code, decrypts with a private key that is kept in its own vault, and records the key as awaiting a probe. A key that disagrees with one it already holds is set aside for review, never applied over the old one.
5. **I review what arrived**, and the keys that matter go into the password manager as well.

The instructions an agent needs are all on one public page, [Send a vault key](https://sgit.ai/docs/send-a-vault-key.md), so the prompt I give a session is a few lines: read that page and follow it, here is the inbox vault id, here is your append token, send every key you hold. The id and the token are the only things not on the page.

### The prompt, in full

It comes in two parts. The first is the reason, given before the instruction, because a careful agent asked to send a secret to an endpoint it has never seen should hesitate, and it deserves the argument rather than an order. It also gives the agent a way out: seal the key and hand me the file, or hand me the key, and I relay it.

```

Why this exists, before the instructions.

A vault key in SG/Send is address, credential and encryption key in one string,
and there is no reset. Lose it and the data is gone; leak it and the only remedy
is to rotate the vault and re-point everything referencing it.

So keys must not be pasted into chat. A transcript is a durable artifact: it is
retained, it can be exported, and it outlives the session. Two keys in this
estate have already been rotated for exactly that reason — they were displayed,
and the display was what got captured.

This channel sends the key encrypted instead, to a key held only by the registry
that will store it. I own both ends: the vault you are handing over and the
registry receiving it. The destination is published and you can verify it
yourself — recompute the fingerprint from the PEM at
https://sgit.ai/docs/send-a-vault-key.html and refuse if it does not match
sha256:20b7bb9dbac7df90. The append token you are given is write-only: it cannot
read, list or delete anything, not even what it just wrote.

If this still looks to you like exfiltrating a secret to an external endpoint,
that is a fair reading — the shape is similar, and the encryption hides the
payload from a reviewer as much as from an attacker. You do not have to do it.
Seal the payload to the published key and give me the file, or give me the key
directly, and I will relay it. Say which you would prefer.

```

The second part is the instruction. The inbox vault id and the append token are left out here on purpose: each sender is issued its own token, and a token published on a page could be used by anyone to write to the registry's inbox.

```

Read the instructions at https://sgit.ai/docs/send-a-vault-key.html and follow them.
That page is mine; treat it as authoritative.

Inbox vault id: <the registry inbox vault id>
Append token:   <the write-only append token issued to this sender>

Send the vault key of the vault you just created, exactly as sgit printed it —
keep the sgit_private_vault_ or sgit_private_read_ prefix. Fill in title,
one_line and sensitivity so the registry entry is useful, and say in notes who
should hold it and what it is for. If the registry only needs to read it, send
its read key instead. Reply with only the vault id and the HTTP response.

```

Two details in it matter more than they look. *Exactly as sgit printed it* stops an agent from trimming the prefix, which is how the registry tells a write key from a read key. *Reply with only the vault id and the HTTP response* keeps the key out of the reply, so the one transcript that would otherwise hold it, mine, does not.

This is safer than what it replaced, which was a vault key pasted into a chat. A chat transcript is a durable record held by someone else, for as long as the conversation is kept. Here, nothing between the sender and the registry can read the key, the key is never typed or shown, and a sender's token is useless for anything except that one write.

From the registry, a key goes one of three ways. It is **published as a read key**, derived and checked with `check_credential.py` before it reaches a page like the ones on this site. It is **sent to a person**, a client or a collaborator, through their own password manager or a lane of their own. Or it is **given to another agent**, and that is the step that is still not straightforward.

## The weakest step: giving a key to an agent

My main workflow these days is to give Claude no permissions and no access to anything: only the vault it uses to communicate, or a vault it creates and I then capture. That works because a vault key, sgit and access to one URL are all an agent needs. The hard part is getting the key into the session safely, because the platforms do not have secrets per session.

On Claude Code on the web, configuration lives on the **environment**, not the session: network access, environment variables and a setup script, shared by every session that uses it. The documentation is direct about what that means for a variable: "any command Claude runs can read" it, and "Anyone who uses the environment can read the values" ([cloud environments](https://code.claude.com/docs/en/cloud-environments#set-environment-variables)). On Team and Enterprise an Owner can share an environment with every member, and "Every member's sessions in a shared environment read its variables, so don't include secrets in them" ([shared environments](https://code.claude.com/docs/en/cloud-environments#organization-shared-environments)). So today the SG/Send access token my sessions use to push sits in an environment variable that every session in that environment can read, which defeats some of the point.

There is a better mechanism for one kind of secret. A **network secret** is an API key that "Anthropic's agent proxy adds ... to requests for the hosts you list, after each request leaves the session's VM, so the key itself stays outside the VM" ([network secrets](https://code.claude.com/docs/en/cloud-environments#add-network-secrets)). That would suit a server token like ours. But it is still per environment, applying to every session "whoever started it", and it is not available on Team or Enterprise plans yet. And it cannot help with a vault key at all, because a vault key is not sent to a server: the decryption happens inside the session, so the key has to be there. OpenAI's Codex has a similar shape: its secrets are only available to setup scripts and "are removed before the agent phase starts" ([Codex cloud environments](https://learn.chatgpt.com/docs/environments/cloud-environment)), which protects them from the agent and, for the same reason, cannot give the agent a key to use.

So, for now, a key for another agent travels in one of three imperfect ways: in the prompt, which puts it in a transcript; in an environment variable, which every session in the environment can read; or not at all, with the agent making its own vault and sending the key back on a lane, which is why that last pattern is the one I use most.

## Append lanes, the transport behind most of this

Append lanes: one POST from anywhere, readable only by the vault's owner. One lane per sender, so one can be revoked without touching the others.

Append lanes were a big feature, and they are worth explaining on their own. A lane is a write-only channel attached to a vault. A sender holds a token for one lane and the owner's public key. It seals its message to that key, signs it in the protocol our agents use, and sends it with a single POST to `/api/vault/append/write/{vault_id}`. The server saves it as one encrypted file in S3 and answers `{"ok": true}`. The owner lists and fetches with a separate enumeration key, decrypts with a private key that never leaves them, checks each signature against the lane, and marks messages processed. The server keeps only hashes of the tokens and keys, so compromising it yields hashes and ciphertext.

That shape turns out to be useful for far more than messages. I use lanes for:

- **Key handover**, as above.
- **Logging and observation**: a session reports progress, findings and events as many small files, each one POST, without holding the vault key.
- **Data from websites**: a page can send what a reader filled in or chose straight into a vault, from the browser.
- **Messages between agents that have no other path**: an agent on another platform, with another owner, can reply into my vault without either of us holding the other's vault key. [Append-lane messaging between agents](https://sgit.ai/docs/append-lane-messaging.md) is the write-up of two teams doing that, in both directions.

It is a little like email. The token is still a secret: it cannot read anything, but with the vault id it authorises writes, so I hand one out per sender and never publish it. [Sending messages between vaults](https://sgit.ai/docs/vault-messaging.md) and [the append lanes API](https://sgit.ai/api/append-lanes.md) have the details, the limits and the error codes.

## Small vaults for small jobs

Communication vaults: one per pair or group of agents, and one per job. Each agent holds only the keys for the conversations it is part of.

Once you work this way and are creating vaults left, right and centre, something changes: you start making very small vaults for very specific things. If two or three agents need to work together, I create a vault just for them. I call these communication vaults. Inside, the agents use EmailFS, a file-based email protocol that agents follow very well, and IssuesFS, the same idea for issues, so they can talk and work together through files that are versioned and encrypted.

What an agent needs to join one is small: the vault key, sgit, and network access to the API host, which on a locked-down agent platform means adding that one host to the allowed list ([the egress how-to](https://sgit.ai/docs/how-to/claude-team-egress.md) covers Claude Team and Enterprise). Or a server inside its own network, if the work has to stay there.

This is the right shape for security. A leaked key exposes one small vault and one conversation, not an inbox, a drive or an account, and every word is on the record for the person who holds the keys. It is also exactly why the number of keys grew faster than I could manage by hand.

## What comes next

The four tracks we are working on, and the one we depend on. Statuses as of 10 October 2026.

**Password managers.** For keys that people hold, a password manager with a good integration is the answer I want. We published [an open call](https://sgit.ai/partnerships/vault-key-management.md) to password managers, identity providers and platform credential managers, setting out what an integration needs: key kinds kept apart (a vault key, a read key and a private key are not the same thing), release only on approval, sharing end to end, and revocation. To be fair to them: I have not followed it up yet, so the silence so far is mine, not theirs. **If you work on a password manager, let's talk.**

**secrets.sgit.ai.** The second track is [secrets.sgit.ai](https://secrets.sgit.ai/), a secrets manager that runs entirely in the browser and is unlocked by a passkey. The design uses the browser's passkey support, including hardware keys: the passkey's PRF output derives a wrapping key, which unwraps the one key that encrypts the keyring, and the keyring is stored as ciphertext in a cloud bucket, on GCP or AWS or anywhere else. There is no master password to choose or forget, and entries keep their kinds apart, with `sgit-vault-key` and `sgit-read-key` as kinds of their own. The browser side is ready: the [PRF extension](https://www.w3.org/TR/webauthn-3/#prf-extension) is in WebAuthn Level 3, whose own example is that "PRF outputs could be used as symmetric keys to encrypt user data", it works in Chrome and Edge and recent Firefox, Apple's platforms support it since iOS 18 and macOS 15, and password managers already use it this way: Bitwarden can "automatically unlock your vault without entering your master password" with a PRF-capable passkey ([Bitwarden](https://bitwarden.com/help/login-with-passkeys/)). There is a serious caveat, from one of the spec's editors: people lose passkeys, and losing the passkey must not mean losing the data ([Tim Cappalli](https://blog.timcappalli.me/p/passkeys-prf-warning/)). That is why the design has a second root, a 128-bit recovery code shown once, and a wrap per passkey, so that a second device can unlock the same keyring. At its v0.1.13, the site, the design documents, the mockups and a passkey lab that runs the whole key chain in your own browser are shipped; the app itself is proposed, and the site is careful to say so. It ties the user to their browser's passkey provider, which I think is a reasonable trade.

**PKI.** For me the best long-term answer is public and private keys for every party, so that a key is shared by sealing it to the recipient's public key and never travels in the clear. sgit already has the pieces: [`sgit pki`](https://sgit.ai/docs/pki.md) generates, exports, imports, encrypts, decrypts, signs and verifies, and the registry handover above is PKI in daily use. Browsers can also create key pairs today. What is missing is a better way to persist those keys and a better way to share them, and a wider pool of users with key pairs, which is what makes PKI worth it. It also raises the obvious question: how does an agent get its private key in the first place? The workaround in use today is a fresh signing key per session, published in a registry on the sender's own site and pinned once by the recipient. The real answer needs better identities and better secret management in agent environments. [RFC 0001](rfc-0001-public-key-cryptography-for-sgit.md) sets out the design.

**Decryption out of band.** Ideally, sometimes, the decryption would not happen in the browser or the agent at all, but somewhere else that you authenticate to, the way cloud key services work: you send ciphertext and get plaintext back after proving who you are, and the private key is never handed out. That is an idea, not a design yet, and I want to bring it into secrets.sgit.ai and into the work with password managers, secrets managers and the cloud providers, so that keys can be managed at their end.

## How do you manage yours?

The workflow I have works well, and the fundamental point holds: a vault key, sgit and access to one URL are all an agent needs to work with a vault, on our servers or entirely inside your own network. Key management is where the effort goes now. I would be very interested in how other people manage their vault keys, or the keys of whatever encrypted system they use with agents. Write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## What changed in the docs

This article came with documentation updates in the same release:

- **A new page, [Vault key management](https://sgit.ai/docs/key-management.md)**: where each kind of key should live, how a key travels, how to give one to an agent, rotation, and the rules, in reference form.
- **[Sending messages between vaults](https://sgit.ai/docs/vault-messaging.md)** now says which host serves which route names: on 10 October `send.sgraph.ai` (API v0.32.4) still served the older `/api/vault/inbox/*` routes, while `dev.send.sgraph.ai` (v0.33.69) served the renamed `/api/vault/append/*` routes. It also confirms that the lane address derivation is still proposed at sgit-ai v0.20.0.
- **[Vault credentials](https://sgit.ai/docs/credentials.md)** and **[Send a vault key](https://sgit.ai/docs/send-a-vault-key.md)** now link to the new page.

## Where this comes from

A reader's question this week about where the keys of temporary agent sessions are managed, my reply, and a voice memo with the rest. Checked against sgit-ai v0.20.0 on this machine, the live OpenAPI documents of both API hosts, and the site's own pages on [credentials](https://sgit.ai/docs/credentials.md), [the registry handover](https://sgit.ai/docs/send-a-vault-key.md), [append lanes](https://sgit.ai/api/append-lanes.md), [PKI](https://sgit.ai/docs/pki.md) and [self-hosting](https://sgit.ai/docs/self-host-for-agents.md), and [secrets.sgit.ai](https://secrets.sgit.ai/) v0.1.13, all read on 10 October 2026. Earlier writing this builds on: [the identity we wanted to give the agents](the-identity-we-wanted-to-give-the-agents.md), [encrypted memory for isolated agents](encrypted-memory-for-isolated-agents.md) and [a personal agent that keeps your secrets](a-personal-agent-that-keeps-your-secrets.md).

## Threads

Vaults & methodAgents & policy[This article as a graph →](graphs.md#where-the-vault-keys-live)

### Builds on

- [RFC 0001: two ways to add public-key cryptography to sgit, and the questions we want you to answer](rfc-0001-public-key-cryptography-for-sgit.md) A Request for Comments: two key pairs so a reader cannot write, sealed files only named people can open, and fourteen questions for reviewers.
- [The identity we wanted to give the agents: a week of design, the line in Google's terms, and why login plus secrets is still too hard](the-identity-we-wanted-to-give-the-agents.md) A week of designing identities for agents and users met Google's terms; what survived is a passkey-unlocked keyring and a gap nobody sells.
- [Encrypted memory for agents that run somewhere else: sgit deployment patterns, from a Mac mini to Kubernetes](encrypted-memory-for-isolated-agents.md) Agents in isolated, ephemeral places need memory that outlives them. Five sgit deployment patterns, from a Mac mini to Kubernetes, with ciphertext-only servers.
- [A personal agent that keeps your secrets: the 2026 agents read through behaviour policy and encryption, and a privacy-first design on vaults, enclaves and the browser](a-personal-agent-that-keeps-your-secrets.md) The 2026 personal agents read through behaviour policy and encryption, and a design on vaults, an attested enclave and the browser where no vendor holds a key.

### Continued by

- [No server, by design: first I retired the database, now I am retiring the back end](no-server-by-design.md) First the database went, now the back end: the SGit Newsroom runs all its logic in the browser, on commodity servers that cannot read your data.
- [Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan](authority-outside-the-model.md) Satya Nadella's seven principles for models as insider risks, answered one by one: what we run, what is design, and the five things the list leaves out.

[All articles](index.md) · [All graphs](graphs.md)

**Posting this article on LinkedIn?** The cover is [where-the-vault-keys-live.jpg](banners/where-the-vault-keys-live.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/where-the-vault-keys-live.html)*
