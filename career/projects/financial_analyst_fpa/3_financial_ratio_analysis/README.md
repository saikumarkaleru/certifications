# Financial Ratio Analysis + DuPont + Peer Benchmarking

Pull real financial statements for a target company and its peers, compute the
ratios an analyst actually uses, decompose Return on Equity with DuPont, rank the
target against its peers, flag trends, and screen earnings quality — then write a
clean Excel workbook and a set of charts.

- **Target:** AAPL
- **Peers:** MSFT, GOOGL, AMZN, META

See **[STUDY_GUIDE.md](STUDY_GUIDE.md)** for the plain-English explanation and
interview Q&A.

## What it does

1. **Load** income statement, balance sheet, and cash flow for all five
   companies (about 4-5 fiscal years each) via `yfinance`.
2. **Ratios** across four families over multiple years:
   profitability, liquidity, leverage/solvency, efficiency.
3. **DuPont** decomposition of the latest ROE, both 3-step and 5-step, which
   reconciles exactly to the directly computed ROE.
4. **Benchmark** the target against peers on each key ratio using a percentile
   rank (0-100), direction-aware so "higher percentile = better positioned".
5. **Trend flags** for the target: each ratio labelled Improving / Deteriorating / Flat.
6. **Earnings-quality red flags:** accruals ratio and CFO/Net-Income cash
   conversion.

## How to run

```bash
pip install yfinance pandas openpyxl matplotlib
python main.py
```

Prints a console summary and writes everything to `output/`. Then, to run tests:

```bash
python -m pytest tests/ -q
```

## Module map (`src/ratios/`)

| Module         | Responsibility                                                        |
|----------------|-----------------------------------------------------------------------|
| `data.py`      | Load statements via yfinance, cache to `input/`, offline fallback, safe `get()` helper, canonical facts table |
| `ratios.py`    | The four ratio families over several years (NaN-safe, average balances)|
| `dupont.py`    | 3-step and 5-step ROE decomposition + reconciliation                   |
| `benchmark.py` | Percentile ranks of target vs peers on each key ratio                  |
| `quality.py`   | Trend flags + earnings-quality red-flag panel                          |
| `reporting.py` | Excel workbook + matplotlib PNG charts                                 |

## Data: live, cached, offline

- On first run, statements are pulled **live** from yfinance and **cached** to
  `input/<TICKER>.pkl`. Reruns read the cache, so they are fast and fully offline.
- If there is no cache **and** no network, the code falls back to bundled
  **illustrative** numbers so `python main.py` always completes with no errors.
- The console prints which source was used: `LIVE`, `CACHE`, `MIXED`, or `FALLBACK`.

## Output (`output/`)

- `financial_ratio_analysis.xlsx` — sheets: **Ratios** (target, multi-year),
  **DuPont**, **Benchmark**, **Trends**, **RedFlags**, and **Raw_\<TICKER\>** for
  every company (audit trail).
- `chart_dupont.png` — 3-step DuPont drivers of the target's latest ROE.
- `chart_margins.png` — gross / operating / net margin trend.
- `chart_benchmark.png` — target's percentile rank on each key ratio.
- `chart_leverage.png` — Debt/Equity of every company (latest year).

Built for a **Financial Analyst (FP&A)** portfolio.
