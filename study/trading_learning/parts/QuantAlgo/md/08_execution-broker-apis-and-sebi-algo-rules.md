# Execution, Broker APIs & the SEBI Retail-Algo Framework (2026)

## Why this matters

A backtest with a great Sharpe and a live account that loses money are separated by one thing amateurs ignore: **execution**. Slippage, latency, partial fills and rejected orders quietly erode edge, and a system that trades 100 times a day can lose its entire theoretical profit to bad fills. Worse, since **01-Apr-2026 SEBI's retail algo framework is mandatory** — and getting it wrong is no longer a "your P&L" problem, it's a *compliance* problem that can freeze your account or expose you to penalties. Pros treat execution and compliance as first-class engineering, not an afterthought. This chapter covers the execution layer (routing, paper trading, slippage/latency), the Zerodha Kite Connect flow as the concrete Indian example, and — most importantly — the 2026 SEBI rules you must obey before a single automated order goes out. Compliance first; cleverness second.

## The essentials

**Order routing & types.** Your order travels app/API → broker OMS/risk checks → exchange (NSE/BSE) matching engine → confirmation back. Use the right type: **MARKET** (guaranteed fill, unknown price — dangerous in illiquid/fast markets), **LIMIT** (known price, maybe no fill), **SL / SL-M** (stop-loss trigger). For anything beyond the most liquid names, prefer LIMIT to control slippage.

**Paper trade first.** Before real capital, run the *live signal* against live data placing simulated orders (or use the broker's sandbox). This surfaces the gap between backtest fills and reality — the single most sobering step for a new algo trader.

**Slippage & latency.** Slippage = (fill price − intended price). Latency = time from signal to fill (network + broker + exchange). For retail on a broker REST API, expect tens to hundreds of milliseconds — you are *not* competing with co-located HFT, so **do not design strategies whose edge lives inside a few milliseconds.** Choose signals that tolerate realistic fills.

**Zerodha Kite Connect flow (concrete India example).**

| Step | What happens |
|---|---|
| Auth | App `api_key`/`api_secret`; user login → `request_token` → exchange for a daily `access_token` (expires each day — re-auth daily) |
| Place | `kite.place_order(variety, exchange, tradingsymbol, transaction_type, quantity, order_type, product, price)` → returns `order_id` |
| Modify / Cancel | `kite.modify_order(...)`, `kite.cancel_order(...)` by `order_id` |
| Postbacks | Webhook pushes order status updates (COMPLETE/REJECTED/etc.) — event-driven, don't poll |

```python
from kiteconnect import KiteConnect
kite = KiteConnect(api_key="xxx")
kite.set_access_token(access_token)          # from daily login flow
oid = kite.place_order(variety=kite.VARIETY_REGULAR,
        exchange=kite.EXCHANGE_NFO, tradingsymbol="BANKNIFTY26JUL52000CE",
        transaction_type=kite.TRANSACTION_TYPE_BUY, quantity=15,
        order_type=kite.ORDER_TYPE_LIMIT, product=kite.PRODUCT_MIS, price=180.5)
```

**The mandatory SEBI Retail Algo Framework (effective 01-Apr-2026).** Every algo order must carry an **exchange-registered Algo-ID** so the exchange can tag and trace it. **Open/unauthenticated APIs are BANNED** — retail algos may run *only* through a registered broker's authenticated API. **Third-party algo vendors must tie up with a registered broker** and register their algo with the exchange. **Orders above 10 per second** from a retail participant require specific exchange approval/registration (treated like higher-frequency activity). **The broker is responsible** for algos operating on its platform — meaning they enforce these rules on you. Static/DIY logic below the order-rate threshold, through your own broker's authenticated API, is the retail-friendly path; anything faster or offered to others crosses into registration territory.

*All rules as of July 2026 — the SEBI algo framework, STT and margin rules change; verify on the SEBI circulars, NSE/BSE notices and your broker's algo policy before deploying.*

## Worked example

You've validated the Bank Nifty trend system from the Python chapter and want it live via Kite Connect.

- **Instrument/costs:** Bank Nifty options, lot = 15. Say the system fires ~8 signals/day. That's ~16 orders/day round-trip — **well under 10 orders/second**, so no special exchange registration for order-rate; but you still need a **valid Algo-ID** tagged to every order, obtained via your broker's algo-registration process (Zerodha's static-algo registration), because from 01-Apr-2026 automated orders without one can be rejected/flagged.
- **Compliance path:** register the strategy with the broker → receive Algo-ID → route orders through the authenticated Kite Connect API (never a scraped/open API) → keep audit logs.
- **Slippage reality check:** backtest assumed fills at ₹180.50. Live, over 200 trades you observe an average fill of ₹181.20 on entries and ₹179.60 on exits — ~₹1.10 total slippage per unit × 15 × 200 = **₹3,300** of edge quietly gone, *before* STT (options ~0.15% on premium sell from 01-Apr-2026), brokerage, exchange txn, 18% GST and stamp. If the backtested edge was ₹4,000, you're barely breakeven — which is *exactly* why you paper-trade to measure real slippage before committing capital.
- **Latency:** signal→fill ~150 ms on a home connection is fine for a daily/positional trend system; it would be fatal for a "scalp the first tick" idea, so you don't build that idea.

## How pros do it / common mistakes

- **Pros are compliance-first.** They obtain the Algo-ID, use only the broker's authenticated API, stay under the order-rate threshold unless properly registered, and keep immutable logs. They treat SEBI rules as hard constraints, not suggestions.
- **They paper-trade to measure slippage** and only fund a strategy once live fills confirm the backtest edge survives.
- **They build kill-switches and reconciliation** — a max-loss auto-halt, and end-of-day checks that broker positions match the system's expected positions.
- **They handle failures** — rejected orders, token expiry, network drops — with retries and alerts, never assuming a placed order filled.
- **Retail mistakes:** using banned open/unofficial APIs (post-01-Apr-2026 this risks account action, not just rejects); hardcoding a `MARKET` order into an illiquid option and eating huge slippage; ignoring daily `access_token` expiry so the bot silently stops; assuming placement = fill; deploying a millisecond-edge idea on a REST API that will never be that fast; no kill-switch on a runaway loop.
- **Red flags:** any dependency on an unregistered third-party algo without a broker tie-up; sustained order rates near/over 10/sec without exchange registration; live P&L diverging from backtest by more than modelled costs (usually slippage or a bug).

## Checklist / drill

Pre-deployment compliance & execution gate (as of July 2026 — re-verify current SEBI/exchange rules):

1. Does every automated order carry a valid **exchange Algo-ID** via my broker's registration?
2. Am I routing **only through the broker's authenticated API** (no open/unofficial APIs)?
3. Is my **order rate < 10/sec** — or am I properly exchange-registered for more?
4. Have I **paper-traded** long enough to measure real **slippage & latency**, and does the edge survive them plus full costs?
5. Do I have a **kill-switch, daily token-refresh handling, and position reconciliation**?

**Drill:** Take your validated strategy and run it in **paper mode against live market data for two weeks** without real capital. Log intended price vs simulated fill for every order, compute average slippage per trade, and subtract it (plus STT/GST/exchange/stamp) from the backtest edge. If the net edge disappears, the strategy was never real — you just saved yourself the tuition. Only strategies that survive this go live, and only after the Algo-ID and API-compliance boxes above are all ticked.
