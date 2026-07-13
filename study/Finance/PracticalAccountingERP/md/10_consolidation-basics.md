# Consolidation basics in practice

## What it is & where it's used

**Consolidation** is combining a parent company and its subsidiaries into **one set of financial statements**, as if the group were a single economic entity. You don't just add the two balance sheets — you **eliminate** the internal relationships (the parent's investment, inter-company loans, inter-company sales) so the group statement shows only what the group owns and owes *to the outside world*.

In India this is governed by **Ind AS 110** (Consolidated Financial Statements) for listed / large companies and **AS 21** for others; globally it's **IFRS 10**. A company must consolidate when it **controls** another entity — practically, when it holds **more than 50% of voting power** (or controls the board / relevant activities).

Who does this at work:

| Role | Consolidation task |
|---|---|
| Group / Corporate accountant | Prepares the quarterly/annual consolidated financials |
| Audit associate (Big 4 / mid-tier) | Tests elimination entries, goodwill, NCI |
| FP&A analyst | Builds the consolidation model in Excel |
| M&A / valuation analyst | Computes goodwill on acquisition (PPA) |
| Financial reporting (controllership) | Owns the consol close each period |

Even a "single company" job touches this the moment the firm buys a stake, sets up a subsidiary, or spins off a division.

## The gap: why companies want this (and college didn't teach it)

College teaches the **theory** — "eliminate the investment against equity, recognise goodwill and minority interest" — usually with a clean single-line example. It almost never makes you build a real **consolidation worksheet** with columns, elimination journals, and a proof that it balances. So freshers can *recite* AS 21 but freeze when handed two trial balances and told "give me the consol by 6 pm."

The specific gaps employers see:

- Candidates confuse **elimination entries** (removing internals) with **regular journals** (they don't hit any single company's books — they live only in the consol worksheet).
- They can't compute **goodwill** correctly — they net the *whole* subsidiary equity instead of only the **parent's share**, and forget the **NCI on net assets**.
- They don't know that **pre-acquisition** profits get capitalised (part of goodwill) while **post-acquisition** profits flow to consolidated reserves.
- They can't split profit between the **parent** and **Non-Controlling Interest (NCI / minority interest)**.

Closing this gap = being the person who can actually *produce* the number, not just describe it.

## What "proficient" looks like

A job-ready person, handed a parent + subsidiary trial balance, can unaided:

1. Set up a **consolidation worksheet** (Parent | Subsidiary | Eliminations Dr | Eliminations Cr | Consolidated).
2. Compute **goodwill** = Cost of investment − Parent's share of net assets at acquisition.
3. Compute **NCI** = NCI % × net assets (at acquisition, then updated for post-acq movements).
4. Pass the **four core eliminations**: investment vs equity, inter-co debtor/creditor, inter-co sales/purchases, and **unrealised profit on stock**.
5. Split the year's profit into **owners of parent** and **NCI**, and prove the consol balances.
6. Explain *why* each entry exists in one sentence.

## Hands-on: how to actually do it

### The four eliminations you must know

**1. Cancel the parent's investment against the subsidiary's equity at acquisition** (this is where goodwill and NCI are born):

| Particulars | Dr (₹) | Cr (₹) |
|---|---|---|
| Share capital (subsidiary) | XXX | |
| Reserves at acquisition (subsidiary) | XXX | |
| Goodwill (balancing, if positive) | XXX | |
| To Investment in subsidiary (parent) | | XXX |
| To Non-Controlling Interest | | XXX |

**2. Cancel inter-company balances** (parent owes/lent to subsidiary):

| Particulars | Dr (₹) | Cr (₹) |
|---|---|---|
| Inter-company creditor | XXX | |
| To Inter-company debtor | | XXX |

