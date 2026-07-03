<!-- v2-deep -->

# Chapter 13 — Standard Costing & Variance Analysis

## 1. The Problem: A Number That Tells You Nothing

Imagine you run a factory that makes steel almirahs. At month-end your cost sheet says: *actual cost of production = ₹47,80,000*. Your boss asks one question: **"Is that good or bad?"**

You cannot answer. ₹47,80,000 is a naked fact. Good compared to *what*? Maybe steel prices spiked. Maybe your workers were slow. Maybe you simply made more almirahs than planned, so of course the total is higher. The single number hides five different stories, and each story demands a *different manager to fix it* — the purchase officer for prices, the shop-floor supervisor for worker speed, the production planner for volume.

This is the central failure of ordinary costing: **it records what happened but cannot say what should have happened, so it cannot locate responsibility.** A cost that is merely *recorded* is a post-mortem. A cost that is *controlled* must be caught, diagnosed, and pinned on a cause while there is still time to act.

So the real problem is not "what did it cost?" It is:

> Given that actual cost differs from what we expected, **by how much, because of which cause, and whose desk does the correction land on?**

Standard costing is the answer. It sets a *pre-determined "should be" cost* for every unit, then compares actual to that standard, and — crucially — **splits the total gap into named pieces**, each piece traceable to one decision, one department, one lever. That splitting is variance analysis.

**Why "should have cost" beats "cost last month".** A tempting alternative is to compare this month's actual against *last month's* actual — a trend line. But last month was itself uncontrolled; it may have baked in the same inefficiency. Comparing bad against bad tells you the inefficiency is *stable*, not that it is *acceptable*. A standard is an *engineered* target, independent of past sloppiness, so the gap it reveals is a gap against what is *achievable*, not merely against what happened to occur before. This is why standard costing is a tool of *control*, whereas historical comparison is merely a tool of *observation*.

**Where standard costing fits — and where it does not.** It shines in **repetitive, standardisable production**: engineering, chemicals, textiles, food processing — anywhere a unit is made the same way thousands of times so a meaningful "par" exists. It struggles in **job/contract work** where every unit differs (no stable standard), in **rapidly changing conditions** (standards go stale overnight), and in **highly creative or R&D work** (output is not repeatable). The exam sometimes tests this judgement directly: *"State two situations where standard costing is unsuitable."*

## 2. The Core Idea: A Budget Per Unit, Then Control by Exception

Two analogies carry the whole chapter.

**Analogy 1 — The par score in golf.** A golf hole has a *par* (say, 4 strokes). Par is not what an average hacker scores; it is what a competent player *should* score under normal conditions. When you take 6 strokes, you are "2 over par". Nobody records "6 strokes" in isolation — they record it *against par*, because par converts a raw number into a judgement. A **standard cost is the par of a product**: the carefully engineered cost a unit *should* incur under efficient, normal operating conditions.

**Analogy 2 — Control by exception, like a car dashboard.** Your car has dozens of systems, but you don't monitor each continuously. You watch the dashboard, and only when a warning light glows do you investigate *that* system. Variance analysis is management's dashboard. When actual equals standard, the light is off — ignore it. When a variance is large, the light glows red — investigate *that specific variance*, not the whole factory. This is **management by exception**: attention flows only to the deviations, and the *decomposition of variances tells you which warning light lit up.*

Put together: standard costing sets par per unit; variance analysis reads the dashboard and names the exception.

**Not every glowing light deserves a trip to the mechanic.** Management by exception has a second edge students forget: *materiality*. A ₹200 adverse variance on a ₹40 lakh cost base is noise — chasing it costs more managerial time than it saves. Firms set an **investigation threshold** (say, variances above 5% of standard cost, or above a fixed rupee limit) below which the light is treated as "off" even when technically non-zero. The reasons a variance may not be worth investigating: (a) it is *small* (immaterial); (b) it is *random* (statistical noise around a stable process, not a controllable cause); (c) the *cost of investigation exceeds the benefit*; (d) it is *uncontrollable* (a market-wide price surge no manager could prevent). This is the difference between a *statistically significant* variance and a *managerially actionable* one — an exam-favourite discussion point.

**Controllable vs uncontrollable variances.** A variance is *controllable* if a specific manager could have influenced it (excess material usage from careless handling), and *uncontrollable* if it arose from factors outside anyone's authority (a nationwide steel price hike, a government wage award). The whole responsibility-accounting purpose of the chapter collapses if you pin an uncontrollable variance on a manager: you demotivate without improving anything. Examiners test this by asking you to *classify* a listed set of variances as controllable or not, and to name the responsible manager.

## 3. Why It's Built This Way: The Logic of Decomposition

Why not just report one total cost variance? Because a total is a *sum of causes that pull in opposite directions and belong to different people*. Consider labour cost. It can differ from standard for two independent reasons:

1. You **paid a different wage rate** than planned (a purchasing/HR decision — you hired costlier workers, or a wage award increased rates).
2. Your workers **took a different number of hours** than the job should need (a shop-floor efficiency matter — supervision, machine condition, worker skill).

A single "labour cost variance" of ₹20,000 adverse could be +₹50,000 from paying too much and −₹30,000 saved from working fast, netting to ₹20,000. Report only the ₹20,000 and you have *hidden a serious rate problem behind an efficiency success*. The two must be separated because **they have different causes, different owners, and different corrective actions.**

The universal engine behind every variance is one idea:

> **Change one thing at a time.** To isolate the price effect, hold quantity constant and vary only price. To isolate the quantity effect, hold price constant (at standard) and vary only quantity.

Every formula in this chapter is that single principle applied to a different input. Once you *see* it, you never memorise a formula again — you *reconstruct* it. The general shapes are:

- **Price/Rate/Expenditure variance** = (Standard price − Actual price) × Actual quantity → *"we bought/paid at a wrong price for what we actually used."* Quantity held at actual.
- **Usage/Efficiency/Quantity variance** = (Standard quantity for actual output − Actual quantity) × Standard price → *"we used a wrong amount, valued at the honest standard price so the price story doesn't leak in."* Price held at standard.

Notice the asymmetry that trips up thousands of students: the **price variance uses *actual* quantity**, but the **usage variance uses *standard* price**. This is deliberate. We value the usage variance at standard price precisely so that no part of the price problem contaminates the efficiency measure — the shop-floor supervisor is judged on hours, not on wage rates he doesn't set.

**The joint variance — the deeper reason for the asymmetry.** When *both* price and quantity change, the total gap actually contains three pieces, not two: a pure price effect, a pure quantity effect, and a *joint* effect (the price change acting on the quantity change). Algebraically, the joint bit = (SP − AP) × (SQ − AQ). Two-way variance analysis must park this joint slice somewhere, and the ICAI convention **absorbs it into the price variance** — which is exactly why the price variance is computed on *actual* quantity (AQ = SQ + the quantity deviation) rather than standard quantity. Some textbooks report a separate three-variance breakdown, but the ICAI two-variance method is standard for the exam. Knowing *where the joint variance hides* is what lets you answer "why actual quantity in the price formula and not standard?" with understanding, not recitation.

### The general "three-column" skeleton

Almost every cost variance in this chapter is one instance of a single three-column layout. Build these three figures and *every* variance is a difference between two adjacent columns:

| Column | What it is | Fixes what |
|---|---|---|
| **① Standard for actual output** | SQ × SP (or SH × SR) | nothing fixed — the pure target |
| **② Actual quantity at standard price** | AQ × SP (or AH × SR) | price fixed at standard, quantity actual |
| **③ Actual** | AQ × AP (or AH × AR) | both actual |

