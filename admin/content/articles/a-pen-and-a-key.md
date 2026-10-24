---
title: A pen and a key: a place on every page to mark it, comment on it and tell the newsroom, and a browser key that pki.sgit.ai vouches for, so a note can be checked as mine
date: 2026-10-24
author: Dinis Cruz
author_url: about/index.html
summary: I read this newsroom on an iPad more than anywhere else, and the way I give it feedback has been a chat window and screenshots. On the page itself, selecting a sentence brings up the iPad's own Copy, Look Up and Translate menu, right where the site's Highlight button was, so the button was hidden under it. So every article now has a Pen, beside the Vault in the bar at the top. Select words and a small bar appears at the foot of the screen, away from the iPad's menu: keep them, comment on them, or tell the newsroom. The Pen opens on the right with three parts: what is selected; my marks on this page, with comments of my own that stay in my browser; and notes for the newsroom, with the passage they are about, which go when I send them, down the lane my vault already has. The fourth part is the one I care most about. pki.sgit.ai now has a register of people and their public keys, with my key as its anchor, and a rule for one key to vouch for another: an operates link, both ways, with an end date. A browser can use the same rule. The Pen makes a key for this browser with pki.sgit.ai's own code, and once my key on pki.sgit.ai says it operates that browser, every note I send from it is signed, and anyone can check it against the public register: the newsroom's lane reader does it in Python, a page does it in the browser. I looked at four ways to log in here with my pki.sgit.ai key: one passkey for both sites, a sign-in redirect like OAuth, a key per browser vouched for in the register, and the same by QR code. The key per browser works today, with nothing new on pki.sgit.ai; the redirect is the better end state; the shared passkey is a wider door than either site needs. The two vaults stay two vaults, connected by keys rather than by a shared door.
version: v0.13.64
license: https://creativecommons.org/licenses/by/4.0/
tags: pen, feedback, pki, keys, identity, signatures, vault, editor, reading, article
status: published
---

!shot pn-pen.webp | images/ | An article with the Pen open on the right, at 1280 pixels wide in the Newsprint theme. In the article, a highlighted sentence. In the Pen, from the top: what is selected; the reader's own marks on this page, private, with a comment; and Tell the newsroom, with a note kept with the passage it is about and waiting to be sent. Below them, out of the picture, Signed as you: this browser's key and what the register says about it. | screenshot

## In short {#in-short}

- **Feedback on this site went through a chat window.** I read on an iPad, and the page itself had nowhere good to put what I thought.
- **The iPad's own menu covered the Highlight button.** Selecting words brings up Copy, Look Up and Translate above the selection, exactly where the button sat.
- **Every article now has a Pen.** A button beside the Vault; a bar at the foot of the screen while words are selected; a panel on the right.
- **My marks are mine.** A highlight with a comment, kept in my browser and drawn on the page, never sent.
- **Notes for the newsroom go when I send them.** With the passage they are about, as the vault pane's own notes, down my own lane.
- **A note can be signed, and checked by anyone.** A key for this browser, vouched for by my key on pki.sgit.ai, signs each note; the register says whether to believe it.
- **Four ways to log in with my pki.sgit.ai key.** One passkey for both sites, a sign-in redirect, a key per browser in the register, the same by QR code.
- **The key per browser works now.** It uses the register's own rule for agents, both ways and dated, and nothing new on pki.sgit.ai.
- **Two vaults, connected by keys.** The reader vault and my pki.sgit.ai account stay separate; keys, not a shared door, connect them.

## Feedback through a chat window {#chat}

