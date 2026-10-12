# Green does not mean live, sgit.ai

> Two releases pushed cleanly, reported success, and never reached the site. Every check we had was green, because the failure happened in a place none of them could see. What we changed, and the general rule underneath it.

*Source: <https://newsroom.sgit.ai/articles/green-does-not-mean-live.html> · sgit.ai v0.7.79 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Green does not mean live

# Green does not mean live

2026-08-17 · [article v1.2.0, 3 versions](versions/green-does-not-mean-live.md) · [sgit.ai v0.2.33](https://sgit.ai/admin/versions.md) · cideployverification

***Abstract:** Two releases pushed cleanly, reported success, and never reached the site. Every check we had was green, because the failure happened in a place none of them could see. What we changed, and the general rule underneath it.*

Two consecutive releases of this site pushed cleanly, verified themselves against both remotes, printed **"both remotes in sync, done"**, and never reached anybody. The site served a two-release-old page for forty minutes. It was noticed by a human on a phone, who looked at the version badge and said *"is this the latest version?"*

Everything about that sentence is worth sitting with. The checks were not weak. They were **checking the wrong boundary**.

## What the release actually verified

The release script does five things, and four of them are good:

1. Build the site from source.
2. Run the validator, structure, links, markdown twins, orphan pages, and a tripwire that scans every tracked file for a vault key.
3. Commit and push the encrypted vault; confirm `sgit status` reports in sync.
4. Commit and push the git mirror; confirm `HEAD == origin/dev`.

Step 4 is where the confidence came from, and it is genuinely a strong check, it compares hashes, not hopes. The problem is what it means. It means **the bytes arrived at GitHub**. It does not mean anybody can read them.

## The gap, named

Publishing this site has three boundaries, and we were verifying two:

```

  source  ──▶  git remote  ──▶  Pages deploy  ──▶  the reader
            ↑               ↑                  ↑
        verified        verified           NOT VERIFIED

```

Between the second and third arrows sits a GitHub Actions job. It has its own failure modes, it reports into a system neither remote knows about, and nothing in our release looked at it.

## What actually failed

Not our code. Not the content. The deploy job died in **"Set up job"**: before running a single step of its own:

```

Download action repository 'actions/configure-pages@v5'
##[warning] Failed to download ... Error: 429 (Too Many Requests)
##[warning] Back off 12.459 seconds before retry.
##[warning] Failed to download ... Error: 429 (Too Many Requests)
##[warning] Back off 26.597 seconds before retry.
##[error]  Failed to download archive after 3 attempts.

```

`codeload.github.com` rate-limited the download of a third-party action. The `validate` job passed. The `tag-release` job passed. The one job that puts bytes in front of readers could not fetch its own dependency.

This is worth stating plainly because it is the ordinary case, not an exotic one: **the most likely thing to break in a deploy is not your code.** It is a piece of shared infrastructure you do not run, on a day you were not thinking about it.

## The fix is one question, asked at the end

A release now finishes by asking the live site what version it is serving:

```

== 5/6 verify the deploy actually published
   waiting for v0.2.34 to appear at https://sgit.ai/ (up to 8 min)
   ......
   live: sgit.ai is serving v0.2.34

```

It polls with a cache-buster, because the origin's own answer is the only one that counts. If the version never appears it **aborts loudly**, names the Actions page, and says that a 429 on the action download is transient and needs a re-run.

The cost is real: up to eight minutes of waiting on every release. We took it, because the alternative had already been demonstrated twice in one afternoon, telling somebody a fix was live when it was not, twice, in writing.

## The rule underneath

This site already had two rules of exactly this shape, and adding the third made the pattern obvious:

- **A page nothing links to is unpublished.** The build fails on an orphan page, it happened once, a brief that was written, built and pushed while nothing linked to it.
- **A page the machine index omits is unpublished.** The build fails if any page would be missing from `llms.txt`, that happened too, a whole section silently absent.
- **A page the deploy never served is unpublished.** Now the release fails on it.

All three are the same claim: *shipped* is a fact about the reader, not about your repository. Every one of them was learned by getting it wrong first, which is the only reason the list is short and specific rather than long and aspirational.

## What this does not fix

Being honest about the edges, since that is the house rule:

- It detects a failed deploy; it does not repair one. A 429 still needs a human or a re-run.
- It checks the home page's version badge, not every page. A partial deploy that published some files would pass.
- It adds up to eight minutes to a release, which is a real tax on small fixes.

All three are acceptable against the failure they replace. The first one to bite will get its own entry.

*The release script is [in the repository](https://github.com/SGit-AI/SGit-AI__CLI); the releases described here are [v0.2.31 to v0.2.33](https://sgit.ai/admin/versions.md).*

*© 2026 Dinis Cruz and the sgit.ai team. This article's own text is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). You're free to share and adapt it, as long as you give credit. Quoted material and linked sources keep their own licences.*

## Threads

Site & engineering[This article as a graph →](graphs.md#green-does-not-mean-live)

### Continued by

- [Go slow to go fast: moving the newsroom from an explorer project to a villager one, with the brief to do it](explorer-to-villager-newsroom.md) The newsroom is live and charging. Move the reader code to its own repo, same bytes and same bugs, then map, test, review and refactor before new features.
- [Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan](authority-outside-the-model.md) Satya Nadella's seven principles for models as insider risks, answered one by one: what we run, what is design, and the five things the list leaves out.
- [Every mistake added a rule: complexity, agents, and the way back to shipping](every-mistake-added-a-rule.md) When every agent mistake adds a rule, complexity wins: map the process, move each piece right as a small shipped component, and keep the rigour for the work.
- [The investigation GitHub owes its customers: why a global outage of a platform the world deploys through deserves an aviation-style inquiry, and how the evidence could now be gathered](the-investigation-github-owes-its-customers.md) A global GitHub Actions outage read the way aviation reads an incident: independent inquiry, near-miss reporting, second and third stories, vaults for the evidence.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 1 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=1)

**Posting this article on LinkedIn?** The cover is [green-does-not-mean-live.jpg](banners/green-does-not-mean-live.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/green-does-not-mean-live.html)*
