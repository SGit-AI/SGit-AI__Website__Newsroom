# Evidence 1: agent identity as it runs (read 29 October 2026)

## The PHP newsroom's published keys
`https://team.php.oct.2026.newsroom.sgit.ai/records/keys/<agent>.json`, read 29 October 2026: ten roles, each record
with `fingerprint`, `encryption_fingerprint`, `public_key` (`k1.` code), `session`, `account`, `from`, `replaces`,
`enrolled` (false). Registered on 28 October 2026 (UTC):

| Role | Fingerprint | From |
|---|---|---|
| dev | sha256:d1331dd12796268e | 01:05:04 |
| conductor | sha256:4bce1d42efd5cb02 | 01:33:49 |
| researcher | sha256:f67bd9ea1e3dec26 | 02:43:30 |
| security | sha256:c944bb5021328dc6 | 02:44:29 |
| curator | sha256:1bfc70ecaaa1ad0d | 02:44:35 |
| journalist | sha256:79a3b7c3bd755aeb | 02:56:34 |
| factcheck | sha256:df7208f6026500f5 | 02:56:55 |
| observability | sha256:fad2cd94a3f3d474 | 03:25:37 |
| correspondent | sha256:60a78bc4a1dcc0b2 | 03:26:45 |
| desk | sha256:46922be9562315cb | (see its record) |

Each has a QR image beside it (`records/keys/<agent>.png`).

## pki.sgit.ai's register
`https://pki.sgit.ai/directory/index.json` (site v0.2.30), read 29 October 2026: 11 records; counts `real_keys` 1,
`agent_keys` 2, `fixtures` 8; anchor `sha256:db7f79fdd87e030a` (dinis.cruz). Agent records:
- `sha256:956934e47063ceaa`, "DC Vault Registry (the vault of vaults)": "Catalogues every SG/Send vault key Dinis Cruz
  and his agents create; receives vault keys and records them"; operated-by the root; the root's `operates` link on
  2026-10-23, until 2026-10-30.
- `sha256:a0f2ccfe07781213`, "pki.sgit.ai site agent (Claude Code session, 19 October 2026)"; operates link until
  2026-10-29.

## An agent-to-agent handover, first-hand (28 October 2026)
newsroom.writer's session made a session key pair with `pki-agent.mjs keygen --session` (fingerprint
sha256:a3bf562dc9ed9306), pinned the root from this repository (`admin/content/agents/dinis-cruz/ROLE.md`), read the
registry's public key from a QR image Dinis shared, checked it with `pki-agent.mjs trust` ("an agent operated by
dinis.cruz; confirmed 2026-10-23, valid until 2026-10-30"; chain sha256:956934e47063ceaa to sha256:db7f79fdd87e030a),
and sealed the vault key of m1wbrefr to it with `seal --to sha256:956934e47063ceaa --from-vault`, never printing the key.
The sealed QR: 1,693 bytes, "to" the registry, "from" the session's key. pki-agent.mjs sha256
fcb28a1cc40d05bf8ccc8fc61a2a907c934840cac7aa41d9d8283c1d461002ab, the same as the PHP newsroom's pinned copy.
