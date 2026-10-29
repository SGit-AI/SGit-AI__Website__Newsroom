---
title: Search as navigation: walking the newsroom's graph with no model, and why a clean graph should beat vectors
date: 2026-10-18
author: Dinis Cruz
author_url: about/index.html
summary: This site's search works, but it answers the way every search box does, with a list. We now have far more than text to search with: a graph of the argument for every article, a one-line summary for every section, figures with captions, trails, topics and reviews. So the next version of search should be navigation rather than question and answer. Type Portugal and see not just the articles about Portugal, but the graph around them: their ideas, their sections as one-liners, their images as a collage, the people and things they connect to, and on the side, what the word could mean and which combinations are worth following, each with an exact count. The reader builds the query by walking. All of it deterministic, in the browser, with code and graphs and no model, plus a pane that shows exactly what was fetched, how each result arrived and how long each step took. It also exposes the work: 663 tags on 182 articles, 396 of them used once, and 2,230 ideas in the graphs, of which only 47 appear in more than one article. That is the taxonomy debt, and paying it down is what makes deterministic search good. My hypothesis is that the better the taxonomy, the ontology and the graph, the less a model is needed, and that when one is added, it will do better on a clean graph than on a vector store. This is the brief for the agent that builds it, and the test of that hypothesis.
version: v0.12.107
license: https://creativecommons.org/licenses/by/4.0/
tags: search, graphs, fractal-semantic-graphs, ontology, taxonomy, graph-rag, newsroom, brief, article
status: published
---

!shot sn-explore.webp | images/ | Search as navigation: a query built from chips, five views of the same result, and what was fetched. | concept

## In short {#in-short}

- **Search should be navigation, not a list.** Type a word and walk into the graph around it.
- **We have far more than text.** A graph per article, a one-liner per section, figures, trails, reviews.
- **Suggestions on the side, all exact.** What a word could mean, what sits near it, which combinations to follow.
- **Many views of one result.** The graph, the sections, a collage of the figures, a timeline, the list.
- **A pane that shows the working.** What was fetched, how each result arrived, the time per step.
- **No model in this version.** Code, graphs and two database engines already in the browser.
- **It exposes the taxonomy debt.** 396 of 663 tags used once; 47 of 2,230 ideas shared between articles.
- **The hypothesis:** a clean graph needs less model, and a model does better on it than on vectors.

## What search is today {#today}

