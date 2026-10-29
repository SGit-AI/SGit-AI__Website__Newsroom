# Take it or leave it: is Meta's crawling clause legal? The law that could reach it, the precedents against Meta, and the asymmetry at its heart, sgit.ai

> Meta's updated Commercial Terms, due on 20 November 2026, let Meta crawl the websites of any business that uses Facebook, Instagram or WhatsApp, create test credentials on them, and keep pulling updates; a business that does not agree must stop all business use of Meta's products. My first reaction was that this is blackmail. The law has a more precise word: Article 102 of the EU Treaty, and the UK's Competition Act word for word, forbid a dominant company from making a contract conditional on "supplementary obligations" that have "no connection with the subject" of the contract. This is not legal advice, and no regulator or court has ruled on the clause. But the routes exist: competition law, which has already found Meta's terms for business customers unfair once, in 2024; the EU's Digital Markets Act; the platform-to-business rules; copyright; and, in the UK, a regulator that says it is "very alive" to the risk but has not designated Meta. And there is an asymmetry worth stating plainly: everything the clause lets Meta do to a business's website, Meta's own terms forbid on Facebook and WhatsApp. If it is legal, I think it should not be.

*Source: <https://newsroom.sgit.ai/articles/take-it-or-leave-it.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Take it or leave it: is Meta's crawling clause legal? The law that could reach it, the precedents against Meta, and the asymmetry at its heart

