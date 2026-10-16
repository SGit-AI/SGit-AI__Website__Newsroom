---
id: 074
title: Highlights: select, tap, kept in the browser, drawn without changing the page
kind: feature
priority: high
created: 2026-10-16T09:10:00Z
source: the owner, in chat, 16 October 2026: "on the bottom little pane that you added... you shouldn't show the total... It flickers... the percentage that you scroll and the percentage that you read... think of the page as a graph... which articles I read, which I don't read, which articles I highlight... a separate section for articles that are written by agents"
release: v0.12.85
estimated_effort: small
---
# Highlights

## What is asked
"The highlighting is very important. It's very intuitive." Until now a selection could only be kept as a quote inside a pane note, in four steps, and nothing marked the page.

## Scenario
```gherkin
Given a passage selected in an article
Then a Highlight button appears beside it
When the reader taps it
Then the passage is marked and kept in this browser, with its section
And it is still marked after a reload
When the reader taps the marked passage
Then Remove highlight takes it out
```

## Outcome
`assets/reader/highlights.js`: kept under `sgit.highlights.v1` as the exact words, 32 characters either side and the section (the W3C Web Annotation text quote selector), anchored by quote so it survives edits elsewhere; drawn with the CSS Custom Highlight API (`::highlight(sgit-highlight)`), so the imported article is unchanged; the button follows its passage as the page scrolls. Counted per section in the reading map. Not yet carried to the vault (card 076, step 1). Test: `admin/build/test_reading.mjs`.
