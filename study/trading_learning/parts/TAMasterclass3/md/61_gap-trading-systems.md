# Gap Trading Systems

A gap is a discontinuity — a place where price teleports overnight, leaving a blank strip on the chart where no trading occurred. In Indian markets, where the cash and F&O segments trade a single 09:15–15:30 session but absorb a full night of global cues, earnings, and macro headlines, the opening gap is the most information-dense event of the day. Gap trading systems are built to exploit two opposing tendencies of these discontinuities: some gaps *fill* (price returns to close them) and some *run* (price continues in the gap's direction). This chapter turns that fork into mechanical systems for Nifty, Bank Nifty, and NSE stocks.

## What it is and the logic

A gap forms when the day's open prints away from the prior day's close — above it (gap-up) or below it (gap-down). The gap encodes an imbalance: overnight order flow has repriced the instrument before continuous auction resumes. The edge in gap trading comes from a simple asymmetry in human behaviour and market microstructure:

- **Gaps that fill** occur when the overnight move was an *overreaction* — emotional, liquidity-driven, or a knee-jerk to a headline that the day session then fades. The prior close acts as a magnet because a large population of resting orders and value perception sits there.
- **Gaps that run** occur when the gap reflects a genuine *repricing* — an earnings surprise, a policy shock, a global regime shift — where new information has permanently moved fair value. The unfilled gap becomes support/resistance and the trend extends.

The trader's job is not to guess which is which by feel but to *classify* the gap using its size, cause, location relative to structure, and the first 15–30 minutes of price action, then apply the matching playbook. The four-way taxonomy from classical technical analysis maps cleanly onto NSE:

1. **Common gap** — small, inside a range, no news. Tends to fill quickly. Fade it.
2. **Breakaway gap** — price gaps out of a consolidation/base on volume and news. Tends to run. Trade continuation.
3. **Runaway (measuring) gap** — appears mid-trend, confirms momentum. Runs; roughly marks the trend's midpoint.
4. **Exhaustion gap** — appears after an extended move, often on climactic volume. Fills and reverses. Fade.

The single most important predictive input is **why the gap happened**. A gap on stock-specific results behaves differently from an index gap on SGX Nifty / GIFT Nifty following the US close. Cause drives everything.

## Construction, rules and settings

We define three systems: two directional (fade and go) plus a single-stock earnings-gap system. All are intraday-first and fully mechanical.

### Gap size normalisation

Absolute points mislead across instruments. Normalise every gap by ATR:

**Gap % = (Today Open − Prior Close) / Prior Close × 100**
**Gap-to-ATR = (Today Open − Prior Close) / ATR(14, daily)**

| Gap-to-ATR | Interpretation | Default bias |
|---|---|---|
| < 0.5 | Small / common | Fill (fade) |
| 0.5 – 1.0 | Moderate | Context-dependent |
| > 1.0 | Large / news-driven | Continuation (go) or exhaustion |

### System A — Gap-Fill Fade (Nifty / Bank Nifty index)

Fades small-to-moderate index gaps back to the prior close.

| Component | Rule |
|---|---|
| Instrument | Nifty / Bank Nifty futures, 5-min chart |
| Setup | Gap-to-ATR between 0.3 and 0.9, **no** major overnight event (results, policy, big US move) |
| Direction | Gap-up → look short; gap-down → look long (fade toward prior close) |
| Trigger | First 15-min candle fails to extend the gap; entry on break of the first-bar high (for longs) / low (for shorts) |
| Target | Prior day's close (the gap-fill level); book majority there |
| Stop | Beyond the opening-range extreme (the session high for a short / low for a long) |
| Filter | Skip if opening 15 min shows one-directional expansion on heavy volume (that is a runner) |

### System B — Gap-and-Go Continuation

Rides large, news-confirmed gaps in the gap's direction.

| Component | Rule |
|---|---|
| Setup | Gap-to-ATR > 1.0 on genuine news; gap out of a base or in trend direction |
| Opening range | Mark the high/low of the first 15 min (ORB) |
| Trigger | Break of the ORB *in the gap's direction* (gap-up → break above 15-min high) |
| Confirmation | Price holds above VWAP; volume on the breakout bar > average |
| Entry | On ORB break + retest hold, or first pullback to VWAP that does not fill the gap |
| Stop | Below VWAP / below the opening range / just inside the gap |
| Target | Measured move = gap size projected from the ORB break; trail under 20-EMA(5m) |
| Invalidation | A full gap-fill kills the continuation thesis — exit |

### System C — Earnings Gap (single-stock swing)

For NSE F&O stocks gapping on results.

| Component | Rule |
|---|---|
| Setup | Stock gaps > 4% (or > 1 ATR) on quarterly results |
| Classification | Gap *and* first-hour close on the same side of open, above/below prior swing structure |
| Long trigger | Gap-up that holds above the opening 60-min low **and** clears the pre-results resistance |
| Entry | End-of-first-hour or next-day continuation above day-1 high |
| Stop | Below day-1 low (below the gap's defended edge) |
| Target | Prior swing extension / 1.5–2R; trail on daily 10-EMA |
| Fade caveat | An exhaustion gap-up that closes red below its open on huge volume is a *short* setup, not a long |

**The "first 15/30 minutes" rule underpins all three.** The opening range is the market's referendum on the gap. If the gap-up cannot hold its opening range and slips below VWAP, sellers won the overnight auction's follow-through — favour the fade. If it builds a base above VWAP and expands, buyers are committed — favour the go.

## Worked India example (levels and ₹)

**Trade: Nifty gap-fill fade (System A).**

Prior day Nifty closes at **24,600**. Overnight the US market drifts slightly higher; GIFT Nifty points to a modest gap-up. Nifty opens at **24,690** — a +90-point, +0.37% gap. Daily ATR(14) ≈ 210, so Gap-to-ATR ≈ 0.43: a common gap, no major event. Bias: fade toward 24,600.

- The first 15-min candle prints a high of 24,702 then closes at 24,678 — it *failed to extend* the gap. This qualifies the fade.
- **Entry (short):** break below the first-bar low of 24,672 → fill at **24,670** on the futures.
- **Stop:** above the session high 24,702 → place at **24,708** (risk ≈ 38 points).
- **Target:** prior close **24,600** (gap-fill), an 70-point objective → reward ≈ 70 points.
- **Reward-to-risk ≈ 1.8R.**

Suppose Nifty grinds down through the morning and touches 24,598 by 11:20 — target filled. On one lot of Nifty futures (lot size 75), 70 points × 75 = **₹5,250 gross** per lot. Round-trip costs (brokerage, STT on futures, exchange, GST, stamp) on a ~₹18.5 lakh notional are roughly ₹200–350 — comfortably absorbed.

Had Nifty instead broken *above* 24,702 in the first 30 minutes on rising volume with price holding over VWAP, the fade filter would have blocked the short and the setup would flip to a **gap-and-go long** (System B): ORB break above 24,702, stop below VWAP, measured-move target of 24,702 + 90 = ~24,792. This is the crucial discipline — the *same gap* is a fade or a go depending on how the opening range resolves, and the rules, not the opinion, decide.

**Single-stock example — TCS earnings gap (System C).** TCS closes at ₹3,900 pre-results, ATR ≈ ₹70. Results beat; it gaps up to **₹4,050** (+3.8%, Gap-to-ATR ≈ 2.1) and clears the ₹3,980 pre-results resistance. Through the first hour it holds above its opening 60-min low of ₹4,020 and never fills the gap. Classification: breakaway gap-and-go. Entry next day above day-1 high ₹4,075 at **₹4,078**, stop below day-1 low ₹4,020 (risk ₹58), target the measured move / prior extension near ₹4,190 (~2R). If instead TCS had gapped to ₹4,050 and then *closed the day red at ₹3,960 below its open on huge volume* — an exhaustion gap — the system flips to a short on the failed gap, stop above ₹4,050, targeting the gap-fill and beyond.

## How to trade it — entry, stop, target, management

**Wait for the opening range.** The amateur trades the tick at 09:15; the system trader lets the first 15 minutes build, because that range is the day's decision. Entering before the range is set is trading noise — the pre-open session and first-minute prints are unreliable.

**Entry via break, not anticipation.** Fades enter on the failure of the gap to extend (break of first-bar extreme back toward the close). Continuations enter on the ORB break *plus* a VWAP hold or first-pullback that respects the gap. Requiring price to *act* first converts a guess into a reaction.

**Stops belong at the structural line.** For a fade, the stop sits beyond the session extreme — if the gap keeps extending, your fade thesis is dead. For a go, the stop sits inside the gap / below VWAP — a full gap-fill means the continuation failed. Never place stops at round rupee amounts divorced from the opening range.

**Targets and management:**

- Fades target the prior close and are largely *done* there — gap-fills are mean-reversion, not trends; do not overstay.
- Continuations use a measured move (gap size projected) for the first target and trail the runner under the 20-EMA(5m) or below the developing VWAP.
- Move to breakeven once price travels 1R in favour.
- Honour a **time stop**: an index fade that has not begun filling within ~45 minutes is losing its edge as the day trends; a go that stalls at VWAP without expanding is suspect.
- Flatten intraday gap trades by ~15:15 unless the setup has become a clean swing (System C).

## Confluence

- **Prior gaps and unfilled zones:** an old unfilled gap overhead is a natural target for today's continuation and a resistance for a fade.
- **VWAP:** the arbiter of gap-and-go vs gap-fill. Holding above VWAP on a gap-up favours continuation; losing it favours the fade.
- **Support/resistance and pivots:** a gap-up straight into a daily resistance or the R1 pivot strengthens a fade; a gap-up that *clears* resistance strengthens a go.
- **Options open interest (F&O):** a Nifty gap into a strike stacked with Call OI (a resistance "wall") supports a fade; a gap that breaks above the max-Call-OI strike on volume supports continuation as writers are forced to hedge. A gap-down into a heavy Put-OI strike often finds a floor.
- **Breadth on the open:** a strong gap-up with weak advance-decline (few stocks participating) is a fade candidate; broad participation supports the go.
- **Volume:** genuine breakaway/runaway gaps carry above-average volume; low-volume gaps are usually common gaps that fill.

## Pitfalls

- **Fading a breakaway gap.** The most expensive error: shorting a genuine news-driven gap-up because "gaps fill." Large, news-backed, above-VWAP gaps run. The size and cause filters exist to stop this.
- **Chasing a gap-and-go without a retest.** Buying the extended open, then getting shaken out on the first VWAP pullback. Wait for the ORB break *and* the hold/retest.
- **Trading the first minute.** Pre-open imbalances and the opening auction produce unreliable prints. Let the opening range form.
- **Ignoring the cause.** Treating an earnings gap like a common index gap. Stock-specific reprices run far more often than they fill.
- **Overstaying a fill.** Gap-fills are mean-reversion; the prior close is the target, not a launchpad. Book it.
- **Gap-risk on overnight positions.** Holding single stocks into results is deliberately taking gap risk — size for a full ATR gap against you, because stops do not trigger inside a gap.
- **Expiry and event distortion.** Weekly-expiry days, RBI policy, and budget sessions produce erratic opens; either sit out or widen filters.
- **Assuming symmetry.** Indian indices gap-down harder on global risk-off than they gap-up on risk-on; calibrate fade/go thresholds separately for up and down gaps.

## Interview-ready summary

A gap is an overnight price discontinuity that encodes an order-flow imbalance; gap trading systems classify each gap and apply the matching playbook rather than guessing. The core fork is **fill vs run**: small, newsless, in-range **common/exhaustion gaps** tend to fill and are *faded* back to the prior close; large, news-confirmed **breakaway/runaway gaps** tend to run and are *traded for continuation*. The decisive inputs are **gap size normalised by ATR**, the **cause** (index macro vs stock earnings), **location** versus structure, and the resolution of the **first 15–30 minute opening range** relative to **VWAP**. The three canonical builds are the **gap-fill fade** (index, fade the failure to extend toward prior close), **gap-and-go** (ORB break + VWAP hold, measured-move target), and the **earnings gap** (single-stock swing with day-1-low stop). Stops sit at structural invalidation — the session extreme for fades, inside the gap/below VWAP for continuations — and fades are managed as mean-reversion (target the close, do not overstay) while gos are trailed as trends. The defining skill is refusing to fade a breakaway and refusing to chase an exhaustion: let the opening range and VWAP, not the opinion, decide which system fires.
