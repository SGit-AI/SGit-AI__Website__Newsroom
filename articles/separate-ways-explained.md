# Separate Ways, explained: what my brother's synth video shows, frame by frame, and why describing work at the moment you make it is the first step to publishing it, sgit.ai

> My brother Gabriel DaCruz posted a short video of Journey's Separate Ways, played on a synthesizer in his studio and filmed from three cameras at once. Most people who watch it will not know what they are seeing. So I asked him to explain it, recorded it, and gave it to this site's agent to check and package. The explanation: a Bluetooth MIDI keyboard with no cable, a Behringer Pro-800, which is a reproduction of the Sequential Prophet-600 from 1982, chorus and delay to match the 1983 record, and, at the end, the decay turned down live so each chord goes staccato and the delay repeats the short chord. The checking found two things he had flagged himself: the record's credits list a Roland Jupiter-8, not the Prophet-5 he remembered, and his synth copies the Prophet-600, not the Prophet-5. And on the way, he mentioned, almost in passing, that he had filmed it with three old iPhones synced live to an iPad, which became an article of its own. That is the point of this one. The people who hire someone like Gabriel are the people who want to know how it was done, and the only time anyone explains it is at the moment of creation, quickly, with an agent doing the rest.

*Source: <https://newsroom.sgit.ai/articles/separate-ways-explained.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Separate Ways, explained: what my brother's synth video shows, frame by frame, and why describing work at the moment you make it is the first step to publishing it

