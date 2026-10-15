# Your own newsroom: how a founder can tell their story by voice memo, with an agent that checks it and publishes it to GitHub Pages, and readers who pay a little if they find it useful, sgit.ai

> The founders I most want to see succeed are the authentic ones, the people who come from the field they are building for. Their brand is themselves, and they need a medium for it: a place that keeps their history, what they do, their stories, their struggles, their ideas, their path and their milestones, so that they remember it and others can find it. This site is written that way. I record a voice memo, an agent session wired to GitHub researches it, checks every claim, writes it in my voice and publishes it to a static site, and readers pay a few pence a page if they find it useful. Everything needed to do the same exists today. This is the recipe, step by step: one public GitHub repository; GitHub Pages, published by GitHub Actions after a validation step; a Claude plan with cloud sessions and the Claude GitHub App, used from a browser or a phone; a house-rules file the agent reads first; the reader meter from api.newsroom.sgit.ai, pinned to a release, with a Stripe Payment Link you own; and the habits that make it trustworthy: corrections in the open, sources at the end, and nothing confidential in a public repository. It is simpler than this newsroom, and it does not need to be called a newsroom. It is also a good way to learn, in a native way, what publishing a pure client-side site actually means.

*Source: <https://newsroom.sgit.ai/articles/your-own-newsroom.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Your own newsroom: how a founder can tell their story by voice memo, with an agent that checks it and publishes it to GitHub Pages, and readers who pay a little if they find it useful

