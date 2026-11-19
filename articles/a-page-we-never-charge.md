# A page we never charge: how the PrompTugal agents found that YouTube's terms forbid charging to watch an embedded player, on the one site of ours that bills, put the conflict to me as a question, quoted the six conditions from YouTube's own policies once I suggested a page that is never charged, and built the gate that refuses a YouTube player on any page that is, in 84 minutes of commits, sgit.ai

> Just after midnight on 19 November the PrompTugal agents had a working YouTube key and a feed of Web Summit's official replays, and a problem. YouTube's developer policies say "API Clients must not charge users to watch content in an embedded YouTube player", and promptugal.news is the one site of ours that bills its readers. The licensing agent put YouTube's terms on its register as unclear; the conductor brought the question to me rather than fixing it. My answer was to put the videos on a page that is never charged, because our billing is per page, not per site. Within six minutes the licensing agent had quoted YouTube's own policies and set six conditions; the designer drew the page within them, the journalist wrote its explanation, and the developer built a flag for free pages and a gate that refuses a YouTube player on any page that is charged. From the first finding to the gate: 84 minutes of commits. The page itself is not live yet; it waits for the licensing agent to check it against the six conditions.

*Source: <https://newsroom.sgit.ai/articles/a-page-we-never-charge.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / A page we never charge: how the PrompTugal agents found that YouTube's terms forbid charging to watch an embedded player, on the one site of ours that bills, put the conflict to me as a question, quoted the six conditions from YouTube's own policies once I suggested a page that is never charged, and built the gate that refuses a YouTube player on any page that is, in 84 minutes of commits

