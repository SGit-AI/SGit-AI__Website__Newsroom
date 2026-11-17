---
title: Patient vaults, answered point by point: the seven questions a healthcare team asked before putting any real patient data into sgit vaults, on the live date, the patient's address, the storage region, erasure, backing up the clinic's key, per-patient tokens and writing from another site, and why QR codes and public keys are how a clinic and its patients should pass keys and links
date: 2026-11-17
author: Dinis Cruz
author_url: about/index.html
summary: A healthcare team building encrypted patient vaults with their own agents, pointed at our public repositories, sent me seven careful questions before putting any real patient data in. Everything so far had been design work with invented data, which is exactly right. Their questions are the ones every health organisation should ask, so here are the answers, point by point. There is no live date for the doctor console yet; test on our development service with invented data, and for real data run your own server, at the version you tested. A patient's details live in the patient's own vault, opened from a link the clinic gives them. The storage region is whichever you choose, once you deploy into your own AWS account. Erasure works: a deleted vault is removed from the server and a marker stops that vault id ever being uploaded again, and without its key any copy is unreadable anyway. If the clinic's key is lost, the vault is lost, which is the zero-knowledge deal, so seal it to two or more custodians and keep an offline copy. The server's token only authorises uploads; making changes needs the vault key and its identity, and per-patient writing is what append lanes are for, including from another website. And underneath it all, QR codes: public keys swapped as QR codes, and links sealed to a patient's key, so no key ever travels in clear.
version: v0.14.137
license: https://creativecommons.org/licenses/by/4.0/
tags: sgit, vaults, healthcare, privacy, gdpr, pki, qr-codes, article
status: published
---

!shot hcq-answers.webp | images/ | Seven questions from a healthcare team, answered: live date, address, region, erasure, keys, tokens, writing. | table

## In short {#in-short}

- **A healthcare team asked seven questions** before putting real patient data into vaults; good questions, asked at the right time.
- **No live date** for the doctor console: test on dev with invented data, and run your own server for real data.
- **Region: yours to choose,** in your own AWS account.
- **Erasure works:** the vault is removed and its id can never be reused; without a key, copies are unreadable.
- **Lose the clinic key, lose the vault:** so seal it to custodians and keep an offline QR copy.
- **The server token only authorises uploads;** changes need the vault key.
- **QR codes and public keys** pass keys and links, never in clear.

## The questions {#context}

A healthcare team, who learned to build with agents only last week, has been designing patient vaults for a clinic: patient vaults created from the clinic's vault, keys held in custody, writable links for patients. They pointed their agents at our public repositories, checked the facts, and then, before putting a single real patient record in, sent me seven questions. Nothing real has been used: everything so far is design work with invented data.

That is exactly the right order, and the questions are the ones any health organisation should ask, for its data protection impact assessment and for its patients. If you are deploying sgit in a healthcare environment, these are your answers too.

## 1. When will the doctor console be live? {#live}

I do not have a date. The doctor console's features run on our development service, dev.vault.sgraph.ai, and not yet on vault.sgraph.ai. My advice is not to wait for us. Keep testing on dev with invented data, and when real data is close, run your own server, from your own pipeline, at the exact version you tested ([deploy sgit in your own environment](/articles/deploy-sgit-from-ci.html)). Then your live date is yours.

## 2. Which address should patients use? {#address}

The patient's details live in the patient's own vault, encrypted on the device, and nowhere else: not in a database the clinic runs, and not in a message thread. The patient opens that vault from a link the clinic gives them, on the deployment the clinic uses, ideally as a link sealed to the patient's own key and shown as a QR code (below). The old address in our June notes no longer serves the app; once you run your own server, the address is your own domain.

## 3. Where are the vaults stored? {#region}

In the region you choose. Run your own server and its S3 bucket is named after your account and your region, `{account}--sgraph-send-transfers--{region}`; nothing in the deployment templates is region-specific, so London, Frankfurt or Ireland is a parameter. That is the answer a data protection impact assessment wants: our own account, in this region, run by our own pipeline. And whatever the region, the host holds ciphertext only; it sees which vault ids exist, their sizes and timing, never contents or keys.

## 4. How is a request to erase handled? {#erasure}

