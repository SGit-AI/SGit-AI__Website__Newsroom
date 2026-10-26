---
title: Inside Kitewing Websites: a made-up studio that sells websites you own, and three made-up client sites built as vault apps, a potter's catalogue, a community garden and a local plumber's guides library, each one file, each different, and each ready to be changed by talking to it
date: 2026-10-26
author: Dinis Cruz
author_url: about/index.html
summary: To make the model in websites you own concrete, the agents built a mock-up of it. Kitewing Websites is a made-up studio that sells exactly that offer: setup of three accounts the client owns, a build from the client's own material with designs to choose from, QA, a handover, and nothing monthly. Next to it are three made-up client sites in a made-up town called Harrowby, chosen because they are the kinds of site that sound complicated and are easy for an agent to maintain: Tidewrack Studio Pottery, a catalogue of 28 pieces with filters; Fennick Lane Community Garden, with a season of events, a volunteer rota and 14 growing guides; and Quillon Heat & Plumbing, a local trade with a map of the villages it covers and 19 household guides. Each is one HTML file with its words and data in a JSON file beside it, no external requests, no fonts or images to fetch, and each looks different. They are built as vault apps, so each can live in an encrypted sgit vault, and the studio's vault holds the three examples inside it: a vault in a vault. The four vaults are made and committed; pushing them to the vault server is the step that needs the editor's token. Meanwhile, the four sites are served here, as previews.
version: v0.13.92
license: https://creativecommons.org/licenses/by/4.0/
tags: websites, vaults, sgit, demos, business-models, article
status: published
---

!shot kw-sites.webp | images/ | Kitewing Websites and its three example clients, all made up: the studio's own site, "a website you own, and can talk to"; Tidewrack Studio Pottery, a catalogue in clay and sea-grey; Fennick Lane Community Garden, in leaf green and sunflower yellow; and Quillon Heat & Plumbing, in navy and safety orange. | collage

## In short {#in-short}

