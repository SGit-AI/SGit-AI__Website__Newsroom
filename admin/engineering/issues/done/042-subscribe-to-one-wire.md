---
id: 042
title: Subscribe to one wire alone, down the same lane
kind: story
priority: high
created: 2026-10-13T15:10:00Z
source: the owner's voice memo of 13 October 2026: let people subscribe just to the OWASP one or just to the AWS one; we already have the subscription base, the append lanes
release: v0.12.20
estimated_effort: small
---
# Subscribe to one wire alone, down the same lane
## Scenario
```gherkin
Given I am on a wire's page
When I give my address, tick the consent box and press Subscribe
Then the request is encrypted in my browser to the subscribe agent's key and appended to the subscribe lane
And it carries X-SGit-Form: subscribe and X-SGit-List: wire:<slug>, with the wire's name in the subject
And nothing is stored on this site; if the lane cannot be reached the same request is offered as an email
```

## Outcome
Shipped in v0.12.20: `wire/subscribe.js` (this site's own, the newsletter's envelope and lane, one header more) and the block on every wire's edition page. The brief for the desks tells the lane's agent to keep one list per value. Checked in `test_wire.mjs` with the append intercepted.
