# Chapter 40: Straddles — Long & Short

Suppose Nifty results season is here. A big event is coming — the RBI policy, the Union Budget, a major company's earnings, an election result — and you are *certain* the market is going to move hard. There is just one problem: you have no idea which way. Up? Down? A coin toss. A directional bet (a plain call or put) is useless to you, because being right on the size of the move but wrong on the direction still loses. What you want is a position that does not care about direction at all — it only cares that the market *moves*. That position exists, and it is called the **straddle**.

A straddle is the cleanest pure bet on **volatility** rather than direction. Buy one (a **long straddle**) and you win if the market makes a big move either way, or if fear and uncertainty (implied volatility) spike. Sell one (a **short straddle**) and you win if the market sits still and the storm everyone feared never arrives. This chapter takes you through both sides — the rupee mechanics, the breakevens, the Greeks, and the single most expensive trap that catches beginners: the **IV crush** that vaporises a long straddle even when you got the move right.

## Core concepts

### What a straddle is

A **straddle** is two options bought (or sold) together:

- one **call** and one **put**,
- on the **same underlying**,
- at the **same strike** `K`,
- with the **same expiry**.

Almost always the strike chosen is **at-the-money (ATM)** — the strike closest to the current spot price. That is what makes a straddle a *neutral* position: with an ATM call and an ATM put together, the call's positive delta (roughly +0.5) and the put's negative delta (roughly -0.5) cancel out, leaving you with **near-zero net delta** at inception. You are not leaning bullish or bearish. You are leaning on *movement itself*.

Because the two legs share a strike and expiry, the position has a memorable V-shaped (or inverted-V) payoff. You pay (or collect) the **sum of the two premiums**, and everything flows from that single number.

### The long straddle: buying a big move

When you **buy a straddle**, you pay both premiums up front and you own both rights. You profit if the underlying moves far enough — in *either* direction — that one leg pays more than the *total* you spent on both.

The payoff at expiry is just the sum of a long call and a long put on the same strike:

`Payoff (long straddle) = max(S - K, 0) + max(K - S, 0) - (call premium + put premium)`

At expiry only one of the two `max(...)` terms can be positive (spot is either above or below the strike), so this simplifies to:

`Payoff = |S - K| - total premium`

where `|S - K|` is the absolute distance of spot from the strike. Read it in three zones:

- **Spot pins the strike** (`S = K` at expiry): both legs expire worthless. You lose the **entire** total premium. This is the worst case — the bottom of the V.
- **Spot moves but not enough**: `|S - K|` is positive but smaller than the total premium. You are recovering cost, still at a net loss.
- **Spot moves a lot**: `|S - K|` exceeds the total premium, and every further point in either direction is pure profit.

**The defining numbers of a long straddle:**

- `Total premium = call premium + put premium` — your maximum loss, paid up front, and it occurs only if spot finishes exactly at the strike.
- `Upper breakeven = K + total premium`
- `Lower breakeven = K - total premium`
- `Max loss = total premium` (capped, defined, no margin calls)
- `Max gain = unlimited` on the upside; **very large** (capped only by spot falling to zero) on the downside.

Notice the breakevens sit *one full total-premium away from the strike on each side*. The market does not just have to move — it has to move **more than the combined premium you paid**. That gap is the price of admission, and it is wide, because you bought *two* options.

### Why a long straddle is "long gamma, long vega"

Two Greeks dominate the long straddle, and understanding them is what separates a gambler from a trader.

**Long gamma.** Gamma measures how fast your delta changes as spot moves. A long straddle starts delta-neutral, but the moment spot moves, the position automatically tilts in the direction of the move — if spot rises, the call's delta grows and the put's shrinks, so your net delta turns positive; if spot falls, it turns negative. In effect, **the position keeps repositioning itself to face the move**, accelerating into profit. That is the gift of being long gamma: you make money from movement regardless of direction, and you make it *faster* the bigger the move.

