---
id: 050
title: How to write here: the guide beside the article sources
kind: task
priority: normal
created: 2026-10-13T21:30:00Z
source: the owner, in chat on 13 October 2026, "really pay attention to how you're writing articles ... there should be some guidance on how to write in the same voice"
release: v0.12.28
estimated_effort: small
---
# How to write here: the guide beside the article sources
## What is asked
The nine articles written in this repository since v0.12.10 share a voice, a shape and a contract, but the only description of them is spread across sgit.ai's `CONTENT.md`, which has not moved here, the behaviour policy of a session that ends, and the articles that describe themselves. Before the next article is written, write the guidance down, beside the sources, so a new session or a person writes in the same voice without re-reading nine articles.

## Scenario
```gherkin
Given a session that has not written an article here before
When it reads admin/content/articles/README.md
Then it knows the voice (first person, the memo's order, plain words, the moves the argument makes)
And the wording rules, including the two the build refuses
And the shape, part by part, with the anchors the build reads
And how a figure is declared and drawn, and what the graph beside the article holds
And the run from the markdown to a release
And it has a checklist to read the article against before the release

Given publish.py runs
Then the README is not copied to the generator's tree, because publish.py skips a file of that name
```

## Mock-up
One markdown file, `admin/content/articles/README.md`, in the voice it describes: an In short, the two kinds of author, the voice as counted from the nine articles, the seven wording rules and the desk's three, the shape as a skeleton, figures, the graph, before writing, the run, the checklist.

## Outcome
Shipped in v0.12.28. The guide is drawn from the nine articles read in full and counted: words, sentence lengths, links, semicolons, em-dashes (none), spellings, the sections and their sizes, the figure kinds in use, the graphs' node kinds and edge relations. The one banned ladder word is named once, in the guide only, so that a writer knows it; the articles continue to refer to it as the ladder word. The root `README.md` points at the guide from its `admin/content/articles/` line.
