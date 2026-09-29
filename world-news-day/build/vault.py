#!/usr/bin/env python3
"""world-news-day/ — the vault bundle.

    python3 world-news-day/build/vault.py      (build.py runs it last)

Writes world-news-day/vault.zip: everything this section is built from and everything it
produces, in one file, laid out exactly as the sgit vault would be so that the same folder
can be pushed as one without being rearranged.

WHY A BUNDLE AND NOT A PUSHED VAULT. An sgit vault is created against an SG/Send server with
an access token. This build environment has neither, and the one thing a section about
licensing must not do is invent a credential or publish a key. So the bundle is built and
hashed here, PACKAGE.sh carries the exact commands that turn it into a vault, and the vault
page says plainly that no vault has been pushed yet. When one is, what gets published beside
it is the READ KEY — read keys are publishable, vault keys never are, and the whole-site gate
carries a tripwire for anything key-shaped.

WHAT IS IN IT, and under which terms — the distinction this whole section exists to make:

  · OUR description, counts, graph, lexicon, transcription and code: CC BY 4.0, named, with a
    version and a URL, and declared in machine-readable form in licence.json.
  · THEIR twenty-one op-eds, frozen as bytes: not ours, not relicensed, not reproduced as
    prose anywhere in our files. Included as evidence, under the terms the publisher stated,
    quoted verbatim in the bundle's own README.

That second bullet is a deliberate departure from the standing house rule that a delivered
vault carries no copies of third-party pages (briefs/13 §F). That rule is about a researcher
handing us a copy nobody asked them to make. Here the frozen copies ARE the evidence, they
are already public in this repository, they carry the publisher's own permission to
republish, and a bundle of claims without the bytes they rest on is the thing this
publication argues against. The reasoning is written into the bundle rather than left
implicit, so that whoever opens it can disagree with it.
"""
import hashlib
import json
import zipfile
from pathlib import Path

SEC = Path(__file__).resolve().parents[1]
DATA = SEC / "data"
OUT = SEC / "vault.zip"
VAULT_ID = "wnd-2026-09-29"


def load(n):
    return json.loads((DATA / n).read_text(encoding="utf-8"))


LICENCE_JSON = {
    "@context": "https://schema.org",
    "@type": "Dataset",
    "name": "World News Day 2026: the corpus described",
    "description": "Twenty-one commissioned op-eds published for World News Day 2026, "
                   "fetched, frozen, hashed, described, classified by a published lexicon and "
                   "expressed as a typed graph. The description is ours; the op-eds are not.",
    "url": "https://newsroom.sgit.ai/world-news-day/",
    "version": VAULT_ID,
    "license": "https://creativecommons.org/licenses/by/4.0/",
    "copyrightHolder": {"@type": "Organization", "name": "newsroom.sgit.ai",
                        "url": "https://newsroom.sgit.ai"},
    "copyrightNotice": "CC BY 4.0 covers the description, the counts, the graph, the lexicon, "
                       "the transcription and the code in this bundle. It does NOT cover the "
                       "twenty-one op-eds under sources/frozen/, which are the work of their "
                       "authors, published at worldnewsday.org, and carried here as frozen "
                       "evidence under the terms their own pages state.",
    "usageInfo": "https://newsroom.sgit.ai/world-news-day/licences.html",
    "isAccessibleForFree": True,
    "creator": {"@type": "Organization", "name": "sgit agents",
                "description": "Researched, extracted and drafted by software agents against "
                               "frozen, hashed bytes. No human editor of record."},
    "distribution": [
        {"@type": "DataDownload", "encodingFormat": "application/zip",
         "contentUrl": "https://newsroom.sgit.ai/world-news-day/vault.zip"},
        {"@type": "DataDownload", "encodingFormat": "application/json",
         "contentUrl": "https://newsroom.sgit.ai/world-news-day/data/graph.json"},
        {"@type": "DataDownload", "encodingFormat": "application/n-triples",
         "contentUrl": "https://newsroom.sgit.ai/world-news-day/data/triples.nt"},
    ],
    "note": "This file is the one line we asked the publisher for, written out in full. "
            "schema.org has carried `license` since 2015; none of the twenty-one uses it.",
}

