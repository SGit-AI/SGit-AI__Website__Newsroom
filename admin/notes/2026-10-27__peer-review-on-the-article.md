# Peer review on the article: who has read it, which text, and what they said

Status: a design note by newsroom.writer, 27 October 2026, at the editor's request. Built in v0.13.105 for every
article; the case study is two articles, "The evidence behind four days" and "Meta's new terms and the news".
It builds on the review records and criteria (`admin/content/reviews/`) and the review lane (v0.13.103, newsroom.dev).

## The idea

An article's credibility should be visible as a record of review, not as a claim: who has taken a fresh look at it,
agents and people, on which text, what they said, and what the newsroom did about it. Agreement and disagreement are
both on the record. Counts, not a score.

## The rules

1. **A review is of one text.** It carries the article's text hash. When the article changes, earlier reviews stay on
   the record, marked "an earlier text", and the new text waits for a fresh look. So a correction never silently
   inherits the approval of the text it replaced.
2. **Agents and people are counted apart.** An agent review is a fresh look by a model from a named vendor; a person's
   review is signed by the person: the editor (Dinis Cruz is a registered reviewer, kind `editor`), a journalist on
   the desk, or a reader who signs what they write.
3. **Disagreement is a verdict.** `changes-needed` from anyone puts the article in "Disputed" until it is answered.
   `comment` is a note on the record without a verdict (an expert's view, the editor's later note).
4. **Every finding is answered**: fixed (with the site release and the article version that carries the fix),
   declined (with the reason), or open.
5. **Credit where the change came from.** A version of the article that fixes a review's findings says so on its
   diff page ("Prompted by review") and in the versions table, linking the review and the answers.

## What a reader sees

- **Under the byline**, one line: the article's standing, and the counts behind it.
  - Not reviewed yet
  - N findings open, or Disputed (someone asked for changes)
  - Corrected after review; this text not yet re-read
  - Checked by N agents; no person yet
  - Checked by people / Checked by agents and people
- **At the foot**, "Reviews": the standing in a sentence, then People and Agents, each review with its verdict, its
  date, its text (this one or an earlier one, and which article version answered it), its summary, its findings'
  status and the record.
- **On the version pages**: which review prompted which version.

## How a person reviews

- **The editor**: say it to the newsroom ("I have read the four days article: approve", or what is wrong); the
  newsroom files the record as kind `editor`, verdict as said, `run_by` naming the conversation. Later, the review
  lane's send page with a short form for people.
- **Anyone else**: through the review lane's send link from the editor, or a pull request. A person is named only
  with their consent; a public comment (on LinkedIn, say) can be recorded as a `comment` quoting the public text,
  with the link, never a private message.

## Not built yet

- A form for people on the send page (today it takes the JSON record).
- Rechecks of fixed findings by the reviewer who raised them (the queue lists them; nothing shows "the fix holds"
  separately from a fresh review yet).
- Weighting: two agents from the same vendor are two looks, not two independent ones. The line names the reviewers,
  so a reader can see it; nothing discounts it.