Then: **Usage/Efficiency = ① − ②** (price held at standard, quantity varies) and **Price/Rate = ② − ③** (quantity held at actual, price varies), and **Cost = ① − ③** (the whole gap). Master this one skeleton and you can reconstruct material, labour and variable-overhead variances without a single memorised formula.

### The sign convention (learn this once, apply everywhere)

For **cost** variances: `Standard − Actual`.
- Positive result = **Favourable (F)** → actual cost was *below* standard, good.
- Negative result = **Adverse (A)** → actual cost *exceeded* standard, bad.

For **sales/profit** variances the logic flips because more is better: `Actual − Budget` for the value, and favourable means actual *exceeds* budget.

If you always write the standard/budget figure first and subtract the actual, and then read "positive = F for costs, remember to flip for sales," you never lose a sign.

**Why the sign flips for sales — first principles.** A cost and a revenue are opposite-signed contributions to profit. For a *cost*, "actual below standard" *raises* profit → favourable, so favourable = standard − actual > 0. For a *sale*, "actual above budget" *raises* profit → favourable, so favourable = actual − budget > 0. The single unifying rule underneath both is: **a variance is Favourable when it increases profit, Adverse when it decreases profit.** If you ever forget which subtraction to write, ask "does this movement make the firm richer?" — that never fails, even on an exotic variance you have never seen.

## 4. Full Technical Content: Setting Standards and the Complete Variance Tree

### 4.1 What a standard cost is, and how it is set

A **standard cost** is a pre-determined cost per unit of output, built up element by element from two things: a **physical standard** (how much input a unit *should* consume — kg, hours) and a **price standard** (what each unit of input *should* cost — ₹/kg, ₹/hour). Their product is the standard cost of that element.

Standards are set by the **standard costing committee** (production engineer, purchase manager, cost accountant, personnel manager) using:

- **Material quantity standards** — from the bill of materials and engineering studies, *including a normal allowance for unavoidable scrap/wastage*.
- **Material price standards** — from the purchase manager's forecast of prices over the standard period, net of trade discounts.
- **Labour time standards** — from time-and-motion study, including normal idle/rest allowances.
- **Wage rate standards** — from HR/wage agreements.
- **Overhead standards** — budgeted overheads divided by a budgeted activity base (standard hours or units).

**Types of standard (matters for interpretation):**

| Type | Basis | Problem |
|---|---|---|
| **Ideal standard** | Perfect conditions, no wastage, no breakdown | Unattainable; demotivating; always adverse |
| **Basic standard** | Fixed long-term, unchanged for years | Goes stale; useless for current control |
| **Current standard** | Present conditions, short period | Reflects inefficiencies as "normal" |
| **Normal (Expected) standard** | Attainable under normal efficient conditions | **The preferred, realistic benchmark** |

The **normal/attainable standard** is what ICAI problems assume unless told otherwise: tight enough to motivate, loose enough to be reachable.

**Why the choice of standard is a behavioural decision, not just an accounting one.** An *ideal* standard is always missed, so every report is adverse — workers stop believing the number and tune it out (the "cry wolf" effect). A *loose* current standard flatters everyone and hides real slack. The *attainable* standard sits in the motivational sweet spot: hard enough that hitting it means something, soft enough that hitting it is possible, so the variance carries *information* rather than *noise or flattery*. This is why the choice of standard is examined as a management-accounting judgement, not merely a formula input.

**The "standard hour" — the unit that makes everything comparable.** A *standard hour* is not sixty minutes; it is **the quantity of output that should be produced in one hour**. It is a measure of *output expressed in time*. Its power: a factory making three dissimilar products (chairs, tables, stools) cannot add "40 chairs + 30 tables" meaningfully, but it *can* add the standard hours each represents, giving one common yardstick of activity. Every overhead and efficiency variance leans on this idea — "standard hours for actual output" is literally actual output re-expressed as the time it *should* have taken. Get comfortable with it, because SH is the pivot of half the chapter.

**Revision of standards.** Standards are revised when there is a *permanent* change — a new wage agreement, a redesigned product, a lasting change in material prices or method. They are **not** revised for *temporary* fluctuations (a one-off price spike), because a standard that chases every wobble stops being a stable benchmark. The exam contrast: a temporary deviation produces a *variance* (to be investigated); a permanent change justifies *revising the standard itself*.

**Standard costing vs budgetary control:** a budget is a *total* plan for a *department/period* (₹ for the whole factory); a standard is a *per-unit* cost. Budgets are extensive (aggregate totals); standards are intensive (per unit). They are complementary — the standard cost card feeds the flexible budget. A further distinction examiners like: budgetary control can operate for *any* function (finance, admin, sales — even where no physical unit exists), whereas standard costing needs a *measurable, repetitive unit of output*. So budgetary control is *broader in scope*; standard costing is *deeper in analysis*.

### 4.2 The variance tree — the map of the whole chapter

```mermaid
flowchart TD
    A["Total Cost Variance"] --> B["Direct Material"]
    A --> C["Direct Labour"]
    A --> D["Variable Overhead"]
    A --> E["Fixed Overhead"]
    B --> B1["Price Variance"]
    B --> B2["Usage Variance"]
    B2 --> B3["Mix Variance"]
    B2 --> B4["Yield Variance"]
    C --> C1["Rate Variance"]
    C --> C2["Efficiency Variance"]
    C --> C3["Idle Time Variance"]
    C2 --> C4["Mix Variance"]
    C2 --> C5["Yield Variance"]
    D --> D1["Expenditure Variance"]
    D --> D2["Efficiency Variance"]
    E --> E1["Expenditure Variance"]
    E --> E2["Volume Variance"]
    E2 --> E3["Capacity Variance"]
    E2 --> E4["Efficiency Variance"]
```
*Figure 13.1 — The full cost-variance tree. Every parent equals the sum of its children; this "adding up" is your self-check.*

The unbreakable rule of the tree: **at every node, the children reconcile to the parent.** Price + Usage = Cost. Mix + Yield = Usage. Capacity + Efficiency = Volume. If they don't add up, you have an arithmetic error — the tree is your built-in proof.

**A map to the same idea seen a second way** — the three-column skeleton (§3) sitting behind each element:

```mermaid
flowchart LR
    A["Std for actual output = SQ times SP"] --> B["AQ times SP"]
    B --> C["Actual = AQ times AP"]
    A -->|"Usage or Efficiency"| B
    B -->|"Price or Rate"| C
    A -->|"Total Cost Variance"| C
```
*Figure 13.2 — One skeleton, every element. The left gap is the quantity story, the right gap is the price story, the whole span is the cost variance.*

### 4.3 Direct Material Variances

Let `SQ` = standard quantity **for actual output** (not budgeted output!), `AQ` = actual quantity used, `SP` = standard price, `AP` = actual price. `AI` = actual quantity purchased/input.

- **Material Cost Variance (MCV)** = (SQ × SP) − (AQ × AP)
  *Meaning:* total gap between what the actual output should have cost in materials and what it did cost. The parent.

- **Material Price Variance (MPV)** = (SP − AP) × AQ
  *Meaning:* the cost of buying at the wrong price, for the quantity actually used. Owner: **purchase manager.** (Some texts compute on quantity *purchased* AI when price variance is isolated at purchase point; ICAI default uses AQ unless purchase and usage quantities differ and the question specifies.)

- **Material Usage (Quantity) Variance (MUV)** = (SQ − AQ) × SP
  *Meaning:* the cost of using the wrong amount of material, valued at the honest standard price. Owner: **production/shop floor.**

  **Check:** MPV + MUV = MCV.

When there are **several materials mixed together** (e.g., a chemical batch), the usage variance splits again:

