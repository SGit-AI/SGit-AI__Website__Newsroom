---
title: Your website, from a vault: how to show someone five versions of their own website without publishing anything, sealed in an encrypted sgit vault and opened with a QR code, a link or a zip on one drop page, the demo pipeline from a name to an email, and how a demo becomes their sovereign website without starting again
date: 2026-11-19
author: Dinis Cruz
author_url: about/index.html
summary: There are a lot of people I want to show a Sovereign Agentic Website to, and the best way is to show them their own: five versions of it, made by agents. The problem is that a demo cannot be public. Our repositories and sites are public by default, and "public but not linked" has never felt right. The answer has been in front of us: encrypted vaults. The demo cell takes a name, researches only public information, builds five designs, has them reviewed, and seals all five into one sgit vault. The person gets a QR code, a link with the key after the #, or a zip, and drops it on one page, which decrypts the vault in their browser and shows their site in a sandboxed frame, with a banner and the five designs one tap apart. Nothing is published, the key never reaches a server, and if they say yes, the factory makes their repository from the same vault, so the demo becomes the first chapter of their site's history. This piece maps the workflow and the pipeline, and what is still to build.
version: v0.14.173
license: https://creativecommons.org/licenses/by/4.0/
tags: sovereign-website, sgit, vaults, demos, qr-codes, go-to-market, article
status: published
---

!shot fv-flow.webp | images/ | The demo pipeline: a name in, five designs sealed in one vault, opened by QR code, link or zip. | concept

## In short {#in-short}

- **The best demo is someone's own website,** five versions of it.
- **A demo cannot be public,** and "public but not linked" never felt right.
- **So it goes in an encrypted vault:** five designs, one key.
- **One drop page, three ways in:** a QR code, a link with the key after the #, or a zip.
- **The browser decrypts it;** nothing is published and the key never reaches a server.
- **If they say yes,** their sovereign website is made from the same vault.

## The problem with demos {#problem}

I want to reach a lot of people with this: owners of small businesses, people I meet at events, investors, partners. The most convincing thing I can show any of them is not our site, or a slide. It is their own website, in five versions, made by agents from what is already public about them.

But that demo cannot be public. Everything we put in our repositories is public by default, and I want to keep it that way: I do not want to start dealing with private repositories. Until now the workaround has been a site that is public but not linked, which works, and has never felt right. A person who has not yet agreed to anything should not find a version of themselves on the open web.

## The answer: a vault {#vault}

sgit's vaults solve exactly this. Everything in a vault is encrypted before it leaves the machine that wrote it, and a web page can open one in the browser: compute where the head is from the key, fetch a handful of objects, decrypt them, and either read files or run an app in a sandboxed frame ([how a vault works](/articles/how-a-vault-works.html)). A website is just files. So a website can live in a vault, and a page can show it to whoever holds the key, and to nobody else.

It also feels natural in a way the public-but-unlinked site never did. The vault is not a hiding place; it is where the work lives, versioned and signed, and the demo is just the first thing in it. And there is a continuation: the same vault can become the person's real site.

## The drop page {#drop}

!shot fv-drop.webp | images/ | The drop page: three ways in, and the site rendered in the browser with five designs a tap apart. | concept

One page, with three ways in:

- **Scan a QR code,** on a card, a letter or a slide ([a secret is a QR code](/articles/a-secret-is-a-qr-code.html)).
- **Open a link,** with the key after the `#`. That part of a link is never sent to the server, so the server that serves the page never sees the key.
- **Drop a zip,** the whole site in one file, opened in the browser with no server at all. For someone who wants to evaluate it offline, or deploy it themselves, it is the simplest form there is.

The page decrypts the vault and renders the site in a sandboxed frame, with a banner on top: a demo made for you, by agents; five designs; nothing here is public; make it yours. The five designs are one tap apart. The banner can be hidden, so the site can be seen as it would really be.

It needs a name, and I would keep it under sgit, at an address we already have, something like from.sgit.ai: one generic page, the same for everyone, and the same page could sit on sovereignwebsite.ai.

## The demo pipeline {#pipeline}

This is a job for an agentic cell, and it maps cleanly:

1. **A name.** I give the demo cell a person or a company, and why: someone I am about to meet, an investor, a shop I walked past.
2. **Research,** from public information only: what they do, in their own words, how they look today.
3. **Five designs,** by the cell's designers, as for every site we make ([the website cell](/articles/the-website-cell.html)).
4. **Review:** nothing private, every claim checked against its source, and every page marked as a demo.
5. **Seal:** all five into one vault, and from its key a QR code, a link and a zip.
6. **Send:** the agent drafts the email, and I send it, as I do every email the agents draft for me.
7. **Open:** they drop it on the page and see their site.

All I am doing is selling. The cell does the rest, and a Claude session can run it for many names at once.

## From demo to their site {#convert}

If they say yes, nothing is thrown away. The factory makes their repository from the same vault: the design they chose becomes their [sovereign website](/articles/sovereign-agentic-website.html), live at its own address, with [the team inside it](/articles/a-website-with-a-team-inside.html). The vault they opened is the first chapter of the site's history.

The keys follow the same path. Today the vault key is the whole secret. The better version gives the person a key pair of their own, so that what we send them is sealed to their key, and once the site is theirs, only they can change it ([a key for every person](/articles/a-key-for-every-person.html)). Vaults do not fully support that yet; it is on the list.

## What is still to build {#build}

- **The drop page,** taking a QR code, a link or a zip, and rendering a vault's site with the banner and the five designs.
- **A demo cell** that runs the pipeline from a name to a sealed vault and a drafted email.
- **The step from vault to repository** in the factory.
- **Private keys for vaults,** so a demo can be sealed to its recipient.

## What this does not claim {#limits}

- **None of this is built yet;** the vault and its browser reading are, the drop page and the demo cell are not.
- **A demo uses public information only,** is marked as a demo, and is shown only to the person it is about.
- **The address is a proposal;** nothing has been registered for it.

## Where this comes from {#sources}

My own thinking, in writer-10's session on 19 November 2026, building on [how a vault works](/articles/how-a-vault-works.html), [a secret is a QR code](/articles/a-secret-is-a-qr-code.html), [a key for every person](/articles/a-key-for-every-person.html), [the website cell](/articles/the-website-cell.html), [Sovereign Agentic Website](/articles/sovereign-agentic-website.html) and [a website with a team inside](/articles/a-website-with-a-team-inside.html).
