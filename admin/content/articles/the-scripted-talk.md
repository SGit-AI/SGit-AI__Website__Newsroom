---
title: The scripted talk: a presentation as a timeline that plays on a clock, the two vaults it grows out of, and a player built for tonight's ten minutes
date: 2026-10-15
author: Dinis Cruz
author_url: about/index.html
summary: I usually give a talk by reading it, with the slides behind me. For a short slot tonight I want to try something else: a talk that is completely scripted, where the slides, the builds, the animations and even the demo play on a clock, and I speak to them instead of reading from them. This grows out of two talks already published as vaults on sgit.ai. The Black Hat Europe 2025 keynote made the slides data: 26 slides in one JSON file that the app reads at load time, with ten versions of the slide system beside it. The VoiceDebrief pitch added a presenter with per-slide timings, a countdown and speaker notes, built from a template by a script. The next step is to make the whole talk a timeline. This site's agent built a first version: one HTML file that plays a file of beats, each with a start, a duration, a slide and the words to say, with builds, a terminal that types a command and prints its recorded output, tables that reveal row by row, video, and a presenter view with the words, the seconds left and what comes next. A rehearsal mode records planned against actual times. The first timeline is the five-minute demo for ruv.sgit.ai, the newest site in the sgit family, built for tonight's Agentic Engineering Live with rUv in London. And Claude Motion, which Anthropic released in beta on 8 October, makes the animations the same way: as code, exported as MP4.
version: v0.12.61
license: https://creativecommons.org/licenses/by/4.0/
tags: presentations, talks, slides, scripting, animation, claude-motion, vault-apps, sgit, ruv, agentics, brief, article
status: published
---

!shot tp-architecture.webp | images/ | A scripted talk, from the memo to the room: a file of beats, each with its slide and its words; a player that turns it into slides on a clock; the audience sees the slide, the speaker sees the words, the time left and what comes next; a rehearsal records planned against actual times. Dashed boxes are proposed. | architecture

## In short {#in-short}

- **A talk as a timeline.** Slides, builds, animations and the demo play on a clock; the speaker speaks to them.
- **It grows out of two vaults.** Black Hat made the slides data; the VoiceDebrief pitch added timings and a presenter.
- **A player, built and tested.** One HTML file, a file of beats, a presenter view and a rehearsal mode.
- **The demo is recorded truth.** The terminal types the command and prints the output the real run produced.
- **Animations as code.** Claude Motion, Manim or Remotion: editable, versioned, exported as MP4.
- **First use, tonight.** The five-minute demo for ruv.sgit.ai, at Agentic Engineering Live with rUv in London.

## Why script a talk {#why}

I usually read my presentations, with the slides behind me as a backdrop. It works, but it splits the attention: the audience reads the slide while I read the script, and the two drift apart. For a short slot, where every second counts, I want to try the opposite: a talk that is completely scripted. The slides, the builds, the animations and the demo are written down as a timeline and play on a clock, and I speak to them. The pace is set before I walk on, the demo cannot fail live, and the whole thing can be rehearsed, measured and changed like code.

## Where it comes from {#lineage}

!shot tp-lineage.webp | images/ | Three talks, one direction: Black Hat Europe 2025 made the slides data; the VoiceDebrief pitch added a presenter with timings, notes and a countdown; the player for tonight makes the whole talk a timeline that plays on a clock. All three live in vaults. | comparison

This is the third step of something I have done twice before, and both are published as vaults on sgit.ai.

