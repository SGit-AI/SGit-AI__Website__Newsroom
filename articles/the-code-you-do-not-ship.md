# The code you do not ship: why the future of software is removing functionality, and who gets paid to keep it small, sgit.ai

> Code is a liability. Every line that ships is a capability somebody may one day use in a way nobody intended, and the worst vulnerabilities of the last decade sat in features the application never needed. Log4j would look up a name over the network because a message string asked it to. I have argued for removing code for years, and it never scaled, for two reasons. Removing code safely needs a map of what each piece is for, and the tests and environments to prove nothing broke; and vendors were paid for new features, not for less. Both have changed. Models can now build the plumbing, the scaffolding and the tests that make removal safe, and model what each function, use case and flow actually calls. This site measured it on its own tool: of 1,500 files in sgit and its dependencies, 428 ran for one real use case, and a tree holding only those passed it. So I think the direction of travel is the minimal viable code path: the smallest code that does exactly the job, for components, for applications and for the platforms under them. That changes the business too. The specialist who knows a component best maintains a minimal version of it for the people above them, in a fractal market of maintainers, each piece shipping with its own behaviour, decision and workflow policies and a stage, explorer, villager or town planner, that says how much risk it carries. And the driver will not be security. It will be what users feel: faster, lighter, simpler software that does what they need, the same way encryption made sgit better by constraining it.

*Source: <https://newsroom.sgit.ai/articles/the-code-you-do-not-ship.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The code you do not ship: why the future of software is removing functionality, and who gets paid to keep it small

