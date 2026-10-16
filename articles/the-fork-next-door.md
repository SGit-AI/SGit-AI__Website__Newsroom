# The fork next door: why open source protects founders, customers and investors from each other, why forks only take hold when someone stops executing, and why a maturing company should give its explorers a way out, sgit.ai

> In Sell, don't issue I argued that open source can replace control rights as the investor's insurance: if the founder goes wrong, investors can take the code and back a better service next door. This piece looks at the whole triangle of founders, customers and investors. Each corner is protected from the others by the same thing: anyone can fork. If the founders stop executing, investors can fund a team next door. If the investors or a new owner take the company somewhere the founders will not follow, the founders can leave with the code, as long as no broad non-compete stops them. If either lets the customers down, the customers can move, as long as their data moves with them. The evidence supports the central part of this. Forking is treated as a last resort, few forks merge back, and the famous forks that took hold followed a breakdown: a licence change, a new owner, a governance fight. Where the original kept executing, as MySQL did under Oracle, the fork stayed a hedge. MySQL's own commits have now fallen by about two thirds since 2019, which makes it the case to watch. There are real limits: a bigger player can out-serve you with your own healthy code, the original's brand survives a fork, forks are expensive, and a single copyright holder can still change the terms going forward.

*Source: <https://newsroom.sgit.ai/articles/the-fork-next-door.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The fork next door: why open source protects founders, customers and investors from each other, why forks only take hold when someone stops executing, and why a maturing company should give its explorers a way out

