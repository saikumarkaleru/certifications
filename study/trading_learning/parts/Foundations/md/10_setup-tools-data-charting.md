# Setting Up: Platforms, Charting & Data

## Why this matters

The gap between a retail trader and a pro is often not strategy — it's **infrastructure and workflow**. Retail trades from a phone, on one screen, reacting to Twitter/Telegram tips, with no scanner, no alerts, and no idea of true costs. A pro has a clean, deliberate stack: an execution terminal, a charting layer, a scanner to find setups *before* they're obvious, official data (not forwarded screenshots), and alerts so they aren't glued to the screen making impulse trades. You do **not** need an expensive setup — India's ecosystem gives you a professional-grade stack for close to zero. What you need is the *discipline* of separating the four jobs — **execute, chart, scan, verify** — and not mixing them. This chapter builds that starter stack, India-first, and is honest about what's worth paying for and what isn't.

(Tools, plans, and prices below are as of July 2026 — verify current offerings with each provider; they change.)

## The essentials

Think of your setup as four layers, each doing one job:

| Layer | Job | India-first tools | Free vs paid |
|---|---|---|---|
| **Execution** | Place/manage orders, margins, positions | Zerodha **Kite**, Dhan, Upstox, Fyers, Angel One | Free platform; you pay brokerage + statutory charges |
| **Charting** | Analyse price, draw, indicators | **TradingView**, Kite charts, Fyers, GoCharting | Free tier works; paid = more indicators, multi-chart, alerts |
| **Scanning** | Find setups across 1,900+ stocks | **Chartink**, TradingView screener, Streak | Chartink free tier strong; paid for real-time/more scans |
| **Data / verify** | Official prices, option chain, filings | **NSE India site**, BSE site, NSDL/CDSL, broker feed | Free (official) |

**Execution — the broker terminal.** Your broker (e.g. Kite) is where money actually moves. Learn its order types cold: **Market, Limit, SL (stop-loss limit), SL-M (stop-loss market)**, GTT (Good-Till-Triggered), and the margin/positions/funds tabs. Know that live order data on the terminal is your ground truth for fills. Note: under SEBI's **retail algo framework (mandatory 01-Apr-2026)**, open APIs are banned and any automated order needs an exchange **Algo-ID** via your registered broker — so "auto-buy" bots you find online are now non-compliant unless routed through a registered broker's approved API. Verify on SEBI/NSE circulars.

**Charting — TradingView.** The de-facto standard. Free tier: real-time-ish NSE data (with a small delay unless you take the paid real-time add-on), unlimited saved layouts, most indicators, one or two alerts. Paid tiers (Essential/Plus/Premium) unlock multiple charts per tab, more alerts, more indicators, and second-based intervals. For Indian data, connect via a supported broker (Zerodha, Dhan, Fyers, etc.) so you can also trade from the chart.

**Scanning — Chartink.** India's most-used free screener. You build a scan in plain conditions ("close crossed above 20 SMA and volume > 2× average") across NSE/BSE and get a live list. This is how you stop *hunting* and start *filtering*. Paid tier adds real-time scanning and more saved scans.

**Data / verify — the NSE site.** For the **official option chain**, delivery %, market-wide position limits, F&O ban list, corporate actions, and circulars, go to the source: **nseindia.com**. Never trade off a forwarded screenshot; the free official data is more reliable than any paid "tip" channel.

**Watchlists & alerts.** Keep a *small* watchlist (say 15–25 names you actually understand: Nifty/Bank Nifty, a few index heavyweights, your sector focus). Set **price and indicator alerts** so you can step away — the single biggest edge of alerts is that they stop you from overtrading out of boredom.

**A clean workstation.** Two screens if you can (chart + terminal); a wired connection or reliable broadband; a backup — mobile hotspot and your broker's phone app and call-and-trade number saved, because internet *will* drop mid-position.

## Worked example — a zero-to-₹0 starter stack

