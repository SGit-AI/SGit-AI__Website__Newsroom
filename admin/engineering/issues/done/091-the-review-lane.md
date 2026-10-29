---
id: 091
title: Independent reviewers on a schedule: the review queue, the brief, criteria v1.2, and the review lane
kind: story
priority: high
created: 2026-10-27T13:00:00Z
source: Dinis, 27 October 2026, with the prompt he sent to ChatGPT and Perplexity and ChatGPT's first review: "I want to set up an independent review for ChatGPT and Perplexity ... We should have a page for them that we update that contains the articles that we would like review, the next batch of articles ... one by one ... or groups of two or three or four ... map out the priority ... exact description of what we would like them to do, how they would like to provide information, and how they provide the feedback. And we need to then have an append line, so we need to create a new vault that we're going to share with them using QR codes and the append line ... from pki.sgit.ai ... then we need to have a scheduling process on our side that will basically process the append lane and then see what changes could be made. And then for now, I'll review it, but then we might even be able to automate that process."
release: v0.13.103
estimated_effort: large
---
# Independent reviewers on a schedule: the review queue, the brief, criteria v1.2, and the review lane

## What is asked
1. A page, kept up to date, with what each scheduled reviewer (ChatGPT, Perplexity) reviews next, in priority order, one article at a time and later two to four.
2. An exact description of what they do, how they answer and how the answer reaches the newsroom.
3. An append lane on a vault of its own, shared with them by link and QR code, its secret handed over with pki.sgit.ai.
4. A scheduled run on the newsroom's side that drains the lane and proposes changes for the editor to approve; later, perhaps, automated.
5. ChatGPT's first review, of *The evidence behind four days*, taken in.

## Scenario
```gherkin
Given the editor's priority list and the reviews on the record
When the site is released
Then each scheduled reviewer has a queue of dated batches, with each article's text hash and why it was chosen

Given a scheduled reviewer's answer, with its records in json blocks among its words
When it is pasted into the send page opened on the lane's link
Then each record is checked against the criteria, the site's status and the article's text
And a repeat of a review on the record is refused with the reason
And the good records are sealed to the lane's key in the browser and appended

Given messages in the lane
When the scheduled run drains it
Then each new record is written beside its article, checked again, committed and pushed
And only then are the messages marked processed
```

## Outcome
Shipped in v0.13.103. The queue: `admin/content/reviews/queue.json` (the editor's order), `admin/build/review_queue.py` into `reviews/queue/` (a page, and `<id>.md` and `.json` per reviewer: a week of dated batches; the editor's priority to every reviewer, then rechecks where the text changed, then the backlog dealt between them). The brief: `admin/content/reviews/brief.md`, published as `reviews/queue/brief.md`, the scheduled task's prompt. Criteria v1.2: `verification`, `source_passage` and `method` on a finding, `verified` and `not_checked` on a record. The send page: `reviews/send.html`, `assets/reviews/send.js` and `record.js` (shared with the drain). The lane: `admin/build/review_lane.mjs` (`create`, `drain`, `mark`), made on the vault server as vault jk20axc2, key sha256:61c7748dad522984, public half in `admin/content/reviews/lane.json`; the secret sealed to Dinis's pki.sgit.ai key with pki.sgit.ai's message code (`admin/build/pki-message/`, vendored). Perplexity registered. ChatGPT's review on the record (changes needed, nine findings, open). Test: `admin/build/test_review_lane.mjs` (33 checks, against the mock). Design and the scheduled run's prompt: `admin/notes/2026-10-27__the-review-lane.md`. Left: the secret into the environment as `REVIEW_LANE_SECRET`, then the daily scheduled run; the newsroom's answers to ChatGPT's nine findings.
