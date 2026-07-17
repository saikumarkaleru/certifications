# vectorbt & backtesting.py (Deep)

## The concept

Computing indicators is not backtesting. A backtest answers a harder question: *if I had actually placed these orders, with real fills, real costs, and real position sizing, what would my equity curve, drawdown, and risk-adjusted return have been?* Two Python libraries dominate this space for the individual quant, and they represent two different philosophies you should understand before picking one.

**vectorbt** is *vectorised*: it represents the entire history as NumPy arrays and simulates thousands of parameter combinations at once, in bulk, extremely fast. It is built for *research at scale* — sweeping a 20×20 grid of EMA lengths across all Nifty stocks in seconds, producing a heatmap of Sharpe ratios. Its strength is throughput; its danger is that vectorisation makes it easy to accidentally encode look-ahead or unrealistic fills if you do not think carefully.

**backtesting.py** is *event-driven* (bar-by-bar): it steps through candles one at a time, calling your `next()` method on each bar, exactly as a live system would. It is slower and single-strategy-at-a-time, but its sequential nature makes complex, path-dependent logic (trailing stops, partial exits, pyramiding, "only one position at a time") natural and hard to cheat on. Its strength is realism and clarity; its weakness is speed — you do not sweep 400 parameter sets in it comfortably.

The professional pattern is to use **both**: vectorbt to *explore* a large parameter/universe space and find robust regions, then backtesting.py (or a custom event loop) to *confirm* the finalists with realistic, path-dependent execution. Neither is a toy — but neither is a live-trading engine either. Both simulate on historical bars; live slippage, partial fills, and latency will always be worse than the sim.

## The method and the maths (precise)

### vectorbt: from signals to portfolio

vectorbt's core object is a `Portfolio`. The cleanest entry point is `Portfolio.from_signals`, which takes a price series and boolean `entries`/`exits` arrays and simulates the whole thing:

```python
import vectorbt as vbt
import numpy as np, pandas as pd

price = vbt.YFData.download("^NSEBANK", start="2016-01-01").get("Close")

fast = vbt.MA.run(price, 20).ma
slow = vbt.MA.run(price, 50).ma
entries = fast.vbt.crossed_above(slow)
exits   = fast.vbt.crossed_below(slow)

pf = vbt.Portfolio.from_signals(
    price, entries, exits,
    init_cash=200_000,
    fees=0.0003,        # 3 bps per side (approx brokerage+exch)
    slippage=0.0005,    # 5 bps slippage
    freq="1D",
)
print(pf.stats())          # total return, Sharpe, max DD, win rate...
print(pf.total_return(), pf.sharpe_ratio(), pf.max_drawdown())
```

The maths under the hood: vectorbt processes signals in order, but because entries/exits are pre-computed arrays, **you** are responsible for ensuring those arrays only use information available at each bar. If you compute a crossover on the *close* and let `from_signals` fill on the *same bar's close*, you have a subtle look-ahead unless you shift or use the next open. Use `Portfolio.from_signals(..., price=open_next)` or shift entries by one bar to model "signal on close, fill next open."

The parameter-sweep superpower:

```python
windows = np.arange(10, 60, 5)
fast_ma, slow_ma = vbt.MA.run_combs(price, window=windows, r=2, short_names=["f","s"])
entries = fast_ma.ma_crossed_above(slow_ma.ma)
exits   = fast_ma.ma_crossed_below(slow_ma.ma)
pf = vbt.Portfolio.from_signals(price, entries, exits, fees=0.0003, freq="1D")
sharpe = pf.sharpe_ratio()          # a Series indexed by (fast, slow) pair
sharpe.vbt.heatmap().show()          # visual robustness map
```

That heatmap is the single most useful vectorbt output: you are looking for a *plateau* of good Sharpe across neighbouring parameters, not an isolated spike. A spike is overfitting; a plateau is a robust region.

### backtesting.py: event-driven realism

