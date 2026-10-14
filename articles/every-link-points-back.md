# Every link points back: 566 links between 105 articles, 15 that point forward, and why an article should know what came next and what corrected it, sgit.ai

> I tend to write these articles in sequence, and I think of them as reading in sequence. Then I go back to one and realise there is no path from it to the next, because the earlier article cannot know what came after it. So we counted. Across the 105 articles on this site there are 566 links from one article to another, written into the text, and 551 of them point back in time. Only 15 point forward, and every one of those was added later, by an edit. 94 of the 105 articles are cited by a later one, 551 citations in all, and 11 of them are answered by a link the other way. Of 104 pairs of articles published one after the other, the later one links to the earlier one 42 times; the earlier one links to the later one 7 times. That is by design: a link is written when the article is written, and the future does not exist yet. The site already derives a Continued by list at the foot of every article, so the path exists, but it sits below the sources, it does not say why, and it treats a correction the same as a passing mention. Corrections matter most. We found three kinds: an article revised in place, which the version pages already show; a later article correcting an earlier one, of which there is one clear case and its earlier article does point to it; and the quieter one, a plan described in one article that a later article says has not happened. So this release adds What came next notes at the top of the four articles I wrote in a row today, and proposes four kinds of forward link, so that the graph of articles can be read in both directions.

*Source: <https://newsroom.sgit.ai/articles/every-link-points-back.html> · sgit.ai v0.7.87 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Every link points back: 566 links between 105 articles, 15 that point forward, and why an article should know what came next and what corrected it

