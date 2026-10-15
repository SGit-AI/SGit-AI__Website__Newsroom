# From sending a file to sgit: eight months of SG/Send, told by its own briefs and commits, and how a file-sharing service became encrypted version control and vaults, sgit.ai

> SG/Send started because sending a file was harder than it should be, and because I wanted to build a service where the server holds nothing: the best way to protect an asset is not to have one. Eight months later it has become sgit, encrypted version control with Git's model, and the vaults that this site runs on. The whole journey is in public repositories, so this time I asked this site's agent to check my memory against the record: 4,476 commits on the SG/Send app on 246 of its first 249 days, 1,620 on the sgit command line, 739 release tags, 1,389 brief files and 268 debriefs. The record changes the order I remembered. The vault and the data room were named in February, before folders, zips and Git; the first feature a paying user asked for went from proposal to production in 22 minutes; the move to Git's model took about two weeks of briefs and a simulation that found 14 gaps before any code was written. It also shows the pace: fast from February to May, a turn to focus in June, two long pauses on the command line, and a burst in October. And it shows the lesson: by 5 March the briefs already said "Users buy credits, test once, and don't come back." The technology worked. The use case was not there yet.

*Source: <https://newsroom.sgit.ai/articles/from-send-to-sgit.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / From sending a file to sgit: eight months of SG/Send, told by its own briefs and commits, and how a file-sharing service became encrypted version control and vaults

