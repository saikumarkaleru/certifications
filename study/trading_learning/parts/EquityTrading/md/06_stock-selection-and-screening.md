# Stock Selection & Screening

## Why this matters — the pro vs retail gap this closes

Retail traders pick stocks the way they pick movies — a tip on a WhatsApp group, a stock "in the news," a name their uncle bought. Then they wonder why the position won't move, or gaps 15% against them on a result day, or can't be exited without a 2% slippage. The professional starts one level higher: *build a universe, filter it hard, and only then look at charts.* Selection is 80% of the outcome; a great pattern on an illiquid, low-relative-strength stock is a trap.

The gap this closes: retail confuses "a stock I like" with "a stock that fits my system." Pros run a repeatable **scan → shortlist → watchlist** funnel every day, so the chart work happens only on names that already passed liquidity, volatility, and strength filters. In an Indian market of ~2,000 tradeable names, your job is to throw away 1,960 of them fast.

## The essentials — India-specific filters

**1. Liquidity (the first, non-negotiable filter).** You must be able to enter and exit your size without moving the price.
- **Value traded:** prefer stocks doing **> ₹50 crore/day** turnover for swing size; **> ₹200 crore/day** if you trade large or intraday.
- **F&O universe (~180-200 names):** these are pre-vetted by NSE for liquidity and have lot-based futures/options for hedging. For most active traders, restricting to the **F&O list + Nifty 500** is a clean, safe universe.
- **Impact cost / spread:** on Kite or NSE, check the bid-ask. A 0.05% spread (e.g., ₹0.50 on a ₹1,000 stock) is fine; a ₹3 spread on a ₹300 stock is a red flag.
- **Avoid:** anything hitting frequent circuits, SME board names, and illiquid microcaps — a stop-loss is worthless if there's no buyer.

**2. Volatility (ATR) — is there enough movement to pay you?**
- **ATR%** = 14-day ATR ÷ price. A stock with ATR% of 0.8% barely moves; 2-4% is a healthy swing candidate; > 6% is a war zone that needs smaller size.
- ATR also *sizes* the position (shares = rupee-risk ÷ ATR-based stop) and sets realistic targets.

**3. Beta — how it moves vs the index.**
- **Beta > 1** (e.g., many PSU banks, metals, realty) amplifies Nifty moves — good in a strong trend, brutal in a reversal.
- **Beta < 1** (FMCG, pharma) is defensive. Match beta to your market-regime read (next chapter).

**4. Relative Strength (RS) vs Nifty — the money filter.**
- RS line = stock price ÷ Nifty. **Rising RS = the stock is outperforming the index.** In an uptrend you want the strongest RS names (leaders); in a downtrend, weak-RS names are your short/avoid list.
- A simple proxy: compare the stock's 3-month and 6-month return to Nifty's. Leaders beat the index; laggards don't.

**5. Sector strength.** Stocks move ~50% with their sector. Rank the NSE sectoral indices (Bank Nifty, Nifty IT, Nifty Auto, Nifty Pharma, Nifty Metal, Nifty PSE, etc.) by 1-month return and trade *leaders in leading sectors*. A great chart in the worst sector usually fails.

## Worked example — from scan to watchlist

**Goal:** a swing-long watchlist for the coming week. Capital ₹5,00,000, risk 1.5% (₹7,500) per trade.

**Step 1 — Universe.** Start with the **F&O + Nifty 500** list.

**Step 2 — Chartink scan (long swing).** Build a scan with these clauses:
- Daily close **> 50-DMA > 200-DMA** (uptrend structure).
- **Volume today > 1.5 × 20-day average volume** (participation).
- **Close within 3% of 20-day high** (breakout proximity).
- **Turnover > ₹50 crore** (liquidity — approximate via close × volume).

Say this returns **28 stocks**.

**Step 3 — Rank by relative strength & sector.** Cross-check each against Nifty's 1-month and 3-month return; keep only names beating Nifty on both. Rank the parent sectors; keep names in the **top-3 sectors** (say Auto and PSE are leading). This trims 28 → **9 names**.

**Step 4 — Volatility / tradeability sanity check** for each survivor:
- Stock A: ₹1,240, ATR ≈ ₹31 (ATR% 2.5%), turnover ₹310 cr, beta 1.2, RS rising. **Keep.**
- Stock B: ₹95, ATR% 6.5%, turnover ₹40 cr, frequent gaps. **Drop** (illiquid + too wild for size).
- …repeat.

**Step 5 — Final watchlist (5 names)** with pre-computed levels:

| Stock | Price | Entry trigger | Stop (≈1×ATR below) | Shares (₹7,500 risk) | Position value |
|---|---|---|---|---|---|
| A | ₹1,240 | > ₹1,255 | ₹1,209 (₹46 risk) | 163 | ₹2.02L |
| C | ₹640 | > ₹648 | ₹620 (₹28 risk) | 268 | ₹1.71L |
| D | ₹2,150 | > ₹2,180 | ₹2,095 (₹85 risk) | 88 | ₹1.89L |

Now you have a *plan*: exact triggers, stops, and sizes on 5 pre-vetted names — not a vague list of "stocks I'm watching."

## How pros do it / common mistakes

**Pros:**
- **Trade the leaders, not the laggards.** In a bull leg, buy the strongest-RS stock in the strongest sector, not the "cheap" one that "hasn't moved yet."
- **Let the scan do the rejecting.** They review 15-30 pre-filtered names in 10 minutes, not 500 charts.
- **Match instrument to size.** Big size → F&O-universe large caps; small size → can venture into midcaps with acceptable liquidity.
- **Re-run the sector ranking weekly** — leadership rotates (IT → PSU → pharma → capex).

**Retail errors / red flags:**
- Buying illiquid microcaps and SME names, then being unable to exit on bad news.
- Chasing "news" stocks after the move, at the top of a spike.
- Ignoring relative strength — buying a stock down 20% "because it's cheap" while the index rips.
- Same share count on a ₹150 stock and a ₹3,000 stock (no volatility-based sizing).
- One giant scan that returns 200 names and paralysis — no ranking, no shortlist.

## Checklist / drill

**Selection checklist (a stock must pass ALL):**
- [ ] In your defined universe (F&O + Nifty 500).
- [ ] Turnover > ₹50 cr/day (> ₹200 cr for large/intraday size).
- [ ] Tradeable spread / impact cost (checked on Kite/NSE).
- [ ] Trend structure aligned (e.g., 50-DMA > 200-DMA for longs).
- [ ] Relative strength vs Nifty positive on 1M and 3M.
- [ ] In a top-3 ranked sector.
- [ ] ATR% in your comfort band (≈ 2-4%); size computed from ATR.
- [ ] Entry trigger, stop, and share count written before market open.

**Drill:** Every evening for 10 trading days, run one Chartink scan and rank the sectoral indices. Force yourself to output exactly **5 names** with triggers/stops/sizes each night. After 10 days you'll have a repeatable funnel and a feel for how leadership rotates — the core professional habit this chapter installs.

*Filters, thresholds, and the F&O list are illustrative as of 2026. Verify current F&O eligibility, turnover, and lot sizes on NSE and your broker — the list and rules change.*
