---
title: A secret is a QR code and a link to a public key: the workflow the QR experiment opens, who else already does this, and a format to share
date: 2026-10-21
author: Dinis Cruz
author_url: about/index.html
summary: The QR experiment showed that two AI sessions can pass keys and an encrypted message through QR codes and a screenshot. This is what I want to do with it. If I want to give someone a secret, all I have to do now is send them a QR code and a link to my public key; if they want to give me one, they encrypt it to my key and send me back a QR code. The first message carries their public key too, so after one exchange we can both write to each other, and once we have checked each other's fingerprints, we know who we are talking to. The same works for agents: an agent makes its own key pair, publishes the public half, and swaps QR codes with me or with another agent. None of it needs a server. The pieces are not new, and that is a good sign: QR codes already carry signed health certificates, verify keys in messaging apps, sign people in with a passkey on another device, and move signed transactions in and out of offline wallets. What is new is putting them together for secrets and agents, on top of public keys we publish, in a format we can share across our tools. The experiment's QRE1 format is a good start for that, with three things to add.
version: v0.13.26
license: https://creativecommons.org/licenses/by/4.0/
tags: qr-codes, pki, secrets, agents, encryption, article
status: published
---

!shot qw-flow.webp | images/ | The workflow: publish a public key as a QR code, the sender encrypts to it, the ciphertext travels as a QR code. | concept

## In short {#in-short}

- **A secret is a QR code and a link to my public key.** That is all it takes now.
- **The first message carries the sender's key.** After one exchange, it is two-way.
- **The fingerprint check makes it trusted.** Once, out of band.
- **Agents can do it too.** Their own key pair, the same QR codes.
- **No server.** Any channel can carry the code: it is ciphertext.
- **Others already use QR codes this way.** For certificates, keys, passkeys and wallets.
- **QRE1 is a good start for a shared format.** It needs chunking, forward secrecy and an identity.

## From the experiment to a workflow {#workflow}

In [the human is the network](/articles/the-human-is-the-network.html) two AI sessions passed keys, a certificate, images and an encrypted message through QR codes, with me screenshotting from one browser tab to the other. Afterwards I recorded what I think it opens up, and it is simple. In my words: "if I want to give a user a secret, all I have to do now is send them a QR code and the link to my public key, right? Isn't it? If you think about it, that's it."

It works in both directions:

