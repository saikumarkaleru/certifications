# Overheads (Absorption Costing)

## Snapshot
- Overhead = Indirect Material + Indirect Labour + Indirect Expenses — real cost that points at no single product.
- "Indirect" is relative: an item is overhead when tracing to the unit is impossible (rent) or not economically worthwhile (dab of glue) — the convenience & materiality test.
- Core flow: Total OH → (Allocation + Apportionment = Primary distribution) → cost centres → (Re-apportionment = Secondary distribution) → production depts → (Absorption) → units.
- Three destinations: Factory OH → product cost & closing stock; Admin OH → generally period cost recovered on cost of production; S&D OH → recovered only on goods sold, never in stock.

## Core concepts
- **Allocation** = charge whole item to one centre (100% traceable). **Apportionment** = split a shared item across centres on a fair basis. **Absorption** = charge production-dept OH onto units via a rate. Allocation + apportionment = primary distribution; re-apportionment of service depts = secondary distribution.
- **Collection** (accumulate by nature, standing-order/cost-account number) precedes allocation (charge to a centre).
- Allocation vs apportionment razor = traceability of the whole. Separately metered power → allocate; single factory bill → apportion. A line can mix both (e.g. power ₹50,000 with ₹12,000 separately metered to A → allocate ₹12,000, apportion ₹38,000).
- Production depts work on the product (units absorb cost); service depts (Stores, Maintenance, Canteen, Power House) serve other depts, so their cost must first be pushed to production depts.
- **Pre-determined rate** = Budgeted OH ÷ Budgeted (normal) activity — needed because prices are quoted before period ends; the mismatch with actuals causes under/over-absorption (a fixed-OH phenomenon).
- **Normal capacity** anchor: divide fixed OH by normal (long-run average, after normal idle time) capacity so idle-capacity cost is exposed as a period loss, not hidden in units.

## Key provisions / rules

**Semi-variable split (know all 4):** High–Low, Comparison/range, Least-squares regression, Graphical/scatter.
- High–Low: Variable/unit = (Cost_high − Cost_low) ÷ (Units_high − Units_low); Fixed = Total − Variable × Activity.

**Apportionment bases (memorise pairing):**

| Overhead | Basis |
|---|---|
| Rent, rates, building dep./repairs | Floor area (sq ft) |
| Lighting, heating | Floor area / light points (use light points/wattage if given); heating on volume if given |
| Power / electricity | HP × machine hours (or metered KWH) |
| Depreciation & insurance of plant | Value / capital of plant |
| Supervision, canteen, welfare, ESI, PF, time-keeping | Number of employees |
| Stores / material handling | Value or weight of material issued |
| Fire insurance of stock | Average value of stock held |
| Delivery / distribution | Weight, volume, tonne-km |
| General / indirect wages | Direct wages or direct labour hours |

Rule: always pick the **most cause-specific basis the data permits**.

**Primary distribution cross-checks:** (1) each row sums across depts to item total; (2) primary-total row = grand total.

**Secondary distribution method chooser:**

| Situation | Method |
|---|---|
| Ignore inter-service work | Direct re-distribution (re-base % onto production depts only, sum to 100%) |
| One-way service between service depts | Step-ladder — rank by number of depts served; larger overhead breaks ties; once closed nothing returns |
| Mutual service, exactly 2 service depts | Simultaneous equations |
| Mutual service, 2+ service depts | Repeated distribution (iterate till service balances ≈ 0) |

**Simultaneous-equation template:** S1 = a + p·S2 ; S2 = b + q·S1 → solve → distribute *solved totals* to production depts in original %. Reciprocal methods must agree (differ only by rounding). Extends to 3 depts via 3 equations.

**Absorption rate (general) = Production dept overhead ÷ Total base quantity.** Six bases:

| Method | Formula | Use when |
|---|---|---|
| % of Direct Material | (Prod OH ÷ Direct Material) × 100 | rarely fair (price swings) |
| % of Direct Wages | (Prod OH ÷ Direct Wages) × 100 | uniform labour rates |
| % of Prime Cost | (Prod OH ÷ Prime Cost) × 100 | seldom ideal |
| Labour Hour Rate | Prod OH ÷ Direct Labour Hours | **labour-intensive** |
| Machine Hour Rate | Prod OH ÷ Machine Hours | **machine-intensive** |
| Rate per unit | Prod OH ÷ Units produced | homogeneous output |

Time-based rates (labour hr, machine hr) preferred — overhead is fundamentally time-related; money bases get distorted by price fluctuation.

**Machine Hour Rate:** MHR = Standing charges/hr + Machine running expenses/hr. Denominator = **effective (productive) hours** = gross − normal idle (setup, maintenance, breakdowns). Abnormal idle is NOT deducted (→ Costing P&L). Depreciation for MHR = (Cost − Residual) ÷ Life, then ÷ effective hours. One operator/one machine → wage may be direct (out of MHR); one operator/several machines → indirect (inside comprehensive MHR). "Comprehensive MHR" usually includes wages + setup.

