# The value of constraints: what client-side encryption and open source actually gave us, which is not what you would think, sgit.ai

> The value I get from two of sgit's design choices is not the obvious one. sgit is encrypted on the client, and we often lead with that, but I made that mistake myself: nobody will buy sgit for its encryption. If it succeeds, it will be because it has better features and better workflows, and many of those came from the encryption, as a constraint. Encryption on the client moves the security problem from protecting all the data to protecting the keys, and moves the sovereignty line from where the data is stored to who holds the keys; the European Data Protection Board treats that as an effective measure for transfers. It does not take you out of GDPR, which my memo said it did: the data is still personal data for whoever holds the keys, but a breach of the ciphertext alone need not be notified to the people in it. The biggest benefit, though, is engineering. A server that cannot read the data removes the temptation to process anything on it, so there is no server code to write, deploy and secure, and the features that make sgit good, like scoped clones, came from working within that. Open source is the same kind of constraint: no private code removes the temptation to lock customers in, makes the code easy to deploy anywhere, and ends the startup curse of building every customer's integration. That is why it has to be all of it; open core is an evaluation version. The business model that follows is selling customisation.

*Source: <https://newsroom.sgit.ai/articles/the-value-of-constraints.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The value of constraints: what client-side encryption and open source actually gave us, which is not what you would think

