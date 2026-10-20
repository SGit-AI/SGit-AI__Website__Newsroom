---
title: The vault crosses Chrome profiles: state and memory between browser sessions, found by using it rather than by building it
date: 2026-10-13
author: Dinis Cruz
author_url: about/index.html
summary: In the newsroom workflow we just found something I did not plan. I keep separate Google accounts in separate Chrome profiles, and moving anything between them has always been awkward. The newsroom's reader vault fixed that without a line of new code. It got there by a path that was not a straight line: first we tracked what a reader does, in local storage; then the activity was worth keeping, so we persisted it, driven by what the reader valued; then we opened sgit vaults in the browser, which we already knew how to do; then the marks arrived, read later, not for me, more like this, and I started to have a stake in my own newsroom, with the usage and the payment travelling with it. Across devices was the feature I asked for. Across Chrome profiles is the one I found, and I suspect it is the more common case, because people switch between browser profiles far more often than between computers. What it really is, is memory and state between sessions, the same thing sgit already does for agents in different Claude accounts, now done through the interface of a website. This is how it works, what each profile needs to get in, and why the best features are sometimes the ones you discover by using what you built.
version: v0.12.11
license: https://creativecommons.org/licenses/by/4.0/
tags: vaults, chrome-profiles, browser, state, memory, passkeys, newsroom, local-first, feedback-loop, agents, article
status: published
---

!shot vp-profiles.webp | images/ | Two Chrome profiles on one computer, each signed in to a different Google account, each with its own local storage that the other cannot see. The reader's vault sits outside both: each profile writes its own file to it and reads the other's, so the marks, the reading and the balance in one are there in the other. The way in differs by where the passkey lives. | architecture

## In short {#in-short}

- **I use separate Chrome profiles for separate Google accounts**, and moving anything between them has always been awkward: copy, paste, email it to myself.
- **The reader's vault crossed that line without new code.** The newsroom on one profile now shows what I read, marked and paid for on the other, the same way it does across devices.
- **It got here by a path that was not a straight line.** Activity tracked in local storage; persisted because it was worth keeping; vaults opened in the browser, which we already had; marks that gave me a stake in my own newsroom; then devices; then profiles.
- **Profiles are probably the more common case.** People switch browser profiles during the day far more often than they switch computers. I think this matters more than the feature I asked for.
- **What it really is: memory and state between sessions.** sgit already carries state between agents in different Claude accounts. Here the same thing happens through the interface of a website, for a person.
- **Each profile gets in by its own path.** Where the passkey lives decides it: a Mac's iCloud Keychain answers both profiles alike; a passkey in one Google account does not follow into the other, and the phone or the recovery code adds a door once.
- **Found, not built.** Nothing in the code mentions Chrome profiles. The property was there because each piece was built to be general, and I found it by using it.

## The problem: two accounts, two browsers in one {#problem}

I have several Google accounts, and each lives in its own Chrome profile: mine, and the accounts my agents use, which [Replicating the agentic inbox](/articles/replicating-the-agentic-inbox.html) explains, because the agent's mailbox, calendar and Claude account must never be mine. A Chrome profile is, for most purposes, a separate browser. It has its own history, its own passwords, its own extensions, and its own storage for every website. That separation is exactly what I want for the accounts, and exactly what makes it hard to get anything from one to the other. The usual answer is to copy and paste, or to email it to yourself, which, for the agent's account, means sending something into a mailbox I am trying to keep clean.

## How we got here, which was not a straight line {#path}

!shot vp-path.webp | images/ | Six steps, three days, and not a straight line. Each of the first five was built for its own reason, following what the reader valued; the sixth was not built at all, it was found by using the others. Dates and releases from the release histories of sgit.ai and the newsroom. | timeline

None of this was designed as a way to cross profiles, and the path is worth telling, because I wrote yesterday that [progress is not a straight line](/articles/not-a-straight-line.html) and this is a small, clean example of it.

