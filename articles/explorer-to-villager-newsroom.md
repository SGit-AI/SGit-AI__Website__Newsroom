# Go slow to go fast: moving the newsroom from an explorer project to a villager one, with the brief to do it, sgit.ai

> The newsroom's first MVP already has a crazy amount of powerful features, and it is live, and it is taking money. Like most explorer projects, it is also bundled in the middle of something much bigger: the application that bills, remembers and personalises sits in the same repository as 74 articles and their images. Measured on newsroom v0.8.0, the live reader code is about 2,700 lines, the tests that cover it are 433 and the one workflow never runs them, and the same application has two upstreams, with two diverging copies of the meter. I want to keep shipping a massive number of features without breaking anything, so this is the moment to take a step back and go slow to go fast. This article is the case for it and the brief: move every feature that is not content into its own repository that both sites consume, as a pure refactoring, with the same behaviour and the same bugs, checked by hashing the files the live site serves; map every file, capability and web control; build the safety net, with bugs and vulnerabilities written down as tests that pass; review it for security and quality, with every finding a GitHub issue; refactor until no change that alters what a reader sees or pays can slip through; and build a pipeline fast enough to run on every commit, in Node, in three browser engines, against a pre-production copy and with synthetic readers. Then the explorer returns, with the vault and the passkey.

*Source: <https://newsroom.sgit.ai/articles/explorer-to-villager-newsroom.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Go slow to go fast: moving the newsroom from an explorer project to a villager one, with the brief to do it

