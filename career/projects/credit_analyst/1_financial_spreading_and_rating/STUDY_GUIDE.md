# Study Guide — Credit Spreading, Serviceability & Internal Rating

A defence sheet for this project. If you can explain everything here, you can
defend every line of the code in an interview.

---

## 30-second pitch

> "I built a small credit-analysis engine in Python. It spreads a borrower's
> financials into one standard template, computes the leverage / coverage /
> liquidity / profitability / working-capital ratios a committee looks at,
> builds a cash-flow-based DSCR against the debt schedule, and runs a
> transparent weighted scorecard that outputs an internal rating band (AAA–D),
> an indicative PD and a written rationale. Then it stress-tests EBITDA, rates
> and revenue and shows the rating migrate to the downside. It writes an Excel
> workbook and charts. Three sample borrowers rate AA, BBB and C by design so
> the whole spectrum is exercised."

---

## Code walkthrough (what each module does)

- **data.py** — loads the long-format CSVs, coerces to numbers, reindexes onto a
  fixed canonical line-item order, and validates four accounting identities
  (EBITDA build, EBIT build, Total Debt = ST + LT, Assets = Liabilities +
  Equity). Output: `code → DataFrame` (rows = line items, columns = years).
- **ratios.py** — `compute_year` returns every ratio for one year as a dict;
  `compute_ratios` stacks all years. `_safe` returns NaN on a zero/missing
  denominator instead of crashing.
- **serviceability.py** — `cfads`, `debt_service`, `dscr`, `icr`,
  `headroom_class`, and a per-year `serviceability_table`. Optional EBITDA /
  interest / tax overrides let the scenario module reuse the exact formulas.
- **rating.py** — factor weights (must sum to 0.65 financial + 0.35 business,
  asserted at import), threshold-based sub-score functions, `band_from_score`,
  `scorecard` (returns the breakdown table + composite + band + PD), and
  `rating_rationale`.
- **scenario.py** — `make_stressed` rebuilds a consistent stressed spread;
  `recompute` re-runs ratios + rating on it; `scenario_table` runs all eight
  scenarios. Crucially it calls the *same* rating code, not a copy.
- **reporting.py** — builds the Summary table, writes the multi-sheet workbook,
  and renders three charts on the headless `Agg` backend.

---

## Core credit concepts

### The 5 Cs of Credit
- **Character** — willingness to pay: management quality, track record, governance. (Business factor in the scorecard.)
- **Capacity** — ability to pay: cash flow vs debt service → **DSCR / ICR**.
- **Capital** — the owner's skin in the game: equity, net worth, gearing.
- **Collateral** — the fallback: security, asset cover (drives LGD, not modelled in depth here).
- **Conditions** — the environment: industry cyclicality, the economic cycle, use of proceeds. (Business factor.)

### Financial spreading
Re-casting a borrower's as-reported statements into a **standard template** so
that different companies and years are comparable, adjustments (one-offs,
leases, related-party items) are normalised, and every ratio is computed off the
same definitions. This project standardises into one canonical line-item list
and validates the identities.

### DSCR vs ICR — and why both
- **ICR (Interest Coverage Ratio)** = EBIT / Interest. Can the borrower cover
  just the *interest*?
- **DSCR (Debt-Service Coverage Ratio)** = CFADS / (Interest + Scheduled
  Principal). Can cash flow cover interest **and** the principal amortisation
  falling due?
- A borrower can pass ICR comfortably and still fail DSCR once bulky principal
  repayments are layered on — which is exactly why term-loan covenant packs test
  DSCR, not just interest cover.

### CFADS (Cash Flow Available for Debt Service)
`CFADS = EBITDA − cash taxes − maintenance capex`. EBITDA is a cash proxy;
taxes and the capex needed just to keep the assets running rank ahead of / beside
lenders. Growth capex is treated as discretionary (this project uses a 40%
maintenance split), so it is **not** a fixed charge. In full project finance you
would also add/subtract the working-capital movement.

