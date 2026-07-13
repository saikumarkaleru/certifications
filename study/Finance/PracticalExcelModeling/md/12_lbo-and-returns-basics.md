# LBO & Returns Model Basics

## What it is & where it's used

A Leveraged Buyout (LBO) is the acquisition of a company funded mostly with **debt** and a slice of **equity**. A private-equity (PE) fund buys a business, uses the target's own cash flows to repay that debt over 4-6 years, and sells at exit. Because debt is paid down and (hopefully) the business grows, the equity slice multiplies in value. The LBO model is the spreadsheet that proves the deal makes money — it links **Sources & Uses**, a **debt schedule with a cash sweep**, and an **equity returns** block (IRR and MOIC).

Who builds these:
- **PE / buyout funds** (Blackstone, KKR, in India: ChrysCapital, Kedaara, Multiples, True North) — every deal is an LBO model.
- **Investment banking** (Leveraged Finance, Sponsors coverage, M&A) — banks size the debt and stress-test it.
- **Credit funds / NBFC structured finance** — lend into the deal, model the debt from the lender's side.
- **Corp-dev / strategy** teams doing acquisitions with acquisition financing.
- **Equity research / valuation** — an LBO gives a "floor" valuation (what a financial buyer would pay).

It is the single most common technical case in PE and LevFin interviews.

## The gap: why companies want this (and college didn't teach it)

MBA finance teaches NPV, WACC, and CAPM — a *cost of capital* mindset. LBO is a *cash-and-debt-paydown* mindset. The gap is specific:

- College values a firm with one discount rate. PE cares about **how the capital structure changes year by year** as debt amortizes.
- College treats leverage as a WACC input. In an LBO, leverage is the **engine of returns** — you must build the debt schedule that mechanically sweeps free cash into repayment.
- Textbooks skip the **circularity**: interest depends on debt balance, which depends on cash sweep, which depends on cash-after-interest. Real models handle this with iterative calc or an interest-on-opening-balance shortcut.
- Nobody teaches **Sources & Uses** or how a returns bridge decomposes IRR into deleveraging vs. EBITDA growth vs. multiple expansion.

Employers pay for someone who can build the whole thing in 45 minutes without a template.

## What "proficient" looks like

A job-ready person can, unaided:

1. Build a **Sources & Uses** table that balances to the penny.
2. Compute entry Enterprise Value from an **EV/EBITDA** multiple and back into equity cheque.
3. Build a **debt schedule** for a Term Loan (mandatory amortization + cash sweep) and a revolver.
4. Project a simple **FCF-before-debt** line and route it through the sweep.
5. Compute **exit equity value**, then **MOIC** (= exit equity / entry equity) and **IRR** using `=IRR()` or `=XIRR()`.
6. Explain a **returns bridge**: how much of the gain came from paying down debt vs. growing EBITDA vs. selling at a higher multiple.
7. Run sensitivities (entry multiple, exit multiple, leverage) with a **Data Table**.

## Hands-on: how to actually do it

### Step 1 — Sources & Uses

Uses = what you pay for. Sources = how you fund it. They must equal.

| Sources | Rs cr | Uses | Rs cr |
|---|---|---|---|
| Term Loan (Debt) | =`D_ebitda*4.0` | Purchase Enterprise Value | =`EntryEBITDA*EntryMult` |
| Sponsor Equity (plug) | =Total Uses − Debt | Transaction fees (2%) | =`EV*0.02` |
| **Total Sources** | =SUM | **Total Uses** | =SUM |

Excel — say entry EBITDA in `B3`, entry multiple in `B4`, leverage (Debt/EBITDA) in `B5`:

```
EV               =B3*B4
Debt             =B3*B5
Fees             =EV*0.02
Total Uses       =EV+Fees
Equity (plug)    =Total_Uses - Debt      ' the sponsor cheque
```

### Step 2 — Project EBITDA and FCF

```
Year                1        2        3        4        5
EBITDA          =prior*(1+g)  ...
Less: D&A       =-EBITDA*0.06
EBIT            =EBITDA+D&A
Less: Interest  =-Opening_Debt*rate      ' link to debt schedule
EBT             =EBIT+Interest
Less: Tax@25%   =-MAX(EBT,0)*0.25
Net Income      =EBT+Tax
Add: D&A        =-D&A line
Less: Capex     =-EBITDA*0.05
Less: ΔNWC      =-Revenue_change*0.10
FCF (pre-sweep) =NI + D&A + Capex + ΔNWC
```

