---
title: Keys after payment: how to hand vault keys and access keys to customers once they have paid, what Stripe does and does not do after the money is taken, what FastSpring, Paddle, Lemon Squeezy, Polar, Gumroad and Square offer instead, and a design where the key is sealed to the buyer's own public key, keys are stock, and a payment provider can sell them without ever holding one
date: 2026-11-17
author: Dinis Cruz
author_url: about/index.html
summary: We now have things people want to buy: secure sends, vaults, access keys to our servers, and agentic cells. What they are buying, in the end, is a key. So we need a good way to hand a key to someone who has just paid, and today we do not have one. Our Stripe integration is a payment link, a payment, and a redirect. My research shows the picture is a little better than I thought, and still not enough. Stripe takes the money and screens fraud very well, sends a signed webhook and can put the session id in the redirect; it has products and prices, but no stock, it does not generate keys, and it knows nothing about the buyer's keys; its Workflows can chain Stripe's own actions after a payment, in preview, with custom code still in private preview. Others go further on keys: FastSpring can sell from a pre-defined list of keys, which is stock, or call your server; Paddle Classic did the same with an uploaded list; Lemon Squeezy, Polar and Gumroad generate keys per sale; Square has none. Not one of them seals a key to the buyer's own public key. So here is the design I want: the buyer's browser makes a key pair before checkout; Stripe takes the money; one small serverless function takes a key from our stock, seals it to the buyer's key, signs it, and hands it back as a link and a QR code that only they can open. And for stock managed by someone else: give the provider claim codes, not keys.
version: v0.14.139
license: https://creativecommons.org/licenses/by/4.0/
tags: payments, stripe, keys, pki, vaults, qr-codes, product, article
status: published
---

!shot kds-flow.webp | images/ | A key only the buyer can open: their key pair, Stripe for the money, our function seals the key, a QR code. | process

## In short {#in-short}

- **What we sell is, in the end, a key:** a vault key, an access key to a server, a cell.
- **Stripe takes the money well,** and stops there: no stock, no keys, no buyer keys.
- **Others do more:** FastSpring sells from a list of keys, Paddle Classic did, others generate keys.
- **None seals a key to the buyer's own public key.**
- **So: Stripe for the money, one serverless function for the key,** sealed and signed, shown as a QR code.
- **Keys as stock:** give a provider claim codes, not keys, and let it count them.

## The problem {#problem}

We now have good reasons for people to buy things from us: secure sends, vaults, access keys to our servers, and, since this week, their own agentic cells ([your own agentic cell, end to end](/articles/your-own-agentic-cell.html)). In almost every case, what they are buying, in the end, is a key: a vault key, an access token, a licence.

Our payments today are simple: I put a Stripe payment link on a page, the person goes to Stripe, pays, and is redirected back. That is all. What happens next, handing over the key, has to be built, and I wanted to know whether I was right that Stripe gives me nothing for it, and what the alternatives do.

## What Stripe does, and does not {#stripe}

I was partly right. Stripe is very good at the payment: checkout, cards and wallets, fraud screening, receipts. After the money, it gives you the building blocks and not the building:

