# The human is the network: two AI sessions passing keys, a certificate, images and an encrypted message through QR codes and a screenshot, sgit.ai

> This afternoon I ran one of those experiments that starts as a small question and ends somewhere much more interesting. Can two AI sessions that share nothing, no memory, no network link, no files, send each other data through QR codes that I screenshot in one browser tab and paste into another? In about three hours the answer went from maybe to yes, all the way to the format's limit. One session generated the codes; the other decoded and verified them. Text, then signed JSON, then public keys and an X.509 certificate, then images, then a real key exchange: one session published an encryption key as a QR code, the other encrypted and signed a message to it and returned it as a QR code, and the first decrypted it. The densest code, 2,953 bytes, the most one QR code can hold, decoded from a screenshot at about 1.3 pixels per square, and every screenshot payload was byte-identical to the original. The failures are as useful as the results: the AI cannot read a QR code by looking at it, the decoder mattered more than the resolution, and a lost key turned the experiment into a lesson in why fingerprints matter. For me the result is simple: QR codes are a far friendlier way to move keys and encrypted messages than the blobs of text we have been pasting.

*Source: <https://newsroom.sgit.ai/articles/the-human-is-the-network.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The human is the network: two AI sessions passing keys, a certificate, images and an encrypted message through QR codes and a screenshot

