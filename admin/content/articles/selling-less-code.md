---
title: Selling less code: the economics of customised open source, where the customer pays for the features they use, the maker certifies what it ships, and the pipeline is finally tied to revenue
date: 2026-10-30
author: Dinis Cruz
author_url: about/index.html
summary: One of our business models is to sell customised versions of open source software: a version made for one customer and relicensed to them. Some of the customisation is cosmetic, a logo or a brand. The part that matters is that we are selling a reduction in complexity. If a customer uses 10% of an application's features, why should they pay for all of them, and why should they take on all of their technical debt? Every feature is code to maintain, a screen of options to learn and a place for the next vulnerability to land. The fewer moving parts, the better the security and the engineering. Open source is what makes this possible: with the code available, we can build custom static analysis, custom environments and semantic knowledge graphs of what a customer actually uses, and the people best placed to certify the result are the ones who made it. And there is a positive loop. When the cost of customising is ours, we invest in making it cheap: software designed to be mixed and matched, and the CI pipeline, the non-functional requirements, the threat models and the certification that usually fight for budget because they are not tied to revenue. Here they are the product. It is the next phase of RiskMandate, with sgit and SHarness: a customised build is a signed, hashed release in a vault, licensed to the customer with our key, with a smaller behaviour policy and fewer rows for an insurer to price. The base stays open, maintained by many; the customer's version can be proprietary to them; and the more customisation a customer wants, the more it costs, which rewards everyone for keeping as much as possible in the open.
version: v0.14.6
license: https://creativecommons.org/licenses/by/4.0/
tags: open-source, business-model, complexity, attack-surface, riskmandate, sgit, sharness, licensing, article
status: published
---

!shot qx-less.webp | images/ | One customer's use of an application: the features they use, and the rest they would otherwise run and maintain. | concept

## In short {#in-short}

- **We sell customised versions of open source software,** made for one customer and relicensed to them.
- **The product is less complexity.** Branding is the easy part; the value is the features, the code and the debt the customer no longer carries.
- **Every feature has a cost** in maintenance, in cognitive load and in attack surface, whether it is used or not.
- **Open source makes it possible:** with the code, we can map what a customer actually uses, and the maker is the best placed to certify the result.
- **The loop:** when customising is our cost, the pipeline, the non-functional requirements and the certification are tied to revenue, so they get the investment they usually fight for.
- **The stack:** each customised build is a signed, hashed release with its own smaller behaviour policy, and fewer rows for an insurer to price.
- **The more customisation, the higher the price,** which rewards keeping as much as possible open.

## What the customer is really buying {#buying}

The model is simple to state. We take open source software, ours or someone else's, make a version for one customer, and license that version to them. Some of the customisation is cosmetic: their logo, their name, their colours. That is the part people see, and it is the least important.

What we are really selling is a reduction in complexity. If a customer needs 10% of an application's features, why should they pay for all of them? And why should they also buy all of the technical debt behind the other 90%? Every feature that exists in an application is something to maintain. It is also cognitive load: if a team uses five features out of fifty, why does the interface show fifty? And it is code that runs, which means it is somewhere a vulnerability can be found.

I have argued for running less code for years, in [the code you do not ship](/articles/the-code-you-do-not-ship.html), [the attack surface you do not have](/articles/the-attack-surface-you-do-not-have.html) and [the minimum code below](/articles/the-minimum-code-below.html), where removing what one use case never runs took a real tool from 1,500 files to 428. The question those articles left open was who pays for the removal. This is the answer: the customer does, because it is what they are buying.

## Fewer moving parts {#moving-parts}

From a security and an engineering point of view, the principle underneath is the reduction of moving parts. The best way to make sure a product does not have a vulnerability is to have less code in it. When the next critical flaw is published in a library or a feature, the question every customer asks is whether it affects them. With a customised version, the answer is more often no, because the code is not there.

!shot qx-shared.webp | images/ | One open base and three customers' versions: each runs only what it uses; the shared core stays maintained. | architecture

That is also why open source matters so much here. We are happy to own less of the stack. The base stays open and is maintained by a wide range of people; what we own is the work of fitting it to each customer, and keeping that fit current.

## Why open source makes it possible {#open}

You can only remove code safely if you know what it is for and what depends on it. With the code available, and now with agents, we can build what used to be too expensive to build for one customer: a static analysis written for this application, an environment that runs exactly the customer's use, and a semantic knowledge graph of what the customer actually uses, from the feature down to the function. That is the map [the code you do not ship](/articles/the-code-you-do-not-ship.html) said was missing.

And the people best placed to certify the result are the ones who made it. I argued in [who maintains the PHP you run](/articles/who-maintains-the-php-you-run.html) and [who signs for this](/articles/who-signs-for-this.html) that a version should be signed off by the people who maintain it, because they understand it and have invested in it. A customised version is the same, with one more line on the certificate: what was removed, and why it is safe to have removed it.

## The loop: the pipeline gets paid for {#loop}

