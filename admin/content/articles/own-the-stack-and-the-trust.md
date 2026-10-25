---
title: Own the stack, and the trust: a reply to Bert Kok on who gets paid for journalism when AI sits between the newsroom and the reader, with agents that augment journalists rather than replace them, and a tour of what we have built
date: 2026-10-25
author: Dinis Cruz
author_url: about/index.html
summary: Bert Kok's essay for The News Stack argues that AI is separating the production of original journalism from the systems that synthesise it and own the interface, and that publishers may fund the most expensive layer and capture the least valuable. I agree with most of it, and we have been building the parts he describes. His "knowledge architecture", where each story keeps which statements are facts and which are claims, where they came from, when they were checked and what has changed, is what the PHP story site does for php2shell, every claim tied to a dated, hashed capture. His "interface as a sensor" is our feedback loop: one outside collaborator sent three rounds of ideas, and the agents turned them into working features within hours. Two additions. First, agents are not here to replace journalists. What our newsrooms are missing is more journalists, and more readers, because every human in the loop makes the system much better. Second, I disagree that publishers should not own the stack. They should, because the stack is no longer a multi-million investment: I am publishing ours as open source, and others will follow. What publishers must own above all is the reader's trust. That leads to an economic model for local and niche publishers, which I set out in a companion article, and a tour of what we have built, for readers who have not seen it.
version: v0.13.76
license: https://creativecommons.org/licenses/by/4.0/
tags: news, journalism, ai, provenance, open-source, business-models, article
status: published
---

!shot kb-collage.webp | images/ | What we have built, in twelve pages: this newsroom's front page; the PHP October 2026 story site; its state of affairs, versioned; its source watch of 913 pages; Wikipedia's article on the flaw, read as a graph; the control room for its 23 agents; the bridge, a local story kept as a graph; the waiting room that knew first; a desk kept in a vault; the Industry Wire; the World News Day corpus; and Pulse, exploited against talked about. | collage

## In short {#in-short}

