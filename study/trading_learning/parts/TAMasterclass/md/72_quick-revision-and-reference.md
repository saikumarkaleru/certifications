# Quick-Revision Cheat-Sheet & Indicator/Formula Reference

## What it is & why it works

This is the closing reference chapter of the masterclass — the single page (well, several) you photograph on your phone the night before an interview, a live market open, or an exam. It compresses the entire book into scannable tables: indicator formulas and default settings, pattern targets, option-chain reads, the price-OI matrix, key Indian levels and market timings, position-sizing arithmetic, and a pre-trade checklist.

Why a compression like this "works" is a genuine cognitive point, not filler. Under time pressure — the last minute before the bell, an interviewer's rapid-fire follow-up — you don't have the working memory to *derive* things. You need *retrieval cues*: a formula seen fifty times, a target rule stated the same way every time, a checklist that runs on rails so your discipline survives your adrenaline. The market behaviour this defends against is your own: the well-documented tendency to abandon your process exactly when it matters most (chasing a breakout, widening a stop, freezing on a scenario question). A cheat-sheet externalises the process so the decision is already made before emotion arrives. Everything here is drawn from the earlier chapters and stated in India-first terms — Nifty, Bank Nifty, Fin Nifty, rupees, NSE timings, 2026 levels — so the reference matches the market you actually trade.

Use it as a *revision* tool (test yourself against each table), not a substitute for understanding the chapters. A formula without its "why" is a trap; every row here has its reasoning in the body of the book.

## The mechanics — how the reference is organised

Nine reference blocks, each a self-contained table or list you can revise in isolation:

| Block | Contents |
|-------|----------|
| A | Indicator formulas & default settings |
| B | Interpretation quick-reads (levels & thresholds) |
| C | Chart-pattern targets & triggers |
| D | Candlestick one-liners |
| E | Option-chain & OI reference (incl. price-OI matrix) |
| F | Greeks & IV quick-reference |
| G | Indian market facts, timings, key levels (2026) |
| H | Position sizing & risk arithmetic |
| I | The pre-trade checklist & the scenario-answer template |

### Block A — Indicator formulas & default settings

| Indicator | Formula (core) | Default | Type |
|-----------|----------------|---------|------|
| SMA | Σ(closes)/n | 20, 50, 200 | Trend |
| EMA | Price×k + EMA_prev×(1−k), k = 2/(n+1) | 20, 50 | Trend |
| RSI | 100 − 100/(1+RS); RS = avg gain/avg loss | 14 | Momentum |
| Stochastic %K | 100×(Close − Low_n)/(High_n − Low_n) | 14,3,3 | Momentum |
| MACD | (12-EMA − 26-EMA); signal = 9-EMA of MACD | 12,26,9 | Trend/momentum |
| Bollinger Bands | 20-SMA ± 2σ (of 20 closes) | 20, 2 | Volatility |
| ATR | Avg of True Range; TR = max(H−L, |H−Cₚ|, |L−Cₚ|) | 14 | Volatility |
| ADX | Smoothed |+DI − −DI|/(+DI + −DI) | 14 | Trend strength |
| VWAP | Σ(price×vol)/Σ(vol), from session open | intraday | Volume/mean |
| Supertrend | ±multiplier×ATR around (H+L)/2 | 10, 3 | Trend/stop |
| OBV | Cumulative: +vol on up-close, −vol on down-close | — | Volume |
| Ichimoku | Tenkan 9, Kijun 26, Span B 52, shift 26 | 9,26,52 | Trend system |

*Revision cue:* every oscillator is a **transformation of price/volume** → it lags and repackages, never predicts.

### Block B — Interpretation quick-reads