# Take it or leave it: is Meta's crawling clause legal? The law that could reach it, the precedents against Meta, and the asymmetry at its heart

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-27 · [article v1.0.0](versions/take-it-or-leave-it.md) · [newsroom v0.13.107](https://newsroom.sgit.ai/admin/versions.html) · metapublisherslawcompetitionlicensingcrawlersrightsarticle

***Abstract:** Meta's updated Commercial Terms, due on 20 November 2026, let Meta crawl the websites of any business that uses Facebook, Instagram or WhatsApp, create test credentials on them, and keep pulling updates; a business that does not agree must stop all business use of Meta's products. My first reaction was that this is blackmail. The law has a more precise word: Article 102 of the EU Treaty, and the UK's Competition Act word for word, forbid a dominant company from making a contract conditional on "supplementary obligations" that have "no connection with the subject" of the contract. This is not legal advice, and no regulator or court has ruled on the clause. But the routes exist: competition law, which has already found Meta's terms for business customers unfair once, in 2024; the EU's Digital Markets Act; the platform-to-business rules; copyright; and, in the UK, a regulator that says it is "very alive" to the risk but has not designated Meta. And there is an asymmetry worth stating plainly: everything the clause lets Meta do to a business's website, Meta's own terms forbid on Facebook and WhatsApp. If it is legal, I think it should not be.*

Meta's Commercial Terms page, with the crawling clause highlighted.

## In short

- **This is not legal advice.** No regulator or court has ruled on the clause, and Meta can impose it on 20 November.
- **The law has a name for what it does.** Conditions with "no connection with the subject" of a contract, imposed by a dominant firm.
- **Meta has lost on this before.** €797.72 million in 2024, for unfair terms that used business customers' data.
- **The EU's Digital Markets Act has a direct hook,** fair access for business users of Facebook and Instagram, never yet tested.
- **The UK can't use its new powers.** Meta has no strategic market status there; the old competition law still applies.
- **Copyright is the quiet part.** A licence the publisher signs can make its machine-readable opt-out irrelevant.
- **Meta forbids on its own products what it asks for on yours.** Crawling, accounts, ignoring robots.txt.
- **Fines have not changed the pattern.** Meta earned about $166 million a day in 2025.
- **If this is legal, it should not be.** Reciprocity is the minimum a publisher should ask.

## My first reaction

When I read the clause in [Tami Hoffman's post](https://www.linkedin.com/posts/tami-hoffman_mediapolicy-ai-ugcPost-7520771480264306688-x85h), [which we went through earlier today](https://newsroom.sgit.ai/articles/meta-terms-and-the-news.html), my first reaction was that this is blackmail. You use a platform for one thing, to reach your readers, to run ads, to talk to customers on WhatsApp. The platform then says: to keep doing that, give us the right to crawl your website, create accounts on it and keep pulling from it. And if you don't agree, leave.

Blackmail is a strong word, and it is not the right one in law. But the law does have a word for this, and it is close to what I felt. Article 102 of the Treaty on the Functioning of the European Union says that an abuse of a dominant position may consist in "making the conclusion of contracts subject to acceptance by the other parties of supplementary obligations which, by their nature or according to commercial usage, have no connection with the subject of such contracts". The UK's Competition Act 1998, section 18(2)(d), says the same, word for word. The point before it, (a), covers "unfair trading conditions".

So the question is not whether it feels wrong. It is whether Meta is dominant where it matters, whether the crawling has a connection with the services Meta provides, and which regulator acts first. What follows is what I found, with the sources, and where I think the answer should go if the law does not get there.

## What the clause actually reaches

The text, as Meta's preview of the updated terms puts it: Meta, "or any entity acting on our behalf", may "use automated software (such as web scrapers, bots, robots, spiders, crawlers, and user agents) and create test credentials to access, index, cache, analyze, collect, retrieve, or crawl the domains, web pages, or URLs (and any content available through them) that are associated with your products or services, or that are made available through your or users' use of Meta Company Products and services, and to periodically pull updates" from them.

Three things about its reach are easy to miss:

- **It is not only your website.** It covers URLs "made available through your or users' use of" Meta's products, so links that other people share.
- **It covers every business use.** The Commercial Terms apply to any business use of Facebook, Instagram, WhatsApp and Messenger, not only advertising. WhatsApp is a messaging service, which businesses use to talk to their customers.
- **robots.txt is not in it.** Meta says it respects robots.txt. Its own crawler documentation says Meta-ExternalFetcher "may bypass robots.txt rules" and FacebookExternalHit "might bypass robots.txt when performing security or integrity checks". A policy is not a term, and this one has exceptions.

The word "train" was removed after the first objections, and the date moved from 30 October to 20 November. The European Publishers Council's answer to the first change: "removing that one word does not establish an express exclusion of AI training, fine-tuning, grounding".

## The asymmetry

What Meta's terms let it do to a business's website, against what Meta allows on Facebook and WhatsApp.

My next question was the simplest one: can a publisher do the same to Facebook? The answer, in Meta's own words, is no.

- **Facebook's terms:** "You may not access or collect data from our Products using automated means (without our prior permission)".
- **Meta's Automated Data Collection Terms:** "You will not engage in Automated Data Collection without first obtaining Meta's express written permission", and "You will comply with Meta's robots.txt protocols". The data may be used for search results and link previews, and "All other Uses are prohibited".
- **facebook.com's robots.txt** opens with "Collection of data on Facebook through automated means is prohibited unless you have express written permission from Facebook", names the crawlers of OpenAI, Anthropic, Google's AI training and others as fully blocked, and ends with `Disallow: /` for everyone else.
- **Accounts:** on Facebook, one account per person, in your real name; on WhatsApp, you may not "create accounts for our Services through unauthorized or automated means".

And Meta enforces it. In 2023 it sued Voyager Labs, saying it "designed its scraping software to use fake accounts to scrape data accessible to a user when logged into Facebook"; the case settled in December 2024 with a permanent injunction and a payment to Meta. Fake accounts used to collect data from behind a login is close to a description of what "test credentials" would let Meta do on a news site.

There is one place where the courts went the other way, and it is worth knowing. In Meta v. Bright Data, in January 2024, a US court found that a scraper collecting public pages while logged off "stands in the same shoes as a visitor to whom the Terms cannot apply" (as quoted by the law firm Farella Braun + Martel). Meta dropped the rest of the case a month later. So public pages are public, both ways. The clause is about something else: consent, given under pressure, to go further than a visitor can.

## The law that could reach it

The legal routes in the EU, the UK, Germany and India, and where each stands on 27 October 2026.

**Competition law, Article 102, and Meta's own record.** On 14 November 2024 the European Commission fined Meta €797.72 million for "tying its online classified ads service Facebook Marketplace to its personal social network Facebook and by imposing unfair trading conditions on other online classified ads service providers". The unfair conditions were in Meta's terms for business customers, and they let Meta "use ads-related data generated by other advertisers for the sole benefit of Facebook Marketplace". In the same decision the Commission found Meta "dominant in the market for personal social networks". That is the closest precedent I found: same company, same kind of terms, business customers' data taken for Meta's benefit. And in June 2026 the Commission ordered interim measures against Meta over WhatsApp's terms for rival AI assistants, about six months after the change; the crawling clause takes effect in weeks.

**Germany has gone further.** In 2019 the Bundeskartellamt prohibited Facebook from combining data from other websites without real consent, and its president said: "In view of Facebook's superior market power, an obligatory tick on the box to agree to the company's terms of use is not an adequate basis for such intensive data processing." The EU's Court of Justice later held, in Meta v Bundeskartellamt (2023), that a competition authority may consider whether terms break other laws, the GDPR there, as "a vital clue". The decision became final in 2024, and Germany designated Meta under section 19a of its competition act in 2022, which lets it prohibit practices without proving dominance in a single market.

**The Digital Markets Act.** Article 6(12) says a gatekeeper "shall apply fair, reasonable, and non-discriminatory general conditions of access for business users to its ... online social networking services". For Meta that means Facebook and Instagram, not WhatsApp or the ad tools. It has never been tested on a social network, and DMA interim measures can only follow formal proceedings, which have not been opened. The German publishers' associations say the clause "infringes Meta's obligation to grant business users fair and reasonable conditions of access".

**The Platform-to-Business Regulation** requires terms "drafted in plain and intelligible language", at least 15 days' notice of changes, and a right to terminate; terms that do not comply are "null and void". It applies to Facebook and Instagram as services for businesses selling to consumers, but not to the ad tools, and it is about procedure, not whether a term is fair.

**The UK.** The Competition and Markets Authority has not designated Meta with strategic market status, so the new conduct requirements, which include trading "on fair and reasonable terms", are not available. Its chief executive, Sarah Cardell, told a Lords committee: "We obviously don't have a live designation in relation to Meta", and that it was "very alive to the potential impact that this could have for UK businesses". The CMA has written to Meta. The old route, the Competition Act's Chapter II, needs an investigation opened before any interim measures.

**India** has already called this shape of term by its name. In November 2024 the Competition Commission fined Meta ₹213.14 crore over WhatsApp's 2021 privacy policy, imposed on a "take-it-or-leave-it" basis; the appeal tribunal upheld the fine in November 2025.

## The quiet part: copyright

This is the part I think matters most for publishers, and it is not obvious. In the EU, text and data mining of public content is allowed unless the rightholder has reserved it "in an appropriate manner, such as machine-readable means". That is what robots.txt and the newer machine-readable licences do. But the protection is against mining done under the exception. A licence the rightholder signs is a different thing: if a publisher accepts Meta's terms, Meta can argue it has permission, and the opt-out never comes into play. The Directive protects some exceptions from being overridden by contract; it deliberately does not list this one.

That is my reading of the texts, not a ruling, and it has limits. A business can only grant rights it holds: wire copy, freelance photographs and syndicated pieces belong to someone else. The EU's AI Act requires providers of general-purpose models to respect opt-outs. And in the UK, where there is no commercial mining exception at all, a licence is the only route, which makes the contract more important there, not less.

## Test credentials, and the people on the page

A news site is not only the publisher's words. It carries readers' comments, profiles, bylines, the names of people in stories. A crawler that logs in reaches what a logged-in reader sees. Two things follow.

First, a publisher's agreement does not cover those people. Under the GDPR, Meta would need its own lawful basis for their data; the publisher cannot consent for its readers. The irony is that Meta was fined €265 million by the Irish regulator in 2022 for failing to protect its own users from scraping.

Second, consent to access is what computer misuse law turns on. In the UK, access is unauthorised if the person does not have consent "from any person who is so entitled". Meta would argue the terms are that consent. But the person who clicks accept on an ad account may not control the whole site, the owners of sites that users merely link to never agreed, and creating accounts to get past a paywall may not be the "kind" of access anyone consented to. James Grimmelmann, of Cornell, told Nieman Lab, as reported, that the wording would let Meta "sign up as a fake user". WAN-IFRA asked Meta to "remove the right to create test credentials", and to commit that paywalls "will not be circumvented". As far as I can find, Meta has not answered.

And yes, this is where Cambridge Analytica comes in. In 2018 Facebook said the data of "up to 87 million people" may have been shared improperly through an app on its platform; the US Federal Trade Commission imposed a $5 billion penalty in 2019, and on 21 October this year a New Mexico court ordered Meta to pay $25 billion over the state's privacy case, which Meta says it will appeal. That case was about data collected through Meta's platform about people who had not agreed. The clause runs the other way, onto other people's platforms, and the same question applies: who agreed for the people on the page?

## If we get sued, we pay the fine

Meta's largest fines and penalties, in euros and in dollars, against its 2025 earnings.

My suspicion is that Meta has priced this in. It is a suspicion, not a fact, but the numbers make it reasonable. The largest GDPR fine to date, €1.2 billion in 2023, is still under appeal. The Commission's Marketplace fine was €797.72 million; the DMA fine in 2025 was €200 million. Meta's net income in 2025 was $60.5 billion, about $166 million a day. Cory Doctorow put the logic in one line: "Companies that fear a regulator will fine them more than they expect to make from cheating, will cheat less." The reverse is also true.

## A textbook case of enshittification

Doctorow's word for the pattern is enshittification, and his definition fits this better than anything I could write: "first, they are good to their users; then they abuse their users to make things better for their business customers; finally, they abuse those business customers to claw back all the value for themselves." What makes the last stage possible is switching costs, which he describes as "everything you have to give up when you leave a product or service".

For news, those costs are real. In this year's Reuters Institute Digital News Report, "Facebook remains the biggest platform overall for news consumption (used by 43% this year)", and "for the first time, social media and video networks are, on average across the markets covered, more popular than both TV and owned news websites and apps as sources of news". At the same time, according to the Institute's 2026 trends report, referrals from Facebook to news sites fell by 43% in two and a half years. Less traffic sent, more taken: that is the third stage. And Meta has shown what "leave it" means: since August 2023 it has blocked news in Canada rather than pay under the Online News Act.

The closest analogy I found is not a landlord or a shopping centre, though those come to mind. It is the investigation the Commission opened in December 2025 into Google, over publishers who cannot refuse the use of their content in AI answers "without losing access to Google Search", and YouTube creators who cannot upload without letting Google use their videos. The same shape: your content, as the price of a platform you cannot leave.

## My view: if it is legal, it should not be

Even if every route above fails, I think a rule like this should not be possible, and the principle to fix it is simple: **a platform should not be able to impose on its business users terms it would not accept from them.** If Meta may crawl a publisher's site and create accounts on it, the publisher should be able to do the same on Meta's products, on the same terms. Meta will not offer that, which tells you what the clause is.

Concretely, what would make it fair:

- **No condition without a connection.** Crawling an advertiser's landing page to check an ad is connected. Crawling a newsroom because it has a Facebook Page is not.
- **robots.txt and machine-readable licences binding, in the contract,** with no documented exceptions.
- **No test credentials,** and paywalls and registration walls left alone.
- **WhatsApp and Messenger out.** A messaging service is not a reason to crawl anyone.
- **Saying no without losing the tools,** which is WAN-IFRA's fifth demand.

And, as I argued earlier today, publishers should not wait for regulators: state the terms on their own sites in machine-readable form, price their crawls, and build the channels they own. The law moves slowly; a file on your own server can be published today.

## What to watch

- Whether the Commission or the CMA opens formal proceedings before 20 November, which interim measures would need.
- Whether Meta writes robots.txt, an exclusion for news, or a definition of "business products" into the text.
- Whether the CMA starts a strategic market status investigation into Meta, as the News Media Association asks.
- What the press associations' complaints actually argue, when they are published.
- The appeals: New Mexico's $25 billion order, and the Marketplace fine.

## What this does not claim

- **This is not legal advice.** It is a reading of public texts by someone who is not a lawyer. Nothing here is settled until a regulator or court rules.
- **Dominance is not proven here.** Article 102 and section 18 apply only to a dominant firm in the relevant market; the 2024 finding was about personal social networks.
- **The copyright point is my reading,** not a court's. I found no lawyer applying it to this clause.
- **Some sources are press reports.** The complaints are not public; the New Mexico order, Nieman Lab's article and some fines rest on press reports.
- **Meta's statements are attributed to Meta,** since reports differ on which spokesperson gave some of them.
- **The clause is quoted from Meta's US preview.** The UK page uses British spelling, and the final text may change before 20 November.

## Where this comes from

The clause: Meta's [Commercial Terms preview](https://www.facebook.com/legal/commercial_terms_preview) and [current Commercial Terms](https://www.facebook.com/legal/commercial_terms), read on 27 October 2026; Tami Hoffman's [LinkedIn post](https://www.linkedin.com/posts/tami-hoffman_mediapolicy-ai-ugcPost-7520771480264306688-x85h). Meta's own rules: [Facebook Terms of Service](https://www.facebook.com/terms), [Automated Data Collection Terms](https://www.facebook.com/apps/site_scraping_tos_terms.php), [facebook.com/robots.txt](https://www.facebook.com/robots.txt), [WhatsApp Terms of Service](https://www.whatsapp.com/legal/terms-of-service), [Meta's web crawlers](https://developers.facebook.com/docs/sharing/webmasters/web-crawlers/). Law: [Article 102 TFEU](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:12016E102), [Competition Act 1998 s.18](https://www.legislation.gov.uk/ukpga/1998/41/section/18), [Digital Markets Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R1925), [Platform-to-Business Regulation](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32019R1150), [DSM Directive](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32019L0790), [Computer Misuse Act 1990 s.17](https://www.legislation.gov.uk/ukpga/1990/18/section/17), [DMCC Act 2024 s.20](https://www.legislation.gov.uk/ukpga/2024/13/section/20). Decisions: European Commission [IP/24/5801](https://ec.europa.eu/commission/presscorner/detail/en/ip_24_5801) (Marketplace), [IP/25/1085](https://ec.europa.eu/commission/presscorner/detail/en/ip_25_1085) (DMA), [IP/26/1276](https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1276) (WhatsApp interim measures), [IP/25/2964](https://ec.europa.eu/commission/presscorner/detail/en/ip_25_2964) (Google and publishers); the [Bundeskartellamt's 2019 decision](https://www.bundeskartellamt.de/SharedDocs/Meldung/EN/Pressemitteilungen/2019/07_02_2019_Facebook.html) and [section 19a designation](https://www.bundeskartellamt.de/SharedDocs/Meldung/EN/Pressemitteilungen/2022/04_05_2022_Facebook_19a.html); the Court of Justice in [C-252/21](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62021CJ0252); the [Irish DPC's scraping decision](https://www.dataprotection.ie/en/news-media/press-releases/data-protection-commission-announces-decision-in-facebook-data-scraping-inquiry); [Bar & Bench](https://www.barandbench.com/news/cci-imposes-21314-crore-penalty-on-meta-for-abuse-of-dominant-position) on India's CCI order. Cases: [Meta on Voyager Labs](https://about.fb.com/news/2023/01/leading-the-fight-against-scraping-for-hire/), [Farella Braun + Martel on Bright Data](https://www.fbm.com/post/102kqw7/). Cambridge Analytica: [Facebook, 2018](https://about.fb.com/news/2018/04/restricting-data-access/), [the FTC](https://www.ftc.gov/news-events/news/press-releases/2019/07/ftc-imposes-5-billion-penalty-sweeping-new-privacy-restrictions-facebook), [Al Jazeera on New Mexico](https://www.aljazeera.com/news/2026/10/22/facebooks-wrongdoing-why-has-meta-been-fined-25bn-in-new-mexico). The UK: [Press Gazette, 21 October 2026](https://pressgazette.co.uk/news/uk-competition-chief-very-alive-to-risks-from-sweeping-meta-scraping-change/). Publishers: [WAN-IFRA's letter](https://cdn.wan-ifra.org/wp-content/uploads/2026/10/22151536/20261022_WAN-IFRA-Meta-TC-Letter.pdf), [PPC Land](https://ppc.land/meta-delays-website-crawling-terms-to-nov-20-after-publisher-complaints/). Doctorow: [Pluralistic, 21 January 2023](https://pluralistic.net/2023/01/21/potemkin-ai/) and [30 January 2024](https://pluralistic.net/2024/01/30/go-nuts-meine-kerle/). News use: the Reuters Institute's [Digital News Report 2026](https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2026/dnr-executive-summary) and [Trends and Predictions 2026](https://reutersinstitute.politics.ox.ac.uk/journalism-media-and-technology-trends-and-predictions-2026). Meta's finances: its Form 10-K for 2025. Related: [Meta's new terms and the news](https://newsroom.sgit.ai/articles/meta-terms-and-the-news.html), [free to copy, paid at the source](https://newsroom.sgit.ai/articles/free-to-copy-paid-at-the-source.html), [websites you own](https://newsroom.sgit.ai/articles/websites-you-own.html). Researched and written by this site's agent, newsroom.writer, from three research passes with their notes kept; the editorial responsibility is mine.

## Threads

News & evidenceStartups & strategy[This article as a graph →](graphs.md#take-it-or-leave-it)

No other article links here yet.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 303 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=303)

**Posting this article on LinkedIn?** The cover is [take-it-or-leave-it.jpg](banners/take-it-or-leave-it.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/take-it-or-leave-it.html)*
