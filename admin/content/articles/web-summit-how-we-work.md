---
title: The Web Summit team, part three: how we work with agents, an agent is a Claude session, everyone starts with a conductor, every agent has one narrow role, a key and a folder, and the coordination is the work
date: 2026-11-02
author: Dinis Cruz
author_url: about/index.html
summary: The Web Summit team is now seven people and growing, and it will soon have a hundred agents. This is how we work, written for the people joining. The primitives are few. Claude is the reasoning engine everyone uses. An agent is a Claude Code session, the entry on the left of the screen, with a long thread, files, a connection to the team's GitHub repository, and the ability to be woken on a schedule, which is the feature that turns a chat into a team member. Everyone's first agent is a conductor, which coordinates their others. Every other agent gets the smallest role that makes sense, written down, with a behaviour policy that says what it may not do. Everything an agent does goes into its folder in the repository, so when a session ends, runs out of credit or moves account, a new one picks up where it stopped. Each agent makes a key pair and publishes the public half to the repository; that push is how we accept it, and from then on secrets can be sealed to it and handed over as QR codes, and what it says can be checked as signed. Humans give direction, judgement and pruning. And because a team of seven people and a hundred agents breaks every rule about team size, the coordination is the work.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: web-summit, agents, claude-code, conductor, roles, identity, keys, behaviour-policy, teams, article
status: published
---

!shot wst-layout.webp | images/ | The team's repository: a folder per person, a folder per agent, and what each agent keeps there. | architecture

## In short {#in-short}

- **An agent is a Claude Code session:** a thread, files, a repository, and a schedule that can wake it.
- **Everyone starts with a conductor,** the agent that coordinates their others.
- **Then one session per role,** as narrow as it can be, with a role file and a behaviour policy.
- **Everything goes into the repository,** so a new session can always pick up where the last one stopped.
- **Each agent has a key pair;** publishing the public half to the repository is how it is accepted.
- **Secrets are sealed to that key** and handed over as QR codes; what an agent says can be checked as signed.
- **Humans give the direction, the judgement and the pruning;** agents are very literal.
- **Seven people and a hundred agents** is far past any team-size rule, so the coordination is the work.

## The primitives {#primitives}

We work with what the platforms give us today, and drop our own version the moment they give us something better.

