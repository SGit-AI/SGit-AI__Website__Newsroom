# How a vault works: an encrypted store that acts like a database, where a server that is fully compromised leaks nothing, one mutable file lets every other object be cached for ever, and a web page can open a file in four requests or run a whole app in a sandbox, sgit.ai

> This is the key idea behind sgit's vaults, for a technical reader. The design principle was simple to say and hard to keep: everything is encrypted before it reaches the server, so that if the server had a catastrophic failure and someone had all of it, no confidential data would leak. The challenge that followed was how to make an encrypted store act like a database, the way Git is a database of objects in a graph, when the server cannot read any of it. The insight was a deterministic file: from the read key, a client computes the name of the one file that holds the head of the branch, an HMAC of the key over a fixed domain and the vault id. That file is the only mutable one. Decrypt it and you have the head commit; the commit gives the tree; the tree gives the file. Every other object is named by the hash of its own ciphertext and never changes, so a reader can verify it without a key and cache it for ever, and refreshing a whole site means re-reading one small file. Commits chain to their parents, so a swapped object is caught. On a web page, that gives two modes: read a file directly, in four requests, decrypted in the browser; or run a vault app in a sandboxed frame that can only ask the host for what it is allowed, through a small sg bridge, which is where behaviour policies come next.

*Source: <https://newsroom.sgit.ai/articles/how-a-vault-works.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / How a vault works: an encrypted store that acts like a database, where a server that is fully compromised leaks nothing, one mutable file lets every other object be cached for ever, and a web page can open a file in four requests or run a whole app in a sandbox

