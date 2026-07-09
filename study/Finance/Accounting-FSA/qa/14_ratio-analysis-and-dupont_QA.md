# Q&A — Ratio Analysis & the DuPont Framework

A mixed bank of conceptual and numerical questions. Numericals are fully solved and self-verified. Conceptual answers include the crisp "how to say it in an interview" line.

---

## Conceptual questions

### Q1. Why do we use ratios at all instead of raw numbers?

**Model answer.** Raw figures carry *scale*, so a ₹500 cr profit is meaningless until you know the capital that produced it. A ratio divides one figure by another to strip scale out, leaving a rate, proportion, or multiple that is comparable across companies of any size, across years, and against industry benchmarks.

**Interview line:** "A ratio removes scale so I can compare a corner shop with Reliance on the same footing — it turns absolute rupees into a rate I can actually judge."

---

### Q2. Why does the quick ratio exclude inventory?

**Model answer.** Inventory is the least liquid current asset — to become cash it must first be *sold* (creating a receivable) and then *collected*. In distress it's often sold at fire-sale prices or not at all. The quick ratio asks the harsher question: could you cover current liabilities without selling a single item of stock?

**Interview line:** "Quick ratio is the acid test — it assumes your inventory is worthless and asks if you can still pay your bills."

---

### Q3. Why use COGS for inventory turnover but Revenue for receivables turnover?

**Model answer.** You match the numerator's *valuation basis* to the denominator's. Inventory sits on the books at cost, so the matching flow is COGS. Receivables sit at selling price, so the matching flow is Revenue. Matching the basis keeps the ratio economically clean; mixing them (e.g., Revenue ÷ Inventory) distorts the true turnover by the gross margin.

**Interview line:** "Cost with cost, price with price — inventory is at cost so use COGS; receivables are at sale price so use revenue."

---

### Q4. Explain the 3-step and 5-step DuPont decompositions.

**Model answer.** 3-step: ROE = Net Margin × Asset Turnover × Equity Multiplier — profitability, efficiency, leverage. 5-step splits net margin into Tax Burden (NI/Pretax) × Interest Burden (Pretax/EBIT) × Operating Margin (EBIT/Revenue), then × Asset Turnover × Financial Leverage. The extra granularity separates *operating* performance from *financing* and *tax* effects, so you can see, for example, leverage lifting one term while its interest cost drags another.

**Interview line:** "DuPont turns 'ROE moved' into 'ROE moved *because of* margin, turnover, or leverage' — it's the difference between observing and diagnosing."

---

### Q5. Two firms have identical 18% ROE. How do you decide which is the better business?

**Model answer.** Decompose both. Quality ROE comes from strong operating margin and asset turnover with modest leverage — it's durable and operations-driven. Engineered ROE comes from a high equity multiplier on a mediocre operating margin — it's fragile, because a downturn hits a thin equity base and interest burden can spike. Same ROE, very different risk profile.

**Interview line:** "Same ROE can be a fortress or a house of cards — I'd DuPont both and pay up for the one whose returns come from operations, not leverage."

---

### Q6. Why is ROIC compared to WACC and not ROE?

**Model answer.** ROIC uses NOPAT over invested capital — it's pre-financing and counts *all* capital, so it measures the pure operating return, uncontaminated by how the firm is financed. WACC is the blended cost of *all* that capital. Comparing like-for-like (operating return vs total capital cost) is the clean value test. ROE, being post-leverage and post-tax, blends operating skill with financing choices and can't be cleanly compared to a cost of capital.

**Interview line:** "ROIC and WACC are apples to apples — both cover all capital, unlevered. ROE mixes in leverage, so it's the wrong number for the value test."

---

### Q7. A company's ROIC is 9% and its WACC is 12%. Management wants to grow. What do you advise?

