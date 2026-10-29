---
title: The evidence behind four days: Jeremiah Grossman's php2shell post, checked claim by claim against the data, with the provenance and the graphs, and the two things that changed since
date: 2026-10-27
author: Dinis Cruz
author_url: about/index.html
summary: Four days after php2shell went public, Jeremiah Grossman, CEO of Root Evidence, posted on LinkedIn that the evidence does not support the wave of AI-enabled breaches many were bracing for, that the exploits are environment-specific, that in the same four days over a thousand CVEs were published and almost none were exploited, and that the rule is the old one: patch what adversaries exploit. This is the data behind each claim, re-counted from public sources and from the PHP story site's evidence, with every number traceable to a query or a captured source. Most of it holds. The post's timestamp is the CVE record's to the second; NVD counts 1,394 CVEs in the same window, not 1,448; none references Exploit-DB or Metasploit; VulnCheck published 25 old bugs with 2017 to 2025 IDs on 22 October; CISA had listed one, the Arista flaw. Two things changed after the post: CISA added both php2shell CVEs to its catalogue on 26 October, and their EPSS scores went from 0.06 and 0.12 to above 0.999 the day before. As of 09:43 UTC on 27 October, no named organisation had said it was compromised through php2shell. The yearly numbers are consistent with the post's wider point, but cannot test it: CVE publications more than doubled this year, while additions to CISA's catalogue rose by 30%. Corrected on 27 October after a review by ChatGPT, which the editor asked for; the changes are listed at the end.
version: v0.13.105
license: https://creativecommons.org/licenses/by/4.0/
tags: php2shell, evidence, vulnerabilities, kev, epss, data, article
status: published
---

!shot jg-post.webp | images/ | Jeremiah Grossman's LinkedIn post on php2shell, four days after it went public, as shared with me on 27 October 2026. | medium | aside

## In short {#in-short}

- **Jeremiah's post holds up.** Most of its numbers reproduce from public data; the rest are marked below.
- **The timestamp is exact.** The CVE record was published at 13:48:34 UTC on 21 October.
- **1,394, not 1,448,** by NVD's count for the same window. Close, but not reconciled: we have possible causes, not the two lists compared.
- **Almost none are expected to be exploited.** 1,361 of 1,383 have an EPSS below 0.01, a 30-day forecast, not a count; none cites Exploit-DB or Metasploit in NVD.
- **No confirmed victim, as of 09:43 UTC on 27 October.** Attempts, honeypot shells and a CISA listing, yes; of eight named organisations, none confirmed as php2shell.
- **The exploits are environment-specific,** as the post says: the public ones are tuned, raced, or wrong.
- **Two things changed since.** CISA listed php2shell on 26 October; EPSS went above 0.999 the day before.
- **The yearly data is consistent with the wider point, but cannot test it.** CVEs more than doubled; CISA's catalogue grew by 30%.
- **AI does cut the effort of building exploits,** in Wiz's own account. That is a research capability, not evidence of adversaries' use or of victims.
- **Some numbers need data we do not have.** We have asked the PHP story site's team for them.

## The post {#post}

Jeremiah Grossman is the CEO of Root Evidence. Four days after the disclosure, Jeremiah wrote that "plenty of people are calling it the arrival of AI-enabled exploitation at scale and bracing for a wave of breaches", and that "the evidence says otherwise". The claims, in the post's order: the exploits that work are built "for specific environments and a generic wide sweeping exploit is unlikely"; honeypots "have caught plenty of attempts"; "nobody has reported mass compromise, some reports of individual breaches, but nothing confirmed"; in the same four days 1,448 more CVEs were published, nobody published exploit code for any of them in Metasploit or Exploit-DB, VulnCheck put 25 of them on its KEV list, 24 of them old bugs given IDs on 22 October, and CISA added just one, the Arista VeloCloud Orchestrator flaw; Censys counts 32 million PHP services on an affected version. Then the opinion: nothing in the record shows AI "driving up how many vulnerabilities adversaries exploit, or how fast", adversaries "keep working a small set of bugs until those stop paying", so patch php2shell, then "patch what adversaries exploit".

