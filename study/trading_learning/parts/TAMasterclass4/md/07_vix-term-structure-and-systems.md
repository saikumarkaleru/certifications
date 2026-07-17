# India VIX Term Structure & Volatility Systems

Most Indian retail traders treat India VIX as a single number they glance at on the NSE homepage — "VIX is 13, market is calm; VIX is 22, something is wrong." That is a first-grade reading of a doctorate-level instrument. Volatility is not one number. It is a *surface* — a structure that varies across strikes (the smile/skew) and across time (the term structure). The professionals who consistently extract money from options — the market-makers, the vol arb desks, the disciplined premium-sellers — trade the *shape* of that surface, not its level. This chapter builds the term-structure reading of India VIX into a decision system you can actually run on Nifty and Bank Nifty in 2026.

## What India VIX Actually Is, and Why the Term Structure Matters

India VIX is computed by NSE using the CBOE VIX methodology applied to Nifty option prices. It is a *model-free* estimate of the market's expected 30-day annualised volatility, derived by weighting a strip of near- and next-month out-of-the-money Nifty call and put prices. Two properties that retail traders routinely forget:

1. **VIX is forward-looking, not backward-looking.** It is *implied* volatility from option prices — the market's paid-for guess about the next 30 calendar days. It is not the realised volatility of the last month. Confusing the two is the single most common analytical error.
2. **VIX is a 30-day constant-maturity construct.** NSE interpolates between the near-month and next-month expiries to hold the horizon fixed at 30 days. So the headline VIX itself smooths over the expiry cycle — but the *raw* implied vols of individual expiries do not, and that is where the term structure lives.

The **volatility term structure** is the plot of implied volatility against time-to-expiry. Take the weekly Nifty expiries and the monthly, compute the at-the-money implied vol for each, and plot IV on the y-axis against days-to-expiry on the x-axis. The *slope* of that curve is the entire game.

- **Contango (upward slope):** near-term IV < far-term IV. This is the normal, "calm" regime. The market expects the immediate future to be quiet and prices a modest risk premium into longer expiries. Roughly 70-75% of trading days in a typical year sit in mild contango.
- **Backwardation (downward slope):** near-term IV > far-term IV. This is the "panic" regime. Something is happening *now* — a crash, an event, a gap — and the market pays up violently for immediate protection while assuming the storm passes. Backwardation is rarer, sharper, and far more tradeable.

The logic is insurance pricing. In calm times, insurance for next year costs more than insurance for next week (contango) because more can go wrong over a longer horizon. In a fire, insurance for *tonight* costs more than insurance for next year (backwardation) because the fire is now. Volatility behaves identically, and it *mean-reverts* — which is what makes the term structure a timing tool rather than just a thermometer.

## Construction and Reading: Building the Curve Yourself

You do not need a Bloomberg terminal. Here is the desk-grade method using the NSE option chain, which is free.

**Step 1 — Pick your maturities.** For Nifty in 2026 you have weekly expiries (Thursday) and the monthly. Take the current-week ATM, next-week ATM, and current-month and next-month ATM straddle-implied vols. NSE publishes IV per strike in the option chain; take the ATM call IV and ATM put IV and average them.

**Step 2 — Annualise consistently.** NSE already reports IV annualised. Just tabulate.

**Step 3 — Compute the slope metric.** The cleanest single number is the **VIX ratio** or **term-structure spread**:

$$\text{TS Spread} = \text{IV}_{\text{near week}} - \text{IV}_{\text{month+1}}$$

Or as a ratio: $\text{VRatio} = \text{IV}_{\text{near}} / \text{IV}_{\text{far}}$. A ratio above 1.0 = backwardation; below 1.0 = contango.

Here is an illustrative calm-day snapshot (numbers realistic for a quiet Nifty session):

| Maturity | Days to expiry | ATM IV (annualised) | Regime signal |
|---|---|---|---|
| Current week | 3 | 10.5% | anchor |
| Next week | 10 | 11.4% | contango |
| Current month | 17 | 12.1% | contango |
| Next month | 45 | 13.0% | contango |

VRatio (near/far) = 10.5 / 13.0 = **0.81** — healthy contango, calm regime. Now a panic-day snapshot (say, a global risk-off gap):

| Maturity | Days to expiry | ATM IV | Regime signal |
|---|---|---|---|
| Current week | 2 | 34.0% | anchor |
| Next week | 9 | 28.0% | backwardation |
| Current month | 16 | 24.5% | backwardation |
| Next month | 44 | 21.0% | backwardation |

