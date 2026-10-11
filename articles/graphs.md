# The articles as graphs, sgit.ai

> Every article on sgit.ai as a semantic graph: the ideas it rests on, the claims it makes, and how they connect, plus a map of how the articles link to each other.

*Source: <https://newsroom.sgit.ai/articles/graphs.html> · sgit.ai v0.7.51 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Graphs

# The articles as graphs

Every article here has a semantic graph beside it: the ideas it rests on, the claims it makes, the methods and the examples, and how they connect. The map first, then one graph per article. Hover a node for its summary and an edge for its relation.

The graphs are data first and pictures second. Take them as JSON: [all articles in one file](graphs.json), with the topics, the teasers and the links between articles resolved, or one file per article at `articles/graphs/<slug>.json` (for example [this one](graphs/footprint-and-blast-radius.json)). The pages on this site are rendered from the same files at build time; nothing here is hand-written HTML.

74 of 74 articles have a graph. The map draws every article in date order round the circle, oldest at the top and clockwise from there, sized by how many other articles link to it. Teal edges run from an article to an earlier one it cites; amber edges run the other way, from an older article that was updated to point at a newer one. Thicker edges are articles that mention each other more than once.

## How the articles connect

*[diagram]*

74 articles, 349 links between them (577 mentions in all). 65 articles cite an earlier one; 10 links in amber run from an older article to a newer one, which means the older page was updated after the newer one existed. Most linked: [Fractal Semantic Graphs](#introducing-fractal-semantic-graphs) (21 articles link to it). Most linking: [The Mandate Stack](#the-mandate-stack) (20 links out). 0 articles not yet linked either way.

## [From me to you, in a link: a personal reading list, two briefs to build and use it, and the loop that makes it a day's work](a-reading-list-in-a-link.md)

2026-10-11 · Site & engineeringStartups & strategy

A personal reading list in a URL fragment (from, to, article numbers to read, to look at, and to follow) that opens on the newsroom as a persona the reader can keep or remove, with a stable public number for every article and a page to make a list for anyone. Two briefs: the newsroom builds it with validation, tests and no tracking; the RiskMandate agent, which keeps the contacts, chooses the person with Dinis, researches public sources, picks articles with reasons, tests the link, drafts the email, and Dinis sends it. The core is the loop: editorial, product, engineering, sales and the founder connected by written briefs, small contracts, owned repositories and tests, closing in about a day, as it did this week, with costs that are written down: drift, budgets and one person as the router.

*[diagram]*
**concept**claim**method**example

**10 nodes, 9 edges**

- **A reading list in a link** (method) Names and article numbers in the fragment; the server never sees them.
- **A number for every article** (concept) Assigned once, never changed or reused: the contract for links.
- **The list becomes a persona** (method) Added as a visitor, kept or removed in one tap.
- **Anyone can make a list** (claim) Curating for someone else becomes a link, and a business model.
- **The RiskMandate agent uses it** (method) Choose, research, pick with reasons, test, draft; Dinis sends.
- **Nothing tracks the reader** (claim) No opens counted; the conversation starts with a reply.
- **The loop** (concept) Five parts of a company connected by written briefs, closing in about a day.
- **This week's loops** (example) Personas by link 17 hours after the brief; three articles corrected 32 minutes after payments went live.
- **What the loop costs** (claim) Drift between parts, session budgets, and one person as the router.
- **Vibe coding with a slow loop** (concept) Product owners always described software; the loop was the bottleneck.

> The loop is fast because those costs are written down, not because they are gone. The honest version of the claim.

> An article number that never changes is a contract. Why two parts can move independently.

builds on [Pay to keep your persona: readers should pay because it helps them, not because they feel they should](#pay-to-keep-your-persona), [A link to a persona: send people to the newsroom as someone, not as nobody](#a-link-to-a-persona), [No server, by design: first I retired the database, now I am retiring the back end](#no-server-by-design), [RFC 0001: two ways to add public-key cryptography to sgit, and the questions we want you to answer](#rfc-0001-public-key-cryptography-for-sgit), [How to run synthetic users on your own site: five people who do not exist, a browser, and an afternoon](#how-to-run-synthetic-users), [A second reader the agent cannot skip: how two wrong emails became a gate on every draft](#a-second-reader-the-agent-cannot-skip), [The SaaS apocalypse will be decided by inertia, not by AI](#saas-apocalypse-decided-by-inertia-not-by-ai), [The same argument, in our words: Satya Nadella on models as insider risks, translated into the language of RiskMandate](#the-same-argument-in-our-words).

## [A model in the tab: Chrome now ships an LLM to capable desktops, and it is the hardest piece of the client-side puzzle](a-model-in-the-tab.md)

2026-10-11 · Site & engineeringGraphs & knowledge

Since Chrome 148 any page can prompt Gemini Nano on the reader's device, which supplies the hardest missing piece of the client-side pattern; the rough first run is mostly fixable by the page, the scarcity of examples has real causes, the standards objections are serious, and the way to build on it without being captured is to keep the meaning in anchored graphs and use the model as a checkable function.

*[diagram]*
**concept**claim**method**artefact**example**question

**10 nodes, 10 edges**

- **The Prompt API, stable in Chrome 148** (artefact) Gemini Nano on the device: text, image and audio in, text or JSON out.
- **The last piece of the client-side puzzle** (claim) Intelligence was what kept a back end in the picture.
- **The download never stopped** (example) The page lost the progress bar on refresh; the download carried on.
- **Why there are so few examples** (claim) New, gated hardware, a 4 GB first run, five languages, no native tools, contested.
- **The case against** (concept) Prompts do not travel; a vendor policy in front of a web API; the browser decides the model.
- **Keep the meaning in the data** (method) Anchored graph slices and narrow schema-constrained questions make the model replaceable.
- **Graph answers fit a small window** (claim) A 2,600-token anchored slice fits; the prose does not.
- **A download panel that tells the truth** (method) Bytes, rate, time left, survives a refresh, explains unavailable.
- **Ask this article, personas, voice memos** (example) The first uses: grounded answers, local personas, on-device transcription.
- **What is fast enough, on which machines?** (question) Speed, context window and accuracy are unmeasured; the vault will measure them.

> Keep the meaning in the data, not in the prompt. How to build on one vendor's model without being captured by it.

> The page should be complete without the model, and better with it. The design rule for a gated, contested capability.

builds on [No server, by design: first I retired the database, now I am retiring the back end](#no-server-by-design), [The agent is the reader: why agents will pay for graphs, personas and signed claims, because it is cheaper than not paying](#the-agent-is-the-reader), [Pay to keep your persona: readers should pay because it helps them, not because they feel they should](#pay-to-keep-your-persona), [How to run synthetic users on your own site: five people who do not exist, a browser, and an afternoon](#how-to-run-synthetic-users).

## [No server, by design: first I retired the database, now I am retiring the back end](no-server-by-design.md)

2026-10-11 · Site & engineeringVaults & method

After replacing the database with the file system (LETS), the next step is removing the back end: encrypted vaults make the server blind, so the application moves to the browser, leaving only commodity products on the server side; the security gaps this leaves are written down and accepted because they do not match the threat, and the result scales without its complexity scaling and ships as files.

*[diagram]*
**concept**claim**method**example**question

**10 nodes, 11 edges**

- **The file system is the database** (method) LETS: load, extract, transform, save; every state a file you can version and read.
- **No back end** (claim) All application logic runs in the reader's browser.
- **A blind server** (concept) Vaults are encrypted in the client, so anything that reads data must run where the key is.
- **Commodity servers, not no servers** (claim) Static hosting, a ciphertext store, a payment link, DNS and CI, with a sign-in provider next, all products.
- **The SGit Newsroom** (example) Personas, a reading meter, a payment on-ramp, a newsroom of your own, encrypted sharing, in-browser databases.
- **Gaps written down and accepted** (method) SG Meter's security model: every cheat changes a number only the cheater sees.
- **Scales without complexity scaling** (claim) More readers add bandwidth against cached files, not moving parts.
- **A release is a set of files** (example) 114 releases in eleven days; the meter in seven releases in an afternoon.
- **Sovereignty, privacy, explainability, determinism** (concept) The pattern's properties, not its policies.
- **How far can it be pushed?** (question) Secrets the reader must not hold are the honest boundary.

> Encryption came first, and the client-side architecture followed, because there was nowhere else for the logic to go. The constraint that designed it.

> First the database went, and the work got simpler. Now the back end is going, and the work is getting faster. The pattern in two sentences.

builds on [Where the vault keys live: key management at sgit-ai v0.20.0, and what comes next](#where-the-vault-keys-live), [A link to a persona: send people to the newsroom as someone, not as nobody](#a-link-to-a-persona), [Pay to keep your persona: readers should pay because it helps them, not because they feel they should](#pay-to-keep-your-persona), [Going live with the reading meter: pay for what you read, go below zero if you like, and the numbers we will check in eight weeks](#going-live-with-the-reading-meter), [Pay after you read: how a reading meter became a working business model in one afternoon, one release at a time](#pay-after-you-read), [Every mistake added a rule: complexity, agents, and the way back to shipping](#every-mistake-added-a-rule), [Who are you protecting against? Draw the security line where the attacker is, not above it](#who-are-you-protecting-against), [How to run synthetic users on your own site: five people who do not exist, a browser, and an afternoon](#how-to-run-synthetic-users), [Encrypted memory for agents that run somewhere else: sgit deployment patterns, from a Mac mini to Kubernetes](#encrypted-memory-for-isolated-agents), [A chat box on a site with no server, the plan, and the trade it makes](#chat-on-a-static-site); continued by [From me to you, in a link: a personal reading list, two briefs to build and use it, and the loop that makes it a day's work](#a-reading-list-in-a-link), [A model in the tab: Chrome now ships an LLM to capable desktops, and it is the hardest piece of the client-side puzzle](#a-model-in-the-tab).

## [The agent is the reader: why agents will pay for graphs, personas and signed claims, because it is cheaper than not paying](the-agent-is-the-reader.md)

2026-10-11 · News & evidenceStartups & strategy

When agents are the readers, a publisher that serves curated meaning, an anchored graph fitted to the agent's persona and objective, and claims signed with an expiry saves the agent more tokens than it charges, so the agent pays not to pay; measured on five articles the graph answers in 90% fewer tokens, and on 70 articles compression with scale appears only where a Cartographer curates, which is the work worth paying for.

*[diagram]*
**concept**claim**method**example**question

**10 nodes, 11 edges**

- **The graph is bigger than the text** (example) The full catalogue is 2.8 times the articles; the concept index is 7%.
- **A question costs 90% less in the graph** (claim) Median 2,579 tokens against 25,698, across all 45 concepts, with anchors.
- **Making the map is the verification** (example) 32 flags, 37 corrections, one systematic catch; the cost per finding rises on the third pass.
- **Compression with scale needs curation** (claim) 908 of 928 uncurated labels unique; 114 curated mentions over 45 concepts.
- **Projected to 100,000 articles** (claim) Curated index 150 to 2,660 times smaller; a question about 13,000 tokens; search sees 2%.
- **PageRank with meaning** (concept) Typed edges citing their sentences say what a link means; a two-article loop tops our own PageRank.
- **Agents are personas too** (concept) An agent arrives with an objective; the slice fitted to it is the product.
- **The agent pays not to pay** (claim) A fee below the token saving is rational; about ten questions pay for an article's graph.
- **Signed claims with an expiry** (method) A claim re-checked and signed as of a date, until a date, renewed for a fee.
- **Will agents pay?** (question) The rails exist and the arithmetic works on paper; demand is untested.

> Compression with scale is not a property of graphs. It is a property of curation. The hypothesis, tested.

> A reader that saves money by using it will pay for it, not out of goodwill but because paying is cheaper than not paying. The economic model in one sentence.

builds on [One article, five readers: a librarian, a cartographer, a historian, an explainer and a storyteller read the same piece](#one-article-five-readers), [The bridge, followed to the end: what one local story is worth when it is kept as a graph](#the-bridge-followed-to-the-end), [Pay to keep your persona: readers should pay because it helps them, not because they feel they should](#pay-to-keep-your-persona), [A link to a persona: send people to the newsroom as someone, not as nobody](#a-link-to-a-persona), [Re-anchoring: keeping an agent's rules alive through every summary, and a canary that shows when they are not](#re-anchoring-agent-behaviour-policies), [Sixteen thousand fetches, ten clicks, and a token bill nobody is sending: the case for paying publishers to be easy to read](#token-bill-nobody-is-sending), [Pay after you read: how a reading meter became a working business model in one afternoon, one release at a time](#pay-after-you-read), [RFC 0001: two ways to add public-key cryptography to sgit, and the questions we want you to answer](#rfc-0001-public-key-cryptography-for-sgit), [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](#introducing-fractal-semantic-graphs), [Memory is not a spectator sport: how a web of open sites, graphs and vaults became the memory for sessions like this one](#memory-is-not-a-spectator-sport), [The future of news is the story vault, not the paywall](#future-of-news-story-vault-not-paywall); continued by [A model in the tab: Chrome now ships an LLM to capable desktops, and it is the hardest piece of the client-side puzzle](#a-model-in-the-tab).

## [Where the platform draws the line: Microsoft Execution Containers, the shared responsibility model for agents, and the business logic above it](where-the-platform-draws-the-line.md)

2026-10-11 · Agents & policy

Microsoft Execution Containers and the Agent Control Specification confirm the direction of travel, policy outside the agent, deny by default, observe before enforcing, but like the cloud's shared responsibility model they draw the line where the platform can see, at paths, numeric addresses and tool calls, so the business logic above it, what a label means, whose voice, how many, which customer, and who accepts what is left, has to come from the deployer's behaviour policy, which is what turns the platform's hooks into boundaries.

*[diagram]*
**concept**claim**method**artefact**example**question

**8 nodes, 7 edges**

- **Microsoft Execution Containers** (artefact) A versioned JSON policy enforced by the OS: sandbox, process, paths, network, desktop; deny by default.
- **Agent Control Specification** (artefact) Eight interception points, a snapshot of the session, a policy engine and a normalised verdict; hooks, not rules.
- **Permissive, learning, enforcement** (method) Measure the reach, calibrate it, enforce it: the ABP's three verbs as platform modes.
- **Shared responsibility, for agents** (concept) Every platform draws its line at the granularity it can touch.
- **Business logic above the line** (claim) Labels, voice, quantity and customer are business content no platform can supply.
- **Eight scenarios, three designs** (example) Plain: 8 open. ABP: 8 named, 0 bounded. ABP on MXC and ACS: 3 OS boundaries, 4 if the rule is written, 1 accepted.
- **Same code, different owner** (claim) An MXC file or ACS manifest the agent can edit is a setting, not a boundary.
- **The policy writes the rules** (question) Generating MXC JSON and ACS policies from ABP rows: a design, not a product.

> The unit of restriction is the application and the tool. It is not the data, and it is not the business. The line every platform draws.

> The policy names it, proposes the boundaries that shrink it What a behaviour policy does with a risk inside the mandate.

builds on [The same argument, in our words: Satya Nadella on models as insider risks, translated into the language of RiskMandate](#the-same-argument-in-our-words), [Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan](#authority-outside-the-model), [How to run synthetic users on your own site: five people who do not exist, a browser, and an afternoon](#how-to-run-synthetic-users), [A second reader the agent cannot skip: how two wrong emails became a gate on every draft](#a-second-reader-the-agent-cannot-skip), [Zoom into an agent's behaviour policy and you find the business logic](#the-behaviour-policy-is-the-business-logic), [Before you give an agent a connector, give the connector a twin](#connector-twin-before-you-deploy-an-agent), [Hope or enforcement: one customer service agent, three designs, and who keeps each promise](#hope-or-enforcement), [Every risk is already accepted. The only question is by whom, and for how long.](#every-risk-is-already-accepted), [Footprint and blast radius: what the agent actually did, and what it would have cost](#footprint-and-blast-radius), [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](#riskmandate-ten-questions).

## [The same argument, in our words: Satya Nadella on models as insider risks, translated into the language of RiskMandate](the-same-argument-in-our-words.md)

2026-10-11 · Agents & policy

Nadella's argument and ours are the same argument in two vocabularies: his lost code path is software was the law, his insider is the ultimate insider, his separation of supply from authority is the grant is not the mandate, his controls outside the model are the enforcer test, and his last line is our brakes; the languages differ in unit, a model against one agent in one deployment, and in frame, observation against authority accepted by a named person for a stated interval.

*[diagram]*
**concept**claim**method**artefact

**10 nodes, 9 edges**

- **Models as insider risks** (artefact) Nadella's post, paraphrased throughout and quoted once.
- **Software was the law** (concept) Rules the interface enforced by omission are gone when an agent calls the API.
- **The ultimate insider** (concept) A threat need not be malicious; the distance between benign and hostile is a prompt.
- **Every risk is already accepted** (concept) No deny button; the only questions are who holds it and until when.
- **The grant is not the mandate** (concept) Supply arrives with a grant; authority is a mandate with an issuer, scope and clock.
- **The enforcer test** (concept) Only a boundary the agent cannot reach is a control.
- **Reality is the calibrator** (method) Measure the grant on the thing itself and compare the footprint with the mandate.
- **Brakes let a car go fast** (claim) Constraint is what makes autonomy affordable.
- **One agent, one deployment** (claim) Risk is a property of a deployment, not of a model.
- **Authority before observation** (claim) A written mandate and a named acceptor tell you whether what you observed was allowed.

> And a mandate with no clock is just a grant. What authority needs before it is separate from supply.

> Independence is not a property of the checker. It is a property of who controls it. The answer to nested black boxes.

builds on [Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan](#authority-outside-the-model), [Zoom into an agent's behaviour policy and you find the business logic](#the-behaviour-policy-is-the-business-logic), [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](#ultimate-insider-three-collisions), [Every risk is already accepted. The only question is by whom, and for how long.](#every-risk-is-already-accepted), [Knowing when to stop: what experience gives people, and what we have to design into agents](#knowing-when-to-stop), [A second reader the agent cannot skip: how two wrong emails became a gate on every draft](#a-second-reader-the-agent-cannot-skip), [Hope or enforcement: one customer service agent, three designs, and who keeps each promise](#hope-or-enforcement), [Six agents, one inbox: what a real multi-agent setup taught me about access policies](#six-agents-one-inbox), [Footprint and blast radius: what the agent actually did, and what it would have cost](#footprint-and-blast-radius), [Before you give an agent a connector, give the connector a twin](#connector-twin-before-you-deploy-an-agent); continued by [From me to you, in a link: a personal reading list, two briefs to build and use it, and the loop that makes it a day's work](#a-reading-list-in-a-link), [Where the platform draws the line: Microsoft Execution Containers, the shared responsibility model for agents, and the business logic above it](#where-the-platform-draws-the-line), [Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan](#authority-outside-the-model).

## [Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan](authority-outside-the-model.md)

2026-10-11 · Agents & policy

Treating models as insider risks is right, and each of the seven principles maps to something this network runs, publishes or plans, but the principles work only with the column they leave thin: authority written down before the agent runs, a mandate compared with the footprint, risk belonging to one deployment rather than a model, a named owner and expiry for what is left, recoverability beyond the brake, and decisions made in advance as envelopes.

*[diagram]*
**concept**claim**method**artefact

**10 nodes, 9 edges**

- **Models as insider risks** (artefact) Nadella's post: separate the supply of intelligence from the authority over it; seven principles.
- **The enforcer test** (concept) A control bounds a grant only if enforced by something the grant does not include.
- **A second reader the agent cannot skip** (method) Code checks first, a different model with less context, fail closed, log every verdict.
- **Same code, different owner** (claim) Whether a check is a setting or a boundary depends on who owns its installation.
- **Evidence the writer cannot edit** (method) Vault history, append lanes, hashed ledgers, the connector twin.
- **The mandate is the missing column** (claim) Observation says what happened; only a written mandate says whether it was allowed.
- **Footprint in the gap is a near miss** (concept) Countable long before anything breaks; the number worth disclosing.
- **Risk belongs to a deployment** (claim) The same model is harmless in one setup and serious in another.
- **A brake does not undo** (claim) Containment needs a list of what can and cannot be reversed.
- **Honest maturity** (artefact) What runs, what is published as design, what is only argued, principle by principle.

> Observation tells you what an agent did. It cannot tell you whether the agent was allowed to, unless somebody wrote down what it was for before it ran. The missing column, in two sentences.

> Containment without recoverability is a brake on a car with no reverse gear. Why the brake is not enough.

builds on [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](#ultimate-insider-three-collisions), [The same argument, in our words: Satya Nadella on models as insider risks, translated into the language of RiskMandate](#the-same-argument-in-our-words), [A second reader the agent cannot skip: how two wrong emails became a gate on every draft](#a-second-reader-the-agent-cannot-skip), [Why my agents do not run on my laptop: chat, Cowork and Code in the cloud, a vault as the shared drive, and the two walls an operating system has](#why-my-agents-do-not-run-on-my-laptop), [The infographic bake-off: which image model for which job, judged blind on 10 October 2026](#the-infographic-bake-off), [One article, five readers: a librarian, a cartographer, a historian, an explainer and a storyteller read the same piece](#one-article-five-readers), [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](#the-agent-team-as-it-runs), [Where the vault keys live: key management at sgit-ai v0.20.0, and what comes next](#where-the-vault-keys-live), [Re-anchoring: keeping an agent's rules alive through every summary, and a canary that shows when they are not](#re-anchoring-agent-behaviour-policies), [Before you give an agent a connector, give the connector a twin](#connector-twin-before-you-deploy-an-agent), [Footprint and blast radius: what the agent actually did, and what it would have cost](#footprint-and-blast-radius), [Hope or enforcement: one customer service agent, three designs, and who keeps each promise](#hope-or-enforcement), [Green does not mean live](#green-does-not-mean-live), [How to run synthetic users on your own site: five people who do not exist, a browser, and an afternoon](#how-to-run-synthetic-users), [The investigation GitHub owes its customers: why a global outage of a platform the world deploys through deserves an aviation-style inquiry, and how the evidence could now be gathered](#the-investigation-github-owes-its-customers), [Every risk is already accepted. The only question is by whom, and for how long.](#every-risk-is-already-accepted), [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](#riskmandate-ten-questions); continued by [Where the platform draws the line: Microsoft Execution Containers, the shared responsibility model for agents, and the business logic above it](#where-the-platform-draws-the-line), [The same argument, in our words: Satya Nadella on models as insider risks, translated into the language of RiskMandate](#the-same-argument-in-our-words).

## [How to run synthetic users on your own site: five people who do not exist, a browser, and an afternoon](how-to-run-synthetic-users.md)

2026-10-10 · Vaults & methodSite & engineering

Synthetic users are invented people, each a record with a situation, a question, what they know and do not, what they decide on and what makes them leave, played by a model that drives a real browser one screenshot at a time instead of reading the page's code, so it can get lost as a person would. Claude Sonnet is good enough to play each user; the study lives in a GitHub repository or a vault shared by a link. Choose five to ten users of about five types, write profiles and expected journeys first, run the observe-think-act loop, interview and rate, order findings by cost, check every surprising finding against the browser's record, publish and run again. On newsroom.sgit.ai five readers produced 31 findings, six blocking; two were caused by the helper, and one became a measured bug: 51 of 527 figures missing.

*[diagram]*
**concept**claim**method**artefact**example

**11 nodes, 10 edges**

- **Screenshot, not the code** (method) An agent reading the code finds every link and therefore no confusion.
- **A profile is a record** (concept) Situation, question, knows, does not know, decides on, walks away if, patience, screen.
- **Expected journey first** (method) Written before the run, so a surprise shows as a difference.
- **Sonnet plays each user** (claim) Good enough to read a screenshot and stay in character; Opus for checking evidence.
- **Repository or vault** (concept) Public GitHub is easiest to share; a vault is encrypted, opens as an app, shared by a link.
- **Interview and rating** (method) The same ten questions for everyone; a rating from 1 to 5.
- **Findings ordered by cost** (method) Blocks a pilot, costs a payment, costs trust, loses a reader, minor.
- **Check before publishing** (method) Two newsroom findings were the helper's doing and are labelled, not deleted.
- **51 of 527 figures missing** (example) The researcher's broken image, measured across the newsroom after the move.
- **Run against a verified copy** (method) Byte-identical local files: nothing reaches the live site, and the run repeats.
- **Three studies** (artefact) store.sgit.ai, riskmandate.ai and newsroom.sgit.ai, each in a vault.

> An agent that reads the code finds every link every time, and so finds no confusion, which is the only thing worth running this for. The method in one sentence.

> A findings list that silently loses items cannot be compared with the next one. Why artefacts are labelled, not deleted.

builds on [A link to a persona: send people to the newsroom as someone, not as nobody](#a-link-to-a-persona); continued by [From me to you, in a link: a personal reading list, two briefs to build and use it, and the loop that makes it a day's work](#a-reading-list-in-a-link), [A model in the tab: Chrome now ships an LLM to capable desktops, and it is the hardest piece of the client-side puzzle](#a-model-in-the-tab), [No server, by design: first I retired the database, now I am retiring the back end](#no-server-by-design), [Where the platform draws the line: Microsoft Execution Containers, the shared responsibility model for agents, and the business logic above it](#where-the-platform-draws-the-line), [Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan](#authority-outside-the-model).

## [A link to a persona: send people to the newsroom as someone, not as nobody](a-link-to-a-persona.md)

2026-10-10 · Startups & strategyVaults & method

A link should land a reader as someone rather than as nobody: personas move from the site's code into an encrypted vault kept by the newsroom's agents and opened in the browser with a published read key, reached through a page of their own, a URL fragment that never reaches a server, or a private vault for one person, and the reader can follow the persona as it is updated or fork it as their own, all client side.

*[diagram]*
**concept**claim**method**artefact**example**question

**10 nodes, 9 edges**

- **Landing as nobody** (question) A link to the front page lands a reader on a page made for nobody in particular.
- **Personas in a vault** (artefact) Encrypted, versioned, opened in the browser with a published read key; updated without touching the site.
- **Three kinds of link** (method) A page of its own, a fragment for any number more, a private vault for one person.
- **The fragment never reaches a server** (concept) RFC 3986: the fragment is dereferenced solely by the user agent.
- **Follow or fork** (method) Track the persona as it is kept up to date, or copy it and make it your own.
- **The persona keeper** (method) A newsroom role that updates personas on every article and issue, each change a vault commit.
- **Bluesky starter packs** (example) A link that sets up a newcomer: up to 150 people and three feeds, June 2024.
- **Netflix profiles** (example) Up to five profiles per account from August 2013.
- **Personas about people stay private** (claim) A public persona describes a role; a persona about a person goes in a vault sent only to them.
- **All client side** (claim) Static pages, ciphertext on the vault host, everything else in the browser.

> The better move is for the person who sends the link to choose it Why a link should name a persona.

> a persona is a reading list with a history, and you either track the upstream or branch from it. Follow and fork, from git.

builds on [Pay to keep your persona: readers should pay because it helps them, not because they feel they should](#pay-to-keep-your-persona); continued by [From me to you, in a link: a personal reading list, two briefs to build and use it, and the loop that makes it a day's work](#a-reading-list-in-a-link), [No server, by design: first I retired the database, now I am retiring the back end](#no-server-by-design), [The agent is the reader: why agents will pay for graphs, personas and signed claims, because it is cheaper than not paying](#the-agent-is-the-reader), [How to run synthetic users on your own site: five people who do not exist, a browser, and an afternoon](#how-to-run-synthetic-users).

## [Pay after you read: how a reading meter became a working business model in one afternoon, one release at a time](pay-after-you-read.md)

2026-10-10 · News & evidenceStartups & strategy

On 10 October the reading meter became a working pay-on-demand publication in seven releases in 3 hours 40 minutes: pay for the share read from a balance that can go below zero, rate usefulness after reading to set the price from free to double, personas and newsrooms kept in the reader's browser, and consented, encrypted sharing for a designed front page. Paying after the value inverts Leanpub's pay-before model and is supported, with caveats, by pay-what-you-want evidence; Blendle's refunds show ratings measure quality. Each feature grew from using the last, which a Wardley map shows: new components on the left, built on commodities already there. It was fast because of non-functional work done before. Every decision started from not ripping off the reader. What is missing is traffic.

*[diagram]*
**claim**method**example

**10 nodes, 9 edges**

- **Pay by depth, below zero** (method) A price per page charged for the share read, from a balance that never blocks.
- **Usefulness sets the price** (method) Rate after reading, 1 free to 5 double; more like this moves the persona.
- **Personas and newsrooms** (method) Built from reading, kept in the browser, a front page for each.
- **Share your reading** (method) Shown word for word, copied or sent encrypted with consent, for a designed front page.
- **Pay after the value** (claim) Leanpub prices before reading; here the reader decides after.
- **Pay what you want evidence** (example) Gneezy 2010, Kim, Natter and Spann 2009, Riener and Traxler 2012; Blendle refunds up to 50% for gossip.
- **Do not rip off the reader** (claim) Value for money over money left on the table.
- **One release at a time** (claim) Each feature came from using the last; the end state was not designed.
- **The more we have, the faster we go** (claim) Gates, versioned components, tests, git and reused lanes made it fast.
- **Test it on a site with traffic** (claim) SG Meter is ready for others; what is missing is readers.

> The only question left is whether people will pay for it. What changed on 10 October.

> If you saw the value, pay; if you saw more value, pay more; if you did not, do not. The reader card in one line.

builds on [Open source is not free: who pays to keep the long tail working?](#open-source-is-not-free), [Every mistake added a rule: complexity, agents, and the way back to shipping](#every-mistake-added-a-rule), [Going live with the reading meter: pay for what you read, go below zero if you like, and the numbers we will check in eight weeks](#going-live-with-the-reading-meter), [A meter in the browser: a penny a page, a history you keep, and a site that picks for you](#a-meter-in-the-browser), [Who will game the reading meter? Eight kinds of reader, nine ways to cheat, and the risks that will actually happen](#who-will-game-the-reading-meter), [Pay to keep your persona: readers should pay because it helps them, not because they feel they should](#pay-to-keep-your-persona); continued by [No server, by design: first I retired the database, now I am retiring the back end](#no-server-by-design), [The agent is the reader: why agents will pay for graphs, personas and signed claims, because it is cheaper than not paying](#the-agent-is-the-reader).

## [Where the vault keys live: key management at sgit-ai v0.20.0, and what comes next](where-the-vault-keys-live.md)

2026-10-10 · Vaults & methodAgents & policy

Vaults are encrypted in the client, so the server never holds a key and the key is the whole question. Today vault keys live in a password manager and in a registry vault run by an isolated session; agents that create vaults seal the key to the registry's public key and send it on a write-only append lane, so it never enters a chat. The weakest step is giving a key to another agent, because agent platforms have no per-session secrets. Append lanes carry keys, logs, observations and messages; small communication vaults keep each key's blast radius small and multiply the keys. Next: password manager integrations, secrets.sgit.ai's passkey-unlocked keyring, PKI, and out-of-band decryption.

*[diagram]*
**concept**claim**method**artefact**example

**9 nodes, 8 edges**

- **Decryption in the client** (concept) S3 stores ciphertext; the API and the edge never see a vault key.
- **One secret, derived keys** (concept) The vault key reads and writes; the read key is derived one way and published on purpose.
- **Where keys live today** (example) A password manager for a person's keys; a registry vault for keys agents create.
- **Sealed handover** (method) Seal to the registry's public key, one POST on a write-only lane, deterministic drain, human review.
- **Giving a key to an agent** (claim) No per-session secrets: environment variables are shared per environment; network secrets carry API keys only.
- **Append lanes** (method) Write-only, blind, one POST from anywhere; used for keys, logs, observations and messages.
- **Communication vaults** (method) A vault per conversation or job, with EmailFS and IssuesFS inside.
- **What comes next** (claim) Password managers, secrets.sgit.ai, PKI, out-of-band decryption.
- **secrets.sgit.ai** (artefact) A passkey PRF unwraps the keyring key; ciphertext in a cloud bucket; app proposed at v0.1.13.

> The key is the whole question. Why key management matters for client-side encryption.

> Nothing between the sender and the registry can read the key, the key is never typed or shown. What the sealed handover changes.

builds on [RFC 0001: two ways to add public-key cryptography to sgit, and the questions we want you to answer](#rfc-0001-public-key-cryptography-for-sgit), [The identity we wanted to give the agents: a week of design, the line in Google's terms, and why login plus secrets is still too hard](#the-identity-we-wanted-to-give-the-agents), [Encrypted memory for agents that run somewhere else: sgit deployment patterns, from a Mac mini to Kubernetes](#encrypted-memory-for-isolated-agents), [A personal agent that keeps your secrets: the 2026 agents read through behaviour policy and encryption, and a privacy-first design on vaults, enclaves and the browser](#a-personal-agent-that-keeps-your-secrets); continued by [No server, by design: first I retired the database, now I am retiring the back end](#no-server-by-design), [Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan](#authority-outside-the-model).

## [The infographic bake-off: which image model for which job, judged blind on 10 October 2026](the-infographic-bake-off.md)

2026-10-10 · Site & engineeringNews & evidence

To make infographics part of the newsroom's workflow, every image-output model on OpenRouter on 10 October 2026 was given the same briefs from one article, from 18 words to 2,800, plus an edit, a component, a brand slide and a deck, over five rounds with blind judging and recorded costs; the answer is to choose the model by the job, not the budget: Nano Banana 2.1 for concept slides, charts and decks, Gemini 3 Pro Image when speed matters, GPT-5.4 Image 2 for documents, edits, components and brand slides, with prompt rules learned from the faults and a style reference for every deck.

*[diagram]*
**concept**claim**method**artefact**example**question

**14 nodes, 16 edges**

- **Which model for which job** (question) Infographics are moving into the newsroom's daily workflow; the choice of model needs evidence.
- **Every image model on OpenRouter** (concept) Eight models, the auto-router and a code-drawn control; none free.
- **Eleven briefs from one article** (method) From an 18-word stat card to the whole article, plus edit, component, brand and deck.
- **Blind judging** (method) A Designer agent fact-checked and scored every image under a random id; OCR as an independent check.
- **Every cent recorded** (artefact) OpenRouter's usage cost per generation: $10.44 for 101 images.
- **Cost per usable image** (concept) Half the spend bought images the judge would not use; price per image flatters failure.
- **Give it the document** (claim) GPT-5.4 Image 2 scored 9 on the document and the whole article; the older GPT-5 Image got worse.
- **An edit is a redraw** (example) Only GPT-5.4 Image 2 made three changes without breaking anything.
- **The cheap model's limit** (claim) Nano Banana 2.1 had no usable image where every character was specified.
- **Slide 1 as a style reference** (method) Attaching slide 1 raised every model's deck consistency from 1 or 2 to 4 or 5 of 5.
- **Three models, three tiers** (claim) Nano Banana 2.1, Gemini 3 Pro Image, GPT-5.4 Image 2.
- **Guidance and prompt rules** (artefact) Which model for which job, and rules such as never name the platform and say No other text.
- **The bake-off vault** (artefact) Every brief, image, score, reason and cost, as an app.
- **The answer has a date** (question) Models and prices change; the bake-off is built to be run again.

> Give it the document, not a description of the picture. The finding that matches how ChatGPT is best used, and where it applies.

> Choose the model by the job, not by the budget. The conclusion, in the article's own words.

builds on [Re-anchoring: keeping an agent's rules alive through every summary, and a canary that shows when they are not](#re-anchoring-agent-behaviour-policies), [One article, five readers: a librarian, a cartographer, a historian, an explainer and a storyteller read the same piece](#one-article-five-readers); continued by [Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan](#authority-outside-the-model).

## [Pay to keep your persona: readers should pay because it helps them, not because they feel they should](pay-to-keep-your-persona.md)

2026-10-10 · Startups & strategyNews & evidence

Paying for content because you have to, feel you should, or think it right works to a degree but does not scale and makes readers feel the wrong thing; what readers would pay for is what helps them, time, context, focus and good decisions, carried by a persona built from their reading, named, drawn as a graph, curated, and multiplied for focus, and the paid product is that persona following them between devices and agents with the privacy intact.

*[diagram]*
**concept**claim**artefact**example**question

**9 nodes, 8 edges**

- **Paying because you have to, or feel you should** (concept) Paywall, the ask, the donation: they work to a degree and do not scale.
- **£12 to avoid the supporter messages** (example) The Guardian's middle tier sells, among other things, the end of the ask.
- **8 million donors, $10.58 on average** (example) Wikimedia's 2023-24 fundraising: what asking everybody reaches.
- **Pay for time, context, focus and good decisions** (claim) What a reader is actually buying.
- **The persona** (artefact) Built from reading, named from its topics, drawn as a graph, curated with Keep and Not for this persona.
- **Personas are focus** (claim) Users of personalisation want several personas, one per kind of reading.
- **Five starting personas** (artefact) Founder, journalist, security lead, AI builder, board member, built from what the site publishes.
- **Two devices, two strangers** (question) Not a cheat to worry about but a bad experience that worsens as the persona improves.
- **A persona that follows you** (claim) To phone, laptop and agent, in a vault only the reader can open: the thing worth paying for.

> The reader should pay because paying helps them. The value proposition in one line.

> A persona is a way to manage focus. Why one reader wants several personas.

builds on [Going live with the reading meter: pay for what you read, go below zero if you like, and the numbers we will check in eight weeks](#going-live-with-the-reading-meter), [Who will game the reading meter? Eight kinds of reader, nine ways to cheat, and the risks that will actually happen](#who-will-game-the-reading-meter), [Git for things you cannot put on GitHub](#what-sgit-is), [One article, five readers: a librarian, a cartographer, a historian, an explainer and a storyteller read the same piece](#one-article-five-readers); continued by [From me to you, in a link: a personal reading list, two briefs to build and use it, and the loop that makes it a day's work](#a-reading-list-in-a-link), [A model in the tab: Chrome now ships an LLM to capable desktops, and it is the hardest piece of the client-side puzzle](#a-model-in-the-tab), [No server, by design: first I retired the database, now I am retiring the back end](#no-server-by-design), [The agent is the reader: why agents will pay for graphs, personas and signed claims, because it is cheaper than not paying](#the-agent-is-the-reader), [A link to a persona: send people to the newsroom as someone, not as nobody](#a-link-to-a-persona), [Pay after you read: how a reading meter became a working business model in one afternoon, one release at a time](#pay-after-you-read), [Going live with the reading meter: pay for what you read, go below zero if you like, and the numbers we will check in eight weeks](#going-live-with-the-reading-meter).

## [Who will game the reading meter? Eight kinds of reader, nine ways to cheat, and the risks that will actually happen](who-will-game-the-reading-meter.md)

2026-10-10 · Startups & strategyAgents & policy

A reading meter kept entirely in the browser can be cheated by anyone, but the people who could cheat are readers, not attackers; sized on a ladder from invisible engineers (about 0.6% of internet users are developers) to people who cannot use a computer (26% of OECD adults), with agents moving between steps, the cheating costs the site nothing it would have had, while the risks that will actually happen are confusion, a shared computer exposing history and card fraud, so the design is aimed at the readers who will pay and at not frightening the rest.

*[diagram]*
**concept**claim**method**artefact**example

**9 nodes, 8 edges**

- **Who are you protecting against, one level down** (concept) Kinds of reader instead of tiers of attacker; none malicious.
- **Eight kinds of reader** (concept) Invisible, agents, power users, instruction followers, pragmatic payers, little understanding, mixed, struggling.
- **Agents change level in a single request** (claim) Outside the meter by design; reading the markdown twin is not metered.
- **Nine ways to cheat or leak** (artefact) Devtools, private window, forged return page, replay, clearing data, agents, shared computer, injected script, card fraud.
- **Cheating costs nothing that reaches the site** (claim) It changes a number only the cheater sees and removes a payment that was never coming.
- **The risks that will actually happen** (claim) Confusion at the bottom of the ladder, shared-computer history, card fraud on the payment link.
- **Aim at the readers who will pay** (method) Do not build for step 1 at the expense of steps 5 to 8.
- **26% of adults cannot use a computer** (example) OECD Survey of Adult Skills via Nielsen Norman Group: only 5% at the most skilled level.
- **Developers are about 0.6% of internet users** (example) 36.5 million professional developers against about 6.0 billion internet users.

> An agent is not a step; it is a lift. Agents move between levels of sophistication in a single request.

> The struggling reader is protected by the meter asking nothing of them. Why the usability work is aimed at the bottom of the ladder.

builds on [Who are you protecting against? Draw the security line where the attacker is, not above it](#who-are-you-protecting-against), [Going live with the reading meter: pay for what you read, go below zero if you like, and the numbers we will check in eight weeks](#going-live-with-the-reading-meter), [Sixteen thousand fetches, ten clicks, and a token bill nobody is sending: the case for paying publishers to be easy to read](#token-bill-nobody-is-sending); continued by [Pay after you read: how a reading meter became a working business model in one afternoon, one release at a time](#pay-after-you-read), [Pay to keep your persona: readers should pay because it helps them, not because they feel they should](#pay-to-keep-your-persona), [Going live with the reading meter: pay for what you read, go below zero if you like, and the numbers we will check in eight weeks](#going-live-with-the-reading-meter).

## [Going live with the reading meter: pay for what you read, go below zero if you like, and the numbers we will check in eight weeks](going-live-with-the-reading-meter.md)

2026-10-10 · Startups & strategyNews & evidence

The reading meter goes live as an honesty box rather than a paywall: pages are charged by scroll depth, the balance may go below zero forever, there is no ask and no banner, readers can decline to pay with a reason, and topping up is one £5 Stripe payment credited by an unverified return page; the business case is evidence, not revenue, and five hypotheses with thresholds and a review date are written down before the first payment.

*[diagram]*
**concept**claim**method**artefact**example**question

**10 nodes, 8 edges**

- **Pay for the share you read** (method) A page costs its price times the deepest point scrolled to, never less than a tenth.
- **Below zero, forever, without shame** (method) Nothing blocked, nothing shown but a small balance in the top bar.
- **Not worth it? Don't charge me** (method) Refund with a reason, kept locally as a signal for the picks.
- **The Guardian's counter and ask** (example) Weekly article counts in localStorage used to ask for support; £4, £12 and £27 a month, £107m digital reader revenue.
- **The subscription commitment** (concept) £4 a month is £48 a year, decided before the reading happens.
- **An honesty box, not a paywall** (claim) Bagels about 87 to 95% paid; Radiohead 38%; pay-what-you-want raises take-up and lowers the average.
- **One £5 Stripe payment** (artefact) 1.5% + 20p on a standard UK card, about 5.5%; the return page credits without verifying.
- **The business case is evidence** (claim) A payment is the only signal on the site curiosity cannot produce.
- **Five hypotheses and a review date** (question) First payment in 14 days, 10 payers, 3 repeat payers, no disputes, below zero is normal; review eight weeks after the link goes live.
- **SG Meter, a library** (artefact) One web component any site can add, with config, events, storage and a security model.

> And going below zero is not a failure state. The design choice that separates this meter from a paywall or an ask.

> A payment is the only signal on this site that cannot be produced by curiosity. The business case in one line.

builds on [A meter in the browser: a penny a page, a history you keep, and a site that picks for you](#a-meter-in-the-browser), [Pay to keep your persona: readers should pay because it helps them, not because they feel they should](#pay-to-keep-your-persona), [For a startup, the most important question is whether they miss it](#the-question-is-whether-they-miss-it), [The reader was always the product: a corrected history of how news got into this mess](#how-news-got-here), [Price it, then give it away: the early access programme as the next step after "do they miss it"](#price-it-then-give-it-away), [Who will game the reading meter? Eight kinds of reader, nine ways to cheat, and the risks that will actually happen](#who-will-game-the-reading-meter); continued by [No server, by design: first I retired the database, now I am retiring the back end](#no-server-by-design), [Pay after you read: how a reading meter became a working business model in one afternoon, one release at a time](#pay-after-you-read), [Pay to keep your persona: readers should pay because it helps them, not because they feel they should](#pay-to-keep-your-persona), [Who will game the reading meter? Eight kinds of reader, nine ways to cheat, and the risks that will actually happen](#who-will-game-the-reading-meter), [A meter in the browser: a penny a page, a history you keep, and a site that picks for you](#a-meter-in-the-browser).

## [Open source is not free: who pays to keep the long tail working?](open-source-is-not-free.md)

2026-10-10 · Startups & strategyVaults & method

Open source is not free: somebody pays, at least in time. The long tail of old versions and old machines is measurable (6.99% of Homebrew macOS install events in 30 days, 16.66% in a year, are on versions older than the newest three) and projects drop it because it has no revenue stream, while vendors such as Oracle and Red Hat turn the same need into large, high-margin support businesses. Pence payments only work aggregated, because a 20p card fee dominates below about five pounds. Simulated over 10,000 draws for one project at Homebrew's scale, micro-paid supported builds cover the long-tail cost in half the draws at about 1.80 pounds a machine a year with typical conversion but never in nine in ten, donations in about a quarter, and customised builds for companies in 94%: the reliable money is companies paying for a build below their own cost of keeping the tool working, sold as value, not as a donation or a weaker free tier.

*[diagram]*
**concept**claim**method**artefact**example

**11 nodes, 10 edges**

- **One old iMac** (example) Intel iMac on Ventura: Chrome and Claude work; Homebrew and Docker Desktop do not; Python by hand.
- **Open source is not free** (claim) Somebody pays, at least in time; the long tail has no revenue stream back to the maintainers.
- **The long tail, measured** (artefact) Homebrew: 6.99% (30 days) to 16.66% (365 days) of macOS install events on versions older than the newest three; PyPI: 18.55% of pip on end-of-life Python.
- **Where money flows** (concept) Oracle support $19.8bn, Red Hat subscriptions at about 93% margin, Windows 10 ESU, Ubuntu Pro, against about 0.09% of open source's value invested.
- **Charging has costs** (concept) Docker's seat licence and the switch to alternatives, relicensing forks, dual licensing, gamed per-install rewards.
- **The pence problem** (claim) A 20p card fee is 41.5% of 50p; pence payments need aggregation.
- **Five models, simulated** (method) Donations, seat licence, support rising with age, micro-paid builds, customised builds for companies; 10,000 seeded draws.
- **Break-even near two pounds** (artefact) About 1.80 pounds a machine a year covers the cost in half the draws with typical conversion; no price reaches nine in ten.
- **Customised builds for companies** (method) Priced below the internal cost of keeping the tool working; covers the cost in 94% of draws.
- **The satellites** (concept) About 18 small support firms worldwide per project's pool; Rimini Street as the existence proof.
- **Long Tail Ledger vault** (artefact) 175 sourced facts, 36 labelled assumptions, the model in Python and in the browser, gated to agree exactly.

> Open source is not free. Somebody is paying for it, even if what they pay with is only their time. The thesis.

> Pence from individuals can make the long tail roughly self-funding. They cannot make it safe to depend on. What the break-even view shows.

builds on [A meter in the browser: a penny a page, a history you keep, and a site that picks for you](#a-meter-in-the-browser); continued by [Pay after you read: how a reading meter became a working business model in one afternoon, one release at a time](#pay-after-you-read).

## [One article, five readers: a librarian, a cartographer, a historian, an explainer and a storyteller read the same piece](one-article-five-readers.md)

2026-10-10 · News & evidenceGraphs & knowledge

Long, evidence-rich articles are hard to consume, and the answer is not shorter articles but extraction after the writing: the prose stays the source because writing is how the argument is found, and five agent readers with defined roles then produce other views of it, two building the platform (a Librarian that catalogues every item with its verbatim anchor, a Cartographer that builds an ontology at article, topic and site altitude and draws the maps) and three writing for a person (a Historian on what the article added and where it sits, an Explainer in two minutes, a Storyteller as a deck); run on five articles it catalogued 662 items, flagged 32 problems in published text, merged ideas named differently across articles, and measured each article's contribution as new concepts falling 17, 11, 5, 11, 1.

*[diagram]*
**concept**claim**method**artefact**example**question

**15 nodes, 17 edges**

- **Deep articles are hard to consume** (claim) Five articles of 2,200 to 5,100 words: good sources, hard reading.
- **The prose comes first** (claim) Writing is how the argument is found; every other view is extracted afterwards.
- **Five readers** (concept) Agents with roles: Librarian, Cartographer, Historian, Explainer, Storyteller.
- **Platform readers build the graph** (concept) Librarian and Cartographer: catalogue, ontology and maps.
- **Context readers write for a person** (concept) Historian, Explainer, Storyteller: deliberately short.
- **Every item anchored verbatim** (method) Each catalogued item carries the sentence it came from, checked by script.
- **Ontology at three altitudes** (method) Article, topic and site, one grammar, every edge citing catalogue items.
- **32 problems flagged** (example) Totals that do not add up, counts longer than lists, claims unsupported in the text.
- **Same idea, different names** (example) Expectation and hope; second reader and maker-checker; one method under five names.
- **New concepts: 17, 11, 5, 11, 1** (example) What each article brought, measured from the graph.
- **New to the set is not new to the site** (claim) The Historian found earlier articles introduced several 'new' concepts: the case for a site altitude.
- **Read it another way** (artefact) The five views on each article page and in its markdown twin.
- **The Article Views vault** (artefact) Roles, catalogues, ontology, maps, notes, decks, tools and an app.
- **Image prompts not yet run** (question) Decks are code-drawn; image-model prompts are written and need a key.
- **Feedback written, not applied** (question) The Cartographer's merges and splits await the second Librarian pass.

> It does not change how the writing is done. It maximises what the writing produces. The design rule: extraction after the prose, not a new way of writing.

> a topic ontology tells you what is new to the topic; only a site ontology tells you what is new. The finding that sets the next step.

builds on [Liquid content needs water: liquefy the journalist's notebook, not the finished product](#liquid-content-needs-water), [Zoom into an agent's behaviour policy and you find the business logic](#the-behaviour-policy-is-the-business-logic), [Every mistake added a rule: complexity, agents, and the way back to shipping](#every-mistake-added-a-rule), [Hope or enforcement: one customer service agent, three designs, and who keeps each promise](#hope-or-enforcement), [A second reader the agent cannot skip: how two wrong emails became a gate on every draft](#a-second-reader-the-agent-cannot-skip), [Re-anchoring: keeping an agent's rules alive through every summary, and a canary that shows when they are not](#re-anchoring-agent-behaviour-policies), [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](#introducing-fractal-semantic-graphs), [Footprint and blast radius: what the agent actually did, and what it would have cost](#footprint-and-blast-radius), [The Mandate Stack: a multi-agent system in production, layer by layer](#the-mandate-stack), [Every risk is already accepted. The only question is by whom, and for how long.](#every-risk-is-already-accepted); continued by [The agent is the reader: why agents will pay for graphs, personas and signed claims, because it is cheaper than not paying](#the-agent-is-the-reader), [Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan](#authority-outside-the-model), [The infographic bake-off: which image model for which job, judged blind on 10 October 2026](#the-infographic-bake-off), [Pay to keep your persona: readers should pay because it helps them, not because they feel they should](#pay-to-keep-your-persona).

## [A meter in the browser: a penny a page, a history you keep, and a site that picks for you](a-meter-in-the-browser.md)

2026-10-10 · Startups & strategyNews & evidence

A reading meter that lives only in the browser, a few pence a page from five pounds of starting credit with a simulated top-up and no blocking, tests whether people would pay a little for reading when what they get back is a site that personalises itself from a history nobody else holds; escaping the meter is easy, but escaping it also discards the history, which is the point of the experiment.

*[diagram]*
**claim**method**artefact**example**question

**8 nodes, 7 edges**

- **A meter in the browser** (artefact) Every page priced in pence, debited from £5.00 of credit kept in localStorage; one debit per page per visit.
- **Never block a page** (method) Out of credit, the page is shown and the read recorded as unpaid, with an offer to top up.
- **Every step but the payment** (method) Packs, a cart, a review, a confirm and a receipt; credit added at once, nothing charged.
- **The history is the product** (claim) The ledger of what was read, with topics, is enough to pick unread articles for the reader.
- **The meter can be escaped; the personalisation cannot be copied** (claim) A private window starts again at £5.00 and with no history.
- **Would people pay for a site that knows them?** (question) The experiment the meter puts in front of a reader.
- **The pt.newsroom wallet** (example) One cent a page, a self-refilling five-euro wallet, a ledger page: the first version.
- **402 Payment Required** (example) Reserved in the web's protocol in 1997 for micropayments, still unused.

> The meter can be escaped; the personalisation cannot be copied. The trade the experiment puts in front of a reader.

> The history never leaves the machine it was made on. Personalisation without an account, a cookie banner or a server.

builds on [Going live with the reading meter: pay for what you read, go below zero if you like, and the numbers we will check in eight weeks](#going-live-with-the-reading-meter), [For a startup, the most important question is whether they miss it](#the-question-is-whether-they-miss-it), [Price it, then give it away: the early access programme as the next step after "do they miss it"](#price-it-then-give-it-away), [The reader was always the product: a corrected history of how news got into this mess](#how-news-got-here), [Sixteen thousand fetches, ten clicks, and a token bill nobody is sending: the case for paying publishers to be easy to read](#token-bill-nobody-is-sending), [The bridge, followed to the end: what one local story is worth when it is kept as a graph](#the-bridge-followed-to-the-end); continued by [Pay after you read: how a reading meter became a working business model in one afternoon, one release at a time](#pay-after-you-read), [Going live with the reading meter: pay for what you read, go below zero if you like, and the numbers we will check in eight weeks](#going-live-with-the-reading-meter), [Open source is not free: who pays to keep the long tail working?](#open-source-is-not-free).

## [Re-anchoring: keeping an agent's rules alive through every summary, and a canary that shows when they are not](re-anchoring-agent-behaviour-policies.md)

2026-10-10 · Agents & policySite & engineering

Instructions given only in conversation can be lost when a long session is summarised, and this site's own session was summarised eighteen times in a month, keeping about 1.7% each time; re-anchoring keeps the agent's rules in an Agent Behaviour Policy file and has a SessionStart hook on the compact matcher print it back after every summary, so rules are restored rather than remembered, while a canary status report computed from the transcript, checked by a Stop hook and expected by the person, shows the policy is still being read; the same file serves as memory, checker rulebook and enforcement list, and the best recipe for each rule changes with every platform release, which is the work worth curating.

*[diagram]*
**concept**claim**method**artefact**example

**10 nodes, 9 edges**

- **Instructions lost at compaction** (claim) The platform's own documentation says conversation-only instructions can disappear after a summary.
- **Eighteen summaries, 1.7% kept** (example) This session's transcript: about 785,000 tokens replaced by 9,000 to 19,000, each time automatic.
- **Three ways a rule fails** (concept) It forgets, it does not see, it argues; each needs a different fix.
- **Re-anchoring** (method) A SessionStart hook on the compact matcher prints the ABP back after every summary.
- **One file, three jobs** (concept) The ABP is memory, the checker's rulebook and the list of rules still needing a gate.
- **The canary report** (method) A short report every few answers, computed from the transcript and checked by a Stop hook.
- **The brown M&M** (example) A small clause that shows whether the whole contract was read.
- **A rule measured** (artefact) Commits not preceded by a leak scan, counted from the transcript.
- **Recipes that age** (claim) The best way to keep each rule changes with every platform release; keeping it current is the work.
- **A second reader and a gate** (method) What fixes the failures re-anchoring cannot.

> The rules are restored, not remembered. What re-anchoring changes.

> A policy row with a number next to it is a different thing from a policy row on its own. Why the canary measures a rule.

builds on [A second reader the agent cannot skip: how two wrong emails became a gate on every draft](#a-second-reader-the-agent-cannot-skip); continued by [The agent is the reader: why agents will pay for graphs, personas and signed claims, because it is cheaper than not paying](#the-agent-is-the-reader), [Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan](#authority-outside-the-model), [The infographic bake-off: which image model for which job, judged blind on 10 October 2026](#the-infographic-bake-off), [One article, five readers: a librarian, a cartographer, a historian, an explainer and a storyteller read the same piece](#one-article-five-readers).

## [A second reader the agent cannot skip: how two wrong emails became a gate on every draft](a-second-reader-the-agent-cannot-skip.md)

2026-10-09 · Agents & policySite & engineering

A rule held by the agent it governs is an expectation that can be forgotten, missed or argued around, so the inbox agent's fix after two emails went out in the founder's voice puts a gate on the draft tool itself: deterministic code checks first, then a fresh model call with only the rules, the sources and the draft, a different model from the author, failing closed on anything but an explicit PASS and logging every verdict; its independence depends on where it is installed, a setting while the agent can change it and a boundary only under managed placement, and the pattern is the old maker-checker control applied to any consequential tool call.

*[diagram]*
**concept**claim**method**artefact**example

**11 nodes, 10 edges**

- **Two emails in the founder's voice** (example) 9 October: a rule written in four places failed, because only the drafter enforced it.
- **A rule held by the agent it governs** (claim) It can be forgotten at compaction, missed by its author, or argued around.
- **The draft guard** (artefact) A hook on create_draft and update_draft: code checks, then a fresh checker model.
- **Code checks first** (method) Signature, HTML, dashes, key shapes and recipients, with no model call.
- **A fresh checker** (method) No history, no tools, a different model; only rules, sources and the draft.
- **Fail closed** (method) Hooks fail open by default; errors, timeouts and bad answers must deny.
- **Six kinds of independence** (concept) What the checker sees, who decides it runs, and who wrote the evidence.
- **Placement decides the barrier** (claim) A session mod or plugin is a setting; managed placement makes it a boundary.
- **Maker-checker** (concept) Segregation of duties, the two-person rule, the independent double check.
- **The reusable pattern** (method) Pick the consequential call, code first, fresh checker, explicit PASS, log.
- **What the first run caught** (example) Four invented claims, and false FAILs for facts without sources.

> An email that is late is a small cost. An email that goes out wrong cannot be taken back. Why the guard fails closed.

> A rule kept by the agent it governs is hope. The general weakness the guard answers.

builds on [Hope or enforcement: one customer service agent, three designs, and who keeps each promise](#hope-or-enforcement), [Every mistake added a rule: complexity, agents, and the way back to shipping](#every-mistake-added-a-rule); continued by [From me to you, in a link: a personal reading list, two briefs to build and use it, and the loop that makes it a day's work](#a-reading-list-in-a-link), [Where the platform draws the line: Microsoft Execution Containers, the shared responsibility model for agents, and the business logic above it](#where-the-platform-draws-the-line), [The same argument, in our words: Satya Nadella on models as insider risks, translated into the language of RiskMandate](#the-same-argument-in-our-words), [Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan](#authority-outside-the-model), [One article, five readers: a librarian, a cartographer, a historian, an explainer and a storyteller read the same piece](#one-article-five-readers), [Re-anchoring: keeping an agent's rules alive through every summary, and a canary that shows when they are not](#re-anchoring-agent-behaviour-policies).

## [The AI governance stack, as a graph: an answer to Hari Kota, built](the-ai-governance-stack-as-a-graph.md)

2026-10-09 · Graphs & knowledgeAgents & policy

Keep Hari Kota's ten-layer stack exactly as posted as the view and make a fractal semantic graph the model: the table already contains ten edges across layers where rows share an instrument, role or jurisdiction; each layer is its own world with its own ontology, sharing only a grammar of verbs with inverses; the edges between worlds come from the provisions themselves, such as EU AI Act Article 26(2) and NIST AI RMF GOVERN 1.6; changes over time are dated edges rather than rewrites; and a gap is a missing edge, so the do-this-today test and the gaps in layers 3, 5 and 10 become queries anyone can run.

*[diagram]*
**concept**claim**method**artefact**example**question

**12 nodes, 11 edges**

- **Hari's stack, as posted** (artefact) Ten layers, ten purposes and forty-six examples, kept word for word as nodes.
- **The table already contains a graph** (claim) Ten edges cross the layers where rows name the same instrument, role or jurisdiction.
- **Each layer is its own world** (concept) Law, standards, inventory, testing and people each keep their own ontology.
- **Five grammar rules** (method) Verbs with inverses, no relates_to, data in properties, supersede never delete, render answers.
- **Edges from provisions** (method) Every added edge rests on a readable provision: Art 26(2), Art 4, Annex III, GOVERN 1.6, 42001 7.2.
- **Zoom from one cell down** (concept) Cell to instrument to provision to an organisation's systems, owners and records.
- **The graph keeps time** (claim) 2026 amendments sit under Hari's labels as dated edges, older values struck through.
- **Do this today, as a traversal** (method) System to owner, and system to classification to tier and basis; a missing step is the gap.
- **Gaps as queries** (method) Layers 3, 5 and 10 become queries with traversals and results.
- **Hollow Oak Home** (example) A fictional shop with eight AI systems in three jurisdictions and planted gaps.
- **What 4 or 5 means** (question) 10 of 10 layers somewhere, 1 of 10 for every system, 0 with the shadow tool.
- **AI Governance Graph vault** (artefact) 335 nodes, 702 edges, a 22-check gate and an app, published with its read key.

> start with the edges the people who wrote the layers already drew without drawing them The first answer to Hari's question.

> A table is correct on the day it is drawn. Why the graph keeps time.

builds on [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](#introducing-fractal-semantic-graphs), [Code review as a fractal semantic graph: source code is already one, and the review should read every layer of it](#code-review-as-a-fractal-semantic-graph).

## [RFC 0001: two ways to add public-key cryptography to sgit, and the questions we want you to answer](rfc-0001-public-key-cryptography-for-sgit.md)

2026-10-09 · Vaults & methodSite & engineering

An sgit vault's read key is symmetric, so anyone who holds it and can write to the store can author history clients accept; turning the read key into a public key does not fix that, but two key pairs do, giving a native PKI vault mode where readers cannot write, hosts cannot forge and write-only depositors become possible, while an optional sealed-files layer encrypts chosen files to named people's public keys with the private key held in a file, an ssh key, hardware or a remote service that logs and approves each decryption; both share a first step, a writer signature on today's vaults, and nothing is built until reviewers have answered fourteen questions.

*[diagram]*
**concept**claim**method**artefact**example**question

**11 nodes, 11 edges**

- **One symmetric read key** (concept) PBKDF2 derives a read key that encrypts everything and a write key only the server checks.
- **Whoever can read can forge** (claim) A read-key holder who can write to the store, such as the host or a mirror, can author history.
- **One key pair is not enough** (claim) The private half yields the public half, and decrypting with a public key is signing; two pairs work.
- **A writer signature first** (method) An Ed25519 key from a third derivation path signs refs and index on today's vaults.
- **Native PKI vault mode** (method) A read pair and a write pair; a data key sealed to the read public key; signed heads.
- **The write-only depositor** (concept) Can add content readers open, cannot read: append to an inbox branch.
- **Sealed files** (method) An age v1 inner envelope seals chosen files to named people's public keys, on any vault.
- **Where the private key lives** (artefact) A key file, an ssh key, hardware, or a remote service that logs and approves each unwrap.
- **Writers can replace blindly** (claim) Sealing needs only public keys, so integrity needs signed envelopes and author rules.
- **Known shapes** (example) Tahoe-LAFS, Hypercore, git-crypt, SOPS, age and HPKE (RFC 9180).
- **Fourteen questions** (question) Where an outside view would most change the design, before anything is built.

> Add a second key pair for reading, and every property falls out. The correction to the obvious idea.

> its hard part is not the cryptography but downgrade resistance Where the writer signature's real work is.

builds on [Encrypted memory for agents that run somewhere else: sgit deployment patterns, from a Mac mini to Kubernetes](#encrypted-memory-for-isolated-agents); continued by [From me to you, in a link: a personal reading list, two briefs to build and use it, and the loop that makes it a day's work](#a-reading-list-in-a-link), [The agent is the reader: why agents will pay for graphs, personas and signed claims, because it is cheaper than not paying](#the-agent-is-the-reader), [Where the vault keys live: key management at sgit-ai v0.20.0, and what comes next](#where-the-vault-keys-live).

## [A Mac of the agent's own: a business plan for agent desktops, what Apple's licence allows, and three behaviour policies](a-mac-of-the-agents-own.md)

2026-10-09 · Startups & strategyAgents & policyVaults & method

After a mailbox, a code-host account and a Claude account, an agent's next dedicated resource is a desktop, and it should be a Mac; Apple's licence rules out a pool rented by the minute, so the business is a dedicated Mac per customer, run for them, metered by the minute, built clean per run from encrypted vaults with keys by PKI and erased at the end, plus developer agents, software for your own Mac and a request to Apple for terms; the behaviour policies show why: the same agent's unbounded excess falls from 23 rows to 11 to 3.

*[diagram]*
**concept**claim**method**artefact**example**question

**11 nodes, 10 edges**

- **The next dedicated resource** (claim) After a mailbox, a code-host account and a Claude account, a desktop of the agent's own.
- **Why a Mac** (claim) Agent desktop apps ship to the Mac first; it is familiar; and it is the one you cannot rent by the minute.
- **What Apple's licence allows** (concept) Leases of 24 hours or more, for developer services, to one customer; no time-sharing of virtual copies.
- **The shapes that are allowed** (method) Your Mac run for you, a dedicated Mac metered, developer agents, software, and asking Apple.
- **A clean Mac, a key, a vault** (method) Install sgit, decrypt one key, clone the set-up vault, run its signed program; erase at the end.
- **Keys by PKI** (method) Each desktop's own key pair; vault keys encrypted to it; the private key in its keychain.
- **Three desktops, one agent** (example) Unbounded excess 23 on your own Mac, 11 on a dedicated Mac, 3 on a hardened one.
- **The shop admin screen** (claim) What remains on the hardened Mac is mostly one screen that shows every customer.
- **A meter on a Mac one customer holds** (artefact) About £211 a month against £119 for a Mac mini you run and £390 for daily leases, on assumptions.
- **Productising the agent's desktop** (artefact) A Wardley map: the desktop moves to product on parts that are already products or commodities.
- **What are we looking for?** (question) Dedicated Macs with erase and provision APIs, a meter, a developer offer, and a joint approach to Apple.

> The pool of Macs rented by the minute that I first imagined is not allowed. The licence finding, stated first.

> Per-minute pricing survives, as a meter on a Mac one customer holds, never as a share of a Mac that others use. How the business model survives the licence.

builds on [A locked-down desktop for an agent, by the minute, is still hard to rent](#an-agent-desktop-by-the-minute), [Why my agents do not run on my laptop: chat, Cowork and Code in the cloud, a vault as the shared drive, and the two walls an operating system has](#why-my-agents-do-not-run-on-my-laptop), [Six agents, one inbox: what a real multi-agent setup taught me about access policies](#six-agents-one-inbox), [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](#the-agent-team-as-it-runs), [Encrypted memory for agents that run somewhere else: sgit deployment patterns, from a Mac mini to Kubernetes](#encrypted-memory-for-isolated-agents), [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](#riskmandate-ten-questions), [Hope or enforcement: one customer service agent, three designs, and who keeps each promise](#hope-or-enforcement).

## [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](riskmandate-ten-questions.md)

2026-10-09 · Agents & policyStartups & strategy

Every answer rests on four objects for one agent in one deployment, mandate, grant, delta and barriers, and a strict division of roles: RiskMandate authors the policy and pre-commits the verdict, the customer's controls enforce it, a named executive owns the residual risk, and logs calibrate the grant; so RiskMandate is not inline, not an insurer and not one button, the value lands before the action, new capability can only land as excess, and the headline metric is the reduction in risk the business has to accept.

*[diagram]*
**concept**claim**method**artefact**example**question

**13 nodes, 12 edges**

- **Mandate, grant, delta, barriers** (concept) Four objects for one agent in one deployment; only a boundary is a control.
- **Author, decide, enforce** (concept) RiskMandate authors and pre-commits; the customer's stack enforces; an executive owns the rest.
- **The 5k order was possible on day one** (example) Bypass is unbounded excess the policy surfaces before any action.
- **The mandate is locked business logic** (claim) New capability can only land in the reach, as excess, never as new authority.
- **Reality is the calibrator** (method) The grant is reverse-engineered from logs; documentation said no attachments, Claude found a way.
- **Open source, maintained per customer** (claim) The product is a customised, maintained vault; the moat is delivery and trust.
- **Authorisation is the grant** (claim) Liability sits with the customer from the moment the reach exists; risks route to an executive.
- **We make agents insurable** (claim) The record is what an underwriter can price; no risk transfer exists today.
- **The supply chain is a bigger agent** (claim) A compromise is a grant that exploded or a boundary that vanished; trust travels by connectivity.
- **Containment now, reversal next** (method) Circuit breakers pre-committed; twins, replay and version control, bounded by one-way doors.
- **Authorisation by encryption** (method) Delegated authority attenuated by keys, not inherited by privilege.
- **What is the headline metric?** (question) Reduction in accepted risk; runtime metrics belong to the enforcement layer.
- **Three fixes on our own site** (artefact) Homepage enforcement wording, insurance page tense, the Level 1 price.

> The value is delivered **before** the action, not at it. Where the value of a behaviour policy lands.

> **the moment of authorisation is the moment you granted the reach, not the moment you wrote the mandate.** The liability reframe.

builds on [Footprint and blast radius: what the agent actually did, and what it would have cost](#footprint-and-blast-radius), [Hope or enforcement: one customer service agent, three designs, and who keeps each promise](#hope-or-enforcement), [Zoom into an agent's behaviour policy and you find the business logic](#the-behaviour-policy-is-the-business-logic), [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](#introducing-fractal-semantic-graphs), [Before you give an agent a connector, give the connector a twin](#connector-twin-before-you-deploy-an-agent), [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](#the-agent-team-as-it-runs), [Where is the why? A permission prompt asked me to decide, and kept the reason](#where-is-the-why), [Agency is not a yes: a scale for human and agent decisions, from rubber stamp to the reviewer who fixes the source](#agency-is-not-a-yes), [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](#ultimate-insider-three-collisions), [The Mandate Stack: a multi-agent system in production, layer by layer](#the-mandate-stack), [Six agents, one inbox: what a real multi-agent setup taught me about access policies](#six-agents-one-inbox), [The identity we wanted to give the agents: a week of design, the line in Google's terms, and why login plus secrets is still too hard](#the-identity-we-wanted-to-give-the-agents), [Git for things you cannot put on GitHub](#what-sgit-is), [Encrypted memory for agents that run somewhere else: sgit deployment patterns, from a Mac mini to Kubernetes](#encrypted-memory-for-isolated-agents), [Every risk is already accepted. The only question is by whom, and for how long.](#every-risk-is-already-accepted), [Code review as a fractal semantic graph: source code is already one, and the review should read every layer of it](#code-review-as-a-fractal-semantic-graph), [Knowing when to stop: what experience gives people, and what we have to design into agents](#knowing-when-to-stop), [The investigation GitHub owes its customers: why a global outage of a platform the world deploys through deserves an aviation-style inquiry, and how the evidence could now be gathered](#the-investigation-github-owes-its-customers); continued by [Where the platform draws the line: Microsoft Execution Containers, the shared responsibility model for agents, and the business logic above it](#where-the-platform-draws-the-line), [Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan](#authority-outside-the-model), [A Mac of the agent's own: a business plan for agent desktops, what Apple's licence allows, and three behaviour policies](#a-mac-of-the-agents-own).

## [How I work with Claude: one session per topic, agents with names, and memory you curate](how-i-work-with-claude.md)

2026-10-09 · Agents & policyVaults & method

Working well with Claude comes from a few habits: one session per major or recurring topic and no mixed threads, a naming pattern with @ names for agents, an agent defined as a focused session with a role.md, memory treated as what the session reads and curated as websites, graphs and vaults wired together and accessible by default, vaults for sharing by key instead of broad permissions, review as the quality step that fixes the brief, and an Agent Behaviour Policy before every new connector.

*[diagram]*
**concept**claim**method**artefact**example**question

**12 nodes, 11 edges**

- **One session per topic** (method) Every major or recurring topic gets its own session, tab or window; no mixed threads.
- **Mixed threads mix context** (claim) Everything in a thread is context for the next answer, so topics bleed into each other.
- **Name every session** (method) project | what we are working on; agent sessions get an @ name.
- **An agent is a focused session** (concept) Project documents, a role.md, and a session named for the role.
- **Memory is what the session reads** (concept) Curated websites, graphs and vaults wired together are the agent's universe.
- **Access by default** (claim) Publish what you can; inside a company, make most content available to most people.
- **Vaults to receive and send** (method) A vault key instead of broad permissions; read keys for read-only.
- **Review fixes the brief** (method) Mistakes traced to a brief or file that needed to be better, and fixed there.
- **Starter prompts** (artefact) Start a project session, an agent session, hand over a vault, end a session.
- **Policy before connectors** (claim) Each connector adds power and danger; an ABP makes connecting more comfortable.
- **A Cowork session per agent** (example) For agentic work, a separate session for each agent, with its own name and role.
- **Where do I start?** (question) Close the mixed thread, write one role.md, make memory findable, share by key.

> One topic per session keeps the frame of reference small and right. Why sessions stay separate.

> The more time I spend curating and maintaining those files, the more relevant and accurate the agents are. Where the quality comes from.

builds on [Memory is not a spectator sport: how a web of open sites, graphs and vaults became the memory for sessions like this one](#memory-is-not-a-spectator-sport), [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](#the-agent-team-as-it-runs), [Replicating the agentic inbox: a walkthrough from one Claude session to a team of agents that never press send](#replicating-the-agentic-inbox), [Agency is not a yes: a scale for human and agent decisions, from rubber stamp to the reviewer who fixes the source](#agency-is-not-a-yes), [Why my agents do not run on my laptop: chat, Cowork and Code in the cloud, a vault as the shared drive, and the two walls an operating system has](#why-my-agents-do-not-run-on-my-laptop), [Encrypted memory for agents that run somewhere else: sgit deployment patterns, from a Mac mini to Kubernetes](#encrypted-memory-for-isolated-agents), [Hope or enforcement: one customer service agent, three designs, and who keeps each promise](#hope-or-enforcement).

## [The waiting room knew first: a live local story, and the gap where local information used to be](the-waiting-room-knew-first.md)

2026-10-08 · News & evidenceVaults & method

On 8 October 2026 staff at two sites of one London trust told patients the IT systems were down, a five-hour wait was announced and a doctor called it national, yet nothing a local person could check before leaving home showed any of it; the story is not the outage or the hospital but the gap in local information: some UK nations publish live emergency waits, England has no national equivalent, local news has thinned and social feeds have fragmented, so the evidence is kept in a vault by level, with sources re-checked, an enquiry to the trust and the answer logged, as the first live counterpart to the fictional bridge story.

*[diagram]*
**concept**claim**method**artefact**example**question

**12 nodes, 12 edges**

- **Two sites, one message: the IT is down** (example) Staff at Charing Cross and Western Eye; about five hours announced; a doctor said national.
- **Evidence separated by level** (method) Heard second-hand, told by staff, observed, documented, confirmed by the organisation, corroborated.
- **Two sites, one trust** (claim) Both run by Imperial College Healthcare: not two independent signs of a national outage.
- **Not found is not none** (claim) Status channels need a login or an NHS network; blocked pages are limits of access.
- **The waiting room knew first** (claim) The information existed and reached people only once they were already there.
- **Newsworthy to the person deciding** (concept) Go now, later, tomorrow or elsewhere: the decision a status line would have changed.
- **Live waits exist in parts of the UK** (example) Northern Ireland and Wales publish live emergency waits; England has no national page.
- **A duty to warn, for emergencies** (concept) The Civil Contingencies Act duty applies to serious emergencies, not an afternoon slowdown.
- **Where local information went** (claim) News deserts, fewer people on X for news, local groups with rumour and hoaxes.
- **Not naming and shaming** (claim) The question is the channel, for any trust, council or operator, not the staff.
- **The Local evidence log** (artefact) Observations, claims, sources, leads, an enquiry, scheduled checks, by incident.
- **What would close the gap?** (question) A plain status line, a route from inside to outside, evidence not rumour, an agent that asks.

> What strikes me is that the only way to find out was to be there. The gap in one line.

> It is not small if you are deciding whether to set off now. Why a small story is newsworthy to the person affected.

builds on [The bridge, followed to the end: what one local story is worth when it is kept as a graph](#the-bridge-followed-to-the-end), [Story vault underneath, Reader Skills on top: why local journalism has the most to gain](#story-vault-meets-reader-skills).

## [Encrypted memory for agents that run somewhere else: sgit deployment patterns, from a Mac mini to Kubernetes](encrypted-memory-for-isolated-agents.md)

2026-10-08 · Vaults & methodAgents & policySite & engineering

Agents are safer in isolated places, but isolation takes away the shared drive and ephemeral compute takes away the disk, so their memory has to live somewhere the owner controls and a breach does not expose; a self-hosted SG/Send container with an access token and storage in a folder or bucket, with sgit in each agent, gives them that: scoped clones make each run fast, the server holds only ciphertext, any clone can restore any server, and the trust sits with the agents and their keys, so a scoped clone is speed, not a boundary, and one vault per trust boundary is the rule.

*[diagram]*
**concept**claim**method**artefact**example**question

**13 nodes, 14 edges**

- **Isolated agents lose their memory** (claim) No shared drive in the box, and no disk that survives ephemeral compute.
- **Owner-controlled, reachable, breach-safe** (concept) The three conditions the memory has to meet.
- **One vault container, an access token** (artefact) diniscruz/sg-send-vault, port 8080, storage in a folder, S3 or memory.
- **Start with a Mac mini** (method) Vault container next to agent containers; back up one folder of ciphertext.
- **One agent run** (method) Scoped shallow clone, one task, commit, push, delete the container.
- **Scoped clones make it fast** (example) One folder of a 600-commit vault in 14 s against 80 s for the whole.
- **A scoped clone is not a boundary** (claim) sgit fetch widened a1's clone to a2's folder: one vault per trust boundary.
- **Kubernetes: a Deployment and Jobs** (method) One replica on disk or more on S3, ClusterIP, NetworkPolicy, a Secret per agent.
- **The cloud, with no public route** (method) Container or Lambda, both inside the VPC behind an internal load balancer; S3, a VPN, CloudFront.
- **Two servers, one vault** (example) Push to a backup remote; any clone restored a memory-mode server after a restart.
- **A breach gives away ciphertext** (claim) No plaintext, no file names in storage; vault ids, sizes, timing, a write-key hash.
- **The trust sits with the agents** (claim) Writing agents hold the vault key on disk; ephemeral boxes and per-agent secrets matter.
- **What is ready and what is not** (question) The image runs; cloud templates are in progress; use --base-url, not --endpoint.

> An agent that starts every run from nothing repeats work, loses what it found, and cannot hand anything to the next agent. Why isolated agents need memory outside the box.

> `--path` decides what is downloaded, not what can be read. Scoped clones are speed, not an access boundary.

builds on [Why my agents do not run on my laptop: chat, Cowork and Code in the cloud, a vault as the shared drive, and the two walls an operating system has](#why-my-agents-do-not-run-on-my-laptop), [A locked-down desktop for an agent, by the minute, is still hard to rent](#an-agent-desktop-by-the-minute), [Who are you protecting against? Draw the security line where the attacker is, not above it](#who-are-you-protecting-against), [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](#the-agent-team-as-it-runs); continued by [No server, by design: first I retired the database, now I am retiring the back end](#no-server-by-design), [Where the vault keys live: key management at sgit-ai v0.20.0, and what comes next](#where-the-vault-keys-live), [RFC 0001: two ways to add public-key cryptography to sgit, and the questions we want you to answer](#rfc-0001-public-key-cryptography-for-sgit), [A Mac of the agent's own: a business plan for agent desktops, what Apple's licence allows, and three behaviour policies](#a-mac-of-the-agents-own), [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](#riskmandate-ten-questions), [How I work with Claude: one session per topic, agents with names, and memory you curate](#how-i-work-with-claude).

## [Knowing when to stop: what experience gives people, and what we have to design into agents](knowing-when-to-stop.md)

2026-10-08 · Agents & policyStartups & strategy

Knowing when to stop is the hardest call in most work: for people it comes from perspective, knowing the attackers, the phase of the business, the bottleneck and what good enough looks like, which is much of what seniority is; good teams without it defend against movie plots or hit every KPI without moving the business; agents have the same problem by design because their range is the feature, so they keep going; the answer for both is constraints that carry perspective, direction, a mandate, memory with the bigger picture, graphs that narrow the scope, a stop named in advance, one kind of work per step, a reviewer with agency, and shipping often enough to see whether it mattered.

*[diagram]*
**concept**claim**method**example

**10 nodes, 9 edges**

- **Variability is the feature** (claim) Agents can go in every direction; that is what makes them useful, and why they need direction.
- **What seniority gives you** (concept) The bigger picture: strategy, the real risks, moving between tactical and strategic.
- **Debating whether GUIDs are random enough** (example) Teams that automated away bug classes then defended against a movie plot; 122 random bits.
- **Giving permission to take risks** (claim) Perspective, not common sense: technically possible, and it does not matter here.
- **Every KPI hit, needle still** (example) Teams reverse-engineer metrics; when a measure becomes a target it stops measuring.
- **Which phase are you in?** (method) A Wardley map says whether polish is right or waste, and where the bottleneck is.
- **Art is knowing when to stop** (claim) Good enough and diminishing returns; shipping and observability as the feedback loop.
- **Why it is harder for agents** (claim) A wide range of skills and no natural limit: fix the small thing, then the bigger one, then all twenty.
- **Work expands to fill the team** (concept) Parkinson 1955; any entity that can do work, put in a team, will find work.
- **Constraints that carry perspective** (method) FIRE rather than draconian rules: direction, mandate, memory, graphs, a named stop, one step, review, shipping.

> An entity that can go anywhere has no natural reason to stop anywhere. Why agents need the stop designed in.

> What I found myself doing, in that meeting and in many others across the business, was giving people permission to take risks. Perspective as the senior contribution.

builds on [Agency is not a yes: a scale for human and agent decisions, from rubber stamp to the reviewer who fixes the source](#agency-is-not-a-yes), [How much of this did I write? The numbers behind twenty articles in four weeks, and what the input actually was](#how-much-of-this-did-i-write), [Who are you protecting against? Draw the security line where the attacker is, not above it](#who-are-you-protecting-against), [Every mistake added a rule: complexity, agents, and the way back to shipping](#every-mistake-added-a-rule), [Hope or enforcement: one customer service agent, three designs, and who keeps each promise](#hope-or-enforcement), [Memory is not a spectator sport: how a web of open sites, graphs and vaults became the memory for sessions like this one](#memory-is-not-a-spectator-sport), [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](#the-agent-team-as-it-runs); continued by [The same argument, in our words: Satya Nadella on models as insider risks, translated into the language of RiskMandate](#the-same-argument-in-our-words), [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](#riskmandate-ten-questions).

## [Agency is not a yes: a scale for human and agent decisions, from rubber stamp to the reviewer who fixes the source](agency-is-not-a-yes.md)

2026-10-08 · Agents & policyGraphs & knowledge

Agency for anyone asked to decide, a person or an agent, needs options beyond yes, context in their own terms, the ability to look behind what they are shown, time or tokens, symmetric incentives, escalation and authority over the source; the weakest of these caps the decision on a seven-level scale; below level 3 the decider carries liability rather than agency and accountability belongs to whoever designed the decision point and up their chain; above it the review is a QA step that validates everything upstream and fixes the source, and at the top proven cases become rules that run as code under a behaviour policy, which is also what the EU AI Act's oversight requirements already ask for.

*[diagram]*
**concept**claim**method**artefact**example

**13 nodes, 12 edges**

- **A yes or no is not agency** (claim) The least interesting part of a decision; a no that stalls the work is not a real option.
- **Add label 756-459-3214?** (example) An identifier instead of a thing: which message, which label, why?
- **Whatever you punish, you teach the other answer** (claim) Asymmetric blame makes reviewers say no, or say yes; omission bias is the studied form.
- **Everything shown is a compression** (concept) Provenance and zoomable graphs let a decider decompress the summary when there is a question.
- **Accountability without agency is liability** (claim) Takeover times, Bainbridge's irony, the moral crumple zone; accountability belongs up the chain.
- **Seven levels, seven dimensions** (method) Options, context, depth, time, incentives, escalation, authority; the weakest caps the level.
- **Fourteen decision points scored** (artefact) Eight at level 0; the fixed sign-in push at 1; a clinician at 4; draft review at 5; the hold email at 6.
- **Agents are deciders too** (claim) An agent asked 'is this OK?' with no context is a rubber stamp; the final yes should be code.
- **The review is a QA step** (method) Read as the signer, question each statement, trace it, fix the source, think better, record it.
- **Ownership changes attention** (concept) Publishing under someone's name, or making them accept a risk, is what makes them engage.
- **From review to rule** (method) Clean passes become rules under a behaviour policy; cheaper models for defined tasks; senior reviewers for the rest.
- **The law puts the floor at level 3** (claim) EU AI Act Articles 14(4) and 26(2) and the guidance on meaningful oversight.
- **The agency scale, the vault** (artefact) The levels, dimensions, cases, the loop, the law and an assessment to run on your own decisions.

> Whatever you punish, you teach the other answer. Incentives decide the answer before the decider does.

> The right fix is not to the email. It is to the record, the graph, the connection, so that every future email has it. The review as QA.

builds on [Where is the why? A permission prompt asked me to decide, and kept the reason](#where-is-the-why), [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](#introducing-fractal-semantic-graphs), [Hope or enforcement: one customer service agent, three designs, and who keeps each promise](#hope-or-enforcement), [How much of this did I write? The numbers behind twenty articles in four weeks, and what the input actually was](#how-much-of-this-did-i-write), [Every risk is already accepted. The only question is by whom, and for how long.](#every-risk-is-already-accepted), [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](#the-agent-team-as-it-runs); continued by [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](#riskmandate-ten-questions), [How I work with Claude: one session per topic, agents with names, and memory you curate](#how-i-work-with-claude), [Knowing when to stop: what experience gives people, and what we have to design into agents](#knowing-when-to-stop).

## [Hope or enforcement: one customer service agent, three designs, and who keeps each promise](hope-or-enforcement.md)

2026-10-08 · Agents & policyVaults & method

Every design of an agent can have a rule for every behaviour; what differs is who enforces each rule and how much the agent can reach, so refactoring a customer service agent from one model with broad connectors, to a harness of business tools, to a team of narrow agents behind a deterministic identity gateway turns most of its policy from expectations the model keeps into boundaries it cannot reach, shrinks the policy because it no longer has to forbid what is impossible, cuts tokens, and leaves a short map of what still rests on hope and which boundary to build next, read after every run and shown to the client as a record rather than a score.

*[diagram]*
**concept**claim**method**artefact**example

**12 nodes, 11 edges**

- **A customer service agent on a shop's inbox** (example) Fictional shop, 38,000 customers, 1,400 emails a week; one mandate of twelve actions.
- **Hope and enforcement** (concept) Expectation is a rule the model keeps; boundary is a limit the agent cannot reach; only the second is a control.
- **Design 1: one agent, two connectors** (example) 38-rule policy, 97% hope; one run reaches 38,000 records, any refund, any address; 35,000 tokens per email.
- **Design 2: a harness of business tools** (example) Reach falls to 1,000 records, 5,000 GBP, 20 emails; six rules move into code; 73% still hope.
- **Tool signatures are where policy hopes** (claim) Every argument naming a customer, an order or an address is a rule the model must keep.
- **Design 3: a team behind a gateway** (example) Runs bound to one verified customer; 23% hope; unbounded excess zero; 4,400 tokens per email.
- **More tools, each narrower** (claim) Granular tools carry business knowledge in code: once per order, before dispatch, the bound customer.
- **Narrow agents still have too much power** (claim) A compromised mailbox and voucher farming work inside the mandate; the policy finds them.
- **The policy says which boundary to build next** (method) Address confirmation, per-customer refund and voucher caps, sampled review of tone.
- **Read the policy after every run** (method) What was exercised, what hostile mail tested, what held; tokens against the budget.
- **The client sees the record, not a score** (artefact) Eight promises, and for each design what keeps each one; the business case from the same record.
- **Hope or enforcement, the vault** (artefact) The mandate, three designs, 62 emails, the analyst's report and a recomputable year.

> Every design has a policy for every behaviour. The difference is who enforces it. The thesis.

> The design breaks its own budget rule on every email, which is what happens to a budget that is an expectation. Tokens as a policy like any other.

builds on [Zoom into an agent's behaviour policy and you find the business logic](#the-behaviour-policy-is-the-business-logic), [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](#the-agent-team-as-it-runs); continued by [Where the platform draws the line: Microsoft Execution Containers, the shared responsibility model for agents, and the business logic above it](#where-the-platform-draws-the-line), [The same argument, in our words: Satya Nadella on models as insider risks, translated into the language of RiskMandate](#the-same-argument-in-our-words), [Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan](#authority-outside-the-model), [One article, five readers: a librarian, a cartographer, a historian, an explainer and a storyteller read the same piece](#one-article-five-readers), [A second reader the agent cannot skip: how two wrong emails became a gate on every draft](#a-second-reader-the-agent-cannot-skip), [A Mac of the agent's own: a business plan for agent desktops, what Apple's licence allows, and three behaviour policies](#a-mac-of-the-agents-own), [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](#riskmandate-ten-questions), [How I work with Claude: one session per topic, agents with names, and memory you curate](#how-i-work-with-claude), [Knowing when to stop: what experience gives people, and what we have to design into agents](#knowing-when-to-stop), [Agency is not a yes: a scale for human and agent decisions, from rubber stamp to the reviewer who fixes the source](#agency-is-not-a-yes).

## [Who are you protecting against? Draw the security line where the attacker is, not above it](who-are-you-protecting-against.md)

2026-10-08 · Agents & policyStartups & strategy

Security decisions start with who the threat agent is, what the attack vector is and how sophisticated they are; read against a ladder from your own mistakes to elevated threats, grounded in NIST SP 800-30, the NCSC and MITRE ATT&CK, most startups should plan up to organised crime for money, do the basics consistently because they beat most attackers, sell something better than the customer's baseline rather than beyond their needs, prefer isolation and visibility over disconnection, and write down what they accept above their ceiling, because drawing the line too high slows everything, can create new holes and can stop the technology being used.

*[diagram]*
**concept**claim**method**artefact**example

**14 nodes, 14 edges**

- **An air-gapped Mac mini written in Perl** (example) No network, nothing installed, the OS's Perl, USB transfers: a design that buys technical debt.
- **Who, how, how sophisticated** (method) Threat agent, attack vector and sophistication come before any control.
- **Six tiers of attacker** (concept) Mistakes, bots, activists, organised crime, targeted commercial and insiders, elevated threats.
- **The toolkit asks, but does not define** (claim) DSIT's AI Risk Management Toolkit asks who the new threat actors are and points elsewhere for the answer.
- **The basics beat most of the ladder** (claim) Defending well against commodity threats makes a very hard target for all attackers (NCSC).
- **Few survive the top tier** (claim) Very few commercial organisations can withstand a determined state; deploy inside the customer's controls.
- **The Mac mini read against the ladder** (example) Worse for mistakes, equal for bots, mostly irrelevant to ransomware, no help at the top; adds a USB path.
- **Isolate, do not disconnect** (method) No inbound ports, outbound allowlist, containers, scanning, logs: visibility from mainstream tools.
- **Local versus cloud, the same mistake** (claim) On-premises for security often means more holes and fewer experts watching them.
- **Better than what they have, not beyond what they need** (claim) The customer's baseline is the bar; a line drawn too high is a disservice to both sides.
- **Threat-sized security, the vault** (artefact) Eight fictional startups, attack trees mapped to ATT&CK, a line for each, and a questionnaire.
- **Attack trees with ATT&CK on every branch** (method) Schneier's goal-rooted trees, each leaf a technique, a tier and a cost; the line draws itself.
- **Write down what you accept** (method) Above the ceiling is an accepted risk with a reason and a review date, not a failure.
- **Publish the threat model and ask** (method) One page, public, reviewed by people who have seen the attack before.

> The question is who, not how much. The article's thesis in one line.

> So the air gap protects against an attacker who, for a firm like this, does not really exist, and pays for it with the tools that defend against the attackers who do. The Mac mini, read against the ladder.

builds on [Every risk is already accepted. The only question is by whom, and for how long.](#every-risk-is-already-accepted); continued by [No server, by design: first I retired the database, now I am retiring the back end](#no-server-by-design), [Who will game the reading meter? Eight kinds of reader, nine ways to cheat, and the risks that will actually happen](#who-will-game-the-reading-meter), [Encrypted memory for agents that run somewhere else: sgit deployment patterns, from a Mac mini to Kubernetes](#encrypted-memory-for-isolated-agents), [Knowing when to stop: what experience gives people, and what we have to design into agents](#knowing-when-to-stop).

## [Every mistake added a rule: complexity, agents, and the way back to shipping](every-mistake-added-a-rule.md)

2026-10-08 · Agents & policySite & engineering

Founders who now work as engineers with agents often meet complexity not in their code but in the process around it, and answer each mistake with a rule, which grows the prompt, brings compaction sooner and breeds new mistakes; on a Wardley map that complexity is a position, custom-built process sitting where commodities already exist, and the way out is to make each piece a small, tested, shipped component that moves right and no longer needs a rule, with short sessions, memory as versioned files, security matched to assets and attack vectors, rules only for incidents and machines for enforcement, and shipping as the discipline that keeps blast radius and over-engineering under control.

*[diagram]*
**concept**claim**method**artefact**example**question

**17 nodes, 17 edges**

- **A verification where the code holds and the process breaks** (example) Agents write, verify and review in Cowork with ChatGPT; tests reproduce and 812 race attacks pass; six process failures recur.
- **Every mistake added a rule** (claim) Rules grow the prompt, compaction decides which survive, and rules contradict each other and the harness.
- **Complexity is a position on a map** (concept) Custom-built components sitting where the world already has products and commodities.
- **Map one: the custom-built blob** (artefact) The verification's process mapped: six hand-built components between the agents and unused files, hashes and git.
- **Map two: each piece moved right** (artefact) Short policy on disk, steps that finish before compaction, a run wrapper, committed scripts, an audit card, harm-only stops.
- **Rules for incidents, machines for enforcement** (claim) What a machine enforces holds; what attention enforces drifts; each failed rule is replaced by a stronger barrier.
- **Commoditise small chunks and let them compound** (method) Self-contained, shipped, testable components, each the base for the next, with blast radius kept small.
- **Ship, and stop** (method) Shipping means usable by somebody else, an agent included; half-baked by design; stopping is part of the method.
- **Small sessions, your own context** (method) Compaction chooses what to keep; debrief documents are compression you control; productive from the first prompt.
- **Memory is files, versioned** (concept) Briefs, reviews and indexes as a graph in git or vaults; Email-FS and Issues-FS between agents.
- **When complexity hits, slow down** (claim) If you are not getting faster, complexity is winning; you have time; pushing through slows you down.
- **Secure against the threat, not against everything** (method) Assets, attack vectors and what customers buy set the rigour; publish the threat model and ask.
- **Run it in five environments** (method) Local, air-gapped and three clouds each break a different assumption and show the bottlenecks.
- **Reverse-engineer the path to the destination** (method) Large designs need the five to ten paths that evolve into them; like a forest, early stages disappear.
- **Learn the engineering that exists** (method) CI, Kanban, patterns, nfrs.sgit.ai and coding.sgit.ai: cheaper to read than to rediscover.
- **Compaction, audit cards and what deserves a STOP** (question) Finish steps before compaction; audit the transcript afterwards; log form, stop for harm or a broken boundary.
- **The same lesson, one level up** (claim) Customers need simpler components first; if it fails in simple cases it struggles in complex ones; funding can mislead.

> Every rule added to fix one of them is one more custom component in the same place, which is exactly the loop my friend described. Why adding rules makes complexity worse, read on the map.

> If you are not releasing something, you are probably not solving problems at the right altitude. Shipping as the check on over-engineering.

builds on [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](#the-agent-team-as-it-runs), [Memory is not a spectator sport: how a web of open sites, graphs and vaults became the memory for sessions like this one](#memory-is-not-a-spectator-sport), [Git for things you cannot put on GitHub](#what-sgit-is), [Every risk is already accepted. The only question is by whom, and for how long.](#every-risk-is-already-accepted), [Footprint and blast radius: what the agent actually did, and what it would have cost](#footprint-and-blast-radius), [The bridge, followed to the end: what one local story is worth when it is kept as a graph](#the-bridge-followed-to-the-end), [Green does not mean live](#green-does-not-mean-live); continued by [No server, by design: first I retired the database, now I am retiring the back end](#no-server-by-design), [Pay after you read: how a reading meter became a working business model in one afternoon, one release at a time](#pay-after-you-read), [One article, five readers: a librarian, a cartographer, a historian, an explainer and a storyteller read the same piece](#one-article-five-readers), [A second reader the agent cannot skip: how two wrong emails became a gate on every draft](#a-second-reader-the-agent-cannot-skip), [Knowing when to stop: what experience gives people, and what we have to design into agents](#knowing-when-to-stop).

## [Liquid content needs water: liquefy the journalist's notebook, not the finished product](liquid-content-needs-water.md)

2026-10-07 · News & evidenceGraphs & knowledge

Liquid content, journalism built from datafied components, is right in its instincts, but what makes content liquid is the reporting inside it, so the way in is not a reinvention of newsroom norms but putting the experienced journalist and their existing workflow at the centre, liquefying their notebook into a story graph as they work, keeping the writing theirs because writing is how the story is found, bringing in experts paid for time and credibility, personalising by intersecting the reader's graph with the story's, keeping editorial direction rather than readers' tastes as the brief, and getting paid per use down the graph rather than only through advertising, subscriptions and licensing.

*[diagram]*
**concept**claim**method**question

**14 nodes, 14 edges**

- **Liquid content, as FT Strategies defines it** (concept) Content made of datafied atomic objects, quotes, events, dates, rather than finished products; clay kept wet.
- **What the guide gets right** (claim) Data journalism as the model, honest open questions, structure behind every front end, pay-per-query with agents.
- **Liquid needs water: the reporting** (claim) What makes content liquid is the notebook, interviews, documents and hypotheses, kept with their sources as a graph.
- **The limit of clay** (concept) By the time it is clay the sources and doubts are mixed in and gone; a graph keeps them.
- **The method already exists** (claim) Centuries of journalistic practice need tools, not reinvention; bring back the experienced journalists.
- **A desk built around the journalist** (method) Capture the notebook as it is kept, a custom interface per journalist, a graph they can see and correct.
- **Writing is how the story is found** (claim) The journalist writes the article and discovers the narrative; other projections come from the graph and are checked against it.
- **Experts a newsroom could rarely afford** (concept) Historians, analysts, professors, practitioners, paid for time and for the credibility they lend, credited in the graph.
- **The three 'is not's, with a graph underneath** (method) Archives can be liquefied, interfaces are built from the graph, and personalisation means graph intersection.
- **Personalisation as the meeting of two graphs** (concept) The reader's role, company, time, depth and language meet the story's claims; only there is something to say.
- **Readers' tastes are not the brief** (claim) Prioritising what readers click is the path to clickbait; readers pay for a publication's judgment and direction.
- **Paid per use, down the edges** (claim) Beyond retention, ads and licensing: per use, per agent question, per claim to who found it, per citation.
- **The structure has a value to whoever reads it** (question) Publishers did the indexing work for search engines for free; structuring for AI engines should be priced.
- **Start with one journalist** (method) One topic, one reporter's notebook, one desk, one expert, one extra projection, then liquefy what the next story touches.

> If content is to be liquid, it needs water in it, and the water is not the format. Where the article departs from the guide: liquidity comes from the reporting, not the product.

> Part of the skill of a journalist is writing the article, because writing it is how they discover the narrative. Why AI should not write everything.

builds on [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](#introducing-fractal-semantic-graphs), [The future of news is the story vault, not the paywall](#future-of-news-story-vault-not-paywall), [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](#custom-uis-are-not-the-exception), [The bridge, followed to the end: what one local story is worth when it is kept as a graph](#the-bridge-followed-to-the-end), [How much of this did I write? The numbers behind twenty articles in four weeks, and what the input actually was](#how-much-of-this-did-i-write), [The reader was always the product: a corrected history of how news got into this mess](#how-news-got-here), [Sixteen thousand fetches, ten clicks, and a token bill nobody is sending: the case for paying publishers to be easy to read](#token-bill-nobody-is-sending); continued by [One article, five readers: a librarian, a cartographer, a historian, an explainer and a storyteller read the same piece](#one-article-five-readers).

## [The bridge, followed to the end: what one local story is worth when it is kept as a graph](the-bridge-followed-to-the-end.md)

2026-10-07 · News & evidenceGraphs & knowledge

Played out as a simulation on a story vault, one local bridge closure shows the value of journalism as getting a disputed fact right and keeping it right: newsworthy on five days but needed on fifty-seven, used through Reader Skills by readers whose own graphs meet the story graph at shared anchors and who decide better with it, bought by institutions and agents who need the same claims, cheaper for agents than searching, and paid for in small amounts that walk back down the claims to the reporter, the paper and the residents whose evidence the graph names.

*[diagram]*
**concept**claim**method**artefact**example

**12 nodes, 12 edges**

- **A bridge closes; the council says one week** (example) A fictional town's main crossing shuts for urgent repairs; the official estimate is a week.
- **The journalism is getting the date right** (claim) The contract says three weeks, the engineer five to seven; the reporter finds both and the paper runs the contradiction.
- **Each correction supersedes the last** (method) The graph keeps every estimate with its date, so it can say what was believed on any day and why.
- **Newsworthy on five days, needed on fifty-seven** (claim) The paper leads with the story five times; readers need its current state every day it is closed.
- **Each reader's graph meets the story** (concept) Home, school, routes and customers held on the reader's device, joined to the claims at shared anchors.
- **A parent, a café owner, a plumber** (example) The same claims become a walking route, a stock plan and a job schedule.
- **Better decisions, counted** (claim) A club booked in time, £640 of stock not wasted, £1,200 of relief claimed, nine hours of driving saved.
- **Without it: stale pages, rumours, nobody accountable** (claim) The council page says a week for nine days, a group says Friday, TV covers day one and day forty-six.
- **Buyers who do not read the paper** (concept) Highways teams, investors and national desks need the same graph for regional and national decisions.
- **Agents spend less and are right** (claim) Searching costs about $377 over the closure and finds the stale page; asking the newsroom costs about $54.
- **£2,707, walked back to the sources** (artefact) Small amounts from 1,596 readers and businesses plus institutions; 35% to the reporter, £203 to a resident.
- **The simulation as a vault** (artefact) Every figure computed from written assumptions by a build script, published with its read key.

> An article is written once. A maintained claim, kept current until the bridge opens, is a service. Why the value of a local story outlives its news cycle.

> As agents start planning school runs, deliveries and site visits for people, the cheapest thing they can buy is an accurate, maintained, accountable source. Why agents should pay for local journalism.

builds on [Story vault underneath, Reader Skills on top: why local journalism has the most to gain](#story-vault-meets-reader-skills); continued by [The agent is the reader: why agents will pay for graphs, personas and signed claims, because it is cheaper than not paying](#the-agent-is-the-reader), [A meter in the browser: a penny a page, a history you keep, and a site that picks for you](#a-meter-in-the-browser), [The waiting room knew first: a live local story, and the gap where local information used to be](#the-waiting-room-knew-first), [Every mistake added a rule: complexity, agents, and the way back to shipping](#every-mistake-added-a-rule), [Liquid content needs water: liquefy the journalist's notebook, not the finished product](#liquid-content-needs-water), [Story vault underneath, Reader Skills on top: why local journalism has the most to gain](#story-vault-meets-reader-skills).

## [Story vault underneath, Reader Skills on top: why local journalism has the most to gain](story-vault-meets-reader-skills.md)

2026-10-07 · News & evidenceGraphs & knowledge

Markus Franz's Liquid Utility proposes Reader Skills that help people understand, update, relate, compare, follow and act on journalism; the story vault keeps reporting as a versioned graph of claims tied to hashed evidence; put together, each skill is an operation on the graph and each safeguard he asks for is a property the graph already has, his bridge closure becomes a graph in which one supersede edge is the update, the alert and the correction, and his emphasis on locality supplies what the vault's economics had not mapped: local contributors and local journalists sit where trust is strongest, stories travel up to national and international outlets, and if every use pays back down the chain of claims it rests on, small payments from many people fund the reporting nearest to them.

*[diagram]*
**concept**claim**method**artefact**example**question

**13 nodes, 13 edges**

- **Liquid Utility** (concept) Markus Franz: trusted journalistic knowledge plus reusable methods and tools, to help someone understand, follow or act.
- **Six Reader Skills** (concept) Understand, Update, Relate, Compare, Follow, Act: bounded capabilities a reader uses directly.
- **The story vault** (concept) Claims tied to hashed evidence, versioned, superseded rather than deleted; the article is one projection.
- **What we know, and what we can help someone do** (claim) Markus Franz's reply: the vault answers why it can be trusted, the skills answer what it can reliably help someone do.
- **Each skill is an operation on the graph** (method) Update is a diff between versions, Follow a subscription on claims, Relate a join held on the reader's side.
- **His safeguards are graph properties** (claim) Corrections as supersede edges, protected sources flagged at the node, freshness for could-not-check.
- **The bridge closure as a graph** (example) One supersede edge is the update, the alert and the correction at once; the reader's route stays on the reader's side.
- **Local is where the trust is** (claim) Everything that touches the day is local; readers can check local reporting themselves, so trust and brand form there.
- **The local contributor is a node** (concept) Residents and local sources are named or flagged, linked to the claims their evidence supports, and verified.
- **Every use pays back down the chain** (method) National and international stories that rest on local claims pay for them per use; shares reach the contributor.
- **Is this still current?** (artefact) The verification API: a paid, maintained answer about a claim, and how a local newsroom gets paid for being right.
- **Trust, use, payment, reporting, evidence, trust** (claim) Small payments from many people about the things nearest to them fund the next local story.
- **One topic, one vault, one service, one ledger** (question) Markus's tightly scoped service, kept as a story vault, with contributors recorded and the ledger published.

> Over a pile of articles, Update is a summarisation problem. Over a story graph, it is a diff. Why the story vault makes Reader Skills dependable.

> Use it, and pay the people who found it out. The clause the monetisation adds to Markus Franz's closing line.

builds on [The future of news is the story vault, not the paywall](#future-of-news-story-vault-not-paywall), [The reader was always the product: a corrected history of how news got into this mess](#how-news-got-here), [The bridge, followed to the end: what one local story is worth when it is kept as a graph](#the-bridge-followed-to-the-end); continued by [The waiting room knew first: a live local story, and the gap where local information used to be](#the-waiting-room-knew-first), [The bridge, followed to the end: what one local story is worth when it is kept as a graph](#the-bridge-followed-to-the-end).

## [Zoom into an agent's behaviour policy and you find the business logic](the-behaviour-policy-is-the-business-logic.md)

2026-10-07 · Agents & policy

The first rules written for an agent are mechanical and vendors enforce them well, but every layer above them is the company's own business logic: how a function is done, the steps a process goes through, who a client is right now, and what the company is for; much of that logic was never written down because software enforced it by omission, and agents working through APIs bypass that; a behaviour policy built in layers, each refining the one below with its own owner, can hold it, can count how much of it is backed by a control, by an accepted risk or by hope, and gives vendors a written rule to enforce and a number to move, which is what lets the business hand work to agents and scale.

*[diagram]*
**concept**claim**method**artefact**example**question

**14 nodes, 14 edges**

- **The bottom layers are mechanics** (concept) Own account, secrets held by the platform, tools switched off, sending needs a person: boundaries vendors enforce well.
- **send_message ran with no prompt** (example) The measured Gmail deployment: thirty tools, sending unprompted, trashing behind an approval. Mechanics need measuring.
- **Above the mechanics is the business** (claim) Function, process, relationship and organisation layers, each a set of rules a manager would say out loud, each with its own owner.
- **Vendors cannot model each customer's business** (claim) To scale they build what is the same for everybody; the business layers differ per company and are often unwritten.
- **Software was the law** (concept) Approval chains, RBAC and workflows encoded the rules; a missing button was a control.
- **Agents work through the API, not the screen** (claim) The rule the interface enforced by omission is no longer enforced unless it is written down.
- **Policies inside policies** (method) Each layer refines the one below inside the room it allows, from tool permissions up to what the company is for.
- **Shared facts, own formulas, declared bridges** (concept) The ABP vocabulary's three layers: customers extend it in their own vault without changing the shared one.
- **Control, accepted risk, or hope** (method) Each rule is backed by a boundary, governed by a named acceptance with an expiry, or resting on hope; the counts are the finding.
- **Five, six and six of seventeen** (example) In the fictional firm the platform layer is all control and the organisation layer all hope.
- **A vendor control moves one written rule** (method) Send gateways, content checks, ledger approvals and blocked-recipient lists each move a rule from hope or acceptance to control.
- **Frameworks already ask for the description** (artefact) AI BCF RG.2 asks that what an autonomous system does is described; AC.3 asks for a named owner.
- **The upper layers read like skills** (claim) A skill says how; a policy layer says what is allowed, who owns it and what stands in the way. Together they codify the business.
- **A real inbox, layered and counted** (question) Write the upper layers above the measured Gmail deployment, publish the counts, then again with a vendor's control in the path.

> The rule that the user interface enforced by omission is no longer enforced, unless somebody writes it down and something enforces it. Why agents force business logic out of software and into policy.

> A control attached to a written rule is worth more than one switched on in general, because the customer can see what it bought. Why the behaviour policy is a good integration point for vendors.

builds on [Six agents, one inbox: what a real multi-agent setup taught me about access policies](#six-agents-one-inbox), [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](#introducing-fractal-semantic-graphs), [Every risk is already accepted. The only question is by whom, and for how long.](#every-risk-is-already-accepted), [An open AI governance framework, and what its licence let us build](#ai-baseline-control-framework); continued by [Where the platform draws the line: Microsoft Execution Containers, the shared responsibility model for agents, and the business logic above it](#where-the-platform-draws-the-line), [The same argument, in our words: Satya Nadella on models as insider risks, translated into the language of RiskMandate](#the-same-argument-in-our-words), [One article, five readers: a librarian, a cartographer, a historian, an explainer and a storyteller read the same piece](#one-article-five-readers), [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](#riskmandate-ten-questions), [Hope or enforcement: one customer service agent, three designs, and who keeps each promise](#hope-or-enforcement).

## [A locked-down desktop for an agent, by the minute, is still hard to rent](an-agent-desktop-by-the-minute.md)

2026-10-07 · Agents & policyStartups & strategy

A desktop safe to hand to an agent needs isolation, an egress allowlist, secrets kept outside, its own identity, a live view, a record, a clean reset, billing that follows the work and the right operating system; in October 2026 each exists somewhere and no product we read has all nine; Linux sandboxes come closest, with key controls in beta, Windows agent desktops arrived in June, and macOS cannot be leased for less than 24 hours under Apple's licence, which also limits leased Macs to developer services; because prompt injection is not solved the desktop has to be the barrier, so the proposal is one mandate per task, a fresh desktop per task by operating system, and a vault outside every desktop, paid for at first by startup programmes listed with how to apply.

*[diagram]*
**concept**claim**method**artefact**example**question

**14 nodes, 14 edges**

- **A desktop per agent, billed by the minute** (question) Can a locked-down desktop be rented for the two to eight hours a day an agent uses it?
- **Nine properties of a locked-down desktop** (concept) Isolation, egress allowlist, secrets outside, own identity, live view, record, reset, billing that follows work, the right OS.
- **The desktop is the agent's grant** (concept) Read through the Agent Behaviour Policy, the box keeps what the agent can reach close to what the task needs.
- **No product has all nine** (claim) Nine products read from their own documentation on 7 October 2026; each property exists somewhere.
- **Linux sandboxes come closest** (example) E2B and Daytona: microVMs or VMs, deny-by-default egress, proxy-held secrets, per-second billing; some controls in beta.
- **Windows agent desktops arrived in June** (example) Windows 365 for Agents and Amazon WorkSpaces for AI agents, both generally available in June 2026.
- **macOS leases last at least a day** (claim) Apple's licence requires 24-hour leases, so two hours of work buys a day, at up to $1,040 a month on AWS.
- **Leased Macs are for developer services** (question) Whether a general agent desktop on a leased Mac fits Apple's Permitted Developer Services is a legal question.
- **Native computer use and governed computer use do not meet** (claim) The desktop app runs on a person's Pro or Max machine; the API tool needs a Linux environment you supply.
- **Prompt injection is not solved** (claim) About 1% success in Anthropic's own browser tests still represents meaningful risk, so the box must be the barrier.
- **One mandate per task, a fresh desktop per task** (method) Linux by default, Windows for Windows tools, macOS only for development by the day, configured from the task's mandate.
- **A vault outside every desktop** (method) Outputs, setup, mandate and footprint go to an encrypted sgit vault the desktop can append to and cannot rewrite.
- **Startup programmes, verified with how to apply** (artefact) E2B, Daytona, Scaleway, AWS, Microsoft, Google, Cloudflare, Modal and Anthropic, with amounts, criteria and links.
- **What only running it will tell** (question) Takeover reliability, paused state over days, allowlist breakage, recording cost, Windows against Linux on one task.

> The Mac is not expensive per hour; it is expensive because the hour you can buy is a day. Why the macOS bars in the cost figure are long.

> The model's own defences reduce how often that matters, and do not replace it. Why the desktop, not the model, is the barrier.

builds on [Why my agents do not run on my laptop: chat, Cowork and Code in the cloud, a vault as the shared drive, and the two walls an operating system has](#why-my-agents-do-not-run-on-my-laptop), [The Mandate Stack: a multi-agent system in production, layer by layer](#the-mandate-stack), [Where is the why? A permission prompt asked me to decide, and kept the reason](#where-is-the-why); continued by [A Mac of the agent's own: a business plan for agent desktops, what Apple's licence allows, and three behaviour policies](#a-mac-of-the-agents-own), [Encrypted memory for agents that run somewhere else: sgit deployment patterns, from a Mac mini to Kubernetes](#encrypted-memory-for-isolated-agents).

## [An open AI governance framework, and what its licence let us build](ai-baseline-control-framework.md)

2026-10-07 · Graphs & knowledgeAgents & policy

The AI Baseline Control Framework is a practical, deployer-focused set of twenty AI governance controls in five categories and three types, each with a why and a how and a mapping to the NIST AI RMF, ISO/IEC 42001 and the EU AI Act; its Access category covers what an AI system can reach, which the three it maps to do not; its CC BY-SA licence and CSV export let it be converted on the day into a semantic graph with an ontology, a taxonomy, linked data, documents and a browser database, joined by id to a graph of the AI Act, and walked as a fractal graph from the framework down to a paragraph of law, which surfaced findings the list does not state and kept every addition labelled apart from the source.

*[diagram]*
**concept**claim**method**artefact**example**question

**15 nodes, 15 edges**

- **AI BCF: twenty controls for deployers** (artefact) Five categories, three types, a why and a how per control, mapped to NIST AI RMF, ISO/IEC 42001 and the AI Act; v1.0, 2 October 2026.
- **Baseline, Tier II, Trigger** (concept) Trigger controls apply only when a stated condition holds, which keeps the framework proportionate across organisation sizes.
- **The Access controls have no equivalent in the three** (claim) AC.1 to AC.4: access reviews, named identities, accountable owners and the access model for AI systems themselves.
- **Grant, mandate and owner** (concept) The Agent Behaviour Policy's words for what an agent can reach, what it may do, and who answers for it.
- **CC BY-SA 4.0 says yes in advance** (concept) Share and adapt for any purpose with credit, changes indicated and the same licence on what is shared.
- **ShareAlike keeps the tools open** (claim) A framework is worth the tools built on it; ShareAlike keeps shared tools as open as the framework.
- **A CSV export turned a reading into a dataset** (example) One row per control, sources in one column, a URL per control: the input for the whole conversion.
- **One CSV in, five shapes out** (method) A deterministic build writes a graph, an ontology, a SKOS taxonomy, JSON-LD and Turtle, eighty documents and a SQLite database.
- **Every edge says where it came from** (method) Source, structure, parser-derived, derived-join and overlay, shown in every view so additions are never mistaken for the framework.
- **Five altitudes, one grammar** (example) The graph view walks from the framework to a category, a control, a cited clause and the paragraph of the AI Act it resolves to.
- **Two vaults joined by matching ids** (method) AI Act citations resolve to the Regulation Graph's nodes because both graphs keep the same grammar.
- **The law links controls listed separately** (claim) The AI Act's own cross-references connect four pairs of Comply controls by seven paths.
- **Four cited articles were amended in 2026** (claim) Articles 4, 5, 27 and 50, amended by Regulation (EU) 2026/1744; GV.3, CM.1, CM.2 and CM.4 are the controls to re-read first.
- **SQL and triples in the browser** (artefact) sql.js builds the tables in the page; a triple console asks the same graph from either end through declared inverses.
- **If the framework publishes its own graph** (question) It should be authoritative, and this vault should be superseded by it rather than merged into it.

> for now there is only Export as CSV on https://aibcf.org/controls/ on the top right. Good suggestions! The framework author's reply, and the input the whole conversion was built from.

> A licence that permits adaptation in advance means each of those can be built, and shared, without asking. Why an open licence matters more for a control framework than for most documents.

builds on [Six agents, one inbox: what a real multi-agent setup taught me about access policies](#six-agents-one-inbox), [The identity we wanted to give the agents: a week of design, the line in Google's terms, and why login plus secrets is still too hard](#the-identity-we-wanted-to-give-the-agents), [Where is the why? A permission prompt asked me to decide, and kept the reason](#where-is-the-why), [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](#introducing-fractal-semantic-graphs), [Every risk is already accepted. The only question is by whom, and for how long.](#every-risk-is-already-accepted), [Code review as a fractal semantic graph: source code is already one, and the review should read every layer of it](#code-review-as-a-fractal-semantic-graph); continued by [Zoom into an agent's behaviour policy and you find the business logic](#the-behaviour-policy-is-the-business-logic).

## [Where is the why? A permission prompt asked me to decide, and kept the reason](where-is-the-why.md)

2026-10-07 · Agents & policy

A permission prompt that asks a person to approve an agent's grant change without saying which session asks, why, what changes, what it could cost and what a no would do, leaves the person a choice between breaking the work and owning a decision they could not judge; read through the Agent Behaviour Policy it is a mid-session grant change whose barrier is a human judgement as strong as the information given, and whose risk lies in the combination with what the session already holds; courts and regulators across medicine, contract, data protection and automated decisions mostly put the duty to disclose on whoever asks and deny weight to token sign-offs, while in practice blame lands on the nearest person; the fixes that worked, purpose strings, number matching and context, refusal as easy as acceptance, all put the reason or the context into the prompt; so the proposal is a why card that carries the reason, the change in reach, the cost, the decline path and a record, and becomes a risk acceptance when the risk rises.

*[diagram]*
**concept**claim**method**example**question

**14 nodes, 15 edges**

- **Three fields, two buttons, no reason** (example) Owner, repository, access; Decline or Allow once; not which session, which step, which instruction, what changes or what a no costs.
- **Decline breaks the work, Allow buys accountability** (claim) Both offered answers carry an unstated cost; the answer that removes both, a reason, was not on the screen.
- **A prompt is a grant change mid-session** (concept) The question is what the session becomes once it holds this and what it already holds, not whether the resource is safe.
- **Read is small, write is a publishing channel** (claim) Read of a public repository adds little; write to it from a session holding confidential data adds an exfiltration path.
- **A barrier that is a person** (claim) Enforced by the host, so the agent cannot click it; as strong as the information the person is given.
- **93% approved, 13.6% caught** (example) Vendor figures: most agent prompts are approved, and planted dangerous commands are rarely caught, less so as prompts pile up.
- **Fewer prompts leaves the hard ones** (claim) Sandboxing and classifiers remove the easy prompts; the remaining ones need the reason most, and the classifier's own misses are about consent covering the action.
- **The asker must disclose** (concept) Montgomery, the red hand rule, Berman and Nguyen, the Consumer Rights Act and GDPR Article 7 put the duty to make information usable on whoever asks.
- **A token sign-off is not a human decision** (concept) WP251 and SCHUFA: oversight must be meaningful, and a determining machine output stays automated even when a person signs.
- **Blame lands on the nearest person** (claim) Elish's moral crumple zone and the Post Office Horizon cases: in practice the click is the record, and it carries the person's name.
- **The fixes put the why into the prompt** (example) Apple's required purpose strings, Microsoft's number matching with app and location, the CNIL's refusal as easy as acceptance.
- **The why card** (method) Who asks, why with the instruction quoted, what changes, what it could cost, if you decline, scope and record; allow for task, decline and continue, ask, park.
- **When the risk rises, a risk acceptance** (method) A grant change that raises the session's blast radius names who accepts it, for how long and what ends it, and is recorded as such.
- **Which session asked, and why** (question) Not known: the prompt did not say; nor whether its fields are configurable; vendor figures not replicated; not legal advice.

> A boundary whose enforcement is a human judgement is exactly as strong as the information that human is given. Why the prompt is a real barrier and a weak one at the same time.

> In practice, the click is the record, and the click has the person's name on it. The gap between where the law puts the duty and where the blame lands.

builds on [Footprint and blast radius: what the agent actually did, and what it would have cost](#footprint-and-blast-radius), [Every risk is already accepted. The only question is by whom, and for how long.](#every-risk-is-already-accepted), [The Mandate Stack: a multi-agent system in production, layer by layer](#the-mandate-stack), [Six agents, one inbox: what a real multi-agent setup taught me about access policies](#six-agents-one-inbox), [Before you give an agent a connector, give the connector a twin](#connector-twin-before-you-deploy-an-agent), [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](#ultimate-insider-three-collisions), [Why my agents do not run on my laptop: chat, Cowork and Code in the cloud, a vault as the shared drive, and the two walls an operating system has](#why-my-agents-do-not-run-on-my-laptop), [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](#the-agent-team-as-it-runs), [A personal agent that keeps your secrets: the 2026 agents read through behaviour policy and encryption, and a privacy-first design on vaults, enclaves and the browser](#a-personal-agent-that-keeps-your-secrets); continued by [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](#riskmandate-ten-questions), [Agency is not a yes: a scale for human and agent decisions, from rubber stamp to the reviewer who fixes the source](#agency-is-not-a-yes), [A locked-down desktop for an agent, by the minute, is still hard to rent](#an-agent-desktop-by-the-minute), [An open AI governance framework, and what its licence let us build](#ai-baseline-control-framework).

## [The Mandate Stack: a multi-agent system in production, layer by layer](the-mandate-stack.md)

2026-10-06 · Agents & policyGraphs & knowledge

RiskMandate runs its business with about fifteen agents and one person, and the agent that runs its CRM described the setup as eight layers: rented compute and channels, encrypted vaults as shared memory with mail as files and append lanes, a vault per domain, semantic graphs over people, contexts, teams and policies, a scheduled conductor with security first and last, written behaviour policies with grant, mandate, gap and barrier, and a human who holds the one irreversible step; the world writes in from the left and nothing leaves without the person on the right; the loop that makes it hold treats the draft as a release candidate for the whole pipeline with the recipient's reply closing it; two Wardley maps show what the team is commoditising (shared memory, the CLI, on encrypted storage) and what it is productising (the policies, the graphs); and the published record of agent projects that stall for unclear value, cost, trust, security and governance is read last, each reason mapped to the mechanism that answers it; the name is a working one and nothing planned is included.

*[diagram]*
**concept**claim**method**example**question

**17 nodes, 23 edges**

- **One that runs** (example) About fifteen agents and one person run RiskMandate's relationships, research, writing and events every few hours; the briefing was written by the agent that runs the CRM.
- **The world writes in, the person sends** (concept) Email, the subscribe form, other teams' agents and an event extension enter from the left as data; the person enters from the right through Claude and Gmail; nothing leaves unsent by them.
- **Compute and channels are rented** (concept) Cowork and Claude Code cloud sessions; one Workspace identity cut into roles; the send row has no agent in it.
- **Shared memory is files the host cannot read** (method) Encrypted, versioned vaults cloned per session; agent mail as files in each other's mailroom; append lanes for outsiders who hold no key.
- **A vault per domain and per mission** (method) One vault for relationships, one per project with its own owner, policy and key holders; least privilege applied to context.
- **Every record is a node with typed edges** (concept) People, their work, interests and the team's materials; contexts as graphs over the same people; the team's requests, each ABP and the custody register as graphs.
- **A missing edge is a reason not to send** (claim) An interest met by a material is a reason to send it; an interest with no edge is something to make or a reason not to email; nudges come from edges, not lists.
- **A conductor with security at both ends** (method) Open and lock, security, drafts, inbox, briefs, CRM, mission, research, dev, security, a card to the human, stop; the order is a design decision.
- **One written mandate per agent** (method) Grant, mandate, gap and barrier in one grammar; roles split the risk; drafts only; a security hold; secrets never in files; a card per session; a custody register.
- **One human holds the irreversible step** (claim) No agent sends, replies or forwards; everything below can be wrong and still be caught at the draft.
- **The vault is an app platform, not storage** (concept) A friction becomes a tool as HTML in the same session, deployed into the vault, used and corrected; tools compound down to an interface for one person; the loop stops when a piece of work no longer calls for a tool.
- **The draft is the release candidate** (concept) The whole pipeline has run before the person sees the draft; reviewing it is QA on the system and where the thinking happens; the recipient's reply closes the loop.
- **Mistakes traced to captured data, an edge or the model** (method) Every fact carries source, capture method and hash; the cause is fixed where it came from; model error reported as the rarest of the three.
- **Commoditise the memory, productise the mandate** (claim) Two Wardley maps, from outside and inside: shared memory and the sgit CLI pushed toward commodity on encrypted storage; the policies and the graphs pulled from genesis toward product. Placements are claims.
- **Five reasons it holds** (claim) Small versioned control surface; the human at the irreversible step; state as files; meaning on the read path; everything leaves a trail.
- **A working name, and what is not in it** (question) The Mandate Stack carries the mandate and the layers but not the human who sends; nothing planned is included; unsigned authorship, no key revocation, policy-only barriers, and who gives the mandate over information stay open.
- **The record is of pilots that stall** (claim) Gartner, S&P Global, McKinsey, Deloitte, KPMG and Forrester, June 2025 to July 2026: cancelled, paused or trapped in pilot, for unclear value, cost, trust, security and governance; the same surveys show agents shipping where the workflow stops at the draft.

> Many small agents, one written mandate each, everything connected as a graph, one human who sends. The one-line version of the pattern, and the part the working name leaves out.

> The record is of pilots that stall, not of a technology that cannot ship. The fair reading of the surveys, kept for the end.

builds on [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](#the-agent-team-as-it-runs), [Why my agents do not run on my laptop: chat, Cowork and Code in the cloud, a vault as the shared drive, and the two walls an operating system has](#why-my-agents-do-not-run-on-my-laptop), [Six agents, one inbox: what a real multi-agent setup taught me about access policies](#six-agents-one-inbox), [Before you give an agent a connector, give the connector a twin](#connector-twin-before-you-deploy-an-agent), [The identity we wanted to give the agents: a week of design, the line in Google's terms, and why login plus secrets is still too hard](#the-identity-we-wanted-to-give-the-agents), [Git for things you cannot put on GitHub](#what-sgit-is), [Replicating the agentic inbox: a walkthrough from one Claude session to a team of agents that never press send](#replicating-the-agentic-inbox), [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](#custom-uis-are-not-the-exception), [Memory is not a spectator sport: how a web of open sites, graphs and vaults became the memory for sessions like this one](#memory-is-not-a-spectator-sport), [Seven vaults, one method](#seven-vaults-one-method), [A supply chain of vaults: how GenAI, open data and small custom tools could bring the price of food down](#supply-chain-of-vaults), [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](#introducing-fractal-semantic-graphs), [If somebody built a company on code review: how I would do it, and why it is only now possible](#if-somebody-built-a-company-on-code-review), [Code review as a fractal semantic graph: source code is already one, and the review should read every layer of it](#code-review-as-a-fractal-semantic-graph), [Footprint and blast radius: what the agent actually did, and what it would have cost](#footprint-and-blast-radius), [Every risk is already accepted. The only question is by whom, and for how long.](#every-risk-is-already-accepted), [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](#ultimate-insider-three-collisions), [How much of this did I write? The numbers behind twenty articles in four weeks, and what the input actually was](#how-much-of-this-did-i-write), [The wall under the reply: end an email with the state of the thread, not the thread](#the-wall-under-the-reply), [Twenty sites in fifteen days, and what that did to the writing](#nineteen-sites); continued by [One article, five readers: a librarian, a cartographer, a historian, an explainer and a storyteller read the same piece](#one-article-five-readers), [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](#riskmandate-ten-questions), [A locked-down desktop for an agent, by the minute, is still hard to rent](#an-agent-desktop-by-the-minute), [Where is the why? A permission prompt asked me to decide, and kept the reason](#where-is-the-why).

## [Why my agents do not run on my laptop: chat, Cowork and Code in the cloud, a vault as the shared drive, and the two walls an operating system has](why-my-agents-do-not-run-on-my-laptop.md)

2026-10-06 · Agents & policyVaults & method

No model runs on the author's laptop because a process there runs as the author and the operating system has no boundary inside a user account between an agent and the SSH keys, cloud credentials, password manager session, browser cookies and files; the desktop agents' prompts and sandboxes are settings enforced by the process they constrain, and fifteen months of incidents show what a mistake or an injected instruction reaches; so the agents run on four cloud surfaces chosen by reach, Claude chat with nothing connected, Cowork with no repositories, Claude Code with one repository and an allowlist, ChatGPT with no assets, and a vault the host cannot read is the shared drive between them, with keys handed per session; the trade-offs are accepted, three wishes remain, identity, secrets and a key pair per agent, and the caveat is that a dedicated machine with separate accounts is a different model to be reported on later.

*[diagram]*
**concept**claim**method**example**question

**12 nodes, 13 edges**

- **Why not run it on the laptop** (question) No business need for an offline model; the one thing a local agent would need to offer, isolation better than the cloud's, is the thing none offers.
- **An operating system has two hard walls** (claim) The kernel and the user account; inside one account there is no boundary between an agent and the keys, credentials, sessions and files the account can read.
- **The desktop agents add settings, not boundaries** (claim) Approval prompts, allow lists and process sandboxes are enforced by the process they constrain; the vendor's own docs list credential files as the default read scope and call the boundary a permission prompt.
- **Fifteen months of incidents** (example) Deleted home directories and drives, repositories executing before the trust prompt, hidden instructions exfiltrating secrets, tens of thousands of exposed self-hosted gateways, a local sandbox escape reaching SSH keys; every one fixed, the pattern remaining.
- **The lethal trifecta is the laptop's default** (concept) Private data, untrusted content and a way out are all present on a laptop by default: the account, every file read, and the user's network.
- **Four places the agents run** (method) Claude chat with nothing connected for thinking; Cowork in the cloud with no repositories for the team; Claude Code on the web with one repository and an allowlist for code; ChatGPT with no assets as a second model.
- **The vault is the shared drive** (method) Encrypted on the agent's side, keys handed per session out of band, clone or pull, work, leak check, commit, push; the next session pulls; the laptop passes keys and nothing else.
- **Same mandate, two deployments** (claim) On the laptop the grant is the account and barriers are expectations; in a cloud session the grant is small and barriers are boundaries; injection is stopped in neither, and what it reaches differs.
- **What it costs** (claim) No agents without a connection, a key per session by hand, no per-session secrets in Cowork so one vault per scope, chat without cross-chat memory, two products with two flows; accepted.
- **Identity, secrets and a key pair per agent** (question) An agent identity the platform knows with signed commits; secrets injected and revocable per agent; a key pair per agent; each exists in pieces on this site and none as a product feature.
- **The dedicated machine is a different model** (question) A second machine with separate accounts and nothing of the author's on it has an empty wall marked that user; closer to the cloud model; to be run and reported on later, not before.
- **What exists and what does not** (question) The setup runs and the team's twelve-agent version runs; the three wishes, a desktop agent running as a separate user by default, and the dedicated-machine report do not exist yet.

> A mistake inside a boundary is a bad afternoon. The same mistake inside "me" is an incident. Why hallucination is the wrong word for what goes wrong with a local agent.

> The barrier that holds is the small grant, not a cleverer filter. Prompt injection is not prevented by the cloud; what the injected instruction can reach is.

builds on [Six agents, one inbox: what a real multi-agent setup taught me about access policies](#six-agents-one-inbox), [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](#the-agent-team-as-it-runs), [Footprint and blast radius: what the agent actually did, and what it would have cost](#footprint-and-blast-radius), [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](#ultimate-insider-three-collisions), [A personal agent that keeps your secrets: the 2026 agents read through behaviour policy and encryption, and a privacy-first design on vaults, enclaves and the browser](#a-personal-agent-that-keeps-your-secrets); continued by [Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan](#authority-outside-the-model), [A Mac of the agent's own: a business plan for agent desktops, what Apple's licence allows, and three behaviour policies](#a-mac-of-the-agents-own), [How I work with Claude: one session per topic, agents with names, and memory you curate](#how-i-work-with-claude), [Encrypted memory for agents that run somewhere else: sgit deployment patterns, from a Mac mini to Kubernetes](#encrypted-memory-for-isolated-agents), [A locked-down desktop for an agent, by the minute, is still hard to rent](#an-agent-desktop-by-the-minute), [Where is the why? A permission prompt asked me to decide, and kept the reason](#where-is-the-why), [The Mandate Stack: a multi-agent system in production, layer by layer](#the-mandate-stack).

## [The deck I could not download: an author-first home for presentations, as a business plan somebody else can build](the-deck-i-could-not-download.md)

2026-10-06 · Startups & strategyVaults & method

A reader is sold a 30-day trial and a monthly subscription for a single presentation while the deck's author receives nothing, under an uploader agreement that grants a royalty-free, sublicensable licence to monetise and train models on the work; the platform persists through fifteen years of embeds and links, which is inertia; an author can ask today for counts and recipients under the right of access and, in some EU states, for revenues under the copyright transparency duty; and the service the author would have chosen can be built on this site's primitives: every author's decks in a vault the host cannot read, access decided by keys, decryption in the browser, an attested enclave for the one step that needs plaintext, seven separable roles, pay once with 85% to the author on a ledger they can recompute, provenance as the product; the plan is published as a vault with a working mock, with its economics worked and the card-fee floor stated as the hard row.

*[diagram]*
**claim**method**artefact**example**question

**13 nodes, 16 edges**

- **One download, one subscription decision** (example) A 30-day trial then £10.99 a month ($11.99 in the US) for a single file, no one-off option unless the author switched a setting on, which was reported as off by default when the paywall arrived in September 2021.
- **What the author agreed to** (claim) The uploader agreement grants a royalty-free, sublicensable licence to monetise, charge for, advertise against and train models on the work, and does not entitle the author to any payment; the same company forbids users from training on the content.
- **Three complaints, and the one that is not** (claim) The reader is sold a subscription for one file; the author has no say and no share; the author does not know where the work went. The licence allows all of it, so the complaint is that the service the author would have chosen does not exist.
- **Why it has not been replaced** (claim) Fifteen years of embeds, backlinks and search ranking; about forty million visits a month, mostly from search; past success breeds inertia, and the authors' links are what the incumbent holds.
- **What an author can ask for today** (method) Switch the download setting on; send a right-of-access request for the counts and the recipients, with the EDPB's derived-data guidance and the Court's ruling on naming recipients; in some EU states, the copyright transparency duty on all revenues generated; the UK did not implement it.
- **The author holds the keys** (method) Every author's decks in a vault the host cannot read; a publishing key bound to a passkey; a content key per deck; a read key for what is free; a receipt turned into a ten-minute key; a revocable grant; decryption in the browser; an enclave for the one step that needs plaintext.
- **Seven roles, no single owner** (method) Storage host, key service, unlock service, payments, identity and provenance, the front, add-ons; no party holds more than one of the content, the keys and the money; each can be provided per country, profession or company.
- **Read free, pay once, grant and revoke** (method) A read is a count on the author's ledger; a one-off payment becomes a receipt the enclave turns into a short key; a grant is wrapped to a recipient and revoked by re-keying; a downloaded file is the reader's and the plan says so.
- **Near-zero marginal cost, and the card-fee floor** (claim) Serving one author's shelf for a month costs less than the incumbent charges one reader for one download; the hard row is 1.5% plus 20p with a 30p minimum, which the plan states and gets under with wallets, batching and an open payments protocol.
- **85% to the author, on a ledger they can recompute** (claim) The platform's 15% pays the card fee and lives on top-ups, batching and add-ons at a 70% author share; the statement is reconciled to the author's ledger, never the reverse.
- **What the service sells is provenance** (claim) This file, with this hash, published by this person, bound to a key in tiers; a conference, an employer, a journalist and a reader each have a cheap question answered.
- **The plan as a vault with a working mock** (artefact) Ten plan documents, the data, the right-of-access letter, a register of ten accepted risks, and an app of web components bundled for the vault host: the shelf, a deck page, the author's view, the roles, the flows, the economics, the rights.
- **What exists, and what does not** (question) Vaults, read keys, lanes and browser decryption exist; the deck enclave, grants as a service, the receipt that becomes a key, the migration tool and a sub-five-pence rail for a person do not; step zero is the author's own 69 decks.

> A setting lives on a server and changes when the server's owner changes. A key lives with the author and is verified by anyone. The whole design in two sentences: access by keys, not by settings.

> The right the platform reserves for itself it withholds from its users. The asymmetry in the terms on model training, stated without overstating the licence.

builds on [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](#the-agent-team-as-it-runs), [A personal agent that keeps your secrets: the 2026 agents read through behaviour policy and encryption, and a privacy-first design on vaults, enclaves and the browser](#a-personal-agent-that-keeps-your-secrets), [A supply chain of vaults: how GenAI, open data and small custom tools could bring the price of food down](#supply-chain-of-vaults), [The future of news is the story vault, not the paywall](#future-of-news-story-vault-not-paywall), [The reader was always the product: a corrected history of how news got into this mess](#how-news-got-here), [The SaaS apocalypse will be decided by inertia, not by AI](#saas-apocalypse-decided-by-inertia-not-by-ai).

## [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](the-agent-team-as-it-runs.md)

2026-10-06 · Agents & policyVaults & method

A running team of twelve Claude agents is described as a system and as a set of properties: each agent a role on a dedicated account with a behaviour policy; encrypted vaults the host cannot read as the only memory; messages between agents as email files in a mailroom; a CRM of one folder per person with provenance and hashes; a conductor with a security role first and last; drafts only, a person sends; identity and encryption as the strong barriers and policy as the weak one, said plainly; three classes of information, public, private-ish and personal, with the vaults built to refuse the third and rules scoped per customer or written for the recipient; each piece mapped to the idea on the site that argued for it; and the open question of who gives the mandate over information.

*[diagram]*
**concept**claim**method**example**question

**15 nodes, 17 edges**

- **One line: phone, sessions, vaults, drafts, people** (concept) The person talks from a phone; agents work in cloud sessions, keep everything as encrypted files, leave email as drafts; the person sends; a conductor runs the team four times a day.
- **The account is the blast radius** (claim) A dedicated Workspace, a dedicated Claude Team account, vault keys per session and a separate personal agent; a mistake stays inside one account, and this is the first control because it depends on nobody behaving.
- **Twelve agents, one focus each** (concept) Each agent is a role with a brief and a behaviour policy; eleven of twelve policies forbid sending; one role reads the mailbox, one writes drafts into it, none sends.
- **Email, but as files** (method) Agents drop .eml files into each other's mailroom folder in the shared vault; the recipient moves them to inbox and done; every message has a sender, recipient, kind and references; the vault keeps every version.
- **The conductor and the session steps** (method) Four runs a day, security first and last, one step per agent of up to twelve minutes; a session checks for a hold, snapshots, pulls, works, leak-checks, commits and ends with a card measured from the transcript.
- **Memory is one folder per person** (method) Plain JSON and Markdown: a record, an append-only ledger, every message with provenance and a hash, meeting notes, a graph of interests against what meets them, a generated summary; no database.
- **The rules never negotiated** (claim) Keys never in a file; no agent sends, with one named exception and a hold behind it; no agent changes a schedule; create anywhere, edit your own.
- **Barriers typed honestly** (claim) Identity and encryption are strong by construction; grant and record are medium; policy is weak and many rows rely on it; the honest column is where the next tooling goes.
- **The security properties, as properties** (concept) The host cannot read the memory; a reader cannot write; a writer can be given only a slot; keys never touch a file; a leaked write key means a new vault; the team can be stopped; inbound is data; everything is read afterwards.
- **Public, private-ish, personal** (claim) The vaults hold public and private-ish information and refuse personal; most of what a company agent handles is public or nearly so, which bounds the worst case before encryption is counted.
- **Rules per customer, rules for the recipient** (method) A policy per agent and a folder per person let a rule be scoped to one relationship or written to protect the person on the other end: capture only what the work needs, show them what is held.
- **Files, graphs and a state machine** (concept) Every piece of state is a file; the CRM graph and the team are the same fractal grammar at two altitudes; each role reads state, does one kind of work, writes state and stops.
- **Every piece has an argument on this site** (example) Dedicated accounts, behaviour policies, drafts only, the session card, the twin, graded barriers, vaults, lanes, rotation, fractal graphs, memory with provenance, interfaces from files, the agents' identity.
- **What is not working yet** (question) Two registers disagree; vault-to-vault messaging needs a person; one agent holds most open work; no daily brief channel; most barriers are policy-only because the platform cannot remove send tools per agent.
- **Who gives the mandate over information?** (question) Something sent to a person was not sent to a team of agents or to what they pass it to next; the setup holds less and says what it holds; the question gets a document of its own.

> A policy can ask an agent not to look; an account boundary means there is nothing there to see. Why the dedicated account is the first control and not the policy.

> A memory that can be shown to its subject is a memory that has been kept to what can be shown. The privacy design showing through the product design: the what-we-know-about-you pack.

builds on [Replicating the agentic inbox: a walkthrough from one Claude session to a team of agents that never press send](#replicating-the-agentic-inbox), [Six agents, one inbox: what a real multi-agent setup taught me about access policies](#six-agents-one-inbox), [A personal agent that keeps your secrets: the 2026 agents read through behaviour policy and encryption, and a privacy-first design on vaults, enclaves and the browser](#a-personal-agent-that-keeps-your-secrets), [Footprint and blast radius: what the agent actually did, and what it would have cost](#footprint-and-blast-radius), [Every risk is already accepted. The only question is by whom, and for how long.](#every-risk-is-already-accepted), [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](#custom-uis-are-not-the-exception), [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](#introducing-fractal-semantic-graphs), [Memory is not a spectator sport: how a web of open sites, graphs and vaults became the memory for sessions like this one](#memory-is-not-a-spectator-sport), [Before you give an agent a connector, give the connector a twin](#connector-twin-before-you-deploy-an-agent), [The wall under the reply: end an email with the state of the thread, not the thread](#the-wall-under-the-reply), [The identity we wanted to give the agents: a week of design, the line in Google's terms, and why login plus secrets is still too hard](#the-identity-we-wanted-to-give-the-agents); continued by [Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan](#authority-outside-the-model), [A Mac of the agent's own: a business plan for agent desktops, what Apple's licence allows, and three behaviour policies](#a-mac-of-the-agents-own), [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](#riskmandate-ten-questions), [How I work with Claude: one session per topic, agents with names, and memory you curate](#how-i-work-with-claude), [Encrypted memory for agents that run somewhere else: sgit deployment patterns, from a Mac mini to Kubernetes](#encrypted-memory-for-isolated-agents), [Knowing when to stop: what experience gives people, and what we have to design into agents](#knowing-when-to-stop), [Agency is not a yes: a scale for human and agent decisions, from rubber stamp to the reviewer who fixes the source](#agency-is-not-a-yes), [Hope or enforcement: one customer service agent, three designs, and who keeps each promise](#hope-or-enforcement), [Every mistake added a rule: complexity, agents, and the way back to shipping](#every-mistake-added-a-rule), [Where is the why? A permission prompt asked me to decide, and kept the reason](#where-is-the-why), [The Mandate Stack: a multi-agent system in production, layer by layer](#the-mandate-stack), [Why my agents do not run on my laptop: chat, Cowork and Code in the cloud, a vault as the shared drive, and the two walls an operating system has](#why-my-agents-do-not-run-on-my-laptop), [The deck I could not download: an author-first home for presentations, as a business plan somebody else can build](#the-deck-i-could-not-download), [A personal agent that keeps your secrets: the 2026 agents read through behaviour policy and encryption, and a privacy-first design on vaults, enclaves and the browser](#a-personal-agent-that-keeps-your-secrets).

## [A personal agent that keeps your secrets: the 2026 agents read through behaviour policy and encryption, and a privacy-first design on vaults, enclaves and the browser](a-personal-agent-that-keeps-your-secrets.md)

2026-10-06 · Agents & policyVaults & method

The personal agent became a product category in 2026, an always-on agent with a cloud computer, memory as files and connectors into a person's life; read through RiskMandate's behaviour policy the products differ most on the barrier, with Meta's Sentinel a boundary on actions and most others settings, while the mandate is unwritten and liability sits with the user; read for data sovereignty most sit in the vendor's corner, with Meta's own engineers saying today's protection is policy not cryptography and Apple's Private Cloud Compute the published design that does most; a page per person is a memory about non-users with no route to it; the vendors' memory and this site's CRM converged on files, no database and a page per person, so the privacy question is who holds the keys, not architecture; a privacy-first design puts memory in vaults the host holds as ciphertext, a behaviour policy as the permission authority, compute in the browser or an attested enclave with a per-task key released by the user's device and destroyed after, the frontier model only for the step that needs it, and a folder per person the person can read; what exists and what does not is stated, and the question of who gives the mandate over information is left for its own document.

*[diagram]*
**claim**method**example**question

**18 nodes, 21 edges**

- **The year the agent got a computer** (example) Spark in May, Scout in June, Siri AI in June, Grok Bot in August, Muse in September, dots in September, Alexa+ in February, Cowork from January; OpenClaw, self-hosted and open source, as the acknowledged origin of the shape.
- **The shape came from a self-hosted project** (claim) A personal agent as a small operating system of files, built by one developer for himself, then productised; Meta confirmed Muse was heavily inspired by it.
- **Lens one: what stops the agent** (method) Reach, mandate, gap, barriers and footprint applied to products: the reach is the user's life, the mandate is unwritten, liability sits with the user, and the barriers differ.
- **A separate permission authority is a boundary** (claim) Muse's Sentinel decides every connector action and every byte of egress outside the agent's reach, stronger on actions than the team's drafts-only rule; rules and approval prompts elsewhere are settings.
- **The blast radius was demonstrated** (example) A Mac zero-day redirecting dictation, a crafted link exfiltrating from a browser agent, exposed self-hosted endpoints and malicious skills: the reach exercised by someone other than the user.
- **Lens two: who can read what it knows** (method) Where it rests, encrypted by whom, who processes, who can be compelled, what trains, what deletes; the products answer the encryption question least.
- **Today's protection is policy, not cryptography** (claim) Meta's engineers say the Secure VM does not prevent Meta accessing data to support, secure or operate the service; the Confidential VM with a user-held key is with trusted testers and promised for later in the year.
- **The published design that does most** (example) Apple's Private Cloud Compute: stateless, attested nodes, the device wrapping keys only to measurements in a public log, two independent roots of trust.
- **The people who never signed up** (question) A page per person is a memory about non-users; the vendor says such information is not linked to an account and rights can only be honoured where it is; the ICO and the CNIL have named the risk.
- **What pays for it, and how much to trust** (claim) Transaction fees, subscriptions, hardware, a foundation; companies whose other products are advertising and engagement, a policy keeping the agent's data from ads, and a personal arithmetic of reach against benefit.
- **Same shape, different keys** (claim) A vendor's memory and the team's CRM both arrived at files, no database and a page per person filled from evidence; the privacy question is who holds the keys, who reads, what stops the agent and what pays, not architecture.
- **Memory in vaults the host cannot read** (method) Every file encrypted client-side, the host holding ciphertext; vault key, one-way read key and append lane as three reaches; one vault per scope until scoped reads exist; nothing trains because nothing can read.
- **The behaviour policy as the permission authority** (method) A separate authority enforcing a written policy: measured reach, written mandate, typed barriers, the send kept with the person for the irreversible, the footprint read from the vault afterwards.
- **Browser first, enclave second, frontier last** (method) Small models in the browser for triage and summaries over a locally decrypted vault; an attested enclave with GPUs for what the device cannot do; the frontier model only for the step that needs it with no standing access.
- **Temporary access to one slice, with a public key** (method) The device scopes a task to files, verifies the enclave's attestation, wraps a fresh key to its public key, the enclave decrypts in memory and encrypts results back, the key dies with the task, and the grant is a file in the vault.
- **What the operator still sees** (question) Timing and sizes, vendor-controlled attestation roots, physical memory-bus attacks, and a key policy a support ticket can restore: the design's own gap, to be typed honestly.
- **What exists today, and what does not** (question) Vaults, read keys, lanes, the policy and the team exist; the permission authority, the enclave image, the device-side key release, scoped reads, revocation and signed authorship do not; a five-step build order.
- **Who gives the mandate over information?** (question) Information given to a person was not given to an agent or to what it passes it to; a different question from who holds the key, left for its own document, with the mechanisms it would need already named.

> The privacy question is not a question of architecture. The files can be the same files. Why the convergence on file-based memory is good news: what differs is who holds the keys.

> Who gives the mandate over a piece of information is a different question from who holds the key. The question the design does not answer, and the mechanisms it would need.

builds on [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](#the-agent-team-as-it-runs), [Footprint and blast radius: what the agent actually did, and what it would have cost](#footprint-and-blast-radius), [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](#ultimate-insider-three-collisions), [Git for things you cannot put on GitHub](#what-sgit-is), [Six agents, one inbox: what a real multi-agent setup taught me about access policies](#six-agents-one-inbox), [The identity we wanted to give the agents: a week of design, the line in Google's terms, and why login plus secrets is still too hard](#the-identity-we-wanted-to-give-the-agents), [Memory is not a spectator sport: how a web of open sites, graphs and vaults became the memory for sessions like this one](#memory-is-not-a-spectator-sport), [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](#introducing-fractal-semantic-graphs), [Before you give an agent a connector, give the connector a twin](#connector-twin-before-you-deploy-an-agent); continued by [Where the vault keys live: key management at sgit-ai v0.20.0, and what comes next](#where-the-vault-keys-live), [Where is the why? A permission prompt asked me to decide, and kept the reason](#where-is-the-why), [Why my agents do not run on my laptop: chat, Cowork and Code in the cloud, a vault as the shared drive, and the two walls an operating system has](#why-my-agents-do-not-run-on-my-laptop), [The deck I could not download: an author-first home for presentations, as a business plan somebody else can build](#the-deck-i-could-not-download), [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](#the-agent-team-as-it-runs).

## [The investigation GitHub owes its customers: why a global outage of a platform the world deploys through deserves an aviation-style inquiry, and how the evidence could now be gathered](the-investigation-github-owes-its-customers.md)

2026-10-05 · Agents & policyVaults & method

A fault that reaches every customer of a platform the world deploys through is a near miss for all of them and a statement about how the platform is built, and it deserves what aviation gives its incidents: an independent investigator whose only job is prevention, mandatory and confidential reporting, published evidence, and the second and third story, why the system allowed it and why the fix was not paid for; the old objection that software incident evidence is too confidential and expensive to share has expired, because signed, versioned vaults with one-way read keys and agents that read the graph make the aviation docket affordable for a ninety-minute fault.

*[diagram]*
**concept**claim**method**example**question

**14 nodes, 14 edges**

- **What happened on 5 October** (example) From 19:11 UTC hosted runners stopped being reliably assigned for every customer; by 20:47 degraded availability; this site's release was cancelled by it and went live two hours late on a retry.
- **The status page is the whole record** (claim) Delays, degraded, resolved: true words chosen with care that do not name the component, its reach, the scope or whether the same thing nearly happened before.
- **Everybody is the point** (claim) A fault reaching one customer is an incident; a fault reaching all of them at once is a statement about isolation on the one component that gates every deploy, and a near miss for everyone who needed to ship a fix.
- **What aviation does** (method) Independent investigators whose sole objective is prevention, mandatory reporting of serious incidents, confidential near-miss reporting in the tens of thousands a year, preliminary reports within weeks, full dockets, tracked recommendations.
- **A near miss gets the same investigation** (claim) Because the systemic causes are the same and the only difference is luck; actual damage is usually a tenth of what was possible; you don't build safety on luck.
- **Count the rolls of the dice** (method) How many times the same event happened where they got away with it; from a one-off to a predictable statistic; do the people who depend on you consent to that risk.
- **First, second and third story** (concept) What happened; why the system allowed it; why the fix was not paid for. Software write-ups stop at the first; the third is where the money is.
- **The what-if ladder** (question) A day, a week, a corruption that cannot be restored, a withdrawal of service by decision: each a dependency question with a blast radius that has not been published, for the platform or for countries.
- **Why the market does not fix it** (claim) Customers cannot see how close to the wind the platform flies; only incidents that reach the status page are known; with the barrier to exit this high, uptime becomes marketing and the business case for hardening cannot be made from inside.
- **The objection has expired** (claim) Evidence was confidential, enormous and expensive to share; signed, versioned vaults, one-way read keys per party, agents under a behaviour policy and findings as a graph make the aviation docket affordable for a ninety-minute fault.
- **How the evidence would move** (method) Provider captures and signs; reviews and redacts, never rewrites; investigator reads by need; each customer gets its own derived vault; findings published as a graph linked to evidence hashes with recommendations held open.
- **What the regulation does and does not do** (example) Incident reporting duties and critical third-party regimes are arriving; none yet requires an independent published second story for a platform outage.
- **Four things to ask for** (method) A published second story within thirty days for every status-page incident; near misses counted and reported in aggregate; evidence captured into a signed record as a matter of course; an independent reader when an incident reaches everyone.
- **Help the people inside** (claim) Engineers who know where the single points of failure are cannot make the business case against revenue without evidence; a readable record makes it for them.

> A fault that reaches one customer is an incident. A fault that reaches every customer at once is a statement about how the system is built. Why the scope of tonight's fault, not its duration, is what deserves the inquiry.

> A system too complicated to understand and too fragile to change is not a reason to leave it alone. It is the single point of failure, named. The third story, and why it needs an investigator who does not report to the budget it is about.

builds on [Send an agent, not a spreadsheet: the next generation of software due diligence, and why the companies that stopped reading their code are about to be asked about it](#send-an-agent-not-a-spreadsheet), [Footprint and blast radius: what the agent actually did, and what it would have cost](#footprint-and-blast-radius), [Green does not mean live](#green-does-not-mean-live), [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](#ultimate-insider-three-collisions), [Every risk is already accepted. The only question is by whom, and for how long.](#every-risk-is-already-accepted); continued by [Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan](#authority-outside-the-model), [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](#riskmandate-ten-questions).

## [Send an agent, not a spreadsheet: the next generation of software due diligence, and why the companies that stopped reading their code are about to be asked about it](send-an-agent-not-a-spreadsheet.md)

2026-10-05 · Agents & policyStartups & strategy

Software due diligence was a questionnaire answered by the vendor and disconnected from the code; a buyer can now send a prompt or a small agent under a behaviour policy to run inside the vendor's environment and derive a graph of what reaches production unreviewed, what is documented and threat modelled, what the bugs touched and which agents act under what policy, with the vendor redacting but not rewriting; the test is risk-based, the behaviour policy is the due diligence document for the agents, the companies that stopped reading their code are about to meet the consequence they have not had, a startup should double down on understandability, and the code review company is better sold to buyers than to developers.

*[diagram]*
**concept**claim**method**example**question

**15 nodes, 16 edges**

- **Due diligence was a form** (claim) A spreadsheet of questions answered by the people being asked, measuring whether a document with the right title exists, disconnected from the code and out of date on arrival; built because nothing better was possible.
- **Companies will not lie on a record** (concept) Questionnaires invite careful, composed, defensible answers with room in them; a false statement on a record comes back with a lawyer, so the room is where the risk lives.
- **Send an agent, not a spreadsheet** (method) A prompt and a small agent under a behaviour policy run inside the vendor's environment, derive graphs of practices and code, write files the vendor reviews before anything leaves, and deliver what is shown in a vault only the buyer opens.
- **Derived, not composed** (claim) The vendor keeps the redaction marker and loses the pen: a map read from the repository can be withheld but not described into shape, and a false map is a false statement on a record.
- **Questions where silence is an answer** (method) Does code reach production unreviewed; is there a threat model and who wrote it; does the documentation match the code; what did the last fifty bugs touch; which agents touch the pipeline; who still understands it.
- **A threat model is the fastest read of a team** (claim) Thin means the team does not know what it protects; gaps seen and decided about mean a team that knows where the lines are; the critical unknown vulnerability is almost never in it.
- **Two kinds of bug** (concept) Bugs in reviewed deterministic parts have reasons; bugs from unreviewed generated code are in places no story asked for, repeat, and reveal something structural each time.
- **Risk-based, not pure** (claim) What counts as enough rises with what the software can do to the buyer; a startup on a prototype passes by saying so; the same sentence from a vendor of mission-critical software is the finding.
- **The behaviour policy is the due diligence document** (claim) A buyer reads off the blast radius, which controls are enforced by the identity and which are wishes, and which risks the vendor has accepted on the buyer's behalf; its absence is a finding before any code is read.
- **The consequence that was missing** (claim) Companies that stopped reviewing, let engineers go and let anyone prompt features into production accumulated liability that few outside could see; a buyer who can send an agent is the consequence, and investors and acquirers get it too.
- **Most companies already do not understand their software** (claim) People moved on, merges were made by people who left, documentation describes an earlier system; the agent asks them the same questions for the first time.
- **The startup's two advantages** (claim) It can play the same game as the biggest buyer with the same open source tools, and it has less code to understand; double down on understandability and make it the reason to buy.
- **Duties arriving before visibility** (example) Software bills of materials, the Cyber Resilience Act and the revised Product Liability Directive create duties and evidence rights; none tells a buyer whether a vendor understands its software; the agent connects the duties to the facts.
- **Sell it to the buyers** (claim) The code review company is better sold as due diligence to those who buy, invest in and acquire software than as review to developers who have been told they do not need it; the vendor runs it on itself first.
- **What is open** (question) The agent does not exist; the pieces do; the first vendor it should run against is this site's own repository, with the results published.

> The questionnaire gave the vendor the pen. The agent takes the pen away and leaves the vendor the redaction marker, and that is the whole change. Why a derived answer differs from a composed one even though the vendor still controls what leaves.

> A vendor that does not know what reaches production unreviewed does not know what reaches production. The first question, and why the non-answer is the finding.

builds on [If somebody built a company on code review: how I would do it, and why it is only now possible](#if-somebody-built-a-company-on-code-review), [Footprint and blast radius: what the agent actually did, and what it would have cost](#footprint-and-blast-radius), [Six agents, one inbox: what a real multi-agent setup taught me about access policies](#six-agents-one-inbox), [Every risk is already accepted. The only question is by whom, and for how long.](#every-risk-is-already-accepted), [Code review as a fractal semantic graph: source code is already one, and the review should read every layer of it](#code-review-as-a-fractal-semantic-graph), [Before you give an agent a connector, give the connector a twin](#connector-twin-before-you-deploy-an-agent), [A supply chain of vaults: how GenAI, open data and small custom tools could bring the price of food down](#supply-chain-of-vaults); continued by [The investigation GitHub owes its customers: why a global outage of a platform the world deploys through deserves an aviation-style inquiry, and how the evidence could now be gathered](#the-investigation-github-owes-its-customers).

## [How much of this did I write? The numbers behind twenty articles in four weeks, and what the input actually was](how-much-of-this-did-i-write.md)

2026-10-05 · Graphs & knowledgeSite & engineering

Measured from the session transcript and the git history, the twenty articles of the last four weeks took 63,000 words from the author, mostly in thirty-five voice memos, and came out at 85,000 words through 122 releases, with no article from a one-line prompt; the corrections were to direction, framing, voice, vocabulary and scope rather than to hallucinations, and the input that mattered most was twenty years of published writing the agent could find and quote, which is why people with a direction are the input to the loop rather than displaced by it.

*[diagram]*
**concept**claim**method**artefact**example**question

**15 nodes, 17 edges**

- **How much of this did I write?** (question) A friend found the volume of text baffling; the answer that I write briefs and review drafts is true and unbelieved, so the session was measured instead.
- **The session record as evidence** (method) The Claude Code transcript parsed for who said what and when, joined to the site's git history; limits stated, dataset published beside the article.
- **The evidence, as a vault** (artefact) Every number as a file in a published vault with a read key: messages, releases, days, ledgers with message ids, corrections with latency, the dependency map, the article's own fractal, versions with diffs and provenance captures; built by two agents from a brief in an afternoon, and it corrected the article twice.
- **The scale** (example) 281 messages and 62,896 words in, 52,719 of them in thirty-five voice memos; twenty articles and 85,209 words out, 94 figures, 122 releases, 135 searches, 22 research agents.
- **No article from a one-line prompt** (claim) The shortest brief was one memo of 1,943 words; the longest ran to twenty-nine messages; the median article took three releases.
- **Seven articles accounted for by hand** (example) From 2,395 words in and 2,447 out over five rounds, to 4,522 words in plus a reader's email and 9,289 out over five; the ratio runs from one to four and is the least interesting number.
- **What the corrections were** (claim) Direction, framing, voice, vocabulary and scope, with one fact corrected in each direction; briefs getting better, not hallucinations being caught.
- **A model needs someone with a direction** (claim) A model that can write well in every direction makes educated guesses; the person's job is to say which guess was meant, and each correction narrows the next.
- **What the memo stands on** (claim) The last article quotes thirty-three pieces of earlier writing: a 2010 tool, a book, 107 posts, 3,025 team files and twenty-six articles; the agent is fast because the record exists.
- **Published record as memory** (concept) The memory article's mechanism measured: curated, open, machine-readable material the agent is pointed at, rebuilt from twenty-two times when the context was compacted.
- **Being able to keep going** (concept) For twenty years lines of thinking stopped at the edge of what the business needed; now a thought can be followed to the end and published for the next one to stand on.
- **The compounding** (claim) Nineteen of twenty-seven articles cite an earlier one; corrections become rules in the build; each article is the distillation the next assumes.
- **The experts are the input** (claim) Direction, angle, taste and experience are what the loop needs from a person; the architect and the reviewer scale the same way the writing does.
- **What is open** (question) The articles could be shorter; attribution is hand-checked for seven; the oldest record is quoted not counted; the conversations behind the memos are in no record.
- **A better universe to learn from** (claim) The published trail of an idea, with its graphs, corrections and versions, is a better thing for a model to learn from than everything ever written without context; the vault behind this article is the next brief.

> I rarely experience hallucinations; I experience briefs that need to be better. The finding of the corrections list: one fact wrong, the rest a model choosing a reasonable direction and a person saying which one was meant.

> The agent is fast because the record exists. The real input is twenty years of published writing, not the memo.

builds on [Memory is not a spectator sport: how a web of open sites, graphs and vaults became the memory for sessions like this one](#memory-is-not-a-spectator-sport), [If somebody built a company on code review: how I would do it, and why it is only now possible](#if-somebody-built-a-company-on-code-review), [Code review as a fractal semantic graph: source code is already one, and the review should read every layer of it](#code-review-as-a-fractal-semantic-graph), [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](#introducing-fractal-semantic-graphs), [Replicating the agentic inbox: a walkthrough from one Claude session to a team of agents that never press send](#replicating-the-agentic-inbox), [The wall under the reply: end an email with the state of the thread, not the thread](#the-wall-under-the-reply); continued by [Knowing when to stop: what experience gives people, and what we have to design into agents](#knowing-when-to-stop), [Agency is not a yes: a scale for human and agent decisions, from rubber stamp to the reviewer who fixes the source](#agency-is-not-a-yes), [Liquid content needs water: liquefy the journalist's notebook, not the finished product](#liquid-content-needs-water), [The Mandate Stack: a multi-agent system in production, layer by layer](#the-mandate-stack).

## [If somebody built a company on code review: how I would do it, and why it is only now possible](if-somebody-built-a-company-on-code-review.md)

2026-10-05 · Graphs & knowledgeStartups & strategy

One technology can now read every layer from strategy to bytecode, which makes a graph at every altitude buildable and close to reality, and moves code review from an art of opinion to a science of facts if the models build, prune and maintain the graphs and then leave the line; what is fractal is the grammar and the layers are each company's own, so a code review company projects a graph from stories, derives one from code, reviews the join, holds one layer still to call a change a refactor, reshapes changes by reach, budgets per altitude as the objective good enough, runs its agents under behaviour policies, and gives the grammar away.

*[diagram]*
**concept**claim**method**example

**18 nodes, 22 edges**

- **One technology can read every layer** (claim) From a board objective to a syntax tree in one path or through sub-agents of the same kind; what people did by instinct between altitudes becomes buildable, and buildable close to reality, for the first time at scale.
- **From art to science** (claim) Review was opinion, taste and power because there was no fact base; the map says where the code is and the graph says what a change reaches, and the models get review there only by building and maintaining the graphs and then leaving the line.
- **The grammar is fractal, the layers are yours** (claim) Nodes, edges, an ontology, a taxonomy and the move between altitudes are constant; which layers exist, what they are called and where they stop are decided by the company, its culture, languages and stack.
- **The projected graph** (method) Built top down before the code exists: objectives, stories with rules and examples, features and flows, the commands and surfaces they will touch, components as far as design can honestly see.
- **The derived graph** (method) Built bottom up from the syntax tree with no model in line: fingerprinted nodes, resolved calls, classes, modules, the commands the code exposes, and proposed stories marked as proposed.
- **The review is the join** (claim) Three outcomes: a match, where a derived surface serves a projected story; derived but not projected, a bug or an unwritten story; projected but not derived, the plan or the forgotten thing.
- **Stories as rules and examples** (method) Example Mapping's cards as the top layer: a story node whose children are rules, whose children are examples a test or a run can satisfy; prose stories were the right first layer and the wrong final one.
- **A refactor is relative to the held layer** (claim) A refactor is a change where some layers move and one chosen layer, the one with the tests or the contract, does not; an architecture migration holding only the client interface is a refactor at a higher altitude.
- **The deploy is a layer** (concept) Pipelines, environments, running services, configuration and secrets form a graph with its own verbs; a change's reach continues through it, and the non-functional requirements live there.
- **Who reads the code depends on the map** (claim) Explorer code is read for intent, mostly by agents; villager code is read all the way down; town planner code is read by deterministic checks at the boundary, with a person for exceptions. The company sits in the two moves.
- **Reshape the change before reviewing it** (method) Split a change by reach: provably no behaviour, merged by a check; reaches tested behaviour, checks plus a glance; reaches a mission-critical path, the right people. Review is sorting, not saying no.
- **Replicate reality first** (method) Derive what a parser can, let a model propose the rest marked proposed, confront the graph with users, experts and tests, version everything so a review can be replayed as the graph was.
- **A budget per altitude, per change** (method) Deterministic checks always run; the delta re-derives only what changed; models get small budgets and hard stops; onboarding starts at one point and continues; handed-on work carries its budget and never widens it.
- **The reviewing agents run under a policy** (method) Every agent deriving, proposing or summarising runs under an Agent Behaviour Policy written before its first run: which repositories, which actions, where it writes, what it spends; the control on the reviewers' own blast radius.
- **The five whys fix the layer below** (method) Every finding at one layer is a question about the layer below, and the fix goes there as a rule or a graph query, so the next change like it is caught for the price of a query. Not whack-a-mole.
- **Compare the blast radius to the intent** (claim) Not to the old code: to the projected graph, the commit message, the existing documentation and the stories. Report one line per layer that moved; measure increments as projected nodes gaining a derived match.
- **Open source is the only model that fits** (claim) The layers are the customer's and the loop runs where the code is; sell the customised deployment, the running of the loop and the accumulated rules; give away the grammar, the parser and the model.
- **What the first article got wrong** (example) The refactor sentence was one refactor at one altitude; the seven altitudes were one repository's layers; the text skipped the commands and modules the delta had and the figure showed.

> A model in the line on every change is the art again with a different reviewer. The condition on which the move from art to science depends: the models build and maintain the graphs, then leave the line.

> The grammar is fractal. The layers are yours. The distinction the whole answer turns on, and the reason a review product has to learn each company's layers rather than impose its own.

builds on [Code review as a fractal semantic graph: source code is already one, and the review should read every layer of it](#code-review-as-a-fractal-semantic-graph), [Six agents, one inbox: what a real multi-agent setup taught me about access policies](#six-agents-one-inbox), [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](#introducing-fractal-semantic-graphs), [The SaaS apocalypse will be decided by inertia, not by AI](#saas-apocalypse-decided-by-inertia-not-by-ai), [Footprint and blast radius: what the agent actually did, and what it would have cost](#footprint-and-blast-radius), [Before you give an agent a connector, give the connector a twin](#connector-twin-before-you-deploy-an-agent), [For a startup, the most important question is whether they miss it](#the-question-is-whether-they-miss-it); continued by [The Mandate Stack: a multi-agent system in production, layer by layer](#the-mandate-stack), [Send an agent, not a spreadsheet: the next generation of software due diligence, and why the companies that stopped reading their code are about to be asked about it](#send-an-agent-not-a-spreadsheet), [How much of this did I write? The numbers behind twenty articles in four weeks, and what the input actually was](#how-much-of-this-did-i-write), [Code review as a fractal semantic graph: source code is already one, and the review should read every layer of it](#code-review-as-a-fractal-semantic-graph).

## [The identity we wanted to give the agents: a week of design, the line in Google's terms, and why login plus secrets is still too hard](the-identity-we-wanted-to-give-the-agents.md)

2026-10-05 · Agents & policyVaults & method

A plan to give every agent and user a Workspace identity from one tenant was stopped by Google's resale and function-account clauses; the design moved to a login product plus a bucket of ciphertext plus a browser keyring that only the user's passkey can open, on the rule that no secret can live inside an identity provider, and the week exposed that login, zero-knowledge storage and agent identity are still three separate jobs.

*[diagram]*
**concept**claim**method**artefact**example**question

**16 nodes, 17 edges**

- **A real identity for every agent and user** (concept) A Workspace seat per person and per agent from our tenant: mailbox, calendar, drive, login, with sgit encrypting before Google and a passkey as the only decryptor.
- **Workspace has no admin-proof zone** (claim) A super administrator can reach any Drive; client-side encryption is Enterprise Plus and Education only; so encryption happens in sgit, before Google.
- **The resale and function-account clauses** (claim) Current Cloud terms forbid selling, reselling, sublicensing or distributing the Services; the acceptable use policy names reselling End User Accounts in a product and accounts assigned to functions rather than humans.
- **A correction to our own pack** (example) The 'substitute or similar service' clause cited as section 2.6 is in the legacy free-edition agreement the standard-terms URL still serves, not in the current terms.
- **Five options, one table** (method) Shared Workspace (needs Google's agreement), Identity Platform plus bucket (chosen), customer's own Workspace, private customer cloud, Cognito plus S3 as the AWS variant.
- **No secret can live in the login** (claim) Whoever administers identity can reset a password, mint a token or sign in as anyone; the authority to decrypt must come from the user's authenticator.
- **Login decides paths; the passkey decides meaning** (concept) The identity provider and the bucket rules decide which paths a user may touch; the passkey decides whether the bytes mean anything; an administrator fakes the first, never the second.
- **The code is the boundary** (claim) Whoever controls the repository or DNS controls the app; so host away from the cloud project, vendor and hash every dependency, scope the passkey to one subdomain, never the apex.
- **The keyring** (artefact) One encrypted file per user holding a key pair and every small secret, unlocked by passkey PRF with a recovery code as second method, shared through per-user public keys, using sgit pki's algorithms.
- **A password manager first** (method) Every risky piece in one small product; the acceptance test is to hand a project owner a user id and ask for one plaintext field, then publish the attempt.
- **Passkey PRF: most places, not everywhere** (example) WebAuthn Level 3 became a Recommendation in August 2026; Chrome, Edge, Safari 18 and desktop Firefox ship PRF; Bitwarden and Dashlane unlock vaults with it; the MVP ships a compatibility matrix.
- **Agents are not seats** (claim) An agent gets a service identity, a lane for signed mail and a keyring entry a person releases, scoped and time-limited; our own agents keep their mailboxes because they are our organisation's.
- **Agent identity from the vendors** (example) Entra Agent ID, Okta for AI Agents, Google Cloud Agent Identity on SPIFFE, Anthropic's managed-agent vaults: workload identity that says which agent, not which person's key.
- **Three jobs, still separate** (claim) Login is solved; zero-knowledge per-user storage exists in pieces; agent identity exists for machines; nothing on the shelf is all three, and the joins are a startup's first month.
- **The regulator describes the property** (example) Articles 32 and 34(3)(a) and the EDPB's 'if the confidentiality of the key is intact' favour keys the operator cannot break; the market does not sell it.
- **Unless we are missing something obvious** (question) The design pack is published to be corrected; the nearest off-the-shelf answers found were two small password-derived open-source backends.

> Login decides which paths you may touch. The passkey decides whether the bytes mean anything. An administrator can fake the first and never the second. The rule the whole design rests on, and why no secret can live inside an identity provider.

> The law describes the property; the market does not sell it. The gap the article ends on: login, zero-knowledge storage and agent identity are still three separate jobs.

builds on [The wall under the reply: end an email with the state of the thread, not the thread](#the-wall-under-the-reply), [Six agents, one inbox: what a real multi-agent setup taught me about access policies](#six-agents-one-inbox), [Replicating the agentic inbox: a walkthrough from one Claude session to a team of agents that never press send](#replicating-the-agentic-inbox), [Footprint and blast radius: what the agent actually did, and what it would have cost](#footprint-and-blast-radius), [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](#ultimate-insider-three-collisions); continued by [Where the vault keys live: key management at sgit-ai v0.20.0, and what comes next](#where-the-vault-keys-live), [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](#riskmandate-ten-questions), [An open AI governance framework, and what its licence let us build](#ai-baseline-control-framework), [The Mandate Stack: a multi-agent system in production, layer by layer](#the-mandate-stack), [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](#the-agent-team-as-it-runs), [A personal agent that keeps your secrets: the 2026 agents read through behaviour policy and encryption, and a privacy-first design on vaults, enclaves and the browser](#a-personal-agent-that-keeps-your-secrets).

## [The wall under the reply: end an email with the state of the thread, not the thread](the-wall-under-the-reply.md)

2026-10-04 · Agents & policyVaults & method

The quoted wall under a reply is redundant and occupies the space where a reader asks what they need to know; replace it with a short, reader-specific state of the thread, derived from the record and linking back to it, drafted by the agent team's drafts role from typed blocks and reviewed by a person, and run as an experiment rather than a format.

*[diagram]*
**concept**claim**method**example**question

**14 nodes, 17 edges**

- **The quoted wall is redundant** (claim) Every reply ships the whole thread to a reader who already has it, and the clients hide it on arrival behind a trimmed-content link.
- **The reader's questions** (concept) Where are we, what was decided, what is open and whose, what happens next and do I act, who is on this thread now; the wall holds the material and answers none of them.
- **End with the state of the thread** (method) Decided, open, next, on copy, sources: a hundred words written for this reader, with links to the messages condensed, which stay in the thread as the record.
- **Written for one reader** (claim) The same thread condenses differently for the counterparty, the newcomer and the colleague who read everything; the question is what this person needs now.
- **Who is on copy is part of the state** (claim) Who joined, who left, which participants are agents: facts every newcomer needs that no quoted wall carries.
- **Derived, not the record** (concept) The tail points back at the thread instead of repeating it; if the tail is wrong the record underneath is not, and the reader can check in one tap.
- **Netiquette, BLUF, Minto, TL;DR, ADRs** (example) RFC 1855 asked for a summary instead of the full quote in 1995; the Army's bottom line up front; the Pyramid Principle; decision records with a Status line.
- **Reader-side AI summaries** (example) Superhuman, Shortwave, Copilot in Outlook, Apple Mail and Gmail now compute a summary at the top of a thread for the reader, privately and regenerated each time.
- **Sender's statement versus reader's view** (concept) The client summary belongs to one reader and nobody stands behind it; the tail is reviewed, shared with everyone on copy, in the record, and can be argued with.
- **The drafts role writes it** (method) From the typed blocks the inbox role already captures, for a chosen reader, with message ids cited and a hash logged; the person edits and sends; the inbox role records what went out.
- **Personal, so configurable** (method) Five rows, one line, or the wall back: the reader's preference is a row in their folder in the CRM; text first, richer forms are variants.
- **An experiment, not a format** (method) Four variants rotated by thread for a month on one person's correspondence, with measurements the record can take and the results published either way.
- **What would make this wrong** (question) Readers scrolling to the quotes anyway, condensations corrected in more than a few replies in ten, clients mangling the rows.
- **What does not exist yet** (question) The drafts role writing tails automatically, the preference row, the templates, the measurement report, the month of data and the follow-up.

> The wall is shipped with every message and hidden on arrival, which is the clearest possible sign that it is the wrong thing to ship. The observation the proposal starts from.

> The client's summary says what the thread looks like from here; the tail says what the sender believes it is. How the proposal differs from the AI summaries mail clients already compute.

builds on [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](#custom-uis-are-not-the-exception), [Replicating the agentic inbox: a walkthrough from one Claude session to a team of agents that never press send](#replicating-the-agentic-inbox), [Memory is not a spectator sport: how a web of open sites, graphs and vaults became the memory for sessions like this one](#memory-is-not-a-spectator-sport), [Six agents, one inbox: what a real multi-agent setup taught me about access policies](#six-agents-one-inbox); continued by [The Mandate Stack: a multi-agent system in production, layer by layer](#the-mandate-stack), [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](#the-agent-team-as-it-runs), [How much of this did I write? The numbers behind twenty articles in four weeks, and what the input actually was](#how-much-of-this-did-i-write), [The identity we wanted to give the agents: a week of design, the line in Google's terms, and why login plus secrets is still too hard](#the-identity-we-wanted-to-give-the-agents).

## [Memory is not a spectator sport: how a web of open sites, graphs and vaults became the memory for sessions like this one](memory-is-not-a-spectator-sport.md)

2026-10-03 · Graphs & knowledgeAgents & policy

Memory for agents is context management: many context-specific memories, fractal so an agent loads only the altitude its question needs, published and open so they can be fetched and cited, shared through vaults so sessions and agents hand off through files, with provenance on every item.

*[diagram]*
**concept**claim**method**artefact**example**question

**15 nodes, 21 edges**

- **Memory is not a spectator sport** (claim) Not one store that accumulates and retrieves by similarity; memory is made, placed, sourced and linked by people and agents.
- **Memory is context management** (concept) The question is what this agent needs in its window now, not what we remember; the same question the industry calls context engineering.
- **What the industry built** (example) Vendor memory features as a single store of conversations; frameworks from MemGPT to Mem0 and Zep; a filesystem beating a graph store on a memory benchmark; builders treating files as the ultimate context.
- **Two modes, one memory** (concept) The agentic session walks the altitudes and is summarised across resets; the one-shot call is handed one bundle; both are served by memory shaped in altitudes.
- **Many memories, each its own context** (claim) Sites, release log, briefs, vaults, Email-FS, the CRM's per-contact worlds: different vocabularies, inconsistent in places on purpose, joined by links and an index rather than a schema.
- **The fractal is the budget** (method) Index, graphs, one article's graph, the article, a vault's bundle, the vault: an agent loads the altitude its question lives at, because context has a token cost and degrades as it fills.
- **Findable because it is open** (claim) Open source and Creative Commons let an agent fetch, quote, link and cite; the more is published, the better the next context.
- **Provenance built in** (method) A URL for every quote, a commit for every release, a read key for every vault, a hash for every source file, a byline on every page; claims from memory are not allowed.
- **A vault is a memory bundle** (artefact) The right information for a moment, encrypted, versioned, hashed, opened with a read key that cannot write; the medium through which agents share memory without a shared session.
- **Email-FS, Issues-FS, per-contact worlds** (artefact) Agents talk in files with mailroom, inbox, done and outbox; issues are folders; each contact has its own graph and interface; each agent writes only its own folders.
- **The session that wrote this** (example) One Claude Code session across context resets: read the summary of itself, the conventions, the published sites and a review vault; loaded by altitude; checked; wrote back articles with graphs, a vault and six releases.
- **Publish, index, load, act, write back** (method) The loop that makes published material a memory rather than an archive; the next session starts from the files, because the model remembers nothing between sessions.
- **Stale pages become false memories** (question) Four stale facts found while writing: a node count, an index size, generated dates, a feed that stopped; two fixed by measuring at build time, two left standing and named.
- **Opinionated, hard to discover, and one estate** (question) One person's vocabulary at the top of every ladder; discovery strains the index; the thesis is tested only when a second estate is read alongside.
- **What does not exist yet** (question) A freshness check in the build, a published shape for the hand-off summary, the one-shot bundle as a vault, a librarian role on this site, a second estate.

> Nothing is remembered by the model between sessions. Everything is remembered by the files. The design in one line: memory lives in published, shared files, not in the model or a vendor's store.

> Provenance is what lets memory be shared without being trusted, and it is the part that a vector store cannot give you, because a similarity score is not a source. Why every item in the memory carries its source.

builds on [Sixteen thousand fetches, ten clicks, and a token bill nobody is sending: the case for paying publishers to be easy to read](#token-bill-nobody-is-sending), [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](#introducing-fractal-semantic-graphs), [Replicating the agentic inbox: a walkthrough from one Claude session to a team of agents that never press send](#replicating-the-agentic-inbox), [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](#custom-uis-are-not-the-exception), [Six agents, one inbox: what a real multi-agent setup taught me about access policies](#six-agents-one-inbox), [Code review as a fractal semantic graph: source code is already one, and the review should read every layer of it](#code-review-as-a-fractal-semantic-graph), [Price it, then give it away: the early access programme as the next step after "do they miss it"](#price-it-then-give-it-away); continued by [The agent is the reader: why agents will pay for graphs, personas and signed claims, because it is cheaper than not paying](#the-agent-is-the-reader), [How I work with Claude: one session per topic, agents with names, and memory you curate](#how-i-work-with-claude), [Knowing when to stop: what experience gives people, and what we have to design into agents](#knowing-when-to-stop), [Every mistake added a rule: complexity, agents, and the way back to shipping](#every-mistake-added-a-rule), [The Mandate Stack: a multi-agent system in production, layer by layer](#the-mandate-stack), [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](#the-agent-team-as-it-runs), [A personal agent that keeps your secrets: the 2026 agents read through behaviour policy and encryption, and a privacy-first design on vaults, enclaves and the browser](#a-personal-agent-that-keeps-your-secrets), [How much of this did I write? The numbers behind twenty articles in four weeks, and what the input actually was](#how-much-of-this-did-i-write), [The wall under the reply: end an email with the state of the thread, not the thread](#the-wall-under-the-reply).

## [Code review as a fractal semantic graph: source code is already one, and the review should read every layer of it](code-review-as-a-fractal-semantic-graph.md)

2026-10-03 · Graphs & knowledgeStartups & strategy

Source code is already a fractal semantic graph, stories to syntax tree and below, so a code review should diff every layer: a refactor moves the bottom and leaves the top still, a fix is a story that holds again, and the blast radius is the climb from changed methods to the stories that can reach them.

*[diagram]*
**concept**claim**method**example**question

**15 nodes, 20 edges**

- **Source code is a fractal semantic graph** (claim) Stories, flows, components, classes, methods and calls, the syntax tree, and down to the machine: each layer a graph with its own node types and verbs, and you change universe between them.
- **C4 and Gherkin: right instinct, fixed levels** (concept) C4 named four levels and left the code level optional; Gherkin shaped the top layer and glued it to code with regular expressions. Both saw the shape before anything could fill it cheaply.
- **Naming is now the cheap part** (claim) A model can say what a function does, which story a command serves and the verb between two nodes, from the syntax tree, once per change, as structured files.
- **Start from the syntax tree** (method) The tree survives reformatting and renaming; derive deterministically what a parser can, and spend the model on what it cannot know.
- **Every source file produces a pile of files** (method) Classes, methods and calls, package edges, fingerprints, tests, pattern results, kept as JSON next to the code in git, a vault or both; regenerated only on change.
- **Diff every layer** (method) A refactor moves the bottom layers and leaves the top still; a fix moves the bottom and is visible at the top as a story holding again, with a test; a leak is a forbidden edge.
- **Blast radius as the climb** (concept) From the methods a change touched, up the call graph with dynamic dispatch, to the commands and stories that can reach them, before anything runs.
- **Method streams** (method) Follow the call tree from one method and write out only that code; a 2012 O2 Platform review technique, now one script over a syntax tree with resolved calls.
- **The sgit CLI, read as layers** (example) 427 files, 377 classes, 1,111 methods, 2,592 calls, 72 commands, eleven stories, two streams, ten rules, one commit read upwards; nothing run; published as a vault.
- **One commit, read upwards** (example) Seven methods changed, no signature or field moved, six tests added; the climb reaches nine commands and six stories. The shape of a fix, and the commit message agrees.
- **Reality corrects the graph** (claim) You do not have to get the graph right; users confirm the top, experts confirm their layer, tests confirm execution, and every correction is a commit.
- **Patterns are findings** (claim) Folder shape, type shape, test shape and size shape are queries over the graph; the rules a project states most firmly are the ones that hold.
- **The review burden of generated code** (example) More cloned code and less refactoring, lower delivery stability with adoption, developers reporting almost-right answers and longer debugging: the answer is a different diff, not a faster reviewer.
- **What does not exist yet** (question) Proposed stories and edges from a model, node-level tree diffs, a second language, the interface layer, execution paths compared to predicted streams, and the review surface itself.
- **A company to build** (concept) A review that reads every layer, keeps the graph as files the customer owns, runs their rules as queries and improves with every correction; defensible through the record, not the model.

> You do not have to get the graph right. You have to get it to where user behaviour, the people who know each layer, and the tests can confirm or correct it. The condition that makes a model-derived graph of a codebase usable at all.

> The answer is not a faster reviewer reading the same diff. It is a different diff. The article's claim about the review burden of generated code.

builds on [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](#introducing-fractal-semantic-graphs), [Footprint and blast radius: what the agent actually did, and what it would have cost](#footprint-and-blast-radius), [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](#custom-uis-are-not-the-exception), [Every risk is already accepted. The only question is by whom, and for how long.](#every-risk-is-already-accepted), [If somebody built a company on code review: how I would do it, and why it is only now possible](#if-somebody-built-a-company-on-code-review); continued by [The AI governance stack, as a graph: an answer to Hari Kota, built](#the-ai-governance-stack-as-a-graph), [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](#riskmandate-ten-questions), [An open AI governance framework, and what its licence let us build](#ai-baseline-control-framework), [The Mandate Stack: a multi-agent system in production, layer by layer](#the-mandate-stack), [Send an agent, not a spreadsheet: the next generation of software due diligence, and why the companies that stopped reading their code are about to be asked about it](#send-an-agent-not-a-spreadsheet), [How much of this did I write? The numbers behind twenty articles in four weeks, and what the input actually was](#how-much-of-this-did-i-write), [If somebody built a company on code review: how I would do it, and why it is only now possible](#if-somebody-built-a-company-on-code-review), [Memory is not a spectator sport: how a web of open sites, graphs and vaults became the memory for sessions like this one](#memory-is-not-a-spectator-sport).

## [Replicating the agentic inbox: a walkthrough from one Claude session to a team of agents that never press send](replicating-the-agentic-inbox.md)

2026-10-02 · Agents & policyVaults & method

Claude is used as an agent state machine, one session per role, every message between agents a file in a vault and every outgoing email a draft a person sends; the phases take you from one session to a scheduled team without ever breaking that rule.

*[diagram]*
**concept**claim**method**artefact**example**question

**16 nodes, 21 edges**

- **Claude as a state machine** (concept) Each role is one session that reads its state from a vault, does one kind of work, writes files back and stops; the conductor makes this literal.
- **Accounts of the agent's own** (method) A Workspace mailbox on a domain you own, a Claude Team seat, a GitHub account on the same identity; never your own inbox.
- **Connectors enabled, then connected** (artefact) On a Team plan the owner enables connectors for the organisation; the agent's own account then connects, so the OAuth grants live only there.
- **The inbox role** (artefact) The one session that reads the mailbox, labels, moves, summarises and captures what people wrote into the CRM.
- **The policy as a table** (method) Reach, mandate, gap and barriers written before the first run; most barriers in front of a single session are the policy and nothing technical, and the table says so.
- **Roles: @inbox, @drafts, @crm, @briefs, @dev** (concept) Each role a session with a policy short enough to check; every account has the same reach to the mailbox, two have it in their mandate, one may write.
- **Email-FS lite** (artefact) A message is a file with email headers and typed blocks; mailroom, inbox, done and outbox folders; each role writes only its own folders; one commit per cycle after a leak check.
- **The agent drafts, a person sends** (claim) Nothing is sent by an agent; the draft is Cc'd to the person, its hash is logged, and the inbox role records the send from the Sent folder afterwards.
- **The security hold** (example) The one exception: the security role may send one email to one address on a critical finding, and writes a hold file that stops every agent and every run until a person releases it.
- **The conductor** (artefact) A scheduled session that runs every role exactly once in a fixed order with a time box, leak-checks and pushes after each step, and writes a report; a security role runs first and last.
- **The clone cost** (claim) Clone time grows with the number of commits, not file size; fifty commits a day made a seven-minute clone after three days. Commit once per run and compact when a clone passes five minutes.
- **A leaked write key means a new vault** (method) History keeps what was committed, so a key quoted in a committed file is fixed by a fresh vault seeded from the current files, not by a redaction; scan for other people's secret shapes too.
- **Interfaces for the moment** (artefact) The Now card and the waiting-on board, computed from the vault files when the page opens, nothing stored; each one gets a policy.
- **The record** (concept) Every message a file, every draft in the mailbox, every decision a row: a footprint that can be read afterwards without touching anything.
- **Trust built from the record** (claim) You do not have to believe what the agent says it did; you can read what it did, and give it more as the drafts you did not change pile up.
- **The agents' own account** (question) Each role describes what it reads, writes and refuses, in its own words; the dev role's paragraph and the briefs role's picture of the twelve-agent team are the first two.

> Nothing is sent by an agent. The rule that never changes, and the reason the setup gives the person more control rather than less.

> You do not have to believe what the agent says it did. You can read what it did. Why the record is the point for someone learning to trust a set of agents.

builds on [Six agents, one inbox: what a real multi-agent setup taught me about access policies](#six-agents-one-inbox), [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](#custom-uis-are-not-the-exception), [Footprint and blast radius: what the agent actually did, and what it would have cost](#footprint-and-blast-radius), [Before you give an agent a connector, give the connector a twin](#connector-twin-before-you-deploy-an-agent), [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](#ultimate-insider-three-collisions); continued by [How I work with Claude: one session per topic, agents with names, and memory you curate](#how-i-work-with-claude), [The Mandate Stack: a multi-agent system in production, layer by layer](#the-mandate-stack), [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](#the-agent-team-as-it-runs), [How much of this did I write? The numbers behind twenty articles in four weeks, and what the input actually was](#how-much-of-this-did-i-write), [The identity we wanted to give the agents: a week of design, the line in Google's terms, and why login plus secrets is still too hard](#the-identity-we-wanted-to-give-the-agents), [The wall under the reply: end an email with the state of the thread, not the thread](#the-wall-under-the-reply), [Memory is not a spectator sport: how a web of open sites, graphs and vaults became the memory for sessions like this one](#memory-is-not-a-spectator-sport), [Six agents, one inbox: what a real multi-agent setup taught me about access policies](#six-agents-one-inbox).

## [Price it, then give it away: the early access programme as the next step after "do they miss it"](price-it-then-give-it-away.md)

2026-10-02 · Startups & strategyAgents & policy

A price is a statement of what you think the thing is worth, and giving it away at that price to people who already know you is the cleanest test of whether the statement is true, provided you measure and cut what the free offer costs them.

*[diagram]*
**concept**claim**method**artefact

**13 nodes, 17 edges**

- **Do they miss it** (concept) The earlier article's test: hand the thing to people for free, briefly, then take it away, and ask whether they miss it.
- **Define the product** (method) For RiskMandate the thing somebody receives is an Agent Behaviour Policy for one agent, as an encrypted vault the customer holds the keys to, with the mandate corrected for their deployment.
- **Price it before you give it away** (claim) A price is a statement of what you think the thing is worth, and giving it away at that stated price to people who know you is the cleanest test of whether the statement is true.
- **The four-tier ladder** (artefact) Ten pounds for the pack downloaded, fifty for a working vault, five hundred for the vault corrected for your situation, fifteen hundred for two sessions and a professional's signature.
- **Cost that grows a step at a time** (method) The agentic workflow means the marginal customer costs a little more, not a lot more, so serving the twentieth customer costs close to serving the second.
- **Offer it to the people who already know you** (method) Early adopters, power users and past customers get the first twenty, as a thank-you and as the best possible test group, because their silence means the most.
- **Free is never free for the other side** (claim) Engaging costs them reading, thinking, deciding and finding a slot, so the first measurement the programme makes is of that attrition and the exercise is to reduce it.
- **Do not make them apply** (method) "We have twenty of these in the first round. Would you like one? If not, I will give it to someone else" is honest about scarcity and leaves them nothing to do but say yes or no.
- **RiskMandate early access programme** (artefact) Live on 30 September 2026, invite only, it gives the five-hundred-pound tier to people who already run an agent with real access and asks them to say where it is wrong.
- **The answer is brutal either way** (claim) If friendlies take it and ask for more, the question becomes price; if they say it is interesting but have no time, the problem is not the price and you go back to the drawing board.
- **What we count** (method) Policies created, customised, used, and scenarios run, plus corrections received and the minutes each step cost the person on the other side.
- **For the agents running this** (method) The list, the short message with no application, the clock on every step, daily counts, every stop recorded as a product change, a stop rule set before the first message, and this article as the record.
- **The site is becoming the memory** (claim) An agent picking this up in a year should read, in order, the earlier article, the published offer, this article and the vault holding the counts, so it gets context rather than instructions.

> A price is a statement of what you think the thing is worth. Giving it away at that stated price, to people who know you, is the cleanest test of whether the statement is true. The whole method in two sentences: the price is set first and the free offer is the test of it.

> None of that is zero, and all of it is paid by them. The part that is easy to leave out: the offer costs the other side attention and schedule, and that cost is what the programme measures.

builds on [For a startup, the most important question is whether they miss it](#the-question-is-whether-they-miss-it); continued by [Going live with the reading meter: pay for what you read, go below zero if you like, and the numbers we will check in eight weeks](#going-live-with-the-reading-meter), [A meter in the browser: a penny a page, a history you keep, and a site that picks for you](#a-meter-in-the-browser), [Memory is not a spectator sport: how a web of open sites, graphs and vaults became the memory for sessions like this one](#memory-is-not-a-spectator-sport), [For a startup, the most important question is whether they miss it](#the-question-is-whether-they-miss-it).

## [Footprint and blast radius: what the agent actually did, and what it would have cost](footprint-and-blast-radius.md)

2026-10-02 · Agents & policyVaults & method

Add two words to the Agent Behaviour Policy: footprint, what the agent actually did, read afterwards from the record and compared with the mandate, and blast radius, what a row of its reach would cost the business if used in full today, with whether there is a way back.

*[diagram]*
**concept**claim**method**artefact**example**question

**16 nodes, 21 edges**

- **Reach, mandate, gap and barriers** (concept) RiskMandate's policy is written before the agent runs: reach is what it can do, mandate what you asked, gap the difference in both directions, barriers what stands in the way.
- **Only a boundary is a control** (concept) A barrier is a boundary, a setting, an expectation or nothing, and most of what organisations call controls turn out to be expectations once they are typed.
- **Footprint** (concept) The set of things the agent actually did, in a period, read from the record afterwards; the same kind of list as the reach and the mandate, but evidence rather than a decision.
- **Where the footprint comes from** (artefact) The connector's audit log, the model provider's tool-call record, a connector twin's replay, a vault's commit history, the append lanes and the agents' own messages.
- **Reading, not intercepting** (claim) Nothing sits inline, a copy of the logs or a read key is enough so an outside reviewer can do it, and the footprint accumulates so some findings only exist at the twelfth week.
- **Footprint in the gap** (concept) The agent did something within its reach and outside its mandate and nothing stopped it, which is a near miss, and it resolves by adding the row to the mandate or putting a boundary in front of it.
- **Dormant mandate** (concept) A row the owner asked for that the footprint never shows: an over-stated mandate, a check that was relied on and never ran, or a shortfall the reach inventory missed.
- **Expected-use hint** (method) Each mandate row wants a hint of how often the owner expects to see it, always, sometimes, rarely, hopefully never, so a dormant row can be told from a contingency that was never needed.
- **The mandate as practised** (method) Read the footprint for a month and you have the rows the agent actually uses, with the near misses marked, as the first draft of a policy for an agent that has none.
- **Blast radius** (concept) What it would cost the business if a row were used in full, today, defined over the reach because whoever takes the agent over inherits its reach and ignores its mandate.
- **Whether there is a way back** (concept) Two rows with the same scope and different reversibility are not the same risk, and the policy should say so.
- **Same footprint, different blast radius** (example) An agent drops a staging table three times over two months; the row is identical each time, and only on day forty-one, when it held six weeks of real records, is it the incident.
- **What the cloud already does** (example) AWS, Google Cloud and Microsoft Entra already compare permissions granted with permissions used, but a permission set carries no statement of intent, so there is no dormant mandate.
- **A vault is a footprint recorder by construction** (claim) Every commit is signed, versioned and append-only, so an agent working in a vault leaves a footprint whether or not anyone intended to collect one, and most of what sgit does shrinks the irreversible part of the blast radius.
- **The gap plus blast radius is the risk** (claim) The gap is exposure, blast radius is impact, and the person who accepts a gap is accepting its blast radius, which until now the policy did not state.
- **Reading our own footprint** (question) Ten agents, six with a written policy, eight days of commit history; the footprint against the six policies is still to be read and published as the second article.

> The mandate tells you what you hoped for. The reach tells you what you are exposed to. Why blast radius is defined over the reach, not the mandate: an attacker inherits the reach.

> The footprint is how you get near misses for agents without waiting for the luck to run out. The payoff of reading the footprint against the gap: incidents and near misses are the same events with different luck.

builds on [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](#ultimate-insider-three-collisions), [Before you give an agent a connector, give the connector a twin](#connector-twin-before-you-deploy-an-agent), [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](#custom-uis-are-not-the-exception), [Every risk is already accepted. The only question is by whom, and for how long.](#every-risk-is-already-accepted), [Six agents, one inbox: what a real multi-agent setup taught me about access policies](#six-agents-one-inbox); continued by [Where the platform draws the line: Microsoft Execution Containers, the shared responsibility model for agents, and the business logic above it](#where-the-platform-draws-the-line), [The same argument, in our words: Satya Nadella on models as insider risks, translated into the language of RiskMandate](#the-same-argument-in-our-words), [Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan](#authority-outside-the-model), [One article, five readers: a librarian, a cartographer, a historian, an explainer and a storyteller read the same piece](#one-article-five-readers), [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](#riskmandate-ten-questions), [Every mistake added a rule: complexity, agents, and the way back to shipping](#every-mistake-added-a-rule), [Where is the why? A permission prompt asked me to decide, and kept the reason](#where-is-the-why), [The Mandate Stack: a multi-agent system in production, layer by layer](#the-mandate-stack), [Why my agents do not run on my laptop: chat, Cowork and Code in the cloud, a vault as the shared drive, and the two walls an operating system has](#why-my-agents-do-not-run-on-my-laptop), [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](#the-agent-team-as-it-runs), [A personal agent that keeps your secrets: the 2026 agents read through behaviour policy and encryption, and a privacy-first design on vaults, enclaves and the browser](#a-personal-agent-that-keeps-your-secrets), [The investigation GitHub owes its customers: why a global outage of a platform the world deploys through deserves an aviation-style inquiry, and how the evidence could now be gathered](#the-investigation-github-owes-its-customers), [Send an agent, not a spreadsheet: the next generation of software due diligence, and why the companies that stopped reading their code are about to be asked about it](#send-an-agent-not-a-spreadsheet), [If somebody built a company on code review: how I would do it, and why it is only now possible](#if-somebody-built-a-company-on-code-review), [The identity we wanted to give the agents: a week of design, the line in Google's terms, and why login plus secrets is still too hard](#the-identity-we-wanted-to-give-the-agents), [Code review as a fractal semantic graph: source code is already one, and the review should read every layer of it](#code-review-as-a-fractal-semantic-graph), [Replicating the agentic inbox: a walkthrough from one Claude session to a team of agents that never press send](#replicating-the-agentic-inbox), [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](#ultimate-insider-three-collisions).

## [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](custom-uis-are-not-the-exception.md)

2026-10-01 · Graphs & knowledgeAgents & policy

Every message has a graph with altitudes, so a message is designed for the recipient's moment rather than the sender's thread; a custom interface per moment is how interfaces now get made, each one commoditising the next, and each is an agent surface that gets a policy.

*[diagram]*
**concept**claim**method**artefact**example

**16 nodes, 20 edges**

- **The follow-up problem** (concept) Following up is harder than doing the work, because every person has a different context and the thread you share hides its own structure.
- **Every message has a graph** (concept) Extract the actions, questions, statements, decisions and concepts from every message and a thread stops being a thread and becomes a graph.
- **Altitudes** (concept) There is a graph for the block inside a message, the message, the conversation, the company and the contact, each navigable on its own and pointing up and down.
- **Email is a medium** (claim) The design brief for a message is the recipient's moment when they open it, not the sender's thread, so send what they need in the shape they need it.
- **A message is a projection** (concept) A message to a person is a projection of the conversation graph, for one reader, at the moment they open it, and a thread is only the raw stream.
- **Genesis, custom, product, commodity** (concept) Everything moves from genesis through custom-built to product to commodity, and every new interface built is a thing commoditised for next time.
- **Custom interfaces are not the exception** (claim) A custom interface per message, per thread, per topic, per question is not an exception; it is how interfaces get made.
- **The page that is both the to-do and the place to act** (example) A page lists the PDFs still owed and gives a place to drop them, through the vault's append lane, with no context switch, no second tool and no email.
- **Append lane** (artefact) A write-only channel anyone with the token can drop a file into, which the vault's owner drains and processes in order.
- **Email-FS blocks** (artefact) The fenced decision, answer and status blocks that Email-FS-lite uses so agents can read each other's asks without parsing prose, rendered as an interface for a human.
- **Eight days, not one afternoon** (example) From 25 September to 2 October 2026 a small team of agents and one human went from an empty vault to a working way of doing outreach, with sixteen CRM interface releases and around 230 commits.
- **Every tap teaches the next interface** (method) A moment gets a shape, the shape gets a decision, the decision is written to the vault as a record, and the record shapes the next version of the interface.
- **Why it compounds** (claim) Every interface makes the next one better, each one teaches the agent how its user wants to work, and when automation outgrows the inbox the interface becomes the prioritisation.
- **The future of email** (claim) The future of email is sender-served structure, read by the recipient's agent, with the inbox as one view of the graph, and a plain email still works on day one.
- **Ten agents and one human** (example) Ten agents with narrow jobs and one human who decides, talking to each other in files, each writing only its own folders, six with a written Agent Behaviour Policy.
- **An interface is an agent surface, so it gets a policy** (claim) A page that drops files into a vault, answers questions or lets a model read a CRM has a grant, a mandate, a delta and barriers, so it gets a policy like any agent.

> Every time I ask an agent in chat for something a page could have shown me, that is the next interface. The measurable version of the title: the trigger that produces each custom interface.

> The graph is the medium. Email, cards, voice and boards are views of it. The turn where email stops being the medium and becomes one projection of the graph.

builds on [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](#introducing-fractal-semantic-graphs), [Six agents, one inbox: what a real multi-agent setup taught me about access policies](#six-agents-one-inbox), [The future of news is the story vault, not the paywall](#future-of-news-story-vault-not-paywall), [Before you give an agent a connector, give the connector a twin](#connector-twin-before-you-deploy-an-agent), [A chat box on a site with no server, the plan, and the trade it makes](#chat-on-a-static-site), [Seven vaults, one method](#seven-vaults-one-method), [Sixteen thousand fetches, ten clicks, and a token bill nobody is sending: the case for paying publishers to be easy to read](#token-bill-nobody-is-sending), [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](#ultimate-insider-three-collisions); continued by [Liquid content needs water: liquefy the journalist's notebook, not the finished product](#liquid-content-needs-water), [The Mandate Stack: a multi-agent system in production, layer by layer](#the-mandate-stack), [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](#the-agent-team-as-it-runs), [The wall under the reply: end an email with the state of the thread, not the thread](#the-wall-under-the-reply), [Memory is not a spectator sport: how a web of open sites, graphs and vaults became the memory for sessions like this one](#memory-is-not-a-spectator-sport), [Code review as a fractal semantic graph: source code is already one, and the review should read every layer of it](#code-review-as-a-fractal-semantic-graph), [Replicating the agentic inbox: a walkthrough from one Claude session to a team of agents that never press send](#replicating-the-agentic-inbox), [Footprint and blast radius: what the agent actually did, and what it would have cost](#footprint-and-blast-radius).

## [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](ultimate-insider-three-collisions.md)

2026-09-30 · Agents & policy

Agents are the insider threat that never scaled before, the infrastructure was designed for none of it, and risk management runs at the speed of spreadsheets, so the way out is to constrain the agent in order to trust it.

*[diagram]*
**concept**claim**method**example

**16 nodes, 20 edges**

- **A threat is anything that causes business impact** (concept) A threat does not need to be malicious, and most of the worst damage was a bug, a misconfiguration or a person doing something that was allowed and should not have been.
- **The insider threat never scaled** (claim) There were two kinds of insider, a human bounded by hours and conscience and static code that did what it was written to do, and both were constrained by something soft but real.
- **An agent is a reasoning engine in a loop** (concept) An agent is a language model in a loop with tools and an objective, and unlike any insider before it has skills: every language, every schema, the ability to write its own connectors and try again.
- **The lethal trifecta** (concept) Give a model private data, untrusted content and a way to communicate outward, and it can be turned against you by a document it reads.
- **Five incidents** (example) Replit, Gemini CLI, Amazon Q, EchoLeak and the AI-orchestrated espionage campaign, of which three were not attacks but agents being agents.
- **82 machine identities per human** (example) Agents are arriving into a population of identities that is already unmanaged, with 42 per cent of machine identities holding privileged access.
- **The infrastructure that cannot hold them** (claim) Recovery, identity, permissions and containment were all built for code that stays where you put it, and the stack falls over on its own.
- **The grant and the mandate** (concept) Cloud permissions are the union of everything anyone ever needed, so an agent's grant is not what you meant but everything the role accumulated.
- **The two outages** (example) A DNS race condition took down a large part of AWS US-East-1 for over fourteen hours, and a configuration file that doubled in size broke Cloudflare and much of the web.
- **Risk management at the speed of spreadsheets** (claim) 48 per cent of organisations track risk in spreadsheets, reviewed quarterly, when the decisions now have to be made in seconds and in advance.
- **The chain to pulling the plug** (claim) Because the register cannot see what the agent can reach it cannot say what the risk is, cannot decide whether it fits the appetite, cannot fund the controls, and the plug comes out.
- **Nobody has to report** (claim) Companies are not required to disclose most of what agents do to them, and aviation solved this fifty years ago with confidential reporting that cyber has nothing like.
- **The collision** (claim) An entity inside the company with reach we have not measured, controls we cannot rely on, and a decision process too slow to matter before, during or after the incident.
- **Agent Behaviour Policy** (method) Grant measured, mandate elicited, delta derived, barrier recorded, with each barrier typed honestly as a boundary, a setting, an expectation or nothing.
- **Contain in layers** (method) Identity per agent, twins that journal every call, network segmentation, and append-only records in vaults the host cannot read.
- **Brakes are what let a car go fast** (claim) The more you can constrain an agent, the more you can trust it, and the more autonomy you can afford to give it.

> Three of those five were not attacks. They were agents being agents. The distance between benign and malicious agent damage is a prompt, which is why the insider framing fits.

> The more you can constrain an agent, the more you can trust it, and the more autonomy you can afford to give it. The irony the talk would end on, and the turn from the problem to the way out.

builds on [Every risk is already accepted. The only question is by whom, and for how long.](#every-risk-is-already-accepted), [Footprint and blast radius: what the agent actually did, and what it would have cost](#footprint-and-blast-radius), [Six agents, one inbox: what a real multi-agent setup taught me about access policies](#six-agents-one-inbox), [Before you give an agent a connector, give the connector a twin](#connector-twin-before-you-deploy-an-agent), [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](#introducing-fractal-semantic-graphs); continued by [The same argument, in our words: Satya Nadella on models as insider risks, translated into the language of RiskMandate](#the-same-argument-in-our-words), [Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan](#authority-outside-the-model), [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](#riskmandate-ten-questions), [Where is the why? A permission prompt asked me to decide, and kept the reason](#where-is-the-why), [The Mandate Stack: a multi-agent system in production, layer by layer](#the-mandate-stack), [Why my agents do not run on my laptop: chat, Cowork and Code in the cloud, a vault as the shared drive, and the two walls an operating system has](#why-my-agents-do-not-run-on-my-laptop), [A personal agent that keeps your secrets: the 2026 agents read through behaviour policy and encryption, and a privacy-first design on vaults, enclaves and the browser](#a-personal-agent-that-keeps-your-secrets), [The investigation GitHub owes its customers: why a global outage of a platform the world deploys through deserves an aviation-style inquiry, and how the evidence could now be gathered](#the-investigation-github-owes-its-customers), [The identity we wanted to give the agents: a week of design, the line in Google's terms, and why login plus secrets is still too hard](#the-identity-we-wanted-to-give-the-agents), [Replicating the agentic inbox: a walkthrough from one Claude session to a team of agents that never press send](#replicating-the-agentic-inbox), [Footprint and blast radius: what the agent actually did, and what it would have cost](#footprint-and-blast-radius), [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](#custom-uis-are-not-the-exception).

## [The reader was always the product: a corrected history of how news got into this mess](how-news-got-here.md)

2026-09-29 · News & evidence

The reader has been the product since 1833 and the money has always flowed to whoever owned the road, so the fix is to stop charging for the road and charge for the cargo: the story as a graph with every claim tied to hashed evidence.

*[diagram]*
**concept**claim**method**artefact**example

**15 nodes, 18 edges**

- **The reader was always the product** (claim) The reader stopped being the customer in 1833 and became the audience sold to the advertiser, and by 2005 advertising was 82% of American newspaper revenue.
- **Penny press** (example) The New York Sun of September 1833 sold on the street for a cent and was paid for by advertising while other papers relied on high-priced subscriptions.
- **Unregulated toll bridge** (concept) A monopoly city newspaper was the only way for a local advertiser to reach local households, and its margins of 20 to 30 per cent paid for the reporting.
- **Classifieds collapse** (example) Classifieds were about 40% of revenue and fell from $19.6 billion in 2000 to about $6 billion in 2009 once Craigslist let people list a sofa for free.
- **The measurable reader** (concept) Cookies in 1996 and AdSense in 2003 let the reader be followed from page to page, and by 2017 Google and Meta took 54.7% of American digital advertising.
- **Publisher as tenant** (claim) Publishers depended on traffic from companies that could switch it off, and Facebook referrals to news sites fell 58% in six years.
- **Novelty beats truth** (claim) False news on Twitter was 70% more likely to be retweeted than true news, spread by humans not bots, and Facebook weighted an anger reaction at five times a like.
- **Provenance is labour** (claim) Following a claim to its source is hours of a person's time, and newsrooms that lost 57% of their jobs cut those hours first because they did not move the click.
- **AI removes the traffic** (claim) Search traffic to publishers fell a third in the year to November 2025 while the crawlers that replaced it fetch tens of thousands of pages per reader they send back.
- **Back to selling to readers, by rent** (claim) Circulation revenue overtook advertising in 2021, but what is sold is the subscription, unlimited access priced for the reader who forgets to cancel.
- **402 Payment Required** (artefact) HTTP/1.1 reserved a status code in 1997 for digital cash or micropayment systems, and it is still reserved for future use with no browser having implemented it.
- **Mental transaction costs** (concept) Szabo and Shirky argued that deciding whether an article is worth two cents costs more than two cents, an argument that does not apply to an agent with a wallet.
- **Advertising as the default** (claim) The banner ad, the cookie, the pop-up and AdSense were small decisions that together made advertising the default model to support online content.
- **People pay when paying is easy** (claim) A million iTunes songs sold in the first week in 2003 and Substack passed five million paid subscriptions in 2025, in an industry that insisted people never would.
- **Charge for the cargo, not the road** (method) Sell the story as a graph, every claim walked to frozen and hashed evidence, in pence and on demand, with the money walking back to whoever made the fact.

> The reader stopped being the customer in 1833. The reader became the audience that was sold to the customer, and the cover price became a way of proving the audience existed. The most important of the four corrections: the web did not make the reader the product, the penny press did.

> The fix is to stop charging for the road and start charging for the cargo. The four eras end here: the money followed whoever owned distribution, so the proposal is to sell the evidence itself.

builds on [The future of news is the story vault, not the paywall](#future-of-news-story-vault-not-paywall), [Sixteen thousand fetches, ten clicks, and a token bill nobody is sending: the case for paying publishers to be easy to read](#token-bill-nobody-is-sending), [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](#introducing-fractal-semantic-graphs); continued by [Going live with the reading meter: pay for what you read, go below zero if you like, and the numbers we will check in eight weeks](#going-live-with-the-reading-meter), [A meter in the browser: a penny a page, a history you keep, and a site that picks for you](#a-meter-in-the-browser), [Liquid content needs water: liquefy the journalist's notebook, not the finished product](#liquid-content-needs-water), [Story vault underneath, Reader Skills on top: why local journalism has the most to gain](#story-vault-meets-reader-skills), [The deck I could not download: an author-first home for presentations, as a business plan somebody else can build](#the-deck-i-could-not-download).

## [Six agents, one inbox: what a real multi-agent setup taught me about access policies](six-agents-one-inbox.md)

2026-09-29 · Agents & policy

Write an agent's access policy as a table with a column for how each rule is enforced, and the policy is exactly as strong as the row that says the agent has been told.

*[diagram]*
**concept**claim**method**artefact**example

**16 nodes, 19 edges**

- **The worst row** (claim) If the enforcement column says the agent has been told, that row is a hope, and the policy is exactly as strong as that hope on the day something goes wrong.
- **The account is the blast radius** (claim) Every session an agent opens through a connector runs as the account that authorised it, with everything that account can reach.
- **Dedicated accounts per agent** (method) A dedicated Workspace seat, a dedicated Claude seat and a dedicated GitHub account per agent, so the worst a session can do is bounded by what its account can see.
- **Organisational unit** (concept) An account of its own puts each agent in its own organisational unit, and Google Workspace applies its Gmail compliance rules per unit.
- **Restrict delivery** (method) A delivery restriction to my own domain means that even if the reader sends, it can only reach me.
- **Attachment compliance** (method) An outbound rule that strips attachments turns a policy into a property of the mail system.
- **Scope limits on third-party apps** (method) The sharpest tool in the box cannot express drafts only, because the Gmail API puts drafting and sending in the same grant.
- **Six roles** (concept) The reader, the mailbox, the inbox, the CRM, the dev team and the site editor, each with a policy short enough to check and differing on who may send.
- **The exception arrived before the policy** (example) The reader that must never reply must reply when the message came from me, and never became never, unless on day one.
- **Signature registry** (artefact) The append-lane machinery of per-session keys and a pinned registry is what would let the reader verify a message came from me, once my key is in it.
- **The attachment finding** (example) An agent found that create_draft and update_draft accept an attachments array and proved it with a 17 KB signed PDF that arrived intact.
- **The documentation disagrees with itself** (claim) One vendor page says the Gmail connector is read-only and another says it can send, reply and forward, so a policy that cites the documentation has cited a moving target.
- **Connector twin** (method) Before you write down what an agent may do, replay what it can do.
- **Enforcement ladder** (concept) Identity boundaries and keys enforce themselves, compliance rules enforce at the platform, approval prompts enforce at the human, and everything else is the agent doing as it was told.
- **The policy table** (artefact) One rule per row across six roles, with the column that says whether it is enforced, an admin rule, an approval, or told.
- **Cowork and Claude Code reach** (example) The Cowork agent has no GitHub connector and cannot open the repository, while the Claude Code agent on the same seat edits the site.

> An access policy for an agent is only as real as its worst row. The claim the whole article is built to test, stated so it can be wrong.

> The only way to know what a connector can do is to try. The attachment finding showed a policy written from documentation was wrong.

builds on [Before you give an agent a connector, give the connector a twin](#connector-twin-before-you-deploy-an-agent), [Replicating the agentic inbox: a walkthrough from one Claude session to a team of agents that never press send](#replicating-the-agentic-inbox); continued by [The same argument, in our words: Satya Nadella on models as insider risks, translated into the language of RiskMandate](#the-same-argument-in-our-words), [A Mac of the agent's own: a business plan for agent desktops, what Apple's licence allows, and three behaviour policies](#a-mac-of-the-agents-own), [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](#riskmandate-ten-questions), [Zoom into an agent's behaviour policy and you find the business logic](#the-behaviour-policy-is-the-business-logic), [An open AI governance framework, and what its licence let us build](#ai-baseline-control-framework), [Where is the why? A permission prompt asked me to decide, and kept the reason](#where-is-the-why), [The Mandate Stack: a multi-agent system in production, layer by layer](#the-mandate-stack), [Why my agents do not run on my laptop: chat, Cowork and Code in the cloud, a vault as the shared drive, and the two walls an operating system has](#why-my-agents-do-not-run-on-my-laptop), [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](#the-agent-team-as-it-runs), [A personal agent that keeps your secrets: the 2026 agents read through behaviour policy and encryption, and a privacy-first design on vaults, enclaves and the browser](#a-personal-agent-that-keeps-your-secrets), [Send an agent, not a spreadsheet: the next generation of software due diligence, and why the companies that stopped reading their code are about to be asked about it](#send-an-agent-not-a-spreadsheet), [If somebody built a company on code review: how I would do it, and why it is only now possible](#if-somebody-built-a-company-on-code-review), [The identity we wanted to give the agents: a week of design, the line in Google's terms, and why login plus secrets is still too hard](#the-identity-we-wanted-to-give-the-agents), [The wall under the reply: end an email with the state of the thread, not the thread](#the-wall-under-the-reply), [Memory is not a spectator sport: how a web of open sites, graphs and vaults became the memory for sessions like this one](#memory-is-not-a-spectator-sport), [Replicating the agentic inbox: a walkthrough from one Claude session to a team of agents that never press send](#replicating-the-agentic-inbox), [Footprint and blast radius: what the agent actually did, and what it would have cost](#footprint-and-blast-radius), [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](#custom-uis-are-not-the-exception), [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](#ultimate-insider-three-collisions).

## [Sixteen thousand fetches, ten clicks, and a token bill nobody is sending: the case for paying publishers to be easy to read](token-bill-nobody-is-sending.md)

2026-09-28 · News & evidenceGraphs & knowledge

The fetches that answer engines make are a token cost to the fetcher as well as a loss to the publisher, and a publisher who serves structure is saving the provider money it already spends, so a share of that saving is owed.

*[diagram]*
**concept**claim**method**example**question

**16 nodes, 20 edges**

- **Sixteen thousand fetches, ten clicks** (example) A week of Cloudflare AI answer retrievals for baekdal.com came to 16,000 requests and the referrals they sent back came to 10.
- **The commons reading** (concept) The answer engines graze on a shared field and give nothing back, so the field will be fenced and the grazing priced.
- **The second reading** (claim) Those 16,000 fetches are also a cost to the fetcher, because every one is a page of HTML parsed, extracted and turned into tokens.
- **HTML against markdown** (claim) On this site's 183 pages the markdown twin is 62% fewer tokens than the HTML, and Cloudflare's own example is 81%.
- **The re-fetch waste** (claim) More than half of legitimate bot crawl traffic re-fetches pages that have not changed, and more than 90% of pages crawlers process are unique, which defeats the cache layer.
- **The arithmetic** (example) Sixteen thousand fetches a week of HTML is about 113 million tokens against 43 million as markdown, tens of dollars a week for one site and a line on a very large invoice across the web.
- **A markdown twin and a map** (method) Every page served as clean markdown at a predictable address, with an llms.txt at the root, generated from the same source so the two cannot drift.
- **A date and a hash** (method) Tell the fetcher when the page last changed and give it a hash, so a fetch of an unchanged page can be skipped altogether.
- **Frozen, hashed sources** (method) Claims that carry the byte range and SHA-256 of the page they came from do the verification round trip once for everyone.
- **A typed graph** (method) A fractal semantic graph lets an agent load exactly as much as the question needs, so the tokens saved are the page minus the answer.
- **Every rail prices the content** (claim) Pay per crawl, RSL, the IAB's protocols, Microsoft's marketplace, Perplexity's pool and Cloudflare's pay per use all price the fetch or the citation, and none pays a site for being cheap to read.
- **The exchange** (claim) A provider that spends fewer tokens reading a site that serves structure has saved money it was already spending, and should hand part of the saving back as a rebate for the format.
- **Tokens as currency** (concept) A publisher could be paid in the provider's own credits, which are the budget that builds the site, and News Corp already took part of its deal in credits.
- **The broker** (concept) A single site cannot send the invoice, so the broker will be whoever sits between the bots and the sites, which today means Cloudflare, TollBit and the marketplaces.
- **Baekdal wants an audience** (question) Tokens are not an audience, though structure is what makes a citation land on the right paragraph and tokens are the budget that builds the site the reader arrives at.
- **What would settle it** (question) Three numbers per domain for a week of real retrieval, the tokens spent on HTML, the tokens the twin would have cost and the fetches a change signal would have skipped, live in the providers' logs.

> Every step exists today. What does not exist is anyone paying for them. The gap the proposal is written to fill: the publisher's half of the exchange is already built.

> It is not new money. It is money being spent today, by the answer engines, on reading the web the hard way. Why a rebate on waste is the easiest money in the negotiation to agree to.

builds on [The future of news is the story vault, not the paywall](#future-of-news-story-vault-not-paywall), [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](#introducing-fractal-semantic-graphs); continued by [The agent is the reader: why agents will pay for graphs, personas and signed claims, because it is cheaper than not paying](#the-agent-is-the-reader), [Who will game the reading meter? Eight kinds of reader, nine ways to cheat, and the risks that will actually happen](#who-will-game-the-reading-meter), [A meter in the browser: a penny a page, a history you keep, and a site that picks for you](#a-meter-in-the-browser), [Liquid content needs water: liquefy the journalist's notebook, not the finished product](#liquid-content-needs-water), [Memory is not a spectator sport: how a web of open sites, graphs and vaults became the memory for sessions like this one](#memory-is-not-a-spectator-sport), [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](#custom-uis-are-not-the-exception), [The reader was always the product: a corrected history of how news got into this mess](#how-news-got-here).

## [A supply chain of vaults: how GenAI, open data and small custom tools could bring the price of food down](supply-chain-of-vaults.md)

2026-09-27 · Vaults & methodStartups & strategy

The food chain is logistics, logistics is a data problem, and a supply chain of encrypted vaults with small custom tools built once by GenAI could bring the price of food down, if somebody runs the experiment.

*[diagram]*
**concept**claim**method**artefact**example**question

**16 nodes, 19 edges**

- **The food pound** (example) For a kilo of supermarket apples selling at £2.20, the grower's costs were 76p and their profit 3p.
- **A chain of spreadsheets** (claim) Each hop keeps its own record of the same consignment, mostly in spreadsheets, and an order, a delivery note, a grade, a price and a payment date are typed in five times.
- **Food lost before retail** (example) The FAO puts the share of food lost between harvest and retail at 13.3% in 2023, and a good deal of it is information.
- **The chokepoint** (concept) Once a buyer holds a large share of a farm's output it names the price, which is the mechanism Giblin and Doctorow call a chokepoint.
- **The limit of regulation** (claim) Codes of practice regulate the conduct of the party with the systems and leave the party without them exactly where it was.
- **All of it is logistics** (claim) Everything between the field and the shelf is a workflow, and logistics is a data problem before it is a transport problem.
- **A supply chain of vaults** (method) Every party in the chain holds its own encrypted, versioned vault, readable by nobody who does not hold a key, including the host.
- **Append lanes** (artefact) Write-only channels through which one party can put a file into another's vault without being able to read anything there.
- **One graph across the vaults** (concept) Each vault keeps its own vocabulary and typed edges join them, which is what makes waste visible.
- **Use GenAI not to use GenAI** (method) The model is used once, to turn a grower's brief into a working tool, and production runs on plain files with no model in the line.
- **Villagers and town planners** (concept) A small company takes the finished tool and runs it for a hundred other growers, paid because it keeps working rather than by the seat.
- **The price hypothesis** (question) The hypothesis is that a supply chain run this way brings the price of food and goods down, and the evidence is partial.
- **The deflation dogma** (claim) The BIS found the link between falling goods prices and lower growth to be weak, and a cheaper loaf because the chain wasted less is not a Japanese lost decade.
- **The cost of not sharing** (claim) About 80% of industrial data is never used, and every grower who learns what a buyer will reject learns it alone.
- **Open-weight models** (concept) Companies that build on open weights can run a near-frontier model inside their own environment and innovate on top of it.
- **The experiment** (question) Nobody has put a grower, a packer and a buyer on vaults and run a season through them, and this article is the brief for that experiment.

> Everything between the field and the shelf is a workflow, and every workflow is a set of records moving between parties. The step that turns a food price problem into a data problem the vaults can address.

> What we never calculate is the economic cost of not sharing. The second memo's argument, that openness is the other half of the case.

builds on [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](#introducing-fractal-semantic-graphs), [The SaaS apocalypse will be decided by inertia, not by AI](#saas-apocalypse-decided-by-inertia-not-by-ai); continued by [The Mandate Stack: a multi-agent system in production, layer by layer](#the-mandate-stack), [The deck I could not download: an author-first home for presentations, as a business plan somebody else can build](#the-deck-i-could-not-download), [Send an agent, not a spreadsheet: the next generation of software due diligence, and why the companies that stopped reading their code are about to be asked about it](#send-an-agent-not-a-spreadsheet).

## [Every risk is already accepted. The only question is by whom, and for how long.](every-risk-is-already-accepted.md)

2026-09-24 · Agents & policyGraphs & knowledge

Every risk an organisation has is already accepted by somebody, so the only questions are who has accepted it and until when; a register that cannot answer them, on facts, is disconnected from reality.

*[diagram]*
**concept**claim**method**artefact**example

**15 nodes, 19 edges**

- **Every risk is already accepted** (claim) A risk exists the moment the exposure does, so the organisation is carrying it from the start, signed for or not.
- **There is no deny button** (claim) You cannot vote a fact out of existence, and a register that lets you reject a risk lets you pretend.
- **Three doors** (method) Accept it personally for a stated interval, fund the work that reduces it, or fix it so the facts that make it true stop holding; silence is not a fourth door.
- **Unaccepted is critical** (claim) A risk nobody has accepted rests on whoever is nearest and rolls upward to their boss, and then to theirs, until somebody signs.
- **The interval is the decision** (method) One hour means more data, four hours is a priority-one incident, one month is assemble and fund, and six months is do nothing and review it then, with a name on it.
- **Accepted is not acceptable** (concept) Accepted is an act by a named person on a date for an interval; acceptable is a threshold, and the dangerous state is a risk over the line that nobody has signed for.
- **EU AI Act, Article 9(5)** (example) Providers of high-risk AI systems must have residual risk judged to be acceptable, and the Act never defines the word.
- **Every risk has a boss** (claim) Every risk has a holder, every holder has a boss, and every path ends at the board, computed rather than reported, and nobody can accept on anybody else's behalf.
- **Risk Graph Explorer** (artefact) A vault that computes what each role is assigned and what arrives through it, so no risk is orphaned and nobody at the top is surprised.
- **From the board to the bytes** (concept) A board line such as loss of customer funds opens into business, operational and technical risks, each with its own holder and vocabulary, down to the configuration file.
- **Established by facts, ended by facts** (method) Every risk names the facts that make it true and the facts that would end it, so it ships with its own falsification condition.
- **One risk, six weeks** (example) An agent's irreversible production writes are accepted for two weeks, expire with the action undone, escalate, are funded, materialise as an incident and cease on day 42 on evidence.
- **A vault per risk** (artefact) Each material risk deserves a vault as its evidence pack, keeping every fact, acceptance, escalation and incident, readable by each audience with its own key.
- **Why people resist** (concept) Executives resist giving risk owners an acceptance workflow because they understand it would change their job, which makes this a change programme rather than a feature.
- **It fits alongside every GRC platform** (claim) The model reads the register from the platform and writes back what the platform lacks: who accepted, until when, what happens at expiry, and a link to the evidence.

> Every acceptance is for an interval, and the interval is not a detail of the decision. The interval ladder is the model's working part: each length names a different response.

> Nothing in the row is wrong. It just never learned that the risk was accepted twice, expired once, escalated, funded, materialised as an incident, and ended. The air gap between a register and reality, shown on one row at one moment.

builds on [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](#introducing-fractal-semantic-graphs); continued by [Where the platform draws the line: Microsoft Execution Containers, the shared responsibility model for agents, and the business logic above it](#where-the-platform-draws-the-line), [The same argument, in our words: Satya Nadella on models as insider risks, translated into the language of RiskMandate](#the-same-argument-in-our-words), [Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan](#authority-outside-the-model), [One article, five readers: a librarian, a cartographer, a historian, an explainer and a storyteller read the same piece](#one-article-five-readers), [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](#riskmandate-ten-questions), [Agency is not a yes: a scale for human and agent decisions, from rubber stamp to the reviewer who fixes the source](#agency-is-not-a-yes), [Who are you protecting against? Draw the security line where the attacker is, not above it](#who-are-you-protecting-against), [Every mistake added a rule: complexity, agents, and the way back to shipping](#every-mistake-added-a-rule), [Zoom into an agent's behaviour policy and you find the business logic](#the-behaviour-policy-is-the-business-logic), [An open AI governance framework, and what its licence let us build](#ai-baseline-control-framework), [Where is the why? A permission prompt asked me to decide, and kept the reason](#where-is-the-why), [The Mandate Stack: a multi-agent system in production, layer by layer](#the-mandate-stack), [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](#the-agent-team-as-it-runs), [The investigation GitHub owes its customers: why a global outage of a platform the world deploys through deserves an aviation-style inquiry, and how the evidence could now be gathered](#the-investigation-github-owes-its-customers), [Send an agent, not a spreadsheet: the next generation of software due diligence, and why the companies that stopped reading their code are about to be asked about it](#send-an-agent-not-a-spreadsheet), [Code review as a fractal semantic graph: source code is already one, and the review should read every layer of it](#code-review-as-a-fractal-semantic-graph), [Footprint and blast radius: what the agent actually did, and what it would have cost](#footprint-and-blast-radius), [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](#ultimate-insider-three-collisions).

## [Before you give an agent a connector, give the connector a twin](connector-twin-before-you-deploy-an-agent.md)

2026-09-24 · Agents & policyVaults & method

If you cannot say what your agent did, what it saw when it did it, and which of its actions you can undo, you are not ready to give it a connector, and a twin of the connector, a journal plus a replay, answers all three.

*[diagram]*
**concept**claim**method**artefact**example**question

**15 nodes, 19 edges**

- **A connector is a grant of action** (claim) An agent with Gmail and Calendar connectors can send, archive, trash, permanently delete, move events, decline invitations and cancel meetings on somebody's behalf, at machine speed.
- **The platform keeps no way back for some actions** (claim) The Gmail API documents its delete as permanent, Undo Send is a feature of the interface not the API, and a moved calendar event has no version history a user can open.
- **What the platform keeps** (concept) Trash windows, an administrator's bulk restore and audit logs record that things happened, but none records what the agent saw when it decided to act, or why.
- **Connector twin** (concept) A journal of every request and response the agent makes, and a replay of that journal into the views the agent saw.
- **Twin, not backup, log or replay** (concept) A backup copies the mailbox, a log is too small, replay is the verb; a twin is an interface to reality, valued for its connection to the real thing.
- **Capture** (method) For every connector call, copy the tool call the agent made, the request sent to the platform and the response received, and never the Authorization header or any token.
- **Append lane** (artefact) A write-only channel gated by a token the writer holds, whose write response is exactly {"ok": true}, so the capture point learns nothing about what else is in the lane.
- **Chain** (method) Each entry carries the hash of the one before it, so a missing, edited or reordered entry shows to anyone holding the read key.
- **When the journal gets processed** (question) On a timer, on a threshold of pending entries, on demand or at the end of each session; the right default will come from a few real users rather than from more design.
- **Replay and revert** (method) A vault app rebuilds the inbox and the calendar as the agent saw them at any step, shows before and after for every change, and writes a revert plan a person approves.
- **The twin is not a copy of the mailbox** (claim) It holds only what passed through the connector, so it scales with the agent's activity rather than with the size of the mailbox.
- **One session, replayed** (example) An invented scheduling assistant makes seventeen calls in under three minutes and writes a true summary that hides a cancellation sent to a supplier and a permanently deleted payment reminder.
- **Undo is a list, not a promise** (claim) Every change gets a grade, reversible, partly reversible or not reversible, and the value of the list is that the red rows are named.
- **Broker, gateway or requirement of the agent** (concept) Three places to capture and three grades of evidence; the mode does not change what is captured, it changes what the evidence is allowed to claim.
- **What it does to the agent's behaviour policy** (concept) With the list of irreversible actions in hand the mandate can say what the agent may do freely, must ask before, and may never do without approval.

> If you cannot say what your agent did, what it saw when it did it, and which of its actions you can undo, you are not ready to give it a connector. The claim the whole article is built to defend, stated so it can be wrong.

> The value of the list is not that most of it is green. It is that the red rows are named. Why the twin changes governance: irreversible actions become a named list the mandate can be written against.

continued by [Where the platform draws the line: Microsoft Execution Containers, the shared responsibility model for agents, and the business logic above it](#where-the-platform-draws-the-line), [The same argument, in our words: Satya Nadella on models as insider risks, translated into the language of RiskMandate](#the-same-argument-in-our-words), [Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan](#authority-outside-the-model), [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](#riskmandate-ten-questions), [Where is the why? A permission prompt asked me to decide, and kept the reason](#where-is-the-why), [The Mandate Stack: a multi-agent system in production, layer by layer](#the-mandate-stack), [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](#the-agent-team-as-it-runs), [A personal agent that keeps your secrets: the 2026 agents read through behaviour policy and encryption, and a privacy-first design on vaults, enclaves and the browser](#a-personal-agent-that-keeps-your-secrets), [Send an agent, not a spreadsheet: the next generation of software due diligence, and why the companies that stopped reading their code are about to be asked about it](#send-an-agent-not-a-spreadsheet), [If somebody built a company on code review: how I would do it, and why it is only now possible](#if-somebody-built-a-company-on-code-review), [Replicating the agentic inbox: a walkthrough from one Claude session to a team of agents that never press send](#replicating-the-agentic-inbox), [Footprint and blast radius: what the agent actually did, and what it would have cost](#footprint-and-blast-radius), [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](#custom-uis-are-not-the-exception), [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](#ultimate-insider-three-collisions), [Six agents, one inbox: what a real multi-agent setup taught me about access policies](#six-agents-one-inbox).

## [The future of news is the story vault, not the paywall](future-of-news-story-vault-not-paywall.md)

2026-09-22 · News & evidenceGraphs & knowledge

The story is a graph and the article is a projection, so a newsroom that keeps the graph in a vault can sell five things from it, in pence and on demand, that reward investigative reporting rather than the click or the renewal.

*[diagram]*
**concept**claim**method**artefact**example

**16 nodes, 21 edges**

- **Both models are bad for the reader** (claim) Advertising sells the reader to somebody else, so the content is bait; a subscription charges rent on something most subscribers have stopped using, so the content is the excuse.
- **The two clocks** (example) Organic Google search traffic to publishers fell 33% in the year to November 2025, and the UK's subscription rules were brought forward to 1 January 2027.
- **The objective is a loop, not a price** (concept) A commercial model that rewards investigative journalism, so evidenced reporting drives usage, usage drives revenue that depends on neither search nor renewals, and revenue funds more reporting.
- **Why paying per item failed before** (concept) A $100 subscription lost is 500 micropayments to replace, unbundling breaks the cross-subsidy, and the reader will not stop to decide whether an article is worth twenty pence.
- **Who is standing at the till** (concept) The reader who wants one thing, the firm that has to forward it with its provenance, and the agent paying per query with a wallet and no anxiety; none of them wants the article.
- **The story is a graph, the article is a projection** (claim) A story being reported is claims, evidence, sources, raw materials, analysis and drafts, and the article is one walk through that graph for one audience at one moment.
- **The graph is fractal, and meaning comes from connectivity** (concept) A node means nothing on its own, every edge is a verb with a named inverse, and zooming into any node enters a world with its own vocabulary joined by a single named edge.
- **Trust through provenance, provenance via evidence** (concept) Evidence is frozen bytes with a SHA-256 hash, provenance is the path from a claim down named edges to that evidence, and trust is what a market extends to a source whose provenance has held before.
- **What a story vault holds** (artefact) The published text, the evidence it cites, the story graph it belongs to, the source list, the translations and every prompt and decision that produced it, as one addressable unit.
- **Anonymous sources are marked at the node** (method) A source the journalist cannot name is a node flagged as anonymous, so every projection built from the graph redacts it automatically.
- **Five things to sell from one graph** (concept) The public article free as the door, the licensed article in pence, the evidence vault, the customised projection and the verification API.
- **The evidence vault** (concept) The graph itself, licensed by read key to analysts, lawyers, regulators and other newsrooms, which is the payment that rewards the reporting rather than the click.
- **The verification API** (concept) A company or agent asks whether a claim was reported, is still current and is soundly used, and gets an on-record answer with the chain attached and a warranty.
- **Who gets paid** (concept) 60% to the original researcher, 25% to the data organisation, 10% to the journalist and 5% to the outlet, and you cannot pay the fact creator unless the graph names them.
- **The rails** (concept) The x402 protocol puts a payment inside the HTTP 402 response, settles in about 200 milliseconds and charges no protocol fee, so paying in pence now works.
- **The parts that already run** (example) Hash-verified regulation graphs, a Portuguese newsroom with frozen sources and an editor-gated pipeline, a pentest sold as eight projections, and thirty-one vaults on 295 MB, with the billing not built.

> The news industry sells the one thing whose price is going to zero, the article, and throws away the one thing nobody else has, the evidence the article was made from. The claim stated so it can be wrong; everything else is its long form.

> The story is a graph. The article is a projection. Sell the graph. The shift the five products follow from, in three sentences.

builds on [For a startup, the most important question is whether they miss it](#the-question-is-whether-they-miss-it); continued by [The agent is the reader: why agents will pay for graphs, personas and signed claims, because it is cheaper than not paying](#the-agent-is-the-reader), [Liquid content needs water: liquefy the journalist's notebook, not the finished product](#liquid-content-needs-water), [Story vault underneath, Reader Skills on top: why local journalism has the most to gain](#story-vault-meets-reader-skills), [The deck I could not download: an author-first home for presentations, as a business plan somebody else can build](#the-deck-i-could-not-download), [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](#custom-uis-are-not-the-exception), [The reader was always the product: a corrected history of how news got into this mess](#how-news-got-here), [Sixteen thousand fetches, ten clicks, and a token bill nobody is sending: the case for paying publishers to be easy to read](#token-bill-nobody-is-sending).

## [For a startup, the most important question is whether they miss it](the-question-is-whether-they-miss-it.md)

2026-09-21 · Startups & strategy

A startup operating model in three pillars: be profitable, make investors come to you, and open source everything, each buying the position needed for the next.

*[diagram]*
**concept**claim**method**artefact**example**question

**14 nodes, 16 edges**

- **Three pillars** (concept) Be profitable, have investors talking to you, and open source everything, in that order because each one buys you the position you need to do the next.
- **Ship** (method) Shipping means a thing somebody else can go and use, on their own, and get value from, not a proof of concept or a demo.
- **Near-zero running cost** (method) To ship that often the running cost must be near nothing: serverless, as little live state as you can stand, and in our case the file system is the database.
- **Give it away** (method) Hand it to people for free for a short window, because the feedback starts the moment somebody who is not you has the thing.
- **Take it away** (method) The trial expired, it is not available right now, nothing else about the product changes, and no apology is needed.
- **Do they miss it?** (question) If they shrug you have something people will accept when it is free; if they come back and ask for it, you have something.
- **Charge, and charge at a profit** (claim) Two questions, is the price one they are happy to pay and is that price profitable for you, and people routinely answer only the first.
- **No subscription by default** (claim) Charging rent for something people are not using is a worse business than being paid when you deliver.
- **Raise from strength** (claim) The worst possible time to raise money is before you are profitable, because you are bargaining from weakness and the worst terms are about control.
- **Do not get signed before you have the album** (example) Write the songs, record them, get people buying, then take the record deal as somebody who already has an audience.
- **Open source everything** (method) It sounds like giving away the asset and is the opposite, for five reasons that each stand alone.
- **The technology is not the moat** (claim) Treating it as open from the start forces you to find the thing that actually is defensible, usually the data, the relationships, the distribution, or the speed at which you ship.
- **You leave with your tools** (claim) Build in the open and the work is still yours when you move on.
- **The vault as substrate** (artefact) A vault carries data, app, history and sources as one string, with no database to run and no hosting for the reader, so shipping a small product is cheap, fast and reversible.

> It means a thing somebody else can go and use, on their own, and get value from. The definition of shipping that the whole loop depends on.

> The worst possible time to raise money is before you are profitable, before you have the product, before you understand the fit. Pillar two stated plainly, and the reason profitability comes first.

builds on [Price it, then give it away: the early access programme as the next step after "do they miss it"](#price-it-then-give-it-away); continued by [Going live with the reading meter: pay for what you read, go below zero if you like, and the numbers we will check in eight weeks](#going-live-with-the-reading-meter), [A meter in the browser: a penny a page, a history you keep, and a site that picks for you](#a-meter-in-the-browser), [If somebody built a company on code review: how I would do it, and why it is only now possible](#if-somebody-built-a-company-on-code-review), [Price it, then give it away: the early access programme as the next step after "do they miss it"](#price-it-then-give-it-away), [The future of news is the story vault, not the paywall](#future-of-news-story-vault-not-paywall).

## [The SaaS apocalypse will be decided by inertia, not by AI](saas-apocalypse-decided-by-inertia-not-by-ai.md)

2026-09-21 · Startups & strategy

AI is available to both sides, so the SaaS apocalypse will be decided by inertia: where each company sits on the evolution axis and how much past success it has to protect.

*[diagram]*
**concept**claim**example

**15 nodes, 20 edges**

- **The claim, stated so it can be wrong** (claim) Most medium and large SaaS companies will struggle, spectacularly, in the medium term, as companies and individuals build more of what they actually want instead of renting an approximation of it.
- **AI is available to both sides** (claim) The incumbents have the same models the newcomers have, plus more data, more engineers and more money, and if the technology decided this they would already have won.
- **Success breeds inertia** (concept) Wardley's climatic pattern: the pre-existing installed base causes inertia to change, and it is almost always new entrants, unencumbered by past success, who initiate it.
- **Nokia, twice** (example) Nokia met the mobile phone with nothing to protect and dominated for fifteen years; it met the iPhone with fifteen years of success to protect and was gone from the category within seven.
- **The SaaSpocalypse of February 2026** (example) Roughly $285 billion left the sector in about 48 hours after Anthropic shipped Claude Cowork plug-ins, and by September software stocks had rallied about 40% from the April low.
- **The database is the moat** (claim) Investors decided the thing underneath was safe and quietly stopped defending the thing on top; that is not a rebuttal of the apocalypse, it is the apocalypse, priced.
- **Users were never happy** (claim) 91% of employees are frustrated with workplace technology, 80% of features are rarely or never used, and the average organisation wastes $21 million a year on unused licences.
- **The persistence of Excel** (example) 73% of companies prepare VAT returns in Excel; its persistence is the clearest evidence that SaaS failed users, because it is the one tool where they control the shape of the thing.
- **The SaaS product slid right** (concept) On the map, what was a product is commoditising into a substrate, a database, a message bus, a state machine, on which higher-order things get built.
- **Vibe coding is writing good briefs** (concept) Product owners were always describing the software they wanted; the loop from I want this to here it is was weeks or months, and is now minutes.
- **Why incumbents cannot simply do this** (claim) SaaS companies never invested in non-functional requirements, engineers spend 42% of their time on maintenance and bad code, and only 19% of teams are elite performers.
- **The irony** (claim) The things SaaS companies refused to build to protect their moats, portability, open schemas, a real API, data you can take out, are precisely the things an agent needs.
- **The brief is not a product** (claim) The reason you bought SaaS was never the features but that the thing is maintained, and the person who vibe coded a replacement does not want to maintain it.
- **Village and town-planner companies** (concept) Businesses that take the finished brief and run it, maintain, secure, version and deploy it, paid by consumption rather than by the seat, where the handover is a file move plus a version bump.
- **More engineers, not fewer** (claim) We will need as many developers as now and probably more, because somebody has to read, harden and run the code, and larger human-agent teams become possible once communication can be scaled.

> AI is not the deciding factor, because AI is available to both sides. The title's argument in one line: the variable both the panic and the recovery stared at was the wrong one.

> The things SaaS companies refused to build, to protect their moats, are precisely the things an agent needs. The irony the article calls the whole piece in one paragraph: the moat is now what the customer's agent cannot get past.

continued by [From me to you, in a link: a personal reading list, two briefs to build and use it, and the loop that makes it a day's work](#a-reading-list-in-a-link), [The deck I could not download: an author-first home for presentations, as a business plan somebody else can build](#the-deck-i-could-not-download), [If somebody built a company on code review: how I would do it, and why it is only now possible](#if-somebody-built-a-company-on-code-review), [A supply chain of vaults: how GenAI, open data and small custom tools could bring the price of food down](#supply-chain-of-vaults).

## [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](introducing-fractal-semantic-graphs.md)

2026-09-20 · Graphs & knowledge

Every unit of knowledge is already a graph in its owner's vocabulary, and a short shared grammar rather than a shared schema is what lets any node in one world link to any node in another, up or down, without an adapter.

*[diagram]*
**concept**claim**method**artefact**example**question

**15 nodes, 18 edges**

- **Fractal Semantic Graph** (concept) A fractal semantic graph has no privileged level and no single schema; zoom into any node and you enter a new world with its own node types, verbs and taxonomy.
- **Semantic graph** (concept) A semantic graph gives the edges meaning: every edge is a verb, and every verb has a named inverse, so a link reads correctly from whichever end you are standing at.
- **Ontology** (concept) An ontology is the agreed vocabulary of node types and verbs that a graph is allowed to use, and each altitude gets its own.
- **The jump** (method) On one link in a risk register you can jump into another universe, from an incident to security operations to the DNS estate to a single TCP packet, and nobody built an adapter.
- **Everything is already a graph** (claim) A regulation, a PDF, a spreadsheet, a codebase and a JSON document are already graphs; each one only needs its edges named.
- **The five-rule grammar** (method) Every edge is a verb with an inverse, relates_to is banned, properties carry data never meaning, supersede never delete, and never render the whole graph.
- **relates_to is banned** (claim) An edge with no verb constrains nothing and cannot narrow a query; the granularity of the verb is the precision of the question you will later be able to ask.
- **Provenance comes free** (claim) When the leaf is a word connected to the byte range it came from and the hash of the file that held it, every claim at every altitude above it is traceable to source.
- **The ladder of eleven altitudes** (artefact) Eleven altitudes, each a live graph in its own vocabulary, from the law down to the compute instance, every altitude joined to the next by a named edge.
- **Regulation Graph** (artefact) The EU AI Act parsed from the official XML into 1,523 nodes and 1,944 edges, with the SHA-256 of the retrieved bytes at the end of every provenance chain.
- **The crosswalk finding** (example) Joining the AIUC-1 standard to the regulation graph showed that 8 of the 27 articles reached have since been amended, a finding that existed in neither graph on its own.
- **GDPR Article 45** (example) The text has not changed a word since 2016 while what it permits has flipped four times, drawn as a timeline of ruling nodes over one unchanged article node.
- **Threat model zoom ladder** (artefact) Eleven linked models, 51 nodes and 179 threats, tracing a single SQL injection from the method it lives in to the revenue it puts at risk.
- **What is still modelled rather than imported** (question) The bottom four altitudes are placed by an author, enterprise architecture is missing, crosswalks resolve at article level only, and the agent altitude is a vocabulary not yet a join.
- **Why now** (claim) Naming edges became the cheap part, agents acting on the world make provenance mandatory, and the schema wars are over because nobody won.

> There is no top and no bottom. There is only the altitude you happen to be looking from, and how much definition you choose to load at it. The definition of fractal in one line: no privileged level, no single schema.

> Two graphs, built by different people for different purposes in different vocabularies, joined by declared edges, produced a finding that did not exist in either of them. The evidence that the method does work, not just that it is defined: the amended-articles finding came from the join.

continued by [The agent is the reader: why agents will pay for graphs, personas and signed claims, because it is cheaper than not paying](#the-agent-is-the-reader), [One article, five readers: a librarian, a cartographer, a historian, an explainer and a storyteller read the same piece](#one-article-five-readers), [The AI governance stack, as a graph: an answer to Hari Kota, built](#the-ai-governance-stack-as-a-graph), [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](#riskmandate-ten-questions), [Agency is not a yes: a scale for human and agent decisions, from rubber stamp to the reviewer who fixes the source](#agency-is-not-a-yes), [Liquid content needs water: liquefy the journalist's notebook, not the finished product](#liquid-content-needs-water), [Zoom into an agent's behaviour policy and you find the business logic](#the-behaviour-policy-is-the-business-logic), [An open AI governance framework, and what its licence let us build](#ai-baseline-control-framework), [The Mandate Stack: a multi-agent system in production, layer by layer](#the-mandate-stack), [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](#the-agent-team-as-it-runs), [A personal agent that keeps your secrets: the 2026 agents read through behaviour policy and encryption, and a privacy-first design on vaults, enclaves and the browser](#a-personal-agent-that-keeps-your-secrets), [How much of this did I write? The numbers behind twenty articles in four weeks, and what the input actually was](#how-much-of-this-did-i-write), [If somebody built a company on code review: how I would do it, and why it is only now possible](#if-somebody-built-a-company-on-code-review), [Memory is not a spectator sport: how a web of open sites, graphs and vaults became the memory for sessions like this one](#memory-is-not-a-spectator-sport), [Code review as a fractal semantic graph: source code is already one, and the review should read every layer of it](#code-review-as-a-fractal-semantic-graph), [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](#custom-uis-are-not-the-exception), [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](#ultimate-insider-three-collisions), [The reader was always the product: a corrected history of how news got into this mess](#how-news-got-here), [Sixteen thousand fetches, ten clicks, and a token bill nobody is sending: the case for paying publishers to be easy to read](#token-bill-nobody-is-sending), [A supply chain of vaults: how GenAI, open data and small custom tools could bring the price of food down](#supply-chain-of-vaults), [Every risk is already accepted. The only question is by whom, and for how long.](#every-risk-is-already-accepted).

## [The proof moved up, the homepage after the rebuild, next to the before pictures](proof-moved-up.md)

2026-09-07 · Site & engineeringVaults & method

The homepage stopped being a page somebody edits and became a view over the site's own data, with real vaults placed before the mechanism and the one unproven claim left unpretended.

*[diagram]*
**concept**claim**method**artefact**example**question

**12 nodes, 14 edges**

- **The reframed sentence** (claim) The hero changed from "the encrypted git for humans and AI agents" to "a vault is a unit of work: data, app, history and sources, shipped as one string", with encryption as the subordinate clause.
- **Four real vaults in the hero** (artefact) Four published vaults with their screenshots sit under the sentence, chosen by a hero field in the vault data, so changing the front door is a data edit, not a page edit.
- **What people actually ship** (artefact) Six vaults chosen by the job they do, hand over a report, publish a standard, give a talk, pitch an investor, ship a game, give an agent a workspace, and none of the six lines is about encryption.
- **A vault as a unit** (concept) Retest scripts that travel with the findings and cited papers that never separate from the deck are properties of a vault as a unit, which a newcomer can actually feel.
- **One human, a team of agents** (artefact) A band with four numbers computed at build time, releases, vaults, sibling sites, briefs, and the loop told in three beats with the artefacts linked.
- **The numbers are not typed** (method) Releases come from the version log, vaults from the vault data, sites from the network directory and briefs from the briefs page, so a wrong number means the site is wrong somewhere else too.
- **What was cut** (example) The abstract use-case band and the three-doors band were cut, and the terminal walkthrough moved down under the heading Under the hood, it is git.
- **Nine bands before, nine after** (example) Three bands were cut and three added, corrected in v0.2.61 after counting rather than remembering, and 1,370 words became 1,332 with ten screenshots.
- **What it cannot show yet** (question) No published vault demonstrates two agents on one vault, their branches and a human merging them, and the team band is written so that it does not pretend otherwise.
- **admin/content/vaults.json** (artefact) One file now drives the hero cards, the six jobs, the sortable table and the vault count; adding a vault is adding a row and promoting one is setting a field.
- **The homepage as a view over data** (claim) The homepage stopped being a page somebody edits and became a view over the site's own data, the rule the articles band, network directory and update feed already followed.
- **Beside the before pictures** (method) The rebuild is put next to the previous article's screenshots so the comparison can be made honestly, including what it still cannot show.

> If a number on that band is wrong, the site is wrong somewhere else too, and that is the right dependency. The rule behind the rebuild: nothing on the homepage is typed, everything is computed from the site's own records.

> That is the trade: pictures of real things instead of paragraphs about them. What actually changed, stated against the byte and word counts rather than as a slogan.

builds on [The proof is two clicks behind the claim, what the homepage gets wrong, and the fix](#proof-behind-the-claim).

## [The proof is two clicks behind the claim, what the homepage gets wrong, and the fix](proof-behind-the-claim.md)

2026-09-07 · Site & engineeringVaults & method

Encryption is a property you cannot look at, so the homepage should put the real vaults a visitor can open before the mechanism, and should not carry a claim that no published vault demonstrates.

*[diagram]*
**claim**method**artefact**example**question

**13 nodes, 15 edges**

- **Twenty-five published vaults** (artefact) Three weeks ago the site had four published vaults; today it has twenty-five, built by several agents working with one human, including a pentest report with a retest script per finding and a standard rebuilt as a citable graph.
- **Encryption is a property you cannot look at** (claim) Zero knowledge cannot be seen either, so the visitor is asked to take the value on faith before being shown anything.
- **The terminal walkthrough** (example) The hero's create, commit, history and clone walkthrough demonstrates familiarity, which is a virtue, but not power.
- **Use cases as categories** (example) Five use-case cards, each a category rather than a thing, while the vault that embodies the category sits one level down.
- **The proof is a table, two clicks away** (claim) A table is the right shape for finding a vault and the wrong shape for being convinced by one, and it is under a dropdown two clicks from the hero.
- **Opened by one string** (claim) Both proof vaults are opened by one string, run entirely in the browser, ship with their data, sources and tests, and require the visitor to click rather than to understand encryption.
- **Agents build for each other** (example) A brief published on 6 September was read by another agent who built a vault from it the same day, and the API team's correction is now published above the mistake.
- **The briefs page as a log** (example) The collaboration record is filed under Docs, three levels from the homepage, written as a log, which is the right format for the record and the wrong one for a first-time reader.
- **The claim with no artefact** (question) The homepage says a human reviews the merge of agents' branches, and no published vault shows two agents' branches and a human merge in its history.
- **Reorder so proof comes before mechanism** (method) The hero shows four real vaults as cards, then six vaults chosen by job, then the team story, then the terminal walkthrough and the zero-knowledge explanation.
- **Generated from the same data** (method) The six vaults chosen by job are generated from the same data as the table, so they never go stale.
- **A page that says who is behind it** (artefact) A beta tool that asks people to publish their read keys is asking for trust, so there will be a page about who builds sgit, borrowing Interests declared and Reach me, or correct me from a sibling site.
- **The site card** (artefact) A card describes a sibling site the way it describes itself, from its entry in the network directory, because a bare link does not say this continues elsewhere, on purpose.

> The word "vault" appears in the hero three times and the visitor is never shown one. The diagnosis in one line: the homepage names the thing and never shows it.

> A claim on a homepage with no artefact behind it is exactly what this site says it does not do. The gap the article names against itself: the multi-agent merge claim has no published vault behind it.

continued by [The proof moved up, the homepage after the rebuild, next to the before pictures](#proof-moved-up).

## [A chat box on a site with no server, the plan, and the trade it makes](chat-on-a-static-site.md)

2026-08-27 · Site & engineering

With no server to hold a key, a chat box on a static site has three honest tiers: a local matcher, a key in the reader's browser, or a vault app with a bridge, and only one of those is free.

*[diagram]*
**concept**claim**method**artefact**example**question

**14 nodes, 18 edges**

- **The constraint nobody can design around** (concept) sgit.ai is a static site on GitHub Pages with no server, no session and no place to keep a secret, and every sibling on *.sgit.ai is the same.
- **The catalogue** (artefact) Nineteen theses, summaries and categories, emitted at build time from the same data the cards and the table are built from.
- **Tier 0, match** (method) A deterministic scorer runs in the browser against the catalogue of all nineteen sites and shows you which words it matched on.
- **A reader should never have to hold a credential to use an index** (claim) The property that made the local matcher the default: it is instant, free, private, works offline and tells you why it chose.
- **Tier 1, bring your own key** (method) Paste an OpenRouter key and the browser calls the model directly, streaming, with the catalogue as the system prompt.
- **The key lives in this page's origin** (concept) With no host there is no permission floor, so the key goes into localStorage and a fetch to openrouter.ai, and the page cannot protect it the way a vault app can.
- **Degrade to what works** (method) When the model call fails the panel falls back to Tier 0 and says so, because degrading to something that works beats an error message.
- **The SG/Vault workbench vault** (example) The workbench vault already calls the same OpenRouter endpoint with the versioned sg-llm-request module, so the BYOK client reuses a proven pattern.
- **Tier 2, the bridge** (method) Serve the directory as a vault app so the key lives in .vault/llm/config.json below the permission floor, the host makes the call and the app never sees the credential.
- **Permission floor** (concept) The line below which a vault host keeps the key, with an sg.llm API whose grants default to deny and a chat panel every existing vault app gets without being changed.
- **The bridge protects your key, not all egress** (claim) The bridge protects the credential you trusted it with; it does not yet stop a malicious app calling a provider with a credential of its own.
- **Ask this site** (artefact) Ten days later every page carries a pane whose model is given seven tools that run in the page over an index the build emits, and the pane shows every call it made.
- **One site's copy, not a versioned module** (question) The site-wide pane is still one site's copy rather than a versioned module the other eighteen sites can load, and that row decides whether this was worth doing.
- **Routing, not teaching** (claim) The panel points you at a site rather than answering questions about the subjects, because a summary that drifts from the arguments is worse than a link that does not.

> The important property: a reader should never have to hold a credential to use an index. The rule that makes the free local matcher the default rather than the model.

> A chat box on one site is a feature. The same panel on all nineteen, reading each site's own catalogue, is the thing that makes a network of nineteen sites navigable, and it is why the catalogue is generated rather than written. Why the piece is about a network's navigation rather than one widget.

continued by [No server, by design: first I retired the database, now I am retiring the back end](#no-server-by-design), [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](#custom-uis-are-not-the-exception).

## [Twenty sites in fifteen days, and what that did to the writing](nineteen-sites.md)

2026-08-26 · Site & engineeringVaults & method

A body of work outgrew the site it was published in and split into nineteen siblings so each argument could keep its own version history, and the index into them starts from the reader's question rather than a list of names.

*[diagram]*
**concept**claim**method**example

**12 nodes, 14 edges**

- **Twenty repositories in fifteen days** (example) On 11 August this was one website; by 26 August there were twenty repositories, nineteen of them siblings on *.sgit.ai, fifteen created in the last five days.
- **A section is a promise** (concept) A section promises that something is part of the thing it sits inside, and that promise stopped holding when the writing answered questions that were not about sgit.
- **Its own version history** (claim) Nineteen arguments moving at different speeds through one release log produces a record nobody can read; split, each gets its own record of when it changed its mind.
- **Discovery got worse** (claim) Nineteen domains is not a menu; names like nfrs.sgit.ai and issues-fs.sgit.ai mean nothing until you already know what they argue.
- **Consistency by discipline** (claim) One site has one stylesheet by construction; nineteen have one stylesheet by discipline, and discipline is the thing that quietly stops happening.
- **Cross-link drift** (example) The audit found graphs.sgit.ai pointing at sentinel.sgit.ai, which does not exist; the site is sg-sentinel.sgit.ai, one character of drift and the link is dead.
- **Start from the question** (method) The directory starts from the question the reader arrived with, seventeen lines of it, then five groups by area, then a table of all nineteen.
- **Every thesis in the site's own words** (method) Each thesis on the directory page is quoted from the site's H1 or lede rather than summarised, because a summary drifts and a quotation either matches or is visibly wrong.
- **Same generator, same release script** (method) Same generator, same stylesheet, same release script, same validator, same rule that publishing is adding one file.
- **Publishing is adding one file** (claim) Adding the twentieth site is writing one markdown file, the same property that lets two agents publish on the same day without conflict.
- **skills.sgit.ai, not published yet** (example) One of the nineteen has a repository and a DNS record and nothing behind it, listed as not published yet rather than quietly omitted.
- **Arguments, not products** (claim) sg-sentinel says NOT BUILT, risks states zero lines of code implement its model, wardley-maps is PROPOSED: publish the argument before the thing exists and say what it is worth.

> A summary drifts. A quotation either matches or is visibly wrong. The rule that keeps the directory honest, and the reason the index quotes each site rather than describing it.

> One character of drift, and the link is dead. The concrete cost of splitting: a link between sites is a claim about another site that has to be checked.

builds on [Git for things you cannot put on GitHub](#what-sgit-is); continued by [The Mandate Stack: a multi-agent system in production, layer by layer](#the-mandate-stack).

## [Git for things you cannot put on GitHub](what-sgit-is.md)

2026-08-25 · Vaults & method

sgit gives the files people say they cannot put on GitHub the history, branches and shareable links of git, on a server that holds ciphertext and nothing else.

*[diagram]*
**concept**claim**artefact**example

**13 nodes, 18 edges**

- **Files with nowhere good to live** (concept) A risk register with real system names, a regulatory analysis still being argued about, the working memory of an AI agent, client material under NDA.
- **sgit** (artefact) sgit is git for those files: encrypted before they leave your machine, versioned exactly like git, stored on a server that cannot read a single byte.
- **Zero knowledge, precisely** (claim) The server holds ciphertext and nothing else, not your filenames, not your directory structure, not your commit messages.
- **No key escrow** (claim) There is no key escrow, no admin override, no support engineer who can recover it for you, and that last part is a feature with a real cost.
- **Vault key** (concept) A single string that is three things at once, the address of the vault, the authorisation to write to it, and the key that decrypts it.
- **Read key** (concept) Derived one way from the vault key, same vault, read-only, safe to publish, and that asymmetry is the whole sharing model.
- **Release tripwire** (artefact) No vault key has ever been published, a rule enforced by a tripwire in the release pipeline that scans every file before either remote is touched.
- **Content-addressed over ciphertext** (concept) The object's name is a SHA-256 of the encrypted bytes, so the host can deduplicate it, cache it and serve it from a CDN while unable to tell you what it is.
- **A real version control system** (claim) Multi-parent commits, a tree per directory, deterministic refs derived by HMAC, a genuine merge-base computation and three-way merge, on content the server cannot interpret.
- **Nineteen vaults you can open** (example) Every vault on sgit.ai is live, and cloning all nineteen from their published keys gave 1,389 files and no failures.
- **Capability without credential** (concept) A vault can contain an application that requests no permissions and still renders the whole risk graph, because the host reads the vault and passes results in.
- **The network of sites** (artefact) sgit.ai is one of nineteen sites on *.sgit.ai, each taking one question further than a section could.
- **Checkable rather than impressive** (claim) Each site publishes its argument before the thing exists and states plainly what has shipped and what has not.

> Lose it and the data is gone. Leak it and someone can rewrite your history. The two costs of a vault key being address, authorisation and encryption key at once.

> We would rather be checkable than impressive. The house style that the live vaults, the version log and the NOT BUILT pages all follow.

continued by [Pay to keep your persona: readers should pay because it helps them, not because they feel they should](#pay-to-keep-your-persona), [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](#riskmandate-ten-questions), [Every mistake added a rule: complexity, agents, and the way back to shipping](#every-mistake-added-a-rule), [The Mandate Stack: a multi-agent system in production, layer by layer](#the-mandate-stack), [A personal agent that keeps your secrets: the 2026 agents read through behaviour policy and encryption, and a privacy-first design on vaults, enclaves and the browser](#a-personal-agent-that-keeps-your-secrets), [Twenty sites in fifteen days, and what that did to the writing](#nineteen-sites).

## [Seven vaults, one method](seven-vaults-one-method.md)

2026-08-19 · Vaults & method

A repeatable method for publishing encrypted vaults, each rule learned by getting something wrong first, starting with classifying the credential before it touches anything.

*[diagram]*
**concept**claim**method**artefact**example

**14 nodes, 19 edges**

- **Classify the credential** (method) Classify the credential before it touches anything, because three of the seven vaults arrived as a vault key described as a read key.
- **Vault key** (concept) A vault key is write access, and because it is also the address and the encryption root there is no revocation, no rotation, and no undo.
- **Read key** (concept) A read key is 64 hex characters, derived one-way from a vault key, and safe to publish.
- **check_credential.py** (artefact) A script that classifies a credential by shape, exits 0 for publishable and 1 for stop, and never echoes what it was given.
- **Release validator tripwire** (artefact) The release validator scans every tracked file for any key-shaped string and for the actual passphrases, and has caught its own author three times.
- **Derive rather than refuse** (method) A submission that cannot be published can still become one that can, by deriving the read key and putting the vault key in a gitignored tier.
- **Strictly less capability** (claim) The whole shape of the project is a capability you can hand over that is strictly less than the one you hold, with the reduction enforced by mathematics rather than by policy.
- **Audit with the key you publish** (method) Audit every file with exactly the credential a reader will have, not with the vault key.
- **Sealed LLM credential check** (example) One vault carried a sealed LLM credential, and attempting to open it with the published read key got InvalidTag from AES-GCM, so no budget was exposed.
- **Risk Graph Explorer** (artefact) The sixth vault was public by design, with its own PUBLIC.md whose third rule, no metered capability behind a published read key, was adopted into the guidance.
- **Capture evidence by driving the real product** (method) Every screenshot is taken by opening the actual vault in a real browser with the published read key, and the rig grew an appProbe step to ask the app what its elements are called.
- **Describe, show, then admit** (method) Every vault page ends with what the vault does not do, as a section with the same weight as the features.
- **Publishing playbook** (artefact) The method is written down as a playbook aimed at another site's agent rather than at us, which was the real test of whether it was a method or just a habit.
- **The honest ledger** (claim) Three vault keys caught, one budget exposure checked and cleared, one upstream rule adopted, and three bugs found by testing rather than assumption.

> Which is the point: a rule that only catches other people is not a rule. The tripwire catching its own author is what turns a habit into a control.

> A published vault is an argument that this way of working is sound; an argument that omits its own edges is a brochure. The reason every vault page ends with what the vault does not do.

continued by [The Mandate Stack: a multi-agent system in production, layer by layer](#the-mandate-stack), [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](#custom-uis-are-not-the-exception).

## [Green does not mean live](green-does-not-mean-live.md)

2026-08-17 · Site & engineering

Shipped is a fact about the reader, not about your repository, so a release has to verify the boundary the reader is on and not only the ones the repository can see.

*[diagram]*
**concept**claim**method**artefact**example**question

**12 nodes, 15 edges**

- **Two releases that never reached anybody** (example) Two consecutive releases pushed cleanly, printed both remotes in sync, and the site served a two-release-old page for forty minutes until a human on a phone asked if it was the latest version.
- **The version badge** (artefact) The badge on the home page that a human looked at to notice the miss, and that the release now polls for the new version.
- **Checking the wrong boundary** (claim) The checks were not weak; they were checking the wrong boundary.
- **What the release actually verified** (method) Build the site, run the validator, commit and push the encrypted vault and confirm sync, commit and push the git mirror and confirm HEAD equals origin/dev.
- **The bytes arrived at GitHub** (concept) HEAD == origin/dev compares hashes, not hopes, but it means the bytes arrived at GitHub, not that anybody can read them.
- **Three boundaries, two verified** (concept) Source to git remote, git remote to Pages deploy, Pages deploy to the reader; a GitHub Actions job sits in the unverified gap and reports into a system neither remote knows about.
- **What actually failed** (example) The deploy job died in Set up job because codeload.github.com rate-limited the download of actions/configure-pages with a 429, while the validate and tag-release jobs passed.
- **The most likely thing to break is not your code** (claim) It is a piece of shared infrastructure you do not run, on a day you were not thinking about it.
- **Ask the live site what version it is serving** (method) A release now polls sgit.ai with a cache-buster for the new version, up to eight minutes, and aborts loudly if it never appears, naming the Actions page.
- **Shipped is a fact about the reader** (claim) Shipped is a fact about the reader, not about your repository.
- **Three rules of the same shape** (method) A page nothing links to, a page the machine index omits, and a page the deploy never served are all unpublished, and the build or the release fails on each.
- **What this does not fix** (question) It detects a failed deploy but does not repair one, it checks only the home page's badge so a partial deploy would pass, and it adds up to eight minutes to every release.

> The checks were not weak. They were checking the wrong boundary. The diagnosis: strong checks on the wrong side of the deploy.

> All three are the same claim: shipped is a fact about the reader, not about your repository. The general rule the fix joins, learned from three failures of the same shape.

continued by [Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan](#authority-outside-the-model), [Every mistake added a rule: complexity, agents, and the way back to shipping](#every-mistake-added-a-rule), [The investigation GitHub owes its customers: why a global outage of a platform the world deploys through deserves an aviation-style inquiry, and how the evidence could now be gathered](#the-investigation-github-owes-its-customers).

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/graphs.html)*
