# Q&A — Risks of Derivatives and Lessons

Practice bank for Chapter 18. Every question is followed by a full worked answer. Attempt each one before reading the solution. This chapter is largely conceptual and historical, so the numerical section (B) stresses the two engines that recur in every disaster — notional-to-margin leverage and the netting/collateral arithmetic. Where a scenario echoes a real blow-up, the mechanism, not the headline, is what matters.

---

## Section A — Concept Check

**A1. In one sentence, what do derivatives do to risk, and why does that make them both useful and dangerous?**

Derivatives do not create or destroy risk — they *transfer* it to whoever takes the other side and *transform* it into a finely sliced, concentrated form; that same concentration (large economic exposure on a small cash footprint) is exactly what lets a hedger protect a portfolio cheaply *and* lets a speculator lose everything on a small market move, which is why usefulness and danger are two faces of the one property, leverage.

**A2. Why is a blow-up almost never caused by a single risk?**

Because the risks feed each other in a self-reinforcing loop. Leverage turns a modest adverse move into a large mark-to-market loss; the loss triggers a margin call; meeting the call forces selling; forced selling in a thin market pushes prices further against you; worse prices raise margins again; and a watching counterparty refuses to roll your financing. Leverage × liquidity × counterparty × correlation, looping. No single link is fatal — the loop is. A risk manager's job is not to eliminate any one box but to stop the *arrows* between boxes forming a fatal loop.

**A3. Distinguish market risk from leverage risk.**

Market risk is the "intended" risk that the underlying moves against you — price, rate, FX, or vol — measured with the Greeks, scenario analysis, and VaR. Leverage risk is *not* an independent source of loss; it is a *multiplier* on market risk. It changes the size and speed of a loss, not its direction. It arises from notional leverage (large notional on small margin) and from embedded gamma (a short-option position whose losses accelerate as the market moves).

**A4. What is wrong-way risk, and why is it the "venom" of counterparty risk?**

Wrong-way risk is the poisonous case where your exposure to a counterparty *rises exactly as their creditworthiness falls*, so the protection you counted on evaporates precisely when you need it. The archetype is AIG: it sold CDS protection on CDOs, so as the CDOs deteriorated it owed more *and* was itself failing. Buying sovereign-default protection from a bank domiciled in that same country is the textbook example — if the country defaults, the bank is failing too.

**A5. Name and separate the two flavours of liquidity risk, and explain how they couple.**

*Market (asset) liquidity risk* — you cannot exit a position without moving the price against yourself, or at all (spreads blow out, depth vanishes). *Funding liquidity risk* — you cannot raise cash to meet margin calls or roll financing, even though you are economically solvent. They couple into a spiral: needing cash forces you to sell, thin markets mean selling raises less cash and moves prices, which deepens the funding hole. This coupling is the LTCM and 2008 killer.

**A6. Why is model risk described as "silent," and give one crystallised example.**

Because the position looks fine on the screen right up until it doesn't — the screen itself uses the model, so a mispriced or mismarked position reveals nothing wrong until reality diverges from the model's regime. The 2008 Gaussian copula is the crystallised example: it assumed a tame correlation among mortgage defaults, so when house prices fell nationally and borrowers defaulted together (correlation → 1), even AAA senior CDO tranches took losses the model had rated near-impossible.

**A7. Define basis risk and explain why "hedged" is not "risk-free."**

Basis risk is the risk that a hedge does not move one-for-one with the thing it hedges; the "basis" is the difference between the spot price of your exposure and the price of the hedging instrument, and a hedge is perfect only if that basis stays constant. It arises from asset mismatch (jet fuel hedged with crude), maturity mismatch (5-month exposure hedged with 3-month futures rolled forward), or location/quality mismatch (Brent hedged with WTI). A hedger has not eliminated risk; they have *swapped* a large obvious market risk for a smaller subtler basis risk — usually a good trade, but not a free one.

**A8. In one line each, what single lesson does each of Barings, LTCM, and 2008 teach?**

