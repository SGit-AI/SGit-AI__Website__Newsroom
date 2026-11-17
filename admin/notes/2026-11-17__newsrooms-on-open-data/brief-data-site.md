# Brief: the PrompTugal data site, and focused newsrooms on top

From writer-09 (newsroom.sgit.ai), written at Dinis Cruz's request, 17 November 2026, from his dictated brief. For conductor@PrompTugal.dinis. Decisions marked [Dinis] are his.

## Why
When Dinis shows PrompTugal.news, people like the live data most: weather, fire risk, flights, each value with its provenance. The data is valuable and spread across PrompTugal__News__Website, PrompTugal__News__Storm-Charles and others. Consolidate it, then build focused newsrooms on it. Public article: https://newsroom.sgit.ai/articles/newsrooms-on-open-data.html (once live).

## 1. Check observability first (today)
Dinis wants visits collected on every site and a daily debrief. Inventory says: obs.js still appends encrypted views and reads to the private vault, but observability's drain and debrief schedule in board/schedule.json is "disabled" since 16 Nov, and no daily traffic report exists. Please: confirm collection is still happening on promptugal.news, storm-charles.promptugal.news, the fringe site and the place pages; re-enable the drain; produce one daily debrief (visits and reads per site and per page, top countries and cities, referrers if captured), sealed to Dinis as now. Note: the newsroom.sgit.ai site has no visitor analytics at all; tell writer-09 if you want the same obs.js there [Dinis].

## 2. A data repository and site
- New repo and site, name [Dinis]: suggestion "PrompTugal Data", data.promptugal.news, repo PrompTugal/PrompTugal__Data.
- Public sources only. One folder and one vault per source. Start with what runs today:
  IPMA warnings, station observations, city daily forecasts, fire risk (rcm d0-d2), UV, sea forecast (all api.ipma.pt/open-data); adsb.lol flights around LPFR; MeteoAlarm CAP for Portugal; Wikipedia pinned revisions; the 34 Storm Charles datasets (as an archive with hashes); the place files' public sources.
- For each source:
  1. collector as code (move board/tools/local-now.mjs and storm's ipma-read.mjs, flights-poll, transport-* here; keep politeness: 2-3 s between requests, backoff);
  2. vault, versioned, public read key where the source is public;
  3. OpenAPI 3.1 + Swagger page (reuse newsroom/build/features/openapi.mjs);
  4. provenance on every value: source, page, read_at, by (keep the existing fields);
  5. a card: owner agent, schedule, licence/terms of the source (check reuse terms; public is not always free to republish), and the split below.
- PrompTugal.news and the place pages then consume the data site's APIs instead of their own copies.

## 3. Code vs agents vs people, and tokens
Per dataset and per page made from it, record: runs by code (no model), runs by agents (which, which model), checks by a person; tokens and API-equivalent dollars (from accountant@'s ledger). Show it on each card. This is the "steering/background" provenance idea applied to data, and the commercial point: if it is mostly code, it is nearly free to run.

## 4. Focused newsrooms (after the data site exists)
Sub-brands, each on its own address under promptugal.news [Dinis: names, domains], each run by a small agentic team, each a possible company. First candidates:
- Agriculture: weather, fire risk, UV, drought, municipal news; farmers, co-ops, insurers.
- Investors: companies, funding, records, ECB rates; investors and founders.
- The sea: sea forecast, ports, weather.
- Fire and civil protection: the storm site made permanent.
- Tourism and travel: flights, weather, sea, events, transport.
- AI: GAMMA-Ray ratings and the field's news.
Each publishes with the provenance model (type, five axes, ladder) and the meter (sg-meter v1.5.0, already in data/billing/prices.json).

## 5. Related, published today on newsroom.sgit.ai
paid-by-the-read (monetisation: meter, revenue share for newsrooms PrompTugal carries, associations UK/PT/EU); any-data-with-any-data (connecting datasets across entities, sold as cells); who-steered-this (steering and background). Quote or adapt freely, CC BY 4.0.

## Questions for Dinis
1. Name and domain of the data site.
2. Which focused newsroom first.
3. Observability on newsroom.sgit.ai too?
