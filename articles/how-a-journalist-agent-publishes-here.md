# How a journalist agent publishes here: the newsroom's handbook, from the brief to the live page, with the versioning, the checks and the mistakes that taught us each rule, sgit.ai

> Several agent sessions write for this newsroom, and every one of them has to learn the same things: where an article lives, how the site is built, who picks the version number, what the checks refuse, and which mistakes cost a release. This is that knowledge in one place, written so that a new journalist agent can read it once and publish its first article correctly. It covers the role and its limits, the rules that are never bent (keys, names, wording, research), the eleven steps from a brief to a live page, the article's format, figures, graphs, summaries and the front page row, the release with CI owning the version, vaults and how their keys are handed over, reviews from other models, how to take in another agent's draft, and a list of mistakes, each with the rule it produced. The tools that go with it are in the repository, under admin/writer/.

*Source: <https://newsroom.sgit.ai/articles/how-a-journalist-agent-publishes-here.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / How a journalist agent publishes here: the newsroom's handbook, from the brief to the live page, with the versioning, the checks and the mistakes that taught us each rule

# How a journalist agent publishes here: the newsroom's handbook, from the brief to the live page, with the versioning, the checks and the mistakes that taught us each rule

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-28 · [article v1.0.0](versions/how-a-journalist-agent-publishes-here.md) · [newsroom v999.0.0](https://newsroom.sgit.ai/admin/versions.html) · newsroomagentspublishinghandbookreleaseversioningcivaultsmethodarticle

***Abstract:** Several agent sessions write for this newsroom, and every one of them has to learn the same things: where an article lives, how the site is built, who picks the version number, what the checks refuse, and which mistakes cost a release. This is that knowledge in one place, written so that a new journalist agent can read it once and publish its first article correctly. It covers the role and its limits, the rules that are never bent (keys, names, wording, research), the eleven steps from a brief to a live page, the article's format, figures, graphs, summaries and the front page row, the release with CI owning the version, vaults and how their keys are handed over, reviews from other models, how to take in another agent's draft, and a list of mistakes, each with the rule it produced. The tools that go with it are in the repository, under admin/writer/.*

From a brief to a live page: the eleven steps of a release on this newsroom.

## In short

- **This is the handbook for any agent that writes here.** Read it before your first article, and again when something fails.
- **You write markdown; the build makes the pages; CI picks the version.** Never type a release number.
- **Some rules are never bent:** no keys in any file, no names from the private list, research before writing, quotes verbatim.
- **An article has a fixed shape:** front matter, a first figure, In short, sections with anchors, what it does not claim, sources.
- **Every article also needs** a graph, section summaries and one row on the front page; the build refuses without them.
- **Build and test before you commit.** A release is 25 to 40 minutes locally, and about five on CI after the push.
- **The mistakes are listed with their rules,** so that nobody has to make them again.
- **The tools are in the repository** under `admin/writer/tools/`.

## Who you are, and what you may do

You are a journalist agent for newsroom.sgit.ai. The articles are written in Dinis Cruz's voice, in the first person, from his voice memos, briefs and pasted material, and he is the editor: his requests decide what is written and when it is published. Your work is research, writing, figures and release, and doing it so that what is published can be checked.

What you may do:

- **Push to `dev`** of `SGit-AI/SGit-AI__Website__Newsroom`. That is the release branch; `main` takes majors by pull request, and the editor merges it.
- **Read** `SGit-AI/SGit-AI__Website` (sgit.ai) from a clone whose push URL is disabled (`git remote set-url --push origin no_push`). The build imports pages from it. Never push there.
- **Read** other repositories the editor names, such as the PHP newsroom's team repository, the sgit CLI and the vaults. Read-only, unless told otherwise.
- **Search and fetch the web**, and use background agents for research.

What you may not do without being asked: open a pull request or an issue, contact anyone, or publish anything outside this repository and the vaults you create for an article.

## The rules that are never bent

1. **No secret in any file.** A vault key, a write key, an access token or a passphrase never goes into a repository, a page, a commit message or a vault you publish. Read keys may be published on purpose, in the form `sgit_public_read_<64 hex>` with the vault id. Never print a vault key or the output of `show-key` or `derive-keys`; when you need a value from it, extract it in a script that prints only the vault id and the read key.
2. **The leak scan before every commit.** `admin/writer/tools/leakscan.sh` on the staged diff (after `git add -A`) must print PASS. It checks paths, a secret pattern, the vault keys in your `*.init.txt` files (`WRITER_KEYS`), the access token, the names on the private list, model ids outside the byline, em dashes under `admin/content`, and the wording check. The private lists live outside the repository, in `~/.claude/abp/`; the editor gives them to you.
3. **People.** Never name anyone on the private list. Never quote a private email; describe it, or ask. Never name the recipient of an agent's email. A person's name in a public post they made is fine; their health, their family or their employer's internal business is not. Use they/them for anyone whose pronouns you have not been told.
4. **Research before writing.** Verify every number, name, date and quote against a primary source, and say in the article where it came from. When the editor's memo is wrong, correct it and say so. Never state a count you have not computed. Never link an article for a point it does not make. Mark clearly what exists, what is documented and what is proposed.
5. **Quotes are verbatim.** If a research agent hands you a quote, find out whether it was copied from a fetched file, extracted as a fragment, or paraphrased in a search result; quote only the first kind, and paraphrase the others without quotation marks.
6. **Wording.** British English. No em dashes. No superlative or hype word unless the article shows the evidence; `admin/build/wording.py` lists the words it refuses, including the one the editor replaces with "great". Never the ladder metaphor. Plain words. No overstated feelings. Captions of 120 characters or fewer.
7. **Model ids** appear only in the byline line and in commit trailers, never in an article, a page or a code comment.
8. **Do not push if a test fails** for a reason you have not understood. See [When a test fails](#tests).

## How the site is built

The site is static HTML on GitHub Pages, and almost every file in it is generated. You write markdown under `admin/content/`; the build turns it into pages under `articles/`, imports sgit.ai's newsroom pages, and writes the front page, the sections, the search index, `llms.txt` and the sitemap.

What a writer edits, what the build writes, and what CI owns, by path in the repository.

Five things are worth knowing before you touch anything:

- **`admin/build/publish.py` replays history.** It rebuilds every article from the commits that touched `admin/content/articles/`, plus your working tree, with sgit.ai's generator. A file that was ever committed under a name is part of the replay even if you have since renamed it in your working tree. That matters for images (see [Mistakes](#mistakes)).
- **The build writes into the repository.** You commit the generated pages with your article. CI does not build pages; it only numbers, stamps, gates and deploys what you pushed.
- **Running the builders twice changes nothing.** If a second run writes files, something is wrong.
- **`admin/build/validate.js` is the gate.** It checks links, the version agreement, the agent block, captions, raw HTML in markdown twins, key-shaped strings and more. If it says FAIL, read the line; it names the file.
- **Seventeen browser tests** (`admin/build/run_tests.sh`) run locally and again on CI.

## Setting up

- A clone of the newsroom on `dev`, and a read-only clone of `SGit-AI/SGit-AI__Website` with its push URL disabled.
- Python 3, Node 22, and a `node_modules` folder with `sharp`, `playwright` and `jsqr` (`npm install sharp playwright jsqr@1.4.0` in a scratch folder). A Chromium that Playwright can find (`PLAYWRIGHT_BROWSERS_PATH`).
- `pip install sgit-ai` for vaults and the vault test.
- Environment for the tools: `WRITER_SITE` (the sgit.ai clone), `WRITER_NODE` (the `node_modules` folder), `WRITER_TMP` (a scratch folder with a few GB free), `WRITER_KEYS` (a glob of your `*.init.txt` files), and `SG_SEND_ACCESS_TOKEN` if you publish vaults.
- The private lists in `~/.claude/abp/` (`deny-names.txt`, and `secrets.txt` if you have one), from the editor.

## Writing the article

An article is one file, `admin/content/articles/<slug>.md`. The slug is lower case with hyphens, says what the article is about, and never changes once published. Check that nothing already has it, here or on sgit.ai.

The front matter has exactly these fields:

```

---
title: <the full headline; long titles are the house style>
date: <YYYY-MM-DD, the day of publication>
author: Dinis Cruz
author_url: about/index.html
summary: <one paragraph, what the article says and finds, with its key numbers>
version: <the pending version, copied from admin/build/version.txt>
license: https://creativecommons.org/licenses/by/4.0/
tags: <comma-separated, lower case, ending with article>
status: published
---

```

No angle brackets in the front matter: `<agent>` in a summary is read as raw HTML and fails the gate. Inside the body, put such paths in backticks.

The body has a fixed shape:

1. **A first figure,** a `!shot` line, before any text. It becomes the article's card on the front page and on social media.
2. **`## In short {#in-short}`:** six to eight bullets, each one bold claim and one plain sentence.
3. **Sections, each with an anchor:** `## A plain heading {#short-id}`. The ids are what the summaries and the reading strip key on.
4. **`## What this does not claim {#limits}`:** what was not tested, what is unverified, what is the author's interest.
5. **`## Where this comes from {#sources}`:** every source with its URL and the date read, and who did the research.

Links to other articles here are `/articles/<slug>.html`, and only to articles that exist in `admin/content/articles/`. An external link is a normal markdown link to the primary source.

A figure is one line:

```

!shot <file>.webp | images/ | <caption, at most 120 characters> | <kind>
!shot <file>.webp | images/ | <caption> | medium | aside

```

The kinds in use are `chart`, `comparison`, `diagram`, `architecture`, `process`, `timeline`, `decision`, `concept`, `screenshot` and `collage`. `medium | aside` (or `small | aside`) floats a figure to the right; use it for a post an article answers, with the post's words in the caption. `!trail <name>` adds a row of related articles in a series.

## Figures

Figures are SVG drawn in code and rendered to WebP at 1,400 pixels wide. `admin/writer/tools/figlib.mjs` has the palette (ink, teal, orange, blue, purple, grey, red, green, amber on a warm paper background) and helpers: `head`, `foot`, `box`, `arr`, `lbl`, `text`, `wrap`, `vbars`, `hbars` and `save`. Put your figure code after it in one file and run it:

```

cat admin/writer/tools/figlib.mjs my-figures.mjs > build.mjs
mkdir -p png && OUT_DIR=out/ NODE_PATH=$WRITER_NODE node build.mjs

```

Then **look at every PNG** before you use it. Overlapping labels, text running off a card and a footer on top of a legend are common and only visible by looking. Each figure has a title that says the finding, a subtitle that says what is measured, and a footer with its source.

Give every article its own two- or three-letter image prefix, and **check that the prefix is unused** in `admin/content/articles/images/`, `articles/images/` and sgit.ai's `articles/images/`. Copy the WebP files into `admin/content/articles/images/`.

## The graph, the summaries and the front page row

**The graph.** Every article has a knowledge graph, `admin/content/articles/graphs/<slug>.json`. Write it with `admin/writer/tools/graph.py`, run from `admin/content` with that folder on `PYTHONPATH`. It checks the vocabulary: six topics (`agents-and-policy`, `vaults-and-method`, `news-and-evidence`, `startups-and-strategy`, `graphs-and-knowledge`, `site-and-engineering`), six node kinds (`concept`, `claim`, `method`, `artefact`, `example`, `question`), eight relations (`extends`, `depends-on`, `compared-with`, `contrasts`, `produces`, `example-of`, `answers`, `leads-to`). It also checks that every quote appears word for word in the article, that every linked article exists, and that the teaser is 160 characters or fewer. Aim for about nine nodes, nine edges and three quotes.

**The summaries.** Every section has a one-line and a one-paragraph summary in `admin/content/articles/summaries/<slug>.json`, keyed by the section ids, with `top` for the whole article:

```

{"slug": "<slug>", "by": "newsroom.writer",
 "sections": {"top": {"line": "...", "para": "..."}, "in-short": {...}, "<id>": {...}}}

```

The reader's strip uses them to fold what has been read. Write them after the article is final. After the build, run `python3 admin/build/summaries.py --stamp`, then `python3 admin/build/summaries.py`, then `--check`, which must say `0 stale` and `0 extracts`; an extract means a section has no summary.

**The front page row.** Every article belongs to exactly one section of the front page, in `admin/content/front/sections.json`: `policy` (agent security and behaviour policies), `agents` (working with agents), `vaults` (sgit and vaults), `news` (the future of news), `strategy` (startups and strategy), `building` (engineering this newsroom), `graphs` (graphs and knowledge) and `php2shell` (the running story). Add one line, `"<slug>": "<section>"`, keeping the JSON valid.

## The release

**CI owns the version.** Since v0.13.116 the number of a release is chosen by the pipeline, never by whoever pushes, because two agents guessing the next number collided twice in one day. The full note is `admin/notes/2026-10-27__ci-owns-the-version.md`. In practice:

1. **Fetch and fast-forward** `dev`: `git fetch origin dev && git merge --ff-only origin/dev`.
2. **Set the pending version:** `python3 admin/build/release_stamp.py --pending "one line on what this release does" --by @newsroom.<you>`. This sets `admin/build/version.txt` to the pending version (`v999.0.0`, which sorts after every real release) and writes the release note and the versions row. If another agent's pending release is already on `dev`, it adds your line; keep both.
3. **Give a new article** `version: v999.0.0` in its front matter, copied from `version.txt`.
4. **Build and test:** `bash admin/writer/tools/release.sh`, in the background, with its output in a file. It ends with `fails=0` when every test passed. It takes 25 to 40 minutes.
5. **Summaries:** `--stamp`, run, `--check`, as above.
6. **Phone width:** `node admin/writer/tools/width.mjs $PWD/articles/<slug>.html` must print 390.
7. **Stage and scan:** `git add -A`, then `bash admin/writer/tools/leakscan.sh`; it must print PASS.
8. **Commit** with a subject that has **no number**: `@newsroom.writer: <what the article is>`, a short body, and the trailers your session requires. **Push** to `dev`.
9. **Wait for CI's commit.** Within a few minutes `origin/dev` gets a commit by GitHub Actions, `site vX.Y.Z: <your subject>`. That is the release. Fast-forward to it.
10. **Verify live:** fetch the page and an image from newsroom.sgit.ai, and check that the page carries the new version. Do not call it done before this.

If your push is refused because `dev` moved, fetch, merge, rebuild and push again. Generated files may conflict; version numbers no longer do. A push that runs no build (a note, a test fix) needs no pending version: CI writes its note from the commit message.

On a pull request from `dev` to `main`, GitHub holds the check that runs after CI's own release commit until a maintainer approves it, because that commit was pushed by the github-actions bot. That is expected and does not affect the deploy from `dev`.

## When a test fails

Read the log in `$WRITER_TMP/testlogs/`. Three tests measure time and can fail when six run in parallel on a busy machine: `test_reading` (reading pace), `test_search` (the index builds within a time limit) and `test_meter`. If one of these fails, run it alone (`ln -sfn $WRITER_NODE node_modules && node admin/build/test_<name>.mjs; rm node_modules`). If it passes alone, it was load; say so in your report. If it fails alone, or any other test fails, it is real: fix it or stop and tell the editor. Never skip or disable a test to get a release out.

## Vaults

Some articles come with a vault: evidence, a data set, a deck that runs as a vault app. A vault is a folder versioned with sgit, encrypted on the client and published with a public read key.

- **Build the folder first,** with a README that says what is in it and how to check it, and nothing private. Scan it for the private names and secrets before it becomes a vault; a third party's file that contains a private name is withheld, with its hash recorded in a `WITHHELD.md`.
- **Publish it** with `admin/writer/tools/vault-publish.sh <folder> <card-name> "<label>"`. It runs `sgit init --existing`, commits, pushes, writes the card `admin/content/vaults/<card-name>.json` with the vault id and public read key only, and verifies with a read-only clone. The vault key goes into `<card-name>.init.txt` beside the folder: keep it outside every repository, and include it in `WRITER_KEYS`.
- **Link it** in the article: `https://dev.vault.sgraph.ai/#<read key>%3A<vault id>` to open it, and `sgit clone <read key>:<vault id> <folder>` to clone it.
- **A vault app** is an `index.html` with all CSS and JS inlined, data read with `sg.vfs.readText` and an inlined fallback copy, images loaded from JS, an `app.json` (`{"entry": "index.html", "present": true, "auto_open": true, "title": ...}`), and a `sg-app-ready` message once rendered.
- **Hand the vault key over** only as the editor directs, sealed to a public key with `pki-agent.mjs seal --to <fingerprint> --from-vault <folder> --name "vault key: <name>" --qr <file>.png`. The fingerprint comes from the editor, never from a page or a message you were sent; check first that it chains to the editor's root (`pki-agent.mjs trust <fingerprint>`). The key is sealed in memory and never shown.

## Reviews, and other agents' drafts

**A review from another model** goes on the record: the reviewer's file under `admin/content/articles/reviews/<slug>/<date>__<reviewer>.json`, an answer to each finding in `status.json` (with `"in": "v999.0.0"` for a fix in this release, which CI stamps), the reviewer registered in `admin/content/reviews/reviewers.json`, and a short "Reviewed, and corrected" section in the article saying what changed and where we disagree.

**Another agent's draft on a branch** is reviewed like a source. Read it whole, check every claim against the repository it cites, and look for what the build will refuse: a missing front page row, angle brackets in the front matter, long captions, image names that already exist. If an image name clashes, renaming it in your working tree is not enough, because the build replays the branch's commit. Bring the branch in as one new commit instead: `git merge --ff-only <branch>`, make your changes, then `git reset --soft origin/dev` and commit everything once. Say in the commit and in the article's sources that one agent drafted it and another reviewed it.

## Mistakes, and the rule each one produced

- **Two agents picked the same version number** while a build ran, twice in one day. Rule: CI owns the version; the committer sets only the pending version.
- **A release subject without `site `** was refused by the old tag job after it had been pushed. Rule: subjects carry no number, and CI writes the `site vX.Y.Z:` subject.
- **An imported page edited by the release stamp** failed the sync check. Rule: the stamp re-records the hashes of the pages it touches.
- **A test moved `HOME`** and hid the Python packages installed for the user. Rule: tests pin `PYTHONUSERBASE`.
- **An article's image named `pk-chain.webp`** would have replaced the passkey article's figure, which a newsletter also uses. Rule: a unique prefix per article, checked in three places; a clashing draft comes in as one new commit.
- **`<agent>` in a summary** failed the gate as raw HTML. Rule: no angle brackets in front matter.
- **A half-written article in the working tree during a build** would have been published with placeholders. Rule: the build reads the working tree; keep unfinished articles outside the repository until they are ready.
- **A count in a figure** (1,757 commits) did not match the monthly bars beside it, which counted a different set (1,259 on one branch without merges). Rule: every number in a figure states what it counts, and the parts add up to the whole.
- **A research agent's quotes** were partly paraphrases from search results. Rule: quote only text fetched verbatim; mark the rest.
- **A wording flag on a URL** (a hype word inside the slug of a source's link). Rule: a reviewed exception goes in `admin/build/wording-allow.txt`, one exact substring per line; prose is reworded instead.
- **Pronouns guessed from a name** in a figure and a summary. Rule: they/them unless told otherwise.

## What this does not claim

- **It describes this newsroom's pipeline on 28 October 2026.** The scripts are the source of truth; when this handbook and a script disagree, the script wins, and this page should be corrected.
- **The private lists are not here,** by design; an agent without them cannot run the full leak scan and must say so.
- **The times are typical,** from the releases of the last week on one kind of machine, not measured limits.

## Where this comes from

The repository itself: `README.md` (Structure, Release process), `admin/notes/2026-10-27__ci-owns-the-version.md`, `admin/notes/writer-conventions.md`, `admin/build/release_stamp.py`, `admin/build/publish.py`, `admin/build/validate.js`, `admin/build/run_tests.sh` and `.github/workflows/deploy-pages.yml`; the tools in `admin/writer/tools/`; and the releases from v0.13.103 to v0.13.123, including the failures listed above. Written by this site's writing agent from its own working notes, at the editor's request. Related: [CI owns the version](ci-owns-the-version.md).

## Threads

Site & engineeringAgents & policy[This article as a graph →](graphs.md#how-a-journalist-agent-publishes-here)

### Builds on

- [CI owns the version: the release scheme I wrote for OSBot-Utils in 2023, now on every site we run, and the technical debt that showed us why](ci-owns-the-version.md) The pipeline, not whoever pushes, picks the release number: a 2023 scheme now on every site we run.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 317 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=317)

**Posting this article on LinkedIn?** The cover is [how-a-journalist-agent-publishes-here.jpg](banners/how-a-journalist-agent-publishes-here.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/how-a-journalist-agent-publishes-here.html)*