VRatio = 34.0 / 21.0 = **1.62** — steep backwardation. The market is screaming *acute stress now, calming later*. Historically, steep backwardation in India VIX has been a far better contrarian *buy-the-index* signal than any oscillator, because it marks capitulation in the options market.

**Reading the level alongside the slope.** Combine two axes into a 2x2:

| | Contango (VRatio < 0.95) | Backwardation (VRatio > 1.05) |
|---|---|---|
| **Low VIX (<14)** | Grind-up regime. Sell premium cautiously, trend-follow. | Rare; early stress creeping in. Reduce size, watch. |
| **High VIX (>20)** | Elevated but structured fear. Premium selling pays, but size down. | Capitulation. Contrarian long index; long-dated premium sell setup. |

## Worked India Example: The Event Spike and the Roll

Consider a realistic 2026 sequence around a scheduled binary event — a Union Budget or an RBI policy or a national election result day. Say Nifty spot is 24,800 heading into the event.

**Three sessions before the event:** India VIX sits at 12.8. The weekly ATM IV is 11%, but the *event-week* expiry that captures the announcement shows ATM IV of 19%. This is the classic **event kink** — a single expiry sticking up out of an otherwise smooth curve because it straddles the binary. The curve is: week-1 (pre-event) 11%, event-week 19%, month 14%, month+1 13.5%. That kink is not a forecast that volatility will stay high; it is the market *pricing the jump* into precisely the expiry that contains it.

**The trade logic:** if you *buy* the event-week straddle, you are paying 19% IV for a move you hope exceeds the breakeven. But you are also exposed to the brutal **IV crush** — the moment the event passes, that event-week IV collapses from 19% toward the ambient 11-12%, and the straddle can lose 30-40% of its premium *even if the move goes your way modestly*. This is why naive event straddle buyers lose: they are right on direction and still lose on vega.

**The professional's version:** a **calendar spread** that sells the inflated event-week vol and buys the cheaper further-out vol — or simply staying flat vega and expressing direction through spreads (bull call / bear put) that are less vega-sensitive. On event morning, VIX might spike to 17 pre-result; the instant the result is digested by mid-morning, VIX collapses to 12 and the entire term structure flattens back to contango. A trader who *sold* the event straddle (defined-risk, via an iron condor or short strangle with wings) harvests the crush. Realistically most such sellers make money 6-7 times out of 10 and give a chunk back on the tail event — which is the honest arithmetic of premium selling and the reason position sizing, not the entry, decides whether you survive.

**The capitulation version:** now imagine the event disappoints and Nifty gaps down 3% over two sessions to 24,050. VIX rockets from 13 to 26. The term structure *inverts* into backwardation: current-week IV 31%, month+1 IV 20%. The mechanical, unemotional signal here is the contrarian one — steep backwardation plus a >2-standard-deviation VIX spike has historically marked short-term bottoms in Nifty. Not *the* bottom always, but a high-probability mean-reversion window. The system trade: initiate defined-risk bullish exposure (bull put spreads) *into* the fear, because you are selling now-expensive premium that will decay as VIX mean-reverts.

## How to Use It for Bias and Timing: The Volatility System

Turn the theory into rules. Here is a complete, honest volatility-regime system for Nifty/Bank Nifty options in 2026.

**Regime classification (run daily, EOD):**

1. Record India VIX close and its 20-day and 100-day averages.
2. Compute VRatio (near-week ATM IV / month+1 ATM IV).
3. Compute the **VIX percentile** — where today's VIX sits within its trailing 1-year range (0-100).

**Rule set:**

- **Premium-selling green light:** VIX percentile > 60 AND term structure in contango (VRatio < 0.97) AND VIX beginning to *fall* (today < yesterday, and below 5-day average). This is the sweet spot — fear is elevated (premium is fat) but structurally receding (the tide is going out). Deploy iron condors / short strangles on Nifty with wings, sized so max loss ≤ 1.5% of capital.
- **Premium-selling red light / buy-vol:** VIX percentile < 20 AND contango is flat-to-steep. Volatility is cheap and complacent. Selling premium here offers thin credit for fat tail risk. Either stand aside or *buy* cheap optionality (long calendars, long-dated strangles) as a lottery on a regime change.
- **Contrarian long-index:** VRatio > 1.15 (steep backwardation) AND VIX spiked > 2 SD in ≤ 3 sessions. Take defined-risk long via bull put spreads or long futures with a hard stop. This is a *mean-reversion* bet on vol, not a directional conviction call — treat it as such and take profit fast.
- **Trend-continuation caution:** persistent contango with rising VIX *level* (12 → 14 → 16 while still contango) often precedes a volatility-expansion breakout. Tighten stops on premium-selling; the calm is loading a spring.

