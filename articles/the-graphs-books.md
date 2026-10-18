# The graphs books: three books written by agents in a day, the altitudes, the board and the book as a graph, what they got right, and why they stopped under review, sgit.ai

> In August, on graphs.sgit.ai, agents wrote three books from a month of work on fractal semantic graphs, about 100,000 words between them, because I had a long flight the next day and wanted something to read. I read them, printed, and made a lot of notes. They are good, and much of what is in them, and in how they were made, now runs this newsroom. But two months later they are still at v0.3.0, v0.2.0 and v0.1.0, under review or held. This is the story of those books: what each one argues; the experiments around them, from an altitude ladder that compresses a book into one paragraph and lets you climb back down, to a board of workstreams and a book decomposed to the word and rebuilt byte-identical; why the book about making books read far better than the book about graphs; and where it stopped, which is the most useful part. The change-control workflow designed to apply my review notes had seven stages, and the approve stage was me. Nothing ever passed through it. It is a good example of a workflow that moves fast while there is energy and then stops, because the next step is too big, and it is why the next books will be made from articles.

*Source: <https://newsroom.sgit.ai/articles/the-graphs-books.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The graphs books: three books written by agents in a day, the altitudes, the board and the book as a graph, what they got right, and why they stopped under review

# The graphs books: three books written by agents in a day, the altitudes, the board and the book as a graph, what they got right, and why they stopped under review

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-16 · [article v1.1.0, 2 versions](versions/the-graphs-books.md) · [newsroom v0.12.77](https://newsroom.sgit.ai/admin/versions.html) · booksgraphsfractal-semantic-graphsagentspublishingworkflowscase-studyreviewfeedback-looparticle

***Abstract:** In August, on graphs.sgit.ai, agents wrote three books from a month of work on fractal semantic graphs, about 100,000 words between them, because I had a long flight the next day and wanted something to read. I read them, printed, and made a lot of notes. They are good, and much of what is in them, and in how they were made, now runs this newsroom. But two months later they are still at v0.3.0, v0.2.0 and v0.1.0, under review or held. This is the story of those books: what each one argues; the experiments around them, from an altitude ladder that compresses a book into one paragraph and lets you climb back down, to a board of workstreams and a book decomposed to the word and rebuilt byte-identical; why the book about making books read far better than the book about graphs; and where it stopped, which is the most useful part. The change-control workflow designed to apply my review notes had seven stages, and the approve stage was me. Nothing ever passed through it. It is a good example of a workflow that moves fast while there is energy and then stops, because the next step is too big, and it is why the next books will be made from articles.*

The shelf on graphs.sgit.ai: three books, each with its own version, and v1.0.0 reserved for a final release; Fractal Semantic Graphs at v0.3.0, under review, 18 chapters and 38,824 words, with the change that moved it.

## In short

- **Three books in a day.** Written on 26 August from a month of work, for a long flight.
- **About 100,000 words.** 47 chapters, three print PDFs, every claim anchored.
- **Experiments around them.** An altitude ladder, a board, the book as a graph.
- **One read far better.** The book about making books, written over a real record.
- **They stopped at review.** Seven stages, and the approve stage was me.
- **Much of it lives on here.** Roles, versions, "where we lose", per-article graphs.
- **The lesson.** Small finished pieces beat one big review.

## How they started

[graphs.sgit.ai](https://graphs.sgit.ai/) was built in about a month, from 21 August to 20 September 2026, to make one idea concrete: in a fractal semantic graph, a node means nothing on its own, and what it is arrives through its edges, at every level of zoom. A first book, *Meaning Through Connectivity*, was written in the first days and frozen on 23 August, its files hashed so the build fails if any changes.

Then, on 26 August, I sent a memo: "can you write a brief to write three books/pdf created from this repo and the work we have done so far (I have a long flight tomorrow and will use it to read these)". The agent read the flight as the shape of the deadline: each book had to be one self-contained PDF of 60 to 120 pages. Each book got a folder and a README that was its first prompt, and three fresh Claude Code sessions wrote them in parallel, the same day.

## The three books

[The shelf](https://graphs.sgit.ai/v2/books/index.html) gives each book its own version, and keeps v1.0.0 "reserved for a book's actual final release, so a number below it says plainly that the book is still under review."

**[Fractal Semantic Graphs: Meaning Through Connectivity](https://graphs.sgit.ai/v2/books/fsg/index.html)**, v0.3.0, is the argument: 15 chapters in five parts, from "A node is just a node" to "Your first graph, tomorrow", 38,824 words and a 119-page PDF. Its opening line is the idea in one sentence: "A node connected to nothing is literally meaningless. This book is what follows from taking that seriously." It says it was "designed to be finished on a flight".

**[Creating a Book Using Agentic Workflows](https://graphs.sgit.ai/v2/books/making-a-book/index.html)**, v0.2.0, is the making-of: twelve chapters, from "The loop" to "The failures, lovingly" and "What it costs, and where it loses", 31,435 words and 92 pages, built from 88 tagged releases over six days. Its subtitle is what this newsroom now does every day: "A voice memo in the morning, a shipped release by the afternoon, and a repository where every claim can be checked."

**[The Universe volume](https://graphs.sgit.ai/v2/books/fsg-universe/index.html)**, v0.1.0, held, is an atlas: 90 concepts in eight regions, 168 named verbs, 165 verbatim quotes from 35 sources, and what the atlas found, "6 contradictions · 9 named absences · 23 near-but-nots".

## The experiments around them

The altitude ladder: the first edition at five altitudes, from the book in one paragraph to the six parts, the seventeen units, the sections and the book itself; every highlighted phrase descends into what it compressed, coloured by the evidence behind it.

What I find most valuable now is not the books but what was tried around them.

**The altitude ladder.** [The same book at five altitudes](https://graphs.sgit.ai/v1/altitudes/index.html), "where each level is a compression of the level below it, and every highlighted phrase descends into the units it compressed": the book in a paragraph of 135 words, the six parts, the seventeen units, the sections, and the book itself. Its best finding is why this matters: "a compression puts sentences next to each other that the full text keeps forty pages apart", and two of them turned out to contradict each other. And: "Level 3 is where the book becomes readable in one sitting, level 2 is where it becomes quotable, and level 1 is where it becomes a claim you either accept or reject."

**The book as a graph.** [Decomposed all the way to the word](https://graphs.sgit.ai/v2/books/making-a-book/graph/index.html), book, chapter, section, block, sentence, word, "and provably put back together": "Every chapter below rebuilt byte-identical on this build." The point was to make a big edit a transformation on the graph, checked by a gate, instead of an edit in a word processor.

**Worked examples and vaults.** [Graphs with real numbers](https://graphs.sgit.ai/v1/examples/index.html), from a two-factor authentication finding traced up to the board and the regulator, to Article 26(5) of the AI Act, where five of nine questions are unanswered and the brief calls those five "the actual output of the exercise".

**The team.** [Seven roles, one folder each](https://graphs.sgit.ai/v2/team/index.html), librarian, researcher, writer, editor, developer, QA and publisher, each with its briefs and debriefs, and my memos kept verbatim, because "the founder's voice is source material and is not edited."

## Why one book read better

The book as a graph: Creating a Book Using Agentic Workflows decomposed into book, chapter, section, block, sentence and word, with the counts per chapter, and every chapter rebuilt byte-identical on the build.

When I read them, the difference was striking. In my memo after the flight I said the alignment of the making-of was "way stronger, like by orders of magnitude" than the book about graphs; reading it, "there was actually not that much stuff I felt wanted to change." The site's release notes give the reason, and it is the most important lesson in the whole estate: "the same agent, the same day, the difference being that book C was written over 41 narrated release rows, 38 verbatim briefs and a repository it could interrogate, while book B was written over an argument."

That is what these articles are now: a record. Every article here starts from a voice memo, is checked against sources, and lands in a repository the next article can read. That is why I think [books can be made from them](books-from-articles.md).

## Where it stopped

The project board for the making-of book: queued, up next and in progress, nothing done; the naming question and the workflow document both four stages of seven in and blocked, waiting on the founder, and publishing held until part one lands.

This is the part worth learning from. After the flight I asked for review as change control: "we start by planning, mapping, defining, reviewing, approving, and then implementing, and then approving the implementation". The agents built it, with care: a [board](https://graphs.sgit.ai/v2/books/making-a-book/board.html) of eight workstreams, 40 tasks and seven stages per change. And the board tells the story itself: "The two change-control workstreams are both blocked at the same stage, on the same person." The state map says it more plainly: the approved stage "has two items waiting and nothing has ever passed through it".

The last release was on 20 September. My energy had moved on, to the next [place of highest leverage](places-of-highest-leverage.md), and the books stayed where they were. I said in another memo why my Leanpub books never finished, and it is the same story: "I got to that sort of 60 70% of the content, and then the overhead of making changes." The workflow was well designed for quality and badly designed for momentum: every step was big, and the biggest one waited on me.

## What lives on here

A lot of it moved into this newsroom, which is why I do not think of the books as wasted:

- **Seven roles, one folder each**, the [team](https://newsroom.sgit.ai/governance/team.html) here, whose shape, its page says, is borrowed from graphs.sgit.ai.
- **"Where we lose"**, the participant disclosure, and **what ships against what is argued**, both here as pages.
- **Versions you can read**, a release history, and versions per article instead of per book.
- **A graph per document**: every article here has one, with its nodes, edges and quotes, the small descendant of the book as a graph.
- **llms.txt and a markdown twin for every page.**
- **Memos as source material**, kept and quoted, never edited.

And the state map went the other way: graphs.sgit.ai borrowed it from this newsroom's brief. That is how it should work; ideas move between the sites as they prove themselves.

## What this does not claim

- **The books are not finished.** Two are under review, one is held, one is frozen.
- **The flight notes are not on the site.** It records "a bunch of notes", not each one.
- **Not that the workflow was wrong.** It was right for quality; it needed smaller steps.
- **The comparison is one case.** Two books, one agent, one day.

If you want to try writing a book this way, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 16 October 2026, written by this site's agent in the voice of this site; the editorial responsibility is mine. Everything else is from [graphs.sgit.ai](https://graphs.sgit.ai/) as published on 16 October 2026: [the books](https://graphs.sgit.ai/v2/books/index.html), [the altitude ladder](https://graphs.sgit.ai/v1/altitudes/index.html), [the book as a graph](https://graphs.sgit.ai/v2/books/making-a-book/graph/index.html), [the board](https://graphs.sgit.ai/v2/books/making-a-book/board.html), [the team](https://graphs.sgit.ai/v2/team/index.html), [the release history](https://graphs.sgit.ai/admin/versions.html) and [its v0.5 part](https://graphs.sgit.ai/admin/versions-v0.5.html), and the founder memos 38, 39, 40, 42 and 44 kept there verbatim. Page counts were measured from the published PDFs.

## Threads

Graphs & knowledgeSite & engineering[This article as a graph →](graphs.md#the-graphs-books)

### Builds on

- [Books from articles: why my books stall at 95%, why these articles do not, and a plan to turn them into books by Web Summit](books-from-articles.md) My books stall at 60 to 95%; these articles do not. The hypothesis: a book is an ordered set of finished articles, tested by Web Summit in November.
- [Places of highest leverage: where to focus when the agents can go in every direction, told with three days of real steps](places-of-highest-leverage.md) Where to focus when agents can go in every direction: the place of highest leverage, shown on three days of real steps, two walked back and one parked.

### Continued by

- [A website to finish the book: gen-z-developers.sgit.ai, where the released book lives in the repository, the working book lives in a vault, and agents help me review it at every altitude](a-website-to-finish-the-book.md) gen-z-developers.sgit.ai: the released book in the repository, the working book in a public vault, and agents helping me review it at every altitude.
- [Generation Z Developers (AI edition): the 2018 book that said act like you are part of the company, what it got right, and a new edition for the people I want to help](generation-z-developers-again.md) My 2018 book for young developers, 60% done, its outlines since written here as articles, and an AI edition, dated October 2026, made first.
- [Bringing my past work back: a daily worker that turns eighteen years of essays, talks, posts and tools into linkable articles, and why every team needs one](bringing-my-past-work-back.md) A daily worker that turns eighteen years of essays, talks, posts and tools into linkable articles: then and now, connected, two or three a day.
- [Portugal and Europe, 2025: five essays on Portuguese as a programming language, an open-source sovereign cloud, regulation as graphs and Europe's chance in GenAI, and how they read a year and a half later](portugal-and-europe-2025.md) Five 2025 essays on Portuguese as code, a sovereign open-source cloud, regulation as graphs and Europe in GenAI, read again: two moved, one did not.
- [Books from articles: why my books stall at 95%, why these articles do not, and a plan to turn them into books by Web Summit](books-from-articles.md) My books stall at 60 to 95%; these articles do not. The hypothesis: a book is an ordered set of finished articles, tested by Web Summit in November.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 148 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=148)

**Posting this article on LinkedIn?** The cover is [the-graphs-books.jpg](banners/the-graphs-books.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-graphs-books.html)*
