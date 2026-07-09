<!-- v2-deep -->

# Chapter 28 — AS 28: Impairment of Assets

## 1. The Problem

You already know how the balance sheet handles a machine. You bought it for ₹10,00,000, you expect it to last 10 years, so you write off ₹1,00,000 a year through depreciation (AS 10). After 4 years its book value — its *carrying amount* — sits at ₹6,00,000. Clean, orderly, predictable.

Now watch what depreciation *cannot* see.

**Scenario A — the technology dies overnight.** Your machine makes a specific automotive part. In year 4, the manufacturer redesigns the car and the part is discontinued. Nobody wants what this machine produces. It can generate almost no future cash. Yet the depreciation schedule cheerfully insists the asset is worth ₹6,00,000, and will keep insisting so for six more years. Depreciation spreads cost over time on a *pre-set formula*. It has no eyes. It does not know the world changed.

**Scenario B — the market collapses.** You have a plot of land (never depreciated) bought for ₹50,00,000. A new law bans commercial construction in that zone. Land like yours now sells for ₹15,00,000. The balance sheet still shows ₹50,00,000.

**Scenario C — the plant is damaged.** A flood corrodes a production line. It still runs, but at 40% capacity and with constant breakdowns. Its remaining cash-earning power has been gutted, but depreciation marches on unchanged.

Here is the accounting crime hiding in all three: **the balance sheet is overstating an asset.** An asset, by definition, is a resource expected to give *future economic benefits*. If those benefits have silently shrunk below the carrying amount, then the number on the balance sheet is a lie — it promises benefits the asset can no longer deliver. Investors relying on that number are misled. Profits of past years were overstated (we under-charged expense). The **prudence** concept — do not overstate assets, do not anticipate profit — is being violated.

Depreciation answers the question *"how do I spread a known cost over useful life?"* It was never built to answer *"has this asset suddenly lost value beyond the normal wear I already planned for?"* That second question needs its own machinery. That machinery is **AS 28 — Impairment of Assets**.

Notice *why* depreciation is structurally blind here. Depreciation is decided **once, at acquisition**, on three inputs — cost, estimated useful life, estimated residual value — and then runs on autopilot. It is a *cost-allocation* device, not a *valuation* device. It answers "how much of what I already paid belongs to this year?" It never re-asks "is the remaining balance still worth carrying?" Impairment is the opposite: it is a *point-in-time valuation* re-test that looks at the outside world *today*. That is the deep distinction the examiner keeps probing — depreciation is backward-looking cost allocation; impairment is forward-looking value verification. The two are complementary, never substitutes: even a fully-up-to-date depreciation schedule can sit on top of a badly impaired asset.

There is also a subtle *timing* point. An impairment can strike an asset that is **brand new** — bought last month, barely depreciated — if the world turns against it. So "the asset is nearly new, it can't be impaired" is a false instinct. Age and impairment are independent. A ₹1 crore custom machine that the customer cancels the day after installation is impaired on day one.

The one-sentence problem AS 28 exists to solve: **How do we detect, measure, and record a sudden or unexpected fall in an asset's value that ordinary depreciation would never catch — so that no asset is ever carried at more than the cash it can actually generate?**

## 2. The Core Idea (Analogy)

Think of an asset as an **investment that must justify its shelf-value by what you can still get out of it.**

Imagine you own a second-hand delivery van, recorded in your personal ledger at ₹3,00,000. A friend asks, "Is it really worth three lakh?" You'd sanity-check two escape routes:

1. **Sell it.** What would a buyer pay you today, minus the cost of advertising and paperwork? Say ₹2,20,000. Call this its **net selling price**.
2. **Keep using it.** How much cash will it earn me over its remaining life — deliveries, fees — brought back to today's value? Say ₹2,60,000. Call this its **value in use**.

A rational owner does whichever is better. You would *not* sell for ₹2,20,000 when keeping it is worth ₹2,60,000 to you. So the van is really worth **₹2,60,000 — the higher of the two** — because that is the most you can *recover* from it. This "best of your two options" figure is the **recoverable amount**.

Now compare: ledger says ₹3,00,000, but you can only recover ₹2,60,000. The van is **impaired by ₹40,000**. Honesty demands you write it down to ₹2,60,000 and book a ₹40,000 loss.

That is the *entire* logic of AS 28 in one picture. An asset must never be carried above what a rational owner could recover from it, and recoverable amount is the **higher of what you'd get by selling and what you'd get by using** — because that is what a sensible owner would actually do.

Extend the analogy to see two hidden depths the exam loves:

- **The floor of ₹0 and "why not negative?"** Suppose the van is a wreck — nobody will buy it (NSP = 0) and running it now *costs* more fuel and repair than it earns (VIU would be negative). Recoverable amount is then **zero**, not negative, because you always have the free option to simply *abandon* it and stop the bleeding. An asset can be written down to nil but never below nil — you cannot be forced to keep losing money on something you can walk away from. That is why "highest of NSP, VIU, and **zero**" appears later in the CGU floor rule.
- **Why you needn't always compute both routes.** If the van's sale price alone (₹2,20,000... imagine instead ₹3,10,000) already exceeds the ledger's ₹3,00,000, you can *stop* — it is not impaired, and computing value in use would be wasted effort. You only need the harder second number when the first one you looked at falls short of carrying amount.

```mermaid
flowchart TD
    A["Asset on balance sheet at Carrying Amount"] --> B["What can I actually recover from it?"]
    B --> C["Option 1: SELL it now = Net Selling Price"]
    B --> D["Option 2: KEEP using it = Value in Use"]
    C --> E["Recoverable Amount = HIGHER of the two"]
    D --> E
    E --> F["Is Carrying Amount greater than Recoverable Amount?"]
    F -->|Yes| G["Impaired -- write down, book loss"]
    F -->|No| H["Fine -- leave it alone"]
```
*Every impairment test is just this rational-owner sanity check: never carry an asset above the best of sell-or-use.*

## 3. Why It's Built This Way

Three design choices in AS 28 look arbitrary until you see the problem each one closes.

**Why "higher of" and not "lower of"?** This is the question that trips everyone, because inventory (AS 2) uses *lower of* cost and net realisable value, and students blur the two. The difference is about *what you are measuring and why*.

- Inventory is held **to sell**. Its whole purpose is one exit route — the market. So its economic value can't exceed what the market gives you; lower-of is prudent there.
- A fixed asset is held **to be used**, and *selling is only a fallback*. The owner controls the decision. A rational owner will pick the route — sell or use — that yields **more**. Recoverable amount must reflect the *best available* outcome, because that is genuinely what the asset can recover for the entity. If we forced "lower of," we'd write assets down below what the owner can truly get, which *understates* assets and *overstates* the impairment loss — itself a distortion. Accounting wants faithful representation, not maximum pessimism.

