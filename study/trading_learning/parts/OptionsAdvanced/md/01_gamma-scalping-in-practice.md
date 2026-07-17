# Gamma Scalping in Practice

*India F&O desk note — drafted July 2026. Rules cited (STT, SPAN, expiry structure) reflect 2026 as I understand it; treat every number as "verify current on NSE/SEBI/your broker" before you trade.*

## The idea

Gamma scalping is how you get *paid to be long options* instead of just bleeding theta. When you buy an option you own positive gamma — your delta changes as spot moves, mechanically getting longer as price rises and shorter as it falls. Gamma scalping is the discipline of continuously re-hedging that changing delta with the underlying (futures) so that you *lock in* the P&L that the curvature creates. You buy low and sell high, over and over, in tiny slices, funded by the realised movement of the market. The bet is not on direction. It is on **realised volatility exceeding implied volatility** — the vol you paid for in the premium.

This is the single most important concept separating a directional option buyer from a volatility trader. The directional buyer holds a long straddle, waits for a big move, and prays it arrives before theta eats the premium. The gamma scalper *harvests* every wiggle along the way. If the underlying oscillates enough — if the sum of squared daily moves beats the implied variance baked into the premium — the scalps pay for the theta and then some. If the market goes dead, theta wins and you lose.

When does it earn its keep in India? Three regimes. First, **when you think India VIX is too cheap relative to what's coming** — a budget, an RBI policy, an election result, an earnings-heavy Bank Nifty week — and you want a non-directional way to be long that event. Second, **event-driven intraday** on Bank Nifty, which is the most gamma-rich instrument on the planet on expiry day: a 1.5–2% intraday range on an index that moves in 50-point strikes gives you enormous re-hedging opportunity. Third, as a **research/desk overlay** — you're long vol as a book stance and you scalp to reduce the carrying cost while you wait for the vol re-rating you forecast.

Be honest about the counter-party: the person on the other side is short gamma, collecting theta, and *most of the time they win* because most days realised vol undershoots implied. You are buying the tail. Gamma scalping done sloppily just converts a clean theta bleed into a theta bleed plus transaction costs. The edge is entirely in execution.

## The mechanics

Start with a **delta-neutral long-gamma position**. The cleanest is an at-the-money (ATM) long straddle: buy one ATM call and one ATM put, same strike, same expiry. At inception the call delta (~+0.5) and put delta (~−0.5) roughly cancel, so net delta ≈ 0. What you're left holding is **positive gamma, positive vega, negative theta**.

The Greeks that matter:

| Greek | Sign (long straddle) | What it does to you |
|---|---|---|
| Delta | ~0 at inception | Drifts away from zero as spot moves — this is what you hedge |
| Gamma | Positive (large near ATM, near expiry) | Rate at which delta changes; your scalp engine |
| Theta | Negative | Daily premium decay; your rent |
| Vega | Positive | Gains if IV rises, loses if IV falls |

The core relationship, and the only equation you truly need:

**Scalping P&L over a small move ≈ ½ × Γ × (ΔS)² − (θ decay for the period)**

That ½·Γ·(ΔS)² term is the curvature capture. Note the **square** on the move — it doesn't matter which way spot goes, up or down both make you money on gamma. Note also that it grows with the *square* of the move, so a handful of big swings beats many tiny ones for the same total distance travelled. Theta is the constant subtraction. Break-even for the day is when ½·Γ·(daily range effect) = theta. Rearranged, that's just the statement **realised vol = implied vol**.

**The re-hedge rule.** As spot moves, delta accumulates. You flatten it by trading the underlying — in India, the index future (or, for smaller size, a synthetic/mini). Suppose spot rises: your call gains delta faster than your put loses it, net delta goes positive, say +0.30 per straddle. You *sell* futures to bring net delta back to ~0. You've now sold high. If spot then falls back, delta goes negative, you *buy* futures — buying low. The round trip banks the difference. That, mechanically, is the scalp.

**When to re-hedge — two schools:**

1. **Fixed-band (delta trigger):** re-hedge whenever |net delta| crosses a band, e.g. ±25 or ±50 deltas per lot-cluster. Simple, disciplined, ignores time-of-day.
2. **Fixed-time / fixed-move:** re-hedge on a clock (every N minutes) or every fixed spot increment (every 50 Bank Nifty points). Easier to automate.

Tighter bands = more scalps, more capture of small oscillations, but more transaction cost and more chance of getting whipsawed by noise. Wider bands = fewer trades, lower cost, but you leave curvature on the table and carry more directional risk between hedges. There is no free lunch; band width is *the* tuning parameter and it should scale with how choppy vs. trending you expect the tape to be.

