# Send to my vault from any browser: an inbox on the reader vault, a link three ways, and the drain

*13 October 2026, built in newsroom.sgit.ai v0.12.26. Card 049. The request and the brief are the article [Sixteen notes I did not want to lose](../../articles/sixteen-notes-i-did-not-want-to-lose.html) (No. 105). The sending page is [/vault/send.html](../../vault/send.html); the link is made in the vault pane's Vault tab.*

## In short

- **The problem.** The vault opens with a passkey, and some browsers cannot reach one: a web view an app opens a link in, a browser signed in to nothing, an old iPad. What they hold stayed there, counted on the Vault button as changes only in this browser. The only way in without the passkey was the recovery code, which opens the master: too much power for a job that only needs to add.
- **The answer is a lane.** Every account can have an inbox: an append lane on the reader vault that any browser can write to and none can read, and a key pair made in the reader's browser whose private half is in the master. The link carries where to write and the key to encrypt to, nothing else.
- **A browser with the link sends its own device file**, the same file the vault already holds for every device, sealed to the key. The vault takes it in the next time it is opened with the passkey: the pane lists what is waiting, opens it, shows it, and on one press writes it into the reader vault as that browser's file, so the merge that already exists brings it in, with that browser as the author.
- **Nothing new on the server.** The append routes (`/api/vault/append/*` on dev.send.sgraph.ai), the envelope (sgit's hybrid v2) and the device files existed; the pieces new here are the reader's key pair, the link, the sending page and the drain.

## The four capabilities

The append-lanes API splits what a lane can do into four, and the design puts each where it belongs:

| Capability | Where it lives | Can |
|---|---|---|
| append token | in the link, and in the master | write to this lane; nothing else |
| enum key | in the master (random, 32 bytes; the server keeps its hash) | list, fetch, mark processed |
| write key | derived from the reader vault's key, which the master holds | configure the lane (with the access key), purge |
| private key | in the master (RSA-OAEP 3072, PKCS#8) | decrypt; never sent anywhere |

The link is `https://newsroom.sgit.ai/vault/send.html#sgi1.<reader vault id>.<append token>.<public key, SPKI, base64url>`, about 650 characters. The fragment never reaches a server, and the sending page takes it out of the address once it has kept it, so a copied address or a screenshot does not carry it.

## The flow

1. **Make the link** (the Vault tab, unlocked): a key pair in this browser; a random append token (16 bytes) and enum key (32 bytes); `configure` on the reader vault with `append_anchors: [sha256(token)]` and `enum_key_hash`, with the reader vault's write key and the access key from the master; the record `inbox.json` written into the master.
2. **Send** (any browser, `vault/send.html`, or *Send to my vault* in the strip above the pane once a link is kept): `extract()` this browser's own records into one device file, wrap it as `{kind: "sgit-newsroom-inbox/v1", to: <key fingerprint>, sent_at, file}`, seal it (a fresh AES-256-GCM key wrapped with RSA-OAEP, the envelope `{v: 2, w, i, c}`, base64 twice as the API documents), and `POST /append/write` with the token. The answer is `{"ok": true}` and nothing else. The browser keeps every record; the time of the send becomes its last update, so the count goes to zero.
3. **Drain** (the Vault tab, every time it is drawn, and on *Look in the lane*): `list` with the enum key, `fetch` each lane's pending files, open each with the private key, check it. Valid messages are listed by the name the browser gave itself, the time and what they carry; refused ones with the reason.
4. **Bring them in**: each browser's files combined (`combine()`: every record of either, the one that knows more where both have it), combined again with the file already in the vault for that browser, written, one publish; `mark-processed`; then the merge every device already uses, which reloads the page and says what arrived.
5. **A new link**: a new token, the same key; `configure` replaces the anchors, so the old token is refused (404). It waits until the lane is empty, so nothing is stranded in a lane no anchor names.

## What is refused

A message that does not open with the key (sealed to another one), one whose ciphertext was changed (AES-GCM's tag fails), one that opens but is not a newsroom inbox message, is addressed to another key's fingerprint, carries a browser id that is not a plain file name, or has notes that claim another browser. They are listed and can be discarded; nothing in them is merged.

What is not refused: a well-formed message from whoever holds the link. That is the brief's model: the link writes, it does not prove who wrote. The drain shows the browser's name, its platform, the time and the counts before anything is brought in, and a new link stops the old one.

## Choices, and why

- **RSA-OAEP 3072, not 4096.** The sgit CLI makes 4096-bit keys. 3072 is 128-bit security, and it keeps the link at about 650 characters and the QR code at 89 modules, which a phone camera reads off a laptop screen; at 4096 the link is about 820 characters and the code 97 modules.
- **The device file as the message.** Inventing a second format for the same records would have needed a second merge. A browser that sends through the inbox is a device like any other: it gets a row across the devices, and its records keep it as their author.
- **The lane on the reader vault, not a new vault.** The brief asks for it there; it keeps the account at four vaults (door, master, reader, the newsroom lane) and the inbox's files out of every commit tree (`bare/append/…`).
- **The sending page loads no vault library.** It reads local storage, encrypts with Web Crypto and makes one POST, so it works where nothing else of the vault does.

## Not built

- **Expiry.** The append routes have no expiry on a token; a date in the link would be honoured by this page and by nobody else. A new link is the revocation the server enforces.
- **Signatures.** A sender holds no key; the link is the credential, as for the subscribe form.
- **Purge** of processed files (write key and access key; a later release).
- **The reply lane** (card 015): the newsroom answering under a message. The same machinery, pointed the other way.
- **An A/B test** of the link against a pairing flow, which the article proposes.

## Tests

`admin/build/test_inbox.mjs`: in Node, the link, the envelope, the refusals and `combine()`; in Chromium, against the mock of the vault API (now with the append routes), browser A with a virtual passkey makes the account and the link (the QR code decoded back with jsQR), browser B with no passkey at all reads, keeps notes and sends twice, three bad messages are appended beside them, A brings B's in and refuses the three, discards them, makes a new link, and the old one can no longer write.
