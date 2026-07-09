# Q&A — WACC & Discount Rates for Valuation

A mixed bank of theory and numerical questions. Theory answers include a model answer *and* a crisp "how to say it in an interview" line. Numerical answers are fully worked and self-verified.

---

## Theory

### Q1. What is a discount rate, conceptually, and what determines its level?

**Model answer.** A discount rate is an **opportunity cost of capital** — the return an investor could earn on an alternative investment of equivalent risk. It converts future cash into present value. Its level is set by the **risk of the cash flows**, specifically their *systematic* (undiversifiable) risk, because investors can diversify away company-specific risk for free and so aren't compensated for it. Higher systematic risk → higher required return → higher discount rate.

**Say it in an interview:** *"A discount rate is an opportunity cost. It's the return I'd demand on something equally risky, and it's driven by the risk of the cash flows themselves, not by who owns them."*

---

### Q2. Derive/justify the WACC formula.

**Model answer.** A firm is financed by debt D (required return Kd) and equity E (required return Ke), V = D+E. To keep both investor groups whole, the firm must generate Ke×E + Kd×D in returns; as a rate on total capital that's Ke×(E/V) + Kd×(D/V). Because interest is tax-deductible, each dollar of interest saves T in tax, so the effective cost of debt is Kd×(1−T). Hence:

> **WACC = Ke×(E/V) + Kd×(1−T)×(D/V)**

**Say it in an interview:** *"WACC is just the blended required return of everyone who funds the business, weighted by how much each provides, with debt taken after tax because interest is deductible."*

---

### Q3. Why after-tax cost of debt but no after-tax cost of equity?

**Model answer.** Interest is paid *before* tax, so it reduces taxable income and creates a tax shield worth T×interest. Dividends are paid *out of after-tax profit* — they don't reduce the tax bill — so equity earns no shield. The (1−T) therefore sits only on the debt term.

**Say it in an interview:** *"Interest is tax-deductible, dividends aren't. The shield is real for debt and zero for equity, so WACC only after-taxes the debt leg."*

---

### Q4. Explain CAPM and why beta — not total volatility — is the risk measure.

**Model answer.** CAPM: **Ke = Rf + β×ERP**. Rf is the risk-free rate; ERP is the reward for holding equities over the risk-free asset; β measures how much the stock moves with the overall market. Beta, not total volatility, is used because investors diversify: idiosyncratic (company-specific) risk washes out in a portfolio and so isn't priced. Only **systematic** risk — co-movement with the market, captured by beta — earns a premium.

**Say it in an interview:** *"CAPM prices only the risk you can't diversify away. Beta measures that systematic risk; total volatility includes diversifiable noise the market won't pay you for."*

---

### Q5. When do you discount at WACC versus at the cost of equity?

**Model answer.** Match the rate to the claimholders of the cash flow. **FCFF** (cash to all capital providers, before financing) → **WACC** → gives **enterprise value**. **FCFE** or **dividends** (cash to shareholders only, after interest and debt movements) → **cost of equity** → gives **equity value directly**, with no net-debt bridge.

**Say it in an interview:** *"FCFF at WACC to get enterprise value; FCFE at cost of equity to get equity value directly. Never cross the wires."*

---

### Q6. Why must you unlever and relever beta? Walk through the mechanics.

**Model answer.** An observed equity beta reflects **both** business risk **and** the financial risk from that firm's leverage. To value a target you want its *business* risk plus *your* target leverage — so you (1) unlever each comparable's beta with its own D/E and tax rate to isolate the asset beta, (2) average the asset betas for a robust estimate, (3) relever that average to the target's capital structure. Hamada: βU = βL/[1+(1−T)(D/E)]; βL = βU×[1+(1−T)(D/E)].

**Say it in an interview:** *"A raw beta is polluted by the comp's own leverage. I strip leverage out to get pure business risk, average across comps, then re-add my target's leverage."*

