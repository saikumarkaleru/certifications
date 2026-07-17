# Real Options Trade Case Studies (Wins & Losses)

*India F&O, 2026. Case studies are illustrative reconstructions built on realistic Nifty/Bank Nifty behaviour and 2026 cost rules — numbers are teaching examples, not tick-accurate history. Verify current STT (~0.10% options sell premium; ~0.125% ITM exercise intrinsic), lot sizes, and expiry calendar on NSE before trading.*

## The idea

Strategy chapters teach you the shape of a trade; case studies teach you what actually happens between entry and exit — the adjustments you didn't plan, the cost drag you underestimated, the day the thesis was right but the timing killed you. This chapter walks six full trades — three wins, three losses — each with entry rationale, live management, and a post-mortem. The losses matter more than the wins: in options, you learn risk from the trades that hurt, and the Indian F&O landscape is littered with traders who only studied the winning setups.

These earn their keep as pattern libraries. When you're mid-trade and Nifty is grinding against your short strike into expiry, you want a remembered analogue — "this is the 24,200 condor from the case studies; last time I rolled the untested wing and it saved the trade." The value is in the *management branches*, not the entry.

A running theme: **most of these outcomes were decided by management and sizing, not by the entry.** The winning strangle and the losing strangle had near-identical entries. The difference was what the trader did on day three.

## The mechanics

Each case follows the same skeleton so you can compare them:

| Field | What it captures |
|---|---|
| Thesis | Why the trade went on |
| Structure | Legs, strikes, premiums, net Greeks |
| Sizing | Lots vs capital, max loss |
| What happened | The move, IV, days |
| Management | Every adjustment, with reasoning |
| Exit & P&L | After all costs |
| Lesson | The transferable rule |

Costs assumed throughout (2026, verify): flat brokerage ~₹20/order, STT ~0.10% on options sell premium, exchange txn + SEBI + stamp + 18% GST on brokerage/txn. Multi-leg trades carry meaningful cost drag — flagged in each case.

## Worked trade

### WIN 1 — Iron condor that respected its exit (Nifty)

**Thesis.** Nifty 24,000, India VIX 13, range-bound week, no major events. Sell premium with defined risk.
**Structure.** Sold 24,200 CE ₹40 / bought 24,350 CE ₹13; sold 23,800 PE ₹38 / bought 23,650 PE ₹14. Net credit ₹51 × 75 = ₹3,825/lot. Delta flat, theta +₹14/lot/day, vega negative.
**Sizing.** ₹12 lakh capital, max loss ₹99 × 75 = ₹7,425/lot, 1% risk ≈ ₹12,000 → 1 lot (conservative; could justify 1–2).
**What happened.** Nifty drifted 23,900–24,120 for three sessions; VIX eased to 12. By Wednesday the condor marked at ₹22 to close.
**Management.** Pre-set rule: take profit at ~55% of max credit. At ₹22-to-close I'd captured ₹29 of the ₹51. **Closed the entire condor Wednesday afternoon** rather than holding for the last ₹22 into Thursday's expiry gamma and gap risk.
**Exit & P&L.** Gross +₹29 × 75 = ₹2,175. Costs (8 executions, STT on sells) ~₹170. **Net ≈ +₹2,005/lot.**
**Lesson.** The discipline was the *early exit.* Holding to expiry for the final ₹22 exposes you to a Thursday gap that can turn a +₹2,000 win into a −₹7,000 loss. The market pays you to leave the last bit on the table.

### WIN 2 — Long-vega calendar into an event (Bank Nifty)

**Thesis.** RBI policy in 9 days. Front-week Bank Nifty IV cheap (~14%), monthly IV likely to firm into the event. Buy time spread.
**Structure.** Sold weekly 52,000 CE ₹210, bought monthly 52,000 CE ₹520. Net debit ₹310 × 30 = ₹9,300/lot. Positive theta, **long vega**.
**Sizing.** Defined risk ~net debit; 2 lots on ₹15 lakh (₹18,600 at risk ≈ 1.2%).
**What happened.** Bank Nifty stayed near 52,000; front weekly decayed fast; monthly IV rose from 14% to 17.5% into policy week — long vega worked.
**Management.** Rolled the short weekly to the next weekly once (sold fresh ₹190), collecting a second round of decay against the long monthly. Held the monthly through the IV expansion.
**Exit & P&L.** Closed the spread for ₹430 (from ₹310 debit) after the vega expansion + two rounds of front decay. Gross +₹120 × 30 × 2 = ₹7,200; costs ~₹400. **Net ≈ +₹6,800.**
**Lesson.** Calendars are a *vega + theta* trade, not a directional one — they win when the underlying sits still *and* back-month IV firms. Choosing the structure because the book needed long vega (and the event supplied it) is the craft.