The subtlety: prudence says "don't *overstate*." It does **not** say "understate as hard as you can." Recoverable amount = higher of the two escape routes is the *most* the asset is worth to the entity, and we cap the balance sheet at that. That is exactly enough prudence and no more.

A sharper way to see it: NSP and VIU are two *independent estimates of the same underlying thing* — the asset's recoverable value — computed by two different methods. When you have two honest estimates of one quantity and you want the *true recoverable* value, you don't average them and you don't take the pessimistic one; you take the route the owner will actually choose, which is the better one. The lower figure would describe a decision no rational owner would make (selling when using is worth more, or vice-versa).

**Why an "indicator" trigger instead of testing every asset every year?** Testing recoverable amount is expensive — you'd have to estimate future cash flows, discount rates, market prices for every machine annually. That's disproportionate. So AS 28 says: at each balance sheet date, just *scan for warning signs* (indicators). Only if a red flag appears do you run the full test. It's a cheap smoke-detector triggering an expensive fire-brigade only when needed. (Ind AS 36 forces an annual test for goodwill and indefinite-life intangibles; ICAI AS 28 does **not** — under AS 26 goodwill/intangibles are amortised, so the pure indicator approach suffices. Flag this contrast; it's an examiner favourite.)

This is the accounting expression of a **cost-benefit / materiality** trade-off. The standard-setter is buying *reasonable assurance* that no material overstatement survives, not *perfect certainty*. Indicators are chosen to be the observable, low-cost symptoms that almost always precede a real loss of value — like checking for smoke rather than dismantling the building to look for embers.

**Why the Cash Generating Unit concept?** Value in use needs *future cash flows from the asset*. But many assets don't earn cash on their own. A conveyor belt inside a factory earns nothing by itself — the *whole factory* earns cash. You cannot isolate "the belt's revenue." So AS 28 says: when an individual asset can't generate independent cash inflows, group it with the smallest cluster of assets that *can*, test *that* cluster's recoverable amount, and allocate any impairment back down. That smallest independent cash-earning cluster is the **Cash Generating Unit (CGU)**. It exists purely because value-in-use is meaningless for an asset that doesn't independently earn.

There is a first-principles test buried in the word *"largely independent."* Ask: if I shut this asset (or group) down, does a *distinct, separately measurable* stream of cash inflows stop? If yes, it is (or contains) a CGU. If the cash it feeds is inseparable from a bigger pool, it is only *part* of a larger CGU. The unit boundary is drawn by the **inflows**, not by how management happens to organise costs or departments — a favourite examiner nuance.

**Why allow reversal?** Depreciation is a one-way ratchet, but impairment is a *judgement about current conditions*. If the condition that caused the write-down reverses — the banned zone is re-opened, the discontinued part comes back into demand — then continuing to carry the asset at the depressed value would *understate* it. So AS 28 permits reversal (with one big exception, goodwill), because the whole point is to keep carrying amount *truthful*, not to punish the asset permanently.

Contrast this with **AS 10 revaluation and with depreciation**, both of which are *not* freely reversed, and you see the logic: impairment is a correction of an *estimate about recoverable value*, and estimates get revised when facts change (AS 5 spirit). It is not a policy choice or a cost allocation, so symmetry — reverse when the estimate improves — is the honest treatment. The single asymmetry (goodwill) exists only because reversing it would smuggle in internally generated goodwill.

## 4. Full Technical Content (Recognition, Measurement, Presentation, Disclosure)

### 4.1 Scope — where AS 28 applies and where it doesn't

AS 28 applies to **all assets** *except* those covered by other standards' own valuation rules, because it would be double-regulation. Carved out:

| Excluded asset | Governed instead by |
|---|---|
| Inventories | AS 2 |
| Assets from construction contracts | AS 7 |
| Financial assets / investments | AS 13 |
| Deferred tax assets | AS 22 |

So AS 28 mainly bites on **fixed assets (AS 10), intangible assets (AS 26), and goodwill.**

The unifying principle behind the carve-outs: each excluded item **already has its own "don't overstate" mechanism** built into its home standard — inventory has lower-of-cost-and-NRV (AS 2), investments have their own diminution rules (AS 13), construction-contract assets are measured under AS 7's recognition logic, and DTAs carry a "reasonable/virtual certainty of realisation" recognition test (AS 22). Applying AS 28 on top would be redundant regulation. Whenever an examiner lists a mixed bag of assets and asks "which are within AS 28's scope," reason from this: *does the asset already have a valuation-cap rule of its own?* If yes, it's out.

Two clarifications students miss:
- **Investment property** and other AS 10 items *are* within scope (they are not AS 13 "investments" in the financial-asset sense unless classified so — verify treatment against current ICAI material for the relevant asset).
- The exclusions are about the *asset*, not the *entity*. A manufacturing company's inventory is out, but its factory building, patents, and goodwill are squarely in.

### 4.2 The master rule (Recognition principle)

> An asset is **impaired** when its **carrying amount exceeds its recoverable amount**. The excess is the **impairment loss**, recognised immediately.

$$\text{Impairment Loss} = \text{Carrying Amount} - \text{Recoverable Amount} \quad (\text{only if positive})$$

- **Carrying amount** = cost (or revalued amount) less accumulated depreciation and any earlier accumulated impairment.
- **Recoverable amount** = **higher of** (a) Net Selling Price and (b) Value in Use.

Practical shortcut the standard itself allows: you don't always need *both* figures. If **either** NSP or VIU already exceeds carrying amount, the asset is not impaired — stop, no need to compute the other. You only need both when the first one you compute is *below* carrying amount.

Two words in the master rule carry weight:
- **"Immediately"** — the loss is not spread, not deferred, not netted against future gains. It hits *this* period's P&L (or revaluation reserve) at once. This kills any temptation to "amortise the impairment."
- **"Exceeds"** — the test is strictly greater-than. If carrying amount *equals* recoverable amount, there is no impairment (loss = 0). And a *rise* in recoverable amount above carrying amount for a never-impaired asset does **nothing** — AS 28 never writes assets *up* except by reversing a prior impairment. Unrecognised gains stay unrecognised (prudence).

### 4.3 Net Selling Price (NSP)

