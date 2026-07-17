# The Expiry-Day Playbook (Bank Nifty)

*Practitioner supplement — NSE F&O options, India, 2026. Expiry-day conventions, STT and lot sizes are date-stamped to Jan 2026. SEBI/NSE changed index expiry days and single-weekly-expiry rules in 2024–25; **verify the current expiry weekday for Bank Nifty and whether Bank Nifty still has a weekly expiry at all** before trading. Some of what follows assumes a weekly Bank Nifty expiry exists; adapt to the current schedule.*

## The idea

Expiry day is the one session where **time decay is not a slow drip but a waterfall.** An option that spans a week loses theta gradually; on expiry day, an at-the-money weekly option can lose 60–90% of its remaining extrinsic value in a single session, most of it in the last two hours. That concentrated decay is the entire opportunity — and the entire danger.

Bank Nifty (BNF) is the classic expiry-day instrument in India because it is high-beta, deeply liquid, and moves in large point terms (a 0.5% wobble on a 52,000 index is ~260 points, enough to turn a comfortable short into a loss). Two opposite crowds live on expiry day. **Premium sellers** treat the day as a theta harvest: sell ATM/OTM options, collect the fast decay, and pray the index pins near their strikes ("max pain"). **Gamma scalpers and lottery buyers** treat it as convexity day: buy cheap far-OTM options for a few rupees hoping a late trend or a "0DTE" squeeze multiplies them 5–20×.

The defining feature is **gamma.** On the last day, near-ATM options have enormous gamma: their delta flips from 0.5 toward 1 or 0 with tiny index moves. For the seller, that means a position that is delta-neutral at 1:00pm can be deeply directional by 2:30pm without you touching it. Expiry-day P&L is therefore a **theta-vs-gamma tug of war**: you are paid theta to accept gamma risk, and the market spends the last two hours deciding whether the pin holds or a trend runs the strikes.

Honest framing: **expiry-day selling has a beautiful equity curve until it doesn't.** It wins on the majority of quiet expiries and gives it all back on the occasional trending expiry — a policy leak, a global gap, an index heavyweight bank cracking. Most retail "expiry sellers" are short gamma with no plan for the trend day, and the trend day is what clears them out. This chapter is about harvesting theta *with* a gamma stop, not selling naked and hoping.

## The mechanics

### Why decay accelerates: theta and gamma on the last day

Extrinsic value ≈ proportional to √(time). With hours left, √t is tiny, so extrinsic value is small and *falls fast*. Meanwhile gamma ≈ inversely proportional to √t, so gamma is *huge*. The two are linked: high gamma is the price you pay for high theta. On expiry morning an ATM BNF weekly might have ₹120–₹180 of pure time value that must decay to **zero by settlement**.

**Settlement:** BNF weekly options are **cash-settled** on the expiry-day settlement value (typically a time-weighted average of the last trading window of the underlying — verify current methodology). There is no delivery; ITM options settle to intrinsic, OTM expire worthless.

### The STT-on-exercise trap (critical on expiry)

- Intraday, STT on options is charged on the **sell-side premium** (~0.1%, verify 2026 rate).
- But if you **let a long option expire in-the-money**, STT is levied on the **full intrinsic/settlement value**, not the premium. A 200-point ITM BNF call left to expire can attract STT on the entire ~₹200 × lot notional-of-intrinsic — vastly more than the premium STT. **Rule: square off ITM longs before close; do not let them expire ITM unless you've done the STT math.** This single mechanic quietly destroys naïve expiry-day P&L.

### "Max pain" and pinning

**Max pain** is the strike at which the total value of all outstanding options (that expire worthless) is maximised — loosely, the strike where option *buyers* lose the most and *sellers* gain the most. Markets often gravitate toward high open-interest strikes near expiry ("pinning") because dealers who are short gamma hedge in a way that dampens moves near those strikes. It is a *tendency, not a law* — pinning fails hard on trend days and news. Use it as a magnet hypothesis, never as a guarantee.

### Structures for expiry day

| Structure | Greeks | Thesis | Risk |
|---|---|---|---|
| Short ATM straddle | +theta, −gamma, −vega | pin near strike | trend day = large loss |
| Short iron fly (straddle + wings) | +theta, −gamma, capped | pin, defined risk | wing-width max loss |
| Short strangle (OTM) | +theta, −gamma | index stays in range | tail gap |
| Iron condor (defined) | +theta, −gamma, capped | range-bound | width − credit |
| Long OTM "lottery" | −theta, +gamma, +vega | late trend/squeeze | premium → 0 (most days) |
| Directional debit spread | mixed | intraday trend view | premium at risk |

