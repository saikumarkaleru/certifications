# Q&A — Valuing Banks & Financial Institutions

A mix of theory (with interview-ready phrasing) and fully-solved numerical problems. Every number is self-verified and reconciles across methods.

---

## Theory

### Q1. Why can't you use enterprise value or EV/EBITDA to value a bank?
**A.** Enterprise value works by separating the operating business from its financing, valuing the operations, then bridging to equity via net debt. A bank breaks that separation: its "debt" — deposits and wholesale funding — is not financing, it is the **raw material** it re-sells as loans. There is no unlevered bank, so EV is undefined. EBITDA fails for the same reason: it adds back interest, but for a bank interest is effectively **cost of goods sold** (it buys money and sells money; the net interest spread is its gross profit). An earnings-before-interest number for a bank measures nothing.

**How to say it:** *"For a bank, debt is inventory, not financing, and interest is COGS. So there's no enterprise value and no meaningful EBITDA — I value the equity directly."*

### Q2. So how *do* you value a bank?
**A.** Value the equity directly, discounted at the **cost of equity** (never WACC). Primary intrinsic methods: the **dividend discount model** and the **residual income / excess return model**. Primary relative method: **price-to-tangible-book versus ROE**, governed by `P/B = (ROE − g)/(r − g)`. Triangulate the three, plus P/E. Core drivers to forecast: net interest margin, balance-sheet growth, cost of risk (provisions), efficiency ratio, and the CET1 capital ratio.

### Q3. Why discount at cost of equity and never WACC?
**A.** WACC discounts a to-the-firm (FCFF) cash flow shared by debt and equity. A bank has no separable to-the-firm cash flow — financing and operations are the same activity — so there is no FCFF and no role for WACC. Every cash flow you discount (dividends, residual income, excess-capital releases) belongs to equity holders only, so the discount rate is the cost of equity, typically from CAPM. Bank betas usually exceed 1 (leveraged, cyclical), so bank costs of equity are above the market average.

### Q4. What is the residual income (excess return) model, and why is it the preferred method for banks?
**A.** Residual income = net income minus a capital charge = `NI − r·B = (ROE − r)·B`. Equity value = **current book value + PV of all future residual income**. It is preferred because most of the value sits in today's book value — a hard balance-sheet number — so you only forecast the ROE *spread*, which mean-reverts and is far more stable than raw cash flows. It puts far less weight on the terminal value than a DDM, making it more robust and defensible.

**How to say it:** *"A bank is worth the capital already in it, plus the capitalized value of every year it earns more than its cost of equity. I'm anchored on known book value and only forecasting a shrinking spread."*

### Q5. Derive and explain the P/B–ROE formula.
**A.** From single-stage residual income: `V₀ = B₀ + (ROE − r)B₀/(r − g)`. Divide by `B₀`: `P/B = 1 + (ROE − r)/(r − g) = (ROE − g)/(r − g)`. It says a bank earning exactly its cost of equity is worth 1.0× book; earning above cost → premium to book; earning below → discount to book. It's the Rosetta Stone of bank valuation.

### Q6. A bank earns ROE = cost of equity. What P/B?
**A.** Exactly **1.0×**, for any growth rate. Plug ROE = r into `(ROE − g)/(r − g)` → `(r − g)/(r − g) = 1`. Value above book requires ROE > r; a bank that just covers its cost of equity is worth precisely the capital shareholders put in.

### Q7. A bank has ROE below its cost of equity but is growing fast. Is growth good?
**A.** **Bad.** Growth adds value only when ROE > r. When ROE < r, every retained dollar earns a negative spread, so faster growth destroys more value — in the formula, raising g lowers P/B when ROE < r. The right move for such a bank is to shrink or return capital. This is a classic trap; most candidates reflexively say growth is good.

### Q8. What is the sustainable-payout constraint and why does it matter?
**A.** A bank must retain enough earnings to grow its capital in line with its assets, or it breaches its capital ratio. If it grows at `g` and earns `ROE`, it must retain `g/ROE`, so `payout = 1 − g/ROE`. It matters because assuming a high payout *and* high growth simultaneously is internally inconsistent and inflates a DDM. Payout, growth, and ROE must reconcile.

### Q9. Why value banks on tangible book and ROTCE rather than book and ROE?
**A.** Regulators deduct goodwill and intangibles from CET1 capital — they absorb no losses and earn no regulatory credit. The capital that actually supports the balance sheet and backstops depositors is **tangible** common equity. So analysts use price-to-tangible-book (P/TBV) and return on tangible common equity (ROTCE) to align valuation with the capital regulators and the market care about.

### Q10. What is net interest margin and why is it the master value driver?
**A.** `NIM = net interest income / average earning assets` — the spread between asset yields and funding costs, scaled by the earning-asset base. It's the bank's gross margin. NIM × earning assets = net interest income, the largest revenue line; because banks run high leverage on a thin ROA (~1%), a small NIM change is heavily geared to ROE. NIM flows straight through to net income → ROE → the P/B multiple, so it's the single most-watched number in bank research.

