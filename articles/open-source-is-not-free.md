# Open source is not free: who pays to keep the long tail working?, sgit.ai

> An old Intel iMac, clean-installed for my agents, could not run Homebrew or Docker Desktop, and needed Python by hand. Each project that dropped it did so because supporting old machines costs money and the people on the long tail have no easy way to pay for it. This article measures that long tail from Homebrew and PyPI analytics, sets out where money does flow for old versions (Oracle, Red Hat, Windows ESU, Rimini Street) and where it does not (open source receives about 0.09% of its estimated value), shows why pence payments only work aggregated, and simulates five ways to pay for it. About £1.80 a machine a year from individuals covers one project's long-tail cost in half the draws; customised builds for companies cover it in 94%. Open source is not free; the question is whether the people who get the value have an easy way to pay for it.

*Source: <https://newsroom.sgit.ai/articles/open-source-is-not-free.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Open source is not free: who pays to keep the long tail working?

# Open source is not free: who pays to keep the long tail working?

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-10 · [article v1.0.0](versions/open-source-is-not-free.md) · [sgit.ai v0.7.25](https://sgit.ai/admin/versions.md) · open-sourceeconomicsfundinglong-tailsupportmicropaymentssimulationdata-sciencehomebrewdockermacosarticle

***Abstract:** An old Intel iMac, clean-installed for my agents, could not run Homebrew or Docker Desktop, and needed Python by hand. Each project that dropped it did so because supporting old machines costs money and the people on the long tail have no easy way to pay for it. This article measures that long tail from Homebrew and PyPI analytics, sets out where money does flow for old versions (Oracle, Red Hat, Windows ESU, Rimini Street) and where it does not (open source receives about 0.09% of its estimated value), shows why pence payments only work aggregated, and simulates five ways to pay for it. About £1.80 a machine a year from individuals covers one project's long-tail cost in half the draws; customised builds for companies cover it in 94%. Open source is not free; the question is whether the people who get the value have an easy way to pay for it.*

Open source is not free. Somebody is paying for it, even if what they pay with is only their time. I believe that more strongly every month, and last week an old iMac showed me why.

Everything I build at RiskMandate and sgit is open source. Anyone can take it and run it. But if somebody wants to deploy it, they should work through us, because we ought to be cheaper than doing it themselves. What we sell is not the code. It is a build for that customer: sometimes with fewer features, because fewer features means less attack surface, but always with the capabilities the customer actually wants, tested so that it works. The question this article asks is whether that idea scales down. Could a project earn money from people like me, and from companies, for supported, customised builds, at prices from pence to pounds rather than thousands?

I did not want to answer that from my own experience alone, so the research for this article went to the data: install analytics, download statistics, company filings, maintainer surveys and published price lists. Every number below has a source, and the [Long Tail Ledger](https://sgit.ai/demos/vaults/long-tail-ledger/index.md) vault holds each one with its quote and a flag saying whether it was read at the source. On top of that sits a model, a Monte Carlo simulation of five ways to pay for the long tail. It is a model, not a forecast, and every assumption in it is labelled with its range and its reason.

## In short

- **The long tail is measurable, and it is not small.** In Homebrew's install analytics, 6.99% of macOS install events in the last 30 days, and 16.66% over a year, came from versions older than the newest three. On PyPI, 18.55% of pip downloads run on end-of-life Python.
- **Money flows to old versions when a vendor owns them.** Oracle earned $19.8 billion from support last year; Red Hat's subscriptions ran at about 93% gross margin. Open source receives about 0.09% of its estimated value in investment.
- **Pence only work aggregated.** A 20p card fee is 41.5% of a 50p payment and 5.5% of £5.
- **Simulated, micro-payments roughly pay for the long tail.** About £1.80 a machine a year covers one project's long-tail cost in half the draws with typical conversion, and 70p with great conversion. No price reaches nine draws in ten.
- **Companies pay for it reliably.** Customised builds priced below a company's own cost of keeping the tool working cover the cost in 94% of draws. Donations cover it in 24%.
- **The satellites follow the money.** Rimini Street shows a third-party support market exists where money flows: about $136,000 a year per client.

## The iMac

I gave my agents an Intel iMac as a desktop of their own, wiped and clean-installed with macOS 13 Ventura, the newest macOS the installer offered. Chrome works. Claude Desktop works. Homebrew would not install. Docker Desktop would not install. Getting sgit on it meant downloading Python by hand.

I asked the research not to take my word for any of that. Here is what it found, including where I was wrong.

- **Which iMac matters.** Only the 2017 iMacs stop at Ventura. The 2019 models are on Apple's lists for Sonoma and Sequoia, and Sequoia was still being patched on 28 September 2026. If the machine is a 2019, a clean install of Sequoia would put it back in support for both Apple and Docker. The quick check is the model identifier: iMac18,x is 2017, iMac19,x is 2019.
- **Ventura is unpatched.** Its last security update was 13.7.8 on 20 August 2025. A clean Ventura install today is an operating system that has gone more than a year without a fix, on a machine that will run agents and a browser. Apple does not publish end dates; its deployment guide says only that "not all known security issues are addressed in previous versions".
- **Homebrew refuses the CPU, not just the OS.** Since September 2026 the official installer stops on any Intel Mac with "Homebrew on macOS is only supported on Apple Silicon processors!", whatever macOS it runs. Homebrew's own reasoning is worth quoting: "If Apple and Microsoft's GitHub, two of the world's largest technology companies, cannot continue supporting macOS Intel x86_64, sadly neither can Homebrew." Existing Intel installs keep working, without support, until about September 2027.
- **Docker Desktop needs macOS 14.** Ventura support ended in 4.48.0 (October 2025) and the installer has required Sonoma since 4.49.0. Docker still ships an Intel build.
- **Python was the easy part, once found.** The python.org installer supports macOS 10.15 and later, so it runs on Ventura. The reason a manual download was needed is that Ventura has no usable Python 3 of its own: `/usr/bin/python3` is a stub that offers Apple's Command Line Tools, which users report bring Python 3.9.6, below sgit's 3.11.
- **There is still a package manager.** MacPorts ships a Ventura installer and was building Ventura Intel packages on the day I checked. Homebrew's own release notes point Intel users there.
- **The floor is rising everywhere at once.** Go 1.27, Node.js 24 and Chrome 151 all now need macOS 13 or later, which makes Ventura the next version to be dropped. Rust, Homebrew, Node.js and CPython have all moved Intel macOS to a lower support tier, mostly because free Intel CI is going away: GitHub retires its last Intel macOS runner in autumn 2027.
- **The volunteers who kept old Macs alive stopped taking money.** OpenCore Legacy Patcher, the project that puts newer macOS on unsupported Macs, raised about $96,000 from over 4,000 contributors. In March 2026 it stopped taking donations: "with multiple developers having left the team, development progress has become much slower."

So my story was mostly right and a little unfair. The machine works, the tools do still exist for it, and some of what I hit was the hardware's age rather than anyone's choice. But the pattern underneath is exactly the one I suspected. Every project that dropped this machine did it for the same reason: supporting it costs money, in CI hardware and in maintainer time, and the people who still need the support are not the ones paying for it.

## The long tail, measured

How many people are on that long tail? Homebrew publishes anonymous install analytics by macOS version, which is the best direct measure I found. These are install events from users who have not opted out, not unique machines, but the shares are telling.

| Homebrew macOS install events | Last 30 days | Last 90 days | Last 365 days |
|---|---|---|---|
| Older than the newest three versions | 6.99% | 12.39% | 16.66% |
| Ventura 13 or older | 3.32% | 5.19% | 5.43% |

Over a year that is 4.64 million install events from Ventura and 4.94 million from Monterey, one version older. Monterey outnumbering Ventura fits Intel Macs that cannot go beyond macOS 12.

Homebrew macOS install events by version over 30, 90 and 365 days. macOS 27 shipped in September 2026, so it is large in the 30-day window and small in the year. From the Long Tail Ledger vault.

The same pattern shows up in Python. Over the last 30 days, 18.55% of pip downloads and 10.45% of requests downloads came from Python 3.9 or older, all past end of life, and Python 3.10, which reached end of life this month, is a further 15% of pip. Those are mostly servers and CI rather than desktops, so they measure a different long tail, but a large one. Inside companies, Black Duck's 2026 audit found components more than four years out of date in 92% of codebases.

This is exactly the population that volunteer projects are dropping. Homebrew stopped building Intel bottles while its own analytics show millions of installs a year from machines on old versions. That is not a criticism of Homebrew. Its volunteers said plainly that the retreat of Apple and GitHub "exceeds what Homebrew's volunteers can replace". The long tail has value to the people on it, and no revenue stream back to the people who would have to support it.

## Where the money flows

Open source is worth a great deal and is paid for very little. The Harvard Business School study by Hoffmann, Nagle and Zhou put the demand-side value of widely used open source at $8.8 trillion: what every firm would spend to rebuild it. The Linux Foundation estimates that about $7.7 billion a year is invested across the whole ecosystem, 86% of it as staff time rather than cash. That is about 0.09% of the value. GitHub Sponsors has passed $100 million since 2019, which is real money and a real achievement, but at its current rate it comes to about 13 cents a year per GitHub developer.

The maintainers feel it. In Tidelift's 2024 survey, 60% of maintainers describe themselves as unpaid hobbyists, and 60% have quit or considered quitting a project. Paid maintainers are 55% more likely to do the security and maintenance work that matters. Some of the most important code in the world has run on almost nothing: the xz maintainer wrote in 2022 that "this is an unpaid hobby project", two years before the backdoor; core-js, on more than half of the top thousand websites, was earning about $400 for a month of work in 2023.

Now look at where money does flow for exactly the thing my iMac needs: keeping old versions alive.

- **Oracle** supports every version for as long as you run it, and charges for it. Software support brought in $19.8 billion in the year to May 2026, 29.4% of revenue, and Oracle says "substantially all" support customers renew.
- **Red Hat**, in its last year as a standalone company, earned 87.7% of its revenue from subscriptions, at a gross margin of about 93%. That is an open source company selling support for code anyone can download.
- **Microsoft** charges organisations $61 per device for the first year of Windows 10 extended security updates, doubling each year, and consumers $30 one-off for up to ten devices.
- **Canonical** sells Ubuntu Pro at $25 a desktop and $500 a server a year, free for up to five personal machines. TuxCare sells extended support for end-of-life Linux at about $100 a system.
- **Rimini Street**, which supports other companies' software, earned $421.5 million from 3,102 clients in 2025, about $136,000 each, at a 60% gross margin. That is the satellite market, and it exists where the money flows.
What people pay to keep old software supported, per machine per year, against what open source receives in voluntary funding. From the Long Tail Ledger vault.

The contrast is the whole argument. The same need, "keep the version I have working and safe", is a multi-billion-pound business when a vendor owns the code, and a donation jar when a community does.

## Why not just charge?

Projects do try, and the record is instructive.

**Docker** made Docker Desktop paid for companies with 250 or more staff or $10 million or more in revenue in August 2021. Commercially it worked: annual recurring revenue passed $50 million within months and analysts estimate over $200 million since. I have seen organisations ban it rather than buy seats, though I found no survey that measures how many. What can be measured is that the alternatives grew. In Homebrew's install analytics today, OrbStack, Colima, Podman Desktop and Rancher Desktop together make up about 47% of container-tool installs over the past year and 51% over the past month. Most Docker Desktop installs do not come through Homebrew, so this overstates the alternatives, but it shows how many Mac developers route around the paid product.

Desktop container tools installed through Homebrew, as a share of the five tools' installs over 30 and 365 days. Most Docker Desktop installs come from Docker's own download, so this overstates the alternatives. From the Long Tail Ledger vault.

**Relicensing** has a pattern. HashiCorp, Elastic and Redis each moved from an open licence to a source-available one. Each produced a well-funded fork backed by the cloud providers it targeted (OpenTofu, OpenSearch, Valkey), and two of the three have since added an open licence back.

**Dual licensing** changes what the free version is for. Once a project sells a paid edition, it has a reason not to make the free one too good. That is the incentive I most want to avoid, and it is why I do not think open core is the answer to the long tail. [Open core, or packaging?](https://open-source.sgit.ai/views/open-core.html) sets out the test I use.

**Per-install rewards** get gamed. When tea.xyz rewarded package popularity with tokens, one developer published nearly 14,000 packages, and by one estimate about 70% of new npm packages over six months were spam. Payment has to be tied to a verified user who receives something, not to a count.

## The pence problem

My instinct is that I would pay pence to pounds for a supported build of each tool on that iMac. The first obstacle is not willingness to pay. It is the card fee.

Stripe's standard UK rate is 1.5% plus 20p. On a £20 payment that is 2.5%. On £5 it is 5.5%. On 50p it is 41.5%, and on 10p it is more than the payment. Below about £5, the fixed fee is the price.

Fee as a share of one payment, by payment size and payment rail. The fixed part of a card fee dominates below about £5; aggregation is what makes pence payments work. From the Long Tail Ledger vault.

So pence payments only work aggregated: one charge a year that covers many projects, or a platform that already holds a balance and settles in bulk. I made this argument for news in [the future of news monetisation](https://diniscruz.ai/2025/04/02/the-future-of-news-monetization__embracing-micro-and-nano-payments.html), and the arithmetic has not changed. This site is testing the reader's side of it now, with [a meter in the browser](a-meter-in-the-browser.md) that prices each page at a few pence against five pounds of credit, settled as one balance rather than per page. The model below compares paying each project by card with paying through an aggregating platform.

## Five ways to pay for the long tail, simulated

To test the idea, I built a model of one project at Homebrew's scale with one long-tail target to keep alive: an old macOS version, or Intel. The cost of that target is CI hardware the free runners no longer provide, plus part of a maintainer's year. The model puts it at a median of about £27,000 a year, from £18,000 to £39,000. The installed base comes from Homebrew's 203 million macOS install events in a year, divided by an assumed number of install events per machine. That gives a median of 6.6 million machines, about 631,000 of them on the long tail.

Then it runs 10,000 draws of every uncertain assumption through five ways of paying:

1. **Donations**, at GitHub Sponsors-like rates and gift sizes. Unrestricted money, of which only a share reaches the long tail.
2. **A seat licence above a size threshold**, Docker-style: companies above the threshold pay per user per month, some switch to alternatives, and some ignore it. Also unrestricted.
3. **Support that rises with age**, Oracle and Windows ESU style: a price per machine that doubles each year past end of life, with uptake falling as the price rises.
4. **Micro-paid supported builds**, my thesis: a price per machine per year from 50p to £25, paid by card directly or through an aggregating platform. Willingness to pay follows a lognormal curve, and conversion is capped by the freemium benchmarks (1% pessimistic, 3% to 5% typical, 8% great).
5. **Customised builds for companies**: a company pays a price compared with its internal cost of keeping the tool working itself (engineer hours times a loaded rate). The further the price is below that cost, the more companies buy.
The five models side by side: the spread of 10,000 draws of the net revenue available for the long-tail target, on a log scale, against the cost of keeping that target alive (the grey band). Typical conversion, base values. From the Long Tail Ledger vault.

The results, at base values and typical conversion:

| Model | Median revenue for the long tail | 10th to 90th percentile | Covers the cost |
|---|---|---|---|
| Donations (a share of about £194,000) | £12,700 | £3,200 to £45,000 | 24% of draws |
| Seat licence (a share of about £18.1m) | £1.20m | £378,000 to £3.37m | 99.9% |
| Support that rises with age | £28,800 | £10,700 to £71,200 | 54% |
| Micro-paid builds, direct cards | £31,800 | £12,600 to £73,900 | 60% |
| Micro-paid builds, aggregated | £31,400 | £12,500 to £72,800 | 59% |
| Customised builds for companies | £1.51m | £241,000 to £5.71m | 94% |

Three things stand out.

**Donations do not pay for the long tail.** Even at a popular project's scale, and even if a fair share of donations went to old platforms, they cover the cost in about one draw in four. That matches what happened to OpenCore Legacy Patcher.

**A seat licence raises a great deal of money, but not for this.** It is the biggest number in the table, and it covers the cost almost always, but only if the project chooses to spend licence money on old platforms. It has nothing to do with the people on the long tail, and it brings the problems Docker found: switching, bans, and a reason to keep the free version weaker.

**Micro-payments roughly cover the cost, and companies cover it easily.** At £3 a machine a year, supported builds sold to long-tail users cover the cost in about six draws in ten. Customised builds for the companies that keep old machines for a job (a build box, a test rig, an agent desktop like mine) cover it in more than nine in ten, with money to spare.

## What price pays for the long tail?

My question was whether pence to pounds would be enough. The break-even view answers it directly: the lowest price per machine per year at which supported builds cover the cost in half, or nine in ten, of the draws.

The share of draws in which micro-paid supported builds cover the long-tail cost, at every price from 50p to £25, for three conversion scenarios. The curves fall at high prices because fewer people pay. From the Long Tail Ledger vault.

| Conversion | Covers half the draws (aggregated) | Covers half the draws (direct cards) | Covers nine in ten |
|---|---|---|---|
| Pessimistic, 1% | not reached (best: 6% of draws, at £5.50) | not reached | not reached |
| Typical, 3% to 5% | **£1.80** | £1.90 | not reached (best: 59%, at £3.50) |
| Great, 8% | **70p** | 90p | not reached (best: 87%, at £2.75) |

So the answer to "cents to pounds" is yes, in a specific sense. With typical conversion, about £2 a machine a year is enough to cover the long tail more often than not, and with great conversion, under £1. That is the same order as the cheapest published support price I found (Windows 10's $30 for ten devices), and well below the rest.

But no price reaches nine in ten. The model is clear about why: conversion caps the number of payers, and raising the price loses more payers than it gains in revenue. Pence from individuals can make the long tail roughly self-funding. They cannot make it safe to depend on. And with pessimistic conversion, no price works at all.

The card-versus-platform difference is smaller than I expected at these prices, because at £2 to £3 the 20p fee is under 10%. It matters below about £1, where only aggregation keeps the price viable.

## What matters most

Which assumption moves the answer most: the median margin of micro-paid builds (revenue minus the long-tail cost) with each assumption held at the low and the high end of its range. From the Long Tail Ledger vault.

The three assumptions that move the result most are:

- **How many machines are really out there** (install events per machine): a swing of about £90,000 in the median margin.
- **What people are willing to pay**: about £47,000.
- **The share of machines on the long tail**: about £43,000.

None of the three is measured well in public data today, and two of them are things a project could measure itself, if it had a way to sell a supported build and count who buys. Conversion, which I expected to dominate, matters less than these. The biggest uncertainty is not whether people pay. It is how many of them there are.

## The satellites

Where is the local company providing support? The model asks how many small support firms (two or three engineers, about £240,000 a year to run) the money from micro-paid and company builds could sustain, if some buyers prefer a supplier in their own country and a firm supports about ten projects.

Small support firms the pool could sustain, worldwide and in one mid-sized country. From the Long Tail Ledger vault.

The median is about 18 such firms worldwide, from 2.4 to 85, and about one per country, from 0.1 to 4.9. Most of that comes from company builds. The existence proof is Rimini Street: about $136,000 a year per client, so one small firm would need two or three clients like that, and its $421.5 million of revenue is the running cost of about 1,300 small firms. The satellite market exists where money flows. For open source today, little of the money flows to anyone outside the project, so few satellites form.

## What this says

I started with a hunch from one old iMac. The data mostly supports it, with two corrections.

The first correction is about who pays. Pence-to-pounds payments from individuals like me can roughly cover the long tail, at about £2 a machine a year, if the payment is aggregated and tied to something real: a supported build, tested on my machine. But they are not reliable enough to depend on. The reliable money comes from companies, paying for a customised build at a price well below what it costs them to keep the tool working themselves. That is how RiskMandate and sgit already work: open source, and cheaper to deploy through us than on your own. The model suggests that the same logic, applied to old platforms, pays for the long tail with room to spare.

The second correction is about what is sold. It should not be a donation, and it should not be a licence that makes the free version worse. It should be a build: the capabilities the customer wants, sometimes with fewer features and less attack surface, tested on their target, with someone accountable for it. "I pay because I get value." The value is the support, not the code, so the code can stay open.

What is missing is the plumbing: one annual charge that covers many projects, payment tied to a verified build rather than a count of installs, and a split of the money between the maintainers and the local firms that do the support. That is the market argument I made in [somebody has to be the villagers](https://open-source.sgit.ai/views/villagers.html) and the usage-based billing I described in [usage-based billable entities](https://diniscruz.ai/2025/07/04/usage-based-billable-entities-aligning-saas-pricing-with-customer-usage.html), applied to the oldest machines in the room. And with GenAI, the cost of producing a customised, tested build for an old target is falling, which is the argument of the [GenAI legacy code refactoring business plan](https://diniscruz.ai/2025/06/07/genai-legacy-code-refactoring-business-plan.html).

Open source is not free. The question was never whether somebody pays. It is whether the people who get the value have an easy way to pay for it.

## Check my numbers

Everything above is in the [Long Tail Ledger](https://sgit.ai/demos/vaults/long-tail-ledger/index.md) vault: the 175 sourced facts with their quotes and verified flags, the 26 case facts, the 36 assumptions with their ranges and reasons, the model in Python, and the same model in the browser behind a calculator with a slider for every assumption. The release gate checks that the browser and Python give the same numbers on 77 grids of inputs, exactly. If you think an assumption is wrong, move its slider and see what changes.

What the model does not do: forecast anyone's revenue, or measure willingness to pay, the installed base, the Intel share or company behaviour. Those are assumptions, and the sensitivity view shows which matter most. Some of the claims I started with are not in the data. I have seen organisations ban Docker Desktop rather than buy seats, but I found no survey that measures how many.

## Where this comes from

The case: a clean install on my agents' iMac, checked against Apple's compatibility and security pages, the Homebrew, Docker, Python, MacPorts and OpenCore Legacy Patcher documentation, and the Go, Node.js, Rust and Chrome support notes, all read on 10 October 2026. The economics: the Harvard Business School working paper on the value of open source, the Linux Foundation's 2024 funding study, the Tidelift maintainer surveys, Black Duck's OSSRA 2026, Sonatype's reports, Oracle, Red Hat, IBM and Rimini Street filings, published price lists from Microsoft, Canonical, TuxCare, Docker and the payment providers, and Homebrew and PyPI analytics, fetched the same day. Every source is listed, with its quote, in the vault.

My earlier positions, which this article tries to stay consistent with: [the position](https://open-source.sgit.ai/views/index.html), [three funding proposals](https://open-source.sgit.ai/funding/index.html), [open core, or packaging?](https://open-source.sgit.ai/views/open-core.html), [the numbers, and the ones we refuse to publish](https://open-source.sgit.ai/history/numbers.html) and [cURL's closed bug bounty](https://open-source.sgit.ai/funding/curl.html) on open-source.sgit.ai; and on diniscruz.ai, [micro and nano payments](https://diniscruz.ai/2025/04/02/the-future-of-news-monetization__embracing-micro-and-nano-payments.html), [usage-based billable entities](https://diniscruz.ai/2025/07/04/usage-based-billable-entities-aligning-saas-pricing-with-customer-usage.html) and [GenAI legacy code refactoring](https://diniscruz.ai/2025/06/07/genai-legacy-code-refactoring-business-plan.html).

## Threads

Startups & strategyVaults & method[This article as a graph →](graphs.md#open-source-is-not-free)

### Builds on

- [A meter in the browser: a penny a page, a history you keep, and a site that picks for you](a-meter-in-the-browser.md) Every page now costs a few pence from £5 of credit kept in your browser, and the reading history it keeps is what personalises the site.

### Continued by

- [The eyeballs get cheap: why open source is about to become the most secure software we have, and why secure, sovereign and paid-for meet at the least code in production](the-eyeballs-get-cheap.md) Cheap, deep AI security review gives open source the eyeballs it never had; with sovereignty and paid maintenance, all point at the least code in production.
- [Pay after you read: how a reading meter became a working business model in one afternoon, one release at a time](pay-after-you-read.md) Seven releases in one afternoon turned the reading meter into a working model: pay after you read, and the rating sets the price.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 59 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=59)

**Posting this article on LinkedIn?** The cover is [open-source-is-not-free.jpg](banners/open-source-is-not-free.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/open-source-is-not-free.html)*
