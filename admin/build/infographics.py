#!/usr/bin/env python3
"""Infographics for the wires: one card per story and one hero per edition, made by an image model through the SGraph
infographic generator (dev.tools.sgraph.ai), driven from Python with Playwright.

    python3 admin/build/infographics.py --check                                   # is the tool's API live? methods, version, models; no key
    python3 admin/build/infographics.py --wire industry --from <clone> --dry-run    # the prompts and the plan, nothing spent
    python3 admin/build/infographics.py --wire owasp --from <clone> [--edition YYYY-MM-DD] [--stories id,id]
                                        [--max-images N] [--max-cost USD] [--out DIR]

THE KEY. The OpenRouter key is read from the environment variable OPENROUTER_API_KEY and from nowhere else: never a file,
never an argument. It is handed to the tool's connect() as a Playwright argument, not written into a script string, and
it is never printed, never put in a prompt file and never put in a ledger. With no key in the environment the run is a
dry run whether or not --dry-run was given: it writes the prompts and the plan and spends nothing.

WHAT IT MAKES. For the edition (the brief's, or --edition) of one wire (--wire industry, or a slug such as owasp, with
--from a clone of its vault), first a landscape 16:9 "what's going on" hero from the editor's note, the lead and the
threads, with the stories' ids as small labels; then one portrait 4:5 card per story: the headline, the date, the primary
source's publisher and its licence tier, one key number only when the summary holds one (quoted verbatim), and the beat.
The stories are --stories when given, else the ones the edition added (brief.new_in_edition), else every story that
carries that edition, else every story.

SQUARE. The tool's generate() takes a prompt and a model and nothing about size: every model behind it returns a
1024 by 1024 image (the first live run, 14 October 2026, asked for 16:9 and got a square). So the prompts ask for a
square and lay the card out for one: the headline in the top two thirds, the four facts under a rule; a ratio the
prompt names and the model ignores would only make the disclosure untrue. The bake-off's first rule still holds: the
format by name, never the platform.

THE PROMPT RULES, from articles/the-infographic-bake-off.md: never name the platform; end with "No other text."; say
"no numbers other than those given"; keep hex codes, type sizes and separators out of any text to be drawn; and attach
the first image to the later ones for consistency, so the edition's hero is attached to every card as the style
reference when the tool offers its image input. The model per job started from the bake-off: a card is a concept slide,
so the cheap model (Nano Banana 2.1); the hero starts from a document, so GPT-5.4 Image 2. The first live run (14 October
2026) changed the card's model: Nano Banana 2.1 was rate-limited upstream for everyone, and the fallback, Gemini 3.1 Flash
Image, misspelt two headlines in two cards ("patch paph", "IoT T devices"); a card whose headline is not exact breaks the
rule the design note sets, so Gemini 3 Pro Image (about 0.14 USD, every word exact in the probe) is now first for cards,
with the cheaper ids behind it. The ids are not hard-coded:
at run time the script reads the model ids the tool's own skill files list and takes the first that matches each
preference, falling back to the tool's default model when none is offered.

IDEMPOTENT. An image is keyed by wire, edition, story id (or "edition") and the sha256 of its prompt; a key the ledger
already holds, with its file on disk, is skipped, so a second run after a correction remakes only the stories whose text
changed. Output: wire/<slug>/infographics/<edition>/<story-or-edition>.<hash8>.webp (PNG when Pillow is missing),
prompts/<key>.txt beside them, and ledger.json: per image the key, kind, model, generationId, duration, cost (queried
from OpenRouter fifteen seconds after the last generation, as the tool's skill shows), the prompt's sha256 and file;
totals for the edition. wire/<slug>/infographics/ledger.json sums every edition's ledger by month. --max-images and
--max-cost stop the run cleanly, ledger written; the cost cap counts the bake-off's prices per job before each image,
since the real cost is only known afterwards, and the ledger then carries the real figure.

THE MORNING ROUTINE. The desk brief asks the desks to publish at seven (London). After a desk has published and wire.py
has refreshed the snapshot, the newsroom's run calls, for each wire,

    OPENROUTER_API_KEY=... python3 admin/build/infographics.py --wire <slug> --from <clone> --max-images 40 --max-cost 2.00

with the key in the environment of that step only. It makes the hero, then a card for each story the release added,
skips what exists, writes the ledgers and stops at either cap; a wire whose edition did not change makes nothing. The
images and ledgers are committed with the release like the snapshot is. Nothing on the pages reads them yet: showing a
card beside its story is a later card on the board, once the first editions' images have been looked at.

PLAYWRIGHT FROM PYTHON. The script needs the playwright package (pip install playwright==1.56.0 in a venv) and a
Chromium; PLAYWRIGHT_BROWSERS_PATH names a shared install (/opt/pw-browsers in the build sessions). Chromium ignores
HTTPS_PROXY, so the proxy is passed to it from that variable as the skill's helper does; the CA bundle for Python's own
request to OpenRouter is /root/.ccr/ca-bundle.crt when it exists; and in a sandbox whose TLS is intercepted,
CHROMIUM_SPKI_ALLOW (as test_wire.mjs uses it) is passed to Chromium so it trusts that one key and nothing else.
"""
import argparse
import base64
import hashlib
import io
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote, urlparse

