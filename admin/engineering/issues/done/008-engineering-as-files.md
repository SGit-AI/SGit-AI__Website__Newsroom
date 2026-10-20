---
id: 008
title: Engineering as files: issues, releases, and the pages that render them
kind: task
priority: high
created: 2026-10-12T15:20:00Z
source: the owner's first run of v0.12.0 on an iPad, 12 October 2026: three screenshots and a note kept in the pane, relayed in chat
release: v0.12.1
estimated_effort: medium
---
# Engineering as files: issues, releases, and the pages that render them
## What is asked
The owner: a dev section where everything said in feedback is reverse-engineered into user stories and bugs, with mock-ups, Gherkin and screenshots when done; releases that list their issues; and the tracking as issues-fs, files in the repository, so every change to the site is connected to an issue and a version row can say which ids it answers.

## Scenario
```gherkin
Given a card in admin/engineering/issues/open/
When the site is built
Then /engineering/ lists it under Open with its id, kind, priority and release
And /engineering/issues/NNN.html renders its body, Gherkin and all
When the card is moved to done/ with an Outcome appended
Then it is listed under Done, and the release page that names it links to it
And the version row names the ids
```

## Outcome
Shipped in v0.12.1: admin/engineering/ (the files, in the Issues-FS-lite layout: open, blocked, done; releases), admin/build/engineering.py and md.py (the renderer), /engineering/ (the board, one page per issue, one per release, issues.json as a derived index), a link in the About menu. The sgit.ai board's own convention is the model; the full issues-fs CLI is not installable here, so the lite protocol is used as written.