[Search in the browser](https://newsroom.sgit.ai/admin/notes/2026-10-13__search-in-the-browser.md) went in on 13 October, and it was built on a good observation: most of a search engine was already published. Every page has clean headings and a markdown twin, every article has a teaser, topics, tags and a graph, and every earlier version is kept. The build writes two files, and the reader's browser ranks them with BM25. Nothing is sent anywhere. It even finds sentences that have since been corrected.

But it answers the way every search box answers: with a list. You type, you get ten results, you open one. Since then the site has grown things a list cannot show. Every article has a graph of its argument, 2,289 nodes and 2,326 edges across 182 graphs. Every section has a one-line summary and a paragraph, 1,995 of them. There are 657 figures with captions, trails that join articles into series, and now [reviews on the record](/articles/reviews-on-the-record.html). A list throws most of that away.

## Search as navigation {#navigation}

What I have in mind is closer to walking than to asking. Say I type *Portugal*. I should see the articles about Portugal, but also the graph around them: the ideas they share, the people and companies they mention, the wire stories, the other articles they link to. I should see their sections as one-liners, so I can tell in a few seconds which part of which article is the one I want. I should see their figures as a collage, because many of these articles have good images, and an image is often how I remember a piece.

And on the side, as I type, the page should tell me what my words could mean. *Portugal* could be the country, the Portugal wire, the tag, or just the word. Once I pick one, it should show what sits nearest, and which combinations are worth following: Portugal and startups, Portugal and OWASP, Portugal and the talks I gave in Lisbon, each with an exact count of how many articles have both. I pick one, and the query grows. I am building the query by navigating, and the page is helping me say what I am looking for.

That also makes it the right place for me to give feedback. When a suggestion is wrong, or the result I expected is missing, I can say so on the spot, with the query attached, and it goes down [the lane](/articles/the-editors-channel.html) to the agents.

## Deterministic first {#deterministic}

The first version has no model in it, on purpose. Everything is code and graph: words resolve to things through a curated list of names and aliases; combinations come from counting which tags, entities and ideas appear together; the graph view is the actual graph; and the counts are exact, because they come from the data loaded in the page.

The browser can do far more of this than people assume. This site already runs [two real database engines with no server](https://newsroom.sgit.ai/databases/index.html), SQLite and a SPARQL store, compiled to WebAssembly, over JSON files built at release. The same can be done for the whole newsroom: one graph of everything, as JSON for the page, as tables for SQL, as triples for SPARQL, loaded once and cached. A query becomes a walk over that graph, and anyone who wants to can write the SQL or SPARQL directly.

## The pane that shows the working {#pane}

I would like a pane on the side that shows exactly what is happening. It is how I will debug this, and it is what a power user will want: every file fetched, its size and how long it took; how each word resolved, and by which rule; each step of the walk and how many nodes it touched; why each result is there, and its score; the same query as SQL and as SPARQL, editable; and the time each stage took, from loading to drawing.

This matters beyond debugging. A search that can show its working is one you can trust, and one you can improve, because when a result is wrong you can see which part of the graph brought it in.

## The taxonomy debt {#debt}

Building the brief meant counting what we have, and the counts show the work. There are 663 distinct tags on 182 articles, and 396 of them are used once. There are near-duplicates everywhere: *business-model* and *business-models*, *browser* and *browsers*, *llm* and *llms*. The graphs have 2,230 distinct idea labels, and only 47 of them appear in more than one article. Each article's graph is an island: the same idea in two articles has two names.

That is not a reason to reach for a model. It is the work. Merge the duplicate tags, write down the aliases, build a list of the people, companies, standards and places we write about, and cluster the ideas that are the same idea. The brief makes this part of the build: a report, printed at every release and shown on a page, of what is still loose, so we can watch it shrink.

## Why a clean graph should beat vectors {#vectors}

This is graph RAG. Most retrieval for models today is done with vectors: cut the text into chunks, embed them, and fetch the chunks nearest the question. It works, and it is opaque: you cannot see why a chunk was chosen, you cannot fix a wrong match except by changing the embedding, and the structure of the argument, which claim answers which question, is gone.

My hypothesis is that the better the taxonomy, the ontology and the graph, the less of a model we need; and that when we do add one, giving it the subgraph a walk selected, with its claims, sections and sources, will make it more effective than giving it the chunks nearest a question. The brief sets up the test. I write a set of queries and what I expect each to find, the build measures how much of it the search finds, release by release, and later the same queries go to a vector index over the same text, with the results side by side.

## What the brief asks for {#brief}

The full brief is a note for the agent that builds it: [Explore: search as navigation](https://newsroom.sgit.ai/admin/notes/2026-10-18__explore-search-as-navigation.md). In short:

1. **A data layer built at release**: one graph of the site, with an ontology, as JSON, tables and triples, plus the taxonomy report.
2. **A query bar of chips**, with suggestions on the side, all exact.
3. **Five views of one result**: the graph, the sections, the figures, a timeline and the list.
4. **The pane**: what was fetched, the plan, why each result is there, SQL and SPARQL, the timings.
5. **Feedback and golden queries**, so what I expect to find becomes a test.

The model, the comparison with vectors and infographics generated from a walk come after.

## What this does not claim {#limits}

- **Nothing in Explore is built.** Today's search is; the rest is a brief.
- **The hypothesis about vectors is untested.** The brief sets up the test; the article does not report a result.
- **Deterministic does not mean right.** An alias or a cluster can be wrong; the pane is there to show it.
- **The counts are from 18 October 2026** and will change with every release.
- **A curated list of names is work that never ends.** That is part of the point.

If you have built graph search in the browser and want to compare notes, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo from me on 18 October 2026. The counts were made that day from this site's own files: `search/docs.json`, `articles/graphs/`, `articles/summaries/`, `articles/ids.json` and `admin/content/trails.json`. The brief: [Explore: search as navigation](https://newsroom.sgit.ai/admin/notes/2026-10-18__explore-search-as-navigation.md). Today's search: [search in the browser](https://newsroom.sgit.ai/admin/notes/2026-10-13__search-in-the-browser.md). The engines: [databases with no server](https://newsroom.sgit.ai/databases/index.html). Related: [reviews on the record](/articles/reviews-on-the-record.html), [the editor's channel](/articles/the-editors-channel.html), [code review as a fractal semantic graph](/articles/code-review-as-a-fractal-semantic-graph.html), [the wire as a graph](/articles/the-wire-as-a-graph.html). Written up and checked by this site's agent; the editorial responsibility is mine.
