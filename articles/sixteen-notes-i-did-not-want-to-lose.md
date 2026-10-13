# Sixteen notes I did not want to lose: a request to send from any browser to my vault, why identity is still this hard, and how two more wires became a product line, sgit.ai

> I opened the newsroom on my iPhone, in a browser that looked like Chrome but could not reach my passkeys, and the vault button told me there were sixteen changes that existed only in that browser. My reaction is the most interesting part: those were notes and reads I wanted to keep. They had become pieces of intelligence, and I was happy to do a couple of steps to get them into my vault, as long as I only had to do it once. That is the nudge working for the right reason. So this is a feature request and a brief. Every reader vault should have a lane that any browser can write to, by a link, a piece of text or a QR code carrying only where to write and the key to encrypt with, so that a browser with no passkey, no sign-in, or an old operating system can send what it holds into my vault, and the vault takes it from there the next time I open it. The newsroom already does exactly this to send a reading summary to sgit.ai, so it is a pattern pointed at myself. It is also a commentary. Identity is still a mess: passkeys that work in one browser and not in the one an app opens a link in, and an email connector that makes attachments, inline images and a clean reply in a thread far harder than the underlying service does. Users will accept a lot of friction, once, when the value is clear, which is how WhatsApp links a computer and how Midjourney grew on a Discord bot. What they will not accept is losing their data. And the other half of the day's news is the opposite story: two new wires, OWASP and AWS, built from two small config files on the same pipeline, and suddenly a new product line.

*Source: <https://newsroom.sgit.ai/articles/sixteen-notes-i-did-not-want-to-lose.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Sixteen notes I did not want to lose: a request to send from any browser to my vault, why identity is still this hard, and how two more wires became a product line

