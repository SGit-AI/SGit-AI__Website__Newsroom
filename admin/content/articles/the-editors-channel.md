---
title: The editor's channel: what I read, sign off and want changed, sent to the newsroom's agent in a vault
date: 2026-10-18
author: Dinis Cruz
author_url: about/index.html
summary: Most of what I tell this newsroom's agent I type into a chat, and most of it is about something I was reading a minute earlier: this sentence is over the top, that figure is too big, this one is fine, ship it. The chat loses where I was. The site already has most of a better channel: a lane I send notes down, an inbox any browser can append to, a vault that carries my reading between devices. What it does not have is an editor's channel, where what I read, what I sign off and what I want changed reaches the agent on its own, and where the agent answers. This proposes one. A browser becomes an editor's when it is given a key, made by the agent or by another editor; without it, the site is the plain reader's site, unchanged. With it, on newsroom pages only, my reads, my sign-offs against the article's version, my fixes with the phrase selected and my tweaks go up to an editor vault, a subset of my reading account and never all of it. Once a day, and whenever I press a button, an agent with a written mandate reads the vault, runs the checks, such as the wording check I asked for today, applies what is cheap to undo, proposes the rest, and writes back. Around it are five audiences, from the plain reader who sends nothing to the editor who sends everything, each with its own lane and its own key: an anonymous append lane behind a checkbox, a named reader's lane, and the two-way editor's vault. The keys are shared secrets today. They should become key pairs, one per person and per agent, and the inbox already uses one. Another agent on this site builds the vault pane; the brief for it is linked at the end.
version: v0.12.106
license: https://creativecommons.org/licenses/by/4.0/
tags: newsroom, editor, feedback-loop, vaults, append-lanes, agents, privacy, pki, brief, article
status: published
---

!shot ec-channel.webp | images/ | The editor's channel. A key turns a browser into an editor's; on newsroom pages it sends what I read, sign off and want changed to an editor vault; a daily pass, or a press, reads it, runs the checks, acts and replies. Below, five audiences, each a lane with its own key: the plain reader sends nothing; a reader with a vault syncs only their own devices; an anonymous checkbox appends a little and reads nothing back; a named reader sends notes they choose; an editor sends everything and gets answers. | concept

## In short {#in-short}

- **Editing happens in a chat, away from the page.** The chat loses which sentence, which version, which figure.
- **Most of a better channel exists.** A lane for notes, an inbox any browser can append to, a vault across devices.
- **What is missing is an editor's channel.** Reads, sign-offs and fixes reaching the agent on their own, and answers coming back.
- **A key turns a browser into an editor's.** Without it, the plain reader's site, unchanged.
- **An editor vault holds a subset of my account.** Newsroom pages only, and only the kinds I choose.
- **A daily pass reads it, and so does a button.** Checks, cheap fixes released, the rest proposed, a report back.
- **Five audiences, five lanes.** From sending nothing, through an anonymous checkbox, to two-way.
- **Shared keys now, key pairs later.** The inbox already seals to a public key; the rest should follow.

## The problem with editing in a chat {#chat}

Today I asked this site's agent to stop writing sentences like "the clearest example I have seen". It had used one in an article I was reading, and it was the kind of claim that loses a reader's trust. The fix took minutes: the agent found every case in the recent articles, rewrote them, and added a check so the next one fails before it is committed.

But look at how the request got there. I was reading on one device, I noticed the phrase, and I went to a chat on another to describe it from memory. The agent then had to search for which article I meant. That is most of my editing: a sentence is wrong, a figure is too big, a section can go, this piece is fine. Each one starts on a page, at a version, with a phrase selected, and each one arrives in the chat stripped of all of that.

The other half is worse. When I read an article and it is fine, nothing happens. The agent never learns that I read it, how far I got, or that I would have signed it off. A sign-off I do not record is one the agent cannot count on, so the gap between what was published and what I have reviewed stays invisible.

## What already exists {#exists}

This site has built most of the pieces, for readers rather than for editors.

