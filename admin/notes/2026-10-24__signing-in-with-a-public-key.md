# Signing in with a public key: newsroom.sgit.ai and pki.sgit.ai (24 October 2026)

Dinis asked, in a voice memo on 24 October 2026: can he log in to the newsroom with the key he holds on pki.sgit.ai,
how does that connect to the reader vault he already opens here with a passkey, and can a note he sends to the newsroom
be identified as his, because his public key is published in the register? This note is the design, what card 090
builds of it, and what is left for pki.sgit.ai.

## What is there today

| | newsroom.sgit.ai | pki.sgit.ai |
|---|---|---|
| Passkey | opens a door vault, then the master (the reader vault): `assets/door.js` | the same design and code: `assets/people/door.js` is this site's `door.js` copied, with one constant changed |
| Relying party | `rpId = location.hostname`: passkeys are made for newsroom.sgit.ai | the same: passkeys are made for pki.sgit.ai |
| Door derivation | `RP_FOR_DERIVATION = 'newsroom.sgit.ai'` | `'pki.sgit.ai'`: "a door here is not a newsroom door" |
| Keys | the inbox's RSA key, made for one job | a key pair per person (RSA-OAEP 4096 and ECDSA P-256, byte-compatible with `sgit pki`), published in a signed record |
| Identity | none: the reader is a browser | the register: records, two-way links, anchors; Dinis's master key `sha256:db7f79fdd87e030a` is the anchor |
| Writes from strangers | the reader's lane (needs a vault), the inbox (an append lane, sealed to the reader) | the `inbox` statement type: an append lane a record publishes |

So the two sites share a design and code, and differ on purpose in two places: each passkey belongs to its own host,
and each derives its own door from it. The same passkey cannot open both today, and the same PRF bytes would open two
different doors even if it could.

## The question, split in three

1. **Identity: is this Dinis?** The newsroom has to know a note is his, and so does an agent reading the lane later,
   from the public register, without asking the newsroom's word for it.
2. **Login: a place of his own here.** An area of the site that knows who he is: his notes, his marks, his edits.
3. **The vault: one account or two?** His reading account on the newsroom and his account on pki.sgit.ai.

## Options considered

### A. One passkey for both sites (a shared relying party, `sgit.ai`)

WebAuthn allows a page to use a registrable suffix of its own host as the relying party, so newsroom.sgit.ai and
pki.sgit.ai could both ask for passkeys made for `sgit.ai`. One passkey would then work on both. The doors could stay
separate (each site keeps its own derivation constant) or be one (the same constant).

- For: one gesture everywhere; nothing to copy between devices.
- Against: every passkey made so far is for its own host, so every reader and every pki account would have to make a
  new one; and it makes every sgit.ai subdomain able to ask for the same passkey, which is a wider door than either
  site needs. A shared door would also mean one site's code bug can read the other's vault. Not now.

### B. Sign in with pki.sgit.ai (a redirect, like OAuth, with no server)

The newsroom sends the reader to `pki.sgit.ai/authorize/#…` with a fresh public key it has made for this browser and a
nonce; pki.sgit.ai, where the reader is signed in with their passkey, shows who is asking and for what, and signs a
statement with the reader's own key: "this browser key acts for me, for newsroom.sgit.ai, until this date"; it returns
to the newsroom in the fragment. The newsroom checks the signature against the register and from then on signs as the
reader with the browser key.

- For: one click for the reader; the private key never leaves pki.sgit.ai; it is the shape people know from "sign in
  with".
- Against: needs a page on pki.sgit.ai that does not exist yet (`/authorize/`), and a delegation statement the register
  does not have yet (or an `operates` link made by that page). The best end state; the second step.

### C. A key per browser, operated by the person (the register's agent pattern)

