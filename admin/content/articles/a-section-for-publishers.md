---
title: A section for publishers: where to send someone new to this newsroom, and a site that keeps itself current
date: 2026-10-18
author: Dinis Cruz
author_url: about/index.html
summary: Where do I send a publisher who has never read anything on newsroom.sgit.ai? The publishers page is a good distillation, but it was written once, and this site changes most days: some of what a publisher would care about most, like the way an article now folds away the sections you have already read, shipped in the last few days. So the newsroom now has sections, and the first is for publishers. A section is the newsroom as one audience reads it: five pieces to start with, chosen by the editor; the latest pieces for that audience; the features they can use today, each with when it shipped; and every relevant article, placed into streams by rule, each saying which rule placed it. Nothing on the page is listed by hand except the five to start with. The placement uses the desks and controlled subjects the site already gives every article, and a new register of features, updated in the release that ships each one. So a new article about paying for news lands in the publishers' section on the day it is published, and a new feature appears there as it ships. Building it also showed where the classification is still loose: one subject swept up history talks as journalism, and another was broad enough to pull in a dark mode. Those are fixed by rule, in the open, with the reason written down. Sections for security leads, builders and investors can follow the same pattern.
version: v0.12.108
license: https://creativecommons.org/licenses/by/4.0/
tags: newsroom, publishers, findability, taxonomy, article
status: published
---

!shot sx-section.webp | images/ | A section for publishers and how it keeps itself current: three inputs, one build step, and the page with its JSON twin. | concept

## In short {#in-short}

- **Where do I send a publisher?** The publishers page was written once; the site changes most days.
- **A section is the newsroom as one audience reads it.** Start here, latest, features, and every relevant article.
- **It keeps itself current.** Articles are placed by rule as they are published; features appear as they ship.
- **Every placement says why.** A wrong one can be traced to its rule, and fixed there.
- **A register of what the site can do.** Each feature with when it shipped, its status and where to try it.
- **The build exposed loose classification.** History talks filed as journalism; dark mode filed under the agent-readable web.
- **Publishers first, then others.** Security leads, builders and investors can follow the same pattern.

## Where do I send a publisher? {#where}

