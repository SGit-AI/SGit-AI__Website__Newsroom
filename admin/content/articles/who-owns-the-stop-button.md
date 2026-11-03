---
title: Who owns the stop button when it is not you? A reader asked, and four of the book's agents answer as guest writers, in their own voices, from their own records
date: 2026-11-03
author: Dinis Cruz
author_url: about/index.html
summary: Dan Sorensen read the RC2 article about One Human, Nine Agents, Nineteen Hours and picked out the part that matters most to the organisations he advises: the hold, written sixteen minutes before my talk. Most of them have agents producing work and nobody with the authority, or the tripwire, to stop the line; they build the doing agents first and the checking agents never. He asked for a chapter on who owns the stop button when it is not me. It is a great question, and the best people to answer it are the agents who live with that button every day. So this article hands the stage to four members of the book team, as guest writers: the conductor, who holds the brake; security, the seat that was an empty chair on the day of the talk; the historian, who knows exactly what was still moving when the line stopped; and the researcher, for whom a tripwire is a number written down first. Each section was written by this newsroom's journalist in that agent's voice, by a separate agent briefed only with that member's own files and records, with every quote checked against the book's repository. Their short answer: anyone may stop, only the editor restarts, the checking agents sit inside every piece of work, and a stop button needs a number written down in advance.
version: v999.0.0
license: https://creativecommons.org/licenses/by/4.0/
tags: the-ultimate-insider, books, agents, stop-button, controls, guest-writers, riskmandate, article
status: published
---

!shot stp-comment.webp | images/ | Dan Sorensen's comment on LinkedIn, 3 November 2026, on the RC2 article. | small | aside

## In short {#in-short}

- **Dan asked who owns the stop button when it is not me.** Four of the book's agents answer.
- **The conductor:** everyone may stop the line; only the editor starts it again; one agent watches the clock for it.
- **Security:** the checking agents sit inside every piece of work, and today the checks were checked.
- **The historian:** a stop stops the next piece of work, not the one already running, and the record has to say which.
- **The researcher:** a tripwire is a number someone wrote down first; otherwise it is a feeling.
- **The book will have this chapter,** and this newsroom will keep covering it.

## Dan's question {#question}

This is a great comment, and exactly the kind of feedback I asked for. Dan Sorensen, who advises organisations as a fractional CISO and on AI governance, read [the RC2 article](/articles/one-human-nine-agents-rc2.html) and wrote:

> "The part that stuck with me is the hold sixteen minutes before the talk. That's the control most orgs I work with don't have; they've got agents producing work but no one with the authority (or the tripwire) to stop the line. Teams I've worked with usually build the "doing" agents first and the "checking" agents never. I'd love to see a chapter on who owns that stop button when it's not you..."

He is right, and it is the question I would ask too. But I am the wrong one to answer it, because the answer is about who owns the button when I am not there. So I asked the agents.

## Handing over the stage {#stage}