### Step 3 — Debt schedule with cash sweep

The sweep: after mandatory amortization, any leftover cash **prepays** the term loan.

```
Opening Debt          =prior Closing Debt
Mandatory amort (5%)  =-MIN(Opening, Original_TL*0.05)
Cash avail for sweep  =FCF_pre_sweep + Mandatory_amort   ' amort already negative
Optional sweep        =-MIN(MAX(Cash_avail,0), Opening+Mandatory_amort)
Closing Debt          =Opening + Mandatory + Optional_sweep
Interest expense      =Opening_Debt * rate               ' opening-balance avoids circularity
```

Using **opening balance** for interest breaks the circular reference — the standard interview shortcut. (Production models use average balance + enable iterative calc: File > Options > Formulas > Enable iterative calculation, max 100.)

### Step 4 — Exit and returns

```
Exit EBITDA       = Year-5 EBITDA
Exit EV           = Exit_EBITDA * Exit_Multiple
Exit Net Debt     = Year-5 Closing Debt − Cash
Exit Equity       = Exit_EV − Exit_Net_Debt
MOIC              = Exit_Equity / Entry_Equity
IRR               = (MOIC)^(1/Years) − 1        ' single in/out shortcut
```

In Excel with actual dated cash flows (equity out at entry, in at exit):

```
=IRR({-Entry_Equity, 0, 0, 0, 0, Exit_Equity})
=XIRR(values_range, dates_range)     ' when dates are irregular
=MOIC^(1/5)-1                          ' quick CAGR check
```

## Worked example / mini-project

**Target:** an Indian mid-market auto-components firm. Entry EBITDA Rs 100 cr, entry multiple 8.0x, EBITDA grows 8%/yr, hold 5 years, exit at 8.0x (flat — conservative). Leverage 4.0x. Interest 11%. Tax 25%. D&A 6% of EBITDA, Capex 5%, ΔNWC 10% of revenue growth (assume EBITDA≈EBIT proxy for simplicity, revenue ≈ 2x EBITDA).

**Sources & Uses (Rs cr):**

| Uses | Rs cr | Sources | Rs cr |
|---|---|---|---|
| Entry EV (100 × 8.0) | 800 | Term Loan (4.0x) | 400 |
| Fees (2%) | 16 | Sponsor Equity | 416 |
| **Total** | **816** | **Total** | **816** |

**Debt paydown (opening-balance interest, 5% mandatory amort, full sweep):**

| Year | EBITDA | Interest@11% | Tax@25% approx | FCF pre-sweep | Opening Debt | Closing Debt |
|---|---|---|---|---|---|---|
| 1 | 108 | 44.0 | ~13 | ~58 | 400 | 342 |
| 2 | 116.6 | 37.6 | ~16 | ~66 | 342 | 276 |
| 3 | 126.0 | 30.4 | ~19 | ~72 | 276 | 204 |
| 4 | 136.0 | 22.4 | ~22 | ~80 | 204 | 124 |
| 5 | 146.9 | 13.6 | ~26 | ~88 | 124 | 36 |

(FCF ≈ EBITDA − interest − tax − capex − ΔNWC; numbers rounded to show the mechanic, not to the last rupee.)

**Exit:**

```
Exit EBITDA      = 146.9
Exit EV          = 146.9 × 8.0 = 1,175
Exit Net Debt    = 36
Exit Equity      = 1,175 − 36 = 1,139
Entry Equity     = 416
MOIC             = 1,139 / 416 = 2.74x
IRR              = 2.74^(1/5) − 1 = 22.3%
```

**Returns bridge — where did the 2.74x come from?** With a *flat* multiple, every rupee came from **EBITDA growth** (100 → 147) and **deleveraging** (net debt 400 → 36). Zero from multiple expansion. That is a *clean, defensible* deal — you don't need to sell higher than you bought.

Reproduce it: put assumptions in a block, build the 5-year strip, and add a two-way **Data Table** (Data > What-If Analysis > Data Table) with exit multiple across the top (7.0x–9.0x) and leverage down the side (3.0x–5.0x) referencing the IRR cell. You'll see IRR swing roughly 15%–30%.

## How it's tested