# Sixteen notes I did not want to lose: a request to send from any browser to my vault, why identity is still this hard, and how two more wires became a product line

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-13 · [article v1.0.0](versions/sixteen-notes-i-did-not-want-to-lose.md) · [newsroom v0.12.23](https://newsroom.sgit.ai/admin/versions.html) · vaultsappend-lanesqr-codespasskeysidentityusabilitygmailagentswireproductbriefarticle

***Abstract:** I opened the newsroom on my iPhone, in a browser that looked like Chrome but could not reach my passkeys, and the vault button told me there were sixteen changes that existed only in that browser. My reaction is the most interesting part: those were notes and reads I wanted to keep. They had become pieces of intelligence, and I was happy to do a couple of steps to get them into my vault, as long as I only had to do it once. That is the nudge working for the right reason. So this is a feature request and a brief. Every reader vault should have a lane that any browser can write to, by a link, a piece of text or a QR code carrying only where to write and the key to encrypt with, so that a browser with no passkey, no sign-in, or an old operating system can send what it holds into my vault, and the vault takes it from there the next time I open it. The newsroom already does exactly this to send a reading summary to sgit.ai, so it is a pattern pointed at myself. It is also a commentary. Identity is still a mess: passkeys that work in one browser and not in the one an app opens a link in, and an email connector that makes attachments, inline images and a clean reply in a thread far harder than the underlying service does. Users will accept a lot of friction, once, when the value is clear, which is how WhatsApp links a computer and how Midjourney grew on a Discord bot. What they will not accept is losing their data. And the other half of the day's news is the opposite story: two new wires, OWASP and AWS, built from two small config files on the same pipeline, and suddenly a new product line.*

Send to my vault, from any browser. The reader's vault offers a link three ways, a URL, text and a QR code, carrying only where to write and the public key to encrypt with. Any browser, with no passkey and no sign-in, encrypts what it holds and appends it to the lane; it can write and never read. The next time the vault is opened with the passkey, the pane drains the lane into the reader's records.

## In short

- **Sixteen changes, only in one browser.** On my iPhone, in a browser that could not reach my passkeys, the vault said sixteen changes existed nowhere else.
- **I wanted them, and that is the point.** They had become my intelligence, and I would do a couple of steps to keep them. The nudge works when it shows you what is yours.
- **The request: send from any browser to my vault.** A lane on every reader vault, offered as a URL, text or QR code, that any browser can write to and none can read.
- **The pattern already exists.** The newsroom encrypts a reading summary in the browser and appends it to sgit.ai's inbox with no vault and no passkey. Point it at the reader's own vault.
- **Solve my iPhone, solve every browser.** Not signed in, no passkey provider, an old iPad: a link opened anywhere, even sent to myself on WhatsApp, is enough.
- **Identity is still a mess, and that is why things do not get adopted.** Passkeys work in one browser and not in the one an app opens links in. Email through an agent connector makes simple things hard.
- **Users accept friction once, for value.** WhatsApp's QR code and Midjourney's Discord bot are proof. Losing data is the thing they do not forgive.
- **Two config files, a new product line.** The OWASP Wire and the AWS Wire run on the Industry Wire's pipeline, and each may find its own audience.

## What happened

I was on my iPhone, reading the newsroom in a browser that looked like Chrome, but not the Chrome I am signed in to. It felt like it was running with low permissions, never logged in to anything. The Vault button showed a count: sixteen changes only in this browser, reads, notes and stories seen, that my vault did not have. And that browser could not open my vault, because it could not reach my passkeys.

The likely reason is less mysterious than it felt. On iOS, a link opened inside another app, WhatsApp, Gmail, LinkedIn, often opens in that app's own web view rather than in the browser, and Apple's rule for those is strict: an app ["can't use passkeys to authenticate for services that you haven't configured as the app's associated domains"](https://developer.apple.com/documentation/authenticationservices/supporting-passkeys). The real browsers get an entitlement that lets them use passkeys for any site, and Chrome on iOS 17 or later [can use passkeys from Google Password Manager](https://developer.chrome.com/blog/passkeys-gpm-ios). So the same phone has a browser that can open my vault and a browser-shaped view that cannot, and nothing on the screen tells you which one you are in.

## The nudge is working, for the right reason

What interested me most was my own reaction. I did not think, oh well. I thought: I want those. They were not page views any more. They were things I had read, notes I had made, stories I had marked, pieces of intelligence that were mine and that I did not want to lose. And I wanted to get back to my account, because that is where my newsroom is, the one customised to what I read.

In [The site is an inbox](the-site-is-an-inbox.md) I said none of this should be gamified: no decision placed at the end of a page to make you scroll there. The count on the vault button is not that. It does not invent a reason to click. It tells you what is yours and where it is at risk, and the reason to act is real. That is a nudge for the right reason, and it is working, on me. It is the same loop as [I miss it, so it is working](i-miss-it.md): the moment you have something to lose, the feature you need announces itself.

## The request: send from any browser to my vault

So how do I get those sixteen changes from that browser into my vault? Today there is one way without the passkey, the recovery code, which opens a second door to the master. That is too much power to type into a browser I do not trust, for a job that only needs to add things.

What it needs is a lane. My vault, when it is created, should also have a communication lane, an [append lane](connector-twin-before-you-deploy-an-agent.md) that an outside writer can add to and never read. To write to it, a browser needs only two things: where the lane is, and the public key to encrypt with, or a place to fetch it. That fits in a link. So the vault pane should offer it three ways: a URL I can open, the text I can copy and paste, and a QR code I can scan from the other device. Whichever browser opens it encrypts what it holds to my key and appends it to the lane. It learns nothing about my vault and can read nothing back. The next time I open my vault with my passkey, on any device, the pane drains the lane and the sixteen changes are mine.

The newsroom already does this, pointed somewhere else. When a reader sends their reading to sgit.ai, the meter encrypts a summary in the browser to sgit.ai's published key and posts it to an append lane, with no vault and no passkey. The request is the same pattern pointed at the reader's own vault.

And this is a good example of the non-linear path I keep writing about, in [Not a straight line](not-a-straight-line.md). Once it exists, it solves far more than my iPhone. It works in any browser: one not signed in to anything, one with no passkey provider, an old iPad where the passkey never worked and only a QR code would. I could even send the link to myself on WhatsApp and open it on the other side. The friction of identity stops deciding whether your data is safe.

## The brief

The brief in six steps, with what already exists beside each: the append lanes, the browser-side encryption the meter already uses, the drain the reply lane needs anyway, and the tests. Only the reader's key pair and the pane's link are new.

*For the session that builds the reader's vault pane on newsroom.sgit.ai. Written by @newsroom.writer for Dinis Cruz, 13 October 2026, on top of the vault pane at v0.12.22.*

1. **A key pair for the reader.** Generated in the browser when the vault is created or first opened at this version, the private key kept in the master vault, the public key in the clear. Today the reader has none; the persona key pairs in [The site is an inbox](the-site-is-an-inbox.md) were the plan for this.
2. **An append lane on the reader vault**, configured with the master's credentials, with its token kept in the master.
3. **The link, three ways.** A URL, the same as text, and a QR code, carrying the lane address, the append token and the public key or where to fetch it. Nothing else: not the vault key, not the read key.
4. **The sender's side.** On any page, a browser holding a link encrypts its pending records, the same ones the count already lists, and appends them as one message per send, then marks them sent and keeps a copy until they are confirmed.
5. **The drain.** On every unlock, the pane lists what is waiting in the lane, says which browser sent it and when, and merges it into the reader's records on one press, keeping the sender's device as the author, as records brought in from another device already are.
6. **Tests.** A browser with no authenticator sends; the vault, opened with a virtual passkey, drains; a tampered or foreign message is refused; the QR round-trips.

What to be careful about: anyone holding the link can write to the lane, so the token should be rotatable from the pane, the drain should show what arrived before it merges, and a link should be able to expire. None of them can read anything. The same machinery is what card 015, a reply lane from the newsroom to the reader, needs anyway.

## This stuff is hard in the real world

And this is the commentary I most wanted to make. Things like this are why good ideas do not get mainstream adoption. Identity is a mess. It works in some browsers and not others, on some paths and not others, and the user is not told which. From a user's point of view this should be straightforward. It just has to work, inside the workflow and the experience they are already in. It cannot be "it only works on this browser, in this situation, with this setting", and then, oh, you have lost some data.

But here is the other side of it, and I think it is just as important. Users have a lot of tolerance for complex workflows when they can see the value, when the steps are not repeated, and when they are connected to the value. Connecting a computer to WhatsApp is a good example: you open the app on your phone, go to linked devices, scan a QR code on the other screen, and then it is done. Nobody calls that great design, and everybody does it, because it happens once and what you get is immediate.

Midjourney is the extreme case. When it started, it had one of the strangest workflows I had seen: you joined a Discord server and typed a slash command, ["/imagine"](https://discord.com/build-case-studies/midjourney), into a channel full of other people's images. I remember thinking, how does this even work? And people loved it. Discord says the server hit "the prior server cap of an astonishing one million users". The value was obvious and the friction was the price of it.

I am not saying bad experience is fine. I am saying that a one-off step, connected to value, is acceptable, and that this is something to test, not assume. We can A/B test the link against a pairing flow and see which readers finish.

## And then there is email

Another example of things being harder than they should be: sending an email through an agent, with Claude connected to Gmail. For basic emails it works well. Then it gets painful. An attachment is possible, but not the way you would expect: as [Six agents, one inbox](six-agents-one-inbox.md) found, the connector's draft call takes the file inline, and the agent had to shrink a 1.4 MB scanned PDF to 17 KB to get a signed letter out. Replying in the same thread while cutting the wall of quoted text underneath, which [The wall under the reply](the-wall-under-the-reply.md) argued for, I have not been able to do. Inline images, which make a message far more powerful, I cannot send at all.

None of these are limits of Gmail itself. Google's API lets a program ["upload file data when creating or updating a draft"](https://developers.google.com/workspace/gmail/api/guides/uploads), put a draft into an existing thread by its ID, and replace a draft whole, quoted text included. Claude's own help page lists drafting, sending, replying and forwarding, and says attachment content is "metadata only" for reading. So the constraint is the connector's, and I can only guess why. If it is security, I do not think it buys much: an agent that wants to leak data can share a folder on Drive, or send fifty small emails, or a thousand. What it does do is push people to other tools to send the emails they actually need to send, and then the mailbox is no longer managed in one place, which is a bigger risk than the attachment ever was. These look like small things. In real use they are the difference between a workflow and a workaround.

## Two config files, a new product line

One pipeline, three wires. A wire is a vault plus a config: the Industry Wire came first, and the OWASP Wire and the AWS Wire were added on 13 October with two 17-line configs, the same builder and the same reader, each with its own audience to find.

The day's other story is the opposite of all that friction. The wire started simple: one agent writing industry news into an encrypted vault, [and this site drawing it](two-agents-one-vault.md) with only the read key. Today the agent that runs it added two more: an [OWASP Wire](https://newsroom.sgit.ai/wire/owasp/), everything happening at and about OWASP, joined to a graph of its projects, and an [AWS Wire](https://newsroom.sgit.ai/wire/aws/), everything AWS announced, filtered by a declared stack. On this site that was barely a feature: two configuration files of seventeen lines each, and one builder that now serves every wire. In the release's own words, "a wire is a vault plus a config".

And suddenly the use cases and the value exploded. A newswire for cyber security risk is one product. A wire for one community, or for the customers of one platform, is another, and each can be followed up to see whether there is an audience that cares about exactly that. If we can add value there, that is a very good value proposition, from almost no new code. It is the same lesson as the lane: build the general thing once, and the next use is nearly free.

## What this does not claim

- **The iPhone browser is my best explanation, not a diagnosis.** An in-app web view fits what I saw; it could also have been another browser mode.
- **The lane is a request, not a feature.** Nothing in this brief is built; the append lanes, the browser-side encryption and the recovery code are.
- **The email limits are what I and my agents have met.** The connector may handle more than its help page says; the attachment route works, at a size.
- **"Users accept friction once" is a hypothesis to test.** WhatsApp and Midjourney are examples, not evidence that readers of a newsroom will.
- **The wires are new.** Whether OWASP or AWS readers want a wire is exactly what has not been tested yet.

If you have hit the same walls with passkeys, browsers or agent email, or you want a wire for your own community, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 13 October 2026, written by this site's agent in the voice of this site. The argument and the editorial responsibility are mine. The vault pane, the pending count, the meter's reading share and the wires are from the newsroom's code and release notes up to v0.12.22. Apple, [Supporting passkeys](https://developer.apple.com/documentation/authenticationservices/supporting-passkeys); Google, [passkeys in Google Password Manager on iOS](https://developer.chrome.com/blog/passkeys-gpm-ios), 16 January 2025; the Gmail API guides on [uploads](https://developers.google.com/workspace/gmail/api/guides/uploads) and [threads](https://developers.google.com/workspace/gmail/api/guides/threads); Anthropic, [Google Workspace connectors](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors); Discord's [Midjourney case study](https://discord.com/build-case-studies/midjourney).

## Threads

Vaults & methodSite & engineering[This article as a graph →](graphs.md#sixteen-notes-i-did-not-want-to-lose)

### Builds on

- [The site is an inbox: deciding before reading, marks that build the reader's own graph, and why I could not write this brief until the vault existed](the-site-is-an-inbox.md) The site as an inbox that starts empty: decide fast before reading, mark slowly while reading, build a graph you own, and sign what you send to the newsroom.
- [I miss it, so it is working: the people who decide the roadmap have to use the product, and the vault the newsroom now needs](i-miss-it.md) I read the newsroom on four devices and they do not agree. Missing a feature is the best sign; the makers must use it. And the brief for the reader's vault.
- [Before you give an agent a connector, give the connector a twin](connector-twin-before-you-deploy-an-agent.md) An agent with a Gmail or Calendar connector can do things the platform cannot undo; a journal of every call, replayed, shows what it did and what can go back.
- [Not a straight line: working for RiskMandate by working on the newsroom, and why the thinking is never wasted](not-a-straight-line.md) Working on the newsroom solved RiskMandate's oldest problem in two days: progress is not a straight line, and the thinking is never wasted.
- [Six agents, one inbox: what a real multi-agent setup taught me about access policies](six-agents-one-inbox.md) An access policy for an agent is only as real as its worst row: every rule in a real six-agent setup, graded by how it is enforced today.
- [The wall under the reply: end an email with the state of the thread, not the thread](the-wall-under-the-reply.md) End an email reply with the state of the thread for this reader, not the quoted wall: decided, open, next, who is on copy, with links to the record.
- [Two agents, one vault: the Industry Wire is written into an encrypted vault by one agent and drawn by newsroom.sgit.ai, which holds only the read key](two-agents-one-vault.md) One agent writes the Industry Wire into an encrypted vault; newsroom.sgit.ai holds only the read key and draws it, so a commit reaches the page with no release.

### Continued by

- [Every link points back: 566 links between 105 articles, 15 that point forward, and why an article should know what came next and what corrected it](every-link-points-back.md) 551 of 566 links between articles point back in time. Why older articles should say what came next and what corrected them.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 105 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=105)

**Posting this article on LinkedIn?** The cover is [sixteen-notes-i-did-not-want-to-lose.jpg](banners/sixteen-notes-i-did-not-want-to-lose.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/sixteen-notes-i-did-not-want-to-lose.html)*
