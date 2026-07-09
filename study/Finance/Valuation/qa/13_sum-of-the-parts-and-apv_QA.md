# Q&A — Sum-of-the-Parts & Adjusted Present Value

A mix of **theory** (with interview model answers and "how to say it") and **numerical problems** (fully solved, numbers self-verified). Work each problem before reading the solution.

---

## Section A — Theory & interview questions

### Q1. What is Sum-of-the-Parts valuation and when do you use it?

**Answer.** SOTP values a diversified company by valuing each business segment separately — at its own cost of capital or peer multiple — then adding the segment values plus non-operating assets, subtracting capitalized corporate overhead, and bridging to equity. Use it when the firm runs multiple businesses with materially different growth, margin, risk, or capital intensity, so that a single blended DCF distorts value. Classic cases: conglomerates, holding companies with listed stakes, break-up/spin-off analysis, and firms with a hidden crown-jewel division.

**How to say it:** "One blended WACC over a diversified firm over-discounts the safe cash flows and under-discounts the risky ones. SOTP prices each part on its own terms, then adds them — because value is additive."

---

### Q2. Why is value additivity the foundation of SOTP?

**Answer.** In a no-arbitrage market, a portfolio is worth the sum of its holdings — otherwise you could buy the cheap side and sell the dear side risklessly. That principle licenses chopping a firm into independent cash-flow streams and valuing each separately. The wrinkle: additivity holds for the *cash flows*, but the market may discount the *wrapper* (the holdco), producing the conglomerate discount.

---

### Q3. Walk me through the EV-to-equity bridge in a SOTP.

**Answer.** Start from total operating EV (sum of segment EVs minus capitalized overhead). Add non-operating assets shareholders own — cash, investments, listed stakes (often after a tax/holdco haircut), equity-accounted associates. Subtract every claim senior to or alongside common equity — total debt, minority (non-controlling) interest, preferred stock, underfunded pensions, and debt-like leases. The result is equity value; divide by diluted shares for value per share.

**Trap to flag out loud:** "I subtract minority interest because I consolidated 100% of a partly-owned subsidiary's EBITDA into a segment EV, so I owe the minority holders their share back."

---

### Q4. What is the conglomerate discount and what drives it?

**Answer.** Diversified firms often trade 10-20% below their sum-of-parts value. Drivers: (1) capital misallocation — the parent cross-subsidizes weak divisions; (2) complexity and low analyst coverage → higher perceived risk; (3) agency costs and empire-building — managers prefer size to per-share value; (4) trapped cash and tax leakage on internal transfers; (5) no clean pure-play exposure, so investors won't pay pure-play multiples. The catalyst to unlock it is a spin-off or demerger that lets each part re-rate.

---

### Q5. What is a holding-company discount and does it make a holdco cheap?

**Answer.** A listed holdco that mainly owns stakes in other listed companies typically trades 20-50% below its look-through NAV (market value of stakes minus holdco net debt). On top of the general conglomerate reasons, holdcos carry tax on eventual disposal of the stakes, holdco-level costs, and dividend leakage. It's cheap only if the discount is wider than justified *and* there's a catalyst — a buyback at NAV, stake monetization, or structure collapse — to close it. A wide discount with no catalyst can persist for decades.

---

### Q6. Explain APV from first principles.

**Answer.** APV values a firm in two independent layers: (1) the unlevered value — project unlevered FCF (EBIT×(1−t) + D&A − capex − ΔNWC) and discount at the unlevered cost of equity r_U, as if all-equity financed; (2) the value of financing side-effects — mainly the interest tax shield (interest × tax rate), discounted at the cost of debt if the schedule is fixed, minus expected distress costs. Sum the layers for firm value, then subtract net debt for equity. The logic: operating cash flows don't care how they're funded; leverage only adds a tax benefit and a distress cost, so value those separately.

---

### Q7. When does APV beat WACC-based DCF, and why?

**Answer.** WACC assumes a *constant* debt-to-value ratio, because it embeds the tax shield into a single discount rate. That breaks whenever leverage *changes* — LBOs (debt amortizes from 6x to 2x EBITDA), deleveraging firms, project finance with a fixed loan schedule. APV handles it by modeling the tax shield explicitly year by year, at the right rate, while discounting stable operating cash flows at r_U. Under constant leverage APV and WACC give the identical answer — APV's advantage appears only when the capital structure moves.

