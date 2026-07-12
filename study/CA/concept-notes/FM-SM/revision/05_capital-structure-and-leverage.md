# Capital Structure & Leverage

## Snapshot
The financing decision trades higher expected owner return (cheap, tax-deductible debt) against higher risk of ruin (fixed interest paid in bad years too). **Leverage** measures how cost/financing structure magnifies profit swings; **capital structure theory** diagnoses whether adding debt makes owners richer or just bumpier. Value is highest exactly when WACC is lowest (Value = operating cash flow ÷ WACC).

## Core concepts
- **Vocabulary guard:** Capital structure = long-term mix only. Financial structure = whole liabilities side. Capitalisation = total long-term amount. Over-capitalised (too much total capital for earnings, low ROI) ≠ over-geared (too much debt) ≠ over-trading (too little capital for sales).
- **Operating leverage** (fixed operating costs; sales→EBIT) → **business risk** (from asset/technology choice). **Financial leverage** (fixed interest; EBIT→EPS) → **financial risk** (from financing choice). Business risk exists before financing (EBIT computed pre-interest).
- Leverage is highest **near its break-even** and decays toward 1 as you move away; always "at a stated activity level," never a fixed firm property.
- **maximise value ⟺ minimise WACC** — the axis of all four theories.

## Key provisions / rules

**Income skeleton:** Sales − Variable Cost = **Contribution** − Fixed Cost = **EBIT** − Interest = **EBT** − Tax = **PAT** − Pref Div = Equity earnings ÷ N = **EPS**.

| Concept | Formula | Notes |
|---|---|---|
| DOL | Contribution ÷ EBIT | Sales→EBIT; =1 if no fixed cost |
| DOL (units) | Q ÷ (Q − BEQ) | explodes near break-even |
| DFL | EBIT ÷ (EBIT − Interest) = EBIT/EBT | EBIT→EPS; =1 if no debt |
| DFL (with pref.) | EBIT ÷ [EBIT − I − PD/(1−t)] | gross up preference dividend |
| DCL | DOL × DFL = Contribution ÷ EBT | Sales→EPS; total risk |
| EPS | [(EBIT − I)(1−t) − PD] ÷ N | N = existing + new shares |
| Financial break-even EBIT | I + PD/(1−t) | EBIT where EPS = 0 |
| Operating break-even (units) | Fixed cost ÷ (s − v) | EBIT = 0 |
| Indifference EBIT | solve EPS₁ = EPS₂ | above → pick more debt |
| Favourable leverage test | ROI (EBIT/capital) > Kd | else debt drags EPS down |

**Reverse-engineering:** DCL ÷ DOL = DFL. Contribution = DOL × EBIT; Fixed cost = Contribution − EBIT; EBT = EBIT/DFL; Interest = EBIT − EBT; Debt = Interest ÷ rate. "Financial leverage = 2" usually means DFL (elasticity); "highly geared" means D/E amount.

**Capital structure theories** (V = S + D; Kd < Ke always):

| Feature | NI | NOI | Traditional | MM no-tax | MM tax |
|---|---|---|---|---|---|
| Held constant | Ke & Kd | Ko | neither | Ko | — |
| Ke as debt rises | constant | rises | rises (mild→sharp) | rises linearly | rises |
| WACC as debt rises | falls | constant | U-shaped | constant | falls |
| Optimal structure | 100% debt | none | sweet spot | none | ≈100% debt |
| Value | S=(EBIT−I)/Ke; V=S+D; Ko=EBIT/V | V=EBIT/Ko | — | V_L=V_U | V_L=V_U+tD |

- **NI:** Ke, Kd constant → WACC falls, gear to 100%.
- **NOI:** Ko fixed by business risk; V = EBIT/Ko; Ke = Ko + (Ko−Kd)(D/S); structure irrelevant.
- **Traditional:** U-shaped WACC, three stages (low gearing WACC falls → optimal zone → high gearing both Ke & Kd climb, WACC rises); optimum at bottom.
- **MM no-tax:** V_L = V_U by arbitrage/homemade leverage; Prop II: Ke = Ko + (Ko−Kd)(D/S).
- **MM tax:** V_L = V_U + t×D; V_U = EBIT(1−t)/Ke; shield = tD (Kd cancels, assumes permanent debt + enough profit).
- **Trade-off theory:** V_L = V_U + PV(tax shield) − PV(financial distress & bankruptcy costs). Distress: *direct* (legal/admin fees) vs *indirect* (lost customers/suppliers/staff, forgone projects — usually larger). Optimum where marginal tax benefit = marginal distress cost.
- **Pecking order (Myers):** retained earnings → debt → equity last (info asymmetry); no target ratio.

**Common theory assumptions:** only debt & equity; EBIT/assets fixed; 100% payout; constant business risk; rational investors (MM: perfect markets, no tax base case, equal borrowing rate).

## Worked mini-example (all three leverages)
50,000 units × ₹40; VC ₹24/unit; fixed ₹4,00,000; 10% debentures ₹10,00,000; tax 30%.
- Contribution = 50,000×16 = 8,00,000; EBIT = 8,00,000 − 4,00,000 = 4,00,000; Interest = 1,00,000; EBT = 3,00,000.
- DOL = 8,00,000/4,00,000 = **2.0**; DFL = 4,00,000/3,00,000 = **1.33**; DCL = 2.0×1.33 = **2.67** (= 8,00,000/3,00,000).
- Break-even = 4,00,000/16 = 25,000 units; firm at 2× BEQ → DOL = 50,000/(50,000−25,000) = 2.0 ✓. At 30,000 units DOL leaps to 6.0.

## Exam traps & must-remember
1. Preference dividend must be **grossed up** by /(1−t) in DFL and financial break-even.
2. "More leverage is good" ≠ "safe" — below indifference/break-even EBIT, high leverage gives *lower*/negative EPS.
3. DOL, DFL are not constants — computed at a base level; explode near break-even.
4. DFL = EBIT/EBT only valid with **no** preference shares.
5. **NI vs NOI:** NI capitalises income-to-equity (residual, optimum trend); NOI capitalises whole-firm operating income (irrelevant).
6. MM no-tax V_L = V_U; MM tax V_L = V_U + tD; state which world.
7. Homemade leverage: investor **borrows personally** to buy the undervalued unlevered firm (unwinds/lends if levered firm cheaper) — know both directions.
8. Include existing + newly issued shares in EBIT-EPS.
9. DCL = Contribution/EBT (not /EBIT = DOL, not EBIT/EBT = DFL).
10. Leverage magnifies both directions; falling sales → same multiplier negative.
11. Trading on equity benefits owners only when **ROI > Kd**.
12. MM-tax: capitalise EBIT(1−t) at Ke for V_U (not pre-tax EBIT); shield = tD regardless of rate.
13. Over-capitalisation ≠ over-gearing ≠ over-trading.
14. Valuation tables use **market** values (WACC = EBIT/V on market values), not book unless stated.

## One-line recall
- DOL = Contribution/EBIT; DFL = EBIT/EBT (gross up pref div); DCL = DOL×DFL = Contribution/EBT.
- Financial break-even EBIT = I + PD/(1−t); EPS = [(EBIT−I)(1−t) − PD]/N.
- Above indifference EBIT → more debt; below → more equity; sanity-check ROI > Kd.
- NI: WACC falls (100% debt). NOI/MM-no-tax: WACC flat (irrelevant). Traditional: U-shape (optimum). MM-tax: V_L = V_U + tD.
- Trade-off = tax shield vs distress cost; Pecking order = internal → debt → equity.
- Leverage magnifies feast and famine, largest near break-even.
