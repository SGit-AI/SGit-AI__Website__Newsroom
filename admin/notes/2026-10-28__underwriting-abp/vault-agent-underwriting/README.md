# Agent underwriting: a premium calculator for one agent's behaviour policy

A vault for the underwriting series on newsroom.sgit.ai, 28 October 2026: "A payout for every row", "Who carries the
risk" and "The vendor's layer". It holds the formula as data, so it can be argued with in numbers.

| File | What it is |
|---|---|
| `formula.md` | the formula in seven steps, in words |
| `policy.json` | the inputs: four rows, seven controls, the runtime factors, the vendor's share per row, four scenarios |
| `premium.py` | computes every scenario and a claim; Python 3, standard library only: `python3 premium.py` |
| `index.html` | the calculator, in the browser: switch controls on and off, change limits and the vendor's share |
| `app.json` | how the vault viewer opens the calculator |

**Check it.** `python3 premium.py` prints, for the worked example: £69,850 a year for £80,000 of cover uncontrolled
(87%); £6,720 with five enforced controls on a certified runtime (8%); and of that £6,720, £1,816 carried by the
vendor when its guardrails are left on. The calculator shows the same numbers from the same file.

**What it is not.** Every limit, rate, factor and share is illustrative, chosen for the articles; none is fitted to
loss data, and no insurer has agreed to it. It is a shape to argue with, not a price.

Content CC BY 4.0, Dinis Cruz and the newsroom's agents. Nothing in this vault is secret.

The calculator is kept here as `index.html.txt`, so this site does not serve it as one of its own pages; in the vault it is `index.html`.
