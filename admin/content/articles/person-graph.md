---
title: Person Graph: one picture of what we have been building, people and their agents with their own keys and repositories, links that count only both ways, kinds of link from "real" to "vouch to hire", groups as centres of gravity, countersigned claims, anonymous personas, a check for re-identification, all done through each person's own Claude, with mock-ups of the site and a simulation of 150 people and 40 fake accounts that shows why two-way links make bad actors cheap to spot
date: 2026-11-21
author: Dinis Cruz
author_url: about/index.html
summary: Everything we have been talking about this week is one thing. Every person, and every agent, has their own keys in a repository they control, usually the one behind their sovereign website. Links between them are signed, have a kind, from "this is a real person" to "I know them", "I worked with them" and "I would hire them", and count only when both sides publish them. Organisations countersign claims about work and study. People can publish an anonymous persona and be vouched for, and an agent team checks it cannot be traced back. Links group into centres of gravity, artists, founders, educators, professionals, agents, so nobody is one node with a thousand strangers, and the graph becomes a way to navigate everything we do. At first I say I know this person, and this one; then it takes on a life of its own, a distributed social network that no platform owns, run through each person's own Claude. I call it Person Graph, and I have mocked up four of its pages. I also simulated it: 150 fictional people in five groups and 40 fake accounts that spam links and fool three real people into linking back. Counting links puts 34 fakes in the top 40; spreading trust from three trusted people through two-way links only puts none there, and leaks 1.2% of the trust to the fakes. It degrades honestly as more real people are fooled, which is why every link must be a deliberate, signed act. Bad-actor detection then scales, because everyone's agent does a little of it.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: identity, web-of-trust, person-graph, sovereign-website, agents, simulation, article
status: published
---

!shot pg-profile.webp | images/ | A Person Graph profile, mocked up: two-way links with their kind, and claims countersigned. Fictional. | concept

## In short {#in-short}

- **One picture:** people and agents, keys in repositories, two-way links, countersigned claims.
- **Kinds of link:** real, know, worked with, vouch to hire, operates.
- **Groups as centres of gravity,** so the graph stays readable and navigable.
- **A distributed social network,** run through each person's own Claude, owned by nobody.
- **Simulated:** counting links rewards fakes; two-way trust does not.
- **Bad-actor detection scales,** because everyone's agent does a little of it.

## It is all one thing {#one}

This week's articles are pieces of the same picture. Everyone has keys they make themselves, published in a repository they control ([a directory of people and their keys](/articles/a-directory-of-people-and-keys.html)), usually the repository behind their own sovereign website ([the showroom](/articles/the-showroom.html)). Links between people count only when both sides publish them, and organisations countersign claims about work and study, with link lists instead of revocation lists ([a web of trust for careers](/articles/a-web-of-trust-for-careers.html)). A person who cannot go public can publish a persona and be vouched for ([an anonymous profile, vouched for](/articles/an-anonymous-profile-vouched-for.html)), and an agent team checks it cannot be traced back ([can you find me?](/articles/can-you-find-me.html)). Agents are in the graph too, with their own keys, operated by a person for a time ([agents have an identity now](/articles/agents-have-an-identity-now.html)).

Put together, that is the world of the CV, and of people: a graph of who is real, who knows whom, who worked with whom and who would hire whom, that anyone can check and nobody owns. I call it Person Graph.

## Kinds of link {#kinds}

- **Real:** I met this person, or saw them on stage; they are a person, not an avatar.
- **Know:** I know them.
- **Worked with:** on this, in these years.
- **Vouch to hire:** given rarely.
- **Operates:** a person runs this agent, until a date.

Every kind is a signed statement, and every one counts only when the other side signs it back.

## Groups, as centres of gravity {#groups}

!shot pg-groups.webp | images/ | Groups as centres of gravity: you link to people in an area, not to a thousand strangers. Fictional. | concept

You do not want one person who knows a thousand people, or two hundred. Links fall into groups: artists, professionals, startup founders, educators, agents. The artists on our hub, for example, are a natural group, and people like Emily Cruz and Grace Farrell could link to each other and to the people who know their work. Each group is a centre of gravity, the way the Galaxy drew the team's agents ([a galaxy of agents](/articles/a-galaxy-of-agents.html)), and it gives a way to navigate: from a person to their groups, from a group to its people, from a project to the people around it.

