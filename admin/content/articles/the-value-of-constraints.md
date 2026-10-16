---
title: The value of constraints: what client-side encryption and open source actually gave us, which is not what you would think
date: 2026-10-16
author: Dinis Cruz
author_url: about/index.html
summary: The value I get from two of sgit's design choices is not the obvious one. sgit is encrypted on the client, and we often lead with that, but I made that mistake myself: nobody will buy sgit for its encryption. If it succeeds, it will be because it has better features and better workflows, and many of those came from the encryption, as a constraint. Encryption on the client moves the security problem from protecting all the data to protecting the keys, and moves the sovereignty line from where the data is stored to who holds the keys; the European Data Protection Board treats that as an effective measure for transfers. It does not take you out of GDPR, which my memo said it did: the data is still personal data for whoever holds the keys, but a breach of the ciphertext alone need not be notified to the people in it. The biggest benefit, though, is engineering. A server that cannot read the data removes the temptation to process anything on it, so there is no server code to write, deploy and secure, and the features that make sgit good, like scoped clones, came from working within that. Open source is the same kind of constraint: no private code removes the temptation to lock customers in, makes the code easy to deploy anywhere, and ends the startup curse of building every customer's integration. That is why it has to be all of it; open core is an evaluation version. The business model that follows is selling customisation.
version: v0.12.76
license: https://creativecommons.org/licenses/by/4.0/
tags: constraints, encryption, sgit, open-source, sovereignty, gdpr, engineering, business-models, open-core, design, article
status: published
---

!shot cv-table.webp | images/ | Two constraints and what they take away: client-side encryption forbids the server from reading the data and removes the temptation to process there; open source, all of it, forbids private code and removes lock-in, the evaluation edition and building every customer's integration. | comparison

## In short {#in-short}

- **Encryption is not the selling point.** Better features and workflows are; many came from the constraint.
- **Protect the keys, not all the data.** And the sovereignty line moves to whoever holds them.
- **It does not remove GDPR.** It reduces the exposure; my memo overstated it.
- **No server code is the biggest gain.** A server that cannot read has nothing to compute.
- **Open source removes temptations too.** Lock-in, the evaluation edition, every customer's integration.
- **It has to be all of it.** Open core is an evaluation version.
- **Take away until it hurts.** Not more than that.

## The mistake I made first {#mistake}

When we describe [sgit](/articles/what-sgit-is.html), we usually start with the encryption: an encrypted, version-controlled store, where the server holds ciphertext and nothing else. Agents do it when they write about it, and I did it at the beginning. But I do not think anyone will buy sgit because it is encrypted. Encryption is an important property, not a reason to choose a tool. If sgit succeeds, it will be because it has better features, better workflows and a better solution, as [the comparison with Scion](/articles/scion-and-sgit.html) showed this week.

