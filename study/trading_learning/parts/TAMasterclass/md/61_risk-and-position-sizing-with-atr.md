# Risk & Position Sizing with ATR

## What it is & why it works

Position sizing is the single most important — and most neglected — decision in trading. It answers the question every trade forces on you: *how many lots, how many shares, how much money do I put at risk here?* Most retail traders answer it by gut ("I'll buy 5 lots because that feels right") or by capital ("I'll use half my account"). Both are recipes for eventual ruin, because they ignore the one variable that actually determines survival: how much you *lose* if you're wrong, expressed as a fixed, small fraction of your capital.

The professional answer is **fixed-fractional risk sizing**: on every trade you risk the same small percentage of your capital — typically 0.5% to 1% — regardless of the instrument or how confident you feel. The number of lots is then a *derived* quantity: it falls out of two inputs — your rupee risk budget and the distance from entry to stop. This flips the beginner's logic on its head. The beginner picks the quantity first and discovers the risk later; the professional fixes the risk first and lets the quantity adjust. This is why the same trader might buy 8 lots of a tight-stop Nifty setup and only 2 lots of a wide-stop Bank Nifty setup — same rupee risk, different size, because the *stop distance* differs.

This is where **ATR — Average True Range** — becomes indispensable. ATR measures how much an instrument typically moves in a given period; it is a pure volatility gauge. It matters for sizing because a stop must be placed *beyond the noise* — far enough that ordinary volatility doesn't take you out, but no further. A fixed rupee stop ("I'll risk 50 points on everything") is nonsensical: 50 points is a hair-trigger on Bank Nifty (which swings 400+ points a day) and a mile-wide stop on a quiet stock. ATR normalises this. By setting stops as a multiple of ATR and sizing off that ATR-based stop, you automatically risk the same fraction of capital whether you trade calm Nifty or wild Bank Nifty, calm markets or a VIX-spiking panic. Volatility expands, your stop widens, and your position size shrinks to keep rupee risk constant. That is the mechanism that keeps you alive across regimes.

The deep reason this works is the mathematics of ruin. Trading is a game of surviving losing streaks. Risk 1% per trade and a run of ten losers costs you ~10%; risk 10% and the same streak nearly wipes you out. Small, consistent fractional risk is what lets your positive expectancy actually compound instead of getting interrupted by a blow-up. Sizing is not a detail — it *is* risk management.

## The mechanics — ATR, the R-model, and the sizing formula

