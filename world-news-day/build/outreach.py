#!/usr/bin/env python3
"""world-news-day/ — the outreach vault, generated.

    python3 world-news-day/build/outreach.py        (build.py runs it)

Writes world-news-day/outreach/, which is the CONTENT of a second vault: the one handed to
the agent at riskmandate.ai to collaborate in. It is generated rather than hand-kept so that
what the other agent receives is derived from the same frozen bytes as everything else, and
so that anyone can rebuild it and diff.

WHY A SECOND VAULT AND NOT A FOLDER IN THE FIRST. The corpus vault is a record of what
somebody else published: twenty-one op-eds, frozen, described, and finished. This one is a
record of what WE do about it — who was written to, when, what was said, what came back. Two
different kinds of claim with two different failure modes, and mixing them would mean the
evidence and the outreach share a history, a hash chain and an audience. They do not:

  · the corpus vault is complete on the day it is made and should not move again except on a
    new capture;
  · this one is append-only and will move every time a message is sent or answered;
  · the corpus vault can be handed to anyone, including the people it describes. This one
    holds who we are contacting and what we plan to say, which is ours until it is sent.

Provenance is the point. Every action the other agent records here has to name what it acted
on, by hash, in a vault it can verify independently.
"""
import json
from pathlib import Path

SEC = Path(__file__).resolve().parents[1]
DATA = SEC / "data"
OUT = SEC / "outreach"
HOST = "https://newsroom.sgit.ai/world-news-day"


def load(n):
    return json.loads((DATA / n).read_text(encoding="utf-8"))


ACTION_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "An action taken in this outreach",
    "description": "One append-only record per action. Write a new file; never edit an old "
                   "one. The file name is <utc-timestamp>__<target>__<verb>.json.",
    "type": "object",
    "required": ["id", "at", "actor", "verb", "target", "stands_on", "summary"],
    "additionalProperties": False,
    "properties": {
        "id": {"type": "string", "description": "Stable id, unique in this vault."},
        "at": {"type": "string", "description": "UTC, RFC3339. When it happened, not when it was written up."},
        "actor": {"type": "string", "description": "Who acted: an agent name, or a person's role. Be specific: 'riskmandate.ai outreach agent' or 'editor'."},
        "verb": {"enum": ["drafted", "sent", "delivered", "bounced", "opened", "replied",
                           "declined", "agreed", "published", "corrected", "withdrew",
                           "no_response", "escalated", "noted"],
                  "description": "A closed list on purpose. If none of these fits, the action "
                                 "is 'noted' with the summary saying what happened. Do not "
                                 "invent a verb; propose one in a noted action instead."},
        "target": {"type": "string", "description": "An organisation slug from targets/, or 'all'."},
        "channel": {"enum": ["email", "linkedin", "contact-form", "web", "phone", "in-person", "other"]},
        "to": {"type": "string", "description": "The ROLE address or public profile written to. Never a personal email address of a natural person."},
        "stands_on": {"type": "array", "items": {"type": "string"},
                       "description": "What this action rests on: a SHA-256 from the corpus "
                                      "vault's MANIFEST.json, a URL on newsroom.sgit.ai, or "
                                      "the id of an earlier action here. An action that "
                                      "stands on nothing is an assertion."},
        "summary": {"type": "string", "maxLength": 1200,
                     "description": "What was done, in a sentence or two. Not a transcript."},
        "body_ref": {"type": "string", "description": "Path in this vault to the full text sent or received, if any."},
        "outcome": {"type": "string"},
        "next": {"type": "string", "description": "What this action makes due, and by when."},
        "uncertain": {"type": "string", "description": "Anything you are not sure of. Fill this rather than rounding it off."},
    },
}