$$\text{NSP} = \text{Fair value from sale (arm's length)} - \text{Direct costs of disposal}$$

Costs of disposal = legal costs, stamp duty, removal costs, direct incremental selling costs. **Exclude** finance costs, income-tax, and any cost already recognised as a liability. Best evidence = a binding sale agreement price; next best = market price in an active market; failing both, best estimate from recent transactions.

**Hierarchy of evidence for fair value (learn the order):**
1. Price in a **binding sale agreement** in an arm's-length transaction, adjusted for incremental disposal costs.
2. If no binding agreement, the **market price** in an active market (usually the *current bid* price; if unavailable, the price of the most recent transaction, provided circumstances have not changed significantly).
3. If no active market, the **best estimate** of what a knowledgeable, willing buyer would pay, based on recent comparable transactions in the same industry.

A subtle exclusion: costs that are **already recognised as liabilities** are not deducted again (else double-counting) — e.g., an accrued removal/dismantling provision. And **termination/redundancy costs or costs of reorganising the business** after disposal are *not* disposal costs. Only costs *directly attributable to bringing the asset to saleable condition and completing the sale* count.

### 4.4 Value in Use (VIU)

VIU = the present value of the future cash flows expected from **continuing use** of the asset plus its **residual value on eventual disposal**, discounted at a pre-tax rate.

$$\text{VIU} = \sum_{t=1}^{n} \frac{\text{CF}_t}{(1+r)^t} + \frac{\text{Residual/Disposal value}}{(1+r)^n}$$

Two ingredients, each with rules:

**(a) Estimating future cash flows** — base on reasonable, supportable assumptions and the *most recent* management budgets/forecasts (AS 28 guidance: projections generally not beyond **5 years** unless a longer period is justified; beyond that, extrapolate with a steady or declining growth rate). Include:
- cash *inflows* from continuing use;
- cash *outflows* necessarily incurred to generate those inflows (including day-to-day servicing);
- net disposal proceeds at end of life.

**Exclude** (critical — heavily examined):
- cash flows from **future restructuring** not yet committed;
- cash flows from **improving/enhancing** the asset's performance (test it in its *current* condition);
- cash inflows/outflows from **financing activities**;
- **income tax** receipts or payments.

**(b) The discount rate** — a **pre-tax** rate reflecting current market assessments of the time value of money and the risks specific to the asset. It must *not* double-count risks already baked into the cash-flow estimates.

**Why each exclusion exists (reason, don't memorise):**
- **Future restructuring not yet committed / enhancements:** VIU must value the asset *as it is today*. Cash flows from a not-yet-done upgrade or reorganisation belong to *future actions and future spending* the entity hasn't yet committed to; counting their benefit without counting their cost (and without a firm commitment) would inflate VIU. The asset is tested "in its current condition." (Once restructuring is *committed* under provision rules, its effects can be reflected — an AS 4/provision link.)
- **Financing cash flows:** interest and principal are already captured in the **discount rate** (which reflects the time value of money). Putting them in the cash flows too would double-count financing.
- **Income tax:** VIU uses **pre-tax** cash flows discounted at a **pre-tax** rate, deliberately keeping tax out of both sides so they stay consistent. Tax effects live in AS 22, not here.

**Consistency rule (the deep trap):** the cash flows and the discount rate must be on the **same basis**. Pre-tax cash flows ↔ pre-tax rate. Real (inflation-stripped) cash flows ↔ real rate; nominal cash flows ↔ nominal rate. A mismatch — e.g., pre-tax flows discounted at a post-tax rate, or nominal flows at a real rate — is a wrong answer even if the arithmetic is flawless.

**Growth-rate discipline for years beyond the budget horizon:** the extrapolation growth rate should be **steady or declining**, and should *not* exceed the long-term average growth rate for the products/industry/country unless a higher rate can be justified. Assuming an ever-rising growth rate is prohibited — it would let VIU explode unrealistically.

**Residual/terminal value:** the net disposal proceeds at the end of the asset's life are estimated using prices prevailing at the *valuation date* for similar assets that have reached the end of their useful life (less expected disposal costs), not speculative future prices.

### 4.5 Indicators of impairment (the annual scan)

At each balance sheet date, assess whether **any indicator** exists. If none, no formal estimate of recoverable amount is required (except where another rule mandates it). Indicators are grouped as **External** and **Internal**.

```mermaid
flowchart TD
    A["Balance sheet date: scan for indicators"] --> B["EXTERNAL signs"]
    A --> C["INTERNAL signs"]
    B --> B1["Market value fell significantly, more than expected"]
    B --> B2["Adverse tech, market, economic or legal change"]
    B --> B3["Market interest rates rose -- pushes discount rate up"]
    B --> B4["Net assets carrying amount exceeds market capitalisation"]
    C --> C1["Physical damage or obsolescence"]
    C --> C2["Asset idle, part of discontinuing operation, or plan to dispose early"]
    C --> C3["Internal reports show economic performance worse than expected"]
    B1 --> D["Any one present? Estimate recoverable amount"]
    B2 --> D
    B3 --> D
    B4 --> D
    C1 --> D
    C2 --> D
    C3 --> D
```
*If even one flag is up, you must estimate recoverable amount; if all are clear, you may skip the expensive test.*

**External indicators**
1. Asset's market value has declined significantly more than expected from normal use/passage of time.
2. Significant adverse changes (technological, market, economic, legal) in the entity's environment or the market the asset serves.
3. Market interest rates / rates of return have increased, likely raising the discount rate and cutting VIU.
4. The carrying amount of the entity's net assets exceeds its market capitalisation.

**Internal indicators**
5. Evidence of physical damage or obsolescence.
6. Significant adverse changes in the extent/manner an asset is used — idle, part of an operation being discontinued/restructured, or plan to dispose before the earlier-expected date.
7. Internal reporting indicates the asset's economic performance is, or will be, worse than expected.

**The list is a minimum, not a ceiling.** AS 28 explicitly says these indicators are illustrative; an entity may identify *other* indications and must still test. So a question describing an unlisted-but-clearly-adverse event (a key customer's insolvency, a raw-material supply collapse) is still a trigger — don't reject it just because it isn't verbatim in the seven.

**The market-cap indicator (No. 4) is the most misunderstood.** Carrying amount of *net assets* exceeding *market capitalisation* means the stock market values the whole entity at less than its books claim its net assets are worth — a collective market verdict that assets are overstated. It is an *external* signal precisely because it comes from outside the firm.

**Interest-rate indicator (No. 3) has a built-in escape valve.** A rise in market rates raises the discount rate and *tends* to cut VIU — but AS 28 notes you need not do a formal test if (a) the discount rate affected is unlikely to be affected by the rate rise (e.g., short-term-rate rises may not affect a long-life asset), or (b) VIU is likely well above carrying amount, or (c) the asset's recoverable amount is likely insensitive to the rate change. Rising rates are a *soft* trigger.

**Symmetry — indicators of reversal.** The same scan runs the *other* way at each balance sheet date: is there any sign a past impairment has decreased or vanished? The reversal indicators mirror the impairment ones (market value *risen* significantly, favourable tech/market/legal change, market rates *fallen* raising VIU, physical/performance *improvement*, etc.). Same discipline, opposite direction.

Even if **no** indicator exists, if an indicator triggered a *revised remaining useful life, depreciation method, or residual value* last time, those may still need updating — the scan has side-benefits.

### 4.6 Accounting for the impairment loss (the entry)

**Asset carried at cost (most common):**

| Particulars | Dr (₹) | Cr (₹) |
|---|---|---|
| Impairment Loss A/c ....... Dr | XXX | |
| &nbsp;&nbsp;&nbsp;To Accumulated Impairment / Asset A/c | | XXX |
| *(Impairment loss charged to Statement of P&L)* | | |

Then: **Impairment Loss A/c** is transferred to the **Statement of Profit and Loss** (it is an expense of the period).

**Asset carried at revalued amount (AS 10 revaluation model):** the impairment loss is treated as a **revaluation decrease** — first debited against any existing **Revaluation Reserve** for *that same asset* (to the extent available), and only the excess hits P&L.

**After impairment, adjust depreciation:** depreciation for *future* periods is recalculated on the **revised carrying amount** (recoverable amount) less residual value, spread over the **remaining useful life**. Impairment resets the depreciation base going forward.

**A subtlety on the revaluation-reserve route:** the loss is debited against the revaluation surplus **only of that specific asset**, and only to the extent that surplus exists. You cannot dip into another asset's revaluation reserve, and you cannot make the reserve go negative. Example: an asset with ₹1,00,000 revaluation surplus suffers a ₹1,50,000 impairment → ₹1,00,000 debited to Revaluation Reserve (extinguishing it), ₹50,000 charged to P&L.

**Liability side-effect:** an impairment can sometimes require recognising or re-measuring a related liability (e.g., an onerous-contract or decommissioning obligation) — but AS 28 itself does not create liabilities; it only measures the asset write-down. Keep the two separate in the answer.

### 4.7 Cash Generating Units (CGUs) — mechanics

**Definition:** the *smallest identifiable group of assets* that generates cash inflows **largely independent** of the cash inflows from other assets or groups.

**When to use:** when an individual asset's recoverable amount can't be estimated because it doesn't generate independent cash inflows and its VIU can't be assessed alone. Then estimate recoverable amount for the *CGU* it belongs to.

**Identifying the CGU — the decisive test:** the boundary is set by *independent cash inflows*, and you should identify CGUs **consistently from period to period** for the same asset(s). Two guiding points examiners test:
- If there is an **active market for the output** of an asset or group, that asset/group is a CGU **even if some or all of the output is used internally** — because the internal output *could* be sold, so an independent inflow effectively exists (measure using market prices).
- The way *management monitors operations* or makes *continue/dispose* decisions is useful evidence of CGU boundaries, but the ultimate criterion remains independence of cash *inflows*.

**Carrying amount of a CGU must be measured consistently with its recoverable amount:** include the carrying amounts of only those assets that generate the relevant cash inflows, plus a portion of assets that serve the unit (e.g., allocated **corporate/head-office assets** and **goodwill**) on a reasonable, consistent basis; exclude recognised **liabilities** unless recoverable amount cannot be determined without them. Apples-to-apples: don't compare a CGU carrying amount that includes an asset whose cash flows you *excluded* from VIU.

**Goodwill and corporate assets that can't be allocated on a reasonable basis** are handled with a "bottom-up / top-down" logic in AS 28: test the smallest CGU to which they can be reasonably allocated first (bottom-up); where goodwill/corporate assets relate to a *larger* group of CGUs, also test that larger group (top-down). For CA-Inter numericals you will usually be *given* the allocation; know that the allocation exists and why.

**Allocating a CGU impairment loss — the strict order:**
1. **First**, reduce the carrying amount of any **goodwill** allocated to the CGU (goodwill is the softest, riskiest asset — it absorbs the first blow).
2. **Then**, reduce the **other assets** of the CGU **pro rata** on the basis of their carrying amounts.

**Floor rule (a crucial limit):** in reducing individual assets, you must **not** write any single asset below the *highest* of: its own net selling price (if determinable), its own value in use (if determinable), and **zero**. Any impairment that "can't land" because of this floor is **reallocated pro rata to the other assets** of the CGU.

```mermaid
flowchart TD
    A["CGU impairment loss identified"] --> B["Step 1: wipe out GOODWILL of the CGU first"]
    B --> C["Any loss left over?"]
    C -->|Yes| D["Step 2: allocate to other assets PRO RATA by carrying amount"]
    C -->|No| E["Stop"]
    D --> F["But never below an asset's own NSP, VIU, or zero"]
    F --> G["Amount that cannot land there = reallocate to remaining assets"]
```
*Goodwill takes the first hit; the rest is shared pro rata, with a hard floor protecting each identifiable asset's own recoverable value.*

**Why goodwill absorbs the first blow (reason):** goodwill has *no independent recoverable value* — you can't sell it separately, and it has no value-in-use of its own; it exists only as the premium paid for the unit's future super-profits. When the unit under-performs, that premium is exactly what has evaporated. So it is both logical and prudent to extinguish goodwill before touching identifiable assets that *do* have their own realisable/usable value (protected by the floor).

### 4.8 Reversal of an impairment loss

At each balance sheet date, assess whether there is any indication that a **previously recognised impairment loss no longer exists or has decreased.** If so, re-estimate recoverable amount and **reverse** — but with a strict ceiling and one prohibition.

**The ceiling (the golden limit):** the increased carrying amount after reversal must **not exceed** the carrying amount that *would have been determined (net of depreciation) had no impairment loss been recognised in prior years.* In other words, you can climb back up only to the "would-have-been-if-never-impaired" line — never higher. Any excess would be a revaluation, not a reversal.

**Recognition of reversal:**
- Asset at cost → reversal is credited to the **Statement of P&L** (as income).
- Asset at revalued amount → reversal treated as a **revaluation increase** (credited to Revaluation Reserve), except to the extent it reverses a prior decrease that was charged to P&L (that part goes to P&L as income).

**After reversal, adjust depreciation** for future periods on the new (higher) carrying amount, less residual, over remaining life.

**Reversal for a CGU — the allocation:** a reversal of a CGU impairment is allocated to the assets of the unit **pro rata by carrying amounts**, but **NOT to goodwill**, and subject to a per-asset ceiling — no asset's carrying amount may be increased above the *lower* of (i) its recoverable amount (if determinable) and (ii) the carrying amount that would have been determined had no impairment been recognised. Any reversal amount that can't be allocated because an asset hit its ceiling is allocated pro rata to the *other* assets of the unit (except goodwill).

**The prohibition:** an impairment loss recognised for **GOODWILL is NOT reversed** in a subsequent period — *unless* the loss was caused by a specific external event of an exceptional nature not expected to recur, and later external events reverse it (an extremely narrow window; treat goodwill reversal as effectively banned for exam problems). Reason: any later increase in goodwill's recoverable amount is almost certainly *internally generated goodwill*, which AS 26 forbids recognising.

```mermaid
flowchart TD
    A["Indicator that impairment reversed?"] --> B["Re-estimate recoverable amount"]
    B --> C["Reverse the loss..."]
    C --> D["...but CAP at carrying amount that would exist had asset NEVER been impaired -- depreciated normally"]
    D --> E["Credit reversal to P&L -- or Revaluation Reserve if revalued"]
    F["Is it GOODWILL?"] -->|Yes| G["Do NOT reverse -- would be internally generated goodwill"]
```
*Reversal restores truth up to the never-impaired line, and no further; goodwill impairment is a one-way door.*

**Why the ceiling exists (deep reason):** a reversal is meant to *undo an earlier over-write-down*, not to recognise a *gain* the asset never had on a historical-cost basis. Had the asset never been impaired, ordinary depreciation would have carried it down to a definite line by today. Restoring exactly to that line returns the books to the historical-cost narrative. Going *above* it would be recognising an unrealised holding gain — that is revaluation territory (AS 10), which has its own reserve-based route and cannot masquerade as a reversal through P&L.

## 5. Worked Examples

### Example 1 — The basic sanity check (easy)

A machine has a carrying amount of ₹8,00,000. Due to a new competing technology (external indicator), the entity estimates:
- Net selling price = ₹5,50,000
- Value in use = ₹6,20,000

**Step 1 — Recoverable amount = higher of NSP and VIU** = higher of ₹5,50,000 and ₹6,20,000 = **₹6,20,000**.

**Step 2 — Compare with carrying amount:** ₹8,00,000 > ₹6,20,000 → impaired.

**Step 3 — Impairment loss** = ₹8,00,000 − ₹6,20,000 = **₹1,80,000**.

**Entry:**
| Particulars | Dr (₹) | Cr (₹) |
|---|---|---|
| Impairment Loss A/c ..... Dr | 1,80,000 | |
| &nbsp;&nbsp;To Machinery A/c | | 1,80,000 |

Impairment Loss ₹1,80,000 transferred to P&L. New carrying amount = ₹6,20,000. Note the trap: a careless student picks VIU because it's "the one you keep using it at" or picks NSP as "conservative." The rule is mechanical — **higher of the two**, here VIU.

*Examiner tweak — the shortcut in action:* suppose instead NSP = ₹8,40,000 (a firm buyer offer) and VIU is not yet computed. Since NSP ₹8,40,000 already **exceeds** carrying ₹8,00,000, recoverable amount is at least ₹8,40,000 > carrying → **not impaired**, and you *need not* compute VIU at all. Recognising when to stop saves marks and time.

### Example 2 — Computing Value in Use, then depreciation reset (medium)

On 1 April 2025, a plant has carrying amount ₹20,00,000, remaining useful life 4 years, nil residual value, straight-line depreciation. A flood damages it (internal indicator). Estimated net cash inflows from continued use: ₹6,00,000 per year for 4 years. Disposal value after 4 years: ₹1,00,000. Appropriate pre-tax discount rate: 10%. Net selling price now: ₹15,00,000.

**Step 1 — Value in Use** (PV of 4 annual inflows + PV of disposal). Discount factors at 10%: Yr1 0.909, Yr2 0.826, Yr3 0.751, Yr4 0.683.

| Year | Cash flow (₹) | DF @10% | PV (₹) |
|---|---|---|---|
| 1 | 6,00,000 | 0.909 | 5,45,400 |
| 2 | 6,00,000 | 0.826 | 4,95,600 |
| 3 | 6,00,000 | 0.751 | 4,50,600 |
| 4 | 6,00,000 | 0.683 | 4,09,800 |
| 4 (disposal) | 1,00,000 | 0.683 | 68,300 |
| **Total VIU** | | | **19,69,700** |

**Step 2 — Recoverable amount** = higher of NSP ₹15,00,000 and VIU ₹19,69,700 = **₹19,69,700**.

**Step 3 — Impairment loss** = carrying ₹20,00,000 − recoverable ₹19,69,700 = **₹30,300**.

**Entry:** Impairment Loss A/c Dr ₹30,300 / To Plant A/c ₹30,300 → charged to P&L. New carrying amount = **₹19,69,700**.

**Step 4 — Depreciation for future years** resets on the new base: ₹19,69,700 ÷ 4 remaining years = **₹4,92,425 per year** (instead of the old ₹5,00,000). This is the reconciling payoff — impairment lowers both the asset and all subsequent depreciation.

*Self-check: had NSP been, say, ₹19,90,000 (above VIU), recoverable amount would have been ₹19,90,000, and impairment only ₹10,000 — proving the "higher of" rule protects the asset from over-writedown.*

*Examiner tweak — the "cash flows after upgrade" trap:* suppose the problem adds "if the company spends ₹2,00,000 next year to refurbish, annual inflows rise to ₹7,50,000." You must **ignore** the enhanced flows and the refurbishment cost — VIU tests the asset in its *current, damaged* condition. Using ₹7,50,000 would wrongly inflate VIU and understate (or erase) the impairment. Strip out any post-improvement or uncommitted-restructuring numbers before discounting.

### Example 3 — Cash Generating Unit with goodwill and the floor (exam-hard)

A CGU (a small factory) comprises: Goodwill ₹2,00,000, Building ₹6,00,000, Plant ₹4,00,000, Fittings ₹2,00,000 — total carrying amount **₹14,00,000**. After an adverse market change, the CGU's recoverable amount is estimated at **₹9,00,000**. Additional info: the Building's own net selling price is reliably ₹5,20,000 (so it cannot be written below that).

**Step 1 — Total impairment loss for the CGU** = ₹14,00,000 − ₹9,00,000 = **₹5,00,000**.

**Step 2 — Allocate to goodwill first.** Goodwill ₹2,00,000 fully written off. Remaining loss to allocate = ₹5,00,000 − ₹2,00,000 = **₹3,00,000**.

**Step 3 — Allocate ₹3,00,000 pro rata across other assets by carrying amount** (Building 6,00,000 : Plant 4,00,000 : Fittings 2,00,000 = total 12,00,000).

| Asset | Carrying (₹) | Pro-rata share of ₹3,00,000 | Provisional new carrying (₹) |
|---|---|---|---|
| Building | 6,00,000 | 3,00,000 × 6/12 = 1,50,000 | 4,50,000 |
| Plant | 4,00,000 | 3,00,000 × 4/12 = 1,00,000 | 3,00,000 |
| Fittings | 2,00,000 | 3,00,000 × 2/12 = 50,000 | 1,50,000 |
| **Total** | **12,00,000** | **3,00,000** | **9,00,000** |

**Step 4 — Apply the floor rule.** Building must not fall below its own NSP ₹5,20,000. Provisional ₹4,50,000 is *below* that floor — not allowed. So Building is written only down to **₹5,20,000** (a reduction of ₹80,000, not ₹1,50,000). The **un-absorbed** ₹70,000 (1,50,000 − 80,000) must be **reallocated to Plant and Fittings pro rata** (their carryings 4,00,000 : 2,00,000 = 4:2).

| Asset | Extra ₹70,000 reallocated | Final reduction | Final carrying (₹) |
|---|---|---|---|
| Plant | 70,000 × 4/6 = 46,667 | 1,00,000 + 46,667 = 1,46,667 | 2,53,333 |
| Fittings | 70,000 × 2/6 = 23,333 | 50,000 + 23,333 = 73,333 | 1,26,667 |
| Building | — | 80,000 | 5,20,000 |

**Step 5 — Reconcile.** Final carryings: Goodwill 0 + Building 5,20,000 + Plant 2,53,333 + Fittings 1,26,667 = **₹9,00,000** ✔ (equals recoverable amount; total loss ₹5,00,000 fully absorbed: 2,00,000 + 80,000 + 1,46,667 + 23,333... let me total the identifiable reductions: Building 80,000 + Plant 1,46,667 + Fittings 73,333 = 3,00,000, plus goodwill 2,00,000 = **₹5,00,000** ✔). Assumes Plant and Fittings have no binding floor (their own NSP/VIU below these figures). Everything ties.

### Example 4 — Reversal capped at the "never-impaired" line (medium-hard)

Continue a simpler asset. On 1 April 2023, a machine (cost ₹10,00,000, life 10 years, SLM, nil residual) had carrying amount after 2 years' depreciation of ₹8,00,000. On 31 March 2024 (end of year 3... let's fix the timeline): after year 3 depreciation ₹1,00,000, carrying would normally be ₹7,00,000, but an impairment brought recoverable amount to **₹5,60,000**, so an impairment loss of ₹1,40,000 was booked.

Remaining life at that point = 7 years. New depreciation = ₹5,60,000 ÷ 7 = **₹80,000/year**.

Two years later (after 2 more years), carrying amount = ₹5,60,000 − (2 × ₹80,000) = **₹4,00,000**. Now the adverse condition reverses (market recovers). Re-estimated recoverable amount = **₹6,50,000**.

**Step 1 — What is the ceiling?** Carrying amount had there been **no** impairment: original ₹7,00,000 (at the impairment date) would have depreciated at the *original* ₹1,00,000/year for 2 more years → ₹7,00,000 − ₹2,00,000 = **₹5,00,000**.

**Step 2 — Reverse, but cap at ₹5,00,000.** Recoverable ₹6,50,000 exceeds the ceiling, so we can raise carrying amount only to **₹5,00,000**, not ₹6,50,000.

**Step 3 — Reversal amount** = ₹5,00,000 − ₹4,00,000 = **₹1,00,000**, credited to P&L as income.

**Entry:** Machinery A/c Dr ₹1,00,000 / To Reversal of Impairment Loss (P&L) ₹1,00,000.

**Step 4 — Depreciation going forward** on ₹5,00,000 over remaining life. This is the whole discipline of reversal: restore up to where normal depreciation would have left you, and *not one rupee more* — otherwise you'd be revaluing upward, which AS 28 reversal is not.

*Examiner tweak — partial reversal below the ceiling:* if instead the re-estimated recoverable amount were only **₹4,70,000**, the reversal would be **₹4,70,000 − ₹4,00,000 = ₹70,000** (recoverable is *below* the ₹5,00,000 ceiling, so the ceiling doesn't bite and you reverse only up to recoverable). The rule is: reverse up to the **lower of** re-estimated recoverable amount and the never-impaired ceiling. Students who always jump to the ceiling get this wrong.

### Example 5 — NSP-vs-VIU with a decommissioning cost, and the shortcut (medium)

A wind turbine has carrying amount ₹40,00,000. A regulatory change (external indicator) prompts a test. Data: a broker's firm indicative sale price ₹43,00,000; direct removal and legal costs to sell ₹1,20,000; VIU from continued generation is estimated at ₹38,00,000.

**Step 1 — Net Selling Price** = 43,00,000 − 1,20,000 = **₹41,80,000**.

**Step 2 — Do we even need VIU?** NSP ₹41,80,000 already **exceeds** carrying ₹40,00,000. Recoverable amount = higher of (₹41,80,000, ₹38,00,000) = **₹41,80,000** > carrying → **no impairment**. The VIU figure is a red herring; because NSP alone cleared carrying amount, the asset is safe.

**Reconcile / self-check:** even though VIU (₹38,00,000) is *below* carrying amount, the asset is *not* impaired, because recoverable amount is the **higher** route and the sell route wins. A student who anchored on VIU would have wrongly booked a ₹2,00,000 loss. The lesson: compute the *cheaper/available* figure first, and if it clears carrying amount, stop.

*Examiner tweak:* if the broker price were only ₹40,50,000, NSP = 40,50,000 − 1,20,000 = ₹39,30,000, now *below* carrying. Then VIU matters: recoverable = higher(39,30,000, 38,00,000) = ₹39,30,000, impairment = 40,00,000 − 39,30,000 = **₹70,000**. Small changes in the disposal-cost or sale figure flip the whole answer — read those numbers carefully.

### Example 6 — Revalued asset: impairment splits between reserve and P&L (medium-hard)

A building is carried under AS 10's revaluation model at ₹50,00,000, and its **Revaluation Reserve** for this building holds ₹8,00,000 (from an earlier upward revaluation). A zoning ban (external indicator) crushes its value: recoverable amount now ₹39,00,000.

**Step 1 — Impairment loss** = 50,00,000 − 39,00,000 = **₹11,00,000**.

**Step 2 — Route the loss (revaluation-decrease treatment).** First absorb against this building's Revaluation Reserve to the extent available (₹8,00,000), then the balance to P&L.
- Debit Revaluation Reserve ₹8,00,000 (reserve now nil).
- Debit P&L (Impairment Loss) ₹3,00,000.

**Entries:**
| Particulars | Dr (₹) | Cr (₹) |
|---|---|---|
| Revaluation Reserve A/c ..... Dr | 8,00,000 | |
| Impairment Loss (P&L) A/c ..... Dr | 3,00,000 | |
| &nbsp;&nbsp;To Building A/c | | 11,00,000 |

**Reconcile:** total debits 8,00,000 + 3,00,000 = ₹11,00,000 = credit to Building ✔. New carrying amount ₹39,00,000.

*Examiner tweak — the reversal mirror:* if this building's value later recovers, the reversal is credited **first to P&L** to the extent of the ₹3,00,000 previously charged there (reversing a P&L charge), and any excess is credited to **Revaluation Reserve** (an upward revaluation) — again subject to the never-impaired ceiling. Getting the reserve-vs-P&L split backwards is a classic error: *loss* goes reserve-first-then-P&L; *reversal* goes P&L-first (to undo the earlier charge)-then-reserve.

## 6. Presentation & Disclosure

**Where it appears:** an impairment loss is an **expense in the Statement of Profit and Loss** (reversal is income). If the asset was carried at revalued amount, the loss/reversal goes through the **Revaluation Reserve** to the extent that reserve holds a balance for that asset, and only the remainder through P&L.

**Balance sheet / notes — for each class of assets, disclose:**
- the amount of **impairment losses recognised** in P&L during the period, and the line item(s) of the P&L in which they are included;
- the amount of **reversals** of impairment losses recognised in P&L during the period, and the line item(s);
- impairment losses / reversals recognised **directly in revaluation surplus** during the period.

**If an individual impairment loss (or reversal) is material, additionally disclose:**
- the **events and circumstances** that led to it;
- the **amount** recognised or reversed;
- for an **individual asset**: its nature and the reportable segment it belongs to;
- for a **CGU**: a description of the unit, the amount by class of asset (and by segment), and if the CGU's composition changed, that fact;
- whether recoverable amount is **net selling price or value in use**; if NSP, the basis of determining it; if VIU, the **discount rate** used.

**Segment disclosure (for entities applying AS 17):** impairment losses and reversals recognised during the period, by reportable segment.

**Encouraged (not mandatory) disclosures** — AS 28 *encourages* an entity to disclose the **key assumptions** used to determine recoverable amount (e.g., growth rates, discount rates), which improves comparability. Know the distinction: *required* vs *encouraged* is a favourite one-mark theory point.

The presentation logic mirrors the substance: a *sudden loss of value* deserves visibility, so the standard forces you to explain *why* it happened, *how much*, and *which method* revealed it — no burying it inside depreciation. The disclosure philosophy is **decision-usefulness**: a user must be able to judge whether the impairment is a one-off shock or a symptom of a deteriorating business, and whether management's recoverable-amount assumptions are aggressive or conservative — hence the emphasis on *cause, method, and key assumptions*.

## 7. Connections

```mermaid
flowchart LR
    A["AS 10 -- Depreciation spreads known cost over life"] --> B["AS 28 -- catches SUDDEN falls depreciation misses"]
    B --> C["After impairment, AS 10 depreciation continues on new base"]
    D["AS 26 -- Intangibles and internally generated goodwill rules"] --> B
    B --> E["Goodwill impairment NOT reversible -- because AS 26 bans internal goodwill"]
    F["AS 13 / AS 2 / AS 7 / AS 22"] -.excluded from.-> B
```
*AS 28 is the safety net stretched under AS 10 and AS 26; its no-reversal-of-goodwill rule is a direct consequence of AS 26.*

- **AS 10 (Property, Plant & Equipment):** AS 10 gives carrying amount via depreciation; AS 28 tests whether that carrying amount is still supportable and, if not, writes it down — after which AS 10 depreciation resumes on the *revised* base. They are partners: AS 10 handles the *planned* decline, AS 28 the *unplanned* one. Revaluation under AS 10 also dictates *where* an impairment lands (reserve vs P&L). Note the reciprocity: an AS 28 *reversal* also feeds back into AS 10 depreciation (higher base going forward).
- **AS 26 (Intangible Assets):** AS 26 forbids recognising internally generated goodwill and requires intangibles to be amortised; AS 28 tests those same intangibles for impairment. The prohibition on **reversing goodwill impairment** flows straight from AS 26 — any recovery in goodwill value is deemed *internally generated* and thus non-recognisable.
- **AS 2 (Inventories):** deliberately excluded — but the *lower of cost and NRV* rule there is the perfect contrast to AS 28's *higher of NSP and VIU*, and examiners exploit the confusion.
- **AS 4 / provisions (AS 29):** future restructuring cash flows are excluded from VIU until a provision is actually committed — links to obligation-recognition logic. A **decommissioning/dismantling** liability, once recognised, interacts with both the asset's cost (AS 10) and its disposal cost (AS 28 NSP).
- **AS 5 (Accounting Policies, Changes in Estimates):** an impairment is the recognition of a *change in estimate* about an asset's recoverable value — its prospective treatment (reset depreciation going forward, no retrospective restatement) is pure AS 5 logic.
- **AS 22 (Deferred Tax):** an impairment loss changes the difference between book and tax carrying values, potentially creating/altering a **deferred tax asset or liability** — even though DTAs themselves are outside AS 28's scope.
- **AS 17 (Segment Reporting):** impairment losses/reversals are disclosed by reportable segment — a direct cross-reference.

## 8. Traps & Examiner Tricks

1. **"Higher of" vs "lower of" swap.** The single most common error: applying inventory's *lower of cost and NRV* to fixed assets. AS 28 recoverable amount is **HIGHER** of NSP and VIU. Anchor it: a fixed asset is *used*, so the owner takes the better of sell-or-use.
2. **Picking the wrong one of NSP/VIU without comparing.** Always compute (or at least reason about) both, take the higher, *then* compare to carrying amount. Students often stop at VIU.
3. **Forgetting the shortcut waste.** Conversely, if the first figure you compute already exceeds carrying amount, the asset is not impaired — no need to compute the second. Don't burn exam time computing VIU when NSP already clears carrying amount.
4. **Including forbidden cash flows in VIU.** Future *restructuring* not yet committed, *enhancement/improvement* cash flows, *financing* flows, and *income tax* are all **excluded**. Test the asset in its *present condition*. A favourite: examiner slips in "cash flows after planned upgrade" — strip them out.
5. **Using a post-tax discount rate.** VIU uses a **pre-tax** rate. Mixing post-tax rate with pre-tax cash flows is a classic setup. Same trap in disguise: mixing *nominal* cash flows with a *real* rate.
6. **Not resetting depreciation after impairment (or reversal).** The revised carrying amount must be depreciated over *remaining* useful life. Forgetting this loses easy marks.
7. **CGU allocation order.** Goodwill **first** (fully), then other assets **pro rata** by carrying amount — never the reverse, never equally.
8. **Ignoring the floor in CGU allocation.** An individual asset can't be written below its own NSP / VIU / zero; the un-absorbed amount reallocates to the others. High-difficulty questions hinge on this.
9. **Breaching the reversal ceiling.** Reversal is capped at the *depreciated historical carrying amount had no impairment occurred*. Writing back to full recoverable amount when that exceeds the ceiling is wrong.
10. **Over-shooting on reversal when recoverable is *below* the ceiling.** The reverse of Trap 9: reverse up to the **lower of** re-estimated recoverable amount and the ceiling. Don't always leap to the ceiling.
11. **Reversing goodwill impairment.** Goodwill impairment is **not** reversed (treat as absolute for exams). Any "recovery" would be internally generated goodwill, banned by AS 26. This also means a CGU *reversal* is **never allocated to goodwill**.
12. **Revaluation routing (both directions).** For a revalued asset, *impairment* first hits the **Revaluation Reserve** of *that* asset (only up to its balance), then P&L; a *reversal* is credited to **P&L first** (to undo any prior P&L charge), then to the reserve. Don't dump everything straight to P&L, and don't reverse the order.
13. **Annual test confusion (AS vs Ind AS).** Under **ICAI AS 28** there is *no* mandatory annual impairment test for goodwill — only the indicator-based test. The annual test is an **Ind AS 36** feature. State the correct one for the paper you're sitting.
14. **Treating indicators as an exhaustive list.** The seven indicators are illustrative minimums; an unlisted adverse event still triggers a test.
15. **Comparing mismatched CGU figures.** The CGU's carrying amount and its recoverable amount must be built on the *same* set of assets/liabilities. Including an asset in carrying amount whose cash flows you excluded from VIU corrupts the comparison.
16. **Writing an asset below zero.** Recoverable amount (and each asset's floor) is bounded at **zero**; VIU can never be treated as negative in the floor — you can abandon the asset.
17. **Confusing "carrying amount" inputs.** Carrying amount is cost/revalued amount *less accumulated depreciation AND accumulated impairment*. Forgetting prior impairment (or prior depreciation) mis-states the loss.

## 9. First-Principles Recap

- An asset promises *future economic benefits*; if those benefits silently fall below its carrying amount, the balance sheet lies — depreciation, being a fixed formula, cannot detect this. AS 28 is the detector.
- Depreciation is *cost allocation* fixed at acquisition; impairment is *point-in-time value verification* driven by today's world. They are partners, not substitutes — even a new, fully-depreciated-to-schedule asset can be impaired.
- The master rule: **carrying amount must never exceed recoverable amount**; the excess is an impairment loss recognised *immediately*.
- **Recoverable amount = higher of net selling price and value in use** — because a rational owner takes the better of selling or continuing to use, and prudence means "don't overstate," *not* "understate maximally." Bounded below at **zero** (you can always abandon).
- Testing is **indicator-driven** (external + internal red flags, illustrative not exhaustive) — a cheap annual scan that triggers the expensive recoverable-amount estimate only when warranted.
- **Value in use** = PV of future cash flows *in the asset's current condition*, at a **pre-tax** rate, excluding restructuring, enhancement, financing, and tax flows; cash flows and rate must be on the *same basis*.
- When an asset can't earn cash alone, test its **Cash Generating Unit** — the smallest group with *largely independent cash inflows* — and allocate impairment: **goodwill first, then pro rata**, with a floor protecting each asset's own recoverable value.
- After impairment, **depreciation resets** on the new carrying amount over remaining life.
- Impairment is **reversible** (conditions permitting), but only up to the **never-impaired depreciated carrying amount** — never beyond, and only up to re-estimated recoverable amount if that is lower.
- **Goodwill impairment is not reversed**, because any later increase is internally generated goodwill, which AS 26 forbids; CGU reversals are never allocated to goodwill.
- Impairment loss is a **P&L expense** (or a revaluation decrease for revalued assets, reserve-first); reversal is income (P&L-first for revalued assets); material impairments demand disclosure of cause, amount, method, and segment.

## 10. Quick-Revision Sheet

| Item | Rule |
|---|---|
| **Core test** | Impaired if Carrying Amount > Recoverable Amount; loss = the excess |
| **Recoverable Amount** | HIGHER of Net Selling Price and Value in Use (min zero) |
| **Net Selling Price** | Fair sale value − direct disposal costs (exclude finance & tax) |
| **NSP evidence order** | Binding sale agreement → active-market price → best estimate from recent deals |
| **Value in Use** | PV of future cash flows (current condition) + disposal value; **pre-tax** rate |
| **VIU exclusions** | Future restructuring (uncommitted), enhancements, financing, income tax |
| **Basis consistency** | Pre-tax flows ↔ pre-tax rate; nominal ↔ nominal; real ↔ real |
| **Forecast horizon** | Generally ≤ 5 yrs budgets, then extrapolate steady/declining growth |
| **When to test** | On any External or Internal **indicator** at B/S date (list is illustrative) |
| **External indicators** | Market value fall, adverse tech/market/legal change, ↑ interest rates, net assets > market cap |
| **Internal indicators** | Physical damage/obsolescence, asset idle/discontinuing, poor internal performance |
| **Loss entry** | Impairment Loss A/c Dr / To Asset (or Accum. Impairment); to P&L |
| **Revalued asset — loss** | Revaluation Reserve (of that asset) first, then P&L |
| **Revalued asset — reversal** | P&L first (undo prior P&L charge), then Revaluation Reserve |
| **Post-impairment** | Recompute depreciation on new base ÷ remaining life |
| **CGU** | Smallest group with largely independent cash **inflows** |
| **CGU carrying amount** | Consistent basis with recoverable amount; include allocated goodwill/corporate assets; exclude liabilities (usually) |
| **CGU allocation** | (1) Goodwill fully, (2) other assets pro rata by carrying amount |
| **CGU floor** | No asset below its own NSP / VIU / zero; excess reallocates pro rata |
| **Reversal ceiling** | Up to carrying amount had **no** impairment ever occurred (depreciated) |
| **Reversal amount** | LOWER of re-estimated recoverable amount and the ceiling; minus current carrying |
| **Reversal entry** | Asset A/c Dr / To Reversal (P&L income) [or Reval. Reserve if revalued] |
| **CGU reversal** | Pro rata to assets, **never goodwill**; per-asset ceiling applies |
| **Goodwill reversal** | **Not permitted** (internally generated goodwill barred by AS 26) |
| **Scope-out** | AS 2 inventory, AS 7 contracts, AS 13 investments, AS 22 DTA |
| **AS vs Ind AS** | AS 28: indicator test only. Ind AS 36: **annual** test for goodwill/indefinite intangibles |

**Golden mnemonic chain:** *Indicator → Recoverable = Higher(NSP, VIU) → compare → write down to recoverable → reset depreciation → reverse later only up to never-impaired line (and not above recoverable) → but never reverse goodwill.*
