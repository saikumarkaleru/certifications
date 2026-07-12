# Chapter 13 — Standard Costing & Variance Analysis

## Snapshot
Set a pre-determined "should be" cost per unit, compare with actual, and **split the gap into named pieces** each traceable to one cause/owner. Universal engine: **change one thing at a time** — price variance holds quantity at **actual**, usage variance holds price at **standard**. Every parent = sum of its children (the reconciliation is the proof). SQ/SH are always for **actual output**.

## Core concepts
- **Standard hour** = quantity of output that should be produced in one hour (output expressed in time).
- **Three-column skeleton** (material/labour/VOH): ① SQ×SP · ② AQ×SP · ③ AQ×AP → Usage/Efficiency = ①−②, Price/Rate = ②−③, Cost = ①−③.
- **Sign convention**: Cost variances = **Standard − Actual** (positive = Favourable). Sales = **Actual − Budget**. Master rule: **Favourable = increases profit**.
- **Joint variance** (SP−AP)×(SQ−AQ) is absorbed into the **price** variance (why price uses actual quantity).
- Standard types: **Ideal** (perfect, demotivating), **Basic** (fixed long-term, goes stale), **Current**, **Normal/Attainable** (preferred). Revise standards only for **permanent** changes.
- Budgetary control = totals/any function (extensive); standard costing = per-unit, needs measurable repetitive output (intensive/deeper).

## Key provisions / rules
Let SQ/SH = standard qty/hours **for actual output**; AQ/AH = actual; SP/SR = standard price/rate; AP/AR = actual; RSQ/RSH = revised standard (actual total in standard ratio); AI = qty purchased.

**Direct Material**
- MCV = (SQ×SP) − (AQ×AP)
- MPV = (SP − AP) × AQ  [use AI if price isolated at purchase point]
- MUV = (SQ − AQ) × SP    → **MPV + MUV = MCV**
- MMV = (RSQ − AQ) × SP
- MYV = (SQ − RSQ) × SP   → **MMV + MYV = MUV**
- RSQ = actual total input × standard mix ratio.
- Yield shortcut: MYV = (Standard output from actual input − Actual output) × Std cost per unit of output.
- Purchase-point: MPV on AI, stock at standard; MPV+MUV ≠ MCV (gap sits in closing stock).

**Direct Labour** (AH_paid; AH_worked = paid − idle)
- LCV = (SH×SR) − (AH_paid×AR)
- LRV = (SR − AR) × AH_paid   [hours **paid**]
- LEV = (SH − AH_worked) × SR  [hours **worked**]
- ITV = Idle hours × SR = (AH_paid − AH_worked) × SR — **always Adverse**
- → **LRV + LEV + ITV = LCV** (ITV=0 if no idle)
- LMV = (RSH − AH_worked) × SR; LYV = (SH − RSH) × SR → **LMV + LYV = LEV**
- Mix/yield use hours **worked** (strip idle first).

**Variable Overhead** (SR_v = std rate/hour)
- VOH Cost = (SH×SR_v) − Actual VOH
- VOH Expenditure = (AH_worked×SR_v) − Actual VOH
- VOH Efficiency = (SH − AH_worked) × SR_v  → **Exp + Eff = Cost**
- Use hours worked (no VOH during idle).

**Fixed Overhead** (FOR = Budgeted FOH ÷ Budgeted output or hours; Absorbed = actual output × FOR)
- FOH Cost = Absorbed − Actual
- FOH Expenditure (Budget) = Budgeted − Actual
- FOH Volume = Absorbed − Budgeted  → **Exp + Vol = Cost**
- FOH Capacity = (AH_worked − Budgeted hrs) × FOR/hr
- FOH Efficiency = (SH − AH_worked) × FOR/hr
- FOH Calendar = (Actual − Budgeted days) × Budgeted FOH/day  → **Cap + Eff + Cal = Vol**
- Revised Budgeted Hours = Budgeted hrs/day × actual days (measure capacity against revised when calendar applies, to avoid double count).

