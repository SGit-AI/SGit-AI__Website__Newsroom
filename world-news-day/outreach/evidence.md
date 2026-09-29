# Verifying anything in here

Every claim in this vault traces to the corpus vault or to a published page. Neither asks to
be taken on trust.

## The corpus vault

A separate, finished vault holding the twenty-one op-eds as frozen bytes, every derived
dataset, the build code and the gate. Its **public read key** is published at
https://newsroom.sgit.ai/world-news-day/vault.html — a read key grants read and only read.

The same contents are downloadable without any tooling:

    curl -O https://newsroom.sgit.ai/world-news-day/vault.zip
    shasum -a 256 vault.zip        # 4771646e9d274f0daf242608aa37fe716c35450f92b0a8d3539efeab73a7a9c0
    unzip vault.zip -d wnd && cd wnd
    python3 build/gates.py         # re-derives every published count from the frozen bytes

`MANIFEST.json` inside carries the SHA-256 of every file. The `stands_on` field of an action
should carry one of those hashes, or a URL under https://newsroom.sgit.ai/world-news-day/.

## The published pages

- https://newsroom.sgit.ai/world-news-day/licences.html — the licence finding, both wordings quoted verbatim
- https://newsroom.sgit.ai/world-news-day/corpus.html — the twenty-one described, linked, never reproduced
- https://newsroom.sgit.ai/world-news-day/findings.html — the aggregate, and how it maps to what we have argued
- https://newsroom.sgit.ai/world-news-day/contacts.html — the routes in `targets/`, and the rules that produced them
- https://newsroom.sgit.ai/world-news-day/method.html#corrections — what this section has already got wrong, and fixed

## If a number here and a number there disagree

The data files win, and the disagreement is a `corrected` action. Do not reconcile it by
editing this vault quietly.
