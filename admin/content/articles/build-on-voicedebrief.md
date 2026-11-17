---
title: Build on VoiceDebrief: the techniques from our iPhone and iPad voice app that any team can take into its own, from recording without loss and transcribing offline on the device to debriefs by Apple Intelligence, controlling an app by voice, three layers of intelligence and a CI pipeline that lets agents build a native app without a Mac, with a prompt to point your own Claude at the code
date: 2026-11-17
author: Dinis Cruz
author_url: about/index.html
summary: VoiceDebrief is our voice app for iPhone and iPad, and it has quietly become a worked example of a lot of hard things done right, in a public repository under Apache 2.0. I know several people working on voice projects, and they should not have to rediscover any of it. So here are the key learnings, each with where it lives in the code. Record without loss: the note is written to the library the moment recording starts, as WAV that can be repaired, with a second copy of what the speech engine heard as a safety net. Transcribe offline, on the device, with Apple's SpeechAnalyzer: a live preview while you speak, then the kept transcript made again from the file; 6 minutes 44 seconds of speech in 5.4 seconds on an iPad. Debrief with Apple Intelligence: the Foundation Models framework, one fresh session per request, long notes read in parts sized to a small context. Control the app by voice: fixed phrases first, then the model picks one action as a tool call that does nothing by itself, and a person confirms. Route every step to the lowest of three layers that can do it: code, the model on the device, agents. And build it with agents that never touch a Mac: CI is the compiler, the tester and the release, with a picture of every screen. At the end, a prompt to give your own Claude, so it can find all of this in the code and use it in your app.
version: v0.14.133
license: https://creativecommons.org/licenses/by/4.0/
tags: voicedebrief, ios, on-device-ai, apple-intelligence, speech, open-source, agents, article
status: published
---

!shot vdk-offline.webp | images/ | A voice note, offline, end to end on the device: record, preview, transcript, debrief, keep. | process

## In short {#in-short}

- **VoiceDebrief is a public, Apache 2.0 worked example** of a native voice app, and others can build on it.
- **Record without loss:** written to disk from the first second, repairable, with a safety-net copy.
- **Transcribe offline, on the device,** with Apple's SpeechAnalyzer: no server, no key, no cost per minute.
- **Debrief with Apple Intelligence:** the Foundation Models framework, one small question at a time.
- **Control the app by voice:** the model proposes one action; the code and the person decide.
- **Three layers:** code, the model on the device, agents; push each step down.
- **Agents built it without a Mac:** CI is the compiler; every screen is photographed.
- **A prompt for your Claude** at the end.

## Why share it {#why}

When I relaunched VoiceDebrief yesterday, I described it as an app that already solves real problems ([VoiceDebrief, relaunched](/articles/voicedebrief-relaunch.html)). Looking at it again, it is also something else: a worked example of how to build a voice app now, with the device doing the understanding and agents doing the building. Most of what made it hard, we have now figured out, and written down next to the code.

I know a couple of people working on voice projects right now. They should not have to rediscover any of this. The repository is public, the code is Apache 2.0 and the text CC BY 4.0, and the repository's own site explains it ([ios.app.voicedebrief.ai](https://ios.app.voicedebrief.ai/)). So here are the learnings, and where to find each one.

## Never lose a recording {#record}

The first rule of a voice app is that the recording is sacred. In VoiceDebrief, a note is written into the library the moment recording starts, as 16 kHz mono WAV, a format that can be repaired if the app dies before the file is closed (`VoiceRecorder`, `WAVRepair`). Every later step updates the note on disk, so nothing is ever the only copy in memory (`DebriefSession`).

Two lessons cost us real notes on real devices. Several recordings on the owner's iPhone and iPad came out as pure digital silence, so the live speech engine now writes what it hears to a second file beside the note, a safety net (`LiveTranscriber`). And nothing else may touch the audio session while a note records, because changing it mid-recording leaves a file of silence: playback, the Lab and everything else waits for the microphone (`MicrophoneTurn`). You can also record the next note while the last one is still being written up.

## Transcribe offline, on the device {#transcribe}

Transcription uses Apple's `SpeechAnalyzer` with `SpeechTranscriber`, on the device, in two passes. While you speak, a live preview shows the words appear, settled text and the part that may still change. When you stop, the transcript is made again from the recorded file, and that is the one kept; if the preview fails, the recording carries on without it (`LiveTranscriber`, `SpeechFileTranscriber`). The app lists the languages the model supports and which are already on the device, and picks the one closest to the device's own.

The numbers are what make it a product: a 22.6-second note in 0.6 seconds on a Mac, and 6 minutes 44 seconds of speech in 5.4 seconds on an iPad. No server, no API key, no cost per minute, and it works on a plane.

One bug worth knowing before you hit it: installing an audio tap when one is already on the bus, or with a format that does not match the hardware, raises an Objective-C exception Swift cannot catch. It crashed one build on the owner's iPhone. The fix is in the code: remove any old tap first, and let the node use its own format.

## Debrief with Apple Intelligence {#debrief}

The debrief, a summary, key points and actions, is written by Apple's on-device model through the Foundation Models framework (`OnDeviceModel`). The rules that made it work:

- **One fresh session per request,** so nothing from one note leaks into the next.
- **Respect the small context:** about 4,096 tokens on an iPhone and 8,192 on an iPad. A long note is read in parts sized to the model's context, then merged; the 6 minute 44 second note was debriefed in 10.5 seconds.
- **Ask one small question at a time,** and let the code decide what to do with the answer. The model once gave a task to "[Claude]" because the note addressed Claude by name; small questions keep that kind of mistake small.
- **Say plainly when it cannot run:** the app tells the person, in words, whether Apple Intelligence is available on this device.

