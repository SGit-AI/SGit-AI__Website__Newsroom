# Agentic cost is an engineering problem: a business plan for a service that reads the logs a company already has and finds the money, then the engineering, sgit.ai

> A business plan, written to be handed to someone who wants to build it or to collaborate on it. The service helps companies manage the cost of agentic AI, and it starts from a claim this site has made before: cost is an engineering problem. An agent estate whose bill nobody can explain is an estate that shipped from the explorer side without the villager's discipline, and the Wardley map says so: prompts and workflows grown in sessions, running in production on commodity model APIs, with logs, traces and invoices that exist and are never read together, and no one who owns the cost. The service installs nothing. It reads what is already there, draws the footprint of every agent, builds a digital twin of the estate, writes the behaviour policy each agent was in fact running under, and maps cost and capability into one graph. The findings are two lists: what to stop paying for, which pays for the engagement, and what to build, which is the reason to have it: the places of attrition, the gaps, the workflow three teams rebuilt, the policy that would end a loop. The gaps are findings too: a company that cannot provide the data has learned the first one. Vaults carry the data in, the transformations as commits, and anonymised extracts out as sealed envelopes. Four price levels on the RiskMandate pattern, every number a labelled assumption.

*Source: <https://newsroom.sgit.ai/articles/agentic-cost-is-an-engineering-problem.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Agentic cost is an engineering problem: a business plan for a service that reads the logs a company already has and finds the money, then the engineering

