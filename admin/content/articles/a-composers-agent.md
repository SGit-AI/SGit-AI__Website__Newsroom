---
title: A composer's agent: a plan to read a piano score from a PDF into Sibelius, then the composer's own handwriting, with MusicXML in the middle and a check by rendering back
date: 2026-10-31
author: Dinis Cruz
author_url: about/index.html
summary: A friend of mine, a composer, described the agent they would like. First phase: give it a PDF of a piano piece, and it reads the notes and writes the piece into Sibelius, the notation software they use. Second phase: they write music by hand, scan it, and the agent learns to read their handwriting and puts it on the staff, so the good things they write by hand stop waiting to be typed in. They have already seen an agent catalogue all their MP3s and PDFs while they watched, so they know this kind of thing is close. I think it is completely doable, and this is the plan. The key question is recognition, and the trick is to keep an open format in the middle. Optical music recognition engines, the open-source Audiveris or Neuratron's PhotoScore, which is sold for Sibelius, turn a page into MusicXML, and Sibelius imports MusicXML. The agent's job is to run that, then check the result by rendering the MusicXML back into an image and comparing it with the page, and fix what is wrong. Only then does it touch Sibelius itself, for the things a composer cares about, layout, house style, instruments, through a Sibelius plugin or Sibelius Connect, the remote control added in 2024, and through the screen only when nothing else will do. The second phase is closer than it sounds: models already read my handwriting, which is worse than most music. The agent keeps every page and every correction in a vault, so each run has the composer's own past pages as examples. A Claude session on a schedule runs it, connected by Remote Control to the computer where Sibelius lives. Four MVPs, in order, each useful on its own.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: music, agents, sibelius, omr, musicxml, handwriting, mvp, article
status: published
---

!shot cm-plan.webp | images/ | A composer's agent in two phases: printed piano music into Sibelius first, then the composer's own handwriting. | process

## In short {#in-short}

- **Phase one:** a PDF of a piano piece in, the piece written into Sibelius out.
- **Phase two:** the composer's handwritten pages, scanned, read and put on the staff.
- **Keep an open format in the middle.** Recognition produces MusicXML, and Sibelius imports MusicXML.
- **Check by rendering back:** draw the MusicXML as an image, compare it with the page, fix.
- **Drive Sibelius only where it must be driven:** a plugin or Sibelius Connect first, the screen last.
- **Handwriting is closer than it sounds,** with the composer's own past pages and corrections as examples.
- **Four MVPs,** each useful on its own.

## What my friend wants {#want}

A friend of mine, a composer, described in a voice memo the agent they would like. First, give it a PDF of a piano piece: it reads the notes, then goes to Sibelius, the notation program they use, and writes the piece there. They have seen an agent do comparable work already: they asked one to catalogue their MP3s, and watched it catalogue all of them, and all their PDFs too.

Second, the harder part: they write music by hand, scan it, and the agent learns to read their writing and puts it on the staff. They have good things written by hand, and this would save them the work of entering them.

I think it is completely doable, and that a couple of MVPs would show it. The interesting question is recognition.

## An open format in the middle {#musicxml}

The first decision is not to make the agent copy notes into Sibelius one by one. Put an open format in the middle. MusicXML is the exchange format notation programs share, and Sibelius imports it. So the pipeline is: recognise the page into MusicXML, check it, and import it.

For recognition there are two kinds of engine:

- **Optical music recognition software.** Audiveris is open source, under the AGPL, and exports MusicXML; its latest release listed is 5.10.2, from March 2026. Neuratron's PhotoScore is commercial and sold as a plugin for Sibelius; its Ultimate edition is described by its sellers as reading printed music and, with less accuracy, handwritten music, and sending the result straight to Sibelius or saving MusicXML.
- **The model reading the page itself,** the way it reads a photographed page of notes, writing MusicXML directly. Less proven for dense piano scores, and worth comparing against the engines on the same pages.

## Check by rendering back {#check}

