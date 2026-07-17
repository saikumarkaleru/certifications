# Position-Sizing Systems (Deep)

Ask a hundred struggling traders what they need to fix and ninety-five will say "my entries." They are wrong. Entry quality — the exact tick where you buy — is the least important variable in the survival equation. The two variables that actually decide whether your account grows or dies are how much you lose when you are wrong and how many shares or lots you carry. The first is your stop. The second is your position size. This chapter is about the second, and it is the single most under-studied topic in retail trading because it involves arithmetic instead of pretty chart patterns, and arithmetic is not glamorous.

Here is the brutal truth that frames everything below: **you can be right 60% of the time and still blow up if your size is wrong, and you can be right 40% of the time and compound steadily if your size is right.** Position sizing is the bridge between "having an edge" and "keeping the money the edge produces." Most Indian retail F&O traders — 91% of whom lose money per SEBI's own 2024 study — never build that bridge. They trade one lot because that is what the margin allowed, or five lots because they felt confident, and they let account emotion, not a formula, decide their exposure.

## The principle: risk-per-trade is the master dial

Every sizing system, no matter how sophisticated, is ultimately a way to answer one question: *how many rupees am I willing to lose on this one trade if my stop is hit?* Call that number **R**. R is not your position value. R is not your margin. R is the distance from entry to stop, multiplied by your quantity. That is the only number that matters for survival.

The fixed-fractional rule says: **risk a constant small percentage of current equity on every trade.** The industry-standard band for that percentage is 0.5% to 2%. Below 0.5% your edge barely moves the needle and you get bored; above 2% a normal losing streak — which *will* come — can cripple you. Let us prove why with the mathematics of drawdown, because the number is more violent than intuition suggests.

The gambler's ruin arithmetic: suppose you risk a fixed fraction *f* per trade and hit a run of *n* consecutive losses. Your equity multiplies by (1 − f) each time, so after *n* losses you retain (1 − f)^n of capital. More important is the *recovery* asymmetry — after a drawdown of D%, the gain needed to get back to even is D / (1 − D), which is not symmetric:

| Drawdown | Gain needed to recover |
|---|---|
| 10% | 11.1% |
| 20% | 25.0% |
| 33% | 49.3% |
| 50% | 100% |
| 66% | 194% |
| 75% | 300% |

This table should be taped to your monitor. A 50% drawdown does not need a 50% gain to recover — it needs a 100% gain, a doubling. This is why deep drawdowns are near-fatal: they push the recovery requirement into a range your edge cannot realistically deliver before you quit in despair. The entire job of position sizing is to keep you on the top three rows of this table.

## The core system: fixed-fractional sizing, worked in rupees

The master formula, and you should burn it into memory:

> **Quantity = (Equity × Risk%) ÷ (Entry − Stop per unit)**

Then round *down* to the tradable lot/share increment. Never round up.

Let us run it on a real Indian cash-equity example. Your account is Rs 5,00,000. You risk 1% per trade, so R = Rs 5,000. You want to buy Tata Motors at Rs 940 with a stop at Rs 910 — the swing low below a base. Risk per share = 940 − 910 = Rs 30. Quantity = 5,000 ÷ 30 = 166.67, round down to **166 shares**. Position value = 166 × 940 = Rs 1,55,840, which is 31% of your account. Notice you are deploying a third of capital but only risking 1%. The stop, not the position value, controls the risk.

Now the same account, same 1% risk, a *tighter* setup: buy HDFC Bank at Rs 1,680 with a stop at Rs 1,665, a Rs 15 risk per share. Quantity = 5,000 ÷ 15 = 333 shares. Position value = 333 × 1,680 = Rs 5,59,440 — larger than your account, requiring margin/MTF. The tighter stop *let you carry a bigger position for the same rupee risk.* This is the mechanism most traders get exactly backwards: they size by conviction ("I love this trade, I'll go big") instead of by stop distance. A tight, well-defined stop is what earns you size — not a strong feeling.

## Sizing in F&O: the lot problem

Indian derivatives do not let you buy 166 units. You trade in fixed lots — Nifty 75, Bank Nifty 35, Reliance 500, and so on (exchange lot sizes are revised periodically, so always check the current NSE circular). This creates a granularity problem: sometimes the "correct" fractional size is 1.4 lots, and you cannot trade 1.4 lots.

Worked example, Bank Nifty futures. Account Rs 10,00,000, risk 1% = Rs 10,000. Lot size 35. You go long Bank Nifty futures at 52,000 with a stop at 51,700 — a 300-point stop. Risk per lot = 300 × 35 = Rs 10,500. Correct quantity = 10,000 ÷ 10,500 = 0.95 lots. You cannot trade 0.95 lots. You round *down* to **0 lots** — meaning this trade's stop is too wide for your account at 1% risk. Your honest choices are: (a) skip it, (b) find a tighter stop that still respects the chart, or (c) accept a marginally larger risk on a single lot if the stop is structurally sound.

