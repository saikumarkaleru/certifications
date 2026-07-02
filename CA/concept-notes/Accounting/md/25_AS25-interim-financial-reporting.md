# Chapter 25 — AS 25: Interim Financial Reporting

## 1. The Problem

Imagine you are a lender, an equity analyst, or a regulator watching a listed company. The company publishes a full, audited set of financial statements **once a year** — say for the year ended 31 March. Now put yourself in July. The last picture you have of this business is four months old. In those four months, interest rates may have moved, a factory may have flooded, a competitor may have launched a product, the company may have raised or lost a huge contract. Yet the numbers you are staring at describe a world that no longer exists.

Annual reporting has a **staleness problem**. Financial statements are useful only if they are *timely*, and once-a-year is not timely enough for capital markets that price securities every second. The regulator's answer (SEBI's Listing Regulations) is to force listed companies to publish **quarterly** results. That solves timeliness — but immediately creates three brand-new accounting problems:

1. **The chopping problem.** A year is a natural accounting period — you buy assets, consume them, sell goods, and close the books. A *quarter* is an artificial slice. How do you cut a continuous business into three-month pieces without distorting each piece? Costs and revenues do not fall neatly into calendar quarters.

2. **The seasonality problem.** A woollen-garment maker earns almost nothing in the June and September quarters and makes its entire profit in December–March. A crackers manufacturer sells everything around Diwali. If you report a naked June-quarter loss, is that a "loss" — or just the shape of the year? Should you *smooth* it out so every quarter looks similar?

3. **The lumpy-cost problem.** Some costs hit once a year — a bonus declared in Q4, an advertising blitz in Q2, a major repair, property tax paid annually, staff welfare at year-end. Do you dump the whole cost into the quarter it is paid, or spread it across quarters?

There is also a **content problem**. A full annual report is a heavy document — full balance sheet, full P&L, cash flow, dozens of note-schedules, directors' report. Must a company reproduce *all* of that four times a year? That would be enormously costly and would drown the reader. So what is the *minimum* a useful interim report must contain?

AS 25 exists to answer exactly these four questions: **what** an interim report must contain, and **how** you measure the numbers in it — especially seasonal revenue and lumpy costs.

> **One-line framing:** AS 25 is the rulebook for slicing a year into pieces without lying about any piece.

---

## 2. The Core Idea (analogy)

Think of a **film versus a photograph**.

The annual financial statements are a *photograph* taken at year-end plus a summary of the whole film. An interim report is a **still frame pulled from the middle of the film**. The central design question is: *what does that middle frame mean on its own?*

There are two philosophies for how to treat a mid-film frame:

- **The "integral" view — the frame belongs to the whole film.** Under this view, each quarter is just a *part* of the annual whole. The purpose of a quarter's numbers is to *predict* and *build toward* the annual figure. So you are allowed to smooth, defer, and anticipate: if you know a big annual cost is coming, you accrue a slice of it each quarter; if a quarter is seasonally strong, you may defer some profit to help the weak quarters. The quarter is a *forecasting instrument*.

- **The "discrete" view — the frame is its own photograph.** Under this view, each interim period is a **standalone reporting period**. You apply the *same* recognition and measurement rules you would apply if that quarter were a mini-year. A cost is recognised when it meets the definition of an expense in that period — not spread just because it is "annual" in flavour. Revenue is recognised when earned — even if that makes the quarter look lumpy. The quarter tells the truth about itself, warts and all.

**AS 25 chooses the discrete view for recognition and measurement** — with one crucial, sensible exception baked into how you *compute* the numbers (the "year-to-date" mechanism, explained in Part 4). The reason for choosing discrete is the theme of this whole chapter: *smoothing hides information*. If a June-quarter loss is real, the market deserves to see it. Papering over seasonality would defeat the entire purpose of interim reporting, which was **timely, honest information**.

Hold onto this single sentence: **treat each interim period basically as if it were a small, independent accounting period — recognise costs and revenues by the same rules as an annual period — but measure cumulatively from the start of the year.**

---

## 3. Why It's Built This Way

Let's earn each of AS 25's big design choices from first principles, so nothing needs memorising.

**Why discrete, not integral?**
The whole reason SEBI forced quarterly reporting was that annual data is stale and users want the *real* mid-year situation. If the accounting standard then let managers *smooth* the quarters to look uniform, users would be back to a fiction — a manufactured picture rather than the truth. Smoothing also hands management a dangerous lever: "defer profit from a good quarter, release it in a bad quarter" is precisely how earnings management and fraud begin. So the standard's spine is: **the quarter must not deliberately anticipate future events or defer present ones just to look smooth.** A cost that *is* an expense of Q1 stays in Q1. Revenue earned in Q3 stays in Q3.

