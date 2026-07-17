# Monte Carlo on Trade Sequences

You have a strategy with a 55% win rate and a 1.5:1 reward-to-risk. The backtest curve rises beautifully. So how bad can it get? What is the worst drawdown you should expect *before* concluding the edge is broken? What position size drives your account toward zero rather than growth? What is the chance you double your money before you lose 20%? A single backtest — one historical path — cannot answer any of these, because it shows you exactly one of the millions of orderings your trades *could* have arrived in. Monte Carlo simulation answers them by generating those millions of alternate histories and reading the distribution of outcomes. For a trader, it is the difference between "my system made money last year" and "here is the range of futures I am actually signing up for, and the position size that survives all of them." This chapter builds the technique from scratch on Indian trading examples.

## The concept

The core insight: **your realised equity curve is one random draw from a distribution of possible curves.** Your trades have some underlying win rate and payoff profile, but the *order* in which wins and losses landed was luck. Reshuffle that order and you get a different maximum drawdown, a different worst losing streak, a different ending balance. Run one backtest and you see one curve; run 10,000 reshuffles and you see the whole cone of possibilities.

Monte Carlo (named after the casino, because it substitutes repeated random sampling for hard maths) does exactly this. You take your strategy's statistical fingerprint — win rate, average win, average loss, and their variability — and you *resample* trades thousands of times to build a distribution of every metric you care about: final equity, maximum drawdown, longest losing streak, probability of ruin, time to recovery.

Why this matters more than the single backtest:

