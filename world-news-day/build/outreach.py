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


def page_json(contacts, corpus, states):
    """The outreach vault as a page rather than a folder of JSON.

    Same convention as the corpus vault and as sgit.ai's published vaults: a `_page.json` at
    the root so that opening the vault shows what it is for and what the rules are, rather
    than whichever file sorts first — which here would be README.md's neighbour in a tree of
    twenty-seven target files."""
    c = contacts["counts"]
    return {
        "title": "World News Day 2026 — the outreach vault",
        "theme": {"mode": "light", "accent": "#b45309", "font": "sans",
                  "density": "comfortable", "background": "#faf9f7"},
        "navigation": [
            {"label": "What this is", "anchor": "what-this-is"},
            {"label": "The rules", "anchor": "the-rules"},
            {"label": "The state", "anchor": "the-state"},
            {"label": "Verify", "anchor": "verify"},
        ],
        "components": [
            {"type": "hero", "props": {
                "title": "The outreach vault",
                "subtitle": f'{c["organisations"] - 1} organisations · {c["authors"]} authors · '
                            f'{states.get("ready", 0)} ready to contact · nothing sent',
                "color": "#2b1e14", "height": "medium", "align": "center"}},
            {"type": "section", "props": {"title": "What this is", "layout": "narrow"},
             "children": [
                {"type": "text", "props": {"content":
                    "The working vault for reaching the people who wrote the twenty-one World "
                    "News Day op-eds. It is separate from the corpus vault on purpose: that "
                    "one is a finished record of what somebody else published and is safe to "
                    "hand to anyone, including the people it describes. This one is an "
                    "append-only record of what we do about it, and it moves every time a "
                    "message is sent or answered."}},
                {"type": "text", "props": {"content":
                    "Not one of the twenty-one pages offers a way to reach its author or its "
                    "publisher — no contact address, no author URL in the structured record, "
                    "no press line. That is why this exists as a separate piece of work "
                    "rather than a mail merge."}},
             ]},
            {"type": "section", "props": {"title": "The rules", "layout": "narrow",
                                           "background": "alt"},
             "children": [
                {"type": "bullet-points", "props": {"items": [
                    "No personal contact detail for any natural person, ever. Route through "
                    "the organisation's published role address or contact form.",
                    "Every action names what it stands on — a SHA-256 from the corpus vault, "
                    "a URL, or an earlier action here. An action that stands on nothing is an "
                    "assertion.",
                    "Append; never edit. A wrong action is corrected by a new action that "
                    "names it. The history is the product.",
                    "Say what is good about their work first, and mean it. One ask per "
                    "message, and make it small.",
                    "Escalate rather than commit the newsroom to anything: no embargoes, no "
                    "exclusivity, no payment, no publishing to the site.",
                ]}},
                {"type": "markdown", "props": {"file": "protocol.md"}},
             ]},
            {"type": "section", "props": {"title": "The state", "layout": "narrow"},
             "children": [
                {"type": "bullet-points", "props": {"items": [
                    f'{states.get("ready", 0)} organisations with a published role address',
                    f'{states.get("route only", 0)} with a contact page or LinkedIn but no address',
                    f'{states.get("blocked", 0)} with no route established at all',
                    f'{c["authors_reachable_via_an_organisation"]} of {c["authors"]} authors '
                    "reachable, every one of them via an organisation",
                    "0 actions recorded. Nothing has been sent.",
                ]}},
                {"type": "markdown", "props": {"file": "brief.md"}},
             ]},
            {"type": "section", "props": {"title": "Verify", "layout": "narrow"},
             "children": [
                {"type": "markdown", "props": {"file": "evidence.md"}},
             ]},
        ],
    }


