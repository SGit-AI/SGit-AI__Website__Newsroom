---
id: 083
title: A line and a paragraph for every section of every article
kind: feature
priority: high
created: 2026-10-17T10:00:00Z
source: the owner, in chat, 17 October 2026: "Charge based on what you read, not based on what you scroll ... allow me to reset the timers ... allow the user to pause it ... add a visual clue for what's been marked as read ... 3 or 4 variations or 5 ... hide it completely ... show just like a line of it ... show a small paragraph ... every paragraph that you already captured, you need to have that one-liner ... needs to have a paragraph and needs to have the whole content"
release: v0.12.99
estimated_effort: large
---
# A line and a paragraph for every section of every article

## What is asked
"Every paragraph that you already captured, you need to have that one-liner ... a paragraph and the whole content", made every time an article is made.

## Outcome
`admin/build/summaries.py` reads each article's sections as the strip does and builds `articles/summaries/<slug>.json` from `admin/content/articles/summaries/<slug>.json`; a section without a written summary gets an extract; each written summary carries a hash of its section and is marked stale when the section changes; `--dump`, `--stamp`, `--check`. Every section of all 174 articles has a written line and paragraph, by fourteen agents of this session, checked by script. The authoring guide (`admin/content/articles/README.md`) asks for the file with every new article.
