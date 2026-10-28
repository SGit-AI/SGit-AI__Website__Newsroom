# Handover: @newsroom.reviews

*From @newsroom.dev, 28 October 2026, to the session that starts as @newsroom.reviews. Read this, then `admin/notes/2026-10-27__the-reviewers-vaults.md` and `admin/notes/2026-10-27__the-review-lane.md`. Everything below is checked against the repository and the live vault on the day it was written.*

## State

- **ChatGPT's review vault is `gfzbzp41`** on https://dev.send.sgraph.ai, public. Its read key is in `admin/content/reviews/vaults.json` (published at `reviews/vaults.json`). Its vault key is held by the editor, who sealed nothing to you yet.
- **ChatGPT's key** is `sha256:dec7fa758ecb9eb1` ("ChatGPT newsroom reviewer, this workspace"), pinned as `reviewer_key` in `vaults.json`. It belongs to ChatGPT's current session only. It wrote `keys/reviewer.json` and one note, `notes/2026-10-28__openai-chatgpt__connection-and-email-fs.eml`, both signed by that key.
- **The desk's signature on the vault's files is dead.** `README.md`, `brief.md`, `criteria.md`, `queue.md|json`, `keys/` and `answers/` are signed by a desk key (`sha256:fb35b723a2ae8b98`) whose private half was deleted, because private keys stay in the session that made them. Nobody can sign as that key any more. ChatGPT pinned it from the site, so it will refuse your new key until told.
- **The review lane** (vault `jk20axc2`, an append lane for reviewers without a vault) works and was tested live. Its secret was never handed over: nothing drains it yet. Perplexity has no vault.
- **The tools exist and are tested** (`admin/build/test_review_vault.mjs`, `test_review_lane.mjs`): `review_vault.py create|publish|gate|take|scan`, `review_keys.mjs`, `review_queue.py`, `review_lane.mjs create|drain|mark`.

## What to do, in order

1. **Make your key** in this session (`sgit pki keygen`, or `node admin/build/review_keys.mjs make`, which should be changed to keep the private half in memory and show the editor a pki.sgit.ai key QR code). Do not write the private half to a file in the repository or send it anywhere. Show the editor the key QR code and the register submission, and ask him to link it from his root key with "operates".
2. **Receive the vault key**: the editor seals it to your key as a pki.sgit.ai sealed QR code (the same way it reached ChatGPT). Open it; keep it in this session.
3. **Replace the dead desk key.** `admin/build/review_vault.py` and `review_keys.mjs` still call this role "desk" (`keys/newsroom-desk.json`, `NEWSROOM_DESK_KEY`). Rename to `newsroom-reviews`, load the key from this session instead of the environment, and publish the new public bundle at `reviews/keys/`. Then `review_vault.py publish openai-chatgpt` re-signs everything in the vault, and tell ChatGPT (in a signed note) to re-pin the key from https://newsroom.sgit.ai/reviews/keys/. Ask the editor to approve before the first publish.
4. **Answer ChatGPT's question** in its note: does the vault support Email-FS-lite (immutable `.eml` messages, recipient inbox/done folders, a sender outbox copy)? The recommendation was yes. If the editor agrees: update the vault README, the brief and the security check (`notes/` currently allows only `.md` and `.json`; the scan reads `@reviewer.invalid` message ids as email addresses and should ignore `.invalid`).
5. **Start @newsroom.security** as its own session (the one that clears files must not be the one that takes them). Until it runs, `take` refuses everything: it needs a signed verdict.
6. **Schedule yourself**: a daily wake-up (the prompt is in the reviewers' vaults note). The security agent runs about an hour earlier.
7. **Take what is cleared**, put each finding to the editor, and ask @newsroom.writer to correct and answer them. ChatGPT's first review, of *The evidence behind four days*, is on the record with nine open findings and no proposed fixes yet: start there.

## Open decisions (the editor's)

- Email-FS-lite for the vault, yes or no.
- Perplexity: a vault of its own, or the lane. It has not said whether it can run sgit.
- Whether `admin/content/reviews/**` should be owned by this agent exclusively (the draft policy says so) and the review tools' code stay with @newsroom.dev.

## Things that were learned

- A read-only clone of a vault has no commit history, so the security gate works on file content hashes, not commits.
- `sgit pki sign` and pki.sgit.ai's `keys.js` make and verify the same signatures, both ways (ECDSA P-256 over the file's bytes).
- A sealed pki.sgit.ai QR code holds about 2,300 characters; an RSA key does not fit one, an EC signing key does.
- CI owns the version: never write a number (`admin/build/release_stamp.py --pending`).
