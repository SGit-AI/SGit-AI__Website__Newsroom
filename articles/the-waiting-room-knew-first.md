# The waiting room knew first: a live local story, and the gap where local information used to be, sgit.ai

> This afternoon, at two London hospitals, staff told the people in front of them that the IT systems were down. One waiting room was announced at about five hours, and a doctor said the problem was national. Nothing a person could check before leaving home showed any of it: no notice from the trust, no post, no local story, no dated search result. This is not a story about one hospital, whose staff were working through it, and it is not yet a story about a national outage, which has not been confirmed. It is a story about where local information is supposed to come from now. The information existed; it reached people only once they were already in the waiting room. Northern Ireland publishes live emergency waits for every hospital, updated tonight at 10.20 pm, and Wales has a live service; England has no national equivalent, and I found no live or disruption page for the trust involved. Local news has thinned out, and the social feeds that used to carry this kind of thing have fragmented. So I have started a vault to log this as a live local story, with the evidence separated by level, the public sources checked on a schedule, and an enquiry to the trust that my agent will send. It is the real counterpart of the fictional bridge story, and the first of several.

*Source: <https://newsroom.sgit.ai/articles/the-waiting-room-knew-first.html> · sgit.ai v0.7.82 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The waiting room knew first: a live local story, and the gap where local information used to be

