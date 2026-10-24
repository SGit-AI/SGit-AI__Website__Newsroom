---
title: A newsroom for one: the reading list I send by email became the first page of this newsroom for the people I write to, so it now says what it is, shows what they have read, and asks for an answer
date: 2026-10-24
author: Dinis Cruz
author_url: about/index.html
summary: The reading list has become one of the most useful things this newsroom does for me. On 11 October I asked for a way to send someone a link that says: from me, for you, these are the articles I think you should read, in this order, and here is why. It shipped the same day. Since then the agent behind agent@riskmandate.ai has been building these lists into the emails it drafts for me, about twenty of them by its debrief of 18 October, and I read and send every one. What I had not thought through was that for most of the people I send one to, the list is the first page of this newsroom they ever open. They arrive from an email, often through a link their mail client has wrapped, and until this week they found a narrow column of titles that did not say what the site was, what a price of a few pence meant, or what to do next. So on 21 October the page changed. It now opens as a letter: a dateline, my note signed, and one line on what the list holds and what it costs. It uses the width of the screen, with the articles as cards whose pictures can be read, four more views (headlines, sections, pictures, and the list as a graph), and a column that explains the newsroom in four steps. And it shows the reader what they have read, section by section, from their own browser, with done, later and not for me on every article. Before it shipped, the newsroom's Designer role reviewed it on a real list and fourteen of its findings were fixed. This is the second page this week that had to be brought up to date because people started to use it, after the page for publishers, and it points at the next step: the answers coming back to me, and to the agent, as easily as the lists go out.
version: v0.13.63
license: https://creativecommons.org/licenses/by/4.0/
tags: reading-lists, personas, email, riskmandate, agents, design, newsroom, the-newsroom, publishing-method, article
status: published
---

!shot nf-list.webp | images/ | A reading list from me to Steve, the site's own example, as it opens since 21 October, at 1440 pixels wide in the Newsprint theme, after one article was read and half of another. At the top, a dateline and my note, signed; a ring at 32% with one of seven read and 55 minutes left; the first article as a card, its section bar full, marked Read; and on the right, what the page is, in four steps, and the list as a persona. | screenshot

## In short {#in-short}

- **A reading list is a link from me to one person.** The articles to read in order, a few worth a look, what to follow and a line from me, all in the part of the address after the #, which the browser never sends to the server. It shipped on 11 October, the day I asked for it.
- **The agent behind agent@riskmandate.ai builds them into my emails.** It picks the articles by number, writes the line on why, builds the link and opens it on the live site to check it; I read the draft and send it. About twenty by its debrief of 18 October.
- **For most people, the list is the first page of the newsroom they see.** They arrive from an email, not from the front page, so the list has to say what the site is and what to do.
- **The first version was a column of links.** It worked, and it did not explain anything: not the price of a few pence, not the free credit, not that nothing about their reading reaches me.
- **Since 21 October it opens as a letter, and uses the screen.** A dateline, my note signed, one line on what the list holds and costs; the articles as cards with pictures that can be read; a side column that explains the newsroom in four steps.
- **It shows the reader what they have read.** Section by section, from their own browser's records, with a ring, the time left and what it has cost, and done, later and not for me on every article. Nothing of it is sent anywhere.
- **Five views of the same list.** Cards, headlines, sections as one line each, the articles' pictures, and the list as a graph of its ideas and the links between them.
- **The Designer reviewed it before it shipped.** Fourteen findings on a real list at desktop and phone widths, all fixed in the same release.
- **Pages that people use have to keep up.** The page for publishers was the first, a week ago; the reading list is the second. The next step is the answers: notes from the page that reach me, and the agent, signed, as easily as the lists go out.

## A link from me to one person {#link}

I keep meeting people I would like to point at three or four articles: a founder I mentor, a publisher, someone shaping a roundtable, a security lead with a specific problem. The newsroom's curation is close, [the personas and the desks](/articles/a-link-to-a-persona.html) get most of the way, but it is not personal, and the last part is the part that starts a conversation. So on 11 October I asked for [a reading list in a link](/articles/a-reading-list-in-a-link.html): from Dinis, for Steve, here are the articles I think you should read, the ones worth a look, and what to follow.

It shipped the same day, as release v0.8.0 of this site. Every article has a number that never changes, so a list is a handful of numbers, two first names and a note, after the # in the address. A browser keeps that part to itself, so the newsroom never sees who sent a list to whom, and there is no account and nothing to sign up for. When the link opens, the list becomes one of the reader's personas in their browser, which they can keep or remove, and the newsroom's picks follow it.

## The agent builds them into my emails {#agent}