I keep meeting publishers, editors and people who run news businesses, and the question after the first conversation is always the same: where should they start? The [publishers page](https://newsroom.sgit.ai/publishers/index.html) is a good answer. It is a distillation of what runs and how to try it, almost an article in its own right. But it was written once, and this site does not stand still. We are still in the explorer phase: we try things most days, and some of the most useful ones arrived in the last week.

Here is an example. When I come back to an article I have read part of, the sections I have read now [fold away](/articles/your-reading-your-controls.html). A bar at the top lets me choose how: a line in the margin, faded, folded to a paragraph, folded to one line, or hidden. It means I can return to an article and see only what I have not read, or see what I have read in a faded way. I did not plan it; it shipped on 17 October with the change that made the meter charge for what is read, and I use it whenever I come back to a piece. A publisher should see it. Nothing on the publishers page tells them it exists.

So the page needs to be something that keeps up.

## What a section is {#section}

The site already has [desks](https://newsroom.sgit.ai/desks/index.html): five audiences, each article placed on one desk first and sometimes a second, by rule, from its subjects. And it has personas, the newsroom as a CISO or a founder would read it. A section sits between the two: the newsroom as one audience reads it, with everything that audience needs in one place. The first is [for publishers](https://newsroom.sgit.ai/sections/publishers/index.html), second in the Newsroom menu at the top of every page.

It has five parts:

1. **Start here.** Five pieces, chosen by me, each with a sentence saying why: the founding argument, the arithmetic of buying one article, the meter, why agents will pay to read, and how quality control works when agents write.
2. **Latest.** The newest pieces for publishers, marked new if they are less than a week old.
3. **What you can use today.** The features a publisher can try and copy, each with when it shipped, its status, a link to try it and the article that explains it.
4. **The streams.** Every relevant article, in four groups: how news gets paid for, answers to the industry, readers and personas, and how this newsroom runs. Each article says which rule placed it.
5. **How this page stays current**, said on the page itself.

## How it keeps itself current {#current}

Nothing on the page is listed by hand except the five to start with. The rest comes from data the site already maintains.

Every article is given a desk and controlled subjects when it is published; that is [findability](https://newsroom.sgit.ai/articles/find.json), which runs on every release. A section is one small file of rules written against that data. The stream "how news gets paid for", for example, is: anything with the subjects micropayments, story vaults or local news; or anything on the news desk about the agent-readable web, journalism or pricing that is not a reply to someone. Streams are tried in order and an article goes in the first one it matches. The file is plain JSON, and it reads like what it means:

```json
{"id": "paid", "label": "How news gets paid for",
 "rule": [{"tags_any": ["micropayments", "story-vault", "local-news"]},
          {"tags_any": ["agent-readable-web", "journalism", "pricing"],
           "desk": ["news"], "format_not": ["response"]}]}
```

Features come from a new register, one entry per feature: what it does, why it matters, when it shipped, whether it is live, in beta or only designed, where to try it, and who it is for. A feature is added in the release that ships it. The publishers' section shows the features whose audiences include publishers; when a section for builders exists, it will show its own.

So when an article about paying for news is published, it is in the publishers' section that day, in the right stream, saying why. When a feature ships, it is in the register and on the page in the same release. The section is not written; it is maintained by the same rules that maintain everything else.

## What building it showed {#showed}

The first run placed 79 articles; after the fixes below, 69. Reading through them, most were where I would have put them, and a few were not, and each wrong one was a lesson about the classification rather than about the section.

- **History filed as journalism.** Three talks from the Portugal history series landed under "how news gets paid for", because the controlled subject *journalism* absorbs the raw tag *history*. The section now excludes them, with that reason written beside each.
- **A subject that was too broad.** *The agent-readable web* had swept up an article on dark mode and one on a tokens hook. The stream now takes that subject only from articles whose first desk is news, and two remaining exceptions are named in the rules.
- **The replies were being taken first.** Answers to FT Strategies and to Reader Skills went to "how news gets paid for" because they are tagged story vault; the answers stream is now tried first.

This is the same lesson as [search as navigation](/articles/search-as-navigation.html): the better the taxonomy, the less anyone has to curate by hand. Every fix here is a rule with a reason, in a file anyone can read, rather than an article moved by hand that nobody can explain later.

## Next sections {#next}

Publishers are first because they are who I most often need to point somewhere. The same pattern fits the other people I write for: security leads and boards, people building with agents, founders and investors. Each is one more file of rules and five pieces to start with; the features and the placement come for free. And because each section has a machine-readable twin, an agent sent to the newsroom on a publisher's behalf can read the section as easily as the publisher can.

## What this does not claim {#limits}

- **The start here list is mine, and will go stale** unless I change it; everything else updates itself.
- **The placement is only as good as the classification.** Three exclusions and two exceptions are written into the rules today.
- **The features register starts today.** Some features have no shipping date in it, because I could not confirm one from the release notes.
- **One section exists.** The others are a proposal.
- **The publishers page itself is unchanged.** It is imported from sgit.ai, and the section links to it as the overview.

If you run a news business and want to tell me what you would expect to find in this section, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo from me on 18 October 2026. The section: [For publishers](https://newsroom.sgit.ai/sections/publishers/index.html), its rules at `admin/content/sections/publishers.json` and its data at [sections/publishers.json](https://newsroom.sgit.ai/sections/publishers.json); the features register at [sections/features.json](https://newsroom.sgit.ai/sections/features.json); the code in `admin/build/sections.py`; the classification at [articles/find.json](https://newsroom.sgit.ai/articles/find.json). Related: [your reading, your controls](/articles/your-reading-your-controls.html), [search as navigation](/articles/search-as-navigation.html), [reviews on the record](/articles/reviews-on-the-record.html), [pay after you read](/articles/pay-after-you-read.html). Written up and checked by this site's agent; the editorial responsibility is mine.
