# Black-Scholes Options Pricer & Greeks Toolkit

A compact but real options-analytics library: closed-form **Black-Scholes-Merton**
pricing (with continuous dividend yield `q`), first- **and** second-order Greeks,
a **binomial tree** (European + American), a **Monte-Carlo** pricer, an
**implied-vol** solver, live **option-chain** ingestion, and a
**finite-difference** Greeks validator. Everything is heavily commented so each
line is defensible in an interview.

## What it does

Running `main.py` walks through eight steps and prints a summary of each:

1. Price a sample ATM option: call/put + all Greeks + put-call parity check.
2. Cross-check the price three ways: BSM vs CRR tree vs Monte-Carlo.
3. Show the American early-exercise premium (American put > European put).
4. Implied-vol round-trip: recover a known sigma from a price (~1e-16 here).
5. Validate analytic Greeks against finite differences (max err ~1e-8).
6. Pull a real option chain (yfinance, with offline fallback), solve each
   contract's implied vol, report re-pricing accuracy, and build the IV smile.
7. Write `output/black_scholes_summary.xlsx` (Prices, Greeks, Validation, Smile).
8. Save 4 charts: payoff, Greeks-vs-spot, IV smile, tree convergence.

## How to run

```bash
python main.py                 # full demo -> console summary + Excel + charts
python tests/test_pricer.py    # unit tests (plain asserts, no pytest needed)
python -m pytest tests/        # same tests under pytest, if installed
```

No network is required: if yfinance fails, the code loads a cached chain from
`input/`, or synthesizes one, so `main.py` always completes.

## File map

```
main.py                       Orchestrator: runs all 8 steps, writes Excel + charts
src/pricer/__init__.py        Package exports
src/pricer/black_scholes.py   N(x)/n(x), d1/d2, prices, 1st + 2nd order Greeks
src/pricer/implied_vol.py     Newton-Raphson IV solver + bisection fallback
src/pricer/binomial.py        Cox-Ross-Rubinstein tree (European & American)
src/pricer/monte_carlo.py     Risk-neutral GBM MC + antithetic variates + s.e.
src/pricer/market_data.py     yfinance option chain, cache, offline fallback
src/pricer/validation.py      Analytic vs finite-difference Greeks table
tests/test_pricer.py          Unit tests (parity, BSM=tree=MC, IV, Greeks, American)
input/                        Cached option chains (auto-created)
output/                       Excel workbook + PNG charts (auto-created)
```

## Dependencies

`numpy`, `pandas`, `matplotlib` (Agg backend), `openpyxl`, `yfinance`.
The normal CDF is built from `math.erf`, so **no scipy** is needed. Python 3.10+.

## Math conventions (stated so nothing surprises a reviewer)

- BSM with dividend yield `q`; set `q=0` to recover classic Black-Scholes.
- `vega`, `rho` reported **per 1%** move; `theta`, `charm` **per calendar day**.
- IV solver uses **raw** vega (`dPrice/dsigma`, not `/100`) in the Newton step.
- CRR: `u=e^(sigma*sqrt(dt))`, `d=1/u`, `p=(e^((r-q)dt)-d)/(u-d)`.
