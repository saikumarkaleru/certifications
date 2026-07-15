# Case Study: Straddles/Strangles That Worked and Didn't

*The premiums and levels below are approximate reconstructions of real Bank Nifty sessions; pull up the actual option chain to verify the ticks — the transferable value is the payoff logic of a straddle, not the exact numbers.*

A straddle — buy (or sell) the at-the-money call and put on the same strike — is the purest non-directional bet in the book. A **long** straddle wins if the underlying MOVES enough, in either direction, to cover both premiums. A **short** straddle wins if the underlying SITS STILL and time/vol decay both legs. You are never betting on up or down; you are betting on *move versus stillness*. The four vignettes below — two long, two short — show the same instrument, Bank Nifty, paying and punishing the exact same structure depending on whether the move showed up.

Bank Nifty weekly, lot size 30 throughout.

## Long straddle that WORKED — the move arrived (a policy/event breakout)

**The setup.** Bank Nifty coiled around 47,000 for three sessions ahead of a monetary-policy decision the Street saw as genuinely two-sided. Tight range, but an event known to move banks. A trader bought the 47,000 straddle: 47,000 CE at ~₹210 and 47,000 PE at ~₹200. Total debit = 410 points. Break-evens: 47,410 up / 46,590 down. Cost = 410 × 30 = ₹12,300 per lot, 1 lot.

**Walkthrough.**

| Moment | Bank Nifty | 47,000 CE | 47,000 PE | Straddle value |
|--------|-----------|-----------|-----------|-----------------|
| Pre-event | 47,000 | ~210 | ~200 | 410 (entry) |
| Decision +10 min | 47,180 | ~300 | ~110 | 410 (flat, IV still up) |
| +40 min (trend) | 47,650 | ~680 | ~35 | 715 |
| Exit | 47,720 | ~740 | ~25 | 765 |

**What happened.** The policy surprised hawkish; banks ran ~720 points. The trader exited the whole straddle at ~765. Profit = (765 − 410) × 30 = ₹10,650 gross, ~₹10,200 after costs — an ~0.85R... actually a healthy return on the ₹12,300 risk. Note the call did all the work; the put decayed toward zero, exactly as designed — the losing leg's max loss is capped at its premium.

**The lesson.** A long straddle pays when the *realised* move exceeds the *sum of premiums*. Here the 720-point move dwarfed the 410 paid. The professional bought the straddle when IV was still reasonable relative to the expected move and, crucially, took profit *on the move* rather than holding for "more."

## Long straddle that BLED — no move, IV crush (the range that refused to break)

**The setup.** Another week, Bank Nifty near 48,000, a lesser data event. A trader bought the 48,000 straddle at 190 + 185 = 375 debit, expecting fireworks.

**Walkthrough.**

| Moment | Bank Nifty | Straddle value |
|--------|-----------|-----------------|
| Entry | 48,000 | 375 |
| Post-event | 48,060 | 300 (IV crushed) |
| Next day | 47,950 | 210 |
| Exit (2 days) | 48,020 | 165 |

**What happened.** The event was a non-event; Bank Nifty chopped in a 150-point box. IV collapsed and theta ground both legs down. Exit at 165: loss = (375 − 165) × 30 = ₹6,300 + costs. The trader was neither right nor wrong on direction — there was no direction — and that is precisely how a long straddle dies. **The lesson:** a long straddle is a *long-volatility* position; buy it when you expect realised movement to beat the priced-in movement, not merely "because something is scheduled."

## Short straddle that COLLECTED — stillness paid (a quiet post-event drift)

**The setup.** The morning after a big event, IV still elevated but the catalyst spent. Bank Nifty near 46,500, likely to drift. A seller sold the 46,500 straddle: CE ~₹180 + PE ~₹175 = 355 credit. Break-evens 46,145 / 46,855. Credit = 355 × 30 = ₹10,650 per lot. Stop: cover if Bank Nifty breaks either break-even decisively.

**Walkthrough.**

| Moment | Bank Nifty | Straddle value |
|--------|-----------|-----------------|
| Entry (morning) | 46,500 | 355 |
| Midday | 46,540 | 250 (IV + theta bleeding) |
| Afternoon | 46,480 | 170 |
| Exit | 46,510 | 150 |

**What happened.** Bank Nifty spent the day in a 120-point range. The seller bought back at 150: profit = (355 − 150) × 30 = ₹6,150 gross, ~₹5,900 net, on ~₹1.6 lakh margin. Post-event IV crush + theta did the work. **The lesson:** short straddles harvest stillness and falling vol — the ideal habitat is *after* the catalyst, when premium is still fat but the reason to move is gone.

## Short straddle that GOT RUN OVER — a trend day (the tail)

**The setup.** Same structure, wrong day. Bank Nifty near 49,000, seller sold the 49,000 straddle for 170 + 165 = 335 credit, break-evens 48,665 / 49,335 — a comfortable-looking band. Then a global risk-off session turned it into a one-way trend day.

**Walkthrough.**

| Moment | Bank Nifty | 49,000 CE | 49,000 PE | Straddle value |
|--------|-----------|-----------|-----------|-----------------|
| Entry | 49,000 | ~170 | ~165 | 335 |
| 11:30 (breaking down) | 48,650 | ~55 | ~360 | 415 — through break-even |
| Stop hit | 48,600 | ~48 | ~400 | 448 |
| If held to close | 48,250 | ~25 | ~720 | 745 |

**What happened.** The put leg exploded as Bank Nifty trended down all day. A disciplined seller covered at the lower break-even (~448): loss = (448 − 335) × 30 = ₹3,390 — a controlled ~0.3x of margin. The seller who *hoped* it would revert held to the close (745): loss = (745 − 335) × 30 = ₹12,300, wiping out roughly two clean weeks of straddle income in one trend day. **The lesson:** a short straddle is short-volatility with *unlimited* risk on one side; a trend day is its natural predator, and only a mechanical stop (or a protective wing turning it into an iron fly) keeps the tail survivable.

## Transferable rules

- **A straddle is a bet on MOVE vs TIME/VOL, never on direction** — decide first whether you expect the underlying to travel or to sit, then pick long or short accordingly.
- **Long straddles need the realised move to beat the sum of premiums** — buy them when volatility is underpriced relative to a genuine catalyst, and take profit on the move, not on hope.
- **Short straddles harvest stillness and IV crush** — their best habitat is *after* a spent catalyst, but they carry a fat, effectively unlimited tail.
- **Every short straddle needs a mechanical exit at the break-even** — or convert it to a defined-risk iron fly with wings; a trend day will otherwise hand back weeks of income.
- **The same structure on the same instrument wins or loses purely on whether the move showed up** — respect that you are trading volatility, and size for the day you're wrong about it.
