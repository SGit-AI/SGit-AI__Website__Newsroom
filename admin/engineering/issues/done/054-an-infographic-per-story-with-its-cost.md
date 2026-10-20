---
id: 054
title: An infographic per story and per edition, with what each cost, made by the newsroom and never by the desks
kind: story
priority: high
created: 2026-10-13T20:45:00Z
source: the owner's voice memo of 13 October 2026 ("an infographic per news item... that top-level view... capture how much it costs and add to the thing"), the bake-off article's guidance
release: v0.12.42
estimated_effort: large
---
# An infographic per story and per edition, with what each cost, made by the newsroom and never by the desks
## Scenario
```gherkin
Given an edition the desk has just published
When the morning routine runs with the OpenRouter key in its environment
Then it makes one hero for the edition from the editor's note, the lead and the threads, and one card per story the release names as added
And each card carries the headline exactly, the date, the publisher with its tier, at most one number the summary holds, and the beat; the hero is attached to each card as the style reference
And a ledger records, per image, the model asked for and the one that answered, the seconds, the cost from OpenRouter's own accounting, the prompt's hash; and per edition, per wire, per month
And an unchanged story is never redrawn; a corrected one is; the run stops at a count or a cost cap
And without the key the run is dry: the prompts and the plan are written, nothing is sent, the pages are complete without pictures
```

## Outcome
The pipeline is in the tree in v0.12.42: `admin/build/infographics.py` (`--check`, `--wire`, `--from`, `--edition`, `--stories`, `--dry-run`, `--max-images`, `--max-cost`, `--out`), through dev.tools.sgraph.ai by Playwright, the key from `OPENROUTER_API_KEY` only and scrubbed from every message; the tripwire in `validate.js` now also fires on an OpenRouter key. Checked live against the tool (version, health, twelve methods, image input accepted); a dry run on the four wires wrote 166 prompts. Open until the owner hands the key to the routine's environment: the first live edition, the images and the ledger on the pages (card 056).
