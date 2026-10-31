# Explorer coding: a better name for what people call vibe coding, what it is good for, and the handover to villagers and town planners before anyone depends on it, sgit.ai

> I would like to propose a better name for what is usually called vibe coding: explorer coding. Vibe coding sounds as if people are just typing and ad-libbing, and I have never liked it, because what they are doing is the best thing to happen to software since the spreadsheet: everyone with a need can now explore it by building, with the fast feedback loop that made spreadsheets win, and what they build is a better brief than any document. Explorer is Simon Wardley's word for exactly that kind of work. It also makes the limit clear. An explorer-coded app may look and feel like an application, but nobody has read the code or checked the architecture, and it is not ready to be in line: once other people depend on it, it is mission critical, and it needs villagers to maintain it, with agent behaviour policies, data handling and releases that do not break it, and then town planners who own the code in production and are accountable for it, as the Linux kernel, Fedora and GitHub already say the human who ships code must be. The further towards commodity, the fewer agents in line and the more deterministic code. And it suggests a commercial model: every product should have an explorer version, where users reshape it by talking to it, and paid conversions from there to a villager product and a town planner one.

*Source: <https://newsroom.sgit.ai/articles/explorer-coding.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Explorer coding: a better name for what people call vibe coding, what it is good for, and the handover to villagers and town planners before anyone depends on it

