# The Intraday TA Playbook

## What it is & why it works

An intraday playbook is a written, rule-bound decision tree that converts everything you know about technical analysis into a *repeatable sequence of actions* for a single Indian trading session — 09:15 to 15:30 IST. It is not a strategy; it is the operating system that decides *which* strategy is allowed to run *when*, on *what*, and with *how much* size. The difference between a trader with a playbook and one without is the difference between a surgeon following a checklist and someone improvising with a scalpel.

Intraday TA works — to the extent it works — because of three durable behavioural facts about the Indian session:

1. **Time-of-day structure is real.** The auction is not uniform across the session. The opening 15-45 minutes (09:15-10:00) carry the overnight gap, global cues (SGX Nifty / GIFT Nifty, Dow, Nasdaq futures, crude, USD-INR) and the largest order imbalances. The mid-session lull (roughly 11:30-13:30) sees volume and range contract as institutional desks step back. The final hour (14:30-15:30) brings position squaring, MIS auto-square-off pressure, and directional resolution. A playbook that trades the open like the lunch lull will bleed.

2. **Liquidity concentrates in a handful of instruments.** Nifty 50 futures, Bank Nifty (weekly expiry Thursday), Fin Nifty, and roughly 30-40 large-cap F&O stocks (Reliance, HDFC Bank, ICICI Bank, SBI, Infosys, TCS, Tata Motors, Axis Bank, L&T) absorb the vast majority of intraday flow. Tight spreads and reliable fills are a prerequisite for a repeatable edge. Illiquid mid-caps give you slippage that eats the entire edge.

3. **Intraday reversion and continuation both exist, but not at the same time.** In a trending session, pullbacks to VWAP or a rising 20-EMA get bought; in a balanced/range session, extremes at the day's high/low get faded. The single most valuable skill is *classifying the day type early* and only deploying the strategy that matches it.

The playbook exists because under live P&L stress your prefrontal cortex degrades. Rules written in a calm mind on Sunday are the only thing that survives the adrenaline of 09:16 on Monday.

## The mechanics

A complete intraday playbook has five modules: **pre-market prep, day-type classification, the setups themselves, execution & risk rules, and the review loop.**

### 1. Pre-market routine (08:45-09:15)

| Item | What to record | Why |
|---|---|---|
| Global cues | GIFT Nifty premium/discount vs prev close; Dow/Nasdaq futures; crude, USD-INR | Sets gap expectation and bias |
| Prior day levels | PDH, PDL, prev close, prev day VWAP | Reference magnets/rejections |
| Overnight range | High/low of the 15:30-onwards + Asian session | Gap context |
| Key S/R | Weekly pivot, round numbers (Nifty 24000/24500), swing highs/lows | Decision zones |
| Event calendar | RBI policy, US CPI/FOMC, expiry (Thu Bank Nifty), results | Reduce/avoid size |
| Option-chain | Max-pain, highest OI Call (resistance) & Put (support) strikes, PCR | Sticky levels + sentiment |

### 2. Day-type classification (decided by ~09:45-10:15)

- **Trend day (up/down):** Opens with a gap or a strong first 15-min candle, holds above/below the opening range, VWAP slopes cleanly, price makes higher-highs / lower-lows and never revisits the open. ~20-25% of days. Trade *with* it, buy pullbacks.
- **Range / balanced day:** Opens inside prior value, oscillates around VWAP, repeatedly rejects PDH/PDL. Majority of days. Fade extremes.
- **Trend-then-range / range-then-breakout:** Common hybrids. The open resolves, then consolidates.

### 3. Core setups (only 3-4; a playbook is defined by what it *excludes*)

| Setup | Trigger | Best day type | Stop |
|---|---|---|---|
| Opening Range Breakout (ORB) | Break of 09:15-09:30 (or 09:45) range with volume | Trend | Opposite side of range |
| VWAP pullback continuation | Retrace to VWAP/20-EMA in a trend, reversal candle | Trend | Below VWAP swing |
| Range fade | Rejection wick at PDH/PDL/OI wall | Range | Beyond the extreme |
| Failed-breakout reversal | Break of level fails, closes back inside | Range/reversal | Beyond the failed extreme |

### 4. Execution & risk rules (the non-negotiable spine)

