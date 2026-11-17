# Five primitives, one store: a reply to Andy Goundry on Anthropic's always-on agents guide, why the inbox, timers, memory, permissions and outbox can share one versioned, signed store, how every AgentiCCells cell will ship with all five, and the levels we have added on top, all in public repositories, sgit.ai

> Andy Goundry, CEO of Levantar, shared Anthropic's guide to building always-on agents on LinkedIn, with its five primitives, an event inbox, timers, memory, permissions and an outbox, and made a point I agree with completely: the model is one component, and the architecture around it is where the engineering, the cost and the risk live. He added that each primitive needs its own durable store, its own failure handling and its own tuning. That is where our experience differs, usefully. We run the same five primitives, and have since the ten days of Web Summit with around 250 agents, but they share one store: a versioned, signed, encrypted repository or vault. The inbox is append lanes, timers are scheduled wakes and a HOLD file read first, memory is REALITY.md, briefs and hand-overs, permissions are behaviour policies, keys and keyless agents behind a broker, and the outbox is drafts that a gateway or a person sends. One store gives durability, history, signatures and one audit trail for all five. I mapped them side by side with the guide yesterday; this is the reply, the mapping to AgentiCCells, where every cell is meant to ship with all five from the factory, and the levels we have added on top: many people, provenance, measured policies, a credential proxy built and measured, stopping as a file, a factory, and all of it open.

*Source: <https://newsroom.sgit.ai/articles/five-primitives-one-store.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Five primitives, one store: a reply to Andy Goundry on Anthropic's always-on agents guide, why the inbox, timers, memory, permissions and outbox can share one versioned, signed store, how every AgentiCCells cell will ship with all five, and the levels we have added on top, all in public repositories

