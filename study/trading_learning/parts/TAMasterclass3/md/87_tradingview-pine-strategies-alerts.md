# TradingView Pine: Strategies & Alerts

## What it is and the logic

Pine Script is TradingView's domain-specific language for encoding indicators and trading strategies directly on the chart you already stare at all day. For an Indian retail or semi-pro trader, this matters because TradingView is where you likely already watch Nifty 50, Bank Nifty, Fin Nifty, MCX crude, and NSE cash stocks. Instead of eyeballing a 20-EMA crossover on Reliance and manually noting whether it "would have worked," Pine lets you write the rule once, run `strategy()` mode to get a backtest with a P&L curve, and then flip the same logic into `indicator()` mode to fire real alerts that can push to your phone, email, or a webhook that hits your broker's API.

The core mental model: Pine executes your script once per bar, left to right, from the oldest visible bar to the current one. On historical bars it runs on closed candles; on the live bar it re-runs on every tick (unless you tell it otherwise). Every variable is really a *series* — `close` is not one number, it is the whole array of closes, and `close[1]` means "close one bar ago." This series-first design is what trips up people coming from Python, and understanding it is 80% of writing correct Pine.

The honest framing up front: Pine's built-in `strategy` backtester is excellent for *idea triage* — killing bad ideas fast and comparing variations — but it is not a substitute for a proper vectorised or event-driven backtest in Python when money is on the line. It has real limitations around repainting, intrabar fills, and survivorship that we will cover in the Pitfalls section. Use it as a first filter, not as final proof.

## Construction: language rules and settings

Pine has gone through versions; **always write `//@version=6`** at the top in 2026. A script is one of three declaration types, and you pick exactly one:

| Declaration | Purpose | Can place orders? | Can fire alerts? |
|---|---|---|---|
| `indicator()` | Plot studies, fire `alert()` / `alertcondition()` | No | Yes |
| `strategy()` | Backtest + forward-test with virtual orders | Yes (`strategy.entry` etc.) | Yes (auto + manual) |
| `library()` | Reusable exportable functions | No | No |

A minimal but *realistic* Bank Nifty strategy skeleton:

```pine
//@version=6
strategy("BNF 20/50 EMA Pullback", overlay=true,
     initial_capital=200000,
     default_qty_type=strategy.fixed,
     default_qty_value=15,          // 1 lot BankNifty = 15 (2026)
     commission_type=strategy.commission.cash_per_order,
     commission_value=40,           // brokerage per order in Rs
     slippage=2,                    // ticks
     calc_on_every_tick=false,
     process_orders_on_close=true)

fastLen = input.int(20, "Fast EMA")
slowLen = input.int(50, "Slow EMA")
atrLen  = input.int(14, "ATR")
riskR   = input.float(1.5, "Reward multiple")

fast = ta.ema(close, fastLen)
slow = ta.ema(close, slowLen)
atr  = ta.atr(atrLen)

// session filter: NSE cash/F&O liquid window
inSession = not na(time(timeframe.period, "0930-1500", "Asia/Kolkata"))

longSetup  = ta.crossover(fast, slow) and inSession
stopDist   = 1.5 * atr

if longSetup and strategy.position_size == 0
    strategy.entry("L", strategy.long)
    strategy.exit("Lx", from_entry="L",
         stop = close - stopDist,
         limit = close + riskR * stopDist)

plot(fast, "Fast", color.aqua)
plot(slow, "Slow", color.orange)
```

Several construction rules are load-bearing here:

- **`default_qty_value=15`** encodes one Bank Nifty lot. If you copy a US example that uses a rupee amount as quantity, your backtest is nonsense. Set quantity in *contracts/shares*, and set lot sizes correctly (Nifty 75, Bank Nifty 15, Fin Nifty 25 — verify current SEBI/NSE values because they change).
- **`commission_value` and `slippage`** are the difference between a curve that looks like a rocket and one that reflects reality. On index options a flat cash-per-order plus 2-tick slippage is a *minimum* honest assumption.
- **`process_orders_on_close=true`** forces fills at bar close, which removes a subtle look-ahead problem where an order could otherwise be assumed to fill intrabar at a price you would not really have gotten.
- **The session filter** using `time(..., "0930-1500", "Asia/Kolkata")` keeps you out of gaps and prevents the backtester from pretending you traded at 3:31 pm on an illiquid post-close print.

### Alerts: the three mechanisms

There are three ways to emit signals, and they are not interchangeable:

| Mechanism | Where used | Dynamic message? | Notes |
|---|---|---|---|
| `alertcondition()` | indicator only | Limited (placeholders) | Older; must be manually added in UI |
| `alert()` | indicator + strategy | Yes (full string) | Fires from code at runtime; `freq` control |
| Strategy alerts | strategy only | Yes (`{{strategy.order.*}}`) | Auto-generated from order events |

The modern default is `alert()` inside your logic:

```pine
if longSetup
    alert("BUY BANKNIFTY 1 lot | px=" + str.tostring(close, "#.##") +
          " | stop=" + str.tostring(close - stopDist, "#.##"),
          alert.freq_once_per_bar_close)
```

`alert.freq_once_per_bar_close` is the safe frequency: it evaluates only when the bar closes, which eliminates the classic "alert fired then the candle reversed and un-fired" problem. Avoid `freq_once_per_bar` (fires intrabar) for anything you plan to trade mechanically.

## Worked India example (levels and rupees)

Let's design and reason through a concrete, tradable rule on **Bank Nifty, 15-minute chart**, and walk the numbers. Assume spot around 52,000 (a realistic 2026 level).

Strategy idea: *trend-pullback long*. We only go long when the daily trend is up (200-EMA on daily rising), we wait for the 15-min 20-EMA to cross above the 50-EMA after a shallow dip, and we filter for the liquid morning session.

We add a multi-timeframe filter using `request.security` — but carefully, to avoid repainting:

```pine
dailyEma = request.security(syminfo.tickerid, "D",
     ta.ema(close, 200)[1], lookahead=barmerge.lookahead_off)
trendUp  = close > dailyEma
```

