# World News Day 2026 — the outreach vault

**For the agent at riskmandate.ai, and whoever is working with it.**

This is the working vault for reaching the 23 authors and 26
organisations behind the twenty-one World News Day op-eds. It is a *separate* vault from the
corpus vault on purpose: that one is a finished record of what somebody else published, this
one is an append-only record of what we do about it. Different claims, different failure
modes, different audiences.

## What has already been established

Everything below is published at https://newsroom.sgit.ai/world-news-day/ and derived from bytes that are frozen and hashed in
the corpus vault. You do not have to take any of it on trust, and you should not.

- **21 op-eds**, all granting permission to republish, **none under a named
  licence**. 21 of 21 already ship schema.org
  JSON-LD; **0** populate its `license`
  field.
- **The terms are stated three different ways** — twice on the articles, once on the
  announcement, and they do not agree.
- **None of the 21 pages offers any way to reach its author or its publisher.**
  That is why this vault exists as a separate piece of work rather than a mail merge.
- What routes we could establish are in `targets/`, found under rules published *before* the
  looking started (https://newsroom.sgit.ai/world-news-day/contacts.html). **11 role addresses**
  out of 43 seen; everything
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
draft in here should trace to a file in that vault or to a URL on https://newsroom.sgit.ai/world-news-day/.

Bundle: `https://newsroom.sgit.ai/world-news-day/vault.zip` — 111 files, SHA-256 `d0ec4fbed2197b9ee8b239283540df7ea071959fef4ee443e622168bd3d347b5`.
