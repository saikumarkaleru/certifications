# Calendars & Diagonals: Construction & Management

*India F&O supplement — written July 2026. STT (~0.1% on option sells), SEBI expiry/lot-size framework and SPAN margining reflect 2026 as understood at time of writing. **Verify current expiry days, lot sizes and STT with NSE/SEBI/your broker before trading** — these have been revised repeatedly.*

## The idea

A calendar spread (a.k.a. time spread or horizontal spread) sells a near-dated option and buys a longer-dated option at the **same strike**. A diagonal does the same but at **different strikes**. Both are, at heart, a bet on **the term structure of volatility and on time decay differentials**: the option you sold decays faster than the option you bought, because theta is not linear in time — a weekly option loses value per day far quicker than a monthly option. You are long the calendar; you *own* the back month and *rent it out* month by month (or week by week) by selling the front.

Where the condor is a bet on *low realised movement*, the calendar is fundamentally a bet on **vega and the shape of the vol curve**, with a directional overlay you dial in via strike selection. A pure at-the-money calendar is **long vega, positive theta, and roughly delta-neutral** — a rare and elegant combination. It earns its keep when the index sits near your strike and, ideally, when back-month IV is cheap relative to where it might go (you *want* vol to rise, unlike the condor seller).

For an experienced Indian trader the calendar is the tool of choice in two situations. First, when **India VIX is low and you expect it to normalise up** but you don't want the unlimited risk of buying a naked straddle — the calendar is a cheaper, theta-positive way to be long vega. Second, as an **earnings/event play** on the back of a vol term-structure kink: sell the expensive event-week option, own a calmer post-event option. The diagonal extends this into a directional-plus-income structure — think of it as a "poor man's covered call" when built with a deep-ITM long call and a short OTM call, letting you replicate covered-call income without pledging ₹18+ lakh of Nifty index exposure.

The India-specific wrinkle that makes calendars *harder* here than in the US: **the weekly expiry ecosystem and the crush of front-week IV into expiry**. Nifty weeklies (Tuesday expiry as of 2026 — verify) see the front option's IV and time value collapse fast, which is exactly the theta you're harvesting, but it also means the front short can go ITM and get pin-risked on expiry day. And with Bank Nifty weeklies discontinued in the SEBI rationalisation, Bank Nifty calendars now span monthly expiries only — a different, slower animal.

## The mechanics

**Long calendar (call), same strike:**
- Sell 1 near-expiry call at strike K.
- Buy 1 far-expiry call at strike K.
- Net **debit** (the far option costs more than the near). That debit is your max loss.

Greeks at entry, ATM:

| Greek | Sign | Why |
|---|---|---|
| Delta | ~0 (ATM) | The two same-strike deltas roughly offset |
| Theta | Positive | Front decays faster than back |
| Vega | **Positive** | Back-month has more vega than front; net long vol |
| Gamma | Negative | Short the faster-gamma front option |

This is the signature profile: **positive theta AND positive vega simultaneously**, which the condor cannot offer. The cost is negative gamma (a big fast move hurts) and the fact that the position has a **profit tent centred on the strike** — you want price to finish *near* K at front expiry, so both a large up-move and a large down-move lose (the payoff diagram looks like a tent, similar in shape to a short straddle but with defined and much smaller risk).

**Diagonal:** same idea, but the long back-month is at a different strike. A **call diagonal** (buy lower-strike far call, sell higher-strike near call) leans bullish and behaves like a financed covered call. A **put diagonal** leans bearish. You trade some vega-neutrality for directional lean and, often, a wider or asymmetric tent.

**Poor Man's Covered Call (PMCC)** — the most practically useful diagonal in India: buy a deep-ITM long-dated call (delta ~0.80, acts as stock surrogate), sell a near-dated OTM call against it. You get covered-call-like income for a fraction of the capital of holding the underlying basket. On Nifty this is attractive precisely because holding one lot of "Nifty" outright means ₹18+ lakh notional; the LEAP-style long call proxies it for a much smaller debit.

**Margin.** A long calendar/diagonal is a **debit** structure — you pay for it, and because the long leg fully covers the short leg (same or protective strike, longer tenor), the margin is essentially the net debit plus a small exposure/short-option component, *far* less than a naked short. This capital efficiency is a core reason calendars appeal to smaller accounts.

**Strike & tenor selection.** For a neutral vega play: strike at-the-money, sell the nearest weekly, buy 3–5 weeks out (or the next monthly). For a directional diagonal: place the long strike per your bias and the short strike where you'd be happy to "cap out". The **width between the near expiry and far expiry drives vega and theta** — a wider gap (weekly vs monthly) gives more theta per unit time but also more sensitivity to term-structure shifts.

## Worked trade

