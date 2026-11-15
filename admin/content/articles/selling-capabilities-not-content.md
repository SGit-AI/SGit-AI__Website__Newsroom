---
title: Selling capabilities, not content: a reply to Florent Daudens' "We have the protocols. Where are the products?", from two newsrooms built for agents, PrompTugal.news going local and a storm site built in a night, and what we think the products are
date: 2026-11-15
author: Dinis Cruz
author_url: about/index.html
summary: Florent Daudens asks a sharp question: publishers now have the protocols, connectors, collective licences and telemetry standards, so where are the products? His answer is that "we need to move beyond licensing content and start selling capabilities", and his bet is connecting the news subscriptions people already pay for to their personal agents. I agree, and our own newsrooms point at what those capabilities can be. The Storm Charles site went from a voice brief to 2,618 pages in three days, every fact with its source and the time it was read: not articles, but a live, sourced picture of a crisis that people and agents could use. PrompTugal.news ran a newsroom of agent desks for Web Summit and is now going local: a site for Portugal, one for the Algarve and one for every Algarve town, each a lens on one shared semantic graph, which is a product a town, a business or an agent can use, not a stream of articles. And for Florent's open questions on access, permissions and payment, we have been building answers with keys people own, vaults opened by read keys, licences on every page, a meter that charges for what you read, and pages written for agents. This is our second reply to him.
version: v0.14.106
license: https://creativecommons.org/licenses/by/4.0/
tags: publishers, agents, ai, journalism, promptugal, storm-charles, reply, article
status: published
---

!shot scc-stack.webp | images/ | The publisher-agent stack Florent Daudens describes, against what our newsrooms already do. | comparison

## In short {#in-short}

- **Florent Daudens asks where the products are,** now that publishers have the protocols.
- **His answer, which I agree with:** sell capabilities, not content.
- **The Storm Charles site was a capability:** 2,618 pages in three days, every fact sourced and timed.
- **PrompTugal.news going local is a product:** a site per town, each a lens on one shared graph.
- **For access, permissions and payment,** we have answers: keys people own, read keys, licences, a meter, pages for agents.
- **This is our second reply to Florent,** after [would you pay to plug this newsroom in?](/articles/would-you-pay-to-plug-this-newsroom-in.html)

## His question {#question}

In [We have the protocols. Where are the products?](https://fdaudens.substack.com/p/we-have-the-protocols-now-what-are) (and [on LinkedIn](https://lnkd.in/p/eduvEsh7)), Florent Daudens, co-founder of Mizal, lists what has arrived in a few months: Reuters and Getty with MCP services, university presses piloting access through ChatGPT Edu and a shared gateway, the Internet Licensing Collective's first customer, and a telemetry standard from a coalition of large publishers. His point is that protocols alone cannot create a market: "We need to move beyond licensing content and start selling capabilities." The opportunity he is most excited about is connecting the subscriptions people already pay for to their personal agents, because "people already pay for journalism. But their AI agents don't have access to the content they're paying for."

I agree with all of it. The question is what a capability looks like, and we have two newsrooms that suggest an answer.

## A storm site is a capability {#storm}

When Storm Charles reached Lisbon during Web Summit, I asked our agents, by voice, for a site about it. Three days later it had 2,618 pages and 1,434 versions, with desks for the weather, flights, transport and the cloud, and every fact carried its source and the time it was read ([Storm Charles, a newsroom built in a night](/articles/storm-charles-a-newsroom-built-in-a-night.html)).

That is not content to license. It is a capability: a live, sourced picture of a situation, kept current, that a person can read and an agent can query, with the provenance to trust it. The value is not in any one article; it is in having the whole picture, now, with its sources.

## A newsroom by place is a product {#place}

[PrompTugal.news](/articles/promptugal-news-the-newsroom-we-ran.html) ran a newsroom of agent desks for Web Summit: 73 signed articles in ten days, a reviewer for every draft, every source opened at its own address. Now it is going local ([PrompTugal.news by place](/articles/promptugal-news-by-place.html)): one site for Portugal, one for the Algarve and one for every Algarve town, each on its own subdomain, each a lens on one shared semantic graph of stories, places, companies, institutions and events. A story about a company in Loulé leads on Loulé's site and is a small item on the national one.

That is the kind of product Florent is asking for. A town's site is a service for the people, businesses and agents of that town: what is happening in AI where they are, with every fact sourced, and the graph behind it to ask questions of. An agent working for a business in Faro does not need our articles; it needs that lens, and the graph, on demand.

## Answers to the open questions {#answers}

Florent lists the questions Mizal is still working out: the user experience, authentication and permissions, what publishers will expose, and whether people want this at all. We have been working on the same ones, from the other side:

- **Access for agents:** every page of our newsrooms has a markdown twin and an `llms.txt` index, so an agent reads the page, not the chrome ([reading your way into an agentic team](/articles/reading-your-way-into-an-agentic-team.html)).
- **Authentication and permissions:** keys people own. Each person gets a key, and an agent acting for them can hold one; private material sits in encrypted vaults opened by a key, and public material by a published read key ([a key for every person](/articles/a-key-for-every-person.html)).
- **Conditions:** a licence on every page, and, for the agents themselves, Agent Behaviour Policies that say what each may reach and do ([what can your agent reach?](/articles/what-can-your-agent-reach.html)).
- **Payment and verification:** this newsroom charges for what is read, not what is scrolled, with the reader in control of the meter ([your reading, your controls](/articles/your-reading-your-controls.html)); articles and releases are signed; and our observability records who read what.

None of these is finished, and a shared standard for telemetry would help us as much as anyone. But they are working pieces, and they point at an answer to "do people want this": they want the capability, the town's picture or the storm's, delivered where they already are.

## What I would build next {#next}

With Florent's framing, I would build three things. A subscription that a person's agent can hold as a key, so the paywall is a permission, not a login page. A lens per place and per topic, sold as a capability, with its graph exposed to agents under a licence. And a decision service on top, a graph for one decision with every source ([a market for sweets](/articles/a-market-for-sweets.html)), which is where trusted journalism is worth most to an agent: at the moment its person has to decide.

## What this does not claim {#limits}

- **The local sites are a strategy, not yet built;** the storm site and PrompTugal.news ran in November 2026.
- **The meter and keys are working pieces on our own sites,** not a product sold to publishers.
- **Florent's examples and quotes are from his post** of 15 November 2026, summarised here.

## Where this comes from {#sources}

Florent Daudens, [We have the protocols. Where are the products?](https://fdaudens.substack.com/p/we-have-the-protocols-now-what-are), AI in the News, 15 November 2026, and [his LinkedIn post](https://lnkd.in/p/eduvEsh7). Earlier on this site: [would you pay to plug this newsroom in?](/articles/would-you-pay-to-plug-this-newsroom-in.html), [Storm Charles, a newsroom built in a night](/articles/storm-charles-a-newsroom-built-in-a-night.html), [PrompTugal.news, the newsroom we ran](/articles/promptugal-news-the-newsroom-we-ran.html), [PrompTugal.news by place](/articles/promptugal-news-by-place.html), [a key for every person](/articles/a-key-for-every-person.html), [your reading, your controls](/articles/your-reading-your-controls.html), [a market for sweets](/articles/a-market-for-sweets.html).
