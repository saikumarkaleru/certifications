# Position Sizing, SPAN Margin & Managing Book Greeks

*India F&O, 2026. Figures illustrative — verify current SPAN parameters, margin percentages, STT (~0.10% on options sell premium; ~0.125% on ITM exercise intrinsic — verify), and SEBI lot sizes on NSE/your broker before trading.*

## The idea

Amateurs pick trades; professionals size them and manage the aggregate. The difference between a trader who survives ten years and one who blows up in one bad month is almost never strategy selection — it is **how much** they put on and **how the whole book breathes** when volatility jumps. This chapter is about the two disciplines that separate the two: sizing each position against capital and margin, and managing the *net Greeks of the entire book* rather than the Greeks of any single trade.

This earns its keep every single day, but it *saves your account* on the three or four days a year when Nifty gaps 3–5% or India VIX doubles overnight. A book that looks perfectly hedged trade-by-trade can be catastrophically exposed in aggregate — five different "market-neutral" credit trades can all be short vega and short gamma, so one vol spike hits all five at once. The retail F&O reality in India is stark: SEBI's own studies have repeatedly shown the large majority of individual F&O traders lose money, and the losers are disproportionately the ones who wrote naked options sized to calm markets. Sizing and book-Greek management is the antidote.

The core idea: **margin tells you what you *can* put on; risk-based sizing tells you what you *should*; and net book Greeks tell you what you're *actually* exposed to.** All three must agree before a trade goes on.

## The mechanics

**SPAN + Exposure margin.** NSE uses SPAN (Standard Portfolio Analysis of Risk) to compute the margin on your F&O portfolio. SPAN simulates your book across a grid of price and volatility scenarios (spot moved up/down by the scan range, vol up/down) and charges you the *worst-case* loss across that grid. On top sits the **Exposure margin** (an additional buffer). Key consequences:

- SPAN is **portfolio-based**: hedged legs reduce margin. A long option that offsets a short one's tail is recognised, so spreads and condors cost far less margin than naked shorts.
- Margin is **dynamic**: as VIX rises, the scan range widens and margin on short options *increases* — often exactly when you're already losing, forcing liquidation at the worst time. This is the margin-call spiral.
- **Naked short options** carry the heaviest margin (they anchor the worst-case scenario) and can see intraday margin hikes.

| Structure | Typical margin/lot (illustrative, verify) | Max loss | Margin efficiency |
|---|---|---|---|
| Naked short Nifty straddle | ₹1.6–2.2 lakh | Unlimited | Poor |
| Short strangle | ₹1.4–2.0 lakh | Unlimited | Poor |
| Iron condor (150-wide wings) | ₹40k–70k | Defined ~₹7–11k | Good |
| Debit vertical spread | Premium paid only | Premium paid | Best (buyer) |
| Calendar spread | ₹30k–60k | ~net debit | Good |

**Position sizing — the risk-first method.** Size off *defined risk*, not off available margin. The mistake is "I have ₹10 lakh, margin per lot is ₹50k, so I can do 20 lots." No. Size off the loss you'll accept:

1. Fix **risk per trade** = R = 1% of capital (aggressive traders 2%, never more).
2. Compute **max loss per lot** for the structure.
3. **Lots = (Capital × R%) / max-loss-per-lot**, then floor it.

On ₹10 lakh, R = 1% = ₹10,000. Iron condor max loss ₹7,275/lot → **1 lot** (not 20). The margin permits 20; risk permits 1. Margin is the constraint that stops you; risk is the constraint that *should* stop you first.

**Book Greeks — the aggregation.** Every position contributes delta, gamma, theta, vega (and rho, minor for weeklies). The book's exposure is the *sum*, weighted by lots and lot size. You manage the totals:

| Greek | What the net tells you | Target discipline |
|---|---|---|
| **Net delta** | Directional exposure (in index points) | Keep within a band you'd accept as a naked position |
| **Net gamma** | How fast delta changes on a move | Short gamma near expiry is the killer — cap it |
| **Net theta** | Daily decay P&L | Positive if net seller — but that's the vega/gamma trade-off |
| **Net vega** | P&L per 1 vol-point move | The single most under-managed book risk in retail |

