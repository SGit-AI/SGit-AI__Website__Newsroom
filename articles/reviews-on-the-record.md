# Reviews on the record: other models, the editor and the desk check every article, and never the same text twice, sgit.ai

> The publishing workflow here works, and I have come to like it as a way to answer people: an article is a reply I can point to. But the articles are written by one model, with a lot of context, and some things fall through, a figure that is a little off, a sentence I would never say. So this adds review, as a record. There are published criteria that any reviewer reads first, an agent from another vendor, an open-weight model, me, and later the journalists on the desk: are the facts right, is it my voice, are the claims and limits honest, are the conversions right, is the article still in good health, is anyone named who should not be. Each review is one file in the article's own folder, about one text of the article, written once and never edited, and the newsroom answers every finding: fixed in which version, declined and why, or open. The unit of work is the reviewer, the article and its text, so the same reviewer never reviews the same text twice; it takes the next five, newest first, from a status file that lists every article's current hash and the reviews it has, and it reads its own past reviews before it starts. Every article now has a Reviews section that shows who reviewed it, at which version, and what happened to what they found. My own reading, sign-offs and later notes use the same record, which keeps an article alive: I can go back and say I got it wrong, or that it came true. Signed readers who confirm or dispute an article are the next step, and an article of their own.

*Source: <https://newsroom.sgit.ai/articles/reviews-on-the-record.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Reviews on the record: other models, the editor and the desk check every article, and never the same text twice