---

### Q7. What are the country risk premium and size premium, and where do they go?

**Model answer.** **CRP** compensates for emerging-market risks CAPM misses — political, currency, expropriation, weak rule of law. Estimate it as the sovereign default spread, often scaled by equity/bond volatility (Damodaran). Add it to Ke (optionally weighted by exposure λ) or fold it into a country ERP. **Size premium** reflects the empirical excess return of small caps beyond their CAPM beta (~+1% to +5%); add it to Ke for small companies. Both raise the cost of equity — omitting them for an EM small-cap understates the rate and overstates value.

**Say it in an interview:** *"For an emerging-market small cap I'd add a country risk premium off the sovereign spread and a size premium off the small-cap data — but only once, in one consistent place."*

---

### Q8. What happens to WACC as a company adds leverage?

**Model answer.** It's a **U-shape**. Initially WACC falls: you swap expensive equity for cheaper, tax-shielded debt. But as leverage rises, default risk lifts Kd and financial risk lifts Ke (beta relevers up), and beyond an optimal point the rising costs dominate and WACC turns back up. So "more debt lowers WACC" holds only up to the optimal structure.

**Say it in an interview:** *"WACC is U-shaped in leverage — it falls as cheap debt is added, bottoms at the optimal structure, then rises as default and equity risk take over."*

---

### Q9. What risk-free rate and what maturity do you use, and why market-value target weights?

**Model answer.** Use a long-dated government bond matched to the **currency** and **duration** of the cash flows — the 10-year (or 20-year) Treasury for USD forecasts. Weights should be **market values** (book equity is backward-looking and can be tiny/negative) and ideally **target** weights, because WACC discounts the *whole* forecast horizon and shouldn't be distorted by a temporary structure. Using the current market-value equity also creates circularity (E is both input and output), which target weights sidestep.

**Say it in an interview:** *"Long-dated government bond in the cash flows' currency for Rf; target, market-value weights so I capture the sustainable structure and avoid the circularity in the equity value."*

---

### Q10. Why is the discount rate the most sensitive assumption in a DCF?

**Model answer.** Because the terminal value — often 60–80% of total value — depends on the spread (WACC − g), and that spread is small, so a 100bp change in WACC moves the denominator a lot. On a stable company, cutting WACC by 1% can lift EV 15–25%. That leverage is why interviewers stress the discount rate and why you should always run a WACC/g sensitivity table.

**Say it in an interview:** *"Terminal value dominates a DCF and it's driven by WACC minus g — a tiny spread — so small rate changes swing value hugely. I always sensitise it."*

---

## Numerical

### Q11. Basic WACC.

Rf = 3.5%, β = 1.30, ERP = 5.5%, E = $8,000m, D = $2,000m, Kd = 6.0%, T = 25%. Find WACC.

**Solution.**
- Ke = 3.5% + 1.30×5.5% = 3.5% + 7.15% = **10.65%**
- Kd(1−T) = 6.0%×0.75 = **4.5%**
- V = 10,000; E/V = 0.80, D/V = 0.20
- WACC = 10.65%×0.80 + 4.5%×0.20 = 8.52% + 0.90% = **9.42%**

**Check:** between 4.5% and 10.65%. ✓

---

### Q12. Unlever a beta.

A comp has levered β = 1.40, D/E = 0.50, T = 30%. Find the unlevered (asset) beta.

**Solution.**
βU = 1.40 / [1 + (1−0.30)×0.50] = 1.40 / [1 + 0.35] = 1.40 / 1.35 = **1.037**

**Check:** unlevered < levered (leverage removed), as expected. ✓

---

### Q13. Relever to a new structure.

Take βU = 1.037 from Q12. Relever to a target D/E = 0.20, T = 30%.

**Solution.**
βL = 1.037 × [1 + 0.70×0.20] = 1.037 × 1.14 = **1.182**

