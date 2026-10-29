# The underwriting formula, in words

An agent behaviour policy names what an agent can reach (the grant), what the business asked it to do (the mandate),
and the gap between them (the delta). Read as an insurance policy, every row it names can have a limit, a rate and a
premium, and a share that the agent's vendor carries.

1. **A row with no limit is excluded.** If a capability is reachable and the policy names no limit for it, nobody
   covers it, at any price.
2. **Each row starts at a base rate.** The share of the limit an uncontrolled agent would pay for that row in a year.
3. **Each enforced control on a row multiplies its rate by a factor below one.** A capability removed from the grant,
   a proxy that caps records per action, drafts only, an egress allow list, a hook that holds a reply for a person.
   A control nothing enforces, such as a line in the system prompt, has a factor of 1.
4. **Where the agent runs multiplies every row.** Below one on a certified runtime, above one on an uncertified one.
   No row's rate goes above the cap rate.
5. **The premium for a row is its limit times its rate.** The policy's premium is the sum.
6. **The vendor carries its share of a row** when the vendor's own conditions held (here: its guardrails and output
   filters left on). The vendor's layer is priced into what it sells; the customer's insurer prices the rest.
7. **A claim pays if the event maps to a row and every condition on that row held at the time, up to the row's limit.**
   If a condition was not holding, the row does not pay.

`policy.json` holds every input; `premium.py` computes every number with the standard library only; `index.html`
does the same in the browser. The numbers are illustrative: fitting them is what an underwriter does with loss data.
