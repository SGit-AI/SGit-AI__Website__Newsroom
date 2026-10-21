# How a memo becomes a release: the newsroom's pipeline end to end, what runs in the session and what runs on GitHub, how long each part takes, and what a new session would be missing, sgit.ai

> Every article on this site starts as a voice memo and ends as a tagged release on GitHub Pages. In between there are two sets of checks. In the session, the newsroom's writer agent researches, writes and builds: it runs sgit.ai's generator and validator through publish.py, this site's own builders and validator, the 18 tests, a phone-width check, and a leak scan of what it is about to commit. Then, on GitHub, Actions validate the site again, run the 18 tests again, tag the release and deploy it. After v0.13.7, a release that adds no new article takes about 400 seconds in the session and about 290 on GitHub, down from about 750 and 640; a release with a new article still takes about 720 in the session, because a new card and banner need all three of sgit.ai's page builds. This article documents all of it, with the times, and asks two questions about it. First, what is redundant: the 15 browser tests run in both places, and I propose they run only on GitHub unless the change is to the site's code, which would save almost three minutes in the session on every article release. Second, what a new session would have: the repository holds the builders, the tests, the workflow and the writing rules, but the release script, the graph writer, the figure helpers, the phone-width check, the session's behaviour policy and the leak scan live only in this session's container, and a new one would not have them.

*Source: <https://newsroom.sgit.ai/articles/how-a-memo-becomes-a-release.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / How a memo becomes a release: the newsroom's pipeline end to end, what runs in the session and what runs on GitHub, how long each part takes, and what a new session would be missing