def readme(contacts, licences, corpus, vault):
    c = contacts["counts"]
    return f"""# World News Day 2026 — the outreach vault

**For the agent at riskmandate.ai, and whoever is working with it.**

This is the working vault for reaching the {c['authors']} authors and {c['organisations'] - 1}
organisations behind the twenty-one World News Day op-eds. It is a *separate* vault from the
corpus vault on purpose: that one is a finished record of what somebody else published, this
one is an append-only record of what we do about it. Different claims, different failure
modes, different audiences.

## What has already been established

Everything below is published at {HOST}/ and derived from bytes that are frozen and hashed in
the corpus vault. You do not have to take any of it on trust, and you should not.

- **{corpus['count']} op-eds**, all granting permission to republish, **none under a named
  licence**. {licences['counts']['with_ld_json']} of {corpus['count']} already ship schema.org
  JSON-LD; **{licences['counts']['whose_ld_json_declares_a_licence']}** populate its `license`
  field.
- **The terms are stated three different ways** — twice on the articles, once on the
  announcement, and they do not agree.
- **None of the {corpus['count']} pages offers any way to reach its author or its publisher.**
  That is why this vault exists as a separate piece of work rather than a mail merge.
- What routes we could establish are in `targets/`, found under rules published *before* the
  looking started ({HOST}/contacts.html). **{c['role_addresses_published']} role addresses**
  out of {c['role_addresses_published'] + c['addresses_found_and_dropped']} seen; everything
  else was dropped.

## The rules of this vault

Read `protocol.md` before writing anything. The three that matter most:

1. **No personal contact detail for any natural person, ever** — not in a target file, not in
   an action, not in a draft. Route through the organisation. This is not a style preference;
   the newsroom's build fails on it.
2. **Every action names what it stands on.** A hash from the corpus vault, a URL, or an
   earlier action id. An action that stands on nothing is an assertion, and this vault exists
   precisely so that outreach is not a pile of assertions.
3. **Append; never edit.** A wrong action is corrected by a new action that says so. The
   history is the product.

## Layout

```
README.md          this file
protocol.md        the rules of engagement, in full — read before writing
brief.md           what we are asking for, and what we are not
targets/           one file per organisation: who, what route, what state
actions/           append-only. One file per action. _schema.json is the contract
drafts/            message drafts, per target. Nothing here has been sent
state.json         the run: counts by state, what is due
evidence.md        how to verify any claim in here against the corpus vault
```

## Getting the evidence

The corpus vault is a separate, read-only vault. Its **public read key** and the SHA-256 of
the downloadable bundle are in `evidence.md`. Verify before you cite: every number in every
draft in here should trace to a file in that vault or to a URL on {HOST}/.

Bundle: `{HOST}/vault.zip` — {vault['count']} files, SHA-256 `{vault['sha256']}`.
"""


