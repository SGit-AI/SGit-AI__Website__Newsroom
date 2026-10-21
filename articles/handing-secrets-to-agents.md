# Handing secrets to agents and browsers: SG/Send's next focus, a key pair where the work runs, one-time drops, and a brief for a site that does only this, sgit.ai

> The pain I have right now is giving secrets to the places that do my work: vault keys to a browser where the passkey does not reach, and vault keys to the agent sessions I schedule every day. Copying them by hand is slow and risky, and when I tell an agent in its prompt that something is a secret to be careful with, it sometimes refuses to use it at all. So I would like SG/Send's technology to focus on one use case: handing a secret, or a public key, to an agent or a browser, as a separate site, mostly client-side, with a command line. The back end already has most of what this needs: a transfer that can be downloaded once and then deleted, an expiry, and client-side encryption; it does not, I found, restrict by location, which I thought it did. The design flips the usual direction: the recipient makes its own key pair where it runs and shows only the public half, by QR code, link or paste; the owner encrypts the secret to it and signs it; the drop is read once; and the secret goes from the drop into the tool, never into the chat. This site's agent ran it end to end on a local server: the agent decrypted the secret, the second download got a 410, the owner's signature verified once the agent knew the owner's key, and a browser made a key pair it refused to export. The industry is moving the other way, keeping secrets out of agents entirely; for an encrypted vault that cannot work, because the key has to reach the place that decrypts.

*Source: <https://newsroom.sgit.ai/articles/handing-secrets-to-agents.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Handing secrets to agents and browsers: SG/Send's next focus, a key pair where the work runs, one-time drops, and a brief for a site that does only this

