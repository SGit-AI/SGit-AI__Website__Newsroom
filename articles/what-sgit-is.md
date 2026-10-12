# Git for things you cannot put on GitHub, sgit.ai

> An introduction to sgit and sgit.ai, what an encrypted vault is, why version control had to be rebuilt to get one, and what nineteen published vaults look like when the server storing them cannot read a byte.

*Source: <https://newsroom.sgit.ai/articles/what-sgit-is.html> · sgit.ai v0.7.79 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Git for things you cannot put on GitHub

# Git for things you cannot put on GitHub

2026-08-25 · [article v1.4.2, 7 versions](versions/what-sgit-is.md) · [sgit.ai v0.2.42](https://sgit.ai/admin/versions.md) · introzero-knowledgevaultsagents

***Abstract:** An introduction to sgit and sgit.ai, what an encrypted vault is, why version control had to be rebuilt to get one, and what nineteen published vaults look like when the server storing them cannot read a byte.*

There is a category of file that has nowhere good to live.

A risk register with real system names in it. A regulatory analysis you are still arguing about internally. The working memory of an AI agent that has been reading your codebase for a month. Client material under NDA. Anything a lawyer would want to see before it went near a third party.

All of it wants exactly what git gives you, history, branches, diffs, the ability to hand somebody a link and know what they will see. And all of it is the reason people say *"we can't put that in GitHub."* So it ends up in a shared drive, an email thread, or a Notion page nobody can diff, and the version history that mattered is gone.

**sgit is git for those files.** Encrypted before they leave your machine, versioned exactly like git, stored on a server that cannot read a single byte.

sgit.ai, `pip install sgit-ai`. Pure Python, two runtime dependencies, Apache-2.0.

## The part that is easy to say and hard to build

Zero knowledge is a claim people make loosely, so here is the precise version: **the server holds ciphertext and nothing else.** Not your filenames, not your directory structure, not your commit messages. Encryption and decryption happen on your machine. There is no key escrow, no admin override, no support engineer who can recover it for you, and that last part is a feature with a real cost, which is worth being honest about up front.

What makes it work is a single string:

```

<24-char passphrase>:<vault-id>

```

That is the **vault key**, and it is three things at once, the address of the vault, the authorisation to write to it, and the key that decrypts it. Lose it and the data is gone. Leak it and someone can rewrite your history.

From it you can derive, one way, a **read key**: same vault, read-only, safe to publish. That asymmetry is the whole sharing model. Every vault linked from sgit.ai is published as a read key, and no vault key has ever been published, a rule enforced by a tripwire in the release pipeline that scans every file before either remote is touched.

## Ten seconds of proof

The read key is the entire credential. No account, no login, no access request:

A real clone of the published EU AI Act vault. 273 objects, 207 files.

Now the same vault, as the machine storing it sees it:

786 bytes of AES-256-GCM ciphertext. The object's name is a SHA-256 of the encrypted bytes.

That second screenshot is the argument. The object is **content-addressed over its ciphertext**, which means the host can deduplicate it, cache it for a year, and serve it from a CDN, while remaining unable to tell you what it is. You get the operational benefits of a normal object store without granting it the usual price of admission.

Underneath, it is a real version control system rather than a sync folder: multi-parent commits, a tree per directory, deterministic refs derived by HMAC, a genuine merge-base computation across all parents, and three-way merge. Branches, diffs and history all work, on content the server cannot interpret.

## Nineteen vaults you can open right now

The best way to understand a vault is to open one. **Every vault on sgit.ai is live**: the screenshots are of real vaults, opened with the read keys published beside them.

The published vaults. Each one carries its read key on the page.

They range from a photo library to Regulation (EU) 2024/1689 parsed from official Formex XML into 1,523 nodes and 1,944 edges. Before writing this I cloned all nineteen from their published keys: **1,389 files, no failures.**

## The part that surprises people

A vault can contain an *application*, not just documents, and that application runs against the vault without ever being handed a credential.

`"permissions": {}`, the app requests nothing, and is granted nothing.

Look at `"permissions": {}` in that file. The app asks for no filesystem access at all. It still renders the whole risk graph, because the host reads the vault and passes results in. The app never sees a key. **Capability without credential**, and it means you can run code you did not write against data you care about, with the blast radius set by a config file you can read in one screen.

## Why there is a network of sites

sgit.ai is one of **nineteen** sites on `*.sgit.ai`, each taking one question further than a section could. Most of the thinking behind sgit now lives out there rather than here.

The network directory: start from the question you arrived with.

A few of them, to give the range:

- [**graphs.sgit.ai**](https://sgit.ai/network/graphs.md), *"A node is just a node. Meaning lives in the edges."*
- [**risks.sgit.ai**](https://sgit.ai/network/index.md#risk-governance), *"You cannot deny a risk. You can only say how long you accept it."*
- [**llms.sgit.ai**](https://sgit.ai/network/index.md#agents-ai), your app calls a language model without ever holding an API key.
- [**issues-fs.sgit.ai**](https://sgit.ai/network/index.md#graphs-method). The issues are files, and the files are a graph.
- [**open-source.sgit.ai**](https://sgit.ai/network/index.md#business-publishing), *"Open source is a strategy. It is not a charity."*
- [**sg-sentinel.sgit.ai**](https://sgit.ai/network/sg-sentinel.md), an edge guard design that says `NOT BUILT` at the top of every page.

The [network directory](https://sgit.ai/network/index.md) starts from the question you arrived with rather than the list of domains.

That last one is the house style in miniature. Each site publishes its argument **before** the thing exists, and states plainly what has shipped and what has not. graphs.sgit.ai devotes a page to [where its own approach loses](https://graphs.sgit.ai/about/participant.html). We would rather be checkable than impressive.

## Try it

```

pip install sgit-ai
sgit clone sgit_public_read_c004daae386e8d17fa648884acc527018bd4ea1116ad673fb2f1b068011695c9:73heuprz

```

That is the EU AI Act vault, 207 files on your disk in under a minute, from a key printed on a public web page, with no account anywhere.

If you would rather not install anything, [every vault opens in the browser](https://sgit.ai/demos/vaults/index.md) from the same key.

**Status, plainly.** sgit is beta and says so on every page. The CLI is `pip install sgit-ai`, Apache-2.0, pure Python. The site you are reading is itself served from a vault, released 59 times, and each release is [logged in full](https://sgit.ai/admin/versions.md), including the ones that broke something.

This article is also published as a [LinkedIn newsletter post](https://www.linkedin.com/pulse/git-things-you-cannot-put-github-dinis-cruz-qwrte/), same argument, same screenshots, for readers who live there.

*Written by Dinis Cruz and the agentic team working with him. Licensed CC BY 4.0, reuse it, quote it, argue with it.*

## Threads

Vaults & method[This article as a graph →](graphs.md#what-sgit-is)

### Continued by

- [Move the cloud, not the code: twins, sovereignty that works in practice, and the migration that pays for itself on the day you switch](move-the-cloud-not-the-code.md) Workloads stay on hyperscalers because moving means changing code; a twin lets the code not know, and the value in the twin is what signs the migration.
- [Pay to keep your persona: readers should pay because it helps them, not because they feel they should](pay-to-keep-your-persona.md) Readers should pay because it helps them: a persona with a name and a graph, several for focus, and one that follows you between devices.
- [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](riskmandate-ten-questions.md) Ten hard questions from a conference, answered in a two-hour interview: what RiskMandate does, what it deliberately is not, and how mature each part is.
- [Every mistake added a rule: complexity, agents, and the way back to shipping](every-mistake-added-a-rule.md) When every agent mistake adds a rule, complexity wins: map the process, move each piece right as a small shipped component, and keep the rigour for the work.
- [The Mandate Stack: a multi-agent system in production, layer by layer](the-mandate-stack.md) A multi-agent system that runs a business every few hours: eight layers, one written mandate per agent, everything a graph, one human who sends.
- [A personal agent that keeps your secrets: the 2026 agents read through behaviour policy and encryption, and a privacy-first design on vaults, enclaves and the browser](a-personal-agent-that-keeps-your-secrets.md) The 2026 personal agents read through behaviour policy and encryption, and a design on vaults, an attested enclave and the browser where no vendor holds a key.
- [Twenty sites in fifteen days, and what that did to the writing](nineteen-sites.md) One site became twenty repositories in fifteen days because each argument needed its own version history, and the index now starts from a question.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 3 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=3)

**Posting this article on LinkedIn?** The cover is [what-sgit-is.jpg](banners/what-sgit-is.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/what-sgit-is.html)*
