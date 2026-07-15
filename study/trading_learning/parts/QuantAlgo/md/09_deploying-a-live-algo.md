# Deploying & Running a Live Algo

## Why this matters

Your backtest showed a beautiful equity curve. That is the easy 20%. The other 80% — the part that separates a hobbyist from a professional — is running the thing live, unattended, without it blowing up your account while you sleep or step away for chai. A backtest is a spreadsheet that never disconnects, never gets a partial fill, never sees SPAN margin spike at 14:55, and never has its VPS reboot for a Windows update mid-position. Live is where all of that happens on the same day.

The retail gap here is brutal. Most retail "algos" are a Python loop on a home laptop with `while True: place_order()`, no logging, no reconciliation, no kill-switch — and a broker API key. When the Wi-Fi drops mid-trade, the trader has an open naked Bank Nifty position and no idea. Pros treat deployment as an engineering problem: assume every component *will* fail, and design so that failure is safe (flat or hedged), not catastrophic. This chapter is that engineering discipline, India-specific.

**A compliance note you cannot skip (as of 2026 — verify on NSE/SEBI, rules change):** Under SEBI's retail algo framework, **mandatory from 01-Apr-2026**, every algo order must carry an **exchange Algo-ID**, **open/unregistered APIs are banned**, and retail algos may only run **through your registered broker's authenticated API**. Orders above **10/second** need exchange approval/registration, and the **broker is responsible** for algos on their platform. Third-party algo vendors must tie up with a registered broker. Translation: you deploy against Zerodha Kite Connect, Dhan, Fyers, etc. with proper auth — not a scraped session token.

## The essentials

Think of a live deployment as five layers, each of which must be independently reliable.

| Layer | What it does | India-specific detail |
|---|---|---|
| **Infra** | Where code runs 24/5 | VPS/cloud in **Mumbai region** (AWS ap-south-1 / low-latency co-lo). ~5–20 ms to NSE beats a home line's 60–150 ms + outages. |
| **Scheduler** | Starts/stops the strategy on the clock | Login token refresh **before 09:15**, square-off timer at **15:20**, hard stop by **15:30**. |
| **Logging** | Immutable record of every decision & order | Every signal, order request, order response, fill, error — timestamped to the millisecond. |
| **Monitoring** | Tells you when something breaks | Heartbeat + alerts to Telegram/phone, not just an email you'll read tomorrow. |
| **Reconciliation** | "Does the broker agree with me?" | Compare *my* expected positions/orders vs broker's actual, every cycle. |

**Scheduling.** Indian equity/F&O trades **09:15–15:30 IST**. Your daily flow: (1) a cron/scheduler job at ~08:45 refreshes the broker access token (Kite tokens expire daily — you must re-auth each morning), (2) strategy starts consuming ticks at 09:15, (3) a forced square-off at 15:20 for intraday, (4) everything hard-flat and process idle by 15:30. Never let an intraday algo carry a position past auto-square-off — the broker's RMS will close it at a worse price and charge you for it.

**Logging.** Two streams: a human-readable app log and a structured **orders ledger** (CSV/SQLite/DB row per order with `client_order_id`, timestamp, symbol, side, qty, price, status, broker_order_id). The `client_order_id` you generate is your anchor for reconciliation and for tax/audit later.

**Monitoring & kill-switch.** A **heartbeat**: the process writes "alive + P&L + open positions" every 30–60 s to a channel you watch. Two automated cutoffs must exist:
- **Max-loss cutoff:** if realized+unrealized P&L breaches a rupee floor, square off everything and **stop trading for the day**.
- **Kill-switch:** a manual big red button (a Telegram command or a sentinel file) that flattens and halts, for when *you* see something wrong that the code doesn't.

**Disconnects & partial fills.** Assume the WebSocket tick feed will drop. On disconnect: stop generating new entries, reconnect with backoff, and on reconnect **reconcile before acting**. For orders, never assume "placed = filled." Poll order status / consume postbacks; handle `qty=100 requested, 50 filled` explicitly (you own 1 lot, not 2).

## Worked example

Strategy: intraday **Bank Nifty** long-straddle-scalp exit logic — but the point here is the *deployment*, so take a simple one: buy 1 lot Bank Nifty futures on a signal, target/stop intraday, forced square-off 15:20. **Bank Nifty futures lot = 15** (verify current lot on NSE — revised periodically). At an index level of 52,000, 1 lot notional ≈ ₹7,80,000; SPAN+Exposure margin ≈ ₹1.4–1.6 lakh (varies daily — check broker margin calc).

