---
title: VoiceDebrief, relaunched: what the iPhone and iPad app already does, from recording without loss to an on-device transcript, a debrief and an encrypted vault, why the agent workflows move to the CRM app, and the list that takes it to the App Store properly, under its own name and its own accounts
date: 2026-11-16
author: Dinis Cruz
author_url: about/index.html
summary: This is a debrief for the VoiceDebrief team, because I think we can now go to market. The iPhone and iPad app already solves a lot of problems, and it is already better than much of what I was using. It records without loss, with the words appearing as you speak; it transcribes and writes a debrief with Apple's on-device models, so a voice note never has to leave the phone to be understood; it keeps a library on the device; and it saves each debrief, with its transcript and audio, into an encrypted vault, on the device or on a server, with the vault keys in iCloud Keychain. Along the way it also grew a workbench for talking to our agents: sending notes to Claude, live replies, an agents screen, an inbox of decisions, a lab of experiments. That part was designed for my workflow of talking to agents, and it makes the app more complex than a first product should be. So the relaunch takes a step back: the core stays, the agent workflows move to the CRM app, where they belong on top of our email and messaging protocols, and the launch essentials get finished: real payments through the App Store for the credit the app already counts, an account, the share sheet, iCloud Drive. Then we do it properly: its own name on the App Store, its own Apple Developer account and Apple ID, its domains and its accounts, and the full flow from usage to payment.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: voicedebrief, ios, apps, on-device-ai, vaults, go-to-market, product, article
status: published
---

!shot vdr-screens.webp | images/ | VoiceDebrief on iPad, from its own screen tests: recording, a note, the library, a vault, credit, identity and more. | collage

## In short {#in-short}

- **We can go to market:** the app already solves real problems, and is better than much of what I was using.
- **The core works:** record without loss, transcribe and debrief on the device, save to an encrypted vault.
- **It grew a workbench for talking to agents,** which makes it too complex for a first product.
- **Keep the core, move the agent workflows to the CRM app,** and finish the launch essentials.
- **Do it properly:** its own App Store name, Apple Developer account, Apple ID, domains, payments.
- **And dream bigger:** fifteen features for the relaunch team, from asking all your notes to recording from the Watch.

## What VoiceDebrief already does {#features}

!shot vdr-art.webp | images/ | The app's own section art: record, library, vaults, words, recipients, agents, identity, guide. | collage