**Margin.** The long straddle itself requires **no SPAN margin** beyond the premium paid — you own the options outright, so you fund full premium up front. The hedging futures leg *does* consume SPAN + exposure margin. Under SEBI's portfolio (SPAN) framework the long options partially offset the future's risk in the same underlying, so the net margin on the hedge is smaller than a naked future, but budget for it: you must have futures margin available to run the hedge, and it can spike if you carry a large directional delta between re-hedges.

## Worked trade

**Instrument: Bank Nifty weekly straddle. Date-stamp the setup as a Tuesday, expiry Thursday (verify the current weekly-expiry day and the single-weekly-expiry rule — SEBI moved to fewer weekly expiries per exchange).**

- Bank Nifty spot/future ≈ **52,000**.
- Lot size: assume **15** (verify — lot sizes are revised periodically).
- ATM 52,000 CE premium ≈ **₹380**; 52,000 PE premium ≈ **₹360**. India VIX-equivalent implied ~ 14%.
- Buy 1 lot straddle: premium out = (380 + 360) × 15 = **₹11,100** per straddle. This is your max loss and your full funding.

**Greeks at inception (per lot, approx):**
- Net delta ≈ 0
- Gamma ≈ such that a 100-point move shifts net delta by ~+0.06 per share × 15 ≈ let's work in delta-units: a 100-pt move changes straddle delta by roughly +0.12 (call gains, put sheds) → +1.8 deltas/lot in share terms... I'll keep it practical below in rupee terms.
- Theta ≈ **−₹1,300/day** on the straddle (rent). Two days to expiry, so ~₹2,600 of decay to overcome — but theta accelerates into Thursday.
- Vega positive: a 1-vol-point rise in IV adds ~₹900.

**The session (expiry-week Tuesday, illustrative tape):**

| Time | BankNifty | Net delta (pre-hedge) | Action | Futures P&L on that leg |
|---|---|---|---|---|
| 09:20 | 52,000 | 0 | none (flat) | — |
| 10:05 | 52,300 | +0.35 (×15 ≈ +5.3 sh) | Sell hedge @ 52,300 | banked high |
| 11:10 | 51,950 | −0.28 | Buy back @ 51,950 → +350 pts on the sold hedge | +₹ from round trip |
| 12:40 | 52,250 | +0.30 | Sell @ 52,250 | banked high |
| 14:15 | 51,900 | −0.30 | Buy @ 51,900 → +350 pts | +₹ from round trip |
| 15:15 | 52,050 | +0.10 | Flatten into close | small |

Two clean round trips of ~350 points each on roughly ~5 share-equivalents of hedge delta ≈ **2 × 350 × 5 ≈ ₹3,500** of gross scalp capture (rough; exact figure depends on the delta you carried on each leg). Against that: theta for the day ≈ **−₹1,300**. Gross day P&L ≈ **+₹2,200 before costs.**

**Costs — and this is where India-2026 specifics bite.** Every hedge is a futures trade (buy + sell). Charges per futures round trip: brokerage (flat, say ₹20 each side on a discount broker), **exchange transaction charges**, **STT on the sell side of futures (~0.02% of turnover — verify)**, GST on brokerage+txn, stamp duty on buy side, SEBI turnover fee. On a 52,000 × 15 = ₹7.8 lakh notional futures leg, a round trip can cost **₹150–₹300** all-in. Four hedge legs across two round trips → ~₹500–₹700 of frictions on the day. Net day ≈ **+₹1,500 to +₹1,700.** The options exit STT (~0.15% of *premium* on sell — verify) hits when you finally close the straddle, not on each scalp.

The lesson is stark: **your scalp per round trip (₹1,750) must clear your cost per round trip (~₹300) with margin to spare.** On Bank Nifty with 300+ point swings it clears easily. On Nifty with 40-point wiggles, the same cost structure can eat the whole edge — which is why gamma scalping in India is overwhelmingly a **Bank Nifty (and Fin Nifty) expiry-day** game, not a large-cap-Nifty grind.

**Outcome at expiry.** If realised vol over the two days genuinely beats the ~14% implied you paid, the accumulated scalps + residual straddle value exceed the ₹11,100 premium and you're green. If the market went comatose Wednesday (no range, full theta), the Tuesday gains get given back and you're red. Realised > implied is the whole game.

## Management

**Re-hedging is the management.** But there are higher-order decisions.

**Choosing band width dynamically.** On a trending morning (gap-and-go), widen your bands — re-hedging too tightly on a trend means you keep selling into strength and buying into weakness on the *hedge*, which is correct for gamma but you sacrifice letting a big favourable ½Γ(ΔS)² term compound. On a range-bound chop, tighten bands to harvest the oscillation. Practically: if the 5-min range is expanding, hedge less often and let curvature build; if it's contracting into a range, hedge more often.

