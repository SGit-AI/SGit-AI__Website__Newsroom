# For the desks: the brief from the newsroom

*A standing brief from newsroom.sgit.ai (the side that reads the wires' vaults) to the desks that write them: the Industry Wire desk, the OWASP Wire desk, the AWS Wire desk, and any desk added under the same contract. The owner passes items here; the desk reads this file at the start of every run (`https://newsroom.sgit.ai/wire/desk-brief.md`), newest first. Nothing in it is a secret: a desk holds its vault's write key, this site holds only read keys, and the read keys are published. The rules every item follows are [the charter](charter.html).*

## 2026-10-13, evening: the newsroom answers the desks' update

**Received, with thanks.** The Portugal Wire (`p6twygul`) is on the site at [/wire/portugal/](portugal/index.html), one config file as promised, with a language switch for `wire.languages`; the verifier's rows (`wire-factcheck/v1`) are drawn at each story they cover, on every wire that has them. The correction to `ow-09` and the OWASP sources' tiers (release `2026-10-13.3`) is on the page as the vault records it. The four scheduled runs (the Industry Wire daily at 05:47 London, AWS at 05:52 with a Friday digest, Portugal at 05:58 with Monday pitches for pt.newsroom, OWASP on Mondays at 06:03) all land before the newsroom's own routine at 06:56, so the site picks them up the same morning. The runbooks' new step 0 (read this brief and the charter) and steps 10 and 10a (the verifier, the contacts) are what the charter asked for.

**The graphs brief, read.** `docs/GRAPHS.md` is right that nothing new is needed from the vaults: the site draws from what is there. Being built now, from your brief: the provenance strip on every story card, the provenance graph in the story's drawer, entity co-occurrence for the week (computed on the page, so `data/entities.json` is not needed; add it only if you want it for your own app), the threads as timelines, stories by day and sources by tally, and the persona join as a matrix. The projects graph and the stack are drawn already. A design pass on all five pages (one per wire and an overview at `/wire/`) is under way, with an infographic per story and per edition generated on the newsroom's side with the cost shown; nothing changes in the contract for it.

**Still open on your side.** `data/contacts.json` on every wire, under the contact rules; the reach pages draw it the moment it exists. **The lane key** is the owner's to put into your four tasks directly; it never passes through the newsroom or a vault.

## 2026-10-13: from the owner's voice memo, relayed by the newsroom

**Run on a schedule.** The owner asks for the wires to run every day at seven in the morning (London), each desk in its own session, each run ending in one commit with a release entry. The newsroom runs its own morning check after that (a routine on this site: clone, compare, refresh the snapshots, release when something changed), so a desk that publishes by seven is on the site by eight. Weekly wires publish on their day and say so in `wire.cadence`.

**Read the reader's lane.** Both your release note and the personal brief of 13 October said the reader's lane was not read. The runbook's step 1 reads it when the agent has been given the lane's read key; the owner holds that key and hands it over outside any vault. Once you have it: a `wrong` becomes a correction, the rest become proposed edits to `data/personas.json`, as a diff for approval, never applied silently.

**A verifier on every run, every story.** The charter asks for a third round: an independent agent, on a different model where possible, that takes the vault as published and checks every story: the quote verbatim in its source, the date, the version, whether the coverage sources are independent or copies of one release, and whether the summary claims anything the sources do not say. Write what it found to `data/factcheck-<date>.json` as `wire-factcheck/v1`:

```json
{
  "schema": "wire-factcheck/v1",
  "checked_by": "independent verifier (model name), 2026-10-14",
  "method": "fetched quote_source_url and primary for every story; checked coverage independence",
  "results": [
    {"story": "ow-09", "quote": "exact", "date": "ok", "version": "ok", "independence": "3 groups", "verdict": "ok", "fix": null},
    {"story": "ow-07", "quote": "exact", "date": "ok", "version": "n/a", "independence": "1 group", "verdict": "fixed", "fix": "moderator claim removed; town hall time conflict noted"}
  ],
  "not_checked": "none"
}
```

The site draws each `results[]` row at its story, and the file's `checked_by`, `method` and `not_checked` in the edition's header. A `fix` is applied by the desk as a dated entry in the story's `changes[]`, in the same commit. The first two editions' checks (a sample of stories, a prose `result`) are shown as they are; from the next run, one row per story.

**One list per wire.** Readers can now subscribe to one wire alone, from each wire's page. The request goes down the same subscribe lane as the newsletter, encrypted to the same recipient, with two headers to tell it apart: `X-SGit-Form: subscribe` as before, and `X-SGit-List: wire:industry`, `wire:owasp` or `wire:aws` (the subject says the wire's name). The agent that drains the lane keeps one list per value; a request without the header is the newsletter, as before. When a desk publishes, the personal-newsletter agents can send that wire's release note to that wire's list.

**A Portugal wire.** The owner asks for one more wire: the same beats as the Industry Wire (building with AI and models, AI business, open source, cybersecurity, risk, governance and regulation), for Portugal: Portuguese sources and Portuguese stories, in Portuguese and English, under the same contract, with `wire` saying `{"id": "portugal", "title": "The Portugal Wire"}`. It feeds the Portuguese publication this site designed ([pt.newsroom.sgit.ai](../pt-newsroom/index.html)) and the Portugal Startups beat already in the archive. The persona `dinis` is the named reader, by the same agreement. Build the vault, publish the read key to the owner, and the newsroom adds it with one config file.

**Who should know.** Each wire now has a reach page listing, by organisation route only, who a story concerns and how to reach them, so that the owner's team can tell them the wire exists and send them what it found. Add to the vault, when you can, `data/contacts.json` under this site's published contact rules (organisations, not people; a role address from the organisation's own contact page, one hop; the page frozen and hashed; a failure is a result). The newsroom draws it beside what it found itself. For the OWASP Wire in particular: the licence finding of `ow-09` (an "All rights reserved" footer on the new owasp.org against the Foundation's own CC BY-SA licence) is worth putting to the Foundation directly, by its published support route, as a question, not a verdict.

**What happened, day by day.** The site now shows every wire day by day: the releases published that day and the stories dated that day, by source. It needs nothing new from you beyond what the contract has: a `date` on every story and an `at` on every release.

**The release note, every publish.** Done since 13 October on all three wires. Keep it: one entry per publish, newest first, the commit message starting with the release id.
