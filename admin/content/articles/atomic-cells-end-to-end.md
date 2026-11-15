---
title: Atomic cells, end to end: the £500 website as AgentiCCells' first offering, an order on a queue, an agentic team that builds a public site, a customer who steers it from their browser with a key, and a handover, with no daily work for the founder
date: 2026-11-15
author: Dinis Cruz
author_url: about/index.html
summary: AgentiCCells now has a first site live, and I think we are close to an offering that is easy to buy and easy to deliver. It starts with the simplest case: a public website, as an atomic cell, for a one-off price anchored at £500. The customer orders and picks a name on agenticcells.app or agenticcells.site; the order goes on a queue; an agentic team builds the site; and the customer steers it without any accounts of their own, by making a key in their browser and sending us its public half, so their requests reach the agents through a vault lane that an agent reads every hour. When they are ready, the repository moves to their GitHub and they have three months to bring their own domain. That is the no-touch mode. In the second mode, from £1,500, the customer has their own GitHub and Claude accounts, and we set the team up in them and step away. Every step is a primitive that a person or an agent can run from a queue, so it scales by capacity, not by my time, and the first implementers are people who have already done it: Angelo Leggio, Silvio Switha and José Bota, with Vicky Wang as project manager.
version: v0.14.100
license: https://creativecommons.org/licenses/by/4.0/
tags: agenticcells, offering, websites, atomic-cells, pki, vaults, workflow, article
status: published
---

!shot ace-flow.webp | images/ | The £500 cell end to end: order, queue, build, preview, key, steer, handover, with no daily work for the founder. | flow

## In short {#in-short}

- **The first offering is a website, as an atomic cell,** for a one-off price anchored at £500.
- **The customer steers it from their browser:** a key, a QR code, requests on a vault lane, an agent that wakes every hour.
- **No-touch or their own:** we run the team for them, or we set it up in their GitHub and Claude accounts and step away.
- **Public websites only,** to keep publishing simple; three months on our subdomain before their own domain.
- **It scales by capacity, not by my time:** every step is a primitive on a queue.
- **The first implementers:** Angelo Leggio, Silvio Switha and José Bota, with Vicky Wang as project manager.

## Why start with a website {#why}

[AgentiCCells](/articles/starting-agenticcells.html) has its first site live at agenticcells.com, built by its own agentic team from the articles on this site. That is the product in miniature: a team of agents, given a brief, that builds and keeps a website. So that is what I want to sell first.

Even the customers who will buy the bigger setups will start simple. A website is the easiest way for someone to experience what an agentic team can do for them, and I can offer it to the people I already help, my brother among them, end to end, from the agentic model to their site being published.

## Atomic cells {#atomic}

!shot ace-organisms.webp | images/ | The ladder as organisms: a single cell at £500, a cell handed over at £1,500, a colony at £5,000, a network at £20,000. | concept

Every offering is an atomic cell. It is a one-off price for a setup that is useful on its own and that the customer owns. There is no subscription; we keep no state; and when it is done, it is theirs.

The ladder reads well as biology. The £500 cell is a single-cell organism: one site, one small team, a feedback lane and a handover. The £1,500 cell is the same, set up with the customer in a couple of meetings and handed over into their own accounts. At £5,000 it becomes a colony, several cells integrated with the customer's work, with a conductor, a board and keys. At £20,000 it is a multi-cell organism: a custom network of cells, conductors of conductors, policies and observability ([six setups of an agentic system](/articles/six-setups-of-an-agentic-system.html)).

The £500 anchor is deliberate. It is a fair price, in pounds or in euros, and it leaves room: I can offer it for less to people I am helping, and someone else can deliver it with a margin.

## The £500 cell, end to end {#flow}

The flow has seven steps, and none of them needs me on a given day:

1. **Order.** The customer pays the one-off price and chooses a name, on agenticcells.app or agenticcells.site, whichever they prefer.
2. **Queue.** The order waits for capacity. Delivery is a matter of staff and agents, not of my diary.
3. **Build.** An agentic team, on our account, builds a public site in a repository, from a short brief.
4. **Preview.** The site goes live at their name on our domain.
5. **Key.** The customer makes a key in their browser, on the site itself, and sends us the public half as a QR code. We add it to the repository as a trusted key.
6. **Steer.** From then on, they can ask for changes. Their requests, signed with their key, go on an append lane in a vault; an agent wakes every hour, reads the lane, makes the changes and releases the site.
7. **Handover.** When they are ready, the repository moves to their GitHub, and they have three months to bring their own domain. Keeping their name on our domain for a while costs us almost nothing, so it is best effort, with a date.

Everything we use for this already exists: the agentic team that builds sites, the person keys we used at Web Summit ([a key for every person](/articles/a-key-for-every-person.html)), and the vault lanes our agents already talk through ([an inbox only your agents can write to](/articles/an-inbox-only-your-agents-can-write-to.html)).

## Two modes {#modes}

!shot ace-modes.webp | images/ | Two modes: we run the agentic team on our account for them, or we set it up in their GitHub and Claude accounts. | comparison

**No-touch: we run the team.** For the £500 cell, the agentic team runs on our accounts. The customer needs no accounts at all, only a browser to make a key. They steer by request, and the site is theirs to take.

**Their own: they run the team.** If the customer wants to control their own destiny, they need two things: a GitHub account and a Claude account, connected to each other. Our stack depends on Claude today, so that is a real requirement, and the first step is a guide that walks them through creating both and connecting them. Then we set up the agentic team in their accounts, the brief, the rules, the board and the site, and the handover is as simple as giving their GitHub access to the repository. That is the £1,500 cell, with a couple of meetings, and the mode the bigger cells build on.

## Why the console matters here {#control}

In both modes, what we are really selling is the ability to control the website through its agents. In the no-touch mode, the customer's key and the vault lane are their control; in their own mode, it is [the agentic console](/articles/an-agentic-console.html). Either way they can see what their agents do, ask for changes, and stop them.

## A queue, a staff, and the people {#people}

The test of the design is that it runs without me. An order arrives, it goes on the queue, someone picks it up, the agentic team builds, the customer steers, and it is handed over. Some of it can happen automatically; most of it is a person running a well-defined step with agents doing the work.

The first people on that queue are the ones who already did this with me at [Web Summit](/articles/ten-days-at-web-summit.html): Angelo Leggio, Silvio Switha and José Bota as implementers, and Vicky Wang as project manager. They will go on the AgentiCCells site as the people behind the offering, and as the first of a network of partners who can deliver it.

## We are our own first customers {#dogfood}

The same flow is how we will publish our own work. Many of the things we do deserve a small site of their own, and each one can be a cell on agenticcells.app, with me as the editor steering it through the same key and vault lane. Some of our demo vaults can move there too. Every one of them tests the offering and becomes an example to show the next customer.

## What this does not claim {#limits}

- **The prices and the flow are a proposal:** the steps exist as pieces, and the end-to-end flow is being built now by AgentiCCells' own team.
- **Public websites only,** for now.
- **The no-touch mode runs on our accounts during the build,** and moves to the customer at handover; the "no state on our side" promise holds after the handover.
- **The customer-run mode needs Claude and GitHub accounts,** which the customer creates and pays for.

## Where this comes from {#sources}

My own thinking, 15 November 2026, after AgentiCCells' first site went live. Earlier on this site: [starting AgentiCCells](/articles/starting-agenticcells.html), [selling mini agentic teams](/articles/selling-mini-agentic-teams.html), [six setups of an agentic system](/articles/six-setups-of-an-agentic-system.html), [an agentic console](/articles/an-agentic-console.html), [a key for every person](/articles/a-key-for-every-person.html), [an inbox only your agents can write to](/articles/an-inbox-only-your-agents-can-write-to.html), [websites you own](/articles/websites-you-own.html).
