# What open source is, and what it is not: six misconceptions, a little history, and why the point is that nobody can lock you in, sgit.ai

> At an event today I heard a couple of misconceptions about open source that are worth correcting, and they are increasingly common in a generation of developers and buyers who use open source every day without having grown up in its culture. Open source is a copyright licence: the holder uses the right to control copying to grant it instead. It began as copyleft, the GPL's condition that what you build from it is shared on the same terms, and the term "open source" came in 1998 as a pragmatic reframing; Linux, the most pragmatic project of all, stayed on the GPL. The misconceptions: that anybody can change it so nobody controls it, when a few maintainers decide what goes in; that anybody contributes, when most projects are run by a handful of people; that it is more or less secure than proprietary software, when the metric is whether somebody had the time, and was paid, to review it; that it costs nothing, when somebody is always paying; that open weights are open source, when weights are a compiled binary; and that no licence is the most open choice, when no licence is all rights reserved. For me the power of open source has nothing to do with contributions. It is that nobody can lock you in, and that the whole development workflow is yours.

*Source: <https://newsroom.sgit.ai/articles/what-open-source-is-and-is-not.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / What open source is, and what it is not: six misconceptions, a little history, and why the point is that nobody can lock you in

# What open source is, and what it is not: six misconceptions, a little history, and why the point is that nobody can lock you in

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-12 · [article v1.0.0](versions/what-open-source-is-and-is-not.md) · [sgit.ai v0.7.83](https://sgit.ai/admin/versions.md) · open-sourcelicensingcopyleftgplapache-2copyrightopen-weightsmaintainersfundingsecuritysovereigntyhistoryarticle

***Abstract:** At an event today I heard a couple of misconceptions about open source that are worth correcting, and they are increasingly common in a generation of developers and buyers who use open source every day without having grown up in its culture. Open source is a copyright licence: the holder uses the right to control copying to grant it instead. It began as copyleft, the GPL's condition that what you build from it is shared on the same terms, and the term "open source" came in 1998 as a pragmatic reframing; Linux, the most pragmatic project of all, stayed on the GPL. The misconceptions: that anybody can change it so nobody controls it, when a few maintainers decide what goes in; that anybody contributes, when most projects are run by a handful of people; that it is more or less secure than proprietary software, when the metric is whether somebody had the time, and was paid, to review it; that it costs nothing, when somebody is always paying; that open weights are open source, when weights are a compiled binary; and that no licence is the most open choice, when no licence is all rights reserved. For me the power of open source has nothing to do with contributions. It is that nobody can lock you in, and that the whole development workflow is yours.*

Six misconceptions about open source, and what is true. The control is real and visible; most projects are run by a few people; the security metric is whether somebody had the time to review it; somebody is always paying; weights are a compiled binary; and no licence means all rights reserved.

## In short

- **Open source is a copyright licence.** Copyright gives the creator the right to decide who may copy. An open source licence uses that right to grant copying, use and change, on stated terms.
- **It began as copyleft.** The GPL's innovation, from Richard Stallman and the Free Software Foundation, was to make sharing a condition: build on it and distribute the result, and the result is shared on the same terms. Critics called that viral. "Open source", in 1998, was the pragmatic reframing of the same freedoms.
- **Nobody controlling it is a myth.** A few maintainers decide what goes in; contributions are reviewed, signed off and refused. The control is real. It is just visible.
- **Security is about time, not openness.** Open source is not more or less secure than proprietary software. Code somebody had the time, and the money, to review is more secure than code nobody did.
- **Somebody is always paying.** Powerful software used by millions is often maintained by a few people who are paid little or nothing, which is the funding problem, not a property of the licence.
- **The point is no lock-in.** Not contributions. The ability to read it, run it, fix it and move it, and to own the whole development workflow, which is why there is no sovereignty without it.

## A copyright licence, from copyleft to open source

From free software to open weights, the short version: GNU in 1983, the Free Software Foundation in 1985, the GPL in 1989, Linux from 1991, the Debian guidelines in 1997, "open source" and the OSI in 1998, Apache 2.0 in 2004, and in 2024 both the xz utils backdoor and the Open Source AI Definition.

It helps to start with what open source legally is, because most misconceptions start from not knowing. Copyright gives the person who creates a work the right to control copying. Normally that means you cannot copy it without the holder's permission, and what a holder usually grants is a licence to use, not to copy. An open source licence is the holder using exactly that right to grant the opposite: you may copy, use, change and share, on these terms. It is a copyright licence. It is not the absence of copyright.

The great innovation came from Richard Stallman and the Free Software Foundation. GNU was announced in 1983 and the Foundation founded in 1985, and in 1989 the first version of the GNU General Public License turned an idea into a licence: copyleft, a clever inversion of copyright that makes sharing a condition. If you build on GPL code and distribute what you built, what you distribute has to carry the same licence. Critics called that viral, because it spreads to whatever touches it, and it was meant to.

The term "open source" came later than people think. It was proposed by Christine Peterson at a meeting in February 1998, after Netscape decided to release its browser's source, and the [Open Source Initiative](https://en.wikipedia.org/wiki/Open_Source_Initiative) was founded that month by Bruce Perens and Eric Raymond, with an Open Source Definition derived from the Debian Free Software Guidelines that Perens had drafted. It was a deliberately pragmatic reframing: the same freedoms, described for businesses rather than as a moral position, and without the ambiguity of "free". Linus Torvalds is the person I associate with that pragmatism, and the correction to my own shorthand is that Linux did not leave the GPL to get it: Linux adopted GPL version 2 in 1992 and has stayed there. The pragmatism was in the attitude, not a different licence.

My own view is closest to that pragmatic one. Open source, for me, is about not closing the software: not having software that is locked away from the user, who cannot copy it, cannot run it and cannot see how it works. Apache 2.0, from 2004, does that well. Anybody can use it, copy it, change it and share it, without paying, and it adds an explicit patent grant, which matters more than it looks. The repositories behind this site are Apache 2.0 for code and Creative Commons for writing, and [open-source.sgit.ai](https://open-source.sgit.ai/practice/apache-vs-mit.html) explains why Apache rather than MIT.

One thing I believed for a while, and was wrong about, is worth saying because I hear it often. I thought the most open thing was not to licence at all. It is the opposite. With no licence, ordinary copyright applies and all rights are reserved: [nobody may copy, change or share the work](https://choosealicense.com/no-permission/) without asking. If you want people to be able to use it, you have to say so, and a licence is how you say it.

## Misconception one: anybody can change it, so nobody controls it

This is the one I heard today, and it is the most important to correct. The idea is that because the source is open, anybody can change it, so the software is a free-for-all with no control. That is not how any serious project works. A small group of maintainers decides what goes into the project, and most projects have one or a handful. Contributions are reviewed, tested, often signed off under a developer certificate or a contributor agreement that records who wrote what and that they had the right to give it, and many are refused. Even before generative AI, provenance was a large part of maintaining a project well. Anybody can fork a project and change their own copy; nobody can change yours without you.

The control is real. It is just visible, which is a strength: you can see exactly who decides, how, and what they accepted.

## Misconception two: open source means anybody contributes

It is true that the barrier to contributing is lower. With proprietary software you usually cannot even get a buildable system, so contributing is not possible at all. But in my experience, and apart from a very small minority of extremely popular projects, almost every open source project is run by a small number of people. That is not a failure of open source; it is the normal shape of it. Treating "anybody can contribute" as the point leads people to expect a community that is not there, and to miss what is.

## Misconception three: it is more, or less, secure

We have reached a sensible balance on this, and the honest answer is that neither is true. Open source is not dramatically more secure or less secure than proprietary software, because openness is not the metric. The metric is whether somebody had the time to focus on it, which in practice means somebody was paid, even if the one paying is the maintainer with their own free time, to do security reviews, testing and quality work. Show me software that has had no security review, open or closed, and I will show you software with plenty of vulnerabilities. Usage matters too: software that many people run has more people finding its problems.

It is also worth remembering how much proprietary software is open source underneath. Black Duck's [annual analysis of commercial codebases](https://www.blackduck.com/ossra) finds open source in almost all of them, year after year. Closing a product does not close its dependencies; it only hides them.

## Misconception four: it is free, so it costs nothing

This is where the culture gap shows most. A new generation of developers and buyers treats open source as simply free to use, without having grown up with the culture that produced it. Somebody is always paying. [Tidelift's 2024 maintainer survey](https://www.theregister.com/2024/09/18/open_source_maintainers_underpaid/) found around 60% of maintainers describing themselves as unpaid hobbyists, and found paid maintainers markedly more likely to implement recommended security practices. The result is a tragedy of the commons: extraordinarily powerful software used by millions, and organisations that will pay a consultant to customise it or work out how to use it rather than paying the people who wrote it and would do it better.

The [xz utils backdoor](https://en.wikipedia.org/wiki/XZ_Utils_backdoor), found in March 2024, is the case everybody should know. A compression library that sits underneath much of Linux was maintained for years by one person; an attacker spent years earning trust as a contributor, with pressure on the maintainer to hand over responsibility, and shipped a backdoor in two releases before an engineer noticed SSH logins were slow. The lesson is not that open source is unsafe. It is that mission-critical software was being maintained by somebody with almost no time and no money, and the expectation that such a person would also do the due diligence of a well-funded team is a bit rich. We should be paying those individuals, with financial models built for it; [open-source.sgit.ai's funding section](https://open-source.sgit.ai/funding/index.html) compares the proposals. Part of the reason this never worked is that the people who write open source want to write code, not run professional services, and until recently the workflows to do both were not practical. With agents, I think they are becoming practical.

## Misconception five: open weights are open source

The word open source has been stretched a lot recently, and the model labs are a good example of both the problem and the right answer. Model weights are like a compiled application: you can run them, and you can fine-tune them, but you cannot build them from scratch, which is exactly what source code is for. So I agree with the labs that now say open weights rather than open source. The Open Source Initiative's [Open Source AI Definition](https://opensource.org/ai/open-source-ai-definition) draws the line clearly: for a model to be open source it needs the code used to train and run it, the parameters, and enough information about the training data that a skilled person could build a substantially equivalent system.

That does not make open weights less useful. [Supply chain of vaults](supply-chain-of-vaults.md) argues that open-weight models are one of the largest economic advantages a company can have, because they can be run and built on inside your own environment. It just makes them a different thing, and calling them by the right name is part of keeping the term meaningful.

## Misconception six: openness is the danger

There is a lot of fear, uncertainty and doubt at the moment about open-weight models and how dangerous they are. At the end of the day the question is how a tool is used and by whom. You can search for alarming things already. Metasploit made exploitation dramatically easier when it appeared, and the world adjusted. That does not mean everything should be published: there are highly destructive capabilities nobody should be releasing, and some technologies will be controlled, as some always have been. And even open source has to be hosted somewhere and distributed through somebody, which is itself a point of control. The idea that open source is a free-for-all without any control is simply not true.

## What open source is for

For me, the power of open source has nothing to do with the fact that people can contribute. The power is that you are not locked in. You can read it, run it, fix it and move it, and if the company behind it is sold, changes its licence or disappears, you can keep going. And you get the whole development and technology workflow with it: the history, the tests, the build, the reasoning in the commits, all of which are as valuable as the code.

That is why I keep saying there is no sovereignty without it. [Sovereignty is the ability to move](sovereignty-is-the-ability-to-move.md), and a European supplier today is one acquisition away from not being one; only control that survives a change of owner counts, and open source is how you get it. [open-source.sgit.ai](https://open-source.sgit.ai/) is the longer version of all of this: the position, the history with its corrections and sources, the licences I use and why, a stress test you can run on a vendor, and the funding question. Its first lesson is the one I would want a new developer to take away: "open source is not free, somebody is always paying for it."

## What this does not claim

- **It is not legal advice.** Licences are legal instruments; read the licence, and ask a lawyer when it matters.
- **The history is the short version.** Earlier permissive licences existed alongside the GPL, and the full story, with its corrections and sources, is on [open-source.sgit.ai](https://open-source.sgit.ai/history/index.html).
- **The maintainer figures are surveys.** Tidelift's 60% is how maintainers describe themselves; the share who say they are unpaid for their work is lower in the same survey.
- **Contributions do happen.** The claim is that they are not the point and not the norm, not that they never matter.

If you are deciding how to licence something, or how to depend on open source without being surprised by it, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 12 October 2026, after an event, written by this site's agent in the voice of this site; where my memo had the history slightly wrong, the agent corrected it from sources and the corrections are in the text. The argument and the editorial responsibility are mine. History: the [Open Source Initiative](https://en.wikipedia.org/wiki/Open_Source_Initiative) and [open-source.sgit.ai's timeline](https://open-source.sgit.ai/history/timeline.html). Licensing default: [choosealicense.com](https://choosealicense.com/no-permission/). Figures: [Black Duck's OSSRA](https://www.blackduck.com/ossra), [Tidelift's 2024 maintainer report via The Register](https://www.theregister.com/2024/09/18/open_source_maintainers_underpaid/). Models: the [Open Source AI Definition](https://opensource.org/ai/open-source-ai-definition). The xz case: [Wikipedia](https://en.wikipedia.org/wiki/XZ_Utils_backdoor).

## Threads

Startups & strategySite & engineering[This article as a graph →](graphs.md#what-open-source-is-and-is-not)

### Builds on

- [A supply chain of vaults: how GenAI, open data and small custom tools could bring the price of food down](supply-chain-of-vaults.md) The food chain is a data problem: one encrypted vault per party, joined by append lanes and a typed graph, could cut the waste that keeps prices high.
- [Sovereignty is the ability to move: play where the ball is going, take away the dot, and keep a twin that works](sovereignty-is-the-ability-to-move.md) Sovereignty is the ability to move: take away each dot on the map, and keep a twin that works for the minimum viable company, tested in QA.

### Continued by

- [The eyeballs get cheap: why open source is about to become the most secure software we have, and why secure, sovereign and paid-for meet at the least code in production](the-eyeballs-get-cheap.md) Cheap, deep AI security review gives open source the eyeballs it never had; with sovereignty and paid maintenance, all point at the least code in production.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 96 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=96)

**Posting this article on LinkedIn?** The cover is [what-open-source-is-and-is-not.jpg](banners/what-open-source-is-and-is-not.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/what-open-source-is-and-is-not.html)*
