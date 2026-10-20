---
id: 072
title: Two wires about people: the Dinis Cruz Wire, and the rUv Wire once its desk is allowed to run
kind: story
priority: high
created: 2026-10-16T12:20:00Z
source: the owner, 16 October 2026: "two more wires... mappings for individuals that have a high throughput... the first one is actually me... the other one... Ruben, R-U-V, from the Agentics Foundation... ruv.sgit.ai"
release: null
estimated_effort: medium
blocked_on: the rUv Wire's desk task, which this session's permission check refused to create (a scheduled run following a named person who has not agreed); the owner decides, and records rUv's answer in the vault's README
---
# Two wires about people: the Dinis Cruz Wire, and the rUv Wire once its desk is allowed to run
## Scenario
```gherkin
Given a vault per person (j008k1ti for Dinis Cruz, u10tbqpc for rUv) with a brief and the rules for a wire about a person
When the desk publishes its first edition (the last 30 days of the person's public work)
Then the site adds the wire with its read key under the same contract, at wire/dinis/ and wire/ruv/
And the charter's rules for a wire about a person hold: works, not life; primary first; no scraping behind logins; corrections and stopping; agreement recorded
```

## Progress, 16 October 2026
The Dinis Cruz Wire's first run (fired 12:08 UTC, Sonnet, $0.18) published nothing: every web fetch (the desk brief, the charter, his GitHub page) waited for an approval no one was there to give, so the desk rightly refused to publish a first edition from search results alone; its second turn then hit the account's five-hour session limit. It had cloned its vault and the Industry Wire's pipeline, ready to adapt. The desk tasks that run unattended were made in the app with web fetches judged automatically; a task created from this session is not, so its fetches wait. The fix is the owner's: recreate the Dinis Cruz Wire's task from the routines page with the same prompt, or allow web fetches for it.