Priya has ₹2,00,000 to trade Nifty/Bank Nifty and a few large caps. Her starter stack, July 2026:

- **Broker:** Zerodha Kite — account opening free; she'll pay brokerage (₹20 or 0.03% per executed order, whichever lower, for intraday/F&O; **₹0 on equity delivery** at Zerodha) plus statutory charges. **Cost: ₹0 to set up.**
- **Charting:** TradingView **free** tier, connected to her Zerodha account. **Cost: ₹0.** She'll consider the paid plan only once she needs 4 charts + many alerts.
- **Scanner:** Chartink **free** — three saved scans: (1) breakout on volume, (2) 20/50 EMA pullback, (3) 52-week-high proximity. **Cost: ₹0.**
- **Data:** nseindia.com bookmarked — option chain, F&O ban list, corporate actions. **Cost: ₹0.**
- **Alerts:** 10 TradingView alerts on her watchlist levels. **Cost: ₹0.**

**Total monthly software cost: ₹0.** Now the honest part — the money leaves via *charges*, not subscriptions. One Bank Nifty option round trip (buy + sell, premium say ₹200 × lot 15 = ₹3,000 notional premium each way): brokerage ₹20 + ₹20 = ₹40; **STT ~0.15% on premium on the sell side** (from 01-Apr-2026) ≈ ₹4.5–9; plus exchange txn charge, **SEBI charge, 18% GST on (brokerage + txn), and stamp duty**. On small tickets these fixed-ish costs are a *large* % — which is exactly why overtrading a free setup still drains an account. The stack is free; the *activity* is not. Verify current brokerage and STT with your broker.

When should Priya pay? Only when a paid tool **removes a real bottleneck** — e.g. TradingView Plus once she genuinely needs multi-chart + real-time NSE data, or Chartink real-time once end-of-scan lists arrive too late. Paying for "tips", "sure-shot calls", or Telegram/algo signal groups is a red flag, not a tool.

## How pros do it / common mistakes

- **Separate the four jobs.** Don't scan, chart, and execute in one cramped phone window — impulse follows. Terminal for execution, chart for analysis, scanner for ideas, NSE for truth.
- **Data hygiene.** Verify on the official NSE/BSE/SEBI source. Screenshots forwarded on WhatsApp are how people get trapped into pump-and-dumps.
- **Small watchlist, deep knowledge** beats 200 tickers you don't understand.
- **Alerts over screen-staring.** The pro sets levels and walks away; the amateur watches every tick and revenge-trades.
- **Beware "signal" services and unapproved algos.** Post SEBI's 01-Apr-2026 algo framework, open-API auto-trading bots are non-compliant; third-party vendors must tie up with a registered broker and carry an Algo-ID. Anyone selling you an "open API bot" is selling a compliance and money risk.
- **Know your true costs before you scale size.** Free software hides the real leak: STT + txn + GST + stamp duty stacked on frequent small trades.

## Checklist / drill

**Starter setup checklist:**

- [ ] Broker account funded; **order types learned** (Market, Limit, SL, SL-M, GTT).
- [ ] Call-and-trade number + broker app saved as internet backup.
- [ ] TradingView account, connected to broker, one clean layout saved.
- [ ] 3 Chartink scans saved and tested end-of-day.
- [ ] nseindia.com bookmarked: option chain, F&O ban list, corporate actions.
- [ ] Watchlist trimmed to ≤ 25 names you understand.
- [ ] 5–10 alerts set on key levels.
- [ ] A **cost sheet** for your typical trade (brokerage + STT + txn + SEBI + GST + stamp).
- [ ] Two screens (ideal) or a disciplined single-screen layout.

**Drill:** For one week, place **zero** trades. Only: build the scans, set alerts, and each evening log which alerts fired and whether the setup was clean. You'll learn your tools *and* prove to yourself how many "opportunities" were noise — before a single rupee is at risk.

*(All tools, plans, prices, and charges as of July 2026 — verify with each provider, NSE, and SEBI; they change.)*