def agent_brief(contacts, licences, corpus, analysis, claims, terms, vault, outreach_vault):
    """The operational brief: what the agent at diniscruz.ai is being asked to do, to whom, in
    what order, with what words, and what it must write down afterwards.

    Separate from brief.md, which says what we are ASKING FOR. This one says how to ask. It is
    generated so that every figure in the message templates comes from the data files rather
    than from a draft somebody typed, and so it can be rebuilt when the corpus is recaptured."""
    C, K, A = licences["counts"], contacts["counts"], analysis["evidence"]
    bt = claims["counts"]["by_type"]
    ready = [o for o in contacts["organisations"] if o["addresses"]]
    route_only = [o for o in contacts["organisations"]
                  if not o["addresses"] and (o.get("contact_page") or o.get("linkedin"))]
    blocked = [o for o in contacts["organisations"]
               if not o["addresses"] and not o.get("contact_page") and not o.get("linkedin")]

    def rows(group):
        out = []
        for o in sorted(group, key=lambda x: x["org"]):
            who = ", ".join(o["authors"]) or "—"
            route = (", ".join(o["addresses"]) if o["addresses"]
                     else o.get("contact_page") or (o.get("linkedin") or ["—"])[0])
            out.append(f'| {o["org"]} | {who} | {route} |')
        return "\n".join(out)

    return f"""# Brief: the World News Day outreach

**For the AI agent at diniscruz.ai.** You are being asked to run the outreach on this work:
to write to the people who wrote twenty-one op-eds, to the organisation that commissioned
them, and to newsrooms beyond the corpus who would find the finding useful. Everything you
need is published; nothing here asks anyone to take us on trust.

Read `protocol.md` before you write anything. It is short, it is strict, and it binds you the
way the build gates bind the newsroom. Read `brief.md` for what we are asking for. This file
is how to ask.

---

## 1 · What has been established

All of it is published at <https://newsroom.sgit.ai/world-news-day/> and every number walks
back to bytes that are frozen and hashed in the corpus vault.

- **{corpus['count']} op-eds**, commissioned by WAN-IFRA and the Canadian Journalism Foundation
  for World News Day on 28 September 2026, and made free to republish. All
  {corpus['count']} grant permission. **{C['carrying_a_named_public_licence']} grant it under a
  licence with a name.** No Creative Commons, no `rel="license"`, no copyright notice.
- **The terms are stated three different ways** — twice on the articles, once on the
  announcement, and they do not agree. The articles require republication *in full* and never
  mention credit; the announcement requires *appropriate credit* and never says in full.
- **{C['with_ld_json']} of {corpus['count']} already ship schema.org JSON-LD**, generated
  automatically by the site's own SEO plugin.
  **{C['whose_ld_json_declares_a_licence']} populate its `license` field.** That is the ask:
  one line in a record that is already being written.
- **{A['with_no_outbound_link_at_all']} of {A['articles']} offer the reader no outbound link at
  all.** {A['total_links']} links across the whole corpus; of {A['distinct_domains']} domains
  cited between them, no two pieces point at the same one.
- **{bt.get('proposal', 0)} of {claims['counts']['claims']:,} sentences propose doing
  anything.** {bt.get('assertion', 0)} are flat assertions.
- **{terms['counts']['definitions_found']} places in {claims['counts']['claims']:,} sentences
  where anybody says what trust, truth or journalism *means*.**
- **Not one of the {corpus['count']} pages offers a way to reach its author or its publisher.**
  Which is why this vault exists rather than a mail merge.

## 2 · The links to send

Send these, not attachments. Everything is public and nothing needs an account.

| What | Link |
|---|---|
| The section | <https://newsroom.sgit.ai/world-news-day/> |
| **The finding** | <https://newsroom.sgit.ai/world-news-day/licences.html> |
| The article, written to be sent | <https://newsroom.sgit.ai/world-news-day/stories/free-to-republish-is-not-a-licence.html> |
| Their own piece, described | `https://newsroom.sgit.ai/world-news-day/pieces/<slug>.html` — one page per op-ed, the slug is on each target file |
| The aggregate | <https://newsroom.sgit.ai/world-news-day/findings.html> |
| The vault (read-only, no account) | <https://newsroom.sgit.ai/world-news-day/vaults/corpus.html> |
| The bundle, no tooling at all | <https://newsroom.sgit.ai/world-news-day/vault.zip> |
| What we got wrong, and fixed | <https://newsroom.sgit.ai/world-news-day/method.html#corrections> |

The corpus vault opens read-only with a published key and no account:
`sgit clone {vault['read_key']}:{vault['vault_id']}`

**Lead with their own piece's page, not with ours.** A person will click a page about their own
work before a page about our argument.

## 3 · Who to write to, and in what order

Three tiers. Do them in order; do not start tier 2 before tier 1 has had a week.

### Tier 1 — the commissioner ({len([o for o in contacts['organisations'] if 'WAN-IFRA' in o['org'] or o['org'] == 'World News Day'])} targets)

WAN-IFRA and World News Day commissioned the corpus and can fix all three asks at once. They
are the only ones who can. Write here first, and say plainly that the other twenty-one letters
are on hold until they reply, because a licence is theirs to name, not an author's.

### Tier 2 — the {len(ready)} organisations with a published role address

| Organisation | Who writes from it | Route |
|---|---|---|
{rows(ready)}

### Tier 3 — the {len(route_only)} with a contact page or LinkedIn but no address

| Organisation | Who writes from it | Route |
|---|---|---|
{rows(route_only)}

### Not reachable: {len(blocked)}

{rows(blocked) or '| — | — | — |'}

No route was established for these under the published rules. **Do not go looking for a
personal address.** If you find a published organisational route, record it as a `noted`
action with where you found it, and it will be added to the map at the next build.

### Beyond the corpus

Newsrooms, press bodies and journalism-school programmes who are not in the corpus but would
use the finding. Same rules, same links, and one change to the message: they are not being
asked to fix anything, they are being shown a method they can apply to their own archive.
Keep this tier small and specific. A hundred generic letters would be spam, and would discredit
the work rather than spread it.

## 4 · What to say

Three templates. Adapt them; do not send them verbatim to twenty-seven people. **One ask per
message.** If a draft would be embarrassing to receive, it is wrong.

### 4a · To the commissioner

> Subject: World News Day 2026 — the twenty-one op-eds, and one line of JSON
>
> You gave away twenty thousand words for World News Day, in a year when almost nobody in
> this industry gives anything away. We took that seriously enough to look at what it amounts
> to for anyone who wants to act on it — a translator, a local paper, an archive, a machine.
>
> We fetched all {corpus['count']} pieces, froze and hashed them, described every one, and
> republished none of them. The description is public and free to reuse:
> https://newsroom.sgit.ai/world-news-day/licences.html
>
> The finding, in one line: all {corpus['count']} grant permission to republish;
> {C['carrying_a_named_public_licence']} grant it under a licence with a name. The terms are
> stated three different ways — twice on the articles, once on the announcement — and they do
> not agree on whether credit is required or whether an extract is allowed.
>
> The part that is nearly done already: all {C['with_ld_json']} pages ship schema.org JSON-LD,
> generated by your own SEO plugin. None uses its `license` field. One line in a record that
> is already being written would make twenty thousand words of deliberately open material
> usable as open material by every machine that reads the page.
>
> Three small things, all on the publisher's side: name the licence; put it in the JSON-LD you
> already ship; state the terms once, in one place, with a contact on it.
>
> Everything is checkable — the frozen bytes, the counts and the code that produced them are
> one download: https://newsroom.sgit.ai/world-news-day/vault.zip
>
> We are not neutral: we are building infrastructure for exactly this, and we say so on every
> page. We have also already corrected ourselves in public about your own infrastructure:
> https://newsroom.sgit.ai/world-news-day/method.html#corrections
>
> If anything here is wrong, tell us and it changes.

### 4b · To an author's organisation

> Subject: Your World News Day op-ed, described and linked
>
> [AUTHOR] wrote [TITLE] for World News Day. We have described it — who wrote it, what it
> argues, what it cites, and the terms it is published under — without republishing a word of
> it: [PIECE PAGE URL]
>
> We did the same for all {corpus['count']} pieces, and one thing stood out. All
> {corpus['count']} say they are free to republish. None says so under a licence with a name,
> and none uses the schema.org `license` field its page already ships. That is a publisher-side
> fix rather than an author-side one, and we have written to WAN-IFRA about it.
>
> Two things you might find useful in your own archive: whether your structured data carries
> your terms, and whether your pieces give a reader anything to follow. Across this corpus,
> {A['with_no_outbound_link_at_all']} of {A['articles']} offer no outbound link at all.
>
> All of it is free to reuse under CC BY 4.0, and it is checkable rather than assertable:
> https://newsroom.sgit.ai/world-news-day/
>
> If we have anything wrong about [AUTHOR] or [ORGANISATION], say so and it changes — we
> record corrections in public, with the version that carried the error.

### 4c · Beyond the corpus

> Subject: A method for checking what your archive actually says
>
> Twenty-one op-eds were published for World News Day and made free to republish. We froze
> them, described them and published the description — and found that none names a licence,
> none populates the `license` field its own pages already ship, and
> {A['with_no_outbound_link_at_all']} of {A['articles']} give the reader no link to follow.
>
> The method is more useful than the finding: every count is derived from frozen bytes by one
> program and re-derived by a second, the classification rules are published so you can
> disagree with them precisely, and the whole corpus is one download with a hash.
>
> https://newsroom.sgit.ai/world-news-day/method.html
>
> If it is useful against your own archive, take it. It is CC BY 4.0.

## 5 · What to record, every time

One file per action in `actions/`, matching `actions/_schema.json`, named
`<utc-timestamp>__<target-slug>__<verb>.json`. **Append; never edit.**

Every action names what it `stands_on`: a SHA-256 from the corpus vault's `MANIFEST.json`, a
URL under newsroom.sgit.ai, or the id of an earlier action here. An action that stands on
nothing is an assertion, and this vault exists so that outreach is not a pile of assertions.

Record `no_response` explicitly once a fortnight has passed. Silence is data; an empty folder
is not. Fill `uncertain` rather than rounding a doubt away.

## 6 · Pacing, and when to stop

- Tier 1 first, then wait a week.
- No more than five messages a day across all tiers.
- One follow-up per target, after two weeks, and never a second.
- A `declined` is final: record it and stop. No other channel, no later attempt.
- Escalate rather than commit the newsroom to anything: no embargoes, no exclusivity, no
  payment, no publishing to the site.

## 7 · The state right now

{outreach_vault['targets']} targets, **{outreach_vault['actions_recorded']} actions recorded,
nothing sent.** {K['authors_reachable_via_an_organisation']} of {K['authors']} authors have a
published route, every one of them via an organisation.

Rebuild this brief with `python3 world-news-day/build/outreach.py` after any recapture; every
figure in it comes from the data files rather than from a draft.
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

    (OUT / "agent-brief.md").write_text(
        agent_brief(contacts, licences, corpus, load("analysis.json"), load("claims.json"),
                    load("terms.json"), load("vault.json"), load("outreach-vault.json")),
        encoding="utf-8")

    (OUT / "_page.json").write_text(
        json.dumps(page_json(contacts, corpus, states), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8")

    n = len(list((OUT / "targets").glob("*.json")))
    print(f"outreach: {n} targets, {states}, 0 actions — nothing sent")
    return states


if __name__ == "__main__":
    main()
