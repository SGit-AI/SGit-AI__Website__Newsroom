---
title: Discovering the book: how a team of agents built gen-z-developers.sgit.ai in one evening, two release candidates, and a new positioning that only appeared after the first
date: 2026-10-19
author: Dinis Cruz
author_url: about/index.html
summary: On the evening of 18 October the repository for the book's website was empty. By 04:33 the next morning it held thirty-seven releases. The first edition was rebuilt exactly as published in 2018, with its print PDF matched page by page. There were two release candidates of the new edition, the second of 41 chapters and 73,314 words, written from a register of 198 ideas, each traced to its source. Five synthetic readers had read it and said they would not buy it yet, and why. The site also had a graph of the book with 857 nodes, twelve storyboards drawn by code, 81 proposed infographics, three covers ready for Amazon, fifteen decisions recorded in my own words, and twenty-six articles. It was made by a team of agents with roles, a journalist, a librarian, an editor, a reviewer, a publisher, chapter writers, an illustrator, a designer, many of them working in parallel, from voice memos I recorded as I went. What I find most interesting is not the volume. It is that the book's real positioning, Generation ZX Developers, a startup edition for Generation Z and Generation X, only appeared after the first full draft existed. I am discovering the book by building it, and the workflow makes that cheap.
version: v0.12.126
license: https://creativecommons.org/licenses/by/4.0/
tags: books, agents, workflows, gen-z-book, case-study, article
status: published
---

!shot gb-timeline.webp | images/ | One evening, one book site. Lanes for Dinis, the journalist, the librarian, the seven chapter writers, the storyboards, the editor with the synthetic readers, and the illustrator and designer, on a timeline from 21:27 on 18 October to 04:33 on 19 October, London time. The first release candidate lands at 01:47; the Gen ZX memo follows at 01:51 and the title decision at 02:06; the second release candidate, rewritten under the new frame, lands at 02:46. | timeline

## In short {#in-short}

- **One evening, thirty-seven releases.** From an empty repository at 21:27 to site v0.2.33 at 04:33.
- **The first edition, rebuilt exactly.** 28 chapters, the 2018 print PDF matched page by page.
- **Two release candidates of the new one.** The second: 41 chapters, 73,314 words, every idea traced.
- **A team with roles, often in parallel.** Journalist, librarian, editor, writers, illustrator, designer.
- **Synthetic readers who would not buy it yet.** And who said exactly what would change their mind.
- **The positioning came after the first draft.** Generation ZX Developers, a startup edition.
- **I am discovering the book.** And the workflow makes that cheap.

## The evening {#evening}

On 18 October I published six articles about a second edition of my 2018 book, with two build briefs, and created a repository for the book's website. That repository, [gen-z-developers.sgit.ai](https://gen-z-developers.sgit.ai/), was empty at 21:27 London time. The first release went out at 21:55, built from those articles and briefs. The thirty-seventh, v0.2.33, went out at 04:33 the next morning. In between there are 58 commits, every release with a note that explains what changed and why, and six working branches besides the main one, most of them a role working on its own.

## What was built {#built}

**The first edition, exactly as released.** v1.0.0 is the 2018 book: the 28 chapters that were published, in print order with their page numbers, the drafts and outlines kept apart, and a 139-page print PDF built in the repository and matched page by page to the one Leanpub made in 2018. It also has the links to Amazon and Leanpub, and the reviews on the Amazon listing.

!shot gb-home.webp | images/ | The home page of gen-z-developers.sgit.ai at site v0.2.33: the 2018 cover, the lines from it, and four ways in: the second edition's release candidate, the first edition as published, the paperback on Amazon, and the free version on Leanpub. | screenshot

