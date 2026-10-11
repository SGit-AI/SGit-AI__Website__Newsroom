# The proof is two clicks behind the claim, what the homepage gets wrong, and the fix, sgit.ai

> Twenty-five real vaults a stranger can open in one click are the most persuasive thing on this site, and the homepage shows none of them. It leads with encryption, which cannot be seen, and buries the artefacts under a table. This is the diagnosis, with screenshots, before the rebuild, and the second article will show what changed.

*Source: <https://newsroom.sgit.ai/articles/proof-behind-the-claim.html> · sgit.ai v0.7.46 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The proof is two clicks behind the claim, what the homepage gets wrong, and the fix

# The proof is two clicks behind the claim, what the homepage gets wrong, and the fix

2026-09-07 · [article v1.1.2, 4 versions](versions/proof-behind-the-claim.md) · [sgit.ai v0.2.59](https://sgit.ai/admin/versions.md) · homepagepositioningvaultsagents

***Abstract:** Twenty-five real vaults a stranger can open in one click are the most persuasive thing on this site, and the homepage shows none of them. It leads with encryption, which cannot be seen, and buries the artefacts under a table. This is the diagnosis, with screenshots, before the rebuild, and the second article will show what changed.*

Three weeks ago this site had four published vaults. Today it has twenty-five, built by several agents working with one human, and the collection now includes things that are genuinely hard to make without sgit: a penetration test report that ships with a retest script per finding, a conference keynote that carries its eight cited papers, a compliance standard rebuilt as a citable graph with 82 hashed source snapshots, a game that reports anonymous telemetry through a write-only channel.

None of that is visible from the homepage. This article is the diagnosis of why, written before the rebuild rather than after, so the two can be compared honestly.

## The homepage leads with the thing you cannot see

Here is the first screen a visitor gets:

The hero today: a claim about encryption, a pip install, and a terminal walkthrough of create, commit, history and clone.

Every word of it is true, and almost none of it is *persuasive*, for one reason: **encryption is a property you cannot look at.** Zero knowledge is a property you cannot look at. The visitor is asked to take the value on faith before being shown anything, and the first thing they are then shown is a terminal walking through `create`, `commit`, `history` and `clone`, which any git user has watched a thousand times. The walkthrough demonstrates *familiarity*, which is a virtue, but not *power*.

The word "vault" appears in the hero three times and the visitor is never shown one.

## The use cases are abstract while twenty-five concrete ones sit one level down

Scroll on and the site tells you what people use it for:

Five use-case cards, each a category rather than a thing: private memory, multi-agent collaboration, workspaces, encrypted folders, signed exchange.

These are categories, not examples. *"Multi-agent collaboration, agents on their own branches, humans reviewing the merge"* is a description of a capability. Meanwhile, one level down, there is a vault where one agent copied another agent's entire catalogue byte for byte and built a conformance layer on top of it, and the tests that prove the copy is exact still pass. That is the same idea, except you can open it.

The homepage has the abstraction. The proof is elsewhere.

## The proof is a table, two clicks away

Where is it? Under a dropdown:

Vaults → Published vaults. Two clicks from the hero to the most persuasive page on the site.

And when you get there, it is a table:

The published vaults, as of this week: sortable, categorised, and still a table, the right shape for finding a vault, the wrong shape for being convinced by one.

To be fair to the table, it was rebuilt this week and it is now a good table, sortable, categorised, newest first, with the read keys moved off it because they were squeezing the vault id to one character per line. But a table is the right shape for *finding* a vault and the wrong shape for being *convinced* by one. It answers "which of these do I want" for a visitor who already wants one.

Here is what the visitor could have been looking at one second after arriving, with no account and no install:

A real vault, open: the AIUC-1 conformance layer computing insurability for a named subject as of a date, one condition met, 52 exclusions, zero of five consequences covered, each with the reason in the control's own words.Another: a game about which wings of the building an agent can enter, drawn as a floor plan, with a belief column ranking nine public agent profiles as you answer.

Both of these are opened by one string. Both run entirely in the browser. Both ship with their data, their sources and their tests inside the same encrypted unit. The second one built its own telemetry from a brief published on this site. **None of this requires the visitor to understand encryption first.** It requires them to click.

## The strongest story has no front door

The thing that most distinguishes how this site is made is that it is built by one person and a team of agents, and the agents build for each other. The evidence is real and specific:

- A brief published here on 6 September was read by another agent, who built a vault from it the same day.
- That vault was reviewed by the team that owns the API it uses, who found the brief had been wrong in two places, and the correction is now published above the mistake.
- One agent forked another agent's vault, kept every byte, added a layer, and shipped a fourteen-version history that labels seven of the versions as *reconstructed* rather than inventing commits.

Where does a visitor learn this? Here:

The briefs page, the cross-team collaboration log, filed under Docs, three levels from the homepage, and written as a log rather than a story.

It is filed under Docs. It is written as a log, which is the right format for the record and the wrong one for a first-time reader. The productivity claim that the whole site rests on, *this is what working with agents looks like when the state is versioned and shareable*, has no page that tells it end to end.

## One gap worth naming

The homepage says *"a branch per agent; work meets on named branches; a human reviews the merge."* It is the site's strongest claim about multi-agent work, and **no published vault demonstrates it.** Every vault here was built by one agent, or by one agent on top of another's finished work. None shows two agents' branches and a human merge in its history.

If such a vault exists, publishing it is the single highest-value addition to the site. If it does not, the next multi-agent build should be run so that its history shows it. A claim on a homepage with no artefact behind it is exactly what this site says it does not do.

## The fix, in order

Not more bands. The homepage already has nine, and 1,370 words. The fix is to reorder so proof comes before mechanism, and to cut.

1. **The hero shows vaults.** One reframed sentence (a vault is a unit of work: data, app, history and sources, shipped as one string, and the server cannot read it) with **four real vaults as cards** under it, each with a screenshot and an *open it* link. The visitor is inside an artefact before they have read a paragraph. `pip install` stays, second.
2. **"What people actually ship"**: six vaults chosen by *job* rather than by shape: hand over a report, publish a standard as data, give a talk, pitch an investor, run a game, give an agent a workspace. Each with one line on why it is hard without this. Generated from the same data as the table, so it never goes stale.
3. **"One human, a team of agents"**: the collaboration story told as a story, with the numbers, and a single page behind it that walks the loop end to end.
4. Then the terminal walkthrough and the zero-knowledge explanation, for the developer who is *now* interested in how.
5. The honesty band and the network band stay. The "three doors" band moves to the docs.

## And a page that says who is behind it

A beta tool that asks people to publish their read keys on it is asking for trust, and this site has no page saying who is asking. There will be one. It will be about **sgit** (who builds it, honestly including the agents; why; the commercial line) and it will borrow two sections that fit this site's culture exactly, *Interests declared* and *Reach me, or correct me*, from the fuller record that already exists on a sibling site:

open-source.sgit.ai · Business & publishing · [About the author, Dinis Cruz ↗](https://open-source.sgit.ai/about/index.html) · The record across four companies, built in the open including the parts most companies keep closed, and the interests declared. · “Open source is a strategy. It is not a charity.” · part of the sgit.ai network

That card is new as of this article. The `*.sgit.ai` sites exist so each topic can get the depth a section here could not give it, which only pays off if this site points at them constantly, and a bare link does not say *this continues elsewhere, on purpose*. The card does. Authors write one line; the site's own category and thesis come from its entry in the network directory, so the card describes that site the way it describes itself.

## What happens next

The rebuild is the next release. The article after it will put the new homepage next to these screenshots, and say what changed and what it cost. If the "before" pictures here still look better than the "after", that article will say so too.

*Written by Dinis Cruz and the agentic team working with him. Licensed CC BY 4.0.*

## Threads

Site & engineeringVaults & method[This article as a graph →](graphs.md#proof-behind-the-claim)

### Continued by

- [The proof moved up, the homepage after the rebuild, next to the before pictures](proof-moved-up.md) The rebuilt homepage puts four real vaults under one sentence, picks six by the job they do, and computes its numbers at build time from the site's own data.

[All articles](index.md) · [All graphs](graphs.md)

**Posting this article on LinkedIn?** The cover is [proof-behind-the-claim.jpg](banners/proof-behind-the-claim.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/proof-behind-the-claim.html)*
