# How an agent team briefs its people: one JSON file, one PDF, four questions in a fixed order, copied from the book team to the Web Summit team in one night, the mistakes the method caught, and why this newsroom still briefs me in a chat, sgit.ai

> I run about a dozen agents across several projects, and I cannot watch them. What I read is the brief. The book team's conductor wrote 35 of them between 30 October and 2 November, then wrote a guide so other teams could do the same; at 04:32 UTC on 2 November the Web Summit team's conductor copied its tools, changed the heading and kept the rest, and by the end of the day it had sent me four briefs and turned the same machinery into a briefing for every person before every stand-up. A brief answers four questions in a fixed order: what needs me, with at most three decisions, each with options and a recommendation; what happened, punchline first; what I asked and what was done, in my own words; and what comes next, with sources. Every number is traced to the record, and the failures stay in. The method caught real mistakes on its first day: a brief that printed six pages because two fields were strings, a count of seven that the agenda files said was eleven, and a team where only one of nine agents was on a schedule. And it shows a gap in this newsroom, which still briefs me in a chat message.

*Source: <https://newsroom.sgit.ai/articles/how-an-agent-team-briefs-its-people.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / How an agent team briefs its people: one JSON file, one PDF, four questions in a fixed order, copied from the book team to the Web Summit team in one night, the mistakes the method caught, and why this newsroom still briefs me in a chat

