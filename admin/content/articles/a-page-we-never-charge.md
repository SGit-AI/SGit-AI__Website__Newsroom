---
title: A page we never charge: how the PrompTugal agents found that YouTube's terms forbid charging to watch an embedded player, on the one site of ours that bills, put the conflict to me as a question, quoted the six conditions from YouTube's own policies once I suggested a page that is never charged, and built the gate that refuses a YouTube player on any page that is, in 84 minutes of commits
date: 2026-11-19
author: Dinis Cruz
author_url: about/index.html
summary: Just after midnight on 19 November the PrompTugal agents had a working YouTube key and a feed of Web Summit's official replays, and a problem. YouTube's developer policies say "API Clients must not charge users to watch content in an embedded YouTube player", and promptugal.news is the one site of ours that bills its readers. The licensing agent put YouTube's terms on its register as unclear; the conductor brought the question to me rather than fixing it. My answer was to put the videos on a page that is never charged, because our billing is per page, not per site. Within six minutes the licensing agent had quoted YouTube's own policies and set six conditions; the designer drew the page within them, the journalist wrote its explanation, and the developer built a flag for free pages and a gate that refuses a YouTube player on any page that is charged. From the first finding to the gate: 84 minutes of commits. The page itself is not live yet; it waits for the licensing agent to check it against the six conditions.
version: v0.14.164
license: https://creativecommons.org/licenses/by/4.0/
tags: promptugal, youtube, terms, licensing, billing, agents, article
status: published
---

!shot fyt-mock.webp | images/ | designer@'s mock-up of the free replays page: "Free to watch", YouTube's own player, the credit and the Terms link. | screenshot | medium

## In short {#in-short}

- **The clause:** YouTube's policies say "API Clients must not charge users to watch content in an embedded YouTube player".
- **The clash:** promptugal.news is the one site of ours that bills its readers.
- **The question came to me,** not a fix; the idea and the decision were mine.
- **The answer:** a page that is never charged, because the billing is per page, not per site.
- **Six conditions,** quoted from YouTube's own pages, then a design, a text, a flag and a gate.
- **84 minutes** from the first finding to the gate; the page waits on one last check.

## The clause {#clause}

Around midnight on 18 November I set up a Google Cloud project with a key for five APIs, YouTube's Data API among them, and the PrompTugal team had a feed of Web Summit's official replays from the organiser's own channel. The obvious next step was to show the videos on promptugal.news.

The team has a licensing agent, rights@, started that evening, whose job is to read the terms of every source before anything from it is shown. At 00:19 UTC it put YouTube's API terms on its register as finding R6 and marked commercial use "unclear". The reason is one sentence in YouTube's Developer Policies, under Playback Integrity: "API Clients must not charge users to watch content in an embedded YouTube player." And promptugal.news is the one site of ours that bills its readers: its meter charges by how much of a page was read ([paid by the read](/articles/paid-by-the-read.html)).

## A question, not a fix {#question}

The conductor, conductor.b@, did not choose for me. It could have dropped the videos, or put them on one of our free sites, or decided that a page with a meter was fine if the player itself was free. Its commit at 00:50 is the question, put to me.

My answer, at about 01:05, recorded in the team's guidance: "what about putting them in a page that is not charged, which actually is a really powerful case study and example of the power of our custom billing model, since we can be compliant with that requirement by using an IFrame for Google and not charging for that page right?"

That is the point of billing per page. A site that charges for some pages can choose not to charge for others, and can do it where another party's terms say it must not.

## Six conditions {#conditions}

At 01:11 rights@ committed YouTube's Developer Policies and Required Minimum Functionality, quoted from the source, and a conditional go with six conditions for the page:

- **C1, never charged or gated:** no paywall, sign-in or meter between the reader and the play button.
- **C2, no advertising or sponsorship** sold on or around the player.
- **C3, YouTube's own iframe player,** at least the size YouTube sets ("Embedded players must have a viewport that is at least 200px by 200px"), with nothing over it: "You must not display overlays, frames, or other visual elements in front of any part of a YouTube embedded player".
- **C4, YouTube credited** and its Terms of Service linked beside the player.
- **C5, nothing from the API kept** longer than the 30 calendar days the policies allow.
- **C6, not counted as a read,** so the reading log and the simulated payments to sources never include it.

No agent accepted YouTube's terms on my behalf; the register says so in its first line, and that decision stays mine.

!shot fyt-time.webp | images/ | The commits from rights@'s first finding at 00:19 to dev@'s gate at 01:43 UTC on 19 November. | chart

## The build {#build}

Each step answered the one before it. At 01:16 the journalist agent drafted the page's own explanation of why it is free. At 01:20 designer@ committed a specification and mock-ups at desktop and phone widths, light and dark: a green "Free to watch" note above the title, YouTube's player from youtube-nocookie.com, a text credit and the Terms link under each player, no logo until the branding guidelines were read. At 01:26 rights@ quoted YouTube's branding guidelines and said the design was a go. At 01:43 dev@ built the flag: a page marked free loads no meter, so it is never charged, never in a reading log and never in the simulated payments. The site's build gate now refuses three things: a YouTube player on a page that is not free, a free page that still loads the meter, and a player from youtube.com instead of youtube-nocookie.com.

## What it shows {#shows}

- **Billing per page, not per site.** The rule that limits us is YouTube's; the page that obeys it is ours to make.
- **Terms read before anything is shown.** The clause was found before a single video was on a page, and quoted from YouTube's own text.
- **Agents found it; a person decided.** The agents found the conflict and the exact clause; the idea and the decision were mine.
- **A trail you can follow.** Every step is a commit or a board file in a public repository.

## What this does not claim {#limits}

- **The page is not live yet.** It waits for rights@ to check the built page against C1 to C6.
- **The times are commit times** in the repository; the agents' own notes sometimes give times a few minutes later, as their clocks ran ahead.
- **Nothing here is legal advice,** and nothing is claimed about YouTube beyond its published text.

## Where this comes from {#sources}

[PrompTugal__News__Website](https://github.com/PrompTugal/PrompTugal__News__Website) on its dev branch, read on 19 November 2026: `board/team/rights/findings.md` (R6), `board/team/rights/register/google-apis.md`, `board/guidance/2026-11-19-signed-commits-paid-search-and-free-embeds.md` (section 3), `board/spec-the-free-replays-page.md`, `board/team/dev/note-2026-11-19-free-pages.md`, `newsroom/build/features/free-pages.mjs` and the mock-ups in `design/decisions/free-replays/`. YouTube's [Developer Policies](https://developers.google.com/youtube/terms/developer-policies) and [Required Minimum Functionality](https://developers.google.com/youtube/terms/required-minimum-functionality), read on 19 November 2026. Earlier: [paid by the read](/articles/paid-by-the-read.html), [PrompTugal.news, the newsroom we ran at Web Summit](/articles/promptugal-news-the-newsroom-we-ran.html).
