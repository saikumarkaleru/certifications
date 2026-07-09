# DCF Valuation (live, real-company)

A discounted-cash-flow model that values a **real** company pulled live from
yfinance. Derives unlevered free cash flow (FCFF) from the financial
statements, estimates a WACC via CAPM (real beta + live 10Y Treasury), projects
FCFF with fading growth, builds Gordon **and** exit-multiple terminal values,
and produces an intrinsic value per share — stress-tested with scenarios, a
2-way sensitivity grid, and a reverse DCF.

## Run
```bash
pip install pandas numpy matplotlib openpyxl yfinance
python main.py            # defaults to AAPL
python main.py MSFT       # any ticker
```
Live data is cached to `input/`; if you're offline it falls back to the cache
and then a bundled snapshot, so it always runs.

## Structure
```
main.py                 orchestrator + console summary
src/dcf/
  data.py               yfinance fetch, caching, offline fallback
  fcff.py               derive FCFF from the statements (+ cross-check)
  wacc.py               CAPM cost of equity, cost of debt, WACC blend
  model.py              projection, terminal values, scenarios, sensitivity,
                        reverse DCF
  report.py             Excel workbook + charts
tests/test_dcf.py       unit tests (PV maths, Gordon TV, FCFF, WACC, reverse)
input/                  cached yfinance snapshots
output/                 dcf_valuation.xlsx, fcf_bridge.png, football_field.png
```

## Output
- **`output/dcf_valuation.xlsx`** — sheets: Assumptions, DCF, Scenarios,
  Sensitivity, ReverseDCF.
- **`output/fcf_bridge.png`** — projected vs discounted FCFF + terminal value.
- **`output/football_field.png`** — bull/base/bear range vs market price.

## Tests
```bash
python -m pytest -q
```

## Key formulas
- FCFF: `EBIT × (1 − tax) + D&A − Capex − ΔNWC`
- CAPM cost of equity: `Ke = rf + beta × ERP`
- WACC: `E/V·Ke + D/V·Kd·(1 − tax)`
- Present value: `PV = FCFF_t / (1 + WACC)^t`
- Terminal value (Gordon): `TV = FCFF_N × (1 + g) / (WACC − g)`

See `STUDY_GUIDE.md` for the interview walkthrough and Q&A.

*Uses live market data for education only — not investment advice.*
