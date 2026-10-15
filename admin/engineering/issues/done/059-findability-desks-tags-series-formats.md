---
id: 059
title: Findability: five desks, a controlled vocabulary, series, formats and reading time, derived once
kind: feature
priority: high
created: 2026-10-14T18:10:00Z
source: card 051's order of work ("the data first: desks, tags, series, formats"), from the Newsroom Design Lab's newsroom-proto-find vault; the owner: "pull the latest articles and just start taking from there"
release: v0.12.52
estimated_effort: medium
---
# Findability: five desks, a controlled vocabulary, series, formats and reading time, derived once

## What is asked
The lab's finding was that 123 articles under six topics and 504 raw tags (most used once) cannot be found by the reader they are for. Its derivation (a desk is an audience; each controlled tag belongs to one desk; an article scores by its tags and topics; the editor overrides and says why) is carried over with its rules intact, run on today's wire, and written once as data every page reads and the API will serve.

## Scenario
```gherkin
Given the wire, every article's markdown twin and the editor's file
When find.py runs
Then every article has a primary desk, a secondary when it touches one, its controlled tags, its series and position, a format and reading minutes
And a raw tag the editor has not mapped is listed for the Librarian and does not stop the build
And each desk has a page: who it is for, three to start with and why, its series in order, every article newest first
```

## Outcome
`admin/content/find/find-editorial.json` (ported from the lab, status accepted), `admin/build/find.py` → `articles/find.json` (desks security 35, building 25, vaults 20, news 24, strategy 19; 42 controlled tags from 504 raw, 165 unmapped and listed; 11 series; reading minutes at 230 words a minute from the first h2 to Threads). `admin/build/desks.py` → `desks/index.html` and `desks/<id>.html`. The front page's chips, desk sections and start-here lists read it.
