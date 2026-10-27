---
title: A website to finish the book: gen-z-developers.sgit.ai, where the released book lives in the repository, the working book lives in a vault, and agents help me review it at every altitude
date: 2026-10-18
author: Dinis Cruz
author_url: about/index.html
summary: To make Generation Z Developers (AI edition), the plan is a website for it, consolidating the best of everything we have built so far into the most productive environment I can have for reviewing a book. The rule that organises it: the repository holds the official versions, and a vault holds the working versions. Version one is the book as released in 2018, so it goes into the repository as it is, dated, and the site starts as that book; everything after it is worked on in the vault and moved into the repository when it is ready, with a delta between each version, which is something I have always wanted for my books. From there: a semantic graph of the book, with its ontology and taxonomy; the book at every altitude, from a one-page view to the full text, with an infographic at each one; a narrative that guides the reader through it like a plot. While I read, I can comment by voice. There is a board, issues, and agents in roles, an editor, a copywriter and a publisher, who read the book, challenge it, write interview scripts for me, and sign off the parts we are happy with. Market research, evidence and maps for every section. And one correction to my own memo: the vault the book lives in will be public, so the OpenRouter key cannot go in it; it needs a vault of its own. The last part of the book should explain how all of this was built, because that is exactly what I hope a Generation Z developer will be able to do. And I would argue that anyone who read the 2018 book and acted on it was well prepared for what happened next.
version: v0.12.118
license: https://creativecommons.org/licenses/by/4.0/
tags: books, generation-z, vaults, graphs, publishing, gen-z-book, brief, article
status: published
---

!shot gw-site.webp | images/ | The book's website: the repository with the official versions, and the public vault with the working versions. | architecture

## In short {#in-short}

- **A website for the book.** gen-z-developers.sgit.ai, matching the book's name.
- **The repository holds the official versions.** Starting with the 2018 book, exactly as released.
- **A vault holds the working versions.** Public, so anyone can read along.
- **A delta between every version.** Something I have always wanted for my books.
- **The book as a graph, at every altitude.** With an infographic at each one.
- **Agents in roles.** Editor, copywriter, publisher: reading, challenging, interviewing me, signing off.
- **The OpenRouter key goes in a vault of its own.** Not in the public one.

## Why a website {#why}