1. **Track what the reader does.** On 10 October the [reading meter](/articles/pay-after-you-read.html) started recording every page read and every penny spent, in the browser's local storage, with no account and no server. Personas, ratings and declines followed the same afternoon, all in the same local state.
2. **Keep it, because it was worth keeping.** The next day I noticed my iPhone, iPad, laptops and iMac did not agree: four balances, four reading histories. [I miss it, so it is working](/articles/i-miss-it.html) was the moment the activity became something I wanted to keep, and the reason to persist it came from the value to the reader, not from a plan.
3. **Open vaults in the browser, which we already knew how to do.** The [passkey opens the vault](/articles/the-passkey-opens-the-vault.html), and by two in the morning on 12 October [the vault was live](/articles/the-vault-is-live.html): a pane on every page, three real sgit vaults, the vault library that already ran elsewhere, vendored unedited. It was an extension of things we had built, not a new system.
4. **Marks, and a stake in it.** The same day the newsroom added notes as you read, read later, not for me, more like this, liked, wrong, fix this, and an idea, and the next day the wire became an inbox whose seen stories travel in the device's file. This is the part of [The site is an inbox](/articles/the-site-is-an-inbox.html) that is now real. Once I was marking which stories I want and which I do not, I had a vested interest in keeping my newsroom, and the usage and the payment went with it.
5. **Across devices**, as asked: one file per device in the reader vault, every device's activity brought into the browser you are holding, one balance.
6. **Across Chrome profiles**, as found.

## Across profiles, as found {#found}

The moment was simple. I was in the Chrome profile of another account, opened the newsroom, and wanted my newsroom there: my marks, what I had read, my balance. Not the empty one a fresh profile shows. And it was there, by the same steps as on a second device, because to the vault a second Chrome profile is a second device. It has a device id of its own, it writes its own file, and it reads the files of every other device, including the profile next door.

Nothing in the newsroom's code mentions Chrome profiles, and no test covers them. The tests treat a device as a browser whose storage has been cleared, which is exactly what a new profile is. The property was there because each piece was built to be general: the reader's state is records, not totals; each device writes only its own file, so there is nothing to merge; the view is computed when the vault opens. A design that works for an iPad and an iMac works for two profiles on one iMac, without anybody deciding that it should.

## What each profile needs to get in {#door}

The honest detail is in how a profile opens the vault, because a passkey lives in a store, and the store decides. [The passkey article](/articles/the-passkey-opens-the-vault.html) has the table; for profiles it comes down to three cases.

