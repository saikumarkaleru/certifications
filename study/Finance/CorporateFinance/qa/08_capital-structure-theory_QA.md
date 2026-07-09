# Q&A — Capital Structure Theory

A mixed bank of theory (with model answers and interview phrasing) and fully-solved numericals. Numbers are self-verified and internally consistent.

---

## Theory questions

### Q1. State Modigliani-Miller Proposition I (no taxes) and prove it in one sentence.

**Answer.** `V_L = V_U`: the value of a levered firm equals that of an identical unlevered firm — capital structure is irrelevant. **Proof idea:** if the levered firm were worth more, an investor could sell it, replicate its cash flows using the unlevered firm plus *personal* borrowing ("homemade leverage"), and arbitrage the difference risk-free; that arbitrage forces the values equal. The load-bearing assumption is that investors can lever on personal account at the same terms as firms, so corporate leverage adds nothing they can't do themselves.

**Interview line:** *"Financing just slices a fixed cash-flow pie; slicing a pizza differently doesn't create more pizza."*

---

### Q2. Why does the cost of equity rise as a firm adds debt?

**Answer.** Equity is the *residual* claim — it gets whatever is left after fixed debt payments. Promising more cash to bondholders makes the leftover stream to shareholders more volatile and more sensitive to swings in EBIT. This added **financial risk** sits on top of the firm's inherent **business risk**, so shareholders demand a higher return. Formally, MM Proposition II: `r_e = r_a + (r_a − r_d)(D/E)`. The cost of equity rises linearly in D/E; the slope is the asset-return-minus-debt-cost spread.

**Interview line:** *"Cheap debt isn't free — it's paid for by a higher cost of equity."*

---

### Q3. What is the interest tax shield and why does it create value?

**Answer.** Interest is tax-deductible; dividends and retained earnings are not. So a levered firm pays less corporate tax — each year it saves `T_c × interest`. That saved cash would otherwise have gone to the government, so debt effectively *shifts value from the tax authority to investors.* For perpetual debt, the present value of all future shields is `T_c × D`. It's the single reason MM-with-taxes says debt adds value.

**Caveat to mention:** the shield only has value if the firm actually has taxable income; a loss-making firm gets no benefit, and personal taxes claw some of it back.

---

### Q4. If the tax shield makes debt valuable, why isn't every firm 100% debt?

**Answer.** Because **financial distress and agency costs** rise with leverage and eventually overwhelm the tax shield. The **trade-off theory** says `V_L = V_U + PV(tax shield) − PV(distress costs)`, and value peaks at an *interior* optimum where the marginal tax benefit of one more dollar of debt equals the marginal distress cost. Distress costs include direct ones (legal/court fees) and larger indirect ones (lost customers, fleeing suppliers and staff, risk-shifting, debt overhang, fire sales, lost flexibility). The tax shield grows linearly but distress costs grow convexly — that convexity produces the optimum.

---

### Q5. Explain the pecking-order theory and its sharpest empirical prediction.

**Answer.** Because managers know the firm's true value and outside investors don't, financing follows a pecking order: **internal funds first, then debt, then equity as a last resort.** Internal cash carries no information problem; debt is relatively information-insensitive; equity is the most information-sensitive, so issuing it signals that management thinks the stock is overvalued — and the market punishes the announcement (~2-3% average drop). **Sharpest prediction:** *profitable firms borrow less*, because they self-fund and rarely tap external markets. This negative profitability-leverage correlation is one of the most robust facts in corporate finance and is exactly the *opposite* of naive trade-off theory (which says profitable firms should borrow more to shield more income).

---

### Q6. How is issuing debt a signal? Contrast with issuing equity.

