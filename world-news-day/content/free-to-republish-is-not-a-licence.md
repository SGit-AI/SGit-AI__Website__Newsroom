On 28 September, for World News Day, WAN-IFRA and the Canadian Journalism Foundation published {{articles}} commissioned opinion pieces by editors, publishers and directors from Manila to Managua, and made them free to republish. In a year when almost nobody in this industry gives anything away, {{words}} words were given away, by people whose day job is deciding what stays behind a paywall.

That is the story, and it should be said first, because everything below is a technical complaint about a generous act.

We fetched all {{articles}}, froze the bytes, hashed them, described them and published the description. We did not republish a word of the prose. Then we asked the question a machine asks: **under what licence?**

## There isn't one

All {{articles}} carry a permission. Not one carries a licence.

The permission is a sentence at the foot of the prose — free to republish or translate in full, provided translations remain faithful to the original meaning, minor edits for length or house style permitted on the same basis. It is clear, it is generous, and it appears in {{wordings}} slightly different wordings across the corpus.

What it is not is a licence. It has no name, no version, no URL and no identifier. There is nothing to cite in a rights field, nothing to point a lawyer at, nothing for a machine to match. Across all {{articles}}: {{cc}} mention Creative Commons. {{rel_license}} carry `rel="license"`. {{copyright_notice}} carry a copyright notice naming a holder — not even an "all rights reserved".

And the terms are stated twice, differently. The articles require republication **in full** and never mention credit. The announcement that points at them requires **appropriate credit** and never says in full. A newsroom that follows one is not following the other.

That is not pedantry, it is the whole of the problem. Consider a small paper in Ohio that wants to run one of these pieces about local news. "In full" and "minor edits for house style" are in tension; nobody says whether a standfirst is an edit; nobody says who to credit or how. So the editor does the rational thing and writes to ask — except, as we will come to, there is nobody to write to. Or consider a translator in Manila, working in a language the author does not read, told that the translation must remain "faithful to the original meaning". Who decides? Under CC BY, none of those questions arise, because a decade of practice has already answered them.

## The machine-readable version is one line away

Here is the part that is genuinely frustrating, because almost all of the work is already done.

Every one of the {{articles}} pages already ships schema.org structured data as JSON-LD, with an Article node, generated automatically by the site's own SEO plugin. Nobody had to decide to do that; it happens. schema.org has carried a `license` property since 2015, alongside `copyrightHolder`, `copyrightNotice`, `usageInfo` and `isAccessibleForFree`.

**{{ldjson_licence}} of {{ldjson}} use any of them.**

The record is being written on every page already. Adding the terms to it is one line:

    "license": "https://creativecommons.org/licenses/by/4.0/"

There is more that is nearly there. worldnewsday.org serves the entire corpus as structured JSON at `/wp-json/wp/v2/posts` — every piece, with its title, dates and full body, in a form any program can read. It is open, undocumented and unadvertised: a machine-consumable edition that exists by accident of the platform rather than by a decision to publish one. It carries no licence field either. The taxonomy is a single category and a single tag across all {{articles}}, so the corpus has no topical classification of its own. And the structured author field is wrong on {{authorfield}} of the {{articles}}: on one it gives the CMS account name `329976pwpadmin` where a person's name should be.

A machine-readable field that is wrong twice in {{articles}} is worse than no field, because nothing on the page tells a reader which to believe.

## What {{articles}} of the most senior people in news said, counted

Read one at a time, these are opinion pieces. Counted together they are something more useful: a picture of what the people who run the world's newsrooms currently believe is worth saying.

{{truth}} of {{articles}} are about truth and facts. {{ai}} raise artificial intelligence. **{{copyright_theme}} mention copyright or licensing at all** — in a corpus whose central anxiety is machines taking journalism's work without paying for it, and which is itself published without a licence.

Then the count this publication exists to make. **{{nolinks}} of the {{articles}} offer the reader no outbound link whatsoever.** Not one anchor in the article body. Across the whole corpus there are {{total_links}} links, and of the {{domains}} distinct domains cited between them, **no two pieces point at the same one**. There is no shared evidence base here. {{articles}} arguments for why the public should trust journalism, and the reader is asked to take almost all of it on the author's word.

