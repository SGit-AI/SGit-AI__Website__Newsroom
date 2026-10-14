# Two agents, one vault: the Industry Wire is written into an encrypted vault by one agent and drawn by newsroom.sgit.ai, which holds only the read key, sgit.ai

> Open newsroom.sgit.ai/wire/#lens=dinis and you get a week of industry news read as me: forty stories across five beats, each with its primary source, who else covered it, one exact quote and why it matters, twenty-five of them reaching me through a named concern and fourteen withheld with the reason, and a personal brief at the top. None of it is on the newsroom. It is in an encrypted sgit vault that a separate agent wrote on the afternoon of 11 October, in a session the newsroom never saw, with a write key the newsroom does not have. The newsroom's own agent, in its session, took the vault's read key, published it on purpose, and built three pages and about four hundred lines of code that open the vault in the reader's browser, decrypt it and draw it as text, with twenty-eight checks against the real vault in CI. A commit to the vault is on the page within two minutes, with no release of the site. This article walks the workflow from both sides, with the two git logs as the record: what the wire desk wrote and under what rules, what the newsroom holds and what it refused, why the vault is the right interface between two agents that never share a session, and the honest list of what is unreviewed. It is also the first running piece of a plan I had years ago and did not use, and I am now its first reader.

*Source: <https://newsroom.sgit.ai/articles/two-agents-one-vault.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Two agents, one vault: the Industry Wire is written into an encrypted vault by one agent and drawn by newsroom.sgit.ai, which holds only the read key