### Q11. Walk through the driver tree from NIM to equity value.
**A.** `NIM × earning assets = net interest income`; `+ fee income − operating expense − loan loss provisions − tax = net income`; `net income / equity = ROE`; and `value = f(ROE, r, g)` via `P/B = (ROE − g)/(r − g)`. So the five value levers are NIM, asset growth, cost of risk (provisions), the efficiency ratio, and the capital ratio.

### Q12. Explain regulatory capital and how it drives value.
**A.** Under Basel III, a bank must hold equity capital (CET1) as a percentage of **risk-weighted assets** (assets weighted by riskiness). CET1 caps how big the balance sheet — and thus earning capacity — can be. Capital *above* the target ratio is **excess capital**, distributable to shareholders on top of earnings (subject to stress tests); a fast grower must retain earnings or raise capital. So a bank's distributable cash to equity = earnings − capital needed for RWA growth + release of excess capital.

### Q13. What is the bank-specific definition of FCFE?
**A.** `FCFE_bank = Net income − Δ(capital required to maintain the target CET1 ratio as RWA grows)`. Unlike the industrial "NI + D&A − capex − ΔNWC + net borrowing," the bank version treats the change in *required regulatory capital* as the reinvestment need. A bank with excess capital can distribute more than earnings for a while (payout > 100%); a growing one distributes less.

### Q14. Why are bank ROEs cyclical, and what does that mean for terminal value?
**A.** Loan loss provisions swing dramatically between benign environments (low credit costs, high ROE) and recessions (surging losses, collapsing or negative ROE). So a single year's ROE can be far from normal. For terminal value you must use a **normalized, mid-cycle ROE**, not a peak-cycle one — using an elevated current ROE in perpetuity is the most common overvaluation error.

### Q15. How do insurance companies differ, and what carries over?
**A.** Same philosophy — value equity directly, off book value, using DDM/RIM and P/B-vs-ROE. Differences: insurers collect premiums up front and pay claims later, investing the **float** in between. Life insurers are often valued on **embedded value** (PV of the in-force book + adjusted net worth) and P/EV; P&C insurers on the **combined ratio** (claims + expenses / premiums; below 100% = underwriting profit) and P/B. The unifying theme: any business where the balance sheet *is* the business is valued on equity and return on book.

### Q16. What's the one-sentence reason EBITDA is nonsense for a bank?
**A.** *"EBITDA adds back interest, but for a bank interest is the cost of goods sold — so EBITDA adds back its single biggest operating cost and measures nothing."*

---

## Numerical Problems

### Q17. Gordon DDM ↔ P/B ↔ residual income must reconcile.
**Setup.** BVPS = $25, ROE = 14%, cost of equity r = 10%, g = 6%.

**Solve.**
- Sustainable payout = `1 − g/ROE = 1 − 6/14 = 0.5714`.
- E₁ = `ROE × BVPS = 0.14 × 25 = $3.50`.
- D₁ = `E₁ × payout = 3.50 × 0.5714 = $2.00`. (Shortcut check: `D₁ = B₀(ROE − g) = 25 × (0.14 − 0.06) = 25 × 0.08 = $2.00`. ✓)
- **DDM:** `P₀ = D₁/(r − g) = 2.00/(0.10 − 0.06) = 2.00/0.04 = $50.00`.
- **P/B formula:** `(ROE − g)/(r − g) = (0.14 − 0.06)/(0.10 − 0.06) = 0.08/0.04 = 2.0×` → `2.0 × 25 = $50.00`. ✓
- **Residual income:** `V₀ = B₀ + (ROE − r)B₀/(r − g) = 25 + (0.04 × 25)/0.04 = 25 + 1.00/0.04 = 25 + 25 = $50.00`. ✓

**All three give $50.00.** Half the value is existing book ($25), half is capitalized excess return ($25).

### Q18. P/B sensitivity to ROE and to the ROE < r case.
**Setup.** r = 11%, g = 4%. Compute justified P/B at ROE = 15%, 11%, and 8%.

**Solve** using `P/B = (ROE − g)/(r − g)`, denominator = `0.11 − 0.04 = 0.07`:
- ROE 15%: `(0.15 − 0.04)/0.07 = 0.11/0.07 = 1.571×` (premium).
- ROE 11% (= r): `(0.11 − 0.04)/0.07 = 0.07/0.07 = 1.000×` (exactly book).
- ROE 8% (< r): `(0.08 − 0.04)/0.07 = 0.04/0.07 = 0.571×` (discount — value-destructive).

**Trap check — does growth help the ROE = 8% bank?** Raise g from 4% to 6%: `(0.08 − 0.06)/(0.11 − 0.06) = 0.02/0.05 = 0.40×` — P/B *falls* from 0.571× to 0.40×. **Growth destroys value when ROE < r.** ✓

### Q19. Build ROE from NIM and value the bank.
**Setup.** Earning assets = $80,000m; NIM = 2.75%; fee income = $600m; operating expense = $1,700m; provisions = $400m; tax = 25%; equity = $6,000m; r = 10%; g = 4%.

