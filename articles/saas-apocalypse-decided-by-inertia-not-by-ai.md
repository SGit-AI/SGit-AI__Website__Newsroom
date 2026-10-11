# The SaaS apocalypse will be decided by inertia, not by AI, sgit.ai

> The SaaS apocalypse has not happened yet, and the market has already declared it cancelled once. It remains a very strong possibility, argued here with data rather than vibes. Most users were never happy, most features were never used, and most licences sit idle, because success bred inertia and inertia bred lock-in. Now anybody can brief the software they actually want, and the portability, APIs and schemas that SaaS companies refused to build are precisely what an agent needs. It will be decided by inertia, not by AI, because AI is available to both sides: the incumbents have the same models as the newcomers, plus more data, more engineers and more money, and if the technology were the deciding factor they would already have won. Nokia when the mobile phone arrived had nothing to protect, and moved. Nokia when the iPhone arrived had fifteen years of success to protect, and did not. Which side of that path each SaaS provider ends up on will be settled by where it sits on the evolution axis and how much it has to protect, which is why the newcomers, not the incumbents, are the ones to watch.

*Source: <https://newsroom.sgit.ai/articles/saas-apocalypse-decided-by-inertia-not-by-ai.html> · sgit.ai v0.7.45 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The SaaS apocalypse will be decided by inertia, not by AI

