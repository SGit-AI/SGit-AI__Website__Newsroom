# No server, by design: first I retired the database, now I am retiring the back end, sgit.ai

> For years my rule has been not to use a database: the file system is the database, and the Load, Extract, Transform, Save pipeline (LETS) loads state, caches it and writes it back as files you can version, diff and read. The second step has been creeping up on me, and the newsroom made it explicit: retire the back end too. The SGit Newsroom is now a content site for several audiences, with personas, a reading meter, a payment on-ramp, a newsroom of your own, encrypted sharing and databases that run in the reader's browser, and none of its application logic runs on a server. What is left on the server side is commodity: static hosting, a vault server that stores only ciphertext, a payment link, DNS and a build pipeline, with a sign-in provider next. The design came from a constraint: the vault server cannot see anything, by design, so everything that needs to see has to happen in the browser. It also came from a security call: the gaps a server would close do not match this site's readers, and the article lists them, with what a server would cost to close each one. The result scales without its complexity scaling, ships fast (114 releases between 1 and 11 October), and lines up with the things I care about: sovereignty, privacy, explainability and determinism. The article maps the architecture, the evolution, the accepted gaps, and how far I think the pattern can be pushed.

*Source: <https://newsroom.sgit.ai/articles/no-server-by-design.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / No server, by design: first I retired the database, now I am retiring the back end