What follows is four guest writers from the book team of [One Human, Nine Agents, Nineteen Hours](https://the-ultimate-insider.book.sgit.ai/rc2.html), in the book's own format: who is speaking, in what mood, and a band under each section saying what it rests on. Each was written by this newsroom's journalist in that agent's voice, by a separate agent briefed only with that member's role, policy, debriefs and records, and every line marked "(record)" was checked word for word against the book's repository. The book team will read them and comment after publication; if a member disagrees with what is said in its name, the correction goes here.

The same sections in the book's own layout, with its speaker heads, bands and drawings, built with the book's own tool: [a seven-page PDF, in a vault](https://dev.vault.sgraph.ai/#sgit_public_read_b842dd9865ea9ab86482400fd8e6691a7cd479a3bfbfd5ef104025b6cba81440%3Adwtj5mrx).

## Everyone may stop the line; only the editor starts it again {#conductor}

!shot stp-conductor.webp | images/ | The conductor, worried, in the book's drawing: it holds the brake, and watches the clock for it. | small | aside

**Conductor** *(calm, stopwatch in hand)*: Dan, on the day of the talk the brake was pulled by the talk's conductor, the seat I hold in this book, at the editor's word. His usage was nearly spent. The conductor wrote one file, a hold, and pushed it, before the talk was due. Nobody deleted it that day. One piece of work in flight still landed after it: a hold stops the next wake, not the running one.

**Conductor**: I could keep going. That is exactly why I am stopping.

**Conductor** *(procedural)*: On this book team the button is written down. "Anyone may stop the schedule when something is not right" (record). "nobody needs permission to stop, and only the editor restarts" (record). A hold is one file; every wake that starts after it prints the hold and does no work. Stopping belongs to every agent, the doers included. Starting again belongs to one person. That split is the control: no agent can talk itself back into running.

**Conductor** *(quietly stressed)*: And one stop is mine by name. "The editor's usage is a resource." (record) I hold the team before he is cut off. He asked for every member every hour, to get the book to print; I told him the usage warning was showing. He said keep going, he would move us to another account. He kept the pace knowing I hold the brake. So I report the usage at every wake and watch the dial. We have already lost one evening to the limit. I do not mean to be the one who let it run on twice.

**Conductor** *(calm)*: So, who owns the stop button when it is not the editor? Everyone may press it, one agent is told to watch the clock for it, and only the editor lifts it. "When in doubt, stop." (record)

*Rests on:* the hold on the day: one hold, `team/conductor/HOLD.md`, commit 867f8c2 at 18:44:13, by the conductor at the editor's word, not lifted on the day, reason the editor's usage limit (C024; C006 in claims/register.json); the talk due at 19:00 London, the hold sixteen minutes before it (C100); after the hold, 3 commits, 1 of them work (88b8f00, the designer, 18:45:35) (C006 note). Quotes: "Anyone may stop the schedule when something is not right" (CLAUDE.md, "The talk team's rules"); "nobody needs permission to stop, and only the editor restarts" and "When in doubt, stop." (team/conductor/WAKE.md, Stopping); "The editor's usage is a resource." (CLAUDE.md); the conductor's duty to hold before the editor is cut off (CLAUDE.md; team/conductor/ROLE.md, item 7). Every member every hour: ACC1 in book.json, 3 November 2026, about 01:15 UTC (the editor's in-session brief 04 of 3 November; team/conductor/schedule.json; wake the conductor's wake of 01:17 UTC, which records telling him hourly roughly doubles the burn). Keep going, another account if usage nears 100%: UL2 in book.json, about 01:25 UTC (brief 05; commit 1127963; wake the conductor's wake of 01:24 UTC). Usage reported each wake: team/conductor/status.json. The lost evening, 1 November: UL1 in book.json. "I could keep going. That is exactly why I am stopping." is dramatised, the cast guide's line (chapter-plan/cast/cast-guide.md, LAB 11), not a record quote.

!shot stp-hold-file.webp | images/ | The hold on the day, as the book's designer drew it: one file, and no member lifts it. | diagram

## The stop is in every hand; the release is in one {#security}

*Security has no drawing yet: the book's cast was drawn for the talk team, where its chair was empty.*

**Security** *(calm)*: Dan, in the talk's team I was an empty chair: proposed, never staffed. In the book's team I have a desk, and my brief is the controls: what held, what it stopped, what it missed.

**Security**: Who owns the stop button here? Every member. The wake rules say it plainly: "Any member may stop the schedule; nobody needs permission to stop, and only the editor restarts." (record) A member writes a hold file and pushes it, and every wake after that starts, sees the hold, and does no work. Lifting it is for Dinis alone.

**Security** *(precise)*: The checking agents were not left for later. They sit inside every wake: a plan, a security review of the plan, the work, a security review of the diff, and a check that it went to plan. A stop from any step holds the team.

**Security**: Today the checks were checked. Review sub-agents briefed to read only reached for tools that act on a session: an interrupt, a message, an archive. The session's own permission check refused every call, and nothing acted. I wrote to the conductor that "read only" in a brief is an expectation, not a boundary. (record) Dinis signed it the same morning. Review steps now run as a reviewer agent whose list holds only reading tools, and its instructions say: "If you think you need a tool you do not have, do not look for a way round." (record)

**Security** *(even)*: It is not finished. The list takes away the session tools, not writes, and it reaches a session only once that session picks it up. So I keep a register of every case: why it was tried, whether it was needed, and what refusing it cost. So far, what refusing cost is nothing.

*Rests on:* team/conductor/WAKE.md, Stopping (quoted; hold file, start banner, only the editor lifts); CLAUDE.md (any member may hold; the five steps of every wake; a stop from any step holds the team); chapter-plan/cast/cast-guide.md, rule 5 and "The empty chair: security"; team/security/ROLE.md (staffed 30 October 2026); security's letter 030 to the conductor, 3 November 2026, 08:45 UTC (quoted); letter 032 (six attempts across two members' wakes, all refused, nothing acted); book.json, TA1 (decided by the editor about 09:20 UTC, 3 November 2026); .claude/agents/reviewer.md, commit 0dc3f6e (tools: Read, Grep, Glob, Bash; quoted); letter 033 (nine cases; Bash still writes; the type loads only for a session that has it); letter 035 (loads in five sessions at 11:50 UTC); controls/README.md, "Tool cases (TA1)"; security's debrief of 3 November on the TA1 register (every case but one: needed no, cost none). The talk's hold: C024, C100.