The first was [AI vs. AI](https://sgit.ai/demos/vaults/blackhat-eu-2025/index.html), my keynote at the AI Security Summit at Black Hat Europe on 9 December 2025. The deck was fully generated from scripts. Its 26 slides, in seven layouts, are one JSON file: "The app reads it through the vault bridge at load time, so a content change needs no rebuild." The vault also carries the slide system itself at ten versions, six PDF exports, and the eight research papers the talk was built from. The lesson I took from it is the one that matters here: content is data, the renderer is code, and they change separately.

The second was the [VoiceDebrief pitch](https://sgit.ai/demos/vaults/voicedebrief-pitch/index.html) to Founder Institute on 2 September 2026: a presenter app with per-slide target timings, a three-minute countdown and speaker notes, built from a template by a script in the vault, with the spoken script extracted from the notes and the PDF and PPTX regenerated on every release. That added time to the slides: each one knew when it should be on screen.

The next step is to let the clock drive. Instead of a deck with timings beside it, a timeline with slides on it.

## The player {#player}

!shot tp-presenter.webp | images/ | The prototype's presenter view, at 2:58 of the five-minute demo: the slide on the left, with every row of the table revealed; on the right, the words for this beat, the seconds left and what comes next; along the bottom, the clock and a progress bar marked at every beat. | comparison

This site's agent built a first version, and it is deliberately small: one HTML file and one JSON file, no build. It is a page made for one moment, which [Custom UIs are not the exception](/articles/custom-uis-are-not-the-exception.html) argued is normal now: "A custom interface per message or moment is not an exception". The talk is a list of beats. Each beat has a start in seconds, a duration, a title, the words to say, and a slide with a layout:

- **statement**: a line of text, with builds that appear at set seconds;
- **terminal**: a command typed out character by character, then the output the real run produced;
- **table**: rows revealed every few seconds;
- **bullets**, **video**, for example an MP4 exported from Claude Motion, and **iframe**, for a live page.

A clock drives everything. Press Space and it plays; the beat at the current second is on screen, its builds appear at their offsets, and the next beat starts on time without a click. The arrow keys jump between beats if the room needs a moment. P opens the presenter view: the words for this beat, the seconds left, highlighted in the last five, and what comes next. R starts a rehearsal, which records when each beat actually began; when it stops, it saves a file of planned against actual times, the evidence of whether the script fits the slot.

It was tested in Chromium: every beat came on at its second, the builds and rows appeared on schedule, the terminal finished typing and then printed, the arrows jumped forward and back, it stopped at 5:00, and the page raised no errors. A version with the talk inlined opens straight from a file, with no server and no network, which is the version to carry into a room with bad wifi.

## The demo is recorded truth {#demo}

The part I like most is the terminal. A live demo is where talks go wrong: the network, the package cache, the one command that behaves differently on stage. In a scripted talk, the command is typed on the timeline and the output is the one the real run produced, captured beforehand and kept with the talk. That is not faking the demo. It is the same principle as every vault on sgit.ai: the evidence is recorded, versioned and inspectable, and anyone can run the command again from the vault and compare.

## Animations as code {#motion}

The memo's transcription garbled two names. The first is clearly Claude Motion, which Anthropic [released in beta](https://claude.com/resources/articles/dashboards-and-motion) on 8 October 2026 for Team and Enterprise plans: "Claude writes code that animates your text, charts, shapes, and images, so you can change any word, number, or timing." It "doesn't use a video generation model", and the result downloads as an MP4. I could not make out the second word with confidence; the code-based animation tools it most likely refers to are Manim, the Python library for mathematical animation, and Remotion, which makes video from React components, and both are already used with Claude Code through community skills.

They all fit the timeline the same way. An animation made as code can be edited a word or a number at a time, versioned beside the talk, exported as an MP4, and placed on a beat. The talk stays data from end to end: the words, the slides, the animations and the recorded output, each in a file, each with a history.

## First use: ruv.sgit.ai {#ruv}

The first timeline is a real one. [ruv.sgit.ai](https://ruv.sgit.ai/index.html) is the newest site in the sgit family, built on 14 October for Agentic Engineering Live with Reuven Cohen, rUv, in London on 15 October. It shows sgit vaults and agent behaviour policies running inside his stack, Ruflo, RuVector, RVM and MetaHarness, as six proofs of concept, and it already has a [five-minute demo](https://ruv.sgit.ai/demo.html) written in five beats. The agent turned those beats into the first `talk.json`: the claim, Ruflo's default saying yes to sending email, the same eleven actions with and without the behaviour policy, read from the site's own data, memory with history across runners, and the ask. A ten-minute version is the same file with more beats.

## A brief for the talk vault {#brief}

1. **The talk vault.** `talk.json`, the player, the assets and every rehearsal file in one vault, with a published read key once the talk is given.
2. **Recorded demos.** A script that runs each demo command and saves its output beside the beat that shows it.
3. **Motion on beats.** Animations made in Claude Motion, Manim or Remotion, exported as MP4 and referenced by path.
4. **Rehearsal as a test.** A rehearsal file committed after each run-through, and a check that fails if any beat runs more than ten seconds over.
5. **Exports.** The same timeline rendered to a PDF, one page a beat, and to one MP4 of the whole talk.
6. **A vault app.** The player served from the vault itself, as the Black Hat deck is, so the talk and its evidence travel as one object.

## What this does not claim {#limits}

- **It has not been given yet.** The player was tested in a browser, not in a room.
- **Scripted is not read.** The words are in the presenter view; whether to read them is the speaker's choice.
- **The second animation tool is a guess.** The transcription was unclear.
- **Claude Motion was not used here.** Its details are from Anthropic's pages; it is in beta on Team and Enterprise plans.
- **The exports and the talk vault are proposed.** The player, the timeline and the tests exist.

If you give talks and want yours to be a timeline with its evidence attached, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo of mine on 14 October 2026, written by this site's agent in the voice of this site; the argument and the editorial responsibility are mine. The player was built and tested by this site's agent on 15 October 2026, from the two published vaults, which it cloned with their read keys, and from ruv.sgit.ai's demo script and data. From sgit.ai: [AI vs. AI, Black Hat Europe 2025](https://sgit.ai/demos/vaults/blackhat-eu-2025/index.html) and [A three-minute pitch](https://sgit.ai/demos/vaults/voicedebrief-pitch/index.html). Anthropic, [Build live dashboards and animate explainers with Claude](https://claude.com/resources/articles/dashboards-and-motion), 8 October 2026, and [Get started with Claude Motion](https://support.claude.com/en/articles/17454997-get-started-with-claude-motion); [ruv.sgit.ai](https://ruv.sgit.ai/index.html) and its [demo](https://ruv.sgit.ai/demo.html). Read on 15 October 2026.
