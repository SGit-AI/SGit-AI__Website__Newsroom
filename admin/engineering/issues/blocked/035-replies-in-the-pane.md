---
id: 035
title: Replies: the newsroom answers a message where it was written
kind: story
priority: medium
created: 2026-10-13T11:00:00Z
source: the owner, in chat, 13 October 2026, after the first send: "is this a new vault for us to communicate?"
release: none yet
estimated_effort: medium
blocked_by: the newsroom needs an access key of its own to create and write a vault (as card 010)
---
# Replies: the newsroom answers a message where it was written
## What is asked
The lane carries notes one way: from the reader to the newsroom, which reads it with the published read key and cannot write to it. Answers come back in chat today. The owner asked whether the lane is a channel between them and the newsroom's agent; in one direction it is.

## Scenario
```gherkin
Given I sent a message through my lane
When the newsroom's agent answers it
Then the answer is written to a reply vault that the newsroom holds the write key of
And my pane reads it with a read key kept in my master vault
And the answer is shown under my message, in This page and in All your notes, with the time it was written
```

## Blocked by
A vault the newsroom writes to needs an access key on the newsroom's side; none is held here (card 010 is blocked on the same key). The key would live in the session's environment, never in this repository.