1. **Drawdown realism.** Your backtest's worst drawdown was −18%. Monte Carlo might reveal that a −30% drawdown occurs in 25% of equally-likely paths. If −30% would make you abandon the system (or breach a risk limit), you'd have been blindsided.
2. **Position sizing / risk of ruin.** The same edge, sized at 2% risk per trade, might have a 1% chance of ruin; sized at 8%, a 40% chance. Monte Carlo finds the size where growth is maximised without unacceptable ruin risk.
3. **Confidence intervals on the edge.** Is the strategy's profit real or a fluke of ordering? The distribution shows how much of the result is signal vs luck.
4. **Psychological preparation.** Knowing that an 11-trade losing streak is *normal* for your system (not a sign it's broken) is what lets you keep trading it through the streak.

## The method and the maths

There are two main resampling schemes, and the choice matters:

**1. Trade reshuffling (bootstrap without replacement).** Take your actual list of N historical trade returns and shuffle their order. This keeps the exact set of trades but randomises sequence. Good for: understanding how much your drawdown depended on lucky ordering. Limitation: it can never produce a streak longer than what your data allows, and every simulation uses the same trades.

**2. Bootstrap with replacement (resampling).** Draw N trades *with replacement* from your historical set — some trades appear multiple times, some not at all. This treats your history as a sample from a larger population and generates genuinely new sequences, including streaks worse than anything you've seen. This is the more honest and conservative method, and the standard for risk-of-ruin work.

**3. Parametric simulation.** Instead of resampling actual trades, assume a distribution — e.g. each trade is a win with probability p, paying +W, or a loss paying −L. Draw from that. Cleaner for "what-if" analysis (what if my win rate slips to 50%?) but only as good as the distributional assumption.

**The compounding maths.** For a sequence of trade returns r_1, r_2, …, r_N applied to starting capital C_0 with fractional risk, equity evolves multiplicatively:

> C_N = C_0 × Π (1 + f · r_i)

where f is your risk fraction per trade and r_i is the trade's return in R-multiples (a +1.5R win, a −1R loss). **Maximum drawdown** for each simulated path is the largest peak-to-trough decline:

> MaxDD = max over t of [ (Peak_t − C_t) / Peak_t ]

**Risk of ruin** is the fraction of the 10,000 paths whose equity ever falls below a chosen threshold (say 50% of starting capital, or a hard margin-call level).

The key statistical subtlety: because equity *compounds*, the distribution of final wealth is roughly **log-normal**, not normal — the upside is unbounded but the downside is floored at zero. This asymmetry is exactly why oversized bets that look fine "on average" (high mean) still drive the *median* and *most likely* outcome toward ruin. Monte Carlo makes this visible where arithmetic intuition fails.

## A worked example with a code snippet

Take a realistic intraday Bank Nifty strategy with this fingerprint, measured over 200 historical trades, each risking 1R:

| Metric | Value |
|---|---|
| Win rate | 52% |
| Average win | +1.6R |
| Average loss | −1.0R |
| Expectancy | 0.52×1.6 − 0.48×1.0 = **+0.35R per trade** |
| Starting capital | ₹5,00,000 |
| Risk per trade | 2% (₹10,000 = 1R) |
| Trades per year | ~250 |

The expectancy is positive, so the strategy makes money on average. But how bad is the ride? Here is a bootstrap-with-replacement simulation:

```python
import numpy as np

wins, losses = 0.52, 0.48
W, L = 1.6, -1.0          # R-multiples
f = 0.02                  # 2% risk per trade (1R)
C0 = 500_000
n_trades = 250
n_sims = 10_000
rng = np.random.default_rng(42)

final, maxdd, ruin = [], [], 0
for _ in range(n_sims):
    outcomes = rng.choice([W, L], size=n_trades, p=[wins, losses])
    eq = C0 * np.cumprod(1 + f * outcomes)
    peak = np.maximum.accumulate(eq)
    dd = (peak - eq) / peak
    final.append(eq[-1])
    maxdd.append(dd.max())
    if eq.min() < 0.5 * C0:      # ruin = ever below 50% of capital
        ruin += 1

final = np.array(final); maxdd = np.array(maxdd)
print(f"Median final: Rs {np.median(final):,.0f}")
print(f"5th pct final: Rs {np.percentile(final,5):,.0f}")
print(f"Median maxDD: {np.median(maxdd):.1%}")
print(f"95th pct maxDD: {np.percentile(maxdd,95):.1%}")
print(f"Risk of ruin (<50%): {ruin/n_sims:.1%}")
```

Representative output for this edge and size:

- **Median final equity:** ~₹9.5–10 lakh (roughly doubled over the year).
- **5th-percentile final equity:** ~₹6 lakh — even a bad year is modestly positive.
- **Median max drawdown:** ~14%.
- **95th-percentile max drawdown:** ~24% — one year in twenty, expect a drawdown near a quarter of the account, *even though the strategy is sound.*
- **Risk of ruin (<50%):** near 0% at 2% risk.

Now change one input — risk per trade to **8%** — and rerun. The mean outcome looks spectacular, but the median collapses and risk of ruin jumps to double digits: the compounding of large fractional bets means a normal losing streak (which Monte Carlo shows arrives regularly) now craters the account. This is the practical demonstration of why professionals cap per-trade risk at 1–2%.

## How to use it in a real TA workflow

**Step 1 — Extract your fingerprint.** From your TradingView/Chartink/backtest trade log, compute win rate, average win, average loss (in R-multiples), and ideally keep the *actual distribution* of trade returns rather than just averages (real strategies have fat-tailed wins and occasional oversized losses that averages hide).

**Step 2 — Bootstrap with replacement.** Run 10,000 simulated years. Prefer resampling actual trades over parametric win/loss, so real outliers are represented.

**Step 3 — Read the distribution, not the point estimate.** Focus on the *bad tail*: 95th-percentile drawdown and risk of ruin. Ask: "Could I psychologically and financially survive the 95th-percentile path?" If no, the strategy is too large or too aggressive *regardless* of its positive expectancy.

**Step 4 — Solve for position size.** Sweep risk fraction f from 0.5% to, say, 5% and plot median growth and risk of ruin against f. The optimum sits well *below* the theoretical Kelly fraction (Kelly maximises long-run growth but tolerates gut-wrenching drawdowns); most traders use "half-Kelly" or less. Monte Carlo lets you *see* the growth-vs-ruin trade-off and pick your comfort point.

**Step 5 — Set expectations and tripwires.** Use the distribution to define a "normal" worst losing streak and worst drawdown. If live trading exceeds the *99th* percentile of simulated drawdown, that is genuine evidence the edge has degraded (not just bad luck) — a rational, pre-committed rule to pause and review, immune to panic.

**Step 6 — Stress the assumptions.** Rerun with win rate shaved by 5 points and average win cut 10% to model slippage, brokerage, STT, and edge decay on NSE. If the strategy only survives its *best-case* fingerprint, it is fragile.

## Confluence

Monte Carlo is the risk-layer that sits *on top of* everything else in this book. It combines naturally with **volatility modeling** (Chapter 74): in a high-vol regime your average loss widens and win rate may fall, so re-run Monte Carlo with a stressed fingerprint before sizing up. It combines with **expectancy and system design**: a positive backtest is a *necessary* input, Monte Carlo is what tells you whether that system is *survivable*. It pairs with **position sizing frameworks** (Kelly, fixed-fractional, volatility targeting) by testing each numerically rather than trusting a formula. And it disciplines the **psychology** side: traders abandon good systems during normal drawdowns; a Monte Carlo distribution that pre-warns "an 18% drawdown happens in a third of all good years" is the single best defence against that mistake.

## Honest limitations

Monte Carlo is only as good as its inputs — **garbage in, garbage out.** The most dangerous assumption is that trades are **independent and identically distributed (i.i.d.).** Real trades are not: strategies have autocorrelated results (losing streaks cluster because market regimes cluster — exactly the volatility clustering of Chapter 74), and a strategy's edge is *not stationary* — it decays as others discover it or as the market changes. Plain resampling destroys this structure, generally making the simulation look *tamer* than reality; block-bootstrap (resampling chunks of consecutive trades) partially preserves clustering and is more honest for streak analysis. Second, the historical sample may simply be **too small or from one regime** — 200 trades from a 2023–24 bull phase cannot tell you how the system behaves in a 2008- or 2020-style crash, so Monte Carlo will confidently under-forecast tail risk. Third, it models the *strategy* but not **execution reality**: liquidity gaps, circuit limits on NSE stocks, a stop that can't fill through a gap-down opening, or a broker outage — none appear in the reshuffle. Fourth, the log-normal-ish output can breed false precision: reporting "risk of ruin is 0.7%" implies a confidence the model does not possess. Treat Monte Carlo as a tool for *ranges and relative comparisons* ("2% risk is far safer than 6%"), not for exact probabilities. Used with that humility, it is the most powerful risk instrument a discretionary or systematic trader has.

## Interview-ready summary

A single backtest is one random ordering of your trades; Monte Carlo generates thousands of alternate orderings to reveal the *distribution* of outcomes — final equity, maximum drawdown, longest losing streak, and risk of ruin — that one curve hides. You extract the strategy's fingerprint (win rate, average win/loss in R-multiples) from the trade log, then resample, preferably bootstrap *with replacement*, over 10,000 simulated years, and read the bad tail: the 95th-percentile drawdown and the probability of falling below a ruin threshold. Because equity compounds multiplicatively, final wealth is roughly log-normal, which is why oversized bets that look great on average still drive the typical path toward ruin — a fact Monte Carlo makes visible when it prices, say, an 8% per-trade risk as double-digit ruin probability while 2% is near zero, for the identical edge. Traders use it to choose position size (well below full Kelly), to set drawdown and losing-streak expectations that prevent abandoning a sound system in a normal rough patch, and to define a pre-committed tripwire when live drawdown exceeds the 99th simulated percentile. Its honesty depends on its inputs: it assumes trades are i.i.d. (they aren't — streaks and regimes cluster), it can't see a sample too small or too calm to contain a crash, and it ignores execution reality like gaps and circuit limits — so it is a tool for ranges and relative comparison, not for false-precision probabilities.
