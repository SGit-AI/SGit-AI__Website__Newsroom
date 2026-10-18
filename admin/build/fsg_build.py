#!/usr/bin/env python3
"""The derivation of the graph of meaning: the join, the gravity, the clusters, the cut, the peaks, the scores.

Imported by admin/build/fsg.py (which is the command); nothing here is run on its own. Everything is deterministic:
the same files give the same layers, so a difference between two runs is a difference in the files. The only numeric
dependency is numpy (the spectral cut, the layout and the 3D embedding); the clustering is a small Louvain written
here so the build needs nothing else installed.

What it writes:
  admin/content/graphs/registry/*.json         new ids folded in, duplicates merged (the old id kept as an alias)
  admin/content/graphs/articles/<slug>.json    rewritten only when a merge changed an id, or to clear new: true
  admin/content/graphs/runs/<date>-merge.json  the merge log
  graphs/data/*.json                           the layers as data (see write_data), and report.json
  graphs/**.html                               the pages (fsg_pages.py)
"""
import datetime
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlparse

import numpy as np

import fsg
from fsg import ROOT, SRC, ART_SRC, REG, OUT, VERBS, load, registry, article_files, check_file, norm

TODAY = datetime.date.today().isoformat()
RUN = "2026-10-18"
GRAVITY = 2          # a name or concept in this many articles has gravity (the wire's rule)
SEED = 7


# ---------------------------------------------------------------- loading


def load_all(tolerant=False):
    """Every valid article file. With tolerant, a file that fails the check is skipped and named, so a report can run
    while files are still being written; the build itself never tolerates an error."""
    cid, eid = registry()
    gs, errs, skipped = {}, [], []
    for f in article_files():
        e, _ = check_file(f, cid, eid, verbose=False)
        if e:
            if tolerant:
                skipped.append(f.stem)
                continue
            errs += e
            continue
        gs[f.stem] = load(f)
    if skipped:
        print(f"fsg: report skips {len(skipped)} file(s) that do not pass yet: {', '.join(skipped)}")
    return gs, errs


def article_meta():
    """Title, date, topics, tags, links out, desk, controlled tags, series, format, section streams, personas: the editor's
    layers and the article's own metadata, from the files the site already maintains."""
    gj = load(ROOT / "articles/graphs.json")
    find = load(ROOT / "articles/find.json")
    meta = {}
    for a in gj["articles"]:
        f = find["articles"].get(a["slug"], {})
        meta[a["slug"]] = {
            "slug": a["slug"], "title": a["title"], "date": a["date"], "topics": a.get("topics", []),
            "tags": a.get("tags", []), "links_out": a.get("links_out", []), "teaser": a.get("teaser", ""),
            "desk": f.get("desk"), "desk2": f.get("desk2"), "subjects": f.get("tags") or [],
            "series": [s.get("id") if isinstance(s, dict) else s for s in (f.get("series") or [])],
            "format": f.get("format"), "words": f.get("words"), "sections": [], "personas": [],
        }
    secdir = ROOT / "sections"
    for p in sorted(secdir.glob("*.json")) if secdir.exists() else []:
        s = load(p)
        if "streams" not in s:
            continue
        for st in s["streams"]:
            for a in st.get("articles", []):
                slug = a.get("slug") if isinstance(a, dict) else a
                if slug in meta:
                    meta[slug]["sections"].append(f"{s['id']}/{st['id']}")
    pl = ROOT / "persona/links.json"
    if pl.exists():
        p = load(pl)
        for per in p.get("personas", []):
            pid = per.get("id")
            for a in per.get("starts_from", []):
                slug = a.get("slug") if isinstance(a, dict) else a
                if isinstance(slug, str):
                    slug = slug.rsplit("/", 1)[-1].replace(".html", "")
                if slug in meta and pid:
                    meta[slug]["personas"].append(pid)
    desks = {d["id"]: d for d in find["desks"]}
    topics = {t["id"]: t for t in gj["topics"]}
    return meta, desks, topics, find


# ---------------------------------------------------------------- merge


_STOP = ("the ", "a ", "an ")


def key(s):
    s = norm(str(s)).lower().replace("-", " ").replace("_", " ")
    s = re.sub(r"[^a-z0-9 ]", "", s)
    for st in _STOP:
        if s.startswith(st):
            s = s[len(st):]
    s = re.sub(r"\s+", " ", s).strip()
    if s.endswith("ies"):
        s = s[:-3] + "y"
    elif s.endswith("s") and not s.endswith("ss"):
        s = s[:-1]
    return s


