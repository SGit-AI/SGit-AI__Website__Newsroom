## The same three rooms, named twice

Startup Summit Lisbon 2026 has three stages. Every page of its site agrees on that, and every
page agrees that one of them is called **Workshop Rooms**.

The other two depend on which page you open.

The [agenda](https://startupsummit.io/agenda) schedules sessions on the **Unicorn Stage** and
the **Impact Stage** — *AI or Die* and *The LP Perspective* on one, *The Fundraising Meta-Game*
on the other. The [what-to-expect](https://startupsummit.io/what-to-expect) page and the
speakers page use those names too.

The [AI-summary](https://startupsummit.io/ai-summary) page lists "3 stages (Main Stage, Startup
Stage, Workshop Rooms)". The [sponsors](https://startupsummit.io/sponsors) page sells "naming
rights for one of the three stages (Main Stage, Startup Stage, or Workshop Rooms)".

Two disjoint sets, split cleanly by page, published simultaneously by the same event on the
same site, in copies frozen and hashed on 13 September 2026.

## A likely explanation, which is not a finding

The venue is **Unicorn Factory Lisboa**, in the Beato Innovation District. That is stated in the
event's own `llms.txt` and nowhere else on the site — the human-facing pages name only the
district.

A stage called the Unicorn Stage in a venue called the Unicorn Factory is not a coincidence, and
the obvious reading is that *Main Stage* and *Startup Stage* are the earlier, generic names and
the venue-specific ones came later. The pages carrying the older names would then be the ones
nobody has revisited.

**That reading is an inference and this publication is not publishing it as a fact.** The event
has not said which set is current. The opposite explanation — that the agenda is a draft and the
formal names are the generic ones — fits the same evidence. Both are recorded; neither is
resolved. If the event states which is correct, that statement becomes the source and this note
gets a correction.

## Why a naming wobble is worth a page

On its own it is worth almost nothing. Nobody will fail to find a room. The two sets are not
contradictory in any way that matters to somebody standing in Beato with a lanyard on.

It is worth a page for two reasons that have nothing to do with this event.

**First, it is the cheapest possible demonstration of what a graph layer does that reading does
not.** No human reads a conference website end to end holding all of it in their head. A
reader opens the agenda, or opens the sponsors page, and each is internally consistent. The
inconsistency only exists *between* pages, which is exactly the place where nobody is looking.
Extracting typed entities from every page of a site and comparing them is a five-line diff, and
it surfaces the class of problem that human proof-reading is structurally bad at.

**Second, it is a rehearsal on something harmless.** The same technique pointed at a regulator's
guidance, where one page defines a term one way and another page defines it differently, finds
something with consequences. This site's sibling publication
[has a whole section](../../governance/index.html) about regulatory texts where exactly that
matters — and cannot currently do this, because its ingestion path was specified and never
built. Here it runs. Running it first against a conference's stage names is how you find out
whether it works before you point it at something where being wrong is expensive.

## What this note does not say

It does not say the event is disorganised, careless, or misleading anybody. An event mid-way
through naming its rooms, with two of its pages not yet updated, is an event in the perfectly
ordinary condition of every website that has more than three pages and more than one person
editing them.

It says: **there are two published answers to the same question, both live right now, and
nothing on the open web was checking.**
