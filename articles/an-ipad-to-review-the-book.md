# An iPad to review the book: a brief for an app that reads the PDFs, shows the comments on the page, opens its vault with my passkey and carries sgit in Swift, sgit.ai

> I review on the iPad because it is like a book: no notifications, nothing else on the screen. But reviewing the book of The Ultimate Insider there showed me what is missing. Preview has no full screen I could find and no way to work across several files, and the review lives in two PDFs, the book and its companion of cards, with my comments going back by hand. So this is a brief for an iPad app built to review the book, and later to read it. It reads the PDFs properly. It shows the comments, the cards and the votes on the page they are about, because once we control the medium the review does not have to be a second PDF. It sends and receives feedback through append lanes, and everything it exchanges is JSON tied to the book's semantic graph. Its library is an sgit vault on the iPad, encrypted at rest and opened with my passkey, using an extension Apple has offered apps since iOS 18. And sgit inside it is written in Swift, which would make it the third implementation of the format, after the command line and the browser. It meters what it is used for, the way the newsroom's reader account does, with a balance that can go negative, because the reader pays for the use and is not the product. The good news is that I have done part of this before. In March, a team of agents and I built a desktop app for the SGraph sites in two days, signed and notarised with my Apple developer account, ran it on an Android emulator, and set up an iOS build pipeline. This article reads that repository, says what carries over and what does not, and why I now think the iPad app should be native.

*Source: <https://newsroom.sgit.ai/articles/an-ipad-to-review-the-book.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / An iPad to review the book: a brief for an app that reads the PDFs, shows the comments on the page, opens its vault with my passkey and carries sgit in Swift

