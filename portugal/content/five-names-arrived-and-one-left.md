## What the two copies say

On 8 September 2026 at 00:43 UTC this publication fetched the Startup Summit Lisbon 2026
speakers page and kept the bytes. The page said, in its own prose, **"60 confirmed speakers are
listed below"**, and it rendered 60 speaker cards.

On 13 September 2026 at 19:41 UTC it fetched the same page again. That copy says **"64 confirmed
speakers are listed below"**, and renders 64 cards.

Both files are in this repository. Their SHA-256 hashes differ, which is what a changed page
looks like when somebody bothered to write down what it said the first time.

## Who moved

Five names appear in the later copy and not the earlier one:

- **Cíntia Costa** — listed under 351 Portuguese Startup Association
- **Ed Chandler** — listed under PriFly Advisors
- **Olesia Rykova** — listed under SOULBRANDING
- **Olivia Page** — listed under Mykor
- **Ricardo** — listed under Startup Summit

One name appears in the earlier copy and not the later one:

- **Kambis Kohansal Vajargah** — was listed under Austrian Federal Economic Chamber

> We do not know why that name is no longer on the list, and this publication is not going to
> guess.

That is not a hedge, it is the rule. A speaker withdrawing, a scheduling clash, a duplicate
record being merged, a data-entry correction and an editing mistake are **indistinguishable
from outside the organisation**. Publishing a diff costs nobody anything. Publishing a motive
attached to a named individual, on this evidence, would be the easiest way for a publication
like this one to do real harm to a real person. The change is recorded; the reason field is
empty and stays empty unless a source fills it.

## The addition is not a finding

An event adding five speakers nine days before it opens is an event working exactly as
advertised. The speakers page says so itself: more are **"announced weekly"**. Nothing in the
growth is surprising, and nobody should read this as a correction to anything.

What is worth noticing is smaller and duller. The number in the prose moved *with* the list —
60 with 60 cards, 64 with 64 cards. A page whose stated count tracks its own contents is a
maintained page, and that is more than can be said for most.

## So what is the story

The story is that **five days ago this list said something else, and by the time the doors open
nothing on the open web will remember what.**

The earlier version is not archived anywhere the reader can reach. It is not in the page's
history, because the page has no history. Search engines will show the current one. An
assistant asked "who is speaking at Startup Summit Lisbon" will answer from whatever is live at
the moment it is asked, with no sense that the answer had a different shape last week.

This is the ordinary condition of nearly everything published on the open web, and it is
invisible precisely because it is ordinary. A conference speaker list is a harmless example. The
same property holds for a company's pricing page, a regulator's guidance, a government
consultation and a hospital's waiting-time figure — and it is the reason this network keeps
arguing that a link is not evidence, because the thing on the other end of a link is free to
change and usually does.

## What it cost to be able to say this

One `curl`, one `sha256sum`, and the decision to keep the file.

That is the entire apparatus. There is no archive service in the loop, no third party to trust
and nothing to subscribe to. The [method page](../method.html) sets out the five verbs — fetch,
freeze, hash, extract, diff — and the expensive one is not any of them. The expensive part is
having done it *before* you needed it, which means doing it on a cadence when nothing is
happening, which is why almost nobody does.

Both copies, both hashes and the instructions for checking them are in
[the source register](../sources.html). If the live page now says something different from what
is quoted above, that is not an error in this story. That is the next entry.