**Check:** relevered beta (1.182) < original 1.40 because target leverage (0.20) is lower than the comp's (0.50). ✓

---

### Q14. Full private-company WACC via comps.

Two comps: (A) βL 1.20, D/E 0.40; (B) βL 1.00, D/E 0.20. Both T = 25%. Target D/E = 0.30, T = 25%, Rf = 4%, ERP = 5%, size premium 1.5%, Kd = 6%. Find Ke and WACC.

**Solution.**
- Unlever A: 1.20/[1+0.75×0.40] = 1.20/1.30 = 0.923
- Unlever B: 1.00/[1+0.75×0.20] = 1.00/1.15 = 0.870
- Avg βU = (0.923+0.870)/2 = **0.896**
- Relever to 0.30: 0.896×[1+0.75×0.30] = 0.896×1.225 = **1.098**
- Ke = 4% + 1.098×5% + 1.5% = 4% + 5.49% + 1.5% = **10.99%**
- D/E 0.30 → D/V = 0.30/1.30 = 0.2308, E/V = 0.7692
- Kd(1−T) = 6%×0.75 = 4.5%
- WACC = 10.99%×0.7692 + 4.5%×0.2308 = 8.454% + 1.039% = **9.49%**

**Check:** WACC between 4.5% and 10.99%. ✓

---

### Q15. Cost of debt via synthetic rating.

EBIT = $240m, interest expense = $40m, Rf = 4%. Coverage of 6× maps to a default spread of 1.75%. T = 25%. Find pre- and after-tax cost of debt.

**Solution.**
- Interest coverage = 240/40 = 6.0× → spread 1.75%
- Pre-tax Kd = Rf + spread = 4% + 1.75% = **5.75%**
- After-tax Kd = 5.75%×0.75 = **4.31%**

**Check:** after-tax below pre-tax by exactly T. ✓

---

### Q16. Terminal value and its share of EV.

FCFF₅ = $150m, g = 2.5%, WACC = 9%. Find TV₅ and its PV, then its share of a DCF whose explicit-period PV is $500m.

**Solution.**
- TV₅ = 150×1.025/(0.09−0.025) = 153.75/0.065 = **$2,365.4m**
- Discount factor Y5 = 1/1.09^5 = 1/1.5386 = 0.6499
- PV(TV) = 2,365.4×0.6499 = **$1,537.3m**
- EV = 500 + 1,537.3 = **$2,037.3m**
- TV share = 1,537.3/2,037.3 = **75.5%**

**Check:** WACC (9%) > g (2.5%), TV positive and finite; TV share ~75% is typical for a growing firm. ✓

---

### Q17. EV-to-equity bridge and per share.

EV = $2,037m. Total debt $600m, cash $90m, preferred $50m, minority interest $70m, non-operating investments $30m, diluted shares 150m. Find equity value and value per share.

**Solution.**
- Net debt = 600 − 90 = 510
- Equity = EV − net debt − preferred − minority + non-op = 2,037 − 510 − 50 − 70 + 30 = **$1,437m**
- Per share = 1,437/150 = **$9.58**

**Check:** every non-common claim subtracted, non-operating asset added back, then ÷ diluted shares. ✓

---

### Q18. FCFE discounted at cost of equity (matching principle).

FCFE₁ = $80m growing at 3% forever. Rf = 4%, β = 1.1, ERP = 5%. Value the equity and per share on 120m shares.

**Solution.**
- Ke = 4% + 1.1×5% = 4% + 5.5% = **9.5%**
- Equity value = FCFE₁/(Ke−g) = 80/(0.095−0.03) = 80/0.065 = **$1,230.8m**
- Per share = 1,230.8/120 = **$10.26**

**Note:** discounted FCFE at **Ke**, got equity value **directly** — no net-debt bridge. That's the matching principle in action.

**Check:** Ke (9.5%) > g (3%), positive finite value. ✓

---

### Q19. WACC sensitivity — quantify the leverage.

