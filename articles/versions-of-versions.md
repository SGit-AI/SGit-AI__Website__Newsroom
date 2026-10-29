# Versions of versions: when a part of the site is big enough to need its own versions, the publishers' section first, and a tree of versions that runs from a page to the API, sgit.ai

> Versioning is one of the things that works best on this site. Every release has a number and a note, every article has its versions and the differences between them, and that history helps everyone: me, to see what changed between sessions; readers, to see what is new; and agents, to understand what is going on before they build. Now parts of the site are big enough to need the same discipline on their own. The first is the section for publishers, which has grown from a page into something closer to a website of its own, with a specific audience, regular updates and an environment that has to be maintained. On 18 October it got the start of this: a version history for its page, with every version frozen and the differences shown block by block. The idea I would like to name is the next step, versions of versions: the section gets its own version line, independent of the site's, and the site's release records which version of each part it carries. It is a tree, and it is fractal: a version can contain other versions, which contain their own. The newsroom will soon be built on the newsroom API, which already has two version lines of its own, so that connection needs tracking too. In time the home page and the article pipeline could work the same way, each area with its own releases, checks and quality bar. That part is coming later. This article is also an example of writing for an agent: the idea was in my head and nowhere the agents could find it, so now it is.

*Source: <https://newsroom.sgit.ai/articles/versions-of-versions.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Versions of versions: when a part of the site is big enough to need its own versions, the publishers' section first, and a tree of versions that runs from a page to the API