**Solve.**
- NII = `2.75% × 80,000 = $2,200m`.
- Revenue = `2,200 + 600 = 2,800`.
- Pre-provision profit = `2,800 − 1,700 = 1,100`.
- Pre-tax = `1,100 − 400 = 700`; net income = `700 × 0.75 = $525m`.
- ROE = `525 / 6,000 = 8.75%`.
- Efficiency ratio = `1,700 / 2,800 = 60.7%`.
- **P/B** = `(0.0875 − 0.04)/(0.10 − 0.04) = 0.0475/0.06 = 0.792×`.
- Equity value = `0.792 × 6,000 = $4,750m`.

Below book because ROE (8.75%) < cost of equity (10%).

**Now +25bp NIM (2.75% → 3.00%):** NII = `3.00% × 80,000 = 2,400` (+200). Net income = `(700 + 200) × 0.75 = 900 × 0.75 = $675m`. ROE = `675/6,000 = 11.25%`. P/B = `(0.1125 − 0.04)/0.06 = 0.0725/0.06 = 1.208×`. Equity value = `1.208 × 6,000 = $7,250m`.

**A 25bp NIM lift raised equity value from $4,750m to $7,250m — +53%.** That is the leverage of NIM. ✓

### Q20. Two-stage residual income with a fading ROE.
**Setup.** Tangible book B₀ = $2,000m; r = 10%; Years 1–2 ROE = 16%, payout 50% (retain 50%); from year 3 mature ROE = 11%, g = 5% perpetual.

**Step 1 — roll book (retained = 50% × NI = 50% × ROE × B_beg = 0.08 × B_beg):**

| Year | Beg book | NI = 16%×B | RI = (0.16−0.10)×B | Retained (50%) | End book |
|---|---|---|---|---|---|
| 1 | 2,000.0 | 320.0 | 120.0 | 160.0 | 2,160.0 |
| 2 | 2,160.0 | 345.6 | 129.6 | 172.8 | 2,332.8 |

**Step 2 — PV of explicit RI (discount 10%):**
- Yr1: `120.0/1.10 = 109.09`
- Yr2: `129.6/1.21 = 107.11`
- Sum = **216.20**

**Step 3 — terminal RI.** Year-3 beginning book = 2,332.8. RI₃ = `(0.11 − 0.10) × 2,332.8 = 0.01 × 2,332.8 = 23.33`, growing at 5%.
`TV₂ = RI₃/(r − g) = 23.33/(0.10 − 0.05) = 23.33/0.05 = 466.6`. PV = `466.6/1.21 = 385.6`.

**Step 4 — equity value:** `V₀ = 2,000 + 216.20 + 385.6 = $2,601.8m`. Implied P/TBV = `2,601.8/2,000 = 1.30×`.

**Cross-check via DDM.** Dividends yr1–2 (payout 50%): `160.0, 172.8`. PV = `160.0/1.10 + 172.8/1.21 = 145.45 + 142.81 = 288.26`. Mature-phase terminal P/B = `(0.11 − 0.05)/(0.10 − 0.05) = 0.06/0.05 = 1.20×` on year-2 end book of 2,332.8 → 2,799.4 at end of yr2; PV = `2,799.4/1.21 = 2,313.5`. Total = `288.26 + 2,313.5 = $2,601.8m`. ✓ **DDM and RIM reconcile exactly.**

### Q21. Excess capital release (the FCFE kicker).
**Setup.** Bank has RWA = $50,000m, actual CET1 = 13.0%, target CET1 = 11.0%, net income = $700m, cost of equity 10%, and the bank is not growing RWA this year.

**Solve.**
- CET1 capital = `13.0% × 50,000 = $6,500m`.
- Required at target = `11.0% × 50,000 = $5,500m`.
- **Excess capital = 6,500 − 5,500 = $1,000m** distributable on top of earnings.
- Total distributable to equity this year = `net income + excess release = 700 + 1,000 = $1,700m` → payout ratio = `1,700/700 = 243%`.

**Point:** an analyst modeling only the earnings-based dividend would miss $1,000m of returnable capital and undervalue the bank. Distributable cash = earnings **plus** release of trapped excess CET1 (subject to stress-test approval).

### Q22. ROE decomposition and the leverage insight.
**Setup.** Bank ROA = 1.1%, assets = $120,000m, equity = $10,000m.

**Solve.**
- Leverage = `assets/equity = 120,000/10,000 = 12.0×`.
- Net income = `ROA × assets = 0.011 × 120,000 = $1,320m`.
- ROE = `net income/equity = 1,320/10,000 = 13.2%`.
- Check via identity: `ROE = ROA × leverage = 1.1% × 12.0 = 13.2%`. ✓

**Insight:** the bank turns a thin 1.1% ROA into a healthy 13.2% ROE purely through 12× leverage. That same leverage is why regulators impose capital minimums — the leverage that produces the ROE is the leverage that creates fragility. If a regulator forced leverage down to 10× (more capital), ROE would fall to `1.1% × 10 = 11.0%`, directly lowering the justified P/B. Capital rules and valuation are two sides of one coin.
