---
id: 095
title: The front page by day and by section: the lead and five with images, the last five days in full, eight topic sections with every article in one
kind: story
priority: high
created: 2026-10-28T12:00:00Z
source: Dinis, in chat, 28 October 2026: "we're publishing quite a lot of articles every day … have a section where you list per day, so you have the last 5 days … and then maybe go per section … in terms of the topic … I don't think you should have the article in more than one section"; approving the brief: "those sections are good. 5 days is fine … PHP shell should be a section … one big headline and maybe five, all with images … and then as you go down, then the text based that you have there now"
estimated_effort: medium
---
# The front page by day and by section

## What is asked
The Broadsheet view of the front page, rebuilt from the top: a compact masthead with the sections as jump links; the editor's lead, large, with its image, beside the running-story box; five more with their images; the last five publishing days, every article listed under its day; eight topic section cards, each with its five newest and a link to a page per section. The full brief, with mock-ups and the decisions, is `admin/notes/2026-10-28__brief__the-front-page-by-day-and-section.md`. The section of every article is in `admin/content/front/sections.json`.

## Scenario
```gherkin
Given admin/content/front/sections.json assigns every article to exactly one of eight sections
When admin/build/front.py runs
Then the front page shows the lead and five more with their card images
And every article of the last five publishing days appears once, under its day, with its section
And each section card shows its five newest, its count and a link to sections/<id>/
And sections/<id>/index.html lists every article in the section by month
And the build fails, naming the slug, for an article with no section or an unknown one
And a phone at 390 px has no horizontal scroll
```

## Mock-up
In the brief: `admin/notes/2026-10-28__front-page/`.

## Outcome
To be filled by @newsroom.dev when it ships.