# Separate Ways, explained: what my brother's synth video shows, frame by frame, and why describing work at the moment you make it is the first step to publishing it

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-02 · [article v1.0.0](versions/separate-ways-explained.md) · [newsroom v999.0.0](https://newsroom.sgit.ai/admin/versions.html) · musicsynthesizersjourneyprophetmidibluetoothvideopublishingcreatorsarticle

***Abstract:** My brother Gabriel DaCruz posted a short video of Journey's Separate Ways, played on a synthesizer in his studio and filmed from three cameras at once. Most people who watch it will not know what they are seeing. So I asked him to explain it, recorded it, and gave it to this site's agent to check and package. The explanation: a Bluetooth MIDI keyboard with no cable, a Behringer Pro-800, which is a reproduction of the Sequential Prophet-600 from 1982, chorus and delay to match the 1983 record, and, at the end, the decay turned down live so each chord goes staccato and the delay repeats the short chord. The checking found two things he had flagged himself: the record's credits list a Roland Jupiter-8, not the Prophet-5 he remembered, and his synth copies the Prophet-600, not the Prophet-5. And on the way, he mentioned, almost in passing, that he had filmed it with three old iPhones synced live to an iPad, which became an article of its own. That is the point of this one. The people who hire someone like Gabriel are the people who want to know how it was done, and the only time anyone explains it is at the moment of creation, quickly, with an agent doing the rest.*

Three moments of Gabriel's Separate Ways video, each from three cameras: beginning, middle and end.

## In short

- **My brother posted a video** of the synth part from Journey's Separate Ways, filmed from three cameras in one take.
- **Most viewers will not know what they are seeing,** and the people who would, producers and people hiring, get no explanation.
- **So he explained it,** by voice, and this site's agent checked every claim and packaged it.
- **The setup:** a Bluetooth MIDI keyboard, a Behringer Pro-800 (a Prophet-600 reproduction), chorus and delay.
- **The trick:** decay turned down live, so each chord goes staccato and the delay repeats it.
- **The checking corrected two details** he had flagged himself: the original is credited to a Jupiter-8, and his synth copies the Prophet-600.
- **A side remark became a second article:** three old iPhones synced live to an iPad.
- **The lesson:** describe it at the moment you make it, or it never gets published.

## The video

Gabriel's post is short: three stacked frames of the same take. The top camera looks down on a small white keyboard. The middle one shows him at the desk, with the mixing console, the screen and the rack behind him. The bottom one is close on the synthesizer's panel and the units under it. You hear the riff of Separate Ways (Worlds Apart), the song that opens Journey's album Frontiers, released as a single in January 1983, and near the end you see his hand go down to the panel and the sound change.

It is a good video. And I would guess that nine in ten people who watch it have no idea what they are looking at: why three cameras, which instrument is making the sound, what the hand on the panel does. The tenth person is the one who matters most to him: another producer, a composer, someone looking for a musician to hire. They want to know exactly that, and the post does not tell them.

So I asked him, with the recorder on.

## What he explained

In his words, it is "a song by Journey" from the eighties, played on a synthesizer that "emulates the Prophet, which was a famous synthesizer" on many albums of the period, with delay and chorus "to replicate the sounds of the original recording". "I put this video to show how it works."

The three keyboards are one keyboard. "I had three cameras shooting, and I synchronized the cameras on Final Cut Pro." It is one take, with no cuts, seen from three angles.

The signal chain in the video, and the trick at the end: decay turned down, so the delay repeats a short chord.

The chain, with the details checked against the makers' own pages:

- **The keyboard has no cable.** It is a small Bluetooth MIDI keyboard; he remembered it as "X Air or something like that", and the keyboard in the video matches CME's Xkey Air. I asked about latency, because Bluetooth headphones lag. His answer: "The Bluetooth has a problem with the protocol that they use for the headphones, but there's a different protocol if you want to connect MIDI." He is right. MIDI over Bluetooth Low Energy, published by the MIDI Association in 2015 from Apple's implementation, sends only small note messages, and the specification requires the connection to update every 15 milliseconds or less, which "places a lower bound on latency". Headphones stream buffered audio, which is where their delay comes from. macOS has supported Bluetooth MIDI since OS X Yosemite, set up in Audio MIDI Setup.
- **The synthesizer is a Behringer Pro-800,** an eight-voice reproduction of the Sequential Prophet-600 from 1982, which shipped in 2023. The Prophet family is the sound of a lot of early-eighties records.
- **Chorus, then delay,** to widen the sound and repeat it, as on the record.

And the trick at the end, which is what the hand on the panel is doing. A synthesizer's envelope shapes each note: how fast it starts (attack) and how fast it falls away (decay). "You play a chord, and you shorten, so the sound, instead of being longer, becomes almost staccato." Then the delay repeats the short chord, so the end of the take turns into a run of staccato echoes, each softer than the last. It is a small, specific technique, and it is exactly what a producer watching the video would want to know.

## What the checking found

Gabriel said it himself while explaining: "They used that Prophet 5, I think. I have to check that out." So the agent checked, and two details changed.

- **The record:** the credits for Frontiers list Jonathan Cain on a Roland Jupiter-8 for the opening track, and Arturia's sound designers, who model the Jupiter-8, name it as the sound of Cain's Separate Ways. A 2026 sale listing of Cain's synthesizers says he also used a Prophet-5 on Escape and Frontiers, which is probably where the memory comes from; I found no interview in which he names the instrument for that riff.
- **His synth:** the Pro-800 is Behringer's reproduction of the Prophet-600, a later and cheaper Sequential instrument than the Prophet-5.

None of that makes the video less good. It makes the explanation better, and it is the kind of correction that only happens when someone writes it down and checks.

## The side-quest that became an article

The best part of the conversation was not planned. Asked how the three cameras worked, he said he had used three old iPhones, two iPhone 12s and an iPhone 13 bought second-hand "because they were cheaper", connected to an iPad running Final Cut Pro, which records all of them live and in sync. "I discovered by accident." "When I discovered this, I was blown away."

That is a technique a lot of musicians, teachers and small event organisers would want, and Gabriel, who knows this world well, had not heard of it until he stumbled on it. If he did not know, there is a universe of people who do not know either. So it is now its own article, [four iPhones and an iPad](four-iphones-and-an-ipad.md), checked against Apple's documentation.

One video, explained by voice the same evening, became two articles once an agent checked and packaged it.

## Why this is the first step

This is what I mean when I tell Gabriel to publish his material, and what [the brief for his Claude](a-website-for-my-brother.md) is built around.

- **Capture it at the moment of creation.** He was about to explain this to me anyway; he loves this stuff, and he is a teacher. If he had waited to write a proper article, he would have overbaked it, and a month later it would not have happened at all.
- **Describe, do not write.** He talks; the agent researches, checks every model name and protocol, finds the sources, drafts, and he approves. Practitioners who talk and an agent that does not make things up are a good combination: it found the evidence and corrected the details.
- **Every explanation is a door.** The video gets a page of its own on his site, with this explanation, the gear, the trick and the sources, and the post on Instagram and YouTube links to it. Someone who likes the video can go much deeper, and the people who might hire him see how he works.
- **The side-quests are the gold.** The multicam technique only came out because he was explaining something else. That is how most of the articles on this site started.
- **The captured ideas compound.** Every idea written down becomes context for the next agent session. Mine get better because they can see the history and the intent behind what I am asking.

And there is a business in it: this newsroom's reading meter lets readers pay a few pence for what they read, without being patrons, so explanations like this one can earn something on their own.

## What this does not claim

- **The explanation is Gabriel's,** from a recorded conversation of 2 November 2026; the agent checked the model names, the protocol and the record against public sources.
- **The keyboard is identified from his description and the video,** as CME's Xkey Air; the latency figures are the specification's lower bound, not a measurement of his setup.
- **The rack unit** marked Tegeler Audio Manufaktur is not identified for certain and is left out of the chain.
- **The original synth** is from the album credits and a sound designer's note; no first-person interview with Jonathan Cain naming it was found.

## Where this comes from

Gabriel's video, from his YouTube channel @gabrieldacruz_composer, and the conversation of 2 November 2026. [Separate Ways (Worlds Apart)](https://en.wikipedia.org/wiki/Separate_Ways_%28Worlds_Apart%29) and [Frontiers](https://en.wikipedia.org/wiki/Frontiers_%28Journey_album%29) (release dates and credits); [Arturia's Jup-8 V sound design notes](https://www.arturia.com/products/software-instruments/jup-8-v/sounddesign); [Behringer Pro-800](https://www.behringer.com/en/products/0718-ABF) and [MusicTech on its Prophet-600 basis](https://musictech.com/news/behringer-unveils-its-pro-800-based-on-sequentials-prophet-600); [Sequential](https://sequential.com/about/); [CME Xkey Air](https://xkeyair.com/xkey-air/); [the MIDI Association on BLE-MIDI](https://midi.org/midi-over-bluetooth-low-energy-ble-midi); [Apple's Audio MIDI Setup guide](https://support.apple.com/guide/audio-midi-setup/ams33f013765/mac); [Sound On Sound on ADSR envelopes](https://www.soundonsound.com/glossary/adsr-attack-decay-sustain-release). All read 2 November 2026; quotes in the research notes.

## Threads

News & evidenceAgents & policy[This article as a graph →](graphs.md#separate-ways-explained)

### Builds on

- [Four iPhones and an iPad: how my brother filmed a three-camera music video with old phones synced live to Final Cut Pro, a feature Apple shipped in 2024 that he found by accident](four-iphones-and-an-ipad.md) Three old iPhones and an iPad, synced live in Final Cut Pro: Apple's Live Multicam, found by accident.
- [A website for my brother: a brief for Gabriel DaCruz's Claude, to rebuild gabrieldacruz.com on GitHub Pages and Google Workspace, interview him every day, and tell the story of a musician who will not tell it himself](a-website-for-my-brother.md) A brief for Gabriel DaCruz's Claude: his site on GitHub Pages, Google Workspace, daily interviews and a newsroom.

### Continued by

- [Sellable units: applying api.newsroom.sgit.ai to my brother's website, the reading meter on a composer's site that does not look like a newsroom, the pathways from a viewer to a buyer, and every lesson, score and master as something to sell](sellable-units.md) The newsroom's reading meter on a composer's site: sellable units, pathways to a buyer, and CC BY with a paid licence.
- [Four iPhones and an iPad: how my brother filmed a three-camera music video with old phones synced live to Final Cut Pro, a feature Apple shipped in 2024 that he found by accident](four-iphones-and-an-ipad.md) Three old iPhones and an iPad, synced live in Final Cut Pro: Apple's Live Multicam, found by accident.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 361 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=361)

**Posting this article on LinkedIn?** The cover is [separate-ways-explained.jpg](banners/separate-ways-explained.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/separate-ways-explained.html)*