**Average True Range (ATR).** True Range for a candle is the greatest of: (a) current high − current low, (b) |current high − previous close|, (c) |current low − previous close|. The last two capture gaps. ATR is a smoothed average (Wilder's, default period 14) of True Range. It is expressed in the instrument's own units — points for indices, rupees for stocks. If Bank Nifty's 14-day ATR is 620, the index typically travels about 620 points in a day; if a stock's daily ATR is Rs 18, it typically ranges Rs 18.

**The R-model.** "R" is your risk unit — the rupee amount you lose if a single trade hits its stop. Everything is measured in R: a trade that makes twice your risk is +2R; a loss is −1R. Fixing R as a constant fraction of capital is what makes results comparable and compounding clean.

**The core sizing formula.** Three steps:

1. **Rupee risk budget** = Capital × risk% per trade.
2. **Per-unit risk** = |Entry − Stop| × instrument multiplier (lot size for F&O, or 1 for a share).
3. **Quantity** = Rupee risk budget ÷ Per-unit risk (round *down*).

Where the stop comes from ATR: **Stop = Entry − (k × ATR)** for a long (or Entry + k×ATR for a short), with k typically 1.5–3. A tighter k (1.5) suits mean-reversion; a wider k (2.5–3) suits trend trades that must breathe.

Let's make it concrete. Capital Rs 10,00,000, risk 1% = **Rs 10,000 budget**. Bank Nifty ATR(14) = 600, you choose k = 2, so stop distance = 1,200 points. Bank Nifty lot = 15, so per-lot risk = 1,200 × 15 = Rs 18,000. Quantity = 10,000 ÷ 18,000 = 0.55 → **round down to 0 lots** — meaning at 1% risk this wide ATR stop is too big for one lot on a 10-lakh account. Either reduce k, reduce timeframe, or accept you need more capital. This is ATR *telling you the truth*: the trade is too big for your account. A fixed-rupee sizer would have blindly bought lots and over-risked.

Contrast with Nifty: ATR(14) = 130, k = 1.5, stop = 195 points, lot = 75, per-lot risk = 195 × 75 = Rs 14,625. Quantity = 10,000 ÷ 14,625 = 0.68 → still under a lot at 1%. This shows why index F&O sizing on a small account is tight — and why traders use a smaller k, tighter timeframe (15-min ATR is far smaller than daily), or accept 0.5-lot-equivalent risk via options.

For a **stock** example: Reliance at Rs 2,900, daily ATR Rs 55, k = 2 → stop distance Rs 110, stop at Rs 2,790. Per-share risk = Rs 110. Budget Rs 10,000 ÷ 110 = **90 shares** (round down). If you'd instead bought "Rs 5 lakh worth" (172 shares), a stop-out would cost Rs 18,900 — nearly 2% — almost double your intended risk. The ATR method sizes it correctly.

Summary table of the workflow:

| Step | Formula | Example (Reliance) |
|---|---|---|
| Risk budget | Capital × risk% | 10,00,000 × 1% = Rs 10,000 |
| ATR & k | ATR(14), choose k | Rs 55, k = 2 |
| Stop distance | k × ATR | Rs 110 |
| Per-unit risk | stop dist × multiplier | Rs 110 (1 share) |
| Quantity | budget ÷ per-unit risk | 90 shares |

## Reading it — a worked Bank Nifty swing example, phase by phase

Capital Rs 20,00,000; risk 0.75% = **Rs 15,000 per trade**. A Bank Nifty swing long setup forms on the daily chart around 48,000.

**Phase 1 — Measure volatility.** Bank Nifty's daily ATR(14) reads 640. This immediately tells me the instrument routinely moves ±640 points a day; my stop must sit well beyond that or normal noise will stop me out. India VIX is a moderate 13, so this is a *normal*, not panic, volatility environment.

**Phase 2 — Place the ATR stop.** For a swing trend trade I use k = 2.5 to give the position room to breathe through daily swings. Stop distance = 2.5 × 640 = 1,600 points. Entry at 48,050 (on the breakout trigger), stop at **46,450**. I sanity-check against structure: the recent swing low is 46,600, so my ATR stop at 46,450 sits *just below* structure — good confluence, the volatility-based and structure-based stops agree.

**Phase 3 — Size the position.** Per-lot risk = 1,600 points × 15 (lot size) = Rs 24,000. Budget Rs 15,000 ÷ 24,000 = 0.63 lots → I can't take even one lot in futures at this risk. Reading this honestly: on a 20-lakh account, a full-ATR Bank Nifty *swing* stop is too wide for one futures lot at 0.75%. My options are (a) raise risk to 1.2% (Rs 24,000) to fund exactly 1 lot — a deliberate, sized-up decision, or (b) express the trade via an **in-the-money option** whose delta approximates the futures exposure but caps absolute loss at the premium, or (c) trade a tighter timeframe. I choose (a) consciously: I accept 1.2% risk this once and take **1 lot**, knowing my rupee risk is Rs 24,000.

**Phase 4 — Define the trade in R.** My risk R = Rs 24,000 (1,600 points × 15). My first target is a measured move to 50,050 — that's 2,000 points, or 2,000 ÷ 1,600 = **1.25R**. A trailing extension to 51,000 would be (2,950 ÷ 1,600) = **1.84R**. Framing every target in R keeps me comparing apples to apples across trades of different point-sizes.

**Phase 5 — Volatility-adjusted management.** As the trade works and Bank Nifty rallies, I re-read ATR: if VIX spikes to 20 and ATR jumps to 900, I *widen* my trailing stop distance (a 2×ATR trail is now 1,800 points, not 1,280) so the noisier tape doesn't shake me out prematurely. Conversely, if volatility contracts and ATR falls to 450, I tighten the trail. The stop *breathes with the market* because it's tied to ATR, not a fixed number. This dynamic adjustment is the practical payoff of ATR-based risk.

The lesson the numbers teach: ATR forced me to confront that Bank Nifty swing futures are *large* relative to a 20-lakh account, and to make a conscious sizing decision rather than blindly buying lots. That confrontation is the entire point.

## Trading it — applying sizing across entry, stop, and scenarios

Position sizing isn't a one-time calculation at entry; it governs behaviour through the trade's life across scenarios.

**Scenario A — Normal winner.** Sized at 1 lot / Rs 24,000 risk. Hits +1.25R at first target; sell half (or in a 1-lot case, book two-thirds via partial exit if using multiple option legs), move stop to breakeven. Now the position is risk-free and any further move is pure profit. Sizing correctly at entry is what made the +1.25R worth a meaningful Rs 30,000, not a trivial amount.

**Scenario B — Volatility expansion mid-trade.** VIX spikes on a global cue; ATR jumps 40%. A fixed-stop trader gets whipsawed out on noise. The ATR sizer had *already* placed a wider stop and, on the *next* trade, will automatically size *smaller* (bigger ATR → wider stop → fewer lots for the same rupee risk). The system self-throttles in dangerous conditions — a crucial survival feature. Many pros add an explicit rule: if India VIX > 20, cut risk% in half.

**Scenario C — Gap through the stop.** Bank Nifty gaps down 900 points overnight on a banking-sector shock, blowing past your 46,450 stop; you exit at 46,000, losing ~1.3R instead of 1R. This is why (i) swing sizing uses a smaller risk% than intraday, (ii) event-heavy periods warrant reduced size, and (iii) options (defined-risk) are attractive for holding through binary events — the most you can lose is the premium, known in advance.

**Scenario D — Adding to a winner (pyramiding).** As price runs and you trail the stop up, the *original* position now has locked-in profit. You may add a second tranche — but sized off *its own* fresh ATR stop and counted within total open risk. The rule of thumb: total open risk across all positions should stay under ~2–3% of capital. Pyramiding done off ATR keeps each add correctly sized rather than doubling blindly.

The unifying principle: at *every* decision — initial entry, scaling in, trailing, or reacting to a vol spike — you recompute size or stop from current ATR and a fixed rupee-risk rule. Consistency of *risk*, not consistency of *quantity*, is the goal.

## Confluence — combining ATR sizing with structure, VIX, and option data

ATR sizing is most powerful when combined with other tools rather than used in isolation.

**ATR stop + structural stop.** The best stop is one where the *volatility* stop and the *structure* stop (below a swing low, below support, below VWAP) roughly coincide, as in our Bank Nifty example (ATR said 46,450, structure said 46,600). When they agree, you have high confidence. When ATR would place the stop *inside* obvious structure, respect the structure and place it just beyond — then re-size for the wider distance. Structure defines *where* you're wrong; ATR confirms the distance is beyond noise.

**ATR + India VIX (portfolio-level throttle).** ATR is instrument volatility; India VIX is the market's expected volatility. Rising VIX warns that ATRs across instruments will expand and gaps become more likely. A robust rule: scale total portfolio risk *down* as VIX rises (e.g., halve risk% above VIX 20, quarter it above 30). This is macro-level position sizing layered on top of per-trade ATR sizing.

**ATR + option-chain / IV for instrument choice.** When implied volatility (and hence option premiums) is high, buying options is expensive and theta bleeds fast — a wide-ATR environment where you'd otherwise size small in futures might favour *spreads* (defined risk, cheaper) or option *selling* with strict risk caps. When IV is low relative to realised ATR (options "cheap"), buying options to express a directional view is attractive because the premium underprices the movement ATR says is likely. Thus ATR (realised movement) versus IV (priced movement) informs *which instrument* gives the best risk-adjusted expression of the same signal. Sizing the option position still ties back to a rupee-risk budget: risk the premium such that a full loss is ≤ your R.

**ATR + expected R for trade selection.** Compute each candidate trade's target in ATR/R terms. A setup offering 3R for 1R risk beats one offering 1.2R, even if both "look good." ATR-normalised R lets you rank trades objectively and allocate risk to the best ones.

## Pitfalls & false signals — where sizing goes wrong

**Fixed-quantity thinking.** "I always trade 5 lots." This is the cardinal error: it risks wildly different amounts on tight-stop versus wide-stop trades and guarantees eventual over-risk in volatile conditions. Always size from risk, never from a habitual quantity.

**Fixed-rupee stops ignoring ATR.** Placing the same "50-point stop" on every instrument means you're inside the noise on volatile names (stopped out constantly) and too wide on quiet ones (over-risking). ATR exists precisely to prevent this.

**Risking too much per trade.** The most common account-killer. At 5% per trade, a perfectly normal 6-trade losing streak costs ~26%; at 10%, it's catastrophic. Keep per-trade risk at 0.5–1%. Higher feels faster but mathematically courts ruin — the drawdowns compound against you.

**Ignoring correlation / total open risk.** Sizing three trades at 1% each *looks* like 3% risk, but if they're Bank Nifty, HDFC Bank, and ICICI Bank, they're effectively the *same* bet — a bank-sector shock stops out all three for ~3% at once. Correlated positions must be treated as one; cap *aggregate* risk, not just per-trade risk.

**Over-tight ATR multiples.** Using k = 1 to "keep the stop small and size big" defeats the purpose — you get stopped out by normal noise repeatedly, death by a thousand cuts. Match k to the trade type: mean-reversion 1.5, trend 2.5–3.

**Forgetting gap and liquidity risk.** ATR-sized stops assume you get filled *at* the stop. Overnight gaps and illiquid stocks blow through stops; your realised loss can exceed 1R. Model this by sizing swing trades smaller, avoiding illiquid names, and using defined-risk options through binary events.

**Static sizing in changing volatility.** Using last month's ATR when volatility has since doubled produces stale, over-sized positions. Recompute ATR regularly; in fast markets, use recent (shorter-period) ATR so sizing reflects *current* conditions.

**Confusing conviction with size.** Feeling sure about a trade is not a reason to risk 3%. Conviction is unmeasurable and usually wrong at extremes. Let confluence-grade adjust size *within a capped band* (e.g., 0.5% for B-setups, 1% for A+ setups) — never beyond the ceiling.

## Interview-ready summary

Position sizing is risk management, and the professional method is fixed-fractional: risk the same small percentage (0.5–1%) of capital on every trade, letting *quantity* be a derived output rather than a chosen input. The formula is three steps — rupee risk budget (Capital × risk%), per-unit risk (stop distance × lot size/multiplier), and quantity (budget ÷ per-unit risk, rounded down). ATR (Average True Range, Wilder-smoothed True Range, default 14) supplies the stop distance as a multiple k of ATR (1.5 for mean-reversion, 2.5–3 for trend), which normalises risk across instruments and regimes: when volatility rises, the ATR stop widens and position size automatically shrinks to hold rupee risk constant. Everything is tracked in R (your risk unit), so trades of different point-sizes become comparable and targets are expressed as R-multiples. The best stops are where the ATR (volatility) stop and the structural stop coincide; sizing is then throttled at the portfolio level by India VIX and refined by IV/option-chain data for instrument choice (futures vs spreads vs defined-risk options). The pitfalls are fixed-quantity or fixed-rupee thinking, risking too much per trade, ignoring correlation so several positions are secretly one bet, and forgetting gap risk that makes realised losses exceed 1R. The deep rationale is survival mathematics: small consistent risk lets a positive expectancy compound instead of being interrupted by ruin. The one-liner: *"Fix your risk, not your quantity — let ATR set the stop beyond the noise and let position size fall out of the math, so every trade risks the same small slice of capital regardless of which instrument or how volatile the market."*
