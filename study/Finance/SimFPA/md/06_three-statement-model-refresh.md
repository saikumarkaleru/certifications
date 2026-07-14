# Refreshing the 3-Statement Model (P&L to Balance Sheet to Cash Flow)

## The ask

It's **16 July 2026**. The bank relationship manager has asked NTSPL for a **projected balance sheet and cash flow** to support the working-capital limit renewal, and the CFO wants the same model to answer her own question: *"if we hit the budget, what does the balance sheet and cash position look like at 31 Mar 2027, and can we service the term loan?"*

> "Refresh the three-statement model off the budget P&L. I want the P&L flowing into a **balance sheet** driven by our DSO/DPO/DIO, a proper **term-loan schedule**, and an **indirect cash flow** that reconciles to the closing cash. And it must **balance** — assets = liabilities + equity — with the check cell showing zero. Bank wants it Thursday."

The core skill: a **linked** model where P&L → Balance Sheet → Cash Flow, no hard-coded plugs, ending cash on the cash-flow statement equals cash on the balance sheet.

## What you're given

**Budget P&L (Rs cr, FY2026-27):**

| Line | Amount |
|---|---:|
| Revenue | 12.00 |
| COGS | (8.40) |
| Gross profit | 3.60 |
| Employee + Other opex | (1.86) |
| Depreciation | (0.144) |
| EBIT | 1.596 |
| Finance cost | (0.09) |
| PBT | 1.506 |
| Tax (~26%) | (0.396) |
| **PAT** | **1.11** |

**Balance-sheet drivers (FY2026-27):** DSO 60 days, DPO 45 days, DIO 40 days. Term loan **Rs 1.20 cr @ 9.5%**, repaid **Rs 15 lakh/quarter** (Rs 60 lakh/yr). Capex **Rs 40 lakh**; depreciation Rs 14.4 lakh. **Opening cash Rs 35 lakh.** No dividend.

**Opening balance sheet (1 Apr 2026), Rs cr — the model's starting point:**

| Assets | | Liab & Equity | |
|---|---:|---|---:|
| Net PPE | 1.00 | Creditors | 0.90 |
| Inventory | 0.75 | Term loan | 1.20 |
| Debtors | 1.70 | Share capital | 0.50 |
| Cash | 0.35 | Reserves | 1.70 |
| **Total** | **3.80** | **Total** | **3.80** |

## Build it — step by step

**Step 1 — Working capital from ratios.** Each closing balance is a driver × a P&L flow:

```
Debtors   = Revenue × DSO/365 = 12.00 × 60/365 = 1.97
Inventory = COGS    × DIO/365 = 8.40  × 40/365 = 0.92
Creditors = COGS    × DPO/365 = 8.40  × 45/365 = 1.04
```

These tie to the shared anchors (debtors ~2.0, inventory ~0.9, creditors ~1.05).

**Step 2 — PPE roll-forward.**
```
Closing PPE = Opening PPE + Capex − Depreciation = 1.00 + 0.40 − 0.144 = 1.256
```

**Step 3 — Debt schedule (term loan).** Interest is charged on the **average balance** so the P&L finance cost reconciles:

| Term loan (Rs cr) | Q1 | Q2 | Q3 | Q4 | FY |
|---|---:|---:|---:|---:|---:|
| Opening | 1.20 | 1.05 | 0.90 | 0.75 | 1.20 |
| Repayment | (0.15) | (0.15) | (0.15) | (0.15) | (0.60) |
| Closing | 1.05 | 0.90 | 0.75 | **0.60** | 0.60 |
| Interest @9.5% on avg | 0.027 | 0.023 | 0.020 | 0.016 | **~0.09** |

Average FY balance ≈ Rs 0.90 cr; `0.90 × 9.5% ≈ Rs 0.086 cr ≈ Rs 0.09 cr` finance cost — matching the P&L anchor.

**Step 4 — Equity roll-forward.**
```
Closing reserves = Opening 1.70 + PAT 1.11 − Dividend 0 = 2.81
```

**Step 5 — Indirect cash flow** (rebuild cash bottom-up; it must land on the BS cash):
```
CFO = PAT + Depreciation − ΔDebtors − ΔInventory + ΔCreditors
    = 1.11 + 0.144 − (1.97−1.70) − (0.92−0.75) + (1.04−0.90)
    = 1.11 + 0.144 − 0.27 − 0.17 + 0.14 = 0.954
CFI = − Capex = −0.40
CFF = − Loan repayment = −0.60
Δ Cash = 0.954 − 0.40 − 0.60 = −0.046
Closing cash = 0.35 − 0.046 = 0.304  (≈ 0.30)
```

**Step 6 — The circularity.** Interest depends on the average debt balance; if the model funds shortfalls via a **revolver/overdraft**, interest also depends on the cash line — which depends on cash flow, which depends on interest. That's a **circular reference**. Two fixes:
- **Enable iterative calculation:** *File → Options → Formulas → Enable iterative calculation, Max iterations 100, Max change 0.001.* Excel then solves the loop.
- **Circularity switch (safer for auditability):** a flag cell `Circ_ON` (1/0). Interest = `IF(Circ_ON, rate×AVERAGE(open,close), rate×open)`. Turn it off to break `#REF!`/spiral errors, on to solve. Many shops charge interest on **opening balance only** to avoid the loop entirely — cleaner, marginally less precise.

