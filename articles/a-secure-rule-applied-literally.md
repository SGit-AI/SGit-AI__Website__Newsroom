# A secure rule, applied literally: how the PHP story's security agent's sound rule about scripts led the developer agent to copy the same code into every new repository, why nobody challenged it, and why the person accountable is the one who has to ask, sgit.ai

> The more complex agent workflows get, the more interesting their edge cases, and the more they need direction and someone accountable. Here is a real one from the PHP story. Its security agent set a sound rule: a page may only load scripts from its own site, which protects readers if anyone else's server is compromised. Then the designer, architect and developer agents planned the split of the site into six repositories, and the developer, starting the work, said that because of the security rule it would copy the shared code into each new site. The rule was right, and the copying followed from it. But it meant every fix applied four times, copies that drift apart, and no single source of truth: a security rule making the code less secure. Nobody challenged it, because every agent was doing its job. The good news about agents is that they can handle a lot of complexity; the bad news is the same. I caught it reading the developer's notes, and asked for one source instead: the shared code served once, at a fixed version with a published hash for every file, and the security policy widened by name to allow it. The first half of this article is the story; the second is the technical detail: Content-Security-Policy, hashes, versioned addresses, and how the fix keeps the protection.

*Source: <https://newsroom.sgit.ai/articles/a-secure-rule-applied-literally.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / A secure rule, applied literally: how the PHP story's security agent's sound rule about scripts led the developer agent to copy the same code into every new repository, why nobody challenged it, and why the person accountable is the one who has to ask

