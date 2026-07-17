# DOM, Absorption & Iceberg Detection

The previous two chapters read the auction from *executed* trades — what already happened. This chapter looks at the other half: the **resting liquidity**, the orders sitting in the book *waiting* to happen. That live ledger of unfilled limit orders is the Depth of Market, or DOM. Learning to read it — and specifically to spot the moments when a big passive player is quietly *absorbing* everything thrown at them, or hiding size behind an **iceberg** — is the most execution-intensive skill in technical analysis. It is also the one where the Indian market's structure, and the plague of spoofing, demand the most humility. This chapter teaches the read and is blunt about the traps.

## What it is and the logic

The DOM (also "the ladder," "market depth," or "Level 2") is a vertical price ladder. Down the middle run prices. On one side, at each price *above* the current market, sit the resting **offers** (sellers' limit orders); on the other side, at each price *below*, sit the resting **bids** (buyers' limit orders). Each row shows the *quantity* of contracts resting at that price. The best bid and best offer are the top of the book; NSE disseminates depth for the best five price levels to most retail feeds (and 20 levels on some paid feeds).

The logic is a mirror image of order-flow logic. Executed trades (CVD, footprint) measure **aggressors** — the market orders that cross the spread. The DOM shows **passive liquidity** — the limit orders that aggressors trade *against*. And here is the crucial insight that CVD's blind spot pointed at: **the passive side decides who wins.** Price moves up only when aggressive buyers exhaust the resting offers. If a passive seller keeps *replenishing* the offer faster than buyers can eat it, price stalls no matter how hard buyers push. That is **absorption**, and the DOM is where you see it happen in real time — the offer at 48,600 keeps showing 5,000 lots no matter how many trades print against it.

An **iceberg order** is absorption's stealth version: a large order that displays only a small "tip" in the book (say 500 lots shown) while a hidden reserve (maybe 10,000) refills the visible quantity each time it's hit. The book *looks* thin; the reality is a wall. Detecting icebergs — inferring hidden size from the *pattern of refills and executions* rather than the displayed number — is the DOM reader's signature skill.

## Construction, rules and settings

### Anatomy of the ladder

| Column | Meaning |
|---|---|
| Price | The ladder rung (one tick / grouped ticks) |
| Bid size | Resting buy limit quantity at that price |
| Offer size | Resting sell limit quantity at that price |
| Volume / trades | Executed volume printing at each price (some DOMs overlay this) |
| Delta / imbalance | Live net aggression at each rung (advanced DOMs) |

Two numbers change constantly: the **resting sizes** (as orders are added/pulled) and the **prints** (as trades execute). Reading the DOM is watching the *interaction* between them.

### What genuine absorption looks like

You are watching the best offer at 48,600 in Bank Nifty. It shows 4,800 lots. Aggressive buyers hit it: prints of 300, 800, 1,200 flash by — clearly thousands of contracts are trading — yet the displayed 4,800 *barely drops, or drops and instantly refills to 4,800 again*. Price does not tick up. **That is absorption / an iceberg.** A passive seller is refilling the offer as fast as it's consumed. The tell is the mismatch: **large executed volume + stable displayed size + no price progress.**

### Iceberg detection heuristics

You cannot see hidden size directly. You *infer* it:

1. **Refill signature:** the displayed quantity at a price is repeatedly consumed and *reappears at the same number* (e.g. always snaps back to 500). Genuine natural liquidity varies; an iceberg's tip is mechanically constant.
2. **Executed-vs-displayed ratio:** track cumulative volume printing *at one price* versus what the book ever displayed there. If 9,000 lots executed at 48,600 but the book never showed more than 500, ~8,500 was hidden. Order-flow platforms (Bookmap, Quantower, ATAS, Sierra) automate this and often paint an "iceberg" marker.
3. **Price refuses to break** despite obvious sustained aggression against the level.
4. **Time:** an iceberg holds a level for *minutes* while volume piles up, not seconds.

### Absorption vs a plain thick book

A statically thick offer that *nobody is hitting* is not absorption — it's just size resting. Absorption requires **active consumption that fails to move price**. No prints against it, no absorption story.

### Settings and platform reality (India)

