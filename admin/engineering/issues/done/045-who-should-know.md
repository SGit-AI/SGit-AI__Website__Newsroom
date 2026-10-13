---
id: 045
title: Who should know: a reach page per wire, by organisation route only
kind: story
priority: normal
created: 2026-10-13T15:10:00Z
source: the owner's voice memo of 13 October 2026: find contacts to reach out and tell them about it, a public page of people or organisations that should be made aware, so the outreach can be verified
release: v0.12.20
estimated_effort: medium
---
# Who should know: a reach page per wire, by organisation route only
## What is asked
A public page per wire of who its stories concern and how to reach them, for the owner's team to tell them the wire exists. Public, so the outreach can be checked; under the contact rules this site already publishes (world-news-day): organisations, not people; a role address from the organisation's own contact page, one hop, hashed; a failure is a result.

## Scenario
```gherkin
Given a wire
When I open its reach page
Then I see the routes this site found on the organisations' own contact pages, each with the page, the date, the hash and the role addresses the page publishes
And what the vault carries: data/contacts.json when the desk adds it, the map's entities with their pages and repositories, the sources' sites
And no personal address anywhere
```

## Outcome
Shipped in v0.12.20: `admin/build/wire-reach.json` records the routes found on 13 October (the OWASP Foundation's support and events addresses from owasp.org/contact, the board page which publishes none, AWS's security address from its vulnerability-reporting page); `wire/<slug>/reach.html` draws them with the vault's own. The Industry Wire's sources have no fetched route yet; the brief asks the desks for `data/contacts.json`. Checked in `test_wire.mjs`: every recorded address is a role address and none appears elsewhere.
