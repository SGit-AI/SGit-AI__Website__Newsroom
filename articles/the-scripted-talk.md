# The scripted talk: a presentation as a timeline that plays on a clock, the two vaults it grows out of, and a player built for tonight's ten minutes, sgit.ai

> I usually give a talk by reading it, with the slides behind me. For a short slot tonight I would like to try something else: a talk that is completely scripted, where the slides, the builds, the animations and even the demo play on a clock, and I speak to them instead of reading from them. This grows out of two talks already published as vaults on sgit.ai. The Black Hat Europe 2025 keynote made the slides data: 26 slides in one JSON file that the app reads at load time, with ten versions of the slide system beside it. The VoiceDebrief pitch added a presenter with per-slide timings, a countdown and speaker notes, built from a template by a script. The next step is to make the whole talk a timeline. This site's agent built a first version: one HTML file that plays a file of beats, each with a start, a duration, a slide and the words to say, with builds, a terminal that types a command and prints its recorded output, tables that reveal row by row, video, and a presenter view with the words, the seconds left and what comes next. A rehearsal mode records planned against actual times. The first timeline is the five-minute demo for ruv.sgit.ai, the newest site in the sgit family, built for tonight's Agentic Engineering Live with rUv in London. And Claude Motion, which Anthropic released in beta on 8 October, makes the animations the same way: as code, exported as MP4.

*Source: <https://newsroom.sgit.ai/articles/the-scripted-talk.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The scripted talk: a presentation as a timeline that plays on a clock, the two vaults it grows out of, and a player built for tonight's ten minutes

