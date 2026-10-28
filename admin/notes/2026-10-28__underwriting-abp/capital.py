"""How much it would take to start an insurer for agent behaviour policies: an illustrative model for article 4.

Two stages. Every input is an assumption, stated here, chosen for the article and not fitted to any market data:

  Stage 1, a managing agent (MGA or Lloyd's coverholder) for two years: it prices and sells policies on a carrier's
  capital, so it needs money to run, not capital to back the policies.
  Stage 2, carrying the risk: capital to survive a bad year. Because every row of a behaviour policy is capped, the
  worst year can be bounded from the limits sold: the share of all limits one shared failure could hit at once
  (one model's flaw, one tool's bug), times the share the company keeps after reinsurance, with a buffer on top,
  and never below the regulatory floor of the place it is licensed.

Run: python3 capital.py   (writes ../../content/articles/data/where-to-build-the-agent-insurer__capital.json)
"""
import json, os

STAGE1 = {
    "months": 24,
    "team": [{"year": 1, "people": 8}, {"year": 2, "people": 15}],
    "cost_per_person_gbp": 150000,
    "regulatory_legal_actuarial_pi_gbp_per_year": 250000,
    "technology_gbp_per_year": 200000,
}
STAGE2 = {
    "agents": [500, 2000, 10000],
    "limits_per_agent_gbp": 80000,
    "shared_failure_share": [0.05, 0.10],
    "kept_after_reinsurance": 0.5,
    "buffer": 1.2,
    "floors_gbp": {"Bermuda Class 3A ($1m)": 800000, "UK general insurer (PRA MCR)": 2400000, "EU non-life (Solvency II MCR)": 2350000},
}


def stage1():
    years = [{"year": t["year"], "people": t["people"],
              "cost": t["people"] * STAGE1["cost_per_person_gbp"] + STAGE1["regulatory_legal_actuarial_pi_gbp_per_year"] + STAGE1["technology_gbp_per_year"]}
             for t in STAGE1["team"]]
    return {"years": years, "total": sum(y["cost"] for y in years)}


def stage2():
    rows = []
    for n in STAGE2["agents"]:
        limits = n * STAGE2["limits_per_agent_gbp"]
        for c in STAGE2["shared_failure_share"]:
            need = limits * c * STAGE2["kept_after_reinsurance"] * STAGE2["buffer"]
            rows.append({"agents": n, "total_limits": limits, "shared_failure_share": c,
                         "capital_from_limits": round(need),
                         "capital_with_uk_floor": round(max(need, STAGE2["floors_gbp"]["UK general insurer (PRA MCR)"])),
                         "capital_with_bermuda_floor": round(max(need, STAGE2["floors_gbp"]["Bermuda Class 3A ($1m)"]))})
    return rows


if __name__ == "__main__":
    s1, s2 = stage1(), stage2()
    out = {"note": "Illustrative. Computed by admin/notes/2026-10-28__underwriting-abp/capital.py; every input is an assumption stated in it.",
           "stage1_inputs": STAGE1, "stage2_inputs": STAGE2, "stage1": s1, "stage2": s2}
    here = os.path.dirname(os.path.abspath(__file__))
    json.dump(out, open(os.path.join(here, "..", "..", "content", "articles", "data", "where-to-build-the-agent-insurer__capital.json"), "w"), indent=1)
    print("stage 1, two years as a managing agent: £{:,}".format(s1["total"]), [f"year {y['year']}: £{y['cost']:,}" for y in s1["years"]])
    for r in s2:
        print(f"stage 2: {r['agents']:>6,} agents, £{r['total_limits']:,} of limits, shared failure {r['shared_failure_share']:.0%}: capital £{r['capital_from_limits']:,} (UK floor applied £{r['capital_with_uk_floor']:,}; Bermuda £{r['capital_with_bermuda_floor']:,})")
