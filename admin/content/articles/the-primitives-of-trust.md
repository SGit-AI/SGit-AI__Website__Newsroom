---
title: The primitives of trust: why a web of trust between people works now when my earlier attempts at a key store did not, a site per person, keys made in browsers and in agent sessions, signing and following links done by an engine the user never sees, links that only count from the other side, kinds and provenance that can be confirmed, schemas each owner defines, and why it is easy to game one node and hard to game them all
date: 2026-11-21
author: Dinis Cruz
author_url: about/index.html
summary: I tried to build a public key store more than once and never could, because I did not have the right workflows. Now I think we have nailed it, and the reason is a Wardley map lesson: a set of primitives has become commodity, and only then does the next order of magnitude become possible. The primitives are a site per person on GitHub Pages, later DNS; public-key cryptography, which is mature; keys made easily in browsers and inside agent sessions, ephemeral or long-lived; and an engine that signs, verifies, links and follows keys transparently, so the work never lands on the user. That engine is an agent, which is just a model with a loop and some tools; I bet it works with Haiku and small open-weight models too. On top of them sits trust through connectivity. Anybody can link to anybody, but a link from A to B means nothing until B links back, and a person's page only holds the links they made, so bad actors cannot write into anyone's record: they have to convince the person. Links carry kinds and provenance, a date, a place, an event, so they can be confirmed: if someone says they saw me present, my agent nudges me and I confirm. Each owner can define their own schema; only nodes, edges and signatures need to be constant, and the model works out the rest. It is easy to game one node and very hard to game them all at once. And it solves identity in an open way that works with every identity provider rather than replacing them.
version: v0.14.200
license: https://creativecommons.org/licenses/by/4.0/
tags: identity, pki, web-of-trust, wardley-maps, primitives, agents, article
status: published
---

!shot prim-map.webp | images/ | The primitives under a web of trust: what was custom is now commodity, so the top layer works now. | concept

## In short {#in-short}

- **I tried before and failed;** the workflows were missing, not the cryptography.
- **A set of primitives has become commodity,** and that makes the next layer possible.
- **An engine signs, verifies and follows keys for the user,** and it can be a small model.
- **A link counts only from the other side;** nobody can write into your record.
- **Links carry kinds and provenance,** so they can be confirmed.
- **Easy to game one node, hard to game them all;** and it works with every identity provider.

## Why now {#why-now}

