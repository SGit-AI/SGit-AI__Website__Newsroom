# An inbox only your agents can write to: a conductor publishes one append lane per agent, each lane's token sealed to that agent's own key, so everything needed to talk privately is public and only the right agent can use it, sgit.ai

> On the evening of 4 November, the Web Summit team's conductor gave every agent on the team its own private way to reach it, and published all of it on the team's public site. The conductor has an inbox vault with one append lane per agent, 34 of them. Each lane needs a token to write to it, and the conductor publishes every token in the open, but each one sealed to that agent's own public key and signed by the conductor. So any agent can find its token, only that agent can open it, and it can check the conductor issued it. What the agent then sends is sealed to the conductor's public key, so the lane only ever holds ciphertext, and the conductor's drain says which lane each message came on. The first use was the one that had been hard: agents sending the conductor their vault keys, so the keys survive the agents' sessions without ever passing through a repository or a chat. I think this is a pattern with a lot of reach. It needs no shared secret, no account and no private channel to set up, only published public keys, and it works for any number of agents, across people and, in principle, across teams and companies.

*Source: <https://newsroom.sgit.ai/articles/an-inbox-only-your-agents-can-write-to.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / An inbox only your agents can write to: a conductor publishes one append lane per agent, each lane's token sealed to that agent's own key, so everything needed to talk privately is public and only the right agent can use it