**How to say it:** "In an LBO there is no single correct WACC because the debt ratio falls every year. APV sidesteps that entirely."

---

### Q8. Should the tax shield be discounted at r_d or r_U?

**Answer.** It depends on debt policy. If debt is a fixed, pre-set dollar schedule (an LBO paydown), the shields are as safe as the debt itself → discount at r_d; for permanent fixed debt this collapses to PV = t×D. If the firm rebalances debt to a constant percentage of firm value, the shields move with firm value and are as risky as the assets → discount at r_U (Harris-Pringle). Choosing the wrong rate is the single biggest APV judgment error.

---

### Q9. What are unlevered free cash flows and why does APV use them?

**Answer.** UFCF = EBIT×(1−t) + D&A − Capex − ΔNWC. The taxes are computed *as if all-equity* — no interest deduction — so UFCF deliberately excludes the tax shield. APV uses UFCF because it values the shield *separately* in the financing layer. If you instead used levered FCF (which already captures the interest tax benefit) and *also* added PV(tax shield), you'd double-count the shield.

---

### Q10. How do r_U, r_e, r_d, and WACC relate?

**Answer.** r_U is the cost of capital with no leverage (business risk only). Adding debt raises the cost of equity: r_e = r_U + (r_U − r_d)(1−t)(D/E). WACC = r_e×E/V + r_d×(1−t)×D/V, which sits *below* r_U by the tax-shield benefit. Under rebalanced debt, WACC ≈ r_U − r_U×t×(D/V). WACC lowers the discount rate to embed the shield; APV keeps r_U and adds the shield in the numerator. Same economics, different bookkeeping.

---

### Q11. Why does a single WACC fail in an LBO specifically?

**Answer.** An LBO starts at very high leverage and pays debt down on a schedule, so D/V falls every year. A single WACC would be too low in the early, highly-levered years (overvaluing) and too high later (undervaluing), and there's no self-consistent constant rate. APV avoids the problem: r_U is constant (it reflects only business risk), and the shrinking tax shields are discounted at r_d on their actual schedule.

---

### Q12. What are distress costs and how do they fit APV?

**Answer.** PV(distress) = probability of default × cost-given-default (as a % of firm value). Default probability rises steeply with leverage; cost-given-default is larger for intangible, reputation-dependent businesses (customers, talent, suppliers flee) and smaller for hard-asset firms. In APV it's subtracted, offsetting the tax shield. This trade-off — tax benefit up, distress cost up — is the entire theory of optimal capital structure: the value-maximizing leverage is where marginal shield equals marginal distress cost.

---

## Section B — Numerical problems

### Q13. Basic SOTP with two segments and a bridge

**Problem.** "TwinCo" has: Segment A EBITDA 250 at 10× EV/EBITDA; Segment B EBITDA 180 at 7× EV/EBITDA. Cash 300, total debt 900, minority interest 120, diluted shares 40 cr. Find equity value and value per share.

**Solution.**
- Segment A EV = 250 × 10 = 2,500
- Segment B EV = 180 × 7 = 1,260
- Total operating EV = 3,760
- + Cash 300 → 4,060
- − Debt 900 − Minority 120 = −1,020
- Equity value = 4,060 − 1,020 = **3,040**
- Per share = 3,040 / 40 = **₹76.00**

**Check:** 2,500 + 1,260 = 3,760; +300 −900 −120 = 3,040; /40 = 76 ✓.

---

### Q14. SOTP with capitalized corporate overhead and a listed stake

**Problem.** "OverheadCo": Segment X EV 5,000; Segment Y EV 3,200. Unallocated corporate cost 80/year after tax, capitalize at 8%. A 40% stake in listed "PubCo" (PubCo market cap 1,500), valued after a 30% tax/holdco haircut. Cash 400, debt 2,100, diluted shares 60 cr. Equity per share?