# A page we never charge: how the PrompTugal agents found that YouTube's terms forbid charging to watch an embedded player, on the one site of ours that bills, put the conflict to me as a question, quoted the six conditions from YouTube's own policies once I suggested a page that is never charged, and built the gate that refuses a YouTube player on any page that is, in 84 minutes of commits

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-19 · [article v1.0.0](versions/a-page-we-never-charge.md) · [newsroom v0.14.164](https://newsroom.sgit.ai/admin/versions.html) · promptugalyoutubetermslicensingbillingagentsarticle

***Abstract:** Just after midnight on 19 November the PrompTugal agents had a working YouTube key and a feed of Web Summit's official replays, and a problem. YouTube's developer policies say "API Clients must not charge users to watch content in an embedded YouTube player", and promptugal.news is the one site of ours that bills its readers. The licensing agent put YouTube's terms on its register as unclear; the conductor brought the question to me rather than fixing it. My answer was to put the videos on a page that is never charged, because our billing is per page, not per site. Within six minutes the licensing agent had quoted YouTube's own policies and set six conditions; the designer drew the page within them, the journalist wrote its explanation, and the developer built a flag for free pages and a gate that refuses a YouTube player on any page that is charged. From the first finding to the gate: 84 minutes of commits. The page itself is not live yet; it waits for the licensing agent to check it against the six conditions.*

designer@'s mock-up of the free replays page: "Free to watch", YouTube's own player, the credit and the Terms link.

## In short

- **The clause:** YouTube's policies say "API Clients must not charge users to watch content in an embedded YouTube player".
- **The clash:** promptugal.news is the one site of ours that bills its readers.
- **The question came to me,** not a fix; the idea and the decision were mine.
- **The answer:** a page that is never charged, because the billing is per page, not per site.
- **Six conditions,** quoted from YouTube's own pages, then a design, a text, a flag and a gate.
- **84 minutes** from the first finding to the gate; the page waits on one last check.

## The clause

Around midnight on 18 November I set up a Google Cloud project with a key for five APIs, YouTube's Data API among them, and the PrompTugal team had a feed of Web Summit's official replays from the organiser's own channel. The obvious next step was to show the videos on promptugal.news.

The team has a licensing agent, rights@, started that evening, whose job is to read the terms of every source before anything from it is shown. At 00:19 UTC it put YouTube's API terms on its register as finding R6 and marked commercial use "unclear". The reason is one sentence in YouTube's Developer Policies, under Playback Integrity: "API Clients must not charge users to watch content in an embedded YouTube player." And promptugal.news is the one site of ours that bills its readers: its meter charges by how much of a page was read ([paid by the read](paid-by-the-read.md)).

## A question, not a fix

The conductor, conductor.b@, did not choose for me. It could have dropped the videos, or put them on one of our free sites, or decided that a page with a meter was fine if the player itself was free. Its commit at 00:50 is the question, put to me.

My answer, at about 01:05, recorded in the team's guidance: "what about putting them in a page that is not charged, which actually is a really powerful case study and example of the power of our custom billing model, since we can be compliant with that requirement by using an IFrame for Google and not charging for that page right?"

That is the point of billing per page. A site that charges for some pages can choose not to charge for others, and can do it where another party's terms say it must not.

## Six conditions

At 01:11 rights@ committed YouTube's Developer Policies and Required Minimum Functionality, quoted from the source, and a conditional go with six conditions for the page:

- **C1, never charged or gated:** no paywall, sign-in or meter between the reader and the play button.
- **C2, no advertising or sponsorship** sold on or around the player.
- **C3, YouTube's own iframe player,** at least the size YouTube sets ("Embedded players must have a viewport that is at least 200px by 200px"), with nothing over it: "You must not display overlays, frames, or other visual elements in front of any part of a YouTube embedded player".
- **C4, YouTube credited** and its Terms of Service linked beside the player.
- **C5, nothing from the API kept** longer than the 30 calendar days the policies allow.
- **C6, not counted as a read,** so the reading log and the simulated payments to sources never include it.

No agent accepted YouTube's terms on my behalf; the register says so in its first line, and that decision stays mine.

The commits from rights@'s first finding at 00:19 to dev@'s gate at 01:43 UTC on 19 November.

## The build

Each step answered the one before it. At 01:16 the journalist agent drafted the page's own explanation of why it is free. At 01:20 designer@ committed a specification and mock-ups at desktop and phone widths, light and dark: a green "Free to watch" note above the title, YouTube's player from youtube-nocookie.com, a text credit and the Terms link under each player, no logo until the branding guidelines were read. At 01:26 rights@ quoted YouTube's branding guidelines and said the design was a go. At 01:43 dev@ built the flag: a page marked free loads no meter, so it is never charged, never in a reading log and never in the simulated payments. The site's build gate now refuses three things: a YouTube player on a page that is not free, a free page that still loads the meter, and a player from youtube.com instead of youtube-nocookie.com.

## What it shows

- **Billing per page, not per site.** The rule that limits us is YouTube's; the page that obeys it is ours to make.
- **Terms read before anything is shown.** The clause was found before a single video was on a page, and quoted from YouTube's own text.
- **Agents found it; a person decided.** The agents found the conflict and the exact clause; the idea and the decision were mine.
- **A trail you can follow.** Every step is a commit or a board file in a public repository.

## What this does not claim

- **The page is not live yet.** It waits for rights@ to check the built page against C1 to C6.
- **The times are commit times** in the repository; the agents' own notes sometimes give times a few minutes later, as their clocks ran ahead.
- **Nothing here is legal advice,** and nothing is claimed about YouTube beyond its published text.

## Where this comes from

[PrompTugal__News__Website](https://github.com/PrompTugal/PrompTugal__News__Website) on its dev branch, read on 19 November 2026: `board/team/rights/findings.md` (R6), `board/team/rights/register/google-apis.md`, `board/guidance/2026-11-19-signed-commits-paid-search-and-free-embeds.md` (section 3), `board/spec-the-free-replays-page.md`, `board/team/dev/note-2026-11-19-free-pages.md`, `newsroom/build/features/free-pages.mjs` and the mock-ups in `design/decisions/free-replays/`. YouTube's [Developer Policies](https://developers.google.com/youtube/terms/developer-policies) and [Required Minimum Functionality](https://developers.google.com/youtube/terms/required-minimum-functionality), read on 19 November 2026. Earlier: [paid by the read](paid-by-the-read.md), [PrompTugal.news, the newsroom we ran at Web Summit](promptugal-news-the-newsroom-we-ran.md).

## Threads

Agents & policy[This article as a graph →](graphs.md#a-page-we-never-charge)

### Builds on

- [Paid by the read: a proposal to news editors who want more revenue from the journalism they already make, without another subscription, the evidence on micropayments and why it mostly failed, the meter that charges by how much of a page was read and runs in the reader's browser, free for any publisher, a revenue share when PrompTugal.news carries a newsroom's stories with their source, and the associations we should be talking to in the UK and Portugal](paid-by-the-read.md) A proposal to news editors: earn from the read, not the subscription, with free client-side code, a revenue share and the associations.
- [PrompTugal.news, the newsroom we ran at Web Summit: desks of agents that captured, mapped, wrote and reviewed 73 signed articles in ten days, an accountant that counted every run, and fifty outreach drafts that no agent was allowed to send](promptugal-news-the-newsroom-we-ran.md) PrompTugal.news: 73 signed articles in ten days from desks of agents, a reviewer for every draft, and fifty outreach drafts no agent could send.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 489 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=489)

**Posting this article on LinkedIn?** The cover is [a-page-we-never-charge.jpg](banners/a-page-we-never-charge.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/a-page-we-never-charge.html)*
