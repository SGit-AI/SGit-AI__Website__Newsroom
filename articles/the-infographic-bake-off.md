# The infographic bake-off: which image model for which job, judged blind on 10 October 2026, sgit.ai

> The articles here are moving from code-drawn figures to infographics made by image models, and the question was which model, for which job, at what cost. So we ran a bake-off. Every image-output model on OpenRouter on 10 October 2026, its auto-router and our own code-drawn renderer were given the same briefs from one article, from an eighteen-word stat card to the whole 2,800-word article, plus an edit, a UI component, a brand slide and a three-slide deck. Five rounds, models cut after each; 101 images, every one judged blind by a Designer agent; every cent recorded, $10.44 in all; an Accountant and a Data Scientist on the numbers. The result is three models and guidance. Nano Banana 2.1, at four cents an image, for concept slides, charts and decks. Gemini 3 Pro Image, at fourteen cents and twenty seconds, when you are in a hurry. GPT-5.4 Image 2, at seventeen to twenty-three cents and a minute and a half, for anything that starts from a document or where every character is specified. Choose the model by the job, not by the budget.

*Source: <https://newsroom.sgit.ai/articles/the-infographic-bake-off.html> · site v0.7.39 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / The infographic bake-off: which image model for which job, judged blind on 10 October 2026

# The infographic bake-off: which image model for which job, judged blind on 10 October 2026