Note two defensive choices: `[1]` takes the *previous* daily value (confirmed, not the still-forming today's daily EMA), and `lookahead=barmerge.lookahead_off` is explicit even though it is the default, because look-ahead here would let the strategy "know" the day's close before it happened — a fatal cheat.

Now the trade math. Suppose the setup triggers at close = 52,000, ATR(14) on 15-min = 180 points.

- Stop distance = 1.5 × 180 = 270 points → stop at 51,730.
- Reward multiple 1.5 → target = 52,000 + 405 = 52,405.
- Position = 1 lot Bank Nifty = 15 units.
- Risk if stopped = 270 × 15 = ₹4,050.
- Reward if target hit = 405 × 15 = ₹6,075.
- Costs: brokerage ~₹40 in + ₹40 out = ₹80, plus STT/exchange/GST/stamp — on a Bank Nifty futures round-turn realistically another ₹100–200. Slippage of 2 ticks (~2 points) on entry and exit ≈ 4 × 15 = ₹60. Call total frictions ≈ ₹250.

So the *net* winner is ~₹5,825 and the *net* loser is ~₹4,300. Your break-even hit rate is roughly 4,300 / (5,825 + 4,300) ≈ 42.5%. If your backtest shows a 50% hit rate at 1.5R gross, the edge survives costs but is thinner than the gross figure suggested — exactly the kind of reality-check Pine gives you when you fill in commissions honestly.

On a 200,000-capital account this is a single-lot Bank Nifty position risking ~2% per trade, which is aggressive; a more sober version would trade Fin Nifty or use a wider stop with fewer lots. The point of coding it is that you *see* these numbers instead of guessing.

## How to trade it: entry, stop, target, management

Translating Pine signals into real management:

- **Entry**: fire `alert()` on bar close, then enter market/limit near the alerted price. Do not chase if price has already run past your target minus 1R; the R:R is gone.
- **Stop**: encode the stop *in the strategy* with `strategy.exit(stop=...)` so the backtest and your live behaviour match. Live, place it as an actual SL order with your broker, not a mental stop.
- **Target and trailing**: Pine supports trailing via `trail_points` / `trail_offset` in `strategy.exit`. A common upgrade: take half off at 1R, trail the rest under a chandelier stop (`highest - 3*ATR`). You can model both legs with two `strategy.exit` calls or `strategy.close`.
- **Management via alerts**: emit distinct alert strings for ENTRY, MOVE-STOP, EXIT-HALF, EXIT-FULL so a webhook consumer (or you) can act unambiguously. Structure the message as JSON if a bot will parse it:

```pine
alert('{"action":"buy","symbol":"BANKNIFTY","qty":15,' +
      '"stop":' + str.tostring(close - stopDist) + '}',
      alert.freq_once_per_bar_close)
```

### Webhook wiring (honest version)

TradingView alerts can POST a JSON body to a webhook URL. In India, direct broker order placement from a webhook requires a middle layer — a small server (or a service) that receives the POST and calls your broker's API (Zerodha Kite Connect, Angel SmartAPI, Dhan, etc.). SEBI's algo-trading framework for retail (rolled out through 2025) requires broker-approved/registered strategies above certain order-rate thresholds, so fully automated execution is *not* a copy-paste hobby project — treat the webhook as a *signal delivery* mechanism and keep a human in the loop unless you have gone through your broker's approved-algo process.

## Confluence

Pine strategies improve dramatically when the entry is a *confluence* of independent conditions rather than one crossover. Good confluence layers that are cheap to code:

- **Regime filter**: only take longs when daily close > daily 200-EMA (coded above). This single filter usually cuts drawdown more than any parameter tweak.
- **Volatility filter**: skip signals when ATR% (`ta.atr(14)/close`) is in the top decile — those are gap/news days where stops slip badly. `ta.percentile_nearest_rank` or a rolling max makes this easy.
- **Breadth/relative strength**: for a stock, require it to outperform Nifty (`close/close_nifty` rising) using a `request.security` pull of the index.
- **Session/time-of-day**: many Indian intraday edges live in the 9:30–11:00 and 13:30–15:00 windows; the noon lull is chop. Encode it and let the backtest confirm.

Each filter you add should be justified by the backtest showing *better risk-adjusted* returns (higher profit factor or lower max drawdown), not just higher total profit — adding filters that only raise gross P&L while shrinking sample size is curve-fitting.

## Pitfalls

**Repainting.** The single biggest Pine trap. It comes in three flavours: (1) `request.security` with default `lookahead` on a higher timeframe can leak future data on historical bars — always use `[1]` and `lookahead_off`; (2) intrabar signals that flip before the bar closes — use `freq_once_per_bar_close` and `calc_on_every_tick=false`; (3) functions like `ta.valuewhen`/`ta.barssince` referencing not-yet-final conditions. Rule of thumb: if your backtest looks amazing but live alerts feel "late" or wrong, you are almost certainly repainting.

**Look-ahead in backtest fills.** Without `process_orders_on_close=true`, the tester may assume fills at prices unreachable in real time. Set it, and set realistic slippage.

**No costs = fantasy.** A strategy with 0 commission and 0 slippage that shows profit factor 1.4 often collapses below 1.0 once real Indian F&O costs (STT is meaningful, especially on the sell side of options) are applied. Always fill these in.

**Small sample / overfitting.** Pine makes it trivial to tweak inputs until the equity curve is beautiful. If you optimised across 12 parameters on 300 trades, you have memorised noise. Reserve the last 30–40% of history as untouched out-of-sample, and prefer parameters that are robust across a *plateau* of values, not a single spike.

**Bar-magnifier and intrabar order of fills.** On a single bar the tester assumes a fill sequence (open→high→low→close for up bars, the reverse for down bars) which may not match reality when both your stop and target sit inside one candle. TradingView's bar-magnifier feature (Premium) mitigates this by checking lower-timeframe data; without it, treat same-bar stop-and-target results with suspicion.

**Alert limits and downtime.** Free/Pro tiers cap active alerts; alerts can also miss if TradingView has an outage. Never build a system that *requires* every alert to fire perfectly with no reconciliation.

**Lot-size and expiry drift.** Hard-coded lot sizes go stale when NSE revises them; continuous futures charts stitch across expiries and can distort gaps. For F&O backtests, be aware you are testing on spot/continuous data, not the exact contract you will trade.

## Interview-ready summary

Pine Script is TradingView's series-based language with three modes — `indicator`, `strategy`, `library`. Write `//@version=6`, remember that every variable is a full time-series and `close[1]` is the prior bar. Use `strategy()` for fast idea triage: set lot-correct `default_qty_value`, real `commission_value` and `slippage`, and `process_orders_on_close=true` to avoid look-ahead. Encode risk with `strategy.entry` + `strategy.exit(stop=, limit=, trail_=)`. Fire signals with `alert()` at `alert.freq_once_per_bar_close`, emit JSON for webhook consumers, but keep a human in the loop given SEBI's retail-algo rules. The cardinal sin is repainting — always pull higher-timeframe data with `[1]` and `lookahead_off`, and never trust a cost-free, single-parameter-spike backtest. Pine is a first filter, not final proof; a surviving idea graduates to a proper Python backtest before it earns real size.
