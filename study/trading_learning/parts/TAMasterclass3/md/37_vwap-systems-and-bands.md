# VWAP Systems & Bands

The Volume-Weighted Average Price is the most important single line on an institutional trader's screen, and yet retail traders routinely misuse it as if it were just another moving average. It is not. VWAP is the day's *fair-value benchmark* — the price at which the average share or contract actually changed hands, weighted by size. Desks are measured against it. Algos are tuned to it. That is precisely why it works as a technical tool: when a reference is used by the people who move size, it becomes self-fulfilling support and resistance. This chapter builds VWAP correctly, adds standard-deviation and percentage bands to turn it into a complete mean-reversion-and-trend *system*, and works India examples on Nifty, Bank Nifty and cash stocks with entries, stops and targets in rupees. (Anchored VWAP — the discretionary cousin — gets its own dedicated chapter next.)

## What it is & the logic

A simple moving average treats every bar equally. VWAP does not: it weights every price by the volume that traded there, so a print of 50,000 shares moves the line far more than a print of 500. The result answers a question institutions genuinely care about: *what is the average price a participant paid today?*

The trading logic follows directly:

- A buyer whose average fill is **below VWAP** has beaten the day's benchmark; a buyer filled **above VWAP** has underperformed. Desks therefore lean to buy dips *toward or below* VWAP and sell rallies *above* it — which mechanically creates mean-reversion pressure toward the line.
- **Above VWAP = buyers in control** for the session; **below VWAP = sellers in control.** The line is a real-time proxy for who is winning.
- Because VWAP resets each session and accumulates volume through the day, it becomes *heavier and harder to move* as the session ages. A cross at 09:30 means little; a decisive reclaim of VWAP at 14:30 on heavy volume is a genuine shift.

VWAP without bands is only half a system. Price rarely sits *on* VWAP; it oscillates around it. The **bands** — standard-deviation or percentage envelopes — quantify how far is "far", converting VWAP from a single line into a statistical channel you can fade or ride.

## Construction, rules & settings

### The core formula

For each intraday period *i* with typical price *TP_i* = (High + Low + Close)/3 and volume *V_i*:

```
Cumulative TPV = Σ (TP_i × V_i)     [summed from session open]
Cumulative Vol = Σ (V_i)
VWAP           = Cumulative TPV / Cumulative Vol
```

The sums **reset at the session open** and accumulate through the day. That cumulative, resetting nature is what makes VWAP a *session* tool by default.

### Standard-deviation bands

The bands measure dispersion of price around VWAP, volume-weighted:

```
Variance = [ Σ V_i × (TP_i − VWAP)² ] / Σ V_i
StdDev   = √Variance
Upper Band k = VWAP + k × StdDev
Lower Band k = VWAP − k × StdDev
```

Typical multipliers: **±1σ, ±2σ, ±3σ**. Roughly speaking (and only roughly — intraday price is not normal), price spends most of its time inside ±1σ, and touches of ±2σ are the classic mean-reversion trigger. ±3σ is a genuine stretch — either a climax to fade or the signature of a strong trend day that has left mean-reversion behind.

### Percentage bands (an alternative)

Some traders prefer fixed percentage envelopes (VWAP ± 0.5%, ± 1%), which are easier to reason about across instruments of different volatility. On a ₹1,000 stock, a 1% band is ₹10; on Nifty at 24,000, 0.5% is 120 points. Percentage bands don't adapt to the day's volatility the way σ-bands do, so they are simpler but blunter.

### Key settings for Indian markets

| Setting | Recommendation | Why |
|---|---|---|
| Session anchor | Day session, reset 09:15 | Standard for NSE cash & futures |
| Bands | ±1, ±2, ±3 σ | Cover the practical fade/stretch range |
| Instrument for indices | Use futures for volume-true VWAP | Nifty/Bank Nifty spot has **no volume** |
| Timeframe | 1–5 min for intraday | Finer than 5-min just adds noise to bands |
| Cash stocks | Use the stock's own volume | Native, no proxy needed |

**India-critical caveat, again:** the Nifty and Bank Nifty *indices* have no volume, so charting-platform "VWAP" on the index is computed from a volume series that doesn't exist — treat it as unreliable and use the **futures** (or a liquid ETF/futures proxy) for a volume-true VWAP. On cash equities like Reliance, HDFC Bank or Tata Motors, VWAP is native and trustworthy.

## Worked India example (levels & ₹)

Take **Reliance Industries** on an intraday session. Suppose:
- Open 2,940, VWAP anchored at 09:15.
- By mid-morning VWAP has settled at **2,955**, with σ = 12.
- Bands: +1σ 2,967, +2σ 2,979, −1σ 2,943, −2σ 2,931.

**Trend-day read:** price opens at 2,940, dips to −1σ (2,943) at 09:35, is bought, reclaims VWAP by 09:50 and never closes back below it. Every subsequent pullback holds *above* VWAP. This is a **VWAP trend day up** — buyers defend the benchmark. The play is not to fade +2σ but to *buy pullbacks toward VWAP* and hold. A long from the 2,955 VWAP retest, stop under 2,943 (−1σ / the morning low), targeting +2σ 2,979 and beyond as the band expands, risks ₹12 to make ₹24+ — a clean 1:2. On 505-share equivalent sizing (Reliance F&O lot; confirm current lot on NSE), ₹24 captured ≈ **₹12,120** gross per lot.

**Mean-reversion read (different day):** a *balanced* session where VWAP is flat at 2,955 and price oscillates. Price spikes to **+2σ 2,979** on a news blip with a rejection wick. Short at 2,979, stop above +3σ (~2,991), target VWAP 2,955. Risk ₹12, reward ₹24 back to the mean. The −2σ touch is the mirror long.

