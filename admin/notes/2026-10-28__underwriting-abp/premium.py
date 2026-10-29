"""The worked example behind "A payout for every row": an illustrative premium for one agent, row by row.

Every number in INPUT is illustrative, chosen for the article, not fitted to loss data. The formula is the point:

    a row is excluded       if its capability is reachable and the policy names no limit for it
    rate(row)               = base_rate(row) x product of the factors of the enforced controls on that row x where_it_runs, at most 0.95
    premium(row)            = limit(row) x rate(row)
    payout(event)           = min(loss, limit(row)) if the event maps to the row and every condition held, else 0

A control counts only if something enforces it (a hook, a proxy, a removed grant), never if it is only a line in the prompt.

Run: python3 premium.py  (writes ../../content/articles/data/a-payout-for-every-row__worked-example.json)
"""
import json, os

INPUT = {
    "agent": "a support agent connected to the customer database (the Licence to Operate vault's agent:concierge, generalised)",
    "currency": "GBP, illustrative",
    "where_it_runs": {"certified": 0.8, "uncertified": 1.1},
    "rows": [
        {"id": "corruption", "risk": "Customer records corrupted or deleted", "capability": "crm:write", "limit": 20000, "base_rate": 0.8},
        {"id": "leakage", "risk": "Customer data leaked", "capability": "crm:export, mail:send", "limit": 50000, "base_rate": 0.85},
        {"id": "advice", "risk": "Wrong answer acted on by a customer", "capability": "llm:generate", "limit": 10000, "base_rate": 0.5},
        {"id": "host", "risk": "Commands run on the host", "capability": "shell:exec", "limit": None, "base_rate": None},
    ],
    "controls": [
        {"id": "no-write", "control": "crm:write removed from the grant", "enforced_by": "the grant", "rows": {"corruption": 0.1}},
        {"id": "cap-20", "control": "At most 20 customer records per action", "enforced_by": "a proxy in front of the CRM", "rows": {"leakage": 0.4, "corruption": 0.5}},
        {"id": "draft-only", "control": "Drafts only; a person sends", "enforced_by": "mail:send removed from the grant", "rows": {"leakage": 0.5}},
        {"id": "egress", "control": "Outbound network only to an allow list", "enforced_by": "the runtime's egress policy", "rows": {"leakage": 0.6}},
        {"id": "review", "control": "Answers with a refund or a legal point go to a person", "enforced_by": "a hook that holds the reply", "rows": {"advice": 0.5}},
        {"id": "prompt-line", "control": "\"Never export customer data\" in the system prompt", "enforced_by": None, "rows": {"leakage": 0.6}},
    ],
}


def price(controls_on, where):
    on = [c for c in INPUT["controls"] if c["id"] in controls_on]
    rows = []
    for r in INPUT["rows"]:
        if r["limit"] is None:
            rows.append({"id": r["id"], "risk": r["risk"], "status": "excluded: no limit named, so not covered"})
            continue
        rate = r["base_rate"]
        applied = []
        for c in on:
            f = c["rows"].get(r["id"])
            if f is None:
                continue
            if not c["enforced_by"]:
                applied.append({"control": c["id"], "factor": 1.0, "why": "not enforced: no discount"})
                continue
            rate *= f
            applied.append({"control": c["id"], "factor": f})
        rate = min(rate * INPUT["where_it_runs"][where], 0.95)
        rows.append({"id": r["id"], "risk": r["risk"], "limit": r["limit"], "rate": round(rate, 4),
                     "premium": round(r["limit"] * rate), "controls": applied})
    covered = [x for x in rows if "limit" in x]
    total_limit = sum(x["limit"] for x in covered)
    total_premium = sum(x["premium"] for x in covered)
    return {"controls_on": controls_on, "where_it_runs": where, "rows": rows,
            "total_limit": total_limit, "total_premium": total_premium,
            "premium_as_share_of_limit": round(total_premium / total_limit, 3)}


SCENARIOS = {
    "uncontrolled": price([], "uncertified"),
    "a line in the prompt": price(["prompt-line"], "uncertified"),
    "enforced controls, certified runtime": price(["no-write", "cap-20", "draft-only", "egress", "review"], "certified"),
}

WALK = [
    ("Uncontrolled, uncertified runtime", [], "uncertified"),
    ("+ a line in the prompt (not enforced)", ["prompt-line"], "uncertified"),
    ("Runs on a certified runtime", ["prompt-line"], "certified"),
    ("+ crm:write removed from the grant", ["prompt-line", "no-write"], "certified"),
    ("+ drafts only, mail:send removed", ["prompt-line", "no-write", "draft-only"], "certified"),
    ("+ at most 20 records per action, by proxy", ["prompt-line", "no-write", "draft-only", "cap-20"], "certified"),
    ("+ outbound only to an allow list", ["prompt-line", "no-write", "draft-only", "cap-20", "egress"], "certified"),
    ("+ refunds and legal points held for a person", ["prompt-line", "no-write", "draft-only", "cap-20", "egress", "review"], "certified"),
]

if __name__ == "__main__":
    out = {"note": "Illustrative. Computed by admin/notes/2026-10-28__underwriting-abp/premium.py; no number here is fitted to loss data.",
           "formula": __doc__.strip().split("\n\n")[1], "input": INPUT, "scenarios": SCENARIOS,
           "walk": [{"step": l, "total_premium": price(c, w)["total_premium"]} for l, c, w in WALK]}
    here = os.path.dirname(os.path.abspath(__file__))
    dst = os.path.join(here, "..", "..", "content", "articles", "data", "a-payout-for-every-row__worked-example.json")
    with open(dst, "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    for k, v in SCENARIOS.items():
        print(f"{k:40} premium £{v['total_premium']:>6,} for £{v['total_limit']:,} of cover ({v['premium_as_share_of_limit']:.0%})")
        for r in v["rows"]:
            print("   ", r["id"], r.get("premium", r.get("status")))
