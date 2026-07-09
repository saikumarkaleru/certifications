# Fund NAV, Trade & Cash Reconciliation, and KYC/AML Risk Scoring

A compact but realistic **investment-operations / fund-accounting** tool. It
strikes a daily fund NAV, reconciles trades and cash between the internal book
and the custodian, and runs a KYC/AML control (customer risk rating plus
transaction monitoring). It ships with synthetic-but-realistic sample data and
runs **fully offline** — no network, no market-data feed.

## What it does

**1. Pricing** (`pricing.py`)
- Values every holding from a positions file and a prices file.
- Explicit, documented **stale / missing price policy**:
  - `GOOD` — priced on the valuation date.
  - `STALE` — latest price older than 3 days (used as last-known-good, flagged).
  - `FALLBACK_PRIOR` — no price today, carry forward the prior-day close (flagged).
  - `MISSING` — no price anywhere → value at 0 and raise a hard exception.

**2. NAV** (`nav.py`)
- NAV waterfall: `GAV = holdings MV + cash + accrued income`, then
  `NAV = GAV − management fee accrual (TER) − other accrued expenses`.
- The management fee accrues pro-rata daily on the annual TER.
- Computes **NAV per unit** and flags a **≥2% day-over-day move** for review.

**3. Reconciliation** (`reconciliation.py`)
- One generic engine reconciles both **trades** and **cash** (book vs custodian).
- Classifies every record into a break type: `QUANTITY_MISMATCH`,
  `PRICE_AMOUNT_MISMATCH`, `DUPLICATE`, `MISSING_AT_CUSTODIAN`,
  `ORPHAN_AT_CUSTODIAN` (matched records drop off the queue).
- Builds an **aged exception queue** (0–2d / 3–5d / 6–10d / 10d+) with severity
  so breaks can be worked worst-first.

**4. KYC / AML** (`kyc.py`)
- **Customer risk rating**: weighted score across geography (35%), product (35%)
  and profile (30%) → Low / Medium / High tier → CDD / CDD+ / EDD.
- **Mandatory-EDD overrides**: PEP, sanctioned/high-risk jurisdiction, or
  correspondent banking force EDD regardless of score.
- **Transaction monitoring** rules: `LARGE_VALUE` (CTR-style), `STRUCTURING`
  (multiple deposits just under the threshold), `RAPID_MOVEMENT` (in→out
  layering), `HIGH_RISK_COUNTERPARTY` → alert queue for analyst review / STR.

**5. Reporting** (`reporting.py`)
- Formatted **Excel workbook** (`fund_ops_report.xlsx`) with six sheets:
  `NAV_Summary`, `Pricing`, `Trade_Breaks`, `Cash_Breaks`, `KYC_Risk`, `AML_Alerts`.
- Three **PNG charts**: NAV composition, break aging, risk-tier distribution.

## Project layout

```
1_nav_and_reconciliation/
├── main.py                     # end-to-end pipeline + console summary
├── src/fund_ops/
│   ├── data.py                 # CSV loaders (offline)
│   ├── pricing.py              # stale/missing price policy + market value
│   ├── nav.py                  # NAV waterfall + per-unit + move flag
│   ├── reconciliation.py       # generic break engine (trades + cash)
│   ├── kyc.py                  # risk scoring + AML transaction monitoring
│   └── reporting.py            # Excel workbook + charts
├── tests/test_fund_ops.py      # pytest: NAV math, each break type, KYC tiers, AML rules
├── input/                      # synthetic sample data (CSV)
└── output/                     # generated .xlsx + .png (created on run)
```

## Sample data (synthetic)

`Meridian Global Balanced Fund` — 9 holdings (7 equities, 2 bonds), 5M units,
$1.25M cash. The data is seeded with **intentional breaks**: a stale price
(NVDA), a missing price (CORP28), a quantity mismatch, a price/amount mismatch,
a missing trade, a duplicate, an orphan, plus cash mismatches — and 8 customers
covering every risk tier with transactions that trip each AML rule.

## Run it

```bash
python -m venv venv
venv/Scripts/pip install pandas numpy openpyxl matplotlib pytest   # Windows
# source venv/bin/activate; pip install ...                        # macOS/Linux

python main.py                 # runs the pipeline, writes output/, prints a summary
python -m pytest tests/ -q     # 11 unit tests
```

`main.py` prints a full desk-style summary and populates `output/` with the
workbook and three charts. Everything is deterministic and offline.

## Notes / assumptions

- Bond prices are treated as clean prices per unit of quantity for simplicity
  (no separate day-count accrued-interest engine at the position level; income
  is captured at the fund level as accrued income).
- The high-risk jurisdiction and product-risk tables are illustrative
  (FATF-style) and configurable at the top of `kyc.py`.
- Thresholds (stale days, move %, CTR line, structuring band) are named
  constants so they are easy to explain and tune.