# How a vault works: an encrypted store that acts like a database, where a server that is fully compromised leaks nothing, one mutable file lets every other object be cached for ever, and a web page can open a file in four requests or run a whole app in a sandbox

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-03 · [article v1.0.0](versions/how-a-vault-works.md) · [newsroom v0.14.50](https://newsroom.sgit.ai/admin/versions.html) · sgitvaultsencryptionarchitecturecachingsandboxbehaviour-policiestechnicalarticle

***Abstract:** This is the key idea behind sgit's vaults, for a technical reader. The design principle was simple to say and hard to keep: everything is encrypted before it reaches the server, so that if the server had a catastrophic failure and someone had all of it, no confidential data would leak. The challenge that followed was how to make an encrypted store act like a database, the way Git is a database of objects in a graph, when the server cannot read any of it. The insight was a deterministic file: from the read key, a client computes the name of the one file that holds the head of the branch, an HMAC of the key over a fixed domain and the vault id. That file is the only mutable one. Decrypt it and you have the head commit; the commit gives the tree; the tree gives the file. Every other object is named by the hash of its own ciphertext and never changes, so a reader can verify it without a key and cache it for ever, and refreshing a whole site means re-reading one small file. Commits chain to their parents, so a swapped object is caught. On a web page, that gives two modes: read a file directly, in four requests, decrypted in the browser; or run a vault app in a sandboxed frame that can only ask the host for what it is allowed, through a small sg bridge, which is where behaviour policies come next.*

From a key to a file: one mutable file, named from the key, then objects that never change.

## In short

- **The principle:** if the server is fully compromised, nothing confidential leaks.
- **The challenge:** make an encrypted store act like a database the server cannot read.
- **The insight:** one file whose name the client computes from the read key, holding the head.
- **Everything else is immutable,** named by the hash of its ciphertext: verifiable without a key, cacheable for ever.
- **A file is four requests away,** decrypted in the browser.
- **Refreshing a whole site** means re-reading one small file.
- **Two ways onto a web page:** file by file, or an app in a sandboxed frame with a small bridge.
- **Behaviour policies are the next layer** for those apps.

## The principle

From the start, the rule for SG/Send and then sgit was that everything is encrypted on the client, before it reaches the server. Not most things: just about everything. The test I used was a catastrophe. If the server failed in the worst way, and someone had a copy of all of it, what would they learn? The answer had to be: nothing confidential. No file contents, no file names, no folder structure they could read, no way to tell which objects belong to which file.

That rule is easy to state for a file locker. It is much harder for something that has to behave like a database.

## Making it act like a database

Git is, underneath, a database: a graph of objects, where commits point to trees, trees point to files and other trees, and a branch is a pointer to a commit. It works because the server and the client can both read the objects and the pointers. Here the server can read neither. And there is one key, the vault key, that decrypts everything; from it comes the read key, which can read but not write, and which can be published.

So the question was: how does a client find anything, when the server cannot tell it where anything is?

## The deterministic file

The insight was to make one file's location computable from the key. In sgit's code, the client takes the read key and computes an HMAC-SHA256 over a fixed domain string, `sg-vault-v1:file-id:ref`, and the vault id; for a named branch, the branch name is part of the domain too. The first twelve hex characters become the file's name: `ref-pid-muw-` and the twelve characters. Anyone with the read key can compute it. Nobody without it can, and the name says nothing about what is inside.

That is the only file in the vault whose name is derived, and the only one that changes. Its prefix says so: `pid`, an id derived from the key, and `muw`, multi-writer, because many clients may update it and each update uses a compare-and-swap, a write that succeeds only if the file is still what the writer last saw.

Inside it, encrypted, is the id of the head commit. Every new commit overwrites it.

## The walk

From there, a client walks the graph like Git does:

1. **Compute the ref's name** from the read key, and fetch it. Decrypt it: the head commit's id.
2. **Fetch the commit.** It holds its parents, the id of the root tree, the message and, if signed, a signature.
3. **Fetch the tree.** It lists the files and folders at the root, with their names encrypted inside it, and each one's id.
4. **Fetch the file,** or, for a file in a subfolder, the subfolder's tree first, then the file.

Three or four small requests, every one a plain GET of a fixed name, and the file is decrypted in the browser with AES-256-GCM. The server answered requests for names it cannot interpret and returned bytes it cannot read. The [standard](sgit-is-a-standard.md) behind it means any storage that answers a GET can serve the read half.

## Immutable, and named by its content

Every object other than the ref is named `obj-cas-imm-` followed by the SHA-256 of its own ciphertext: `cas`, content-addressed, and `imm`, immutable. That naming does three jobs at once.

- **It can be verified without a key.** A reader recomputes the hash of the bytes it received and compares it with the name. sgit's code states it as an invariant: every such object "can be checked with no key and no trust in the host", because "its id IS sha256(ciphertext)". A reader never stores an object it has not verified.
- **It can be cached blindly.** An object with an `imm` name will never change, so any cache, a browser, a CDN, a disk, can keep it for ever without asking.
- **It makes history tamper-evident.** As in Git, each commit names its parents, and a commit can also carry a signature. Replace an object and its hash no longer matches its name; rewrite history and the chain no longer verifies.

The cost is efficiency: a changed file is a new object, not a difference against the old one. The gain is everything above.

## One file to refresh a whole site

This is what made it work on the web. A page can show a whole site from a vault, and to know whether anything changed, it re-reads one small file: the ref. If the ref has not changed, every object it already has is still right, because none of them can change. If it has, the page walks from the new commit and fetches only the objects it does not have.

So a documentation site can be built entirely from a vault: to update the site, update the vault, and the next visit picks it up. It is a better reading experience than Git gives you: getting one blob out of a Git server is possible, but not easy. Here it is four requests and a decryption.

## Two ways onto a web page

Two ways to put a vault on a page: read files directly, or run an app in a sandboxed frame.

**File by file.** The page walks to each file it needs, decrypts it, and renders it: markdown, images, data. That is how a reader vault or a documentation page works.

**As an app.** The vault contains an HTML app, and the page runs it full screen in a sandboxed frame. The frame has very little power: no key, no access to the vault itself, no storage of its own. It gets a channel to the host page, exposed inside the frame as `sg`: `sg.vfs.readText` to read a file, `sg.state` to keep a preference, `sg.llm.chat` to ask the vault's own model, and others. The host holds the key, decrypts, and checks every request against the permissions the app declared, which are denied by default. Images in the app are loaded from the vault by the host, and links in markdown navigate inside the vault, so pages work as you would expect.

I learned this pattern from looking at how others, Claude's artifacts among them, put untrusted code in a frame without giving it the page: isolate the code, and give it one narrow, checked channel.

## Next: behaviour policies for vault apps

The permission model was built before behaviour policies existed. It already is a small policy: what an app may read, write, and ask. The next step is to write it as one, so that it says not only what the app may call, but what the app is for, and which barrier holds each line, as [the teacher's vault](inside-english-with-ines.md) does for its tutor: the host sends it one lesson, and nothing else.

## What this does not claim

- **The details are from sgit-ai version 0.21.0's code,** read on 3 November 2026; formats are versioned and may change.
- **Object ids can be 12 or 32 hex characters** depending on the vault's format version.
- **The server still sees metadata:** how many objects there are, their sizes, and when they change.
- **The iframe bridge's API** is the SG/Send host's; its full reference is in that project's documentation.

## Where this comes from

My explanation of 3 November 2026, in this site's repository under `admin/notes/2026-11-03__how-a-vault-works/`. The sgit-ai package, version 0.21.0, on PyPI: `crypto/Vault__Crypto.py` (key derivation, file ids, object ids), `storage/Vault__Verified_Write.py`, `schemas/Schema__Object_Commit.py`, `safe_types/Enum__Cache_Mutability.py`. Earlier on this site: [sgit is a standard, not a server](sgit-is-a-standard.md).

## Threads

Vaults & methodSite & engineering[This article as a graph →](graphs.md#how-a-vault-works)

### Builds on

- [sgit is a standard, not a server: everything in a vault is one hash away, any storage can serve it, and the server is the least interesting part](sgit-is-a-standard.md) Git won as a standard, not a server. sgit is one too: every name computed from the key, a file four GETs away, any storage can serve it.
- [English with Inês, inside the vault: a teacher's site as a vault app, with an experiment for every lesson, cards that come back when you are about to forget, a tutor that answers about one lesson only, a concept map, and the back office with every agent's policy](inside-english-with-ines.md) English with Inês, a teacher's site as a vault app: experiments, spaced cards, a tutor bound to one lesson, a concept map and every agent's policy.

### Continued by

- [A sovereign website on a Raspberry Pi: the experiment of running the whole thing on one small box at home, a Raspberry Pi 5 with 16GB and 256GB, serving the site, checking the signature of every update, running a local model, building a website on the device itself under behaviour policies, and backing it up to a vault, step by step, what we will measure, and why this becomes a product when the Kickstarter finishes](a-sovereign-website-on-a-raspberry-pi.md) The experiment: a sovereign website, its local model, its build and its signed updates, all on one Raspberry Pi 5 at home.
- [Simple on top of years: why a startup has to find something very easy, very narrow and able to scale, why building from the bottom up, from provenance, understanding and determinism, ended in a simple product anyway, and how a website in five designs opened from a QR code sits on a CI pipeline, zero-knowledge sharing, sgit, vaults, keys and agentic teams, each learnt on its own](simple-on-top-of-years.md) Why a startup needs something very easy, and how a website opened from a QR code sits on years of layers learnt one at a time.
- [Your website, from a vault: how to show someone five versions of their own website without publishing anything, sealed in an encrypted sgit vault and opened with a QR code, a link or a zip on one drop page, the demo pipeline from a name to an email, and how a demo becomes their sovereign website without starting again](your-website-from-a-vault.md) Show someone five versions of their own website without publishing anything: sealed in a vault, opened with a QR code, a link or a zip.
- [Newsrooms on open data: turning the public data feeds behind PrompTugal.news and the Storm Charles site into one data site, a vault per source with an API and its provenance, then building small, focused newsrooms on top, for farmers, investors, the sea, fire, tourism and AI, each run by an agentic team, each a possible company, and why this is exactly where journalism comes in](newsrooms-on-open-data.md) Turning PrompTugal.news's public data feeds into one data site, then small focused newsrooms on top, each run by an agentic team.
- [Any data, with any data: why I am now comfortable saying we can connect any data source with any other, the nine steps from access to a vault, a key and a map on the other side, how each owner keeps control, where the person stays in charge, and why connecting two, five, fifty or a hundred datasets should be something an agentic cell sells](any-data-with-any-data.md) Why we can now connect any data source with any other: nine steps, owners keep control, a person approves every key, sold as cells.
- [Our companies and UTH: each company, technology and website we have built, mapped to what UAlgTec Heritage needs to build a European HeritageTech sector, from SGit's vaults and pki.sgit.ai's keys to SHarness, Agent Behaviour Policies, RiskMandate, AgentiCCells and its site factory, GAMMA-Ray, VoiceDebrief and PrompTugal.news, with what each could do for a heritage team, and why a sector needs companies like these](our-companies-and-uth.md) Each of our companies, technologies and websites mapped to what UAlgTec Heritage needs to build a European HeritageTech sector.
- [HeritageTech, together: how our open-source stack could plug into UAlgTec Heritage, the University of the Algarve's new European centre of excellence for heritage science and technology, mapped from the dig to the museum, with encrypted evidence vaults per site, signed finds, graphs of every excavation, agents with written policies, and what I would write in its "start a conversation" form](heritage-tech-together.md) How our open-source trust stack could plug into UAlgTec Heritage, the Algarve's new European centre for heritage science and technology.
- [Working with WizPress: how the AI operating system for newsrooms, built in Faro, and our open-source trust stack fit together, WizPress doing the production, from the inbox to the draft to the CMS, and our layer making every article carry its own proof, with an evidence vault per story, a behaviour policy per agent, a journalist's signature and signed responses, and a thirty-day pilot with one regional newsroom](working-with-wizpress.md) How WizPress, the AI operating system for newsrooms built in Faro, and our open-source trust stack fit: production plus proof, and a pilot.
- [Your own agentic cell, end to end: how a person asks for a site like the ones we made for Yiheng Wang and Silvio Switha, through a key pair in the browser, a vault they fill themselves and the site factory, with only three human gates, and then continues in their own Claude on their own repository](your-own-agentic-cell.md) How a person gets their own agentic cell: a key pair in the browser, a vault they fill themselves, the site factory, and then their own Claude.
- [Agents rating agents: GAMMA-Ray, the draft standard eight agents built at Web Summit to rate an AI agent on its freedom and its governance from public evidence, joining eight instruments into 21 questions, with a review workflow where no agent marks its own work, twenty company cards kept at direct links, and every card honestly marked Draft](agents-rating-agents.md) GAMMA-Ray: eight agents built a draft standard to rate AI agents on freedom and governance, with no agent marking its own work, and every card a Draft.
- [Relate, debriefed: what Neo4j's new agent-native graph database does, where its own documentation says it fits and where it does not, how it compares with the way we keep graphs, as plain JSON files in encrypted, versioned sgit vaults, and why the two could work together, with Relate as the throwaway engine inside our Load, Extract, Transform, Save cycle](relate-debriefed.md) A debrief of Neo4j's Relate, and how it compares with keeping graphs as JSON in encrypted, versioned sgit vaults, and why they fit together.
- [Five primitives, one store: a reply to Andy Goundry on Anthropic's always-on agents guide, why the inbox, timers, memory, permissions and outbox can share one versioned, signed store, how every AgentiCCells cell will ship with all five, and the levels we have added on top, all in public repositories](five-primitives-one-store.md) A reply to Andy Goundry: Anthropic's five always-on primitives can share one versioned, signed store, and every AgentiCCells cell ships with all five.
- [Fork it: making forking the way people adopt our cells and template sites, as GitHub made it the way people adopt code, with five ways to make a cell yours, what a fork-ready repository needs, paths from one repository to the next, a hub that lets usage decide what we build, and the brief for the team](fork-it.md) Forking as the way people adopt our cells: fork a template, point Claude at it, and it is yours. Five ways, fork-ready repositories, and a hub.
- [The cell is the unit: positioning AgentiCCells around small, focused cells, each with an objective, a deliverable and a behaviour policy, each with a page that sells it, a free recipe and three ways to get help, a catalogue that grows one need at a time, in each industry's own words, and why we should run our own work in cells first](the-cell-is-the-unit.md) The cell is the unit of AgentiCCells: one focused job with an objective, a deliverable and a behaviour policy, each with a page that sells it.
- [VoiceDebrief, relaunched: what the iPhone and iPad app already does, from recording without loss to an on-device transcript, a debrief and an encrypted vault, why the agent workflows move to the CRM app, and the list that takes it to the App Store properly, under its own name and its own accounts](voicedebrief-relaunch.md) VoiceDebrief is ready for market: record, transcribe and debrief on the device, save to a vault. A simpler relaunch, under its own name and accounts.
- [The email agentic cell: why connecting Gmail to agents the usual way is a security mess, and the architecture we will build instead, with one gateway agent that alone touches Gmail, a digital twin of the mailbox in a vault that people and agents work on together, signed proposals, approvals and even reads on append lanes, and behaviour policies at five altitudes](the-email-agentic-cell.md) Our own email connector: one gateway agent touches Gmail, everyone else works on a signed twin of the mailbox in a vault, with policies at five altitudes.
- [A CRM for us and for our agents: why the next stage is a CRM of our own, built on vaults with an iOS app, why we will build it by using it first for our own team and our own fleet of agents, how the open-source and agentic CRMs compare, and the two teams it needs, one that builds it and one that uses it](a-crm-for-us-and-our-agents.md) Our next stage is a CRM of our own, on vaults with an iOS app, for us and our agents. Twenty leads the field; agents propose, people send.
- [Odoo's agents can now write to the system of record: how our stack fits around Odoo, from version 12 to 20, with behaviour policies for Odoo agents, an Odoo cell, plan-then-apply through a vault, an ephemeral proof of concept that went from nothing to customised in under a minute on four versions, and why we use whatever version is on the other side](odoo-and-our-stack.md) Odoo's agents can write to the system of record. Our stack fits every Odoo from 12 to 20: a proof of concept ran on four versions in under a minute each.
- [Resilience when the workforce includes agents: what Synergy Six Degrees rates with OCRR, recovers with NeuShield and protects with Actifile, and where RiskMandate, sgit and SHarness meet it](resilience-when-the-workforce-includes-agents.md) What Synergy Six Degrees rates with OCRR and sells with NeuShield and Actifile, and the agent rows RiskMandate, SHarness and sgit add.
- [Would you pay to plug this newsroom in? A reply to Florent Daudens, on five publishers' bets for the AI era, from a newsroom built for agents, with what it answers, where it goes further, and the questions it has not answered either](would-you-pay-to-plug-this-newsroom-in.md) A reply to Florent Daudens on five publishers' AI bets: open to agents, paid at the source, vaults as the unit, and what is still open.
- [No tech stack to maintain: it is not that there is no backend, it is that the only code you own is HTML, CSS and JavaScript, with every other primitive rented as a commodity or run in the user's browser over encrypted vaults](no-tech-stack-to-maintain.md) Not no backend: no tech stack of your own. Only HTML, CSS and JavaScript; every other primitive rented or run in the browser over vaults.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 375 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=375)

**Posting this article on LinkedIn?** The cover is [how-a-vault-works.jpg](banners/how-a-vault-works.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/how-a-vault-works.html)*