# An iPad to review the book: a brief for an app that reads the PDFs, shows the comments on the page, opens its vault with my passkey and carries sgit in Swift

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-31 · [article v1.0.0](versions/an-ipad-to-review-the-book.md) · [newsroom v999.0.0](https://newsroom.sgit.ai/admin/versions.html) · ipadappsbookreviewsgitpasskeysbriefspublishingarticle

***Abstract:** I review on the iPad because it is like a book: no notifications, nothing else on the screen. But reviewing the book of The Ultimate Insider there showed me what is missing. Preview has no full screen I could find and no way to work across several files, and the review lives in two PDFs, the book and its companion of cards, with my comments going back by hand. So this is a brief for an iPad app built to review the book, and later to read it. It reads the PDFs properly. It shows the comments, the cards and the votes on the page they are about, because once we control the medium the review does not have to be a second PDF. It sends and receives feedback through append lanes, and everything it exchanges is JSON tied to the book's semantic graph. Its library is an sgit vault on the iPad, encrypted at rest and opened with my passkey, using an extension Apple has offered apps since iOS 18. And sgit inside it is written in Swift, which would make it the third implementation of the format, after the command line and the browser. It meters what it is used for, the way the newsroom's reader account does, with a balance that can go negative, because the reader pays for the use and is not the product. The good news is that I have done part of this before. In March, a team of agents and I built a desktop app for the SGraph sites in two days, signed and notarised with my Apple developer account, ran it on an Android emulator, and set up an iOS build pipeline. This article reads that repository, says what carries over and what does not, and why I now think the iPad app should be native.*

A sketch of the brief: the library, the page with its comments, and the append lane beside it. Nothing is built yet.

## In short

- **I review on the iPad because it is like a book.** Nothing else is on the screen.
- **Preview gets in the way.** No full screen I could find, and no way to work across the book's several files.
- **So this is a brief for an iPad app to review the book,** and later to read it. iPad first; no Android for now.
- **The comments appear on the page they are about,** with the companion's cards, votes and highlights, sent and received through append lanes.
- **Everything it exchanges is JSON,** tied to the book's semantic graph.
- **Its library is an sgit vault, opened with my passkey,** and sgit inside it is written in Swift: a third implementation of the format.
- **It meters its use,** with a balance that can go negative. The reader pays for the use, and is not the product.
- **I have built part of this before.** A desktop app from March, signed with my Apple developer account, with an iOS pipeline.

## Why an iPad

I do a lot of my reading and reviewing on the iPad. My laptop has too much going on: messages, terminals, a dozen things moving. The iPad has none of that. It is like a book, and that is the point.

This week I reviewed RC1 of the book of [The Ultimate Insider](the-book-of-the-talk-and-its-companion.md) on it, with its companion, the PDF of 98 cards each pinned to a sentence and a page, with boxes to tick. It worked, and it showed me the gaps. Preview has visibility problems: I could not find its full screen mode, and it has no good way to see several files together, which is what a review is. And the review is in two documents, the book and the companion, joined only by page numbers and by me.

## The book app as a review desk

So the app is designed for one job first: helping me, and the other reviewers, review the book.

- **A library, not a file.** The book, the companion, the cold read, the briefs and the graph, side by side, with what is new since I last looked.
- **A proper PDF reader.** Full screen, two pages or one, quick jumps, search, and the page I was on when I come back.
- **The comments on the page.** We made two PDFs, one to read and one to comment on, because a PDF cannot carry the conversation. In our own app it can: a reviewer's comment, a card from the companion and my tick appear on the sentence they are about.
- **Highlight and vote.** Mark a passage, agree with a comment, and it goes into the review.
- **Append lanes,** to send and receive. My highlights, votes and comments go out as signed entries; reviewers' comments and the book agents' replies come in. An append lane only grows, so the review is a record, like the [hundred writers on one lane](agent-workflows-on-ephemeral-vaults.md) we tested.
- **Pull and push from the site.** The app loads a new release of the book and its cards from the site, and pushes the review back.

Everything it exchanges is JSON: the briefs, the cards, the comments, the votes, each pointing at the node of the book's semantic graph it concerns, not only at a page number. That is what lets a comment survive the next release, when the page numbers move.

## The page as a projection

This is where it becomes more than a review tool. If the app draws the comments on the page, then the page is only one way to show the book's content. The PDF is one projection, the website another, the app a third, and the comments, the sources and the graph can appear in any of them. That is the idea of [a book for one reader](a-book-for-one-reader.md), and the start of a better digital way to read the book, not only to review it.

## A vault that opens with my passkey

The vault opens with the passkey: Face ID, the PRF secret, a key derived on the device, and the vault key unwrapped.

The feature I think matters most is that the library is an sgit vault, on the iPad, and that it opens with my passkey.

A passkey normally only proves who I am. With an extension called PRF it can also return a secret, always the same one for the same passkey and the same input, and that secret can become a key. Apple added PRF to its passkey APIs for apps in iOS 18: the [assertion input](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfassertioninput-swift.struct) asks a passkey for it, and the [registration input](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfregistrationinput-swift.struct) checks whether a new passkey supports it. So the design is:

1. **Face ID** unlocks my passkey, kept in iCloud Keychain.
2. **The passkey returns its PRF secret,** for a salt the vault keeps.
3. **A key is derived from it on the device,** and never stored.
4. **That key unwraps the vault key,** and the vault decrypts.

The files are encrypted at rest, and nothing opens them without my face and my passkey. [A browser for one](a-browser-for-one.md), my brief for an iPhone app, had one unknown: whether PRF works inside an app's web view. A native app does not need the web view for this; it asks the passkey directly. It still has to be tested on day one, on my iPad, before anything else is built. And it needs a second way in: a recovery key, printed as a QR code like [a secret is a QR code](a-secret-is-a-qr-code.md) describes, so that losing a passkey is not losing the vault.

## sgit in Swift

[sgit is a standard, not a server](sgit-is-a-standard.md): a documented format that today has two implementations, the command line and the browser vault app, each verifying what the other writes. The iPad app is the chance for a third, written natively in Swift, Apple's own language, which reads a vault from the site, keeps it on the device and writes back what the review adds.

That is worth doing for its own sake. A format with three implementations, in three languages, written by different teams, is far more of a standard than one with two. Every place where the Swift version and the others disagree is a gap in the documentation, and finding those gaps is the work.

## The meter

The app should also carry the newsroom's reader meter. Every page read, every graph opened, every navigation costs a little, against credits the reader buys, and the balance can go negative, as [paying after the value](paying-after-the-value.md) argues and [the user keeps the meter](the-user-keeps-the-meter.md) designs. It is easy, and it is fair: the reader pays for what they used.

All of this rests on one idea, and I want it said plainly. The reader is the customer, not the product. We do not sell the user, or the user's attention, or what we learn about them. We charge for the use of the product, the reader pays for the value they get, and the meter, like the vault, is theirs.

## What I built in March

I have done part of this before. In March, a team of agents and I built [SGraph Desktop](https://github.com/the-cyber-boardroom/SGraph-AI__Desktop), an app that wraps the SGraph websites, Send, Vault, Workspace and Tools, in native web views. I read its repository today. It records:

- **A macOS app in a day.** Built with Tauri, signed with my Apple developer account and notarised in its CI pipeline; first launched on a MacBook Air on 8 March 2026.
- **Android in two days.** On 9 March it launched on an Android emulator, from its own pipeline, with tabs at the bottom; Vault and Tools loaded, and Send refused to be framed in a web view.
- **An iOS pipeline.** A build on GitHub's macOS runners, an iOS shell with a tab bar, and a minimum of iOS 16. The repository records no launch on an iPhone or iPad.
- **A team.** An architect, a designer, a developer, DevOps, a historian and a librarian, with briefs, reviews and a record of what exists, the same way our teams work now.

Its last commit is from 9 March. What carries over is the Apple developer account, the signing and notarisation in CI, the macOS build pipeline and the team's structure. What does not is the architecture: it wraps websites, and its own architect's review found that several web views at once, its main pattern, is experimental on mobile.

## Native, this time

So I think the iPad app should be native: Swift, with Apple's own frameworks.

- **The PDF is the centre,** and Apple's PDFKit is the iPad's own PDF reader, with selection, search and annotations.
- **The passkey is native** too, through AuthenticationServices, as above.
- **sgit in Swift** is part of the point, not a cost.
- **The web is still there** for what is already web: the newsroom and the site's pages, in a web view, as the iPhone brief described.

Tauri's way, a web app inside a native shell, made sense for a launcher of websites. For a reading and review app built around PDFs, a vault and a passkey, the native parts would be most of the app.

## The plan

1. **Phase 0, test first.** On my iPad: a passkey with PRF, returning the same secret twice; a vault key wrapped and unwrapped with it; a recovery key.
2. **Phase 1, the reader.** The library from a vault, the PDF reader, full screen, several files.
3. **Phase 2, the review.** Comments, cards and votes on the page; append lanes in and out; JSON tied to the graph.
4. **Phase 3, sgit in Swift.** Clone, read and write a vault natively, checked against the command line.
5. **Phase 4, the meter.** The reader account and credits, as on the site.

The builds run on GitHub's macOS runners, as in March, and go to the iPad through TestFlight, so no session needs the device itself.

## What this does not claim

- **Nothing is built.** This is a brief, and the figure is a sketch.
- **PRF has not been tested on my iPad.** The API is in Apple's documentation from iOS 18; Phase 0 is there to check it.
- **No Swift implementation of sgit exists.** The format has two implementations today.
- **The March app's iOS build is not recorded as having run** on a device; the pipeline and the shell are in the repository.
- **My interest:** I build sgit, the newsroom and the book.

## Where this comes from

- My voice memo of 31 October 2026, word for word in `admin/notes/2026-10-31__ipad-app/memo-01.md` in this site's repository.
- [the-cyber-boardroom/SGraph-AI__Desktop](https://github.com/the-cyber-boardroom/SGraph-AI__Desktop), read on 31 October 2026 at its last commit of 9 March 2026: the README, `src-tauri/tauri.ios.conf.json`, `.github/workflows/ci-pipeline__ios.yml`, the brief of 8 March on the mobile path, the architect's review of it, and the historian's records of the first macOS and Android launches.
- Apple, AuthenticationServices: the [PRF assertion input](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfassertioninput-swift.struct) and the [PRF registration input](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfregistrationinput-swift.struct), read on 31 October 2026.
- Related: [a browser for one](a-browser-for-one.md), [the book of the talk and its companion](the-book-of-the-talk-and-its-companion.md), [sgit is a standard](sgit-is-a-standard.md), [the user keeps the meter](the-user-keeps-the-meter.md).

## Threads

Vaults & methodSite & engineering[This article as a graph →](graphs.md#an-ipad-to-review-the-book)

### Builds on

- [The book of the talk by morning: RC1 of The Ultimate Insider, written from the record, read cold by a second team, with a companion PDF that turns reviews into tick boxes](the-book-of-the-talk-and-its-companion.md) Two agent teams, one night: RC1 of the book of The Ultimate Insider, a cold read by a team that knew only the record, and a companion PDF of tick boxes.
- [Agent workflows on ephemeral vaults: seven architectures from one agent to a swarm, a repository of recipes that gates sgit's releases, and what a hundred writers did to an append lane](agent-workflows-on-ephemeral-vaults.md) Seven architectures for agents on ephemeral vaults, a recipe repository that gates sgit's releases, and a hundred writers measured on an append lane.
- [A book for one reader: a personalised edition of Generation Z Developers, assembled by an agent for one person, and paid for as it is read](a-book-for-one-reader.md) A personalised edition of Generation Z Developers, assembled by an agent for one person from a private brief, and paid for as it is read.
- [A browser for one: an iPhone app that only reads my newsroom, why I am building it now, and why I will still pay someone to keep it working](a-browser-for-one.md) An iPhone app that only reads my newsroom: WebKit in the UK, a paid membership and a Mac to build it, one passkey test first, and someone else to maintain it.
- [A secret is a QR code and a link to a public key: the workflow the QR experiment opens, who else already does this, and a format to share](a-secret-is-a-qr-code.md) Send a QR code and a link to a public key: the workflow the QR experiment opens, who already does this, and a format to share.
- [sgit is a standard, not a server: everything in a vault is one hash away, any storage can serve it, and the server is the least interesting part](sgit-is-a-standard.md) Git won as a standard, not a server. sgit is one too: every name computed from the key, a file four GETs away, any storage can serve it.
- [Paying after the value: why a balance that can go negative feels different from a subscription, the psychology behind it, and the experiment this newsroom is running](paying-after-the-value.md) Most purchases are bets on future value; a reading balance that can go negative asks for payment when the value is already in view.
- [The user keeps the meter: a proposed design for user management, activity and billing on vaults, with one billing vault per user, two signed writers, and one light check at the server](the-user-keeps-the-meter.md) A proposed design for billing on vaults: the user's browser keeps the meter, credit now and validated later, one light check at the server.

### Continued by

- [The augmented book: one source in layers, projected to the web, the iPad and print, so the reader gets the right information at the right time, and what fifty years of attempts teach](the-augmented-book.md) The augmented book: one source in layers, projected to web, iPad and print, with the right information at the right time, and what precedents teach.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 335 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=335)

**Posting this article on LinkedIn?** The cover is [an-ipad-to-review-the-book.jpg](banners/an-ipad-to-review-the-book.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/an-ipad-to-review-the-book.html)*
