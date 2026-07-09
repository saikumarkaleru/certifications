# Finance Projects — Saikumar Kaleru

Eleven finance projects across five analyst tracks. Each is a small, readable Python
package (a `src/` module tree, not a single script), runs from real or realistic
cached data, produces Excel and chart output, ships unit tests, and carries a
`STUDY_GUIDE.md` (30-second pitch, how it works, interview Q&A) so every line is
defensible in an interview.

![Tests](https://github.com/saikumarkaleru/career/actions/workflows/finance-projects-tests.yml/badge.svg)

**Stack:** Python 3.13, pandas, numpy, matplotlib (Agg / headless), openpyxl, yfinance.
Tests with pytest. No network needed to run: each project reads cached input data
committed under its `input/` folder.

## The projects

| Track | Project | What it does | Tests |
|-------|---------|--------------|:----:|
| Credit | [`credit_analyst/1_financial_spreading_and_rating`](credit_analyst/1_financial_spreading_and_rating) | Spreads a borrower's financials, computes leverage/coverage/DSCR/ICR, maps to an internal rating scorecard, stress tests serviceability. | 13 |
| Credit / Risk | [`risk_analyst/2_credit_risk_scoring`](risk_analyst/2_credit_risk_scoring) | Default risk via Altman Z-score and Merton distance-to-default; rolls single-name PD/LGD/EAD up to a portfolio expected loss. | 8 |
| Equity Research | [`equity_research_analyst/1_dcf_valuation`](equity_research_analyst/1_dcf_valuation) | Five-year FCFF DCF: WACC, terminal value, equity bridge, reverse DCF, two-way WACC x growth sensitivity. | 10 |
| Equity Research | [`equity_research_analyst/2_comparable_company_analysis`](equity_research_analyst/2_comparable_company_analysis) | Peer trading multiples (P/E, EV/EBITDA, EV/Sales, P/B, PEG) to an implied valuation range and football field. | 11 |
| FP&A | [`financial_analyst_fpa/1_three_statement_model`](financial_analyst_fpa/1_three_statement_model) | Linked income statement, balance sheet and cash flow with a driver-based five-year forecast that stays balanced. | 7 |
| FP&A | [`financial_analyst_fpa/2_budget_vs_actual`](financial_analyst_fpa/2_budget_vs_actual) | Monthly budget-vs-actual variance with a price/volume/cost bridge and auto-generated commentary. | 8 |
| FP&A / Equity | [`financial_analyst_fpa/3_financial_ratio_analysis`](financial_analyst_fpa/3_financial_ratio_analysis) | Ratio and DuPont analysis with earnings-quality checks, benchmarking five large-cap peers (AAPL, MSFT, GOOGL, META, AMZN). | 7 |
| Investment Operations | [`investment_operations/1_nav_and_reconciliation`](investment_operations/1_nav_and_reconciliation) | Daily fund NAV, custodian-vs-book trade and cash reconciliation with aged exception breaks, and KYC/AML scoring. | 11 |
| Quant / Derivatives | [`quant_derivatives_analyst/1_black_scholes_pricer`](quant_derivatives_analyst/1_black_scholes_pricer) | Black-Scholes, binomial and Monte-Carlo pricing, full Greeks, an implied-vol solver, and analytic-vs-finite-difference Greek validation. | 6 |
| Quant / Derivatives | [`quant_derivatives_analyst/2_options_strategy_payoffs`](quant_derivatives_analyst/2_options_strategy_payoffs) | Multi-leg option strategies: payoff, P&L, net Greeks and probability of profit across a spot and vol grid. | 8 |
| Risk | [`risk_analyst/1_value_at_risk`](risk_analyst/1_value_at_risk) | One-day VaR (historical, parametric, Monte-Carlo), expected shortfall, backtesting, and component/marginal VaR with Cholesky correlation. | 8 |

**97 tests total, all passing.**

## Run any project

```bash
# from the repo root
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r projects/requirements.txt               # or the project's own requirements.txt

cd projects/quant_derivatives_analyst/1_black_scholes_pricer
python main.py            # writes Excel + charts to output/
python -m pytest -q       # run this project's tests
```

Each project also has its own pinned `requirements.txt` if you want to install only
what that one needs.

## Run every test suite

```bash
pip install -r projects/requirements.txt
for d in projects/*/*/ ; do [ -f "$d/main.py" ] && (cd "$d" && python -m pytest -q); done
```

CI runs exactly this on every push (see `.github/workflows/finance-projects-tests.yml`).
