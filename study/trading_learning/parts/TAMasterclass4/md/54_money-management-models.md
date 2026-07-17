# Money-Management Models

Money management is the part of trading that decides whether your edge ever reaches your bank account. You can read charts brilliantly, time entries to the tick, and still go to zero — because position sizing, not signal quality, is what determines the *shape* of your equity curve and whether you survive the inevitable losing streak. This chapter is a working library of sizing models: fixed-fractional, fixed-ratio, Kelly and fractional-Kelly, volatility-parity (ATR) sizing, the martingale/anti-martingale family, and portfolio-heat budgeting. Everything is framed for an Indian retail/HNI trader working with rupees, NSE cash, F&O lots, and MCX contracts.

The honest premise up front: most retail traders lose, and the largest single reason is not bad analysis — it is oversizing. A trader with a genuine 55% win-rate edge can still blow up if he bets 20% of capital per trade, because the variance of outcomes will hand him a drawdown deep enough to force capitulation or a margin call. Money management is how you convert a fragile edge into a durable business.

## The principle: geometric growth punishes big losses asymmetrically

Trading returns compound *multiplicatively*, not additively. That single fact drives everything.

If you lose 50% of capital, you need +100% to get back to even. Lose 20%, you need +25%. Lose 10%, you need +11.1%. The recovery burden accelerates viciously as drawdowns deepen. So the goal of every sizing model below is the same: **keep the per-trade and portfolio drawdowns small enough that the geometric drag stays manageable and the emotional pressure stays survivable.**

| Drawdown | Gain needed to recover |
|---|---|
| −5% | +5.3% |
| −10% | +11.1% |
| −20% | +25.0% |
| −33% | +49.3% |
| −50% | +100% |
| −75% | +300% |
| −90% | +900% |

The table is not a scare tactic; it is the actual arithmetic your account obeys. A trader who caps any single loss at 1% of capital would need 50 consecutive full-stop losses to reach a −50% drawdown (before compounding math softens it). A trader risking 10% reaches −50% in roughly seven losses. Seven losing trades in a row is *ordinary* — even a 55%-win system throws a 7-loss streak fairly often over a few hundred trades.

## Model 1 — Fixed-fractional (percent-risk) sizing

This is the default professional model and the one I recommend for 90% of Indian retail traders. You risk a fixed **percentage of current equity** on each trade, defined by the distance to your stop.

**The master formula:**

```
Position size (units) = (Equity × Risk%) ÷ (Entry − Stop)
```

Worked example, NSE cash: Capital ₹5,00,000. Risk per trade 1% = ₹5,000. You buy RELIANCE at ₹1,450 with a stop at ₹1,420 (₹30 risk per share).

```
Shares = 5,000 ÷ 30 = 166 shares
Position value = 166 × 1,450 = ₹2,40,700
```

Note the position *value* (₹2.4L, ~48% of capital) is large, but the *risk* is controlled at ₹5,000. Beginners fixate on position value; professionals fixate on risk. The stop distance, not the notional, defines exposure.

**F&O version with lots.** Bank Nifty lot = 15 (2026 spec — always verify current lot size). Say you go long a Bank Nifty future at 52,000 with a stop at 51,700 (300 points). Point value = ₹15/point per lot, so one lot risks 300 × 15 = ₹4,500.

```
Lots = ₹5,000 risk budget ÷ ₹4,500 per lot = 1.1 → round DOWN to 1 lot
```

Always round *down*. Rounding up quietly breaks your risk cap.

**Why fractional (percent-of-equity) beats fixed-rupee.** Because the risk unit scales with the account, you de-risk automatically in drawdowns and press when winning. After a 20% drawdown, 1% of a shrunken account is a smaller rupee bet — the model brakes for you. This anti-fragile property is the whole point.

**The recommended risk-% ladder:**

| Trader profile | Risk per trade |
|---|---|
| New / rebuilding after a blowup | 0.25%–0.5% |
| Consistent but still learning | 0.5%–1.0% |
| Proven edge, 200+ logged trades | 1.0%–2.0% |
| Anyone who says "3%+" | Reconsider — you are one streak from ruin |

## Model 2 — Fixed-ratio sizing (Ryan Jones)

Fixed-fractional adds contracts *linearly* with equity. Fixed-ratio adds them based on a "delta" — the profit per contract required before you add the next one. It grows exposure slower early (safer for small accounts) and faster once large.

```
Contracts N is held until profit = (N × (N−1) ÷ 2) × Delta
```

With a delta of ₹50,000: you trade 1 lot until you've made ₹50,000, then 2 lots; go to 3 lots after a further ₹1,00,000 cumulative, and so on. The bigger the delta, the more conservative. Fixed-ratio suits a trader compounding a single instrument (say one who trades only Nifty futures) and wanting a disciplined, mechanical scale-up rule that doesn't over-lever a ₹2–3L account early. Its weakness: it ignores per-trade stop distance, so pair it with a hard per-trade risk cap.

