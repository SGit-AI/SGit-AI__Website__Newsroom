# Selling less code: the economics of customised open source, where the customer pays for the features they use, the maker certifies what it ships, and the pipeline is finally tied to revenue, sgit.ai

> One of our business models is to sell customised versions of open source software: a version made for one customer and relicensed to them. Some of the customisation is cosmetic, a logo or a brand. The part that matters is that we are selling a reduction in complexity. If a customer uses 10% of an application's features, why should they pay for all of them, and why should they take on all of their technical debt? Every feature is code to maintain, a screen of options to learn and a place for the next vulnerability to land. The fewer moving parts, the better the security and the engineering. Open source is what makes this possible: with the code available, we can build custom static analysis, custom environments and semantic knowledge graphs of what a customer actually uses, and the people best placed to certify the result are the ones who made it. And there is a positive loop. When the cost of customising is ours, we invest in making it cheap: software designed to be mixed and matched, and the CI pipeline, the non-functional requirements, the threat models and the certification that usually fight for budget because they are not tied to revenue. Here they are the product. It is the next phase of RiskMandate, with sgit and SHarness: a customised build is a signed, hashed release in a vault, licensed to the customer with our key, with a smaller behaviour policy and fewer rows for an insurer to price. The base stays open, maintained by many; the customer's version can be proprietary to them; and the more customisation a customer wants, the more it costs, which rewards everyone for keeping as much as possible in the open.

*Source: <https://newsroom.sgit.ai/articles/selling-less-code.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Selling less code: the economics of customised open source, where the customer pays for the features they use, the maker certifies what it ships, and the pipeline is finally tied to revenue

