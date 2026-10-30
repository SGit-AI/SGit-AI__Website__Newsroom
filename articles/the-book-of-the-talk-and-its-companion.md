# The book of the talk by morning: RC1 of The Ultimate Insider, written from the record, read cold by a second team, with a companion PDF that turns reviews into tick boxes, sgit.ai

> The night after I gave The ultimate insider at hack::soho, two agent teams worked on the book of it while I slept. One, in a new repository started at 00:35 UTC, built the book's machinery: a claims register, a timeline of the day hour by hour, an index and a chapter plan. The other, started two minutes later, was given only the talk's repository at one commit and told to read it cold: thirteen agents, no briefing, every claim cited to a path or written as "the record does not say". By 10:00 the cold read had made 349 commits, 78 releases and about 42,400 words, and a 16-page debrief as a PDF. At about 10:00 I signed the chapter plan and said I was flying later and wanted a PDF to read on the plane. At 11:00 I had two. RC1 is 294 pages at 6 by 9 inches: thirteen chapters, a chapter on how to read a Wardley map, sixteen maps, 28 infographics, 50 call-outs and an appendix that reruns every number from git. The second PDF is the part I think matters most. The companion is 67 A4 pages of 98 cards, from eight readers: the book team's roles and the team of my previous book. Each card quotes one sentence of RC1, finds the page it is on and prints that page small beside it, and gives me boxes to tick and lines to write on. 53 of the cards are decisions only I can take. A book review used to be a pile of comments; here it is a form I can fill in on a plane, and the conductor turns my ticks into decisions. This article tells how both PDFs were made, with the times from the two repositories, and what went wrong, including a leak account that turned out to be about values that were never secrets.

*Source: <https://newsroom.sgit.ai/articles/the-book-of-the-talk-and-its-companion.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The book of the talk by morning: RC1 of The Ultimate Insider, written from the record, read cold by a second team, with a companion PDF that turns reviews into tick boxes

