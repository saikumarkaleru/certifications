# Initial Balance & Day Types

The single most useful predictive tool in the entire Market Profile toolkit is not the value area or the POC — it is the **Initial Balance** and the family of **day types** it helps you anticipate. If AMT gives you the *why* and the TPO profile gives you the *picture*, the Initial Balance and day-type framework give you the *game plan for today*: the moment-by-moment expectation of whether this is a day to fade the edges, ride a trend, or sit on your hands. This chapter builds the Initial Balance precisely, classifies the seven canonical day types with their India-specific tells, and turns them into concrete Nifty and Bank Nifty trade plans.

## What it is and the logic

The **Initial Balance (IB)** is the price range established during the *first two 30-minute brackets* of the session — the A and B periods, i.e. the first hour of trade. On the NSE that is roughly **09:15–10:15**. The IB high is the highest price of that first hour; the IB low is the lowest. The distance between them is the **IB range**.

Why does the first hour matter so much? Because the opening hour is when the *responsive*, professional, longer-timeframe participants establish the day's initial parameters — they set the boundaries of where two-sided trade is willing to happen given all the overnight information. The IB is the day's opening auction bracket. Everything that follows is measured against it: does the day *stay inside* the IB (balance — the longer-timeframe player is in control and content), or does it *break out* of the IB (imbalance — one side has taken control and is extending the auction to find new value)? That single question — *did we break the IB, and did the break hold?* — organizes the whole trading day.

The related concept is **range extension**: any trade that occurs *above the IB high* or *below the IB low* later in the day. Range extension up = buyers took initiative beyond the opening auction; range extension down = sellers did. The *presence, direction, and symmetry* of range extension is what distinguishes the day types.

A structural note for India: the classic IB = first hour framework was built on US markets. On the NSE, some profile traders shorten the IB to the first 30 or 45 minutes because Indian index futures are fast and news-driven, and a full hour can already contain most of the day's range. A common practical choice is a **45-minute IB (09:15–10:00)** for Nifty/Bank Nifty. Pick one and be consistent; the *logic* is identical whichever bracket length you use.

## Construction: measuring the IB and the extension

The IB is trivial to build but the derived measures are what you trade:

| Measure | Definition |
|---|---|
| IB High | Highest price in periods A+B (first hour) |
| IB Low | Lowest price in periods A+B |
| IB Range | IB High − IB Low |
| IB Midpoint | (IB High + IB Low) / 2 — an intraday pivot |
| Range extension up | Any print above IB High after period B |
| Range extension down | Any print below IB Low after period B |

**IB range as a day-type predictor.** A *wide* IB (large first-hour range) means much of the day's discovery already happened in the opening auction — the rest of the day is more likely to *balance* inside it (a wide IB is hard to break because a lot of price was already covered). A *narrow* IB means the opening auction was tight and coiled — a small IB is easy to break, so a narrow IB raises the odds of *range extension* and a trend or breakout day. This inverse relationship is one of the most useful heuristics on the desk:

> Wide IB → lean toward balance / range trades inside it.
> Narrow IB → lean toward breakout / trend; watch for range extension and go with it.

**The IB extension "target" heuristic.** A rough rule of thumb from the CBOT era: on a trend day, range extension often runs about *one additional IB range* beyond the IB in the direction of the break. If Nifty's IB is 60 points and it breaks the IB high, an initial extension target near IB high + 60 is a reasonable first objective. It is a heuristic, not a law, but it sizes expectations.

## The day types

There are seven canonical day types. In practice you are usually deciding between three families — *balance* (Normal, Normal Variation, Neutral), *trend* (Trend, Double Distribution Trend), and *one-sided open-driven* (Trend/Open-Drive) — but knowing all seven sharpens the read.

| Day type | IB & extension signature | Character | How to trade |
|---|---|---|---|
| **Normal** | Wide IB; little/no range extension; day stays largely inside IB | LTF player passive, wide opening auction contains the day | Fade IB edges toward IB midpoint / POC |
| **Normal Variation** | Moderate IB; range extension on *one* side, ~1× IB | One side takes control after the open, extends then balances | Enter on the extension, target ~1 IB range, then range |
| **Trend** | Narrow-ish IB; strong one-directional range extension; value migrates all day; profile thin/elongated | One-timeframe control; each bracket makes progress | Buy pullbacks (uptrend) into developing value; hold |
| **Double Distribution Trend** | IB, then a *drive* to a new area, single prints between, second balance | Balance → catalyst → new balance; two bulges | Trade the break of first distribution to the second |
| **Neutral** | Range extension on *both* sides of IB, then closes back inside | Two-sided fight, no winner; longer-timeframe indecision | Fade both extremes; expect close near IB middle |
| **Neutral Extreme** | Both-side extension but closes *on one extreme* | Late resolution; one side finally wins into the close | Go with the late winner into the close |
| **Trend / Open-Drive** | Opens and drives immediately, never trades back through the open; almost no IB rotation | Highest-conviction directional day; gap or news driven | Enter early with the drive, wide stop, hold |

