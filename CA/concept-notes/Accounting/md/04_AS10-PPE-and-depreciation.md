# Chapter 4 — AS 10: Property, Plant & Equipment (and *why* depreciation exists)

*This chapter proves that even a "computational" topic is really a concept. Depreciation confuses students precisely because they compute it before they understand what it is. We'll fix the order: idea first, formula second.*

---

## 1. The Problem

A company buys a machine for ₹10,00,000 that will be used for 10 years. Two naive approaches, both wrong:

- **"Expense the whole ₹10,00,000 in Year 1."** But the machine will help *earn* revenue for 10 years! Dumping its entire cost on Year 1 makes Year 1 look terrible and Years 2–10 look artificially great — even though the machine worked equally hard every year. That violates **accrual/matching** (Chapter 1): costs should sit in the same periods as the revenues they help produce.
- **"Never expense it; it's an asset."** But the machine is *wearing out*. After 10 years it's scrap. If you keep it on the books at ₹10,00,000 forever, you're pretending value that has physically evaporated still exists — overstating assets and profit. That violates **prudence** and **reliability**.

So there are really two problems knotted together:
1. **How do we spread a long-lived asset's cost over the years it serves?** (an income-statement matching problem)
2. **How do we show the asset shrinking in value on the Balance Sheet?** (a realistic-valuation problem)

---

## 2. The Core Idea

> **Depreciation is not "loss in market value." It is the systematic *spreading* of an asset's cost over the years it is used** — matching the cost to the benefit.

Picture the machine as a **prepaid bucket of 10 years of usefulness.** You paid ₹10,00,000 up front for that bucket. Each year you "use up" one year's worth of usefulness, so each year you move a slice of the cost from the Balance Sheet (asset) into the P&L (expense). After 10 years the bucket is empty and the asset's book value has fallen to its scrap (residual) value.

The two problems solve together: the slice you expense each year (P&L) is the same slice by which the asset shrinks (Balance Sheet). One mechanism, two jobs.

**Key mental correction:** depreciation is a process of **allocation, not valuation.** It does *not* try to track the machine's resale price on any given day. It answers "how much of what I paid have I consumed?", not "what's it worth today?"

---

## 3. Why it's built this way

### 3a. Why depreciation is charged even in a loss year, even if the asset's market price rose
Because depreciation is about **consuming the benefit you paid for**, not about market price. The machine helped you try to earn revenue this year regardless of whether you made a profit, and regardless of whether second-hand machine prices went up. The cost of that year's *use* still has to be recognised. Students find this counter-intuitive only because they wrongly think depreciation = "fall in value." Drop that, and it makes sense.

### 3b. Why we need three inputs: cost, useful life, residual value
To spread a cost fairly you must know:
- **Depreciable amount = Cost − Residual value.** You only spread what you'll actually *consume*. If you'll sell the scrap for ₹50,000 at the end, you never really "used up" that ₹50,000 — so you don't depreciate it.
- **Useful life** — over *how many years* (or units) will *this business* use it? Note it's the life *to you*, not the total physical life. A rental-car firm might use a car 3 years then sell it; its useful life is 3, even if the car could run 12.

Both residual value and useful life are **estimates** — judgements. That's fine (Chapter 1 allows judgement) as long as they're reasonable and revisited.

### 3c. Why more than one *method* is allowed (SLM vs WDV)
Different assets *deliver* their benefit differently, so the pattern of expensing should match the pattern of benefit:

- **Straight Line Method (SLM):** equal depreciation each year. *Use when* the asset gives roughly **equal benefit every year** (e.g., a building, furniture). Logic: steady use → steady cost.
- **Written Down Value / Reducing Balance (WDV):** a fixed *percentage* on the *reducing* book value, so depreciation is high early and low later. *Use when* the asset is **most productive when new** and/or **repair costs rise as it ages** (e.g., machinery, vehicles). Logic: high benefit early → high cost early; and as repairs climb later, the falling depreciation keeps the *total* yearly cost (depreciation + repairs) more even.

So the method isn't arbitrary — it's chosen to **mirror how the asset actually gives up its usefulness.** That's the matching principle picking the right shape.

### 3d. Why "component" thinking and why revaluation is optional
- **Componentisation:** if a machine has a major part with a *different* life (say an engine lasting 5 years inside a body lasting 15), AS 10 says depreciate them **separately.** *Why?* Lumping them uses one wrong life for both and mis-states expense. Match each part to its own consumption.
- **Cost vs Revaluation model:** AS 10 lets you carry PPE either at **cost less depreciation** or at a **revalued amount.** *Why offer revaluation?* For assets like land/buildings whose value genuinely changes a lot, historical cost can become misleading. But revaluation must be done consistently for the whole *class* and kept up to date — otherwise it becomes cherry-picking (revalue only what went up). The revaluation surplus goes to a **reserve**, not to profit, because it's **unrealised** (prudence: you haven't sold it, so it isn't profit).

### 3e. What goes into "cost" (same logic as AS 2)
Cost = purchase price + import duties/non-refundable taxes + **all costs directly needed to bring the asset to the location and condition for its intended use** (site prep, installation, testing, initial delivery) + the initial estimate of **dismantling/restoration** costs where the company is obliged to restore the site. Same "get it ready to use" test as inventory. Costs *after* it's ready to run (normal repairs, staff training) are **period expenses**, not part of the asset — because they don't create the asset, they just keep it running.

