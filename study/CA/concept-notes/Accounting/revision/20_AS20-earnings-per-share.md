# Chapter 20 — AS 20 — Earnings Per Share

## Snapshot
EPS expresses performance per unit of ownership. AS 20 fixes every input so EPS is comparable and un-gameable. Two figures: Basic EPS (today's slice) and Diluted EPS (worst-case slice after potential shares convert). Mandatory for listed / to-be-listed enterprises; if any enterprise presents EPS it must follow AS 20 in full.

## Core concepts
- **Equity share** — residual claimant, subordinate to all other classes.
- **Potential equity share** — instrument that may become equity: convertible debentures, convertible preference, warrants, options, contingently issuable shares.
- **Dilution** — reduction in EPS (or increase in loss per share) on assumed conversion. **Anti-dilution** — increase in EPS (or reduction in loss) → excluded.
- **Options/warrants** = right to *buy* shares (fresh cash in). **Convertibles** = right to *swap* an existing instrument (no fresh cash).
- Scope: listed → both Basic & Diluted mandatory. Consolidated statements → EPS on consolidated figures; standalone → separate EPS. Present two sets, never blended. Schedule III requires EPS in notes for all companies.

## Key provisions / formulas

**Basic EPS = (Net profit after tax − Preference dividend) ÷ Weighted average number of equity shares.**

Numerator ("clean" equity profit): start with net profit after tax and after extraordinary items; deduct:
- **Cumulative preference dividend** — current year always, whether or not declared. Only the *current year* — NOT arrears (already deducted when they accrued).
- **Non-cumulative preference dividend** — only if declared/provided.
- Premium on redemption of preference shares / excess of buy-back consideration over carrying amount (a preference charge). Mirror: gain on buy-back below carrying amount is *added*.

Denominator (time-fair weighted average) — organising test: **"Did new resources enter the business?"**
- **Resources in (cash issue, shares for asset/acquisition, conversion of debt, dividend reinvestment, shares in lieu of interest/principal)** → include from date resource arrives; time-weight.
- **No resources (bonus, share split, consolidation/reverse split)** → treat as outstanding from *start of earliest period presented*; NO time-weighting; restate prior EPS.
- **Buy-back / cancellation** → subtract time-weighted from date it occurs.
- **Partly paid shares** → fraction of a full share = dividend-participation (paid-up) ratio. If they rank equally for dividend, count as full.
- **Contingently issuable shares** → in Basic EPS only from date all conditions met; before that, tested in Diluted.

**Rights issue (hybrid = bonus element + cash issue):**
- TERP = (Fair value of all shares before rights + Total amount received on rights exercise) ÷ Number of shares after rights.
- Adjustment factor = Fair value per share before rights (cum-rights close) ÷ TERP. Always ≥ 1; = 1 means no bonus element → treat as ordinary cash issue.
- Pre-rights shares × factor × time-fraction; post-rights shares × time-fraction. Restate prior EPS = old EPS ÷ factor.
- Fair value = cum-rights market price on last day traded *with* rights — NOT the issue price, NOT an average.

**Diluted EPS = (Basic numerator + after-tax interest on convertible debentures + preference dividend on convertible preference) ÷ (Basic shares + dilutive potential shares).**
- Add back convertible-debenture interest **net of tax**; convertible-preference dividend added back **without** tax adjustment (dividends are post-tax). Adjust for any consequential second-order income/expense (e.g. profit-based commission), net of tax.
- Potential shares assumed converted from **start of period, or issue date if later** (mid-year convertible time-weighted from issue).
- **Options/warrants — treasury stock method:** dilutive only if Exercise price < Average market price (average, because exercise can happen anytime). Incremental (free) shares = Options × (Market − Exercise) ÷ Market. Incremental EPS = 0, numerator effect nil → options always dilutive when in the money. ESOP with unrecognised service cost → add that amount to assumed proceeds (reduces dilution).
- **Anti-dilution sequencing:** (1) incremental EPS = after-tax numerator effect ÷ shares added; (2) rank smallest incremental EPS first (options at 0 usually first); (3) add one at a time; (4) keep only while running EPS falls; exclude the instrument (and all remaining) once its incremental EPS ≥ running diluted EPS. Test against **profit from continuing ordinary operations** (control figure), not against Basic, and not against total profit inflated by extraordinary gains.
- **Loss year → all potential shares anti-dilutive → Diluted EPS = Basic EPS** (both negative).

## Journal / presentation
No journal entries. Present **Basic and Diluted on the face of the Statement of P&L, equal prominence, every period**, for each class of equity with different rights; present even if negative; present Diluted even if equal to Basic (separate lines).

## Worked mini-examples
- **Basic (cash issue + buy-back):** Profit 8,00,000 − pref div (10% × 5,00,000 cumulative, undeclared) 50,000 = 7,50,000. WA shares: 1,00,000 + 30,000×8/12 − 12,000×3/12 = 1,17,000. EPS = ₹6.41.
- **Bonus (1:2, mid-year):** current 22,50,000 ÷ 9,00,000 = ₹2.50; bonus factor 1.5, restate prior 18,00,000 ÷ 9,00,000 = ₹2.00 (was ₹3.00).
- **Bonus + cash issue (Ex 2A):** bonus factor multiplies the *whole* WA. [4,00,000 + 2,00,000×9/12]×4/3 = 7,33,333; EPS ₹2.25.
- **Rights (Ex 3):** TERP = (2,00,000×25 + 50,000×15)/2,50,000 = ₹23; factor 25/23. WA = 2,00,000×(25/23)×9/12 + 2,50,000×3/12 = 2,25,543; EPS ₹4.21; prior restated 4.00×23/25 = ₹3.68.
- **Diluted (Ex 4):** debentures 1,60,000 shares, after-tax interest 2,40,000×0.7 = 1,68,000, incremental EPS ₹1.05; options 25,000 free shares, incremental EPS ₹0. Both dilutive → 11,68,000 ÷ 6,85,000 = ₹1.71. A 10% convertible pref (incremental EPS ₹5.00 > 1.71) is anti-dilutive → excluded.

## Disclosures
1. Numerators for Basic & Diluted + **reconciliation to net profit/loss** (net profit → less pref div → Basic numerator → add back after-tax interest/dividend → Diluted numerator).
2. Weighted-average shares (denominators) for Basic & Diluted + **reconciliation of the two** (Basic shares + dilutive potential = Diluted shares).
3. **Nominal (face) value** of shares with the EPS figures.
- Post-year-end **bonus/split/consolidation/rights-bonus-element** (before accounts approved) → recompute EPS for all periods on new share count; disclose fact. Post-year-end **cash/fair-value issue** → NO restatement; AS 4 non-adjusting disclosure only.

## Exam traps & must-remember
- Cumulative pref: deduct even if undeclared; non-cumulative: only if declared. Only current year, not arrears.
- Bonus/split NOT time-weighted; restate comparatives; bonus factor multiplies the whole WA (incl. mid-year cash shares).
- Rights at fair value → factor = 1 → ordinary cash issue, no restatement. Use cum-rights price for TERP.
- Debenture add-back net of tax; preference add-back gross.
- Rank by incremental EPS, test against *running* diluted EPS (not Basic); options first.
- Loss year: Diluted = Basic; dilution can only worsen a result.
- Buy-back reduces WA from buy-back date. Mid-year convertible dilutes only from issue date. Partly paid = fraction; contingent shares enter Basic only when condition met.
- Redemption/buy-back premium on preference deducted from numerator.

## One-line recall
- Basic EPS = (PAT − preference dividend) ÷ weighted-average equity shares.
- Numerator = equity's residual; denominator = time-fair count; the master question is "did resources enter?"
- Rights = bonus element (retrospective, via factor) + cash element (time-weighted); factor = FV before ÷ TERP.
- Diluted = worst case: add back after-tax interest & preference dividend, add dilutive potential shares.
- Options dilute via treasury stock (free shares, average market price); anti-dilutive instruments excluded, sequenced most-dilutive-first.
- Present Basic & Diluted on face, equal prominence, every period, even if negative or equal.