# Agentic cost is an engineering problem: a business plan for a service that reads the logs a company already has and finds the money, then the engineering

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-12 · [article v1.1.0, 2 versions](versions/agentic-cost-is-an-engineering-problem.md) · [sgit.ai v0.7.74](https://sgit.ai/admin/versions.md) · business-planagentic-aicostwardley-mapsexplorer-villageragent-behaviour-policydigital-twinlogsvaultsriskmandatestartupsarticle

***Abstract:** A business plan, written to be handed to someone who wants to build it or to collaborate on it. The service helps companies manage the cost of agentic AI, and it starts from a claim this site has made before: cost is an engineering problem. An agent estate whose bill nobody can explain is an estate that shipped from the explorer side without the villager's discipline, and the Wardley map says so: prompts and workflows grown in sessions, running in production on commodity model APIs, with logs, traces and invoices that exist and are never read together, and no one who owns the cost. The service installs nothing. It reads what is already there, draws the footprint of every agent, builds a digital twin of the estate, writes the behaviour policy each agent was in fact running under, and maps cost and capability into one graph. The findings are two lists: what to stop paying for, which pays for the engagement, and what to build, which is the reason to have it: the places of attrition, the gaps, the workflow three teams rebuilt, the policy that would end a loop. The gaps are findings too: a company that cannot provide the data has learned the first one. Vaults carry the data in, the transformations as commits, and anonymised extracts out as sealed envelopes. Four price levels on the RiskMandate pattern, every number a labelled assumption.*

The map in three frames: the problem as most companies have it, what the service adds from what is already there, and where it goes. Agents in production on the explorer side, billed by the token, with logs nobody reads together; then the footprint, the twin, the policy and the graph; then cost as a discipline.

The 3 frames, one image each: [1](images/ac-wardley-1.webp) [2](images/ac-wardley-2.webp) [3](images/ac-wardley-3.webp).

This is a business plan, of the kind this site has published before: [Agent Desk](an-agent-desktop-by-the-minute.md), [Connector Twin](connector-twin-before-you-deploy-an-agent.md) and the others on the [business plans page](https://sgit.ai/startups/business-plans.md). It is written to be handed to someone, and the someone is whoever wants to build it, or build it with me. The service is simple to say: help companies manage the cost of agentic AI, by observing what is already happening.

The reason I think it is a business, and not a consulting engagement, is that the inputs already exist in every company that has put agents into production, nobody is reading them together, and the two things that come out of reading them, a shorter bill and a map of what to build, are both things companies pay for.

## In short

- **Cost is an engineering problem.** When the bill for agents cannot be explained, it is not because models are expensive. It is because the estate shipped from the explorer side, prompts and workflows grown in sessions, without the discipline production needs: a policy, a twin, an owner, a cap. The Wardley map shows the shape.
- **The logs already tell the story.** Model and gateway invoices by key and day; the traces agents write; the prompts and schedules as they are. Read together, they give every agent a footprint, and a footprint is most of a policy.
- **The service installs nothing.** The customer drops what they have into a vault; the service reads it; the customer gets the twin, the policies and two lists.
- **Two lists, in this order.** The cost list: loops disguised as retries, whole context sent every call, big models where small ones answer, schedules nobody reads, keys with no ceiling. The engineering list: the workflow three teams rebuilt, the policy that would end the loop, the twin that would make the next incident replayable, the prompt that should be a component.
- **The gaps are findings.** The less data a company can provide, the more it has learned already: an agent with no logs has no footprint, no owner and no policy.
- **Vaults carry it.** Data in, encrypted to the service's key in a vault the customer owns; every transformation a commit, so the chain from invoice to finding is walkable; anonymised extracts out as sealed envelopes to a benchmark vault, seen by the customer before they go.
- **Four price levels**, on the RiskMandate pattern, and a share-of-savings option. Every number is a labelled assumption.

## The problem, on a map

The problem. The person who pays the bill sees a total. Below it, agents in production built from prompts and workflows grown in sessions, on commodity model APIs metered by the token, with logs, traces and invoices that exist and are never read together, and no one who owns the cost.

Take any company that has agents doing real work: reading a mailbox, running a schedule, answering customers, writing code. Draw the value chain with the person who pays the bill at the top. Under them, the agents. Under the agents, where did they come from? Almost always from a session: someone built a prompt that worked, wrapped it in a workflow, and it went to production because it worked. That is the explorer side of the map, genesis and custom-built, and it is the right place to build something new. It is the wrong place to run something at scale, and [the newsroom's move from explorer to villager](explorer-to-villager-newsroom.md) is this site's own worked example of what the move involves.

Meanwhile the things the agents run on are at the far right: model APIs, token metering, cloud compute, all commodities, all billed by use, and billed well, which is the irony. The invoice is exact. The logs are complete. The traces exist because the platforms write them whether anyone asked or not. And nobody reads them together, because the agents came from the explorer side where nobody needed to, and the one node on the map that should connect the bill to the agents, an owner of cost, is missing.

That is why [cost is an engineering problem](knowing-when-to-stop.md), in the sense that article meant it about security: not a thing you fix by negotiating a discount, but a class of defect with a cause, a fix and a test. An agent that retries in a loop is a bug. A workflow that sends its whole context on every call is a bug. A key with no ceiling is a missing control. These are the things engineers fix once they can see them, and the service exists to make them visible.

## What the service does

Observe, map, find: the three steps, the two lists, how it makes money, why vaults, and the positive frame. Every price is a labelled assumption.What the service adds, from what is already there. The footprint read from the logs; the twin of the estate; the behaviour policy each agent was in fact running under; and the cost and capability graph that produces the findings. Nothing is installed in the customer's estate.

**Observe.** No agent is installed and nothing in the customer's environment is changed. The customer drops into a vault what they already have: model and gateway invoices by key and by day; the logs and traces their agents write; the prompts, workflow files and schedules as they are; and whatever they know about who owns which agent. The vault is theirs; the contents are sealed to the service's key, as [RFC 0001](rfc-0001-public-key-cryptography-for-sgit.md) describes.

**Map.** Three things are built from that, and they are the three things this site has been arguing for all along, applied to cost.

- **The footprint** of every agent: what it actually did, read from the logs. Calls, tokens, tools, retries, loops, hours of the day, which data it touched. This is the [footprint](footprint-and-blast-radius.md) that article proposed as the after-the-fact twin of a mandate, with nobody inline and no production access needed, and here it is the first thing the money attaches to.
- **The twin** of the estate: a graph of agents, models, keys, tools, data, owners and schedules, with a cost on every edge. It is a digital twin in the plain sense: a representation of what is running that can be queried, compared with the invoice, and followed. The [connector twin](connector-twin-before-you-deploy-an-agent.md) is one component of it; this is the whole estate.
- **The policy** each agent was in fact running under. Not the one somebody wrote, if anybody did, but the one the footprint reveals: what it reached, what it did with what it reached, where it stopped and where it did not. Written as an [Agent Behaviour Policy](the-behaviour-policy-is-the-business-logic.md), with the enforcement column filled honestly, so that the rows that say "told" are visible, because that is where both the cost and the risk are. Where the cost is large, the policy will be large, and that is the intersection this plan sits on.

And the gaps: where there is no log, no owner, no policy, no cap. These go on the map as findings, not as missing data.

**Find.** Two lists, in this order. The cost list first, because it pays for the engagement: retries that are loops; context sent whole on every call when a graph would send a slice, which [The agent is the reader](the-agent-is-the-reader.md) measured at ninety per cent less; the large model used where a smaller one answers the same; agents on schedules whose output nobody reads; keys with no ceiling. Then the engineering list, which is the reason to have the engagement at all: the workflow three teams built separately; the policy that would end the loop for good; the twin that would make the next incident replayable; the thing that should be a component and is a prompt that every session has to remember, which is the argument of [Every mistake added a rule](every-mistake-added-a-rule.md).

## Why the positive frame matters

A cost review is a thing companies buy once and resent. A map of what to build is a thing they come back for. The difference is the frame, and it is not a sales trick; it is what the data supports. The same logs that show an agent looping show the workflow it was trying to run, and the workflow is usually worth more than the loop costs. The same twin that shows three teams calling the same model with the same prompt shows the component they should share. The places of attrition, where an agent gives up, retries, or hands off to a person, are the places where a policy and a component would change what the company can do, not only what it spends.

So the service sells cost reduction, and delivers engineering opportunity, and the business model follows the second. That is also why the gaps are findings rather than obstacles. A company that cannot produce a log for an agent has an agent nobody is watching; a company with no owner for a key has a key that will be the next incident; a company whose prompts live only in a session has no way to know what its agents are doing. Not being able to do the analysis is the first result of the analysis, and it is the one most companies need first.

## Why vaults

The plan is specific about vaults because they fit this job unusually well, and because the latest capabilities make the fit better.

- **Capture.** The customer's logs go into a vault once, encrypted in their browser or on their machine, in a vault they own and can revoke. The service holds a read key to that vault and nothing else.
- **Transform.** Every step from invoice to finding is a commit: the parsed logs, the footprints, the twin, the policies, the lists. The chain is walkable, so a finding can be followed back to the lines it rests on, which is the same provenance rule the [newsroom](the-article-remains-a-product.md) runs on.
- **Move.** The twin is a vault of its own, and a read key opens exactly one customer's estate to exactly one analyst or agent. Anonymised extracts, the shape of a loop, the ratio of context to answer, the distribution of cost by agent type, can leave as [sealed envelopes](rfc-0001-public-key-cryptography-for-sgit.md) to a benchmark vault, and the customer sees the extract before it goes. Over time that vault is the thing that lets the service say "companies like yours spend this much on this", which is the second business.

## How it makes money

Four levels, on the pattern RiskMandate uses, and one alternative.

| Level | What | Price |
|---|---|---|
| **Kit** | The log formats, the twin schema, the policy template and the scripts, to run yourself | £50 |
| **Your cost vault** | The customer runs the catalogue of analyses on their own logs, in their own vault | £250 |
| **Standard** | One estate read: the twin, the policies, both lists, a one-page board summary, within ten working days | £3,000 |
| **Tailored** | Standard, plus the engineering list worked through with the team, and a re-read when the bill moves | from £9,000 |
| **Share of savings** | Where a customer prefers it: a share of the first year's reduction, measured from the invoices | an assumption |

About eight Standard and two Tailored a month cover a two-founder burn, on the same arithmetic as [Company X-Ray](https://sgit.ai/startups/business-plans.md). Every number is a labelled assumption, and the calculator belongs in the plan vault when it is made.

## What is already here, and what is not

What exists on this site, and in the agents that run it: the footprint method, the behaviour policy format with its enforcement column, the connector twin design, the vault tooling for capture, transform and move, the sealed envelopes, and the Company X-Ray pattern of reading a company's own documents in a vault and returning findings in five days. What does not exist: the catalogue of cost analyses, the twin schema for an agent estate, the log parsers for the common platforms, the benchmark vault, a single customer. That is the work, and it is a few weeks of it, which is why I am writing the plan rather than keeping it.

## What this does not claim

- **No customer has been read.** The method is assembled from pieces that run elsewhere; the cost list and the engineering list are what I expect to find, not what has been found.
- **The prices are assumptions.** Labelled as such, on the pattern of the other plans here, and to be tested against the first three customers.
- **The map is a sketch.** Wardley maps are arguments, not measurements; this one says where I think the problem sits and why.
- **Share of savings is hard to measure honestly.** It needs a baseline from the invoices and an agreed way to attribute a reduction; the plan should say how before anyone signs it.

If you want to build this, or you run agents in production and would like to be the first estate read, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 12 October 2026, after a conversation with someone I may collaborate with; they are not named. Written by this site's agent in the voice of this site. The argument and the editorial responsibility are mine. The plan rests on earlier work here: the footprint in [Footprint and blast radius](footprint-and-blast-radius.md), the policy in [The behaviour policy is the business logic](the-behaviour-policy-is-the-business-logic.md), the twin in [Connector Twin](connector-twin-before-you-deploy-an-agent.md), the explorer-to-villager move in [the newsroom's own case](explorer-to-villager-newsroom.md), the context measurement in [The agent is the reader](the-agent-is-the-reader.md), the component argument in [Every mistake added a rule](every-mistake-added-a-rule.md), the vault cryptography in [RFC 0001](rfc-0001-public-key-cryptography-for-sgit.md), and the pricing pattern of the plans on the [business plans page](https://sgit.ai/startups/business-plans.md). The Wardley maps and the plan figure were drawn for this article. Related: [Knowing when to stop](knowing-when-to-stop.md), [An agent desktop by the minute](an-agent-desktop-by-the-minute.md) and [The article remains a product](the-article-remains-a-product.md).

## Threads

Startups & strategyAgents & policyVaults & method[This article as a graph →](graphs.md#agentic-cost-is-an-engineering-problem)

### Builds on

- [A locked-down desktop for an agent, by the minute, is still hard to rent](an-agent-desktop-by-the-minute.md) Nine properties a safe agent desktop needs, nine products against them, the macOS day-long lease, and the startup credits that would pay for testing it.
- [Before you give an agent a connector, give the connector a twin](connector-twin-before-you-deploy-an-agent.md) An agent with a Gmail or Calendar connector can do things the platform cannot undo; a journal of every call, replayed, shows what it did and what can go back.
- [Go slow to go fast: moving the newsroom from an explorer project to a villager one, with the brief to do it](explorer-to-villager-newsroom.md) The newsroom is live and charging. Move the reader code to its own repo, same bytes and same bugs, then map, test, review and refactor before new features.
- [Knowing when to stop: what experience gives people, and what we have to design into agents](knowing-when-to-stop.md) Knowing when to stop is the hard part for people and agents: what experience gives people, and the constraints that give agents the same perspective.
- [RFC 0001: two ways to add public-key cryptography to sgit, and the questions we want you to answer](rfc-0001-public-key-cryptography-for-sgit.md) A Request for Comments: two key pairs so a reader cannot write, sealed files only named people can open, and fourteen questions for reviewers.
- [Footprint and blast radius: what the agent actually did, and what it would have cost](footprint-and-blast-radius.md) Footprint is what an agent actually did, read afterwards from logs and vault history; blast radius is what a row of its reach would cost the business today.
- [Zoom into an agent's behaviour policy and you find the business logic](the-behaviour-policy-is-the-business-logic.md) Below the first rules, an agent's behaviour policy is the business: functions, processes, clients, values. Layered, owned, counted, and where vendors plug in.
- [The agent is the reader: why agents will pay for graphs, personas and signed claims, because it is cheaper than not paying](the-agent-is-the-reader.md) Agents pay to read the raw web and guess its meaning. A curated graph answers for 90% fewer tokens, so paying the publisher is cheaper than not paying.
- [Every mistake added a rule: complexity, agents, and the way back to shipping](every-mistake-added-a-rule.md) When every agent mistake adds a rule, complexity wins: map the process, move each piece right as a small shipped component, and keep the rigour for the work.
- [The article remains a product: Jonathan Palmer's four outputs for a newsroom with no human readers, checked against one that runs](the-article-remains-a-product.md) Jonathan Palmer's four outputs for a newsroom with no human readers, quoted line by line and checked against newsroom.sgit.ai as it runs, screenshots included.

### Continued by

- [Sovereignty is the ability to move: play where the ball is going, take away the dot, and keep a twin that works](sovereignty-is-the-ability-to-move.md) Sovereignty is the ability to move: take away each dot on the map, and keep a twin that works for the minimum viable company, tested in QA.
- [Move the cloud, not the code: twins, sovereignty that works in practice, and the migration that pays for itself on the day you switch](move-the-cloud-not-the-code.md) Workloads stay on hyperscalers because moving means changing code; a twin lets the code not know, and the value in the twin is what signs the migration.
- [Why I love Wardley maps: the best of ours, how I read one, and a map inside a map inside a map](why-i-love-wardley-maps.md) The best of our Wardley maps with their context, why the technique matters, one map read as a story, and a map inside a map inside a map.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 88 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=88)

**Posting this article on LinkedIn?** The cover is [agentic-cost-is-an-engineering-problem.jpg](banners/agentic-cost-is-an-engineering-problem.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/agentic-cost-is-an-engineering-problem.html)*
