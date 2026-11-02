---
title: Sellable units: applying api.newsroom.sgit.ai to my brother's website, the reading meter on a composer's site that does not look like a newsroom, the pathways from a viewer to a buyer, and every lesson, score and master as something to sell
date: 2026-11-02
author: Dinis Cruz
author_url: about/index.html
summary: I showed my brother Gabriel the newsroom, including topping up my own reading credit, and his first question was the right one: his site should not look like a newsroom. It will not. What the newsroom's technology adds is not a look but a way to be paid: every reader starts with £5 of credit, each page uses a few pence by how much was read, a rating sets the price from nothing to double, the balance can go below zero, and a top-up through Stripe comes when the value is clear. All of it is published as an open API, api.newsroom.sgit.ai, that any page can add with a few lines. On a composer's site that looks like a composer's site, every page becomes a sellable unit: a lesson's materials, a score he owns, an analysis of what makes a song work, a how-to, a video explained, the WAVs of a piece like Amazónia. His readers are other musicians, producers and students, a demanding audience and a large one. The habit that makes it work is to create sellable units every day, at the moment of creation, and let an agent publish them. And for the works that should travel, Creative Commons Attribution with a paid licence alongside, with one honest correction: once a work is under CC BY, a buyer can get a licence on other terms, but not exclusivity.
version: v0.14.32
license: https://creativecommons.org/licenses/by/4.0/
tags: monetisation, meter, music, creators, creative-commons, licensing, newsroom-api, sellable-units, article
status: published
---

!shot sel-units.webp | images/ | Sellable units: lessons, scores, analyses and masters as pages on his own site, each with the newsroom's meter. | architecture

## In short {#in-short}

- **His site will not look like a newsroom;** it will look like a composer's site, with the newsroom's way to be paid.
- **The meter is already built:** £5 of starting credit, a few pence a page, a balance that can go negative, Stripe top-ups.
- **It is an open API,** api.newsroom.sgit.ai, that a page adds with a few lines.
- **Every page becomes a sellable unit:** a lesson, a score, an analysis, a how-to, a video explained, a master.
- **His market is musicians, producers and students:** demanding, and large.
- **The pathways:** found on a platform, a page on his site, more pages, a top-up, then a score, a master, a licence, a lesson.
- **The habit is the product:** create sellable units every day, and let an agent publish them.
- **For works that should travel:** CC BY plus a paid licence; a buyer gets other terms, not exclusivity.

## "It should not look like a newsroom" {#look}

I showed Gabriel the newsroom, including the payment: I topped up my own reading credit while he watched, and it worked. His question: yes, but his site should not look like a newsroom.

He is right, and it will not. Look at a film composer's official site, Alan Silvestri's for example: a biography, a filmography, a discography, clips, awards, news and a media gallery. That is the shape Gabriel's site should have, with photos, videos, scores and articles, built from [the starter kit his Claude will run](/articles/a-website-for-my-brother.html). What the newsroom adds is not a look. It is a meter.

## What the meter does {#meter}

It is running on this site today, and [the reading account, as built](/articles/the-reading-account-as-built.html) says exactly what is live:

- **Every reader starts with £5 of credit,** in their own browser, with no account.
- **Each page uses a few pence,** charged by how much of it was read, and a rating at the foot sets the price from nothing to double.
- **The balance can go below zero** and stay there. I explained why in [paying after the value](/articles/paying-after-the-value.html): by the time you are asked to pay, you already know what you got. One reader was unsure about paying at first; once the value was clear, they topped up.
- **A top-up is £5 through Stripe,** live since 11 October.

All of it is published as an open API, api.newsroom.sgit.ai, Apache 2.0: pinned, versioned files on one host, a small configuration file and a custom element, `<sg-meter>`, that a page adds in a few lines. The reader's state stays in the reader's browser, on Gabriel's domain.

## How it plugs into his site {#plug}

The API's own guide, add the meter, describes it as "ten lines on each page, one config written by your build, and five account pages you copy. Nothing to deploy but files." On Gabriel's site, which his agent builds from markdown, that means:

1. **One element at the foot of every page that should earn,** after the last paragraph a reader would reach:

    ```
    <sg-meter view="page" kind="article" date="2026-11-02" topics="arranging synths" title="Separate Ways, explained"></sg-meter>
    ```

   The kind is the price class: article, note, issue, collection, page, or free. A score could be a collection, a quick studio tip a note, a lesson's materials an article, and the biography and contact pages free.
2. **The balance chip in his navigation,** so a reader always sees their credit.
3. **One config,** written by his build, with his prices and his site's details.
4. **The account pages,** copied as they are: the history, the top-up, the reader's vault.

The meter, the credit, the history and the Stripe top-up come with it. His design stays his: the element draws a small card at the foot of the page, and the rest is his site. Two more features of the API fit him well:

- **Reading-list links.** A list is a link: the articles to read, in order, with a note, and no account. After a lesson, he sends the student a link to the five pages that matter, from him to them. That is a syllabus, and every page on it earns.
- **Personas.** The newsroom opens as a founder, a journalist, a builder; his site could open as a composer, a producer, a student or a fan, each with its own starting list. That needs his own set of personas, which is a small piece of work, not a feature already there.

## Pathways {#pathways}

!shot sel-pathways.webp | images/ | The pathways: found on a platform, a page on his site, more pages, a top-up, then a purchase. | process