### Leverage measures
- **Debt/EBITDA** and **Net Debt/EBITDA** (net of cash) — "how many years of
  cash earnings equal the debt". <2x is strong, >6x is stressed.
- **Debt/Equity** and **Gearing = Debt/(Debt+Equity)** — the capital-structure
  cushion. Negative equity (Deccan) makes Debt/Equity meaningless — a red flag
  in itself, which is why the scorecard scores gearing off the debt-to-cap ratio
  and floors negative-equity cases.

### Working-capital cycle
- **DSO** = Receivables/Revenue×365 (how long to collect).
- **DIO** = Inventory/COGS×365 (how long stock sits).
- **DPO** = Payables/COGS×365 (how long we take to pay suppliers).
- **CCC = DSO + DIO − DPO** — days of cash tied up in operations. A lengthening
  CCC quietly drains liquidity even when the P&L looks fine.

### Covenants
Contractual tests in the loan agreement. **Maintenance** covenants are tested
every period (e.g. DSCR ≥ 1.25x, Net Debt/EBITDA ≤ 3.5x, current ratio ≥ 1.0);
**incurrence** covenants bite only on an action (raising new debt, paying a
dividend). Breaching a covenant is an event of default that lets the lender
re-price, demand cure, or accelerate. The DSCR chart plots the 1.0 breakeven and
a 1.25 covenant line for exactly this reason.

### PD / LGD / EAD and Expected Loss
- **PD** — Probability of Default (this scorecard outputs an indicative 1-yr PD per band).
- **LGD** — Loss Given Default = 1 − recovery; driven by collateral/seniority.
- **EAD** — Exposure at Default (drawn + expected drawdown of undrawn lines).
- **Expected Loss = PD × LGD × EAD.** This project models the PD leg via the
  rating; LGD/EAD would extend it. This is also the Basel IRB vocabulary.

### Through-the-cycle vs point-in-time
A **PIT** rating reflects current conditions and is more volatile; a **TTC**
rating looks through the cycle and is more stable. Bank internal ratings usually
aim TTC. Our stress scenarios are the manual version of asking "where does this
rating sit at the bottom of the cycle?".

### Rating scorecard design
Real internal models are weighted scorecards: quantitative factors (leverage,
coverage, profitability, size) + qualitative factors (management, industry,
market position), each scored and weighted, mapped to a masterscale calibrated
to historical default rates. This project is a faithful miniature: 65% financial
/ 35% business, explicit thresholds, transparent composite → band → PD.

---

## Interview Q&A (15–20)

**1. What does "spreading" mean and why do it?**
Re-casting as-reported statements into one standard template so companies/years
are comparable and every ratio uses the same definition. It's the foundation for
everything downstream.

**2. Walk me through your DSCR.**
CFADS ÷ debt service. CFADS = EBITDA − cash taxes − maintenance capex; debt
service = interest + scheduled principal. For the strong borrower it's ~3.0x,
for the distressed one 0.25x — i.e. cash covers only a quarter of what's due.

**3. Why EBITDA − maintenance capex, not all capex?**
Growth capex is discretionary — under stress you can defer expansion. Only the
capex needed to keep the existing asset base running is a genuine fixed charge.
I used a 40% maintenance split, which is a stated, adjustable assumption.

**4. ICR vs DSCR — when do they diverge?**
When principal amortisation is large relative to interest. A borrower can cover
interest 5x yet fail DSCR because a big principal tranche falls due. That's why
lenders test DSCR.

**5. Net Debt/EBITDA of 16x — what does that tell you?**
The borrower would need 16 years of current cash earnings to repay debt — deeply
distressed, well beyond the ~3–4x investment-grade comfort zone. Combined with
negative equity and DSCR < 1, it's effectively a default-risk credit.

**6. Your rated borrower has negative equity. What breaks?**
Debt/Equity becomes meaningless (negative). I score capital structure off
gearing = Debt/(Debt+Equity) and floor negative-net-worth cases to the worst
sub-score, because negative net worth is itself a severe red flag.

