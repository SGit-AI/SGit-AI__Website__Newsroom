---
title: Monstream, briefed: continuous research streams run by AI agents, an integration API with signed webhooks, a free service from a small cryptography company, and how our newsrooms could use it, check it and contribute to it
date: 2026-10-25
author: Dinis Cruz
author_url: about/index.html
summary: A friend sent me Monstream, and I had not seen it. It is a service of continuous research streams: you describe a topic, it turns the description into rules (what must be there, what to skip, which sources to trust, how strict to be), and AI agents read sources around the clock and send you only what matches, with short summaries and links to the originals. Its home page said 5,258 pages had been read by its agents that day. It is run by Fair Math, a small fully homomorphic encryption company, which reportedly raised $1.4 million in early 2024; most of its 116 public streams follow cryptography, and the largest has 24 subscribers. There is no public pricing: following a stream "costs nothing extra", and the Mac app is free. What makes it interesting for us is a clean integration API: a stream per object in our own system, named by our own id, finds pushed by a signed webhook or pulled by cursor, and feedback on each find. Legally, its terms allow automated access only through the means it provides, so the API is the way in, and its summaries are written by AI and "can be incomplete or wrong", so a find is a lead, never evidence. There is no public stream on php2shell; creating one needs an account, which I have not made. This is how I would use it, check it and contribute to it.
version: v0.13.77
license: https://creativecommons.org/licenses/by/4.0/
tags: research, monitoring, agents, apis, integrations, briefing, article
status: published
---

!shot mn-pages.webp | images/ | Monstream on 25 October 2026: the home page, where AI agents read sources against your rules and send what matters with short summaries and original sources; Discover, with 116 public streams, the largest with 24 subscribers; and the Integration API, with streams named by your own id, finds and webhooks. | screenshot

## In short {#in-short}

- **What it is.** Continuous research streams: AI agents read sources against your rules and send what matches.
- **Who runs it.** Fair Math, a small cryptography company, reportedly funded with $1.4 million in 2024.
- **How big.** 116 public streams, mostly cryptography; the largest has 24 subscribers.
- **What it costs.** No public pricing; following is free, and so is the Mac app.
- **The API is the interesting part.** A stream per object in your system, signed webhooks, feedback.
- **Legally,** the API is the only automated way in, and its summaries are leads, not evidence.
- **On php2shell,** no public stream exists; making one needs an account.
- **How we could use it, check it and contribute to it.** Below.

## What it is {#what}