**Why then a "year-to-date" measurement, which sounds integral?**
Here is the subtlety students trip on. AS 25 says the *frequency* of reporting should not change the *annual* result. If you measured each quarter in complete isolation and simply added four quarters, you could get an annual figure different from what you'd get by measuring the year as one period — because of how estimates and thresholds work. To prevent that, AS 25 measures things **cumulatively (year-to-date)** and treats the interim period as *part of the annual period for the limited purpose of not letting quarterly slicing change the annual total*. This is not smoothing; it is *consistency*. The classic consequence: if an estimate made in Q1 turns out wrong, you don't restate Q1 — you correct it in a *later* quarter's year-to-date figure. The annual number stays honest; the quarter carries the change when knowledge improves.

**Why a *minimum* set of components, not the full annual report?**
Cost and timeliness. Forcing a full audited annual report four times a year would be so slow and expensive that it would destroy timeliness — the very thing interim reporting exists to deliver. So AS 25 asks only for **condensed** statements plus **selected explanatory notes** — enough for a reader who *already has* the latest annual report to understand *what changed*. Interim reports are built to be read *alongside* the last annual report, not instead of it.

**Why lean so heavily on estimates?**
A three-month deadline is brutal. You cannot do a full physical stock count, full actuarial valuation, or full tax computation every quarter. So AS 25 openly accepts **greater use of estimates** in interim periods than in annual accounts — while insisting the information remains *reliable and relevant*. This is an honest trade-off: a slightly rougher number delivered on time beats a perfect number delivered too late.

```mermaid
flowchart TD
    A["Users need timely mid-year data"] --> B["Regulator mandates quarterly reporting"]
    B --> C["How to measure a 3-month slice?"]
    C --> D["Integral view -- smooth toward annual"]
    C --> E["Discrete view -- quarter stands alone"]
    E --> F["Chosen -- prevents smoothing and earnings management"]
    F --> G["But measure year-to-date so frequency does not change annual result"]
    G --> H["AS 25 recognition and measurement model"]
```
*Figure 1 — The chain of reasoning from the staleness problem to AS 25's discrete, year-to-date model.*

---

## 4. Full Technical Content

This is the part you must know cold for the exam. Every rule below is tied back to the reasoning above.

### 4.1 Objective and Scope

**Objective.** AS 25 prescribes the *minimum content* of an interim financial report and the *recognition and measurement principles* for complete or condensed financial statements for an interim period. Timely and reliable interim reporting improves the ability of investors, creditors, and others to understand an enterprise's capacity to generate earnings and cash flows and its financial condition.

**Scope — a critical exam point.** AS 25 **does not mandate which enterprises must publish interim reports, how frequently, or how soon after period-end.** That is the job of a *statute or a regulator* (e.g., SEBI Listing Regulations, or an RBI/other regulator). **AS 25 only says: IF an enterprise is required or elects to prepare an interim financial report, THEN it should comply with AS 25.** 

There is one nuance in the ICAI text worth stating precisely: if an enterprise's interim report is *described as complying with Accounting Standards*, it must comply with **all** AS 25 requirements. A presentation of only *some* interim information (not claiming full compliance) triggers a specific disclosure (see 4.7). Confirm the exact wording in current ICAI material, but the principle — "AS 25 governs *how*, not *whether*" — is the reliably tested point.

**Interim period** = a reporting period *shorter than a full financial year* (typically a quarter or half-year).
**Interim financial report** = a financial report containing either a *complete* set of financial statements (as per AS 1) or a *set of condensed* financial statements for an interim period.

### 4.2 Minimum Components of an Interim Financial Report

AS 25 permits an enterprise to publish **either** a complete set **or** a condensed set. In practice, listed companies publish **condensed**. The minimum condensed components are:

| # | Component | Minimum form required |
|---|-----------|----------------------|
| (a) | Condensed **Balance Sheet** | Each heading and sub-heading that was in the most recent *annual* balance sheet, plus selected notes |
| (b) | Condensed **Statement of Profit and Loss** | Each heading and sub-heading from the most recent annual P&L, plus selected notes |
| (c) | Condensed **Cash Flow Statement** | Each *major* heading/sub-heading from the most recent annual cash flow statement, plus selected notes |
| (d) | **Selected explanatory notes** | The notes listed in 4.6 below |

**Minimum line items rule:** a condensed statement must include, at minimum, **each of the headings and sub-headings** that were included in the *most recent annual* financial statements, **plus the selected explanatory notes**. **Additional line items are included if their omission would make the condensed statement misleading.** (You compress the detail, but you cannot drop a whole heading that was in the annual accounts.)

**Earnings per share (EPS):** basic and diluted EPS must be presented **on the face** of the Statement of Profit and Loss (complete or condensed) for the interim period. (AS 25 requires EPS presentation where AS 20 applies to the enterprise.)