**Model answer.** Push back hard. ROIC below WACC means each rupee invested earns 9% against a 12% cost — destroying 3% of value per rupee. Growth *accelerates* the destruction. The right actions are to fix operations to lift ROIC above the hurdle, or if that's not achievable, return cash via dividends/buybacks rather than reinvest.

**Interview line:** "When ROIC is below WACC, growth is the enemy — you're just burning value faster. Fix the returns first or give the cash back."

---

### Q8. What happens to ROE, and to the *quality* of ROE, after a debt-funded buyback?

**Model answer.** ROE typically rises: the buyback shrinks equity (denominator) and the new debt raises the equity multiplier — both lift ROE. But quality falls: added interest lowers net income and the interest-burden term, and financial risk climbs. The higher ROE is leverage-driven, not operations-driven.

**Interview line:** "ROE goes up, but it's financial engineering, not better operations — I'd flag that coverage is now thinner and the ROE is lower quality."

---

### Q9. Current ratio jumped from 1.2 to 2.5 year over year. Is that good?

**Model answer.** Not necessarily — investigate composition. If driven by rising cash, good. If driven by unsold inventory piling up or receivables ballooning because customers aren't paying, it's deteriorating quality disguised as improving liquidity. Check quick ratio, DSO and DIO trends.

**Interview line:** "A rising current ratio can be a warning, not a comfort — I'd check whether it's cash going up or dead inventory and uncollected receivables."

---

### Q10. Why does DPO *subtract* in the cash conversion cycle?

**Model answer.** DIO and DSO measure how long cash is *tied up* — building inventory and waiting for customers to pay. DPO measures how long you *delay* your own cash outflow by not paying suppliers immediately, which is a free source of financing. Because it offsets the cash tied up, it subtracts. CCC = DIO + DSO − DPO. A negative CCC means suppliers fund your growth — you collect before you pay.

**Interview line:** "Payables are free financing — the longer you take to pay suppliers, the less of your own cash is trapped in the cycle, so DPO subtracts."

---

### Q11. Why must the cost of debt in WACC be after-tax?