- **A passkey in iCloud Keychain, on a Mac.** The store belongs to the Mac, not to the Chrome profile, and the lab found an iCloud Keychain passkey gave the same bytes in Safari and in Chrome. Both profiles reach the same door.
- **A passkey in Google Password Manager.** Google says such passkeys are ["synced to your Google Account"](https://support.google.com/chrome/answer/13168025), so they follow the account signed in to the profile, so a profile signed in to a different account does not have it. That profile gets in by the phone over QR, which gives different bytes and therefore its own door, or by the recovery code, once. After that, it opens without the code.
- **Chrome's own profile store**, in a clean profile with no provider, returns no bytes for a door at all; the recovery code is the way in.

So "it just worked" needs one sentence of care: it just worked once each profile had a door, and with a Mac's keychain the first door is the only one needed.

## Profiles are the more common case {#common}

Here is the angle I think matters most. I asked for the newsroom across devices because that was the pain I felt first. But how often does anyone move to another computer in a day? A few times. How often do people switch between browser profiles, between work and personal, between clients, between a person's account and an agent's? Many times, every day, on the same machine. My hypothesis is that state across profiles is the more common need, and the less served one, because every website treats each profile as a stranger.

I looked for numbers and found none: neither Google nor the Chromium project publishes how many people use more than one profile. What Google's own help says is what profiles are for: ["Keep your different accounts, like work and personal, separate"](https://support.google.com/chrome/answer/2364824). Chromium's documentation is explicit that [each profile is its own directory](https://chromium.googlesource.com/chromium/src/+/HEAD/docs/user_data_dir.md), with its own history, bookmarks and cookies, and a site's local storage lives in the profile too, which is why a fresh profile opens the newsroom empty. And agents are about to make profiles more common, not less: Anthropic's own advice for Claude in Chrome is to [consider "a separate browser profile without access to sensitive accounts"](https://support.claude.com/en/articles/12902428-using-claude-in-chrome-safely). Every person who follows it will have one more profile, and one more place their state does not reach.

## Memory and state between sessions {#memory}

Step back and this is not really about Chrome. It is a way to give a person memory and state between sessions, in whatever browser and whatever account they happen to be in, without a server that holds it and without signing in to anything. We already do this for agents. My agents run as separate Claude sessions on separate accounts, and [the only memory they share is encrypted vaults](/articles/encrypted-memory-for-isolated-agents.html): each clones what it needs, works, commits and pushes, and they talk through files, an inbox and a done folder per agent in Email-FS, issues as folders in Issues-FS, as [Memory is not a spectator sport](/articles/memory-is-not-a-spectator-sport.html) describes. The reader's vault is the same idea with a different interface. The sessions are browser profiles, and the interface is a website.

That opens more than it looks. A browser session can now hand state to another browser session through a site's own interface: a reading list, a set of marks, a half-finished task. It also fits the service in [Stop the bleeding, then ask for it back](/articles/stop-the-bleeding-then-ask-for-it-back.html), where an operator works in one browser while an agent drives another, and the vaults are the place they meet. I do not want to overstate it: today the newsroom carries the newsroom's state, and only when the reader presses Update. But the pattern is general, and that is the point.

## The best features are found {#discovered}

The last point is the one I keep relearning. This feature needed no new development. It needed the earlier features to be built well enough to be general, and then it needed somebody to use them in a way nobody had planned. That is the loop in [I miss it](/articles/i-miss-it.html), running one more time: use it, notice what it does, and only then decide what it is for. If I had set out to build "state across Chrome profiles" I would have designed something specific, and probably something worse. Instead it fell out of records that are never totals and files that have one author. The next step is to treat it as a feature: test it with two real profiles, make the pane say which profile is which, and see what else a person wants to carry from one browser session to another.

## What this does not claim {#limits}

- **No test covers Chrome profiles yet.** The tests treat a device as a cleared browser, which is what a new profile is; a run with two real profiles, each signed in to a different account, is the next experiment.
- **The sync is by hand.** Each profile updates the vault when its reader presses the button; automatic sync is still open work.
- **The way in depends on the passkey's store.** The iCloud Keychain result is from the lab's runs on a Mac; a Google Password Manager passkey does not follow into another account's profile, and that profile needs its own door.
- **"More common than devices" is a hypothesis.** I looked for figures on how many people use several browser profiles and found none published by Google or Chromium; the claim rests on how profiles are meant to be used, and on mine.
- **The state is the newsroom's.** What crosses today is the reader's newsroom: reading, marks, notes, balance. Anything wider is the pattern, not a feature.

If you switch between browser profiles all day and want to try carrying something across, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo of mine on 13 October 2026, written by this site's agent in the voice of this site. The argument and the editorial responsibility are mine. The path from local storage to the vault is from the newsroom's release history, v0.11.0 to v0.12.8 of 12 and 13 October 2026, and from the sgit.ai releases of 10 October; the way each profile gets in is from [The passkey opens the vault](/articles/the-passkey-opens-the-vault.html) and the newsroom's note on [one door per passkey path](https://newsroom.sgit.ai/admin/notes/2026-10-12__one-door-per-passkey-path.md). Chrome profiles: Google's [help on profiles](https://support.google.com/chrome/answer/2364824) and [on passkeys](https://support.google.com/chrome/answer/13168025) ("synced to your Google Account"), and Chromium's [user data directory](https://chromium.googlesource.com/chromium/src/+/HEAD/docs/user_data_dir.md). The advice on a separate profile is from Anthropic's [Using Claude in Chrome safely](https://support.claude.com/en/articles/12902428-using-claude-in-chrome-safely).