The uncomfortable truth every credit-seller learns: **positive theta is bought with negative vega and negative gamma.** You collect decay daily and pay it all back (and more) on the day vol and price both jump. Managing the book means capping the vega and gamma you'll carry so that the "pay it back" day is survivable.

## Worked trade

**Setup.** Capital ₹15 lakh. I already run two positions and want to add a third. Let me build the book and read its aggregate Greeks. (Nifty spot 24,000, lot 75; Bank Nifty 52,000, lot 30 — verify.)

**Existing book:**

- **Position 1:** Nifty 24,000 short straddle, 1 lot (sold 24000 CE ₹120 + 24000 PE ₹115). Delta ~0, gamma **−0.010**, theta **+₹9,000/day**, vega **−₹5,500 per vol pt**.
- **Position 2:** Bank Nifty long 52,000 put, 1 lot (bought for ₹600) as a crash hedge. Delta **−0.45 × 30 = −13.5 (Bank units)**, gamma small +, theta **−₹1,800/day**, vega **+₹2,200 per vol pt**.

**Book so far (converting to a common ₹-per-point / ₹-per-vol frame):**
- Net delta: near flat on Nifty, short on Bank Nifty (a directional short-crash lean).
- Net gamma: **negative** (dominated by the straddle) — dangerous into expiry.
- Net theta: **+₹7,200/day** (straddle decay minus put bleed).
- Net vega: **−₹3,300/vol pt** (straddle short-vega minus put long-vega).

**The read:** I'm net short vol and short gamma. A calm grind pays me ₹7,200/day. A vol spike hurts (−₹3,300/vol pt) but the Bank Nifty put cushions it. My worst case is a *sharp Nifty move* (short gamma) on a *vol spike* (short vega) — a gap day.

**New trade decision.** I want more theta but I will *not* add more short vega/gamma — the book is already leaning that way. So instead of another short straddle, I add a **defined-risk, vega-light** position: a **Nifty iron fly converted toward a condor** is still short vega. Better: I add a **calendar spread** (sell weekly 24,000 CE, buy monthly 24,000 CE). A calendar is **long vega** and **positive theta** — it *reduces* my net short vega while still earning decay.

- Sell weekly 24,000 CE ₹120, Buy monthly 24,000 CE ₹260. Net debit ₹140 × 75 = ₹10,500/lot.
- Greeks: delta ~flat, theta **+₹2,500/day** (front decays faster), vega **+₹4,000/vol pt** (long the back month).

**New book Greeks:**
- Net delta: ~flat.
- Net theta: **+₹9,700/day**.
- Net vega: −3,300 + 4,000 = **+₹700/vol pt** — I've flipped from short vega to roughly vega-neutral while *increasing* theta.
- Net gamma: still short front (straddle) partly offset by calendar's short front gamma... net short gamma, smaller.

That's the craft: I added income without adding to my dominant risk. The calendar was chosen *because of the book's existing Greeks*, not on its own merit.