PACKAGE_SH = """#!/usr/bin/env bash
# Turn this folder into an sgit vault. Requires an SG/Send access token, which is why the
# newsroom could not run it: the build environment has no credential, and a section about
# licensing does not invent one.
#
#   pip3 install sgit-ai
#   export SGIT_TOKEN=...        # your SG/Send access token
#
set -euo pipefail
VAULT_ID="{vault_id}"

sgit init "$VAULT_ID" --token "$SGIT_TOKEN"    # PRINTS THE VAULT KEY. Keep it. It is write access.
cd "$VAULT_ID"
cp -R ../data ../sources ../build ../README.md ../MANIFEST.json ../licence.json .
sgit commit "world news day 2026: {count} files, {snapshot}"
sgit push
sgit history log --json

# Handing it over: publish the READ KEY, derived one-way from the vault key, and never the
# vault key itself. A read key grants read and only read:
#   python3 -c "from sgit_ai.vault.crypto import Vault__Crypto; \\
#     print(Vault__Crypto().derive_keys(VAULT_KEY, '$VAULT_ID')['read_key'])"
# Or hand over a one-shot share token instead:  sgit share
"""


def readme(register, corpus, licences, manifest_count):
    s = licences["the_statement"][0]["text"]
    return f"""# World News Day 2026 — the vault

{corpus['count']} commissioned op-eds, fetched once on {register['snapshots'][-1]}, frozen to
bytes, hashed, described, classified and graphed. Everything the published section stands on,
in one file.

Built by newsroom.sgit.ai. The live section: https://newsroom.sgit.ai/world-news-day/

## Two sets of terms, and they are not the same

**Ours** — everything under `data/` and `build/`, and this file: **CC BY 4.0**
(https://creativecommons.org/licenses/by/4.0/). Named, versioned, with a URL, and declared in
machine-readable form in `licence.json`. That is deliberate: this section's finding is that the
corpus it describes has no such declaration, and it would be cheap to say so without doing it.

**Theirs** — everything under `sources/frozen/`: the twenty-one op-eds as served, and the
records the publisher's own REST API returns for them. **Not ours, not relicensed, and not
reproduced as prose anywhere in our files.** Each piece carries this sentence, and it is the
only statement of terms anywhere on it:

> {s}

A second wording appears on one of the {corpus['count']}, and the announcement page states the
terms a third way. What that does and does not permit is set out in `data/licences.json` and at
https://newsroom.sgit.ai/world-news-day/licences.html. **If you are deciding whether you may
republish one of these pieces, read the terms on the piece and ask the publisher.** Nothing here
is legal advice, and nothing here grants you anything over somebody else's work.

## Layout

```
README.md              this file
licence.json           our terms, in the schema.org field the corpus leaves empty
MANIFEST.json          every file in the bundle with its size and SHA-256
PACKAGE.sh             the commands that turn this folder into an sgit vault
data/
  register.json        every frozen file, its URL, retrieval time, size and SHA-256,
                       and the one page that could not be fetched, with the reason
  corpus.json          the {corpus['count']} described — and never their prose
  licences.json        the licence finding, counted
  affiliations.json    where each author works, transcribed from their own role line
  analysis.json        the aggregate: themes, co-occurrence, the evidence count
  lexicon.json         the {len(load('lexicon.json')['entries'])} published theme patterns — the only classification here
  ontology.json        types and verbs, each with a named inverse and a Portuguese form
  graph.json           the graph
  triples.nt           the same graph as N-Triples, owl:inverseOf on every verb
build/                 the code that produced all of it, including the gate that checks it
sources/frozen/{register['snapshots'][-1]}/
  <slug>.snapshot      the page as served
  api/<slug>.json      the record the publisher's REST API returns
```

## Checking it

Nothing here asks to be taken on trust.

```bash
python3 - <<'EOF'
import hashlib, json
m = json.load(open("MANIFEST.json"))
bad = [f["path"] for f in m["files"]
       if hashlib.sha256(open(f["path"], "rb").read()).hexdigest() != f["sha256"]]
print("files:", m["count"], "| mismatched:", bad or "none")
EOF

python3 build/gates.py     # re-derives every published count from the frozen bytes
```

`build/gates.py` is the executable specification: it re-hashes every frozen file, re-derives
every licence count with a second implementation, re-runs every theme pattern on the frozen
prose in both directions, checks every transcribed affiliation against the bytes it claims to
come from, and fails if twelve consecutive words of any op-ed appear on a page we generate.

## What is NOT here

- **The prose of the op-eds, as text in any file we wrote.** It is in the frozen pages, because
  those are the evidence; it is in none of our JSON. Read the pieces at worldnewsday.org.
- **Any contact detail for any named person.** Refused where the data is parsed, not hidden
  where it is rendered.
- **Any assessment of anybody.** No sentiment, no stance, no scoring, no claim that any author
  agrees with any other. `agrees_with` is a banned verb in the ontology.
- **The announcement page.** wan-ifra.org answered an automated reader with HTTP 307 and no
  body, from two user-agents, while rendering normally for a browser. `data/register.json`
  records the refusal rather than hiding it.

{manifest_count} files in the bundle, frozen {register["snapshots"][-1]}. The bundle is
built deterministically: the same frozen bytes produce the same zip, hash for hash.
"""


