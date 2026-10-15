---
id: 061
title: The reading strip: how far, what this page cost, what is left
kind: feature
priority: normal
created: 2026-10-14T18:30:00Z
source: the owner, in chat, 14 October 2026: "I really like that one... the little progress bar of what's been read... and also the spend"
release: v0.12.52
estimated_effort: small
---
# The reading strip: how far, what this page cost, what is left

## Scenario
```gherkin
Given an article page, which the meter charges for
When the reader scrolls
Then a hairline across the top of the viewport fills with how far they are
And a chip, bottom right, says the percentage, what this page has cost and the balance left, and opens the account
Given a page this site writes and declares free
Then there is no strip
```

## Outcome
`assets/reader/strip.css` and `strip.js`, injected by `chrome.py` inside the nav block of every page with the meter (so the imported pages stay unedited for check 11), running only where `<sg-meter view="page">` has a charged kind. Reads the meter's records; refreshes on its events; charges nothing. Tokens only; in the themes gate.
