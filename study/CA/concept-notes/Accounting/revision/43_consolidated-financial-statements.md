# Chapter 43 — Consolidated Financial Statements (Holding Companies)

## Snapshot
CFS present a parent + its subsidiaries **as one economic entity** (substance over form). Prepared **in addition to** (never replacing) standalone accounts. Governed by **AS 21**; **Sec 129(3) Companies Act 2013** mandates CFS for a company with any subsidiary/associate/JV. Trigger = **control**, not ownership %.

## Core concepts
- **Control** = >50% of **voting power** OR control of **composition of Board**. Either test suffices. Measured on *voting* equity (ignore non-voting/pref).
- **Full consolidation**: add assets, liabilities, income, expenses **line by line, 100%**, because control (not %) is the trigger; then carve out **Minority Interest (MI/NCI)** on the equity side.
- **Direct + indirect holdings combine** (chain): P 60% of Q, Q 70% of R → R is P's subsidiary; effective interest 60%×70% = 42%, but R fully consolidated.
- **Pre-acquisition profit** = reserves/P&L existing **on acquisition date** → **capital** (netted vs cost → goodwill/capital reserve). **Post-acquisition profit** = growth after acquisition → **revenue** (parent's share → consolidated reserves).
- Uniform accounting policies; same reporting date (gap ≤ 6 months). Exclude subsidiary only if control **temporary** (held for disposal) or **severe long-term restrictions** on fund transfer.
- Control ladder: **≤20%** investment (AS 13) · **>20–50% + significant influence** → associate (AS 23, **equity method**) · **>50% / Board control** → subsidiary (AS 21, full consolidation).

## Key provisions / rules — formulas, treatment

| Item | Formula |
|---|---|
| Holding % | Shares held by parent ÷ Total shares of subsidiary |
| Minority % | 100% − Holding % |
| **Minority Interest** | Minority % × (Share Capital + **ALL** Reserves & Surplus of sub on B/S date, pre + post) |
| **Cost of Control** | Cost of Investment − Parent's share of (Share Capital + **Pre-acq** profits) |
| → positive | **Goodwill** (non-current asset) |
| → negative | **Capital Reserve** (added to equity Reserves) |
| **Consolidated Reserves** | Parent's own reserves + Parent's share of **POST-acq** profits − Unrealised profit − Goodwill written off ± other adj |
| Mid-year split | Pre = opening reserves + opening P&L + (year profit × months **before** ÷ 12); Post = year profit × months **after** ÷ 12 |
| Unrealised profit in stock | Transfer price of **unsold** goods × profit margin fraction |
| Profit "on cost" | profit = sale × 25/125 |
| Profit "on sales" | profit = sale × 25/100 |

**Analysis of Profits** (master working note; do FIRST — feeds MI, goodwill, consolidated reserves): two columns Capital (pre-acq) | Revenue (post-acq). Parent's pre-acq share → goodwill; parent's post-acq share → consolidated reserves; minority's share of both + share capital → MI.

**Adjustment placement:**
- Revaluation of sub's assets **at acquisition** → **capital** column; asset carried at revalued figure. Post-acq extra depreciation on uplift → reduces revenue column.
- **Pre-acquisition dividend** received by parent → **return of capital**: reduce **Cost of Investment** AND reduce parent's P&L (reverse wrongly-booked income). Post-acq dividend = genuine income (avoid double count).
- Opening reserves/P&L are entirely **pre-acq**; only current-year profit is time-apportioned on mid-year acquisition.
- Bonus from **pre-acq** reserves → goodwill up (pre-acq reserve netted shrinks); from **post-acq** → consolidated reserves down; MI unchanged either way.
- Sub accumulated **loss** = negative profit; pre-acq loss **increases** goodwill; minority bears its share (MI can fall below share capital). Carry minus signs.

**Elimination of intra-group items** (Step 6):
- Mutual debtor/creditor, loans, bills → knock off **both** sides. Reconcile **cash/goods in transit** first if balances disagree (add in-transit item, then cancel equal amounts).
- Unrealised profit on stock → full amount out of **Inventory**; profit-side split by **who is the seller**:
  - **Parent sells to sub** → deduct **full** unrealised profit from Consolidated P&L.
  - **Sub sells to parent** → split: parent's share from Consolidated P&L, **minority's share reduces MI**.
- Intra-group dividend → eliminate from group income.

## Journal entries (worksheet eliminations, not book entries)
**(a) Cancel investment vs sub's equity (parent's share):**
Share Capital of Sub (parent share) Dr; Pre-acq Reserves (parent share) Dr; Goodwill Dr (if cost > net assets); To Investment in Subsidiary; To Capital Reserve (if net assets > cost).