**Blanket rate = total factory OH ÷ total factory base** (one rate). Acceptable only when single product OR all products pass uniformly through all departments; else use **departmental rates**.

**Under/Over-absorption:**
- Overhead absorbed = Pre-determined rate × **Actual** base.
- Under/Over = Absorbed − Actual overhead.
- Absorbed > Actual → **over-absorbed** (credit Costing P&L, costing profit understated).
- Absorbed < Actual → **under-absorbed** (debit Costing P&L, costing profit overstated).
- Two causes: Expenditure part = Budgeted OH − Actual OH; Volume part = Std rate × (Actual activity − Budgeted activity). They sum to the total gap (seed of fixed-OH expenditure & volume variances).

**Treatment of under/over-absorption:**

| Cause / size | Treatment |
|---|---|
| Abnormal (strike, fire, breakdown) | Costing P&L |
| Sub-normal capacity (idle-capacity cost) | Costing P&L (do NOT spread) |
| Normal & small | Costing P&L |
| Normal & large (wrong rate/volume estimate) | **Supplementary rate** → WIP + FG + COGS |

Supplementary rate = under/over amount ÷ actual base. Under → positive rate added; over → negative rate deducted. Apply either per unit/hour, or pro-rata on absorbed-OH value in each of WIP/FG/COGS.

**Administration OH — 3 views:** (1) apportion between production and S&D; (2) charge to Costing P&L as period cost; (3) ICAI default — recover as % of cost of production/works cost. **S&D OH:** recovered only on units sold, never enters stock; bases = % of works cost, % of selling price, rate per unit sold; distribution costs on weight/volume/tonne-km.

## Worked mini-example
Machine hour rate. Machine ₹2,40,000, scrap ₹20,000, life 10 yr; dept rent ₹36,000 (machine = 1/4 area); supervision ₹48,000 (1 of 4 machines); power 5 units/hr @ ₹6; R&M ₹11,000; runs 2,200 effective hrs.
- Depreciation = (2,40,000 − 20,000)/10 = ₹22,000; Rent = 36,000 × 1/4 = ₹9,000; Supervision = 48,000 × 1/4 = ₹12,000; R&M ₹11,000. Standing total = ₹54,000.
- Standing/hr = 54,000 ÷ 2,200 = ₹24.545. Power/hr = 5 × 6 = ₹30.
- **MHR = 24.545 + 30 = ₹54.55/hr.** Check: 54.545 × 2,200 = ₹1,20,000 = 54,000 + 66,000 ✔.
- Comprehensive (operator ₹40/hr) = 54.55 + 40 = ₹94.55/hr.

## Exam traps & must-remember
- Overhead absorbed uses **actual** base, NOT budgeted (pre-determined rate uses budgeted; application uses actual).
- Direction: Absorbed > Actual = over (credit P&L); Absorbed < Actual = under (debit P&L).
- Simultaneous method: distribute the **solved** service total (not the residual/primary); include service-to-service % — dropping them wrongly makes it the direct method.
- Step method: start with dept serving most others (larger OH breaks ties); never return cost to closed dept; re-base surviving %.
- Abnormal causes (strike, fire, idle capacity, breakdown) → always Costing P&L, never supplementary rate.
- Supplementary rate must hit **WIP too**, not just FG and COGS.
- **Idle-capacity under-absorption (sub-normal working) → Costing P&L, NOT spread** — exception to "normal + large → supplementary rate". Read the cause.
- Power on HP × machine hours, NOT floor area/headcount. Depreciation on plant value, NOT floor area. Supervision on employees, NOT plant value.
- Allocate any separately-metered/named slice first, then apportion the remainder.
- MHR denominator = effective hours (after normal idle), not gross.
- S&D overhead never enters closing-stock value; include factory OH (admin per policy).
- Direct method: renormalise service-to-production % to 100%.
- Blanket rate justification = "single product OR uniform flow", not "convenient".

## One-line recall
- Allocate whole, Apportion shared, Absorb into units; Primary then Secondary then Absorption.
- Pre-determined rate = Budgeted OH ÷ Budgeted (normal) activity; Absorbed = rate × actual base; gap = Absorbed − Actual.
- Machine-intensive → machine hour rate; labour-intensive → labour hour rate; time bases beat money bases.
- Reciprocal (mutual) service → simultaneous equations or repeated distribution; both land whole total on production depts and must agree.
- Normal & large gap → supplementary rate over WIP+FG+COGS; abnormal / idle-capacity / small → Costing P&L.
- MHR = standing charges/hr + running expenses/hr, over effective hours.
