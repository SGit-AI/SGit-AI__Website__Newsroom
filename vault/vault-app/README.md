# The newsroom's vault viewer

The app every reader vault of newsroom.sgit.ai opens with (card 079). It lives in this vault, which the newsroom publishes with a public read key, and is linked read-only into each reader vault:

- `newsroom-viewer.link.json` in the reader vault: the pointer, with no key;
- `.vault/owner/ro-links.json`: this vault's read key and ref file id, the vault UI's own convention;
- `.vault/app.json`: `entry: index.html`, `present: true`, so the reader vault boots into the app;
- `index.html`: a small entry page that loads `newsroom-viewer/viewer.js` from here with `sg.loadJs`, and shows a plain summary if it cannot.

`viewer.js` reads the reader's records (`activity/account.json`, `activity/devices/*.json`, `activity/aliases.json`) with `sg.vfs`, recomputes the account as the pane does, and renders it. It writes nothing and sends nothing. Opened on its own, this vault shows `demo/activity/`, a made-up account.

Source: `vault/vault-app/` in the newsroom.sgit.ai repository. Published with `admin/build/viewer_vault.mjs`.
