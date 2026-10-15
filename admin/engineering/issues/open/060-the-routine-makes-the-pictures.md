---
id: 060
title: The morning routine makes the pictures: the key in the environment's secrets, the step in the run, the caps
kind: story
priority: high
created: 2026-10-14T22:30:00Z
source: card 056's outcome; the owner's voice memo of 13 October 2026 ("capture how much it costs and add to the thing")
release: null
estimated_effort: small
blocked_on: the owner putting OPENROUTER_API_KEY in the secrets of the environment the routine runs in (never in a file, never in the prompt), and allowing the sgit clone and the pip install in the scheduled tasks' settings (the first unattended runs of 14 October stopped at both)
---
# The morning routine makes the pictures: the key in the environment's secrets, the step in the run, the caps
## Scenario
```gherkin
Given OPENROUTER_API_KEY in the environment the routine runs in
When a desk has published and the routine has refreshed the wire's snapshot
Then the routine runs the pipeline for that wire with the documented caps (forty images, two dollars), commits the images and the ledgers with the release, and says in its report what the pictures cost
And a wire whose edition did not change makes nothing
And the routine's prompt names the step, the caps and where the key comes from, and never the key
```

## Outcome
The step is in the routine's prompt since 14 October (the newsroom's morning run, 06:56 London). It makes nothing until the key is in the environment: without it the pipeline runs dry and says so.