!shot qx-loop.webp | images/ | The loop: customisation is sold, its cost falls on the maker, so the maker invests in the pipeline. | process

There is a positive loop here that I have seen work before. When we carry the cost of customising, we want that cost to be as small as possible. So we start designing the software to be easy to customise: components that can be mixed and matched, features that can be left out cleanly. And we start investing in everything that makes a customised release cheap and safe: the CI pipeline, the non-functional requirements, the tests, the threat models, the certification.

This matters because those are the things that usually lose. If the CI pipeline is not directly connected to revenue, it is always fighting for investment and for focus, because it is a cost, not a profit centre. But if the ability to customise the application, to secure it, to certify it, to threat model it and to deliver a secure version of it is what the customer is paying for, then it is the product, and it gets the investment. On this newsroom, [CI owns the version](/articles/ci-owns-the-version.html) because two agents collided on release numbers; in a business that sells customised releases, the release pipeline is the business.

The loop also gives evidence that is normally missing. Imagine finding that 90% of customers use only 30% of the stack. In most companies that is a curiosity. Here it is a direct question about revenue: why are we maintaining the rest? The design of the base starts to follow what customers actually use.

## The maker should do the customising {#maker}

It will almost always be cheaper for the maker of a piece of software to customise it than for anyone else, because the maker has the expertise. So for the stack we build, Agent Behaviour Policies and RiskMandate, the hooks, SHarness and sgit, we should be the ones selling the customised versions. And for technology we use but did not make, the same logic runs the other way: if we want it customised, we should pay the company that makes it to do it, and if they do not offer that service, we should not do it ourselves.

That is the same argument as [who maintains the PHP you run](/articles/who-maintains-the-php-you-run.html): pay the people who maintain the core, and they will invest in exactly the things that make maintenance cheaper.

## How it fits RiskMandate, sgit and SHarness {#stack}

This is the next phase of RiskMandate, and it is where our pieces fit together:

!shot qx-stack.webp | images/ | A customised release in our stack: an open base, a hashed build, a signed licence, a smaller policy. | architecture

- **The base is open.** Our own stack is open source, and the policies and hooks are open for anyone to copy, as [free to copy, paid at the source](/articles/free-to-copy-paid-at-the-source.html) describes.
- **The customised build is a release in a vault.** sgit versions it, so every customer's version has a history, a hash and a place where only the customer and we can read it.
- **The licence is signed.** The version is licensed to that customer with our key: a signature over the build's hash, so anyone can check which version is licensed to whom. At that moment it can become proprietary to the customer, because it is licensed to them, while the base it came from stays open.
- **The policy is smaller.** An Agent Behaviour Policy, or an application behaviour policy, lists what the software can reach. Remove features and the reach shrinks, and with it the policy. SHarness enforces the smaller policy on the processes the build runs.
- **The insurance is cheaper.** [A payout for every row](/articles/a-payout-for-every-row.html) prices an agent or an application row by row. Fewer capabilities, fewer rows, and more of the remaining rows enforced as Boundaries, is a smaller premium for the customer and a clearer risk for the insurer.

## Who pays for what {#price}

The price follows the work: the more customisation a customer needs, the more it costs them. That has a useful side effect. It rewards everyone, us and the customer, for keeping as much of the code open and shared as possible, because shared code is maintained by many people and costs each of them less. The customer pays for what is theirs alone, and the base gets better for everyone.

There is no proprietary software in this model on our side. Everything we make is open source. What we sell is the work of making it fit one customer, the certification that it is safe, and the licence that makes that version theirs.

## What this does not claim {#limits}

- **It is a model, not yet a business at scale.** We have documented it and use parts of it; we have not sold many customised versions yet.
- **The 10%, 90% and 30% figures are illustrations** from the memo, not measurements of any product.
- **Removing code is not free.** It needs the map and the tests first, and a customised version has to be kept current with its base, which is the cost the customer pays for.
- **Relicensing depends on the base's licence.** Permissive licences allow a proprietary version for the customer; copyleft licences constrain it, and each base has to be checked.
- **My interest:** I build the stack this article argues for, and the model is ours.

## Where this comes from {#sources}

- My voice memo of 30 October 2026, word for word in `admin/notes/2026-10-30__customised-open-source/memo-01.md` in this site's repository.
- Earlier articles here: [the code you do not ship](/articles/the-code-you-do-not-ship.html), [the attack surface you do not have](/articles/the-attack-surface-you-do-not-have.html), [the minimum code below](/articles/the-minimum-code-below.html) (the 1,500 to 428 files), [the eyeballs get cheap](/articles/the-eyeballs-get-cheap.html), [who maintains the PHP you run](/articles/who-maintains-the-php-you-run.html), [who signs for this](/articles/who-signs-for-this.html), [CI owns the version](/articles/ci-owns-the-version.html), [free to copy, paid at the source](/articles/free-to-copy-paid-at-the-source.html), [a payout for every row](/articles/a-payout-for-every-row.html).
- Written by this site's writing agent from the memo, at my request.
