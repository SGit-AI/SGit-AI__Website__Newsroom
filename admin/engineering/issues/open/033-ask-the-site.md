---
id: 033
title: Ask the site: Chrome's built-in model, or the reader's OpenRouter key, answering from the search index
kind: story
priority: high
created: 2026-10-13T10:30:00Z
source: the owner, in chat, 13 October 2026: a client-side search engine, built from the graphs, sections and summaries the site already has; the question just asked about an article should be findable from the website; then a local model, or the reader's OpenRouter key, to talk to the site
release: v0.12.9
estimated_effort: large
---
# Ask the site: Chrome's built-in model, or the reader's OpenRouter key, answering from the search index
## What is asked
The owner: the next step is a model that talks to the site and its articles, with the reader's OpenRouter key or a local model, now that Chrome's built-in model runs in the browser.

## Scenario
```gherkin
Given I ask a question on the search page
Then the question is searched, and the top passages are given to a model with the instruction to answer only from them and to cite them by number
And the answer is shown with the passages beside it, each linked to its page and section

Given my browser has Chrome's built-in model
Then it is used, on my machine, with no key and nothing sent

Given it does not, and I paste an OpenRouter key and choose a model
Then the key is kept in this tab unless I ask to keep it, is sent to openrouter.ai only, and the page says so
And the request and the passages sent are shown

Given neither is available
Then the page says so and shows the passages alone
```

## Mock-up
Under the search box, a second button, *Ask*; under it the answer, then "From these passages" with the numbered snippets, then "Answered by: Chrome's built-in model" or "by openrouter.ai, model …, with your key". The design is in [search in the browser](../../admin/notes/2026-10-13__search-in-the-browser.md), "Next: asking the site".