**Bank Nifty overlay.** Bank Nifty has no separate published VIX, but it runs structurally *hotter* than Nifty — its ATM IV typically trades 3-6 vol points above Nifty's because banks are higher-beta and the index is more concentrated. Build a synthetic Bank Nifty VIX from its ATM straddle IV and apply the same term-structure logic. The backwardation signals fire harder and reverse faster on Bank Nifty; it is the more violent instrument, so halve your size relative to a Nifty equivalent.

**The volatility-of-volatility tell.** Watch how fast VIX itself moves. A VIX that *jumps* 20% intraday (say 14 → 17) but on a *green* Nifty day is a warning — someone is buying protection aggressively into strength, often smart money hedging. A VIX falling on a red day (Nifty down, VIX down) signals the selloff is orderly and likely near exhaustion. These divergences between price and VIX are among the highest-quality tells the term structure offers.

## Pitfalls

- **Confusing IV with realised vol.** VIX being "high" does not mean the market *will* be volatile — it means options are *priced* as if it will be. The edge in premium selling comes precisely from IV persistently exceeding subsequent realised vol (the variance risk premium). But when realised *exceeds* implied — during a genuine crash — sellers get destroyed. Never assume the premium is "free."
- **Selling into steep backwardation thinking it's high premium.** Backwardation means near-term premium is fat *because the fire is now*. Selling naked strangles into a crashing, backwardated market is how accounts blow up in a single session. The fat premium is fat for a reason. Contango-with-falling-VIX is the safe sell; backwardation is not.
- **Ignoring the event kink.** Placing a "cheap" calendar without noticing that your short leg is an event-week expiry inflated by a Budget/RBI/result means you misprice the whole trade. Always map expiries to the economic calendar.
- **Over-trusting the contrarian bottom signal.** Steep backwardation marks *most* short-term bottoms — but in a true regime break (2008, March 2020 style), VIX can stay backwardated and elevated for weeks while price grinds lower. Always use defined risk; the signal has real edge but is not a guarantee, and "most retail traders lose" applies hardest to those who bet the farm on a single mean-reversion.
- **Liquidity blindness.** Far-dated Nifty options and most Bank Nifty non-weekly strikes are thin. Your "term structure" IV from an illiquid strike may be a stale or wide-spread quote, not a real market. Use ATM strikes and check open interest and bid-ask before trusting the number.
- **Weekly-expiry distortion near expiry.** On expiry day, the current-week IV is nearly meaningless (gamma, not vega, dominates, and time value is tiny). Roll your "near" anchor to the next weekly once you are within a day of expiry, or the VRatio spikes for mechanical reasons unrelated to fear.

## Interview-Ready Summary

India VIX is a 30-day constant-maturity implied-volatility index derived from the Nifty option strip using the CBOE methodology — it is *forward-looking and model-free*, the market's paid-for estimate of future volatility, not a measure of past moves. The tradeable signal is not the level but the **term structure**: plot ATM implied vol against time-to-expiry. **Contango** (near < far, upward slope) is the calm, ~70% regime; **backwardation** (near > far, downward slope) is the panic regime. The key metrics are the VRatio (near-week IV / month+1 IV — above 1 is backwardation) and the VIX percentile within its one-year range. The professional system: **sell premium** when VIX percentile is high, structure is contango, and VIX is *falling* (fear receding, tide going out — the variance risk premium is being harvested); **go contrarian long the index** into steep backwardation with a >2-SD VIX spike (a mean-reversion bet, defined risk, quick profit); **buy cheap optionality** when VIX is in a low percentile and complacent. Bank Nifty runs 3-6 vol points hotter and reverses faster, so size down. The event kink — a single expiry inflated because it straddles a Budget, RBI policy, or election result — must be mapped to the economic calendar, and the IV crush after the event passes is where naive straddle buyers lose and disciplined defined-risk sellers earn. The honest caveats: implied is not realised, backwardation premium is fat for a reason (never sell naked into a fire), and the contrarian bottom signal has genuine edge but fails in true regime breaks — so defined risk and position sizing, not the entry, determine survival.