ROOT = Path(__file__).resolve().parents[2]
BUILD = ROOT / "admin/build"
TOOL_URL = "https://dev.tools.sgraph.ai/en-gb/infographic-gen/"
OPENROUTER_GENERATION = "https://openrouter.ai/api/v1/generation?id="
CA_BUNDLE = Path("/root/.ccr/ca-bundle.crt")
PRICE_SOURCE = "OpenRouter's own figures on the first live run of 14 October 2026 (the bake-off article, 10 October, had 0.039 and 0.176 for Nano Banana 2.1 and GPT-5.4 Image 2)"
PRICES = {"card": 0.14, "hero": 0.245}           # price per image as OpenRouter billed the first live run (14 October 2026: a card on
                                                  # Gemini 3 Pro Image, a hero on GPT-5.4 Image 2); the bake-off's table said 0.039 and
                                                  # 0.176 for Nano Banana 2.1 and GPT-5.4 Image 2. The cap is counted in these.
# the model per job, as the bake-off's guidance names them; matched, in this order, against the ids the tool's own skill
# files list at run time, then against OpenRouter's public catalogue of image-output models (no key needed), else the
# tool's default. On 13 October 2026 the tool's files named three ids and none of these; the catalogue named both.
MODEL_PREFS = {"card": ["gemini-3-pro-image", "nano-banana-2.1", "gemini-3.1-flash-image", "nano-banana"],
               "hero": ["gpt-5.4-image-2", "gpt-5.4-image", "gpt-5-image"]}
OPENROUTER_MODELS = "https://openrouter.ai/api/v1/models"
TEMPLATES = {"card": "executive", "hero": "executive"}
SETTLE_S = 15                                     # OpenRouter's accounting settles after the generation; the skill waits this long
PAUSE_S = 6                                       # between two generations, so a batch is not a burst
RETRY_WAITS_S = (20, 45, 90)                      # after an HTTP 429 or a 5xx from the tool or the model: wait, then try again, three times
MAX_FAILURES_IN_A_ROW = 3                         # then the run stops: a storm of refusals is not a reason to work through the plan
SAFE_ID = re.compile(r"[^A-Za-z0-9_-]")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
# a key number in a summary: money of three figures or more or with a magnitude word (a bare "$4" is a unit price, not a
# figure), a percentage, a size, a CVSS score, a count with its noun; the first match is quoted as written
KEY_NUMBER = re.compile(
    r"(?:(?:US)?\$|€|£)\s?(?:\d{1,3}(?:,\d{3})+|\d{3,})(?:\.\d+)?\s?(?:million|billion|trillion|bn|m|k|M)?\b"
    r"|(?:(?:US)?\$|€|£)\s?\d[\d.]*\s?(?:million|billion|trillion|bn|m|k|M)\b"
    r"|\b\d[\d,.]*\s?(?:%|percent|GB|TB|MB|GW|MW|million|billion|bn|thousand)\b"
    r"|\bCVSS\s?\d+(?:\.\d+)?\b"
    r"|\b\d{1,3}(?:,\d{3})+\b(?:\s+[A-Za-z]+){0,2}"
    r"|\b\d+\s+(?:exploitation attempts|attempts|people|sites|municipalities|projects|organisations|companies|functions|seats|members|participants|"
    r"stories|CVEs|vulnerabilities|devices|accounts|customers|users|agents|regions|services|days|weeks|months|years)\b")
# the words that may follow a count: not these, which begin the rest of the sentence
NOT_A_NOUN = {"and", "per", "across", "of", "in", "on", "to", "the", "for", "from", "with", "by", "at", "or", "as", "is", "was", "were", "that", "its", "their", "has", "have", "had", "are", "but", "than", "more", "over", "under", "about"}


def say(*parts):
    print("infographics:", *parts, flush=True)


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ------------------------------------------------------------------ the wire and its bundle
def wire_dir(slug):
    return "wire/" + (slug + "/" if slug else "")


def wire_name(slug, bundle):
    cfg = BUILD / ("wire-vault.json" if not slug else f"wire-vault.{slug}.json")
    if cfg.exists():
        try:
            return json.loads(cfg.read_text(encoding="utf-8")).get("name") or (slug or "The Industry Wire")
        except (OSError, ValueError):
            pass
    meta = bundle.get("wire") if isinstance(bundle.get("wire"), dict) else {}
    return meta.get("title") or ("The Industry Wire" if not slug else f"The {slug} wire")


def load_bundle(clone: Path):
    f = clone / "data/bundle.json"
    if not f.exists():
        raise SystemExit(f"infographics: {clone} has no data/bundle.json; --from must name a clone of the wire's vault")
    b = json.loads(f.read_text(encoding="utf-8"))
    if not isinstance(b, dict) or not isinstance(b.get("stories"), list):
        raise SystemExit("infographics: data/bundle.json has no stories list")
    return b


