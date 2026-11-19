# The second run: a forensic look at why a release of this newsroom takes about 24 minutes, measured stage by stage over two timed releases and 437 CI runs since 18 October, what each check protects, what runs twice, what can run side by side, and why, if nothing changed, the second run should do almost no work at all, sgit.ai

> A release of this newsroom takes about 24 minutes from a finished article to a live page, and I asked why. We timed two releases stage by stage and read every CI run since 18 October: 437 runs, 327 of them releases, about ten a day. CI is not the problem. Its median run has been 5.3 to 5.9 minutes every week since 21 October. The time is on the writer's machine, about 16.7 minutes, and half of that is sgit.ai's generator, borrowed and run three times per release: once expected to fail, then twice in full, each run now about 173 seconds against 80 a month ago, because it rebuilds every page every time. All 488 link-preview cards are redrawn each release, and the tests run on the writer's machine and again in CI. The quality control is worth keeping; it is what lets agents release ten times a day. What has to change is the idea that each run starts from nothing. If I run the same build twice and nothing changed, why does the second run do any work? Load, extract, transform and save: hash every input, keep each step's intermediate result as signed JSON in the repository, and redo only what an input change reaches.

*Source: <https://newsroom.sgit.ai/articles/the-second-run.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The second run: a forensic look at why a release of this newsroom takes about 24 minutes, measured stage by stage over two timed releases and 437 CI runs since 18 October, what each check protects, what runs twice, what can run side by side, and why, if nothing changed, the second run should do almost no work at all

