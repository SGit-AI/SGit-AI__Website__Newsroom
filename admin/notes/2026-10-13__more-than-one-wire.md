# More than one wire: one code, one contract, one config and one vault each

*13 October 2026, built in newsroom.sgit.ai v0.12.14. Status: a beta with one named reader. It extends [the Industry Wire](../../wire/index.html) and [the wire as an inbox](2026-10-13__the-wire-as-an-inbox.md) to two more vaults the research agent built on the same pipeline: [the OWASP Wire](../../wire/owasp/index.html) and [the AWS Wire](../../wire/aws/index.html). The card is 040 on [the engineering board](../../engineering/index.html).*

## In short

- **A wire is a vault plus a config.** `admin/build/wire-vault.json` is the Industry Wire at `/wire/`; `wire-vault.<slug>.json` is another wire at `/wire/<slug>/`. The config holds the endpoint, the vault id, the public read key, the clone command, the wire's name, a paragraph of what it is, and the named readers with the date and the way they agreed. Nothing else on this site knows a wire by name: `wire.py` writes every wire's three pages and snapshot, `wire.js` draws every wire, `test_wire.mjs` tests every wire, and the search indexes every snapshot.
- **The contract is the same, and a vault may say more.** Every vault gives `data/bundle.json`, `data/deliveries.json`, `data/releases.json` and `docs/*.md` as [how the wire works](../../wire/how.html) says. A vault that describes itself in `wire` (id, title, cadence, beats, the personal persona) gets its lenses from its own personas, all but the personal one, plus the named readers in the config; without it the page offers the Industry Wire's six. A `map` or a `stack` is drawn when it is there and nothing breaks when it is not.
- **The named reader's agreement is per wire.** Each config records it. The agreement of 12 October covered the Industry Wire; on 13 October the owner extended it to the two new wires in chat, and each config says so with the date.
- **Each wire is its own inbox.** The notes already keep the page's path, so a decision at `/wire/owasp/ow-09` is not one at `/wire/ai-09`. The stories seen, the visit and the lens now take a scope too: the Industry Wire's are stored as before, a scoped wire's seen ids as `slug:id`, its visit and lens beside the Industry Wire's. The device file carries the seen ids as stored, so another device tells them apart.

## What a vault adds beyond the edition

**A map** (`data/map.json`, the OWASP projects graph): `title`, `intro`, and `entities`, each with `id`, `name`, `kind`, `aliases`, `facts` (a flat object of label to value; an http value becomes a link), `leaders`, `standards` and `notes`. The page draws it as a folded section under the bar: each entity with its facts, leaders and standards, and the stories whose own `entities` values match the entity's name or an alias, case-insensitively. That match is the only thing the page computes; the vault's app does the same. Twenty projects, twelve named by a story in the first edition.

**A stack** (`data/stack.json`, the AWS services a reader runs): `persona`, `what`, `services` (each `id`, `name`, `aliases`, `runtime`, `watch`), `extra_concerns`, `deadlines` (each `what`, `date`, `then`, `source`) and `later`. The join in the vault turns each service into a concern of the stack's persona, so the deliveries already say which items touched which service: a reached delivery to that persona whose connections name the service's id. The page draws the deadlines in the edition's header, soonest first, with the days left and red inside thirty days, and each service as a folded entry with the items that touched it. To change what reaches the reader, the desk edits the file in the vault; nothing on this site changes.

## What is not built

- **A page of the wires.** The strip at the top of each edition names them all; `/wire/` is still the Industry Wire, not an index.
- **One inbox across wires.** Each wire's bar counts its own; nothing adds them up. The Vault button's count does, since it counts notes and stories seen wherever they were kept.
- **The runs.** None of the three runbooks is scheduled; the desks publish when asked.
- **The AWS stack from an account.** The vault's `later` says it: derive the file from what the account runs, with the declared list as an override. Today it is a file the desk seeded.

## The names

The agent that keeps these pages, reading vaults and drawing them on this site, is the newsroom's side of the wire; the owner proposed calling it `@newsroom.wire`. The agent that writes a vault is what its runbook calls it, the wire's desk: the Industry Wire desk, the OWASP Wire desk, the AWS Wire desk. One reads, the others write, and the read key is the only thing they share.
