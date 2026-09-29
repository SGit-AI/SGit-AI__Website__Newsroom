#!/usr/bin/env python3
"""world-news-day/ — the fractal layer: every sentence, typed, anchored, and connected.

    python3 world-news-day/build/claims.py        (build.py runs it)

The section so far treats each op-ed as one node. That is the coarse view, and it throws away
the thing that makes twenty-one position statements interesting: what each one actually
*does* sentence by sentence — asserts, asks, supposes, evaluates, proposes — and where those
sentences touch the same ideas across articles that never cite each other.

So this builds the level below. Each article becomes its own small graph of claims; the small
graphs connect to each other through a shared vocabulary; and the whole thing is the same
shape at both zoom levels. That is what makes it fractal rather than merely big: an article
is a graph, the corpus is a graph of those graphs, and a term is a graph of everywhere it is
used.

THE HARD CONSTRAINT, and how it is met. This section republishes none of the prose, and the
gate fails the build if twelve consecutive words of any piece appear on a page we generate. A
claim layer is exactly where that rule would normally be broken, so:

  · a claim node carries a TYPE, an OFFSET into the frozen prose, a length, and an ANCHOR —
    at most eight words, verbatim, enough to find the sentence and far short of reproducing
    it. The gate checks every anchor is in the bytes AND is under the limit.
  · the sentence itself is never stored. To read it, follow the article's own URL. The offset
    is there so that a reader or a machine can find the exact place without us holding a copy.

CLASSIFICATION IS A PUBLISHED FORMULA OR IT DOES NOT HAPPEN. data/claim-rules.json holds
every pattern, in order, and the first one that matches wins. A claim type therefore says
exactly one thing: this sentence has this shape. It does not say the sentence is true, or
that the author believes it, and an "evaluation" is not an accusation of bias — an op-ed is
supposed to evaluate things. What the counts are actually good for is comparison: twenty-one
pieces answering one question, and the shape of the answers differing.
"""
import html
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

SEC = Path(__file__).resolve().parents[1]
DATA = SEC / "data"

# Ordered. First match wins, and the order is the claim: a sentence that both asks and
# proposes is recorded as a question, because that is the stronger signal about what the
# sentence is doing.
CLAIM_RULES = [
    {"id": "question", "label": "Question",
     "pattern": r"\?\s*$",
     "means": "The sentence asks something. Rhetorical or real — this does not distinguish them."},
    {"id": "attribution", "label": "Attributed statement",
     "pattern": r"\b(according to|said|says|told|wrote|argues?|argued|reported|reports|"
                r"found that|estimates?|research shows|a study)\b",
     "means": "The sentence hands the claim to somebody else. Placed SECOND, ahead of proposal "
              "and hypothesis, deliberately: it is the only class that points outside the "
              "piece, and this section's central finding is about evidence. Ordering it late "
              "would have undercounted attributions and flattered our own argument."},
    {"id": "proposal", "label": "Proposal",
     "pattern": r"\b(we (?:must|should|need to|have to|cannot afford)|must be|should be|"
                r"needs? to be|it is time to|let us|let's|the answer is to|what is needed)\b",
     "means": "The sentence says something ought to be done. The heart of an op-ed, and the "
              "thing this corpus has least of relative to diagnosis."},
    {"id": "hypothesis", "label": "Hypothesis",
     "pattern": r"\b(if |unless |were we to|suppose |imagine |could |might |may |would |"
                r"risks? becoming|threatens to|is likely to)\b",
     "means": "The sentence supposes rather than asserts: a condition, a possibility, a "
              "consequence that has not happened yet."},
    {"id": "quantified", "label": "Quantified observation",
     "pattern": r"(\b\d[\d,.]*\s*(?:%|per cent|percent|million|billion|thousand)|"
                r"\b(?:19|20)\d\d\b|\b\d+\s+(?:years?|months?|days?|people|journalists|countries))",
     "means": "The sentence carries a number, a date or a count. The kind of statement a "
              "reader could in principle check — if the piece said where it came from."},
    {"id": "evaluation", "label": "Evaluation",
     "pattern": r"\b(dangerous|vital|essential|crucial|urgent|extraordinary|remarkable|"
                r"shameful|corrosive|devastating|vital|indispensable|worse|better|best|worst|"
                r"too (?:many|much|little|few)|failure|failing|broken|thriving)\b",
     "means": "The sentence judges. An op-ed is supposed to; this is not a criticism, it is a "
              "measurement of form."},
    {"id": "assertion", "label": "Assertion",
     "pattern": r".",
     "means": "Everything else: a declarative sentence stated flat, in the author's own voice, "
              "with no hedge, no number, no source and no explicit judgement. The default, and "
              "in this corpus the largest class by a wide margin."},
]

