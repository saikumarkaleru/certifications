# Market Profile & Order Flow (Deep)

## What it is & why it works

Most charts answer *where* price went. Market Profile answers a different, more powerful question: **where did price spend time, and at what prices did real business get done?** It re-organises a session's trading not by time-slices (candles) but by *price-acceptance* — how much of the day each price level was traded. The result is a distribution, a bell-shape lying on its side, that reveals the market's *value area*: the band of prices the auction agreed were "fair" today.

The intellectual engine is the **auction market theory** of J. Peter Steidlmayer: markets are a continuous two-way auction seeking a price that facilitates trade. Price moves *up* until it chokes off buyers, moves *down* until it chokes off sellers, and rotates around the level where the most volume transacts. When price trades away from value and quickly returns, that's *rejection* — the auction said "too high" or "too low." When price leaves value and *builds new value* up there, that's *acceptance* — a genuine shift. Everything in Market Profile and order flow is a way of reading acceptance vs rejection in real time.

Why it works for Indian traders specifically: Nifty and Bank Nifty futures are deeply liquid, so their distributions are statistically meaningful. Bank Nifty in particular is a *rotational, mean-reverting* instrument on most days — it loves to build a value area and revert to it — which makes profile-based fading and value-area trades unusually effective. And because so much Indian intraday flow is options-driven, the futures profile plus the option chain together give you both the *price acceptance* map and the *positioning* map.

## Mechanics: building and reading the profile

**TPO (Time-Price-Opportunity) profile.** Split the session into 30-minute periods, each labelled with a letter (A, B, C, …). For every 30-min period, mark each price the market traded with that period's letter. Stack the letters at each price. Prices touched in many periods grow long rows; prices touched briefly stay short. The finished shape is the profile. Key structures:

- **Point of Control (POC):** the price with the most TPOs (widest row) — the session's fairest, most-accepted price, a magnet.
- **Value Area (VA):** the price band containing ~**70%** of the day's TPOs (one standard deviation), bounded by the **Value Area High (VAH)** and **Value Area Low (VAL)**. This is where "value" lived.
- **Initial Balance (IB):** the range of the *first hour* (periods A and B). It frames the day; breakouts of the IB signal directional intent.
- **Range Extension:** price pushing beyond the IB later in the day — evidence one side is in control.
- **Single prints:** prices touched in only one period — fast, un-auctioned moves; they mark rejection zones that often get revisited ("single-print magnets").
- **Poor high / poor low:** an unfinished end of the distribution (multiple TPOs at the extreme, no tapering tail) — the auction was cut short and price often returns to complete it.

**Day types** (the profile's *shape* tells you the day's character):

| Day type | Shape | Meaning |
|---|---|---|
| Normal day | Fat bell, wide IB | Balanced, range-bound; fade the extremes |
| Normal variation | Bell with one range extension | Mild directional lean |
| Trend day | Thin, elongated, IB broken and never revisited | One-sided; do NOT fade — go with it |
| Double-distribution | Two bells stacked, thin middle | Value migrated; the thin middle is a fast zone |
| Neutral day | IB broken *both* ways, closes middle | Indecision; two-timeframe fight |
| b-shape / P-shape | Long tail up (P) or down (b) | Short-covering (P) or long-liquidation (b), then balance |

**Volume Profile** is the modern cousin: instead of counting time (TPOs), it counts *volume* at each price. Its POC is the **Volume Point of Control (VPOC)** — the highest-volume price. On TradingView, the "Session Volume Profile," "Visible Range Volume Profile (VRVP)," and "Fixed Range Volume Profile" tools draw this instantly. Volume Profile is generally preferred today because it measures where *contracts changed hands*, not merely where time passed — but TPO shape still adds the "how the day unfolded" narrative that pure volume loses.

## Order flow: the layer beneath the profile

Market Profile tells you *where* value formed; **order flow** tells you *how aggressively* it formed — who was pressing the bid vs the offer. The core objects:

- **The order book (DOM / Depth of Market):** resting limit orders (passive liquidity) on the bid and ask. Large resting orders can act as walls; but beware *spoofing* (orders placed to be pulled).
- **Aggressor / market orders:** trades that lift the offer (aggressive buyers) or hit the bid (aggressive sellers). The *aggressor side* is what moves price.
- **Delta:** cumulative (aggressive buys − aggressive sellers). Rising delta = buyers pressing; the *divergence* between price and delta is the tell (covered in depth in the Footprint chapter).
- **Absorption:** heavy aggressive selling that price *refuses to fall on* — a large passive buyer is absorbing it. This is the order-flow signature of a bottom.
- **Exhaustion:** aggressive buying that produces smaller and smaller upticks — demand running dry near a high.

In India, retail traders don't always have institutional-grade DOM/tape feeds, but the *concepts* map directly onto tools you do have: Volume Profile (acceptance), footprint/delta (aggression, where available via GoCharting, Quantsapp, Sensibull-style or broker platforms), and the **option chain OI** (positioning). A Bank Nifty VPOC at 51,200 with heavy Put writing at 51,000 and Call writing at 51,500 is an order-flow *and* positioning picture: value at 51,200, floor at 51,000, ceiling at 51,500.

## Worked India example (levels & ₹)

**Bank Nifty — a value-area rotation with an absorption low (approximate reconstruction; verify on charts).**

Context: Bank Nifty futures. Yesterday's profile printed **VAH 51,450, POC 51,250, VAL 51,050** — a balanced Normal day. Auction-market logic for the next session: if today opens *inside* yesterday's value area, the base case is **rotation** — a fade of the extremes back toward POC.

The session:

- **Open:** Bank Nifty opens at **51,300**, inside yesterday's value (between VAL 51,050 and VAH 51,450). "Open inside value" → expect rotational, mean-reverting behaviour. Bias: fade edges, target POC.
- **Period A–B (IB):** builds a first-hour range of **51,200–51,420**. It probes up to 51,420 (near yesterday's VAH) and gets sold — rejection at value-area high.
- **Rotation down:** price rotates to **51,120**, near yesterday's VAL. Here the order-flow tell appears: aggressive selling hits the bid repeatedly, but price *stops falling* around 51,110–51,120 — the down-ticks shrink, and delta prints negative while price holds. That's **absorption**: a passive buyer is soaking up the sellers at value-area low.
- **Trade (value-area long):** enter long on the reclaim of 51,150 with the absorption signature under you. **Stop** below the absorption low, ~51,060 (below yesterday's VAL — if VAL breaks and *accepts*, the whole thesis is wrong). Risk ~90 points.
- **Target:** POC magnet at **51,250** (first), then VAH **51,420** (second). On a rotational day, POC is the highest-probability target.
- **Outcome:** price rotates back to POC 51,250 (booking half, +100), then grinds to 51,400 near VAH where single prints from the IB get filled and the auction stalls. Book the rest (~+250). Reward ~150–250 vs 90 risk → ~1.7–2.7:1.

The lesson: the profile framed the *day type* (open-inside-value → rotational), the value area gave the *levels* (fade VAL, target POC/VAH), and order flow (absorption at VAL) gave the *trigger and conviction*. Fading VAL blind is dangerous; fading it *with visible absorption* is a trade.

## How to trade it (entry / stop / target)

Three high-value, repeatable playbooks:

**1. Open location vs prior value (the master template).**
- **Open inside value** → rotational bias → fade VAH/VAL toward POC. Entry at the edge with a rejection/absorption tell; stop just outside the value area; target POC then opposite edge.
- **Open outside value but inside range** → look for acceptance vs rejection back into value ("look above/below and fail" or "look and go").
- **Open outside range (gap)** → either a trend day (gap holds, IB doesn't get revisited — go with it) or a gap-fill day (price re-enters range — fade back toward prior POC). The *first hour's* behaviour vs the prior range edge decides which.

**2. Initial Balance breakout (trend-day capture).**
- Trigger: clean break and *acceptance* (a full 30-min period closing) beyond the IB high/low, ideally with expanding volume/delta in the breakout direction.
- Stop: back inside the IB (a failed breakout reverts).
- Target: measured range extension; on a suspected trend day, trail rather than fix a target — trend days run.

**3. POC / VPOC mean-reversion and naked-POC magnets.**
- A **naked POC** (a prior session's POC never revisited since) is a magnet; price tends to return to it. Trade *toward* an untested POC; take profit *at* it.
- Enter on rotation away from an extreme with a reversal signature; target the VPOC.

Across all three: **the value area edges are your fences**, the POC is the magnet, and *acceptance vs rejection* (does price stay or snap back?) is the single decision you keep making.

## Confluence (including OI)

- **Option chain OI:** Overlay VPOC and value area on the option OI map. When VPOC ≈ max-pain, and Put-writer support sits at/near VAL while Call-writer resistance sits at/near VAH, the profile and positioning *agree* — high-conviction rotational day. Divergence (VPOC drifting away from max-pain) warns of a coming directional move.
- **Prior-day levels:** yesterday's VAH/VAL/POC, the overnight (GIFT Nifty) range, and the weekly VPOC are all confluence levels. A trade located where multiple prior VPOCs stack is stronger.
- **VWAP:** intraday VWAP and its bands often coincide with POC/value; a VAL that sits on the lower VWAP band is a doubly-defended level.
- **Delta / footprint:** the confirming micro-signal — absorption at VAL, exhaustion at VAH, delta divergence at extremes (see the Footprint & Delta chapter).
- **Breadth / index vs constituents:** on Bank Nifty, watch whether HDFC Bank / ICICI are confirming the futures' value-area move.

## Pitfalls

1. **Fading a trend day.** The deadliest error. On a trend day the profile is thin and elongated, the IB breaks and *never* gets revisited — fading the "extreme" back to POC gets you run over. *Read the day type first.* Open outside range + IB one-sided = do not fade.
2. **Treating the 70% value area as a hard wall.** Value migrates. Price *accepting* beyond VAH isn't a fade — it's tomorrow's new value forming. The question is always acceptance vs rejection, never "it's at the edge so I short."
3. **Spoofing and thin-book illusions.** A big resting order in the DOM may be bait that vanishes when approached. Trust *executed* volume (footprint, delta) over resting size.
4. **Wrong session template for the instrument.** Bank Nifty is rotational; a strong trending stock or a momentum small-cap is not. Profile mean-reversion works best on liquid, balanced instruments and fails on thin, one-directional movers.
5. **Ignoring the higher timeframe.** A perfectly balanced daily profile inside a raging weekly downtrend still favours the short side. Nest the intraday profile inside the daily/weekly value.
6. **Over-reading single sessions.** One day's profile is noisy. Composite (multi-day) profiles reveal the *real* value areas and the balance/imbalance the market is working through.
7. **Data quality.** Profile is only as good as the volume/tick data. Use continuous futures with clean volume; be wary of illiquid strikes or stocks where the distribution is jagged and meaningless.

## Interview-ready summary

Market Profile re-plots a session by *price acceptance* rather than time, revealing the **value area** (the ~70% TPO/volume band where trade was facilitated), the **Point of Control / VPOC** (the most-accepted, magnet price), and the **Initial Balance** (first-hour frame). Its foundation is auction theory: price seeks a level that facilitates trade, and every move is a test of *acceptance vs rejection*. The profile's *shape* classifies the day — a fat bell means rotational (fade the edges toward POC), a thin elongated shape means a trend day (go with it, never fade). **Order flow** sits beneath the profile: delta and footprint show *aggression*, while **absorption** (heavy selling that price won't drop on) and **exhaustion** mark turns. The master playbook is *open location vs prior value*: open-inside-value → rotate and fade extremes to POC; open-outside-range → trend or gap-fill depending on the first hour. In India this is potent on Bank Nifty (naturally rotational and deeply liquid), and it's strongest when the VPOC and value-area edges *confluence* with option-chain OI (max-pain, Put/Call writer walls), VWAP, and prior-day levels. The recurring discipline — the one idea that ties it together — is reading, level by level, whether the auction *accepted* the price or *rejected* it.
