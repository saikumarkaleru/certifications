# Reading & Trading the Option Chain (Deep)

*India F&O, 2026. Nifty / Bank Nifty / Fin Nifty. All rules date-stamped — verify current figures on NSE/SEBI/your broker before you trade. STT on options ~0.10% of premium on sell (equity options); STT on exercised/ITM options is ~0.125% of intrinsic settlement value — verify current.*

## The idea

The option chain is the single most information-dense screen an Indian options trader looks at. It is not a "levels" oracle and it is not a crystal ball — it is a real-time map of where premium is being paid, where open interest is stacked, and how the market is pricing volatility across strikes and expiries. An experienced trader reads the chain the way a bond desk reads a yield curve: not for a single number, but for shape, skew, and change.

The chain earns its keep at three moments. First, at **trade selection** — before you put on a spread you want to know which strikes are liquid, where the implied volatility (IV) is rich or cheap, and whether the strike you like is a crowded OI wall or an empty one. Second, at **intraday decision points** — when Nifty is pinned near a big open-interest strike into expiry, the chain tells you whether dealers are likely to defend that pin. Third, at **risk read** — the put-call ratio, the IV term structure, and the change-in-OI columns together tell you whether the market is complacent or braced.

The honest caveat up front: retail traders routinely over-read the chain. "Max pain," "OI support/resistance," and "PCR says bullish" get treated as mechanical signals. They are soft, contextual, and frequently wrong on any single day. What the chain reliably gives you is **relative** information — this strike vs that strike, today vs yesterday, calls vs puts — and pricing information you can arbitrage against your own view. Use it for edge in construction and timing, not as a directional signal generator.

## The mechanics

A live NSE option chain for one expiry is a table centred on the at-the-money (ATM) strike, calls on the left, puts on the right, strikes running down the middle. For each strike you get, per side: LTP (last traded premium), bid/ask, volume, Open Interest (OI), change in OI, and IV. The columns that carry the most signal:

| Column | What it measures | How a pro uses it |
|---|---|---|
| **OI** | Total open contracts at that strike | Where positions are *stacked* — potential magnets/walls |
| **Change in OI** | Net new positions today | *Fresh* activity — far more informative than raw OI |
| **IV** | Implied vol per strike | Skew shape; rich/cheap vs your forecast |
| **Volume** | Contracts traded today | Liquidity + conviction; OI without volume is stale |
| **Bid/Ask spread** | Cost to cross | Tradability; wide = you bleed on entry/exit |
| **LTP** | Last premium | Mark, but check against bid/ask mid |

**Strikes and lots (2026, verify current).** Nifty strike interval is 50; lot size 75. Bank Nifty strike interval 100; lot size 30 (verify — SEBI/NSE revised lot sizes through 2024–25). Fin Nifty strike interval 50. Under SEBI's 2024–25 expiry rationalisation, each exchange now runs limited weekly expiries — Nifty weekly on NSE (typically Thursday), and index weeklies were consolidated so that not every index has its own weekly. **Verify the exact weekly-expiry calendar for each index on NSE for 2026 before trading — this changed materially in 2024–25.**

**OI mechanics.** OI rises by one when a *new* buyer and *new* seller open a contract; it falls when both close. So OI change decomposes into four states, and reading them is the actual skill:

| Price | OI | Interpretation |
|---|---|---|
| Up | Up | Longs building — trend backed by fresh money |
| Down | Up | Shorts building — bearish conviction |
| Up | Down | Short covering — rally may be hollow |
| Down | Down | Long unwinding — fall may be hollow |

For options specifically, a call OI build at a strike overhead often means writers (sellers) expect the index to stay below it — that strike behaves like resistance *because* writers defend it by delta-hedging. But this can flip violently: if spot pushes through, those short calls flip to buying delta and fuel the move (gamma squeeze). OI "support/resistance" is therefore conditional, not structural.

**Put-Call Ratio (PCR).** PCR (OI) = total put OI / total call OI. Above ~1.3 is often read as oversold/fearful (lots of puts written or bought); below ~0.7 as complacent. But PCR is a *level in context* — Bank Nifty routinely runs a different baseline than Nifty. Track PCR's **change** and its **percentile vs its own recent range**, not the absolute number.

**IV skew and term structure.** Plot IV against strike: index puts trade at higher IV than equidistant calls (the classic equity "put skew" / smirk) because crash risk is bid. Plot ATM IV against expiry: normally upward-sloping (contango). When the front weekly's IV spikes above later expiries (backwardation), the market is pricing a near-dated event — earnings-heavy weeks, RBI policy, budget, US Fed, elections. India VIX is the 30-day model-free vol on Nifty; treat it as the anchor and read the chain's per-strike IV as deviations around it.