Deletion works, and it is final. When a vault is deleted, it is removed from the server, and a small marker is written so that the same vault can never be uploaded again under that id. From the command line, `sgit vault delete-on-remote` does it with the vault's write key and a typed confirmation.

Two things make erasure stronger than in most systems. Without its key, a vault's ciphertext is unreadable, so destroying the key is itself a form of erasure, for any copy anywhere. And on your own server, you set the storage rules: whether the bucket keeps old versions, and for how long backups live, which is what your assessment should state. One honest limit: anyone who already cloned a vault keeps their copy; deletion stops future access, not past copies.

## 5. What if the clinic's key is lost? {#backup}

Then the vaults it protects are lost. That is the zero-knowledge deal: nobody, including us, can recover a vault without its key, and that is the property that makes it safe for patient data in the first place. So plan the backup before the first patient:

- **Seal the clinic's key to two or more custodians,** each with their own key pair, so no single person or device is a single point of failure ([PKI everywhere](/articles/pki-everywhere.html)).
- **Keep an offline copy as a QR code,** printed and locked away, for the day every device is gone.
- **A password manager** for the people who hold it day to day; never a chat, an email or a document.
- **Rotate** when someone leaves: `sgit vault rekey` replaces the key and re-encrypts the content.

## 6. Per-patient access tokens? {#tokens}

The only token the server checks is the one that authorises uploads, and it is an authorisation level, not a key: it lets a vault be updated on that server. It cannot read anything, and it cannot change a vault on its own: making changes needs the vault's key and its identity. So per-patient security does not come from server tokens. It comes from each patient's vault having its own key, and, for letting a patient or another system add to a vault without being able to read it, from append lanes.

## 7. Writing to a vault from another site {#append}

That is what append lanes are for. A lane is a write-only channel attached to a vault: each sender gets its own token, writes with no account, and learns nothing, not even whether anyone else writes there. A form on another of the clinic's sites seals the patient's answers to the clinic's public key in the browser and writes them to the lane; only the clinic can read them ([an inbox only your agents can write to](/articles/an-inbox-only-your-agents-can-write-to.html)). One detail to plan for: when our documentation was last checked, the lane routes were on the development service only, so this is another reason to run your own server.

## QR codes, and how this scales {#qr}

!shot hcq-qr.webp | images/ | QR codes carry keys and links: swap public keys, seal the vault link to the patient's key, back up the clinic key. | process

The thread running through these answers is how keys and links travel. Our answer is public key cryptography, made friendly with QR codes, on [pki.sgit.ai](https://pki.sgit.ai/): each browser makes its own key pair; a public key is shown as a QR code; and a message sealed to someone's key becomes a link, `pki.sgit.ai/m/#m1…`, and a QR code, signed by the sender and with an expiry ([a secret is a QR code](/articles/a-secret-is-a-qr-code.html)).

For a clinic, that means: the clinic and the patient swap public keys by scanning each other's QR codes, once; the clinic seals the patient's vault link to the patient's key, and the patient opens it in their own browser; and the clinic's own key is backed up sealed to its custodians. No key ever travels in clear, and nothing about a patient sits in an email.

And it scales, because it is the same pattern for everyone: a clinic, a person onboarding to their own agentic cell ([your own agentic cell, end to end](/articles/your-own-agentic-cell.html)), an agent getting its first key. The point is to empower the people building it, not to sit in their path.

## What this does not claim {#limits}

- **No live date** for the doctor console on our hosted service.
- **This is not legal advice:** a data protection impact assessment is the organisation's own.
- **Append lane routes were on the development service** when last documented; check your deployment.
- **Deletion stops future access,** not copies someone already made.

## Where this comes from {#sources}

The team's questions of 17 November 2026, and my answers the same day; sgit.ai's documentation on [key management](https://sgit.ai/docs/key-management.html) and [append lanes](https://sgit.ai/api/append-lanes.html); the SG/Send deployment guides published at [sgit.ai/deploy](https://sgit.ai/deploy/); [pki.sgit.ai](https://pki.sgit.ai/). Earlier on this site: [deploy sgit in your own environment](/articles/deploy-sgit-from-ci.html), [PKI everywhere](/articles/pki-everywhere.html), [a secret is a QR code](/articles/a-secret-is-a-qr-code.html), [an inbox only your agents can write to](/articles/an-inbox-only-your-agents-can-write-to.html).
