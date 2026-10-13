---
id: 030
title: The wire's desk reads the reader's decisions: Not for me and Should reach me reach the join
kind: story
priority: high
created: 2026-10-13T09:40:00Z
source: the owner, in chat, 13 October 2026: the wire read as an inbox; flag stories read, to do, done, follow up; update the wire's vault with a description of what changed, as a release; see the new stuff, for me and not for me; local first, an explicit push to the vault, and knowing what would be lost without it
release: 
estimated_effort: medium
---
# The wire's desk reads the reader's decisions: Not for me and Should reach me reach the join
## What is asked
The point of Not for me and Should reach me is that the join learns from them. Today they reach the desk only if the reader sends them down their lane and the wire's agent reads it with the lane's read key. The wire's own morning read writes to `feedback/<date>.jsonl` in its vault, which a reader with only a read key cannot do.

## Scenario
```gherkin
Given I have decided about stories on the wire and sent my notes
When the wire's agent runs its weekly pass
Then it reads my lane with the read key it was given, takes the wire decisions (path /wire/, story id, kind)
And proposes edits to the personas from them, as a diff for approval
```

## Seen on the first release, 13 October 2026
The desk's first release note (`2026-10-13.1`) and the personal brief both say: "Your lane was not read, so your five wire decisions are not reflected yet." The runbook's step 1 now reads the lane when the agent has been given its read key; it has not been given one. What is missing is the handover, not the code: the lane's read key reaches the wire's agent through the owner, as the brief's message to the agent says.