**Solution.**
- Operating EV = 5,000 + 3,200 = 8,200
- Capitalized overhead = −80 / 0.08 = −1,000
- Stake = 1,500 × 40% = 600; after 30% haircut = 600 × 0.70 = 420
- Bridge: 8,200 − 1,000 (overhead) + 400 (cash) + 420 (stake) − 2,100 (debt)
- = 8,200 − 1,000 = 7,200; +400 = 7,600; +420 = 8,020; −2,100 = **5,920** equity
- Per share = 5,920 / 60 = **₹98.67**

**Check:** overhead correctly subtracted, stake haircut applied, cash added once, debt subtracted → 5,920/60 = 98.67 ✓.

---

### Q15. Compute the conglomerate discount and implied upside

**Problem.** SOTP equity value = ₹12,000 cr; shares 100 cr; stock trades at ₹92. What is the conglomerate discount, and what's the upside if it fully closes?

**Solution.**
- SOTP per share = 12,000 / 100 = ₹120
- Discount = 1 − (92 / 120) = 1 − 0.7667 = **23.3%**
- Upside to close = 120 / 92 − 1 = **+30.4%**

**Check:** trading at 76.7% of intrinsic → 23.3% discount; to go from 92 to 120 is +30.4% ✓. (Note discount % and upside % differ — a 23.3% discount implies 30.4% upside because they use different bases.)

---

### Q16. PV of a tax shield — fixed perpetual debt (MM)

**Problem.** A firm holds permanent fixed debt D = 500, r_d = 7%, tax rate 25%. What is the annual tax shield and its present value?

**Solution.**
- Annual shield = D × r_d × t = 500 × 0.07 × 0.25 = **8.75/year**
- It's a perpetuity discounted at r_d: PV = 8.75 / 0.07 = 125
- Equivalently, MM shortcut: PV = t × D = 0.25 × 500 = **125**

**Check:** both routes give 125 ✓. The 8.75/0.07 confirms the t×D collapse.

---

### Q17. PV of a tax shield — declining LBO schedule

**Problem.** LBO debt schedule (beginning balance): Yr1 600, Yr2 480, Yr3 360, Yr4 240, Yr5 120. r_d = 8%, t = 25%. After year 5 debt is repaid to zero (no terminal shield). PV of the tax shields (discount at r_d)?

**Solution.** Shield_t = balance × 0.08 × 0.25 = balance × 0.02.

| Yr | Balance | Shield | DF @8% | PV |
|---|---|---|---|---|
| 1 | 600 | 12.0 | 0.9259 | 11.11 |
| 2 | 480 | 9.6 | 0.8573 | 8.23 |
| 3 | 360 | 7.2 | 0.7938 | 5.72 |
| 4 | 240 | 4.8 | 0.7350 | 3.53 |
| 5 | 120 | 2.4 | 0.6806 | 1.63 |
| | | | **Total** | **30.22** |

**PV(tax shields) ≈ ₹30.2.**

**Check:** shields shrink with the balance; used r_d (fixed schedule); no terminal shield since debt→0. Sum 11.11+8.23+5.72+3.53+1.63 = 30.22 ✓.

---

### Q18. Full APV valuation (unlevered value + shields → equity)

**Problem.** UFCF: Yr1 90, Yr2 100, Yr3 110, terminal growth 3% thereafter. r_U = 11%. Tax shields (already computed) have PV = 40. Entry net debt = 350. Find V_U, APV, and equity value.

**Solution.**
- DF @11%: 0.9009, 0.8116, 0.7312
- PV of explicit UFCF: 90×0.9009=81.08; 100×0.8116=81.16; 110×0.7312=80.43 → sum = 242.67
- Terminal: UFCF Yr4 = 110 × 1.03 = 113.3; TV at Yr3 = 113.3 / (0.11 − 0.03) = 113.3 / 0.08 = 1,416.25
- PV of TV = 1,416.25 × 0.7312 = 1,035.56
- **V_U = 242.67 + 1,035.56 = 1,278.2**
- **APV = 1,278.2 + 40 = 1,318.2**
- **Equity = 1,318.2 − 350 = 968.2**

**Check:** TV dominates (1,036 of 1,278 ≈ 81%), normal for a growing firm; shield adds ~3%; equity = APV − net debt ✓.

---

### Q19. Prove APV = WACC-DCF under constant leverage

