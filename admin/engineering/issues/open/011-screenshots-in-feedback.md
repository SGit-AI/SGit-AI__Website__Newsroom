---
id: 011
title: Screenshots in feedback: paste or pick an image, resized in the browser, sent with the note
kind: story
priority: high
created: 2026-10-12T15:20:00Z
source: the owner's first run of v0.12.0 on an iPad, 12 October 2026: three screenshots and a note kept in the pane, relayed in chat
release: v0.12.2
estimated_effort: medium
---
# Screenshots in feedback: paste or pick an image, resized in the browser, sent with the note
## What is asked
The owner: "it should support screenshots too, as we've done in other places, like copy and paste of screenshots."

## Scenario
```gherkin
Given I am writing a note in the pane
When I paste an image, or pick one
Then it is resized in my browser to at most 1280 pixels wide and kept with the note as webp
And it is shown under the note, and sent with it
And nothing is uploaded anywhere until I send
```

## Mock-up
Under the words field: "Paste a screenshot here, or choose a file"; a thumbnail with a remove cross once there is one. The note record gains `images: [{mime, bytes (base64), w, h}]`; the lane message carries them; the vault file carries them, which is why the resize matters.
