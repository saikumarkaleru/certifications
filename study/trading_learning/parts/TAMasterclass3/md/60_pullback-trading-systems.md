# Pullback Trading Systems

A pullback is the market's most generous gift to a trend follower: a temporary counter-move against an established trend that lets you enter at a better price, with a tighter stop, in the direction that has the wind at its back. Volume III of this masterclass has already established the raw materials — trend structure, moving averages, Fibonacci, and volatility. This chapter welds them into complete, rule-based *systems* you can run mechanically on Nifty 50, Bank Nifty, and NSE cash stocks. We do not re-teach what a higher-high is; we build machines that trade the dip.

## What it is and the logic

Trends do not travel in straight lines. Price advances in impulse legs, then pauses or retraces as early buyers book profit and late buyers hesitate, before the dominant force reasserts itself. A pullback system exploits three durable edges:

1. **Location edge.** Buying a shallow dip in an uptrend gives you a stop that sits just below recent structure — a small, well-defined risk — while the target rides the resumption of trend. Reward-to-risk expands mechanically because you are not chasing.

2. **Behavioural edge.** Pullbacks flush weak longs and tempt shorts. When the trend resumes, those shorts must cover, adding fuel. In Indian index futures this shows up as sharp V-shaped recoveries around VWAP or the 20-EMA.

3. **Selection edge.** The requirement that a *trend must already exist* filters out chop. You only trade instruments that have proven directional intent, which is where trend-following expectancy actually lives.

The counter-intuitive truth: pullback systems typically win *less* than half the time on individual signals if targets are ambitious, yet remain profitable because winners are multiples of losers. The discipline is not prediction — it is buying strength on weakness and letting asymmetry compound.

A pullback is distinct from a **reversal** (where the trend ends) and a **breakout** (where you enter on strength as price exits a range). The pullback trader deliberately sacrifices the breakout entry to get a lower-risk fill, accepting that some trends run away without ever offering a dip.

## Construction, rules and settings

We will define three complementary systems. Each is fully mechanical so it can be coded in Pine Script on TradingView or scanned on Chartink.

### System A — The 20-EMA Trend Pullback (swing, NSE stocks)

The workhorse. Trade only *with* the daily trend, buy the first controlled dip to the rising 20-EMA.

| Component | Rule |
|---|---|
| Universe | NSE F&O stocks + Nifty 500, price > ₹100, 20-day avg turnover > ₹50 cr |
| Trend filter | Close > 50-EMA **and** 50-EMA > 200-EMA (stage-2 uptrend) |
| Trigger | Price pulls back to touch/undercut 20-EMA, then closes back above it (a "reclaim" bar) |
| Confirmation | Reclaim bar closes in upper 50% of its range; volume not climactic |
| Entry | Buy next day above reclaim-bar high |
| Stop | Below reclaim-bar low, or 1.5× ATR(14) below entry — whichever is tighter but never < swing low |
| Target 1 | Prior swing high (book 50%) |
| Target 2 | Trail remainder under rising 10-EMA on daily close |
| Sizing | Risk 0.75–1.0% of capital per trade |

### System B — The Fibonacci 50–61.8% Pullback (index & stock swing)

Uses the impulse leg itself to define the buy zone.

| Component | Rule |
|---|---|
| Setup | Identify a clean impulse leg making a fresh 20-day high |
| Buy zone | 50%–61.8% retracement of that leg |
| Trend filter | The 61.8% level must still sit above the 50-EMA |
| Trigger | Bullish candle (hammer, bullish engulfing, or 2-bar reversal) inside the zone |
| Entry | Above trigger-candle high |
| Stop | Below 78.6% retracement of the impulse leg |
| Target | 1.272–1.618 extension of the impulse leg |
| Invalidation | A close below the impulse leg's origin cancels the setup entirely |

### System C — The Intraday VWAP Pullback (Bank Nifty / Nifty futures)

Session-scoped, for the 09:15–15:30 tape.