## The deliverable

**Projected Balance Sheet, 31 Mar 2027 (Rs cr):**

| Assets | | Liab & Equity | |
|---|---:|---|---:|
| Net PPE | 1.256 | Creditors | 1.04 |
| Inventory | 0.92 | Term loan | 0.60 |
| Debtors | 1.97 | Share capital | 0.50 |
| Cash | 0.30 | Reserves | 2.81 |
| **Total assets** | **4.45** | **Total L+E** | **4.45** |
| | | **Check (A − L−E)** | **0.00** |

**Cash Flow Statement (indirect, Rs cr):**

| | FY |
|---|---:|
| PAT | 1.11 |
| + Depreciation | 0.144 |
| − Increase in debtors | (0.27) |
| − Increase in inventory | (0.17) |
| + Increase in creditors | 0.14 |
| **Cash from operations** | **0.954** |
| Capex | (0.40) |
| **Cash from investing** | **(0.40)** |
| Loan repayment | (0.60) |
| **Cash from financing** | **(0.60)** |
| **Net change in cash** | **(0.046)** |
| Opening cash | 0.35 |
| **Closing cash** | **0.30** |

**Commentary:** "On budget, NTSPL ends FY27 with a **balanced sheet at Rs 4.45 cr**, cash easing from Rs 35 to Rs 30 lakh. Operations throw off **Rs 95 lakh**, but Rs 30 lakh is absorbed by working-capital growth (debtors and inventory rising with the business), Rs 40 lakh goes to capex, and Rs 60 lakh de-levers the term loan to Rs 0.60 cr. The Rs 4.6 lakh cash draw is comfortable but thin — a bad debtors quarter would pressure it, which is exactly why the working-capital limit renewal matters. Debt service is easily covered: EBIT Rs 1.60 cr vs interest Rs 0.09 cr (interest cover ~18×)."

## How it's reviewed

- **The check cell = 0.** Assets − (Liabilities + Equity) must be zero, not "Rs 400 rounding." A non-zero check = a broken link somewhere.
- **Cash ties twice.** Closing cash on the CF statement must equal cash on the balance sheet — the ultimate integrity test of a linked model.
- **No plugs.** Every BS line must roll from opening + a driver. If the controller finds a hard-typed number where a formula belongs, it fails.
- **Ratios back-check:** re-derive DSO from the model (`Debtors/Revenue×365 = 1.97/12×365 = 60`) — must return the input.
- **Interest reconciles** to the debt schedule, not a random 9.5% × 1.20.

## Common mistakes & red flags

- **Plugging cash to force a balance.** The cardinal sin — if you type the cash figure to make A = L+E, the model is lying. Cash must *fall out* of the cash flow.
- **Sign errors on working capital.** An *increase* in debtors is a cash *outflow* (negative); an increase in creditors is an *inflow* (positive). Flip one sign and the check breaks by 2× the delta.
- **Double-counting depreciation.** It's added back in CFO (non-cash) *and* reduces PPE — both, not either.
- **Circular-reference spiral (`0` or `#REF!` everywhere).** Forgetting to enable iterative calc, or leaving it on when a genuine error enters. Keep the circularity switch.
- **Interest on closing (not average) balance** overstates the de-levering benefit; on opening overstates cost. Average is the honest middle — state which you use.
- **Tax on EBIT instead of PBT.** Tax is on profit *after* interest.

## On the job & in the interview

The 3-statement model is the FP&A rite of passage — banks, boards, and diligence all want it. The mantra: **P&L drives the balance sheet, the balance sheet drives cash, and cash proves the P&L was real.**

**Q: "Walk me through how a Rs 10 increase in depreciation flows through all three statements."**
"P&L: EBIT and PBT fall by 10, tax falls by ~2.6, so PAT falls by ~7.4. Cash flow: PAT down 7.4 but depreciation is added back +10, so CFO rises by +2.6 — the tax shield. Balance sheet: PPE falls 10, cash rises 2.6, and retained earnings fall 7.4; both sides move by −7.4 and it still balances."

**Q: "What causes circularity and how do you handle it?"**
"Interest expense feeds the P&L, which drives cash, and if a revolver funds shortfalls, the debt balance depends on that cash — so interest depends on itself. I enable iterative calculation (100 iterations, 0.001 tolerance) with a circularity switch to break it if an error spirals, or I charge interest on the opening balance to avoid the loop entirely."

**Q: "Your model won't balance — how do you find the error?"**
"Check the CF closing cash against BS cash first; the gap size often names the culprit. Then I audit working-capital signs, confirm every BS line rolls from opening + driver with no plug, and re-derive the ratios. Ninety percent of the time it's a sign flip on a working-capital movement or a missing add-back."
