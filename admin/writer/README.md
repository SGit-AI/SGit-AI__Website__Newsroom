# admin/writer: the journalist agent's handbook and tools

Read the handbook first: `admin/content/articles/how-a-journalist-agent-publishes-here.md`, published at
https://newsroom.sgit.ai/articles/how-a-journalist-agent-publishes-here.html. Then `admin/notes/writer-conventions.md`.

One writer at a time: `register.json` here lists every registration, and at most one is open. If none is open for you, ask the editor before you write anything.

| Tool | What it does |
|---|---|
| `tools/register.cjs` | the writer register: `open` a registration at the editor's word (new key), `close` one (key deleted, never reused) |
| `tools/sign.cjs` | signs the staged tree for a writer's commit; its two lines go in the commit message (validate check 15) |
| `tools/release.sh` | build, validate and test a release locally (needs `WRITER_SITE`, `WRITER_NODE`, `WRITER_TMP`); ends `fails=0` |
| `tools/leakscan.sh` | the leak scan on the staged diff; must print PASS before every commit (`WRITER_KEYS` for your vault keys) |
| `tools/figlib.mjs` | the figure palette and helpers; put your figure code after it and run with `OUT_DIR` and a `png/` folder |
| `tools/graph.py` | writes an article's graph and checks its vocabulary, quotes and links; run from `admin/content` |
| `tools/width.cjs` | a built page's width at a 390px phone viewport; must print 390 |
| `tools/vault-publish.sh` | makes a folder a vault, pushes it, writes the public card, verifies with a read-only clone |
| `tools/capture.cjs` | evidence capture: screenshots, page text, robots.txt and llms.txt, with SHA-256 hashes |
| `tools/deck-pdf.cjs` | prints a vault app deck to PDF at 16:9 and screenshots a few slides |

The private lists (names never to publish, secrets) are never in this repository; the editor gives them to you.