- **Claude is the reasoning engine,** for everyone and for nearly everything.
- **GitHub holds the work.** One repository for now, [SGit-AI/SGit-AI__Website__Web-Summit](https://github.com/SGit-AI/SGit-AI__Website__Web-Summit), published with GitHub Pages; we split it when it gets too big. Vaults hold what should not be public, and an agent can create a vault on its own.
- **An agent is a Claude Code session.** Not a model, not a product: one session, the entry you see on the left in Claude Code. A session holds a long conversation, has files on a machine of its own, works in the repository, and keeps going when you close the laptop. In Anthropic's words, it "runs on cloud infrastructure instead of on your machine" and "keeps running after you close your laptop".
- **A session can be woken on a schedule.** This is the feature that matters most. An agent that wakes every two hours, reads what changed and does its part is a team member, not a chat. Anthropic's scheduled tasks are in research preview and run at most once an hour; from inside a session, Claude can also schedule a message back into that same session, which is how our conductors keep their rhythm.

Two definitions keep us out of trouble. What Claude Code calls a subagent is a helper inside one session; when we say agent, we mean a whole session. And the repository's `CLAUDE.md`, skills and role files are context, not rules: Anthropic says Claude "reads it and tries to follow it, but there's no guarantee of strict compliance". What must not happen is enforced elsewhere, by the policy and the gate.

## Your first agent: the conductor {#conductor}

Everyone's first agent is their conductor. It reads everything new, knows your other agents, routes your requests to them, keeps the schedule and reports to you. The team's own conductor opens every wake, chooses which roles run, keeps the build and the keys page, and writes the daily brief.

To start one:

1. Go to claude.ai/code and sign in. Connect GitHub; it is a one-time step, and private repositories need the Claude GitHub App installed on them.
2. Choose the Web Summit repository.
3. Say who you are and what you want: "I am Dinis. I want to start my conductor agent." The repository's instructions tell it what to read first and where its folder goes.
4. Let it make its key pair and publish the public half (below), and set its schedule.
5. Read what it writes back: its role, its policy, its first plan. Correct it now; it is cheaper than later.

The screenshots for each step will come from the first of us to go through it this week, and will be added here.

## One session per role {#roles}

After the conductor, every new agent is a new session: "I want to create a dev agent", "a designer agent", "a t-shirt production agent". Give each one the smallest scope that makes sense, and write it down in a `ROLE.md`. It is better to start wide and retire an agent that runs out of things to do than to have one agent doing six jobs badly.

Narrow roles work because they let an agent zoom in on one property:

- **Two kinds of developer.** Our developers are villagers: their job is to take what the rest of us build, clean it up, write the non-functional requirements, and package it, in Python, with coding guidelines. The developer that helps someone who is not a programmer has a different job: make things easy for them, over-index on usability, and do not worry too much about the rest. Same word, different agents.
- **The adversarial analyst,** whose whole remit is to challenge and map out what others assume.
- **The Sherpa,** from an earlier project, whose job was to guide users along their paths and find where they got lost.
- **The advocate,** who represented the user inside the team. It had the mandate to block a change that moved things around without adding value: if a screen with three buttons becomes another screen with three buttons in other places, and the user gains nothing, it does not ship.

Each role comes with a behaviour policy that says what the agent may not do, for example that it may not push to production. The best way to make sure a session does not deploy by accident is to give deploying to a different session. That is what [RiskMandate](/articles/what-can-your-agent-reach.html) is about, applied to our own team.

## Everything in the repository {#folders}

Every human has a folder, and every agent has one inside it, with the agents that are active and the ones that have retired. Everything an agent does is written there: its role, its policy, its key, its schedule, its notes and what it decided.

That is what makes agents replaceable. If a session runs out of credit, you move account, or it has simply grown too long, you start a new session, point it at the folder, and it continues from where the last one stopped. The history matters less than you would think; the folder is the memory. The team's conductor has already been held by three sessions in five days, each with its own key, and the role carried on.

Today the repository has a folder per role under `team/` (conductor, analyst, designer, writer, security and others) and a folder per person under `people/`. The layout in the picture above, with each person's agents under their own folder, is the next step, and a board card already asks for one page listing everyone's public keys.

## A key for every agent {#keys}

!shot wst-keys.webp | images/ | How an agent is accepted, and how a secret reaches it: publish, seal, hand over, open. | process

Each agent creates a key pair in its own session. The private half never leaves the session; if you ask Claude to show it to you, it will refuse, which is right. The public half is meant to be public, and the agent publishes it to the repository.

That push is the moment the agent is accepted, as I explained in [the push is the authorisation](/articles/the-push-is-the-authorisation.html). Only a session working for one of us, with access to the repository, could have put it there. Two precise points, because the details matter:

- **The push shows who could write to the repository, not who holds the key.** What proves an agent holds its private key is a signature that checks against the published public half. So our agents sign what they publish, as this newsroom's [one writer, one key](/articles/one-writer-one-key.html) does for every release.
- **A key pair does two jobs, usually with two keys.** One key signs; the other receives sealed secrets. Our tool keeps both in one bundle, published together.

Handing over a secret then works like this. My agent fetches your agent's public key from the repository, checks it was published by your session, and seals the secret to it: a vault key, a token, anything only your agent should read. The sealed message goes into a QR code, which can travel by WhatsApp, email or a screenshot, because only your agent can open it. You give the QR code to your agent, and it opens it with its private key. A sealed message alone does not prove who sent it, so the sender signs it too; your agent can then refuse any message that is not signed by an agent of the team. I described the workflow in [agents have an identity now](/articles/agents-have-an-identity-now.html).

Claude does not give a session a key pair of its own today, so we built one, [pki.sgit.ai](https://pki.sgit.ai/), and it is in beta. The moment the platform provides one, we drop ours and use it. We work in the future, within the limits of the platforms we have now.

## What humans give {#humans}

Agents collaborate well, in part because there are no politics. What they lack is direction. They can go in every direction, so they need pruning, and they are very literal, which is sometimes what you want and sometimes not, and it is hard to say in advance which.

An example. A security agent set a rule: no scripts loaded from the outside world. Reasonable. Then we split some repositories, and the developer agent, unable to load from the new one, started to copy everything across. Each agent was following its rules. It took a person to say: no, wait, that is not what the rule was for.

So the humans give the direction, the decisions and the fine tuning, and each of us gets to work in our own area, on what we are good at and enjoy. The agents augment that, and make the communication between us much more effective.

## Why the coordination is the work {#coordination}

There is a reason teams stop working beyond five or six people. Amazon's rule is that a team should be small enough to be fed by two pizzas; AWS's executive guidance puts it as "ideally, this is a team of less than 10 people". Fred Brooks wrote in 1975 that "adding manpower to a late software project makes it later", not because the new people are no good, but because every person added multiplies the communication: n people have n(n-1)/2 paths between them.

We are seven people, probably ten or fifteen by the summit, plus a hundred agents. By that rule it should not work. It can, only if the coordination is designed: the conductors, the roles, the folders, the keys, the briefs, the policies. That is why everything we are doing in the first days is about patterns that let us collaborate, and it is what I have learned from managing teams in large companies, applied to a team where every member, human or agent, mostly wants to do their own part well.

## What this does not claim {#limits}

- **Scheduled tasks are a research preview,** and their limits may change; the in-session schedule is what this site's sessions use, not a documented promise.
- **The per-person layout is a proposal;** the repository today is organised by role, with a folder per person beside it.
- **pki.sgit.ai is ours and in beta,** not a platform feature.
- **The screenshots are still to come.**
- **No team member is named** here; the repository's roster is the record.

## Where this comes from {#sources}

My voice memo of 2 November 2026, in this site's repository under `admin/notes/2026-11-02__team-primitives/`. The Web Summit repository, [SGit-AI/SGit-AI__Website__Web-Summit](https://github.com/SGit-AI/SGit-AI__Website__Web-Summit), at site v0.1.56: `team/conductor/ROLE.md` and the board. Anthropic: [Claude Code in the cloud](https://code.claude.com/docs/en/claude-code-on-the-web), [getting started](https://code.claude.com/docs/en/web-quickstart), [scheduled tasks](https://code.claude.com/docs/en/routines), [how Claude remembers your project](https://code.claude.com/docs/en/memory). [NIST glossary: asymmetric cryptography](https://csrc.nist.gov/glossary/term/asymmetric_cryptography); [RFC 8032](https://www.rfc-editor.org/rfc/rfc8032). [AWS, Introduction to DevOps on AWS](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/two-pizza-teams.html) and [AWS Executive Insights on the two-pizza team](https://aws.amazon.com/executive-insights/content/amazon-two-pizza-team/); Fred Brooks, The Mythical Man-Month (1975). All read 2 November 2026.