- **Risk per trade:** fixed fraction, e.g. 0.5-1.0% of capital. On ₹5,00,000 that is ₹2,500-₹5,000 max loss per trade.
- **Position size = Risk ÷ (entry − stop).** Size is an *output*, never a feeling.
- **Daily stop:** 2-3 losing trades OR −2% on the day → flat, screens off. This is the single rule that saves careers.
- **Max trades:** cap (e.g. 4-5) to prevent overtrading in chop.
- **No averaging losers intraday.** Ever.
- **MIS square-off awareness:** brokers auto-close MIS ~15:10-15:20; exit on your terms before that.

### 5. Review loop

Every trade logged: setup name, screenshot, entry/stop/target, R multiple, day-type, adherence (did you follow the rule?). Grade *process*, not outcome.

## Reading it — a worked Bank Nifty session

Take a realistic Bank Nifty Thursday (weekly expiry) with prior close 51,200.

**Pre-market (08:50):** GIFT Nifty +90 points, Dow up 0.7% overnight. PDH 51,480, PDL 50,950. Option chain shows heavy Call OI at 51,500 (resistance) and heavy Put OI at 51,000 (support); PCR 0.85 (mildly bearish/balanced). Expiry, so premiums will decay fast — favour directional moves early, avoid holding options into the afternoon theta bleed.

**09:15-09:30 (opening range):** Gap-up open at 51,290. First 15-min candle prints a range of 51,340 (high) to 51,240 (low) on strong volume. VWAP tracks near 51,290. This is my ORB reference: **51,340 up / 51,240 down.**

**09:30-09:45 (classification):** Price pushes to 51,360, pulls back to VWAP at 51,300, holds, and makes a higher low at 51,320. VWAP is sloping up. No revisit of the low. This is behaving like a **trend-up day**, but 51,500 Call OI looms as a ceiling — so I target *toward* 51,500, not beyond, until proven.

**09:50 (ORB trigger):** A 5-min candle closes at 51,375, clearing the 51,340 opening-range high on above-average volume. Entry long on the retest of 51,345.

- Entry: 51,345
- Stop: 51,290 (below VWAP and the higher low) → risk 55 points
- Target 1: 51,480 (PDH), Target 2: 51,500 (Call wall) — measured move roughly equal to the opening range projected up also points near 51,440.

**10:30:** Price grinds to 51,470, stalls at PDH. I book half at 51,470 (+125 pts, ~2.3R) and trail the rest to breakeven (51,345). Price tags 51,505, rejects hard off the 51,500 Call wall with a long upper wick — the OI wall did its job. Trailed stop at 51,420 catches the runner as it slips back, out for +75 pts.

**Mid-session (11:45-13:15):** Range collapses to 51,380-51,460, VWAP flat. **Playbook says: stand aside.** No trend, no clean extreme. I take zero trades. This discipline is the edge.

**14:40 (final hour):** Price breaks 51,380 support on rising volume, VWAP now flat-to-down. But I've hit my daily target and taken my two quality trades; per my max-trade and don't-give-back rules, I watch only. Session closes 51,410.

**Net:** two clean partials, roughly +2.3R realised, no give-back, no lunch-hour chop trades. That is a *good day* — not because of the rupees but because every action matched a written rule.

## Trading it — entries, stops, targets, scenarios

**Entry triggers** must be objective and candle-close based (or a defined tick beyond a level with volume), never anticipatory:

- ORB: 5-min close beyond the opening range + volume ≥ 1.5× the average of the first candles. Enter on break or on the *retest* (higher win-rate, occasionally misses runaways).
- VWAP pullback: in an established trend, price tags VWAP/20-EMA, prints a reversal candle (hammer/engulfing), enter on the break of that candle's high (long).
- Range fade: price pokes PDH/PDL or an OI wall, prints a rejection wick, closes back inside — enter on the close, stop just beyond the wick.

**Stops** are structural, not monetary — placed where the setup is *invalidated*, then size adjusted so that distance equals your fixed risk. For Bank Nifty, a 40-60 point stop is typical intraday; for Nifty, 25-40; for a stock like Reliance, below the pullback swing low.

**Targets & measured moves:**
- ORB measured move = opening-range height projected from the breakout.
- VWAP pullback target = prior swing high / next OI wall / previous day's value-area edge.
- Always scale: book 50% at 1.5-2R, trail the rest with a rising swing-low or the 20-EMA / VWAP.

