# Event Trading Playbook (Results, Budget, RBI, Fed)

*Practitioner supplement — NSE F&O options, India, 2026. Rules and tax figures are date-stamped to Jan 2026; verify current SEBI/NSE circulars, STT rates and margin parameters before you trade.*

## The idea

An "event" is a scheduled moment where the market knows *when* new information arrives but not *what*. Quarterly results, the Union Budget (Feb 1), the RBI Monetary Policy Committee (MPC) decision, the US Fed FOMC, CPI/GDP prints, and index rebalancing all share one signature: **implied volatility (IV) rises into the event and collapses the instant the news is out.** That collapse is the "IV crush," and it is the single most important fact in event trading. You are almost never being paid to guess direction; you are being paid — or you are paying — for the volatility term structure around a known date.

The event playbook earns its keep in two opposite modes. **Short-vol (you sell the event):** you believe the market has over-priced the move — the options are pricing a 4% swing and you think 2% is realistic — so you sell premium and harvest the crush. **Long-vol / convexity (you buy the event):** you believe the market has under-priced a fat tail — a Budget with a surprise capital-gains change, an RBI that turns hawkish, a bank result with an asset-quality bomb — so you buy cheap optionality and hope for a gap that dwarfs the premium.

The professional's edge is not a directional view. It is a **priced-move vs. realised-move** view. Before every event you compute the *breakeven move the options are pricing* and compare it to the *distribution of historical realised moves* for that specific event type. If the straddle prices a 3.5% Budget-day move and Budget days over the last ten years realised a median 1.6% with a 90th-percentile of 3.1%, the options are rich and you lean short. If the straddle prices 1.2% into an RBI meeting where a repo-rate surprise is live, you lean long. Everything else — strike selection, structure, sizing — flows from that one comparison.

Honest framing up front: **most retail event traders lose, and the ones who blow up are almost always short-vol.** Selling a naked strangle into results feels like free money nineteen times out of twenty; the twentieth is a 6-sigma gap that erases a year of gains. This chapter is biased toward *defined-risk* event structures for exactly that reason.

## The mechanics

### The priced move (straddle-implied move)

The fastest read on what options price for an event is the **at-the-money (ATM) straddle** of the nearest expiry that *contains* the event.

Priced move (₹) ≈ ATM Call premium + ATM Put premium
Priced move (%) ≈ (ATM straddle) / Spot

A sharper version uses ~0.85 × straddle because the straddle slightly overstates the one-standard-deviation move, but the raw straddle is the working desk number. If Nifty is at 24,000 and the weekly ATM straddle that spans the RBI meeting trades at ₹360, the market prices a ±1.5% move (≈ 360 points) by that expiry.

### Term-structure and IV crush

Event IV lives in the **front expiry**. The tell is a *kinked, backwardated* term structure: the expiry containing the event shows higher IV than both the expiry before and the expiry after. After the event, front IV mean-reverts violently — a 30–50% relative IV drop in a single session is normal for single-stock results, 15–30% for macro events on the index.

| Instrument | Typical pre-event ATM IV | Typical post-event ATM IV | Relative crush |
|---|---|---|---|
| Large-cap single stock (results) | 45–70% | 28–38% | −35% to −50% |
| Bank Nifty (RBI / results season) | 18–26% | 13–17% | −25% to −35% |
| Nifty (Budget / Fed) | 14–20% | 11–14% | −20% to −30% |
| India VIX (proxy) | spikes 2–5 pts pre-Budget | reverts next 2 sessions | — |

### Structures and their Greeks

| Structure | Direction view | Vega | Theta | Event thesis |
|---|---|---|---|---|
| Long straddle/strangle | none | long (+) | short (−) | realised > priced move |
| Short straddle/strangle | none | short (−) | long (+) | realised < priced; **undefined risk** |
| Iron condor / iron fly | none | short | long | crush + range, capped loss |
| Calendar (sell front, buy back) | none | long back / short front | mixed | monetise term-structure kink |
| Directional debit spread | yes | modest | modest | you have an edge on direction |
| Broken-wing butterfly | mild directional | short | long | crush + a lean, cheap/free wing |

### Margin and cost mechanics (India, 2026)

- **Buying options** costs only premium + charges — no SPAN margin. This is why defined-risk long structures are capital-light and blow-up-proof.
- **Short/undefined-risk** (naked straddle/strangle) attracts full **SPAN + Exposure** margin, and NSE raises these parameters *ahead of* big events (Budget, election counting days, major expiry). Expect margins to be 1.3–1.6× normal around events.
- **Defined-risk spreads** (condors, iron flies) are margined on max loss (roughly the wing width × lot × qty minus credit), so they are far more capital-efficient than naked shorts and cannot gap past your defined loss.
- **STT (2026):** ~0.1% on option *sell-side premium* on exercise/normal sale of options; STT on *exercised* in-the-money options is charged on **intrinsic/settlement value** — a real trap on expiry-week event trades (see the expiry chapter). Options are cash-settled on the index. *Verify current STT schedule.*
- **Other charges:** exchange txn charges, SEBI turnover fee, stamp duty on buy, brokerage, and 18% GST on (brokerage + txn + SEBI). On multi-leg event trades the round-trip friction on the index is typically ₹40–₹120 per lot per leg — material when you are harvesting a ₹300 crush.