### Costs

Expiry structures are multi-leg and turned over intraday, so friction is heavy: brokerage per leg, exchange txn charges, SEBI fee, stamp duty (buy side), **STT on sell premium**, plus 18% GST on charges. Four-leg round-trip on BNF: **~₹250–₹450 per lot.** On a day where you're harvesting ₹100–₹150 of decay, fees are a first-order cost, not a rounding error.

## Worked trade — Bank Nifty expiry-day iron fly

**Setup (illustrative).** Expiry day, 10:15am. BNF spot = **51,900**, coiling in a 51,700–52,100 range, India VIX low (~13), no scheduled event, heavyweight banks quiet. Max-pain and highest-OI strikes cluster around **52,000**. I want to harvest theta into the pin with a hard cap.

**Structure: short 52,000 iron fly.**

| Leg | Strike | Action | Premium (₹) |
|---|---|---|---|
| Call | 52,000 CE | Sell | 150 |
| Put | 52,000 PE | Sell | 160 |
| Call wing | 52,300 CE | Buy | 55 |
| Put wing | 51,700 PE | Buy | 60 |

- **Net credit** = (150 + 160) − (55 + 60) = **₹195** per share.
- Lot size (BNF, verify) = **15** → credit/lot = 195 × 15 = **₹2,925**.
- **Wing width** = 300 pts; **max loss** = (300 − 195) × 15 = **₹1,575** per lot.
- **Breakevens** ≈ 52,000 ± 195 = **51,805 / 52,195**.
- **Greeks (per lot, approx):** Delta ≈ 0, Theta **+₹1,200–₹1,800/day equivalent** front-loaded (the prize), Gamma **strongly negative** (the danger), Vega mildly negative.

**How the day plays (base case — pin holds).** BNF chops between 51,850 and 52,050 all afternoon, closing/settling **51,980**. The short 52,000 straddle decays toward ~₹20 intrinsic-ish combined; wings expire worthless.

**P&L at settlement (base case):**

| Leg | Entry (₹) | Settlement value (₹) | Leg P&L (₹) |
|---|---|---|---|
| 52,000 CE sold | 150 | 0 (settles ~0, spot below) | +150 |
| 52,000 PE sold | 160 | 20 (52,000−51,980) | +140 |
| 52,300 CE long | 55 | 0 | −55 |
| 51,700 PE long | 60 | 0 | −60 |
| **Net** | | | **+175 / share** |

- Gross = 175 × 15 = **₹2,625/lot** (of ₹2,925 max).
- **Costs** ~₹300/lot → **Net ≈ ₹2,325/lot.** On ~₹18,000 blocked margin (defined-risk fly, verify SPAN), ~**13% for the day**. But note: I must square the ITM 52,000 PE before close to avoid STT-on-intrinsic.

**Trend-day counterfactual.** Suppose at 1:30pm a global cue gaps BNF to **52,350** and it trends. The fly is now at/through the call wing: max loss **₹1,575/lot** realised — a bad day, capped. A *naked* short straddle instead would be losing (52,350 − 52,000 − 310) = ~₹40 and climbing with no cap; a further squeeze to 52,600 makes it ~(600 − 310) = ₹290 × 15 = **₹4,350/lot** and rising unbounded. The wings are the whole point.

## Management

**The gamma stop is the trade.** Because expiry gamma is huge, you cannot manage by staring at premium — manage by **spot distance to your short strike.** Pre-commit: "If BNF trades and holds beyond my breakeven (52,195 / 51,805) for X minutes, I act." Options:

**Scenario A — pin holds, quiet tape (base case).** Do nothing; let theta work. Consider closing at ~70–80% of max profit in the last hour rather than carrying settlement/STT mechanics. Square any ITM long/short legs before close.

**Scenario B — index drifts toward one side (delta building).** Two clean moves: (1) **roll the untested side in** — buy back the now-cheap far leg (e.g., PE side if drifting up), collect the dregs, and reduce; or (2) **delta-hedge with BNF futures / a single option** to flatten delta and keep collecting theta. Do not "average up" the short — that adds gamma exactly when gamma is dangerous.

**Scenario C — trend day / breakout.** Take the capped loss and *get out* or flip. On expiry, a confirmed trend beats mean-reversion because there's no time left for it to revert. Many desks **stop-and-reverse**: cut the short fly, buy the OTM option in the trend direction (now cheap, high gamma) as a lottery to recoup. Discipline over hope: the trend day is the day that decides your monthly P&L.

