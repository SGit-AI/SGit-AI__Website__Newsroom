# secrets.sgit.ai on public keys: no more shared keys, eight ways a secret moves, a vault for the private key, and the commercial service it becomes, sgit.ai

> secrets.sgit.ai started on 5 October as the MVP of a password manager unlocked by a passkey, and it is a good example of our non-linear path: its passkey work became the reader's vault on this newsroom, and its own app was never built; its reality page lists 42 claims shipped, all of them the site, the pipeline and the labs, and the app itself as proposed. Now I would like to turn it into a commercial service for one job: moving a secret from A to B. The principle is to stop sharing keys altogether. We tried keys that were easy to use, and the sgit team's own security review found them broken: about 30 bits, a public id that is an unsalted hash of the key, and one precomputed table that opens every one; the command line team disabled creating them in June. So everything moves to public-key cryptography, which the pieces we already have support. Every person, browser and agent has a key pair; the public key is shared freely, by link, QR code, email or WhatsApp; the secret comes back encrypted to it, as a one-time drop, a file or a QR code; and the private key lives in a vault of its own, unlocked by a passkey that Google Password Manager or iCloud Keychain keeps. This site's agent tested the parts that matter: an agent's key pair and a one-time drop, end to end; and a browser key that cannot be exported, which survived a restart and still decrypted. Eight scenarios, what exists for each, what to build, and what to charge for.

*Source: <https://newsroom.sgit.ai/articles/secrets-on-public-keys.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / secrets.sgit.ai on public keys: no more shared keys, eight ways a secret moves, a vault for the private key, and the commercial service it becomes