Of everything we have built in these repositories, the idea is to bring the best parts together in one place, set up as the most effective and productive environment I can have for one job: reviewing and finishing this book. The ideas came from many places, most of them from the books on [graphs.sgit.ai](https://graphs.sgit.ai/v2/books/index.html), where a lot of these concepts first appeared: a shelf with versions, seven roles with a folder each, the book as a graph, the same book at several altitudes. This is where they come together, for a book I would like to finish.

## The name {#name}

The site should match the book. The printed cover says *Gen Z Developers*, and the book is *Generation Z Developers*, so the address is gen-z-developers.sgit.ai rather than something shorter like genz-devs.

## The repository and the vault {#repo-and-vault}

The organising rule: **the repository contains the official versions; the vault contains the working versions.**

The first version of the book is already final: released, dated September 2018, sixty per cent complete. So it goes into the repository as it is, and the first version of the website shows exactly that book. Everything after it is worked on in the vault: drafts, comments, graphs, reviews. When a version is ready, it moves from the vault into the repository, on top of the one before.

That gives the thing I have always wanted when I issue a new version of a book: a proper delta between one version and the next. The first one, from 2018 to 2026, will be brutal. After that, each delta will say exactly what changed, the way [the versions of the page for publishers](https://newsroom.sgit.ai/publishers/versions/index.html) already do for one page, and the way [versions of versions](/articles/versions-of-versions.html) proposes for the parts of this site.

## The book as a graph, at every altitude {#graph}

Then the book becomes a semantic graph: its ontology and taxonomy, its concepts linked to each other and to the evidence, so I can make references across it and reshape it. The [graphs books](/articles/the-graphs-books.html) tried an [altitude ladder](https://graphs.sgit.ai/v1/altitudes/index.html), the same book at five altitudes, from a single paragraph down to the full text, each level a compression of the one below. This book should have that from the start, and an infographic at every altitude: the whole book on one page; a view per part; an infographic per chapter, and how they connect; the graph of each area. We go up and down between them until we arrive at the version that is just right.

And through it, a narrative. Not only a table of contents, but a path that guides the reader through the book, almost like a plot, from a simple version to the full one.

## Reading, reviewing, signing off {#review}

What I need while I review:

- **Voice, while I read.** Comments recorded as I read a section, attached to it.
- **Comments, a board and issues.** What is open, what is being worked on, what is done.
- **Agents in roles.** An editor, a copywriter and a publisher, at least, who read the book, give feedback, challenge it, and write interview scripts for me, so that I have to justify the points, the way [ten hard questions for RiskMandate](/articles/riskmandate-ten-questions.html) was done.
- **Sign-off.** A way to mark parts of the book that we are happy with, so the work moves on.

All of it is public. The dynamic data starts in the vault, and the official versions end up in the repository.

## Research and evidence {#evidence}

Then the agentic tasks around the text: market research on who the book is for and what else they read; validation of the claims; evidence behind each one; and maps and graphs for each section, eventually for each paragraph. The book should be able to show its work, the way this newsroom's articles do.

## The OpenRouter key needs its own vault {#key}

My memo said to put an OpenRouter key in the book's vault, available only with the vault key. That does not work as described, because the book's vault is meant to be public: its read key will be published, so that anyone can read the working book. Anything in it is readable by everyone.

So the key goes in a second, private vault that opens only with my passkey, the way this newsroom's reader vault does. And the key itself should have a credit limit set at OpenRouter, so a mistake costs a little, not a lot; [the key is the billing system](/articles/the-key-is-the-billing-system.html) describes keys with limits. The agents that need a model get it through that key; the public vault never holds it.

## The last part of the book {#last}

The last part of the book should explain how all of this comes together: the repository and the vault, the graph and the altitudes, the agents and their roles, the reviews and the versions. Because that is exactly what I hope a Generation Z developer will be able to build, for their own ideas.

It will also be interesting to see how much of the first book's core ideas has not changed. I would argue that they are universal. And I would say it plainly, not as a boast: anyone who read the 2018 book and acted on it, who learned how to learn, questioned everything and built things in public, was well prepared for the AI revolution that has just happened. Those who read it now should be ready for what happens next.

## The brief {#brief}

The build brief is a note: [a website to finish the book](https://newsroom.sgit.ai/admin/notes/2026-10-18__a-website-to-finish-the-book.md). It is also on [the briefs page](https://newsroom.sgit.ai/briefs/index.html#gen-z-book-website). The book's plan is in [Generation Z Developers (AI edition)](/articles/generation-z-developers-again.html).

## What this does not claim {#limits}

- **Nothing is built.** No repository, vault or site yet.
- **The address is a proposal.** gen-z-developers.sgit.ai, to confirm.
- **The altitude ladder was an experiment.** It worked on graphs.sgit.ai for one book; this would be its second.
- **"Well prepared" is my argument.** Not a measured result.

## Where this comes from {#sources}

A voice memo from me on 18 October 2026. [graphs.sgit.ai](https://graphs.sgit.ai/v2/books/index.html), its [altitude ladder](https://graphs.sgit.ai/v1/altitudes/index.html) and [roles](https://graphs.sgit.ai/v2/team/index.html); the [versions of the page for publishers](https://newsroom.sgit.ai/publishers/versions/index.html). Related: [Generation Z Developers (AI edition)](/articles/generation-z-developers-again.html), [versions of versions](/articles/versions-of-versions.html), [the graphs books](/articles/the-graphs-books.html), [the key is the billing system](/articles/the-key-is-the-billing-system.html), [a book for one reader](/articles/a-book-for-one-reader.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