Take Q16's company (FCFF₅ = 150, g = 2.5%, explicit PV = 500). Recompute EV if WACC falls from 9% to 8%. By what % does EV rise? (Assume explicit-period PV rises ~3% to $515m at the lower rate.)

**Solution.**
- New TV₅ = 150×1.025/(0.08−0.025) = 153.75/0.055 = **$2,795.5m**
- New DF Y5 = 1/1.08^5 = 1/1.4693 = 0.6806
- PV(TV) = 2,795.5×0.6806 = **$1,902.7m**
- New EV = 515 + 1,902.7 = **$2,417.7m**
- Old EV = 2,037.3 → increase = (2,417.7−2,037.3)/2,037.3 = **+18.7%**

**Check:** a 100bp WACC cut lifted EV ~19% — squarely in the "15–25%" range quoted in the chapter, driven by the terminal value. ✓

---

### Q20. Country risk premium build.

EM company. Rf(US) = 4%, β = 1.2, mature ERP = 5%. Sovereign default spread = 2.5%; equity/bond volatility ratio = 1.4. Company earns 60% of revenue domestically (λ = 0.6). Find Ke using the lambda-weighted scaled CRP.

**Solution.**
- Scaled CRP = 2.5%×1.4 = **3.5%**
- Exposure-weighted CRP = 0.6×3.5% = **2.1%**
- Ke = 4% + 1.2×5% + 2.1% = 4% + 6.0% + 2.1% = **12.1%**

**Check:** lambda < 1 reduces the full 3.5% CRP to 2.1%, reflecting partial exposure. ✓

---

### Q21. Full WACC with country premium, then bridge.

Continue Q20 (Ke = 12.1%). Kd = 9% (includes country spread), T = 30%, target E/V = 0.65, D/V = 0.35. FCFF: Y1 100, Y2 108, Y3 117 then TV at g = 3%. Find WACC, EV, and equity value if net debt = $150m, minority = $20m, shares 100m.

**Solution.**
- Kd(1−T) = 9%×0.70 = 6.3%
- WACC = 12.1%×0.65 + 6.3%×0.35 = 7.865% + 2.205% = **10.07%**
- TV₃ = 117×1.03/(0.1007−0.03) = 120.51/0.0707 = **$1,704.5m**
- DFs at 10.07%: Y1 1/1.1007 = 0.9085; Y2 1/1.1007² = 0.8254; Y3 1/1.1007³ = 0.7499
- PV Y1 = 100×0.9085 = 90.85; PV Y2 = 108×0.8254 = 89.14; PV Y3 = 117×0.7499 = 87.74
- PV(TV) = 1,704.5×0.7499 = 1,278.2
- EV = 90.85 + 89.14 + 87.74 + 1,278.2 = **$1,545.9m**
- Equity = 1,545.9 − 150 − 20 = **$1,375.9m**; per share = 1,375.9/100 = **$13.76**

**Check:** WACC (10.07%) between 6.3% and 12.1%; > g (3%); bridge reconciles. ✓

---

### Q22. Circularity / iteration intuition (numerical illustration).

A firm's target D/V is uncertain. At E/V = 0.70 the WACC computes to 9.6%, giving equity value of $2,100m; total debt is $900m, so implied D/V = 900/(900+2100) = 0.30, E/V = 0.70. Is the assumption self-consistent?

**Solution.**
- Assumed E/V = 0.70. Implied from output: E = 2,100, D = 900, V = 3,000 → E/V = 2,100/3,000 = **0.70**. 
- The assumed weight equals the weight implied by the DCF output → **the WACC is self-consistent; no further iteration needed.**

**Check:** input weight = output-implied weight → converged. Had they differed (say output E/V = 0.75), you'd recompute WACC at 0.75 and re-run until the two match — that's the iteration loop, avoided in practice by simply fixing target weights up front. ✓

---

*End of Q&A bank.*
