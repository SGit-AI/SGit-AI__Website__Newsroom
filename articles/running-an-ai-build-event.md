# Running an AI build event where everyone ships something someone else can use: guidance on the primitives, from a browser-only workspace to synthetic users testing the day before it happens, sgit.ai

> The best way to get people excited about AI is to tell them: come along, bring your laptop and a problem, a spreadsheet, a process, and let's build something. I have been to many events like that, and organised many, including the Open Security Summit, which treated every participant as a presenter. This is guidance on how I would run one now. The hardest thing is not getting someone to build something; it is getting them to build something somebody else can use. So the day should be designed around shipping. Five primitives make the difference. Use AI and agentic workflows to run the event itself, or you are teaching advanced technology without using it: know who is coming, and prepare materials, playbooks and handouts for them. Give people a workspace that needs only a browser: nothing to install, no payments on the day, no database. Prepare cases and recipes in advance, like ready-made spreadsheets, so nobody faces a blank page. Have villagers in the room, people who help publish and share, and let AI do the supporting work: a synthetic user that tests each app, a description of what it does, a website for it. And test the event before it happens, with synthetic users going through the onboarding. Underneath it is a simple architecture, everything in the browser, everything on GitHub Pages, which handles most simple use cases and gives each app a page that says what it does and the thing itself. There are five stages, from typing something and seeing it work to an app other people use, and the day is a success when people experience the feedback loop.

*Source: <https://newsroom.sgit.ai/articles/running-an-ai-build-event.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Running an AI build event where everyone ships something someone else can use: guidance on the primitives, from a browser-only workspace to synthetic users testing the day before it happens

