# Trading Volatility: The Long-Vol / Short-Vol Playbook

*India F&O desk note — drafted July 2026. STT, SPAN, expiry-structure and lot sizes reflect 2026 as I understand them; verify every number on NSE/SEBI/your broker before trading.*

## The idea

Every option position is, underneath the direction, a **bet on volatility**. You are either **long vol** (you own optionality — you profit if the world becomes more uncertain, if IV rises or realised movement is large) or **short vol** (you sold optionality — you profit from calm, from IV falling and realised movement staying small). The single most useful reframe for an experienced trader is to stop thinking "am I bullish or bearish" and start thinking "am I long or short vol, and is vol cheap or dear right now."

The reason vol is *tradeable* is that **implied volatility and realised volatility are different numbers that persistently disagree**, and the gap is a risk premium. Implied vol — what India VIX and option prices quote — is, on average, *higher* than the volatility the market subsequently realises. Option sellers collect this **variance risk premium** as compensation for insuring buyers against tail moves. That's why, structurally and over long samples, **short vol makes money most of the time** — and why it periodically hands back years of gains in a single crash. Long vol is the mirror: it bleeds most of the time and pays off violently in the tail.

The playbook, then, is not "always short vol" (the naive premium-harvester's grave) nor "always long vol" (the perpetual bleeder). It's: **form a view on whether current implied vol is rich or cheap relative to what realised vol will be, express it with the cleanest instrument, and size for the tail on whichever side you're on.**

When does each earn its keep in India?

**Short vol earns its keep** when India VIX is *elevated relative to what's justified* — post-event, when fear is priced but the event resolved; in grinding low-realised-vol regimes where the index chops in a range; when the term structure is steep and you're paid to be short the front. The Indian retail options ecosystem is *enormous* and structurally long lottery-ticket OTM options, which keeps OTM implied vols (and skew) fat — a persistent tailwind for disciplined sellers.

**Long vol earns its keep** when VIX is *complacently cheap* ahead of a known catalyst — Union Budget (Feb 1), RBI MPC, election counting day, a Fed meeting that spills into Indian markets, a geopolitical flashpoint; or when you forecast a regime shift from calm to turbulent that the market hasn't priced. Long vol is also the correct *hedge overlay* for a book that's implicitly short vol everywhere else.

Be brutally honest: **most retail F&O participants lose money** (SEBI's own studies show the vast majority of individual F&O traders are net losers), and a large share of that loss is *short-vol blow-ups* — selling naked options, collecting small premiums for months, then getting detonated by one gap. If you are short vol, you are selling insurance; price it, hedge the tail, and never confuse "hasn't blown up yet" with "won't."

## The mechanics

**Measuring the edge.** The trade is *implied vs realised*. Pull India VIX (30-day implied on Nifty) and compare it to trailing realised vol (e.g. 10- or 20-day close-to-close, annualised). The spread (IV − RV) is the variance risk premium on offer. Positive and wide → sellers are well paid → lean short vol. Compressed or negative (realised already exceeds implied, VIX complacent) → lean long vol.

**The instruments, mapped to vol exposure:**

| Structure | Vol stance | Vega | Theta | Gamma | Max loss |
|---|---|---|---|---|---|
| Long straddle/strangle | Long | + | − | + | Premium (bounded) |
| Short straddle/strangle | Short | − | + | − | **Unbounded** (naked) |
| Iron condor / iron fly | Short (defined) | − | + | − | Capped (width − credit) |
| Calendar spread | Long vega, structure-dependent | + | mixed | − near | Net debit |
| Long options + delta hedge | Long realised vol (gamma scalp) | + | − | + | Premium |
| Ratio spreads | Mixed | varies | varies | varies | Can be unbounded |

**Vega is the master Greek for the vol trade.** It measures P&L per 1-vol-point move in IV. A long straddle is long vega — it gains if India VIX rises even if spot is still. A short strangle is short vega — it gains if VIX falls. **Theta and vega trade off:** short-vol positions are long theta (paid to wait) and short vega (hurt if vol jumps); long-vol positions pay theta and own vega.

**The critical distinction — implied-vol trades vs realised-vol trades.** If you buy a straddle and *hold it*, you're betting on IV *rising* (a vega bet) and/or a large move (a gamma/realised bet). If you buy a straddle and *delta-hedge it*, you've stripped the direction and you're purely betting realised > implied (see the gamma-scalping chapter). Symmetrically, a *naked short strangle* held is short both vega and realised; a *delta-hedged short* is a pure "realised will stay below implied" bet.

**Margin — the asymmetry that defines the trade.** Long-vol structures (long straddle/strangle) cost **premium only, no SPAN** — bounded and fully funded up front. Short-vol structures consume **SPAN + exposure margin**, and for naked shorts that margin is large and *scales with vol* — when VIX spikes, SPAN inflates precisely when your position is losing, a double-squeeze that forces liquidation at the worst moment. **Defined-risk short structures (iron condor/iron fly)** consume far less margin (roughly the spread width less credit) because the long wings cap the risk — this is why disciplined retail short-vol is almost always *defined-risk*, not naked.

## Worked trade

**Two mirror trades on Nifty around a known catalyst — RBI MPC week. Date-stamp: illustrative; verify VIX, lot size (assume Nifty lot = 75 — verify), premiums, STT.**

Setup: Nifty ≈ **24,000**. India VIX = **11.5** (historically low — market is complacent into the policy). Trailing 10-day realised ≈ 9%. You judge VIX *too cheap into a live event*.

### Trade A — Long vol (you think VIX is too low)

Buy the ATM weekly straddle:
- 24,000 CE ≈ **₹150**, 24,000 PE ≈ **₹140**. Total premium = (150+140) × 75 = **₹21,750**. This is max loss and full funding. No SPAN.
- Net delta ≈ 0, **long vega ≈ +₹1,600 per vol point**, theta ≈ **−₹2,500/day**.

**Outcome 1 — VIX pops to 15 on policy-day nerves, spot moves 250 pts:** vega gain ≈ (15−11.5) × 1,600 ≈ **+₹5,600**; plus intrinsic from the 250-pt move on the winning leg ≈ (250−~193 breakeven contribution) — net the straddle now worth well above ₹290. Say straddle marks **₹430** → value 430×75 = ₹32,250, gross P&L ≈ **+₹10,500** before the ~₹2,500 theta already embedded. **Green.**

**Outcome 2 — policy is a non-event, VIX crushes to 9, spot flat:** vega loss ≈ (11.5−9)×1,600 ≈ −₹4,000, plus theta bleed. Straddle marks maybe ₹190 → value ₹14,250 → **−₹7,500. Red.** This is the long-vol reality: you're right that it *could* move, but if it doesn't, IV crush + theta punish you. Bounded at ₹21,750 though.

### Trade B — Short vol (you think VIX is fair/rich and calm will hold)

Sell a **defined-risk iron condor** (never naked):
- Sell 24,300 CE ₹60 / Buy 24,500 CE ₹25 → call credit ₹35
- Sell 23,700 PE ₹55 / Buy 23,500 PE ₹22 → put credit ₹33
- Net credit = (35+33) × 75 = **₹5,100**. Max loss = (200 width − 68 credit) × 75 = **₹9,900**. SPAN margin ≈ the ₹9,900-ish risk (far less than a naked strangle).
- **Short vega ≈ −₹900/pt**, long theta ≈ **+₹1,400/day**, short gamma.

**Outcome 1 — calm holds, Nifty inside 23,700–24,300 at expiry:** all four legs expire worthless-ish, you keep most of the ₹5,100 credit. **+~₹4,500 after costs.** Long theta paid you to wait; short vega gained as VIX drifted down.

**Outcome 2 — the event surprises, Nifty gaps to 24,450, VIX to 16:** short vega and short gamma both hurt; loss approaches the capped max ≈ **−₹9,900.** Painful but *known and bounded* — the long wings did their job. A naked short strangle here could have lost multiples of the credit with SPAN exploding simultaneously.

**Costs note (both trades):** options **STT ≈ 0.15% of premium on the sell leg (verify 2026 rate)** — on short structures you're selling to open, so STT and exchange charges apply on the opening sells and any buy-to-close; brokerage is typically flat per leg. The iron condor's four legs mean four sets of charges — factor ~₹200–₹400 all-in into the credit. On the long straddle, the STT hits when you sell to close.

## Management

**Long vol (Trade A):**
- *Move for you (spot runs, IV up):* consider **taking profit into the IV spike** — vol-crush risk grows the longer you hold post-event. Or convert to a gamma-scalp: delta-hedge and harvest the realised move rather than betting on further IV rise.
- *Against you (calm, IV bleeding):* cut early. Don't pay full theta hoping. If a catalyst is still ahead, roll to the next expiry to reset gamma/vega before terminal decay.
- *IV crush is the enemy:* the classic trap is holding a long straddle *through* the event and watching IV collapse the instant uncertainty resolves — you were right it'd be volatile *before*, but the crush eats you. Exit into, not after, the vol peak where possible.

**Short vol (Trade B):**
- *For you (calm, IV falling, theta accruing):* let it decay, but **take profit at ~50% of max credit** rather than squeezing the last rupee — the risk/reward turns ugly near expiry (all gamma risk, little premium left). This is the professional's discipline.
- *Against you (spot approaching a short strike):* **roll the tested side** — buy back the threatened short spread, re-sell further out, or roll out in time for a credit. Or delta-hedge with futures to neutralise the accumulating short delta. Or simply take the defined loss — the wings cap it.
- *IV spike:* short vega bleeds on mark-to-market even before expiry; SPAN inflates. Have margin buffer so a VIX pop doesn't force liquidation.

**The meta-management rule:** long vol you tend to *take profits quickly and cut losses slowly-ish* (bounded anyway); short vol you *take profits at 50% and cut/roll losses decisively* (because the tail is what kills you).

## Risk & sizing

**Long vol** — max loss is the premium, bounded and known. Size so that a full IV-crush-plus-theta loss on a dead event is an acceptable, repeatable cost — because you'll pay it often. The edge is that a few big wins (real vol events) dwarf the many small bleeds. Cap aggregate long vega so a portfolio-wide IV collapse (VIX −3 across the board) is survivable.

**Short vol** — this is where sizing is life-or-death. **Never naked.** Even defined-risk, size so the *simultaneous* worst case across all short positions — a gap that tests every short strike *while SPAN margin inflates* — fits inside your risk budget with room. The killer is correlation: in a crash *all* your short-vol positions lose *together*, IV spikes on *all* of them, and margin balloons on *all* of them at once. Model the "everything gaps 4%, VIX doubles" day and make sure it's a drawdown, not a blow-up.

**Portfolio Greeks — run daily:** net vega (are you a vol buyer or seller overall?), net gamma (self-correcting or self-destructing?), net theta (paid or paying to wait?). A book that's net short vega and short gamma is *the retail F&O death trap* — collecting theta happily until the one day it isn't. Keep net short vega capped against a defined VIX-spike scenario.

**The tail, both sides:**
- Long vol tail is *benign* (bounded loss, occasional windfall) — you bleed the premium repeatedly, which is a P&L problem, not a solvency one.
- Short vol tail is *malignant* (potentially unbounded if naked; capped-but-simultaneous if defined) — the variance risk premium is real, but it's *compensation for a genuine tail risk that eventually shows up*. The graveyard of Indian F&O is full of consistent short-vol sellers who were "profitable" for eighteen months.

## Pitfalls & interview-ready summary

**Pitfalls:**
- **Selling naked options for the premium** — the number-one retail killer. SPAN inflates as you lose; one gap ends the account. Always define risk.
- **Confusing an IV bet with a realised bet** — holding a straddle expecting a move but getting crushed on IV, or hedging a position you meant to leave directional. Know which vol you're trading.
- **Ignoring the variance risk premium's direction** — shorting vol when it's already cheap (no premium to harvest, all tail), or buying vol when it's already rich into a resolved event.
- **The IV-crush trap** — long options through an event, right on the move, still lose because IV collapses. Exit into the peak.
- **Squeezing short-vol to expiry** — the last 20% of premium carries most of the gamma risk. Take 50% and redeploy.
- **Not modelling the correlated crash** — sizing each short position independently, forgetting they all detonate together.

**Interview-ready summary:** Every option position is a long- or short-vol bet. Implied vol structurally exceeds realised (the variance risk premium), so short vol wins most of the time and blows up in the tail; long vol bleeds most of the time and pays in the tail. The trade is a view on *implied vs realised* — go long vol (straddle/strangle, bounded premium, long vega) when VIX is complacent into a catalyst; go short vol (**always defined-risk** iron condor/fly, capped loss, long theta/short vega) when the variance premium is fat and calm is likely. In India the huge retail long-OTM flow keeps skew and OTM IV rich, favouring disciplined sellers — but SEBI data shows most F&O retail loses, largely to naked short-vol detonations and IV-crush traps. Manage by taking long-vol profits into the vol peak and short-vol profits at ~50% of credit, roll the tested side, and size short vol for the correlated-crash day when everything gaps and SPAN inflates at once.