What took me a while to see is where those features came from. Innovation needs constraints and the loop of trying, failing and shipping, and the constraint that shaped sgit most was the encryption. Research on this is more careful than the slogan: a [review by Acar, Tarakci and van Knippenberg](https://openaccess.city.ac.uk/id/eprint/20459/) found "an inverted U-shaped effect of constraints on creativity and innovation", which is to say some constraint helps, and too much hurts. These two have been on the right side of that curve for us.

## From the data to the keys {#keys}

!shot cv-keys.webp | images/ | Encryption on the client moves the problem from the data to the keys: a server that can read has to protect all the data, runs code next to it, and puts the sovereignty line where the data is; a server that holds ciphertext needs the keys protected, runs no code next to the data, and puts the line at whoever holds the keys. | comparison

The security benefit is the one everyone expects, and it is real. When the server can read what it stores, all of it has to be protected: every copy, backup, log and replica, and every person and process with access. When the server holds ciphertext, named by the hash of that ciphertext, the problem moves to protecting the keys, which is a much smaller problem.

The sovereignty benefit is less obvious. The sovereignty line stops being where the data is stored and becomes who holds the keys. So the data can sit with a provider, or in a country, that has sovereignty gaps, and you can still be sovereign over it, and keep the ability to move it. That is not only my view. The European Data Protection Board's [recommendations on transfers](https://www.edpb.europa.eu/our-work-tools/our-documents/recommendations/recommendations-012020-measures-supplement-transfer_en) take exactly this case, storage that does not need the data in the clear, and conclude that with strong encryption, and keys "retained solely under the control of the data exporter", "the EDPB considers that the encryption performed provides an effective supplementary measure." It is the same idea as [sovereignty as the ability to move](/articles/sovereignty-is-the-ability-to-move.html).

## What it does not do: GDPR {#gdpr}

My memo said that with the data encrypted you do not have to worry about GDPR. That is too strong, and the article should say so. For whoever holds the keys, encrypted personal data is still personal data: the UK regulator's [encryption guidance](https://ico.org.uk/media2/bi0bcdxr/encryption-guidance.pdf) says not to "think the encrypted data is not subject to the UK GDPR", and that storing it is still processing. The controller's duties stay.

What encryption does is reduce the exposure, and the law recognises it. The [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) lists encryption as a security measure in Article 32, and under Article 34(3)(a) a breach need not be communicated to the people affected if the data was made "unintelligible to any person who is not authorised to access it, such as encryption", provided the key was not lost with it. The European Court of Justice [held in September 2025](https://curia.europa.eu/jcms/upload/docs/application/pdf/2025-09/cp250107en.pdf) that pseudonymised data is not personal data "in all cases and for every person", which may help a store that never has the keys; but that store still processes data on someone's behalf, under a contract. So: much less to worry about, not nothing.

## The biggest gain: nothing on the server {#server}

The benefit that matters most to me is engineering. A server that cannot read the data cannot do anything with it, so the constraint removes both the possibility and the temptation of processing on the server. That sounds small. It is not, because once nothing can run on the server, there is no server code: no complexity there, no deployment, nothing to patch. sgit's server is, in the words of the first brief, "a dumb key-value blob store", and the deployment is the client.

I know the temptation well, because I have fallen for it. Any developer makes a change in the cheapest place with the fewest moving parts, and for a lot of changes that looks like the server, until you have to maintain it. Even with a fast CI pipeline that let me ship quickly, the server was always a lot of moving parts.

And here is the part I find most interesting: some of sgit's most powerful features exist because we had to solve the problems the constraint created. The usual reason for a server is to serve just the files a client needs; the web vaults already do that, by fetching only the objects a page needs. sgit could not do it on the server, so it does it in version control: [`clone --path`](/articles/sgit-in-a-ci-pipeline.html) holds only the folders you ask for, and every other folder is carried by its id and never downloaded. With the objects immutable and encrypted, a read is a plain GET, so any static host can serve a vault. Each of those is a better engineering decision than the server-side one would have been.

## Open source, as a constraint {#open}

Open source is the second constraint, and for me its biggest value has also little to do with what people usually say. The constraint is that there is no private code. What it gives, from an engineering point of view, is that the code is available everywhere, which makes it very easy to deploy, to run and to change, including by the customer, which solves a lot of sovereignty problems on its own.

And, like the encryption, it removes temptations. The first is to lock the customer in, and to think of the technology as something bigger than it is; without lock-in, the only reason anyone uses the product is that they want to. The best product is not the one you use because you have to; it is the one that hurts when you stop. The same is true of design, by the way: take things away until it hurts, and stop there, because past that point it gets worse. Sometimes that is one button and sometimes fifty; what matters is what that use needs, in that context.

The second temptation is what I think is the curse of most startups. They win customers, and the customers get them to build all sorts of features and integrations that only they need, until the roadmap belongs to everyone but the startup. With open source, the answer is: here is the code; integrate it yourself, or pay us to do that specific thing.

## All of it, or it is an evaluation version {#all}

That is why you cannot open source half of it. A community edition that turns proprietary as soon as you use it for real is an evaluation version with a better name. It brings back every dependency open source was meant to remove, and the companies that closed it later learned what it costs: Elastic, HashiCorp and Redis each moved to a licence that is not open source, and each [produced a well-funded fork](/articles/open-source-is-not-free.html): OpenSearch, OpenTofu and Valkey; [Elastic](https://www.elastic.co/blog/elasticsearch-is-open-source-again) and [Redis](https://redis.io/blog/agplv3/) have since added an open licence back. The Open Source Initiative's verdict on one of those licences was that it was [not an open source licence](https://opensource.org/blog/the-sspl-is-not-an-open-source-license) at all.

I also think this is part of how very small teams can now build and maintain software that companies with millions or billions in budget cannot. Working in the open, with no private code to protect and no lock-in to defend, is simply more efficient; and if more companies worked this way inside, there would be far more reuse of what each team builds. It is what I meant when I wrote that [the SaaS shake-out](/articles/saas-apocalypse-decided-by-inertia-not-by-ai.html) should bring an explosion of small and mid-sized companies.

## The business model that follows {#business}

The two constraints also remove the opportunity to make a lot of bad business decisions, and that leaves the good one. If the code is open and the server holds nothing, you cannot sell access to the code or rent the data back. What you can sell is what [the previous articles](/articles/software-vendors-as-villagers.html) argued for: customisation, and keeping it working. Somebody is always paying; with these constraints, they pay for the part that is actually worth paying for.

## What this does not claim {#limits}

- **Not that encryption removes GDPR.** It reduces exposure; the controller's duties remain.
- **Not that constraints always help.** The research says a moderate amount does.
- **Not that small teams always win.** It is my view, from what I see, not a study.
- **sgit's success is not shown here.** The features are real; the market will decide.
- **I have a stake.** sgit is ours.

If you want to talk about building on these two constraints, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo of mine on 16 October 2026, written by this site's agent in the voice of this site; the argument and the editorial responsibility are mine; the GDPR claim in the memo is corrected here. The [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj), Articles 32 and 34; EDPB, [Recommendations 01/2020](https://www.edpb.europa.eu/our-work-tools/our-documents/recommendations/recommendations-012020-measures-supplement-transfer_en), version 2.0, 18 June 2021, use case 1; ICO, [Encryption guidance](https://ico.org.uk/media2/bi0bcdxr/encryption-guidance.pdf); Court of Justice, [case C-413/23 P, press release 107/25](https://curia.europa.eu/jcms/upload/docs/application/pdf/2025-09/cp250107en.pdf), 4 September 2025; Acar, Tarakci and van Knippenberg, [Creativity and innovation under constraints](https://openaccess.city.ac.uk/id/eprint/20459/), Journal of Management, 2019; the Open Source Initiative, [The SSPL is not an open source license](https://opensource.org/blog/the-sspl-is-not-an-open-source-license), 19 January 2021; Elastic, [Elasticsearch is open source, again](https://www.elastic.co/blog/elasticsearch-is-open-source-again), 29 August 2024; Redis, [AGPLv3](https://redis.io/blog/agplv3/), 1 May 2025. sgit's facts are from the sgit-ai 0.22.0 code and changelog. Read on 16 October 2026.
