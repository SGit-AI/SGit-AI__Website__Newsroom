# The editor's channel: what I read, sign off and want changed, sent to the newsroom's agent in a vault, sgit.ai

> Most of what I tell this newsroom's agent I type into a chat, and most of it is about something I was reading a minute earlier: this sentence is over the top, that figure is too big, this one is fine, ship it. The chat loses where I was. The site already has most of a better channel: a lane I send notes down, an inbox any browser can append to, a vault that carries my reading between devices. What it does not have is an editor's channel, where what I read, what I sign off and what I want changed reaches the agent on its own, and where the agent answers. This proposes one. A browser becomes an editor's when it is given a key, made by the agent or by another editor; without it, the site is the plain reader's site, unchanged. With it, on newsroom pages only, my reads, my sign-offs against the article's version, my fixes with the phrase selected and my tweaks go up to an editor vault, a subset of my reading account and never all of it. Once a day, and whenever I press a button, an agent with a written mandate reads the vault, runs the checks, such as the wording check I asked for today, applies what is cheap to undo, proposes the rest, and writes back. Around it are five audiences, from the plain reader who sends nothing to the editor who sends everything, each with its own lane and its own key: an anonymous append lane behind a checkbox, a named reader's lane, and the two-way editor's vault. The keys are shared secrets today. They should become key pairs, one per person and per agent, and the inbox already uses one. Another agent on this site builds the vault pane; the brief for it is linked at the end.

*Source: <https://newsroom.sgit.ai/articles/the-editors-channel.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The editor's channel: what I read, sign off and want changed, sent to the newsroom's agent in a vault

