---
title: An anonymous profile, vouched for: how someone who needs to leave their job without going public can publish a persona that shows the depth of their work but not their name, how the web of trust lets people who know them vouch for it, with different kinds of connection from "this is a real person" to "I would hire them", how an employer reaches them, and the one risk to test, triangulation
date: 2026-11-21
author: Dinis Cruz
author_url: about/index.html
summary: Someone I know is in a job at a company heading in the wrong direction. They want to leave, but they cannot go public yet. So we will publish a profile for them, a persona, anonymised enough that nobody can trace it back, but strong enough to make someone say: I want to hire that person, because it shows their history and the depth of their work. The missing piece was how an employer finds and trusts them, and the web of trust solves it. The persona has its own key. People who know the person, and who are public themselves, vouch for the persona with signed links it countersigns. And there are different kinds of link: this is a real person, I met them; I know them; I worked with them; and, given rarely, I would hire them. The more credible the people who vouch, the more hireable the person becomes, and someone who has been in an industry for years should have many, across disciplines. An employer checks the vouchers in the graph and writes to the persona, sealed to its key. The same typed links fix a softer problem too: when I vouch for someone like Vicky Wang, it becomes a signed statement anyone can check, not a recommendation on a platform. The risk is triangulation: with enough vouchers, someone may work out who it is, so an agent should try to, before anyone else does.
version: v0.14.194
license: https://creativecommons.org/licenses/by/4.0/
tags: careers, identity, web-of-trust, privacy, sovereign-website, personas, article
status: published
---

!shot anon-persona.webp | images/ | An anonymous profile with its own key, vouched for by people you can check, reachable sealed. | concept

## In short {#in-short}

- **A persona for someone who cannot go public yet:** their depth of work, without their name.
- **People who know them vouch for it,** with signed links the persona countersigns.
- **Different kinds of link,** from "a real person" to "I would hire them".
- **The more credible the vouchers, the more hireable the person.**
- **An employer writes to the persona,** sealed to its key; the reveal is the person's choice.
- **The risk is triangulation,** and an agent should test for it first.

## The situation {#situation}

Someone I know is in a job, and the company is going in the wrong direction. They want to leave, but they cannot go public: not on LinkedIn, not with "open to work", not with a new site under their name. It is the inefficient part of the job market: the people best placed to be hired are often the ones who cannot say they are available.

So we will create a persona for them: a profile anonymised enough that it cannot be traced back to them, and powerful enough that someone reading it says, I want to hire that person. It shows the history and the depth: the kinds of problems they solved, the systems they built, how they work, what they want next. A sovereign website, like the others on [the hub](/articles/the-showroom.html), with everything that would identify them left out.

## The missing piece {#missing}

The problem we had was trust and contact. An anonymous profile is easy to write and hard to believe, and if someone wants to hire that person, how do they reach them? My first answer was that I would be the go-between. The web of trust gives a better one ([a web of trust for careers](/articles/a-web-of-trust-for-careers.html)).

The persona is an identity of its own: a key pair, published in its own repository, like any other ([a key for every person](/articles/a-key-for-every-person.html)). People who know the real person, and who are public themselves, link to the persona, and the persona links back. An employer can check every one of those people, and write to the persona sealed to its key, through its inbox, without anyone in the middle ([an inbox only your agents can write to](/articles/an-inbox-only-your-agents-can-write-to.html)).

## Kinds of connection {#kinds}

This is where links need types, because "connected" means too many things:

- **Real.** I met this person, or saw them on stage; they may not know me, but I can say they are real. That matters more every month, as it gets harder to tell people from avatars.
- **Known.** I know them.
- **Worked with.** We worked together, on this, in these years.
- **Vouch to hire.** I would hire this person. I do not give this easily: there are not many people I would say it about.

Each is a signed link, counting only when the other side countersigns, like every link in the network.

## Credibility from the vouchers {#credibility}

One person vouching for another is weak. Five is something; ten, thirty, fifty is a lot. Someone who has been in an industry for years and is looking for a job should have many people able to vouch for them, and from different disciplines: managers, peers, people who reported to them, clients. And the more credible the people who vouch, the more valuable and hireable the person becomes. The vouchers are public and checkable; the person stays private. That is what turns an anonymous profile into something an employer can believe.

## Vouching in public, too {#public}

The same links fix a softer problem for people who are public. Take Vicky Wang: she ran a team of agents at Web Summit, and I think she is amazing ([a website that is her](/articles/a-website-that-is-her.html)). I vouch for her. Today the best I can do is a LinkedIn recommendation, which is soft and lives on a platform. With a typed link, "worked with" and "vouch to hire", signed by my key and countersigned by hers, it is a statement anyone, or anyone's agent, can check, and that she carries with her, in her own repository.

## Reaching them, and the reveal {#reveal}

An employer who likes what they see writes to the persona, sealed to its key; only the person can read it. If both want to go further, the person reveals who they are to that employer alone, by signing a link between the persona's key and their real identity and sending it sealed. Nothing becomes public that the person did not choose.

## The risk: triangulation {#triangulation}

There is an honest risk. If enough people vouch for one persona, someone might work out who it is from who the vouchers have in common: the same company, the same years, the same city. Maybe that is part of the game; maybe not. Either way it should be tested before it is published, not after. So an agent should try to reverse-engineer each persona from its vouchers and its text, and the person decides what to change if it succeeds: fewer vouchers from one company, broader descriptions, or vouchers shown to an employer only after the first sealed exchange.

## What this does not claim {#limits}

- **This is a proposal;** the first persona has not been published yet.
- **Anonymity is not guaranteed;** the triangulation test reduces the risk, it does not remove it.
- **The kinds of link are a proposal,** to be added to the register.

## Where this comes from {#sources}

My own thinking in writer-10's session on 21 November 2026, building on the web of trust described the same day. The person the first persona is for is not named here and will not be. Related: [a web of trust for careers](/articles/a-web-of-trust-for-careers.html), [a key for every person](/articles/a-key-for-every-person.html), [an inbox only your agents can write to](/articles/an-inbox-only-your-agents-can-write-to.html), [a website that is her](/articles/a-website-that-is-her.html), [hired as an agentic worker](/articles/hired-as-an-agentic-worker.html), [the showroom](/articles/the-showroom.html).
