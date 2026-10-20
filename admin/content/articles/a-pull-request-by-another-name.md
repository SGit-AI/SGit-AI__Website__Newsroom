---
title: A pull request by another name: the book reviewed chapter by chapter, the principles it should follow, and seven patches in a vault
date: 2026-10-19
author: Dinis Cruz
author_url: about/index.html
summary: This morning I am reading the printed release candidate 2 of Generation ZX Developers, with a pen. At the same time, I asked the newsroom's agent to review the same text, chapter by chapter, in my voice, and not just to list problems but to fix them, work out the principles behind the fixes, suggest how the book should be paced and ordered, and bring over what works on this site, including a way to draw the book itself. Six editors worked in parallel, one per part, under one brief whose first rule was never to invent anything. They found that the book's main problem is that it repeats itself: the same story, quote or number told in two to four chapters. They found the point of a chapter often came after the 2018 book or a tour of later parts, that some chapters were their newsroom articles pasted in, and that the company part has five chapters of hypotheses and no result. The fixes come as seven patches, in priority order, that take the book from 74,666 to 64,351 words, still above 200 pages. The seventh exists because a review in parts drops things between the parts. It is all in a vault, because the agent does not have write access to the book's repository and does not need it: a patch is the change, and applying it is the decision. A pull request by another name.
version: v0.12.127
license: https://creativecommons.org/licenses/by/4.0/
tags: books, gen-z-book, writing, review, vaults, article
status: published
---

!shot gb-printed.webp | images/ | Release candidate 2, printed and spiral-bound on a café table, with a pen for marking it up: Generation ZX Developers, GenAI Startup Edition, release candidate v2.0.0-rc2, 19 October 2026, page 1 of 168. This is the copy I am reading this morning, while the agents read the same text. Photographed by Dinis. | photo

## In short {#in-short}

- **Two reviews at once.** I read the printed book; the agents reviewed the same text.
- **Not a list of problems.** Fix them, then name the principles behind the fixes.
- **Six editors, one brief.** One per part, and the first rule: never invent anything.
- **The book repeats itself.** That is most of the cut: 74,666 words down to 64,351.
- **The point should come first.** Not the 2018 book, and not a tour of later parts.
- **Seven patches, in priority order.** The seventh fixes what fell between the parts.
- **The book, drawn as itself.** A graph of the chapters, for the back cover.
- **A vault, not a pull request.** A patch is the change; applying it is the decision.

## Reading it twice {#reading}

This morning I am reading the book. Release candidate 2 is printed and spiral-bound, 168 pages, and I am going through it with a pen, the way I read anything I care about. [Discovering the book](/articles/discovering-the-book.html) told the story of how it was written in one evening; this is the first time I have held it.

At the same time, I asked the newsroom's agent to read the same text. Not to tell me whether it was good, but to do the work an editor does: go chapter by chapter, propose the changes, make the ones that only need cutting and reordering, and then reverse engineer them into a set of principles the book should follow and the guidelines to check them. Then make suggestions about pacing and structure. And take what works here, the graphs, the altitudes, the visualisations, and see what the book could use, including whether one of those visualisations could represent the book itself, on the cover or on the back.

## Six editors and one rule {#editors}

The agent split the book into six parts and gave each to an editor working in parallel: the opening, the frame and the job, working with agents and judgement, the company, building without a server and the long game, and the hands-on part. Each one read the newsroom's description of my voice and three recent articles of mine, then their chapters in full.

The brief had one rule above the others: never invent a fact, a number, a quote, a name, a date or a story. They could cut, reorder, merge, tighten and rephrase. If a chapter needed something only I could supply, it became a question for me, not a sentence in the book. They kept every "For Dinis" note, kept every quotation exactly, and wrote a note for every chapter and one for each part: what works, what did not sound like me, what they changed, what they would change but could not, and the figures the chapter needs.

## What they found {#found}

The main finding is that the book repeats itself. Each chapter was drafted from the register of ideas and from the newsroom articles, and each one retold what it needed. So the 2018 *Be a founder* answer is told in chapter 1, again in 17 and again in 11. The habit of one session per topic appears, nearly word for word, in four chapters. The six-line email policy is in 13 and again in 30. "Users buy credits, test once, and don't come back" is in 5, 14 and 18. None of these is wrong on its own. Together, they are why a book that should be short and punchy was not.

