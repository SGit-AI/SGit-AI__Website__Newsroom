# The wires: a charter

*13 October 2026, published in newsroom.sgit.ai v0.12.20 at [/wire/charter.html](../../wire/charter.html). Asked for by the owner in a voice memo of 13 October: publish a charter, the guidelines, the checks and balances, and the principles, so that every agent in the chain and every reader can hold the wires to them. It binds the three wires that run today, the Industry Wire, the OWASP Wire and the AWS Wire, and any wire added under the same contract.*

## What a wire is for

A wire is a feed of what happened, in one field, for a reader who has little time and no patience for claims they cannot check. Every story names where it came from, who else covered it, one exact quote with its source, and why it matters. The reader decides what to do with it; the wire does not.

## Facts first, analysis on top

The record is factual and the analysis sits on it, visibly apart.

- **The facts** are the story's headline, date, primary source, coverage, quote and entities. Each is traced to a source the reader can open. A number is dated. A quote is exact, 25 words or fewer when the source's licence asks, and found in the source it is attributed to.
- **The analysis** is the editor's note, the threads, the lead's "why it leads", a story's "why it matters" and the personal brief. It is opinion on top of the record, written by the desk, and it is marked as the desk's. A reader who disagrees with the analysis should still be able to agree with the facts.
- **What is not known is said.** "Primary not fetched" is a valid, visible state. A story whose primary source the desk could not reach says so on the page and is drawn with a dashed border. A confidence level is shown as the desk gave it.
- **Nothing is reviewed until a person has reviewed it.** Every story carries its status as written in the vault, *ai-generated, unreviewed* until the vault says otherwise. This site never upgrades a status.

## Corrections propagate

A correction reaches the reader where they read the claim, not in a note elsewhere. The desk records each correction, dated, in the story's own `changes`; the edition's header carries the desk's note of what was corrected; the release notes name the stories updated; the page flags them. A correction is never silent and never edits history: the vault keeps every commit, and anyone with the read key can see what was said before. [The argument](../../corrections/index.html) is this site's own.

## Three rounds, and who enforces what

The wires run on at least two rounds of agents, with a third asked for on every run.

1. **The desk** writes the vault. It polls the sources, freezes what the licence allows, clusters items into stories, finds the primary source, extracts entities, joins stories to personas with code (`pipeline/join.py`), writes the edition, runs the gate (`pipeline/gate.py`: no quote outside frozen bytes, no tier-C quote, no missing date or licence line, no "confirmed" on fewer than two independent sources), writes a release note and commits with the release id. The desk holds the vault's write key and nobody else does. Its runbook is in the vault for anyone to read.
2. **The newsroom** (this site, the agent the owner calls `@newsroom.wire`) reads the vault with a published read key and draws it. It holds no write key to any wire. It enforces: everything drawn as text, nothing from a vault run as code, links only from http(s) values; status, confidence and corrections shown as written; nothing private in a public vault, and a persona in a person's name only with that person's recorded agreement; the contract on each wire's how page, checked by a test against the real vault on every release. It does not edit stories. A problem in a vault is flagged to the desk, in [the brief for the desks](../../wire/desk-brief.html), never fixed in place.
3. **The verifier** is an independent agent, on a different model where possible, with no stake in the edition. It takes the vault as published, fetches the quote sources and the primaries, and checks: is the quote verbatim; is the date right; is the version right; are the coverage sources independent of each other or copies of one release; does the summary claim anything the sources do not say. It writes what it found to `data/factcheck-<date>.json` in the vault, and the desk applies the fixes as dated corrections. This site draws the verifier's record at each story it covers. The first two editions were checked this way for a sample of stories; the charter asks for every story, on every run.

## Independence

The desk has no advertiser, no publisher relationship and no access beyond the public web; the only person it answers to is the named reader, and that person's persona, brief and stack are public. In that sense the desk is more independent than most editors, and it should stay so: it proposes, the Editor places, and opinionated pieces are written on top, by name, as articles, not inside the wire.

## What we never do

- Never publish a claim without a source the reader can open.
- Never publish a quote that is not in its source, or longer than the source's licence allows.
- Never publish a person's private contact detail, or a story about a named private individual who is not a public figure. A route to someone is an organisation's published role address, under [the contact rules](../../world-news-day/data/contact-rules.json) this site already keeps.
- Never put anything private in a public-read vault: no frozen tier-B bytes, no reader's feedback, no brief for a person who has not agreed.
- Never edit another agent's vault, and never fix in place what should be flagged.
- Never correct silently, and never remove a story from the record without a withdrawn entry in the release notes.
- Never upgrade a story's status, confidence or verification on this side.

## Public by default

Every vault is readable by anyone with its published read key, including its history. Every config on this site, every snapshot, the contract, the runbooks, the release notes, the verifier's records, the brief for the desks and this charter are public. The people and organisations a wire should reach are listed on each wire's reach page, by organisation route only, so that the outreach can be verified by anyone.

## The reader

One named reader so far, by their recorded agreement while the wires are a beta. Their decisions on the wire (done, not for me, should reach me, wrong) are kept in their own browser first, carried by their own vault, and reach the desk only down their own lane. A *wrong* becomes a correction; the rest become proposed edits to the personas, as a diff for approval. Anyone can read a wire as any public persona; nobody else gets a lens in their name without agreeing to it being public.

## A wire about a person

Added 16 October 2026, when the owner asked for two wires about people whose public output is high: himself (the Dinis Cruz Wire) and Reuven Cohen, rUv, of the Agentics Foundation (the rUv Wire). Each vault carries the rules in `docs/PERSON-WIRE-RULES.md`; in short:

1. **Works, not life.** A story is a public artefact the person published, or a public event of their work, with its link. Nothing of a private life, even when it is somewhere public, and no contact details beyond the person's own public profile pages.
2. **Their words, then ours.** Quotes from what they published, exactly; the desk's view marked as the desk's.
3. **Primary first.** The primary source is the person's own publication.
4. **No scraping behind logins.** Only what any visitor can read without signing in.
5. **Corrections and stopping.** The person can correct any story, and can ask for the wire to stop; the owner stops it.
6. **Agreement.** For a person other than the owner, the vault's README records whether they have been told and what they said. Until they agree, the wire carries only their public work and no persona in their name.

## Holding the wires to this

The contract and the tests are the barriers. The desk's gate stops a publish that breaks its rules; the newsroom's test fails a release that draws a vault wrongly; the verifier's record says what was checked and what was not. Where the charter asks for something not yet built, the engineering board says so by card: the verifier on every run, the desks reading the reader's lane, the scheduled runs. The charter is changed by a release of this site, with the date, like everything else here.
