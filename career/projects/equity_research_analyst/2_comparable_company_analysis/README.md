# Comparable Company Analysis (live, real-company)

Relative valuation of a **real** target against a peer set pulled live from
yfinance. Computes five trading multiples (P/E, EV/EBITDA, EV/Revenue, P/B,
PEG), summarises the peers (median/mean/quartiles), derives an implied value per
multiple and a blended football-field range vs the current price, and runs a
rich/cheap screen (z-scores + an OLS regression of EV/EBITDA on growth &
margin).

## Run
```bash
pip install pandas numpy matplotlib openpyxl yfinance
python main.py            # target AAPL, peers MSFT/GOOGL/META/AMZN/ORCL/IBM
python main.py MSFT       # any target in the peer set
```
Live data is cached to `input/`; if you're offline it falls back to the cache
and then a bundled snapshot, so it always runs.

## Structure
```
main.py                  orchestrator + console summary
src/comps/
  data.py                yfinance fetch (target + peers), caching, offline fallback
  multiples.py           EV + P/E, EV/EBITDA, EV/Revenue, P/B, PEG
  stats.py               peer median/mean/quartiles + z-score & OLS screens
  valuation.py           implied value per multiple + football-field range
  report.py              Excel workbook + football-field chart
tests/test_comps.py      unit tests (multiples, implied value, screens)
input/                   cached yfinance snapshots
output/                  comparable_company_analysis.xlsx, football_field.png
```

## Output
- **`output/comparable_company_analysis.xlsx`** — sheets: Comps, Multiples,
  Implied, Screen.
- **`output/football_field.png`** — implied price per method vs market price.

## Tests
```bash
python -m pytest tests/ -q
```

## Key formulas
- Enterprise value: `EV = market cap + total debt − cash`
- Multiples: `P/E = price/EPS`, `EV/EBITDA`, `EV/Revenue`, `P/B = price/BVPS`,
  `PEG = (P/E) / earnings-growth%`
- Implied (equity multiple): `price = peer median × target per-share metric`
- Implied (enterprise multiple): `EV = median × metric`, then
  `price = (EV − net debt) / shares`
- Fundamentals screen: `EV/EBITDA = b0 + b1·growth + b2·margin`; residual flags
  rich/cheap.

See `STUDY_GUIDE.md` for the interview walkthrough and Q&A.

*Uses live market data for education only — not investment advice.*
