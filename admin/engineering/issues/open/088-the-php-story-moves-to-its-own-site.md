---
id: 088
title: The PHP story moves to its own site: front page, a tracker, a briefing pack, then /php-flaws/ retires into a pointer
kind: story
priority: high
created: 2026-10-22T12:00:00Z
source: Dinis, in chat, 22 October 2026: "once that new site is up (https://php.oct.2026.newsroom.sgit.ai/) we should also put in on our main homepage, and track it's progress from here, can you also create a briefing pack for the other agent (as a zip) that I can share with that team, with the idea is for us to decommision https://newsroom.sgit.ai/php-flaws once the transition has completed"
estimated_effort: medium
---
# The PHP story moves to its own site

## What is asked
php.oct.2026.newsroom.sgit.ai is the story's own site now. Put it on the front page, track its progress from here, give its team a briefing pack, and retire /php-flaws/ once the move is complete.

## Scenario
```gherkin
Given the dedicated site is live
When php-flaws/build/track.py runs
Then php-flaws/data/transition.json holds the site's version, data time, counts and five checks
And the front page shows a Developing story strip in all three views with those numbers
And /php-flaws/ shows the move and its checks at the top

Given checks 1 to 4 pass (live, /status.json, every source, front page)
When Dinis confirms
Then /php-flaws/index.html and sources.html become pointers to the site, at the same addresses
And /php-flaws/data/ stays, frozen and marked superseded
```

## Mock-up
Front page, above the views: a red-ruled strip, "Developing story", the title linked to the site, a two-line dek, "site v0.2.2 · 144 sources captured · data as of ...", and three links (the site, the article, "Moving from this newsroom: 2 of 5 checks").

## Outcome
v0.13.41: `admin/content/front/developing.json` and `Front.developing()` in `front.py`; `php-flaws/build/track.py` and the panel on `/php-flaws/`; the briefing pack at `briefs/php-oct-2026/` and `briefs/php-oct-2026.zip`. Left: `/status.json` and the 40 recovered sources on the site's side, then the pointer.