def pick_stories(bundle, edition, wanted):
    """The stories to draw: --stories, else what the edition added, else the stories of that edition, else all."""
    stories = [s for s in bundle["stories"] if isinstance(s, dict) and s.get("id")]
    by_id = {s["id"]: s for s in stories}
    brief = bundle.get("brief") if isinstance(bundle.get("brief"), dict) else {}
    if wanted:
        missing = [i for i in wanted if i not in by_id]
        if missing:
            say(f"not in the bundle, skipped: {', '.join(missing)}")
        return [by_id[i] for i in wanted if i in by_id], "named with --stories"
    if edition == brief.get("edition") and brief.get("new_in_edition"):
        ids = [i for i in brief["new_in_edition"] if i in by_id]
        if ids:
            return [by_id[i] for i in ids], "added by this edition (brief.new_in_edition)"
    of_edition = [s for s in stories if s.get("edition") == edition]
    if of_edition:
        return of_edition, f"carrying edition {edition}"
    return stories, "every story in the bundle (none carries an edition)"


# ------------------------------------------------------------------ the prompts
def clean(text, limit=None):
    """Prose for a prompt: one line, no hex codes or type sizes (rule 4: they get drawn), trimmed to a limit at a word."""
    t = re.sub(r"\s+", " ", str(text or "")).strip()
    t = re.sub(r"#[0-9a-fA-F]{3,8}\b", "", t)
    t = re.sub(r"\b\d+(?:\.\d+)?\s?(?:pt|px)\b", "", t)
    if limit and len(t) > limit:
        t = t[:limit].rsplit(" ", 1)[0].rstrip(",;:") + "…"
    return t


def key_number(summary):
    """The first key number in a summary, verbatim, with the words after a count kept only while they are its noun."""
    m = KEY_NUMBER.search(str(summary or ""))
    if not m:
        return ""
    tokens = m.group(0).strip().rstrip(".,;:").split()
    out = [tokens[0]]
    for t in tokens[1:]:
        if t.isalpha() and t.islower() and (len(t) < 3 or t in NOT_A_NOUN):    # a unit (GW, GB, CVSS) is upper case and always kept
            break
        out.append(t)
    return " ".join(out).rstrip(".,;:")


STYLE = ("Style: a clean editorial print look on a light paper background, one dark teal accent and black ink, generous margins, "
         "a thin rule under the headline, flat shapes, no gradients, no photographs, no people, no logos, no icons of any brand.")
RULES = "Use no numbers other than those given. Do not invent a source, a date, a figure or a name. No other text."


def card_prompt(story, wire, beat_label, edition):
    p = story.get("primary") if isinstance(story.get("primary"), dict) else {}
    tier = p.get("tier") if p.get("tier") in ("A", "B", "C") else None
    date = story.get("date") if DATE.match(str(story.get("date") or "")) else "date not given"
    number = key_number(story.get("summary"))
    lines = [f'Square news card for a daily wire called "{clean(wire, 60)}", edition of {edition}: one story, as text, laid out as a card that fills the whole square, paper edge to edge: no frame, no border, no background around it, no icons, no illustration.',
             "Draw exactly these lines and nothing else:",
             f'Headline: "{clean(story.get("headline"), 220) or "untitled"}"',
             f"Date: {date}",
             f"Source: {clean(p.get('publisher'), 80) or 'not given'}, licence tier {tier if tier else 'not in the registry'}"]
    if number:
        lines.append(f'Key number: "{number}"')
    lines.append(f"Beat: {clean(beat_label, 60) or 'general'}")
    lines.append("The headline is the largest text, the key number the second largest when there is one; the date, the source and the beat are small and set under a rule.")
    lines.append(STYLE)
    lines.append("Match the attached image's palette and type when one is attached.")
    lines.append(RULES)
    return "\n".join(lines)


def hero_prompt(bundle, wire, edition, by_id):
    brief = bundle.get("brief") if isinstance(bundle.get("brief"), dict) else {}
    lead = brief.get("lead") if isinstance(brief.get("lead"), dict) else {}
    lead_story = by_id.get(lead.get("story")) or {}
    doc = [f"Editor's note: {clean(brief.get('editor_note'), 900) or 'none written'}"]
    if lead_story:
        doc.append(f'The lead ({lead_story.get("id")}): "{clean(lead_story.get("headline"), 200)}". Why it leads: {clean(lead.get("why_it_leads"), 300)}')
    threads = [t for t in (brief.get("threads") or []) if isinstance(t, dict)]
    for i, t in enumerate(threads[:5], 1):
        ids = [str(x) for x in (t.get("stories") or []) if isinstance(x, str) and x in by_id]
        doc.append(f"Thread {i}: {clean(t.get('title'), 80) or t.get('id') or 'untitled'} ({', '.join(ids) or 'no stories'}): {clean(t.get('note'), 260)}")
    lines = [f'Square overview infographic titled "{clean(wire, 60)}: what is going on, edition of {edition}".',
             "Here is the editor's brief as a document. Draw the picture of it:",
             "---", *doc, "---",
             "Layout: the title across the top; the lead as the largest panel on the left with its headline and its story id as a small label; "
             "one panel per thread to its right, each with the thread's title, a one-line gist taken from its words, and its story ids as small labels in a monospaced style; "
             "a short strip along the bottom with the editor's note in the editor's own words, shortened as needed, never reworded into claims the note does not make.",
             STYLE, "Draw the story ids exactly as written.", RULES]
    return "\n".join(lines)


