# Who creates the original? Mapping where the PHP story's data comes from, giving that map to the historian, and the places where we can make content nobody else has: our own counts, interviews and op-eds, sgit.ai

> With publishing working well, and the PHP site about to be split into six repositories, I want to start a new piece of work: a map of where the data in the story actually comes from. Who is creating original data, and who is passing it on? The site already holds the answer in raw form. Of the 418 sources it has captured, 277 are news pages, but when you count who first states each of the 107 claims, numbers and exploitation reports the site attributes, news outlets originate 5 of 146; organisations, agencies and named people originate almost all the rest, led by the PHP Foundation, Wiz, CISA and Cloudflare. The fact-check desk found claims relayed 29 times, 11 of them by the BBC. That map is a job for the historian, the agent that keeps the record and finds the pivot points, and it needs its own visualisations and data work. The second question is where we can create original content ourselves. We already do in a few places: figures we counted, a source watch that catches silent rewording, correction requests. The bigger opportunity is people: interviews with those affected, recorded by me or drafted by an agent, under the Open Security Summit banner, and op-eds from people involved, published on our site.

*Source: <https://newsroom.sgit.ai/articles/who-creates-the-original.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Who creates the original? Mapping where the PHP story's data comes from, giving that map to the historian, and the places where we can make content nobody else has: our own counts, interviews and op-eds