# Selling less code: the economics of customised open source, where the customer pays for the features they use, the maker certifies what it ships, and the pipeline is finally tied to revenue

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-30 · [article v1.0.0](versions/selling-less-code.md) · [newsroom v0.14.6](https://newsroom.sgit.ai/admin/versions.html) · open-sourcebusiness-modelcomplexityattack-surfaceriskmandatesgitsharnesslicensingarticle

***Abstract:** One of our business models is to sell customised versions of open source software: a version made for one customer and relicensed to them. Some of the customisation is cosmetic, a logo or a brand. The part that matters is that we are selling a reduction in complexity. If a customer uses 10% of an application's features, why should they pay for all of them, and why should they take on all of their technical debt? Every feature is code to maintain, a screen of options to learn and a place for the next vulnerability to land. The fewer moving parts, the better the security and the engineering. Open source is what makes this possible: with the code available, we can build custom static analysis, custom environments and semantic knowledge graphs of what a customer actually uses, and the people best placed to certify the result are the ones who made it. And there is a positive loop. When the cost of customising is ours, we invest in making it cheap: software designed to be mixed and matched, and the CI pipeline, the non-functional requirements, the threat models and the certification that usually fight for budget because they are not tied to revenue. Here they are the product. It is the next phase of RiskMandate, with sgit and SHarness: a customised build is a signed, hashed release in a vault, licensed to the customer with our key, with a smaller behaviour policy and fewer rows for an insurer to price. The base stays open, maintained by many; the customer's version can be proprietary to them; and the more customisation a customer wants, the more it costs, which rewards everyone for keeping as much as possible in the open.*

One customer's use of an application: the features they use, and the rest they would otherwise run and maintain.

## In short

- **We sell customised versions of open source software,** made for one customer and relicensed to them.
- **The product is less complexity.** Branding is the easy part; the value is the features, the code and the debt the customer no longer carries.
- **Every feature has a cost** in maintenance, in cognitive load and in attack surface, whether it is used or not.
- **Open source makes it possible:** with the code, we can map what a customer actually uses, and the maker is the best placed to certify the result.
- **The loop:** when customising is our cost, the pipeline, the non-functional requirements and the certification are tied to revenue, so they get the investment they usually fight for.
- **The stack:** each customised build is a signed, hashed release with its own smaller behaviour policy, and fewer rows for an insurer to price.
- **The more customisation, the higher the price,** which rewards keeping as much as possible open.

## What the customer is really buying

The model is simple to state. We take open source software, ours or someone else's, make a version for one customer, and license that version to them. Some of the customisation is cosmetic: their logo, their name, their colours. That is the part people see, and it is the least important.

What we are really selling is a reduction in complexity. If a customer needs 10% of an application's features, why should they pay for all of them? And why should they also buy all of the technical debt behind the other 90%? Every feature that exists in an application is something to maintain. It is also cognitive load: if a team uses five features out of fifty, why does the interface show fifty? And it is code that runs, which means it is somewhere a vulnerability can be found.

I have argued for running less code for years, in [the code you do not ship](the-code-you-do-not-ship.md), [the attack surface you do not have](the-attack-surface-you-do-not-have.md) and [the minimum code below](the-minimum-code-below.md), where removing what one use case never runs took a real tool from 1,500 files to 428. The question those articles left open was who pays for the removal. This is the answer: the customer does, because it is what they are buying.

## Fewer moving parts

From a security and an engineering point of view, the principle underneath is the reduction of moving parts. The best way to make sure a product does not have a vulnerability is to have less code in it. When the next critical flaw is published in a library or a feature, the question every customer asks is whether it affects them. With a customised version, the answer is more often no, because the code is not there.

One open base and three customers' versions: each runs only what it uses; the shared core stays maintained.

That is also why open source matters so much here. We are happy to own less of the stack. The base stays open and is maintained by a wide range of people; what we own is the work of fitting it to each customer, and keeping that fit current.

## Why open source makes it possible

You can only remove code safely if you know what it is for and what depends on it. With the code available, and now with agents, we can build what used to be too expensive to build for one customer: a static analysis written for this application, an environment that runs exactly the customer's use, and a semantic knowledge graph of what the customer actually uses, from the feature down to the function. That is the map [the code you do not ship](the-code-you-do-not-ship.md) said was missing.

And the people best placed to certify the result are the ones who made it. I argued in [who maintains the PHP you run](who-maintains-the-php-you-run.md) and [who signs for this](who-signs-for-this.md) that a version should be signed off by the people who maintain it, because they understand it and have invested in it. A customised version is the same, with one more line on the certificate: what was removed, and why it is safe to have removed it.

## The loop: the pipeline gets paid for

The loop: customisation is sold, its cost falls on the maker, so the maker invests in the pipeline.

There is a positive loop here that I have seen work before. When we carry the cost of customising, we want that cost to be as small as possible. So we start designing the software to be easy to customise: components that can be mixed and matched, features that can be left out cleanly. And we start investing in everything that makes a customised release cheap and safe: the CI pipeline, the non-functional requirements, the tests, the threat models, the certification.

This matters because those are the things that usually lose. If the CI pipeline is not directly connected to revenue, it is always fighting for investment and for focus, because it is a cost, not a profit centre. But if the ability to customise the application, to secure it, to certify it, to threat model it and to deliver a secure version of it is what the customer is paying for, then it is the product, and it gets the investment. On this newsroom, [CI owns the version](ci-owns-the-version.md) because two agents collided on release numbers; in a business that sells customised releases, the release pipeline is the business.

The loop also gives evidence that is normally missing. Imagine finding that 90% of customers use only 30% of the stack. In most companies that is a curiosity. Here it is a direct question about revenue: why are we maintaining the rest? The design of the base starts to follow what customers actually use.

## The maker should do the customising

It will almost always be cheaper for the maker of a piece of software to customise it than for anyone else, because the maker has the expertise. So for the stack we build, Agent Behaviour Policies and RiskMandate, the hooks, SHarness and sgit, we should be the ones selling the customised versions. And for technology we use but did not make, the same logic runs the other way: if we want it customised, we should pay the company that makes it to do it, and if they do not offer that service, we should not do it ourselves.

That is the same argument as [who maintains the PHP you run](who-maintains-the-php-you-run.md): pay the people who maintain the core, and they will invest in exactly the things that make maintenance cheaper.

## How it fits RiskMandate, sgit and SHarness

This is the next phase of RiskMandate, and it is where our pieces fit together:

A customised release in our stack: an open base, a hashed build, a signed licence, a smaller policy.

- **The base is open.** Our own stack is open source, and the policies and hooks are open for anyone to copy, as [free to copy, paid at the source](free-to-copy-paid-at-the-source.md) describes.
- **The customised build is a release in a vault.** sgit versions it, so every customer's version has a history, a hash and a place where only the customer and we can read it.
- **The licence is signed.** The version is licensed to that customer with our key: a signature over the build's hash, so anyone can check which version is licensed to whom. At that moment it can become proprietary to the customer, because it is licensed to them, while the base it came from stays open.
- **The policy is smaller.** An Agent Behaviour Policy, or an application behaviour policy, lists what the software can reach. Remove features and the reach shrinks, and with it the policy. SHarness enforces the smaller policy on the processes the build runs.
- **The insurance is cheaper.** [A payout for every row](a-payout-for-every-row.md) prices an agent or an application row by row. Fewer capabilities, fewer rows, and more of the remaining rows enforced as Boundaries, is a smaller premium for the customer and a clearer risk for the insurer.

## Who pays for what

The price follows the work: the more customisation a customer needs, the more it costs them. That has a useful side effect. It rewards everyone, us and the customer, for keeping as much of the code open and shared as possible, because shared code is maintained by many people and costs each of them less. The customer pays for what is theirs alone, and the base gets better for everyone.

There is no proprietary software in this model on our side. Everything we make is open source. What we sell is the work of making it fit one customer, the certification that it is safe, and the licence that makes that version theirs.

## What this does not claim

- **It is a model, not yet a business at scale.** We have documented it and use parts of it; we have not sold many customised versions yet.
- **The 10%, 90% and 30% figures are illustrations** from the memo, not measurements of any product.
- **Removing code is not free.** It needs the map and the tests first, and a customised version has to be kept current with its base, which is the cost the customer pays for.
- **Relicensing depends on the base's licence.** Permissive licences allow a proprietary version for the customer; copyleft licences constrain it, and each base has to be checked.
- **My interest:** I build the stack this article argues for, and the model is ours.

## Where this comes from

- My voice memo of 30 October 2026, word for word in `admin/notes/2026-10-30__customised-open-source/memo-01.md` in this site's repository.
- Earlier articles here: [the code you do not ship](the-code-you-do-not-ship.md), [the attack surface you do not have](the-attack-surface-you-do-not-have.md), [the minimum code below](the-minimum-code-below.md) (the 1,500 to 428 files), [the eyeballs get cheap](the-eyeballs-get-cheap.md), [who maintains the PHP you run](who-maintains-the-php-you-run.md), [who signs for this](who-signs-for-this.md), [CI owns the version](ci-owns-the-version.md), [free to copy, paid at the source](free-to-copy-paid-at-the-source.md), [a payout for every row](a-payout-for-every-row.md).
- Written by this site's writing agent from the memo, at my request.

## Threads

Startups & strategyAgents & policy[This article as a graph →](graphs.md#selling-less-code)

### Builds on

- [The code you do not ship: why the future of software is removing functionality, and who gets paid to keep it small](the-code-you-do-not-ship.md) Code is a liability, the worst bugs sit in features nobody needed, and models make removing it safe. The minimal viable code path, and who maintains it.
- [The attack surface you do not have: every CVE now makes me smile, because moving to the client side took my servers out of the news, and the constraint turned out to be speed](the-attack-surface-you-do-not-have.md) Every CVE makes me smile: moving to the client side took my servers out of the news, and the constraint turned out to be speed.
- [The minimum code below: container security from the top down, from the user story to the immutable line, measured on one real tool](the-minimum-code-below.md) Container security from the top down: at every layer, keep only the code the layer above needs. Measured on one real tool, with its limits.
- [Who maintains the PHP you run? A version signed off by the people who maintain it, buyers who require that signature, and money that flows down the chain: a follow-up to the maintenance deficit](who-maintains-the-php-you-run.md) Versions signed off by their maintainers, buyers who require it, and money that flows down the chain, scaled by Gen AI.
- [Who signs for this? Accountability maps from the hardware to the business, what is measured and what is declared, and why the parts nobody signs are the blind spots worth paying to see](who-signs-for-this.md) Map every layer from the hardware to the business contract by who signs it; the lines nobody signs are the blind spots worth paying to see.
- [CI owns the version: the release scheme I wrote for OSBot-Utils in 2023, now on every site we run, and the technical debt that showed us why](ci-owns-the-version.md) The pipeline, not whoever pushes, picks the release number: a 2023 scheme now on every site we run.
- [Free to copy, paid at the source: why an official website can charge per use for open policies and hooks, and why we will have them reviewed, audited and signed](free-to-copy-paid-at-the-source.md) Open policies and hooks, free to copy, can still earn per use at the official source, if others review them and we sign them.
- [A payout for every row: underwriting an agent behaviour policy, where each risk it names has its own limit, each enforced control lowers the premium, and what it does not name is not covered](a-payout-for-every-row.md) Underwriting an agent behaviour policy row by row: a limit per named risk, a lower premium per enforced control, and no cover for what is not named.
- [The eyeballs get cheap: why open source is about to become the most secure software we have, and why secure, sovereign and paid-for meet at the least code in production](the-eyeballs-get-cheap.md) Cheap, deep AI security review gives open source the eyeballs it never had; with sovereignty and paid maintenance, all point at the least code in production.

### Continued by

- [Lovable with SHarness, and the trojanised Claude Code extension: how to keep an app builder's code and an editor's extensions inside a policy, and what SHarness can and cannot stop today](lovable-with-sharness.md) Lovable with SHarness, and the trojanised Claude Code extension: where a policy boundary has to sit, and what SHarness can stop today.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 331 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=331)

**Posting this article on LinkedIn?** The cover is [selling-less-code.jpg](banners/selling-less-code.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/selling-less-code.html)*
