# Issue 6: The reader's own newsroom: a passkey that opens a vault, a vault that crosses browsers, and what a reader does once their reading is theirs, SGit Newsroom

> What would a newsroom look like if your reading was yours, kept in a vault only you can open, on every device and in every browser, with nothing to sign up for? Between 11 and 13 October that went from a design to something that runs on newsroom.sgit.ai, and then did more than it was built for. Eight articles. The design, where a passkey computes a door and the door opens a master vault, and the test that made the door a door per path; the night the vault went live, with three real vaults behind a button on every page; the two things found by using it, that a second Chrome profile is just a second device, and that sixteen changes stranded in one browser are worth a lane any browser can write to; and what a reader does once the reading is theirs: an inbox that starts empty, ways into one article that keep the finished piece at the centre, a reading list sent in a link, and five themes kept in the browser.

*Source: <https://newsroom.sgit.ai/articles/newsletter/2026/10/13/006-the-readers-own-newsroom.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../../../index.md) / [SGit Newsroom](../../../../index.md) / [Newsletter](../../../index.md) / Issue 6

SGit Newsroom · Issue 6 · 2026-10-13

# The reader's own newsroom: a passkey that opens a vault, a vault that crosses browsers, and what a reader does once their reading is theirs

By [Dinis Cruz](https://sgit.ai/about/index.md), written with the [Journalist](../../../../../newsroom/roles/journalist.md)

***Abstract:** What would a newsroom look like if your reading was yours, kept in a vault only you can open, on every device and in every browser, with nothing to sign up for? Between 11 and 13 October that went from a design to something that runs on newsroom.sgit.ai, and then did more than it was built for. Eight articles. The design, where a passkey computes a door and the door opens a master vault, and the test that made the door a door per path; the night the vault went live, with three real vaults behind a button on every page; the two things found by using it, that a second Chrome profile is just a second device, and that sixteen changes stranded in one browser are worth a lane any browser can write to; and what a reader does once the reading is theirs: an inbox that starts empty, ways into one article that keep the finished piece at the centre, a reading list sent in a link, and five themes kept in the browser.*

What would a newsroom look like if your reading was yours? Not an account on somebody's server, but a vault only you can open, on every device and in every browser, with nothing to sign up for. Between 11 and 13 October that went from a design to something that runs on newsroom.sgit.ai, and then turned out to do more than it was built for. This is issue 6, the first written since the newsroom became its own publisher, and it picks up where [issue 5, no server by design](https://newsroom.sgit.ai/articles/newsletter/2026/10/11/005-no-server-by-design.html), left off: everything runs in the reader's browser, and now the reader has somewhere to keep it.

The reader's own newsroom in six pictures, one from each of six of the articles

## A passkey, a door and a master

[The passkey opens the vault](https://newsroom.sgit.ai/articles/the-passkey-opens-the-vault.html) is the design, in its third version and the first with a test behind it. A passkey, through the WebAuthn PRF extension, gives the browser 32 bytes that only your authenticator can produce for this site. From those bytes the browser computes the address and the key of a small door vault; the door holds the key of a master vault; the master holds everything else. A review on 11 October took the door out as a layer too many. The lab put it back: the same passkey, answering a QR code, gave different bytes from the same passkey on the device, so the unit of the design became the path, with a door for each. The key pairs that stand for the person are generated at random and never derived from the passkey, because:

>

The passkey is a lock, not an identity.

The key chain after the test: a passkey's bytes, by one path, compute a door; the door holds the master vault's key; the master holds the keys of everything else and the list of its doors.

## Live by two in the morning

[The vault is live](https://newsroom.sgit.ai/articles/the-vault-is-live.html) is the night after. By 02:22 UTC on 12 October a Vault button sat beside the balance on every page, opening a pane that makes three real sgit vaults from a passkey and an access key pasted once, writes each device's reading as one file in one commit, and brings every device's activity into the browser you are holding, so the meter shows one balance. The sync has no conflicts by construction: the vault holds records, never totals, and each device writes only its own file. It was checked by hand on an iPad against the real server. The article ends on why that mattered more than the feature, which is that the next brief could not have been written before it:

>

The constraints limit the scope of what I write, and that is what lets me write it.

## Found by using it

Two articles from 13 October are about what the vault did next, which nobody planned. [The vault crosses Chrome profiles](https://newsroom.sgit.ai/articles/the-vault-crosses-chrome-profiles.html) starts from separate Google accounts kept in separate Chrome profiles, where moving anything between them has always been awkward: copy, paste, or email it to yourself. The vault fixed that without a line of new code, because nothing in it knows what a profile is:

>

To the vault a second Chrome profile is a second device.

Each profile still needs a way in, and where the passkey lives decides it: an iCloud Keychain passkey on a Mac answers both profiles alike, while a Google Password Manager passkey follows its own account, so the other profile adds a door once. The article's hypothesis, untested, is that profiles are the more common case: people switch between them far more often than between computers.

[Sixteen notes I did not want to lose](https://newsroom.sgit.ai/articles/sixteen-notes-i-did-not-want-to-lose.html) is the other side of it. On an iPhone, in a browser-shaped view that could not reach the passkeys, the Vault button said sixteen changes existed only there. The interesting part was the reaction: those notes and reads had become worth keeping. So the article is a brief, not yet built, for a lane on every reader vault that any browser can write to and none can read, offered as a link, as text and as a QR code: the pattern the newsroom already uses to send a reading summary to sgit.ai, pointed at the reader's own vault. It is also about identity: people accept a step once, for value, as WhatsApp's QR code showed, but not this:

>

Losing data is the thing they do not forgive.

Send to my vault from any browser: a link carrying only where to write and the key to encrypt with; any browser can append to the lane and none can read it, and the vault drains it on the next unlock.

## What a reader does with it

[The site is an inbox](https://newsroom.sgit.ai/articles/the-site-is-an-inbox.html) starts from one image: for each reader the site is an inbox that starts empty, and every piece that arrives, an article or a wire story, waits for a decision. The inbox mode decides fast, with nothing loaded: read now, read later, not for me, more like this. The reading mode is slow, and it is where marks of six kinds build a graph the reader owns, joined to the graphs this site publishes beside every article. Part of that brief already runs: marks as you read arrived the same day, and the wire became an inbox the day after. One rule holds for both modes, that no decision is placed at the end of a page to make you scroll there:

>

A signal the site engineered is not a signal.

[Ways to read one article](https://newsroom.sgit.ai/articles/ways-to-read-one-article.html) makes the same move for a single piece. The five readers' views of an article worked, and arrived as one fold under the abstract. Now the reader picks the way in, in the pane about the piece: headlines, the infographic, two minutes, the slides, what is new against what they have read, the facts, the relationships, the vocabulary, or the whole article. Most of those are computed from views that already exist; a model in the reader's own browser is for the rest. And one thing is kept whole on purpose, the finished article, because it has a beginning, a pacing and a voice:

>

The modes are ways in, not replacements.

The modes, what each is and what makes it; the finished article at the centre, with what it keeps that no view has.

## From one reader to another, in your own colours

[From me to you, in a link](https://newsroom.sgit.ai/articles/a-reading-list-in-a-link.html) is a reading list from one person to another, carried in the part of the address that browsers do not send to the server: from Dinis, for Steve, here is what to read, what to look at and what to follow. It needed a stable number for every article, which every article page here now carries, with a link to start a list from it. Its real subject is the loop: a small feature that crosses editorial, product, engineering, sales and the founder, with each hand-off a written brief.

>

Here, the loop is a day.

The newest was asked for in two words. The first reaction to the Industry Wire from outside was "Dark mode!" on WhatsApp, and [Dark mode, and four more](https://newsroom.sgit.ai/articles/dark-mode-and-four-more.html) is how five themes shipped in v0.12.12, written by the agent that built them. Newsprint stays the default, pixel for pixel; Night, Paper, Blueprint and Ember sit behind one pill in the bar. The choice is kept in your browser and not carried by the vault, on the view that

>

A theme is a property of the screen

## The eight articles

### The vault

The design, and the night it went live.

- [**The passkey opens the vault: a door per path, a master vault for every user, and no server of ours**](../../../../the-passkey-opens-the-vault.md). Tested: a passkey's PRF bytes compute a door that holds the master's key, and a different path to the same passkey gives different bytes, so a door per path.
- [**The vault is live: from a design on 11 October to a reader's vault on newsroom.sgit.ai by two in the morning, and how all of it fits together**](../../../../the-vault-is-live.md). The reader's vault runs on newsroom.sgit.ai: a passkey opens three real vaults, each device writes one file, and the architecture is drawn as it stands.

### Found by using it

A second Chrome profile as a second device, and a lane from any browser to your vault.

- [**The vault crosses Chrome profiles: state and memory between browser sessions, found by using it rather than by building it**](../../../../the-vault-crosses-chrome-profiles.md). The reader's vault carries the newsroom between Chrome profiles as it does between devices, a way to share state across browser sessions nobody built.
- [**Sixteen notes I did not want to lose: a request to send from any browser to my vault, why identity is still this hard, and how two more wires became a product line**](../../../../sixteen-notes-i-did-not-want-to-lose.md). Sixteen notes stuck in a browser with no passkey led to a request: let any browser send to my vault, by link, text or QR code.

### What a reader does with it

The inbox that starts empty, and the ways into one article.

- [**The site is an inbox: deciding before reading, marks that build the reader's own graph, and why I could not write this brief until the vault existed**](../../../../the-site-is-an-inbox.md). The site as an inbox that starts empty: decide fast before reading, mark slowly while reading, build a graph you own, and sign what you send to the newsroom.
- [**Ways to read one article: the finished piece stays at the centre, and the reader picks the way in**](../../../../ways-to-read-one-article.md). The five readers' views arrived as folds inside the long piece; now the reader picks the way in, with a default, and the finished article stays at the centre.

### From one reader to another, in your own colours

A reading list in a link, and five themes kept in the browser.

- [**From me to you, in a link: a personal reading list, two briefs to build and use it, and the loop that makes it a day's work**](../../../../a-reading-list-in-a-link.md). A reading list from one person to another, in a link the server never sees; a brief to build it, a brief to use it, and the loop that ships it in a day.
- [**Dark mode, and four more: five themes for the newsroom, chosen once and kept in your browser**](../../../../dark-mode-and-four-more.md). Five themes behind one pill in the bar, kept in the reader's browser, built as a layer over a stylesheet this site cannot edit, with colour as a token and a test.

*This is issue 6 of the SGit Newsroom newsletter, also published on LinkedIn in [Deterministic GenAI](https://www.linkedin.com/newsletters/deterministic-genai-7174563523795005440/). Every article it links to is on [newsroom.sgit.ai](https://newsroom.sgit.ai/articles/index.html), with its sources and its data. To get the next issue by email, [subscribe at newsroom.sgit.ai/subscribe](https://newsroom.sgit.ai/subscribe/).*

**Posting this issue on LinkedIn?** The cover is [006-the-readers-own-newsroom.jpg](../../../../banners/006-the-readers-own-newsroom.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page. Its images copy with it.

[← All issues](../../../index.md)


---

*[Site index for agents](../../../../../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/newsletter/2026/10/13/006-the-readers-own-newsroom.html)*