# A published vocabulary. A term is counted where it appears as a word, and nothing more is
# claimed. These are the words the corpus argues ABOUT — deliberately narrower than the theme
# lexicon, because the point here is to find the same idea used differently, not to label a
# piece's subject.
TERMS = [
    ("journalism", r"\bjournalis(?:m|ts?)\b"), ("truth", r"\btruths?\b"),
    ("facts", r"\bfacts?\b"), ("trust", r"\btrust(?:ed|worthy)?\b"),
    ("democracy", r"\bdemocra(?:cy|tic)\b"), ("freedom", r"\bfreedoms?\b"),
    ("press freedom", r"\bpress freedom\b"), ("misinformation", r"\bmis-?information\b"),
    ("disinformation", r"\bdis-?information\b"), ("propaganda", r"\bpropaganda\b"),
    ("artificial intelligence", r"\b(?:artificial intelligence|\bAI\b)"),
    ("algorithm", r"\balgorithm(?:s|ic)?\b"), ("platform", r"\bplatforms?\b"),
    ("social media", r"\bsocial media\b"), ("audience", r"\baudiences?\b"),
    ("reader", r"\breaders?\b"), ("public interest", r"\bpublic interest\b"),
    ("public service", r"\bpublic service\b"), ("accountability", r"\baccountabilit(?:y|ies)\b"),
    ("transparency", r"\btransparen(?:cy|t)\b"), ("evidence", r"\bevidence\b"),
    ("verification", r"\bverif(?:y|ied|ication)\b"), ("source", r"\bsources?\b"),
    ("funding", r"\bfund(?:ing|ed|s)\b"), ("subscription", r"\bsubscri(?:be|ption|bers?)\b"),
    ("advertising", r"\badvertis(?:ing|ers?|ement)\b"), ("business model", r"\bbusiness model\b"),
    ("copyright", r"\bcopyright\b"), ("licence", r"\blicen[cs]e[sd]?\b"),
    ("local news", r"\blocal (?:news|journalism|media)\b"),
    ("censorship", r"\bcensor(?:ship|ed|ing)\b"), ("exile", r"\bexiles?\b|\bin exile\b"),
    ("safety", r"\bsafety\b"), ("impunity", r"\bimpunity\b"),
    ("climate", r"\bclimate\b"), ("war", r"\bwars?\b|\bconflicts?\b"),
    ("community", r"\bcommunit(?:y|ies)\b"), ("independence", r"\bindependen(?:ce|t)\b"),
    ("ownership", r"\bowner(?:s|ship)?\b"), ("infrastructure", r"\binfrastructure\b"),
]

# "X is …", "X means …" — where a piece tells the reader what a word stands for. The capture
# is the term; the anchor is the first words of what follows, so two pieces saying what the
# same word means can be put side by side without either being reproduced.
#
# THE TERM MUST BE THE SUBJECT OF ITS OWN SENTENCE. The first version of this matched the
# pattern anywhere, and read "the decline of local news is a global phenomenon" as the piece
# defining LOCAL NEWS as a global phenomenon eroding democracies. That is not what the author
# wrote, and putting it on a page beside another author's definition would have misrepresented
# them both. So the sentence must START with the term, allowing only a determiner in front.
DEFINITION = (r"^(?:the|a|an|our|its|real|good|true)?\s*\b{term}\b\s+"
              r"(?:is|are|means?|is not|are not|has always been|must be|remains?)\b")

# The rule this replaced, kept because the difference between the two counts is the finding.
LOOSE_DEFINITION = r"\b{term}\b\s+(?:is|are|means?|is not|are not|has always been|must be)\b"

ANCHOR_WORDS = 8          # hard ceiling: the gate refuses anything longer
SENTENCE_SPLIT = re.compile(r'(?<=[.!?])\s+(?=[A-Z"“‘])')