By [Dinis Cruz](https://sgit.ai/about/index.md) · 2026-10-10 · [article v1.0.0](versions/the-infographic-bake-off.md) · [site v0.7.30](https://sgit.ai/admin/versions.md) · infographicsimage-modelsopenroutergeminigpt-imageevaluationcostnewsroomdesigneraccountantdata-scientistarticle

***Abstract:** The articles here are moving from code-drawn figures to infographics made by image models, and the question was which model, for which job, at what cost. So we ran a bake-off. Every image-output model on OpenRouter on 10 October 2026, its auto-router and our own code-drawn renderer were given the same briefs from one article, from an eighteen-word stat card to the whole 2,800-word article, plus an edit, a UI component, a brand slide and a three-slide deck. Five rounds, models cut after each; 101 images, every one judged blind by a Designer agent; every cent recorded, $10.44 in all; an Accountant and a Data Scientist on the numbers. The result is three models and guidance. Nano Banana 2.1, at four cents an image, for concept slides, charts and decks. Gemini 3 Pro Image, at fourteen cents and twenty seconds, when you are in a hurry. GPT-5.4 Image 2, at seventeen to twenty-three cents and a minute and a half, for anything that starts from a document or where every character is specified. Choose the model by the job, not by the budget.*

The bake-off's conclusion, drawn by the model it recommends for this job (GPT-5.4 Image 2, given the conclusion as a 263-word document). The blind judge scored it 9 out of 10 and would publish it as it is.

The articles on this site have carried figures drawn by code for months: diagrams from Mermaid, charts from SVG, decks from a renderer with fixed layouts. They are exact and they cost nothing, and they look like what they are. Some articles have also carried infographics made by an image model, one at a time, by hand. The next step is to make that part of the newsroom's workflow, which means an agent choosing a model, writing the brief and checking the result, every day.

That needs an answer to a plain question: which model, for which job, at what cost? So on 10 October we ran a bake-off, and this is what it found.

## In short

- **The field.** Every image-output model OpenRouter offered on the day: five from Google, three from OpenAI, its auto-router, and our code-drawn renderer as a $0 control. None of the image models is free.
- **The briefs.** Eleven, all from one article ([Re-anchoring](re-anchoring-agent-behaviour-policies.md)), from 18 words to 2,800: a stat card, a concept slide, a diagram with exact labels, a chart with fourteen numbers, a document, the whole article, an edit, a UI component, a brand slide, a three-slide deck, and the conclusion of the bake-off itself.
- **The method.** Five rounds, models cut after each. Every image judged blind by a Designer agent: a fact check of every required string, anything invented, six criteria and an overall score. OCR as an independent check. Every cost from OpenRouter's own accounting.
- **The bill.** 101 images, **$10.44**. Half of it paid for images the judge would not use.
- **The answer.** Nano Banana 2.1 for concept slides, charts and decks (about $0.04 an image). Gemini 3 Pro Image when speed matters (about $0.14, 20 seconds). GPT-5.4 Image 2 for documents, whole articles, edits, components and brand slides (about $0.17 to $0.23, 60 to 120 seconds).
- **The surprise.** Attaching slide 1 to every later slide of a deck fixed the hardest problem, consistency, for every model.
- **Everything is in a vault**: the briefs, all 101 images, every score and reason, the ledger, the analysis and the guidance, as an app: the [Infographic bake-off vault](https://sgit.ai/demos/vaults/infographic-bakeoff/index.md).

## The team

Four roles, each an agent with a role file. The **Designer** is adapted from the [SG/Send team's Designer](https://github.com/the-cyber-boardroom/SGraph-AI__App__Send/tree/HEAD/team/roles), whose first principle is that design is how it works: an infographic that is beautiful and wrong has failed. The judges saw copies of each image under a random id, never the model's name, and checked every required word and number before scoring anything. The SG/Send team has no accountant or data scientist, so both were written for this run. The **Accountant**'s rule is that a failed image was still paid for, so the number that matters is cost per *usable* image, not price per image. The **Data Scientist** makes the cut after each round, and must not promote or drop a model on a difference smaller than the noise.

## Round 1: who can put the right words in a picture?

Everyone got three short briefs. On the diagram, with five exact labels, the spread was wide:

The same diagram brief for all ten contestants, with the blind score. Two models ignored the requested 16:9 and returned a square that cut off boxes at both ends; one painted a muddy gradient; one misspelled three words.

Spelling turned out to be mostly solved: only one model, Gemini 2.5 Flash Image, misspelled labels. The faults were obedience and format. Most images added text nobody asked for: invented headings, "Source: internal analytics", page footers, a hex colour code from the prompt, "(16pt)" from a layout hint. GPT-5 Image and GPT-5 Image Mini ignore the requested aspect ratio and always return a 1024 square. The auto-router served Gemini 3 Pro Image, at its price. Three were cut.

## Round 2: numbers, a document, a whole article

The chart had fourteen exact values. Five of six models drew every bar right, sorted and in proportion, with both highlight colours where asked:

Fourteen exact numbers. Five models got every value and proportion right; GPT-5 Image wrote "artitty" for artefact, three wrong values, three missing bars and a claim bar a third too short.

Then two briefs that start from text: the Explainer's 240-word two-minute version of the article as "here is a document, create an infographic about it", and the whole article. This is where the pattern I have seen with ChatGPT showed up, but only in the newest model: **GPT-5.4 Image 2 scored 9 on both**, and on the whole article it was the only model with every number right and the whole argument told. Give it the document, not a description of the picture. The older GPT-5 Image got worse with more text. The Google models summarised well but tended to drop the article's caveats ("re-anchoring does not enforce anything") and to invent plausible sample values.

The diagram brief ran again, unchanged, to measure noise: scores moved by up to two points between identical runs. One image per cell separates tiers, not neighbours.

## Round 3: can you direct it?

Three briefs that test obedience. The hardest was an edit: send the model its own round 1 diagram and ask for three changes and nothing else.

The edit. GPT-5.4 Image 2 added a sixth box and kept the other five. Gemini 3 Pro changed the title and the colour, and made room for the new box by replacing the last one: "canary report" is gone.

Only GPT-5.4 Image 2 made all three changes without breaking anything (9). Every Google model treated the edit as a redraw, and something else moved: a box deleted, a label orphaned, a label overwritten. On the UI component (seven rows of exact text) and the brand slide, GPT-5.4 Image 2 again won both samples. Nano Banana 2.1, the best value of the first two rounds, had no usable image in this round: the briefs where every character is specified are the ones it loosens.

## Round 4: three slides that belong together

Each model drew three slides of the same deck, each a separate call. The cheapest set was the best, Nano Banana 2.1's at 8, but no model carried the cover's top bar or footer to the other slides: nothing in a separate call knows what the last slide looked like.

So we tested the obvious fix straight away: send slide 1 with every later slide and ask for the same style. Judged blind in pairs, without knowing which set used the reference, **every model's referenced set was the more consistent one**: from 1 or 2 out of 5 to 4 or 5.

Nano Banana 2.1, slides 2 and 3 without and with slide 1 attached as a style reference. The top bar, the kicker and the headline type carry through.

## Round 5: the conclusion, drawn by the models it recommends

The final three were given the conclusion as a 263-word document, written with the prompt rules the bake-off had produced. All six images got every tier, price and speed right; no LinkedIn logos, no leaked codes, no invented prices. GPT-5.4 Image 2 scored 9 and 9 and told the whole conclusion: it is the image at the top of this article.

## What it cost

Quality against price for every model. The three recommended sit on the frontier; Gemini 3.1 Flash is beaten by Nano Banana 2.1 on both axes; GPT-5 Image is the most expensive and the worst.

| Model | Price per image | Cost per usable image | Median seconds | Mean score |
|---|---|---|---|---|
| Nano Banana 2.1 | $0.039 | $0.066 | 9 | 6.4 |
| Gemini 3 Pro Image | $0.140 | $0.238 | 20 | 6.6 |
| GPT-5.4 Image 2 | $0.176 | $0.230 | 83 | 8.0 |

Three things from the Accountant:

- **Half the money bought images nobody would use** ($4.43 of the first $8.80). Price per image flatters a model that fails often; cost per usable image does not.
- **Gemini 3 Pro is not cheaper than GPT-5.4 Image 2 per usable image.** It is four times faster. That is its case, and the guidance uses it only where waiting a minute and a half matters.
- **A newsroom month.** One article a day with a nine-slide deck, a hero and two figures is twelve images. All on GPT-5.4 Image 2, with its redo rate, about $85 a month; all on Nano Banana 2.1 about $23; the recommended mix (deck on Nano Banana, hero on Gemini 3 Pro, two document figures on GPT-5.4 Image 2) about **$40**. A cost per article of about $1.34 is one I am happy to pay, and to show.

## The guidance

The deliverable is a page any agent can follow, in the vault as `analysis/guidance.md`. The short version:

| Job | Use | Avoid |
|---|---|---|
| Concept slide, data chart | Nano Banana 2.1 | the 1024-square models |
| Labelled diagram, stat card | Gemini 3 Pro Image | Nano Banana for exact labels |
| A deck | Nano Banana 2.1, with slide 1 attached to every later slide | separate calls with no reference |
| Document or whole article to infographic | GPT-5.4 Image 2, given the document | GPT-5 Image |
| Edit an image, UI component, brand slide | GPT-5.4 Image 2 | every Google model for edits |
| In a hurry | Gemini 3 Pro Image | GPT-5.4 Image 2 (83 seconds) |

And the prompt rules the faults taught, which made round 5 clean:

1. **Never name the platform.** "Suitable for LinkedIn" put LinkedIn logos on the image. Say "portrait 4:5".
2. **End with "No other text."** Unrequested headings, sources and footers were the commonest fault.
3. **Say "no numbers other than those given".** Every model invented plausible values somewhere.
4. **Keep hex codes, type sizes and separators out of text to be drawn.** They get drawn.
5. **For an edit, say what must not change.**
6. **For a deck, attach slide 1 to every later slide.**
7. **Check every image.** OCR and the judge agreed on 76% of images: OCR is a cheap alarm, not a judge.

## What this does not show

- **Small samples.** Most cells hold one or two images, and identical runs moved by up to two points. The tiers hold across rounds; a one-point gap between two models does not mean much.
- **One judge, one rubric.** The Designer is an agent with a written rubric, judging blind. A person would weigh craft differently; the fact checks would not change.
- **One day.** Prices, models and their behaviour are OpenRouter's on 10 October 2026. The bake-off is built to be run again: the runner, the scorer and the briefs are in the vault.
- **Only what OpenRouter offers.** Other image models exist outside it; this is the set one key could reach.

## What comes next

The guidance becomes the Storyteller's: the [Five readers](one-article-five-readers.md) decks, drawn so far by code, get an image pass on Nano Banana 2.1 with slide 1 as the reference, and a document figure on GPT-5.4 Image 2, with the cost of each logged against the article. And the bake-off runs again whenever a new model appears, because the answer to "which model" has a date on it.

*Written by agent@riskmandate.ai (Claude Opus 5.5, claude-opus-5-5) in the sgit.ai site session on 10 October 2026, from a voice memo by Dinis Cruz, who has editorial responsibility and paid for the run. Every image was generated through OpenRouter and judged blind by Claude agents under the role files in the vault; every cost is OpenRouter's recorded usage. AI-generated, disclosed as Article 50 of the EU AI Act asks.*

## Threads

Site & engineeringNews & evidence[This article as a graph →](graphs.md#the-infographic-bake-off)

### Builds on

- [Re-anchoring: keeping an agent's rules alive through every summary, and a canary that shows when they are not](re-anchoring-agent-behaviour-policies.md) Summaries keep under 2% of a long session. Re-anchoring prints the agent's rules back after each one; a canary report shows it is working.
- [One article, five readers: a librarian, a cartographer, a historian, an explainer and a storyteller read the same piece](one-article-five-readers.md) Write the article first, then send five agent readers through it: a catalogue, an ontology and maps, the arc, two minutes, and a deck.

[All articles](index.md) · [All graphs](graphs.md)

**Posting this article on LinkedIn?** The cover is [the-infographic-bake-off.jpg](banners/the-infographic-bake-off.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://newsroom.sgit.ai/articles/the-infographic-bake-off.html)*
