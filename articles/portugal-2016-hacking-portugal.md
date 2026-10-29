# Hacking Portugal, 2016: my BSidesLisbon keynote and the book that stopped at 95%, slide by slide, with what holds ten years later and what a new edition needs, sgit.ai

> On 11 November 2016 I gave the keynote at BSidesLisbon, Hacking Portugal and making it a global player in software development, 103 slides, and three weeks later published it as a book on Leanpub, 75 pages, which still says 95% complete. The idea was that if to hack means to solve problems, Portugal should hack itself: make its network hostile to insecure code, replace the old military service with a Portuguese Hacking Service for 15 to 21 year olds, create a hackathon league as famous as football, a Code Made in Portugal brand, OpenSource.pt for all government code, a Ministry of Code, a Clear Software Act, and a national bug bounty, because cyber security is a public health problem. Ten years later, the regulation I asked for has mostly arrived from Europe, and Portugal has open-sourced a national AI model, which is the spirit of OpenSource.pt. The Hacking Service, the league and the Ministry of Code have not happened. And the biggest change is one I did not see: with agents, everybody can now build software by talking, which makes the talk's central claim, that a small country can choose to lead in code, more possible than it was. This article goes through the talk and says what a new edition, for Web Summit in Lisbon, needs.

*Source: <https://newsroom.sgit.ai/articles/portugal-2016-hacking-portugal.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Hacking Portugal, 2016: my BSidesLisbon keynote and the book that stopped at 95%, slide by slide, with what holds ten years later and what a new edition needs