**Theta acceleration into expiry.** On expiry day the ATM straddle's theta is brutal — it can be several thousand rupees for the final session — but gamma is also at its maximum, so the required realised move to break even is very high *and* achievable. Expiry-day Bank Nifty gamma scalping is a specialist's game: enormous gamma, enormous theta, and pin risk into the close. Many desks flatten the straddle by ~2:30pm to avoid the terminal pin, keeping only the scalps banked.

**Scenarios:**
- **Big trend, one direction (IV flat):** you make money — the ½Γ(ΔS)² is large — but you'd have made *more* just holding the delta. Gamma scalping underperforms a naked directional bet in a clean trend. That's fine; you weren't betting direction.
- **Choppy range, IV flat:** ideal. Maximum scalps per unit theta.
- **Dead market, IV flat:** worst case. Theta wins, scalps don't cover it. Cut the straddle early; don't pay full rent for an empty room.
- **IV rises (event repricing):** bonus — your positive vega adds a windfall on top of scalps. This is why you *time entry before* a scheduled event: you want the vega tailwind and the realised-vol payoff.
- **IV collapses (post-event crush):** vega hurts. If you held a long straddle *through* a scheduled event expecting the move, the post-event IV crush can wipe the gain even if spot moved — the classic "the move happened and I still lost" trap. Gamma scalpers who buy *before* events must realise enough scalp+move to beat the crush.

**Rolling.** If your thesis (realised will beat implied) extends past this expiry, roll the straddle to the next weekly before theta peaks — sell the decaying near straddle, buy a fresh ATM. You're paying a fresh vega premium but resetting gamma without eating terminal decay.

## Risk & sizing

**Max loss** on the long straddle is capped and known: the premium, **₹11,100/lot** in the worked trade, if you never scalp and spot pins the strike at expiry. That's the beauty versus short gamma — your disaster is bounded. In practice good scalping recovers part of the premium even on a losing day.

**The real risks are execution and cost, not blow-up.** Slippage on the futures hedge in a fast tape; getting whipsawed (hedging at the extremes of noise, buying the top tick, selling the bottom); and the relentless drip of transaction costs turning a marginal edge negative. **Size the position so that a full day of theta plus a plausible cost drag is a small fraction of your risk budget** — because on dead days that's exactly what you'll pay.

**Portfolio Greeks.** Run the book's net gamma, theta, vega. A desk long gamma across several straddles is net long vega — you're implicitly short the vol carry. Cap aggregate vega so a single overnight IV crush (say India VIX drops 3 points after an event resolves benignly) can't exceed your daily loss limit. Long gamma is comforting because it self-corrects (you get flatter as you lose), but long vega is the tail: a vol crush hits your whole book at once, unhedged by any amount of delta scalping.

**Margin discipline.** Keep enough free margin to run the futures hedge through a spike. If you carry a large directional delta between re-hedges and the market gaps, your hedge future's SPAN can jump; being forced to un-hedge at the wrong moment (margin call) destroys the strategy.

**The tail.** For the long-gamma scalper the tail is *benign directionally* (bounded loss) but *malignant on cost and vol*: the death is a thousand cuts — dead markets plus frictions plus one bad IV crush. You will not blow up; you will bleed if you scalp a low-realised-vol tape. Respect that the counterparty (short gamma) usually wins, and only put this on when you have a genuine reason to think realised will beat implied.

## Pitfalls & interview-ready summary

**Pitfalls:**
- **Trading Nifty instead of Bank Nifty/Fin Nifty for scalps** — the wiggles are too small to clear costs. Match instrument to gamma-richness.
- **Over-hedging (bands too tight)** — you convert an edge into a commission-generation machine for your broker and the exchange. Every hedge must clear its round-trip cost.
- **Ignoring the IV crush** — buying a straddle into an event and being right on the move but wrong on vol. Separate the vega bet from the gamma bet in your head.
- **Holding into the expiry pin** — terminal gamma and pin risk near the strike can hand back a day's scalps. Flatten early if unsure.
- **Confusing gamma P&L with directional P&L** — in a clean trend you'll underperform a naked long; that's not a failure of scalping, it's the point (you were non-directional).
- **Forgetting margin for the hedge** — the straddle is paid-up, but the futures hedge eats SPAN and can spike.

**Interview-ready summary:** Gamma scalping monetises positive gamma by continuously re-hedging the drifting delta of a long-options position with the underlying, buying low and selling high in small slices. P&L per interval ≈ ½·Γ·(ΔS)² − θ; profitability reduces to **realised vol beating the implied vol you paid**. In India it's a Bank Nifty / Fin Nifty expiry-week play because only those instruments swing enough to clear the STT + brokerage + exchange-fee drag on each futures re-hedge. Max loss is bounded (the premium); the practical risks are transaction-cost bleed on dead tapes, whipsaw, and a post-event IV crush on your long vega. You are buying the tail the short-gamma crowd is selling — do it only when you have a real edge on realised vol, size for the dead-day bleed, and cap aggregate vega against a one-shot vol collapse.
