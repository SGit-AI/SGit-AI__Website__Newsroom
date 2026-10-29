# pki.sgit.ai's message code, vendored: pki.sgit.ai v0.2.30

`message.js` and the `keys.js` it imports, copied unchanged from pki.sgit.ai as it served them on 27 October 2026
(site version v0.2.30; `keys.js` is byte for byte the copy in `assets/vendor/pki/v0.2.25/`). Nothing here is edited.

**Upstream:** https://pki.sgit.ai/assets/people/message.js and https://pki.sgit.ai/assets/people/keys.js.

**Used by** `admin/build/review_lane.mjs create`: the review lane's secret is composed as a pki message, sealed to
the editor's published key and handed over as a `https://pki.sgit.ai/m/#m1...` link that only that key opens, so the
secret is never printed or written to the repository (card 091).

| File | SHA-256 |
|---|---|
| `message.js` | `ad91e33ab9a711cad431bfc92f5610c5fe131e828a8e99450dbeccb1535b3b49` |
| `keys.js` | `7c97cbd9dab3c3969b6bed4f24bce211c0406cee15c5a88458fec9fc5d48d143` |
