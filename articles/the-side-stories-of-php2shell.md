# The side stories of php2shell: provenance, features built against a real problem, who corrects their reporting, a crisis with no named victim, the sites that went dark, the flaws nobody watched, and how much of it was AI, sgit.ai

> The PHP story site now holds enough data to go back in time and see how php2shell evolved, and that opens up stories beyond the headline. Provenance, which almost nobody does except Wikipedia. Building features against a real problem: 179 releases in three and a half days, each answering a need, none good enough the first time, and all of it a template for the next incident and for this newsroom. Who corrects their reporting: twelve correction requests are drafted, and one publisher, Amazon, changed "broadly exploited" to "broad exploitation attempts" without a note. A crisis with no named victim, which raises three questions at once: nobody has to disclose, nobody was hit, or sites were taken down for a danger that did not come. Detection: if an attack can be counted, it can be blocked, so why so few shared rules? The 17 entries in the ledger of sites that went dark, and what that cost. Who is being paid, when nobody is exploiting it. The flaws nobody watched: Zimbra's remote code execution is on CISA's exploited list with a national CERT reporting compromises, and got 16 news items to php2shell's 175. And how much of this was AI: AI helped find the flaws, but none of the public proofs of concept VulnCheck reviewed works the way the flaw does. If AI could do what people say it can now, where is the exploitation?

*Source: <https://newsroom.sgit.ai/articles/the-side-stories-of-php2shell.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The side stories of php2shell: provenance, features built against a real problem, who corrects their reporting, a crisis with no named victim, the sites that went dark, the flaws nobody watched, and how much of it was AI

