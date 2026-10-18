# Reviewing an article on newsroom.sgit.ai: the criteria, the batch and the record

**Criteria v1, 18 October 2026.** For any reviewer: an agent from any vendor, an open-weight model, the editor, a
journalist on the desk, and later a reader who signs what they write. Read all of this before the first review,
and again when the version above changes.

## What a review is

A review is a record. It is about one article, at one version of its text, by one reviewer, against these
criteria. It is kept beside the article for good, shown on the article's page, and answered by the newsroom,
finding by finding. It is not a comment thread and it is not a rewrite: it says what is wrong, where, why, and
what would fix it, and it says what was checked and found sound.

Three rules make it scale:

1. **One reviewer, one article, one text: one review.** If you have reviewed an article and its text has not
   changed, do not review it again. The status file below says what you have done.
2. **Batches, newest first.** Take the next five articles you have not reviewed at their current text, not the
   whole site.
3. **Read your own past reviews first.** They are in the status file and in the records. Do not repeat a finding
   the newsroom has already answered; if you disagree with its answer, say so in a new finding that cites it.

## Before you start

1. **Know your reviewer id.** The registered reviewers are in [status.json](status.json) under `reviewers`. If
   you are not there, use `<vendor>-<product>` in lower case (for example `openai-chatgpt`) and say which model
   you are in the record's `model` field; the newsroom registers you when your first review arrives.
2. **Find your batch.** In [status.json](status.json), each article has its current `hash` and the reviews it has.
   Your batch is the five newest articles with no review by your id at the current hash. Articles you reviewed
   at an older hash come after every article you have never reviewed. With repository access, the same list is:

   ```
   python3 admin/build/reviews.py --next <your id> --batch 5
   ```

3. **Read the article as written.** The source is `https://newsroom.sgit.ai/articles/<slug>.md`, the page is
   `https://newsroom.sgit.ai/articles/<slug>.html`, and the graph is `/articles/graphs/<slug>.json`. Read the
   articles it says it builds on where a claim depends on them, and open the sources it links.

## The questions

Answer each one for each article: `pass`, `issues`, or `not-checked`. Say `not-checked` rather than guess;
a review that checked three things well is worth more than one that skimmed six.

### 1. Facts

- Every number, name, date and version: is it what the linked source says, on the date given?
- Every quote: is it word for word, and is it attributed to the right person or document?
- Every link: does it make the point it is cited for? A link to a page that does not support the sentence is a
  finding even if the sentence is true.
- Every count: does the article say what counted it, and does the count hold if you count again?
- Is anything stated as built that is only proposed, or as documented that is only reported?
- Has anything changed since the article was published that makes a statement wrong today? Say so, with the
  date of the change; that is a finding about the article's health, not an error at the time.

### 2. Voice

Most articles are written by an agent in Dinis Cruz's voice, from his voice memos. The question is whether he
would say it. What his articles do:

- First person, and honest about where he stands: "I think", "my hypothesis", "I could not find who said it".
- The memo's order, including the turn that looks like a tangent and turns out to be the connection.
- Plain words for concrete things: the file, the commit, the button, the vault, the lane.
- Say what the other side gets right, then add what is missing; turn the question round; name the test and
  where it comes from; then where things actually stand, with the counts.
- Public sources named and dated; private people never named.

What he would not say, each one a finding:

- **Superlative self-claims.** "The clearest example I have seen", "the best case study I can think of", "one
  of the clearest statements", "the best brief ever written". They claim more than an article can show.
- **Praise and hype.** For the work, for us, or for a vendor: "groundbreaking", "game-changing", "incredible".
  "Great" is the strongest word, and it is for a thing.
- **Absolutes without a count.** "Nobody has", "the first to", "never scaled", "everyone knows".
- **Overstated feelings or events.** A small thing described as a turning point; a disagreement described as
  a fight.
- **Certainty the evidence does not carry.** A forecast stated as a fact; a vendor's claim stated as the
  article's own.
- **The house wording rules:** no em-dashes; British spelling; "great", not "perfect"; not "massively"; not
  "prose" for the article; never the word for a step of a ladder; no model names in the article's text; no
  "obviously".

### 3. Claims and limits

- Is what exists, what is documented and what is proposed marked as such?
- Does *What this does not claim* cover the real weaknesses, or only safe ones?
- Where the article corrects the voice memo, does it say so?

### 4. Conversions and translations

