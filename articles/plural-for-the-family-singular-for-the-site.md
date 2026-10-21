# Plural for the family, singular for the site: why the AWS site is aws.twin.sgit.ai, the naming rule behind it, and what it changes on the twins and providers sites, sgit.ai

> The site proposed in AWS from the vault now has a name: aws.twin.sgit.ai, with its repository SGit-AI__Website__Twin__AWS and its hub at twins.sgit.ai. The name carries the design. It is a twin first: an AWS-shaped interface, for S3, Lambda, EC2, IAM, billing and logs, whose backend is a vault, with the real AWS account put in front of it later as a second backend behind the same interface. That is the same pattern as the one twin that already works, the S3-compatible vault container, where boto3 cannot tell the difference. The name also follows a rule we have now fixed for every family of sites: plural for the hub, singular for the instance, so twins.sgit.ai and aws.twin.sgit.ai, hooks.sgit.ai and tokens.hook.sgit.ai, providers.sgit.ai and elevenlabs.provider.sgit.ai. Held against the hosts that exist, the newer families follow it, and four hosts break it: three under providers and one under games. This records the decisions, the options we rejected, what changes on the twins and providers sites, and one correction: on GitHub Pages, no wildcard certificate is needed.

*Source: <https://newsroom.sgit.ai/articles/plural-for-the-family-singular-for-the-site.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Plural for the family, singular for the site: why the AWS site is aws.twin.sgit.ai, the naming rule behind it, and what it changes on the twins and providers sites

