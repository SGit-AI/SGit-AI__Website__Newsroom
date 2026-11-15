---
title: A hub for agentic sites: every site AgentiCCells builds in a repository and an sgit vault, served at its own address, and listed on hub.agenticcells.site, where it can be found, promoted and copied as a template; with an orange grower as the first example
date: 2026-11-15
author: Dinis Cruz
author_url: about/index.html
summary: I want to build many small agentic websites, several a day, for customers and for ourselves, and each one will also be a template someone else could copy. So they need a home: a hub, like a code host for agentic sites, at hub.agenticcells.site. Every site lives in two places, a public repository and an sgit vault holding the same files, which makes the hub our first real integration with sgit: a vault can be cloned, opened locally because the sites are static, and handed on, so in the beginning vaults can be the distribution medium. Each site has a page on the hub with its owner, the team that built it, its live address on the customer's own domain or our subdomain, its repository and vault, its licence and its versions, and a site marked as a template shows how to copy it. Customers are listed only if they want to be, and for most of the people I work with, a place on the hub is a benefit. A separate agentic team will build it, and the first example to list is an orange grower in the Algarve who sells wholesale with delivery, a made-up customer played by me.
version: v0.14.102
license: https://creativecommons.org/licenses/by/4.0/
tags: agenticcells, hub, sgit, vaults, templates, websites, example, article
status: published
---

!shot hub-arch.webp | images/ | A hub for agentic sites: a repository and an sgit vault kept identical, the live site, and a page on the hub. | architecture

## In short {#in-short}

- **Many small agentic sites need a home:** hub.agenticcells.site, a code host for them.
- **Every site in two places:** a public repository and an sgit vault with the same files.
- **A page per site:** owner, team, live address, repository, vault, licence, versions; templates to copy.
- **Vaults as distribution:** clone a vault, open the static site locally, pass it on.
- **Listed by consent,** and promotion is a benefit for the owner.
- **The first example:** an Algarve orange grower selling wholesale with delivery, played by me.

## Why a hub {#why}

With [atomic cells](/articles/atomic-cells-end-to-end.html), building a small site becomes a matter of capacity, and I want to build many: for people I know, for customers, and for our own projects. Each one is also a standard, a theme that becomes a template. A template is only useful if people can find it, see it working, and copy it.

So the sites need a home where they are published, linked to their live addresses, and easy to copy. It should feel like a code host, a page per project with its history, but for agentic sites, and it should promote the people whose sites it lists.

## Every site in two places {#two-places}

Each site lives in a public repository, built and released by its agentic team and served by GitHub Pages, as now. It also lives in an **sgit vault** that holds the same files, pushed on every release, with its public read key on the hub page.

That makes the hub our first real integration with sgit, and a good stress test of it. Because our sites are static, a vault is a complete site: anyone can clone it, open it locally, or run it from the vault, and in the beginning a vault can be the distribution medium itself. For now we run both in parallel, check that they stay identical, and see how smooth each one is before deciding whether sites should also be served from vaults.

## A page per site {#pages}

Each site gets a page at `hub.agenticcells.site/<owner>/<site>/`: its name and what it does, its owner, the agentic team that built it, its live address, which is the customer's own domain or our subdomain while they get one, its repository, its vault and read key, its licence, its versions and screenshots. A site marked as a template shows how to copy it and what to change. The hub can be searched by kind (a shop, a newsroom, a portfolio, an event) and by place.

There is no database: each site carries a small `hub.json`, the hub keeps a registry of those files, and its pages are generated from them, like every other site we build ([the new data lake](/articles/the-new-data-lake.html)).

## Consent and promotion {#consent}

Nothing is listed without its owner's consent, recorded with the date, and a site leaves the hub the day its owner asks. For most of the people I am helping, being on the hub will be welcome: their site is seen alongside others, and if the hub gets traction, everyone listed gains from it.

## A separate team builds it {#team}

The hub is a site like any other, so it gets its own agentic team, with its own conductor, developer, designer, writer and security roles, and the same rules as AgentiCCells' first team ([starting AgentiCCells](/articles/starting-agenticcells.html)). Its first version lists agenticcells.com, the first example below, and two of this newsroom's demo vaults, and explains how a site is published to the hub and how to copy one.

## The first example: an orange grower {#oranges}

I want to start giving the teams briefs for sites several times a day, and the first is a made-up customer: an orange grower in the Algarve who sells wholesale and ships the oranges. A buyer, a shop or a juice bar, chooses the oranges and the quantity, chooses where they should be delivered, sees the price of the oranges and of the delivery, accepts it, and sends an order request. There are no payments on the site; the farmer confirms by reply.

I will play the farmer. A dedicated session plays the whole team, conductor, designer, editor, developer and security, each step signed and on the board. Once the site is live, I will steer it the way a customer would: a key made in my browser, and requests like "the late Valencias are in from Monday" sent through the site's lane ([atomic cells, end to end](/articles/atomic-cells-end-to-end.html)). It will say on every page that it is an example, and it will go on the hub as an example and as a template.

## What this does not claim {#limits}

- **The hub is a proposal,** briefed today to a new agentic team.
- **Serving sites from vaults is being tested,** in parallel with GitHub Pages, not yet decided.
- **The orange grower is made up,** an example played by me, with no real farm, prices or payments.

## Where this comes from {#sources}

My own thinking, 15 November 2026, and the briefs given to AgentiCCells' teams the same day. Earlier on this site: [atomic cells, end to end](/articles/atomic-cells-end-to-end.html), [starting AgentiCCells](/articles/starting-agenticcells.html), [the new data lake](/articles/the-new-data-lake.html), [reading your way into an agentic team](/articles/reading-your-way-into-an-agentic-team.html).
