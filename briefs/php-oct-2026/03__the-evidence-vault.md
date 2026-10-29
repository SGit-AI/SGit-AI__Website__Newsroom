# 03: The evidence vault, and what the morning taught us

## State at 12:30 UTC

The vault is private and encrypted (sgit), and was opened at 08:03 UTC. Its protocol is in the vault's
own `README.md`. At 12:05 UTC it held **184 sources, 177 dated captures and 855 files hashed at capture**,
from six writers:

| Writer | Sources |
|---|---|
| claude-story-site (your agent) | 83 |
| collector-gov | 37 |
| collector-news | 31 |
| collector-primary | 17 |
| collector-researchers | 14 |
| claude-newsroom-lead | 2 |

Your published data says 144 sources at vault commit `200d08971937`. The difference is 40 sources
that were **recovered after your export**: see below. Pull the vault and re-run
`admin/build/export_vault.py`.

## The 40 sources you do not have yet

Two collecting agents stopped before committing. The newsroom's lead agent found their working folders at
about 12:00 UTC, committed the captures, and pushed them. Each row's `notes` says that it was written by
the lead agent from the capture's `provenance.json`. In those rows the `publisher` is the host name and
`published` is null, because the page has not been read for its date yet. Please fill those in as you
take them over.

They include the most time-sensitive captures in the vault. Two French prefectures (Nord and Rhône) show
"Site en maintenance" at 08:19 UTC, the University of Geneva returns 503 at 08:19, and Edinburgh
council's home page loads normally at the same minute. They also include coverage from Switzerland,
France, Portugal, Germany, Australia, Canada and the US. The full list is
`data/missing-from-site.json`. Several captures in this set failed (the browser closed, or a certificate
error on `latvija.gov.lv`). Their rows say `failed`, and they are worth retrying.

## Two rules to add to the vault protocol

1. **Commit after every source, not at the end of a beat.** An agent's working folder is not the vault.
2. **Before saying the vault is complete, check every clone**: `sgit status` in each working folder,
   uncommitted files included, not only your own.

Also: if `sgit pull` reports many conflicts after two agents captured the same thing, compare the
bytes before choosing a side. At 12:00, 223 of 224 conflicts were identical on both sides. The only
real difference was `sources/index.json`, which is generated: rebuild it with `tools/index.py` and
don't merge it.

## The NCSC-NL inventory

`sources/ncsc-nl-php2shell/raw/` holds the whole repository as a git bundle (52 commits, HEAD
`cca173c64ec5`), the tree at that commit, the commit log, and the inventory parsed to JSON: 674 rows,
206 Vulnerable, 46 Fix, 418 Investigation, 3 Not vuln and 1 with no status. The inventory changes with
every pull request. Each re-count needs a new bundle and the commit it was counted at.
