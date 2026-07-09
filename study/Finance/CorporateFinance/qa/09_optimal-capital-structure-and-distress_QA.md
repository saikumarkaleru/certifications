# Q&A — Optimal Capital Structure & Financial Distress

A mix of theory (with model answers and interview phrasing) and fully-solved numerical problems. Numbers are self-verified and internally consistent.

---

## Theory

### Q1. State the trade-off theory of capital structure in one equation and explain each term.

**Answer.**
$$V_L = V_U + PV(\text{interest tax shield}) - PV(\text{financial distress \& agency costs})$$

- $V_U$ — value of the firm if it were all-equity; set by the operating assets' cash flows.
- $PV(\text{ITS})$ — value added because interest is tax-deductible; for permanent debt it is $t_c \times D$. Grows roughly linearly with debt.
- $PV(\text{distress \& agency})$ — value destroyed by the rising probability and cost of financial distress (direct + indirect) plus agency conflicts. Grows convexly with debt.

The linear-up/convex-down combination produces a hump ⇒ an interior optimum, the leverage that maximizes value (equivalently minimizes WACC).

**How to say it:** "In a frictionless world capital structure is irrelevant. Add taxes and debt is valuable; add distress and too much debt is destructive. The optimum balances the marginal tax benefit against the marginal distress cost."

---

### Q2. Why does the naive MM-with-taxes model wrongly imply 100% debt, and what fixes it?

**Answer.** MM Prop I with taxes gives $V_L = V_U + t_c D$: value rises linearly and without limit as debt increases, so the "optimum" is 100% debt. That is the model announcing a missing piece — it has the tax *benefit* but no *cost* of debt. Trade-off theory fixes it by adding the present value of financial distress and agency costs, which rise convexly with leverage. Now value humps over and there is a finite optimum.

**How to say it:** "If your framework says more debt is always better, you've forgotten distress. The tax shield is real but bounded by the cost of getting closer to default."

---

### Q3. Distinguish direct and indirect costs of financial distress. Which dominate and why does it vary by firm?

**Answer.**
- **Direct** — legal, court, advisory, accounting fees of restructuring/bankruptcy. Largely *fixed*, so a big percentage hit for small firms but only a few percent of value for large firms.
- **Indirect** — lost sales (customers fear no future warranty/service), suppliers demanding cash upfront, employee flight, management distraction, fire-sale asset disposals, and foregone positive-NPV projects. These *dominate* — often 10–25% of firm value.

Indirect costs vary by **asset type and business model**: firms whose value is intangible, reputation-sensitive, or relationship-dependent (software, pharma, consumer brands, complex durables) suffer huge indirect costs; firms with tangible, redeployable assets (real estate, utilities, shipping) suffer little.

**How to say it:** "Direct costs are the lawyers; indirect costs are the franchise eroding. Indirect dominates, and it's largest exactly where the value is intangible."

---

### Q4. Why does a software firm carry ~no debt while a REIT or regulated utility carries a lot?

**Answer.** Three trade-off drivers, all pointing the same way:
1. **Asset type / distress cost** — REIT/utility assets are tangible and hold value in distress (low $L$); software's value is intangible growth options and talent that vanish in distress (high $L$).
2. **Cash-flow stability** — contracted/regulated cash flows safely service fixed debt (low default probability); software cash flows are volatile.
3. **Growth & tax** — high-growth software prizes financing flexibility and may have limited taxable income to shield and severe debt-overhang costs; mature utilities have stable taxable income, few growth options, and gain from debt's discipline.

---

### Q5. Explain asset substitution (risk-shifting) and why lenders care.

**Answer.** Equity is economically a call option on the firm's assets, so once debt is fixed, equity holders benefit from *more* asset risk — they keep the upside, lenders absorb the downside. Near distress this can push them to take even negative-NPV gambles ("heads I win, tails the lender loses"). It is an **agency cost of debt** that destroys value. Lenders anticipate it, so they charge higher rates and impose **covenants** (leverage limits, restrictions on asset risk, negative pledge).

---

### Q6. Explain debt overhang / the underinvestment problem.

**Answer.** (Myers.) A firm with heavy existing debt may reject *positive-NPV* projects because most of the value created would accrue to repairing existing lenders' claims rather than to equity holders, who must fund the investment. Equity therefore won't put up the money, and good projects are starved — an agency cost of debt and itself an indirect distress cost. It is worst for firms simultaneously highly levered and rich in growth options — another reason growth firms keep low leverage.

---

### Q7. How can debt *add* value beyond the tax shield?

