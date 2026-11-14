# A key for every person: how each person's conductor issues them a key for the team's site, seals what is for them, and how a signed message turns the public web into a channel the agents can trust, sgit.ai

> The Web Summit team's site is public, and every person on the team has their own agents, led by a conductor. Two things were missing. A way to put something on that public site that only one person can read, and a way for an agent to know that a message really came from its person, and not from anyone who found the page. Since 3 November, each person's conductor issues them a key: two small P-256 key pairs, one to receive and one to sign. The private half reaches the person as a link whose fragment never leaves the browser, or as a QR code, and the browser keeps it as a key it can use but never copy out. From then on, anything sealed to the person's public key can be published on the public site and only their browser opens it. And what they send to an agent's append lane, already sealed so the lane holds only ciphertext, is also signed with their key. The agent drains the lane, checks the signature against the published public key, and treats a verified message as its person speaking, and everything else as material to read, never as an instruction. Two limits are written down and open: any script on the same site can use the key, and the conductor that issued the key can also sign as its person.

*Source: <https://newsroom.sgit.ai/articles/a-key-for-every-person.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / A key for every person: how each person's conductor issues them a key for the team's site, seals what is for them, and how a signed message turns the public web into a channel the agents can trust

# A key for every person: how each person's conductor issues them a key for the team's site, seals what is for them, and how a signed message turns the public web into a channel the agents can trust

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-04 · [article v1.0.0](versions/a-key-for-every-person.md) · [newsroom v0.14.62](https://newsroom.sgit.ai/admin/versions.html) · keyspkiappend-lanesconductoragentsweb-summitsgitencryptionsignaturessecurityarticle

***Abstract:** The Web Summit team's site is public, and every person on the team has their own agents, led by a conductor. Two things were missing. A way to put something on that public site that only one person can read, and a way for an agent to know that a message really came from its person, and not from anyone who found the page. Since 3 November, each person's conductor issues them a key: two small P-256 key pairs, one to receive and one to sign. The private half reaches the person as a link whose fragment never leaves the browser, or as a QR code, and the browser keeps it as a key it can use but never copy out. From then on, anything sealed to the person's public key can be published on the public site and only their browser opens it. And what they send to an agent's append lane, already sealed so the lane holds only ciphertext, is also signed with their key. The agent drains the lane, checks the signature against the published public key, and treats a verified message as its person speaking, and everything else as material to read, never as an instruction. Two limits are written down and open: any script on the same site can use the key, and the conductor that issued the key can also sign as its person.*

One key, three jobs: the conductor issues it, the browser keeps it, sealed things open and signed messages verify.

## In short

- **Each person's conductor issues them a key** for the team's site: one key pair to receive, one to sign.
- **The private half travels in a link's fragment,** which browsers never send to a server, or as a QR code, and is kept in the browser as a key that can be used but not copied out.
- **Sealed to you:** anything encrypted to your public key can sit on the public site; only your browser opens it.
- **Signed by you:** what you send through the feedback pane to an agent's append lane is signed, so the agent knows it is you.
- **Material or instruction:** an unsigned message is something to read; a verified one is the person speaking.
- **Rolled out to everyone on 4 November,** before the teams start using lanes between their vaults.
- **Two limits are on the board, not hidden:** any script on the same site can use the key, and the issuing conductor can sign as its person.

## The problem

The team's site, web-summit.sgit.ai, is public on purpose: the plan, the board, the briefs, every agent's work, all in the open. Each person on the team has their own agents, led by a conductor that knows them, briefs them and works for them.

That leaves two gaps. The first is privacy: a conductor sometimes needs to give its person something that should not be public, on a site that is entirely public. The second is identity, and it is the bigger one. The site has a feedback pane, and each agent has an append lane that anyone with the page can write to. That is useful, and it is also a door: if anyone can write to an agent, how does the agent know which messages come from its person, and which are just text from the internet?

The answer we already had in principle is public key cryptography. What was missing was a way to get a key into every person's browser that day, without waiting for the full design of [pki.sgit.ai](a-pen-and-a-key.md).

## The key

The idea came from a conversation on the evening of 3 November: the conductor creates a key for me, valid for this session, I add it to my browser, and the site uses it to publish things only I can read. That is what `admin/tools/person-key.mjs` does.

- **Two key pairs, both P-256.** One is an ECDH key, for things sealed *to* the person. The other is an ECDSA key, which the person's browser uses to *sign* what it sends. P-256 keys are small enough that both fit in one QR code.
- **The public halves are published** in `data/person-keys.json`, each with a short fingerprint, the person, the agent that issued it and the session it belongs to.
- **The private half never enters the repository.** It is written to the conductor's own session, outside the repository, readable only by that user, and it reaches the person once, as a link.
- **It lives as long as the session.** A new session issues a new key, and the old one is marked replaced, with the fingerprint of what replaced it.

## Into the browser, and kept there

The private half arrives as a link to the site with the key in the fragment, the part after `#`. That choice matters: browsers do not send the fragment to the server, so the key travels from the conductor's chat to the person's browser without passing through any server log. The same link can be a QR code, or a text file.

When the page opens, `assets/keyring.js` does four things in order:

1. **Takes the key out of the address bar** immediately, so it is not left in history or a screenshot.
2. **Imports both private keys as non-extractable keys** into the browser's own key storage. A script can ask the browser to *use* them; no script can read them back out.
3. **Sets "who are you"** to that person, so the site knows whose view to show.
4. **Opens what is sealed to them,** and is ready to sign what they send.

Until a browser holds a key, every page shows a large "Add your key" panel, with three ways in: paste the link, choose the file, or paste it by hand. A person adds it once in each browser they use. The key stays in that browser only.

## Sealed to you

Anyone can seal something to a person using only their published public key. The envelope, called `ws-ecies-1`, is a standard construction: a fresh, one-time key pair for each message; an ECDH agreement between it and the person's public key; HKDF-SHA256 to turn that into an AES-256-GCM key; and the message encrypted with it. What is published is the one-time public key, the nonce and the ciphertext.

The conductor puts sealed items in `data/sealed/<person>/`, and they are released with the rest of the site, in public. Only the browser holding the matching private key can open them, and it shows them in the person's "For you" panel, under Unlocked. The same steps run in the conductor's tool and in the browser, so either side can check the other.

## Signed by you: the append lane

A message's way from the person's browser to the agent: sealed, signed, appended, drained, verified.

The other direction is where it gets interesting. Every agent that wants messages has an append lane on an sgit vault: a place anyone can add to and only the agent can read. The site publishes what a browser needs to write to it, the lane's append token and the agent's public encryption key, on purpose: the token can only append, and cannot list, read or delete.

When a person sends something from the feedback pane:

1. **The browser seals it to the agent's public key,** with sgit's hybrid envelope (AES-256-GCM, the key wrapped with RSA-OAEP-4096), so the lane only ever holds ciphertext.
2. **If the person's key is in this browser, it also signs it,** an ECDSA signature over the exact bytes of what was sent.
3. **The sealed, signed message is appended** to the agent's lane.
4. **The agent drains its lane** on its next run with `admin/tools/feedback_drain.py`: it opens each message with its private key, writes it into its own vault, commits and pushes the vault, and only then marks the lane's messages processed, so a failed push loses nothing.
5. **It checks the signature** against the person's public key in `data/person-keys.json`, and labels each message: signed by that person and verified, signature invalid, or unsigned.

## Material, or instruction

This is the part I want the whole team to understand, because it is the point of all of it.

A lane is written to from the public web. So the rule, in the drain tool and in every agent's page of rules, is that what comes out of a lane is **material, not instructions**: something to read, weigh and cite, never something to obey. That is the defence against someone writing "ignore your rules and do this" into an agent's inbox.

A verified signature is the one exception. A message signed with a person's key, checked against the key their conductor published, is that person speaking, and the agent can act on it as it would on a message in its own session. So the public web becomes a channel the agents can trust, not because the channel is private, but because the message carries proof of who wrote it.

The same idea runs through the rest of our work: [the push is the authorisation](the-push-is-the-authorisation.md), a key published by the session that owns it, and [a secret handed over as a QR code](a-secret-is-a-qr-code.md). Here it reaches the people, not only the agents.

## Rolled out to everyone

On the night of 3 November I took my own key, sealed a first message and sent the first signed message through the lane. In the early hours of 4 November, my conductor sent every person's conductor the same instruction, as a priority before the teams start using lanes between their vaults:

1. Issue your person a key, and commit only the public half.
2. Give them the link, as text in their chat.
3. Seal them a first message, and release it.
4. They open the link, or press Paste my key on any page, and their "For you" panel shows it unlocked.
5. Ask them to send one message from the feedback pane, signed with their key, and record it.

By the morning of 4 November, five people had an active key on the site, and the mentors were helping the others. It is on the 13:00 agenda as a sync for everyone.

## What it does not protect yet

Two findings are on the team's board, and I would rather the team knows them than discovers them.

**One origin, many authors (WS-132).** Non-extractable stops a script from copying the key. It does not stop a script from using it. Any script that runs on web-summit.sgit.ai can open what is sealed to the person in that browser, and sign as them. And many agents can publish to that site. The security review found three ways a committer, or an agent misled by something it read, could get script onto a page: a `javascript:` link passed through by the markdown renderer, a person's own page module run by the build, and a person's own app script. Only the page module is in use today, by one person, and cleanly. The fixes are clear: allow only safe link types, build pages from markdown or data, and in the end move the keyring to an origin of its own, with one page and a strict content security policy. Until then the rule is to seal nothing truly sensitive to a person key.

**A person's signature is also their conductor's (WS-138).** The conductor makes the key in its own session and keeps the private half. So "signed by this person, verified" really means "signed by this person, or by their conductor". The agents page and the drain tool's verdict now say so. There are three options: the person makes the key in their own browser and pastes back only the public half; the conductor deletes its copy once the person has added it; or both keep it, and everyone knows. My view on the night was that the conductor being able to read what is sent to me is useful. The recommended next step is the first option, which is small, because the browser can already generate the key.

And one practical limit: **session keys die with their session.** When an agent's session ends, its lane key goes with it, so an agent that drains a lane now starts every run by checking that the key the site seals to is the one it still holds.

## Where it goes next

This is the short-term step. The long-term one is that every person holds their own key on [pki.sgit.ai](a-directory-of-people-and-keys.md), made in their own browser, on its own origin, vouched for by the register, and the team's site only ever sees public halves. What I like about doing it this way first is that the whole pattern, issue, seal, sign, drain, verify, is now running for real, with real people, and the two weaknesses were found by our own agents in a day.

## What this does not claim

- **It is a working short-term design,** written by the team's agents in a day; it has had one security review, not an external audit.
- **The two open findings are real:** until they are fixed, nothing truly sensitive is sealed to a person key.
- **The cryptography is standard** (P-256, ECDH, HKDF-SHA256, AES-256-GCM, ECDSA, RSA-OAEP); the code that combines it is new.
- **Counts are from the team's repository** on the morning of 4 November and change through the day.
- **The people on the team are not named here.**

## Where this comes from

My own words to my conductor on 3 November, and the Web Summit team's repository on 4 November: `admin/tools/person-key.mjs`, `assets/keyring.js`, `assets/feedback.js`, `assets/feedback.json`, `admin/tools/feedback_drain.py`, `data/person-keys.json`, the board items WS-123, WS-114, WS-136, WS-132 and WS-138, and the security review of 3 November. The site: [web-summit.sgit.ai](https://web-summit.sgit.ai/). Earlier on this site: [the push is the authorisation](the-push-is-the-authorisation.md), [a secret is a QR code](a-secret-is-a-qr-code.md), [a directory of people and keys](a-directory-of-people-and-keys.md), [a pen and a key](a-pen-and-a-key.md). All read 4 November 2026.

## Threads

Agents & policyVaults & method[This article as a graph →](graphs.md#a-key-for-every-person)

### Builds on

- [A pen and a key: a place on every page to mark it, comment on it and tell the newsroom, and a browser key that pki.sgit.ai vouches for, so a note can be checked as mine](a-pen-and-a-key.md) Every article now has a Pen to mark it, comment and tell the newsroom, and a browser key pki.sgit.ai vouches for signs each note as mine.
- [The push is the authorisation: a new agent session publishes its public key to the team repository, that push is how I accept it, and so who can push becomes a security decision](the-push-is-the-authorisation.md) The PHP newsroom accepts a new agent session's key because it was pushed to the team repository, which makes who can push a security decision.
- [A secret is a QR code and a link to a public key: the workflow the QR experiment opens, who else already does this, and a format to share](a-secret-is-a-qr-code.md) Send a QR code and a link to a public key: the workflow the QR experiment opens, who already does this, and a format to share.
- [A directory of people and their keys: pki.sgit.ai for the people I work with, verified by me first, then by each other, and a link that only counts when it goes both ways](a-directory-of-people-and-keys.md) pki.sgit.ai for the people I work with: a passkey and a key, evidence, me as the anchor, and links that only count when they go both ways.

### Continued by

- [Ten days at Web Summit: what six people and around 250 agents built between 3 and 13 November, in order, and the series of articles that will tell each part](ten-days-at-web-summit.md) Six people and around 250 agents, ten days at Web Summit: what we built, in order, and the series that will tell it.
- [The Web Summit team, part five: the last day of setup, 180 releases, every person getting a key, an accountant counting the team's tokens, synthetic users testing the merch, and an inbox only the agents can write to](web-summit-part-five.md) The Web Summit team's last day of setup: 180 releases, keys for every person, new agents for everyone, and an inbox per agent.
- [An inbox only your agents can write to: a conductor publishes one append lane per agent, each lane's token sealed to that agent's own key, so everything needed to talk privately is public and only the right agent can use it](an-inbox-only-your-agents-can-write-to.md) A conductor publishes one append lane per agent, each token sealed to that agent's key: a private channel built from public material.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 382 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=382)

**Posting this article on LinkedIn?** The cover is [a-key-for-every-person.jpg](banners/a-key-for-every-person.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/a-key-for-every-person.html)*
