# The proof moved up, the homepage after the rebuild, next to the before pictures, sgit.ai

> The previous article diagnosed a homepage that led with encryption and buried twenty-five real vaults under a table. This is the rebuild, put beside those screenshots, what moved, what was cut, what it is generated from, and the one thing it still cannot show.

*Source: <https://newsroom.sgit.ai/articles/proof-moved-up.html> · sgit.ai v0.7.51 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The proof moved up, the homepage after the rebuild, next to the before pictures

# The proof moved up, the homepage after the rebuild, next to the before pictures

2026-09-07 · [article v1.2.2, 5 versions](versions/proof-moved-up.md) · [sgit.ai v0.2.60](https://sgit.ai/admin/versions.md) · homepagepositioningvaultsagents

***Abstract:** The previous article diagnosed a homepage that led with encryption and buried twenty-five real vaults under a table. This is the rebuild, put beside those screenshots, what moved, what was cut, what it is generated from, and the one thing it still cannot show.*

[The previous article](proof-behind-the-claim.md) made a diagnosis and a promise: the homepage led with a property nobody can look at, the proof sat two clicks away as a table, and the rebuild would be put next to those screenshots so the comparison could be made honestly. This is that comparison.

## The first screen

Before: a claim about encryption, a `pip install`, and a terminal walkthrough of four commands every git user has seen.

Before. The word "vault" appears three times and the visitor is shown none.

After: one reframed sentence, and four real vaults under it.

After. Four published vaults with their screenshots, each one click from open. `pip install` is still there, second.

The sentence changed from *"the encrypted git for humans and AI agents"* to *"a vault is a unit of work: data, app, history and sources, shipped as one string."* Encryption did not leave; it became the subordinate clause, *and the server that stores it cannot read it*, which is where a property you cannot see belongs. The four cards are chosen by a `hero` field in the vault data, so changing the front door is a data edit, not a page edit.

## The use cases became things

Before: five cards, each a category.

Before. "Multi-agent collaboration, agents on their own branches, humans reviewing the merge." True, and not something you can open.

After: six vaults chosen by the job they do.

After. Hand over a report. Publish a standard as data. Give a talk. Pitch an investor. Ship a game that reports back. Give an agent a workspace. Each is a real vault, with one line on why it is hard to make any other way.

The distinction the band is built on: none of those six lines is about encryption. A pentest report whose retest scripts travel with the findings; a talk whose cited papers never separate from the deck; a game whose telemetry uses the one credential shape that survives being published. Those are properties of *a vault as a unit*, and they are what a newcomer can actually feel.

## The collaboration story got a front door

Before: a log, filed under Docs.

Before. The cross-team briefs, the record of agents working with each other and with the human, three levels from the homepage, written as a log.

After: a band with the numbers and the story.

After. Four numbers computed at build time (releases, vaults, sibling sites, briefs) and the loop told in three beats with the artefacts linked.

The numbers are not typed. Releases come from the version log, vaults from the vault data, sites from the network directory, briefs from counting the entries on the briefs page. If a number on that band is wrong, the site is wrong somewhere else too, and that is the right dependency.

## What was cut

- **The abstract use-case band.** The five categories still exist as pages, still in the nav under Evidence; they are no longer the homepage's answer to "what is this for".
- **"One vault, three doors."** The sgit / SG/Vault / SG/Send explanation was a full band. It is a single pill in the trust strip now, pointing at the page that already explained it.
- **Nothing from the terminal walkthrough.** It moved down and gained a heading (*Under the hood, it is git*) because for the visitor who has just opened a real vault, *how* is now the question. It gained one feature card too: *apps live inside the data*, which was somehow never on the list.

The band count did not change, nine before, nine after: three were cut and three were added, so what changed is the order and what comes first, not the length. (The first version of this paragraph said "nine became eight"; it was corrected in v0.2.61 after counting rather than remembering.) The page is longer in bytes, because it carries ten screenshots, and slightly shorter in words: 1,370 to 1,332. That is the trade: pictures of real things instead of paragraphs about them. The screenshots load lazily and through the same mechanism every vault page uses, so the page still renders from inside a vault.

## What it cannot show yet

The previous article named a gap, and the rebuild did not close it: **no published vault demonstrates two agents on one vault**: their branches, and a human merging them. The team band tells the story of agents building *for* each other, which is true and evidenced. It does not yet show agents building *with* each other in the same history, which is the site's strongest claim. The band is written so that it does not pretend otherwise. When that vault exists, it goes in the hero.

## What it is generated from

One file, `admin/content/vaults.json`, now drives the hero cards, the six jobs, the sortable table and the vault count on the team band. Adding a vault is adding a row; promoting one to the front door is setting a field. The homepage stopped being a page somebody edits and became a view over the site's own data, which is the same rule the articles band, the network directory and the update feed already followed. It just took the homepage longest to get there.

*Written by Dinis Cruz and the agentic team working with him. Licensed CC BY 4.0.*

## Threads

Site & engineeringVaults & method[This article as a graph →](graphs.md#proof-moved-up)

### Builds on

- [The proof is two clicks behind the claim, what the homepage gets wrong, and the fix](proof-behind-the-claim.md) The homepage leads with encryption, which cannot be seen, while twenty-five vaults a stranger can open in one click sit two clicks away in a table.

[All articles](index.md) · [All graphs](graphs.md)

**Posting this article on LinkedIn?** The cover is [proof-moved-up.jpg](banners/proof-moved-up.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/proof-moved-up.html)*
