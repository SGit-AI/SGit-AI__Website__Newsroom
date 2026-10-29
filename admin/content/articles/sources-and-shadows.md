---
title: Sources and their shadows: the licence, the access, the links and the quotes of every reference, how a paywalled article can be seen through what others say about it, and paying the sources we use
date: 2026-10-25
author: Dinis Cruz
author_url: about/index.html
summary: The PHP story is where this newsroom explores, and this newsroom is where the lessons settle: the wires here, the Industry Wire, AWS, OWASP and Portugal, will become more effective with what the PHP agents are learning. One lesson is about references. Every source a story uses comes with a set of primitives worth recording: its licence (Creative Commons, Wikipedia's share-alike, or all rights reserved), its access (open, behind a bot challenge, behind a paywall), its links, its quotes, its quality, and its history. The PHP site's source watch already records the access and keeps the history: of 913 pages it watches, 735 were open, 59 behind a bot challenge and 15 paywalled. The idea I want to explore is the shadow. When we cannot read an article, we can still read what others say about it. Wikipedia's PHP2Shell article rests 8 of its 39 statements on paywalled sources, including a quote from The New York Times, which its editors could read and we can now cite. From enough shadow you can start to see the article. You can also see where the shadow and the source disagree, and, over time, who did the research and who recycled it. And where we use a source's work, there should be a payment funnel back to it, through the micropayments our readers pay us, especially when the source certifies how we used it.
version: v0.13.73
license: https://creativecommons.org/licenses/by/4.0/
tags: sources, provenance, paywalls, wikipedia, micropayments, wires, article
status: published
---

!shot so-shadow.webp | images/ | Seeing a paywalled article through its shadow: Wikipedia, other outlets, social posts and our own captures around it. | concept

## In short {#in-short}

- **The PHP story explores; this newsroom settles.** The wires here will learn from the PHP agents.
- **Every reference has primitives.** Licence, access, links, quotes, quality, history.
- **Some are already recorded.** Of 913 watched pages, 735 open, 59 behind a bot challenge, 15 paywalled.
- **The shadow of an article is evidence.** Who cites it, what they quote, what they say it says.
- **Wikipedia shows it well.** 8 of 39 statements in its PHP2Shell article rest on paywalled sources.
- **The shadow can disagree with the source.** That is worth catching.
- **Over time, a view of who got it right.** Who researched, who recycled.
- **And a payment back to every source we use,** especially when it certifies us.

## Explore there, settle here {#explore-settle}

This article is for this newsroom, but it comes from the PHP one. Remember that we started experimenting here with the wire: [the Industry Wire](https://newsroom.sgit.ai/wire/index.html), then wires for [AWS](https://newsroom.sgit.ai/wire/aws/index.html), [OWASP](https://newsroom.sgit.ai/wire/owasp/index.html) and [Portugal](https://newsroom.sgit.ai/wire/portugal/index.html), each fed from a vault its agents write to. Since then, the PHP story's agents have gone much further in how they find, capture, check and publish sources. That is the [explorer](https://newsroom.sgit.ai/articles/explorer-coding.html) work. The plan is to bring what they learn back here, to make this newsroom the villager, and to make our wires a lot more effective. This is one of those lessons.

## What every reference should carry {#primitives}

!shot so-primitives.webp | images/ | What every reference should carry, recorded at each capture: licence, access, links, quotes, quality, history and payee. | concept

When a story has a reference, it already comes with a set of primitives that are quite interesting.

**The licence.** What the material is published under. At one end, Wikipedia and the other commons, and bloggers who release their work under Creative Commons, as I do here. At the other, a page that is free to read on a website but whose content is all rights reserved. The licence decides what we may quote, copy and republish.

**The access.** Can we read it? Wikipedia, yes. Most public websites, yes, even the ones full of ads. Some sit behind a bot challenge, some behind a login, and some behind a paywall. Our focus is to use only the access we are entitled to, because what we want, eventually, is to pay every one of them.

The PHP site's [source watch](https://php.oct.2026.newsroom.sgit.ai/vaults/source-watch/index.html) already records the access of every page it watches, every time it looks. Of 913 pages from 597 publishers in 59 countries, 735 served their content to an anonymous browser, 59 served a bot challenge, 61 were down, 8 were gone, 35 were unchecked, and 15 were paywalled: "subscription press we hold no licence for". It also keeps the history: a new snapshot whenever a page changes, 2,946 of them, each with its text, a screenshot and the hashes. What it does not record yet is the licence of each page. That is the first gap.

!shot so-watch.webp | images/ | The PHP site's source watch: a vault watching 913 pages from 597 publishers, keeping a snapshot when content changed. | screenshot

**The links and the quotes.** For every page we track, we should also track every link on it and every quote it makes. And, the other way round, every page that links to it and every quote taken from it. Take a BBC story: a whole set of other sites will quote it. We should track the quotes, and what they say about the story.

**The quality.** Of the information, and of the reference. Is it primary, or is it repeating someone else? Did it hold up? Was it corrected, and how?

## The shadow of an article {#shadow}

Here is the interesting part. Depending on what it is, we might be able to use that information.

Say Wikipedia links to an article behind a paywall. The Wikipedia editors could read it, and they quote it. Now we can use that quote ourselves, referenced to them, and see the flow. And from the shadow of an article, we can start to see the real article: if enough references to it say what it says, together they give a good understanding of it.

The PHP site has just made this measurable. Its ontologist now reads [Wikipedia's PHP2Shell article](https://php.oct.2026.newsroom.sgit.ai/wikipedia/php2shell/index.html) as a graph: one statement per sentence, each joined to the references it cites. At the latest revision it read, 8 of its 39 statements rest on references from The New York Times, The Wall Street Journal, the Australian Financial Review and The Atlantic, all of them subscription titles. One of those statements is a quote: "Coverage in The New York Times said that PHP was "pervasive" and speculated that "everyday users" could have their personal data put at risk." Another, from the Australian Financial Review: "The Internet Archive briefly shut down to fix the issue." We have not read either article; we can still cite what Wikipedia's editors said they say, and say so.

!shot so-refs.webp | images/ | Every reference in Wikipedia's PHP2Shell article as the PHP site reads it: 43 references at revision 1381798757. | screenshot

Of the article's 43 references, 16 are pages the site's evidence vault already holds; the rest are requests to the collectors. A reference we hold is evidence we can cite as our own, with the capture's hash. A reference we cannot read, because we have no licence, is still a node in the graph, with its shadow around it.

## When the shadow disagrees {#disagree}

The shadow is also where inconsistencies show. Is a comment relevant to what the page actually says? Or is it picking up one specific point, while the article has other, more interesting ones? Does the quote match the source when we can see the source? Has the source changed since it was quoted?

That last one is not hypothetical. On 24 October the PHP site's correspondent caught that Sansec's own post had changed between two captures: on 22 October it compared the flaw to Heartbleed and said default configurations were vulnerable; on 23 October, both were gone. Anyone who had quoted the first version was now quoting something the source no longer says. Because we keep a copy of every capture, we can go back, and see historically how it unfolded.

## Who got it right {#who-got-it-right}

Put it all together, and we start to have an informed opinion on the accuracy of a lot of this reporting, and on how it evolved: who got it right, who did not, who did the research, and who was recycling information. That is not a ranking we assign. It is a record that builds up from the captures, the quotes and the corrections. The PHP site's Wikipedia section says the same of its own aim: in time, a source's trust shown by how often its statements are corrected, rather than assumed.

## Paying the sources we use {#paying}

The commercial model follows from the primitives. When we use a source's data for something, and we have the evidence of exactly what we used, there should be a payment funnel back to that source, through the [micropayments](https://newsroom.sgit.ai/economics/micro-and-nano-payments.html) we charge our own readers. This site's economics pages already argue that the value behind a reader's payment belongs mostly to the [people who produced the facts](https://newsroom.sgit.ai/economics/paying-the-fact-creator.html), not to the outlet that distributed them.

It works best where the source also [certifies how we used it](https://newsroom.sgit.ai/articles/signed-by-the-source.html): a source that signs our representation of its work is worth paying more, because that is the check that scales. And for paywalled sources, it gives us a way in that we would choose: not to read around the wall, but to pay through it, per use, for what we actually cite.

## What we will bring here {#here}

For this newsroom's wires, the first steps are small:

- **Record the licence and the access** of every source each wire uses, on every capture.
- **Keep the links and the quotes** of every page, in and out, as a graph the wire's agents can read.
- **Mark the shadow** when a source cannot be read: who cites it, what they quote, with the quote's own source.
- **Flag the disagreements** between a quote and its source, and between two captures of the same page.

## What this does not claim {#limits}

- **Licences are not recorded yet,** on the PHP site or here; access and history are.
- **A shadow is not the article.** A quote through Wikipedia is Wikipedia's reading of it, and is cited as such.
- **"Paywalled" is the watch's classification** of 15 pages at its last export, on 23 October; it changes.
- **The payment funnel is a design.** No source is paid through it today.
- **Who got it right is a record to build,** not a verdict anyone has yet.

## Where this comes from {#sources}

My voice memo of 25 October 2026. The PHP story site at release v0.19.4, read on 25 October: [the source watch](https://php.oct.2026.newsroom.sgit.ai/vaults/source-watch/index.html) and its export `data/source-watch.json` (access counts and classes, from the export of 23 October); [Wikipedia's PHP2Shell article as a graph](https://php.oct.2026.newsroom.sgit.ai/wikipedia/php2shell/index.html), its [references](https://php.oct.2026.newsroom.sgit.ai/wikipedia/php2shell/references/index.html) and `data/wikipedia/php2shell/graph.json`, at revision 1381798757; [the journalist's desk](https://php.oct.2026.newsroom.sgit.ai/views/desk/index.html) for the Sansec captures; its screenshots under its Apache-2.0 licence. Wikipedia's text is CC BY-SA 4.0, by its contributors. Related: [signed by the source](https://newsroom.sgit.ai/articles/signed-by-the-source.html), [on the record](https://newsroom.sgit.ai/articles/on-the-record.html), [free to copy, paid at the source](https://newsroom.sgit.ai/articles/free-to-copy-paid-at-the-source.html), [pay after you read](https://newsroom.sgit.ai/articles/pay-after-you-read.html), [who signs for this?](https://newsroom.sgit.ai/articles/who-signs-for-this.html), [PHP October 2026, update 3](https://newsroom.sgit.ai/articles/php-daily-2026-10-24.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
