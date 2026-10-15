---
id: 060
title: The masthead: "Pay for what you read."
kind: design
priority: normal
created: 2026-10-14T18:20:00Z
source: the owner, in chat, 14 October 2026: "newsroom.skit.ai doesn't mean anything to anybody... It can be still the domain name... pay for what you read... unless you think pay for what you value is much, much stronger"
release: v0.12.52
estimated_effort: small
---
# The masthead: "Pay for what you read."

## What is asked
The domain is the address, not the name. The masthead names the newsroom and, under it, says in four words what is different about it; the subject line names the subject and the author.

## Decision
`SGit Newsroom`, then **Pay for what you read.**, then "Field notes on AI agents, security and the next generation of publishing, by Dinis Cruz." *Pay for what you value* was weighed and held back: it is what the meter does (the rating sets the price) and can take over once ratings are the visible part of the price. The candidates and the reasons are kept in `admin/content/front/masthead.json`; the domain stays in the bar as the brand link. The heart line is on all three views and in `index.md`.