**Answer.** Signaling theory (Ross): financing actions are credible messages *because they are costly to fake.* Taking on fixed debt obligations says "we're confident our cash flows can service this — and if we're wrong, management personally bears the bankruptcy pain." A weak firm can't safely mimic that, so debt is a **positive** signal. Issuing equity is the reverse: managers issue when shares look dear, so it's read as a **negative** signal about intrinsic value. Dividends and buybacks work the same way — raising a dividend signals sustainable earnings; a buyback signals the stock is cheap.

---

### Q7. What does market-timing theory add?

**Answer.** It claims managers **issue equity when the market is high** (equity cheap to sell relative to true worth) and **issue debt or buy back stock when the market is low.** Capital structure is then not a deliberate target but the *cumulative residue of past timing decisions* — leverage ends up correlated with historical market-to-book ratios. It explains why equity issuance clusters in booms and IPO windows.

---

### Q8. Distinguish business risk from financial risk.

**Answer.** **Business risk** is the volatility of EBIT — it comes from the operations and asset side (demand cyclicality, operating leverage, competition) and is *independent of financing.* **Financial risk** is the *extra* volatility of equity returns caused by fixed debt obligations. Leverage never changes business risk; it re-allocates who bears it, piling financial risk onto the residual equity claim. Two firms with identical assets have the same business risk but different financial risk if their leverage differs.

---

### Q9. How does capital structure feed into a DCF valuation?

**Answer.** Through **WACC**, the discount rate: `WACC = (E/V)·r_e + (D/V)·r_d·(1 − T_c)`. Adding low-cost, tax-advantaged debt lowers WACC up to the optimal point, which raises the enterprise value of the discounted free cash flows. Beyond the optimum, rising costs of equity and debt plus distress risk push WACC back up (the U-shaped WACC curve). Best practice: use a **target** capital structure and **market** values in WACC, not today's snapshot or book values, so the valuation isn't whipped around by transient leverage.

---

### Q10. Name the limits to leverage.

**Answer.** (1) Rising cost of equity as the residual claim gets riskier (MM Prop II). (2) Rising cost of debt as lenders price growing default risk and impose covenants. (3) Financial distress costs — direct and, larger, indirect. (4) Agency costs of debt — underinvestment/debt overhang, asset substitution/risk-shifting. (5) Loss of financial flexibility — no dry powder for downturns or opportunities. (6) Finite debt capacity, bounded by asset tangibility and cash-flow stability. Together these create the U-shaped WACC and the inverted-U value curve.

---

### Q11. Which firms should be highly levered, and which lightly?

**Answer.** **High leverage** suits firms with stable, predictable cash flows and tangible, redeployable assets — utilities, real estate, telecoms, consumer staples — because distress costs per dollar of debt are low and lenders lend cheaply against hard collateral. **Low leverage** suits volatile, R&D-heavy, intangible-asset firms — biotech, early-stage software, high-growth tech — where distress destroys franchise value and there's little collateral. The two master variables are **asset tangibility** and **cash-flow stability.**

---

### Q12. What is the Miller (1977) personal-tax refinement?

**Answer.** Investors also pay *personal* taxes, and interest income is typically taxed more heavily than equity income (dividends and deferred capital gains). This personal-tax disadvantage of debt *partially offsets* the corporate tax shield. The net gain from leverage becomes `[1 − (1−T_c)(1−T_e)/(1−T_d)]·D`. If `(1−T_c)(1−T_e) = (1−T_d)`, the gain vanishes — Miller's neutral equilibrium. **Takeaway:** the real-world tax shield is *smaller* than a naive `T_c × D`.

---

## Numerical problems

### Q13. MM no-tax: WACC is constant.

**Problem.** All-equity firm: perpetual EBIT = $300, no taxes, `r_a = 12%`. It issues $800 perpetual debt at `r_d = 7%` to repurchase stock. Find V_L, E, r_e, and WACC.