Recognition makes mistakes: a missed tie, a wrong accidental, a voice on the wrong staff. So the agent's real job is the check. It renders the MusicXML back into an image, with an open-source engraver, and compares it with the original page, bar by bar; where they differ, it fixes the MusicXML and checks again. It keeps a list of what it changed and why, so the composer can see it.

This is the same idea as everything else we build: the output is checked against its source before anyone relies on it.

## Driving Sibelius {#sibelius}

Once the MusicXML is right, it can be imported, and that may be enough. But a composer will want Sibelius-specific things: the layout, the house style, the instruments, the playback. For those, the agent works with Sibelius itself, in this order:

1. **A Sibelius plugin.** Sibelius has its own plugin language, ManuScript, for operations on a score.
2. **Sibelius Connect,** added in Sibelius 2024.3, which lets other programs on the same computer control Sibelius once the user allows it in the preferences. Its technical details are reported to be in the ManuScript reference; we have not read them yet.
3. **The screen, last.** An agent can move the mouse and use the menus, but that is the slowest and most fragile way, kept for what nothing else can reach.

## The agent and its computer {#stack}

The agent is a Claude session, like the ones that write this newsroom, which can install and run the recognition tools itself. It runs on a schedule, so the work grows: drop PDFs in, find them in Sibelius later.

Sibelius runs on the composer's own computer, so the session connects to it with Remote Control, as one of our other sessions already does, with a written policy for what it may touch: the scores folder and Sibelius, and nothing else. Every score, every MusicXML version and every correction is kept in a vault, so nothing is lost and every change can be seen.

## Phase two: the composer's handwriting {#handwriting}

The second phase is, I think, closer than it sounds. Models already read my handwriting, which is worse than most music. And open recognition engines have been weakest on handwriting, which is exactly where a model reading the page, with examples, can help.

The way to make it learn the composer's hand is not to train a model. It is to keep examples. Each handwritten page and its corrected MusicXML go into the vault. On the next run, the agent is given the composer's own past pages and corrections as examples, and the list of mistakes it made before. Every correction makes the next page better, and the composer can see the accuracy rise run by run.

## Four MVPs {#mvps}

1. **One printed page.** A page of a piano PDF through Audiveris to MusicXML, imported into Sibelius by hand. Count the errors.
2. **The check loop.** The agent renders the MusicXML back, compares it with the page, fixes it, and reports what it changed. Count the errors again.
3. **Into Sibelius.** Import, then apply the composer's own settings with a plugin or Sibelius Connect, on their computer, on a schedule.
4. **One handwritten page.** The model reads it to MusicXML, the composer corrects it, and the correction is kept for the next page.

Each one is useful on its own, and each tells us what the next one needs.

## What this does not claim {#limits}

- **It is a plan.** None of the MVPs is built yet.
- **Recognition accuracy is not tested here.** Vendor figures are claims, and handwriting recognition has been weak in open tools.
- **Sibelius Connect's details are unread;** the plugin route and import are the safer first steps.
- **Rights matter.** The PDFs should be music the composer has the right to copy: their own, or out of copyright.
- **My friend is not named,** as a private person.

## Where this comes from {#sources}

- A voice memo of 31 October 2026, my friend's description in Portuguese and my advice in English, word for word with a translation in `admin/notes/2026-10-31__composers-agent/memo-01.md` in this site's repository.
- Seen in search results on 31 October 2026, pages not opened: [Audiveris](https://en.wikipedia.org/wiki/Audiveris) and its [repository](https://github.com/Audiveris/audiveris); [Scoring Notes on Sibelius 2024.3 and Sibelius Connect](https://www.scoringnotes.com/news/sibelius-2024-3/); [PhotoScore at Neuratron](https://www.neuratron.com/photoscore.htm) and [Avid](https://www.avid.com/plugins/photoscore-and-notateme-ultimate).
- Related: [from a checklist to an app you calibrate](/articles/from-a-checklist-to-an-app.html), [reading with a pen](/articles/reading-with-a-pen.html), [Lovable with SHarness](/articles/lovable-with-sharness.html).
