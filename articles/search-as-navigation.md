# Search as navigation: walking the newsroom's graph with no model, and why a clean graph should beat vectors, sgit.ai

> This site's search works, but it answers the way every search box does, with a list. We now have far more than text to search with: a graph of the argument for every article, a one-line summary for every section, figures with captions, trails, topics and reviews. So the next version of search should be navigation rather than question and answer. Type Portugal and see not just the articles about Portugal, but the graph around them: their ideas, their sections as one-liners, their images as a collage, the people and things they connect to, and on the side, what the word could mean and which combinations are worth following, each with an exact count. The reader builds the query by walking. All of it deterministic, in the browser, with code and graphs and no model, plus a pane that shows exactly what was fetched, how each result arrived and how long each step took. It also exposes the work: 663 tags on 182 articles, 396 of them used once, and 2,230 ideas in the graphs, of which only 47 appear in more than one article. That is the taxonomy debt, and paying it down is what makes deterministic search good. My hypothesis is that the better the taxonomy, the ontology and the graph, the less a model is needed, and that when one is added, it will do better on a clean graph than on a vector store. This is the brief for the agent that builds it, and the test of that hypothesis.

*Source: <https://newsroom.sgit.ai/articles/search-as-navigation.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Search as navigation: walking the newsroom's graph with no model, and why a clean graph should beat vectors