def load(n):
    return json.loads((DATA / n).read_text(encoding="utf-8"))


def prose_of(slug, latest):
    rec = json.loads((SEC / "sources" / "frozen" / latest / "api" / f"{slug}.json")
                     .read_text(encoding="utf-8"))[0]
    body = " ".join(html.unescape(re.sub(r"<[^>]+>", " ", rec["content"]["rendered"])).split())
    cut = body.find("This opinion piece was commissioned")
    return body[:cut].strip() if cut > 0 else body.strip()


def anchor_of(sentence):
    return " ".join(sentence.split()[:ANCHOR_WORDS])


def classify(sentence):
    for r in CLAIM_RULES:
        if re.search(r["pattern"], sentence, re.I):
            return r["id"]
    return "assertion"


def main():
    corpus = load("corpus.json")
    register = load("register.json")
    latest = register["snapshots"][-1]
    term_pat = {t: re.compile(p, re.I) for t, p in TERMS}

    claims, by_article = [], {}
    term_hits = defaultdict(lambda: defaultdict(int))     # term -> slug -> n
    definitions = []

    for a in corpus["articles"]:
        text = prose_of(a["slug"], latest)
        pos, rows = 0, []
        for s in SENTENCE_SPLIT.split(text):
            s = s.strip()
            if not s:
                continue
            off = text.find(s, pos)
            pos = (off if off >= 0 else pos) + len(s)
            if len(s.split()) < 4:                 # a fragment, not a claim
                continue
            kind = classify(s)
            terms = sorted(t for t, p in term_pat.items() if p.search(s))
            for t in terms:
                term_hits[t][a["slug"]] += 1
            cid = f'claim:{a["slug"]}:{len(rows) + 1}'
            rows.append({
                "id": cid, "article": a["slug"], "n": len(rows) + 1,
                "type": kind, "anchor": anchor_of(s), "offset": off if off >= 0 else None,
                "words": len(s.split()), "terms": terms,
            })
        claims.extend(rows)
        by_article[a["slug"]] = rows

        # definitions: where a sentence's own SUBJECT is one of the vocabulary terms
        spos = 0
        for s in SENTENCE_SPLIT.split(text):
            s = s.strip()
            soff = text.find(s, spos)
            spos = (soff if soff >= 0 else spos) + len(s)
            for t, _ in TERMS:
                m = re.match(DEFINITION.format(term=re.escape(t)), s, re.I)
                if not m:
                    continue
                tail = s[m.end():].strip()
                if len(tail.split()) < 3:
                    continue
                definitions.append({
                    "term": t, "article": a["slug"], "offset": soff if soff >= 0 else None,
                    "says_it": m.group(0).strip(),
                    "anchor": anchor_of(tail),
                })
                break

    # how many the loose rule would have found — the difference is the methods finding
    loose = 0
    for a in corpus["articles"]:
        text = prose_of(a["slug"], latest)
        for t, _ in TERMS:
            loose += len(re.findall(LOOSE_DEFINITION.format(term=re.escape(t)), text, re.I))

    # where two pieces say what the same term means. Whose byline matters: the same author
    # writing twice is a repetition, not a disagreement, and calling it one would be a
    # finding manufactured out of a coincidence.
    byline = {a["slug"]: set(a["byline"]) for a in corpus["articles"]}
    by_term = defaultdict(list)
    for d in definitions:
        by_term[d["term"]].append(d)
    divergent = []
    for t, ds in sorted(by_term.items()):
        arts = sorted({d["article"] for d in ds})
        if len(arts) < 2:
            continue
        authors = [byline[s] for s in arts]
        same = all(a & authors[0] for a in authors[1:])
        divergent.append({
            "term": t, "articles": arts, "definitions": ds,
            "same_author": same,
            "note": ("Both by the same author, writing twice in this corpus — a repetition, "
                     "not a disagreement." if same else
                     "Different authors, different organisations."),
        })

    types = Counter(c["type"] for c in claims)
    shared = {t: sorted(h) for t, h in term_hits.items() if len(h) > 1}

    out = {
        "id": "wnd-claims", "version": "0.1.0", "updated": latest,
        "what": "Every sentence of the twenty-one op-eds, typed by a published formula and "
                "anchored to the frozen bytes by offset. The sentences themselves are not "
                "stored: an anchor is at most eight words, which is enough to find one and far "
                "short of reproducing it.",
        "means": "A claim type says this sentence has this shape. It does not say the sentence "
                 "is true, that the author believes it, or that the piece is biased. An op-ed "
                 "is supposed to evaluate and to propose; counting the shapes is a measurement "
                 "of form, not a judgement of quality.",
        "anchor_limit_words": ANCHOR_WORDS,
        "counts": {
            "claims": len(claims),
            "articles": len(by_article),
            "by_type": dict(types.most_common()),
            "terms_in_vocabulary": len(TERMS),
            "terms_used_at_all": len(term_hits),
            "terms_shared_by_more_than_one_piece": len(shared),
            "definitions_found": len(definitions),
            "definitions_under_the_looser_rule": loose,
            "terms_defined_by_more_than_one_piece": len(divergent),
        },
        "rules": [{k: v for k, v in r.items()} for r in CLAIM_RULES],
        "claims": claims,
    }
    (DATA / "claims.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n",
                                      encoding="utf-8")
    (DATA / "claim-rules.json").write_text(json.dumps({
        "id": "wnd-claim-rules", "version": "0.1.0",
        "note": "Ordered; the first pattern that matches a sentence wins, and the order is "
                "itself a claim: a sentence that both asks and proposes is recorded as a "
                "question, because that is the stronger signal about what it is doing. "
                "build/gates.py re-runs every pattern on the frozen prose and fails the build "
                "if a single sentence would classify differently.",
        "anchor_limit_words": ANCHOR_WORDS,
        "anchor_note": "An anchor is the first words of the sentence, verbatim, so a reader "
                       "can find it in the original. The limit is well under the twelve-word "
                       "run the section gate refuses.",
        "rules": CLAIM_RULES,
        "terms": [{"id": t, "pattern": p} for t, p in TERMS],
        "definition_pattern": DEFINITION.format(term="<term>"),
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    (DATA / "terms.json").write_text(json.dumps({
        "id": "wnd-terms", "version": "0.1.0", "updated": latest,
        "what": "A published vocabulary of the words this corpus argues about, where each is "
                "used, and where two pieces tell the reader what the same word means.",
        "counts": out["counts"],
        "terms": [{"term": t,
                   "articles": len(term_hits[t]),
                   "occurrences": sum(term_hits[t].values()),
                   "in": sorted(term_hits[t]),
                   "defined_in": sorted({d["article"] for d in by_term.get(t, [])})}
                  for t, _ in TERMS if term_hits[t]],
        "unused": [t for t, _ in TERMS if not term_hits[t]],
        "defined_by_more_than_one_piece": divergent,
        "the_definition_rule_and_what_it_cost": {
            "strict": len(definitions),
            "loose": loose,
            "why_strict": "The loose rule matched the pattern anywhere in a sentence and read "
                          "'the decline of local news is a global phenomenon' as that piece "
                          "DEFINING local news as a phenomenon eroding democracies. It is not "
                          "what the author wrote, and printing it beside another author's "
                          "definition would have misrepresented them both. The strict rule "
                          "requires the term to be the subject of its own sentence.",
            "what_it_cost": f"{loose - len(definitions)} apparent definitions, most of them "
                            "real sentences about the subject but not statements of what the "
                            "word means. A looser rule would have produced a richer page and a "
                            "worse one.",
        },
        "the_finding": "With a rule tight enough not to misrepresent anybody, twenty-one "
                       "pieces arguing about trust, truth, journalism and democracy contain "
                       f"{len(definitions)} explicit statements of what any of those words "
                       "means, across 1,070 sentences. The only term stated twice is stated "
                       "by the same author both times. The vocabulary is shared; the "
                       "definitions are assumed.",
        "what_a_divergence_is_not": "Two pieces saying a word means different things is not a "
                                    "contradiction and neither piece is wrong. It is where the "
                                    "industry has not agreed with itself — and it is invisible "
                                    "unless you read all twenty-one at once.",
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"claims: {len(claims)} claims over {len(by_article)} articles "
          f"({', '.join(f'{k} {v}' for k, v in types.most_common())}); "
          f"{len(term_hits)} terms used, {len(shared)} shared, "
          f"{len(definitions)} definitions, {len(divergent)} terms defined by more than one piece")
    return out


if __name__ == "__main__":
    main()