**Solution.**
- `V_U = 300 / 0.12 = 2,500`. MM Prop I (no tax): `V_L = V_U = 2,500`.
- `E = V_L − D = 2,500 − 800 = 1,700`.
- `r_e = r_a + (r_a − r_d)(D/E) = 0.12 + (0.12 − 0.07)(800/1,700) = 0.12 + 0.05 × 0.4706 = 0.12 + 0.02353 = 14.35%`.
- Check via income: interest = `7% × 800 = 56`; equity income = `300 − 56 = 244`; equity value = `244 / 0.14353 = 1,700`. ✓
- `WACC = (1,700/2,500)(0.14353) + (800/2,500)(0.07) = 0.68 × 0.14353 + 0.32 × 0.07 = 0.09760 + 0.02240 = 12.0%`. ✓

**Answer.** V_L = 2,500 (unchanged), E = 1,700, r_e = 14.35%, WACC = 12% = r_a. Cheap debt bought nothing.

---

### Q14. MM with taxes: value of the tax shield.

**Problem.** Same firm as Q13 but `T_c = 30%`. EBIT = $300, `r_a = 12%`, issues D = $800 at `r_d = 7%`. Find V_U, V_L, E, r_e, WACC.

**Solution.**
- `V_U = EBIT(1 − T_c)/r_a = 300 × 0.70 / 0.12 = 210 / 0.12 = 1,750`.
- `PV(shield) = T_c × D = 0.30 × 800 = 240`.
- `V_L = 1,750 + 240 = 1,990`; `E = 1,990 − 800 = 1,190`.
- `r_e = 0.12 + (0.12 − 0.07)(0.70)(800/1,190) = 0.12 + 0.035 × 0.67227 = 0.12 + 0.02353 = 14.35%`.
- `WACC = (1,190/1,990)(0.14353) + (800/1,990)(0.07)(0.70) = 0.59799 × 0.14353 + 0.40201 × 0.049 = 0.08583 + 0.01970 = 10.55%`.
- Cross-check: `WACC = r_a(1 − T_c·D/V) = 0.12(1 − 0.30 × 800/1,990) = 0.12(1 − 0.12060) = 0.12 × 0.87940 = 10.55%`. ✓
- Value check: `210 / 0.10553 = 1,990`. ✓

**Answer.** V_U = 1,750, tax shield = 240, V_L = 1,990, WACC falls from 12% to 10.55%. Debt now creates $240 of value.

---

### Q15. Cash-flow proof of the annual tax shield.

**Problem.** Using Q14's numbers (EBIT = 300, T_c = 30%, interest = 56), show the levered firm delivers more cash to investors than the unlevered firm, and reconcile with `T_c × D`.

**Solution.**
- Unlevered: tax = `30% × 300 = 90`; cash to investors = `300 − 90 = 210`.
- Levered: interest to debt = `56`; pre-tax equity income = `300 − 56 = 244`; tax = `30% × 244 = 73.2`; after-tax to equity = `170.8`. Total to investors = `56 + 170.8 = 226.8`.
- Difference = `226.8 − 210 = 16.8` per year. Check: `T_c × interest = 0.30 × 56 = 16.8`. ✓
- Capitalize the annual shield at r_d: `16.8 / 0.07 = 240 = T_c × D`. ✓

**Answer.** The levered firm delivers 16.8 more per year, worth 240 today — exactly the tax shield.

---

### Q16. Trade-off theory: find the optimal debt level.

**Problem.** Unlevered value V_U = 2,000, T_c = 25%. Estimated PV of distress costs: D = 500 → 8; D = 1,000 → 35; D = 1,500 → 95; D = 2,000 → 200. Find the value-maximizing debt level.

**Solution.** `V_L = 2,000 + 0.25·D − distress`:

| D | Shield = 0.25D | Distress | V_L |
|---|---|---|---|
| 0 | 0 | 0 | 2,000 |
| 500 | 125 | 8 | 2,117 |
| 1,000 | 250 | 35 | **2,215** |
| 1,500 | 375 | 95 | 2,280 |
| 2,000 | 500 | 200 | 2,300 |