def merge(gs):
    """Fold new ids into the registries; merge a new id that names a registry entry (by id, label or alias) into it,
    keeping the new id as an alias; rewrite the article files so they carry the registry ids and no new: true."""
    cj, ej = load(REG / "concepts.json"), load(REG / "entities.json")
    log = {"run": RUN, "date": TODAY, "concepts": {"added": [], "merged": []}, "entities": {"added": [], "merged": []}}

    def index(items, labelkey):
        idx = {}
        for it in items:
            idx.setdefault(key(it["id"]), it["id"])
            idx.setdefault(key(it[labelkey]), it["id"])
            for al in it.get("aliases", []):
                idx.setdefault(key(al), it["id"])
        return idx

    def fold(kind, items, labelkey, newkey, extra):
        idx = index(items, labelkey)
        byid = {it["id"]: it for it in items}
        remap = {}
        proposals = defaultdict(list)       # new id -> [(slug, record)]
        for slug, g in gs.items():
            for x in g.get(kind, []):
                if x.get("new") and x["id"] not in byid:
                    proposals[x["id"]].append((slug, x))
        for nid, recs in sorted(proposals.items()):
            rec = recs[0][1]
            label = rec.get(labelkey) or rec.get(newkey) or nid
            hit = idx.get(key(nid)) or idx.get(key(label))
            if hit and hit != nid:
                remap[nid] = hit
                tgt = byid[hit]
                for al in {label, nid}:
                    if key(al) != key(tgt[labelkey]) and al not in tgt.get("aliases", []):
                        tgt.setdefault("aliases", []).append(al)
                log[kind]["merged"].append({"from": nid, "into": hit, "label": label, "in": sorted({s for s, _ in recs})})
            else:
                entry = {"id": nid, labelkey: label}
                entry.update(extra(rec))
                entry["aliases"] = sorted({r.get(labelkey) or label for _, r in recs} - {label})
                entry["from"] = f"run {RUN}"
                entry["first_seen"] = sorted({s for s, _ in recs})
                items.append(entry)
                byid[nid] = entry
                idx[key(nid)] = nid
                idx[key(label)] = nid
                log[kind]["added"].append({"id": nid, "label": label, "in": entry["first_seen"]})
        return remap

    cremap = fold("concepts", cj["concepts"], "label", "label",
                  lambda r: {"means": r.get("means", "")})
    eremap = fold("entities", ej["entities"], "name", "name",
                  lambda r: {"type": r.get("type", "organisation")})
    # Also: two files proposing different new ids for the same label. The fold above handles it in order
    # (the second finds the first in the index), so a remap can chain; resolve chains.
    def resolve(m, i):
        seen = set()
        while i in m and i not in seen:
            seen.add(i); i = m[i]
        return i

    changed = 0
    for slug, g in gs.items():
        dirty = False
        for kind, m in (("concepts", cremap), ("entities", eremap)):
            seen = {}
            out = []
            for x in g.get(kind, []):
                nid = resolve(m, x["id"])
                if nid != x["id"] or x.get("new"):
                    dirty = True
                x = dict(x); x["id"] = nid; x.pop("new", None)
                for k in ("name", "type", "label", "means"):
                    x.pop(k, None)
                if nid in seen:            # two aliases of one thing in one file: keep the first role
                    continue
                seen[nid] = x; out.append(x)
            g[kind] = out
        for c in g.get("claims", []):
            ab = []
            for a in c.get("about", []):
                k, i = a.split(":", 1)
                ni = resolve(cremap if k == "concept" else eremap, i)
                if ni != i:
                    dirty = True
                if f"{k}:{ni}" not in ab:
                    ab.append(f"{k}:{ni}")
            c["about"] = ab
        if dirty:
            (ART_SRC / f"{slug}.json").write_text(json.dumps(g, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
            changed += 1
    cj["concepts"].sort(key=lambda x: x["id"]); ej["entities"].sort(key=lambda x: x["id"])
    (REG / "concepts.json").write_text(json.dumps(cj, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    (REG / "entities.json").write_text(json.dumps(ej, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    log["files_rewritten"] = changed
    (SRC / "runs").mkdir(exist_ok=True)
    logp = SRC / "runs" / f"{TODAY}-merge.json"
    if logp.exists():            # a second build the same day adds to the day's log rather than replacing it
        old = load(logp)
        for k, v in old.items():          # keep whatever the day's log already holds (a note, a count)
            if k not in ("concepts", "entities", "files_rewritten"):
                log[k] = v
        for kind in ("concepts", "entities"):
            for k, v in old[kind].items():
                if k not in ("added", "merged"):
                    log[kind][k] = v
            seen = {x["id"] for x in log[kind]["added"]}
            log[kind]["added"] = old[kind]["added"] + [x for x in log[kind]["added"] if x["id"] not in seen]
            log[kind]["merged"] = old[kind]["merged"] + log[kind]["merged"]
        log["files_rewritten"] = old.get("files_rewritten", 0) + changed
    # the added lists are also recoverable from the registries, which stamp every entry a run added
    for kind, items, lk in (("concepts", cj["concepts"], "label"), ("entities", ej["entities"], "name")):
        have = {x["id"] for x in log[kind]["added"]}
        for it in items:
            if it.get("from") == f"run {RUN}" and it["id"] not in have:
                log[kind]["added"].append({"id": it["id"], "label": it[lk], "in": it.get("first_seen", [])})
    logp.write_text(json.dumps(log, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return log


# ---------------------------------------------------------------- the join


def join(gs, meta):
    """Nodes and typed edges across the whole newsroom. Edges carry the verb and its inverse."""
    cid, eid = registry()
    nodes = {}      # id -> {kind, label, ...}
    edges = []      # (from, verb, inverse, to)

    def add(nid, **kw):
        nodes.setdefault(nid, {}).update(kw)

    def edge(a, verb, b):
        inv = VERBS.get(verb) or fsg.DERIVED_VERBS.get(verb)
        edges.append((a, verb, inv, b))

    for slug, g in gs.items():
        m = meta.get(slug, {"title": slug, "date": ""})
        aid = f"article:{slug}"
        add(aid, kind="article", label=m["title"], date=m["date"], slug=slug)
        for cl in g["claims"]:
            qid = f"claim:{slug}:{cl['id']}"
            add(qid, kind="claim", claim_kind=cl["kind"], label=cl["text"], section=cl["section"], quote=cl["quote"],
                value=cl.get("value"), slug=slug, date=m["date"])
            edge(aid, "states", qid)
            for a in cl.get("about", []):
                k, i = a.split(":", 1)
                edge(qid, "uses" if k == "concept" else "names", f"{k}:{i}")
            for r in cl.get("refs", []):
                ref = next((x for x in g.get("references", []) if x["id"] == r), None)
                if ref:
                    edge(qid, "cites", f"ref:{ref_key(ref['url'])}")
        for e in g.get("edges", []):
            edge(f"claim:{slug}:{e['from']}", e["verb"], f"claim:{slug}:{e['to']}")
        for x in g.get("concepts", []):
            c = cid.get(x["id"], {})
            add(f"concept:{x['id']}", kind="concept", label=c.get("label", x["id"]), means=c.get("means", ""))
            if x.get("defined_here"):
                edge(aid, "defines", f"concept:{x['id']}")
        for x in g.get("entities", []):
            e = eid.get(x["id"], {})
            add(f"entity:{x['id']}", kind="entity", label=e.get("name", x["id"]), type=e.get("type", ""))
        for r in g.get("references", []):
            rid = f"ref:{ref_key(r['url'])}"
            n = nodes.get(rid, {})
            add(rid, kind="reference", label=n.get("label") or r.get("title") or r["url"], url=r["url"],
                by=n.get("by") or r.get("by", ""), date=n.get("date") or r.get("date", "undated"), ref_kind=r.get("kind"),
                domain=urlparse(r["url"]).netloc.replace("www.", ""))
            edge(aid, "cites", rid)
        for d in g.get("dates", []):
            did = f"date:{d['date']}"
            add(did, kind="date", label=d["date"])
            edge(aid, "happened_on", did)
        for other in m.get("links_out", []):
            if other in gs:
                edge(aid, "builds_on", f"article:{other}")
        for t in m.get("topics", []):
            add(f"topic:{t}", kind="topic", label=t); edge(aid, "placed_in", f"topic:{t}")
        for d in (m.get("desk"), m.get("desk2")):
            if d:
                add(f"desk:{d}", kind="desk", label=d); edge(aid, "placed_in", f"desk:{d}")
        for s in m.get("subjects", []):
            add(f"subject:{s}", kind="subject", label=s); edge(aid, "placed_in", f"subject:{s}")
        for s in m.get("series", []):
            add(f"series:{s}", kind="series", label=s); edge(aid, "placed_in", f"series:{s}")
        for s in m.get("sections", []):
            add(f"section:{s}", kind="section", label=s); edge(aid, "placed_in", f"section:{s}")
        for p in m.get("personas", []):
            add(f"persona:{p}", kind="persona", label=p); edge(aid, "placed_in", f"persona:{p}")
    return nodes, edges


def ref_key(url):
    u = url.strip().rstrip("/")
    u = re.sub(r"^https?://(www\.)?", "", u)
    u = u.split("#")[0]
    return u.lower()


# ---------------------------------------------------------------- gravity, co-occurrence, clusters


def gravity(gs, meta):
    """For every concept and entity: the articles that use it, the claims about it, the desks and topics they sit on,
    and the first article (by date) that used it."""
    use = defaultdict(lambda: {"articles": set(), "claims": 0, "desks": Counter(), "topics": Counter(), "defined_in": []})
    for slug, g in gs.items():
        m = meta.get(slug, {})
        for cl in g["claims"]:
            for a in cl.get("about", []):
                u = use[a]
                u["articles"].add(slug); u["claims"] += 1
                if m.get("desk"):
                    u["desks"][m["desk"]] += 1
                for t in m.get("topics", []):
                    u["topics"][t] += 1
        for x in g.get("concepts", []):
            if x.get("defined_here"):
                use[f"concept:{x['id']}"]["defined_in"].append(slug)
    out = {}
    for nid, u in use.items():
        arts = sorted(u["articles"], key=lambda s: (meta.get(s, {}).get("date", ""), s))
        out[nid] = {"articles": arts, "n_articles": len(arts), "claims": u["claims"],
                    "desks": dict(u["desks"].most_common()), "topics": dict(u["topics"].most_common()),
                    "first": arts[0] if arts else None, "first_date": meta.get(arts[0], {}).get("date") if arts else None,
                    "defined_in": u["defined_in"]}
    return out


def cooccurrence(gs, grav, min_articles=GRAVITY):
    """Two weighted graphs between the concepts and names with gravity. C counts the articles two nodes share. W is
    C normalised by the geometric mean of the two nodes' article counts (a cosine), so that a node every article
    names (the owner, the voice memo) does not pull every cluster to itself: the clusters, the cut and the layout
    use W; the map's edge labels use C."""
    ids = sorted(i for i, g in grav.items() if g["n_articles"] >= min_articles)
    pos = {i: k for k, i in enumerate(ids)}
    C = np.zeros((len(ids), len(ids)))
    for slug, g in gs.items():
        present = sorted({a for cl in g["claims"] for a in cl.get("about", []) if a in pos})
        for i in range(len(present)):
            for j in range(i + 1, len(present)):
                a, b = pos[present[i]], pos[present[j]]
                C[a, b] += 1; C[b, a] += 1
    n = np.array([grav[i]["n_articles"] for i in ids], dtype=float)
    W = C / np.sqrt(np.outer(n, n))
    W[C < 2] = 0            # one shared article is coincidence, not a tie
    return ids, C, W


def louvain(W, seed=SEED, resolution=1.0):
    """A small Louvain: local moves until no gain, aggregate, repeat. Returns a community index per node."""
    rng = np.random.default_rng(seed)
    n = W.shape[0]
    membership = np.arange(n)
    Wc = W.copy()
    levels = []
    while True:
        m2 = Wc.sum()
        if m2 == 0:
            break
        k = Wc.sum(axis=1)
        comm = np.arange(Wc.shape[0])
        tot = k.copy()
        improved = True
        while improved:
            improved = False
            for i in rng.permutation(Wc.shape[0]):
                ci = comm[i]
                neigh = np.nonzero(Wc[i])[0]
                if len(neigh) == 0:
                    continue
                # weights to each neighbouring community
                wc = defaultdict(float)
                for j in neigh:
                    if j != i:
                        wc[comm[j]] += Wc[i, j]
                tot[ci] -= k[i]
                best, bestgain = ci, 0.0
                base = wc.get(ci, 0.0) - resolution * tot[ci] * k[i] / m2
                for c, w in wc.items():
                    gain = (w - resolution * tot[c] * k[i] / m2) - base
                    if gain > bestgain + 1e-12:
                        best, bestgain = c, gain
                tot[best] += k[i]
                if best != ci:
                    comm[i] = best; improved = True
        # relabel 0..c-1
        labels = {c: idx for idx, c in enumerate(sorted(set(comm)))}
        comm = np.array([labels[c] for c in comm])
        levels.append(comm)
        if len(labels) == Wc.shape[0]:
            break
        # aggregate
        C = len(labels)
        Wn = np.zeros((C, C))
        for a in range(Wc.shape[0]):
            for b in range(Wc.shape[0]):
                if Wc[a, b]:
                    Wn[comm[a], comm[b]] += Wc[a, b]
        Wc = Wn
    # compose levels
    out = np.arange(n)
    for lv in levels:
        out = lv[out]
    return out


def modularity(W, comm):
    m2 = W.sum()
    if m2 == 0:
        return 0.0
    k = W.sum(axis=1)
    q = 0.0
    for c in set(comm):
        idx = np.nonzero(comm == c)[0]
        q += W[np.ix_(idx, idx)].sum() / m2 - (k[idx].sum() / m2) ** 2
    return float(q)


def fiedler_cut(W):
    """Spectral bisection: the sign of the Fiedler vector of the normalised Laplacian on the largest component."""
    n = W.shape[0]
    d = W.sum(axis=1)
    keep = d > 0
    idx = np.nonzero(keep)[0]
    Wk = W[np.ix_(idx, idx)]
    dk = Wk.sum(axis=1)
    Dm = np.diag(1 / np.sqrt(dk))
    L = np.eye(len(idx)) - Dm @ Wk @ Dm
    vals, vecs = np.linalg.eigh(L)
    f = Dm @ vecs[:, 1]
    side = np.full(n, -1)
    side[idx] = (f > np.median(f)).astype(int)
    score = np.zeros(n); score[idx] = f
    return side, score


def layout2d(W, iters=400, seed=SEED):
    """Fruchterman-Reingold on the weighted graph, in the unit square."""
    rng = np.random.default_rng(seed)
    n = W.shape[0]
    if n == 0:
        return np.zeros((0, 2))
    pos = rng.random((n, 2))
    k = math.sqrt(1.0 / n)
    t = 0.1
    Wn = W / (W.max() or 1)
    for it in range(iters):
        delta = pos[:, None, :] - pos[None, :, :]
        dist = np.linalg.norm(delta, axis=2) + 1e-9
        rep = (k * k / dist ** 2)[:, :, None] * delta
        att = (dist * Wn / k)[:, :, None] * delta
        disp = rep.sum(axis=1) - att.sum(axis=1)
        ln = np.linalg.norm(disp, axis=1) + 1e-9
        pos += disp / ln[:, None] * np.minimum(ln, t)[:, None]
        pos = np.clip(pos, 0, 1)
        t *= 0.99
    lo, hi = pos.min(axis=0), pos.max(axis=0)
    return (pos - lo) / np.where(hi - lo == 0, 1, hi - lo)


def layout3d(W, iters=300, seed=SEED):
    """Fruchterman-Reingold in three dimensions, centred and scaled to unit variance per axis."""
    rng = np.random.default_rng(seed)
    n = W.shape[0]
    if n == 0:
        return np.zeros((0, 3))
    pos = rng.random((n, 3))
    k = (1.0 / n) ** (1 / 3)
    t = 0.1
    Wn = W / (W.max() or 1)
    for it in range(iters):
        delta = pos[:, None, :] - pos[None, :, :]
        dist = np.linalg.norm(delta, axis=2) + 1e-9
        rep = (k * k / dist ** 2)[:, :, None] * delta
        att = (dist * Wn / k)[:, :, None] * delta
        disp = rep.sum(axis=1) - att.sum(axis=1)
        ln = np.linalg.norm(disp, axis=1) + 1e-9
        pos += disp / ln[:, None] * np.minimum(ln, t)[:, None]
        pos = np.clip(pos, 0, 1)
        t *= 0.99
    pos = pos - pos.mean(axis=0)
    return pos / (pos.std(axis=0) + 1e-9)


def embed3d(W):
    """Three coordinates from the normalised Laplacian's second to fourth eigenvectors."""
    n = W.shape[0]
    d = W.sum(axis=1)
    keep = d > 0
    idx = np.nonzero(keep)[0]
    Wk = W[np.ix_(idx, idx)]
    dk = Wk.sum(axis=1)
    Dm = np.diag(1 / np.sqrt(dk))
    L = np.eye(len(idx)) - Dm @ Wk @ Dm
    vals, vecs = np.linalg.eigh(L)
    X = np.zeros((n, 3))
    for c in range(3):
        v = Dm @ vecs[:, c + 1]
        v = (v - v.mean()) / (v.std() or 1)
        X[idx, c] = v
    return X


# ---------------------------------------------------------------- build


def build(report_only=False, draft=False):
    """draft: tolerant load and no merge, so the pages can be tried while files are still being written."""
    t0 = datetime.datetime.now()
    gs, errs = load_all(tolerant=report_only or draft)
    if errs:
        for e in errs[:40]:
            print("  FAIL", e)
        raise SystemExit(f"fsg: {len(errs)} error(s) in the article files; fix them before deriving")
    if not gs:
        raise SystemExit("fsg: no article files")
    meta, desks, topics, find = article_meta()
    mlog = None
    if not report_only and not draft:
        mlog = merge(gs)
    else:
        logp = SRC / "runs" / f"{TODAY}-merge.json"
        mlog = load(logp) if logp.exists() else None
        gs, errs = load_all()
        if errs:
            for e in errs[:40]:
                print("  FAIL", e)
            raise SystemExit("fsg: the merge left errors; this is a bug in the merge")
    cid, eid = registry()
    nodes, edges = join(gs, meta)
    grav = gravity(gs, meta)
    ids, C, W = cooccurrence(gs, grav)
    # the constant companions (in more than a quarter of articles) are the frame every article is written in;
    # clustering with them in gives two blobs round the owner and the behaviour policy, so the clusters are computed
    # on the graph without them, and they are listed apart. Both clusterings are kept in the report.
    hub_idx = {k for k, i in enumerate(ids) if grav[i]["n_articles"] >= 0.25 * len(gs)}
    W_nohub = W.copy()
    for k in hub_idx:
        W_nohub[k, :] = 0; W_nohub[:, k] = 0
    comm_all = louvain(W) if len(ids) else np.zeros(0, dtype=int)
    Q_all = modularity(W, comm_all) if len(ids) else 0.0
    comm = louvain(W_nohub) if len(ids) else np.zeros(0, dtype=int)
    Q = modularity(W_nohub, comm) if len(ids) else 0.0
    # a node with no tie left (a hub, or one with no two-article tie) is unplaced: cluster -1
    for k in range(len(ids)):
        if W_nohub[k].sum() == 0:
            comm[k] = -1
    relabel = {c: n for n, c in enumerate(sorted(x for x in set(comm.tolist()) if x >= 0))}
    comm = np.array([relabel.get(int(c), -1) for c in comm])
    side, fscore = fiedler_cut(W) if len(ids) else (np.zeros(0, dtype=int), np.zeros(0))
    pos = layout2d(W) if len(ids) else np.zeros((0, 2))
    X3 = embed3d(W) if len(ids) else np.zeros((0, 3))
    F3 = layout3d(W) if len(ids) else np.zeros((0, 3))
    # the cut axis: every node's rank along the Fiedler vector, spread evenly, so the two sides read left and right
    xr = np.zeros(len(ids))
    if len(ids):
        order = np.argsort(fscore)
        xr[order] = np.linspace(0, 1, len(ids))

    # ---- counts
    claims = [c for g in gs.values() for c in g["claims"]]
    kinds = Counter(c["kind"] for c in claims)
    cc_edges = sum(len(g.get("edges", [])) for g in gs.values())
    verbs = Counter(e["verb"] for g in gs.values() for e in g.get("edges", []))
    all_about = Counter(a for c in claims for a in c.get("about", []))
    shared = {i for i, g in grav.items() if g["n_articles"] >= GRAVITY}
    claims_joined = sum(1 for c in claims if any(a in shared for a in c.get("about", [])))
    refs = {n for n, v in nodes.items() if v["kind"] == "reference"}
    ref_nodes = [nodes[r] for r in refs]
    ref_dated_day = sum(1 for r in ref_nodes if re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(r["date"])))
    domains = Counter(r["domain"] for r in ref_nodes)
    ref_kinds = Counter(r["ref_kind"] for r in ref_nodes)
    dates = Counter(n["label"][:7] for n in nodes.values() if n["kind"] == "date")
    ent_types = Counter(nodes[f"entity:{x['id']}"]["type"] for g in gs.values() for x in g["entities"] if f"entity:{x['id']}" in nodes)
    n_concepts_used = len({x["id"] for g in gs.values() for x in g["concepts"]})
    n_entities_used = len({x["id"] for g in gs.values() for x in g["entities"]})

    # ---- clusters: members, label, desks and topics inside
    clusters = []
    unplaced = [ids[k] for k in range(len(ids)) if comm[k] < 0]
    for c in sorted(x for x in set(comm.tolist()) if x >= 0):
        members = [ids[k] for k in np.nonzero(comm == c)[0]]
        members.sort(key=lambda i: -grav[i]["n_articles"])
        arts = Counter()
        for mbr in members:
            for s in grav[mbr]["articles"]:
                arts[s] += 1
        # an article belongs to the cluster where most of its gravity nodes sit (computed below); here, touched
        dk, tp = Counter(), Counter()
        for s in arts:
            if meta.get(s, {}).get("desk"):
                dk[meta[s]["desk"]] += 1
            for t in meta.get(s, {}).get("topics", []):
                tp[t] += 1
        clusters.append({"id": c, "label": " · ".join(nodes[m]["label"] for m in members[:3]), "members": members,
                         "n_members": len(members), "articles_touched": len(arts),
                         "desks": dict(dk.most_common()), "topics": dict(tp.most_common())})
    # article -> home cluster (plurality of its gravity nodes, weighted by claims about them)
    home = {}
    for slug, g in gs.items():
        votes = Counter()
        for cl in g["claims"]:
            for a in cl.get("about", []):
                if a in shared and comm[ids.index(a)] >= 0:
                    votes[int(comm[ids.index(a)])] += 1
        home[slug] = votes.most_common(1)[0][0] if votes else None
    for cl in clusters:
        cl["articles_home"] = sorted(s for s, h in home.items() if h == cl["id"])
        cl["n_articles_home"] = len(cl["articles_home"])
        cl["label_auto"] = cl["label"]
    # desk purity: share of a desk's articles in its top one and top two clusters
    purity = {}
    for d in desks:
        arts = [s for s in gs if meta.get(s, {}).get("desk") == d]
        hc = Counter(home[s] for s in arts if home.get(s) is not None)
        top2 = sum(n for _, n in hc.most_common(2))
        purity[d] = {"articles": len(arts), "top1": hc.most_common(1)[0][1] / len(arts) if arts and hc else 0,
                     "top2": top2 / len(arts) if arts else 0, "clusters": dict(hc.most_common())}
    topic_purity = {}
    for t in topics:
        arts = [s for s in gs if t in meta.get(s, {}).get("topics", [])]
        hc = Counter(home[s] for s in arts if home.get(s) is not None)
        topic_purity[t] = {"articles": len(arts), "clusters": dict(hc.most_common()),
                           "top2": sum(n for _, n in hc.most_common(2)) / len(arts) if arts else 0}
    sec_purity = {}
    for s in {x for m in meta.values() for x in m.get("sections", [])}:
        arts = [a for a in gs if s in meta.get(a, {}).get("sections", [])]
        hc = Counter(home[a] for a in arts if home.get(a) is not None)
        sec_purity[s] = {"articles": len(arts), "clusters": dict(hc.most_common()),
                         "top1": hc.most_common(1)[0][1] / len(arts) if arts and hc else 0}
    per_purity = {}
    for s in {x for m in meta.values() for x in m.get("personas", [])}:
        arts = [a for a in gs if s in meta.get(a, {}).get("personas", [])]
        hc = Counter(home[a] for a in arts if home.get(a) is not None)
        per_purity[s] = {"articles": len(arts), "clusters": dict(hc.most_common()),
                         "top2": sum(n for _, n in hc.most_common(2)) / len(arts) if arts else 0}

    # ---- the two-way cut
    sidemap = {ids[k]: int(side[k]) for k in range(len(ids))}
    art_side = {}
    for slug, g in gs.items():
        votes = Counter()
        for cl in g["claims"]:
            for a in cl.get("about", []):
                if a in sidemap and sidemap[a] >= 0:
                    votes[sidemap[a]] += 1
        art_side[slug] = votes.most_common(1)[0][0] if votes else None
    side_count = Counter(v for v in art_side.values() if v is not None)
    hemis = []
    for s in (0, 1):
        members = [ids[k] for k in range(len(ids)) if side[k] == s]
        members.sort(key=lambda i: -grav[i]["n_articles"])
        dk = Counter(meta[a]["desk"] for a, v in art_side.items() if v == s and meta.get(a, {}).get("desk"))
        tp = Counter(t for a, v in art_side.items() if v == s for t in meta.get(a, {}).get("topics", []))
        hemis.append({"side": s, "members": members, "n_members": len(members), "articles": side_count.get(s, 0),
                      "share": side_count.get(s, 0) / max(1, sum(side_count.values())),
                      "desks": dict(dk.most_common()), "topics": dict(tp.most_common()),
                      "top": [nodes[m]["label"] for m in members[:12]]})
    # bridges: gravity nodes whose neighbours split most evenly across the cut
    bridges = []
    for k, i in enumerate(ids):
        nb = np.nonzero(W[k])[0]
        if len(nb) < 4:
            continue
        other = sum(W[k, j] for j in nb if side[j] != side[k])
        tot = W[k].sum()
        bridges.append({"id": i, "label": nodes[i]["label"], "cross": float(other / tot), "articles": grav[i]["n_articles"],
                        "side": int(side[k])})
    bridges.sort(key=lambda b: (-min(b["cross"], 1 - b["cross"]) * math.log(1 + b["articles"])))
    bridges = bridges[:15]

    # ---- the constant companions: nodes in more than a quarter of all articles
    hubs = [{"id": ids[k], "label": nodes[ids[k]]["label"], "articles": grav[ids[k]]["n_articles"], "share": round(grav[ids[k]]["n_articles"] / len(gs), 2)}
            for k in sorted(hub_idx)]
    hubs.sort(key=lambda h: -h["articles"])

    # ---- the cut again without the constant companions, to see what the frame hides
    W2 = W_nohub
    side2, _ = fiedler_cut(W2) if len(ids) else (np.zeros(0, dtype=int), None)
    side2map = {ids[k]: int(side2[k]) for k in range(len(ids)) if k not in hub_idx}
    art_side2 = {}
    for slug, g in gs.items():
        votes = Counter()
        for cl in g["claims"]:
            for a in cl.get("about", []):
                if a in side2map and side2map[a] >= 0:
                    votes[side2map[a]] += 1
        art_side2[slug] = votes.most_common(1)[0][0] if votes else None
    sc2 = Counter(v for v in art_side2.values() if v is not None)
    hemis2 = []
    for s in (0, 1):
        members = [ids[k] for k in range(len(ids)) if side2[k] == s and k not in hub_idx]
        members.sort(key=lambda i: -grav[i]["n_articles"])
        dk = Counter(meta[a]["desk"] for a, v in art_side2.items() if v == s and meta.get(a, {}).get("desk"))
        hemis2.append({"side": s, "n_members": len(members), "articles": sc2.get(s, 0),
                       "share": sc2.get(s, 0) / max(1, sum(sc2.values())), "desks": dict(dk.most_common()),
                       "top": [nodes[m]["label"] for m in members[:12]]})
    # how much the two cuts agree, on the nodes both place
    both = [k for k in range(len(ids)) if k not in hub_idx and side[k] >= 0 and side2[k] >= 0]
    agree = sum(1 for k in both if side[k] == side2[k]) / max(1, len(both))
    cut2 = {"sides": hemis2, "agreement_with_full_cut": round(max(agree, 1 - agree), 3), "hubs_removed": len(hub_idx)}
    side2 = np.array([int(side2[k]) if k not in hub_idx else -1 for k in range(len(ids))]) if len(ids) else side2

    # ---- peaks: gravity x bridging (clusters touched through co-occurrence)
    peaks = []
    for k, i in enumerate(ids):
        nb = np.nonzero(W[k])[0]
        touched = len({int(comm[j]) for j in nb if comm[j] >= 0} | ({int(comm[k])} if comm[k] >= 0 else set()))
        g = grav[i]
        peaks.append({"id": i, "kind": i.split(":")[0], "label": nodes[i]["label"], "type": nodes[i].get("type", ""),
                      "articles": g["n_articles"], "claims": g["claims"], "clusters_touched": touched,
                      "cluster": int(comm[k]), "score": g["n_articles"] * touched, "first": g["first"], "first_date": g["first_date"],
                      "desks": g["desks"]})
    peaks.sort(key=lambda p: (-p["score"], -p["articles"], p["label"]))

    # ---- births: concepts and entities with gravity, by the date of the first article that used them
    births = []
    for i in shared:
        g = grav[i]
        births.append({"id": i, "label": nodes[i]["label"], "first": g["first"], "first_date": g["first_date"],
                       "articles": g["n_articles"]})
    births.sort(key=lambda b: (b["first_date"] or "", b["label"]))
    by_month = Counter((b["first_date"] or "")[:7] for b in births)
    # new concepts per article, in date order: a concept is new to the article that first used it
    order = sorted(gs, key=lambda s: (meta.get(s, {}).get("date", ""), s))
    seen = set(); new_per_article = []
    for s in order:
        used = {a for cl in gs[s]["claims"] for a in cl.get("about", [])}
        fresh = used - seen
        new_per_article.append({"slug": s, "date": meta.get(s, {}).get("date", ""), "new": len(fresh), "used": len(used),
                                "new_with_gravity": len(fresh & shared)})
        seen |= used
    for x in new_per_article:
        x["new_concepts"] = 0
    seen_c = set()
    for x in new_per_article:
        used = {a for cl in gs[x["slug"]]["claims"] for a in cl.get("about", []) if a.startswith("concept:")}
        x["new_concepts"] = len(used - seen_c)
        x["new_concepts_with_gravity"] = len((used - seen_c) & shared)
        seen_c |= used
    by_period = Counter()
    for b in births:
        d = b["first_date"] or ""
        by_period["before September" if d < "2026-09" else "September" if d < "2026-10" else "1 to 7 October" if d <= "2026-10-07" else "8 October on"] += 1
    by_period_concepts = Counter()
    for b in births:
        if b["id"].startswith("concept:"):
            d = b["first_date"] or ""
            by_period_concepts["before September" if d < "2026-09" else "September" if d < "2026-10" else "1 to 7 October" if d <= "2026-10-07" else "8 October on"] += 1
    last30 = new_per_article[-30:]
    last30_avg = sum(x["new"] for x in last30) / max(1, len(last30))
    last30_avg_g = sum(x["new_with_gravity"] for x in last30) / max(1, len(last30))

    # ---- first-pass failures, from the check log
    first_pass = {"files": 0, "with_errors": 0, "errors": 0, "quote_errors": 0}
    for p in sorted((SRC / "runs").glob("*-checks.tsv")):
        seen_slugs = set()
        for line in p.read_text(encoding="utf-8").splitlines():
            parts = line.split("\t")
            if len(parts) < 5:
                continue
            _, slug, ne, nw, nq = parts
            if slug in seen_slugs:
                continue
            seen_slugs.add(slug)
            first_pass["files"] += 1
            if int(ne):
                first_pass["with_errors"] += 1
            first_pass["errors"] += int(ne); first_pass["quote_errors"] += int(nq)

    report = {
        "what": "The emergence report of the graph of meaning, derived by admin/build/fsg.py from admin/content/graphs/articles/*.json. Deterministic: the same files give the same report.",
        "run": RUN, "built": datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d %H:%M UTC"),
        "articles": len(gs), "claims": len(claims), "claims_per_article": round(len(claims) / len(gs), 1),
        "claim_kinds": dict(kinds.most_common()),
        "claim_kind_shares": {k: round(v / len(claims), 3) for k, v in kinds.items()},
        "claim_edges": cc_edges, "claim_verbs": dict(verbs.most_common()),
        "edges_total": len(edges), "nodes_total": len(nodes),
        "concepts_used": n_concepts_used, "entities_used": n_entities_used, "entity_types": dict(ent_types.most_common()),
        "registry": {"concepts": len(cid), "entities": len(eid)},
        "shared": {"ids_with_gravity": len(shared), "concepts": sum(1 for i in shared if i.startswith("concept:")),
                   "entities": sum(1 for i in shared if i.startswith("entity:")),
                   "claims_joined": claims_joined, "claims_joined_share": round(claims_joined / len(claims), 3),
                   "about_total": sum(all_about.values())},
        "references": {"distinct": len(refs), "citations": sum(1 for e in edges if e[1] == "cites" and e[0].startswith("article:")),
                       "domains": len(domains), "dated_to_day": ref_dated_day, "dated_to_day_share": round(ref_dated_day / max(1, len(refs)), 3),
                       "top_domains": domains.most_common(15), "kinds": dict(ref_kinds.most_common())},
        "dates": {"distinct": sum(1 for n in nodes.values() if n["kind"] == "date"), "by_month": dict(sorted(dates.items()))},
        "clusters": {"n": len(clusters), "modularity": round(Q, 3), "list": clusters, "unplaced": unplaced,
                     "with_frame": {"n": len(set(comm_all.tolist())), "modularity": round(Q_all, 3),
                                    "sizes": sorted(Counter(comm_all.tolist()).values(), reverse=True)}},
        "cut": {"sides": hemis, "bridges": bridges},
        "hubs": hubs,
        "cut_without_hubs": cut2,
        "purity": {"desks": purity, "topics": topic_purity, "sections": sec_purity, "personas": per_purity},
        "peaks": {"all": peaks[:40], "concepts": [p for p in peaks if p["kind"] == "concept"][:15],
                  "entities": [p for p in peaks if p["kind"] == "entity"][:15],
                  "by_articles": sorted(peaks, key=lambda p: -p["articles"])[:20]},
        "births": {"by_month": dict(sorted(by_month.items())), "by_period": dict(by_period), "by_period_concepts": dict(by_period_concepts),
                   "list": births, "new_per_article": new_per_article,
                   "last30_new_avg": round(last30_avg, 2), "last30_new_with_gravity_avg": round(last30_avg_g, 2),
                   "last30_new_concepts_avg": round(sum(x["new_concepts"] for x in last30) / max(1, len(last30)), 2),
                   "last30_new_concepts_with_gravity_avg": round(sum(x["new_concepts_with_gravity"] for x in last30) / max(1, len(last30)), 2)},
        "first_pass": first_pass,
        "merge": mlog,
        "seconds": round((datetime.datetime.now() - t0).total_seconds(), 1),
    }
    OUT.mkdir(exist_ok=True); (OUT / "data").mkdir(exist_ok=True)
    (OUT / "data" / "report.json").write_text(json.dumps(report, indent=1, ensure_ascii=False, default=str) + "\n", encoding="utf-8")
    print_report(report)
    if report_only:
        return 0
    ctx = {"gs": gs, "meta": meta, "desks": desks, "topics": topics, "nodes": nodes, "edges": edges, "grav": grav,
           "ids": ids, "W": W, "C": C, "F3": F3, "xr": xr, "fscore": fscore, "side2": side2, "comm": comm, "side": side, "pos": pos, "X3": X3, "report": report, "cid": cid, "eid": eid,
           "home": home, "art_side": art_side, "clusters": clusters}
    write_data(ctx)
    import fsg_pages
    n = fsg_pages.write_pages(ctx)
    print(f"fsg: {n} page(s) written under graphs/")
    return 0


def print_report(r):
    print(f"fsg: {r['articles']} articles, {r['claims']} claims ({r['claims_per_article']} each): "
          + ", ".join(f"{k} {v}" for k, v in r["claim_kinds"].items()))
    s = r["shared"]
    print(f"fsg: {s['ids_with_gravity']} ids with gravity ({s['concepts']} concepts, {s['entities']} entities); "
          f"{s['claims_joined']} of {r['claims']} claims ({s['claims_joined_share']:.0%}) about something another article is also about")
    print(f"fsg: {r['references']['distinct']} references over {r['references']['domains']} domains, "
          f"{r['references']['dated_to_day']} dated to the day; top: {r['references']['top_domains'][:5]}")
    print(f"fsg: {r['clusters']['n']} clusters (modularity {r['clusters']['modularity']}):")
    for c in r["clusters"]["list"]:
        print(f"      {c['id']:2d} {c['n_members']:3d} nodes, {c['n_articles_home']:3d} articles home: {c['label']} | desks {c['desks']}")
    for h in r["cut"]["sides"]:
        print(f"fsg: side {h['side']}: {h['articles']} articles ({h['share']:.0%}), {h['n_members']} nodes; top {h['top'][:8]}; desks {h['desks']}")
    for h in r["cut_without_hubs"]["sides"]:
        print(f"fsg: without the hubs, side {h['side']}: {h['articles']} articles ({h['share']:.0%}); top {h['top'][:8]}; desks {h['desks']}")
    print(f"fsg: the two cuts agree on {r['cut_without_hubs']['agreement_with_full_cut']:.0%} of nodes")
    print("fsg: bridges:", [(b["label"], round(b["cross"], 2)) for b in r["cut"]["bridges"][:8]])
    print("fsg: peaks:", [(p["label"], p["articles"], p["clusters_touched"]) for p in r["peaks"]["all"][:12]])
    print("fsg: births by month:", r["births"]["by_month"], "by period:", r["births"]["by_period"], "concepts:", r["births"]["by_period_concepts"],
          "| last 30 articles: new ids per article", r["births"]["last30_new_avg"], "with gravity", r["births"]["last30_new_with_gravity_avg"],
          "| new concepts", r["births"]["last30_new_concepts_avg"], "with gravity", r["births"]["last30_new_concepts_with_gravity_avg"])
    print("fsg: unplaced:", len(r["clusters"]["unplaced"]), "| with the frame:", r["clusters"]["with_frame"])
    print("fsg: top names:", [(p["label"], p["articles"]) for p in r["peaks"]["entities"][:15]])
    print("fsg: top concepts:", [(p["label"], p["articles"]) for p in r["peaks"]["concepts"][:15]])
    print("fsg: desk purity:", {d: (round(v["top1"], 2), round(v["top2"], 2)) for d, v in r["purity"]["desks"].items()})
    print("fsg: first pass:", r["first_pass"])
    if r.get("merge"):
        m = r["merge"]
        print(f"fsg: merge: concepts +{len(m['concepts']['added'])} merged {merged_count(m, 'concepts')}; "
              f"entities +{len(m['entities']['added'])} merged {merged_count(m, 'entities')}; {m['files_rewritten']} files rewritten")


def merged_count(m, kind):
    """Merges of the day: the ones listed, plus a count kept when the first build's list was lost (see the log's note)."""
    return len(m[kind]["merged"]) + int(m[kind].get("merged_count_first_build", 0))


# ---------------------------------------------------------------- data files


def write_data(ctx):
    nodes, edges, grav, ids, comm, side, pos, X3 = (ctx[k] for k in ("nodes", "edges", "grav", "ids", "comm", "side", "pos", "X3"))
    meta, gs = ctx["meta"], ctx["gs"]
    d = OUT / "data"
    # the map: nodes with gravity, their layout, cluster, side, 3D embedding; edges above a weight
    W = ctx["W"]
    mnodes = []
    for k, i in enumerate(ids):
        g = grav[i]
        mnodes.append({"id": i, "label": nodes[i]["label"], "kind": i.split(":")[0], "type": nodes[i].get("type", ""),
                       "articles": g["n_articles"], "claims": g["claims"], "cluster": int(comm[k]), "side": int(side[k]), "side2": int(ctx["side2"][k]),
                       "x": round(float(pos[k, 0]), 4), "y": round(float(pos[k, 1]), 4),
                       "x3": round(float(X3[k, 0]), 4), "y3": round(float(X3[k, 1]), 4), "z3": round(float(X3[k, 2]), 4),
                       "xr": round(float(ctx["xr"][k]), 4), "fiedler": round(float(ctx["fscore"][k]), 5),
                       "xf": round(float(ctx["F3"][k, 0]), 4), "yf": round(float(ctx["F3"][k, 1]), 4), "zf": round(float(ctx["F3"][k, 2]), 4),
                       "first": g["first"], "slugs": g["articles"]})
    medges = []
    C = ctx["C"]
    for a in range(len(ids)):
        for b in range(a + 1, len(ids)):
            if C[a, b] >= 2:
                medges.append([a, b, int(C[a, b]), round(float(W[a, b]), 3)])
    cl = [{"id": c["id"], "label": c["label"], "n": c["n_members"], "articles": c["n_articles_home"]} for c in ctx["clusters"]]
    (d / "map.json").write_text(json.dumps({"what": "The concepts and names with gravity (two or more articles). Coordinates: x,y a force layout; xr the node's rank along the Fiedler vector (the cut's own axis, 0 one side, 1 the other); x3,y3,z3 the Laplacian's second to fourth eigenvectors; xf,yf,zf a force layout in three dimensions. An edge is [a, b, articles shared, normalised weight]. Clusters by Louvain, side by the Fiedler cut.",
                                            "run": RUN, "nodes": mnodes, "edges": medges, "clusters": cl,
                                            "articles": {s: {"title": meta.get(s, {}).get("title", s), "date": meta.get(s, {}).get("date", ""),
                                                             "home": ctx["home"].get(s), "side": ctx["art_side"].get(s)} for s in gs}},
                                           ensure_ascii=False) + "\n", encoding="utf-8")
    # the claims dimension: every claim with its article, kind, section, quote, value, about
    claims = []
    for slug, g in gs.items():
        for c in g["claims"]:
            claims.append({"article": slug, "date": meta.get(slug, {}).get("date", ""), **{k: c.get(k) for k in ("id", "kind", "text", "section", "quote", "about", "value", "refs")}})
    (d / "claims.json").write_text(json.dumps({"what": "Every claim of every article: kind, text, section anchor, the quote it rests on, what it is about, its value if a data point.", "run": RUN, "verbs": VERBS, "claims": claims,
                                               "edges": [{"article": s, **e} for s, g in gs.items() for e in g.get("edges", [])]}, ensure_ascii=False) + "\n", encoding="utf-8")
    # names and concepts with their gravity
    names = {i: {"label": nodes[i]["label"], "kind": i.split(":")[0], "type": nodes[i].get("type", ""), "means": nodes[i].get("means", ""), **g}
             for i, g in grav.items()}
    (d / "names.json").write_text(json.dumps({"what": "Every concept and name a claim is about, with the articles that use it, the claims about it, the desks and topics they sit on, and the first article that used it.", "run": RUN, "gravity_rule": GRAVITY, "nodes": names}, ensure_ascii=False, default=list) + "\n", encoding="utf-8")
    refs = [v | {"id": k, "articles": sorted({e[0].split(":", 1)[1] for e in edges if e[1] == "cites" and e[3] == k and e[0].startswith("article:")})}
            for k, v in nodes.items() if v["kind"] == "reference"]
    refs.sort(key=lambda r: (-len(r["articles"]), r["domain"], r["label"]))
    (d / "sources.json").write_text(json.dumps({"what": "Every outside source the articles cite, with its date as the article gives it, its kind, and the articles that cite it.", "run": RUN, "references": refs}, ensure_ascii=False) + "\n", encoding="utf-8")
    dates = defaultdict(list)
    for slug, g in gs.items():
        for x in g.get("dates", []):
            dates[x["date"]].append({"article": slug, "what": x["what"]})
    (d / "time.json").write_text(json.dumps({"what": "Every date the articles turn on, with what happened and which article says so.", "run": RUN, "dates": dict(sorted(dates.items()))}, ensure_ascii=False) + "\n", encoding="utf-8")
    # the whole graph as typed edges with inverses, for an agent that wants the join itself
    (d / "edges.json").write_text(json.dumps({"what": "Every edge of the join as [from, verb, inverse, to]. Every verb has its inverse; the generic association edge does not exist here.", "run": RUN, "verbs": {**VERBS, **fsg.DERIVED_VERBS},
                                              "nodes": {k: {kk: vv for kk, vv in v.items() if kk in ("kind", "label", "type", "claim_kind", "date", "slug")} for k, v in nodes.items()},
                                              "edges": edges}, ensure_ascii=False) + "\n", encoding="utf-8")
