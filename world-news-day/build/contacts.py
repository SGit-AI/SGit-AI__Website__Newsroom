#!/usr/bin/env python3
"""world-news-day/ — how to reach them.

    python3 world-news-day/build/contacts.py --fetch    # network: one hop per organisation
    python3 world-news-day/build/contacts.py            # rebuild from the frozen bytes

Twenty-three people wrote these pieces. The user of this section — anyone who wants to
respond to the argument, offer something, or ask a question — needs a way to reach them, and
the corpus itself provides almost none: no author contact, no author URL in the REST record,
no press contact on any of the twenty-one pages. So this file goes and looks, under rules
that are published rather than assumed.

THE RULES, and the reason for each:

 1. **Organisations, not people.** Every address here is an organisation's own published
    role address — press@, info@, contact@ — taken from that organisation's own contact page.
    No personal email, no direct line, no private address, for anybody. Individual routing is
    "via the organisation", because a list of twenty-three journalists' personal addresses on
    a public page is a scraping target, and because several of these people work under
    conditions where that would be worse than rude. The section gate refuses a personal
    contact detail where the data is parsed, not where it is rendered.

 2. **A role address is a published formula**, not a judgement. data/contact-rules.json holds
    the list of local parts that count as organisational, in six languages, and anything else
    found on a page is counted and dropped. The count of what was dropped is published too,
    because a filter nobody can see is a filter nobody can check.

 3. **One hop, from the organisation's own site.** Fetch the home page, find the link the site
    itself labels as contact, fetch that one page, freeze both, hash both. Never guess a URL
    beyond the first candidate, never scrape a directory, never use a third-party database of
    email addresses.

 4. **The domain has to be established, not assumed.** Where the corpus itself links to an
    organisation, that is the domain. Otherwise a candidate is fetched and kept ONLY if the
    organisation's name appears in the bytes that came back. A page that does not name the
    organisation is not that organisation's page, and the entry is recorded as unestablished.

 5. **A failure is a result.** Every organisation we could not reach, and every reason, is on
    the page. The most interesting row in the table is the one with nothing in it.
"""
import argparse
import gzip
import hashlib
import html as _html
import json
import re
import ssl
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urljoin, urlparse

SEC = Path(__file__).resolve().parents[1]
DATA = SEC / "data"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36")

# The candidate home page for each organisation an author's role line names. A candidate is a
# starting point, not a claim: nothing is published from it unless the bytes that come back
# name the organisation (rule 4). Where the corpus itself links to the organisation, the
# domain is taken from the corpus and marked as such.
CANDIDATES = {
    "World Editors Forum": "https://wan-ifra.org/",
    "Globe and Mail": "https://www.theglobeandmail.com/",
    "UNESCO": "https://www.unesco.org/",
    "European Broadcasting Union": "https://www.ebu.ch/",
    "Project Kontinuum": None,
    "Truth Tellers": None,
    "World Association of News Publishers (WAN-IFRA)": "https://wan-ifra.org/",
    "Brazilian Newspaper Association (ANJ)": "https://www.anj.org.br/",
    "Paraluman News": "https://www.myparaluman.ph/",
    "Quint Digital Limited": "https://www.thequint.com/",
    "The Quint": "https://www.thequint.com/",
    "AFP": "https://www.afp.com/",
    "News Corp Australasia": "https://www.newscorpaustralia.com/",
    "Association of Independent Regional Press Publishers of Ukraine": None,
    "ZEG Network": None,
    "Coda Story": "https://codastory.com/",
    "The Atlas": "https://theatlasnewspaper.org/",
    "Informed": None,
    "Haitian Times": "https://haitiantimes.com/",
    "URL Media": "https://urlmedia.com/",
    "The GroundTruth Project": "https://thegroundtruthproject.org/",
    "Fondation Hirondelle": "https://www.hirondelle.org/",
    "confidencial.digital": "https://confidencial.digital/",
    "Daraj.com": "https://daraj.com/",
    "Covering Climate Now": "https://coveringclimatenow.org/",
    "Vocento": "https://www.vocento.com/",
    "World News Day": "https://worldnewsday.org/",
}

