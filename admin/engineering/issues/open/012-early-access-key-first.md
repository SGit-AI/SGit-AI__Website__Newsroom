---
id: 012
title: The early-access key first, checked against the server, before a passkey or a vault is made
kind: story
priority: high
created: 2026-10-12T15:20:00Z
source: the owner's first run of v0.12.0 on an iPad, 12 October 2026: three screenshots and a note kept in the pane, relayed in chat
release: v0.12.2
estimated_effort: medium
---
# The early-access key first, checked against the server, before a passkey or a vault is made
## What is asked
The owner: use the access key as an early-access token; "you should not even attempt to create a vault or even attempt to create a passkey until you have been given a valid [key], which you should also be able to check"; the key should be easy to enter, once.

## Scenario
```gherkin
Given I open the Vault tab for the first time on a device with no account
Then the first thing asked is the early-access key, with a Check button
When I paste it and press Check
Then the pane asks the vault server with it, without creating anything, and says valid or not
And only then are Make a passkey and Create the account offered

Given the key is invalid
Then nothing else is offered, and the pane says where a key comes from
```

## How to check a key without side effects
POST /api/vault/append/configure/{any vault id} with the key and a wrong write key: the server answers 401 to a bad or missing key and 404 to a good one (https://sgit.ai/api/append-lanes.html, checked 12 October against dev.send.sgraph.ai). The server also has GET /api/transfers/check-token/{token}, which answers {valid, status, remaining}; whether it takes an access key is not yet known.

## On the question of hiding the key on the page
A hash of the key on the page cannot be used to open anything, so it cannot replace typing the key; the key itself is the credential the server checks. A hash would only let the page say "that is not the key" before asking the server, and a published hash of a short key invites guessing. The early-access flow above is the answer: the key is typed once and kept in the master.
