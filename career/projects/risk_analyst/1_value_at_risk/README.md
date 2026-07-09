# Value at Risk (VaR) — 8-Stock US Large-Cap Portfolio

A compact but realistic market-risk engine. It estimates 1-day Value-at-Risk
and Expected Shortfall for a $1,000,000 equity portfolio three independent ways,
decomposes the risk by asset, and backtests the model with formal statistical
tests.

## What it does
- **Portfolio**: AAPL, MSFT, JPM, XOM, JNJ, PG, WMT, NVDA (weights sum to 1.0).
- **VaR at 95% and 99%** via three methods:
  - Historical (empirical quantile)
  - Parametric / variance-covariance (delta-normal, `w'Σw`)
  - Monte Carlo (50,000 correlated draws via Cholesky)
- **Expected Shortfall (CVaR)**: historical and closed-form parametric.
- **Component & marginal VaR**: which stock drives the risk.
- **Backtest**: rolling 250-day VaR, exception count, Kupiec POF test,
  Christoffersen independence test, combined conditional-coverage test.
- **Outputs**: a formatted Excel workbook and three PNG charts.

## Data
Live daily prices are pulled from Yahoo Finance (`yfinance`, `auto_adjust=True`).
Results are cached to `input/prices.csv`. If the download fails and no cache
exists, a realistic **synthetic** correlated dataset is generated so the project
always runs offline. The console prints whether data is LIVE, CACHED or SYNTHETIC.

## How to run
```
cd 1_value_at_risk
python main.py                 # full analysis + reports
python -m pytest tests/ -q     # unit tests (or: python tests/test_var.py)
```
No scipy required — the normal PDF/CDF/PPF and chi-square p-values are
implemented by hand with the standard library.

## Structure
```
main.py                      orchestrator + console summary
src/var_engine/
  data.py                    download / cache / synthetic fallback
  var_methods.py             historical, parametric, MC, ES, component VaR
  backtest.py                rolling VaR, Kupiec, Christoffersen
  reporting.py               Excel workbook + matplotlib charts
tests/test_var.py            unit tests
input/                       cached prices land here
output/                      var_analysis.xlsx + PNG charts land here
STUDY_GUIDE.md               interview prep
```