# Hacking Portugal, 2016: my BSidesLisbon keynote and the book that stopped at 95%, slide by slide, with what holds ten years later and what a new edition needs

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-16 · [article v1.1.0, 2 versions](versions/portugal-2016-hacking-portugal.md) · [newsroom v0.12.78](https://newsroom.sgit.ai/admin/versions.html) · portugalhacking-portugalbsides-lisbontalksbooksapplication-securityopen-sourceeuropehistoryarticle

***Abstract:** On 11 November 2016 I gave the keynote at BSidesLisbon, Hacking Portugal and making it a global player in software development, 103 slides, and three weeks later published it as a book on Leanpub, 75 pages, which still says 95% complete. The idea was that if to hack means to solve problems, Portugal should hack itself: make its network hostile to insecure code, replace the old military service with a Portuguese Hacking Service for 15 to 21 year olds, create a hackathon league as famous as football, a Code Made in Portugal brand, OpenSource.pt for all government code, a Ministry of Code, a Clear Software Act, and a national bug bounty, because cyber security is a public health problem. Ten years later, the regulation I asked for has mostly arrived from Europe, and Portugal has open-sourced a national AI model, which is the spirit of OpenSource.pt. The Hacking Service, the league and the Ministry of Code have not happened. And the biggest change is one I did not see: with agents, everybody can now build software by talking, which makes the talk's central claim, that a small country can choose to lead in code, more possible than it was. This article goes through the talk and says what a new edition, for Web Summit in Lisbon, needs.*

Twelve slides from Hacking Portugal at BSidesLisbon 2016, from the summary to the future of Portugal.

## In short

- **November 2016, Lisbon.** The BSidesLisbon keynote, 103 slides, then a book.
- **The book is still at 95%.** Published 1 December 2016, never finished.
- **Hack Portugal.** Hostile to insecure code; a Hacking Service; a league like football.
- **Code as a national asset.** Made in Portugal, OpenSource.pt, a Ministry of Code.
- **Europe brought the regulation.** The Clear Software Act, more or less.
- **The service and the league did not happen.** As far as I know.
- **Agents change the bet.** Everybody can build now; a small country can choose to lead.

## The talk and the book

I gave [Hacking Portugal](https://www.slideshare.net/DinisCruz/hacking-portugal-v10) as the keynote at BSidesLisbon on 11 November 2016; the [video](https://www.youtube.com/watch?v=gYuKs30HxqE) is 49 minutes. Its premise was in the book's first lines: "If the word 'hack' means to solve problems, then 'Hacking Portugal' means to find innovative was to solve existing problems." I wanted Portugal to treat software seriously, "a place where programming, TDD, Open Source, learning how to code, hacking (aka bug-bounty style), and DevOps receive the consideration, investment and respect that they deserve", with application security as the enabler.

Three weeks later the talk was [a book on Leanpub](https://leanpub.com/hacking-portugal): 17 chapters, 75 pages, 14,487 words, licensed CC BY 4.0, with a paperback on Amazon. Its page still says 95% complete; it was last updated on 1 December 2016, the day it was published. (Its introduction even gives the wrong date for the talk, 9 November.) It is one of the books [I left behind](books-from-articles.md), and the one I most want to come back to.

## Hostile to insecure code

The talk opened with a Portuguese network "to be hostile to insecure code": make it hard to create, publish or host insecure apps and devices in Portugal, by regulation, by market pressure and by a community that attacks vulnerable code before criminals do. It used a 2016 scan of the country's exposed systems, open remote desktops, industrial controllers, clear-text protocols and data leaks, to ask "How Secure is Portugal?" The honest answer was insecure, but currently safe: not yet attacked at scale.

**Ten years later.** The regulation arrived, from Europe. Since 11 September 2026 the [Cyber Resilience Act](https://www.mccannfitzgerald.com/knowledge/data-privacy-and-cyber-risk/cyber-resilience-act-reporting-obligations-apply-from-11-september-2026) makes manufacturers report actively exploited vulnerabilities, and its security requirements follow in 2027; Portugal's own [cybersecurity law](https://www.pwc.pt/pt/temas-actuais/dl-125-2025.html) came into force in April 2026. That is close to the *Clear Software Act* on slide 83, "like the 'Clean Air Act', but focused on code quality and security". The quote I used there still explains the resistance: "It is difficult to get a man to understand something, when his salary depends upon his not understanding it".

## A Hacking Service, and hacking like football

The idea people remember was the *Portuguese Hacking Service*: update the old compulsory military service into a hacking service for 15 to 21 year olds, to "hack everything that is plugged-in to Portugal's network", code-review open-source and strategic code, contribute fixes, and "help SMEs with their digital security and DevOps", paid for by moving a share of the military budget to cyber. Around it: a national hackathon league, teams sponsored to go to DefCon, and hacking taught the way Portugal teaches football, with the kids, the clubs, the pride.

**Ten years later.** As far as I know, none of this happened in that form. I still think the idea is right, and I would change one thing. In 2016 learning to hack meant learning to code first. With agents, a 16-year-old can explore a system by talking to it, which is what I now call [explorer coding](explorer-coding.md). A Hacking Service in 2026 would teach young people to direct agents against Portugal's own systems, with [a mandate](the-mandate-stack.md) that says what they may and may not touch.

## Code as a national asset

The second half was about code as something a country owns. A *Code Made in Portugal* brand, because "Good software development teams (from developers to management) are one of the most important assets of a company and country." *OpenSource.pt*: "All code written (and paid) for Government agencies to be released under an Open Source license", and all government documents under Creative Commons. A *Ministry of Code*, with a government CTO and CISO. A *Portugal-wide bug bounty*. Cyber security as a *public health problem*, with specialists trained "using similar techniques to the ones we use to train doctors, nurses".

**Ten years later.** The best news is in the spirit of OpenSource.pt: in 2026 Portugal released [Amália](https://thenextweb.com/news/portugal-open-source-ai-model-amalia), a national language model for European Portuguese, as open source, built on the European EuroLLM model and meant as a platform for public services, companies and researchers. It is exactly the kind of code a country should own and share. The Ministry of Code and the national bug bounty are still ideas. And the public health analogy has only grown more apt: Europe now treats software defects as a liability, from December, under the [Product Liability Directive](https://www.hoganlovells.com/en/publications/eu-introduces-comprehensive-digitalera-product-liability-directive).

## Why Portugal, then and now

The talk ended with a choice: Portugal could "be a garden for Europe, a holiday destination", or "a powerhouse that inspires and leads the world in technology and secure coding", working with the Portuguese-speaking countries. The book's last chapter argued it is easier in a small country, "more likely to have fewer agendas and fewer lobby groups wielding influence".

**What holds.** All of it, and I made the same argument this month about AI, in [Judo for small countries](judo-for-small-countries.md). **What I got wrong** is the timescale, and the idea that it would start from security. It did not start from security; it may start from language and AI, where Portugal has just made a real move. And what a book needs that a talk does not: a feedback loop, which is why the next edition will be built from articles like this one, read before they are bound.

## What a new edition needs

A new edition of Hacking Portugal, for Web Summit in November, would keep the structure and change the centre of gravity: from application security to agents, language and sovereignty. It needs the [2010 keynote](portugal-2010-a-challenge.md) as its origin, this talk as its body, [the 2024 talk on GenAI in Portuguese](portugal-2024-genai-in-portuguese.md) as the turn, [the Europe essays](portugal-and-europe-2025.md) as the wider frame, and a new last part on what a small country can do with agents. Most of that is already written; the rest will be published here first.

## What this does not claim

- **"As far as I know" means I did not survey it.** Some of these ideas may exist in a form I missed.
- **The Clear Software Act is an analogy.** The CRA is the EU's law, not mine.
- **The commentary is mine, now.** The slides are from 2016, unchanged.

If you were at BSidesLisbon in 2016, or want to help with the new edition, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 16 October 2026, written by this site's agent in the voice of this site; the commentary and the editorial responsibility are mine. The [slides](https://www.slideshare.net/DinisCruz/hacking-portugal-v10), the [video](https://www.youtube.com/watch?v=gYuKs30HxqE), [the book on Leanpub](https://leanpub.com/hacking-portugal) and its [source](https://github.com/DinisCruz/Book_Hacking_Portugal), and [my blog post](https://diniscruz.blogspot.com/2016/11/presentation-hacking-portugal-and.html) of 11 November 2016. For today: Amália, via [The Next Web](https://thenextweb.com/news/portugal-open-source-ai-model-amalia); the Cyber Resilience Act, via [McCann FitzGerald](https://www.mccannfitzgerald.com/knowledge/data-privacy-and-cyber-risk/cyber-resilience-act-reporting-obligations-apply-from-11-september-2026); Decreto-Lei 125/2025, via [PwC Portugal](https://www.pwc.pt/pt/temas-actuais/dl-125-2025.html); the Product Liability Directive, via [Hogan Lovells](https://www.hoganlovells.com/en/publications/eu-introduces-comprehensive-digitalera-product-liability-directive). Read on 16 October 2026.

## Threads

News & evidenceStartups & strategy[This article as a graph →](graphs.md#portugal-2016-hacking-portugal)

### Builds on

- [Books from articles: why my books stall at 95%, why these articles do not, and a plan to turn them into books by Web Summit](books-from-articles.md) My books stall at 60 to 95%; these articles do not. The hypothesis: a book is an ordered set of finished articles, tested by Web Summit in November.
- [Explorer coding: a better name for what people call vibe coding, what it is good for, and the handover to villagers and town planners before anyone depends on it](explorer-coding.md) Call it explorer coding, not vibe coding: the best thing since the spreadsheet, the best brief there is, and not ready to be in line until villagers take it.
- [The Mandate Stack: a multi-agent system in production, layer by layer](the-mandate-stack.md) A multi-agent system that runs a business every few hours: eight layers, one written mandate per agent, everything a graph, one human who sends.
- [Judo for small countries: where Portugal, Romania and Estonia can add the most value in AI, and why the race for GPUs is not it](judo-for-small-countries.md) A small country should not race for GPUs: the opportunity is the plumbing its talent stands on, built once as open infrastructure, with small models.
- [A web application security challenge to Portugal, 2010: my IBWAS keynote in Lisbon, slide by slide, with what came true, what I got wrong and what still stands](portugal-2010-a-challenge.md) My 2010 IBWAS keynote in Lisbon, slide by slide: twelve actions for Portugal, more of which came true than I expected, mostly from Brussels.
- [GenAI in Portuguese, 2024: my OWASP Global AppSec talk in Lisbon, the first public demo of The Cyber Boardroom, slide by slide, with what two years of agents have confirmed and changed](portugal-2024-genai-in-portuguese.md) My 2024 OWASP talk in Lisbon: Portuguese as a programming language, provenance, graphs instead of RAG, and the first public demo of The Cyber Boardroom.
- [Portugal and Europe, 2025: five essays on Portuguese as a programming language, an open-source sovereign cloud, regulation as graphs and Europe's chance in GenAI, and how they read a year and a half later](portugal-and-europe-2025.md) Five 2025 essays on Portuguese as code, a sovereign open-source cloud, regulation as graphs and Europe in GenAI, read again: two moved, one did not.

### Continued by

- [Bringing my past work back: a daily worker that turns eighteen years of essays, talks, posts and tools into linkable articles, and why every team needs one](bringing-my-past-work-back.md) A daily worker that turns eighteen years of essays, talks, posts and tools into linkable articles: then and now, connected, two or three a day.
- [Portugal and Europe, 2025: five essays on Portuguese as a programming language, an open-source sovereign cloud, regulation as graphs and Europe's chance in GenAI, and how they read a year and a half later](portugal-and-europe-2025.md) Five 2025 essays on Portuguese as code, a sovereign open-source cloud, regulation as graphs and Europe in GenAI, read again: two moved, one did not.
- [GenAI in Portuguese, 2024: my OWASP Global AppSec talk in Lisbon, the first public demo of The Cyber Boardroom, slide by slide, with what two years of agents have confirmed and changed](portugal-2024-genai-in-portuguese.md) My 2024 OWASP talk in Lisbon: Portuguese as a programming language, provenance, graphs instead of RAG, and the first public demo of The Cyber Boardroom.
- [A web application security challenge to Portugal, 2010: my IBWAS keynote in Lisbon, slide by slide, with what came true, what I got wrong and what still stands](portugal-2010-a-challenge.md) My 2010 IBWAS keynote in Lisbon, slide by slide: twelve actions for Portugal, more of which came true than I expected, mostly from Brussels.
- [Books from articles: why my books stall at 95%, why these articles do not, and a plan to turn them into books by Web Summit](books-from-articles.md) My books stall at 60 to 95%; these articles do not. The hypothesis: a book is an ordered set of finished articles, tested by Web Summit in November.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 150 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=150)

**Posting this article on LinkedIn?** The cover is [portugal-2016-hacking-portugal.jpg](banners/portugal-2016-hacking-portugal.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/portugal-2016-hacking-portugal.html)*