# How a memo becomes a release: the newsroom's pipeline end to end, what runs in the session and what runs on GitHub, how long each part takes, and what a new session would be missing

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-21 · [article v1.0.0](versions/how-a-memo-becomes-a-release.md) · [newsroom v0.13.8](https://newsroom.sgit.ai/admin/versions.html) · newsroomengineeringciagentspipelinearticle

***Abstract:** Every article on this site starts as a voice memo and ends as a tagged release on GitHub Pages. In between there are two sets of checks. In the session, the newsroom's writer agent researches, writes and builds: it runs sgit.ai's generator and validator through publish.py, this site's own builders and validator, the 18 tests, a phone-width check, and a leak scan of what it is about to commit. Then, on GitHub, Actions validate the site again, run the 18 tests again, tag the release and deploy it. After v0.13.7, a release that adds no new article takes about 400 seconds in the session and about 290 on GitHub, down from about 750 and 640; a release with a new article still takes about 720 in the session, because a new card and banner need all three of sgit.ai's page builds. This article documents all of it, with the times, and asks two questions about it. First, what is redundant: the 15 browser tests run in both places, and I propose they run only on GitHub unless the change is to the site's code, which would save almost three minutes in the session on every article release. Second, what a new session would have: the repository holds the builders, the tests, the workflow and the writing rules, but the release script, the graph writer, the figure helpers, the phone-width check, the session's behaviour policy and the leak scan live only in this session's container, and a new one would not have them.*

From a memo to a release, in three stages: writing in the session, checking in the session, and shipping on GitHub. A failed leak scan sends the work back to the first stage.

## In short

- **An article starts as a voice memo.** Transcribed, pasted into the writer's session, researched and written up.
- **The session checks it before anything is pushed.** Wording, summaries, sgit.ai's generator, this site's builders, 18 tests, phone width, a leak scan.
- **GitHub checks it again.** Validation and the 18 tests, side by side, then a tag and a deploy.
- **About 400 seconds in the session and 290 on GitHub.** For a release with no new article; a new article, about 720.
- **The 15 browser tests run twice.** They could run only on GitHub, unless the site's code changed.
- **The repository holds the builders, tests, workflow and rules.** The release script, helpers and leak scan do not live there.
- **A new session would not have them yet.** Moving them into the repository is the next step.

## From voice to article

It starts with my voice. I record a memo, Otter.ai transcribes it, and I paste the transcript into the session of the newsroom's writer, the agent that writes as newsroom.writer. Sometimes there is a brief or a document with it.

The writer reads the record first: the earlier articles the new one builds on, the briefs, and the sites involved. Then it researches outside, with web search and fetch, and keeps the primary sources and their dates. Facts are checked, counts are made by a script, and quotes are copied word for word.

Then it writes. An article is a set of files in `admin/content/articles/`: the article itself in Markdown; its figures in `images/`, drawn by small Node scripts that turn SVG into WebP; a graph of its argument in `graphs/`, with ten to fifteen nodes and two quotes that must appear word for word in the text; and a summary of every section in `summaries/`, a line and a paragraph each. The shape, the voice and the wording rules are written down in the articles README: no em-dashes, British spelling, no judging the reader, and a list of words not to use.

## The checks in the session

Before anything is committed, the writer runs a sequence of checks, in this order. Each one stops the release if it fails.

- **Wording and summaries.** `wording.py` looks for superlatives and phrases the guide rules out; `summaries.py --check` confirms every section has a summary and none is stale.
- **sgit.ai's generator and validator, through `publish.py`.** The site's article pages are still made by sgit.ai's generator, borrowed without changing sgit.ai. `publish.py` clones a read-only checkout of sgit.ai, replays this site's 135 commits of articles into the clone so each article keeps its history and versions, draws the link-preview cards and banners, runs the generator, runs sgit.ai's own validator, and imports the result.
- **This site's builders.** Thirty-odd Python builders, from the front page and the sections to the search index, the sitemap and the full-text file for agents.
- **`validate.js`.** This site's validator: structure, links, version numbers, canonical addresses, and a tripwire for anything shaped like a key.
- **The 18 tests.** `run_tests.sh` runs them side by side: 15 drive the reader's side of the site in Chromium (the meter, the reading lists, the notes, the wire, search, the passkey lab), and 3 run in Node. The two that measure timing run alone, afterwards.
- **The phone width.** Each new page is opened at 390 pixels wide, and must not scroll sideways.
- **The leak scan.** On the staged diff, before every commit: no local or key paths, nothing shaped like a secret, none of the session's own keys or passphrases, none of the names on a private list, and no em-dash added. It is gated on its exit code: if it fails, nothing is committed.

Then the commit, named `site vX.Y.Z: @newsroom.writer: <title>`, and the push to `dev`, but only after checking that `dev` on GitHub has not moved since the build.

## The checks on GitHub

A push to `dev` starts the workflow in `.github/workflows/deploy-pages.yml`. Two jobs run side by side: `validate`, which runs `validate.js` again, and `reader-tests`, which installs Chromium, cached between runs, and runs the same 18 tests, four at a time. When both pass, `tag-release` checks that the version in `version.txt` matches the commit and is the next one, and tags it. Then `deploy` publishes the site to GitHub Pages. If either check fails, nothing is tagged and nothing is deployed.

The jobs on GitHub. A push to dev validates, tests, tags and deploys. A pull request into main must be a major. A push to main checks the major, tags it if needed, publishes a GitHub Release and deploys.

Majors take a different path. A release that bumps to the next `.0`, such as v0.13.0, goes from `dev` to `main` by pull request: `major-gate` refuses anything but a major with its release note, and on the merge `major-release` makes sure the tag exists and publishes a GitHub Release. Pull requests run in their own queue, so their checks no longer cancel a release in progress, which is what happened to v0.13.0.

After the push, the writer polls the live `version.txt` until the new version appears, then checks that the new page answers. I read it once it is live, and a correction is a new version, with its own page of changes.

## How long each part takes

Measured on v0.13.7, which added no article, the session's part took about 402 seconds and GitHub's about 291. Before v0.13.7 they took about 747 and 636. A release that adds an article is slower in the session: this article's own release took about 720 seconds, because a new article needs a new card and banner, and then all three of sgit.ai's page builds still run.

One release, in seconds. In the session, the 18 tests are the longest step, then the cards and banners and sgit.ai's page build. On GitHub, the tests again.

In the session, the cards and banners take about 74 seconds, sgit.ai's page build about 90, this site's builders and validator about 40, and the tests about 170. On GitHub, the tests take about 174 seconds of the 291, and the rest is starting the jobs, installing, tagging and deploying. The writing itself, the research, the figures and the graph, is not in these numbers; it is most of the time an article takes.

v0.13.7 halved both by running the tests side by side, by building sgit.ai's pages once instead of three times when no card or cover is new, by caching Chromium on GitHub, and by pushing only new tags. For a new article, only the parallel tests help, which is why the next step matters.

## What runs where, and what lasts

Not all of this lives in the same place, and that matters for what happens when this session ends.

Where each part lives. The builders, tests, workflow and writing rules are in the repository. The release script, graph writer, figure helpers and width check exist only in this session; the behaviour policy and the leak scan only in this container.

- **In the repository, and lasting.** The 47 builders in `admin/build/`, including `publish.py`, `validate.js`, `wording.py` and `summaries.py`; the 18 tests and `run_tests.sh`; the workflow; and the articles README, with the voice, the shape, the run and the checklist.
- **On GitHub.** The Actions runs, the tags, the GitHub Releases and the published site.
- **Only in this session.** The script that runs the builders in order, which is a longer list than the README's; the graph writer, which also checks that the quotes are word for word and the teaser is short enough; the figure scripts and the header they share; the phone-width check; the Node packages the figures and tests need; and the vault tools.
- **Only in this container.** The session's Agent Behaviour Policy, its hooks (the status report every few answers, the re-anchoring after the context is compacted), and the leak scan with its private lists.
- **Read only.** A checkout of sgit.ai, for its generator, with pushing turned off.

## What is redundant

The 15 browser tests run twice: once in the session, about 170 seconds, and once on GitHub. Running them in the session catches a failure before the push; running them on GitHub catches it before the deploy. Either is enough to stop a broken release reaching readers, because nothing is tagged or deployed until GitHub's tests pass.

So I propose that the session runs only what only the session can check, and leaves the heavy, repeatable checks to GitHub:

- **In the session:** wording and summaries; `publish.py`, which makes the pages; the builders and `validate.js`; the 3 Node tests, under ten seconds; the phone width of new pages; and the leak scan, which needs the private lists and must run before the commit.
- **On GitHub:** `validate.js` and the 15 browser tests, then the tag and the deploy.
- **Both, when the code changes.** A change to `assets/` or `admin/build/` is a change to what the browser tests test, so then the session runs them too.
The proposed split: the session runs what only it can check, about 4 minutes; GitHub runs the browser tests, about 5. A change to the site's code runs the browser tests in the session too.

That would take about 165 seconds off every release in the session, from about 720 to about 555 for a new article and from about 400 to about 235 for anything else, while every release is still tested in full before it is deployed. The cost is that a browser test failing on GitHub is found after the push, so the fix is the next version rather than the same one. For an article release, which does not change what those tests test, that should be rare.

`validate.js` also runs twice, but it takes about six seconds, and the session needs it before the commit, so it stays in both.

## What a new session would have

If you started a new session tomorrow and said "you are the newsroom's writer", it would have everything in the repository and on GitHub. GitHub's checks would be exactly the same, because they come from the workflow in the repository.

The session's checks would not be the same. A new session would have to rebuild the release script from the README, whose list of builders is shorter and in a different order; install the Node packages for figures and tests; clone sgit.ai with pushing turned off; and write its own graph writer, figure helpers and phone-width check. Most of that it could work out, and none of it is secret.

Two things matter more. The leak scan and the session's behaviour policy are not in the repository at all. GitHub's `validate.js` would still catch anything shaped like a key, but not the names on the private list, and not a secret that does not look like one. And the behaviour policy, the rules this session works under, would be gone until someone wrote it again.

So the next step is to move into the repository everything that can be shared: the release script, as `admin/build/release.sh`, using `run_tests.sh`; the graph writer and the phone-width check; the figure helper; a setup script for the packages and the sgit.ai checkout; the leak scan's code; and a start-here page for the writer, linked from the README. What must stay private, the list of names and the keys, stays outside the repository, read from the environment or a local file, with the scan refusing to run without it. The session's behaviour policy can be published too, as a policy for the writer's role; it is the kind of thing this site argues every agent should have.

## What this does not claim

- **The times are two releases'.** v0.13.7 and v0.13.8, measured on 21 October 2026; they vary by a few seconds.
- **The split is a proposal.** The session still runs all 18 tests today.
- **Moving the tools is not done yet.** The repository does not have them today.
- **The writing time is not measured.** Only the checks and the deploy.
- **The private lists stay private.** This article says what they are for, not what is in them.

## The diagrams, as source

The diagrams above are Mermaid, rendered for this page. Here is their source, to reuse or correct.

```

flowchart TB
  subgraph W["1 · Write, in the session"]
    direction LR
    A["Dinis records<br/>a voice memo"] --> B["transcribed by Otter.ai,<br/>pasted into the session"]
    B --> C["read the record: earlier<br/>articles, briefs, the sites"]
    C --> D["research outside:<br/>primary sources, dated"]
    D --> E["write the article, figures,<br/>graph, section summaries"]
  end
  subgraph K["2 · Check, in the session"]
    direction LR
    F["wording.py,<br/>summaries.py --check"] --> G["publish.py: sgit.ai's<br/>generator and validator"]
    G --> H["this site's builders,<br/>validate.js"]
    H --> I["18 tests,<br/>run_tests.sh"]
    I --> J["phone width,<br/>390 px"]
    J --> L{"leak scan:<br/>if it fails, back to 1"}
  end
  subgraph G2["3 · Ship, on GitHub"]
    direction LR
    M["commit,<br/>push to dev"] --> N["Actions: validate and<br/>reader-tests, side by side"]
    N --> P["tag-release<br/>vX.Y.Z"] --> Q["deploy to<br/>GitHub Pages"]
    Q --> R["the writer polls<br/>version.txt until live"]
    R -.->|a major| T["PR to main: major-gate,<br/>major-release, deploy"]
  end
  W --> K --> G2

```

```

flowchart LR
  push["push to dev"] --> v["validate<br/>6 s"]
  push --> t["reader-tests<br/>3 min 25 s"]
  v --> tag["tag-release<br/>26 s"]
  t --> tag
  tag --> d["deploy<br/>35 s"]
  pr["pull request into main"] --> mg["major-gate:<br/>a .0 major only"]
  pr --> v2["validate"]
  pr --> t2["reader-tests"]
  main["push to main"] --> v3["validate"] --> mr["major-release:<br/>tag, GitHub Release"] --> d2["deploy"]

```

```

gantt
  title A release after v0.13.7, in seconds from the start
  dateFormat X
  axisFormat %s
  section Local build (402 s)
  clone and replay sgit.ai        : 0, 25
  cards and banners               : 25, 99
  sgit.ai page build, once        : 99, 189
  this site's builders, validate  : 189, 229
  18 tests, 6 at a time           : 229, 402
  section CI on dev (291 s)
  validate                        : 0, 15
  install Playwright, cached      : 0, 37
  18 tests, 4 at a time           : 37, 211
  tag-release                     : 220, 251
  deploy                          : 251, 291

```

```

flowchart LR
  subgraph EPH["Session only (scratchpad)"]
    e1["release.sh: the builder list and order"]
    e2["gw.py: writes and checks graph JSON"]
    e3["figure scripts and their header"]
    e4["sw.mjs: the 390 px width check"]
    e5["node_modules: sharp, playwright, jsqr"]
    e6["vault tools, vault write keys"]
  end
  subgraph CON["This container (~/.claude)"]
    c1["ABP.md: the session's policy"]
    c2["abp.py hooks: prompt, stop, re-anchor"]
    c3["leakscan.sh, deny-names.txt"]
  end
  subgraph REPO["The newsroom repository"]
    r1["admin/build: 47 builders, publish.py,<br/>validate.js, wording.py, summaries.py"]
    r2["run_tests.sh and 18 test_*.mjs"]
    r3["articles README: the voice, the run,<br/>the checklist"]
    r4[".github/workflows/deploy-pages.yml"]
  end
  subgraph GH["GitHub"]
    g1["Actions: validate, reader-tests,<br/>tag-release, deploy, major-gate, major-release"]
    g2["tags and GitHub Pages"]
  end
  subgraph EXT["Read only"]
    x1["sgit.ai checkout:<br/>its generator and validator"]
  end
  e1 --> r1
  e1 --> r2
  x1 --> r1
  c3 -.->|"before every commit"| r1
  r4 --> g1 --> g2

```

```

flowchart TB
  subgraph L["Session · about 4 min"]
    direction LR
    l1["wording.py,<br/>summaries.py --check"] --> l2["publish.py:<br/>makes the pages"] --> l3["builders,<br/>validate.js"] --> l4["3 Node tests,<br/>under 10 s"] --> l5["phone width<br/>of new pages"] --> l6{"leak scan,<br/>private lists"}
  end
  subgraph C["GitHub · about 5 min"]
    direction LR
    c1["validate.js"] --> c2["15 browser tests,<br/>4 at a time"] --> c3["tag, then deploy:<br/>only if both pass"]
  end
  X["a change to assets/ or admin/build/:<br/>run the browser tests in the session too"]
  L --> C
  X -.-> L

```

## Where this comes from

A voice memo of 21 October 2026. The repository's `admin/build/` scripts, `run_tests.sh`, `.github/workflows/deploy-pages.yml` and the articles README; the timings of a release measured step by step in the session, and of GitHub's run for v0.13.7, read from its jobs; and an inventory of the session's scratchpad and container. Related: [v0.12 in numbers](v0-12-in-numbers.md), [a leak without breaking the policy](a-leak-without-breaking-the-policy.md), [hooks are kernel code](hooks-are-kernel-code.md), [the RiskMandate roadmap](the-riskmandate-roadmap.md). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Site & engineering[This article as a graph →](graphs.md#how-a-memo-becomes-a-release)

### Builds on

- [v0.12 in numbers: 159 releases in eight days, 131 articles, 292,000 words, and what the data says about how an agent-run newsroom works](v0-12-in-numbers.md) v0.12 in numbers: 159 versions in eight days, 131 articles, 292,000 words, a graph for every article, and the mistakes the data shows.
- [Can a key leak without breaking the policy? Told, checked, never given: three levels for secrets and personal data, and a hook we tested against nine leaks](a-leak-without-breaking-the-policy.md) A key can leak through an allowed action. Told, checked, never given: a hook tested on nine leaks, four experimental rules, and a real sweep.
- [Hooks are kernel code: a maturity model, the first ten hooks mapped, and a brief for a hooks site and feed where you pay for state, never to run](hooks-are-kernel-code.md) Hooks are small code with kernel reach: a maturity model, the first ten hooks mapped, and a brief for a hooks site where you pay for state, never to run.
- [A proposed roadmap for RiskMandate: policies, understand, risk acceptance, contain, manage and insure, a spectrum of trust we would walk with each customer](the-riskmandate-roadmap.md) A proposed strategy for RiskMandate, a spectrum of trust: policies, understand, risk acceptance, contain, manage, insure.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 232 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=232)

**Posting this article on LinkedIn?** The cover is [how-a-memo-becomes-a-release.jpg](banners/how-a-memo-becomes-a-release.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/how-a-memo-becomes-a-release.html)*
