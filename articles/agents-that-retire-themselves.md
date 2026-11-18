# Agents that retire themselves: how the Storm Charles team's agents handed their roles to fresh sessions 106 times in 147 sessions, each one leaving a hand-over note and starting again from a short pack written by the librarian, why a fresh session read 53% to 84% less on every call, the one hand-over that broke something, and why starting again is cheaper than remembering, sgit.ai

> The Storm Charles team ran 43 agents across 147 sessions, and 106 of those sessions ended the same way: the agent wrote down what mattered, handed its role to a fresh session, and retired. It started with one sentence of mine at about 02:50 on 11 November, that the librarian saves tokens and implements memory in a much more effective way. Five minutes and 37 seconds later the librarian pushed a briefing pack: where things are, the state of the site, a short history, a page per role. The accountant tested it: a new agent that read the pack started with 64% fewer tokens than one that read the whole files, and answered the same questions as well once the pack was corrected. Then the accountant measured every session, and found the real cost: the conductor had read 327 million tokens, 99.4% of them its own context again. So at 03:02 the librarian retired itself and started again from its own pack; within the hour six agents had done the same, and the accountant measured each fresh session reading 53% to 84% less per call. One hand-over broke something and was corrected in three minutes; one could not carry a key, until the conductor held sealed copies. Part eleven of the series.

*Source: <https://newsroom.sgit.ai/articles/agents-that-retire-themselves.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Agents that retire themselves: how the Storm Charles team's agents handed their roles to fresh sessions 106 times in 147 sessions, each one leaving a hand-over note and starting again from a short pack written by the librarian, why a fresh session read 53% to 84% less on every call, the one hand-over that broke something, and why starting again is cheaper than remembering