- **A made-up studio, selling the model in [websites you own](https://newsroom.sgit.ai/articles/websites-you-own.html).** One-off work, no monthly fee.
- **Three made-up client sites,** in three industries, each with a different design.
- **Each is one file,** with its words and data in a JSON file beside it.
- **Built as vault apps,** so each can live in an encrypted sgit vault.
- **A vault in a vault:** the studio's vault holds the three examples.
- **Served here as previews,** until the vaults are pushed.

## Kitewing Websites {#studio}

!shot kw-studio.webp | images/ | The studio's own site: the offer in five steps, setup, build, choose a design, QA and handover; one-off packages as hypotheses, a simple site £500, a larger site £1,000, a lift and shift £200 to £1,000; a domain for a year and blocks of hours as extras; and why there is no monthly fee. | screenshot

[Kitewing Websites](https://newsroom.sgit.ai/demos/vaults/kitewing-websites/vault-app/index.html) is the studio, and its site is the offer: "A website you own, and can talk to." It explains the five steps, what you pay, what you own, why there is no monthly fee, the lift and shift, and the examples, with a frequently asked questions section that answers the obvious ones: is there a page limit (no), what if the AI gets it wrong (GitHub keeps every version, so you can undo), what if I want help (buy a block of hours), and can I leave (there is nothing to leave: it is all yours). The prices are labelled as hypotheses, for a demonstration.

## Three made-up clients {#clients}

The examples were chosen because they are the kinds of site that sound complicated and are easy for an agent to maintain: a lot of products, a lot of community things, a lot of guidance. All three live in the made-up town of Harrowby.

!shot kw-tidewrack.webp | images/ | Tidewrack Studio Pottery, a ceramicist's catalogue: 28 pieces drawn in their glazes, filtered by kind and glaze, each with a reference, size and a price or "price on enquiry", and an enquiry note instead of a checkout; plus the maker, the glazes, classes, open studio days and a care guide. | screenshot

- **[Tidewrack Studio Pottery](https://newsroom.sgit.ai/demos/vaults/kitewing-websites/vault-app/examples/tidewrack-pottery/index.html)** is a catalogue: 28 pieces, mugs, bowls, vases and plates, each drawn in its glaze, filtered by kind and glaze, with a price or "price on enquiry". There is no checkout, on purpose: you enquire in the studio. That keeps the site static, which is what a brochure or catalogue on GitHub Pages should be.

!shot kw-fennick.webp | images/ | Fennick Lane Community Garden: what the garden grows, the plots and the waiting list, a season of 15 events filtered by month and type, a volunteer rota, news, and 14 growing guides that open in a reader view. | screenshot

- **[Fennick Lane Community Garden](https://newsroom.sgit.ai/demos/vaults/kitewing-websites/vault-app/examples/fennick-lane-garden/index.html)** is a community group: what it grows, the plots and the waiting list, a season of 15 events, a volunteer rota, news, and 14 growing guides that open in a reader.

!shot kw-quillon.webp | images/ | Quillon Heat & Plumbing: services, the areas it covers on a sketch map, how to book, what to do in an emergency, and 19 household guides, each marked as general guidance for a demonstration, not professional advice. | screenshot

- **[Quillon Heat & Plumbing](https://newsroom.sgit.ai/demos/vaults/kitewing-websites/vault-app/examples/quillon-heating/index.html)** is a local trade: eight services, a clickable sketch map of Harrowby and ten villages, how to book, what to do in an emergency, and a library of 19 household guides, searchable and filtered by topic. Every guide is marked as general guidance for a demonstration, not professional advice, and anything to do with gas sends you to a registered engineer. There are no reviews or testimonials: they would have been invented.

## How each one is made {#how}

Each site is the same shape, the one a vault app needs.

- **One HTML file,** with every style and script inside it, and pictures drawn as inline SVG. No fonts, images or scripts are fetched from anywhere.
- **The words and data in `content.json`** beside it. The page reads it from the vault when it is in one, falls back to a plain fetch, and then to a copy inlined in the page, so it also works opened as a file.
- **Ready for the owner to change by talking to it.** "Add a new mug in the celadon glaze", "move the June work day to the 19th", "add a guide on bleeding a radiator": each is an edit to `content.json`, which an agent with access to the repository makes in seconds. That is the handover the studio sells.
- **Checked on a phone.** Each fits a 390-pixel screen without scrolling sideways.

## A vault in a vault {#vaults}

Each site is also a vault: an encrypted, versioned sgit folder with an `app.json` that opens the site when the vault is opened. The studio's vault holds the three examples inside it, under `examples/`, so opening the studio's vault gives you the whole demonstration, and each example is also its own vault, to be handed to its owner.

The four vaults are created and committed, locally. Pushing them to the vault server needs an access token, and that step is the editor's. Until then, the four sites are served on this newsroom, from the same files, as previews. When they are pushed, the public read keys will be published here, as for the [other demonstration vaults](https://newsroom.sgit.ai/articles/inside-the-no-server-studio.html).

## What this does not claim {#limits}

- **Everything is made up:** the studio, the clients, the town, the people, the prices.
- **The guides are sample text,** for a demonstration, not advice.
- **The vaults are not pushed yet;** the previews are the same files.
- **The prices are hypotheses,** from [websites you own](https://newsroom.sgit.ai/articles/websites-you-own.html).

## Where this comes from {#sources}

My voice memo of 26 October 2026, and the brief the agents built the four sites from. Related: [websites you own](https://newsroom.sgit.ai/articles/websites-you-own.html), [inside the no-server studio](https://newsroom.sgit.ai/articles/inside-the-no-server-studio.html), [your own newsroom](https://newsroom.sgit.ai/articles/your-own-newsroom.html), [the homepage is a vault](https://newsroom.sgit.ai/articles/the-homepage-is-a-vault.html). Built by four of this site's agents in parallel, from one brief, and written up and checked by newsroom.writer; the editorial responsibility is mine.