## Model 3 — Volatility-parity (ATR) sizing

The problem fixed-fractional ignores if you use fixed *point* stops: a 300-point stop on Bank Nifty at 15% annualised vol is not the same risk as a 300-point stop at 30% vol. Volatility sizing normalises this. You set the stop as a **multiple of ATR**, so position size shrinks automatically when the instrument is wild and grows when it's calm.

```
Stop distance = k × ATR(14)          (k typically 1.5 to 3)
Position size  = (Equity × Risk%) ÷ (k × ATR)
```

Worked example: You trade TATASTEEL. ATR(14) = ₹4.20. You use k = 2, so stop = ₹8.40. Capital ₹5,00,000, risk 1% = ₹5,000.

```
Shares = 5,000 ÷ 8.40 = 595 shares
```

When TATASTEEL calms and ATR drops to ₹2.50, the same 1% risk with k=2 (stop ₹5.00) buys 1,000 shares — larger position, identical rupee risk. This is **risk-parity at the trade level** and it is how most systematic desks size. It also produces a smoother equity curve because each trade contributes roughly equal risk regardless of the instrument's mood. For a multi-instrument book (Nifty + a few stocks + a MCX position), ATR sizing is the cleanest way to make every position "weigh" the same.

## Model 4 — Kelly and fractional-Kelly

Kelly answers a precise question: what bet fraction maximises the *long-run geometric growth rate* of capital? For a two-outcome bet:

```
f* = W − (1 − W) ÷ R
```

where W = win probability and R = win/loss payoff ratio (average win ÷ average loss).

Worked example: your logged stats say W = 0.45 and R = 2.0 (winners average twice your losers).

```
f* = 0.45 − 0.55 ÷ 2.0 = 0.45 − 0.275 = 0.175 → 17.5%
```

Full Kelly says risk 17.5% of capital per trade. **Do not do this.** Full Kelly is the growth-maximising fraction, but its drawdowns are savage — a full-Kelly bettor routinely endures 50%+ drawdowns, and if your estimated W and R are even slightly optimistic (they always are; retail traders overestimate their edge), you cross to the *right* of the Kelly peak, where growth turns negative and ruin becomes likely.

The professional practice is **fractional Kelly** — typically one-quarter to one-half. Half-Kelly captures ~75% of the growth rate with roughly *half* the volatility. Quarter-Kelly is even calmer. In the example above, quarter-Kelly = 4.4%, half-Kelly = 8.75% — and even those feel aggressive against the 1–2% fixed-fractional norm, which tells you how conservative sensible retail sizing actually is.

The real value of Kelly for a retail trader is not the exact number — it is the **diagnostic**. If Kelly comes out *negative*, you have no edge and should not be sizing up at all; you should be paper-trading or fixing the system. If Kelly is tiny (say 3%), it warns you that your edge is thin and demands small size. Kelly is a truth-serum for your win-rate and payoff assumptions.

## Model 5 — The martingale family (and why anti-martingale wins)

**Martingale**: double the bet after every loss so one win recovers everything. On a random-ish market this is a wealth-destruction engine. It converts a string of small losses into one account-ending loss, and it *feels* like it's working right up to the trade that wipes you. Averaging down into a losing F&O position — buying more Bank Nifty puts as the index rips higher against you — is martingale in disguise, and it is the single most common way leveraged retail accounts go to zero. The strategy has a wonderful win-rate (you win most sequences) and a catastrophic expectancy (the rare sequence takes everything). **Never use it.**

**Anti-martingale**: increase size when winning, decrease when losing. Every model in this chapter (fixed-fractional, fixed-ratio, Kelly) is anti-martingale by construction — they press the accelerator with house money and brake into drawdowns. This is the correct instinct: trends and momentum give winning streaks a mild autocorrelation, and pressing during a hot streak while cutting during a cold one aligns your exposure with your recent edge. Pyramiding into a winning position (adding at 51,900, 52,200, 52,500 on a running Bank Nifty long, trailing the stop up) is disciplined anti-martingale scaling — the mirror image of the martingale trap.

## Model 6 — Portfolio heat (the correlation-aware overlay)

Per-trade sizing is necessary but not sufficient. If you're long RELIANCE, long HDFCBANK, long ICICIBANK, and long Nifty futures, you are not in four 1% trades — you are in one ~4% bet on "Indian large-caps go up," because these instruments are heavily correlated. When the market gaps down on a bad global cue, all four stops trigger together and you lose 4% in a morning, not 1%.

