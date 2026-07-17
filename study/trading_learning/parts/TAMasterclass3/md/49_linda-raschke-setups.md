# Linda Raschke Setups

Linda Bradford Raschke is one of the most respected discretionary short-term traders of the modern era — a market maker turned fund manager, co-author with Laurence Connors of *Street Smarts* (1995), a book that quietly became a bible of mechanical-yet-discretionary swing setups. Her genius is a small library of named, repeatable patterns built on two ideas: markets alternate between *contraction and expansion* (quiet begets volatile, volatile begets quiet), and *momentum precedes price* (a thrust in momentum leads to a later price extreme). Her setups — the **Turtle Soup**, **80-20's**, **Holy Grail**, **Anti**, **3-10 Oscillator momentum divergence**, and the **NR7/contraction breakouts** — are precise enough to backtest yet flexible enough for a discretionary trader. This chapter ports the most useful ones to Nifty, Bank Nifty, and NSE stocks, with exact rules, worked rupee examples, and honest edge notes.

Raschke's setups are largely *daily-bar swing* setups (their original home), but most translate cleanly to intraday 5- and 15-minute charts, which is how Indian traders will mostly deploy them. We flag the time frame for each.

## Origin and the core ideas

Two engines drive everything Raschke does.

**1. Contraction–expansion cycles.** Volatility is not constant; it oscillates. A series of narrowing ranges (contraction) stores energy that releases as a large expansion move, and after a big expansion the market rests. This is the basis of NR7 (narrowest range of 7 days) and inside-day breakouts: you position *during* the quiet for the coming storm. It is the same insight Bollinger encoded as "the squeeze," but Raschke traded it years earlier off raw range.

**2. Momentum precedes price.** Using her favourite indicator, the **3-10 oscillator** (a MACD variant: the difference between a 3-period and 10-period simple moving average, with a 16-period SMA of that difference as the "slow line"), she observes that momentum peaks *before* price. So a fresh momentum high after a pullback implies price has more to go, and a momentum divergence at a new price high warns of exhaustion. This drives the Anti and the divergence setups.

A third, tactical idea underlies **Turtle Soup and 80-20's**: *most breakouts of obvious levels fail*, and fading a failed breakout back into the prior range is a high-probability, tight-stop trade — the mirror image of Brooks' "breakouts usually fail."

## Setup 1 — Turtle Soup (fading the failed 20-day breakout)

The name mocks the "Turtles" who bought 20-day breakouts. Raschke's data said most 20-day breakouts fail, so she fades them.

**Rules (long side, daily bars):**

| Element | Rule |
|---|---|
| Universe | Liquid index/stock; original was futures |
| Setup | Today makes a **new 20-day low**, and the prior 20-day low was **at least 4 trading days ago** |
| Entry | Buy-stop 1–2 ticks **above** the prior 20-day low as price re-enters the range (the breakout is failing) |
| Stop | Below today's low |
| Target | Prior swing high / first target 1R, trail the rest; often exit in 1–3 days |
| Filter | Skip if the prior 20-day low was 1–3 days ago (too recent, structure too fresh) |

The short side ("Turtle Soup Plus One" takes the signal a day later) mirrors it at new 20-day highs.

**Worked India example (Nifty daily):** Suppose Nifty has a 20-day low at 24,050 set 9 sessions ago. Today it spikes down to 24,010 (new 20-day low) on a scary headline, then reverses intraday. Place a buy-stop at 24,055 (just above the old 20-day low). If tomorrow (or later today) price trades back above 24,055, you're long a failed breakdown. Stop below today's low 24,010 (45-point risk). If Nifty rallies to the prior swing 24,300 over two days, that's ~245 points, ~5R. The logic: the new low sucked in breakout sellers and stops; when it fails, those shorts must cover, fuelling the bounce.

**Edge notes:** In *Street Smarts*, Turtle Soup showed a high win rate (60%+) with small stops on futures. On Nifty it works best when the false breakout coincides with a support cluster, oversold breadth, or a high-OI put strike, and worst in genuine trend-acceleration regimes (a real breakdown in a bear market keeps going). It is a *counter-trend, mean-reversion* trade — size modestly and honour the stop.

## Setup 2 — 80-20's (open in one extreme, close in the other)

Built from a Toby Crabel observation: when a day opens in the top 20% of the prior day's range but closes in the bottom 20% (or vice-versa), the reversal tends to continue the next day.

**Rules (daily bars, long version):**
- Yesterday closed in its **top 20%** and opened in its **bottom 20%** of range? Not quite — the canonical bullish 80-20 buy: yesterday **opened in top 20%** and **closed in bottom 20%** (a strong down day that overshot), then today take a buy-stop above yesterday's *low + a small offset*, anticipating a snap-back.
- Entry: buy-stop as price retraces back up through yesterday's lower range.
- Stop: below today's low.
- Target: yesterday's midpoint or high; 1–2 day hold.

