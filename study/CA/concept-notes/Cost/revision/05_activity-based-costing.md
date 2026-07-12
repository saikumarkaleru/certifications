# Activity-Based Costing (ABC)

## Snapshot
- Purpose of ABC = a better **decision** (pricing, product mix, make-or-buy, cost reduction), NOT more accurate financial statements. Total profit is unchanged.
- The disease is **averaging**: spreading one overhead pot over one volume base taxes light users to subsidise heavy users (cross-subsidy).
- Causal chain: **Resources → Activities (cost pools) → Products (via cost drivers).** Cost follows causation.
- Distortion law: traditional costing **over-costs high-volume simple** products and **under-costs low-volume complex** products; ABC reverses both. Distortions are equal & opposite (conservation of overhead).

## Core concepts
- **Activity** = task consuming resources (setup, inspect, purchase, move, machine). **Cost pool** = total ₹ of one activity. **Cost driver** = factor causing the activity's cost. **Cost driver rate** = pool ÷ total driver quantity.
- **Resource driver** traces resources INTO a pool (stage 1); **activity driver** traces pool TO products (stage 2). Exams usually give pools pre-totalled (stage 1 done).
- **Cost driver** = cause of cost; **cost object** = thing being costed (product, order, customer, channel).
- **Value-added** vs **non-value-added (NVA)** activities — ABC quantifies rupees in NVA (springboard to ABM). Some NVA are necessary (statutory inspection) and cannot be cut.
- Traditional costing designed when labour was dominant and overhead small; now overhead is 40–70% and product ranges fragmented, so blunt volume allocation swings product costs 30–50%.

## Key provisions / rules

**Master formulae:**
- Cost Driver Rate = Total Cost of Activity Pool ÷ Total Cost Driver Quantity
- Overhead to a Product = Σ (Driver Rate × Driver Units consumed by product)  [across all activities]
- Traditional Rate = Total Overhead ÷ Total Volume Base (labour hrs / machine hrs / units)
- Machine-hr driver total = Σ (units × machine hrs per unit) — NOT units alone
- Unit cost = (Prime cost + Overhead absorbed) ÷ units
- Reconciliation: Σ overhead absorbed by all products = Total overhead given
- Cross-subsidy: ₹ over-costed on one product = ₹ under-costed on the other

**Two kinds of cost driver (accuracy ladder):**
- **Transaction driver** — counts times activity happens (no. of setups, orders, inspections); cheap; use when occurrences uniform.
- **Duration driver** — how long it takes (setup hours, inspection hours); use when occurrences vary widely.
- **Intensity / direct-charge driver** — actual resources charged to a special job; dearest, most accurate; for genuinely special jobs.
- Ladder: transaction (cheapest/least accurate) → duration → intensity (dearest/most accurate).

**Driver-choice tests (both required):** (1) **causation** — driver movement must genuinely cause pool movement; (2) **measurability** — cheap and objective to count. Perfect-but-unmeasurable is useless; measurable-but-non-causal is worse (looks authoritative while lying).

**Cooper's hierarchy of activities (most examinable):**

| Level | Triggered by | Examples | Driver | Avoidable if you… |
|---|---|---|---|---|
| **Unit-level** | each unit | power, machining, consumables/unit | machine hrs, labour hrs, units (volume) | drop one unit |
| **Batch-level** | each batch/run | setup, first-article inspection, material moves, purchase order | no. of setups, batches, orders, inspections | drop/merge a batch |
| **Product-level** | each product line existing | design, BOM maintenance, special testing, dedicated tooling | no. of products, design hours | drop the product line |
| **Facility-level** | factory existing | rent, security, general admin, lighting | none — arbitrary allocation or period cost | close the facility |

- Batch- and product-level costs are fixed to volume but variable to complexity; batch cost is step-fixed (steps up per batch). Facility-level is genuinely un-traceable.
- Relevance ladder = only costs at or below the level you change are avoidable. Dropping a product does NOT remove facility-level cost.

**Seven-step ABC procedure:** identify activities → create cost pool per activity (stage-1) → identify cost driver → compute driver rate → measure each product's driver consumption → charge OH (rate × units, summed) → add prime cost.

**Granularity trade-off:** too few pools = blanket averaging; too many = costly, cluttered. Merge activities driven by the same driver into one **homogeneous cost pool** (costs move in proportion to one driver). Goal = fewest pools that stay homogeneous.

