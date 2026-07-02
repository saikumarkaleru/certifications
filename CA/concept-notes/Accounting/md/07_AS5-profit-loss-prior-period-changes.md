# Chapter 07 — AS 5: Net Profit/Loss for the Period, Prior Period Items & Changes in Accounting Policies

## 1. The Problem — a number that lies by telling the truth

Imagine you are an equity analyst. Every quarter you receive the Statement of Profit and Loss of a company you cover, and every quarter you do the same thing: you take this year's net profit, compare it to last year's, work out a growth rate, and extrapolate. Profit grew 18% last year, 16% this year, so you forecast ~17% next year and price the share on that.

Now suppose this year's profit of ₹120 crore includes:

- ₹40 crore of insurance proceeds from a factory that burned down (that fire will not repeat),
- a ₹15 crore gain because the company this year decided to value inventory using FIFO instead of weighted average (a *bookkeeping choice*, not a business event),
- and buried inside "other expenses" a ₹9 crore charge that actually belonged to *last year* — a supplier's bill for last year's repairs that got recorded only now.

Every rupee of that ₹120 crore is *real* cash-and-accrual accounting. The number is not fraudulent. And yet it is deeply misleading, because you were going to use it to *predict the future*, and none of those three items tell you anything about the future. The fire won't recur. The FIFO switch is a one-time re-labelling. The ₹9 crore was never about this year's performance at all.

This is the problem AS 5 exists to solve. A single bottom-line profit figure is asked to do two jobs at once:

1. **Report** what actually happened to the entity this period (a faithful total), and
2. **Predict** — serve as a base for estimating what *normally recurring* operations will earn next period.

Those two jobs pull in opposite directions. Job 1 says "put everything in — it's all real." Job 2 says "strip out the one-offs, the accounting-choice noise, and the stuff that belongs to other years, or you'll forecast garbage."

AS 5's genius is that it refuses to choose. It keeps *everything* in the net profit (nothing is hidden or taken to reserves), but forces the entity to **label and separate** the noisy components so a reader can mentally rebuild the "clean" recurring number. AS 5 is not about *what* goes into profit — it is about *how the pieces are shown* so the profit figure can serve both masters.

## 2. The Core Idea — one number, honestly itemised

**The single principle: All items of income and expense recognised in a period are included in the determination of net profit or loss — but items whose *nature or size* would distort a reader's view of ordinary performance must be separately disclosed.**

Think of the Statement of Profit and Loss as a bank statement you hand to someone who wants to judge your salary. Your true balance-change is your true balance-change — you can't hide the ₹5 lakh your uncle gifted you. But if you *label* that ₹5 lakh "gift — one-time," the reader can see that your *recurring* monthly income is really ₹80,000, not ₹80,000 + a windfall. You didn't lie about the total; you just made the total *decomposable*.

AS 5 gives you three "labels" (categories that must be shown separately) and three "correction mechanisms" (how you handle things from the past or things that change). That's the whole standard. Everything else is detail hanging off these two skeletons:

**Labels for the current period's profit:**
- Profit from **ordinary activities** (the recurring engine),
- **Extraordinary items** (real, but outside the ordinary engine),
- Certain **ordinary items of exceptional size/nature** that still deserve separate disclosure.

**Correction mechanisms for the past and for change:**
- **Prior period items** (things that belong to earlier years, surfacing now),
- **Changes in accounting estimate** (the future was re-guessed — handle it going forward),
- **Changes in accounting policy** (the *method* changed — disclose it, and quantify the impact).

The mental model to carry through the whole chapter: **AS 5 sorts every unusual thing along two axes — WHEN does it belong (this period vs a past period vs the future) and WHY is it unusual (a real business event vs a change in how we measure).** Get those two axes right and every rule below becomes obvious rather than memorised.

## 3. Why it's built this way — what breaks without each rule

Before the technical content, let's earn each rule by watching what goes wrong in its absence.

**Why include everything in net profit (the "no hiding in reserves" rule)?** Historically, managers loved to route embarrassing losses — a big write-off, a lawsuit settlement — *directly to reserves*, bypassing the P&L entirely. The bottom line stayed pretty; the loss quietly reduced equity. This is "reserve accounting," and it destroys the integrity of profit as a performance measure, because you could make any year look good by dumping the bad bits into the balance sheet. AS 5 slams this door: **net profit/loss for the period comprises (a) profit or loss from ordinary activities and (b) extraordinary items — and *all* items of income and expense are included in determining it.** If it's income or expense of the period, it goes *through* profit. No side exits.

