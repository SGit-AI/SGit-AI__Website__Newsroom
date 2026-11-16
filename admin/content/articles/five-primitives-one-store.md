---
title: Five primitives, one store: a reply to Andy Goundry on Anthropic's always-on agents guide, why the inbox, timers, memory, permissions and outbox can share one versioned, signed store, how every AgentiCCells cell will ship with all five, and the levels we have added on top, all in public repositories
date: 2026-11-16
author: Dinis Cruz
author_url: about/index.html
summary: Andy Goundry, CEO of Levantar, shared Anthropic's guide to building always-on agents on LinkedIn, with its five primitives, an event inbox, timers, memory, permissions and an outbox, and made a point I agree with completely: the model is one component, and the architecture around it is where the engineering, the cost and the risk live. He added that each primitive needs its own durable store, its own failure handling and its own tuning. That is where our experience differs, usefully. We run the same five primitives, and have since the ten days of Web Summit with around 250 agents, but they share one store: a versioned, signed, encrypted repository or vault. The inbox is append lanes, timers are scheduled wakes and a HOLD file read first, memory is REALITY.md, briefs and hand-overs, permissions are behaviour policies, keys and keyless agents behind a broker, and the outbox is drafts that a gateway or a person sends. One store gives durability, history, signatures and one audit trail for all five. I mapped them side by side with the guide yesterday; this is the reply, the mapping to AgentiCCells, where every cell is meant to ship with all five from the factory, and the levels we have added on top: many people, provenance, measured policies, a credential proxy built and measured, stopping as a file, a factory, and all of it open.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: agents, always-on-agents, anthropic, architecture, agenticcells, abp, open-source, article
status: published
---

!shot lev-one-store.webp | images/ | Five primitives, one store: inbox, timers, memory, permissions and outbox as folders in one versioned, signed store. | concept

## In short {#in-short}

- **Andy Goundry is right:** the model is one component; the architecture around it is where the engineering, cost and risk live.
- **We run the same five primitives,** and did at Web Summit, with around 250 agents.
- **But in one store:** a versioned, signed, encrypted repository or vault, not a database per primitive.
- **Every AgentiCCells cell should ship with all five,** made by the factory.
- **We have added levels on top:** many people, provenance, measured policies, a credential proxy, stopping as a file, a factory.
- **All of it is open:** public repositories, Apache 2.0 code, CC BY text.

## The post {#post}

!shot lev-question.webp | images/ | Andy Goundry, CEO and co-founder of Levantar, on Anthropic's always-on agents guide, LinkedIn, November 2026. | medium | aside

Andy Goundry, CEO and co-founder of Levantar, shared Anthropic's guide, [Building always-on agents](https://claude.com/resources/articles/building-always-on-agents), by William Hu, published on 13 November, and summarised its five primitives: an event inbox, timers, memory, permissions and an outbox. Then he made the point that matters: "the model itself is one component." The architecture around it, the event handling, the state and the permission layers, is where the real engineering lives, and, in his words, "it's where the cost and risk live too."

I agree completely, and it matches what we see. I set the guide beside what we ran at Web Summit yesterday ([always-on agents at team scale](/articles/always-on-agents-at-team-scale.html)): I recognised every box. So this is a reply to one line of Andy's in particular, because it is where our experience adds something: "Each primitive needs its own durable store, its own failure handling, its own tuning."

## One store, not five {#one-store}

In the guide, the inbox is a database table, timers live in their own durable store, memory maps to a database or object store, and the outbox is another table with a dispatcher. That is a sound design, and it is five things to build, back up, monitor and secure.

Ours are five folders in one store: a git repository, or an encrypted vault that behaves like one ([how a vault works](/articles/how-a-vault-works.html)).

- **Event inbox:** append lanes. Anyone with a lane's key can add to it; only the agent it belongs to can read it, because each lane's token is sealed to that agent's own key ([an inbox only your agents can write to](/articles/an-inbox-only-your-agents-can-write-to.html)). Commits on the team's board, addressed to a conductor, are the other door in.
- **Timers:** scheduled wakes and one-shot follow-ups. Each wake starts by reading the same files, and first of all a HOLD file, which is how we stop them ([stopping a hundred agents](/articles/stopping-a-hundred-agents.html)).
- **Memory:** REALITY.md, which lists only what exists; briefs; ledgers; and a hand-over file for the next session. The guide's rule, keep only what the agent cannot look up again, is ours too: pointers to sources, not copies.
- **Permissions:** a behaviour policy per agent, saying what it has been granted, what it was asked to do, the gap between the two, and what stands in its way; a key per agent; and agents that hold no credential at all behind a broker that applies only signed, approved plans ([where assist becomes execute](/articles/where-assist-becomes-execute.html)).
- **Outbox:** agents draft, into a folder or a lane; a gateway sends, or a person does. At Web Summit, outreach to target companies was drafted by agents and sent, if at all, by a person ([the email agentic cell](/articles/the-email-agentic-cell.html)).

