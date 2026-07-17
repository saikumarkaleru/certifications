# CANSLIM (Technical Side)

CANSLIM is William O'Neil's growth-stock framework, distilled from a study of the biggest winning stocks in American market history at *Investor's Business Daily*. The name is an acronym for seven characteristics that great winners shared *before* they made their large moves. Four of those letters are fundamental (Current earnings, Annual earnings, New products, Institutional sponsorship), and three are essentially technical (Supply-and-demand, Leader-or-laggard, Market direction). This chapter deliberately concentrates on the **technical machinery** of CANSLIM — the chart reading, the base structures, the pivot buy points, the relative-strength ranking, and the sell rules — because that is the part a technical trader executes, and it is the part most often botched by people who read the fundamentals and then buy at the wrong price. We will translate the whole apparatus into the Indian context: NSE stocks, rupee pivots, Nifty as the "M", and screens you can build on Chartink and TradingView.

The core CANSLIM thesis is that a stock about to run 100-300% does not do so from a random point. It emerges from a **recognisable price structure** (a "base") at a **specific pivot**, on **expanding volume**, while it is a **relative-strength leader**, and while the **general market is in an uptrend**. Get those four technical conditions to line up on top of real earnings growth, and you have a repeatable, high-conviction entry with a tight, definable stop. Miss any one of them — especially "M" — and the same fundamentally great stock will chop you to pieces.

## What it is and the logic

CANSLIM's technical premise rests on **institutional footprints**. A stock that will triple cannot be pushed there by retail buyers; it needs mutual funds, insurance companies, FIIs, and DIIs accumulating for months. That accumulation leaves marks on the chart: tight, orderly price ranges (institutions absorbing supply without paying up), volume drying up on pullbacks (weak holders shaken out, strong hands unwilling to sell), and then sudden volume surges when the stock clears resistance (institutions forced to chase). O'Neil's genius was to name and standardise these structures so a chartist could spot the *same* pattern across decades — from the 1900s railroads to modern tech.

The three technical letters:

- **S — Supply and Demand.** Read through volume and float. Big up-days on big volume = demand; down-days on light volume = shrinking supply. Smaller floats (fewer shares outstanding) move faster.
- **L — Leader or Laggard.** Only buy the #1 or #2 stock in a leading sector. Measured by **Relative Strength (RS) Rank** — a 1-99 percentile of the stock's 12-month price performance versus the whole market. Demand RS Rank ≥ 80, ideally ≥ 90.
- **M — Market Direction.** Roughly three of four stocks follow the general market. So you only take fresh breakout buys when the index (Nifty 50 for us) is in a confirmed uptrend, not a correction.

The "buy high, sell higher" philosophy is the emotional hurdle. CANSLIM asks you to buy a stock at a **new high** or just below it — precisely when it feels expensive — because new highs signal an absence of overhead supply (no trapped sellers waiting to break even). This is the opposite of bargain-hunting, and it is the single most important mental shift.

## Construction: bases, pivots, and RS

### The base structures

A **base** is a sideways consolidation where the stock digests a prior advance and institutions accumulate. O'Neil catalogued a handful. The three you must know:

| Base type | Duration | Depth (correction) | Shape / logic |
|---|---|---|---|
| Cup-with-handle | 7 weeks to 65 weeks | 12-35% (up to 50% in bear-born bases) | Rounded "U" cup, then a short downward-drifting "handle" in the upper half; handle shakes out the last weak holders |
| Flat base | 5+ weeks | ≤ 15% | Tight horizontal rectangle; usually forms *after* a stock has already broken out of a prior base ("base-on-base") |
| Double bottom | 7+ weeks | 12-35% | "W" shape; the second low undercuts the first low by a fraction (the shakeout), pivot is the middle peak |

The **pivot** (or "pivot buy point") is the precise price where the stock signals the base is complete and demand has overwhelmed supply. For a cup-with-handle it is **10 paisa (₹0.10) above the high of the handle**. For a flat base it is 10 paisa above the base's high. For a double bottom it is 10 paisa above the middle peak.

### The handle rules (cup-with-handle)

The handle is where most people get the pivot wrong. Proper handles:
- Form in the **upper half** of the cup (a handle in the lower half is a red flag — too much weakness).
- **Drift downward** along a slight downtrend, not upward (an upward-wedging handle fails more often).
- Show **volume drying up** — the driest volume in the whole base often appears in the days just before the breakout.
- Are relatively short (1-2 weeks typically) and shallow (correction of 8-12% from the handle high, measured peak-to-trough of the handle).

