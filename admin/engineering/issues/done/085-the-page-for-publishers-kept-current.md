---
id: 085
title: The page for publishers, kept current, with a version history of its own
kind: story
priority: high
created: 2026-10-18T16:00:00Z
source: Dinis, in chat, 18 October 2026, to @newsroom.dev: "can you look at this brief (a-section-for-publishers) ... and implement that brief ... I want to start emailing publishers and /publishers/ is quite out of date (given the latest major features we have added to this site, and publisher's related articles) ... can you also add a specific version (i.e. just for the publishers) page, so that we can track its changes over time, and what has been changing with that page"; the article A section for publishers, "What this does not claim": "The publishers page itself is unchanged. It is imported from sgit.ai"
release: v0.12.113
estimated_effort: medium
---
# The page for publishers, kept current, with a version history of its own

## What is asked
1. /publishers/ is the page Dinis will send to publishers. It was written once on sgit.ai on 11 October and imported unchanged; a week of the newsroom's most important features for a publisher is missing from it. Bring it up to date.
2. Keep it up to date without anyone remembering to: the parts that go stale (what is live, the newest pieces, the five to start with) come from the data the publishers' section already uses.
3. A version history for the page alone: every version of its text kept, what changed between them, and what changed in its live parts, release by release.

## Scenario
```gherkin
Given the features register gains an entry for publishers in a release
When the release is built
Then /publishers/ lists it in What is live today, with when it shipped
And publishers/changes.json and the versions page record that release as adding it

Given someone edits admin/content/publishers/page.md
When publishers.py runs and versions.json has no new version for the edit
Then the build stops, names the next version and gives the hash to record

Given a new version of the text is recorded
When the release is built
Then publishers/versions/<version>.md is written once and never rewritten
And the versions page shows what changed from the version before, block by block and word by word
```

## Mock-up
The page as before, in the newsroom's look, with a status line under the first paragraph: "This page: v2.0.0, 18 Oct 2026, every version and what changed. Built with newsroom.sgit.ai v0.12.113: 193 articles, 20 features a publisher can use today." The versions page: a table of versions (date, release, words, changes), each change as the blocks that changed with deletions struck and additions underlined, and a list of releases in which the live parts changed.

## Outcome
Shipped in v0.12.113. `publishers/` is no longer imported (`sync_newsroom.py`: out of `MOVED_DIRS`, links to it from imported pages stay local through `OWNED_HERE`; its six files out of the sync record). `admin/build/publishers.py` builds `publishers/index.html` and `index.md` from `admin/content/publishers/page.md` and the site's data; `admin/build/page_versions.py` is the version history, written for any page: `admin/content/publishers/versions.json`, `publishers/versions/v1.0.0.md` (the 11 October text, frozen from the imported twin) and `v2.0.0.md`, `publishers/changes.json`, `publishers/versions/index.html`. Five features added to the register (Ask the site, Who is speaking, Sections by audience, The briefs, A version history for a page). Left: a version history for the other pages this site writes (the section, the front page's words) by the same module; screenshots of the page's features as they are now.