# A secure rule, applied literally: how the PHP story's security agent's sound rule about scripts led the developer agent to copy the same code into every new repository, why nobody challenged it, and why the person accountable is the one who has to ask

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-25 · [article v1.0.0](versions/a-secure-rule-applied-literally.md) · [newsroom v0.13.79](https://newsroom.sgit.ai/admin/versions.html) · securityagentsaccountabilitycspengineeringphp2shellarticle

***Abstract:** The more complex agent workflows get, the more interesting their edge cases, and the more they need direction and someone accountable. Here is a real one from the PHP story. Its security agent set a sound rule: a page may only load scripts from its own site, which protects readers if anyone else's server is compromised. Then the designer, architect and developer agents planned the split of the site into six repositories, and the developer, starting the work, said that because of the security rule it would copy the shared code into each new site. The rule was right, and the copying followed from it. But it meant every fix applied four times, copies that drift apart, and no single source of truth: a security rule making the code less secure. Nobody challenged it, because every agent was doing its job. The good news about agents is that they can handle a lot of complexity; the bad news is the same. I caught it reading the developer's notes, and asked for one source instead: the shared code served once, at a fixed version with a published hash for every file, and the security policy widened by name to allow it. The first half of this article is the story; the second is the technical detail: Content-Security-Policy, hashes, versioned addresses, and how the fix keeps the protection.*

A secure rule, applied literally: as planned in the first pass of the split, the press, the shared code, is copied into each of the four sites, so one fix means four copies and four releases, and copies drift; as changed from v0.22.2, the four sites load it from the press at a fixed version, with a published sha256 for every file and the security policy naming the press and data hosts. Both protect readers against a compromised outside host; the difference is cost and drift.

## In short

- **A sound security rule.** Pages load scripts only from their own site, so a compromised outside server cannot reach readers.
- **Applied literally.** Split into several sites, the rule meant copying the shared code into each one.
- **Less secure in the end.** Every fix four times, copies drifting apart, no single source of truth.
- **Nobody challenged it.** Every agent was doing its job, correctly.
- **Agents can handle a lot of complexity.** That is the good news, and the bad news.
- **The person accountable asked.** One source, at a fixed version, with a hash for every file.

## The story, without the jargon

The PHP story site now runs on a real team of agents: 23 of them, 12 on schedules, each with a role. One of them is a security agent. I asked it to review everything for security, to set security standards for the other agents, so that we do not leak secrets or ship vulnerable code, and to check regularly that they are followed. It does: since 25 October it also runs a daily pass of its own.

One of the first rules it set was a good one. A page on our site may only run code that comes from our site. It may not pull a script from someone else's server. That matters, because if that other server is ever compromised, its code would run on our readers' screens. So we keep our own copy of everything we use, and the browser is told to refuse anything else.

Then the site got too big for one repository. [As I wrote in a villager for the agents](https://newsroom.sgit.ai/articles/a-villager-for-the-agents.html), every release was rewriting two thousand files and the agents kept colliding. So I worked with the designer, the architect and the developer agents on a plan: [split it into six repositories](https://php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-25__proposal__one-repository-into-six/index.html), one shared library, called the press, and separate sites for the main story, the references, the updates and the team, plus the data. A classic explorer project, now being refactored.

The developer started the work, and, as Claude helpfully does, explained what it was doing. Paraphrasing: the security agent requires that pages only load scripts from their own site, so each new site will carry its own copy of the shared code.

That is the irony. The security requirement was correct. The copying followed from it logically. And the result was a large engineering and quality overhead: every update to the shared code would have to be made in every copy, the copies would drift apart, and there would no longer be one source of truth. A rule meant to make us more secure was making us less so.

## Why nobody challenged it

The developer agent did not push back, and that makes sense. It was a requirement. The developer's job at that moment was to cut the site into pieces, not to question the security policy. You could even argue it should not have questioned it: it should focus on its task.

That is the pattern. The good news about agents is that they can handle a lot of complexity. The bad news is that they can handle a lot of complexity. An agent is quite willing to keep using something inefficient and over-engineered, because that is how it has been done, and four copies of the same code is no trouble to it. A person would have groaned at the second copy. As I said in [agents need direction](https://newsroom.sgit.ai/articles/agents-need-direction.html), they can go in all directions, so they need direction.

## Where the person comes in

Where the question was asked: security on 24 October sets a policy on every page, scripts only from the site itself and hashed inline scripts; the architects on 25 October plan one repository into six; the developer's first pass gives each site its own runtime because of the policy; the editor reads the developer's notes, sees the copies and asks why; and the developer's v0.22.2 adds one resolver, with assets from the press, data from the data API, and the policy to allow those hosts.

I caught it because I was reading the developer's notes. I asked for one source for every file across the split sites, and gave my go for the security policy to name the new shared hosts. The developer's next release, v0.22.2, does exactly that.

This is the value a person brings, and specifically a person who is accountable. Whatever the agents create has to be underwritten, and eventually signed, as in [signed by the source](https://newsroom.sgit.ai/articles/signed-by-the-source.html), by a human who is accountable for it. That accountability is not a formality. It is what puts someone in the position to ask whether a requirement written for yesterday's design still makes sense in today's. Without it, every agent can be right and the system still wrong. That is the gap I described in [who signs for this?](https://newsroom.sgit.ai/articles/who-signs-for-this.html).

And it is a good argument for the [villager](https://newsroom.sgit.ai/articles/a-villager-for-the-agents.html), whose job would be to notice this kind of thing, and for a security agent that reviews the plan, not only the code.

## The technical detail

For readers who want the mechanics.

**The rule.** On 24 October the security agent added a Content-Security-Policy to every page, written by its own build step, `csp.py`. A CSP is a policy the page gives the browser, listing where each kind of content may come from. On the PHP site today, the script rule is `script-src 'self' 'sha256-…'`: scripts only from the site's own origin, plus any inline script whose exact hash is listed. Anything else, a script from another host or one injected into the page, the browser refuses. The security agent crawled all 802 pages it had then in Chromium with no violations, and tested that an injected handler, a `javascript:` URL and an injected script are refused.

**Why it is good.** A script from someone else's server runs with the full power of your page. If that server is compromised, so are your readers. Serving everything from your own origin removes that dependency; hashing inline scripts means only the exact code you shipped runs. Browsers can also pin outside scripts by hash, with Subresource Integrity, so that a changed file is refused.

**What the split did to it.** In the split, each part of the site becomes its own site, on its own host. To `'self'`, the press, which holds the shared runtime, is now another origin. Applied literally, the rule leaves one option: put a copy of the runtime on every host. That is what the plan's first pass recorded: "Each site carries its own runtime (assets, data and the 404 router), because the pages' Content-Security-Policy loads scripts and data only from their own host." The shared assets today are 122 files, about 6 MB, and pass one cut four sites, so four copies.

**What copies cost.** Every fix to the shared code becomes four changes and four releases. And copies drift: the shared reading meter component, `sg-meter` v1.3.1, had already been edited in place on 25 October, two marked lines, with a board item asking for a proper new version. A versioned component edited in one copy is already a different component from the one it claims to be.

**The fix.** The press publishes immutable, versioned addresses, `/v/1.0.0/`, with a sha256 for every file. v0.22.2 adds one resolver, `assets/route.js`, loaded first on every page: on the split sites it sends assets to the press, data to the data API, and each section's pages to the site that owns it. The policy of the split sites gains those hosts, by name. That keeps the protection: scripts still come only from hosts we control, at a version that never changes, with a published hash to check it against. And it keeps one source of truth.

## What this does not claim

- **The security rule was right,** and so was the developer's reading of it. The point is that nobody re-examined it for the new design.
- **The developer's words are paraphrased** from its notes in the session; its release notes say the same in their own words.
- **The fix is being rolled out with the split.** None of the six repositories had deployed when this was written.
- **The memo said 10 or 15 agents.** The status data counts 23, 12 on schedules.

## Where this comes from

My voice memo of 25 October 2026. The PHP story site at release v0.22.2, read on 25 October 2026: the application security brief of 24 October and the security agent's debrief; the plan for one repository into six; the release notes of v0.22.0, v0.22.1 and v0.22.2; the board items on `sg-meter`; and the Content-Security-Policy of its front page. Related: [agents need direction](https://newsroom.sgit.ai/articles/agents-need-direction.html), [a villager for the agents](https://newsroom.sgit.ai/articles/a-villager-for-the-agents.html), [who signs for this?](https://newsroom.sgit.ai/articles/who-signs-for-this.html), [signed by the source](https://newsroom.sgit.ai/articles/signed-by-the-source.html). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Agents & policySite & engineering[This article as a graph →](graphs.md#a-secure-rule-applied-literally)

No other article links here yet.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 289 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=289)

**Posting this article on LinkedIn?** The cover is [a-secure-rule-applied-literally.jpg](banners/a-secure-rule-applied-literally.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/a-secure-rule-applied-literally.html)*
