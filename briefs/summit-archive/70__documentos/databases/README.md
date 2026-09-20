# Databases with no server

Two real database engines running in the reader's browser, compiled to WebAssembly, over the JSON
files the Portugal section is built from. No server, no upload, no store of record.

| Page | What |
|---|---|
| `index.html` | The argument: the file system is the database; the engines are readers |
| `sql.html` | SQLite via sql.js — 15 tables built on load from `data/tables.json`, 16 worked queries |
| `graph.html` | Oxigraph (SPARQL 1.1) over `/portugal/data/triples.nt` (4,001 triples), 13 worked queries with Cypher shown beside each |

## Build

```
python3 portugal/build/graph.py     # writes triples.nt alongside graph.json
python3 databases/build/build.py    # writes data/*.json and the three pages; RUNS every worked query
python3 admin/build/chrome.py
node admin/build/validate.js
```

The build is the test. Every SQL example is executed with Python's `sqlite3` against tables built from
the same spec the browser uses (`assets/nsdb-sql.js` and `build.py` share `tables.json`); every SPARQL
example is executed with `pyoxigraph` (`pip install pyoxigraph`) over the same `triples.nt`. A query
that fails or returns nothing fails the build. The count each returned is written into
`data/queries-*.json` and printed beside the query on the page.

## Vendored engines

| Path | Component | Licence |
|---|---|---|
| `assets/vendor/sql-wasm.js`, `sql-wasm.wasm` | sql.js 1.14.2 (SQLite) | MIT |
| `assets/vendor/oxigraph/web.js`, `web_bg.wasm` | oxigraph 0.5.11, web build | MIT OR Apache-2.0 |

Cypher is shown, not run: Kùzu's WebAssembly build would run it and is 73 MB unpacked.

## Agent surface

Both consoles publish `window.__tools.sql` / `window.__tools.sparql` after a `tool:ready` event,
read-only. See the agent block at the foot of each page.