!shot rp-patches.webp | images/ | Seven patches, in priority order. Body words before and after for each part of release candidate 2: the opening, 11,120 to 8,982; hands-on 2026, 11,326 to 9,425; the frame and the job, 14,357 to 12,145; agents, judgement and how it was made, 11,085 to 9,986; building without a server and the long game, 15,134 to 13,320; the company, 11,644 to 10,347. The seventh patch works across the parts. The whole book goes from 74,666 to 64,351 words, about 215 pages, above the 60,000-word floor. | comparison

The second finding is about where the point is. "You are lucky to be here", which is the core idea of the book, first appeared in the eighth paragraph of chapter 2. Chapter after chapter opened well, then turned to the 2018 book, or the method, or a tour of later parts, before the argument landed. In the last two argument parts, three chapters, 25, 26 and 29, opened with the 2018 book.

The third is that some chapters were their articles. Chapter 11 shared 831 words with [act as the job you want](/articles/act-as-the-job-you-want.html), in the article's order. A chapter can keep an article's quotes and its best lines, but it needs its own spine; 11 now has one, and the overlap is 477 words, mostly the quotes.

The fourth is one I am glad they raised. Two chapter titles named my products, "Privacy by design: SG/Send, sgit, and the value of constraints" and "Controlling your agent: RiskMandate". A book for founders should not read as a pitch. The rule they applied is a good one: the idea first, the product second as an example, and my stake declared at the first mention.

And the fifth is the one only I can fix. *Start the company* has five chapters of strong argument, each careful to say what is still a hypothesis, and then a placeholder. That reads as a company not yet started, which is the opposite of what the book promises. It needs a result, a company from registration to first payment with dates, and the countries. The editors wrote those down as seven questions for me.

## The hands-on part {#hands-on}

The clearest numbers are in the hands-on part. The editor measured how much of each hands-on chapter was also in the chapter it follows, in runs of six words. Chapter 30, the agentic workflow from zero, was 49% chapter 13; chapter 39, the first price and first ten customers, was 37% chapter 19. After the edit, an argument chapter argues and a hands-on chapter instructs: it opens with what you will have, points back in one line, gives the steps, and ends with what you have at the end.

!shot rp-overlap.webp | images/ | Argument chapters argue; hands-on chapters instruct. The share of each hands-on chapter's six-word runs also found in the earlier chapter it follows, before and after the edit: chapter 30 against 13, 49% to 22%; 39 against 19, 37% to 10%; 33 against 7, 20% to 3%; 32 against 7, 18% to 4%; 35 against 16, 16% to 3%; 37 against 22, 13% to 7%; 36 against 12, 11% to 1%. | comparison

