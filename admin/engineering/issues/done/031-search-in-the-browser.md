---
id: 031
title: Search in the browser: an index built at release, ranked in the page
kind: story
priority: high
created: 2026-10-13T10:30:00Z
source: the owner, in chat, 13 October 2026: a client-side search engine, built from the graphs, sections and summaries the site already has; the question just asked about an article should be findable from the website; then a local model, or the reader's OpenRouter key, to talk to the site
release: v0.12.7
estimated_effort: medium
---
# Search in the browser: an index built at release, ranked in the page
## What is asked
A search engine for the site that runs in the reader's browser, built from what the site already publishes: the article graphs, the sections, the summaries and the text. The test the owner gave: the question asked about an article should be found from the website.

## Scenario
```gherkin
Given the site is released
Then search/docs.json and search/text.json hold every page in the sitemap, the wire's snapshot and the site's notes
And every article's entry has its number, date, teaser, topics, tags, graph labels and headings with anchors
And the paragraphs of earlier versions that are no longer in an article are indexed with their version

When I open /search/ and type words
Then results come as I type, ranked titles and tags first, each with its kind, number, date, section and a snippet with the words marked
When I type "a phrase in quotes"
Then only pages with that exact phrase are listed
When the phrase is only in an earlier version of an article
Then the article is listed, the snippet says which version, and the link opens the version page that shows the change
When I type a number alone
Then that article is the result
When I choose Articles, The wire, Engineering, Pages or Archive
Then only that kind of page is listed, and each filter shows its count
Given I have read a result, or marked it done
Then the result says so, and I can hide what I marked done
And nothing I type is sent anywhere: the page fetches two files from this site
```

## Mock-up
```
[ "I have not stopped thinking about"              ] [Search]
[Everything (2)] [Articles (1)] [The wire (0)] [Engineering (1)] [Pages (0)] [Archive (0)]   [ ] Hide what I marked done
375 pages and 5,645 paragraphs, release v0.12.7, indexed in this browser in 310 ms. Nothing you type leaves this page.
ARTICLE · No. 97 · 2026-10-12 · The question                                   Read · you read it all
Who owns the words: agents can make decisions, but they cannot hold responsibility
In v1.0.0, since changed: … with a digression [I have not stopped thinking about]. Paraphrasing: …
```

## Outcome
Shipped in v0.12.7: admin/build/search_index.py, assets/search/search.js and search.css, /search/, a Search link in the nav of every page. The design is [search in the browser](../../admin/notes/2026-10-13__search-in-the-browser.md). Checked by test_search.mjs: the ranking in Node against the built index (the owner's examples among them), and the page in Chromium.

## Screenshots
![A phrase since corrected, found in v1.0.0 and marked as one](../shots/031-phrase.png)
![Results for one word, with the filters and their counts](../shots/031-results.png)