- **I publish my public key.** As a QR code and a link, on a web page such as [pki.sgit.ai](https://pki.sgit.ai/), with its fingerprint.
- **Someone encrypts to it.** Their browser, or their agent, takes my key and encrypts the secret to it, and adds their own public key to the message.
- **The ciphertext travels as a QR code.** By email, chat, a web page or a screenshot. Whoever carries it sees nothing.
- **I decrypt it, and check their key.** Only my private key opens it. I compare their fingerprint with them once, by another channel.
- **From then on it is two-way.** "After that, they both have public keys, and they can swap messages."

## Agents in the loop {#agents}

The same workflow works for agents, and that is where I think it gets most useful. An agent creates a key pair for itself, keeps the private half and publishes the public one. As I put it in the memo, the agent "can literally take go to our website, grab the public key of me or … of the target agent, download the public key, and then create an image that I can just give to the other agent, and suddenly we have a very effective way of communicating."

That solves a real problem I wrote about in [handing secrets to agents](/articles/handing-secrets-to-agents.html): giving a vault key to an agent session without pasting it in the clear. The session shows its public key as a QR code; I encrypt the vault key to it and hand back a QR code; only that session can open it. And the person in the middle, me, can see and control every message that crosses, without being able to read the secrets in it.

## Why QR codes and not text {#why-qr}

We could do all of this with blocks of text, and we have. In the memo: "even when I try to, the whole send a massive blob of text. It's just unusable. It's not practical. It looks messy." A QR code is an object: a person can see it, move it, drop it in a chat or a page, and an agent or a browser can read it with a library. The experiment showed how much fits: up to 2,953 bytes, enough for keys, certificates, a signed message, or a whole infographic. And when something does not fit, a QR code can always carry a link to the rest.

## Who else already does this {#prior}

!shot qw-prior.webp | images/ | Who already moves keys and secrets in QR codes, from the EU Digital COVID Certificate to Signal, WireGuard and eSIMs. | comparison

I asked for research on who else is doing this, and the answer is reassuring: every piece is already in use, at scale, which is good evidence that it works. From their own specifications and documentation:

- **Signed data in one code.** The EU Digital COVID Certificate is almost exactly the stack the experiment arrived at: a signed record in CBOR with a COSE signature, then, in the [specification's](https://github.com/ehn-dcc-development/hcert-spec/blob/main/hcert_spec.md) words, "the CWT SHALL be compressed using ZLIB", encoded in Base45 and prefixed "HC1:". Base45 has its own [RFC 9285](https://www.rfc-editor.org/rfc/rfc9285.html), because "QR codes have a limited ability to store binary data."
- **Verifying a key by scanning it.** Signal compares safety numbers in person with "a single QR code to scan" ([2016](https://signal.org/blog/safety-number-updates/)); in WhatsApp "verification can be done by scanning the QR code or by comparing the 60-digit number" ([whitepaper](https://www.whatsapp.com/security/WhatsApp-Security-Whitepaper.pdf)); and Matrix's code "encodes both parties' master signing keys as well as a random shared secret" ([spec](https://spec.matrix.org/v1.19/client-server-api/)).
- **A public key out, a secret back.** This is closest to my idea. When you link a new device to Signal, the phone "scans a QR code displayed by the new device that contains the device's 'provisioning address' and a public key", then "encrypts a use-case-specific provisioning message" to it ([Signal-Server](https://github.com/signalapp/Signal-Server/blob/main/service/src/main/java/org/whispersystems/textsecuregcm/controllers/ProvisioningController.java)). The difference: the ciphertext goes back through Signal's server, where ours would come back as a second QR code. [Threema](https://threema.com/press-files/2_documentation/cryptography_whitepaper.pdf) goes furthest: an ID and public key in a QR code, and even an encrypted backup of the private key, shown as a QR code "so that the user can more easily transfer it to another device."
- **Passkeys on another device.** The FIDO hybrid flow starts by showing a QR code "that contains a public key and a shared secret key" ([CTAP 2.2](https://fidoalliance.org/specs/fido-v2.2-ps-20250714/fido-client-to-authenticator-protocol-v2.2-ps-20250714.html)), with a Bluetooth check that the phone is really nearby.
- **Offline wallets.** Bitcoin signers that never touch a network pass transactions in and out as QR codes, larger ones "as an animated sequence of QR codes" ([Sparrow](https://sparrowwallet.com/docs/airgapped-wallet-qr.html)), using fountain codes from [Blockchain Commons' UR format](https://github.com/BlockchainCommons/Research/blob/master/papers/bcr-2020-005-ur.md). That is the chunking our format still needs.
- **Raw secrets, every day.** Authenticator apps take their secret as an `otpauth://` QR code, Wi-Fi networks share their password in one, and a WireGuard configuration, private key included, can be loaded from a QR code, as the app's own tip shows. These carry the secret in the clear, which is exactly what encrypting to a public key avoids.

And a warning that comes with the territory. QR codes are a well-known phishing route, "quishing" in the [NCSC's](https://www.ncsc.gov.uk/blog-post/qr-codes-whats-real-risk) word, and in 2025 Google's threat intelligence team reported attackers "crafting malicious QR codes that, when scanned, will link a victim's account to an actor-controlled Signal instance" ([Google](https://cloud.google.com/blog/topics/threat-intelligence/russia-targeting-signal-messenger)). That is the public-key-by-QR pattern turned against its users. The lesson is the one from the experiment: the QR code is only transport, and the trust has to come from a fingerprint the person checks.

What I have not found is the combination: published public keys, secrets encrypted to them and returned as QR codes, with agents as first-class participants, on any channel and with no server. That is the part worth building.

## A format to share: QRE1 {#qre1}

!shot qw-qre1.webp | images/ | Anatomy of a QRE1 frame: version, key id, one-off X25519 key, nonce, ChaCha20-Poly1305 ciphertext and signature. | concept

In the experiment Session B wrote a small format for an encrypted message in a QR code, QRE1. It is one line of text, with fields separated by a vertical bar: a version, an 8-byte id of the recipient's key, a one-off X25519 key made for this message, a nonce, the ciphertext, and optionally the sender's Ed25519 key and a signature over the rest. The shared key comes from X25519 and HKDF, and the cipher is ChaCha20-Poly1305, the same pair that TLS 1.3 and WireGuard use.

When we wrote [secrets.sgit.ai on public keys](/articles/secrets-on-public-keys.html), one of the decisions was one format: "an envelope with sender, recipient, signature and ciphertext, produced and read by both a JavaScript library and `sgit pki`." QRE1 is close to that envelope already. I would make it the shared format across our tools, the vault library, pki.sgit.ai, the inbox's "send to my vault" and `sgit pki`, after three additions:

- **Chunking.** A sequence header, part i of n, and a hash of the whole, so a certificate chain or a larger secret can span several codes. One screenshot can carry several codes at once, as the experiment showed.
- **Forward secrecy, where it matters.** A long-lived recipient key means a leaked key opens old messages. After the first exchange, both sides can switch to short-lived keys.
- **An identity, not just a key.** The sender's key should point to a published, verified entry, such as a key on pki.sgit.ai, so the fingerprint check is done once and reused.

And one practical rule from the experiment: use a decoder that reads dense codes, and write bytes as base45 when the code may meet a decoder that turns bytes into text.

## What this does not claim {#limits}

- **Not a product yet.** The workflow is a proposal; the experiment was one afternoon.
- **The fingerprint check is human.** Without it, a key proves nothing about who holds it.
- **QR codes can be abused.** A code can carry a malicious link as easily as a key; a reader should show what a code contains before acting on it.
- **About 2.9 KB a code.** More needs several codes, or a link.
- **The prior art is a sample.** The uses I could verify from their own documentation; there will be others I did not find.

## Where this comes from {#sources}

My voice memo of 21 October 2026, quoted above; the QR experiment of the same day and its two debriefs, including Session B's QRE1 format; and, for who else does this, the specifications and documentation linked above, read the same day: the eHealth Network certificate specification v1.0.8, RFC 9285, Signal, the WhatsApp security whitepaper, the Matrix specification v1.19, Signal-Server, the Threema cryptography whitepaper, FIDO CTAP 2.2, Sparrow and Blockchain Commons, the NCSC and Google Threat Intelligence. Related: [the human is the network](/articles/the-human-is-the-network.html), [secrets.sgit.ai on public keys](/articles/secrets-on-public-keys.html), [handing secrets to agents](/articles/handing-secrets-to-agents.html), [a directory of people and their keys](/articles/a-directory-of-people-and-keys.html), [sixteen notes I did not want to lose](/articles/sixteen-notes-i-did-not-want-to-lose.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
