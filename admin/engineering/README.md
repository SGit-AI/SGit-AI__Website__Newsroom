# Engineering: the issues and the releases, as files

The work on newsroom.sgit.ai, tracked the way [Issues-FS-lite](https://issues-fs.sgit.ai/lite/index.html) tracks it: markdown files with front matter, in three folders, and the file's path is its status. Nothing runs; `ls`, `grep` and `git log` are the tools, and `admin/build/engineering.py` renders the pages under `/engineering/`.

```
admin/engineering/
├── issues/
│   ├── open/NNN-slug.md        what is asked and not yet done
│   ├── blocked/NNN-slug.md     waiting on something named in blocked_on
│   └── done/NNN-slug.md        done, with an Outcome section appended and screenshots where they help
├── releases/vX.Y.Z.md          one file per release: which issues it carries, and what it says
└── README.md                   this file
```

## A card

```
---
id: 001
title: The pane closes on every navigation
kind: bug                 # bug | story | task
priority: high            # low | normal | high | urgent
created: 2026-10-12T15:00:00Z
source: the owner's first run of v0.12.0 on an iPad, 12 October 2026
release: v0.12.1          # the release it shipped in, or is planned for; empty when not planned
estimated_effort: small   # small | medium | large
blocked_on:               # only in blocked/
---
# The title again

## What happens, or what is asked
## Scenario            (Gherkin: Given, When, Then; the acceptance criteria)
## Mock-up             (words or a sketch of what the reader sees, before it is built)
## Outcome             (appended when the card moves to done/: what shipped, in which release, what was left)
## Screenshots         (../shots/NNN-*.png, taken from the built site by admin/build/shots or by hand)
```

Ids are three digits, in order of creation, never reused. Moving a card is `git mv` between the folders; nothing is deleted and nothing is edited in place except by appending. Every change to the site is connected to a card, and every release file names its cards, so a version row on [the release history](../versions.html) can say which issues it answers by id.

Where a card comes from is recorded in `source`: the owner's feedback (the vault pane's lane, a screenshot, a note in chat), a brief on sgit.ai, a finding in a test, or the agent's own reading of the site.

## A release

```
---
version: v0.12.1
date: 2026-10-12
issues: [001, 002, 003]
kind: patch               # patch | minor | major
---
# v0.12.1: one line
What it carries, in prose, and what was found on the way.
```

Every push is a patch release (the last number). A minor or major release is a consolidation the owner asks for.
