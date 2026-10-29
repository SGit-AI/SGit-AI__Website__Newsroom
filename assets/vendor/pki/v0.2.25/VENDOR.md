# The register's key code, vendored: pki.sgit.ai v0.2.25

The two files in this folder are pki.sgit.ai's own modules for keys and the register of people, copied unchanged from
the site as it served them on 24 October 2026 (site version v0.2.25), so that newsroom.sgit.ai checks signatures and
standings with the register's code and from its own origin. Nothing here is edited; a fix is picked up by refreshing
this copy and its hashes.

**Upstream:** https://pki.sgit.ai/assets/people/keys.js and https://pki.sgit.ai/assets/people/directory.js, the
modules pki.sgit.ai's own pages and its build (`admin/build/people.mjs`) run. `directory.js` imports `./keys.js` and
nothing else; `keys.js` imports nothing.

**Used by** `assets/pen/identity.js`: a browser's key made with `generate`, its record's statements with
`agentStatement` and `linkStatement`, the register read with `readRecord` and `graph`, and a signer judged with
`trustFrom` from a pinned root (Dinis Cruz's master key, `sha256:db7f79fdd87e030a`).

| File | SHA-256 |
|---|---|
| `keys.js` | `7c97cbd9dab3c3969b6bed4f24bce211c0406cee15c5a88458fec9fc5d48d143` |
| `directory.js` | `19d0c8bd374c0670c698d27dcd5a63425560a12013a2efbe7de347d58f3a4a5a` |