# The SaaS apocalypse will be decided by inertia, not by AI

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-09-21 · [article v1.5.0, 8 versions](versions/saas-apocalypse-decided-by-inertia-not-by-ai.md) · [sgit.ai v0.4.2](https://sgit.ai/admin/versions.md) · saasstrategywardley-mapsagentsarticle

***Abstract:** The SaaS apocalypse has not happened yet, and the market has already declared it cancelled once. It remains a very strong possibility, argued here with data rather than vibes. Most users were never happy, most features were never used, and most licences sit idle, because success bred inertia and inertia bred lock-in. Now anybody can brief the software they actually want, and the portability, APIs and schemas that SaaS companies refused to build are precisely what an agent needs. It will be decided by inertia, not by AI, because AI is available to both sides: the incumbents have the same models as the newcomers, plus more data, more engineers and more money, and if the technology were the deciding factor they would already have won. Nokia when the mobile phone arrived had nothing to protect, and moved. Nokia when the iPhone arrived had fifteen years of success to protect, and did not. Which side of that path each SaaS provider ends up on will be settled by where it sits on the evolution axis and how much it has to protect, which is why the newcomers, not the incumbents, are the ones to watch.*

The incumbent and the newcomer are carrying the same AI. What differs is the ball and chain of past success, and the fact that the newcomer was never on the rails in the first place.

Here is the claim, stated so it can be wrong. **Most medium and large SaaS companies will struggle, spectacularly, in the medium term**, as companies and individuals build more of what they actually want instead of renting an approximation of it. Whether they survive depends on what they do next. Whether the companies that come out on top are the ones on top today is an open question, and so is whether there will be companies that big in some of these categories at all.

It is still all to play for, and the reason it is worth writing down is that the outcome is not fixed. Nokia met the arrival of the mobile phone by becoming the mobile phone company, and dominated the category for fifteen years. Nokia met the arrival of the iPhone and was gone from the category within seven. Same company, same industry, two outcomes, and Nokia did not choose either of them. The first time it had nothing to protect, so it moved. The second time it had fifteen years of success to protect, and the climatic pattern Simon Wardley names did the rest: **success breeds inertia**. That is the frame for everything below, and it is why the title says what it says. **AI is not the deciding factor, because AI is available to both sides.** The incumbents have the same models the newcomers have, plus more data to point them at, more engineers and more money. If the technology decided this, they would already have won, and two and a half years in they have not. What decides it is inertia: where a company sits on the evolution axis, and how much past success it has to protect. The SaaS apocalypse is a forecast about that. It will happen to the companies with the most to protect, and it belongs to the ones with the least, which is why the interesting question is not whether the incumbents survive but who is already building on the ground they cannot move onto. The best way to see that ground is a Wardley map.

**Same AI. Different inertia.**

The SaaS product slides right along the evolution axis and becomes a substrate: a database, a message bus, a state machine. On top of that substrate, the custom brief is now cheap to make. What is not cheap is making it last, and that is the handover from explorer to villager to town planner. The mistake, drawn in red, is treating the brief as if it were already a product.

## The market already had this argument once this year

In the first week of February 2026, after Anthropic shipped plug-ins for its Claude Cowork agent covering legal, sales, marketing and data analysis, software stocks fell off a cliff. An equity trader at Jefferies, Jeffrey Favuzza, gave it a name: [the SaaSpocalypse](https://saassentinel.com/2026/07/03/saaspocalypse-2026-what-happened-to-saas-and-where-the-market-stands-now/). Roughly $285 billion left the sector in about 48 hours. [Thomson Reuters fell 16% in a day](https://www.theglobeandmail.com/investing/article-global-software-stocks-hit-by-anthropic-wake-up-call-on-ai-disruption/), the S&P 500 software and services index dropped 13% over five sessions and sat 26% below its October peak, and Forrester published a piece titled, without hedging, [SaaS as we know it is dead](https://www.forrester.com/blogs/saas-as-we-know-it-is-dead-how-to-survive-the-saas-pocalypse/).

Then it recovered. By July the software ETF was [down 10.5% for the year against an S&P 500 up 10.8%](https://finance.yahoo.com/markets/stocks/articles/ai-crushed-software-stocks-igv-194541393.html), and by September it had rallied about 40% from its April low. The recovery came with a narrative: systems of record, proprietary data and sticky workflows are durable moats, and the panic was overblown.

I want to point at something in that recovery story, because it is going to matter for the rest of this piece. **The recovery argument is that the database is the moat.** Not the interface, not the workflow screens, not the per-seat licence. The thing investors decided was safe is the thing underneath, and the thing they quietly stopped defending is the thing on top. That is not a rebuttal of the apocalypse. It is the apocalypse, priced.

Notice, too, what both sides of that argument took for granted: that the question was about AI. The panic said AI would hollow out SaaS. The recovery said AI would not. Both were staring at the wrong variable. The same models were available to the largest incumbent and to a two-person company on the day the plug-ins shipped, and they still are. What differed between them was not the technology. It was what each had to protect.

And the sharpest sceptic in February was making a point I agree with. J.P. Morgan's Mark Murphy called it *"an illogical leap to extrapolate Claude Cowork Plugins to an expectation that every company will write and maintain a bespoke product to replace every layer."* He is right. They will not maintain it. Hold that thought, because it is where the opportunity lives.

## First, the part nobody likes to say: users were never happy

Before any of this, before agents, before vibe coding, the experience of using business software was bad, and it was bad in a specific way. The product did 80% of what you needed, and the remaining 20% was as painful as before you bought it. You fought the system. It did not reflect your case, and it could not be made to.

This is not a vibe. It is measured.

**Nine in ten employees are frustrated with their workplace technology.** Freshworks surveyed 8,698 people in 2022, 6,698 employees and 2,000 line-of-business leaders, and found [91% frustrated by inadequate workplace technology](https://www.freshworks.com/press-releases/survey-nine-in-10-employees-are-frustrated-by-their-workplace-technology/). More than half of the unsatisfied said their software made them *less* productive. The single biggest adoption problem leaders named, at 68%, was applications that are hard to use with a high learning curve.

**Most of what was built is never used.** Pendo analysed feature usage across 615 products that had been instrumented for over a year and found that [80% of features in the average software product are rarely or never used](https://www.pendo.io/resources/the-2019-feature-adoption-report/), and estimated that publicly traded cloud software companies had spent up to $29.5 billion building them. The older, more famous number is Standish's 64%, and it deserves its caveat: as [Mike Cohn documents](https://www.mountaingoatsoftware.com/blog/are-64-of-features-really-rarely-or-never-used), it came from a 2002 keynote based on four internal applications, and should never have been generalised. Pendo's figure is the one with a real sample behind it, and it is worse.

**And most of what was bought sits idle.** Zylo's 2025 SaaS Management Index puts the average organisation's waste on unused licences at [$21 million a year, up 14.2% on the year before](https://zylo.com/news/2025-saas-management-index). SaaS spend is $4,830 per employee. A large enterprise runs around 660 applications. Lines of business now control 70% of that spend and IT only 26%, which is how the waste stays invisible.

Put those three together and you get the pricing complaint in the memo, stated exactly. **You pay 100% for the 10% of features you actually wanted**, and then you pay for the seats you are not using either.

**Then there is the spreadsheet.** A [Deloitte survey found 73% of companies used Excel to prepare VAT returns](https://tax.thomsonreuters.co.uk/blog/excel-the-dirty-secret/); YouGov found 78% of British companies say spreadsheets support key financial decisions, and 72% of medium and large businesses use them for budgeting or forecasting. Every one of those companies owns software that was sold to do that job. **The persistence of Excel is not a failure of users to adopt. It is the clearest evidence we have that SaaS failed them**, because Excel is the one tool where they control the shape of the thing and can build exactly what they want.

## Why it got this way, in one line from Wardley

There are economic reasons, commercial reasons and behavioural reasons, and the winner-takes-all dynamics of technology markets amplify all of them. But the mechanism underneath is the one Simon Wardley names as a climatic pattern: **past success breeds inertia.**

His own phrasing, from the [doctrine chapter](https://blog.gardeviance.org/2016/08/doctrine.html): *"The pre-existing installed base causes inertia to the change. Invariably users will be fixated on a legacy world and hence they will have a bias towards it."* And the corollary he draws everywhere: it is almost always new entrants, unencumbered by past success, who initiate the change.

Watch what a company does once it is above a certain size. Decisions start to be about locking the customer in, keeping them inside the platform, extracting the maximum from the account, rather than about empowering them. The easiest way to see it is to look at what they do not build. Most do not make it easy to leave. Most do not make it easy to get your data out, or your schema, or to move. Most do not put a supported, first-class API at the centre of the product; the API is a tick-box, driven by retention rather than by the user's leverage. What is inside stays hidden, because exposing it was seen as a risk to the moat.

I think about all of this through maps, and [wardley-maps.sgit.ai](https://wardley-maps.sgit.ai/) is where that thinking lives. Its thesis is that *maps are claims, not pictures*: a map asserts where each component sits on the evolution axis, which makes it arguable. Here is the claim I am making with the map above. **The SaaS product has slid right.** What was custom-built became a product, and what was a product is now commoditising into a substrate: a database, a message bus, a state machine. And as Wardley wrote, when a component industrialises, it becomes part of *"an ever expanding platform of discrete industrialised components for which the pioneers can build on."* Higher-order things get built on top of the commodity. That is not the threat. That is the whole point.

## Everybody was already vibe coding, just very slowly

The term is Andrej Karpathy's, from February 2025, and by November it was [Collins Dictionary's word of the year](https://www.cnn.com/2025/11/06/tech/vibe-coding-collins-word-year-scli-intl). I still do not love it, but the word has won, so let me say what it actually describes: **people writing very good briefs.**

Because that is what a product owner has always done. The people with the vision, the managers, the users who knew exactly what they wanted, were always describing the software. They were vibe coding. They just did it in an environment with a catastrophically slow loop. Usually you could not customise the product at all. If you could, you were customising on somebody else's terms. If you hired developers, it was expensive, and the loop from *I want this* to *here it is* was weeks or months. The brief was fine. The execution was the bottleneck.

Now the loop is minutes. And so a thing that was always true becomes visible: **very few products let you strip out the 90% you do not want and keep the 10% you do.** But that is exactly what you can now build. Not everything the vendor thought of. The flow the user actually has, with the features they actually use, with no bloat, absolutely focused.

## And the reason the incumbents cannot simply do this themselves

Here is the uncomfortable line, and I stand behind it: **show me a SaaS company and I will show you a company that is highly inefficient at developing software.** Anybody who has worked inside a large software business knows what the flows behind the scenes look like, what the architecture looks like, what the quality of the internals looks like. It is usually a mess, and the bigger the company the slower it gets.

The reason is specific. Very few businesses ever understood or invested in non-functional requirements. I know this personally, because for years I represented one of them, security, and watched it get pushed out of the pipeline again and again. But it is not only security. It is documentation, architecture, scaffolding, deployment, CI, resilience, the ability to deploy anywhere, the ability to refactor, the ability to ship a customised version that does exactly what one user needs. All of it gets deprioritised, and the vocabulary for deprioritising it is the vocabulary every engineering culture is proudest of: *follow the user, do not over-engineer, do not gold-plate.* Those are good instincts that became a codename for never paying the engineering bill.

The bill shows up anyway. Stripe surveyed over a thousand developers and a thousand C-level executives across five countries and found engineers spend [17.3 hours a week, 42% of their working time, on maintenance and bad code](https://stripe.com/files/reports/the-developer-coefficient.pdf), roughly a third of total capacity on technical debt alone, which they costed at $85 billion a year in lost productivity. And the distribution is not improving: in the [2024 DORA report](https://dora.dev/research/2024/dora-report/) only 19% of teams are elite performers, the high-performing cluster shrank from 31% to 22% in a year, and the low cluster grew from 17% to 25%. Elite teams deploy 182 times more often than low ones. Most organisations are not elite, and most large ones are not close.

Which is why the obvious objection does not hold. *If shipping good software were just a matter of investing in the product and spending money, surely these companies would have built amazing software by now.* They have the money. They have the same AI as everybody else, and more data to point it at. They have not built it. We are two and a half years into the generative AI shift and we still do not see the level of innovation from incumbents that you would expect if the technology were the constraint. It is not. The constraint was never the budget, and it is not the models. It was the handover between explorers, villagers and town planners that these companies never built, the split between the people who find things, the people who make them solid and the people who run them at scale.

## The irony, which is the whole article in one paragraph

**The things SaaS companies refused to build, to protect their moats, are precisely the things an agent needs.** Portability. Open schemas. A real API at the centre. Data you can take out. Capabilities you can call from outside. For twenty years those were treated as churn risks, so they were starved. Now the customer's agent turns up wanting exactly that list, and finds a product built to prevent it. The moat has become the thing the water cannot get past in either direction.

## The mistake, and where the money actually is

Now the part where everybody gets it wrong, in both directions.

**The mistake is to confuse the brief with a product.** Somebody vibe codes the tool their team actually wanted, it works, and the conclusion is drawn that the SaaS product it replaced was pointless. But there is a reason you bought SaaS in the first place, and it was never the features. It was that the thing is *maintained.* For all their flaws, those products are robust. They get new versions. Bugs get fixed. There is a level of security, of reliability, of documentation. They are run. Every non-functional requirement that the SaaS company at least partly paid for has now landed on a customised, business-specific application that a non-engineer built in an afternoon.

And that person does not want to maintain it. This is the point Murphy at J.P. Morgan was making, and he is right. Every department will now have people building software the way they build spreadsheets, and the Excel evidence above tells you exactly how that goes: they build it, it works, and then it is a fragile, unversioned, unsecured thing that somebody has to own. They want to build it and hand it over.

So the future is not *no SaaS.* The future is two things merging.

**Village and town-planner companies.** Businesses that take the finished brief, the thing the explorer built, and run it: maintain it, support it, secure it, version it, deploy it everywhere it needs to be, keep it working. Paid by consumption and by the fact that it keeps working, not by the seat. On [wardley-maps.sgit.ai](https://wardley-maps.sgit.ai/patterns/pst/index.html) that handover is written down as the villager's job, *stabilise, harden, deploy to production*, and the interesting property of doing it with agents is that the handover becomes *a file move plus a version bump*, logged, dated and reviewable in a diff. What I have been building with sgit and [Fractal Semantic Graphs](https://sgit.ai/demos/fractal-graphs/index.md) is one shape this can take: the schemas move with the work, each world keeps its own ontology, and the thing that gets maintained and charged for is the running, versioned, connected artefact, not the screen.

**And some incumbents who manage to pivot** their product into a platform for exactly this, leveraging the interconnections they already hold. Some will. But time is running out, because every improvement in the models makes the custom brief more precise, and the pure Wardley reading is that this is all about components. What you should expect is an explosion of small and mid-sized companies supporting this, and an explosion of components that do one thing extremely well and become the building blocks.

Because here is the other half of the correction: it is not the case that vibe-coded software is automatically good. Most of it will not be, and by design cannot be, because the people driving it are not engineers and do not make the decisions engineers make. You still need people who read the code. You still need people whose whole job is to make components that are genuinely solid. It is worth remembering that almost everything vibe coded today runs on frameworks built before generative AI, by exactly those people, reading exactly that code. We have not even seen the first generation of frameworks built the new way yet.

## Strip the UI and see what is left

Something I read recently put it well: take away the interface, allow the customer to generate their own, and most of these companies turn out to be a glorified database, a glorified messaging system and a glorified state machine. And the honest response to that is two things at once. First: yes, and that can be built. Second: it is very hard to build *well*, which is why the value has not vanished, it has moved down a layer and across to whoever runs it.

That is the map. The product slid right. The screen and the seat lost their value. The substrate did not, and the maintenance did not, and the handover did not.

## More engineers, not fewer

One prediction to close on, because it cuts against the mood. We are going to need as many developers as we have now, and probably more, because we are about to generate an enormous amount more code, and somebody has to read it, harden it and run it. The focus will be engineering excellence rather than feature velocity, and the good news is that the raw material has never been better: the quality of the documentation, the handover, the schemas and the graphs that can now be produced is far higher than anything we could produce by hand.

And I think something else changes. The reason large software companies were slow is the reason Fred Brooks wrote down fifty years ago: adding people to a project slows it down, because the communication overhead grows faster than the output. Two-pizza teams were the workaround. **I think we can now build much larger, much more multidisciplinary teams of humans and agents, because the communication can finally be scaled**, the passing of information, the capture of decisions, the handovers between the people who explore and the people who settle and the people who plan. We could never do that before.

The companies that master that are going to be the biggest software houses of the next decade. Some of them exist today. Most of them do not yet.

Which brings it back to Nokia, and to inertia. The version of the apocalypse that ends with a company gone from its category is not a decision anybody takes. It is what happens by default when a company treats the screen as the moat, keeps the data locked, ships the API as a tick-box, and waits for the panic to pass, which the market has helpfully told it the panic has. Every one of those is the natural behaviour of a business with fifteen years of success to protect. The other version requires acting against that inertia: noticing that what it refused to build is exactly what its customers' agents are asking for, and building it before somebody with nothing to protect does. That is the strategy question, and it is not a question about AI, which both sides have. It is a question about inertia, which only one side has. The newcomers have already answered it, because for them there was never anything in the way.

*© 2026 Dinis Cruz. This article's own text is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). You're free to share and adapt it, as long as you give credit. Quoted material and linked sources keep their own licences.*

## Threads

Startups & strategy[This article as a graph →](graphs.md#saas-apocalypse-decided-by-inertia-not-by-ai)

### Continued by

- [The deck I could not download: an author-first home for presentations, as a business plan somebody else can build](the-deck-i-could-not-download.md) One download offered as a subscription, an author paid nothing, and a design for the service the author would have chosen: vaults, keys, seven roles, 85% to the author.
- [If somebody built a company on code review: how I would do it, and why it is only now possible](if-somebody-built-a-company-on-code-review.md) A reader's seven questions answered as a company plan: one reader for every layer, review as a science, and the layers as the customer's own.
- [A supply chain of vaults: how GenAI, open data and small custom tools could bring the price of food down](supply-chain-of-vaults.md) The food chain is a data problem: one encrypted vault per party, joined by append lanes and a typed graph, could cut the waste that keeps prices high.

[All articles](index.md) · [All graphs](graphs.md)

## From the desk

- [Thinking with a Wardley map](collections/wardley-maps.md) collection, 6 articles

**Posting this article on LinkedIn?** The cover is [saas-apocalypse-decided-by-inertia-not-by-ai.jpg](banners/saas-apocalypse-decided-by-inertia-not-by-ai.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/saas-apocalypse-decided-by-inertia-not-by-ai.html)*