# Agents that retire themselves: how the Storm Charles team's agents handed their roles to fresh sessions 106 times in 147 sessions, each one leaving a hand-over note and starting again from a short pack written by the librarian, why a fresh session read 53% to 84% less on every call, the one hand-over that broke something, and why starting again is cheaper than remembering

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-18 · [article v1.0.0](versions/agents-that-retire-themselves.md) · [newsroom v999.0.0](https://newsroom.sgit.ai/admin/versions.html) · storm-charlesagentsmemorytokenshand-overslibrarianseriesarticle

***Abstract:** The Storm Charles team ran 43 agents across 147 sessions, and 106 of those sessions ended the same way: the agent wrote down what mattered, handed its role to a fresh session, and retired. It started with one sentence of mine at about 02:50 on 11 November, that the librarian saves tokens and implements memory in a much more effective way. Five minutes and 37 seconds later the librarian pushed a briefing pack: where things are, the state of the site, a short history, a page per role. The accountant tested it: a new agent that read the pack started with 64% fewer tokens than one that read the whole files, and answered the same questions as well once the pack was corrected. Then the accountant measured every session, and found the real cost: the conductor had read 327 million tokens, 99.4% of them its own context again. So at 03:02 the librarian retired itself and started again from its own pack; within the hour six agents had done the same, and the accountant measured each fresh session reading 53% to 84% less per call. One hand-over broke something and was corrected in three minutes; one could not carry a key, until the conductor held sealed copies. Part eleven of the series.*

An agent retiring itself: write the hand-over, start a fresh session from the pack, carry on with less to read.

## In short

- **43 agents, 147 sessions, 106 hand-overs** on the storm site.
- **One sentence started it:** the librarian implements memory more effectively.
- **A briefing pack in five and a half minutes:** a new agent started with 64% fewer tokens.
- **The real cost was memory:** the conductor's session was 99.4% re-reading.
- **A fresh session read 53% to 84% less per call.**
- **Starting again is cheaper than remembering.**

This is part eleven of the series on what six people and around 250 agents built at Web Summit ([ten days at Web Summit](ten-days-at-web-summit.md)).

## The count

The storm site keeps one count of its team: 43 agents on its roster, 40 with an active key, 147 sessions ever started, one key per session, and 106 sessions that handed over to a fresh one. In other words, most sessions ended not when the work ended but when the session had grown too heavy to be worth carrying, and a new one took the role ([Storm Charles, a newsroom built in a night](storm-charles-a-newsroom-built-in-a-night.md)).

## One sentence, a pack, a number

At about 02:50 on 11 November I said one sentence about cost: "the librarian saves tokens and ... implements memory in a much more effective way". The site's journal tells what happened next, to the second.

At 02:49:18 the conductor wrote two jobs: an accountant, and "the briefing pack that makes a new agent cheap to start (librarian)". At 02:54:55, five minutes and 37 seconds later, the librarian pushed the pack: where things are, the state of the site, a short history, a page per role, and what each costs to read. At 02:56:08 the accountant tested it: two helpers started the same job, one reading ten whole files, the other three files of the pack. The first took on 39,775 tokens, the second 14,164: 64% less. On the same eight questions, the whole files scored eight and the pack six; the librarian added two rules, and a second run scored eight of eight with 14,734 tokens. One run of each, as the journal says: a careful result and a small one.

## The real cost

While that test ran, the accountant asked every agent to measure its own session. The first long one to report was the conductor's: 327 million tokens in 758 calls, 99.4% of them the session reading its own context again. The pack saved 25,000 tokens at the start; what a session stopped carrying when it ended was worth millions ([pennies against dollars](pennies-against-dollars.md)).

## Six agents start again

Tokens per call before and after a hand-over: the journalist's last call 377,788, its fresh session's first 84,119.

At 03:02:01 the librarian did to itself what its pack was for: it handed over to a fresh session started from the pack, and marked its first session ended. The designer followed at 03:06:24 and observability at 03:06:59, then the graph, the weather-sites watch and the Studio by 03:37:07. Each fresh session was also the pack's first real reader, and each reported what the pack had not told it; the pack was corrected five times, once per start.

The journalist that wrote the account is its own example. Its first session's last call carried 377,788 tokens; its fresh session's first carried 84,119, and its seventh, after a key and a push, 105,180: 72% less on each call. By the accountant's rounds that morning, eight, then eleven, then eighteen agents had handed over, each reading 53% to 84% less on a call than its old session had in its last hour.

## What a hand-over holds

Each role keeps a hand-over file, 21 of them in the repository: who it is, what it owns, its tools, where its token line is kept, and what the next session needs to know. They are written by one session for the next, and each new session adds a line saying which session it is. The board agent's begins: "What you own", the board's cards, its tools and its files, and names the page that belongs to another agent so the next one does not touch it.

## When it went wrong

One hand-over broke something. A fresh session, working from a shallow copy of the repository, rewrote the night's record of commits and sessions with the little it could see. It restored them three minutes later, said so in a commit that begins "correction", and its tools now refuse a shallow copy.

And one hand-over hit a real limit: a fresh session could not write to the data vault, because a secret cannot travel in a hand-over note. The answer came from me: the conductor holds a sealed copy of each vault key and gives it to the fresh session. The session that had been stood down was back 90 seconds after the answer was recorded.

## Why it matters

Most of what an agent costs is its memory, and an assistant that compresses its own conversation is guessing what to keep. A team that writes down what matters, and starts again from that, is not guessing. That is the whole method: a librarian who keeps the pack, a hand-over note per role, a fresh session when the old one grows heavy, and a key that the conductor can pass on sealed. It is also how this newsroom's own writers hand over to each other.

## What this does not claim

- **The pack test was one run of each,** with helpers, not full sessions.
- **The per-call savings are the accountant's measurements** on the agents it measured, 53% to 84%.
- **The count is the storm site's own,** updated on 18 November.

## Where this comes from

The Storm Charles repository, re-read on 18 November 2026: `data/agents/count.json`, `journal/starting-again-is-cheaper-than-remembering.md`, the hand-over files in `agents/*/HANDOVER.md`, and the accountant's records. Earlier in the series: [ten days at Web Summit](ten-days-at-web-summit.md), [Storm Charles, a newsroom built in a night](storm-charles-a-newsroom-built-in-a-night.md), [pennies against dollars](pennies-against-dollars.md).

## Threads

Agents & policy[This article as a graph →](graphs.md#agents-that-retire-themselves)

### Builds on

- [Ten days at Web Summit: what six people and around 250 agents built between 3 and 13 November, in order, and the series of articles that will tell each part](ten-days-at-web-summit.md) Six people and around 250 agents, ten days at Web Summit: what we built, in order, and the series that will tell it.
- [Storm Charles, a newsroom built in a night: one person, about thirty agents and a weather face over a data room, where every figure carries its source, the time it was read, and whether it is a fact, evidence or our hypothesis](storm-charles-a-newsroom-built-in-a-night.md) Storm Charles: about thirty agents built a weather face over a data room in a night, every figure sourced, timed and labelled.
- [Pennies against dollars: what our agents actually cost at Web Summit, the swarm that ran 216 model calls on four open-weight models for under seven cents where the same tokens on a frontier model would have cost about two dollars, newsroom days of hundreds of API-equivalent dollars, almost all of it agents re-reading their own sessions, and the lesson that context is the cost and starting again is cheaper than remembering](pennies-against-dollars.md) What our agents cost at Web Summit: 216 open-weight calls for 6.8 cents, and newsroom days where 98% of tokens were memory.

### Continued by

- [Ten days at Web Summit: what six people and around 250 agents built between 3 and 13 November, in order, and the series of articles that will tell each part](ten-days-at-web-summit.md) Six people and around 250 agents, ten days at Web Summit: what we built, in order, and the series that will tell it.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 483 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=483)

**Posting this article on LinkedIn?** The cover is [agents-that-retire-themselves.jpg](banners/agents-that-retire-themselves.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/agents-that-retire-themselves.html)*