# The book of the talk by morning: RC1 of The Ultimate Insider, written from the record, read cold by a second team, with a companion PDF that turns reviews into tick boxes

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-30 · [article v1.0.0](versions/the-book-of-the-talk-and-its-companion.md) · [newsroom v0.14.2](https://newsroom.sgit.ai/admin/versions.html) · case-studybooksagent-teamsthe-ultimate-insiderpublishingreviewsleanpubarticle

***Abstract:** The night after I gave The ultimate insider at hack::soho, two agent teams worked on the book of it while I slept. One, in a new repository started at 00:35 UTC, built the book's machinery: a claims register, a timeline of the day hour by hour, an index and a chapter plan. The other, started two minutes later, was given only the talk's repository at one commit and told to read it cold: thirteen agents, no briefing, every claim cited to a path or written as "the record does not say". By 10:00 the cold read had made 349 commits, 78 releases and about 42,400 words, and a 16-page debrief as a PDF. At about 10:00 I signed the chapter plan and said I was flying later and wanted a PDF to read on the plane. At 11:00 I had two. RC1 is 294 pages at 6 by 9 inches: thirteen chapters, a chapter on how to read a Wardley map, sixteen maps, 28 infographics, 50 call-outs and an appendix that reruns every number from git. The second PDF is the part I think matters most. The companion is 67 A4 pages of 98 cards, from eight readers: the book team's roles and the team of my previous book. Each card quotes one sentence of RC1, finds the page it is on and prints that page small beside it, and gives me boxes to tick and lines to write on. 53 of the cards are decisions only I can take. A book review used to be a pile of comments; here it is a form I can fill in on a plane, and the conductor turns my ticks into decisions. This article tells how both PDFs were made, with the times from the two repositories, and what went wrong, including a leak account that turned out to be about values that were never secrets.*

RC1's cover, an infographic, a map and call-outs, and the first card page of its companion.

## In short

- **Two teams worked on the book overnight.** The book team built the register, timeline and plan; a second team read the talk's repository cold.
- **The cold read knew nothing but the record.** Thirteen agents, one repository at one commit, every claim cited or marked as unknown.
- **RC1 followed the signed plan within an hour.** 294 pages, thirteen chapters, sixteen maps, 28 infographics and 50 call-outs, built by about 10:57 UTC.
- **The companion is the innovation.** 98 cards, each pinned to a sentence and a page of RC1, with boxes to tick: a review I can answer on paper.
- **Every number has an id.** RC1 uses the claims register, C001 to C042, and its appendix says how to rerun each one from git.
- **The two teams checked each other.** RC1 has a chapter on what the cold reader saw that the insiders missed.
- **The failures stay in.** A kinder account of three findings was corrected within the hour; my own check today shows the values found were not secrets.

## What happened that night

I gave [the talk](the-ultimate-insider-case-study.md) at 19:00 on 29 October. Before I went to bed I asked for two things, in two new repositories on GitHub.

The first, [SGit-AI__Website__Book__The-Ultimate-Insider](https://github.com/SGit-AI/SGit-AI__Website__Book__The-Ultimate-Insider), started at 00:35 UTC on 30 October, is the book. Its brief from me was the book of the day: how a team of agents and one person built a talk in a day, and the controls that kept the team in check. Its conductor had its own session key by 01:17, and by 01:42 six members had theirs: a historian, a librarian, a publisher, a researcher, security and a storyteller, each with a role file, a behaviour policy and an hourly slot. By 10:00 the repository had 215 commits.

The second, [SGit-AI__Website__Cold-Read__The-Ultimate-Insider](https://github.com/SGit-AI/SGit-AI__Website__Cold-Read__The-Ultimate-Insider), started two minutes later, is the cold read. It was given one thing: the talk's repository, pinned at commit `298be4e`. Its brief says: "Nothing else: no briefing on what it is, no memo, no transcript, no contact with any other team." Everything it said had to cite a path and a commit, or say "the record does not say", and "Guessing is a finding against you."

The night in both repositories, UTC, from the first commit to RC1 on the book's site.

I did not want a single team to write the book about itself, because a team reading its own record reads it through what it already knows. The second team was there to see what the first one could not.

## The cold read

The cold read's conductor ported the talk team's own machinery, its rules, tools, build and gate, rather than inventing new ones, and had its first release, v0.1.0, out by 01:20. By 01:54 it had onboarded twelve members, each in its own session with its own key and hourly task: a historian, a technologist, security, GRC, a journalist, an analyst, a critic, and five synthetic readers who read the published talk as strangers.

Its debrief, a 16-page deck also published [as a PDF](https://the-ultimate-insider.cold-read.sgit.ai/debrief/cold-read-debrief.pdf), counts the night as of 10:00 UTC: 349 commits on dev, 78 releases numbered by CI, 85 wake records of five steps each, about 42,400 words in the deliverables, no holds and no request left unanswered. Members finished on their own and paused their own tasks: the first reader at 04:49, the historian at 07:22, the five readers' synthesis at 07:50.

What it found is the reason it exists. It counted 816 commits reachable from `298be4e`. It found fourteen decisions left open in the record, among them that the hold of 18:44 was never lifted before the 23:19 merge, and that the talk's security role was never staffed. Its critic found where the talk and the record do not meet, starting with the second beat's claim of "not one hold". Its five readers agreed, independently, that the first half convinces and that the sources page breaks its own promise. None of this came from me, and none of it came from the team that built the talk.

## RC1: from a signed plan to a printed book

At about 10:00 I read the storyteller's chapter plan, draft 5, and signed it as the team proposed. Then I told the book's conductor: "can you work on creating the first RC of this book, use the judgement of the team. I'm flying later today and want to print this pdf and read it on the flight."

No writer was staffed, so the conductor drafted the chapters with sub-agents, one or two chapters each, from a written brief: the record only, numbers only from the claims register with their ids, the failures kept in, no em dashes, and each chapter ending with where it came from. The conductor's commit at 10:07 says "RC1 begun". At 10:28 another says "RC1, thirteen chapters, Appendix A and 42 images, ready for the publisher".

That first version was printed, and at about 10:30 I sent a voice memo with what I thought was missing: the plumbing (CI, the non-functional requirements, the quality gates) and the two and a half years of work that met on the day, Wardley maps from simple to complex, introduced early, and the concepts explained as they appear. At about 10:45 I asked for a cover and for the reviews of every role in a form I could take with me.

What came back by about 10:57, built from `team/conductor/rc1/`, was RC1 as I printed it: 294 pages at 6 by 9 inches, with a cover (one of three concepts), a chapter on how to read a Wardley map, sixteen maps, a chapter on what was already there, a part on concepts and principles, 28 infographics and 50 call-outs placed at build time, and a corrections pass. It is about 69,000 words in its source files, against the plan's 49,200, which is a finding in itself: a first draft by agents runs long. It is [on the book's site](https://the-ultimate-insider.book.sgit.ai/rc1/), with its hash.

All 294 pages of RC1 in reading order, 21 to a row.

The infographics follow a written visual language: one dark ink, one accent for the thing to see first, nothing under about 9 point at the printed size, and the claim id printed on the image. The renderer refuses text that runs off its canvas or overlaps other text. The call-outs have five kinds (CONCEPT, THE NUMBER, TAKE AWAY, WATCH OUT, TRY THIS), each placed after the paragraph of an anchor sentence that is checked to occur exactly once.

## The companion: a review I can answer on paper

This is the part I want to dwell on, because I have not seen it done before.

When a book is reviewed, the comments arrive as a pile: notes in a document, threads in a tool, emails. The author has to find each passage, decide, and remember what was decided. With a team of agents that pile grows fast, because every role can review every chapter in minutes.

The companion turns the pile into a form. It is a second PDF, 67 A4 pages, made to be read beside RC1. It holds 98 cards from eight readers: the conductor, the storyteller, the historian, the librarian, the researcher, security and the publisher, each drafted by a sub-agent reading RC1 as that role, and the Gen ZX Founders team, the team of my book Generation Z Developers, reading it the way that book's editor, reviewer, illustrator and publisher would. Each member reviews its own cards at its next wake and may change or withdraw them.

The companion's 98 cards by the role that drafted them and by kind.

Every card has a kind: 53 decisions, 25 comments, 13 questions and 7 rationales. A decision has a box per option and a box for "something else", with the role's recommendation and why. A question has lines for my answer. A comment or a rationale has two boxes, agreed or not agreed. The last pages list every decision on one sheet.

What makes it work on paper is the link to the page. Each card quotes one sentence of RC1, copied exactly. The script that builds the companion, `companion.py`, finds that sentence in the RC1 PDF's text, takes the page it is on, and prints a small picture of that page on the card, with its number. I do not have to search: the card says "RC1 page 4" and shows me what page 4 looks like.

The conductor's first card, on the book's voice, and the page of RC1 its sentence is on.

The first card is the conductor's, and it is the right first question: RC1 is written about me, in the third person, because no agent may speak for me. Should the whole book move into my voice? Three options, a recommendation (first person for the opening, the close and the principles first, the record chapters later), and lines for my note.

When I am back, the conductor turns my ticks into open decisions in `book.json` for me to sign. So the loop is: agents review, the review becomes a printed form, I fill it in with a pen, and the form becomes data. It is the same idea as [reading with a pen](reading-with-a-pen.md), where I mark printed pages and an agent does the rest, but here the agents prepared the questions before I picked up the pen.

Because RC1 and the companion are built together, they are replaced together: when RC1 is revised in place, the companion is rebuilt so its page numbers still match.

## Built, rebuilt and checked

At 11:02, with my usage near its limit, the conductor wrote a handover, and at 11:12 a new session on another account took over with its own key. Its first job was to check what it had inherited. It rebuilt both PDFs from the repository with the same scripts and compared them with the files I had printed: RC1 came out at 294 pages and the companion at 67, the extracted text identical, every page rendered at 50 dpi identical pixel for pixel, and 22 sampled pages at 150 dpi identical in colour. Only the embedded timestamps differed. At 11:28 RC1 went on the book's site, with its hash.

Every number in RC1 carries the id of its entry in the researcher's claims register, from C001 to C042, so a reader can check it. Appendix A gives, for each one, a command to rerun it from the talk's git history. The researcher checked RC1's numbers against the register at 10:37 and sent six places back to the conductor.

## Two readings of one record

Chapter 11 of RC1, What the cold reader saw, reads the cold read's finished work against the book team's. Where the two agree, the record is solid: both put the hold at 18:44:13, both found that no part of the talk was ever locked, both found the overnight freeze of the deck. Where they disagree, one of them was blind. The book team knew things the cold read could not, such as the talk as given and my debrief, added after the day. The cold read saw things the insiders had stopped looking for. The book's security member, for one, confirmed at 10:28 a finding about a key file that the cold read had made first.

This is the method I want for every book from now on: one team that knows everything, one that knows only the record, and the book written from where they meet.

## What went wrong

- **RC1 was first pushed with a kinder account of three review findings** than the record supports. During the night of the talk, the researcher's reviews found values in captured web pages, redacted them, and recorded each finding after the captures had already been pushed to a public vault. RC1 said the findings had stopped them in time. The historian's card in the companion says "The book is kinder to the controls than the record is", and the corrections pass fixed it.
- **The values themselves were not secrets.** I asked about them today, and the newsroom's writer checked the vault's history: anonymous cookies that bot-protection and load-balancing services set on the researcher's fetcher, session ids for a visitor who never logged in, and the anti-forgery tokens a site puts in every visitor's form. No key, no credential to any account, no personal data. The researcher's own audit at 07:25 that morning had said the same. So the lesson for the book changes: the gate had no pattern that could tell a harmless value from a harmful one, and the reviews over-flagged three times. The companion was kept off the book's site because its cards point at where those values are; that reason no longer holds.
- **The first build read a stale PDF** from the wrong output folder. A page count caught it.
- **Two infographics went stale** after the corrections and were withdrawn until the second design round.
- **A first draft by agents runs long:** about 69,000 words against a plan of 49,200.
- **I hit my usage limit.** At 94% every scheduled task was paused, both teams', and the work moved to another account by a written handover.

## What it shows

A book is now a release. RC1 has a version, a hash, a build that can be rerun to the pixel, a gate, a register for every number and a page on the web, and it was made between my signing the plan and leaving for the airport.

But the companion is what I will keep. The hard part of making a book was never writing the first draft; it was the editing: hundreds of small decisions, each tied to a sentence on a page, and the discipline to take them all. Agents can now prepare every one of those decisions, with the options and a recommendation, and lay them out so that one person with a pen can take them on a flight. That changes what one author can do.

The first edition goes to Leanpub. The publisher is moving RC1 into Markua, Leanpub's markdown, and the next step is the revision from my ticks.

## What this does not claim

- **RC1 is a release candidate, not the book.** It is in the third person, it has no interview with me, its title is a working title, and its chapters were drafted alone and do not always agree on emphasis. It says so on its own fourth page.
- **The companion's role cards were drafted by sub-agents reading as each role,** not by the members, who review them at their next wake.
- **The times are from the two repositories' commits, keys and debriefs.** Where a time came from a brief or debrief that says "about", I say about.
- **The word count of about 69,000** is my count of the chapter source files with `wc -w`, markdown included; it is not the register's.
- **The cold read's numbers are as of 10:00 UTC**, from its debrief; its critic and GRC member were still in their last wakes.
- **My interest:** these are my repositories, my talk and my book.

## Where this comes from

- The book's repository, [SGit-AI/SGit-AI__Website__Book__The-Ultimate-Insider](https://github.com/SGit-AI/SGit-AI__Website__Book__The-Ultimate-Insider), read on 30 October 2026 at `41b8ba6`: `README.md`, `REALITY.md`, `book.json`, `team/conductor/rc1/` (`BRIEF.md`, `0-about-this-release-candidate.md`, `pdf/README.md`, `annotations/`, `infographics/README.md`, `tools/companion.py`), `team/conductor/debriefs/2026-10-30__rc1-principles-maps-companion.md`, `briefs/2026-10-30__in-session/`, `team/*/key.json` and the git log.
- The two PDFs in `team/conductor/rc1/pdf/`: `the-ultimate-insider-RC1.pdf` (294 pages) and `the-ultimate-insider-RC1-companion.pdf` (67 pages), rendered with `pdftoppm` for the figures. RC1 is published at [the-ultimate-insider.book.sgit.ai/rc1/](https://the-ultimate-insider.book.sgit.ai/rc1/).
- The cold read's repository, [SGit-AI/SGit-AI__Website__Cold-Read__The-Ultimate-Insider](https://github.com/SGit-AI/SGit-AI__Website__Cold-Read__The-Ultimate-Insider), read on 30 October 2026 at `14d6cfd`: `BRIEF.md`, `README.md` and the conductor's debrief, published at [the-ultimate-insider.cold-read.sgit.ai](https://the-ultimate-insider.cold-read.sgit.ai/).
- The talk's repository, [SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider](https://github.com/SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider): `evidence/updates/2026-10-29__the-vault-history-checked.md`; and its public evidence vault, cloned with its published read key, whose revision `836dfa34559e` was searched for cookie and form-token names, printing names and lengths only.
- Researched and written by this site's writing agent from the repositories and the PDFs, at my request.

## Threads

Agents & policyVaults & method[This article as a graph →](graphs.md#the-book-of-the-talk-and-its-companion)

### Builds on

- [A talk built in a day: the ultimate insider, from an empty repository at 00:16 to the stage at hack::soho at 19:00, by nine agents and one editor, every number from their records](the-ultimate-insider-case-study.md) The ultimate insider, built in a day: 814 commits, 210 releases and 162 wakes by nine agents and one editor, from 00:16 to the stage at 19:00.
- [Reading with a pen again: I mark the printed page, photograph it, and an agent does the part that always made me stop, which changes how I read every book](reading-with-a-pen.md) Mark the printed page, photograph it, and an agent does the processing that always made me stop highlighting. The book's new name is in its margins.

### Continued by

- [A brief for the Web Summit team: an event site run by an ephemeral agent team, built from this week's template, with a map of every company we should meet](web-summit-team-brief.md) A brief for the Web Summit team: an event site run by an ephemeral agent team, from a proven template, with a map of every company to meet.
- [A book that looks like the team that made it: what the best visual books, Leanpub's Markua and learning research teach, and what an agent team can put on a printed page](books-for-a-new-generation-of-publishing.md) What the best visual books, Leanpub's Markua, print-on-demand costs and the learning research teach, and what an agent team adds to a printed book.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 326 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=326)

**Posting this article on LinkedIn?** The cover is [the-book-of-the-talk-and-its-companion.jpg](banners/the-book-of-the-talk-and-its-companion.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-book-of-the-talk-and-its-companion.html)*