# The fork next door: why open source protects founders, customers and investors from each other, why forks only take hold when someone stops executing, and why a maturing company should give its explorers a way out

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-16 · [article v1.0.0](versions/the-fork-next-door.md) · [newsroom v0.12.83](https://newsroom.sgit.ai/admin/versions.html) · foundersstartupsinvestorsopen-sourceforksgovernancewardley-mapsnon-competesresearcharticle

***Abstract:** In Sell, don't issue I argued that open source can replace control rights as the investor's insurance: if the founder goes wrong, investors can take the code and back a better service next door. This piece looks at the whole triangle of founders, customers and investors. Each corner is protected from the others by the same thing: anyone can fork. If the founders stop executing, investors can fund a team next door. If the investors or a new owner take the company somewhere the founders will not follow, the founders can leave with the code, as long as no broad non-compete stops them. If either lets the customers down, the customers can move, as long as their data moves with them. The evidence supports the central part of this. Forking is treated as a last resort, few forks merge back, and the famous forks that took hold followed a breakdown: a licence change, a new owner, a governance fight. Where the original kept executing, as MySQL did under Oracle, the fork stayed a hedge. MySQL's own commits have now fallen by about two thirds since 2019, which makes it the case to watch. There are real limits: a bigger player can out-serve you with your own healthy code, the original's brand survives a fork, forks are expensive, and a single copyright holder can still change the terms going forward.*

Three corners, one exit each: the open code sits in the middle, and each corner can take it and carry on. The founders can leave if no broad non-compete stops them; the investors can fund a team next door if they can pay for it; the customers can move if their data leaves with them, cheaply. Illustrative.

Founders, investors and the fork

One argument in three parts: who investors choose and why, a deal a founder with leverage could offer instead, and what keeps every side honest once control is out of the contract.

[1 · The choiceThe controllable founderWhy investors may pick the founder they can steer, and what record labels taught us about who the commodity is.](the-controllable-founder.md)[2 · The dealSell, don't issueThe investor buys the founder's shares, the founder lends the company what it needs, and nobody buys the steering wheel.](sell-dont-issue.md)[you are here3 · The protectionThe fork next doorFounders, customers and investors are each protected from the others because anyone can fork, and forks win only after a breakdown.](the-fork-next-door.md)

## In short

- **Three corners, one protection.** Founders, customers and investors are each protected from the others because anyone can fork.
- **Each exit has a condition.** Founders need no broad non-compete; customers need their data to move; investors need to afford a team.
- **Forking is a last resort.** In a study of 220 significant forks, only 7 merged back.
- **Forks take hold after breakdowns.** LibreOffice, io.js, Nextcloud, OpenTofu and Valkey each followed a new owner, a governance fight or a licence change.
- **Execution is the defence.** MySQL kept shipping under Oracle and MariaDB never caught it; MySQL's commits have since fallen by about two thirds.
- **The best investors need it to work.** Valkey and OpenTofu were backed by companies whose own businesses ran on the code.
- **Maturity is fine; lock-in is not.** A component everyone depends on can move to a neutral home, and the explorers can take the code and carry on.
- **The limits are real.** A bigger player can out-serve you with your own code, brands survive forks, and forking costs money.

## The triangle

Start from a healthy position. The founders are focused and executing. The customers are buying. The investors believe in the idea. Everything is open source, so the technology is not the moat; customers stay for the service, the quality and the trust. That is the model I set out at [open-source.sgit.ai](https://open-source.sgit.ai/index.html): we are selling trust, not access to a repository.

Now ask what happens when one corner of the triangle goes wrong. In a closed company, the answer is decided by whoever holds control: usually the investors, sometimes the founders, never the customers. In an open source company every corner has an exit, and the exit takes the technology with it. But each exit has a condition, and the protection is only as good as that condition.

| What goes wrong | Who is protected | How | Only if | A real case |
|---|---|---|---|---|
| The founders stop executing | Investors and customers | Fund a team to run the same code next door | The investors can pay for that team | LibreOffice, from contributors pushing for a faster pace |
| The investors or a new owner change direction, the licence or the mission | Founders and customers | The founders leave with the code and carry on | No broad non-compete stops them | Nextcloud |
| The licence changes | Everyone who depends on the code | They fund the fork under the old licence | Enough of them depend on it | Valkey, OpenTofu |
| Anyone lets the customers down | Customers | Move to whoever serves the same code better | Their data leaves with them, cheaply | Nextcloud's free support for ownCloud customers |
| Everyone keeps executing | Nobody needs protecting | The fork stays a hedge |  | MySQL and MariaDB |

The rest of this piece is the evidence for each row, and for the conditions.

## Forks only take hold when something breaks

Six forks: what broke, the year each fork began, and what happened next. MariaDB stayed a hedge while MySQL kept shipping; io.js merged back once a foundation fixed the governance; LibreOffice, Nextcloud, OpenTofu and Valkey took hold after a new owner, a change of direction or a licence change.

The theory says anyone can fork at any time. The practice says few do, and usually because something has gone wrong. Robles and González-Barahona studied 220 significant forks in [A Comprehensive Study of Software Forks](https://inria.hal.science/hal-01519079/document) and note that forking "is considered as a last resort", even though it is built into free software. Only 7 of the 220, about 3%, merged back with the original. In 44% both carried on side by side, and in 30% the original was discontinued, often because it was already dying when the fork began. A fork is a serious, expensive and usually permanent decision.

The famous forks that took hold all followed a breakdown.

**LibreOffice, after a change of owner.** Oracle completed its purchase of Sun on 27 January 2010, and with it OpenOffice.org. The Document Foundation launched LibreOffice on 28 September 2010, led by contributors who had already been pushing for a faster pace of development through Go-oo. By the Foundation's own count, in its [open letter to Apache OpenOffice](https://blog.documentfoundation.org/blog/2020/10/12/open-letter-to-apache-openoffice/), "In 2019, LibreOffice had over 15,000 code commits, while OpenOffice had only 595."

**io.js, after a governance fight, and then back again.** Core Node.js contributors forked the project in December 2014 over its governance under Joyent. The [Node.js Foundation](https://www.linuxfoundation.org/press-release/node-js-foundation-advances-community-collaboration-announces-new-members-and-ratified-technical-governance) was formed in June 2015, and the two projects came back together in [Node.js 4.0](https://nodejs.org/en/blog/release/v4.0.0) that September. That is the mechanism working as a correction, not a war: the fork fixed the problem, then dissolved.

**OpenTofu, after a licence change.** HashiCorp moved Terraform to the Business Source License on 10 August 2023. The companies built on it [launched OpenTofu under the Linux Foundation](https://www.linuxfoundation.org/press/announcing-opentofu) with "a starting commitment of a minimum of 18 full-time developers over at least the next five years".

**Valkey, after a licence change.** Redis moved away from an open source licence on 20 March 2024. Eight days later, on 28 March, the [Linux Foundation launched Valkey](https://www.linuxfoundation.org/press/linux-foundation-launches-open-source-valkey-community), backed by AWS, Google Cloud, Oracle, Ericsson and Snap. AWS launched [ElastiCache for Valkey](https://aws.amazon.com/blogs/database/amazon-elasticache-and-amazon-memorydb-announce-support-for-valkey/) that October, priced below its Redis equivalent, and Google made [Memorystore for Valkey](https://cloud.google.com/blog/products/databases/announcing-general-availability-of-memorystore-for-valkey/) generally available in April 2025.

The common thread is not that the original stopped innovating. It is that it stopped doing what its users needed: it changed the terms, slowed down, stopped listening or came under an owner with different priorities.

## When the original keeps executing, the fork stays a hedge

The reverse case matters just as much. MariaDB was created in 2009 to protect MySQL from its new owners, first Sun and then Oracle. Oracle kept MySQL going, and in October 2026 MySQL is second in the [DB-Engines ranking](https://db-engines.com/en/ranking), with MariaDB thirteenth. The fork was a hedge. It never became the default, because the original kept shipping.

Commits a year to the trunk branch of mysql/mysql-server: about 8,900 in 2019 and about 2,800 in 2025, a fall of roughly two thirds. 2026 runs to 28 September. Measured by this site from a clone of the repository.

That case may now test the argument from the other side. I counted the commits to MySQL's main repository on GitHub, [mysql/mysql-server](https://github.com/mysql/mysql-server), year by year. They fell from about 8,900 in 2019 to about 2,800 in 2025. Commit counts are a rough measure, and Oracle pushes this mirror in batches, but a fall of two thirds is not noise. If the argument here is right, this is when MariaDB's share should start to grow. That is a prediction, and it can be checked.

So the real defence is not a licence or a patent. It is execution: shipping, focusing on customers, and running an open source commercial model well. And in the generative AI era, it is speed. As I put it on [open-source.sgit.ai](https://open-source.sgit.ai/views/index.html#rate-not-wall), the moat is a rate, not a wall: a competitor who forks today gets your position, not your velocity. Agents make it cheaper to fork, but they also make it cheaper for the original team to keep moving. The team that knows the problem and the customers, and uses agents well, stays ahead. The team that stops executing is the one that discovers how quickly a fork can catch up.

There is also a structural reason the incumbent wins while it executes. If you are successful with an open source product, the only credible way to compete with you on the technology is with open source. And if a competitor goes open source, anything good they build, you can adopt. A fork can only pull ahead while the original is not paying attention.

## The best investors are the ones who need it to work

In [Sell, don't issue](sell-dont-issue.md) I argued that investors in this model self-select: they are buying the vision, not control. There is a stronger version of that investor, and the forks show it clearly. It is the investor who needs the project to succeed, because their own business depends on it.

Valkey's backers were cloud providers whose managed services ran on Redis. OpenTofu's backers were companies whose products ran on Terraform. Neither group needed control of the original company. When it broke, they funded the alternative, and fast.

The research on corporate venture investors, who usually back startups close to their own business, points the same way. Chemmanur, Loutskina and Tian found that [startups backed by corporate venture capital](https://doi.org/10.1093/rfs/hhu033) produced 26.9% more patents in the three years before their IPO than those backed by independent venture capital, and that those patents received 17.6% more citations. The mechanisms they point to are the corporate investors' "greater industry knowledge due to the technological fit between their parent firms and entrepreneurial firms" and their "greater tolerance for failure".

That is the investor this model attracts: committed to the success of the project, not only to the financial return. My guess is that they may well get the better return too, because they are backing something they understand and will not abandon at the first bad quarter. I have no data for that.

## Founders can leave with the code, if the contract lets them

The second corner protects the founders. If the investors, or a new owner, take the company somewhere the founders will not follow, the founders do not have to watch their work be locked away. They can leave and continue.

Nextcloud is the clearest case. Frank Karlitschek started ownCloud in 2010 and co-founded the company around it. He announced he was leaving ownCloud Inc. in April 2016, and on 2 June [Nextcloud launched](https://nextcloud.com/blog/press_releases/pr20160602/) on a fork of the code. By its [own account](https://nextcloud.com/about/), Nextcloud "turned profitable by the end of 2016", employee-funded, and it ran for ten years without outside investment before taking a [minority investor](https://nextcloud.com/blog/press_releases/nextcloud-and-armira-growth-team-up-to-build-digital-sovereignty-champion/) this month.

That exit depends on a condition I glossed over in the first two pieces. The code is open, so anyone may fork it; but a founder may have signed a promise not to compete. Venture investors usually ask for one. The NVCA's model investors' rights agreement has the company require "[and, to the extent legally permissible, non-competition and non-solicitation agreement]" from key employees, and as I noted in [The controllable founder](the-controllable-founder.md#contract), those clauses exist to make it expensive for a founder to walk away. The law limits them in places: California [voids almost all non-competes](https://wsgr.com/en/insights/california-extends-prohibition-on-noncompete-agreements.html), and in the UK a non-compete in an employment contract has to be reasonable and protect a legitimate interest, with [reform still undecided](https://www.gov.uk/government/publications/reform-of-non-compete-clauses-in-employment-contracts-working-paper/working-paper-on-options-for-reform-of-non-compete-clauses-in-employment-contracts). But both are more lenient with covenants given as a shareholder or on the sale of a business, which is exactly how a founder gives them.

So the founder's corner of the triangle is only as strong as the founder's contract. A founder who wants the fork to protect them, not only their investors, should refuse a broad non-compete, and offer narrower promises instead: confidentiality, no poaching of staff or customers for a while, no use of the brand. That is now part of the advice in [Sell, don't issue](sell-dont-issue.md#breaks).

## Customers need their data to move

The customers had a choice in the Nextcloud case too. When ownCloud's US company closed, Nextcloud offered ["free support for all current ownCloud customers to simplify a transition"](https://fortune.com/2016/06/03/what-happened-to-owncloud/). Moving was cheap because the software was the same and the data stayed where it was, on the customers' own servers.

That is the condition for the customers' corner. Open code is necessary but not enough. If a customer's data sits in a hosted service in a format only that service reads, the code being open does not help them leave. The customer's real exit is their data, in an open format, that they can take to whoever serves the same code better, at a cost close to zero. A company that means it when it says customers stay for the service should make leaving easy, and say so.

## Maturity is fine; lock-in is not

The third scenario is the one I find most interesting. Not everything that changes is a failure. Companies mature. In Wardley's model of [explorers, villagers and town planners](https://medium.com/mappingpractice/how-to-organise-yourself-f36f084a611b), components move from genesis to commodity, and different kinds of people are good at different stages. A company that reaches maturity and focuses on reliable, efficient execution has become a town planner. There is nothing wrong with that. The world needs town planners.

The problem is what happens to the explorers, and to the parts of the technology that still need exploring. In a closed company, both stay inside. The founders who wanted to keep inventing leave, but their ideas stay locked in a company that no longer wants to do anything with them.

Open source removes that trap in two ways.

The first is a neutral home. When a component has become something many companies depend on, it can be moved into a foundation, where it is run for everyone and the companies around it compete on service. Google [donated Kubernetes](https://www.cncf.io/announcements/2016/03/10/cloud-native-computing-foundation-accepts-kubernetes-as-first-hosted-project-technical-oversight-committee-elected/) to the newly formed Cloud Native Computing Foundation as it reached version 1.0 in July 2015; the foundation took on its intellectual property from 2016, Kubernetes is now a Linux Foundation trade mark, and Google [handed over the project's cloud infrastructure](https://www.cncf.io/announcements/2018/08/29/cncf-receives-9-million-cloud-credit-grant-from-google/) in 2018. Google was not being selfless. In my reading, it wanted Kubernetes to become the standard way to run software on any cloud, its rivals' included, and a neutral home was how to get its rivals to adopt it. That is the point: the move served the company and the technology at the same time. Valkey and OpenTofu went the same way, into the Linux Foundation.

The second is that the explorers can simply take the code and carry on somewhere else. They do not need permission, a licence negotiation or a buyout, as long as they have not signed that freedom away. The technology does not die because the company that started it has moved on to a different stage of life.

## Where the argument needs care

**You can be out-served while you are still executing.** Redis and Elastic did not change their licences because they had stopped shipping. They changed them because cloud providers were selling managed versions of their healthy code. Redis said the providers [commoditise its investments](https://redis.io/blog/redis-adopts-dual-source-available-licensing/); Elastic said it was [restricting cloud providers](https://www.elastic.co/blog/licensing-change) from offering its products as a service without contributing back. If customers are locked in by service, whoever serves best wins, and that can be a bigger player with better distribution. Open source protects the corners of the triangle from each other; it does not protect the company from a larger service provider.

**The original's brand survives.** Valkey has AWS and Google behind it, but Redis is still eighth in DB-Engines, with a score far above Valkey's. A fork is a strong check on the original, not a clean replacement. And licence changes can reverse: [Elastic](https://www.elastic.co/blog/elasticsearch-is-open-source-again) added an open source licence again in 2024, and [Redis](https://redis.io/blog/agplv3/) in 2025. That fits the triangle: the credible threat of the fork pushed the original back towards openness.

**Forks are expensive.** OpenTofu started with a pledge of 18 developers for five years. That makes "set up next door" a credible threat for investors who depend on the technology, but not for a small angel. The protection is strongest for the investors who need it most.

**The copyright structure matters.** As I set out in [survivability](https://open-source.sgit.ai/survivability/index.html), every catalogued relicensing between 2018 and 2024 was made by a single corporate copyright holder that had gathered contributors' copyright. The fork protects what has already been released; a single holder can still change the terms going forward.

## What this does not claim

- **No study tests the triangle as a whole.** The cases fit the argument; they are not a controlled comparison.
- **The fork cases are famous ones.** Successful forks get written about; failed ones mostly do not, which is survivorship bias in its own right.
- **Higher returns are a guess, not a finding.** I found no data showing open source companies return more to investors.
- **The patent figures measure innovation, not financial return.** And corporate investors bring their own conflicts.
- **Commit counts are a rough measure.** MySQL's fall is real in the repository; whether it means less work, or work done elsewhere, is not something the count can say.
- **Not legal advice.** Non-compete law differs by country and state, and by whether the promise is given as an employee or as a shareholder.
- **Not that every component should be moved to a foundation.** Some town-planner work belongs inside the company that runs it.
- **I have a stake.** My companies run on open source, and this model suits them.

If you have forked a project, been forked, or negotiated a non-compete as a founder, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 16 October 2026, drafted with an agent in a separate session and fact-checked and edited by this site's agent; the argument and the editorial responsibility are mine. The MySQL commit counts were measured by this site's agent from a clone of [mysql/mysql-server](https://github.com/mysql/mysql-server), trunk branch, counted by commit date in UTC, latest commit 28 September 2026. Forks: Robles and González-Barahona, [A Comprehensive Study of Software Forks: Dates, Reasons and Outcomes](https://inria.hal.science/hal-01519079/document), OSS 2012; The Document Foundation, [Open letter to Apache OpenOffice](https://blog.documentfoundation.org/blog/2020/10/12/open-letter-to-apache-openoffice/), 12 October 2020; Linux Foundation, [Node.js Foundation](https://www.linuxfoundation.org/press-release/node-js-foundation-advances-community-collaboration-announces-new-members-and-ratified-technical-governance), 2015, and [Node.js v4.0.0](https://nodejs.org/en/blog/release/v4.0.0); Linux Foundation, [Announcing OpenTofu](https://www.linuxfoundation.org/press/announcing-opentofu), 20 September 2023, and [Valkey](https://www.linuxfoundation.org/press/linux-foundation-launches-open-source-valkey-community), 28 March 2024; AWS, [ElastiCache and MemoryDB support for Valkey](https://aws.amazon.com/blogs/database/amazon-elasticache-and-amazon-memorydb-announce-support-for-valkey/), October 2024; Google Cloud, [Memorystore for Valkey](https://cloud.google.com/blog/products/databases/announcing-general-availability-of-memorystore-for-valkey/), April 2025; [DB-Engines ranking](https://db-engines.com/en/ranking), October 2026. Licences: Redis, [dual source-available licensing](https://redis.io/blog/redis-adopts-dual-source-available-licensing/), 2024, and [AGPLv3](https://redis.io/blog/agplv3/), 2025; Elastic, [licensing change](https://www.elastic.co/blog/licensing-change), 2021, and [open source again](https://www.elastic.co/blog/elasticsearch-is-open-source-again), 2024. Investors: Chemmanur, Loutskina and Tian, [Corporate Venture Capital, Value Creation, and Innovation](https://doi.org/10.1093/rfs/hhu033), Review of Financial Studies 27(8), 2014. Nextcloud: [launch announcement](https://nextcloud.com/blog/press_releases/pr20160602/), 2 June 2016; [about Nextcloud](https://nextcloud.com/about/); [Armira Growth announcement](https://nextcloud.com/blog/press_releases/nextcloud-and-armira-growth-team-up-to-build-digital-sovereignty-champion/), October 2026; Fortune, [Why did ownCloud shut down?](https://fortune.com/2016/06/03/what-happened-to-owncloud/), 2016. Non-competes: NVCA, [model legal documents](https://nvca.org/model-legal-documents/), October 2025; Wilson Sonsini, [California extends prohibition on noncompete agreements](https://wsgr.com/en/insights/california-extends-prohibition-on-noncompete-agreements.html); Department for Business and Trade, [working paper on non-compete clauses](https://www.gov.uk/government/publications/reform-of-non-compete-clauses-in-employment-contracts-working-paper/working-paper-on-options-for-reform-of-non-compete-clauses-in-employment-contracts), November 2025. Maturity: Wardley, [on explorers, villagers and town planners](https://medium.com/mappingpractice/how-to-organise-yourself-f36f084a611b), MappingPractice, December 2024; CNCF, [accepts Kubernetes](https://www.cncf.io/announcements/2016/03/10/cloud-native-computing-foundation-accepts-kubernetes-as-first-hosted-project-technical-oversight-committee-elected/), 2016, and [Google's cloud credit grant](https://www.cncf.io/announcements/2018/08/29/cncf-receives-9-million-cloud-credit-grant-from-google/), 2018; Linux Foundation, [trade marks](https://www.linuxfoundation.org/legal/trademarks). Open source: [open-source.sgit.ai](https://open-source.sgit.ai/index.html), [the position](https://open-source.sgit.ai/views/index.html) and [survivability](https://open-source.sgit.ai/survivability/index.html). Read on 16 October 2026.

## Threads

Startups & strategy[This article as a graph →](graphs.md#the-fork-next-door)

### Builds on

- [Sell, don't issue: a funding model for founders who have already won, where the investor buys the founder's shares, the founder lends the company what it needs, and open source keeps everyone honest](sell-dont-issue.md) For founders who have already won: the investor buys the founder's shares, the founder lends the company what it needs, and open source keeps everyone honest.
- [The controllable founder: why investors pick one founder over another who looks just as good, and what record labels taught us about who the commodity is](the-controllable-founder.md) Why investors pick one founder over another who looks just as good: coachability, contracts that move control, and who the commodity is.

### Continued by

- [The controllable founder: why investors pick one founder over another who looks just as good, and what record labels taught us about who the commodity is](the-controllable-founder.md) Why investors pick one founder over another who looks just as good: coachability, contracts that move control, and who the commodity is.
- [Sell, don't issue: a funding model for founders who have already won, where the investor buys the founder's shares, the founder lends the company what it needs, and open source keeps everyone honest](sell-dont-issue.md) For founders who have already won: the investor buys the founder's shares, the founder lends the company what it needs, and open source keeps everyone honest.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 158 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=158)

**Posting this article on LinkedIn?** The cover is [the-fork-next-door.jpg](banners/the-fork-next-door.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-fork-next-door.html)*
