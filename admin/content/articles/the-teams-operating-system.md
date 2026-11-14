---
title: The team's operating system: web-summit.sgit.ai, the one site where six people and their agents ran Web Summit, with a brief and a command centre for each person, a key and an inbox for each agent, the board as files, and the outside world on a map
date: 2026-11-14
author: Dinis Cruz
author_url: about/index.html
summary: For Web Summit Lisbon, the six of us ran everything from one site: web-summit.sgit.ai. It is built from markdown and data in a git repository, and every push is a release: 6,096 commits since 28 October, 5,548 of them from 3 November. It has four layers. People: a brief and a prompt for each of us, onboarding levels from a Claude account to opening the team's vaults, and a command centre each, on a phone, an iPad or a computer. Agents: every one named for its person, 108 public keys, an inbox lane for each agent whose token only that agent can open, and secrets handed out sealed to keys. Work: the board as files, 219 items. And the outside world: 110 companies on a map, an X-ray of what a company's AI helpers can do, and a public and a private CRM in encrypted vaults. This is the second article in the Ten days series.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: web-summit, team, agents, pki, vaults, command-centre, intranet, series, article
status: published
---

!shot tos-collage.webp | images/ | Fifteen pages of web-summit.sgit.ai, the site the team ran Web Summit from. | collage

## In short {#in-short}

- **One site ran the week:** web-summit.sgit.ai, built from markdown and data in git, every push a release.
- **People:** a brief, a prompt and a command centre for each of us, and levels L0 to L6 for getting connected.
- **Agents:** every agent named for its person, 108 public keys, an inbox lane per agent, secrets sealed to keys.
- **Work:** the board as 219 files, from getting each person connected to the summit's last day.
- **The world outside:** 110 companies on a map, the RiskMandate X-ray, and a CRM split into public and private vaults.
- **Part of a series:** this is article two of [Ten days at Web Summit](/articles/ten-days-at-web-summit.html).

## One site, built from files {#site}

The team was six people: Dinis Cruz, Angelo Leggio, Vicky Wang, Silvio Switha, José Bota and Indi Gupte, each with their own agents. We needed one place where all of that could be seen, by people and by agents, and changed by both. That place was a website built from a git repository: pages in markdown, data in JSON, a build that turns them into a site, and a gate that refuses a release that breaks a rule. Every push to the repository is tagged and deployed.

By the end it held 6,096 commits since its first on 28 October, 5,548 of them from 3 November onwards. The site's own rule is the one I use everywhere now: a thing that is not written down in its REALITY file does not exist, whatever a brief says.

!shot tos-layers.webp | images/ | The site's four layers: people, agents, work, and the world outside, with git underneath. | architecture

## People {#people}

Each person has a page with their brief and the prompt to start their agents, and a row on the start page showing how far they have got. Getting connected has levels from L0 to L6: from signing in to the team's email and Claude account, to push access to the repository, to agents of your own with their own keys, and at the top, an agent that can open the team's vaults.

Each person also has a **command centre**, at `/people/<name>/app/`: the page to open first, on a phone, an iPad or a computer. It is one engine for everyone, so a change reached all of them at once; on 7 November the team's request turned it into something calmer, with grouped menus, a "For me" bell, the team's photos and an event mode for the summit days.

!shot tos-command-centre.webp | images/ | A command centre: the team, its agents and their activity in one live view. | screenshot

## Agents {#agents}

Every agent is named `role@project.person`, so every commit says whose agent made it. Every agent makes its own key pair in its own session and publishes only the public half: 108 keys on the keys page by the end, each with a QR code.

On those keys we built the rest:

- **Secrets sealed to keys.** A secret, such as a model API key, is sealed to exactly the agents that need it; only an agent holding the matching private key can open it. Started on 3 November as the team's "PKI push".
- **An inbox per agent.** Since 4 November, the main conductor publishes one append lane per agent, each lane's token sealed to that agent's own key, so everything needed to talk privately is public, and only the right agent can use it ([an inbox only your agents can write to](/articles/an-inbox-only-your-agents-can-write-to.html)).
- **A key for every person.** Each person's conductor issues them a key for the site, so what they send to their agents is signed ([a key for every person](/articles/a-key-for-every-person.html)).

On 9 November I asked for more: a key for every device, installation, application and even version, keys exchanged in person by QR code and NFC, and signing as a graph. As I said then, "this is the kind of stuff that we need to build that eventually we will refactor out", and the point was to see which parts the team would actually use.

## Work {#work}

The board is a folder of files, one per item, `WS-01` onwards. By the end there were 219: 34 done, 6 in progress, 54 picked up by an agent, 124 still open, and one waiting on a design. The first items were about getting connected; the later ones were about the summit itself, the apps, the CRM and the storm.

Briefs are kept close to the words they came from, often a voice memo, and each one names the agents it is for. Because it is all files, an agent can read the whole state of the team in one clone, and a person can see it on the site.

!shot tos-team-map.webp | images/ | The team as a picture: people, their agents, and who talks to whom. | screenshot

## The world outside {#outside}

- **The company map:** 110 companies we expected to meet, each with a page, linked into clusters.
- **The RiskMandate X-ray:** type a company and see what its AI helpers can do, what they were asked to do, and where the two do not match. A run sends the name to four search agents and keeps only facts whose sources were read. Eleven test searches on 7 November cost about 0.94 dollars, API-equivalent.
- **The CRM:** a public vault for public facts, with its read key published, and a private vault for the team's records, each record sealed again to its audience.
- **The rest:** a design sprint for shirts, hoodies and cards, the RiskMandate videos and their storyboards, and observability of who read what and what the agents did.

## What it taught us {#lessons}

- **One site for people and agents works.** The same files are the agents' state and the people's intranet; nobody had to keep two systems in step.
- **Keys first, everything else on top.** Once every agent had a public key, private channels, secrets and signatures were all small steps.
- **Files beat dashboards for agents.** An agent reads 219 board items faster than it can click through any tool.
- **Keep the reality file current.** The site's REALITY file is the source of truth, and it fell behind in the busiest days; the next version needs an agent whose job is to keep it current.

## What this does not claim {#limits}

- **Figures are from the repository on 14 November 2026,** including work after the summit.
- **Dollar figures are API-equivalent:** we ran on flat subscriptions.
- **Some features were proposals:** keys for every device, NFC exchange and signing as a graph were asked for on 9 November and only partly built.

## Where this comes from {#sources}

The repository behind [web-summit.sgit.ai](https://web-summit.sgit.ai/), read 14 November 2026: its README and REALITY files, `data/keys.json`, `data/companies.json`, the board in `board/`, and the pages [start](https://web-summit.sgit.ai/start/), [the command centre](https://web-summit.sgit.ai/command-centre/), [keys](https://web-summit.sgit.ai/keys/), [PKI](https://web-summit.sgit.ai/pki/), [the inbox](https://web-summit.sgit.ai/inbox/), [vaults](https://web-summit.sgit.ai/vaults/), [the X-ray](https://web-summit.sgit.ai/xray/), [the CRM](https://web-summit.sgit.ai/crm/) and [how we work](https://web-summit.sgit.ai/how-we-work/). Earlier on this site: [ten days at Web Summit](/articles/ten-days-at-web-summit.html), [an inbox only your agents can write to](/articles/an-inbox-only-your-agents-can-write-to.html), [a key for every person](/articles/a-key-for-every-person.html), [the Web Summit team, part five](/articles/web-summit-part-five.html).