**7. How does the scorecard produce a rating?**
Nine factors, each mapped to a 0–100 sub-score by explicit thresholds, weighted
65% financial / 35% business, summed to a composite 0–100, then mapped to a band
(AAA…D) with an indicative PD. The whole breakdown is in the Excel "Rating" sheet.

**8. Are those PDs real?**
They're illustrative teaching anchors, not a regulator-calibrated masterscale.
In production you'd calibrate bands to observed default frequencies over a long
window. I'm explicit about that — the *mechanics* mirror a real model.

**9. How do you stress test?**
I shock EBITDA (−10/−20/−30%), rates (+100/+200 bps on the whole debt stack) and
revenue (−15%, flowing to EBITDA through the gross margin with opex fixed), plus
a combined downside. Each shock rebuilds a consistent spread and re-runs the same
ratio and rating code, so I can watch the rating migrate — e.g. the BBB borrower
drops to BB and its DSCR falls below 1.0 in the downside.

**10. Why does revenue −15% hit EBITDA by more than 15% in ratio terms?**
Operating leverage. Variable costs fall with revenue but fixed opex doesn't, so
EBITDA falls by the gross-margin share of lost revenue and the *margin*
compresses. That's the whole point of stressing revenue separately.

**11. What's FCCR and how's it different from DSCR?**
Fixed-Charge Coverage — here (EBITDA − maintenance capex) / (interest +
principal). It's a pre-tax cousin of DSCR; in practice it also folds in lease
rentals. Both answer "can fixed obligations be covered?".

**12. What is ROCE and why use it over ROE for credit?**
ROCE = EBIT / (Total Assets − Current Liabilities) — return on the *whole*
capital base, debt + equity, before financing. For credit you care about the
operating asset's return regardless of how it's financed; ROE is distorted by
leverage.

**13. Cash Conversion Cycle — why does a lender care?**
A lengthening CCC ties up more cash in working capital and increases reliance on
short-term borrowing, draining liquidity even when the P&L looks healthy. It's an
early-warning signal.

**14. Expected Loss formula?**
EL = PD × LGD × EAD. My scorecard drives the PD leg via the rating. LGD depends
on collateral/seniority (recovery), EAD on drawn plus likely further drawdown.

**15. What are the 5 Cs and where do they show up here?**
Character & Conditions → the business factors (management, industry). Capacity →
DSCR/ICR. Capital → gearing/net worth. Collateral → LGD (not deeply modelled).

**16. How would you validate this model?**
Back-test predicted PDs vs realised defaults (calibration), check rank-ordering
(discrimination — AUC/Gini), test stability of ratings over time, and benchmark
against agency ratings where available. I already unit-test the math and the
identities.

**17. What's the difference between an obligor rating and a facility rating?**
The obligor (borrower) rating captures PD; the facility rating overlays
collateral/seniority (LGD) for a specific loan. This project is an obligor-level
rating.

**18. Where does this break / what would you add next?**
It ignores off-balance-sheet items, leases (IFRS 16), guarantees and
inter-company exposures; capex maintenance split is an assumption; PDs aren't
calibrated. Next steps: pull real statements, add a peer/percentile overlay,
calibrate PDs, and add an LGD/collateral module to output Expected Loss.

**19. Why is the accounting-identity validation important?**
Because one wrong input row silently corrupts every downstream ratio. Validating
Assets = Liabilities + Equity (and the EBITDA/EBIT/debt builds) on load catches
bad data once, at the door.

**20. NBFC angle — what's different for a finance company?**
For an NBFC you'd shift emphasis to asset quality (GNPA/NNPA), provision cover,
capital adequacy (CRAR), the ALM / liquidity gap, cost of funds vs yield (NIM)
and leverage (Debt/Net-worth) — EBITDA-based DSCR is less central because the
"inventory" is loans. The spreading + scorecard framework carries over; the
factor set changes.
