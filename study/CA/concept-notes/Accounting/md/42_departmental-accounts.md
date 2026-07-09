<!-- v2-deep -->

# Chapter 42 — Departmental Accounts

## 1. The Problem

Imagine you run a large store called **Modern Bazaar** on a single premises. Under one roof you sell three very different things: **Textiles** (cloth, garments), **Groceries** (rice, oil, spices), and **Electronics** (fans, mixers, small appliances). At the end of the year your accountant hands you a single Trading and Profit & Loss Account. It says:

> Net Profit for the year: ₹8,40,000.

You are pleased — until you start thinking like the BTech-MBA that you are. That single number is a *blended average*. It hides everything you actually need to know to run the business:

- Which of the three lines is the engine and which is the anchor dragging you down?
- Textiles occupies 60% of the floor space but maybe contributes only 20% of the profit. Should you shrink it?
- Groceries turns its stock over 12 times a year while Electronics turns it over twice. Are you tying up cash in the wrong place?
- The Electronics salesman earns a commission on his own sales — but you can only compute that fairly if you know **Electronics' own** profit, not the store's total.
- You want to give the grocery manager a bonus of *5% of the department's profit*. What number do you multiply by 5%?

A single combined P&L cannot answer a single one of these questions. The blended profit is **decision-useless** for a multi-line business. You are effectively flying three aeroplanes bolted together, watching one fuel gauge that averages all three tanks.

The core problem, then: **A business that runs several distinct activities under one legal entity needs to measure the profitability of each activity separately — but its transactions, its staff, its rent, its electricity, and its stock all get mixed together in one common set of books.** How do we un-mix them, fairly, so that each department gets credited with exactly the revenue and charged with exactly the costs it truly caused?

That is the entire subject of Departmental Accounts.

> A quick sibling comparison so you know the boundary. In the *next* chapter you meet **Branch Accounts**, where the business is split by **location** (Head Office in Mumbai, branch in Pune). Departmental accounts split by **activity within one location and one set of books**. Same instinct — "show me each unit's profit" — but branches are usually geographically separate and often keep their own books, whereas departments share one premises and one ledger. Keep this distinction; examiners love to test whether you can tell them apart.