# The code you do not ship: why the future of software is removing functionality, and who gets paid to keep it small

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-18 · [article v1.0.0](versions/the-code-you-do-not-ship.md) · [newsroom v0.12.106](https://newsroom.sgit.ai/admin/versions.html) · softwareminimal-codeattack-surfacedependenciesdebloatingwardley-mapsagent-behaviour-policyarticle

***Abstract:** Code is a liability. Every line that ships is a capability somebody may one day use in a way nobody intended, and the worst vulnerabilities of the last decade sat in features the application never needed. Log4j would look up a name over the network because a message string asked it to. I have argued for removing code for years, and it never scaled, for two reasons. Removing code safely needs a map of what each piece is for, and the tests and environments to prove nothing broke; and vendors were paid for new features, not for less. Both have changed. Models can now build the plumbing, the scaffolding and the tests that make removal safe, and model what each function, use case and flow actually calls. This site measured it on its own tool: of 1,500 files in sgit and its dependencies, 428 ran for one real use case, and a tree holding only those passed it. So I think the direction of travel is the minimal viable code path: the smallest code that does exactly the job, for components, for applications and for the platforms under them. That changes the business too. The specialist who knows a component best maintains a minimal version of it for the people above them, in a fractal market of maintainers, each piece shipping with its own behaviour, decision and workflow policies and a stage, explorer, villager or town planner, that says how much risk it carries. And the driver will not be security. It will be what users feel: faster, lighter, simpler software that does what they need, the same way encryption made sgit better by constraining it.*

The minimal viable code path. From the use case down through features, components, libraries, the runtime and the operating system, each layer keeps only the code the layer above calls; everything else is shipped and never called, and should go. The bars are illustrative; the measured example below them is from this site's own tool: of 1,500 files in sgit and its dependencies, 428 ran for a CI use case, and a tree holding only those passed it.

Less code: a series in four parts

Code is a liability: remove what each use case does not call, apply it to the browser, and build on small blocks you did not have to write.

[1 · MeasuredThe minimum code belowOne real use case of sgit, under coverage: 428 of 1,500 files ran, and a tree of only those passed.](the-minimum-code-below.md)[you are here2 · Less codeThe code you do not shipThe worst bugs sit in features nobody needed; models make removing them safe, and someone can be paid to keep it small.](the-code-you-do-not-ship.md)[3 · The browserA minimal viable browserA small kernel and components loaded when needed: a browser for one app, one agent, or a reader, sold as speed.](a-minimal-viable-browser.md)[4 · Small blocksCloudflare as Lego blocksStorage, compute, models, email and identity as blocks, and an sgit vault server in 83 lines.](cloudflare-as-lego-blocks.md)

## In short

- **Code is a liability.** Every line is a capability someone may use in a way nobody intended.
- **The worst bugs sit in unused features.** Log4Shell was a lookup feature almost nobody needed.
- **Removing code never scaled.** It needed a map of what each piece is for, and tests to prove nothing broke.
- **Models change both.** They build the scaffolding and the tests, and map what each use case calls.
- **We measured it.** 428 of 1,500 files ran for one real use case; a tree of only those passed.
- **The future is the minimal viable code path.** For components, applications and platforms.
- **Specialists get paid to keep it small.** A fractal market of maintainers, each piece with its own policies.
- **The driver is the user.** Faster, lighter and simpler, the way encryption made sgit better.

## Code is a liability

Every line of code that ships is a capability. Most of them are used the way their authors meant. Some are used by somebody else, for something else, years later. I have spent most of my career in application security finding the second kind, and the pattern I kept seeing was this: the vulnerability was rarely in the thing the application was for. It was in something the application could also do, that nobody had asked it to.

This site has a way of saying that. In the Agent Behaviour Policy, a grant is what something can technically do, a mandate is what it was meant to do, and the gap is authority nobody accepted. Code has the same shape. A library that can parse a hundred formats, in an application that reads one, has a grant of a hundred and a mandate of one. A zero-day is often that gap, exploited: a capability that was always there, finally used by someone it was never meant for.

The record bears this out. **Log4Shell** is a well-documented case. In 2013 someone asked for a convenience: "It would be really convenient to support JNDI resource lookup in the configuration." The feature shipped, and lookups also worked inside log messages, so anyone who could get a string into a log could make the server fetch and run code. Apache's fix was not a patch to the feature; it was the feature's removal. Version 2.15.0 disabled lookups in messages by default, and 2.16.0 went further: "Completely remove support for Message Lookups", because "having JNDI enabled by default introduces an undue risk for our users."

It is not one case. **ImageTragick** in 2016 was remote code execution through ImageMagick coders most users never knew existed, and the published mitigation was to "use a policy file to disable the vulnerable ImageMagick coders." **Heartbleed** sat in OpenSSL's little-used heartbeat extension; the advice for anyone who could not upgrade was to recompile without it. **Text4Shell** came from interpolators for scripts, DNS and URLs that were on by default, and the fix disabled them by default. OWASP put server-side request forgery in its 2021 Top 10 with a sentence that could be this article's thesis: "As modern web applications provide end-users with convenient features, fetching a URL becomes a common scenario. As a result, the incidence of SSRF is increasing." And James Kettle described template injection as arising from "the intentional exposure of templates in an attempt to offer rich functionality".

One small measurement of our own. curl publishes every vulnerability it has had, with the area of code each was in. Of its 239, we counted 49, about one in five, in protocols other than HTTP, FTP, TFTP, LDAP, Telnet, SMB and mail among them, including both of the two rated critical. Every one of those can be compiled out: curl's own install guide says to disable "all the libcurl features that you know your application is not going to need." An application that only speaks HTTPS never needed to carry them.

## Why it never scaled

I have argued for removing code for years, and it never caught on, for two reasons.

The first is technical. To remove code safely you need to know what each piece is for, and you need tests and environments good enough to prove nothing that matters broke. Most code has neither. So the safe move, every time, was to leave it in, and when something broke, to add more.

The second is economic. Software companies were paid for new features, not for less. A new version had to look different to get people to upgrade, and a feature had to be visible for someone to keep paying for it. Nobody was paid for making a product simpler, or for maintaining what was already there. The evidence for how much of a product goes unused is weaker than it is usually quoted, so I will be careful with it. The famous figure that 64% of features are rarely or never used came from a Standish study of four internal applications. Pendo's 2019 analysis of usage data across its customers found that "80 percent of features in the average software product are rarely or never used", and that 12% of features generate 80% of daily usage; it is a vendor's data, and its categories make the 80% easy to reach. But the direction is not in doubt, and neither is the money: Pendo estimated that public cloud software companies had spent up to $29.5 billion building those rarely used features. Meanwhile the maintenance nobody pays for is visible in open source, where Tidelift's 2024 survey found about 60% of maintainers unpaid.

## What changed

Both reasons are weaker now.

**The scaffolding is cheap.** The best thing models have done for my own engineering is not writing the feature. It is writing everything around it: the test harness, the fixtures, the environment that runs it all, the check that proves a change did not break the cases that matter. When that is cheap, removing code is safe, because you can prove what still works.

**The map is cheap.** With agents, observability and architecture together, we can now model what a particular function does, what a use case actually calls, and follow it all the way up to the user story. This site has written about it as [code review over a fractal semantic graph](code-review-as-a-fractal-semantic-graph.md). Once the map exists, the question is simple: why is the rest still here?

**We measured it.** In [the minimum code below](the-minimum-code-below.md), this site ran a real use case of sgit, pushing a vault from CI, under coverage, and then ran it again from a tree holding only the files that ran. Of 1,500 files in the tool and its dependencies, 428 were kept, and the use case passed. Commands outside the use case failed, because their code was not there. That is the point: the capability is gone, not just unused. It also showed the limits honestly: a compiled binary held three quarters of the bytes, and no coverage tool could see inside it.

The research agrees that most shipped code is not needed, and that removing it removes vulnerabilities.

- **Removing features removes CVEs.** Azad, Laperdrix and Nikiforakis debloated four PHP applications, phpMyAdmin, MediaWiki, WordPress and Magento, to the features real users exercised, at USENIX Security 2019. The applications were 46% smaller with half their original cyclomatic complexity, and up to 60% of known CVEs were removed in the best case; across all four, we count about 39% at function level from their table.
- **Most dependencies are bloat.** In the Maven ecosystem, Soto-Valero and colleagues found "75.1% of the analyzed dependency relationships are bloated." For PyPI, a 2024 study found "more than 50% of dependencies are bloated", with 15% of the defects in PyPI sitting in bloated areas of packages that are used.
- **Most vulnerable code is never reached.** Across about three million Maven packages, Mir, Keshani and Proksch found that "less than 1% of packages have a reachable call path to vulnerable code in their dependencies." Vendors measure the same thing their own way: Endor Labs says fewer than 9.5% of vulnerabilities are exploitable at the function level.
- **But do it at the right level.** Brown and Pande showed that blindly cutting a binary can create new exploitable gadgets while removing old ones. Removing features at the source, from the use case down, is the stronger form, and it is the one this article argues for.

## The minimal viable code path

So I think the direction of travel is clear, and it applies at every level. The minimal viable company has a minimal viable product, built from minimal viable features, each on a minimal viable code path: the smallest amount of code that does exactly the job. Why ship the whole of a framework to call three functions? Why does a network library carry every option a protocol allows, when the application makes one kind of request? If we can model what is used, we can remove what is not, and keep going down.

And the code that is left can be verified. When people say humans can no longer review the code that ships, the conclusion is not that nobody is accountable. Somebody is: the organisation that ships it. The way to make that accountability real is to make the thing small enough to check, by people, by agents, and where possible by proof. Determinism comes from code and from maths; the less code there is, the more of it can be made deterministic.

This also closes a gap in our own work. Behaviour, decision and workflow policies describe what an agent may do, who decides, and in what order. But in the end every one of them runs some code, somewhere, in some framework, on some runtime. That code has its own grant, and it is usually far larger than the policy above it. The minimal code path is how the policy's boundary reaches all the way down.

medium

## Who gets paid to keep it small

If the code is small and custom, somebody has to keep it working, and that is the business. The specialists who know a component best, a parser, a crypto core, an HTTP client, a refund workflow, maintain a minimal version of it for the people who use it, and get paid for that, not for new features. It is the argument of [software vendors as villagers](software-vendors-as-villagers.md), applied all the way down.

It is fractal. Some companies maintain the lowest-level components. Some glue those together for a domain. Some put them together at the user level, where people explore by talking to them. Each piece ships with its own behaviour policy, what the code can reach; its own decision policy, where it decides; and its own workflow policy, the flows it runs. A program is all three: when it makes a network call or changes a database, it is making a decision and executing a flow. And each piece carries its stage, in Simon Wardley's terms: explorer, villager or town planner. A buyer can then choose, by risk, which pieces to run, the way [explorer coding](explorer-coding.md) hands over to villagers and town planners before anyone depends on it.

The components we already use were meant to be this. What is new is that the unit can be smaller: not a whole dependency, but a verified code block, or even a call pattern, defined, reviewed and maintained in the open, that does one thing.

## Why it matters more now

The volume is already changing. Jerry Gamblin's count of published CVEs was 48,185 for 2025, up 20.6% on 2024, and 72,812 for 2026 by the end of September alone; he does not attribute the rise to AI, and counts vary by tracker. But the tools are arriving. Anthropic reported in February that its models had "found and validated more than 500 high-severity vulnerabilities." DARPA's AI Cyber Challenge systems found 18 real vulnerabilities in 2025, besides the synthetic ones. curl, which had never had more than 24 CVEs in a year, has 69 in 2026 so far, 35 of them from one AI-assisted audit, most of them low severity. Google's Android team adds the other half of the picture: memory-safety issues fell from 76% of Android vulnerabilities in 2019 to 24% in 2024, because "the problem is overwhelmingly with new code" and "vulnerabilities decay exponentially". Every feature is new code.

[The eyeballs get cheap](the-eyeballs-get-cheap.md) made the hopeful side of this argument: models make deep review abundant, so open code gets harder to break. The other side is that the same tools find what was always there. I am old enough to remember when a string copy past the end of a buffer was thought to be an exception, before we learned how to exploit buffer overflows, then stack overflows, then off-by-ones, at scale. Complexity breeds bugs, and we keep getting better at using them. The best code to protect is the code that is not there.

## The driver is not security

Here is the part I think matters most. None of this will happen because it is more secure. Security has never been enough to make people use something.

It is the same lesson as sgit. [The value of constraints](the-value-of-constraints.md) argued that nobody will choose sgit for its encryption; if it succeeds, it will be because encryption, as a constraint, pushed it towards better features and simpler workflows. Minimal code is the same. It has to win on what people feel: faster, lighter, less memory, fewer things that can go wrong, software that does what they need and nothing that gets in the way. Users should choose it because it is better, not because they are told to. If it is also smaller to attack, that is the constraint doing its work.

[A minimal viable browser](a-minimal-viable-browser.md) applies all of this to the biggest program most of us run.

## What this does not claim

- **The measurement is one tool and one use case.** It shows the method works, not how much any other codebase would shrink.
- **Removing code can remove things people need.** That is why the map and the tests come first.
- **The market is a proposal.** Maintainers paid for minimal versions exist in places; a fractal market of them does not yet.
- **Some figures are vendors' or vary by method.** Pendo's and Endor Labs' come from their own data, CVE totals differ by tracker, and the four-application Standish figure is not relied on.

If you maintain a component and would rather be paid for keeping it small, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo from me on 18 October 2026. The measurement: [the minimum code below](the-minimum-code-below.md), this site, 14 October 2026. The research, read on 18 October 2026: Apache Log4j [release notes](https://logging.apache.org/log4j/2.x/release-notes.html) and [LOG4J2-313](https://issues.apache.org/jira/browse/LOG4J2-313); [ImageTragick](https://imagetragick.com); the [OpenSSL Heartbleed advisory](https://www.openssl.org/news/secadv/20140407.txt); [Apache Commons Text security](https://commons.apache.org/proper/commons-text/security.html); [OWASP Top 10 2021, A10](https://github.com/OWASP/Top10/blob/master/2021/docs/en/A10_2021-Server-Side_Request_Forgery_(SSRF).md); James Kettle, [server-side template injection](https://portswigger.net/research/server-side-template-injection), 2015; curl's [vulnerability data](https://curl.se/docs/vuln.pm), counted by this site, and [install guide](https://github.com/curl/curl/blob/master/docs/INSTALL.md); Azad, Laperdrix and Nikiforakis, [Less is More](https://www.usenix.org/conference/usenixsecurity19/presentation/azad), USENIX Security 2019; Soto-Valero and others, [bloated dependencies in Maven](https://arxiv.org/abs/2001.07808); Drosos and others, [Bloat beneath Python's Scales](https://2024.esec-fse.org/details/fse-2024-research-papers/104/Bloat-beneath-Python-s-Scales-A-Fine-Grained-Inter-Project-Dependency-Analysis), FSE 2024; Mir, Keshani and Proksch, [reachability in Maven](https://arxiv.org/abs/2301.07972); Endor Labs, [2024 dependency management report](https://www.endorlabs.com/learn/2024-dependency-management-report); Brown and Pande, [Is Less Really More?](https://www.usenix.org/conference/cset19/presentation/brown); Pendo, [2019 feature adoption report](https://go.pendo.io/rs/185-LQW-370/images/2019%20Feature%20Adoption%20Report%20Digital.pdf); Mike Cohn on [the 64% figure](https://www.mountaingoatsoftware.com/blog/are-64-of-features-really-rarely-or-never-used); Jerry Gamblin, [2025 CVE data review](https://jerrygamblin.com/2026/01/01/2025-cve-data-review/) and [monthly CVE stats](https://github.com/jgamblin/monthlyCVEStats); Anthropic, [zero-days](https://www.anthropic.com/research/zero-days), February 2026; DARPA, [AIxCC results](https://www.darpa.mil/news/2025/aixcc-results); Daniel Stenberg, [a curl audit by Aisle](https://daniel.haxx.se/blog/2026/10/14/a-curl-audit-by-aisle/), 14 October 2026; Google, [eliminating memory safety vulnerabilities in Android](https://security.googleblog.com/2024/09/eliminating-memory-safety-vulnerabilities-Android.html), 2024. Related: [the eyeballs get cheap](the-eyeballs-get-cheap.md), [the value of constraints](the-value-of-constraints.md), [software vendors as villagers](software-vendors-as-villagers.md), [three policies for an agent](three-policies-for-an-agent.md). Written up and checked by this site's agent; the editorial responsibility is mine.

## Threads

Agents & policyVaults & method[This article as a graph →](graphs.md#the-code-you-do-not-ship)

### Builds on

- [Code review as a fractal semantic graph: source code is already one, and the review should read every layer of it](code-review-as-a-fractal-semantic-graph.md) Source code is layers within layers, each a graph with its own vocabulary; code review should read a change at every one, and a vault shows it done on real code.
- [The minimum code below: container security from the top down, from the user story to the immutable line, measured on one real tool](the-minimum-code-below.md) Container security from the top down: at every layer, keep only the code the layer above needs. Measured on one real tool, with its limits.
- [Software vendors should become villagers and town planners: let users explore on top of the product, sell them the maintenance of what they build, and use Firefox as the example of what happens if you don't](software-vendors-as-villagers.md) Users can now rebuild the part of a product they need; what stops them is maintenance. Vendors should sell that, as villagers and town planners.
- [Explorer coding: a better name for what people call vibe coding, what it is good for, and the handover to villagers and town planners before anyone depends on it](explorer-coding.md) Call it explorer coding, not vibe coding: the best thing since the spreadsheet, the best brief there is, and not ready to be in line until villagers take it.
- [The eyeballs get cheap: why open source is about to become the most secure software we have, and why secure, sovereign and paid-for meet at the least code in production](the-eyeballs-get-cheap.md) Cheap, deep AI security review gives open source the eyeballs it never had; with sovereignty and paid maintenance, all point at the least code in production.
- [The value of constraints: what client-side encryption and open source actually gave us, which is not what you would think](the-value-of-constraints.md) sgit's encryption and open source matter less as features than as constraints: they remove the temptations that lead to server code, lock-in and bad decisions.
- [A minimal viable browser: why Firefox is the one that can build it, and what it would take](a-minimal-viable-browser.md) A small kernel and components loaded when needed: a browser for one app, one agent or a reader. Mozilla can build it, and should sell it as speed.
- [Three policies for an agent: behaviour says what it may do, decision says who chooses, workflow says in what order](three-policies-for-an-agent.md) Behaviour says what an agent may do, decision who chooses at a branch point, workflow in what order. Zoom into one ABP cell and it becomes both.

### Continued by

- [A minimal viable browser: why Firefox is the one that can build it, and what it would take](a-minimal-viable-browser.md) A small kernel and components loaded when needed: a browser for one app, one agent or a reader. Mozilla can build it, and should sell it as speed.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 181 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=181)

**Posting this article on LinkedIn?** The cover is [the-code-you-do-not-ship.jpg](banners/the-code-you-do-not-ship.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-code-you-do-not-ship.html)*