Deployment settings:
- **VPS:** AWS ap-south-1, ₹1,200–2,500/month t3.small. Measured latency to broker: 8 ms.
- **Max-loss cutoff:** ₹6,000/day (roughly 0.8 Bank Nifty point-move × 15 × a few ticks buffer, sized to ~4% of the margin block).
- **Per-trade stop:** 120 points = 120 × 15 = **₹1,800**.

Now the live-vs-backtest reality on one round trip (approx, **STT from 01-Apr-2026** — futures ~0.05% on **sell** side; verify with broker contract note):
- Buy 52,000, sell 52,120 (a +120 winner). Gross = 120 × 15 = **₹1,800**.
- Costs: brokerage ₹20 (₹40 both legs, capped) + STT on sell ≈ 0.05% × (52,120×15) ≈ **₹391** + exchange txn + SEBI + stamp + **18% GST** on (brokerage+txn) ≈ another ₹30–60. Realistic total costs ≈ **₹450–480**.
- **Net ≈ ₹1,320 on a ₹1,800 gross winner.** Your backtest that ignored STT/GST was overstating each winner by ~₹450 and understating each loser by the same. Over 200 trades/month that is ~₹90,000 of pure friction the backtest hid.

The disconnect scenario that pays for all this plumbing: at 11:32 the tick feed drops for 90 seconds while you're long 1 lot. A naive loop keeps firing on stale prices. The engineered version: heartbeat misses → alert fires → new-entry logic freezes → on reconnect, reconciliation reads broker positions, confirms 1 lot long still open, resumes stop management. No duplicate order, no phantom position.

## How pros do it / common mistakes

**How pros do it**
- **Paper → small-live → scale.** Run the exact live code against a paper/simulated broker for 2–4 weeks, then live with **1 lot and a tiny max-loss** for 3–4 weeks, only then scale size. The bugs that matter (token refresh, partial fills, reconnect) only appear live.
- **Idempotent orders.** Generate a unique `client_order_id`; never re-fire an order just because you didn't see a response — check first.
- **Reconcile every loop**, and again at startup (you may restart mid-day into an existing position).
- **Fail flat.** Any unhandled exception → square off (or confirm hedged) and halt, rather than continue in an unknown state.
- **Separate config from code.** Max-loss, lot size, symbol in a config file you can change without redeploying.

**Common retail mistakes / red flags**
- Home laptop + home Wi-Fi as "production." One power cut = open naked position.
- No max-loss cutoff — the algo "revenge trades" a bad day to -₹80,000.
- Assuming fills; double-sizing on partials.
- Backtest with **zero costs** — then live bleeds on STT/GST/slippage.
- Hard-coding a broker token that expires at midnight; algo silently dead next morning.
- Running an **open/third-party API** algo — now outright non-compliant under the 2026 SEBI framework (verify on SEBI/NSE).
- No reconciliation → your code thinks flat, broker RMS auto-squared you at 15:20 at a bad price.

## Checklist / drill

**Pre-deploy checklist (run before going live with real money):**
1. Broker API registered, Algo-ID/authenticated API in place (SEBI 2026 compliant — verify).
2. VPS in ap-south-1; latency measured; auto-restart on reboot configured.
3. Daily token-refresh job scheduled and tested to succeed before 09:15.
4. Orders ledger writing every request/response with `client_order_id`.
5. Heartbeat posting P&L + positions to a channel on your phone.
6. **Max-loss cutoff** wired and unit-tested to square off + halt.
7. **Kill-switch** (manual flatten) tested end-to-end today.
8. Disconnect handling: reconnect-with-backoff + reconcile-before-acting.
9. Partial-fill logic explicitly handled and tested.
10. Forced square-off at 15:20; process idle by 15:30.
11. Costs (STT/GST/txn/stamp) modeled in the *live* P&L, not just backtest.
12. Startup reconciliation: on restart, read broker positions before trading.

**Drill:** In paper mode, kill your internet for 2 minutes mid-position. Confirm: no duplicate orders fired, the position is correctly reconciled on reconnect, an alert reached your phone, and the max-loss cutoff still armed. If any of those four fail, you are not ready for real money.

*Rules and figures date-stamped to 2026 — always re-verify STT, lot sizes, margins, and the SEBI algo framework on NSE/your broker/SEBI before deploying; they change.*
