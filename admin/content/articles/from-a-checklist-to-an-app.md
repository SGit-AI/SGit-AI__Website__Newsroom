---
title: From a checklist to an app you calibrate: your list is already an information system, so build its smallest version in half an hour, use it, log every run, and let it grow
date: 2026-10-31
author: Dinis Cruz
author_url: about/index.html
summary: At the Vibathon in Faro today, two participants showed me their system for closing up a second home before travelling back to another country: a document with a list of actions, the important ones in bold. This article is the advice I gave them, written so that next time someone shows me a list like that, I can send the link. The first point is that a list like that is already an information system. It holds years of experience, of getting it right, getting it wrong and forgetting things, and the bold is already its priority system. What it lacks is everything around it. It has no history, so nothing is learned from each time it is used; it relies on memory and on its owners to maintain it; and its interface is a flat list, when what you want is an app that shows the first three things, then, once they are done, the next five. The tree is already in its owners' heads. So the advice is not to design the final app. It is to build the smallest useful version in half an hour, with Lovable or any model, deploy it, use it on the next run, keep a small file of what happened each time, and calibrate: these five matter more, if this then that, a step to add. The flat list becomes a tree because using it shows you where the branches are. Start with no database, the browser's own storage or a shared account, and keep anything confidential out, no address, no PIN codes, so that the internet can be the way you share it. The loop is the product.
version: v0.14.20
license: https://creativecommons.org/licenses/by/4.0/
tags: workflow, lovable, mvp, productivity, agents, advice, article
status: published
---

!shot cl-stages.webp | images/ | From a checklist to an app you calibrate: four stages, each usable the day it is built. | process

## In short {#in-short}

- **Your list is already an information system.** Years of experience, and the bold is its priority system.
- **What it lacks is history, memory and a good interface.** Nothing is learned from each time you use it.
- **Do not design the final app.** Build the smallest useful version in half an hour, and use it tomorrow.
- **Show only the bold first.** Then the next five, when those are done.
- **Keep a small file for every run.** That is the memory: what was used, skipped, and what happened.
- **Calibrate every time.** Priorities and "if this, then that" appear from use, and the list becomes a tree.
- **No database, nothing confidential.** The browser's storage or a shared account, and the internet to share it.

## You already have an information system {#system}

At the Vibathon Algarve today, two participants showed me how they manage closing up a second home before travelling back to another country: a document, not even a spreadsheet, with a list of actions. Do this, do that. Turn off the gas. Set the alarm. Call ahead so someone knows you are coming. The important ones are in bold.

That is an information system, and a good one. It condenses years of experience: things got right, things got wrong, things forgotten once and never again. The bold is its priority system, a way of saying look here first. And it relies on one intelligent agent to read it and act on it: you.

Many people have one of these, for a move, a trip, a launch or the end of every month. So this is the advice I gave, written down so I can send it the next time.

## What it is missing {#missing}

From a design point of view, the problem is not the list. It is everything around it.

- **It has no history.** Every time you go round the loop, nothing captures what happened, so you cannot learn from it.
- **It relies on memory,** and on you to maintain it.
- **It has little context.** Why a step is there, what depends on it, when it matters.
- **Its interface is flat.** What you really want is a small app that says: here are the first three things. Done. Now here are the next five. Done.

That is a tree, and the tree is already in your head: you compensate for the flat list every time you use it. Which makes it a perfect place to start, because you already know what the result should feel like.

## Do not aim for the final app {#mvp}

The focus is on shipping something all the time, not on a long tangent that might produce something great at the end. Each step should solve a little of the problem.

I think of it as a question: what is the simplest thing you can build right now that is built through an LLM, deployed, usable, and adds value? That is the minimal viable product. Not a mock-up; something you can use on the next run.

Use one of the models as the intelligent agent that builds it: Lovable, with the credits the Vibathon gave every participant, or Mistral, ChatGPT or a local model. Ask it for an interface that starts to codify your workflow. If the bold items are the ones that matter, the first thing the app shows is just the bold ones. Build it in the next half hour, and make sure the other person can use it too.

## The loop is the product {#loop}

!shot cl-loop.webp | images/ | The loop is the product: build, publish, use, log the run, calibrate, and go round again. | process

The most important thing is not the app. It is a workflow that lets you find the app, and the feedback loop is what does it. As soon as you see just the bold items, you will say: of these twenty, these five matter more. So you prioritise them. Then you will notice that if you do this, you have to do that. So you codify it. Step by step the flat file becomes a tree, a set of "if this, then that", and the interface shows it.

That only happens if you calibrate every time you use it. This is never about a final solution; it is about one you will use tomorrow. It will work, and it will fail, and you will come back and say: now I need this, now I need that. That loop is how you arrive at a really good workflow, and the AI's part is the ability to build each version in minutes. Once you have something you can change and use, you have a positive feedback loop, and that is the hard part.

## Memory is a small file per run {#memory}

Learning here does not mean the model learning. It means this: when you go round the loop once, you store what happened in a small file. What you used, what you skipped, what went wrong, what you added. Next time, another small file. Those files are your memory: at each moment, what was used and what happened. The interface lets you choose from them, and the next version is built from them.

That is the difference from the document you have today, which has no history, no memory and no learning.

## Start with no database, and nothing confidential {#simple}

Two pieces of guidance to give the model when you start:

- **No database at first.** Keep the data in the browser's own storage. If you need to share it, use something you already have, such as a shared Google account, before building anything.
- **Keep anything confidential out,** at least in the first phase. Most of a list like this is common sense: turn off the gas, check the shutters, call ahead. The confidential parts are few: the address, and please never the PIN codes. Take those out.

I come from cybersecurity, and the moment there is private data, you have to protect it: a system, access, all of those things. If the first version holds nothing confidential, it can be public, and then the internet is your way of collaborating: you make a change, you publish it, and that is your distribution. Lovable works that way: make the first version, publish it, use it. If you can share one account, collaborate there; if not, separate accounts work too.

## What this does not claim {#limits}

- **It is advice, not a method with evidence.** It is how I work, and it is the loop behind this newsroom.
- **The example is general.** The participants are not named, and the list in the figure is an illustration, not theirs.
- **Lovable is one option.** Any model that can build and deploy a small web app will do.

## Where this comes from {#sources}

- My conversation of 31 October 2026 at the Vibathon Algarve 2026, transcribed word for word in `admin/notes/2026-10-31__checklist-to-app/memo-01.md` in this site's repository.
- Related: [Vibathon Algarve 2026, and Algarve Evolution](/articles/vibathon-algarve-2026.html), [Lovable with SHarness](/articles/lovable-with-sharness.html), [websites you own](/articles/websites-you-own.html).