Most of what I tell this newsroom I type into a chat with its agent, and most of it is about something I read a minute earlier: this sentence is over the top, this figure is wrong, this one is good. I wrote about the problem in [the editor's channel](/articles/the-editors-channel.html): the chat loses where I was. And in [reading with a pen](/articles/reading-with-a-pen.html) I described the three moments of reading, reading, marking the page, and processing what you marked, and how much I want the second and third to work on a screen the way they now work for me on paper.

The site has had pieces of it for a while. A Highlight button appears when you select words in an article. The vault pane has notes, done, fix this, wrong, idea, with the phrase you selected, and a lane that carries them to the newsroom. But the pieces were in different places, behind different buttons, and on the device I read on most, one of them did not work.

## The iPad's menu was in the way {#ipad}

On an iPad, selecting words in Safari brings up the system's own menu, Copy, Look Up, Translate, Find, just above the selection. That is exactly where the site put its Highlight button, so on an iPad the button sat under the menu. It was not a bug in either; they simply wanted the same place.

!shot pn-ipad.webp | images/ | Two ways to place a button for selected words on an iPad. Left, as it was: the button above the selection, under the system's Copy, Look Up and Translate menu. Right, as it is now: the Highlight button below the selection, and the Pen's bar at the foot of the screen with Keep, Comment and Tell the newsroom. Drawn, not a screenshot. | comparison

Two changes fix it. On a touch screen the Highlight button now goes below the selection, not above it. And while words are selected, a small bar appears at the foot of the screen, out of the menu's way, with three choices: keep the words, comment on them, or tell the newsroom. The Pen keeps the selection the moment it is made, so a tap that clears the selection, as taps on an iPad often do, no longer loses it.

## A Pen on every article {#pen}

The Pen is a button in the bar at the top of every article, beside the Vault. It opens a panel on the right, and the page moves over to make room, so I can read and write at the same time. It has four parts.

- **Selected.** What I have just selected, with keep it, keep it with a comment, or tell the newsroom.
- **Your marks on this page.** The highlights on this page, each with a comment of my own if I want one. They are kept in this browser and drawn on the page, and they are private: nothing sends them anywhere.
- **Tell the newsroom.** A note about this page, of a kind (fix this, wrong, idea, liked, or just words), with the passage it is about. It is the same record the vault pane keeps, so it travels with my vault to my other devices, and it goes to the newsroom only when I press Send, down the lane my vault already has.
- **Signed as you.** Who is holding the pen, which is the new part.

## A key that the register vouches for {#key}

[pki.sgit.ai](https://pki.sgit.ai/) now has [a register of people and their public keys](/articles/a-directory-of-people-and-keys.html), with my key as its anchor. It also has a rule for one key to vouch for another, built for agents: an agent's key is operated by a person when the person's record links to it with *operates* and an end date, and the agent's record links back with *operated-by*. A link only counts when it goes both ways, and it ends when its date does. That is the [first pattern from PKI everywhere](/articles/pki-everywhere.html): a key the session makes for itself, which a person vouches for.

A browser is the same kind of thing as an agent: something that acts for me, for a while. So the Pen makes a key pair for this browser with pki.sgit.ai's own code, which the newsroom now carries unedited, signs two statements, who it is and that I operate it, and gives me the submission for the register. Once the register holds it and my key on pki.sgit.ai says it operates that browser, every note I keep in the Pen is signed with it.

!shot pn-chain.webp | images/ | How a note is checked as mine. This browser's key signs the note. The register at pki.sgit.ai holds the browser's record, which says it is operated by my key, and my record, which says I operate it until a date. The newsroom pins my key as the root, reads the register, checks the signature against the browser's key and the chain back to the root, and marks the note signed and checked, valid but not vouched for, or failing. | diagram

The check is the part that matters. Anyone can do it, from the public register, without taking the newsroom's word for it: a page does it in the browser with the register's own code, and the newsroom's lane reader does it in Python when it reads my notes. Both start from a pinned root, my key's fingerprint, never from whatever the register's list of anchors says, because whoever can change a site can change that list. A note from this browser then reads as "signed and checked: operated by the root until" its date. A note changed after it was signed fails. A key nobody vouches for is valid and says so.

## Four ways to log in {#login}

The question behind all of this is how I log in here with my pki.sgit.ai key. The two sites share a design and code: pki.sgit.ai's passkey door is this site's, copied with one constant changed. They differ on purpose in two places. Each passkey belongs to its own host, and each site derives its own door from it. So the same passkey cannot open both, and would open two different doors if it could. There are four ways through.

!shot pn-options.webp | images/ | Four ways to log in to newsroom.sgit.ai with a pki.sgit.ai key, compared on what it needs from pki.sgit.ai, the steps for the person, where the private key lives, and the decision: a key per browser in the register now, the same by QR code next, a sign-in redirect when pki.sgit.ai has a page for it, and not one passkey for both sites. | comparison

- **One passkey for both sites.** Both could ask for passkeys made for sgit.ai, and then one passkey works on both. But every passkey made so far is for its own host, so everyone would make a new one, and it would let every sgit.ai site ask for the same passkey, a wider door than either needs. Not now.
- **Sign in with pki.sgit.ai.** The newsroom sends me to pki.sgit.ai with a key it made for this browser; pki.sgit.ai, where I am signed in, signs "this key acts for me here until this date" and sends me back. One click, and my private key never leaves pki.sgit.ai. It needs a page on pki.sgit.ai that does not exist yet. The best end state.
- **A key per browser, in the register.** What the Pen does now: three steps the first time, nothing new on pki.sgit.ai.
- **The same, by QR code.** The browser's key shown as a QR code, scanned on my phone where pki.sgit.ai is open, which signs the link. The copying done by the camera, as [a secret is a QR code](/articles/a-secret-is-a-qr-code.html) proposes.

So the key per browser now, the QR code next to it, and the redirect when pki.sgit.ai has an authorize page. The browser key and the checks stay the same in all three; only the way the link is made changes.

## Two vaults, connected by keys {#vaults}

The reader vault here and my account on pki.sgit.ai stay two vaults, with two doors, on two hosts. Merging them would mean one site's code could read the other's vault, and a bug in either becomes a bug in both. They are connected by keys instead. The browser key is the first connection. The next is to keep it in the reader vault's master, so every device that opens my vault can sign. And the reader vault's own key can be handed to pki.sgit.ai sealed to my key, the way pki.sgit.ai already hands over vault keys, so my pki.sgit.ai account holds the key to my newsroom vault, and the newsroom holds nothing of my account there.

A login area, then, is not an account on a server. It is the Pen's signed section and the vault pane: who holds the pen, what the register says about them, and the notes they have sent and their state. It is a place of my own because the key is mine.

## Where this stands {#stands}

The Pen is on every article from this release, with the bar at the foot, the private marks, the notes with their passages and the signing. The lane reader checks signed notes against the register, and a test signs notes, checks them in Python and in the browser against a register of its own, and changes one to show that it then fails. What I still have to do myself is the first link: send the submission for the browser I read on, and link to it from my key on pki.sgit.ai. What is left to build: the authorize page and the QR code on pki.sgit.ai; the browser key kept in the reader vault's master; the newsroom's own feedback lane, published as an inbox in the register, so a reader with no vault can send a note too; and the agent's daily pass reading signed notes first.

## What this does not claim {#limits}

- **No note has been signed and checked against the live register yet.** The check is tested against a register and a root the test makes; my own browser's key is not in the register until I send its submission and link to it.
- **The browser's private key is kept in the browser's storage.** It is worth what its link says and the link ends on a date, but it is not in a vault yet.
- **A note still needs the vault's lane to reach the newsroom.** The newsroom's own lane, for readers with no vault, is not built.
- **The redirect and the QR code are proposals.** They need pages on pki.sgit.ai.
- **The iPad figure is drawn, not a screenshot.** The fix was tested in a browser at phone width, not on an iPad.
- **The register's code is pki.sgit.ai's, copied.** A fix there reaches this site when the copy is refreshed, with its hashes.

If you read this newsroom and want to tell it something about a page, open the Pen on that page; if you would like to try signing your notes too, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo of mine on 24 October 2026, made on an iPad while reading the newsroom, with a screenshot of the iPad's menu over a selection, written by this site's agent in the voice of this site. The argument and the editorial responsibility are mine. pki.sgit.ai as it was on 24 October 2026 (v0.2.25): its [machine-readable guide](https://pki.sgit.ai/llms.txt), its register at https://pki.sgit.ai/directory/index.json and anchors, and its modules `keys.js` and `directory.js`, which this site now carries unedited in `assets/vendor/pki/v0.2.25/` with their hashes. The design and the options compared: `admin/notes/2026-10-24__signing-in-with-a-public-key.md`. The code: `assets/pen/pen.js`, `assets/pen/identity.js`, `admin/build/lane.py`, and the test `admin/build/test_pen.mjs`; card 090 in this site's engineering record. Related: [reading with a pen](/articles/reading-with-a-pen.html), [the editor's channel](/articles/the-editors-channel.html), [PKI everywhere](/articles/pki-everywhere.html), [a directory of people and keys](/articles/a-directory-of-people-and-keys.html), [a secret is a QR code](/articles/a-secret-is-a-qr-code.html), [a newsroom for one](/articles/a-newsroom-for-one.html).
