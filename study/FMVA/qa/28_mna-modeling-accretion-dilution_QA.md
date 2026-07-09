# Q&A — M&A Modeling — Accretion / Dilution

A companion practice bank to Chapter 28. Work Sections B and C with a blank Excel sheet open; every computational answer is fully reconciled so you can check each line against your own build.

---

## Section A — Concept Check

**A1. In one fraction, what is accretion/dilution analysis measuring?**
It compares one number before and after a deal: EPS = Net Income ÷ Shares Outstanding. A merger changes *both* the numerator (pro-forma net income) and the denominator (pro-forma shares). If pro-forma EPS is higher than the acquirer's standalone EPS, the deal is accretive; if lower, dilutive. The headline metric is Accretion/(Dilution)% = PF EPS ÷ Standalone EPS − 1.

**A2. Why do boards obsess over EPS impact rather than strategic merit first?**
Share price ≈ EPS × P/E. Holding the multiple roughly constant, an accretive deal mechanically lifts the acquirer's price and a dilutive one lowers it on day one, before any synergy is realised. Management is paid on stock price and judged on EPS growth, so the EPS question is the financial and political gatekeeper of nearly every acquisition.

**A3. Which financing source changes the numerator, which changes the denominator, and which changes neither?**
Cash and debt change only the *numerator*: cash spent forfeits after-tax interest income; new debt adds after-tax interest expense. Stock changes only the *denominator*: it issues new shares and enlarges the slice count, but carries no interest cost. No source is free — each pays "rent" somewhere.

**A4. State the entire theory of accretion/dilution in one line.**
A deal is accretive when the after-tax yield of what you buy exceeds the after-tax cost of how you pay for it.

**A5. For an all-stock deal, what single comparison predicts the sign of the result?**
Compare the acquirer's P/E with the P/E paid for the target (purchase price ÷ target net income). If the acquirer's P/E is higher than the deal P/E, the all-stock deal is accretive — you fund each dollar of target earnings with richly priced paper, giving up fewer slices than the added income warrants. This is multiple arbitrage.

**A6. For a cash- or debt-financed deal, what comparison predicts the sign?**
Compare the target's earnings yield (target NI ÷ purchase price) with the after-tax financing rate. If the earnings yield exceeds the after-tax cost of cash or debt, the deal is accretive.

**A7. Why must every interest and synergy line be taken after tax?**
Interest expense is tax-deductible, so new debt interest costs the company only rate × (1 − tax) in net income. Foregone interest income would itself have been taxed, so losing it reduces net income only by rate × (1 − tax). Synergies are pre-tax operating gains that flow to the bottom line net of tax. Modeling any of these pre-tax overstates the earnings effect.

**A8. What are "breakeven synergies" and why do boards ask for them?**
They are the pre-tax annual synergy amount that makes pro-forma EPS exactly equal standalone EPS — the point where a dilutive deal just washes. The number reframes the debate from a yes/no verdict into a feasibility question: "Can management credibly deliver $X of synergies?"

**A9. Is "accretive" the same as "value-creating"? Explain.**
No. Accretion is an arithmetic consequence of financing. A deal funded with cheap debt can be accretive even while destroying value through overpayment or poor strategic fit. Accretion is a market-optics and feasibility screen; a DCF is the value arbiter. Serious deals must pass both.

**A10. Which share count belongs in the denominator, and why does it matter?**
Diluted shares (treasury-method options, convertibles), not basic. Using basic shares understates the count and overstates EPS both before and after the deal — and can flip the sign of a marginal result.

**A11. How are new shares issued computed in a stock deal?**
New shares = stock consideration in dollars ÷ the *acquirer's* share price (equivalently, target shares × exchange ratio, where exchange ratio = target offer price ÷ acquirer price). It is the acquirer's price, never the target's, because the acquirer is issuing its own paper.

---

## Section B — Build / Computational Problems

Base company for all three problems — **Acquirer:** net income $600m, 300m diluted shares, share price $40. Standalone EPS = 600 ÷ 300 = **$2.00**; acquirer P/E = 40 ÷ 2.00 = **20.0x**. Tax rate 21% throughout.

### B1 — All-stock deal (multiple arbitrage)

**Target:** net income $80m; equity purchase price $800m; financing 100% stock; no synergies.

| Line | Formula | Value |
|---|---|---|
| Standalone acquirer EPS | 600 / 300 | $2.00 |
| Stock consideration ($) | 800 × 100% | $800m |
| New shares issued | 800 / 40 | 20.0m |
| PF shares | 300 + 20 | 320.0m |
| Foregone interest (no cash) | — | $0 |
| New debt interest (no debt) | — | $0 |
| PF net income | 600 + 80 | $680m |
| PF EPS | 680 / 320 | **$2.1250** |
| Accretion/(dilution) | 2.1250 / 2.00 − 1 | **+6.25%** |