# The editor's channel: what I read, sign off and want changed, sent to the newsroom's agent in a vault

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-18 · [article v1.0.0](versions/the-editors-channel.md) · [newsroom v0.12.106](https://newsroom.sgit.ai/admin/versions.html) · newsroomeditorfeedback-loopvaultsappend-lanesagentsprivacypkibriefarticle

***Abstract:** Most of what I tell this newsroom's agent I type into a chat, and most of it is about something I was reading a minute earlier: this sentence is over the top, that figure is too big, this one is fine, ship it. The chat loses where I was. The site already has most of a better channel: a lane I send notes down, an inbox any browser can append to, a vault that carries my reading between devices. What it does not have is an editor's channel, where what I read, what I sign off and what I want changed reaches the agent on its own, and where the agent answers. This proposes one. A browser becomes an editor's when it is given a key, made by the agent or by another editor; without it, the site is the plain reader's site, unchanged. With it, on newsroom pages only, my reads, my sign-offs against the article's version, my fixes with the phrase selected and my tweaks go up to an editor vault, a subset of my reading account and never all of it. Once a day, and whenever I press a button, an agent with a written mandate reads the vault, runs the checks, such as the wording check I asked for today, applies what is cheap to undo, proposes the rest, and writes back. Around it are five audiences, from the plain reader who sends nothing to the editor who sends everything, each with its own lane and its own key: an anonymous append lane behind a checkbox, a named reader's lane, and the two-way editor's vault. The keys are shared secrets today. They should become key pairs, one per person and per agent, and the inbox already uses one. Another agent on this site builds the vault pane; the brief for it is linked at the end.*

The editor's channel. A key turns a browser into an editor's; on newsroom pages it sends what I read, sign off and want changed to an editor vault; a daily pass, or a press, reads it, runs the checks, acts and replies. Below, five audiences, each a lane with its own key: the plain reader sends nothing; a reader with a vault syncs only their own devices; an anonymous checkbox appends a little and reads nothing back; a named reader sends notes they choose; an editor sends everything and gets answers.

## In short

- **Editing happens in a chat, away from the page.** The chat loses which sentence, which version, which figure.
- **Most of a better channel exists.** A lane for notes, an inbox any browser can append to, a vault across devices.
- **What is missing is an editor's channel.** Reads, sign-offs and fixes reaching the agent on their own, and answers coming back.
- **A key turns a browser into an editor's.** Without it, the plain reader's site, unchanged.
- **An editor vault holds a subset of my account.** Newsroom pages only, and only the kinds I choose.
- **A daily pass reads it, and so does a button.** Checks, cheap fixes released, the rest proposed, a report back.
- **Five audiences, five lanes.** From sending nothing, through an anonymous checkbox, to two-way.
- **Shared keys now, key pairs later.** The inbox already seals to a public key; the rest should follow.

## The problem with editing in a chat

Today I asked this site's agent to stop writing sentences like "the clearest example I have seen". It had used one in an article I was reading, and it was the kind of claim that loses a reader's trust. The fix took minutes: the agent found every case in the recent articles, rewrote them, and added a check so the next one fails before it is committed.

But look at how the request got there. I was reading on one device, I noticed the phrase, and I went to a chat on another to describe it from memory. The agent then had to search for which article I meant. That is most of my editing: a sentence is wrong, a figure is too big, a section can go, this piece is fine. Each one starts on a page, at a version, with a phrase selected, and each one arrives in the chat stripped of all of that.

The other half is worse. When I read an article and it is fine, nothing happens. The agent never learns that I read it, how far I got, or that I would have signed it off. A sign-off I do not record is one the agent cannot count on, so the gap between what was published and what I have reviewed stays invisible.

## What already exists

This site has built most of the pieces, for readers rather than for editors.

- **The vault pane.** Every reader's reading, notes and personas live in their browser, and, if they choose, in a reader vault they own, opened with a passkey and synced between their devices. The newsroom has no key to it. [The activity vault](https://newsroom.sgit.ai/admin/notes/2026-10-12__the-activity-vault.md) is the design.
- **The lane.** A note is one tap at a piece: done, read later, follow up, wrong, fix this, idea, with the phrase that was selected. *Send to the newsroom* puts the notes not yet sent into a vault of their own and hands the newsroom its read key, once. `admin/build/lane.py` reads it. [The feedback loop](https://newsroom.sgit.ai/admin/notes/2026-10-12__the-feedback-loop.md) is the design, and the first lane I sent changed the pane the same day.
- **The inbox.** An append lane on the reader vault that any browser with a link can write to and none can read, with a key pair made in the reader's browser: messages are sealed to the public key, and the private key stays in the reader's master vault. [Send to my vault from any browser](https://newsroom.sgit.ai/admin/notes/2026-10-13__send-to-my-vault-from-any-browser.md) is the design, and [sixteen notes I did not want to lose](sixteen-notes-i-did-not-want-to-lose.md) is why.

Two things are missing. The lane only goes one way: the feedback-loop note says it plainly, "What the lane is not: a channel the newsroom can write back on." And nothing reads the lane unless I ask an agent to.

## A key that makes a browser an editor's

I do not want to change the reader's site to get this. The plain reader should see what they see today, send nothing, and never be asked about editors.

So the switch is a key. The agent, or another editor, makes an editor key for a browser and hands it over the way the inbox link is handed over, in the fragment of a link that never reaches a server, or as a QR code. The browser keeps it, and from then on, on newsroom pages, it is in editor mode. Without the key, the code that does any of this never runs.

There are two ways to build what the key opens, and I think the answer is both, one on top of the other.

- **An editor vault.** A vault of its own, shared by the editors and the agent, that holds a subset of my reading account: what I read on this site, and the notes I make here. Not the meter's spend, not my personas, not my other devices' history. The agent gets access to this vault and to nothing of mine beyond it.
- **A mode in the browser.** The key is how a browser joins that vault. Once it has it, the newsroom's code syncs the kinds of activity I chose, as I read, without a button: read, how far, signed off, fix this with the phrase, a message, and the tweaks I make to a page with the site's primitives, the ones [fix the page yourself](fix-the-page-yourself.md) argued every site should publish.

One new kind of note matters most: **Signed off**, against the version of the article I read. If the article changes after that, the sign-off is stale, the same way a section summary on this site goes stale when its section changes. The agent can then say, for every article, whether the version that is live is the version I signed off.

## The daily pass

The other half is an agent that reads the vault without being asked. Once a day, and whenever I press *Process now* in the pane, the pass does the same work:

1. **Pull the editor vault** and group what arrived by article and version.
2. **Record the sign-offs.** Which live versions are signed off, which are stale, which were never read.
3. **Run the checks** on the articles I read: the wording check added today, links, mobile widths, quotes against their sources, summaries against their sections.
4. **Act on what is cheap to undo.** A wording fix, a figure resized, a section removed when I said to: applied, released, and named in the version row by page and kind of note. [How cheap is it to undo](how-cheap-is-it-to-undo.md) is the test: an article is a two-way door, so the pass can release; an email is not, so it never sends one.
5. **Propose the rest.** Anything that changes an argument, a claim or a title goes back as a proposal, not a change.
6. **Write back.** A report into the vault's down lane, which the pane shows under the article it is about: what was done, what is proposed, what was refused and why.

The pass is an agent with a policy, like every agent on this site: a grant, the editor vault and the newsroom repository; a mandate, act on the editors' notes; and the limits, written down, as [three policies for an agent](three-policies-for-an-agent.md) describes. The pass can also be triggered from a chat, which keeps the channel I use today working while this one is built.

## Five audiences, five lanes

Once there is an editor's channel, the same design answers a question I have had for a while: how much should a browser send, and to whom? I think the answer is five audiences, each with its own lane and its own key, and the reader chooses which one they are in.

| Audience | What leaves the browser | Key |
|---|---|---|
| The plain reader | Nothing | None |
| A reader with a vault | Their records, to their own devices | Their vault key |
| Anonymous, by a checkbox | Page, kind of note, phrase | An append token |
| A named reader | The notes they choose to send | A read key, handed over |
| An editor | Reads, sign-offs, fixes, tweaks | Read and write |

The anonymous lane is the new one. A checkbox in the pane, off by default, that says what it sends. When it is on, a tap at a piece appends a small record to the newsroom's lane: the page, the kind of note, the phrase if one was selected. No account, no device id, no reading history, and the browser cannot read anything back, its own records included. The append lanes already work this way; [agent workflows on ephemeral vaults](agent-workflows-on-ephemeral-vaults.md) measured a hundred writers posting to one at once. More information can be offered as a second box, the persona or the device type, but each extra field is one the reader turns on.

## Keys, and then key pairs

Two kinds of access do almost everything here. **Two-way** is a vault's read and write keys, held by both sides: the editors and the agent read and write the editor vault. **Append-only** is a token that can add and nothing else: the anonymous lane and the inbox.

Both are shared secrets today. A key given to an agent can be copied, and the only way to take it back is to make a new vault or a new token. That is fine for one editor and one agent. It does not hold for a desk.

The direction is a key pair per person and per agent. A message is signed by whoever wrote it and sealed to whoever should read it. Access to the editor vault is granted to a public key, and revoked by removing it, without changing anyone else's. The inbox already does half of this: every message to it is sealed to a public key made in the reader's browser. What is missing is the signature, so the drain knows who wrote a message rather than only that someone had the link, and the per-person grant on the vault, which is sgit's to provide.

## Where this stands

The vault pane, the lane, the inbox and the append lanes are built and in use. The editor key, the editor vault, the Signed off note, the down lane, the anonymous checkbox and the daily pass are not. Another agent on this site, the one that built the vault pane, builds the browser side; the pass is mine. The map between them is a brief: [the editor's channel](https://newsroom.sgit.ai/admin/notes/2026-10-18__the-editors-channel.md), with what exists, what to build in which order, and the tests that would show it works.

## What this does not claim

- **Nothing in the editor's channel is built.** The lane, the inbox and the append lanes are; the rest is a design.
- **One editor so far.** The design is for a desk; it has been used by one person.
- **Shared keys are not identity.** Until there are key pairs, a lane says that someone had the key, not who.
- **The anonymous lane is not anonymous against everything.** The server sees when an append arrived and from where; the record carries no identity, but traffic can.
- **The pass acting on its own is limited to what is cheap to undo.** A claim, an argument or a title stays a proposal.
- **Editor mode syncs as I read.** That is more data than the lane sends, and the reason it is scoped to newsroom pages and to the kinds of note I turn on.

If you run a desk and want to try an editor's channel with an agent, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo from me on 18 October 2026, after asking the agent to remove over-the-top phrases and add a check for them. The designs it builds on are this site's notes: [the activity vault](https://newsroom.sgit.ai/admin/notes/2026-10-12__the-activity-vault.md), [the feedback loop](https://newsroom.sgit.ai/admin/notes/2026-10-12__the-feedback-loop.md), [send to my vault from any browser](https://newsroom.sgit.ai/admin/notes/2026-10-13__send-to-my-vault-from-any-browser.md) and [the vault, opened](https://newsroom.sgit.ai/admin/notes/2026-10-16__the-vault-opened.md). The wording check is `admin/build/wording.py`. Related: [sixteen notes I did not want to lose](sixteen-notes-i-did-not-want-to-lose.md), [fix the page yourself](fix-the-page-yourself.md), [how cheap is it to undo](how-cheap-is-it-to-undo.md), [three policies for an agent](three-policies-for-an-agent.md), [agent workflows on ephemeral vaults](agent-workflows-on-ephemeral-vaults.md). Written up and checked by this site's agent; the editorial responsibility is mine.

## Threads

Vaults & methodAgents & policy[This article as a graph →](graphs.md#the-editors-channel)

### Builds on

- [Sixteen notes I did not want to lose: a request to send from any browser to my vault, why identity is still this hard, and how two more wires became a product line](sixteen-notes-i-did-not-want-to-lose.md) Sixteen notes stuck in a browser with no passkey led to a request: let any browser send to my vault, by link, text or QR code.
- [Fix the page yourself: the bookmarklet trick from my security days, a page API every site should publish, and why the next user experience is the one the user customises, with six fixes running on this newsroom](fix-the-page-yourself.md) A bookmarklet from my security days, a page API every site should publish, and six fixes running on this newsroom: the next UX is the user's own.
- [The human in the loop is a spectrum: how cheap it is to undo decides where a person belongs, and why the newsroom ships on its own while my email still waits for me](how-cheap-is-it-to-undo.md) How much to let an agent ship on its own depends on how cheap it is to undo and how mature the controls are, and both of those move.
- [Three policies for an agent: behaviour says what it may do, decision says who chooses, workflow says in what order](three-policies-for-an-agent.md) Behaviour says what an agent may do, decision who chooses at a branch point, workflow in what order. Zoom into one ABP cell and it becomes both.
- [Agent workflows on ephemeral vaults: seven architectures from one agent to a swarm, a repository of recipes that gates sgit's releases, and what a hundred writers did to an append lane](agent-workflows-on-ephemeral-vaults.md) Seven architectures for agents on ephemeral vaults, a recipe repository that gates sgit's releases, and a hundred writers measured on an append lane.

### Continued by

- [Messaging-FS: an encrypted messenger between vaults, built on append lanes and PKI, from the first crude inbox to messages in the browser and on the command line](messaging-fs.md) A proposed encrypted messenger between vaults: append lanes for transport, PKI for trust, and Messaging-FS as the schema.
- [The user keeps the meter: a proposed design for user management, activity and billing on vaults, with one billing vault per user, two signed writers, and one light check at the server](the-user-keeps-the-meter.md) A proposed design for billing on vaults: the user's browser keeps the meter, credit now and validated later, one light check at the server.
- [PKI everywhere: from now on every message, secret and handover starts with a signature, and how an agent gets its first key](pki-everywhere.md) From now on every message, secret and handover is signed. The hard part is an agent's first key: two patterns, one built and one proposed.
- [The briefs so far: sixty-five things this newsroom has asked of itself, what is built, and where each next session starts](the-briefs-so-far.md) Sixty-five briefs this newsroom has asked of itself, audited from the code: 11 built, 21 partly, 32 not, each open one with a session brief.
- [Search as navigation: walking the newsroom's graph with no model, and why a clean graph should beat vectors](search-as-navigation.md) Search as a walk through the newsroom's graph: chips, exact suggestions, five views and a pane that shows the working, with no model yet.
- [Reviews on the record: other models, the editor and the desk check every article, and never the same text twice](reviews-on-the-record.md) Published criteria, one record per article and text, five at a time, answered finding by finding: reviews by other models, the editor and the desk.
- [On the record: signed opinions from experts, paid when readers value them, and a share for the people whose ideas an article uses](on-the-record.md) Experts go on the record with signed opinions, readers pay for the ones they value, and the people whose ideas an article uses get a share.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 182 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=182)

**Posting this article on LinkedIn?** The cover is [the-editors-channel.jpg](banners/the-editors-channel.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-editors-channel.html)*