# The waiting room knew first: a live local story, and the gap where local information used to be

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-08 · [article v1.0.0](versions/the-waiting-room-knew-first.md) · [sgit.ai v0.7.9](https://sgit.ai/admin/versions.md) · local-newslive-evidencenhshospitalspublic-informationit-outageevidence-levelsvaultsagentsstory-vaultnews-desertsarticle

***Abstract:** This afternoon, at two London hospitals, staff told the people in front of them that the IT systems were down. One waiting room was announced at about five hours, and a doctor said the problem was national. Nothing a person could check before leaving home showed any of it: no notice from the trust, no post, no local story, no dated search result. This is not a story about one hospital, whose staff were working through it, and it is not yet a story about a national outage, which has not been confirmed. It is a story about where local information is supposed to come from now. The information existed; it reached people only once they were already in the waiting room. Northern Ireland publishes live emergency waits for every hospital, updated tonight at 10.20 pm, and Wales has a live service; England has no national equivalent, and I found no live or disruption page for the trust involved. Local news has thinned out, and the social feeds that used to carry this kind of thing have fragmented. So I have started a vault to log this as a live local story, with the evidence separated by level, the public sources checked on a schedule, and an enquiry to the trust that my agent will send. It is the real counterpart of the fictional bridge story, and the first of several.*

What the people inside knew this afternoon, and where a local person could have looked before leaving home. The information existed. It reached people only once they were already in the waiting room.

**Where this comes from.** I spent this afternoon at two London hospitals, accompanying someone to an appointment; they are fine, and nothing about them belongs in this article. What happened around us does. The research behind it was done this evening, with care to separate what I saw from what I was told and from what anyone can verify, and it is all in [the vault](https://sgit.ai/demos/vaults/local-evidence-log/index.md). It follows [The Mill Street Bridge](the-bridge-followed-to-the-end.md), a fictional local story kept as a story vault. This one is real, and it is still happening.

## In short

- **Two hospital sites, one afternoon, the same message from staff: the IT systems are down.** One waiting room was announced at about five hours. A doctor said the problem was national.
- **Nothing a local person could check before leaving home showed it.** No notice from the trust, no matching post, no local story, nothing dated today in search. The channels that do carry operational status need a login or an NHS network connection.
- **This is not naming and shaming.** Both sites are run by the same trust, and its staff were working through it in front of us. The question is about the channel, not the people: when a service is running badly, where does a local person find out in time to plan their day?
- **Parts of the UK already answer that question for emergency waits.** Northern Ireland publishes live median waits for every emergency department; Wales has a live service; some English trusts publish their own. England has no national live page, and I found nothing live for this trust.
- **The places that used to carry this have thinned out.** Local newsrooms have closed, and the social feeds where you could once find a post saying "avoid X today, systems down" are more fragmented and less trusted.
- **So I have started a vault to log it**, as a live local story: the evidence by level, the open questions, the public sources re-checked on a schedule, and an enquiry to the trust that my agent will send. It is the first of several.

**The gap, Mermaid source**

[rendered image](images/le-gap.webp)

```
flowchart TB
  subgraph inside["What the people inside knew, this afternoon"]
    direction LR
    ST["Staff at the desk<br/>'the IT systems are down'"]
    DR["A doctor<br/>'it is national'"]
    IN["Internal bulletins<br/>and supplier alerts"]
    SD["NHS service desk portals<br/>login or NHS network needed"]
  end
  subgraph outside["Where a local person could look before leaving home"]
    direction LR
    WS["The hospital's website"]
    SO["Social media"]
    LN["Local news"]
    SE["A search engine"]
  end
  P(["Someone deciding<br/>whether to go now,<br/>later or tomorrow"])
  ST -- "said out loud,<br/>to people already there" --> P
  DR -- "said in the room" --> P
  IN -. "not public" .-x P
  SD -. "registration, login,<br/>NHS network" .-x P
  WS -. "no notice found" .-x P
  SO -. "no matching post found" .-x P
  LN -. "no story found" .-x P
  SE -. "nothing dated today" .-x P
```

## What happened, separated by level

I am going to be careful here, because the easiest thing to do with an afternoon like this is to turn it into a bigger story than the evidence supports. So each item is labelled with what it is.

| What | Level | What it does not establish |
|---|---|---|
| Staff at Charing Cross Hospital said the IT systems were down | Told on the spot by staff | Which systems, how many, since when |
| We were directed to Western Eye Hospital | Observed first-hand | Why; it is a specialist service, and the referral could have been for the care needed |
| Staff at Western Eye also said the IT systems were down | Told on the spot by staff | That it was the same fault |
| An approximately five-hour wait was announced | Told on the spot by staff, as an announcement | An actual five-hour wait, or how much of it the IT added |
| The waiting room was almost full | Observed first-hand | The cause, or how unusual that is for the department |
| A doctor said the problem was national | Heard second-hand: said to the patient, passed on to me | What "national" meant: a national service, a supplier, or a regional fault |

And from the research, which is in the vault with every source and how it was accessed:

- **Both sites are run by one trust**, Imperial College Healthcare NHS Trust, according to the Care Quality Commission's records. That matters: two sites of one organisation are not two independent pieces of evidence for a national outage.
- **The trust shares IT with its neighbours.** Its own announcement from October 2025 describes a joint IT function and a common Cerner patient administration system across four north-west London trusts. That makes a shared regional dependency a fair line of enquiry. It does not make Cerner, or anything else, the failed system; what failed has not been said publicly.
- **The leads that look relevant do not fit.** A London power notice from another hospital was dated three days ago. Two NHS maintenance windows tonight start at 18:00, after the afternoon. An e-Referral outage is scheduled for tomorrow night. Each was checked against the date on the page, not the date in the search result.
- **Nothing confirms or rules out a national incident.** The NHS service desk status portal, the NHS.net Connect status page and the supplier's support portal all asked for a login. Not finding an incident there is a limit of access, not evidence that there was none.
The same afternoon in the vault: fourteen claims grouped by what the evidence supports, each with its evidence, its level and what would resolve it.

So the honest summary is: a credible first-hand account of IT disruption at two sites of one trust, with a long announced wait, national scope unconfirmed, cause unknown, recovery unknown. That is a small story by news standards. It is not small if you are deciding whether to set off now.

## Newsworthy to me

What strikes me most is not the outage. IT fails, and the staff I saw were doing what staff do: telling people, apologising, getting on with it. What strikes me is that the only way to find out was to be there.

If I had known at lunchtime that both sites were running without their systems, with a five-hour wait being announced, I could have made a different decision. Gone later, gone tomorrow if it could wait, gone somewhere else, or at least gone knowing what the day would look like. We could not make that decision well, because the one fact that mattered was not available anywhere I could look.

That is the gap. It is not that someone hid anything; the research found no sign of that, and the channels that do exist are built for NHS staff and suppliers, not for patients. It is that this kind of information is not newsworthy to a newsroom, not in scope for a national status page, and not anyone's job to publish for the people about to walk through the door. And yet, for those people, it is the most newsworthy thing happening that afternoon.

## Where a local person could look, today

The research for this article looked for public, live or near-live information about how a hospital is running. Here is what exists, verified this evening.

| Where | What it publishes | How fresh |
|---|---|---|
| Northern Ireland, [nidirect](https://www.nidirect.gov.uk/articles/emergency-department-average-waiting-times) | Median time of patients currently waiting, for every emergency department | Live; the page read "Last updated: 10.20 pm, Thursday 8 October 2026" |
| Wales, [My A&E Live](https://aeinfo.nhs.wales/) | Typical time you are likely to spend, for most hospitals | Live |
| England, some trusts, for example [Mid Cheshire](https://www.mcht.nhs.uk/patients-and-visitors/waiting-times-feed) | Current waits for majors and minors, patients in the department | Live, with no timestamp shown |
| England, nationally | Monthly A&E statistics; weekly elective waits on [My Planned Care](https://www.myplannedcare.nhs.uk/?p=137) | Weekly or monthly |
| Scotland | A weekly emergency department update from Public Health Scotland | Weekly |
| Imperial College Healthcare | No live waits or disruption page found | n/a |
| Alberta, New South Wales, Queensland | Live emergency waits; [Alberta](https://www.albertahealthservices.ca/waittimes/waittimes.aspx) says its calculation "is done every 2 minutes" | Live |

Where could a local look? Sixteen places in the vault, whether each is live, and whether it was found to carry anything about this incident.

Two things follow. First, publishing live operational information for hospitals is clearly possible: Northern Ireland does it for every emergency department, tonight. Second, even the best of these pages answers a narrower question than the one I had. A live wait is a number; it does not say "the systems are down, expect delays, here is the next update". The status pages that software companies publish do say that, and they have become an ordinary thing to see.

There is a legal duty in this area, and it is narrower than it sounds. The Civil Contingencies Act gives the bodies it lists a duty to "warn the public, and to provide information and advice to the public if an emergency is likely to occur or has occurred", but only for emergencies serious enough to obstruct their work, and the regulations under it ask responders to avoid "alarming the public unnecessarily". A same-day IT problem that slows a service down is very likely below that bar, and whether the duty applies to this particular trust is something I have not settled. The NHS has published incident updates for patients before, during the 2024 cyber attack in south-east London. That was a declared, weeks-long incident. Nothing similar is expected for an afternoon like this one, which is exactly the gap.

## Why the gap is wider now

For a while, local information like this had somewhere to go. A local paper might run it, a local reporter might post it, and someone in the waiting room might tweet "avoid the eye hospital today, systems down", which the next person would find by searching. Much of that has thinned out.

- **Local news.** The Public Interest News Foundation's latest map, from December 2025, counts 4.4 million people living in local news deserts, and London has the lowest coverage, about one outlet per 100,000 residents. Press Gazette counted at least 293 local newspapers closed since 2005. London lost its last daily print paper in September 2024.
- **The social feeds.** The Reuters Institute's 2026 Digital News Report puts weekly use of X for news in the UK at 10 per cent, down 2 points, with Facebook at 21 per cent. Local Facebook groups now carry much of what is local, and they carry it unevenly: a Social Market Foundation study this June found misinformation in about one in 26 news-related posts in local Facebook groups, and Full Fact found genuine local appeals being dismissed as hoaxes. A real "the hospital's IT is down" post can be lost, or disbelieved.
- **The outage trackers.** Services that track outages track websites. One of them showed zero user reports for the NHS today, which is correct about the websites and says nothing about a ward running on paper.

None of these is a failure by one organisation. Together they leave a person with no good way to find out, and a vacuum that rumour fills more easily than evidence.

## Not naming and shaming

I have to name the trust, because that is where the evidence is, and I want to be clear about what this is not. It is not a complaint about the staff, who were working through an IT failure while a waiting room filled up. It is not a claim that the trust hid anything; there is no evidence of that. And it is not a claim that the NHS was down nationally; that has not been confirmed.

It is a question that applies to any trust, any council, any transport operator: when a local service is running badly, where does a local person find out, in plain words, in time to plan? The vault is built to keep asking it, with evidence, and to change its answer when the evidence changes.

## The vault, and what happens next

[The Local evidence log](https://sgit.ai/demos/vaults/local-evidence-log/index.md) is a vault for live local stories, and this is its first incident. It keeps:

- **Observations, by level**: heard second-hand, told on the spot by staff, observed first-hand, documented, confirmed by the organisation, independently corroborated. Each level says what it can and cannot establish.
- **Claims and their status**: what is supported first-hand, what is verified, what is plausible, what is unresolved, and what would resolve it.
- **The sources**: every page the research used or tried, and how it was accessed: fetched, indexed only, blocked, or behind a login. Blocked is a limit of our access, never evidence about the hospital.
- **The leads that do not fit**, with their real dates.
- **The enquiry**: a short, specific request to the trust's press office, asking which service failed, the incident reference, the sites affected, what "national" meant, and where a patient could have found out. My agent will send it; when it goes, and when an answer comes, both are logged.
- **Regular checks**: a tool that fetches the public sources again and records what changed, so that if a notice appears tomorrow, or never, the log will show it.

I will also ask a couple of clinicians I know whether they can find out what happened, without naming anyone. And I want to do more of these. Every local story like this one is a small test of the same idea as the [bridge](the-bridge-followed-to-the-end.md) and of [Reader Skills on a story vault](story-vault-meets-reader-skills.md): that local information is worth keeping as evidence, with its sources and its gaps, in a form that a person or an agent can query.

## What would close the gap

- **A plain status line for local services.** Which sites, which services, attend or not, next update at what time. Northern Ireland's live emergency waits show the publishing part is possible.
- **A route from the inside to the outside.** The people at the desk knew. A one-line public notice, sent by whoever already sends the internal bulletin, would have reached the people about to leave home.
- **Evidence, not rumour.** A log where a local report is kept with its level, its time and its source, and checked, rather than a post that is either believed or dismissed.
- **Something that keeps asking.** An agent that re-checks the sources, sends the enquiry and logs the answer, so that the question does not die with the afternoon.

*Drafted from a voice memo and an evening's research by Dinis Cruz, who is the author of the argument and the person with editorial responsibility, by agent@riskmandate.ai (Claude Opus 5.5, claude-opus-5-5) in the sgit.ai site session, on 8 October 2026. No hospital, supplier or NHS office has been contacted yet; the enquiry is drafted in the vault and will be sent by the author's agent. The patient and their condition are deliberately not described. The figures on local news are from the Public Interest News Foundation (December 2025), Press Gazette (August 2024), the Reuters Institute Digital News Report (2025 and 2026, the 2026 platform figures via a journalism.co.uk summary), the Social Market Foundation (June 2026) and Full Fact (August 2023); the legal text is from legislation.gov.uk; every source, with how it was accessed, is in the vault.*

## Threads

News & evidenceVaults & method[This article as a graph →](graphs.md#the-waiting-room-knew-first)

### Builds on

- [The bridge, followed to the end: what one local story is worth when it is kept as a graph](the-bridge-followed-to-the-end.md) A bridge closure simulated on a story vault: newsworthy on 5 days, needed on 57, used by three readers, four buyers and an agent, and paid back to its sources.
- [Story vault underneath, Reader Skills on top: why local journalism has the most to gain](story-vault-meets-reader-skills.md) Markus Franz's Reader Skills on top, the story vault underneath: each skill is a graph query, and local stories can pay back down their chain of sources.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 49 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=49)

## From the desk

- [Local news, kept as evidence](collections/local-news-kept-as-evidence.md) collection, 6 articles

**Posting this article on LinkedIn?** The cover is [the-waiting-room-knew-first.jpg](banners/the-waiting-room-knew-first.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-waiting-room-knew-first.html)*