| Signal | Reading | The trap |
|--------|---------|----------|
| RSI > 70 | Overbought | In a strong trend, stays >70 for weeks — NOT a short alone |
| RSI < 30 | Oversold | In a downtrend, stays <30 — NOT a buy alone |
| RSI 50 line | Momentum midpoint; long-bias filter | More robust than 30/70 in trends |
| MACD zero-line cross | Regime/trend shift (slower, reliable) | Lags |
| MACD signal cross | Momentum trigger (faster, noisier) | Whipsaws in range |
| Bollinger squeeze | Vol contraction → move likely soon | Gives no direction |
| Price walks upper band | Trend strength | NOT a sell — band is a stat envelope |
| ADX < 20 | No trend (range) → turn off trend tools | — |
| ADX > 25 | Trending → trend tools valid | Level only; direction from DI |
| Golden/Death cross | Regime marker (50/200 DMA) | Late, whipsaw-prone entries |
| Divergence (price vs osc) | WARNING of momentum weakening | A condition, NOT a trigger — wait for the break |

### Block C — Chart-pattern targets & triggers

| Pattern | Trigger (confirm) | Measured target |
|---------|-------------------|-----------------|
| Head & Shoulders (top) | Close below neckline | Neckline − (head − neckline) |
| Inverse H&S | Close above neckline | Neckline + (neckline − head) |
| Double top | Close below middle trough | Trough − (top − trough) |
| Double bottom | Close above middle peak | Peak + (peak − bottom) |
| Ascending triangle | Break above flat top | Breakout + triangle height |
| Descending triangle | Break below flat base | Break − triangle height |
| Symmetrical triangle | Break either side (prefer pre-apex) | Break ± widest height |
| Bull/Bear flag | Break of flag in pole's direction | Breakout + pole height |
| Pennant | Break in pole's direction | Breakout + pole height |
| Cup & handle | Break above rim | Rim + cup depth |
| Rectangle/range | Close outside the range | Break ± range height |

*Rules that apply to all:* confirm on a **close** not a wick; prefer volume expansion on the break; the **retest** of the broken level is the lower-risk entry; a break that immediately reverses back inside is a **failed pattern** (trade the failure).

### Block D — Candlestick one-liners

| Candle | Location | Meaning |
|--------|----------|---------|
| Bullish engulfing | At support / downtrend low | Demand overwhelms supply |
| Bearish engulfing | At resistance / uptrend high | Supply overwhelms demand |
| Hammer | Downtrend low | Lower prices rejected |
| Shooting star | Uptrend high | Higher prices rejected |
| Doji | Anywhere (matters at extremes) | Indecision / balance |
| Morning star | Downtrend low | 3-candle bullish reversal |
| Evening star | Uptrend high | 3-candle bearish reversal |
| Marubozu | In trend | Conviction / continuation |
| Inside bar | Consolidation | Compression → breakout pending |
| Liquidity sweep / trap | Beyond an obvious level | Runs stops then reverses — trade the reclaim |

*Golden rule:* a candle without **location** (at a level/structure) is noise.

### Block E — Option-chain & OI reference

**Price–OI build-up matrix (memorise cold):**

| Price | OI | Name | Bias |
|-------|-----|------|------|
| Up | Up | Long build-up | Bullish (fresh longs) |
| Down | Up | Short build-up | Bearish (fresh shorts) |
| Up | Down | Short covering | Weak-up (may fade) |
| Down | Down | Long unwinding | Weak-down (may fade) |

**Chain reads:**

| Tool | Definition | Use |
|------|-----------|-----|
| OI | Outstanding contracts at a strike | Conviction; rising = new money |
| Volume | Contracts traded this period | Activity; can be flat OI (day-trade) |
| Call OI wall | Strike with heaviest call OI | Resistance ceiling |
| Put OI wall | Strike with heaviest put OI | Support floor |
| PCR | Put OI / Call OI | Sentiment extreme (contrarian); use at tails only |
| Max-pain | Strike minimising total option-holder payout | Soft expiry magnet; fails in strong trends |
| Expected range | Between put wall and call wall | Trade the rails / write premium |

*PCR rough map:* >1.3 heavy put-writing (contrarian-bullish); <0.7 heavy call-writing (contrarian-bearish). Direction of the OI *change* matters more than the ratio's level.

