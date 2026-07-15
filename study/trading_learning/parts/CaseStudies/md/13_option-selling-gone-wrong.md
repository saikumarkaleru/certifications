# Case Study: Option Selling Gone Wrong (Gap & Tail Risk)

*The levels and P&L below are approximate reconstructions of real gap events; pull up the actual charts to verify the exact prints — the transferable lesson is the arithmetic of tail risk, not the precise ticks.*

Option selling has a seductive equity curve. You collect small premiums, the market sits still most days, and month after month the account ticks up. It feels like income. What that smooth curve hides is the shape of the risk: you are picking up nickels with unlimited (or near-unlimited) downside, and the whole game is whether a single gap arrives before you've built a buffer. When the gap comes — an election result, a pandemic shock, an overnight geopolitical event — it does not respect your stop-loss, because the market is *closed* when the damage happens. You wake up already through your stop. The two cases below walk that arithmetic honestly.

## Case A — The overnight election gap (naked short strangle)

**The setup.** The evening before a major national election result — a genuinely binary, market-moving event. Nifty around 24,000, having drifted up on exit-poll optimism. A seller ran a "safe" naked short strangle for the weekly: sold the 24,500 CE at ~₹90 and the 23,500 PE at ~₹85 — strikes a full 500 points out either way, a band that "never" broke in normal weeks. Credit = (90 + 85) × 75 = ₹13,125 per lot; the trader, emboldened by months of clean income, ran **5 lots**: credit ₹65,625. Margin blocked ≈ ₹9–10 lakh. Mental stop: "cover if either strike is threatened."

The flaw in that stop is that the event happens overnight. There is no intraday to react to.

**Walkthrough.**

| Moment | Nifty | 24,500 CE | 23,500 PE | Note |
|--------|-------|-----------|-----------|------|
| Prev close | 24,000 | ~90 | ~85 | Strangle looks bulletproof |
| Result shock (gap down) | 21,900 | ~5 | ~2,150 | Counting shock — market gaps ~9% down at open |
| First tradable print | 21,900 | — | ~2,150 | Put is now ₹2,150 vs ₹85 collected |

**What happened.** The result defied the exit polls; Nifty gapped roughly 2,100 points *below* the previous close, straight through the 23,500 put. The put the seller wrote for ₹85 opened around ₹2,150. There was no chance to honour the stop — the "cover if threatened" plan assumed a market you could react in; instead the strike was breached by 1,600 points before the first trade.

Loss on the put leg alone: (2,150 − 85) × 75 × 5 lots = **₹7.74 lakh**. The call leg expired worthless, returning the ₹90 credit: +90 × 75 × 5 = ₹33,750. Net loss ≈ ₹7.4 lakh — and because the loss blew past the blocked margin, the broker issued a margin call and force-squared the position near the lows, locking in the worst print. Months of ₹40–60k monthly income — call it a year of theta — were erased in a single overnight gap, plus the account went into deficit.

**The lesson.** The naked seller was not paid enough for the tail. ₹85 of premium against a strike that could be — and was — breached by ₹1,600 is not "500 points of safety"; it is a short position on a catastrophe with no floor. The market maker on the other side knew the event was binary and priced the *average* week fairly while quietly holding the fat tail. The retail seller mistook the quiet months for low risk and, worse, sized *up* into the one week when the tail was most likely. The stop was a fiction because the risk was overnight.

## Case B — The COVID limit-move week (lightly-hedged short puts)

**The setup.** Late in a fast-crashing market (a COVID-style waterfall), Nifty around 9,500 and already down hard. A seller reasoned "it's oversold, puts are rich" and sold the 9,000 PE at a fat ~₹300 — IV was enormous, so the premium looked like a gift. To feel responsible, they bought a token far hedge, the 8,000 PE at ~₹120, netting ₹180 credit — technically a spread, but a *wide, lightly-hedged* one. Credit = 180 × 75 × 3 lots = ₹40,500. Max defined loss on paper = (9,000 − 8,000 − 180) × 75 × 3 = ₹1.845 lakh.

**Walkthrough.**

| Moment | Nifty | 9,000 PE | 8,000 PE | Note |
|--------|-------|----------|----------|------|
| Entry | 9,500 | ~300 | ~120 | "Oversold, sell rich puts" |
| Next day (lower circuit) | 8,600 | ~750 | ~340 | Market hits lower circuit, halts |
| Following day | 8,050 | ~1,150 | ~600 | Gap continues, IV exploding |
| Exit | 8,100 | ~1,100 | ~560 | Both legs deep, spread near max loss |

**What happened.** The waterfall continued; the market even hit a lower circuit and *halted*, meaning the seller could not exit at all for a session — the ultimate "no liquidity when you need it." When trading resumed, the short 9,000 PE was ~₹1,100 and the long 8,000 PE ~₹560. The spread had blown out to nearly its full defined loss. Exit: short leg loss (1,100 − 300) = 800; long leg gain (560 − 120) = 440; net loss per share ≈ 360 points. Loss = 360 × 75 × 3 = **₹81,000**, on the way to the ₹1.845 lakh max. The "responsible" hedge is what saved the account from a Case-A-style wipeout — the 8,000 PE capped the disaster at a known, survivable number even through a circuit halt.

**The lesson.** Case B lost money too — but it lost a *defined, survivable* amount because the position had a floor. The hedge felt like a waste of premium in every quiet week; it justified its entire existence in the one week that mattered. And note the second tail nobody prices in: **liquidity vanishes exactly when you need to exit** — lower circuits, halted trading, blown-out bid-ask spreads. A defined-risk structure protects you even when you *cannot* trade; a naked position does not.

## The arithmetic that matters

Case A collected ₹65,625 that week and lost ₹7.4 lakh — a single event undid a year of income and then some, with no floor. Case B collected ₹40,500 and lost ₹81,000 — painful, but bounded, survivable, and back-in-the-game next month. Same instinct (sell rich premium into fear); opposite outcomes, decided entirely by whether the tail was defined and the size was sane.

## Transferable rules

- **Never sell naked options** — always own a wing so your worst case is a known, survivable number *before* you enter, not a discovery you make at the next open.
- **Your stop-loss is a fiction against overnight gaps** — for event/binary risk the only real risk control is the strike you *bought* and the size you chose, because the damage happens while the market is closed.
- **Size for the gap, not the average week** — months of smooth theta income tempt you to size up exactly when a fat-tail event is most likely; do the opposite and trim into known events.
- **Liquidity disappears when you need it most** — circuits, halts, and blown-out spreads mean you may be unable to exit at all, so the protection must be structural (a bought wing), not reactive.
- **A defined-risk loss keeps you in the game; a naked loss ends it** — the hedge that feels like wasted premium every quiet week is the reason you survive the one week that counts.