Wait — recompute carefully: D=1,500 → `2,000 + 375 − 95 = 2,280`; D=2,000 → `2,000 + 500 − 200 = 2,300`. Values are still rising at D=2,000, so with only these points the peak is at the highest tabulated debt. Add a check point D = 2,500 with distress = 480: `2,000 + 625 − 480 = 2,145` (now falling).

Marginal net value per 500 tranche: 0→500: +117; 500→1,000: +98; 1,000→1,500: +65; 1,500→2,000: +20; 2,000→2,500: `+125 shield − 280 extra distress = −155`. The last profitable tranche ends at **D = 2,000.**

**Answer.** Optimal D = 2,000, V_L = 2,300. The marginal tax shield (125 per tranche) exceeds marginal distress cost through 2,000, then flips negative — value peaks there.

---

### Q17. Unlevering and relevering the cost of equity (Hamada-style via MM).

**Problem.** A firm has `r_a = 11%` (unlevered/asset return), `r_d = 6%`, `T_c = 25%`. It targets D/E = 0.5. What is its levered cost of equity, and its WACC?

**Solution.**
- `r_e = r_a + (r_a − r_d)(1 − T_c)(D/E) = 0.11 + (0.11 − 0.06)(0.75)(0.5) = 0.11 + 0.05 × 0.375 = 0.11 + 0.01875 = 12.875%`.
- Weights from D/E = 0.5 → D/V = 0.5/1.5 = 1/3, E/V = 2/3.
- `WACC = (2/3)(0.12875) + (1/3)(0.06)(0.75) = 0.08583 + 0.015 = 10.083%`.
- Cross-check: `r_a(1 − T_c·D/V) = 0.11(1 − 0.25 × 1/3) = 0.11(1 − 0.08333) = 0.11 × 0.91667 = 10.083%`. ✓

**Answer.** r_e = 12.875%, WACC ≈ 10.08%.

---

### Q18. Effect of a leveraged recapitalization on EPS and cost of equity.

**Problem.** Firm has 100 shares at $20 (equity = $2,000), no debt, EBIT = $300, T_c = 0 (ignore taxes for EPS illustration), r_a = 15%. It borrows $800 at 7% and buys back 40 shares at $20. Show EPS before and after.

**Solution.**
- Before: net income = EBIT = 300 (no tax, no interest); EPS = `300 / 100 = $3.00`.
- After: interest = `7% × 800 = 56`; net income = `300 − 56 = 244`; shares = `100 − 40 = 60`; EPS = `244 / 60 = $4.07`.
- EPS rose from $3.00 to $4.07 — but so did risk. Note: at EBIT = 300 leverage boosts EPS; at low EBIT it would *cut* it. Break-even (indifference) EBIT where levered EPS = unlevered EPS: `EBIT/100 = (EBIT − 56)/60` → `60·EBIT = 100·EBIT − 5,600` → `40·EBIT = 5,600` → `EBIT = 140`. Below 140, leverage hurts EPS.

**Answer.** EPS rises $3.00 → $4.07 at EBIT = 300, but leverage only helps above the break-even EBIT of $140; below that it magnifies losses. This is financial risk in action — higher expected EPS, higher volatility.

---

### Q19. Announcement effect / pecking order in numbers.

**Problem.** Management knows the firm is truly worth $120/share; the market prices it at $100. It needs to raise $200 by issuing new shares at the $100 market price. Firm currently has 100 shares. Show the wealth transfer to new shareholders.

**Solution.**
- Shares issued = `200 / 100 = 2 new shares` (wait: $200 / $100 = 2 shares). Total shares = 102.
- True total value after raise = `true existing value + cash raised = 100 × 120 + 200 = 12,000 + 200 = 12,200`.
- True value per share post-issue = `12,200 / 102 = 119.61`.
- New shareholders paid $100 for something worth $119.61 → they gained `19.61 × 2 = 39.2`.
- Existing shareholders' stake fell from `120.00` to `119.61` per share → lost `0.39 × 100 = 39.2`. ✓ (transfer sums to zero)