| Component | Rule |
|---|---|
| Instrument | Bank Nifty / Nifty futures, 5-min chart |
| Trend filter | After 09:45, price holding above VWAP and rising 20-EMA(5m); ADX(14) > 20 |
| Trigger | Pullback to VWAP or the 20-EMA that does *not* close below VWAP for two bars |
| Entry | Break of the pullback-bar high |
| Stop | Below the pullback low / below VWAP (whichever gives ≤ 0.4% risk on Bank Nifty) |
| Target | Prior swing high; trail the rest under the 20-EMA |
| Time stop | Exit any trade not moving by 20 minutes; flatten before 15:15 |
| No-trade filter | Skip the first 30 min and RBI-policy/expiry-open spikes |

**Shared classification of pullback quality.** Grade every dip A/B/C before acting:

- **A-grade:** shallow (to 20-EMA / 38.2–50% Fib), declining volume into the dip, tight bars. Highest win rate.
- **B-grade:** deeper (to 50-EMA / 61.8%), one wide-range down bar. Tradeable with confirmation only.
- **C-grade:** below 50-EMA, expanding volume, gap-downs — this is a *reversal risk*, not a pullback. No trade.

Falling volume during the retracement is the single most reliable tell that the dip is corrective rather than distributive — it says sellers lack conviction.

## Worked India example (levels and ₹)

**Trade: RELIANCE, System A (20-EMA Trend Pullback).**

Assume Reliance is in a clean daily uptrend: 50-EMA at ₹1,240 rising, 200-EMA at ₹1,150, price recently printed a swing high at ₹1,340 before drifting. Over five sessions it pulls back on *declining* volume to the 20-EMA at ₹1,282, undercutting to an intraday low of ₹1,276, then closing at ₹1,296 — a reclaim bar in the upper third of its range. This is a textbook A-grade dip.

- **Entry trigger:** next-day break above reclaim-bar high of ₹1,300. Filled at **₹1,301**.
- **Stop:** below reclaim-bar low ₹1,276 → place at **₹1,272** (risk = ₹29/share ≈ 2.2%).
- **Position size:** capital ₹10,00,000, risk 0.75% = ₹7,500. Shares = 7,500 / 29 ≈ **258 shares** (round to lot logic if trading futures).
- **Target 1:** prior swing high ₹1,340. Book 50% (129 shares) → +₹39/share on that tranche.
- **Target 2:** trail under rising 10-EMA. Suppose trend extends to ₹1,395 before a daily close breaks the 10-EMA at ₹1,372, exiting the remainder there → +₹71/share.

**P&L:** Tranche 1: 129 × 39 = ₹5,031. Tranche 2: 129 × 71 = ₹9,159. Gross ≈ **₹14,190** on ₹7,500 risk — a blended **1.9R** win. Had the stop hit instead, the loss is a clean −₹7,500 (−0.75R after the 258/259 rounding). Costs (brokerage, STT, exchange, GST, stamp) on a ₹3.4 lakh notional round trip run roughly ₹250–400 with a discount broker — material but not decisive at swing frequency.

**Contrast — a C-grade trap to refuse.** If instead Reliance had *gapped down* below the 50-EMA at ₹1,240 on 3× average volume after a bad earnings print, the "dip to support" is not a pullback — it is the market repricing. System rules (close < 50-EMA, expanding volume) block the trade. Sitting out is the winning move; this is exactly where discretionary pullback traders bleed.

## How to trade it — entry, stop, target, management

**Entry mechanics.** Never buy while price is still falling. Every system here uses a *trigger* — a break above the high of a confirming bar — so you are entering on evidence the dip is over, not catching a knife. On indices intraday, use a 1–2 point buffer above the trigger to avoid stop-run wicks.

**Stop placement.** The stop must live where the *thesis is wrong*, not at an arbitrary rupee amount. For a 20-EMA pullback, a close back below the reclaim-bar low says buyers failed. Use ATR to avoid stops that are structurally too tight in a volatile name — but never widen a stop beyond the invalidation swing just to "give it room." Size down instead.