# ------------------------------------------------------------------ the plan: keys, files, what exists
def sha256(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def plan_jobs(slug, bundle, edition, stories, out_dir: Path, ledger):
    wire = wire_name(slug, bundle)
    by_id = {s["id"]: s for s in bundle["stories"] if isinstance(s, dict) and s.get("id")}
    beat_label = {b.get("id"): b.get("label") for b in (bundle.get("beats") or []) if isinstance(b, dict)}
    done = {e["key"]: e for e in ledger.get("images", []) if e.get("status") == "done" and e.get("key")}
    wire_key = slug or "industry"
    jobs = []

    def job(kind, sid, prompt):
        h = sha256(prompt)
        key = f"{wire_key}.{edition}.{SAFE_ID.sub('_', sid)}.{h[:8]}"
        prior = done.get(key)
        exists = bool(prior and prior.get("file") and (out_dir / prior["file"]).exists())
        jobs.append({"key": key, "kind": kind, "id": sid, "prompt": prompt, "prompt_sha256": h, "prompt_file": f"prompts/{key}.txt",
                     "exists": exists, "estimated_cost_usd": 0.0 if exists else PRICES[kind]})

    job("hero", "edition", hero_prompt(bundle, wire, edition, by_id))
    for s in stories:
        job("card", s["id"], card_prompt(s, wire, beat_label.get(s.get("beat")) or s.get("beat") or "", edition))
    return wire, jobs


def write_prompts(jobs, out_dir: Path):
    (out_dir / "prompts").mkdir(parents=True, exist_ok=True)
    n = 0
    for j in jobs:
        f = out_dir / j["prompt_file"]
        if not f.exists() or f.read_text(encoding="utf-8") != j["prompt"] + "\n":
            f.write_text(j["prompt"] + "\n", encoding="utf-8")
            n += 1
    return n


# ------------------------------------------------------------------ the ledgers
def load_json(f: Path, default):
    try:
        return json.loads(f.read_text(encoding="utf-8")) if f.exists() else default
    except ValueError:
        return default


def write_json(f: Path, data):
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


def write_ledgers(slug, edition, out_dir: Path, wire_root: Path, ledger, entries, stopped=None, budget=None):
    """The edition's ledger (entries merged by key, newest state wins) and the wire's cumulative ledger, summed by month."""
    by_key = {e["key"]: e for e in ledger.get("images", []) if e.get("key")}
    for e in entries:
        by_key[e["key"]] = e
    images = sorted(by_key.values(), key=lambda e: (e.get("kind") != "hero", e.get("id", ""), e.get("key", "")))
    done = [e for e in images if e.get("status") == "done"]
    ledger.update({
        "schema": "wire-infographics/v1", "wire": slug or "industry", "edition": edition, "updated": now_iso(),
        "prices": {"what": "the estimate per job before an image is made; the cost on each image is OpenRouter's own figure", "source": PRICE_SOURCE, "per_image_usd": PRICES},
        "images": images,
        "totals": {"images": len(done), "failed": sum(1 for e in images if e.get("status") == "failed"), "cost_usd": round(sum(e.get("cost_usd") or 0 for e in done), 6),
                   "duration_s": round(sum(e.get("duration_s") or 0 for e in done), 1), "cost_unknown": sum(1 for e in done if e.get("cost_usd") is None)},
    })
    if stopped:
        ledger["stopped"] = stopped
    elif "stopped" in ledger:
        del ledger["stopped"]
    write_json(out_dir / "ledger.json", ledger)
    # the cumulative ledger: every edition under the wire's infographics folder, summed per month of the image's time
    months, editions = {}, {}
    for f in sorted(wire_root.glob("*/ledger.json")):
        led = load_json(f, {})
        ed = led.get("edition") or f.parent.name
        t = led.get("totals") or {}
        editions[ed] = {"images": t.get("images", 0), "cost_usd": t.get("cost_usd", 0.0), "failed": t.get("failed", 0)}
        for e in led.get("images", []):
            if e.get("status") != "done":
                continue
            m = str(e.get("at") or "")[:7] or "unknown"
            row = months.setdefault(m, {"images": 0, "cost_usd": 0.0, "duration_s": 0.0})
            row["images"] += 1
            row["cost_usd"] = round(row["cost_usd"] + (e.get("cost_usd") or 0), 6)
            row["duration_s"] = round(row["duration_s"] + (e.get("duration_s") or 0), 1)
    if not budget:
        budget = (load_json(wire_root / "ledger.json", {}) or {}).get("key_budget")   # a dry run keeps the last live run's figure
    write_json(wire_root / "ledger.json", {
        "schema": "wire-infographics-total/v1", "wire": slug or "industry", "updated": now_iso(),
        "what": "Every infographic made for this wire, summed by month and by edition from the editions' ledgers; the figures are OpenRouter's recorded costs.",
        "months": dict(sorted(months.items())), "editions": dict(sorted(editions.items())),
        "total": {"images": sum(r["images"] for r in months.values()), "cost_usd": round(sum(r["cost_usd"] for r in months.values()), 6)},
        **({"key_budget": budget} if budget else {}),
    })


# ------------------------------------------------------------------ the tool, through Playwright
def proxy_config():
    """Chromium ignores HTTPS_PROXY; the skill's helper turns it into Playwright's proxy option."""
    url = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")
    if not url:
        return None
    p = urlparse(url)
    cfg = {"server": f"{p.scheme or 'http'}://{p.hostname}:{p.port}"}
    if p.username:
        cfg["username"] = p.username
    if p.password:
        cfg["password"] = p.password
    return cfg


def chromium_args():
    spki = os.environ.get("CHROMIUM_SPKI_ALLOW")
    return [f"--ignore-certificate-errors-spki-list={spki}"] if spki else []


def playwright_or_exit():
    try:
        from playwright.sync_api import sync_playwright  # noqa: F401
        return sync_playwright
    except ImportError:
        raise SystemExit("infographics: the playwright package is not installed for this Python. In a venv: pip install playwright==1.56.0; "
                         "PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers when a Chromium is shared, else python -m playwright install chromium")


def open_tool(p, timeout_s=45):
    browser = p.chromium.launch(headless=True, proxy=proxy_config(), args=chromium_args())
    page = browser.new_page(viewport={"width": 1400, "height": 1200})
    page.goto(TOOL_URL, timeout=60000)
    page.wait_for_function("() => window.__tool && window.__tool.meta && typeof window.__tool.meta.getMethods === 'function'", timeout=timeout_s * 1000)
    return browser, page


MODEL_ID = re.compile(r"\b(?:google|openai|anthropic|black-forest-labs|stability|bytedance|x-ai|qwen)/[a-z0-9][a-z0-9.\-]*(?::[a-z0-9-]+)?\b")


def offered_models(page):
    """The model ids the tool's own skill files and manifest list, in the order found; the tool's default first."""
    ids = []
    try:
        default = page.evaluate("() => (window.__tool.getModel && window.__tool.getModel()) || null")
        if default:
            ids.append(str(default))
    except Exception:
        pass
    for script in ("async () => JSON.stringify(await window.__tool.meta.getManifest())", "async () => { const s = await window.__tool.meta.getSkills(); return [s.api, s.browser, s.human].join('\\n') }"):
        try:
            text = page.evaluate(script) or ""
        except Exception:
            continue
        for m in MODEL_ID.findall(str(text)):
            if m not in ids:
                ids.append(m)
    return ids


def catalogue_models():
    """OpenRouter's public list of models whose output includes an image: [(id, name)]; empty when it cannot be fetched."""
    ctx = ssl.create_default_context(cafile=str(CA_BUNDLE) if CA_BUNDLE.exists() else None)
    try:
        with urllib.request.urlopen(urllib.request.Request(OPENROUTER_MODELS, headers={"Accept": "application/json"}), timeout=40, context=ctx) as r:
            data = json.loads(r.read().decode("utf-8")).get("data") or []
    except (urllib.error.URLError, ValueError, OSError):
        return []
    return [(str(m.get("id")), str(m.get("name") or "")) for m in data if isinstance(m, dict) and "image" in ((m.get("architecture") or {}).get("output_modalities") or [])]


def choose_models(kind, offered, catalogue):
    """Every preference that is offered, in order: for each, the tool's own list first, then the catalogue; the tool's default
    (offered[0]) last. A list of (id, how), so that a model refused upstream for the whole run gives way to the next."""
    out, seen = [], set()
    for pref in MODEL_PREFS[kind]:
        for m in offered:
            if pref in m and m not in seen:
                out.append((m, f"the tool lists it (matched {pref})")); seen.add(m)
        for m, name in catalogue:
            if (pref in m or pref.replace("-", " ") in name.lower()) and m not in seen:
                out.append((m, f"OpenRouter's catalogue lists it as {name} (matched {pref}); the tool passes the id through")); seen.add(m)
    if offered and offered[0] not in seen:
        out.append((offered[0], "the tool's default"))
    return out or [(None, "no model offered; the tool's default")]


def choose_model(kind, offered, catalogue):
    """The first choice, as (id, how)."""
    return choose_models(kind, offered, catalogue)[0]


def check(args):
    """Step 2a of the tool's skill: the JS API is live; its methods, version and health, and the models it lists. No key."""
    sync_playwright = playwright_or_exit()
    with sync_playwright() as p:
        browser, page = open_tool(p)
        try:
            methods = page.evaluate("() => window.__tool.meta.getMethods()")
            version = page.evaluate("() => window.__tool.meta.getVersion ? window.__tool.meta.getVersion() : null")
            health = page.evaluate("() => window.__tool.meta.health ? window.__tool.meta.health() : null")
            attach = page.evaluate("() => [...document.querySelectorAll('input[type=file]')].map(i => i.getAttribute('accept') || '')")
            models = offered_models(page)
        finally:
            browser.close()
    catalogue = catalogue_models()
    say(f"the tool at {TOOL_URL} is live")
    say(f"version: {json.dumps(version)}")
    say(f"health: {json.dumps(health)}")
    say(f"methods ({len(methods) if isinstance(methods, list) else '?'}): {', '.join(methods) if isinstance(methods, list) else methods}")
    say(f"image input for a style reference: {'yes (' + ', '.join(a for a in attach if 'image' in a) + ')' if any('image' in a for a in attach) else 'none found'}")
    say(f"models listed by the tool's skill files ({len(models)}): {', '.join(models) or 'none found'}")
    say(f"image-output models in OpenRouter's public catalogue ({len(catalogue)}): {', '.join(m for m, _ in catalogue) or 'not reachable'}")
    for kind in ("hero", "card"):
        m, how = choose_model(kind, models, catalogue)
        say(f"{kind}: {m or 'the tool default'} ({how})")
    return 0


OPENROUTER_KEY_INFO = "https://openrouter.ai/api/v1/auth/key"


def query_budget(key):
    """What OpenRouter says about the key's own budget: its limit, what it has spent and what is left, in USD; the key itself never
    leaves the header. None when the key is absent or the request fails. The accountant shows this on the costs page."""
    if not key:
        return None
    ctx = ssl.create_default_context(cafile=str(CA_BUNDLE) if CA_BUNDLE.exists() else None)
    req = urllib.request.Request(OPENROUTER_KEY_INFO, headers={"Authorization": f"Bearer {key}", "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30, context=ctx) as r:
            d = json.loads(r.read().decode("utf-8")).get("data") or {}
        limit, left = d.get("limit"), d.get("limit_remaining")
        out = {"at": now_iso(), "limit_usd": float(limit) if limit is not None else None, "remaining_usd": round(float(left), 4) if left is not None else None}
        out["spent_usd"] = round(out["limit_usd"] - out["remaining_usd"], 4) if out["limit_usd"] is not None and out["remaining_usd"] is not None else None
        return out
    except (urllib.error.URLError, ValueError, OSError, TypeError):
        return None


def query_cost(generation_id, key):
    """OpenRouter's own figure for one generation; None when it cannot be had. The key goes in the header and nowhere else."""
    ctx = ssl.create_default_context(cafile=str(CA_BUNDLE) if CA_BUNDLE.exists() else None)
    req = urllib.request.Request(OPENROUTER_GENERATION + quote(str(generation_id)), headers={"Authorization": f"Bearer {key}", "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30, context=ctx) as r:
            data = json.loads(r.read().decode("utf-8")).get("data") or {}
            cost = data.get("total_cost")
            return float(cost) if cost is not None else None
    except (urllib.error.URLError, ValueError, OSError):
        return None


def scrub(message, key):
    """An error message with the key removed, in case a library echoed it."""
    m = str(message)
    return m.replace(key, "[key]") if key else m


def save_image(png_b64, out_dir: Path, stem):
    raw = base64.b64decode(png_b64)
    try:
        from PIL import Image
        img = Image.open(io.BytesIO(raw))
        img.load()
        f = out_dir / f"{stem}.webp"
        img.save(f, "WEBP", quality=88, method=6)
        return f.name, raw
    except Exception:
        f = out_dir / f"{stem}.png"
        f.write_bytes(raw)
        return f.name, raw


def generate(args, slug, edition, jobs, out_dir: Path, key):
    """The run: connect once, the hero first, then the cards with the hero attached; each result an entry for the ledger."""
    sync_playwright = playwright_or_exit()
    todo = [j for j in jobs if not j["exists"]]
    entries, spent_est, stopped = [], 0.0, None
    with sync_playwright() as p:
        browser, page = open_tool(p)
        try:
            offered, catalogue = offered_models(page), catalogue_models()
            candidates = {k: choose_models(k, offered, catalogue) for k in ("hero", "card")}
            for k in ("hero", "card"):      # --hero-model / --card-model: the owner's choice first, the preferences behind it
                forced = getattr(args, f"{k}_model", None)
                if forced:
                    candidates[k] = [(forced, "named on the command line")] + [c for c in candidates[k] if c[0] != forced]
            models = {k: v[0] for k, v in candidates.items()}
            say("models: " + "; ".join(f"{k} {m or 'tool default'} ({how})" for k, (m, how) in models.items()))
            try:
                page.evaluate("async (k) => { await window.__tool.connect({ apiKey: k }); return true }", key)   # the key is an argument, never in a script string
            except Exception as e:
                raise SystemExit(f"infographics: the tool could not connect to OpenRouter: {scrub(e, key)[:200]}")
            hero_png = None
            made = failed_in_a_row = 0
            for j in todo:
                if args.max_images is not None and made + sum(1 for e in entries if e.get('status') == 'failed') >= args.max_images:   # attempts, not successes: a refusal spends the cap too
                    stopped = f"max-images {args.max_images} reached"
                    break
                if args.max_cost is not None and spent_est + PRICES[j["kind"]] > args.max_cost + 1e-9:
                    stopped = f"max-cost {args.max_cost:.2f} USD would be exceeded (estimated {spent_est:.3f} so far, {PRICES[j['kind']]:.3f} for the next)"
                    break
                model, how = models[j["kind"]]
                if j["kind"] == "card" and hero_png:
                    attach_reference(page, out_dir, hero_png)      # a no-op once the tool holds the reference
                entry = {"key": j["key"], "kind": j["kind"], "id": j["id"], "prompt_sha256": j["prompt_sha256"], "prompt_file": j["prompt_file"], "template": TEMPLATES[j["kind"]],
                         "model_wanted": model, "model_chosen_because": how, "style_reference": bool(hero_png) if j["kind"] == "card" else None, "at": now_iso()}
                t0 = time.time()
                if entries:
                    time.sleep(PAUSE_S)
                try:
                    try:
                        result = generate_with_retries(page, j, model)
                    except Exception as e:
                        # the model refused for the whole of the waits (rate-limited upstream, for everyone, as OpenRouter's reply says
                        # for Nano Banana 2.1 on 14 October 2026): the next preference takes the job and the rest of the run
                        if not (RETRYABLE.search(str(e)) and len(candidates[j["kind"]]) > 1):
                            raise
                        was = candidates[j["kind"]].pop(0)[0]
                        models[j["kind"]] = model, how = candidates[j["kind"]][0]
                        how = f"{how}; after {was} was refused upstream ({str(e).splitlines()[0][:60]})"
                        models[j["kind"]] = (model, how)
                        entry.update({"model_wanted": model, "model_chosen_because": how})
                        say(f"{j['kind']}: {was} refused for the run; falling through to {model}")
                        result = generate_with_retries(page, j, model)
                    src = result.get("imageSrc") or ""
                    if not src.startswith("data:"):
                        raise RuntimeError("the tool returned no image")
                    b64 = src.split(",", 1)[1]
                    fname, raw = save_image(b64, out_dir, f"{SAFE_ID.sub('_', j['id'])}.{j['prompt_sha256'][:8]}")
                    dur = result.get("duration")
                    entry.update({"status": "done", "file": fname, "model": result.get("model") or model, "generationId": result.get("generationId"),
                                  "duration_s": round(float(dur) / 1000 if isinstance(dur, (int, float)) and dur > 1000 else float(dur) if isinstance(dur, (int, float)) else time.time() - t0, 1),
                                  "cost_usd": None, "bytes": len(raw)})
                    if j["kind"] == "hero":
                        hero_png = raw
                    made += 1
                    failed_in_a_row = 0
                    spent_est += PRICES[j["kind"]]
                    say(f"made {j['kind']} {j['id']} -> {fname} ({entry['duration_s']} s, {entry['model']})")
                except Exception as e:
                    entry.update({"status": "failed", "error": scrub(e, key)[:300]})
                    say(f"failed {j['kind']} {j['id']}: {entry['error'][:120]}")
                    failed_in_a_row += 1
                entries.append(entry)
                if failed_in_a_row >= MAX_FAILURES_IN_A_ROW:
                    stopped = f"{failed_in_a_row} failures in a row"
                    break
        finally:
            browser.close()
    # the costs, from OpenRouter's own accounting, once it has settled
    with_ids = [e for e in entries if e.get("status") == "done" and e.get("generationId")]
    if with_ids:
        say(f"waiting {SETTLE_S} s for OpenRouter's accounting, then asking the cost of {len(with_ids)} generations")
        time.sleep(SETTLE_S)
        for e in with_ids:
            e["cost_usd"] = query_cost(e["generationId"], key)
        known = [e["cost_usd"] for e in with_ids if e["cost_usd"] is not None]
        say(f"cost: {sum(known):.4f} USD over {len(known)} images" + (f", {len(with_ids) - len(known)} not reported" if len(known) < len(with_ids) else ""))
    return entries, stopped


RETRYABLE = re.compile(r"HTTP (429|5\d\d)\b|Too Many Requests|rate limit|overloaded|timed? ?out", re.I)


def generate_with_retries(page, j, model):
    """One generation through the tool; a 429 or a 5xx is waited out and tried again, up to len(RETRY_WAITS_S) times."""
    waits = list(RETRY_WAITS_S)
    while True:
        try:
            return page.evaluate("""async (q) => {
                if (q.template) { try { window.__tool.setTemplate(q.template) } catch (e) { /* the template is a nicety */ } }
                const opts = { prompt: q.prompt, renderUI: false }
                if (q.model) opts.model = q.model
                const r = await window.__tool.generate(opts)
                return { generationId: r.generationId || null, model: r.model || null, duration: r.duration || null, imageSrc: r.imageSrc || '' }
            }""", {"prompt": j["prompt"], "model": model, "template": TEMPLATES[j["kind"]]})
        except Exception as e:
            if not waits or not RETRYABLE.search(str(e)):
                raise
            w = waits.pop(0)
            say(f"{j['kind']} {j['id']}: {str(e).splitlines()[0][:80]}; waiting {w} s, then trying again ({len(waits)} left)")
            time.sleep(w)


def attach_reference(page, out_dir: Path, hero_png: bytes):
    """The hero as the style reference for the cards (bake-off rule 6), through the tool's image input when it has one."""
    try:
        inputs = page.query_selector_all("input[type=file]")
        img = next((i for i in inputs if "image" in (i.get_attribute("accept") or "")), None)
        if img is None:
            return False
        state = page.evaluate("() => (window.__tool.getState && window.__tool.getState()) || {}")
        if state.get("image"):
            return True
        ref = out_dir / ".hero-reference.png"
        ref.write_bytes(hero_png)
        img.set_input_files(str(ref))
        page.wait_for_timeout(800)
        ok = bool((page.evaluate("() => (window.__tool.getState && window.__tool.getState()) || {}") or {}).get("image"))
        ref.unlink(missing_ok=True)
        return ok
    except Exception:
        return False


# ------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="only verify the tool's API is live: methods, version, models; no key needed")
    ap.add_argument("--wire", help="industry, or a wire's slug (owasp, aws, portugal...)")
    ap.add_argument("--from", dest="clone", help="a clone of the wire's vault")
    ap.add_argument("--edition", help="YYYY-MM-DD; the brief's edition when omitted")
    ap.add_argument("--stories", help="comma-separated story ids; the edition's new stories when omitted")
    ap.add_argument("--dry-run", action="store_true", help="write the prompts and the plan, make nothing")
    ap.add_argument("--max-images", type=int, help="make at most this many images in this run")
    ap.add_argument("--max-cost", type=float, help="stop before the estimated spend of this run would exceed this many USD")
    ap.add_argument("--out", help="the output folder; wire/<slug>/infographics under the site by default")
    ap.add_argument("--card-model", default=None, help="an OpenRouter model id for the cards, ahead of the preferences")
    ap.add_argument("--hero-model", default=None, help="an OpenRouter model id for the hero, ahead of the preferences")
    args = ap.parse_args()
    if args.check:
        return check(args)
    if not args.wire or not args.clone:
        ap.error("--wire and --from are needed (or --check)")
    slug = "" if args.wire in ("industry", "wire", "") else re.sub(r"[^a-z0-9-]", "", args.wire.lower())
    clone = Path(args.clone)
    bundle = load_bundle(clone)
    brief = bundle.get("brief") if isinstance(bundle.get("brief"), dict) else {}
    edition = args.edition or brief.get("edition")
    if not edition or not DATE.match(str(edition)):
        raise SystemExit(f"infographics: no edition date ({edition!r}); give --edition YYYY-MM-DD")
    wanted = [x.strip() for x in (args.stories or "").split(",") if x.strip()]
    stories, how = pick_stories(bundle, edition, wanted)
    wire_root = Path(args.out) if args.out else ROOT / wire_dir(slug) / "infographics"
    out_dir = wire_root / edition
    ledger = load_json(out_dir / "ledger.json", {})
    wire, jobs = plan_jobs(slug, bundle, edition, stories, out_dir, ledger)
    key = os.environ.get("OPENROUTER_API_KEY") or ""
    dry = args.dry_run or not key
    if not key and not args.dry_run:
        say("OPENROUTER_API_KEY is not in the environment: this is a dry run; nothing is spent")
    todo = [j for j in jobs if not j["exists"]]
    est = sum(j["estimated_cost_usd"] for j in todo)
    say(f"{wire} ({wire_dir(slug)}), edition {edition}: {len(stories)} stories {how}; {len(jobs)} images planned, {len(jobs) - len(todo)} already made, {len(todo)} to make, about {est:.2f} USD at the bake-off's prices")
    n = write_prompts(jobs, out_dir)
    say(f"{n} prompt files written under {out_dir.relative_to(ROOT) if out_dir.is_relative_to(ROOT) else out_dir}/prompts/")
    plan = {"schema": "wire-infographics-plan/v1", "wire": slug or "industry", "edition": edition, "at": now_iso(), "dry_run": dry, "stories": how,
            "model_preferences": MODEL_PREFS, "prices_usd": PRICES, "price_source": PRICE_SOURCE, "caps": {"max_images": args.max_images, "max_cost_usd": args.max_cost},
            "jobs": [{k: v for k, v in j.items() if k != "prompt"} for j in jobs], "estimate": {"images": len(todo), "cost_usd": round(est, 4)}}
    write_json(out_dir / "plan.json", plan)
    if dry:
        say("dry run: the plan is plan.json beside the prompts; the ledger is untouched")
        return 0
    if not todo:
        say("nothing to make: every image of this plan exists")
        return 0
    entries, stopped = generate(args, slug, edition, todo, out_dir, key)
    write_ledgers(slug, edition, out_dir, wire_root, ledger, entries, stopped, budget=query_budget(key))   # the key's budget after the run, never the key
    made = [e for e in entries if e.get("status") == "done"]
    say(f"{len(made)} made, {len(entries) - len(made)} failed, {len(todo) - len(entries)} not attempted{'; stopped: ' + stopped if stopped else ''}; ledgers written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