# Go slow to go fast: moving the newsroom from an explorer project to a villager one, with the brief to do it

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-11 · [article v1.2.0, 3 versions](versions/explorer-to-villager-newsroom.md) · [sgit.ai v0.7.56](https://sgit.ai/admin/versions.md) · engineeringexplorervillagerrefactoringtestingcisecurity-reviewcode-reviewnewsroomsg-metergithub-issuesbriefarticle

***Abstract:** The newsroom's first MVP already has a crazy amount of powerful features, and it is live, and it is taking money. Like most explorer projects, it is also bundled in the middle of something much bigger: the application that bills, remembers and personalises sits in the same repository as 74 articles and their images. Measured on newsroom v0.8.0, the live reader code is about 2,700 lines, the tests that cover it are 433 and the one workflow never runs them, and the same application has two upstreams, with two diverging copies of the meter. I want to keep shipping a massive number of features without breaking anything, so this is the moment to take a step back and go slow to go fast. This article is the case for it and the brief: move every feature that is not content into its own repository that both sites consume, as a pure refactoring, with the same behaviour and the same bugs, checked by hashing the files the live site serves; map every file, capability and web control; build the safety net, with bugs and vulnerabilities written down as tests that pass; review it for security and quality, with every finding a GitHub issue; refactor until no change that alters what a reader sees or pays can slip through; and build a pipeline fast enough to run on every commit, in Node, in three browser engines, against a pre-production copy and with synthetic readers. Then the explorer returns, with the vault and the passkey.*

What stays and what moves, measured on newsroom v0.8.0. The publication stays where it is; everything the reader does, the meter, the payments, the personas, the lists, the sharing, moves to a repository of its own, with its own engineering.

The newsroom's first MVP has a crazy amount of powerful features. A meter that charges by how far you read. Paying after you read, with a rating that sets the price. Real payments. Personas, a newsroom of your own, reading lists in a link, encrypted sharing. And it is live, and it is being charged for.

It is also, like most explorer projects, bundled in the middle of something much bigger. The application that bills, remembers and personalises lives in the same repository as 74 articles, their graphs, their images and the archive of everything the site has done. It grew there because that is where it was fastest to build. That was right for exploring. It is not right for what comes next.

I want to keep pushing a massive amount of features. The reader's own vault, sign-in with a passkey, packs for the reader's agent: all of it is designed and most of it is waiting. And I want to do it without breaking anything that people are paying for. So this is a perfect example of the moment when you take a step back and go slow, to go fast.

## In short

- **The newsroom is now a villager project.** It is live, it charges, and changes land on real readers. Explorer code is read for intent; villager code is read line by line, because that is where the blast radius lives.
- **Content and application get separate repositories.** Everything the reader does moves to its own repository, released as versioned files that the newsroom pins. The content stays.
- **The numbers are the reason.** About 2,700 lines of live reader code, 433 lines of tests that the one workflow never runs, two upstreams for the same code, and no Content-Security-Policy on any page.
- **First, a pure refactoring.** Same behaviour, same bugs. The proof is not a reviewed diff; it is the live site serving the same bytes before and after, by hash.
- **Six phases, and features wait until the fifth.** Map, move, test, review, refactor; then the explorer returns. Bugs and vulnerabilities found on the way become tests that pass, so fixing them later is a deliberate, visible change.
- **A pipeline fast enough to run on every commit.** Plain JavaScript and static files mean Node tests in seconds and three browser engines in about a minute; pre-production with a Stripe test link; synthetic readers; and a release that ends by checking the live site.
- **Reviews, by people and agents, and GitHub issues** for every finding, so the work is visible and nothing found is lost.

## Why now

In [If somebody built a company on code review](if-somebody-built-a-company-on-code-review.md) I put it this way: how carefully code is read depends on where it sits on the map. Explorer code is read for intent, mostly by agents. Villager code is read line by line, because that is where changes land and where the blast radius lives. Town planner code is read by deterministic checks.

The newsroom's reader features just crossed that line. A few days ago they were an experiment. Today a reader can pay £5 by card, and the meter decides what they spend. A mistake in the meter is a mistake with someone's money, and a mistake in the reading list parser is a mistake on a page that opens from an email in my name.

We have done this before. In March, the sgit command line went through the same transition, with [a brief that set out the phases](https://github.com/SGit-AI/SGit-AI__CLI/blob/main/team/humans/dinis_cruz/briefs/03/12/v0.13.30__brief__code-quality-explorer-villager.md): review without changing anything, build the test net, refactor with every test passing, and only then let the explorer build again. The command line has shipped release after release since then, with the safety net under it. The newsroom gets the same treatment, with one phase added at the start: the move.

The point is speed. Going slow now is what lets me keep going fast without the fear that each new feature breaks something a reader has paid for.

## What I measured

Counted in the newsroom repository at v0.8.0, on 11 October 2026:

| What | Size |
|---|---|
| SG Meter, the live version (v1.4.0): balance, pay by depth, rating, personas, your newsroom, top-up, share | 1,326 lines |
| Reading lists in a link, and the page that makes them | 706 lines |
| The component base, subscribe and the encrypted share | 235 lines |
| Build code for article numbers, lists and personas | 419 lines |
| Account and persona pages | 12 pages |
| Tests for the meter and the lists | 433 lines |
| Earlier meter versions, kept on their versioned paths | 5,016 lines in 10 files |
| GitHub workflows | 1: validate, tag, deploy. It runs the site validator on every push and pull request; it does not run the 433 lines of reader tests |
| Upstreams of the reader code | 2: the account pages, subscribe and the meter to v1.3.1 are imported from sgit.ai on every sync; the newsroom rewrites them to load its own fork, v1.4.0 |
| Pages with a Content-Security-Policy | 0 |

On this site's side, where the meter was first built and the newsroom's content still comes from, the page builder is a single file of 7,844 lines, about 240 of which touch the meter, personas or the account. That is the "bundled in the middle of a massive thing" in numbers. And there is a second kind of bundling: the newsroom's account pages, its subscribe file and the meter up to v1.3.1 are not the newsroom's own. Its sync script imports them from sgit.ai's built pages on every sync, then rewrites every page to load the newsroom's fork of the meter, v1.4.0, in place of sgit.ai's v1.3.1. Two repositories hold two diverging copies of the same application.

None of this is a criticism of the explorer work. It is what explorer code looks like, and it is why it was fast. It is also exactly what has to change before the next wave.

## The six phases

Six phases, from mapping to the explorer's return. Until phase five, no behaviour changes, not a feature and not a fix.

**0. Map.** Before anything moves, map all of it: every file, every capability, every web control (anything a reader can click, type or pay), every input, every place data leaves the browser, every external call and every secret or configuration value. As a table and as a graph, the way [code review as a fractal semantic graph](code-review-as-a-fractal-semantic-graph.md) does it, and the way secrets.sgit.ai's review pages map that project's claims to their evidence. No code changes. The map lives in the new repository and is regenerated every night.

**1. Move.** The reader code goes to its own repository, unchanged, and is released from there as versioned files on versioned paths, which is already how SG Meter is published. Both sites then consume those files: the newsroom pins a version, sgit.ai pins the same one, and the sync stops carrying the account pages, subscribe and the meter. The newsroom's v1.4.0 is the line that continues; sgit.ai's v1.3.1 is retired. The move is one copy-and-cut commit with no edits in it. The rule is strict: **the same behaviour and the same bugs**. The check is strict too: hash every file the live site serves for the reader features before the move and after it, the scripts, styles and JSON raw, and the HTML pages with the site chrome and version stamps normalised, which is exactly what the newsroom's own validator does today for imported pages. If one hash differs, the move is not finished.

The 5,016 lines of earlier meter versions are published artefacts, not code to maintain: they move, frozen, and the only test they ever get is that they are still served byte for byte.

**2. Test.** Only test code is written. Unit tests in Node for the money, the parsing and the state; browser tests in Chromium, WebKit and Firefox, on phone and desktop sizes; tests against a pre-production copy; and a synthetic reader run. No mocks: a test that needs a browser uses a browser, and a test that needs a vault uses a vault. **Bugs and vulnerabilities are written as tests that pass**, recording the current behaviour, so the fix later is a visible change to a test, not a silent one. One exception, because the repository is public: a test that records a vulnerability is a public description of it before the fix, so those tests and their issues live in a private vault until the fix lands, and move into the repository with it.

**3. Review.** Security and quality, by people and by agent reviewers, against the map. Findings, not fixes: every finding is a GitHub issue, labelled, with the test that shows it.

**4. Refactor.** Structure, names, duplication, boundaries, all with every test passing after every commit. And the adversarial exercise from the March brief: try to change what a reader sees or pays without a test failing. Every change that slips through is a missing test. Phase four is finished when none slips through.

**5. The explorer returns.** The fixes land, each as a deliberate change to the test that recorded the bug. Then the features that are waiting: [the reader's vault](i-miss-it.md), [the passkey that opens it](the-passkey-opens-the-vault.md), and [the pack for the reader's agent](brief-the-agent-too.md).

## The pipeline

Every commit, merge, release and night, with what runs at each and the time it should take. Slow checks run at night, not on the commit.

I want to see how fast and effective we can make this. The reader application is pure JavaScript and static files: no server to start, no database to seed, no container to build. That means most of it can be tested in Node in seconds and in real browsers in about a minute, and that is the target for every commit: **under two minutes**, lint, unit tests, three browser engines, and a build that produces the same bytes twice, which means the version and the date it stamps into pages come from a file, not from the clock.

On every merge, pre-production. GitHub Pages serves one site per repository, so the copy is a second site: either the newsroom's `main` branch, which its workflow already describes as a deploy test, published on a host name of its own, or a separate repository. Either way, a copy of the newsroom with the new version, a Stripe link in test mode that can never charge anyone, smoke tests of every reader page and every control, and a short synthetic reader run on a phone and a laptop. On every release: publish the versioned files, pin them in one commit, and ask the live site for its version and the hash of every reader file, because [green does not mean live](green-does-not-mean-live.md). Rolling back is pinning the previous version. And every night: the full synthetic reader study, the adversarial changes, dependency and header checks, and the map regenerated and compared with yesterday's.

Code review becomes part of the pipeline: a pull request needs one person and one agent reviewer before it merges. GitHub only counts a review from an account with write access, so the agent reviewer either has one, or posts its verdict as a status check that branch protection requires; the brief says which. I want to be reviewing these changes myself, and I want a set of agent reviewers alongside me, each with a written role, the way the newsroom's desk already works.

## The brief

*For the newsroom's sessions, and for whoever reviews their work. Written by the sgit.ai site session for Dinis Cruz, 11 October 2026. Dinis decides what ships.*

### What moves, and what stays

- **Moves:** SG Meter, every version, from both repositories, with v1.4.0 as the line that continues; the account pages; reading lists and the make page; persona links and their configuration; subscribe and the encrypted share; the build code for article numbers, lists and personas; and their tests. Next to arrive there: the reader's vault, passkey sign-in and the agent pack.
- **Changes on both sites:** the newsroom's sync stops importing the account pages, subscribe and the meter from sgit.ai; sgit.ai stops building them and pins the released files instead. After the move, neither site holds a copy of the reader code.
- **Stays:** the articles and everything generated from them, the front page, the desk, collections, the newsletter, World News Day, the archive and the content build.
- **The name:** `SGit-AI__Newsroom__API`, following the organisation's convention (`SGit-AI__Website__Newsroom`, `SGit-AI__CLI`). "API" is the honest word for what it owns: the contracts other sites and agents program against, SG Meter's configuration, the reading-list link grammar, `ids.json`, the persona link format, the device logs, the lane and key formats. One caveat, because "API" on this network also means the SG/Send server: the README's first line says it is a client-side API, components, formats and contracts the browser runs, with no server and nothing to deploy but files. And since sgit.ai will pin its releases, sgit.ai becomes a consumer of the newsroom's API, which reverses today's flow on purpose.

### Rules

1. **No behaviour changes until phase five.** Not a feature, not a fix, not a copy edit on a reader page.
2. **Same bytes served.** The move is proved by hashing every reader file on the live site before and after, not by reading the diff: scripts, styles and JSON raw; HTML pages with the site chrome and version stamps normalised, as the newsroom's validator already does.
3. **Bugs and vulnerabilities as passing tests.** Each one gets a test that records the current behaviour, and an issue that links to it. Vulnerability tests and their issues stay in a private vault until the fix lands.
4. **No mocks.** Real browsers, real vaults, a real pre-production copy, a Stripe link in test mode.
5. **Every finding is an issue.** In the new repository's GitHub issues, labelled by phase, area and severity, with its evidence.
6. **Every change is reviewed** by one person and one agent reviewer before it merges, the agent's review as a required status check.
7. **Releases are versioned and pinned.** The newsroom never loads an unversioned reader file; a rollback is one commit.

### Where the security review starts

From the measurement above and the newsroom's own [security model](https://newsroom.sgit.ai/meter/security.html), the review should at least cover:

- **No Content-Security-Policy.** No page sets one. A policy in a `meta` tag can limit scripts and connections, but it cannot set `frame-ancestors`, so protection against framing would need headers that GitHub Pages does not let us set. Decide whether the reader pages need a commodity layer in front that can.
- **Untrusted input in the URL.** The reading list fragment, persona links and the topped-up page's payment reference all come from a link. Each needs its parser tested against malformed and hostile input.
- **Money in the browser.** The balance, the receipts and the credit after a payment are in the reader's own storage by design, and the gaps that follow are accepted in the security model. The tests should prove the accepted gaps are the only ones: for example, that a payment reference is credited once.
- **What leaves the browser.** The share and the subscription encrypt to a published key and write to a lane. Test that nothing else leaves, on any page, with the browser's own record of requests, as the synthetic reader helper already does.
- **Third-party code.** Today the reader pages load none. Keep it that way, and make the build fail if one appears.

### Acceptance

| # | Done when |
|---|---|
| 1 | The map exists in the new repository: files, capabilities, web controls, inputs, outputs, external calls |
| 2 | The reader code is released from the new repository and pinned by both sites, the sync no longer carries it, and every reader file on the live site hashes the same as before the move (pages with chrome and version stamps normalised) |
| 3 | The commit pipeline runs in under two minutes: lint, Node tests, Chromium, WebKit and Firefox, and a reproducible build |
| 4 | Pre-production runs on every merge, on its own host name, with a Stripe test link, smoke tests and a short synthetic reader run |
| 5 | Every known bug and vulnerability is a passing test and an open issue |
| 6 | Every pull request has one person and one agent reviewer |
| 7 | No adversarial change to what a reader sees or pays slips through the tests |
| 8 | Only then: the fixes, and the vault, the passkey and the agent pack |

## What this does not claim

- **It is not a verdict on the code.** The explorer work is why the newsroom exists at all. This is the next phase of the same work, not a correction of it.
- **The numbers are lines, not quality.** 433 lines of tests could cover a lot or a little; phase two is where we find out which.
- **The timings are targets.** Under two minutes per commit is what the shape of the code allows; the pipeline has to prove it.

If you have taken a live product from explorer code to a villager codebase, and you have lessons to share, or you want to review this one with us, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine, recorded on 11 October 2026, asking for an article, a brief and then the execution of the move; written by this site's agent in the voice of this site. The argument and the editorial responsibility are mine. The measurements are from the newsroom's repository at v0.8.0 and this site's source on the same day. The phases adapt [the explorer-to-villager brief of 12 March 2026](https://github.com/SGit-AI/SGit-AI__CLI/blob/main/team/humans/dinis_cruz/briefs/03/12/v0.13.30__brief__code-quality-explorer-villager.md) from the sgit command line. Related: [If somebody built a company on code review](if-somebody-built-a-company-on-code-review.md), [Code review as a fractal semantic graph](code-review-as-a-fractal-semantic-graph.md), [Green does not mean live](green-does-not-mean-live.md), [How to run synthetic users](how-to-run-synthetic-users.md), [I miss it, so it is working](i-miss-it.md), [The passkey opens the vault](the-passkey-opens-the-vault.md) and [Brief the agent too](brief-the-agent-too.md).

## Threads

Site & engineeringStartups & strategy[This article as a graph →](graphs.md#explorer-to-villager-newsroom)

### Builds on

- [If somebody built a company on code review: how I would do it, and why it is only now possible](if-somebody-built-a-company-on-code-review.md) A reader's seven questions answered as a company plan: one reader for every layer, review as a science, and the layers as the customer's own.
- [Code review as a fractal semantic graph: source code is already one, and the review should read every layer of it](code-review-as-a-fractal-semantic-graph.md) Source code is layers within layers, each a graph with its own vocabulary; code review should read a change at every one, and a vault shows it done on real code.
- [I miss it, so it is working: the people who decide the roadmap have to use the product, and the vault the newsroom now needs](i-miss-it.md) I read the newsroom on four devices and they do not agree. Missing a feature is the best sign; the makers must use it. And the brief for the reader's vault.
- [The passkey opens the vault: a door per path, a master vault for every user, and no server of ours](the-passkey-opens-the-vault.md) Tested: a passkey's PRF bytes compute a door that holds the master's key, and a different path to the same passkey gives different bytes, so a door per path.
- [Brief the agent too: the people I talk to work with agents, so what I send has to reach both](brief-the-agent-too.md) The people I advise read through agents. Content needs a second package, a brief for their agent, and memory, so it reads what changed, not everything.
- [Green does not mean live](green-does-not-mean-live.md) Two releases passed every check and never reached the site because the checks stopped at the git remote; a release now ends by asking the live site its version.
- [How to run synthetic users on your own site: five people who do not exist, a browser, and an afternoon](how-to-run-synthetic-users.md) Five invented users, a model reading screenshots, and a real browser: how to run synthetic users, from three studies.

### Continued by

- [The citizen developer is good news: the spreadsheet grown up, the best briefs ever written, and the handover from explorers to villagers and town planners that makes them last](the-citizen-developer.md) The citizen developer is the spreadsheet grown up: the best briefs ever written, handed to villagers and town planners, carried in versioned vaults.
- [The human in the loop is a spectrum: how cheap it is to undo decides where a person belongs, and why the newsroom ships on its own while my email still waits for me](how-cheap-is-it-to-undo.md) How much to let an agent ship on its own depends on how cheap it is to undo and how mature the controls are, and both of those move.
- [Move the cloud, not the code: twins, sovereignty that works in practice, and the migration that pays for itself on the day you switch](move-the-cloud-not-the-code.md) Workloads stay on hyperscalers because moving means changing code; a twin lets the code not know, and the value in the twin is what signs the migration.
- [Places of highest leverage: where to focus when the agents can go in every direction, told with three days of real steps](places-of-highest-leverage.md) Where to focus when agents can go in every direction: the place of highest leverage, shown on three days of real steps, two walked back and one parked.
- [Agentic cost is an engineering problem: a business plan for a service that reads the logs a company already has and finds the money, then the engineering](agentic-cost-is-an-engineering-problem.md) A business plan: read the logs a company already has, draw each agent's footprint, twin and policy, and find the money first and the engineering second.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 78 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=78)

**Posting this article on LinkedIn?** The cover is [explorer-to-villager-newsroom.jpg](banners/explorer-to-villager-newsroom.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/explorer-to-villager-newsroom.html)*