### The open type modifier

The *way* the day opens colours everything. Four open types, in ascending order of conviction:

1. **Open-Auction (in prior value)** — opens inside yesterday's value and rotates; lowest conviction; favours Neutral / Normal balance days.
2. **Open-Auction (outside value)** — opens outside value but still rotates two-sided; moderate; watch for acceptance.
3. **Open-Test-Drive** — opens, briefly tests one direction (probes a level), then reverses and drives the other way with conviction; the initial probe *fails* and confirms the drive. Strong.
4. **Open-Drive** — opens and immediately drives one direction with no look back; the highest-conviction open; almost always produces a Trend or Trend/Open-Drive day. On the NSE this is the classic gap-and-go after a strong global lead or a big earnings/policy surprise.

The heuristic: **the more the open looks like a drive and the less it rotates, the more directional the day.** An Open-Drive with a narrow-to-normal IB and one-sided range extension is the textbook trend day; an Open-Auction-in-value with a wide IB is the textbook balance day.

## Worked India example: three Nifty days

**Day A — Normal / balance day.** Nifty opens 24,010, inside yesterday's value (Open-Auction-in-value). First hour trades a *wide* 24,040–23,960 → IB range 80 points, IB midpoint 24,000. Wide IB + open-in-value → lean balance. Through the day price never sustains beyond the IB; a probe to 24,050 fails (upper single prints), a probe to 23,950 fails. Trade plan executed:
- Short the failed probe of IB high near 24,045, stop 24,075 (above the IB extreme / where a range-extension breakout would be confirmed), risk 30 pts.
- Target the IB midpoint / POC at 24,000. Booked +45 pts, ~1.5R.
- Buy the failed probe of IB low near 23,955, target 24,000 again. The day pays *rotation*, not trend. Sitting for a breakout here would have lost money to chop.