## Done through Claude {#claude}

This is practical now, when it never was for PGP, because each person has an AI to do the work. Their Claude makes the keys, signs a link when they scan a QR code, publishes it in their repository, notices links waiting for a reply, and answers questions by walking the graph: how do I know this person, did they work there, is it still true.

!shot pg-check.webp | images/ | Checking a link: three steps, every link two-way and read now from both repositories. Fictional. | concept

At first it is me saying I know this person, and this one, and this one. Then it takes on a life of its own: people link to people, groups form, and it becomes the social element we want, a distributed social network connected by signed links instead of by a platform.

## A simulation {#simulation}

!shot pg-network.webp | images/ | A simulated graph: 150 people in five groups, and 40 fakes that spam links and fool three people. | chart

To see how it behaves, I simulated it. 150 fictional people in five groups, each linked both ways to a few people in their group and sometimes across; 39 one-way claims among real people that nobody returned. Then an attack: 40 fake accounts, densely linked to each other both ways, sending 200 links to real people, and fooling three real people into linking back.

Two ways of ranking the 190 accounts:

- **Counting links,** one-way included, as a connections count does: 34 of the top 40 are fakes. The median fake has 16 links, the median real person 8.
- **Trust from three trusted people,** spread for eight steps through two-way links only and divided by each account's number of links, the approach of SybilRank ([Cao and others, NSDI 2012](https://www.usenix.org/conference/nsdi12/technical-sessions/presentation/cao)): none of the top 40 are fakes, and only 1.2% of the trust leaks into the fake cluster, through the three people who were fooled.

!shot pg-trust.webp | images/ | Counting links puts 34 fakes in the top 40; two-way trust puts none, until many real people are fooled. | chart

It is not magic, and the simulation shows where it weakens. As the fakes fool more real people, more trust leaks: 4% with ten, 12% with twenty, 18% with forty, 29% with eighty, more than half the real network, where real people and fakes are much harder to tell apart. The defence is that fooling a real person costs a real, signed, deliberate act. That is why one-way links count for nothing, and why every two-way link should be a choice, ideally in person, by QR code.

## Bad actors, at scale {#bad-actors}

!shot pg-badactor.webp | images/ | An account that does not look right, and the two people who linked back, asked to check. Fictional. | concept

This is a way to scale the detection of bad actors, which is one of the problems social networks have never solved. A fake cluster has a shape: many links out, almost none returned, two-way links only among new accounts, no countersigned claims, and very little trust reaching it from anyone real. An agent can see that shape. Nothing is deleted and nobody is banned: the one-way links simply count for nothing, and anyone can see why. The few real people who linked back are asked, through their own agents, whether they really know this person; if they remove the link, the cluster is cut off. Detection is spread across everyone's agent, not done by one platform.

## The site {#site}

Person Graph would be a site, and a tool, on sovereign websites:

- **Profiles,** read from each person's repository: keys, two-way links by kind, claims and who countersigned them.
- **Check a link:** how do I know this person, every step read now from both sides.
- **Groups:** the centres of gravity, and how to move between them.
- **Explore:** the shape of the graph, and what an agent flags.

It is also a business, as the web of trust article set out: free for people, paid by the organisations that countersign and by those who verify at scale.

## What this does not claim {#limits}

- **The mock-ups and the simulation use fictional people;** no links exist yet between the people named on the hub.
- **The simulation is small and simple;** a real network, and a smarter attacker, will behave differently.
- **Person Graph is a proposal;** pki.sgit.ai, the keys and the two-way rule exist.

## Where this comes from {#sources}

My own thinking in writer-10's session on 21 November 2026, pulling together the week's articles. The simulation is a script in the writer's session: 150 people, 40 fakes, seeded random links, trust spread for eight steps from three seeds over two-way links, ranked by trust per link, and a sweep of 3 to 80 fooled people; its figures are as shown. Related: [a web of trust for careers](/articles/a-web-of-trust-for-careers.html), [an anonymous profile, vouched for](/articles/an-anonymous-profile-vouched-for.html), [can you find me?](/articles/can-you-find-me.html), [a directory of people and their keys](/articles/a-directory-of-people-and-keys.html), [agents have an identity now](/articles/agents-have-an-identity-now.html), [a galaxy of agents](/articles/a-galaxy-of-agents.html), [the showroom](/articles/the-showroom.html).
