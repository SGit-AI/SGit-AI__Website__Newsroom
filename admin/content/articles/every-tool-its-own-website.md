---
title: Every tool its own website: turning the 49 browser tools of tools.sgraph.ai, each built because I had a problem, into sovereign websites of their own, with a theme, documentation and a small agent team each, released in waves from the simplest, with shared components pulled out, pinned versions and signed hashes kept apart, and a team of teams to keep them all moving
date: 2026-11-19
author: Dinis Cruz
author_url: about/index.html
summary: Every tool on tools.sgraph.ai exists because I had a problem and built something for it: encrypting a file, making an SSH key, opening a vault in the browser, transcribing a voice note, splitting the audio out of a video. There are 49 of them now, and about 90 shared components, and some became better than anything else I use. They also show the limit of an explorer project: one repository, one site, harder and harder to maintain. And they answer a frustration with the web itself, where simple things are buried under ads and hidden behind sign-ups. Sovereign websites are the place to put them. Each tool gets its own site at its own address, self-contained, documented and good to look at, on GitHub Pages for pennies, forkable, open to a maintainer who wants to take it on, and with a small team of agents inside, and a model where it helps, even one running in the browser. This piece maps the tools by family, proposes the order, starting with the simple ones the factory has already begun, a shared component library, the versioning model the tools already half use, latest and pinned versions with their security notes, signed hashes kept in a separate repository so a compromised site shows, and a team of teams to run it all.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: tools, sovereign-website, open-source, components, versioning, agent-teams, article
status: published
---

!shot tls-families.webp | images/ | 49 tools, each made for a problem: grouped by family, with the first ones the factory has started. | concept

## In short {#in-short}

- **49 tools, about 90 components,** each built because I had a problem.
- **One tool, one sovereign website:** its own address, documentation, design and agent team.
- **Simple first:** encrypt a file, make an SSH key, what is my IP; the factory has started.
- **Shared components pulled out** into a library of their own, each versioned.
- **Pinned versions, and signed hashes kept apart,** so a compromised site shows.
- **A team of teams** to change many tools at once.

## Every tool was a problem {#problem}

