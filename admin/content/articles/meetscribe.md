---
title: MeetScribe: transcripts and a debrief of my Google Meet calls without upgrading every Workspace account, a Chrome extension built in about two hours from a brief that would have failed without an error, and a call for testers
date: 2026-11-03
author: Dinis Cruz
author_url: about/index.html
summary: For the Web Summit work I added a lot of people to my Google Workspace, on Business Starter, which has no Meet recording and no transcripts. Upgrading everyone to Business Standard would double the bill, and the transcription services that join your calls as a bot cost about as much again. So I asked ChatGPT for a brief, gave it to Claude, and between 00:15 and 02:13 UTC on 3 November we built MeetScribe: a Chrome extension that transcribes the Meet call you are in and writes a debrief, with key points, decisions, actions and open questions, each timed. It runs on your own OpenRouter key, with no bot in the call, no Google recording and no server of ours; an hour of meeting costs roughly 5 to 15 US cents. The most interesting part is the review: ChatGPT's brief had its facts mostly right, but four of its choices would have failed without an error, producing text nobody said. Claude's review found 23 problems, wrote a second brief, and built from that, with 45 tests. It is a beta, its first real calls are being made now, and one thing is not optional: in Portugal, recording people's words without their consent is a crime, so MeetScribe asks you to tell everyone, every meeting. If you use Meet, I would like you to try it.
version: v0.14.41
license: https://creativecommons.org/licenses/by/4.0/
tags: meetscribe, voicedebrief, chrome-extensions, google-meet, transcription, openrouter, agents, beta, article
status: published
---

!shot msc-meetings.webp | images/ | MeetScribe's meetings page in a test: the debrief, timed points, the transcript, and the cost OpenRouter reported. | screenshot

## In short {#in-short}

- **The problem:** Business Starter has no Meet recording or transcripts, and upgrading everyone doubles the bill.
- **The tool:** MeetScribe, a Chrome extension that transcribes the call you are in and writes a debrief.
- **No bot, no Google recording, no server of ours:** it runs on your own OpenRouter key.
- **About 5 to 15 US cents an hour** of meeting, paid to OpenRouter directly.
- **Built in about two hours,** from a ChatGPT brief that Claude reviewed, corrected and built with tests first.
- **The brief would have failed without an error;** the review is the story.
- **Consent is not optional:** tell everyone, every meeting.
- **It is a beta.** Try it, and tell us what happened.

## The problem {#problem}

For the [Web Summit team](/articles/web-summit-part-four.html) I added a lot of people to my Google Workspace. It is on Business Starter, and Starter does not have Meet recording or transcripts: on Google's own pricing page, "Meeting recordings saved to Google Drive" is marked "This feature is not supported by this SKU" for Starter, and so is Gemini taking notes in Meet.

The fix Google offers is to upgrade every user. On flexible plans that is $16.80 per user per month for Business Standard against $8.40 for Starter, twice the price, for everyone, so that a few of us can have transcripts. The other route is a transcription service, and the main ones cost about the same per user: Otter's Pro plan is $8.33 a month billed annually, Fireflies $10, Read.ai $15, and most of them work by sending a bot into the call.

I did not want either. I wanted the transcript of the call I am in, on my own key, with nothing joining the call.

## What MeetScribe does {#what}

It is a Chrome extension. In a Meet call, you click its icon, the side panel opens, you tell the others you are transcribing, and you press Start. It captures the tab's audio, and, if you choose, your microphone, cuts it at pauses, drops the silence, and sends each piece to a transcription model through OpenRouter. After the call, you press Write the debrief, and a second model writes the key points, decisions, actions, open questions and the meeting in one sentence, each point with the time of the line it came from. You can export it as Markdown, text or JSON.

What I like most is that it does not guess:

- **It does not know who said what,** so your words are labelled You and everyone else's Meeting.
- **A line that looks like your microphone hearing the call** is marked probable-echo, and dimmed, not deleted.
- **A phrase models invent from silence** is marked suspect.
- **Nothing is lost quietly:** every stretch of speech is saved before it is sent, and anything that failed shows as a gap with a reason.
- **It costs what it says:** each meeting shows the cost OpenRouter reported. In the test in the picture, eight pieces of audio cost $0.0014 and the debrief $0.0003.

At OpenRouter's listed prices on 3 November, transcribing with the default, Whisper large v3, costs about 3 to 11 US cents an hour depending on the provider, and the debrief about 2 to 3 cents. MeetScribe asks OpenRouter for zero-data-retention providers only, and everything else, the meetings, the transcripts, the audio waiting to be sent and the key, stays in your browser.

## Built in about two hours {#built}

I created an empty repository at 00:15 UTC on 3 November. At 00:32 it held a review of ChatGPT's brief, a second brief and a plan. At 01:09, the first working version of the extension, its tests, and a pipeline that validates, tests, tags and deploys. At 01:39, the debrief. At 02:09, the site on its own domain, a download for testers and a test-report form. Five commits, about 1,700 lines of code, and 45 automated tests.