# The human is the network: two AI sessions passing keys, a certificate, images and an encrypted message through QR codes and a screenshot

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-21 · [article v1.0.0](versions/the-human-is-the-network.md) · [newsroom v0.13.26](https://newsroom.sgit.ai/admin/versions.html) · qr-codespkiencryptionagentsexperimentsarticle

***Abstract:** This afternoon I ran one of those experiments that starts as a small question and ends somewhere much more interesting. Can two AI sessions that share nothing, no memory, no network link, no files, send each other data through QR codes that I screenshot in one browser tab and paste into another? In about three hours the answer went from maybe to yes, all the way to the format's limit. One session generated the codes; the other decoded and verified them. Text, then signed JSON, then public keys and an X.509 certificate, then images, then a real key exchange: one session published an encryption key as a QR code, the other encrypted and signed a message to it and returned it as a QR code, and the first decrypted it. The densest code, 2,953 bytes, the most one QR code can hold, decoded from a screenshot at about 1.3 pixels per square, and every screenshot payload was byte-identical to the original. The failures are as useful as the results: the AI cannot read a QR code by looking at it, the decoder mattered more than the resolution, and a lost key turned the experiment into a lesson in why fingerprints matter. For me the result is simple: QR codes are a far friendlier way to move keys and encrypted messages than the blobs of text we have been pasting.*

Text, then JSON, then binary, then PKI, each in one QR code: a plain message, a signed JSON key offer, a compressed vector graphic, a photo-like image, an X.509 certificate and an encrypted message, passed between two Claude sessions by screenshot and paste, and each decoded and verified on arrival. Made by Session B.

## In short

- **Two sessions, no shared anything.** The only link between them was me, with screenshots and paste.
- **It worked up to the format's limit.** 2,953 bytes in one code, decoded from a screenshot.
- **Nothing was lost.** Every screenshot payload matched the original, byte for byte.
- **Keys, a certificate and images fit.** A whole infographic took 539 bytes.
- **The finale was encryption.** A public key out as a QR code, an encrypted message back.
- **The failures taught the most.** No reading by eye; the decoder mattered; a key was lost.
- **QR codes are friendlier than blobs of text.** That is the part I want to build on.

## A small question

This was, as I said in my voice memo afterwards, "one of those super interesting sort of serendipity things that happens when you're doing a bunch of experiments." I asked a Claude session whether it could create QR codes and read them, and whether that could beat copy and paste for moving data between sessions.

So I set it up properly. Two independent Claude sessions, in two browser tabs, with no shared memory, network link or files. Session A generated the codes. Session B decoded and verified them. The only connection between them was me: a screenshot on my Mac, a paste into the other tab, and later a ZIP file. Both sessions wrote up what they did, and this article is built from their two debriefs and the data they produced.

## Three hours, layer by layer

The experiment went up a layer every time the previous one worked:

- **Text.** "hello from session A", 53 bytes, a small code. Trivial.
- **Signed JSON.** A key offer signed with Ed25519. After the trip by screenshot, the signature still verified.
- **Keys and a certificate.** Ed25519, P-256, RSA-2048 and RSA-4096 public keys, and a self-signed X.509 certificate. Session B parsed each key and checked the certificate's signature.
- **Binary and images.** A compressed vector infographic, and photo-like images in AVIF, WebP, JPEG and palette PNG, each rebuilt from its decoded bytes.
- **Encryption.** A real exchange of keys and an encrypted, signed message, below.

Session A built a graded test set of eleven codes, each carrying its own length and hash, from 53 bytes to the 2,953-byte maximum. Session B decoded all eleven and checked every hash against a separate manifest.

## Four codes in one screenshot

The screenshot that carried four QR codes from one session to the other, as Session A showed them in its chat: from a short message to the largest code the format allows, the one on the right, 2,953 bytes.

This was the moment the experiment became interesting. Session A showed four of the codes in its chat. I took one screenshot of the row, with the rounded frames of the chat around them, and pasted it into Session B. That is a browser's rendering and scaling, a Retina screenshot and a clipboard, with nobody trying to keep the image clean.

All four decoded. The largest, a version 40 code with 177 by 177 squares, had been squeezed into about 230 pixels: about 1.3 pixels for each square. It decoded on the first attempt. And when the original files arrived later, Session B compared them: every payload from the screenshot was identical, byte for byte, to the one from the original image. The error correction built into QR codes absorbed everything the screenshot did to the image.

## How much fits

Left: the bytes in each code of the graded test set, from 53 for a short message to 2,953 for the largest code, with its QR version. Right: a version 40 code holds 2,953 bytes written raw, 2,864 as base45 and 2,214 as base64.

The numbers that matter:

- **2,953 bytes is the ceiling.** One QR code, version 40, with the lowest error correction. Reached, and decoded.
- **Elliptic-curve keys are tiny.** An Ed25519 public key is 43 characters. RSA-4096 still fits, at 800.
- **Compression did not help certificates.** A certificate compressed with zlib came out larger than an RSA-4096 key, because signed data is close to random and base64 adds back a third.
- **How the bytes are written matters.** Raw bytes hold the most, but many decoders hand them back as text and corrupt them. Base45, which packs bytes into the characters QR codes store most efficiently, cost about 3 % and survived everywhere.

## Images in a QR code

Two images inside single QR codes, each next to the image rebuilt from its decoded bytes: the whole infographic as compressed SVG, 539 bytes, and a 480 by 320 photo-like image as AVIF, 2,083 bytes.

This is the part I did not expect to work as well as it did. The whole infographic, as compressed SVG, took 539 bytes, about a fifth of one code, and came back exact and sharp at any size. A 480 by 320 photo-like image, generated for the test rather than a real photograph, fitted as AVIF in 2,083 bytes. The same infographic as a raster image needed between 1,881 and 2,810 bytes, and lost detail. For anything drawn, vector wins by a long way.

## The key exchange

The key exchange by screenshot: Session B publishes an X25519 public key as a QR code; the person carries it; Session A encrypts and signs a message to it and returns it as a QR code of 1,329 bytes; Session B decrypts it.

Then the finale. Session B made an X25519 key pair and published the public half as a QR code, and wrote a small format for encrypted frames, which it called QRE1. Session A decoded the key and confirmed its fingerprint, `aab8 bef5 da4f aa76 096b fea0 85f5 ef26`. It then encrypted a message to that key, with a fresh key of its own for this one message, signed the result with Ed25519, and returned it as a single QR code of 1,329 bytes. Session B decrypted it: "Hello session B. If you can read this…"

As I said in the memo, "it worked really well." And notice what I carried between the two tabs: a public key in one direction and ciphertext in the other. Nothing I relayed could be read by anyone else, so it would not have mattered if the same images had gone by email or a chat message.

## The failures

These are the best part of the debriefs, and I want to keep them:

- **The AI cannot read a QR code by looking at it.** Session A could see that an image was a QR code, but could not decode it by eye, and said so instead of pretending, especially as it already knew what the code contained. Every decode was done by code, with a decoding library.
- **The decoder mattered more than the resolution.** OpenCV's detector failed on the dense codes even in clean, high-resolution images; the ZXing library read all of them, down to 1.3 pixels a square. Session B had first blamed the resolution, and corrected itself when the evidence came in.
- **The lost key.** Session B asked Session A to sign with the key from the test set. That private key had only ever existed in memory, and it was gone. Session A did not fake it: it made a new signing key, signed with that, and said so inside the encrypted message, with the new key's fingerprint, `7e45 70bf 5e8c d3fa 2bc1 ebce 1347 169c`, for me to confirm.
- **Integrity is not authenticity.** Both sessions kept saying this, and they are right. A signature proves the bytes did not change; a key that travels inside its own message proves nothing about who sent it. That needs a person comparing fingerprints, or pinning a key the first time it is seen.

## Why I care

Session B's reply to the first QR code: it decoded the signed key offer, verified the Ed25519 signature, and pointed out that this proves integrity, not authenticity.

For me the advantage is practical. In my words from the memo: "QR codes are way more user friendly than what we were using to share the vault keys and the encrypted messages." When I have tried to send a big blob of text, "it's just unusable. It's not practical. It looks messy." A QR code is something a person can see, move and hand over, and it carries a decent amount of data, including images.

And it points at something bigger: a data channel that runs entirely on the client side, with no server in the middle, on top of public keys. We have been heading there for a while: the QR code in [send to my vault](sixteen-notes-i-did-not-want-to-lose.md), the ways a secret moves in [secrets.sgit.ai on public keys](secrets-on-public-keys.md), and the keys in [a directory of people and their keys](a-directory-of-people-and-keys.md). Today we measured the channel. The workflow it makes possible, and who else is already doing this, is the next article.

## What this does not claim

- **No reading by vision.** A decoding library reads the codes, not the model.
- **No proof of who sent it.** That needs a fingerprint checked out of band, or a key pinned on first use.
- **The new signing key is not yet accepted.** Its fingerprint was still waiting for my check when the debriefs were written.
- **Not forward-secret.** Session B's key is long-lived; if it leaked, past messages could be read.
- **An experiment, not a product.** The private keys lived in cloud sessions, which is fine for a test and not for production.
- **About 2.9 KB a code.** Anything bigger needs several codes.

## Where this comes from

The experiment of 21 October 2026, about 14:20 to 17:30 BST: Session A's debrief pack, with its results, manifest, scripts and images, and Session B's own briefing, including the QRE1 format it wrote; and my voice memo afterwards, quoted above. The images were all made in the experiment; the photo-like image was generated, not photographed. Related: [sixteen notes I did not want to lose](sixteen-notes-i-did-not-want-to-lose.md), [secrets.sgit.ai on public keys](secrets-on-public-keys.md), [handing secrets to agents](handing-secrets-to-agents.md), [a directory of people and their keys](a-directory-of-people-and-keys.md). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Site & engineering[This article as a graph →](graphs.md#the-human-is-the-network)

### Builds on

- [Sixteen notes I did not want to lose: a request to send from any browser to my vault, why identity is still this hard, and how two more wires became a product line](sixteen-notes-i-did-not-want-to-lose.md) Sixteen notes stuck in a browser with no passkey led to a request: let any browser send to my vault, by link, text or QR code.
- [secrets.sgit.ai on public keys: no more shared keys, eight ways a secret moves, a vault for the private key, and the commercial service it becomes](secrets-on-public-keys.md) secrets.sgit.ai becomes a service for moving a secret from A to B on public keys only: no shared keys, a vault for the private key, eight scenarios.
- [A directory of people and their keys: pki.sgit.ai for the people I work with, verified by me first, then by each other, and a link that only counts when it goes both ways](a-directory-of-people-and-keys.md) pki.sgit.ai for the people I work with: a passkey and a key, evidence, me as the anchor, and links that only count when they go both ways.
- [Handing secrets to agents and browsers: SG/Send's next focus, a key pair where the work runs, one-time drops, and a brief for a site that does only this](handing-secrets-to-agents.md) SG/Send's next focus: agents and browsers make their own key pair, owners encrypt to it, the drop is read once, and the secret never enters the chat.

### Continued by

- [A secret is a QR code and a link to a public key: the workflow the QR experiment opens, who else already does this, and a format to share](a-secret-is-a-qr-code.md) Send a QR code and a link to a public key: the workflow the QR experiment opens, who already does this, and a format to share.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 246 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=246)

**Posting this article on LinkedIn?** The cover is [the-human-is-the-network.jpg](banners/the-human-is-the-network.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-human-is-the-network.html)*