# Five primitives, one store: a reply to Andy Goundry on Anthropic's always-on agents guide, why the inbox, timers, memory, permissions and outbox can share one versioned, signed store, how every AgentiCCells cell will ship with all five, and the levels we have added on top, all in public repositories

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-16 · [article v1.0.0](versions/five-primitives-one-store.md) · [newsroom v0.14.131](https://newsroom.sgit.ai/admin/versions.html) · agentsalways-on-agentsanthropicarchitectureagenticcellsabpopen-sourcearticle

***Abstract:** Andy Goundry, CEO of Levantar, shared Anthropic's guide to building always-on agents on LinkedIn, with its five primitives, an event inbox, timers, memory, permissions and an outbox, and made a point I agree with completely: the model is one component, and the architecture around it is where the engineering, the cost and the risk live. He added that each primitive needs its own durable store, its own failure handling and its own tuning. That is where our experience differs, usefully. We run the same five primitives, and have since the ten days of Web Summit with around 250 agents, but they share one store: a versioned, signed, encrypted repository or vault. The inbox is append lanes, timers are scheduled wakes and a HOLD file read first, memory is REALITY.md, briefs and hand-overs, permissions are behaviour policies, keys and keyless agents behind a broker, and the outbox is drafts that a gateway or a person sends. One store gives durability, history, signatures and one audit trail for all five. I mapped them side by side with the guide yesterday; this is the reply, the mapping to AgentiCCells, where every cell is meant to ship with all five from the factory, and the levels we have added on top: many people, provenance, measured policies, a credential proxy built and measured, stopping as a file, a factory, and all of it open.*

Five primitives, one store: inbox, timers, memory, permissions and outbox as folders in one versioned, signed store.

## In short

- **Andy Goundry is right:** the model is one component; the architecture around it is where the engineering, cost and risk live.
- **We run the same five primitives,** and did at Web Summit, with around 250 agents.
- **But in one store:** a versioned, signed, encrypted repository or vault, not a database per primitive.
- **Every AgentiCCells cell should ship with all five,** made by the factory.
- **We have added levels on top:** many people, provenance, measured policies, a credential proxy, stopping as a file, a factory.
- **All of it is open:** public repositories, Apache 2.0 code, CC BY text.

## The post

Andy Goundry, CEO and co-founder of Levantar, on Anthropic's always-on agents guide, LinkedIn, November 2026.

Andy Goundry, CEO and co-founder of Levantar, shared Anthropic's guide, [Building always-on agents](https://claude.com/resources/articles/building-always-on-agents), by William Hu, published on 13 November, and summarised its five primitives: an event inbox, timers, memory, permissions and an outbox. Then he made the point that matters: "the model itself is one component." The architecture around it, the event handling, the state and the permission layers, is where the real engineering lives, and, in his words, "it's where the cost and risk live too."

I agree completely, and it matches what we see. I set the guide beside what we ran at Web Summit yesterday ([always-on agents at team scale](always-on-agents-at-team-scale.md)): I recognised every box. So this is a reply to one line of Andy's in particular, because it is where our experience adds something: "Each primitive needs its own durable store, its own failure handling, its own tuning."

## One store, not five

In the guide, the inbox is a database table, timers live in their own durable store, memory maps to a database or object store, and the outbox is another table with a dispatcher. That is a sound design, and it is five things to build, back up, monitor and secure.

Ours are five folders in one store: a git repository, or an encrypted vault that behaves like one ([how a vault works](how-a-vault-works.md)).

- **Event inbox:** append lanes. Anyone with a lane's key can add to it; only the agent it belongs to can read it, because each lane's token is sealed to that agent's own key ([an inbox only your agents can write to](an-inbox-only-your-agents-can-write-to.md)). Commits on the team's board, addressed to a conductor, are the other door in.
- **Timers:** scheduled wakes and one-shot follow-ups. Each wake starts by reading the same files, and first of all a HOLD file, which is how we stop them ([stopping a hundred agents](stopping-a-hundred-agents.md)).
- **Memory:** REALITY.md, which lists only what exists; briefs; ledgers; and a hand-over file for the next session. The guide's rule, keep only what the agent cannot look up again, is ours too: pointers to sources, not copies.
- **Permissions:** a behaviour policy per agent, saying what it has been granted, what it was asked to do, the gap between the two, and what stands in its way; a key per agent; and agents that hold no credential at all behind a broker that applies only signed, approved plans ([where assist becomes execute](where-assist-becomes-execute.md)).
- **Outbox:** agents draft, into a folder or a lane; a gateway sends, or a person does. At Web Summit, outreach to target companies was drafted by agents and sent, if at all, by a person ([the email agentic cell](the-email-agentic-cell.md)).

And one store gives all five the same properties at once: durable, because it is git; versioned, so every change is kept; attributed, every commit naming the agent and the person it works for, and signed where it matters; encrypted, in a vault, so the server learns nothing; replayable, so a new worker, a new session or a reviewer reads exactly the same history. One audit trail, one backup, one failure model. The cost Andy rightly worries about falls, because the hard parts are paid for once.

## Mapped to AgentiCCells

Every AgentiCCells cell ships with the five primitives, plus the factory that creates it from one commit.

AgentiCCells is built around the cell: one focused job, with an objective, a deliverable and a behaviour policy ([the cell is the unit](the-cell-is-the-unit.md)). The five primitives are exactly the parts a cell needs, so every cell should ship with all five: an inbox lane per sender, a schedule of wakes, a vault and a REALITY.md for memory, a behaviour policy and keys, and an outbox where agents draft and a gateway or a person sends. The sixth part is the factory, which creates the repository, the DNS entry, the site and the pipeline from one commit, in about a minute ([the site factory works](the-site-factory-works.md)). Tonight it made two people's websites in an evening ([a website that is her](a-website-that-is-her.md)).

## The levels we have added

Beyond one agent per user: seven levels we have added, each running, in public repositories.

The guide designs for one inbox per user, which is the right place to start. A team of people and agents meets more, and these are the levels we have added, each one running:

- **Many agents, many people:** around 250 named agents, six people, more than 60 at once ([ten days at Web Summit](ten-days-at-web-summit.md)).
- **Provenance:** every commit names the agent and the person it works for, and a person's key vouches for their agents ([a key for every person](a-key-for-every-person.md)).
- **Policies you can measure:** behaviour policies as data, with the grant measured from the system itself; on Odoo, by a module that turns its access rules into policy rows ([our workflow on Odoo 20](our-workflow-on-odoo-20.md)).
- **A credential proxy, built and measured:** the guide's recommended pattern. Our Odoo bills agent held no Odoo credential; a policy check allowed two of five proposals; a signed approval and a narrow broker applied only those. That is also the guide's deferred tool call, with the approval as a signed object.
- **Stopping as a file:** HOLD files that every wake reads first, and pause, never delete.
- **A factory for cells:** a commit becomes a live, governed cell in minutes.
- **Open, all of it:** the repositories are public, the code is Apache 2.0, the text is CC BY 4.0, and the rules our agents follow are published.

## What we would add to the guide

Three things, offered in the guide's own spirit:

1. **Make the store the same for all five,** if you can, and make it versioned: most of the failure handling then comes from replaying history.
2. **Put the stop in a file the wake reads first,** before the inbox: a team of always-on agents needs a brake that does not wait for the next event.
3. **Let the approval be signed,** so that a deferred tool call, once answered, is evidence of who allowed what, not just a resumed session.

## What this does not claim

- **Not that ours is better:** the guide is a clean design for one agent per user; ours grew from git and vaults for a team.
- **The cell format with all five is the target;** today the parts exist across our repositories, not yet as one template.
- **Signing varies by repository:** every commit names its agent and person; cryptographic signatures are used where the stakes need them.
- **Andy's views are his own;** I quote only his post.

## Where this comes from

Andy Goundry's LinkedIn post, read on 16 November 2026, and the guide it shares: William Hu, [Building always-on agents](https://claude.com/resources/articles/building-always-on-agents), Anthropic, 13 November 2026, read the same day. Our own records, as published on this site: [always-on agents at team scale](always-on-agents-at-team-scale.md), [an inbox only your agents can write to](an-inbox-only-your-agents-can-write-to.md), [stopping a hundred agents](stopping-a-hundred-agents.md), [how a vault works](how-a-vault-works.md), [where assist becomes execute](where-assist-becomes-execute.md), [the email agentic cell](the-email-agentic-cell.md), [the cell is the unit](the-cell-is-the-unit.md), [the site factory works](the-site-factory-works.md), [a website that is her](a-website-that-is-her.md), [ten days at Web Summit](ten-days-at-web-summit.md), [a key for every person](a-key-for-every-person.md), [our workflow on Odoo 20](our-workflow-on-odoo-20.md).

## Threads

Agents & policySite & engineering[This article as a graph →](graphs.md#five-primitives-one-store)

### Builds on

- [Always-on agents at team scale: Anthropic's five primitives for an agent that sleeps and wakes, set beside the around 250 named agents six of us ran at Web Summit, and the next problems once there are many](always-on-agents-at-team-scale.md) Anthropic's five primitives for always-on agents, set beside the around 250 named agents six of us ran at Web Summit, and the next problems once there are many.
- [How a vault works: an encrypted store that acts like a database, where a server that is fully compromised leaks nothing, one mutable file lets every other object be cached for ever, and a web page can open a file in four requests or run a whole app in a sandbox](how-a-vault-works.md) How an sgit vault acts like a database on a server that cannot read: one key-derived mutable file, everything else immutable.
- [An inbox only your agents can write to: a conductor publishes one append lane per agent, each lane's token sealed to that agent's own key, so everything needed to talk privately is public and only the right agent can use it](an-inbox-only-your-agents-can-write-to.md) A conductor publishes one append lane per agent, each token sealed to that agent's key: a private channel built from public material.
- [Stopping a hundred agents: the Big Stop, the hand brake and the final hold at Web Summit, why pausing took seconds but hearing the order took up to an hour, what kept running anyway, and why a stop has to be a file every agent reads first](stopping-a-hundred-agents.md) Stopping a hundred agents at Web Summit: pausing took seconds, hearing the order took up to an hour, and a stop has to be a file every agent reads first.
- [Where assist becomes execute: tiering AI agents by what they can reach and whether it can be undone, how Agent Behaviour Policies drew that line for more than a hundred agents at Web Summit, and the rule that failed because it was only a rule](where-assist-becomes-execute.md) Where assist becomes execute: tier AI agents by reach and undo class, enforce each tier with a boundary, and learn from the rule that failed.
- [The email agentic cell: why connecting Gmail to agents the usual way is a security mess, and the architecture we will build instead, with one gateway agent that alone touches Gmail, a digital twin of the mailbox in a vault that people and agents work on together, signed proposals, approvals and even reads on append lanes, and behaviour policies at five altitudes](the-email-agentic-cell.md) Our own email connector: one gateway agent touches Gmail, everyone else works on a signed twin of the mailbox in a vault, with policies at five altitudes.
- [The cell is the unit: positioning AgentiCCells around small, focused cells, each with an objective, a deliverable and a behaviour policy, each with a page that sells it, a free recipe and three ways to get help, a catalogue that grows one need at a time, in each industry's own words, and why we should run our own work in cells first](the-cell-is-the-unit.md) The cell is the unit of AgentiCCells: one focused job with an objective, a deliverable and a behaviour policy, each with a page that sells it.
- [The site factory works: three AgentiCCells sites made by hand, then one made by a commit in two minutes and thirty-nine seconds, live over https with a first version written by Claude Code, and the long list of what it took to make something that hard look easy](the-site-factory-works.md) Three AgentiCCells sites by hand, then one by a commit: live over https in 87 seconds, a first version by Claude Code at 159.
- [A website that is her: how Yiheng Wang's site was made in three passes in one evening, by the site factory, five design agents and then her own agent, with five designs, a kitchen brigade of 26 agents, a printable brief and a page for your AI, and why every claim on it is something she can talk about because she did it](a-website-that-is-her.md) Yiheng Wang's website, made in one evening by the site factory, five design agents and her own agent: five designs, every claim sourced, all of it her.
- [Ten days at Web Summit: what six people and around 250 agents built between 3 and 13 November, in order, and the series of articles that will tell each part](ten-days-at-web-summit.md) Six people and around 250 agents, ten days at Web Summit: what we built, in order, and the series that will tell it.
- [A key for every person: how each person's conductor issues them a key for the team's site, seals what is for them, and how a signed message turns the public web into a channel the agents can trust](a-key-for-every-person.md) How each person's conductor issues them a key for the team's site: sealed to you, signed by you, and a lane the agents can trust.
- [Our workflow on Odoo 20, built and measured: a bills agent with no Odoo credential, a policy check that allowed two proposals and stopped three, a signed approval, a narrow broker, a grant measured from Odoo itself by a new module, and what Odoo's default user role quietly allows](our-workflow-on-odoo-20.md) Our workflow on Odoo 20, built in 98 seconds: a keyless agent, a policy check, a signed approval, a narrow broker and a grant measured from Odoo.

### Continued by

- [Build on VoiceDebrief: the techniques from our iPhone and iPad voice app that any team can take into its own, from recording without loss and transcribing offline on the device to debriefs by Apple Intelligence, controlling an app by voice, three layers of intelligence and a CI pipeline that lets agents build a native app without a Mac, with a prompt to point your own Claude at the code](build-on-voicedebrief.md) VoiceDebrief's techniques for any voice app: record without loss, transcribe offline, debrief with Apple Intelligence, voice control, CI.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 442 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=442)

**Posting this article on LinkedIn?** The cover is [five-primitives-one-store.jpg](banners/five-primitives-one-store.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/five-primitives-one-store.html)*