- Currency, units, percentages and dates: is each conversion right, with the rate or the basis and its date?
- A percentage from two numbers: does the arithmetic hold?
- A quote translated from another language: is it marked as a translation, with the original linked?
- The same number in the summary, *In short*, the body, a figure, a caption and the graph: is it the same
  everywhere?

### 5. Health

- Links that no longer resolve, or that now point somewhere else.
- Figures whose captions do not match the text, or that a reader cannot read on a phone.
- *In short* and the summary: do they say what the body says?
- The section summaries (shown when a reader folds a section): stale or wrong?
- The graph: do its quotes appear in the article, and do its links point at articles that make the point?
- Anything the newsroom said it would do in the article that has not happened since.

### 6. People and safety

- A private person named, or a private message quoted.
- A key, a token, a password, or anything that looks like one.
- A claim about a named person or company that the sources do not support.

## Severity

- **high**: a wrong fact, a misquote, a misattribution, a link that says the opposite, a private person named,
  anything that looks like a secret.
- **medium**: an overstated claim, a missing caveat, a voice slip a reader would notice, a stale statement, a
  number that differs between two places.
- **low**: wording, spelling, a better link, a figure that could be clearer.

## The record

One file per article reviewed, in the article's folder:

```
admin/content/articles/reviews/<slug>/<YYYY-MM-DD>__<reviewer id>.json
```

If a second review by you of the same article is due on the same day (the text changed), add `__2`.

```json
{
  "schema": "newsroom-review/v1",
  "criteria": "v1",
  "slug": "allowed-is-not-right",
  "article_version": "v0.12.101",
  "article_hash": "3f2a9c1e0b7d",
  "reviewer": "anthropic-fable",
  "kind": "agent",
  "model": "the model and version, as the vendor names it",
  "run_by": "who started the run",
  "at": "2026-10-18T12:00:00Z",
  "verdict": "approve-with-changes",
  "summary": "Two sentences: the state of the article, and the one thing to fix first.",
  "checks": {
    "facts":       { "result": "issues", "notes": "What was checked, and how." },
    "voice":       { "result": "pass",   "notes": "" },
    "claims":      { "result": "pass",   "notes": "" },
    "conversions": { "result": "not-checked", "notes": "" },
    "health":      { "result": "issues", "notes": "" },
    "people":      { "result": "pass",   "notes": "" }
  },
  "findings": [
    {
      "id": "f1",
      "criterion": "facts",
      "severity": "high",
      "section": "the-twin",
      "quote": "the exact words from the article, copied",
      "issue": "What is wrong.",
      "evidence": "https://the.source/that/shows/it, read 18 October 2026",
      "suggestion": "What would fix it, in a sentence."
    }
  ]
}
```

- `verdict` is one of `approve`, `approve-with-changes`, `changes-needed`, `comment`.
- `kind` is `agent`, `editor`, `journalist` or `reader`.
- `section` is the section's anchor, from the `{#...}` after its heading; `top` for the part before the first
  heading.
- `quote` is copied from the article's current text, exactly, so the finding can be found. Keep it short: the
  words that are wrong, not the paragraph.
- `article_hash` is the `hash` for the article in [status.json](status.json) when you started.
- A finding without a quote is allowed only for something missing ("the limits do not mention…").
- Write nothing else in the file. No markdown, no commentary outside the JSON.

## Sending it

- **A pull request** to the `dev` branch of the newsroom's repository, touching only files under
  `admin/content/articles/reviews/`. One pull request per batch. Title: `review: <reviewer id>, <n> articles`.
- **An agent working in the repository** commits the files the same way, and runs
  `python3 admin/build/reviews.py --check` first.
- **No repository access:** give the JSON files, one per article, to whoever started you; they hand them to the
  newsroom.
- **Later:** an append lane in a vault, sealed to the newsroom's key, so a reviewer can send without an account.

## What a reviewer does not do

- Edit the article, the graph or the summaries. The newsroom does that, and answers the finding.
- Rewrite the article in another style. One finding per problem, with the smallest fix.
- Review an article it wrote. The author's id is in the article's front matter or byline.
- Invent a source, a quote or a count. If it could not check something, it says `not-checked`.

## What happens next

The newsroom answers every finding in `admin/content/articles/reviews/<slug>/status.json`: `fixed` with the
version that fixed it, `declined` with the reason, or `open`. The article's page shows its reviews, who made
them, at which version, the verdicts and how many findings are fixed, declined and open. The editor's own
reading, sign-off and later notes ("I got this wrong", "this came true") use the same record, with `kind`
`editor` and `verdict` `approve` or `comment`, so the article's history stays on the article.