**Setup: Nifty spot 24,600, India VIX ≈ 12 (low — we think it normalises up). Neutral-to-slightly-bullish. ATM call calendar.**

Nifty weekly expiry ~7 days out; next monthly ~35 days out.

| Leg | Strike | Expiry | Action | IV | Premium (₹) |
|---|---|---|---|---|---|
| Short call | 24,600 CE | Weekly (7d) | Sell | 12.5% | 118 |
| Long call | 24,600 CE | Monthly (35d) | Buy | 13.0% | 268 |

**Net debit** = 268 − 118 = **₹150 per share** → **₹11,250 per lot** (×75). That debit is your **maximum loss** (realised only if the position is closed worthless, e.g. after a huge move away from strike — practically you'll lose less because the long retains value).

Greeks at entry (approx, per share): delta ≈ +0.03 (near-neutral, slight positive as ATM calendars carry a touch of positive delta), **vega ≈ +6** (long vol — a 1-point IV rise adds ~₹6/share ≈ ₹450/lot), **theta ≈ +9/day** early, rising sharply in the front option's final days, **gamma negative**.

**The profit engine, in numbers.** Over the next 7 days, if Nifty sits near 24,600:
- The front 24,600 CE decays from ₹118 toward its intrinsic (₹0 if it expires ATM/just OTM) — you capture ~₹100+ of that.
- The back 24,600 CE also decays, but slowly — maybe ₹268 → ₹240 over the same week (it still has 28 days left).
- Net: you pocket roughly (₹118 collected − ₹0 to buy back) − (₹268 − ₹240 back-month decay) ≈ **+₹90/share ≈ +₹6,750/lot** if price pins the strike and IV is unchanged. That's a ~60% return on the ₹150 debit in a week — the calendar's appeal.

**Now layer the vega.** If our thesis is right and VIX rises from 12 to 15 during the week, the back-month (higher vega) gains more than the front, adding perhaps ₹40–60/share on top. If instead VIX *falls* to 10, that vega works against us and can wipe out much of the theta gain even with price pinned — **the calendar's Achilles' heel is a vol crush.**

**Costs (India).** 4 orders in/out (or fewer if you let the front expire worthless — but mind pin/STT risk). Round-trip frictions ~₹250–400/lot. STT on the sold front option (~0.1% of ₹118 premium — small); the real STT trap is letting the front expire **ITM** and being settled — square it off. Net of costs, a pinned outcome still nets comfortably positive here; a vol-crush or big-move outcome can turn the ₹150 debit into a ₹60–90 loss.

## Management

The calendar is *not* a set-and-forget trade — the front leg expires while the back leg lives on, so it demands a decision at least at every front expiry.

**1. The roll (the entire point of a calendar campaign).** At front expiry, if price is still near strike and the back-month remains healthy, **buy back (or let expire) the front short and sell the next front** — the next weekly. This "re-rents" your back-month long and collects a fresh credit, lowering your net cost basis. A calendar held as a *campaign* can, over 3–4 front expiries, reduce the effective cost of the long option to near zero or below — at which point you own a free long-vol/long-directional option. This rolling is where diagonals shine as income machines (the PMCC is literally "sell a fresh call every week against my LEAP").

**2. Re-centre when price drifts.** The tent is centred on K. If Nifty drifts from 24,600 to 24,850, your calendar's peak is now below spot — theta capture weakens and delta turns. Adjust by **rolling the short leg up** to a higher strike (e.g. sell 24,800 CE next week instead of 24,600), converting the calendar into a diagonal that re-centres the tent toward price and re-neutralises delta. If the move is large and you're convinced of a new regime, roll the *whole* calendar (both legs) to a new strike.

**3. Directional conversion.** A calendar that goes your way can be actively steered. If bullish and price rises, keep rolling the short strike up and out — you gradually walk the structure into a bullish diagonal, banking credits along the way while the long call appreciates.

**Scenario grid:**

| Scenario | Effect on calendar | Action |
|---|---|---|
| **Price pins strike, IV flat/up** | Ideal. Theta + vega both help | Let front decay; roll to next week; consider taking profit at 25–40% of debit |
| **Price pins strike, IV crushes** (12→10) | Theta gain partly/fully offset by vega loss | Hold if terminal thesis intact, but recognise vol crush is the main risk; don't add |
| **Slow drift away (24,600→24,900)** | Tent off-centre, delta turns, theta weakens | Roll short leg up (→ diagonal) to re-centre delta |
| **Sharp move either way** | Negative gamma bites; calendar loses value fast | Long leg cushions loss (defined risk); consider closing and re-establishing a new ATM calendar |
| **Front expiry day, price near strike** | Pin risk on the short front | Actively manage — don't let an ITM front settle; buy it back and roll |
| **Vol term structure inverts** (front IV >> back, e.g. pre-event) | Actually *favourable* to open a calendar here — you sell rich front vol | Best entry timing; harvest the event vol crush |

**IV up vs down is decisive.** Unlike the condor, the calendar *wants* IV up (long vega) but *needs* the front to decay faster than the back. The dangerous combination is a **broad vol crush** — front and back both collapse, and since the back has more vega, you lose net. So the best calendars are opened when **front-month IV is elevated relative to back-month** (a kinked/inverted term structure, common right before a scheduled event) — you sell the temporarily rich front, own the calmer back, and profit as the term structure normalises post-event.

## Risk & sizing

**Max loss = net debit paid.** For our trade, ₹11,250/lot — known, capped, financeable. This is the calendar's great virtue: unlike the strangle, there is no tail beyond your debit (the long leg always outlives and covers the short leg). Size so total debit-at-risk across calendars is a modest fraction of capital; because the realised loss is usually much less than the full debit (the long retains value), calendars are *capital-gentle*.

**The real risks are subtler than max loss:**
- **Vega/term-structure risk.** Your P&L is genuinely a bet on the vol curve. A parallel vol crush hurts; a steepening where the back falls more than the front hurts. Know your net vega in ₹ per VIX point.
- **Pin/assignment risk on the front (expiry day).** In India index options are cash-settled (no physical delivery), which removes the US-style assignment nightmare — but you still face **expiry-day settlement of an ITM front** and its STT, and the front's savage terminal gamma. Manage the front out before it settles ITM.
- **Negative gamma on a fast move.** A gap through your strike loses money quickly *before* the long leg's convexity catches up; defined, but real.
- **Liquidity of the back month.** Monthly and especially further-dated Nifty options are thinner than the front weekly — wider spreads cost you on entry, roll and exit. Bank Nifty back-months are thinner still. Budget for slippage; don't build calendars in illiquid far strikes.

**Portfolio Greeks.** A book of long calendars is **net long vega** — the opposite of a condor book. This makes calendars a natural hedge/diversifier against a short-premium book: when a vol spike smashes your condors, your calendars gain. Consciously running some of each can flatten your aggregate vega and smooth equity. Watch aggregate gamma (still negative from the short fronts) and keep net delta in a chosen band via the strike of the short leg.

**The tail — honest version.** The calendar has no catastrophic tail on price (loss capped at debit), but it has a **slow-bleed tail on vol**: an extended low-vol grind (VIX pinned at 10–11 for weeks) means every calendar you open pays too much for vega that never appears, and theta alone may not cover the debit if price also wanders. Most calendar losses are unspectacular — a series of small debits that didn't work because vol never rose and price never pinned. Boring losses, but they add up if you force calendars in a dead-vol regime.

## Pitfalls & interview-ready summary

**Pitfalls:**
- **Opening calendars in a vol crush / expecting price to pin AND vol to hold.** If you're wrong on vol direction, theta alone may not save you. Open when front IV is rich vs back (pre-event term-structure kink).
- **Letting the front expire ITM.** Settlement + STT surprise, plus terminal gamma. Roll it out.
- **Ignoring back-month liquidity.** Wide spreads on the far leg quietly eat the edge on every roll.
- **Treating it as delta-neutral forever.** The tent goes off-centre as price drifts; re-centre by rolling the short strike (calendar → diagonal).
- **Confusing it with a condor.** A calendar is *long* vega — it *wants* vol to rise; a condor is short vega. Opposite trades.
- **Over-rolling a losing directional diagonal.** Rolling the short strike endlessly to chase a runaway trend can leave you with a busted long leg and negative net credit.
- **PMCC assignment/cap misjudgement** — capping your long call's upside too tightly with an aggressive short strike.

**Interview-ready summary:** *A calendar sells a near-dated option and buys a longer-dated one at the same strike; a diagonal does so at different strikes. The core bet is on the vol term structure and differential time decay: it's long vega, positive theta, negative gamma, roughly delta-neutral at the strike — the rare structure that's long vol AND collects theta. You pay a net debit (your capped max loss), profit most when price pins the strike and IV rises or the front decays faster than the back, and you run it as a campaign — rolling a fresh front short each week/month to re-rent the back-month long and grind the cost basis toward zero. Best entered when front-month IV is rich relative to back (pre-event kinks). Its enemies are a parallel vol crush and a fast gap through the strike; its friends are capital efficiency, defined risk, and being a natural vega hedge to a short-premium book. In India, mind cash-settled expiry-day pin risk on the front, STT on ITM settlement, and thin back-month liquidity — and remember Bank Nifty is monthly-only now, making its calendars slower and coarser than Nifty's weekly-driven ones.*
