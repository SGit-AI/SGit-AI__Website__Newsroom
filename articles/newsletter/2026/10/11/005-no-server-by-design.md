# Issue 5: No server, by design: a newsroom that runs in your browser, a model in the tab, and the agents that read, test and draw for it, SGit Newsroom

> Everything in the last two issues runs in the reader's browser. First the database was retired and the file system took its place; now the back end is retired too, and what is left on the server side is commodity that holds no logic and cannot read the data. Eight articles on how that works and what it makes possible. Why there is no server, and why that made a business decision possible; Chrome's model in the tab, the hardest remaining piece; where the vault keys live and an RFC for keys a reader cannot write with; and the agents that do the newsroom's work: five readers sent through every article, synthetic users driving a real browser, image models judged blind, and a governance framework kept as a graph.

*Source: <https://newsroom.sgit.ai/articles/newsletter/2026/10/11/005-no-server-by-design.html> · sgit.ai v0.7.61 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../../../index.md) / [SGit Newsroom](../../../../index.md) / [Newsletter](../../../index.md) / Issue 5

SGit Newsroom · Issue 5 · 2026-10-11

# No server, by design: a newsroom that runs in your browser, a model in the tab, and the agents that read, test and draw for it

By [Dinis Cruz](https://sgit.ai/about/index.md), written with the [Journalist](../../../../../newsroom/roles/journalist.md)

***Abstract:** Everything in the last two issues runs in the reader's browser. First the database was retired and the file system took its place; now the back end is retired too, and what is left on the server side is commodity that holds no logic and cannot read the data. Eight articles on how that works and what it makes possible. Why there is no server, and why that made a business decision possible; Chrome's model in the tab, the hardest remaining piece; where the vault keys live and an RFC for keys a reader cannot write with; and the agents that do the newsroom's work: five readers sent through every article, synthetic users driving a real browser, image models judged blind, and a governance framework kept as a graph.*

The reading meter, the personas, the newsroom of your own, the encrypted sharing: none of it runs on a server. This issue is about why, what that takes, and the agents that do the work around it. It is the third of three on what was published between 9 and 11 October, after [pay after you read](https://newsroom.sgit.ai/articles/newsletter/2026/10/11/003-pay-after-you-read.html) and [authority outside the model](https://newsroom.sgit.ai/articles/newsletter/2026/10/11/004-authority-outside-the-model.html).

No server, by design, in six pictures, one from each of six of the articles

## No server, by design

[No server, by design](https://newsroom.sgit.ai/articles/no-server-by-design.html) is the decision in two steps. First the database was retired: the file system is the database, and every intermediate result is a file you can version, diff and read. Now the back end is retired too: the application moves to the browser. What is left on the server side is commodity, static hosting, a vault server that stores ciphertext it cannot read, a payment link, and each is a product, not code of mine:

>

It is no servers of mine with logic in them.

The SGit Newsroom's architecture: every piece of application logic runs in the reader's browser.

It is also what made the reading meter's business decisions possible: a server cannot read the reader's data, so anything that needs to has to happen where the key is, and the gaps that leaves are written down rather than closed.

## A model in the tab

[A model in the tab](https://newsroom.sgit.ai/articles/a-model-in-the-tab.html) is about the hardest remaining piece. Chrome now ships a language model that any page can prompt, offline, on capable desktops. It is real and stable, it has rough edges, and the objections to it from other browser makers are serious. The way to build on it without being captured by it:

>

The way to build on it without being captured by it is to keep the meaning in the data, not in the prompt.

## The keys underneath

If the server cannot read anything, the key is everything. [Where the vault keys live](https://newsroom.sgit.ai/articles/where-the-vault-keys-live.html) is key management as it actually runs: one secret per vault and the keys derived from it, a password manager and a registry kept by its own agent, and new keys that travel sealed on a write-only lane instead of through a chat.

>

The key is the whole question.

Where everything lives: encryption and decryption happen in the client; the edge, the API and the bucket only ever handle ciphertext and hashes of capability keys.

[RFC 0001](https://newsroom.sgit.ai/articles/rfc-0001-public-key-cryptography-for-sgit.html) closes the gap that remains: today, whoever can read a vault can also produce data every client accepts. The obvious fix does not work, and what does is two key pairs, so that a reader cannot write and a host cannot forge, with fourteen questions for reviewers.

>

Two key pairs work.

## The agents that do the work

A newsroom that runs in the browser still needs people, and agents, to make what it serves. Four articles on the agents that read, test and draw for it.

[One article, five readers](https://newsroom.sgit.ai/articles/one-article-five-readers.html) keeps the prose first, then sends five agents through each article once it is written: a librarian that catalogues every fact with the sentence it came from, a cartographer that maps the concepts, a historian, an explainer and a storyteller. Cataloguing everything turned them into fact-checkers nobody had asked for.

>

Keep writing the article first.

One article, five readers: the catalogue, the map, the place in the arc, two minutes, and a deck.

[How to run synthetic users](https://newsroom.sgit.ai/articles/how-to-run-synthetic-users.html) is a how-to from three studies: invented readers with a situation and a question, driving a real browser one screenshot at a time, saying what they see and think. The rule that makes it work:

>

Give the agent the screenshot, not the page's code.

[The infographic bake-off](https://newsroom.sgit.ai/articles/the-infographic-bake-off.html) gave every image model on OpenRouter the same eleven briefs, judged 101 images blind, and recorded every cost, $10.44 in all, to answer which model for which kind of picture.

And [the AI governance stack as a graph](https://newsroom.sgit.ai/articles/the-ai-governance-stack-as-a-graph.html) takes Hari Kota's ten-layer stack, keeps it exactly as posted, and makes the graph underneath it the model, with 119 edges between the layers, each citing the provision it rests on:

>

A gap is a missing edge, and a missing edge is a query.

## The eight articles

### No server

The decision, and the model that arrives in the tab.

- [**No server, by design: first I retired the database, now I am retiring the back end**](../../../../no-server-by-design.md). First the database went, now the back end: the SGit Newsroom runs all its logic in the browser, on commodity servers that cannot read your data.
- [**A model in the tab: Chrome now ships an LLM to capable desktops, and it is the hardest piece of the client-side puzzle**](../../../../a-model-in-the-tab.md). Chrome now ships a language model any page can prompt, offline, on capable desktops. The last piece of the client-side puzzle, with rough edges.

### The keys

Where the vault keys live, and keys a reader cannot write with.

- [**Where the vault keys live: key management at sgit-ai v0.20.0, and what comes next**](../../../../where-the-vault-keys-live.md). Vault key management at sgit-ai v0.20.0: the one secret, where keys are kept, how they travel sealed on append lanes, and what comes next.
- [**RFC 0001: two ways to add public-key cryptography to sgit, and the questions we want you to answer**](../../../../rfc-0001-public-key-cryptography-for-sgit.md). A Request for Comments: two key pairs so a reader cannot write, sealed files only named people can open, and fourteen questions for reviewers.

### The agents that do the work

Five readers per article, synthetic users, image models judged blind, and a governance stack kept as a graph.

- [**One article, five readers: a librarian, a cartographer, a historian, an explainer and a storyteller read the same piece**](../../../../one-article-five-readers.md). Write the article first, then send five agent readers through it: a catalogue, an ontology and maps, the arc, two minutes, and a deck.
- [**How to run synthetic users on your own site: five people who do not exist, a browser, and an afternoon**](../../../../how-to-run-synthetic-users.md). Five invented users, a model reading screenshots, and a real browser: how to run synthetic users, from three studies.
- [**The infographic bake-off: which image model for which job, judged blind on 10 October 2026**](../../../../the-infographic-bake-off.md). Every image model on OpenRouter, eleven briefs, 101 images judged blind, $10.44: which model for which infographic, and what it costs.
- [**The AI governance stack, as a graph: an answer to Hari Kota, built**](../../../../the-ai-governance-stack-as-a-graph.md). Hari Kota's ten-layer AI governance stack, kept as posted and turned into a fractal semantic graph: the gaps become missing edges, and queries.

*This is issue 5 of the SGit Newsroom newsletter, also published on LinkedIn in [Deterministic GenAI](https://www.linkedin.com/newsletters/deterministic-genai-7174563523795005440/). Every article it links to is on [sgit.ai](https://newsroom.sgit.ai/articles/index.html), with its sources and its data. To get the next issue by email, [subscribe at sgit.ai/subscribe](https://newsroom.sgit.ai/subscribe/).*

**Posting this issue on LinkedIn?** The cover is [005-no-server-by-design.jpg](../../../../banners/005-no-server-by-design.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page. LinkedIn drops images from a paste, so add these where they appear, in this order, with the caption under each:

1. [005-2026-10-11-noserver.jpg](../../../../banners/collages/005-2026-10-11-noserver.jpg) No server, by design, in six pictures, one from each of six of the articles
2. [ns-architecture.webp](../../../../images/ns-architecture.webp) The SGit Newsroom's architecture: every piece of application logic runs in the reader's browser.
3. [km-architecture.webp](../../../../images/km-architecture.webp) Where everything lives: encryption and decryption happen in the client; the edge, the API and the bucket only ever handle ciphertext and hashes of capability keys.
4. [fr-five.webp](../../../../images/fr-five.webp) One article, five readers: the catalogue, the map, the place in the arc, two minutes, and a deck.

[← All issues](../../../index.md)


---

*[Site index for agents](../../../../../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/newsletter/2026/10/11/005-no-server-by-design.html)*