**Reconciliation & intuition.** Deal P/E = 800 ÷ 80 = 10.0x, below the acquirer's 20.0x, so multiple arbitrage predicts accretion — confirmed at +6.25%. With no financing cost, the only forces are +$80m income vs +20m shares; 680 ÷ 320 = $2.125 > $2.00.

### B2 — Same deal, all cash

Finance the same $800m entirely with **cash earning 5% pre-tax**. Nothing else changes.

| Line | Formula | Value |
|---|---|---|
| Cash used | 800 × 100% | $800m |
| New shares | — | 0 |
| PF shares | 300 + 0 | 300.0m |
| Foregone interest (after tax) | 800 × 5% × (1 − 0.21) | $31.6m |
| PF net income | 600 + 80 − 31.6 | $648.4m |
| PF EPS | 648.4 / 300 | **$2.1613** |
| Accretion/(dilution) | 2.1613 / 2.00 − 1 | **+8.07%** |

**Reconciliation & intuition.** More accretive than the stock version (+8.07% vs +6.25%) because the denominator never grows. Target earnings yield = 80 ÷ 800 = 10.0% crushes the after-tax cash cost = 5% × 0.79 = 3.95%. When what you buy yields more than your financing costs, cash beats stock — the classic case for cash-rich acquirers in low-rate environments.

### B3 — A dilutive mix, plus breakeven synergies

New story. **Target:** net income only $30m, but the acquirer pays a full **$900m** (a rich 30x deal). Financing: **60% debt at 8% pre-tax, 40% stock.** No synergies yet.

| Line | Formula | Value |
|---|---|---|
| Debt raised | 900 × 60% | $540m |
| Stock consideration | 900 × 40% | $360m |
| New shares | 360 / 40 | 9.0m |
| PF shares | 300 + 9 | 309.0m |
| After-tax debt interest | 540 × 8% × (1 − 0.21) | $34.128m |
| PF net income | 600 + 30 − 34.128 | $595.872m |
| PF EPS | 595.872 / 309 | **$1.9284** |
| Accretion/(dilution) | 1.9284 / 2.00 − 1 | **−3.58%** |

**Reconciliation & intuition.** Dilutive by 3.58%. Target earnings yield = 30 ÷ 900 = 3.33%, below the after-tax debt cost of 8% × 0.79 = 6.32%; and the stock portion also adds shares. Both numerator (interest) and denominator (new shares) work against you — you paid too much for too little earnings.

**Breakeven synergies.** Solve for the pre-tax synergy that makes PF EPS = standalone EPS:

Breakeven = (Standalone EPS × PF shares − PF NI ex-synergy) ÷ (1 − tax)
= (2.00 × 309 − 595.872) ÷ (1 − 0.21)
= (618 − 595.872) ÷ 0.79
= 22.128 ÷ 0.79 = **$28.01m pre-tax**.

**Verify:** after-tax synergies = 28.01 × 0.79 = $22.128m; PF NI = 595.872 + 22.128 = $618.0m; PF EPS = 618 ÷ 309 = **$2.00** = standalone exactly. The reconciliation is clean. Any synergy above $28.0m makes the deal accretive; below, it stays dilutive. The board debate shifts from "yes/no" to "can we deliver $28m of synergies?"

---

## Section C — Interview-Style Questions (with model answers)

**C1. Walk me through how an all-stock acquisition affects the acquirer's EPS.**
Model answer: "Start with the acquirer's standalone EPS = net income ÷ diluted shares. In an all-stock deal I add the target's net income to the numerator — there's no financing cost because no cash leaves and no debt is raised. To the denominator I add new shares = stock consideration ÷ the acquirer's share price. Pro-forma EPS = combined net income ÷ enlarged share count. Whether it's accretive comes down to one comparison: if the acquirer's P/E is higher than the P/E it's paying, the deal is accretive, because it funds cheap earnings with expensive paper."

**C2. A company trading at 25x P/E buys a target at 15x, all stock. Accretive or dilutive, and why?**
Model answer: "Accretive. The acquirer's paper is valued at 25x, but it's buying earnings at 15x. Each dollar of target earnings is funded by issuing stock worth 25 times a dollar of the acquirer's own earnings, so it gives up fewer slices than the added income justifies. Pure multiple arbitrage — accretive before any synergies."

**C3. Why can an all-cash deal be more accretive than the same deal done in stock?**
Model answer: "Cash keeps the share count flat — no dilution of the denominator. Its only cost is the after-tax interest the cash was earning. If the target's earnings yield exceeds that after-tax cash yield, you add more earnings than you give up, and because the denominator doesn't move, EPS rises more than in a stock deal where new shares dilute. In today's context you'd flag that this ignores the balance-sheet and opportunity-cost consequences of spending the cash."

