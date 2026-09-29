#!/usr/bin/env python3
"""world-news-day/ — the aggregate.

    python3 world-news-day/build/analysis.py     (build.py runs it)

Twenty-one people who run the world's newsrooms were asked the same question in the same
week and answered it in public, under the same permission. That is an unusual object: not a
survey, not a conference programme, but a set of position statements written to be read
together. Read one at a time they are opinion pieces. Counted together they are a picture of
what this industry's most powerful voices currently believe is worth saying — and, more
usefully, of what they do not say.

Every number here is a count over the frozen bytes, produced by a formula in this file and
re-derived by build/gates.py. Nothing here is a judgement about a person or a publication:

  · A theme count says a piece contains certain words. It does not say the author cares
    about the subject, and the absence of a theme says nothing about what they believe —
    only about what this piece, of 900 words, had room for.
  · A link count says what evidence the piece offered its own reader on the page. It is not
    a measure of how well researched the piece is. It IS the thing this publication has
    argued about since its first page, which is why it is counted.

Written out to data/analysis.json so a reader can check the arithmetic, or do their own.
"""
import collections
import itertools
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SEC = ROOT / "world-news-day"
DATA = SEC / "data"


def load(n):
    return json.loads((DATA / n).read_text(encoding="utf-8"))


def norm(d):
    return re.sub(r"^www\.", "", d)


def main():
    corpus = load("corpus.json")
    graph = load("graph.json")
    lexicon = load("lexicon.json")
    arts = corpus["articles"]
    nodes = {n["id"]: n for n in graph["nodes"]}
    lex_label = {e["id"]: e["label"] for e in lexicon["entries"]}

    # --- what they talk about -------------------------------------------------------
    themes_by_article = collections.defaultdict(set)
    for e in graph["edges"]:
        if e["verb"] == "touches":
            themes_by_article[e["source"].split(":", 1)[1]].add(nodes[e["target"]]["lexicon"])
    freq = collections.Counter()
    for s, ts in themes_by_article.items():
        for t in ts:
            freq[t] += 1
    themes = [{"id": t, "label": lex_label[t], "articles": n,
               "share": round(n / len(arts), 3)}
              for t, n in freq.most_common()]
    for e in lexicon["entries"]:
        if e["id"] not in freq:
            themes.append({"id": e["id"], "label": e["label"], "articles": 0, "share": 0.0})

    # --- what they talk about together ------------------------------------------------
    pairs = collections.Counter()
    for s, ts in themes_by_article.items():
        for a, b in itertools.combinations(sorted(ts), 2):
            pairs[(a, b)] += 1
    together = [{"a": lex_label[a], "b": lex_label[b], "articles": n}
                for (a, b), n in pairs.most_common(12)]
    ids = sorted(lex_label)
    apart = [{"a": lex_label[a], "b": lex_label[b]}
             for a, b in itertools.combinations(ids, 2)
             if pairs[(a, b)] == 0 and freq[a] and freq[b]]

    # --- what evidence they offer the reader --------------------------------------------
    # The count this publication exists to make. Our own thesis page has argued since the
    # first version that a story which cites nothing a reader can follow is a story the
    # reader has to take on trust. Here it is, over the people who make the argument for
    # trusting journalism, in the week they made it.
    per_article = sorted(
        ({"slug": a["slug"], "title": a["title"], "links": len(a["outbound_links"]),
          "domains": sorted({norm(d) for d in a["outbound_domains"]})} for a in arts),
        key=lambda r: (-r["links"], r["slug"]))
    by_domain = collections.defaultdict(set)
    for a in arts:
        for d in a["outbound_domains"]:
            by_domain[norm(d)].add(a["slug"])
    shared = {d: sorted(s) for d, s in by_domain.items() if len(s) > 1}
    # second-level, because unesdoc.unesco.org and www.unesco.org are one institution
    second = collections.defaultdict(set)
    for a in arts:
        for d in a["outbound_domains"]:
            second[".".join(d.split(".")[-2:])].add(a["slug"])
    shared2 = {d: sorted(s) for d, s in second.items() if len(s) > 1}
    evidence = {
        "articles": len(arts),
        "with_no_outbound_link_at_all": sum(1 for a in arts if not a["outbound_links"]),
        "with_at_least_one": sum(1 for a in arts if a["outbound_links"]),
        "total_links": sum(len(a["outbound_links"]) for a in arts),
        "median_links_per_article": sorted(len(a["outbound_links"]) for a in arts)[len(arts) // 2],
        "most_links_in_one_piece": max(len(a["outbound_links"]) for a in arts),
        "distinct_domains": len(by_domain),
        "domains_reached_by_more_than_one_piece": shared,
        "institutions_reached_by_more_than_one_piece": shared2,
        "per_article": per_article,
        "note": "Counted as the article offers them: an <a> in the article body, in the frozen "
                "bytes. Links in the site's own furniture are not the article's evidence and "
                "are not counted. Nothing here was fetched: this section says what the piece "
                "offered, not whether it holds up.",
    }

    # --- who is speaking ------------------------------------------------------------------
    orgs = sorted({n["label"] for n in graph["nodes"] if n["type"] == "Organisation"
                   and n["id"] != "org:world-news-day"})
    people = {
        "articles": len(arts),
        "named_authors": len({b for a in arts for b in a["byline"]}),
        "pieces_with_more_than_one_byline": sum(1 for a in arts if len(a["byline"]) > 1),
        "organisations_named_in_role_lines": len(orgs),
        "organisations": orgs,
        "note": "An author's organisation is taken from the role line the piece itself prints "
                "under the byline, never from anywhere else, and never looked up.",
    }

    # --- the shape of it --------------------------------------------------------------------
    words = sorted(a["words"] for a in arts)
    shape = {
        "total_words": sum(words),
        "shortest": words[0],
        "longest": words[-1],
        "median": words[len(words) // 2],
        "published_between": [min(a["published"] for a in arts)[:10],
                              max(a["published"] for a in arts)[:10]],
        "themes_per_article_min": min(len(v) for v in themes_by_article.values()),
        "themes_per_article_max": max(len(v) for v in themes_by_article.values()),
    }

    out = {
        "id": "wnd-analysis",
        "version": "0.1.0",
        "updated": corpus["snapshot"],
        "question": "Twenty-one editors, publishers and directors answered the same question in "
                    "the same week. Counted together, what did they say — and what did they not?",
        "how": "Every number is a count over the frozen bytes. The themes are the published "
               "lexicon in data/lexicon.json and nothing else; the links are the <a> tags in the "
               "article body. build/gates.py re-derives all of it.",
        "refuses": [
            "No sentiment, no stance, no scoring. A count of words is not a measure of a person.",
            "No claim that two authors agree. agrees_with is a banned verb in this graph.",
            "No claim about what an author believes, only about what this one piece contains.",
            "No ranking of the publications. The corpus is not a competition and we are not a judge.",
        ],
        "shape": shape,
        "people": people,
        "themes": themes,
        "themes_together": together,
        "themes_never_together": apart,
        "evidence": evidence,
    }
    (DATA / "analysis.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n",
                                        encoding="utf-8")
    print(f"analysis: {len(themes)} themes, {evidence['with_no_outbound_link_at_all']} of "
          f"{len(arts)} pieces offer no link, {evidence['distinct_domains']} distinct domains, "
          f"{len(shared)} reached twice")
    return out


if __name__ == "__main__":
    main()