**3. Cancel inter-company sales & purchases** (so group revenue isn't inflated):

| Particulars | Dr (₹) | Cr (₹) |
|---|---|---|
| Sales (inter-company) | XXX | |
| To Purchases / COGS (inter-company) | | XXX |

**4. Remove unrealised profit on closing stock** (goods still held within the group):

| Particulars | Dr (₹) | Cr (₹) |
|---|---|---|
| Consolidated P&L (COGS) | XXX | |
| To Inventory | | XXX |

### The Excel formulas that actually build the worksheet

Assume columns: `C`=Parent, `D`=Subsidiary, `E`=Elim Dr, `F`=Elim Cr. Consolidated column `G`:

```excel
# Assets (Dr nature): Parent + Sub + Elim Dr − Elim Cr
=C4 + D4 + E4 - F4

# Liabilities/Equity/Income (Cr nature): Parent + Sub − Elim Dr + Elim Cr
=C10 + D10 - E10 + F10

# Goodwill = Cost of investment − Parent% × Net assets at acquisition
=Cost_Invest - (Parent_pct * NA_acq)

# NCI at reporting date = NCI% × (Net assets at acquisition + post-acq reserves)
=NCI_pct * (NA_acq + Post_acq_reserves)

# Unrealised profit on stock = intra-group closing stock × margin
=IntraGroup_Stock * (GP_pct)         # if margin is on SALES
=IntraGroup_Stock * (Markup/(1+Markup))   # if profit is a % on COST

# Proof: total Elim Dr must equal total Elim Cr
=SUM(E:E)-SUM(F:F)      # must return 0
```

Use `SUMIF` to pull a full trial balance into the worksheet by account code:

```excel
=SUMIF(Parent_TB[Code], $B4, Parent_TB[Amount])
=SUMIF(Sub_TB[Code],    $B4, Sub_TB[Amount])
```

### Python check (reproducible, audit-friendly)

```python
cost_invest   = 1_800_000
parent_pct    = 0.80
sc_sub        = 1_000_000     # share capital of subsidiary
res_acq       = 500_000       # reserves at acquisition
na_acq        = sc_sub + res_acq

goodwill = cost_invest - parent_pct * na_acq
nci_acq  = (1 - parent_pct) * na_acq
print(f"Goodwill: Rs {goodwill:,.0f}")   # 1,800,000 - 0.8*1,500,000
print(f"NCI @acq: Rs {nci_acq:,.0f}")
```

## Worked example / mini-project

**Facts.** On 1 Apr 2025, **Parent Ltd** buys **80%** of **Sub Ltd** for **₹18,00,000**. At that date Sub's share capital = **₹10,00,000**, reserves = **₹5,00,000** (net assets = ₹15,00,000). By 31 Mar 2026 Sub's reserves have grown to **₹8,00,000** (so **₹3,00,000 post-acquisition** profit). During the year Parent sold goods worth **₹2,00,000** to Sub at a **25% margin on cost**; **₹1,00,000** of it is still in Sub's closing stock. Parent's own reserves = ₹40,00,000. Inter-company: Sub owes Parent ₹1,50,000.

**Step 1 — Goodwill:**
```
Goodwill = 18,00,000 − (80% × 15,00,000)
         = 18,00,000 − 12,00,000 = ₹6,00,000
```

**Step 2 — NCI at year-end:**
```
NCI = 20% × (Net assets at reporting date)
    = 20% × (10,00,000 + 8,00,000) = 20% × 18,00,000 = ₹3,60,000
```

**Step 3 — Unrealised profit on stock** (25% on cost → margin = 25/125 = 20% of price):
```
Stock in group = ₹1,00,000 → profit element = 1,00,000 × 25/125 = ₹20,000
```
This ₹20,000 is deducted from consolidated inventory *and* from the profit-maker (Parent), so from consolidated reserves.

**Step 4 — Consolidated reserves (owners of parent):**
```
Parent's own reserves            40,00,000
+ Parent's share of post-acq (80% × 3,00,000)   2,40,000
− Unrealised profit                   (20,000)
= Consolidated reserves          ₹42,20,000
```

**Step 5 — The elimination journals:**

| # | Entry | Dr (₹) | Cr (₹) |
|---|---|---|---|
| 1 | Share capital (Sub) | 10,00,000 | |
| | Reserves at acq (Sub) | 5,00,000 | |
| | Goodwill | 6,00,000 | |
| | To Investment in Sub | | 18,00,000 |
| | To NCI (20% × 15,00,000) | | 3,00,000 |
| 2 | Inter-co payable (Sub) | 1,50,000 | |
| | To Inter-co receivable (Parent) | | 1,50,000 |
| 3 | Sales | 2,00,000 | |
| | To COGS | | 2,00,000 |
| 4 | COGS (unrealised profit) | 20,000 | |
| | To Inventory | | 20,000 |

Post-acq NCI top-up: NCI is credited a further **20% × 3,00,000 = ₹60,000** (₹3,00,000 + ₹60,000 = **₹3,60,000**, matching Step 2).

**Proof:** goodwill ₹6,00,000 + consolidated reserves ₹42,20,000 + NCI ₹3,60,000 all tie back; the worksheet's Elim Dr = Elim Cr. That's a complete, reproducible consolidation you can rebuild in a fresh Excel tab in under 30 minutes.

## How it's tested

**Interview questions (conceptual):**
- "Why do we eliminate the investment against equity?" (Avoid double-counting — the investment *is* the net assets.)
- "Pre-acquisition vs post-acquisition profit — what's the accounting difference?" (Pre → goodwill/NCI; post → consolidated reserves.)
- "Goodwill formula? What if it's negative?" (Negative = capital reserve / bargain purchase, credited to P&L under Ind AS 103.)
- "How is NCI measured?" (Proportionate net assets, or fair value / full-goodwill method.)
- "What's unrealised profit and why remove it?"

**Practical tests companies give:**
- A **timed Excel case**: two trial balances + a fact sheet → build the consol worksheet and give goodwill, NCI, consolidated reserves in 45–60 min.
- A **"spot the missing elimination"** task: a consol that doesn't balance; find the un-cancelled inter-co entry.
- **PPA (purchase price allocation)** exercise for M&A roles: fair-value the net assets, then derive goodwill.

## Common mistakes & how pros avoid them

| Mistake | The fix |
|---|---|
| Using **whole** subsidiary equity for goodwill | Use only **parent's %** of net assets at acquisition |
| Netting goodwill against **year-end** reserves | Goodwill uses reserves **at the acquisition date** only |
| Forgetting the **post-acquisition NCI top-up** | NCI = NCI% × *reporting-date* net assets, not acquisition-date |
| Margin **on cost vs on sales** confusion | 25% on cost = 20% on price; use `markup/(1+markup)` |
| Consolidating a **≤50% associate** by adding lines | Associates use **equity method** (one-line), not full consolidation |
| Eliminations leaking into a single company's ledger | Eliminations live **only** in the consol worksheet — never posted to Tally of either entity |
| Consol worksheet doesn't balance | Add a **Elim Dr − Elim Cr = 0** check cell before you trust any number |

Pros keep a **one-line "why"** next to every elimination and a **reconciliation of NCI and goodwill** as a standing tab — auditors ask for exactly that.

## Learn-it roadmap & resources

**Time to proficiency:** ~2–3 weeks of focused practice if you already know basic financial statements.

| Week | Focus |
|---|---|
| 1 | AS 21 / Ind AS 110 concepts; goodwill & NCI by hand on paper |
| 2 | Build 3–4 consol worksheets in Excel from scratch (add inter-co, stock, dividends) |
| 3 | Add complications: mid-year acquisition, fair-value adjustments, associates (equity method) |

**Resources:**
- **ICAI** Ind AS 110 / AS 21 study material and illustrations (free, India-specific).
- CA Inter / CA Final **Advanced Accounting** consolidation chapters — the best structured drills for Indian candidates.
- IFRS Foundation's **IFRS 10 / IAS 28** basics for the global framing.
- Practice by taking any two public companies' standalone statements and attempting a mini-consol.
- **Certifications that signal this skill:** CA, ACCA (FR & SBR papers), CPA (FAR), CFA (Financial Reporting).

## Quick-reference

```
Consolidate when:  Control (usually >50% voting power)   → Ind AS 110 / AS 21 / IFRS 10
Associate (20–50%):  Equity method (one line), NOT full consol
```

| Item | Formula |
|---|---|
| **Goodwill** | Cost of investment − Parent% × Net assets **at acquisition** |
| **Negative goodwill** | Bargain purchase → Capital reserve / P&L (Ind AS 103) |
| **NCI (proportionate)** | NCI% × Net assets **at reporting date** |
| **Consolidated reserves** | Parent reserves + Parent% × post-acq profit − unrealised profit |
| **Unrealised profit (margin on sales)** | Intra-group stock × GP% |
| **Unrealised profit (markup on cost)** | Intra-group stock × markup/(1+markup) |

**The four eliminations:** (1) Investment ↔ Equity (birth of goodwill + NCI); (2) Inter-co debtor ↔ creditor; (3) Inter-co sales ↔ purchases; (4) Unrealised profit on stock.

**Golden checks:** Elim Dr = Elim Cr · Goodwill uses acquisition-date reserves · NCI uses reporting-date net assets · Eliminations never touch either company's own ledger.
