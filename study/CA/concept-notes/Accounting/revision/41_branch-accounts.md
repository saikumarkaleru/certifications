# Branch Accounts (including Foreign Branches)

## Snapshot
Measure each branch's profit, strip unrealised inter-branch profit (loading), expose stock losses, and translate foreign figures (**AS 11**). A branch is **legally part of the company**. Two classification axes (separate): **dependent vs independent** (who keeps books) and **integral vs non-integral** (economic autonomy — foreign only).

## Core concepts
- **Dependent branch** — HO keeps books. Systems: Debtors / Stock-and-Debtors / Final Accounts / Wholesale.
- **Independent branch** — own books + trial balance; HO keeps Branch A/c and **incorporates** the TB after reconciling in-transit items. Reciprocal accounts (HO A/c in branch books, Branch A/c in HO books) end **equal and opposite**.
- **Foreign branch** — translate via AS 11 before incorporation.
- All three dependent systems give the **same net profit** (checksum).

## Key provisions / rules — formulas, treatment; tables

**Loading** (k% on cost → loading as fraction of invoice = k/(100+k)):
| Markup | Invoice=Cost× | Load %cost | Load %invoice | Cost %invoice |
|---|---|---|---|---|
| Cost+20% | 1.20 | 20% | 1/6 (16.67%) | 5/6 (83.33%) |
| Cost+25% | 1.25 | 25% | 1/5 (20%) | 4/5 (80%) |
| Cost+33⅓% | 4/3 | 33⅓% | 1/4 (25%) | 3/4 (75%) |
| Cost+50% | 1.50 | 50% | 1/3 (33.33%) | 2/3 (66.67%) |
**"Profit on sales/invoice"** = already loading-on-invoice → do NOT convert. Only "profit on cost" needs k/(100+k).

**Debtors System — Branch A/c (invoice price), four loading lines:**
- Dr: Opening stock (IP), Opening debtors, Goods sent (IP), Expenses paid by HO, **loading on closing stock**, Net profit (bal.).
- Cr: **loading on opening stock**, **loading on net goods sent**, Cash sales, Cash from debtors, Closing stock (IP), Closing debtors.
- At cost → drop all four loading lines.
- Credit sales, bad debts, discount, returns from customers → **only** in memorandum debtors working (net inside closing debtors), NOT shown separately.
- Branch fixed assets: opening → Dr, depreciated closing → Cr (**no separate "To Depreciation"** line).
- Closing debtors = Opening + credit sales − cash − discount − bad debts − returns.

**Stock & Debtors System (all at invoice price) — account sequence:**
1. **Branch Stock A/c** → Dr>Cr = shortage; Cr>Dr = surplus (balancing figure).
2. **Branch Adjustment A/c** (loading only): Cr = loading on opening stock + loading on **net** goods sent; Dr = loading on closing stock + loading on shortage + **Gross Profit** (bal.).
3. **Branch Debtors A/c** → closing debtors.
4. **Branch P&L A/c**: GP − expenses − bad debts − discount − **cost portion of shortage** = Net Profit.
- **Shortage:** cost portion (× cost fraction) → Branch P&L; loading portion → Branch Adjustment. **Surplus = mirror.**
- **Normal loss** (leakage/evaporation) → absorbed in GP rate (no separate loss line). **Abnormal loss** (fire/theft) → isolated: cost portion → P&L (net of insurance), loading → Adjustment.

**Stock Reserve:** create on **closing** stock (Dr profit), release on **opening** stock (Cr profit); balance-sheet stock shown at **cost** (IP − loading).

**Final Accounts System:** memorandum Branch Trading & P&L **at cost** — strip loading before entry; no reserve/loading line inside; net profit → HO General P&L.

**Wholesale Branch:** goods invoiced at wholesale price; branch profit = retail − wholesale margin only; stock reserve on **wholesale price − cost** of unsold branch stock.

**Foreign branch (AS 11):**
| | Integral (temporal) | Non-integral (closing rate/net investment) |
|---|---|---|
| Monetary items (cash, debtors, creditors, loans) | Closing rate | Closing rate |
| Non-monetary at cost (fixed assets, cost stock) | **Historical rate** | Closing rate |
| Income & expenses | Average rate (deprec at asset historical) | Average rate |
| Exchange difference | **→ P&L** | **→ FCTR** (to P&L only on disposal) |
- HO Account → its **₹ book value** (no rate).
- Integral vs non-integral test: *does a fall in foreign currency directly/immediately hit HO's cash flows?* Yes → integral; buffered → non-integral. Non-integral signs: settles in local currency, insulated cash flows, local market/pricing/financing/costs.
- Same data, different classification → **different reported profit**.

## Journal entries
Stock Reserve (create): Branch P&L / Branch Adjustment Dr → To Stock Reserve. (Release opening: reverse.)
Independent branch incorporation — two styles: **Detailed** (each income/expense/asset/liability merged line-by-line via Branch A/c) or **Abridged** (only net profit + assets/liabilities: Dr Branch A/c / Cr Branch P&L). Unrealised profit on branch stock eliminated via Stock Reserve.

## Worked mini-example
Foreign branch, non-integral. Opening stock $8,000 @ ₹70, purchases $40,000 @ ₹72 (avg), closing stock $9,000 @ ₹75 (closing), sales $60,000 @ ₹72, plant $12,000 @ ₹75. All assets/liabilities @ closing 75; income/expenses @ avg 72; opening stock @ opening 70; HO A/c at ₹ book. Exchange difference (balancing figure) → **FCTR** (not P&L). If instead **integral**: plant @ historical rate, opening stock @ its acquisition rate, monetary @ closing, difference → **P&L** — profit changes.

## Exam traps & must-remember
- "Cost + 25%" = 20% of invoice, NOT 25%.
- Credit sales/bad debts/discount in Debtors-System Branch A/c (they net inside closing debtors).
- Loading on **net** goods sent (after returns to HO).
- Shortage: only cost portion → P&L; loading portion → Adjustment. Surplus mirror.
- Stock Reserve direction: create on closing (Dr), release on opening (Cr).
- Depreciation: opening asset Dr + depreciated closing Cr, no separate line.
- Foreign: wrong rate for wrong item; exchange difference to P&L (integral) vs FCTR (non-integral).
- HO Account needs no rate.
- Independent branch: reconcile in-transit goods/cash first; adjust on books of whoever hasn't recorded it — never plug the gap to profit.
- Normal (absorbed) vs abnormal (isolated) loss decided by the cause word.
- Closing stock given at cost in a Stock-and-Debtors sum → gross up to invoice first.
- Wholesale branch reserve on wholesale−cost, not retail−cost.

## One-line recall
- Two axes: dependent/independent (books) and integral/non-integral (economics) — keep separate.
- Loading = k/(100+k) of invoice; strip it wherever unsold stock appears (Stock Reserve → stock at cost).
- Debtors System = one Branch A/c, profit = balancing figure; Stock-and-Debtors exposes shortage.
- All dependent systems give the same profit (checksum).
- AS 11: integral → temporal, difference to P&L; non-integral → closing rate, difference to FCTR.
- Independent branch: reconcile reciprocals to equal-and-opposite before incorporating.