**Control ratios**: Capacity = AH_worked ÷ Budgeted hrs; Efficiency = SH ÷ AH_worked; Activity = SH ÷ Budgeted hrs = Capacity × Efficiency. Above 100% = Favourable.

**Sales — Margin (profit) method** (reconciles profit; SM = std margin/unit, AM = actual margin/unit; RBQ = actual total sales × budget mix ratio)
- Total Sales Margin = (AQ×AM) − (BQ×SM)
- Price = (AM − SM) × AQ = (AP − BP) × AQ
- Volume = (AQ − BQ) × SM  → **Price + Vol = Total**
- Mix = (AQ − RBQ) × SM; Quantity = (RBQ − BQ) × SM → **Mix + Qty = Vol**
- Marginal costing: SM = contribution/unit; **no FOH volume variance**.

**Sales — Value method** (does NOT reconcile to profit)
- Value = (AQ×AP) − (BQ×BP); Price = (AP − BP) × AQ; Volume = (AQ − BQ) × BP.

**Reconciliation**: Budgeted Profit ± Sales margin variances (→ standard profit on actual sales) ± Material ± Labour ± VOH ± FOH = **Actual Profit** (must tie exactly). Marginal: run budgeted→actual contribution, then subtract only FOH expenditure variance.

## Worked mini-example
Std/unit: material 5 kg @ ₹40; labour 3 hr @ ₹50. Actual: 1,100 units; 5,720 kg cost ₹2,37,380; 3,410 hrs cost ₹1,74,910 (no idle).
SQ = 1,100×5 = 5,500 kg; std mat = 2,20,000. SH = 3,300 hr; std lab = 1,65,000.
MCV = 2,20,000 − 2,37,380 = 17,380 A. MPV = (40−41.50)×5,720 = 8,580 A. MUV = (5,500−5,720)×40 = 8,800 A. (Sum = 17,380 A ✓)
LCV = 1,65,000 − 1,74,910 = 9,910 A. LRV = 1,74,910 − 3,410×50 = 4,410 A. LEV = (3,300−3,410)×50 = 5,500 A. (Sum = 9,910 A ✓)

## Exam traps & must-remember
1. **Flex to actual output** for SQ/SH — never budgeted output. Biggest fatal error.
2. Rate/idle use **hours paid**; efficiency uses **hours worked**.
3. Idle time **always Adverse**.
4. Price on purchases (AI) vs usage (AQ) — read wording.
5. FOH Volume is **under-recovery not overspending**.
6. Mix uses (RSQ−AQ), Yield uses (SQ−RSQ); RSQ total must = AQ total.
7. Sales sign flips: favourable = actual exceeds budget.
8. Only **margin** method reconciles to profit (value method won't tie).
9. Compute rate/price as (Actual cost − AQ×SP) to avoid rounding AP/AR.
10. Calendar variance only when actual days ≠ budgeted; then capacity uses revised budgeted hours.
11. If reconciliation won't tie, a sign is flipped — diagnose.
12. FOR on **budgeted** activity, never actual/standard-for-actual.
13. Don't mix marginal (contribution volume) with absorption (FOH volume) in one answer.
14. SQ = standard input for output achieved; RSQ = standard-ratio split of actual input.
15. Efficiency valued at correct rate: labour SR, VOH SR_v, FOH FOR — same hour deviation.
16. Don't blame an **uncontrollable** variance on a manager.

## One-line recall
- Price/rate holds quantity at actual; usage/efficiency holds price at standard.
- Cost variance = Standard − Actual; positive = Favourable; sales flips to Actual − Budget.
- Parent = sum of children at every node (Price+Usage=Cost, Mix+Yield=Usage, Cap+Eff+Cal=Vol).
- Idle time always adverse; rate uses paid hours, efficiency uses worked hours.
- FOR = Budgeted FOH ÷ Budgeted output; Absorbed = actual output × FOR; Volume = Absorbed − Budgeted.
- Activity ratio = Capacity × Efficiency; reconciliation lands exactly on actual profit.
