# Value Area & Value Migration

Volume I introduced the raw shape of a Market Profile — the bell-curve of TPO letters, the Point of Control, the fat middle and the thin tails. This chapter goes past shape and into *behaviour*. The Value Area is not a decoration on the profile; it is the single most tradeable object auction theory produces, and the way it **migrates** from session to session is a running commentary on who is winning the fight between buyers and sellers. Master value migration and you stop asking "is this level support?" and start asking "is value moving toward my trade or away from it?" — a far more honest question.

We will build the Value Area precisely, then spend most of the chapter on migration: the four canonical developing-value patterns, how to read them live on Nifty and Bank Nifty, and a complete trade framework with entries, stops and targets in rupees.

## What it is & the logic

The **Value Area (VA)** is the price range that contains a defined share — conventionally **70%** — of a session's traded activity. In a TPO (Time-Price-Opportunity) profile you count letters; in a volume profile you count contracts/shares. The 70% comes from the statistical convention that one standard deviation either side of the mean of a normal distribution captures roughly 68–70% of the observations. The market is not truly Gaussian, but over a single well-formed auction it is close enough that the 70% band reliably brackets the prices the market agreed were "fair".

Three landmarks define the object:

- **Value Area High (VAH)** — the upper boundary of the 70% band.
- **Value Area Low (VAL)** — the lower boundary.
- **Point of Control (POC)** — the single price with the most TPOs or the most volume; the fairest of the fair, the price the auction returned to most often.

The logic that makes VA tradeable is **acceptance versus rejection**. Inside the Value Area, price is *accepted* — both sides transact willingly, the auction rotates, mean-reversion dominates. Outside the Value Area, price is on *trial*. The auction has pushed into an area where, so far, activity is thin. Either that thin area gets filled with time and volume (acceptance — value is about to migrate) or price is thrown back inside (rejection — the excursion was a probe, not a move). Every Value Area trade is a bet on which of those two outcomes is unfolding.

**Value migration** is simply the day-over-day (or bar-over-bar, in developing form) movement of VAH, VAL and POC. If today's entire Value Area sits above yesterday's, buyers have re-priced the instrument higher and *held* it there — that is far stronger evidence of a trend than any single green candle. Migration is the auction's way of saying "the old fair price is stale; here is the new one."

## Construction, rules & settings

### Building the 70% band (TPO method)

