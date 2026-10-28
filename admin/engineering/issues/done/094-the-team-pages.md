---
id: 094
title: The team: a roster, and a page, a role and a policy for every member; @newsroom.reviews first
kind: story
priority: high
created: 2026-10-28T01:30:00Z
source: Dinis, 28 October 2026: moving the review work into a session of its own, "a new agent called reviews", "is there a page that we use for all roles?", then, after a look at how the PHP story site organises its agents (a team page, a page per member, roles, every member's policy, rounds, guidance): "agreed and yes please start with those pages and then map the entire team".
release: pending
estimated_effort: large
---
# The team: a roster, and a page, a role and a policy for every member; @newsroom.reviews first

## What is asked
1. The pages for the new agent, @newsroom.reviews: its role, its policy, its handover.
2. Then the whole team mapped the same way: one place that lists every member, and a page each.

## Scenario
```gherkin
Given the roster admin/content/team.json and, for each member, a ROLE.md and a policy.json
When the site is built
Then /team/ lists every member by group, with its status and what it does
And each member has a page with its role, its rules, what it writes and what it may and may not hold
And the build fails if a tracked file is claimed by two members' policies

Given a new agent
Then it is a row in the roster, a role file and a policy; the pages, counts and checks follow
```

## Outcome
Shipped in the release this card names. `admin/content/team.json` (15 members in five groups: the editor; writing; building the site; the wires and their cost; independent review) and `admin/content/agents/<id>/` for each: `ROLE.md` (what it is, when it has failed, its rules, what it does not do, how it runs, where its work is), `policy.json` (the files it alone writes, less exceptions; what it appends to; the vaults and keys it may and never holds; a draft until the editor agrees it) and, for the two review agents, `HANDOVER.md`. `admin/build/team.py` draws `team/` (the roster, a page and a markdown twin per member, `policies.json`) and checks every file against every policy: 0 claimed twice, 0 of the source files unowned. Members: the editor; @newsroom.writer, @newsletter; @newsroom.dev, .ux, .vault, .conductor (planned, specified on 14 October, never started); @newsroom.wire, the wire desks, @newsroom.accountant; @newsroom.reviews (starting), @newsroom.security (planned), and the independent reviewers openai-chatgpt, perplexity and anthropic-fable. The PHP story site's team and the original six desk roles are linked as other teams. In the menu under How it runs, and from each agent's page and the review section. The review desk of cards 091 and 092 is now @newsroom.reviews. Also fixed: the security scan read "SG/Send access token" as a request to send a token. Test: `admin/build/test_team.mjs`. Left: the editor agrees (or corrects) each policy; the rounds (each agent's dated debrief) and a guidance page for agents, which the PHP team has and this site does not.
