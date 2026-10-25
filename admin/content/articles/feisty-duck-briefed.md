---
title: Feisty Duck, briefed: Ivan Ristić's cryptography and security news, newsletter, guide and history as an anchor for everything SSL, TLS and PKI, what it shares with our newsrooms, and how we could integrate with it
date: 2026-10-25
author: Dinis Cruz
author_url: about/index.html
summary: Feisty Duck, the small London publisher run by Jelena and Ivan Ristić since 2009, is one of the sources I trust most for anything to do with SSL, TLS, PKI and applied cryptography. Ivan wrote SSL Labs and Bulletproof TLS and PKI, and the Cryptography & Security Newsletter goes to more than 50,000 subscribers. In August it launched Feisty Duck News: it monitors 37 sources, from Adam Langley and Filippo Valsorda to Let's Encrypt and the IETF, takes reader submissions, summarises each article with an LLM, and promotes items to the front page by hand. Its feed held 100 items from 1 September to 25 October, a quarter of them on post-quantum cryptography. The rest of the site is just as useful: a free Bulletproof TLS Guide, updated in June, and an SSL/TLS and PKI history of 174 events, from SSL v2 in 1994 to 47-day certificates in 2029. Feisty Duck has believed in continuous publishing since 2009, which is what we do with versioned articles. This is a brief on what it is, a debrief against what we are building, and integration ideas: an anchor for our crypto claims, a crypto and TLS wire, provenance for the LLM summaries, and the history as a graph. A vault of its content would need its permission: its terms reserve reproduction, and its robots.txt asks crawlers to stay out of the news section.
version: v0.13.86
license: https://creativecommons.org/licenses/by/4.0/
tags: tls, pki, cryptography, sources, anchors, integrations, briefing, article
status: published
---

!shot fd-pages.webp | images/ | Feisty Duck on 25 October 2026: Feisty Duck News, the live front page of cryptography and security news; the Cryptography & Security Newsletter, with issues to #141, "Get Ready for Seven-Day Certificates"; the SSL/TLS and PKI History, starting with SSL v2 in 1994; and the free Bulletproof TLS Guide, last updated on 16 June 2026. | screenshot

## In short {#in-short}

- **Feisty Duck is an anchor for SSL, TLS, PKI and applied cryptography.** Expert, curated, kept up to date.
- **Feisty Duck News, since August.** 37 monitored sources, LLM summaries, a front page chosen by hand.
- **The rest of the site matters as much.** A newsletter, a free guide, a 174-event history.
- **Continuous publishing since 2009.** The same idea as our versioned articles.
- **Integration:** anchor our crypto claims, run a crypto and TLS wire, check the summaries, graph the history.
- **A vault of their content needs their permission.** A vault of our own notes does not.

## Brief: what Feisty Duck is {#brief}