---

## 4. The Mechanics (RMPD lens)

- **Recognition:** capitalise an item as PPE when it's a resource you **control**, it will give **future economic benefit**, it's for **use** (not resale) over **more than one period**, and its cost is measurable. Later spending is capitalised **only if it improves** the asset beyond original performance (e.g., an upgrade that extends life or capacity); routine repairs are expensed.
- **Measurement:**
  - *Initially* at **cost** (per 3e).
  - *Subsequently* under the **cost model** (cost − accumulated depreciation − impairment) or **revaluation model**.
  - **Depreciation** each year:
    - **SLM:** (Cost − Residual) ÷ Useful life → same amount yearly.
    - **WDV:** fixed % × opening book value → falling amount yearly.
  - Review useful life, residual value, and method **periodically**; if the estimate changes, adjust **prospectively** (future years) — it's a change in *estimate* (AS 5), not an error, so you don't rewrite the past.
- **Presentation:** under **Non-current Assets** on the Balance Sheet, shown at cost/revalued amount less accumulated depreciation; depreciation is an expense in the P&L.
- **Disclosure:** for each class — gross amount, depreciation method, useful lives/rates, accumulated depreciation, and a reconciliation of movements. *Why?* So a reader can judge how aggressively/conservatively the company depreciates (AS 1 logic).

### The two journal entries that capture the whole idea
1. **Charge depreciation:** *Depreciation A/c Dr → To Accumulated Depreciation (or Asset) A/c.* (Moves a slice of cost into expense; shrinks the asset.)
2. **Close to P&L:** *Profit & Loss A/c Dr → To Depreciation A/c.* (The slice lands in this year's profit calculation.)

If you understand the "prepaid bucket," these entries are obvious, not memorized.

---

## 5. Reasoned example

*Machine cost ₹10,00,000; expected useful life 10 years; residual (scrap) value ₹1,00,000.*

**Depreciable amount** = 10,00,000 − 1,00,000 = **₹9,00,000** (you only spread what you'll consume).

- **SLM:** 9,00,000 ÷ 10 = **₹90,000 every year.** After 10 years, book value = 10,00,000 − 9,00,000 = ₹1,00,000 = residual. Bucket empty. 
- **WDV (say 20%):** Year 1 = 20% × 10,00,000 = ₹2,00,000; Year 2 = 20% × (10,00,000 − 2,00,000) = ₹1,60,000; Year 3 = 20% × 6,40,000 = ₹1,28,000 … high early, tapering later.

Notice you didn't memorize a formula — you *spread a consumed cost*. SLM spreads it flat; WDV spreads it front-loaded. Same bucket, two pouring speeds, each chosen to match how the machine gives up its usefulness.

---

## 6. Connections

- **Accrual/matching (Ch 1)** is the reason depreciation exists at all.
- **Prudence (Ch 1)** is why revaluation gains go to a reserve, not profit, and why you don't overstate the asset.
- **"Cost to get ready for use" (Ch 3, AS 2)** is the *same* capitalisation test — inventory and PPE share it.
- **Change in useful life = change in estimate → AS 5** (handled prospectively). This is a favourite exam link.
- **Impairment (AS 28):** depreciation handles *normal* consumption; impairment handles a *sudden abnormal* drop in recoverable value. Different triggers, complementary standards.
- **Cost Accounting subject:** the depreciation of factory machines flows into **production overhead / conversion cost** — linking back to AS 2's inventory valuation.

---

## 7. Traps & confusions

- **"Depreciation = fall in market value." Wrong** — it's *allocation of cost over use*. This single misconception causes most depreciation errors. Market price is irrelevant to the annual charge (impairment/revaluation handle value separately).
- **Depreciating the residual value — wrong.** You spread only Cost − Residual.
- **Forgetting to depreciate in loss years — wrong.** Use consumed the benefit regardless of profit.
- **Treating a change in useful life as a past error — wrong.** It's a change in *estimate* → adjust future years only (prospective), never restate prior years.
- **Capitalising routine repairs — wrong.** Only spending that *improves* the asset beyond its original standard is capitalised; upkeep is a period expense.
- **Revaluing one asset in a class and not others — wrong.** Revaluation is by **whole class**, kept current, to stop cherry-picking gains.

---

## 8. First-principles recap

- Depreciation exists to satisfy **matching** (spread an asset's cost across the years it earns) and **prudence** (don't carry a wearing-out asset at full cost).
- It is **allocation of cost, not tracking of market value** — charged every year of use, profit or loss, price up or down.
- Spread only the **depreciable amount = Cost − Residual value**, over the **useful life to this business**.
- **Method mirrors the benefit pattern:** SLM for steady-use assets; WDV for front-loaded/rising-repair assets.
- **Cost** = everything to bring the asset *ready for its intended use*; later routine costs are period expenses, only *improvements* are capitalised.
- Changes in life/residual/method are **changes in estimate → prospective** (AS 5); revaluation gains sit in a **reserve** because they're unrealised.