If instead the stop were 150 points, risk per lot = 150 × 35 = Rs 5,250, correct quantity = 10,000 ÷ 5,250 = 1.9 lots → round down to **1 lot** risking Rs 5,250, or a deliberate 2 lots risking Rs 10,500 (1.05% — acceptable). The lot-size constraint is exactly why small accounts should not trade Bank Nifty futures: one lot's stop often exceeds a sane fraction of the account. Nifty futures (lot 75, but smaller point value per lot relative to Bank Nifty's volatility) or, better, defined-risk *option spreads* where the debit paid *is* your R, are far more size-friendly for accounts under Rs 5 lakh.

## Volatility-adjusted sizing: the ATR method

Fixed-fractional sizing off a chart stop is excellent, but it has a subtle flaw — where you put the stop is discretionary, and in choppy markets you may place it too tight and get whipsawed, or too wide and carry too little size. Volatility-based sizing removes that discretion by tying the stop to the instrument's *own* recent range using **Average True Range (ATR)**.

The method: set your stop at a multiple of ATR (commonly 1.5× to 3× ATR-14) below entry, then size so that this ATR-based risk equals your R. The formula becomes:

> **Quantity = (Equity × Risk%) ÷ (ATR × ATR-multiple × point value)**

Worked example. Nifty is at 24,800 with a daily ATR-14 of 220 points. You use a 2× ATR stop = 440 points, placing the stop at 24,360. Account Rs 8,00,000, risk 1% = Rs 8,000. Nifty lot 75, so risk per lot = 440 × 75 = Rs 33,000. Quantity = 8,000 ÷ 33,000 = 0.24 lots → 0 lots. Again the account is too small for a swing position in Nifty futures at 1% with a volatility-honest stop. This is not the method failing; it is the method *telling you the truth* — that your account cannot carry an index-futures swing at a sane risk level, information you would rather have before the trade than after.

The deep beauty of ATR sizing: it *automatically shrinks your size when volatility expands.* When India VIX spikes from 12 to 22, ATR roughly doubles, the denominator doubles, and your position size roughly halves — exactly the correct response to a more dangerous market, executed by formula rather than by fear. Fixed-lot traders do the opposite: they carry the same lots into a VIX spike and get carried out.

| India VIX regime | Nifty ATR-14 (approx) | Relative position size at fixed R |
|---|---|---|
| Calm (10–13) | 130–180 | 1.0× (baseline) |
| Normal (13–18) | 180–260 | 0.7× |
| Elevated (18–25) | 260–380 | 0.45× |
| Panic (25+) | 400+ | 0.3× or flat |

## The Kelly criterion — and why you should use a fraction of it

The Kelly formula answers a different question: not "how much can I afford to lose" but "what fraction *maximises long-run growth*?" For a two-outcome bet:

> **Kelly f = W − (1 − W) / R**

where W is win probability and R is the reward-to-risk ratio (average win ÷ average loss).

Example: your backtested breakout system wins 45% of the time (W = 0.45) with an average winner of 2.2R and average loser of 1R, so payoff ratio R = 2.2. Kelly f = 0.45 − 0.55/2.2 = 0.45 − 0.25 = **0.20**, i.e. 20% of equity per trade. Twenty percent. If you actually risked 20% per trade you would experience drawdowns of 60–70% routinely — mathematically "optimal" for growth but psychologically and practically suicidal, because your inputs (W and R) are *estimates* and if they are even slightly optimistic, full Kelly overbets into ruin.

The practical rule every serious desk uses: trade **quarter-Kelly to half-Kelly.** Half-Kelly captures ~75% of the growth rate with roughly half the volatility of drawdown. Quarter-Kelly here would be 5% — still aggressive. In practice, professional discretionary traders end up near the same 0.5–2% band that fixed-fractional prescribes, which is a reassuring convergence: Kelly, properly fractioned and stress-tested against estimation error, lands where prudence already lives. Use Kelly as a *sanity ceiling* — "am I risking more than fractional-Kelly allows?" — not as a target.

## Correlation: the hidden multiplier that kills accounts

Here is the mistake that turns disciplined 1%-per-trade traders into blow-up statistics: they take five 1% positions that are all secretly the *same* trade. Long Reliance, long HDFC Bank, long ICICI, long Infosys, long Nifty futures — five positions, "only 1% each," feels like 5% total risk. It is not. On a gap-down day when Nifty falls 2%, all five move together because they are all high-beta India-long. The effective risk is closer to a single 4–5% position.