**(b) Minority Interest:**
Share Capital of Sub (minority share) Dr; Reserves & Surplus of Sub (minority share) Dr; To Minority Interest.

**(c) Unrealised profit on closing stock:**
Consolidated P&L (Reserves) Dr; To Stock (Inventory).

**(d) Mutual debt:**
Sundry Creditors Dr; To Sundry Debtors.

## Worked mini-example
P acquires 30,000 of 40,000 shares (₹10) of Q on 1 Apr 2025 for ₹4,10,000 → **Holding 75%, Minority 25%**. On acquisition Q's GR ₹80,000, P&L ₹40,000; on B/S date GR ₹1,00,000, P&L ₹1,40,000, Share Capital ₹4,00,000. Q's creditors include ₹50,000 owed to P.
- Analysis: Capital (pre) = 80,000+40,000 = **1,20,000**; Revenue (post) = 20,000+1,00,000 = **1,20,000**.
- **MI** = 25% × (4,00,000 + 1,00,000 + 1,40,000) = 25% × 6,40,000 = **₹1,60,000**.
- **Cost of Control** = 4,10,000 − 75%×4,00,000 (3,00,000) − 75%×1,20,000 (90,000) = **Goodwill ₹20,000**.
- **Consolidated GR** = P's 4,00,000 + 75%×20,000 = ₹4,15,000; **Consolidated P&L** = P's 3,00,000 + 75%×1,00,000 = ₹3,75,000.
- Intra-group ₹50,000 → reduce Debtors and Creditors by ₹50,000 each.

## Exam traps & must-remember
1. Pre/post split uses **ACQUISITION date**, not year-start. Mid-year → **time-apportion** current-year profit; opening balances all pre-acq.
2. **MI ignores pre/post split** — minority gets its % of TOTAL equity on B/S date. Pre/post matters only for parent's share.
3. **Pre-acquisition dividend** = return of capital → reduce cost of investment + parent's P&L.
4. **Who is the seller** decides who bears unrealised profit; **full amount always out of Inventory**, only profit-side split differs.
5. "On cost" (×25/125) vs "on sales" (×25/100); apply **unsold fraction** only; re-sold outside group = realised, nothing eliminated.
6. Revaluation at acquisition = **capital**; restate asset on CFS; watch post-acq extra depreciation.
7. **Cum-dividend** cost includes a dividend the buyer will receive — strip it out; if from pre-acq profits, treat as return of capital.
8. Unrealised profit in **fixed asset** sale: eliminate from asset & profit; adjust future depreciation (partly unwinds each year).
9. **Proposed dividend** of subsidiary: under revised AS 4/Sch III, not a liability until declared — don't create unless question provides. *Verify current ICAI/AY.*
10. Balance the sheet — mismatch usually = mis-split pre/post, one-sided netting, one-sided unrealised-profit deduction, or purchase-price change not matched by parent's cash movement.

**Presentation (Schedule III):** Only **parent's** share capital shown; MI = separate line **between Shareholders' Funds and Non-current Liabilities** (AS 21); Goodwill on consolidation = non-current asset; Capital Reserve = added to Reserves. Heading: *"Consolidated Balance Sheet of X Ltd. and its Subsidiary Y Ltd. as at ..."* Disclose list of subsidiaries, ownership %, reason for any exclusion.

## One-line recall
- Control (>50% votes OR Board) triggers **100% line-by-line** consolidation; ownership % only carves out MI.
- **MI** = minority % × (Share Capital + ALL reserves on B/S date) — pre/post irrelevant.
- **Cost of Control** = Cost − parent's share of (SC + pre-acq profits); +ve = Goodwill, −ve = Capital Reserve.
- **Consolidated Reserves** = parent own + parent's share of post-acq − unrealised profit.
- Pre-acq = capital (nets vs cost); post-acq = revenue (to reserves); acquisition date governs, apportion if mid-year.
- Seller's identity splits unrealised profit; full amount always leaves Inventory; CFS must balance.