Barings — *separate the front office from the back office*: a trader must never confirm and settle their own trades. LTCM — *survive the path, not just the destination*: leverage plus illiquidity is lethal even when you are ultimately right, and diversification fails when correlations go to 1. 2008 — *the market was too opaque, interconnected, and under-collateralised*: fix transparency, netting/clearing, and margining.

**A9. Central clearing is often said to "eliminate" counterparty risk. Correct the statement.**

It does not eliminate counterparty risk — it *mutualises and concentrates* it. A CCP novates itself between both sides of every trade, so banks face the clearing house instead of each other; it nets multilaterally, collects margin from all, and absorbs a default through its waterfall (defaulter's margin → defaulter's default-fund contribution → CCP's own capital → surviving members' contributions). Bilateral risk shrinks, but the CCP becomes a systemically critical single point of failure, and non-cleared trades still carry (now-margined) bilateral risk.

**A10. Distinguish variation margin from initial margin by what each protects against.**

Variation margin (VM) is the daily (or intraday) cash settlement of the mark-to-market *change*, so no large uncollateralised exposure can accumulate — it is backward-looking and prevents build-up; this is precisely what AIG was *not* posting. Initial margin (IM) is collateral sized to cover *potential future* exposure over the close-out period (e.g. a 99% move over 5–10 days) if the counterparty defaults — it is forward-looking, a buffer, and is *segregated* so it survives the counterparty's bankruptcy. A book can be fully VM'd today and still require IM.

**A11. Why can netting be "the difference between a haircut and a catastrophe"?**

Because without an enforceable close-out netting clause, a defaulted counterparty's administrator *cherry-picks*: they demand full payment on the trades where you owe, while you join the unsecured creditor queue for the trades where you are owed. Your true exposure is the *gross* amount. An enforceable ISDA master agreement collapses all offsetting trades into a single *net* claim, and collateral against that net number can push the loss toward zero — but only if the paperwork holds up in the relevant jurisdiction, which is why legal/documentation risk is real.

---

## Section B — Applied / Numerical Problems with Full Solutions

**B1. Leverage from notional and margin.** One E-mini S&P 500 future has a multiplier of 50, the index is 5,000, and initial margin is \$12,500. Compute the notional, the leverage, and the capital swing from a 1% index move. Then state the adverse move that wipes out the margin.

Notional $= 50 \times 5{,}000 = \$250{,}000$. Leverage $= 250{,}000 / 12{,}500 = \mathbf{20\times}$. A 1% index move changes the notional by $0.01 \times 250{,}000 = \$2{,}500$, which against \$12,500 margin is $2{,}500/12{,}500 = \mathbf{20\%}$ of capital for a 1% market move — leverage restated. The margin is fully wiped by an adverse move of $1/20 = \mathbf{5\%}$ (since $5\% \times 20 = 100\%$). ✓ An ordinary bad week ends the position; this is a feature, not a bug.

**B2. The margin call in full.** You post \$100,000 and go long 8 E-minis at 5,000 (multiplier 50). Initial margin \$12,500/contract, maintenance \$11,000/contract. The index falls 4% to 4,800 over three days. Compute the loss, remaining equity, the maintenance requirement, and the shortfall.

Loss per contract $= 50 \times (5{,}000 - 4{,}800) = 50 \times 200 = \$10{,}000$. Total loss $= 8 \times 10{,}000 = \mathbf{\$80{,}000}$.

Self-check via leverage: notional $= 8 \times 50 \times 5{,}000 = \$2{,}000{,}000$; leverage $= 2{,}000{,}000/100{,}000 = 20\times$; $4\% \times 20 = 80\%$ of \$100,000 $= \$80{,}000$. ✓

