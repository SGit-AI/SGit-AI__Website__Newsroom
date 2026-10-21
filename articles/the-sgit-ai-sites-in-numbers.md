# The sgit.ai sites in numbers: 53 repositories, 45 live sites, 1,679 commits and 5,419 pages in eleven weeks, and what the shape of the estate says, sgit.ai

> It is worth taking a step back and looking at all the sgit.ai sites together. On 21 October 2026 there were 53 website repositories under SGit-AI, the first started on 11 August. 45 of them answer as live sites, one is built and not yet serving, and seven are placeholders, two of them created this morning for the AWS twin and the user site. Between them they hold 1,679 commits, 33,541 files and 5,419 pages listed in their sitemaps. The estate grew in bursts of about ten new sites a week, and the busiest week for commits was the one of 12 October, with 331. The shape is a long tail: four repositories, sgit.ai, the newsroom, graphs and PKI, hold 62% of the commits, while the median site has seven, because most sites were built in a session or two and then left to do their job. Families are appearing, hubs with instances under them, which is why the naming now needs a rule. This is the data, with the charts, and what I read from it.

*Source: <https://newsroom.sgit.ai/articles/the-sgit-ai-sites-in-numbers.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The sgit.ai sites in numbers: 53 repositories, 45 live sites, 1,679 commits and 5,419 pages in eleven weeks, and what the shape of the estate says

