# A web of trust for careers: everyone with their own keys and their own repository, links that count only when both sides sign them, companies and universities countersigning who worked and studied where, link lists instead of revocation lists, an agent that checks any of it by following the graph, a business that somebody should build, and names for it, with Europe in mind, sgit.ai

> How does a company know that someone really worked somewhere, held that job, or graduated from that university? How do I vouch for someone? On LinkedIn I have 30,000 connections and I do not know 30,000 people. We can now build something better on what we already have. Everyone has an identity, in fact several, with keys they make themselves, published in a repository they control, the same repository as their sovereign website. When I know someone, they show me a QR code, I sign, and I publish that link in my repository. It counts only when they publish theirs: a one-way link is a weak claim and carries no credibility. Companies and universities do the same: the person says "I worked here", the company countersigns. There are no revocation lists, only link lists: to check a link, an agent reads both repositories now, and if either side has removed it, it is gone. Following links is a few simple reads, so it scales, and most people are a few steps from anyone. No recommendations, only connections. Every organisation needs one of these internally, everything is versioned, and people's own AI can set up the keys and sign for them. It could be a LinkedIn for Europe, and a company in itself.

*Source: <https://newsroom.sgit.ai/articles/a-web-of-trust-for-careers.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / A web of trust for careers: everyone with their own keys and their own repository, links that count only when both sides sign them, companies and universities countersigning who worked and studied where, link lists instead of revocation lists, an agent that checks any of it by following the graph, a business that somebody should build, and names for it, with Europe in mind