**Scaling and targets.** Booking half at the prior swing high does two things: it locks a real gain that funds the psychological patience to trail the rest, and it converts the trade to risk-free once the stop moves to breakeven on the runner. The trail (10-EMA on swings, 20-EMA(5m) intraday) is deliberately loose enough to survive noise but tight enough to protect a trend that stalls.

**Trade management rules that separate winners:**

- Move stop to breakeven once Target 1 fills. From that point the trade cannot hurt you.
- Never average down a losing pullback — a failing pullback is a failing thesis.
- Honour the time stop intraday. A pullback that does not resume within ~20 minutes is telling you the trend has lost urgency; capital sitting in a stalled trade is capital not compounding.
- If a fresh, cleaner A-grade setup appears while you hold a stalled B-grade, rotate.

## Confluence

Pullback signals become high-probability when independent methods point at the *same price*:

- **EMA + Fibonacci overlap:** the 20-EMA sitting inside the 50–61.8% retracement zone creates a magnet — System A and System B agreeing. These are the highest-expectancy dips.
- **Round numbers & prior structure:** Nifty pulling back to 24,500 where the 50% retracement, the rising 20-EMA, and a prior breakout shelf coincide.
- **VWAP anchored to the swing origin** intraday, aligning with a moving-average pullback.
- **Options data:** a dip into a strike with heavy Put open interest (a "Put wall") on Bank Nifty adds a structural floor; option writers defending that strike often produce the very bounce you are trading. Rising PCR at a support confluence strengthens the long.
- **Breadth:** in an index pullback, if advance-decline holds up while price dips, the correction is orderly — a green light.

Demand at least two independent confluences for A-grade sizing; a lone EMA touch is a B-grade at best.

## Pitfalls

- **Catching the falling knife.** Entering *during* the pullback instead of on the trigger. Every rule here forbids it; discretion erodes it. The reclaim/trigger bar is non-negotiable.
- **No trend, just chop.** Pullback logic applied to a rangebound instrument prints endless small losses. The stage-2 / ADX filters exist precisely to keep you out. If the 50-EMA is flat, there is no trend to pull back *to*.
- **Pullback vs reversal confusion.** Deep retracements on expanding volume, gap-downs through moving averages, and breaks of the impulse origin are reversals wearing a pullback's clothes. The volume-declining requirement and the 78.6% / origin invalidation guard this.
- **Over-tight stops in volatile names.** A ₹5 stop on a stock that swings ₹40 intraday is a donation. ATR-scale the stop and reduce size.
- **Ignoring costs and gaps on swings.** Overnight gap risk is real on single stocks around results; size for it and avoid holding pullbacks into known events.
- **Revenge re-entry.** After a stop-out, waiting for a *fresh* qualifying setup — not immediately re-buying the same dip — is what preserves the statistical edge.
- **Curve-fitting the parameters.** Do not tune the EMA from 20 to 17 because it looked better on the last three trades. Robust pullback edges survive small parameter changes; fragile ones vanish out of sample.

## Interview-ready summary

A pullback system buys a temporary counter-trend dip *in the direction of an established trend*, capturing a location edge (tight, structurally-defined stop) and a behavioural edge (weak hands flushed, shorts trapped) to produce positive expectancy through reward-to-risk asymmetry rather than high hit-rate. The three canonical builds are the **20-EMA trend pullback** (swing, reclaim-bar trigger), the **50–61.8% Fibonacci pullback** (impulse-leg zone with a candlestick trigger), and the **intraday VWAP pullback** on Bank Nifty/Nifty futures. Non-negotiables: a real trend filter (50-EMA > 200-EMA, or ADX > 20), entry only on a trigger above a confirming bar, a stop at the invalidation point, booking part at the prior swing high, and trailing the rest under a fast EMA. The defining discipline is refusing C-grade "dips" — deep, high-volume, gap-driven declines — which are reversals, not pullbacks. Expect a sub-50% win rate on ambitious targets, made profitable by winners worth 1.5–3R and by the ruthless filtering of non-trending, low-quality setups.
