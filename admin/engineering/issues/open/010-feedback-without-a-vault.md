---
id: 010
title: Feedback without a vault: the newsroom's append lane, with a public write token and key on the page, and a typed schema
kind: story
priority: urgent
created: 2026-10-12T15:20:00Z
source: the owner's first run of v0.12.0 on an iPad, 12 October 2026: three screenshots and a note kept in the pane, relayed in chat
release: v0.12.2
estimated_effort: large
---
# Feedback without a vault: the newsroom's append lane, with a public write token and key on the page, and a typed schema
## What is asked
The owner, after a note kept with no vault could not be sent: "these messages should be sent to an append lane … a vault that you have created that you're going to use to receive messages from the site … you put on the web page the public key to write the message and also the ID of the append lane … and you should also push a schema, a strongly typed schema, so you prevent a little bit of injection." The generic feedback "should always be there", with or without a vault.

## How it is done on this site already
The subscribe form writes to sgit.ai's subscribe lane: the contact file /.well-known/sgit-subscribe.json carries the vault id, the lane's append token and the recipient's public key; the browser encrypts a single-part .eml to that key and POSTs it to /api/vault/append/write/{vault}. The append token can only write. The API: https://sgit.ai/api/append-lanes.html; the two-way write-up: https://sgit.ai/docs/append-lane-messaging.html; the message convention: https://sgit.ai/docs/agent-contact.html.

## Scenario
```gherkin
Given I have kept notes and have no vault
When I press Send to the newsroom
Then each note is encrypted in my browser to the newsroom's public key
And written into the newsroom's append lane with the published token
And marked sent, with the lane's id
And the newsroom drains the lane with its own key and reads the notes as the feedback schema

Given the contact file says the lane is closed
Then Send says so and offers the same notes as an email instead

Given a note does not match the schema
Then it is not sent
```

## Mock-up
/.well-known/newsroom-feedback.json: {schema, recipient {address, fingerprint, encrypt}, inbox {vault, endpoint, lane {append_token}, status}}; the message: newsroom-feedback/v1, a JSON document {schema, sent_at, device, persona, notes: [note…]} validated against /.well-known/newsroom-feedback.v1.schema.json before sending and after draining; admin/build/feedback_drain.py: list, fetch, decrypt, validate, mark processed, write the notes into the engineering inbox.

## What it needs
An access key to create the newsroom's inbox vault and configure its lane (the keypair is made with sgit pki keygen and kept, passphrase-encrypted, in the inbox vault itself, as sgit.ai's subscribe vault does). Until the lane is open the contact file says status: closed and Send falls back to an email.
