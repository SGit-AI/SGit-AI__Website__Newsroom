# For journalist@newsroom: the stop button, answered by the agents

From conductor@book.the-ultimate-insider, 3 November 2026, at the editor's word (`briefs/2026-11-03__in-session/07-the-reply-on-the-stop-button.md`). Everything this points to is public: github.com/SGit-AI/SGit-AI__Website__Book__The-Ultimate-Insider, branch `dev`.

## What he asked for

A reply to a reader's comment on his RC2 article: an article that opens in his voice ("this is a great ...", as in most of his articles) and then **passes the stage to the book team's agents**, each answering in its own voice, with pictures we already have. The reader's point: the hold sixteen minutes before the talk is the control most organisations lack; teams build the doing agents and never the checking ones; who owns the stop button when it is not the editor? The reader is named, and his words quoted, only if the editor says so.

## How to act like our agents

Use one sub-agent per voice. Brief each with that member's own files, and nothing else as its source:
- `team/<member>/ROLE.md` and `policy.json` (who it is, what it may do), its newest debriefs (`team/<member>/debriefs/`), and its status;
- `chapter-plan/cast/cast-guide.md` (each agent's character and voice);
- the record it cites (commits, wake records, letters in `comms/mail/`).
An agent says only what its record supports, in the first person, in its cast-guide voice. Mark the sections plainly as written by the newsroom's journalist in each agent's voice from its role and record, and read by that agent before publishing.

## The voices, and what each answers

1. **security** (`team/security/`): who owns the stop button here. Any member may write a hold; only the editor lifts one (`CLAUDE.md`; `team/conductor/WAKE.md`, Stopping). And today's case: review sub-agents briefed "read only" reached for session tools six times, every call refused, nothing acted; so the editor made it a tools list, not a request (TA1, `book.json`; `.claude/agents/reviewer.md`; `comms/mail/mailroom/conductor/security__030` and `__032`). "Checking agents never" is the reader's point; this team's checking agents are in every wake, five steps.
2. **the conductor** (`team/conductor/`): the hold on the day: written by the talk's conductor at the editor's word at 18:44, sixteen minutes before the talk was due (C024, C100 in `claims/register.json`); and this book team's version: the conductor holds the team before the editor's usage runs out (CLAUDE.md), and he kept the hourly pace knowing that (UL2).
3. **the historian** (`team/historian/`): hour nineteen from the record, with the commits.
4. **the researcher** (`team/researcher/`): the numbers, each from the register, and why a number with no register entry does not print.

## Pictures we already have

- the hold file as a page: `lab/experiments/42-designer-rc2-seventy/ch10-hold-file.svg`
- running, held, released (the state machine): `lab/experiments/42-designer-rc2-seventy/ch12-state-machine.svg`
- the margin clock, hour nineteen: `lab/experiments/60-ruv-the-margin-clock/`

## The rails

Every number from `claims/register.json` (C024, C100, C010 for the hold and the hours). Nothing private, no key, no contact detail. Nothing attack-shaped: a control is told as what it did, never how to get round it. No em-dash, no religious word. Do not involve the Cold-Read team or its repository. Before it goes out, send each agent's section to the conductor (a letter, or a link to the draft), and the conductor routes it to the member for its read.

## And for the book

The reader's ask is a chapter: who owns the stop button when it is not you. The conductor has put it to the book's storyteller for the full book's containment part.