# Who creates the original? Mapping where the PHP story's data comes from, giving that map to the historian, and the places where we can make content nobody else has: our own counts, interviews and op-eds

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-25 · [article v1.1.0, 2 versions](versions/who-creates-the-original.md) · [newsroom v0.13.78](https://newsroom.sgit.ai/admin/versions.html) · provenancesourcesoriginal-contentinterviewsagentsphp2shellarticle

***Abstract:** With publishing working well, and the PHP site about to be split into six repositories, I want to start a new piece of work: a map of where the data in the story actually comes from. Who is creating original data, and who is passing it on? The site already holds the answer in raw form. Of the 418 sources it has captured, 277 are news pages, but when you count who first states each of the 107 claims, numbers and exploitation reports the site attributes, news outlets originate 5 of 146; organisations, agencies and named people originate almost all the rest, led by the PHP Foundation, Wiz, CISA and Cloudflare. The fact-check desk found claims relayed 29 times, 11 of them by the BBC. That map is a job for the historian, the agent that keeps the record and finds the pivot points, and it needs its own visualisations and data work. The second question is where we can create original content ourselves. We already do in a few places: figures we counted, a source watch that catches silent rewording, correction requests. The bigger opportunity is people: interviews with those affected, recorded by me or drafted by an agent, under the Open Security Summit banner, and op-eds from people involved, published on our site.*

Who creates the original, in the PHP story's data: 418 sources captured, 107 attributed claims, and who originated them.

## In short

- **A new piece of work: map where the data comes from.** Who creates original data, and who passes it on.
- **The PHP site already has the raw answer.** Every claim is attributed to who first stated it.
- **News is most of what we read, little of what is original.** 277 of 418 sources; 5 of 146 originations.
- **This is the historian's job.** It keeps the record, finds the pivot points, and needs its own visualisations.
- **Where can we be original?** Our own counts, our own record, our own analysis.
- **And people.** Interviews with those affected, and op-eds from those involved, on our site.

## Who is creating original data?

Publishing on [the PHP story site](https://php.oct.2026.newsroom.sgit.ai/) now works well, and the site is about to be [split into six repositories](https://newsroom.sgit.ai/articles/a-villager-for-the-agents.html). So this is a good moment to start something I have wanted for a while: a map of where the story's data actually comes from. Who is creating original data? Who is creating the insight? And who is passing on what someone else found?

The site already holds the raw material. Its ontologist keeps an attribution file that names, for every claim, number and exploitation report on the site, who first stated it, and, where the fact-check desk found the same words in someone else's capture, who relayed it. I counted it on 25 October, at release v0.22.0.

- **What we read.** 418 sources captured: 277 news pages, 31 government pages, 27 vendors, 25 advisories, 14 CVE records, 11 researchers, and the rest code, social posts and others.
- **Who says it first.** 107 attributed rows, with 146 originations between them. Organisations account for 79, agencies 27, named people 22, groups 5, news outlets 5, and the remaining 8 are unnamed posts, a registry, a platform, a project and this site.
- **Who leads.** The PHP Foundation (13), Wiz (9), CISA (7), Cloudflare (7), the PHP Group (6) and Amazon (6).
- **Who relays.** Claims found relayed 29 times, 11 by the BBC and 6 by The Hacker News. The BBC also originates three statements of its own.

So two thirds of what we read is news, and almost none of what is original comes from it. That is not a criticism of the outlets: relaying, checking and explaining is valuable work. But it is the map that [sources and their shadows](https://newsroom.sgit.ai/articles/sources-and-shadows.html) and [local trust, certified upwards](https://newsroom.sgit.ai/articles/local-trust-certified-upwards.html) need, if anyone is ever going to pay the people who created the original.

## A job for the historian

Which agent should own this? I think it is the historian. The historian is the one that keeps the record: it goes back, finds the nuggets, the interesting elements, the pivot points. Who created what, and when, is exactly that.

Today the PHP site's historian [puts the story beside the ones before it](https://php.oct.2026.newsroom.sgit.ai/admin/agents/historian/index.html) and keeps the corrections, the context page and the version history. It has no schedule card yet, and its status records no round since its policy was written on 22 October. Giving it this map is a reason to wake it.

It is also more than a list. This part of the site needs its own visualisations and its own data work: originators against relays, over time; who was first, and who caught up; which outlets add something and which pass words on. Every other agent can nudge it, the fact-check desk above all, but one agent should maintain it. The data is in place. What is missing is someone whose job it is.

## Where can we be original?

Where we can create original content: counted, recorded, analysed, interviewed or written by others, with each status.

The second question turns the first on ourselves. Where are we creating content that nobody else has?

There are already a few places. Six of the attributed statements are figures the site counted itself, from captured files or a clone of the code, and one claim is the site's own: that no named organisation has confirmed a compromise through php2shell, with its time. The [source watch](https://php.oct.2026.newsroom.sgit.ai/vaults/source-watch/index.html) re-reads 913 pages and has kept 2,946 snapshots, which is how it [caught a publisher rewording without a note](https://newsroom.sgit.ai/articles/the-side-stories-of-php2shell.html). Twelve [correction requests](https://php.oct.2026.newsroom.sgit.ai/outreach/index.html) are drafted, none sent yet. And Pulse, the risk graph and the historian's perspective pieces are our analysis. Nobody else has these, because nobody else kept the record.

## People, in their own words

But the most original content is people. The site already has one interview: [the editor, interviewed](https://php.oct.2026.newsroom.sgit.ai/interview/index.html), with ten questions written by the agent that builds the site, ten answers in my own words from my voice memos, and five questions waiting for a live interview.

We can do a lot more of that.

- **Interviews with people affected.** I can do them myself, and record them as podcasts or videos, especially under the [Open Security Summit](https://newsroom.sgit.ai/articles/the-open-security-summit-and-its-debt.html) banner.
- **Interviews drafted by an agent.** An agent can prepare the questions, as it did for mine, and turn the answers into a page, with the recording as its source.
- **Op-eds.** We can ask the people involved, maintainers, defenders, publishers and those affected, whether they would like to write an opinion piece for the site, under their own name.

That last one matters. Publishing original content from others on our site makes us a place where original content is created, not only a place that maps it.

## What exists, and what is proposed

- **Exists:** the attribution data, the source watch, the correction requests, the counts, the editor's interview.
- **Proposed:** the historian owning the originators map, with its visualisations; interviews with people affected; op-eds from people involved.

## What this does not claim

- **The counts are the site's own attribution,** at v0.22.0; a row can name two originators, and the attribution is still being filled in.
- **"Relays" are only those the fact-check desk found** in a capture; the real number is higher.
- **Nobody has been asked for an interview or an op-ed yet.**

## Where this comes from

My voice memo of 25 October 2026. The PHP story site at release v0.22.0, read on 25 October 2026: its sources, attribution, entities, source watch, outreach, interview and team data, and the historian's role file. Related: [sources and their shadows](https://newsroom.sgit.ai/articles/sources-and-shadows.html), [local trust, certified upwards](https://newsroom.sgit.ai/articles/local-trust-certified-upwards.html), [the side stories of php2shell](https://newsroom.sgit.ai/articles/the-side-stories-of-php2shell.html), [a villager for the agents](https://newsroom.sgit.ai/articles/a-villager-for-the-agents.html), [a call for help](https://newsroom.sgit.ai/articles/a-call-for-help.html), [agents need direction](https://newsroom.sgit.ai/articles/agents-need-direction.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

News & evidenceAgents & policy[This article as a graph →](graphs.md#who-creates-the-original)

No other article links here yet.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 288 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=288)

**Posting this article on LinkedIn?** The cover is [who-creates-the-original.jpg](banners/who-creates-the-original.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/who-creates-the-original.html)*