They also suggest moving them. Today the eleven hands-on chapters sit together at the end. Interleaved, each would be the last chapter of the part it serves, still marked 2026 and listed on one index page so it can be renewed each year. That way you read *Price it, then give it away* and then you price it. I like that. It fits something I said in [zoom in, not discover](https://gen-z-developers.sgit.ai/articles/zoom-in-not-discover.html), which the book's own team published this morning while the review was being put together: the book is a manual, not a journey, and you learn by doing.

## What fell between the parts {#between}

There is one finding about the review itself that I think matters as much as any finding about the book. Two editors, working at the same time, each cut the same passage. The editor of chapter 12 cut the steps for setting up your own newsroom and pointed to chapter 36. The editor of chapter 36 cut the same steps and pointed to chapter 12. Each pointer was correct when it was written. Together, they left the steps in neither chapter.

!shot rp-hole.webp | images/ | A hand-off is only done when the other side has it. Chapter 12's editor cut the five steps and pointed to chapter 36; chapter 36's editor cut the eight steps and pointed to chapter 12. The steps were left in neither. Patch 0007 puts the eight steps back in chapter 36, where the hands-on part instructs, and chapter 12 keeps the why. | concept

That is why there is a seventh patch. After the six editors finished, the agent did a pass across the parts: every passage that had been cut and replaced with a pointer was checked against the chapter it pointed to. That pass found the missing steps, and four citations of chapter 25's old title. It is the same lesson as running agents in parallel anywhere: the work in each lane can be right and the whole still be wrong, so the join needs its own check.

## The principles {#principles}

The part I asked for most was the reverse engineering: what principles were the editors following, without being told to? There are thirteen in the vault, each with a guideline. The ones that matter most:

1. **One home per idea, story, quote and number.** Told once, in full, in the chapter that owns it; everywhere else, one sentence and the chapter's title.
2. **The pointer says what is there.** Not "see chapter 14", but the idea in a clause and the title.
3. **A hand-off is only done when the other side has it.** A register of homes makes that a lookup.
4. **The point first, the story last.** My story and the 2018 book go at the end of a chapter, for whoever wants them.
5. **A chapter is not its article.** Above about 20% shared with its source article, it has been pasted, not written.
6. **Idea, example, stake.** No product names in chapter titles.
7. **Co-writing on the first page.** It was only in the last chapter. Now the front page says the book is co-written with Claude, and what is mine and what is the agents'.

Several of these are what [short, punchy and co-written](/articles/short-punchy-and-co-written.html) asked for, now with a way to check them: every paragraph knowing what it is, and a graph showing where we repeat ourselves.

## The book, drawn as itself {#cover}

I asked whether one of the visualisations could represent the book. The proposal is a graph: the 41 chapters in a ring, in reading order. Each dot is sized by the number of ideas the chapter is written from and coloured by its part. A line joins two chapters that stand on three or more of the same sources. It is drawn by code from the same front matter the book's build checks, so when the book changes, the picture does.

!shot rp-cover.webp | images/ | Generation ZX Developers, the book as a graph: a proposal for the back cover. 41 chapters in a ring, sized by their ideas, 198 in all, and coloured by their part. 50 lines join chapters that share three or more sources. The argument chapters form a dense web; the hands-on chapters are barely joined to it, with 14 of the 50 lines, and eight of them name no ideas at all. Drawn by code from release candidate 2's front matter. | concept

And it shows something the text hides. The argument chapters are a dense web. The hands-on chapters are barely connected to it: 14 of the 50 lines touch them, and eight of the eleven name no ideas at all. That is the same thing the book's team found with its own graph test this morning, from the other direction. When the hands-on chapters are joined to the parts they serve, the back cover will show it. I like a cover that changes when the book gets better.

The other ideas from this site are in the vault too. Altitudes: one line for the book, one paragraph per part, one line per chapter, each checked against the text below it and marked stale when that text changes, which is what this site does with its summaries. Versions with their diffs, so a reader of the next candidate can see what changed in each chapter and why. A review record where every finding is fixed, declined or open. And, at the end of each chapter, what it does not claim and where it comes from.

## Why a vault and not a pull request {#vault}

I asked if the agent could make a pull request against the book's repository, or whether I needed to give it permission. It does not have write access there, and it did not need it. A pull request is a set of patches with a conversation around it. So the review went into an [sgit vault](/articles/research-delivered-as-a-vault.html): the seven patches made with git, the chapters with the patches applied so they can be read without git, the principles, the structure, the visuals, and the 48 notes. Encrypted, versioned, and shared with a read key.

That keeps the decision where it belongs. The agent proposes; whoever applies the patch accepts it. I can take all seven, take the first and leave the rest, or take none. And like every review on this site, each finding needs an answer, and "we are not doing that", with a reason, is one of the answers.

## What happens next {#next}

I will finish reading the printed copy, mark it up, and compare my marks with the patches. Where we agree, the patches go in. Where we do not, that is a finding about the review. Then I owe the book the seven answers only I have, starting with the company: one result, one company from registration to first payment, and the countries. That is the part the synthetic readers said would make them buy it, and it is the part that still needs me.

## What this does not claim {#limits}

- **The review is an editor's reading, not mine.** Every change is a proposal until I sign it off.
- **The patches have not been applied.** They are in the vault, against the book at v0.2.34.
- **The book's build was not run on them.** Its checks on front matter and banned words were run separately and pass.
- **The overlap figures are the editors' measurements.** Six-word runs shared with one earlier chapter; eight-word runs for chapter 11.
- **Word counts are chapter bodies**, without front matter, for release candidate 2.
- **Rc3 will not look like this.** The book's team has its own brief for it, and these patches are one input.

## Where this comes from {#sources}

A voice memo from me on 19 October 2026, and my photograph of the printed release candidate. The book's source, release candidate 2, at [gen-z-developers.sgit.ai](https://gen-z-developers.sgit.ai/), repository [SGit-AI/SGit-AI__Website__Gen-Z-Developers](https://github.com/SGit-AI/SGit-AI__Website__Gen-Z-Developers), at its release v0.2.34, read in full. [Zoom in, not discover](https://gen-z-developers.sgit.ai/articles/zoom-in-not-discover.html), from the book's site. Related: [discovering the book](/articles/discovering-the-book.html), [short, punchy and co-written](/articles/short-punchy-and-co-written.html), [a website to finish the book](/articles/a-website-to-finish-the-book.html), [Generation Z Developers (AI edition)](/articles/generation-z-developers-again.html), [act as the job you want](/articles/act-as-the-job-you-want.html), [research, delivered as a vault](/articles/research-delivered-as-a-vault.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