- **Depth available:** NSE gives best-5 depth by default; 20-level depth needs a paid feed (e.g. via a broker's tick API or a data vendor). Best-5 is enough to see the top-of-book absorption but misses the deeper wall.
- **Platforms:** Bookmap-style heatmaps (which render resting liquidity as a color-intensity map over time — the single best iceberg-hunting view), Quantower, ATAS, GoCharting, and some broker DOMs. TradingView's basic depth is too shallow for serious DOM work.
- **Instruments:** liquid futures only — Nifty, Bank Nifty, Fin Nifty, USDINR on the currency segment, top MCX contracts (Crude, Gold). Illiquid books are un-readable and easily manipulated.

## Worked India example (levels and ₹)

USDINR futures, currency segment — chosen because the DOM there is dense and reads cleanly. Say USDINR is at **83.42**, tick 0.0025, lot USD 1,000 (so one tick ≈ ₹2.50/lot; traders carry hundreds of lots). But let's stay with an equity-index example for familiarity.

Bank Nifty futures, price pinned at **48,600** — prior-day high and a strike with heavy call-writer OI. On the ladder:

- Best offer 48,600 shows **3,500 lots**.
- Over four minutes, prints against 48,600 total roughly **22,000 lots** — you can watch the tape scroll — yet the displayed offer keeps snapping back to ~3,500 and price never closes a full tick above 48,600.
- Meanwhile the bid side below (48,580, 48,560) is *thinning* — buyers pulling, not adding.

**Read:** a large passive seller (an iceberg, almost certainly an option desk hedging short calls at 48,600) is absorbing ~22,000 lots of aggressive buying. The buyers are spending all their ammunition into a wall. When aggression finally exhausts, price has nowhere to go but down.

**Trade:** short as price rolls back below 48,590 (first tick the offer *stops* refilling and price releases), stop at 48,615 above the absorbed wall — risk 25 points = ₹375/lot. Target VWAP / value-area low at 48,420 — 170 points = ₹2,550/lot, ~6.8:1. The DOM gave the *earliest* possible read — earlier than the footprint (which confirms after the bar closes) and earlier than CVD (which just shows fading net delta). On 20 lots: ~₹51,000 for ₹7,500 risk.

**Counter-case (the trap):** the same 3,500-lot offer sits there, price hits it, and it **vanishes the instant buyers arrive** — pulled, not filled — then price rips through 48,600 to 48,700. That was **spoofing**: a fake wall designed to make you short into a breakout. The distinguishing test is always *did volume actually execute against it?* Absorption = consumed and refilled. Spoof = displayed then pulled with little execution. If you can't confirm real prints ate the size, assume spoof.

## How to trade it

### Setup 1 — Absorption fade at a level
- **Location:** PDH/PDL, VWAP band, big option strike.
- **Trigger:** sustained real prints against a refilling offer/bid with no price progress → iceberg inferred.
- **Entry:** the moment price *releases* off the wall (offer stops refilling). **Stop:** just beyond the wall. **Target:** VWAP / opposite value edge. High R because stops are tick-tight.

### Setup 2 — Iceberg as support (join, don't fade)
- If a *buy* iceberg absorbs selling at 48,400 and holds, that level becomes support. Buy the hold with a stop just below — you're trading *with* the big passive player, often the higher-probability side.

### Setup 3 — Liquidity-vacuum breakout
- On a Bookmap heatmap, when resting liquidity *ahead of price thins out* (a vacuum), aggression meets little resistance and price travels fast. Enter on the break into the thin zone; target the next thick liquidity shelf.

**Management:** DOM trades are execution-grade — seconds-to-minutes holds, tight stops, scale out fast. If the wall you faded *reappears against you* (fresh opposing iceberg), exit. Never widen a DOM stop; the whole edge is that the level should hold or you're immediately wrong.

## Confluence

- **Footprint + DOM:** the footprint *confirms* after the bar what the DOM *suggested* live — absorption seen forming on the ladder, then proven by the bar's bid/ask split. The strongest order-flow combination.
- **CVD:** fading net delta *plus* a visible refilling wall = the passive side is winning, seen from both sides.
- **Options OI:** a wall at a heavy-OI strike is the highest-conviction absorption — you know *who* is likely defending it (option writers hedging) and *why*.
- **VWAP / value area:** absorption at a value-area edge reverts to VWAP with good odds.

## Pitfalls

1. **Spoofing and layering.** The DOM's original sin. Displayed size can be entirely fake — placed to deceive, cancelled before execution. SEBI prohibits manipulative order placement, and genuine spoofing is rarer in regulated NSE than in some venues, but *apparent* walls that pull are common (algos managing risk, not necessarily illegal spoofing). **Never trust displayed size alone. Only executed volume is real.** If size vanishes without prints, it was never liquidity.
2. **Shallow depth on retail feeds.** Best-5 depth hides the deeper book. You may fade a top-of-book wall while a bigger opposing wall sits two rungs away, unseen.
3. **Snapshot feeds.** If your depth updates on a snapshot interval rather than every change, fast refills and pulls blur together — you literally cannot see the iceberg's mechanics. Real DOM trading needs genuine tick/depth data.
4. **Latency.** By the time a retail order routes to the exchange, a fast iceberg or a pulled spoof has already changed. You are always slightly behind the co-located algos. Size and stops must respect that you're not first in the queue.
5. **Confirmation bias / tape-reading fatigue.** Stare at a ladder long enough and you'll "see" absorption everywhere. Require the objective test — real prints, stable-refilling display, no price progress — before acting.
6. **Illiquid instruments.** DOM reading on a thin midcap future or far option is worse than useless; a single order distorts the whole ladder and manipulation is trivial.
7. **Mistaking a thick book for absorption.** Resting size that isn't being hit means nothing. Absorption *requires* active consumption.
8. **Over-leverage on a "sure" wall.** Because DOM entries feel so precise, traders over-size. The wall can be spoofed, pulled, or simply overwhelmed by a bigger aggressor. Size for the case where you're wrong in three ticks.

## Interview-ready summary

The Depth of Market (DOM/Level 2/ladder) displays *resting* limit-order liquidity — the passive side of the auction that aggressive orders trade against and that ultimately decides who wins. **Absorption** occurs when a large passive player refills a bid or offer as fast as aggressors consume it, so heavy volume executes with no price progress; an **iceberg** is its stealth form, displaying only a small constant "tip" while a hidden reserve refills. You detect icebergs by inference — a mechanically constant refill size, cumulative executed volume far exceeding anything ever displayed at that price, and price's stubborn refusal to break despite sustained aggression — best seen on a Bookmap-style liquidity heatmap. In Indian markets, trade the DOM only on liquid futures (Nifty, Bank Nifty, Fin Nifty, USDINR, liquid MCX), fade absorption *as price releases off the wall* with tick-tight stops beyond it, or join a supporting iceberg with the big passive player, always in confluence with footprint, CVD, VWAP, and option OI. The non-negotiable discipline is skepticism of displayed size: only **executed volume is real** — size that vanishes without prints is spoofing or risk-management cancellation, not liquidity. Combined with shallow retail depth, snapshot feeds, and latency versus co-located algos, this makes DOM the highest-skill, highest-humility instrument in the technical toolkit — an execution edge for the disciplined and a hall of mirrors for the careless.