## Worked trade

**Setup (illustrative levels, verify live).** Date: a Monday, Nifty spot 24,000. Weekly expiry Thursday (3 sessions out). India VIX 12.5 — historically low, complacent. I want to read the chain to select a trade, not force a direction.

**Reading the chain:**

| Strike | Call OI (lots) | Call ΔOI | Call IV | Put OI | Put ΔOI | Put IV |
|---|---|---|---|---|---|---|
| 24,300 | 92,000 | +40,000 | 10.8% | 8,000 | +500 | — |
| 24,200 | 71,000 | +30,000 | 11.0% | 14,000 | +1,000 | 11.9% |
| 24,100 | 58,000 | +18,000 | 11.3% | 26,000 | +4,000 | 12.1% |
| **24,000 (ATM)** | 41,000 | +9,000 | 11.6% | 44,000 | +12,000 | 12.4% |
| 23,900 | 22,000 | +2,000 | 12.0% | 61,000 | +22,000 | 12.9% |
| 23,800 | 12,000 | +1,000 | 12.4% | 88,000 | +48,000 | 13.6% |
| 23,700 | 7,000 | +500 | 12.9% | 79,000 | +30,000 | 14.2% |

What this tells me: heavy **call writing at 24,200–24,300** (big ΔOI on calls above spot) and heavy **put writing at 23,800–23,900** (big ΔOI on puts below spot). The market is building a **short-strangle / range expectation**: writers on both wings betting Nifty stays roughly 23,800–24,300 into Thursday. PCR is mildly bullish-to-neutral. Put IV > call IV confirms the standard skew; VIX at 12.5 says premium is cheap in absolute terms.

Two coherent trades come out of this read:

**Trade A — fade the complacency (long vol).** VIX 12.5 is near the floor; front-week IV ~11.6% ATM is cheap. Buy a slightly OTM strangle or a debit structure if I expect a break. But long premium into 3-day theta with low IV is a bleed unless I'm confident of a move.

**Trade B — join the writers with defined risk (iron condor).** The chain is *telling* me where the crowd expects the range. Rather than blindly short strangle (undefined risk, ugly if VIX 12.5 is the calm before a gap), I build an **iron condor** anchored on the OI walls:

- Sell 24,200 CE @ ₹42, Buy 24,350 CE @ ₹14 → call spread credit ₹28
- Sell 23,800 PE @ ₹40, Buy 23,650 PE @ ₹15 → put spread credit ₹25
- **Net credit ₹53 × 75 = ₹3,975 per lot**
- Max loss per wing = 150 (strike width) − 53 (total credit) = ₹97 × 75 = **₹7,275 per lot**
- Breakevens: 24,253 up / 23,747 down
- Net Greeks near entry: delta ~flat, **theta positive** (~+₹15/lot/day of decay working for me), **vega negative** (I lose if VIX pops), gamma slightly negative.

**Costs (2026, verify):** 4 legs in, up to 4 out = up to 8 executions. Brokerage on discount brokers is flat (say ₹20/order → ~₹160 round trip). STT on the sell legs ~0.10% of premium sold (verify), plus exchange txn charges, SEBI fee, stamp, and 18% GST on brokerage+txn. On a ~₹4,000 credit these costs run roughly ₹120–200 per lot round-trip — material against a ₹3,975 credit, so **size and don't over-trade legs.** If both short strikes expire OTM, I keep close to the credit minus costs.

## Management

**Scenario 1 — Nifty drifts, stays 23,850–24,150 (base case).** Theta does the work. By Wednesday the condor is worth ~₹25 to close (from ₹53 credit). I take profit at ~50–60% of max credit rather than holding to expiry for the last ₹25 — the tail risk of a Thursday gap isn't worth the residual. **Buy back the whole condor, book ~₹28 × 75 = ₹2,100 gross per lot.** This is the disciplined exit: the chain's put-skew is a standing reminder that downside gaps are the fat tail.

**Scenario 2 — Nifty rallies to 24,180 Tuesday, tests the call wall.** The 24,200 short call goes near ATM; short gamma bites, delta turns negative against me. Two adjustments: (a) **roll the untested put spread up** — close 23,800/23,650 put spread (now cheap) and re-sell 23,950/23,800 to collect fresh credit and re-centre; or (b) if I think the wall breaks, **cut the call spread** for a defined loss and keep the put spread. Watch the 24,200 call ΔOI intraday: if writers are *adding* (OI still rising as price approaches), the wall is being defended and the pin may hold; if writers are *covering* (OI falling as price rises), that's the gamma-squeeze warning — get out.

