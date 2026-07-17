# Relative Rotation Graphs (RRG)

Most technical analysis looks at one instrument in isolation — is Nifty going up or down? But the money that moves markets is almost always a *rotation*: it flows out of one sector and into another, out of large-caps into mid-caps, out of defensives into cyclicals. If you can see that rotation while it is happening rather than after the fact, you can be early into the leaders and out of the laggards. The **Relative Rotation Graph (RRG)** is the single best visual tool ever built for exactly this. This chapter explains what it is, the mathematics underneath it, and precisely how to trade sector and stock rotation on the NSE in 2026.

## What it is & why it works

An RRG is a two-axis scatter plot that shows the **relative strength** and the **momentum of that relative strength** for a basket of securities, all measured against a common benchmark (for Indian markets, almost always the **Nifty 50** or **Nifty 500**). It was created by Julius de Kempenaer and popularised via Bloomberg and StockCharts; on Indian charts it's available on TradingView (via the RRG-style relative-strength studies), on some broker platforms, and on dedicated RRG sites.

The graph has:

- **X-axis: JdK RS-Ratio** — a normalised measure of *relative strength*. Above 100 = the security is outperforming the benchmark; below 100 = underperforming.
- **Y-axis: JdK RS-Momentum** — the *rate of change* of that relative strength. Above 100 = relative strength is improving; below 100 = deteriorating.

The centre of the graph is (100, 100) — the benchmark itself. Every security is plotted as a point, and because both axes evolve over time, each security traces a **tail** — a path showing where it has been over the last several periods.

**Why it works** rests on two robust market truths:

1. **Relative strength trends persist.** Sectors and stocks that are outperforming tend to keep outperforming for weeks to months (the momentum/relative-strength anomaly is one of the most-documented effects in finance). RS-Ratio captures this persistence.
2. **Money rotates in a cycle, not randomly.** Capital leaves an overheated leader, moves to a laggard that is starting to turn, that laggard becomes the new leader, and so on. This cyclical flow shows up on the RRG as a **clockwise rotation** through four quadrants — the entire visual grammar of the tool.

The genius of the RRG is combining *level* (RS-Ratio) and *direction* (RS-Momentum) into one picture, so you see not just who is strong but who is *getting* strong — which is where the future return lives.

## The four quadrants

The plot is divided into four quadrants by the (100,100) crosshair. Read them clockwise:

| Quadrant | Location | RS-Ratio | RS-Momentum | Meaning |
|---|---|---|---|---|
| **Leading** | Top-right | >100 | >100 | Outperforming AND momentum improving — the current leaders |
| **Weakening** | Bottom-right | >100 | <100 | Still outperforming but momentum fading — leaders rolling over |
| **Lagging** | Bottom-left | <100 | <100 | Underperforming and getting worse — the laggards |
| **Improving** | Top-left | <100 | >100 | Still underperforming but momentum turning up — the future leaders |

The healthy, textbook rotation is **clockwise**: a sector travels from Improving (top-left) → Leading (top-right) → Weakening (bottom-right) → Lagging (bottom-left) → back to Improving. Money flows in this circle.

The two most actionable quadrants for a trader are:

- **Improving (top-left)** — buy candidates. These are early. RS is still below 100 but momentum has turned up. If they continue clockwise into Leading, you caught the move early.
- **Weakening (bottom-right)** — sell/reduce candidates. Still strong on an absolute-RS basis but losing momentum. This is where you trim winners *before* they crash into Lagging.

## Mechanics & the maths (settings)

You do not need to compute RRG by hand — every platform does it — but understanding the maths keeps you from misreading it.

**Step 1 — Relative Strength (RS):** For each security, RS = (Security price / Benchmark price). If Nifty Bank / Nifty 50 is rising, banks are outperforming.

**Step 2 — RS-Ratio (JdK):** The raw RS ratio is noisy, so de Kempenaer normalises it. Conceptually: take the RS line, smooth it, measure how far it sits from its own moving average, and normalise that deviation into an index centred on 100. A reading of 102 means meaningfully above its RS trend; 98 means below.

