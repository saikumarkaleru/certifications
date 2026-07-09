# Credit Risk Scoring — Altman Z-Score + Merton Structural Model

Scores the default risk of ~10 real US large-cap companies two independent,
interview-defensible ways, then rolls them into a loan-book expected loss.

## What it does
1. **Altman Z-score** (accounting model) — five balance-sheet ratios → one
   bankruptcy score → Safe / Grey / Distress zone.
2. **Merton structural model** (market model) — treats equity as a call option
   on firm assets, solves for asset value & volatility, and reads off a
   distance-to-default and probability of default (PD).
3. **Portfolio expected loss** — `EL = PD × LGD × EAD`, summed across issuers.

Data is pulled **live** from yfinance, **cached** to `input/`, and falls back to
a realistic **built-in** dataset so it always runs offline. The console prints
which source was used (LIVE / CACHED / FALLBACK).

## How to run
```
python main.py            # full analysis + Excel + charts + console summary
python -m pytest tests/   # unit tests (or: python tests/test_credit.py)
```
Requires: pandas, numpy, matplotlib, openpyxl, yfinance. (No scipy — the normal
CDF is built from `math.erf`.)

## Structure
```
main.py                     orchestrator: fetch -> Altman -> Merton -> EL -> report
src/credit/data.py          yfinance financials + market cap + price vol; cache; fallback
src/credit/altman.py        Altman Z-score: 5 ratios + zone classification
src/credit/merton.py        Merton solver: asset value/vol, distance-to-default, PD
src/credit/portfolio.py     rank issuers; portfolio expected loss
src/credit/reporting.py     Excel workbook + matplotlib charts
tests/test_credit.py        unit tests (Altman math, Merton sanity/monotonicity)
input/                      cached inputs (credit_inputs.csv)
output/                     credit_analysis.xlsx + two PNG charts
STUDY_GUIDE.md              pitch, walkthrough, interview Q&A, vocabulary
```

## Outputs
- `output/credit_analysis.xlsx` — Inputs / Altman / Merton / Portfolio sheets.
- `output/altman_zscore_bar.png` — Z by company, coloured by zone.
- `output/pd_vs_zscore_scatter.png` — Merton PD vs Altman Z.

*Live financials are third-party data; this is a demonstration project, not a
real credit assessment.*
