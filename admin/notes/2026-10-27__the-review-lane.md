# The review lane: independent reviewers on a schedule (card 091)

**27 October 2026.** The editor asked for ChatGPT and Perplexity to review the site on their own schedules, as fact
checkers and editors, with a page that says what to review next, an exact description of what to do and how to
answer, an append lane to send through (a vault of its own, shared by QR code), and a scheduled run on our side that
drains the lane and proposes what to change, which the editor reviews; later, perhaps, automated. ChatGPT's first answer, on
*The evidence behind four days*, is on the record as `admin/content/articles/reviews/the-evidence-behind-four-days/2026-10-27__openai-chatgpt.json`
(changes needed, nine findings), and shaped criteria v1.2.

## The loop

```
 queue.json (the editor's order)
      │  review_queue.py, at every release
      ▼
 reviews/queue/<id>.md ──► ChatGPT / Perplexity, scheduled, running brief.md
                                   │ the answer: one record per article, in json blocks
                                   ▼
 reviews/send.html#rv1… ◄── the editor (or a reviewer with a browser) pastes the answer
      │ checks each record (record.js), seals to the lane's key, appends
      ▼
 the review lane (vault jk20axc2 on dev.send.sgraph.ai, key sha256:61c7748dad522984)
      │ our scheduled run: review_lane.mjs drain, commit, push, mark
      ▼
 admin/content/articles/reviews/<slug>/<date>__<reviewer>.json ──► the editor decides; the newsroom fixes and answers
```

- **The queue** (`admin/content/reviews/queue.json`, built by `admin/build/review_queue.py` into `reviews/queue/`):
  the editor's priority first, every one to every reviewer; then each reviewer's own findings to recheck where the
  text changed; then the backlog, newest first, dealt between the reviewers in turn. One dated batch a day for a week,
  rebuilt at every release. `batch` per reviewer is 1 for now; 2 to 4 once the answers are good.
- **The brief** (`admin/content/reviews/brief.md`, published as `reviews/queue/brief.md`) is the scheduled task's
  prompt, word for word. It carries ChatGPT's own lessons: forecast against observation, the separate dates, like
  for like counts, exact figures, bounded absences, the strongest counterevidence.
- **The criteria** are v1.2: each finding has `verification`, `source_passage` and `method`; each record lists
  `verified` and `not_checked`.
- **The send page** (`reviews/send.html`, `assets/reviews/send.js`) takes a whole answer, finds the records, checks
  each against the criteria, the site's `status.json` and the article's text (quotes, a repeat review, a high finding
  with approve), and sends only the good ones, sealed in the browser. The link carries the vault id, the append token
  and the public key: anyone with it can add, nobody can read. It is given to reviewers, never published.
- **The lane** was made by `admin/build/review_lane.mjs create`: a vault of its own, an append lane, an RSA key
  pair. The public half is `admin/content/reviews/lane.json`. The secret (the private key, the enum key, the vault
  key) was never printed or committed: it was sealed to the editor's key in pki.sgit.ai's register
  (`sha256:db7f79fdd87e030a`) as a pki.sgit.ai message link, with pki.sgit.ai's own message code
  (`admin/build/pki-message/`, vendored).
- **Why a paste, not a POST.** A scheduled ChatGPT or Perplexity task can read pages and cannot send a request; so
  it answers in its chat, and whoever reads the answer pastes it. A reviewer that can drive a browser opens the
  link itself.

## What the editor does, once

1. Open the sealed link on pki.sgit.ai with the editor's key; copy the secret into the cloud environment's variables as
   `REVIEW_LANE_SECRET`.
2. Give each scheduled reviewer the brief (with its id filled in) and keep the send link and its QR code at hand
   to paste their answers.

## Our scheduled run (daily)

The prompt for the scheduled task, a fresh session each time, in this repository:

> You are the newsroom's review desk. Fetch `dev` and branch from it. Run
> `node admin/build/review_lane.mjs drain --taken /tmp/review-lane-taken.json` (REVIEW_LANE_SECRET is in the
> environment). If nothing arrived, stop and say so in one line. Otherwise: run `python3 admin/build/reviews.py --check`;
> commit the new records and any new reviewer as `reviews: <n> from the review lane (<date>)` and push the branch;
> then run `node admin/build/review_lane.mjs mark --taken /tmp/review-lane-taken.json`. Then, for each new record, read
> the article and each finding, and write for the editor: the finding, whether you agree (with the source you
> checked), and the smallest fix you propose, as a diff of the article's markdown. Change no article. End with the
> branch and the list of proposed fixes, highest severity first, for the editor to approve.

Once the editor has approved fixes this way for a while, the same run can apply the ones marked as routine (a
rounding, a quote, a dead link), release them, and answer the findings in `<slug>/status.json` as `fixed`, leaving
the rest to the editor.
