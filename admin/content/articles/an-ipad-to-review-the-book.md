---
title: An iPad to review the book: a brief for an app that reads the PDFs, shows the comments on the page, opens its vault with my passkey and carries sgit in Swift
date: 2026-10-31
author: Dinis Cruz
author_url: about/index.html
summary: I review on the iPad because it is like a book: no notifications, nothing else on the screen. But reviewing the book of The Ultimate Insider there showed me what is missing. Preview has no full screen I could find and no way to work across several files, and the review lives in two PDFs, the book and its companion of cards, with my comments going back by hand. So this is a brief for an iPad app built to review the book, and later to read it. It reads the PDFs properly. It shows the comments, the cards and the votes on the page they are about, because once we control the medium the review does not have to be a second PDF. It sends and receives feedback through append lanes, and everything it exchanges is JSON tied to the book's semantic graph. Its library is an sgit vault on the iPad, encrypted at rest and opened with my passkey, using an extension Apple has offered apps since iOS 18. And sgit inside it is written in Swift, which would make it the third implementation of the format, after the command line and the browser. It meters what it is used for, the way the newsroom's reader account does, with a balance that can go negative, because the reader pays for the use and is not the product. The good news is that I have done part of this before. In March, a team of agents and I built a desktop app for the SGraph sites in two days, signed and notarised with my Apple developer account, ran it on an Android emulator, and set up an iOS build pipeline. This article reads that repository, says what carries over and what does not, and why I now think the iPad app should be native.
version: v0.14.14
license: https://creativecommons.org/licenses/by/4.0/
tags: ipad, apps, book, review, sgit, passkeys, briefs, publishing, article
status: published
---

!shot tb-app.webp | images/ | A sketch of the brief: the library, the page with its comments, and the append lane beside it. Nothing is built yet. | concept

## In short {#in-short}

- **I review on the iPad because it is like a book.** Nothing else is on the screen.
- **Preview gets in the way.** No full screen I could find, and no way to work across the book's several files.
- **So this is a brief for an iPad app to review the book,** and later to read it. iPad first; no Android for now.
- **The comments appear on the page they are about,** with the companion's cards, votes and highlights, sent and received through append lanes.
- **Everything it exchanges is JSON,** tied to the book's semantic graph.
- **Its library is an sgit vault, opened with my passkey,** and sgit inside it is written in Swift: a third implementation of the format.
- **It meters its use,** with a balance that can go negative. The reader pays for the use, and is not the product.
- **I have built part of this before.** A desktop app from March, signed with my Apple developer account, with an iOS pipeline.

## Why an iPad {#why}

I do a lot of my reading and reviewing on the iPad. My laptop has too much going on: messages, terminals, a dozen things moving. The iPad has none of that. It is like a book, and that is the point.

This week I reviewed RC1 of the book of [The Ultimate Insider](/articles/the-book-of-the-talk-and-its-companion.html) on it, with its companion, the PDF of 98 cards each pinned to a sentence and a page, with boxes to tick. It worked, and it showed me the gaps. Preview has visibility problems: I could not find its full screen mode, and it has no good way to see several files together, which is what a review is. And the review is in two documents, the book and the companion, joined only by page numbers and by me.

## The book app as a review desk {#desk}

So the app is designed for one job first: helping me, and the other reviewers, review the book.

- **A library, not a file.** The book, the companion, the cold read, the briefs and the graph, side by side, with what is new since I last looked.
- **A proper PDF reader.** Full screen, two pages or one, quick jumps, search, and the page I was on when I come back.
- **The comments on the page.** We made two PDFs, one to read and one to comment on, because a PDF cannot carry the conversation. In our own app it can: a reviewer's comment, a card from the companion and my tick appear on the sentence they are about.
- **Highlight and vote.** Mark a passage, agree with a comment, and it goes into the review.
- **Append lanes,** to send and receive. My highlights, votes and comments go out as signed entries; reviewers' comments and the book agents' replies come in. An append lane only grows, so the review is a record, like the [hundred writers on one lane](/articles/agent-workflows-on-ephemeral-vaults.html) we tested.
- **Pull and push from the site.** The app loads a new release of the book and its cards from the site, and pushes the review back.

Everything it exchanges is JSON: the briefs, the cards, the comments, the votes, each pointing at the node of the book's semantic graph it concerns, not only at a page number. That is what lets a comment survive the next release, when the page numbers move.

## The page as a projection {#projection}

This is where it becomes more than a review tool. If the app draws the comments on the page, then the page is only one way to show the book's content. The PDF is one projection, the website another, the app a third, and the comments, the sources and the graph can appear in any of them. That is the idea of [a book for one reader](/articles/a-book-for-one-reader.html), and the start of a better digital way to read the book, not only to review it.

## A vault that opens with my passkey {#vault}

!shot tb-vault.webp | images/ | The vault opens with the passkey: Face ID, the PRF secret, a key derived on the device, and the vault key unwrapped. | process

The feature I think matters most is that the library is an sgit vault, on the iPad, and that it opens with my passkey.

A passkey normally only proves who I am. With an extension called PRF it can also return a secret, always the same one for the same passkey and the same input, and that secret can become a key. Apple added PRF to its passkey APIs for apps in iOS 18: the [assertion input](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfassertioninput-swift.struct) asks a passkey for it, and the [registration input](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfregistrationinput-swift.struct) checks whether a new passkey supports it. So the design is:

1. **Face ID** unlocks my passkey, kept in iCloud Keychain.
2. **The passkey returns its PRF secret,** for a salt the vault keeps.
3. **A key is derived from it on the device,** and never stored.
4. **That key unwraps the vault key,** and the vault decrypts.

