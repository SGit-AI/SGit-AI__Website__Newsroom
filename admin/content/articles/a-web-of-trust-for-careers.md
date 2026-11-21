---
title: A web of trust for careers: everyone with their own keys and their own repository, links that count only when both sides sign them, companies and universities countersigning who worked and studied where, link lists instead of revocation lists, an agent that checks any of it by following the graph, a business that somebody should build, and names for it, with Europe in mind
date: 2026-11-21
author: Dinis Cruz
author_url: about/index.html
summary: How does a company know that someone really worked somewhere, held that job, or graduated from that university? How do I vouch for someone? On LinkedIn I have 30,000 connections and I do not know 30,000 people. We can now build something better on what we already have. Everyone has an identity, in fact several, with keys they make themselves, published in a repository they control, the same repository as their sovereign website. When I know someone, they show me a QR code, I sign, and I publish that link in my repository. It counts only when they publish theirs: a one-way link is a weak claim and carries no credibility. Companies and universities do the same: the person says "I worked here", the company countersigns. There are no revocation lists, only link lists: to check a link, an agent reads both repositories now, and if either side has removed it, it is gone. Following links is a few simple reads, so it scales, and most people are a few steps from anyone. No recommendations, only connections. Every organisation needs one of these internally, everything is versioned, and people's own AI can set up the keys and sign for them. It could be a LinkedIn for Europe, and a company in itself.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: identity, web-of-trust, careers, pki, sovereign-website, europe, business-model, article
status: published
---

!shot wot-graph.webp | images/ | Links in repositories, countersigned: a link counts only while both sides publish it. | concept

## In short {#in-short}

- **Everyone has keys and a repository,** the same repository as their sovereign website.
- **A link counts only when both sides sign it;** one-way links carry no credibility.
- **Companies and universities countersign** who worked and studied there.
- **Link lists, not revocation lists:** a link is valid while both sides still publish it.
- **An agent checks anything by following the graph,** in a few reads.
- **No recommendations, only connections.** A business somebody should build, starting in Europe.

## The problem {#problem}

Some of the simplest questions about people have no good answer online. Did this person work at that company? In that role, in those years? Did they graduate from that university? Do I know them, or did we just click a button once? I have 30,000 connections on LinkedIn, and I do not know 30,000 people. Yet there is a credibility in a connection: I would not add someone I have no connection to. That credibility is real, but nothing in today's networks lets anyone check it, and the network belongs to one platform.

## What we already have {#have}