Equity now $= 100{,}000 - 80{,}000 = \mathbf{\$20{,}000}$. Maintenance required $= 8 \times 11{,}000 = \$88{,}000$. You are $88{,}000 - 20{,}000 = \mathbf{\$68{,}000}$ below maintenance, so a margin call is issued to restore equity (typically back to the initial \$100,000, i.e. an \$80,000 top-up). If you cannot post it, the position is liquidated *into the falling market*, crystallising the loss — and if the index rebounds to 5,100 the next week you would have profited had you survived. Leverage did not change whether you were right; it changed whether you stayed in the game. This is LTCM in miniature.

**B3. Gross vs net counterparty exposure.** You hold two offsetting swaps against Counterparty Z: Swap A marks +\$40m (Z owes you), Swap B marks −\$32m (you owe Z). Z defaults; recovery on unsecured claims is 40%. Compute your loss (a) with no netting, (b) with enforceable ISDA close-out netting, (c) with netting plus VM collateral covering the net exposure.

(a) **No netting:** you must pay the \$32m you owe on B in full, and recover only $0.40 \times 40 = \$16$m on the \$40m Z owes you. Net cash out $= 32 - 16 = \mathbf{\$16m}$ (plus a \$24m claim shortfall). Your true exposure was the *gross* \$40m.

(b) **Close-out netting:** the trades collapse to one net claim $= 40 - 32 = \$8$m, on which you recover 40%: loss $= 0.60 \times 8 = \mathbf{\$4.8m}$.

(c) **Netting + collateral:** if you hold VM covering the \$8m net exposure, your loss approaches $\mathbf{\$0}$. Same two economic trades, a \$16m hit or a near-zero hit, decided entirely by *legal documentation* and *collateral*. This is why post-2008 reform put netting and margining at the centre. ✓

**B4. Basis risk — the hedge that under-covers.** An airline will buy 1,000,000 gallons of jet fuel in three months and proxy-hedges with crude futures. At inception jet fuel is \$2.50/gal and crude \$1.90/gal-equivalent; three months later jet fuel is \$2.90 and crude \$2.15. The futures hedge covers 1,008,000 gallons. Compute the physical cost overrun, the hedge gain, the residual, and confirm it via the change in basis.

Physical overrun $= (2.90 - 2.50) \times 1{,}000{,}000 = 0.40 \times 1{,}000{,}000 = \mathbf{\$400{,}000}$.
Hedge gain $= (2.15 - 1.90) \times 1{,}008{,}000 = 0.25 \times 1{,}008{,}000 = \mathbf{\$252{,}000}$.
Residual (basis loss) $= 400{,}000 - 252{,}000 = \mathbf{\$148{,}000}$ still unhedged; the hedge covered $252/400 = 63\%$ of the price rise.

Self-check via the basis: basis moved from $(2.50 - 1.90) = \$0.60$ to $(2.90 - 2.15) = \$0.75$, a widening of $\$0.15$/gal. On 1,000,000 gal that is \$150,000 of adverse basis, matching the ~\$148,000 residual (the small gap is the 1,008,000-vs-1,000,000 contract-granularity rounding). ✓ The refining margin (crack spread) changed, so jet fuel and crude did not move one-for-one. The airline was not reckless — proxy hedging is standard — but "hedged" was not "risk-free."

**B5. Sizing to survive the path.** A relative-value fund has \$100m equity and runs 25:1 balance-sheet leverage, so it holds \$2,500m of positions. A crisis marks the book down 6% and correlations that were assumed to diversify go to 1. Compute the loss and the resulting equity, and state what happens next.

Loss $= 0.06 \times 2{,}500{,}000{,}000 = \mathbf{\$150m}$ against \$100m of equity — the fund is insolvent, equity $= 100 - 150 = \mathbf{-\$50m}$. A move that on the diversified model looked like a fraction of a standard deviation wipes out capital because leverage multiplies it 25× and the correlation-to-1 removes the offsets the model relied on. Margin calls arrive, the fund must sell crowded positions the whole Street copied, moving prices further against it (liquidity spiral). The convergence trades may be *right* eventually — but the fund is forced out before the destination arrives. Being right in the long run and dead in the short run is a statement about margin. ✓ (This is the LTCM arithmetic in outline.)