# The scripted talk: a presentation as a timeline that plays on a clock, the two vaults it grows out of, and a player built for tonight's ten minutes

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-15 · [article v1.2.0, 3 versions](versions/the-scripted-talk.md) · [newsroom v0.12.61](https://newsroom.sgit.ai/admin/versions.html) · presentationstalksslidesscriptinganimationclaude-motionvault-appssgitruvagenticsbriefarticle

***Abstract:** I usually give a talk by reading it, with the slides behind me. For a short slot tonight I would like to try something else: a talk that is completely scripted, where the slides, the builds, the animations and even the demo play on a clock, and I speak to them instead of reading from them. This grows out of two talks already published as vaults on sgit.ai. The Black Hat Europe 2025 keynote made the slides data: 26 slides in one JSON file that the app reads at load time, with ten versions of the slide system beside it. The VoiceDebrief pitch added a presenter with per-slide timings, a countdown and speaker notes, built from a template by a script. The next step is to make the whole talk a timeline. This site's agent built a first version: one HTML file that plays a file of beats, each with a start, a duration, a slide and the words to say, with builds, a terminal that types a command and prints its recorded output, tables that reveal row by row, video, and a presenter view with the words, the seconds left and what comes next. A rehearsal mode records planned against actual times. The first timeline is the five-minute demo for ruv.sgit.ai, the newest site in the sgit family, built for tonight's Agentic Engineering Live with rUv in London. And Claude Motion, which Anthropic released in beta on 8 October, makes the animations the same way: as code, exported as MP4.*

A scripted talk, from the memo to the room: a file of beats, a player on a clock, a speaker view and a rehearsal record.

## In short

- **A talk as a timeline.** Slides, builds, animations and the demo play on a clock; the speaker speaks to them.
- **It grows out of two vaults.** Black Hat made the slides data; the VoiceDebrief pitch added timings and a presenter.
- **A player, built and tested.** One HTML file, a file of beats, a presenter view and a rehearsal mode.
- **The demo is recorded truth.** The terminal types the command and prints the output the real run produced.
- **Animations as code.** Claude Motion, Manim or Remotion: editable, versioned, exported as MP4.
- **First use, tonight.** The five-minute demo for ruv.sgit.ai, at Agentic Engineering Live with rUv in London.

## Why script a talk

I usually read my presentations, with the slides behind me as a backdrop. It works, but it splits the attention: the audience reads the slide while I read the script, and the two drift apart. For a short slot, where every second counts, I would like to try the opposite: a talk that is completely scripted. The slides, the builds, the animations and the demo are written down as a timeline and play on a clock, and I speak to them. The pace is set before I walk on, the demo cannot fail live, and the whole thing can be rehearsed, measured and changed like code.

## Where it comes from

Three talks, one direction: Black Hat Europe 2025, the VoiceDebrief pitch, and tonight's player, all living in vaults.

This is the third step of something I have done twice before, and both are published as vaults on sgit.ai.

The first was [AI vs. AI](https://sgit.ai/demos/vaults/blackhat-eu-2025/index.html), my keynote at the AI Security Summit at Black Hat Europe on 9 December 2025. The deck was fully generated from scripts. Its 26 slides, in seven layouts, are one JSON file: "The app reads it through the vault bridge at load time, so a content change needs no rebuild." The vault also carries the slide system itself at ten versions, six PDF exports, and the eight research papers the talk was built from. The lesson I took from it is the one that matters here: content is data, the renderer is code, and they change separately.

The second was the [VoiceDebrief pitch](https://sgit.ai/demos/vaults/voicedebrief-pitch/index.html) to Founder Institute on 2 September 2026: a presenter app with per-slide target timings, a three-minute countdown and speaker notes, built from a template by a script in the vault, with the spoken script extracted from the notes and the PDF and PPTX regenerated on every release. That added time to the slides: each one knew when it should be on screen.

The next step is to let the clock drive. Instead of a deck with timings beside it, a timeline with slides on it.

## The player

The prototype's presenter view at 2:58 of the five-minute demo: the slide, the words, the time left and a progress bar.

This site's agent built a first version, and it is deliberately small: one HTML file and one JSON file, no build. It is a page made for one moment, which [Custom UIs are not the exception](custom-uis-are-not-the-exception.md) argued is normal now: "A custom interface per message or moment is not an exception". The talk is a list of beats. Each beat has a start in seconds, a duration, a title, the words to say, and a slide with a layout:

- **statement**: a line of text, with builds that appear at set seconds;
- **terminal**: a command typed out character by character, then the output the real run produced;
- **table**: rows revealed every few seconds;
- **bullets**, **video**, for example an MP4 exported from Claude Motion, and **iframe**, for a live page.

A clock drives everything. Press Space and it plays; the beat at the current second is on screen, its builds appear at their offsets, and the next beat starts on time without a click. The arrow keys jump between beats if the room needs a moment. P opens the presenter view: the words for this beat, the seconds left, highlighted in the last five, and what comes next. R starts a rehearsal, which records when each beat actually began; when it stops, it saves a file of planned against actual times, the evidence of whether the script fits the slot.

It was tested in Chromium: every beat came on at its second, the builds and rows appeared on schedule, the terminal finished typing and then printed, the arrows jumped forward and back, it stopped at 5:00, and the page raised no errors. A version with the talk inlined opens straight from a file, with no server and no network, which is the version to carry into a room with bad wifi.

## The demo is recorded truth

The part I like most is the terminal. A live demo is where talks go wrong: the network, the package cache, the one command that behaves differently on stage. In a scripted talk, the command is typed on the timeline and the output is the one the real run produced, captured beforehand and kept with the talk. That is not faking the demo. It is the same principle as every vault on sgit.ai: the evidence is recorded, versioned and inspectable, and anyone can run the command again from the vault and compare.

## Animations as code

The memo's transcription garbled two names. The first is clearly Claude Motion, which Anthropic [released in beta](https://claude.com/resources/articles/dashboards-and-motion) on 8 October 2026 for Team and Enterprise plans: "Claude writes code that animates your text, charts, shapes, and images, so you can change any word, number, or timing." It "doesn't use a video generation model", and the result downloads as an MP4. I could not make out the second word with confidence; the code-based animation tools it most likely refers to are Manim, the Python library for mathematical animation, and Remotion, which makes video from React components, and both are already used with Claude Code through community skills.

They all fit the timeline the same way. An animation made as code can be edited a word or a number at a time, versioned beside the talk, exported as an MP4, and placed on a beat. The talk stays data from end to end: the words, the slides, the animations and the recorded output, each in a file, each with a history.

## First use: ruv.sgit.ai

The first timeline is a real one. [ruv.sgit.ai](https://ruv.sgit.ai/index.html) is the newest site in the sgit family, built on 14 October for Agentic Engineering Live with Reuven Cohen, rUv, in London on 15 October. It shows sgit vaults and agent behaviour policies running inside his stack, Ruflo, RuVector, RVM and MetaHarness, as six proofs of concept, and it already has a [five-minute demo](https://ruv.sgit.ai/demo.html) written in five beats. The agent turned those beats into the first `talk.json`: the claim, Ruflo's default saying yes to sending email, the same eleven actions with and without the behaviour policy, read from the site's own data, memory with history across runners, and the ask. A ten-minute version is the same file with more beats.

## A brief for the talk vault

1. **The talk vault.** `talk.json`, the player, the assets and every rehearsal file in one vault, with a published read key once the talk is given.
2. **Recorded demos.** A script that runs each demo command and saves its output beside the beat that shows it.
3. **Motion on beats.** Animations made in Claude Motion, Manim or Remotion, exported as MP4 and referenced by path.
4. **Rehearsal as a test.** A rehearsal file committed after each run-through, and a check that fails if any beat runs more than ten seconds over.
5. **Exports.** The same timeline rendered to a PDF, one page a beat, and to one MP4 of the whole talk.
6. **A vault app.** The player served from the vault itself, as the Black Hat deck is, so the talk and its evidence travel as one object.

## What this does not claim

- **It has not been given yet.** The player was tested in a browser, not in a room.
- **Scripted is not read.** The words are in the presenter view; whether to read them is the speaker's choice.
- **The second animation tool is a guess.** The transcription was unclear.
- **Claude Motion was not used here.** Its details are from Anthropic's pages; it is in beta on Team and Enterprise plans.
- **The exports and the talk vault are proposed.** The player, the timeline and the tests exist.

If you give talks and want yours to be a timeline with its evidence attached, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 14 October 2026, written by this site's agent in the voice of this site; the argument and the editorial responsibility are mine. The player was built and tested by this site's agent on 15 October 2026, from the two published vaults, which it cloned with their read keys, and from ruv.sgit.ai's demo script and data. From sgit.ai: [AI vs. AI, Black Hat Europe 2025](https://sgit.ai/demos/vaults/blackhat-eu-2025/index.html) and [A three-minute pitch](https://sgit.ai/demos/vaults/voicedebrief-pitch/index.html). Anthropic, [Build live dashboards and animate explainers with Claude](https://claude.com/resources/articles/dashboards-and-motion), 8 October 2026, and [Get started with Claude Motion](https://support.claude.com/en/articles/17454997-get-started-with-claude-motion); [ruv.sgit.ai](https://ruv.sgit.ai/index.html) and its [demo](https://ruv.sgit.ai/demo.html). Read on 15 October 2026.

## Threads

Vaults & methodSite & engineering[This article as a graph →](graphs.md#the-scripted-talk)

### Builds on

- [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](custom-uis-are-not-the-exception.md) Every message has a graph, so it can be shaped for the reader's moment; a custom interface per moment is now how interfaces get made, and each gets a policy.

### Continued by

- [Omnichannel programming: briefs by voice, reviews by voice, previews on the phone, and one shared state underneath, at every stage from explorer to town planner](omnichannel-programming.md) Programming by voice, chat, phone, IDE and pull request, with one shared state underneath, at every stage from explorer to town planner. This site, counted.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 131 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=131)

**Posting this article on LinkedIn?** The cover is [the-scripted-talk.jpg](banners/the-scripted-talk.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-scripted-talk.html)*
