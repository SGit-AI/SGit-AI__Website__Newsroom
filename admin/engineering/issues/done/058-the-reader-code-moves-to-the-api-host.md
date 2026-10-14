---
id: 058
title: The reader code moves to api.newsroom.sgit.ai, the same bytes, proved by hash
kind: task
priority: high
created: 2026-10-13T11:40:00Z
source: the brief in Go slow to go fast (11 October) and its refresh in SGit-AI__Website__Newsroom__API/briefs/ (13 October); Dinis's decisions on the repository's name and the host, 13 October
release: v0.13.0
estimated_effort: large
---
# The reader code moves to api.newsroom.sgit.ai, the same bytes, proved by hash
## What is asked
Phase 1 of the move: every file the reader's browser runs leaves this repository for SGit-AI__Website__Newsroom__API, unchanged, and is served from api.newsroom.sgit.ai at a pinned, versioned path that this site and sgit.ai load. The content stays. The proof is a hash, not a diff.

## Scenario
```gherkin
Given a page of this site at v0.12.50 and the same page at v0.13.0
When both are normalised (the chrome, the version stamps, and a reader-file reference read as API/<path>)
Then they hash the same
And every reader file on the API host hashes as the file did here, apart from the three the host forced to change
And a reader who opens the site keeps their balance, personas, notes and lists
And no page loads a reader file by a relative path, from another release, or from outside the pinned manifest
```

## Outcome
Shipped in v0.13.0. 74 files moved (`tools/served.json` in the API repository); releases v0.1.0 (from v0.12.10) and v0.2.0 (from v0.12.50, the one this site pins) cut there with a manifest; `admin/build/api.py`, `api.json` and `api-manifest.json` here; checks 13 and 14 in the gate; the sync's items 11 and 14; the proof in the API repository's `map/proof/`. Left for later phases: sgit.ai pins the release (then the sync's rule 11 is deleted); the frozen meter copies leave this repository in phase 4; the map (`newsroom-api/`) is frozen at v0.12.10 as the before and is regenerated in the API repository from now on.
