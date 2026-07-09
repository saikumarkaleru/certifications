# Q&A — Real Options & Advanced Capital Budgeting

A mixed bank of theory (with model answers and interview phrasing) and fully solved numerical problems. Numbers are self-verified for internal consistency.

---

## Theory

### Q1. What is a real option, and why does it always have non-negative value?
**Answer.** A real option is the *right, but not the obligation*, to take a business action on a real (non-financial) asset in the future — expand, delay, abandon, contract, or switch — usually at terms partly fixed today. Its payoff is `max(·, 0)`: you exercise only in states where it pays and let it lapse otherwise. Because the downside is truncated at zero while the upside is retained, its value can never be negative.
**Say it in an interview:** "You're not buying the cash flows, you're buying the *right* to the cash flows — and a right you only use when it helps can't hurt you."

### Q2. Give the taxonomy of real options and classify each as a call or a put.
**Answer.**
- **Calls (buy upside):** option to **expand**, option to **defer/delay**, **growth** options. Payoff `max(V − K, 0)`.
- **Puts (limit downside):** option to **abandon**, option to **contract**, option to **shut down temporarily**. Payoff `max(K − V, 0)`.
- **Switching / compound options:** portfolios or sequences of calls and puts (e.g. staged R&D = a call on a call).
**Interview tip:** deliver the call/put split instantly — it's the single most-tested fact in the topic.

### Q3. Why does standard NPV understate the value of a flexible project?
**Answer.** Standard NPV discounts a single, pre-committed stream of expected cash flows — it assumes management commits today and never adapts. That is equivalent to averaging the outcomes and *then* deciding once (`max(E[x], 0)`). A flexible manager instead decides *after* each outcome is revealed (`E[max(x, 0)]`). By Jensen's inequality `E[max(x,0)] ≥ max(E[x],0)`, and the gap is exactly the value of the embedded options — the value NPV throws away.

### Q4. Why does higher volatility increase real-option value? Isn't risk supposed to be bad?
**Answer.** For a *committed* position, more risk is bad. But an option keeps the good tail and discards the bad one, so it *loves* dispersion. Both calls and puts rise in value with `σ`. Formally the payoff `max(·,0)` is convex, and expected value of a convex function increases with the spread of the underlying. It is the one place in finance where more risk is unambiguously good — *provided you hold the option, not the commitment*.

### Q5. How does a real option map onto the Black–Scholes framework?
**Answer.**

| BS input | Real-option meaning |
|---|---|
| `S₀` (stock) | PV of the project's operating cash flows |
| `K` (strike) | Investment cost to exercise |
| `T` | Time the decision can be deferred |
| `σ` | Volatility of project value |
| `r` | Risk-free rate |
| dividends | Value lost by waiting (forgone CFs, competitor entry) |

A growth option is a *call* on the project. You needn't compute BS by hand, but you must name the five inputs and their direction of effect.

### Q6. What is the risk-neutral probability, and why value options with it?
**Answer.** `q = ((1+r) − d)/(u − d)`. It is the probability under which the underlying is expected to earn the risk-free rate. Using it lets us price the option by no-arbitrage replication and discount the payoff at the **risk-free rate**, sidestepping the impossible question of what risk premium an option "deserves." Crucially, `q` is a *pricing device*, not the real-world probability `p` — `p` never enters a binomial option value.

### Q7. When does real-options thinking actually matter — and when is it just noise?
**Answer.** It matters only when **all three** hold: (1) genuine **uncertainty** (high `σ`), (2) real **managerial flexibility** to respond, and (3) **information arriving over time** before you must decide. It matters most *at the margin*, where static NPV is near zero. Where static NPV is strongly positive or negative, options rarely flip the decision — just invest or don't. Sprinkling "real options" on every marginal project to justify it is a classic abuse.

### Q8. Explain APV and when you'd use it instead of WACC-NPV.
**Answer.** APV = **base-case (all-equity) NPV + PV of financing side-effects** (mainly the interest tax shield, plus subsidies, minus issuance and distress costs). You discount operating FCFs at the *unlevered* cost of equity `r_U`, then add the tax shield separately. Use APV when **leverage changes over time** — LBOs, project finance, fixed debt-paydown schedules — because WACC assumes a *constant* D/V ratio and misprices when that's false. WACC and APV agree under consistent assumptions.
**Say it:** "WACC hides financing in the discount rate; APV puts it on its own line."

### Q9. Why can't you just use scenario analysis to capture flexibility?
**Answer.** Scenario analysis probability-weights cash flows and *then* discounts — it decides on the average and never adapts. Real-options valuation takes the `max` at each decision node *after* uncertainty resolves. The difference, by Jensen, is `E[max(x,0)] − max(E[x],0) ≥ 0`, precisely the flexibility value scenario analysis omits.

### Q10. What is a compound option, with a real example?
**Answer.** An option whose underlying is itself an option — exercising one stage buys the right to the next. Staged **R&D** is the canonical case: funding Phase I buys the option to fund Phase II, which buys the option to launch commercially. Each stage caps the downside (you abandon after a bad readout) while preserving the upside — which is why staged/milestone financing is worth more than committing the whole budget upfront.

