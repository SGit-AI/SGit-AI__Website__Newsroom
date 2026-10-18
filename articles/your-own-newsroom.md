# Your own newsroom: how a founder can tell their story by voice memo, with an agent that checks it and publishes it to GitHub Pages, and readers who pay a little if they find it useful, sgit.ai

> The founders I most want to see succeed are the authentic ones, the people who come from the field they are building for. Their brand is themselves, and they need a medium for it: a place that keeps their history, what they do, their stories, their struggles, their ideas, their path and their milestones, so that they remember it and others can find it. This site is written that way. I record a voice memo, an agent session wired to GitHub researches it, checks every claim, writes it in my voice and publishes it to a static site, and readers pay a few pence a page if they find it useful. Everything needed to do the same exists today. This is the recipe, step by step: one public GitHub repository; GitHub Pages, published by GitHub Actions after a validation step; a Claude plan with cloud sessions and the Claude GitHub App, used from a browser or a phone; a house-rules file the agent reads first; the reader meter from api.newsroom.sgit.ai, pinned to a release, with a Stripe Payment Link you own; and the habits that make it trustworthy: corrections in the open, sources at the end, and nothing confidential in a public repository. It is simpler than this newsroom, and it does not need to be called a newsroom. It is also a good way to learn, in a native way, what publishing a pure client-side site actually means.

*Source: <https://newsroom.sgit.ai/articles/your-own-newsroom.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Your own newsroom: how a founder can tell their story by voice memo, with an agent that checks it and publishes it to GitHub Pages, and readers who pay a little if they find it useful

