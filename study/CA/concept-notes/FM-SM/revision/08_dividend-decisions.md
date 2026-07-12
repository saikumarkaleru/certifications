# Dividend Decisions

## Snapshot
How much profit to pay out vs retain. The intellectual spine: **does the payout split change share value, or is it irrelevant?** Relevance school (Walter, Gordon, Graham–Dodd) says it matters; Irrelevance school (MM) proves it doesn't in perfect markets. All hinge on **r vs Ke** and real-world frictions (taxes, issue costs, information gaps).

- **Wealth = market price + dividend received** (not price alone).
- **Dividend policy** (long-run rule) ≠ single **dividend decision** (this year's declaration). Theories evaluate the policy.

## Core concepts
**Notation:** E = EPS; D = DPS; r = return on retained earnings; Ke = cost of equity (required); P = price; b = retention ratio = (E−D)/E; (1−b) = payout = D/E; g = growth = b×r.

**Identity chain:** payout = D/E = 1−b; b = (E−D)/E; g = br; b = g/r. Fix decimals vs % at top and convert before substituting.

**The one comparison ruling relevance:**
| Firm | Relationship | Optimal payout |
|---|---|---|
| Growth | r > Ke | 0% (retain all) |
| Declining | r < Ke | 100% (distribute all) |
| Normal | r = Ke | Indifferent |

## Key provisions / rules

| Model | Core formula | School / lever |
|---|---|---|
| Walter (1963) | P = [ D + (r/Ke)(E − D) ] ÷ Ke | Relevance; r vs Ke |
| Gordon (1962) | P = E(1 − b) ÷ (Ke − br) = D ÷ (Ke − g) | Relevance; bird-in-hand |
| Gordon reversed | Ke = D₁/P + g = D₁/P + br | Cost of equity |
| MM (1961) | P₀ = (P₁ + D₁) ÷ (1 + Ke) | Irrelevance; homemade dividends |
| MM firm value | nP₀ = [ (n+Δn)P₁ − I + E ] ÷ (1 + Ke) | |
| MM new shares | Δn × P₁ = I − (E − nD₁) | |
| Graham–Dodd | P = m(D + E/3) | Strong relevance (dividends ~3× retentions) |
| Linter | D₁ = D₀ + [(target payout × EPS) − D₀] × adjustment factor | Sticky dividends |

**Walter:** always a corner solution (0% or 100%) — coefficient on D is (1 − r/Ke)/Ke: negative if r>Ke (push D to 0), positive if r<Ke (push D to 100%). Assumptions: all-internal finance, constant r & Ke, constant EPS/DPS, infinite life. Criticism: constant r unreal (marginal r falls); entangles investment & dividend decisions.

**Gordon:** g = br (growth only from ploughback earning r). Guardrail **Ke > br** (else denominator ≤ 0, price infinite). Bird-in-hand: risk-averse investors value certain near dividends over uncertain gains; distant dividends discounted higher. Reverse form: grow D₀ → D₁ = D₀(1+g) when dividend "just paid." Assumptions: all-equity, no external finance, constant r & Ke, Ke > br, constant b, tax ignored.

**MM:** homemade dividends (investor sells/buys shares costlessly to make own cash pattern) → arbitrage → dividend irrelevant. D₁ **cancels** when Δn substituted — that cancellation *is* the proof. Bigger dividend → smaller retained earnings → bigger new issue → new shareholders capture exactly what old ones took as dividend (transfer, not value). If retained earnings ≥ I, Δn ≤ 0 (buyback, no fresh issue). New shares raised at **P₁** (year-end), not P₀. Assumptions: perfect markets, no taxes, no flotation costs, no transaction costs, fixed investment policy, perfect certainty.

**How real world revives relevance:** taxes differ (tax-preference for retention/buyback), flotation costs real (retention cheaper), transaction costs real (cash dividend serves income-seekers), information asymmetric (dividend signals).

**Residual theory:** dividend = earnings left after funding all r>Ke projects from (cheapest) retained earnings. Explains why growth firms pay nil, mature firms pay heavily. Implies volatile dividends (clashes with Linter's smoothing). Not a pricing formula.

**Forms of dividend:** cash; **stock dividend/bonus** (capitalises reserves → raises paid-up share capital, face value unchanged, reserves fall; wealth unchanged); **stock split** (only re-denominates face value ₹10→2×₹5, no reserve capitalised, total capital unchanged); scrip/bond. Bonus vs split: bonus increases paid-up capital, split does not.

**Buyback (Sec 68–70):** alternative route to return surplus cash; share count falls → EPS rises; tax-efficient (capital-gains route, verify current tax); flexible for one-off surplus (protects sticky-dividend signal); signals undervaluation, supports control. Dividend & buyback = two taps on same cash tank. EPS rise ≠ wealth creation (concentration only).

**Legal (Companies Act 2013 — verify current text):** Sec 123 — dividend only out of (a) current profits after depreciation, (b) accumulated past profits, or (c) government money; interim from surplus; transfer to reserves now optional. Unpaid dividend → Unpaid Dividend A/c → IEPF after 7 years.

**Factors (L-E-G-A-L + C):** Liquidity, Earnings stability, Growth/financing needs, Access to capital, Legal & contractual limits + Clientele, Control, Confidence-signalling; also taxation, inflation. Structure answer as internal / shareholder-facing / external.

## Worked mini-example
**Walter, E=₹10, Ke=12%, growth firm r=15% (r/Ke=1.25):**
| Payout | D | (r/Ke)(E−D) | Numerator | P = ÷0.12 |
|---|---|---|---|---|
| 0% | 0 | 12.50 | 12.50 | ₹104.17 |
| 50% | 5 | 6.25 | 11.25 | ₹93.75 |
| 100% | 10 | 0 | 10.00 | ₹83.33 |

Max at 0% payout → retain all. (Normal firm r=Ke: P = E/Ke = ₹83.33 at any payout.)

**Reverse Gordon:** P=₹120, D₀=₹6, b=40%, r=20%. g = 0.40×0.20 = 8%. **D₁ = 6×1.08 = ₹6.48** (grow it!). Ke = 6.48/120 + 0.08 = 0.054 + 0.08 = **13.4%**. (Using D₀ gives wrong 13%.)

## Exam traps & must-remember
1. Confusing r (firm earns) and Ke (shareholders require) — inverts every conclusion.
2. Percent vs decimal in r/Ke: 15%/12% = 1.25, not 0.15/12.
3. Forgetting final **÷ Ke** in Walter (whole bracket).
4. Gordon denominator non-positive when br ≥ Ke — flag "Ke > br violated."
5. MM's D₁ cancellation is the point — different firm values = arithmetic slip.
6. MM new shares issued at **P₁**, not P₀.
7. "Bonus increases wealth" — false; only packaging changes.
8. Higher dividend raises price only when r < Ke; for growth firm it *lowers* price.
9. Bird-in-hand is Gordon's, NOT MM's (MM reject it).
10. MM irrelevance is conditional on assumptions, not "always."
11. **D₀ vs D₁** in Gordon: "just paid" → grow by (1+g); "expected" → use as-is.
12. g is often not given — derive g = b×r; b = 1 − payout.
13. Bonus (capitalises reserves, raises paid-up capital, face value same) vs split (re-denominates only).
14. Residual theory explains *how much* is paid, not a price — don't compute a price from it.
15. Buyback's EPS rise ≠ wealth creation — cite tax/signalling/flexibility.
16. Legal ceiling (Sec 123) — carried-forward losses may bar payout.

## One-line recall
- r > Ke → retain (0% payout); r < Ke → distribute (100%); r = Ke → indifferent.
- Walter = level perpetuity, corner solution; Gordon = growing perpetuity, guardrail Ke > br, g = br.
- MM: homemade dividends + arbitrage → D₁ cancels → value set by investment policy, not payout.
- Gordon reversed = dividend-growth cost of equity: Ke = D₁/P + g (grow D₀ first).
- Bonus/split leave wealth unchanged; buyback's EPS rise is concentration, real gains are tax/signal/flexibility.
- Real world = between poles: sticky dividends (Linter), residual after capex, buybacks as flexible tax-smart route.