**Day B — Trend / Open-Drive day.** Overnight the US sells off hard; SGX Nifty points down 250. Nifty *opens* at 23,760 and immediately drives lower — no trade back above the open (Open-Drive). IB is 23,760–23,680, a *narrow* 80-point IB relative to the gap, and price is already extending *below* IB low by period C. Narrow-ish IB + Open-Drive down + one-sided range extension = trend day. Plan:
- Enter short on the first pullback into the developing value / back toward IB low ~23,700 (do *not* wait for a "confirmation" that never comes on a drive day — sell strength into the trend).
- Stop back above the IB midpoint ~23,760, risk ~60 pts.
- Because IB range is ~80, first extension target ≈ IB low − 80 = 23,600; second target the prior swing / naked POC at 23,520.
- Hold as long as value keeps migrating down (each bracket's activity below the last). Booked to 23,540 → ~160 pts, ~2.6R. Fading the IB low here (treating it like Day A) would have been run over — *this is why classifying the day first is non-negotiable.*

**Day C — Neutral day.** Bank Nifty opens 51,400 inside value. IB 51,300–51,500 (200-pt IB, moderate). In period D buyers extend the range up to 51,580 (range extension up); but by period H sellers reject it and extend *down* to 51,240 (range extension down). Both sides tried, neither held → **Neutral day**, longer-timeframe indecision. The read: expect a close back toward the IB middle (~51,400) unless one extreme is defended into the last hour (which would make it Neutral-Extreme). Plan: fade *both* extremes toward the middle, keep size small (Neutral days are choppy), and *do not* marry a directional bias — the market is explicitly telling you it hasn't decided.

## How to trade it: entry, stop, target, management

**Step 1 — build the IB and read its width vs. recent days.** Narrow relative to the last few sessions → breakout-biased. Wide → balance-biased.

**Step 2 — read the open type.** Drive/test-drive → directional; auction-in-value → rotational.

**Step 3 — form the day-type hypothesis, then let range extension confirm or kill it.**
- If you expect balance (wide IB, open-in-value): **fade the IB edges** toward the IB midpoint / POC. Stop just beyond the IB extreme — a *sustained* break of the IB is your thesis being disproven, so exit and possibly reverse. Target the midpoint first, opposite edge second.
- If you expect trend (narrow IB, open-drive): **trade with the range extension.** Enter on the break of the IB in the drive direction, or better, on the first shallow pullback into developing value. Stop back inside the IB (beyond the midpoint). First target ≈ one IB range beyond the IB; then trail with value migration.
- If it turns Neutral (extension both sides): **fade both extremes, small size**, expect a middle close — unless late-session acceptance at one extreme flips it to Neutral-Extreme, then go with the late winner.

**Step 4 — manage by regime, not by ticks.** On balance days, take the rotation and be done — do not overstay. On trend days, the error is exiting too early; hold while value migrates and only exit when overlapping value (balance) returns. The IB midpoint is a clean intraday pivot for trailing: on a trend day, price staying beyond the IB midpoint keeps you in.

## Confluence

- **IB break + prior value.** An IB-high break that also clears *yesterday's VAH* is far stronger than an IB break in the middle of yesterday's range — two auctions agree.
- **Open type + IB width.** Open-Drive with a narrow IB is the highest-probability trend setup; Open-Auction-in-value with a wide IB is the highest-probability fade setup. When open type and IB width agree, conviction is high; when they conflict (e.g. drive open but very wide IB), expect a Normal-Variation compromise.
- **Range extension + volume/delta.** A range extension on expanding volume and supportive footprint delta is real initiative; an extension on fading volume is a probe likely to fail (Neutral-day tell).
- **F&O / OI on the NSE.** An IB-low break that coincides with put unwinding / fresh call writing at the strike just below confirms sellers; an IB-high break into a wall of call writing may stall (the option sellers defend). Around expiry, high-OI strikes cap range extension and bias the day toward Neutral/balance.
- **Global/overnight cues.** Indian index days are strongly conditioned by the overnight US close and SGX/GIFT Nifty. A large gap with an Open-Drive almost always argues trend; a flat lead with an inside open argues balance.

## Pitfalls

- **Applying the US 60-minute IB blindly.** NSE index futures often complete much of their range fast; a 45-minute IB frequently reads the day better. Test both on your instrument.
- **Trading the day type you *want*, not the one in front of you.** The most expensive Market Profile error is fading the IB low on a trend/open-drive day. Classify first, trade second.
- **Declaring a day type too early.** Until range extension appears (or fails to), your day type is a hypothesis. A "Normal" morning can extend into a Trend by afternoon. Keep the hypothesis, but let extension confirm it before committing full size.
- **Ignoring the both-sided warning of Neutral days.** Two-sided range extension is the market shouting "I haven't decided." Trading it with a strong directional bias and normal size is a recipe for getting chopped.
- **Over-respecting the 1× IB extension target.** It sizes expectations; it does not cap a genuine trend day, where value migrates far beyond one IB range. Use it as a first target, not a reason to exit a strong trend.
- **Expiry days (India-specific).** On weekly Bank Nifty / Nifty and Fin Nifty expiries, option pinning distorts the auction — IB breaks fail more often, Neutral outcomes dominate, and range extension is less reliable. Reduce size and skepticism accordingly.
- **Gaps that fill.** A gap-open outside value that immediately reverses back through the open is *not* an Open-Drive — it is a failed auction / gap fill, which often flips to a trend in the *opposite* direction. Do not confuse the two; the tell is whether price trades back through the opening print.

## Interview-ready summary

The **Initial Balance** is the price range of the first hour (periods A and B; on the NSE many traders use the first 45 minutes) — the day's opening auction bracket. Everything after is measured against it: staying inside the IB signals *balance* (the longer-timeframe player is content — fade the edges toward the IB midpoint/POC), while breaking it, called **range extension**, signals *imbalance* (one side took initiative — trade with the break). IB *width* is inversely predictive: a **wide IB** already covered much of the day's discovery and biases toward balance, while a **narrow IB** is easy to break and biases toward a trend/breakout day. The seven **day types** — Normal, Normal Variation, Trend, Double Distribution Trend, Neutral, Neutral Extreme, and Trend/Open-Drive — are distinguished by the presence, direction, and symmetry of range extension, and are further coloured by the **open type** (Open-Drive and Open-Test-Drive = directional; Open-Auction-in-value = rotational). The workflow is: build the IB, read its width and the open type, form a day-type hypothesis, then let range extension confirm or kill it — fading edges on balance days, trading with extension (first target ≈ one IB range) on trend days, and fading both extremes with small size on Neutral days. The cardinal sin is fading the IB on a genuine open-drive trend day: **classify the day first, trade second.** In India, adapt for a shorter IB, respect overnight/SGX-driven gap opens as initiative, and treat F&O expiry sessions — where option pinning caps range extension — with reduced size and extra skepticism.
