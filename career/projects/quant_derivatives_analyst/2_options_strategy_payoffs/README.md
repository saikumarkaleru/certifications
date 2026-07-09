# Options Strategy Payoffs & Risk Toolkit

Builds **16 classic option strategies** from a single `Leg`/`Position`
abstraction, then computes — for every one of them — payoff/P&L **at expiry AND
before expiry** (using Black-Scholes for the time value), **net position Greeks**,
**probability of profit** from the lognormal terminal distribution, a **spot × vol
scenario grid**, and a **cross-strategy screener** that ranks them by risk/reward
and probability of profit.

Strikes and premiums are sourced from a **live yfinance option chain** where
available, cached to `input/`, with a graceful offline fallback (cached snapshot,
else a Black-Scholes-priced synthetic ladder) so `python main.py` **always runs**.

See **[STUDY_GUIDE.md](STUDY_GUIDE.md)** for the plain-English explanation and
interview Q&A.

## Run it
```bash
pip install numpy pandas matplotlib openpyxl yfinance
python main.py                 # live chain if reachable, else offline fallback
OPT_OFFLINE=1 python main.py   # force the offline / synthetic path
python -m pytest tests/ -q     # run the unit tests
```
`main.py` runs 7 steps and prints a console summary at each: market snapshot →
build + summarise all strategies → expiry vs before-expiry P&L → scenario grid →
screener → Excel → charts.

## The 16 strategies
Long call, long put, covered call, protective put, collar, bull call spread,
bear put spread, bull put spread (credit), bear call spread (credit), long
straddle, long strangle, long call butterfly, iron condor, iron butterfly, call
ratio spread (1×2), calendar spread (single-expiry approximation, flagged as
such).

## File map
```
main.py                         7-step orchestrator; prints summary, writes Excel + charts
src/strategies/
    bsm.py                      minimal Black-Scholes-Merton (price + Greeks, q, norm_cdf from math.erf)
    legs.py                     Leg + Position abstraction — the heart of the project
    library.py                  the 16 strategy builders (StrategySpec: name, position, view, category)
    analytics.py                probability_of_profit, scenario_grid, screen_strategies
    market_data.py              yfinance snapshot -> cache -> synthetic fallback
tests/test_strategies.py        leg math, breakevens, synthetic-position parity, net greeks
input/                          cached market snapshot (e.g. AAPL_snapshot.json)
output/                         strategy_summary.xlsx + payoff / time-value / scenario PNGs
```

## Outputs
- `output/strategy_summary.xlsx` — **Summary** (all strategies + Greeks + POP),
  **Screener** (ranked), **Scenario (IronCondor)** (spot × vol grid).
- `output/strategy_payoffs.png` — grid of expiry payoff diagrams for all 16.
- `output/time_value_overlay.png` — one strategy's expiry (kinked) vs
  before-expiry (smooth) P&L, showing time value.
- `output/scenario_heatmap.png` — spot × vol P&L heatmap.

## Conventions
All P&L is **per share** (1 contract = 1 share) to keep the maths transparent;
multiply by the contract multiplier (e.g. 100) for dollar figures. Dependencies:
numpy, pandas, matplotlib (Agg backend), openpyxl, yfinance. No scipy — the
normal CDF is built from `math.erf`.

Built for a **Quant / Derivatives Analyst** portfolio.
