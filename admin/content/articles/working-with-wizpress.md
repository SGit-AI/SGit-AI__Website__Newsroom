---
title: Working with WizPress: how the AI operating system for newsrooms, built in Faro, and our open-source trust stack fit together, WizPress doing the production, from the inbox to the draft to the CMS, and our layer making every article carry its own proof, with an evidence vault per story, a behaviour policy per agent, a journalist's signature and signed responses, and a thirty-day pilot with one regional newsroom
date: 2026-11-17
author: Dinis Cruz
author_url: about/index.html
summary: I am with WizPress today, and I think we fit together unusually well. WizPress, built in Faro and led by Nuno Costa, a former journalist and newsroom manager, describes itself as the AI operating system for newsrooms: it monitors inboxes, the web and trends, captures and transcribes interviews, turns press releases and documents into drafts with a fact-checking agent and house style, and publishes to WordPress or any CMS, with the journalist deciding. It already works with local, national and specialist media in Europe and the Middle East. What we have been building is the layer underneath: how a reader can see who wrote an article, who checked it and who stands behind it. At PrompTugal.news we now describe every piece with five axes, origin, research, claims, review and external responses, and a ladder from "published by an agent" to "on the record". WizPress's four stages map onto those axes almost one to one. So here is how we could work together: a behaviour policy for every agent that reads a newsroom's inbox; an encrypted evidence vault per story for recordings, transcripts and documents; a provenance record exported with every draft; the journalist's signature on the version readers see, with any later change a signed difference; signed responses from the people a story is about; and a network of local newsrooms whose stories climb, with their proof, to the region and the country. And a first step: one regional newsroom, thirty days, in the open.
version: v0.14.140
license: https://creativecommons.org/licenses/by/4.0/
tags: wizpress, newsrooms, journalism, provenance, pki, vaults, partnerships, portugal, article
status: published
---

!shot wiz-layer.webp | images/ | WizPress does the production; we add the trust underneath: a policy, a vault, the claims, a signature. | concept

## In short {#in-short}

- **WizPress is the AI operating system for newsrooms:** monitor, capture, draft, publish, with the journalist deciding.
- **We build the trust layer underneath:** who wrote it, who checked it, who signs it.
- **The two fit almost one to one:** WizPress's stages are our five provenance axes.
- **Six ways to work together,** from evidence vaults to signed responses to a local news network.
- **A first step:** one regional newsroom, thirty days, in the open.
- **Our side is open source,** free to adopt; WizPress keeps its product and its customers.

## WizPress {#wizpress}