That speed is not the point on its own. The point is how it was built.

## The brief that would have failed without an error {#review}

I wrote the idea as a brief with ChatGPT. Claude did not build it. It reviewed it first, claim by claim, against the documentation of every API it relied on. The verdict: the facts were mostly right, 14 claims held, and 23 findings needed changes. Four of them were the kind I worry about most, because they would not have crashed. They would have produced a transcript that looked fine and was wrong:

- **Twenty-second recording chunks.** Only the first chunk of a browser recording is a file a model can decode; the model invents text for the rest. The fix: own the samples, and send each piece as a complete audio file.
- **Fixed cuts, every one sent.** Words cut in half, and silence sent to a model comes back as "Thank you for watching". The fix: cut at pauses, and drop silence before it is sent.
- **Its own microphone stream.** It would have recorded you while you were muted in Meet. The fix: the microphone is opt-in per meeting, with its own mute and shortcut, and the page says so plainly.
- **"Microphone means You".** On speakers, the microphone hears everyone, and their words would have become yours. The fix: echo cancellation, and echoes marked, never deleted.

Then building it corrected the second brief too, and the site lists what it found: the part of the extension that drains the queue could not read its own settings, a template's ignore file had silently left two folders of code out of the first commits, and the microphone's clock starts later than the tab's. Every correction goes into the brief's next version.

This is the pattern I keep coming back to, in [the grant, not the prompt](/articles/the-grant-not-the-prompt.html) and [fix the page yourself](/articles/fix-the-page-yourself.html): an agent that checks before it builds, and a record that says what it got wrong.

## Consent is yours to get {#consent}

When Meet records, Google tells everyone: "Participants get a notification when the recording starts or stops." MeetScribe cannot do that, so it asks you to, every meeting: there is a notice to paste into Meet's chat, and a box to tick before Start works.

That is not a formality. In Portugal, recording someone's words that were not meant for the public, without their consent, is a crime under article 199 of the Penal Code, "mesmo que lhe sejam dirigidas", even if the words were addressed to you, with up to a year in prison or a fine. Being in the call does not make it lawful. Other countries have their own rules, and GDPR applies to the transcript as personal data. Tell people, every time.

And the audio goes to OpenRouter and on to a model provider. MeetScribe asks for providers that keep nothing, but its own page says it plainly: do not use it for anything you would not hand to a third party.

## Try it {#try}

It takes about five minutes, in Chrome 116 or later:

1. **Download** the zip from [the MeetScribe site](https://meetscribe.chrome-extension.voicedebrief.ai/) and unzip it.
2. **Load it:** open `chrome://extensions`, switch on Developer mode, press Load unpacked and pick the folder.
3. **Add an OpenRouter key,** with a credit limit of a few dollars, and press Test the key.
4. **In a Meet call,** click the icon, tell the others, tick the box, and press Start.
5. **After the call,** press Stop, open Meetings, and press Write the debrief.

It is a beta. It has been tested with fake audio and replayed responses, and its first real Meet calls are being made now. Expect rough edges, and tell us what happened: the site has [a short test-report form](https://github.com/VoiceDebrief/VoiceDebrief__Chrome_Extension__MeetScribe/issues/new?template=test-report.md), with the eight questions this beta has to answer, from how much echo the microphone picks up on laptop speakers to which model is good enough in English and Portuguese. Issues are public, so remove anything private from what you attach.

Not there yet: names for the other speakers, editing the transcript, search across meetings, and the Chrome Web Store.

## What this does not claim {#limits}

- **It is a beta;** it had not been used on a real Meet call when it was published.
- **Costs are from OpenRouter's listed prices** on 3 November 2026, and depend on the provider OpenRouter picks.
- **The legal notes are not legal advice;** the Portuguese text is quoted from the consolidated Penal Code.
- **Competitors' prices** are from their own pricing pages on 3 November 2026, cheapest paid plan per user; plans and limits differ.
- **Google's annual price for Business Standard** is from third-party sites; the flexible prices are Google's.

## Where this comes from {#sources}

My conversation of 3 November 2026, and [the MeetScribe site](https://meetscribe.chrome-extension.voicedebrief.ai/) and [repository](https://github.com/VoiceDebrief/VoiceDebrief__Chrome_Extension__MeetScribe) at v0.3.1: the review of brief v1.0, brief v2.0, the plan, what is built, and the git log. Google: [Workspace pricing](https://workspace.google.com/pricing), [recording a meeting](https://support.google.com/meet/answer/9308681), [transcripts](https://support.google.com/meet/answer/12849897). [OpenRouter's speech-to-text guide](https://openrouter.ai/docs/guides/overview/multimodal/stt) and [zero data retention](https://openrouter.ai/docs/guides/features/zdr). The Portuguese Penal Code, article 199, from [the Procuradoria-Geral Distrital de Lisboa](https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=109&tabela=leis). Otter, Fireflies, Read.ai and Fathom pricing pages. All read 3 November 2026.
