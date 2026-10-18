---
title: On the record: signed opinions from experts, paid when readers value them, and a share for the people whose ideas an article uses
date: 2026-10-18
author: Dinis Cruz
author_url: about/index.html
summary: Reviews on the record gave this site's articles a second reader. The next step is to let the people who know a subject go on the record about an article: I support this, I do not, and here is why, or use something else instead. Not a comments section, which many news sites have closed, but a professional opinion, signed with the person's own key and kept with the article, which they can later withdraw. The value is in the disagreement: an expert should not agree with everything, and sometimes the challenge is as interesting as the article, because that is where the facts get tested. Identity comes in levels, from an anonymous tap to a key bound to a domain and backed by a track record, and the pieces exist: Bluesky's domain handles, Mastodon's links back, did:web, signed commits. So does the precedent for paying for opinions: open peer review publishes signed reviews, and Biology Open, which pays reviewers £220, cut its time to a first decision from 37.7 to 5.5 working days. I think readers who rate an opinion as insightful should be able to pay for it, and the expert should get a share; and when an article that earns money is built from other people's ideas, they should get a share of that too. The research on signed comments is more mixed than people assume: real names did not make comments better in the largest study, stable identities did. So the case for signing is accountability and payment, not civility. This maps what exists here, what is missing, and what to build.
version: v0.12.107
license: https://creativecommons.org/licenses/by/4.0/
tags: newsroom, identity, public-keys, experts, payments, reviews, provenance, article
status: published
---

!shot or-levels.webp | images/ | Going on the record. Left, the levels of identity, from an anonymous tap to a key bound to a domain and a track record; each level allows more: a tap, a note, a review, an opinion that counts, and payment. Right, an opinion on the record: a position on the article, the reasons, the evidence, signed by its author's key, answered by the newsroom, rated by readers, paid from what readers pay, and withdrawable, with the withdrawal recorded. | concept

## In short {#in-short}

- **Not comments; opinions on the record.** A position on an article, with reasons, signed by the person who holds it.
- **Disagreement is the point.** An expert should not agree with everything; the challenge is where facts get tested.
- **Identity comes in levels.** From an anonymous tap to a key bound to a domain and a track record.
- **The pieces exist.** Domain handles, links back, did:web, signed commits; each proves less than people assume.
- **Science already publishes signed reviews, and some journals pay for them.** Biology Open pays £220 a review.
- **Readers should be able to pay for an opinion.** And the expert should get a share.
- **Ideas should get a share too.** If an article that earns money is built from someone's idea, they are paid.
- **Signing is for accountability and payment, not civility.** The research on real names is mixed.

## Not a comments section {#not-comments}