### Q11. In APV, what rate discounts the interest tax shield, and why does it matter?
**Answer.** Match the rate to the shield's *risk*. If the debt is fixed in dollars and safe, the shield is nearly certain — discount at the cost of debt `r_D`. If the debt (and thus interest) scales with firm value, the shield shares the assets' risk — discount at `r_U`. The choice materially changes the answer, so state your assumption explicitly. For perpetual fixed debt the shield collapses to `T_c × D`.

### Q12. What's the single biggest conceptual error people make valuing real options?
**Answer.** Averaging *before* deciding. If you compute `E[cash flows]` and discount, you've reproduced the static NPV and captured zero option value. The option only appears when you take `max(continue, alternative)` at each node *after* the uncertainty is revealed, then work backwards. A close second: discounting the option payoff at a risky rate after already using risk-neutral probabilities — that double-counts risk.

---

## Numerical Problems

### Q13. Abandonment option (put) via decision tree.
A firm invests **$120m** now. In one year: **good market (p=0.5)** continuing value **$170m**; **bad market (p=0.5)** continuing value **$70m**. Salvage value at year 1 = **$100m**. Discount rate **10%**. Find (a) static NPV, (b) NPV with abandonment, (c) the option value.

**Solution.**
(a) Static (no abandonment):
```
E[value] = 0.5×170 + 0.5×70 = 85 + 35 = 120
Static NPV = 120/1.10 − 120 = 109.09 − 120 = −10.91m  → reject
```
(b) With abandonment, take `max(continue, 100)` each state:
```
Good: max(170,100)=170 ;  Bad: max(70,100)=100 (abandon)
E[value] = 0.5×170 + 0.5×100 = 85 + 50 = 135
Strategic NPV = 135/1.10 − 120 = 122.73 − 120 = +2.73m  → accept
```
(c) Option value:
```
= 2.73 − (−10.91) = 13.64m
```
Direct check: option pays max(100−70,0)=30 only in bad state → PV = 0.5×30/1.10 = 13.64m. ✓

### Q14. Expansion / growth option, binomial risk-neutral.
Underlying expansion value `V₀ = $80m`; in one year `u=1.5` (→$120m) or `d=0.6` (→$48m). Expansion cost (strike) `K = $90m`. Risk-free `r = 5%`. Value the growth option.

**Solution.**
```
q = ((1+0.05) − 0.6)/(1.5 − 0.6) = 0.45/0.90 = 0.50
Payoffs: up max(120−90,0)=30 ; down max(48−90,0)=0
Call = [0.50×30 + 0.50×0]/1.05 = 15/1.05 = 14.29m
```
The growth option is worth **$14.29m**. If a pilot that unlocks it had a static NPV of, say, −$3m, the pilot still creates 14.29 − 3 = **+$11.29m** of strategic value.

### Q15. Option to delay (defer) — build now vs wait.
Build now: project value `$150m`, cost `$130m`. Wait one year: value → **$210m (up)** or **$110m (down)**; cost stays `$130m`; `r = 6%`; `u = 1.4`, `d ≈ 0.7333`. Should you build now or wait?

**Solution.**
```
Build now static NPV = 150 − 130 = 20m
q = (1.06 − 0.7333)/(1.4 − 0.7333) = 0.3267/0.6667 = 0.490
Wait payoffs: up max(210−130,0)=80 ; down max(110−130,0)=0
Value of waiting = [0.490×80 + 0.510×0]/1.06 = 39.2/1.06 = 36.98m
```
Waiting (**$36.98m**) > building now (**$20m**) → **defer**. The deferral option is worth ~$17m more than immediate exercise because waiting lets you dodge the down state. (Caveat: if delay forfeits cash flows or invites competitors — the "dividend" — that cost must be netted off and can flip the answer to build now.)

### Q16. APV of a levered project.
Unlevered FCFs: Year1 $50m, Year2 $60m, Year3 $70m. `r_U = 13%`. Initial investment $130m. Financed with $80m debt at 8%, `T_c = 30%`, debt flat for 3 years then repaid, shield discounted at `r_D = 8%`. Find APV.

**Solution.**
Base-case NPV:
```
PV = 50/1.13 + 60/1.13² + 70/1.13³
   = 44.25 + 46.99 + 48.52 = 139.76
Base NPV = 139.76 − 130 = 9.76m
```
Tax shield (interest = 8%×80 = 6.4; shield = 0.30×6.4 = 1.92/yr):
```
PV(shield) = 1.92/1.08 + 1.92/1.08² + 1.92/1.08³
           = 1.778 + 1.646 + 1.524 = 4.95m
```
APV:
```
APV = 9.76 + 4.95 = 14.71m
```
The financing adds **$4.95m** of tax-shield value on top of the **$9.76m** all-equity value → **APV = $14.71m**.

