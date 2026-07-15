# Case Study: The Volatility Crush (Buying Options Before Events)

*Price and IV levels below are approximate reconstructions of real event sessions; pull up the actual option chain history to verify — the transferable lesson is the mechanic of IV run-up and collapse, not the exact premiums.*

Here is the trap that catches more thoughtful retail traders than any other: you correctly predict the direction, the stock moves your way, and your long option still loses money. The culprit is implied volatility (IV) — the market's price of expected movement, baked into every option premium through vega. Before a known event, IV inflates because the outcome is uncertain. The moment the event passes, uncertainty vanishes and IV collapses — the "volatility crush," or "IV crush." If your long option's IV bleed outweighs its directional gain, you lose while being right.

## Case A — Right on direction, wrong on vega (a large-cap results day)

**The setup.** A heavyweight IT large-cap (think an Infosys/TCS-scale name) reporting quarterly results after market hours. Stock trading around ₹1,600 the morning of results. The Street expected a move but was split on guidance. In the days before results, the at-the-money options had bid up: the weekly ₹1,600 call was quoting around ₹55, carrying an implied volatility of roughly 42% — well above the stock's usual ~24% baseline. That gap, 42% vs 24%, is the "event premium" you are paying for.

**Price-action & IV walkthrough.**

| Moment | Stock | ATM 1,600 CE | Implied vol | What it means |
|--------|-------|--------------|-------------|----------------|
| 2 days before | ₹1,595 | ~₹48 | ~38% | IV climbing into the event |
| Results morning | ₹1,600 | ~₹55 | ~42% | Peak event premium — most expensive point |
| Next open (gap up) | ₹1,648 | ~₹52 | ~22% | Stock up 3%, IV collapsed to baseline |

Read the last row slowly. The stock rose ₹48 — a solid 3% up-move, exactly what a call buyer wanted. Yet the ₹1,600 call *fell* from ₹55 to ₹52. Why? At results morning the option had ~₹0 intrinsic and ~₹55 of time+event value. Next day it had ₹48 of intrinsic but the time+event value had crushed from ₹55 to ₹4, because IV halved from 42% to 22% and a day of theta burned off. Intrinsic gain (+₹48) minus extrinsic loss (−₹51) ≈ a small net loss.

**The trade.** A retail buyer, bullish on results, bought 2 lots of the ₹1,600 CE at ₹55 the morning of results. Lot size, say, 300 (illustrative for this name). Cost = 55 × 300 × 2 = ₹33,000. No stop possible overnight — the whole bet was the gap.

**What happened.** Results were "good but priced in." Stock gapped to ₹1,648. The buyer, expecting a windfall, opened to find the call at ₹52 — down ₹3. Exiting: 52 × 300 × 2 = ₹31,200. Loss ≈ ₹1,800 before costs, more like ₹2,100 after brokerage/STT/GST — despite a correct, decisive directional call. The buyer needed the stock above roughly ₹1,655 (strike + premium paid) *at the crushed IV* just to break even; a 3% move wasn't enough because they overpaid for volatility.

**The lesson.** You did not buy the stock; you bought a *volatility contract*. Paying 42% IV and receiving 22% after the event means you bought high and the vega instantly repriced against you. The professional's rule: never be a net buyer of options into a known, scheduled event unless you expect a move *larger than the one the IV is already pricing in*. The break-even move implied by 42% IV was far bigger than 3%.

## Case B — Selling the crush (the other side of the same trade)

**The setup.** Same stock, same results, but a seller's view: "the market is overpaying for this move." Instead of buying the inflated call, this trader sold a strangle to harvest the crush — short the ₹1,660 CE (~₹35) and short the ₹1,540 PE (~₹32), collecting ₹67 of inflated premium. Break-evens: below ₹1,473 and above ₹1,727 — a wide band the stock would have to blow through to hurt them.

**IV walkthrough.**

| Moment | Stock | 1,660 CE | 1,540 PE | Implied vol |
|--------|-------|----------|----------|-------------|
| Results morning | ₹1,600 | ~₹35 | ~₹32 | ~42% |
| Next open | ₹1,648 | ~₹14 | ~₹3 | ~22% |

**The trade.** Sold 1 lot each. Credit = (35 + 32) × 300 = ₹20,100. Margin roughly ₹3–3.5 lakh for the short strangle. The risk was a monster gap beyond a break-even; the reward was the IV collapse.

**What happened.** Stock gapped to ₹1,648 — a real move, but inside the band. Next morning the call was ~₹14 (still some intrinsic-adjacent value on the ₹1,660 strike but crushed) and the put was ~₹3. Buying both back: (14 + 3) × 300 = ₹5,100. Profit = 20,100 − 5,100 = ₹15,000 gross, ~₹14,600 after costs. The seller was *less right on direction* than the Case A buyer — the stock went up, threatening the call — yet made money because vega collapsed in their favour.

**The lesson.** The buyer and the seller watched the *same* 3% up-move. The directionally-correct buyer lost ₹2,100; the seller made ₹14,600. The difference was entirely which side of the volatility crush they were on. That is the whole point: around events, vega often dominates delta.

The honest caveat on Case B: the seller was exposed to a fat tail. Had the stock gapped 12% on a shock (a guidance bombshell, an accounting issue), the short call could have exploded and the loss would have dwarfed the ₹20,100 credit. Selling the crush is profitable *on average* precisely because it carries that tail — which is why professionals cap it (spreads, iron condors) rather than selling naked. We treat that failure mode in its own case study.

## Transferable rules

- **An option's price has two engines** — direction (delta) and volatility (vega) — and around scheduled events vega frequently overpowers delta, so being right on direction guarantees nothing.
- **Check IV before you buy, not just the chart** — if ATM IV is far above the stock's baseline, you are paying an event premium that will crush the instant the event passes.
- **The break-even is the IV's implied move** — only buy into an event if you expect a bigger move than the premium is already pricing; otherwise you need a miracle just to break even.
- **The volatility crush is a harvestable edge for sellers**, but it comes attached to a fat tail — collect it with *defined-risk* structures (spreads/condors), never naked, and size for the shock gap.
- **"I was right and still lost" is a vega lesson, not a bad-luck story** — internalise it once and you stop donating premium to event sellers.
