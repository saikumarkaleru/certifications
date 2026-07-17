# Market Profile: TPO (Deep)

If Auction Market Theory is the philosophy, the Market Profile is its instrument. Peter Steidlmayer's genius at the CBOT was to take the raw stream of an auction and re-organize it into a *statistical picture* of where the market spent its time — a picture that reveals value, excess and the shape of the day at a glance. This chapter goes deep on the TPO (Time Price Opportunity) construction specifically: how the letters are actually built, how to compute the value area and POC by hand, how to read profile *shapes*, and how to trade the structure on Nifty and Bank Nifty. We deliberately keep volume profile for its own treatment; here the currency is **time**, because time is what TPO measures and time is what regulates an auction.

## What it is and the logic

A TPO — Time Price Opportunity — is a single unit meaning "at this price, during this time period, there was an opportunity to trade." Divide the session into equal time brackets (classically 30 minutes) and assign each bracket a letter: A, B, C, D... For every price the market touched during bracket A, you print an "A" at that price on the vertical price axis. During bracket B, a "B" at every price it touched. And so on. Then you *collapse* all the letters leftward against the price axis. The result is a horizontal histogram lying on its side: prices where the market spent many brackets grow long rows of letters (the fat middle = value); prices touched in only one bracket stay as lonely single prints (the thin tails = excess).

The profound point: **time spent at a price is a proxy for acceptance of that price as fair.** A price the market revisited in eight different half-hours is a price both buyers and sellers keep agreeing to transact at. A price touched once and abandoned is a price the auction *rejected*. So the TPO count literally maps out where value lives and where the auction found its edges — exactly the AMT vocabulary, now made concrete and countable.

TPO is not the same as volume. Volume profile asks "how many contracts changed hands here?" TPO asks "how much *time* did the market spend here?" They usually agree, but their disagreements are informative — a price with high TPO but low volume was *lingered at* without conviction; high volume in few TPOs was a *fast, decisive* transaction. In this chapter, TPO time is our lens.

## Construction: building the profile by hand

Let us build a Nifty TPO profile explicitly. Assume Nifty futures, 30-minute brackets, NSE session 9:15–15:30, giving roughly these letters:

| Bracket | Time | Letter |
|---|---|---|
| 1 | 09:15–09:45 | A |
| 2 | 09:45–10:15 | B |
| 3 | 10:15–10:45 | C |
| 4 | 10:45–11:15 | D |
| 5 | 11:15–11:45 | E |
| 6 | 11:45–12:15 | F |
| 7 | 12:15–12:45 | G |
| 8 | 12:45–13:15 | H |
| 9 | 13:15–13:45 | I |
| 10 | 13:45–14:15 | J |
| 11 | 14:15–14:45 | K |
| 12 | 14:45–15:15 | L |
| 13 | 15:15–15:30 | M |

Now suppose the day's price ranges per bracket (rounded to a 5-point TPO row) were:

| Price | Letters present | TPO count |
|---|---|---|
| 24,090 | A | 1 |
| 24,085 | A B | 2 |
| 24,080 | A B C | 3 |
| 24,075 | A B C D | 4 |
| 24,070 | A B C D E K L | 7 |
| 24,065 | B C D E F K L M | 8 |
| 24,060 | C D E F G H K L M | 9 |
| 24,055 | D E F G H I J K L M | 10 |
| 24,050 | E F G H I J K L M | 9 |
| 24,045 | F G H I J K | 6 |
| 24,040 | G H I J | 4 |
| 24,035 | H I J | 3 |
| 24,030 | I J | 2 |
| 24,025 | J | 1 |

**Total TPOs** = 1+2+3+4+7+8+9+10+9+6+4+3+2+1 = **69**.

### Finding the POC

The **Point of Control** is the price with the most TPOs — here **24,055** with 10 letters. It is the longest row, the fairest price of the day, the price the auction kept coming back to. (When two prices tie, convention picks the one closest to the *centre* of the range.)

### Computing the Value Area (the 70% rule)

The Value Area contains roughly 70% of the day's TPOs, centred on the POC. The algorithm every profile platform uses:

1. Target = 70% × 69 = 48.3 → **48 TPOs**.
2. Start at the POC row (24,055 = 10 TPOs). Running total = 10.
3. Look at the *two rows above* and the *two rows below* the current value area. Compare the combined TPO count of the pair above vs the pair below. Add whichever pair is larger. Add both rows of the chosen pair.
4. Repeat until running total ≥ 48.

Working it:

- VA = {24,055} = 10.
- Above pair (24,060, 24,065) = 9+8 = 17. Below pair (24,050, 24,045) = 9+6 = 15. Above wins. Add both → VA = {24,065…24,055} = 10+9+8 = 27.
- Above pair (24,070, 24,075) = 7+4 = 11. Below pair (24,050, 24,045) = 9+6 = 15. Below wins. Add both → VA = {24,065…24,045} = 27+9+6 = 42.
- Above pair (24,070, 24,075) = 7+4 = 11. Below pair (24,040, 24,035) = 4+3 = 7. Above wins. Add both → VA = {24,075…24,045} = 42+7+4 = 53 ≥ 48. Stop.

So the **Value Area** runs from **24,045 (VAL)** to **24,075 (VAH)**, with **POC = 24,055**. That single computation — POC, VAH, VAL — is the backbone of every Market Profile trade. Notice the value area is slightly skewed *upward* of centre (it extends to 24,075 above but only 24,045 below): a subtle hint of buyer control late in the session (the K, L, M letters clustering high).

## Reading profile shapes

The *shape* of the collapsed profile is where TPO becomes an art. The main archetypes:

| Shape | Look | Meaning | Bias |
|---|---|---|---|
| **D / Normal** | Symmetric bell, fat middle | Balanced day, value found, two-sided | Range — fade edges |
| **b** | Long thin top, fat bulge at bottom | Selling then long liquidation stalling; longs trapped | Often bearish / unfinished lower |
| **P** | Fat bulge at top, thin tail below | Short-covering rally then balance up high | Often bullish / unfinished higher |
| **Trend / thin** | Elongated, no fat middle, POC in centre of a long line | One-timeframe trend day | Go with the trend |
| **Double distribution (B)** | Two separate bulges joined by thin single prints | Two value areas in one day; market moved and re-based | Breakout from one to the other |

The **b-shape** and **P-shape** deserve care because they signal *unfinished business*. A P-shape (short covering) means the down-auction stopped and shorts bought back, but no *new* long initiative pushed higher — the thin tail below is unfinished, price may revisit it. A b-shape is the mirror: long liquidation stalled, the thin top is unfinished. These are among the most tradable TPO reads because they point to where the market must still "clean up."

The **double distribution** is a workhorse Nifty pattern: the market balances in the morning around, say, 24,050, then in the afternoon a news catalyst drives it to a new balance around 24,180, with only single prints in between (24,090–24,150). Those single prints are a *fast, un-auctioned zone* — a gap in value that becomes a magnet if price returns, and a support/resistance shelf if it holds.

## Worked India example: trading the profile on Bank Nifty

Take Bank Nifty futures. Yesterday closed with a clean D-day: POC 51,400, VAH 51,550, VAL 51,250. Today:

**Open.** Bank Nifty opens at 51,600 — *above* yesterday's VAH. Immediately this is an AMT event: the auction is opening above value. The first job is acceptance vs rejection.

**First hour (A, B brackets).** Price trades 51,560–51,700 and *holds* above yesterday's VAH of 51,550. TPOs build at 51,620–51,660. This is acceptance above value — initiative buying. Today's developing POC forms near 51,640.

**The setup.** By midday the profile is building a P-shape: a fat bulge 51,600–51,700, thin prints trailing down toward 51,560. P-shape = short-covering that has now based higher, and the thin lower tail is unfinished. The play:

- *Entry:* buy the pullback into the developing value area — say a dip to 51,610 (into the bulge / above yesterday's VAH which now acts as support).
- *Stop:* below yesterday's VAH turned support and below where acceptance is disproven — ~51,530 (back *inside* yesterday's value). Risk ≈ 80 points.
- *Target 1:* the day's high extension / a measured move; *Target 2:* the next naked reference above, say a prior swing at 51,900. Reward ≈ 290 points to T2, roughly 3.6R.
- *Management:* as long as value keeps building higher (VAL migrating up), hold. The moment the profile fattens symmetrically into a D (balance returns), the trend has paused — take partials.

**Contrast — the failure.** Had Bank Nifty opened at 51,600 and then *fallen back below* 51,550 in the second bracket on expanding volume, the "above value" open would be *rejected* — a failed auction. You would flip: short the re-entry into yesterday's value, target yesterday's POC (51,400), because the market advertised higher, found no buyers, and must now re-auction down toward accepted value.

## How to trade it: the core TPO playbook

**Where today opens relative to yesterday's value is the master variable.** Four cases:

| Open location | Interpretation | Default plan |
|---|---|---|
| Inside prior value | Balanced, low conviction | Expect rotation; fade toward POC |
| Above prior VAH | Potential initiative up | Watch acceptance; if held, long pullbacks |
| Below prior VAL | Potential initiative down | Watch acceptance; if held, short pullbacks |
| Gap far outside value | Strong initiative *or* fade-the-gap | Acceptance = trend; rejection = gap fill to value |

**Rotations inside value.** In a balanced D-day, price rotates between VAL and VAH around the POC. Sell near VAH, buy near VAL, POC is the target and the pivot. The POC is a battle line: trade *above* it leans long, *below* leans short intraday.

**Value-area relationships day to day.** This is the highest-value TPO habit:
- *Higher value + overlapping* = mild bullish drift.
- *Higher value + non-overlapping (gap up in value)* = strong bullish, trend.
- *Overlapping-to-higher / unchanged* = balance, expect rotation and a possible range trade.
- *Lower value* mirrors the above bearishly.

**Naked POC.** A prior POC that price left and never returned to is a naked/virgin POC — a strong magnet. Many intraday Nifty targets are simply the nearest naked POC.

## Confluence

- **TPO value edges + volume profile HVN/LVN.** When the TPO VAH lines up with a volume High-Volume Node, the level is doubly reinforced. A Low-Volume Node (thin volume) inside a double distribution's single prints is a fast zone price slices through.
- **Single prints + swing levels.** TPO excess (single-print tails) at a prior swing high/low or round number (Nifty 24,000; Bank Nifty 51,000/51,500) is a high-grade rejection.
- **Open type + first-hour range.** The open's location relative to value, combined with the initial balance (next chapter), tells you which shape is likely to form.
- **F&O / OI.** A TPO POC coinciding with the highest-OI strike (a "gravity" strike) is a powerful magnet into expiry. Heavy call writing above the VAH confirms it as resistance; heavy put writing below the VAL confirms support.

## Pitfalls

- **Bracket-size sensitivity.** 30-minute brackets are the classic, but on fast Indian index futures some traders use 15-minute or even volume-based brackets. Change the bracket and the shape changes. Pick one and be consistent, and know that very short brackets over-fragment the picture.
- **Reading the shape before the day is mature.** A P-shape at 10:00 can morph into a D by 14:00. Early shapes are hypotheses, not conclusions. Weight late-session structure more.
- **The 70% is a convention, not physics.** Some platforms use volume-based value areas or a different % ; the *relationships* (higher/lower/overlapping value) matter more than the exact tick of the VAH.
- **Ignoring the composite.** A single day inside a three-week balance is noise. Always keep a weekly / multi-day composite profile alongside the daily — is today happening at the top, middle, or bottom of the bigger auction?
- **Expiry distortion (India-specific).** On weekly/monthly F&O expiry, index auctions get pinned toward high-OI strikes; the TPO can look artificially balanced around max-pain. Read expiry-day profiles with extra scepticism.
- **Thin instruments.** As with AMT, TPO needs genuine time-and-price two-way activity. It sings on Nifty, Bank Nifty, Fin Nifty, liquid MCX and USDINR; it is nearly meaningless on an illiquid stock where whole brackets have no trades.
- **Confusing TPO with volume.** Time at price ≠ conviction at price. A long TPO row on thin volume is a *lingering* market, not a *convinced* one — cross-check with volume when the stakes are high.

## Interview-ready summary

The Market Profile re-organizes a session's auction into a horizontal, time-based histogram. Each 30-minute bracket gets a letter (A, B, C…), a letter is printed at every price touched in that bracket, and collapsing the letters leftward produces a distribution: a fat middle where the market spent time (value) and thin tails where it did not (excess). The three numbers you compute are the **POC** (longest TPO row — the fairest price), and the **VAH/VAL** bounding the ~70% Value Area, found by expanding from the POC, two rows at a time, adding the larger pair until 70% of TPOs are captured. Profile *shapes* carry meaning: D = balance (fade edges), b/P = unfinished business (revisit the thin tail), thin/elongated = trend (go with it), double distribution = two value areas joined by fast single prints. The master trading variable is **where today opens relative to yesterday's value** and whether a move beyond value is *accepted* (time and volume build — go with it) or *rejected* (snaps back — fade it), with day-over-day value relationships (higher/lower/overlapping) giving the swing bias. TPO measures *time*, a proxy for acceptance; its power is turning the abstract idea of "value" into three concrete, tradable levels, and its main hazards are bracket-size sensitivity, premature shape-reading, expiry distortion, and the need for genuinely liquid instruments — in India, the index futures, liquid MCX and USDINR.
