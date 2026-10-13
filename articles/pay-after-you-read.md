# Pay after you read: how a reading meter became a working business model in one afternoon, one release at a time, sgit.ai

> On 10 October the reading meter on sgit.ai went, in seven releases between 12:09 and 15:49, from an experiment to a working pay-on-demand publication. A reader pays pence for the share of a page they actually read, from a balance that can go below zero without ever blocking them; after reading, they say how useful it was, and that sets the price, from free to double; their reading builds personas and a newsroom of their own, kept in their browser; and they can send it to us, encrypted, for a front page designed for them. Once a Stripe link is set, the only question left is whether people pay. This article introduces each feature, shows how each one grew out of the last, with a Wardley map that adds them one at a time, explains why paying after you see the value is the right way round, and why every decision started from one rule: do not rip off the reader. It ends with an offer to sites with traffic that would like to test it.

*Source: <https://newsroom.sgit.ai/articles/pay-after-you-read.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Pay after you read: how a reading meter became a working business model in one afternoon, one release at a time

# Pay after you read: how a reading meter became a working business model in one afternoon, one release at a time

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-10 · updated 2026-10-11 · [article v1.3.0, 4 versions](versions/pay-after-you-read.md) · [sgit.ai v0.7.36](https://sgit.ai/admin/versions.md) · newsroomreading-metermicropaymentspricingpersonalisationpersonaswardley-mapsinnovationagentsarticle

***Abstract:** On 10 October the reading meter on sgit.ai went, in seven releases between 12:09 and 15:49, from an experiment to a working pay-on-demand publication. A reader pays pence for the share of a page they actually read, from a balance that can go below zero without ever blocking them; after reading, they say how useful it was, and that sets the price, from free to double; their reading builds personas and a newsroom of their own, kept in their browser; and they can send it to us, encrypted, for a front page designed for them. Once a Stripe link is set, the only question left is whether people pay. This article introduces each feature, shows how each one grew out of the last, with a Wardley map that adds them one at a time, explains why paying after you see the value is the right way round, and why every decision started from one rule: do not rip off the reader. It ends with an offer to sites with traffic that would like to test it.*

On 10 October, between 12:09 and 15:49, what I had been doing with the reading meter on this site stopped being a theoretical exercise. It went from an interesting piece of research to something commercial. As soon as a Stripe link is wired in, sgit.ai is a fully working pay-on-demand publication: every page has a price, readers pay for what they read and what they valued, and the money arrives in one place. The only question left is whether people will pay for it. That is literally the only thing.

This article does two things. It introduces what was built, because a lot was added in one afternoon and none of it has been described in one place. And it uses the afternoon as a case study, probably the cleanest one we have, of the way I think innovation should happen when you work with agents: the more you have, the faster you go.

The reading meter at the end of 10 October, as a Wardley map: everything added that afternoon sits on the left, built on components that already existed on the right. The animated version, one release at a time, is in How it grew.

## In short

- **Seven releases in 3 hours 40 minutes**, alongside seven other pieces of work, with no slowdown: a meter, then paying by depth with no block below zero, then personas, versions, sharing your reading, and finally a rating that sets the price.
- **You pay after you see the value.** You read; the meter charges for the share you read; then you say how useful it was, and that sets the price, from free to double.
- **Your reading is yours.** It lives in your browser, builds personas and a newsroom for each of them, and reaches us only if you send it, encrypted.
- **The end state was not planned.** Each feature came from using the one before. Designed up front, it would have been a bigger, slower and probably over-engineered project.
- **It is the ILC zigzag at work.** Every layer underneath, from sgit in March to the newsrooms in September, matured until it was invisible, and so the next could be built on it.
- **It was fast because of what was already there**: the build and its gates, versioned components, git as the history, vaults, append lanes and sealed envelopes, and sessions that release on their own.
- **Every decision started with the reader.** Not "money left on the table", but value for money: the reader should always feel the price was fair.
- **What is missing is traffic.** If you run a site with readers and little revenue from them, let's test it together.

## What a reader gets now

Start with a reader arriving at an article.

**A price for every page, and you pay for what you read.** A new article costs 10p and an older one 5p, read to the end. The meter charges the share you actually scroll through, rounded to 5% and never less than a tenth, once per page per session, topping up as you read further. Bounce off a page and it costs almost nothing.

**A balance that can go below zero, for ever.** Everyone starts with £5.00 of credit. When it runs out, nothing happens: no wall, no bar, no nag, only a small balance in the top bar that turns a warmer colour below zero. Paying is something you do because you want to, not because a page has stopped you.

**A card at the foot of every article.** It shows what the page has cost so far, how much of it you read, and the price to the end. It adds the article to your reading list. And it asks three questions, each on a five-step scale that starts in the middle:

- **How useful was this?** This sets the price: 1 is free, 2 is half, 3 is the price, 4 is one and a half times, 5 is double.
- **More like this?** This moves the page's topics and tags in your persona, so your picks change.
- **Level of detail.** This is kept as your preference, and shown in your newsroom.
The reader card at the foot of an article: what it cost, how much was read, the reading list, and the three ratings. Usefulness sets the price; the other two shape the newsroom.

**Personas, and a newsroom for each.** Your default persona is built from everything you read, weighted by how much of each page you read, and named from your top topics until you name it yourself (mine, in the test browser, became "The Fact Finder, with a streak of the Strategist"). You can start from five presets (a founder, a journalist, a security lead, an AI builder, a board member) or add as many of your own as you like, one for each kind of reading you do. Each has a newsroom: a front page of what it would want next, what you kept in it and what you put out of it, and a graph of the topics and pages it has grown.

Your newsroom: a front page for one persona at a time, built in your browser from what you read.

**A reading account that stays with you.** The balance, the history, what you spent and your graph, with a top-up, a pause, an export as JSON and a fresh start. All of it is in your browser's storage and nowhere else.

The reading account: the balance, what was spent, and the controls. Kept in this browser, and only here.

**Send us your reading, and get a front page designed for you.** This is the one way your reading reaches us. The page shows, word for word, everything that would be sent. You can copy it into an email, or send it encrypted in your browser to our list agent's published key, over a write-only lane, with a consent tick. In return, I reply with what your front page could look like, built from your actual reading.

Send us your reading: exactly what would be sent, word for word, then copy it or send it encrypted with your consent.

**Articles that show their changes.** Every article now has versions, read from git, with a page for each showing what changed, paragraph by paragraph. If you pay for writing that keeps improving, you can see what improved.

**One payment, when you choose.** Topping up is one £5 Stripe Payment Link, with no account and nothing that renews. On a standard UK card Stripe's fee is about 27.5p of the £5, so one top-up spreads one card fee over dozens of pages: the aggregation that makes pence payments viable, which the [open source economics article](open-source-is-not-free.md#pence) argued for earlier the same day.

## Pay after you see the value

A model I have always liked is Leanpub's. An author sets a minimum price and a suggested price, and the reader chooses what to pay with a slider, from the minimum upwards; Leanpub says readers "will choose to pay you more than your Minimum Price, and even more than your Suggested Price" ([Leanpub](https://leanpub.com/blog/lean-publishing-tip-of-the-day-leanpubs-variable-pricing-model/)), and it offers a full refund within 60 days ([refunds](https://leanpub.com/refunds)). The one thing that always felt odd to me is that you choose the price before you have seen the value. The reader card turns that round: you read first, and then say what it was worth.

That is a known idea, and the evidence on it is mixed in useful ways.

- **Paying what you want works better than people expect, but not for everyone.** In a field experiment with 113,047 people buying souvenir photos, 0.5% bought at a fixed $12.95, while 8.39% bought when they could pay what they wanted, at an average of $0.92 ([Gneezy and others, Science, 2010](https://pubmed.ncbi.nlm.nih.gov/20647467/)). Across three field studies, prices paid were "significantly greater than zero", and paying what you want "can even lead to an increase in seller revenues" ([Kim, Natter and Spann, 2009](https://doi.org/10.1509/jmkg.73.1.044)). In a restaurant run that way for two years, average payments declined slightly and settled "at a positive level" ([Riener and Traxler, 2012](https://ideas.repec.org/a/eee/soceco/v41y2012i4p476-483.html)). The caution is that some people buy less, because they "feel bad when they pay less than the 'appropriate' price" ([Gneezy and others, PNAS, 2012](https://pmc.ncbi.nlm.nih.gov/articles/PMC3358869)). That is why the card starts at the middle, at the price, so a reader who does nothing pays what the page costs and does not have to name a number.
- **Refunds for articles have been tried, and they measure quality.** Blendle, the Dutch pay-per-article service, charged tens of cents an article and gave "an instant refund on any article they have purchased within 24 hours" ([journalism.co.uk, 2014](https://www.journalism.co.uk/how-the-itunes-of-journalism-reached-100k-users-in-4-months/)). Refunds ran at about 3% of articles at first, about 10% on average by 2016, and "as high as 50 percent" for gossip and lists ([TechCrunch, 2016](https://techcrunch.com/2016/03/23/blendle-us-launch/)). That is the clickbait point in numbers: readers asked for their money back when a page did not deliver.
- **Pay-per-article on its own did not last.** Blendle stopped selling single articles in the Netherlands in 2019 to focus on a monthly subscription, saying "We are still not making a profit" ([DutchNews](https://www.dutchnews.nl/2019/06/dutch-news-aggregate-website-blendle-ditches-pay-per-article-service/)), and closed its German and US pay-per-article service in September 2023 because their user bases were "very limited" ([journalism.co.uk, 2023](https://www.journalism.co.uk/blendle-shuts-down-micropayment-model-due-to-very-limited-user-base/)). The difference here is not the price per page. It is what the page buys: a persona and a newsroom that get better the more you read, and a balance that never stops you.
- **Elsewhere, refunds come with limits.** Steam refunds a game for any reason within 14 days if it was played for under two hours ([Steam](https://store.steampowered.com/steam_refunds/)), and Amazon restricted Kindle returns in 2023 to books less than 10% read ([Authors Guild](https://authorsguild.org/news/amazon-changing-ebook-return-policy/)). Charging for the share actually read solves the same problem from the other end: a page you abandon early costs little, so there is little to refund.

The context is why this is worth trying. Across 20 countries, 17% of people paid for online news in 2026, and in the UK it is about one in ten ([Reuters Institute Digital News Report 2026](https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2026/dnr-executive-summary); [2025](https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2025/dnr-executive-summary)). The subscription has a ceiling. Paying for what you read, after you read it, is one way past it.

## Every decision started with the reader

Every decision this afternoon was a choice between charging more now and making the reader glad they paid.

Looking back at the afternoon, every decision was easy to make, because each one started from the same rule: do not rip off the reader. Make sure they are paying for value, and make sure they are happy with what they paid.

That is not how a lot of pricing is done. A common instinct, in management and in sales, is not to leave money on the table: we could charge a bit more, and by not doing so we are letting the customer get away with something. I think that is a bad instinct. You never want to charge a customer the maximum they can pay, because by definition they end up feeling it was expensive, and a customer who feels that is not happy.

Think about what "expensive" means. I do not find something expensive when its value for money is high, even if it costs a lot. Something becomes expensive when its value drops below its price. I might still pay for it and I can still afford it, but I now find it expensive, which means I use it less, and I do not recommend it: if something is good but expensive, I am not going to push it on friends and make them carry the cost. The sweet spot is value for money, because that is where people use a thing more and more, which is exactly what a publication wants.

So, when the first version had a "Don't charge me" button, it worked, but it felt draconian: a refund you had to ask for, with a reason. The rating that replaced it as the main path says the same thing the other way round: if you saw the value, pay; if you saw more value, pay more; if you did not, do not. "Don't charge me" is still there, as the exception.

What about the readers who read and never pay? Those are not readers a publication is losing money on. And a reader who did not value a page is the last one who should pay for it: charging them makes them more jaded, not more loyal. This is also a measure of the journalism. Click on a headline that promised something the article did not deliver, and you feel it: you came for something and did not find it. If you also paid for it, you feel it twice. A rating after reading puts that feeling on the record, page by page, and gives the publication a reason to stop writing pages that cause it.

## How it grew: one release at a time

The afternoon from git: seven steps of the reading meter in 3 hours 40 minutes, and seven other pieces of work released in the same four hours.

None of the features at the end of the afternoon were where I started. The sequence, from the commits:

1. **The experiment, two weeks earlier.** The first version of browser-based consumption was on [pt.newsroom.sgit.ai](https://pt.newsroom.sgit.ai/carteira/index.html), the Portuguese newsroom: a wallet in which "cada página deste site custa um cêntimo a abrir" (every page costs a cent to open), with the record of what you spent on a page of its own, and the balance kept in the reader's browser.
2. **12:09, a meter in the browser** (v0.7.24). That wallet brought to sgit.ai: a price for every page, £5 of credit, a history, and picks from it. A simulated top-up with every step except the payment.
3. **13:40, the meter goes live** (v0.7.26). Using it made the next steps obvious: pay for how far you read, decline a page with a reason, a real £5 Stripe link, and the meter rebuilt as a component, SG Meter, other sites can install. And the step that made it commercial: **below zero, with no cut-off.** From that moment the offer is simply that readers can pay if they want.
4. **14:23, personas and a newsroom of your own** (v0.7.28). Once the history existed, it could become a persona, and a persona could have a front page.
5. **14:29, articles have versions** (v0.7.29), read from git.
6. **15:28, send us your reading** (v0.7.31). The personalised newsroom raised the obvious question of what readers would actually want, and the way to find out was to ask them to send it, on their terms.
7. **15:49, the reader card** (v0.7.34). The last feature, and probably the best: the ratings, with usefulness setting the price.

There is a direct line between something working, trying it out, and improving it, and improving it again. Each step was me trying the previous one and saying: now add this. Ironically, if I had designed the end state we arrived at, I think we would have over-engineered it. It would have been the typical big project, with too much attempted at once, months of work, and untested features shaping other untested features. Instead, each feature was shaped by the one before it being in use. The "Don't charge me" button is the best example: it had to exist, and feel wrong, for the rating to be the obvious answer.

The Wardley map makes the same point. Every new component sits at the genesis end, on the left, and every one of them is built on components further right that were already there and already boring: browser storage, git, Stripe, the build, vaults, append lanes, the sealed envelope. The afternoon was cheap because the right-hand side of the map was already built.

The afternoon as a Wardley map, one release at a time: what already existed, then each feature as it was added and what it was built on, ending with what comes next. Times are UTC, from the commits.

The 8 frames, one image each: [1](images/pv-wardley-1.webp) [2](images/pv-wardley-2.webp) [3](images/pv-wardley-3.webp) [4](images/pv-wardley-4.webp) [5](images/pv-wardley-5.webp) [6](images/pv-wardley-6.webp) [7](images/pv-wardley-7.webp) [8](images/pv-wardley-8.webp).

## The zigzag: innovate, leverage, commoditise

The same story at a larger scale, built up one layer at a time: each layer matured until it was invisible, and that is what made the next one possible.

The map of the afternoon shows one day. The same pattern runs through the whole project, and Simon Wardley has a name for it: ILC, innovate, leverage, commoditise. You "take an existing product that is relatively well defined and commonplace and turn it into an industrialised utility", then "encourage and enable other companies to innovate by building on top of your utility", and "you then repeat this virtuous circle" ([Wardley, 2016](https://blog.gardeviance.org/2016/08/the-play-and-decision-to-act.html)). His map of it has a platform growing on the right as each component is industrialised, with new things being built on the left.

Drawn for this project, it is a zigzag. Here, a thing is commoditised when it becomes invisible: when the layer above can use it without thinking about it.

1. **sgit**, encrypted vaults from a command line. The first release was on 4 March 2026, as sg-send-cli 0.3.0, and after 88 releases it is sgit-ai 0.20.0. Once it just worked, vaults could hold more than files.
2. **Vaults that open as apps**: HTML in a vault, a read key in the browser. The first on this site was published on 16 August; there are 53 now. Once that was routine, a vault could be an experiment of its own.
3. **Claude sessions with a repository and a vault**, which is the layer we did not build. Agents with no other access, using a vault as their memory and their shared drive. When that became ordinary, building a website became a conversation.
4. **Websites built and released by agents**: sgit.ai from v0.1.1 on 11 August to v0.7.39 today, with gates on every release. Once a release was routine, a site could be a product of its own.
5. **Newsrooms**: sgit.newsroom and pt.newsroom, where the one-cent wallet appeared by 27 September. Once the newsroom worked, it could carry an experiment in paying.
6. **SG Meter**, the reading meter, from v1.0 at 12:09 to v1.3 at 15:49 on 10 October.
7. **At the top, the reader**: read on demand, pay for use and for value. From the reader's side it already just works: open a page, read it, choose what it was worth. Every layer under it is invisible to them, which is the point.

The speed of the afternoon is the zigzag at work. Every time I tried something and it was solid, it became something to stand on: this is working, now do this, now do that. Each step was small because the steps under it had stopped needing attention.

The whole zigzag. Solid arrows are a thing maturing, until it is invisible; dashed arrows are what its maturity made possible, one layer up.

## Why it could go this fast

I have written several times that small shipped components compound ([every mistake added a rule](every-mistake-added-a-rule.md)): the more we have, the faster we go. This afternoon is the cleanest case study we have, and the reasons are specific.

- **A build with gates.** Every release runs the same build and the same validator, so a feature lands without anyone checking the site by hand, and a broken link, a missing card or a leaked key stops the release.
- **Components on versioned, immutable paths.** SG Meter went from v1.0 to v1.3 in an afternoon, each version on a new path with the old ones kept, so nothing that already worked could break.
- **A browser test** for the meter (depth, decline, below zero, the return page, personas, restore), added after the second release and run on every one after.
- **git as the history**, which is what made article versions a feature rather than a project, and the timeline above a query.
- **Things already built for something else.** The encrypted share reuses the subscribe identity, its published key, its write-only lane and its list agent; the persona graph reuses the site's article graphs.
- **Sessions that release on their own.** Several Claude sessions worked on this one repository in parallel, each fetching, rebuilding and releasing in minutes, which is why seven other pieces of work shipped in the same four hours without getting in the way.

These are all non-functional requirements: the work that never appears in a feature list. They are why the feature list could grow by one item every half hour.

## Do we have all the pieces?

I think so, for a first version, and it is worth being exact about what that means.

What exists and runs: a price for every page; metering by depth; a balance that never blocks; feedback that sets the price; personalisation through personas and newsrooms; a way for a reader to share their data with consent and encryption; a payment path; documentation for other sites; a [security page](../meter/security.md) with nine known gaps, all accepted and costed; and [hypotheses with thresholds](going-live-with-the-reading-meter.md) to check after eight weeks.

What does not exist yet:

- **The Stripe link itself.** Until it is set, readers see the simulated top-up, and the eight-week clock has not started. *Update, 11 October 2026: the link is set and payments are live on [newsroom.sgit.ai](https://newsroom.sgit.ai/account/top-up.html), so the clock has started.*
- **Payment verification.** A static site cannot receive Stripe's confirmation, so the return page credits without checking it, and says so. That is accepted, because the cost of someone faking a top-up is that they read more of our articles.
- **Your reading on more than one device.** Everything lives in one browser; a new device starts again unless you export. The answer is a persona in your own encrypted vault, which follows you and your agent, and which we cannot read. That is the next step, and it is why the vault matters.
- **The accounting side of real money**: receipts, and the obligations that come once revenue is material.
- **Readers.** This site does not have the traffic to say whether people pay.

And the real test is not the payment. It is whether a reader prefers the front page personalised for them, or for one of their personas, over the front page everybody gets. The persona that follows you, private by default and readable by us only if you choose, is the value; the payment is what a reader does when they feel it.

## Want to try it on your site?

SG Meter is ready for other sites: five files on versioned paths, a small config, a Stripe Payment Link, and [the documentation](../meter/index.md). How others can commercialise with it, and how we could help as a service, will be a future article, and we will publish it as a fully documented, open model.

What I do not have here is traffic: readers who come back every day. This would be far more interesting on a site that has them, and especially on one that is not monetising its readers much today, so it has almost nothing to lose. A blogger with a loyal readership would be a great fit. I am going to reach out to some people I know, and if you run a site like that, let's work together to test it. It will get more interesting still once the persona lives in the reader's own vault, so I would like a couple of sites validating the model before then. Write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo from Dinis Cruz, the releases of 10 October 2026 (v0.7.24 to v0.7.34) and their commits, read from git, the [SG Meter documentation](../meter/index.md), and the earlier articles on the meter: [a meter in the browser](a-meter-in-the-browser.md), [going live with the reading meter](going-live-with-the-reading-meter.md), [who will game the reading meter](who-will-game-the-reading-meter.md) and [pay to keep your persona](pay-to-keep-your-persona.md). The screenshots were taken in a fresh browser after reading six articles, so the balances are real for that browser.

## Threads

News & evidenceStartups & strategy[This article as a graph →](graphs.md#pay-after-you-read)

### Builds on

- [Open source is not free: who pays to keep the long tail working?](open-source-is-not-free.md) An old iMac, the long tail of old versions that projects are not paid to support, measured from public data, and five ways to pay for it, simulated.
- [Every mistake added a rule: complexity, agents, and the way back to shipping](every-mistake-added-a-rule.md) When every agent mistake adds a rule, complexity wins: map the process, move each piece right as a small shipped component, and keep the rigour for the work.
- [Going live with the reading meter: pay for what you read, go below zero if you like, and the numbers we will check in eight weeks](going-live-with-the-reading-meter.md) Pay for the share of a page you read, go below zero with no nagging, top up £5 on Stripe: the plan, and the numbers we check in eight weeks.
- [A meter in the browser: a penny a page, a history you keep, and a site that picks for you](a-meter-in-the-browser.md) Every page now costs a few pence from £5 of credit kept in your browser, and the reading history it keeps is what personalises the site.
- [Who will game the reading meter? Eight kinds of reader, nine ways to cheat, and the risks that will actually happen](who-will-game-the-reading-meter.md) Eight kinds of reader, none of them attackers, nine ways to cheat a browser meter, and the quieter risks that will actually happen.
- [Pay to keep your persona: readers should pay because it helps them, not because they feel they should](pay-to-keep-your-persona.md) Readers should pay because it helps them: a persona with a name and a graph, several for focus, and one that follows you between devices.

### Continued by

- [The vault crosses Chrome profiles: state and memory between browser sessions, found by using it rather than by building it](the-vault-crosses-chrome-profiles.md) The reader's vault carries the newsroom between Chrome profiles as it does between devices, a way to share state across browser sessions nobody built.
- [Not a straight line: working for RiskMandate by working on the newsroom, and why the thinking is never wasted](not-a-straight-line.md) Working on the newsroom solved RiskMandate's oldest problem in two days: progress is not a straight line, and the thinking is never wasted.
- [Why I love Wardley maps: the best of ours, how I read one, and a map inside a map inside a map](why-i-love-wardley-maps.md) The best of our Wardley maps with their context, why the technique matters, one map read as a story, and a map inside a map inside a map.
- [Places of highest leverage: where to focus when the agents can go in every direction, told with three days of real steps](places-of-highest-leverage.md) Where to focus when agents can go in every direction: the place of highest leverage, shown on three days of real steps, two walked back and one parked.
- [The key is the billing system: VoiceDebrief, a product with no server, the one thing it cannot sell, and who could let it](the-key-is-the-billing-system.md) VoiceDebrief runs with no server on the user's own key; the one thing it cannot sell is a capped key, and this maps who could allow it and what to ask them.
- [Firing journalists is the worst thing a publication can do: what a hiring decision says about where a publisher is going, and who to hire instead](firing-journalists.md) A hiring decision is a direction of travel: fire the journalists and the centre of gravity moves to packaging, where the metric makes clickbait by construction.
- [The site is an inbox: deciding before reading, marks that build the reader's own graph, and why I could not write this brief until the vault existed](the-site-is-an-inbox.md) The site as an inbox that starts empty: decide fast before reading, mark slowly while reading, build a graph you own, and sign what you send to the newsroom.
- [The vault is live: from a design on 11 October to a reader's vault on newsroom.sgit.ai by two in the morning, and how all of it fits together](the-vault-is-live.md) The reader's vault runs on newsroom.sgit.ai: a passkey opens three real vaults, each device writes one file, and the architecture is drawn as it stands.
- [The passkey opens the vault: a door per path, a master vault for every user, and no server of ours](the-passkey-opens-the-vault.md) Tested: a passkey's PRF bytes compute a door that holds the master's key, and a different path to the same passkey gives different bytes, so a door per path.
- [No server, by design: first I retired the database, now I am retiring the back end](no-server-by-design.md) First the database went, now the back end: the SGit Newsroom runs all its logic in the browser, on commodity servers that cannot read your data.
- [The agent is the reader: why agents will pay for graphs, personas and signed claims, because it is cheaper than not paying](the-agent-is-the-reader.md) Agents pay to read the raw web and guess its meaning. A curated graph answers for 90% fewer tokens, so paying the publisher is cheaper than not paying.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 65 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=65)

**Posting this article on LinkedIn?** The cover is [pay-after-you-read.jpg](banners/pay-after-you-read.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/pay-after-you-read.html)*
