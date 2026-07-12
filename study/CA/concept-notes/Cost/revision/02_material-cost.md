# Material Cost

## Snapshot
Material is the largest cost element (40–70% of total) and the leakiest (portable, deteriorates, ties up working capital). Control = keep the right quantity (levels + EOQ), price issues honestly (FIFO/LIFO/WA), classify losses (normal vs abnormal), and apply selective control (ABC). Chain of custody with a document at every link: requisition → PO → GRN → bin card/stores ledger → requisition note.

## Core concepts
- **Cost-flow assumption, not physical flow:** FIFO/LIFO only assume a costing order; physical issue can differ.
- **Landed cost:** material cost = invoice price − trade discount − creditable GST/duty + carriage inward + insurance in transit + other purchase charges. **Cash discount excluded** (financial item); non-creditable GST added.
- **EOQ tug-of-war:** ordering cost falls with big lots, carrying cost rises with big lots; minimum at the crossing (ordering = carrying). Total-cost curve flat near bottom (robust to ±20–30% error).
- **Levels** = safety-buffer system letting a storekeeper run day-to-day control; management sets levels once.

## Key provisions / rules
**Procurement documents:**

| Document | Records | Kept by |
|---|---|---|
| Purchase Requisition | Authorised need | Stores/Dept |
| Purchase Order | Commitment to supplier | Purchasing |
| Goods Received Note (GRN) | Arrival + inspection | Receiving |
| Bin Card | Quantity only | Storekeeper (in stores) |
| Stores Ledger | Quantity + value | Costing office |
| Material Requisition Note | Authorised issue | Production → Stores |

Perpetual inventory (continuous records) vs continuous stocktaking (physical counting that verifies records) — don't confuse.

**Inventory levels:**

| Item | Formula |
|---|---|
| Re-order Level (ROL) | Maximum usage × Maximum lead time |
| ROL (alt) | Safety stock + (Avg usage × Avg lead time) |
| Minimum Level | ROL − (Average usage × Average lead time) |
| Maximum Level | ROL + ROQ − (Minimum usage × Minimum lead time) |
| Danger Level | Average usage × Emergency lead time |
| Average Stock | Minimum level + ½ ROQ = ½(Min + Max) |
| Safety stock | (Max usage × Max LT) − (Avg usage × Avg LT) = Max·Max − Avg·Avg |

Ordering must hold: Danger < Minimum < Re-order < Maximum.

**EOQ:**
- EOQ = √(2 × A × O ÷ C)
- A = annual demand (units); O = ordering cost per order; C = carrying cost per unit per year = carrying % × unit price.
- No. of orders/yr = A ÷ EOQ; Time between orders = 365 ÷ (A/EOQ) days.
- Ordering cost = (A/EOQ)×O; Carrying cost = (EOQ/2)×C; **at EOQ these are equal (self-check).**
- Square-root damping: demand ×4 → EOQ ×2; ordering cost ×2 → EOQ ×√2; carrying cost ×2 → EOQ ÷√2.
- Quantity discounts: minimise Total = (A × price) + (A/Q)×O + (Q/2)×C. Evaluate at plain EOQ and at smallest qualifying quantity of each slab; recompute C at each slab's price. Deepest discount need not win.
- Assumptions: known constant demand; constant O and C; constant price (no discounts); whole order delivered at once; known lead time; no stock-outs.

**Issue valuation (rising prices):**

| Method | Issue cost | Profit | Closing stock |
|---|---|---|---|
| FIFO (oldest issued first) | Lowest | Highest | Highest |
| LIFO (newest first; banned under AS-2/Ind AS-2) | Highest | Lowest | Lowest |
| Weighted Average | Middle | Middle | Middle |