# Your own newsroom: how a founder can tell their story by voice memo, with an agent that checks it and publishes it to GitHub Pages, and readers who pay a little if they find it useful

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-15 · [article v1.2.0, 3 versions](versions/your-own-newsroom.md) · [newsroom v0.12.80](https://newsroom.sgit.ai/admin/versions.html) · newsroomreplicatevoice-memosgithub-pagesgithub-actionsclaude-codefounderssg-meterpaymentsclient-sidehow-toarticle

***Abstract:** The founders I most want to see succeed are the authentic ones, the people who come from the field they are building for. Their brand is themselves, and they need a medium for it: a place that keeps their history, what they do, their stories, their struggles, their ideas, their path and their milestones, so that they remember it and others can find it. This site is written that way. I record a voice memo, an agent session wired to GitHub researches it, checks every claim, writes it in my voice and publishes it to a static site, and readers pay a few pence a page if they find it useful. Everything needed to do the same exists today. This is the recipe, step by step: one public GitHub repository; GitHub Pages, published by GitHub Actions after a validation step; a Claude plan with cloud sessions and the Claude GitHub App, used from a browser or a phone; a house-rules file the agent reads first; the reader meter from api.newsroom.sgit.ai, pinned to a release, with a Stripe Payment Link you own; and the habits that make it trustworthy: corrections in the open, sources at the end, and nothing confidential in a public repository. It is simpler than this newsroom, and it does not need to be called a newsroom. It is also a good way to learn, in a native way, what publishing a pure client-side site actually means.*

The loop: speak a memo; an agent session connected to one repository researches, writes and checks it; it commits and pushes; GitHub Actions validates and publishes to GitHub Pages; readers read, rate and top up through a payment link you own; and the record grows.

## In short

- **An authentic founder's brand is their story.** It needs a medium that keeps it.
- **The loop is short.** Speak a memo; an agent researches, writes, checks and publishes; readers pay a little if it helps.
- **Everything needed exists today.** GitHub, GitHub Pages, Claude cloud sessions, the reader meter, a Stripe Payment Link.
- **The house rules are the product.** One file the agent reads first: your voice, what to check, what never to publish.
- **It is pure client-side.** Static files on a free host; the reader's balance lives in the reader's browser.
- **A behaviour policy runs the agents.** From the privileges they get to how often you publish and in what tone.
- **Writer, editor, publisher.** Separate agents, separate grants, enforced by prompt or by hook.
- **A private vault beside the public site.** Drafts, data and guidance stay encrypted; only the final text is published.
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
8. **Keep the record.** Every article ends with what it does not claim and where it comes from; a correction is a new version of the article, with its diff, not a note about the old one; every release gets a version and a one-line note.

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
- A correction is a new version: republish the article as it should read now, and let the version history and its diff show what changed. Nothing is silently changed.

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

## A behaviour policy for your agents

The house rules are a start. The next step is to write them as an [Agent Behaviour Policy](https://abp.sgit.ai/what-is-an-abp/index.html): a versioned file that says what the agent is given, what it is for, and what it must not do, with each rule marked by what keeps it. It does two jobs at once, and both matter for a founder.

The first is security. An agent that publishes for you needs real privileges: it can push to your repository, which means it can publish anything to your site. The policy is where you write down exactly what it is granted and what it is not: push to the one repository, never to another; publish from the main branch only after the checks pass; never hold your Stripe keys; never commit a key, a password or a client's name. [A policy beside the prompt](a-policy-beside-the-prompt.md) argued that every agent should take one as an input, and [the policy draws the liability line](the-policy-draws-the-liability-line.md): what the agent was allowed to do is what you are accountable for.

The second is the business logic, and this is where it becomes yours. A behaviour policy is not only a security control; it goes all the way down to how you want the work done. You can write that you do not want more than one post a day; that the tone is warm, plain and first person; that every claim about a client needs their written permission; that nothing goes out on a Sunday; that every article ends with what it does not claim. These are the instructions you would give a new member of staff, written once, in a form an agent can follow and a person can check. [Commander's intent is a behaviour policy](commanders-intent-is-a-behaviour-policy.md) makes the same point from the other end: say what you want achieved and the limits, and let the agent work inside them.

```

# Behaviour policy: my site (v1.0)

## Grant
- Push to github.com/me/my-site, branch main. Nothing else.
- Read my drafts vault. Never write to it without asking.

## Mandate
- Turn my voice memos into articles in my voice, check them, publish them.

## Rules  [barrier: expectation = the agent keeps it, setting = a hook keeps it]
1. At most one new article a day.                        [setting: pre-push hook]
2. Every fact has a source link; correct my memo where it is wrong.   [expectation]
3. Tone: warm, plain, first person; British spelling.    [expectation]
4. Never publish a client's name without written consent. [expectation, checked by the editor]
5. Leak scan before every commit: no keys, no client data. [setting: pre-commit hook]
6. Every release is built and validated before it is pushed. [setting: CI]

```

It also lets you split the work, as this site does, across more than one agent. A **writer** turns the memo into a draft; an **editor** checks it against the rules, the sources and your voice, and can send it back; a **publisher** is the only one granted the push, and only for drafts the editor has passed. Each has its own section of the policy and its own grant, so the agent that writes cannot publish on its own, and the one that publishes cannot invent. This newsroom works the same way, with named agents for writing, the wire and the design, each with its own page; [the agents write too](the-agents-write-too.md) describes them.

The policy is enforced in two ways, and the difference is worth knowing. The simplest is the prompt: the policy is read at the start of every session and summarised on every prompt, which is how this site's own writing session works, under a policy of eleven rules that is re-read after every summary and reports its status every few answers. That keeps the rules in view, but it is still the agent keeping them. The stronger way is a hook: a small program the agent's environment runs before and after each action, which blocks a push on a second article in a day or a commit that contains a key, whatever the agent intended. [Are hooks the sweet spot?](are-hooks-the-sweet-spot.md) moved this site's own policy into hooks, rule by rule, and more than half of its rules could move. Mark each rule by which of the two keeps it, and you know which ones to trust.

## Further: a private vault beside the public site

A more advanced setup keeps everything that should not be public out of the public repository altogether. The repository holds what is published. Beside it, an [sgit](https://sgit.ai/) vault holds the rest: drafts you are not ready to show, transcripts of the interviews the agent ran with you, the data an article was built from, notes about clients, the guidance and examples you want the agent to learn your voice from, and the agent's own working files. A vault is encrypted on your machine before anything is uploaded, versioned like git, and opened only with its key, so the server that stores it cannot read it.

The workflow stays the same, with one more step. The agent session clones the vault with a key you give it through the environment, never in a file in the repository; it writes the draft and its working material into the vault; the editor reads it there; and only when an article is approved does the publisher copy the final text into the public repository. Nothing private ever touches the public history. This is how this site's own writing session keeps its working material: scripts, figures, measurements and reviews in a vault of its own, while only the articles reach the site. And because a vault can publish a read-only key on purpose, you can choose to share a single folder, a data set behind an article, say, without sharing the rest. [Agent workflows on ephemeral vaults](agent-workflows-on-ephemeral-vaults.md) goes further, with seven architectures from one agent to a swarm.

## What it is like to run

On this site, in three days, 54 messages from me, ten of them voice memos, became 40 releases, each with figures, sources and a section on what it does not claim. The memo is a draft of a thought; the article is the thought, checked. Two habits make the biggest difference. Ask the agent to interview you when a story is thin: a session acting as a journalist, challenging every answer, is how [Ten hard questions for RiskMandate](riskmandate-ten-questions.md) was written. And let the record build on itself: every article links to the ones before it, so the history is not a list of posts but a map of the path, which is what [Omnichannel programming](omnichannel-programming.md) means by one shared state.

## What this does not claim

- **The writing pipeline is not a kit yet.** This site's generator and release steps are published as a pattern; the brief above has the agent build a smaller one.
- **The meter trusts the reader.** Balances can be edited, and the return page does not verify a payment, both by design.
- **Costs vary.** GitHub Pages is free within its limits; a Claude plan, a domain and Stripe's fees are not.
- **A public repository is public.** On a free plan, Pages needs it; nothing confidential belongs in it.
- **A rule in a prompt is a hope.** Only the rules a hook or CI keeps are enforced; mark which is which.
- **Updated on 15 October.** Added the behaviour policy and the private vault.

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
- [A policy beside the prompt: a proposal that every agent takes a behaviour policy as an input, with enforcement and liability attached, and why aviation and payments say the vendors should want it](a-policy-beside-the-prompt.md) A proposal: every agent takes a behaviour policy beside its prompt, which the vendor accepts and answers for, as aviation and payments learned to.
- [The policy draws the liability line: an answer to Ralf Thomas on agent accountability, and why every agent in a loop should take a behaviour policy beside its prompt](the-policy-draws-the-liability-line.md) An answer to Ralf Thomas: the shell game works because nothing is written down, and a behaviour policy's explicit prohibitions move the liability line.
- [Commander's intent is a behaviour policy: Sondera's argument in our words, the business layer above it, and five of our rules compiled to Cedar and tested](commanders-intent-is-a-behaviour-policy.md) Sondera's commander's intent and our behaviour policies are one idea: twelve terms joined, the business layer above, and five rules tested in Cedar.
- [The agents write too: lessons, debriefs and a page for every agent on the newsroom, and a brief for the conductor that will keep it](the-agents-write-too.md) The newsroom's agents get their own bylines: lessons every agent loads, debriefs as source material, a page for every agent, and a conductor.
- [Are hooks the sweet spot? Moving an agent's rules from hope into hooks, rule by rule, until enforcement moves off the machine](are-hooks-the-sweet-spot.md) One agent's eleven rules, moved from the prompt into hooks and tested: four fully, two mostly, three partly, two not at all, and a gap in the leak scan.
- [Agent workflows on ephemeral vaults: seven architectures from one agent to a swarm, a repository of recipes that gates sgit's releases, and what a hundred writers did to an append lane](agent-workflows-on-ephemeral-vaults.md) Seven architectures for agents on ephemeral vaults, a recipe repository that gates sgit's releases, and a hundred writers measured on an append lane.
- [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](riskmandate-ten-questions.md) Ten hard questions from a conference, answered in a two-hour interview: what RiskMandate does, what it deliberately is not, and how mature each part is.
- [Omnichannel programming: briefs by voice, reviews by voice, previews on the phone, and one shared state underneath, at every stage from explorer to town planner](omnichannel-programming.md) Programming by voice, chat, phone, IDE and pull request, with one shared state underneath, at every stage from explorer to town planner. This site, counted.

### Continued by

- [Three companies, three LinkedIn pages: the brief, the drafts and the first posts, in the open](three-linkedin-pages.md) Three companies, no LinkedIn pages: the decisions, every drafted field with its count, thirty first posts already written, and a new profile, in the open.
- [Research, delivered as a vault: what companies that sell research could do with fractal graphs, behaviour policies for AI-enabled products, and evaluations run by a governed agent hive](research-delivered-as-a-vault.md) Companies that sell research could deliver it as a vault: evidence, a fractal graph, briefings per reader, behaviour policies for AI products, a lane back.
- [Explorer coding: a better name for what people call vibe coding, what it is good for, and the handover to villagers and town planners before anyone depends on it](explorer-coding.md) Call it explorer coding, not vibe coding: the best thing since the spreadsheet, the best brief there is, and not ready to be in line until villagers take it.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 138 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=138)

**Posting this article on LinkedIn?** The cover is [your-own-newsroom.jpg](banners/your-own-newsroom.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/your-own-newsroom.html)*