backtesting.py wants a `Strategy` subclass with `init()` (compute indicators once) and `next()` (called per bar):

```python
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import pandas_ta as ta

class EmaPullback(Strategy):
    fast_len = 20
    slow_len = 50
    atr_len  = 14
    rr       = 1.5

    def init(self):
        c = pd.Series(self.data.Close)
        self.fast = self.I(lambda: ta.ema(c, self.fast_len))
        self.slow = self.I(lambda: ta.ema(c, self.slow_len))
        self.atr  = self.I(lambda: ta.atr(pd.Series(self.data.High),
                                          pd.Series(self.data.Low), c, self.atr_len))

    def next(self):
        price = self.data.Close[-1]
        if not self.position and crossover(self.fast, self.slow):
            stop = price - 1.5 * self.atr[-1]
            tp   = price + self.rr * 1.5 * self.atr[-1]
            self.buy(sl=stop, tp=tp)

bt = Backtest(df, EmaPullback, cash=200_000,
              commission=0.0006, trade_on_close=False)
stats = bt.run()
print(stats)                 # Return %, Sharpe, Max DD, Win Rate, # Trades
bt.plot()
```

Key realism levers: `commission` (fraction per trade), `trade_on_close=False` (fill at next open, not the signal bar's close — avoids look-ahead), and `sl`/`tp` handled *inside* the bar sequentially. Because `next()` runs strictly left to right, a trailing stop is just code that updates `self.position` each bar — no vector gymnastics, no accidental peeking at the future.

Optimisation is built in but slower:

```python
stats = bt.optimize(fast_len=range(10, 40, 5),
                    slow_len=range(40, 80, 5),
                    rr=[1.0, 1.5, 2.0],
                    maximize="Sharpe Ratio",
                    constraint=lambda p: p.fast_len < p.slow_len)
```

Use `constraint` to forbid nonsensical combos and always beware that `bt.optimize` maximising in-sample Sharpe is exactly how you overfit — reserve out-of-sample data.

## A worked example (levels and rupees)

Let's carry the Bank Nifty EMA-pullback idea from the Pine chapter through both engines and read the ₹ output honestly. Assume Bank Nifty daily data, spot ~52,000, and a fixed 1-lot (15-unit) sizing.

In **vectorbt**, sweeping fast ∈ {15,20,25} and slow ∈ {40,50,60} with `fees=0.0003, slippage=0.0005` might produce a heatmap where the (20,50) cell shows Sharpe ~0.9 and neighbours (20,45), (25,50) show ~0.8–0.9 — a healthy plateau. The (15,40) corner might spike to 1.3 but with its neighbours at 0.4 — a red flag, that is noise, discard it. You pick (20,50) *because it is boring and robust*, not because it is highest.

Now confirm (20,50) in **backtesting.py** with proper stops. Suppose it reports: 142 trades over 8 years, win rate 47%, average win 1.5R, Return 118%, Max Drawdown −22%, Sharpe 0.85. Translate to money on ₹2,00,000:

- Per-trade risk (1.5×ATR, ATR≈180, 15 units) ≈ 270 × 15 = ₹4,050 ≈ 2% of capital — aggressive.
- Break-even win rate at 1.5R ≈ 40%; realised 47% → positive expectancy, thin but real.
- **Costs check**: 142 trades × round-turn cost (~₹250 all-in incl. STT, brokerage, slippage) ≈ ₹35,500 drag over 8 years. If gross profit was ~₹2,70,000, net is ~₹2,35,000 — costs ate ~13%. On an *intraday* version with 1,400 trades, the same per-trade drag becomes ₹3,50,000 and very likely turns the whole thing negative. This is the lesson: the daily version survives costs; the tempting intraday version may not, and only an honest backtest reveals it.
- **Drawdown reality**: −22% max DD means ₹44,000 underwater at the worst point. Can you hold a single-lot Bank Nifty position through that psychologically? If not, the "profitable" system is untradeable for *you* — size down.

## How to use it in a real TA workflow

1. **Explore in vectorbt.** Sweep parameters and the symbol universe. Produce Sharpe/drawdown heatmaps. Reject spikes, keep plateaus. This is triage across hundreds of configurations.
2. **Confirm in backtesting.py.** Take 2–3 plateau finalists and re-run with path-dependent logic — trailing stops, partial exits, one-position-at-a-time, session filters. This is where you find that a rule which looked fine in bulk actually behaves badly bar-by-bar (e.g., stops and targets colliding intrabar).
3. **Walk-forward.** Split history into rolling in-sample/out-of-sample windows (e.g., train 2 years, test 6 months, roll). A strategy that only works when the test window follows its own optimisation window is fit to noise. vectorbt has splitter tools; backtesting.py you can loop manually.
4. **Cost-stress and slippage-stress.** Re-run with 1.5× and 2× your assumed costs and slippage. If the edge dies, it was a cost illusion. Indian F&O costs (especially STT on the options sell side) make this test essential.
5. **Paper/forward test** via the alert pipeline from the Pine chapter before committing real size.

A subtle but important point about *intrabar fills*: both libraries, working on daily/15-min bars, do not know the true tick path inside a candle. When both your stop and target lie within one bar, the sim must assume an order (backtesting.py assumes worst-case-ish ordering; vectorbt has conventions). To reduce this uncertainty, backtest the exit logic on a *finer* timeframe than the entry, or accept that same-bar stop/target results are optimistic and haircut them.

## Honest limitations

- **Vectorisation hides look-ahead.** vectorbt's speed comes from computing everything at once; it is trivially easy to let a signal fill on the same bar it was computed from. Always model "signal on close → fill next open" via shifting or `price=next_open`.
- **Both are historical simulators, not execution engines.** No real latency, no partial fills on a 200-lot order, no queue position, no auction-open quirks, no circuit-breaker halts. Live results are worse — plan for it.
- **Overfitting is one line away.** `pf.sharpe_ratio()` across a grid and `bt.optimize()` both invite you to pick the peak. The peak is almost always noise. Robust plateaus and out-of-sample confirmation are non-negotiable.
- **Costs and lot sizes must be right.** Wrong lot size, zero STT, or optimistic slippage produce curves that do not survive contact with a real Zerodha contract note. Model Indian costs explicitly and stress them.
- **Data biases persist downstream.** Survivorship (testing on today's Nifty constituents), unadjusted splits, and continuous-futures stitching corrupt the backtest no matter how good the engine. Garbage in, confident-looking equity curve out.
- **Metrics can mislead.** A high total return with −40% drawdown and 6 trades is not an edge; it is luck with a small sample. Weight Sharpe/Calmar, drawdown, trade count, and out-of-sample stability over headline return.
- **Speed vs realism is a genuine trade-off.** vectorbt cannot easily express some path-dependent rules; backtesting.py cannot sweep large spaces quickly. Using the wrong tool for the phase wastes days.

## Interview-ready summary

vectorbt is the *vectorised* backtester — array-based, blazing fast, built to sweep thousands of parameter/universe combinations and produce Sharpe heatmaps; its risk is that speed hides look-ahead and encourages peak-picking. backtesting.py is the *event-driven* backtester — bar-by-bar `init()`/`next()`, slower but naturally realistic for trailing stops, partial exits, and one-position logic. The professional flow uses both: explore and find robust *plateaus* in vectorbt, then confirm the finalists path-dependently in backtesting.py, then walk-forward and cost-stress. Set fills to "signal on close, execute next open" (`trade_on_close=False`, or shift entries) to kill look-ahead; encode real Indian costs (brokerage, STT, slippage) and correct lot sizes; and always haircut same-bar stop/target results. Both are simulators, not live engines — live will be worse. Judge results on drawdown, trade count, and out-of-sample stability, never on headline return, and remember that the highest-Sharpe cell is usually the most overfit one.
