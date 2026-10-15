---
id: 061
title: The accountant: what every run cost, per wire, edition, month, model and image, and per piece of work, on one page
kind: story
priority: high
created: 2026-10-14T22:40:00Z
source: the owner, 14 October 2026: "really capture in an accountant agent... the cost of all these runs and the cost per edition and the cost per work... and provide visibility on this"
release: v0.12.59
estimated_effort: small
---
# The accountant: what every run cost, per wire, edition, month, model and image, and per piece of work, on one page
## Scenario
```gherkin
Given the ledgers the pipeline writes beside the pictures, with OpenRouter's own cost per image
When the site is released
Then wire/costs.html and wire/costs.json carry every image's cost summed by wire, by edition, by month, by model and by kind
And what a hero costs, what a card costs, what an edition costs and the seconds per image are on the page as tiles
And the key's own budget, as OpenRouter last reported it to a run (the limit, what is spent, what is left; never the key), is shown
And every wire page's strip links the page as "What it costs"
And the page says what is not counted: the desks' own runs and this site's sessions
```

## Outcome
Shipped in v0.12.59: `admin/build/accountant.py` (called by `wire.py` at every release; the role is @newsroom.accountant, a role of the morning routine that writes nothing of its own and spends nothing), `wire/costs.html`, `wire/costs.json` (`wire-costs/v1`); `infographics.py` records the key's budget in the cumulative ledger after each live run. Checked in `test_wire.mjs`: the page's total is the sum of every ledger, and no key is on it.