I have tried to build a public key store more than once, and never could, because I did not have the right workflows. The ideas are old. In February I wrote about key graphs and revocation through graph maintenance rather than revocation lists, about a web of trust where fake networks are destroyed the moment one node is flagged, and about using the same PKI to sign facts and sources, not just files ([SG/Send's briefs](https://github.com/the-cyber-boardroom/SGraph-AI__App__Send/tree/dev/team/humans/dinis_cruz/briefs)). What changed is not the idea. It is that the pieces underneath have become commodities.

That is the Wardley map lesson: sometimes you need a number of things commoditised before you can build the higher order of magnitude on top ([the site factory works](/articles/the-site-factory-works.html)). Now they are.

## The primitives {#primitives}

- **A site per person.** GitHub Pages, so an agent can publish to the web from a commit; later, DNS records as well.
- **Public-key cryptography,** which is as mature as it gets.
- **Keys made easily anywhere:** in a browser behind a passkey, and inside a Claude session or any agent, ephemeral or long-lived ([agents have an identity now](/articles/agents-have-an-identity-now.html)).
- **Git:** every link and every change versioned and signed.
- **QR codes,** to exchange keys in person in a second ([a secret is a QR code](/articles/a-secret-is-a-qr-code.html)).
- **An engine** that creates keys, signs them, links them, verifies them and follows them, transparently. This is important: we cannot push this overhead onto users. The engine is an agent, and an agent is, in quotes, just a model with a loop and some tools. It does not need the most powerful model: I bet this works with Haiku and with light open-weight models.

Put together, that is a trust layer that grows through connectivity: the more people connect, the more meaning the connections carry, and the better it gets.

## Links only count from the other side {#direction}

Anybody can link to anybody. That is fine, the same as anyone can fork anything. A link from A to B has no strength until B links back to A ([a web of trust for careers](/articles/a-web-of-trust-for-careers.html)).

The important property is where links live. When I go to someone's page, I see the links they made, out from them, and nothing else. Nobody else can add to it, so there is nothing for a bad actor to corrupt: to appear in that person's graph, they have to convince that person to link to them. That is the first rule pki.sgit.ai already published, only the owner writes to their own record, drawn from how the old keyservers were flooded ([why the old ones failed](https://pki.sgit.ai/failure/index.html)), and it is also what makes the graph scale.

Links that point at me but that I have not returned are, in effect, connection requests. I can ask my own ChatGPT or Claude: which keys should I sign today, who is linking to me that I have not linked back?

## Kinds and provenance {#provenance}

A link should say what it means and where it comes from: I saw this person, I know them, I work with them, I recommend them, and also when and where. I saw this person present at this event, on this date. I worked with this person on this project, in this place.

Provenance makes links confirmable. If someone says they saw me present at an event, my agent can nudge me: these people say they saw you there. I can answer: yes, I was there and I presented. That confirmation is what prevents a lot of gaming, because a claim about a real event is easy for the other side to check, and easy to refuse. The checks can mostly be deterministic: dates, places and events compared in code, with the model only reading and proposing, behind guards against injection ([an anonymous profile, vouched for](/articles/an-anonymous-profile-vouched-for.html)).

## Schemas each owner defines {#fractal}

Not everything has to be consistent. Each owner of a repository can define their own primitives and their own schema, their own kinds of link and their own claims: the fractal semantic graph. What needs to stay constant is small: nodes, edges, where the signatures are and how they are made. Everything else, a model can read and connect. I do not need everyone to agree on a format; I need the model to be able to figure it out.

## Easy to game one node, hard to game them all {#security}

That diversity is itself a security property. It is easy to game one node, or one component. It is very hard to game them across the board, all at the same time, when every node is owned by someone different, links count only both ways, provenance can be checked, and trust spreads only through confirmed links ([Person Graph](/articles/person-graph.html)).

## Identity, in the open {#identity}

This is a way to solve identity, and to manage identities at scale in an open way. It is also the foundation for something I have wanted for a long time: an author signing a document, an article or a news story, so readers can know that identity is real and that the words are theirs. And it plays with every identity provider rather than against them: a GitHub account, a domain, a passkey, a national digital identity wallet, each is evidence attached to a key, another strength in the graph rather than a competitor ([a directory of people and their keys](/articles/a-directory-of-people-and-keys.html)).

## Towards a standard {#standard}

The next step is to write it down as a small standard and workflow, so any agent can follow it: where a person's keys are published, where their links and claims live, what a link must contain (who, kind, provenance, date, signature), how a link is confirmed, and how an agent walks the graph. Everything else stays open for each owner to define.

## What this does not claim {#limits}

- **Kinds, provenance and confirmations are a proposal;** pki.sgit.ai's keys and two-way rule exist.
- **That small models can run the engine is a bet,** to be tested.
- **DNS-based publishing is later;** sites come first.

## Where this comes from {#sources}

My own thinking in writer-10's session on 21 November 2026; my briefs of February and March 2026 in the SG/Send repository (chain of trust and key graphs, 21 February; trust web and content trust, 23 February; identity infrastructure and the web of trust, 7 March), read that day; and pki.sgit.ai. Related: [a web of trust for careers](/articles/a-web-of-trust-for-careers.html), [Person Graph](/articles/person-graph.html), [an anonymous profile, vouched for](/articles/an-anonymous-profile-vouched-for.html), [a directory of people and their keys](/articles/a-directory-of-people-and-keys.html), [agents have an identity now](/articles/agents-have-an-identity-now.html), [a secret is a QR code](/articles/a-secret-is-a-qr-code.html), [the site factory works](/articles/the-site-factory-works.html).