**Consolidation:** If the enterprise's *annual* statements were consolidated, the interim report should be prepared on a **consolidated** basis. Presenting standalone alongside is optional/consistent with the annual set, but AS 25 does not *require* separate standalone interim statements in addition.

### 4.3 The Periods for Which Interim Statements Are Presented (Comparatives)

This is a favourite exam trap because each statement follows a *different* comparative pattern. Learn the logic, not the grid: **balance sheet is a snapshot (a point in time), so it compares to the last year-end; the flow statements (P&L, cash flow) accumulate over time, so they show both the current period and cumulative year-to-date, each against the corresponding period last year.**

| Statement | Current period columns | Comparative columns |
|-----------|-----------------------|---------------------|
| **Balance Sheet** | As at end of current interim period | As at the immediately preceding **annual** balance sheet date (year-end) |
| **Statement of P&L** | (i) Current interim period **and** (ii) Cumulative **year-to-date** | Comparable interim period **and** comparable year-to-date of the *preceding* financial year |
| **Cash Flow Statement** | Cumulative **year-to-date** for current year | Comparable **year-to-date** of the preceding financial year |

*Worked illustration of the columns — a Q3 (Oct–Dec) report for FY 2025-26:*

- **Balance sheet:** 31 Dec 2025 vs **31 Mar 2025** (last year-end).
- **P&L:** three months Oct–Dec 2025 **and** nine months Apr–Dec 2025 — each shown against Oct–Dec 2024 and Apr–Dec 2024.
- **Cash flow:** nine months Apr–Dec 2025 vs nine months Apr–Dec 2024.

```mermaid
timeline
    title Comparatives for a Q3 interim report FY 2025-26
    section Balance Sheet
        Snapshot now : 31 Dec 2025
        vs last year-end : 31 Mar 2025
    section P and L
        Current quarter : Oct-Dec 2025 vs Oct-Dec 2024
        Year to date : Apr-Dec 2025 vs Apr-Dec 2024
    section Cash Flow
        Year to date only : Apr-Dec 2025 vs Apr-Dec 2024
```
*Figure 2 — Each statement's comparative period; the balance sheet compares to the last year-end, the flow statements accumulate year-to-date.*

### 4.4 Recognition and Measurement — the Heart of AS 25

**Rule 1 — Same accounting policies as annual.** An enterprise applies the **same accounting policies** in its interim statements as in its annual statements, *except* for policy changes made after the last annual statements that will be reflected in the next annual statements. The reason: consistency, and because the frequency of reporting must not change measurement.

**Rule 2 — Frequency of reporting must not affect annual results (the discrete anchor).** Measurements for interim purposes are made on a **year-to-date basis**, so that the frequency of reporting does not affect the measurement of *annual* results. Consequence: **each interim period stands on its own**, but is measured cumulatively.

**Rule 3 — Revenues that arrive seasonally, cyclically, or occasionally are NOT anticipated or deferred.** Such revenue is recognised **when it occurs** — you do not smooth it into other quarters. If a company earns dividend income, or a woollen-maker earns its winter sales, that revenue belongs to the period earned. *Anticipating* future seasonal revenue (booking it early) or *deferring* current seasonal revenue (pushing it to weak quarters) is prohibited — it would be exactly the smoothing that defeats interim reporting.

**Rule 4 — Costs incurred unevenly during the year are anticipated or deferred ONLY IF it would be appropriate to anticipate or defer that cost at the *year-end*.** This is the master test for lumpy costs. Ask: *at annual year-end, would this cost be an asset (deferred) or a liability (accrued in advance)?* 
- If a cost would qualify as an **asset/prepayment** at year-end (e.g., prepaid insurance) → you may carry it forward at interim date too.
- If it would qualify as a **liability/accrual** at year-end (e.g., accrued bonus that meets AS 29 recognition) → you accrue it at interim date too.
- If at year-end it would simply be an **expense when incurred** (no asset, no present obligation earlier) → then at interim date you also expense it *when incurred* — you cannot pre-spread it across quarters just because you *expect* to incur it, and you cannot defer it just because you already paid it.

**Rule 5 — Greater use of estimates.** Interim measurement may rely on estimates to a greater extent than annual measurement, but the information must remain **reliable and relevant**.