**C4. This deal is accretive. Is it a good deal?**
Model answer: "Not necessarily. Accretion is an arithmetic result of the financing mix — cheap debt can make almost any deal accretive, even one that overpays or has a poor strategic fit. Accretion is a market-optics and feasibility screen, not a value test. I'd want to see the DCF and the returns analysis; a deal should be accretive *and* value-creating. Accretive alone is necessary for optics, not sufficient for wisdom."

**C5. A deal is dilutive by 5%. How do you decide whether it can still make sense?**
Model answer: "I'd compute breakeven synergies — the pre-tax synergy that makes pro-forma EPS equal standalone: (standalone EPS × PF shares − PF NI before synergies) ÷ (1 − tax). That converts the dilution into a hurdle. If breakeven is, say, $30m and management has a credible plan for $80m of cost synergies, the reported dilution is a Year-1 optics issue that reverses quickly. Many good deals are dilutive in Year 1 and accretive by Year 2 as synergies phase in."

**C6. How would you present the accretion result to a deal team — a single number or something else?**
Model answer: "Never a single point estimate — the answer depends on share price and interest rates, which move daily. I'd present a two-variable sensitivity table: offer price per share down the rows, % stock financing across the columns, output being accretion/dilution %, conditionally formatted green and red. The boundary line where the deal flips sign is the real deliverable; it shows the deal team exactly how much price or stock they can absorb before the deal turns dilutive."

**C7. What's the intuition for why stock carries no numerator cost but cash and debt do?**
Model answer: "Stock isn't free — it pays its rent in the denominator by permanently enlarging the slice count. Cash and debt keep the slice count fixed but pay rent in the numerator: cash forfeits the interest it was earning, debt adds interest expense, both after tax. Every financing dollar pays somewhere; the model's job is to route each dollar to its correct home."

---

## Section D — Common-Error Spotting

Each item shows a flawed approach; identify the error and the fix.

**D1.** *An analyst models new debt interest of $540m × 8% = $43.2m as a straight reduction to net income.*
Error: interest wasn't taken after tax. Interest is tax-deductible, so the net-income drag is 540 × 8% × (1 − 0.21) = $34.128m, not $43.2m. Modeling it pre-tax overstates the earnings hit and makes debt deals look worse than they are. Every financing-cost line needs a (1 − tax) factor.

**D2.** *For an all-cash deal, the model shows zero financing cost because "no debt was raised."*
Error: forgetting foregone interest on cash. Cash spent was earning interest; spending it forfeits that after-tax income. Omitting it makes all-cash deals look artificially accretive. Add Cash × cash rate × (1 − tax) as a numerator reduction.

**D3.** *New shares issued = stock consideration ÷ the target's share price.*
Error: wrong price. The acquirer issues its *own* shares, so new shares = stock consideration ÷ the *acquirer's* share price (or target shares × exchange ratio). Using the target's price mis-sizes the denominator and corrupts pro-forma EPS.

**D4.** *The financing mix is 30% cash, 40% debt, 25% stock, and the model runs without complaint.*
Error: the mix sums to 95%, silently under-funding the deal by 5% and producing a nonsense EPS. Always build a control-total check =cash% + debt% + stock% and conditionally format it red unless it equals exactly 100%.

**D5.** *A model uses the acquirer's basic share count of 290m instead of its diluted count of 300m.*
Error: basic instead of diluted shares. Diluted (treasury-method options, convertibles) is correct; basic understates the denominator and overstates EPS both before and after — and on a marginal deal can flip an accretive result to dilutive or vice versa.

**D6.** *Cost synergies of $40m are added to target net income (raising it to the combined line) and also entered separately in the synergies cell.*
Error: double-counting synergies. Synergies are added once, after tax, in a dedicated numerator line — not baked into target net income as well. Also watch the sign: cost synergies and revenue synergies add; integration costs subtract.

**D7.** *A pitch deck reports "the deal is +6% accretive" as a fixed conclusion.*
Error: treating the result as static. The 6% depends entirely on the assumed share price, interest rates and offer price, all of which move. Present it as a sensitivity grid across financing mix and offer price, and identify the sign-flip boundary — not a single headline point estimate.

**D8.** *An analyst justifies a deal purely on the grounds that it is accretive.*
Error: confusing accretion with value creation — the cardinal sin. Accretion follows mechanically from cheap financing and can coexist with overpayment and value destruction. Pair the accretion screen with a DCF; accretive is necessary for optics, never sufficient proof of a good deal.

---

*Self-check note: all Section B figures reconcile exactly — B1 PF EPS $2.1250 (+6.25%), B2 $2.1613 (+8.07%), B3 $1.9284 (−3.58%) with breakeven synergies of $28.01m restoring PF EPS to $2.00 precisely.*