# Organisations with no candidate: the reason, stated rather than left as a blank cell.
NO_CANDIDATE = {
    "Project Kontinuum": "A new alliance named only in its founder's role line. No site is "
                         "linked from either piece and none was guessed.",
    "Truth Tellers": "Named in the role line as a summit rather than an organisation with a "
                     "site; nothing in the corpus points at one.",
    "Association of Independent Regional Press Publishers of Ukraine": "The role line gives the "
        "association's name in English only. Guessing a Ukrainian domain from a translated name "
        "is exactly the kind of plausible claim this section refuses.",
    "ZEG Network": "Named in the role line alongside two publications that DO have sites "
                   "(Coda Story, The Atlas); nothing in the corpus points at the network itself.",
    "Informed": "The role line reads 'CEO: Informed' and names nothing else. A common word is "
                "not a domain, and the corpus offers no link.",
}

CONTACT_HINT = re.compile(r"contact|contacto|contacte|contato|contactez|kontakt|impressum|"
                          r"about[-_ ]?us|get[-_ ]in[-_ ]touch|reach[-_ ]us|write[-_ ]to", re.I)
# LinkedIn, but only what an organisation links from its OWN page. Two kinds come back and
# they are treated completely differently — see linkedin_rule on the data file.
LINKEDIN = re.compile(r"https?://(?:[a-z]{2,3}\.)?linkedin\.com/(company|school|in)/"
                      r"([A-Za-z0-9._%\-]+)", re.I)
MAILTO = re.compile(r"mailto:([A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,})", re.I)
INTEXT = re.compile(r"\b([A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,})\b")

RULES = {
    "id": "wnd-contact-rules", "version": "0.1.0",
    "note": "An address is published only if its local part is one of these. Everything else "
            "found on a page is counted and dropped unread. The list is organisational role "
            "names in the languages this corpus spans; it is deliberately conservative, and it "
            "is published so that a reader can see exactly what was let through.",
    "second_rule": "The address's domain must share its second-level label with the site it "
                   "was found on (myparaluman.com beside myparaluman.ph is the same house; "
                   "reportlocal.org on another organisation's page is not). This is what "
                   "removes analytics pseudo-addresses, form placeholders and other people's "
                   "projects, none of which are a way to reach anybody.",
    "storage_rule": "Organisation pages are frozen GZIPPED, because a home page is one to two "
                    "megabytes of script bundle and eleven megabytes of that is payload rather "
                    "than evidence. The SHA-256 recorded is of the ORIGINAL bytes; the gate "
                    "decompresses and re-verifies it, so the anchoring is exactly as strong.",
    "third_rule": "A local part equal to the site's own second-level label counts as a role "
                  "address too — anj@anj.org.br is the association, not a person.",
    "role_local_parts": sorted([
        "info", "information", "contact", "contacts", "contacto", "contato", "contactez",
        "kontakt", "press", "presse", "prensa", "imprensa", "media", "pressoffice",
        "press-office", "media-enquiries", "mediaenquiries", "hello", "hi", "enquiries",
        "inquiries", "enquiry", "general", "office", "mail", "email", "admin", "support",
        "help", "news", "newsroom", "editor", "editors", "editorial", "redaccion",
        "redaccion", "redacao", "redaktion", "comms", "communication", "communications",
        "team", "hey", "ask", "reachus", "webmaster", "secretariat", "secretaria",
        "desk", "submissions", "tips", "letters", "pitches", "correspondence",
    ]),
    "bytes_not_retained_rule": {
        "threshold": 10,
        "what": "A fetched page carrying ten or more addresses that are NOT role addresses is a "
                "directory of people's contact details. Those bytes are not retained: the URL, "
                "the retrieval time, the SHA-256 of what came back and the counts are recorded, "
                "and the file is kept neither in this repository nor in the vault bundle.",
        "why": "The pages are public, so this is not secrecy. It is that freezing a staff "
               "directory into a git repository and shipping it in a downloadable bundle makes "
               "it materially easier to scrape than the publisher made it, which is not a thing "
               "this section will do to twenty-three colleagues. The hash is kept so that anyone "
               "can re-fetch the page and check our count against it.",
        "cost": "A real cost, stated rather than hidden: for a page held this way the count is "
                "an assertion about bytes we no longer have, not a number a reader can "
                "re-derive from this repository.",
    },
    "linkedin_rule": {
        "company_and_school_pages": "Published when the organisation links to it from its own "
                                    "frozen page. A LinkedIn company page is a public corporate "
                                    "profile and a route, like a contact page.",
        "personal_profiles": "Published ONLY when the profile slug matches the name of an "
                             "author in this corpus, letter for letter once punctuation is "
                             "removed. Everything else is dropped unread. The rule exists "
                             "because a site template ships stock profiles: three of the four "
                             "/in/ links on one organisation's page belong to people with "
                             "nothing to do with it, and publishing them as that newsroom's "
                             "staff would have been a fabrication.",
        "what_a_profile_link_is": "A public professional page, which is a route, not a contact "
                                  "detail. It is not permission to message anybody about "
                                  "anything.",
    },
    "never_published": "Any address whose local part is not on this list — including anything "
                       "that could be a person's name. No personal contact detail for any "
                       "natural person appears anywhere in this section's data.",
}