**Portfolio heat** = the sum of all open risk (each position's distance-to-stop × size), expressed as a % of equity. Set a hard ceiling.

| Heat rule | Suggested cap |
|---|---|
| Total open risk (portfolio heat) | 4%–6% of equity |
| Max risk in one *sector* (Bank/IT/etc.) | 2%–3% |
| Max risk in one *direction* (net long/short) | 3%–4% |
| Single-position risk | 1%–2% |

Worked example: Capital ₹5,00,000, heat cap 5% = ₹25,000 of total open risk. You have three banking longs already on, each risking ₹5,000 (₹15,000 total, and all in one sector — already at the 3% sector cap). A fresh long ICICIBANK signal appears. Even though a *single* new 1% trade is "allowed," it would push banking-sector risk to ₹20,000 (4%) — over the sector cap. You skip it or size it down. Heat budgeting is what stops a diversified-looking book from being a concentrated bet in disguise.

For correlated positions, a practical shortcut: treat highly-correlated names (the PSU banks, the private banks, the IT majors) as *one* risk unit and size the *group*, not each ticker independently.

## Putting it together — a worked multi-position session

Capital ₹10,00,000. Rules: 1% per trade, 5% portfolio heat, 3% per sector, ATR stops at k=2.

1. **Long Nifty future** at 24,800, ATR(14)=180, stop = 24,440 (360 pts). Lot=25 → ₹9,000/lot risk. Budget ₹10,000 → **1 lot** (₹9,000 risk). Heat = 0.9%.
2. **Long INFY cash** at ₹1,880, ATR=₹28, stop=₹1,824 (₹56). Budget ₹10,000 → 178 shares (₹9,968 risk). Heat now 1.9%.
3. **Long TCS cash** — signal fires, but INFY + TCS are both IT and correlated. Combined IT risk would be ₹20,000 (2%), under the 3% sector cap, so allowed but sized as a *pair*. Take a half-size TCS (₹5,000 risk). IT sector risk = ₹15,000 (1.5%). Total heat = 2.4%.
4. **Short USDINR** idea on MCX — *uncorrelated* with equity longs, even mildly hedging. Full 1% allowed. Heat → 3.4%, still under 5%. Take it.

Notice the model let you add the *uncorrelated* trade freely while throttling the *correlated* one. That is the entire art.

## Pitfalls that quietly kill accounts

- **Sizing off notional, not risk.** "I only put ₹50,000 into it" tells you nothing. Risk = size × stop distance.
- **Widening the stop to fit a bigger position.** This inverts the model — the stop must come from the chart, then size follows. If the chart stop is too far for 1% risk at a meaningful size, take fewer shares, not a looser stop.
- **Ignoring gap risk in F&O.** Overnight, your "stop" is a suggestion, not a guarantee. Bank Nifty can gap 500 points on a global event. Size assuming your stop might slip; keep overnight positions smaller.
- **Compounding the risk-% too fast after a hot streak.** Three good weeks is not statistical proof of a bigger edge. Scale size on *logged sample size*, not on recent mood.
- **Forgetting costs.** STT, brokerage, exchange fees, GST, and slippage all shrink R. A system with R=1.2 gross can be R<1 net after costs on a frequently-traded intraday strategy.
- **Full Kelly / averaging down.** Covered above. Both feel smart, both are ruin machines.

## How to build it into your routine

Keep a one-line **pre-trade sizing checklist** taped to your monitor:

1. Where is the chart stop? (Not "how much do I want to risk in points" — where does the setup fail?)
2. Rupee risk = 1% of *current* equity. Recompute after every closed trade; don't use last month's number.
3. Size = risk ÷ stop distance. Round **down** to whole shares/lots.
4. Does this push portfolio heat over 5%, or sector risk over 3%? If yes, shrink or skip.
5. Is it correlated to something I already hold? If yes, size the *group*.
6. Log it — instrument, entry, stop, size, rupee risk, R-multiple on exit.

Do this for 200 trades and you will have real W and R statistics to feed Kelly, and a heat history that tells you your true worst-case day. The models in this chapter are not academic — they are the difference between a trader who compounds for a decade and one who is "starting over" every eight months.

## Interview-ready summary

Money management converts a statistical edge into a survivable, compounding business, and it matters more than signal quality because returns compound multiplicatively — a 50% drawdown needs a 100% recovery. The workhorse model is **fixed-fractional (percent-risk)** sizing: risk a fixed 0.5–2% of *current* equity per trade, with position size = (equity × risk%) ÷ (entry − stop), always rounded down. **ATR/volatility sizing** normalises risk across instruments by setting the stop as a multiple of ATR so every trade carries equal rupee risk. **Kelly** defines the growth-maximising bet fraction (f* = W − (1−W)/R) but is used only fractionally (quarter- to half-Kelly) because full Kelly's drawdowns are brutal and estimation error pushes you toward ruin; its best use is as an edge *diagnostic* — negative Kelly means no edge. All sound models are **anti-martingale** (press when winning, cut when losing); the **martingale/averaging-down** family has a great win-rate and a catastrophic expectancy and must be avoided. Finally, **portfolio heat** caps total open risk (≤5–6%) and sector/directional risk, because correlated positions (the private banks, the IT majors, Nifty + its constituents) are secretly one bet. Master these and your edge survives long enough to matter.
