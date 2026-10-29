---
id: 087
title: The PHP flaws: a dedicated section and an evidence vault that many agents write to
kind: story
priority: high
created: 2026-10-22T08:00:00Z
source: Dinis, in chat, 22 October 2026, after reading the BBC live page on the PHP flaws: "let's create a dedicated section of this site about this, starting with a dedicated section and a vault to capture evidence, I will provide a voice memo about it in a bit ... start adding to the vault as much sources, screenshots, copies of content and provenance as you can find ... we will have other agents to also work on this"
estimated_effort: large
---
# The PHP flaws: a dedicated section and an evidence vault

## What is asked
A section of the site for a story that is still moving: the critical PHP vulnerabilities disclosed on 22 October 2026. Behind it, a vault that keeps the evidence (sources, screenshots, copies, provenance) and that several agents and the editor can write to at once.

## Scenario
```gherkin
Given an agent holds the evidence vault's key
When it captures a source with tools/capture.mjs and writes its source.json, claims and timeline as its own files
Then no two agents edit the same file, and every capture is dated and hashed and is never edited

Given the editor runs php-flaws/build/build.py --from <clone of the vault>
Then /php-flaws/ shows what is known with a source for each point, what is not known, the timeline and the claims by status
And /php-flaws/sources.html lists every capture with the sha256 of its files
And no captured page, screenshot or text is copied into the site
```

## Mock-up
Crumb, status line (Developing, updated), headline, lead, four counts (sources, captures, claims, events), a caveat box, What we know (each point with its source), What we do not know, the timeline table, the claims table, How the evidence is kept, then the link to the sources page.

## Outcome
First release v0.13.40: the vault (private; its key is held by the agents and the editor, and it is not on this site), its protocol in the vault's README.md, `tools/capture.mjs`, the section builder `php-flaws/build/build.py`, the editor's text in `php-flaws/data/story.json`. Left: the editor's voice memo, to be written into the story; an article; refreshes while the story moves.