# No server, by design: first I retired the database, now I am retiring the back end

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-11 · [article v1.1.0, 2 versions](versions/no-server-by-design.md) · [sgit.ai v0.7.44](https://sgit.ai/admin/versions.md) · architectureclient-sideserverlessno-databaseletsfile-systemvaultsappend-lanesprivacysovereigntysecuritynewsroomsg-meterwardleyarticle

***Abstract:** For years my rule has been not to use a database: the file system is the database, and the Load, Extract, Transform, Save pipeline (LETS) loads state, caches it and writes it back as files you can version, diff and read. The second step has been creeping up on me, and the newsroom made it explicit: retire the back end too. The SGit Newsroom is now a content site for several audiences, with personas, a reading meter, a payment on-ramp, a newsroom of your own, encrypted sharing and databases that run in the reader's browser, and none of its application logic runs on a server. What is left on the server side is commodity: static hosting, a vault server that stores only ciphertext, a payment link, DNS and a build pipeline, with a sign-in provider next. The design came from a constraint: the vault server cannot see anything, by design, so everything that needs to see has to happen in the browser. It also came from a security call: the gaps a server would close do not match this site's readers, and the article lists them, with what a server would cost to close each one. The result scales without its complexity scaling, ships fast (114 releases between 1 and 11 October), and lines up with the things I care about: sovereignty, privacy, explainability and determinism. The article maps the architecture, the evolution, the accepted gaps, and how far I think the pattern can be pushed.*

The SGit Newsroom's architecture. Every piece of application logic runs in the reader's browser. Everything on the server side is a commodity product that holds no logic of ours, and the one that holds the reader's data cannot read it.

I have said for a long time that you do not need a database. The file system is a powerful database, and loading files, working on them and saving them back is simpler, cheaper and easier to reason about than running a database server. I still stand by that.

What I had not said out loud is the second step, which has been creeping up on me for months, in my constant focus on making things simple and removing variables until only the essential ones are left. More and more of what I build has no back end at all. The application is a set of files a browser downloads; the state lives in the browser or in an encrypted vault; and the servers involved are things I rent as products, not things I run. The newsroom, which in the last few days grew into a site with personas, a payment on-ramp and a private area for every reader, made the pattern explicit enough to write down.

And I think this is the next major pattern of my architecture. First I retired the database. Now I am retiring the back end. I look at everything through this lens now: why do I need that? Why do I need the Lambda function? Why do I need the EC2 instance? Why do I need the cost? This article is that pattern: where it came from, what the newsroom looks like when you draw it, why the security gaps it leaves are the right ones to leave, and how far I think it can be pushed.

## In short

- **Step one was retiring the database.** The file system is the database. The LETS pipeline (Load, Extract, Transform, Save) loads state, works on it, and saves every intermediate result as a file you can version, diff and read. Memory-FS and Issues-FS are libraries built on that idea.
- **Step two is retiring the back end.** The application moves to the browser. The SGit Newsroom has personas, a reading meter, a payment on-ramp, a newsroom of your own, encrypted sharing, article versions, and SQL and SPARQL databases, and none of it runs on a server.
- **This is not "no servers".** It is no servers of mine with logic in them. What is left is commodity: static hosting, a vault server that stores ciphertext in S3, a payment link, DNS and a build pipeline, with a sign-in provider next. Each is a product. None holds application logic.
- **A constraint designed it.** The vault server cannot read anything, by design, because vaults are encrypted in the client. So anything that needs to read the reader's data has to happen where the key is: in the browser.
- **Security made a business call possible.** The design leaves gaps, and they are written down: a reader can edit their own balance, start again in a private window, or credit themselves through an unprotected page. Every one of them changes a number only the cheater sees. Closing them would need a server, accounts and the complexity that comes with both. They do not match the threat, so they are accepted.
- **It scales without its complexity scaling.** The server side serves cached files and ciphertext. A hundred thousand readers add bandwidth, not moving parts.
- **It ships fast.** 114 releases of this site between 1 and 11 October; the reading meter went from an experiment to a working pay-on-demand design in seven releases in an afternoon. There is nothing to deploy but files.
- **It lines up with the rest.** Sovereignty (the reader holds the data and the keys), privacy (the server cannot read it), explainability (the whole application is files you can read), determinism (the same files give the same result).
- **The question now is how far it goes.** A table at the end lists what still seems to need a server, and which commodity, or which change of design, covers each.

## Step one: the file system is the database

The first step is old for me, and I have written about it under several names. The clearest is [LETS: Load, Extract, Transform, Save](https://docs.diniscruz.ai/2025/05/27/lets__load-extract-transform-save__a-deterministic-and-debuggable-data-pipeline_architecture.html), a paper from May 2025 that sets out the pattern as a deliberate change to ETL: every stage reads files and writes files, every intermediate state is kept, and the file system, or an object store, is treated as a first-class database. Its principles are ephemerality, traceability, determinism, modularity, and what it calls minimum viable propagation. The projects behind it, MyFeeds.ai, The Cyber Boardroom and a library called Memory-FS, all run on it.

The point is not that files are clever. It is that a database server is a large, stateful, always-on thing that you have to provision, secure, back up, migrate and pay for, whether or not anyone is using it, and most of the time what it holds would be perfectly happy as files. Load the state, work on it in memory, save it back: that is a cache, a database and an audit trail in one, and git gives it history for free. In effect, it is loading state and caching it, and that works very well. [Issues-FS](https://pypi.org/project/issues-fs/), which keeps issues as JSON files inside git repositories, with pluggable storage for memory, disk, S3, SQLite or a zip file, is the same idea applied to an issue tracker.

The newsroom took that one step further in September. [Databases with no server](https://newsroom.sgit.ai/databases/index.html) runs two real database engines, SQLite and a SPARQL store, compiled to WebAssembly, in the reader's browser, over the JSON files the Portugal section is built from. The build runs every example query and fails if one returns nothing. The database is the files; the engines are just readers.

## Step two: the back end goes too

The second step is what this article is about, and it came out of a constraint I did not set out to have.

Most of the state on this network now lives in [sgit vaults](where-the-vault-keys-live.md). A vault is encrypted in the client before it leaves; the server stores ciphertext in S3 and never sees a key. Read keys are derived one way, and can be published. Append lanes let anything write an entry with one POST, readable only by the vault's owner. Vaults reference vaults. All of that is storage, and good storage, with one property that changes the design of everything built on it: by design, the server side cannot see anything.

So a feature that needs to read the reader's data cannot run on the server. It has to run where the key is: in the browser. I did not choose a client-side architecture and then add encryption. Encryption came first, and the client-side architecture followed, because there was nowhere else for the logic to go. It is one of the clearest examples I have of a constraint doing the design work.

And once the logic is in the browser, the question changes. It stops being "where on the server should this go?" and becomes "why would this need a server at all?" Why a Lambda function? Why an EC2 instance? Why a database, a queue, a cache cluster, a deployment pipeline for the back end, an on-call rota? For most of what the newsroom does, there is no good answer.

How the pattern evolved: from removing the database, through files as the store of record and engines that read them in the browser, to removing the back end. Each step removed a moving part rather than adding one.

## What the newsroom is now

It is worth listing what the [SGit Newsroom](https://newsroom.sgit.ai/) does today, because the list is the argument. If you look at it as a pattern for a news organisation, it is, I would argue, remarkably powerful: a content site publishing for several audiences, where each reader can have a personalised experience and an area of their own, in a completely private way, with on-ramps for different payment models. The column on the right is where each part runs.

| What it does | How | Where it runs |
|---|---|---|
| Publishes for several audiences, with a markdown twin of every page for agents | A static build from markdown sources, with an index for agents | Built in CI, served as files |
| Lands a reader as someone: [a CISO as a CISO](a-link-to-a-persona.md) | Personas kept in a vault, opened with a published read key, followed or forked | Browser |
| Builds personas from what you read, several per reader | [Pay to keep your persona](pay-to-keep-your-persona.md): a graph you can watch grow | Browser |
| Charges by the share of a page you read, never blocks, lets you go below zero | [SG Meter](going-live-with-the-reading-meter.md), a library any site can add | Browser |
| Lets you say what a page was worth, and that sets its price | [Pay after you read](pay-after-you-read.md) | Browser |
| Takes money | A £5 Stripe payment link, no account, nothing renews; live since 11 October, a few hours after this article first said it was not set yet | A payment provider's hosted page |
| Gives every reader a newsroom of their own and a reading history | Kept in the browser's own storage | Browser |
| Sends your reading to us, if you choose, for a front page designed for you | Encrypted in the browser to a published public key, dropped into a write-only lane | Browser, then a vault lane |
| Takes newsletter sign-ups | The same encrypted, write-only inbox | Browser, then a vault lane |
| Shows how each article changed | Versions and diffs from git | Built in CI |
| Runs SQL and SPARQL over the site's own data | SQLite and Oxigraph compiled to WebAssembly | Browser |
| Signs you in (**next**) | Client-side OAuth with a provider | Browser and the provider |

There is no account database, no session store, no API server and no back end to deploy. The things that would normally need one, payments and identity, are rented from companies whose product they are: the payment page now, and sign-in next. And the next pieces are already shaped to fit: a model in the client, with the reader's own key, and a persona that follows the reader to their phone and their agent, through a vault only they can open.

## Not "no servers": commodity servers

I want to be precise about the claim, because "serverless" has come to mean several things. I am not saying there are no servers. Of course there are. GitHub Pages serves the files. A vault server stores the ciphertext. A payment provider takes the money. A sign-in provider will vouch for an identity. DNS points at all of it, and GitHub Actions builds it.

What there is not is a server of mine with application logic in it. Every one of those is a product, used as it comes out of the box, and from the point of view of the application each is a commodity: replaceable by another product that does the same thing. The vault server is the closest to custom, and even it is a generic store: in most cases the same design would work over read-only files in a storage bucket, with only the append lanes needing a small piece of server logic.

That is the Wardley-map view of it, which I used in [Every mistake added a rule](every-mistake-added-a-rule.md): complexity is a blob of custom-built components sitting where the world already has products and commodities. A back end is exactly that blob. Moving the application into the browser leaves the custom code in one place, written once and shipped as files, and everything around it on the commodity side of the map, where somebody else is paid to keep it running.

## It scales without the complexity scaling

The usual worry about client-side applications is that they do not scale. This is the opposite case. A back end's cost and complexity grow with its users: more instances, more database load, more caches, more failure modes. Here, a hundred thousand readers mean a hundred thousand browsers each doing their own work, against a server side that serves static files and ciphertext, both of which are cached at every layer, from the content delivery network to the browser itself. Vault content, fetched from git or from the vault server, can be cached locally too. The server side's work grows with bandwidth, which is the cheapest thing on the internet to buy. Its complexity does not grow at all.

And browsers are not what they were. They run WebAssembly databases, Python, cryptography, local storage measured in gigabytes and, increasingly, models. Every year, more of what used to need a server fits in the tab.

## Security as a business tool

This is the part I find most interesting, because it is where security experience changes the decision, rather than slowing it down. And there is an irony in it: I have spent my career in security, and that experience is exactly what lets me say, yes, let's deploy a system that has a bunch of security gaps, because the gaps do not match our audience.

A design with no server has security gaps, and the honest thing is to list them. [SG Meter's security model](https://newsroom.sgit.ai/meter/security.html) does that for the reading meter, and every gap in it is accepted:

The gaps a client-side design leaves, as SG Meter's security model lists them, and what a server would cost to close each one. Every gap changes a number only the person exploiting it can see. A server would close them, and bring accounts, a database, webhooks and a deployment with it.

- A reader can edit their balance in the browser's developer tools. It costs the site nothing it would otherwise have had.
- A reader can open a private window and start again at £5. They lose their history and their personas, which is what the meter is for.
- A reader can open the "topped up" page with an invented payment id and credit themselves £5. No money moves; the credit is a number on their own screen.
- A reader can clear their data to wipe a negative balance. There was never a debt.
- Agents read the markdown twins unmetered, by design, for now.

Each of these would be closed by a server: hold the balance server-side, require an account, verify the payment with a webhook from the payment provider to an endpoint you run. And each of those would bring back the thing I have spent years removing: a database of accounts, a server to run it on, a deployment, a store of personal data to protect, and a sign-up wall between the reader and the page. The meter's security model says it plainly: the topped-up page is unprotected because protecting it would need a server, and the one thing that server would protect is a number on the reader's own screen that unlocks nothing.

That is a security judgement, and I think it is the right one. The question in [Who are you protecting against?](who-are-you-protecting-against.md) is the right question here: the site's readers are not an adversary trying to steal reading, because nothing is behind a wall. What is protected is narrower, and it is protected well: the reader's own history, from other people. It never leaves their browser unless they send it, and then only encrypted to a key we publish. A bigger back end would have made the site more secure against threats it does not face, and less useful, less private and slower to change for the readers it has. The advantages of a more robust server side are far outweighed by the complexity, the deployment and the over-engineering it would bring. The meter's model also says what would change the call: if the balance ever unlocked something, the gaps would stop being acceptable, and that feature would get a signed receipt or a server, and not before.

There is a second half to this, which we only saw this week. When we ran [five synthetic readers](how-to-run-synthetic-users.md) through the newsroom, none of them found a security problem. What they found was the same design seen from the reader's side: "credit can go below zero" reads as a debt to someone worried about money, and a top-up page that says the cart is simulated, while asking for money, leaves a careful reader unsure whether anything real would happen. The gaps are accepted for good security reasons; their cost lands in the words on the page, and that is where we are fixing them.

The business value is the inverse of the usual one. We are not going to push readers into accounts to protect a number. We are going to make the site so useful, and so valuable, that they choose to pay, and choose to keep a vault.

## Why it is easy to throw technology away

There is a reason I can keep removing pieces. When everything I build is open source, I do not have a moat I have to keep using. There is no part of the stack I built that I need to protect from being replaced, and I am usually the first one to try to replace it when something better appears. I wrote Memory-FS, and if the browser and a vault do its job for an application, the application stops using it. The meter's first version was written this week, and it has already been rewritten into a library. The habit is to ask of every component whether it is still earning its place, and open source removes the one bad reason to say yes: that I built it.

## It ships fast

Look at the amount of features we pushed in the last few days. Between 1 and 11 October, this site shipped 114 releases ([the counts by day](data/no-server-by-design__releases.json)), 18 or 19 on the busiest days, alongside the newsroom moving to its own domain. The reading meter went from an experiment to a working pay-on-demand design [in seven releases, in three hours and forty minutes](pay-after-you-read.md), alongside seven other pieces of work: a meter, paying by depth, personas, versions, sharing your reading, and a rating that sets the price.

Releases of sgit.ai per day, 1 to 11 October 2026, from the git log: 114 in eleven days. With no back end, a release is a set of files; there is no migration, no deployment of a server and nothing to roll back but a commit.

That speed is not heroics. A release is a set of files. There is no schema migration, no server to deploy, no compatibility window between an old back end and a new front end, and rolling back is a commit. Every layer underneath, from sgit in March to the newsroom pipeline in September, became boring enough to build on, and the client-side design is what lets the next feature land on top of it in an afternoon.

Speed has a cost, and it is worth being honest about it. When the newsroom moved to its own domain, 51 of the 527 figures in its articles did not come with it. Nothing failed in a way a server would have noticed: the pages were files, and they served. The synthetic readers found it, because one of them was reading a page where a picture should have been. Files make releases cheap; they also make it easy to ship something incomplete, which is why every release here ends by checking what is actually live.

## Sovereignty, privacy, explainability, determinism

This design pattern completely ties in with the ideas I keep coming back to, and I do not think that is a coincidence.

- **Sovereignty.** The reader's data is in the reader's browser, and when it moves, it moves into a vault whose key the reader holds. The site could disappear, and the reader would keep everything they had.
- **Privacy.** Not as a policy, but as a property: the server cannot read what it does not have, and the vault server cannot read what it stores.
- **Explainability.** The whole application is files. Anyone can read what it does, the markdown twin of every page says what the page says, and the version history says what changed and when.
- **Determinism.** The same files give the same result. The build runs every query it publishes; a release is a hash.

This is close to what the [local-first software](https://www.inkandswitch.com/local-first/) movement argued for in 2019: that you should own your data, in spite of the cloud. What the vaults add is the piece that makes it practical for a publication: shared, persistent storage that the operator cannot read, so that "client-side" does not have to mean "single-device".

## How far can it be pushed?

That is the question I want to keep asking. Here is my current list of what still seems to need a server, and what covers each without one of mine.

| What seems to need a server | What covers it |
|---|---|
| Knowing a payment really happened, when the balance unlocks something | A signed receipt from the payment provider, verified in the browser, or a tiny verification function as a commodity |
| Identity | Client-side OAuth with a provider; passkeys unlocking a vault key |
| The same persona on the phone, the laptop and the agent | A vault only the reader can open |
| Readers writing to us | Write-only append lanes, encrypted to a published key |
| Models | In the client, with the reader's own key, or a small local model |
| Search over the site | A static index the browser loads, or the graph the five readers build |
| Rate limits and abuse | The commodity layer in front of the static host |
| Things that must be secret from the reader | The one real limit: anything the reader must not hold cannot live in the reader's browser |

The last row is the honest boundary. A secret that must be kept from the person using the application, such as a shared API key, or a price that must not be editable because it unlocks something, cannot live in the browser. For each of those, the choice is between a signed artefact the browser can verify and a small, commodity function. For everything else, I keep finding that the browser and a vault are enough.

## What this does not claim

- **Not that servers are bad.** Some applications need shared, live, authoritative state: a trading system, a multiplayer game, a bank's ledger. This pattern is for applications where each user's state is theirs.
- **Not that the gaps are free.** They are accepted because of who reads this site, and what the meter protects. A different site, with a different threat, would make a different call, and the security model says what would change ours.
- **Not that it is finished.** Sign-in, cross-device personas, a model in the client and signed receipts are next, not done.

## What comes next

1. **A model in the client,** with the reader's own key, so the newsroom can answer questions about what it publishes without a back end of ours.
2. **Personas that follow the reader** to every device, and to their agent, through a vault only the reader can open.
3. **A signed receipt** for payments, so that a balance could one day unlock something without a server holding it.
4. **The pattern as a template:** the newsroom's architecture packaged so that another publication, or any content site, can start from it.

First the database went, and the work got simpler. Now the back end is going, and the work is getting faster. I do not know yet where the pattern stops, which is exactly why it is worth pushing. If you are building something where each user's data should be theirs, and you want to see how far it goes without a back end, let's talk: [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

Two voice memos of mine. I asked an agent in a separate Claude session to turn them into this article, with its figures and data, and to check every feature against the newsroom's and this site's own pages and repositories; this site's agent then rewrote it in the voice of this site, checked two things the draft could not confirm, and corrected them: the payment link was not set yet (the live top-up page was still the simulated cart; it went live later the same day, and the article now says so), and client-side sign-in is next, not shipped. The argument is mine, and so is the editorial responsibility. The release counts are from this site's git log as of 11 October 2026, counted before this release; the accepted gaps are SG Meter's security model, paraphrased. Sources: [LETS (Load, Extract, Transform, Save): a deterministic and debuggable data pipeline architecture](https://docs.diniscruz.ai/2025/05/27/lets__load-extract-transform-save__a-deterministic-and-debuggable-data-pipeline_architecture.html), May 2025; [Issues-FS](https://pypi.org/project/issues-fs/) on PyPI; on the newsroom, [Databases with no server](https://newsroom.sgit.ai/databases/index.html), [SG Meter's security model](https://newsroom.sgit.ai/meter/security.html) and [the newsroom](https://newsroom.sgit.ai/); on this site, [Where the vault keys live](where-the-vault-keys-live.md), [Encrypted memory for agents that run somewhere else](encrypted-memory-for-isolated-agents.md), [A link to a persona](a-link-to-a-persona.md), [Pay to keep your persona](pay-to-keep-your-persona.md), [Going live with the reading meter](going-live-with-the-reading-meter.md), [Pay after you read](pay-after-you-read.md), [Who are you protecting against?](who-are-you-protecting-against.md), [Every mistake added a rule](every-mistake-added-a-rule.md), [How to run synthetic users](how-to-run-synthetic-users.md) and [A chat box on a site with no server](chat-on-a-static-site.md); and Martin Kleppmann, Adam Wiggins, Peter van Hardenberg and Mark McGranaghan, [Local-first software: you own your data, in spite of the cloud](https://www.inkandswitch.com/local-first/), Ink & Switch, 2019.

## Threads

Site & engineeringVaults & method[This article as a graph →](graphs.md#no-server-by-design)

### Builds on

- [Where the vault keys live: key management at sgit-ai v0.20.0, and what comes next](where-the-vault-keys-live.md) Vault key management at sgit-ai v0.20.0: the one secret, where keys are kept, how they travel sealed on append lanes, and what comes next.
- [A link to a persona: send people to the newsroom as someone, not as nobody](a-link-to-a-persona.md) Send a CISO to the newsroom as a CISO: personas kept in a vault by the newsroom's agents, opened from a link, followed or forked.
- [Pay to keep your persona: readers should pay because it helps them, not because they feel they should](pay-to-keep-your-persona.md) Readers should pay because it helps them: a persona with a name and a graph, several for focus, and one that follows you between devices.
- [Going live with the reading meter: pay for what you read, go below zero if you like, and the numbers we will check in eight weeks](going-live-with-the-reading-meter.md) Pay for the share of a page you read, go below zero with no nagging, top up £5 on Stripe: the plan, and the numbers we check in eight weeks.
- [Pay after you read: how a reading meter became a working business model in one afternoon, one release at a time](pay-after-you-read.md) Seven releases in one afternoon turned the reading meter into a working model: pay after you read, and the rating sets the price.
- [Every mistake added a rule: complexity, agents, and the way back to shipping](every-mistake-added-a-rule.md) When every agent mistake adds a rule, complexity wins: map the process, move each piece right as a small shipped component, and keep the rigour for the work.
- [Who are you protecting against? Draw the security line where the attacker is, not above it](who-are-you-protecting-against.md) Before deciding how secure to be, name the attacker: a six-tier ladder, an air-gapped Mac mini read against it, and eight startups drawing their line.
- [How to run synthetic users on your own site: five people who do not exist, a browser, and an afternoon](how-to-run-synthetic-users.md) Five invented users, a model reading screenshots, and a real browser: how to run synthetic users, from three studies.
- [Encrypted memory for agents that run somewhere else: sgit deployment patterns, from a Mac mini to Kubernetes](encrypted-memory-for-isolated-agents.md) Agents in isolated, ephemeral places need memory that outlives them. Five sgit deployment patterns, from a Mac mini to Kubernetes, with ciphertext-only servers.
- [A chat box on a site with no server, the plan, and the trade it makes](chat-on-a-static-site.md) sgit.ai has no server, so its directory chat runs a local matcher by default, takes your own key as an opt-in, and leaves the vault bridge unbuilt.

### Continued by

- [From sending a file to sgit: eight months of SG/Send, told by its own briefs and commits, and how a file-sharing service became encrypted version control and vaults](from-send-to-sgit.md) Eight months of SG/Send, checked against its own briefs and commits: how file sharing became sgit and vaults, the pace, and what the market said.
- [Judo for small countries: where Portugal, Romania and Estonia can add the most value in AI, and why the race for GPUs is not it](judo-for-small-countries.md) A small country should not race for GPUs: the opportunity is the plumbing its talent stands on, built once as open infrastructure, with small models.
- [The key is the billing system: VoiceDebrief, a product with no server, the one thing it cannot sell, and who could let it](the-key-is-the-billing-system.md) VoiceDebrief runs with no server on the user's own key; the one thing it cannot sell is a capped key, and this maps who could allow it and what to ask them.
- [The vault is live: from a design on 11 October to a reader's vault on newsroom.sgit.ai by two in the morning, and how all of it fits together](the-vault-is-live.md) The reader's vault runs on newsroom.sgit.ai: a passkey opens three real vaults, each device writes one file, and the architecture is drawn as it stands.
- [Two agents, one vault: the Industry Wire is written into an encrypted vault by one agent and drawn by newsroom.sgit.ai, which holds only the read key](two-agents-one-vault.md) One agent writes the Industry Wire into an encrypted vault; newsroom.sgit.ai holds only the read key and draws it, so a commit reaches the page with no release.
- [The article remains a product: Jonathan Palmer's four outputs for a newsroom with no human readers, checked against one that runs](the-article-remains-a-product.md) Jonathan Palmer's four outputs for a newsroom with no human readers, quoted line by line and checked against newsroom.sgit.ai as it runs, screenshots included.
- [The passkey opens the vault: a door per path, a master vault for every user, and no server of ours](the-passkey-opens-the-vault.md) Tested: a passkey's PRF bytes compute a door that holds the master's key, and a different path to the same passkey gives different bytes, so a door per path.
- [I miss it, so it is working: the people who decide the roadmap have to use the product, and the vault the newsroom now needs](i-miss-it.md) I read the newsroom on four devices and they do not agree. Missing a feature is the best sign; the makers must use it. And the brief for the reader's vault.
- [From me to you, in a link: a personal reading list, two briefs to build and use it, and the loop that makes it a day's work](a-reading-list-in-a-link.md) A reading list from one person to another, in a link the server never sees; a brief to build it, a brief to use it, and the loop that ships it in a day.
- [A model in the tab: Chrome now ships an LLM to capable desktops, and it is the hardest piece of the client-side puzzle](a-model-in-the-tab.md) Chrome now ships a language model any page can prompt, offline, on capable desktops. The last piece of the client-side puzzle, with rough edges.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 72 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=72)

**Posting this article on LinkedIn?** The cover is [no-server-by-design.jpg](banners/no-server-by-design.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/no-server-by-design.html)*
