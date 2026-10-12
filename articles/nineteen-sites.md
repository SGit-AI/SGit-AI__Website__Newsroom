# Twenty sites in fifteen days, and what that did to the writing, sgit.ai

> The thinking behind sgit stopped fitting on one site. It moved out to nineteen siblings on *.sgit.ai, what forced the split, what it cost, and why the index into them now starts with a question instead of a list.

*Source: <https://newsroom.sgit.ai/articles/nineteen-sites.html> · sgit.ai v0.7.81 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Twenty sites in fifteen days, and what that did to the writing

# Twenty sites in fifteen days, and what that did to the writing

2026-08-26 · [article v1.1.2, 4 versions](versions/nineteen-sites.md) · [sgit.ai v0.2.45](https://sgit.ai/admin/versions.md) · networkpublishingmethod

***Abstract:** The thinking behind sgit stopped fitting on one site. It moved out to nineteen siblings on *.sgit.ai, what forced the split, what it cost, and why the index into them now starts with a question instead of a list.*

On 11 August this was one website. By 26 August there were **twenty repositories**, nineteen of them siblings on `*.sgit.ai`, and fifteen of those were created in the last five days of that fortnight.

That is not a plan anybody wrote down. It is what happened when a body of work outgrew the shape it was being published in, and the interesting part is not the count, it is what the count did to the writing.

The network directory. Nineteen siblings, entered through the question you arrived with.

## What forced it

A section is a promise that something is *part of* the thing it sits inside. That promise held while the material was about sgit. It stopped holding the moment the writing started answering questions that were not about sgit at all.

*You cannot deny a risk, you can only say how long you accept it* is not a paragraph in a docs site about encrypted version control. Neither is *maps are claims, not pictures*, or *open source is a strategy, not a charity*, or *the standard is the graph*. Each of those is an argument that needs room, a reader who arrived for it, and, the part that matters most, **its own version history**.

That last one is the real forcing function. On one site, every change is one changelog. Nineteen arguments moving at different speeds through one release log produces a record nobody can read. Split them and each argument gets its own tags, its own release cadence, its own record of when it changed its mind.

## What it cost

Three things, all of them real.

**Discovery got worse before it got better.** Nineteen domains is not a menu, it is a problem. A reader who does not already know these sites cannot pick one from a list of names, `nfrs.sgit.ai` and `issues-fs.sgit.ai` mean nothing until you already know what they argue.

**Consistency became something you have to maintain rather than get for free.** One site has one stylesheet by construction. Nineteen have one stylesheet by discipline, and discipline is the thing that quietly stops happening.

**Cross-linking stopped being automatic.** An internal link is cheap; a link between sites is a claim that the other site still says what you think it says. [graphs.sgit.ai](https://sgit.ai/network/graphs.md) is the only sibling so far that links *back*, and the audit that added it found the same site pointing at `sentinel.sgit.ai`, which does not exist. The site is `sg-sentinel.sgit.ai`. One character of drift, and the link is dead.

## What we did about discovery

The directory used to be a list of cards. At four entries that was fine. At nineteen it is a thing you have to read *before* it helps you, which is the opposite of what an index is for.

So it now **starts from the question**, not the inventory:

*"I have to sign off a risk and I do not want to rubber-stamp it"* → **risks.sgit.ai**

*"My app has to call an LLM and I do not want it holding an API key"* → **llms.sgit.ai**

*"I want an issue tracker with no database"* → **issues-fs.sgit.ai**

Seventeen lines like that, then five groups by area, then a table of all nineteen for anyone who would rather see everything at once. Three ways in, for three kinds of reader, someone with a problem, someone browsing a field, and someone auditing the whole set.

One rule keeps it honest: **every thesis on that page is the site's own words**, quoted from its H1 or lede rather than summarised here. A summary drifts. A quotation either matches or is visibly wrong.

## The thing that made it cheap

None of this would be worth doing if each site were a bespoke build. They are not: same generator, same stylesheet, same release script, same validator, same rule that publishing is adding one file.

Adding the twentieth site to this index is writing one markdown file with a category and a one-line thesis. That is the whole ceremony. The property that makes a network of nineteen sites tractable is the same property that makes an unattended agent safe to run, [two agents publishing on the same day touch two different files and cannot conflict](https://sgit.ai/updates/#the-api-reference-we-did-not-have).

## Where it is honest

**One of the nineteen is not published.** `skills.sgit.ai` has a repository and a DNS record and nothing behind it. It is listed as *not published yet*, pointing at its repository, rather than quietly omitted, the same reason a missing tag is better than a missing page.

**Most of these sites are arguments, not products.** [sg-sentinel.sgit.ai](https://sgit.ai/network/sg-sentinel.md) says `NOT BUILT` at the top of every page. [risks.sgit.ai](https://sgit.ai/network/index.md#risk-governance) states that zero lines of code implement its model. [wardley-maps.sgit.ai](https://sgit.ai/network/index.md#graphs-method) is marked `PROPOSED`. That is the house style working as intended: publish the argument before the thing exists, say precisely what it is worth, and let it be checked later.

If you want the shortest version of what all of this is for, the [introduction](what-sgit-is.md) is one page. If you want the one site that answers your particular question, [the directory](https://sgit.ai/network/index.md) is built to send you there.

*Written by Dinis Cruz and the agentic team working with him. Licensed CC BY 4.0.*

## Threads

Site & engineeringVaults & method[This article as a graph →](graphs.md#nineteen-sites)

### Builds on

- [Git for things you cannot put on GitHub](what-sgit-is.md) sgit is git for files you cannot put on GitHub: encrypted before they leave your machine, versioned like git, stored where the server cannot read a byte.

### Continued by

- [The Mandate Stack: a multi-agent system in production, layer by layer](the-mandate-stack.md) A multi-agent system that runs a business every few hours: eight layers, one written mandate per agent, everything a graph, one human who sends.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 4 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=4)

**Posting this article on LinkedIn?** The cover is [nineteen-sites.jpg](banners/nineteen-sites.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/nineteen-sites.html)*
