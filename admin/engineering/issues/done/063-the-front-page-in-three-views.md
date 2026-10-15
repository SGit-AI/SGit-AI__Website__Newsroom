---
id: 063
title: The front page in three views, this site's own
kind: feature
priority: high
created: 2026-10-14T18:00:00Z
source: the owner, in chat, 14 October 2026: "I really like those designs... we need to A/B test them... present multiple views so that they show quite nicely. And I quite like that the first one looks like a broadsheet... make it big and visible that we now have a user area... the little progress bar of what's been read... and also the spend... pull the latest articles and just start taking from there"
release: v0.12.60
estimated_effort: large
---
# The front page in three views, this site's own

## What is asked
The Newsroom Design Lab's three directions (A Broadsheet, B Briefing, C Your desk), reviewed in card 051, go live as the front page, all three, so readers can be sent to one and the views compared. The front page stops being the copy of sgit.ai's `articles/index.html` written to the root and becomes a page this repository writes from its own data. The reader's own area is big and visible on every view: what they read, what it cost, their board, with a progress bar, from the records the meter and the pane already keep in the browser, whether or not a vault holds them.

## Scenario
```gherkin
Given a reader who has never been here
When they open the front page
Then they see the Broadsheet: the masthead, one lead, the latest, the doors, the five desks, collections, the newsletter, start here
And the switcher offers Briefing and Your desk, and the glance beside it says 0 read, nothing spent, the credit left
When they pick Your desk
Then the page shows their picks with a status each, the progress bar, the You card and the board
And the choice is remembered in this browser, and ?view= in a link opens a view directly
Given the reader read one pick to the end and marked another read later in the pane
When they return
Then the first is Done, the second Follow-up, the bar has moved, the board counts agree, the glance says the same
Given a reader without JavaScript
Then the Broadsheet shows, the switcher does not, and nothing is missing
```

## Outcome
`admin/build/front.py` writes `index.html` (three `<section class="view" data-view>` in one page; `assets/front/front.css` shows the one `data-view` on `<html>` names, Broadsheet when none), `index.md`, `about/index.html` and `articles/front.json`. `assets/front/front.js`, a classic script in `<head>`, sets the view before paint (`newsroom.view`; `?view=` wins and is remembered), runs the switcher as a radio group, and fills Your desk and the glance from the meter's state (`sgit.meter.v1`) and the pane's notes (`sgit.notes.v1`): balance, spend, reads, notes, a status per pick (Done at depth 0.9 or a done decision; Follow-up from a read-later or follow-up decision; Reading when opened), the progress bar, the board; the chooser changes the meter's active persona through the meter's own module. The lead is the newest article unless the editor names one in `admin/content/front/front.json`. The sync no longer writes the root; `articles/index.html` stays as Every article. Test: `admin/build/test_front.mjs` (46 checks, in CI).