**Scenario D — IV spike intraday.** A midday vol pop (news) both raises your short marks and signals trend risk. Short-vega means the mark moves against you first; treat a sharp IV spike as an early warning to reduce, not to sell more "rich" premium.

**Buyer's management (if you're long lottery).** Have a hard time-stop: if the trend hasn't shown by ~1:30–2:00pm, theta will vaporise the premium — cut it. If it runs your way, scale out fast; expiry lottery gains evaporate as quickly as they appear.

## Risk & sizing

**Size to the capped max loss, and assume the trend day.** For the fly, max loss is ₹1,575/lot. Size so a full-loss expiry across all expiry-day positions is ≤ 1% of capital. If you run 5 lots, that's ₹7,875 at risk — fine on a ₹10-lakh book, reckless on ₹1 lakh.

**Never sell naked on expiry with real size.** The equity-curve trap: naked short straddles win ~4 of 5 expiries and the fifth erases a month. If you insist on naked for the extra credit, size it a *fraction* of defined-risk size and keep a hard futures stop. The wings cost you ~₹115 of credit here but convert an unbounded tail into a ₹1,575 cap — cheap insurance.

**Gamma is the portfolio risk.** Aggregate expiry-day short gamma across BNF and Nifty (and Fin Nifty if you trade it) — on a synchronized index gap they all lose together. Cap total short-gamma exposure; know your **net delta at the strikes** if the index gaps 1% either way.

**Liquidity and the last 15 minutes.** Spreads can widen and slippage spikes into the close as everyone squares up. Don't leave large positions to manage in the final minutes; exit the bulk earlier. Illiquid far strikes can trap you — stick to strikes with real OI.

**STT/settlement risk is a P&L risk.** An unsquared ITM long left to expire can turn a winning day into a loser via STT-on-intrinsic. Build "square all ITM before close" into your checklist. Cash settlement means no delivery, but the STT mechanic is real money.

**The honest statistic.** Expiry-day selling is a *short-gamma, positive-theta, negatively-skewed* strategy. The reason "sell options on expiry, it's free money" is a retail meme that ends in liquidation is that the trend day is under-weighted in people's mental model. Respect the gamma; the theta is only rent the market pays you for holding a live grenade.

## Pitfalls & interview-ready summary

**Pitfalls**
- **Selling naked and having no trend-day plan.** The one trending expiry pays for all the quiet ones — for the market, against you.
- **Managing by premium, not by spot-to-strike.** Expiry gamma means delta explodes; watch distance to your short strikes and pre-set a gamma stop.
- **STT-on-exercise.** Letting ITM longs expire attracts STT on intrinsic value — square them before close.
- **Averaging into a loser.** Adding to a short as the index runs toward it piles on gamma at the worst moment.
- **Trusting max pain as law.** Pinning is a tendency dealers create by hedging; it fails on news and trend days.
- **Fee blindness.** ₹250–₹450/lot round-trip on four legs against a ₹100–₹150 decay harvest — the edge is net, not gross.
- **Last-15-minutes liquidity.** Wide spreads and slippage into the close; exit the bulk earlier.
- **Assuming a weekly BNF expiry exists.** SEBI/NSE rationalised weekly expiries in 2024–25 — confirm the current Bank Nifty expiry schedule.

**Interview-ready summary.** *Bank Nifty expiry day is a concentrated theta-vs-gamma trade. Extrinsic value collapses to zero by cash settlement, so premium sellers harvest fast decay — but expiry gamma is enormous, so a delta-neutral short at noon can be deeply directional by afternoon. The professional structure is a defined-risk short iron fly around the high-OI / max-pain strike: it captures the pin's theta, caps the tail at the wing width, and stays margin-light under SPAN, unlike a naked straddle whose trend-day loss is unbounded. Management is a pre-committed gamma stop measured in spot-distance to the short strikes — roll the untested side, delta-hedge with futures, or on a confirmed breakout take the capped loss and possibly stop-and-reverse into cheap high-gamma OTM options. Size to the capped max loss assuming the trend day happens, cap aggregate short gamma across indices, square all ITM legs before close to dodge STT-on-intrinsic, and confirm the current 2026 expiry weekday. The strategy is positive-theta and negatively-skewed: most expiries pay, the trend expiry punishes, and retail loses by selling naked with no plan for that day.*
