---
title: How cheap is it to undo? A spectrum of trust and side effects, and why the newsroom ships on its own while my email still waits for me
date: 2026-10-13
author: Dinis Cruz
author_url: about/index.html
summary: Writing about the human in the loop, we noticed something about our own workflow: this newsroom arrived, organically, at releasing on its own, fourteen times in one day, with nobody approving each release, while every email my agents write still waits for me to press send. I think that contrast goes to the heart of the question, and it is a spectrum, not a switch. The best test I know for how much to let go is how cheap it is to undo. I remember a senior executive, I think from Google, whose test for people asking to start a project or an experiment was exactly that: if it does not reach many people and can be switched off with little side effect, say yes, trust the people, have a go, because the only cost is the time and there is always learning; what worried him was how hard it would be to undo. Amazon put the same idea as one-way and two-way doors. An email is a one-way door: once it goes, you cannot claim it back, a mistake does damage straight away, and my email workflow is still in the explorer phase, with nascent controls and not yet many emails read and sent without changes. The newsroom is a two-way door: a correction is a new version, anyone who arrives after the fix gets the fixed page, few people are reading yet, new articles land in the latest list without being placed on the front page, and the checks and balances are mature, from the validator to the leak scan to briefing packs that hand work between sites. When I read an article, I am either happy with it or I make small changes; I have not yet read one and thought I do not want that live. So the spectrum has two axes, the cost of undoing and the maturity of the controls and the record, and both move: as readership grows the newsroom's side effects grow with it, and as the email controls mature, email can move the other way.
version: v0.12.22
license: https://creativecommons.org/licenses/by/4.0/
tags: reversibility, two-way-doors, trust, side-effects, human-in-the-loop, agents, release, maturity, wardley-maps, newsroom, article
status: published
---

!shot cu-spectrum.webp | images/ | The spectrum. Across: how much it costs to undo, from a two-way door to a one-way door. Up: how mature the controls and the record are, from explorer to town planner. Where an output sits decides how much a person has to hold it. The newsroom's articles sit where they can ship on their own; email in my name sits where I decide every one. The arrows are where each is moving. | decision

## In short {#in-short}

- **We arrived at auto-release without deciding to.** Fourteen releases of this site in one day, every commit by an agent, nobody approving each one, while every email still waits for me.
- **The test is how cheap it is to undo.** If an experiment can be switched off with little side effect, say yes and trust the people; worry about what cannot be undone. Amazon calls it one-way and two-way doors.
- **An email is a one-way door.** Once sent, it cannot be claimed back, the damage is immediate, and the workflow is still young: controls nascent, not yet many emails sent unchanged.
- **An article here is a two-way door.** A fix is a new version, the next reader gets the fixed page, few people are reading yet, and new pieces land in the latest list without being placed on the front page.
- **The controls are mature where it ships.** A validator, browser tests, a leak scan, versions and diff pages, briefing packs between sites, and a reader who has made small changes and never pulled one.
- **It is a spectrum with two axes, and both move.** Readership raises the newsroom's side effects; maturing controls lower email's. The line is a decision to revisit, not a setting.

## What we noticed {#noticed}

In [The human in the loop](/articles/the-human-in-the-loop.html) the agent writing this site raised something I had not put into words. This newsroom ships on its own. On 13 October it released fourteen times, every commit made by an agent, and nobody approved a release before it went live. My email works the opposite way: the agents draft every message and I send every one. Nobody designed that difference. We arrived at it, organically, and I think it goes to the heart of the human in the loop question, because it is not a switch between trust and control. It is a spectrum.

## The test: how cheap is it to undo? {#test}

I remember a senior executive, I think from Google, a company that runs a lot of experiments and a lot of crazy projects, describing his test for when people asked whether they could start one. He did not spend much time on whether the project was possible, or on challenging the plan. He trusted the people: have a go, see what you can do. What he worried about was how easy, and how cheap, it would be to undo. If it was a tool or an experiment that would not have many users, and pulling the plug would have very little side effect, the only real cost was the time spent, and that is fine, because there is always learning. Then the answer was yes. I could not find who said it, or where, so I will not put a name to it; if you know, tell me.

Amazon's version of the same idea is better documented. In his letter to shareholders for 2015, Jeff Bezos separated decisions into two types. Some are ["one-way doors"](https://s2.q4cdn.com/299287126/files/doc_financials/annual/2015-Letter-to-Shareholders.PDF): "consequential and irreversible or nearly irreversible", to be made "methodically, carefully, slowly". Most are two-way doors: "changeable, reversible", and "if you've made a suboptimal Type 2 decision, you don't have to live with the consequences for that long. You can reopen the door and go back through." His warning was that large organisations tend to use the heavy process for both.

