---
id: 028
title: Seen stories carried by the vault, so New is right on every device
kind: story
priority: normal
created: 2026-10-13T09:40:00Z
source: the owner, in chat, 13 October 2026: the wire read as an inbox; flag stories read, to do, done, follow up; update the wire's vault with a description of what changed, as a release; see the new stuff, for me and not for me; local first, an explicit push to the vault, and knowing what would be lost without it
release: v0.12.6
estimated_effort: small
---
# Seen stories carried by the vault, so New is right on every device
## Scenario
```gherkin
Given I saw the wire's stories on one device and updated the vault
When another device brings that device's activity in
Then the stories are recorded as seen there, tagged with the first device
And they are not new when I open the wire on the second device
And the second device's next update does not claim them
```

## Outcome
Shipped in v0.12.6: `wire.seen` in the device file (sync.js extract), the earliest sighting across devices (consolidate), `mergeWire`. Checked by test_sync.mjs and on device B in test_notes.mjs.