**Management scenarios:**
1. *Clean runner:* trail behind 5-min swing lows; let it breathe; don't strangle a trend day with a tight stop.
2. *Immediate stall:* if price doesn't move 1R in your favour within ~3-4 candles, tighten to breakeven — momentum trades pay quickly or not at all.
3. *Chop after entry:* if the tape goes two-sided (overlapping candles, shrinking range), exit flat; the day-type has changed under you.
4. *Gap against overnight (for BTST spillover):* respect it — don't fight a strong gap in the first 15 minutes.

## Confluence — stacking the odds with OI and structure

A single trigger is a coin-flip with an edge; **confluence is where intraday probability actually lives.** The highest-quality intraday setups stack three or more independent factors:

- **Level + VWAP + OI:** an ORB long that also reclaims VWAP *and* sits below a supportive Put wall (buyers defending) is far stronger than an ORB in a vacuum. In the Bank Nifty example, the long worked into a 51,500 Call wall — so I *capped* the target there rather than expecting a runaway. Reading OI walls as intraday magnets/ceilings is the single most India-specific edge on this list.
- **PCR & OI shift:** rising PCR intraday (put writers confident) supports longs; call writers piling into a strike mark it as a ceiling. Watch *change* in OI, not just the static number.
- **Multi-timeframe alignment:** the 5-min entry should agree with the 15-min trend and the daily bias. Longs on the 5-min against a bearish daily are counter-trend scalps — smaller size, faster targets.
- **Volume & delivery:** breakouts need participation. A level break on shrinking volume is a trap.
- **Sector/index confirmation:** a long in ICICI Bank is stronger when Bank Nifty itself is trending up and advance-decline is positive. Trading a stock against its index is swimming upstream.
- **India VIX:** high VIX (>16-18) means wider stops and bigger ORB ranges; low VIX means tighter ranges, favour fades over breakouts.

The rule: **no confluence, no trade — or trade it at half size.** The playbook's power is in refusing the mediocre 50/50 setup to keep powder for the 3-factor A+ setup.

## Pitfalls & false signals

- **Overtrading the lunch lull.** The 11:30-13:30 window generates the most low-conviction, boredom-driven trades. Most intraday accounts die here, one small revenge-scalp at a time. The playbook's max-trades and mid-session stand-aside rule exists precisely for this.
- **Opening-range fakeouts.** The first break often reverses (a "trap" for breakout chasers). Filter with volume, prefer the retest entry, and demand a *close* beyond the range, not a wick.
- **Fighting a trend day with fades.** Fading PDH on a genuine trend-up day is a fast way to compound losses. Classify the day *before* choosing fade vs. continuation.
- **Ignoring expiry mechanics on Bank Nifty Thursday.** Pin risk near max-pain, violent theta decay, and end-of-day option gyrations make late-session option-buying a coin flip. Trade the underlying/futures or exit early.
- **Revenge trading after a stop.** The daily-stop rule (2-3 losses → done) is the antidote. If you feel the urge to "make it back", you have already lost the process.
- **Averaging into a loser.** Intraday, this converts a defined 1R loss into an account-threatening event. Never.
- **Confusing a good outcome with a good process.** A rule-breaking trade that happens to profit is a *loss* for your discipline — it will be repeated and eventually punished. Grade adherence.
- **No pre-market prep.** Trading blind to global cues, event risk (RBI/FOMC/CPI), and OI walls is guessing. The prep table is the cheapest edge available.

## Interview-ready summary

"An intraday playbook is my written operating system for one NSE session. Pre-market I log global cues, prior-day levels, the option-chain OI walls and events. In the first 30-45 minutes I *classify the day* — trend or range — because that decides whether I buy pullbacks or fade extremes. I run only three or four defined setups: opening-range breakout and VWAP-pullback continuation on trend days, range fades and failed-breakout reversals on balanced days. Every entry needs confluence — a level plus VWAP plus supportive OI — or I skip it. Size is an output of a fixed 0.5-1% risk and a structural stop, never a feeling. I stand aside in the lunch lull, respect Bank Nifty expiry mechanics, and hit a hard daily stop after two or three losses. Then I log every trade and grade the *process*, not the P&L. The playbook's edge isn't a magic indicator — it's the discipline to trade only A+ setups and to protect capital so I'm still here next week."