When I look at [tools.sgraph.ai](https://tools.sgraph.ai/), and its development version [dev.tools.sgraph.ai](https://dev.tools.sgraph.ai/), I remember each one, because each was a problem I had: I needed to encrypt a file, so I built a file encryptor; I needed an SSH key, so an SSH key generator; I needed to split the audio out of a video, so a video tool; I needed to read a vault without a command line, so a vault browser. It was the first time I really felt that if you have a challenge, you might as well build the tool for it. Some of those tools became better than anything else I use.

They also answered a frustration. The web became convoluted. Go looking for something as simple as your IP address, a random password or a file's hash, and you find pages riddled with ads, features you did not ask for, and the useful part hidden. I would pay a little for a page that does one thing well; most of these should have a small payment, and let people choose. What I wanted was very simple websites that each do one thing very well. Some could become businesses; others are just good tools.

## What is there {#map}

The repository behind the site, [SGraph-AI__Tools](https://github.com/the-cyber-boardroom/SGraph-AI__Tools), holds 49 tools, from version 0.1.4 to 0.1.70, and about 90 shared components, from a key generator and a vault picker to a whole set for language models and for audio. Grouped by family:

- **Keys and secrets (5):** file encryptor, file hasher, friendly key generator, SSH key generator, and an authentication test bed.
- **Vaults and sending (14):** a vault browser, editor and manager, a vault opened in Python in the browser, send and receive, a send simulator, the sg-send command line in the browser, a speed test, and the folder, file system and tree tools behind them.
- **AI and agents (10):** chat, one-shot requests, a multi-agent chat, an agentic loop with tools, an agent that can act on your machine through a bridge, an LLM development environment, a model compatibility matrix, an OpenRouter account manager, an infographic generator and a slide deck generator.
- **Audio and video (13):** transcription from a file or live, voice memos with local Whisper, a media probe, a narrated review, a video recorder, a video creator, a multi-clip editor, a video publisher, video split and trim, and three YouTube tools.
- **Documents and images (5):** image tools, a HEIC converter, a markdown viewer, Mermaid diagrams and a Python console.
- **Publishing and messages (2):** a LinkedIn publisher and a WhatsApp desk.

## Why one site each {#why}

They are a typical explorer project ([explorer coding](/articles/explorer-coding.html)): fast while I was exploring, then slower, because one repository and one site for 49 tools gets messy to update and maintain. The refactor is one I like from an engineering point of view: individual, self-sufficient parts. Each tool as its own [sovereign website](/articles/what-is-a-sovereign-website.html):

- **Its own address and its own repository,** so it can be found, linked, forked and maintained alone.
- **Self-contained and documented:** what it does, what stays in your browser, how it works.
- **Good to look at,** with the same design family across all of them, which the old site never quite had.
- **Cheap to run:** a static site on GitHub Pages costs almost nothing, and runs inside a company as easily as outside.
- **Open to a maintainer:** I would like people to take some of these on, the video editor most of all, and a repository of its own makes that easy.
- **With a team of agents inside,** to keep it working and to improve it ([a website with a team inside](/articles/a-website-with-a-team-inside.html)).

## A little intelligence in each {#ai}

Every tool can now come with a small agent, and that changes what a simple tool can be: a markdown viewer that summarises, an image tool that suggests what to redact, a transcriber that writes the notes. Where it can, the model should run in the browser or on the device: the voice memo tool already transcribes with Whisper locally. A month ago, running a model in the browser was still clunky; a dedicated site for it, with one model and one job, is a good tool in its own right ([watch your website being built](/articles/watch-your-website-being-built.html)).

## The order {#waves}

Not all at once, and simple first, because the simple ones are the best place for people to start:

1. **Wave one, simple and useful.** The factory has already started: a tools hub, image tools, the file encryptor, the HEIC converter, the SSH key generator and the video recorder, plus two new ones, what is my IP and what am I leaking. Next in this wave: the file hasher, the friendly key generator, a random password, the markdown viewer and video split and trim.
2. **Wave two, secrets and vaults.** Share a secret as a QR code, with public keys underneath, so that I can hand someone a QR code, they put their secret in, and only I can read what comes back ([a secret is a QR code](/articles/a-secret-is-a-qr-code.html)); then the vault browser and send and receive.
3. **Wave three, audio and video.** Transcription, voice memos, the media probe, the recorder, the editor and the publisher.
4. **Wave four, AI and agents.** Chat, the agentic loop, the model compatibility matrix and the deck and infographic generators, each a site that shows agents at work.

## Components, pulled out {#components}

The tools were already broken into components, which makes the refactor easier: the key generator, the vault picker and sync status, the send and receive primitive, the language model request, output and token views, the audio recorder and transcript, the tree view, the header. These become a component library of their own, each component versioned and documented, and each tool site uses a pinned version. Fix a component once, and every tool that chooses to can take the fix.

## Versions, pinned {#versions}

!shot tls-model.webp | images/ | One site per tool: latest and pinned versions, signed hashes kept apart, and a team of teams. | concept

The versioning model is one we have used before, and the tools repository already half follows it, with folders such as `tools/v0/v0.1/v0.1.70`. Each tool site publishes two kinds of folder. `latest/` always holds the newest code, and is overwritten at each release, with the history in git. Beside it, every release is pinned in its own folder, `v0/v0.1/v0.1.5/` and so on, never changed again, holding the same files and what goes with them: its security controls, its architecture, its guidance. Served with CORS from GitHub Pages, any other site or agent can consume a pinned version, or latest. I want to move some of my APIs to the same model.

## Signed hashes, kept apart {#hashes}

A repository can be compromised, and a pinned version is only as safe as the repository it sits in. So at each release, a manifest of every file's hash is signed with a key the tool's repository does not hold, and committed to a separate hashes repository. A consumer checks the files against the signed manifest before using them. If a tool's repository is compromised, its files stop matching a signature the attacker cannot make, and the compromise shows instead of spreading. It is the same thinking as this newsroom's signed commits, one step further out.

## A team of teams {#teams}

This is a good place for agents of agents. Each tool gets a small team of its own: a maker, a writer and a reviewer. Tools of a family share a family team, which owns their components and reviews their releases. Above them, a tools conductor holds the briefs. A change that touches many tools, a new header, a component fix, a security control, becomes one brief from the conductor, planned by each family and applied and released by each tool team. Three levels down, and we see how it works. There is capacity to try it: the accounts bought for the team for Web Summit still have about a month to run.

## What this does not claim {#limits}

- **The tool sites do not exist yet,** beyond the factory's first requests.
- **The signed-hash scheme is a design,** to be built and reviewed.
- **The counts are from the repository on 19 November 2026,** whose last change was on 1 September.

## Where this comes from {#sources}

My own thinking, in writer-10's session on 19 November 2026, and a read of [SGraph-AI__Tools](https://github.com/the-cyber-boardroom/SGraph-AI__Tools), its tool manifests and components, and the AgentiCCells site factory's requests of 19 November. Related: [explorer coding](/articles/explorer-coding.html), [what is a sovereign website](/articles/what-is-a-sovereign-website.html), [a website with a team inside](/articles/a-website-with-a-team-inside.html), [a secret is a QR code](/articles/a-secret-is-a-qr-code.html), [watch your website being built](/articles/watch-your-website-being-built.html).