We built most of this already. [pki.sgit.ai](https://pki.sgit.ai/) is a register of people and their public keys, made in the browser behind a passkey, verified by me first and then by each other, with one rule I care about a lot: a link only counts when it goes both ways ([a directory of people and their keys](/articles/a-directory-of-people-and-keys.html)). Its four rules come from how the old PGP keyservers were destroyed in 2019, flooded with signatures nobody could remove: only the owner writes to their own record, records are bounded in size, and every entry is signed by something you can check ([why the old ones failed](https://pki.sgit.ai/failure/index.html)). Agents already get their own keys this way, and I have signed for them ([agents have an identity now](/articles/agents-have-an-identity-now.html)). And keys pass by QR code, in person, in a second ([a secret is a QR code](/articles/a-secret-is-a-qr-code.html)).

## Identities, in repositories {#identity}

Everyone has an identity, and in fact several: a personal one, a work one, one for each of their agents. Each is a key pair the person makes, with the public half published in a repository they control. For most people that is the repository behind their [sovereign website](/articles/the-showroom.html): the site shows who they are, and the repository holds their keys, their links and their claims, all signed, all versioned. People publish their own keys and their own signatures in their own repositories, which is what lets it scale: nobody hosts the graph.

## Links that go both ways {#links}

When I meet someone, they show me a QR code; I scan it, my agent signs a link, "I know this person, met in person, on this date", and publishes it in my repository. That is my claim. It becomes a link only when they publish the same link back in theirs. If I say I know you and you do not say you know me, that is a weak connection and it carries no credibility.

That one rule does a lot. It makes spam pointless, because a link nobody returns is worth nothing. It makes a connection mean something again, because both people chose it. And it makes behaviour visible: someone who links to everyone will have a graph that looks strange, and that is fine, because the graph says so.

## Who worked where {#work}

The same mechanism answers the career questions:

- **Employment.** I publish "I worked at Acme as an engineer from 2021 to 2025"; Acme's key countersigns it in Acme's repository. A former manager can countersign too.
- **Education.** I publish "I graduated from this university in this degree"; the university countersigns.
- **Vouching.** "I worked with this person on this project" is a link with a description, countersigned by both.

The person makes every claim; the organisation only confirms. Nobody publishes anything about someone who did not ask.

## Link lists, not revocation lists {#links-not-revocation}

Classic certificate systems publish lists of what is no longer valid, and every reader has to fetch them. We do the opposite: we publish what is valid. To check that I still trust someone, or that a company still confirms an employment, my agent reads both repositories now. If either side has removed the link, it is gone. Git keeps the history, so what was true and when stays checkable. A compromised key is different, and is withdrawn by a signed statement from that key, as pki.sgit.ai's rules already say ([the rules](https://pki.sgit.ai/rules/index.html)).

## Following the graph {#graph}

Because every check is a few plain reads of public repositories, following the graph scales: from me to someone I know, to someone they know, to the company that confirms them. The small-world studies found most people are a few steps apart ([six degrees of separation](https://en.wikipedia.org/wiki/Six_degrees_of_separation)); my guess is that nobody would be more than seven or eight steps from anyone. Each person's own AI can do this for them: set up the keys, sign the links, publish them, and walk the graph to answer "how do I know this person, and is it still true?" That is what makes it practical now, when it never was for PGP: the people using these sites have Claude or another model to do the work.

## No recommendations {#no-recommendations}

I would deliberately leave out recommendations, endorsements and scores. The network is about connecting and confirming: who knows whom, who worked where, who studied what. Credibility comes from the shape of the graph, not from ratings.

## Inside every organisation {#organisations}

Every company needs one of these internally: who is staff, in which role, since when, which agents act for whom, all signed and in version control, every change a commit. The same structure that answers "did Ben work at Acme?" from outside answers "may this agent act for Ben?" inside, which is where it meets behaviour policies ([feature behaviour policies](/articles/feature-behaviour-policies.html)).

## A LinkedIn for Europe {#europe}

LinkedIn is global and belongs to one company. A professional network for Europe could be built on these principles instead: every person owns their record, every organisation owns its confirmations, and no platform owns the graph. It fits where Europe is already going, with the EU Digital Identity Wallet ([Regulation 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)), European Digital Credentials for Learning ([Europass](https://europass.europa.eu/en/european-digital-credentials-learning)) and W3C's Verifiable Credentials, a Recommendation since May 2025 ([VC 2.0](https://www.w3.org/TR/vc-data-model-2.0/)). Those formats could carry the claims; the repositories and the two-way links are what make the network.

## A business somebody should build {#business}

This could be a company in itself. A model that keeps the network open and still pays:

- **Free for people.** Keys, a repository, links and claims; the network has to be free to join to be a network.
- **Organisations pay to confirm.** A company or university gets its keys, its repository and an agent that countersigns employment or graduation claims against its own records, with a person's approval.
- **Verification as a service.** Anyone can walk the graph themselves, but recruiters and employers will pay for an agent that does it at scale, with a report and its evidence.
- **The internal edition.** An organisation's own directory of people and agents, signed and versioned, installed in its environment, as an agentic cell.
- **Onboarding.** Setting up keys and the first links, bundled with a sovereign website.

## Names {#names}

Some names to choose from:

- **Countersign:** says exactly what makes a link count.
- **Mutual:** a link is mutual or it is nothing.
- **Vouch:** the act at the heart of it.
- **Trellis:** a structure that people grow along.
- **Nexo:** "connection" in Portuguese and Spanish, for a network that starts in Europe.

My preference is Countersign for the mechanism and Mutual for the network.

## What this does not claim {#limits}

- **The career network is a proposal;** pki.sgit.ai, the keys and the two-way rule exist.
- **Seven or eight steps is my estimate,** not a measurement of this network.
- **No organisation has countersigned an employment yet.**

## Where this comes from {#sources}

My own thinking in writer-10's session on 21 November 2026, pki.sgit.ai's pages on its rules and on the 2019 keyserver failure, read that day, and the standards linked above. Related: [a directory of people and their keys](/articles/a-directory-of-people-and-keys.html), [PKI everywhere](/articles/pki-everywhere.html), [agents have an identity now](/articles/agents-have-an-identity-now.html), [a secret is a QR code](/articles/a-secret-is-a-qr-code.html), [the showroom](/articles/the-showroom.html), [hired as an agentic worker](/articles/hired-as-an-agentic-worker.html).