The distinction between these two days is the *entire* game: on a trend day the bands are ride-with targets; on a balanced day the bands are fade-against triggers. You decide which regime you're in *before* you take a band trade — usually by asking whether price is holding one side of VWAP (trend) or crossing it repeatedly (balance).

**Bank Nifty band example:** VWAP (on futures) at 48,400, σ = 90. −1σ = 48,310, −2σ = 48,220. On a balanced day, a flush to −2σ 48,220 with a rejection candle is a long back to VWAP: 180 points × 15/lot = **₹2,700** gross, risking a stop below −3σ (~48,130), i.e. ~90 points = ₹1,350. 1:2.

## How to trade it (entry, stop, target, management)

### System A — VWAP mean-reversion (balanced/range days)

| Element | Rule |
|---|---|
| Regime filter | Price crossing VWAP repeatedly; flat VWAP; no clear trend |
| Entry | Fade a ±2σ touch that shows a rejection candle |
| Stop | Beyond ±3σ (the statistical stretch) |
| Target 1 | VWAP (the mean) |
| Target 2 | Opposite ±1σ, if momentum carries |
| Management | Take half at VWAP, trail the rest |

### System B — VWAP trend/pullback (trend days)

| Element | Rule |
|---|---|
| Regime filter | Price holds one side of VWAP; VWAP sloping; band expanding |
| Entry | Buy pullbacks into VWAP (or between VWAP and +1σ) in an uptrend; mirror for down |
| Stop | Beyond VWAP by a buffer, or below the prior swing / −1σ |
| Target | +2σ / +3σ, then trail with rising VWAP or a moving −1σ |
| Kill switch | Decisive close back across VWAP on volume = trend over |

### System C — VWAP reclaim/reject (regime-change signal)

The highest-value *event* is a late-session **reclaim** or **loss** of VWAP on heavy volume. Because VWAP is heavy by the afternoon, a 14:00+ reclaim of VWAP after a morning spent below it is a real shift, not noise. Enter on the reclaim, stop back below VWAP, target the day's high/prior value. This is the trade that catches the afternoon reversal.

**Sizing rule across all three:** risk a fixed rupee amount to the *structural* stop. Because σ (and therefore band width) changes intraday and across instruments, your point-stop changes — so your lot count must flex to keep rupee risk constant.

## Confluence

- **Value Area / POC (previous chapter):** when session VWAP sits inside the developing Value Area and both point the same way, you have two independent institutional references agreeing. VWAP crossing the POC is a meaningful confluence event.
- **Prior-day VWAP close & the open:** where price opens relative to yesterday's closing VWAP frames the day.
- **Round numbers & option strikes:** VWAP coinciding with a heavy-OI strike (say Bank Nifty VWAP at 48,500 where the 48,500 call/put OI is stacked) creates a magnet-plus-wall. Fades there are higher-probability.
- **Market breadth:** a VWAP trend day up in Nifty futures is far more trustworthy when advance-decline and the Nifty/Bank Nifty are both above their VWAPs — internal agreement.
- **Anchored VWAP (next chapter):** the *session* VWAP of this chapter plus an *event-anchored* VWAP from a prior swing low often bracket a trade beautifully — session VWAP for today's fair value, anchored VWAP for the swing context.

## Pitfalls

- **Using index VWAP.** The recurring India error: Nifty/Bank Nifty spot has no real volume, so index VWAP is unreliable. Use futures.
- **Fading a trend day.** The commonest way to be run over: shorting +2σ on a strong Open-Drive trend day. If price is holding above VWAP and the band is *expanding*, bands are ride-with targets, not fade triggers. Diagnose the regime first.
- **Trusting VWAP in the first 15 minutes.** With little cumulative volume, early VWAP is jumpy and its bands are wide and meaningless. Give it time to accumulate.
- **Confusing VWAP with a moving average.** VWAP resets daily and is volume-weighted; a 20-EMA is neither. Don't reason about one as if it were the other.
- **Ignoring liquidity.** On thin mid-caps or illiquid options, a few large prints distort VWAP and blow the bands out. VWAP is only as good as the volume feeding it.
- **σ-bands ≠ probability guarantees.** "±2σ contains 95%" is a normal-distribution statement; intraday returns are fat-tailed. A ±2σ touch is a *trigger to look*, not a promise of reversion.
- **Expiry-day gamma.** On weekly expiry, option gamma pins and whipsaws price around strikes; VWAP mean-reversion signals degrade. Trade smaller or stand aside.

## Interview-ready summary

VWAP is the volume-weighted average price of the session — the institutional fair-value benchmark against which desks are measured — computed as cumulative (typical price × volume) divided by cumulative volume, reset each open. Above VWAP, buyers control the session; below, sellers do; and because the line grows heavier through the day, late reclaims matter more than early ones. Standard-deviation bands (±1, ±2, ±3σ) turn the line into a statistical channel: on **balanced** days fade ±2σ touches back to the mean; on **trend** days ride pullbacks into VWAP toward the expanding far band — the single most important decision is diagnosing which regime you are in before taking any band trade. On Indian markets, always build VWAP on **futures** for the indices (spot has no volume) and native volume for cash stocks, size to a fixed rupee risk against structural stops, and stack VWAP with the Value Area/POC, option-OI strikes and breadth for confluence. Respect its limits: it is a session tool, not a moving average, its bands are triggers not guarantees, and expiry-day gamma degrades it.
