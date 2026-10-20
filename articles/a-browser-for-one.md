# A browser for one: an iPhone app that only reads my newsroom, why I am building it now, and why I will still pay someone to keep it working, sgit.ai

> The browsers on my iPhone have frustrated me to the point where I would like to build one. Not a general browser: an app that only opens my newsroom, where I left it, knows what I have read, opens my vault, keeps my tabs, works offline, never reloads a page on its own, lets me build my own reading workflows, and receives what my agents send me. A year ago I would have put up with it. Now I can do something about it, and that changes how much bad interface I am willing to tolerate. This is the brief. The facts decide most of it. In the UK an iPhone app that browses the web must use WebKit; Firefox and Chrome on iOS are WebKit too. Passkeys inside an app and push notifications both need Apple's paid developer membership, and the app has to be built on a Mac, so not by a cloud session like the one that writes this site. The one real unknown is whether the passkey extension the vault depends on works inside an app's web view, so that is the first thing to test. And there is a second point, which matters more than the app. Once it works, it will be part of my day, and I will not want to maintain it. Not because I cannot; because it is not my focus. Being able to compile a Linux kernel does not mean I want to. Even power users will pay someone to keep the thing they built working, and this app is the first example I will live with.

*Source: <https://newsroom.sgit.ai/articles/a-browser-for-one.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / A browser for one: an iPhone app that only reads my newsroom, why I am building it now, and why I will still pay someone to keep it working