**B6. Convex losses from short gamma.** A trader is short options and loses at a rate that scales roughly with the *square* of the move: a 1% move costs \$1m. Estimate the loss on a 2% move and a 5% move, and state the danger signature.

With loss $\propto (\text{move})^2$: at 2%, loss $\approx (2/1)^2 \times 1 = 4 \times 1 = \mathbf{\$4m}$; at 5%, loss $\approx (5/1)^2 \times 1 = 25 \times 1 = \mathbf{\$25m}$. A move 5× larger costs 25× more, not 5× more. The danger signature of leverage-plus-gamma is that losses are *convex* — a short-gamma position loses at an *increasing* rate, its delta getting worse exactly as you would need it to get better. This convexity is the engine behind Barings' short-straddle book into the Kobe jump and every vol-selling blow-up. ✓

---

## Section C — Interview-Style Questions with Model Answers

**C1. "Why are derivatives dangerous?"**

Model answer: "Three things compounding: leverage, mark-to-market, and interconnection. A small margin controls a large notional, so a small market move causes a large loss — 20× leverage turns a 1% move into a 20% capital swing. Because positions are marked to market daily, that loss immediately triggers a margin call, and meeting it by selling into an illiquid market pushes prices further against you — the margin spiral. And in OTC markets the bilateral counterparty web transmits one firm's failure across the system, as with Lehman in 2008. Crucially none of these is fatal alone; the danger is the loop they form. Derivatives don't create risk — they concentrate it into a small footprint, and concentration is where danger lives."

**C2. "Tell me about a famous derivatives failure and what it teaches."**

Model answer: "LTCM, 1998 — my favourite because the lesson is counterintuitive. It ran relative-value convergence trades in fixed income, tiny mispricings between similar bonds, and because the edges were minuscule it applied roughly 25:1 balance-sheet leverage, far more counting derivatives notional. On calm-period models the diversified book looked safe. Then the Russian default triggered a flight to quality; every cheap illiquid position fell and every safe liquid one rose at once — correlations went to 1 and the diversification vanished. Margin calls flooded in, and to raise cash LTCM had to sell crowded trades the whole Street had copied, moving prices further against itself. It lost about \$4.6bn in months and the Fed orchestrated a bank bailout to stop the cascade. The lesson isn't 'the trades were wrong' — many were ultimately profitable for whoever held them after. It's that you must size to survive the *path*: leverage plus illiquidity is lethal even when you're right, and diversification is a fair-weather benefit."

**C3. "What actually was AIG's mistake in 2008?"**

Model answer: "AIG's Financial Products unit sold enormous amounts of CDS protection on CDOs — effectively insuring them — while posting almost no collateral, because the models and AAA ratings said default was near-impossible. That's textbook wrong-way risk: as the CDOs deteriorated, AIG owed more on the protection *and* was itself failing, so the very thing its counterparties were relying on was evaporating just when they needed it. Ratings downgrades then triggered collateral calls AIG couldn't meet — a funding-liquidity death spiral — which forced an \$85bn, ultimately roughly \$182bn, government rescue to stop every counterparty taking the loss simultaneously. The fix in the reforms is direct: mandatory variation margin so exposure is collateralised daily and can't silently accumulate the way AIG's did."

**C4. "Walk me through the four post-2008 reforms and which failure each targets."**