**When ABC pays off:** overhead is large share of cost · product/customer range diverse · non-volume overheads dominate (setups, inspections, handling) · pricing must be sharp · frequent high-stakes mix/pricing decisions. **Not worth it:** single product · trivial overhead · all overhead genuinely volume-driven.

**Limitations:** expensive to install/run · not every cost has a clean driver (residual arbitrariness on facility cost — reduces but never eliminates) · over-refinement breeds complexity · still largely full-absorption/historical (full cost ≠ relevant cost for short-run drop/special-order decisions) · behavioural resistance & driver-count gaming.

**Cost object flexibility:** ABC can cost a product, order, customer or channel. **ABM:** operational ABM = do things right (make activities cheaper — SMED cuts setup, quality-at-source cuts inspection); strategic ABM = do the right things (change mix/design/price). **ABB:** works the plan backward (output → activities → resources) to set driver-based budget; ABC works actuals forward.

## Worked mini-example
Standard (1,00,000 units, prime ₹40) & Premium (10,000 units, prime ₹60). Total OH ₹22,00,000; each uses 0.5 mc hr/unit (Standard 50,000, Premium 5,000).

**Traditional** rate = 22,00,000 ÷ 55,000 = ₹40/mc hr → ₹20 OH/unit both → Standard ₹60, Premium ₹80.

**ABC** driver rates: Machining 5,50,000÷55,000 = ₹10/hr; Setups 6,00,000÷120 = ₹5,000; Inspection 4,50,000÷150 = ₹3,000; Purchasing 3,00,000÷200 = ₹1,500; Handling 3,00,000÷150 = ₹2,000.
- Premium (setups 100, inspections 120, orders 160, moves 100, mc-hr 5,000): OH = 50,000 + 5,00,000 + 3,60,000 + 2,40,000 + 2,00,000 = ₹13,50,000 → ₹135/unit.
- Standard OH = ₹8,50,000 → ₹8.50/unit. Reconcile: 8,50,000 + 13,50,000 = 22,00,000 ✔.
- **ABC total cost: Standard ₹48.50, Premium ₹195** (vs traditional ₹60 / ₹80). Cross-subsidy = ₹11.50 × 1,00,000 = ₹115 × 10,000 = ₹11,50,000 (equal & opposite ✔). Premium sold at "40% margin" ₹112 actually loses ₹83/unit.

## Exam traps & must-remember
- Facility-level costs are NOT driver-traceable — allocate arbitrarily (and say so) or treat as period cost; never invent a spurious driver.
- Machine-related driver total = units × mc hr/unit, NOT units (commonest slip).
- Always **reconcile** absorbed OH back to total OH before writing the comment.
- Keep **4–6 decimals** in driver rates; round only the final answer.
- Don't confuse the two stages — pools usually pre-totalled (stage 1 done); don't re-split.
- ABC raises low-volume cost only because such products are usually complex — mechanism is complexity, not volume per se.
- Total profit is **identical** under ABC and traditional — only per-product profit differs (conceptual error to say otherwise).
- Never recommend dropping a "loss" product on ABC full cost alone — it includes facility-level cost that won't vanish; use avoidable-cost/contribution analysis (full cost ≠ relevant cost).
- Setup hours (duration) vs number of setups (transaction) — use whichever the question offers.
- Keep total-overhead row and per-unit row physically separate; don't divide by units too early or mix per-unit with totals.
- Use the **stated current** traditional base (labour vs machine hrs) — it's a given fact, not your choice; the base changes the magnitude of distortion but never its direction.
- Charge whole setups by count (₹5,000/setup) — never smooth per unit then re-multiply (reintroduces volume-averaging).
- Lowering an over-costed product's cost is not new profit — total profit unchanged; only pricing room changes.
- More pools ≠ more accuracy beyond homogeneity.
- Driver denominator = whole plant's total driver count, not one product's.

## One-line recall
- Cost follows causation: Resources → Activities → Products; rate = pool ÷ total driver, charge = rate × units consumed.
- Traditional over-costs high-volume simple, under-costs low-volume complex; ABC reverses both; distortions equal & opposite (conservation).
- Cooper's hierarchy = unit / batch / product / facility; only unit-level is truly volume-driven; facility-level is un-avoidable except by closing the plant.
- Driver ladder: transaction → duration → intensity; a good driver is causal AND measurable.
- ABC pays off with large overhead + diverse products + non-volume drivers + sharp pricing; total profit never changes, only per-product.
- Full cost (ABC) ≠ relevant cost — use avoidable-cost analysis before dropping a product.