- **Bert Kok's essay is right about the shift.** Synthesis and the interface are merging, and the platforms see the questions.
- **We have been building his "knowledge architecture".** Facts and claims, sources, when checked, what changed.
- **And his "interface as a sensor".** Readers' feedback, turned into features within hours.
- **Agents augment journalists; they do not replace them.** What we are missing is more journalists, and more readers.
- **I would own the stack.** It is no longer a multi-million investment; ours is open source.
- **Above all, own the reader's trust.** That is the asset the platforms cannot copy.
- **The economics follow:** [local trust, certified upwards](https://newsroom.sgit.ai/articles/local-trust-certified-upwards.html).

## Bert Kok's argument {#his-argument}

!shot kb-post.webp | images/ | Bert Kok's post on LinkedIn, 25 October 2026, sharing his essay for The News Stack: "Publishers may fund the most expensive layer and capture the least valuable". | small | aside

[Bert Kok's essay](https://www.linkedin.com/pulse/publishers-may-fund-most-expensive-layer-capture-least-bert-kok-mba-lkgif), published in his newsletter The News Stack on 25 October, starts from a new report by the Tow-Knight Center for Journalism Futures at CUNY, [The Three-Layer Cake](https://www.journalism.cuny.edu/2026/10/tow-knight-center-report-journalisms-future-ai-information/), released on 22 October. The report describes three layers: the products that find out what people want to know, the systems that synthesise answers, and the organisations that produce the underlying reporting.

Bert's point is that the top two are converging. ChatGPT, Gemini and Perplexity "don't just synthesize information. They are also the interface." They see the question, pick the sources and watch what the user does next. Meanwhile, "The most expensive part of journalism is still discovering information that doesn't yet exist in the public record." AI makes processing cheap, not discovery. And scarcity alone does not get you paid: "There is no mature market determining how value moves from platforms that synthesize and deliver information back to the organizations financing its original production."

His answer is three capabilities: origination, a knowledge architecture, and, where a publisher can sustain it, a direct relationship with the reader. And he ends with a question I would put to any newsroom too: "If your articles disappeared tomorrow but your verified knowledge and audience relationships remained, would you still have something valuable enough to build products around and negotiate with AI platforms?"

I replied under his post that I have been thinking along very similar lines, and building the pieces. This is the longer answer.

## Where we agree, and what we built {#agree}

| Bert's point | What we have built |
|---|---|
| "A searchable pile of articles is not a knowledge architecture." Keep which statements are facts and which are claims, where they came from, when they were checked, and what has changed. | The [PHP story site](https://php.oct.2026.newsroom.sgit.ai/): every claim points to a source, every source to a dated, hashed capture; a [versioned state of affairs](https://php.oct.2026.newsroom.sgit.ai/views/index.html); a [source watch](https://php.oct.2026.newsroom.sgit.ai/vaults/source-watch/index.html) of 913 pages that keeps a snapshot whenever a page changes, which is how we caught a publisher [rewording without a note](https://newsroom.sgit.ai/articles/the-side-stories-of-php2shell.html). |
| The interface is "a sensor for the newsroom": readers' questions show what to report next. | This newsroom's [search](https://newsroom.sgit.ai/search/index.html) can answer a question only from cited passages, and every article has a [Pen](https://newsroom.sgit.ai/articles/a-pen-and-a-key.html) for readers' notes; the PHP site has an Ask pane, and an agent, the Sherpa, that answers readers' feedback point by point. |
| Publishers need to know who reads their work: humans, crawlers or agents, and to charge some of them. | The PHP site's private telemetry separates readers, the editor, synthetic readers and crawlers; the source watch records whether each page it reads was open, behind a bot challenge or paywalled. |
| No standard way to measure or price a source's contribution. | [Sources and their shadows](https://newsroom.sgit.ai/articles/sources-and-shadows.html): the licence, access, links and quotes of every reference, and who to pay; [signed by the source](https://newsroom.sgit.ai/articles/signed-by-the-source.html). |

## Agents augment journalists; they do not replace them {#augment}

!shot kb-comment.webp | images/ | My reply under Bert Kok's post, 25 October 2026: thinking along very similar lines, building MVPs that show how the data behind a story can be captured, linked and monetised, and this article to follow. | small | aside

I want to be clear about what the agents are for, because it is easy to read this as automation replacing reporters. It is the opposite.

The PHP story is covered by 23 agents. A researcher captures every source; a curator turns the captures into evidence; a journalist agent publishes; a correspondent agent reviews the journalist's work, and on its first pass [caught nine things the journalist had missed](https://newsroom.sgit.ai/articles/php-daily-2026-10-24.html). That pipeline does exactly what Bert says AI does well: processing information that already exists, keeping it structured, current and attributable, at a cost that makes it possible to do continuously.

What it cannot do is what he says remains expensive: discovering what is not yet in the public record. Cultivating a source. Attending the meeting nobody else attends. Knowing which caveat matters. So, honestly, what is missing from our PHP newsroom, and from this one, is more journalists. If they were involved, it would be so much better. The agents would be doing the work that buries journalists today, and the journalists would be doing what only they can.

And more readers. The feedback loop is real, and it is fast. One outside collaborator sent the PHP site three rounds of comments and ideas. The second, five ideas, turned its risk graph into a working tool within hours. The third said the header took too much of a phone's screen: it went from 233 pixels to one 43-pixel line. One person sending feedback changed the product. Imagine a newsroom with thousands.

On the commodity work, I agree with Bert's caution: do not defend production that a machine can do reliably, but do not cut the routine coverage that keeps readers coming back. With agents, you do not have to choose. The routine coverage can be produced, kept current and sourced by agents, and the time it used to take goes into original reporting.

## Where I disagree: own the stack {#own-the-stack}

Bert writes that "for many, owning the full interface may be unrealistic", and that publishers "are unlikely to outperform the largest technology companies at general-purpose synthesis". On synthesis, he is right. On the stack, I disagree. I think publishers should own it.

The reason they could not in the past is that a stack cost millions to build, and they were stuck with whatever they had paid for. That is no longer true. The stack behind everything on this page, the vaults, the capture, the evidence, the agents, the pages, is being published as open source, and anyone can take it. Others will do the same, and companies will provide it as a service. Publishers should leverage us, and the others. Owning the stack is now a matter of choosing, not of spending.

## Above all, own the trust {#own-the-trust}

What a publisher must own, more than any stack, is the reader's trust. That is the one thing the platforms cannot copy, and it is where the value is moving. And it is strongest where a publisher is closest to its readers: local, niche, expert, in their language and their culture.

That is where the economics change. A local or niche publisher that owns the trust can take everything that has become commodity, including the big outlets' global news, and serve it to its readers from their point of view. And it can certify upwards: when a big outlet runs a story about its patch, the local publisher's journalists are the ones who can say it is right, and should be paid for saying so. I have set that out separately, in [local trust, certified upwards](https://newsroom.sgit.ai/articles/local-trust-certified-upwards.html).

## A guided tour, for readers new to this {#tour}

If you have not seen what we have been building, the collage at the top of this page shows the depth better than a list of links, but here is where to start:

- **[PHP October 2026](https://php.oct.2026.newsroom.sgit.ai/).** A live story covered by agents, with every claim tied to its evidence: start with [the state of affairs](https://php.oct.2026.newsroom.sgit.ai/views/state/v3/index.html), then [the source watch](https://php.oct.2026.newsroom.sgit.ai/vaults/source-watch/index.html), then [Wikipedia, read as a graph](https://php.oct.2026.newsroom.sgit.ai/wikipedia/php2shell/index.html).
- **[The bridge, followed to the end](https://newsroom.sgit.ai/articles/the-bridge-followed-to-the-end.html).** A local bridge closure, simulated from the council's first notice to the first car across, kept as a story graph: what one local story is worth when nothing is thrown away.
- **[The waiting room knew first](https://newsroom.sgit.ai/articles/the-waiting-room-knew-first.html).** A live local story, and the gap where local information used to be.
- **[Story vault underneath, Reader Skills on top](https://newsroom.sgit.ai/articles/story-vault-meets-reader-skills.html).** The same conversation with another journalist, Markus Franz, about why local journalism has the most to gain.
- **[The future of news is the story vault, not the paywall](https://newsroom.sgit.ai/articles/future-of-news-story-vault-not-paywall.html).** The commercial model.
- **[The Industry Wire](https://newsroom.sgit.ai/wire/index.html)** and **[World News Day](https://newsroom.sgit.ai/world-news-day/index.html).** Feeds and a corpus kept in vaults, read in the browser.
- **[The control room](https://php.oct.2026.newsroom.sgit.ai/team/control/index.html).** How the agents behind the PHP story are run, and what waits on me.

## What this does not claim {#limits}

- **Bert's essay is quoted from its public page;** the summaries of it are mine.
- **The open-source stack is being published,** not yet packaged for a newsroom to adopt in a day.
- **The agents do not do original reporting.** That is the point of the argument.
- **The feedback examples are from the PHP site,** with one outside collaborator, not thousands.

## Where this comes from {#sources}

Bert Kok, [Publishers may fund the most expensive layer and capture the least valuable](https://www.linkedin.com/pulse/publishers-may-fund-most-expensive-layer-capture-least-bert-kok-mba-lkgif), The News Stack, 25 October 2026, read on its public page; his LinkedIn post and my reply, from screenshots; the Craig Newmark Graduate School of Journalism, [Tow-Knight Center releases new report on journalism's future in an AI age](https://www.journalism.cuny.edu/2026/10/tow-knight-center-report-journalisms-future-ai-information/), 22 October 2026; my voice memo of 25 October 2026. Related: [local trust, certified upwards](https://newsroom.sgit.ai/articles/local-trust-certified-upwards.html), [sources and their shadows](https://newsroom.sgit.ai/articles/sources-and-shadows.html), [signed by the source](https://newsroom.sgit.ai/articles/signed-by-the-source.html), [the side stories of php2shell](https://newsroom.sgit.ai/articles/the-side-stories-of-php2shell.html), [PHP October 2026, update 3](https://newsroom.sgit.ai/articles/php-daily-2026-10-24.html), [why agent loops are hard](https://newsroom.sgit.ai/articles/why-agent-loops-are-hard.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