News sites have been closing comment sections for more than a decade. Reuters did it in 2014; NPR in 2016, when it counted about [19,400 active commenters](https://talkingpointsmemo.com/news/npr-ending-online-comments) against millions of readers on social media; the Press Democrat's group [on 4 September 2025](https://www.sonomanews.com/2025/08/28/press-democrat-news-group-comments-section-to-be-disabled-starting-sept-4). I understand why. A comments section asks anyone to say anything, and the people with the most to say are rarely the people with the most to add.

What I want is something else. In [reviews on the record](/articles/reviews-on-the-record.html), every article here gets reviewed against published criteria, by other models, by me and by the desk, and every review is a record kept with the article. The next step is to open that record to the people who know the subject: someone who has spent twenty years on supply-chain security, or who runs a newsroom, or who wrote the standard the article discusses. Not to comment, but to go on the record with a professional opinion.

## What going on the record means {#record}

An opinion on the record is short and structured:

- **A position.** I support this. I do not support this. I partly support it. Something else should be used instead.
- **The reasons**, in the expert's own words, and **the evidence**, linked.
- **Which text** of the article it is about, the same way a review is, so a later correction does not silently change what they agreed with.
- **A signature**, by the expert's own key, so that the record says who holds this opinion and nobody else can change it.

It is theirs to withdraw. An expert can change their mind, and the page then stops showing the opinion; the record keeps a signed note that there was one and that its author withdrew it, so nobody can claim later that it was never there, or that it still stands.

The part I care most about is that they should not agree. An expert who agrees with everything adds a name, not a view. The useful opinion comes from their own point of view: this is right for large companies and wrong for small ones; this was tried in 2019 and here is why it failed; this is the right idea with the wrong tool. Sometimes the challenge is as interesting as the article itself, because that is when everyone zooms in on the facts. The article can then change to reflect it, with the change on the record, or the challenge becomes a new article of its own.

## Identity, in levels {#levels}

Going on the record only means something if we know whose record it is. I think of identity here in levels, each allowing more:

1. **Anonymous.** A tap on a piece, through the append lane in [the editor's channel](/articles/the-editors-channel.html). Counts as a signal, never as an opinion.
2. **An account.** A reader with a passkey and a vault, which [this site already runs](/articles/the-passkey-opens-the-vault.html). The same person over time, but nobody knows who.
3. **A key pair.** The reader signs what they send with a private key only they hold. The design is in [RFC-0001](/articles/rfc-0001-public-key-cryptography-for-sgit.html); the inbox already seals messages to a reader's public key, and signing is the other half.
4. **A key bound to a name people know.** A domain they control, a public profile, a code repository.
5. **A key with a track record.** Opinions that turned out right or wrong over time, on the record, which is what [trust as a service](/economics/trust-as-a-service.html) calls calibrating weight by outcomes rather than by rank.

Level 4 is where the existing pieces are, and each proves less than people assume. Bluesky lets anyone use their own domain as their handle by adding a [DNS TXT record](https://bsky.social/about/blog/4-28-2023-domain-handle-tutorial), and said in April 2025 that more than [270,000 accounts](https://bsky.social/about/blog/04-21-2025-verification) had done so. Mastodon shows a green check when your website [links back to your profile](https://community.hachyderm.io/docs/mastodon/user/verification/). did:web resolves an identifier to a [document on your domain](https://github.com/w3c-ccg/did-method-web), and is still a community draft, not a W3C standard. GitHub marks signed commits as verified and now [keeps them verified](https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification) after a key is rotated. All of these prove that one key or account controls one domain or account. None of them proves who the person is; that comes from the domain being one people already associate with them, and from more than one proof agreeing.

And there is a warning in the history. Keybase did exactly this, signed proofs across accounts and domains, and [joined Zoom in May 2020](https://keybase.io/blog/keybase-joins-zoom) with "no specific plans for the Keybase app yet". An identity layer owned by one company lasts as long as that company wants it to. Here, the proofs should live where the person controls them: their domain, their key, their vault.

## Science already does this {#science}

Scientific publishing has been working on signed, public, sometimes paid reviews for years, and it is the closest precedent I know of.

- **Signed and public.** F1000Research [publishes reviewer names and full reports](https://f1000research.com/about) with the article, beside the authors' responses. eLife stopped making accept or reject decisions and publishes every reviewed paper with [public reviews and an assessment](https://elifesciences.org/inside-elife/66d43597/elife-s-new-model-one-year-on). PeerJ made the review history [mandatory from February 2023](https://peerj.com/benefits/review-history-and-peer-review/), and reviewers can choose to sign.
- **Paid.** Biology Open, from the Company of Biologists, pays reviewers £220 a manuscript; in its pilot, time to a first decision fell [from 37.7 to 5.5 working days](https://www.researchinformation.info/news/biology-open-paid-peer-review-model-cuts-times-to-five-working-days/) and the share of invitations accepted rose from 23% to 67%. The Unjournal pays evaluators [about $350](https://globalimpact.gitbook.io/the-unjournal-project-and-communication-space/readme-1/call-for-participants-research) and publishes the evaluations.
- **And the honest counterpoint.** Critical Care Medicine offered $250 a review in a trial: acceptance rose a little, reviews came about a day faster, editors saw [no difference in quality](https://peerreviewcongress.org/abstract/monetary-incentives-for-peer-review-at-a-medical-journal-a-quasi-randomized-experimental-study/), and the journal said it could not afford to continue. Paying makes reviews faster and more willing; it does not by itself make them better.

On the open web, X's Community Notes shows a note only when raters who usually disagree [both find it helpful](https://github.com/twitter/communitynotes/blob/main/documentation/under-the-hood/ranking-notes.md), which is a good idea for deciding what to show. Its note writers are not paid.

## Paying for an opinion {#paying}

The reading meter on this site already lets the reader decide what a page was worth: [pay after you read](/articles/pay-after-you-read.html), and the rating sets the price. The same mechanism works for an opinion. A reader who marks an expert's opinion as insightful, or as a good analysis, pays a little for it, and most of that goes to the expert.

That creates the incentive I want on both sides. The reader is paying for more of the analysis they value. The expert is paid to review properly, and only when readers find it worth paying for, which rewards a careful disagreement more than a quick agreement. I could not find a news platform that pays experts for opinions on its articles today; the nearest are Medium, which counts replies and highlights in what it [pays its authors](https://help.medium.com/hc/en-us/articles/360036691193), and the paid reviewers in science.

## A share for the idea {#share}

The same logic goes further. If an article here earns money, and a good part of it came from someone else's opinion, or from an idea three or four people put on the record, then they should get a share of what it earns. It is their idea we are writing about.

That used to be impossible to work out. It is less so when everything is on the record: the graph of an article names its sources and its claims, the opinions are signed records, and the release history says which change came from which finding. This site's page on [paying the fact creator](/economics/paying-the-fact-creator.html) argues that provenance is what makes the value behind a fact payable, and the AI industry is starting to agree, at the level of publishers: Perplexity's Comet Plus sends [80% of its revenue to publishers](https://www.axios.com/2025/08/26/perplexity-comet-plus-subscription), and ProRata's Gist splits [ad revenue 50/50](https://gist.ai/answers/) with the publishers whose content an answer used. What I am proposing is the same idea at the level of a person and an idea.

## Does signing make opinions better? {#evidence}

I assumed it would, and the research is more mixed than that.

- Santana's 2014 study of newspaper comment boards, as the University of Houston reported it, "found a [significant correlation between anonymity and civility](https://www.uh.edu/news-events/stories/2014/january/12114santana.xml)": anonymous comments were less civil.
- Rost, Stahel and Frey, looking at 532,197 comments on German petitions in 2016, found [non-anonymous commenters were more aggressive](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4912099/), not less.
- Moore and colleagues, across 45 million HuffPost comments, found the quality of argument [rose when stable, authenticated pseudonyms were required](https://journals.sagepub.com/doi/10.1177/0032321719891385) and fell after the switch to Facebook real names.
- South Korea's real-name law cut malicious comments only from 13.9% to about 13%, and its Constitutional Court [struck the law down](https://advox.globalvoices.org/2012/08/28/south-korea-internet-real-name-law-violates-the-constitution/) in 2012.

So I do not think the case for signing is that it makes people polite. It is that a signed opinion is accountable, it can be paid, and it builds a track record over time. And a stable key may matter more than a name: a key is a stable identity first, and a name is something it can be bound to, at level 4, when the person wants their name on it.

## What exists, and what to build {#build}

What this site already has: [reviews on the record](/articles/reviews-on-the-record.html), with a record format that already has a `reader` kind; the reader's passkey and vault; an inbox that seals messages to a reader's public key; the reading meter, with ratings and payment; and every article's text identified by a hash.

What it would take:

1. **A reader key pair**, made in the reader's browser, kept in their vault, used to sign what they send.
2. **A proof page**: the reader shows their public key on a domain they control, or in a DNS record, and the newsroom checks it and records the check.
3. **An opinion record**: the review record with a position, signed, and a signed withdrawal.
4. **On the page**: opinions beside the reviews, with the author's level, the position, the reasons and the newsroom's answer.
5. **Payment**: a rating on an opinion that moves money from the reader's balance to the expert, and a share of an article's revenue to the people whose recorded ideas it used.

## What this does not claim {#limits}

- **None of the opinion records, proofs or payments to experts is built.** The reviews, the passkey vault, the inbox and the meter are.
- **A domain proves control, not identity.** Level 4 is a name people already associate with a domain, and more than one proof agreeing.
- **Paying does not make opinions better.** In science it made reviews faster and more willing; quality is the job of the criteria and the readers.
- **Revenue shares for ideas are a proposal.** How to measure how much of an article came from whose idea is an open question.
- **The research on identity and civility is mixed,** and most of it is about comments, not expert opinions.
- **Some figures are the organisations' own.** Bluesky's count, Biology Open's pilot, Perplexity's and ProRata's shares.

If you are an expert and would like to be among the first to go on the record on an article here, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo from me on 18 October 2026. The research, read on 18 October 2026 by a research agent, with dates in the text: Bluesky on [domain handles](https://bsky.social/about/blog/4-28-2023-domain-handle-tutorial), 28 April 2023, and [verification](https://bsky.social/about/blog/04-21-2025-verification), 21 April 2025; Mastodon [verification](https://community.hachyderm.io/docs/mastodon/user/verification/); W3C CCG, [did:web](https://github.com/w3c-ccg/did-method-web); GitHub, [commit signature verification](https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification); Keybase, [joining Zoom](https://keybase.io/blog/keybase-joins-zoom), May 2020; F1000Research, [about](https://f1000research.com/about); eLife, [one year on](https://elifesciences.org/inside-elife/66d43597/elife-s-new-model-one-year-on); PeerJ, [review history](https://peerj.com/benefits/review-history-and-peer-review/); Research Information on [Biology Open](https://www.researchinformation.info/news/biology-open-paid-peer-review-model-cuts-times-to-five-working-days/); The Unjournal, [call for participants](https://globalimpact.gitbook.io/the-unjournal-project-and-communication-space/readme-1/call-for-participants-research); Peer Review Congress, [monetary incentives](https://peerreviewcongress.org/abstract/monetary-incentives-for-peer-review-at-a-medical-journal-a-quasi-randomized-experimental-study/); X, [Community Notes ranking](https://github.com/twitter/communitynotes/blob/main/documentation/under-the-hood/ranking-notes.md); Medium, [Partner Program](https://help.medium.com/hc/en-us/articles/360036691193); Axios on [Comet Plus](https://www.axios.com/2025/08/26/perplexity-comet-plus-subscription), 26 August 2025; Gist, [Answers](https://gist.ai/answers/); Talking Points Memo on [NPR](https://talkingpointsmemo.com/news/npr-ending-online-comments), 2016; Sonoma News on [the Press Democrat](https://www.sonomanews.com/2025/08/28/press-democrat-news-group-comments-section-to-be-disabled-starting-sept-4); University of Houston on [Santana](https://www.uh.edu/news-events/stories/2014/january/12114santana.xml); Rost, Stahel and Frey, [PLOS ONE](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4912099/), 2016; Moore and others, [Political Studies](https://journals.sagepub.com/doi/10.1177/0032321719891385); Global Voices on [South Korea's real-name law](https://advox.globalvoices.org/2012/08/28/south-korea-internet-real-name-law-violates-the-constitution/), 2012. Related: [reviews on the record](/articles/reviews-on-the-record.html), [the editor's channel](/articles/the-editors-channel.html), [RFC-0001](/articles/rfc-0001-public-key-cryptography-for-sgit.html), [pay after you read](/articles/pay-after-you-read.html), [paying the fact creator](/economics/paying-the-fact-creator.html), [trust as a service](/economics/trust-as-a-service.html). Written up and checked by this site's agent; the editorial responsibility is mine.