[Feisty Duck](https://www.feistyduck.com/about/) describes itself as "a small business focused on providing top-notch computer security education", run by Jelena and Ivan Ristić from London, and founded in 2009 "out of a desire to support continuous publishing, which we believe is the best way to publish technical books." Its flagship book, [Bulletproof TLS and PKI](https://www.feistyduck.com/books/bulletproof-tls-and-pki/), was first published in 2014 and, in its own words, "continues to be up to date today". Ivan Ristić is also the author of SSL Labs, and in 2018 started Hardenize, a platform for monitoring internet assets against TLS and PKI best practice. Training followed in 2016; the site says more than 3,000 students have taken it.

For me, it is one of the places whose content can be taken with a high degree of certainty and quality. When Feisty Duck explains how TLS 1.3 works, or what changes as certificate lifetimes shrink, it is written by someone who has spent many years on exactly that.

## Feisty Duck News {#news}

!shot fd-numbers.webp | images/ | Feisty Duck, in numbers: the 100 items in the news feed between 1 September and 25 October 2026, by category, led by post-quantum cryptography (24), PKI (21), cryptography (18) and security (17); and the 174 events in the SSL/TLS and PKI history, by decade, 109 of them in the 2010s, scored 115 positive and 56 negative. | chart

[Feisty Duck News](https://www.feistyduck.com/news/) launched with the newsletter's issue #140, on 27 August 2026. Its [about page](https://www.feistyduck.com/news/about) is short and honest: "There's so much happening in cybersecurity that it's difficult to keep up, and so we built this tool to help us curate our newsletter." How it works:

- **Monitored sources.** "We automatically monitor a wide range of sources": a [published list](https://www.feistyduck.com/news/sources) of 37, including Adam Langley, Filippo Valsorda, Matthew Green, Eric Rescorla, Sophie Schmieg, the Cloudflare, Let's Encrypt, IETF, APNIC and Trail of Bits blogs, the PKI Consortium, and some LinkedIn accounts.
- **Submissions.** "Our users manually submit links they care about."
- **Summaries.** "We use an LLM to summarise and categorise each article."
- **Promotion.** "Some articles are promoted to the front page", by hand for now.

Its feed held 100 items between 1 September and 25 October 2026: post-quantum cryptography 24, PKI 21, cryptography 18, security 17, privacy and society 12, AI 5. On 25 October the front page had the hijacked Tor exit relays, Bitcoin's post-quantum readiness, CRL caching in Microsoft Edge, OpenSSL 4.1.0, and Quad9 leaving France. None of it was about php2shell, which makes sense: a memory corruption in PHP is not a cryptography story.

## The rest of the site {#site}

The news is the newest part. The rest of the site has more good anchors:

- **The [Cryptography & Security Newsletter](https://www.feistyduck.com/newsletter/),** "enjoyed every month by more than 50,000 subscribers", with recent issues on seven-day certificates (#141), the state of post-quantum cryptography (#139), ECH (#136) and Merkle tree certificates (#135).
- **The [Bulletproof TLS Guide](https://www.feistyduck.com/library/bulletproof-tls-guide/),** free to read online, last updated on 16 June 2026.
- **The [SSL/TLS and PKI History](https://www.feistyduck.com/ssl-tls-and-pki-history/),** "a comprehensive history of the most important events that shaped the SSL/TLS and PKI ecosystem", last updated in August 2026: 174 events, each with a date and an impact score, from SSL v2 in November 1994 to certificate lifetimes of 47 days in March 2029. Nine are dated 2026 or later.
- **The books,** each with a last-update date, and the training.

## Debrief: what we share {#debrief}

Reading it against what we are building, there is a lot of overlap.

- **Continuous publishing.** Feisty Duck has done it with books since 2009. We do it with articles: every article here has a version, and every release a note.
- **A curation pipeline.** Monitored sources, submissions, LLM summaries and a person deciding what is promoted. On [the PHP story site](https://php.oct.2026.newsroom.sgit.ai/), collectors and a researcher gather sources, a curator turns them into evidence, and the editor decides.
- **A source list in public.** Feisty Duck publishes the 37 sources it monitors. The PHP site publishes the [913 pages its source watch](https://php.oct.2026.newsroom.sgit.ai/vaults/source-watch/index.html) re-reads.
- **History as structure.** The SSL/TLS history is data, events with dates and impact. Our stories are kept as graphs.

And the same caution applies to both. Feisty Duck's summaries are written by an LLM, as [Monstream's are](https://newsroom.sgit.ai/articles/monstream-briefing.html). The curation is expert; the summary of each item is still a summary. What makes an anchor useful is being able to go from the summary to the original, quickly, and know it has not changed.

## How we could integrate {#integrate}

!shot fd-flow.webp | images/ | How Feisty Duck and our newsrooms could fit together: Feisty Duck curates and explains; we link our crypto, TLS and PKI claims to its guide, book and newsletter as an anchor, now; we could run a crypto and TLS wire that follows the same public sources and credits Feisty Duck News; we could add provenance to the LLM summaries of items we cite; and, with permission, keep the history as a graph and capture pages in a vault. | process

- **An anchor, now.** Our articles make claims about cryptography all the time: AES-256-GCM and PBKDF2 in sgit, passkeys on pki.sgit.ai, signatures in [signed by the source](https://newsroom.sgit.ai/articles/signed-by-the-source.html). Those claims should link to the guide, the book's chapters and the newsletter, the way the PHP site uses [Wikipedia as an anchor](https://php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-25__brief__wikipedia-as-an-anchor/index.html) for php2shell. The CSP discussion in [a secure rule, applied literally](https://newsroom.sgit.ai/articles/a-secure-rule-applied-literally.html) belongs next to the book's chapter on HSTS, CSP and pinning.
- **A crypto and TLS wire.** Our [Industry Wire](https://newsroom.sgit.ai/wire/index.html) has three wires, AWS, OWASP and Portugal. A fourth could follow the same public sources Feisty Duck lists, and credit and link to Feisty Duck News for what it found first.
- **Provenance on the summaries.** For each item we cite, our researcher captures the original, hashes it, checks the LLM summary against it, and records the verdict. That is the layer Feisty Duck's pipeline does not have yet, and the one ours is built for.
- **The history as a graph.** Those 174 events, with impact scores, are already structured. As a versioned graph, linked to their sources and to our stories, they would let a reader ask what changed in the Web PKI in any year, and why.
- **What is coming, for us too.** Issue #141 is about seven-day certificates, and the history's own data has public certificate lifetimes falling to 47 days by 2029. Our sites run on those certificates too; it is a good test of whether our own stack keeps up.

## Is there a need for a vault? {#vault}

Yes, and it needs to be done right. A vault would keep our links to Feisty Duck items, the dates we read them, our notes, and our verdicts on the summaries we checked, encrypted and versioned. That part is ours, and we can build it now.

Captures of Feisty Duck's own pages are different. Its [terms of use](https://www.feistyduck.com/about/website_terms_of_use) say no part of the site may be reproduced or stored "except in accordance with separately agreed permissions", and its robots.txt disallows `/news/` for every crawler. The feed is published for readers to follow; a crawler that copies the news section into our vault is not what Feisty Duck has asked for. So capturing their pages, and turning the history into our graph, waits for their permission. That is the rule we set ourselves in [sources and their shadows](https://newsroom.sgit.ai/articles/sources-and-shadows.html): record each source's licence and access, and respect them.

## What this does not claim {#limits}

- **The counts are from the public feed, the source list and the history's data,** read on 25 October 2026, and will change.
- **The integrations are proposals.** Nothing has been built, and nothing captured beyond reading the pages.
- **The quality judgement is mine,** from years of reading Feisty Duck's work.

## Where this comes from {#sources}

Feisty Duck's [about page](https://www.feistyduck.com/about/), [news](https://www.feistyduck.com/news/) with its [about](https://www.feistyduck.com/news/about) and [sources](https://www.feistyduck.com/news/sources) pages and its RSS feed, the [newsletter](https://www.feistyduck.com/newsletter/), the [Bulletproof TLS Guide](https://www.feistyduck.com/library/bulletproof-tls-guide/), the [SSL/TLS and PKI History](https://www.feistyduck.com/ssl-tls-and-pki-history/) and its data, the [book page](https://www.feistyduck.com/books/bulletproof-tls-and-pki/), the [terms of use](https://www.feistyduck.com/about/website_terms_of_use) and robots.txt, all read on 25 October 2026; my voice memo of the same day. Related: [Monstream, briefed](https://newsroom.sgit.ai/articles/monstream-briefing.html), [sources and their shadows](https://newsroom.sgit.ai/articles/sources-and-shadows.html), [who creates the original?](https://newsroom.sgit.ai/articles/who-creates-the-original.html), [a secure rule, applied literally](https://newsroom.sgit.ai/articles/a-secure-rule-applied-literally.html), [signed by the source](https://newsroom.sgit.ai/articles/signed-by-the-source.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