What made the reading list useful was not the page. It was that I stopped building the links myself. The agent behind agent@riskmandate.ai, which [drafts my email and waits for me to send it](/articles/answering-a-draft.html), now does it as part of a reply: it reads the thread, picks the articles by number, writes a line on why for each, builds the link, opens it on the live site to check that every article is there and in order, and puts it in the draft. Its debrief of 18 October counts about 20 reading lists among the 178 emails it had drafted, each written for one person. Every one waited in my drafts folder until I read it, changed it and sent it.

!shot nf-flow.webp | images/ | How a reading list goes out and what comes back. The agent reads the thread, picks the articles, builds and tests the link; I read the draft and send it. The person opens the list, reads at their own pace, marks articles and replies; the answer or the next list is drafted for me to read. What they read or skip stays in their browser and their own vault: the newsroom, the agent and I see a reply only if they write one. | diagram

That is [the man behind the curtain](/articles/the-man-behind-the-curtain.html) again, in a small form. The agent does the work of choosing and checking; the email is from me, because I read it and send it; and behind the email there is not one article but a short course, in an order I chose for that person.

## The first page they see {#first}

What I had not thought through is who opens these links. The front page is written for people who already know what this newsroom is. The people I send a list to mostly do not. They arrive from an email, sometimes through a link their mail client has wrapped in a long redirect, and the list is the first page of the newsroom they ever see.

!shot nf-before-after.webp | images/ | The same list from me to Steve, as it opened until 20 October (left) and since 21 October (right), at 1440 pixels wide in the Newsprint theme, before anything on it was read. On the left, a narrow column: the title, the note, two buttons, a box about personas, and the articles as a list of links. On the right, a dateline, my note signed, a line on what the list holds and costs, the first article as a large card, and a side column that explains the page. | comparison

The first version answered the question I asked, which was how to send a list. It did not answer the questions the person on the other end had. What is this site? Why does an article say 10p? Is that money? Do I need an account? What happens if I read half of it? It used a third of a desktop screen, and the first article started below the fold. It was a list of links, which is the thing a newsroom page should not look like.

## A letter, not a list {#letter}

Since release v0.13.19 on 21 October the page opens as a letter. At the top, a dateline: a reading list, seven articles, about an hour and a half, from Dinis, newest 21 October. Then *Chosen for Steve*, the two names, my note, signed, and what to do: Start reading, or Reply to Dinis. Before anything is read, one line says what the list holds and what it costs: five to read and two worth a look, free to start, a few pence an article after you read it, from £5.00 of credit kept in your browser.

The page uses the width of the screen. The first article is a large card with its picture beside it, large enough to read the picture's own headline, and the rest are two to a row. Every card starts with its place in the list and its date, then the headline, two lines of teaser, and at the foot, quietly, where the reader is with it. On a phone the pictures run from edge to edge and the five views fit on one row.

Down the right, a column says what the reader is looking at, in one sentence and four steps, one lit after another: read, and pay a few pence after you read; come back, and what you read is remembered here; keep the list, it is one of your personas now and nothing is sent anywhere; reply, and tell me what landed. Under it, the list as a persona, with keep and remove, and the links to find out more, starting with [the page for publishers](/publishers/index.html).

## What you have read, on the list {#read}

This newsroom already knows, inside the reader's browser, how much of each article they have read, [section by section](/articles/scrolled-is-not-read.html), and it [charges for that](/articles/your-reading-your-controls.html), not for how far the page was scrolled. The list now shows it. A ring says how much of the list is read; next to it, how many articles are read and started, the time left and what has been spent. Each card has a bar of its sections, as wide as their words and filled as they are read, and Continue goes to the first section not yet read in the first article not yet finished.

Every article also has three quiet buttons: done, later and not for me. They are the same notes the reader's vault pane keeps, so they travel with the reader's own vault to their other devices, and they are never sent to me unless the reader sends them. If the reader reads an article in another tab and comes back, the list has already caught up. None of this is tracking: the page reads what the reader's own browser already holds, and nothing leaves it.

## Five ways to see the same list {#views}

A list of seven articles is about an hour and a half of reading, and not everyone wants to start by reading. So the same list has five views, and the page remembers the one the reader chose.

!shot nf-views.webp | images/ | The same list in four of its five views, after one article was read and half of another. Headlines: one line per article, with its one-liner, the date and the time. Sections: every section of every article in one line, ticked as it is read, each a link to that section. Pictures: the articles' figures, uncropped. Graph: the articles in order along a path, their main ideas under them, an arc where one links to another, and below, the articles beyond the list that several of them link to. | collage

