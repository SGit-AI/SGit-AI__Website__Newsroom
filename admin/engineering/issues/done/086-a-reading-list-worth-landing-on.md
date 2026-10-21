---
id: 086
title: A reading list worth landing on: wide, visual, five views, and what was read
kind: story
priority: high
created: 2026-10-18T17:00:00Z
source: Dinis, in chat, 18 October 2026, with two screenshots (an email to Adam with a reading list, and the list it opens): "we really need to make this very visual ... very graphy ... very friendly. At the moment, it's just a massive list of links ... we now have the ability to track every single thing that the person has read, that the person has said okay, that they don't want to read ... we should be showing that here too ... a view here that just shows the headlines, because you now have a one-liner ... a view that just shows the infographics. Um, and then the graph view ... you can go wider ... assume they'll have a normal desktop ... this is now the front page for a lot of people ... maybe on the right ... a bunch of links that explain a bit more what's going on. It's maybe a little animation or maybe a little infographic"
release: v0.13.19
estimated_effort: medium
---
# A reading list worth landing on: wide, visual, five views, and what was read

## What is asked
The reading list at /for/ is now the first page of the newsroom for many people: it arrives in an email. It was a narrow column of links. Make it visual, use the width of a desktop, show what the reader has read, done or set aside, give it views (headlines, pictures, graph), and say on the page what the reader is looking at.

## Scenario
```gherkin
Given a reader opens a list from an email on a desktop
Then the list uses the width of the window, with a side column that says what this is and how it works
And they can see it as Cards, Headlines, Sections, Pictures or Graph, and the choice is remembered

Given the reader has read the first article on the list
When they come back to the list, or it is open in another tab while they read
Then the first card says Read, its section bar is full, the progress ring counts it
And Continue goes to the first section they have not read

Given the reader taps Not for me on an article
Then it is kept as a note on that article, the same note the vault pane keeps, and the card is set aside
And a second tap takes it back
```

## Mock-up
Hero: "A reading list / For Adam, from Dinis", the note, Continue and Reply, a ring with the share read, articles, read, time left and spent, and the list as numbered dots in order, each filled as read. Below, a bar of views and a filter (All, Still to read, Read). Right: What am I looking at?, the newsroom in four steps lit in turn, the list as a persona, links.

## Outcome
Shipped in v0.13.19. `for/list-views.js` draws the list (loaded by `openList` in `for/reading-list.js`); `renderList` stays for the preview on the make page. Data per article: `articles/summaries/<slug>.json`, `articles/graphs/<slug>.json`, `articles/cards/<slug>.webp`. Reading from `sgit.reading.v1`, `sgit.meter.v1` and `sgit.notes.v1`, redrawn on the storage event and when the tab returns. Styles in `for/for.css`, theme tokens only. Twelve new checks in `admin/build/test_lists.mjs`. Then reviewed by the Designer role on 21 October and fourteen findings fixed (`admin/notes/2026-10-21__the-reading-list-design-review.md`). Left: a view chosen by the sender in the link; the list's own picture for the email (a card made from the list); the graph's ideas as links to the article's graph.