- **A reference you choose.** A checkout session, or a payment link through a URL parameter, can carry a `client_reference_id`, up to 200 characters, which comes back in the webhook. Stripe warns not to put secrets in it ([Stripe](https://docs.stripe.com/payment-links/url-parameters)).
- **A signed webhook,** `checkout.session.completed`, and Stripe's advice to fulfil from the webhook, not the success page, because customers may never reach it, and to make fulfilment safe to run twice ([Stripe](https://docs.stripe.com/checkout/custom-checkout/fulfill-orders)).
- **A redirect** with the session id in it, so your own page can look the order up.
- **Products and prices,** but no stock: nothing counts how many keys are left.
- **Entitlements,** a list of features a customer has, which your app reads; Stripe does not enforce them for you.
- **Workflows,** in public preview: chains of Stripe's own API actions, run on events. Custom code, scripts on Stripe's runtime or your own remote functions, is in private preview ([Stripe](https://docs.stripe.com/workflows/custom-actions)).

What it does not do: generate keys, hold a batch of keys and sell them one at a time, or know anything about the buyer's own keys. There is no PKI for customers. So with Stripe, the key hand-over is ours to build.

## What the others do {#others}

!shot kds-providers.webp | images/ | Who can hand over a key after a payment: Stripe, FastSpring, Paddle, Lemon Squeezy, Polar, Gumroad, Square. | table

- **FastSpring** is the closest to what I wanted. A product can deliver keys from a pre-defined list you paste in, which is stock, from a script FastSpring runs, or from a call to your own server during the order, and shows the key on the completion page, in the receipt and in the account ([FastSpring](https://developer.fastspring.com/docs/license-key-fulfillments)).
- **Paddle Classic** did the same with an uploaded list, one key emailed per sale; when the list ran out, Paddle contacted you for more. Paddle Billing, its current platform, signals a completed transaction by webhook, and the rest is yours ([Paddle](https://www.paddle.com/help/start/set-up-paddle/which-fulfillment-method-to-choose)).
- **Lemon Squeezy, Polar and Gumroad** generate a key per sale and give you an API to validate it; I found no way to import your own keys into Lemon Squeezy, and Polar's validation is hosted, so not for offline use.
- **Square** takes payments and sends signed webhooks; a seller asking about product keys was told it does not issue them.

So the idea of keys as stock exists: FastSpring and Paddle Classic both sell from a list. But in every case the provider holds your keys in clear and hands them over in clear, by email or on a page. And not one of them knows the buyer's public key.

## The design I want {#design}

The ideal starts before the payment: the buyer already has a key pair. On our page, their browser makes one, with pki.sgit.ai's module, the private half never leaving the browser ([a secret is a QR code](/articles/a-secret-is-a-qr-code.html)). Then:

1. **Checkout** on Stripe, with the buyer's key fingerprint as the `client_reference_id`. A fingerprint is public, so it is exactly the kind of thing Stripe says is fine to pass; their public key itself is published beside it or posted from the page.
2. **The webhook** reaches one small serverless function, a Lambda: it checks Stripe's signature, fetches the session from Stripe to confirm it is paid, and records the session id once, so a retried webhook cannot issue a second key.
3. **One key from stock:** taken from a vault of pre-made keys, each used once, or minted for this sale.
4. **Sealed and signed:** the key is sealed to the buyer's public key and signed with ours, as a pki.sgit.ai message, a link and a QR code.
5. **The redirect** brings the buyer back to our page with the session id; the page shows the sealed link as a QR code, and only their private key, in their browser, can open it. An email copy can carry the same link, useless to anyone else.

Stripe never sees a key; the key never travels in clear; and the redirect really does carry the secret, because what it carries can only be opened by the person who paid. This is the same pattern we use for patient vaults and for onboarding a person to a cell ([patient vaults, answered](/articles/patient-vaults-answered.html)).

## Keys as stock {#stock}

!shot kds-stock.webp | images/ | Keys as stock: give the provider claim codes, let it count them; the buyer claims, we seal the real key. | process

I like keys as stock: make 50, sell 50, and the count is the inventory. I would love a provider to manage that stock for me, and FastSpring can. But I do not want any provider holding real vault keys.

So the answer is claim codes. Make a batch of 50 random, single-use codes, worth nothing on their own, and keep the 50 real keys in our own vault. Load the codes into a provider that sells from a list. The provider sells one code per sale, counts the stock and stops at zero. The buyer comes to our page with the code and their public key; the code is spent; we seal the real key to them. A leaked code can be claimed once and is then dead, and a real key never sat in someone else's database. The same batch can go to a reseller, an event, or an agent with a budget.

## What I would do now {#now}

- **Keep Stripe for the money** and the fraud screening; it is very good at that part.
- **Build the one function** for the key: webhook, check, stock, seal, redirect. It is small, serverless and ours.
- **Make the buyer's key pair part of checkout,** so every key we hand over is sealed from the first sale.
- **Try claim codes on a list-based provider** for anything sold through someone else.
- **Watch Stripe Workflows' custom code:** when it is generally available, part of the function could move into Stripe.

## What this does not claim {#limits}

- **Provider features change;** this is from their documentation and community reports, read on 17 November 2026, and some details come from secondary sources.
- **The design is mine and not built yet;** the pieces, the pki.sgit.ai module, vaults and lanes, exist.
- **Fees, tax and merchant-of-record questions** are a separate decision from key delivery.

## Where this comes from {#sources}

Stripe's documentation on [payment link parameters](https://docs.stripe.com/payment-links/url-parameters), [fulfilling orders](https://docs.stripe.com/checkout/custom-checkout/fulfill-orders) and [Workflows custom actions](https://docs.stripe.com/workflows/custom-actions), and its [Dahlia changelog](https://docs.stripe.com/changelog/dahlia); FastSpring on [license key fulfilment](https://developer.fastspring.com/docs/license-key-fulfillments); Paddle on [fulfilment methods](https://www.paddle.com/help/start/set-up-paddle/which-fulfillment-method-to-choose) and [transaction.completed](https://developer.paddle.com/webhooks/transactions/transaction-completed); the Lemon Squeezy and Polar license key APIs; a [Square community thread](https://community.squareup.com/t5/Archived-Discussions-Read-Only/Does-Square-have-the-ability-to-issue-a-Product-License-Key-with/m-p/661866); all read on 17 November 2026. Earlier on this site: [your own agentic cell, end to end](/articles/your-own-agentic-cell.html), [a secret is a QR code](/articles/a-secret-is-a-qr-code.html), [patient vaults, answered](/articles/patient-vaults-answered.html).