# Plural for the family, singular for the site: why the AWS site is aws.twin.sgit.ai, the naming rule behind it, and what it changes on the twins and providers sites

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-21 · [article v1.0.0](versions/plural-for-the-family-singular-for-the-site.md) · [newsroom v0.13.16](https://newsroom.sgit.ai/admin/versions.html) · sgitnamingtwinswebsitesdecisionsarticle

***Abstract:** The site proposed in AWS from the vault now has a name: aws.twin.sgit.ai, with its repository SGit-AI__Website__Twin__AWS and its hub at twins.sgit.ai. The name carries the design. It is a twin first: an AWS-shaped interface, for S3, Lambda, EC2, IAM, billing and logs, whose backend is a vault, with the real AWS account put in front of it later as a second backend behind the same interface. That is the same pattern as the one twin that already works, the S3-compatible vault container, where boto3 cannot tell the difference. The name also follows a rule we have now fixed for every family of sites: plural for the hub, singular for the instance, so twins.sgit.ai and aws.twin.sgit.ai, hooks.sgit.ai and tokens.hook.sgit.ai, providers.sgit.ai and elevenlabs.provider.sgit.ai. Held against the hosts that exist, the newer families follow it, and four hosts break it: three under providers and one under games. This records the decisions, the options we rejected, what changes on the twins and providers sites, and one correction: on GitHub Pages, no wildcard certificate is needed.*

The families held against the rule: plural for the hub, singular for the instance. The twins and hooks families follow it; the three provider hosts and the game break it; the twin, hook and demo instances are reserved, with no site yet.

## In short

- **The AWS site is aws.twin.sgit.ai.** Repository `SGit-AI__Website__Twin__AWS`, hub twins.sgit.ai.
- **Because it is a twin first.** An AWS-shaped interface on a vault; the live account is a second backend.
- **The same pattern as the S3 container.** The one twin that works today.
- **The rule: plural is the family, singular is the instance.** twins and aws.twin, hooks and tokens.hook.
- **Repositories follow it too.** `SGit-AI__Website__<Family>__<Instance>`, with the family singular.
- **Four hosts break it today.** Three under providers, one under games.
- **One correction.** On GitHub Pages each host gets its own certificate; no wildcard is needed.

## The decision: aws.twin.sgit.ai

The site proposed in [AWS from the vault](aws-from-the-vault.md) is called `aws.twin.sgit.ai`. Its repository is `SGit-AI__Website__Twin__AWS`, which follows the shape of `SGit-AI__Website__Hook__Tokens`, and its hub is [twins.sgit.ai](https://twins.sgit.ai/). The repository was created this morning, and the host already resolves.

## Why a twin, and not a console

The site is designed twin first, in three steps:

- **Build the twin.** An AWS-shaped interface, for S3, Lambda, EC2, IAM, billing and logs, whose backend is a vault.
- **Put the real connection in front of it.** As a second backend behind the same interface: a temporary IAM Identity Center session, pasted into the user's vault.
- **Everything built against the twin works against the live account.** Because the code that uses it is written against the interface, not the backend.

That is the same pattern as the one twin that already works. twins.sgit.ai describes it: "the container is a digital twin of S3, presenting the same S3-compatible API, so that code using boto3, the AWS CLI, or any S3 SDK believes it is talking to real S3, while the files are served from a vault, from local disk, or from memory, chosen as a swappable backend; the service's own code does not change." The AWS twin is the second instance of that pattern, not an exception to it.

What this gives the workflow:

- **Develop and test against the vault, with no credentials.** Every interface first works on data you can see and seed.
- **Rehearse before running live.** The first job, deploying the SG/Send server components to many accounts and regions, can be rehearsed against the twin.
- **Snapshots are commits either way.** "What changed between Monday and Friday" works the same for data from the live account and data seeded by hand.
- **An account graph.** Resources as nodes; a role and its policies, a function and its bucket, an instance and its security group, as edges.

## The options we rejected

- **aws.sgit.ai.** It loses the twin-first framing, which is the core of the design.
- **aws.platform.sgit.ai.** "Platform" names nothing in the estate: a namespace with one occupant.
- **aws.provider.sgit.ai.** Provider sites are reports, not tools. A companion report may come later, separately.

## The rule: plural for the family, singular for the site

- **Plural is the hub, the family.** `twins.sgit.ai`, `hooks.sgit.ai`, `providers.sgit.ai`.
- **Singular is one instance, at that moment in time.** `aws.twin.sgit.ai`, `tokens.hook.sgit.ai`, `elevenlabs.provider.sgit.ai`.
- **Repositories use the singular family name.** `SGit-AI__Website__<Family>__<Instance>`: `Hook__Tokens`, `Provider__ElevenLabs`, `Twin__AWS`.

Two other kinds of second-level host already exist, and the rule leaves them alone. API sites, like api.send.sgit.ai, are a site's own client code, released by version. Editions, like pt.newsroom.sgit.ai, are the same site in another language or for another audience.

## Held against the estate

Looking at every host, as in [the sgit.ai sites in numbers](the-sgit-ai-sites-in-numbers.md):

- **Following the rule.** `tokens.hook.sgit.ai`, `aws.twin.sgit.ai`, and the two demo sites under `demo`, all reserved, with no site yet.
- **Breaking it, under providers.** `elevenlabs.providers.sgit.ai` and `ungovr.providers.sgit.ai`, both live, and `openrouter.providers.sgit.ai`, listed on the hub and not serving.
- **Breaking it, under games.** `what-can-it-do.games.sgit.ai`, live since 8 September, whose repository, `Game__What-Can-It-Do`, already uses the singular.

The repositories are already right: every family repository uses the singular. It is only the hosts that need to move.

## A correction: DNS, not certificates

The first note on this said that each singular namespace needs its own wildcard certificate, because `*.sgit.ai` does not cover a second-level name like `aws.twin.sgit.ai`. The second half is true, and it applies to DNS as well. But these sites are on GitHub Pages, and there no wildcard certificate is needed. GitHub's documentation says that when a custom domain is set, "GitHub queues a job to request a TLS certificate from Let's Encrypt", one per domain, and uploads it itself.

What each host needs is its own DNS record, a `CNAME` pointing to the organisation's `github.io` domain, which is how the existing hosts work: there is no wildcard record under sgit.ai today. And that is the right way round, because GitHub says: "We strongly recommend that you do not use wildcard DNS records, such as `*.example.com`", as they "put you at an immediate risk of domain takeovers".

## What changes on twins.sgit.ai

The naming ruling on [twins.sgit.ai](https://twins.sgit.ai/naming/index.html) says a twin holds no credentials, and notes that "the S3 container genuinely blurs the line by being both an interface twin and a thing that holds backend access". The AWS twin makes it worth resolving that. The proposed paragraph:

A twin's interface never holds credentials. A twin can have a live backend; when it does, the credential belongs to that backend, not to the twin, and lives in the user's vault for the lifetime of the session (for AWS: a temporary IAM Identity Center session, 1–12 hours, 1 hour by default). The S3 container and the AWS twin are the two worked examples of this: interface first, backends swappable, live access as one backend among several.

And with it:

- **Keep the execution broker distinct.** The broker is a standing, credential-holding intermediary; a twin with a live backend borrows a session the user holds, for a limited time.
- **Watch the name.** Use "the AWS twin", in lower case, or add the capitalised form to the site's allow-list with its meaning.
- **Make the site a hub as well as the definition.** A page of the twins in place, each with its state: the S3 container, working, shipped by SG/Compute; the AWS twin, proposed; and the AWS, organisation, agent and 2FA twins that are specified or designed.
- **Decide whether the S3 container gets its own site.** `s3.twin.sgit.ai`.

## What changes on providers.sgit.ai

- **Move the instances to the singular.** `elevenlabs.provider.sgit.ai`, `ungovr.provider.sgit.ai` and `openrouter.provider.sgit.ai`.
- **Keep the plural hosts as redirects.** So existing links do not break.
- **Switch the canonical hosts first.** The hub's `bin/sync-providers.py` fetches from whichever host answers, and a build check fails if a link disagrees, so changing the links before the hosts would lock in the plural.
- **Later, perhaps, an AWS provider report.** Credentials bound by a clock, which AWS services answer a browser, and the cost of a named workload. Before adding it, check the hub's "no commercial relationship" disclosure against sgit.ai's [AWS page](https://sgit.ai/partnerships/aws.html).

The same move applies to the games family: `what-can-it-do.game.sgit.ai`, with the plural kept as a redirect.

## What changed here

[AWS from the vault](aws-from-the-vault.md) now uses `aws.twin.sgit.ai` throughout, in its title, summary, text and diagram, says the name is decided, and describes the twin-first design. The changes to twins.sgit.ai and providers.sgit.ai belong to those sites, and are listed above for them.

## What this does not claim

- **aws.twin.sgit.ai is not built.** The repository and the DNS record exist; the site does not.
- **The renames have not happened.** The provider and game hosts still use the plural.
- **The twins ruling is not changed yet.** The paragraph above is proposed.
- **The hosting facts are GitHub's.** From its documentation, read on 21 October 2026.

## Where this comes from

A naming discussion of 21 October 2026, captured as decisions the same day. [twins.sgit.ai](https://twins.sgit.ai/), its [naming ruling](https://twins.sgit.ai/naming/index.html) and [what is built](https://twins.sgit.ai/built/index.html); [providers.sgit.ai](https://providers.sgit.ai/); the repositories and DNS of every site; and GitHub's pages on [managing a custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site) and [securing a site with HTTPS](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https), read the same day. Related: [AWS from the vault](aws-from-the-vault.md), [the sgit.ai sites in numbers](the-sgit-ai-sites-in-numbers.md). Written up and checked by this site's agent, newsroom.writer; the editorial responsibility is mine.

## Threads

Site & engineering[This article as a graph →](graphs.md#plural-for-the-family-singular-for-the-site)

### Builds on

- [AWS from the vault: a proposed aws.twin.sgit.ai, where a temporary AWS session lives in the user's vault, the browser does the work, and AWS data finally has a place to go](aws-from-the-vault.md) A proposed aws.twin.sgit.ai: an AWS twin on a vault first, then a temporary AWS session from the user's vault.
- [The sgit.ai sites in numbers: 53 repositories, 45 live sites, 1,679 commits and 5,419 pages in eleven weeks, and what the shape of the estate says](the-sgit-ai-sites-in-numbers.md) All 53 sgit.ai site repositories counted: 45 live sites, 1,679 commits, 5,419 pages, growth in bursts and a long tail.

### Continued by

- [The sgit.ai sites in numbers: 53 repositories, 45 live sites, 1,679 commits and 5,419 pages in eleven weeks, and what the shape of the estate says](the-sgit-ai-sites-in-numbers.md) All 53 sgit.ai site repositories counted: 45 live sites, 1,679 commits, 5,419 pages, growth in bursts and a long tail.
- [AWS from the vault: a proposed aws.twin.sgit.ai, where a temporary AWS session lives in the user's vault, the browser does the work, and AWS data finally has a place to go](aws-from-the-vault.md) A proposed aws.twin.sgit.ai: an AWS twin on a vault first, then a temporary AWS session from the user's vault.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 236 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=236)

**Posting this article on LinkedIn?** The cover is [plural-for-the-family-singular-for-the-site.jpg](banners/plural-for-the-family-singular-for-the-site.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/plural-for-the-family-singular-for-the-site.html)*
