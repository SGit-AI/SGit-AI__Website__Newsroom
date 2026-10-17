---
title: Fix the page yourself: the bookmarklet trick from my security days, a page API every site should publish, and why the next user experience is the one the user customises, with six fixes running on this newsroom
date: 2026-10-17
author: Dinis Cruz
author_url: about/index.html
summary: Years ago, during a security assessment, I packaged an exploit as a bookmarklet, a bookmark that runs a line of JavaScript on the page you are on, and gave it to the business owner to show that one user could see data they should never see. She was more excited about the interface I had wrapped it in than about the vulnerability, because my quick Bootstrap page was so much better than the application she used every day. That story still describes most of the web. Sites are built to show ads and hold attention, not to let me read; even the newest products have gaps their own users could fix in a line of code. My argument is that the next generation of user experience is the one the user customises, and that sites should encourage it: publish a small JavaScript API for the page, the primitives a fix needs, so that every fix is one line, the same API serves tests and agents, and the fixes people keep become the best brief the site will ever get. It is also the cheapest route to accessibility, because each reader can build what they need on primitives the site provides. This newsroom now does it: a page API with six fixes, from reading mode to WCAG text spacing, as buttons, bookmarklets and code. The rest is a brief: a community library of fixes, per-site extensions that only touch the tab you click, and the same API on sgit.ai and ruv.sgit.ai.
version: v0.12.93
license: https://creativecommons.org/licenses/by/4.0/
tags: ux, customisation, bookmarklets, browser-extensions, javascript, accessibility, explorer-coding, agents, playwright, brief, article
status: published
---

!shot pz-before-after.webp | images/ | One click on this newsroom: an article as published, and the same page after three fixes from its page API, reading mode, bigger text and an outline of the headings. Nothing on the site changed; it is CSS in the reader's browser. | comparison

## In short {#in-short}

