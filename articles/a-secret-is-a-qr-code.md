# A secret is a QR code and a link to a public key: the workflow the QR experiment opens, who else already does this, and a format to share, sgit.ai

> The QR experiment showed that two AI sessions can pass keys and an encrypted message through QR codes and a screenshot. This is what I want to do with it. If I want to give someone a secret, all I have to do now is send them a QR code and a link to my public key; if they want to give me one, they encrypt it to my key and send me back a QR code. The first message carries their public key too, so after one exchange we can both write to each other, and once we have checked each other's fingerprints, we know who we are talking to. The same works for agents: an agent makes its own key pair, publishes the public half, and swaps QR codes with me or with another agent. None of it needs a server. The pieces are not new, and that is a good sign: QR codes already carry signed health certificates, verify keys in messaging apps, sign people in with a passkey on another device, and move signed transactions in and out of offline wallets. What is new is putting them together for secrets and agents, on top of public keys we publish, in a format we can share across our tools. The experiment's QRE1 format is a good start for that, with three things to add.

*Source: <https://newsroom.sgit.ai/articles/a-secret-is-a-qr-code.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / A secret is a QR code and a link to a public key: the workflow the QR experiment opens, who else already does this, and a format to share

# A secret is a QR code and a link to a public key: the workflow the QR experiment opens, who else already does this, and a format to share

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-21 · [article v1.1.0, 2 versions](versions/a-secret-is-a-qr-code.md) · [newsroom v0.13.26](https://newsroom.sgit.ai/admin/versions.html) · qr-codespkisecretsagentsencryptionarticle

***Abstract:** The QR experiment showed that two AI sessions can pass keys and an encrypted message through QR codes and a screenshot. This is what I want to do with it. If I want to give someone a secret, all I have to do now is send them a QR code and a link to my public key; if they want to give me one, they encrypt it to my key and send me back a QR code. The first message carries their public key too, so after one exchange we can both write to each other, and once we have checked each other's fingerprints, we know who we are talking to. The same works for agents: an agent makes its own key pair, publishes the public half, and swaps QR codes with me or with another agent. None of it needs a server. The pieces are not new, and that is a good sign: QR codes already carry signed health certificates, verify keys in messaging apps, sign people in with a passkey on another device, and move signed transactions in and out of offline wallets. What is new is putting them together for secrets and agents, on top of public keys we publish, in a format we can share across our tools. The experiment's QRE1 format is a good start for that, with three things to add.*

The workflow: publish a public key as a QR code, the sender encrypts to it, the ciphertext travels as a QR code.

## In short

- **A secret is a QR code and a link to my public key.** That is all it takes now.
- **The first message carries the sender's key.** After one exchange, it is two-way.
- **The fingerprint check makes it trusted.** Once, out of band.
- **Agents can do it too.** Their own key pair, the same QR codes.
- **No server.** Any channel can carry the code: it is ciphertext.
- **Others already use QR codes this way.** For certificates, keys, passkeys and wallets.
- **QRE1 is a good start for a shared format.** It needs chunking, forward secrecy and an identity.

## From the experiment to a workflow

In [the human is the network](the-human-is-the-network.md) two AI sessions passed keys, a certificate, images and an encrypted message through QR codes, with me screenshotting from one browser tab to the other. Afterwards I recorded what I think it opens up, and it is simple. In my words: "if I want to give a user a secret, all I have to do now is send them a QR code and the link to my public key, right? Isn't it? If you think about it, that's it."

It works in both directions:

- **I publish my public key.** As a QR code and a link, on a web page such as [pki.sgit.ai](https://pki.sgit.ai/), with its fingerprint.
- **Someone encrypts to it.** Their browser, or their agent, takes my key and encrypts the secret to it, and adds their own public key to the message.
- **The ciphertext travels as a QR code.** By email, chat, a web page or a screenshot. Whoever carries it sees nothing.
- **I decrypt it, and check their key.** Only my private key opens it. I compare their fingerprint with them once, by another channel.
- **From then on it is two-way.** "After that, they both have public keys, and they can swap messages."

## Agents in the loop

The same workflow works for agents, and that is where I think it gets most useful. An agent creates a key pair for itself, keeps the private half and publishes the public one. As I put it in the memo, the agent "can literally take go to our website, grab the public key of me or … of the target agent, download the public key, and then create an image that I can just give to the other agent, and suddenly we have a very effective way of communicating."

That solves a real problem I wrote about in [handing secrets to agents](handing-secrets-to-agents.md): giving a vault key to an agent session without pasting it in the clear. The session shows its public key as a QR code; I encrypt the vault key to it and hand back a QR code; only that session can open it. And the person in the middle, me, can see and control every message that crosses, without being able to read the secrets in it.

## Why QR codes and not text

We could do all of this with blocks of text, and we have. In the memo: "even when I try to, the whole send a massive blob of text. It's just unusable. It's not practical. It looks messy." A QR code is an object: a person can see it, move it, drop it in a chat or a page, and an agent or a browser can read it with a library. The experiment showed how much fits: up to 2,953 bytes, enough for keys, certificates, a signed message, or a whole infographic. And when something does not fit, a QR code can always carry a link to the rest.

## Who else already does this

Who already moves keys and secrets in QR codes, from the EU Digital COVID Certificate to Signal, WireGuard and eSIMs.

I asked for research on who else is doing this, and the answer is reassuring: every piece is already in use, at scale, which is good evidence that it works. From their own specifications and documentation:

- **Signed data in one code.** The EU Digital COVID Certificate is almost exactly the stack the experiment arrived at: a signed record in CBOR with a COSE signature, then, in the [specification's](https://github.com/ehn-dcc-development/hcert-spec/blob/main/hcert_spec.md) words, "the CWT SHALL be compressed using ZLIB", encoded in Base45 and prefixed "HC1:". Base45 has its own [RFC 9285](https://www.rfc-editor.org/rfc/rfc9285.html), because "QR codes have a limited ability to store binary data."
- **Verifying a key by scanning it.** Signal compares safety numbers in person with "a single QR code to scan" ([2016](https://signal.org/blog/safety-number-updates/)); in WhatsApp "verification can be done by scanning the QR code or by comparing the 60-digit number" ([whitepaper](https://www.whatsapp.com/security/WhatsApp-Security-Whitepaper.pdf)); and Matrix's code "encodes both parties' master signing keys as well as a random shared secret" ([spec](https://spec.matrix.org/v1.19/client-server-api/)).
- **A public key out, a secret back.** This is closest to my idea. When you link a new device to Signal, the phone "scans a QR code displayed by the new device that contains the device's 'provisioning address' and a public key", then "encrypts a use-case-specific provisioning message" to it ([Signal-Server](https://github.com/signalapp/Signal-Server/blob/main/service/src/main/java/org/whispersystems/textsecuregcm/controllers/ProvisioningController.java)). The difference: the ciphertext goes back through Signal's server, where ours would come back as a second QR code. [Threema](https://threema.com/press-files/2_documentation/cryptography_whitepaper.pdf) goes furthest: an ID and public key in a QR code, and even an encrypted backup of the private key, shown as a QR code "so that the user can more easily transfer it to another device."
- **Passkeys on another device.** The FIDO hybrid flow starts by showing a QR code "that contains a public key and a shared secret key" ([CTAP 2.2](https://fidoalliance.org/specs/fido-v2.2-ps-20250714/fido-client-to-authenticator-protocol-v2.2-ps-20250714.html)), with a Bluetooth check that the phone is really nearby.
- **Offline wallets.** Bitcoin signers that never touch a network pass transactions in and out as QR codes, larger ones "as an animated sequence of QR codes" ([Sparrow](https://sparrowwallet.com/docs/airgapped-wallet-qr.html)), using fountain codes from [Blockchain Commons' UR format](https://github.com/BlockchainCommons/Research/blob/master/papers/bcr-2020-005-ur.md). That is the chunking our format still needs.
- **Raw secrets, every day.** Authenticator apps take their secret as an `otpauth://` QR code, Wi-Fi networks share their password in one, and a WireGuard configuration, private key included, can be loaded from a QR code, as the app's own tip shows. These carry the secret in the clear, which is exactly what encrypting to a public key avoids.

And a warning that comes with the territory. QR codes are a well-known phishing route, "quishing" in the [NCSC's](https://www.ncsc.gov.uk/blog-post/qr-codes-whats-real-risk) word, and in 2025 Google's threat intelligence team reported attackers "crafting malicious QR codes that, when scanned, will link a victim's account to an actor-controlled Signal instance" ([Google](https://cloud.google.com/blog/topics/threat-intelligence/russia-targeting-signal-messenger)). That is the public-key-by-QR pattern turned against its users. The lesson is the one from the experiment: the QR code is only transport, and the trust has to come from a fingerprint the person checks.

What I have not found is the combination: published public keys, secrets encrypted to them and returned as QR codes, with agents as first-class participants, on any channel and with no server. That is the part worth building.

## A format to share: QRE1

Anatomy of a QRE1 frame: version, key id, one-off X25519 key, nonce, ChaCha20-Poly1305 ciphertext and signature.

In the experiment Session B wrote a small format for an encrypted message in a QR code, QRE1. It is one line of text, with fields separated by a vertical bar: a version, an 8-byte id of the recipient's key, a one-off X25519 key made for this message, a nonce, the ciphertext, and optionally the sender's Ed25519 key and a signature over the rest. The shared key comes from X25519 and HKDF, and the cipher is ChaCha20-Poly1305, the same pair that TLS 1.3 and WireGuard use.

When we wrote [secrets.sgit.ai on public keys](secrets-on-public-keys.md), one of the decisions was one format: "an envelope with sender, recipient, signature and ciphertext, produced and read by both a JavaScript library and `sgit pki`." QRE1 is close to that envelope already. I would make it the shared format across our tools, the vault library, pki.sgit.ai, the inbox's "send to my vault" and `sgit pki`, after three additions:

- **Chunking.** A sequence header, part i of n, and a hash of the whole, so a certificate chain or a larger secret can span several codes. One screenshot can carry several codes at once, as the experiment showed.
- **Forward secrecy, where it matters.** A long-lived recipient key means a leaked key opens old messages. After the first exchange, both sides can switch to short-lived keys.
- **An identity, not just a key.** The sender's key should point to a published, verified entry, such as a key on pki.sgit.ai, so the fingerprint check is done once and reused.

And one practical rule from the experiment: use a decoder that reads dense codes, and write bytes as base45 when the code may meet a decoder that turns bytes into text.

## What this does not claim

- **Not a product yet.** The workflow is a proposal; the experiment was one afternoon.
- **The fingerprint check is human.** Without it, a key proves nothing about who holds it.
- **QR codes can be abused.** A code can carry a malicious link as easily as a key; a reader should show what a code contains before acting on it.
- **About 2.9 KB a code.** More needs several codes, or a link.
- **The prior art is a sample.** The uses I could verify from their own documentation; there will be others I did not find.

## Where this comes from

My voice memo of 21 October 2026, quoted above; the QR experiment of the same day and its two debriefs, including Session B's QRE1 format; and, for who else does this, the specifications and documentation linked above, read the same day: the eHealth Network certificate specification v1.0.8, RFC 9285, Signal, the WhatsApp security whitepaper, the Matrix specification v1.19, Signal-Server, the Threema cryptography whitepaper, FIDO CTAP 2.2, Sparrow and Blockchain Commons, the NCSC and Google Threat Intelligence. Related: [the human is the network](the-human-is-the-network.md), [secrets.sgit.ai on public keys](secrets-on-public-keys.md), [handing secrets to agents](handing-secrets-to-agents.md), [a directory of people and their keys](a-directory-of-people-and-keys.md), [sixteen notes I did not want to lose](sixteen-notes-i-did-not-want-to-lose.md). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Site & engineering[This article as a graph →](graphs.md#a-secret-is-a-qr-code)

### Builds on

- [The human is the network: two AI sessions passing keys, a certificate, images and an encrypted message through QR codes and a screenshot](the-human-is-the-network.md) Two AI sessions sharing nothing passed keys, a certificate, images and an encrypted message through QR codes and a screenshot.
- [Handing secrets to agents and browsers: SG/Send's next focus, a key pair where the work runs, one-time drops, and a brief for a site that does only this](handing-secrets-to-agents.md) SG/Send's next focus: agents and browsers make their own key pair, owners encrypt to it, the drop is read once, and the secret never enters the chat.
- [secrets.sgit.ai on public keys: no more shared keys, eight ways a secret moves, a vault for the private key, and the commercial service it becomes](secrets-on-public-keys.md) secrets.sgit.ai becomes a service for moving a secret from A to B on public keys only: no shared keys, a vault for the private key, eight scenarios.
- [A directory of people and their keys: pki.sgit.ai for the people I work with, verified by me first, then by each other, and a link that only counts when it goes both ways](a-directory-of-people-and-keys.md) pki.sgit.ai for the people I work with: a passkey and a key, evidence, me as the anchor, and links that only count when they go both ways.
- [Sixteen notes I did not want to lose: a request to send from any browser to my vault, why identity is still this hard, and how two more wires became a product line](sixteen-notes-i-did-not-want-to-lose.md) Sixteen notes stuck in a browser with no passkey led to a request: let any browser send to my vault, by link, text or QR code.

### Continued by

- [Signed by the agent, vouched for by the person: a brief to give every email agent its own key, so each email carries a QR code that proves it is authentic](signed-email-from-the-agent.md) A brief to give every email agent its own key, vouched for by its person, so each email carries a QR code that proves it is authentic.
- [Seven IAM predictions for 2027, checked against an agent team that runs today: where we already are, where we agree, and the two where I would bet the other way](seven-iam-predictions-already-here.md) Sunnykumar K.'s seven IAM predictions for 2027, checked against agent teams that run today: four already here, one agreed, two different bets.
- [A pen and a key: a place on every page to mark it, comment on it and tell the newsroom, and a browser key that pki.sgit.ai vouches for, so a note can be checked as mine](a-pen-and-a-key.md) Every article now has a Pen to mark it, comment and tell the newsroom, and a browser key pki.sgit.ai vouches for signs each note as mine.
- [The sidecar repository: a second repository the agent cannot write to, which checks every release against the policy, trusts signed checks instead of re-running them, and is the only thing that deploys, designed for an agent that is fully compromised](the-sidecar-repository.md) A second repository the agent cannot write to, which checks every release, trusts signed checks instead of re-running them, and is the only thing that deploys.
- [Where a check runs is part of the policy: tests as enforcers of Agent Behaviour Policies, and what moving them out of the agent's environment would gain, measured on this newsroom](where-a-check-runs.md) Tests as enforcers of behaviour policies, and what moving them out of the agent's environment would gain, measured on this newsroom.
- [Governed semi-autonomous development, read in a newsroom run by agents: where Levente Simon's method and our work arrived at the same ideas, how we measure up to it, and what we would add](governed-semi-autonomous-development-read-here.md) Levente Simon's method for governing agent teams, read in a newsroom run by agents: shared ideas, a mirror, and five suggestions.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 245 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=245)

**Posting this article on LinkedIn?** The cover is [a-secret-is-a-qr-code.jpg](banners/a-secret-is-a-qr-code.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/a-secret-is-a-qr-code.html)*