# A web of trust for careers: everyone with their own keys and their own repository, links that count only when both sides sign them, companies and universities countersigning who worked and studied where, link lists instead of revocation lists, an agent that checks any of it by following the graph, a business that somebody should build, and names for it, with Europe in mind

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-21 · [article v1.0.0](versions/a-web-of-trust-for-careers.md) · [newsroom v0.14.194](https://newsroom.sgit.ai/admin/versions.html) · identityweb-of-trustcareerspkisovereign-websiteeuropebusiness-modelarticle

***Abstract:** How does a company know that someone really worked somewhere, held that job, or graduated from that university? How do I vouch for someone? On LinkedIn I have 30,000 connections and I do not know 30,000 people. We can now build something better on what we already have. Everyone has an identity, in fact several, with keys they make themselves, published in a repository they control, the same repository as their sovereign website. When I know someone, they show me a QR code, I sign, and I publish that link in my repository. It counts only when they publish theirs: a one-way link is a weak claim and carries no credibility. Companies and universities do the same: the person says "I worked here", the company countersigns. There are no revocation lists, only link lists: to check a link, an agent reads both repositories now, and if either side has removed it, it is gone. Following links is a few simple reads, so it scales, and most people are a few steps from anyone. No recommendations, only connections. Every organisation needs one of these internally, everything is versioned, and people's own AI can set up the keys and sign for them. It could be a LinkedIn for Europe, and a company in itself.*

Links in repositories, countersigned: a link counts only while both sides publish it.

## In short

- **Everyone has keys and a repository,** the same repository as their sovereign website.
- **A link counts only when both sides sign it;** one-way links carry no credibility.
- **Companies and universities countersign** who worked and studied there.
- **Link lists, not revocation lists:** a link is valid while both sides still publish it.
- **An agent checks anything by following the graph,** in a few reads.
- **No recommendations, only connections.** A business somebody should build, starting in Europe.

## The problem

Some of the simplest questions about people have no good answer online. Did this person work at that company? In that role, in those years? Did they graduate from that university? Do I know them, or did we just click a button once? I have 30,000 connections on LinkedIn, and I do not know 30,000 people. Yet there is a credibility in a connection: I would not add someone I have no connection to. That credibility is real, but nothing in today's networks lets anyone check it, and the network belongs to one platform.

## What we already have

We built most of this already. [pki.sgit.ai](https://pki.sgit.ai/) is a register of people and their public keys, made in the browser behind a passkey, verified by me first and then by each other, with one rule I care about a lot: a link only counts when it goes both ways ([a directory of people and their keys](a-directory-of-people-and-keys.md)). Its four rules come from how the old PGP keyservers were destroyed in 2019, flooded with signatures nobody could remove: only the owner writes to their own record, records are bounded in size, and every entry is signed by something you can check ([why the old ones failed](https://pki.sgit.ai/failure/index.html)). Agents already get their own keys this way, and I have signed for them ([agents have an identity now](agents-have-an-identity-now.md)). And keys pass by QR code, in person, in a second ([a secret is a QR code](a-secret-is-a-qr-code.md)).

## Identities, in repositories

Everyone has an identity, and in fact several: a personal one, a work one, one for each of their agents. Each is a key pair the person makes, with the public half published in a repository they control. For most people that is the repository behind their [sovereign website](the-showroom.md): the site shows who they are, and the repository holds their keys, their links and their claims, all signed, all versioned. People publish their own keys and their own signatures in their own repositories, which is what lets it scale: nobody hosts the graph.

## Links that go both ways

When I meet someone, they show me a QR code; I scan it, my agent signs a link, "I know this person, met in person, on this date", and publishes it in my repository. That is my claim. It becomes a link only when they publish the same link back in theirs. If I say I know you and you do not say you know me, that is a weak connection and it carries no credibility.

That one rule does a lot. It makes spam pointless, because a link nobody returns is worth nothing. It makes a connection mean something again, because both people chose it. And it makes behaviour visible: someone who links to everyone will have a graph that looks strange, and that is fine, because the graph says so.

## Who worked where

The same mechanism answers the career questions:

- **Employment.** I publish "I worked at Acme as an engineer from 2021 to 2025"; Acme's key countersigns it in Acme's repository. A former manager can countersign too.
- **Education.** I publish "I graduated from this university in this degree"; the university countersigns.
- **Vouching.** "I worked with this person on this project" is a link with a description, countersigned by both.

The person makes every claim; the organisation only confirms. Nobody publishes anything about someone who did not ask.

## Link lists, not revocation lists

Classic certificate systems publish lists of what is no longer valid, and every reader has to fetch them. We do the opposite: we publish what is valid. To check that I still trust someone, or that a company still confirms an employment, my agent reads both repositories now. If either side has removed the link, it is gone. Git keeps the history, so what was true and when stays checkable. A compromised key is different, and is withdrawn by a signed statement from that key, as pki.sgit.ai's rules already say ([the rules](https://pki.sgit.ai/rules/index.html)).

## Following the graph

Because every check is a few plain reads of public repositories, following the graph scales: from me to someone I know, to someone they know, to the company that confirms them. The small-world studies found most people are a few steps apart ([six degrees of separation](https://en.wikipedia.org/wiki/Six_degrees_of_separation)); my guess is that nobody would be more than seven or eight steps from anyone. Each person's own AI can do this for them: set up the keys, sign the links, publish them, and walk the graph to answer "how do I know this person, and is it still true?" That is what makes it practical now, when it never was for PGP: the people using these sites have Claude or another model to do the work.

## No recommendations

I would deliberately leave out recommendations, endorsements and scores. The network is about connecting and confirming: who knows whom, who worked where, who studied what. Credibility comes from the shape of the graph, not from ratings.

## Inside every organisation

Every company needs one of these internally: who is staff, in which role, since when, which agents act for whom, all signed and in version control, every change a commit. The same structure that answers "did Ben work at Acme?" from outside answers "may this agent act for Ben?" inside, which is where it meets behaviour policies ([feature behaviour policies](feature-behaviour-policies.md)).

## A LinkedIn for Europe

LinkedIn is global and belongs to one company. A professional network for Europe could be built on these principles instead: every person owns their record, every organisation owns its confirmations, and no platform owns the graph. It fits where Europe is already going, with the EU Digital Identity Wallet ([Regulation 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)), European Digital Credentials for Learning ([Europass](https://europass.europa.eu/en/european-digital-credentials-learning)) and W3C's Verifiable Credentials, a Recommendation since May 2025 ([VC 2.0](https://www.w3.org/TR/vc-data-model-2.0/)). Those formats could carry the claims; the repositories and the two-way links are what make the network.

## A business somebody should build

This could be a company in itself. A model that keeps the network open and still pays:

- **Free for people.** Keys, a repository, links and claims; the network has to be free to join to be a network.
- **Organisations pay to confirm.** A company or university gets its keys, its repository and an agent that countersigns employment or graduation claims against its own records, with a person's approval.
- **Verification as a service.** Anyone can walk the graph themselves, but recruiters and employers will pay for an agent that does it at scale, with a report and its evidence.
- **The internal edition.** An organisation's own directory of people and agents, signed and versioned, installed in its environment, as an agentic cell.
- **Onboarding.** Setting up keys and the first links, bundled with a sovereign website.

## Names

Some names to choose from:

- **Countersign:** says exactly what makes a link count.
- **Mutual:** a link is mutual or it is nothing.
- **Vouch:** the act at the heart of it.
- **Trellis:** a structure that people grow along.
- **Nexo:** "connection" in Portuguese and Spanish, for a network that starts in Europe.

My preference is Countersign for the mechanism and Mutual for the network.

## What this does not claim

- **The career network is a proposal;** pki.sgit.ai, the keys and the two-way rule exist.
- **Seven or eight steps is my estimate,** not a measurement of this network.
- **No organisation has countersigned an employment yet.**

## Where this comes from

My own thinking in writer-10's session on 21 November 2026, pki.sgit.ai's pages on its rules and on the 2019 keyserver failure, read that day, and the standards linked above. Related: [a directory of people and their keys](a-directory-of-people-and-keys.md), [PKI everywhere](pki-everywhere.md), [agents have an identity now](agents-have-an-identity-now.md), [a secret is a QR code](a-secret-is-a-qr-code.md), [the showroom](the-showroom.md), [hired as an agentic worker](hired-as-an-agentic-worker.md).

## Threads

Agents & policy[This article as a graph →](graphs.md#a-web-of-trust-for-careers)

### Builds on

- [A directory of people and their keys: pki.sgit.ai for the people I work with, verified by me first, then by each other, and a link that only counts when it goes both ways](a-directory-of-people-and-keys.md) pki.sgit.ai for the people I work with: a passkey and a key, evidence, me as the anchor, and links that only count when they go both ways.
- [Agents have an identity now: a key pair made in every session, published with its role, so any agent can seal a secret to it, and the piece the cloud providers could add](agents-have-an-identity-now.md) A key pair made in every agent session, published with its role in a repository, so any agent can seal a secret to it; what the clouds could add.
- [A secret is a QR code and a link to a public key: the workflow the QR experiment opens, who else already does this, and a format to share](a-secret-is-a-qr-code.md) Send a QR code and a link to a public key: the workflow the QR experiment opens, who already does this, and a format to share.
- [The showroom: what the Sovereign Website hub shows after its first days, 33 live sites from one pipeline, people's portfolios with five designs each, independent brochures for our startups, a provider guide, tools that run on the owner's own key, made-up businesses, a family of news sites, and the theme that is emerging across all of them, a site that is yours, says how it was made and can be worked on by your own AI](the-showroom.md) The Sovereign Website hub after its first days: 33 live sites from one pipeline, and the shared bones that are becoming the product.
- [Feature behaviour policies: taking the idea of agent behaviour policies down to every feature, bug fix and resource, so that a feature's policy is also its description, what changed is the difference between two policies, the gap between what a resource can do and what a feature needs is where the vulnerabilities live, and signed policies travelling with each request make a bug or an attack a path that was never supposed to exist](feature-behaviour-policies.md) Write a behaviour policy per feature: it describes the feature, sets what to enforce, and makes a bug or attack a path outside it.
- [PKI everywhere: from now on every message, secret and handover starts with a signature, and how an agent gets its first key](pki-everywhere.md) From now on every message, secret and handover is signed. The hard part is an agent's first key: two patterns, one built and one proposed.
- [Hired as an agentic worker: what a sovereign website offers someone looking for a job, from a better CV that shows the depth of your work, you in action and a video of you talking, to a site you change with your own AI, a team of agents you work with, and a crash course in being an agentic worker served on a plate, four levels of involvement, each one a choice](hired-as-an-agentic-worker.md) What a sovereign website offers someone looking for a job: from a better CV to a crash course in being an agentic worker, four levels, each a choice.

### Continued by

- [Person Graph: one picture of what we have been building, people and their agents with their own keys and repositories, links that count only both ways, kinds of link from "real" to "vouch to hire", groups as centres of gravity, countersigned claims, anonymous personas, a check for re-identification, all done through each person's own Claude, with mock-ups of the site and a simulation of 150 people and 40 fake accounts that shows why two-way links make bad actors cheap to spot](person-graph.md) Person Graph: people and agents with their own keys, links that count only both ways, groups, claims, and a simulation of fakes being caught.
- [An anonymous profile, vouched for: how someone who needs to leave their job without going public can publish a persona that shows the depth of their work but not their name, how the web of trust lets people who know them vouch for it, with different kinds of connection from "this is a real person" to "I would hire them", how an employer reaches them, and the one risk to test, triangulation](an-anonymous-profile-vouched-for.md) An anonymous profile for someone who cannot go public yet, made credible by people who vouch for it in the web of trust.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 524 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=524)

**Posting this article on LinkedIn?** The cover is [a-web-of-trust-for-careers.jpg](banners/a-web-of-trust-for-careers.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/a-web-of-trust-for-careers.html)*