**Step 3 — RS-Momentum (JdK):** This is essentially the rate-of-change of the RS-Ratio, also normalised around 100. It's a leading measure — momentum turns before the ratio does, which is why Improving-quadrant securities are early signals.

**Settings that matter:**

- **Benchmark:** Nifty 50 for large-cap sector rotation; Nifty 500 if you're comparing across market caps; a sector index if you're rotating *within* a sector (e.g., individual banks vs Nifty Bank).
- **Tail length:** how many periods of history to show. 5–8 tail points is standard. Short tails miss the trajectory; very long tails clutter.
- **Timeframe:** **Weekly RRG** for positional/investment rotation (the classic use — smooth, reliable, low-noise). **Daily RRG** for swing trading (faster, noisier). Intraday RRG exists but is mostly noise; avoid it for decisions.

A crucial reading skill: **the tail's direction and length matter more than the current quadrant.** A security deep in Lagging but with a long tail curling up-and-left toward Improving is more interesting than one sitting still in Leading with a short, flat tail. You are trading the *rotation*, not the snapshot.

## Worked India example (levels & context)

Consider a **weekly RRG of the 11 major NSE sector indices** against Nifty 50 — Bank, IT, Auto, FMCG, Pharma, Metal, Energy, Realty, PSU Bank, Financial Services, Media (reconstructed scenario; verify current positions live on your platform):

Suppose the snapshot shows:

- **Nifty IT** — deep in **Improving** (RS-Ratio 97, RS-Momentum 103), tail curling up from the Lagging quadrant. IT had been the market's dog for two quarters; now money is quietly rotating back in.
- **Nifty Auto** — firmly in **Leading** (RS-Ratio 104, RS-Momentum 102), long tail pointing up-right. The reigning leader, still accelerating.
- **Nifty FMCG** — in **Weakening** (RS-Ratio 101, RS-Momentum 97), tail curling down from Leading. The defensive trade is tiring.
- **Nifty Metal** — in **Lagging** (RS-Ratio 96, RS-Momentum 95), tail still pointing down-left. Avoid.

**The rotation trade:** The RRG tells a coherent macro story — leadership is passing from defensives (FMCG weakening) and toward IT (improving), while Auto still leads. Your playbook:

1. **Add/hold Auto** — it's Leading with strong momentum; stay long the sector's strongest stocks. But watch for its tail to flatten (the early sign of a move to Weakening).
2. **Start accumulating IT** — the Improving quadrant with an up-curling tail is the highest-value early signal. You buy the leading IT names (say the sector heavyweight and one mid-cap IT name breaking out on its own chart) *before* the crowd confirms the rotation.
3. **Trim FMCG** — Weakening quadrant; book profits on defensive holdings and redeploy into IT/Auto.
4. **Ignore Metal** — Lagging with a down tail; no reason to be there until its tail curls.

The dated-level layer: you don't buy the *sector* — you use the RRG to pick the *pond*, then use conventional TA (breakouts, moving averages, OI) to pick the *fish* and set entries/stops. If IT is Improving on the RRG and the sector heavyweight is breaking out above, say, ₹4,200 resistance on rising volume, you enter there with a stop below the breakout — the RRG gave you the *conviction and timing* to trust that breakout because the sector's relative momentum is with you.

## How to trade it (entry / stop / target)

RRG is a **top-down selection and timing filter**, not an entry-trigger tool. Use it in layers:

| Element | Rule |
|---|---|
| **Universe selection** | Plot sector indices (or a stock basket) vs Nifty on a **weekly** RRG |
| **Buy zone** | Securities in **Improving** with an up-curling tail, or early **Leading** with a lengthening tail |
| **Sell/trim zone** | Securities in **Weakening** with a down-curling tail; exit fully as they cross into **Lagging** |
| **Actual entry** | Drop to the security's own chart; enter on a conventional trigger (breakout, MA reclaim, pullback to support) *in the RRG-favoured direction* |
| **Stop** | Set on the price chart (below breakout/support), not on the RRG |
| **Target/exit** | Ride until the RRG tail rotates into Weakening/Lagging, or the price chart gives an exit; the RRG is your *hold-or-fold* gauge |
| **Timeframe** | Weekly for positional; daily for swing; never intraday for decisions |
| **Regime** | Works in any regime, but rotation signals are cleanest in trending markets; in a flat, correlated market everything clusters near (100,100) and there's little to trade |