Money comes from a path, not a page. Someone finds a reel, a Short, a Spotify track, or searches for how to sync four iPhones. Every one of those [projections](/articles/a-website-for-my-brother.html) links to a page on his site, where the meter charges a few pence from the starting credit. They go deeper: related works, the series, a reading list. When the balance goes below zero, the value is already clear, and they top up. And some of them buy more: a score, the masters, a licence, a lesson, a commission. The meter covers the pages and the top-ups today; the larger purchases need a payment link of their own on the same pages, which Stripe already provides for the top-up.

## Sellable units {#units}

This is the principle I care most about. The site has to be set up so that Gabriel creates sellable units, every day: pieces of value a reader can pay a few pence for.

- **Lessons.** Every lesson he gives produces materials: what was covered, the exercises, the recording. The student goes home with a personalised record, and the materials become a page. I do the same: when someone needs an idea I explained a month ago, I send them the article.
- **Scores.** He arranges and composes, and he owns the sheet music: a page per score, with the PDF, the story and a recording.
- **Analyses.** What makes a song special, the way Rick Beato built an audience on YouTube by explaining one song at a time; his channel has millions of subscribers, and he sells courses alongside it.
- **How-tos.** The gear and the trick, like the [three old iPhones synced to an iPad](/articles/four-iphones-and-an-ipad.html).
- **Video breakdowns,** like [Separate Ways, explained](/articles/separate-ways-explained.html).
- **Masters.** The WAVs and stems of a piece like Amazónia, which already has a little traction, delivered as a download or from a vault.

Each one is another page that can earn a few pence, and another door for someone who finds one piece they like and wants to go deeper. A couple of them catching on brings traffic to all the others. You only get there by publishing a lot.

## His market {#market}

Gabriel's readers are other composers, musicians, producers and students: a more advanced reader, and there are a lot of them. Some visitors will never pay, and that is fine; they are not the market. The market is the student who learns a lot and thinks it is the best five pounds they have spent, and the producer who sees how he works and hires him.

Two ideas to try. His own students could start with more credit, as a gift, so they learn that the work has a price and he learns what they read. And fans of an artist might enjoy paying: being among the people who support the work is part of the connection, and an artist can publish material only those fans would want.

## Licences: CC BY, with a paid licence alongside {#licences}

For the works that should travel, my recommendation is to release many of them under Creative Commons Attribution (CC BY 4.0). Anyone can then use a piece in a video, a short film or a game, as long as they credit him, and every use is a link back to him. A song that nobody can use goes nowhere.

Alongside it, he sells a paid licence. Creative Commons says so directly: "All CC licenses are non-exclusive", and the licensor "may also offer the Licensed Material under separate terms". A company may want to use a piece without the credit, or want a signed licence with warranties, or the masters and stems; those are things CC BY does not give, and he sets the price.

One correction to what I told him in the conversation. Under CC BY, a buyer gets a licence on different terms; they do not come to own the song. CC licences "are not revocable once granted", so once a work is out under CC BY, nobody can be sold exclusivity over it. For a piece he might want to sell exclusively one day, he keeps it out of CC BY.

And one thing to check first: if he is a member of SPA, the Portuguese authors' society, its by-laws limit what members may license themselves; I found no SPA statement on Creative Commons, so he should ask them in writing before releasing anything under CC BY.

## More ideas {#ideas}

- **A page per work, with three prices:** read it (the meter), use it (CC BY, free with credit), or license it (a paid licence, with the masters).
- **Score previews:** the first page of a score as a free image, the full PDF as a paid download.
- **A series:** the Separate Ways video, the synth it copies, the Bluetooth keyboard, the multicam setup: four pages, one reading list.
- **Lesson bundles:** the materials of a course as a collection, with credit included in the lesson's price.
- **Commissions:** a page that shows what he can write, for whom, and what it costs, with a form his agent triages.
- **Requests:** readers asking for a score in a style, an analysis of a song; his agent counts them, and he writes what is asked for most.
- **Behind the scenes for patrons:** his Patreon keeps the early previews; the site keeps the finished, paid pages.

## The habit {#habit}

The commercial model is simple: you earn as soon as you have traffic, and you get traffic by publishing a lot. So the workflow is the product. Every time he does something interesting, finds a new nugget, gives a lesson or figures something out, he describes it, and his agents publish it: one more sellable unit. Then he learns what gets traction, does more of it, and learns how to price it. Gabriel's idea of a good night is composing and writing music for fun. Now that work can be published, and it can earn.

## What this does not claim {#limits}

- **The meter is live on this newsroom,** not yet on his site; adding it is part of his starter kit's next step.
- **Nobody knows yet what his pages will earn;** the numbers will come from his traffic.
- **The licensing notes are not legal advice;** the Creative Commons quotes are from its own pages, and the SPA question needs SPA's answer.
- **The students' credit, the fans' club, his own personas and the larger purchases are proposals,** not features of the API today.

## Where this comes from {#sources}

The conversation with Gabriel of 2 November 2026. [api.newsroom.sgit.ai](https://api.newsroom.sgit.ai/); [Creative Commons FAQ](https://creativecommons.org/faq/) and [CC BY 4.0 legal code](https://creativecommons.org/licenses/by/4.0/legalcode.en); [SPA's by-laws](https://www.spautores.pt/wp-content/uploads/2022/03/Estatutos_SPA_Ingles_cf-alteracao-2018.pdf); [Alan Silvestri's site](https://www.alansilvestri.com/); [Rick Beato on YouTube](https://www.youtube.com/@RickBeato). All read 2 November 2026.
