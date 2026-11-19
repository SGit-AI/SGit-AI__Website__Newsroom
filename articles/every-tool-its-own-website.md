# Every tool its own website: turning the 49 browser tools of tools.sgraph.ai, each built because I had a problem, into sovereign websites of their own, with a theme, documentation and a small agent team each, released in waves from the simplest, with shared components pulled out, pinned versions and signed hashes kept apart, and a team of teams to keep them all moving, sgit.ai

> Every tool on tools.sgraph.ai exists because I had a problem and built something for it: encrypting a file, making an SSH key, opening a vault in the browser, transcribing a voice note, splitting the audio out of a video. There are 49 of them now, and about 90 shared components, and some became better than anything else I use. They also show the limit of an explorer project: one repository, one site, harder and harder to maintain. And they answer a frustration with the web itself, where simple things are buried under ads and hidden behind sign-ups. Sovereign websites are the place to put them. Each tool gets its own site at its own address, self-contained, documented and good to look at, on GitHub Pages for pennies, forkable, open to a maintainer who wants to take it on, and with a small team of agents inside, and a model where it helps, even one running in the browser. This piece maps the tools by family, proposes the order, starting with the simple ones the factory has already begun, a shared component library, the versioning model the tools already half use, latest and pinned versions with their security notes, signed hashes kept in a separate repository so a compromised site shows, and a team of teams to run it all.

*Source: <https://newsroom.sgit.ai/articles/every-tool-its-own-website.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Every tool its own website: turning the 49 browser tools of tools.sgraph.ai, each built because I had a problem, into sovereign websites of their own, with a theme, documentation and a small agent team each, released in waves from the simplest, with shared components pulled out, pinned versions and signed hashes kept apart, and a team of teams to keep them all moving