- **Material Mix Variance (MMV)** = (Revised Standard Quantity − Actual Quantity) × SP
  where **Revised Standard Quantity (RSQ)** = total actual input re-apportioned in the *standard mix ratio*.
  *Meaning:* the cost effect of using inputs in the wrong *proportion* (using more of the cheap material and less of the dear one, or vice versa). Owner: whoever controls the recipe/blend.

- **Material Yield (Sub-usage) Variance (MYV)** = (SQ − RSQ) × SP
  *Meaning:* the cost effect of the total mix producing more or less output than standard — i.e., getting a different *yield* from the same total input. Also expressible as (Actual Yield − Standard Yield from actual input) × Standard cost per unit of output.

  **Check:** MMV + MYV = MUV.

Why RSQ is the pivot: it is the bridge figure that holds *total quantity at actual* but *proportion at standard*. Mix compares actual-proportion vs standard-proportion at the same total (RSQ vs AQ). Yield compares standard-for-output vs standard-proportion-of-actual-total (SQ vs RSQ). One variable changes per step — the golden rule again.

**The purchase-point vs usage-point distinction (finer than most students realise).** There are two philosophies for the price variance:

1. **Price variance at time of purchase** — compute MPV on the quantity *purchased* (AI), so the entire price variance is recognised when material enters stores, and inventory is then carried at *standard* price. Advantage: prices are flagged early, and stock records stay clean at standard. This means purchases and usage quantities can differ (you may buy 6,000 kg but use 5,720 kg), and **MPV then uses 6,000 while MUV uses 5,720** — they no longer share a base, and MPV + MUV ≠ MCV exactly (the difference sits in the closing-stock valuation).
2. **Price variance at time of usage** — compute MPV on quantity *used* (AQ); purchases and usage tie, and MPV + MUV = MCV cleanly. This is the ICAI default when the question does not separate purchase and usage.

Read the wording: the phrase "material *purchased*… material *consumed*" with two different quantities is the examiner signalling the purchase-point method.

### 4.4 Direct Labour Variances

Let `SH` = standard hours **for actual output**, `AH` = actual hours *paid*, `AH_worked` = actual hours *worked* (paid minus idle), `SR` = standard rate, `AR` = actual rate.

- **Labour Cost Variance (LCV)** = (SH × SR) − (AH_paid × AR)
  *Meaning:* total labour cost gap for actual output.

- **Labour Rate Variance (LRV)** = (SR − AR) × AH_paid
  *Meaning:* cost of paying a wrong wage rate. Owner: **HR/personnel.** Computed on hours *paid* because you pay for every paid hour regardless of idleness.

- **Labour Efficiency Variance (LEV)** = (SH − AH_worked) × SR
  *Meaning:* cost of workers taking wrong number of *productive* hours. Owner: **production supervisor.** Uses hours *worked* so idle time doesn't distort efficiency.

