# The user keeps the meter: a proposed design for user management, activity and billing on vaults, with one billing vault per user, two signed writers, and one light check at the server, sgit.ai

> Billing is usually a server problem: a server, a database, a balance every action has to update, race conditions, and either a bottleneck or a scheduler to keep it all in step. This is an exploration of doing it the other way round, on the client, with vaults. Each user gets a billing vault that both they and I can write to. The user's browser meters its own activity and appends it there, signed with the user's key, the way this newsroom's meter already works. When the user pays, their browser adds the credit straight away, so they can carry on. My admin vault, which can be offline for a while, later reconciles payments with Stripe, from my browser, and commits a validation back into the user's vault, signed with the admin key, so anyone can check it. Credit is then unvalidated, validated, or not valid, and the product keeps working on unvalidated credit, because on the client it costs us nothing. Since the vault's first commit is pinned and every commit is signed, we always know who wrote what. The one server left, the sgit upload server, does a light check only: is the key valid, and is there credit, read from a cached, signed value through a small credits API. Four parties, each with its own key: the admin vault, the user, the upload server and the API. And because the user's data lives in their vault, it travels with them across our sites. It is all PKI from here. Where it lives is open: user.sgit.ai, or billing.sgit.ai, so others can use it too. This is a proposal, with the open questions written down.

*Source: <https://newsroom.sgit.ai/articles/the-user-keeps-the-meter.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The user keeps the meter: a proposed design for user management, activity and billing on vaults, with one billing vault per user, two signed writers, and one light check at the server