### Q17. APV vs WACC consistency check (perpetuity).
A project generates level unlevered FCF of **$12m/yr in perpetuity**. `r_U = 12%`. It carries **$40m of perpetual debt**, `T_c = 25%`. Value it by (a) APV and (b) confirm the tax-shield component.

**Solution.**
(a) Base (unlevered) value = `12 / 0.12 = 100m`.
Perpetual fixed-debt shield = `T_c × D = 0.25 × 40 = 10m`.
```
APV = 100 + 10 = 110m
```
(b) Check via annual shield: interest at, say, `r_D = 8%` = `0.08×40 = 3.2`; shield = `0.25×3.2 = 0.8/yr`; perpetuity discounted at `r_D`: `0.8/0.08 = 10m`. ✓ Matches `T_c × D`. The tax shield contributes exactly **$10m**, and total value is **$110m**.

### Q18. Two-step binomial expansion option.
`V₀ = $100m`; each step `u = 1.25`, `d = 0.8`; `r = 5%` per step; strike `K = $110m`, exercisable only at the end of step 2 (European). Value the call.

**Solution.**
Terminal values after two steps:
```
uu: 100×1.25×1.25 = 156.25
ud: 100×1.25×0.80 = 100.00
dd: 100×0.80×0.80 = 64.00
```
Payoffs `max(V−110,0)`:
```
uu: 46.25 ; ud: 0 ; dd: 0
```
Risk-neutral prob per step: `q = (1.05−0.8)/(1.25−0.8) = 0.25/0.45 = 0.5556`.
Probability of uu = `q² = 0.3086`.
```
Call = q² × 46.25 / (1.05)² = 0.3086 × 46.25 / 1.1025
     = 14.273 / 1.1025 = 12.95m
```
The two-step growth option is worth **$12.95m**.

### Q19. Contract (downsize) option — a put.
A plant investment yields continuing value in one year of **$140m (good, 0.5)** or **$60m (bad, 0.5)**. Management can *contract* operations in the bad state: give up 40% of value but recover **$50m** of released capital. Discount rate 10%. Is contracting valuable, and by how much?

**Solution.**
Bad-state choice: continue at $60m, or contract to `0.6×60 + 50 = 36 + 50 = 86m`. Take `max(60, 86) = 86` → contract.
```
Without option: E = 0.5×140 + 0.5×60 = 100 → PV = 100/1.10 = 90.91
With option:    E = 0.5×140 + 0.5×86 = 113 → PV = 113/1.10 = 102.73
Contract option value = 102.73 − 90.91 = 11.82m
```
The contraction option (a put) adds **$11.82m** by letting the firm release $50m of capital when demand disappoints.

### Q20. Volatility sensitivity — demonstrating that higher σ raises option value.
Same growth option as Q14 (`V₀=80`, `K=90`, `r=5%`) but compare **low-vol** (`u=1.25, d=0.8`) vs **high-vol** (`u=1.5, d=0.6`). Show the option is worth more under higher volatility.

**Solution.**
Low-vol:
```
q = (1.05−0.8)/(1.25−0.8) = 0.25/0.45 = 0.5556
up value 80×1.25=100 → payoff max(100−90,0)=10 ; down 64 → 0
Call = 0.5556×10/1.05 = 5.556/1.05 = 5.29m
```
High-vol (from Q14): **14.29m**.
```
Higher σ → 14.29 vs 5.29 → option value nearly triples.
```
Confirms the principle: **more uncertainty raises option value**, even though the same dispersion would *hurt* a committed (non-optional) position.

### Q21. Putting it together — negative static NPV rescued by an option.
A biotech spends **$20m** on a Phase II trial (static NPV **−$5m** on its own). Success (risk-neutral prob `q = 0.4`) unlocks a launch worth **$300m** for a build cost of **$180m** in one year; failure makes launch worthless. `r = 6%`. Should they run the trial?

**Solution.**
Launch (call) payoff: success `max(300−180,0)=120`; failure `0`.
```
Option value = [0.4×120 + 0.6×0]/1.06 = 48/1.06 = 45.28m
Strategic value of trial = −5 + 45.28 = +40.28m
```
**Yes — run it.** The trial loses $5m standalone but buys a $45.3m launch option, for **+$40.3m** strategic value. This is the archetypal "unprofitable pilot that's actually a great investment" answer.

### Q22. WACC vs APV — why the LBO shop prefers APV (conceptual + quick number).
An LBO closes with **$500m debt** falling to **$100m over 5 years**. Explain in one line why WACC misprices it, then quick-value the year-1 shield (`interest 9%`, `T_c=25%`, discount `r_D=9%`).

**Solution.**
*Why WACC fails:* WACC assumes a **constant D/V ratio**; here leverage collapses from very high to modest, so no single WACC is correct at any point — you'd need a different WACC each year. APV values the unlevered business once at `r_U` and adds each year's actual shield separately, staying correct as leverage falls.
*Year-1 shield:* interest = `0.09 × 500 = 45m`; shield = `0.25 × 45 = 11.25m`; PV = `11.25/1.09 = 10.32m`. You'd repeat this for each year's *declining* debt balance and sum — something a single WACC simply cannot represent.