- Weighted-avg rate = value on hand ÷ units on hand, recomputed after each **receipt** (issue doesn't change rate). Periodic weighted average = one rate for whole period.
- Notional-price methods (standard, replacement/market) throw up a variance → Costing P&L; actual-price methods recover exactly what was paid.
- Simple average (average of rates, ignores quantities) can break reconciliation — theoretically unsound.
- Universal check: Opening + Purchases = Issues + Closing (in quantity AND value). Falling prices → reverse FIFO/LIFO.

**Losses (golden principle: normal absorbed by good output; abnormal → Costing P&L):**

| Type | Recovery | Treatment |
|---|---|---|
| Waste (no recovery) | Nil/negative | Normal → good output; Abnormal → Costing P&L |
| Scrap (small sale value) | Yes small | Normal scrap credited to cost/OH; Abnormal → Costing P&L |
| Spoilage (unrectifiable) | Low | Normal net cost → good output; Abnormal net → Costing P&L |
| Defectives (rectifiable) | Rectifiable | Normal rectification → good output/OH; Abnormal → Costing P&L |

- Cost per good unit = (Total cost − normal-loss scrap value) ÷ **expected good output** (input − normal loss).
- Abnormal loss = expected good output − actual output; value at cost per good unit, less its own scrap → Costing P&L.
- Abnormal gain = actual output − expected good output; value at same rate; DEBIT process / CREDIT Costing P&L; then claw back scrap on the normal loss that did NOT occur (reduces the gain).

**Selective control:**

| Class | ~% items | ~% value | Control |
|---|---|---|---|
| A | 10% | 70% | Tight, low safety stock, frequent review, EOQ enforced |
| B | 20% | 20% | Moderate |
| C | 70% | 10% | Loose, bulk buy, high safety stock, two-bin |

Classify by **annual consumption value = annual qty × unit price** (not sticker price). Cousins: VED (criticality — spares), FSN (movement — dead stock), HML (unit price — authorisation), SDE (availability — imports).

**Inventory turnover** = Cost of material consumed ÷ Average stock [Avg = ½(Opening+Closing)]; Holding days = 365 ÷ turnover. Low/falling turnover = slow-moving/obsolete → investigate.

## Worked mini-example
A = 12,000 units/yr, O = ₹150/order, unit price ₹20, carrying 20% → C = ₹4.
EOQ = √(2 × 12,000 × 150 ÷ 4) = √9,00,000 = **948.68 ≈ 949 units.**
Orders/yr = 12,000 ÷ 948.68 = 12.65 (~13). Time between = 365 ÷ 12.65 ≈ 29 days.
Ordering cost = 12.65 × 150 = ₹1,897; Carrying = (948.68/2) × 4 = ₹1,897 (equal → correct). Total inventory cost ≈ ₹3,795.

## Exam traps & must-remember
- Carrying cost given as % → convert to ₹ per unit per year (% × unit price) before EOQ. #1 error.
- O is per order, not annual purchasing-dept cost.
- ROL uses MAX × MAX; Minimum subtracts AVG × AVG; Maximum subtracts MIN × MIN. Keep usage and lead time on the same time basis (don't mix days/weeks).
- Quantity discounts: compare total annual cost (purchase + ordering + carrying) at EOQ and each break-point; deepest discount need not win.
- Cost per good unit uses EXPECTED good output, not actual output.
- Scrap routing: normal-loss scrap reduces cost-per-unit; abnormal-loss scrap nets against Costing P&L; abnormal gain claws back scrap on loss that didn't occur.
- Weighted average recomputed after every RECEIPT (not period-end, not on issues).
- FIFO = higher profit only in RISING prices; reverse if falling.
- ABC by annual consumption value, not unit price; ABC ignores criticality (use VED for vital cheap spares).
- Cash discount excluded from material cost; creditable GST excluded; carriage inward added.
- Bin card = quantity only (storekeeper); stores ledger = quantity + value (costing office).

## One-line recall
- EOQ = √(2AO/C); at EOQ ordering cost = carrying cost.
- ROL = Max usage × Max lead time; Danger = Avg usage × Emergency lead time.
- Rising prices: FIFO → highest profit & closing stock; LIFO → lowest; WA middle.
- Normal loss absorbed by good output; abnormal loss/gain → Costing P&L at cost-per-good-unit rate.
- ABC by consumption value; classify attention where rupees are.
- Check: Opening + Purchases = Issues + Closing (qty & value).