## Worked trade — Bank Nifty into the RBI MPC decision

**Setup (illustrative levels, Jan-2026 style).** RBI MPC outcome is Friday morning. Bank Nifty spot = **52,000**. Weekly expiry is the same Thursday-of-following-week convention (verify current expiry day; NSE moved index expiries in 2024–25). The weekly ATM straddle spanning the event:

- 52,000 CE = **₹520**
- 52,000 PE = **₹500**
- ATM straddle = **₹1,020** → priced move ≈ **±1.96%** (≈ 1,020 pts)

Historical RBI-day realised moves on Bank Nifty over the last 12 meetings: median **1.1%**, 75th pct **1.7%**, max **3.4%** (a surprise hike). So the market prices ~2% but the *median* delivers ~1.1%. Consensus is "hold, neutral tone," rate cut fully priced out. My read: **options are rich, but a hawkish-surprise tail is live.** I do not want naked short risk into a central bank. I want the crush with a capped tail.

**Structure chosen: Iron Fly (short ATM straddle + protective wings).**

| Leg | Strike | Action | Premium (₹) |
|---|---|---|---|
| Call | 52,000 CE | Sell | 520 |
| Put | 52,000 PE | Sell | 500 |
| Call wing | 52,600 CE | Buy | 250 |
| Put wing | 51,400 PE | Buy | 240 |

- **Net credit** = (520 + 500) − (250 + 240) = **₹530** per share.
- Lot size (Bank Nifty, verify current) = **15**. 1 lot credit = 530 × 15 = **₹7,950**.
- **Max profit** = net credit = ₹7,950 (if BNF pins 52,000 at expiry).
- **Wing width** = 600 pts; **max loss** = (600 − 530) × 15 = **₹1,050** per lot. Cap is tiny relative to a naked straddle whose loss on a 3.4% gap would be ~(1,768 − 1,020) × 15 = **₹11,220** and theoretically unbounded.
- **Breakevens** ≈ 52,000 ± 530 = **51,470 / 52,530**.

**Greeks at entry (approx, per lot):** Delta ≈ 0 (balanced), Vega **negative** (~−₹90 per IV point — I *want* IV to fall), Theta **positive** but modest because the wings bleed too, Gamma **negative** (my enemy if BNF trends).

**The event.** RBI holds, tone dovish-neutral, no surprise. Bank Nifty opens the post-decision session and settles the day at **52,180** (+0.35%, well inside breakevens). ATM IV crushes from ~22% to ~16%.

**P&L after crush (same day, pre-expiry mark):**

| Leg | Entry (₹) | Post-event mark (₹) | Leg P&L (₹) |
|---|---|---|---|
| 52,000 CE sold | 520 | 300 | +220 |
| 52,000 PE sold | 500 | 210 | +290 |
| 52,600 CE long | 250 | 130 | −120 |
| 51,400 PE long | 240 | 95 | −145 |
| **Net** | | | **+245 / share** |

- Gross = 245 × 15 = **₹3,675** per lot (of a ₹7,950 max).
- **Costs (round trip, 4 legs, both sides):** brokerage ~₹80, txn+SEBI+stamp ~₹120, STT on sell legs ~₹60, GST ~₹18 → call it **~₹280 per lot**.
- **Net ≈ ₹3,395 per lot.** On margin blocked (~₹35,000 for the defined-risk fly, verify SPAN), that is ~**9.7% in a day**, with a hard-capped ₹1,050 downside had the tail hit.

Contrast: the crush earned most of the profit in the *first hour* after the decision. **Event trades are exit trades, not hold trades** — I close before theta on my long wings and any afternoon trend can erode the edge.

## Management

Event management is a decision tree you write *before* the event, because you will not think clearly in the 90 seconds after the print.

**Scenario A — move in your favour / IV crush as expected (base case).** Take profit fast. On a short-vol event structure, **80% of the crush is realised within the first 30–60 minutes.** I set a working buy-to-close order at ~60–70% of max profit and pull the trade the same session. Gamma risk (the market trending away from your short strikes intraday) is not worth carrying overnight for the last few rupees.

**Scenario B — small move, IV falls, but market drifts toward one wing.** Roll the *untested* side in. If BNF drifts up toward the call wing, I buy back the now-cheap 52,000 PE and 51,400 PE for a few rupees and let the call side ride, or roll the whole fly up 200 points to re-center. This "harvest the dead side" move locks the easy profit and re-neutralises delta.

