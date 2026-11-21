# An anonymous profile, vouched for: how someone who needs to leave their job without going public can publish a persona that shows the depth of their work but not their name, how the web of trust lets people who know them vouch for it, with different kinds of connection from "this is a real person" to "I would hire them", how an employer reaches them, and the one risk to test, triangulation, sgit.ai

> Someone I know is in a job at a company heading in the wrong direction. They want to leave, but they cannot go public yet. So we will publish a profile for them, a persona, anonymised enough that nobody can trace it back, but strong enough to make someone say: I want to hire that person, because it shows their history and the depth of their work. The missing piece was how an employer finds and trusts them, and the web of trust solves it. The persona has its own key. People who know the person, and who are public themselves, vouch for the persona with signed links it countersigns. And there are different kinds of link: this is a real person, I met them; I know them; I worked with them; and, given rarely, I would hire them. The more credible the people who vouch, the more hireable the person becomes, and someone who has been in an industry for years should have many, across disciplines. An employer checks the vouchers in the graph and writes to the persona, sealed to its key. The same typed links fix a softer problem too: when I vouch for someone like Vicky Wang, it becomes a signed statement anyone can check, not a recommendation on a platform. The risk is triangulation: with enough vouchers, someone may work out who it is, so an agent should try to, before anyone else does.

*Source: <https://newsroom.sgit.ai/articles/an-anonymous-profile-vouched-for.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / An anonymous profile, vouched for: how someone who needs to leave their job without going public can publish a persona that shows the depth of their work but not their name, how the web of trust lets people who know them vouch for it, with different kinds of connection from "this is a real person" to "I would hire them", how an employer reaches them, and the one risk to test, triangulation

