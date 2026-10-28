---
id: 095
title: The front page by day and by section: the lead and five with images, the last five days in full, eight topic sections with every article in one
kind: story
priority: high
created: 2026-10-28T12:00:00Z
source: Dinis, in chat, 28 October 2026: "we're publishing quite a lot of articles every day … have a section where you list per day, so you have the last 5 days … and then maybe go per section … in terms of the topic … I don't think you should have the article in more than one section"; approving the brief: "those sections are good. 5 days is fine … PHP shell should be a section … one big headline and maybe five, all with images … and then as you go down, then the text based that you have there now"
release: v999.0.0
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
Shipped in v999.0.0 (stamped by CI). The Broadsheet is rebuilt from the top: a compact masthead with the eight sections as jump links; the lead with its card image beside the running-story box (`developing.json`); five more with images (the editor's `highlights`, else the five newest after the lead); the last five publishing days, every article under its day with its section, a subtitle cut at a word, and on a phone a subtitle only under the newest day; eight section cards (five newest, the count, "All N") and a page per section at `sections/<id>/index.html` with its `.md` twin, by month. Below, as before: the newsletter and Start here, Collections, Who are you reading as?, From the agents, and a foot line to every article, the desks and the archive. The five desks band left the Broadsheet; the desk pages stay.

`front.py` stops the build, naming the slug, for an article with no row in `admin/content/front/sections.json`, a row naming an undefined section, or a row for no article. The two articles published after the brief was approved (`a-payout-for-every-row`, `who-carries-the-risk`) were placed in Agent security & behaviour policies, so the build passes; the writer adds the row in the commit that publishes an article from now on. The Briefing and Your desk are unchanged (four highlights). Section colours are inline custom properties from `sections.json`, and text in them is mixed toward the ink so it holds 4.5:1 in all five themes; the stylesheet still names no colour. Tests in `test_front.mjs`: the last five days appear once each, five more with images, the eight cards with their five newest, the pages and twins, the failing build, 390 px with no sideways scroll and subtitles only on the newest day, the jump links landing, and the section colours' contrast in five themes. Not done, as the brief says: feeds per section, and refreshing Collections and From the agents.
