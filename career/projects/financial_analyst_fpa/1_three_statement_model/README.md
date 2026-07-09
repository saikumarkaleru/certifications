# Three-Statement Model + Forecast + Scenarios + Sensitivity + DCF

A driver-based FP&A model that pulls a **real company's** financials (default
**MSFT**) via `yfinance`, builds a fully linked **5-year Income Statement /
Balance Sheet / Cash Flow** forecast, adds a **debt/revolver cash sweep**, runs
**bull / base / bear scenarios** and a **2-way sensitivity table**, and values
the business with a **DCF**. The balance sheet **ties out to ~0 every year**.

See **[STUDY_GUIDE.md](STUDY_GUIDE.md)** for the plain-English walkthrough and
the interview Q&A.

## Run it
```bash
pip install yfinance pandas openpyxl matplotlib
python main.py
```
On the first run it pulls live data from yfinance and caches it to `input/`.
Every later run reads that cache (so it's **offline and instant**). If there's
no network *and* no cache, it falls back to bundled illustrative numbers — so
`python main.py` **always** runs. The console prints which data source was used.

## What it produces
- A console summary of all three statements, the debt schedule, scenarios,
  the sensitivity grid and the DCF.
- `output/three_statement_model.xlsx` — tabs: Income Statement, Balance Sheet,
  Cash Flow, Debt Schedule, FCFF, Scenarios, Sensitivity, DCF, Assumptions.
- `output/*.png` — revenue & net-income trend, free cash flow, scenario value/share.

## File / module map
```
main.py                  orchestrates: load -> model -> scenarios -> DCF -> report
src/model/
  data.py                yfinance pull + cache + offline fallback; derives drivers
  forecast.py            the linked 3-statement engine + debt/revolver cash sweep
  scenarios.py           bull/base/bear cases + 2-way DCF sensitivity table
  valuation.py           WACC + DCF off the model's unlevered free cash flow (FCFF)
  reporting.py           writes the Excel workbook and the PNG charts
tests/test_model.py      pytest: balance ties out, cash rolls forward, DCF finite
input/                   cached yfinance pull (created on first run)
output/                  Excel workbook + charts (created on run)
```

## Tests
```bash
python -m pytest tests/ -q      # or: python tests/test_model.py
```

Built for a **Financial Analyst (FP&A)** portfolio — medium difficulty, fully
explainable line by line.