# A browser for one: an iPhone app that only reads my newsroom, why I am building it now, and why I will still pay someone to keep it working

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-18 · [article v1.1.0, 2 versions](versions/a-browser-for-one.md) · [newsroom v0.12.111](https://newsroom.sgit.ai/admin/versions.html) · browsersioswebkitnewsroomexplorer-codingvillagersbriefarticle

***Abstract:** The browsers on my iPhone have frustrated me to the point where I would like to build one. Not a general browser: an app that only opens my newsroom, where I left it, knows what I have read, opens my vault, keeps my tabs, works offline, never reloads a page on its own, lets me build my own reading workflows, and receives what my agents send me. A year ago I would have put up with it. Now I can do something about it, and that changes how much bad interface I am willing to tolerate. This is the brief. The facts decide most of it. In the UK an iPhone app that browses the web must use WebKit; Firefox and Chrome on iOS are WebKit too. Passkeys inside an app and push notifications both need Apple's paid developer membership, and the app has to be built on a Mac, so not by a cloud session like the one that writes this site. The one real unknown is whether the passkey extension the vault depends on works inside an app's web view, so that is the first thing to test. And there is a second point, which matters more than the app. Once it works, it will be part of my day, and I will not want to maintain it. Not because I cannot; because it is not my focus. Being able to compile a Linux kernel does not mean I want to. Even power users will pay someone to keep the thing they built working, and this app is the first example I will live with.*

A browser for one, sketched on an iPhone. It opens on the newsroom where it was left, with tabs in a strip that hides as you read, read and unread marked, the vault open, an inbox of what the agents sent, and reading workflows as runs of tabs. Underneath: a native Swift shell around WebKit, a small bridge to the page, an offline cache, and a push sender. The first step is a test: do passkeys with the PRF extension work inside the app.

## In short

- **The browsers on my phone have lost my patience.** Wrong page, reloads, no offline, no memory of where I was.
- **So the idea is a browser for one.** An app that only reads my newsroom, and knows what I have read.
- **In the UK it has to be WebKit.** So are Firefox and Chrome on iOS; other engines are allowed only in the EU and Japan.
- **It needs the paid developer membership and a Mac.** For passkeys in the app, for push, and for building it.
- **One unknown, tested first.** Whether the vault's passkey extension works inside an app.
- **Empowerment lowers patience.** When I can build it, a bad interface stops being something I put up with.
- **I will still pay someone to maintain it.** Being able to does not mean wanting to.

## Why now

Every day I read and manage this newsroom from my iPhone, and every browser I use gets something wrong. One loads the wrong thing; another refreshes the page I was halfway through; none has a good offline mode; none keeps track of where I was across days; none understands what I have been doing; all of them use too much of the screen for themselves. I have lived with this for years, like everyone.

What changed is not the browsers. It is me. After weeks of building with agents, things that would have sounded unreasonable, like writing my own browser for one site, do not sound unreasonable any more. I have hit this problem enough times, and I now have enough leverage, that the frustration has turned into a brief. And there is a practical trigger too: I have some compute left before my next batch, and this is a good use of it. Constraints shape what gets built.

## What it does

It is a browser for one site and one person:

- **It opens on the newsroom, where I left it.** The last tab, the same place on the page.
- **It knows what I have read.** The site already records it, section by section; the app shows read, part read and unread in its own lists, and the [folded views](your-reading-your-controls.md) work as they do on the site.
- **It opens my vault**, with my passkey, as the site does.
- **Tabs, with almost no chrome.** A strip that hides when I read, no address bar unless I ask.
- **It never reloads a page on its own**, and every article I open stays readable offline, figures included.
- **My own workflows.** A morning run: the wires, then new articles, then [the briefs](https://newsroom.sgit.ai/briefs/index.html). A review run: articles with open findings. A catch-up run: articles changed since I last read them. Each is a small file in my vault, so it travels with me and an agent can propose a new one.
- **It hears from my agents.** A daily brief, a review, an answer to a note, in an inbox in the app.

It is a layer of business logic on top of the site. The logic that proves itself in the app should move into the site, so the app gets thinner over time, not thicker.

## Which engine

I asked which engine to build on: WebKit, Firefox or Chrome. On an iPhone in the UK, the question answers itself. Apple's rule is that an app that browses the web must use WebKit; the exceptions are the EU, since iOS 17.4, and [Japan, since iOS 26.2](https://developer.apple.com/support/alternative-browser-engines/). Firefox and Chrome on iOS are WebKit underneath. Mozilla [said in September](https://piunikaweb.com/2026/09/30/mozilla-gecko-ios-apple-eu-rules/) that an EU-only Gecko build would roughly double its iOS team, and Google's port of its own engine to iOS stayed an experiment.

The UK may change this. The Competition and Markets Authority [designated Apple](https://www.gov.uk/cma-cases/sms-investigation-into-apples-mobile-platform) with strategic market status on 22 October 2025, with the browser engine in scope, but as of today it has published no requirement about engines. So the app is a small native shell, in Swift, around Apple's own web view, which since iOS 26 has a [SwiftUI version](https://webkit.org/blog/16993/news-from-wwdc25-web-technology-coming-this-fall-in-safari-26-beta/). This is the same conclusion [a custom Firefox of my own](a-custom-firefox-of-my-own.md) reached for the iPad: on Apple's phones and tablets, the engine is not a choice.

## What it costs

Two facts decide the rest.

**It needs Apple's paid developer membership.** In Apple's [capability table](https://developer.apple.com/help/account/reference/supported-capabilities-ios/), *Associated domains* and *Push notifications* are available to the paid programmes and not to a free account. Associated domains are what let a passkey for newsroom.sgit.ai work inside the app, which is how the vault opens; push is how my agents reach the phone. A free account also expires the install every seven days.

**It has to be built on a Mac.** An iPhone app is built and signed with Xcode on macOS, so the cloud sessions that write this site cannot build it. Either a session runs on my Mac, or the build runs on GitHub's macOS machines, at about [$0.062 a minute](https://docs.github.com/en/billing/reference/actions-runner-pricing) against $0.006 for Linux, or on Apple's Xcode Cloud, with 25 hours a month included in the membership. I would rather the agent builds in the cloud and sends the app to my phone through TestFlight, so it never needs the phone.

There is a cheaper path, and the brief keeps it as the fallback: add the site to the Home Screen. Since iOS 26 every site added that way opens as a web app, passkeys work as in Safari, and web push works since iOS 16.4. No Mac, no membership. What it cannot give me is native tabs and a reliable offline mode, which are half of why I want this.

## The one unknown

The vault opens with a passkey and an extension called PRF, which turns the passkey into a key. Safari supports it for iCloud Keychain passkeys from iOS 18. No source I could find confirms that it works inside a web view in a third-party app. So the first thing the agent builds is the smallest app that tries the site's own unlock. If PRF does not come back, the app does the passkey ceremony natively and hands the result to the page. Either way, it is better to know on day one, not after the tabs are built.

## Even power users want someone to maintain it

This is the part that matters beyond my phone. When this app works, it will be part of my workflow every day. And I will not want to maintain it. Not because I cannot; I could easily take the time. Because it is not my focus. I would rather do something else. Being able to compile a Linux kernel does not mean I want to compile Linux kernels, and being able to code does not mean I want to spend my evenings keeping my own browser up to date with every iOS release.

That is the argument of [software vendors as villagers](software-vendors-as-villagers.md), and now I am the customer. The explorer, me, builds exactly the app I want, which is a better brief than any document. Then I would like to hand it to someone, a person or a company, and pay a couple of pounds a month for them to keep it working: rebuild it when iOS changes, fix what breaks, keep the behaviour policy current. [Who will fix your mess](who-will-fix-your-mess.md) asked who does that for companies; this is the same question for one person.

And it says something about what happens as people get this kind of power. Patience for bad interfaces wears thin when you can do something about them. That is good for users, and a warning for anyone shipping software that gets in their way.

## The brief

The full build brief is a note for the agent that builds it: [a browser for one](https://newsroom.sgit.ai/admin/notes/2026-10-18__a-browser-for-one.md). In short:

1. **Phase 0, test first.** Passkeys with PRF inside the app; the association file on the site; whether the web view's storage survives.
2. **Phase 1, the app.** Opens where I left it, tabs, offline, no reloads, knows the reading, a small bridge to the page with a written policy.
3. **Phase 2, workflows.** Runs of tabs I define, kept in my vault.
4. **Phase 3, from the agents.** An inbox polled from the vault, and push through a small sender.

It is also on [the briefs page](https://newsroom.sgit.ai/briefs/index.html#browser-for-one), with its session brief.

## What this does not claim

- **Nothing is built.** This is a brief.
- **PRF inside an app's web view is untested.** It is the first thing the build checks.
- **The UK engine rule may change.** The designation covers browser engines; no requirement has been published yet.
- **The prices are as of 18 October 2026.** GitHub's per-minute rates and Apple's membership change.
- **The fallback is real.** A Home Screen web app may turn out to be enough.

If you have built a single-site browser on iOS and know where it hurts, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo from me on 18 October 2026. The research, read that day by a research agent: Apple, [alternative browser engines](https://developer.apple.com/support/alternative-browser-engines/), [supported capabilities](https://developer.apple.com/help/account/reference/supported-capabilities-ios/) (the table read directly) and [supporting passkeys](https://developer.apple.com/documentation/authenticationservices/supporting-passkeys); the CMA's [case page](https://www.gov.uk/cma-cases/sms-investigation-into-apples-mobile-platform); WebKit, [WWDC25](https://webkit.org/blog/16993/news-from-wwdc25-web-technology-coming-this-fall-in-safari-26-beta/) and [app-bound domains](https://webkit.org/blog/10882/app-bound-domains/); GitHub, [runner pricing](https://docs.github.com/en/billing/reference/actions-runner-pricing); PiunikaWeb on [Mozilla and Gecko on iOS](https://piunikaweb.com/2026/09/30/mozilla-gecko-ios-apple-eu-rules/), 30 September 2026. The site's own unlock: `assets/door.js` and `assets/vault-pane/vault-pane.js`. Related: [a minimal viable browser](a-minimal-viable-browser.md), [a custom Firefox of my own](a-custom-firefox-of-my-own.md), [software vendors as villagers](software-vendors-as-villagers.md), [who will fix your mess](who-will-fix-your-mess.md), [explorer coding](explorer-coding.md), [your reading, your controls](your-reading-your-controls.md). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Site & engineeringStartups & strategy[This article as a graph →](graphs.md#a-browser-for-one)

### Builds on

- [Your reading, your controls: the meter charges for what you read, you can pause or reset it, and what you have read folds away in six ways](your-reading-your-controls.md) The meter now charges for what is read; the reader can pause, reset or mark it, and what was read folds away six ways, with a line and a paragraph per section.
- [A custom Firefox of my own: the full plan to build one with a governed agent hive, for the laptop and the iPad, and how Mozilla could sell me the part I do not want to do, which is keeping it working](a-custom-firefox-of-my-own.md) A full plan to build a custom Firefox for laptop and iPad with a governed agent hive, and why the part worth paying Mozilla for is keeping it working.
- [Software vendors should become villagers and town planners: let users explore on top of the product, sell them the maintenance of what they build, and use Firefox as the example of what happens if you don't](software-vendors-as-villagers.md) Users can now rebuild the part of a product they need; what stops them is maintenance. Vendors should sell that, as villagers and town planners.
- [Who will fix your mess? An answer to HBR's "deployment gap" from what this site has already published: explorers, villagers and town planners, a record of what the agents built, and open source so the answer never depends on one partner](who-will-fix-your-mess.md) HBR's deployment gap, answered from this site's articles: explorers, villagers and town planners, a record the agents keep, and open source.
- [A minimal viable browser: why Firefox is the one that can build it, and what it would take](a-minimal-viable-browser.md) A small kernel and components loaded when needed: a browser for one app, one agent or a reader. Mozilla can build it, and should sell it as speed.
- [Explorer coding: a better name for what people call vibe coding, what it is good for, and the handover to villagers and town planners before anyone depends on it](explorer-coding.md) Call it explorer coding, not vibe coding: the best thing since the spreadsheet, the best brief there is, and not ready to be in line until villagers take it.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 190 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=190)

**Posting this article on LinkedIn?** The cover is [a-browser-for-one.jpg](banners/a-browser-for-one.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/a-browser-for-one.html)*