The register already says how one key vouches for another: an agent's key is operated by a person when the person's
record links to it with `operates` and an end date, and the agent's record links back with `operated-by`. A browser is
the same kind of thing as an agent: something that acts for a person, for a while. So the newsroom makes a key pair for
this browser (pki.sgit.ai's own code, vendored), signs its identity and its `operated-by` link, and hands the two over as
a submission; Dinis signs `operates` back on pki.sgit.ai, with an end date. From then on every note this browser signs
is checked by anyone against the register, from a pinned root.

- For: works with pki.sgit.ai as it is today; uses its trust rules unchanged (two-way, dated, revocable by letting the
  link lapse); the same check runs in a browser (`trustFrom`) and in Python (`lane.py`).
- Against: three steps the first time (make, submit, link back), and the submission reaches the register by a reviewed
  commit, as every submission does today.

### D. A QR code between the two

The browser's key link (pki.sgit.ai's `k1` form) shown as a QR code on the newsroom, scanned on the phone where pki.sgit.ai
is signed in, which signs `operates` there. The same as C with the copying done by the camera. It fits the in-person QR
work pki.sgit.ai has already published.

## The recommendation

**C now, D next to it, B when pki.sgit.ai has an authorize page; not A.**

C is what card 090 builds: it needs nothing new from pki.sgit.ai and it is checkable by anyone. D is C's second step done
by camera. B removes the copying altogether and should replace C's first two steps once it exists; the browser key and
the checks stay exactly the same, only the way the `operates` link is made changes.

## The vault: connected, not merged

The reader vault and the pki.sgit.ai account stay two vaults, with two doors, on two hosts. They are connected by keys,
not by sharing a door:

- **The browser key** lives in this browser's storage, as pki.sgit.ai's own browser-only account keeps its keys before a
  vault holds them. The next step is to keep it in the reader vault's master, so every device that opens the reader vault
  can sign, and each device's key is its own record.
- **The reader vault's key can be handed to pki.sgit.ai**, sealed to Dinis's own encryption key, as a pki.sgit.ai message
  with a grant: that is how pki.sgit.ai already hands over SG/Send access keys. His pki account then holds the key to his
  newsroom vault, without the newsroom holding anything of his pki account.
- **A login area** on the newsroom is the Pen's Signed section plus the vault pane: who holds the pen, standing in the
  register, the notes they sent and their state. It is a place of one's own because the key is, not because a server
  keeps an account.

## Sending as Dinis

Today a note goes to the newsroom down the reader's own lane (the vault pane's Send), and with card 090 it carries
`signed: {signer, at, sig}`. `lane.py` checks each signed note against the register: the signature against the signer's
key, and the signer against the pinned root. A note from Dinis's browser is then marked "signed and checked: operated by
the root until <date>".

Two steps make it complete:

1. **The newsroom's own feedback lane.** An append lane the newsroom publishes, so a reader with no vault can still send
   a note (the brief "Feedback without a vault"). The register already has the statement for it: `inbox`, an append lane a
   record publishes. A record for the newsroom (an agent operated by Dinis) with an `inbox` makes the lane findable and the
   notes sealed to the newsroom's key.
2. **The authorize page** on pki.sgit.ai (option B), so the browser key is vouched for in one step.

## What card 090 builds

- `assets/pen/identity.js`: this browser's key (`generate`), its identity and `operated-by` statements, the submission,
  the key link, signing a note, and the check against the register from the pinned root (`readRecord`, `graph`,
  `trustFrom`), with pki.sgit.ai's `keys.js` and `directory.js` vendored unedited in `assets/vendor/pki/v0.2.25/`.
- The Pen's Signed section: make the key, copy the submission, open the key on pki.sgit.ai, check the register.
- `admin/build/lane.py`: every signed note in a lane checked against the register.

## What is left

- For pki.sgit.ai: take the submission (a reviewed commit, as now); later, `/authorize/` (B) and an `operates` link made
  by scanning a QR code (D).
- For the newsroom: keep the browser key in the reader vault's master; publish the newsroom's own feedback lane as an
  `inbox`; the agent's daily pass reading signed notes first (the editor's channel).
