---
id: 034
title: Write to the newsroom: a message box that says what it is, and Save and send
kind: bug
priority: high
created: 2026-10-13T11:00:00Z
source: the owner, in the lane (note n-8a168aae, 13 October 2026, on the wire): "where do I add a specific comment to the newsroom agent", and "Keep these words" is a weird button description
release: v0.12.8
estimated_effort: small
---
# Write to the newsroom: a message box that says what it is, and Save and send
## What happens
The first notes sent through the lane arrived whole: five decisions on wire stories, one Done on article No. 10, and one note with words. The note was a question: where to write to the newsroom's agent. The text box under the one-tap buttons had no heading, a placeholder that read as optional ("Words, if you want"), and a button, *Keep these words*, that said what happens in this browser and not where the words go. Sending was a second step, further down, under *All your notes*.

## Scenario
```gherkin
Given I open the vault pane on any page
Then under the one-tap buttons there is a box headed "Write to the newsroom"
And it says the message goes to the newsroom's agent, with the page's address and anything I selected
When I write a message and press "Save and send"
Then it is kept in this browser and sent to my lane in the same press
And "Save, send later" keeps it for the next send
And the newsroom's digest of the lane lists messages first, before the decisions
```

## Outcome
Shipped in v0.12.8. A note with words alone is labelled *Message*. `admin/build/lane.py` names the newer kinds (Done, Follow up), gives each wire story its headline, and prints the messages first. The first lane read is answered in chat; a way for the newsroom to answer in the pane is card 035.

## Screenshots
![The pane on the wire: the one-tap chips, then Write to the newsroom with Save and send](../shots/034-write-to-the-newsroom.png)