# From sending a file to sgit: eight months of SG/Send, told by its own briefs and commits, and how a file-sharing service became encrypted version control and vaults

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-15 · [article v1.0.0](versions/from-send-to-sgit.md) · [newsroom v0.12.62](https://newsroom.sgit.ai/admin/versions.html) · sg-sendsgitvaultshistoryagentic-developmentbriefsproduct-market-fitexplorersvillagersencryptionarticle

***Abstract:** SG/Send started because sending a file was harder than it should be, and because I wanted to build a service where the server holds nothing: the best way to protect an asset is not to have one. Eight months later it has become sgit, encrypted version control with Git's model, and the vaults that this site runs on. The whole journey is in public repositories, so this time I asked this site's agent to check my memory against the record: 4,476 commits on the SG/Send app on 246 of its first 249 days, 1,620 on the sgit command line, 739 release tags, 1,389 brief files and 268 debriefs. The record changes the order I remembered. The vault and the data room were named in February, before folders, zips and Git; the first feature a paying user asked for went from proposal to production in 22 minutes; the move to Git's model took about two weeks of briefs and a simulation that found 14 gaps before any code was written. It also shows the pace: fast from February to May, a turn to focus in June, two long pauses on the command line, and a burst in October. And it shows the lesson: by 5 March the briefs already said "Users buy credits, test once, and don't come back." The technology worked. The use case was not there yet.*

Eight months of SG/Send and sgit, week by week: commits per week across all branches of the SG/Send app (bars) and the sgit command line (line), from 8 February to 14 October 2026, with the milestones the briefs and commits record and the command line's two long pauses shaded.

## In short

- **A service where the server holds nothing.** Encrypted on the client; the key never sent.
- **Live in five days.** First commit on 8 February, send.sgraph.ai live on 13 February.
- **Users, payments, a 22-minute feature.** Stripe on 1 March, ten paying customers on 2 March, folders as zips that evening.
- **The ideas came first.** The vault and the data room were named in February, before the features that made them.
- **Copy Git.** About two weeks of briefs, a simulation, and the name sgit by 16 March.
- **The vault grew into apps.** Previews, Markdown, HTML, and sandboxed vault apps by May.
- **The pace is in the data.** Commits on 246 of 249 days on the app; bursts and pauses on the command line.
- **The market said: not yet.** "Users buy credits, test once, and don't come back."

## A service where the server holds nothing

SG/Send began with a problem I had every week: sending a file, or a folder, to someone, securely, without either of us installing anything. I was deep in Lambda development at the time, so I built a service. And it was the first time I deliberately used my security background to shape a product from the start. The best way to protect an asset is not to have the asset. If people were going to use it, the last thing I wanted was to hold their data.

The first commit was on 8 February 2026, and the same day a specification went in that set the rule everything since has followed: "files are encrypted on the client before upload, and the decryption key is never sent to the server." The spec was blunt about why: "This single architectural decision eliminates ~90% of the security risk surface." [No server, by design](no-server-by-design.md) is where that idea ended up.

## Live in five days

On 12 February the team's historian recorded "a working MVP user site with end-to-end zero-knowledge encrypted file transfer, deployed to AWS Lambda", and on 13 February send.sgraph.ai went live. The historian's status report put it simply: "The project moved from 'infrastructure sprint' (v0.1.4 brief, 10 Feb) to 'live with real users' (13 Feb) in 3 days."

The way of working was written down the same day: voice memos become briefs, "briefs flow down, debriefs flow up, and a clear folder structure makes everything findable." By 14 February there were explorers and villagers, the people who discover and the people who harden, with a note that "We are NOT creating the Town Planners team yet." That structure, and the [3,025 markdown files](how-much-of-this-did-i-write.md) it produced this year, is how a lot of this got built so quickly.

## Users, payments, and a feature in 22 minutes

Then I took it to market, end to end, which is where I learnt Stripe, pricing and everything else a real product needs. By the time I built the newsroom, I already knew how to do all of it: a good example of how exploring something early pays off later, in a way nobody plans. The pricing brief of 28 February set £5 for 500 file credits and named the real question: "will they buy more?" The Stripe checkout went live on 1 March. On 2 March, the briefs record, "SG/Send had its **first 10 paying customers**", recruited with a simple offer: buy credits for £5 and I would send a £5 Amazon voucher. "Several declined the Amazon voucher."

The first feature request came the same day: a user wanted to send a folder, not a file. At 20:26 the architect's proposal for folder upload as a client-side zip was committed; at 20:48 the implementation; at 22:15 a viewer for the zip on the download page. The debrief the next day: "First feature request (folder upload) shipped in 90 minutes." The viewer also came from a real problem: a week earlier, a recipient could not open a Markdown file inside a zip on a phone. "The recipient literally could not read the file they were sent."

## The data room I had already built

On 3 March, while emailing material to investors, I realised something, and the brief records it: "we already built the data room." Folder upload, the zip viewer and the file previews, together, were a data room. The daily brief that day added the next step: "The vault is the persistent, editable evolution."

This is where my memory and the record part ways, in an instructive direction. I remembered the data room and the vault as things the zip led to. The record shows I had named both earlier: the data room as an investor and product idea between 17 and 21 February, and "a personal data vault", with its own interface, on 22 February. The ideas came first. The features caught up with them, and when they did, I recognised what I had built.

## Copy Git

The order I remembered, and the order the record shows: the memo's sequence on the left, the same steps dated from the briefs and commits on the right. The vault and the data room were named in February, before folders, zips and Git.

A vault you can only replace whole is not much of a vault. Two sessions saving at once lost data; there was no history and no way to merge. The architecture brief of 4 March is the turning point, and it is short on hesitation: "stop inventing solutions to these problems. Git already solved all of them. Copy Git." The model was Git's, commits, trees, blobs, refs and branches, with encryption on top, and a server that is "a dumb key-value blob store" while "All intelligence lives in the client."

I remembered this as a week of briefs. The record says about two weeks: some 48 brief files on vaults, Git and the command line between 3 and 18 March. The most interesting of them is a case study of designing without code, using the model as a simulator of software that did not exist yet: "The process produced 6 revisions of a simulation document, found 14 architectural gaps, resolved 13 of them". The decision that makes the whole thing work came on 3 and 17 March: file names and ids that are encrypted but deterministic, derived from the read key, so that a server that knows nothing can still serve the right object to someone who holds the key, and "Knowing the `read_key` does **not** let you compute the `write_key`".

The name followed. The briefing for the sgit.ai domain called it "Git with integrated trust", and said the s "can stand for **signed**, **secure**, or **sgraph**". The `sgit` command arrived on 16 March as an alias of the command line, which had started on 3 March as sg-send-cli; on 20 March the package was renamed sgit-ai and published to PyPI. On 4 March the command line had already cloned a vault from the terminal. [What sgit is](what-sgit-is.md) describes what it became.

## The vault grows into apps

Once sgit existed, the vault became its interface, and then much more than a better zip. It rendered Markdown, then images inside the Markdown, then CSV tables, audio and video, and by 30 March HTML. Claude learnt to create vaults through skills, from late March. And when HTML pages started to work well, the next question was obvious: why show the vault around the page at all? On 2 May the architecture brief for sandboxed apps put the security model in two lines: "The iframe cannot load anything, cannot access anything, cannot reach the network. It can run JavaScript." And: "The iframe is user-mode. The runtime is kernel-mode." By 8 May a vault whose `app.json` asks for it opens full screen as an app. That is what the vaults on this site, and on sgit.ai, are today.

## The pace

sgit's unit tests as recorded in its commit messages, from 237 on 5 March to 4,232 on 14 October, and its releases to PyPI per month: the tests grew fastest from March to May; the releases came in bursts.

The repositories show the speed, and its shape. The SG/Send app has 4,476 commits on 246 of its first 249 days, and 739 release tags from v0.1.0 to v0.34.0: 196 tags in February, 253 in March, then fewer each month, and five in September. The busiest weeks were in March, at 427 and 439 commits.

The sgit command line has 1,620 commits, and its own rhythm: a fast start in March, its biggest week in early May at 337 commits, then two long pauses, 36 days from the end of June to early August and 28 days from late August to late September, and then a burst in October, when versions 0.17 to 0.21 shipped in eight days. It went to PyPI 20 times as sg-send-cli in March, and 89 times as sgit-ai since. Its unit tests grew from 237 on 5 March to 4,232 on 14 October.

The data also shows who wrote what. Of the 1,671 commits under my name on the app, 1,298 are merges of the agents' branches, and most of the rest are brief files. The agents wrote the code; I wrote the briefs, read the debriefs, and merged. The agents' own share of the app's commits rose from 38% in February to over 85% from September. [The agent team as it runs](the-agent-team-as-it-runs.md) describes that team.

## What the market said

The technology worked. The use case did not land, and the briefs said so early. On 5 March: "We have paying customers but not enough usage. Users buy credits, test once, and don't come back. Credits sit unused." In April the plan was a different experiment, £5 of model credits in each user's vault, with the same test: "If users spend their £5, enjoy the experience, and then buy more credits, we have a business." On 19 June the strategy brief set the priority as "reaching profitability, the first batch of users using the product regularly", and from then on the briefs turn towards risk acceptance and RiskMandate. Nobody ran out of credits and came back for more, and nobody came back asking for the next feature. That silence was a signal in itself.

It was a platform without a workflow that needed it. The difference now is that I have the workflows: the newsroom, RiskMandate and the vaults themselves need exactly the features SG/Send built, which is why they are getting used. Explorers find things early; the use case decides when they matter. That is the next article: what SG/Send could be now, with the same technology and a real need.

## What this does not claim

- **My memory was wrong in places.** The order, the length of the Git work, and nine months, which is eight.
- **Usage is described, not counted.** The briefs say credits sat unused; I did not find usage figures.
- **"30 paying customers"** appears only in an investor one-pager, and the team's librarian could not verify it; ten is the recorded number.
- **The iframe inspiration is my recollection.** The sandbox briefs do not cite the chat apps.
- **Commit counts include automation.** Release tags and some commits are made by CI.

If you are building something that works and nobody is using yet, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 15 October 2026, written by this site's agent in the voice of this site; the argument and the editorial responsibility are mine. Two research agents read the briefs, debriefs, reviews and commits, and every date and quote here was checked in the repositories: [SGraph-AI__App__Send](https://github.com/the-cyber-boardroom/SGraph-AI__App__Send), including [the Git brief of 4 March](https://github.com/the-cyber-boardroom/SGraph-AI__App__Send/blob/dev/team/humans/dinis_cruz/briefs/03/04/v0.11.1__arch-brief__git-like-encrypted-object-store.md), [the first customers](https://github.com/the-cyber-boardroom/SGraph-AI__App__Send/blob/dev/team/humans/dinis_cruz/briefs/03/03/v0.10.30__brief__first-customers-debrief.md), [the simulation case study](https://github.com/the-cyber-boardroom/SGraph-AI__App__Send/blob/dev/team/humans/dinis_cruz/briefs/03/12/vault/v0.13.30__case-study__simulation-driven-architecture.md) and [the activation brief of 5 March](https://github.com/the-cyber-boardroom/SGraph-AI__App__Send/blob/dev/team/humans/dinis_cruz/briefs/03/05/v0.11.08__brief__shell-architecture-user-activation-growth.md); [SGit-AI__CLI](https://github.com/SGit-AI/SGit-AI__CLI) and its predecessor [SG_Send__CLI](https://github.com/the-cyber-boardroom/SG_Send__CLI); and the [sgit-ai releases on PyPI](https://pypi.org/project/sgit-ai/). Counts are from git logs of all branches on 15 October 2026.

## Threads

Vaults & methodStartups & strategy[This article as a graph →](graphs.md#from-send-to-sgit)

### Builds on

- [No server, by design: first I retired the database, now I am retiring the back end](no-server-by-design.md) First the database went, now the back end: the SGit Newsroom runs all its logic in the browser, on commodity servers that cannot read your data.
- [How much of this did I write? The numbers behind twenty articles in four weeks, and what the input actually was](how-much-of-this-did-i-write.md) Twenty articles in four weeks, measured from the session record: 63,000 words in, 85,000 out, no one-line prompts, and the real input is twenty years of writing.
- [Git for things you cannot put on GitHub](what-sgit-is.md) sgit is git for files you cannot put on GitHub: encrypted before they leave your machine, versioned like git, stored where the server cannot read a byte.
- [The agent team as it runs: one person, twelve agents, encrypted vaults, and a mailbox nobody sends from](the-agent-team-as-it-runs.md) Twelve agents on dedicated accounts, encrypted vaults as the only memory, messages as files, a folder per person, and a mailbox nobody sends from.

### Continued by

- [My memory, checked: thinking out loud in a voice memo, publishing only what the record supports, and why peer review has moved to before publishing](my-memory-checked.md) I say it as I remember it; the agent checks it against the record before anyone reads it. Five confirmed, five corrected, two not found.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 132 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=132)

**Posting this article on LinkedIn?** The cover is [from-send-to-sgit.jpg](banners/from-send-to-sgit.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/from-send-to-sgit.html)*