### WIN 3 — Debit put spread as a sized crash bet (Nifty)

**Thesis.** Overbought Nifty at 24,400, VIX complacent at 11, negative global cues building. Wanted downside with capped, small cost.
**Structure.** Bought 24,300 PE ₹90, sold 24,000 PE ₹38. Net debit ₹52 × 75 = ₹3,900/lot. Defined risk = debit; max value = 300 width.
**Sizing.** 2 lots, ₹7,800 at risk on ₹13 lakh (0.6%).
**What happened.** Nifty fell to 23,950 over two days on a global risk-off; VIX popped to 15 (helped the long leg's vega).
**Management.** At 23,980 the spread was near max value (~₹240). Rather than squeeze the last rupees near the 24,000 short strike (pin risk), **closed at ₹230.**
**Exit & P&L.** Gross +₹178 × 75 × 2 = ₹26,700; costs ~₹250. **Net ≈ +₹26,450.** Best risk/reward of the six — small defined cost, large payoff, because it caught a vol *and* direction move together.
**Lesson.** Buying spreads (not naked options) when IV is cheap gives asymmetric payoff without theta terror. The vertical caps cost so you can size to survive being early.

### LOSS 1 — Naked short strangle sized to the calm (Nifty)

**Thesis.** Same as Win 1's condor — range-bound, VIX 13 — but the trader went **naked** for more premium.
**Structure.** Sold 24,200 CE ₹40 + 23,800 PE ₹38. Credit ₹78 × 75 = ₹5,850/lot. **Undefined risk.** Margin ~₹1.8 lakh/lot.
**Sizing.** ₹12 lakh capital, **4 lots** because "margin allowed it" (₹7.2 lakh margin, 60% utilisation). No defined max loss computed.
**What happened.** Overnight global shock; Nifty gapped down 3.2% to 23,230 at open. VIX spiked 13 → 21.
**Management.** No pre-set stop. At the open the 23,800 puts were deep ITM and short gamma had blown the delta hugely negative; short vega compounded the pain as VIX doubled. SPAN margin **jumped**, triggering a margin call. Forced to buy back the puts near the panic low.
**Exit & P&L.** Puts bought back at ~₹620 (from ₹38); calls near worthless. Loss per lot ≈ (620 − 78) × 75 = ₹40,650. **× 4 lots ≈ −₹1,62,600** — a 13.5% capital hit in one gap, plus margin-call forced timing at the worst price.
**Lesson.** Every failure mode in one trade: **naked** (undefined tail), **sized off margin not risk** (4 lots), **no stop**, **short vega into a VIX spike**, **short gamma into a gap**, and **SPAN margin hikes forcing liquidation at the low.** The identical *entry* as the winning condor — the condor's long wings would have capped this at ₹7,425/lot. Defined risk was the whole difference.

### LOSS 2 — Right thesis, wrong timing: long straddle bleed (Bank Nifty)

**Thesis.** Expected a big Bank Nifty move "soon"; bought volatility.
**Structure.** Bought 52,000 CE ₹210 + 52,000 PE ₹230. Debit ₹440 × 30 = ₹13,200/lot. **Long gamma, long vega, deeply negative theta.**
**Sizing.** 2 lots, ₹26,400 at risk on ₹18 lakh (1.5%) — sizing was fine; *the structure* was the problem.
**What happened.** Bank Nifty chopped in a 400-point range for 5 sessions. No move. VIX drifted *down* 14 → 12 (vega hurt). Theta bled ~₹1,100/lot/day.
**Management.** The trader kept holding, "waiting for the move." Each day theta + falling IV eroded the premium. By expiry week the straddle was worth ₹250 (from ₹440).
**Exit & P&L.** Closed at ₹250. Loss ₹190 × 30 × 2 = **−₹11,400** plus ~₹200 costs. The move came the *following* week — after the position was dead.
**Lesson.** Being right on *direction eventually* is worthless if you're paying theta while you wait. Long premium is a bet on **magnitude AND timing AND IV** — all three. If you must be long vol, prefer cheaper structures (spreads, or buy when IV is genuinely low, not average) and set a time-stop: if the move hasn't come by day X, cut it.

### LOSS 3 — Over-adjusted a condor into a bigger loss (Nifty)

**Thesis.** Standard iron condor, Nifty 24,000, VIX 14. Fine entry.
**Structure.** Sold 24,200 CE ₹44 / bought 24,400 CE ₹16; sold 23,800 PE ₹42 / bought 23,600 PE ₹16. Credit ₹54 × 75. 2 lots.
**What happened.** Nifty trended up steadily to 24,180 — testing the call wall — over three sessions.
**Management (the mistake).** As spot approached 24,200, the trader **rolled the call spread up** to 24,350/24,550 for a small extra credit — but Nifty kept trending. Then rolled *again* to 24,500/24,700. Each roll added credit but also **added directional short exposure into a trend**, chasing the market up. The put spread, meanwhile, was left far OTM (its cushion wasted). Nifty closed expiry at 24,560.
**Exit & P&L.** The twice-rolled call spread finished near max loss. Net across all rolls: collected ~₹54 + ₹20 + ₹18 = ₹92 credit, but the final call spread lost ~₹150 width breached. **Loss ≈ (150 − 92) × 75 × 2 ≈ −₹8,700**, worse than if the original condor had simply been stopped when spot first hit 24,150.
**Lesson.** **Don't roll a tested wing repeatedly into a trend** — you're doubling down on being wrong and converting a defined-risk trade into a directional chase. The correct move when the call side is decisively breached: take the defined loss, or roll the *untested* (put) wing up toward spot to recentre — never keep pushing the losing wing further out chasing the trend.

## Management (cross-case synthesis)

Across the six trades, the branches that decided outcomes:

- **Exit discipline (Win 1, Win 3):** taking profit at 50–60% and not squeezing expiry-day gamma turned good marks into booked wins.
- **Structure choice for the book/event (Win 2):** picking a calendar because it supplied long vega into an event.
- **Defined vs undefined risk (Loss 1 vs Win 1):** the same entry, opposite outcome — long wings cap the tail.
- **Time-stops on long premium (Loss 2):** long vol needs a "if no move by day X, cut" rule.
- **Adjusting the right wing (Loss 3):** roll the *untested* side to recentre; never chase the tested side into a trend.

## Risk & sizing (what the losses teach)

The three losses map to the three classic Indian-retail F&O death modes:

1. **Naked short vol sized to calm** (Loss 1) — the account-killer. Margin permitted it; risk should have forbidden it. Defined-risk structures and 1% sizing are the fix.
2. **Long premium bleed** (Loss 2) — the slow death. Theta + IV decay grind out the buyer who has no time-stop.
3. **Over-adjustment** (Loss 3) — the self-inflicted wound. Rolling a losing wing into a trend converts a small defined loss into a large one.

Sizing rule reaffirmed: **lots = (capital × 1%) / max-loss-per-lot.** Loss 1's trader had 4 lots where risk allowed ~1 defined-risk lot; that 4× oversize turned a survivable event into a 13.5% drawdown. The tail is not hypothetical — Nifty gaps of 3%+ happen most years.

## Pitfalls & interview-ready summary

**Pitfalls:**
- **Copying winning entries without the management plan** — Win 1 and Loss 1 had the same entry.
- **Sizing naked shorts off available margin** — the fastest path to a blow-up.
- **No stop and no time-stop** — sellers need a loss stop; buyers need a time-stop.
- **Squeezing the last rupees into expiry gamma** — small extra gain, large gap risk.
- **Rolling the tested wing repeatedly into a trend** — doubling down on being wrong.
- **Ignoring vega on event weeks** — short vega into a VIX spike compounds a directional loss.

**Interview-ready summary:** Real trades are decided by management and sizing more than by entry. The winning cases shared exit discipline (book at 50–60%, don't squeeze expiry gamma), structure-fit (calendar for long vega into an event), and defined risk (spreads/condors cap the tail). The losing cases map to the three Indian-retail death modes: naked short vol sized to calm (blow-up on a gap + VIX spike + SPAN margin hike), long-premium theta bleed (right thesis, no time-stop), and over-adjustment (rolling the tested wing into a trend). The transferable rules: size off risk not margin (1% rule), prefer defined-risk structures, set both loss-stops and time-stops, adjust the *untested* wing to recentre, and always respect the negative-vega/negative-gamma tail that gap days expose.
