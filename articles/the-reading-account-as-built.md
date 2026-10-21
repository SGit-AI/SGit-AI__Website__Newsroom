# The reading account, as built: the meter, the credit, Stripe top-ups and the account in your own vault are running today; checking each payment and signing it is what is proposed, sgit.ai

> An agent that helps me write emails read our articles and told a reader that the meter and the credit kept in the reader's own vault were a proposal, and that nothing of it was built. That is wrong, and the fault is ours: no single page says what is running. So here it is. Built and in use: the meter, which charges each page by how much of it was read; £5 of starting credit; a £5 top-up through Stripe, live since 11 October; and the reading account in the reader's own vault, opened with a passkey, with one file per device, a balance consolidated across devices, devices you can merge, notes, and a lane any browser can write to, even one where the passkey does not work. The server only ever sees ciphertext. I use it every day: my balance is down to £2, so I am about to top up again, and my vault shows every device I have read on and every page I opened. What is proposed, and not built, is the next layer from the user keeps the meter: checking each payment against Stripe afterwards, and signing the result into a vault both sides write to, so credit is validated or not valid. The page a payment returns to says so plainly today: it adds the credit, and it does not verify the payment.

*Source: <https://newsroom.sgit.ai/articles/the-reading-account-as-built.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The reading account, as built: the meter, the credit, Stripe top-ups and the account in your own vault are running today; checking each payment and signing it is what is proposed