PROTOCOL = """# Protocol

The rules of engagement for this outreach. They are short, they are strict, and they exist
because the thing being demonstrated *is* the method: we are writing to twenty-one senior
journalists to argue that claims should carry their provenance. An outreach that cannot show
its own working would be an argument against itself.

## 1. People

- **Never publish, store or send a personal contact detail of any natural person.** No private
  email address, no direct line, no home address. Route through an organisation's published
  role address or its contact form.
- A public professional profile (an organisation's LinkedIn page, an author's public profile
  page) is a *link*, not a contact detail, and may be recorded. Treat it as a route, not as a
  licence to message anyone about anything.
- If someone asks not to be contacted again, that is a `declined` action and it is final.
  Record it and stop. No follow-up, no second channel, no "one last thing".
- Several of these journalists work under conditions where being easy to find is dangerous.
  Behave accordingly.

## 2. Claims

- **Every action names what it stands on.** A SHA-256 from the corpus vault's `MANIFEST.json`,
  a URL under newsroom.sgit.ai, or the id of an earlier action in this vault.
- **Do not restate a number from memory.** Copy it from the data files, or leave it out. If a
  number in a draft cannot be traced, the draft does not go out.
- **Do not characterise anybody.** The corpus analysis reports shared vocabulary; it does not
  report agreement, stance or quality. `agrees_with` is a banned verb in the graph and it is a
  banned claim here too.
- **Never say the pieces cannot be republished.** The permission is real and generous. The
  finding is about its *form*.

## 3. Messages

- Say what is good about their work first, and mean it. Twenty thousand words were given away.
- Lead with the finding that is useful to *them*, not the one that is most interesting to us.
- One ask per message, and make it small: name the licence, put it in the JSON-LD you already
  ship, say it once.
- Offer the evidence, do not attach the argument. A link to the vault and the piece is enough.
- Invite correction explicitly, and mean that too — see rule 5.

## 4. Records

- **Append; never edit.** One file per action, named `<utc>__<target>__<verb>.json`, matching
  `actions/_schema.json`.
- A wrong action is corrected by a new action (`corrected`) that names the id of the one it
  corrects and says what was wrong. The original stays.
- Record `no_response` explicitly once a reasonable window has passed. Silence is data; an
  empty file is not.
- Fill `uncertain` rather than rounding a doubt away. An agent that never records uncertainty
  is not being careful, it is being confident.

## 5. Corrections

If anyone tells us something published about them or their organisation is wrong:

1. Record it as a `corrected` action naming what they said and what we had claimed.
2. Fix the underlying data in the newsroom repository, not just the message.
3. Record the correction publicly, with the version number that carried the error.
4. Reply saying it has been fixed and where.

The newsroom section already carries one such correction, about the publisher of this very
corpus. That is the standard; nothing in here gets to fall below it.

## 6. Limits of this agent

- You may draft, send through published routes, and record.
- You may **not** make commitments on behalf of the newsroom, agree to embargoes, offer
  exclusivity, or accept or offer payment.
- You may **not** publish anything to newsroom.sgit.ai. Propose it as a `noted` action.
- If a reply raises something outside this protocol, `escalate` and stop on that thread.
"""


BRIEF = """# The brief

## What we are asking for

Three things, all small, all on the publisher's side rather than the author's:

1. **Name the licence.** "Free to republish or translate in full, faithful to the original
   meaning" is close to CC BY-ND 4.0 with a translation permission; "with appropriate credit"
   is CC BY 4.0. Either is a URL, a version and a decade of settled practice, instead of a
   sentence each republisher has to interpret alone.
2. **Put it in the JSON-LD that is already being generated.** One `license` line in a record
   every one of the pages already ships.
3. **Say it once.** One canonical statement of the terms, linked from every piece and from the
   announcement — instead of two wordings on the articles and a third on the page that points
   at them. And put a contact route on it.

## What we are not asking for

- Not a link to us, not coverage, not a partnership, not a meeting.
- Not agreement with our analysis. Several of them will think the evidence count is unfair to
  the op-ed form, and that is a conversation worth having in public.
- Not a correction of their piece. Nothing in this work says anybody's argument is wrong.

## What we are offering

- The whole corpus, described, hashed, graphed and downloadable, under CC BY 4.0 — to them
  first, free, with no conditions.
- The finding itself, which is useful whether or not they ever reply: their own structured
  data is one line away from carrying their terms.
- An open repository and a public correction record, so that anything wrong about them can be
  fixed and the fix is visible.

## The tone

They are colleagues who did a generous thing. We are a small publication with a strong
opinion about infrastructure and an argument we are trying to demonstrate rather than assert.
Nothing in a message should read as a gotcha, a pitch, or a lecture. If a draft would be
embarrassing to receive, it is wrong.
"""


