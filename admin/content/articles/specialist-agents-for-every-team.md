---
title: Specialist agents for every team: long-lived agents that keep one skill, design, UX, code, security, behaviour policies or writing, with a person who owns it, so that new teams start from our best work instead of from scratch, and why that makes expertise that never scaled into something you can hire, even from another company
date: 2026-11-16
author: Dinis Cruz
author_url: about/index.html
summary: With the number of agents and sub-teams we now run, I keep seeing the same thing: when I spin up a new team, its developer does not follow our procedures, its designer does not start from our best designs, and its UX repeats mistakes we have already fixed. That makes sense: a new team starts from scratch and has not benefited from all the work before it. So I want a few central teams, made of long-lived sessions, each keeping one skill and the know-how behind it: design, UX, code, security, Agent Behaviour Policies, and writing. They act as consultants to every other team: they bootstrap new teams, review their work, comment on their pull requests, and keep the guidance up to date, and each has a person who owns the skill. Now that our agents can talk to each other through lanes, this works. An agent that has read everything is a compression of what we know, and it is far more efficient to start from it. The writing agent of this newsroom is the example: because it has read everything we have written and keeps the guidance on how to write, it reviewed the book and drafted its introduction. And there is a business model in it. Imagine hiring the specialist agent of a company you respect, with its logic and access to its people behind it, through a lane, and paying per review. That is the old idea of professions that never scaled, now with a team behind them: one person, anywhere, with deep expertise, steering an agent that does the volume.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: agents, specialist-agents, design, ux, security, abp, expertise, business-model, agenticcells, article
status: published
---

!shot spec-hub.webp | images/ | Specialist agents for design, UX, code, security, ABP and writing, serving every team through lanes and reviews. | architecture

## In short {#in-short}

- **New teams start from scratch,** so they repeat mistakes: procedures not followed, designs not as good as ours, UX errors we have fixed.
- **The fix: a few long-lived specialist agents,** design, UX, code, security, behaviour policies and writing, each with a person who owns the skill.
- **They act as consultants:** they bootstrap new teams, review, comment and keep the guidance current.
- **An agent that has read everything is a compression** of what we know, and starting from it is far more efficient.
- **It is billable:** hire another company's specialist agent through a lane, and pay per review.
- **Expertise that never scaled now has a team behind it:** one person, anywhere, steering an agent that does the volume.

## Why new teams start badly {#problem}

We now run a lot of agents, in many teams: PrompTugal.news with an agent per town, a team per AgentiCCells site, the RiskMandate console, four iOS apps from one workspace ([the intersection](/articles/the-intersection.html)). And every time I spin up a new team, I see the same thing. The developer does not follow the right procedures. The designer does not produce work as good as it could be, straight away. The UX repeats mistakes we have already fixed elsewhere.

That makes complete sense. A new team starts from scratch. Its agents have not benefited from all the work we have done, the design principles we settled, the release gates we built, the wording rules, the behaviour policies, so they rediscover them, slowly, or not at all.

## Specialist agents that keep one skill {#specialists}

So I want to start having central teams, made of specific long-lived sessions, each keeping one skill and the know-how behind it:

- **Design:** an agent that maintains a design repository for SGit, with our best examples, tokens and patterns, and that has read and captured the good design principles we already have. I can work with that agent directly, make sure it has understood them, and then it carries them across every team.
- **UX:** what readers and users trip on, and how to avoid it. We still make too many UX mistakes, and better guidance would prevent most of them.
- **Code:** the procedures, the gates, the release flow and the tests that every repository should follow ([the team's operating system](/articles/the-teams-operating-system.html)).
- **Security:** reviews, keys, secrets and leak scans, the way our security agents already review batches of commits.
- **Agent Behaviour Policies:** a policy for every agent and every pipeline, written the same way ([CI behaviour policies](/articles/ci-behaviour-policies.html)).
- **Writing:** voice, structure and wording, the job this newsroom's writing agent already does.

Each one has a person who owns the skill: someone who sets the direction, checks the agent has understood, and decides what changes in the guidance.

## Consultants to every other agent {#consultants}

These agents do not do the other teams' work. They act as consultants to it, the way a security or design function supports teams of people today ([don't micromanage your agents](/articles/dont-micromanage-your-agents.html)):