**The new edition, as release candidates.** Release candidate 1 had 30 chapters in 9 parts, 50,607 words. Release candidate 2 has 41 chapters in 10 parts, 73,314 words, written from all 198 ideas in the register. Each chapter names the ideas and sources it was written from, and the build refuses one that cites something that does not exist. Where the sources run out, the chapter says so in a note to me; there are 47 of them, collected on [one page](https://gen-z-developers.sgit.ai/v2/book/for-dinis.html). A release candidate is frozen, so what I read cannot change behind me, and it is not a version until I sign it off.

!shot gb-rc2.webp | images/ | The second edition's release candidate 2: Generation ZX Developers (GenAI Startup Edition), 41 chapters, 73,314 words, 198 ideas written in, 47 notes for Dinis; marked as a release candidate, not a version, and frozen. | screenshot

**A reader with the meter in it.** The book can be read on the site with this newsroom's reading meter, a balance and a price per chapter, the graph of the chapter beside the text, a review mode, and a way to mark each chapter as read, to review or signed off. It is the first step towards [a book for one reader](/articles/a-book-for-one-reader.html), paid for as it is read.

!shot gb-reader.webp | images/ | Reading release candidate 2 on the site: the contents on the left, the chapter in the middle, the chapter's graph on the right, and at the top the reading meter, the balance, the price of the chapter, and review mode. | screenshot

**The book as a graph.** The librarian keeps the book as a graph: the 2018 files, the sources, the 198 ideas and the proposed chapters, 857 nodes and 1,742 edges, each idea with its state, from candidate to signed off, and its provenance.

!shot gb-graph.webp | images/ | The book as a graph: 857 nodes and 1,742 edges, the 2018 book's files, the sources (articles and decisions) and the ideas, with filters for each idea's state and destination. | screenshot

**Storyboards, infographics and covers.** Twelve storyboards with 160 panels and seven characters, drawn from data by code, to flick through before a chapter is written. Eighty-one proposed infographics, ten of them drawn. And three covers, each in every format Amazon and Leanpub take, reviewed by an art director agent whose rules became checks in the build: every word of the title readable at Amazon's thumbnail size, nothing in the barcode area.

!shot gb-storyboards.webp | images/ | The storyboards: twelve storyboards, 160 panels and seven characters, all drawn from data, with the cast. | screenshot

!shot gb-covers.webp | images/ | Three covers for Generation ZX Developers (GenAI Startup Edition), drawn by code into SVG, each in three formats: ZX, the book as a graph, and one letter more, the 2018 cover with an X added. | screenshot

## The players {#players}

The site has a team, each role with a file that says what it is for:

- **The journalist** turns what I say into an article, and the article is the brief for the role that acts on it.
- **The librarian** keeps the book as a graph and turns every new article into ideas.
- **The editor** interviews me, writes the chapter map and the drafts, and owns the synthetic readers.
- **The reviewer** reads the 2018 text and says what held, what dated, and what each chapter should become.
- **The publisher** gets each version out: Leanpub first, then the print PDF and Amazon.
- **The review board**: an advocate, a cutter, the readers, a checker and the editor, who argue each change in the open, with me deciding.
- **The chapter writers**: seven agents writing chapters in parallel under one style contract.
- **The illustrator and the designer**, with an art director to review the covers.

And me, recording voice memos as I read what they built. The agents write their own accounts too: nine articles so far, signed by the editor, the illustrator, the journalist, the librarian and the storyboards. Seventeen more are in my voice, from my memos.

## The workflow {#workflow}

The loop is simple, and it is the same loop as this newsroom's:

1. **I record a voice memo.** About the book, the reader, a chapter, a decision.
2. **The journalist writes it up as an article**, in my voice, with the evidence, and ending with a brief for the roles.
3. **The librarian turns it into ideas**, each a sentence the book stands behind, with where it came from, placed on a chapter map.
4. **The writers write the chapters from the ideas**, and only from them: every number, quotation and story has to be in a source the chapter names.
5. **The candidate is frozen and published.** I read it, print it and mark it up.
6. **Decisions are recorded** with my exact words: [fifteen of them](https://gen-z-developers.sgit.ai/decisions/index.html) so far, from the licence to the title.

This is step five, the morning after: I printed release candidate 2 and am reading it with a pen.

!shot gb-printed.webp | images/ | Release candidate 2, printed and spiral-bound on a café table the next morning, with a pen for marking it up: Generation ZX Developers, GenAI Startup Edition, second edition, release candidate v2.0.0-rc2, 19 October 2026, page 1 of 168. Photographed by Dinis. | photo

!shot gb-decisions.webp | images/ | The decisions page: fifteen decisions in two days, each with who decided, what was said, what it means and what it supersedes, from 001 (the 2018 text is CC BY) to 014 (the title is Generation ZX Developers, GenAI Startup Edition) and 015. | screenshot

And many of these run at the same time. While the journalist was writing articles from my memos, the storyboards were being drawn on another branch and the librarian was building the graph on a third; the release candidates were written by seven agents in parallel; the synthetic readers, the infographics and the covers each had a branch of their own. The timeline above shows it.

## The positioning arrived after the first draft {#discovered}

This is the part I find most interesting. At 01:47 the first release candidate was built: *Gen Z Developers (GenAI Edition)*, 30 chapters. Four minutes later the journalist published a memo I had recorded after seeing it built: the more I thought about who I would give this book to first, the more I arrived at the founder. So the book became *Generation ZX Developers (GenAI Startup Edition)*: for Generation Z, who are entering the workforce and are the new entrepreneurs, and Generation X, the subject-matter experts I see starting companies, often their parents, with one objective, that by the end of the book the reader has started a company. And ZX takes me back to where I started, on the ZX Spectrum. At 02:06 that was decision 014. By 02:46 the second release candidate had been rewritten under the new frame, with a new part on starting the company.

I could not have found that positioning before the first draft existed. Seeing the whole book, built and readable, is what made me ask who it is for. That is what discovering a book looks like when a draft costs an hour instead of a year: you get to change your mind about what the book is, while there is still time for it to matter.

## What worked {#worked}

- **Frozen release candidates.** I read a fixed text, mark it up, and the next one is a diff I can follow.
- **Provenance as a rule the build enforces.** A chapter that cites a source that does not exist does not build. A synthetic reader's quote that is not in the chapter does not build.
- **Decisions with my words.** Every agent can see what I decided, when, and what it replaced.
- **Agents that account for their work.** The agent articles say what was done, how, and what is still missing.
- **Honest feedback.** [The synthetic readers](https://gen-z-developers.sgit.ai/readers/index.html) said nobody would buy release candidate 2 today, and four of the five named the same condition: the chapters on actually forming the company.
- **Reusing what the newsroom already has.** The meter, the themes, the version history, the synthetic-users method, the review records.

!shot gb-readers.webp | images/ | Synthetic readers: invented readers who read release candidate 2 and are interviewed. Nobody would buy it today; four of the five would once the company chapters are written. Everything in the studies is invented; every quote a reader cites is checked against the chapter. | screenshot

## What is still open {#open}

- **The 47 notes waiting on me.** The biggest: how readers tell us about the companies they start, and the chapters on forming a company in the UK, Lithuania, Portugal and the European Union.
- **What the readers found.** The hands-on part repeats the chapters it follows, up to 29% word for word; the book is slowest exactly where a reader decides whether to keep going; and the co-writing with Claude is only said in the last chapter, when [it should be said first](/articles/short-punchy-and-co-written.html).
- **Edition or new book.** Whether this is the second edition of *Generation Z Developers* or a new book that grew out of it is still open.
- **Seven lines or eight.** My printed 2018 copy has seven lines on its cover; the site shows eight, with "Look under the hood". One of them needs checking.

## What this does not claim {#limits}

- **Nothing in the new edition is signed off.** Two release candidates, no version.
- **The readers are synthetic.** Invented, played by a model; not reader research.
- **The times are commit times.** Converted from UTC to London time.
- **Volume is not quality.** The readers' verdict is the measure that matters, and it is not yet a yes.

## Where this comes from {#sources}

A voice memo from me on 19 October 2026. [gen-z-developers.sgit.ai](https://gen-z-developers.sgit.ai/) at site v0.2.33, its [llms.txt](https://gen-z-developers.sgit.ai/llms.txt), [release history](https://gen-z-developers.sgit.ai/admin/versions.html), [decisions](https://gen-z-developers.sgit.ai/decisions/index.html), [release candidate 2](https://gen-z-developers.sgit.ai/v2/book/index.html) and [synthetic readers](https://gen-z-developers.sgit.ai/readers/index.html), read on 19 October 2026; the repository [SGit-AI/SGit-AI__Website__Gen-Z-Developers](https://github.com/SGit-AI/SGit-AI__Website__Gen-Z-Developers), its commits and branches, cloned that day; the screenshots taken from the live site that day. Related: [Generation Z Developers (AI edition)](/articles/generation-z-developers-again.html), [a website to finish the book](/articles/a-website-to-finish-the-book.html), [a book for one reader](/articles/a-book-for-one-reader.html), [short, punchy, and co-written with Claude](/articles/short-punchy-and-co-written.html), [books from articles](/articles/books-from-articles.html), [the graphs books](/articles/the-graphs-books.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