The files are encrypted at rest, and nothing opens them without my face and my passkey. [A browser for one](/articles/a-browser-for-one.html), my brief for an iPhone app, had one unknown: whether PRF works inside an app's web view. A native app does not need the web view for this; it asks the passkey directly. It still has to be tested on day one, on my iPad, before anything else is built. And it needs a second way in: a recovery key, printed as a QR code like [a secret is a QR code](/articles/a-secret-is-a-qr-code.html) describes, so that losing a passkey is not losing the vault.

## sgit in Swift {#swift}

[sgit is a standard, not a server](/articles/sgit-is-a-standard.html): a documented format that today has two implementations, the command line and the browser vault app, each verifying what the other writes. The iPad app is the chance for a third, written natively in Swift, Apple's own language, which reads a vault from the site, keeps it on the device and writes back what the review adds.

That is worth doing for its own sake. A format with three implementations, in three languages, written by different teams, is far more of a standard than one with two. Every place where the Swift version and the others disagree is a gap in the documentation, and finding those gaps is the work.

## The meter {#meter}

The app should also carry the newsroom's reader meter. Every page read, every graph opened, every navigation costs a little, against credits the reader buys, and the balance can go negative, as [paying after the value](/articles/paying-after-the-value.html) argues and [the user keeps the meter](/articles/the-user-keeps-the-meter.html) designs. It is easy, and it is fair: the reader pays for what they used.

All of this rests on one idea, and I want it said plainly. The reader is the customer, not the product. We do not sell the user, or the user's attention, or what we learn about them. We charge for the use of the product, the reader pays for the value they get, and the meter, like the vault, is theirs.

## What I built in March {#march}

I have done part of this before. In March, a team of agents and I built [SGraph Desktop](https://github.com/the-cyber-boardroom/SGraph-AI__Desktop), an app that wraps the SGraph websites, Send, Vault, Workspace and Tools, in native web views. I read its repository today. It records:

- **A macOS app in a day.** Built with Tauri, signed with my Apple developer account and notarised in its CI pipeline; first launched on a MacBook Air on 8 March 2026.
- **Android in two days.** On 9 March it launched on an Android emulator, from its own pipeline, with tabs at the bottom; Vault and Tools loaded, and Send refused to be framed in a web view.
- **An iOS pipeline.** A build on GitHub's macOS runners, an iOS shell with a tab bar, and a minimum of iOS 16. The repository records no launch on an iPhone or iPad.
- **A team.** An architect, a designer, a developer, DevOps, a historian and a librarian, with briefs, reviews and a record of what exists, the same way our teams work now.

Its last commit is from 9 March. What carries over is the Apple developer account, the signing and notarisation in CI, the macOS build pipeline and the team's structure. What does not is the architecture: it wraps websites, and its own architect's review found that several web views at once, its main pattern, is experimental on mobile.

## Native, this time {#native}

So I think the iPad app should be native: Swift, with Apple's own frameworks.

- **The PDF is the centre,** and Apple's PDFKit is the iPad's own PDF reader, with selection, search and annotations.
- **The passkey is native** too, through AuthenticationServices, as above.
- **sgit in Swift** is part of the point, not a cost.
- **The web is still there** for what is already web: the newsroom and the site's pages, in a web view, as the iPhone brief described.

Tauri's way, a web app inside a native shell, made sense for a launcher of websites. For a reading and review app built around PDFs, a vault and a passkey, the native parts would be most of the app.

## The plan {#plan}

1. **Phase 0, test first.** On my iPad: a passkey with PRF, returning the same secret twice; a vault key wrapped and unwrapped with it; a recovery key.
2. **Phase 1, the reader.** The library from a vault, the PDF reader, full screen, several files.
3. **Phase 2, the review.** Comments, cards and votes on the page; append lanes in and out; JSON tied to the graph.
4. **Phase 3, sgit in Swift.** Clone, read and write a vault natively, checked against the command line.
5. **Phase 4, the meter.** The reader account and credits, as on the site.

The builds run on GitHub's macOS runners, as in March, and go to the iPad through TestFlight, so no session needs the device itself.

## What this does not claim {#limits}

- **Nothing is built.** This is a brief, and the figure is a sketch.
- **PRF has not been tested on my iPad.** The API is in Apple's documentation from iOS 18; Phase 0 is there to check it.
- **No Swift implementation of sgit exists.** The format has two implementations today.
- **The March app's iOS build is not recorded as having run** on a device; the pipeline and the shell are in the repository.
- **My interest:** I build sgit, the newsroom and the book.

## Where this comes from {#sources}

- My voice memo of 31 October 2026, word for word in `admin/notes/2026-10-31__ipad-app/memo-01.md` in this site's repository.
- [the-cyber-boardroom/SGraph-AI__Desktop](https://github.com/the-cyber-boardroom/SGraph-AI__Desktop), read on 31 October 2026 at its last commit of 9 March 2026: the README, `src-tauri/tauri.ios.conf.json`, `.github/workflows/ci-pipeline__ios.yml`, the brief of 8 March on the mobile path, the architect's review of it, and the historian's records of the first macOS and Android launches.
- Apple, AuthenticationServices: the [PRF assertion input](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfassertioninput-swift.struct) and the [PRF registration input](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfregistrationinput-swift.struct), read on 31 October 2026.
- Related: [a browser for one](/articles/a-browser-for-one.html), [the book of the talk and its companion](/articles/the-book-of-the-talk-and-its-companion.html), [sgit is a standard](/articles/sgit-is-a-standard.html), [the user keeps the meter](/articles/the-user-keeps-the-meter.html).