### Block F — Greeks & IV quick-reference

| Greek | Measures | Trader use |
|-------|----------|-----------|
| Delta | Δoption per ₹1 in underlying (≈ prob. ITM) | Strike selection to match conviction |
| Gamma | Δdelta per ₹1 move | Highest near ATM/expiry — fast-changing risk |
| Theta | Premium lost per day (time decay) | Brutal on weeklies into expiry — buyers need speed, writers harvest |
| Vega | Δoption per 1% IV change | Event risk — the source of IV crush |
| IV / India VIX | Market's forward vol expectation | Buy options when IV low; write when rich; sizes ranges |

*The classic trap:* right on direction, still lose on a long option post-event → **IV crush** (vega loss > delta gain). Buying options into results/RBI/Budget is a volatility bet as much as a direction bet.

### Block G — Indian market facts, timings & 2026 levels

| Item | Detail |
|------|--------|
| Cash/F&O session | 09:15–15:30 IST; pre-open 09:00–09:15 |
| Nifty 50 | Broad-market benchmark; ~23,000–27,000 (2026 zone) |
| Bank Nifty | Heaviest sector; leads/confirms Nifty; ~50,000–58,000 |
| Fin Nifty | Financial-services index; ~24,000–27,000 |
| Weekly expiries | Index weeklies (check current NSE schedule); theta accelerates last 2 days |
| Key psych levels | Nifty round 24,000/25,000/26,000; Bank Nifty 50,000/55,000 |
| 200-DMA | The institutional bull/bear regime line on Nifty |
| India VIX | Expected 30-day Nifty vol; contrarian (spikes ≈ capitulation lows) |
| USDINR / DXY | Rising DXY / weak rupee ≈ FII outflow headwind for Nifty |
| Delivery % | High delivery on up-move = genuine accumulation vs churn |

*Confirmation habit:* a Nifty move that **Bank Nifty won't confirm** is fragile (Dow's confirmation tenet, modernised).

### Block H — Position sizing & risk arithmetic

**The one equation that governs everything:**

> **Position size = Rupee risk per trade ÷ Stop distance (per unit)**

Where rupee risk per trade = account × risk-% (typically 0.5–1.0% for pros).

| Concept | Formula / rule |
|---------|----------------|
| R (the unit of risk) | Entry − Stop (longs); size so 1R = your fixed ₹ risk |
| ATR-based stop | Stop = Entry − (1.5 to 2 × ATR) |
| Reward:risk | (Target − Entry)/(Entry − Stop); demand ≥ 1.5–2 |
| Expectancy | (Win% × avg win) − (Loss% × avg loss); must be > 0 |
| Fixed-fractional | Risk same % of *current* equity each trade |

**Worked example:** Account ₹10,00,000; risk 0.5% = ₹5,000. Long Reliance ₹1,435, stop ₹1,400 → stop distance ₹35 → size = 5,000/35 ≈ **142 shares**. Target ₹1,585 → reward ₹150 vs risk ₹35 ≈ **1:4.3 R:R**. ATR-sizing (Part 1, Q29) equalises risk across volatile and calm names — same ₹ risk, different share counts.

### Block I — The pre-trade checklist & scenario template

**Pre-trade checklist (run every time):**
1. **Regime** — trending or ranging? (ADX, structure). Right tool for the regime?
2. **Structure** — HH/HL or LH/LL? Where's the last swing (invalidation)?
3. **Level** — am I at meaningful support/resistance (with polarity)?
4. **Trigger** — is there a confirmed trigger (close-based break, candle at level, divergence + break)?
5. **Volume/OI** — does participation confirm? Long/short build-up supportive?
6. **Confluence** — do ≥3 independent tools agree? Index/VIX/USDINR aligned?
7. **Risk** — where's the stop, what's the size, is R:R ≥ 1.5–2?
8. **Invalidation** — what exact price proves me wrong, and will I honour it?