The discipline: **budget risk by theme, not by ticker.** Set a portfolio heat limit — total open risk across all positions — of, say, 5–6% of equity, and count correlated positions as one. A useful working rule for Indian markets:

| Correlation cluster | Count toward heat as |
|---|---|
| Same stock, multiple entries | Fully additive (pyramiding — see next chapter) |
| Same sector (2+ PSU banks) | ~80% additive |
| Broad-market longs (index + large-cap basket) | ~70% additive |
| Uncorrelated (equity long + gold + a genuine short) | Additive at face value |

"Portfolio heat" is your true exposure. Compute it as the sum of all R across open trades, discounted for genuine diversification and *inflated* for hidden correlation. Cap it. When heat is at the cap, you take no new trade until an existing one moves its stop to breakeven and frees up risk budget.

## Scaling risk to conviction and to your equity curve

Two advanced refinements separate professionals from rule-followers.

**Conviction tiers.** Not every A-setup deserves the same risk as every C-setup. Define, in writing, a tiered risk schedule: A-grade setups (all your criteria align, clean structure, favourable regime) get 1.0%; B-grade get 0.6%; C-grade get 0.3% or a pass. The key word is *in writing* — decided before the emotion of the live trade, so "conviction" cannot be code for "I got excited."

**Equity-curve throttling.** Trade smaller when you are losing, larger when you are winning — but do it by rule, not by mood. A simple robust rule: if your account is below its own 20-day equity moving average, cut risk per trade in half until you climb back above it. This is a systematic circuit-breaker that pulls you out of the death-spiral where a losing streak meets full size. It respects the reality that losing streaks cluster (markets regime-shift, and your edge temporarily stops working), and it protects capital precisely when your read is worst.

## Building it into your routine: the pre-trade sizing card

None of this works as knowledge. It works only as a *habit* executed in the ninety seconds before you click buy. Build a physical or spreadsheet card and fill it in for every single trade — no exceptions, no "this one's obvious."

**Pre-trade sizing checklist:**
1. Current equity: Rs ______ (today's actual number, not last month's)
2. Risk % for this grade of setup: ____% → R = Rs ______
3. Entry price: ______
4. Stop price (structural — where the idea is *wrong*): ______
5. Risk per unit = Entry − Stop = ______
6. Raw quantity = R ÷ risk-per-unit = ______
7. Round DOWN to lot/share increment = ______
8. Position value = ______ ; % of equity = ____%
9. Current portfolio heat (open R + this R) = ____% — under the 6% cap? Y/N
10. If any answer is "N" or the rounded quantity is 0 → **skip or re-engineer the stop.** Do not fudge.

The traders who survive their first three years in Indian F&O are, almost without exception, the ones who fill in this card mechanically. The ones who blow up are the ones who "know all this" but size by feel. Knowing the formula is worthless; the discipline of *computing it every time* is the entire game.

## Pitfalls

- **Sizing by margin, not by stop.** "I have Rs 1.5 lakh margin, so I'll sell 3 lots" ignores the only question that matters — what you lose if wrong. Margin is a capacity constraint, never a sizing method.
- **Rounding up.** 1.9 lots is not 2 lots. Round down, always. The rounding-down bias is a free, permanent reduction in ruin probability.
- **Recomputing equity only on good days.** Update your equity base *down* after losses too, or fixed-fractional sizing silently becomes fixed-rupee sizing and loses its self-protecting property.
- **Ignoring gap risk in F&O.** Your stop protects you intraday; overnight gaps can blow through it. For overnight positions, size as if your stop could slip by an extra ATR — because on event nights it will.
- **Treating correlated positions as diversified.** The most common professional-looking way to blow up.
- **Full Kelly.** Mathematically optimal, practically fatal, because your edge estimates are never as good as you think.

## Interview-ready summary

Position sizing is the discipline of controlling *how much you lose when wrong*, not how much you make when right. The master formula is Quantity = (Equity × Risk%) ÷ (Entry − Stop), rounded down to the tradable increment, with risk held to 0.5–2% of current equity per trade. Volatility-adjusted (ATR) sizing ties the stop to the instrument's own range and automatically shrinks exposure when India VIX and ATR expand — the correct response to danger, executed by formula. Kelly defines the growth-maximising fraction but must be cut to a quarter or half because edge estimates are noisy and full Kelly courts ruin; fractioned Kelly conveniently lands in the same 0.5–2% band as prudence. Correlation is the hidden multiplier: five "1% each" India-long positions are really one 4–5% position, so budget risk by theme and cap total portfolio heat near 5–6%. The recovery-asymmetry table (a 50% loss needs a 100% gain) is the reason drawdown control outranks entry precision. The system only works as a ninety-second pre-trade card filled in mechanically every time — the edge is not the formula, it is the habit of computing it.