- **A bookmarklet is a line of code you click.** I learnt to use them breaking into websites.
- **My best demo was remembered for its UI.** The exploit mattered less to the owner than the better interface.
- **Most sites still fight their readers.** Built for ads and attention, not for the person reading.
- **The next UX is customised by the user.** And paid for, so someone else keeps it working.
- **Sites should publish the primitives.** A page API makes every fix one line, and serves tests and agents too.
- **The fixes are briefs.** The ones people keep are the roadmap; adopt them, and the script disappears.
- **It is the cheapest accessibility there is.** Each reader builds what they need, on what the site provides.
- **It runs here.** [Six fixes on this newsroom](https://newsroom.sgit.ai/demos/fixes/index.html), as buttons, bookmarklets and an API.

## The bookmarklet that out-designed the application {#story}

A long time ago, when most of my work was finding vulnerabilities in other people's software, I picked up a habit. Instead of describing an attack, I would write it as a small piece of JavaScript and run it in the page: log in, go to a particular screen, call what needed calling, show the result. Often I packaged it as a bookmarklet: a bookmark whose address is a line of JavaScript instead of a web page. You click it, and it runs on whatever page you are on. Nothing to install.

On one assessment I found an injection flaw in a business application that let one user see data they should never have been able to see, much of it personal. To show the business owner what that meant, I wrapped the whole thing in a bookmarklet and gave it to her: click here. It pulled the records out and laid them in a clean interface I had thrown together with Bootstrap.

Her reaction was not the one I expected. She was far more excited about the interface than about the vulnerability. Could they have this? I said that this was a serious finding, the kind that is a legal problem when personal data is involved. Yes, she said, but can we have this UI? It was so much better than the one she used every day.

I still think about that, because it says something true about software. That application was legacy even then, and its users had simply stopped expecting anything better. A security consultant's afternoon of Bootstrap beat years of the product.

## Every site still fights its readers {#problems}

Most of the web has the same problem today, and it is not only legacy software. LinkedIn is designed to show ads and drive engagement; when I want to read a post, I get a menu, suggestions and a feed I did not ask for. YouTube, when I want to watch one video, gives me fifty things competing for my attention. Newspapers wrap their article in everything except the article. Even the newest products, the AI assistants built by some of the best engineering teams in the world, have interface gaps their users notice in the first hour and could fix in a line of code.

Some of that is not the site's fault: there are always more requests than time. But much of it is, because the best teams have the means to let users change what they need and have not done it. The default experience is built for the average user and for the business model. Nobody's experience is the average.

## The next user experience is the one the user customises {#customised}

My argument is simple. The next generation of user experience is the one the user customises: the reading mode, the layout, the contrast, the things hidden and the things kept, set by the person reading, for themselves. And then, as I argued in [Software vendors should become villagers and town planners](/articles/software-vendors-as-villagers.html), it is the one they pay for, so that somebody else keeps their customisation working through every release. I do not want to maintain my fixes. I want to make them, and pay someone to keep them alive.

People already do this, at the edges. Bookmarklets have been around since the early web. Userscript managers, from Greasemonkey to Tampermonkey and Violentmonkey, run community scripts from libraries like Greasy Fork; Stylus does the same with user styles; Arc's Boosts let you restyle a site from inside the browser. Every browser has a reader mode. What all of them have in common is that the site is not involved. They guess at its structure, they break when it changes, and the most capable of them need an extension with access to every site you visit.

## Sites should publish the primitives {#primitives}

The fix is for the site to take part. If a page publishes a small JavaScript API, the primitives a fix needs, then a fix is one line, it does not break when the markup changes, and it does not need to guess.

We already have the convention. The SGraph tools put each tool's API on the page at `window.__tools`, announce it with a `tool:ready` event, and describe it in an `api.json`; the principle, in the architect's review, is "API is the tool, UI is a consumer". The same surface that a user's fix calls is the one Playwright tests call, and the one an agent driving a browser calls. A page with an API is a page that can be automated, tested and fixed with the least code, by people and by agents alike.

!shot pz-loop.webp | images/ | The user's fix is the best brief the site will get: the site publishes primitives; readers write fixes in a line or two; the site learns from the fixes people keep; popular ones are adopted as settings or themes, and personal ones are maintained for a fee. | architecture

And here is the part sites should want. A fix a user writes, and keeps, is the clearest brief the site will ever get: what a real person needed, in a form that runs. It is [explorer coding](/articles/explorer-coding.html) applied to the page in front of you. The fixes many people keep should become settings, and then the script disappears, because the product does it. This newsroom has done exactly that once already: the first outside reaction to its Industry Wire was two words on WhatsApp, "Dark mode!", and [five themes](/articles/dark-mode-and-four-more.html) shipped soon after. The personal fixes that stay personal are where the vendor becomes the villager and is paid to maintain them.

## It is the cheapest accessibility there is {#accessibility}

There is a large accessibility angle here, and I think it is where the money is for companies. Every reader's needs are different: bigger text, more spacing, higher contrast, no motion, no clutter, a different order. A site that tries to build every variation itself never finishes. A site that publishes the primitives, and lets each reader build, or install, what they need, serves far more people for far less.

The standards already point this way. WCAG's success criterion 1.4.12, Text Spacing, asks that content survive a user changing line, paragraph, letter and word spacing, which assumes users will. And in the European Union the European Accessibility Act has applied to many consumer services since 28 June 2025, which gives companies a reason to care about this beyond good intentions.

## How the fixes reach the page {#delivery}

There are three ways to deliver a fix, and the order matters.

| How | Who triggers it | What it can reach | Notes |
|---|---|---|---|
| A bookmarklet | The reader, by clicking | The page they are on, when they click | Nothing to install; a site's Content Security Policy can block it, or the script it loads |
| An extension per site, with `activeTab` | The reader, by clicking the extension | The current tab only, until they leave it | Chrome's `activeTab` grants "temporary access to the currently active tab when the user invokes the extension", with no install warning |
| A userscript manager | Runs on its own | Every site it is allowed on | Chrome now requires an "Allow User Scripts" toggle for its userScripts API; one extension with broad access |

I prefer the first two, because the reader is the one who clicks. I do not like one extension with access to every site I visit; one small extension per site, that only touches the tab I click it on, is a much smaller thing to trust. Such an extension could be shipped from a GitHub repository or an encrypted vault and loaded locally, so the reader can see exactly what they are installing.

## It runs here {#here}

So we did it for this newsroom. [Fix the page](https://newsroom.sgit.ai/demos/fixes/index.html) is a page with six fixes, each one a button to try, a bookmarklet to drag to your bookmarks bar, and a call on a page API:

- **Reading mode.** Only the text, in one column: no menu, no strip, no chips, no footer.
- **Bigger text.** Everything at 125%.
- **High contrast.** Black on white, links underlined.
- **Text spacing.** The spacing WCAG 1.4.12 says a page must survive.
- **Outline.** A box of the page's headings, to jump around.
- **Markdown.** The same page as its markdown twin, which every article here has.

Underneath is one small file, `page-fixes.js`, versioned and immutable at its path, which puts an API at `window.__tools.page`: `list()`, `apply(name, on)`, `toggle(name)` and `reset()`, with an [api.json](https://newsroom.sgit.ai/assets/page-fixes/v0/v0.1/v0.1.0/api.json) that describes it. A bookmarklet is one line that loads the file if needed and calls `toggle`. What a reader turns on is remembered for this site, in their browser, and nothing leaves it. The same API is what a Playwright test or an agent calls.

The page also has a fix that needs no file at all: a generic reading mode for any site, in one line. It shows the limit of fixing a site from the outside. It hides the usual tags, and it gets the rest wrong, because it has to guess. The newsroom's own reading mode does not guess, because the site says which parts are its chrome.

## The brief {#brief}

This is the plan, for this site and its neighbours.

1. **Load the page API on every page of the newsroom**, so a fix never needs the loader, and name the parts of each page in it, not only the chrome.
2. **A community library of fixes.** One file per fix, versioned paths, each with the one-line bookmarklet beside it, and a page per site listing what exists.
3. **A per-site extension with `activeTab`**, built from that library, shipped from a GitHub repository or a vault, loaded locally.
4. **The same API on sgit.ai and ruv.sgit.ai**, so the fixes are a family, not a one-off.
5. **Count which fixes are kept**, in the reader's own record, sent only if they choose, and treat the list as the roadmap.
6. **Adopt the popular ones** into settings and themes, and retire their scripts.
7. **Let a model write the fix.** Chrome now ships [a model in the tab](/articles/a-model-in-the-tab.html); a reader should be able to say what they want changed and get a one-line fix on the page API, to keep or throw away.
8. **Pay to keep it.** Personal fixes, maintained across releases, are a product, as [the villagers argument](/articles/software-vendors-as-villagers.html) says.

There is more to say about design itself, and that will be the subject of a site of its own.

## What this does not claim {#limits}

- **Other sites can refuse it.** A strict Content Security Policy can block a bookmarklet or the script it loads.
- **Six fixes, one site.** A start, not a library.
- **No extension yet.** The per-site extension is designed here, not built.
- **The security story is from memory.** The details of that assessment are years old and deliberately left out.
- **Customisation is not a substitute for good defaults.** It is what a good default makes room for.

If you have a fix you would like on this site, or a site you would like fixed, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo of mine on 17 October 2026, written by this site's agent in the voice of this site; the argument, the story and the editorial responsibility are mine. The fixes, the page API and the page were built and tested by this site's agent the same day: [Fix the page](https://newsroom.sgit.ai/demos/fixes/index.html), [page-fixes.js](https://newsroom.sgit.ai/assets/page-fixes/v0/v0.1/v0.1.0/page-fixes.js) and its [api.json](https://newsroom.sgit.ai/assets/page-fixes/v0/v0.1/v0.1.0/api.json). The page API convention: the SGraph tools' JS API primitive, in [the-cyber-boardroom/SGraph-AI__Tools](https://github.com/the-cyber-boardroom/SGraph-AI__Tools), the architect's review of 9 April 2026 and the debrief on the JS API for agents. Chrome: [the activeTab permission](https://developer.chrome.com/docs/extensions/develop/concepts/activeTab) and [the userScripts API](https://developer.chrome.com/docs/extensions/reference/api/userScripts). Accessibility: W3C, [WCAG 2.2, success criterion 1.4.12, Text Spacing](https://www.w3.org/TR/WCAG22/#text-spacing); the European Accessibility Act, Directive (EU) 2019/882. Context on this site: [Explorer coding](/articles/explorer-coding.html), [Software vendors should become villagers and town planners](/articles/software-vendors-as-villagers.html), [A custom Firefox of my own](/articles/a-custom-firefox-of-my-own.html), [Dark mode, and four more](/articles/dark-mode-and-four-more.html), [Custom UIs are not the exception](/articles/custom-uis-are-not-the-exception.html) and [A model in the tab](/articles/a-model-in-the-tab.html).
