---
title: A custom Firefox of my own: the full plan to build one with a governed agent hive, for the laptop and the iPad, and how Mozilla could sell me the part I do not want to do, which is keeping it working
date: 2026-10-16
author: Dinis Cruz
author_url: about/index.html
summary: The previous articles argued that software vendors should let users explore and sell them the maintenance of what they build. This is the practical version, for the product I used as the example: a plan to make a custom Firefox with the workflow we showed at the agentics talk, a Ruflo hive of Claude Code workers, an sgit vault as its memory and a behaviour policy as its mandate, and to run it on my laptop and my iPad. The plan puts each thing I want on the least invasive layer that can deliver it: enterprise policies, hidden preferences, a stylesheet for the browser's own interface, an extension, and only then a patch set on Firefox's source, built in a mode that skips the C++ compile. The iPad is different: Apple requires WebKit, Firefox for iOS is a separate Swift codebase, and the only route is a fork of it, installed with a developer account. The plan works, and it shows where the cost is. Since September Firefox ships every two weeks, so a fork has to be rebased 26 times a year, on two codebases. I can have the hive do that, but it is exactly what I would pay Mozilla to do. Mozilla now sells a branded build and custom development to organisations; I think it should sell the same to one person: explore for free, keep it working for about 50p a release, a change built properly for £50 to £500.
version: v0.12.76
license: https://creativecommons.org/licenses/by/4.0/
tags: firefox, mozilla, customisation, forks, agents, ruflo, sgit, agent-behaviour-policy, ipad, business-models, explorers, villagers, town-planners, article
status: published
---

!shot fx-layers.webp | images/ | A custom Firefox, from the least invasive layer to a fork: policies, preferences, the browser's own stylesheet, an extension, and a patch set rebased every two weeks; the iPad has only one option, a fork of the separate iOS codebase. | architecture

## In short {#in-short}

- **The want.** A Firefox that behaves as I want, on the laptop and the iPad, next month and next year.
- **The workflow.** A Ruflo hive, an sgit vault and a behaviour policy, as at the agentics talk.
- **The lowest layer first.** Policies, preferences, CSS and an extension before any fork.
- **The fork is for the rest.** A front-end patch set, rebuilt in artifact mode, renamed.
- **The iPad is a second codebase.** WebKit, Swift, and a developer account to install it.
- **The cost is maintenance.** 26 releases a year since September, on two codebases.
- **Mozilla should sell it.** It already does, to organisations; the missing offer is for one person.

## What I want {#want}

[The first article](/articles/software-vendors-as-villagers.html) explained how I came back to Firefox and found a good browser I could not bend. So here is the practical question: what would it take to make my own version, with the workflow I already use, and keep it working? The point is not the first version. I might have the time to spend on version one, creating the experience I want. After that, I do not want it to break.