*Cards* is the default. *Headlines* is the list in one screen, each article's headline and its one-liner. *Sections* uses the line every section of every article now has: the whole argument of the list, a line at a time, each a link straight to that section. *Pictures* shows the articles' figures, because for some readers the figure is the article. And *Graph* draws the list as a path, with the main ideas of each article under it, an arc where one article links to another, and at the foot, the articles outside the list that several of them point to, which is where a curious reader goes next.

## Reviewed before it shipped {#review}

Before the release, I asked for the page to be reviewed by the newsroom's Designer, the role whose rules are that a card on a news page needs a date, that the picture is the card's argument and is shown where it can be read or not at all, and that nothing scrolls sideways at 390 pixels wide. It looked at a real list in every view, at desktop and phone widths, before anything was read, and ranked fourteen problems by how much each would hurt someone opening the list for the first time.

The worst were the ones I would not have noticed. The box to keep or remove the list was cut off on a desktop, inside a side column that scrolled on its own. No headline was visible before scrolling. Before reading anything, the reader saw a dashboard of zeros: 0%, read 0, spent 0p. The pictures were too small to read, and every card asked for a decision before it said what the article was. All fourteen were fixed in the same release, and [the review is published](https://newsroom.sgit.ai/admin/notes/2026-10-21__the-reading-list-design-review.md) with what was done about each.

## Pages that people use have to keep up {#keep-up}

This is the second page in a week that had to change because people started to use it. The first was [the page for publishers](/publishers/index.html), which was written once on 11 October and was out of date within a week, because this site ships something most days. It is now rebuilt in every release from the site's own register of what it can do, and it keeps a version history of its own, so a page I send to someone can be held to what it said on the day I sent it. The reading list is the same lesson in another form: the page that a person lands on is the page that has to be good, and it is rarely the one I would have designed first.

The workflow is what makes that possible. A voice memo becomes a brief, the brief becomes a release, the release is reviewed, and the next person who opens a list gets the new page. The list itself never changes: a link sent in the first week opens the new page today, with the same articles in the same order, because the link is only numbers and names.

## What comes back {#back}

The lists go out easily now. The answers do not come back as easily. Today a reader can reply by email, and the reply comes to me. What I would like next is for the page itself to be the place to answer: to select a sentence, add a note, and send it to me, and for those notes to reach the agent as well as me, in the same form as the notes the newsroom already collects from its own readers.

Two pieces of that are already on this site. Every reader's notes are already records in their own browser and their own vault, and the newsroom already has a lane that a note can be sent down. And on [pki.sgit.ai](https://pki.sgit.ai/) there is a working way, in the browser, to hold a key pair, publish a public key, and sign and encrypt a message to someone, even through a QR code. The next step is to join them: notes from a list that are signed, so the agent knows they are from the person they claim to be, and my own notes, signed with my key, so the newsroom knows they are mine. The two smaller next steps are for the sender to choose the view a list opens in, and for the list to have a picture of its own, for the email.

## What this does not claim {#limits}

- **There is no count of how many lists were opened, or read.** By design, the newsroom keeps no record of who opened a link. What I know comes from replies.
- **The twenty is the agent's count, as of 18 October.** It is from its debrief, by subject, and it has not been recounted since.
- **The screenshots use an example list.** The people I have sent lists to are not named; Steve is the site's own example.
- **The reading shown on a list is what that browser knows.** A reader who read an article on their phone sees it on their laptop only if they use their own vault.
- **The Designer is a role played by an agent.** Its review is published with what was done about each finding; it is a check, not an outside study.
- **The answers coming back, signed, are a proposal.** Nothing in the last section is built yet.

If you have received a reading list from me and would like to tell me what worked and what did not, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo of mine on 24 October 2026, after the list page had been in use for three days, written by this site's agent in the voice of this site. The argument and the editorial responsibility are mine. The brief: [a reading list in a link](/articles/a-reading-list-in-a-link.html) (11 October 2026), shipped as v0.8.0 the same day. The new page: release v0.13.19 (21 October 2026), card 086 in this site's engineering record, with the code in `for/list-views.js`; the Designer's review, `admin/notes/2026-10-21__the-reading-list-design-review.md`. The count of about 20 reading lists among 178 emails: the inbox agent's debrief of 18 October 2026, as reported in [answering a draft](/articles/answering-a-draft.html). The screenshots were taken from the built site at 1440 and 390 pixels wide in the Newsprint theme, with an example list from me to Steve; the before picture is release v0.13.18. Related: [the man behind the curtain](/articles/the-man-behind-the-curtain.html), [a link to a persona](/articles/a-link-to-a-persona.html), [scrolled is not read](/articles/scrolled-is-not-read.html), [your reading, your controls](/articles/your-reading-your-controls.html), [a section for publishers](/articles/a-section-for-publishers.html), [who is speaking](/articles/who-is-speaking.html).
