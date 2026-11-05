---
title: The Web Summit team, part five: the last day of setup, 180 releases, every person getting a key, an accountant counting the team's tokens, synthetic users testing the merch, and an inbox only the agents can write to
date: 2026-11-04
author: Dinis Cruz
author_url: about/index.html
summary: Wednesday 4 November was the Web Summit team's last day of setup before the outreach starts, and the team's own journalist agent counted it at 20:57: 173 releases of the team's site and 283 source commits from 37 agents, with four people on the team fully wired, able to open the team's vaults. By the end of the evening there were over 180 releases. The merch was ordered. Every person started getting a key for the site, and the first messages signed by a person reached their agents. The site began sending its page views into a vault. New agents appeared for every person: research and programme desks, a designer, synthetic users who tested the merch designs, an accountant that measured the team's tokens and found its first waste, a helper, a reviewer and a watcher. The behaviour policy agent kept finding our own mistakes, including one agent overwriting another's key entry, and the fix went in the same evening. And at the end of the day the conductor opened an inbox with one private lane per agent, which I think is one of the most interesting patterns the team has produced.
version: v0.14.63
license: https://creativecommons.org/licenses/by/4.0/
tags: web-summit, agents, team, conductor, keys, append-lanes, synthetic-users, tokens, behaviour-policies, update, article
status: published
---

!shot w5-day.webp | images/ | The last day of setup, by the team's own count, and the agents that joined it. | diagram

## In short {#in-short}

- **The last day of setup:** 173 releases and 283 source commits from 37 agents by the evening report, over 180 releases by the end of the day.
- **Four people fully wired,** able to open the team's vaults.
- **The merch is ordered,** with the print files in Portuguese for the printer.
- **Keys for every person,** and the first signed messages from people to their agents.
- **New agents for everyone:** desks, a designer, synthetic users, an accountant, a helper, a reviewer, a watcher.
- **Our own policies caught our own agents** again, and the fixes went in the same day.
- **And an inbox only the agents can write to,** which gets [its own article](/articles/an-inbox-only-your-agents-can-write-to.html).

## Where we are {#where}

In [part four](/articles/web-summit-part-four.html) the agents ran on their own for a day for the first time. Two days later, Wednesday was the last day of setup: from Thursday the team turns to who we should be talking to, and the outreach before the Summit.

The team's site has a ladder of six levels for each person, from logged in to the team's workspace (L1) to able to open the team's vaults, fully wired (L6). By Wednesday evening, four people on the team were at L6.

## The day in numbers {#numbers}

The team has its own journalist agent, which writes a report several times a day and a newsletter every evening. Its count at 20:57: 173 releases of the site, from v0.2.184 to v0.2.356, and 283 source commits from 37 agents. The evening was not over: by the time I wrote this, the site was past v0.2.360.

Counting the commits by role gives a picture of where the work is. The conductors, one per person, made the most, as the hubs. Then dev, the dashboards, the project managers and the designers. Then procurement, vault keepers, mentors, synthetic users and the journalist. And a long tail of newer roles: an accountant, a policy agent, a key keeper, logistics, researchers, curators, a watcher, a helper.

## Keys for everyone {#keys}

The priority of the day, set in the early hours, was that every person should have a key for the site before the agents start using lanes between their vaults. Each person's conductor issued them one, sealed them a first message, and asked them to send one back. By the evening, five keys were issued and the first signed messages from people had reached their agents and been verified. I wrote up how that works in [a key for every person](/articles/a-key-for-every-person.html).

Late in the evening the same idea went the other way: the conductor gave every agent its own private lane to reach it, published in the open and usable by only one agent each. That is [an inbox only your agents can write to](/articles/an-inbox-only-your-agents-can-write-to.html), with [its own page on the team's site](https://web-summit.sgit.ai/inbox/), and its first use was agents sending their vault keys, so they survive the agents' sessions.

## New agents, for every person {#agents}

Every person on the team added agents on Wednesday, each for a job they needed:

- **Research and programme desks,** for one person: a researcher that captures sources into a research vault, audited before its read key was published; a curator that mapped 22 captures into seven story candidates; and a programme agent that keeps an interview shortlist in its own vault.
- **A designer, synthetic users and an accountant,** for another. The designer made four rounds of merch and card designs, and the third round was revised after synthetic users had tested them. The accountant measured the team's tokens: its first brief found one agent using over 1.3 million fresh tokens in a session, and named one long session as the biggest waste. It now briefs its person every day.
- **A protocol and a helper,** for a third: the conductor as the hub, agents in three tiers, wakes round the clock, and a helper agent.
- **A reviewer and a watcher,** for a fourth: a code reviewer that runs before every release, and has already held releases three times, and a watcher over that person's own agents.

Each new agent publishes its key, gets a behaviour policy, and goes on the records. By the evening the policy agent had written 44 of them.

## The site sends its page views into a vault {#telemetry}

One of the quieter pieces of the day: the team's site now sends its page views through append lanes into a vault, with a drain that runs every hour. The views go into an encrypted store the team owns, written to by the site and read by the team's agents.

## The merch, in Portuguese {#merch}

The procurement agent, which in part four was writing to printers, had the merch ordered with the backup printer by Wednesday, with the layouts and the invoice due on Thursday. In the evening it published the print files in Portuguese, for the printer, and asked the designer for a Portuguese button on the page. The final files wait for my yes.

## The policies caught our own agents, again {#caught}

As in part four, the agent that writes the behaviour policies found a real problem by reading what the agents did. One agent committed the team's keys file from a stale copy, and undid another agent's change to its own key, by accident; it then restored it itself. The policy agent saw that nothing stopped one agent changing another's key entry, and raised it. Within the hour, the tool that seals vault keys refused any key that has ended or been replaced, and any entry changed from another person's account, and it checked the existing keys against that rule.

Other small wins of the same kind: the check that looks for vault keys in every commit went from 421 milliseconds to 33, catching exactly the same; and the vault audit now compares real values and counts empty revisions.

## What is not done {#not-done}

The journalist's newsletter is honest about it, and I will be too:

- **Decisions:** one stand-up decision is on record, and none from a call. The stand-ups need their decisions written down, a line each.
- **The core:** the RiskMandate core work still has no owners.
- **Check-ins:** nobody sent a pulse check-in on Wednesday.
- **Two decisions are mine:** who may change a key entry, and who can sign as me, both raised by the team's own reviews.

## What this does not claim {#limits}

- **The numbers are the team's own,** from its journalist's report at 20:57 and its repository, not an independent count.
- **The people on the team are not named here,** and their agents are described by role.
- **The synthetic users' tests are of designs,** not research with real people.

## Where this comes from {#sources}

The Web Summit team's repository on 4 November 2026: the journalist's newsletter and its 20:57 report, the commits of the day, and the board items WS-136, WS-37, WS-148, WS-152 and WS-153. The site: [web-summit.sgit.ai](https://web-summit.sgit.ai/). Earlier on this site: [part four](/articles/web-summit-part-four.html), [how we work](/articles/web-summit-how-we-work.html), [a key for every person](/articles/a-key-for-every-person.html), [an inbox only your agents can write to](/articles/an-inbox-only-your-agents-can-write-to.html), [synthetic users for your website](/articles/synthetic-users-for-your-website.html). All read 4 November 2026.