**Answer.** Through **discipline** (Jensen's free-cash-flow theory). Fixed interest obligations absorb cash that entrenched managers might otherwise waste on empire-building, perks, or value-destroying acquisitions, and the threat of default forces operational efficiency. Debt is a bonding device aligning managers with owners. This is a core rationale for LBOs and leveraged recaps — separate from and additive to the tax benefit.

---

### Q8. What is the significance of the investment-grade boundary (BBB–/BB+)?

**Answer.** It separates **investment grade** (BBB– and above) from **high yield / speculative** (BB+ and below). Crossing down — becoming a **fallen angel** — triggers forced selling by IG-mandated funds, widens the spread sharply, and can shut off commercial paper and cheap bank facilities. Because these costs are discrete and large, many treasurers manage explicitly to hold a notch above BBB–, so the IG line effectively caps prudent leverage.

---

### Q9. Trade-off theory vs pecking-order theory — contrast them.

**Answer.**
- **Trade-off:** there *is* a target leverage that balances tax shields against distress/agency costs; firms gravitate to it.
- **Pecking order (Myers–Majluf):** from **asymmetric information**, firms have *no* target — they finance with internal funds first, then debt, then equity as a last resort, because issuing equity signals the stock is overvalued.

Key evidence: the most *profitable* firms often carry the *least* debt (they self-fund from retained earnings) — natural under pecking order, awkward for a pure tax-driven trade-off. **Synthesis:** firms have a target range but adjust toward it slowly and let information/flexibility concerns drive short-run financing.

---

### Q10. What is a leveraged recapitalization and why do firms do one?

**Answer.** The firm issues a large slug of new **debt** and returns the proceeds to shareholders via a **share buyback** or **special (dividend) recap** — re-gearing the balance sheet toward debt without changing the assets. Motives: (1) capture unused **tax shield**; (2) impose **discipline** on free cash flow; (3) **signal confidence**; (4) boost **EPS/ROE** and concentrate ownership; (5) act as a **takeover defense**. It's essentially "an LBO the company does to itself," with existing shareholders (not a sponsor) capturing the value — but it consumes financial flexibility and raises distress risk.

---

### Q11. The most profitable firms often have the least debt. Does this break trade-off theory?

**Answer.** It's a tension, not a knockout. Pure trade-off says profitable firms have the *most* taxable income to shield, so they should use *more* debt — the opposite of what we see. Pecking order explains the pattern: profitable firms generate enough internal cash that they rarely need external funds, so they stay low-leverage by default. The reconciliation: trade-off sets the long-run *target range*; pecking-order/timing forces explain deviations and the slow speed of adjustment. Good candidates hold both ideas at once.

---

### Q12. Why is WACC U-shaped, and how does that relate to the optimum?

**Answer.** After-tax debt is cheaper than equity, so adding debt first pulls WACC *down*. But leverage makes equity riskier (equity beta and $r_e$ rise) and, at higher levels, makes debt riskier too ($r_d$ rises as default risk grows). Eventually the rising cost of the components overwhelms the benefit of holding more cheap debt, so WACC turns *up*. The result is a U-shape, and its **minimum coincides with the value-maximizing leverage** $D^*$ — because $V = FCF/WACC$, minimizing the discount rate maximizes value.

---

## Numerical problems

### Q13. Tax shield on permanent debt.

**Problem.** A firm raises \$800m of permanent debt at 5%; tax rate 25%. What is the annual tax shield and its present value? If it were rebalanced to a target ratio (discount at $r_U = 9\%$), how does PV change qualitatively?

**Solution.**
- Annual interest = \$800m × 5% = \$40m. Annual tax shield = \$40m × 25% = **\$10m/yr.**
- PV (permanent debt, discount at $r_d$) = $\frac{t_c r_d D}{r_d} = t_c D$ = 0.25 × \$800m = **\$200m.** (Check: \$10m / 0.05 = \$200m ✓.)
- If rebalanced, discount the \$10m at $r_U = 9\%$: PV = \$10m / 0.09 ≈ **\$111m** — materially *smaller*, because a rebalanced shield is riskier (tracks firm value) than a fixed one.

**Takeaway:** the $t_c D$ figure is the upper bound; real shields are often smaller.

---

### Q14. Finding the optimum from a trade-off table.

**Problem.** $V_U = \$2{,}000$m, $t_c = 25\%$, permanent debt so $PV(\text{ITS}) = 0.25D$. Distress PV by debt level: D=0→0; 400→8; 800→40; 1,000→70; 1,200→130; 1,400→230. Find optimal debt and value.

**Solution.** $V_L = 2{,}000 + 0.25D - \text{distress}$:

| D | 0.25D | Distress | $V_L$ |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 2,000 |
| 400 | 100 | 8 | 2,092 |
| 800 | 200 | 40 | 2,160 |
| 1,000 | 250 | 70 | **2,180** |
| 1,200 | 300 | 130 | 2,170 |
| 1,400 | 350 | 230 | 2,120 |

Peak at **D = \$1,000m, $V_L$ = \$2,180m** (+\$180m, +9% vs unlevered). Marginal check 800→1,000: shield +\$50m, distress +\$30m ⇒ +\$20m (good). 1,000→1,200: shield +\$50m, distress +\$60m ⇒ −\$10m (bad). Optimum ≈ \$1,000m. ✓

---

### Q15. Levered cost of equity and WACC (MM Prop II with tax).

**Problem.** $r_U = 10\%$, $r_d = 6\%$, $t_c = 25\%$, target D/E = 1.0 (so D/V = 50%). Find $r_e$ and WACC.

**Solution.**
- $r_e = r_U + (r_U - r_d)\frac{D}{E}(1-t_c) = 10\% + (10\%-6\%)(1.0)(0.75) = 10\% + 3.0\% = $ **13.0%.**
- After-tax $r_d = 6\%(0.75) = 4.5\%$.
- WACC $= 0.5(13.0\%) + 0.5(4.5\%) = 6.5\% + 2.25\% = $ **8.75%.**

Sanity check via the unlevered-WACC identity: with taxes, WACC should be below $r_U$ = 10% by the tax-shield benefit — 8.75% < 10% ✓.

---

### Q16. WACC across leverage — spotting the tax-only trap.

**Problem.** Using $r_U=10\%$, $t_c=25\%$, and a *rising* $r_d$ schedule (D/E 0→$r_d$5%; 0.5→5.5%; 1.0→6.5%; 2.0→9%), compute WACC at each and comment.

**Solution.** $r_e = 10\% + (10\%-r_d)(D/E)(0.75)$; WACC $= \frac{E}{V}r_e + \frac{D}{V}r_d(0.75)$.

| D/E | D/V | $r_d$ | $r_e$ | after-tax $r_d$ | WACC |
|---:|---:|---:|---:|---:|---:|
| 0 | 0% | 5.0% | 10.00% | 3.75% | 10.00% |
| 0.5 | 33.3% | 5.5% | 11.69% | 4.125% | 9.17% |
| 1.0 | 50% | 6.5% | 12.63% | 4.875% | 8.75% |
| 2.0 | 66.7% | 9.0% | 11.50% | 6.75% | 8.33% |

Check D/E=0.5: $r_e = 10\%+(4.5\%)(0.5)(0.75)=10\%+1.69\%=11.69\%$; WACC $=0.667(11.69\%)+0.333(4.125\%)=7.79\%+1.375\%=9.17\%$ ✓.
Check D/E=2.0: $r_e=10\%+(1\%)(2)(0.75)=11.5\%$; WACC $=0.333(11.5\%)+0.667(6.75\%)=3.83\%+4.50\%=8.33\%$ ✓.

**Comment:** WACC keeps falling — the classic **tax-only pitfall**. Real WACC turns up once a convex *distress premium* (extra $r_e$/$r_d$ near the top) is added; then the minimum sits at moderate leverage. The exercise shows why you must model distress explicitly.

---

### Q17. Debt capacity from a target rating (trough sizing).

**Problem.** EBITDA \$300m (peak), \$240m (downside). Existing net debt \$600m. Target BBB requires net debt/EBITDA ≤ 3.0x through-cycle and EBITDA/interest ≥ 4.0x. New debt costs 6%. How much more debt fits?

**Solution.**
- Leverage cap (trough): 3.0 × \$240m = **\$720m** max net debt ⇒ headroom = 720 − 600 = **\$120m** on a downside basis (on peak it would be 3×300=\$900m ⇒ \$300m, but that's the fallen-angel mistake).
- Coverage check at \$720m: interest = 720×6% = \$43.2m; downside coverage = 240/43.2 = **5.6x** ≥ 4.0x ✓. Leverage binds, not coverage.
- **Prudent incremental capacity ≈ \$120m** (through-cycle). Taking the extra \$180m to reach \$900m would put downside leverage at 900/240 = **3.75x**, breaching BBB ⇒ downgrade risk in a recession.

---

### Q18. Leveraged recap — EPS, ROE, and value.

**Problem.** 200m shares at \$40 (equity \$8,000m), no debt; EBIT \$800m; tax 25%. Recap: issue \$3,000m debt at 5%, buy back shares at \$40. Find new EPS, ROE, tax-shield value, and comment on risk.

**Solution.**
- Shares repurchased = 3,000/40 = 75m ⇒ **125m shares** remain.
- Pre-recap: NI = 800×0.75 = \$600m; EPS = 600/200 = **\$3.00**; earnings yield = 3/40 = 7.5%; ROE = 600/8,000 = 7.5%.
- Interest = 3,000×5% = \$150m; new pre-tax = 800−150 = \$650m; NI = 650×0.75 = **\$487.5m.**
- New EPS = 487.5/125 = **\$3.90** (+30%). Accretive because earnings yield 7.5% > after-tax cost of debt 5%×0.75 = 3.75%.
- New book equity ≈ 8,000 − 3,000 = \$5,000m; ROE = 487.5/5,000 = **9.75%** (up from 7.5%).
- Tax-shield value = 0.25 × 3,000 = **\$750m** created.
- **Risk:** coverage falls from ∞ to 800/150 = **5.3x**; debt/EBITDA = 3,000/800 = **3.75x** (BBB/BB border); equity beta and $r_e$ rise; flexibility shrinks. If EBIT dropped 35% to \$520m, coverage = 520/150 = 3.5x — getting tight. Worth it only with stable cash flows and redeployable assets.

---

### Q19. Is a debt-funded buyback accretive? Quick decision rule.

**Problem.** A firm trades at a P/E of 20x (earnings yield 5%). It can borrow at 8% pre-tax, tax rate 25%. Would a debt-funded buyback be EPS-accretive?

**Solution.** After-tax cost of debt = 8%×0.75 = **6.0%.** Earnings yield = 1/20 = **5.0%.** Since earnings yield (5%) < after-tax cost of debt (6%), the buyback is **dilutive** — you'd be borrowing at 6% to retire earnings yielding only 5%. Rule: **accretive iff E/P > $r_d(1-t_c)$.** (Contrast Q18, where 7.5% > 3.75% ⇒ accretive.)

**Caveat to state:** EPS accretion ≠ value creation. High-multiple stocks are usually dilutive to buy back with debt, and even when accretive the higher risk must be weighed.

---

### Q20. Expected cost of distress.

**Problem.** Firm value (pre-distress) \$1,000m. At its current leverage, annual probability of entering distress is 8%, and the loss given distress is 20% of firm value. Estimate the expected one-period distress cost, and show how it scales if leverage doubling raises the probability to 25%.

**Solution.**
- Current: expected cost = $p \times L \times V$ = 0.08 × 0.20 × \$1,000m = **\$16m.**
- After lever-up: 0.25 × 0.20 × \$1,000m = **\$50m** — more than **3x** higher, though leverage only doubled. That convex jump (probability rising faster than leverage) is exactly why distress costs bend the value curve down and create a finite optimum.

---

### Q21. Fallen-angel spread impact.

**Problem.** A firm has \$5,000m of debt. Staying BBB, its spread is 150 bps; a downgrade to BB widens the spread to 350 bps. Estimate the annual extra interest cost of the downgrade, and the value impact if that higher cost is treated as permanent (discount at the new 9% cost of debt... use the incremental-spread approach).

**Solution.**
- Extra spread = 350 − 150 = 200 bps = 2.0%.
- Extra annual interest = 2.0% × \$5,000m = **\$100m/yr** (pre-tax); after-tax at 25% = **\$75m/yr.**
- Capitalized as a perpetuity at ~9%: \$75m / 0.09 ≈ **\$833m** of value lost — before counting forced selling, tighter covenants, and lost CP access. This quantifies why the IG line is defended so fiercely and why it effectively caps leverage.

---

### Q22. Putting it together — recommend a capital structure.

**Problem.** Two firms: (A) a regulated water utility, stable contracted cash flows, tangible assets, high taxable income; (B) an early-stage biotech, pre-profit, volatile, intangible IP. For each, recommend a leverage posture and justify with the trade-off framework.

**Solution.**
- **Firm A (utility):** *High leverage is optimal.* Low default probability (stable cash flows), low loss-given-distress (tangible, financeable assets), full use of the tax shield (high taxable income), strong free-cash-flow discipline benefit, minimal debt-overhang cost (few growth options). Target investment grade with meaningful Debt/EBITDA (e.g., 4–6x is common in the sector), sized off through-cycle cash flows. Consider a leveraged recap if under-levered.
- **Firm B (biotech):** *Little or no debt.* High default probability (volatile, pre-profit), huge loss-given-distress (intangible IP and talent evaporate), no taxable income so the tax shield is worthless (worse, it has NOLs), severe debt-overhang and asset-substitution risk. It should be equity-financed and preserve flexibility (pecking order: internal/venture equity, not debt). Debt would push it toward the cliff with none of the benefits.

**How to say it:** "Same framework, opposite answers — because the utility's distress cost is low and its tax shield is fully usable, while the biotech's distress cost is enormous and its tax shield is zero. Leverage should track the *survivability of value in distress and the usability of the shield*, not just cash-flow level."
