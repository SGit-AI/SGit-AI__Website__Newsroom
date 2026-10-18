---
title: Versions of versions: when a part of the site is big enough to need its own versions, the publishers' section first, and a tree of versions that runs from a page to the API
date: 2026-10-18
author: Dinis Cruz
author_url: about/index.html
summary: Versioning is one of the things that works best on this site. Every release has a number and a note, every article has its versions and the differences between them, and that history helps everyone: me, to see what changed between sessions; readers, to see what is new; and agents, to understand what is going on before they build. Now parts of the site are big enough to need the same discipline on their own. The first is the section for publishers, which has grown from a page into something closer to a website of its own, with a specific audience, regular updates and an environment that has to be maintained. On 18 October it got the start of this: a version history for its page, with every version frozen and the differences shown block by block. The idea I want to name is the next step, versions of versions: the section gets its own version line, independent of the site's, and the site's release records which version of each part it carries. It is a tree, and it is fractal: a version can contain other versions, which contain their own. The newsroom will soon be built on the newsroom API, which already has two version lines of its own, so that connection needs tracking too. In time the home page and the article pipeline could work the same way, each area with its own releases, checks and quality bar. That part is coming later. This article is also an example of writing for an agent: the idea was in my head and nowhere the agents could find it, so now it is.
version: v0.12.118
license: https://creativecommons.org/licenses/by/4.0/
tags: versioning, publishers, releases, brief, article
status: published
---

!shot vv-tree.webp | images/ | A tree of versions. At the top, a release of the newsroom, v0.12.118. Inside it, the parts it carries, each with a version line of its own: the publishers' section and its page, at version 2.0.0; the articles, each with its own versions; the API release the site pins, with its own site version and reader-code release. Coming later: the home page and the feeds. Each node can hold more versions inside it; the release records which version of each it carries. | architecture

## In short {#in-short}

- **Versioning works.** It shows what changed, between which sessions, and why.
- **Some parts of the site now need their own.** The publishers' section first.
- **It has started.** Since 18 October the page for publishers has its own versions and diffs.
- **Versions of versions.** The site's release records which version of each part it carries.
- **It is a tree, and fractal.** A version can hold versions, which hold their own.
- **The API is part of the tree.** The newsroom will be built on it, and it has its own versions.
- **The home page and the pipeline come later.** Each area with its own releases and checks.

## Why versioning works {#why}

The way this site is versioned is one of the parts that works best. Every push to the release branch is a release, with a number and a note saying what changed and why. Every article has a version, shown in its byline, and a page with every version and the differences between them. Sections are summarised with a hash, so a summary knows when its section changed under it.

That gives several things at once. A visual way of seeing what happened. A description of what changed between one session and the next. A diff, when it is needed. And a history, which matters most of all, because the history is what lets an agent understand what is going on before it builds, and what lets a reader see what is new.

## The publishers' section needs its own {#publishers}

[The section for publishers](/articles/a-section-for-publishers.html) has grown from a simple page into something closer to a website of its own. It has a specific audience, it has regular updates, it has major changes, and it has an environment that needs to be maintained. It needs exactly the same discipline as the main site: the same workflow, the same versioning, the same history.

It has started. In [v0.12.113](https://newsroom.sgit.ai/engineering/releases/v0.12.113.html), the agent that builds the site gave [the page for publishers](https://newsroom.sgit.ai/publishers/index.html) a version history of its own: each version of the text is frozen, the build stops if the text changes without a new version, and [the versions page](https://newsroom.sgit.ai/publishers/versions/index.html) shows the differences block by block and word by word, with a ledger of what changed in each release. The page went from v1.0.0, the text written on 11 October, to v2.0.0.

## Versions of versions {#versions-of-versions}

The next step is to treat the whole section the same way. The section gets its own version line, independent of the site's: it can release when it is ready, at its own pace. And the site's release records which version of the section it carries, the way a project that uses git submodules records which commit of each one it is built with. I used to do this with submodules; this is the same idea, applied to content.

The point is that you can then ask two questions, and get an answer to both. What changed in the publishers' section between its version 2 and version 3? And which version of the publishers' section was live in newsroom release v0.12.120?

## A tree, and fractal {#tree}

Once one part has its own versions, the site starts to look like a tree of versions. And it is fractal: a version can be connected to another version that has more versions inside it. A release of the site holds a version of the publishers' section, which holds a version of its page, which holds the versions of its text.

The newsroom API is already a branch of that tree. [api.newsroom.sgit.ai](https://api.newsroom.sgit.ai/) has two version lines of its own: its website, at v0.2.15 today, and the reader code it serves, at release v0.2.5. Each release is served under its own prefix and never edited afterwards. The newsroom will soon be built on top of it, pinning one release, and when it is, the site's release should record which API release it was built with. Track the versions, and track the connection between them.

## Areas with their own releases {#areas}

Taken further, the site becomes a combination of areas that are managed independently, each with its own release cycle, its own CI pipeline, its own checks and its own quality bar. Articles could be published in one area and, once they have been reviewed, move to the home page, which has its own versions, so you can see when an article arrived there and why. The feeds would follow the same pipeline. Every step would be a recorded event, and the history of the whole site would be the history of its parts.

The home page and the article pipeline are for later. The publishers' section is now, and the API connection is next.

## Written for an agent {#for-an-agent}

This article is also an example of a habit. I referred to this idea in a conversation and asked the agent to find where we had written it down. It could not, because we had not. So I record the idea, the agent writes it up, and now the agent working on the publishers' section, and any agent after it, can find it, link it, and build it.

## The brief {#brief}

For the agent that builds the site, in order:

1. **A version line for the publishers' section**, extending the page versioning of v0.12.113 from one page to the whole section, with its own changelog page.
2. **The release records it.** Each newsroom release lists the version of each part it carries, in its release note and as data.
3. **The API pin.** When the newsroom is built on api.newsroom.sgit.ai, the release records which API release it pins.
4. **A view of the tree.** One page showing, for a given site release, the version of every part it contains, and the differences from the release before.
5. **Later:** the home page and the article pipeline as areas of their own.

It is on [the briefs page](https://newsroom.sgit.ai/briefs/index.html#versions-of-versions).

## What this does not claim {#limits}

- **Only one part has its own versions today.** The page for publishers, since v0.12.113.
- **The newsroom does not yet pin an API release.** It will be built on the API soon.
- **The home page and pipeline are an idea.** Marked as later on purpose.
- **More versions means more to maintain.** Each area's version line is worth it only where the area really changes on its own.

## Where this comes from {#sources}

A voice memo from me on 18 October 2026. This site's release note for [v0.12.113](https://newsroom.sgit.ai/engineering/releases/v0.12.113.html) and the [versions of the page for publishers](https://newsroom.sgit.ai/publishers/versions/index.html); [api.newsroom.sgit.ai](https://api.newsroom.sgit.ai/) and its [llms.txt](https://api.newsroom.sgit.ai/llms.txt), read that day. Related: [a section for publishers](/articles/a-section-for-publishers.html), [the briefs so far](/articles/the-briefs-so-far.html), [my memory, checked](/articles/my-memory-checked.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.