### The breakout confirmation

A valid pivot breakout requires **volume at least 40-50% above the stock's 50-day average volume** on the breakout day, and ideally 100%+. Volume *is* the confirmation. A breakout on average or light volume is suspect — it is more likely to fail or become a "false breakout" that traps buyers.

### Relative Strength line and RS Rank

Two different tools with a confusingly similar name:
- **RS line** = stock price ÷ index (Nifty) plotted as a line. When this line makes a **new high before the price itself does**, it is a powerful "blue dot"/leadership signal — the stock is outperforming the market even during the base.
- **RS Rank** = a 1-99 percentile ranking of trailing performance. IBD's formula weights the most recent quarter double: roughly `RS = 0.4×Q1 + 0.2×Q2 + 0.2×Q3 + 0.2×Q4` of price change, then percentile-ranked across the universe.

You can approximate RS Rank on Chartink or TradingView by ranking your NSE universe on 6-month or 12-month returns and taking the top 20% (rank ≥ 80).

## Worked India example (levels and ₹)

Let us construct a realistic CANSLIM setup on a mid-cap NSE name. Assume **"Company X"** — a capital-goods stock riding an order-book upcycle — trading through 2025.

**The base.** X ran from ₹380 to ₹640 over five months (a prior uptrend that qualifies it — CANSLIM bases form *after* an advance, off a "proper" prior move of 30%+). It then corrected into a cup:
- Left side of cup high: **₹640** (this is the eventual resistance / rim).
- Cup low: **₹470** — a correction of (640−470)/640 = **26.6%**, within the healthy 12-35% range.
- The cup rounds out over 11 weeks and rallies back to **₹625**, just below the rim.
- A handle then forms: X drifts from ₹625 down to **₹588** over 8 trading days — a handle correction of (625−588)/625 = 5.9%, shallow and orderly, in the upper half of the cup. Crucially, volume in the handle shrinks to well below the 50-day average.

**The pivot.** Handle high = ₹625. Pivot buy point = **₹625.10** (₹625 + 10 paisa). In practice you set an alert at ₹625 and act on the intraday clearance.

**The breakout.** On a Nifty up-day, X gaps to ₹628 and closes at ₹641 on volume of 4.1x its 50-day average (its 50-day avg is ~9 lakh shares; the breakout day trades 37 lakh). The RS line, meanwhile, punched to a new high two weeks *before* price — a textbook leadership tell. RS Rank sits at 94.

**Entry.** You buy the pivot clearance around **₹626-632**. CANSLIM discipline: never chase more than **5% above the pivot**. 5% of ₹625 = ₹31.25, so your maximum buy zone is ₹625-656. At ₹641 you are 2.6% extended — fine. If X had rocketed to ₹700 (12% past pivot) intraday, you would **pass** and wait for the next base; extended buys have terrible risk/reward.

**Stop.** O'Neil's rule: cut every loss at **7-8% below the buy point**, no exceptions. Buy at ₹632 → stop at ₹632 × 0.92 = **₹581.44** (round to ₹581-582). Note the stop sits just below the handle low of ₹588, which is logical support. If X breaks ₹581 you are out — the base has failed.

**Targets and management.** CANSLIM is a trend system; you do not set a fixed target but manage the trend:
- Take partial profits at **+20-25%** unless the move is explosive. ₹632 × 1.20 = ₹758.
- **The exception that makes the system:** if a stock rises **20% within the first 1-3 weeks** out of a proper base, you *hold at least 8 weeks* — such power signals a potential huge winner. X hits ₹759 (+20%) in nine trading days → apply the 8-week hold rule.
- Trail using the **21-day EMA** for fast movers or the **50-day SMA / 10-week line** for the primary trend. Sell when price closes decisively below the 50-day on heavy volume.

## How to trade it: entry, stop, target, management

The mechanical checklist for pulling the trigger:

1. **M first.** Is Nifty 50 above its 50-day and 200-day, with the 50-day above the 200-day, and no recent distribution cluster (see below)? If Nifty is in a correction, **do nothing** regardless of how good the stock looks.
2. **Base quality.** Is there a proper base (cup/handle, flat, double-bottom) of correct depth and duration, formed after a real prior advance?
3. **Pivot defined.** Mark the exact pivot (10 paisa above handle/peak high).
4. **RS check.** RS Rank ≥ 85 and RS line at/near new highs.
5. **Volume trigger.** Breakout volume ≥ 40-50% above 50-day average.
6. **Buy** within 0-5% of pivot; never chase beyond 5%.
7. **Stop** 7-8% below buy.
8. **Manage** with partials at +20-25%, the 8-week hold rule for explosive movers, and the 50-day/10-week line as trend backbone.