**Answer.** Issuing undervalued equity transfers ~$39 from existing to new shareholders. This is exactly why managers avoid equity issuance (pecking order) and why the market reads an equity issue as a negative signal — it typically only happens when management thinks shares are *over*valued.

---

### Q20. WACC minimum along a leverage schedule.

**Problem.** A firm's estimated costs at different D/V ratios (T_c = 25%):

| D/V | r_e | r_d (pre-tax) |
|---|---|---|
| 0% | 10.0% | — |
| 30% | 11.2% | 6.0% |
| 50% | 12.6% | 7.0% |
| 70% | 15.5% | 9.5% |

Find the WACC at each level and the optimal structure.

**Solution.** `WACC = (E/V)·r_e + (D/V)·r_d·(0.75)`:
- 0%: `1.0 × 10.0% = 10.00%`.
- 30%: `0.70 × 11.2% + 0.30 × 6.0% × 0.75 = 7.84% + 1.35% = 9.19%`.
- 50%: `0.50 × 12.6% + 0.50 × 7.0% × 0.75 = 6.30% + 2.625% = 8.925%`.
- 70%: `0.30 × 15.5% + 0.70 × 9.5% × 0.75 = 4.65% + 4.9875% = 9.64%`.

**Answer.** WACC: 10.00% → 9.19% → **8.93%** → 9.64%. Minimum WACC (≈8.93%) is at **D/V = 50%** — the optimal capital structure. Beyond 50%, the jump in r_e and r_d from distress risk outweighs the extra cheap-debt weighting, and WACC turns back up. Classic U-shape.

---

### Q21. APV vs WACC consistency check.

**Problem.** Unlevered FCF perpetuity = $140/yr, r_a = 10%, T_c = 30%. Firm carries perpetual debt D = 500 at r_d = 6%. Value the firm via (a) APV and (b) WACC, and confirm they match.

**Solution.**
- **(a) APV:** `V_U = 140 / 0.10 = 1,400`; `PV shield = 0.30 × 500 = 150`; `V_L = 1,400 + 150 = 1,550`.
- **(b) WACC:** need E = V_L − D = 1,050. `r_e = 0.10 + (0.10−0.06)(0.70)(500/1,050) = 0.10 + 0.028 × 0.47619 = 0.11333`. `WACC = (1,050/1,550)(0.11333) + (500/1,550)(0.06)(0.70) = 0.07677 + 0.01355 = 9.032%`. Then `V_L = 140 / 0.09032 = 1,550`. ✓

**Answer.** Both give V_L = 1,550. **Trap to avoid:** APV adds the shield explicitly and discounts unlevered FCF at r_a; WACC embeds the shield in the after-tax cost of debt and discounts the *same* unlevered FCF. Never do both at once — that double-counts the tax shield.

---

### Q22. Distress-cost break-even for a marginal borrowing decision.

**Problem.** A firm with T_c = 28% is deciding whether to add a final $1,000 of debt. The tax shield on that tranche is worth `0.28 × 1,000 = 280`. Management estimates the extra debt raises the probability of distress by 6 percentage points, and distress would destroy $X of firm value if it occurs. For what $X is the firm indifferent?

**Solution.**
- Marginal expected distress cost = `0.06 × X`.
- Indifference when marginal shield = marginal expected distress: `280 = 0.06 × X` → `X = 280 / 0.06 = 4,667`.

**Answer.** If distress would destroy more than ~$4,667 of value, the $1,000 debt tranche is value-*destroying* and should not be taken; if less, it's worth taking. This is the trade-off rule at the margin: borrow while `T_c × ΔD > Δ(probability) × (distress loss)`.

---

*End of Q&A bank — Capital Structure Theory.*
