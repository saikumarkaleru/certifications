# Case Study: Anatomy of a Blown Account

*Price levels are approximate reconstructions of a real pattern; the numbers here are a realistic composite built from common retail behaviour and SEBI's published F&O-loss data — pull up your own broker statement to verify. The transferable value is the mechanics and the lesson, not the exact ticks.*

This chapter is not about one heroic trade. It is about the slow, ordinary way a ₹5,00,000 account dies. SEBI's studies on individual F&O traders (FY22 and the FY24 update) found that roughly 9 in 10 lose money, that the average loser lost over ₹1,00,000 in a year, and that the most active traders lost the most. Those are not exotic gamblers. They are ordinary people repeating five or six behaviours. Below is a composite trader — call him Rahul, ₹5,00,000 capital, a full-time job, trading Nifty and Bank Nifty weekly options from his phone — walked week by week down to zero. Every mistake here is one the data says is common.

## The setup

- **Trader:** Rahul, ₹5,00,000, opened with a discount broker in early 2026.
- **Instrument:** Nifty and Bank Nifty weekly options — bought and sold, mostly buying out-of-the-money (OTM) calls and puts because "they're cheap and they move fast."
- **Context:** A choppy, range-bound couple of months on the index — exactly the environment that quietly bleeds option buyers through theta (time decay) while feeling like "it should break out any day."

## Price-action walkthrough — the equity curve down

| Week | Account start | What Rahul did | Account end |
|------|--------------|----------------|-------------|
| 1 | ₹5,00,000 | Bought 10 lots Nifty OTM calls on a "breakout" that failed | ₹4,55,000 |
| 2 | ₹4,55,000 | Won on a Bank Nifty put — felt invincible, sized up | ₹5,10,000 |
| 3 | ₹5,10,000 | Held expiry-day OTM longs, they went to zero | ₹4,20,000 |
| 4 | ₹4,20,000 | Averaged a losing call twice, index kept falling | ₹3,25,000 |
| 5 | ₹3,25,000 | Revenge-traded after the loss, 3 trades same day | ₹2,60,000 |
| 6 | ₹2,60,000 | Acted on a Telegram "sure-shot" tip, no stop | ₹1,80,000 |
| 7 | ₹1,80,000 | Doubled lot size "to recover faster" | ₹95,000 |
| 8 | ₹95,000 | All-in on expiry lottery ticket | ₹12,000 |

Eight weeks. No single catastrophic trade — just compounding of the same errors.

## The trade — where it turned from bad luck into a blown account

Look at Week 3 and Week 4, the real turning point. On Wednesday of expiry week, Nifty sat around 24,000. Rahul held 10 lots (each lot 75) of the 24,200 CE bought at ₹85. That is 10 × 75 × 85 = ₹63,750 of premium — about 12.7% of his remaining capital riding on one out-of-the-money option into expiry.

- **Entry:** 24,200 CE at ₹85, 10 lots (750 qty).
- **Stop-loss:** none. "It's an option, my risk is already limited to the premium."
- **Target:** "If Nifty hits 24,400 this doubles."
- **Risk in ₹:** the *entire* ₹63,750 — because with no stop and one day to expiry, the realistic outcome for an OTM long that doesn't move is total loss.
- **R-multiple:** undefined, because he never defined R. That is the whole problem.

Nifty drifted to 23,950 by close. The 24,200 CE expired near ₹2. He got back roughly ₹1,500. A ₹62,000 loss on one position — not from a crash, just from theta and a market that did nothing.

Then Week 4: instead of stopping, he "averaged." Bought more of a falling call at ₹40, then again at ₹18, telling himself his average cost was now "much better." The index kept sliding. Averaging a losing directional option is buying more of a decaying asset that the market is voting against — it turns a defined small loss into an undefined large one.

## What happened — the exit and the real P&L after costs

By Week 8 the account was ₹12,000 — down 97.6%. Costs quietly accelerated the fall. Rahul never counted them, but they were real:

- **STT** on options (2026: 0.1% of premium on sell for options), **brokerage** (flat ~₹20/order but he was placing 8-15 orders on busy days), **exchange fees, GST, stamp duty.**
- On a heavy revenge-trading day (Week 5) he did 14 round-trip orders. Even at ₹20 flat + statutory charges, that is roughly ₹500-₹700 gone in costs alone before the market moved — on an account already under ₹3,00,000. Over eight weeks his total transaction cost drag ran into the tens of thousands. SEBI's data makes the same point at scale: after costs, the aggregate losses balloon, and the most active traders pay the most in charges.

There was no dramatic exit. The account just became too small to trade meaningfully, and Rahul stopped — the most common "exit" of all.

## The lesson

**What the professional sees:** Rahul was never beaten by the market's direction. He was beaten by his own **position sizing and his refusal to define risk before entering.** A professional risks a fixed, small fraction (0.5-1%) of capital per trade — on ₹5,00,000 that is ₹2,500-₹5,000 of *actual* risk, not ₹63,750. At that size, no single trade and no bad week can end you. The professional also treats a bought option's premium as real risk capital, uses a hard stop (an exit price or a max-loss rupee figure), never averages a losing directional bet, and counts every cost.

**What the typical retail trader did wrong — the checklist of ruin:**
1. **Over-leverage in weekly options** — putting 10-25% of capital on single OTM lottery tickets.
2. **No stop-loss** — hiding behind "limited risk," which for an OTM buyer means the limit is 100%.
3. **Averaging losers** — pouring good money into a decaying, wrong-way position.
4. **Revenge trading** — trying to win the money back *today*, multiplying both losses and costs.
5. **Tip-based entries** — outsourcing decisions to Telegram/"sure-shot" calls with no plan or exit.
6. **Ignoring costs and theta** — treating friction and time decay as free.

Each one alone is survivable. Stacked together, they are the anatomy of a blown account — and they are exactly what the SEBI numbers describe across millions of real traders.

## Transferable rules

- **Define your risk in rupees before you click buy.** If you can't state your max loss, you don't have a trade — you have a bet.
- **Cap risk at ~1% of capital per trade.** On ₹5,00,000 that is ~₹5,000. Size the position to fit the stop, never the stop to fit the position.
- **Never average a losing directional option.** Adding to a decaying, wrong-way position converts a small planned loss into an account-ending one.
- **One loss does not need to be repaid today.** Revenge trades and "double up to recover" are how a drawdown becomes a blow-up.
- **Count costs and theta as real.** STT, brokerage and time decay are always working against the option buyer — trade rarely enough that friction doesn't eat your edge.