And one store gives all five the same properties at once: durable, because it is git; versioned, so every change is kept; attributed, every commit naming the agent and the person it works for, and signed where it matters; encrypted, in a vault, so the server learns nothing; replayable, so a new worker, a new session or a reviewer reads exactly the same history. One audit trail, one backup, one failure model. The cost Andy rightly worries about falls, because the hard parts are paid for once.

## Mapped to AgentiCCells {#cells}

!shot lev-cell.webp | images/ | Every AgentiCCells cell ships with the five primitives, plus the factory that creates it from one commit. | concept

AgentiCCells is built around the cell: one focused job, with an objective, a deliverable and a behaviour policy ([the cell is the unit](/articles/the-cell-is-the-unit.html)). The five primitives are exactly the parts a cell needs, so every cell should ship with all five: an inbox lane per sender, a schedule of wakes, a vault and a REALITY.md for memory, a behaviour policy and keys, and an outbox where agents draft and a gateway or a person sends. The sixth part is the factory, which creates the repository, the DNS entry, the site and the pipeline from one commit, in about a minute ([the site factory works](/articles/the-site-factory-works.html)). Tonight it made two people's websites in an evening ([a website that is her](/articles/a-website-that-is-her.html)).

## The levels we have added {#levels}

!shot lev-levels.webp | images/ | Beyond one agent per user: seven levels we have added, each running, in public repositories. | concept

The guide designs for one inbox per user, which is the right place to start. A team of people and agents meets more, and these are the levels we have added, each one running:

- **Many agents, many people:** around 250 named agents, six people, more than 60 at once ([ten days at Web Summit](/articles/ten-days-at-web-summit.html)).
- **Provenance:** every commit names the agent and the person it works for, and a person's key vouches for their agents ([a key for every person](/articles/a-key-for-every-person.html)).
- **Policies you can measure:** behaviour policies as data, with the grant measured from the system itself; on Odoo, by a module that turns its access rules into policy rows ([our workflow on Odoo 20](/articles/our-workflow-on-odoo-20.html)).
- **A credential proxy, built and measured:** the guide's recommended pattern. Our Odoo bills agent held no Odoo credential; a policy check allowed two of five proposals; a signed approval and a narrow broker applied only those. That is also the guide's deferred tool call, with the approval as a signed object.
- **Stopping as a file:** HOLD files that every wake reads first, and pause, never delete.
- **A factory for cells:** a commit becomes a live, governed cell in minutes.
- **Open, all of it:** the repositories are public, the code is Apache 2.0, the text is CC BY 4.0, and the rules our agents follow are published.

## What we would add to the guide {#add}

Three things, offered in the guide's own spirit:

1. **Make the store the same for all five,** if you can, and make it versioned: most of the failure handling then comes from replaying history.
2. **Put the stop in a file the wake reads first,** before the inbox: a team of always-on agents needs a brake that does not wait for the next event.
3. **Let the approval be signed,** so that a deferred tool call, once answered, is evidence of who allowed what, not just a resumed session.

## What this does not claim {#limits}

- **Not that ours is better:** the guide is a clean design for one agent per user; ours grew from git and vaults for a team.
- **The cell format with all five is the target;** today the parts exist across our repositories, not yet as one template.
- **Signing varies by repository:** every commit names its agent and person; cryptographic signatures are used where the stakes need them.
- **Andy's views are his own;** I quote only his post.

## Where this comes from {#sources}

Andy Goundry's LinkedIn post, read on 16 November 2026, and the guide it shares: William Hu, [Building always-on agents](https://claude.com/resources/articles/building-always-on-agents), Anthropic, 13 November 2026, read the same day. Our own records, as published on this site: [always-on agents at team scale](/articles/always-on-agents-at-team-scale.html), [an inbox only your agents can write to](/articles/an-inbox-only-your-agents-can-write-to.html), [stopping a hundred agents](/articles/stopping-a-hundred-agents.html), [how a vault works](/articles/how-a-vault-works.html), [where assist becomes execute](/articles/where-assist-becomes-execute.html), [the email agentic cell](/articles/the-email-agentic-cell.html), [the cell is the unit](/articles/the-cell-is-the-unit.html), [the site factory works](/articles/the-site-factory-works.html), [a website that is her](/articles/a-website-that-is-her.html), [ten days at Web Summit](/articles/ten-days-at-web-summit.html), [a key for every person](/articles/a-key-for-every-person.html), [our workflow on Odoo 20](/articles/our-workflow-on-odoo-20.html).