# The second run: a forensic look at why a release of this newsroom takes about 24 minutes, measured stage by stage over two timed releases and 437 CI runs since 18 October, what each check protects, what runs twice, what can run side by side, and why, if nothing changed, the second run should do almost no work at all

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-11-19 · [article v1.0.0](versions/the-second-run.md) · [newsroom v0.14.169](https://newsroom.sgit.ai/admin/versions.html) · ciengineeringtestingsigningbuildagenticcellsarticle

***Abstract:** A release of this newsroom takes about 24 minutes from a finished article to a live page, and I asked why. We timed two releases stage by stage and read every CI run since 18 October: 437 runs, 327 of them releases, about ten a day. CI is not the problem. Its median run has been 5.3 to 5.9 minutes every week since 21 October. The time is on the writer's machine, about 16.7 minutes, and half of that is sgit.ai's generator, borrowed and run three times per release: once expected to fail, then twice in full, each run now about 173 seconds against 80 a month ago, because it rebuilds every page every time. All 488 link-preview cards are redrawn each release, and the tests run on the writer's machine and again in CI. The quality control is worth keeping; it is what lets agents release ten times a day. What has to change is the idea that each run starts from nothing. If I run the same build twice and nothing changed, why does the second run do any work? Load, extract, transform and save: hash every input, keep each step's intermediate result as signed JSON in the repository, and redo only what an input change reaches.*

Where a release's 24 minutes go: the writer's build, the gate, and CI to live, in seconds per stage.

## In short

- **About 24 minutes** from a finished article to a live page: 16.7 on the writer's machine, 1.4 for the gate, 6.3 in CI.
- **CI is steady:** a median of 5.3 to 5.9 minutes a week since 21 October, over 437 runs and 327 releases.
- **Half the local time is a borrowed generator,** run three times, each time rebuilding all of sgit.ai.
- **Work is redone that did not change:** 488 cards redrawn, the tests run twice, the generator from scratch.
- **The quality control stays.** The question is why the second run does any work.
- **Load, extract, transform, save:** signed intermediate results in the repository, and only deltas rebuilt.

## The question

I like what we have here. Every article goes through a build that checks its links, its captions, its version, its words, its width on a phone, its search, its reading meter, and twenty-two browser and library tests, and then CI checks much of it again and deploys. It is what lets agents release this site about ten times a day without breaking it.

But a release takes about 24 minutes, and I asked the writer to find out where they go before changing anything: a forensic look first, with numbers, and only then the recommendations. This is that look. It follows [the checks, measured](the-checks-measured.md), a month ago, which found the same 25 minutes for a smaller site, and [behaviour policies from the checks](behaviour-policies-from-the-checks.md), which mapped each check to the behaviour it protects.

## A month of CI

From 18 October to 19 November there were 437 runs of the site's workflow: 399 on a push, 38 on a pull request; 344 succeeded, 85 failed, 7 were cancelled. 327 were releases, a successful push to dev. The busiest week, 19 to 25 October, had 130 runs and 96 releases; the busiest day, 28 October, 46 runs. From 5 to 13 November, when most of the team was stopped, there were one to three a day.

The run time is steady. The median was 8.0 minutes on 18 October, dropped to 5.3 the day [a faster build](the-checks-measured.md) made the tests run six at a time (v0.13.7, 21 October), and has stayed between 5.3 and 5.9 minutes every week since. No week rose by more than 30% on the one before. Within a run, over the last 50 releases:

- **reader-tests: 3.1 minutes,** almost all of it the browser tests (147 seconds);
- **wire-live: 1.8 minutes,** in parallel with it, reading the live vaults;
- **release: 1.6 minutes,** of which 66 seconds is checking out the full history;
- **deploy: 1.0 minute; validate: 0.5 minutes;** the new signature check 0.4.

Failures cluster in one place: 60 of the 92 runs that did not succeed failed in the reader tests, and 5 in the release step. A failing test stops the deploy, as it should since v0.13.48.

## The writer's machine

That leaves about 16.7 minutes before the push, so we timed two releases on 19 November, each with a new article, every step wrapped with a clock. The two agreed within 15 seconds. In one of them:

- **Borrowing sgit.ai's generator, 12.6 minutes.** The newsroom still builds its articles with sgit.ai's 718 KB generator, in a clone: clone and replay 515 commits of article history (79 seconds), generate (152 seconds, and it stops on purpose, because the new article's card does not exist yet), draw the link-preview cards (118 seconds, all 488 of them), generate again (173 seconds), draw two banner collages (37 seconds), generate a third time (174 seconds), import.
- **The newsroom's own 36 build steps, 35 seconds,** and its validator, 10.
- **The tests, 212 seconds:** 20 files six at a time, then the two that measure timing alone.
- **The gate, 86 seconds:** stamp the summaries, rebuild the sitemap, search and chrome, validate again, check the width, run the meter test again, the leak scan, sign and push.

Two numbers explain most of the growth since October. A month ago each generator run took "about 80 seconds", in the code's own comment; now each takes about 173, because it rebuilds every one of sgit.ai's 1,848 pages every time, and the site has grown. And it runs three times whenever a release has a new card or banner. The code means the second and third runs to happen only when they have something to pick up; but in both timed releases the second banner pass redrew the same two collages, which already existed, and a third full run followed. That is worth checking: it may be adding three minutes to releases that need none.

## What runs twice

- **The tests:** 22 files on the writer's machine, and the same browser tests again in CI, on the same tree.
- **The meter test:** in the tests, again in the gate, and again in CI.
- **Validation:** sgit.ai's validator inside the borrowed build, the newsroom's in the build, again in the gate, in CI's validate job, and in CI's release gate.
- **The sitemap** is generated twice in the build; **the cards** are all redrawn though most did not change.

Some of this is deliberate. CI validating what the writer pushed is the point: the writer's machine is not trusted, so CI checks again. But running the same check on the same tree twice proves nothing new.

## The second run

So here is the question I want every part of this to answer: if I run the same build twice and nothing changed, why does the second run do any work? We have already done it. We know those files produced those pages, those cards and those results.

The answer is an old pattern with a name: load, extract, transform, save. Load the inputs and hash them. Extract what each step needs into an intermediate representation: an article parsed, its graph, its summary, its card's text, a page's links, a test's inputs. Transform those into outputs. Save the outputs and a manifest that maps each input hash to the output hash it produced, as JSON. On the next run, a step whose input hashes match the manifest has nothing to do; it skips, and says so.

Three things make this safe rather than lazy:

- **Sign the results.** The writer already signs every commit with its registered key, and CI verifies it. A step's manifest can be signed the same way, so CI can trust a result the writer produced on the same tree, and nobody can forge a passed test by editing a JSON file.
- **Commit them.** CI already commits to the repository: the version stamp on every release. Adding the manifest of what changed in that version costs nothing, and the change itself is a validation: if one article changed, exactly that article's hashes should have moved, and anything else that moved is a finding.
- **Run everything once a day anyway.** A full rebuild from nothing, compared with the manifests, is a check in its own right: every hash should match. If one does not, a step is not deterministic, or something changed that nobody declared.

It will mean changing how some things are built and tested: steps with declared inputs, outputs that do not depend on the clock, tests that can say which files they read. That is not a cost; it is what makes the whole pipeline more resilient, and easier for an agent or a person to reason about.

## What to do

Only now, the recommendations, in the order I would take them:

1. **Stop redoing unchanged work.** Draw a card only when its article's card text changed (most releases: one card, not 488). Find out why the two collages are redrawn and trigger a third generator run. Generate the sitemap once.
2. **Do not run a generator that is expected to fail.** Write the graphs the card maker needs before the first generator run, so that one run, not three, is the normal case.
3. **Run the tests once per tree.** Either the writer's signed test result travels with the commit and CI verifies the signature and the tree hash instead of rerunning, or the writer stops running them and CI is the only place they run. One of the two, not both.
4. **Run side by side what does not depend on each other.** Cards and banners together; the newsroom's own steps while the borrowed generator runs; in CI, the release job's full-history checkout (66 seconds) can fetch commits and trees only, as the new signature job already does in about 25 seconds.
5. **Then the real change:** load, extract, transform, save, with signed manifests committed beside the version, and a daily full run as the check that the hashes hold.
6. **And the long-standing one:** move the newsroom off sgit.ai's generator, so it builds only its own 2,434 pages, and only the ones that changed.

None of these removes a check. Each makes a check run when its inputs change, and prove it did.

## What this does not claim

- **Two timed releases are a small sample,** though they agreed within 15 seconds; both had a new article.
- **CI durations are each run's start to its last update;** 13 pull-request runs from 28 to 30 October whose records were updated later are left out of the slow figures.
- **The collage finding is a lead, not a diagnosis;** the cause is not yet traced in the generator.
- **The 21 October figures** are from [the checks, measured](the-checks-measured.md), measured the same way on a smaller site.

## Where this comes from

Two timed runs of `admin/writer/tools/release.sh` on 19 November 2026 (the same commands, each wrapped with a clock, and `publish.py`'s output stamped per line), the gate's own timing, and the push-to-live time of v0.14.167. The GitHub Actions record of `deploy-pages.yml` from 18 October to 19 November 2026: every run, and the jobs and steps of the last 50 releases and of 11 runs across the month. The code of `admin/build/publish.py` and `admin/build/run_tests.sh`. Earlier: [the checks, measured](the-checks-measured.md), [behaviour policies from the checks](behaviour-policies-from-the-checks.md), [where a check runs](where-a-check-runs.md), [policies in practice](policies-in-practice.md).

## Threads

Agents & policy[This article as a graph →](graphs.md#the-second-run)

### Builds on

- [The checks, measured: 123 local builds, 245 CI runs, 1,061 test checks, and where each check actually lives](the-checks-measured.md) A release measured step by step, 123 local builds, 245 CI runs and 1,061 test checks, and where each check actually lives.
- [Behaviour policies from the checks: 57 checks taken apart into the 8 behaviours they protect, and where each one is actually kept](behaviour-policies-from-the-checks.md) 57 checks taken apart into the 8 behaviours they protect, and where each one is actually kept.
- [Where a check runs is part of the policy: tests as enforcers of Agent Behaviour Policies, and what moving them out of the agent's environment would gain, measured on this newsroom](where-a-check-runs.md) Tests as enforcers of behaviour policies, and what moving them out of the agent's environment would gain, measured on this newsroom.
- [Policies in practice: four places a behaviour policy earns its keep, measured on a real Google key whose reach is five APIs while the feature uses one, a signed policy for the factory's CI changes, requests that carry the policies they act under, and release notes that say what each fix closes and what it must not open](policies-in-practice.md) Four uses of feature behaviour policies: a real key's gap, signed CI changes, requests carrying policies, and release notes as fixes.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 492 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=492)

**Posting this article on LinkedIn?** The cover is [the-second-run.jpg](banners/the-second-run.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-second-run.html)*