- **The vault pane.** Every reader's reading, notes and personas live in their browser, and, if they choose, in a reader vault they own, opened with a passkey and synced between their devices. The newsroom has no key to it. [The activity vault](https://newsroom.sgit.ai/admin/notes/2026-10-12__the-activity-vault.md) is the design.
- **The lane.** A note is one tap at a piece: done, read later, follow up, wrong, fix this, idea, with the phrase that was selected. *Send to the newsroom* puts the notes not yet sent into a vault of their own and hands the newsroom its read key, once. `admin/build/lane.py` reads it. [The feedback loop](https://newsroom.sgit.ai/admin/notes/2026-10-12__the-feedback-loop.md) is the design, and the first lane I sent changed the pane the same day.
- **The inbox.** An append lane on the reader vault that any browser with a link can write to and none can read, with a key pair made in the reader's browser: messages are sealed to the public key, and the private key stays in the reader's master vault. [Send to my vault from any browser](https://newsroom.sgit.ai/admin/notes/2026-10-13__send-to-my-vault-from-any-browser.md) is the design, and [sixteen notes I did not want to lose](/articles/sixteen-notes-i-did-not-want-to-lose.html) is why.

Two things are missing. The lane only goes one way: the feedback-loop note says it plainly, "What the lane is not: a channel the newsroom can write back on." And nothing reads the lane unless I ask an agent to.

## A key that makes a browser an editor's {#key}

I do not want to change the reader's site to get this. The plain reader should see what they see today, send nothing, and never be asked about editors.

So the switch is a key. The agent, or another editor, makes an editor key for a browser and hands it over the way the inbox link is handed over, in the fragment of a link that never reaches a server, or as a QR code. The browser keeps it, and from then on, on newsroom pages, it is in editor mode. Without the key, the code that does any of this never runs.

There are two ways to build what the key opens, and I think the answer is both, one on top of the other.

- **An editor vault.** A vault of its own, shared by the editors and the agent, that holds a subset of my reading account: what I read on this site, and the notes I make here. Not the meter's spend, not my personas, not my other devices' history. The agent gets access to this vault and to nothing of mine beyond it.
- **A mode in the browser.** The key is how a browser joins that vault. Once it has it, the newsroom's code syncs the kinds of activity I chose, as I read, without a button: read, how far, signed off, fix this with the phrase, a message, and the tweaks I make to a page with the site's primitives, the ones [fix the page yourself](/articles/fix-the-page-yourself.html) argued every site should publish.

One new kind of note matters most: **Signed off**, against the version of the article I read. If the article changes after that, the sign-off is stale, the same way a section summary on this site goes stale when its section changes. The agent can then say, for every article, whether the version that is live is the version I signed off.

## The daily pass {#pass}

The other half is an agent that reads the vault without being asked. Once a day, and whenever I press *Process now* in the pane, the pass does the same work:

1. **Pull the editor vault** and group what arrived by article and version.
2. **Record the sign-offs.** Which live versions are signed off, which are stale, which were never read.
3. **Run the checks** on the articles I read: the wording check added today, links, mobile widths, quotes against their sources, summaries against their sections.
4. **Act on what is cheap to undo.** A wording fix, a figure resized, a section removed when I said to: applied, released, and named in the version row by page and kind of note. [How cheap is it to undo](/articles/how-cheap-is-it-to-undo.html) is the test: an article is a two-way door, so the pass can release; an email is not, so it never sends one.
5. **Propose the rest.** Anything that changes an argument, a claim or a title goes back as a proposal, not a change.
6. **Write back.** A report into the vault's down lane, which the pane shows under the article it is about: what was done, what is proposed, what was refused and why.

The pass is an agent with a policy, like every agent on this site: a grant, the editor vault and the newsroom repository; a mandate, act on the editors' notes; and the limits, written down, as [three policies for an agent](/articles/three-policies-for-an-agent.html) describes. The pass can also be triggered from a chat, which keeps the channel I use today working while this one is built.

## Five audiences, five lanes {#audiences}

Once there is an editor's channel, the same design answers a question I have had for a while: how much should a browser send, and to whom? I think the answer is five audiences, each with its own lane and its own key, and the reader chooses which one they are in.

| Audience | What leaves the browser | Key |
|---|---|---|
| The plain reader | Nothing | None |
| A reader with a vault | Their records, to their own devices | Their vault key |
| Anonymous, by a checkbox | Page, kind of note, phrase | An append token |
| A named reader | The notes they choose to send | A read key, handed over |
| An editor | Reads, sign-offs, fixes, tweaks | Read and write |

The anonymous lane is the new one. A checkbox in the pane, off by default, that says what it sends. When it is on, a tap at a piece appends a small record to the newsroom's lane: the page, the kind of note, the phrase if one was selected. No account, no device id, no reading history, and the browser cannot read anything back, its own records included. The append lanes already work this way; [agent workflows on ephemeral vaults](/articles/agent-workflows-on-ephemeral-vaults.html) measured a hundred writers posting to one at once. More information can be offered as a second box, the persona or the device type, but each extra field is one the reader turns on.

## Keys, and then key pairs {#pki}

Two kinds of access do almost everything here. **Two-way** is a vault's read and write keys, held by both sides: the editors and the agent read and write the editor vault. **Append-only** is a token that can add and nothing else: the anonymous lane and the inbox.

Both are shared secrets today. A key given to an agent can be copied, and the only way to take it back is to make a new vault or a new token. That is fine for one editor and one agent. It does not hold for a desk.

The direction is a key pair per person and per agent. A message is signed by whoever wrote it and sealed to whoever should read it. Access to the editor vault is granted to a public key, and revoked by removing it, without changing anyone else's. The inbox already does half of this: every message to it is sealed to a public key made in the reader's browser. What is missing is the signature, so the drain knows who wrote a message rather than only that someone had the link, and the per-person grant on the vault, which is sgit's to provide.

## Where this stands {#stands}

The vault pane, the lane, the inbox and the append lanes are built and in use. The editor key, the editor vault, the Signed off note, the down lane, the anonymous checkbox and the daily pass are not. Another agent on this site, the one that built the vault pane, builds the browser side; the pass is mine. The map between them is a brief: [the editor's channel](https://newsroom.sgit.ai/admin/notes/2026-10-18__the-editors-channel.md), with what exists, what to build in which order, and the tests that would show it works.

## What this does not claim {#limits}

- **Nothing in the editor's channel is built.** The lane, the inbox and the append lanes are; the rest is a design.
- **One editor so far.** The design is for a desk; it has been used by one person.
- **Shared keys are not identity.** Until there are key pairs, a lane says that someone had the key, not who.
- **The anonymous lane is not anonymous against everything.** The server sees when an append arrived and from where; the record carries no identity, but traffic can.
- **The pass acting on its own is limited to what is cheap to undo.** A claim, an argument or a title stays a proposal.
- **Editor mode syncs as I read.** That is more data than the lane sends, and the reason it is scoped to newsroom pages and to the kinds of note I turn on.

If you run a desk and want to try an editor's channel with an agent, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo from me on 18 October 2026, after asking the agent to remove over-the-top phrases and add a check for them. The designs it builds on are this site's notes: [the activity vault](https://newsroom.sgit.ai/admin/notes/2026-10-12__the-activity-vault.md), [the feedback loop](https://newsroom.sgit.ai/admin/notes/2026-10-12__the-feedback-loop.md), [send to my vault from any browser](https://newsroom.sgit.ai/admin/notes/2026-10-13__send-to-my-vault-from-any-browser.md) and [the vault, opened](https://newsroom.sgit.ai/admin/notes/2026-10-16__the-vault-opened.md). The wording check is `admin/build/wording.py`. Related: [sixteen notes I did not want to lose](/articles/sixteen-notes-i-did-not-want-to-lose.html), [fix the page yourself](/articles/fix-the-page-yourself.html), [how cheap is it to undo](/articles/how-cheap-is-it-to-undo.html), [three policies for an agent](/articles/three-policies-for-an-agent.html), [agent workflows on ephemeral vaults](/articles/agent-workflows-on-ephemeral-vaults.html). Written up and checked by this site's agent; the editorial responsibility is mine.