# The sgit.ai sites in numbers: 53 repositories, 45 live sites, 1,679 commits and 5,419 pages in eleven weeks, and what the shape of the estate says

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-21 · [article v1.0.0](versions/the-sgit-ai-sites-in-numbers.md) · [newsroom v0.13.16](https://newsroom.sgit.ai/admin/versions.html) · sgitwebsitesdataestatearticle

***Abstract:** It is worth taking a step back and looking at all the sgit.ai sites together. On 21 October 2026 there were 53 website repositories under SGit-AI, the first started on 11 August. 45 of them answer as live sites, one is built and not yet serving, and seven are placeholders, two of them created this morning for the AWS twin and the user site. Between them they hold 1,679 commits, 33,541 files and 5,419 pages listed in their sitemaps. The estate grew in bursts of about ten new sites a week, and the busiest week for commits was the one of 12 October, with 331. The shape is a long tail: four repositories, sgit.ai, the newsroom, graphs and PKI, hold 62% of the commits, while the median site has seven, because most sites were built in a session or two and then left to do their job. Families are appearing, hubs with instances under them, which is why the naming now needs a rule. This is the data, with the charts, and what I read from it.*

Fifty-three repositories in eleven weeks. Left: new site repositories each week, with the running total underneath. Right: commits across all of them each week, peaking at 331 in the week of 12 October.

## In short

- **53 repositories, 45 live sites.** One built and not serving yet, seven placeholders.
- **1,679 commits in eleven weeks.** The first repository started on 11 August 2026.
- **5,419 pages in the sitemaps.** And 33,541 files across the repositories.
- **It grew in bursts.** About ten new sites in each of five weeks.
- **A long tail.** Four repositories hold 62% of the commits; the median site has seven.
- **Families are appearing.** Hubs with instances under them, which is why naming needs a rule.

## The estate, counted

On 21 October 2026 there were 53 repositories under SGit-AI whose names start with `SGit-AI__Website`, each one a website. I fetched the history of every one of them, all branches, without the file contents, counted the files at the head of each, and asked every host whether it answers, how many pages its sitemap lists, and which version it says it is.

- **45 answer as live sites.** Every one of them on GitHub Pages, under sgit.ai.
- **1 is built and not serving.** ux.sgit.ai has a repository of 209 files and a domain set, and returns 404.
- **7 are placeholders.** A README and little else: hooks, tokens.hook, demos and two demo sites, all made on 14 October, and aws.twin and user, made this morning.

Together they hold 1,679 commits, 1,416 of them with a version number in the subject, which is how these sites mark a release. At their heads there are 33,541 files: 9,317 HTML pages, 9,602 markdown files and 5,995 images. And the live sites list 5,419 pages in their sitemaps.

Most of them can be read by an agent as well as a person: 35 of the 46 repositories with content publish an `llms.txt`, 41 of the 45 live sites serve a sitemap, and 33 publish their version at the usual path.

## How it grew

The first repository, sgit.ai itself, started on 11 August 2026. Then the estate grew in bursts. Nine new sites in the week of 17 August and ten in the week of 24 August, as the first ideas each got a site of their own: NHI, PKI, graphs, the newsroom, risks, standards, twins and others. Ten more in the week of 7 September, with the games, the providers family and the store. A quieter stretch through September and early October, with the Portuguese and sgit editions of the newsroom, MyFeeds, vCISO and secrets. Then ten in the week of 12 October, with the newsroom's API, Ruv, the hooks and demos placeholders, UX, NotebookLM and the Gen Z Developers book; and eight in the week of 19 October: the CLI, storyboards and its API, send and its API, startups, and, this morning, the AWS twin and the user site.

Commits follow a different rhythm. The busiest week was the one of 12 October, with 331 commits across all repositories, more than any other week by far; the quietest the week of 28 September, with 60.

## Where the work is

Commits per repository, the fourteen busiest. sgit.ai has 495, the newsroom 262, graphs 139 and PKI 137; together they hold 62% of the 1,679 commits.

The shape is a long tail. Four repositories, sgit.ai, the newsroom, graphs and PKI, hold 62% of all the commits. The median site, among the 46 with content, has seven. And 22 of those 46 have their whole history inside a single day.

That is not a sign of neglect. It is how these sites are made: an idea gets a site in one session, the site does its job, and it is left alone until the idea needs it again. 22 repositories were touched in the last week; 12 have not changed since the end of August. The ones that keep growing are the ones that are used every day: the hub, the newsroom, and the two that hold primitives the others rest on, graphs and PKI.

## Where the pages are

Pages listed in each live site's sitemap, the fourteen largest. The newsroom lists 1,282 and its Portuguese edition 929; sgit.ai 604 and the Gen Z Developers book 496.

Pages tell a slightly different story from commits. The newsroom lists 1,282 pages, and its Portuguese edition, pt.newsroom.sgit.ai, 929, built in 74 commits. The Gen Z Developers book site lists 496 pages from 70 commits in three days. A site that renders a book or a corpus can be large and young at the same time.

## Families, and the naming they need

The families held against the convention agreed on 21 October: plural for the hub, singular for the instance. The twins and hooks families follow it; four provider and game hosts break it; the demo, hook and twin instances are reserved, with no site yet.

The newest thing in the data is families: a hub site, and instance sites under it. There are three kinds of second-level host today:

- **API sites.** api.newsroom, api.send and api.storyboards: a site's client code, released by version.
- **Editions.** pt.newsroom and sgit.newsroom: the same newsroom, in another language or for another audience.
- **Family instances.** elevenlabs and ungovr under providers, what-can-it-do under games, and, reserved, tokens under hook, two demos under demo and aws under twin.

The last kind is where the naming was inconsistent, so on 21 October we fixed a rule: plural for the hub, singular for the instance. [Plural for the family, singular for the site](plural-for-the-family-singular-for-the-site.md) sets it out, with the decisions behind it. Held against the hosts that exist, four live or listed hosts break it, the three provider instances and the game, and the newer families already follow it.

## What it says

- **A site is cheap.** Most were built in one or two sessions. That is why there are 53.
- **Attention concentrates.** Four repositories carry most of the work; the rest are finished, or waiting for their idea to come back.
- **Hubs make families.** Once there are several sites of one kind, they need a hub and a naming rule.
- **The loose ends are few, and visible.** One site not serving, four without a sitemap, seven placeholders, four hosts to rename.

## What this does not claim

- **The counts are of 21 October 2026.** They change with every release.
- **Commits are across all branches.** Including working branches that were later merged.
- **A version in the subject is how release commits are counted.** Not every site marks releases that way.
- **Sitemaps list what a site chooses to list.** Not every file it serves.
- **The version check looked at the usual paths.** A site may publish its version elsewhere.

## Where this comes from

The git history of the 53 `SGit-AI__Website` repositories on GitHub, all branches, and the files at the head of each, fetched on 21 October 2026; each site's home page, `sitemap.xml` and version file, and the DNS of each host, checked the same day. Related: [plural for the family, singular for the site](plural-for-the-family-singular-for-the-site.md), [v0.12 in numbers](v0-12-in-numbers.md), [how a memo becomes a release](how-a-memo-becomes-a-release.md). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Site & engineering[This article as a graph →](graphs.md#the-sgit-ai-sites-in-numbers)

### Builds on

- [Plural for the family, singular for the site: why the AWS site is aws.twin.sgit.ai, the naming rule behind it, and what it changes on the twins and providers sites](plural-for-the-family-singular-for-the-site.md) Why the AWS site is aws.twin.sgit.ai: a twin first, and one naming rule for every family of sites.
- [v0.12 in numbers: 159 releases in eight days, 131 articles, 292,000 words, and what the data says about how an agent-run newsroom works](v0-12-in-numbers.md) v0.12 in numbers: 159 versions in eight days, 131 articles, 292,000 words, a graph for every article, and the mistakes the data shows.
- [How a memo becomes a release: the newsroom's pipeline end to end, what runs in the session and what runs on GitHub, how long each part takes, and what a new session would be missing](how-a-memo-becomes-a-release.md) From voice memo to tagged release: the session's checks, GitHub's checks, the times, what is redundant, and what a new session would lack.

### Continued by

- [Plural for the family, singular for the site: why the AWS site is aws.twin.sgit.ai, the naming rule behind it, and what it changes on the twins and providers sites](plural-for-the-family-singular-for-the-site.md) Why the AWS site is aws.twin.sgit.ai: a twin first, and one naming rule for every family of sites.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 237 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=237)

**Posting this article on LinkedIn?** The cover is [the-sgit-ai-sites-in-numbers.jpg](banners/the-sgit-ai-sites-in-numbers.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-sgit-ai-sites-in-numbers.html)*