# Reviews on the record: other models, the editor and the desk check every article, and never the same text twice

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-18 · [article v1.0.0](versions/reviews-on-the-record.md) · [newsroom v0.12.107](https://newsroom.sgit.ai/admin/versions.html) · newsroomreviewsqualityagentseditorarticle

***Abstract:** The publishing workflow here works, and I have come to like it as a way to answer people: an article is a reply I can point to. But the articles are written by one model, with a lot of context, and some things fall through, a figure that is a little off, a sentence I would never say. So this adds review, as a record. There are published criteria that any reviewer reads first, an agent from another vendor, an open-weight model, me, and later the journalists on the desk: are the facts right, is it my voice, are the claims and limits honest, are the conversions right, is the article still in good health, is anyone named who should not be. Each review is one file in the article's own folder, about one text of the article, written once and never edited, and the newsroom answers every finding: fixed in which version, declined and why, or open. The unit of work is the reviewer, the article and its text, so the same reviewer never reviews the same text twice; it takes the next five, newest first, from a status file that lists every article's current hash and the reviews it has, and it reads its own past reviews before it starts. Every article now has a Reviews section that shows who reviewed it, at which version, and what happened to what they found. My own reading, sign-offs and later notes use the same record, which keeps an article alive: I can go back and say I got it wrong, or that it came true. Signed readers who confirm or dispute an article are the next step, and an article of their own.*

Reviews on the record. Reviewers, agents from other vendors and open-weight models, the editor, the desk, and later signed readers, read the published criteria, take their next five articles from a status file, write one record per article in the article's folder, and send it by pull request, by commit or by hand; the newsroom answers each finding, and the article's page shows the reviews and the answers. The unit of work is the reviewer, the article and its text.

## In short

- **The workflow works; review is what it lacks.** One model writes, with a lot of context, and some things fall through.
- **Published criteria, for any reviewer.** Facts, voice, claims and limits, conversions, health, people.
- **A review is a record.** One article, one text, one reviewer, one file, in the article's own folder.
- **Never the same text twice.** Each reviewer takes its next five, newest first, and reads its past reviews first.
- **The newsroom answers every finding.** Fixed in which version, declined and why, or open.
- **Every article shows its reviews.** Who, when, at which version, and what happened to what they found.
- **The editor and the desk use the same record.** A sign-off, a comment, and later "I got this wrong".
- **Signed readers are next.** Confirm, dispute, agree, disagree, under their own key.

## Why review now

The way this site publishes is working well. I record a memo or point at something I read, an agent researches it and writes it in my voice, the build checks what it can, and a release goes out. What I like most is something I did not plan: an article has become the way I answer people. When someone asks what we do, or pushes back on an idea, I can send them a page that answers properly, with the sources, and that stays answered for the next person.

But almost every article here is written by one model, and a model with a lot of context does more and misses more. Today I asked for a check on phrases like "the clearest example I have seen", because one had got into an article and it is not something I would say. That was caught by me reading. Most things will not be, unless something else reads.

So I want a second pass on every article, by readers that are not the writer. Other models first: a different model from the same vendor, a model from another vendor, an open-weight model, each reading the same article in its own way. Then me, and later the journalists on the desk. And I want it to be cheap to run, so I can point a reviewer at the site whenever I have credits to spare, without it starting from the beginning every time.

## What a review checks

The criteria are [published](https://newsroom.sgit.ai/reviews/criteria.html), and also [as markdown](https://newsroom.sgit.ai/reviews/criteria.md), so that I can point any agent at one address and it can read them before it starts. Six questions, each answered pass, issues or not checked:

1. **Facts.** Every number, name, date and quote against the source it links; every link for the point it is cited for; every count, counted again.
2. **Voice.** Would I say it? First person, honest about where I stand, plain words; and not the things I would not say: superlative self-claims, praise, absolutes without a count, overstated feelings, a forecast stated as a fact.
3. **Claims and limits.** What is built, what is documented and what is proposed, marked as such; and whether *What this does not claim* names the real weaknesses.
4. **Conversions and translations.** Currencies and units with their basis and date, percentages that add up, the same number the same everywhere.
5. **Health.** Is the article still right today: links that moved, statements that went stale, summaries that no longer match.
6. **People.** Nobody private named, no private message quoted, nothing that looks like a key.

Each finding has a severity, the section, the exact words from the article, what is wrong, the evidence and the smallest fix. "Not checked" is allowed and asked for: a review that checked three things properly is worth more than one that skimmed six.

## One article, one text, one reviewer

The part I care most about is that this scales, and scaling here means not doing the same work twice.

A review is one file, in the article's own folder of reviews, named by its date and its reviewer. It is written once by its reviewer and never edited. It says which text it reviewed, by a hash of the article's sections, so if the article changes later the review stays on the page, marked as about an earlier text.

The unit of work is the reviewer, the article and that hash. A reviewer never gets the same article at the same text twice. It does not review the whole site either: it takes its next five, newest first, from [a status file](https://newsroom.sgit.ai/reviews/status.json) that lists every article's current hash and the reviews it already has. Articles it has never read come first; articles that changed since it read them come after. Before it starts, it reads its own past reviews and the newsroom's answers to them, so it does not raise again what has already been answered. With the repository, the same list is one command: `python3 admin/build/reviews.py --next <reviewer> --batch 5`.

That is what makes it a background job rather than a project. Once it is stable, a reviewer comes along, sees what is new, does five, and leaves.

## How a review arrives

There is more than one way, and I do not want to choose one too early.

- **A pull request**, touching only review files. For an agent from another vendor this is the best fit today: it is attributable, it is reviewable, and the newsroom can check it with `reviews.py --check` before it is merged.
- **A commit**, by an agent already working in the repository, after the same check.
- **By hand.** An agent with no repository access writes the JSON, and I hand it over.
- **A vault**, later. The append lane from [the editor's channel](the-editors-channel.md) works for this too: a reviewer can send without an account, sealed so that only the newsroom can read it.

## The newsroom answers

A finding with no answer is just a complaint. So every finding gets one, in a status file per article that only the newsroom writes: fixed, with the version that fixed it; declined, with the reason; or open. The reviews hub lists every open finding, and the daily pass from [the editor's channel](the-editors-channel.md) is the natural place to work through them, with the same rule as any other change here: what is cheap to undo is fixed and released, and anything that changes an argument goes to me.

Every article page now has a **Reviews** section, after the threads: who reviewed it, when, at which version, the verdict, a sentence of summary, and how many findings were fixed, declined or still open, with a link to the record itself.

## People on the record

This is not a comments section. Anyone commenting on anything is a different feature, and maybe one we add one day. This is comments on the record: a review by someone who said who they are, against criteria everyone can read, kept with the article.

My own reviews use the same file. When I have read an article and it is right, that is a review: an approval, by the editor, at that version, which is the sign-off [the editor's channel](the-editors-channel.md) proposed. When I disagree with part of it, that is a comment with a finding. When the desk has journalists, they review the same way, with their own name and their own opinion, and their reviews sit beside mine and the agents'.

And it works backwards in time, which I think is the most interesting part. I can go back to an article from a year ago and add a note on the record: I got this wrong; or, this came through, here is when. The article stays what it was, its history stays with it, and it stays alive and relevant instead of being something nobody touches after the week it was published.

The next step is readers: signed readers, with a key of their own, who confirm or dispute an article, agree or disagree with it, and whose reviews count because they are signed. That needs the key pairs from [the editor's channel](the-editors-channel.md), and it deserves an article of its own.

## The first run

The first reviewer was another model, from the same vendor as the one that writes the articles, given the criteria and its first batch from `reviews.py --next`: the five newest articles. It took about nineteen minutes and wrote five records.

- **One approval and four approvals with changes.** [The editor's channel](the-editors-channel.md) had no findings. The other four had 18 between them: 4 medium and 14 low, none high.
- **The medium ones were real.** A quote attributed to Google linked to coverage that did not carry it; Mozilla's latest audited statements are for 2024, not 2023; a report's link had started redirecting to a vendor's product page; and riskmandate.ai's front page says "Enforced in real time" while [what can your agent reach?](what-can-your-agent-reach.md) says RiskMandate is never in the request path, without saying how the two fit.
- **The low ones were the kind I would have missed.** "Public cloud software companies" where the source says publicly traded ones; Wrangler's 18 months counted from the wrong date; a version number linked to a page that does not give it; three sentences of the kind I asked to stop today: "has never been enough", "the best thing models have done", "the fastest way I know".
- **It checked as much as it found.** It counted curl's 239 vulnerabilities again and got the same 49, and reproduced the CVE counts from NVD's API exactly. Saying what held is as useful as saying what did not.

Every finding was checked and fixed in the same release that published this article, and each article's Reviews section says so. Because the fixes changed the text, those reviews now show as reviews of an earlier text, which is what the hash is for: the next batch for that reviewer starts with articles it has never read.

It also reviewed the criteria, unasked, and its points went straight into version 1.1: which text a quote is checked against, what each verdict means, whether naming a product the article is about breaks the rule on model names, what to do when there is nothing to convert, and how severe a weak link is.

## What this does not claim

- **Review does not make an article right.** It makes what was checked, and what was found, visible.
- **One reviewer, one batch so far.** Five articles, by one model; the criteria are version 1.1 and will keep changing as more reviewers use them.
- **Reviewers are models, and models make mistakes.** A finding is a claim for the newsroom to check, not a verdict.
- **A hash is not a signature.** It says which text was reviewed, not who reviewed it; records are attributed by who sent them until reviewers sign.
- **Nothing reviews the reviewers yet.** If two reviewers disagree, the newsroom answers both, and I decide.
- **Signed readers are a proposal.**

If you want to point your own agent at the criteria and send a review, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai), or open a pull request.

## Where this comes from

A voice memo from me on 18 October 2026. The criteria: [/reviews/criteria.md](https://newsroom.sgit.ai/reviews/criteria.md), version 1, written from this site's [article guide](https://newsroom.sgit.ai/admin/content/articles/README.md) and the wording check in `admin/build/wording.py`. The status file: [/reviews/status.json](https://newsroom.sgit.ai/reviews/status.json). The code: `admin/build/reviews.py`. Related: [the editor's channel](the-editors-channel.md), [how cheap is it to undo](how-cheap-is-it-to-undo.md), [the human in the loop](the-human-in-the-loop.md), [three policies for an agent](three-policies-for-an-agent.md). Written up and checked by this site's agent; the editorial responsibility is mine.

## Threads

Vaults & methodAgents & policy[This article as a graph →](graphs.md#reviews-on-the-record)

### Builds on

- [The editor's channel: what I read, sign off and want changed, sent to the newsroom's agent in a vault](the-editors-channel.md) A key makes a browser an editor's: reads, sign-offs and fixes go to a vault, a daily pass acts and replies, and five lanes set what any reader sends.
- [What can your agent reach? RiskMandate and the Agent Behaviour Policy, explained for the person who has to decide](what-can-your-agent-reach.md) RiskMandate and the Agent Behaviour Policy in plain words: what it does, why it is not real time, which agents it covers, and how it gets into the room.
- [The human in the loop is a spectrum: how cheap it is to undo decides where a person belongs, and why the newsroom ships on its own while my email still waits for me](how-cheap-is-it-to-undo.md) How much to let an agent ship on its own depends on how cheap it is to undo and how mature the controls are, and both of those move.
- [The human in the loop, safety net or bottleneck: both, until you decide which outputs need a person and give that person the why](the-human-in-the-loop.md) Checking every output is a bottleneck and a weak safety net; put the person where it cannot be undone, and let controls do the rest.
- [Three policies for an agent: behaviour says what it may do, decision says who chooses, workflow says in what order](three-policies-for-an-agent.md) Behaviour says what an agent may do, decision who chooses at a branch point, workflow in what order. Zoom into one ABP cell and it becomes both.

### Continued by

- [Three companies, three LinkedIn pages: the brief, the drafts and the first posts, in the open](three-linkedin-pages.md) Three companies, no LinkedIn pages: the decisions, every drafted field with its count, thirty first posts already written, and a new profile, in the open.
- [Search as navigation: walking the newsroom's graph with no model, and why a clean graph should beat vectors](search-as-navigation.md) Search as a walk through the newsroom's graph: chips, exact suggestions, five views and a pane that shows the working, with no model yet.
- [On the record: signed opinions from experts, paid when readers value them, and a share for the people whose ideas an article uses](on-the-record.md) Experts go on the record with signed opinions, readers pay for the ones they value, and the people whose ideas an article uses get a share.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 184 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=184)

**Posting this article on LinkedIn?** The cover is [reviews-on-the-record.jpg](banners/reviews-on-the-record.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/reviews-on-the-record.html)*
