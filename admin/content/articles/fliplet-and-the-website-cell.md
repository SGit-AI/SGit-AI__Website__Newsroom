---
title: Rent or own: Fliplet, an AI software builder advertised on the London Underground, against the AgentiCCells website cell, both building from a plain-language description and changing by talking to an AI, one a monthly platform paid in credits, the other a one-off build handed over into the customer's own repository, and why we should promise to move every site into its owner's hands within three months
date: 2026-11-18
author: Dinis Cruz
author_url: about/index.html
summary: One of our team saw an advert for Fliplet on the Tube today, and it is a good example of the kind of service that will appear more and more. Fliplet, a company from Croydon, builds web and mobile software from a plain-language prompt: you describe the workflow, the audience and the data, it generates a first draft, and you change it by describing the change to the AI. It is serious: it says 34,000 organisations have used it, names law firms and EY as customers, and offers reviews before launch, role-based access and a choice of data centre. And it is a platform you rent. Its plans run from free to $25, $50, $100 and $200 a month, with credits that pay for the AI, the publishing, the hosting, the traffic and the data activity; You can use your own domain on the paid plans; but its standard terms say the service and what you build in it are Fliplet's, that it offers no way to transfer or copy your applications to another provider, that you may not take the code, and that when the terms end you must stop using it, with no right to a copy. The AgentiCCells website cell does the same core thing, a description in and a professional result out, changed afterwards by talking to Claude, and inverts the business: one payment, the site in the customer's own repository, static files they can host anywhere, and no subscription from us. I would go further, and put it in our terms: every site we build moves into its owner's ownership within three months, at the latest.
version: v0.14.164
license: https://creativecommons.org/licenses/by/4.0/
tags: agenticcells, fliplet, websites, ownership, lock-in, pricing, comparison, article
status: published
---

!shot flp-compare.webp | images/ | Rent or own: Fliplet and the website cell side by side, how each is built, paid for, hosted, changed and owned. | comparison

## In short {#in-short}

- **Fliplet builds software from a prompt,** and changes it when you describe the change.
- **It is serious,** with large customers and governance features.
- **It is rented:** free to $200 a month, paid in credits for AI, hosting and traffic.
- **Its terms say the application is Fliplet's:** no transfer, no code, no copy when you leave.
- **The website cell does the core thing** and inverts the business: pay once, own it.
- **Our promise should be written down:** the site moves to its owner within three months.

## A sign of what is coming {#sign}

Fliplet's advert on the London Underground is a sign of the market. Building software from a description is becoming a product anyone can buy, and there will be many more like it. That is good: it means the idea we have been building on, that a person describes what they want and agents make it, is going mainstream. The question that will separate these services is not whether the AI is good. It is who owns what it makes.

## What Fliplet is {#fliplet}

[Fliplet](https://fliplet.com/) calls itself "an AI-powered platform for web and mobile software without sacrificing control, security, or reliability". You describe a workflow, an audience and the data it needs, and it generates a first draft, which your team reviews, edits and publishes; later changes are made by describing them to the AI. Its examples are event apps, compliance training portals, offline checklists for field service, and intranets. It reviews software, screens and data access before launch, offers role-based access, and hosts accounts in Dublin by default or in California. It says 34,000 organisations and 326,000 software users in the past year, and names customers including EY, Clifford Chance and Eversheds Sutherland. The company is in Croydon.

## How it is paid for {#rent}

[Its pricing](https://fliplet.com/pricing/) is a subscription paid in credits, which cover "AI usage, publishing, hosting, traffic, authentication events, and data activity":

- **Free:** 500 credits, no publishing, no custom domain.
- **Plus, $25 a month:** 2,500 credits, publishing to the web and to iOS and Android, custom domains, audit logs, but no integrations.
- **Max, $50, $100 or $200 a month:** 6,000 to 32,000 credits.
- **Enterprise:** custom prices, with single sign-on, environments and custom integrations.

Its own domain is possible: custom domains come with the paid plans, from Plus at $25 a month; the free plan has none.

## Who owns it {#ownership}

Its pages do not say who owns what you build. [Its terms of service](https://fliplet.com/terms/) do, and this is the heart of the comparison:

- **The platform, and what you build in it, are Fliplet's:** "Fliplet and/or its licensor(s) are the sole owners of the Service" (9.2), which the terms say includes the structure, coding and functional changes users make when building an application. Your content is excluded; nothing says you own the application.
- **You get a licence, not ownership:** "a worldwide, royalty-free, non-exclusive, terminable and limited licence" to use its tools (9.1).
- **No moving out:** "Fliplet does not offer a facility for You to transfer or copy any Content or Applications" to another provider (8.2).
- **No code:** you may not export or copy the service or any part of it without Fliplet's written consent, nor "attempt to derive the source code" (9.3, 6.4.1). I found no GitHub repository, export or integration of any kind.
- **On termination:** Fliplet may end the terms at its discretion by written notice (15.1); you must "immediately cease use of the Services", with no right to a copy of any application (15.2).

An organisation with a negotiated contract may have different terms. But on the standard ones, your content is yours and the application is not: you can use your own domain, and you cannot take the application with you.

## The same core, the other business {#cell}

!shot flp-own.webp | images/ | What the owner holds at the end: an account on a platform, or the repository and the right to leave. | concept

The website cell does the same core thing: a person describes what they want, with their photos, videos and words, a team of agents makes five designs, and afterwards the owner changes the site by talking to Claude ([the website cell](/articles/the-website-cell.html)). The difference is everything around it:

- **Paid once,** £500, at a launch price of £250, not a monthly credit meter.
- **Owned:** the site lives in the customer's own GitHub repository, with its history.
- **Portable:** static files, hosted anywhere; GitHub Pages hosts them free ([static against the platforms](/articles/static-against-the-platforms.html)).
- **No subscription from us,** and no platform between the owner and their site.
- **Open:** the code, the policies and the factory are open source; anyone can do it themselves ([governance from zero](/articles/governance-from-zero.html)).

Fliplet does things the website cell does not: native mobile apps, authentication, enterprise single sign-on, a managed platform for large organisations. For those buyers, a platform may well be right. For a person or a small business who wants a site that is theirs, the cell is the better shape.

## Put ownership in the terms {#terms}

We say the customer owns the site. I want to make it a promise in our terms, not a claim on a page: every site we build is moved into its owner's ownership, the repository transferred to their GitHub account and the address pointed where they choose, within three months at the latest, and sooner if they ask. Until then we hold it only so we can finish the work; after that we hold nothing. No platform, no lock-in, no question about what happens if they stop paying, because there is nothing to stop paying for.

## What this does not claim {#limits}

- **Fliplet is described from its own website and standard terms,** read on 18 November 2026; a negotiated enterprise contract may differ.
- **The two are not the same product:** Fliplet builds apps for organisations; the website cell builds sites people own.
- **The three-month promise is a soft requirement** for now, agreed today and passed to the AgentiCCells team; it may be enforced later.

## Where this comes from {#sources}

[fliplet.com](https://fliplet.com/) and [its pricing](https://fliplet.com/pricing/), read on 18 November 2026; agenticcells.ai's website cell, as in [the website cell](/articles/the-website-cell.html). Earlier on this site: [static against the platforms](/articles/static-against-the-platforms.html), [governance from zero](/articles/governance-from-zero.html), [the pitch](/articles/the-pitch.html).