**Model answer.** Interest is tax-deductible, so each rupee of interest saves the company tax at its marginal rate. The *effective* cost to the firm is therefore Rd × (1 − t). Using the pre-tax rate overstates WACC and understates value. Note the tax shield applies only to debt, not equity (dividends aren't deductible).

**Interview line:** "Interest is deductible, so debt costs the firm Rd times one-minus-tax — forgetting the shield inflates your hurdle rate."

---

### Q12. Why is EBITDA not the same as free cash flow?

**Model answer.** EBITDA ignores three real cash needs: capex (maintaining/growing the asset base), changes in working capital (cash tied up in inventory and receivables), and cash taxes. A capital-intensive firm can post fat EBITDA and still bleed cash. FCF = EBITDA − cash taxes − capex − ΔNWC.

**Interview line:** "EBITDA is earnings before the bad stuff — it flatters capital-heavy businesses because it ignores the capex and working capital they actually have to fund."

---

## Numerical problems

### Q13. Compute the full liquidity and leverage panel.

A company reports: Current assets 900 (of which inventory 300, cash 120), Current liabilities 400, Total interest-bearing debt 700, EBITDA 250, EBIT 180, Interest expense 45, Equity 800. All ₹ cr.

**Solution.**
- Current ratio = 900 / 400 = **2.25x**
- Quick ratio = (900 − 300) / 400 = 600 / 400 = **1.50x**
- Cash ratio = 120 / 400 = **0.30x**
- D/E = 700 / 800 = **0.875x**
- Debt-to-capital = 700 / (700 + 800) = 700 / 1,500 = **0.467 (46.7%)**
- Net Debt / EBITDA = (700 − 120) / 250 = 580 / 250 = **2.32x**
- Interest coverage = EBIT / Interest = 180 / 45 = **4.0x**

**Reading:** healthy liquidity (quick 1.5x), moderate leverage (net debt 2.3x EBITDA), comfortable 4x interest coverage — investment-grade profile.

---

### Q14. 3-step DuPont from scratch.

Net income 120, Revenue 1,500, Total assets 1,000, Equity 500 (all ₹ cr). Compute ROE via DuPont and confirm directly.

**Solution.**
- Net margin = 120 / 1,500 = 0.08 (8%)
- Asset turnover = 1,500 / 1,000 = 1.5x
- Equity multiplier = 1,000 / 500 = 2.0x
- ROE = 0.08 × 1.5 × 2.0 = **0.24 (24%)**

Direct check: ROE = 120 / 500 = 0.24 = **24%** ✓

---

### Q15. 5-step DuPont and interpretation.

Given: Revenue 1,500, EBIT 195, Pretax income 150, Net income 120, Total assets 1,000, Equity 500 (₹ cr). Decompose ROE five ways and reconcile.

**Solution.**
- Tax burden = NI / Pretax = 120 / 150 = 0.800
- Interest burden = Pretax / EBIT = 150 / 195 = 0.7692
- Operating margin = EBIT / Rev = 195 / 1,500 = 0.130
- Asset turnover = 1,500 / 1,000 = 1.500
- Financial leverage = 1,000 / 500 = 2.000

ROE = 0.800 × 0.7692 × 0.130 × 1.500 × 2.000
- 0.800 × 0.7692 = 0.6154
- × 0.130 = 0.08000
- × 1.500 = 0.12000
- × 2.000 = **0.24000 (24%)**

Direct check: 120 / 500 = **24%** ✓

**Interpretation:** Operating margin is a solid 13%, but interest burden of 0.77 shaves ~23% off operating profit — the cost of leverage. Leverage of 2.0x doubles the equity return. Tax retains 80% (20% effective rate).

---

### Q16. "Why did ROE change?" attribution.

Year 1: net margin 8%, asset turnover 1.5x, equity multiplier 2.0x.
Year 2: net margin 7%, asset turnover 1.6x, equity multiplier 2.1x.
Compute both ROEs and explain the driver.

**Solution.**
- ROE(Y1) = 0.08 × 1.5 × 2.0 = **0.240 (24.0%)**
- ROE(Y2) = 0.07 × 1.6 × 2.1 = 0.07 × 1.6 = 0.112; × 2.1 = **0.2352 (23.5%)**
- Change = 23.5% − 24.0% = **−0.5 pts**

**Attribution:** ROE fell ~50bp *despite* higher turnover (1.5→1.6) and higher leverage (2.0→2.1), because the 100bp margin decline (8%→7%) outweighed both gains. **Interview framing:** "The margin compression dominated — and note the improvement is partly propped up by more leverage, so the underlying operating deterioration is worse than the headline 0.5-point drop suggests."

---

### Q17. Cash conversion cycle.

COGS 1,200, Revenue 2,000, average inventory 200, average receivables 250, average payables 150 (₹ cr). Compute DIO, DSO, DPO, CCC.

**Solution.**
- DIO = (200 / 1,200) × 365 = 0.16667 × 365 = **60.8 days**
- DSO = (250 / 2,000) × 365 = 0.125 × 365 = **45.6 days**
- DPO = (150 / 1,200) × 365 = 0.125 × 365 = **45.6 days**
- CCC = 60.8 + 45.6 − 45.6 = **60.8 days**

**Reading:** Cash is tied up ~61 days per operating cycle. Payables (45.6 days) fully offset receivables (45.6 days), so the cycle is essentially inventory-driven. Cutting DIO is the biggest lever to free up cash.

---

### Q18. ROIC computation.

EBIT 400, tax rate 30%, total debt 600, equity (book) 1,400, cash 200 (₹ cr). Compute NOPAT, invested capital, and ROIC.

**Solution.**
- NOPAT = EBIT × (1 − t) = 400 × 0.70 = **280**
- Invested capital = Debt + Equity − Cash = 600 + 1,400 − 200 = **1,800**
- ROIC = NOPAT / IC = 280 / 1,800 = **15.56%**

---

### Q19. WACC computation.

Market equity 3,000, market debt 1,000. Rf 7%, β 1.1, ERP 5.5%, pre-tax cost of debt 8%, tax 30%. Compute WACC.

**Solution.**
- Cost of equity Re = Rf + β × ERP = 7% + 1.1 × 5.5% = 7% + 6.05% = **13.05%**
- After-tax cost of debt = 8% × (1 − 0.30) = **5.6%**
- V = 3,000 + 1,000 = 4,000; E/V = 0.75; D/V = 0.25
- WACC = 0.75 × 13.05% + 0.25 × 5.6% = 9.7875% + 1.40% = **11.19%**

---

### Q20. ROIC vs WACC and EVA — the full value test.

Combine Q18 and Q19: ROIC = 15.56%, invested capital 1,800, WACC = 11.19%. Is value being created? Compute EVA two ways.

**Solution.**
- Spread = ROIC − WACC = 15.56% − 11.19% = **+4.37%** → positive, value is created.
- EVA (spread method) = 4.37% × 1,800 = **₹78.7 cr**
- EVA (residual-income method) = NOPAT − WACC × IC = 280 − 0.1119 × 1,800 = 280 − 201.4 = **₹78.6 cr** ✓ (rounding)

**Verdict:** The company earns a 437bp spread over its cost of capital, generating ~₹79 cr of economic profit per year. Value is being created — management should reinvest in growth, since every rupee deployed earns well above the hurdle.

---

### Q21. Debt-funded buyback — quantify the ROE effect.

Before: Net income 150, Equity 1,000, no interest (all-equity). The company borrows 400 at 10% pre-tax to buy back 400 of equity. Tax 25%. Show the new net income and ROE, and comment on quality.

**Solution.**
- New interest = 400 × 10% = 40 (pre-tax)
- After-tax cost of that interest = 40 × (1 − 0.25) = 30
- New net income = 150 − 30 = **120**
- New equity = 1,000 − 400 = **600**
- ROE before = 150 / 1,000 = **15.0%**
- ROE after = 120 / 600 = **20.0%**

**Comment:** ROE jumped from 15% to 20% — but net income actually *fell* (150→120). The entire ROE increase is leverage: a smaller equity base earning slightly less absolute profit. This is textbook lower-quality ROE. In an interview: "ROE rose 500bp purely from the buyback shrinking equity and adding leverage; earnings fell, and financial risk is now higher — I'd never mistake this for operational improvement."

---

### Q22. Cross-industry comparison — same ROE, decompose the difference.

**Grocer:** net margin 2%, asset turnover 5.0x, equity multiplier 2.0x.
**Software firm:** net margin 25%, asset turnover 0.6x, equity multiplier 1.33x.
Compute each ROE and explain why both models "work."

**Solution.**
- Grocer ROE = 0.02 × 5.0 × 2.0 = **0.20 (20%)**
- Software ROE = 0.25 × 0.6 × 1.33 = 0.25 × 0.6 = 0.15; × 1.33 = **0.1995 ≈ 20%**

**Explanation:** Both reach ~20% ROE by opposite routes. The grocer runs razor-thin 2% margins but spins assets 5x a year — a *volume/velocity* model. The software firm turns assets slowly (0.6x) but keeps 25% of every sale — a *margin* model. Neither is "better" in the abstract; each is optimised for its industry's economics. **Interview takeaway:** never compare margins or turnover across industries in isolation — DuPont shows how the levers substitute for one another to reach the same return.

---

**Self-check note:** Every numerical answer above has been verified — DuPont products reconcile to the direct ROE, EVA computed two ways agrees, and the balance-sheet identities hold. Practise Q14–Q16 and Q20 until the decompositions are reflexive; those are the ones interviewers reach for most.