# Two agents, one vault: the Industry Wire is written into an encrypted vault by one agent and drawn by newsroom.sgit.ai, which holds only the read key

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-12 · [article v1.0.0](versions/two-agents-one-vault.md) · [sgit.ai v0.7.65](https://sgit.ai/admin/versions.md) · vaultsagentsnewsroomindustry-wireread-keyclient-sideprovenancepersonasworkflowmyfeedsarticle

***Abstract:** Open newsroom.sgit.ai/wire/#lens=dinis and you get a week of industry news read as me: forty stories across five beats, each with its primary source, who else covered it, one exact quote and why it matters, twenty-five of them reaching me through a named concern and fourteen withheld with the reason, and a personal brief at the top. None of it is on the newsroom. It is in an encrypted sgit vault that a separate agent wrote on the afternoon of 11 October, in a session the newsroom never saw, with a write key the newsroom does not have. The newsroom's own agent, in its session, took the vault's read key, published it on purpose, and built three pages and about four hundred lines of code that open the vault in the reader's browser, decrypt it and draw it as text, with twenty-eight checks against the real vault in CI. A commit to the vault is on the page within two minutes, with no release of the site. This article walks the workflow from both sides, with the two git logs as the record: what the wire desk wrote and under what rules, what the newsroom holds and what it refused, why the vault is the right interface between two agents that never share a session, and the honest list of what is unreviewed. It is also the first running piece of a plan I had years ago and did not use, and I am now its first reader.*

Two agents, one vault. The wire desk writes the vault with a key the site never holds; the vault server holds ciphertext; newsroom.sgit.ai holds the read key and draws what the reader's browser decrypts. The timeline is from the two git logs.

Open [newsroom.sgit.ai/wire/#lens=dinis](https://newsroom.sgit.ai/wire/#lens=dinis) and you get a week of industry news read as me. Forty stories across five beats, each with where it came from and who else covered it. Twenty-five of them reach me through a concern the vault knows I have; fourteen are withheld, each with the reason. At the top, a personal brief: three things I can write about directly, and a note for the PKI site.

The thing I find remarkable is not the page. It is that the newsroom did not write any of it, does not store any of it, and could not change a word of it if it wanted to. The news is in an encrypted vault that a different agent keeps. The newsroom holds the vault's read key and draws what the key opens. Two agents, two sessions, two git logs, one vault between them, and a page that updates when the vault does.

## In short

- **The news is not on the site.** It is in sgit vault `u9i9jp0l` on a vault server, written by a wire desk agent on 11 October at 16:16 UTC: 40 stories, 55 sources, 7 personas, a join of 280 rows, five design documents and a runbook, in one commit of 24 files.
- **The site holds the read key and nothing else.** newsroom.sgit.ai keeps the key in a config file, published on purpose, and three pages open the vault in the reader's browser, decrypt it with Web Crypto and draw it as text. The write key is with the desk; the site has never seen it.
- **A commit is on the page within two minutes.** The page re-checks the vault's head pointer every two minutes and caches for good the objects that cannot change. No release of the site moves the news.
- **The lens is the vault's own join.** Six public personas and one named reader. Under a lens the page shows what reached that reader, through which concern, and what was withheld and why, as the vault recorded it. The join is code with four weights, and the same rule runs in the vault's own app, so a reader can check it.
- **The site read the whole vault before it published the key**, found no credential in it, held back the lens that named one person, and turned it on only after that person agreed in writing, with the date recorded.
- **Everything in the vault is public for good.** A published read key cannot be withdrawn from anyone who fetched the objects, so the contract says what may never go in: frozen bytes under restrictive licences, a reader's feedback, a brief for one person without their agreement.
- **Unreviewed, and said so.** Every story carries "ai-generated, unreviewed" because the vault says so; 22 of 40 primary sources were not fetched by the research agent; an independent check of 10 stories corrected 3. The page shows the status as the vault wrote it.
- **This is the interface between agents.** Not an API, not a shared session, not a database: a vault one writes and another reads, with the history as the audit trail. It is the pattern sgit.ai uses for its own documents, applied to a daily feed.

## What the reader sees

The wire's edition page on 12 October. The grey line is the vault's own head: its id, the time the pointer was checked, the commit and its message. Then the editor's note and the three threads of the week, read from the vault seconds earlier.

The page opens with a line that tells you where it came from: the vault id, the time the head pointer was checked, the commit's short id and the first hundred characters of its message, and how many objects were fetched or came from cache. Then the edition: an editor's note of three sentences, three threads the desk saw running across the week, the lead story with why it leads, and the stories by beat.

Each story is the same shape. A headline, a date, the primary source and what kind of source it is, a confidence level, a summary in the desk's words, one exact quote with where it came from, why it matters, and a fold for who else covered it. The chips at the bottom are the entities the desk extracted and the personas the story is tagged for.

The lead story as the page draws it: date, publisher, source kind, confidence, why it leads, the summary, the quote with its source, why it matters, who else covered it, the entities, and the status the vault gave it.

Then the lens. "Read as" offers the six public personas, Morgan the founder, Kai the AI builder, Sam the security lead, Jordan the board member, Rowan the journalist, and the risk owner, and one named reader. Pick one and every beat heading changes to how many stories reach that reader and how many are withheld, each withheld story folds under the heading with its reason, and the lens goes into the address, so a link can carry it.

Under the Dinis lens, two stories in the first beat are withheld, and the page says why: no concern matched, and the ten concerns that were tried. The next beat says five reach and three are withheld.

Under my own lens there is one more thing: the personal brief the desk wrote, as the vault wrote it. A note of four sentences, and seven stories by join score with the concerns that matched each, linked to the stories on the page. Under it, the sentence that makes it allowed: "A named reader, by their own agreement while the wire is a beta. Like everything in the vault, this brief is public."

The personal brief under the Dinis lens: the note, seven stories by score with the concerns that matched, and the sentence that says why a brief for one person is on a public page.

## The vault, and the agent that keeps it

The vault was made in a session I was not in, by an agent working from a voice brief, and it says so in its README: a first pass, 11 October 2026, built by research agents, not yet reviewed by a person. Its history is two commits, an `init` at 16:16:03 UTC and the first pass nine seconds later, 24 files. Anyone can read it:

```

sgit clone sgit_public_read_4c7aefb739e52e9a03c35be01bf7e311af00872e33c477b4d7c4319cdb91bdba:u9i9jp0l

```

What is in it, in the desk's own order:

- **The edition.** `briefs/2026-10-11/`: the brief as markdown for a person and as JSON for an agent, and the editorial file with the editor's note, the lead and the three threads.
- **The stories.** 40 of them, 8 per beat except 10 for cybersecurity and 6 for governance, as one JSON file and as a folder per story with its JSON and its markdown. Each has a primary source, one to four other outlets, one exact quote, the entities named, why it matters and a confidence level. 127 publishers were seen and 176 coverage links checked to get there.
- **The sources.** 55 of them, each with a tier. Tier A is an open licence or public domain: the text may be kept and shown. Tier B is a primary source that is not openly licensed: a quote of 25 words or fewer and a link. Tier C is commercial press and paywalls: headline, link and date, never the text. A source is verified only when a person has opened its licence page.
- **The personas.** Seven: the six the newsroom already uses, and me, with ten concerns. Each concern has terms; the terms are what the join matches.
- **The join.** `data/deliveries.json`, 280 rows, one per story and persona: reached or withheld, the score, the connections that reached, and for a withheld story the list of concerns tried. The rule is a short Python file, and its first line says what matters: "This is code, not a model." Entity match counts 3, a tag by the research desk 2, a keyword 2, the right beat 1, and each concern counts once at its strongest match.
- **The fact check.** An independent check of 10 stories, which found 3 to correct, and the corrections made.
- **The design.** Five documents: the architecture, the workflows, the sources policy, the UI options and what the wire borrows from where. And the runbook, which is the prompt the daily agent will start from in a fresh session, so it is all the context that agent has.
- **The app.** The vault opens as an app of its own, with four tabs and the same lens, so the data can be read without the newsroom at all.
The vault opened as its own app, read-only, with the public key: the same edition, the same lens, the same numbers, drawn by the code inside the vault rather than by the newsroom.

The runbook is where the workflow shows its discipline. The desk is four roles, and each may write only in its own folders: a Poller that never judges importance, a Clusterer that never writes prose, an Extractor that never invents an entity absent from the frozen bytes, a Writer that never writes a quote that is not in a frozen source. The Editor, a person or the newsroom's Editor role, places stories on the front; the desk only proposes. Before a commit, a gate fails the run on a quote not found in frozen bytes, a quote from a tier-C source, a missing date, a missing licence line, or a story marked confirmed with fewer than two independent sources. And there are stop conditions that end the run and report instead of publishing: the gate failing twice, more than 30 per cent of sources degraded, a story about a named private individual.

None of that is new to readers of this site. It is [the story as a graph](future-of-news-story-vault-not-paywall.md) with provenance first, [the Editor as the one role that places](https://newsroom.sgit.ai/newsroom/index.html), and the rule from [Every mistake added a rule](every-mistake-added-a-rule.md) that a component which makes the mistake impossible beats a prompt that asks the model to remember. What is new is that the desk is a different agent from the one that runs the site, and the only thing between them is the vault.

## The site that only reads

The newsroom's own agent, in its own session, found the vault on the afternoon of 11 October and released the wire at 23:51 UTC as v0.9.0. The commit message is the design, and the [how page](https://newsroom.sgit.ai/wire/how.html) says the same thing to a reader.

How the wire works, on the newsroom: how the site reads the vault, the contract between the vault and the site, and the clone command with the read key, which is the whole credential.

How the site reads the vault is five steps, all in the reader's browser. Derive the address of the vault's head pointer from its id. Fetch the pointer, then the commit, then the tree, then three files: the bundle, the deliveries and the documents. Decrypt each with Web Crypto using the read key. Draw. The code is [sgit.ai's vault reader](https://sgit.ai/docs/vault/vault-from-javascript.md), vendored and cut down to 182 lines, and a drawing file of 214 lines that builds every element with `createElement` and `textContent`, makes a link only from a value that starts with `http`, and renders the vault's markdown documents through a renderer that escapes. Nothing from the vault is run. The page re-checks the pointer at most every two minutes, and caches for good the objects that cannot change, because their ids are their hashes.

What the site holds is one config file: the server, the vault id, the read key, the files it reads, and now the named readers. The read key is public on purpose, and the file says what that means in its first line: the key can read every file and every commit of this vault and cannot write, so everything in the vault is public, for ever, because a published read key cannot be withdrawn from anyone who has fetched the objects. The write key is held by the agents that run the wire and is not on the site. That sentence is the whole security model, and [Where the vault keys live](where-the-vault-keys-live.md) is why it holds.

The contract between the vault and the site is on the how page, in words a person can read and a test can check: the bundle has beats, stories, sources, personas and a brief; each story carries sixteen named fields; the deliveries carry five. A story's status is shown as written, so "ai-generated, unreviewed" stays on the page until the vault says otherwise. The head commit's message is shown on every wire page. And the one rule about privacy: nothing private goes in the vault, not frozen tier-B bytes, not a reader's feedback, not a brief meant for one person unless that person has agreed to it being public.

Then the tests. A file of checks runs in Chromium against the real vault, in CI, as the fifth test file the newsroom runs: the edition opens from the vault; the status names the vault and the commit; at least thirty stories are drawn across five headings; the lead carries why it leads; every story shows its status; every link drawn from the vault is http(s) or an anchor; nothing from the vault became a script, a frame, an image or a handler; the snapshot stays hidden while the vault is live; as Sam, reached plus withheld is the whole edition and each withheld story carries its reason; the lens is in the address. Twenty-three checks at v0.9.0, twenty-eight by v0.9.3. The snapshot is the fallback: what the vault held at the last release, headlines and primary links only, for a reader without a script and for an agent without a browser, and the index it reads first.

### What the site refused

Two things in the commit message of v0.9.0 are the part of the workflow I most want to point at, because they are where a second agent earns its place.

The newsroom's agent cloned the vault and read it in full before it published the read key: no key, token or credential in it. Publishing a read key is publishing everything the key opens, for good, and you do not do that on trust.

And it found two things it would not fix itself but flagged for the vault's keeper: a persona and a note aimed at one named reader were about to become public, and the runbook's plan to keep frozen tier-B bytes and reader feedback privately needs a vault of its own, because this one cannot hold anything private. The first was resolved the next morning, at 00:54 UTC, in v0.9.3: I agreed in writing to be the wire's named reader while it is a beta, the agreement is recorded with the date in the config file, and that record is what tells the page to offer the lens. No other named person gets one without a recorded agreement, and the how page's contract now says so. The second is still open, and it is the vault's problem, not the site's, which is the point.

## Why the vault is the interface

There are three ordinary ways to get one agent's work in front of another's readers. The first agent could push pages into the second's repository, and then the second site's history is full of commits it did not review. The second could call an API the first runs, and then there is a server, a credential on the site, and a dependency on a process that has to be up. Or the two could share a session, and then there are not two agents.

A vault is the fourth way, and it has properties the others do not.

- **The site owns the presentation and the vault owns the news.** The newsroom decides how a story looks, what a lens means, what the page says about status. The desk decides what the stories are. Neither can do the other's job, because neither has the other's key.
- **Updating is a commit, not a release.** The desk commits; the page sees the new head within two minutes. The site's own release history is untouched by the news, and its tests still run against the live vault.
- **The read key is the whole credential, and it is public.** No account, no token, nothing to rotate on the site. The write key never leaves the desk, so a compromise of the site's repository, which is public anyway, cannot change a story.
- **The server sees nothing.** Ciphertext, sizes, times, and ids that look random. It cannot read a story, and it cannot tell who reads. The newsroom [has no server](no-server-by-design.md), and this adds a daily feed without one.
- **The history is the audit trail.** Every edition is a commit, and the head commit's message is on every page. A correction is a new file; nothing is deleted. The vault's own workflows document says every one of its six workflows ends in a commit, "so the history doubles as the audit trail."
- **A third agent can join without asking either.** The clone command is on the page. An agent that wants the wire reads the vault, not the site, and the snapshot tells it where to start.

This is also how sgit.ai reads its own documents: a case study on this site, [How this page works](https://sgit.ai/case-studies/live-vault-docs.md), is a page that reads itself from a vault with a published key. The newsroom took that arrangement and applied it to a feed written by someone else, which is the harder case, because now the contract between writer and reader has to be written down. It was.

## The loop, and whose plan this was

The timeline from the two git logs is the workflow in one line. 11 October, 16:16 UTC: the vault's first commit. 23:51 UTC: the newsroom's three pages. 12 October, 00:54 UTC: the named reader, by agreement. Three sessions, and I was in none of the first two.

The vault's README calls itself the first step in carrying out the MyFeeds plan, and that lands. In [I miss it, so it is working](i-miss-it.md) I wrote that MyFeeds was a good idea I did not use, and that not using it was the signal I should have listened to. The wire's workflows document has a step called the morning read: open the personal brief with the lens set to me, and for each item take one of four actions, more like this, not for me, write about this, or wrong, each of which writes a line to a feedback file, with a weekly pass in which an agent proposes edits to the personas from that feedback as a diff for approval. "This is how the persona graph learns without a black box: every change to what you see is a reviewed edit to a file." That is MyFeeds, running, with me as the first user. Whether I miss it when it stops is the test, and it is the right one.

The next turns of the loop are already written down. A pitched wire story becomes a newsroom article that inherits the story's frozen sources and provenance graph, so its claims rest on evidence before a word is written. The Editor places up to three wire stories on the front with a reason per slot. A weekly newsletter is cut from the week's briefs, with every quote checked against frozen bytes at build time. And feedback, which is private, needs the vault of its own that the newsroom's agent flagged. The brief for that is the brief in [I miss it](i-miss-it.md): a reader's own vault, which is also what [the passkey](the-passkey-opens-the-vault.md) is for.

## What this does not claim

- **It is a first pass, unreviewed.** The edition is a week's catch-up, not yet a daily, and every story carries "ai-generated, unreviewed" because the vault says so. 22 of the 40 primary sources were not fetched by the research agent, and the page says so on each. An independent check of 10 stories corrected 3; the other 30 have not had one.
- **The join is matching, not understanding.** Entities, tags, keywords and beats, with four weights. It explains itself, which is the point, and it will withhold a story I would have wanted and reach me with one I would not.
- **The personas are the desk's draft of me.** Ten concerns and their terms, written by an agent from what I publish. The morning read is designed to correct them; it has not run yet.
- **The vault is on a development server**, and its read key is public, which means everything in it is. The contract is what keeps that safe, and one of its two flags is still open.
- **Nothing here is a product.** A beta with one named reader, by agreement, on a site with few readers.

If you run a newsroom or a desk of agents and want a feed that one agent writes and another site reads, or you want to be a named reader of the wire when it has more than one, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A message of mine on 12 October 2026 pointing at the newsroom's latest commits and the wire under my own lens, written by this site's agent in the voice of this site. The argument and the editorial responsibility are mine. The facts are from the two records: the newsroom repository's commits v0.9.0 and v0.9.3 of 11 and 12 October 2026, including their full messages, the config file, the build script and the test file; and the wire's vault, cloned read-only with its published key on 12 October, including its README, its five design documents, its runbook, its join code and its two commits. The counts, 40 stories, 55 sources, 127 publishers, 176 coverage links, 7 personas, 280 deliveries, 22 primaries not fetched, 10 checked and 3 corrected, are the vault's own. The screenshots are of [newsroom.sgit.ai/wire/](https://newsroom.sgit.ai/wire/) at v0.9.3 and of the vault opened as an app, on 12 October 2026. Related: [The future of news is the story vault, not the paywall](future-of-news-story-vault-not-paywall.md), [No server, by design](no-server-by-design.md), [Where the vault keys live](where-the-vault-keys-live.md), [Every mistake added a rule](every-mistake-added-a-rule.md), [I miss it, so it is working](i-miss-it.md), [The passkey opens the vault](the-passkey-opens-the-vault.md), [How this page works](https://sgit.ai/case-studies/live-vault-docs.md) and [Creating, opening and writing a vault from JavaScript](https://sgit.ai/docs/vault/vault-from-javascript.md).

## Threads

Vaults & methodNews & evidenceAgents & policy[This article as a graph →](graphs.md#two-agents-one-vault)

### Builds on

- [The future of news is the story vault, not the paywall](future-of-news-story-vault-not-paywall.md) A story is a graph of claims and evidence and the article is one projection of it; keep the graph in a vault and sell what the article was made from.
- [Every mistake added a rule: complexity, agents, and the way back to shipping](every-mistake-added-a-rule.md) When every agent mistake adds a rule, complexity wins: map the process, move each piece right as a small shipped component, and keep the rigour for the work.
- [Where the vault keys live: key management at sgit-ai v0.20.0, and what comes next](where-the-vault-keys-live.md) Vault key management at sgit-ai v0.20.0: the one secret, where keys are kept, how they travel sealed on append lanes, and what comes next.
- [No server, by design: first I retired the database, now I am retiring the back end](no-server-by-design.md) First the database went, now the back end: the SGit Newsroom runs all its logic in the browser, on commodity servers that cannot read your data.
- [I miss it, so it is working: the people who decide the roadmap have to use the product, and the vault the newsroom now needs](i-miss-it.md) I read the newsroom on four devices and they do not agree. Missing a feature is the best sign; the makers must use it. And the brief for the reader's vault.
- [The passkey opens the vault: a door per path, a master vault for every user, and no server of ours](the-passkey-opens-the-vault.md) Tested: a passkey's PRF bytes compute a door that holds the master's key, and a different path to the same passkey gives different bytes, so a door per path.

### Continued by

- [sgit in a CI pipeline: encrypted, versioned data in and out of GitHub Actions, between its jobs, through write-only lanes, and a key for every job](sgit-in-a-ci-pipeline.md) Encrypted, versioned vaults as the way data gets into, out of and between CI jobs, with a key per job and a sidecar when there is no server.
- [Attacks rewritten as mandates: 28 supply-chain incidents, the column each one was missing, and why the next maintainer is an agent](attacks-rewritten-as-mandates.md) 28 supply-chain attacks read as reach beyond mandate: what a hardened registry stops, what only a written mandate can, and why agents change it.
- [Sixteen notes I did not want to lose: a request to send from any browser to my vault, why identity is still this hard, and how two more wires became a product line](sixteen-notes-i-did-not-want-to-lose.md) Sixteen notes stuck in a browser with no passkey led to a request: let any browser send to my vault, by link, text or QR code.
- [The site is an inbox: deciding before reading, marks that build the reader's own graph, and why I could not write this brief until the vault existed](the-site-is-an-inbox.md) The site as an inbox that starts empty: decide fast before reading, mark slowly while reading, build a graph you own, and sign what you send to the newsroom.
- [The vault is live: from a design on 11 October to a reader's vault on newsroom.sgit.ai by two in the morning, and how all of it fits together](the-vault-is-live.md) The reader's vault runs on newsroom.sgit.ai: a passkey opens three real vaults, each device writes one file, and the architecture is drawn as it stands.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 80 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=80)

**Posting this article on LinkedIn?** The cover is [two-agents-one-vault.jpg](banners/two-agents-one-vault.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/two-agents-one-vault.html)*