# Every link points back: 566 links between 105 articles, 15 that point forward, and why an article should know what came next and what corrected it

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-13 · [article v1.0.0](versions/every-link-points-back.md) · [newsroom v0.12.24](https://newsroom.sgit.ai/admin/versions.html) · linksgraphscorrectionsversionsnavigationnewsroomanalysisreadingarticle

***Abstract:** I tend to write these articles in sequence, and I think of them as reading in sequence. Then I go back to one and realise there is no path from it to the next, because the earlier article cannot know what came after it. So we counted. Across the 105 articles on this site there are 566 links from one article to another, written into the text, and 551 of them point back in time. Only 15 point forward, and every one of those was added later, by an edit. 94 of the 105 articles are cited by a later one, 551 citations in all, and 11 of them are answered by a link the other way. Of 104 pairs of articles published one after the other, the later one links to the earlier one 42 times; the earlier one links to the later one 7 times. That is by design: a link is written when the article is written, and the future does not exist yet. The site already derives a Continued by list at the foot of every article, so the path exists, but it sits below the sources, it does not say why, and it treats a correction the same as a passing mention. Corrections matter most. We found three kinds: an article revised in place, which the version pages already show; a later article correcting an earlier one, of which there is one clear case and its earlier article does point to it; and the quieter one, a plan described in one article that a later article says has not happened. So this release adds What came next notes at the top of the four articles I wrote in a row today, and proposes four kinds of forward link, so that the graph of articles can be read in both directions.*

Every link points back. The links written into the text of 105 articles to other articles, counted by article number: 551 of 566 point to an earlier article; of 551 later citations, 11 are answered by a link the other way; and of 104 pairs published one after the other, the later links the earlier six times as often as the reverse.

## In short

- **I write in sequence, and the site reads one way.** An article links to what came before; it cannot link to what came after, because that did not exist.
- **551 of 566 links point back.** 15 point forward, in 14 articles, and every one was added by an edit.
- **94 articles are continued, few say so.** 551 later citations; 11 answered by a forward link.
- **Pairs written in a row.** The later links the earlier 42 times in 104 pairs; the earlier links the later 7 times.
- **The path exists, at the foot.** Every article ends with a derived Continued by list, below the sources, with no reason and no difference between a sequel and a mention.
- **Corrections are the sharper case.** An edit in place is versioned; a correction by a later article, or a plan that has not happened, is invisible from the earlier page.
- **The proposal: four kinds of forward link.** What came next, Corrected by, Status since, and Cited by, the first three at the top. This release adds the first kind to the four articles I wrote in a row today.

## The problem

The article that made me notice is [The policy draws the liability line](the-policy-draws-the-liability-line.md). I think it is a good article. But I wrote the next one, [A policy beside the prompt](a-policy-beside-the-prompt.md), straight after it, and that one takes the argument into how it would work in the real world. Someone reading the first had no way to know. Then [The human in the loop](the-human-in-the-loop.md) came after that, and then [The human in the loop is a spectrum](how-cheap-is-it-to-undo.md). Four articles, written in a row, meant to read in a row, and each one only knows about the one before.

That is not a bug. A link is written when the article is written. But in a graph of articles, it means every edge points one way in time, and a reader who lands on an older article, which is most readers arriving from a search or a share, is at a dead end exactly where the story continues. The same is true, and worse, when a later article corrects an earlier one.

## What the links say

So we counted, before writing anything else. The method: every link in the text of every article to another article on this site, from the markdown each was written in, not from the generated lists around it; one link per pair of articles; order by article number, which is the order they were published.

- **566 links between 105 articles.** 551 point to an earlier article. 15 point to a later one, in 14 articles. A forward link can only be added after the later article exists, so all 15 came from an edit.
- **94 of the 105 articles are cited by at least one later article**, 551 citations in all. 11 of those are answered by a link back the other way.
- **104 pairs of consecutive articles.** In 42 the later one links the earlier; in 7 the earlier links the later. 78 of those pairs were published the same day, and the numbers barely move: 31 and 7. When I write in sequence, the later piece usually says so; the earlier piece almost never learns.
- **22 runs of consecutive articles where each links the one before**, the longest five long, Nos. 66 to 70, with one forward link inside it.
- **The most cited articles link forward least.** [Introducing fractal semantic graphs](introducing-fractal-semantic-graphs.md) is cited by 23 later articles and links to none of them; [Footprint and blast radius](footprint-and-blast-radius.md) by 22, with none; [Six agents, one inbox](six-agents-one-inbox.md) by 21, with one.

The density has changed too. The five August articles average fewer than one link each to another article; the September ones about one and a half; in October most days average between about four and ten. The more there is to link to, the more each new article links back, and the more each older article falls behind what has been written about it.

## The path exists, at the foot

The site already does part of this. Every article ends with a Threads section, derived from the links at build time: Builds on, the articles it links to, and Continued by, the later articles that link to it. The liability line article does list A policy beside the prompt there. I did not see it, and I wrote both.

There are three reasons it is easy to miss. It is at the very end, after the limits and the sources, where most readers have stopped. It has no reason in it, only titles, so the article that continues the argument looks the same as the one that mentions it in a list of related pieces. And it has one kind: Continued by covers a sequel, a passing citation and a correction alike.

## Corrections are the sharper case

A forward link to a sequel is a convenience. A forward link to a correction is the record. I looked for corrections in two ways: the version history sgit.ai keeps for its articles, and every sentence where a later article links an earlier one near a word like correct, wrong, revised or no longer. That second scan found 45 sentences; reading them, most use the words in other senses. What is left falls into three kinds.

**Revised in place.** Of the 97 articles whose history sgit.ai keeps, 62 have more than one version. [The passkey opens the vault](the-passkey-opens-the-vault.md) went from v1.0.0 to v1.4.0 in two days, the last one "revised after the lab", and the article says what changed. Later articles, [The vault is live](the-vault-is-live.md) and [Not a straight line](not-a-straight-line.md), link to the revised article. This kind is already handled: the version and diff pages show the edit, and the page a reader lands on is the corrected one.

**Corrected by a later article.** One clear case: [If somebody built a company on code review](if-somebody-built-a-company-on-code-review.md) answers a reader's questions on [Code review as a fractal semantic graph](code-review-as-a-fractal-semantic-graph.md), and that earlier article was edited to point at it as "the follow-up that answers a reader's seven questions and corrects this article on refactoring". That is exactly the right thing to do. It is also in a list at the end of the article, so a reader who stops halfway has read the part that was corrected and not the pointer.

**Status since.** The quieter kind, and I think the most common. [The site is an inbox](the-site-is-an-inbox.md) describes personas with their own key pairs as part of the plan. [Sixteen notes I did not want to lose](sixteen-notes-i-did-not-want-to-lose.md), written the next day, says the reader has no key pair yet. Neither article is wrong on its day. But a reader of the first has no way to know the plan has not happened, and this is the kind of drift that turns into a quoted claim.

## Four kinds of forward link

Four articles written in a row on 13 October: each was written with a link back, and none could link forward. This release adds a What came next note to the top of the first three. Below, the four kinds of forward link proposed, three at the top of the page and one at the foot.

What I would like, for every article, is to be able to see what came after it, and to be told when something later changed what it says. Concretely:

1. **What came next**, at the top: when a later article continues this one, one line saying what it adds. Added by the release that publishes the later article, as part of the same commit.
2. **Corrected by**, at the top and stronger: when a later article, a lab or a reader finds this one wrong, the way a newspaper prints a correction. An edit in place already has its versions; this is for a correction that lives somewhere else.
3. **Status since**, a dated note: the plan here has happened, has not, or has changed, with the article that says so.
4. **Cited by**, the rest, which stays in the Threads list at the foot, separate from the first three.

The first is done for the chain I wrote today: The policy draws the liability line, A policy beside the prompt and The human in the loop each now open with a note pointing to the next. The other three need a better place in the page than a line of text, and that is a job for the session that works on the reading experience. In graph terms, the cross-article links could carry a relation the way the edges inside each article's graph already do, continues, corrects or cites, so a validator could warn when a later article says it corrects an earlier one and the earlier one does not say so.

And it does not need doing for everything at once. Start from the most recent articles and go down the line, a few at a time, taking turns with the new writing. The counts above are the baseline to measure against.

## What this does not claim

- **The counts are of links written in the text.** The generated lists, Threads and Related, are not counted; one link per pair of articles; article order is by number.
- **The correction scan is by words.** It finds sentences that say correct, wrong or revised near a link; a correction that uses other words would be missed.
- **The version counts are sgit.ai's.** The articles written here since the move have their versions in this repository, and are not in the 97.
- **"Status since" is one example.** I have not counted how many plans in older articles have since happened or not.
- **The four kinds are a proposal.** Only the What came next notes on three articles are built, in this release.

If you run a site where the old pages need to know about the new ones, or you have a better pattern for corrections than a note at the top, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from

A voice memo of mine on 13 October 2026, prompted by The policy draws the liability line, written by this site's agent in the voice of this site. The argument and the editorial responsibility are mine. The counts are from the source markdown of the 105 articles numbered in this site's articles/ids.json at v0.12.23, read by a script that parses article links; the versions are from sgit.ai's admin/build/article_versions.json; the Threads section is built by sgit.ai's build_pages.py.

## Threads

Site & engineeringGraphs & knowledge[This article as a graph →](graphs.md#every-link-points-back)

### Builds on

- [The policy draws the liability line: an answer to Ralf Thomas on agent accountability, and why every agent in a loop should take a behaviour policy beside its prompt](the-policy-draws-the-liability-line.md) An answer to Ralf Thomas: the shell game works because nothing is written down, and a behaviour policy's explicit prohibitions move the liability line.
- [A policy beside the prompt: a proposal that every agent takes a behaviour policy as an input, with enforcement and liability attached, and why aviation and payments say the vendors should want it](a-policy-beside-the-prompt.md) A proposal: every agent takes a behaviour policy beside its prompt, which the vendor accepts and answers for, as aviation and payments learned to.
- [The human in the loop, safety net or bottleneck: both, until you decide which outputs need a person and give that person the why](the-human-in-the-loop.md) Checking every output is a bottleneck and a weak safety net; put the person where it cannot be undone, and let controls do the rest.
- [The human in the loop is a spectrum: how cheap it is to undo decides where a person belongs, and why the newsroom ships on its own while my email still waits for me](how-cheap-is-it-to-undo.md) How much to let an agent ship on its own depends on how cheap it is to undo and how mature the controls are, and both of those move.
- [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](introducing-fractal-semantic-graphs.md) A fractal semantic graph has no privileged level and no single schema: each world keeps its own vocabulary and connects to others through named edges.
- [Footprint and blast radius: what the agent actually did, and what it would have cost](footprint-and-blast-radius.md) Footprint is what an agent actually did, read afterwards from logs and vault history; blast radius is what a row of its reach would cost the business today.
- [Six agents, one inbox: what a real multi-agent setup taught me about access policies](six-agents-one-inbox.md) An access policy for an agent is only as real as its worst row: every rule in a real six-agent setup, graded by how it is enforced today.
- [The passkey opens the vault: a door per path, a master vault for every user, and no server of ours](the-passkey-opens-the-vault.md) Tested: a passkey's PRF bytes compute a door that holds the master's key, and a different path to the same passkey gives different bytes, so a door per path.
- [The vault is live: from a design on 11 October to a reader's vault on newsroom.sgit.ai by two in the morning, and how all of it fits together](the-vault-is-live.md) The reader's vault runs on newsroom.sgit.ai: a passkey opens three real vaults, each device writes one file, and the architecture is drawn as it stands.
- [Not a straight line: working for RiskMandate by working on the newsroom, and why the thinking is never wasted](not-a-straight-line.md) Working on the newsroom solved RiskMandate's oldest problem in two days: progress is not a straight line, and the thinking is never wasted.
- [If somebody built a company on code review: how I would do it, and why it is only now possible](if-somebody-built-a-company-on-code-review.md) A reader's seven questions answered as a company plan: one reader for every layer, review as a science, and the layers as the customer's own.
- [Code review as a fractal semantic graph: source code is already one, and the review should read every layer of it](code-review-as-a-fractal-semantic-graph.md) Source code is layers within layers, each a graph with its own vocabulary; code review should read a change at every one, and a vault shows it done on real code.
- [The site is an inbox: deciding before reading, marks that build the reader's own graph, and why I could not write this brief until the vault existed](the-site-is-an-inbox.md) The site as an inbox that starts empty: decide fast before reading, mark slowly while reading, build a graph you own, and sign what you send to the newsroom.
- [Sixteen notes I did not want to lose: a request to send from any browser to my vault, why identity is still this hard, and how two more wires became a product line](sixteen-notes-i-did-not-want-to-lose.md) Sixteen notes stuck in a browser with no passkey led to a request: let any browser send to my vault, by link, text or QR code.

### Continued by

- [Knowledge that maintains itself: semantic graphs for an organisation's policies and internal knowledge, briefing people and agents from the graph, and vaults to carry the brief](knowledge-that-maintains-itself.md) Fractal semantic graphs for policies and internal knowledge: brief people and agents from the graph, maintain it in a loop, carry the brief in a vault.
- [Four frameworks, one agent: iason's comparison of the OECD classification, the NIST AI RMF, Japan's guidelines and the EU AI Act, read against what runs here, with the evidence and the graphs](four-frameworks-one-agent.md) iason's comparison of four AI risk frameworks, mapped to the behaviour policy, the footprint and the graphs that run here, with the status of each row.

[All articles](index.md) · [All graphs](graphs.md)

Article No. 106 · [start a reading list with it](https://newsroom.sgit.ai/for/make.html#r=106)

**Posting this article on LinkedIn?** The cover is [every-link-points-back.jpg](banners/every-link-points-back.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/every-link-points-back.html)*