**Problem.** Perpetual unlevered FCF = 80/year, no growth. r_U = 10%, r_d = 6%, t = 25%, constant fixed debt D = 300. Value the equity via APV, then confirm via WACC.

**Solution — APV.**
- V_U = 80 / 0.10 = 800
- PV(shield) = t × D = 0.25 × 300 = 75
- APV = 800 + 75 = 875; Equity = 875 − 300 = **575**

**Solution — WACC.** With V_L = 875, D = 300, E = 575: D/E = 0.5217, D/V = 0.3429, E/V = 0.6571.
- r_e = 0.10 + (0.10 − 0.06)(0.75)(0.5217) = 0.10 + 0.04×0.75×0.5217 = 0.10 + 0.01565 = 0.11565
- WACC = 0.11565×0.6571 + 0.06×0.75×0.3429 = 0.07600 + 0.01543 = 0.09143
- V_L = UFCF / WACC = 80 / 0.09143 = 875.0; Equity = 875 − 300 = **575** ✓

**Check:** both methods give V_L = 875 and equity = 575. WACC 9.14% < r_U 10% by the shield benefit. Identical, as required under constant leverage.

---

### Q20. Segment DCF inside a SOTP

**Problem.** "MixCo": Legacy segment EBITDA 400 at 6× → EV. Growth segment valued by DCF: UFCF Yr1 30, Yr2 45, Yr3 60; terminal growth 4%; segment WACC 12%. Net debt 500, shares 30 cr. Equity per share?

**Solution.**
- Legacy EV = 400 × 6 = 2,400
- Growth DCF, DF @12%: 0.8929, 0.7972, 0.7118
  - PV UFCF: 30×0.8929=26.79; 45×0.7972=35.87; 60×0.7118=42.71 → 105.37
  - TV Yr3 = 60×1.04/(0.12−0.04) = 62.4/0.08 = 780; PV = 780×0.7118 = 555.20
  - Growth EV = 105.37 + 555.20 = 660.6
- Total EV = 2,400 + 660.6 = 3,060.6
- Equity = 3,060.6 − 500 = 2,560.6; per share = 2,560.6 / 30 = **₹85.35**

**Check:** growth EV 660.6; total 3,060.6; equity 2,560.6; /30 = 85.35 ✓.

---

### Q21. Unlever a beta and find r_U for APV

**Problem.** A firm's levered equity beta = 1.4, D/E = 0.8, tax rate 25%. Risk-free 6%, equity risk premium 5.5%. Find the unlevered beta and r_U.

**Solution.**
- β_U = β_L / [1 + (1−t)(D/E)] = 1.4 / [1 + 0.75×0.8] = 1.4 / 1.60 = **0.875**
- r_U = r_f + β_U × ERP = 6% + 0.875 × 5.5% = 6% + 4.8125% = **10.81%**

**Check:** unlevering reduces beta from 1.4 to 0.875 (removes financial risk); r_U = 10.81% is the rate to discount UFCF in an APV ✓.

---

### Q22. APV with distress costs — does the extra leverage add value?

**Problem.** A firm has V_U = 1,000. Adding debt of 400 creates PV(tax shield) = 100 (= t×D at t=25%). But at that leverage, probability of distress = 20% and cost-given-default = 30% of unlevered value. Compute APV with and without distress. Is the leverage value-accretive?

**Solution.**
- PV(distress) = 0.20 × (0.30 × 1,000) = 0.20 × 300 = 60
- APV without distress = 1,000 + 100 = 1,100
- APV with distress = 1,000 + 100 − 60 = **1,040**
- Net value added by leverage = 1,040 − 1,000 = **+40** (still positive, but the ₹100 tax shield is more than a third eaten by distress)

**Interpretation:** leverage is still accretive here (+40), but push leverage higher and distress cost grows faster than the shield — beyond some point net value turns negative. That inflection is the optimal capital structure.

**Check:** distress 60 offsets shield 100 → net +40 over V_U ✓; illustrates the shield-vs-distress trade-off cleanly.

---

**End of Q&A.** If you can do Q17, Q18, and Q19 cold — the declining-schedule shield, a full APV bridge, and the APV=WACC reconciliation — you own the mechanics interviewers actually test.