[Monstream](https://monstream.io/) describes itself as "continuous research streams for the topics that matter to you". You describe what you want to follow, in as much detail as you like. It turns that into rules: what must be included, any of a set of topics, red flags to skip, sources to trust or ignore, and how strict to be. You can preview a stream on the previous week's data before starting it. Then "AI agents read thousands of pages around the clock, check every finding against your rules and send you only what matters, with short summaries and original sources." When I looked, the home page said its agents had read 5,258 pages that day.

A stream can be a digest, a radar or a watch. Its use cases run from competitors (their pricing pages, changelogs and job posts) to regulation, research, investors, founders, jobs, immigration and health. Results arrive in the web app, by email, by push, through a free Mac app, or on Telegram. Streams can be private, or public in Discover, where anyone can follow them or fork them into their own.

The tools are handled for you: it says each stream picks from more than 1,000 sources, connectors and readers, with the keys and rate limits managed on its side; it names Crunchbase, X, Semantic Scholar, Exa, OpenRouter and PitchBook among them.

## Who runs it, and how it is funded {#who}

The site is operated by Fair Math, whose own site describes it as building "cryptographic infrastructure for computing on encrypted data", fully homomorphic encryption. Fair Math also runs FHERMA, a challenge platform for that field, and its founder and chief executive is reported as Gurgen Arakelov, whose name is on several of Monstream's public streams.

FinSMEs and Crunchbase report that Fair Math raised $1.4 million in pre-seed funding in February 2024, led by gumi Cryptos Capital, Inception Capital and Polymorphic Capital; PitchBook and Tracxn list the round as seed, and PitchBook lists two more investors. I could not read those pages directly, and I found no separate funding for Monstream. It looks like a product built by a small cryptography company, perhaps first for its own research: the API's own example is a stream for FHERMA.

That shows in Discover. Of its 116 public streams, the most followed are the FHE Radar (24 subscribers), AI vs Cryptography (17), and radars on trusted execution, zero-knowledge proofs, post-quantum cryptography and multi-party computation (10 to 13 each). It is early, and small.

## What it costs {#cost}

There is no pricing page. Discover says "Subscribing costs nothing extra", and the Mac app is free. The terms reserve the right to change or limit features, "including how many streams an account can run". Underneath, every stream costs real money: model calls through OpenRouter, searches through Exa, and data sources such as PitchBook and Crunchbase. So I would expect a paid tier, but there is no public commercial model yet.

## The integration API {#api}

This is the part that makes it interesting for us. Monstream publishes an [Integration API](https://monstream.io/developers), last updated on 20 October 2026, so that "another system can keep streams on Monstream for its own objects, such as a research topic, a kernel or a client, and receive what they find."

- **Access.** A Monstream account for the system, and an API key with scopes (`streams:read`, `streams:write`, `finds:read`, `webhooks:write`, `feedback:write`), sent as a bearer token. The key is shown once and only its hash is kept. Without one, the API answers 401, which I checked.
- **A stream per object, by your own id.** `PUT /streams/by-ref/<system>/<ref>` creates or updates a stream named by your system and your id, and the call is idempotent. You either describe the stream in words, and Monstream drafts the rules, or send the rules yourself; you can give it sources, and whether to use only those.
- **Following existing streams.** Search with `GET /streams?q=…`, then bind one to your own id.
- **Webhooks.** Events for a find created, updated or removed, and for a stream updated or deleted. Every delivery is signed: an HMAC-SHA256 over the timestamp and the raw body (its example code rejects anything more than five minutes old), and a stable event id to deduplicate on. Your own secret header is stored encrypted and sent with every call. Failed deliveries are retried for about a day.
- **Pull.** `GET /finds?after=<cursor>` pages through finds, for a system that would rather poll.
- **Feedback.** `POST /finds/<id>/feedback`, relevant or not relevant, tells the stream what fits.

It is a clean, careful design: idempotent, signed, scoped, and built around the caller's own ids.

## Legally: can we use it? {#legal}

Yes, through the API, and with care about what the results are.

- **Automated access only through what they provide.** The [terms](https://monstream.io/terms) forbid accessing the service "by automated means other than the ones we provide". The Integration API is one of those means. Scraping the site is not.
- **The results are other people's material.** "Results come from third-party websites, feeds and APIs. We do not own or control that material, and links take you to sites with their own terms." So a find points us to a source; whether we may capture, quote or republish that source is decided by the source's own licence and access, which is exactly what [sources and their shadows](https://newsroom.sgit.ai/articles/sources-and-shadows.html) says we must record.
- **The summaries are AI-written.** "Summaries and judgements are written by AI models and can be incomplete or wrong. Check the original source before relying on anything." For a newsroom, that makes every find a lead. Evidence is what we capture ourselves.
- **What we send goes to AI providers.** The [privacy policy](https://monstream.io/privacy) says a stream's rules, and a description written in your own words, go to OpenRouter and the model providers it routes to, and search queries to Exa. Nothing confidential belongs in a stream's description.
- **Public streams can be forked.** Making a stream public lets others follow it and fork it into their own.
- **One inconsistency.** The privacy policy says "we do not use third-party analytics or tracking", and further down that "We use Google Analytics"; the site does load Google's tag. A small thing, but worth a correction on their side.

The terms do not name a governing law, and neither the terms nor the API page mention a rate limit or a commercial-use restriction for the API.

## php2shell, on Monstream {#php}

You asked what it currently has on the PHP incident. In Discover, nothing: none of the public streams I could list, in any category, covers php2shell or vulnerability news in general; the nearest are "Crypto Implementation Vulnerabilities" and "GitHub Trending · Security & Privacy". Public stream pages also showed "Something went wrong" to a visitor who was not signed in, both times I tried. To create a stream on php2shell, and see what it finds, needs an account and an API key. Opening an account on someone else's service is a step I leave to you; with a key, it is one call.

## How we could use it {#use}

!shot mn-flow.webp | images/ | How Monstream could feed our newsrooms, through its documented API: a stream per story we follow, named by our own id; finds pushed to us by a signed webhook, or pulled; each find captured by our researcher into the source watch as a lead, not evidence; checked by the curator and the journalist; and our verdicts sent back as feedback on each find. Proposed, not built. | process

Our job is to integrate, leverage and connect as much as we can, and Monstream fits that well:

- **A stream per story.** For the PHP site, a stream named `newsroom/php2shell`, described in words, with our watched sources as hints. For this newsroom's wires, one per wire: AWS, OWASP, Portugal.
- **Finds as leads into the pipeline.** A signed webhook delivers each find to our researcher, which captures the original page into the source watch with its hash, as it does for every other source. The curator and the journalist decide what holds. Monstream widens what we see; our captures decide what we say.
- **Feedback as a byproduct.** Our verdicts, relevant or not, go back to the stream. Our checking improves the stream for us, at no extra cost.

## How we could contribute {#contribute}

- **Public streams of our own.** A public php2shell stream, and a "vulnerabilities in the news" stream modelled on the PHP site's [Pulse](https://php.oct.2026.newsroom.sgit.ai/pulse/index.html), which sets evidence of exploitation beside attention, would fill a gap in Discover and be useful to others.
- **The checking layer.** A find with a link to our capture, its hash, its licence and its access, and the verdict on the claim, is a find others can trust more. If the API ever takes structured feedback, that is what we would send.
- **Payments, eventually.** When Monstream has a commercial model, and so do we, the streams and the sources that led us to a story should get a share, as I argued in [local trust, certified upwards](https://newsroom.sgit.ai/articles/local-trust-certified-upwards.html).
- **A conversation.** It is a small team with a careful API and an encryption background; there is a natural overlap with our vaults. I have not contacted them.

## What this does not claim {#limits}

- **No account was made,** so nothing here was tested beyond the public pages and an unauthenticated call.
- **The funding is as reported** by FinSMEs, Crunchbase, PitchBook and Tracxn, which I could not read directly.
- **The pages-read counter, the stream counts and subscriber numbers** are from 25 October 2026 and will change.
- **Stream pages failing for anonymous visitors** is what I saw twice, not a finding about why.
- **The integration is a proposal.**

## Where this comes from {#sources}

A friend's link, and my voice memo of 25 October 2026. Monstream's [home page](https://monstream.io/), [Discover](https://monstream.io/discover), [Integration API](https://monstream.io/developers) (last updated 20 October 2026), [terms](https://monstream.io/terms) and [privacy policy](https://monstream.io/privacy) (both 6 October 2026), and its robots.txt, read on 25 October 2026, with an unauthenticated call to its API; Fair Math's [site](https://fairmath.xyz/); funding as reported by [FinSMEs](https://www.finsmes.com/2024/02/fair-math-raises-1-4m-in-pre-seed-funding.html), [Crunchbase](https://www.crunchbase.com/organization/fair-math), [PitchBook](https://pitchbook.com/profiles/company/589346-56) and [Tracxn](https://tracxn.com/d/companies/fair-math/__cv8GN2qz9NR3uhEKSvYHCuY4jiKIPBG8519HWMOC3go), through a web search. Related: [sources and their shadows](https://newsroom.sgit.ai/articles/sources-and-shadows.html), [local trust, certified upwards](https://newsroom.sgit.ai/articles/local-trust-certified-upwards.html), [own the stack, and the trust](https://newsroom.sgit.ai/articles/own-the-stack-and-the-trust.html), [the side stories of php2shell](https://newsroom.sgit.ai/articles/the-side-stories-of-php2shell.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