**Scenario-answer template (for interviews & live decisions):**
> Regime → Structure/level → Pattern trigger & measured target → OI/IV confirmation or contradiction → Invalidation level → How I'd manage a disagreement.

Answer as a *process with defined risk*, never a one-word prediction.

## Reading it — a worked one-minute revision run

Before a Bank Nifty session, run the sheet top-to-bottom in sixty seconds. Suppose spot 54,600, four-week ascending triangle capped at 55,000, 55,000 call is the biggest call OI, 54,000 put the biggest put OI, ADX 27, India VIX calm. Read across the blocks: **G** — 55,000 is a psych + call-wall resistance, 54,000 a put-wall support, expected rail range 54,000–55,000. **B/A** — ADX 27 = trending, so trend tools valid. **C** — ascending triangle, target on a *close* above 55,000 = 55,000 + (55,000−53,200) ≈ 56,800. **E** — watch whether 55,000 call OI *falls* on the test (wall cracking → short-covering fuel) or *rises* (wall holds → likely fail back to 54,000). **F** — VIX calm, so no event IV distortion; option-buying theta risk is normal. **H** — if long on a 55,000 close with stop 54,600 (dist 400) and ₹5,000 risk on Bank Nifty lots, size accordingly; target 56,800 gives ~1:4.5. **I** — checklist confirms regime, level, pending trigger, OI to watch, invalidation 54,600. In one minute the sheet has produced a complete, risk-defined plan.

## Trading it — from sheet to order

- **Long trigger:** daily *close* above 55,000 + falling 55,000 call OI + volume → buy; stop 54,600; partial 55,800, target 56,800.
- **Failure trigger:** three rejections at 55,000 with *rising* call OI, then close below 54,600 → short toward 53,200/54,000 put wall; stop above 55,000.
- **Expiry overlay:** if 55,000 is also max-pain, expect the wall to hold *into* expiry — don't chase a late-Thursday poke.
- **Sizing:** always Block H — size = ₹ risk ÷ stop distance, never a round-number lot count picked by feel.

## Confluence

The whole point of a reference sheet is to make **confluence mechanical**. Block I's checklist forces you to require agreement across independent families before you act — structure (Block C/D) + level (Block G) + momentum (Block B) + volume/OI (Block E) + volatility/event (Block F) + cross-market (Block G). A single green row is never a trade; three-plus independent green rows is a research call. The sheet's job is to stop you acting on one tool in isolation — the error that quietly drains most accounts.

## Pitfalls & false signals

- **Using the sheet as a substitute for the "why."** A formula recalled without its reasoning (RSI 78 ≠ automatic short) is worse than not knowing it — it produces confident mistakes.
- **Treating soft references as laws.** Max-pain, PCR, round numbers, band edges — all *soft*; they bend in strong trends and news.
- **Skipping the checklist under adrenaline.** The exact moment you're tempted to skip step 7 (risk) or step 8 (invalidation) is the moment you most need them.
- **Stale levels.** The 2026 Nifty/Bank Nifty zones here are anchors, not truth — update the numbers, keep the logic.
- **One-tool trades.** The sheet exists precisely to prevent this; honour the confluence requirement.

## Interview-ready summary

This reference distils the masterclass into retrieval cues: indicators are lagging transformations of price/volume (Block A–B); patterns give a bias, a *close*-confirmed trigger, and a measured target (C–D); the option chain shows whose money is behind the move via the price-OI matrix, OI walls, PCR and max-pain (E), while Greeks and IV/VIX decide whether an options expression pays even when the chart is right (F); Indian context — Bank Nifty confirmation, the 200-DMA regime line, India VIX, USDINR, delivery % (G) — filters it all; and everything is bounded by mechanical risk: size = risk ÷ stop distance, demand R:R ≥ 1.5–2, and run the eight-point checklist every time (H–I). The professional signature is never a one-word call — it is *regime, trigger, target, confirmation, invalidation, management*: a probabilistic plan with defined risk, which is the only honest thing technical analysis can ever offer.