- **Idle Time Variance (ITV)** = Idle Hours × SR = (AH_paid − AH_worked) × SR — **always Adverse** (idle time is paid-for, never productive; you can't "gain" from it).
  *Meaning:* cost of paying for hours during which nobody produced (power cut, machine breakdown, material shortage).

  **Check:** LRV + LEV + ITV = LCV.
  (If the question gives no idle time, AH_paid = AH_worked and ITV = 0, collapsing to LRV + LEV = LCV.)

When several **grades of labour** work together, efficiency splits (exactly parallel to materials):

- **Labour Mix (Gang) Variance (LMV)** = (Revised Standard Hours − Actual Hours worked) × SR
- **Labour Yield (Sub-efficiency) Variance (LYV)** = (SH − Revised Standard Hours) × SR

  **Check:** LMV + LYV = LEV.

**A subtlety in the gang: mix uses hours *worked*, not paid.** When idle time and a multi-grade gang appear *together*, the mix and yield variances are built from hours *worked* (RSH is actual *worked* hours in standard grade ratio), because idle time is quarantined into its own variance first. A common exam trap is to feed *paid* hours into the mix calculation and double-count the idle loss. Sequence: strip idle → then split worked hours into mix and yield.

**Two idle-time conventions — read the question.** (a) *Idle time included in the standard* (a normal, expected allowance): then the standard rate already assumes some idle time, and only *abnormal* idle time above the norm is separated. (b) *Idle time not in the standard* (the usual exam case): all idle time becomes an adverse Idle Time Variance. ICAI problems almost always mean (b) and label idle time as abnormal, but the phrase "normal idle time is X%" is your cue that (a) applies and the standard hours must already embed it.

**Why the labour efficiency and material usage variances are cousins, not twins.** Both measure "wrong quantity at standard price". But labour has an extra wrinkle materials lack: *idle time* — you pay for labour hours whether or not they produce, whereas you do not pay for material you never used. That asymmetry is exactly why labour has a third child (idle time) and materials do not. Seeing *why* the trees differ in shape stops you from mechanically hunting for a "material idle variance" that does not exist.

### 4.5 Variable Overhead Variances

Variable OH varies with activity, so it is treated like a "labour-hour-driven" cost. Let `SR_v` = standard variable OH rate per hour, `AH` = actual hours, `SH` = standard hours for actual output, `Actual VOH` = actual variable overhead incurred.

- **Variable OH Cost Variance** = (SH × SR_v) − Actual VOH

- **Variable OH Expenditure (Spending) Variance** = (AH × SR_v) − Actual VOH
  = (Standard variable OH for actual hours) − (Actual variable OH).
  *Meaning:* did each hour of activity cost more/less variable OH than budgeted? A *rate* effect.

- **Variable OH Efficiency Variance** = (SH − AH) × SR_v
  *Meaning:* because variable OH is absorbed per hour, working faster/slower than standard changes VOH absorbed. Mirror of labour efficiency.

  **Check:** Expenditure + Efficiency = VOH Cost Variance.

**Which "AH" for variable overhead — worked or paid?** Variable overhead is consumed only while machines/people are *actively working*, so the VOH efficiency variance uses hours *worked* (like labour efficiency). During idle time no variable overhead is incurred, so idle hours drop out. If a question gives idle time, use `AH_worked` in both the expenditure and efficiency formulas above. (Where there is no idle time, worked = paid and the distinction vanishes — which is why the base formula just says AH.) The deep reason: variable overhead is *activity-driven*; idle time is *absence* of activity.

### 4.6 Fixed Overhead Variances — the subtle one

Fixed OH is a *fixed lump* in reality, but standard costing *absorbs* it per unit at a pre-determined rate. This clash — fixed in fact, unitised in absorption — creates the richest variance family. Definitions:

- **Standard Fixed OH Rate per unit (FOR)** = Budgeted Fixed OH ÷ Budgeted Output.
  (Or per hour = Budgeted Fixed OH ÷ Budgeted Hours.)
- `Absorbed FOH` = Actual output × FOR (= Standard hours for actual output × rate per hour).
- `Budgeted FOH` = the original fixed OH budget.
- `Actual FOH` = fixed OH actually incurred.

Variances:

- **Fixed OH Cost Variance** = Absorbed FOH − Actual FOH
  *Meaning:* total over/under-absorption of fixed overhead.

- **Fixed OH Expenditure (Budget) Variance** = Budgeted FOH − Actual FOH
  *Meaning:* did we *spend* more or less fixed overhead than budgeted? Pure spending. Owner: whoever authorises the fixed spend.

- **Fixed OH Volume Variance** = Absorbed FOH − Budgeted FOH
  *Meaning:* because fixed cost per unit assumes a planned volume, producing more/less than planned over- or under-recovers the fixed lump. Producing *above* budget volume = Favourable (fixed cost spread over more units). This is *not* a spending issue — it is a *capacity utilisation* issue.

  **Check:** Expenditure + Volume = FOH Cost Variance.

Volume splits further:

- **Fixed OH Capacity Variance** = (Actual hours worked − Budgeted hours) × FOR per hour
  *Meaning:* did we run the plant for more/fewer hours than budgeted? Owner: capacity/planning.
  (Some ICAI problems use "revised budgeted hours" adjusting for the number of days actually worked — see Calendar variance.)

- **Fixed OH Efficiency Variance** = (Standard hours for actual output − Actual hours worked) × FOR per hour
  *Meaning:* even at given capacity, working efficiently produces more standard-hours of output, recovering more fixed OH.

- **Fixed OH Calendar Variance** = (Actual working days − Budgeted working days) × Budgeted FOH per day (used only when actual days differ from budget).

  **Check:** Capacity + Efficiency (+ Calendar) = Volume.

```mermaid
flowchart LR
    A["Fixed OH Cost Variance"] --> B["Expenditure Variance"]
    A --> C["Volume Variance"]
    C --> D["Capacity Variance"]
    C --> E["Efficiency Variance"]
    C --> F["Calendar Variance"]
```
*Figure 13.3 — Fixed overhead splits by a different logic than variable: spending vs volume, then volume by capacity, efficiency and calendar.*

**Why fixed overhead alone breeds a volume variance — the deepest "why" in the chapter.** Material, labour and variable overhead all *flex* with output: make more, they cost proportionally more, and there is nothing to "over- or under-recover". Fixed overhead is different — the rent is ₹3,00,000 whether you make 4,000 units or 6,000. But absorption costing *pretends* it is variable by charging a flat FOR per unit. That pretence works only if you actually make the budgeted volume. Make fewer units and you have absorbed less than the lump you must still pay → *under-recovery* → adverse volume variance. The volume variance is literally **the accounting error created by forcing a fixed cost through a per-unit rate.** No fixed cost, no volume variance — which is exactly why marginal costing (which never absorbs fixed cost into units) has *no* volume variance at all.

**The three utilisation ratios (examiners love these alongside FOH variances).** Because volume variance is about *how much of budgeted capacity you actually converted into output*, ICAI often pairs it with three ratios, all built from standard hours:

- **Capacity Ratio** = (Actual hours worked ÷ Budgeted hours) × 100 → did we operate the plant for as many hours as planned?
- **Efficiency Ratio** = (Standard hours for actual output ÷ Actual hours worked) × 100 → within the hours run, did we produce at standard pace?
- **Activity (Volume) Ratio** = (Standard hours for actual output ÷ Budgeted hours) × 100 → overall, did output reach the planned level? Note **Activity Ratio = Capacity Ratio × Efficiency Ratio** (as fractions), mirroring Volume = Capacity + Efficiency in the variances. A ratio above 100% is favourable; below 100% adverse. These ratios and the fixed-OH sub-variances are two languages for the same story.

**Revised budgeted hours and the calendar variance — avoiding the double count.** When the actual number of working days differs from budget, ICAI computes a *revised* budgeted capacity: Revised Budgeted Hours = Budgeted hours per day × *actual* days. The calendar variance captures the day-count effect [(actual − budgeted days) × budgeted FOH per day], and the capacity variance is then measured against the *revised* budgeted hours so the day effect is not counted twice. If you forget to revise, capacity and calendar overlap and the volume reconciliation fails. This is the single most error-prone corner of fixed-OH analysis.

### 4.7 Sales Variances — measuring the revenue/profit side

Cost variances explain why *cost* moved. Sales variances explain why *profit* moved because of selling activity. Two bases exist; ICAI favours the **profit (margin) method**, which is what reconciles budgeted to actual profit. Let `BQ`=budgeted qty, `AQ`=actual qty sold, `BP`=budgeted price, `AP`=actual price, `SM`=standard margin (profit) per unit, `AM`=actual margin per unit.

**Sales Value method (turnover-based):**
- **Sales Value Variance** = (AQ × AP) − (BQ × BP)
- **Sales Price Variance** = (AP − BP) × AQ
- **Sales Volume Variance** = (AQ − BQ) × BP

**Sales Margin (Profit) method — reconciles profit:**
- **Total Sales Margin Variance** = (AQ × AM) − (BQ × SM)
- **Sales Margin Price Variance** = (AM − SM) × AQ = (AP − BP) × AQ *(cost is held at standard, so margin change equals price change)*
- **Sales Margin Volume Variance** = (AQ − BQ) × SM

Volume splits (for multi-product sales), using **RBQ** = Revised Budgeted Quantity = total actual units in budgeted mix ratio:

- **Sales Margin Mix Variance** = (AQ − RBQ) × SM *(sold a different product mix than budgeted)*
- **Sales Margin Quantity (Sub-volume) Variance** = (RBQ − BQ) × SM *(sold a different total quantity)*

  **Check:** Mix + Quantity = Volume; Price + Volume = Total Sales Margin Variance.

**Absorption vs marginal margin — a live exam distinction.** The "standard margin per unit" (SM) can be defined two ways depending on the costing system: under **absorption costing** SM = selling price − *total* standard cost (including absorbed fixed OH); under **marginal costing** SM = *contribution* per unit = selling price − *variable* cost. The volume variance therefore differs numerically between systems — under marginal costing the sales volume variance is valued at **standard contribution**, which is generally the more decision-relevant figure because selling one more unit adds contribution, not the arbitrary fixed-cost slice. The exam expects you to use whichever the question specifies, and to know *why* the marginal version is preferred for decision-making.

**Why the margin price variance equals the value price variance.** Selling price rose by ₹5; standard cost is held constant (it is a *sales* variance, not a cost one); therefore the whole ₹5 drops straight to margin. That is why (AM − SM) = (AP − BP), and the two methods agree on the *price* variance while differing on the *volume* variance (valued at BP under value, at SM/contribution under margin). Understanding this keeps you from computing the price variance twice by two "different" formulas.

### 4.8 The reconciliation statement — the point of it all

The final deliverable is a bridge from **Budgeted Profit** to **Actual Profit**, threading every variance:

> Budgeted Profit
> ± Sales Margin variances (price, mix, quantity)
> = Standard profit on actual sales... then
> ± all Cost variances (material, labour, VOH, FOH)
> = **Actual Profit**

If it lands exactly on actual profit, every variance is correct. This is why examiners love it: it self-checks the entire answer.

**Absorption-costing reconciliation vs marginal-costing reconciliation.** Under **absorption costing** the bridge threads *all* fixed-OH variances (expenditure *and* volume). Under **marginal costing** the fixed-overhead *volume* variance does not exist, so the bridge instead runs from budgeted *contribution* → actual contribution via sales and variable-cost variances, then subtracts the fixed-OH *expenditure* variance (budgeted vs actual fixed cost) to reach actual profit. If a reconciliation refuses to tie, the first thing to check is whether you have mixed a marginal-costing sales volume variance (valued at contribution) with an absorption-costing set of cost variances — a classic self-inflicted mismatch.

## 5. Worked Examples

### Example 1 — Material and Labour, single input (foundational)

**Data.** SamCo makes one product. Standard cost per unit: material 5 kg @ ₹40/kg; labour 3 hours @ ₹50/hour. Budgeted output 1,000 units. **Actual:** 1,100 units produced; 5,720 kg of material used costing ₹2,37,380; 3,410 labour hours paid costing ₹1,74,910 (no idle time).

**Step 1 — Set the "standard for actual output" (flex to 1,100 units).**
- SQ = 1,100 × 5 = **5,500 kg**; SP = ₹40 → standard material cost = 5,500 × 40 = ₹2,20,000.
- SH = 1,100 × 3 = **3,300 hrs**; SR = ₹50 → standard labour cost = 3,300 × 50 = ₹1,65,000.
- AP = 2,37,380 ÷ 5,720 = **₹41.50/kg**; AR = 1,74,910 ÷ 3,410 = **₹51.30/hr**.

**Step 2 — Material variances.**

| Variance | Formula | Working | Result |
|---|---|---|---|
| Cost (MCV) | (SQ×SP) − (AQ×AP) | 2,20,000 − 2,37,380 | ₹17,380 A |
| Price (MPV) | (SP − AP)×AQ | (40 − 41.50)×5,720 | ₹8,580 A |
| Usage (MUV) | (SQ − AQ)×SP | (5,500 − 5,720)×40 | ₹8,800 A |

**Check:** 8,580 A + 8,800 A = 17,380 A = MCV. ✓

**Step 3 — Labour variances (no idle time).**

| Variance | Formula | Working | Result |
|---|---|---|---|
| Cost (LCV) | (SH×SR) − (AH×AR) | 1,65,000 − 1,74,910 | ₹9,910 A |
| Rate (LRV) | (SR − AR)×AH | (50 − 51.30)×3,410 | ₹4,433 A |
| Efficiency (LEV) | (SH − AH)×SR | (3,300 − 3,410)×50 | ₹5,500 A |

**Check:** 4,433 A + 5,500 A = 9,933 A. Rounding in AR (51.30) causes a ₹23 gap; using exact AR = 1,74,910/3,410, LRV = 1,74,910 − 3,410×50 = 1,74,910 − 1,70,500 = ₹4,410 A, and 4,410 + 5,500 = 9,910 A = LCV. ✓
*(Lesson: compute rate variance as Actual cost − AH×SR to avoid rounding the actual rate.)*

**Reading it:** every variance is adverse. Material: paid ₹1.50/kg over and wasted 220 kg. Labour: overpaid ₹0.10-odd per hour and took 110 excess hours. Two managers, four distinct actions.

**Examiner tweak — "material purchased 6,000 kg, used 5,720 kg; price variance at purchase point".** Now the price variance is recognised on the *purchased* quantity: MPV = (SP − AP) × AI = (40 − 41.50) × 6,000 = **₹9,000 A** (AP is unchanged because the actual price per kg is the same on stock bought). The usage variance is unaffected (still ₹8,800 A on the 5,720 kg consumed). Notice MPV + MUV = 9,000 + 8,800 = 17,800 A, which no longer equals the ₹17,380 MCV computed on consumption — the ₹420 gap is the price variance sitting in the 280 kg of closing stock (280 × ₹1.50). *Lesson: under the purchase-point method the neat "Price + Usage = Cost" tie holds only on the quantity consumed; the rest is carried in inventory at standard.*

### Example 2 — Full overheads with idle time (intermediate)

**Data.** Budget for the month: output 5,000 units; each unit takes 2 standard hours. Budgeted fixed OH ₹3,00,000; budgeted variable OH ₹1,50,000. **Actual:** 4,800 units produced; 10,200 hours paid, of which 300 hours idle (power failure); actual fixed OH ₹3,05,000; actual variable OH ₹1,58,000. Budgeted and actual working days both 25 (no calendar variance).

**Step 1 — Rates and standards.**
- Budgeted hours = 5,000 × 2 = 10,000 hrs.
- Standard VOH rate = 1,50,000 ÷ 10,000 = **₹15/hr**. Standard FOH rate = 3,00,000 ÷ 10,000 = **₹30/hr** (= ₹60/unit).
- Actual output 4,800 → **SH = 4,800 × 2 = 9,600 hrs**.
- AH paid = 10,200; **AH worked = 10,200 − 300 = 9,900 hrs**.
- Absorbed FOH = 9,600 × 30 = ₹2,88,000. Budgeted FOH = ₹3,00,000.

**Step 2 — Variable OH.**

| Variance | Formula | Working | Result |
|---|---|---|---|
| VOH Cost | SH×SR_v − Actual | 9,600×15 − 1,58,000 = 1,44,000 − 1,58,000 | ₹14,000 A |
| VOH Expenditure | AH_worked×SR_v − Actual | 9,900×15 − 1,58,000 = 1,48,500 − 1,58,000 | ₹9,500 A |
| VOH Efficiency | (SH − AH_worked)×SR_v | (9,600 − 9,900)×15 | ₹4,500 A |

**Check:** 9,500 A + 4,500 A = 14,000 A = VOH Cost. ✓
*(VOH efficiency uses hours worked; idle hours consume no variable overhead.)*

**Step 3 — Fixed OH.**

| Variance | Formula | Working | Result |
|---|---|---|---|
| FOH Cost | Absorbed − Actual | 2,88,000 − 3,05,000 | ₹17,000 A |
| FOH Expenditure | Budgeted − Actual | 3,00,000 − 3,05,000 | ₹5,000 A |
| FOH Volume | Absorbed − Budgeted | 2,88,000 − 3,00,000 | ₹12,000 A |
| FOH Capacity | (AH_worked − Budgeted hrs)×FOR | (9,900 − 10,000)×30 | ₹3,000 A |
| FOH Efficiency | (SH − AH_worked)×FOR | (9,600 − 9,900)×30 | ₹9,000 A |

**Checks:** Expenditure 5,000 A + Volume 12,000 A = 17,000 A = FOH Cost. ✓
Capacity 3,000 A + Efficiency 9,000 A = 12,000 A = Volume. ✓
*(We ran 100 hours short of budgeted capacity — that's the capacity loss — and within the hours we ran, we were inefficient by 300 hours — that's the efficiency loss. Volume shortfall is the sum.)*

**Step 4 — Labour idle-time slice (illustration).** If SR = ₹50: Idle Time Variance = 300 × 50 = **₹15,000 A**, always adverse, quarantined from efficiency. This ensures the power-failure cost lands on facilities, not on the workers' efficiency record.

**Step 5 — Control ratios cross-check.** Capacity Ratio = 9,900 ÷ 10,000 = **99%**; Efficiency Ratio = 9,600 ÷ 9,900 = **96.97%**; Activity Ratio = 9,600 ÷ 10,000 = **96%**. Confirm: 99% × 96.97% ≈ 96% = Activity Ratio ✓, matching Capacity + Efficiency = Volume. All below 100%, i.e. all adverse — the same verdict as the rupee variances, in ratio language.

**Examiner tweak — calendar variance.** Suppose budget assumed 25 working days but a public-holiday cut actuals to 24 days, budgeted FOH per day = 3,00,000 ÷ 25 = ₹12,000. Then Calendar Variance = (24 − 25) × 12,000 = **₹12,000 A**, and Revised Budgeted Hours = (10,000 ÷ 25) × 24 = 9,600 hrs, so Capacity Variance is re-measured as (AH_worked − Revised budgeted hrs) × FOR = (9,900 − 9,600) × 30 = **₹9,000 F**. Now Capacity 9,000 F + Efficiency 9,000 A + Calendar 12,000 A = **12,000 A = Volume** ✓ — the same volume total, re-attributed: the lost day (calendar) is separated from how hard we ran the *available* days (capacity).

### Example 3 — Multi-material mix & yield with full reconciliation (exam-hard)

**Data.** A chemical "Zenol" is made by mixing three materials. Standard mix for 100 kg of output:

| Material | Std qty (kg) | Std price ₹/kg | Std cost ₹ |
|---|---|---|---|
| A | 50 | 20 | 1,000 |
| B | 30 | 30 | 900 |
| C | 40 | 10 | 400 |
| **Input total** | **120** | | **2,300** |
| Less: normal loss 20% | (20) | | |
| **Output** | **100** | | **2,300** |

Standard cost per kg of output = 2,300 ÷ 100 = ₹23.

**Actual (one batch):** Output 4,750 kg of Zenol. Materials consumed:

| Material | Actual qty (kg) | Actual price ₹/kg | Actual cost ₹ |
|---|---|---|---|
| A | 2,900 | 21 | 60,900 |
| B | 1,600 | 28 | 44,800 |
| C | 1,300 | 12 | 15,600 |
| **Total input** | **5,800** | | **1,21,300** |

**Step 1 — Standard quantity for actual output (SQ).** For 4,750 kg output at standard input ratio (120 kg input per 100 kg output):
- Total std input = 4,750 × 120/100 = 5,700 kg, split 50:30:40 of 120.
- SQ(A) = 5,700 × 50/120 = 2,375 kg; SQ(B) = 5,700 × 30/120 = 1,425 kg; SQ(C) = 5,700 × 40/120 = 1,900 kg.

Standard cost of actual output = 4,750 × 23 = **₹1,09,250** (cross-check: 2,375×20 + 1,425×30 + 1,900×10 = 47,500 + 42,750 + 19,000 = 1,09,250 ✓).

**Step 2 — Revised Standard Quantity (RSQ)** = actual total input (5,800) in standard ratio 50:30:40 (of 120):
- RSQ(A) = 5,800 × 50/120 = 2,416.67 kg
- RSQ(B) = 5,800 × 30/120 = 1,450.00 kg
- RSQ(C) = 5,800 × 40/120 = 1,933.33 kg

**Step 3 — Material Cost Variance** = Std cost of output − Actual cost = 1,09,250 − 1,21,300 = **₹12,050 A**.

**Step 4 — Price Variance** = Σ(SP − AP)×AQ:

| Material | (SP − AP) | ×AQ | Result |
|---|---|---|---|
| A | (20 − 21) = −1 | ×2,900 | 2,900 A |
| B | (30 − 28) = +2 | ×1,600 | 3,200 F |
| C | (10 − 12) = −2 | ×1,300 | 2,600 A |
| **MPV** | | | **₹2,300 A** |

**Step 5 — Usage Variance** = Σ(SQ − AQ)×SP:

| Material | (SQ − AQ) | ×SP | Result |
|---|---|---|---|
| A | (2,375 − 2,900) = −525 | ×20 | 10,500 A |
| B | (1,425 − 1,600) = −175 | ×30 | 5,250 A |
| C | (1,900 − 1,300) = +600 | ×10 | 6,000 F |
| **MUV** | | | **₹9,750 A** |

**Check:** MPV 2,300 A + MUV 9,750 A = **12,050 A = MCV.** ✓

**Step 6 — Mix Variance** = Σ(RSQ − AQ)×SP:

| Material | (RSQ − AQ) | ×SP | Result |
|---|---|---|---|
| A | (2,416.67 − 2,900) = −483.33 | ×20 | 9,666.67 A |
| B | (1,450.00 − 1,600) = −150.00 | ×30 | 4,500.00 A |
| C | (1,933.33 − 1,300) = +633.33 | ×10 | 6,333.33 F |
| **MMV** | | | **₹7,833.33 A** |

**Step 7 — Yield Variance** = Σ(SQ − RSQ)×SP:

| Material | (SQ − RSQ) | ×SP | Result |
|---|---|---|---|
| A | (2,375 − 2,416.67) = −41.67 | ×20 | 833.33 A |
| B | (1,425 − 1,450.00) = −25.00 | ×30 | 750.00 A |
| C | (1,900 − 1,933.33) = −33.33 | ×10 | 333.33 A |
| **MYV** | | | **₹1,916.67 A** |

**Check:** MMV 7,833.33 A + MYV 1,916.67 A = **9,750 A = MUV.** ✓

**Interpreting the story:** The batch overspent ₹12,050. Of that, ₹2,300 was a *price* problem (paid more for A and C, partly rescued by cheaper B), and ₹9,750 was a *usage* problem. Digging into usage: ₹7,833 came from a *wrong blend* — we loaded far more of the expensive materials A and B and skimped on the cheap C, a costly mis-mix — while ₹1,917 came from a *poor yield* (5,800 kg of input yielded only 4,750 kg vs the standard 4,833 kg it should have yielded, i.e. 5,800×100/120). Two very different corrections: fix the recipe discipline (mix) and investigate process loss (yield).

*Yield cross-check:* standard output from 5,800 kg input = 5,800 × 100/120 = 4,833.33 kg; actual = 4,750 kg; shortfall 83.33 kg × ₹23 = **₹1,916.67 A** — matches MYV exactly. ✓

**Examiner tweak — the "single weighted standard price" shortcut for yield.** Instead of the material-by-material yield table, the yield variance can be got in one line: MYV = (Standard output from actual input − Actual output) × Standard cost per unit of output = (4,833.33 − 4,750) × 23 = 83.33 × 23 = **₹1,916.67 A**. This is faster under time pressure and is what the *cross-check* above uses — but it only works because *all three materials scale together in the yield step* (SQ − RSQ is the same proportion across materials). If asked to "show mix and yield material-wise", you still need the tables; if merely asked for the yield figure, the one-liner suffices. Knowing both saves minutes.

### Example 4 — Sales margin variances and profit reconciliation (capstone)

**Data.** A firm budgets two products:

| Product | Budget qty | Std profit/unit ₹ | Budget profit ₹ |
|---|---|---|---|
| X | 600 | 40 | 24,000 |
| Y | 400 | 60 | 24,000 |
| **Total** | **1,000** | | **48,000** |

**Actual:** X sold 700 units at a margin of ₹35/unit; Y sold 500 units at a margin of ₹58/unit.

**Step 1 — Actuals.** Actual profit = 700×35 + 500×58 = 24,500 + 29,000 = **₹53,500.**

**Step 2 — RBQ** (total actual 1,200 units in budget ratio 600:400 = 60:40):
- RBQ(X) = 1,200 × 60/100 = 720; RBQ(Y) = 1,200 × 40/100 = 480.

**Step 3 — Sales Margin Price Variance** = (AM − SM)×AQ:
- X: (35 − 40)×700 = 3,500 A; Y: (58 − 60)×500 = 1,000 A → **₹4,500 A.**

**Step 4 — Sales Margin Volume Variance** = (AQ − BQ)×SM:
- X: (700 − 600)×40 = 4,000 F; Y: (500 − 400)×60 = 6,000 F → **₹10,000 F.**

**Step 5 — split Volume into Mix and Quantity.**
- **Mix** = (AQ − RBQ)×SM: X (700−720)×40 = 800 A; Y (500−480)×60 = 1,200 F → **₹400 F.**
- **Quantity** = (RBQ − BQ)×SM: X (720−600)×40 = 4,800 F; Y (480−400)×60 = 4,800 F → **₹9,600 F.**

**Check:** Mix 400 F + Quantity 9,600 F = **10,000 F = Volume.** ✓

**Step 6 — Total Sales Margin Variance** = Price 4,500 A + Volume 10,000 F = **₹5,500 F.**
Cross-check: Actual profit 53,500 − Budget profit 48,000 = 5,500 F. ✓ *(Since only selling-side data given, cost variances are nil here.)*

**Step 7 — Reconciliation Statement.**

| Item | ₹ | ₹ |
|---|---|---|
| **Budgeted Profit** | | 48,000 |
| Sales Margin Price Variance | 4,500 A | |
| Sales Margin Mix Variance | 400 F | |
| Sales Margin Quantity Variance | 9,600 F | +5,500 |
| **Actual Profit** | | **53,500** |

Lands exactly on ₹53,500. The reconciliation *is* the proof.

**Examiner tweak — sales *value* method on the same data.** Suppose instead the question gives budgeted selling prices (X ₹200, Y ₹300) and actual prices (X ₹195, Y ₹296), asking for value-based variances. Sales Price Variance = (AP − BP)×AQ = (195−200)×700 + (296−300)×500 = 3,500 A + 2,000 A = **₹5,500 A**. Sales Volume Variance (at BP) = (700−600)×200 + (500−400)×300 = 20,000 F + 30,000 F = **₹50,000 F**. These *turnover* figures look nothing like the margin figures and — critically — **do not reconcile to profit**, because they ignore the cost of the extra units sold. Only the margin method threads into the profit reconciliation. The trap: a question that mixes value-based volume with a profit reconciliation will never tie; spot which method is demanded from the phrase "reconcile budgeted and actual *profit*" (→ margin method).

### Example 5 — Labour gang with idle time, mix and yield (exam-hard)

**Data.** A job is standard-manned by a gang: 4 skilled @ ₹80/hr and 2 unskilled @ ₹50/hr, working a standard 40-hour week to produce 100 standard units. **Actual for one week:** the gang produced 108 units; hours *paid* — skilled 170, unskilled 90; of which 10 skilled hours and 5 unskilled hours were *idle* (machine breakdown). Actual wages: skilled ₹14,110, unskilled ₹4,680.

**Step 1 — Standards.** Standard gang hours per 100 units: skilled 4×40 = 160, unskilled 2×40 = 80, total 240 hrs → standard 2.4 gang-hours per unit. For 108 units: **SH(skilled) = 160×108/100 = 172.8; SH(unskilled) = 80×108/100 = 86.4** (total SH = 259.2). SR skilled ₹80, unskilled ₹50.

**Step 2 — Hours worked (strip idle).** Skilled worked = 170 − 10 = 160; unskilled worked = 90 − 5 = 85; total worked = 245. Actual rates: AR skilled = 14,110 ÷ 170 = ₹83; unskilled = 4,680 ÷ 90 = ₹52.

**Step 3 — Rate Variance** = (SR − AR) × AH_paid:
- Skilled (80 − 83)×170 = 510 A; Unskilled (50 − 52)×90 = 180 A → **₹690 A.**

**Step 4 — Idle Time Variance** = idle hrs × SR:
- Skilled 10×80 = 800 A; Unskilled 5×50 = 250 A → **₹1,050 A** (always adverse).

**Step 5 — Efficiency Variance** = (SH − AH_worked) × SR:
- Skilled (172.8 − 160)×80 = 1,024 F; Unskilled (86.4 − 85)×50 = 70 F → **₹1,094 F.**

**Step 6 — Labour Cost Variance** (parent) = (SH×SR) − (AH_paid×AR):
- Standard cost = 172.8×80 + 86.4×50 = 13,824 + 4,320 = 18,144; Actual = 14,110 + 4,680 = 18,790 → **₹646 A.**

**Check:** Rate 690 A + Idle 1,050 A + Efficiency 1,094 F = 646 A = LCV. ✓

**Step 7 — Split efficiency into Mix and Yield** (on hours *worked*, total 245 in standard ratio 160:80 = 2:1):
- RSH(skilled) = 245 × 160/240 = 163.33; RSH(unskilled) = 245 × 80/240 = 81.67.
- **Mix** = (RSH − AH_worked) × SR: skilled (163.33 − 160)×80 = 266.67 F; unskilled (81.67 − 85)×50 = 166.67 A → **₹100 F.**
- **Yield** = (SH − RSH) × SR: skilled (172.8 − 163.33)×80 = 757.33 F; unskilled (86.4 − 81.67)×50 = 236.67 F → **₹994 F.**

**Check:** Mix 100 F + Yield 994 F = **1,094 F = Efficiency.** ✓

**Reading it:** The gang cost ₹646 more than standard — but that hides a strong story. Rates were higher (₹690 A, an HR matter) and a breakdown wasted 15 paid hours (₹1,050 A, a maintenance matter), yet the crew was genuinely *efficient*: they turned 245 worked hours into 108 units when standard would need 259.2 hours — a ₹1,094 F efficiency gain, of which ₹994 was superior yield (more output per worked hour) and only ₹100 came from a marginally cheaper mix. Three managers, three verdicts, from one ₹646 figure.

## 6. Presentation / Format

Examiners award marks for *structure*, not just answers. Standard layout:

1. **Working Note 1 — Standard cost card** and the flexed "standard for actual output" figures (SQ, SH).
2. **Working Note 2 — Basic actuals** (AP, AR derived; AH worked vs paid; RSQ/RBQ).
3. **Variance computations**, each labelled with F/A, grouped material → labour → VOH → FOH → sales.
4. **Verification lines** after each family: "Price + Usage = Cost ✓".
5. **Reconciliation Statement** from budgeted to actual profit.

Always write the **F or A** tag — a variance without its direction is worth zero. Present the reconciliation vertically with a clear running total. Show RSQ/RBQ as an explicit working; markers look for it in mix/yield questions.

**Time-management order for a full 15-mark variance question.** (i) First build the two working notes — SQ/SH and AP/AR/RSQ — because *every* variance draws on them; a mistake here poisons the whole answer. (ii) Compute the *parent* cost variances (MCV, LCV, overhead cost variances) directly from totals — they are quick and give you the reconciliation targets. (iii) Compute the children, then run each check line *immediately*; catching a break at the child stage costs one line, catching it at the reconciliation costs a re-do. (iv) Leave the reconciliation statement to last as the capstone. If time runs out, a correct set of *parent* variances plus stated formulas earns more than a half-finished mix/yield table.

```mermaid
flowchart TD
    A["Budgeted Profit"] --> B["Add or less Sales Margin Variances"]
    B --> C["Standard Profit on Actual Sales"]
    C --> D["Add or less Material Variances"]
    D --> E["Add or less Labour Variances"]
    E --> F["Add or less Overhead Variances"]
    F --> G["Actual Profit"]
```
*Figure 13.4 — The operating-profit reconciliation walk: start at plan, thread every variance, land on actual.*

## 7. Connections

- **Marginal costing (Ch. 14) & CVP:** the *sales margin* method uses contribution/profit per unit — under marginal costing the sales volume variance is valued at **standard contribution**, and there is **no fixed OH volume variance** (fixed cost isn't absorbed into units). Know which system the question assumes.
- **Overheads & absorption (Ch. 04):** the FOH volume variance is exactly the "over/under-absorption" of Chapter 04, now *decomposed* into capacity, efficiency and calendar.
- **Budgetary control (Ch. 15):** flexible budgets supply the "budgeted for actual output" figures; standard costing is budgetary control at the per-unit level.
- **Material & labour costing (Ch. 02–03):** standard quantities come from the bill of materials; standard hours from time study.
- **Responsibility accounting:** each variance maps to a responsibility centre — the whole point of decomposition.
- **Process costing (Ch. 10):** the mix/yield split maps directly onto normal-loss/abnormal-loss thinking — the yield variance *is* the cost value of abnormal process loss/gain, valued at standard cost per unit of output.
- **Cost accounting standards / integral accounts:** under a standard cost *ledger*, variances are posted to dedicated variance accounts and closed to costing P&L, which is why clean reconciliation matters beyond the exam.

## 8. Traps & Examiner Tricks

1. **Flexing to the wrong output.** SQ and SH must be based on **actual output**, never budgeted output. Using budgeted quantity is the single most common fatal error.
2. **Hours paid vs hours worked.** Rate variance and idle-time use **hours paid**; efficiency uses **hours worked**. Swap them and both go wrong. When idle time exists, LEV must exclude it.
3. **Idle time is always Adverse.** Never favourable. If your formula yields a favourable idle variance, you've mis-signed.
4. **Price variance on purchases vs usage.** If purchase quantity ≠ usage quantity and the question isolates price at purchase point, compute MPV on quantity *purchased*; otherwise on quantity used. Read the wording.
5. **FOH volume is not a spending variance.** Producing less than budget gives an adverse *volume* variance even if you spent exactly the budget — it's under-*recovery*, not over-*spending*. Students wrongly call it wasteful.
6. **Mix vs Yield direction.** Mix uses (RSQ − AQ); Yield uses (SQ − RSQ). Getting the pivot RSQ wrong (must be *actual total* in *standard* ratio) breaks both. RSQ total = AQ total; if they don't match, recompute.
7. **Sales price sign flips.** For sales, favourable = actual *exceeds* budget. Don't carry the cost convention (std − actual) into sales.
8. **Sales value vs sales margin method.** They give different volume variances (BP vs SM). Only the *margin* method reconciles to profit. Use the method the question demands.
9. **Rounding the actual rate.** Compute rate/price variances as (Actual cost − AQ×SP) to sidestep rounding of AP/AR (see Example 1's ₹23 discrepancy).
10. **Calendar variance double-count.** Only include it when actual days ≠ budgeted days; then capacity variance uses *revised* budgeted hours to avoid double counting.
11. **Reconciliation not tying.** If budgeted profit + variances ≠ actual profit, a sign is flipped somewhere. Treat the mismatch as a diagnostic, not a rounding excuse.
12. **Wrong FOR base.** Fixed OH *rate* must be computed on the *budgeted* activity (budgeted output or budgeted hours), never on actual or standard-for-actual. Dividing budgeted FOH by actual hours silently rebuilds the whole fixed-OH family wrong.
13. **Mixing marginal and absorption in one answer.** A sales volume variance valued at *contribution* (marginal) cannot be reconciled against a cost set that includes a fixed-OH *volume* variance (absorption). Pick one system for the whole question.
14. **Standard for actual output vs actual quantity in mix.** In mix/yield, SQ is the standard input for the *output achieved*, while RSQ is the standard-ratio split of *actual input*. Confusing the two totals (output-based vs input-based) is the classic mix/yield wipeout.
15. **Efficiency measured at the wrong price.** Fixed-OH efficiency uses FOR (per hour); labour efficiency uses SR; VOH efficiency uses SR_v. They are three *different* rates on the *same* hour deviation (SH − AH_worked); using one rate for another double-books or mis-values the hour.
16. **Treating an uncontrollable variance as a performance failure.** A market-wide price surge is an adverse price variance but is *not* the purchase manager's failing. Marks are lost when the "responsibility" comment blames the wrong person or ignores controllability.

## 9. First-Principles Recap

Strip everything away and one sentence remains: **a variance isolates the cost effect of changing exactly one input factor while holding the others at standard.** Price factors are valued at *actual quantity* (you paid the wrong price on what you actually used); quantity factors are valued at *standard price* (so the price story cannot leak into the efficiency story). The reason for that exact asymmetry is the *joint variance*: when both price and quantity move together, their interaction has to be parked somewhere, and the two-variance convention buries it inside the price variance — which is precisely why the price formula carries *actual* quantity. Mix and yield are just "quantity" split once more, pivoting on RSQ = actual total held in standard proportions. Fixed overhead is the odd one out only because a genuinely fixed cost is being forced through a per-unit rate, so a *volume* variance is born — the price you pay for pretending a fixed cost is variable per unit; and volume splits again into how many hours you ran (capacity), how hard you ran them (efficiency), and how many days you had (calendar). Sales flips the sign because more revenue is good — the true master rule being *favourable = increases profit*. And every parent equals the sum of its children, which is why the reconciliation statement, landing precisely on actual profit, proves the entire analysis in one line. Memorise nothing; hold quantity or price fixed and rebuild each formula on demand.

## 10. Quick-Revision Sheet

**Convention:** Cost variances = (Standard − Actual); positive = Favourable. Sales = (Actual − Budget). SQ/SH always for **actual output**. Master rule: Favourable = the movement *increases profit*.

**Three-column skeleton (material / labour / VOH):** ① SQ×SP · ② AQ×SP · ③ AQ×AP → Usage/Efficiency = ①−②, Price/Rate = ②−③, Cost = ①−③.

| # | Variance | Formula |
|---|---|---|
| **Material** | | |
| 1 | Cost (MCV) | (SQ×SP) − (AQ×AP) |
| 2 | Price (MPV) | (SP − AP) × AQ |
| 3 | Usage (MUV) | (SQ − AQ) × SP |
| 4 | Mix (MMV) | (RSQ − AQ) × SP |
| 5 | Yield (MYV) | (SQ − RSQ) × SP |
| | *Check* | MPV+MUV=MCV; MMV+MYV=MUV |
| **Labour** | | |
| 6 | Cost (LCV) | (SH×SR) − (AH_paid×AR) |
| 7 | Rate (LRV) | (SR − AR) × AH_paid |
| 8 | Efficiency (LEV) | (SH − AH_worked) × SR |
| 9 | Idle Time (ITV) | Idle hrs × SR (always A) |
| 10 | Mix/Gang (LMV) | (RSH − AH_worked) × SR |
| 11 | Yield (LYV) | (SH − RSH) × SR |
| | *Check* | LRV+LEV+ITV=LCV; LMV+LYV=LEV |
| **Variable OH** | | |
| 12 | Cost | (SH×SR_v) − Actual VOH |
| 13 | Expenditure | (AH×SR_v) − Actual VOH |
| 14 | Efficiency | (SH − AH) × SR_v |
| | *Check* | Exp+Eff=Cost |
| **Fixed OH** | | |
| 15 | Cost | Absorbed − Actual |
| 16 | Expenditure (Budget) | Budgeted − Actual |
| 17 | Volume | Absorbed − Budgeted |
| 18 | Capacity | (AH_worked − Budgeted hrs) × FOR |
| 19 | Efficiency | (SH − AH_worked) × FOR |
| 20 | Calendar | (Actual − Budgeted days) × FOH/day |
| | *Check* | Exp+Vol=Cost; Cap+Eff+Cal=Vol |
| **Sales (Margin)** | | |
| 21 | Total Margin | (AQ×AM) − (BQ×SM) |
| 22 | Price | (AM − SM) × AQ |
| 23 | Volume | (AQ − BQ) × SM |
| 24 | Mix | (AQ − RBQ) × SM |
| 25 | Quantity | (RBQ − BQ) × SM |
| | *Check* | Price+Vol=Total; Mix+Qty=Vol |
| **Sales (Value)** | | |
| 26 | Value | (AQ×AP) − (BQ×BP) |
| 27 | Price | (AP − BP) × AQ |
| 28 | Volume | (AQ − BQ) × BP |

**Control ratios:** Capacity = AH_worked ÷ Budgeted hrs; Efficiency = SH ÷ AH_worked; Activity = SH ÷ Budgeted hrs = Capacity × Efficiency. Above 100% = F.

**Key figures:** RSQ = actual total input × standard mix ratio. RBQ = actual total sales × budget mix ratio. FOR = Budgeted FOH ÷ Budgeted output (or hours). Absorbed FOH = actual output × FOR. Revised budgeted hours = budgeted hrs/day × actual days (calendar cases).

**Reconciliation:** Budgeted Profit ± Sales margin variances ± Material ± Labour ± VOH ± FOH = **Actual Profit** (must tie exactly). Marginal costing: no FOH volume variance; sales volume valued at contribution; subtract only FOH expenditure variance.
