# The bridge, followed to the end: what one local story is worth when it is kept as a graph, sgit.ai

> A simulation of Markus Franz's bridge example, played out on a story vault from the council's first notice to the first car across. A fictional town's main bridge closes; the council says one week, the contract on site says three, an independent engineer says five to seven, and it opens after forty-six days. The paper leads with it five times; readers need it on fifty-seven days. Three readers, a parent, a café owner on the far bank and a plumber who works both banks, use the same claims in three different ways, each from their own graph, and make better decisions with them: an after-school club booked in time, £640 of stock not wasted and £1,200 of relief claimed, nine hours of driving saved. A county highways team, an investor, a national desk and a routing agent buy from the same graph, and the agent spends a seventh of what it would have spent searching, and is right from the first week. Everything they pay, £2,707 in the simulation, walks back down the claims to the reporter, the paper and the resident whose photos were the evidence. The vault is published with its read key.

*Source: <https://newsroom.sgit.ai/articles/the-bridge-followed-to-the-end.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The bridge, followed to the end: what one local story is worth when it is kept as a graph

# The bridge, followed to the end: what one local story is worth when it is kept as a graph

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-07 · [article v1.3.0, 4 versions](versions/the-bridge-followed-to-the-end.md) · [sgit.ai v0.6.96](https://sgit.ai/admin/versions.md) · journalismlocal-newsreader-skillsliquid-utilitystory-vaultfractal-semantic-graphsmicropaymentsagentssimulationarticle

***Abstract:** A simulation of Markus Franz's bridge example, played out on a story vault from the council's first notice to the first car across. A fictional town's main bridge closes; the council says one week, the contract on site says three, an independent engineer says five to seven, and it opens after forty-six days. The paper leads with it five times; readers need it on fifty-seven days. Three readers, a parent, a café owner on the far bank and a plumber who works both banks, use the same claims in three different ways, each from their own graph, and make better decisions with them: an after-school club booked in time, £640 of stock not wasted and £1,200 of relief claimed, nine hours of driving saved. A county highways team, an investor, a national desk and a routing agent buy from the same graph, and the agent spends a seventh of what it would have spent searching, and is right from the first week. Everything they pay, £2,707 in the simulation, walks back down the claims to the reporter, the paper and the resident whose photos were the evidence. The vault is published with its read key.*

The Wendmouth Courier on 2 November, in the simulation: the headline is one projection of the story graph, and the tracker beside it shows every source's reopening date. Everything in the simulation is fictional.

Where I live, a bridge closed. It was a nightmare on the school run, and a nightmare for the businesses on the other side, because suddenly the people who used to walk in could not reach them. Nothing seemed coordinated. You could not tell whether it would be a week or a season. You looked on social media, on the council's website, on a local news page that had last been updated on the day it closed, and nobody you asked was accountable for the answer.

Markus Franz used the same example in [The Article Is Only the Beginning](https://www.linkedin.com/pulse/article-only-beginning-markus-franz-qzyqe/), and I wrote earlier today about [how his Reader Skills sit on top of a story vault](story-vault-meets-reader-skills.md). This article plays his example out in full, as a working simulation, from the first notice to the reopening: the journalism, the paper, three readers, the institutions and agents that also need the answer, and where the money goes. Everything in it is fictional, the town of Wendmouth, the Mill Street Bridge, the Courier and its staff, the readers, the contractor and every figure. The [vault](https://sgit.ai/demos/vaults/bridge-simulation/index.md) is published with its read key, and every number below is computed by its build script from assumptions written down in it.

One story, four ways in

Read them in order, or start with the one you need: the idea, the connection, the simulation explained, and the working vault.

[1 · The originalThe Article Is Only the Beginning ↗Markus Franz's proposal: Liquid Utility, six Reader Skills, and a bridge closure as the example.](https://www.linkedin.com/pulse/article-only-beginning-markus-franz-qzyqe/)[2 · The connectionStory vault underneath, Reader Skills on topWhy his skills and the story vault are two halves of one system, and why local journalism has the most to gain.](story-vault-meets-reader-skills.md)[you are here3 · The simulation, explainedThe bridge, followed to the endOne closure from first notice to reopening: the journalism, three readers, the buyers, the money, and two years on.](the-bridge-followed-to-the-end.md)

4 · The vaultThe Mill Street BridgeThe working simulation: 23 views in four themes, the economics, an API, and every assumption written down. Fictional throughout.[The vault's page](https://sgit.ai/demos/vaults/bridge-simulation/index.md)[Open the vault ↗](https://dev.vault.sgraph.ai/#sgit_public_read_cb3838a0e965dc9d5af9009fef6e867dbdf18a8fc615cb3f5f2bee5424639705%3Avk3jlgzb)

## The journalism is getting the date right

Three answers to the only question that mattered, as the newsroom held them on 15 October: an official estimate, a documented contract and an expert assessment, each with its evidence and a confidence that comes from how independent that evidence is.

On 12 October the council announced that the bridge would close on the 19th for urgent bearing repairs and was "expected to reopen within a week". That is the headline, and most coverage stops there.

The reporter did not. On the 14th she found the contract on the procurement portal: three weeks, £186,000. Two workers on site said the same, "if nothing else turns up"; they are flagged anonymous at the node, so every projection redacts them. On the 15th she called an independent structural engineer, who said five to seven weeks is typical for this repair. Three sources, three dates, and two of them independent of each other and of the council. The paper ran it: *Bridge contract runs three weeks, not one; engineer warns of six.*

That is the work of the journalist, and it is what a reader is paying for: not the prose, but getting the fact right when the official version is wrong. The council moved its date to mid-November on the 21st. On 2 November a second defect was found and the contract was extended by three weeks. The bridge reopened on 4 December, day forty-six, inside the engineer's range and almost six weeks past the council's first date. In the story graph each of those is a claim, and each correction supersedes the last rather than replacing it, so the graph can still say what was believed on any day and why.

Sometimes the text is not even the product. Markus makes the point that much of what a reader needs is deterministic: a date, a stop, a route, a yes or no. The value of the journalism is that the date is right, sourced and current.

## Newsworthy on five days, needed on fifty-seven

Top: what each source said the reopening date would be, day by day. Bottom: the five days the paper led with the story, against the fifty-seven days readers needed its current state.

This is the chart I think matters most. A story is newsworthy at the beginning and at the end: the closure, the scandal in the middle if there is one, the reopening. The paper in the simulation leads with the bridge on five days. But the information is valuable every day it is closed, to everybody who has to plan around it, and in the simulation readers need its current state on fifty-seven days. The thirteen days on which something actually changed are the days the tracker earns its keep: the update, the alert, the correction, sent to the people it affects.

The Courier on the five days the bridge was news, each front page one projection of the story graph with the tracker beside it, and the fifty-seven days in between that readers needed it.

That gap between the news cycle and the need is where the money has been left on the table. An article is written once. A maintained claim, kept current until the bridge opens, is a service.

## Three readers, three graphs, one story

Three readers' graphs meet the story graph at shared anchors: the bridge, the footbridge, the bypass, a bus route and a stop. Green claims are current; grey ones have been superseded and are kept.

Every reader has a graph of their own: where they live, where their children go to school, which bus they take, where their business is and where its customers come from. In the simulation it is held on the reader's device and not sent anywhere. Where it touches the story graph, at a place, a route, a stop, the Reader Skills have something to answer, and the same claims answer three people differently.

**Hannah** lives on the south bank. Her two children are at the primary school on the north bank, and she takes the 08:05 bus. On the 15th, the day the contract story ran, she booked the after-school club for three weeks, before the places filled; on the 16th the tracker told her the bus stop was moving and the diverted bus would take eighteen minutes longer, and that the footbridge would stay open, twelve minutes on foot. She walked. When the second defect was reported she extended the club the same evening. She paid £2.28 over seven weeks. By her own reckoning it was worth about £180 of pay she did not lose and seventeen hours she did not spend on buses.

Hannah's graph meets the story graph: her home, her children's school, her routines and routes on the left, held on her device; the anchors both graphs share; the claims that reach her through them.

**Dev** runs a café on the north bank, where about sixty per cent of his morning trade walks across the bridge. On the 15th he had three dates in front of him and the confidence attached to each, and he planned on six weeks: stock orders cut by forty per cent, one member of staff moved to a coffee cart at the north end of the footbridge, where Hannah and everybody else on foot now passed. On 2 November he applied for the council's disruption relief with the dates and the Courier's claims as evidence, before the scheme was capped. He paid £5.76. He kept about £640 of stock out of the bin and received £1,200 of relief.

**Marco** is a plumber with jobs on both banks. On the 19th he started clustering jobs by bank and crossing once a day, after ten. From the 26th the cycle club's queue data put a number on it: about eight minutes after ten, against a median of twenty-four and a peak of forty-one at eight. He added a time allowance to cross-river quotes until December. His scheduling agent asked the tracker each morning rather than searching the web. He paid 54p, in alerts and skill runs. He saved about nine hours of driving.

What Hannah received, as WhatsApp messages from the tracker: seven messages over seven weeks, each one about her route, each with its source.

The intersection is the point. The footbridge is a route for Hannah and a customer flow for Dev; the bypass is a cost for Marco and a clue for Dev about who still comes. One set of claims, kept once, by one reporter, serves all of them, and the vault shows exactly which claim reached whom, through which anchor.

## With accurate information, and without it

The vault puts each decision beside its counterfactual, the way the closure usually goes. Without the tracker, Hannah plans on one week, takes the diverted bus for the first week, is late three days running, and finds the after-school club full by the second. Dev orders for normal trade three times, once for each date the council gives, and applies for relief late. Marco crosses at peak and absorbs the detour on fixed prices.

The sources in that version of events are familiar. The council's page says "within a week" until the 21st; its new date, when it comes, is on page forty-one of a cabinet report. The local Facebook group says it is opening on Friday, two hundred shares. Regional television covers the closure on day one and the reopening on day forty-six. Nobody in that list is accountable for the answer, and nobody is paid to keep it right.

## The buyers who do not read the paper

Local information has buyers far beyond the local reader. In the simulation a county highways team licenses the evidence vault, because a second defect on one bridge is a question about eight others of the same design, and brings two inspections forward. An analyst at a fund that holds the contractor's parent licenses it commercially, because contract variations like this one, across three councils, are a pattern worth raising on a results call. A national desk writing about ageing bridges pays to cite the local claims and passes a penny per reader back down. Short, medium and long term, local, regional and national: the vault lays out who needs the same graph for which decision.

One question an agent asks every morning: is the bridge open, and when will it be? Searching on its own, it reads six pages, spends about sixteen cents and finds the council's first page; asking the newsroom, it spends about two cents and is right.

And then there are agents. A regional delivery firm's routing agent plans 140 vans a day across the river. Asked whether the bridge is open and when it will reopen, it can search, read and reconcile: five searches, six pages, about forty-five thousand tokens, and the page that ranks first is the council's original "within a week". Or it can ask the newsroom that keeps the claim current, for a penny. In the simulation, over 2,392 questions, searching costs about $377 in tokens and is wrong for the first week; asking costs about $54 including the pennies, and is right from the 15th. As agents start planning school runs, deliveries and site visits for people, the cheapest thing they can buy is an accurate, maintained, accountable source. The token prices are illustrative and the vault says so; the shape of the comparison is the point.

## Where the money goes

Who paid, and where it went: £2,707 from 1,596 readers and businesses, three institutions and an agent; 60% to the Courier, which pays the reporter's base salary out of it, a 20% commission to the reporter, 10% to the evidence contributors, 10% to infrastructure and payments. The prices, volumes and split are assumptions written in the vault's build script.

In the simulation, one closure earns £2,707. Most of it, £2,408, is small amounts from the town: 1,240 people following the bridge for thirty pence a week while it was closed, forty-six businesses on a business tracker, 310 people paying per alert, five thousand skill runs at two pence. The institutions and the agent add £291. The reporter is on the Courier's payroll: sixty per cent goes to the Courier, which pays her base salary out of it, and twenty per cent comes to her as a commission on every use, £541 on top of her salary for one story kept right for seven weeks, and still arriving after the bridge reopens. The base is what any newsroom pays; the commission is what grows with the story, and with the outlet: the larger and more prominent the paper, the larger the commission the same work earns. Ten per cent goes to infrastructure and payments; and ten per cent to the people whose evidence the claims rest on, shared by how many claims each supported. Priya, the resident who photographed the site notice, the footbridge sign and the first traffic, receives £203. The cycle club that logged the bypass queues twice a day receives £68.

Interviewees are not paid. The Courier does not pay for comment, and an anonymous source cannot be paid without being identified. The people paid are the people whose evidence the graph names, which is the mechanism this whole series keeps returning to: *a page that cannot name its source cannot pay it.*

Every figure here is an assumption, and the vault writes them down where anybody can change them and run it again. What does not depend on the assumptions is the shape: a local story kept as a graph is worth something every day it matters, to everybody it touches, in amounts small enough to pay without thinking, and the graph knows whom to pay.

## Version 0.2: what it cost, and what it keeps earning

The first version of the vault showed who was paid. The question it left open is the one any publisher would ask next: what did it cost, and does it make money? So the vault now has a second build script, `tools/economics.py`, and nine new views, and because the vault is versioned like code, its *What's new* page records the change.

The vault, view by view: twenty of its twenty-three views, in the Day theme, the nine added in version 0.2 outlined.

**Costs and profit.** The fixed cost is mostly the reporting, and it comes first: 31 hours of the reporter's time and 4.5 of the editor's, both paid by the Courier, £1,350 with a legal read, set-up and the platform. Thirty-one hours is what the first week's payments justified: enough to dig into the contract and find the engineer, not enough to camp on the bridge, because an hour that does not pay for itself is an hour the next story needs. The variable costs, payments, alerts, compute and hosting, follow use and come to 9.3% of revenue. During the closure every business is in profit and the reporter is well paid: the Courier makes £274 after paying her salary, the infrastructure share covers its costs with £20 to spare, and the reporter, who is paid rather than in profit, earns her base salary of £930 plus a commission of £541, £1,471 in all, about £47 an hour against a base rate of £30. The story breaks even on 5 November, day twenty-five, and the scale chart says why the town mattered: below about 1,000 followers it would not have paid for its reporting, and above that every follower is margin.

Revenue against cost, day by day, crossing on 5 November; and the same story with more or fewer followers, where fixed costs stay put and variable costs follow use.

**Two years on.** The story stopped being news on 4 December. It kept selling. A council post-incident review, loss adjusters handling business-interruption claims, the county's inspections of eight bridges of the same design, a second fund ahead of the contractor's results, a procurement watchdog, a university research group, an insurer and two other towns with the same bridge all buy the record of what was known, when, and from whom. Over two years the bridge earns £4,378 and £1,871 of profit. After the reopening, 96% of its revenue comes from institutions and agents rather than the town: the revenue moves from the local reader to the players who want the data. The reporter's base stops when the work stops and her commission does not, so her effective rate rises from £48 an hour at the reopening to £51, and Priya's three photographs have earned her £328.

Revenue by month over two years, by who paid: the town in October and November, institutions and agents after that, against a cost that is almost all in the first two months.

**The next stories, and the payment as a signal.** The bridge is the first story in the Courier's graph, not the last. The vault plays out eleven more over two years: a school catchment change, the footbridge resurfacing, the county's sister-bridge inspections, a business rates review, a bus timetable, a wharf flood-defence overrun, a contractor's pattern across three councils, a car park, winter floods, a school meals contract and night closures on the bypass. Each starts with the council, the procurement portal, the routes and the contributors already in the graph, which saves 157 of 310 reporting hours. And each is sized by what people paid for in its first week, from readers and from institutions asking ahead: six are investigated, five get a tracker, and the footbridge resurfacing, which few people needed, gets a brief, an hour, and roughly breaks even. That is the argument made concrete: a bridge nobody cares about earns no payments and gets no investigation, and the first payments are what tell the newsroom where to dig. By the second year 41% of revenue comes from stories more than three months old, the twelve together earn £26,523 and £14,731 of profit, and across all of them the reporter earns £65 an hour, base and commission together.

The money is also the bluntest editor in the building, and an honest one. Beside each story the vault records what the editor expected before the first week and what the town paid for. They agree on five of twelve. On four the town cared more, starting with the bridge itself, which the newsroom expected to be a week of roadworks; on three it cared less. A newsroom close to its community knows a lot about what matters to it, and the community, paying for what it needs, still knows more.

Revenue by month across twelve stories: stories in their first three months in blue, the long tail of older stories in orange, which grows with every story added.

**Trust, earned.** Every story with a date in it adds a row to a record: the official estimate, the Courier's range and the outcome. Across eight of them the outcome lands inside the Courier's range seven times, and once a day outside it; the official estimates are out by 34 days on average. The record also keeps what each source got right, including the engineer who was interviewed for nothing and whose range held, and the anonymous workers whose record attaches to the claim, not to a name. A trust index built from the record scales the take-up of the stories that follow, so credibility shows up in the accounts.

**The council and the accountants.** Dev's £1,200 of relief looks different from the council's side. A council wants to refund correctly. With the tracker it sized the budget from the graph on 16 October rather than topping it up on 25 November, paid 44 of the 52 eligible businesses instead of 18 and none it was not meant for, and spent half the staff time, for £152 of targeting bought from the Courier. On the business's side, an accountant agent reads the same claims, keeps the takings and the van log on the business's side, and pays pence per question: for Dev's café the closure costs £1,530 net with the tracker, against £5,540 without it.

The relief scheme without and with the tracker: when the budget was set, who heard about it, who was paid, and what it cost the council to process.

**Ask the graph, and the API.** Two views show what the vault is to a machine. *Ask the graph* simulates a model query: pick a question and a date, and the answer is composed from the claims live that day, with citations and the context a model would be given, 583 tokens against 45,000 for searching six pages, about a tenth of the cost and right. No model is called, which is the point: the hard part is the graph. *The API* is a Swagger-style explorer for an OpenAPI description in the vault, seventeen endpoints, each a GET whose response is a file already in the vault, with a price per call where there is one. The thirty data files are listed as assets in their own right, with downloads. Readers' graphs have no endpoint: they live on readers' devices.

A simulated model query: when will it reopen, asked on 16 October, answered from the three live claims with citations, and the context the model would be given.The story as an API: every endpoint a GET, every response a file in the vault.

## Version 0.3: a professional finish, and the reporter in profit

The vault is also a demonstration of what a vault can be, so version 0.3 is a design and quality pass. The navigation is five numbered groups, the story, the people, the economics, the data and the vault itself, with an icon for each view, the three readers as people rather than indented lines, counts read from the data, and Previous and Next so the views read as a sequence. It has four themes, the same Night, Day, Paper and Ember as secrets.sgit.ai, with every colour a token valued in one file, so a theme is one block there and charts restyle in place.

Four themes, one set of tokens: the same view in Night, Day, Paper and Ember.

Underneath, an architect agent reviewed the code against the estate's guidance, the vault-app rules on sgit.ai, coding.sgit.ai and nfrs.sgit.ai, and a developer agent applied it. Every view now renders through a template that escapes by default, so data in the vault cannot become markup; a view that cannot load its data says so instead of going blank; the interactive views keep keyboard focus; every chart has a text summary; and a gate of 44 checks, from the bundle contract and byte-for-byte downloads to theme completeness and contrast, fails the build if any of it regresses. The reviews and the decisions are in the vault, as `BRIEF-CORRECTIONS.md` and `REALITY.md`.

The model was corrected in the same version, as described above: the reporter is on the Courier's payroll with a commission from every use, the reporting was sized by the first week's payments, and every business ends the closure in profit. (In version 0.3.1 her row was corrected to show pay, base salary plus commission, rather than a profit: her salary is the Courier's cost, not hers.) And beside each story, the vault now records what the editor expected against what the town paid for.

What the editor expected, and what the town paid for: five of twelve agreed; the town cared more about the bridge than the newsroom did.

## What the simulation is for

It is not a forecast. It is a way to see the argument whole, with the parts that are usually invisible drawn in: the reporter's work behind the date, the readers' own graphs and where they meet the story, the decisions made better, the buyers beyond the town, the agents, and the money walking back. Markus asked what journalism could help someone do. In one bridge closure, the answer is: plan a school run, keep a café open, price a job, inspect eight bridges, route a hundred and forty vans, and know, every day until it reopens, that the answer is right and who is answerable for it.

*Revised on 8 October 2026 for the vault's versions 0.2 and 0.3, from a second voice note asking for the costs, the profitability over time, the next stories, the trust, the council, an accountant agent, simulated model queries and an API.*

*Drafted from a voice note by Dinis Cruz, who is the author of the argument and the person with editorial responsibility, by agent@riskmandate.ai (Claude Opus 5.5, claude-opus-5-5) in the sgit.ai site session, on 7 October 2026. The simulation, its town, people, organisations, dates and figures are fictional, and every number above is computed by the vault's build script from assumptions written in it. Markus Franz's bridge example and his terms, Liquid Utility and Reader Skills, are credited to his article. The opening anecdote is the author's own experience, not part of the simulation.*

## Threads

News & evidenceGraphs & knowledge[This article as a graph →](graphs.md#the-bridge-followed-to-the-end)

### Builds on

- [Story vault underneath, Reader Skills on top: why local journalism has the most to gain](story-vault-meets-reader-skills.md) Markus Franz's Reader Skills on top, the story vault underneath: each skill is a graph query, and local stories can pay back down their chain of sources.

### Continued by

- [The agent is the reader: why agents will pay for graphs, personas and signed claims, because it is cheaper than not paying](the-agent-is-the-reader.md) Agents pay to read the raw web and guess its meaning. A curated graph answers for 90% fewer tokens, so paying the publisher is cheaper than not paying.
- [A meter in the browser: a penny a page, a history you keep, and a site that picks for you](a-meter-in-the-browser.md) Every page now costs a few pence from £5 of credit kept in your browser, and the reading history it keeps is what personalises the site.
- [The waiting room knew first: a live local story, and the gap where local information used to be](the-waiting-room-knew-first.md) Staff at two London hospitals said the IT was down; nothing a local could check showed it. A live local story about where local information comes from now.
- [Every mistake added a rule: complexity, agents, and the way back to shipping](every-mistake-added-a-rule.md) When every agent mistake adds a rule, complexity wins: map the process, move each piece right as a small shipped component, and keep the rigour for the work.
- [Liquid content needs water: liquefy the journalist's notebook, not the finished product](liquid-content-needs-water.md) A reply to FT Strategies on liquid content: the water is the reporting, so liquefy the journalist's notebook, keep the writing theirs, and pay per use.
- [Story vault underneath, Reader Skills on top: why local journalism has the most to gain](story-vault-meets-reader-skills.md) Markus Franz's Reader Skills on top, the story vault underneath: each skill is a graph query, and local stories can pay back down their chain of sources.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 41 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=41)

## From the desk

- [Local news, kept as evidence](collections/local-news-kept-as-evidence.md) collection, 6 articles

**Posting this article on LinkedIn?** The cover is [the-bridge-followed-to-the-end.jpg](banners/the-bridge-followed-to-the-end.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-bridge-followed-to-the-end.html)*