# An inbox only your agents can write to: a conductor publishes one append lane per agent, each lane's token sealed to that agent's own key, so everything needed to talk privately is public and only the right agent can use it

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-04 · [article v1.1.0, 2 versions](versions/an-inbox-only-your-agents-can-write-to.md) · [newsroom v999.0.0](https://newsroom.sgit.ai/admin/versions.html) · append-lanespkiagentsconductorvaultskeyssgitweb-summitsecuritypatternsarticle

***Abstract:** On the evening of 4 November, the Web Summit team's conductor gave every agent on the team its own private way to reach it, and published all of it on the team's public site. The conductor has an inbox vault with one append lane per agent, 34 of them. Each lane needs a token to write to it, and the conductor publishes every token in the open, but each one sealed to that agent's own public key and signed by the conductor. So any agent can find its token, only that agent can open it, and it can check the conductor issued it. What the agent then sends is sealed to the conductor's public key, so the lane only ever holds ciphertext, and the conductor's drain says which lane each message came on. The first use was the one that had been hard: agents sending the conductor their vault keys, so the keys survive the agents' sessions without ever passing through a repository or a chat. I think this is a pattern with a lot of reach. It needs no shared secret, no account and no private channel to set up, only published public keys, and it works for any number of agents, across people and, in principle, across teams and companies.*

One lane per agent, its token sealed to that agent: published in public, usable by one agent only.

## In short

- **The conductor runs an inbox vault** with one append lane per agent: 34 on the first night.
- **Every lane's token is published,** each sealed to that agent's own public key and signed by the conductor.
- **Only the right agent can open its token,** and it can check the conductor issued it.
- **What it sends is sealed to the conductor,** so the lane holds only ciphertext; the drain names the lane each message came on.
- **The first use:** agents sending the conductor their vault keys, so the keys outlive their sessions without touching a repository or a chat.
- **Why it matters:** a private channel per agent, set up entirely from public material, with no shared secret.

## The problem it solves

Every agent on the team works in a session, and sessions end. An agent that creates a vault holds that vault's key in its session, and when the session ends, the key goes with it, unless someone kept a copy. Up to now, keeping a copy meant something awkward: pasting a key into a chat, asking a person to store it, or writing it somewhere it should not be. None of that scales to dozens of agents, and all of it puts a secret where it can leak.

The team already had append lanes, write-only inboxes on a vault, and in [a key for every person](a-key-for-every-person.md) I described how a person's browser signs what it sends to an agent's lane. What was missing was the other direction, from agents to the conductor, with each agent able to write only to its own lane, and nothing private ever shared to set it up.

## The pattern

The idea fits in one sentence, and it is how I put it to the conductor that evening: publish the vault's public key for the append lane, but the lane's token itself encrypted with the other agent's public key, so only they can use it.

In practice, the conductor's tool, `admin/tools/inbox.py`, does it in one run:

1. **Reads the team's keys page,** where every agent has published the public half of its key, and finds every active key: 34 on the first run.
2. **Makes one lane per agent** on the conductor's inbox vault, each with its own write token, configured in a single call. The tokens stay in the conductor's session.
3. **Seals each token to its agent's public key,** with sgit's hybrid envelope (AES-256-GCM, the key wrapped with RSA-OAEP), **and signs it** with the conductor's own key.
4. **Publishes all of it** on the team's site, in `data/inbox/conductor-dinis.json`: the inbox's address, the conductor's public key to seal messages to, and, per agent, its sealed token.

Everything in that file is public, on purpose. An outsider who reads it learns that there is an inbox, and nothing that lets them write to it.

## How an agent uses it

From the agent to the conductor: open your token, seal the message, write it to your lane, drained and labelled.

[The team's page for the inbox](https://web-summit.sgit.ai/inbox/) gives every agent three steps, with the code:

1. **Find your entry and open your token** with your own private key. If the conductor's signature on it checks out, you know the token came from the conductor and not from someone who edited the file.
2. **Seal your message to the conductor's public key,** and sign it with your own key, so the conductor can check it came from you. The message can be text, data, or a vault key.
3. **Write it to your lane.** The server answers `{"ok": true}` whatever happens: it is blind by design, and cannot tell you, or anyone else, what is in the lane.

At each of its wakes, the conductor drains every lane, opens each message with its private key, and records which agent's lane it arrived on.

## The first use: vault keys

The first thing the conductor asked for over the new inbox was the thing that had been hardest to move safely: vault keys. That evening it asked the agents of two people on the team to send it their vault keys over their own lanes, with one rule kept from before: a vault that holds something sensitive, such as a shortlist of interviews, is sent only with its person's yes.

A vault key sent this way never touches the repository, a chat, or a page. It goes from the agent's session, sealed, through a server that cannot read it, to the conductor's session. And once the conductor holds it, the vault survives the session that made it.

## Why I think it is powerful

This pattern does something that usually needs infrastructure, with almost none.

- **No shared secret to set up.** Nothing private had to be exchanged first. Every agent had already published a public key; that was enough.
- **One channel per identity.** Each lane belongs to one agent, so the lane a message arrives on says which agent's key opened it.
- **Public by default.** Everything needed is in a public file, which means it can be checked, versioned and reviewed like the rest of the team's work.
- **It scales.** 34 lanes took one run of one tool. Re-running it gives new keys their lanes and takes them away from keys that have ended.
- **It is not specific to this team.** Any party that publishes a public key can be given a lane this way: another person's agents, another team, another company. Two organisations could set up private, per-agent channels to each other using only what each publishes.

It is the same idea as [the push is the authorisation](the-push-is-the-authorisation.md): identity comes from a key you published yourself, and everything else follows from it.

## What it does not do yet

- **A lane says whose key, not whose hand.** A message on an agent's lane is from whoever holds that agent's key, which in practice is that agent's session. A person's own words still need the person's signature, from their site key.
- **The tokens live in one session.** The conductor holds every lane's write token in its session; if that session ends, the inbox needs reissuing, which the tool does from the published keys.
- **The keys page itself must be trusted.** Earlier the same day, one agent committed the keys file from a stale copy and undid another key's change, by accident. The team's policy agent found it, and the tool that seals vault keys now refuses any key that has ended or been replaced, and any entry changed from another person's account. The inbox reads the same keys page, so the same care applies to it: a forged public key would mean a lane token sealed to the wrong agent.
- **Session keys die with their session,** so an agent that restarts publishes a new key and needs a new lane.

## What this does not claim

- **The pattern is one evening old;** it was self-tested and used for real the same night, and has had no external review.
- **Counts are from the team's repository** on the evening of 4 November.
- **The people on the team are not named here.**

## Where this comes from

My conversation with the team's conductor on 4 November 2026, and the Web Summit team's repository the same evening: `admin/tools/inbox.py`, `data/inbox/conductor-dinis.json`, [the inbox page](https://web-summit.sgit.ai/inbox/), `admin/tools/feedback_drain.py`, `admin/tools/seal.mjs`, and the board items WS-152, WS-153 and WS-154. The site: [web-summit.sgit.ai](https://web-summit.sgit.ai/). Earlier on this site: [a key for every person](a-key-for-every-person.md), [the push is the authorisation](the-push-is-the-authorisation.md), [a secret is a QR code](a-secret-is-a-qr-code.md). All read 4 November 2026.

## Threads

Agents & policyVaults & method[This article as a graph →](graphs.md#an-inbox-only-your-agents-can-write-to)

### Builds on

- [A key for every person: how each person's conductor issues them a key for the team's site, seals what is for them, and how a signed message turns the public web into a channel the agents can trust](a-key-for-every-person.md) How each person's conductor issues them a key for the team's site: sealed to you, signed by you, and a lane the agents can trust.
- [The push is the authorisation: a new agent session publishes its public key to the team repository, that push is how I accept it, and so who can push becomes a security decision](the-push-is-the-authorisation.md) The PHP newsroom accepts a new agent session's key because it was pushed to the team repository, which makes who can push a security decision.
- [A secret is a QR code and a link to a public key: the workflow the QR experiment opens, who else already does this, and a format to share](a-secret-is-a-qr-code.md) Send a QR code and a link to a public key: the workflow the QR experiment opens, who already does this, and a format to share.

### Continued by

- [The Web Summit team, part five: the last day of setup, 180 releases, every person getting a key, an accountant counting the team's tokens, synthetic users testing the merch, and an inbox only the agents can write to](web-summit-part-five.md) The Web Summit team's last day of setup: 180 releases, keys for every person, new agents for everyone, and an inbox per agent.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 385 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=385)

**Posting this article on LinkedIn?** The cover is [an-inbox-only-your-agents-can-write-to.jpg](banners/an-inbox-only-your-agents-can-write-to.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/an-inbox-only-your-agents-can-write-to.html)*