1. Split the session into time brackets (30 minutes each is the classic; on NSE's 09:15–15:30 cash session that gives brackets A–M). Bank Nifty futures run 09:15–15:30 too.
2. For every 30-min bracket, mark a TPO letter at each price it traded.
3. Count total TPOs. Multiply by 0.70 — that is your target count.
4. Find the POC — the price row with the most TPOs.
5. From the POC, walk outward. Compare the two rows immediately above your current band with the two immediately below; add whichever *pair* has more TPOs. Repeat, alternating, accumulating rows until the accumulated count reaches or exceeds the 70% target.
6. The highest and lowest prices included are VAH and VAL.

### Volume method (what most traders actually use in 2026)

TradingView's "Volume Profile" and the fixed-range/session-volume tools do the same walk using **traded volume per price** instead of letter counts. For F&O instruments this is superior because it weights by size, not just time. Settings that matter:

| Setting | Typical value | Note |
|---|---|---|
| Value Area Volume | 70% | Keep the convention; changing it breaks comparability |
| Row size / ticks per row | Auto or 24–50 rows | Too fine = noisy POC; too coarse = imprecise VAH/VAL |
| Profile type | Session (per day) | Use "Session" for daily migration analysis |
| Data source | Futures, not spot | Nifty **futures** carry volume; the spot index has none |

**Critical India note:** the Nifty 50 and Bank Nifty *indices* have no volume — they are computed numbers. To build a volume profile you must load the **futures** (NIFTY1! / BANKNIFTY1! continuous, or the current-month contract) or a liquid proxy. TPO profiles can be built on the index because they count time, not volume, but for serious value work use futures.

### Developing Value Area (the live object)

Intraday, the Value Area is **developing** — recomputed after each completed bracket. This is where migration is read in real time. A developing POC that drifts steadily higher through the day (developing-value-up) tells you the auction is migrating before the session even closes. Chartink can't draw this, but TradingView's session volume profile with "developing VA" enabled will.

## Worked India example (levels & ₹)

Take a two-day Bank Nifty futures sequence. Round numbers for clarity.

**Day 1** — a balanced, rotational session:
- High 48,650, Low 48,050
- POC 48,350
- VAH 48,520, VAL 48,180
- Value Area width ≈ 340 points; a classic "D-shaped" balanced profile.

**Day 2 opens at 48,600** — *above* Day 1's VAH of 48,520. This is an **open-outside-value, above** condition. The first question of the session: will 48,600 be accepted (value migrates up) or rejected (fade back into Day 1 value)?

By 10:15 (three brackets in), the developing profile shows:
- Developing POC 48,610
- Developing VAL 48,540 — note this is *above* Day 1's VAH.

The auction has built a fresh 70% band entirely above yesterday's value and has not traded back below 48,520. That is **higher-value acceptance**. By close, Day 2 settles:
- POC 48,720, VAH 48,880, VAL 48,560.

Day 2's *entire* Value Area (48,560–48,880) sits above Day 1's (48,180–48,520). Value has cleanly migrated up ~370 points on the POC. A trader who bought the accepted breakout of Day 1's VAH at ~48,540, with a stop back inside Day 1 value, rode the migration.

Now suppose instead Day 2 had opened at 48,600 and by 10:15 the developing POC had sagged to 48,510 with price printing back at 48,300 — *inside* Day 1's Value Area. That is **rejection**: the open above value failed, price re-entered the prior balance, and the highest-probability target becomes the prior POC (48,350) and then the far side (VAL 48,180). This is the single most reliable Market Profile intraday trade: **open outside value that fails re-enters and rotates to the opposite extreme.**

The rupee arithmetic on Bank Nifty: one futures lot is 15 units (2026 lot size — always confirm the current lot on NSE). A 370-point migration captured on one lot ≈ 370 × 15 = **₹5,550** gross. On the rejection rotation, 48,600 → 48,350 POC is 250 points ≈ **₹3,750**; carrying to VAL 48,180 is 420 points ≈ **₹6,300**.

## How to trade it (entry, stop, target, management)

Auction theory gives you a small number of high-quality setups. Here are the four that revolve around value and migration.

### 1. Value-Area rotation (fade the edges of balance)

**Context:** an established, balanced day — wide VA, price rotating, no migration. Trade the extremes back to POC.

| Element | Rule |
|---|---|
| Entry | Sell into VAH / buy into VAL, only after a rejection tail forms at the edge |
| Stop | Just beyond the session extreme (not just beyond VAH — beyond the *high*) |
| Target 1 | POC |
| Target 2 | Opposite value edge |
| Invalidation | Acceptance (two brackets) outside VA → this is now a breakout, not a rotation |

### 2. Failed-auction / open-outside-value fade

**Context:** open above prior VAH (or below prior VAL) that fails to find acceptance and re-enters prior value.

| Element | Rule |
|---|---|
| Trigger | Price trades back *inside* yesterday's VA after opening outside |
| Entry | On the re-entry through yesterday's VAH (short) or VAL (long) |
| Stop | Above the session high (short) — the excursion extreme |
| Target | Prior POC first, prior opposite edge second |

### 3. Value-migration continuation (trade *with* migrating value)

**Context:** developing value is stepping in one direction — higher POC each bracket, VAL not overlapping the prior bracket's VAL.

| Element | Rule |
|---|---|
| Entry | Buy pullbacks into the *developing* VAL or developing POC as long as it keeps rising |
| Stop | Below the developing VAL of the bracket you entered on |
| Target | Prior day's range extension / measured move; trail using developing VAL |
| Kill switch | Developing POC turns down two brackets in a row → migration stalling |

### 4. Poor-high / poor-low retest

A **poor high** is an auction extreme with multiple TPOs (a flat, "unfinished" top rather than a single-print spike). Poor highs tend to be revisited because the auction never found a genuine buyer to reject the level. Fade rallies *into* a poor high with a tight stop above; the market usually comes back to repair it.

**Position sizing across all four:** risk a fixed fraction (say 0.5–1% of capital) to the *structural* stop, never a fixed point stop. A rotation trade with a 60-point stop on Bank Nifty (60 × 15 = ₹900/lot) and a migration trade with a 140-point stop (₹2,100/lot) should carry different lot counts so both risk the same rupees.

## Confluence

Value and migration are strongest when they agree with independent tools:

- **Prior-day levels & Naked POC:** an untested POC from a previous session ("virgin" or naked POC) acts as a magnet — price is statistically drawn back to repair it. Migration *toward* a naked POC is high-conviction.
- **VWAP:** covered fully in the next two chapters. When the session VWAP sits inside the developing Value Area and both are rising, longs have two independent institutional references agreeing.
- **Open type:** an *Open-Drive* (price leaves the open and never returns) almost always precedes strong value migration; an *Open-Auction-in-Range* precedes rotation. Read the open type first.
- **Options OI:** if value is migrating up toward a strike with heavy call OI (a resistance wall), expect migration to *stall* there; if it migrates through it, the short-covering unwind can accelerate the move. Overlay the OI max-pain and the migrating POC.
- **Initial Balance (IB):** the first hour's range. Range extension beyond the IB in the direction of migrating value confirms trend-day conditions.

## Pitfalls

- **Using the index, not the futures, for volume profiles.** Nifty/Bank Nifty spot has no volume; your "volume POC" on the index is fiction. Load futures.
- **Treating VAH/VAL as hard lines.** They are zones. A two-tick poke through VAH is not acceptance; two full brackets of trade above it is. Wait for time.
- **Ignoring the open location.** The same VAH means completely different things if today opened above it (potential migration) versus below it (potential rejection). Always frame today relative to yesterday's value *and* the open type.
- **Comparing profiles with different row sizes.** If yesterday's profile was drawn at 24 rows and today's auto-scaled to 50, your POCs aren't comparable. Lock the setting.
- **Fading strong migration.** In a trend day, "buy VAL" gets run over. Developing value that steps consistently one way is telling you rotation trades are switched off — trade continuation instead.
- **Holiday and expiry distortion.** Thin pre-holiday sessions and expiry-day gamma pinning produce misshapen profiles with unreliable value. Down-weight them.
- **Over-fitting the 70%.** Don't tinker with the percentage to make a level "work." The value of the convention is that everyone uses it, so it becomes a shared reference.

## Interview-ready summary

The Value Area is the 70% band of a session's activity, bounded by VAH and VAL around the Point of Control, and it encodes where the market agreed price was fair. Inside value, mean-reversion dominates; outside value, price is on trial and must be either accepted or rejected. **Value migration** — the day-over-day drift of VAH/VAL/POC — is the cleanest read of trend in auction theory: entire value shifting up on non-overlapping bands is genuine higher re-pricing, not noise. The four core trades are rotation (fade balanced edges to POC), the failed-auction fade (open-outside-value that re-enters rotates to the far side), migration continuation (buy pullbacks into rising developing value), and poor-high/low retests. On Indian markets, always build volume profiles on **futures**, frame every session against yesterday's value and the open type, and use naked POCs, VWAP and options OI as confluence. The professional question is never "is this support?" but "which way is value migrating, and is my trade going with it or against it?"
