# Corporate / NBFC Credit Analysis — Financial Spreading, Serviceability & Internal Rating

A compact, fully offline credit-analysis engine. Feed it a few years of a
borrower's financials and it produces the same package a junior credit analyst
hands to a committee:

1. **Standardised spread** — every statement re-cast into one template.
2. **Ratio families** — leverage, coverage, liquidity, profitability, working-capital cycle.
3. **Debt serviceability** — CFADS-based **DSCR** and **ICR** against a debt schedule, with headroom classes.
4. **Internal rating** — a transparent weighted scorecard mapping to a band (AAA…D) and an indicative 1-year PD, plus a written rationale.
5. **Stress testing** — EBITDA, interest-rate and revenue shocks that re-derive every metric and show the rating migrate base → downside.
6. **Reporting** — a formatted Excel workbook and three PNG charts.

Everything runs on **bundled synthetic-but-realistic data** (three borrowers,
FY2022–FY2024, INR crore) — no network, no APIs.

## The three sample borrowers (deliberately different credit profiles)

| Code | Borrower | Profile | Latest rating |
|------|----------|---------|---------------|
| AARTI | Aarti Manufacturing Ltd | Low leverage, strong cash generation | **AA** |
| SUNRISE | Sunrise Consumer Products Ltd | Moderate leverage, adequate cover | **BBB** |
| DECCAN | Deccan Infra & Logistics Ltd | Over-levered, negative net worth, DSCR < 1 | **C** |

## Layout

```
1_financial_spreading_and_rating/
├── main.py                     # orchestrates the whole pipeline
├── input/
│   ├── financials.csv          # 3 borrowers × 3 years, long format
│   ├── business_risk.csv       # qualitative 1–5 factor scores
│   └── companies.csv           # code → name + sector
├── src/credit_spread/
│   ├── data.py                 # load, clean, validate → standardised spread
│   ├── ratios.py               # the five ratio families
│   ├── serviceability.py       # CFADS, DSCR, ICR, headroom
│   ├── rating.py               # weighted scorecard → band + PD + rationale
│   ├── scenario.py             # stress scenarios + rating migration
│   └── reporting.py            # Excel workbook + PNG charts
├── tests/test_credit.py        # 13 pytest cases
└── output/                     # generated: credit_analysis.xlsx + 3 PNGs
```

## Run it

```bash
python -m venv .venv
# Windows:  .venv\Scripts\activate     |  macOS/Linux:  source .venv/bin/activate
pip install pandas numpy openpyxl matplotlib pytest

python main.py            # prints the credit read, writes output/
python -m pytest tests/ -q
```

## Methods, in one screen

- **Spread & validation** — every borrower is reindexed onto one canonical line-item list; four accounting identities (EBITDA build, EBIT build, Total Debt, Assets = Liabilities + Equity) are checked on load so bad data is caught once.
- **Ratios** — plain division off the spread. Leverage: Debt/EBITDA, Net Debt/EBITDA, Debt/Equity, Gearing. Coverage: Interest Cover (EBIT/int), EBITDA interest cover, FCCR. Liquidity: current, quick. Profitability: EBITDA margin, net margin, ROCE. Cycle: DSO, DIO, DPO, CCC.
- **Serviceability** — `CFADS = EBITDA − cash taxes − maintenance capex` (growth capex is treated as discretionary via a 40% maintenance split); `DSCR = CFADS / (interest + scheduled principal)`. Headroom: ≥1.50 Comfortable, 1.25–1.50 Adequate, 1.00–1.25 Thin, <1.00 Shortfall.
- **Rating** — 65% financial factors (Net Debt/EBITDA, DSCR, interest cover, EBITDA margin, gearing) + 35% business factors (market position, industry, diversification, management). Each factor maps to a 0–100 sub-score by explicit thresholds; the weighted composite maps to a band and an indicative PD.
- **Scenarios** — EBITDA −10/−20/−30%, rates +100/+200 bps (on the whole debt stack), revenue −15% (flows to EBITDA through the gross margin with opex fixed), and a combined downside. Each shock rebuilds the spread and re-runs the *same* ratio/rating code, so scenario numbers are computed identically to the base case.

The bands, PDs and thresholds are **illustrative teaching anchors**, not a
regulator-calibrated master scale — but the mechanics mirror a real internal
rating model. See `STUDY_GUIDE.md` for the credit concepts and interview Q&A.