**Long vega.** Vega measures sensitivity to implied volatility (IV). A long straddle owns two options, so it owns a lot of vega. If **India VIX** (the market's fear gauge) jumps — say uncertainty spikes before an event — both options inflate in value and the straddle gains *even if spot has not moved at all*. This is why a long straddle is also a clean way to bet that volatility is **about to rise**.

The cost of these two gifts is **theta** — time decay. A long straddle is **short theta**: you are paying for two wasting assets, and every day that passes without a move bleeds value out of both legs. The straddle is a race: the move (gamma) and the IV spike (vega) must arrive *before* theta eats your premium.

### The short straddle: selling calm

When you **sell a straddle**, you do the opposite. You sell the ATM call and the ATM put, **collect both premiums** up front, and bet that the market stays quiet — that it pins near the strike and that IV falls. You keep the premium as long as the market does not move far enough to overwhelm it.

The payoff is simply the mirror image:

`Payoff (short straddle) = total premium collected - |S - K|`

**The defining numbers of a short straddle:**

- `Max profit = total premium collected` — realised only if spot expires **exactly** at the strike.
- `Upper breakeven = K + total premium`
- `Lower breakeven = K - total premium` (same breakevens as the long straddle, by construction)
- `Max loss = unlimited` on the upside, **very large** on the downside.

The Greeks flip sign. A short straddle is **short gamma** (a move in either direction turns your delta *against* you — you get longer as the market falls and shorter as it rises, exactly the wrong way), **short vega** (you lose if IV rises, you win if it falls — an **IV crush** is your friend), and crucially **positive theta** (every quiet day, time decay drips premium into your pocket). The short straddle is the canonical "theta-positive, sell-the-overpriced-fear" trade.

### When to use each — and the honest warning

**Use a long straddle when:**

- A **known catalyst** is coming (Budget, RBI policy, big earnings, election count day) and you expect a violent move but cannot call the direction.
- IV is **still cheap** relative to the move you expect — i.e., you are buying volatility *before* the crowd bids it up. This is the critical condition. A long straddle bought when India VIX is already elevated and event premium is already priced in is a near-certain loser (see the IV-crush trap below).
- You think the market is *underestimating* how much something will move.

**Use a short straddle when:**

- IV is **rich** — option premiums are fat with fear, India VIX is high, and you believe the actual move will be smaller than what the market has priced in.
- You expect a **quiet, range-bound** period — for example, the days *after* a big event when the uncertainty has resolved and IV is collapsing.

**The tail-risk warning — read this twice.** A short straddle has **undefined, potentially catastrophic loss**. You collect a small, fixed premium in exchange for unlimited risk. One overnight gap — a surprise rate decision, a geopolitical shock, a circuit-breaker move — can produce a loss many times the premium collected. It is the textbook "picking up pennies in front of a steamroller." SEBI studies show roughly **9 in 10 retail F&O traders lose money**, and naked option selling is a fast lane into that statistic. Never sell a naked straddle without strict position sizing and a hard stop-loss plan. Many professionals never sell a *naked* straddle at all — they convert it into a defined-risk **iron butterfly** by buying protective wings (covered later).

### The IV-crush trap (why long-straddle buyers lose even when they are "right")

Here is the single most expensive lesson for straddle buyers in Indian markets, and it deserves its own section.

Before a known event — quarterly results, RBI policy, the Union Budget — everyone *knows* a move is coming, so everyone bids up option premiums in advance. **Implied volatility inflates**, sometimes dramatically: an ATM option that "should" cost ₹80 of time value might trade at ₹150 because the event premium is baked in. India VIX rises into the event.

Now the event happens and the uncertainty **resolves** — the unknown becomes known. The instant it does, IV **collapses**. This is the **IV crush** (or *vol crush*). Both legs of your long straddle lose a chunk of value *purely because vega fell*, independent of spot.

The trap: you can **call the move correctly** and *still lose money*. Suppose Nifty jumps 1.5% on Budget day — a real move — but you paid an inflated premium that priced in a 2.5% move. The IV crush deflates your remaining time value, and the realised move is smaller than what you paid for. You were right that "it would move," yet you lose, because **you overpaid for volatility that then evaporated.**

The professional discipline: a long straddle into a known event only works if you buy it **before** IV inflates (days ahead, when premiums are still cheap), or if the actual move **dwarfs** the priced-in expectation. Buying a straddle the morning of results, when VIX is already screaming, is paying top rupee for an asset about to be marked down. The crowd's fear is already in the price.

## Worked example (₹, Nifty)

Let us price a real Nifty straddle. Assume:

- **Nifty spot = 24,000**, a weekly expiry a few days out.
- The **24,000-strike call** trades at a premium of **₹120**.
- The **24,000-strike put** trades at a premium of **₹100**.
- **Nifty lot size = 75** (use the current exchange value; it changes over time).

You buy one straddle: long the 24,000 call at ₹120 and long the 24,000 put at ₹100.

**Step 1 — Total premium paid.**

`Total premium = 120 + 100 = ₹220 per unit`

In rupee terms for one lot: `220 * 75 = ₹16,500`. That is your **maximum loss**, paid up front, and it happens only if Nifty expires *exactly* at 24,000.

**Step 2 — Breakevens.**

`Upper breakeven = 24,000 + 220 = 24,220`
`Lower breakeven = 24,000 - 220 = 23,780`

Nifty must finish **above 24,220 or below 23,780** — a move of more than **220 points (about 0.92%)** in either direction — for the straddle to turn a profit at expiry.

**Step 3 — Outcomes at expiry.**

- **Nifty pins at 24,000:** both legs expire worthless. Loss = ₹220/unit = **₹16,500/lot**. Worst case.
- **Nifty rallies to 24,400:** the call is worth `24,400 - 24,000 = 400`; the put is worthless. Payoff = `400 - 220 = ₹180/unit` profit = `180 * 75 = ₹13,500/lot`.
- **Nifty crashes to 23,600:** the put is worth `24,000 - 23,600 = 400`; the call is worthless. Payoff = `400 - 220 = ₹180/unit` profit = **₹13,500/lot**. Note the symmetry — same profit for the same-sized move down.
- **Nifty drifts to 24,150:** only 150 points up, below the 220 breakeven. The call is worth 150, the put zero. Payoff = `150 - 220 = -₹70/unit` = **₹5,250 loss/lot**. You got the direction right but the move was too small.

**Step 4 — Now flip it: the short straddle.**

If instead you **sold** this straddle, you would collect **₹220/unit (₹16,500/lot)** up front. That is your maximum profit, kept in full only if Nifty pins 24,000 at expiry. Your breakevens are identical — 24,220 and 23,780 — but now they are the points beyond which you start *losing*. If Nifty gaps to 24,600 overnight, the call you sold is worth 600, and your loss is `600 - 220 = ₹380/unit = ₹28,500/lot` — already larger than the premium you collected, and **growing without limit** the further Nifty runs. That single sentence is the entire risk of short option selling.

![Figure: long straddle payoff](figs/long_straddle.png)

![Figure: short straddle payoff](figs/short_straddle.png)

## Common mistakes / risk note

- **Buying a straddle right before results when IV is already sky-high.** This is the IV-crush trap. You pay inflated premiums, the event resolves, vega collapses, and you lose even if the move goes your way. Check **India VIX** and the option's IV percentile *before* buying — if vol is already rich, the straddle is a bad buy.
- **Underestimating how far the market must move.** Beginners see "I profit if it moves either way" and forget the breakevens sit a *full combined premium* away from the strike. In the example above, Nifty had to move nearly 1% just to break even. A 0.5% move — which feels "big" intraday — still loses.
- **Forgetting theta on a long straddle.** Holding a long straddle through a quiet, sideways week is death by a thousand cuts. You own two wasting assets; if the move does not come *soon*, time decay grinds both to nothing.
- **Selling a naked short straddle without respecting the tail.** The premium feels like easy income on quiet days — until one gap blows through months of accumulated profit. Undefined risk is real risk. Size tiny, use stops, and seriously consider buying protective wings to cap the loss.
- **Ignoring transaction costs and margin.** A straddle is *four* legs of brokerage round-trip, plus **STT**, exchange fees, and GST. A short straddle also locks up substantial **SPAN + exposure margin** because the risk is large. These costs eat into thin edges.
- **Confusing a straddle with a strangle.** A straddle uses the *same* ATM strike for both legs (higher premium, narrower breakevens); a strangle uses *different* out-of-the-money strikes (cheaper, wider breakevens). Covered next chapter — do not mix them up.

## Key takeaways

- A **straddle** = a call and a put at the **same strike and expiry**, usually **ATM**. It is a bet on **movement (volatility)**, not direction — net delta starts near zero.
- **Long straddle**: buy both. Pay total premium; profit on a **big move either way** or an **IV spike**. Max loss = total premium (capped); breakevens = `strike ± total premium`; upside unlimited. It is **long gamma, long vega, short theta**.
- **Short straddle**: sell both. Collect total premium; profit if the market stays **quiet** and **IV falls**. Max profit = premium collected; **loss is undefined and potentially catastrophic**. It is **short gamma, short vega, positive theta**.
- The market must move **more than the combined premium** to make a long straddle pay — the breakevens are wide because you bought two options.
- The **IV-crush trap**: buying a straddle into a known event when IV is already inflated often loses *even if the move is correct*, because vega collapses once uncertainty resolves. Buy volatility when it is **cheap**, not after the crowd has bid it up.
- Sell straddles only when IV is **rich** and you expect calm — and **never naked without strict sizing and a stop**, given the tail risk that ruins most retail sellers.

## Practice problems

1. **(Conceptual)** Why does a long straddle have *near-zero* net delta at the moment you put it on, and what happens to that net delta if Nifty subsequently rallies 300 points? Which Greek is responsible for the change?

2. **(Numeric)** Bank Nifty is at 52,000. The 52,000 call costs ₹400 and the 52,000 put costs ₹350. Compute the total premium, both breakevens, and the percentage move from spot required to reach each breakeven.

3. **(Numeric)** Using the Bank Nifty straddle from Problem 2, find the expiry profit or loss per unit if Bank Nifty finishes at (a) 52,000, (b) 53,200, (c) 50,900.

4. **(Conceptual / risk)** A trader buys a Nifty ATM straddle the morning of the RBI policy announcement, paying a fat total premium because India VIX has spiked to 22. Nifty moves 0.8% on the news — a genuine move — yet the trader still loses money. Explain precisely why.

5. **(Numeric)** You **sell** a Nifty 24,000 straddle, collecting ₹120 (call) + ₹110 (put) = ₹230 total. Nifty gaps up overnight and opens at 24,520. What is your profit or loss per unit at that spot (ignore remaining time value)? How does this compare with your maximum possible profit?

6. **(Conceptual)** Two traders both expect a big Budget-day move in Nifty. Trader A buys the straddle three weeks before the Budget; Trader B buys the identical straddle on Budget morning. Both are "right" — Nifty moves sharply. Why might Trader A profit handsomely while Trader B barely breaks even or loses?

## Solutions

**1.** At inception the straddle is ATM, so the long call has a delta of roughly **+0.5** and the long put a delta of roughly **-0.5**. They sum to about **zero**, so the position is direction-neutral. If Nifty rallies 300 points, the call moves into-the-money (its delta climbs toward +1) while the put moves out-of-the-money (its delta drifts toward 0). The net delta therefore turns **positive** — the position automatically becomes bullish, leaning into the move. The Greek responsible is **gamma**: a long straddle is **long gamma**, so its delta shifts favourably with the direction of any move, which is exactly why it profits from movement either way.

**2.** Total premium = `400 + 350 = ₹750`.
Upper breakeven = `52,000 + 750 = 52,750`.
Lower breakeven = `52,000 - 750 = 51,250`.
Required move = 750 points each way. As a percentage of spot: `750 / 52,000 = 0.0144`, i.e. about **1.44%** up to reach 52,750, and about **1.44%** down to reach 51,250. Bank Nifty must move more than roughly 1.44% in either direction just to break even.

**3.** Total premium = ₹750. Use `Payoff = |S - K| - 750`.
(a) **S = 52,000:** `|52,000 - 52,000| - 750 = 0 - 750 = -₹750/unit`. Maximum loss — spot pinned the strike, both legs worthless.
(b) **S = 53,200:** `|53,200 - 52,000| - 750 = 1,200 - 750 = +₹450/unit` profit. (The call is worth 1,200; the put expires worthless.)
(c) **S = 50,900:** `|50,900 - 52,000| - 750 = 1,100 - 750 = +₹350/unit` profit. (The put is worth 1,100; the call expires worthless.)

**4.** This is the **IV-crush trap**. With India VIX at 22, the straddle's premium was inflated by **event premium** — the market priced in a large expected move, pumping both options' implied volatility and their time value. The moment the RBI decision was announced, the uncertainty **resolved**, and IV **collapsed** back toward normal. Both legs lost a large chunk of value from the **vega** (volatility) component alone. A 0.8% Nifty move is genuine, but it was *smaller than the move the inflated premium had priced in*. So the intrinsic value the trader captured from the 0.8% move was less than the premium lost to the IV crush. The trader was right about *movement* but **overpaid for volatility that then evaporated** — a net loss despite a correct read on direction.

**5.** As a short straddle seller you collected ₹230 up front. At expiry-equivalent with Nifty at 24,520, the **call you sold** is worth `24,520 - 24,000 = ₹520`; the put you sold is worthless. Your loss on the position = `value owed - premium collected = 520 - 230 = ₹290/unit loss`. Per lot of 75: `290 * 75 = ₹21,750 loss`. Compare this with your **maximum possible profit** of just ₹230/unit (₹17,250/lot), achievable only if Nifty had pinned 24,000. A single overnight gap of 520 points turned the maximum-₹230 gain into a ₹290 loss — and had Nifty opened even higher, the loss would keep growing without limit. This is the undefined tail risk of selling straddles in one number.

**6.** Trader A bought **three weeks early, before the event premium inflated IV** — paying a relatively cheap total premium. As the Budget approached, India VIX rose and option premiums fattened, so even before the move Trader A's straddle gained value from **rising vega**. When the sharp move arrived, A captured it on top of an already-cheap cost base — a handsome profit. Trader B bought **on Budget morning, at peak IV**, paying a fat premium that already discounted a large move. The instant the Budget resolved, **IV crushed**, deflating B's time value. Unless the realised move *exceeded* the move priced into B's inflated premium, B barely breaks even or loses. Same direction call, same straddle — opposite outcomes, driven entirely by **when each trader bought volatility relative to the IV cycle.**