Model answer: "They came out of the G20 Pittsburgh 2009 agenda, implemented as Dodd-Frank, EMIR, and Basel III. First, central clearing of standardised OTC derivatives: a CCP novates itself between both sides, nets multilaterally, and mutualises defaults through a waterfall — this attacks the bilateral counterparty opacity and interconnection that froze markets after Lehman. Second, mandatory margining: variation margin settles mark-to-market daily so no large uncollateralised exposure builds — that's the AIG fix — and segregated initial margin covers potential future exposure over the close-out period if a counterparty defaults. Third, trade reporting to repositories and trading on organised platforms, so regulators can finally *see* the exposure network nobody could see in 2008. Fourth, higher risk-sensitive capital under Basel III, including an explicit CVA capital charge for counterparty-risk volatility, SA-CCR for measuring exposure, and a non-risk-based leverage ratio so banks can't game risk-weights to near-zero. The nuance worth adding: clearing *concentrates* risk into CCPs that are now too-big-to-fail themselves, and margining consumes huge amounts of high-quality collateral, which can be procyclical — margin calls spike in exactly the stressed markets where cash is scarcest, as we saw in March 2020."

**C5. "How would you manage a derivatives book responsibly?"**

Model answer: "In layers, on the assumption that any single layer can fail. Governance first — a board-set risk appetite and a risk function independent enough to veto the desk, which is what LTCM lacked. Segregation of duties so the front office can't settle its own trades — the Barings fix. Hard position, VaR, Greek, and concentration limits. Stress testing and Expected Shortfall to probe the tail VaR ignores, assuming correlations go to 1 and liquidity to 0. Daily collateral and enforceable ISDA netting so exposure stays net and covered. Liquidity buffers so I can survive margin calls without forced selling — the ability to *not* sell when everyone else must is itself an asset. Independent model validation and price verification, because the screen uses my model and looks fine until it doesn't. And basis/hedge-effectiveness monitoring, because a hedge is never perfectly one-for-one. The governing philosophy: size to survive the path not the destination, never trust a single number, and if you can't independently value it, don't trade it."

---

## Section D — Multiple-Choice Questions with Reasoning

**D1.** The single mechanism underlying almost every derivatives disaster is:

A) high transaction costs  B) notional-to-margin leverage and the margin spiral  C) tax mistiming  D) currency mismatch

**Answer: B.** Controlling a large notional on small margin means a small adverse move causes a large mark-to-market loss, which triggers a margin call, forced selling, worse prices, and more losses — the self-reinforcing spiral. A, C, and D are peripheral frictions, not the common engine of blow-ups.

**D2.** Leverage risk is best described as:

A) an independent source of loss  B) a multiplier on market risk  C) the same as counterparty risk  D) a type of operational risk

**Answer: B.** Leverage does not generate losses on its own; it *amplifies* market-risk losses, changing their size and speed but not their direction. That is why it is drawn as an amplifying arrow onto market risk in the taxonomy, not a separate root cause.

**D3.** Wrong-way risk is the situation where:

A) you hedge the wrong asset  B) your exposure to a counterparty rises as their creditworthiness falls  C) a model uses the wrong volatility  D) margin is posted in the wrong currency

**Answer: B.** Wrong-way risk is the correlation between your exposure growing and the counterparty's ability to pay shrinking — AIG is the archetype. A describes a basis/hedge error, C is model risk, D is an operational detail; none is wrong-way risk.

**D4.** Variation margin and initial margin differ in that:

A) they are identical for cleared trades  B) VM is a forward-looking buffer, IM settles today's MTM  C) VM settles today's MTM change, IM buffers potential future exposure over close-out  D) only IM is exchanged daily

**Answer: C.** VM is the backward-looking daily cash settlement of the mark-to-market change (preventing accumulation — the AIG fix); IM is the forward-looking, segregated buffer covering potential future loss over the close-out horizon if a counterparty defaults. B reverses the two; A and D are false.

**D5.** Without an enforceable close-out netting agreement, a defaulted counterparty's administrator will:

A) net all trades to a single claim  B) cherry-pick — demand what you owe in full while you queue for what you are owed  C) return all your collateral first  D) waive both legs

**Answer: B.** Cherry-picking is exactly why gross exposure, not net, is at risk absent enforceable netting: you must pay the losing trades in full and recover only a fraction on the winning ones. A is what netting *does* achieve; C and D do not happen in a default.

**D6.** LTCM's failure is best summarised as:

A) a rogue trader hiding losses  B) extreme leverage plus illiquidity plus correlation breakdown, forced out despite ultimately sound trades  C) selling CDS with no collateral  D) a fat-finger booking error

**Answer: B.** LTCM combined ~25:1 leverage, crowded illiquid convergence trades, and a flight-to-quality that drove correlations to 1, forcing liquidation into markets it had helped make. A is Barings, C is AIG, D is generic operational risk.

**D7.** The Gaussian copula's role in 2008 is an example of:

A) operational risk  B) basis risk  C) model risk — mispriced default correlation  D) funding liquidity risk

**Answer: C.** The copula assumed borrowers default largely independently; a national housing decline made them default together (correlation → 1), so even AAA senior tranches lost — the model was wrong about the regime. That is textbook model risk, distinct from the other three.

**D8.** A central counterparty (CCP) reduces systemic risk primarily by:

A) eliminating all counterparty risk  B) novating itself between both sides, netting multilaterally, and mutualising defaults via a waterfall  C) guaranteeing every trade is profitable  D) removing the need for margin

**Answer: B.** Novation converts an opaque bilateral mesh into a transparent hub-and-spoke, enabling multilateral netting and a centralised default waterfall. A overstates the effect (risk is concentrated into the CCP, not eliminated), C is nonsense, and D is the opposite of the truth — CCPs require margin.

**D9.** Metallgesellschaft's near-collapse is the textbook case of:

A) wrong-way risk  B) a rogue trader  C) basis/rollover risk with margin cash drains  D) copula model risk

**Answer: C.** MG hedged a long-dated supply obligation with short-dated futures that had to be rolled; contango on the roll plus mark-to-market margin calls on the futures leg drained cash even though the overall economic position was sound. A, B, and D belong to AIG, Barings, and 2008 respectively.

**D10.** "VaR tells me my worst case" is wrong because:

A) VaR is always understated by regulators  B) VaR gives a threshold, not the tail beyond it, and is calibrated on normal-period data  C) VaR ignores market risk entirely  D) VaR only applies to equities

**Answer: B.** VaR states a loss you won't exceed on, say, 99% of days; it says nothing about how bad the other 1% gets and is fitted to calm data that understates crises — which is why stress tests and Expected Shortfall exist. A, C, and D misstate what VaR is.

**D11.** Barings (1995) and the 2008 crisis are:

A) the same kind of failure  B) opposite ends — micro operational-controls failure at one firm vs macro systemic model/counterparty/interconnection failure  C) both caused by a rogue trader  D) both caused by central clearing

**Answer: B.** Barings was one rogue trader with no segregation of duties (micro, operational); 2008 was model risk, counterparty opacity, and interconnection across the whole system (macro, systemic). Different lessons, different fixes. C describes only Barings; D is anachronistic (clearing was a post-2008 *fix*).

---

*Self-verification notes: B1's 5% wipe-out reconciles with the 20× leverage (5% × 20 = 100%). B2's \$80,000 loss is cross-checked two ways (per-contract price change and leverage × move), and the shortfall (\$88k maintenance − \$20k equity = \$68k) is internally consistent. B3's three cases (\$16m / \$4.8m / ~\$0) isolate the effect of netting and collateral on identical trades. B4's \$148k residual matches the \$0.15/gal basis widening on 1,000,000 gal (~\$150k) within rounding. B5's \$150m loss on \$100m equity confirms insolvency from a 6% mark at 25× leverage. B6's convex 1×/4×/25× loss pattern confirms the square-law signature of short gamma. Formulas/relations used: Leverage = Notional/Margin, capital swing = move × leverage, net exposure = Σ MTM, loss = (1 − recovery) × claim, Basis = S_exposure − F_hedge, short-gamma loss ∝ (move)². Mechanisms mapped to reforms: AIG → VM; Lehman opacity → clearing + reporting; LTCM → limits + liquidity buffers + stress testing; Barings → segregation of duties.*
