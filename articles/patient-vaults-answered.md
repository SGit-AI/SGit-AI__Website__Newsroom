# Patient vaults, answered point by point: the seven questions a healthcare team asked before putting any real patient data into sgit vaults, on the live date, the patient's address, the storage region, erasure, backing up the clinic's key, per-patient tokens and writing from another site, and why QR codes and public keys are how a clinic and its patients should pass keys and links, sgit.ai

> A healthcare team building encrypted patient vaults with their own agents, pointed at our public repositories, sent me seven careful questions before putting any real patient data in. Everything so far had been design work with invented data, which is exactly right. Their questions are the ones every health organisation should ask, so here are the answers, point by point. There is no live date for the doctor console yet; test on our development service with invented data, and for real data run your own server, at the version you tested. A patient's details live in the patient's own vault, opened from a link the clinic gives them. The storage region is whichever you choose, once you deploy into your own AWS account. Erasure works: a deleted vault is removed from the server and a marker stops that vault id ever being uploaded again, and without its key any copy is unreadable anyway. If the clinic's key is lost, the vault is lost, which is the zero-knowledge deal, so seal it to two or more custodians and keep an offline copy. The server's token only authorises uploads; making changes needs the vault key and its identity, and per-patient writing is what append lanes are for, including from another website. And underneath it all, QR codes: public keys swapped as QR codes, and links sealed to a patient's key, so no key ever travels in clear.

*Source: <https://newsroom.sgit.ai/articles/patient-vaults-answered.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Patient vaults, answered point by point: the seven questions a healthcare team asked before putting any real patient data into sgit vaults, on the live date, the patient's address, the storage region, erasure, backing up the clinic's key, per-patient tokens and writing from another site, and why QR codes and public keys are how a clinic and its patients should pass keys and links

