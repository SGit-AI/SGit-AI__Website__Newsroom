---
id: 089
title: The PHP desk: an admin page for the work and the roles, and the evidence vault opened with a public read key
kind: story
priority: high
created: 2026-10-22T13:00:00Z
source: Dinis, in chat, 22 October 2026: "can you create an admin section for us to track our work, for us to define all the roles and responsibilities with the multiple agents that we're working on here, for us to provide, for example, a view of the vault that we have here ... we need to share the vault with a public read key the same way that we do on the main sgit.ai vault or the newsroom.sgit.ai"; on scope, "you are only working on the main newsroom.sgit.ai website, for now 100% focused on this PHP story"; on the vault, "we should publish the whole vault"
estimated_effort: medium
---
# The PHP desk and the open vault

## What is asked
One admin page for the PHP story: the work and who owns it, the roles and responsibilities of the people and agents, and a view of the evidence vault, opened to everyone with a public read key.

## Scenario
```gherkin
Given work.json and roles.json in admin/content/php-oct-2026/
When admin/build/php_desk.py runs
Then /admin/php-oct-2026/ shows the work (open first), the roles, and the vault with its public read key and the scan
And the build refuses a work row whose owner is not in the roles, or a done row with no proof

Given a reader opens the page
Then the vault is read in the browser with the public read key: the manifest first, and a source's notes, captures, thumbnails, screenshot and text only when opened
And a clone made with the read key cannot push
```

## Mock-up
Crumb admin / php desk; four counts; the work table with status pills; by owner; the move's five checks; role cards (kind, name, responsibility, may, must not, works in, record); the vault box with the read key, clone command and two buttons; the live view with a filter; the scan; the vault's contents by writer, kind and top level; the latest commits.

## Outcome
v0.13.42: `admin/build/php_desk.py`, `admin/php-oct-2026/` (index.html, desk.css, vault-view.js on wire/vault-reader.js), `admin/content/php-oct-2026/work.json` and `roles.json`, `admin/content/vaults/php-evidence.json`; the brief `admin/notes/2026-10-22__the-php-desk.md`; the article *A desk anyone can open* by newsroom.dev, newly registered in `admin/content/agents.json`; the review of the story's site, `briefs/php-oct-2026-review.zip`. Left: work rows w-17 to w-19, w-21 to w-23.