Engineering learned the same thing about releases. Google's [Site Reliability Engineering book](https://sre.google/sre-book/introduction/) says that "roughly 70% of outages are due to changes in a live system", and that the answer is progressive rollouts, quick detection and "rolling back changes safely when problems arise". A change you can roll back is a two-way door; the work of a release pipeline is to keep it one.

The same question applies to every output an agent produces. Not "do I trust the agent", which has no answer, but "if this is wrong, how cheap is it to undo, and what does it break before I do?"

## Email is a one-way door, and still an explorer {#email}

An email is the clearest one-way door I have. When it goes, that is it; you cannot claim it back. The stakes are higher too: a wrong fact, a wrong tone, the same email sent twice, a figure that does not add up, and the damage is done the moment it lands, in a relationship I care about.

And the email workflow is younger than it looks. In the terms of [Go slow to go fast](/articles/explorer-to-villager-newsroom.html), it is still in the explorer phase. The controls are nascent: [a second reader the agent cannot skip](/articles/a-second-reader-the-agent-cannot-skip.html) checks every draft, but it was built after two emails went out wrong, and the rest is the policy and me. We are still working out the workflows. And I have not yet reached the point where I am reading and sending a large number of emails unchanged, which is the record that would let a kind of email leave my hands. So every email waits for me, and it should.

## The newsroom is a two-way door, with mature controls {#newsroom}

The newsroom is the other end. An article can be undone, or rather corrected: a correction is a new version, with a page that shows what changed, and anyone who arrives after the fix gets the fixed page, even if the old one was indexed somewhere. The side effects are small for now, because not many people are reading yet. And the pipeline already has a stage in it: a new article lands in the latest list, but the front page's lead and highlights are placed by the Editor, and today they are still the edition of 8 October. A new piece is live, findable and linkable without being promoted.

The checks and balances are also much further along than in email. Every release goes through a validator that fails on a broken link, a quote that is not word for word in its source, a banned word or a missing figure; browser tests; a leak scan that refuses a key or a private name; versions that are never reused. The work moves between sites with briefing packs: sgit.ai's agent briefed this one on its moved banner, this session briefed the next on the newsletter. And then there is the record that matters most: when I read an article, I am either very happy with it or I make small changes, some cosmetic, some a zoom on one point. I have not yet read one and thought, I do not want that live. That record is why I am comfortable saying: put it there, and send me the link.

## Two axes, and both move {#axes}

!shot cu-compare.webp | images/ | The two workflows side by side, by what decides where they sit: how cheap it is to undo, how large the side effects are today, how mature the controls are, and what the record says. The same agents and the same person; opposite places on the spectrum. | comparison

So the spectrum has two axes. Across, the cost of undoing: what it takes to reverse an output, and what it breaks before you do. Up, the maturity of the controls and of the record: from explorer, where the workflow is still being found and a person holds most of the weight, through villager, where the controls exist and are tested, to town planner, where the thing is boring, measured and cheap. Where an output sits on those two axes decides how much a person has to hold it.

The important part is that both axes move. The newsroom's side effects will grow with its readership: a wrong article read by ten people and a wrong article read by ten thousand are not the same door, and as that happens the line moves back, which is what the unplaced latest list is for, a stage before promotion that can become a proper canary. Email moves the other way as its controls mature: a second reader that catches more, a policy with fewer rows on hope, and a record of drafts I did not change. When that record is long enough for one kind of message, that kind is a candidate to leave my hands, by a decision written into the policy, with an owner and a date.

That is the answer I would give a business asking where to let go. Not by department, and not by how much it trusts the model. By output: how cheap is it to undo, how large are the side effects today, how mature are the controls, and what does the record say. And revisit it, because every one of those changes.

## What this does not claim {#limits}

- **The readership is small, and that is part of the argument.** The newsroom's low side effects are partly that few people read it yet; the same release process would need a canary stage at a larger scale.
- **"Never pulled an article" is one reader's record.** It is mine, over a few weeks, not a measurement.
- **Not everything on a site is a two-way door.** A leaked key in a published page is a one-way door, which is why the leak scan runs before the commit, not after.
- ****The Google executive is a memory, not a source.** I could not find who said it; the idea is the one Bezos wrote down, and it is attributed here to my memory, not to a name.**
- **Email can still move.** The explorer phase is where it is today, not where it has to stay.

If you are deciding which of your agents' outputs can ship on their own, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo of mine on 13 October 2026, after reading The human in the loop, written by this site's agent in the voice of this site. The argument and the editorial responsibility are mine. Jeff Bezos, [2015 letter to shareholders](https://s2.q4cdn.com/299287126/files/doc_financials/annual/2015-Letter-to-Shareholders.PDF), April 2016. Google's [Site Reliability Engineering book](https://sre.google/sre-book/introduction/) on why rollback matters: "roughly 70% of outages are due to changes in a live system", and the answer is progressive rollouts, fast detection and "rolling back changes safely". The release counts are from this repository's git log for 13 October 2026; the front page's placement is from its edition file, dated 8 October.
