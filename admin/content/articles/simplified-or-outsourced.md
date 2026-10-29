---
title: Simplified, or outsourced? A reply to Nadzeya Stalbouskaya on removing servers and databases: the risk is real, so map it, move only to real commodities, and ask who would certify what you now depend on
date: 2026-10-25
author: Dinis Cruz
author_url: about/index.html
summary: Under my LinkedIn comment that I run with no databases, serverless services and no server-side code of my own, Nadzeya Stalbouskaya asked a good question: removing servers and databases does not necessarily remove complexity; sometimes it just moves it into external services, APIs and dependencies we do not fully control, trading operational overhead today for dependency and lock-in tomorrow. So how do you tell genuinely simplifying an architecture from outsourcing its complexity? My answer: Nadzeya is right that there is risk, and it must be a conscious decision. The way to make it is to map it. On a Wardley map, moving a component from custom-built to commodity removes complexity only if what you move to really is a commodity. Replacing our own login with passkeys is that: a standard every major browser and platform supports, with a track record. Moving our data to object storage and static hosting is too. But moving to a young startup's service can look like a commodity on our map while, behind it, it is as messy as what we had, or worse. So you de-risk the move by choosing the commodity, and you can test which one you have by asking who would certify it, insure it, or sign a high SLA on it. Maturity and certifiability go together.
version: v0.13.80
license: https://creativecommons.org/licenses/by/4.0/
tags: architecture, wardley-maps, serverless, passkeys, risk, certification, article
status: published
---

!shot nz-thread.webp | images/ | The LinkedIn thread: my reply to Stephan Bitton and Nadzeya Stalbouskaya's challenge on simplifying or outsourcing. | small | aside

## In short {#in-short}

- **The challenge is fair.** Removing servers can move complexity into dependencies you do not control.
- **So the move must be a conscious decision.** Made on a map, not by habit.
- **Map it.** Moving a component right, to commodity, simplifies only if the destination is a real commodity.
- **Passkeys and object storage are.** Standards and utilities with a track record.
- **A young startup's service may only look like one.** Behind it, it can be messier than what you had.
- **Test it by asking who would certify it.** Maturity, insurability and certification go together.

## The question {#question}

