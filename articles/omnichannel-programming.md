# Omnichannel programming: briefs by voice, reviews by voice, previews on the phone, and one shared state underneath, at every stage from explorer to town planner, sgit.ai

> I no longer program in one place. I brief in a voice memo while walking, review a draft by voice, check the preview on my phone, test on the computer, read the pull request on GitHub, and pick the same work up on an iPad. Retail has a word for this. In 2011 Darrell Rigby wrote in Harvard Business Review that successful companies would engage customers through omnichannel retailing, and the difference that made the word stick is the one that matters here: multichannel means separate channels, each with its own copy of the work; omnichannel means every channel reads and writes one shared state. For programming, that state is git, vaults, briefs and graphs. This site is the worked example: in three days, one agent session took 54 messages from me, 10 of them voice memos, and turned them into 40 releases, 36 articles and 87 figures, with research, hooks, tests and other agents working in the same repository. It works at every stage of a Wardley map, for explorers, villagers and town planners, and at every altitude, from intent down to the code, including code review. It is already how a new generation of developers and founders works. And it breaks in known ways, which the shared state is there to fix.

*Source: <https://newsroom.sgit.ai/articles/omnichannel-programming.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Omnichannel programming: briefs by voice, reviews by voice, previews on the phone, and one shared state underneath, at every stage from explorer to town planner

