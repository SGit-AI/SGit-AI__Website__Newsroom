# Notes: versioned-api-sites (22 November 2026)

Written by newsroom.d (writer-11) at Dinis's word of 22 November (admin/notes/2026-11-22__newsroom.d-twin/memo-02.md), from the entry queued on 21 October in admin/notes/articles-to-write.md (Dinis had asked whether a write-up of how the API sites are versioned existed).

## The check

A Python script fetched each release's manifest.json from the live host and every file it lists, hashed each with SHA-256 and compared: api.send.sgit.ai v0.1.0 (36 files, 274,733 bytes) and v0.1.1 (36, 276,069); api.newsroom.sgit.ai v0.1.0 (63, 890,555), v0.2.0 (74, 1,154,686), v0.2.5 (74, 1,154,711); api.storyboards.sgit.ai /v0/v0.1/v0.1.0/ (13, 233,785). 296 files, 3,984,539 bytes, 0 mismatches, 22 November 2026 at 03:31 UTC.

## The history

SGit-AI/SGit-AI__Website__Send__API: four commits, all on 20 October; releases/v0.1.0 touched only by 07e13c8. In 07e13c8 the versioning page read 'starts as a copy of v0.1.0'; 1c9056b (v0.1.1) changed website/pages/docs/versioning/index.md and how-to/make-a-release/index.md so that both versions read v0.1.1. The Independent releases article says v0.1.0 is 34 files and 270,337 bytes; the manifest committed with it says 36 files and 274,733 bytes; not explained in the repository, and not used in the article.

## The newsroom's copies

Each of the 74 v0.2.5 paths compared with this repository at v0.14.203: 61 identical; 4 listed by the manifest as changed by the move (assets/search/ask.js, assets/search/search.js, assets/vault-pane/vault-pane.js, wire/wire.css); 9 identical at the source commit e52fe3b1 (v0.12.50) and edited after: assets/newsroom-vault.js, assets/vault-pane/notes.js, send.js, sync.js, vault-pane.css, for/for.css, for/reading-list.js, passkey/vectors.json (six edits, 28 Oct to 13 Nov), wire/wire.js.
