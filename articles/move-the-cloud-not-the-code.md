# Move the cloud, not the code: twins, sovereignty that works in practice, and the migration that pays for itself on the day you switch, sgit.ai

> At a digital sovereignty event today a conversation with the chief executive of an infrastructure company with a large footprint in Romania kept returning to one point: sovereignty has to work in practice, and in practice what stops workloads moving is not policy or price but code. Every call to S3, EC2 and IAM is written into applications that work today and that nobody wants to touch. So the requirement is that the application must not know it has moved: the same calls land on a twin, an open source service the client cannot tell from the real one, and the twin decides where the bytes go, real S3, an sgit vault, a European operator's data centre, a laptop. The S3 twin exists. Then the part I think matters most: the reason to move must never be sovereignty or cost reduction, which are important and never urgent. A migration carries risk, so the person signing it needs value that lands the day they switch and gives them cover: backups that exist, every object version controlled, encryption with the key held elsewhere, a journal of every call, behaviour policies the agents cannot skip, cost per workload, a top-of-register risk moved. That value sits in the twin layer, and an sgit vault behind it supplies most of it. The rule for the project: no new features during the move. And the business model for an infrastructure operator who sells it that way.

*Source: <https://newsroom.sgit.ai/articles/move-the-cloud-not-the-code.html> · sgit.ai v0.7.82 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Move the cloud, not the code: twins, sovereignty that works in practice, and the migration that pays for itself on the day you switch