# Running an AI build event where everyone ships something someone else can use: guidance on the primitives, from a browser-only workspace to synthetic users testing the day before it happens

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-31 · [article v1.0.0](versions/running-an-ai-build-event.md) · [newsroom v0.14.26](https://newsroom.sgit.ai/admin/versions.html) · eventsai-adoptiononboardinggithub-pagessynthetic-userseducationguidancearticle

***Abstract:** The best way to get people excited about AI is to tell them: come along, bring your laptop and a problem, a spreadsheet, a process, and let's build something. I have been to many events like that, and organised many, including the Open Security Summit, which treated every participant as a presenter. This is guidance on how I would run one now. The hardest thing is not getting someone to build something; it is getting them to build something somebody else can use. So the day should be designed around shipping. Five primitives make the difference. Use AI and agentic workflows to run the event itself, or you are teaching advanced technology without using it: know who is coming, and prepare materials, playbooks and handouts for them. Give people a workspace that needs only a browser: nothing to install, no payments on the day, no database. Prepare cases and recipes in advance, like ready-made spreadsheets, so nobody faces a blank page. Have villagers in the room, people who help publish and share, and let AI do the supporting work: a synthetic user that tests each app, a description of what it does, a website for it. And test the event before it happens, with synthetic users going through the onboarding. Underneath it is a simple architecture, everything in the browser, everything on GitHub Pages, which handles most simple use cases and gives each app a page that says what it does and the thing itself. There are five stages, from typing something and seeing it work to an app other people use, and the day is a success when people experience the feedback loop.*

Five stages from never having done this to something others use, and the primitives that carry people up them.

## In short

- **The best format is simple:** bring your laptop and a problem, and let's build something.
- **The hard part is shipping:** getting someone to build something that somebody else can use.
- **Use AI to run the event itself,** from knowing who is coming to preparing their materials.
- **A browser-only workspace:** nothing to install, no payments on the day, no database.
- **Prepared cases and recipes,** so nobody faces a blank page.
- **Villagers and synthetic users in the room,** to help publish, test and describe each app.
- **Test the event before it happens,** and make the feedback loop the thing people take home.

## The format that works

I have been to a lot of events that try to get people excited about AI, and I have organised many events, including the [Open Security Summit](the-open-security-summit-and-its-debt.md), which treated every participant as a presenter rather than an audience. The format I believe in most is the simplest: come along, bring your laptop and something from your work, a problem, a spreadsheet, a process, and let's build something.

It works because it starts from the participant's own world, not from the technology. What follows is guidance on making that format as effective as it can be now, with the tools that exist today. It is not about any one event; it is the set of primitives I would put in place before the doors open.

## Ship something someone else can use

The most challenging part of these days is not getting somebody to build something. It is getting them to build something that somebody else can use. A demo on your own laptop is a start; an app that the person at the next table can open and use is a different experience, and it is the one that changes how people think.

So design the day around shipping. Every participant should leave having pushed something, shared a link, and watched someone else in the room use it. That moment, someone else using what you made an hour ago, is the feedback loop, and it is what people remember.

## Use AI to run the event

If the event is about AI and agentic workflows, it should be run with them. Otherwise you are talking about advanced technology without using it yourself.

- **Know who is coming.** A registration form that asks what people do and what they would like to build.
- **Prepare materials for them.** An agent can turn each answer into a short, customised starting brief, and match each person to a prepared case.
- **Playbooks and handouts,** written and checked before the day, for each stage of the build.
- **Follow-up,** drafted for each person after the day, with their app's link and a next step.

## A browser and nothing else

The onboarding is everything. The first minutes decide whether someone leans in or checks their phone, so remove every obstacle before the day:

- **Nothing to install.** Everything happens in a browser.
- **No payments on the day.** Credits, free tiers or shared accounts arranged in advance, so nobody stops to enter a card.
- **No database.** Data stays in the browser, or in a file published with the app.

## Cases and recipes, ready before the day

Nobody should face a blank page. Prepare cases in advance: realistic spreadsheets and documents with invented data, each mapped to an app it can become, with a recipe of prompts that gets there. The [Spreadsheet to App pack](spreadsheet-to-app-sessions.md), five examples and five prompts in a public vault, is one way to do it.

This is the point I made in [Generation Z Developers](generation-z-developers-again.md): what helps people start is easy examples and easy recipes, things that work the first time and can be changed from there.

## Villagers and synthetic users in the room

The participants are the explorers. Around them, you want two kinds of help:

- **Villagers:** people in the room whose job is to help publish, share and fix, so a participant's app gets from their tool to a link in minutes. It is the [villager](villager-services-for-explorer-coders.md) role, on the day.
- **AI doing the supporting work:** once someone has built an app, another agent can create a synthetic user to test it, another can write a description of what it does, and another can turn that into a small website that presents it. Each of these used to take a team; now each is a prompt.

## A simple architecture

For almost everything built in a day, the same architecture holds: no major databases, everything runs in the browser, and everything is published from GitHub with GitHub Pages. It handles most simple use cases, and it gives each app, in one go, a website that describes what it is supposed to do and the thing itself, doing something valuable.

## Five stages

People arrive at very different points, so plan for five stages and let each person climb as far as they can:

1. **Type and see it work.** Someone who has never done this types a request and sees something appear.
2. **Change it.** They ask for more and watch it change: the loop begins.
3. **Share a link.** Someone else opens it. This is the step the day is for.
4. **A website.** On GitHub Pages, saying what it does, with the app itself.
5. **Used by others.** Deployed, tested by a synthetic user, and used by a second real person.

The aim is to make it so simple that someone who has never done this still gets a great deal of value, while someone who has done it before can go to stage five.

## Test the event before it happens

You can even try the day out before anyone arrives. Synthetic users, agents given the profile of the people who registered, can go through the onboarding, the cases and the recipes, and say where they got stuck. Their feedback arrives before the first participant does, and the materials are better for it.

## What the day is for

All of this serves one experience: the power of the feedback loop. Build something, ship it, watch someone use it, change it, ship it again. People who feel that loop once go home and do it with the next spreadsheet, and the next.

## What this does not claim

- **It is guidance, from experience,** not a measured method; the five stages are a model, not a standard.
- **It is not about any particular event.** It draws on many, and on events I have organised.
- **Free tiers and credits change,** and need arranging for each event.
- **My interest:** I build tools these events could use, and I offer villager services.

## Where this comes from

- My voice memos of 31 October 2026, word for word in `admin/notes/2026-10-31__running-ai-build-events/` in this site's repository.
- Related: [Spreadsheet to App](spreadsheet-to-app-sessions.md), [from a checklist to an app you calibrate](from-a-checklist-to-an-app.md), [villager services for explorer coders](villager-services-for-explorer-coders.md), [the Open Security Summit and its debt](the-open-security-summit-and-its-debt.md), [Generation Z Developers (AI edition)](generation-z-developers-again.md).

## Threads

Startups & strategySite & engineering[This article as a graph →](graphs.md#running-an-ai-build-event)

### Builds on

- [The Open Security Summit and its debt: how a summit that treated every participant as a presenter stalled on its own website, what the code shows, and why agents make it worth restarting](the-open-security-summit-and-its-debt.md) How technical debt stalled the Open Security Summit's website and follow-up, what the repositories show, and why agents make a restart worthwhile.
- [Spreadsheet to App: a session programme for Algarve Evolution, with five example spreadsheets, five prompts, a mock event and a public vault, so nobody arrives needing a problem to solve](spreadsheet-to-app-sessions.md) Spreadsheet to App: a session programme for Algarve Evolution, with five examples, five prompts, a mock event and a public vault.
- [Generation Z Developers (AI edition): the 2018 book that said act like you are part of the company, what it got right, and a new edition for the people I want to help](generation-z-developers-again.md) My 2018 book for young developers, 60% done, its outlines since written here as articles, and an AI edition, dated October 2026, made first.
- [Villager services for explorer coders: the founders with ten years of checklists will build the apps, and the business is everything behind them, sold in finite packs, never as rent](villager-services-for-explorer-coders.md) Villager services for explorer coders: founders with ten years of checklists build the apps; we sell everything behind them in finite packs.
- [From a checklist to an app you calibrate: your list is already an information system, so build its smallest version in half an hour, use it, log every run, and let it grow](from-a-checklist-to-an-app.md) From a checklist to an app you calibrate: build the smallest version in half an hour, use it tomorrow, log every run, and let it grow.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 349 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=349)

**Posting this article on LinkedIn?** The cover is [running-an-ai-build-event.jpg](banners/running-an-ai-build-event.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/running-an-ai-build-event.html)*