# Handing secrets to agents and browsers: SG/Send's next focus, a key pair where the work runs, one-time drops, and a brief for a site that does only this

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-15 · [article v1.3.0, 4 versions](versions/handing-secrets-to-agents.md) · [newsroom v0.12.80](https://newsroom.sgit.ai/admin/versions.html) · secretspkiagentsbrowserssg-sendsgitvaultsqr-codespasskeysone-time-linksbriefarticle

***Abstract:** The pain I have right now is giving secrets to the places that do my work: vault keys to a browser where the passkey does not reach, and vault keys to the agent sessions I schedule every day. Copying them by hand is slow and risky, and when I tell an agent in its prompt that something is a secret to be careful with, it sometimes refuses to use it at all. So I would like SG/Send's technology to focus on one use case: handing a secret, or a public key, to an agent or a browser, as a separate site, mostly client-side, with a command line. The back end already has most of what this needs: a transfer that can be downloaded once and then deleted, an expiry, and client-side encryption; it does not, I found, restrict by location, which I thought it did. The design flips the usual direction: the recipient makes its own key pair where it runs and shows only the public half, by QR code, link or paste; the owner encrypts the secret to it and signs it; the drop is read once; and the secret goes from the drop into the tool, never into the chat. This site's agent ran it end to end on a local server: the agent decrypted the secret, the second download got a 410, the owner's signature verified once the agent knew the owner's key, and a browser made a key pair it refused to export. The industry is moving the other way, keeping secrets out of agents entirely; for an encrypted vault that cannot work, because the key has to reach the place that decrypts.*

Handing a secret to an agent or a browser, without anyone seeing it: the recipient makes its own key pair and shows only the public half; the owner encrypts to it, signs and drops the ciphertext for one download; the recipient decrypts it straight into the tool that needs it. Steps 1 to 4 ran end to end on a local SG/Send server.

## In short

- **One use case.** Handing a secret, or a public key, to an agent or a browser.
- **The back end is mostly there.** One download, then deleted; an expiry; client-side encryption.
- **Flip the direction.** The recipient makes its key pair; the owner encrypts to it.
- **Into the tool, not the chat.** The agent is told what to run, not what the secret is.
- **Tested end to end.** Decrypted once, refused twice, signature verified, private key unexportable.
- **The first secret is the hard one.** A scheduled session starts with one key from its environment.
- **Against the trend, on purpose.** Proxies keep API keys out of agents; a vault key must reach the place that decrypts.

## The pain

I have a growing number of places that need secrets: browsers where I read and write my vaults, and agent sessions that run on a schedule and need a vault key to do their work. [The passkey opens the vault](the-passkey-opens-the-vault.md) works well when it works, but it does not always: the same passkey, answering a QR code from another device, gave different bytes, and some browsers and profiles simply do not have it. [Sixteen notes I did not want to lose](sixteen-notes-i-did-not-want-to-lose.md) came out of exactly that, and proposed a link or QR code "carrying only where to write and the public key to encrypt with". QR codes worked well in those experiments; they carry a lot more than people think.

The agents are the other half. My observation, from many sessions, is that the more a prompt insists that a value is a secret, to be handled carefully and not exposed, the more likely the model is to refuse to use it at all. The caution is correct; the result is useless. And the secret I really want to give an agent is not a vault key. It is the agent's own private key, so that every other secret can be sent to it.

## What SG/Send already has

The back end does most of this already, and I wanted to know exactly how much. The transfer API takes, at creation, `max_downloads` ("Max downloads before exhausted"), `auto_delete` ("Wipe payload after last allowed download"), `expires_at`, and the hash of a delete code; the payload is encrypted in the client before upload; access tokens carry a usage limit and log a hash of the caller's address. What it does not have is a restriction by location. I thought it did; the code has no geographic check, so that is new work if we want it.

It also has a friendly mode, where two words and four digits derive both the key and the transfer id. The word list has 320 words, so a code is one of about a billion, roughly 30 bits, stretched with PBKDF2 at 600,000 iterations. That is not enough for anything. The sgit team's [security review of 6 August](https://github.com/SGit-AI/SGit-AI__CLI/tree/dev/team/explorer/architect/reviews/08/06) found that the public id is an unsalted hash of the code, so anyone who sees the id can recover the code offline, and that the fixed salt lets one precomputed table open every such transfer; the command line stopped creating them in June. And sgit already has public-key cryptography: `sgit pki keygen` makes an RSA-OAEP 4096 key for encryption and an ECDSA P-256 key for signing, and `encrypt` and `decrypt` do the rest.

## The design: the recipient makes the key

The usual way to share a secret is to send a link with the key in it. For agents and browsers, the idea is the opposite direction:

1. **The recipient makes a key pair where it runs.** An agent runs `sgit pki keygen` in its session; a browser uses WebCrypto with a private key that cannot be exported. Only the public half leaves: the bundle sgit exported was 1,164 bytes, which fits in one QR code; a QR code holds up to 2,953 bytes at its largest size, [according to its inventor](https://www.qrcode.com/en/about/version.html).
2. **The owner checks and encrypts.** I check the fingerprint, encrypt the secret to that public key, and sign it with my own key.
3. **SG/Send holds it once.** The ciphertext goes into a transfer with one download, deletion afterwards and an expiry. The server never sees a key.
4. **The recipient decrypts into the tool.** It downloads once, checks my signature against my public key, which it was given when it was set up, and pipes the result straight into `sgit clone -`, which already reads the key from standard input to keep it out of the command line and its history.

The last step is the answer to the refusals. The agent is never shown the secret, and never asked to be careful with it. Its instructions say what to run; the secret travels from the drop to the tool through a pipe, and never enters the prompt, the transcript or the model's context. That matters more than it seems: [the tokens hook](the-tokens-hook.md) found that the session transcript holds everything the model is told, and anything that can read the transcript can read that.

## Tested end to end

This site's agent ran the whole flow on a local SG/Send server, with sgit 0.21.0 and a dummy secret. An "agent" made a key pair and exported its public bundle; a "human" imported it, encrypted the secret to it and signed it; the 1,288 bytes of ciphertext went into a transfer with `max_downloads` set to 1, `auto_delete` and a one-hour expiry. The agent's first download returned the ciphertext intact, and it decrypted to the exact secret; the second download got `410` and "exhausted"; and the human's own key could not decrypt what it had sent. At first the agent reported "Signature present but UNVERIFIED"; once it held the owner's public key, it reported "Signature verified (signer: human-laptop)", which is why the owner's key has to be pinned when the recipient is set up.

In a browser, Chromium made an RSA-4096 key pair in 649 milliseconds and a P-256 pair in 0.3; asked to export the private key, it refused with `InvalidAccessError`, which is the point of a key made with `extractable` set to false. The [WebCrypto specification](https://w3c.github.io/webcrypto/) adds that "CryptoKey objects are serializable objects", so the key can live in the browser's storage without ever being readable as bytes. On the command line, a key pair took between half a second and a second. One friction showed up: `sgit pki keygen` asks for a passphrase to protect the private key, which a session running on its own cannot type, so it had to come from standard input.

## The first secret

Everything above depends on one thing: the recipient's private key. For a browser, it is made in place and never leaves. For a scheduled agent session, which starts from nothing every time, it has to come from somewhere, and that is the one secret this design cannot avoid. The honest options are two. The environment can hold it, accepting what Anthropic's own documentation says of cloud environment variables: "Anyone who uses the environment can read the values." That makes the key an identity of the environment, not of a session, which is right for an environment that is mine. Or each session makes its own key pair and asks to be paired, by showing a fingerprint or a QR code that I approve from my phone, the way a new device is paired.

## Against the trend, on purpose

The industry is moving the other way. Claude Code's cloud environments offer network secrets: "A network secret is an API key or token you store on a cloud environment so Claude can call that API from any session in the environment without seeing the key," because "Anthropic's agent proxy adds the key to requests for the hosts you list, after each request leaves the session's VM". 1Password's environments server for agents says that "By design, the server cannot return secret values stored in 1Password to the client, even if an agent requests them." For API keys, that is the right answer: the agent never needs to hold the key.

A vault key is different. The whole point of a zero-knowledge vault is that decryption happens at the client, so the key has to reach the place that decrypts; a proxy cannot add it on the way out. What this design can do is make that reach as small as possible: a key made where it is used, a secret encrypted to it, read once, piped into the tool, and never in the model's context.

## What exists, and the name

One-time secret sharing, and what is different about handing one to an agent: where the secret is encrypted, whether it is read once, whether it expires, whether it is encrypted to the recipient's own key, and whether there is a command line, from each tool's documentation; the last row was run.

One-time secrets are a solved problem for people: Bitwarden Send, 1Password's share links, Yopass and PrivateBin all encrypt in the client and expire. [Magic Wormhole](https://magic-wormhole.readthedocs.io/en/latest/welcome.html) solves the short code properly, with a key exchange where "Each code is one-time use only", and [age](https://github.com/FiloSottile/age) encrypts to a recipient's public key from the command line. What none of them is built around is a recipient that is an agent or a browser, making its own key, with an owner's signature it checks. The closest I found are small plugins for agent frameworks, such as Hermes' secret handoff, which keeps the value out of the transcript but, by its own account, not out of the chat history of the surface that asked for it.

The name needs work. Handoff is Apple's; KeyDrop is a Consumer Reports project that scans for exposed API keys; Courier is a messaging platform for humans and agents; Baton is an identity governance tool. I found no prominent product called SealDrop, which says what it does, a sealed drop, and is my working name; I have not checked trademark registries.

## A brief for the site

1. **One site, one job.** A separate site, built on SG/Send's transfer API, for handing secrets and public keys to agents and browsers.
2. **Client first.** All cryptography in the browser or the command line; a JavaScript library and the sgit command line share one format.
3. **Recipients make keys.** A browser makes a non-extractable key pair; an agent session runs one command; both show the public half as a QR code, a link and text.
4. **Owners encrypt and sign.** The page that sends shows the recipient's fingerprint, encrypts, signs, and creates a transfer with one download, deletion and a short expiry.
5. **Receive into the tool.** One command downloads, verifies the owner's signature against a pinned key, decrypts and pipes into `sgit clone -`; nothing is printed.
6. **Pairing for new sessions.** A session that has no key yet shows a fingerprint and a QR code; the owner approves it from a phone.
7. **No passphrase prompt for agents.** A documented way to give the private key's protection from the environment, and a test that it never reaches a log.
8. **No short codes.** The friendly code is retired; a short code is only safe inside a key exchange built for it, as Magic Wormhole does.
9. **Location limits, if wanted.** New work in the back end, not something it has today.

## What this does not claim

- **It ran locally.** One local server, one dummy secret, one browser; not the hosted service.
- **The refusals are my observation.** Not measured here.
- **The first secret is not solved.** It is moved to the environment, or to a pairing step.
- **The prior art is from documentation.** None of the other tools was run for this article.
- **SealDrop is a working name.** Checked on the web, not in trademark registries.
- **The friendly code is not safe on its own.** The sgit security review shows it can be recovered offline from the public id, even for a single download that expires in minutes.

If you hand secrets to agents and have found a better way, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 15 October 2026, written by this site's agent in the voice of this site; the argument and the editorial responsibility are mine. The back end was read in [SGraph-AI__App__Send](https://github.com/the-cyber-boardroom/SGraph-AI__App__Send), the flow was run by this site's agent on 15 October 2026, and a research agent read the documentation of the other tools; the quotes were checked. Anthropic, [cloud environments](https://code.claude.com/docs/en/cloud-environments); 1Password, [environments MCP server](https://www.1password.dev/environments/mcp-codex-server); W3C, [Web Cryptography API](https://w3c.github.io/webcrypto/); DENSO WAVE, [QR code versions](https://www.qrcode.com/en/about/version.html); [Magic Wormhole](https://magic-wormhole.readthedocs.io/en/latest/welcome.html); [age](https://github.com/FiloSottile/age); Bitwarden, [Send](https://bitwarden.com/help/about-send/); [Yopass](https://github.com/jhaals/yopass); [PrivateBin](https://github.com/PrivateBin/PrivateBin); [onetimesecret](https://github.com/onetimesecret/onetimesecret); Hermes, [secret handoff](https://hermes-agent.nousresearch.com/docs/zh-Hans/plugins/secret-handoff).

## Threads

Vaults & methodAgents & policy[This article as a graph →](graphs.md#handing-secrets-to-agents)

### Builds on

- [The passkey opens the vault: a door per path, a master vault for every user, and no server of ours](the-passkey-opens-the-vault.md) Tested: a passkey's PRF bytes compute a door that holds the master's key, and a different path to the same passkey gives different bytes, so a door per path.
- [Sixteen notes I did not want to lose: a request to send from any browser to my vault, why identity is still this hard, and how two more wires became a product line](sixteen-notes-i-did-not-want-to-lose.md) Sixteen notes stuck in a browser with no passkey led to a request: let any browser send to my vault, by link, text or QR code.
- [The tokens hook: a token behaviour policy that shows what every session reads, caches, writes and costs, why a prompt cannot do it, and a brief for tokens.hook.sgit.ai](the-tokens-hook.md) A token behaviour policy as a 132-line hook: the user sees what each session reads, caches and costs; a prompt cannot do it.

### Continued by

- [The human is the network: two AI sessions passing keys, a certificate, images and an encrypted message through QR codes and a screenshot](the-human-is-the-network.md) Two AI sessions sharing nothing passed keys, a certificate, images and an encrypted message through QR codes and a screenshot.
- [A secret is a QR code and a link to a public key: the workflow the QR experiment opens, who else already does this, and a format to share](a-secret-is-a-qr-code.md) Send a QR code and a link to a public key: the workflow the QR experiment opens, who already does this, and a format to share.
- [Can a key leak without breaking the policy? Told, checked, never given: three levels for secrets and personal data, and a hook we tested against nine leaks](a-leak-without-breaking-the-policy.md) A key can leak through an allowed action. Told, checked, never given: a hook tested on nine leaks, four experimental rules, and a real sweep.
- [PKI everywhere: from now on every message, secret and handover starts with a signature, and how an agent gets its first key](pki-everywhere.md) From now on every message, secret and handover is signed. The hard part is an agent's first key: two patterns, one built and one proposed.
- [A directory of people and their keys: pki.sgit.ai for the people I work with, verified by me first, then by each other, and a link that only counts when it goes both ways](a-directory-of-people-and-keys.md) pki.sgit.ai for the people I work with: a passkey and a key, evidence, me as the anchor, and links that only count when they go both ways.
- [Omnichannel programming: briefs by voice, reviews by voice, previews on the phone, and one shared state underneath, at every stage from explorer to town planner](omnichannel-programming.md) Programming by voice, chat, phone, IDE and pull request, with one shared state underneath, at every stage from explorer to town planner. This site, counted.
- [secrets.sgit.ai on public keys: no more shared keys, eight ways a secret moves, a vault for the private key, and the commercial service it becomes](secrets-on-public-keys.md) secrets.sgit.ai becomes a service for moving a secret from A to B on public keys only: no shared keys, a vault for the private key, eight scenarios.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 134 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=134)

**Posting this article on LinkedIn?** The cover is [handing-secrets-to-agents.jpg](banners/handing-secrets-to-agents.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/handing-secrets-to-agents.html)*