# An anonymous profile, vouched for: how someone who needs to leave their job without going public can publish a persona that shows the depth of their work but not their name, how the web of trust lets people who know them vouch for it, with different kinds of connection from "this is a real person" to "I would hire them", how an employer reaches them, and the one risk to test, triangulation

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-21 · [article v1.0.0](versions/an-anonymous-profile-vouched-for.md) · [newsroom v0.14.194](https://newsroom.sgit.ai/admin/versions.html) · careersidentityweb-of-trustprivacysovereign-websitepersonasarticle

***Abstract:** Someone I know is in a job at a company heading in the wrong direction. They want to leave, but they cannot go public yet. So we will publish a profile for them, a persona, anonymised enough that nobody can trace it back, but strong enough to make someone say: I want to hire that person, because it shows their history and the depth of their work. The missing piece was how an employer finds and trusts them, and the web of trust solves it. The persona has its own key. People who know the person, and who are public themselves, vouch for the persona with signed links it countersigns. And there are different kinds of link: this is a real person, I met them; I know them; I worked with them; and, given rarely, I would hire them. The more credible the people who vouch, the more hireable the person becomes, and someone who has been in an industry for years should have many, across disciplines. An employer checks the vouchers in the graph and writes to the persona, sealed to its key. The same typed links fix a softer problem too: when I vouch for someone like Vicky Wang, it becomes a signed statement anyone can check, not a recommendation on a platform. The risk is triangulation: with enough vouchers, someone may work out who it is, so an agent should try to, before anyone else does.*

An anonymous profile with its own key, vouched for by people you can check, reachable sealed.

## In short

- **A persona for someone who cannot go public yet:** their depth of work, without their name.
- **People who know them vouch for it,** with signed links the persona countersigns.
- **Different kinds of link,** from "a real person" to "I would hire them".
- **The more credible the vouchers, the more hireable the person.**
- **An employer writes to the persona,** sealed to its key; the reveal is the person's choice.
- **The risk is triangulation,** and an agent should test for it first.

## The situation

Someone I know is in a job, and the company is going in the wrong direction. They want to leave, but they cannot go public: not on LinkedIn, not with "open to work", not with a new site under their name. It is the inefficient part of the job market: the people best placed to be hired are often the ones who cannot say they are available.

So we will create a persona for them: a profile anonymised enough that it cannot be traced back to them, and powerful enough that someone reading it says, I want to hire that person. It shows the history and the depth: the kinds of problems they solved, the systems they built, how they work, what they want next. A sovereign website, like the others on [the hub](the-showroom.md), with everything that would identify them left out.

## The missing piece

The problem we had was trust and contact. An anonymous profile is easy to write and hard to believe, and if someone wants to hire that person, how do they reach them? My first answer was that I would be the go-between. The web of trust gives a better one ([a web of trust for careers](a-web-of-trust-for-careers.md)).

The persona is an identity of its own: a key pair, published in its own repository, like any other ([a key for every person](a-key-for-every-person.md)). People who know the real person, and who are public themselves, link to the persona, and the persona links back. An employer can check every one of those people, and write to the persona sealed to its key, through its inbox, without anyone in the middle ([an inbox only your agents can write to](an-inbox-only-your-agents-can-write-to.md)).

## Kinds of connection

This is where links need types, because "connected" means too many things:

- **Real.** I met this person, or saw them on stage; they may not know me, but I can say they are real. That matters more every month, as it gets harder to tell people from avatars.
- **Known.** I know them.
- **Worked with.** We worked together, on this, in these years.
- **Vouch to hire.** I would hire this person. I do not give this easily: there are not many people I would say it about.

Each is a signed link, counting only when the other side countersigns, like every link in the network.

## Credibility from the vouchers

One person vouching for another is weak. Five is something; ten, thirty, fifty is a lot. Someone who has been in an industry for years and is looking for a job should have many people able to vouch for them, and from different disciplines: managers, peers, people who reported to them, clients. And the more credible the people who vouch, the more valuable and hireable the person becomes. The vouchers are public and checkable; the person stays private. That is what turns an anonymous profile into something an employer can believe.

## Vouching in public, too

The same links fix a softer problem for people who are public. Take Vicky Wang: she ran a team of agents at Web Summit, and I think she is amazing ([a website that is her](a-website-that-is-her.md)). I vouch for her. Today the best I can do is a LinkedIn recommendation, which is soft and lives on a platform. With a typed link, "worked with" and "vouch to hire", signed by my key and countersigned by hers, it is a statement anyone, or anyone's agent, can check, and that she carries with her, in her own repository.

## Reaching them, and the reveal

An employer who likes what they see writes to the persona, sealed to its key; only the person can read it. If both want to go further, the person reveals who they are to that employer alone, by signing a link between the persona's key and their real identity and sending it sealed. Nothing becomes public that the person did not choose.

## The risk: triangulation

There is an honest risk. If enough people vouch for one persona, someone might work out who it is from who the vouchers have in common: the same company, the same years, the same city. Maybe that is part of the game; maybe not. Either way it should be tested before it is published, not after. So an agent should try to reverse-engineer each persona from its vouchers and its text, and the person decides what to change if it succeeds: fewer vouchers from one company, broader descriptions, or vouchers shown to an employer only after the first sealed exchange.

## What this does not claim

- **This is a proposal;** the first persona has not been published yet.
- **Anonymity is not guaranteed;** the triangulation test reduces the risk, it does not remove it.
- **The kinds of link are a proposal,** to be added to the register.

## Where this comes from

My own thinking in writer-10's session on 21 November 2026, building on the web of trust described the same day. The person the first persona is for is not named here and will not be. Related: [a web of trust for careers](a-web-of-trust-for-careers.md), [a key for every person](a-key-for-every-person.md), [an inbox only your agents can write to](an-inbox-only-your-agents-can-write-to.md), [a website that is her](a-website-that-is-her.md), [hired as an agentic worker](hired-as-an-agentic-worker.md), [the showroom](the-showroom.md).

## Threads

Agents & policy[This article as a graph →](graphs.md#an-anonymous-profile-vouched-for)

### Builds on

- [The showroom: what the Sovereign Website hub shows after its first days, 33 live sites from one pipeline, people's portfolios with five designs each, independent brochures for our startups, a provider guide, tools that run on the owner's own key, made-up businesses, a family of news sites, and the theme that is emerging across all of them, a site that is yours, says how it was made and can be worked on by your own AI](the-showroom.md) The Sovereign Website hub after its first days: 33 live sites from one pipeline, and the shared bones that are becoming the product.
- [A web of trust for careers: everyone with their own keys and their own repository, links that count only when both sides sign them, companies and universities countersigning who worked and studied where, link lists instead of revocation lists, an agent that checks any of it by following the graph, a business that somebody should build, and names for it, with Europe in mind](a-web-of-trust-for-careers.md) A web of trust for careers: keys in people's own repositories, links that count only both ways, and jobs and degrees countersigned.
- [A key for every person: how each person's conductor issues them a key for the team's site, seals what is for them, and how a signed message turns the public web into a channel the agents can trust](a-key-for-every-person.md) How each person's conductor issues them a key for the team's site: sealed to you, signed by you, and a lane the agents can trust.
- [An inbox only your agents can write to: a conductor publishes one append lane per agent, each lane's token sealed to that agent's own key, so everything needed to talk privately is public and only the right agent can use it](an-inbox-only-your-agents-can-write-to.md) A conductor publishes one append lane per agent, each token sealed to that agent's key: a private channel built from public material.
- [A website that is her: how Yiheng Wang's site was made in three passes in one evening, by the site factory, five design agents and then her own agent, with five designs, a kitchen brigade of 26 agents, a printable brief and a page for your AI, and why every claim on it is something she can talk about because she did it](a-website-that-is-her.md) Yiheng Wang's website, made in one evening by the site factory, five design agents and her own agent: five designs, every claim sourced, all of it her.
- [Hired as an agentic worker: what a sovereign website offers someone looking for a job, from a better CV that shows the depth of your work, you in action and a video of you talking, to a site you change with your own AI, a team of agents you work with, and a crash course in being an agentic worker served on a plate, four levels of involvement, each one a choice](hired-as-an-agentic-worker.md) What a sovereign website offers someone looking for a job: from a better CV to a crash course in being an agentic worker, four levels, each a choice.

### Continued by

- [Can you find me? A service that checks whether an anonymous profile can be traced back to its person before it is published, an agent team of six steps with several models attacking the draft on their own, the truth sealed with the owner and compared only in code, a rewriter that closes what leaked, run in a Claude session or in the browser, and who would use it](can-you-find-me.md) A service that tries to re-identify an anonymous profile before it is published: several models attack it, and code checks them against a sealed truth.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 525 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=525)

**Posting this article on LinkedIn?** The cover is [an-anonymous-profile-vouched-for.jpg](banners/an-anonymous-profile-vouched-for.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/an-anonymous-profile-vouched-for.html)*