**Position sizing.** With a hard 8% stop, risk-per-trade of 1% of a ₹10,00,000 account = ₹10,000. Position size = ₹10,000 ÷ 0.08 = **₹1,25,000** notional (about 12.5% of capital in one name). O'Neil ran concentrated books — 4 to 8 positions — precisely because the setup is selective. Do not dilute into 30 names.

## Confluence

CANSLIM's technical letters *are* a confluence system by design, but you can layer additional Indian-market confirmation:

- **Sector leadership.** Buy X only if capital-goods / infra is a leading NSE sector (top 4 by 3-month return). Winners cluster in themes — 2020-21 IT and pharma, 2023-24 PSU/defence/capex.
- **Delivery percentage.** On NSE, a breakout accompanied by rising **delivery %** (not just intraday churn) corroborates real accumulation. A pivot day with 4x volume but 25% delivery is weaker than one with 3x volume and 55% delivery.
- **FII/DII and bulk-deal data.** Institutional sponsorship ("I") showing up as increasing mutual-fund holdings quarter-on-quarter, or bulk/block deals by known funds, confirms the "S" and "I" together.
- **Follow-Through Day (FTD) for "M".** O'Neil's market-timing signal: after a market low, wait for an attempted rally, then a day (usually day 4-7 of the attempt) where a major index rises **1.25%+ on higher volume than the prior day**. That FTD greenlights fresh breakout buying. On the flip side, count **distribution days** (index down 0.2%+ on higher volume than prior day); **5-6 distribution days within 4-5 weeks** typically signals the uptrend is under threat — tighten up, stop taking new breakouts.

When the pivot breakout, RS-line new high, leading sector, rising delivery %, *and* a recent Nifty FTD all coincide, you have maximum-confluence — the trades worth sizing up.

## Pitfalls

- **Ignoring "M".** The most expensive error. In a Nifty correction, roughly two-thirds of breakouts fail. Backtests of breakout systems show win rates collapsing from ~50% in uptrends to ~25% in downtrends. Respect the market.
- **Buying extended.** Chasing 8-15% past the pivot converts a 7% stop from "logical" to "you'll get shaken out on the first normal pullback." Discipline the 5% rule.
- **Faulty bases.** Wide, loose, sloppy bases (V-shaped with no handle, deep 45%+ corrections in a bull market, handles in the lower half, wedging-up handles) fail far more. "Tight and orderly" beats "deep and wild."
- **Low-volume breakouts.** No volume, no institutions, no conviction. Skip.
- **Small floats and illiquidity.** In Indian small-caps, a "breakout" can be a manipulated pump. Insist on genuine institutional presence and adequate liquidity (avoid names where your position is a large fraction of daily turnover).
- **Fighting the sell rules.** The 7-8% stop and the "cut it, don't average down" rule are non-negotiable. Winners in CANSLIM come from letting a few 100%+ runs pay for many small 8% losses. Averaging down a broken base is how the system's math breaks.
- **Over-diversification.** 25 half-conviction names guarantee mediocrity. The edge is concentration in confirmed leaders.
- **Applying it in choppy, rangebound indices.** CANSLIM shines in trending bull phases with clear leadership. In a sideways Nifty year, breakout setups whipsaw; reduce activity.

## Interview-ready summary

CANSLIM is O'Neil's growth-momentum framework; its **technical core** is: buy a **relative-strength leader** (RS Rank ≥ 85, RS line at new highs) as it **breaks out of a proper base** (cup-with-handle, flat base, or double bottom) at a **precise pivot** (10 paisa above the handle/peak high) on **volume ≥ 40-50% above the 50-day average**, but **only when the general market ("M") is in a confirmed uptrend** (Nifty above rising 50/200-day, a recent Follow-Through Day, no distribution-day cluster). Manage with a **hard 7-8% stop**, take partials near +20-25%, **hold explosive +20%-in-3-weeks movers at least 8 weeks**, and ride the trend on the 50-day/10-week line. The philosophy is "buy high to sell higher" — new highs mean no overhead supply. The fatal errors are ignoring market direction, chasing extended pivots, and violating the stop-loss discipline. In India: run RS-rank screens on Chartink over your NSE universe, confirm with delivery % and FII/DII sponsorship, keep a Nifty distribution-day count, and stay concentrated in the leading sectors of the cycle.
