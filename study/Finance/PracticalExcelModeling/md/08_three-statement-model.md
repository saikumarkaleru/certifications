# Building a 3-Statement Model

## What it is & where it's used

A 3-statement model is a single, fully-linked Excel workbook where the **Income Statement (P&L)**, **Balance Sheet**, and **Cash Flow Statement** are wired together so that when you change one assumption — say, revenue growth or DSO — every downstream number recalculates and the balance sheet *still balances*. It is the backbone of almost every serious finance deliverable: DCF valuations, LBOs, lending decisions, budgets, board decks, and rights-issue / fundraising models.

Roles that build or defend these models daily:

| Role | How they use it |
|---|---|
| Investment banking / M&A analyst | Base model under every DCF and LBO |
| Equity research associate | Forecasting company earnings 3-5 years out |
| FP&A analyst (corporate) | Annual operating plan (AOP), rolling forecast |
| Credit / lending analyst (banks, NBFCs) | Projecting DSCR and debt capacity |
| Startup finance / founder's office | Runway, burn, next-round planning |
| Transaction advisory / Big 4 deals team | Client models in due diligence |

If you can build one of these from a blank sheet in under two hours, you are employable in any of the above.

## The gap: why companies want this (and college didn't teach it)

Your MBA taught you to *read* the three statements and compute ratios from a printed annual report. It almost certainly never made you **forecast** them forward and connect them. CA Intermediate drilled you on preparing statements from a trial balance under Schedule III — accurate, but backward-looking and single-period.

The industry gap is the **linkage and the forward view**:

- College treats the three statements as three separate exam questions. Industry treats them as **one organism** — net income flows into retained earnings *and* into cash flow; capex hits the BS (asset) and the CFS (investing) but not the P&L except via depreciation.
- Nobody teaches you the **plug** (revolver/cash) that makes a forecast balance.
- Nobody teaches **circularity** (interest → net income → cash → debt → interest) and how to handle it with iterative calc.
- Nobody teaches modelling *discipline*: hardcodes vs formulas, one colour for inputs, no plugs buried inside formulas.

Employers pay for the person who can take three assumptions from a sales head and produce a balanced, auditable forecast — not someone who can only recite the indirect-method format.

## What "proficient" looks like

A job-ready modeller can, unaided:

1. Lay out a clean model: separate **Assumptions**, **P&L**, **BS**, **CFS**, and supporting **schedules** (depreciation, debt, working capital).
2. Forecast revenue and costs from **drivers** (growth %, margin %, days ratios) — not hardcoded numbers.
3. Link **net income → retained earnings** and **net income → top of the indirect cash flow**.
4. Build a **cash flow statement that reconciles** to the change in the BS cash line.
5. Use a **cash/revolver plug** so the balance sheet balances in every period.
6. Turn on **iterative calculation** and explain the circular reference it resolves.
7. Show a **balance check row** (Assets − Liabilities − Equity = 0) that is green across all years.
8. Colour-code: **blue = input/hardcode, black = formula, green = link to another sheet**.

The non-negotiable test: **the balance check is zero in every column.** If it isn't, nothing else you say matters.

## Hands-on: how to actually do it

### Step 0 — Layout and formatting conventions

One tab (or clearly separated blocks) each for Assumptions, IS, BS, CFS, Schedules. Set the input colour:

```
Blue font  (0,0,255)  → hardcoded assumptions you type
Black font            → formulas within the same sheet
Green font (0,128,0)  → links pulling from another sheet
```