**Costs & margin.** Adding the calendar: margin blocked ~₹10,500 (near the debit, since it's a defined structure). Round-trip costs (4 legs, STT on the sold weekly, txn+GST) ~₹150/lot. Against +₹2,500/day theta over, say, 4 days = ₹10,000 potential, costs are a small drag.

## Management

**Daily book review (the routine).** Every morning before the open I mark net delta, gamma, theta, vega and check them against my caps. Overnight the Greeks drift — a Nifty move re-loads delta onto the short straddle (short gamma effect). If net delta has drifted beyond my band (say ±₹4,000/point), I **delta-hedge**: buy/sell Nifty futures or an ATM option to flatten. Delta-hedging a short-gamma book is a *cost* (you buy high, sell low), and that cost is the flip side of the theta you collect — budget for it.

**Scenario — Nifty gaps up 1.5% at open (360 pts).** Short straddle's short gamma means my delta has swung sharply negative; I'm losing on the up-move. The calendar's ATM strike is now OTM, changing its Greeks. Actions: (1) hedge delta with futures immediately to stop the bleed; (2) if VIX rose too, my vega-neutral book is roughly protected on vol; (3) decide whether the straddle's short strike needs rolling up. The Bank Nifty put is now further OTM (less protection) — I note the book is more exposed on a *reversal down*.

**Scenario — VIX spikes 12 → 18 on a global shock, spot flat.** Because I engineered net vega to ~+₹700, this *helps* me slightly on vol — a deliberate contrast to where I was before adding the calendar (−₹3,300 would have cost ₹19,800 on a 6-point spike). This is the entire point of managing book vega: the same spot outcome, opposite P&L, depending on aggregate vega.

**Scenario — margin expands.** As VIX rises, SPAN widens the scan range and my short-straddle margin jumps 30–50%. If I'm near my margin limit, the broker can force-liquidate at the worst moment. Defence: **run at ≤50–60% margin utilisation**, never 90%. The unused margin is not idle — it's the buffer that stops a vol spike from becoming a forced-liquidation cascade.

**Rolling and exits.** Weekly legs into expiry: square off ITM shorts before close to avoid exercise STT and assignment. Roll the calendar's short weekly to the next weekly if the thesis holds (collect fresh premium against the long back-month). Take the straddle off at a target (e.g., 40–50% of credit) rather than holding through expiry gamma.

## Risk & sizing

**Caps I trade to (illustrative, set your own):**
- Risk per trade ≤ 1% of capital; total open defined-risk ≤ 5–6% of capital.
- Net vega such that a **+5 VIX-point** shock costs ≤ 2% of capital.
- Net gamma such that a **2% overnight gap** costs ≤ 3% of capital *after* first-morning hedge.
- Margin utilisation ≤ 60% in normal regime, ≤ 40% when VIX is elevated (dry powder for margin hikes).
- Single-underlying concentration cap: no one index's positions risk more than X% — correlated crashes (Nifty and Bank Nifty fall together) mean "diversification" across indices is partly illusory.

**The tail — quantify it, don't hope.** Before every position I compute the **worst realistic gap**: Nifty −4%, VIX +8, overnight, no chance to hedge. If that scenario exceeds my capital's pain threshold at current size, I cut size *now*. Short-vol books die because they were sized to the median day and the tail arrived. The margin system will not save you — it *accelerates* the death via margin hikes. Only pre-sized risk saves you.

**Portfolio Greeks over single-trade Greeks.** Restate the whole discipline: a "delta-neutral, theta-positive" trade is meaningless in isolation if the book is already carrying ₹15,000/vol-pt of short vega. Judge every new trade by its **marginal contribution to net book Greeks**, not by its standalone profile. The calendar in the worked example was a bad trade in a vacuum (thin theta, tied-up capital) and an excellent trade *for that book* (it flattened vega).

## Pitfalls & interview-ready summary

**Pitfalls:**
- **Sizing off margin, not risk.** "Margin allows 20 lots" is not "I should do 20 lots." Size off max loss and a 1% rule.
- **Running high margin utilisation.** 90% utilisation + a VIX spike = forced liquidation at the bottom. Keep dry powder.
- **Managing trades, not the book.** Five neutral trades can all be short vega; the book is a concentrated vol bet nobody planned.
- **Ignoring dynamic margin.** SPAN margin *rises* as you lose — the system pro-cyclically forces you out. Plan for it.
- **Collecting theta blind to vega/gamma.** Positive theta is financed by negative vega and gamma; the bill comes on gap days.
- **Assuming index diversification.** Nifty, Bank Nifty, Fin Nifty crash together; correlated tail, not diversified.
- **Letting ITM shorts get exercised.** Square off to avoid exercise STT and assignment surprises.

**Interview-ready summary:** Position sizing and book-Greek management are the survival disciplines of options trading. NSE margin is portfolio-based SPAN + Exposure — hedged structures (spreads, condors, calendars) cost a fraction of naked shorts, and margin is *dynamic*, rising with volatility exactly when you're losing. Size off **risk, not margin**: lots = (capital × 1%) / max-loss-per-lot. Manage the **aggregate book Greeks** — net delta, gamma, theta, vega — not single-trade Greeks, because "neutral" trades often stack the same short-vega/short-gamma exposure. Positive theta is always financed by negative vega and gamma; the bill arrives on gap days. Keep margin utilisation moderate for the dry powder that survives SPAN margin hikes, cap net vega and gamma against defined shock scenarios, and quantify the worst realistic overnight gap before sizing. The Indian retail F&O loss statistics are dominated by undersized-buffer, oversized-short-vol books — the discipline in this chapter is the direct defence.