def main():
    register, corpus, licences = load("register.json"), load("corpus.json"), load("licences.json")
    files = []
    for p in sorted(DATA.glob("*.json")) + sorted(DATA.glob("*.nt")):
        # data/manifest.json is the section's file list; inside the bundle that job belongs to
        # MANIFEST.json, which covers the bundle's own contents. Two lists that disagree is
        # worse than one, and this one would: the bundle is built before the section's manifest.
        # ...and data/vault.json is the record OF this bundle, carrying its hash. Putting it
        # inside would make the hash depend on itself: the bundle would never settle, and two
        # builds from identical bytes would differ. It was circular until it was caught here.
        if p.name in ("manifest.json", "vault.json"):
            continue
        files.append(("data/" + p.name, p))
    for p in sorted((SEC / "build").glob("*.py")):
        files.append(("build/" + p.name, p))
    for p in sorted((SEC / "sources" / "frozen").rglob("*")):
        if p.is_file():
            files.append((p.relative_to(SEC).as_posix(), p))

    entries = [{"path": rel, "bytes": src.stat().st_size,
                "sha256": hashlib.sha256(src.read_bytes()).hexdigest()} for rel, src in files]
    lic = json.dumps(LICENCE_JSON, indent=2, ensure_ascii=False) + "\n"
    pkg = PACKAGE_SH.format(vault_id=VAULT_ID, count=len(entries) + 4,
                            snapshot=register["snapshots"][-1])
    rdm = readme(register, corpus, licences, len(entries) + 4)
    for name, text in (("README.md", rdm), ("licence.json", lic), ("PACKAGE.sh", pkg)):
        entries.append({"path": name, "bytes": len(text.encode()),
                        "sha256": hashlib.sha256(text.encode()).hexdigest()})
    man = json.dumps({
        "id": "wnd-vault", "vault_id": VAULT_ID,
        "snapshot": register["snapshots"][-1],
        "note": "Every file in this bundle with its SHA-256. MANIFEST.json itself is absent: a "
                "file cannot carry its own hash.",
        "licence": {"ours": "https://creativecommons.org/licenses/by/4.0/",
                    "covers": "data/, build/, README.md, licence.json",
                    "theirs": "sources/frozen/ — the publishers' work, under the terms their "
                              "own pages state, quoted in README.md; not relicensed here"},
        "count": len(entries), "files": entries}, indent=2, ensure_ascii=False) + "\n"

    # Deterministic: the same frozen bytes must produce the same bundle, hash for hash, or the
    # SHA-256 published beside it is a build timestamp wearing a hash's clothes. Every entry
    # carries the snapshot date rather than the moment the build ran, and mtimes are not read.
    stamp = tuple(int(x) for x in register["snapshots"][-1].split("-")) + (0, 0, 0)

    def add(z, name, data):
        info = zipfile.ZipInfo(name, date_time=stamp)
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o644 << 16
        z.writestr(info, data)

    with zipfile.ZipFile(OUT, "w") as z:
        for rel, src in files:
            add(z, rel, src.read_bytes())
        add(z, "README.md", rdm)
        add(z, "licence.json", lic)
        add(z, "PACKAGE.sh", pkg)
        add(z, "MANIFEST.json", man)

    digest = hashlib.sha256(OUT.read_bytes()).hexdigest()
    (DATA / "vault.json").write_text(json.dumps({
        "id": "wnd-vault-record", "vault_id": VAULT_ID, "snapshot": register["snapshots"][-1],
        "bundle": "vault.zip", "bytes": OUT.stat().st_size, "sha256": digest,
        "count": len(entries) + 1,
        "pushed": False,
        "why_not_pushed": "An sgit vault is created against an SG/Send server with an access "
                          "token. This build environment has neither, and a section about "
                          "licensing does not invent a credential or publish a key. PACKAGE.sh "
                          "inside the bundle carries the exact commands; when a vault is "
                          "pushed, the READ KEY goes here — never the vault key.",
        "read_key": None,
        "licence": LICENCE_JSON,
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"vault: {len(entries) + 1} files, {OUT.stat().st_size / 1_048_576:.2f} MB, "
          f"sha256 {digest[:16]}…")
    return digest


if __name__ == "__main__":
    main()