The workflow is the one from [the agentics talk](/articles/agentics-ready-to-sell.html): a hive, a memory and a mandate. A [Ruflo](https://ruv.sgit.ai/articles/how-it-was-made.html) hive gives the hands, Claude Code workers with one role each; an sgit vault gives the memory, encrypted and versioned, kept by me; and an [Agent Behaviour Policy](https://abp.sgit.ai/what-is-an-abp/index.html) gives each role its mandate. The plan below is a proposal: I have not run it yet, and it says so where it matters.

## Step 1: the brief {#brief}

It starts as explorer coding. I write down, in my own words, what I want: compact density everywhere; a toolbar that hides on the iPad; no sponsored content and none of the AI features I do not use; my search engine; my own new-tab page; a sidebar with the tools I use daily. That list goes into the vault, and it is the brief. The first worker's job is triage: for each want, find the lowest layer that delivers it, because every layer up is more to maintain.

## Step 2: the laptop, without forking {#layers}

Most of the list stops before a fork.

**Policies.** Firefox reads a `policies.json` from a `distribution` folder next to the browser, the mechanism companies use to manage it, documented in the [administrator reference](https://firefox-admin-docs.mozilla.org/reference/policies/). Policies cover the menu bar, the bookmarks toolbar, the home page and new-tab page, search engines, messaging, extensions and, since Firefox 150, the AI chatbot sidebar. They survive updates and need almost no maintenance.

**Preferences.** The same policies can set and lock many hidden preferences. That includes the one that turns on custom stylesheets for the browser's own interface, and, until Firefox 157 made it a setting again, the one that showed compact density.

**The browser's own stylesheet.** With that preference on, a `userChrome.css` in the profile can restyle or hide any part of the browser's interface. It is the most powerful layer without code, and the least stable: it is unsupported, and it breaks when Firefox's markup changes.

**An extension.** A sidebar, a toolbar button, context menus, a new-tab page and a theme are all [extension surfaces](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface). Extensions "need to be signed by Mozilla before they can be installed in release and beta versions of Firefox", but an unlisted one is signed and then distributed by me. They cannot restructure the browser.

The hive writes all four, each with a test, and commits them to the vault.

## Step 3: the fork, for the rest {#fork}

What no layer can do becomes a patch. Firefox's code has lived on [GitHub](https://github.com/mozilla-firefox/firefox) since 2025, though Mozilla still takes changes through its own tools. A personal fork is not a new branch of everything; it is a small patch set on top of the release, the way [LibreWolf](https://librewolf.net/docs/faq/) carries 63 patches and Debian 17, applied to each new version.

For front-end changes there is a shortcut. Firefox's [artifact mode](https://firefox-source-docs.mozilla.org/contributing/build/artifact_builds.html) "downloads pre-built C++ components rather than building them locally", so a change to the interface does not need the full compile. A full build is still within reach on a laptop: Mozilla asks for [8 GB of memory and 30 GB of disk](https://firefox-source-docs.mozilla.org/setup/linux_build.html).

One rule matters here. Mozilla's [trademark policy](https://www.mozilla.org/en-US/foundation/trademarks/distribution-policy/) says that "you may not distribute a modified form of Firefox and continue to call it Firefox". A fork for myself has to be renamed. Only Mozilla can ship a custom build called Firefox.

## Step 4: the iPad {#ipad}

The iPad is a different problem, and an important one, because that is where I started. Apple's [App Review Guideline 2.5.6](https://developer.apple.com/app-store/review/guidelines/) says "Apps that browse the web must use the appropriate WebKit framework", with exceptions only in the EU and Japan, and Mozilla has decided not to build Gecko for iOS: its head of Firefox [said](https://piunikaweb.com/2026/09/30/mozilla-gecko-ios-apple-eu-rules/) a separate build "would mean we would basically have to double the size of our iOS team". So Firefox on the iPad is a different browser: [Firefox for iOS](https://github.com/mozilla-mobile/firefox-ios), a separate Swift codebase on WebKit, open source.

None of the desktop layers exist there. The only route is a fork of that codebase, changed by the hive, built in Xcode and installed on my own iPad. With a free Apple account, [the install lasts 7 days](https://developer.apple.com/support/compare-memberships/), on up to 3 devices; a paid developer account gives a year and TestFlight. It works, and it is a second fork to keep alive.

## Step 5: keeping it working {#loop}

!shot fx-loop.webp | images/ | The maintenance loop: each Firefox release starts a run in which the hive rebases the patches, rebuilds, tests each want, compares screenshots and reports, with everything in the sgit vault and every role under a behaviour policy; I approve or refuse. | architecture

This is the step that decides whether the whole thing is worth it. Since Firefox 155, on 1 September, [a new major release is made every two weeks](https://firefox-admin-docs.mozilla.org/guides/firefox-channels/), so a fork has 26 releases a year to follow, on each of two codebases. LibreWolf, with a team, ships within "three days from each upstream stable release". Waterfox's maintainer, [writing about 15 years of forking](https://waterfox.com/blog/15-years-of-forking), describes a project often run by one person and "a few months in the red recently".

So the loop runs on every release. The rebaser applies each patch and notes every conflict; the builder rebuilds; the tester runs one test per want and compares screenshots with the last version; the reporter writes what changed, what broke and what it fixed. Everything goes into the vault. And the behaviour policy says what no worker may do: change anything but the front end, weaken security, updates or signing, use Mozilla's trademarks, or ship without my approval.

Agents can do much of this. [PortGPT](https://arxiv.org/abs/2510.22396), a research system for porting Linux patches to older versions, reported "an 89.15% success rate" on 1,815 cases. But I found no browser fork maintained without people checking the result, and the plan does not assume one: I read the report and approve every release.

## Step 6: what Mozilla could sell {#business}

!shot fx-model.webp | images/ | How Mozilla could sell it: explore in the browser for free; keep your customisation tested against every release for about 50p a release; adopt a change built properly for £50 to £500; own a maintained branded build by contract, which exists today for organisations. | comparison

The plan works, and it makes the case for its own replacement. Two codebases rebased 26 times a year is a lot of work to keep a browser the way I like it. I would much rather pay Firefox to do it, and Mozilla is better placed than I am: it is the only one that can ship a modified build called Firefox; it signs the extensions; it builds the next release and can test my changes against it before it ships; and it already maintains both codebases.

Mozilla has started down this road, for organisations. On 12 October it introduced [Firefox Enterprise](https://blog.mozilla.org/en/firefox/introducing-firefox-enterprise/), with its own branding and a management console the organisation runs itself, and its [paid support](https://blog.mozilla.org/en/firefox/firefox-support-for-organizations/), now Firefox Professional Support, offers "custom development options". What is missing is the same offer for one person, in four steps, as in [explorer coding](/articles/explorer-coding.html):

- **Explore, free.** Ask Firefox, in words, to change; it writes the policies, the stylesheet or the extension, in a sandbox, reversible. What I ask for is the brief.
- **Keep, about 50p a release.** Mozilla tests my customisation against each release before it ships, and fixes it or tells me. That is £13 a year.
- **Adopt, £50 to £500 a change.** A change that needs code, built properly, maintained as mine or shipped to everyone.
- **Own, by contract.** A maintained, branded custom build, which is roughly what Firefox Enterprise already is.

Charging per version or per change is the honest way to price it, because that is where the cost is. For Mozilla, which depends on royalties for about three quarters of its revenue, it is also the kind of income its chief executive meant by "diversifying revenue beyond search". And every customisation it keeps working tells it what its users want. I do not have to be the only one paying, either: [with the constraints of open source](/articles/the-value-of-constraints.html), the code is there for anyone who would rather do it themselves.

## What this does not claim {#limits}

- **The plan has not been run.** It is a plan; every step is checked against the documentation, not tried end to end.
- **The prices are illustrative.** Mine, not Mozilla's.
- **Mozilla's consumer offer does not exist.** Its enterprise build and support do; their prices are not public.
- **No agent maintains a browser fork alone.** The plan keeps a person approving every release.
- **The iPad route needs a developer account.** And it only changes what Firefox for iOS can change on WebKit.

If you want a customised build of a tool your team depends on, kept working, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo of mine on 16 October 2026, written by this site's agent in the voice of this site; the plan and the editorial responsibility are mine. Mozilla: [Firefox channels](https://firefox-admin-docs.mozilla.org/guides/firefox-channels/), the [policy reference](https://firefox-admin-docs.mozilla.org/reference/policies/), [artifact builds](https://firefox-source-docs.mozilla.org/contributing/build/artifact_builds.html), [building on Linux](https://firefox-source-docs.mozilla.org/setup/linux_build.html), [extension user interfaces](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface), [signing](https://extensionworkshop.com/documentation/publish/signing-and-distribution-overview/), the [distribution policy](https://www.mozilla.org/en-US/foundation/trademarks/distribution-policy/), [Introducing Firefox Enterprise](https://blog.mozilla.org/en/firefox/introducing-firefox-enterprise/), 12 October 2026, and [Firefox Support for Organizations](https://blog.mozilla.org/en/firefox/firefox-support-for-organizations/); Apple, [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) and [membership comparison](https://developer.apple.com/support/compare-memberships/); [PiunikaWeb](https://piunikaweb.com/2026/09/30/mozilla-gecko-ios-apple-eu-rules/), 30 September 2026, relaying Ars Technica; [LibreWolf FAQ](https://librewolf.net/docs/faq/) and its source repository; [Waterfox](https://waterfox.com/blog/15-years-of-forking), 27 March 2026; Li and others, [PortGPT](https://arxiv.org/abs/2510.22396), 2025. Read on 16 October 2026.