## Confluence (including OI & breadth)

RRG becomes far more powerful stacked with other layers:

- **Breadth confirmation:** if the RRG says Banking is rotating into Leading, check the Nifty Bank advance-decline and the % of bank stocks above their 50-DMA. Broad participation confirms the rotation is real, not one heavyweight.
- **Option OI (F&O):** once the RRG points you to a leading sector, use the sector index option chain (Bank Nifty, Fin Nifty) to time entries — buying support near heavy put-OI strikes, taking profit near heavy call-OI walls. The RRG picks the sector; OI refines the level.
- **Relative-strength on the stock chart:** within an Improving sector, rank individual stocks by their *own* RS vs the sector. Buy the strongest stock in the strengthening sector — "double relative strength."
- **Sector-vs-benchmark price confirmation:** the RRG's RS-Ratio should agree with the raw sector/Nifty ratio line trending up. If they disagree, trust the raw price ratio.

## Pitfalls

- **Treating RRG as an entry signal.** It is a *selection and timing* tool for baskets, not a candle-level trigger. Always confirm on the price chart.
- **Whipsaw near the centre.** Securities hovering around (100,100) flip quadrants on noise. Only act on securities with clear, lengthening tails away from the centre.
- **Wrong benchmark.** Plotting mid-caps against Nifty 50 during a broad mid-cap rally makes everything look Leading — meaningless. Match the benchmark to your universe.
- **Timeframe mismatch.** Using a daily RRG for a positional portfolio produces constant, contradictory rotation. Use weekly for positional decisions.
- **Ignoring the tail's shape.** The snapshot quadrant is the least important thing. A stock in Leading with a tail curling *down* is a sell, not a buy — the direction of travel is everything.
- **Correlation blindness in crashes.** In a sharp market-wide sell-off, correlations spike toward 1 and the RRG collapses toward the centre — sector rotation stops meaning anything until the panic clears. Don't force rotation trades in a crash.
- **Survivorship in the basket.** If you only plot the current index constituents, you miss stocks recently added/removed; keep the basket meaningful and current.

## Building an RRG-driven rotation routine

A practical weekly routine an Indian positional trader can run every weekend:

1. **Sector scan (weekly RRG, benchmark = Nifty 50):** note which sectors are in Improving and early Leading (your buy universe) and which are Weakening/Lagging (your avoid/trim universe). Write down the clockwise story: "leadership passing from X to Y."
2. **Confirm with breadth:** for each favoured sector, check % of constituents above the 50-DMA and the sector advance-decline. Demand broad participation.
3. **Stock scan (weekly RRG within the sector, benchmark = sector index):** find the strongest 2–3 stocks in each favoured sector.
4. **Chart & OI timing:** on each shortlisted stock, mark the breakout/support level and, for F&O names, the OI walls. Set alerts.
5. **Execute on trigger:** enter only when the price chart confirms in the RRG-favoured direction. Stops on the price chart.
6. **Manage by rotation:** hold while the sector tail stays in Leading; trim as it rotates to Weakening; exit as it enters Lagging. Recycle capital into the next Improving sector.

This routine mechanises the single most valuable thing the RRG offers: **being early into strengthening sectors and out of tiring ones**, systematically, every week, instead of chasing whatever rallied yesterday.

## Interview-ready summary

*A Relative Rotation Graph plots a basket of securities against a benchmark (Nifty 50 for Indian sectors) on two axes: JdK RS-Ratio (relative strength, X) and JdK RS-Momentum (rate of change of that strength, Y), both centred on 100. Securities rotate clockwise through four quadrants — Improving (top-left, early buys), Leading (top-right, momentum leaders), Weakening (bottom-right, trim), Lagging (bottom-left, avoid). It works because relative-strength trends persist and capital rotates cyclically between sectors. Use it top-down: pick strengthening sectors on a weekly RRG, then use conventional TA and option OI on the stock chart to time entries and stops. It is a selection-and-timing filter, not an entry trigger — and the direction and length of a security's tail matter far more than the quadrant it currently sits in.*
