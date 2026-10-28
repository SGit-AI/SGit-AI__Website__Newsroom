"""Price one agent's behaviour policy, row by row, and split each row between the vendor and the customer.

    python3 premium.py            every scenario in policy.json
    python3 premium.py --json     the same, as JSON

The formula (formula.md has it in words):
    a row with no limit is excluded
    rate(row)      = base_rate x the factors of the ENFORCED controls on that row x where_it_runs, at most cap_rate
    premium(row)   = limit x rate
    vendor layer   = premium x vendor_share, only when every vendor condition is on; the customer pays the rest
    payout(event)  = min(loss, limit) if the event maps to the row and every condition held at the time, else 0

Standard library only. Every number in policy.json is illustrative.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
P = json.load(open(os.path.join(HERE, "policy.json")))


def price(on, where):
    ctl = [c for c in P["controls"] if c["id"] in on]
    vendor_ok = all(c["id"] in on for c in P["controls"] if c.get("vendor_condition"))
    rows = []
    for r in P["rows"]:
        if r["limit"] is None:
            rows.append({"id": r["id"], "risk": r["risk"], "excluded": True})
            continue
        rate = r["base_rate"]
        for c in ctl:
            f = c["rows"].get(r["id"])
            if f is not None and c["enforced_by"]:
                rate *= f
        rate = min(rate * P["where_it_runs"][where], P["cap_rate"])
        prem = round(r["limit"] * rate)
        vend = round(prem * r["vendor_share"]) if vendor_ok else 0
        rows.append({"id": r["id"], "risk": r["risk"], "limit": r["limit"], "rate": round(rate, 4),
                     "premium": prem, "vendor": vend, "customer": prem - vend})
    cov = [x for x in rows if not x.get("excluded")]
    tl, tp, tv = sum(x["limit"] for x in cov), sum(x["premium"] for x in cov), sum(x["vendor"] for x in cov)
    return {"rows": rows, "limit": tl, "premium": tp, "vendor": tv, "customer": tp - tv, "share": round(tp / tl, 3)}


def payout(row_id, loss, conditions_held):
    r = next(x for x in P["rows"] if x["id"] == row_id)
    if r["limit"] is None or not conditions_held:
        return 0
    return min(loss, r["limit"])


if __name__ == "__main__":
    out = {name: dict(price(s["controls"], s["where"]), controls=s["controls"], where=s["where"]) for name, s in P["scenarios"].items()}
    if "--json" in sys.argv:
        print(json.dumps(out, indent=1))
    else:
        for name, v in out.items():
            print(f"{name}: £{v['premium']:,} for £{v['limit']:,} of cover ({v['share']:.0%}); vendor £{v['vendor']:,}, customer £{v['customer']:,}")
        print("a £30,000 leak, conditions held:", payout("leakage", 30000, True), "| not held:", payout("leakage", 30000, False), "| on the host row:", payout("host", 30000, True))