# The side stories of php2shell: provenance, features built against a real problem, who corrects their reporting, a crisis with no named victim, the sites that went dark, the flaws nobody watched, and how much of it was AI

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-25 · [article v1.0.0](versions/the-side-stories-of-php2shell.md) · [newsroom v0.13.74](https://newsroom.sgit.ai/admin/versions.html) · php2shellprovenancecorrectionsexploitationaiopen-sourcearticle

***Abstract:** The PHP story site now holds enough data to go back in time and see how php2shell evolved, and that opens up stories beyond the headline. Provenance, which almost nobody does except Wikipedia. Building features against a real problem: 179 releases in three and a half days, each answering a need, none good enough the first time, and all of it a template for the next incident and for this newsroom. Who corrects their reporting: twelve correction requests are drafted, and one publisher, Amazon, changed "broadly exploited" to "broad exploitation attempts" without a note. A crisis with no named victim, which raises three questions at once: nobody has to disclose, nobody was hit, or sites were taken down for a danger that did not come. Detection: if an attack can be counted, it can be blocked, so why so few shared rules? The 17 entries in the ledger of sites that went dark, and what that cost. Who is being paid, when nobody is exploiting it. The flaws nobody watched: Zimbra's remote code execution is on CISA's exploited list with a national CERT reporting compromises, and got 16 news items to php2shell's 175. And how much of this was AI: AI helped find the flaws, but none of the public proofs of concept VulnCheck reviewed works the way the flaw does. If AI could do what people say it can now, where is the exploitation?*

The side stories of php2shell, from the data the PHP site keeps: provenance; building on a real problem; who corrects, and how; no named victim; detection and the WAF; the sites that went dark; follow the money; the flaws nobody watched; and how much of it was AI.

## In short

- **We now have data that lets us go back in time.** The evolution of the story, not only its latest state.
- **Provenance is rare.** Wikipedia is the other place I have seen it done well.
- **Features built against a real problem.** 179 releases in three and a half days, none good enough the first time.
- **Who corrects?** Twelve correction requests drafted; one publisher changed its words without a note.
- **No named victim.** Nobody has to disclose, nobody was hit, or sites went dark for nothing?
- **Detection is immature.** If you can count attacks, you can block them.
- **The sites that went dark,** and what that cost.
- **Follow the money.** Who is being paid, when nobody is exploiting it?
- **The flaws nobody watched.** Real exploitation, a fraction of the coverage.
- **How much was AI?** It helped find the flaws; where is the AI-driven exploitation?

## The data behind the side stories

The PHP story site now keeps a lot: [418 sources](https://php.oct.2026.newsroom.sgit.ai/sources/index.html) in its evidence vault, each with its captures; a [source watch](https://php.oct.2026.newsroom.sgit.ai/vaults/source-watch/index.html) of 913 pages that keeps a new snapshot whenever a page changes; and versioned views of [the state of affairs](https://php.oct.2026.newsroom.sgit.ai/views/index.html). Because nothing is thrown away, we can go back in time and see the evolution, and that lets us ask questions beyond the headline. These are the ones I want to explore. Some we can answer now; most need the record to keep growing.

## Provenance

The first is provenance itself. It is very rare for a site to show where each of its claims comes from. The only site I have seen do it well is Wikipedia, and even there you cannot easily see what a reference said or whether it changed. The PHP site goes further: every claim points to a source, every source to a dated capture with its hash. That is what makes the rest of this article possible.

## Features built against a real problem

This project is also a case study in how features should be built. If you develop features in a vacuum, you are predicting the problem. Here, every feature is built to solve a specific problem we have, right now, and we zoom in and iterate. The PHP site went from its first commit on the morning of 22 October to 179 releases by the afternoon of 25 October. Some of those features would normally take a week, or a month.

The key point is what happens when you use them: they are not good enough. The observability, the workflows, the UI: each one works, and each one immediately shows what it is missing. There is a lot of data to show, and the only way to understand how to show it is to see it and iterate. I wrote about one example, [why agent loops are hard](https://newsroom.sgit.ai/articles/why-agent-loops-are-hard.html).

When this stabilises, we will have two things. A template for the next major incident, or the next major story. And a set of features to bring back to this newsroom: the observability is the first, and we are already finding its limits, its scalability, what works and what does not.

## Who corrects their reporting?

Once we know which parts of a story were wrong, the next question is who goes back and corrects them. How many publishers revisit what they wrote, change it, and say "we did not get this right"? And does anyone correct without acknowledging it?

The PHP site's corrections liaison has [twelve correction requests](https://php.oct.2026.newsroom.sgit.ai/outreach/index.html) drafted, each quoting the publisher only from a capture. They are about two kinds of mistake. The first is the 70%: Wiz's headline said the flaws affect 70% of the internet, when its own post says PHP powers 70% of websites, and the BBC, CNN, Fortune and Clarín carried a version of it. The second is "exploited": headlines from WIRED and BankInfoSecurity said hackers exploited the flaws, when their own sources described attempts. None has been sent yet; I send each one myself.

And one publisher has already corrected without a note. Amazon's security blog said on 22 October that PHP2Shell "is now being broadly exploited in the wild". At 21:25 UTC that day it revised the sentence, as the PHP site's fact-check desk recorded, "without a note", to "now seeing broad exploitation attempts in the wild". That is a better sentence, and it is what the evidence supports. But anyone who quoted the first version is now quoting words that are no longer there, with nothing to tell them it changed. We only know because we kept both captures.

## A crisis with no named victim

The most interesting arc of the story is that, four days in, no named organisation has said it was compromised through php2shell. That touches two important points at once.

First, organisations do not have to disclose this kind of exploitation, so the absence of a named victim is not proof of no victims. Second, if organisations have not been hit, then many of them probably took sites offline that did not need to be. You take a site offline when there is a clear and present danger. Unless a lot of applications are being compromised, which the evidence does not show, this looks like an overreaction, and that is worth measuring.

Not to blame anyone. Somebody has to be [accountable](https://newsroom.sgit.ai/articles/who-signs-for-this.html), in the sense of making the right decision. As a CISO I was always aware that you have a limited number of credits with the business, unless you are adding a lot of value. Taking a site offline spends a lot of them. If you do it because of a clear and present danger, and the danger is not there, you have a problem the next time you need to ask.

## Detection, and the WAF

Detection does not seem mature yet, both of whether a site is vulnerable and exploitable, and of intrusions, with WAF rules. There are two sides to that. Some say they will not share detection details because it would help attackers. But if you do not share them, you do not help the defenders, and defenders who do not know what to block cannot block it.

And there is an inconsistency in the numbers. We have seen lots of figures about exploitation attempts. But if you can detect that an attack is happening, you should be able to put a rule on the WAF that blocks it. Cloudflare says its rules blocked the traffic it saw, and that attackers mutated their payloads to get past them; Switzerland's national cyber security centre says "even a web application firewall alone is not sufficient". We need good data on this, because we need good protections.

## The sites that went dark

This is the area I want to research most. Which sites went offline, what did that cost, which are still offline, why were they taken down, when are they coming back, and how much of it was acknowledged? The PHP site's ledger has 17 entries, from the Dutch national cyber security centre's own site, taken down "as a precaution", to Finland's and Latvia's government services, the Wikimedia Foundation, city councils in the UK, banks in Japan and Morocco, and, on 25 October, government portals in Nepal. Two are confirmed by the organisation; the rest come from the press. The community tracker lists 51 sites, with 50 back.

Some of the most striking cases are security products themselves. The Dutch NCSC's inventory, at its last change on 23 October, listed 10 products from security and network vendors as vulnerable, 26 as not, and 16 under investigation. How many of their users knew that the products protecting them ran PHP? And then there is the economic question we have already written about: [who pays for the fix](https://newsroom.sgit.ai/articles/who-maintains-the-php-you-run.html).

## Follow the money

Over time, I want to see whether money is flowing into this, and to whom. If there is little exploitation, it is not criminals making money, or not much. But a lot of teams are spending a lot of time on it: vendors, consultants, incident responders, extended-support providers, and every organisation that patched, tested, took something down and brought it back. Following the money means mapping who is being paid, and for what.

Then we can do the calculation. If that money had instead gone into the model I described, paying maintainers to sign off versions, paying for the tests and the pipeline that make [a patch routine](https://newsroom.sgit.ai/articles/patch-for-breakfast.html), and paying for certification, would we not be in a much better place? I think so, but I want the numbers.

## The coverage, and whether the conversation moved

How fast the coverage faded: the PHP site's evidence vault holds 4 sources published on 20 October, 117 on 21 October, 94 on 22 October, 34 on 23 October and 8 on 24 October, of 418 sources, 53 with no date; the latest days are partly the capture lag.

We also need to track the coverage over time. If you just follow the news, it is not sustainable: the energy goes, everyone moves on, and nothing changes. The evidence vault shows the curve: 117 of its sources were published on 21 October, the day of the release, 94 the next day, 34 the day after, and 8 on 24 October, though the latest days are partly the time it takes to capture them. So the real question is whether the conversation moved. Are we now talking about the sustainability of open source, or about who maintains the software everything runs on? That is a story the data can answer, given time.

## The flaws nobody watched

Attention against evidence, from the Pulse data: English-language news items over 30 days against the furthest step of evidence of exploitation. php2shell, 175 items, a public proof of concept and attempts reported, not on CISA's exploited list; Windows command injection, 40, on the list with attempts reported; BeyondTrust, 24; Ivanti, 23, on the list; a GitLab flaw rated 10.0, 22, no step reached; Zimbra, 16, on the list with a national CERT reporting compromises; SharePoint, 1, on the list with attempts reported.

The other big story is all the other vulnerabilities released at the same time, which got a fraction of the attention and, in some cases, have real exploitation behind them. We know the number of vulnerabilities is going to rise. The site has quietly started monitoring this, in a section called [Pulse](https://php.oct.2026.newsroom.sgit.ai/pulse/index.html), which keeps, for 26 flaws, the evidence of exploitation as eight dated steps, and beside it the attention each one gets, never combined.

The contrast is stark. php2shell had 175 English-language news items in the like-for-like count, a public proof of concept and exploitation attempts reported by a named party, and it is not on CISA's list of known exploited vulnerabilities. Zimbra's remote code execution flaw is on that list, and a national CERT reports compromises through it: 16 items. A SharePoint remote code execution flaw, on the list, with exploitation attempts reported: 1 item.

## How much of it was AI?

The last question is the one I most want answered. We talk about AI discovering vulnerabilities and about mass exploitation by AI. But we have always had this. We have always had big vulnerabilities, some with brands and logos; we have had Metasploit; we have had automatic scanners for decades; and we have had mass exploitation before.

AI did help find these flaws: the discovery came out of an AI-assisted research project, and the discoverers used AI models, as the reporting says. But on the other side, the evidence is thin. AhnLab, as reported, examined 100 related GitHub repositories and classed 27 as proofs of concept. Sophos, as reported, found working exploitation difficult even with AI support. And the PHP site records that none of the public proofs of concept reviewed by VulnCheck had the correct mechanism. Neither flaw is on CISA's exploited list.

So, if AI can do now what people say it can do, and I am not saying it will not in the future, where is the exploitation? I think the answer is a mix of three things. Orchestrating this is hard. Someone needs a business model or an agenda to do it at scale. And, for many of these assets, the value of exploiting them, beyond making some noise, is probably not that significant. If there were a lot of value on the other side, people would be doing it. I could be wrong. That is why I want to answer it from the data we have, rather than from the headlines.

## What this does not claim

- **These are questions, not findings.** Most need more time and more data.
- **No named victim is time-bounded.** One statement would change it, and disclosure is not required.
- **The ledger of sites taken offline is incomplete,** and most of its entries come from the press.
- **Attention counts are hard to compare.** The like-for-like English-language count is used here; the PHP site warns that its wider counts, over different numbers of feeds, should not be compared row with row.
- **The coverage curve includes capture lag** for the latest days.
- **The correction requests are drafted, not sent.** The publishers have not yet been asked.
- **The AI evidence on exploitation is as reported** by AhnLab, Sophos and VulnCheck, through the press and the PHP site.

## Where this comes from

My voice memo of 25 October 2026. The PHP story site at release v0.21.4, read on 25 October: its sources (`data/sources.json`, 418 sources), its [state of affairs](https://php.oct.2026.newsroom.sgit.ai/views/index.html) (`data/state.json`, version 3), its [corrections requests](https://php.oct.2026.newsroom.sgit.ai/outreach/index.html) (`data/outreach.json`) and fact-check record of Amazon's revision (`data/factcheck.json`), its ledger of [systems taken offline](https://php.oct.2026.newsroom.sgit.ai/impact/index.html) (`data/impact.json`), its defence claims (`data/claims.json`, Cloudflare and the Swiss BACS on WAFs), its [Pulse](https://php.oct.2026.newsroom.sgit.ai/pulse/index.html) section (`data/pulse.json`), and its git history (179 releases since 22 October). Related: [who maintains the PHP you run?](https://newsroom.sgit.ai/articles/who-maintains-the-php-you-run.html), [patch for breakfast](https://newsroom.sgit.ai/articles/patch-for-breakfast.html), [who signs for this?](https://newsroom.sgit.ai/articles/who-signs-for-this.html), [sources and their shadows](https://newsroom.sgit.ai/articles/sources-and-shadows.html), [why agent loops are hard](https://newsroom.sgit.ai/articles/why-agent-loops-are-hard.html), [PHP October 2026, update 3](https://newsroom.sgit.ai/articles/php-daily-2026-10-24.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Agents & policyStartups & strategy[This article as a graph →](graphs.md#the-side-stories-of-php2shell)

No other article links here yet.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 281 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=281)

**Posting this article on LinkedIn?** The cover is [the-side-stories-of-php2shell.jpg](banners/the-side-stories-of-php2shell.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-side-stories-of-php2shell.html)*