The same model also labels a note while you speak (who it is for, its topic, title and urgency, each through one tool call) and turns a transcript into clean text, a passage at a time, with up to three phrases it could not follow.

## Control the app by voice {#control}

!shot vdk-control.webp | images/ | Controlling the app by voice: fixed phrases first, then one tool call, then a person confirms. | process

This is the part I find most exciting, and it is in the app's Lab as experiment L02 (`LabControlCentre`, `LabActionHost`, `LabToolbox`). A sentence comes in, spoken or typed. First it is matched against fixed phrases, because "send this now" at the end of a note should be exact, instant and free. Then it goes to the on-device model, where each of the app's actions is a tool. A tool carries nothing out: it records that the model asked for that action, and the first tool call ends the request, which saves time and energy. The proposed action appears on a card, and the person confirms it. Only actions that are safe to undo are carried out, showing a section or a read-only search; the rest are recorded. The session is prewarmed before the words arrive, and the tools only ever read a copy of the library, so nothing a tool does can change a note.

The same pattern runs a small voice game in the app, and the play button on headphones is wired to finish a recording (not yet tried on a device). Model proposes, code decides, person confirms: it is a behaviour policy, inside an app ([two decision engines](https://ios.app.voicedebrief.ai/articles/two-decision-engines/)).

## Three layers {#layers}

!shot vdk-layers.webp | images/ | Three layers: code, Apple's model on the device, agents in a loop. Push each step to the lowest one that can do it. | concept

The idea that ties it together is the app's own position ([three layers](https://ios.app.voicedebrief.ai/articles/three-layers/)): there are three things that can do work. Code is exact, instant, free and offline. Apple's model on the device understands language, is free per use, private and answers in about a second, but is small. Agents in a loop can read, plan, build and act, but take minutes and cost money. The skill is to push each step to the lowest layer that can do it, and to make every hand-over a file, a sealed message or a commit you can see. A note sent to Claude is sealed on the device and dropped into an append lane; the conductor files it in a vault and the reply comes back into the app ([five primitives, one store](/articles/five-primitives-one-store.html)).

## Built by agents, without a Mac {#ci}

!shot vdr-screens.webp | images/ | Every screen photographed by CI from invented sample data, iPhone and iPad, and read by synthetic users. | collage

Almost all of VoiceDebrief was written by agents in Linux containers that cannot compile Swift. So the repository's rule is: CI is the compiler. Every push runs one Mac job that builds and tests, and copies compiler errors and failed tests into the job summary, where an agent can read them through the Actions API (`ios.yml`, `.github/scripts/run-and-summarize.sh`). Because nobody can run the app from a container, CI also photographs every screen, launched with invented sample data and the network off, on an iPhone and an iPad, light and dark (`screens.yml`, `ScreensTests.swift`, `LaunchOptions.swift`). Synthetic users review those pictures in rounds. And every green push to `dev` goes to TestFlight, which is the subject of the next article ([shipping an iOS app with agents](/articles/shipping-an-ios-app-with-agents.html)).

Two documents make it navigable for any agent: a reality file that lists only what exists (`website/built/index.md`), and a guide to building, testing and releasing (`website/develop/index.md`). Start there.

## The prompt for your Claude {#prompt}

If you are building something with voice, give your own Claude the repository and this prompt:

```
I am building [describe your app: platform, what the voice does].
Study the open-source VoiceDebrief iOS app as a reference:
https://github.com/VoiceDebrief/VoiceDebrief__App__iOS (Apache 2.0).

Start with website/built/index.md (what exists) and
website/develop/index.md (build, test, release), then
website/articles/three-layers/index.md.

Find and explain, with file paths, how it:
1. records without loss (VoiceRecorder, WAVRepair, MicrophoneTurn);
2. transcribes on the device (LiveTranscriber, SpeechFileTranscriber);
3. writes a debrief with Apple's Foundation Models (OnDeviceModel,
   DebriefSession), including how it splits long notes;
4. lets the model propose app actions as tool calls that a person
   confirms (LabControlCentre, LabActionHost, LabToolbox);
5. builds, tests, photographs every screen and ships to TestFlight
   from CI (.github/workflows, scripts/release/testflight.sh).

Then propose how to apply each technique to my app, in order of value,
with what to copy, what to change, and what to test on a real device.
Credit the source and keep its licence.
```

## What this does not claim {#limits}

- **Many features are tested in parts, not all proven on a device;** the reality file marks what is unverified, and simulators have no speech model or Apple Intelligence.
- **The timings are single runs,** recorded in the reality file.
- **On-device models need recent hardware** and Apple Intelligence switched on; check the device first, as the app does.
- **Voice control is a Lab experiment,** with only safe-to-undo actions carried out.

## Where this comes from {#sources}

The repository [VoiceDebrief__App__iOS](https://github.com/VoiceDebrief/VoiceDebrief__App__iOS), read on 17 November 2026: its README, `website/built/index.md`, `website/develop/index.md`, the articles `three-layers` and `two-decision-engines`, the sources named above and its workflows. Its site, [ios.app.voicedebrief.ai](https://ios.app.voicedebrief.ai/). Earlier on this site: [VoiceDebrief, relaunched](/articles/voicedebrief-relaunch.html), [native apps by agents](/articles/native-apps-by-agents.html), [the Mac bottleneck](/articles/the-mac-bottleneck.html), [five primitives, one store](/articles/five-primitives-one-store.html).