**Rule 6 — Change in estimate in a later interim period.** If an estimate reported in an earlier interim period **changes** in a later interim period **of the same year**, the change is accounted for in that *later* period — **you do NOT restate the earlier interim period**. Its nature and amount are disclosed. (This flows directly from AS 5's "change in estimate = prospective".)

### 4.5 Applying the Principles — the Standard's Own Examples (know these)

These are drawn from the illustrative guidance in AS 25 and are extremely commonly tested. Reason each one, don't memorise.

| Item | Interim treatment | Why (first principle) |
|------|-------------------|-----------------------|
| **Employee benefit — payroll tax / insurance paid by employer that is assessed on an annual basis** | Accrue on an **estimated average annual effective rate** basis across interim periods | The obligation builds continuously with employment; at year-end you'd have a liability, so accrue proportionately |
| **Year-end / annual bonus** | Accrue over the year **only if** there is a *present legal or constructive obligation* and a *reliable estimate* (AS 29 test); otherwise recognise when the obligation arises | Anticipate only what would be a liability at year-end |
| **Major planned periodic maintenance / overhaul expected later in the year** | Do **NOT** accrue in earlier interim periods | No present obligation exists yet at interim date; a plan to spend is not a liability — same as at year-end |
| **Volume rebates / discounts to customers, contractually anticipated** | Accrue **if** it is probable they will be earned (a present obligation) | Would be a liability at year-end, so accrue proportionately |
| **Intangible costs / advertising / start-up / training** | Expense as incurred; **do not defer** as an asset merely because future benefit is expected | AS 26 forbids deferral at year-end, so forbidden at interim date too |
| **Depreciation** | Based only on assets **owned during that interim period**; do not include depreciation on assets to be acquired later | Discrete: only actual events of the period count |
| **Foreign exchange / provisions / impairment** | Apply the same AS (AS 11, AS 29, AS 28) at the interim date using conditions then existing | Discrete measurement on the same policies |
| **Inventory valuation** | Same principles (AS 2) — lower of cost and NRV — but may use estimates/interim gross-margin methods for cost | Same policy; estimates permitted for practicality |

### 4.6 Selected Explanatory Notes (the required disclosures)

Because the interim report is read *alongside* the last annual report, the notes focus on **what changed and what is new**, not on repeating unchanged policies. AS 25 requires, at minimum, in the *notes to the interim statements* (year-to-date basis, unless immaterial):

1. A statement that the **same accounting policies** are followed as in the most recent annual statements, or, if changed, a description of the nature and effect of the change.
2. Explanatory comments about the **seasonality or cyclicality** of interim operations.
3. Nature and amount of items affecting assets, liabilities, equity, net income, or cash flows that are **unusual** because of their nature, size, or incidence.
4. Nature and amount of **changes in estimates** of amounts reported in prior interim periods of the *current* year, or in prior financial years, if material to the current interim period.
5. **Issuances, buy-backs, repayments, and restructuring** of debt, equity, and potential equity shares.
6. **Dividends** — aggregate or per share — separately for equity and other shares.
7. **Segment information** (segment revenue, segment result) — required where the enterprise is subject to AS 17 (segment reporting) in its annual statements.
8. **Material events subsequent** to the end of the interim period not reflected in the interim statements.
9. The effect of **changes in the composition** of the enterprise during the interim period — business combinations, acquisition/disposal of subsidiaries and long-term investments, restructurings, discontinuing operations.
10. Material changes in **contingent liabilities** since the last annual balance sheet date.

### 4.7 Compliance Statement and "Complete vs Condensed"

- If the interim report is **described as complying with Accounting Standards**, it must comply with **all** requirements of every applicable standard, and this fact should be disclosed. A report that does not comply with *all* applicable standards should not claim full compliance.
- If an enterprise prepares and presents a **complete** set of financial statements in its interim report, the *form and content* must conform to AS 1's requirements for a complete set.
- If it prepares a **condensed** set, the form and content follow AS 25's minimum-components rule (4.2).

### 4.8 Materiality

Materiality for interim reporting is assessed **in relation to the interim period's financial data — not the annual data.** Interim measurements may rely more on estimates, but items must not be misclassified or omitted if that would mislead a reader of the *interim* period. The reasoning: judging materiality against the whole year would let large interim-period distortions hide inside a big annual number.

```mermaid
flowchart TD
    A["A cost is incurred unevenly in the year"] --> B["At YEAR-END would this be an asset -- prepaid?"]
    B -->|Yes| C["Carry forward -- defer at interim date too"]
    B -->|No| D["At YEAR-END would this be a liability -- present obligation under AS 29?"]
    D -->|Yes| E["Accrue proportionately at interim date"]
    D -->|No| F["Expense in the interim period when incurred -- no pre-spreading no deferral"]
```
*Figure 3 — The master decision test for lumpy costs: anticipate or defer only if you could at year-end.*

---

## 5. Worked Examples

### Example 1 (Easy) — Seasonal revenue is NOT smoothed

**Facts.** Himalaya Woollens Ltd manufactures sweaters. Its sales are highly seasonal. For FY 2025-26 the quarterly sales actually earned are: Q1 (Apr–Jun) Rs 20 lakh; Q2 (Jul–Sep) Rs 30 lakh; Q3 (Oct–Dec) Rs 150 lakh; Q4 (Jan–Mar) Rs 200 lakh. The finance manager proposes to report Rs 100 lakh of revenue in *each* quarter "so the results look stable and comparable."

**Required.** How should each quarter's revenue be reported under AS 25?

**Solution.** Under **Rule 3**, revenues received seasonally or cyclically are recognised **when they occur** and must **not be anticipated or deferred**. Smoothing to Rs 100 lakh a quarter would be exactly the prohibited deferral/anticipation. Therefore report the actual amounts:

| Quarter | Reported revenue (Rs lakh) | Year-to-date revenue (Rs lakh) |
|---------|---------------------------|-------------------------------|
| Q1 | 20 | 20 |
| Q2 | 30 | 50 |
| Q3 | 150 | 200 |
| Q4 | 200 | 400 |

**Reconciliation.** Sum of quarters = 20 + 30 + 150 + 200 = **Rs 400 lakh = the annual figure.** ✔
**Required note:** the company must include an **explanatory comment on the seasonality** of its operations (disclosure item 2), so a reader understands the lumpy Q1/Q2 numbers are normal, not distress.

---

### Example 2 (Medium) — Uneven costs: which to spread, which not

**Facts.** For the quarter ended 30 June 2025 (Q1 of FY 2025-26), Deccan Manufacturing Ltd is finalising its interim results. Consider the following costs relating to the *full year*:

1. **Property tax** of Rs 12 lakh for the year, payable/assessed annually.
2. **Annual advertising campaign** planned for the festive Q3; estimated Rs 40 lakh — nothing spent yet in Q1.
3. **Staff annual bonus** of Rs 24 lakh — there is a long-standing, contractually enforceable bonus scheme; management can reliably estimate it.
4. **Major plant overhaul** scheduled for December 2025, estimated Rs 30 lakh — not yet incurred.
5. **Insurance premium** of Rs 8 lakh paid on 1 April 2025 covering the full year.

**Required.** Determine the amount (if any) of each item to charge to the Q1 interim P&L, applying **Rule 4** (anticipate/defer only if appropriate at year-end).

**Solution — apply the master test item by item:**

| Item | At year-end, asset or liability? | Q1 treatment | Q1 charge (Rs lakh) |
|------|----------------------------------|--------------|---------------------|
| 1. Property tax Rs 12L | It's a cost accruing evenly with the passage of time; at year-end the full year's tax is an expense — accrue ratably | Accrue 3/12 | **3** |
| 2. Advertising Rs 40L (Q3) | Not yet incurred; no obligation at Q1; AS 26 → expense when incurred, cannot defer as asset, cannot pre-accrue | Nothing in Q1 | **0** |
| 3. Bonus Rs 24L | Present legal/constructive obligation + reliable estimate (AS 29) → a liability builds over the year | Accrue 3/12 | **6** |
| 4. Overhaul Rs 30L (Dec) | No present obligation at Q1 (a plan is not a liability); would not be accrued early at year-end | Nothing in Q1 | **0** |
| 5. Insurance Rs 8L paid 1 Apr | Prepaid at year-end for unexpired portion → an asset; expense the expired 3 months | Charge 3/12 | **2** |

**Q1 interim charge total = 3 + 0 + 6 + 0 + 2 = Rs 11 lakh.**

**Full-year reconciliation check (that frequency didn't change annual result):** over four quarters, property tax 12, bonus 24, insurance 8 are each fully expensed; advertising 40 hits when incurred (Q3); overhaul 30 hits when incurred (Q3). Annual total across these items = 12 + 40 + 24 + 30 + 8 = **Rs 114 lakh**, identical to what a once-a-year accounting would record. ✔ Interim slicing changed *timing within the year*, not the annual total.

**Teaching point:** items 2 and 4 are the traps. Both are large, both are "expected", both are tempting to pre-spread across quarters for smoothness — but neither is a liability or asset at year-end before it is incurred, so **zero** in Q1.

---

### Example 3 (Exam-hard) — Estimate change across interim periods + effective annual tax rate

**Facts.** Konkan Chemicals Ltd reports quarterly. Two issues arise in FY 2025-26.

**(A) Income tax — effective annual rate.** The company's pre-tax profit is earned unevenly: Q1 Rs 100 lakh, Q2 Rs 100 lakh, Q3 Rs 300 lakh, Q4 Rs 100 lakh (annual = Rs 600 lakh). At the *start* of the year, the *estimated weighted-average annual effective tax rate* — after considering an expected R&D deduction and a slab structure — is **25%**. AS 25/AS 22 require interim tax to be accrued using the **estimated average annual effective tax rate** applied to year-to-date pre-tax profit.

**(B) Change in estimate.** At the end of Q3, a change in tax law removes part of the expected R&D benefit, and the best estimate of the annual effective rate is revised **upward to 30%**. 

**Required.** Compute the tax expense to be reported in each quarter, showing how the estimate change is absorbed *without restating* earlier quarters.

**Solution.**

*Principle.* Interim tax = (estimated annual effective rate × **year-to-date** pre-tax profit) − tax already recognised in prior interim periods of the year. A change in the estimated rate is a **change in estimate** (Rule 6): apply it to the *year-to-date* figure in the quarter of change and **prospectively** — earlier quarters are **not** restated.

*Quarters 1 and 2 — rate 25%:*

| Quarter | YTD pre-tax (Rs L) | YTD tax at rate (Rs L) | Less prior tax (Rs L) | Tax this quarter (Rs L) |
|---------|--------------------|------------------------|-----------------------|-------------------------|
| Q1 | 100 | 100 × 25% = 25 | 0 | **25** |
| Q2 | 200 | 200 × 25% = 50 | 25 | **25** |

*Quarter 3 — rate revised to 30%, applied to YTD:*

| Quarter | YTD pre-tax (Rs L) | YTD tax at NEW rate (Rs L) | Less prior tax (Rs L) | Tax this quarter (Rs L) |
|---------|--------------------|----------------------------|-----------------------|-------------------------|
| Q3 | 500 | 500 × 30% = 150 | 25 + 25 = 50 | **100** |

Notice Q3's tax of Rs 100 lakh contains (i) 30% on Q3's own Rs 300 lakh = Rs 90 lakh, **plus** (ii) the catch-up of the rate change on the first two quarters: (30% − 25%) × Rs 200 lakh = Rs 10 lakh. The Rs 10 lakh "true-up" lands in **Q3**, not by reopening Q1 and Q2. ✔

*Quarter 4 — rate stays 30%:*

| Quarter | YTD pre-tax (Rs L) | YTD tax at rate (Rs L) | Less prior tax (Rs L) | Tax this quarter (Rs L) |
|---------|--------------------|------------------------|-----------------------|-------------------------|
| Q4 | 600 | 600 × 30% = 180 | 50 + 100 = 150 | **30** |

**Reconciliation.** Sum of quarterly tax = 25 + 25 + 100 + 30 = **Rs 180 lakh**, which equals 30% × Rs 600 lakh, the correct *annual* tax on the final best estimate. ✔ The annual result is right; the estimate change was absorbed in Q3 without restating any earlier interim period.

**Required disclosure:** the *nature and amount* of the change in estimate (revised effective rate 25% → 30%, effect Rs 10 lakh catch-up plus higher Q3–Q4 charge) must be disclosed in the Q3 notes (disclosure item 4).

---

### Example 4 (Short, conceptual) — What must a condensed Q2 report contain?

**Facts.** A listed company (annual accounts are consolidated, and it reports segments under AS 17) wants to publish the *minimum* half-yearly (H1) report.

**Answer.** It must include: (a) condensed **consolidated** balance sheet at 30 Sep vs 31 Mar; (b) condensed P&L for the quarter Jul–Sep *and* the half-year Apr–Sep, each vs the prior year's corresponding periods, with **basic and diluted EPS on the face**; (c) condensed cash flow for the half-year Apr–Sep vs prior-year Apr–Sep; (d) **selected explanatory notes** including a policies statement, seasonality comment, unusual items, changes in estimates, share/debt movements, dividends, **segment revenue and result**, subsequent events, changes in enterprise composition, and material contingent-liability changes. Each condensed statement must retain **every heading/sub-heading** present in the last annual statements.

---

## 6. Presentation & Disclosure Formats

### 6.1 Illustrative face of a Condensed Statement of Profit and Loss (quarterly)

*(Format follows Schedule III headings, condensed; figures illustrative.)*

| Particulars | 3 months ended 31 Dec 2025 | 9 months ended 31 Dec 2025 | 3 months ended 31 Dec 2024 | 9 months ended 31 Dec 2024 | Year ended 31 Mar 2025 (audited) |
|-------------|---------------------------|----------------------------|----------------------------|----------------------------|----------------------------------|
| Revenue from operations | | | | | |
| Other income | | | | | |
| **Total income** | | | | | |
| Cost of materials consumed | | | | | |
| Changes in inventories | | | | | |
| Employee benefits expense | | | | | |
| Finance costs | | | | | |
| Depreciation and amortisation | | | | | |
| Other expenses | | | | | |
| **Total expenses** | | | | | |
| **Profit before tax** | | | | | |
| Tax expense (at est. annual effective rate) | | | | | |
| **Profit for the period** | | | | | |
| **Basic EPS (Rs)** | | | | | |
| **Diluted EPS (Rs)** | | | | | |

*The current-quarter and year-to-date columns are the AS 25 requirement; the audited full-year column is commonly shown by convention/SEBI practice.*

### 6.2 Illustrative Condensed Balance Sheet columns

| Particulars | As at 31 Dec 2025 (unaudited) | As at 31 Mar 2025 (audited) |
|-------------|-------------------------------|------------------------------|
| EQUITY AND LIABILITIES … (each Schedule III heading, condensed) | | |
| ASSETS … (each Schedule III heading, condensed) | | |

### 6.3 The selected-notes checklist (present all that apply)

Policies statement/change · Seasonality comment · Unusual items · Changes in estimates · Debt & equity issuances/buy-backs/repayments · Dividends (equity & other, per share) · Segment revenue & result (if AS 17 applies) · Material subsequent events · Changes in composition of the enterprise · Material changes in contingent liabilities · Compliance statement (if claiming full AS compliance).

---

## 7. Connections

AS 25 is a *host* standard — it does not replace measurement rules, it borrows them. Knowing which standard it plugs into is heavily tested.

| Connected standard | How AS 25 uses it |
|--------------------|-------------------|
| **AS 1 (Disclosure of Accounting Policies)** | Defines a "complete set" of statements; the policies-consistency requirement flows from here |
| **AS 5 (Net Profit/Loss, Prior Period, Changes in Estimates)** | The "change in estimate is prospective, no restatement" rule for interim periods is AS 5's principle applied within a year |
| **AS 2 (Inventories)** | Interim stock at lower of cost and NRV; estimates/gross-margin methods permitted for interim cost |
| **AS 20 (EPS)** | Basic & diluted EPS on the face of the interim P&L |
| **AS 17 (Segment Reporting)** | Segment revenue & result required in interim notes if AS 17 applies annually |
| **AS 22 (Taxes on Income)** | Interim tax uses the estimated **weighted-average annual effective tax rate** on YTD profit |
| **AS 26 (Intangibles)** | Advertising/start-up/training expensed, never deferred — at interim date exactly as at year-end |
| **AS 28 (Impairment)** | Impairment tested at interim date on conditions then existing; note the special caution on reversals |
| **AS 29 (Provisions, Contingent Liabilities)** | The "present obligation + reliable estimate" gate for accruing lumpy costs (bonus, rebates) at interim date |
| **AS 4 (Events after Balance Sheet Date)** | "Material subsequent events" disclosure in interim notes mirrors this logic |
| **SEBI LODR Regulations** | The *external* trigger that actually *requires* quarterly reporting — AS 25 supplies the *how* |

**Big-picture placement:** AS 25 sits at the intersection of *timeliness* (a regulatory demand) and *faithful representation* (an accounting demand). Its entire personality is the refusal to trade the second for the first — you get the news faster, but you still get the truth.

---

## 8. Traps & Examiner Tricks

1. **"AS 25 requires companies to prepare quarterly results." — FALSE.** AS 25 does *not* mandate *who*, *how often*, or *how soon*. That is a statute/regulator's job (SEBI). AS 25 only governs *content and measurement* once you *do* prepare an interim report. This is the single most-tested scope point.

2. **Smoothing seasonal revenue.** The tempting "report equal revenue each quarter for comparability" is *prohibited*. Seasonal/cyclical revenue is recognised *when earned*; disclose seasonality instead of hiding it.

3. **Pre-spreading a future lumpy cost.** A planned Q3 advertising blitz or a December overhaul must **not** be accrued in Q1/Q2. Test: *would it be a liability at year-end before being incurred?* No → zero until incurred. Students wrongly "provide 1/4 each quarter."

4. **Deferring a cost already paid.** Conversely, a one-time cost incurred in Q1 that is *not* a prepaid asset at year-end (e.g., a training program) must be **fully charged in Q1**, not spread forward for smoothness.

5. **Restating an earlier quarter for an estimate change.** WRONG. Changes in estimate hit the *later* interim period's year-to-date figure **prospectively**; earlier quarters are never reopened (Example 3). Disclose nature and amount.

6. **Wrong comparative periods.** The classic slip: putting a *year-to-date* comparative on the balance sheet, or forgetting the *two* P&L columns (current quarter *and* YTD). Balance sheet → vs last **year-end**; P&L → current period *and* YTD, each vs prior-year corresponding periods; cash flow → YTD only.

7. **Forgetting EPS on the face.** Basic *and* diluted EPS must appear on the face of the interim P&L, not just in notes.

8. **"Condensed" ≠ "drop headings."** A condensed statement must still carry **every heading and sub-heading** from the last annual statements; you compress *detail*, you don't delete a whole line item.

9. **Materiality judged against the year.** Interim materiality is judged against the **interim period's** data, not the annual figures — otherwise big quarterly distortions vanish inside the annual total.

10. **Tax at a flat statutory rate.** Interim tax is *not* simply "current-quarter profit × statutory rate." It is the **estimated weighted-average annual effective rate** (reflecting expected deductions, slabs, credits) applied to **year-to-date** profit, less tax already booked.

11. **Impairment/inventory write-down reversals.** Be cautious: AS 25's guidance flags that some interim losses (e.g., certain write-downs) require careful treatment; do not assume automatic reversal in a later quarter — apply the underlying standard (AS 2/AS 28). Confirm the specific reversal wording in current ICAI material.

12. **Standalone vs consolidated.** If annual accounts are consolidated, the interim report should be on a **consolidated** basis — candidates often default to standalone.

---

## 9. First-Principles Recap

Rebuild the whole standard from one need and three consequences:

- **The need:** annual data is *stale*; capital markets need *timely* mid-year information. So regulators force quarterly reporting. (Timeliness.)
- **Consequence 1 — Content:** reproducing the full annual report four times a year would destroy timeliness and cost. So AS 25 asks only for a **condensed** balance sheet, P&L, and cash flow **plus selected notes**, read *alongside* the last annual report. Keep every heading; compress the detail; put EPS on the face.
- **Consequence 2 — Measurement philosophy:** if quarters could be *smoothed*, users would be back to fiction and managers would gain an earnings-management lever. So AS 25 chooses the **discrete view** — each quarter tells the truth about itself — *but measures year-to-date* so the reporting frequency never changes the annual result. Seasonal revenue is recognised when earned; a lumpy cost is anticipated or deferred **only if** you could do so at **year-end**; estimate changes are absorbed **prospectively** in later quarters.
- **Consequence 3 — Reliability trade-off:** three-month deadlines force **greater use of estimates**; that is accepted, provided the numbers stay reliable and relevant, and provided the notes explain *seasonality, unusual items, estimate changes, and what's new*.

If you can derive "don't smooth, but measure year-to-date, and anticipate/defer a cost only if you could at year-end" from the single idea *timely information must still be honest information*, you own AS 25.

```mermaid
flowchart LR
    A["Need -- timely honest mid-year data"] --> B["Content -- condensed statements plus selected notes"]
    A --> C["Measurement -- discrete view but year-to-date"]
    A --> D["Reliability -- more estimates accepted"]
    C --> E["Seasonal revenue when earned"]
    C --> F["Lumpy cost -- defer or accrue only if OK at year-end"]
    C --> G["Estimate change -- prospective no restatement"]
```
*Figure 4 — AS 25 on one page: one need, three consequences.*

---

## 10. Quick-Revision Sheet

**Scope.** AS 25 governs *content + recognition/measurement* of interim reports. It does **NOT** mandate who prepares, how often, or how soon — that's the regulator (SEBI). If you claim AS compliance, comply with *all* standards.

**Interim period** = period shorter than a full year (usually a quarter/half-year).

**Minimum components (condensed):** (a) Balance Sheet (b) Statement of P&L (c) Cash Flow Statement (d) Selected explanatory notes. Keep every annual heading/sub-heading; add lines if omission misleads. **Basic & diluted EPS on the face.** Consolidated if annual is consolidated.

**Comparatives:**
- Balance Sheet → current interim date **vs last year-end**.
- P&L → **current period AND year-to-date**, each vs prior-year corresponding periods.
- Cash Flow → **year-to-date** vs prior-year YTD.

**Recognition & measurement:**
- Same accounting policies as annual.
- **Year-to-date** measurement so frequency doesn't change annual result (discrete view).
- **Seasonal/cyclical revenue → recognise when earned; never anticipate or defer.**
- **Uneven cost → anticipate/defer only if you could at YEAR-END** (asset/prepaid or AS 29 liability); else expense when incurred.
- Depreciation only on assets owned in the period.
- **Interim tax = estimated weighted-average ANNUAL effective rate × YTD pre-tax profit − prior-period tax.**
- **Change in estimate → prospective in the later interim period; NEVER restate an earlier quarter.**
- Greater use of estimates permitted (must stay reliable & relevant).
- **Materiality judged against interim data, not annual.**

**Selected notes:** policies statement/change · seasonality · unusual items · estimate changes · share & debt movements · dividends · segment revenue & result (if AS 17) · subsequent events · changes in composition · material contingent-liability changes.

**Top traps:** don't smooth seasonal revenue · don't pre-spread a future lumpy cost · don't defer a paid one-off · don't restate earlier quarters for estimate changes · balance sheet compares to year-end (not YTD) · EPS on the face · "condensed" keeps all headings.

**The one sentence:** *Treat each interim period as a standalone period measured year-to-date — recognise costs and revenues by the same rules as at year-end — so the reader gets the news faster without getting a smoothed-over fiction.*