**Worked (an NSE stock, daily):** Say Reliance opens at ₹2,955 (near the day's high of ₹2,960) and, on a weak market, sells off to close at ₹2,905 (near the low ₹2,900) — an 80-20 down day. The next morning, place a buy-stop at ~₹2,912. If it triggers, you're fading the overshoot; stop below ₹2,900, target the prior midpoint ~₹2,930+. The read: a day that opens strong and closes weak often over-extends and mean-reverts.

**Edge notes:** 80-20's are a volatility mean-reversion tell. On Indian single stocks they interact with delivery-based selling and news; use them as a *bias*, confirmed by a reversal bar or a 3-10 momentum turn, not blindly.

## Setup 3 — The Holy Grail (ADX + 20-EMA pullback)

Raschke's most famous *trend-continuation* setup, and the antidote to the two mean-reversion setups above.

**Rules:**
| Element | Rule |
|---|---|
| Trend filter | **ADX(14) > 30** (a strong trend exists) |
| Setup | Price pulls back to the **20-period EMA** for the first time after a strong thrust |
| Entry | Buy (in an uptrend) as price turns back up off the EMA — a buy-stop above the prior bar's high |
| Stop | Below the pullback low / below the EMA |
| Target | Retest of the recent high; trail for a new high |
| Mirror | Short pullbacks to the EMA in strong downtrends (ADX>30) |

The name is tongue-in-cheek, but the setup encodes a real edge: strong trends (high ADX) resume after the *first* shallow pullback to the mean.

**Worked (Bank Nifty 15-minute):** Bank Nifty is trending hard up intraday, ADX(14) reads 34. It rallies to 52,300, then pulls back for the first time to the 20-EMA at 52,180, printing a small reversal bar. Buy-stop above that bar at 52,205; stop below the pullback low 52,160 (≈45 pts). Target the prior high 52,300 first, then trail for a measured extension to ~52,420. The high ADX is your permission slip to trade *with* the trend rather than fade it — the exact opposite mindset to Turtle Soup, which is why knowing *which regime you're in* is everything.

**Edge notes:** The Holy Grail's win rate is strong precisely because the ADX>30 filter refuses to trade in ranges. Most failures come from taking it on the *second or third* pullback (the trend is tiring) or when ADX is really 20–25 and you fudged it.

## Setup 4 — The Anti (trading with the trend after a counter-trend pause)

The Anti uses the 3-10 oscillator to enter a trend-resumption. In an uptrend, the oscillator pulls back (a small counter-trend hook down) while price merely consolidates; when the oscillator hooks back up, you buy the resumption. It is "anti" the small counter-move — you fade the pause, not the trend.

**Rules (uptrend long):**
- Trend up; the 3-10 fast line makes a series of higher highs, then hooks down for 2–3 bars (a pause, not a reversal — price holds).
- Entry: buy when the fast line turns back up (or price takes out the prior bar's high).
- Stop: below the pause low.
- Target: a new price high / prior momentum high.

**Worked (Nifty 5-minute):** Nifty trends up; the 3-10 oscillator peaks, then hooks down for three bars while price only drifts sideways from 24,360 to 24,345 (shallow — momentum cooled but price didn't break). When the 3-10 curls up and Nifty trades above 24,362, go long; stop 24,338; target a new high 24,390+. The Anti captures the second thrust of a two-legged momentum move — closely related to Brooks' H2.

**Edge notes:** The Anti is a momentum-continuation pattern; it fails when the "pause" is actually a top (price breaks down with the oscillator). Confirm price is holding, not breaking, during the momentum hook.

## Setup 5 — NR7 and contraction breakouts

Pure contraction–expansion. **NR7** = today's range is the **narrowest of the last 7 days**. An inside day (**ID**) is one whose range is inside yesterday's. An **NR7 that is also an inside day (ID/NR7)** is the tightest coil of all.

**Rules:**
- Identify an NR7 (or ID/NR7).
- Place a buy-stop above its high and a sell-stop below its low (bracket order).
- Whichever triggers, that's the direction; stop at the opposite end (or a fraction of it).
- Target: a measured move / the recent swing; expansion days often run.

**Worked (an NSE stock, daily):** Say Infosys prints an NR7 with high ₹1,530 and low ₹1,512 after a quiet session. Bracket: buy-stop ₹1,532, sell-stop ₹1,510. Next day it gaps and drives through ₹1,532 — long, stop ₹1,514 (or ₹1,522 for a tighter version), target a range-expansion move to ₹1,560+. The contraction stored energy; the breakout released it.

**Edge notes:** Works best after a multi-day contraction *cluster* (several NR days in a row) and near a decision level. On Nifty/Bank Nifty, an NR7 the day *before* a known event (RBI policy, budget, expiry, Fed) is a coiled spring — but beware whipsaw gaps that hit both brackets.

## Setup 6 — 3-10 Oscillator momentum divergence

At the end of a trend, price makes a new extreme but the 3-10 fast line does not — a **divergence**, warning of exhaustion. Raschke uses it not as a standalone reversal trigger but as a *heads-up* to tighten stops and look for a reversal setup (a Turtle Soup, an 80-20, a reversal bar).

**Worked:** Bank Nifty pushes to a new intraday high 52,450, but the 3-10 fast line prints a lower high than at the 52,400 peak — momentum diverged. Raschke wouldn't short blindly; she'd wait for a confirming trigger (a failed breakout above 52,450 → a Turtle-Soup-style short, or an 80-20 reversal bar). Divergence sets the bias; a setup gives the entry.

## Backtest, edge, and realistic costs (India)

Honest accounting:

- **Win rates:** Turtle Soup and 80-20's historically 55–65% with small stops; Holy Grail high win rate *only* with the ADX>30 filter; NR7 breakouts ~50% but with expansion payoff (>2R) that carries the expectancy.
- **Costs on NSE:** Intraday equity/F&O costs stack up — brokerage, STT (notably on the sell side and heavy on options), exchange fees, GST, stamp duty, SEBI turnover. A Bank Nifty options scalp can lose 8–15 points to round-trip costs; index-futures costs are lighter but real. Every backtest must subtract these or the edge is illusory.
- **Slippage:** stop-entry orders in fast markets (news, expiry) slip; model 1–3 ticks on Nifty, more on Bank Nifty and thin stocks.
- **Regime dependence:** the mean-reversion setups (Turtle Soup, 80-20) bleed in strong trends; the trend setups (Holy Grail, Anti) bleed in ranges. A regime filter (ADX, or simply "is the market trending or ranging?") is non-negotiable — it decides *which half of the library you deploy today*.

## Adaptations for NSE / F&O

- **Express risk in rupees, not points.** Bank Nifty's point value dwarfs Nifty's; size to a fixed % of capital per trade.
- **Trade the setup on the index, express via options with care.** A Holy Grail long on Bank Nifty is cleaner in futures than in options, where theta and IV crush distort the R:R; if using options, prefer slightly ITM/ATM and short holding periods.
- **OI and VWAP confluence.** A Turtle Soup long that fails right at the highest-OI put strike, or a Holy Grail pullback that holds VWAP, is materially stronger.
- **Event awareness.** NR7 before RBI/budget/expiry is a premium contraction setup, but gap risk is real — bracket with defined risk and accept that both sides can trigger.

## Pitfalls

- **Deploying the wrong half of the library for the regime** — fading breakouts in a trend, or buying pullbacks in a range. The regime read comes first.
- **Ignoring the "days-ago" filter on Turtle Soup** — a too-recent prior extreme means the structure isn't a genuine failed breakout.
- **Fudging the ADX threshold on the Holy Grail** — below ~30 it's not a strong-enough trend and the pullback keeps going.
- **Trading divergence as a trigger** rather than a heads-up — divergence can persist for many bars in a strong trend.
- **Under-costing options** — a "profitable" scalp system can be net-negative after STT and spreads.
- **Both brackets filling on NR7 event days** — whipsaw eats the edge; either skip the riskiest events or halve size.
- **Over-holding mean-reversion trades** — Turtle Soup and 80-20 are 1–3 day (or intraday) snapbacks, not position trades; take the reversion and leave.

## Interview-ready summary

Linda Raschke's setup library rests on two pillars — volatility alternates between contraction and expansion, and momentum precedes price — plus the tactical truth that most obvious breakouts fail. The library splits cleanly by regime. **Mean-reversion:** *Turtle Soup* fades a failed 20-day breakout (with a "prior extreme ≥4 days ago" filter), and *80-20's* fade a day that opens in one extreme and closes in the other. **Trend-continuation:** the *Holy Grail* buys the first pullback to the 20-EMA only when ADX>30, and the *Anti* buys the resumption after a shallow 3-10 oscillator hook against an intact trend. **Contraction breakout:** *NR7 / inside-day* brackets position during the quiet for the coming expansion. The *3-10 oscillator divergence* is a heads-up for exhaustion, not a standalone trigger. Each has exact rules — entry on a stop beyond a defined level, stop at the structure's opposite end, targets of 1R plus a trailed runner or measured move. Ported to India, they demand rupee-based sizing, VWAP/OI confluence, honest deduction of STT and slippage, and above all a regime filter that decides which half of the library you trade today. The discipline that ties it together is Raschke's own: know whether the market is contracting or expanding, trending or ranging, and deploy the matching setup — never the opposite one.
