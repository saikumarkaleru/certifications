# Positional Trading & Trend Following

## Why this matters — the pro vs retail gap this closes

Retail traders live inside the 5-minute chart. They scalp, they overtrade, they pay STT and brokerage 40 times a day, and they wonder why a "70% win-rate" system still bleeds. The professional edge in Indian equities over a career is captured mostly by a handful of multi-week and multi-month trends — the 2023-24 PSU and defence run, the 2020-21 pharma and IT surge, the capex/railways theme, individual movers like a stock that goes from ₹400 to ₹1,200 over eight months. Positional trend following is how you hold those moves without getting shaken out on every 3% dip.

The gap this closes: retail books a 6% winner because "profit is profit," then watches it become a 60% winner they missed. Pros do the opposite — they cut losers fast and let winners run for months, accepting many small losses to catch the few 3x-5x moves. This chapter is about the *holding* discipline, position building, and the tax-aware structure (delivery + LTCG) that makes it work in India.

## The essentials — India-specific mechanics

**Instrument and settlement.** Positional trend following in equities is done in the **cash/delivery segment** (shares hit your NSDL/CDSL demat, T+1 rolling settlement as of 2026 — *verify on NSE/broker, rules change*). You are NOT rolling futures every month, so you avoid roll costs and the ~₹ margin drag. You own the stock.

**Cost structure (from 01-Apr-2026, Budget 2026 — verify on NSE/SEBI):**

| Item | Delivery equity |
|---|---|
| STT | 0.1% on buy + 0.1% on sell |
| Brokerage | ₹0 (many discount brokers on delivery) to 0.3% |
| Exchange txn + SEBI + GST (18% on brokerage+txn) + stamp duty | small, few bps |

Because you trade rarely (a handful of entries a year per position), these costs are trivial versus an intraday churner.

**Tax structure (FY2026-27 — verify with a CA):**
- Held **> 12 months** → **LTCG**, taxed at the applicable LTCG rate with the annual exemption; this is the tax home of trend following. A stock held 14 months that triples is taxed gently.
- Held **≤ 12 months** → **STCG** at the applicable STCG rate.
- Delivery is treated as capital gains (if that is your consistent treatment), NOT business income — cleaner than F&O.

**The trailing toolkit** (you already know the indicators; here is how pros *use* them positionally):
- **Moving-average trail:** hold above the 20-week EMA (or 50-DMA) on a weekly close. Exit only on a decisive weekly close below.
- **ATR chandelier trail:** stop = highest-high-since-entry − (3 × 14-period ATR). Widens in volatile stocks, tightens in calm ones.
- **Structure trail:** exit when price makes a lower-high AND lower-low on the daily/weekly (trend structure breaks).

## Worked example — a positional trend trade

**Setup.** Stock XYZ (F&O + cash, highly liquid) breaks a 9-month base at **₹500** on heavy weekly volume, relative strength rising vs Nifty. Capital allocated: **₹5,00,000**. Risk per trade: **1.5% of ₹5,00,000 = ₹7,500**.

**Initial entry (scale-in plan).** Enter one-third first.
- Buy 1: 330 shares × ₹500 = **₹1,65,000**.
- Initial stop: weekly close below ₹465 (below the breakout pivot). Risk per share ≈ ₹35 → 330 × ₹35 = **₹11,550** open risk. Slightly above budget, so trim to 215 shares (215 × ₹35 = ₹7,525). Buy 1 = **215 shares @ ₹500 = ₹1,07,500**.

**Pyramiding (adding to a winner — the core skill).** Add only as the trend confirms and only if the *new* stop keeps total risk bounded.
- Price runs to **₹560**; move stop on the first tranche up to **₹520** (locks in ₹20/sh, ≈ breakeven-plus). Now add tranche 2: **150 shares @ ₹560**, stop ₹520 → new-lot risk 150 × ₹40 = ₹6,000. Blended stop keeps total risk near budget because tranche 1 is now house money.
- Price runs to **₹640**; raise combined stop to **₹590**. Add tranche 3: **120 shares @ ₹640**.

Position now: 215 + 150 + 120 = **485 shares**, avg ≈ ₹552, invested ≈ **₹2,67,700**.

**Trailing the runner.** Use a weekly 20-EMA trail plus a 3×ATR chandelier. Over the next 7 months the stock grinds to **₹980** with two scary 12-15% dips — both hold above the weekly 20-EMA, so you sit tight. On month 8 the stock closes a week decisively below the 20-EMA at **₹910**.

**Exit.** Sell 485 @ ₹910 = **₹4,41,350**. Gross gain = ₹4,41,350 − ₹2,67,700 = **₹1,73,650** on ₹2.68L deployed. Held > 12 months on the first two tranches → LTCG treatment on that portion; tranche 3 (~8 months) is STCG. STT+charges on the round trip are a few thousand rupees — immaterial next to the gain.

The trade paid because you (a) added into strength instead of averaging down, (b) never let total risk blow past ₹7,500-ish, and (c) *sat through* the dips.

## How pros do it / common mistakes

**Pros:**
- **Add to winners, never to losers.** Pyramiding up; averaging down is how retail turns a 5% loss into a 40% loss.
- **Trail on the higher timeframe.** Positional decisions on weekly closes, not intraday noise. Checking the position every hour guarantees you exit early.
- **Position size off volatility (ATR), not gut.** A ₹2,000 stock and a ₹200 stock get different share counts for the same rupee risk.
- **Let the LTCG clock work for you** — the 12-month mark is a *tax* reason to keep holding a healthy trend, not a reason to sell a broken one.

**Classic retail errors / red flags:**
- Booking winners at +8% "to be safe" while holding losers "till they recover."
- Pyramiding into a *falling* price and calling it "accumulating."
- Setting a tight 3% stop on a stock whose ATR is 4% — you'll be stopped out by normal noise before the trend even starts.
- Confusing a positional thesis with an intraday one and panic-selling on a red opening.
- Selling a great trend one month before 12 months and paying full STCG for no reason.

## Checklist / drill

**Before entering a positional trend trade:**
- [ ] Higher-timeframe (weekly) trend is up; price above rising 20-week EMA.
- [ ] Clear base/pivot breakout on above-average volume.
- [ ] Relative strength vs Nifty positive (stock outperforming the index).
- [ ] Stock is liquid (delivery-able size without impact); F&O availability a bonus for hedging.
- [ ] Risk per trade fixed (e.g., 1-1.5% of capital); share count = risk ÷ (entry − stop).
- [ ] Pyramiding plan written: add levels, and each add's stop keeps *total* risk bounded.
- [ ] Trail rule chosen in advance (weekly 20-EMA / 3×ATR chandelier / structure).

**Drill:** Pick 3 stocks in confirmed uptrends. On a weekly chart, mark the last 12 months' 20-EMA. Count how many times a weekly close below it would have exited you — and how much of the total move you'd have kept. This teaches you, viscerally, that fewer decisions capture bigger trends.

*Rules and rates cited are as of 2026 (Budget 2026 / FY2026-27). Verify current STT, settlement cycle, and tax treatment on NSE, your broker, and SEBI before trading — rules change.*