**Scenario C — the tail: gap through a breakeven.** With the defined-risk fly, do *nothing panicked* — your loss is already capped at ₹1,050. If you were (against advice) in a naked strangle, this is the blow-up: buy back the tested leg immediately regardless of price, or hedge with a futures/deep option to stop the bleed. The lesson is structural: **the fly's wings mean the tail is a bad day, not a career-ending day.**

**Scenario D — IV does *not* crush (event postponed, or two-part event).** Sometimes a Budget is a two-day story, or the Fed presser at 12:30am IST re-ignites vol. If IV holds up after the print, my short-vol edge hasn't paid — exit at scratch rather than hoping. Never turn a failed event trade into a directional bet.

**Rolling long-vol event trades.** If you *bought* the straddle and the event gapped your way, don't be greedy on IV — the crush works against your remaining vega. Sell the winning leg into the move (delta is now large), keep the cheap losing leg as a free lottery, or close the whole thing. If the event fizzled and you're long, you're fighting both theta and crush — cut it in the first hour; the trade is dead.

**Directional event edge.** When you genuinely have a view (e.g., a bank with pre-announced strong deposit growth into results), express it as a **debit spread** or **broken-wing butterfly**, not a naked long option — the crush will eat a plain long call even if you're right on direction but the move is smaller than priced.

## Risk & sizing

**Position size to the tail, not the base case.** For defined-risk structures, size so that the *max loss* of all correlated event trades combined is ≤ 1–1.5% of capital. For the fly above (₹1,050 max loss/lot), a ₹10-lakh book could hold ~10 lots and still cap event loss near 1%.

**Never carry naked short vol into a central bank or Budget on size.** The realised-vs-priced edge is real, but the payoff is negatively skewed: many small wins, rare catastrophic loss. If you must be short naked, size it at a *fraction* of your normal — the SPAN margin hike itself is the exchange telling you the tail widened.

**Portfolio Greeks around events.** Aggregate vega across positions. If you are running short vega in an index condor *and* short vega in three single-stock result trades in the same week, you have a concentrated short-vol book that a single systemic shock (a surprise Fed, a geopolitical gap) hits all at once. Cap **net portfolio vega** and keep a small long-tail hedge (see the tail-risk chapter) live through event-heavy weeks like results season + Budget in late Jan–Feb.

**Margin/liquidity risk.** Exchanges raise margins *before* events and can widen further intraday on volatility. Keep 30–40% margin buffer so an event-day spike doesn't force a peak-of-panic liquidation. Bank Nifty and Nifty options are deeply liquid; single-stock options can gap on wide bid-ask right when you need to exit — prefer index events or the most liquid single names.

**The honest tail statistic.** Straddle-implied moves are *unbiased-ish* on average, which means the short-vol edge is thin and fee-sensitive. Retail typically loses because: (1) they sell naked and eat the one gap, (2) they hold past the crush and give back the edge to gamma/theta, and (3) friction (STT, GST, brokerage on 4 legs) quietly consumes a ₹200–₹300 edge. Respect all three.

## Pitfalls & interview-ready summary

**Pitfalls**
- **Confusing direction with volatility.** Being right on direction but the move being smaller than priced still loses money on a long option (crush). Trade the *priced-vs-realised* gap, not a hunch.
- **Holding through the crush.** The edge is front-loaded; the afternoon is gamma/theta noise. Exit windows are minutes, not days.
- **Naked short vol into macro.** The Budget capital-gains surprise, the hawkish RBI, the hot US CPI — these are exactly when naked strangles blow up. Use defined-risk wings.
- **STT-on-exercise trap.** Event trades that land in expiry week can be settled ITM and hit with STT on intrinsic value — reconcile settlement mechanics before expiry.
- **Ignoring term structure.** Selling the *back* month before an event, or buying an expiry that doesn't contain the event, means you paid for/against vol you never wanted.
- **Fee blindness.** Four-leg index structures round-trip ₹250–₹400/lot in charges — size the edge net, not gross.
- **Correlated event stacking.** A results-season book of short-vol single stocks + a short-vol index condor is one macro shock away from a synchronized drawdown.

**Interview-ready summary.** *Event trading in Indian options is a volatility term-structure trade, not a directional bet. Options price a "priced move" (≈ ATM straddle / spot) that inflates into a known date and collapses on the news — the IV crush. The professional compares that priced move to the distribution of historical realised moves for the specific event (results, Budget, RBI MPC, Fed) and leans short vol when options are rich, long vol when a fat tail is under-priced. Because the short-vol payoff is negatively skewed, defined-risk structures — iron flies and condors — dominate naked strangles: they capture the crush, cap the tail at the wing width, and are margin-light under SPAN. Execution is front-loaded (80% of the crush in the first hour), so event trades are exit trades. Size to the tail, cap portfolio vega across a stacked results/Budget calendar, respect 2026 STT-on-exercise and event margin hikes, and remember most retail loses on events by selling naked, holding past the crush, and bleeding the edge to fees.*
