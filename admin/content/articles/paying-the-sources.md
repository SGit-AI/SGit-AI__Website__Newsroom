---
title: Paying the sources: the business model behind PrompTugal.news's data, a reader's money flowing back to the sources the reader actually read, worked out in the open and simulated for now, a licence link on every value, a public register of who we read and who we do not, and why a platform built on public data with no lock-in can be a positive loop for everyone who feeds it
date: 2026-11-18
author: Dinis Cruz
author_url: about/index.html
summary: My business model for this platform is a positive feedback loop: the reader pays for what they read, and the money flows back to the sources that made it possible, in a way the reader can see. Today the PrompTugal.news team built the first version of that, as a simulation. A page shows how a reader's £5 would be shared: 30% kept for costs, the rest split among the sources behind the pages they read, weighted by how each was used, a cited fact, quoted words, a data set, a lead; 504 sources behind 112 pages, IPMA's data at the top. No money moves yet, and every page says so. Beside it, every value the sites serve now carries a link to its licence, and a public register lists 92 sources, the 18 we read and the 74 we do not, quoting why. There is no lock-in: everything is published, built on public data, with its evidence. And the gaps are the next step: some publishers do not allow their data to be shown, even data their own users gave them, and the answer is to ask them, on the record, and to make paying them part of the offer. Part three of the series.
version: v0.14.158
license: https://creativecommons.org/licenses/by/4.0/
tags: promptugal, business-model, payments, licences, sources, open-data, series, article
status: published
---

!shot gs-payments.webp | images/ | Paying the sources, simulated: how a reader's £5 would be shared among the sources behind what they read. | screenshot | medium

## In short {#in-short}

- **The model:** readers pay for what they read; the money flows back to the sources.
- **Simulated today:** a reader's £5, 30% for costs, the rest shared by how each source was used.
- **504 sources behind 112 pages,** IPMA's data at the top.
- **A licence link on every value.**
- **A public register** of 92 sources, read and not read, and why.
- **No lock-in:** everything published, from public data, with its evidence.

Part three of [gaining speed](/articles/gaining-speed.html).

## A positive loop {#loop}

I want this platform to pay the people whose work it rests on. The reader pays by the read, a few pence for the share of a page they actually read ([paid by the read](/articles/paid-by-the-read.html)); and the money flows back to the sources behind that page, in a way the reader can see. The better the sources, the better the pages; the more readers, the more the sources earn; and the more the sources earn, the more reason they have to publish openly. Everyone who feeds it gains from it, and nothing is hidden.

## The simulation {#simulation}

Today, at 15:38, the team's developer agent published the first version: [paying the sources, a simulation](https://promptugal.news/payments/simulated/). It says at the top of every page: "Simulated. No payment is made or collected; no money moves."

- **The rules, open to change:** 30% kept for costs; of a reader's £5, £3.50 shared; a minimum payout of £1 to any source.
- **The weights:** a cited fact counts 1, quoted words 1.5, a data set 1, and a lead found by discovery 0.5.
- **The sources:** 504 behind 112 pages; IPMA's public data at the top.
- **Your £5:** worked out in your own browser, from your own reading log, and sent nowhere.

The point of simulating it first is to argue about the rules in public, with the numbers, before any money moves.

## A licence on every value {#licence}

!shot gs-sources.webp | images/ | The register of sources: each with its owner, what it would give, and whether we read it, with the reason. | screenshot | medium

At about 14:25 I asked that every piece of data the sites hold carry a link to its licence. By 14:45 every data object the sites serve carried one, ours in green, CC BY 4.0, and others' in their own terms, with a check in the build that fails a page without it. A reader can see, value by value, whose it is and on what terms we show it.

And the register of sources, 92 of them today, lists the 18 we read and the 74 we do not, each with the terms or robots.txt quoted and the date it was read ([whose event is it?](/articles/whose-event-is-it.html)).

## The gaps, and asking {#gaps}

The register makes the gaps visible: event platforms, local guides, social networks that do not allow us to show their data, some of it data their own users gave them to be seen. The answer is not to take it; it is to ask, on the record, and to make paying them part of what we offer. A source that allows us to show its data, with credit and a link, would also be one that the simulated payout pays. That is a better offer than a takedown request.

## No lock-in {#open}

Everything is published: the data, its sources, its licences, the code that collects it and the rules that share the money. A reader, a partner or a rival can take all of it and build on it ([governance from zero](/articles/governance-from-zero.html)). What we sell is the service around it: the team that runs it, the integrations, the speed.

## What this does not claim {#limits}

- **No money moves yet;** the payout is a simulation, and its rules are mine to change.
- **The weights are a first proposal.**
- **Not every value carries a licence yet:** the work started today.

## Where this comes from {#sources}

[promptugal.news/payments/simulated/](https://promptugal.news/payments/simulated/) and [data.promptugal.news/sources/](https://data.promptugal.news/sources/), read on 18 November 2026; the PrompTugal.news repository's guidance on licences and submissions and the commits of 18 November. Earlier on this site: [gaining speed](/articles/gaining-speed.html), [paid by the read](/articles/paid-by-the-read.html), [whose event is it?](/articles/whose-event-is-it.html), [governance from zero](/articles/governance-from-zero.html).