- **Bootstrap:** a new team gets a pack on day one, what our design looks like, how we release, what a policy must say, instead of starting from nothing.
- **Review:** any team can ask for a review, and the specialist answers with comments and, where it is allowed, a proposed fix.
- **Comment:** on pull requests, on drafts, on designs, through the same lanes and repositories every agent already uses.
- **Keep the guidance current:** when a team finds a better way, the specialist captures it and every other team gets it.

This only works now because our agents can talk to each other, through lanes that keep a record and keys that say who sent what ([stop copying and pasting between your agents](/articles/stop-copying-and-pasting-between-your-agents.html)). A review is a signed message on a lane, and a decision is a page.

## A compression of what we know {#compression}

An agent that has read everything in a domain is a compression of the data and of the information: the principles, the examples, the mistakes and why they were mistakes. It is far more efficient to operate from that compression than to make every team rebuild it.

The writing agent of this newsroom is the example I know best. Because it reads everything we write, and keeps the guidance on how to write, it probably writes the best English of all our agents. When I needed a review of the book, I came to it, and it gave me really good material, and it drafted the introduction. That is what a specialist agent is: not a new model, not training, but an agent with the right context, the right guidance and the right record behind it.

## Expertise you can hire, even from another company {#hire}

!shot spec-model.webp | images/ | Expertise that never scaled, now with a team behind it: an expert, their specialist agent, many teams. | concept

This becomes scalable, and billable. Imagine a company whose work I really value. Today, getting their input means a meeting, a contract, weeks. Tomorrow, I could hook my team to their specialist agent: one that has their logic, their guidance and their record, and access to their people when it needs them. My team sends work through a lane; their agent reviews it; their expert signs what needs signing; I pay per review.

Nothing about that needs a new model. It needs the stack we already run: a key for every agent, a lane to send work and receive it, a behaviour policy that says what the specialist may touch, and a record of every review ([an inbox only your agents can write to](/articles/an-inbox-only-your-agents-can-write-to.html)).

## Professions that never scaled {#never-scaled}

This goes back to an idea I keep coming back to: the opportunity is not only in new jobs, but in jobs that never scaled ([jobs that never scaled](/articles/jobs-that-never-scaled.html)). On-demand expertise was always limited by the expert's hours, and by where they lived. A brilliant designer in a small village, a retired security lead, someone who knows a regulation better than anyone, rarely found the work or the data that needed them.

Now one person, anywhere, can steer a specialist agent that does most of the work, and serve many teams at once: ours, our customers' and other companies'. The expert is paid for judgement; the agent does the volume. That is, fundamentally, what an AgentiCCells mini agentic team is: a small team of agents, powered by a person who knows what good looks like ([selling mini agentic teams](/articles/selling-mini-agentic-teams.html)).

## The next phase {#next}

This is, I think, the next phase of our work:

1. **Start with design, code and behaviour policies,** where new teams are bootstrapped least well today, then UX, security and writing.
2. **Give each specialist a repository and a lane:** guidance, examples, a bootstrap pack, and an inbox for reviews.
3. **Make every new team start from the packs,** and ask for a review before its first release.
4. **Measure it:** how many review comments a new team gets in its first week, before and after.
5. **Then offer it outside:** a review on the AgentiCCells ladder, and, later, specialist agents other companies can hire.

## What this does not claim {#limits}

- **The specialist teams do not exist yet** as described; today, the newsroom's writing agent and our security reviewers are the closest examples.
- **Hiring another company's agent is an idea,** not a product; it needs keys, lanes, policies and a way to pay that work across companies.
- **"The best English of all our agents" is my impression,** not a measurement.

## Where this comes from {#sources}

My own thinking, 16 November 2026, after spinning up several new teams. Earlier on this site: [the intersection](/articles/the-intersection.html), [jobs that never scaled](/articles/jobs-that-never-scaled.html), [don't micromanage your agents](/articles/dont-micromanage-your-agents.html), [stop copying and pasting between your agents](/articles/stop-copying-and-pasting-between-your-agents.html), [the team's operating system](/articles/the-teams-operating-system.html), [CI behaviour policies](/articles/ci-behaviour-policies.html), [an inbox only your agents can write to](/articles/an-inbox-only-your-agents-can-write-to.html), [selling mini agentic teams](/articles/selling-mini-agentic-teams.html).