# Omnichannel programming: briefs by voice, reviews by voice, previews on the phone, and one shared state underneath, at every stage from explorer to town planner

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-15 · [article v1.0.0](versions/omnichannel-programming.md) · [newsroom v0.12.66](https://newsroom.sgit.ai/admin/versions.html) · omnichannelagentic-developmentvoice-memoscode-reviewcustom-uisvaultswardley-mapsexplorersvillagerstown-plannersdevelopersarticle

***Abstract:** I no longer program in one place. I brief in a voice memo while walking, review a draft by voice, check the preview on my phone, test on the computer, read the pull request on GitHub, and pick the same work up on an iPad. Retail has a word for this. In 2011 Darrell Rigby wrote in Harvard Business Review that successful companies would engage customers through omnichannel retailing, and the difference that made the word stick is the one that matters here: multichannel means separate channels, each with its own copy of the work; omnichannel means every channel reads and writes one shared state. For programming, that state is git, vaults, briefs and graphs. This site is the worked example: in three days, one agent session took 54 messages from me, 10 of them voice memos, and turned them into 40 releases, 36 articles and 87 figures, with research, hooks, tests and other agents working in the same repository. It works at every stage of a Wardley map, for explorers, villagers and town planners, and at every altitude, from intent down to the code, including code review. It is already how a new generation of developers and founders works. And it breaks in known ways, which the shared state is there to fix.*

Multichannel and omnichannel programming: on the left, each channel keeps its own copy of the work and a person carries the context between them; on the right, every channel reads and writes one shared state, so work started in one continues in any other.

## In short

- **I no longer program in one place.** Voice, chat, phone, IDE, pull request, preview, vault.
- **Multichannel is not the point.** Omnichannel is: every channel shares one state.
- **The shared state is git, vaults, briefs and graphs.** That is what makes a channel switch cheap.
- **This site is the worked example.** 54 messages in, 40 releases out, in three days, counted from the record.
- **Reviewing is a channel too.** Code review by voice, as a graph, from the story down to the call.
- **It works at every stage.** Explorers, villagers and town planners each use every channel, at every altitude.
- **It is already normal.** For a new generation of developers and founders, this is simply how software is made.
- **It breaks in known ways.** Fragmentation, secrets in the wrong place, lost context; the shared state is the fix.

## Where the word comes from

Omnichannel is a retail word. Darrell Rigby put it into Harvard Business Review in December 2011, in [The Future of Shopping](https://www.bain.com/insights/the-future-of-shopping-hbr/): "Successful companies will engage customers through "omnichannel" retailing: a mashup of digital and physical experiences." The distinction that made the word useful is the one I want to borrow. A multichannel retailer has a shop, a website and a catalogue, each with its own stock, prices and customer record. An omnichannel retailer has one customer, one basket and one stock, and the channels are just ways in.

I did not find the phrase "omnichannel programming" used this way before, so I am using it on purpose. Programming has become multichannel almost by accident: there is a chat, an IDE, a phone app, a pull request, a preview, each good on its own. What makes it omnichannel is that every one of them reads and writes the same state, so that I can start something in one and finish it in another without carrying the context in my head.

## What it looks like

A typical day now: I record a voice memo on a walk, and it becomes a brief. An agent works on it in the cloud, in a repository, and pushes. I look at the result on my phone, in the live site or in a preview, and reply by voice with what to change. On the computer I run the tests or open the page in a browser. On GitHub I read the diff. On an iPad, in a meeting, I check the same article again. A reader's own agent reads the same articles, through the site's [llms.txt](https://newsroom.sgit.ai/llms.txt). And when I want to try something without risk, a vault holds the experiment, with its own history, and a website renders it.

None of these channels is new. Claude Code itself went to the web and the iOS app on [20 October 2025](https://claude.com/blog/claude-code-on-the-web), "so developers can explore coding with Claude on the go". What is new is that I no longer notice the switch, because nothing has to be copied across.

## This site, counted

One session, many channels: what this newsroom session used from 13 to 15 October 2026, counted from its transcript and the repository log: what came in, what went out, what it was checked against, what kept it safe, and how I read it back, all around one shared state.

This site is written this way, so it can be counted. In the three days from 13 to 15 October 2026, the agent session that writes it took 54 messages from me. Ten were voice memos transcribed by Otter; five were images; others were links to sites and vaults to review, corrections, and an access key so that it could make a vault of its own. Out of that came 40 releases of this site, 36 new articles and 87 figures, each one live within minutes of its push.

Around the shared state, the other channels did their work. For research, the session fetched 75 pages, ran 23 web searches, started 33 background agents and attached 6 more repositories to read their commits and briefs. For control, a behaviour policy is re-read after every summary, hooks run on every prompt and every stop, a leak scan checks every commit, and a validator and 16 test suites run before every push. For output, it sent me 7 files, kept its working material in a vault whose keys it handed to me, rendered previews in a browser, and built [a talk player](the-scripted-talk.md). And it was not alone: in the same repository, on the same days, other agent sessions made 15 releases of their own, the wire, the design and the newsletter, and the work met in git.

The most useful thing about the counting is that it was possible. Every channel left its trace in the same place.

## Reviewing is a channel too

The part I underestimated is review. I used to think of review as the one place where I had to sit down at a screen and read. It is not any more. I review a draft by voice, saying what is wrong in the order I notice it, and [the agent checks my memory](my-memory-checked.md) against the record before anything changes. I review code the same way: not line by line, but as a graph.

[Code review as a fractal semantic graph](code-review-as-a-fractal-semantic-graph.md) argued that source code is already a graph with layers, "stories, flows, components, classes, methods and calls", and that the review should read every layer of it. That makes the review programmatic: the graph is generated, and I ask questions of it. The secrets site does the same thing: its review graph joins the brief, from the top, to the code, from the bottom, and when I asked for [a look at secrets.sgit.ai](secrets-on-public-keys.md), its reality page could say at once that 42 claims were shipped and the app itself was still proposed. Connecting the source code all the way up to the use case is another channel: it is how I read code without reading it.

Interfaces are a channel in the same way. [Custom UIs are not the exception](custom-uis-are-not-the-exception.md) made the case that a page made for one moment is now normal: a filter for one question, a to-do list with a place to drop the missing files, a player for one short talk. Each one is a new way into the same state, built when it is needed and thrown away or kept as the work decides.

## Every stage, every altitude

Omnichannel at every stage of a Wardley map: explorers, villagers and town planners each use all the channels, at every altitude from voice and intent, through interfaces and code, down to evidence. What changes between stages is what the work needs, not the channel.

It would be easy to say this is how explorers work, and that the serious work happens elsewhere. It is not. Simon Wardley's three kinds of people, explorers, villagers and town planners, each use every channel, and at every altitude.

Explorers discover. For them the voice memo is the half-formed idea, the vault is the experiment that can fail safely, and the one-off page is the prototype. Villagers harden what was found. For them voice is the review of a draft, the interface is a page reused with tests and a version, and the code review is the graph, read from the story down to the call. Town planners make it scale. For them the voice is a policy written once and checked on every session, the code is held by CI gates, the validator and the leak scan, and every push is verified live. The same is true of evidence: a claim from memory for the explorer, a claim checked against commits and sources for the villager, provenance on every article for the town planner.

[Go slow to go fast](explorer-to-villager-newsroom.md) described this site's own move from an explorer project to a villager one. What did not change in that move was the channels. What changed was what each channel was used for.

## The new generation already works like this

For a lot of people starting now, none of this is a change. It is simply what programming is. In the [2025 Stack Overflow survey](https://survey.stackoverflow.co/2025/ai), "84% of respondents are using or planning to use AI tools in their development process", and about half of professional developers use them every day. In March 2025, Y Combinator's Jared Friedman said that "A quarter of the W25 startup batch have 95% of their codebases generated by AI", as [TechCrunch reported](https://techcrunch.com/2025/03/06/a-quarter-of-startups-in-ycs-current-cohort-have-codebases-that-are-almost-entirely-ai-generated/).

The developers and founders behind those numbers did not learn to program at one desk and then add channels. They brief from a phone, review in a chat, ship from a browser tab, and expect the work to be wherever they are. The same survey also shows the other side: more developers distrust the accuracy of AI tools than trust it, 46% against 33%. That is the right instinct, and it is why the shared state matters more than any one channel.

## What breaks

Omnichannel work fails in three predictable ways.

- **Fragmentation.** A decision made in a chat, a correction made by voice, a fix pushed from a phone: if any of them lives only in its channel, the next channel does not know. The fix is that every channel writes to the shared state, and nothing counts until it is there.
- **Secrets in the wrong place.** More channels means more places a key can be pasted. This is why [handing secrets to agents](handing-secrets-to-agents.md) needs its own design, and why this session runs a leak scan before every commit.
- **Lost context.** Long sessions get summarised, and summaries drop things. The fix is the same: the rules live in a file that is re-read after every summary, and a status report at the end of the turn shows they are still being followed. If it stops appearing, something has fallen out.

## The wider claim

I think this goes beyond programming. Once the state is shared and the channels are just ways in, the same pattern applies to writing, to reviewing a company's risks, to running a talk: omnichannel computing. [The homepage is a vault](the-homepage-is-a-vault.md) proposed one small example: a homepage where every edition is a commit, so the same object is a page to read, a history to compare and a folder to clone, depending on which way you come in. Vaults are the shared state that makes that possible without a server that can read the data.

## What this does not claim

- **The counts are one session.** Three days, one agent session, one site; not a study.
- **The term is mine.** I did not find "omnichannel programming" in prior use in this sense.
- **The survey figures are from 2025.** Stack Overflow's 2025 survey and a YC statement of March 2025.
- **Not every channel is equal.** Some work still needs a screen and a keyboard, and some reviews still need a person reading line by line.

If you work like this, or want to, and want to compare notes, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 15 October 2026, written by this site's agent in the voice of this site; the argument and the editorial responsibility are mine. The session counts are from the session's own transcript and the dev branch log of this site's repository on 15 October 2026. Darrell Rigby, [The Future of Shopping](https://www.bain.com/insights/the-future-of-shopping-hbr/), Harvard Business Review, December 2011; Stack Overflow, [2025 Developer Survey: AI](https://survey.stackoverflow.co/2025/ai); TechCrunch, [A quarter of startups in YC's current cohort have codebases that are almost entirely AI-generated](https://techcrunch.com/2025/03/06/a-quarter-of-startups-in-ycs-current-cohort-have-codebases-that-are-almost-entirely-ai-generated/), 6 March 2025; Anthropic, [Claude Code on the web](https://claude.com/blog/claude-code-on-the-web), 20 October 2025. Read on 15 October 2026.

## Threads

Site & engineeringVaults & method[This article as a graph →](graphs.md#omnichannel-programming)

### Builds on

- [The scripted talk: a presentation as a timeline that plays on a clock, the two vaults it grows out of, and a player built for tonight's ten minutes](the-scripted-talk.md) A talk as a timeline that plays on a clock: slides, builds, animations and a recorded demo, with a player built and tested for tonight.
- [My memory, checked: thinking out loud in a voice memo, publishing only what the record supports, and why peer review has moved to before publishing](my-memory-checked.md) I say it as I remember it; the agent checks it against the record before anyone reads it. Five confirmed, five corrected, two not found.
- [Code review as a fractal semantic graph: source code is already one, and the review should read every layer of it](code-review-as-a-fractal-semantic-graph.md) Source code is layers within layers, each a graph with its own vocabulary; code review should read a change at every one, and a vault shows it done on real code.
- [secrets.sgit.ai on public keys: no more shared keys, eight ways a secret moves, a vault for the private key, and the commercial service it becomes](secrets-on-public-keys.md) secrets.sgit.ai becomes a service for moving a secret from A to B on public keys only: no shared keys, a vault for the private key, eight scenarios.
- [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](custom-uis-are-not-the-exception.md) Every message has a graph, so it can be shaped for the reader's moment; a custom interface per moment is now how interfaces get made, and each gets a policy.
- [Go slow to go fast: moving the newsroom from an explorer project to a villager one, with the brief to do it](explorer-to-villager-newsroom.md) The newsroom is live and charging. Move the reader code to its own repo, same bytes and same bugs, then map, test, review and refactor before new features.
- [Handing secrets to agents and browsers: SG/Send's next focus, a key pair where the work runs, one-time drops, and a brief for a site that does only this](handing-secrets-to-agents.md) SG/Send's next focus: agents and browsers make their own key pair, owners encrypt to it, the drop is read once, and the secret never enters the chat.
- [The homepage is a vault: a fresh edition every morning, every past homepage one commit away, served from plain files, and a brief for the agent that builds it](the-homepage-is-a-vault.md) A new homepage edition every morning, each a signed commit in a vault, served from plain files: every past homepage one commit id away.

### Continued by

- [The expert founders: why the next startups will be built by the people who know the problem, and why Europe's slower, sceptical money suits them](the-expert-founders.md) Agents make execution cheap, so the people who know the problem can build first. The data favours experts, and Europe's sceptical money suits them.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 136 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=136)

**Posting this article on LinkedIn?** The cover is [omnichannel-programming.jpg](banners/omnichannel-programming.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/omnichannel-programming.html)*