def fetch_one(url, timeout=20):
    """Python first, curl second. Three of these sites refused Python's client and served the
    same page to curl with the same user-agent — a difference in TLS handshake, not in
    intent. Which client got the bytes is recorded on the entry, because "we could not read
    it" and "our first client could not read it" are different claims."""
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-GB,en;q=0.9",
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ssl.create_default_context()) as r:
            return r.getcode(), r.geturl(), r.read(), "urllib"
    except Exception:
        pass
    out = subprocess.run(
        ["curl", "-sSL", "--max-time", str(timeout), "-A", UA,
         "-w", "\n%{http_code} %{url_effective}", url],
        capture_output=True)
    if out.returncode != 0:
        raise RuntimeError(f"curl exit {out.returncode}")
    body, _, tail = out.stdout.rpartition(b"\n")
    code, _, final = tail.decode().partition(" ")
    return int(code), final.strip(), body, "curl"


def slugify(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-") or "unnamed"


def keep_bytes(out, name, body, entry, which):
    """Freeze the page — unless it is a directory of people's contact details.

    See contact-rules.json. Ten or more non-role addresses on one page and the bytes are not
    retained. The Globe and Mail's contact page is the case this exists for: it publishes the
    direct address of seventy-nine named journalists. Those pages are public, so this is not
    secrecy; it is that freezing a staff directory into a git repository and shipping it in a
    downloadable bundle makes it materially easier to scrape than the publisher made it. The
    hash of what came back is kept, so the count can be checked by re-fetching."""
    text = body.decode("utf-8", "replace")
    found = {m.lower() for m in MAILTO.findall(text)} | {m.lower() for m in INTEXT.findall(text)}
    role = set(RULES["role_local_parts"])
    personal = sorted(a for a in found if a.partition("@")[0] not in role)
    if len(personal) >= RULES["bytes_not_retained_rule"]["threshold"]:
        entry[f"{which}_bytes_not_retained"] = {
            "sha256": hashlib.sha256(body).hexdigest(), "bytes": len(body),
            "addresses_on_the_page": len(found), "not_role_addresses": len(personal),
            "why": "A directory of people's contact details. See data/contact-rules.json.",
        }
        f = out / name
        if f.exists():
            f.unlink()
        print(f"    (bytes not retained: {len(personal)} addresses that are not role addresses)")
        return False
    # Stored gzipped. An organisation's home page is one to two megabytes of script bundle,
    # and eleven megabytes of that is payload rather than evidence. The SHA-256 recorded is of
    # the ORIGINAL bytes, not of the compression — the gate decompresses and re-verifies it, so
    # the anchoring is exactly as strong and the repository is a fifth of the size.
    entry[f"{which}_sha256"] = hashlib.sha256(body).hexdigest()
    entry[f"{which}_bytes"] = len(body)
    with gzip.GzipFile(filename="", mode="wb", fileobj=open(out / (name + ".gz"), "wb"),
                       mtime=0) as z:
        z.write(body)
    stale = out / name
    if stale.exists():
        stale.unlink()
    return True


def fetch(date):
    """One hop per organisation: the home page, then the one link the site itself labels as
    contact. Both frozen. Nothing else is requested."""
    out = SEC / "sources" / "frozen" / date / "orgs"
    out.mkdir(parents=True, exist_ok=True)
    log = []
    for org, url in CANDIDATES.items():
        sl = slugify(org)
        if not url:
            log.append({"org": org, "state": "no candidate"})
            continue
        try:
            code, final, body, how = fetch_one(url)
        except urllib.error.HTTPError as e:
            log.append({"org": org, "url": url, "state": f"HTTP {e.code}"})
            print(f"  ! {org}: HTTP {e.code}")
            continue
        except Exception as e:
            log.append({"org": org, "url": url, "state": type(e).__name__})
            print(f"  ! {org}: {type(e).__name__}")
            continue
        if code >= 400 or (code == 307 and len(body) < 4000):
            log.append({"org": org, "url": url, "state": f"HTTP {code}", "client": how,
                        "body_bytes": len(body),
                        "sha256": hashlib.sha256(body).hexdigest()})
            print(f"  ! {org}: HTTP {code} ({len(body)} bytes, {how})")
            continue
        entry = {"org": org, "url": url, "final": final, "state": f"HTTP {code}", "client": how}
        if keep_bytes(out, f"{sl}.snapshot", body, entry, "home"):
            entry["home"] = f"orgs/{sl}.snapshot.gz"
        text = body.decode("utf-8", "replace")
        # the link the SITE labels as contact — its word, not ours
        best = None
        for m in re.finditer(r'<a[^>]+href="([^"#]+)"[^>]*>(.*?)</a>', text, re.S | re.I):
            href, label = m.group(1), re.sub(r"<[^>]+>", " ", m.group(2))
            if CONTACT_HINT.search(label) or CONTACT_HINT.search(href):
                cand = urljoin(final, href)
                if urlparse(cand).netloc.replace("www.", "") == urlparse(final).netloc.replace("www.", ""):
                    best = cand
                    break
        if best:
            try:
                c2, f2, b2, how2 = fetch_one(best)
                entry.update({"contact_url": f2, "contact_state": f"HTTP {c2}",
                              "contact_client": how2})
                if keep_bytes(out, f"{sl}-contact.snapshot", b2, entry, "contact"):
                    entry["contact"] = f"orgs/{sl}-contact.snapshot.gz"
            except Exception as e:
                entry["contact_state"] = f"{type(e).__name__} on {best}"
        log.append(entry)
        print(f"  · {org}: {code} {'+contact' if best else ''}")
    (out / "fetch-log.json").write_text(json.dumps(log, indent=2, ensure_ascii=False) + "\n",
                                        encoding="utf-8")
    print(f"contacts fetch: {sum(1 for l in log if l.get('home'))} home pages, "
          f"{sum(1 for l in log if l.get('contact'))} contact pages")


# ------------------------------------------------------------------ build ---
def second_level(host):
    parts = host.lower().replace("www.", "").split(".")
    # co.uk, org.br, org.ua and friends: the label that identifies the house is the one
    # before a two-letter country code preceded by a short public suffix
    if len(parts) >= 3 and len(parts[-1]) == 2 and parts[-2] in {"co", "com", "org", "net", "gov", "ac"}:
        return parts[-3]
    return parts[-2] if len(parts) >= 2 else parts[0]


def build():
    register = json.loads((DATA / "register.json").read_text(encoding="utf-8"))
    corpus = json.loads((DATA / "corpus.json").read_text(encoding="utf-8"))
    aff = json.loads((DATA / "affiliations.json").read_text(encoding="utf-8"))
    latest = register["snapshots"][-1]
    froot = SEC / "sources" / "frozen" / latest
    log = json.loads((froot / "orgs" / "fetch-log.json").read_text(encoding="utf-8"))
    by_org = {e["org"]: e for e in log}

    ROLE = set(RULES["role_local_parts"])
    # the domains the corpus itself points at — an established domain rather than a candidate
    corpus_domains = {re.sub(r"^www\.", "", urlparse(l).netloc).lower()
                      for a in corpus["articles"] for l in a["outbound_links"]}

    author_flat = {r["author"]: re.sub(r"[^a-z0-9]", "", r["author"].lower())
                   for r in aff["people"]}
    authors_of = {}
    for r in aff["people"]:
        for o in r["organisations"]:
            authors_of.setdefault(o, []).append(r["author"])

    orgs, dropped_total, addr_total = [], 0, 0
    for org in CANDIDATES:
        sl = slugify(org)
        e = by_org.get(org, {})
        row = {"org": org, "slug": sl, "authors": sorted(authors_of.get(org, [])),
               "candidate": CANDIDATES[org], "state": e.get("state", "no candidate"),
               "client": e.get("client"), "frozen": [], "addresses": [], "dropped": 0}
        if not CANDIDATES[org]:
            row["why_none"] = NO_CANDIDATE.get(org, "No site is named or linked anywhere in the corpus.")
            orgs.append(row)
            continue
        for which in ("home", "contact"):
            if e.get(f"{which}_bytes_not_retained"):
                row.setdefault("bytes_not_retained", {})[which] = e[f"{which}_bytes_not_retained"]
        if not e.get("home") and not e.get("contact") and not row.get("bytes_not_retained"):
            row["why_none"] = (f"The organisation's own site answered {e.get('state', 'nothing')} "
                               f"to an automated reader, so nothing could be read from it.")
            row["body_bytes"] = e.get("body_bytes")
            row["fetched_sha256"] = e.get("sha256")
            orgs.append(row)
            continue
        if not e.get("home") and not e.get("contact"):
            row["site"] = e.get("final")
            row["contact_page"] = e.get("contact_url")
            row["domain"] = re.sub(r"^www\.", "", urlparse(e.get("final") or CANDIDATES[org]).netloc).lower()
            row["established"] = "fetched, and the bytes deliberately not retained"
            row["why_none"] = ("Every page fetched for this organisation is a directory of named "
                               "people's contact details, so the bytes were not kept and no "
                               "address from them is published. See data/contact-rules.json.")
            orgs.append(row)
            continue

        pages, text = [], ""
        for k in ("home", "contact"):
            if e.get(k):
                f = froot / e[k]
                raw = gzip.decompress(f.read_bytes())
                pages.append({"role": k, "path": f"sources/frozen/{latest}/{e[k]}",
                              "stored_bytes": f.stat().st_size,
                              "bytes": len(raw),
                              "sha256": hashlib.sha256(raw).hexdigest(),
                              "note": "Stored gzipped; the SHA-256 is of the original bytes."})
                text += raw.decode("utf-8", "replace")
        row["frozen"] = pages
        row["site"] = e.get("final")
        row["contact_page"] = e.get("contact_url")
        host = urlparse(e.get("final") or CANDIDATES[org]).netloc
        row["domain"] = re.sub(r"^www\.", "", host).lower()
        row["established"] = ("the corpus links to it" if row["domain"] in corpus_domains
                              else "the page that came back names the organisation")

        # RULE 4, in full: a page that does not name the organisation is not that
        # organisation's page. Four ways to establish it, all published, all checkable:
        #   (a) the corpus itself links to the domain;
        #   (b) the organisation's name is in the page, with "the" and any parenthetical dropped;
        #   (c) the acronym the role line gives in brackets is in the page — anj.org.br is in
        #       Portuguese and never says "Brazilian Newspaper Association";
        #   (d) the domain's own label is in the page AND inside the organisation's name —
        #       daraj.media for "Daraj.com".
        # Anything else stays UNESTABLISHED, with the candidate and the reason on the record.
        # "News Corp Australasia" fails all four because the site says News Corp Australia:
        # close is not the same, and a contacts list is exactly where close is dangerous.
        plain = " ".join(_html.unescape(re.sub(r"<[^>]+>", " ", text)).split()).lower()
        bare = re.sub(r"\s*\(.*?\)\s*", " ", org).strip().lower()
        acronym = (re.search(r"\(([^)]{2,12})\)", org) or [None, ""])[1].strip()
        label = second_level(row["domain"])
        flat = re.sub(r"[^a-z0-9]", "", org.lower())
        how = None
        if row["domain"] in corpus_domains:
            how = "the corpus itself links to this domain"
        elif bare in plain or bare.replace("the ", "") in plain:
            how = "the page that came back names the organisation"
        elif acronym and re.search(r"\b" + re.escape(acronym.lower()) + r"\b", plain):
            how = f"the page that came back carries the acronym the role line gives ({acronym})"
        elif label in plain and label in flat:
            how = f"the page that came back and the organisation's name share the label '{label}'"
        row["established"] = how
        if not how:
            row["why_none"] = ("The page that came back does not name the organisation by any of "
                               "the four published tests, so it is kept as a candidate and "
                               "nothing is published from it.")
            orgs.append(row)
            continue

        # LinkedIn, by the published rule: company pages as the organisation offers them,
        # personal profiles only where the slug IS an author of this corpus.
        org_li, person_li, li_dropped = [], [], 0
        for kind, handle in LINKEDIN.findall(text):
            url = f"https://www.linkedin.com/{kind.lower()}/{handle}"
            if kind.lower() in ("company", "school"):
                if url not in org_li:
                    org_li.append(url)
                continue
            flat_handle = re.sub(r"[^a-z0-9]", "", handle.lower())
            who = next((a for a, fl in author_flat.items() if fl == flat_handle), None)
            if who:
                rec = {"author": who, "url": url}
                if rec not in person_li:
                    person_li.append(rec)
            else:
                li_dropped += 1
        row["linkedin"], row["linkedin_people"] = org_li, person_li
        row["linkedin_dropped"] = li_dropped

        found = {m.lower() for m in MAILTO.findall(text)} | {m.lower() for m in INTEXT.findall(text)}
        keep, drop = [], 0
        for a in sorted(found):
            local, _, dom = a.partition("@")
            if second_level(dom) != label:
                drop += 1
                continue
            if local in ROLE or local == label:
                keep.append(a)
            else:
                drop += 1
        row["addresses"], row["dropped"] = keep, drop
        dropped_total += drop
        addr_total += len(keep)
        orgs.append(row)

    reachable = {o["org"] for o in orgs
                 if o["addresses"] or o.get("contact_page") or o.get("linkedin")}
    out = {
        "id": "wnd-contacts", "version": "0.1.0", "updated": latest,
        "question": "Twenty-three people wrote these pieces. How do you reach them — and what "
                    "does the corpus itself give you to do it with?",
        "rules": "data/contact-rules.json. Organisations, not people; a published list of role "
                 "local parts; one hop from the organisation's own site; the domain has to be "
                 "established, not assumed; and a failure is a result.",
        "from_the_corpus_alone": {
            "pieces": corpus["count"],
            "carrying_an_author_contact": 0,
            "carrying_an_author_url_in_the_rest_record": 0,
            "carrying_any_press_or_general_contact": 0,
            "note": ("Not one of the twenty-one pages offers a way to reach its author or the "
                     "publisher. The REST record has an author field but no author URL. "
                     "Everything below had to be found by going to the organisations' own "
                     "sites — which is the point: a corpus published to be spread carries no "
                     "route back to the people who wrote it."),
        },
        "counts": {
            "organisations": len(orgs),
            "with_an_established_site": sum(1 for o in orgs if o.get("established")),
            "with_a_contact_page": sum(1 for o in orgs if o.get("contact_page")),
            "with_a_publishable_role_address": sum(1 for o in orgs if o["addresses"]),
            "role_addresses_published": addr_total,
            "addresses_found_and_dropped": dropped_total,
            "with_no_route_at_all": len(orgs) - len(reachable),
            "with_a_linkedin_page": sum(1 for o in orgs if o.get("linkedin")),
            "author_profiles_established": sum(len(o.get("linkedin_people", [])) for o in orgs),
            "linkedin_profiles_found_and_dropped": sum(o.get("linkedin_dropped", 0) for o in orgs),
            "authors": aff["count"],
            "authors_reachable_via_an_organisation":
                sum(1 for r in aff["people"] if any(o in reachable for o in r["organisations"])),
        },
        "organisations": orgs,
        "authors": [{"author": r["author"], "organisations": r["organisations"],
                     "route": ("via " + ", ".join(r["organisations"])) if r["organisations"]
                              else "no current organisation in the role line — no route",
                     "reachable": any(o in reachable for o in r["organisations"])}
                    for r in aff["people"]],
        "refuses": [
            "No personal email address, direct line or private address for any named person.",
            "No third-party contact database, no directory scrape, no pattern-guessed address.",
            "Nothing inferred: an address is published only if it is in bytes we froze and "
            "hashed, and only if the published rules let it through.",
        ],
    }
    (DATA / "contacts.json").write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n",
                                        encoding="utf-8")
    (DATA / "contact-rules.json").write_text(json.dumps(RULES, indent=2, ensure_ascii=False) + "\n",
                                             encoding="utf-8")
    c = out["counts"]
    print(f"contacts: {c['organisations']} organisations, {c['with_an_established_site']} established, "
          f"{c['with_a_contact_page']} with a contact page, {c['role_addresses_published']} role "
          f"addresses published, {c['addresses_found_and_dropped']} dropped, "
          f"{c['with_a_linkedin_page']} with LinkedIn, "
          f"{c['authors_reachable_via_an_organisation']}/{c['authors']} authors reachable")
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--fetch", action="store_true")
    ap.add_argument("--date", default=None)
    a = ap.parse_args()
    if a.fetch:
        d = a.date or json.loads((DATA / "register.json").read_text())["snapshots"][-1]
        fetch(d)
        build()
    else:
        build()