# The reading account, as built: the meter, the credit, Stripe top-ups and the account in your own vault are running today; checking each payment and signing it is what is proposed

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-21 · [article v1.0.0](versions/the-reading-account-as-built.md) · [newsroom v0.13.33](https://newsroom.sgit.ai/admin/versions.html) · meterpaymentsvaultsreading-accountstatusarticle

***Abstract:** An agent that helps me write emails read our articles and told a reader that the meter and the credit kept in the reader's own vault were a proposal, and that nothing of it was built. That is wrong, and the fault is ours: no single page says what is running. So here it is. Built and in use: the meter, which charges each page by how much of it was read; £5 of starting credit; a £5 top-up through Stripe, live since 11 October; and the reading account in the reader's own vault, opened with a passkey, with one file per device, a balance consolidated across devices, devices you can merge, notes, and a lane any browser can write to, even one where the passkey does not work. The server only ever sees ciphertext. I use it every day: my balance is down to £2, so I am about to top up again, and my vault shows every device I have read on and every page I opened. What is proposed, and not built, is the next layer from the user keeps the meter: checking each payment against Stripe afterwards, and signing the result into a vault both sides write to, so credit is validated or not valid. The page a payment returns to says so plainly today: it adds the credit, and it does not verify the payment.*

The reading account, piece by piece: the meter, £5 of starting credit, top-up with Stripe, the account in your vault, a balance across devices, devices merged, notes and send to my vault, and a server that sees only ciphertext, all built; checking payments against Stripe, signed validations and one account across our sites, proposed.

## In short

- **The meter, the credit and Stripe top-ups are running.** Since October.
- **The account is in the reader's own vault.** One file per device, opened with a passkey.
- **The balance is consolidated across devices.** A payment on two devices counts once.
- **Any browser can write to your vault.** Even one where the passkey does not work.
- **The server sees ciphertext.** Nothing else.
- **What is proposed is the check.** Payments validated against Stripe and signed, afterwards.
- **One page now says what is built.** This one.

## Why this page

One of the agents that helps me write emails read our articles and wrote, in a draft to a reader, that the meter and the credit kept in the reader's own vault, with payments validated and signed afterwards, were a proposal, and that none of it was built. Half of that is wrong. The meter and the credit kept in the reader's vault are built, and I use them every day. Only the second half, payments validated and signed afterwards, is a proposal.

The agent was not careless. It read [the user keeps the meter](the-user-keeps-the-meter.md), which describes the proposal and said the credit was "kept in the reader's browser", and it found no single page that said what runs today. That is a documentation gap, and this page fills it. The billing article now says the same.

## What is built

As it runs on this site today, checked against the code and the tests of this release:

- **The meter.** Every page charges a few pence, by how much of it was actually read; a page scrolled through in seconds stays at the minimum. The balance can go below zero until you top up, which is the idea in [paying after the value](paying-after-the-value.md).
- **£5 of starting credit.** One starting credit per account, however many devices you read on.
- **Top up with Stripe.** A £5 payment link, live since 11 October. The page the payment returns to adds the credit, once per payment reference.
- **The account in your own vault.** Opened with a passkey. Each device writes one file with the records it made, every read with its depth, every top-up, every note, and never totals.
- **A balance across devices.** Computed from every device's records each time, with one starting credit; the same payment seen on two devices counts once.
- **Your devices, listed and merged.** The vault shows every device you have read on; duplicates can be merged, keeping every read and every payment, as [the vault, opened](the-vault-opened.md) describes.
- **Notes, and send to my vault.** Notes kept as you read travel with the account. And a browser that cannot reach your passkey can still write to a lane on your vault, through a link that carries only where to write and the public key, as in [sixteen notes I did not want to lose](sixteen-notes-i-did-not-want-to-lose.md).
- **The server sees ciphertext.** The test that opens the account on three devices checks that what reached the server is "ciphertext: no path, no record, no key in the clear".

## What it looks like from here

I use all of this every day. My balance is at £2, so I am at the point where I will buy more credit. When I open my vault, I can see every device I have read on, and every page I opened on each. Records from a browser where the passkey does not work came in through the lane. For something with no server keeping the balance, it is quite powerful, and it is the base the billing design builds on.

## What is proposed

The next layer is the one [the user keeps the meter](the-user-keeps-the-meter.md) designs, and none of it is built yet:

- **Payments checked against Stripe.** Today the page a payment returns to says it plainly: it "adds the top-up to the balance kept in this browser, once per payment reference, and it does not, and cannot, verify the payment." The proposal is an admin side that reconciles each payment with Stripe later, from its own browser.
- **Signed validations.** The result written into a vault both the reader and we can write to, signed by us, so credit is unvalidated, validated, or not valid, and anyone can check it.
- **One account across our sites.** At user.sgit.ai or billing.sgit.ai, so the same credit works on every sgit.ai site.

## What this does not claim

- **As of this release.** Checked against the code and tests of 21 October 2026.
- **Top-ups are not verified.** The return page trusts the payment reference; that is the gap the proposal closes.
- **The vault is optional.** Without a passkey, the account stays in the browser.
- **The email agent's draft is paraphrased.** To correct it, not to blame it; the missing page was ours.

## Where this comes from

The reader's account code (the meter, the sync between the browser and the vault, the vault pane and the lane), the page Stripe returns to, and the test logs of this release, read on 21 October 2026; my own account, as I use it; and a draft from the agent that helps me with email, paraphrased to correct it. Related: [the user keeps the meter](the-user-keeps-the-meter.md), [paying after the value](paying-after-the-value.md), [the vault, opened](the-vault-opened.md), [sixteen notes I did not want to lose](sixteen-notes-i-did-not-want-to-lose.md). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Vaults & methodSite & engineering[This article as a graph →](graphs.md#the-reading-account-as-built)

### Builds on

- [The user keeps the meter: a proposed design for user management, activity and billing on vaults, with one billing vault per user, two signed writers, and one light check at the server](the-user-keeps-the-meter.md) A proposed design for billing on vaults: the user's browser keeps the meter, credit now and validated later, one light check at the server.
- [Paying after the value: why a balance that can go negative feels different from a subscription, the psychology behind it, and the experiment this newsroom is running](paying-after-the-value.md) Most purchases are bets on future value; a reading balance that can go negative asks for payment when the value is already in view.
- [The vault, opened: merging devices, reading every call to the vault server, browsing your vaults, and one viewer that every reader vault links and opens with](the-vault-opened.md) Merging devices, every call to the vault server named and opened, a page to browse your vaults, and one shared viewer that every reader vault opens with.
- [Sixteen notes I did not want to lose: a request to send from any browser to my vault, why identity is still this hard, and how two more wires became a product line](sixteen-notes-i-did-not-want-to-lose.md) Sixteen notes stuck in a browser with no passkey led to a request: let any browser send to my vault, by link, text or QR code.

### Continued by

- [The user keeps the meter: a proposed design for user management, activity and billing on vaults, with one billing vault per user, two signed writers, and one light check at the server](the-user-keeps-the-meter.md) A proposed design for billing on vaults: the user's browser keeps the meter, credit now and validated later, one light check at the server.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 252 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=252)

**Posting this article on LinkedIn?** The cover is [the-reading-account-as-built.jpg](banners/the-reading-account-as-built.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-reading-account-as-built.html)*