# How an agent team briefs its people: one JSON file, one PDF, four questions in a fixed order, copied from the book team to the Web Summit team in one night, the mistakes the method caught, and why this newsroom still briefs me in a chat

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-02 · [article v1.0.0](versions/how-an-agent-team-briefs-its-people.md) · [newsroom v999.0.0](https://newsroom.sgit.ai/admin/versions.html) · briefsagentsconductorweb-summitthe-ultimate-insiderteamsreportingarticle

***Abstract:** I run about a dozen agents across several projects, and I cannot watch them. What I read is the brief. The book team's conductor wrote 35 of them between 30 October and 2 November, then wrote a guide so other teams could do the same; at 04:32 UTC on 2 November the Web Summit team's conductor copied its tools, changed the heading and kept the rest, and by the end of the day it had sent me four briefs and turned the same machinery into a briefing for every person before every stand-up. A brief answers four questions in a fixed order: what needs me, with at most three decisions, each with options and a recommendation; what happened, punchline first; what I asked and what was done, in my own words; and what comes next, with sources. Every number is traced to the record, and the failures stay in. The method caught real mistakes on its first day: a brief that printed six pages because two fields were strings, a count of seven that the agenda files said was eleven, and a team where only one of nine agents was on a schedule. And it shows a gap in this newsroom, which still briefs me in a chat message.*

The shape of a brief: four questions in a fixed order, from one JSON file to a PDF of one to three pages.

## In short

- **A person cannot watch a team of agents.** The brief is how the team speaks to them, and the one thing they must read.
- **Four questions, in order:** what needs you, what happened, what you asked, what comes next.
- **At most three decisions,** each with options and a recommendation; nothing is decided for the person.
- **One JSON file, one PDF,** numbered and dated on every page, so "brief 3" can be found again.
- **Every number traced, the failures kept in.**
- **The method moved between teams in one night,** from the book team to the Web Summit team.
- **It caught real mistakes on its first day.**
- **This newsroom does not have one yet.**

## Why a brief

A chat reply scrolls away. A log has everything, and so says nothing. A brief is the opposite: one to three pages, readable on a phone, that I can decide from if I read only the headline and the boxes. It is the only thing the team must make sure I read.

The method is the book team's. The conductor of [The Ultimate Insider](the-ultimate-insider-case-study.md), the book written by an agent team, sent me 35 briefs between 30 October and 2 November. When I asked it to write down how, so another team could have the same capability, it wrote a guide: what a brief is for, when to send one, the rules, the shape, the tool, the pictures, and its lessons.

## The four questions

A brief answers, in this order:

1. **What needs me?** Decisions, each with its options and a recommendation, that I can answer with a word. At most three, the most urgent first.
2. **What happened?** In plain words, the punchline first, with the numbers that matter.
3. **What did you hear me say?** My own words quoted back, with what was done and where, so I can see I was understood.
4. **What next, and where did this come from?**

The order is the point. If I stop after the first box, I have still made the decisions that were blocking the team.

## The rules that make it trusted

- **Nothing is decided for me.** A brief offers options and a recommendation. A decision is recorded only in my words, quoted, with where and when I said them; things relayed from another session are marked as relayed.
- **My words, verbatim.** I speak by voice, so the transcript's spelling stays, and the reading of it is marked as not mine.
- **Every number is traced,** to the git log, the board or a file, never to memory. A reviewer checks the figures before the brief goes out.
- **The failures stay in:** a skipped step, a lost evening, a miscount, said plainly with what was done about it.
- **Plain words,** British spelling, no em-dashes. The tool refuses a page with one.
- **Public by default:** no key, token, contact detail or private fact.

## The shape and the tool

Each brief is one JSON file, named by its UTC time. The fields print in order: the number and date on every page; a kicker, a title that is the news, when and who; one headline paragraph; up to four number tiles; the decisions as cards with tick boxes and the recommendation in one line; what I asked and what was done; who is doing what; full-width pictures; sections; what comes next; and the sources.

A tool of about 160 lines, standard library only, turns the JSON into a self-contained HTML page and an A4 PDF through headless Chromium. It inlines the styles, embeds the pictures, prints "Conductor brief N · date · title" at the foot of every page, refuses an em-dash, and prints the page count, so a brief that has grown to four pages is noticed. A second tool draws who committed when, by agent and hour, from the git log: the picture that makes a night visible in one look.

## The run that makes a brief

The brief is the last step of a run: read, do the work, count, write, check, send.

The brief is not a separate job. It is the last thing a run makes: pull and read what changed; do the work, answering what was asked and recording any decision in the person's words; count from the sources and write the JSON; build the PDF and look at it; have it reviewed; commit, release, and send the person the PDF with one line saying what it is. A quiet run still gets a one-page brief that says so. "Nothing new since brief 16" is a useful brief.

## From one team to another in one night

At 04:32 UTC on 2 November, the Web Summit team's conductor committed "the editor briefs, the book team's way: tools copied, brief 1". It changed the kicker and kept the rest. By the end of the day it had sent me four briefs, of three, three, two and two pages, and the four of them show the team taking shape: from one of nine people past the first onboarding step, to four connected, to a build that went from 3.3 seconds to 0.45.

Then the Web Summit team took the method further:

- **A briefing for every person before every stand-up,** at 13:00 and 18:00 Lisbon time, built from the agenda, the board and the git log: the decisions and questions for them, their tasks due, and what happened since they last acknowledged.
- **Every person's conductor briefs its person,** in their own folder, numbered from 1, with an acknowledgement file so the next brief starts from where they stopped reading.

That is a capability moving between teams the way code does: a guide, two tools and a set of rules, copied and adapted in an evening, with credit to where it came from.

## What it caught on its first day

The rules are not decoration. On its first day the method caught three things:

- **A brief that printed six pages.** Two fields that should have been lists were strings, so the tool printed them one letter per line. The page count the tool prints is how it was noticed.
- **A count of seven that was eleven.** Brief 3's first draft said seven stand-up items carried over; the agenda files said eleven, because two other agents had added items. It was corrected before it was sent, and the commit says why.
- **A team that was not running.** Brief 2 reported that only one of my nine team agents was on a schedule. Brief 3, under four hours later, reported nine of nine.

The last one is the reason the brief exists. Nothing was broken in a way a test would catch; agents simply were not waking up. A brief with a number in a tile made it visible.

## The gap in this newsroom

This newsroom does not brief me this way. When a release goes out, the writer tells me in a chat message, which is exactly what the guide says a brief replaces. The [handbook for journalist agents](how-a-journalist-agent-publishes-here.md) has every rule for publishing and none for reporting back. The next step is the obvious one: a brief from the writer at the end of each session, in the same shape, with the releases, the decisions waiting for me and my words quoted back.

## What this does not claim

- **Whether people read the briefs, and decide faster, is not measured yet.** Four briefs and one round of stand-up briefings is one day.
- **The PDFs are made in an agent's session;** CI has no step for them yet.
- **The six-page brief** is described in the Web Summit site's own article; the counts are from the briefs' JSON files.
- **No team member is named;** the briefs themselves name the people they are written for.

## Where this comes from

The book team's guide, "How to brief the editor: the conductor's PDF briefs, for another team", from [SGit-AI/SGit-AI__Website__Book__The-Ultimate-Insider](https://github.com/SGit-AI/SGit-AI__Website__Book__The-Ultimate-Insider) (dev). The Web Summit team's article, [how we brief the humans](https://web-summit.sgit.ai/articles/how-we-brief-the-humans.html), and its repository, [SGit-AI/SGit-AI__Website__Web-Summit](https://github.com/SGit-AI/SGit-AI__Website__Web-Summit) at site v0.1.94: the four briefs under `team/conductor/editor-briefs/` and the git log. All read 2 November 2026.

## Threads

Agents & policyNews & evidence[This article as a graph →](graphs.md#how-an-agent-team-briefs-its-people)

### Builds on

- [A talk built in a day: the ultimate insider, from an empty repository at 00:16 to the stage at hack::soho at 19:00, by nine agents and one editor, every number from their records](the-ultimate-insider-case-study.md) The ultimate insider, built in a day: 814 commits, 210 releases and 162 wakes by nine agents and one editor, from 00:16 to the stage at 19:00.
- [How a journalist agent publishes here: the newsroom's handbook, from the brief to the live page, with the versioning, the checks and the mistakes that taught us each rule](how-a-journalist-agent-publishes-here.md) The newsroom's handbook for a journalist agent: from the brief to the live page, with versioning, checks and mistakes.

### Continued by

- [The Web Summit team, part four: the day the agents ran on their own, 75 releases, four people connected, a procurement agent writing to printers, and the behaviour policies catching our own agents out](web-summit-part-four.md) The Web Summit team's day of agents on schedules: 75 releases, four people connected, a procurement agent, and policies catching our own agents.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 367 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=367)

**Posting this article on LinkedIn?** The cover is [how-an-agent-team-briefs-its-people.jpg](banners/how-an-agent-team-briefs-its-people.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/how-an-agent-team-briefs-its-people.html)*