**Why a mere ratio analysis of the combined figures will not do.** A student might object: "Why bother splitting the ledger at all? Just take the combined accounts and eyeball the ratios." But you *cannot* compute a departmental gross-profit ratio, a departmental stock-turnover, or a departmental net margin from a blended account — those inputs (that department's sales, that department's cost of goods sold, that department's closing stock) do not exist as separate line items in a combined Trading and P&L. Departmental accounting is precisely the machinery that *manufactures* those inputs. The analysis is downstream; the accounting is upstream and indispensable.

**Two purposes, one technique.** Notice that the chapter serves two masters at once. (i) A **management/decision** purpose — which line to grow, shrink, price, staff, reward. (ii) A **statutory/true-profit** purpose — when the departments sit inside one company, the *combined* figure that emerges after eliminating internal profit must be the true profit that faces the Balance Sheet. The elegance of the technique is that the same columnar exercise satisfies both. Examiners test both faces: some questions ask only for "departmental net profit" (management face); others push through to "the profit to be carried to the Balance Sheet after stock reserve" (statutory face). Always read *which* number the question actually wants.

---

## 2. The Core Idea (Analogy)

Think of the combined store as an **apartment building with shared utilities**, and each department as a **flat**.

Some bills belong cleanly to one flat. Flat 2 ran its own air-conditioner on its own sub-meter — that electricity is *directly* Flat 2's. No argument, no arithmetic. In accounting language this is **allocation**: a cost that is *wholly identifiable* with one department is simply *charged directly* to it.

But the building also has shared costs: the lift, the security guard, the water tank, the exterior paint. No flat "owns" these, yet all flats consume them. You cannot ignore them — they are real costs of living there. So you invent a **fair sharing rule**. The lift and paint (building-related) get split by **floor area**; the water bill gets split by **number of occupants**; the security guard's cost by… well, everyone benefits roughly equally, maybe split by area again. In accounting language this is **apportionment**: a *common* cost is *divided among* departments on a *logical basis that reflects who caused or benefited from it*.

The whole art of departmental accounting is exactly this: for every rupee of cost and every rupee of revenue, ask one question — **"Can I point directly at one department, or must I share it?"** If you can point, you *allocate*. If you must share, you *apportion* on the most cause-and-effect basis you can defend.

One more piece of the analogy, for the trickiest part of the chapter. Suppose Flat 1 (a bakery) sells bread to Flat 2 (a café) at a marked-up price. On the *building's* combined accounts, that "sale" is not a real sale to the outside world — it's money moving from one pocket to another. If the café hasn't yet sold that bread to a real customer, the bakery's "profit" on it is **imaginary from the building's point of view**. We must strip it out. This is **inter-departmental transfer** and **unrealised profit elimination** — Section 4.4 and 5's Example 3 make it concrete.

**A third layer to the analogy — the "residual" bills.** Some building costs refuse to attach to any flat even by a sharing rule: the interest on the loan the *building society* took to construct the parking lot, the penalty the *society* paid for a filing default, the dividend the society received on its reserve fund parked in a mutual fund. These are the society's, not any flat's, and no floor-area or headcount rule makes them a flat's cost. They live in a **common pool** — the accounting equivalent is the **General Profit & Loss Account** (Section 4.5). So the analogy gives you all three homes a rupee can find: *this flat* (allocate), *shared among flats* (apportion), *the society's own* (General P&L). Every item in every departmental problem lands in exactly one of these three.

---

## 3. Why It's Built This Way

Why not just keep three completely separate businesses with three separate ledgers? Because that throws away the whole *point* of running them together. The departments genuinely **share** resources — one rent, one manager, one electricity connection, one set of administrative staff — and sharing those resources is *why* the combined business is cheaper to run than three standalone shops. So the books *must* be combined at the base level. The departmental split is a **reporting overlay** on top of a shared ledger, not three separate ledgers.

Why insist on *logical* apportionment bases rather than just splitting everything equally, or by sales? Because an arbitrary base produces a **misleading** departmental profit, and a misleading number is worse than no number — it drives wrong decisions. If you apportion rent equally across three departments when Textiles occupies 60% of the floor, you *flatter* Textiles and *punish* the small departments, and you might close a perfectly good department on the strength of a bad allocation. The principle is **cause and effect**: charge each department the cost *in proportion to the factor that drives that cost*. Rent is driven by space → apportion by **floor area**. Lighting by space or by points → **area** or **light-points**. Labour welfare by headcount → **number of employees**. Carriage inward by purchases → **purchase values**. Depreciation by asset value in each department → **asset values**.

Why eliminate unrealised profit on inter-departmental transfers? Because of the **prudence** and **realisation** concepts that run through all of accounting (and through AS 2 *Valuation of Inventories*). Profit is earned only when goods are sold to an **outside** party. If Department A "sells" to Department B at a profit, and B still holds those goods in closing stock, then from the *whole entity's* standpoint nothing has been sold to anyone outside — no profit has been realised. If you left A's mark-up inside B's closing stock, you would (a) overstate the entity's total profit and (b) overstate the value of an asset (stock) above cost, which AS 2 forbids (inventory is carried at *cost or net realisable value, whichever is lower* — never above cost). So a **stock reserve** is created to knock the unrealised profit back out.

Why does this matter beyond bookkeeping tidiness? Because the *combined* net profit that flows into the company's Balance Sheet must be **true**. Departmental accounting is not just a management convenience; when the departments belong to one company, the final combined figure hits the statutory financial statements, and that figure must obey the same AS and Companies Act discipline as any other. So the reasoning is not academic — get the unrealised profit wrong and your Balance Sheet is wrong.

**Why keep the departmental gross profit even for a "loss" department?** A subtle first-principles point examiners probe indirectly. A department can show a *positive gross profit but a negative net profit* after it absorbs its share of common overheads. The naive reaction — "close it" — is often wrong. If the department is covering its **own** direct costs and making a *contribution* toward the shared overheads, then closing it does not make those shared overheads disappear; the rent, the manager, the lighting continue and simply re-distribute onto the surviving departments, possibly pushing *them* into loss. This is the contribution-vs-absorption insight from Cost Accounting appearing inside financial accounting. Departmental accounts, by *separating* the direct-cost tier (Trading) from the shared-overhead tier (P&L), let you see this. That is *why* the two-tier structure exists and is not collapsed into one step: the split of "costs the department caused alone" from "costs it merely shares" is itself decision-information.

**Why apportion at all rather than just report gross profit per department and stop?** Because gross profit per department flatters the space-hungry, staff-heavy department. A department can post the biggest gross profit yet be the worst *net* performer once it is charged the rent for the 60% of the floor it occupies and the wages of the 20 staff it employs. The apportionment tier is where the department finally "pays its rent." Skipping it gives management a systematically biased ranking. So apportionment is not busywork — it is the step that makes the comparison *fair*.

---

## 4. Full Technical Content

### 4.1 The two-tier structure of a departmental account

A departmental set of final accounts has three tiers:

1. **Departmental Trading Account** — one column per department, computing **Gross Profit** for each. Everything here is either directly departmental or apportioned on a trading-related basis.
2. **Departmental Profit & Loss Account** — one column per department, taking each department's gross profit down to **Departmental Net Profit** after charging apportioned operating expenses.
3. **General Profit & Loss Account** — a *single* combined column (no departmental split) where truly **non-departmental** items sit: items that cannot sensibly be linked to any department by any cause-and-effect base. Examples: interest on loans/debentures, income tax, dividends received, general managerial salary of the whole entity, share transfer fees, profit/loss on sale of investments, and the **net stock reserve adjustment** on unrealised profit.

*Figure 4.1 — how a rupee of cost finds its home.*

```mermaid
flowchart TD
    A["A cost or income arises"] --> B{"Identifiable wholly with one department"}
    B -->|"Yes"| C["ALLOCATE - charge directly to that department"]
    B -->|"No"| D{"Can it be shared on a logical cause-effect basis"}
    D -->|"Yes"| E["APPORTION across departments on that basis"]
    D -->|"No"| F["Leave in General P&L - not departmentalised"]
    C --> G["Departmental Trading or P&L column"]
    E --> G
    F --> H["General P&L single column"]
```

*A cost is allocated if you can point at one department, apportioned if you must share it, and parked in the General P&L only if no logical base exists.*

**Which tier does an expense belong to — Trading or P&L?** A second sorting question sits underneath the first. Once you know a cost is *departmental*, you must decide whether it enters the **Trading** account (above gross profit) or the **P&L** account (below it). The rule mirrors ordinary final accounts: costs of *bringing goods to saleable condition/location* — purchases, direct wages, carriage inward, manufacturing/conversion expenses, factory power — go **above the line** (Trading); costs of *running and selling* — rent of showroom, salaries, selling expenses, depreciation, discount — go **below the line** (P&L). Placement matters because gross profit itself is a reported figure and because manager's commission or a transfer price is sometimes defined as a percentage *of gross profit* or *of sales*, so a mis-placed carriage-inward silently corrupts a downstream calculation.

### 4.2 Allocation vs Apportionment — the precise distinction

| Feature | **Allocation** | **Apportionment** |
|---|---|---|
| Nature of cost | Directly attributable to ONE department | Common / shared across departments |
| Method | Charged in full to that department | Split using a ratio (the "basis") |
| Judgement involved | None — it's a fact | Yes — choose the fairest basis |
| Example | Salesmen's salary of the Electronics counter; direct purchases of Groceries | Building rent, common lighting, general manager's salary |

Mnemonic to reason (not memorise): **Allocation = "Assign it, it's theirs." Apportionment = "Apportion it, it's shared."**

**The three-way test, stated crisply.** Every rupee faces two yes/no gates in order:
1. *Is it wholly one department's?* → **Allocate** (stop).
2. If not, *is there a defensible cause-effect base?* → **Apportion** (stop).
3. If neither → **General P&L** (park it).

Do the gates *in this order*. Students who jump to gate 2 sometimes apportion a cost that was actually allocable (e.g. splitting "salesmen's salaries" on sales when the question already gave the salary of *each department's own* counter staff — those are allocations, not apportionments).

### 4.3 The standard apportionment bases (and the logic of each)

You should never memorise this table cold — you should be able to *derive* each row by asking "what drives this cost?" But here is the exam-standard set, with the driving logic:

| Expense | Usual basis of apportionment | Driving logic ("what causes it") |
|---|---|---|
| Rent, rates, taxes, building repairs, building insurance | **Floor area** (or space occupied) | Cost is driven by space consumed |
| Lighting & heating | **Floor area** or number of **light/power points** | Driven by space or by points used |
| Selling expenses, discount allowed, bad debts, salesmen's commission, freight **outward**, after-sale service | **Net sales** of each department | Driven by how much each dept sells |
| Carriage / freight **inward** | **Purchases** of each department | Driven by how much each dept buys |
| Depreciation, repairs & insurance of plant/machinery/assets | **Value of assets** in each dept | Driven by asset value held |
| Works manager's / supervisor's salary | **Time devoted** to each dept (or wages, or output) | Driven by supervisory time |
| Labour welfare, canteen, ESI, PF, staff welfare | **Number of employees** in each dept | Driven by headcount |
| Power / fuel | **Horse-power × hours**, or machine hours | Driven by machine usage |
| Discount received | **Purchases** of each department | Driven by purchase value |
| Insurance of **stock** | **Average stock** or purchases | Driven by stock value carried |

> **Watch the direction.** Carriage *inward* follows **purchases**; carriage/freight *outward* (a selling cost) follows **sales**. Students routinely apportion both by sales — that is wrong and a favourite trap (Section 8).

**When the question gives you a base directly, use it — do not "improve" on it.** If the problem says "apportion rent in the ratio 3:2:1" or "office expenses to be divided by sales," follow the instruction even if you personally think another base is more logical. The examiner is testing obedience to the data, not your creativity. Your derivation skill is for the cases where *no* base is stated and you must pick the cause-effect one.

**Choosing between two defensible bases.** Some costs admit more than one reasonable base (lighting: floor area *or* light points; supervisor salary: time *or* wages *or* output). The tie-breaker hierarchy is: (1) use whatever the question supplies data for — if it gives light *points*, it wants light points; (2) if it gives data for several, use the one most *directly* causal; (3) state your chosen base in a working note so the examiner can follow your logic and award method marks even if the "expected" base differed.

**Bases that are subtly wrong even though they look reasonable:**
- Apportioning **all** salaries by employee count when some staff are clearly a single department's (allocate those first, apportion only the genuinely shared remainder).
- Apportioning **rent** by sales "because bigger departments sell more" — rent is driven by *space*, not turnover; a high-turnover jewellery counter may occupy tiny space.
- Apportioning **advertising** by floor area — advertising drives, and is driven by, *sales*, not space (unless the ad is a shared signboard, which some questions specify by area — read carefully).

### 4.4 Inter-departmental transfers

Departments often supply each other. A **furniture** department may draw timber from a **timber** department; a **restaurant** may take provisions from a **grocery** department. Two questions arise:

**(a) At what price is the transfer recorded?** Either at **cost** or at a **transfer price** (cost + a loading/mark-up, sometimes called "cost plus" or "at selling price"). The exam tells you which.

**(b) How is it recorded?** The transferring department credits its Trading Account (like a sale to another dept) and the receiving department debits its Trading Account (like a purchase). To keep the *combined* accounts honest, these transfers are shown as separate lines — "Transfer to Dept Y" (a credit in X's Trading) and "Transfer from Dept X" (a debit in Y's Trading) — and they **cancel out** in the combined total, so the entity's total purchases and sales are not inflated.

**(c) Unrealised profit.** If the transfer was at a price **above cost**, and the receiving department still holds some of those goods in **closing stock**, then the mark-up sitting inside that closing stock is **unrealised** from the entity's viewpoint. We remove it by creating a **Stock Reserve**.

**Formula for unrealised profit in closing stock:**

$$\text{Unrealised profit} = \text{Closing stock arising from transfer} \times \frac{\text{Profit loading}}{\text{Transfer price (or cost, as given)}}$$

Be careful which fraction the question implies:
- If goods are transferred at **cost + 25% (i.e. 25% on cost)**, then in a transfer price of ₹125, profit = ₹25, so unrealised profit = closing-transfer-stock × **25/125**.
- If goods are transferred at a price that yields **25% on selling price**, then unrealised profit = closing-transfer-stock × **25/100**.

**Journal entries for the stock reserve (unrealised profit):**

For the **closing** unrealised profit (created at year-end):

| Particulars | Dr (₹) | Cr (₹) |
|---|---|---|
| General Profit & Loss A/c ......... Dr | XXX | |
| &nbsp;&nbsp;&nbsp;To Stock Reserve A/c | | XXX |
| *(Being unrealised profit in closing stock on inter-departmental transfer eliminated)* | | |

The Stock Reserve is then **deducted from the value of closing stock** in the Balance Sheet (stock is shown net of the reserve, i.e. at cost).

For the **opening** unrealised profit (which was created last year and is now realised because last year's stock has since been sold), we **reverse** it:

| Particulars | Dr (₹) | Cr (₹) |
|---|---|---|
| Stock Reserve A/c ......... Dr | XXX | |
| &nbsp;&nbsp;&nbsp;To General Profit & Loss A/c | | XXX |
| *(Being opening stock reserve written back as the profit is now realised)* | | |

**Net effect on General P&L** = Opening stock reserve (credit) − Closing stock reserve (debit). Only the *net* movement hits the combined profit — this is why the stock reserve adjustment lives in the **General** P&L, not in any single department's column (it concerns transfers *between* departments, so it belongs to no one department alone).

*Figure 4.2 — the life of unrealised profit on an inter-departmental transfer.*

```mermaid
flowchart LR
    A["Dept X transfers goods to Dept Y at cost plus markup"] --> B["Y records as purchase - X records as transfer out"]
    B --> C{"Any transferred goods left in Y closing stock"}
    C -->|"No - all sold outside"| D["Profit fully realised - no reserve needed"]
    C -->|"Yes"| E["Markup inside that stock is unrealised"]
    E --> F["Create Stock Reserve - Debit General P&L"]
    F --> G["Show closing stock net of reserve in Balance Sheet"]
    G --> H["Next year that stock is sold - reverse the reserve back to profit"]
```

*Unrealised profit is only the mark-up trapped inside unsold transferred stock; it is reserved this year and released next year.*

**Transfer at cost — no reserve, but transfers still cancel.** A common exam simplification: goods are moved between departments **at cost**. Then there is *no* mark-up, so *no* unrealised profit and *no* stock reserve — but you must still show the transfer as a credit in the giver's Trading and a debit in the receiver's Trading and cancel it in the Total column. Students sometimes assume "transfer ⇒ reserve" reflexively and invent a reserve that does not exist. The reserve exists **only** when transfer price exceeds cost **and** transferred goods remain unsold at year-end.

**Deriving how much transferred stock is left when the question does not tell you.** Sometimes the problem does not state "of the closing stock, ₹X is transferred goods." Instead it says the receiving department made *no* outside purchases of that item, so *all* its stock of that item is transferred stock; or it gives the proportion of the year's transfers still unsold. Read for these clues. If the receiving department both purchased outside *and* received transfers of the same goods and the split is unstated, the question is usually solvable only if it gives you enough to isolate the transfer portion — do not fabricate a split.

**Two-way transfers.** Occasionally each department transfers to the other (X → Y *and* Y → X), each at its own mark-up. Then you compute **two** stock reserves — one for the mark-up X trapped in Y's closing stock, one for the mark-up Y trapped in X's closing stock — and both hit the *net* stock-reserve line in the General P&L. The logic is unchanged; you just do it twice. Watch that you use *each* transferring department's *own* mark-up fraction.

### 4.4A Inter-departmental transfer of a *service* or *fixed asset*

A finer distinction the examiner can spring. Not all inter-departmental transfers are of *trading goods*:

- **Transfer of a fixed asset** made by one department for another (e.g. the Furniture department builds shelving used by the Grocery department). Here the "unrealised profit" is trapped not in *stock* but in the *fixed asset's* carrying value, and it should be eliminated so the asset is carried at cost to the entity; the associated depreciation must also be corrected. This is rarer at Intermediate level but appears in tweaked problems — the principle (strip internal mark-up so the asset is at entity cost) is identical to the stock-reserve principle.
- **Transfer of a service** (repairs department serving other departments) is normally charged at cost via apportionment (time/hours), and no reserve arises because a service is consumed as rendered, not stored.

Flag: the *depreciation-on-internal-asset* correction is examinable but treatment specifics can vary — **verify against current ICAI study material** before writing an internal-asset-transfer answer in the exam.

### 4.5 Items that are NEVER apportioned (stay in General P&L)

Because there is no cause-and-effect link to any department: interest on loan/debentures, income tax, transfer to general reserve, dividend paid, profit/loss on sale of investments or fixed assets, share issue expenses, and the net inter-departmental stock reserve. Also, the **general manager's salary** is often left in General P&L unless the question gives a basis (time devoted) to apportion it.

**A useful test for "does it belong in General P&L?"** Ask: *would this item still exist, unchanged, if the business had only one department?* Interest on the company's loan, income tax on the company's profit, dividend to the company's shareholders, loss on sale of the company's investment — all would exist identically with a single department, because they attach to the *entity's financing and ownership*, not its trading activities. Such items have no departmental "cause," so they cannot be apportioned by any honest base and default to the General P&L.

**Interest — the exception that proves the rule.** If a question says "interest is charged on capital *invested in each department*" or "notional interest on departmental stock," then interest *does* have a departmental base (the capital/stock employed in each department) and is apportioned accordingly. So the rule is not "interest is always general" — it is "interest is general *unless the question supplies a departmental base for it*." This is a favourite discriminator between average and top scripts.

### 4.6 Manager's / departmental commission

A department manager is often paid a commission of *x*% of "profit." This introduces a small algebra step and a big reading-comprehension trap:

- **On profit *before* charging his commission** — straightforward: commission = *x*% × (that department's net profit before commission).
- **On profit *after* charging his commission** — circular; solve: if commission = *x*% of profit *after* commission, then commission = profit-before × *x* / (100 + *x*). (Same structure as the "25/125" reserve fraction — a percentage *on the post-charge base* becomes *x*/(100+*x*) of the pre-charge base.)

Always state clearly whether commission is on gross profit, net profit, before or after commission, and *whose* profit (that department's, or the combined). Charge a departmental manager's commission in **that department's** P&L (it is caused by that department); charge a general manager's commission on *total* profit in the **General** P&L. Worked in Example 4.

### 4.7 The columnar mechanics and the Total column

The Total column is not decoration — it is your **self-check**. Because it is the sum of the departmental columns, and because inter-departmental transfers are equal-and-opposite, the Total column must reproduce exactly the figures a *single combined* Trading and P&L would show (transfers vanishing). If your Total column does not equal the standalone combined account, something is mis-apportioned or a transfer failed to cancel. Build the habit: foot each departmental column, then foot the Total column, then confirm the Total column reconciles to the combined figures the question implies.

### 4.8 Basis data that must be *derived* before use

Apportionment ratios are sometimes hidden one step back. The question gives raw data from which you first compute the ratio:
- "Floor area" may be given as length × breadth per department — compute the areas first.
- "Sales" for the selling-cost base means **net sales** (after returns), and it means sales **to outsiders** — *exclude* inter-departmental transfers from the selling-expense base unless told otherwise (selling *effort* was not spent on internal transfers).
- "Average stock" = (opening + closing)/2 per department.
- "Wages" as a base means the *direct* wages allocated to each department.

Reading the base correctly is worth as much as the apportionment arithmetic itself.

---

## 5. Worked Examples

### Example 1 — Warm-up: pure allocation vs apportionment (two departments)

**Facts.** M/s Sharma Traders has two departments, **A** and **B**. For the year ended 31 March 2026:

| Item | Dept A (₹) | Dept B (₹) |
|---|---|---|
| Opening stock | 40,000 | 20,000 |
| Purchases | 3,00,000 | 1,80,000 |
| Sales | 4,60,000 | 3,10,000 |
| Closing stock | 50,000 | 30,000 |

Common expenses to apportion: **Rent ₹48,000** (Dept A occupies 3,000 sq ft, Dept B occupies 1,000 sq ft). **Salaries ₹36,000** (10 employees in A, 8 in B). Direct wages allocated: A ₹22,000, B ₹15,000. Advertisement ₹15,400 to be apportioned on sales.

**Step 1 — Work out the apportionment ratios (with logic).**
- Rent → **floor area** 3,000 : 1,000 = **3 : 1**. So A = 48,000 × 3/4 = ₹36,000; B = ₹12,000.
- Salaries → **number of employees** 10 : 8 = **5 : 4**. A = 36,000 × 5/9 = ₹20,000; B = ₹16,000.
- Advertisement → **sales** 4,60,000 : 3,10,000 = **46 : 31** (total 77). A = 15,400 × 46/77 = ₹9,200; B = 15,400 × 31/77 = ₹6,200.

**Step 2 — Departmental Trading Account.**

| Particulars | Dept A (₹) | Dept B (₹) | Particulars | Dept A (₹) | Dept B (₹) |
|---|---|---|---|---|---|
| To Opening stock | 40,000 | 20,000 | By Sales | 4,60,000 | 3,10,000 |
| To Purchases | 3,00,000 | 1,80,000 | By Closing stock | 50,000 | 30,000 |
| To Direct wages | 22,000 | 15,000 | | | |
| To Gross profit c/d | 1,48,000 | 1,25,000 | | | |
| **Total** | **5,10,000** | **3,40,000** | **Total** | **5,10,000** | **3,40,000** |

Check A: 40,000 + 3,00,000 + 22,000 = 3,62,000 debit before GP; credit side 4,60,000 + 50,000 = 5,10,000; GP = 5,10,000 − 3,62,000 = **1,48,000**. ✓
Check B: 20,000 + 1,80,000 + 15,000 = 2,15,000; credit 3,40,000; GP = **1,25,000**. ✓

**Step 3 — Departmental Profit & Loss Account.**

| Particulars | Dept A (₹) | Dept B (₹) | Particulars | Dept A (₹) | Dept B (₹) |
|---|---|---|---|---|---|
| To Rent | 36,000 | 12,000 | By Gross profit b/d | 1,48,000 | 1,25,000 |
| To Salaries | 20,000 | 16,000 | | | |
| To Advertisement | 9,200 | 6,200 | | | |
| To Net profit | 82,800 | 90,800 | | | |
| **Total** | **1,48,000** | **1,25,000** | **Total** | **1,48,000** | **1,25,000** |

**Insight the single P&L would have hidden.** Combined net profit = ₹1,73,600. But Dept **B**, with *lower* sales (₹3,10,000 vs ₹4,60,000), earns *more* net profit (₹90,800 vs ₹82,800). B is the more efficient department. That is precisely the decision-useful fact departmental accounting exists to reveal.

**Examiner tweak — "what if rent were split equally?"** Suppose a careless accountant splits the ₹48,000 rent 50:50 (₹24,000 each). Then A's net profit rises to ₹94,800 and B's falls to ₹78,800 — *reversing* the ranking. This is not a rounding difference; it flips the entire management conclusion about which department is stronger. It is the single cleanest demonstration of why the *basis* matters more than the arithmetic, and why "equal split" is a trap (Section 8.8).

---

### Example 2 — Deriving the apportionment ratios yourself (three departments)

**Facts.** Bright Stores has three departments — **X, Y, Z**. Trading results already give gross profits: X ₹2,10,000, Y ₹1,60,000, Z ₹1,30,000. Now apportion the following common expenses and find departmental net profit.

| Common expense | Amount (₹) | Given data |
|---|---|---|
| Rent & rates | 90,000 | Floor area X 4,000, Y 3,000, Z 2,000 sq ft |
| Lighting | 18,000 | Light points X 30, Y 24, Z 18 |
| Selling expenses | 66,000 | Sales X 8,00,000, Y 6,00,000, Z 4,00,000 |
| Carriage inward | 24,000 | Purchases X 5,00,000, Y 4,00,000, Z 3,00,000 |
| Depreciation | 21,000 | Asset value X 3,00,000, Y 2,50,000, Z 2,00,000 |
| Labour welfare | 12,000 | Employees X 20, Y 16, Z 12 |

**Step 1 — Choose the base for each (reason it out).**

| Expense | Base chosen | Ratio | Total parts |
|---|---|---|---|
| Rent & rates | Floor area | 4,000 : 3,000 : 2,000 = 4 : 3 : 2 | 9 |
| Lighting | Light points | 30 : 24 : 18 = 5 : 4 : 3 | 12 |
| Selling expenses | Sales | 8 : 6 : 4 = 4 : 3 : 2 | 9 |
| Carriage **inward** | Purchases | 5 : 4 : 3 | 12 |
| Depreciation | Asset value | 3,00,000 : 2,50,000 : 2,00,000 = 6 : 5 : 4 | 15 |
| Labour welfare | Employees | 20 : 16 : 12 = 5 : 4 : 3 | 12 |

**Step 2 — Apportion.**

| Expense | X (₹) | Y (₹) | Z (₹) | Total |
|---|---|---|---|---|
| Rent & rates (4:3:2) | 40,000 | 30,000 | 20,000 | 90,000 |
| Lighting (5:4:3) | 7,500 | 6,000 | 4,500 | 18,000 |
| Selling expenses (4:3:2) | 29,333 | 22,000 | 14,667 | 66,000 |
| Carriage inward (5:4:3) | 10,000 | 8,000 | 6,000 | 24,000 |
| Depreciation (6:5:4) | 8,400 | 7,000 | 5,600 | 21,000 |
| Labour welfare (5:4:3) | 5,000 | 4,000 | 3,000 | 12,000 |
| **Total expenses** | **1,00,233** | **77,000** | **53,767** | **2,31,000** |

*(Selling expenses: 66,000 × 4/9 = 29,333.33 → ₹29,333; × 3/9 = 22,000; × 2/9 = 14,666.67 → ₹14,667. Rounded to reconcile to 66,000.)*

**Step 3 — Departmental net profit.**

| | X (₹) | Y (₹) | Z (₹) | Total |
|---|---|---|---|---|
| Gross profit | 2,10,000 | 1,60,000 | 1,30,000 | 5,00,000 |
| Less: expenses | 1,00,233 | 77,000 | 53,767 | 2,31,000 |
| **Net profit** | **1,09,767** | **83,000** | **76,233** | **2,69,000** |

Combined net profit ₹2,69,000. Notice Z, the smallest by sales, still returns a healthy ₹76,233 — because it carries the *lowest* share of every common cost. Rank by *net margin* and you get a different story from ranking by sales. Decision-useful.

---

### Example 3 — Exam-hard: inter-departmental transfer + unrealised profit + full final accounts

This is the flagship problem type. Read every working note.

**Facts.** ABC Manufacturing Ltd has two departments: **Cloth (C)** and **Readymade Garments (G)**. The garments department makes garments *out of cloth supplied by the Cloth department*. For the year ended 31 March 2026:

| Particulars | Cloth Dept (₹) | Garments Dept (₹) |
|---|---|---|
| Opening stock (1 Apr 2025) | 3,00,000 | 50,000 |
| Purchases (from outside) | 20,00,000 | 15,000 |
| Sales (to outside) | 22,00,000 | 8,00,000 |
| **Transfer of cloth to Garments dept** | 3,00,000 | — |
| Manufacturing expenses (direct) | — | 3,60,000 |
| Selling expenses (direct) | 20,000 | 6,000 |
| Closing stock (31 Mar 2026) | 2,00,000 | 2,00,000 |

**Additional information:**
1. The Cloth department transfers cloth to the Garments department **at its usual selling price**, which includes a profit of **25% on cost** (i.e. cost + 25%).
2. The Garments department's **closing stock of ₹2,00,000 includes cloth (at transfer price) of ₹1,20,000**; the balance ₹80,000 is other conversion cost / outside purchases.
3. The Garments department's **opening stock of ₹50,000 included cloth (at transfer price) of ₹25,000**.
4. General expenses (not departmental): office salaries ₹90,000, general manager's salary ₹60,000. These are to be apportioned between the two departments in the ratio of their **net sales to outsiders** — *except* that the question says to charge them to a combined General P&L. (We will show both the departmental split and, per the requirement, run general items through General P&L. For clarity we apportion office salaries by sales and keep the stock-reserve adjustment in General P&L.)

To keep the illustration clean and unambiguous, we adopt this treatment (standard ICAI approach):
- Office salaries ₹90,000 → apportioned to departments on **sales to outsiders** (22,00,000 : 8,00,000 = 11 : 4).
- General manager's salary ₹60,000 and the **net stock reserve** → **General P&L** (non-departmental).

**Step 1 — Departmental Trading Account (compute gross profit).**

Note the transfer: it is a **credit** in Cloth's Trading (like a sale) and a **debit** in Garments' Trading (like a purchase).

| Particulars | Cloth (₹) | Garments (₹) | Particulars | Cloth (₹) | Garments (₹) |
|---|---|---|---|---|---|
| To Opening stock | 3,00,000 | 50,000 | By Sales | 22,00,000 | 8,00,000 |
| To Purchases | 20,00,000 | 15,000 | By Transfer to Garments | 3,00,000 | — |
| To Transfer from Cloth | — | 3,00,000 | By Closing stock | 2,00,000 | 2,00,000 |
| To Manufacturing exp. | — | 3,60,000 | | | |
| To Gross profit c/d | 4,00,000 | 2,75,000 | | | |
| **Total** | **27,00,000** | **10,00,000** | **Total** | **27,00,000** | **10,00,000** |

*Cloth check:* Debit before GP = 3,00,000 + 20,00,000 = 23,00,000. Credit = 22,00,000 + 3,00,000 + 2,00,000 = 27,00,000. GP = 27,00,000 − 23,00,000 = **4,00,000**. ✓
*Garments check:* Debit before GP = 50,000 + 15,000 + 3,00,000 + 3,60,000 = 7,25,000. Credit = 8,00,000 + 2,00,000 = 10,00,000. GP = 10,00,000 − 7,25,000 = **2,75,000**. ✓

**Step 2 — Departmental Profit & Loss Account.**

Office salaries ₹90,000 in ratio 11 : 4 → Cloth = 90,000 × 11/15 = ₹66,000; Garments = ₹24,000.

| Particulars | Cloth (₹) | Garments (₹) | Particulars | Cloth (₹) | Garments (₹) |
|---|---|---|---|---|---|
| To Selling expenses | 20,000 | 6,000 | By Gross profit b/d | 4,00,000 | 2,75,000 |
| To Office salaries | 66,000 | 24,000 | | | |
| To Net profit c/d | 3,14,000 | 2,45,000 | | | |
| **Total** | **4,00,000** | **2,75,000** | **Total** | **4,00,000** | **2,75,000** |

Departmental net profit (before general items) = Cloth ₹3,14,000 + Garments ₹2,45,000 = **₹5,59,000**.

**Step 3 — Unrealised profit on inter-departmental transfer (the crux).**

Cloth transfers at **cost + 25%**, so profit is **25/125 = 1/5** of the transfer price.

*Closing stock* of Garments contains transferred cloth of **₹1,20,000** (at transfer price).
Unrealised profit in closing stock = 1,20,000 × 25/125 = **₹24,000** → create **Stock Reserve (closing) = ₹24,000** (debit General P&L).

*Opening stock* of Garments contained transferred cloth of **₹25,000** (at transfer price).
Unrealised profit in opening stock = 25,000 × 25/125 = **₹5,000** → this reserve was created last year; reverse it now (credit General P&L).

**Net stock reserve charge to General P&L = closing 24,000 − opening 5,000 = ₹19,000 (net debit).**

**Journal entries:**

| Particulars | Dr (₹) | Cr (₹) |
|---|---|---|
| Stock Reserve A/c (opening) ......... Dr | 5,000 | |
| &nbsp;&nbsp;&nbsp;To General P&L A/c | | 5,000 |
| *(Opening unrealised profit now realised)* | | |
| General P&L A/c ......... Dr | 24,000 | |
| &nbsp;&nbsp;&nbsp;To Stock Reserve A/c (closing) | | 24,000 |
| *(Unrealised profit in closing stock eliminated)* | | |

**Step 4 — General Profit & Loss Account.**

| Particulars | ₹ | Particulars | ₹ |
|---|---|---|---|
| To General manager's salary | 60,000 | By Net profit b/d (Cloth) | 3,14,000 |
| To Stock reserve (closing) | 24,000 | By Net profit b/d (Garments) | 2,45,000 |
| To Net profit transferred to B/S | 4,80,000 | By Stock reserve (opening) w/back | 5,000 |
| **Total** | **5,64,000** | **Total** | **5,64,000** |

**Combined net profit for the year = ₹4,80,000.**

*Reconciliation:* 5,59,000 (dept net profit) − 60,000 (GM salary) − 24,000 (closing reserve) + 5,000 (opening reserve) = **4,80,000**. ✓

**Step 5 — Balance Sheet effect of the stock reserve.** In the Balance Sheet, closing stock is shown **net of the closing stock reserve**:

Total closing stock = Cloth 2,00,000 + Garments 2,00,000 = 4,00,000. *Less* Stock Reserve 24,000 = **₹3,76,000** carried to the Balance Sheet (this restores the transferred portion to cost, satisfying AS 2).

**Why this matters:** had we ignored the reserve, the entity's profit would be overstated by the *net* ₹19,000 and its stock asset overstated by ₹24,000 above cost. Departmental accounting forces both errors out.

**Examiner tweak — "transfer at 25% on selling price instead of on cost."** If Additional info (1) instead read "profit of 25% *on selling price*," the fraction becomes **25/100 = 1/4**, not 25/125. Then closing reserve = 1,20,000 × 1/4 = **₹30,000** and opening reserve = 25,000 × 1/4 = **₹6,250**; net charge = ₹23,750; combined profit = 5,59,000 − 60,000 − 30,000 + 6,250 = **₹4,75,250**; Balance-Sheet stock = 4,00,000 − 30,000 = ₹3,70,000. Everything downstream shifts. This single-word change ("on cost" vs "on sale price") is the most-tested lever in the whole chapter — always underline it before you compute.

---

### Example 4 — Manager's commission on departmental profit (before vs after)

**Facts.** Konark Retail has two departments, **P** and **Q**. After apportioning all common expenses, the departmental net profits *before manager's commission* are: P ₹4,00,000, Q ₹3,30,000. Each department's manager is entitled to a commission of **10% of the net profit of his own department**. The general manager gets **5% of the combined net profit** (of both departments, after departmental managers' commission). Required: net profit finally carried to the Balance Sheet under two independent assumptions —
(a) departmental commission is **10% of profit *before* charging such commission**;
(b) departmental commission is **10% of profit *after* charging such commission**.

**Assumption (a) — commission on profit *before* commission.**

| | Dept P (₹) | Dept Q (₹) |
|---|---|---|
| Profit before commission | 4,00,000 | 3,30,000 |
| Manager's commission = 10% × profit | 40,000 | 33,000 |
| **Profit after departmental commission** | **3,60,000** | **2,97,000** |

Combined after departmental commission = 3,60,000 + 2,97,000 = ₹6,57,000.
General manager's commission = 5% × 6,57,000 = ₹32,850.
**Net profit to Balance Sheet = 6,57,000 − 32,850 = ₹6,24,150.**

**Assumption (b) — commission on profit *after* commission.**

Commission = profit-before × 10/(100+10) = profit-before × 10/110 = 1/11 of profit-before.

| | Dept P (₹) | Dept Q (₹) |
|---|---|---|
| Profit before commission | 4,00,000 | 3,30,000 |
| Commission = 1/11 × profit-before | 36,364 | 30,000 |
| **Profit after departmental commission** | **3,63,636** | **3,00,000** |

*Verify (b):* P's commission ₹36,364 should be 10% of P's profit *after* commission = 10% × 3,63,636 = ₹36,364. ✓ (Q: 10% × 3,00,000 = ₹30,000. ✓)

Combined after departmental commission = 3,63,636 + 3,00,000 = ₹6,63,636.
General manager's commission = 5% × 6,63,636 = ₹33,182.
**Net profit to Balance Sheet = 6,63,636 − 33,182 = ₹6,30,454.**

**Takeaway.** The *before/after* wording moved the final profit by nearly ₹6,300 here. The departmental commission belongs in each **department's** P&L (it is caused by that department); the general manager's commission belongs in the **General** P&L (it is on combined profit). Mis-placing the general manager's commission into a departmental column understates one department and is a common slip.

---

### Example 5 — Transfer at cost (no reserve) plus a loss-making department decision

**Facts.** Sunrise Stores runs **Hardware (H)** and **Paints (Pt)**. Paints draws some hardware fittings from Hardware **at cost** (₹40,000 transferred; all sold to outsiders by year-end — nothing left in Paints' closing stock). Data:

| Item | Hardware (₹) | Paints (₹) |
|---|---|---|
| Sales (outside) | 9,00,000 | 4,00,000 |
| Opening stock | 1,20,000 | 60,000 |
| Purchases (outside) | 6,00,000 | 2,40,000 |
| Closing stock | 1,40,000 | 70,000 |
| Direct wages | 30,000 | 20,000 |

Common expenses: Rent ₹1,20,000 (area H 2,000 sq ft, Pt 1,000 sq ft); Administration ₹90,000 (apportion on sales, outside only); Depreciation ₹30,000 (asset value H 2,00,000, Pt 1,00,000).

**Step 1 — Trading Account (transfer at cost, so no reserve; still cancels in Total).**

Hardware credits "Transfer to Paints ₹40,000"; Paints debits "Transfer from Hardware ₹40,000."

| Particulars | H (₹) | Pt (₹) | Particulars | H (₹) | Pt (₹) |
|---|---|---|---|---|---|
| To Opening stock | 1,20,000 | 60,000 | By Sales | 9,00,000 | 4,00,000 |
| To Purchases | 6,00,000 | 2,40,000 | By Transfer to Paints | 40,000 | — |
| To Transfer from Hardware | — | 40,000 | By Closing stock | 1,40,000 | 70,000 |
| To Direct wages | 30,000 | 20,000 | | | |
| To Gross profit c/d | 3,30,000 | 1,10,000 | | | |
| **Total** | **10,80,000** | **4,70,000** | **Total** | **10,80,000** | **4,70,000** |

*H check:* debit before GP = 1,20,000 + 6,00,000 + 30,000 = 7,50,000; credit = 9,00,000 + 40,000 + 1,40,000 = 10,80,000; GP = **3,30,000**. ✓
*Pt check:* debit before GP = 60,000 + 2,40,000 + 40,000 + 20,000 = 3,60,000; credit = 4,00,000 + 70,000 = 4,70,000; GP = **1,10,000**. ✓

**Step 2 — Apportion and find net profit.**
- Rent 2,000 : 1,000 = 2 : 1 → H ₹80,000, Pt ₹40,000.
- Administration on outside sales 9,00,000 : 4,00,000 = 9 : 4 → H = 90,000 × 9/13 = ₹62,308; Pt = ₹27,692.
- Depreciation 2,00,000 : 1,00,000 = 2 : 1 → H ₹20,000, Pt ₹10,000.

| | H (₹) | Pt (₹) |
|---|---|---|
| Gross profit | 3,30,000 | 1,10,000 |
| Less: Rent | 80,000 | 40,000 |
| Less: Administration | 62,308 | 27,692 |
| Less: Depreciation | 20,000 | 10,000 |
| **Net profit** | **1,67,692** | **32,308** |

**No stock reserve** — transfer was at cost and nothing transferred remained in stock. Combined net profit = ₹2,00,000.

**Decision tweak — "should Paints be closed because its margin is thin?"** Paints' net profit ₹32,308 on sales ₹4,00,000 is a slim ~8% net margin versus Hardware's ~18.6%. But before recommending closure, note that Paints still absorbs ₹77,692 of *common* fixed costs (rent + admin + depreciation share). If Paints closed, those common costs do not vanish — most (rent of the shared premises, the shared administrator) would re-fall on Hardware, cutting Hardware's profit. Paints is making a **positive contribution** toward shared overheads, so closing it would *reduce* total profit, not raise it. This is the contribution insight from Section 3 made numerical. Examiners reward the candidate who *resists* the naive "low margin ⇒ close" answer and reasons about contribution.

---

## 6. Presentation Formats

**(A) Columnar Departmental Trading and Profit & Loss Account** — the standard exam format. One column per department, side by side, with a final "Total" column, and the General P&L shown *below* as a single combined section.

```
                 Departmental Trading and Profit & Loss Account
                        for the year ended 31 March 20XX
------------------------------------------------------------------------------
 Particulars      | Dept A | Dept B | Total ||  Particulars    | Dept A | Dept B | Total
------------------------------------------------------------------------------
 To Opening stock |   ...  |   ...  |  ...  ||  By Sales        |   ...  |   ...  |  ...
 To Purchases     |   ...  |   ...  |  ...  ||  By Transfers    |   ...  |   ...  |  ...
 To Direct wages  |   ...  |   ...  |  ...  ||  By Closing stock|   ...  |   ...  |  ...
 To Gross Profit  |   ...  |   ...  |  ...  ||                  |        |        |
------------------------------------------------------------------------------
 To (dept expenses)|  ...  |   ...  |  ...  ||  By Gross Profit |   ...  |   ...  |  ...
 To Net Profit c/d|   ...  |   ...  |  ...  ||                  |        |        |
------------------------------------------------------------------------------
             General Profit & Loss Account (NOT departmentalised)
 To General mgr salary ........ ||  By Net profit b/d (all depts) .......
 To Stock reserve (closing) .... ||  By Stock reserve (opening) .........
 To Net profit to Balance Sheet  ||
------------------------------------------------------------------------------
```

**(B) Balance Sheet presentation of the stock reserve.** Under Current Assets:

| Current Assets | ₹ | ₹ |
|---|---|---|
| Inventories (closing stock) | 4,00,000 | |
| Less: Stock Reserve (unrealised inter-dept profit) | (24,000) | 3,76,000 |

**(C) Memorandum vs actual.** In practice the departmental columns are often prepared as a **memorandum** (management) statement, while the ledger keeps one combined Trading and P&L. For CA Intermediate you present the **columnar** account as the answer unless told otherwise.

**(D) Order of the three tiers on the page.** Present *all* departmental Trading rows first (closing each column to gross profit c/d), then *all* departmental P&L rows (closing each column to net profit c/d), and only then the single **General P&L** section drawing the departmental net profits in and pushing one final figure out to the Balance Sheet. A frequent presentation error is to intermingle general items (GM salary, stock reserve) into the departmental columns — this both mis-states departmental profit and loses presentation marks. The visual rule: *anything with a single un-split figure lives below, in the General section.*

*Figure 6.1 — the three homes a rupee finds and where each surfaces in the statement.*

```mermaid
flowchart TD
    R["Every rupee of income or expense"] --> A["Directly one department"]
    R --> B["Shared - apportion on a base"]
    R --> C["Entity level - no departmental cause"]
    A --> T["Departmental Trading or P&L column"]
    B --> T
    C --> G["General P&L single column"]
    T --> N["Departmental net profit per column"]
    N --> G
    G --> P["One true combined net profit to Balance Sheet"]
```

*Direct and shared items build each department's net profit; entity-level items and the net stock reserve meet them in the General P&L to yield one Balance-Sheet figure.*

---

## 7. Connections

- **AS 2 – Valuation of Inventories.** The unrealised-profit / stock-reserve rule is a direct application of AS 2: inventory must never be carried above cost. Inter-departmental mark-up trapped in stock inflates it above cost, so AS 2 requires it removed. If you understand Chapter on AS 2, this chapter's hardest bit is just AS 2 in a new costume.
- **Branch Accounts (next chapter).** Same "measure each unit" instinct, but split by **location** and often with the branch keeping separate books. The **stock reserve** idea reappears identically for goods invoiced to a branch at cost-plus (the "loading" and stock reserve there is the same mathematics as unrealised inter-departmental profit here).
- **Cost Accounting – overhead apportionment.** The allocation-vs-apportionment framework and the "logical basis" idea are *exactly* the primary/secondary distribution of overheads you meet in Cost Accounting. Same reasoning, different report.
- **Cost Accounting – marginal costing / contribution.** The "don't close a positive-contribution department" reasoning (Examples 3 and 5) is the make-or-buy / shut-down decision from marginal costing, surfacing here. Financial and cost accounting are teaching the same lesson from two doors.
- **Companies Act / Schedule III.** When the departments are inside a company, the *combined* net profit and the *net-of-reserve* stock value flow into the Schedule III Balance Sheet and Statement of Profit and Loss. Departmental columns are the management overlay; the statutory statement shows only the consolidated figures.
- **Segment Reporting (AS 17).** Departmental accounts are the small-scale, internal ancestor of AS 17 segment reporting, which requires *listed/large* entities to disclose profitability by business/geographical segment. Same motive — don't hide unit performance inside a blended total — scaled up to a statutory disclosure.

---

## 8. Traps & Examiner Tricks

1. **Carriage inward apportioned on sales.** The single most common error. Carriage/freight **inward** is a *buying* cost → apportion on **purchases**. Only *selling*/outward costs follow sales.
2. **Wrong unrealised-profit fraction.** "Cost + 25%" means profit is **25/125** of transfer price, *not* 25/100. "25% on selling price" means **25/100**. Read which base the question states; mis-reading changes the reserve and hence the combined profit.
3. **Applying the reserve to the whole closing stock.** The reserve applies **only to the portion of closing stock that arose from inter-departmental transfer**, and only to the *mark-up* in it — not to the department's own outside-purchased stock. In Example 3, only ₹1,20,000 (not the full ₹2,00,000) was transferred cloth.
4. **Forgetting the opening stock reserve reversal.** Last year's unrealised profit becomes realised this year (that stock was sold). You must **write it back** (credit General P&L). Only the *net* (closing − opening) hits profit. Candidates who forget the opening reversal overstate the charge.
5. **Putting the stock reserve inside a department's column.** It concerns transfers *between* departments and belongs to *neither* alone → it goes in **General P&L**, never in a single department's P&L.
6. **Not cancelling transfers in the total column.** "Transfer to Garments" (credit, Cloth) and "Transfer from Cloth" (debit, Garments) are equal and opposite; in the *Total* column they net to zero, so the entity's total sales/purchases are not inflated. If your total column double-counts the transfer, it won't reconcile.
7. **Apportioning non-departmental items.** Interest on loan, income tax, dividends, profit on sale of asset — do **not** force these into departmental columns; park them in General P&L. Apportioning them fabricates precision that does not exist.
8. **Equal split by default.** Never split a common cost equally unless the question says so or no better base exists. Always hunt for the cause-and-effect base (area, employees, sales, purchases, asset value). Example 1's tweak shows an equal rent split can *reverse* which department looks better.
9. **Manager's commission on "profit".** If a manager gets a % of *his department's* profit, base it on that department's **net profit before his commission** (or after, as specified) — and be clear whether it is before or after charging the commission itself. State your assumption. "After commission" ⇒ use x/(100+x) (Example 4).
10. **Depreciation apportioned on sales.** Depreciation is driven by **asset value in each department**, not sales. Another cause-and-effect slip.
11. **Using total sales (incl. transfers) as the selling-expense base.** The selling-cost base is sales **to outsiders**; internal transfers involved no selling effort. Including them inflates the transferring department's expense share.
12. **Inventing a reserve on a cost-price transfer.** Transfer at cost ⇒ no mark-up ⇒ **no** reserve, even though transfers still appear and cancel (Example 5). "Transfer" does not automatically mean "reserve."
13. **Reserve on transferred goods that were fully sold.** The reserve exists only for transferred stock **still unsold** at year-end. If the question says all transferred goods were sold to outsiders, closing reserve = nil regardless of mark-up.
14. **Wrong direction of the net reserve.** Closing reserve is a **debit** to General P&L (reduces profit); opening reserve write-back is a **credit** (increases profit). Reversing these two flips the adjustment sign and mis-states profit by twice the amount.
15. **Reading "gross profit ratio to sales" as a given and back-solving carelessly.** Some questions give a GP% and expect you to *derive* one missing figure (e.g., closing stock). Set up the Trading account algebraically and solve; do not guess.

---

## 9. First-Principles Recap

Start from the felt need: *a multi-activity business needs each activity's profit, but shares one ledger.* Everything follows by pure reasoning:

1. **Un-mix revenue and cost, department by department.** For each rupee ask: *point at one department (allocate) or share (apportion)?*
2. **Apportion on cause and effect.** Charge each department the shared cost in proportion to the factor that *drives* it — space for rent, headcount for welfare, sales for selling costs, purchases for buying costs, asset value for depreciation. Any base that ignores causation produces a lie.
3. **Build two tiers.** Trading Account → each department's gross profit; P&L Account → each department's net profit after its share of operating costs. The two-tier split is itself information: it separates costs a department caused alone from costs it merely shares, letting you judge contribution vs absorption.
4. **Handle internal trade honestly.** Transfers between departments are not real sales to the outside world. Record them, but cancel them in the total, and if any transferred goods remain unsold in closing stock, **strip out the mark-up** (stock reserve) because profit is only real when realised outside — and because AS 2 forbids carrying stock above cost.
5. **Keep the genuinely un-departmental items in a single General P&L**, then arrive at one true combined net profit that can face the statutory Balance Sheet.

If you internalise those five moves, you never need to memorise a format again — you can *reconstruct* the whole columnar statement from the logic. And when the examiner tweaks a variable — mark-up on cost vs on sale price, commission before vs after, transfer at cost vs cost-plus, a department that looks weak but contributes — you re-derive the answer instead of hunting for a remembered template.

---

## 10. Quick-Revision Sheet

**Purpose:** measure each department's own profitability inside one shared ledger → drive decisions (expand, shrink, reward, price).

**Three homes for every rupee:** *this department* (allocate) → *shared* (apportion on a base) → *entity-level, no cause* (General P&L).

**Allocation** = cost wholly one department's → charge direct. **Apportionment** = shared cost → split on a logical base.

**Standard bases (derive them — "what drives this cost?"):**

| Cost | Base |
|---|---|
| Rent, rates, building repairs/insurance, lighting/heating | Floor area (lighting also by light points) |
| Selling exp, discount allowed, bad debts, carriage **outward**, salesmen commission | Sales (to outsiders) |
| Carriage **inward**, discount received | Purchases |
| Depreciation, repairs & insurance of assets | Asset value |
| Labour welfare, canteen, PF, ESI | No. of employees |
| Power / fuel | HP × hours or machine hours |
| Supervisor / works-manager salary | Time devoted |

**Trading vs P&L placement:** costs of getting goods saleable (purchases, wages, carriage inward, manufacturing, factory power) go **above** the line; costs of running/selling (rent, salaries, selling exp, depreciation) go **below**.

**Structure:** Departmental Trading (GP per dept) → Departmental P&L (NP per dept) → **General P&L** (single column: interest, tax, GM salary, GM commission, net stock reserve → final combined NP). Total column = self-check.

**Inter-departmental transfer:** credit transferring dept's Trading, debit receiving dept's Trading; **cancel in Total column**. Transfer at cost ⇒ no reserve (but still cancels).

**Unrealised profit (stock reserve):**
- Only on **transferred goods still in closing stock**, and only the **mark-up** in them.
- Cost + x% → profit fraction = **x/(100+x)** of transfer price. "x% on sale price" → **x/100**.
- Closing reserve: **Dr General P&L, Cr Stock Reserve** (deduct from stock in B/S).
- Opening reserve: **Dr Stock Reserve, Cr General P&L** (write back).
- Net charge to profit = **Closing reserve − Opening reserve**.

**Manager's commission:** departmental manager's → that dept's P&L; general manager's → General P&L. "After commission" ⇒ commission = profit-before × x/(100+x).

**Never departmentalise:** interest on loan/debentures (unless a departmental base is given), income tax, dividends, profit/loss on sale of fixed assets/investments, net stock reserve → **General P&L**. Test: *would it exist unchanged with only one department?* If yes → General P&L.

**Top traps:** carriage *inward* on purchases (not sales); reserve fraction 25/125 vs 25/100; reserve only on unsold transferred portion; don't forget opening reserve reversal; reserve → General P&L not a department; depreciation on asset value not sales; no reserve on cost-price transfers; don't close a positive-contribution department.

**Self-check every answer:** each Trading and P&L column must foot; Total column = sum of dept columns with transfers cancelled; combined NP must equal (Σ dept NP − general items − net reserve); Balance-Sheet stock shown *net of reserve*.