# The user keeps the meter: a proposed design for user management, activity and billing on vaults, with one billing vault per user, two signed writers, and one light check at the server

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-21 · [article v1.2.0, 3 versions](versions/the-user-keeps-the-meter.md) · [newsroom v0.13.13](https://newsroom.sgit.ai/admin/versions.html) · vaultsbillingpkiarchitectureproposalarticle

***Abstract:** Billing is usually a server problem: a server, a database, a balance every action has to update, race conditions, and either a bottleneck or a scheduler to keep it all in step. This is an exploration of doing it the other way round, on the client, with vaults. Each user gets a billing vault that both they and I can write to. The user's browser meters its own activity and appends it there, signed with the user's key, the way this newsroom's meter already works. When the user pays, their browser adds the credit straight away, so they can carry on. My admin vault, which can be offline for a while, later reconciles payments with Stripe, from my browser, and commits a validation back into the user's vault, signed with the admin key, so anyone can check it. Credit is then unvalidated, validated, or not valid, and the product keeps working on unvalidated credit, because on the client it costs us nothing. Since the vault's first commit is pinned and every commit is signed, we always know who wrote what. The one server left, the sgit upload server, does a light check only: is the key valid, and is there credit, read from a cached, signed value through a small credits API. Four parties, each with its own key: the admin vault, the user, the upload server and the API. And because the user's data lives in their vault, it travels with them across our sites. It is all PKI from here. Where it lives is open: user.sgit.ai, or billing.sgit.ai, so others can use it too. This is a proposal, with the open questions written down.*

The proposed design. The user's browser appends its activity, and adds credit when it pays, to a billing vault, signed by the user. The admin vault reads it, reads payments from Stripe, and commits validations back, signed by the admin. The upload server checks the validated credit through a small credits API before it accepts an upload.

## In short

- **Billing is usually a server problem.** A database, a balance every action updates, and races.
- **This proposal does it on the client.** Each user has a billing vault; their browser keeps the meter.
- **Two writers, two keys.** The user signs activity; the admin signs the validation of credit.
- **Credit now, validated later.** The user carries on straight away; the admin side catches up.
- **Stripe is reconciled from the admin's browser.** Payments are read, matched and validated.
- **One server, one light check.** The upload server asks: is the key valid, and is there credit?
- **The user's data travels with them.** Across every site, because it lives in their vault.
- **It is a proposal.** Nothing here is built yet, and the open questions are written down.

## The old problem

Every time I have built billing, it has been the same shape. You need a server and a database. Every action a user takes has to update something central, a balance, a usage count, and the moment two actions arrive at once you have a race condition on that balance. You can try to make a file the single source of truth, but keeping one file in sync across many writers is hard.

The usual way out is to append first and update later: write every event to a log, and work out the balance from it. But then either every action goes through the thing that updates the balance, and it becomes the bottleneck, or the update runs on a schedule, a cron job or a set of Lambda functions, which works, and is messy, and is one more thing to run, watch and pay for.

## What we already have

What made me look at this again is that most of the pieces already exist on our sites.

**A meter in the reader's browser.** This newsroom already charges per use, without a server keeping the balance: every reader starts with £5 of credit, each page draws a few pence from it, the credit is kept in the reader's browser, and the balance can go below zero until they top up with a £5 payment link, live since 11 October. I wrote about why in [paying after the value](paying-after-the-value.md).

**Append lanes.** A vault can have a lane that others write to and only its owner reads. On this site that is already in use: in [the editor's channel](the-editors-channel.md), "An append lane on the reader vault that any browser with a link can write to and none can read, with a key pair made in the reader's browser". And from [secrets on public keys](secrets-on-public-keys.md): "Append lanes are already write-only inboxes, read with an enum key, and this site has measured a hundred writers on one."

**Version control.** A vault is versioned. Every change is a commit, and two writers' changes can be seen, ordered and merged, which is exactly what a balance kept in a file was missing.

**Keys.** [PKI everywhere](pki-everywhere.md) set the direction: every message, secret and handover starts with a signature, and the public keys live in a register, at pki.sgit.ai, that anyone can check.

## The idea: the user keeps the meter

So the idea is to do user management, activity tracking and billing on the client, with vaults. Where it lives is a question in itself. It could be user.sgit.ai, with api.user.sgit.ai for its client code. Or, because we want it to be easy for others to use, our other sites and other people's, the billing part could stand on its own: billing.sgit.ai, with api.billing.sgit.ai. Either way, the API sites would be released the same way as our others.

The insight that makes it work is a simple one. A user very rarely runs several clients at the same time. The race condition that hurts a central server, many writers on one balance, mostly does not exist for one person's own activity. And for the cases where it does, two tabs or a laptop and a phone, the vault's version control already does the merging.

So each user has a vault that tracks their own activity. Their browser collects what they do, at intervals, and appends it to a lane in that vault. That is the same model as this newsroom's meter, use first, then buy or top up, but with the record kept in a vault rather than only in one browser, so it can be backed up, synced, checked and billed.

## Two writers, two keys

The design settles on one billing vault per user, which two parties can write to.

**The user writes activity.** Their browser commits what they used, signed with the user's key. That record belongs to them: they can read it, keep it and take it elsewhere.

**The admin validates credit.** When the user comes back from paying, their browser adds the credit straight away, with a signed claim. Later, the admin side checks that claim against Stripe and commits a validation into the same vault, signed with the admin key. Because it is signed, anyone can verify it against the admin's public key, and nobody else, the user included, can write a validation that verifies.

A validation record could be as small as this. The field names are a sketch, not a format:

```

{
  "billing_vault": "the vault's id",
  "claims": [
    { "claim": "the user's claim commit", "stripe_event": "the event's id",
      "pence": 500, "status": "validated" }
  ],
  "validated_balance_pence": 4210,
  "covers_activity_to": "the last activity commit counted",
  "as_of": "2026-10-21T10:00:00Z",
  "valid_until": "2026-10-28T10:00:00Z",
  "signed_by": "the admin key's fingerprint",
  "signature": "over everything above"
}

```

Each side signs only what it is responsible for. The user can add credit their browser believes in, but cannot make it validated, and the admin cannot invent activity the user did not sign.

## The admin vault, and Stripe

The other half is a central admin vault, which I control. Usage data flows into it from the users' vaults: close to anonymised, but tied to the user, so it can be billed. And it is where payments are reconciled with Stripe, from the admin's browser.

How that reconciliation should work needs some care, because of how Stripe works:

- **Webhooks need a server.** Stripe's documentation says "Registered webhook endpoints must be publicly accessible HTTPS URLs", and its webhooks are signed with a shared secret, an HMAC with SHA-256, not with a public key. That does not fit a design with no server to receive them.
- **So the admin side reads instead.** Stripe's API can "List events, going back up to 30 days", so the admin's browser can pull recent payments when it runs, rather than wait for a push.
- **The key that reads Stripe stays on the admin's machine.** Stripe is plain that "Only publishable keys are safe to expose outside your application's backend". The admin's browser, on my machine, plays the role of that backend, with a restricted key that can only read.
- **A payment can say which vault it is for.** A payment link can carry a `client_reference_id`, which Stripe describes as "a unique string of your choice", and returns with the completed payment. It should be the billing vault's id, never anything secret.

So the flow is: the user is sent to Stripe with a payment link tagged with their billing vault; Stripe sends them back to a page that gives them the credit, and their browser adds it straight away and appends a signed claim, "I paid"; later, the admin's browser lists recent payments, matches each claim to a payment, and commits a signed validation. Two-way sync between the two vaults, with each side writing only its own records.

A top-up, step by step. The user pays through a payment link, comes back, and their browser adds the credit straight away with a signed claim. Later, the admin's browser reads recent payments from Stripe, matches the claim, and commits a signed validation. The upload server reads that validation and checks it.

## Credit now, validated later

When should a payment count? The user should be able to use what they paid for straight away. That has to be immediate. So the credit goes into their browser the moment they come back from Stripe, and they carry on.

The check comes afterwards, as a layer on top. The admin side does not need to be online when the user pays; it can catch up hours later. When it does, it adds a note to the user's vault, signed by us as the commercial authority: payment validated, or payment not accepted. Nothing central sits in the path of the user's work. The product keeps working, and the credit simply moves from unvalidated to validated.

So credit can be in one of three states:

- **Credit not yet validated.** The user paid, or says they did, and the admin side has not checked yet. Normal, and short-lived.
- **Credit validated.** The admin side matched it to a payment in Stripe, and signed it.
- **Credit not valid.** No matching payment. In our case this is unlikely: it means an attack, or a bug.

That is why the product should carry on with the credit the user has, validated or not. Most of what it meters runs on the client, so letting a user carry on with unvalidated credit costs us nothing. And Stripe's own guidance fits this order: "You can't rely on triggering fulfillment only from your checkout landing page, because your customers aren't guaranteed to visit that page." The admin side reads Stripe directly, so a payment whose user never came back can still be credited, and one that is slow to confirm, like a bank debit, which "can take 2-14 days to confirm the payment", simply stays unvalidated for longer.

## Who are we defending against?

The question that sizes this design is the one in [who are you protecting against?](https://newsroom.sgit.ai/articles/who-are-you-protecting-against.html). Here, the party that could cheat is the user, by gaming the client: adding credit they did not pay for, or leaving out activity. In the short term that is unlikely, and it is also very easy to detect. Every claim has to match a payment in Stripe, every commit is signed, and a claim with no payment behind it shows up as not valid the next time the admin side runs.

So the design does not try to make cheating impossible on the client. It makes it visible, and it puts the hard check where a mistake would cost us money: at the server.

## A vault shared by two parties

There is a more general idea underneath this. The billing vault is shared by an untrusted party, the user, and a trusted one, us. Once the vault exists, we pin its first commit. From then on, every later commit can be checked for consistency against it: that it descends from that first commit, and that it is signed by a key we know.

That gives a two-way channel between the two parties, through the vault, where we always know who did what. The user writes activity and claims; we write validations; and because of PKI, neither can pass off their writing as the other's. Billing is the first use, and the same pattern fits any place where a user and a service need to keep a shared record that both can trust.

## The one server left

Most of our sites already run with no server of their own. The one that remains in this picture is the sgit upload server, which stores vaults, and it is also where usage costs us money, in storage and transfer. So that is where the check belongs, and it should stay light:

- **Is the key valid?** A PKI check, against the register.
- **Is there credit?** A read of the user's latest signed validation record, verified against the admin's public key.

The upload server should not compute a balance or keep a database of its own. It reads a cached, signed value, through a small credits API with its own simple definition, separate from the rest. A cached value can be slightly out of date, so the record carries a `valid_until`, and the upload server can also count what it serves, so the units that cost real money are measured where they happen, not reported by the client.

Today, the access key gates use of the upload server, but it does not meter it: vault creation, for example, is not tracked per user. That is the gap this design fills.

## Four parties

Put together, there are four parties, each with its own role and its own key:

- **The admin vault.** Writes the licensing and validation records, collects the usage, and reconciles with Stripe.
- **The user.** Commits their own activity, and owns the record of it.
- **The upload server.** The inline billing unit: checks the key and the credit before it does the work.
- **The credits API.** A simple read of the signed credit, so the server's check stays small and cacheable.

## What the user gets

This is not only a billing design. Once a user is logged in, their data lives in their vault, and it travels with them across all of our sites: what they read, what they set, what they bought, their keys and their preferences. A logged-in user gets a better experience on every site, without each site keeping a copy of them on a server.

## What it trusts, and what it does not

- **Activity reported by the browser is on trust.** The same as this newsroom's meter, where the reader can set the price of a page. That is fine where the cost to us is small.
- **What costs us real money is counted at the server.** Storage and transfer are measured where they happen.
- **Validated credit cannot be forged by the user.** It needs the admin's signature. Unvalidated credit could be, and it would show up as not valid.
- **A cached record can be a little stale.** So it carries an end date.
- **The admin key matters most.** It should live where [PKI everywhere](pki-everywhere.md) says keys should: made on the device, never exported.

## Open questions

- **Where does it live?** user.sgit.ai and api.user.sgit.ai, or billing.sgit.ai and api.billing.sgit.ai, so others can use it easily.
- **Should the upload server accept unvalidated credit?** Where usage costs us real money, it may want only validated credit, or a small amount on top.
- **Who creates the first vault?** Maybe we create a user's first vault for them, when they first log in. For now the design assumes the vault already exists.
- **How does login work?** It should start with a PKI handshake, as everything now does.
- **How anonymous is the usage?** The admin vault needs enough to bill, and should get no more.
- **How often does the browser sync?** Often enough to bill, not so often it slows the user down.
- **How are refunds and disputes written?** Probably as signed validation records too, with their own status.

## The versioned API sites

api.user.sgit.ai, or api.billing.sgit.ai, would follow the rule our other API sites already use, written down on [api.send.sgit.ai](https://api.send.sgit.ai/articles/independent-releases.html): every release is a complete, independent copy at its own versioned path, never edited after it is published, with a manifest of hashes. A site pins the version it uses, so a change to the API is a new version, not an edit to an old one. This newsroom has not written about that rule yet; it should, and it is now on the list.

## What this does not claim

- **Nothing here is built.** Neither user.sgit.ai nor billing.sgit.ai exists yet.
- **The record formats are sketches.** The field names will change.
- **The Stripe flow is not tested.** Its constraints are from Stripe's documentation, read on 21 October 2026.
- **Client-reported activity is not proof.** The design says where it is trusted and where it is counted.
- **The pieces it builds on exist.** The meter, the append lanes, the versioning and the key register are in use today.

## The diagrams, as source

The two diagrams above are Mermaid, rendered for this page. Here is their source, to reuse or correct.

```

flowchart TB
  U["User's browser<br/>meters its own use"]
  subgraph BV["Billing vault, one per user"]
    A["Activity and claims<br/>signed by the user"]
    C["Validations<br/>signed by the admin"]
  end
  AD["Admin vault<br/>in the admin's browser"]
  ST["Stripe"]
  API["Credits API<br/>a simple read"]
  UP["Upload server<br/>key valid? credit left?"]
  U -->|appends activity, adds credit| A
  A -->|synced| AD
  ST -->|payments, read by| AD
  AD -->|validates| C
  C -->|cached| API
  API --> UP
  U -->|uploads| UP

```

```

sequenceDiagram
  participant U as User's browser
  participant S as Stripe
  participant B as Billing vault
  participant A as Admin's browser
  participant P as Upload server
  U->>S: Pay with a payment link, tagged with the billing vault
  S-->>U: Back to a page that gives the credit
  U->>B: Add the credit now, with a signed claim
  Note over U,B: The user carries on straight away
  A->>S: Later: list recent payments, with a read-only key
  A->>B: Match the claim to the payment
  A->>B: Commit a signed validation, or not accepted
  P->>B: Read the signed validation, cached
  P->>P: Check the signature and the balance

```

## Where this comes from

Two voice memos of 21 October 2026. Stripe's documentation, read the same day: [webhooks](https://docs.stripe.com/webhooks), [API keys](https://docs.stripe.com/keys), [listing events](https://docs.stripe.com/api/events/list), [the success page](https://docs.stripe.com/payments/checkout/custom-success-page) and [payment link parameters](https://docs.stripe.com/payment-links/url-parameters). api.send.sgit.ai's [independent releases](https://api.send.sgit.ai/articles/independent-releases.html). Related: [paying after the value](paying-after-the-value.md), [who are you protecting against?](https://newsroom.sgit.ai/articles/who-are-you-protecting-against.html), [the editor's channel](the-editors-channel.md), [secrets on public keys](secrets-on-public-keys.md), [PKI everywhere](pki-everywhere.md), [free to copy, paid at the source](free-to-copy-paid-at-the-source.md). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Vaults & method[This article as a graph →](graphs.md#the-user-keeps-the-meter)

### Builds on

- [Paying after the value: why a balance that can go negative feels different from a subscription, the psychology behind it, and the experiment this newsroom is running](paying-after-the-value.md) Most purchases are bets on future value; a reading balance that can go negative asks for payment when the value is already in view.
- [The editor's channel: what I read, sign off and want changed, sent to the newsroom's agent in a vault](the-editors-channel.md) A key makes a browser an editor's: reads, sign-offs and fixes go to a vault, a daily pass acts and replies, and five lanes set what any reader sends.
- [secrets.sgit.ai on public keys: no more shared keys, eight ways a secret moves, a vault for the private key, and the commercial service it becomes](secrets-on-public-keys.md) secrets.sgit.ai becomes a service for moving a secret from A to B on public keys only: no shared keys, a vault for the private key, eight scenarios.
- [PKI everywhere: from now on every message, secret and handover starts with a signature, and how an agent gets its first key](pki-everywhere.md) From now on every message, secret and handover is signed. The hard part is an agent's first key: two patterns, one built and one proposed.
- [Free to copy, paid at the source: why an official website can charge per use for open policies and hooks, and why we will have them reviewed, audited and signed](free-to-copy-paid-at-the-source.md) Open policies and hooks, free to copy, can still earn per use at the official source, if others review them and we sign them.

### Continued by

- [The attack surface you do not have: every CVE now makes me smile, because moving to the client side took my servers out of the news, and the constraint turned out to be speed](the-attack-surface-you-do-not-have.md) Every CVE makes me smile: moving to the client side took my servers out of the news, and the constraint turned out to be speed.
- [Messaging-FS: an encrypted messenger between vaults, built on append lanes and PKI, from the first crude inbox to messages in the browser and on the command line](messaging-fs.md) A proposed encrypted messenger between vaults: append lanes for transport, PKI for trust, and Messaging-FS as the schema.
- [AWS from the vault: a proposed aws.twin.sgit.ai, where a temporary AWS session lives in the user's vault, the browser does the work, and AWS data finally has a place to go](aws-from-the-vault.md) A proposed aws.twin.sgit.ai: an AWS twin on a vault first, then a temporary AWS session from the user's vault.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 233 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=233)

**Posting this article on LinkedIn?** The cover is [the-user-keeps-the-meter.jpg](banners/the-user-keeps-the-meter.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-user-keeps-the-meter.html)*