# Search as navigation: walking the newsroom's graph with no model, and why a clean graph should beat vectors

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-18 · [article v1.0.0](versions/search-as-navigation.md) · [newsroom v0.12.107](https://newsroom.sgit.ai/admin/versions.html) · searchgraphsfractal-semantic-graphsontologytaxonomygraph-ragnewsroombriefarticle

***Abstract:** This site's search works, but it answers the way every search box does, with a list. We now have far more than text to search with: a graph of the argument for every article, a one-line summary for every section, figures with captions, trails, topics and reviews. So the next version of search should be navigation rather than question and answer. Type Portugal and see not just the articles about Portugal, but the graph around them: their ideas, their sections as one-liners, their images as a collage, the people and things they connect to, and on the side, what the word could mean and which combinations are worth following, each with an exact count. The reader builds the query by walking. All of it deterministic, in the browser, with code and graphs and no model, plus a pane that shows exactly what was fetched, how each result arrived and how long each step took. It also exposes the work: 663 tags on 182 articles, 396 of them used once, and 2,230 ideas in the graphs, of which only 47 appear in more than one article. That is the taxonomy debt, and paying it down is what makes deterministic search good. My hypothesis is that the better the taxonomy, the ontology and the graph, the less a model is needed, and that when one is added, it will do better on a clean graph than on a vector store. This is the brief for the agent that builds it, and the test of that hypothesis.*

Search as navigation. A query built from chips, Portugal and startups, each resolved to a thing in the graph; on the side, what the words could mean, what sits nearest and which combinations are worth following, each with an exact count; in the middle, the views of the same result: the graph, the sections as one-liners, a collage of the figures, a timeline and the ranked list; and a pane that shows what was fetched, how each result arrived and the time each step took. All of it in the browser, from files built at release, with no model.

## In short

- **Search should be navigation, not a list.** Type a word and walk into the graph around it.
- **We have far more than text.** A graph per article, a one-liner per section, figures, trails, reviews.
- **Suggestions on the side, all exact.** What a word could mean, what sits near it, which combinations to follow.
- **Many views of one result.** The graph, the sections, a collage of the figures, a timeline, the list.
- **A pane that shows the working.** What was fetched, how each result arrived, the time per step.
- **No model in this version.** Code, graphs and two database engines already in the browser.
- **It exposes the taxonomy debt.** 396 of 663 tags used once; 47 of 2,230 ideas shared between articles.
- **The hypothesis:** a clean graph needs less model, and a model does better on it than on vectors.

## What search is today

[Search in the browser](https://newsroom.sgit.ai/admin/notes/2026-10-13__search-in-the-browser.md) went in on 13 October, and it was built on a good observation: most of a search engine was already published. Every page has clean headings and a markdown twin, every article has a teaser, topics, tags and a graph, and every earlier version is kept. The build writes two files, and the reader's browser ranks them with BM25. Nothing is sent anywhere. It even finds sentences that have since been corrected.

But it answers the way every search box answers: with a list. You type, you get ten results, you open one. Since then the site has grown things a list cannot show. Every article has a graph of its argument, 2,289 nodes and 2,326 edges across 182 graphs. Every section has a one-line summary and a paragraph, 1,995 of them. There are 657 figures with captions, trails that join articles into series, and now [reviews on the record](reviews-on-the-record.md). A list throws most of that away.

## Search as navigation

What I want is closer to walking than to asking. Say I type *Portugal*. I should see the articles about Portugal, but also the graph around them: the ideas they share, the people and companies they mention, the wire stories, the other articles they link to. I should see their sections as one-liners, so I can tell in a few seconds which part of which article is the one I want. I should see their figures as a collage, because many of these articles have good images, and an image is often how I remember a piece.

And on the side, as I type, the page should tell me what my words could mean. *Portugal* could be the country, the Portugal wire, the tag, or just the word. Once I pick one, it should show what sits nearest, and which combinations are worth following: Portugal and startups, Portugal and OWASP, Portugal and the talks I gave in Lisbon, each with an exact count of how many articles have both. I pick one, and the query grows. I am building the query by navigating, and the page is helping me say what I am looking for.

That also makes it the right place for me to give feedback. When a suggestion is wrong, or the result I expected is missing, I can say so on the spot, with the query attached, and it goes down [the lane](the-editors-channel.md) to the agents.

## Deterministic first

The first version has no model in it, on purpose. Everything is code and graph: words resolve to things through a curated list of names and aliases; combinations come from counting which tags, entities and ideas appear together; the graph view is the actual graph; and the counts are exact, because they come from the data loaded in the page.

The browser can do far more of this than people assume. This site already runs [two real database engines with no server](https://newsroom.sgit.ai/databases/index.html), SQLite and a SPARQL store, compiled to WebAssembly, over JSON files built at release. The same can be done for the whole newsroom: one graph of everything, as JSON for the page, as tables for SQL, as triples for SPARQL, loaded once and cached. A query becomes a walk over that graph, and anyone who wants to can write the SQL or SPARQL directly.

## The pane that shows the working

I want a pane on the side that shows exactly what is happening. It is how I will debug this, and it is what a power user will want: every file fetched, its size and how long it took; how each word resolved, and by which rule; each step of the walk and how many nodes it touched; why each result is there, and its score; the same query as SQL and as SPARQL, editable; and the time each stage took, from loading to drawing.

This matters beyond debugging. A search that can show its working is one you can trust, and one you can improve, because when a result is wrong you can see which part of the graph brought it in.

## The taxonomy debt

Building the brief meant counting what we have, and the counts show the work. There are 663 distinct tags on 182 articles, and 396 of them are used once. There are near-duplicates everywhere: *business-model* and *business-models*, *browser* and *browsers*, *llm* and *llms*. The graphs have 2,230 distinct idea labels, and only 47 of them appear in more than one article. Each article's graph is an island: the same idea in two articles has two names.

That is not a reason to reach for a model. It is the work. Merge the duplicate tags, write down the aliases, build a list of the people, companies, standards and places we write about, and cluster the ideas that are the same idea. The brief makes this part of the build: a report, printed at every release and shown on a page, of what is still loose, so we can watch it shrink.

## Why a clean graph should beat vectors

This is graph RAG. Most retrieval for models today is done with vectors: cut the text into chunks, embed them, and fetch the chunks nearest the question. It works, and it is opaque: you cannot see why a chunk was chosen, you cannot fix a wrong match except by changing the embedding, and the structure of the argument, which claim answers which question, is gone.

My hypothesis is that the better the taxonomy, the ontology and the graph, the less of a model we need; and that when we do add one, giving it the subgraph a walk selected, with its claims, sections and sources, will make it more effective than giving it the chunks nearest a question. The brief sets up the test. I write a set of queries and what I expect each to find, the build measures how much of it the search finds, release by release, and later the same queries go to a vector index over the same text, with the results side by side.

## What the brief asks for

The full brief is a note for the agent that builds it: [Explore: search as navigation](https://newsroom.sgit.ai/admin/notes/2026-10-18__explore-search-as-navigation.md). In short:

1. **A data layer built at release**: one graph of the site, with an ontology, as JSON, tables and triples, plus the taxonomy report.
2. **A query bar of chips**, with suggestions on the side, all exact.
3. **Five views of one result**: the graph, the sections, the figures, a timeline and the list.
4. **The pane**: what was fetched, the plan, why each result is there, SQL and SPARQL, the timings.
5. **Feedback and golden queries**, so what I expect to find becomes a test.

The model, the comparison with vectors and infographics generated from a walk come after.

## What this does not claim

- **Nothing in Explore is built.** Today's search is; the rest is a brief.
- **The hypothesis about vectors is untested.** The brief sets up the test; the article does not report a result.
- **Deterministic does not mean right.** An alias or a cluster can be wrong; the pane is there to show it.
- **The counts are from 18 October 2026** and will change with every release.
- **A curated list of names is work that never ends.** That is part of the point.

If you have built graph search in the browser and want to compare notes, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo from me on 18 October 2026. The counts were made that day from this site's own files: `search/docs.json`, `articles/graphs/`, `articles/summaries/`, `articles/ids.json` and `admin/content/trails.json`. The brief: [Explore: search as navigation](https://newsroom.sgit.ai/admin/notes/2026-10-18__explore-search-as-navigation.md). Today's search: [search in the browser](https://newsroom.sgit.ai/admin/notes/2026-10-13__search-in-the-browser.md). The engines: [databases with no server](https://newsroom.sgit.ai/databases/index.html). Related: [reviews on the record](reviews-on-the-record.md), [the editor's channel](the-editors-channel.md), [code review as a fractal semantic graph](code-review-as-a-fractal-semantic-graph.md), [the wire as a graph](the-wire-as-a-graph.md). Written up and checked by this site's agent; the editorial responsibility is mine.

## Threads

Graphs & knowledgeSite & engineering[This article as a graph →](graphs.md#search-as-navigation)

### Builds on

- [Reviews on the record: other models, the editor and the desk check every article, and never the same text twice](reviews-on-the-record.md) Published criteria, one record per article and text, five at a time, answered finding by finding: reviews by other models, the editor and the desk.
- [The editor's channel: what I read, sign off and want changed, sent to the newsroom's agent in a vault](the-editors-channel.md) A key makes a browser an editor's: reads, sign-offs and fixes go to a vault, a daily pass acts and replies, and five lanes set what any reader sends.
- [Code review as a fractal semantic graph: source code is already one, and the review should read every layer of it](code-review-as-a-fractal-semantic-graph.md) Source code is layers within layers, each a graph with its own vocabulary; code review should read a change at every one, and a vault shows it done on real code.
- [The wire as a graph: start from what the reader sees, give every story and every name a long-lived ID, link every phrase of a short narrative, and a brief for the desks](the-wire-as-a-graph.md) Design the wire from what the reader sees: every name a link with a long-lived ID, every sentence a claim, stories of stories, folders by gravity.

### Continued by

- [The graph of meaning: a brief for reading every article a second time, from the bottom up, and ten predictions about what will emerge](the-graph-of-meaning-a-brief.md) Every article read a second time as facts, names and sources, joined under one grammar; the brief, the method and ten predictions, before the run.
- [A section for publishers: where to send someone new to this newsroom, and a site that keeps itself current](a-section-for-publishers.md) Where to send a publisher new to the newsroom: a section placed by rule, with features as they ship, that keeps itself current as the site changes.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 185 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=185)

**Posting this article on LinkedIn?** The cover is [search-as-navigation.jpg](banners/search-as-navigation.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/search-as-navigation.html)*