# Explorer coding: a better name for what people call vibe coding, what it is good for, and the handover to villagers and town planners before anyone depends on it

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-16 · [article v1.3.0, 4 versions](versions/explorer-coding.md) · [newsroom v0.12.76](https://newsroom.sgit.ai/admin/versions.html) · explorer-codingvibe-codingwardley-mapsexplorersvillagerstown-plannerscitizen-developeraccountabilitybusiness-modelsagentsarticle

***Abstract:** I would like to propose a better name for what is usually called vibe coding: explorer coding. Vibe coding sounds as if people are just typing and ad-libbing, and I have never liked it, because what they are doing is the best thing to happen to software since the spreadsheet: everyone with a need can now explore it by building, with the fast feedback loop that made spreadsheets win, and what they build is a better brief than any document. Explorer is Simon Wardley's word for exactly that kind of work. It also makes the limit clear. An explorer-coded app may look and feel like an application, but nobody has read the code or checked the architecture, and it is not ready to be in line: once other people depend on it, it is mission critical, and it needs villagers to maintain it, with agent behaviour policies, data handling and releases that do not break it, and then town planners who own the code in production and are accountable for it, as the Linux kernel, Fedora and GitHub already say the human who ships code must be. The further towards commodity, the fewer agents in line and the more deterministic code. And it suggests a commercial model: every product should have an explorer version, where users reshape it by talking to it, and paid conversions from there to a villager product and a town planner one.*

Explorer coding and its handover: explorers build, villagers maintain, town planners own the code in production.

## In short

- **Call it explorer coding.** What people call vibe coding is exploration, and the word should say so.
- **It is the best thing since the spreadsheet.** Everyone with a need can now build, with a fast feedback loop.
- **What it produces is a brief.** The best one there is: it runs.
- **It is not ready to be in line.** Once others depend on it, it is mission critical, and needs more.
- **Villagers maintain it; town planners own it.** Policies, data and releases first; accountable code after.
- **Towards commodity, fewer agents in line.** And more deterministic code.
- **Every product needs an explorer version.** With paid conversions to villager and town planner products.

## Why not vibe coding

The term is [Andrej Karpathy's](https://en.wikipedia.org/wiki/Vibe_coding), from a post in February 2025: "There's a new kind of coding I call "vibe coding", where you fully give in to the vibes, embrace exponentials, and forget that the code even exists." He was describing throwaway weekend projects, and by November it was Collins Dictionary's word of the year. In [an article in September](saas-apocalypse-decided-by-inertia-not-by-ai.md) I wrote that I did not love it, but that the word had won. I would like to go further now, because the word is doing harm. It sounds as if people are just typing, ad-libbing, going with a feeling; it is a little demeaning to the people doing it, and it hides what is actually happening. I am not alone in this: Andrew Ng [said in May 2025](https://www.aol.com/andrew-ng-says-vibe-coding-065832544.html) "It's unfortunate that that's called vibe coding", and that coding with AI is "a deeply intellectual exercise".

So I would like to propose **explorer coding**. I considered spreadsheet coding, because of where this comes from, and brief coding, because of what it produces. But if you think in [Wardley maps](https://blog.gardeviance.org/2023/12/how-to-organise-yourself-dangerous-path.html), the right word is already there. Explorers "explore never-before-discovered concepts, the uncharted land"; "They show you wonder but they fail a lot." That is exactly what someone does when they build the tool they need with an agent. I could not find anyone using explorer coding as a term. The nearest is *exploratory programming*, the [research term](https://dblp.org/rec/conf/vl/KeryM17.html) for programming while the requirements are still being discovered, which is a good ancestor to have.

## The best thing since the spreadsheet

People have always built software with whatever they controlled, and for most of them it was a spreadsheet. Spreadsheets won because of the feedback loop: change a cell and see the result, a read-evaluate-print loop for people who would never call it that. Everybody was already exploring; it was just very slow, because anything beyond a spreadsheet meant writing a document and waiting for someone else to build it. What has changed is that the loop is now fast for anything: an app, a workflow, a customisation of a product, a change to the [interface of a single moment](custom-uis-are-not-the-exception.md).

That is why I think it is the best thing to happen to software since the spreadsheet, and why [the citizen developer is good news](the-citizen-developer.md). It is an explosion of empowerment. I was talking to someone who works in HR this week, and once we started to explore what her team will be doing, the apps, the customisations and the workflows they will build, and the agents they will have to manage, her answer was: "Amazing! When can I start?"

And what explorers produce is the best brief there is. A working app says what its user wants better than any document, because it runs.

## Not ready to be in line

This is the part the new word makes easier to say, and the part that matters most. An explorer-coded app may look like an application and feel like an application, but it is a brief. Nobody has read the code. Nobody has validated the architecture. It does not meet any internal standard, and it is not ready to be run in production, or, the better way to say it, not ready to be *in line*: in the path of work that other people depend on.

The trap is that dependence comes quickly. Once something gets used, it is mission critical, because people depend on it; even for one person, if it replaced how they work, it is mission critical to them. From then on it has to be maintained, checked and kept working, and new versions cannot break it.

## Villagers and town planners

That is the villagers' work. They take what the explorer built and make it safe for others to depend on: maintenance, tests around what people rely on, releases that do not break it, and, because these apps now run agents, [agent behaviour policies](your-own-newsroom.md#policy) and rules for the data the agents touch. In Wardley's words, they "turn the prototype into a product, make it manufacturable, listen to customers".

When it matures, the town planners take it, and they own the code. Here the accountability is not new: more and more of the industry already says that whoever ships code is responsible for it, however it was written. The Linux kernel's [rules for AI coding assistants](https://docs.kernel.org/process/coding-assistants.html) say "AI agents MUST NOT add Signed-off-by tags" and "Only humans can legally certify the Developer Certificate of Origin", and make the submitter responsible for "Taking full responsibility for the contribution". Fedora's [policy proposal](https://communityblog.fedoraproject.org/council-policy-proposal-policy-on-ai-assisted-contributions/) says "The contributor is always the author and is fully accountable for their contributions." We cannot make an explorer accountable for code they never read. We can make the team the work is handed to accountable, and the town planners above all.

They can use agents, of course. But the direction is set by where the code sits on the map: the further towards commodity, the fewer agents in line, and the more deterministic code. I have argued it for [code review](if-somebody-built-a-company-on-code-review.md), where "A model has no place in line on a mission-critical path", and for [cost](agentic-cost-is-an-engineering-problem.md): explorer-style code running in a commodity place is an engineering problem.

## An explorer version of every product

An explorer version of every product and the paid conversions from it, up to the town planner product. Proposed.

The name also suggests a commercial model, and it follows from [the previous article](software-vendors-as-villagers.md). Products need to become explorer-friendly; more than that, they need an explorer version. In it, users can talk to the product with a model, reshape it, move things around and keep their own version; the product is treated as primitives. When the user has something they want to keep, they submit it, and pay to convert it into a villager product, maintained across releases, and, if it matters enough, into a town planner product, built properly or kept as a maintained fork. Each step is a revenue stream, and each submission tells the vendor exactly what its users want.

The same path should exist inside companies, between a department and its engineers, and around open-source projects, between their users and their maintainers. [The custom Firefox plan](a-custom-firefox-of-my-own.md) walks through what it would look like for one product.

## What this does not claim

- **Explorer coding is a proposal.** I found no established use of the term; exploratory programming is its ancestor.
- **Not that explorer-coded apps are good code.** The point is that they are briefs, not products.
- **The HR conversation is one conversation.** An illustration, not a survey.
- **The explorer version of a product is a proposal.** I know of no vendor selling it.

If you want to set up the handover from explorers to villagers and town planners in your company, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 16 October 2026, written by this site's agent in the voice of this site; the argument and the editorial responsibility are mine. Andrej Karpathy's post of 2 February 2025, quoted from [Wikipedia](https://en.wikipedia.org/wiki/Vibe_coding); Andrew Ng, reported by [Business Insider via AOL](https://www.aol.com/andrew-ng-says-vibe-coding-065832544.html); Simon Wardley, [How to organise yourself: the dangerous path to Explorer, Villager and Town Planners](https://blog.gardeviance.org/2023/12/how-to-organise-yourself-dangerous-path.html), 7 December 2023; Kery and Myers, [Exploring Exploratory Programming](https://dblp.org/rec/conf/vl/KeryM17.html), VL/HCC 2017; the Linux kernel, [AI Coding Assistants](https://docs.kernel.org/process/coding-assistants.html); Fedora Council, [policy proposal on AI-assisted contributions](https://communityblog.fedoraproject.org/council-policy-proposal-policy-on-ai-assisted-contributions/), 25 September 2025. Read on 16 October 2026. The HR conversation was mine, and the person is not named.

## Threads

Startups & strategyAgents & policy[This article as a graph →](graphs.md#explorer-coding)

### Builds on

- [The SaaS apocalypse will be decided by inertia, not by AI](saas-apocalypse-decided-by-inertia-not-by-ai.md) Incumbents and newcomers have the same AI; what separates them is how much past success each has to protect, so inertia decides which SaaS companies survive.
- [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](custom-uis-are-not-the-exception.md) Every message has a graph, so it can be shaped for the reader's moment; a custom interface per moment is now how interfaces get made, and each gets a policy.
- [The citizen developer is good news: the spreadsheet grown up, the best briefs ever written, and the handover from explorers to villagers and town planners that makes them last](the-citizen-developer.md) The citizen developer is the spreadsheet grown up: the best briefs ever written, handed to villagers and town planners, carried in versioned vaults.
- [Your own newsroom: how a founder can tell their story by voice memo, with an agent that checks it and publishes it to GitHub Pages, and readers who pay a little if they find it useful](your-own-newsroom.md) The recipe for a founder's own site: voice memos, an agent wired to GitHub that checks and publishes, GitHub Pages, and readers who pay a little.
- [If somebody built a company on code review: how I would do it, and why it is only now possible](if-somebody-built-a-company-on-code-review.md) A reader's seven questions answered as a company plan: one reader for every layer, review as a science, and the layers as the customer's own.
- [Agentic cost is an engineering problem: a business plan for a service that reads the logs a company already has and finds the money, then the engineering](agentic-cost-is-an-engineering-problem.md) A business plan: read the logs a company already has, draw each agent's footprint, twin and policy, and find the money first and the engineering second.
- [Software vendors should become villagers and town planners: let users explore on top of the product, sell them the maintenance of what they build, and use Firefox as the example of what happens if you don't](software-vendors-as-villagers.md) Users can now rebuild the part of a product they need; what stops them is maintenance. Vendors should sell that, as villagers and town planners.
- [A custom Firefox of my own: the full plan to build one with a governed agent hive, for the laptop and the iPad, and how Mozilla could sell me the part I do not want to do, which is keeping it working](a-custom-firefox-of-my-own.md) A full plan to build a custom Firefox for laptop and iPad with a governed agent hive, and why the part worth paying Mozilla for is keeping it working.

### Continued by

- [Villager services for explorer coders: the founders with ten years of checklists will build the apps, and the business is everything behind them, sold in finite packs, never as rent](villager-services-for-explorer-coders.md) Villager services for explorer coders: founders with ten years of checklists build the apps; we sell everything behind them in finite packs.
- [The Open Security Summit and its debt: how a summit that treated every participant as a presenter stalled on its own website, what the code shows, and why agents make it worth restarting](the-open-security-summit-and-its-debt.md) How technical debt stalled the Open Security Summit's website and follow-up, what the repositories show, and why agents make a restart worthwhile.
- [Programming, taught upside down: what Lockhart said about maths applies to code, the tools that got the loop right, and why explorer coding finally starts at the right end](programming-taught-upside-down.md) We teach programming the way Lockhart says we teach maths: concepts first. Explorer coding starts where the hook is.
- [v0.12 in numbers: 159 releases in eight days, 131 articles, 292,000 words, and what the data says about how an agent-run newsroom works](v0-12-in-numbers.md) v0.12 in numbers: 159 versions in eight days, 131 articles, 292,000 words, a graph for every article, and the mistakes the data shows.
- [The exit is when you sell control: why a founder should leave the day someone else is calling the shots, and why to negotiate that day at the start, the Mourinho clause](the-exit-is-when-you-sell-control.md) A founder's exit is the day someone else buys control, which can come long before the shares go. Leave then, and agree the terms at the start.
- [The no-server startup: a blueprint for products that run entirely in the browser, with no server and no database of yours, the user's own AI key, and a team of agents to build them](the-no-server-startup.md) A blueprint for products with no server and no database of yours: static files, the user's own AI key and storage, and agents to build them.
- [You are a developer, you just do not call it that: what every GenAI founder I know does all day, the sausage factory they never saw, and why the book may be called Generation ZX Founders](you-are-a-developer.md) Every GenAI founder I know is a developer and does not think so. They never saw the sausage factory. So the book may be Generation ZX Founders.
- [Generation Z Developers (AI edition): the 2018 book that said act like you are part of the company, what it got right, and a new edition for the people I want to help](generation-z-developers-again.md) My 2018 book for young developers, 60% done, its outlines since written here as articles, and an AI edition, dated October 2026, made first.
- [Act as the job you want: if you are looking for a job, you have time, so do the work in public, make it linkable, and let the people who want to help you help you](act-as-the-job-you-want.md) If you are looking for a job you have time: act as the person in the job you want, in public, and give the people who want to help you a link.
- [Hired for the workflow: why October 2026 is the moment to get into agentic work, why you are more technical than you think, and how the edge starts with the application](hired-for-the-workflow.md) October 2026 is the moment to get into agentic work: companies need AI operators, not model builders, and the edge starts with the application.
- [Ephemeral town planner services: a better name than serverless, now that serverless includes things that bill you by the hour](ephemeral-town-planner-services.md) Serverless meant scale to zero and pay per use; now it covers hourly bills. A better name: ephemeral town planner services, and a test for it.
- [A browser for one: an iPhone app that only reads my newsroom, why I am building it now, and why I will still pay someone to keep it working](a-browser-for-one.md) An iPhone app that only reads my newsroom: WebKit in the UK, a paid membership and a Mac to build it, one passkey test first, and someone else to maintain it.
- [The code you do not ship: why the future of software is removing functionality, and who gets paid to keep it small](the-code-you-do-not-ship.md) Code is a liability, the worst bugs sit in features nobody needed, and models make removing it safe. The minimal viable code path, and who maintains it.
- [Fix the page yourself: the bookmarklet trick from my security days, a page API every site should publish, and why the next user experience is the one the user customises, with six fixes running on this newsroom](fix-the-page-yourself.md) A bookmarklet from my security days, a page API every site should publish, and six fixes running on this newsroom: the next UX is the user's own.
- [Who will fix your mess? An answer to HBR's "deployment gap" from what this site has already published: explorers, villagers and town planners, a record of what the agents built, and open source so the answer never depends on one partner](who-will-fix-your-mess.md) HBR's deployment gap, answered from this site's articles: explorers, villagers and town planners, a record the agents keep, and open source.
- [GenAI in Portuguese, 2024: my OWASP Global AppSec talk in Lisbon, the first public demo of The Cyber Boardroom, slide by slide, with what two years of agents have confirmed and changed](portugal-2024-genai-in-portuguese.md) My 2024 OWASP talk in Lisbon: Portuguese as a programming language, provenance, graphs instead of RAG, and the first public demo of The Cyber Boardroom.
- [Hacking Portugal, 2016: my BSidesLisbon keynote and the book that stopped at 95%, slide by slide, with what holds ten years later and what a new edition needs](portugal-2016-hacking-portugal.md) Hacking Portugal, my 2016 BSidesLisbon keynote and the book at 95%: a Hacking Service, OpenSource.pt, a Ministry of Code, and what holds ten years on.
- [Software vendors should become villagers and town planners: let users explore on top of the product, sell them the maintenance of what they build, and use Firefox as the example of what happens if you don't](software-vendors-as-villagers.md) Users can now rebuild the part of a product they need; what stops them is maintenance. Vendors should sell that, as villagers and town planners.
- [A custom Firefox of my own: the full plan to build one with a governed agent hive, for the laptop and the iPad, and how Mozilla could sell me the part I do not want to do, which is keeping it working](a-custom-firefox-of-my-own.md) A full plan to build a custom Firefox for laptop and iPad with a governed agent hive, and why the part worth paying Mozilla for is keeping it working.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 144 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=144)

**Posting this article on LinkedIn?** The cover is [explorer-coding.jpg](banners/explorer-coding.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/explorer-coding.html)*