# Versions of versions: when a part of the site is big enough to need its own versions, the publishers' section first, and a tree of versions that runs from a page to the API

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-18 · [article v1.2.0, 3 versions](versions/versions-of-versions.md) · [newsroom v0.12.118](https://newsroom.sgit.ai/admin/versions.html) · versioningpublishersreleasesbriefarticle

***Abstract:** Versioning is one of the things that works best on this site. Every release has a number and a note, every article has its versions and the differences between them, and that history helps everyone: me, to see what changed between sessions; readers, to see what is new; and agents, to understand what is going on before they build. Now parts of the site are big enough to need the same discipline on their own. The first is the section for publishers, which has grown from a page into something closer to a website of its own, with a specific audience, regular updates and an environment that has to be maintained. On 18 October it got the start of this: a version history for its page, with every version frozen and the differences shown block by block. The idea I would like to name is the next step, versions of versions: the section gets its own version line, independent of the site's, and the site's release records which version of each part it carries. It is a tree, and it is fractal: a version can contain other versions, which contain their own. The newsroom will soon be built on the newsroom API, which already has two version lines of its own, so that connection needs tracking too. In time the home page and the article pipeline could work the same way, each area with its own releases, checks and quality bar. That part is coming later. This article is also an example of writing for an agent: the idea was in my head and nowhere the agents could find it, so now it is.*

A tree of versions: a newsroom release, v0.12.118, and the parts it carries, each with its own version line.

## In short

- **Versioning works.** It shows what changed, between which sessions, and why.
- **Some parts of the site now need their own.** The publishers' section first.
- **It has started.** Since 18 October the page for publishers has its own versions and diffs.
- **Versions of versions.** The site's release records which version of each part it carries.
- **It is a tree, and fractal.** A version can hold versions, which hold their own.
- **The API is part of the tree.** The newsroom will be built on it, and it has its own versions.
- **The home page and the pipeline come later.** Each area with its own releases and checks.

## Why versioning works

The way this site is versioned is one of the parts that works best. Every push to the release branch is a release, with a number and a note saying what changed and why. Every article has a version, shown in its byline, and a page with every version and the differences between them. Sections are summarised with a hash, so a summary knows when its section changed under it.

That gives several things at once. A visual way of seeing what happened. A description of what changed between one session and the next. A diff, when it is needed. And a history, which matters most of all, because the history is what lets an agent understand what is going on before it builds, and what lets a reader see what is new.

## The publishers' section needs its own

[The section for publishers](a-section-for-publishers.md) has grown from a simple page into something closer to a website of its own. It has a specific audience, it has regular updates, it has major changes, and it has an environment that needs to be maintained. It needs exactly the same discipline as the main site: the same workflow, the same versioning, the same history.

It has started. In [v0.12.113](https://newsroom.sgit.ai/engineering/releases/v0.12.113.html), the agent that builds the site gave [the page for publishers](https://newsroom.sgit.ai/publishers/index.html) a version history of its own: each version of the text is frozen, the build stops if the text changes without a new version, and [the versions page](https://newsroom.sgit.ai/publishers/versions/index.html) shows the differences block by block and word by word, with a ledger of what changed in each release. The page went from v1.0.0, the text written on 11 October, to v2.0.0.

## Versions of versions

The next step is to treat the whole section the same way. The section gets its own version line, independent of the site's: it can release when it is ready, at its own pace. And the site's release records which version of the section it carries, the way a project that uses git submodules records which commit of each one it is built with. I used to do this with submodules; this is the same idea, applied to content.

The point is that you can then ask two questions, and get an answer to both. What changed in the publishers' section between its version 2 and version 3? And which version of the publishers' section was live in newsroom release v0.12.120?

## A tree, and fractal

Once one part has its own versions, the site starts to look like a tree of versions. And it is fractal: a version can be connected to another version that has more versions inside it. A release of the site holds a version of the publishers' section, which holds a version of its page, which holds the versions of its text.

The newsroom API is already a branch of that tree. [api.newsroom.sgit.ai](https://api.newsroom.sgit.ai/) has two version lines of its own: its website, at v0.2.15 today, and the reader code it serves, at release v0.2.5. Each release is served under its own prefix and never edited afterwards. The newsroom will soon be built on top of it, pinning one release, and when it is, the site's release should record which API release it was built with. Track the versions, and track the connection between them.

## Areas with their own releases

Taken further, the site becomes a combination of areas that are managed independently, each with its own release cycle, its own CI pipeline, its own checks and its own quality bar. Articles could be published in one area and, once they have been reviewed, move to the home page, which has its own versions, so you can see when an article arrived there and why. The feeds would follow the same pipeline. Every step would be a recorded event, and the history of the whole site would be the history of its parts.

The home page and the article pipeline are for later. The publishers' section is now, and the API connection is next.

## Written for an agent

This article is also an example of a habit. I referred to this idea in a conversation and asked the agent to find where we had written it down. It could not, because we had not. So I record the idea, the agent writes it up, and now the agent working on the publishers' section, and any agent after it, can find it, link it, and build it.

## The brief

For the agent that builds the site, in order:

1. **A version line for the publishers' section**, extending the page versioning of v0.12.113 from one page to the whole section, with its own changelog page.
2. **The release records it.** Each newsroom release lists the version of each part it carries, in its release note and as data.
3. **The API pin.** When the newsroom is built on api.newsroom.sgit.ai, the release records which API release it pins.
4. **A view of the tree.** One page showing, for a given site release, the version of every part it contains, and the differences from the release before.
5. **Later:** the home page and the article pipeline as areas of their own.

It is on [the briefs page](https://newsroom.sgit.ai/briefs/index.html#versions-of-versions).

## What this does not claim

- **Only one part has its own versions today.** The page for publishers, since v0.12.113.
- **The newsroom does not yet pin an API release.** It will be built on the API soon.
- **The home page and pipeline are an idea.** Marked as later on purpose.
- **More versions means more to maintain.** Each area's version line is worth it only where the area really changes on its own.

## Where this comes from

A voice memo from me on 18 October 2026. This site's release note for [v0.12.113](https://newsroom.sgit.ai/engineering/releases/v0.12.113.html) and the [versions of the page for publishers](https://newsroom.sgit.ai/publishers/versions/index.html); [api.newsroom.sgit.ai](https://api.newsroom.sgit.ai/) and its [llms.txt](https://api.newsroom.sgit.ai/llms.txt), read that day. Related: [a section for publishers](a-section-for-publishers.md), [the briefs so far](the-briefs-so-far.md), [my memory, checked](my-memory-checked.md). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Site & engineeringVaults & method[This article as a graph →](graphs.md#versions-of-versions)

### Builds on

- [A section for publishers: where to send someone new to this newsroom, and a site that keeps itself current](a-section-for-publishers.md) Where to send a publisher new to the newsroom: a section placed by rule, with features as they ship, that keeps itself current as the site changes.
- [The briefs so far: sixty-five things this newsroom has asked of itself, what is built, and where each next session starts](the-briefs-so-far.md) Sixty-five briefs this newsroom has asked of itself, audited from the code: 11 built, 21 partly, 32 not, each open one with a session brief.
- [My memory, checked: thinking out loud in a voice memo, publishing only what the record supports, and why peer review has moved to before publishing](my-memory-checked.md) I say it as I remember it; the agent checks it against the record before anyone reads it. Five confirmed, five corrected, two not found.

### Continued by

- [A website to finish the book: gen-z-developers.sgit.ai, where the released book lives in the repository, the working book lives in a vault, and agents help me review it at every altitude](a-website-to-finish-the-book.md) gen-z-developers.sgit.ai: the released book in the repository, the working book in a public vault, and agents helping me review it at every altitude.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 202 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=202)

**Posting this article on LinkedIn?** The cover is [versions-of-versions.jpg](banners/versions-of-versions.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/versions-of-versions.html)*