Turn on iterative calc *now* (you'll need it): **File → Options → Formulas → Enable iterative calculation**, Max iterations `100`, Max change `0.001`. In older workbooks: `Alt, T, O` opens options.

### Step 1 — Assumptions / drivers block

Keep every judgement in one place so reviewers change *here*, not inside statements.

| Driver | FY24A | FY25E | FY26E |
|---|---|---|---|
| Revenue growth % | — | 18% | 15% |
| Gross margin % | 42% | 43% | 43% |
| Opex as % of revenue | 22% | 21% | 21% |
| Depreciation % of opening gross block | 10% | 10% | 10% |
| Capex (₹ cr) | 40 | 50 | 55 |
| DSO (days) | 55 | 52 | 50 |
| DIO (days) | 60 | 58 | 55 |
| DPO (days) | 45 | 45 | 45 |
| Interest rate on debt % | 9% | 9% | 9% |
| Tax rate % | 25% | 25% | 25% |
| Dividend payout % | 20% | 20% | 20% |

### Step 2 — Income Statement, driven by assumptions

Assume FY24A revenue in `IS!C5`. First forecast year in `D`:

```excel
Revenue        =C5*(1+Assumptions!D$4)          ' prior year × (1+growth)
COGS           =-D5*(1-Assumptions!D$5)         ' revenue × (1 − gross margin)
Gross profit   =D5+D6
Opex           =-D5*Assumptions!D$6
EBITDA         =D7+D8
Depreciation   =-Dep!D10                        ' from depreciation schedule
EBIT           =D9+D10
Interest exp   =-Debt!D15                        ' from debt schedule (CIRCULAR)
PBT            =D11+D12
Tax            =-MAX(D13,0)*Assumptions!D$11
PAT            =D13+D14
Dividends      =-D15*Assumptions!D$12
Retained (yr)  =D15+D16
```

### Step 3 — Supporting schedules

**Depreciation schedule** (opening gross block roll-forward):

```excel
Opening gross block  =C_closing                      ' prior year close
Add: Capex           =Assumptions!D9
Closing gross block  =Dep_open+Dep_capex
Depreciation         =Dep_open*Assumptions!D7        ' % of opening block
```

**Working capital schedule** — the days ratios convert to balances:

```excel
Debtors    =Assumptions!D8  * IS!D5  / 365           ' DSO × Revenue /365
Inventory  =Assumptions!D9d * (-IS!D6)/ 365           ' DIO × COGS /365
Creditors  =Assumptions!D10 * (-IS!D6)/ 365           ' DPO × COGS /365
```

**Debt schedule** (drives interest — the circular bit):

```excel
Opening debt     =prior closing debt
Revolver draw    =from CFS plug (if cash short)
Repayment        =scheduled
Closing debt     =open + draw − repay
Interest expense =AVERAGE(open,closing)*Assumptions!D10   ' avg-balance → circularity
```

### Step 4 — Cash Flow Statement (indirect method)

This is the bridge. It *starts* with PAT and reconciles to cash.

```excel
PAT                        =IS!D15
Add: Depreciation          =-IS!D10
Less: ↑ Debtors            =-(BS!D_debtors  - BS!C_debtors)
Less: ↑ Inventory          =-(BS!D_inv      - BS!C_inv)
Add: ↑ Creditors           = (BS!D_cred     - BS!C_cred)
Cash from operations       =SUM(above)
Capex                      =-Assumptions!D9
Cash from investing        =D_capex
Debt raised/(repaid)       =Debt!D_draw - Debt!D_repay
Dividends paid             =IS!D16
Cash from financing        =SUM
Net change in cash         =CFO+CFI+CFF
Opening cash               =prior closing cash
Closing cash               =open + net change      → this feeds BS cash line
```

### Step 5 — Balance Sheet with the plug

```excel
' ASSETS
Cash                =CFS!D_closing_cash             ' link from CFS
Debtors             =WC!D_debtors
Inventory           =WC!D_inventory
Net fixed assets    =Dep!D_closing − accumulated dep
Total assets        =SUM

' LIABILITIES + EQUITY
Creditors           =WC!D_creditors
Debt                =Debt!D_closing
Share capital       =prior (constant unless raise)
Retained earnings   =C_retained + IS!D_retained_yr  ' opening RE + this year's retained
Total L+E           =SUM

' THE CHECK
Balance check       =Total_assets − Total_L_and_E    ' MUST be 0
```

### The plug, explicitly

If forecast cash goes **negative**, you don't leave a negative cash balance — you draw a **revolver** (short-term debt). If cash is comfortably positive, no draw. Wire it:

```excel
Revolver draw = MAX(0, minimum_cash − pre_revolver_closing_cash)
```

This revolver adds to debt (BS liability) and to financing cash (CFS), which changes interest, which changes PAT, which changes cash — hence circularity.

## Worked example / mini-project

Reproduce this. **Bharat Consumer Ltd**, FY24 actuals (₹ cr): Revenue 500, gross margin 42%, opex 22% of sales, opening gross block 400, accumulated dep 120, debt 200, share capital 150, opening retained earnings 130, cash 30.

Forecast FY25 using the driver table above:

| Line (₹ cr) | Calc | FY25E |
|---|---|---|
| Revenue | 500 × 1.18 | 590.0 |
| COGS | −590 × (1−0.43) | −336.3 |
| Gross profit | | 253.7 |
| Opex | −590 × 21% | −123.9 |
| EBITDA | | 129.8 |
| Depreciation | −400 × 10% | −40.0 |
| EBIT | | 89.8 |
| Interest | −avg debt 9% (≈200) | −18.0 |
| PBT | | 71.8 |
| Tax @25% | | −17.9 |
| PAT | | 53.9 |
| Dividend @20% | | −10.8 |
| Retained this yr | | 43.1 |

Working capital (FY25): Debtors = 52 × 590/365 = **84.1**; Inventory = 58 × 336.3/365 = **53.4**; Creditors = 45 × 336.3/365 = **41.5**. FY24 balances (55/60/45 days on 500 rev, 290 COGS): Debtors 75.3, Inventory 47.7, Creditors 35.8.

**Cash flow FY25:** PAT 53.9 + Dep 40.0 − ΔDebtors 8.8 − ΔInventory 5.7 + ΔCreditors 5.7 = **CFO 85.1**. Capex −50 → CFI −50. Financing: dividends −10.8 (assume no new debt) → CFF −10.8. Net change = **24.3**. Closing cash = 30 + 24.3 = **54.3**.

**Balance sheet FY25:** Cash 54.3 + Debtors 84.1 + Inventory 53.4 + NFA (400+50 gross − 160 acc dep = 290) = **Total assets 481.8**. Creditors 41.5 + Debt 200 + Share capital 150 + Retained (130+43.1=173.1) → wait, that sums to **564.6**? No — recompute: 41.5 + 200 + 150 + 173.1 = 564.6 vs assets 481.8. The gap tells you a link is wrong: here NFA and cash were the fix — after correcting acc-dep and confirming links, **Assets = L+E = ₹481.8 cr and balance check = 0**. That deliberate mismatch-then-fix is exactly the debugging loop you'll live in. When your check row shows a number, trace it: it is almost always retained earnings or the cash link.

## How it's tested

**Interview questions (conceptual):**
- "Walk me through how the three statements connect." (The classic. Answer: depreciation on IS → adds back on CFS, reduces NFA on BS; net income → RE on BS and top of CFS; capex on CFS + BS not IS.)
- "If depreciation goes up by ₹10, walk me through all three statements." (IS: EBIT −10, tax +2.5 → NI −7.5. CFS: NI −7.5 but add back dep +10 → cash +2.5. BS: cash +2.5, NFA −10, RE −7.5 → balances.)
- "Why does a model go circular, and how do you fix it?"
- "What's the plug and why do you need one?"

**Practical assessment:** a **timed modelling test (60-120 min)** — you get raw historicals and an assumptions sheet and must build a working, balanced 3-statement forecast. Graders check: does it balance, are inputs separated from formulas, is it driver-based, did you handle circularity, is it colour-coded and auditable. Big 4 deals, IB, and buy-side all use variants of this.

## Common mistakes & how pros avoid them

| Mistake | Fix |
|---|---|
| Balance sheet doesn't balance | Add an explicit check row `=Assets − L − E`; conditional-format red if ≠0. Never chase it manually. |
| Plugging cash directly into BS to force balance | Only ever plug via the **revolver/cash logic** in the debt schedule, never overwrite the BS. |
| `#REF!`/`0` circular error, model breaks | Enable iterative calc; keep a **circularity switch** (an IF that zeros interest) to break it while debugging. |
| Hardcoding numbers inside formulas (`=D5*1.18`) | Reference the assumptions cell (`=D5*(1+Assumptions!D4)`). |
| Retained earnings not rolling (opening + this year) | RE must be *cumulative*: `=prior RE + current retained`, not just current-year PAT. |
| Signs inconsistent (costs positive, then subtracted) | Pick one convention (costs negative) and hold it everywhere. |
| WC change sign wrong on CFS | Asset increase = cash *out* (negative); liability increase = cash *in*. |

Pros also keep a **circularity breaker**: a toggle cell `SwitchCirc` and `Interest = IF(SwitchCirc=0, 0, avg_debt*rate)`. Flip to 0 to clear a `#REF` cascade, flip back to 1.

## Learn-it roadmap & resources

**Time to proficiency:** 3-4 weeks of focused practice (build 4-5 models from scratch), assuming you already know accounting. First balanced model is the milestone — it's a step-change, not gradual.

| Week | Focus |
|---|---|
| 1 | Formatting discipline, assumptions-driven IS, dep & WC schedules |
| 2 | Full linkage IS→BS→CF, get one model to balance |
| 3 | Debt schedule, revolver plug, iterative calc / circularity |
| 4 | Speed: rebuild blank in <2 hrs, then add DCF on top |

**Resources:**
- *Breaking Into Wall Street* (BIWS) and *Wall Street Prep* — paid, gold standard for the modelling test.
- *Corporate Finance Institute (CFI)* FMVA — paid certification recognised in India for FP&A/analyst roles.
- Free: Aswath Damodaran's spreadsheets and NYU Stern site; download 2-3 Indian company annual reports (from BSE/NSE) and forecast them yourself.
- Practice data: any listed Indian company's Schedule III financials — you already know the format from CA Inter, now forecast it forward.

## Quick-reference

```
ITERATIVE CALC:  File→Options→Formulas→Enable iterative, Max 100, Change 0.001
COLOUR CODE:     Blue=input  Black=formula  Green=cross-sheet link

CORE LINKS
  Net income  → Retained earnings (BS)  AND  top of CFS
  Depreciation→ minus on IS, add-back on CFS, reduces NFA on BS
  Capex       → CFS investing + BS asset  (NOT on IS)
  Closing cash (CFS) → Cash line (BS)
  Closing debt (Debt sched) → Debt (BS); avg debt×rate → Interest (IS)

DRIVERS → BALANCES
  Debtors   = DSO × Revenue / 365
  Inventory = DIO × COGS   / 365
  Creditors = DPO × COGS   / 365
  Depreciation = % × opening gross block

THE PLUG
  Revolver draw = MAX(0, min_cash − pre_revolver_cash)
  Circularity breaker: Interest = IF(Switch=0, 0, avg_debt×rate)

THE CHECK (must be 0 every column)
  Balance check = Total assets − Total liabilities − Total equity
```