def main():
    contacts = load("contacts.json")
    licences = load("licences.json")
    corpus = load("corpus.json")
    vault = load("vault.json")
    aff = load("affiliations.json")

    OUT.mkdir(exist_ok=True)
    (OUT / "targets").mkdir(exist_ok=True)
    (OUT / "actions").mkdir(exist_ok=True)
    (OUT / "drafts").mkdir(exist_ok=True)

    (OUT / "README.md").write_text(readme(contacts, licences, corpus, vault), encoding="utf-8")
    (OUT / "protocol.md").write_text(PROTOCOL, encoding="utf-8")
    (OUT / "brief.md").write_text(BRIEF, encoding="utf-8")
    (OUT / "actions" / "_schema.json").write_text(
        json.dumps(ACTION_SCHEMA, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (OUT / "actions" / "README.md").write_text(
        "# Actions\n\nOne file per action, append-only, matching `_schema.json`. Name them\n"
        "`<utc-timestamp>__<target-slug>__<verb>.json`. Never edit a file in here; correct it\n"
        "with a new `corrected` action that names the id of the one it corrects.\n\n"
        "This directory is deliberately empty at handover. Nothing has been sent.\n",
        encoding="utf-8")

    roles = {r["author"]: r for r in aff["people"]}
    states = {}
    for o in contacts["organisations"]:
        route = ("role address" if o["addresses"]
                 else "contact page" if o.get("contact_page")
                 else "none established")
        state = "ready" if o["addresses"] else ("route only" if o.get("contact_page") else "blocked")
        states[state] = states.get(state, 0) + 1
        rec = {
            "org": o["org"], "slug": o["slug"], "state": state,
            "authors": [{"name": a, "role_as_printed": roles[a]["role_as_printed"],
                         "wrote": roles[a]["stated_in"]} for a in o["authors"]],
            "route": {
                "kind": route,
                "role_addresses": o["addresses"],
                "contact_page": o.get("contact_page"),
                "site": o.get("site"),
                "established_how": o.get("established"),
            },
            "evidence": {
                "frozen": [f["path"] for f in o.get("frozen", [])],
                "sha256": [f["sha256"] for f in o.get("frozen", [])],
                "published_at": f"{HOST}/contacts.html#orgs",
            },
            "why_no_route": o.get("why_none"),
            "never": "No personal contact detail for any named person. Route through the "
                     "organisation or do not write.",
            "actions": [],
        }
        (OUT / "targets" / f'{o["slug"]}.json').write_text(
            json.dumps(rec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    (OUT / "state.json").write_text(json.dumps({
        "id": "wnd-outreach-state",
        "built_from": {"snapshot": corpus["snapshot"], "section": f"{HOST}/"},
        "targets": len(contacts["organisations"]),
        "by_state": states,
        "authors": contacts["counts"]["authors"],
        "authors_with_a_route": contacts["counts"]["authors_reachable_via_an_organisation"],
        "actions_recorded": 0,
        "note": "Nothing has been sent. This is the state at handover; the collaborating agent "
                "updates it from the action log, and the action log is the source of truth.",
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    (OUT / "evidence.md").write_text(f"""# Verifying anything in here

Every claim in this vault traces to the corpus vault or to a published page. Neither asks to
be taken on trust.

## The corpus vault

A separate, finished vault holding the twenty-one op-eds as frozen bytes, every derived
dataset, the build code and the gate. Its **public read key** is published at
{HOST}/vault.html — a read key grants read and only read.

The same contents are downloadable without any tooling:

    curl -O {HOST}/vault.zip
    shasum -a 256 vault.zip        # {vault['sha256']}
    unzip vault.zip -d wnd && cd wnd
    python3 build/gates.py         # re-derives every published count from the frozen bytes

`MANIFEST.json` inside carries the SHA-256 of every file. The `stands_on` field of an action
should carry one of those hashes, or a URL under {HOST}/.

## The published pages

- {HOST}/licences.html — the licence finding, both wordings quoted verbatim
- {HOST}/corpus.html — the twenty-one described, linked, never reproduced
- {HOST}/findings.html — the aggregate, and how it maps to what we have argued
- {HOST}/contacts.html — the routes in `targets/`, and the rules that produced them
- {HOST}/method.html#corrections — what this section has already got wrong, and fixed

## If a number here and a number there disagree

The data files win, and the disagreement is a `corrected` action. Do not reconcile it by
editing this vault quietly.
""", encoding="utf-8")

    n = len(list((OUT / "targets").glob("*.json")))
    print(f"outreach: {n} targets, {states}, 0 actions — nothing sent")
    return states


if __name__ == "__main__":
    main()