**Interview questions:**
- "Walk me through an LBO." (Sources & Uses → buy → pay down debt with FCF → sell → equity multiplies.)
- "What are the 3 drivers of LBO returns?" (Deleveraging, EBITDA growth, multiple expansion.)
- "If I double the leverage, what happens to IRR?" (Higher — smaller equity cheque — but higher risk / interest burden.)
- "Why use opening-balance interest?" (Avoids circular reference in a timed test.)
- "MOIC of 2.5x over 5 years ≈ what IRR?" (~20%; know 2x/5yr≈15%, 3x/5yr≈25%.)

**Practical tests companies give:**
- **Paper LBO** (no computer, 5 min): entry 5x, exit 5x, given growth and paydown — compute IRR mentally. Extremely common at PE first rounds (ChrysCapital, Everstone, bulge-bracket LevFin).
- **Timed Excel LBO** (30-60 min): build the full model from a one-page CIM summary. Judged on: does S&U balance, is the debt schedule right, no hardcodes, clean IRR.
- **Take-home case**: full model + 2-slide recommendation over a weekend.

## Common mistakes & how pros avoid them

| Mistake | Fix |
|---|---|
| Sources ≠ Uses | Always make **equity the plug** = Total Uses − Debt. Never hardcode equity. |
| Forgetting **fees** in Uses | Add transaction + financing fees; they raise the equity cheque. |
| Circular-reference `#REF` spiral | Use **opening-balance** interest, or enable iterative calc deliberately. |
| Sweeping debt **below zero** | Wrap sweep in `=MIN(cash, opening_balance)` so it can't over-repay. |
| Confusing EV and equity at exit | Exit **equity** = Exit EV − **net debt**. Subtract debt, add cash. |
| MOIC vs IRR confusion | MOIC ignores time; IRR is annualized. A 3x over 10 years (12% IRR) is worse than 2x over 3 years (26%). |
| Assuming multiple expansion | Model **flat exit multiple** as base case. Expansion is a bonus, never the thesis. |
| Ignoring a **cash flow sanity check** | FCF must stay positive; if interest > FCF the deal is over-levered. |

## Learn-it roadmap & resources

**Time to proficiency:** 2-3 weeks of focused practice to build one unaided; 6-8 weeks to be interview-fast (including paper LBOs).

| Week | Focus |
|---|---|
| 1 | Sources & Uses + entry/exit mechanics. Build the S&U 10 times. |
| 2 | Debt schedule + cash sweep + circularity. This is the hard part. |
| 3 | Returns bridge, sensitivities, paper LBOs on a stopwatch. |

**Resources:**
- **Free:** Wall Street Prep / Macabacus free LBO tutorials; Aswath Damodaran (NYU) sessions on YouTube for the valuation base; Corporate Finance Institute free templates.
- **Paid:** Breaking Into Wall Street (BIWS) "LBO Modeling" course; Wall Street Prep Premium; Rossum / Financial Edge for the India/UK market.
- **Certification:** CFA (Level II corporate finance / equity), or FMVA (CFI) which includes an LBO module. For India PE roles, a strong self-built model beats any certificate.
- **Practice:** rebuild any listed mid-cap as an LBO — pull EBITDA from screener.in, assume 4x leverage, model 5 years.

## Quick-reference

```
EV               = EBITDA × Entry Multiple
Equity (entry)   = Total Uses − Debt          [equity is the plug]
Total Uses       = EV + Fees
Interest         = Opening Debt × rate         [avoids circularity]
Sweep            = MIN(FCF_after_mandatory, Opening Debt)
Closing Debt     = Opening − Mandatory − Sweep
Exit Equity      = Exit EBITDA × Exit Mult − Net Debt
MOIC             = Exit Equity / Entry Equity
IRR              = MOIC^(1/years) − 1          [single in/out]
```

| Quick IRR ↔ MOIC (5-year hold) | MOIC | IRR |
|---|---|---|
| | 1.5x | ~8% |
| | 2.0x | ~15% |
| | 2.5x | ~20% |
| | 3.0x | ~25% |
| | 4.0x | ~32% |

**Three return drivers:** (1) Deleveraging — debt paid by FCF. (2) EBITDA growth — organic + margin. (3) Multiple expansion — sell higher than bought (model flat; treat as upside).

**Key Excel:** `=IRR()`, `=XIRR(values,dates)`, `=MIN()`/`=MAX()` for the sweep, Data > What-If > Data Table for sensitivities, File > Options > Formulas > Enable iterative calculation for average-balance interest.