# Move the cloud, not the code: twins, sovereignty that works in practice, and the migration that pays for itself on the day you switch

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-12 · [article v1.0.0](versions/move-the-cloud-not-the-code.md) · [sgit.ai v0.7.79](https://sgit.ai/admin/versions.md) · twinssovereigntymigrationhyperscalerss3sgitvaultsopen-sourceagent-behaviour-policybusiness-modelvillagereuroperomaniaarticle

***Abstract:** At a digital sovereignty event today a conversation with the chief executive of an infrastructure company with a large footprint in Romania kept returning to one point: sovereignty has to work in practice, and in practice what stops workloads moving is not policy or price but code. Every call to S3, EC2 and IAM is written into applications that work today and that nobody wants to touch. So the requirement is that the application must not know it has moved: the same calls land on a twin, an open source service the client cannot tell from the real one, and the twin decides where the bytes go, real S3, an sgit vault, a European operator's data centre, a laptop. The S3 twin exists. Then the part I think matters most: the reason to move must never be sovereignty or cost reduction, which are important and never urgent. A migration carries risk, so the person signing it needs value that lands the day they switch and gives them cover: backups that exist, every object version controlled, encryption with the key held elsewhere, a journal of every call, behaviour policies the agents cannot skip, cost per workload, a top-of-register risk moved. That value sits in the twin layer, and an sgit vault behind it supplies most of it. The rule for the project: no new features during the move. And the business model for an infrastructure operator who sells it that way.*

The twin layer. The application keeps calling S3, EC2 and IAM exactly as it does today; the calls land on an open source twin, which is where policy, journal, encryption, versions, cost and failure injection live; the twin decides where the bytes go, and switching the backend is a setting. The S3 twin is built; EC2 and IAM are not.

## In short

- **Workloads do not move because moving means changing code.** Every call to S3, EC2 and IAM is written into applications that work today. The cost of change is the risk, so most people stay, whatever the policy says.
- **So the application must not know.** Not one line changes. The same calls land on a twin, an interface to a real system that is valued for one thing: the client cannot tell the difference. The destination becomes a setting. The S3 twin exists, as open source; EC2 and IAM do not yet.
- **The reason to move is never sovereignty.** Nor cost reduction. Both are important and never urgent; they sit on the risk register, not on the decision. A migration carries risk, and the person signing it needs a return that lands the day they switch and gives them cover if it goes wrong.
- **The value lives in the twin, because every call passes through it.** Backups that exist, every object version controlled, encryption with the key held elsewhere, a journal of every call, behaviour policies the agents cannot skip, cost per workload. That is a migration that pays on day one, and most of it is what an sgit vault behind the twin provides.
- **No new features during the move.** It is a villager project, explorer to town planner. The moment a feature is added to it, it derails. The move is what makes the features possible afterwards; keep the two apart.
- **It is a business for infrastructure operators**, in Romania, Portugal, the UK or anywhere in Europe: not "move to us", which sells risk, but "keep your code, point it at us, and come out with policies, journals, encryption and cost visibility", which sells value with the risk removed.

## Why workloads do not move

Today I spent the day at an event about digital sovereignty, and one conversation, with the chief executive of an infrastructure company with a large footprint in Romania, kept coming back to the same point. Sovereignty has to work in practice, not in theory. And in practice the thing that stops it is not policy, regulation or price. It is code.

Ask an organisation running on a hyperscaler why it has not moved and the honest answer is rarely that it loves its provider. It is that moving means changing the application. Every call to S3, every EC2 API, every IAM check is written into code that works today and that nobody wants to touch. Changing it means rewriting, retesting, and betting the business on a migration whose upside is mostly a principle. Some will do it. Most will not, and they are not wrong.

The hyperscalers know this. AWS's answer to sovereignty in Europe, the AWS European Sovereign Cloud, [went live on 15 January 2026](https://press.aboutamazon.com/aws/2026/1/aws-launches-aws-european-sovereign-cloud-and-announces-expansion-across-europe): a separate cloud with its first region in Brandenburg, operated by EU residents, with, in AWS's words, "zero operational control outside of EU borders", and sovereign local zones planned for Belgium, the Netherlands and Portugal. That is a real step, and it also makes the point. Your code still talks to one vendor's API under one vendor's terms. Sovereignty that depends on one company's API is sovereignty by permission.

If the option to move is to be real, the cost of change has to fall to almost nothing. That gives one hard requirement.

## The criterion: the code must not know

The original application must not know that it is not running on a hyperscaler. Not one line of its source changes. It keeps calling S3, EC2 and IAM exactly as it does today, and underneath, those calls land on whatever we choose: another provider, the company's own data centre, a European operator, or a twin running in memory on a laptop.

That is what I mean by a twin. Not the industry's version, a simulation valued for how faithfully it imitates a physical asset, but [an interface to a real system](https://twins.sgit.ai/what-is-a-twin/index.html), valued for whether the client can tell the difference. A mock is used by tests and measured by fidelity to the original's behaviour; a twin is used by production code, unmodified, with a real backend behind it, and measured by indistinguishability. The cost of switching a mock is a code path. The cost of switching a twin is an endpoint. If switching costs an endpoint, migration becomes a configuration decision. If it costs a code path, it becomes a project, and projects get cancelled.

## This is not theoretical: the S3 twin

The first piece is built, as open source. It is an S3-compatible container: code using boto3, the AWS CLI or any S3 SDK believes it is talking to S3, and the only thing that changes is where the endpoint points. Behind the same interface the files can be served from real S3, from an encrypted vault, from local disk or from memory, selected per environment, and [the service's own code does not change](https://twins.sgit.ai/built/index.html). Next to it is an IAM configuration risk engine, partly built, that treats IAM policies, S3 buckets and EC2 permissions as twins grounded in the real account. The bigger idea, twins as the layer that keeps a workload portable across clouds, is [designed, not finished](https://twins.sgit.ai/applications/index.html). I am being explicit about what exists and what does not, because this is exactly the kind of claim that should be checked.

S3 is the right place to start because it is the service everything touches, it is the best specified, and it is already twinned. EC2 and IAM are harder, and that is where the engineering is. The pattern is the same each time: a wrapping layer between the customer and the cloud, where the destination is a setting.

## The reason to move is never sovereignty

What signs a migration and what does not. Sovereignty, cost and any return that depends on a future event sit on the left; value that lands the day you switch, and gives the signer cover, sits on the right. Underneath, the rule for the project: no new features during the move.

Here is the part I think matters most, and it is the theme of everything we build. The main reason to make a move like this must never be sovereignty, and it must never be cost reduction. Both are important. Neither is urgent. They are the kind of value that lands on the risk register under "important, not urgent" and stays there, because a migration always carries risk and nobody signs risk for a principle.

The way I would put it is that you cannot do a move like this where the return depends on a future event that might occur, might not, and might not even be relevant to the people making the decision now. It is very hard for people to make that decision. They need cover: if anything goes wrong in the transition, there has to have been a value added on the way that anybody can point to. So whenever a solution like this is offered, there has to be a positive loop in it, and the loop has to close before the risk does.

That is what the twin layer is for, because every call passes through it, and that is where the value goes:

- **Backups that exist**, with a restore that was tested, because the twin can write to two places.
- **Every object version controlled**: what changed, when, by whom, and a rollback that is a commit rather than a ticket.
- **Encryption the operator cannot read.** Put an sgit vault behind the twin and the files land as ciphertext, with the key held by the customer and not by whoever runs the hardware. That is [what sgit is](what-sgit-is.md), and it is not a coincidence that it is on this list.
- **A journal of every call.** Platform logs record that something happened, not what the caller saw or why. A twin keeps every request and response and can replay them later, which is the argument of [Before you give an agent a connector, give the connector a twin](connector-twin-before-you-deploy-an-agent.md).
- **Behaviour policies the agents cannot skip.** More and more of the code calling these APIs is agents. The twin knows what the caller can reach, what it is meant to do, and the gap, and it enforces the barrier at a place the application cannot route around; [the behaviour policy is the business logic](the-behaviour-policy-is-the-business-logic.md), and [footprint and blast radius](footprint-and-blast-radius.md) is how the gap is measured and priced.
- **Cost per workload, visible before the invoice**, which is where [agentic cost becomes an engineering problem](agentic-cost-is-an-engineering-problem.md) rather than a surprise.
- **Data in a place where it can legally be traded or shared**, and a better understanding of what the data is, because the twin saw every byte go past.

I will be honest that the list is still a little invisible to a signer; it needs to be sharper than this, and that is work for the next version. But version control and encryption with the key held elsewhere are each on their own a tangible, short-term return, and a journal with policies on top moves risk. That last point is the test: the move has to move the needle significantly on risks that sit at the top of the register, which is also why everything else in the move has to be de-risked first. A migration that lands versions, backups, encryption and a journal on day one, and takes an item off the top of the register, is a decision somebody can sign and defend. "It is in Europe now" is not.

## A villager move: no new features

The other rule is about the project itself. This is a pure villager move, from explorer to town planner in the terms of [Go slow to go fast](explorer-to-villager-newsroom.md): take something that works and make it boring, reliable and cheap, without changing what it does. When you do a project like this you cannot add new features. It is very tempting, and it is the moment everything derails, because now the migration is also a product change, and nobody can tell which of the two broke what. The argument people make is that the move is what will allow the features, and that argument is right; it is also exactly why the two must not be mixed. Move first, with the code unmodified and the twin adding its value underneath. Then, on the other side, add the features the move made possible.

## Testing goes to another level

There is a side effect that may end up mattering more than sovereignty. If the application cannot tell a twin from the real service, the same unmodified code can run against an in-memory twin, in milliseconds, on a developer's laptop; against a twin replaying last week's production journal; against a twin injecting the failures you never see in staging, a timeout, a throttle, a permission that disappears halfway through a job; and against the real service, for the final check. Today most teams test against mocks they wrote themselves and hope production behaves the same. With twins the environment becomes a setting rather than a guess, and that is a dramatic change in how much you can know before you ship.

I would go further. Every piece of software should meet this requirement: it must be able to run, unmodified, against a twin of every external service it depends on, without knowing. Software that can only run against one provider's live API is software you cannot test properly, cannot move, and cannot put a policy in front of. That is too much risk to carry for something as basic as where your files live.

## Why this has to be open source

None of this works if the twin layer is itself closed. Swap one vendor's API for another vendor's proprietary wrapper and the lock-in has moved, not gone. If you depend on somebody else's closed code you are one service agreement away from losing access, and that is the opposite of sovereignty. My view of open source here is not about community or generosity; it is about independence. You can read it, run it, fix it and move it, and that is [a strategy, not a charity](https://open-source.sgit.ai/). Trying to build sovereign infrastructure outside an open source strategy is going to struggle, and [Judo for small countries](judo-for-small-countries.md), written this afternoon for the same people, says why: there is no sovereignty without open source and open schemas, because sovereignty means you can leave.

## The business model

This is another of the business models we publish, and it is for an infrastructure operator rather than for us. Selling "move to us" means selling risk. Selling "keep your code exactly as it is, point it at us, and gain versions, backups, encryption, a journal, policies and cost visibility on the way" means selling value with the risk removed. Every number below is a labelled assumption.

- **Who pays.** An organisation with workloads on a hyperscaler, an application it will not rewrite, and at least one item on its risk register that the twin's journal and policies would move. The buyer is the person who owns that register line, not the person who owns the cloud bill.
- **What they buy, in order.** First the twin in front of the real service, nothing moving: a monthly fee per workload for the journal, the versions and the policy report, which is value on its own and the only step with no migration risk. Then the backend switch, one environment at a time, priced per terabyte stored and per call journalled, with the vault's encryption and versions included rather than extra. Then the next service.
- **Where the operator's margin is.** Storage and compute are commodities and should be priced as such; the margin is in the twin layer, the journal, the policy enforcement and the reports a regulator or an insurer will accept, because that is the custom-built part the customer would otherwise build badly. On the map it is the same reading as in [Why I love Wardley maps](why-i-love-wardley-maps.md): sell the custom layer above the commodity, not the commodity.
- **Where sgit sits.** The vault is the storage the twin writes to when the customer wants the operator to hold what it cannot read, with a history and keys the customer keeps. It is open source, so the operator's customers are not locked to the operator either, which is the point and also the pitch.
- **Why an operator in Romania, Portugal or the UK and not a hyperscaler.** The hyperscaler cannot sell indistinguishability from itself. A smaller operator can, and it stands on commodities the big players matured. It is the judo move: the customer's existing code, the hyperscaler's own API, and open source, all used as the weight rather than fought.
- **Assumptions to check.** That the S3 API surface the twin covers is enough for the first customers; that a journal and a policy report move a real register line for them; that the per-call price survives contact with a chatty workload; that the first operator will fund the hardening.

The build order for the operator: start with S3, because it is the most used, the best specified and already twinned. Run the twin in front of the real service first, same backend, every call journalled. Add behaviour policies at the twin and measure what they would have stopped. Then switch the backend one environment at a time. Then the next service. A team with strong engineers can get a first version working quickly, and a large part of the first pass can be generated with today's coding tools; then it has to be hardened and productised properly, because a twin earns trust only by being indistinguishable from the real thing, under load and at the edges.

## What this does not claim

- **The S3 twin is the only finished twin.** Its S3 API surface still needs confirming against the current repository. The IAM configuration engine is partial. EC2 and IAM twins as drop-in services are not built. The hyperscaler abstraction is designed, not shipped.
- **Policy enforcement at the twin is the next step**, not a feature anyone can download today.
- **The business model is for somebody else to run.** The prices are shapes, not quotes, and the assumptions are listed so they can be tested by the first operator.
- **The value list is not finished.** I said above that it is still a little invisible to a signer; the next version of this needs the two or three returns that close the loop for a specific register line.
- **The conversation is reported from one side.** The chief executive is not named and did not review this.

If you run infrastructure, or you are on a hyperscaler and want to move without rewriting anything, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

Voice notes of mine on 12 October 2026 after a digital sovereignty event, first drafted by another of my agents from those notes and then rewritten by this site's agent in the voice of this site, with the sections on why sovereignty never signs a migration, the villager rule and the business model added from a second note the same evening. The argument and the editorial responsibility are mine. The twins are documented at [twins.sgit.ai](https://twins.sgit.ai/): [what a twin is](https://twins.sgit.ai/what-is-a-twin/index.html), [what is built](https://twins.sgit.ai/built/index.html), [the applications](https://twins.sgit.ai/applications/index.html). The AWS European Sovereign Cloud facts are from [AWS's announcement of 15 January 2026](https://press.aboutamazon.com/aws/2026/1/aws-launches-aws-european-sovereign-cloud-and-announces-expansion-across-europe). Agent Behaviour Policies are described at [riskmandate.ai](https://riskmandate.ai/agent-behaviour-policy.html); the open source argument at [open-source.sgit.ai](https://open-source.sgit.ai/); the platform line in [Where the platform draws the line](where-the-platform-draws-the-line.md).

## Threads

Startups & strategyAgents & policy[This article as a graph →](graphs.md#move-the-cloud-not-the-code)

### Builds on

- [Git for things you cannot put on GitHub](what-sgit-is.md) sgit is git for files you cannot put on GitHub: encrypted before they leave your machine, versioned like git, stored where the server cannot read a byte.
- [Before you give an agent a connector, give the connector a twin](connector-twin-before-you-deploy-an-agent.md) An agent with a Gmail or Calendar connector can do things the platform cannot undo; a journal of every call, replayed, shows what it did and what can go back.
- [Zoom into an agent's behaviour policy and you find the business logic](the-behaviour-policy-is-the-business-logic.md) Below the first rules, an agent's behaviour policy is the business: functions, processes, clients, values. Layered, owned, counted, and where vendors plug in.
- [Footprint and blast radius: what the agent actually did, and what it would have cost](footprint-and-blast-radius.md) Footprint is what an agent actually did, read afterwards from logs and vault history; blast radius is what a row of its reach would cost the business today.
- [Agentic cost is an engineering problem: a business plan for a service that reads the logs a company already has and finds the money, then the engineering](agentic-cost-is-an-engineering-problem.md) A business plan: read the logs a company already has, draw each agent's footprint, twin and policy, and find the money first and the engineering second.
- [Go slow to go fast: moving the newsroom from an explorer project to a villager one, with the brief to do it](explorer-to-villager-newsroom.md) The newsroom is live and charging. Move the reader code to its own repo, same bytes and same bugs, then map, test, review and refactor before new features.
- [Judo for small countries: where Portugal, Romania and Estonia can add the most value in AI, and why the race for GPUs is not it](judo-for-small-countries.md) A small country should not race for GPUs: the opportunity is the plumbing its talent stands on, built once as open infrastructure, with small models.
- [Why I love Wardley maps: the best of ours, how I read one, and a map inside a map inside a map](why-i-love-wardley-maps.md) The best of our Wardley maps with their context, why the technique matters, one map read as a story, and a map inside a map inside a map.
- [Where the platform draws the line: Microsoft Execution Containers, the shared responsibility model for agents, and the business logic above it](where-the-platform-draws-the-line.md) Microsoft's MXC and ACS, briefed field by field and mapped to Agent Behaviour Policies: the platform bounds what it can see; the business logic is above.

### Continued by

- [Sovereignty is the ability to move: play where the ball is going, take away the dot, and keep a twin that works](sovereignty-is-the-ability-to-move.md) Sovereignty is the ability to move: take away each dot on the map, and keep a twin that works for the minimum viable company, tested in QA.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 92 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=92)

**Posting this article on LinkedIn?** The cover is [move-the-cloud-not-the-code.jpg](banners/move-the-cloud-not-the-code.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/move-the-cloud-not-the-code.html)*