The app is at version 0.1.138, built and tested on every push, with TestFlight uploads from a green build ([VoiceDebrief for iPhone and iPad](https://ios.app.voicedebrief.ai/)). Its reality file, which lists only what exists, is long. The main features:

- **Record without loss.** A note is written to the library the moment recording starts; the words appear as you speak, with a level display; a silent recording can be rescued; you can record the next note while the last one is being written up. Recording is never charged and never interrupted.
- **Transcript and debrief on the device.** Apple's speech models transcribe, and Apple's on-device foundation model writes a debrief in three sections. A long note is read in parts and merged. On an iPad, a note of 6 minutes 44 seconds was transcribed in 5.4 seconds and debriefed in 10.5.
- **A library on the device:** notes by day, playback, run again in another language, delete.
- **Vaults.** Each debrief, with its transcript, details and audio, is saved as a signed commit into an encrypted vault, on the device with no network needed, or pushed to a server; the vault keys and server tokens are kept in iCloud Keychain. A finished note can save itself to a chosen vault ([how a vault works](/articles/how-a-vault-works.html)).
- **Send a note to someone:** recipients added by QR code, finish and send in one press, sends that retry and say when they went.
- **Identity:** your own key pair, a key for each device, made in the Secure Enclave where there is one, and vouching for a device ([a key for every person](/articles/a-key-for-every-person.html)).
- **Credit that counts down:** a balance that starts at £5, charges only for what was done, never for recording, and never blocks anything below zero; the top-up is simulated today.
- **A briefing on opening, a guide, diagnostics, release notes,** and a welcome on the first launch.

Its screens are tested the way our other apps are: one UI test per screen over sample data, 35 screens on iPad in the latest round, reviewed by synthetic users who each have a reason to use the app ([native apps by agents](/articles/native-apps-by-agents.html)). Beside it, the web version at [voicedebrief.ai](https://voicedebrief.ai/) runs in the browser on your own key, where a 42-second note costs about £0.003 for a transcript and a debrief, and the MeetScribe extension does the same for Google Meet.

## Why simpler {#simpler}

VoiceDebrief also grew a second life. Because I use it to talk to our agents, it gained a button to send a note to Claude and see the replies, a live panel of notes and agents by topic, an agents screen and a workbench, an inbox of decisions from the conductor, recipients that are agent lanes, and a lab of on-device experiments. All of it works, and some of it is brilliant. But it was designed for one workflow, mine, and it makes the app much more complex than a first product should be.

So the relaunch takes a step back.

!shot vdr-keep.webp | images/ | VoiceDebrief, simpler: keep the core, move the agent workflows to the CRM app, add what launch needs. | comparison

- **Keep the core:** record, transcript and debrief on the device, the library, vaults, sharing with a person, the briefing.
- **Move the agent workflows to the CRM app,** where they make sense: talking to agents, live replies, the inbox of decisions, agent lanes. There they sit on top of the email twin and the messaging protocols we are building ([a CRM for us and for our agents](/articles/a-crm-for-us-and-our-agents.html), [the email agentic cell](/articles/the-email-agentic-cell.html)).
- **Add what launch needs:** real payments, an account with a passkey and a recovery code, notes received from the share sheet (WhatsApp voice notes too), recording in the background proven, iCloud Drive as well as vaults, and debriefs signed by the device key.

## What it can become {#vision}

!shot vdr-features.webp | images/ | What VoiceDebrief can become: fifteen features, from asking all your notes to recording from the Watch. | concept

This is a brief for the team that relaunches it, so here is the whole vision, not only the next release:

- **Debriefs for every occasion.** A meeting, an interview, a doctor's appointment, a sales call, a lecture, a site visit: each with its own sections, chosen before or after recording.
- **Actions out of the debrief.** Tasks go to Reminders, dates to Calendar, people to Contacts, and follow-ups to the CRM, each one a tap to confirm.
- **Ask all your notes.** "What did I promise Ana last month?" answered on the device, citing the note and the minute it was said.
- **Brief me before.** Before a meeting, a one-page brief from every note about that person or company.
- **Who said what.** Speakers told apart, with names you confirm once.
- **Every language.** Record in one language and read the debrief in another, translated on the device.
- **Record from anywhere.** The Apple Watch, AirPods, the Action button, Siri, a lock-screen widget, and a Live Activity while it records.
- **WhatsApp and the share sheet.** Any voice note from any app, debriefed where it lands.
- **An infographic per debrief.** One picture of the key points, to share instead of a wall of text.
- **Share safely.** A debrief shared as a link to a vault with its own key, revocable, with signed reads.
- **Your notes, your storage.** On the device, in iCloud Drive, in your own vault on a server, or all three.
- **A weekly digest.** What you talked about, decided and still owe, every Friday.
- **A Mac app and a web app.** The same library everywhere, synced through your vault.
- **Teams and families.** Shared spaces with roles, one plan, and nobody reading what they should not.
- **Privacy you can check.** A page that proves what ran on the device and what, if anything, left it.

## Going to market properly {#market}

!shot vdr-market.webp | images/ | Going to market properly: name and domains, its own accounts, payments, privacy and review, usage, launch. | process

Now that we have the gist, it is time to do it properly:

1. **Name and domains:** settle the name on the App Store, and register the domains it needs; voicedebrief.ai already serves the site.
2. **Its own accounts:** an Apple Developer account for VoiceDebrief, its own Apple ID, and its own email and support addresses, so the product stands on its own.
3. **Payments:** turn on the App Store purchase the app already has written and switched off, put the ledger in the user's vault, and replace the placeholder prices.
4. **Privacy and review:** privacy labels, review notes and a support page, telling the on-device story plainly.
5. **Usage:** what people use and where they stop, from the app's own activity log, with consent.
6. **Launch:** TestFlight to outside testers, then the App Store, with the web version and MeetScribe beside it.

The monetisation angle is good: most of the work happens on the device, with Apple's models, so a note costs us very little to process, and the credit model the app already counts lets people pay for what they use, with no subscription.

## What this does not claim {#limits}

- **Many features are marked "unverified" in the app's own reality file:** written and tested in parts, not all proven on a device by a run.
- **Payments, the account, the share sheet and the App Store listing do not exist yet;** the credit top-up is simulated, and the features under "what it can become" are a brief, not a promise of dates.
- **The timings are from single runs** recorded in the reality file.

## Where this comes from {#sources}

The repository VoiceDebrief__App__iOS, read on 16 November 2026: `website/built/index.md` (the reality file), `website/credit/index.md`, `website/reviews/round-3/` (the screen sheets the collage is cut from), the app's section art, and `issues/open/`. The live sites [ios.app.voicedebrief.ai](https://ios.app.voicedebrief.ai/) and [voicedebrief.ai](https://voicedebrief.ai/). Earlier on this site: [native apps by agents](/articles/native-apps-by-agents.html), [a CRM for us and for our agents](/articles/a-crm-for-us-and-our-agents.html), [the email agentic cell](/articles/the-email-agentic-cell.html), [how a vault works](/articles/how-a-vault-works.html), [a key for every person](/articles/a-key-for-every-person.html).