**Scenario 3 — VIX pops from 12.5 to 16 on a global risk-off, spot still inside range.** My vega-negative condor loses on the mark even though spot behaved, because both wings re-price richer. Here the position is *right on direction, wrong on vol.* I hold if within range and let the vega bleed reverse as event passes — but I reduce size if VIX regime is shifting, because a vol spike is often the first candle of a spot move. This is the classic short-vol trap: the P&L looks fine until it doesn't.

**Scenario 4 — Thursday expiry pin.** Into the last hours, Nifty often gravitates toward the strike with the largest combined OI (the "max pain" gravity is real *near* expiry because dealer hedging concentrates). If spot is at 24,050 with the 24,000 strike heavy, expect chop around 24,000. I let OTM legs expire worthless (no STT on worthless, but ITM exercise carries STT ~0.125% of intrinsic — verify — so **square off ITM legs before close** rather than let them be exercised).

## Risk & sizing

**Max loss is defined:** ₹7,275/lot (one wing) minus whatever credit remains — an iron condor can only lose one wing at a time at expiry, so the true max loss is width − credit on the breached side. Never size so that a full-wing loss on max lots exceeds ~1–1.5% of trading capital. On ₹10 lakh capital, that's roughly ₹10,000–15,000 at risk → ~1–2 lots here, not 10.

**Margin (SPAN + Exposure).** A defined-risk iron condor gets **margin benefit** — SPAN recognises the long wings as hedges, so blocked margin is a fraction of a naked strangle. Expect roughly ₹40,000–70,000 per lot of condor margin (verify on your broker's SPAN calculator; it moves with VIX). A *naked* short strangle on the same strikes would block far more (₹1.5–2 lakh+/lot) and carry unlimited tail risk. The margin efficiency is a direct reason to prefer the condor.

**Portfolio Greeks.** Read the book, not the trade. If I already run other short-vega positions, this condor *adds* to a concentrated short-vol exposure — a single VIX spike hits everything at once. Aggregate net vega and cap it: I want book vega such that a +3 VIX move costs no more than a defined fraction of capital. Net delta near flat is comfortable; net gamma is the sneaky risk into expiry — short gamma means my delta swings fast near the short strikes.

**The tail.** The chain's persistent put skew is the market pricing the truth: indices gap down harder than they gap up. A short-vol condor collects small credits many weeks and gives some back in a crash week. Position so that the worst realistic overnight gap (say Nifty −4% on a global event) is survivable at your size. Most retail blow-ups in Indian F&O come from naked option writing sized to the calm, not the storm.

## Pitfalls & interview-ready summary

**Pitfalls:**
- **Treating OI walls as hard support/resistance.** They're conditional; a break flips writers into buyers (gamma squeeze). Watch *change* in OI as price approaches the wall.
- **Trading raw PCR levels.** Context and percentile matter; Bank Nifty's baseline ≠ Nifty's. PCR is a change/regime read, not a signal.
- **Ignoring liquidity.** Deep-OTM strikes show OI but wide spreads — you lose 10–20% on entry/exit. Trade where volume, not just OI, is present.
- **Max-pain worship.** It has gravity only near expiry and only because of dealer hedging; on Monday it's noise.
- **Reading LTP as the price.** Use bid/ask mid; LTP can be a stale off-market print.
- **Forgetting costs on multi-leg trades.** 8 executions of STT+txn+GST can eat a third of a thin credit. Size up per lot rather than over-leg.
- **Confusing "cheap IV" with "good long vol."** VIX 12.5 is cheap, but 3-day theta can still bleed you dry if nothing moves.

**Interview-ready summary:** The option chain is a real-time map of premium, open interest, and per-strike implied volatility across strikes and expiries. The highest-signal columns are **change in OI** (fresh positioning) and **IV skew** (crash pricing), not raw OI or LTP. OI decomposes into long-build / short-build / covering / unwinding via the price-OI matrix. PCR and "max pain" are soft, contextual reads — useful for regime and near-expiry gravity, dangerous as mechanical signals. A disciplined practitioner reads the chain to (1) select liquid strikes, (2) identify rich/cheap IV to trade against a forecast, and (3) size a defined-risk structure like an iron condor anchored on the OI walls, taking profit at 50–60% of credit, respecting the negative-vega tail that the persistent index put skew is warning about.