**Why separate extraordinary items?** Because of the analyst story in Section 1. If the fire-insurance windfall is buried inside operating profit, next year's forecast inherits a ₹40 crore ghost. Separating it lets the reader compute "profit *before* extraordinary items" — the number that actually has predictive value.

**Why a *separate* category for prior period items rather than just fixing last year?** Two reasons. First, you cannot un-publish last year's audited accounts — they've been filed, distributed, relied upon. Second, if you silently absorbed last year's ₹9 crore repair bill into this year's ordinary expenses, this year's *ordinary* performance would look worse than it truly was, for a reason that has nothing to do with this year. So AS 5 says: put it in *this* year's profit (you have to — it's being recognised now), but *label* it "prior period item," so the reader knows to exclude it when judging *this* year's operations.

**Why is a change in *estimate* handled prospectively (going forward), while a change in *policy* demands full disclosure and impact quantification?** This is the subtlest and most examined distinction, so let's nail the logic. An estimate is an inherent, honest guess about the future — the useful life of a machine, the % of debtors who'll default, the warranty claims that will come. When new information arrives and you revise the guess, *nothing was wrong before*. You made the best estimate with the information you had; now you have better information. There was no error and no method-change. Reopening the past would punish an honest, unavoidable feature of accounting. So you simply carry the new estimate forward. A *policy*, by contrast, is a *choice of method* — FIFO vs weighted average, cost model vs revaluation. Changing it makes this year's numbers non-comparable with last year's for a reason the reader can't see. So AS 5 demands you *quantify and disclose* the impact, restoring the reader's ability to compare like with like.

**Why is an *error* different from both?** If last year you simply got it wrong — arithmetic mistake, misread contract, omitted a transaction — that's not an honest estimate and not a method-change. It's a prior period item (an error/omission surfacing now), disclosed separately so it doesn't contaminate this year's ordinary profit.

Notice the elegant symmetry: **estimate change = no one was wrong, look forward. Error = someone was wrong, disclose the correction. Policy change = the ruler changed, disclose the impact.** Everything in AS 5's back half is these three cases.

## 4. Full Technical Content — the RMPD lens

AS 5 is primarily a **presentation and disclosure** standard. It does *not* tell you *whether* to recognise income/expense (that's the job of AS 9, AS 10, AS 2, etc.) or *how much* to measure it at. It tells you how to *classify and disclose* what other standards have already recognised. Keep that scope in mind — examiners love to test it (Section 8).

### 4.1 The anatomy of net profit or loss

> **Net profit or loss for the period = Profit/loss from Ordinary Activities + Extraordinary items.**

Both components must be recognised in the Statement of Profit and Loss and disclosed on the face of the statement. This is the anti-reserve-accounting backbone.

**Ordinary activities** = any activities undertaken by an enterprise as part of its business, *and* such related activities in which the enterprise engages in furtherance of, incidental to, or arising from these activities. The word to feel is *"related / incidental / arising from."* A manufacturer's sale of goods is ordinary. So is the sale of a used delivery van, the writing-down of obsolete inventory, a foreign-exchange loss on a trade payable, a bad-debt write-off. These are *not* the core, but they *arise from* running the business. They are ordinary.

### 4.2 Extraordinary items (Recognition of the label + Presentation)

**Definition:** Extraordinary items are income or expenses that arise from events or transactions that are (a) **clearly distinct from the ordinary activities** of the enterprise and (b) therefore **not expected to recur frequently or regularly.**

Both tests must be met: *distinct from ordinary* **and** *not expected to recur*. The recurrence test alone is not enough — an event can be rare yet still ordinary (a large but once-a-decade export order is rare, but selling goods is your ordinary business).

**Presentation rule:** The **nature and amount** of each extraordinary item should be **separately disclosed** in the Statement of Profit and Loss in a manner that its **impact on current profit or loss can be perceived.** In practice this means you present "Profit before extraordinary items," then the extraordinary item, then "Net profit." The reader can lift the extraordinary line out and see the recurring base.

**Classic textbook examples of extraordinary items:**
- Loss of assets / claims from an earthquake, flood, or fire (a genuine natural catastrophe),
- Attachment or confiscation of property by a government (expropriation),
- The proceeds/loss on such events.

**Crucial caveat the examiner exploits:** whether an item is extraordinary depends on *the nature of the event in relation to the business of the enterprise.* An event ordinary for one entity may be extraordinary for another. Flood losses are extraordinary for most factories — but for an insurance company that *insures against floods*, flood-related payouts are its *ordinary* business. Always ask: "distinct from *this* entity's ordinary activities?"

### 4.3 Exceptional items — ordinary in nature, but disclosed for size

Here is a category students constantly conflate with "extraordinary." AS 5 recognises that **certain items, though part of ordinary activities, are of such size, nature or incidence that their separate disclosure is needed to explain the performance of the enterprise.** These are *not* extraordinary — they arise from ordinary activities — but they're big or unusual enough that a reader should see them broken out. The standard requires their **nature and amount to be disclosed separately** (typically in the notes, or as a separate line within ordinary profit — often called "exceptional items" in practice).

The standard gives a specific, examinable list of circumstances that may give rise to such separate disclosure:

1. The **write-down of inventories** to net realisable value (and its reversal),
2. A **restructuring** of the activities of an enterprise and the **reversal of any provisions** for the costs of restructuring,
3. **Disposals of items of fixed assets** (profit/loss on sale of PPE),
4. **Disposals of long-term investments**,
5. **Legislative changes** having retrospective application,
6. **Litigation settlements**, and
7. Other **reversals of provisions.**

Memorise the *spirit*, not just the list: these are all things that happen *within* ordinary business but are lumpy, occasional, or large. They stay inside "profit from ordinary activities" (unlike extraordinary items, which are shown as a distinct block after ordinary profit), but their *nature and amount* are disclosed so performance is understood.

> **The one-line discriminator:** Extraordinary = *distinct from* ordinary activities → shown as a separate block *after* profit from ordinary activities. Exceptional = *part of* ordinary activities but big/unusual → disclosed separately *within* ordinary profit. Both get separate disclosure; only extraordinary sits outside the ordinary line.

### 4.4 Prior period items (Definition, Recognition, Presentation, Disclosure)

**Definition:** Prior period items are **income or expenses which arise in the current period as a result of errors or omissions in the preparation of the financial statements of one or more prior periods.**

Dissect this definition — the examiner tests every word:
- **"Errors or omissions"** — the trigger is a *mistake* (mathematical error, mistake in applying an accounting policy, oversight, misinterpretation of facts, or fraud) or an *omission* (something that should have been recorded but wasn't). It is **not** an estimate that later turned out different — that's a change in estimate, not a prior period item (this is the single most common trap; see 4.5).
- **"Arise in the current period"** — the item *surfaces* now, even though it *belongs* to a past period.
- **"Preparation of financial statements of prior periods"** — it relates to an earlier year's accounts.

**Recognition & Presentation:** Prior period items are **included in the determination of net profit or loss for the current period.** (You *don't* restate/reopen last year's published accounts under AS 5 — contrast with Ind AS 8, which *does* require retrospective restatement; flag this contrast, Section 7.) But they must be **separately disclosed** in the Statement of Profit and Loss in a manner that their **impact on the current profit or loss can be perceived.**

Two acceptable presentation methods:
1. Show the prior period items **after determination of current net profit or loss**, as a distinct line (e.g., "Net profit before prior period items," then the prior period item, then "Net profit for the period"); or
2. Include them in the determination of net profit but **disclose the amount and nature separately** (often in the notes) so the reader can gauge their effect.

**Watch the boundary — what is NOT a prior period item:**
- The **difference between an earlier estimate and the actual outcome** is *not* a prior period item (e.g., bad debts of ₹3 lakh provided last year, but ₹3.4 lakh actually written off this year — the extra ₹40,000 is not a prior period item; it's just this year's expense from a change in estimate).
- **Normal recurring adjustments** — e.g., income-tax adjustments finalised in the current year, or arrears of a wage revision agreed this year — depend on facts, but a routine settlement that reflects *this year's* negotiation is a current-period item, not a prior period item. Only genuine *errors/omissions* of past accounts qualify.

### 4.5 Changes in accounting estimates (the prospective machine)

**Why estimates exist:** Because business is uncertain, many financial-statement items *cannot* be measured with precision — they can only be *estimated*. Examples: useful life and residual value of a depreciable asset, the allowance for doubtful debts, the provision for warranty claims, obsolescence of inventory, fair value guesses. Estimation is not a weakness of accounting; it is unavoidable, and using estimates *does not undermine* reliability.

**The rule (Recognition/Measurement of the change):** An estimate may need revision when the circumstances on which it was based change, or as a result of new information or more experience. **The revision of an estimate, by its nature, does not bring the adjustment within the definitions of an extraordinary item or a prior period item.** The effect of a change in an accounting estimate is included in the determination of net profit or loss in:
- **the period of the change**, if the change affects that period only (e.g., a change in the estimate of bad debts affects only the current year); **or**
- **the period of the change and future periods**, if the change affects both (e.g., revising the useful life of an asset changes depreciation for the current *and* remaining years).

This is called **prospective application** — you never touch the past; you fold the new estimate into the current and future periods. *Why?* Because (Section 3) nothing was wrong before; the estimate was honest given what was known.

**Classification of the effect:** The effect of a change in estimate is included in the *same income/expense classification* as was previously used for the estimate. So a change in the estimate of depreciation flows through the same "depreciation" line; a change in bad-debt estimate flows through the same "provision for doubtful debts" line. This keeps the P&L comparable line-by-line.

**Disclosure:** The **nature and amount of a change in an accounting estimate which has a material effect** in the current period (or which is expected to have a material effect in subsequent periods) should be **disclosed.** If the amount is impracticable to quantify, disclose that fact.

**The grey-zone rule (memorise this — it's a favourite):** *Sometimes it is difficult to distinguish between a change in accounting policy and a change in an accounting estimate. In such cases, the change is treated as a change in an accounting estimate, with appropriate disclosure.* The default, when genuinely ambiguous, is **estimate** (prospective) — because policy changes carry the heavier restriction (see 4.6).

### 4.6 Changes in accounting policy (Definition, the three triggers, Disclosure)

**What is an accounting policy?** (From AS 1, the sister standard — see Section 7.) Accounting policies are the **specific accounting principles and the methods of applying those principles** adopted by an enterprise in preparing and presenting financial statements — e.g., the method of depreciation (SLM vs WDV), the cost formula for inventory (FIFO vs weighted average), the basis of valuing investments, treatment of goodwill.

**The core restriction — policies should be consistent:** A change in accounting policy should be made **only if**:
1. it is **required by statute**, or
2. it is **required for compliance with an Accounting Standard**, or
3. it is considered that the change would result in a **more appropriate presentation** of the financial statements of the enterprise.

You cannot change a policy on a whim; consistency (an AS 1 fundamental assumption) is the default, because comparability is precious.

**What is NOT a change in accounting policy (examinable list):**
- The **adoption of a policy for events/transactions that differ in substance** from those previously occurring (a genuinely new kind of transaction — a new policy, not a *change*),
- The **adoption of a new policy for events/transactions that did not occur previously or were immaterial** (e.g., first-time depreciation policy for a new class of asset).

**Disclosure — the heart of the rule:**
- **Any change in an accounting policy which has a material effect** should be **disclosed.** The **amount** by which any item in the financial statements is affected by the change should also be disclosed **to the extent ascertainable.** Where such amount is **not ascertainable**, wholly or in part, **the fact should be indicated.**
- If a change in policy **has no material effect in the current period but is reasonably expected to have a material effect in later periods**, the fact of the change should be **appropriately disclosed** in the current period (so future readers are pre-warned).

**Note on treatment under AS (vs Ind AS):** Under Indian AS 5, the effect of a change in policy is generally recognised in the *current* period's profit or loss with disclosure of the amount (there is no mandatory retrospective restatement of prior-year comparatives as under Ind AS 8). The examinable requirement is the *disclosure of the amount and the fact* — not a restatement.

### 4.7 The decision tree — how to classify anything AS 5 throws at you

```
An unusual/one-off/changed item appears. Ask, in order:

Q1. Is it income/expense of THIS period at all, or a re-guess of the FUTURE?
    → If it re-guesses the future (life, provision, NRV): CHANGE IN ESTIMATE
      → apply prospectively (current + future periods); disclose if material.

Q2. Does it BELONG to a prior period (arises now due to an ERROR or OMISSION)?
    → YES: PRIOR PERIOD ITEM
      → include in current profit, but disclose nature & amount separately.
    (Beware: estimate-vs-actual difference is NOT a prior period item.)

Q3. Did the METHOD/PRINCIPLE change (SLM↔WDV, FIFO↔WA, cost↔revaluation)?
    → YES: CHANGE IN ACCOUNTING POLICY
      → allowed only if statute / AS / more appropriate presentation;
        disclose the change AND the amount of impact (or state 'not ascertainable').

Q4. Is it a real event DISTINCT from ordinary activities & not expected to recur?
    → YES: EXTRAORDINARY ITEM → separate block after ordinary profit.
    → NO (part of ordinary activities but large/unusual): EXCEPTIONAL ITEM
      → disclose nature & amount within ordinary profit.

If genuinely torn between POLICY and ESTIMATE → treat as ESTIMATE.
```

## 5. Worked Examples

### Example 1 (easy) — Classifying five items

Rane Ltd, a car-components manufacturer, reports the following in the year ended 31 March 2026. Classify each per AS 5 and state the presentation.

| # | Item | ₹ |
|---|------|---|
| a | Loss of raw materials in a flood at the Chennai plant | 22,00,000 |
| b | Profit on sale of an old CNC machine | 4,50,000 |
| c | Write-down of obsolete inventory to NRV | 6,00,000 |
| d | Interest income on a fixed deposit of surplus cash | 1,20,000 |
| e | Bad debts written off | 3,00,000 |

**Reasoning:**
- **(a) Flood loss → Extraordinary item.** A flood is clearly distinct from making car components and not expected to recur regularly. Present as a separate block *after* "profit from ordinary activities," disclosing nature and amount so its impact is perceivable.
- **(b) Profit on sale of machine → Ordinary, but exceptional-type disclosure.** Selling a fixed asset *arises from* ordinary activities (it's on AS 5's list of items warranting separate disclosure due to nature/size). Not extraordinary. Disclose nature and amount separately *within* ordinary profit if material.
- **(c) Inventory write-down to NRV → Ordinary; separate disclosure.** Explicitly on the AS 5 list. Part of ordinary activities; disclose separately if size warrants.
- **(d) Interest on surplus-cash FD → Ordinary income.** Incidental to running the business; nothing unusual. No special disclosure.
- **(e) Bad debts → Ordinary expense.** Arises from ordinary trading. No extraordinary treatment.

**Takeaway:** Only the flood is *outside* ordinary activities. Everything else is ordinary — some (b, c) merely deserve *separate disclosure* for size/nature, which is a different thing from being extraordinary.

### Example 2 (medium) — Change in estimate: revising useful life

Vega Ltd bought a machine on 1 April 2022 for ₹50,00,000, estimated life 10 years, nil residual value, straight-line. On 1 April 2025 (start of Year 4), based on new technical assessment, management concludes the *total* useful life is only 8 years (not 10). How is this handled, and what is the depreciation for FY 2025-26?

**Step 1 — Classify.** Useful life is an *estimate*. Revising it because of new technical information is a **change in accounting estimate**, not a policy change and not a prior period item. → **Prospective** treatment. We do *not* touch FY23, FY24, FY25 depreciation already charged.

**Step 2 — Depreciation already charged (Years 1–3, at old estimate).**
Annual SLM = 50,00,000 / 10 = ₹5,00,000.
Three years charged = 3 × 5,00,000 = ₹15,00,000.
Carrying amount on 1 April 2025 = 50,00,000 − 15,00,000 = **₹35,00,000.**

**Step 3 — Apply the new estimate prospectively.** Total life now 8 years; 3 already elapsed → **5 years remaining.** Spread the *current carrying amount* over the *remaining* life:
Revised annual depreciation = 35,00,000 / 5 = **₹7,00,000 per year** for FY26 through FY30.

**Step 4 — Presentation & disclosure.** The extra ₹2,00,000 (₹7,00,000 vs old ₹5,00,000) flows through the *same* depreciation line (same classification). If material, disclose the *nature and amount* of the change in estimate. No restatement of prior years.

**Why this is right:** In FY22–FY25 the 10-year estimate was the honest best guess. Nothing was "wrong," so we don't reopen the past — we simply depreciate the *remaining book value over the remaining life.*

### Example 3 (medium-hard) — Prior period item vs change in estimate

In FY 2025-26, Meridian Ltd's accountant discovers three things. Classify each and state the P&L effect.

1. Sales invoice of ₹8,00,000 dated **March 2025** (last year) was **completely omitted** from FY 2024-25's books; it's being recorded now.
2. Depreciation in FY 2024-25 was computed as ₹12,00,000 but, due to a **formula error in the spreadsheet**, should have been ₹14,00,000 — a ₹2,00,000 under-charge.
3. A **provision for warranty** of ₹5,00,000 was made in FY 2024-25; actual warranty claims settled in FY26 came to ₹5,90,000.

**Item 1 — Omitted sales invoice → PRIOR PERIOD ITEM (income).** It's income that *belongs to* FY25 but arises now due to an **omission**. Recognise the ₹8,00,000 income in FY26's profit, but **disclose it separately** as a prior period item so FY26's *ordinary* performance isn't overstated by last year's sale.

**Item 2 — Depreciation formula error → PRIOR PERIOD ITEM (expense).** A ₹2,00,000 under-charge caused by an *error* in preparing FY25's statements. Charge the ₹2,00,000 additional depreciation in FY26, **disclosed separately** as a prior period item. (Note: it's an *error*, so prior period — contrast with Example 2, where the *same* line, depreciation, changed for a non-error reason and was an *estimate change*.)

**Item 3 — Warranty ₹5,00,000 estimated vs ₹5,90,000 actual → CHANGE IN ESTIMATE, not a prior period item.** The FY25 provision was an honest *estimate*; the ₹90,000 shortfall is simply the difference between estimate and outcome. Per AS 5, an estimate-vs-actual difference is **expressly not** a prior period item. The extra ₹90,000 is a *current-period* expense (change in estimate), flowing through the normal warranty/provision line — **no separate prior-period disclosure.**

**The lesson (this is the exam's favourite trap):** Items 2 and 3 both concern "last year's number turned out different this year," yet they are treated oppositely. The discriminator is **error vs estimate.** Item 2 was a *mistake* (formula error) → prior period item, disclosed. Item 3 was an honest *estimate* that missed → change in estimate, ordinary current expense. Always ask: *was someone wrong, or did the world simply differ from an honest guess?*

### Example 4 (exam-hard) — Change in policy with impact quantification

Kaveri Textiles has always valued inventory at **weighted-average cost**. From FY 2025-26 it switches to **FIFO**, believing FIFO gives a more appropriate presentation given rapidly rising cotton prices. Data:

- Closing inventory 31 Mar 2026 under weighted average = ₹40,00,000; under FIFO = ₹46,00,000.
- Opening inventory 1 Apr 2025 (i.e., FY25 closing) under weighted average = ₹30,00,000; had FIFO been used it would have been ₹33,00,000.
- Net profit for FY26 as computed *using weighted average* = ₹80,00,000.

**Step 1 — Classify.** Changing the *cost formula* for inventory (WA → FIFO) is a change in the **method of applying an accounting principle** = a **change in accounting policy.** It is permitted here because management believes it yields a *more appropriate presentation* (one of the three valid triggers). This must be *disclosed* along with the *amount of the impact.*

**Step 2 — Effect on current-year profit.** Profit is affected through both opening and closing inventory:
- Higher **closing** inventory raises profit: 46,00,000 − 40,00,000 = **+₹6,00,000.**
- Higher **opening** inventory *lowers* profit (higher opening stock = higher cost of goods sold): effect = −(33,00,000 − 30,00,000) = **−₹3,00,000.**

Net effect of the policy change on FY26 profit = +6,00,000 − 3,00,000 = **+₹3,00,000.**

**Step 3 — Restated profit and disclosure.**
Profit under FIFO ≈ 80,00,000 + 3,00,000 = **₹83,00,000.**

Disclosure in the notes should read, in substance:

> *"During the year, the company changed its method of valuing inventories from weighted-average cost to FIFO, as management considers FIFO to result in a more appropriate presentation. Consequent to this change, the net profit for the year is higher by ₹3,00,000."*

If any part of the impact were **not ascertainable**, the company would state that fact. Because the change has a material effect, disclosure is mandatory.

**Step 4 — Why not treat it prospectively like an estimate?** Because it is a *method* change, not a re-guess of the future. A method change makes this year's numbers non-comparable with last year's *unless the reader is told the rupee impact.* Hence: disclose the change **and quantify it.** (Contrast Example 2, an estimate change, where no impact-quantification of the *cumulative* past is required — only prospective application plus nature/amount disclosure of the current effect.)

## 6. Presentation & Disclosure formats

**On the face of the Statement of Profit and Loss** (illustrative structure AS 5 drives):

```
Revenue from operations                                     XXX
Other income                                                XXX
Total income                                                XXX
Expenses (materials, employee, finance, depreciation, ...)  XXX
------------------------------------------------------------
Profit before exceptional & extraordinary items and tax     XXX
Exceptional items (disclosed separately, ordinary in nature)(XX)   <- e.g. profit/loss on sale of PPE,
Profit before extraordinary items and tax                   XXX          inventory write-down, restructuring
Extraordinary items (nature & amount shown)                (XX)    <- e.g. flood/earthquake loss, expropriation
------------------------------------------------------------
Profit before tax                                           XXX
Tax expense                                                (XX)
------------------------------------------------------------
Profit for the period from ordinary + extraordinary         XXX
Prior period items (separately disclosed)                  (XX)    <- error/omission of prior years
------------------------------------------------------------
Net profit for the period                                   XXX
```

The essential idea: a reader can start from the bottom and *strip away* prior-period items, extraordinary items, and exceptional items to arrive at **profit from ordinary, recurring activities** — the predictive base.

**Disclosure checklist (what notes must carry):**

| Situation | Mandatory disclosure |
|-----------|----------------------|
| Extraordinary item | Nature and amount, on the face of the P&L, so impact is perceivable |
| Exceptional (ordinary but large/unusual) item | Nature and amount, separately |
| Prior period item | Nature and amount, separately, in P&L (impact perceivable) |
| Change in accounting estimate | Nature and amount, if material this period or expected material later; if impracticable to quantify, state so |
| Change in accounting policy | The fact of change; the amount of impact (to the extent ascertainable); if not ascertainable, state the fact; if no current effect but expected material later, disclose the fact now |

**Note under Schedule III (Companies Act):** Schedule III presentation uses "Exceptional items" and "Extraordinary items" line items consistent with AS 5, and requires prior period items to be disclosed. (For companies on Ind AS, the "extraordinary items" concept is *removed* — see Section 7.)

## 7. Connections

- **AS 1 (Disclosure of Accounting Policies):** AS 1 defines *accounting policies* and enshrines **consistency** as a fundamental assumption; AS 5 supplies the *procedure* when that consistency is broken (change in policy) — the two are a matched pair. AS 1 says "be consistent and disclose your policies"; AS 5 says "if you must change, here's how to disclose the change and its impact."
- **AS 10 (Property, Plant & Equipment) / depreciation:** Useful life, residual value, and *method* of depreciation live at the AS 5 fault-line. Revising **life or residual value** = change in **estimate** (prospective — Example 2). Changing the **method** (SLM ↔ WDV) is now treated, under revised AS 10, as a **change in estimate** applied prospectively — a subtle point: even though "method" sounds like a policy, AS 10 specifically classifies a depreciation-method change as a change in *estimate*. Keep this exception in mind (many older texts called it a policy change; the current position aligns it with estimate).
- **AS 2 (Valuation of Inventories):** The cost formula (FIFO/weighted average) is a *policy*; switching it is a change in policy (Example 4). Inventory write-down to NRV is an *ordinary but separately-disclosed* item.
- **AS 4 (Contingencies & Events After the Balance Sheet Date):** Distinguish a *prior period item* (error/omission of an earlier year) from an *adjusting event after the balance sheet date* (new information about conditions existing at the year-end). Different standards, different mechanics.
- **AS 22 (Accounting for Taxes on Income):** Prior period tax adjustments and the tax effect of extraordinary items interact with AS 5's classification.
- **Ind AS 8 contrast (very examinable):** Ind AS 8 (a) **abolishes the "extraordinary items" category** — nothing may be labelled extraordinary; (b) requires **retrospective restatement** of prior-period *errors* and of *changes in policy* (restate comparatives, adjust opening retained earnings) — *unlike* AS 5, which keeps them in the *current* period with disclosure. Changes in *estimate* remain **prospective** under both. If a question mentions Ind AS, switch to restatement thinking.
- **Financial Management / Equity Research:** The whole "profit before extraordinary items" idea *is* the analyst's normalised/recurring earnings — AS 5 is the accounting embodiment of the FM concept of *sustainable earnings* used in valuation.
- **Audit:** Auditors specifically test classification of extraordinary/exceptional/prior period items and the adequacy of policy-change disclosures — a favourite audit-report qualification area.

## 8. Traps & Examiner Tricks

1. **"Rare = extraordinary."** *False.* Both tests must hold: distinct from ordinary activities *and* not expected to recur. A once-a-decade bumper export order is rare but *ordinary*. Recurrence alone never makes something extraordinary.
2. **Entity-specific classification.** A flood loss is extraordinary for a factory but *ordinary* for a flood-insurer. Always classify *relative to the specific entity's business.*
3. **Estimate-vs-actual masquerading as a prior period item.** Bad debts provided ₹3,00,000, actual write-off ₹3,40,000 → the ₹40,000 is a **change in estimate** (current expense), **not** a prior period item. The examiner loves to phrase this as "prior year's provision fell short — is it a prior period item?" Answer: **No.**
4. **Depreciation-method change misclassified.** Under current AS 10, changing SLM↔WDV is a **change in estimate (prospective)**, *not* a change in policy — despite "method" sounding policy-like. Contrast: changing *inventory cost formula* (FIFO↔WA) *is* a policy change. Don't cross the wires.
5. **"Take the loss to reserves to protect profit."** Forbidden. All income/expense of the period goes *through* net profit. Any question that routes an operating loss straight to reserves is testing this — flag it as non-compliant.
6. **Confusing extraordinary with exceptional.** Profit on sale of fixed assets, inventory write-down, restructuring, litigation settlement = *ordinary but separately disclosed (exceptional)* — **not** extraordinary. Extraordinary is reserved for events *outside* ordinary activities (natural disaster, expropriation).
7. **Policy change without a valid trigger.** A change in policy is allowed *only* if required by statute, required by an AS, or for more appropriate presentation. A question where management switches methods "to boost profit" is an *invalid* change — flag it.
8. **Forgetting the "amount" in policy-change disclosure.** Disclosing merely *that* a policy changed is incomplete; you must disclose the **rupee impact to the extent ascertainable**, or state that it is not ascertainable. Students routinely lose marks by writing the narrative but omitting the quantification.
9. **Reopening prior years under AS (not Ind AS).** Under AS 5 you do **not** restate last year's published accounts for prior period items or policy changes — you take them through the *current* year with disclosure. Restatement is an *Ind AS 8* behaviour. Mixing the two loses marks.
10. **The ambiguous case default.** When you genuinely can't tell policy from estimate, AS 5 says treat it as a **change in estimate** (prospective) with disclosure. Don't default to policy.

## 9. First-Principles Recap

- A single profit figure must serve two masters — *report the period* and *predict the future* — so AS 5 keeps everything *in* profit but forces it to be *decomposable*.
- **Nothing hides in reserves.** Net profit = ordinary-activity result + extraordinary items; all income/expense flows through it.
- **Two axes classify everything:** *when* it belongs (past / present / future) and *why* it's unusual (real event / measurement change).
- **Extraordinary** = distinct from ordinary activities *and* not recurring → separate block after ordinary profit. Judge relative to *this* entity.
- **Exceptional** = ordinary in nature but large/unusual (asset sales, write-downs, restructuring, litigation) → separate disclosure *within* ordinary profit.
- **Prior period item** = an *error or omission* of a past year surfacing now → put in current profit, disclose separately. An estimate-vs-actual gap is *never* a prior period item.
- **Change in estimate** = an honest re-guess of the future (life, provisions, NRV) → *prospective* (current + future periods), same line classification, no restatement. *Nothing was wrong before.*
- **Change in policy** = the *method/principle* changed → allowed only if statute / AS / more appropriate presentation; disclose the change **and** quantify the impact.
- **Error → disclose; Estimate → look forward; Policy → quantify the impact.** That triad is the entire back half of AS 5.
- When policy vs estimate is genuinely unclear, **treat as estimate.**

## 10. Quick-Revision Sheet

**Net profit = Profit/loss from ordinary activities + Extraordinary items.** (All income/expense included; nothing to reserves.)

| Category | Test | Where shown | Disclose |
|----------|------|-------------|----------|
| **Ordinary** | Business + related/incidental/arising activities | Within operating result | Normal |
| **Exceptional** | Ordinary in nature but big/unusual (PPE sale, NRV write-down, restructuring, litigation, retrospective law change) | *Within* ordinary profit, separate line | Nature + amount |
| **Extraordinary** | Distinct from ordinary *and* not expected to recur (flood, earthquake, fire, expropriation) | *Separate block after* ordinary profit | Nature + amount, impact perceivable |
| **Prior period item** | Income/expense from *error or omission* of a prior year, arising now | In current profit, separate line | Nature + amount, impact perceivable |

**Change mechanics:**

| Change type | Trigger | Treatment | Disclosure |
|-------------|---------|-----------|-----------|
| **Estimate** | New info / more experience (life, residual value, bad debts, warranty, NRV) | **Prospective** — current (+ future) periods; same classification | Nature + amount if material (or state impracticable) |
| **Policy** | Only if statute / AS / more appropriate presentation (SLM↔WDV is *estimate* per AS 10; FIFO↔WA is *policy*) | Current period + disclosure (no AS restatement) | Fact of change + **amount of impact** (or "not ascertainable"); pre-warn if future material |
| **Error/omission** | Mistake in a prior year | Prior period item — current profit | Nature + amount, separate |

**Golden discriminators:**
- Rare ≠ extraordinary (need *distinct from ordinary* too).
- Estimate-vs-actual gap = change in estimate, **not** prior period item.
- Depreciation *method* change = **estimate** (prospective, per AS 10); inventory *cost formula* change = **policy**.
- Ambiguous policy/estimate → treat as **estimate**.
- Ind AS 8 contrast: **no** "extraordinary" category; errors & policy changes are **restated retrospectively**; estimates stay prospective.

**Depreciation-on-revised-life formula (Example 2):**
Revised annual depreciation = (Carrying amount at date of change − revised residual value) ÷ remaining useful life.

**Policy-change profit impact (Example 4):**
Effect on profit = Δ closing inventory − Δ opening inventory (higher opening stock reduces profit via higher COGS).
