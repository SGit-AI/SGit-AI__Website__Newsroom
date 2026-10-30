---
title: A book that looks like the team that made it: what the best visual books, Leanpub's Markua and learning research teach, and what an agent team can put on a printed page
date: 2026-10-30
author: Dinis Cruz
author_url: about/index.html
summary: The talk I gave at hack::soho looked like it was made by an agent team: a custom player, its own navigation, and animations everywhere, each one made to drive a point home. The book of the talk has to do the same, or the medium contradicts the message. But a book that goes to Leanpub and to print on demand has only text, images and a little layout. So before designing it I asked for research: what the best visual books do, what Markua (Leanpub's markdown) and Amazon's print service allow, and what the research on learning says about pictures and words. The findings are clear. Markua gives more than I expected: images sized as a share of the page, floated toward or away from the spine, or full bleed; numbered figures with captions; SVG and Mermaid diagrams kept as text; and seven kinds of typed box, for tips, warnings, questions and exercises. The limits are mostly cost and craft: no raw HTML, no text on both sides of an image, and colour printing that costs from about twice to more than five times as much per page as black ink. Richard Mayer's experiments rate pictures with words at an effect size of 1.39 and putting the words next to the picture at 1.09, and show that decoration hurts. Retrieval practice and spacing are rated the most useful study techniques. The best books, from Edward Tufte's to Julia Evans's zines, Simon Wardley's maps and Bob Nystrom's Crafting Interpreters, apply these by hand. An agent team can apply them by machine: one visual grammar across every figure, each figure a spec that can be rerun when I change my mind, animations turned into filmstrips, every number tied to the register, and questions to remember by. This article sets out what we found, and the plan for the book.
version: v0.14.3
license: https://creativecommons.org/licenses/by/4.0/
tags: books, publishing, leanpub, markua, infographics, learning, visual-explanation, agent-teams, the-ultimate-insider, article
status: published
---

!shot nb-filmstrip.webp | images/ | An animation from the talk as three stills: what a moving slide becomes on a printed page. | process

## In short {#in-short}

- **The book has to look like the team that made it.** If a book made by agents looks like every book before it, the medium contradicts the message.
- **The page gives us text, images and a little layout.** Markua and Amazon's print service allow more than that sounds like, and limit it mostly by cost.
- **The learning research is clear on pictures.** Words with pictures, placed together, without decoration, teach better than words alone.
- **The best visual books already do this by hand.** Tufte, Head First, Wardley, Evans, Nystrom: one grammar, words on the drawing, every figure earning its place.
- **An agent team can do it by machine.** Every figure a spec, rerun on request, held to one grammar, its numbers tied to the register.
- **An animation becomes a filmstrip.** The talk's motion pieces were already captured as stills at named seconds.
- **The plan:** a cast of concepts up front, one map grammar, filmstrips, call-outs mapped to Markua's boxes, greyscale first, and questions to remember by.

## Why a book has to look like its workflow {#signal}

The talk I gave on 29 October did not look like a normal presentation. It had its own player and navigation, and almost every slide was a live web page with its own animation, made by a team with a motion designer and a studio of Ruflo runs. I think that matters beyond taste. If I stand up and say a talk was made by an agent team, and it looks like every talk before it, maybe a bit better, the audience has no reason to believe that anything has changed. The look is the signal.

The book is the same problem with fewer tools. A book is a teaching aid: its job is to move concepts from my head to a reader's, and most of what I am explaining is concepts and ideas, not procedures. So I did not want to start from the conventions of the last book I read. I wanted to start from what is known: what the best visual books do, what the platform allows, and what the research on learning says works. This article is that research, done by an agent at my request on 30 October, and what we will do with it.

## What the page allows {#page}

The book will be written in Markua, the markdown that Leanpub uses, and sold on Leanpub as PDF and EPUB, then printed on demand through Amazon's Kindle Direct Publishing (KDP).

!shot nb-markua.webp | images/ | What Markua and print on demand allow, and what they do not, from the Markua spec and KDP's help pages. | comparison

**Markua gives more than "text and images".** The specification, version 0.31.50 of 11 August 2026 (Leanpub's default is still Markua 0.30, in beta), lets an image be sized as a percentage of the page's content area, aligned, floated left or right, or floated "inside" toward the spine or "outside" away from it, or set full bleed, "the full size of the page, with no margins". An image's title becomes a numbered caption. A code block fenced as `svg` or `mermaid` "is rendered as an image by default", so a diagram can live in the manuscript as text that can be diffed and reviewed. There are asides that can run across pages and short boxes typed by letter: discussion, error, information, question, tip, warning and exercise, which Leanpub draws with an icon. Tables can come from CSV files, and code can be cropped from real files.

**And it says plainly what it does not do.** Raw HTML is "completely removed". A page break exists but "the use of this directive is discouraged. Authors should spend their time writing, not formatting." And: "Markua is not a good choice for the types of advanced layouts which flow text on both sides of an image. For that, you should use something like InDesign".

**Print adds its own rules.** KDP asks for images of at least 300 DPI and calls anything under 200 low resolution; transparent layers must be flattened. Bleed is all or nothing: "Even if just one page in your interior requires bleed, then your entire file should be set up with bleed." The inside margin grows with the page count, to half an inch for a book of 151 to 300 pages. RC1 is 6 by 9 inches, which KDP calls "the most common trim size for paperbacks in the U.S."; Leanpub moved its own default to 7 by 10 in December 2024.

**The real constraint is colour.** KDP's print cost is "Fixed cost + (page count * per page cost)". On a regular trim, black ink costs 1.2 cents a page, standard colour 2.55 cents and premium colour 6.5 cents, and the ink cannot be changed after publication. So the figures must work in greyscale, and colour is a choice we make once.

!shot nb-ink.webp | images/ | KDP's print cost per page by ink and trim, in US cents, from its help pages read on 30 October 2026. | chart

## What the best visual books do {#best}

The research looked for books known for how they explain with pictures, and asked of each technique whether it survives on a printed page.

- **Edward Tufte**: small multiples (the same small chart repeated to compare), sparklines the size of a word, and no chart junk. Made for print.
- **Head First**, the series Kathy Sierra and Bert Bates started in 2003: visual, conversational, words placed inside or next to the pictures, deliberately odd. It survives print but needs a designer's layout tool; Markua can only approach it.
- **Simon Wardley's Wardley Maps**, on Leanpub under a Creative Commons licence: one map grammar, repeated until the reader reads it without thinking. RC1 already uses it, with sixteen maps.
- **Simon Brown's C4 model**, also on Leanpub: a whole book about one diagram notation.
- **Julia Evans's zines**: "Each of these zines is 20-28 pages. I spend hours on each page making sure that every single one explains one or two important ideas as succinctly and clearly as I possibly can."
- **Randall Munroe's Thing Explainer**: hard subjects with only the thousand most common words, a constraint a machine can check.
- **Scott McCloud's Understanding Comics**, a book about comics written as a comic: sequential panels, which suit a process like an agent's hand-off.
- **Martin Fowler's duplex book**: a narrative part read cover to cover and a reference part "to be dipped into when needed", with his rule of thumb that "200 pages is the limit for a narrative cover-to-cover technical book."
- **Bob Nystrom's Crafting Interpreters**: "The ultimate goal for me is a print book, so I stuck with black and white ink." He drew every illustration by hand against an x-height guide, with "a pair of registration marks a fixed distance apart", and his build tested every code sample in the book: "I could automatically verify that the code that I was showing readers did exactly what I expected."
- **Quantum Country**, by Andy Matuschak and Michael Nielsen: "Embedded within the text of the essay are 112 questions", reviewed on a schedule, so that reading becomes remembering.

The pattern is that the best of these do by hand, with great effort, what a pipeline does by default: one grammar, consistent drawings, tested examples. Nystrom's registration marks are a case in point: that is the work an agent team does not get tired of.

## What the learning research says {#science}

Most of the research on pictures and words in teaching comes from Richard Mayer and his colleagues, summarised in *Multimedia Learning* (Cambridge University Press, second edition, 2009). Each principle was tested in experiments that compared a lesson with and without it.

!shot nb-mayer.webp | images/ | Seven of Mayer's principles, with the median effect size in his studies, and what each means on a page. | chart

- **Multimedia:** "People learn better from words and pictures than from words alone." Eleven tests out of eleven, a median effect size of 1.39, and stronger for readers new to the subject.
- **Spatial contiguity:** "Students learn better when corresponding words and pictures are presented near rather than far from each other on the page or screen." 1.09. On a page, this means labels on the drawing, not in a legend, and the figure beside the paragraph about it.
- **Coherence:** "People learn better when extraneous material is excluded rather than included." 0.97. Other studies, of so-called seductive details, find that interesting but irrelevant pictures and asides lower what readers learn.
- **Segmenting:** a message in pieces the reader paces, 0.98. On a page: one idea per figure, steps as panels.
- **Pre-training:** "People learn more deeply from a multimedia message when they know the names and characteristics of the main concepts." 0.85. On a page: introduce the cast of concepts before the story uses them.
- **Personalisation:** conversational words rather than formal ones, 1.11. That is the first-person voice the book's first companion card asks about.

These effect sizes come from short lessons in Mayer's own studies, so they are an upper bound, not a promise. Two more findings matter. A review by Weinstein, Madan and Sumeracki (2018) explains that combining words and pictures works because pictures are more memorable than words, and that this is "distinct from the notion of 'learning styles'", which "is not supported by empirical findings". And Dunlosky and colleagues (2013), rating ten study techniques, found that "Practice testing and distributed practice received high utility assessments", while rereading and highlighting were rated low. A book that asks questions, and asks them again later, teaches more than one that is only read.

## Where the industry is {#industry}

Publishing is already changing under agents, mostly at the edges. Leanpub sells AI tools to authors, among them one that "adds AI-generated alt text to every image in your Leanpub book" and an index generator. Amazon, in 2023, limited self-publishers to three new titles a day, according to the Authors Guild: "KDP confirmed this number with us". The flood that prompted it is the opposite of what I want: books made cheaper, not books made better.

The other trend is older and more useful: books that version like software. Leanpub's readers "get free updates, regardless of when they bought the book or how much they paid". Pro Git is open source and takes corrections from its readers. Quarto, Bookdown, O'Reilly's Atlas and Pandoc all build a book from source files in a repository into several formats. RC1 is already one of these: a release with a version, a hash and a build that reproduces it to the pixel.

## What an agent team adds {#agents}

None of the techniques above is new. What is new is that the cost of applying all of them, to every figure, every time, has fallen to almost nothing, and that a figure can be changed by asking.

- **Every figure is a run with a spec.** In the talk, ruv.sgit made 25 runs on the day, each with a spec that quotes its request, an evidence file naming the source of every number, and a note for me. A book's figures can be made the same way, so that each one can be traced, checked and remade.
- **A change is a request, not a redraw.** At 18:25 on the day of the talk I told the motion member that the gap between people and agents in its first animation was too exaggerated. At 18:29 the changed piece was on dev, with an explainer. A publisher could not have offered that; an illustrator would not have.
- **The grammar is enforced, not hoped for.** RC1's infographics already follow a written visual language: one dark ink and one accent, nothing under about 9 point at the printed size, the claim id on the image, and a renderer that refuses text that runs off the canvas or overlaps. That is Nystrom's registration marks, done by a checker.
- **An animation becomes a filmstrip.** The motion member checked every piece by capturing stills at named seconds, such as 22, 31 and 43 seconds into the first piece. Those stills are the print form: three frames in a row, read left to right, are a small multiple of the animation, and a QR code beside them can open the moving version.
- **Reviews become decisions.** RC1's companion turned 98 review points into cards pinned to pages, with boxes to tick. The same pipeline can check every figure against the research: does it have words on it, is it next to its paragraph, does it teach or decorate?

## The plan for the book {#plan}

This is what we will build into the book of The Ultimate Insider, and test in the next release candidate:

1. **A cast of concepts up front.** The ultimate insider, a mandate, a boundary, the five-step wake, a hold: each named and drawn once before the story uses it (pre-training).
2. **One map grammar.** The Wardley maps stay, simplest first, with the chapter on how to read one before them.
3. **Filmstrips from the talk.** Each animation that carries an argument appears as three to five stills in a row, with a short URL or QR code to the moving version on the talk's site.
4. **Words on the drawing.** Labels inside the figure, the figure next to its paragraph, captions that say what the image is (spatial contiguity).
5. **Call-outs mapped to Markua's boxes.** RC1's five kinds (concept, the number, take away, watch out, try this) become Markua's information, tip, warning and exercise boxes, so they survive into Leanpub's PDF and EPUB.
6. **Greyscale first.** Every figure checked in greyscale by the pipeline; meaning carried by shape, position and words, never by colour alone.
7. **No decoration.** A figure that does not teach something is removed (coherence).
8. **Questions to remember by.** A few questions at the end of each chapter, asked again later in the book, with an online deck for spaced review (retrieval practice).
9. **Every number with its id,** on the figure as in the text, so any reader can rerun it.
10. **Every figure a spec,** kept in the repository with its source and its renderer, so that changing my mind costs a sentence.

And the book will be shared: the repository, the figures' specs and this research are public, so anyone writing a book can copy what works.

## What this does not claim {#limits}

- **The research was done by an agent in one session,** from sources it could fetch. Edward Tufte's own site blocked it, so his techniques here come from secondary descriptions; the Head First principles come from a second-hand summary, so they are paraphrased, not quoted.
- **Mayer's effect sizes** come from short lessons in his own laboratory and are upper bounds; a book chapter is not a five-minute lesson.
- **The best Leanpub books** are an editorial choice: Leanpub publishes no ranked list we could check.
- **The print costs** are KDP's rates for Amazon.com on 30 October 2026, before tax, and change.
- **The plan is a plan.** None of it is in RC1 yet beyond the maps, the infographics and the call-outs; the next release candidate will show how much of it works.

## Where this comes from {#sources}

All read on 30 October 2026 by a research agent working for this newsroom; quotations are copied from the fetched pages.

- Markua specification, version 0.31.50 (2026-08-11): [markua.com](https://markua.com/). Leanpub: [the author update for December 2024](https://leanpub.com/blog/the-leanpub-author-update-for-december-2024/); [Leanpub's home page](https://leanpub.com/) for royalties, free updates and the AI tools.
- Amazon KDP help: [trim size, bleed and margins](https://kdp.amazon.com/en_US/help/topic/GVBQ3CMEQW3W2VL6), [images](https://kdp.amazon.com/en_US/help/topic/G202169030), [printing cost](https://kdp.amazon.com/en_US/help/topic/G201834340), [colour ink](https://kdp.amazon.com/en_US/help/topic/GX56BFPW4BKNPGFW).
- Mayer, *Multimedia Learning*, 2nd edition, chapter abstracts on [cambridge.org](https://www.cambridge.org/core/books/multimedia-learning/) (multimedia, coherence, spatial contiguity, segmenting, pre-training, personalisation).
- Weinstein, Madan and Sumeracki (2018), [Teaching the science of learning](https://pmc.ncbi.nlm.nih.gov/articles/PMC5780548/), *Cognitive Research: Principles and Implications*. Dunlosky et al. (2013), *Psychological Science in the Public Interest* 14(1), 4 to 58.
- Julia Evans, [wizardzines.com/about](https://wizardzines.com/about/). Bob Nystrom, [Crafting "Crafting Interpreters"](https://journal.stuffwithstuff.com/2020/04/05/crafting-crafting-interpreters/). Martin Fowler, [Duplex Book](https://martinfowler.com/bliki/DuplexBook.html). Matuschak and Nielsen, [How can we develop transformative tools for thought?](https://numinous.productions/ttft/). Simon Wardley, [Wardley Maps on Leanpub](https://leanpub.com/wardley-maps). Simon Brown, [The C4 model on Leanpub](https://leanpub.com/visualising-software-architecture).
- Authors Guild, [Amazon caps daily self-publishing uploads](https://authorsguild.org/news/amazon-adds-to-kdp-generative-ai-policy-caps-daily-self-publishing-uploads/), 27 September 2023.
- The talk's repository, [SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider](https://github.com/SGit-AI/SGit-AI__Website__Presentation__The-Ultimate-Insider): `team/ruv-sgit/runs/` (25 specs), `team/motion/ROLE.md` and `team/motion/debriefs/` (the stills and the 18:25 change). The book's repository: `team/conductor/rc1/infographics/README.md`.
- Related: [the book of the talk, RC1 and its companion](/articles/the-book-of-the-talk-and-its-companion.html), [the talk built in a day](/articles/the-ultimate-insider-case-study.html).
