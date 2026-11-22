# Memo 01, 22 November 2026: two writers, as twins on two accounts

Dinis's answer to writer-10, word for word, after writer-10 asked him to confirm two things: that the twin, newsroom.d@sgit.ai.dinis, runs on account D (run by maestro.d), and that the newsroom's one-writer rule changes to allow two writers at once.

> yes confirm both

## What it changes

- `admin/writer/register.json` now allows at most two open registrations (`max_open: 2`, approved by this memo), instead of one.
- Two open registrations must be on different accounts (`account`, the letter in the agent's name): that is what makes them twins, the same role on two accounts. A second writer on the same account is refused.
- Every other rule of memo 01 of 31 October stands: a registration is opened only at the editor's word, with a new key made in the writer's own session; a closed registration is never reopened; its key is never used again.
- `admin/writer/tools/sign.cjs` signs with the one open registration whose private key is on this machine.
- The two writers avoid each other with the claim rule in `CLAIMS.md` beside this memo, as maestro.b proposed: writer-10 keeps what it holds; the twin claims each article before writing; never two builds at once.
- writer-10 is recorded as `newsroom.b@sgit.ai.dinis` on account b. The twin's registration is opened by the twin in its own session on account D, at Dinis's word there, with this memo as its approval.
