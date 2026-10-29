# 05: Checklist

For the site team:

- [ ] `sgit pull` the evidence vault, and re-run `admin/build/export_vault.py`. Expect 184 or more sources.
- [ ] Fill `publisher` and `published` for the 40 recovered rows as you read each page. Retry the ones marked `failed`.
- [ ] Publish `/status.json` (`02__status-json.md`) from the build, deterministic, under the gate.
- [ ] From this pack's folder, run `python3 track.py --sources data/sources.json --out /tmp/transition.json`
      against your live site. Checks 1 to 4 should pass.
- [ ] Add the two rules in `03` to the vault's `README.md`.
- [ ] Point your README's link at the article once the section is retired.

For the newsroom:

- [x] Front-page strip linking to the site (v0.13.41).
- [x] Tracker `php-flaws/build/track.py`, and the panel on `/php-flaws/` (v0.13.41).
- [x] The article `capture-first` (v0.13.41).
- [ ] Read `/status.json` in the strip and the tracker once it exists.
- [ ] Retire `/php-flaws/` into a pointer when checks 1 to 4 pass and Dinis confirms (card 088).