# Your own newsroom: how a founder can tell their story by voice memo, with an agent that checks it and publishes it to GitHub Pages, and readers who pay a little if they find it useful

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-15 · [article v1.0.0](versions/your-own-newsroom.md) · [newsroom v0.12.68](https://newsroom.sgit.ai/admin/versions.html) · newsroomreplicatevoice-memosgithub-pagesgithub-actionsclaude-codefounderssg-meterpaymentsclient-sidehow-toarticle

***Abstract:** The founders I most want to see succeed are the authentic ones, the people who come from the field they are building for. Their brand is themselves, and they need a medium for it: a place that keeps their history, what they do, their stories, their struggles, their ideas, their path and their milestones, so that they remember it and others can find it. This site is written that way. I record a voice memo, an agent session wired to GitHub researches it, checks every claim, writes it in my voice and publishes it to a static site, and readers pay a few pence a page if they find it useful. Everything needed to do the same exists today. This is the recipe, step by step: one public GitHub repository; GitHub Pages, published by GitHub Actions after a validation step; a Claude plan with cloud sessions and the Claude GitHub App, used from a browser or a phone; a house-rules file the agent reads first; the reader meter from api.newsroom.sgit.ai, pinned to a release, with a Stripe Payment Link you own; and the habits that make it trustworthy: corrections in the open, sources at the end, and nothing confidential in a public repository. It is simpler than this newsroom, and it does not need to be called a newsroom. It is also a good way to learn, in a native way, what publishing a pure client-side site actually means.*

The loop: speak a memo; an agent session connected to one repository researches, writes and checks it; it commits and pushes; GitHub Actions validates and publishes to GitHub Pages; readers read, rate and top up through a payment link you own; and the record grows.

## In short

- **An authentic founder's brand is their story.** It needs a medium that keeps it.
- **The loop is short.** Speak a memo; an agent researches, writes, checks and publishes; readers pay a little if it helps.
- **Everything needed exists today.** GitHub, GitHub Pages, Claude cloud sessions, the reader meter, a Stripe Payment Link.
- **The house rules are the product.** One file the agent reads first: your voice, what to check, what never to publish.
- **It is pure client-side.** Static files on a free host; the reader's balance lives in the reader's browser.
- **Honest about the gaps.** The writing pipeline is a pattern to copy, not yet a kit.

## Why a founder needs one

When you go into the whole entrepreneur flow, the thing that matters most for some founders is not the deck; it is that they are the real deal. [The expert founders](the-expert-founders.md) argued that the next generation of companies will be built by people who come from the field. For them, the brand is the founder: their authenticity is the proof.

That brand needs a medium. A founder has to remember their own history, and needs a way to capture what they do as they do it: the stories, the struggles, the ideas, the path, the milestones. Most of it is lost in calls and chats. A site written from voice memos keeps it, with dates, and because every claim is checked before it is published, it is a record that others can trust. I found out on this site that [my own memory needs checking](my-memory-checked.md); a founder's does too, and it is better to find out before an investor does.

And there is a second reason. Building one teaches what a pure client-side site is: static files on a host, code that runs in the reader's browser, and no server that holds anyone's data. For a founder moving their own product in that direction, publishing their story this way is the most native way to learn it.

## What you need

What you need, what it costs, and what is ready: a public GitHub repository, GitHub Pages published by GitHub Actions, a Claude plan with cloud sessions and the Claude GitHub App, a recorder that transcribes, house rules, the reader meter from api.newsroom.sgit.ai, a Stripe Payment Link; the writing pipeline as one package is not ready yet.

- **A GitHub account and one repository.** GitHub Pages is free, with one condition that matters: "If the account that owns the repository uses GitHub Free or GitHub Free for organizations, the repository must be public." [GitHub's limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) are generous for a writing site: "Published GitHub Pages sites may be no larger than 1 GB", with "a *soft* bandwidth limit of 100 GB per month."
- **A Claude plan with cloud sessions.** [Cloud sessions](https://code.claude.com/docs/en/claude-code-on-the-web) "are available on Pro, Max, and Team plans", and run from the browser at claude.ai/code or from the Code tab of the Claude app on a phone. They need GitHub connected; the Claude GitHub App gives them "Any public repository, and private repositories that the Claude GitHub App is installed on".
- **A way to record and transcribe.** Any app that turns a voice memo into text. I use Otter; the order you said things in, and the words you reached for, are the raw material for your voice.
- **A Stripe account and a Payment Link.** The top-up page sends the reader to it; your site never sees card details.
- **Optionally, a domain.** GitHub Pages serves `<you>.github.io` until you add one.

## Step by step

1. **Create the repository and turn on Pages.** A new public repository, a README, and in Settings, Pages, choose GitHub Actions as the source. [GitHub's guide](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site) covers it in five steps.
2. **Add a workflow that validates before it publishes.** This site's [deploy workflow](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/.github/workflows/deploy-pages.yml) is the pattern: validate, then tag the release, then deploy. A small version is below. The rule that matters is that a failed check stops the release.
3. **Write the house rules.** One file at the root, `CLAUDE.md`, which Claude Code reads at the start of every session. A template is below. This is where your voice, your verification rules and your release steps live, and it grows by one line every time you correct the agent.
4. **Connect a cloud session to the repository.** At claude.ai/code, connect GitHub, choose the repository, and start a session. From then on you can do the same from your phone.
5. **Give it the first brief.** Paste the brief below. The agent sets up the folders, the article template, a small build script that turns Markdown into pages, and a validator, and publishes a first page about you.
6. **Record, paste, review.** Record a memo, paste the transcript into the session, and read what comes back on your phone. Correct it by voice. The agent changes it, rebuilds, validates, pushes, and checks the live page.
7. **Add the meter.** When there is something worth paying for, add the reader meter (next section).
8. **Keep the record.** Every article ends with what it does not claim and where it comes from; corrections are added in the open, dated; every release gets a version and a one-line note.

The workflow, small enough to read:

```

name: deploy-pages
on:
  push:
    branches: [main]
permissions:
  contents: read
  pages: write
  id-token: write
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
- uses: actions/checkout@v4
- run: python3 build/validate.py
  deploy:
    needs: validate
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
- uses: actions/checkout@v4
- uses: actions/configure-pages@v5
- uses: actions/upload-pages-artifact@v3
        with:
          path: site
- id: deployment
        uses: actions/deploy-pages@v4

```

## The house rules

The file the agent reads first is what turns a general model into your writer. This site's version grew from [every mistake that added a rule](every-mistake-added-a-rule.md), and [How the voice works](how-the-voice-works.md) explains why the voice comes from the memos, not from a setting. A starting point:

```

# House rules

## Who I am
[Two paragraphs: your field, your years in it, what you are building and for whom.]

## The voice
- Write as me, in the first person, from my voice memos, keeping my order and my phrases.
- Plain words. British spelling. No em-dashes. Never overstate.

## Before writing
- Check every fact, number, name and date against a source. Link it.
- Where my memo is wrong, correct it and say so in the article.
- Mark what exists, what is planned, and what is only my recollection.

## Never publish
- Anything confidential: client names, case details, transcripts, contracts,
  private messages, personal data. This repository is public.
- Keys, passwords or tokens. Scan the staged diff before every commit.

## Every article
- A title, a summary, "In short", the argument in sections,
  "What this does not claim", and "Where this comes from".
- Corrections are added at the end, dated. Nothing is silently changed.

## Every release
1. Build and validate. Stop on any failure.
2. Bump the version and add a one-line release note.
3. Commit, push, and check the live page loads.

```

And the first brief, to paste into the first session:

```

Set up this repository as my personal site, written from my voice memos.
Read CLAUDE.md first and follow it. Create: content/articles/ for Markdown
articles with front matter; build/build.py to render them into site/ as
static HTML with an index, an about page and an RSS feed; build/validate.py
to check links, front matter and that no secret-looking string is in site/;
and the GitHub Actions workflow in .github/workflows/. Then write the first
article from the memo below, build, validate, commit, push, and tell me
the live URL once it loads.

```

## Readers who pay a little

The payment side is already packaged, at [api.newsroom.sgit.ai](https://api.newsroom.sgit.ai/). It is a client-side API: versioned files a site loads and pins, which run "in the reader's browser, with no server of ours". The reader starts with credit, pays a few pence a page by how far they read, rates the page, and the rating moves the price; [for publishers](https://api.newsroom.sgit.ai/for-publishers/) the defaults are "£5 of credit to begin", 5p an article and 10p when new. Top-ups go through "a Stripe Payment Link you own". The [developer quick start](https://api.newsroom.sgit.ai/for-developers/) puts it on a page with a config and one import, pinned to a release:

```

<sg-meter view="balance"></sg-meter>
<sg-meter view="page" kind="article" date="2026-10-15" title="The page's title"></sg-meter>
<script type="application/json" id="sg-meter-config">
{"storageKey": "mysite.meter.v1", "start": 500, "symbol": "£",
 "prices": {"article_new": 10, "article": 5, "page": 1, "free": 0},
 "topup": {"amount": 500, "link": ""}}
</script>
<script>
  const release = 'https://api.newsroom.sgit.ai/v0.2.5/';  // the pinned release: change it in one place
  import(release + 'assets/components/sg-meter/v1/v1.4/v1.4.0/sg-meter.js');
</script>

```

Put your own Stripe Payment Link in `topup.link`; while it is empty, no money moves. It is an honesty box, not a paywall: it never blocks a page, and because the balance is in the reader's browser, a reader can change it. That is the deliberate trade, explained in [paying after the value](paying-after-the-value.md): people who find it useful pay a little, and nobody is kept out. The same release also has reading lists in a link, personas, search and an encrypted vault for readers who want to carry their account between devices; add them when they are useful.

One condition to know. GitHub says Pages "is not intended for or allowed to be used as a free web-hosting service to run your online business", or a site "primarily directed at either facilitating commercial transactions or providing commercial software as a service". A writing site with an optional meter is primarily writing; if yours becomes primarily a shop, move it to a host that allows that. The files are static, so they move anywhere.

## What it is like to run

On this site, in three days, 54 messages from me, ten of them voice memos, became 40 releases, each with figures, sources and a section on what it does not claim. The memo is a draft of a thought; the article is the thought, checked. Two habits make the biggest difference. Ask the agent to interview you when a story is thin: a session acting as a journalist, challenging every answer, is how [Ten hard questions for RiskMandate](riskmandate-ten-questions.md) was written. And let the record build on itself: every article links to the ones before it, so the history is not a list of posts but a map of the path, which is what [Omnichannel programming](omnichannel-programming.md) means by one shared state.

## What this does not claim

- **The writing pipeline is not a kit yet.** This site's generator and release steps are published as a pattern; the brief above has the agent build a smaller one.
- **The meter trusts the reader.** Balances can be edited, and the return page does not verify a payment, both by design.
- **Costs vary.** GitHub Pages is free within its limits; a Claude plan, a domain and Stripe's fees are not.
- **A public repository is public.** On a free plan, Pages needs it; nothing confidential belongs in it.

If you want help setting one up for your own story, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 15 October 2026, written by this site's agent in the voice of this site; the argument and the editorial responsibility are mine. The recipe is this site's own: its [repository](https://github.com/SGit-AI/SGit-AI__Website__Newsroom), its [deploy workflow](https://github.com/SGit-AI/SGit-AI__Website__Newsroom/blob/dev/.github/workflows/deploy-pages.yml) and its [Replicate](https://newsroom.sgit.ai/replicate/index.html) page. [api.newsroom.sgit.ai](https://api.newsroom.sgit.ai/), its [page for publishers](https://api.newsroom.sgit.ai/for-publishers/), its [developer quick start](https://api.newsroom.sgit.ai/for-developers/) and [its source](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__API), release v0.2.5; GitHub Docs, [Creating a GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site) and [GitHub Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits); Claude Code Docs, [Use Claude Code in the cloud](https://code.claude.com/docs/en/claude-code-on-the-web). Read on 15 October 2026.

## Threads

Site & engineeringStartups & strategy[This article as a graph →](graphs.md#your-own-newsroom)

### Builds on

- [The expert founders: why the next startups will be built by the people who know the problem, and why Europe's slower, sceptical money suits them](the-expert-founders.md) Agents make execution cheap, so the people who know the problem can build first. The data favours experts, and Europe's sceptical money suits them.
- [My memory, checked: thinking out loud in a voice memo, publishing only what the record supports, and why peer review has moved to before publishing](my-memory-checked.md) I say it as I remember it; the agent checks it against the record before anyone reads it. Five confirmed, five corrected, two not found.
- [Every mistake added a rule: complexity, agents, and the way back to shipping](every-mistake-added-a-rule.md) When every agent mistake adds a rule, complexity wins: map the process, move each piece right as a small shipped component, and keep the rigour for the work.
- [How the voice works: why these articles sound like me, with a section in which Claude explains it from its side](how-the-voice-works.md) Why these articles sound like their author: a corpus, the voice memos, seven wording rules and a reader who corrects, with Claude explaining it from its side.
- [Paying after the value: why a balance that can go negative feels different from a subscription, the psychology behind it, and the experiment this newsroom is running](paying-after-the-value.md) Most purchases are bets on future value; a reading balance that can go negative asks for payment when the value is already in view.
- [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](riskmandate-ten-questions.md) Ten hard questions from a conference, answered in a two-hour interview: what RiskMandate does, what it deliberately is not, and how mature each part is.
- [Omnichannel programming: briefs by voice, reviews by voice, previews on the phone, and one shared state underneath, at every stage from explorer to town planner](omnichannel-programming.md) Programming by voice, chat, phone, IDE and pull request, with one shared state underneath, at every stage from explorer to town planner. This site, counted.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 138 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=138)

**Posting this article on LinkedIn?** The cover is [your-own-newsroom.jpg](banners/your-own-newsroom.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/your-own-newsroom.html)*