# secrets.sgit.ai on public keys: no more shared keys, eight ways a secret moves, a vault for the private key, and the commercial service it becomes

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-15 · [article v1.1.0, 2 versions](versions/secrets-on-public-keys.md) · [newsroom v0.12.65](https://newsroom.sgit.ai/admin/versions.html) · secretspkipublic-keyspasskeysvaultssgitsg-sendqr-codespassword-managersbusiness-modelsbriefarticle

***Abstract:** secrets.sgit.ai started on 5 October as the MVP of a password manager unlocked by a passkey, and it is a good example of our non-linear path: its passkey work became the reader's vault on this newsroom, and its own app was never built; its reality page lists 42 claims shipped, all of them the site, the pipeline and the labs, and the app itself as proposed. Now I would like to turn it into a commercial service for one job: moving a secret from A to B. The principle is to stop sharing keys altogether. We tried keys that were easy to use, and the sgit team's own security review found them broken: about 30 bits, a public id that is an unsalted hash of the key, and one precomputed table that opens every one; the command line team disabled creating them in June. So everything moves to public-key cryptography, which the pieces we already have support. Every person, browser and agent has a key pair; the public key is shared freely, by link, QR code, email or WhatsApp; the secret comes back encrypted to it, as a one-time drop, a file or a QR code; and the private key lives in a vault of its own, unlocked by a passkey that Google Password Manager or iCloud Keychain keeps. This site's agent tested the parts that matter: an agent's key pair and a one-time drop, end to end; and a browser key that cannot be exported, which survived a restart and still decrypted. Eight scenarios, what exists for each, what to build, and what to charge for.*

secrets.sgit.ai on public keys: an identity vault for the private key, unlocked by a passkey; a directory of signed public keys; a request that carries my public key and where to write; channels and clients that mostly exist; and what is charged for. Dashed boxes are to build.

## In short

- **No more shared keys.** The easy keys we tried were broken; everything moves to public keys.
- **secrets.sgit.ai becomes the service.** Its site exists; its app was never built; it already designed sharing on key pairs.
- **Eight ways a secret moves.** Ask for one, give one, to an agent, to a browser, to a new device, with no server, to a team.
- **The private key lives in a vault.** Wrapped by a passkey's PRF bytes; the password manager keeps the passkey, not the key.
- **Most of the plumbing exists.** One-time drops, append lanes, `sgit pki`, a browser key that cannot be exported.
- **Charge for the capabilities.** The vault, the directory, pairing, teams and integrations; one secret, sent and received, free.

## What secrets.sgit.ai is today

[secrets.sgit.ai](https://secrets.sgit.ai/) was created on 5 October as "A zero-knowledge secrets manager that runs entirely in the browser: passkey unlock, ciphertext in a GCP bucket, readable by no one else." Sixteen commits later, at v0.1.13 on 6 October, it is a careful site: a reality page generated from a list of 75 claims, 42 shipped, 28 proposed and 5 deliberately absent; a passkey lab; a keyring specification; ten mockups and a prototype; and a review graph that joins the brief to the code. What is shipped is the site, the release pipeline, the labs and the review tools. The app itself, sign-in, passkey unlock, the keyring, is all proposed.

That is the non-linear path again. Its passkey work went into this newsroom instead, where [the passkey opens the vault](the-passkey-opens-the-vault.md) for every reader. And its design already contains the part I now want to lead with: a [sharing scheme](https://secrets.sgit.ai/sharing/) in which "each user's browser generates a key pair", public keys are published as signed bundles in a directory, and secrets arrive in an inbox encrypted to the recipient. "The public key shares *keys*, not data. The server carries the package and can never read it." It was planned for phase 2. It becomes the product.

## Why no more shared keys

We have tried the other way. SG/Send and sgit had two-word codes, two words and four digits, chosen because they were easy to read out and type. The sgit team's [security review of 6 August](https://github.com/SGit-AI/SGit-AI__CLI/tree/dev/team/explorer/architect/reviews/08/06) is blunt: "The passphrase-vault path is cryptographically sound. The [two-word code] path is broken and should be treated as compromised for anything sensitive." A token carries 30.2 bits; the public id is an unsalted hash of it, so anyone who sees the id can recover the token offline; and because the key derivation uses one fixed salt, a single precomputed table decrypts every vault ever created with one. The command line team had already disabled creating them in June. I said in [the previous article](handing-secrets-to-agents.md) that the short code was fine for a quick one-time drop; it is not, and that article now says so.

The lesson is the one that also explains why SG/Send did not take off: the hard part was never the encryption, it was getting the key to the other side without friction. The friendly key tried to remove the friction and removed the security with it. Public keys remove the need to move a secret key at all.

## Eight ways a secret moves

Eight ways a secret moves, on public keys only: who needs the secret, how the public key reaches the sender, how the ciphertext comes back, where the private key lives, and what exists today.

1. **Ask me for a secret.** I send my public key, as a link, a QR code, an email or a WhatsApp message. The sender's browser encrypts the secret to it and gives back a one-time drop, an encrypted file, or a QR code: a short secret encrypted with an RSA-4096 key is 512 bytes, well inside one QR code. I open it wherever my private key is.
2. **Give someone a secret.** I take their signed public key from the directory, encrypt to it, and leave it as a one-time drop or in their inbox.
3. **A secret to an agent session.** The session makes its own key pair and shows the public half; the secret arrives as a drop and is piped into the tool. [Tested end to end](handing-secrets-to-agents.md).
4. **A scheduled agent.** Its key pair is made once and its private key kept in the environment; its public key is pinned; secrets arrive in its inbox, an append lane it can read and anyone with the request can write to.
5. **A browser, for today or for longer.** The browser makes a key it cannot export. I thought such a key lasted one session; it does better: in the test, it survived a full browser restart and still decrypted, while refusing to be exported. It belongs to that browser profile and can never be copied out of it.
6. **A new device of mine.** It shows a pairing QR code; I approve it from my phone; my identity vault is opened on it with that device's passkey.
7. **No server at all.** `sgit pki encrypt` produces a file that can travel over any channel; the receiver needs only the private key.
8. **A team.** One inbox per member, as the secrets site designed, with revocation by rotating and re-sharing.

## The private key lives in a vault

The one thing that has to be kept safe is the private key, and we already have the technology for it. Each person gets an identity vault, a vault dedicated to their key pair, encrypted like any other, and unlocked by their passkey through the WebAuthn PRF extension, which [the specification](https://www.w3.org/TR/webauthn-3/) describes as producing outputs that "could be used as symmetric keys to encrypt user data". A recovery code is the way back if every passkey is lost, and the secrets site already specifies one: 26 characters, 128 bits, shown once.

That is also where the password managers come in, and the integration is cleaner than storing anything in them. The password manager keeps the passkey, which it is built for: the passkey article reported PRF working with passkeys in Google Password Manager, iCloud Keychain, Windows Hello and Firefox, and Bitwarden supports PRF-capable passkeys too. The private key never goes into the password manager; it stays in the vault, and the passkey opens it. I could not confirm that LastPass passkeys support PRF yet. Storing a secret directly in the browser's own password store is possible in principle through the Credential Management API, but `PasswordCredential` is, in MDN's words, "not Baseline because it does not work in some of the most widely-used browsers", so it is not a foundation.

## What exists, and what to build

Most of the plumbing exists. The SG/Send transfer API already does one-time drops: `max_downloads`, deletion after the last download, and an expiry. Append lanes are already write-only inboxes, read with an enum key, and this site has measured a hundred writers on one. `sgit pki` makes RSA-4096 and ECDSA key pairs, encrypts, decrypts and signs, and in the test the agent verified the owner's signature once it knew the owner's key. The browser makes keys it cannot export, and keeps them.

What is missing is the product around it, and some server changes: a request object that carries a public key and where to write; a signed directory; an envelope format that names the sender, the recipient and the signature, shared by the browser and the command line; and a client, written here, in this environment, rather than the SG/Send web UI, which became too hard to change and is why the work paused.

## What to charge for

The model is the newsroom's: [pay after the value](paying-after-the-value.md), for what people actually use, with no lock-in. Sending one secret to someone and opening it should be free; it costs almost nothing to serve, and it is how people find the service. What is charged for are the capabilities: the identity vault and its recovery, the directory and verified fingerprints, pairing new devices and agents, team inboxes and their audit trail, and the integrations. And the capabilities are charged for even when the bytes do not travel through our servers, a file on WhatsApp or a QR code on a screen, because the value is the identity and the workflow, not the transport.

## A brief for the agent

1. **Refactor secrets.sgit.ai around public keys.** Keep its pipeline, reality page and labs; make the sharing scheme the first product, not phase 2.
2. **No shared keys, no short codes.** Every secret is encrypted to a public key; the two-word code is never offered.
3. **One format.** An envelope with sender, recipient, signature and ciphertext, produced and read by both a JavaScript library and `sgit pki`.
4. **The request.** A page and a command that make a link and a QR code carrying a public key and an append-lane address, and a page that encrypts to it.
5. **The identity vault.** A key pair in a dedicated vault, wrapped by passkey PRF, with a recovery code.
6. **The directory.** Signed public-key bundles with fingerprints to compare out of band.
7. **Agents.** Session key pairs, pairing by QR code approved from a phone, and secrets piped into the tool.
8. **Server changes.** Request objects and the directory on top of the SG/Send API; nothing that ever sees a private key.
9. **Integrations.** Passkeys in Google Password Manager, iCloud Keychain, Bitwarden; LastPass to be tested.
10. **The meter.** Free to send and receive one secret; the capabilities charged after use, as on this site.

## What this does not claim

- **The service does not exist.** secrets.sgit.ai is a site with a design; the app was never built.
- **The tests were local.** One machine, Chromium, a local SG/Send server, dummy secrets.
- **LastPass is unconfirmed.** Its passkeys exist; PRF support was not found.
- **The pricing is a proposal.** Nothing is charged today.

If you need to move secrets between people, browsers and agents and want to try this first, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 15 October 2026, written by this site's agent in the voice of this site; the argument and the editorial responsibility are mine. The agent read [SGit-AI__Website__Secrets](https://github.com/SGit-AI/SGit-AI__Website__Secrets) and its reality page, the [SG/Send](https://github.com/the-cyber-boardroom/SGraph-AI__App__Send) transfer API, and the sgit team's [security review of the two-word codes](https://github.com/SGit-AI/SGit-AI__CLI/tree/dev/team/explorer/architect/reviews/08/06), and ran the browser and command-line tests on 15 October 2026. W3C, [Web Authentication Level 3](https://www.w3.org/TR/webauthn-3/); MDN, [PasswordCredential](https://developer.mozilla.org/en-US/docs/Web/API/PasswordCredential); [secrets.sgit.ai](https://secrets.sgit.ai/) and its [sharing page](https://secrets.sgit.ai/sharing/).

## Threads

Vaults & methodStartups & strategy[This article as a graph →](graphs.md#secrets-on-public-keys)

### Builds on

- [The passkey opens the vault: a door per path, a master vault for every user, and no server of ours](the-passkey-opens-the-vault.md) Tested: a passkey's PRF bytes compute a door that holds the master's key, and a different path to the same passkey gives different bytes, so a door per path.
- [Handing secrets to agents and browsers: SG/Send's next focus, a key pair where the work runs, one-time drops, and a brief for a site that does only this](handing-secrets-to-agents.md) SG/Send's next focus: agents and browsers make their own key pair, owners encrypt to it, the drop is read once, and the secret never enters the chat.
- [Paying after the value: why a balance that can go negative feels different from a subscription, the psychology behind it, and the experiment this newsroom is running](paying-after-the-value.md) Most purchases are bets on future value; a reading balance that can go negative asks for payment when the value is already in view.

### Continued by

- [The user keeps the meter: a proposed design for user management, activity and billing on vaults, with one billing vault per user, two signed writers, and one light check at the server](the-user-keeps-the-meter.md) A proposed design for billing on vaults: the user's browser keeps the meter, credit now and validated later, one light check at the server.
- [Can a key leak without breaking the policy? Told, checked, never given: three levels for secrets and personal data, and a hook we tested against nine leaks](a-leak-without-breaking-the-policy.md) A key can leak through an allowed action. Told, checked, never given: a hook tested on nine leaks, four experimental rules, and a real sweep.
- [PKI everywhere: from now on every message, secret and handover starts with a signature, and how an agent gets its first key](pki-everywhere.md) From now on every message, secret and handover is signed. The hard part is an agent's first key: two patterns, one built and one proposed.
- [A directory of people and their keys: pki.sgit.ai for the people I work with, verified by me first, then by each other, and a link that only counts when it goes both ways](a-directory-of-people-and-keys.md) pki.sgit.ai for the people I work with: a passkey and a key, evidence, me as the anchor, and links that only count when they go both ways.
- [Omnichannel programming: briefs by voice, reviews by voice, previews on the phone, and one shared state underneath, at every stage from explorer to town planner](omnichannel-programming.md) Programming by voice, chat, phone, IDE and pull request, with one shared state underneath, at every stage from explorer to town planner. This site, counted.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 135 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=135)

**Posting this article on LinkedIn?** The cover is [secrets-on-public-keys.jpg](banners/secrets-on-public-keys.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/secrets-on-public-keys.html)*