# Patient vaults, answered point by point: the seven questions a healthcare team asked before putting any real patient data into sgit vaults, on the live date, the patient's address, the storage region, erasure, backing up the clinic's key, per-patient tokens and writing from another site, and why QR codes and public keys are how a clinic and its patients should pass keys and links

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-17 · [article v1.0.0](versions/patient-vaults-answered.md) · [newsroom v0.14.137](https://newsroom.sgit.ai/admin/versions.html) · sgitvaultshealthcareprivacygdprpkiqr-codesarticle

***Abstract:** A healthcare team building encrypted patient vaults with their own agents, pointed at our public repositories, sent me seven careful questions before putting any real patient data in. Everything so far had been design work with invented data, which is exactly right. Their questions are the ones every health organisation should ask, so here are the answers, point by point. There is no live date for the doctor console yet; test on our development service with invented data, and for real data run your own server, at the version you tested. A patient's details live in the patient's own vault, opened from a link the clinic gives them. The storage region is whichever you choose, once you deploy into your own AWS account. Erasure works: a deleted vault is removed from the server and a marker stops that vault id ever being uploaded again, and without its key any copy is unreadable anyway. If the clinic's key is lost, the vault is lost, which is the zero-knowledge deal, so seal it to two or more custodians and keep an offline copy. The server's token only authorises uploads; making changes needs the vault key and its identity, and per-patient writing is what append lanes are for, including from another website. And underneath it all, QR codes: public keys swapped as QR codes, and links sealed to a patient's key, so no key ever travels in clear.*

Seven questions from a healthcare team, answered: live date, address, region, erasure, keys, tokens, writing.

## In short

- **A healthcare team asked seven questions** before putting real patient data into vaults; good questions, asked at the right time.
- **No live date** for the doctor console: test on dev with invented data, and run your own server for real data.
- **Region: yours to choose,** in your own AWS account.
- **Erasure works:** the vault is removed and its id can never be reused; without a key, copies are unreadable.
- **Lose the clinic key, lose the vault:** so seal it to custodians and keep an offline QR copy.
- **The server token only authorises uploads;** changes need the vault key.
- **QR codes and public keys** pass keys and links, never in clear.

## The questions

A healthcare team, who learned to build with agents only last week, has been designing patient vaults for a clinic: patient vaults created from the clinic's vault, keys held in custody, writable links for patients. They pointed their agents at our public repositories, checked the facts, and then, before putting a single real patient record in, sent me seven questions. Nothing real has been used: everything so far is design work with invented data.

That is exactly the right order, and the questions are the ones any health organisation should ask, for its data protection impact assessment and for its patients. If you are deploying sgit in a healthcare environment, these are your answers too.

## 1. When will the doctor console be live?

I do not have a date. The doctor console's features run on our development service, dev.vault.sgraph.ai, and not yet on vault.sgraph.ai. My advice is not to wait for us. Keep testing on dev with invented data, and when real data is close, run your own server, from your own pipeline, at the exact version you tested ([deploy sgit in your own environment](deploy-sgit-from-ci.md)). Then your live date is yours.

## 2. Which address should patients use?

The patient's details live in the patient's own vault, encrypted on the device, and nowhere else: not in a database the clinic runs, and not in a message thread. The patient opens that vault from a link the clinic gives them, on the deployment the clinic uses, ideally as a link sealed to the patient's own key and shown as a QR code (below). The old address in our June notes no longer serves the app; once you run your own server, the address is your own domain.

## 3. Where are the vaults stored?

In the region you choose. Run your own server and its S3 bucket is named after your account and your region, `{account}--sgraph-send-transfers--{region}`; nothing in the deployment templates is region-specific, so London, Frankfurt or Ireland is a parameter. That is the answer a data protection impact assessment wants: our own account, in this region, run by our own pipeline. And whatever the region, the host holds ciphertext only; it sees which vault ids exist, their sizes and timing, never contents or keys.

## 4. How is a request to erase handled?

Deletion works, and it is final. When a vault is deleted, it is removed from the server, and a small marker is written so that the same vault can never be uploaded again under that id. From the command line, `sgit vault delete-on-remote` does it with the vault's write key and a typed confirmation.

Two things make erasure stronger than in most systems. Without its key, a vault's ciphertext is unreadable, so destroying the key is itself a form of erasure, for any copy anywhere. And on your own server, you set the storage rules: whether the bucket keeps old versions, and for how long backups live, which is what your assessment should state. One honest limit: anyone who already cloned a vault keeps their copy; deletion stops future access, not past copies.

## 5. What if the clinic's key is lost?

Then the vaults it protects are lost. That is the zero-knowledge deal: nobody, including us, can recover a vault without its key, and that is the property that makes it safe for patient data in the first place. So plan the backup before the first patient:

- **Seal the clinic's key to two or more custodians,** each with their own key pair, so no single person or device is a single point of failure ([PKI everywhere](pki-everywhere.md)).
- **Keep an offline copy as a QR code,** printed and locked away, for the day every device is gone.
- **A password manager** for the people who hold it day to day; never a chat, an email or a document.
- **Rotate** when someone leaves: `sgit vault rekey` replaces the key and re-encrypts the content.

## 6. Per-patient access tokens?

The only token the server checks is the one that authorises uploads, and it is an authorisation level, not a key: it lets a vault be updated on that server. It cannot read anything, and it cannot change a vault on its own: making changes needs the vault's key and its identity. So per-patient security does not come from server tokens. It comes from each patient's vault having its own key, and, for letting a patient or another system add to a vault without being able to read it, from append lanes.

## 7. Writing to a vault from another site

That is what append lanes are for. A lane is a write-only channel attached to a vault: each sender gets its own token, writes with no account, and learns nothing, not even whether anyone else writes there. A form on another of the clinic's sites seals the patient's answers to the clinic's public key in the browser and writes them to the lane; only the clinic can read them ([an inbox only your agents can write to](an-inbox-only-your-agents-can-write-to.md)). One detail to plan for: when our documentation was last checked, the lane routes were on the development service only, so this is another reason to run your own server.

## QR codes, and how this scales

QR codes carry keys and links: swap public keys, seal the vault link to the patient's key, back up the clinic key.

The thread running through these answers is how keys and links travel. Our answer is public key cryptography, made friendly with QR codes, on [pki.sgit.ai](https://pki.sgit.ai/): each browser makes its own key pair; a public key is shown as a QR code; and a message sealed to someone's key becomes a link, `pki.sgit.ai/m/#m1…`, and a QR code, signed by the sender and with an expiry ([a secret is a QR code](a-secret-is-a-qr-code.md)).

For a clinic, that means: the clinic and the patient swap public keys by scanning each other's QR codes, once; the clinic seals the patient's vault link to the patient's key, and the patient opens it in their own browser; and the clinic's own key is backed up sealed to its custodians. No key ever travels in clear, and nothing about a patient sits in an email.

And it scales, because it is the same pattern for everyone: a clinic, a person onboarding to their own agentic cell ([your own agentic cell, end to end](your-own-agentic-cell.md)), an agent getting its first key. The point is to empower the people building it, not to sit in their path.

## What this does not claim

- **No live date** for the doctor console on our hosted service.
- **This is not legal advice:** a data protection impact assessment is the organisation's own.
- **Append lane routes were on the development service** when last documented; check your deployment.
- **Deletion stops future access,** not copies someone already made.

## Where this comes from

The team's questions of 17 November 2026, and my answers the same day; sgit.ai's documentation on [key management](https://sgit.ai/docs/key-management.html) and [append lanes](https://sgit.ai/api/append-lanes.html); the SG/Send deployment guides published at [sgit.ai/deploy](https://sgit.ai/deploy/); [pki.sgit.ai](https://pki.sgit.ai/). Earlier on this site: [deploy sgit in your own environment](deploy-sgit-from-ci.md), [PKI everywhere](pki-everywhere.md), [a secret is a QR code](a-secret-is-a-qr-code.md), [an inbox only your agents can write to](an-inbox-only-your-agents-can-write-to.md).

## Threads

Agents & policySite & engineering[This article as a graph →](graphs.md#patient-vaults-answered)

### Builds on

- [Deploy sgit in your own environment, from a CI pipeline: one Docker image, ciphertext in your own S3 bucket in the region you choose, an access token only you hold, and the pipeline pattern we learned building the AgentiCCells site factory, a protected environment, AWS through OpenID Connect with no keys, a role that trusts one repository and one environment, check workflows before anything real, and a full cycle that deploys, tests and tears down](deploy-sgit-from-ci.md) Run your own sgit server in your own AWS account and region, deployed from CI with the site factory's pattern: OIDC, no keys, checks first.
- [PKI everywhere: from now on every message, secret and handover starts with a signature, and how an agent gets its first key](pki-everywhere.md) From now on every message, secret and handover is signed. The hard part is an agent's first key: two patterns, one built and one proposed.
- [An inbox only your agents can write to: a conductor publishes one append lane per agent, each lane's token sealed to that agent's own key, so everything needed to talk privately is public and only the right agent can use it](an-inbox-only-your-agents-can-write-to.md) A conductor publishes one append lane per agent, each token sealed to that agent's key: a private channel built from public material.
- [A secret is a QR code and a link to a public key: the workflow the QR experiment opens, who else already does this, and a format to share](a-secret-is-a-qr-code.md) Send a QR code and a link to a public key: the workflow the QR experiment opens, who already does this, and a format to share.
- [Your own agentic cell, end to end: how a person asks for a site like the ones we made for Yiheng Wang and Silvio Switha, through a key pair in the browser, a vault they fill themselves and the site factory, with only three human gates, and then continues in their own Claude on their own repository](your-own-agentic-cell.md) How a person gets their own agentic cell: a key pair in the browser, a vault they fill themselves, the site factory, and then their own Claude.

### Continued by

- [Who wrote it, who steered it, who signs it: the provenance model PrompTugal.news adopted today, a type label, five axes and a ladder from "published by an agent" to "on the record", applied to seven articles on this site, and what the ladder cannot see yet, how much of the author is in a piece, the brief, the corrections and months of background](who-steered-this.md) PrompTugal.news's provenance model, a label, five axes and a ladder, applied to seven articles here, and the two measures it misses.
- [Keys after payment: how to hand vault keys and access keys to customers once they have paid, what Stripe does and does not do after the money is taken, what FastSpring, Paddle, Lemon Squeezy, Polar, Gumroad and Square offer instead, and a design where the key is sealed to the buyer's own public key, keys are stock, and a payment provider can sell them without ever holding one](keys-after-payment.md) How to hand vault and access keys to customers after payment: what Stripe and others do, and a design that seals each key to the buyer's own key.
- [Your own agentic cell, end to end: how a person asks for a site like the ones we made for Yiheng Wang and Silvio Switha, through a key pair in the browser, a vault they fill themselves and the site factory, with only three human gates, and then continues in their own Claude on their own repository](your-own-agentic-cell.md) How a person gets their own agentic cell: a key pair in the browser, a vault they fill themselves, the site factory, and then their own Claude.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 450 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=450)

**Posting this article on LinkedIn?** The cover is [patient-vaults-answered.jpg](banners/patient-vaults-answered.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/patient-vaults-answered.html)*