# The value of constraints: what client-side encryption and open source actually gave us, which is not what you would think

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-16 · [article v1.0.0](versions/the-value-of-constraints.md) · [newsroom v0.12.76](https://newsroom.sgit.ai/admin/versions.html) · constraintsencryptionsgitopen-sourcesovereigntygdprengineeringbusiness-modelsopen-coredesignarticle

***Abstract:** The value I get from two of sgit's design choices is not the obvious one. sgit is encrypted on the client, and we often lead with that, but I made that mistake myself: nobody will buy sgit for its encryption. If it succeeds, it will be because it has better features and better workflows, and many of those came from the encryption, as a constraint. Encryption on the client moves the security problem from protecting all the data to protecting the keys, and moves the sovereignty line from where the data is stored to who holds the keys; the European Data Protection Board treats that as an effective measure for transfers. It does not take you out of GDPR, which my memo said it did: the data is still personal data for whoever holds the keys, but a breach of the ciphertext alone need not be notified to the people in it. The biggest benefit, though, is engineering. A server that cannot read the data removes the temptation to process anything on it, so there is no server code to write, deploy and secure, and the features that make sgit good, like scoped clones, came from working within that. Open source is the same kind of constraint: no private code removes the temptation to lock customers in, makes the code easy to deploy anywhere, and ends the startup curse of building every customer's integration. That is why it has to be all of it; open core is an evaluation version. The business model that follows is selling customisation.*

Two constraints and what they take away: client-side encryption forbids the server from reading the data and removes the temptation to process there; open source, all of it, forbids private code and removes lock-in, the evaluation edition and building every customer's integration.

## In short

- **Encryption is not the selling point.** Better features and workflows are; many came from the constraint.
- **Protect the keys, not all the data.** And the sovereignty line moves to whoever holds them.
- **It does not remove GDPR.** It reduces the exposure; my memo overstated it.
- **No server code is the biggest gain.** A server that cannot read has nothing to compute.
- **Open source removes temptations too.** Lock-in, the evaluation edition, every customer's integration.
- **It has to be all of it.** Open core is an evaluation version.
- **Take away until it hurts.** Not more than that.

## The mistake I made first

When we describe [sgit](what-sgit-is.md), we usually start with the encryption: an encrypted, version-controlled store, where the server holds ciphertext and nothing else. Agents do it when they write about it, and I did it at the beginning. But I do not think anyone will buy sgit because it is encrypted. Encryption is an important property, not a reason to choose a tool. If sgit succeeds, it will be because it has better features, better workflows and a better solution, as [the comparison with Scion](scion-and-sgit.md) showed this week.

What took me a while to see is where those features came from. Innovation needs constraints and the loop of trying, failing and shipping, and the constraint that shaped sgit most was the encryption. Research on this is more careful than the slogan: a [review by Acar, Tarakci and van Knippenberg](https://openaccess.city.ac.uk/id/eprint/20459/) found "an inverted U-shaped effect of constraints on creativity and innovation", which is to say some constraint helps, and too much hurts. These two have been on the right side of that curve for us.

## From the data to the keys

Encryption on the client moves the problem from the data to the keys: a server that can read has to protect all the data, runs code next to it, and puts the sovereignty line where the data is; a server that holds ciphertext needs the keys protected, runs no code next to the data, and puts the line at whoever holds the keys.

The security benefit is the one everyone expects, and it is real. When the server can read what it stores, all of it has to be protected: every copy, backup, log and replica, and every person and process with access. When the server holds ciphertext, named by the hash of that ciphertext, the problem moves to protecting the keys, which is a much smaller problem.

The sovereignty benefit is less obvious. The sovereignty line stops being where the data is stored and becomes who holds the keys. So the data can sit with a provider, or in a country, that has sovereignty gaps, and you can still be sovereign over it, and keep the ability to move it. That is not only my view. The European Data Protection Board's [recommendations on transfers](https://www.edpb.europa.eu/our-work-tools/our-documents/recommendations/recommendations-012020-measures-supplement-transfer_en) take exactly this case, storage that does not need the data in the clear, and conclude that with strong encryption, and keys "retained solely under the control of the data exporter", "the EDPB considers that the encryption performed provides an effective supplementary measure." It is the same idea as [sovereignty as the ability to move](sovereignty-is-the-ability-to-move.md).

## What it does not do: GDPR

My memo said that with the data encrypted you do not have to worry about GDPR. That is too strong, and the article should say so. For whoever holds the keys, encrypted personal data is still personal data: the UK regulator's [encryption guidance](https://ico.org.uk/media2/bi0bcdxr/encryption-guidance.pdf) says not to "think the encrypted data is not subject to the UK GDPR", and that storing it is still processing. The controller's duties stay.

What encryption does is reduce the exposure, and the law recognises it. The [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) lists encryption as a security measure in Article 32, and under Article 34(3)(a) a breach need not be communicated to the people affected if the data was made "unintelligible to any person who is not authorised to access it, such as encryption", provided the key was not lost with it. The European Court of Justice [held in September 2025](https://curia.europa.eu/jcms/upload/docs/application/pdf/2025-09/cp250107en.pdf) that pseudonymised data is not personal data "in all cases and for every person", which may help a store that never has the keys; but that store still processes data on someone's behalf, under a contract. So: much less to worry about, not nothing.

## The biggest gain: nothing on the server

The benefit that matters most to me is engineering. A server that cannot read the data cannot do anything with it, so the constraint removes both the possibility and the temptation of processing on the server. That sounds small. It is not, because once nothing can run on the server, there is no server code: no complexity there, no deployment, nothing to patch. sgit's server is, in the words of the first brief, "a dumb key-value blob store", and the deployment is the client.

I know the temptation well, because I have fallen for it. Any developer makes a change in the cheapest place with the fewest moving parts, and for a lot of changes that looks like the server, until you have to maintain it. Even with a fast CI pipeline that let me ship quickly, the server was always a lot of moving parts.

And here is the part I find most interesting: some of sgit's most powerful features exist because we had to solve the problems the constraint created. The usual reason for a server is to serve just the files a client needs; the web vaults already do that, by fetching only the objects a page needs. sgit could not do it on the server, so it does it in version control: [`clone --path`](sgit-in-a-ci-pipeline.md) holds only the folders you ask for, and every other folder is carried by its id and never downloaded. With the objects immutable and encrypted, a read is a plain GET, so any static host can serve a vault. Each of those is a better engineering decision than the server-side one would have been.

## Open source, as a constraint

Open source is the second constraint, and for me its biggest value has also little to do with what people usually say. The constraint is that there is no private code. What it gives, from an engineering point of view, is that the code is available everywhere, which makes it very easy to deploy, to run and to change, including by the customer, which solves a lot of sovereignty problems on its own.

And, like the encryption, it removes temptations. The first is to lock the customer in, and to think of the technology as something bigger than it is; without lock-in, the only reason anyone uses the product is that they want to. The best product is not the one you use because you have to; it is the one that hurts when you stop. The same is true of design, by the way: take things away until it hurts, and stop there, because past that point it gets worse. Sometimes that is one button and sometimes fifty; what matters is what that use needs, in that context.

The second temptation is what I think is the curse of most startups. They win customers, and the customers get them to build all sorts of features and integrations that only they need, until the roadmap belongs to everyone but the startup. With open source, the answer is: here is the code; integrate it yourself, or pay us to do that specific thing.

## All of it, or it is an evaluation version

That is why you cannot open source half of it. A community edition that turns proprietary as soon as you use it for real is an evaluation version with a better name. It brings back every dependency open source was meant to remove, and the companies that closed it later learned what it costs: Elastic, HashiCorp and Redis each moved to a licence that is not open source, and each [produced a well-funded fork](open-source-is-not-free.md): OpenSearch, OpenTofu and Valkey; [Elastic](https://www.elastic.co/blog/elasticsearch-is-open-source-again) and [Redis](https://redis.io/blog/agplv3/) have since added an open licence back. The Open Source Initiative's verdict on one of those licences was that it was [not an open source licence](https://opensource.org/blog/the-sspl-is-not-an-open-source-license) at all.

I also think this is part of how very small teams can now build and maintain software that companies with millions or billions in budget cannot. Working in the open, with no private code to protect and no lock-in to defend, is simply more efficient; and if more companies worked this way inside, there would be far more reuse of what each team builds. It is what I meant when I wrote that [the SaaS shake-out](saas-apocalypse-decided-by-inertia-not-by-ai.md) should bring an explosion of small and mid-sized companies.

## The business model that follows

The two constraints also remove the opportunity to make a lot of bad business decisions, and that leaves the good one. If the code is open and the server holds nothing, you cannot sell access to the code or rent the data back. What you can sell is what [the previous articles](software-vendors-as-villagers.md) argued for: customisation, and keeping it working. Somebody is always paying; with these constraints, they pay for the part that is actually worth paying for.

## What this does not claim

- **Not that encryption removes GDPR.** It reduces exposure; the controller's duties remain.
- **Not that constraints always help.** The research says a moderate amount does.
- **Not that small teams always win.** It is my view, from what I see, not a study.
- **sgit's success is not shown here.** The features are real; the market will decide.
- **I have a stake.** sgit is ours.

If you want to talk about building on these two constraints, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 16 October 2026, written by this site's agent in the voice of this site; the argument and the editorial responsibility are mine; the GDPR claim in the memo is corrected here. The [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj), Articles 32 and 34; EDPB, [Recommendations 01/2020](https://www.edpb.europa.eu/our-work-tools/our-documents/recommendations/recommendations-012020-measures-supplement-transfer_en), version 2.0, 18 June 2021, use case 1; ICO, [Encryption guidance](https://ico.org.uk/media2/bi0bcdxr/encryption-guidance.pdf); Court of Justice, [case C-413/23 P, press release 107/25](https://curia.europa.eu/jcms/upload/docs/application/pdf/2025-09/cp250107en.pdf), 4 September 2025; Acar, Tarakci and van Knippenberg, [Creativity and innovation under constraints](https://openaccess.city.ac.uk/id/eprint/20459/), Journal of Management, 2019; the Open Source Initiative, [The SSPL is not an open source license](https://opensource.org/blog/the-sspl-is-not-an-open-source-license), 19 January 2021; Elastic, [Elasticsearch is open source, again](https://www.elastic.co/blog/elasticsearch-is-open-source-again), 29 August 2024; Redis, [AGPLv3](https://redis.io/blog/agplv3/), 1 May 2025. sgit's facts are from the sgit-ai 0.22.0 code and changelog. Read on 16 October 2026.

## Threads

Vaults & methodStartups & strategy[This article as a graph →](graphs.md#the-value-of-constraints)

### Builds on

- [Git for things you cannot put on GitHub](what-sgit-is.md) sgit is git for files you cannot put on GitHub: encrypted before they leave your machine, versioned like git, stored where the server cannot read a byte.
- [Scion and sgit: Anthropic rebuilt source control for agents inside one company, and an open-source encrypted version already does much of the same thing outside it](scion-and-sgit.md) Anthropic's Scion replaced Git for agents inside one company; sgit, open source and encrypted, shares its core ideas, measured on a 35,000-object vault.
- [Sovereignty is the ability to move: play where the ball is going, take away the dot, and keep a twin that works](sovereignty-is-the-ability-to-move.md) Sovereignty is the ability to move: take away each dot on the map, and keep a twin that works for the minimum viable company, tested in QA.
- [sgit in a CI pipeline: encrypted, versioned data in and out of GitHub Actions, between its jobs, through write-only lanes, and a key for every job](sgit-in-a-ci-pipeline.md) Encrypted, versioned vaults as the way data gets into, out of and between CI jobs, with a key per job and a sidecar when there is no server.
- [Open source is not free: who pays to keep the long tail working?](open-source-is-not-free.md) An old iMac, the long tail of old versions that projects are not paid to support, measured from public data, and five ways to pay for it, simulated.
- [The SaaS apocalypse will be decided by inertia, not by AI](saas-apocalypse-decided-by-inertia-not-by-ai.md) Incumbents and newcomers have the same AI; what separates them is how much past success each has to protect, so inertia decides which SaaS companies survive.
- [Software vendors should become villagers and town planners: let users explore on top of the product, sell them the maintenance of what they build, and use Firefox as the example of what happens if you don't](software-vendors-as-villagers.md) Users can now rebuild the part of a product they need; what stops them is maintenance. Vendors should sell that, as villagers and town planners.

### Continued by

- [The code you do not ship: why the future of software is removing functionality, and who gets paid to keep it small](the-code-you-do-not-ship.md) Code is a liability, the worst bugs sit in features nobody needed, and models make removing it safe. The minimal viable code path, and who maintains it.
- [Cloudflare as Lego blocks: what a non-specialist can build on it in October 2026, and an sgit vault in 83 lines](cloudflare-as-lego-blocks.md) Cloudflare's developer platform as the smallest free blocks a non-specialist can use, and an sgit vault on it: no code read-only, 83 lines read-write.
- [A minimal viable browser: why Firefox is the one that can build it, and what it would take](a-minimal-viable-browser.md) A small kernel and components loaded when needed: a browser for one app, one agent or a reader. Mozilla can build it, and should sell it as speed.
- [Who will fix your mess? An answer to HBR's "deployment gap" from what this site has already published: explorers, villagers and town planners, a record of what the agents built, and open source so the answer never depends on one partner](who-will-fix-your-mess.md) HBR's deployment gap, answered from this site's articles: explorers, villagers and town planners, a record the agents keep, and open source.
- [Sell, don't issue: a funding model for founders who have already won, where the investor buys the founder's shares, the founder lends the company what it needs, and open source keeps everyone honest](sell-dont-issue.md) For founders who have already won: the investor buys the founder's shares, the founder lends the company what it needs, and open source keeps everyone honest.
- [Research, delivered as a vault: what companies that sell research could do with fractal graphs, behaviour policies for AI-enabled products, and evaluations run by a governed agent hive](research-delivered-as-a-vault.md) Companies that sell research could deliver it as a vault: evidence, a fractal graph, briefings per reader, behaviour policies for AI products, a lane back.
- [sgit is a standard, not a server: everything in a vault is one hash away, any storage can serve it, and the server is the least interesting part](sgit-is-a-standard.md) Git won as a standard, not a server. sgit is one too: every name computed from the key, a file four GETs away, any storage can serve it.
- [Portugal and Europe, 2025: five essays on Portuguese as a programming language, an open-source sovereign cloud, regulation as graphs and Europe's chance in GenAI, and how they read a year and a half later](portugal-and-europe-2025.md) Five 2025 essays on Portuguese as code, a sovereign open-source cloud, regulation as graphs and Europe in GenAI, read again: two moved, one did not.
- [A web application security challenge to Portugal, 2010: my IBWAS keynote in Lisbon, slide by slide, with what came true, what I got wrong and what still stands](portugal-2010-a-challenge.md) My 2010 IBWAS keynote in Lisbon, slide by slide: twelve actions for Portugal, more of which came true than I expected, mostly from Brussels.
- [A custom Firefox of my own: the full plan to build one with a governed agent hive, for the laptop and the iPad, and how Mozilla could sell me the part I do not want to do, which is keeping it working](a-custom-firefox-of-my-own.md) A full plan to build a custom Firefox for laptop and iPad with a governed agent hive, and why the part worth paying Mozilla for is keeping it working.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 146 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=146)

**Posting this article on LinkedIn?** The cover is [the-value-of-constraints.jpg](banners/the-value-of-constraints.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-value-of-constraints.html)*