Under Stephan Bitton's post on how founders can make the most of Google's AI capabilities to build efficient, AI-first startups, I [replied](https://www.linkedin.com/feed/update/urn:li:ugcPost:7514330476652859394/?dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287517520031300120576%2Curn%3Ali%3AugcPost%3A7514330476652859394%29&dashReplyUrn=urn%3Ali%3Afsd_comment%3A%287520169754456911873%2Curn%3Ali%3AugcPost%3A7514330476652859394%29) that my strategy has been to have no databases, run serverless services, and these days even have no server-side code that I maintain, which keeps the architecture simple and cost-effective. Nadzeya Stalbouskaya, a co-founder working in enterprise architecture and transformation, replied with a challenge I want to answer properly:

> "removing databases and server-side code doesn't necessarily remove complexity. Sometimes it just moves it into external services, APIs and dependencies that we don't fully control. From an enterprise architecture perspective, that's an interesting trade-off. We reduce operational overhead today, but potentially create dependency and vendor lock-in risks tomorrow. How do you distinguish between genuinely simplifying architecture and simply outsourcing its complexity?"

Nadzeya is right that there is risk. And I would argue that it has to be a very conscious decision. If you replace a server or a service of your own with a third-party component that is itself an explorer project, or even a villager one, then I agree: you have outsourced your complexity, and probably added some. The difference is the town planner services, the commodities. By design, they are very stable. They are effective, they have a track record, documentation and SLAs, and a level of maturity your own version will never have. Which is why you have to map it.

## Map it {#map}

!shot wm-three.webp | images/ | Three moves to the right on the map: our own login, our own database server and a feature moved to a startup. | concept

On a [Wardley map](https://newsroom.sgit.ai/articles/explorer-coding.html), each component sits somewhere on the line from genesis to custom-built, to product, to commodity. Replacing something we built with something we buy is moving its dot to the right. That only removes complexity if the thing on the right really is a commodity. Three examples.

**Login: our own, to passkeys.** A login we build means passwords, a password database, resets, multi-factor, and every vulnerability that comes with them. Passkeys move all of that to a standard. The [FIDO Alliance](https://fidoalliance.org/passkeys/) says passkeys are "supported in all major operating systems, internet browsers, and by third-party passkey providers", built on WebAuthn, the browser API for them; Google made them the default option for personal accounts in [October 2023](https://www.cnbc.com/2023/10/10/google-passkeys-now-default-login-option-for-google-accounts.html). It is a better way to create a user identity and sign in, and it is very mature. You can see that flow working on [pki.sgit.ai](https://pki.sgit.ai/), where a passkey opens the vault that holds your keys. Behind the dot is the whole industry. That is a genuine simplification.

**Data: our servers, to a utility.** A database server of our own means backups, patches, failover, upgrades and someone on call. Moving the data to object storage and static hosting, utilities run at enormous scale, removes a whole branch of that map. The dependency is real, but it is on a commodity, with alternatives that do the same thing, so the lock-in is shallow.

**A feature: our own, to a young startup's service.** Here is the irony. On our map, their service sits on the right: we call an API, and it works. But behind the scenes, their own map has its components on the left: their glue, their early code, their own suppliers. It is probably as messy as what we had, or worse, and now we cannot see it or fix it. That is exactly the outsourced complexity Nadzeya describes.

## Where our own products sit {#ours}

The same test applies to what we build. SG/Send's vault is now a product, and it is gaining traction. I would argue it is not yet a commodity. But it already removes a lot of complexity, because the encryption happens on the user's device, and the server only ever stores ciphertext. That one decision means a lot of other things are simply not needed: no plaintext to protect at rest, no user data to breach, as I wrote in [the attack surface you do not have](https://newsroom.sgit.ai/articles/the-attack-surface-you-do-not-have.html). So it sits in the middle of the map, a villager product, and an honest map says so.

## Who would certify it? {#certify}

!shot wm-certify.webp | images/ | Maturity is what can be certified, insured and held to an SLA, shown from explorer to town planner. | concept

This connects to something I have been writing about: [who signs for this?](https://newsroom.sgit.ai/articles/who-signs-for-this.html), and [signed by the source](https://newsroom.sgit.ai/articles/signed-by-the-source.html). If someone has to certify what we depend on, the question becomes: are they certifying a villager product, or a town planner one?

I think you will often find that nobody wants to certify a villager product, because by design it is still glued together, and an explorer project has not got the maturity at all. The maturity of a company and of a service is, I would argue, directly proportional to its insurability, and to anyone's ability to certify it and to sign high SLAs on its core service and its non-functional requirements: security, stability, reliability, disaster recovery, resilience, documentation.

So that is my practical answer to Nadzeya's question. Using third-party services carries risk; you de-risk it by using commodity services. And you tell a commodity from outsourced complexity by asking who would certify it, insure it, or put a high SLA on it. If the answer is nobody, you have not simplified. You have moved the mess somewhere you cannot see.

## What this does not claim {#limits}

- **Corrected on 25 October 2026.** The first version said the thread sat under a post about open source as a business model; that line was my own LinkedIn headline. The thread is under Stephan Bitton's post on AI-first startups, and is now linked.
- **The maps are illustrative.** The positions are judgements, not measurements.
- **Commodities have outages and lock-in too.** The point is that the risk is shallower, better documented and shared by everyone.
- **Not every startup is messy.** The point is that you cannot tell from your own map.
- **The certification market is an argument,** not one that exists today for most services.

## Where this comes from {#sources}

[The LinkedIn thread](https://www.linkedin.com/feed/update/urn:li:ugcPost:7514330476652859394/?dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287517520031300120576%2Curn%3Ali%3AugcPost%3A7514330476652859394%29&dashReplyUrn=urn%3Ali%3Afsd_comment%3A%287520169754456911873%2Curn%3Ali%3AugcPost%3A7514330476652859394%29), under Stephan Bitton's post, from a screenshot: my reply to him and Nadzeya Stalbouskaya's comment, quoted as written; my voice memo of the same day. The FIDO Alliance, [passkeys](https://fidoalliance.org/passkeys/), read on 25 October 2026; CNBC, [Google passkeys now default login option for Google accounts](https://www.cnbc.com/2023/10/10/google-passkeys-now-default-login-option-for-google-accounts.html), 10 October 2023; [pki.sgit.ai](https://pki.sgit.ai/). Related: [explorer coding](https://newsroom.sgit.ai/articles/explorer-coding.html), [the attack surface you do not have](https://newsroom.sgit.ai/articles/the-attack-surface-you-do-not-have.html), [the no-server startup](https://newsroom.sgit.ai/articles/the-no-server-startup.html), [ephemeral town planner services](https://newsroom.sgit.ai/articles/ephemeral-town-planner-services.html), [who signs for this?](https://newsroom.sgit.ai/articles/who-signs-for-this.html), [signed by the source](https://newsroom.sgit.ai/articles/signed-by-the-source.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
