# Q&A — Applied Equity Valuation

Theory plus fully-solved numerical problems on turning a model into a target price and rating.

---

### Q1. How would you value a company for a research recommendation?

**Model answer.** Triangulate two independent methods: a DCF (project FCFF, discount at WACC, add terminal value, bridge enterprise value to equity value, divide by diluted shares) for intrinsic value, and relative valuation (apply the appropriate peer multiple — EV/EBITDA, P/E, EV/Sales, or P/B depending on sector) for relative value. Weight or range the two into a target price, compare to the market price, and set a rating from the implied return.

---

### Q2. Worked — DCF to target price.
*FCFF in year 5 = ₹150 cr, WACC = 10.5%, terminal growth = 4%. Sum of PV of years 1-5 FCFF = ₹480 cr. Net debt = ₹250 cr. Diluted shares = 80 mn.*

**Model answer.**
```
TV = 150 × 1.04 / (0.105 − 0.04) = 156 / 0.065 = ₹2,400 cr (undiscounted, at year 5)
PV(TV) = 2,400 / (1.105)^5 = 2,400 / 1.6763 ≈ ₹1,431.6 cr
Enterprise Value = 480 + 1,431.6 = ₹1,911.6 cr
Equity Value = 1,911.6 − 250 = ₹1,661.6 cr
Value per share = 1,661.6 / 80 = ₹20.77
```
If the market price is ₹17, upside ≈ (20.77−17)/17 ≈ 22% → a Buy on the standard >15% threshold.

---

### Q3. Worked — reconciling DCF with a comps cross-check.
*Continuing Q2: peers trade at 9.5× EV/EBITDA; the company's current-year EBITDA is ₹260 cr.*

**Model answer.**
```
Implied EV = 260 × 9.5 = ₹2,470 cr
Implied Equity Value = 2,470 − 250 = ₹2,220 cr
Implied value per share = 2,220 / 80 = ₹27.75
```
DCF says ₹20.77, comps say ₹27.75 — a real gap. The analyst must explain it (e.g. "peers are pricing in faster medium-term growth than my base-case forecast assumes") and state which figure they trust more, rather than silently averaging the two or picking the more favourable number without justification.

---

### Q4. Why doesn't EV/EBITDA work for valuing a bank?

**Model answer.** EV/EBITDA assumes debt is a financing choice separate from operations — but for a bank, deposits (debt-like liabilities) *are* the raw material of the business, and "EBITDA" is not economically meaningful when interest income/expense is the core operating activity, not a financing afterthought. Banks are instead valued on **P/B linked to ROE** (a bank earning above its cost of equity should trade above 1x book, and vice versa) or a **dividend-discount/residual-income model**.

---

### Q5. Worked — P/B via ROE for a bank.
*Bank's sustainable ROE = 15%, cost of equity = 12%, long-run growth = 8%.*

**Model answer.** Using the Gordon-growth-derived P/B relationship:
```
P/B = (ROE − g) / (Ke − g) = (0.15 − 0.08) / (0.12 − 0.08) = 0.07 / 0.04 = 1.75x
```
If current book value per share is ₹200, the implied fair value is ₹200 × 1.75 = **₹350/share**. The intuition: a bank earning ROE above its cost of equity (15% > 12%) deserves to trade above 1x book, and the multiple compresses as the ROE-Ke spread narrows.

---

### Q6. A high-growth, loss-making company can't be DCF'd on near-term FCFF — how do you value it?

**Model answer.** Use revenue multiples (EV/Sales) benchmarked to comparable growth-stage peers as the primary cross-check, alongside a longer-horizon DCF with an explicit, well-reasoned path to profitability (modelling the margin trajectory year by year rather than assuming near-term steady-state margins), and always stress-test the terminal-margin assumption specifically, since that single assumption typically drives most of the valuation for a pre-profit name.

---

### Q7. What's wrong with presenting a single-point target price with no range?

**Model answer.** It implies false precision about inherently uncertain inputs (WACC, terminal growth, peer multiples all carry real estimation error) and hides how sensitive the conclusion is to assumptions at the edge of a reasonable range. A credible target price is always accompanied by a sensitivity table (e.g. WACC × terminal growth) or a football-field chart spanning the methods used, so a reader can see how much of the "Buy" case depends on optimistic inputs.

---

### Q8. Your DCF and comps disagree by more than 10%. Is that a red flag on your work?

**Model answer.** Not automatically — the two methods answer different questions (DCF reflects the analyst's own forecast, comps reflect what the market is currently paying for similar growth/risk) and can legitimately diverge when the analyst's view differs from what's priced into peers. It becomes a red flag only if the analyst can't articulate *why* they diverge — an unexplained gap suggests an error somewhere (a modelling mistake, a wrong peer set, or an unrealistic terminal assumption) rather than a genuine, defensible difference of view.
