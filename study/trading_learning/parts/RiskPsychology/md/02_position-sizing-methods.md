# Position Sizing Methods

## Why this matters — the pro vs retail gap this closes

Retail traders decide size by asking "how many lots can my margin buy?" Pros ask "how many units keep my loss at 1R if the stop hits?" That single inversion is the difference between a controlled book and a random one. Two traders with the *same* winning strategy will have wildly different equity curves purely from sizing — one compounds smoothly, the other rides a rollercoaster to zero. Sizing is the throttle; the strategy is only the engine. This chapter gives you the methods and the exact arithmetic to convert a stop into a quantity across cash and F&O.

## The essentials — the methods, India-specific

**1. Fixed-fractional (fixed % of equity).**
Risk a constant fraction — say 1% — of *current* equity each trade. As the account grows, rupee risk grows; as it shrinks, risk shrinks automatically. This is the professional default because it compounds gains and decelerates losses.

**2. Fixed-rupee-risk-to-stop (THE core method).**
This is the workhorse. 

> **Quantity = Rupee Risk Budget ÷ (Entry − Stop) per unit**

- Cash equity: Qty (shares) = Risk ₹ ÷ (Entry − Stop).
- Futures/options: the "per unit" risk is *per point × lot size*. Number of lots = Risk ₹ ÷ (Stop distance in points × lot size × points-value).

Everything else is a refinement of this.

**3. Volatility / ATR-based sizing.**
Set the stop at a multiple of **ATR** (Average True Range, e.g. 14-period) so the stop breathes with the instrument. Stop distance = *k* × ATR (k ≈ 1.5–2.5). Then size with the core formula. Benefit: a quiet stock gets a tight stop and a bigger position; a wild one (say Adani-name volatility) gets a wide stop and a small position — **risk stays constant at 1R across both.**

**4. Kelly & fractional Kelly.**
Kelly gives the growth-optimal fraction: **f\* = W − (1−W)/RR**, where W = win rate, RR = avg win/avg loss. Full Kelly is far too aggressive (huge drawdowns), so pros use **fractional Kelly — a quarter to a half of f\***. If Kelly says 20%, you risk 5%. In practice, for retail F&O, Kelly usually confirms that 0.5–1% is sane and that anything above ~5% is gambling.

**5. Pyramiding (scaling in).**
Add to *winners*, never losers. Take the first tranche at entry; add a second only after price moves in your favour and you can trail the stop so total open risk stays ≤ 1R. Done right, average size rises only when the trade is already right.

**F&O margin note (verify on broker/NSE — rules change, as of 2026):** upfront **SPAN + Exposure** margin is blocked per lot, peak-margin fully enforced. Margin determines *whether you can hold* the position; it must **never** determine your size. Your size is set by the stop. If the stop-based size needs more margin than you have, the trade is too big for the account — skip it, don't oversize to fit.

## Worked example — size-from-stop across cash and F&O

**Capital ₹5,00,000, risk 1% = ₹5,000 = 1R.**

**(a) Cash equity — Reliance.** Entry ₹2,900, structure stop ₹2,850 → stop distance ₹50.
- Qty = 5,000 ÷ 50 = **100 shares.** Position value = ₹2,90,000 (use MTF/delivery; verify STT: delivery 0.1% buy+sell from 01-Apr-2026).
- If stop hits: 100 × ₹50 = −₹5,000 = −1R. Correct.

**(b) ATR-based — a midcap at ₹800, ATR(14) = ₹25, stop = 2×ATR = ₹50 below → ₹750.**
- Qty = 5,000 ÷ 50 = **100 shares.** Wider ATR would mean fewer shares — risk held at 1R.

**(c) Nifty futures.** Lot size **75** (verify — lot sizes change), point value = ₹75/point. Entry 24,000, stop 23,920 → 80 points.
- Risk per lot = 80 × 75 = **₹6,000.** That is 1.2R > 1R → **1 lot is already slightly over budget.** Either tighten the stop, or accept 1 lot only if you flex to a 1.2% day-limit — never take 2 lots (₹12,000 = 2.4R).

**(d) Bank Nifty options — buying an ATM call at ₹250, lot 35.** You define a stop on the *option* at ₹100 premium loss (₹250→₹150).
- Risk per lot = 100 × 35 = **₹3,500 = 0.7R.** You could take **1 lot** comfortably; a 2nd lot = ₹7,000 = 1.4R > 1R, so no. Premium × lot also sets margin (buyers pay full premium: ₹250×35 = ₹8,750 per lot).

Notice: in every case **quantity fell straight out of the stop distance.** You never asked "how many lots can I afford."

## How pros do it / common mistakes

**Pros:**
- Use fixed-fractional on equity + fixed-risk-to-stop on every trade; ATR-set the stop when volatility varies.
- Cap at fractional Kelly, treating 1% as the norm and 2% as a hard ceiling.
- Pyramid only into open profit with total risk trailed back to ≤1R.
- Recompute the 1R rupee figure monthly as equity changes.

**Retail errors & red flags:**
- **Margin-based sizing** ("₹1L free margin, so 3 lots") — the single most common blow-up cause.
- **Constant lot count** (always "2 lots") regardless of stop distance — risk swings wildly trade to trade.
- **Full Kelly / all-in** on a "sure" setup — a 30% drawdown from one bad expiry.
- **Averaging down** and calling it "pyramiding" — it is the opposite; you're adding to a loser.
- Selling naked options sized by margin — one gap converts a "high-probability" ₹5,000 credit into a ₹50,000 loss.

## Checklist / drill

**Sizing checklist:**
- [ ] Stop level chosen from structure/ATR *before* size.
- [ ] Qty = Risk₹ ÷ (per-unit stop distance). Written down.
- [ ] For F&O: lots = Risk₹ ÷ (points × lot size × point-value). Rounded *down*.
- [ ] Resulting margin ≤ available? If not, trade is too big — skip, don't shrink the stop.
- [ ] Any add-on keeps total open risk ≤ 1R.

**Drill:** Take 10 real setups this week. For each, write entry, ATR-based stop, and compute quantity by the core formula. Then check what you *would have* traded by gut. Log the gap. Most traders discover their gut size is 2–4× the correct size — that ratio *is* your blow-up risk.