That is not an accusation. An 800-word commissioned op-ed is not investigative reporting and nobody promised footnotes. It is the ordinary form. That is exactly the point: the ordinary form gives a reader nothing to walk.

## And no way to reach anyone

We wanted to send this piece to the people who wrote those. So we looked for a route.

Not one of the {{articles}} pages offers a way to reach its author or its publisher. No contact address, no author URL in the structured record, no press line. We went to the organisations' own sites instead — one hop each, rules published before the looking started, organisations and never people. Of {{orgs}} organisations named in the authors' own role lines, we could establish a site for most and publish a role address for {{addresses}}. {{reachable}} of the {{authors}} authors have any published route at all, and every one of those routes goes through an organisation.

{{articles}} pieces published to be spread, and the corpus carries no way back to the people who wrote them.

## This is not a gotcha

We are not a neutral party. We are building a stack that argues facts should carry their provenance, that corrections should propagate to whatever they disprove, and that the person who did the original work should be paid when a machine uses it. Read these {{articles}} pieces together and the striking thing is not disagreement — it is that the diagnosis is shared, precisely, across continents and business models. Trust is eroding. Truth is contested. AI is taking the work. The model is broken.

What is almost entirely absent is a **mechanism**. Nobody in the corpus proposes a way by which a correction reaches what it disproved, a fact carries its provenance, or the fact's creator gets paid when a model uses it. And the {{articles}} pieces are themselves the worked example of the gap: published to be spread, with no machine-readable statement of how.

We should say what we have not built, because the same standard applies to us. The payment rails are a design. Trust-as-a-service is a design. What runs is this: sources fetched, frozen and hashed; claims that walk back to bytes; gates that fail the build when a number stops re-deriving. That is the part we can show, so this is a demonstration on somebody else's corpus rather than a pitch.

## What it took, and what it would take

It took an afternoon. The {{articles}} pieces and their {{frozen}} frozen files are hashed and registered; the corpus is described as data; the themes come from {{lexicon}} published regular expressions, so you can disagree with the classification precisely rather than in general; the whole thing is a graph of {{nodes}} nodes and {{edges}} edges, {{triples}} triples, every verb with a named inverse and a Portuguese form. It is one download of {{vault_files}} files and {{vault_mb}} MB, with a SHA-256 you can check before you open it. Our description is CC BY 4.0, named and declared in the fields we are asking you to use. Your prose is not ours and is not in it.

For the corpus itself, three things would close the gap:

1. **Name the licence.** "In full, faithful to the original meaning" is close to CC BY-ND with a translation permission; "with appropriate credit" is CC BY. Either is a URL, a version, and a decade of practice, instead of a sentence to interpret. Publishing the not-quite-right named licence beats publishing none.
2. **Put it in the JSON-LD you already ship.** One line in a record that is already generated makes {{words}} words of deliberately open material discoverable, indexable and usable *as* open material, by every machine that reads the page.
3. **Say it once.** One canonical statement of the terms, linked from every piece and from the announcement — rather than two wordings on the articles and a third on the page that points to them. And put a contact on it.

## One more thing, about being wrong

An earlier version of this section said the announcement page was the one page in the beat a machine could not read. We had tried twice and been refused twice by a JavaScript-challenge firewall. Going back to the same host for an unrelated reason, it answered on the third attempt and gave us the whole page.

So we withdrew the claim, recorded what we had said and why it was wrong, wrote down the rule it produced — a refusal observed twice is a fact about two attempts, not a property of a page — and added a gate that fails the build if the withdrawn claim ever appears again without the correction beside it. It is on the method page, permanently, with the version number that carried the error.

That is the standard we are asking for, and the reason to ask for it out loud is that it is cheap to meet and it is checkable. Everything above is derived from bytes anyone can re-hash. If something here is wrong, the repository is open, the data files are plain JSON, and corrections are recorded rather than quietly edited away.

Tell us where we are wrong, and it changes.
