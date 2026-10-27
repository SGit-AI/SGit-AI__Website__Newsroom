---
title: The reading account, as built: the meter, the credit, Stripe top-ups and the account in your own vault are running today; checking each payment and signing it is what is proposed
date: 2026-10-21
author: Dinis Cruz
author_url: about/index.html
summary: An agent that helps me write emails read our articles and told a reader that the meter and the credit kept in the reader's own vault were a proposal, and that nothing of it was built. That is wrong, and the fault is ours: no single page says what is running. So here it is. Built and in use: the meter, which charges each page by how much of it was read; £5 of starting credit; a £5 top-up through Stripe, live since 11 October; and the reading account in the reader's own vault, opened with a passkey, with one file per device, a balance consolidated across devices, devices you can merge, notes, and a lane any browser can write to, even one where the passkey does not work. The server only ever sees ciphertext. I use it every day: my balance is down to £2, so I am about to top up again, and my vault shows every device I have read on and every page I opened. What is proposed, and not built, is the next layer from the user keeps the meter: checking each payment against Stripe afterwards, and signing the result into a vault both sides write to, so credit is validated or not valid. The page a payment returns to says so plainly today: it adds the credit, and it does not verify the payment.
version: v0.13.33
license: https://creativecommons.org/licenses/by/4.0/
tags: meter, payments, vaults, reading-account, status, article
status: published
---

!shot rb-built.webp | images/ | The reading account, piece by piece: what is built, and what is proposed. | comparison

## In short {#in-short}

- **The meter, the credit and Stripe top-ups are running.** Since October.
- **The account is in the reader's own vault.** One file per device, opened with a passkey.
- **The balance is consolidated across devices.** A payment on two devices counts once.
- **Any browser can write to your vault.** Even one where the passkey does not work.
- **The server sees ciphertext.** Nothing else.
- **What is proposed is the check.** Payments validated against Stripe and signed, afterwards.
- **One page now says what is built.** This one.

## Why this page {#why}

One of the agents that helps me write emails read our articles and wrote, in a draft to a reader, that the meter and the credit kept in the reader's own vault, with payments validated and signed afterwards, were a proposal, and that none of it was built. Half of that is wrong. The meter and the credit kept in the reader's vault are built, and I use them every day. Only the second half, payments validated and signed afterwards, is a proposal.

The agent was not careless. It read [the user keeps the meter](/articles/the-user-keeps-the-meter.html), which describes the proposal and said the credit was "kept in the reader's browser", and it found no single page that said what runs today. That is a documentation gap, and this page fills it. The billing article now says the same.

## What is built {#built}

As it runs on this site today, checked against the code and the tests of this release:

- **The meter.** Every page charges a few pence, by how much of it was actually read; a page scrolled through in seconds stays at the minimum. The balance can go below zero until you top up, which is the idea in [paying after the value](/articles/paying-after-the-value.html).
- **£5 of starting credit.** One starting credit per account, however many devices you read on.
- **Top up with Stripe.** A £5 payment link, live since 11 October. The page the payment returns to adds the credit, once per payment reference.
- **The account in your own vault.** Opened with a passkey. Each device writes one file with the records it made, every read with its depth, every top-up, every note, and never totals.
- **A balance across devices.** Computed from every device's records each time, with one starting credit; the same payment seen on two devices counts once.
- **Your devices, listed and merged.** The vault shows every device you have read on; duplicates can be merged, keeping every read and every payment, as [the vault, opened](/articles/the-vault-opened.html) describes.
- **Notes, and send to my vault.** Notes kept as you read travel with the account. And a browser that cannot reach your passkey can still write to a lane on your vault, through a link that carries only where to write and the public key, as in [sixteen notes I did not want to lose](/articles/sixteen-notes-i-did-not-want-to-lose.html).
- **The server sees ciphertext.** The test that opens the account on three devices checks that what reached the server is "ciphertext: no path, no record, no key in the clear".

## What it looks like from here {#mine}

I use all of this every day. My balance is at £2, so I am at the point where I will buy more credit. When I open my vault, I can see every device I have read on, and every page I opened on each. Records from a browser where the passkey does not work came in through the lane. For something with no server keeping the balance, it is quite powerful, and it is the base the billing design builds on.

## What is proposed {#proposed}

The next layer is the one [the user keeps the meter](/articles/the-user-keeps-the-meter.html) designs, and none of it is built yet:

- **Payments checked against Stripe.** Today the page a payment returns to says it plainly: it "adds the top-up to the balance kept in this browser, once per payment reference, and it does not, and cannot, verify the payment." The proposal is an admin side that reconciles each payment with Stripe later, from its own browser.
- **Signed validations.** The result written into a vault both the reader and we can write to, signed by us, so credit is unvalidated, validated, or not valid, and anyone can check it.
- **One account across our sites.** At user.sgit.ai or billing.sgit.ai, so the same credit works on every sgit.ai site.

## What this does not claim {#limits}

- **As of this release.** Checked against the code and tests of 21 October 2026.
- **Top-ups are not verified.** The return page trusts the payment reference; that is the gap the proposal closes.
- **The vault is optional.** Without a passkey, the account stays in the browser.
- **The email agent's draft is paraphrased.** To correct it, not to blame it; the missing page was ours.

## Where this comes from {#sources}

The reader's account code (the meter, the sync between the browser and the vault, the vault pane and the lane), the page Stripe returns to, and the test logs of this release, read on 21 October 2026; my own account, as I use it; and a draft from the agent that helps me with email, paraphrased to correct it. Related: [the user keeps the meter](/articles/the-user-keeps-the-meter.html), [paying after the value](/articles/paying-after-the-value.html), [the vault, opened](/articles/the-vault-opened.html), [sixteen notes I did not want to lose](/articles/sixteen-notes-i-did-not-want-to-lose.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
