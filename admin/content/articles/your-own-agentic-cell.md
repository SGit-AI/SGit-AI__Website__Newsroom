---
title: Your own agentic cell, end to end: how a person asks for a site like the ones we made for Yiheng Wang and Silvio Switha, through a key pair in the browser, a vault they fill themselves and the site factory, with only three human gates, and then continues in their own Claude on their own repository
date: 2026-11-17
author: Dinis Cruz
author_url: about/index.html
summary: Since the sites for Yiheng Wang and Silvio Switha went up, people have been asking for one of their own. Each site is cheap in tokens. What costs is the workflow around it: collecting the person's details and photos, the first round of designs, and the hand-over. So the product is the workflow, and this is the plan, written up by the conductor agent of PrompTugal from my brief and now in my words. A person arrives at a start page, their browser makes a key pair, and they ask for a cell with a signed request and no secrets. I approve it. A welcome pack arrives sealed to their key: a template vault, their own lane to the factory, and a key scoped to creating one vault. They fill their vault over days with photos, words, links, style and a signed consent, then seal its read key to the factory. The factory turns it into a request, I merge it, and the site factory makes the repository, the address, the site and a first round of five designs, written back into their vault. They choose, I approve a GitHub invitation, and they carry on in their own Claude, with a CLAUDE.md written for them. Everything is automated, signed and encrypted, except three gates that are mine: approve the request, merge it, approve the invitation.
version: v0.14.137
license: https://creativecommons.org/licenses/by/4.0/
tags: agenticcells, site-factory, onboarding, pki, vaults, product, article
status: published
---

!shot onb-flow.webp | images/ | Your own agentic cell: a key, a request, a vault, the factory, five designs, a hand-over; three human gates. | process

## In short {#in-short}

- **People ask for a site like Yiheng's and Silvio's;** the sites are cheap, the workflow is not.
- **So the product is the workflow:** a secure, guided intake, the factory, and a hand-over.
- **It starts with a key pair in the browser** and a signed request with no secrets.
- **The person fills their own vault,** over days, and seals it to the factory.
- **The factory makes the site and five designs,** written back into their vault.
- **They continue in their own Claude,** on their own repository.
- **Three human gates:** approve, merge, invite.

## Why now {#why}

When the sites for [Yiheng Wang](/articles/a-website-that-is-her.html) and [Silvio Switha](/articles/a-portfolio-with-a-film-first.html) went up, the first reaction from several people was: can I have one? Each site is cheap to make in tokens. What costs is everything around it: collecting a person's details and photos, running the first round of designs, and handing it over so they can keep it alive. Today that means a Claude session per person waiting for "drop the photos here", and me in the middle of every step.

So the thing to build is not the site; it is the workflow. I briefed it, by mistake, in PrompTugal's conductor session instead of here, and its conductor wrote a thorough plan. This is that plan, in my words, because it is the right one.

## Ask, with a key {#ask}

It starts at a start page, "create your own agentic cell", with what it is, three live examples, what you will be asked for and what happens to your data. On arrival, the browser makes a key pair with pki.sgit.ai's own module, one key to receive and one to sign, with the private halves kept in the browser and never exported, and shows it as a code and a QR code: this is you ([a secret is a QR code](/articles/a-secret-is-a-qr-code.html)). A draft of the basics, name, what you do, links, what you want the site to say, stays in the browser.

Then one button: ask for a cell. It writes to the factory's intake lane: the public key, a short signed note, the headline fields and a way to reach you. An append lane accepts writes and returns nothing, so the page can carry its token openly: the worst anyone can do is send a request ([an inbox only your agents can write to](/articles/an-inbox-only-your-agents-can-write-to.html)).

## Gate one: I approve {#approve}

The intake agent drains the lane, checks each signature against the key inside it, and lists the requests for me, in a private vault, with Approve and Not now. One tap per request. This is the cost control and the abuse control: nothing that costs tokens or storage happens before it.

## A welcome pack, sealed to your key {#welcome}

Once approved, the person receives one message, sealed to their public key and signed by the factory's, with an expiry: as a pki.sgit.ai link by email, or on a lane their page watches. Inside: the template vault to start from, which holds no secrets; their own lane to the factory; a key scoped to creating one vault; and the factory's public key, also published at a stable address so they can check it. No key ever travels in clear.

## Your vault, filled by you {#vault}

The template vault carries a small app that guides them: about you, photos (originals kept, web sizes made in the browser), your own words, links, style (three sites you like and why, colours, what to avoid), and consent, what may be public and that agents will read the vault, signed with their key. They can fill it over days, share it with someone who helps them, and it stays theirs, encrypted ([how a vault works](/articles/how-a-vault-works.html)).

When they are ready, "send to the factory" seals the vault's read key, not its write key, to the factory's public key.

## Gate two: I merge {#merge}

The intake agent opens the vault, checks it is complete, photos present and consent signed, and writes the factory request as a pull request: what the site needs, copy, photos and style notes, while their private notes stay in the vault. I merge it, and the factory's apply workflow does what it already does: the repository, the address at `<name>.agenticcells.site`, and the site ([the site factory works](/articles/the-site-factory-works.html)).

## Five designs, back in their vault {#designs}

One factory session runs the first round of five designs from the vault's photos and words, the way Yiheng's and Silvio's five designs were made, instead of a waiting session per person. The designs go back into their vault, each with a screenshot, a preview link and a note, and their app shows them side by side. They pick one and comment in the vault; the factory applies it.

## Gate three: the hand-over {#handover}

The factory proposes inviting their GitHub account to the site's repository as a collaborator; I approve; they accept. The repository carries a CLAUDE.md written for its owner: what the site is, how to change words and photos, the checks, how to release, what not to touch. From then on they work in their own Claude session, the way Yiheng's own agent took over her site within an hour of it being handed to her.

The invitation itself is made by a small workflow in the factory, triggered by a merged invite file, with the admin token as a CI secret, so no agent session ever holds it.

## Security, and what it costs {#security}

- **Keys travel only sealed to a public key;** templates hold no secrets; every request and every send is signed.
- **The factory reads only what a person seals to it,** and only the read key.
- **Consent is a signed file** in the person's vault; what is public is their choice.
- **A security specialist agent reviews** the start page and the lane protocol before the first outside person.
- **Free for the first ten cells,** to learn the workflow and count the tokens per cell, before any price.

## What this does not claim {#limits}

- **This is a plan,** for me to decide and for the factory's agents to build; none of it exists end to end yet.
- **The scoped key is a pilot** until per-person keys exist.
- **The GitHub hand-over needs checking** with the first person before it is promised.

## Where this comes from {#sources}

The plan "Your own agentic cell, end to end", written by conductor@PrompTugal.dinis from my brief of 17 November 2026, in the PrompTugal.news repository (`board/spec-agentic-cells-onboarding.md`). Earlier on this site: [a website that is her](/articles/a-website-that-is-her.html), [a portfolio with a film first](/articles/a-portfolio-with-a-film-first.html), [the site factory works](/articles/the-site-factory-works.html), [a secret is a QR code](/articles/a-secret-is-a-qr-code.html), [an inbox only your agents can write to](/articles/an-inbox-only-your-agents-can-write-to.html), [how a vault works](/articles/how-a-vault-works.html), [patient vaults, answered](/articles/patient-vaults-answered.html).