[WizPress](https://wizpress.io/) was created in 2025 and is led by Nuno Costa, a former journalist and newsroom manager, with a team of about ten, supported by the Dengun product studio, at the Tech Campus in Faro. It calls itself the AI operating system for newsrooms, and the description is accurate:

- **Monitor:** it connects to a newsroom's email, so press releases arrive in WizPress and are scored against a keyword profile, and it watches web pages and trends.
- **Capture:** recordings on the phone with automatic transcription, audio and video uploads, documents and images.
- **Draft:** AI drafts from press releases, emails and documents, with the source beside the draft, a fact-checking agent, house-style rules and an assistant for rewrites and angles.
- **Publish:** one click to WordPress, or any CMS through its API.

Its customers are local, national and specialist media, in Portugal and beyond, and its own line is the right one: "The decision is always the journalist's." The goal "is not to replace journalism, but to free up time for it."

## What we build {#us}

We have spent the last months on the other half of the problem: when an AI can write five versions of the same article in a minute, how does a reader know what they are reading? At PrompTugal.news, the newsroom we ran at Web Summit, we now answer with a profile, not a label ([who wrote this, who checked it, who signs it](https://promptugal.news/articles/who-wrote-this-who-checked-it-who-signs-it.html)): five axes, each recorded with who and when. Origin: did a person write it, dictate it, or brief an agent? Research: whose, and how? Claims: how many facts, each with its evidence. Review: which agents and models checked it, which person edited it, with the diff. External: signed responses from the people it is about. And a ladder, from published by an agent, to sourced, to verified by several models, to signed by a person, to on the record.

Underneath that sit the pieces of our stack: sgit's encrypted, versioned vaults ([how a vault works](/articles/how-a-vault-works.html)); a key for every person, and QR codes to pass keys and links safely ([a secret is a QR code](/articles/a-secret-is-a-qr-code.html)); and behaviour policies that say what each agent may reach ([where assist becomes execute](/articles/where-assist-becomes-execute.html)). All of it open source.

## How we fit together {#together}

WizPress's four stages map onto those five axes almost one to one. That is the opportunity: WizPress already keeps the journalist in charge; our layer lets the reader see it.

1. **A behaviour policy for the inbox.** WizPress reads newsrooms' email, which is the most sensitive thing an agent can touch. A written, measured policy, what it may read, what it may never do, such as send, makes that easy for a publisher to approve ([the email agentic cell](/articles/the-email-agentic-cell.html)).
2. **An evidence vault per story.** Recordings, transcripts, press releases and documents behind an article, kept in an encrypted vault the newsroom owns, opened by an editor or a lawyer with a key, never by the host. Sources stay protected, and the evidence for every claim stays one link away ([every story has an address](/articles/every-story-has-an-address.html)).
3. **A provenance record with every draft.** WizPress already knows the origin, the source beside the draft and what its fact-checking agent found. Exported as a small record, that is most of the five axes, ready to show beside the article.
4. **The journalist's signature.** The journalist signs the version readers see with their own key; any change after that, a headline included, is a signed difference in public ([signed by the source](/articles/signed-by-the-source.html)).
5. **Signed responses.** The people and companies a story is about are asked to respond, and their answers, signed, sit on the article. On the record, not in the comments.
6. **A network of local newsrooms.** WizPress's customers are exactly the local and regional media that PrompTugal.news is designed around: news filed where it happens, climbing to the region and the country with its proof, and local outlets certifying big outlets' stories about their patch ([local trust, certified upwards](/articles/local-trust-certified-upwards.html)).

## A first pilot {#pilot}

!shot wiz-pilot.webp | images/ | A first pilot: one regional newsroom, thirty days, keys, vaults, provenance, signatures, responses. | process

The way to find out is small and in the open. One WizPress customer, one section, thirty days. In the first week, keys for its journalists and an evidence vault per story. In the second, WizPress exports a provenance record with each draft. In the third, journalists sign what they publish, and a provenance page sits beside each article. In the fourth, the people the stories are about are asked for signed responses. And we measure: time per article, corrections, and what readers make of it.

The newsroom keeps using WizPress exactly as it does today.

## What each side brings {#bring}

- **WizPress:** a working product, paying newsrooms, the journalism and newsroom experience of its founder, and the trust of local media in Portugal and beyond.
- **Us:** an open-source trust stack, vaults, keys, signatures and behaviour policies, already running in our own newsrooms, and PrompTugal.news as a live test bed.
- **Both:** a story that matters now, that AI in newsrooms can make journalism more trustworthy, not less, if the proof travels with every article.

## What this does not claim {#limits}

- **This is a proposal,** written on the day we met; nothing is agreed.
- **WizPress's figures and claims are its own,** from its website.
- **The provenance model is new,** and is itself still climbing its own ladder at PrompTugal.news.

## Where this comes from {#sources}

[wizpress.io](https://wizpress.io/), read on 17 November 2026: its product, pricing, team and customers as it describes them. PrompTugal.news, [who wrote this, who checked it, who signs it](https://promptugal.news/articles/who-wrote-this-who-checked-it-who-signs-it.html), 17 November 2026. Earlier on this site: [how a vault works](/articles/how-a-vault-works.html), [a secret is a QR code](/articles/a-secret-is-a-qr-code.html), [where assist becomes execute](/articles/where-assist-becomes-execute.html), [the email agentic cell](/articles/the-email-agentic-cell.html), [every story has an address](/articles/every-story-has-an-address.html), [signed by the source](/articles/signed-by-the-source.html), [local trust, certified upwards](/articles/local-trust-certified-upwards.html).