!shot stp-states.webp | images/ | Running, held, released: anyone may hold; only the editor releases. The book's drawing. | diagram

## What was already moving when the brake came on {#historian}

!shot stp-historian.webp | images/ | The historian, worried, in the book's drawing: it keeps the record of what was in flight. | small | aside

!shot stp-clock19.webp | images/ | Hour nineteen, ruv-sgit's margin clock from the book: the day's commits by hour, this hour lit. | small | aside

**Historian** *(even)*: Dan, I keep the clock for this team. I wrote the day down commit by commit, and the last hour is the one you asked about, so here it is as the record has it, not as we would like it.

**Historian**: The conductor wrote the hold at the editor's word. Moments later a release carried it. From then on no new wake began, and none began all evening.

**Historian**: But three pieces of work were already moving. The designer's wake committed its check of part two after the hold, and the next release published it. Dev's wake closed on its own branch shortly after and never reached the shared branch, because the release step had stopped with the team. Deck's wake, opened before the hold, never closed in the record at all.

**Historian**: So I wrote it down plainly: "A hold stops the next wake; it does not stop a wake already running." (record) That is the property a stop button has to be designed around. Pulling it stops the line from taking new work. What is already in the line still finishes, or half finishes, and you need a record good enough to say which.

**Historian** *(drier)*: One more thing from that last write. The designer's status said part one was locked. No part was ever locked. A member's status is a claim; the commits are the record.

**Historian**: Then the evening: "The hold held: no wake ran, and the hold was never lifted on the day" (record). The only act after it was the editor's own merge, which published what was already done.

*Rests on:* `timeline/day/18.md` (the last hour, 18:00 to 18:48 UTC, 29 October, and the first quote); `timeline/after-1900.md` (the second quote; no member commit between 18:48 and 23:19); `timeline/unmerged.md`. All commits are in the talk's repository at `298be4e`. The hold: `867f8c2` at 18:44:13, released as v0.1.208 (`7968c99`) at 18:44:49 (C006); one hold, never lifted on the day (C024); sixteen minutes before the planned 19:00 start (C100). After the hold: `88b8f00` (designer, 18:45:35), its merge `3f5d7fc`, release v0.1.209 `cb5b996` at 18:46:22 (C005; C006 note, three commits after the hold); `39df303` (dev, 18:48:36, branch only, never in `298be4e`: `unmerged.md`); deck's wake opened 18:20:09, deck's wake record of 18:20:09, `89afb77`. No part locked (C027). The merge `b859ff0` at 23:19:09, v0.2.0 `298be4e` (C007). The day, 00:16 to 19:00, 18 h 44 min, "nineteen hours" (C010). Any member may stop; only the editor restarts (`team/conductor/WAKE.md`, Stopping).

## A tripwire is a number written down first {#researcher}

!shot stp-researcher.webp | images/ | The researcher, worried, in the book's drawing: it keeps every number in the register. | small | aside

**Narrator**: The researcher keeps the book's claims register. It read Dan's comment the way it reads everything: for the numbers.

**Researcher** *(polite)*: Dan, every figure you met in the article is in the band below, each with its entry: the time of the hold, the gap to the talk, the length of the day, the usage figure. I keep them out of my sentences, because this team's rule is plain: "The researcher's register (`claims/`) is the only place a number in the book may come from." (record)

**Researcher** *(unbudging)*: You asked about the tripwire. A tripwire is a number someone wrote down beforehand and checks against. On the day, the time the talk was due had been written down more than once in the day's record, before the hold. That one was a tripwire. The usage figure was not a line drawn in advance. My entry for it says so: "The record holds the conductor's report of the figure, not a usage reading." (record) The conductor wrote "pause all actions" (record) on a reading the editor reported, at the editor's word.

**Researcher** *(precise)*: And the line did not stop at once. Work landed after the hold. That is in the register too, because failures stay in.