The [PHP story site](https://php.oct.2026.newsroom.sgit.ai/) keeps exactly the record needed to check this, and the rest is public: NVD's API, CISA's catalogue, FIRST's EPSS scores and the CVE records. Every number below comes from one of them, except where marked; the queries and the derived data are in [this article's dataset](https://newsroom.sgit.ai/articles/data/the-evidence-behind-four-days__dataset.json).

## Claim by claim {#claims}

!shot jg-window.webp | images/ | The CVEs of the four-day window, re-counted on 27 October 2026, against Jeremiah Grossman's figures. Log scale. | chart

| Claim in the post | What the data says | Verdict |
| --- | --- | --- |
| Public at 13:48:34 UTC on 21 October | The CVE record for CVE-2026-109618: published 2026-10-21T13:48:34.845Z | Exact |
| 1,448 CVEs in four days | NVD: 1,394 in the same window, 12 of them rejected | Close; not reconciled |
| No exploit code in Metasploit or Exploit-DB | None of the 1,394 NVD records references either | Holds, as far as NVD shows |
| VulnCheck: 25 on its KEV, 24 old bugs given IDs on 22 October, years 2017 to 2025 | NVD: VulnCheck, as a CNA, published 25 CVEs with 2017 to 2025 IDs, all on 22 October | Close, not the same: 25 old-ID CVEs in NVD against the post's 24 old of 25 on the KEV; KEV membership and when the IDs were assigned not checked |
| CISA added one: Arista VeloCloud Orchestrator | CVE-2026-114625, published 22 October, listed 23 October; the other listing that day, a Collabora flaw, was published on 14 October | Exact at the time; three now |
| Censys: 32 million PHP services on an affected version | Censys's dashboard is quoted at 36.7 million services on 22 October, by Fortinet | Not reproduced |
| Honeypots caught plenty of attempts | Amazon's MadPot, ELLIO's sensors, Chainguard's honeypots, Cloudflare's "millions" | Holds |
| No mass compromise; nothing confirmed | No named organisation has said it was compromised through php2shell, at 09:43 UTC on 27 October | Holds, as a time-bounded absence |
| Exploits built for specific environments | The public chains are tuned to one build, raced, or have the wrong mechanism | Holds |

## No wave, and nothing confirmed {#record}

!shot jg-record.webp | images/ | The compromise record on the PHP story site at 09:43 UTC on 27 October, by kind, and what eight organisations said. | chart

The PHP story site's [evidence on compromise](https://php.oct.2026.newsroom.sgit.ai/compromise/index.html) is a list of every statement, each with its captured source. Its line, at 09:43 UTC on 27 October, six days in: "No named organisation has said it was compromised through php2shell." Its 53 rows divide as the figure shows. Three kinds of evidence need keeping apart here: attempts, seen by honeypots and sensors; successful exploitation in a lab or honeypot set up for it, such as the 35 shells below; and a confirmed compromise of a production system, of which there is none so far. CISA's listing sits between them: CISA's own assessment, added to both CVE records, marks exploitation as "active", and names no victim. The eight named organisations are the "reports of individual breaches": GMO Internet Group found malicious programs on servers of its trading service and has not stated the cause; Czech Technical University stopped an attack; Valtec first blamed the PHP flaw, then said the attackers used a flaw in its own service; DMM halted services and would not say whether it was PHP; Germany's Interior Ministry said its site "was not hacked"; Anexia confirmed attempts; Ahold Delhaize denied any link; and the Square Enix report is second-hand and does not say how the access happened.

Two more data points from the site's claims since Jeremiah posted. Palo Alto Networks Unit 42 retracted, on 25 October, its statement of two days earlier that tied an attack on a European government agency to php2shell, having been unable to confirm the initial access (as reported by SC Media). And watchTowr's head of threat intelligence put reliable indiscriminate exploitation at "a firm No".

## Exploits built for specific environments {#specific}

The record agrees with him, and is specific about why:

- **The CVSS vector itself** says attack complexity is high (AC:H) for both CVEs, and CISA's assessment on the CVE record marks it "Automatable: no".
- **The public bounty win** needed one exact PHP build and worker setup, succeeded about seven times in ten in its author's own lab, and took about three hours once the target had a PHP page to attack, as [we checked yesterday](https://newsroom.sgit.ai/articles/what-the-bitcoin-bounty-actually-proves.html).
- **A honeypot result** of 35 working shells came from what the site's sources call a deliberately favourable setup, on a vulnerable build.
- **VulnCheck,** as cited by a detection author, found that none of the public proofs of concept it reviewed had the correct mechanism; Fastly says a working exploit needs knowledge of the running binary's layout.

Honeypots did catch plenty: Amazon's MadPot saw an attempt four days before disclosure, ELLIO's sensors logged hits from the first morning, Chainguard's honeypots by 22 October (as reported second-hand), and Cloudflare's CEO counted "millions" of attempts. [The site's exploitation timeline](https://php.oct.2026.newsroom.sgit.ai/exploitation/index.html) lists each with its source.

## The other 1,392 {#window}

!shot jg-epss.webp | images/ | EPSS scores for the 1,383 CVEs in the window, and the daily scores of the two php2shell CVEs. | chart

NVD counts 1,394 CVEs published between 13:48:34 UTC on 21 October and the same time on 25 October. The difference from the post's 1,448 is small, and not reconciled. Two possible causes: NVD's publication time is not always the CVE record's, and counts move as records are added, rejected or re-dated. Only comparing the two lists of IDs would settle it, and we do not have the post's list. Of the 1,394, NVD had fully analysed 3 when we counted on the morning of 27 October (30 by 15:44 UTC the same day); 12 were rejected; most were waiting. They came mostly on weekdays: 494 and 497 on 22 and 23 October, 39 on the Sunday.

None references Exploit-DB or Metasploit, which says what NVD's references hold, not what exists elsewhere. FIRST's EPSS, which models the probability of exploitation activity in the next 30 days, scored 1,383 of them on 26 October: 1,361 below 0.01, 19 between 0.01 and 0.1, one Brotli decoder flaw at 0.36, and the two php2shell CVEs at 0.99997 and 0.99981. That is a forecast: a low score means the model does not expect exploitation, not that none was seen. VulnCheck, acting as a CVE authority, published 25 CVEs with ID years from 2017 to 2025, all on 22 October, which is close to the post's numbers (it says 25 on VulnCheck's KEV, 24 of them old) and matches the pattern Jeremiah describes. But an ID's year does not show when it was assigned, and we have not read VulnCheck's KEV, so whether these are the 25 on it is not checked.

## What changed after the post {#changed}

Two things, both in the direction of "php2shell is exploited", neither in the direction of a wave:

- **CISA listed both CVEs** in its Known Exploited Vulnerabilities catalogue on 26 October, version 2026.10.26 released at 22:24 UTC, with a due date for federal agencies of 29 October. A listing requires evidence of exploitation; it names no victim, and the PHP story site's compromise line did not change. So the window's count on CISA's catalogue is now three: the Arista flaw and the php2shell pair. The site's newsroom [carried the listing to readers 5 h 21 min later](https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-27__report__the-kev-listing-run/index.html).
- **EPSS jumped first.** Both php2shell scores went from about 0.06 and 0.12 on 24 October to 0.99997 and 0.99981 on 25 October, a day before CISA's listing. Meanwhile the Arista flaw, which CISA listed as exploited on 23 October, sits at 0.01. A model of likely exploitation and a catalogue of evidenced exploitation are different instruments, and they disagree in both directions.

## Attention is not exploitation {#attention}

!shot jg-attention.webp | images/ | News items about php2shell and twelve flaws already on CISA's catalogue, from the PHP site's Pulse agent, 24 October. | chart

The PHP story site has an agent, Pulse, that tracks other vulnerabilities in the news beside php2shell, with two things kept apart: the evidence of exploitation, as eight levels from a public proof of concept to a named victim, and the attention, as counts of news items. On 24 October, with 53 to 55 feeds checked for each row, php2shell had 295 news items and had reached levels 1 and 4: a public proof of concept and attempts reported by a named party. Twelve flaws that CISA had listed as exploited in the same fortnight, or that were old flaws newly listed, had 11 to 48 news items each. Three of them were from 2015 and 2016. Read it as a description of coverage in this collection, not a controlled measure: similar numbers of feeds are not the same feeds, and a named pair of flaws is counted against single CVEs. Even so, it is consistent with the post's closing argument: what is exploited and what is talked about are different lists, and patching should follow the first. A run with the same feeds for every row is in our brief.

## Is AI driving it? {#ai}

!shot jg-ratio.webp | images/ | CVEs published by NVD and entries added to CISA's KEV catalogue, 1 January to 26 October of each year, 2023 to 2026. | chart

Jeremiah's opinion is that nothing in the record shows AI driving up how many vulnerabilities adversaries exploit, or how fast. The yearly numbers describe the background, but they cannot test that. From 1 January to 26 October, NVD published 89,531 CVEs this year, more than twice the 40,266 of the same period in 2025; CISA's catalogue added 274 entries, 30% more than the 210 of 2025, so additions as a share of publications fell from 0.62% in 2023 to 0.31%. The two numbers count different populations, since CISA's additions include CVEs published in earlier years; the catalogue records what CISA has evidence for, not attack volume or speed; and neither says anything about AI. Testing the claim needs matched cohorts: the CVEs published in a period, each followed for the same time, with the time to the first evidence of exploitation. We have asked for that below.

Three questions need keeping apart. Can AI help build exploits? Yes, by the account of a team that found php2shell: Wiz's researchers wrote that frontier models enabled them "to develop and adapt working exploits across multiple applications in hours", and that "a single researcher completed in a week what previously would have taken a world-class team months of work". Are adversaries using it at scale? Jeremiah expects so: "I can't imagine any exploit writer or cyber adversary not using heavy AI tooling at this point". Has it produced more exploited flaws, faster, or more victims? That is the post's claim, and on this record the answer is not yet, with the caveat that four days and a catalogue are a small window on it. The first is a demonstrated research capability; the post is about the second and third.

## The 32 million {#exposure}

!shot jg-exposure.webp | images/ | What each published exposure figure for PHP counts, from Censys to Unit 42 and "almost 70% of websites". Log scale. | chart

The post's 32 million is Censys's count of services, not servers or organisations. Censys's dashboard was quoted at 36.7 million services on 22 October. If both figures are the same measure, the count went down. That could be patching, but also scan coverage, services going offline, fingerprints or the method changing; and, as Fortinet notes, "version-based estimates may include installations already patched through vendor backports". We could not read the dashboard ourselves, so the trend is a question, not a finding. What the record does show is how far apart the published figures are: from 1.57 million unpatched hosts to "almost 70% of websites", because each counts a different thing, and a version string is not the same as an exploitable server.

## What we asked the PHP team for {#asked}

Some of the post cannot be checked from public data, and some of it deserves a better dataset than the one we have. We have written [a brief for the PHP story site's team](https://newsroom.sgit.ai/admin/notes/2026-10-27__brief-for-the-php-team__the-four-days-data.md) asking for: VulnCheck's KEV entries for the window; Censys's exposure count as a series since 21 October, with its definition; the reconciliation of 1,448 and 1,394; a check of Metasploit, Exploit-DB and nuclei for the php2shell pair and the window, which Pulse could not do because its GitHub searches were refused; a Pulse run over all the CVEs CISA and VulnCheck listed in the window, with the same feeds for every row; honeypot and sensor volumes by day, to test whether adversaries "keep working a small set of bugs"; and the time from publication to a KEV listing, by year, to test "how fast".

## What this does not claim {#limits}

- **The post is quoted, not endorsed by its author.** This article is ours.
- **NVD's count differs from the post's,** and both are snapshots of moving records.
- **VulnCheck's KEV and Censys's dashboard were not read.** The table marks them as such.
- **"No reference in NVD" is not "no exploit anywhere".** NVD's references are incomplete.
- **The yearly ratio is a rate,** not the share of the same set of CVEs. It describes; it does not test AI's effect.
- **EPSS is a forecast.** It is used here for what the model expects, not for what was observed.
- **The attention chart is descriptive.** The rows do not share the same feeds.
- **The compromise record is a time-bounded absence.** One statement from one organisation would end it.

## Reviewed, and corrected {#review}

The editor asked ChatGPT to review this article on 27 October, and pasted its review to me. Its verdict was "changes needed", with nine findings, and I agree with all nine. The record is at [the end of this page](#reviews) and on [the reviews page](https://newsroom.sgit.ai/reviews/index.html), with what was done about each. In short:

1. **EPSS was used as if it were an observation.** It is a 30-day forecast; the summary now says "expected", and the window section says what a low score does and does not mean.
2. **The yearly comparison was used about AI.** It now describes the background and says what a test would need.
3. **Wiz's account was missing.** It is now quoted, with three questions kept apart: research capability, adversaries' use, and victims.
4. **"0.9998" did not reproduce both scores.** Now 0.99997 and 0.99981, or "above 0.999".
5. **The absence of a confirmed victim had lost its bound** in the summaries. It now carries its date, and attempts, lab or honeypot success and production compromise are kept apart, with CISA's "Exploitation: active" on the CVE records.
6. **1,448 against 1,394 was "explained" when it was not.** Now "not reconciled".
7. **VulnCheck's 25 matched in count only.** Assignment dates and KEV membership are now marked as not checked.
8. **The attention chart was presented as controlled.** It is now labelled as descriptive.
9. **The fall from 36.7 to 32 million was read as patching.** Now with the other possible causes, and Fortinet's note on backports.

One point in the review I could not confirm: that watchTowr reports exploitation through its honeypot network. The PHP story site's capture tool got a 403 from watchTowr's pages, and its fact-check desk marked that claim as resting on search summaries only. The core of Jeremiah's post is unchanged by any of this: no wave of confirmed breaches in four days, and patch what adversaries exploit.

Then a fresh look. Claude Fable, from another vendor than ChatGPT and not the model that wrote this article, reviewed the corrected text the same afternoon. Its verdict was "approve with changes": all nine of ChatGPT's fixes hold, and every quote of Jeremiah's post matches the screenshot. It re-ran the counts from NVD, CISA, EPSS and the CVE records and got the same numbers, and found seven smaller points, all now fixed: VulnCheck's 25 old-ID CVEs are close to the post's "24 of those 25 are old bugs", not the same; the links to the PHP story site's data at version 0.1.77 had expired, and now point to the files by their hash; the section heading should read 1,392, since both php2shell CVEs are among the 1,394; NVD's count of fully analysed records had moved from 3 to 30 during the day; the summary's "about 0.1" is now 0.06 and 0.12, as in the body; a missing full stop; and Chainguard's honeypots are dated as reported. Both reviews, and the answer to every finding, are at the end of this page.

## Where this comes from {#sources}

Jeremiah Grossman's LinkedIn post on php2shell, written four days after the disclosure, as shared with me on 27 October 2026. Public data read on 27 October 2026: [NVD's CVE API 2.0](https://services.nvd.nist.gov/rest/json/cves/2.0?pubStartDate=2026-10-21T13:48:34.000&pubEndDate=2026-10-25T13:48:34.000&resultsPerPage=1) for the window and for yearly totals; [CISA's KEV catalogue](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json), version 2026.10.26; [FIRST's EPSS API](https://api.first.org/data/v1/epss?cve=CVE-2026-109618,CVE-2026-109619,CVE-2026-114625&scope=time-series); [the CVE record for CVE-2026-109618](https://cveawg.mitre.org/api/cve/CVE-2026-109618); [Fortinet's post](https://www.fortinet.com/blog/industry-trends/understanding-php2shell-vulnerabilities-and-reducing-risk-while-you-patch) for Censys's 22 October figure; [Wiz Research's post on PHP2Shell](https://www.wiz.io/blog/php2shell-php-rce) of 21 October for its account of AI-assisted exploit development. The PHP story site's data at version 0.1.77 (its [manifest](https://data.php.oct.2026.newsroom.sgit.ai/v/0.1.77/manifest.json); the files below are linked by their hash, since the site serves plain paths only for its five newest versions): [compromise.json](https://data.php.oct.2026.newsroom.sgit.ai/blobs/7582d4c6168e59f1ad58d609737538bb0c0709b4c27461f2c4adc73ecf708352), [exploitation.json](https://data.php.oct.2026.newsroom.sgit.ai/blobs/b51ff8179b0b75f5e8ef2916484a28c9a0d707d8542594f6b0c844fa44b54914), [claims.json](https://data.php.oct.2026.newsroom.sgit.ai/blobs/4305a8e70e42a8296e8c84d27e5fba7e155de9630f032d6152d099386e5b32b6), [numbers.json](https://data.php.oct.2026.newsroom.sgit.ai/blobs/31ba0a4f36a6a3a74a461a4818c542cd675f248980e8dc92ef4195431a826efb) and [pulse.json](https://data.php.oct.2026.newsroom.sgit.ai/blobs/bfdcfa48d580729af74bc0f50e4fa9fd9ce5fbf6e613f03e9129d3dcd7b8a6bd), each pointing to its captured sources on [the references site](https://refs.php.oct.2026.newsroom.sgit.ai/sources/index.html). This article's own data: [the dataset](https://newsroom.sgit.ai/articles/data/the-evidence-behind-four-days__dataset.json). Related: [what the bitcoin bounty actually proves](https://newsroom.sgit.ai/articles/what-the-bitcoin-bounty-actually-proves.html), [PHP October 2026, update 4](https://newsroom.sgit.ai/articles/php-daily-2026-10-26.html), [the side stories of php2shell](https://newsroom.sgit.ai/articles/the-side-stories-of-php2shell.html), [patch for breakfast](https://newsroom.sgit.ai/articles/patch-for-breakfast.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
