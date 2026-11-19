# Signed commits for the newsroom writer, 19 November 2026

## The editor's word

conductor.b@PrompTugal.dinis relayed (01:15 UTC, 19 November) that Dinis had agreed in its session that every agent publishes its public key, with its session, in the repository it maintains, and signs every commit with it (PrompTugal__News__Website, board/guidance/2026-11-19-signed-commits-paid-search-and-free-embeds.md, section 2). The writer took that as material and asked Dinis in its own session. His answer there, word for word:

> yes write that YouTube article, and add those PKI signatures to the newsroom

## What the newsroom does

- **One key per writer, as before.** The writer's registered ed25519 key (admin/writer/register.json, opened at the editor's word with register.cjs) is also its git signing key. Its OpenSSH line and the time signing began are published on the registration as `git_signing`, beside the session it was opened for.
- **Every writer commit is a git SSH signature by that key**, as well as the tree signature it already carried (Writer-Registration, Writer-Signature), and names the registration's session in its Claude-Session: trailer. `admin/writer/tools/signing-setup.sh` sets this checkout's git (locally, never globally) to sign through `admin/writer/tools/sshsig.mjs`, copied from dev@PrompTugal.dinis's tool in PrompTugal__News__Website.
- **Checked in CI and locally.** `admin/build/validate.js` check 15 (admin/build/writer_register.js) verifies HEAD's git signature and session on every writer commit, in CI on each pushed commit and in release.sh's build; with full history it checks every writer commit since `git_signing.since`. It starts from the commit that adds it; history is not rewritten. CI's own version commits ("site v...") are not writer commits and are exempt.
- **Not covered:** @newsroom.accountant's commits (another agent; its own key is its owner's step), and commits before 19 November.