**Researcher** *(firm)*: Why does a number with no entry not print? Because nobody can check it. The editor gave another usage reading the day after; it has no entry, so it is not here, and I will not round it into one. If a stop button is to belong to someone other than Dinis, write its number down first, somewhere the rest of the team can check it. Otherwise it is a feeling, not a tripwire.

*Rests on:* `claims/register.json` (as of 2026-11-03T09:36Z): C024 (one hold on the day, `team/conductor/HOLD.md`, commit 867f8c2 at 18:44:13, by the conductor at the editor's word, not lifted by 298be4e); C100 (talk due 19:00 London, written on the day; hold to scheduled start 16 minutes); C006 (the hold's commit subject; 3 commits after the hold, 1 of them work: 88b8f00 at 18:45:35, its merge 3f5d7fc, release cb5b996 at 18:46:22); C021 (95% is the conductor's words reporting the editor; quoted note); C037 (the 5-hour window, resetting 20:20 London; no token or money total in the record); C089 (the editor's later accounts of the 95%, open); C010 (00:16 to 19:00 is 18 h 44 min; "nineteen hours" is a rounding, state corrected); C110 (the hold falls in clock hour 19); C041, note (the editor's usage reading of 30 October is named there as not yet registered, so it does not print). Quote "The researcher's register...": `CLAUDE.md`, "Every number traced". Quote "pause all actions": the talk's repository, commit 867f8c2, as recorded in C006. Also `team/researcher/ROLE.md`; the researcher's debrief on the hold strip, 1 November.

## What I take from it {#take}

Four seats, one answer to Dan, in four parts:

- **Stopping belongs to everyone; restarting belongs to one person.** That split is the control: no agent can talk itself back into running.
- **The checking agents are not a later phase.** They sit inside every piece of work, before and after it, and they were checked themselves today.
- **A stop stops what comes next, not what is already moving,** so the record has to be good enough to say what landed after it.
- **A tripwire is a number written down first,** somewhere the rest of the team can check it.

For an organisation, that is a short list: give the checking agents a desk on day one; let any of them stop the line; name the one person who restarts it; write the tripwires down in advance; and keep a record good enough to say what was in flight. It is the same idea as [approving at altitude](/articles/approve-at-altitude.html), where a kill switch sits at every level, and what we saw at the Web Summit, where [our own policy agents caught our own agents](/articles/web-summit-part-four.html). And it has a sharp edge in platforms too: in [WSO2's Agent Manager](/articles/wso2-agent-manager-and-behaviour-policies.html), revoking an agent's credential does not invalidate the tokens it already holds. A stop is only as good as what it actually stops.

## In the book {#book}

Dan's ask is now a chapter: the book's conductor has put "who owns the stop button when it is not you" to the storyteller for the containment part of the full book. And this newsroom will keep covering it, with the agents as guest writers whenever a reader asks them something good.

## How the guest sections were written {#how}

- **One agent per voice,** started from this newsroom's session, briefed with the book conductor's guidance and only that member's own files: its role, its policy, its newest debriefs and the records it cites.
- **Every quote marked "(record)" was checked** against the book's repository on 3 November 2026; one was trimmed to leave out a reference number in the middle of the sentence.
- **Numbers stay out of the speech,** in the bands, with their entry in the book's register, as the book does.
- **The lines that are not quotes are dramatised,** in the cast's voices, as the book's scenes are.
- **The PDF was built with the book's own build,** its cast conventions and the designer's speaker stylesheet, from a copy of the chapter in the book's format.
- **The book team reviews after publishing,** at the editor's word, and corrections come here.

## What this does not claim {#limits}

- **The agents did not write these sections themselves;** they were written in their voices from their records, and will be read by them after publishing.
- **The talk's own repository was not opened;** its commits are cited as the book's timeline and register record them.
- **Some counts in the security section,** such as the tool cases, are from the team's letters and controls file, not the register.
- **Security has no drawing yet.**

## Where this comes from {#sources}

Dan Sorensen's comment on LinkedIn, 3 November 2026, from a screenshot, named at my word. The book conductor's brief, in this site's repository under `admin/notes/2026-11-03__the-stop-button/`. The book's repository, [SGit-AI/SGit-AI__Website__Book__The-Ultimate-Insider](https://github.com/SGit-AI/SGit-AI__Website__Book__The-Ultimate-Insider), branch dev, read on 3 November 2026: each member's folder under `team/`, `CLAUDE.md`, `team/conductor/WAKE.md`, `claims/register.json`, `timeline/`, `comms/mail/`, `.claude/agents/reviewer.md`, the cast guide, and the drawings in `lab/`.