# Every tool its own website: turning the 49 browser tools of tools.sgraph.ai, each built because I had a problem, into sovereign websites of their own, with a theme, documentation and a small agent team each, released in waves from the simplest, with shared components pulled out, pinned versions and signed hashes kept apart, and a team of teams to keep them all moving

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-19 · [article v1.0.0](versions/every-tool-its-own-website.md) · [newsroom v999.0.0](https://newsroom.sgit.ai/admin/versions.html) · toolssovereign-websiteopen-sourcecomponentsversioningagent-teamsarticle

***Abstract:** Every tool on tools.sgraph.ai exists because I had a problem and built something for it: encrypting a file, making an SSH key, opening a vault in the browser, transcribing a voice note, splitting the audio out of a video. There are 49 of them now, and about 90 shared components, and some became better than anything else I use. They also show the limit of an explorer project: one repository, one site, harder and harder to maintain. And they answer a frustration with the web itself, where simple things are buried under ads and hidden behind sign-ups. Sovereign websites are the place to put them. Each tool gets its own site at its own address, self-contained, documented and good to look at, on GitHub Pages for pennies, forkable, open to a maintainer who wants to take it on, and with a small team of agents inside, and a model where it helps, even one running in the browser. This piece maps the tools by family, proposes the order, starting with the simple ones the factory has already begun, a shared component library, the versioning model the tools already half use, latest and pinned versions with their security notes, signed hashes kept in a separate repository so a compromised site shows, and a team of teams to run it all.*

49 tools, each made for a problem: grouped by family, with the first ones the factory has started.

## In short

- **49 tools, about 90 components,** each built because I had a problem.
- **One tool, one sovereign website:** its own address, documentation, design and agent team.
- **Simple first:** encrypt a file, make an SSH key, what is my IP; the factory has started.
- **Shared components pulled out** into a library of their own, each versioned.
- **Pinned versions, and signed hashes kept apart,** so a compromised site shows.
- **A team of teams** to change many tools at once.

## Every tool was a problem

When I look at [tools.sgraph.ai](https://tools.sgraph.ai/), and its development version [dev.tools.sgraph.ai](https://dev.tools.sgraph.ai/), I remember each one, because each was a problem I had: I needed to encrypt a file, so I built a file encryptor; I needed an SSH key, so an SSH key generator; I needed to split the audio out of a video, so a video tool; I needed to read a vault without a command line, so a vault browser. It was the first time I really felt that if you have a challenge, you might as well build the tool for it. Some of those tools became better than anything else I use.

They also answered a frustration. The web became convoluted. Go looking for something as simple as your IP address, a random password or a file's hash, and you find pages riddled with ads, features you did not ask for, and the useful part hidden. I would pay a little for a page that does one thing well; most of these should have a small payment, and let people choose. What I wanted was very simple websites that each do one thing very well. Some could become businesses; others are just good tools.

## What is there

The repository behind the site, [SGraph-AI__Tools](https://github.com/the-cyber-boardroom/SGraph-AI__Tools), holds 49 tools, from version 0.1.4 to 0.1.70, and about 90 shared components, from a key generator and a vault picker to a whole set for language models and for audio. Grouped by family:

- **Keys and secrets (5):** file encryptor, file hasher, friendly key generator, SSH key generator, and an authentication test bed.
- **Vaults and sending (14):** a vault browser, editor and manager, a vault opened in Python in the browser, send and receive, a send simulator, the sg-send command line in the browser, a speed test, and the folder, file system and tree tools behind them.
- **AI and agents (10):** chat, one-shot requests, a multi-agent chat, an agentic loop with tools, an agent that can act on your machine through a bridge, an LLM development environment, a model compatibility matrix, an OpenRouter account manager, an infographic generator and a slide deck generator.
- **Audio and video (13):** transcription from a file or live, voice memos with local Whisper, a media probe, a narrated review, a video recorder, a video creator, a multi-clip editor, a video publisher, video split and trim, and three YouTube tools.
- **Documents and images (5):** image tools, a HEIC converter, a markdown viewer, Mermaid diagrams and a Python console.
- **Publishing and messages (2):** a LinkedIn publisher and a WhatsApp desk.

## Why one site each

They are a typical explorer project ([explorer coding](explorer-coding.md)): fast while I was exploring, then slower, because one repository and one site for 49 tools gets messy to update and maintain. The refactor is one I like from an engineering point of view: individual, self-sufficient parts. Each tool as its own [sovereign website](what-is-a-sovereign-website.md):

- **Its own address and its own repository,** so it can be found, linked, forked and maintained alone.
- **Self-contained and documented:** what it does, what stays in your browser, how it works.
- **Good to look at,** with the same design family across all of them, which the old site never quite had.
- **Cheap to run:** a static site on GitHub Pages costs almost nothing, and runs inside a company as easily as outside.
- **Open to a maintainer:** I would like people to take some of these on, the video editor most of all, and a repository of its own makes that easy.
- **With a team of agents inside,** to keep it working and to improve it ([a website with a team inside](a-website-with-a-team-inside.md)).

## A little intelligence in each

Every tool can now come with a small agent, and that changes what a simple tool can be: a markdown viewer that summarises, an image tool that suggests what to redact, a transcriber that writes the notes. Where it can, the model should run in the browser or on the device: the voice memo tool already transcribes with Whisper locally. A month ago, running a model in the browser was still clunky; a dedicated site for it, with one model and one job, is a good tool in its own right ([watch your website being built](watch-your-website-being-built.md)).

## The order

Not all at once, and simple first, because the simple ones are the best place for people to start:

1. **Wave one, simple and useful.** The factory has already started: a tools hub, image tools, the file encryptor, the HEIC converter, the SSH key generator and the video recorder, plus two new ones, what is my IP and what am I leaking. Next in this wave: the file hasher, the friendly key generator, a random password, the markdown viewer and video split and trim.
2. **Wave two, secrets and vaults.** Share a secret as a QR code, with public keys underneath, so that I can hand someone a QR code, they put their secret in, and only I can read what comes back ([a secret is a QR code](a-secret-is-a-qr-code.md)); then the vault browser and send and receive.
3. **Wave three, audio and video.** Transcription, voice memos, the media probe, the recorder, the editor and the publisher.
4. **Wave four, AI and agents.** Chat, the agentic loop, the model compatibility matrix and the deck and infographic generators, each a site that shows agents at work.

## Components, pulled out

The tools were already broken into components, which makes the refactor easier: the key generator, the vault picker and sync status, the send and receive primitive, the language model request, output and token views, the audio recorder and transcript, the tree view, the header. These become a component library of their own, each component versioned and documented, and each tool site uses a pinned version. Fix a component once, and every tool that chooses to can take the fix.

## Versions, pinned

One site per tool: latest and pinned versions, signed hashes kept apart, and a team of teams.

The versioning model is one we have used before, and the tools repository already half follows it, with folders such as `tools/v0/v0.1/v0.1.70`. Each tool site publishes two kinds of folder. `latest/` always holds the newest code, and is overwritten at each release, with the history in git. Beside it, every release is pinned in its own folder, `v0/v0.1/v0.1.5/` and so on, never changed again, holding the same files and what goes with them: its security controls, its architecture, its guidance. Served with CORS from GitHub Pages, any other site or agent can consume a pinned version, or latest. I want to move some of my APIs to the same model.

## Signed hashes, kept apart

A repository can be compromised, and a pinned version is only as safe as the repository it sits in. So at each release, a manifest of every file's hash is signed with a key the tool's repository does not hold, and committed to a separate hashes repository. A consumer checks the files against the signed manifest before using them. If a tool's repository is compromised, its files stop matching a signature the attacker cannot make, and the compromise shows instead of spreading. It is the same thinking as this newsroom's signed commits, one step further out.

## A team of teams

This is a good place for agents of agents. Each tool gets a small team of its own: a maker, a writer and a reviewer. Tools of a family share a family team, which owns their components and reviews their releases. Above them, a tools conductor holds the briefs. A change that touches many tools, a new header, a component fix, a security control, becomes one brief from the conductor, planned by each family and applied and released by each tool team. Three levels down, and we see how it works. There is capacity to try it: the accounts bought for the team for Web Summit still have about a month to run.

## What this does not claim

- **The tool sites do not exist yet,** beyond the factory's first requests.
- **The signed-hash scheme is a design,** to be built and reviewed.
- **The counts are from the repository on 19 November 2026,** whose last change was on 1 September.

## Where this comes from

My own thinking, in writer-10's session on 19 November 2026, and a read of [SGraph-AI__Tools](https://github.com/the-cyber-boardroom/SGraph-AI__Tools), its tool manifests and components, and the AgentiCCells site factory's requests of 19 November. Related: [explorer coding](explorer-coding.md), [what is a sovereign website](what-is-a-sovereign-website.md), [a website with a team inside](a-website-with-a-team-inside.md), [a secret is a QR code](a-secret-is-a-qr-code.md), [watch your website being built](watch-your-website-being-built.md).

## Threads

Agents & policy[This article as a graph →](graphs.md#every-tool-its-own-website)

### Builds on

- [Explorer coding: a better name for what people call vibe coding, what it is good for, and the handover to villagers and town planners before anyone depends on it](explorer-coding.md) Call it explorer coding, not vibe coding: the best thing since the spreadsheet, the best brief there is, and not ready to be in line until villagers take it.
- [What is a sovereign website: defining the category the way serverless was defined, a website you own and can move, built only on commodity technology because one proprietary part anywhere in the middle is enough to lock you in, seven principles, a sovereignty maturity model from rented to proven, and the proof that the same site runs on every host, in Europe and on your own computer](what-is-a-sovereign-website.md) What a sovereign website is: owned and movable, commodity only, seven principles, a maturity model from rented to proven, and every host.
- [A website with a team inside: why a Sovereign Agentic Website is delivered not as a site but as a site with six or seven agents already set up and coordinated in its repository, a conductor, a designer, a writer, a developer, a reviewer, a translator and a keeper, each with a role and a behaviour policy, and what that means for the person who owns it](a-website-with-a-team-inside.md) A Sovereign Agentic Website comes with a team inside: seven agents set up and coordinated in the owner's repository, each with a behaviour policy.
- [Watch your website being built: a brief for a page that builds a first version of a sovereign website in the visitor's own browser, from a description or a voice note, with their own model key, showing every agent at work, every behaviour policy being applied and every penny it costs, then hands back a zip, the same brief run on several models side by side as evals, and the Web Summit demos it grows from](watch-your-website-being-built.md) A page that builds a first version of a sovereign website in your browser, showing every agent, behaviour policy and penny, then hands back a zip.
- [A secret is a QR code and a link to a public key: the workflow the QR experiment opens, who else already does this, and a format to share](a-secret-is-a-qr-code.md) Send a QR code and a link to a public key: the workflow the QR experiment opens, who already does this, and a format to share.

### Continued by

- [Websites for the moment: an experiment in letting an agent team keep building topical sites, around what people are looking for now, GTA VI on its launch day, Christmas posting dates, an advent of tools, the Kickstarter itself, each built in a day within a budget, every fact sourced, live for its moment and then archived, and a first calendar to start from](websites-for-the-moment.md) An agent team building topical websites around what people are looking for now, each built in a day within a budget and sourced.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 507 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=507)

**Posting this article on LinkedIn?** The cover is [every-tool-its-own-website.jpg](banners/every-tool-its-own-website.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/every-tool-its-own-website.html)*
