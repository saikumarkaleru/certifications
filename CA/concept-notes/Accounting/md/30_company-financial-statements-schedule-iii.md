<!-- v2-deep -->

# Chapter 30 — Financial Statements of Companies (Schedule III)

## 1. The Problem

Imagine you are an investor deciding where to park ₹10 lakh. You pull the annual accounts of three companies. The first lists "Money owed to us" in one place. The second calls the same thing "Sundry Debtors" and buries it between fixed assets and cash. The third splits it into "Amounts due within a year" and "Long-term dues" but puts long-term dues *above* the buildings. Now try to answer one simple question across all three: *How much cash is likely to come in within the next 12 months?* You cannot. Not because the information is hidden, but because each company has arranged the same facts in a different order, under different names, with different groupings.

This is the core problem. A sole proprietor or a partnership can arrange its Balance Sheet however it likes — the only readers are the owners and maybe a banker who will ask questions directly. But a **company** is different. Its shareholders may number in the thousands, most of whom will never meet the directors. Its creditors, lenders, tax authorities, regulators, and potential acquirers all read the same document from a distance, with no ability to phone up and ask "what did you mean by this line?" The financial statements are the *only* channel of communication, and that channel must carry the same meaning to every reader.

If every company invented its own layout, three things break:

1. **Comparability dies.** You cannot compare Company A with Company B, nor Company A this year with Company A last year, if the shape of the statement keeps shifting.
2. **Completeness cannot be checked.** A reader has no way of knowing whether a company *omitted* something (say, contingent liabilities) if there is no standard checklist of what must appear.
3. **Manipulation becomes easy.** A company wanting to look liquid could quietly reclassify a long-term loan as "other liabilities" and shuffle it out of sight.

So the law steps in and says: *there will be one prescribed skeleton, and every company will hang its numbers on that skeleton.* That skeleton is **Schedule III to the Companies Act, 2013**. This chapter is about understanding *why* the skeleton has the exact bones it has, and then how to actually take a raw trial balance and drape a real company's figures over it — correctly, completely, and in a way that would pass an exam and an audit.

A subtler layer of the same problem, which the exam probes constantly: standardising the *shape* of the statement is not enough. Two further leaks must be plugged. First, **once profit is measured, who is allowed to take money out of the company, and how much?** Managers might vote themselves lavish pay; owners might strip out cash as dividend and leave creditors exposed. Second, **the "profit" on the face of the P&L is an accounting number, but the law needs a differently-defined profit for those withdrawal decisions** — because accounting profit can be inflated by capital gains or distorted by items the law does not want managers rewarded on. So Schedule III presentation is only Act One; Sections 197, 198 and 123 (remuneration and dividend) are Act Two, and the exam tests the join between them.

## 2. The Core Idea (Analogy)

Think of Schedule III as a **standardised shipping manifest**.

When cargo crosses international borders, every container is accompanied by a manifest with fixed columns in a fixed order: contents, weight, origin, destination, hazard class. A customs officer in Mumbai, Rotterdam, and Singapore can each read the *same form* and instantly find the *same fact* in the *same box*. Nobody has to learn a new form at each port. The manifest does not tell the shipper *what* to ship — that is the business's choice — it only tells them *how to describe* what they shipped so that any reader anywhere can decode it.

Schedule III is exactly this manifest for a company's financial position. It does not tell the company how much to earn or what assets to buy. It tells the company: *whatever your facts are, describe them in this order, under these headings, with this split between "will settle within a year" and "will settle later."* The genius of the manifest is the **current vs non-current split** — it is the customs officer's single most important sorting rule, because it answers the question every reader cares about most: *what is coming and going in the near term versus locked up for the long haul?*

Extend the analogy to the two governance provisions. The **manifest** describes the cargo; but a port also enforces **how much of the cargo the crew may keep for themselves (wages) and how much the owner may unload for personal sale (dividend) before the ship is safe to sail on**. Section 197 is the wage cap on the crew; Section 123 is the rule that the owner cannot strip the hold below a safe ballast (reserves and depreciation must stay aboard). The manifest and these two rules are separate mechanisms serving the same distant-trust problem: a reader must be able to see both *what is there* and *that it was not quietly siphoned off*.

Keep this analogy in your head for the whole chapter. Every time a rule feels arbitrary, ask: *what would a customs officer at a distant port need, in a fixed box, to trust this cargo without a phone call?*

## 3. Why It's Built This Way

Schedule III did not fall from the sky. Its structure is the answer to a sequence of "what does the distant reader need?" questions.

**Why a vertical format and not the old horizontal T-account?** The older Companies Act, 1956 permitted a horizontal Balance Sheet (liabilities on the left, assets on the right). Schedule III mandates the **vertical form** only. A vertical statement reads top-to-bottom like a narrative — sources of funds first (what the company owes to owners and outsiders), then application of funds (what it did with that money). It also allows a clean single column of previous-year figures right alongside, which the horizontal form handles clumsily.

**Why the "current vs non-current" classification instead of "fixed vs floating"?** The old law sorted assets into "fixed" and "current" using a vague notion of permanence. Schedule III replaces this with a **time-based test aligned to the operating cycle**. The distant reader's real question is about *timing of cash*: which assets will turn into cash within the next operating cycle, and which liabilities must be paid in that window? Sorting by time directly answers the solvency and liquidity question, which permanence never did cleanly.

**Why must the Notes carry so much?** Schedule III keeps the face of the Balance Sheet and P&L short — a handful of line items — and pushes all the detail into **Notes to Accounts**. This is deliberate. The face gives the customs officer the headline; the notes are the detailed packing list inside. A reader who only wants the big picture reads the face; a reader who wants to verify reads the notes. This separation of *summary* from *detail* is the second structural genius after the current/non-current split.

**Why does an Accounting Standard override Schedule III?** Schedule III itself contains a "General Instruction" stating that if a disclosure requirement of the **Companies Act or an Accounting Standard** is different from Schedule III, the Act/AS prevails, and Schedule III's requirements are *in addition*. The logic: Schedule III is a presentation template, but the *substance* of recognition and measurement lives in the Accounting Standards. Form must yield to substance. This is why, for example, AS 3 (Cash Flow) and AS 18 (Related Party) disclosures sit alongside Schedule III without conflict.

**Why three Divisions of Schedule III?** The same presentation logic must serve companies on different accounting regimes, so Schedule III is split into **Division I** (companies following notified **Accounting Standards** — the CA Intermediate syllabus), **Division II** (companies following **Ind AS**), and **Division III** (**NBFCs following Ind AS**). They share the current/non-current DNA but differ in headings — e.g. Division II replaces "Reserves and Surplus" with "Other Equity" and shows a separate **Statement of Changes in Equity**, while Division III orders the Balance Sheet by **liquidity** rather than current/non-current because a finance company's whole business *is* current/non-current assets. Knowing that these Divisions exist prevents you from importing an Ind AS heading (like "Other Equity") into a Division I answer.

**Why a "true and fair view" clause on top of a rigid format?** A prescribed format could, in a freak case, still mislead. So Section 129 layers a **substance-over-form override**: the statements must give a true and fair view, and where the prescribed format would defeat that, additional disclosure is required. The format is the floor of disclosure, never the ceiling. This is the philosophical anchor for every "disclose in notes" rule in the chapter.

**Why define profit twice — once for accounting and once for withdrawals (Section 198)?** Because the two profits answer different questions. Accounting profit answers "how did the business perform?" It legitimately includes capital gains, revaluation effects, and one-off items. But the question "how much may managers be paid?" and "how much may be distributed?" needs a **sustainable, operating, distributable** profit — otherwise a company could sell a building at a huge capital gain and reward managers on a one-time windfall, or pay dividends out of paper revaluation surpluses that never generated cash. Section 198 therefore *strips out capital-nature profits and re-adds items* so the percentage caps bite on a defensible base. The double definition is not bureaucratic duplication; it is the law refusing to let a distributable decision ride on a non-distributable number.

With the "why" established, we now install the actual bones.

## 4. Full Technical Content

### 4.1 What Schedule III covers and what "financial statements" means

Under **Section 2(40) of the Companies Act, 2013**, "financial statements" include:

- a **Balance Sheet** as at the end of the financial year;
- a **Statement of Profit and Loss** for the financial year;
- a **Cash Flow Statement** for the financial year (not required for a **One Person Company, small company, dormant company**, or a private company that qualifies as a startup);
- a **Statement of Changes in Equity**, if applicable (this is an Ind AS concept; under AS-based Schedule III Division I it is not a separate statement); and
- any explanatory notes.

**Section 129** requires financial statements to give a **true and fair view**, comply with the notified Accounting Standards, and be in the **form provided in Schedule III**. For CA Intermediate (AS regime, non-Ind-AS companies) the relevant part is **Division I of Schedule III**.

**Section 128** requires books of account to be kept on an accrual basis and the double-entry system. **Section 130/131** deal with re-opening and voluntary revision — out of scope here but worth knowing they exist.

**Finer distinctions the exam probes here:**

- A **small company** [Sec 2(85)] is a private company below both a paid-up capital and a turnover threshold (thresholds have been revised more than once — **verify current limits against the latest ICAI material / AY**). The exam point is *why* it is exempt from the Cash Flow Statement: its readership is small and close, so the distant-reader rationale weakens, and the compliance cost would outweigh the benefit. A **holding, subsidiary, Section 8 (charitable), or company governed by a special Act is never a small company** regardless of size.
- **"Financial year"** under Section 2(41) must end on **31 March** for every company (with narrow exceptions for holding/subsidiaries of foreign entities, allowed by the Tribunal). This is why exam Balance Sheets are dated 31 March.
- A **Statement of Changes in Equity (SOCE)** does **not** exist as a separate statement under Division I. If an exam answer in the AS regime shows a SOCE, it is wrong; the equivalent movement is captured inside the **Reserves and Surplus** note. Reserve this concept for Ind AS (Division II).

### 4.2 The operating cycle — the master key

Everything in the Balance Sheet classification hinges on one definition.

> **Operating cycle** = the time between the acquisition of assets for processing and their realisation into cash or cash equivalents. Where the cycle cannot be identified, it is **assumed to be 12 months**.

An asset is **current** if it satisfies *any one* of these:

1. it is expected to be realised in, or is intended for sale or consumption in, the company's **normal operating cycle**; or
2. it is held **primarily for the purpose of trading**; or
3. it is expected to be realised **within 12 months** after the reporting date; or
4. it is **cash or cash equivalent** (unless restricted from being exchanged or used to settle a liability for at least 12 months after the reporting date).

**All other assets are non-current.**

A liability is **current** if *any one* holds:

1. it is expected to be settled in the **normal operating cycle**; or
2. it is held **primarily for trading**; or
3. it is due to be settled **within 12 months** after the reporting date; or
4. the company **does not have an unconditional right to defer settlement** for at least 12 months after the reporting date.

**All other liabilities are non-current.**

```mermaid
flowchart TD
    A["Item to classify"] --> B["Realised or settled within operating cycle?"]
    B -->|"Yes"| C["CURRENT"]
    B -->|"No"| D["Held primarily for trading?"]
    D -->|"Yes"| C
    D -->|"No"| E["Due or expected within 12 months?"]
    E -->|"Yes"| C
    E -->|"No"| F["Cash equivalent or no right to defer 12 months?"]
    F -->|"Yes"| C
    F -->|"No"| G["NON-CURRENT"]
```
*Figure 1 — The single decision tree that classifies every asset and liability; satisfying any one branch makes the item current.*

**Why the operating-cycle branch matters even when it seems redundant.** For a business with a long production cycle — a distillery ageing whisky for four years, a shipbuilder, a real-estate developer — inventory that will take three years to sell is **still a current asset**, because it is realised *within the normal operating cycle* even though that cycle exceeds 12 months. This is the classic examiner tweak: "raw material expected to be consumed after 18 months, but the company's operating cycle is 24 months — classify it." Answer: **current asset**, because branch 1 (operating cycle) is satisfied; you never even reach the 12-month branch. The 12-month test is only a *fallback* for items outside the operating cycle. Reverse the trap: a debt due in 15 months for a company with a 3-month operating cycle is **non-current** — none of the four branches is met.

**Symmetry point for liabilities.** Trade payables arising in the operating cycle are **current even if not due within 12 months** (branch 1). But a **refinanced** long-term loan is non-current only if the company has an *unconditional right* to defer at the reporting date; a refinancing agreement signed *after* the year end does not help — the right must exist *on* the Balance Sheet date. A loan repayable on demand (breach of covenant giving the lender an immediate call) is **current**, because the borrower has no unconditional right to defer.

### 4.3 Structure of the Balance Sheet (Division I)

The Balance Sheet has two grand totals that must be equal: **Total Equity and Liabilities = Total Assets**. Its skeleton, in mandatory order, is below. The number in brackets is the **Note number** where detail lives.

**I. EQUITY AND LIABILITIES**

1. **Shareholders' Funds**
   - (a) Share Capital
   - (b) Reserves and Surplus
   - (c) Money received against share warrants
2. **Share Application Money Pending Allotment**
3. **Non-Current Liabilities**
   - (a) Long-term Borrowings
   - (b) Deferred Tax Liabilities (Net)
   - (c) Other Long-term Liabilities
   - (d) Long-term Provisions
4. **Current Liabilities**
   - (a) Short-term Borrowings
   - (b) Trade Payables *(with sub-split: total dues of micro & small enterprises; and others)*
   - (c) Other Current Liabilities
   - (d) Short-term Provisions

**II. ASSETS**

1. **Non-Current Assets**
   - (a) Property, Plant and Equipment and Intangible Assets
     - (i) Property, Plant and Equipment (Tangible Assets)
     - (ii) Intangible Assets
     - (iii) Capital Work-in-Progress
     - (iv) Intangible Assets under Development
   - (b) Non-Current Investments
   - (c) Deferred Tax Assets (Net)
   - (d) Long-term Loans and Advances
   - (e) Other Non-Current Assets
2. **Current Assets**
   - (a) Current Investments
   - (b) Inventories
   - (c) Trade Receivables
   - (d) Cash and Cash Equivalents
   - (e) Short-term Loans and Advances
   - (f) Other Current Assets

```mermaid
flowchart TD
    BS["Balance Sheet"] --> EL["I. Equity and Liabilities"]
    BS --> AS["II. Assets"]
    EL --> SF["1. Shareholders Funds"]
    EL --> SA["2. Share Application Money Pending Allotment"]
    EL --> NCL["3. Non-Current Liabilities"]
    EL --> CL["4. Current Liabilities"]
    AS --> NCA["1. Non-Current Assets"]
    AS --> CA["2. Current Assets"]
```
*Figure 2 — The two grand divisions and their four/two major heads; the two grand totals must reconcile.*

**Two positions that sit "between" equity and liabilities and are heavily tested:**

- **Share Application Money Pending Allotment** gets its *own line* between Shareholders' Funds and Non-Current Liabilities. Why a separate line and not capital? Because at the reporting date the shares are *not yet allotted* — the money is neither fully "owners' capital" nor an ordinary liability. The nuance: money **that can be allotted** (company has enough authorised capital, the issue is not going to be refunded) sits here as quasi-equity; any portion that **must be refunded** (over-subscription, or authorised capital insufficient) is a **current liability**, not this line. Examiners split one figure across the two.
- **Money received against share warrants** sits inside Shareholders' Funds as item (c). A warrant holder has paid for the *right* to subscribe later; the money is non-refundable consideration towards future equity, so it is grouped with owners' funds, not liabilities.

### 4.4 Contents of key heads (the detail you must know)

**Share Capital note** must disclose, for each class:
- Number and amount of shares **authorised**, **issued**, **subscribed and fully paid**, and **subscribed but not fully paid**;
- par value per share;
- a **reconciliation** of the number of shares outstanding at the beginning and end of the year;
- rights, preferences and restrictions attaching to each class;
- shares held by each **shareholder holding more than 5%**;
- shares reserved for issue under options;
- for the last **5 years**: shares allotted for consideration other than cash, bonus shares, and shares bought back;
- **Calls unpaid** (showing separately amounts from directors and officers) shown as a deduction; **forfeited shares** amount shown separately.

**Reserves and Surplus** — classified as: Capital Reserve; Capital Redemption Reserve; Securities Premium; Debenture Redemption Reserve; Revaluation Reserve; Share Options Outstanding; Other Reserves (specify nature); and **Surplus** i.e. the balance in the Statement of Profit and Loss (showing allocations and appropriations such as dividend, transfer to reserves). A **debit balance of Surplus** (accumulated losses) is shown as a **negative figure under this head**, even if it makes Reserves and Surplus negative.

*Distinguish the three "capital" reserves the exam confuses:* **Capital Reserve** arises from capital profits (e.g. profit on reissue of forfeited shares, profit prior to incorporation); **Capital Redemption Reserve (CRR)** is created by law when preference shares are redeemed or shares are bought back out of profits (equal to the nominal value redeemed); **Securities Premium** is the excess over par received on a share/debenture issue. Only CRR and Securities Premium have *statutorily restricted* uses; Capital Reserve is generally not available for dividend either. **Revaluation Reserve** can never be used for dividend and is not a free reserve.

**Long-term Borrowings** — bonds/debentures, term loans (from banks / others), deferred payment liabilities, deposits, loans from related parties, long-term maturities of finance lease obligations. Must state **secured vs unsecured**, nature of security, terms of redemption/repayment, and **period and amount of any continuing default** in repayment of principal or interest as on the Balance Sheet date.

**Trade Payables / Trade Receivables** — a payable/receivable is "trade" only if it arises from the **purchase/sale of goods or services in the normal course of business**. Amounts due on any other account (e.g. sale of a fixed asset) are **not** trade and go under "Other" heads.

**Trade Receivables** must further disclose: aggregate **outstanding for more than six months** from the date they became due (separately), and be sub-classified as **secured/considered good**, **unsecured/considered good**, and **doubtful**, with the allowance for bad and doubtful debts shown. Receivables from directors/related parties disclosed separately.

**Cash and Cash Equivalents** — balances with banks; cheques/drafts on hand; cash on hand; others. Earmarked balances (e.g. unpaid dividend), balances held as **margin money or security** against borrowings, and **bank deposits with more than 12 months maturity** must each be disclosed separately.

**A critical current-vs-non-current carve-out:** the **current maturities of long-term debt** (the portion of a term loan repayable within 12 months) are shown under **Other Current Liabilities**, NOT under Short-term Borrowings and NOT under Long-term Borrowings. This trips up most students.

**Further finer placements the examiner tests one item at a time:**

- **Deferred Tax Liability / Asset (net)** appears **only under non-current** — there is no "current deferred tax." DTL and DTA of the *same* entity are shown **net**, and you disclose the net figure on the appropriate side. A company shows *either* a net DTA *or* a net DTL, never both.
- **Long-term Provisions** (e.g. provision for gratuity, warranty beyond 12 months) vs **Short-term Provisions** (provision for tax, proposed portion of employee benefits due within a year). The *same* liability (gratuity) can split across both heads by timing.
- **Interest accrued and due** on borrowings → Other Current Liabilities (it is payable now); **interest accrued but not due** → also Other Current Liabilities. Both leave the borrowing line and sit as current — a common tweak.
- **Unpaid dividend, unpaid matured deposits/debentures, application money refundable** → Other Current Liabilities.
- **Provision for doubtful debts** is *not* a Balance Sheet liability head — it is netted against Trade Receivables in that note.
- **Capital advances** (advances paid for acquiring fixed assets) are **Long-term Loans and Advances (non-current)**, never Inventories or current — because they will crystallise into a non-current asset.
- **Loose tools, stores and spares, packing material, loose stock** → **Inventories** (current), regardless of how long they last, because they are consumed in operations.

### 4.5 Structure of the Statement of Profit and Loss

The P&L is strictly vertical and arrives at profit through a fixed sequence:

| Line | Item |
|------|------|
| I | Revenue from Operations |
| II | Other Income |
| III | **Total Income (I + II)** |
| IV | Expenses: Cost of materials consumed; Purchases of stock-in-trade; Changes in inventories of finished goods, WIP and stock-in-trade; Employee benefits expense; Finance costs; Depreciation and amortisation expense; Other expenses |
| V | **Total Expenses** |
| VI | **Profit before exceptional and extraordinary items and tax (III − V)** |
| VII | Exceptional items |
| VIII | Profit before extraordinary items and tax (VI − VII) |
| IX | Extraordinary items |
| X | **Profit before tax (VIII − IX)** |
| XI | Tax expense: (1) Current tax (2) Deferred tax |
| XII | **Profit for the period from continuing operations (X − XI)** |
| XIII–XV | Profit/loss from discontinuing operations, its tax, and net |
| XVI | **Profit for the period** |
| XVII | Earnings per equity share: (1) Basic (2) Diluted |

Note the **"Changes in inventories"** line: it is computed as **Opening stock − Closing stock** of finished goods/WIP/stock-in-trade. A positive figure (stock fell) is an expense; a negative figure (stock rose) reduces expense. There is **no separate "opening stock" and "closing stock"** the way a proprietor's Trading Account shows them — Schedule III nets them into one line.

**Careful sub-distinctions inside expenses (frequently mis-slotted):**

- **Cost of materials consumed** applies to a *manufacturer* = Opening raw material + Purchases of raw material − Closing raw material. **Purchases of stock-in-trade** applies to a *trader* who buys finished goods for resale. A pure trader has *no* "materials consumed" line; a pure manufacturer's resale purchases are nil. Mixed businesses show both.
- **Changes in inventories** covers only **finished goods, WIP and stock-in-trade** — *not raw materials* (raw-material movement is already inside "materials consumed"). Putting raw-material stock movement into "Changes in inventories" double-counts. This is a precision trap.
- **Finance costs** = interest expense, other borrowing costs, and net loss on foreign-currency borrowings to the extent treated as interest. Note: **interest on income tax** and **bank charges** are *not* finance costs — bank charges go to Other Expenses.
- **Exceptional items** are ordinary-activity items of unusual size/incidence (e.g. a large one-off write-down); **extraordinary items** are outside ordinary activities (now a shrinking category). They are shown *separately* on the face, not buried in Other Expenses, precisely so the distant reader can strip them out to judge sustainable profit — the same logic that drives Section 198.

**Revenue from Operations** for a company **other than a finance company** = sale of products + sale of services + other operating revenues, **less** excise duty (historically). Broken up in the notes. For a **finance company**, revenue from operations = interest + other financial-services income — its "operations" *are* financial, so the face heading differs.

**Additional information required in notes to P&L** includes: value of imports on CIF basis (raw materials, components, capital goods); expenditure in foreign currency; earnings in foreign exchange; **auditor's remuneration** (as auditor, for taxation, for company law matters, for other services, reimbursements); and consumption of imported vs indigenous raw materials/stores with percentages.

### 4.6 Managerial Remuneration (Section 197) and Divisible Profits

Once profit is computed, two governance questions arise, and both are examinable:

**(a) How much can be paid to managers/directors?**

**Section 197** caps total managerial remuneration payable by a **public company** to its directors (including MD, WTD and manager) in any financial year at **11% of the net profits** of that year, computed under **Section 198**. Within that ceiling:

| Situation | Maximum remuneration |
|-----------|----------------------|
| Overall (all directors together) | 11% of net profits |
| One managing/whole-time director or manager | 5% of net profits |
| More than one such director | 10% of net profits (together) |
| Directors who are neither MD nor WTD — if there is a MD/WTD | 1% of net profits |
| Directors who are neither MD nor WTD — if there is no MD/WTD | 3% of net profits |

If profits are **inadequate or there is a loss**, remuneration may be paid per the limits in **Schedule V** (based on effective capital) — otherwise it requires shareholder approval. (Post the 2018 amendment, remuneration exceeding these limits requires only a **special resolution** of shareholders, not Central Government approval.)

*Scope points the exam hides:* the 11%/5% caps apply to **public companies**; a **private company is not bound by Section 197 limits** and may pay any remuneration authorised by its articles. **Sitting fees** paid to directors for attending meetings are **outside** the 11% ceiling (Section 197(5)), subject to a per-meeting cap prescribed by rules. The **11%** is a *ceiling that itself can be crossed by special resolution*; the *individual* 5%/10%/1%/3% figures are the sub-limits within (or, when crossed, alongside) it.

**Net profit under Section 198** is a specially computed figure — it is *not* simply the P&L profit. The mechanics (know the direction of each adjustment):

- **Start** with profit as per P&L, then
- **Add back** (credit) items wrongly credited or to be excluded, and expenses allowed to be added back;
- **Do NOT credit** (i.e. exclude from income): profit on sale of undertaking/investments (capital nature), premium on shares/debentures, profit on forfeiture of shares, profit of a capital nature including profit on sale of fixed assets *above original cost*;
- **Deduct** (allow as expenses): usual working charges, directors' remuneration, bad debts written off, depreciation as per Section 123, etc.;
- **Do NOT deduct**: income tax, voluntary compensation/damages, capital losses, and — importantly — **the managerial remuneration itself is not deducted before applying the percentage** (the percentage is applied on profit *before* charging such remuneration).

A frequently-tested subtlety: **profit on sale of a fixed asset** is included in Section 198 profit only to the extent of the **write-back of depreciation / up to original cost**; any excess over original cost (a genuine capital profit) is **excluded**.

**A compact Section 198 template (memorise the direction of each line):**

| | ₹ |
|---|---|
| Net profit as per Statement of Profit and Loss | X |
| **Add back** if already debited: managerial remuneration; provision for tax (not allowed as deduction); voluntary compensation; capital losses; loss on sale of undertaking; scientific research capital expenditure; depreciation in excess of Schedule II | + |
| **Less** if already credited but to be excluded: capital profits; profit on sale of fixed assets **above original cost**; premium on shares/debentures; profit on forfeiture; profit on sale of undertaking/investments (capital) | − |
| **Add** if not yet credited but includible; **Less** allowable items not yet charged (e.g. Schedule II depreciation, bad debts) | ± |
| **= Net profit u/s 198** | **XX** |
| Apply 11% / 5% etc. on XX | |

The single most common error is deducting the managerial remuneration *before* computing the base — the base is *before* remuneration, so if the P&L profit was struck *after* charging remuneration, you must **add it back** first.

**(b) Out of what can dividend be paid? (Divisible profits)**

Dividend can be declared out of:
1. **profits of the current year** (after providing depreciation per Schedule II);
2. **accumulated past profits** transferred to reserves; or
3. **money provided by Central/State Government** for dividend under a guarantee.

Key guardrails under **Section 123**:
- Depreciation must be provided **before** declaring dividend.
- A company **may** (voluntarily — it is no longer mandatory since 2014) transfer a percentage of profits to reserves before dividend.
- Dividend out of **past reserves** in a year of inadequate profit is governed by the **Companies (Declaration and Payment of Dividend) Rules** — the rate cannot exceed the **average of the last three years' rates**, the amount drawn cannot exceed **1/10th (10%) of paid-up capital plus free reserves**, and the balance of reserves after withdrawal must not fall below **15% of paid-up share capital**.
- **Unpaid/unclaimed dividend** must be transferred to a **separate Unpaid Dividend Account within 7 days** after the 30-day payment window; amounts unclaimed for **7 years** go to the **Investor Education and Protection Fund (IEPF)**.

*Two further guardrails often set as MCQ traps:* (i) before declaring dividend out of reserves in a lean year, the **amount so drawn must first be used to set off the current year's loss**; and (ii) a company that has **defaulted** on repayment of deposits, debentures or their interest **cannot declare dividend** until the default is made good. A company can pay **interim dividend** out of the current period's surplus (and, if there is a loss for the elapsed period, the interim rate cannot exceed the average of the last three years' rates).

### 4.7 The workflow: from trial balance to Schedule III statements

```mermaid
flowchart LR
    A["Trial Balance"] --> B["Post adjustments"]
    B --> C["Classify each ledger into a Schedule III head"]
    C --> D["Split current vs non-current"]
    D --> E["Build Notes to Accounts"]
    E --> F["Carry note totals to face of Balance Sheet and P and L"]
    F --> G["Verify grand totals reconcile"]
```
*Figure 3 — The preparation pipeline; every adjustment has a dual effect that must land in two places.*

The discipline that avoids errors: **every adjustment hits two places** (a P&L effect and a Balance Sheet effect, or two Balance Sheet effects). Closing stock appears once as a deduction in "Changes in inventories" (P&L) and once as Inventories (current asset). Outstanding salary appears once as an expense addition and once as "Other Current Liabilities." Miss one leg and the grand totals will not reconcile — which is precisely the built-in check.

**A reusable adjustment map (both legs) for the most common exam adjustments:**

| Adjustment | Leg 1 (P&L) | Leg 2 (Balance Sheet) |
|---|---|---|
| Closing stock | reduces expense (Changes in inventories) | Inventories (CA) |
| Depreciation | Depreciation expense | reduces PPE / adds Accumulated Depreciation |
| Outstanding expense | adds to the expense | Other Current Liabilities |
| Prepaid expense | reduces the expense | Other Current Assets |
| Accrued income | adds to income | Other Current Assets |
| Income received in advance | reduces income | Other Current Liabilities |
| Bad debts written off | Other Expenses | reduces Trade Receivables |
| Increase in provision for doubtful debts | Other Expenses | reduces Trade Receivables (netted) |
| Interest accrued but not paid on loan | Finance cost | Other Current Liabilities |
| Provision for tax | Tax expense (below PBT) | Short-term Provisions |
| Proposed dividend (revised AS 4) | **no P&L / no provision** | **note disclosure only** |

If a candidate simply walks this table adjustment by adjustment, both legs are guaranteed to land and the sheet balances by construction.

## 5. Worked Examples

### Example 1 — Warm-up: classify these items

Classify each into its Schedule III main head and sub-head, and mark current (C) or non-current (NC).

| Item | Head / Sub-head | C/NC |
|------|-----------------|------|
| Securities Premium | Shareholders' Funds → Reserves and Surplus | — |
| Provision for tax | Current Liabilities → Short-term Provisions | C |
| 10% Debentures redeemable after 5 years | Non-Current Liabilities → Long-term Borrowings | NC |
| Term loan instalment due next year | Current Liabilities → Other Current Liabilities (current maturities of long-term debt) | C |
| Loose tools | Current Assets → Inventories | C |
| Goodwill | Non-Current Assets → Intangible Assets | NC |
| Bank overdraft | Current Liabilities → Short-term Borrowings | C |
| Unclaimed dividend | Current Liabilities → Other Current Liabilities | C |
| Calls-in-arrears | Deduction from Subscribed Capital (Share Capital note) | — |
| Prepaid insurance | Current Assets → Other Current Assets | C |
| Advance to supplier for raw material | Current Assets → Short-term Loans and Advances | C |
| Debit balance of Statement of P&L | Reserves and Surplus (shown as negative Surplus) | — |
| Capital advance for new machinery | Non-Current Assets → Long-term Loans and Advances | NC |
| Interest accrued but not due on debentures | Current Liabilities → Other Current Liabilities | C |
| Deferred Tax Liability (net) | Non-Current Liabilities → Deferred Tax Liabilities (Net) | NC |
| Provision for gratuity payable after 12 months | Non-Current Liabilities → Long-term Provisions | NC |
| Public deposits maturing in 8 months | Current Liabilities → Other Current Liabilities (current maturities) | C |
| Share application money to be refunded (over-subscription) | Current Liabilities → Other Current Liabilities | C |

**Teaching point:** the term-loan instalment and the debentures come from the *same* kind of borrowing, yet split across current and non-current. That split is the whole point of Schedule III — it answers "what must I pay within a year?" Note also that a **capital advance** for machinery is *non-current* even though "advance" sounds short-term — it follows the nature of the asset it will become.

### Example 2 — Building a simple Balance Sheet from adjusted balances

Sunrise Ltd (authorised capital 1,00,000 equity shares of ₹10 each) has these balances after all adjustments (₹):

| Debit balances | ₹ | Credit balances | ₹ |
|---|---|---|---|
| Land & Building | 6,00,000 | Equity Share Capital (60,000 shares of ₹10) | 6,00,000 |
| Plant & Machinery | 3,00,000 | General Reserve | 1,50,000 |
| Inventories | 1,80,000 | Surplus (P&L balance) | 1,90,000 |
| Trade Receivables | 1,40,000 | 12% Debentures (redeemable 2032) | 2,00,000 |
| Cash & Bank | 70,000 | Trade Payables | 1,20,000 |
| Short-term Loans & Advances | 40,000 | Provision for Tax | 40,000 |
| | | Outstanding Expenses | 30,000 |
| **Total** | **13,30,000** | **Total** | **13,30,000** |

**Balance Sheet of Sunrise Ltd as at 31 March 2026**

| Particulars | Note | ₹ |
|---|---|---|
| **I. EQUITY AND LIABILITIES** | | |
| 1. Shareholders' Funds | | |
| (a) Share Capital | 1 | 6,00,000 |
| (b) Reserves and Surplus | 2 | 3,40,000 |
| 2. Non-Current Liabilities | | |
| (a) Long-term Borrowings | 3 | 2,00,000 |
| 3. Current Liabilities | | |
| (a) Trade Payables | | 1,20,000 |
| (b) Other Current Liabilities | 4 | 30,000 |
| (c) Short-term Provisions | 5 | 40,000 |
| **Total** | | **13,30,000** |
| **II. ASSETS** | | |
| 1. Non-Current Assets | | |
| (a) Property, Plant and Equipment | 6 | 9,00,000 |
| 2. Current Assets | | |
| (a) Inventories | | 1,80,000 |
| (b) Trade Receivables | | 1,40,000 |
| (c) Cash and Cash Equivalents | | 70,000 |
| (d) Short-term Loans and Advances | | 40,000 |
| **Total** | | **13,30,000** |

Note 2 (Reserves and Surplus) = General Reserve 1,50,000 + Surplus 1,90,000 = **3,40,000**. Note 6 (PPE) = Land & Building 6,00,000 + Plant & Machinery 3,00,000 = **9,00,000**. Both sides total **₹13,30,000** — reconciled.

**Teaching point:** because these opening balances are already *adjusted real accounts only* (no nominal/revenue/expense ledgers left to close), the Balance Sheet total equals the trial balance total. That is a special case. The moment a trial balance still contains nominal accounts (Example 3), those collapse into a single Surplus figure and the Balance Sheet total will differ from the TB total — so never force the Balance Sheet to the TB total; let the classified structure produce its own total and check it balances.

### Example 3 — Exam-hard: full preparation from trial balance with adjustments

**Trial Balance of Meridian Ltd as at 31 March 2026** (Authorised capital: 2,00,000 equity shares of ₹10 each)

| Particulars | Dr (₹) | Cr (₹) |
|---|---|---|
| Equity Share Capital (1,50,000 shares of ₹10, fully paid) | | 15,00,000 |
| 10% Debentures (redeemable 2030) | | 5,00,000 |
| General Reserve | | 2,00,000 |
| Surplus (opening credit balance) | | 1,10,000 |
| Securities Premium | | 1,50,000 |
| Land & Building (cost) | 12,00,000 | |
| Plant & Machinery (cost) | 8,00,000 | |
| Accumulated Depreciation (1 Apr 2025) | | 3,00,000 |
| Furniture | 1,20,000 | |
| Purchases | 18,00,000 | |
| Sales | | 32,00,000 |
| Opening Inventory | 2,60,000 | |
| Wages | 3,40,000 | |
| Salaries | 2,20,000 | |
| Trade Receivables | 4,80,000 | |
| Trade Payables | | 3,10,000 |
| Cash & Bank | 9,60,000 | |
| Interest on Debentures (paid, half year) | 25,000 | |
| Rent | 90,000 | |
| Provision for Doubtful Debts (opening) | | 20,000 |
| Bank Loan (repayable 2028) | | 2,00,000 |
| Advance Tax paid | 1,00,000 | |
| Bills Receivable | 55,000 | |
| Miscellaneous Expenses | 40,000 | |
| **Total** | **64,90,000** | **64,90,000** |

**Adjustments:**
1. Closing inventory ₹3,80,000.
2. Depreciate Land & Building at 5% and Plant & Machinery at 10% on cost. Furniture at 10%.
3. Provide the remaining half-year's interest on 10% Debentures (₹25,000 outstanding).
4. Write off bad debts ₹30,000; maintain Provision for Doubtful Debts at 5% of Trade Receivables (after bad-debt write-off).
5. Outstanding wages ₹20,000; prepaid rent ₹15,000.
6. Provide for tax ₹1,60,000.
7. The Board proposes a dividend of 8% on equity capital. (Proposed dividend, per AS 4 revised, is a **non-adjusting event** and is **disclosed in notes**, not provided as a liability. Advance tax remains an asset; tax provision is a separate liability.)

---

**Step A — Work out the adjustment effects.**

*Depreciation for the year:*
- Land & Building: 5% × 12,00,000 = 60,000
- Plant & Machinery: 10% × 8,00,000 = 80,000
- Furniture: 10% × 1,20,000 = 12,000
- **Total depreciation = 1,52,000**
- Accumulated depreciation carried forward = 3,00,000 (opening) + 1,52,000 = **4,52,000**

*Debenture interest:* 10% × 5,00,000 = 50,000 for the year; 25,000 paid, so **25,000 outstanding** (finance cost 50,000 total; outstanding shown as Other Current Liability).

*Bad debts / provision:*
- Trade Receivables 4,80,000 − bad debts 30,000 = **4,50,000** net receivable.
- Provision required = 5% × 4,50,000 = **22,500**.
- Opening provision 20,000 → charge to P&L = bad debts 30,000 + (22,500 − 20,000 increase) = 30,000 + 2,500 = **32,500**.

*Wages:* 3,40,000 + outstanding 20,000 = **3,60,000**; outstanding wages 20,000 is Other Current Liability.

*Rent:* 90,000 − prepaid 15,000 = **75,000** expense; prepaid 15,000 is Other Current Asset.

*Changes in inventories:* Opening 2,60,000 − Closing 3,80,000 = **(1,20,000)** — a negative expense (stock rose), reducing total expenses. Closing inventory 3,80,000 is a current asset.

---

**Step B — Statement of Profit and Loss for the year ended 31 March 2026**

| Particulars | Note | ₹ |
|---|---|---|
| I. Revenue from Operations | | 32,00,000 |
| II. Other Income | | — |
| **III. Total Income** | | **32,00,000** |
| IV. Expenses: | | |
| Purchases of Stock-in-Trade | | 18,00,000 |
| Changes in Inventories | 8 | (1,20,000) |
| Employee Benefits Expense (Wages 3,60,000 + Salaries 2,20,000) | 9 | 5,80,000 |
| Finance Costs (Debenture interest) | 10 | 50,000 |
| Depreciation and Amortisation | | 1,52,000 |
| Other Expenses | 11 | 1,47,500 |
| **V. Total Expenses** | | **26,09,500** |
| **VI. Profit before Tax (III − V)** | | **5,90,500** |
| VII. Tax Expense — Current tax | | 1,60,000 |
| **VIII. Profit for the period** | | **4,30,500** |

*Note 11 (Other Expenses):* Rent 75,000 + Bad debts and provision 32,500 + Miscellaneous 40,000 = **1,47,500** (wages and salaries sit in Employee Benefits, not here).

**Cross-check of Total Expenses:** Purchases 18,00,000 + Changes in inventories (1,20,000) + Employee benefits 5,80,000 + Finance cost 50,000 + Depreciation 1,52,000 + Other expenses 1,47,500 = **26,09,500**. Profit before tax = 32,00,000 − 26,09,500 = **5,90,500**; less current tax 1,60,000 = **Profit for the period 4,30,500**.

*Independent check (Trading-style):* Gross profit = Sales 32,00,000 − COGS (Opening 2,60,000 + Purchases 18,00,000 − Closing 3,80,000 = 16,80,000) = 15,20,000. Less other expenses (Wages 3,60,000 + Salaries 2,20,000 + Interest 50,000 + Depreciation 1,52,000 + Rent 75,000 + Bad debts/provision 32,500 + Misc 40,000 = 9,29,500) = PBT 5,90,500. Same figure — the profit is confirmed.

---

**Step C — Surplus roll-forward**

| Surplus (Statement of P&L) | ₹ |
|---|---|
| Opening balance | 1,10,000 |
| Add: Profit for the period | 4,30,500 |
| **Closing balance (before appropriations)** | **5,40,500** |

Proposed dividend (8% × 15,00,000 = 1,20,000) is **not** deducted here — under revised AS 4 it is a non-adjusting event, disclosed in notes only. So closing Surplus carried to Balance Sheet = **₹5,40,500**.

---

**Step D — Balance Sheet of Meridian Ltd as at 31 March 2026**

| Particulars | Note | ₹ |
|---|---|---|
| **I. EQUITY AND LIABILITIES** | | |
| 1. Shareholders' Funds | | |
| (a) Share Capital | 1 | 15,00,000 |
| (b) Reserves and Surplus | 2 | 8,90,500 |
| 2. Non-Current Liabilities | | |
| (a) Long-term Borrowings | 3 | 7,00,000 |
| 3. Current Liabilities | | |
| (a) Trade Payables | | 3,10,000 |
| (b) Other Current Liabilities | 4 | 45,000 |
| (c) Short-term Provisions | 5 | 1,60,000 |
| **Total** | | **36,05,500** |
| **II. ASSETS** | | |
| 1. Non-Current Assets | | |
| (a) Property, Plant and Equipment | 6 | 16,68,000 |
| 2. Current Assets | | |
| (a) Inventories | | 3,80,000 |
| (b) Trade Receivables | 7 | 4,27,500 |
| (c) Cash and Cash Equivalents | | 9,60,000 |
| (d) Short-term Loans and Advances (Advance tax) | | 1,00,000 |
| (e) Other Current Assets (Bills Receivable 55,000 + Prepaid rent 15,000) | | 70,000 |
| **Total** | | **36,05,500** |

**Both grand totals = ₹36,05,500 — the Balance Sheet reconciles.** Two verification habits made this safe: (i) the *same* Profit for the period (₹4,30,500) that appears on the P&L is the figure added to Surplus below; and (ii) every adjustment landed on the sheet with both legs (e.g. depreciation reduced PPE and hit the P&L; outstanding wages became a current liability and raised the expense). If your two totals ever differ, do not plug a Suspense figure — re-check each note total and each adjustment's second leg.

**Supporting notes:**

- *Note 1 — Share Capital:* Authorised 2,00,000 equity shares of ₹10 = 20,00,000; Issued, subscribed and fully paid 1,50,000 shares of ₹10 = **15,00,000**.
- *Note 2 — Reserves and Surplus:* General Reserve 2,00,000 + Securities Premium 1,50,000 + Surplus (opening 1,10,000 + profit 4,30,500) 5,40,500 = **8,90,500**.
- *Note 3 — Long-term Borrowings:* 10% Debentures 5,00,000 (secured) + Bank Loan 2,00,000 = **7,00,000**.
- *Note 4 — Other Current Liabilities:* Outstanding debenture interest 25,000 + Outstanding wages 20,000 = **45,000**.
- *Note 5 — Short-term Provisions:* Provision for tax **1,60,000**.
- *Note 6 — PPE:* Gross 21,20,000 (L&B 12,00,000 + P&M 8,00,000 + Furniture 1,20,000) − Accumulated depreciation 4,52,000 = **16,68,000**.
- *Note 7 — Trade Receivables:* Gross 4,80,000 − bad debts 30,000 − provision 22,500 = **4,27,500** (all considered good, unsecured; none over six months).

**Disclosure (not provided as liability):** The Board has proposed dividend @ 8% on equity capital = ₹1,20,000, subject to member approval — disclosed under "proposed dividend" per revised AS 4; not recognised as a liability at year end.

**Teaching point — the self-check is the whole discipline.** When your two totals do not agree in the exam hall, run this drill: (1) verify each note total, (2) confirm the *same* profit flows into Surplus, (3) confirm every adjustment's *second leg* is on the sheet, (4) if it still fails, a source figure is mis-stated. Never plug the difference into "Suspense" in a company Balance Sheet.

**What if the examiner tweaks Example 3?** Common variations and the one line that changes:
- *"Debentures are redeemable in 2027 (within 12 months of year end)."* Then the ₹5,00,000 leaves Long-term Borrowings and becomes **Other Current Liabilities (current maturities)**; Long-term Borrowings falls to ₹2,00,000 (bank loan only). Totals unchanged.
- *"Transfer ₹50,000 to General Reserve."* Surplus falls to ₹4,90,500 and General Reserve rises to ₹2,50,000 — Reserves and Surplus total (and both grand totals) are **unchanged**, because the appropriation is a *movement within the same head*. This is a favourite because a careless student changes only one leg and unbalances the sheet.
- *"Tax already includes deferred tax of ₹30,000."* Split the tax line into current 1,30,000 + deferred 30,000 in the P&L; put a **Deferred Tax Liability (net) 30,000 under Non-Current Liabilities**, and the current-tax provision (net of advance tax if set-off is stated) under Short-term Provisions. Grand totals rise by 30,000 on both sides.

### Example 4 — Section 198 net profit and Section 197 managerial remuneration

**Straturn Ltd** (a public company) shows a Net Profit as per the Statement of Profit and Loss of **₹42,00,000** for the year, after debiting/crediting the following:

Debited to P&L (already reducing the ₹42,00,000):
- Managing Director's remuneration ₹6,00,000
- Provision for income tax ₹9,00,000
- Depreciation charged in books ₹5,00,000 (depreciation as per Schedule II works out to ₹4,20,000)
- Compensation paid voluntarily (not under any legal obligation) ₹1,00,000
- Loss on sale of investments (capital loss) ₹80,000

Credited to P&L (already increasing the ₹42,00,000):
- Profit on sale of a machine ₹1,50,000 (original cost ₹5,00,000; WDV ₹3,00,000; sold for ₹4,50,000)
- Profit on sale of a long-term investment (capital profit) ₹60,000
- Subsidy from government (revenue nature) ₹2,00,000

**Required:** Compute net profit under Section 198 and the maximum remuneration payable to the sole Managing Director (5% limit).

---

**Step 1 — Understand the machine profit split.** The machine cost ₹5,00,000, WDV was ₹3,00,000, sold for ₹4,50,000. Book profit = 4,50,000 − 3,00,000 = ₹1,50,000. Under Section 198, profit on sale of a fixed asset is includible **only up to original cost**. Sale price ₹4,50,000 is *below* original cost ₹5,00,000, so the **entire ₹1,50,000 is a write-back of depreciation and is fully includible** — nothing to exclude here. (If it had sold for ₹5,60,000, the ₹60,000 above cost would be excluded.)

**Step 2 — Build the Section 198 statement.**

| | ₹ | ₹ |
|---|---|---|
| Net profit as per Statement of P&L | | 42,00,000 |
| **Add back (items debited that Section 198 disallows):** | | |
| Managing Director's remuneration (base is before remuneration) | 6,00,000 | |
| Provision for income tax (not deductible u/s 198) | 9,00,000 | |
| Voluntary compensation (not a legal obligation) | 1,00,000 | |
| Capital loss on sale of investments | 80,000 | |
| Excess depreciation charged over Schedule II (5,00,000 − 4,20,000) | 80,000 | 17,60,000 |
| | | **59,60,000** |
| **Less (items credited that Section 198 excludes):** | | |
| Capital profit on sale of long-term investment | 60,000 | |
| Profit on sale of machine above original cost | Nil | 60,000 |
| **Net profit under Section 198** | | **59,00,000** |

*Notes on direction:* the government subsidy of ₹2,00,000 is **revenue** in nature, so it stays in — no adjustment. The machine profit stays in fully (Step 1). Depreciation allowed under Section 198 is the Schedule II figure ₹4,20,000; since books charged ₹5,00,000, the **excess ₹80,000 is added back** (Section 198 only allows Schedule II depreciation).

**Step 3 — Apply the Section 197 limit.** Sole Managing Director ⇒ ceiling **5% of ₹59,00,000 = ₹2,95,000**.

**Step 4 — Compare with actual.** The company actually paid the MD ₹6,00,000, but the maximum permissible without a special resolution is **₹2,95,000**. The **excess ₹3,05,000** is either recovered/refunded or regularised by a **special resolution** of shareholders (post-2018, no Central Government approval needed). If profits had instead been *inadequate*, the ceiling would come from **Schedule V** (based on effective capital), not the 5% rule.

**Self-check:** the base ₹59,00,000 is deliberately *before* charging the MD's remuneration — that is why we added ₹6,00,000 back. Applying 5% to a post-remuneration profit is the classic wrong answer.

### Example 5 — Dividend out of reserves in a year of inadequate profit (Section 123 Rules)

**Cobalt Ltd** has paid-up equity share capital of **₹50,00,000** and free reserves of **₹30,00,000** at the start of the year. Its profit this year is only **₹1,20,000** — inadequate to sustain its usual dividend. The Board wishes to draw on reserves to pay a dividend. Dividend rates declared in the last three years were **12%, 10% and 8%**. Determine the maximum dividend the company may declare out of accumulated reserves under the Companies (Declaration and Payment of Dividend) Rules.

---

Apply the three statutory ceilings; the **lowest** governs.

**Ceiling 1 — Rate cap (average of last three years' rates):**
Average rate = (12% + 10% + 8%) ÷ 3 = **10%**.
Maximum dividend by rate = 10% × paid-up capital ₹50,00,000 = **₹5,00,000**.

**Ceiling 2 — Amount drawn from reserves cannot exceed 1/10th (10%) of (paid-up capital + free reserves):**
= 10% × (50,00,000 + 30,00,000) = 10% × 80,00,000 = **₹8,00,000** is the maximum *withdrawal* from reserves.
Since current profit is ₹1,20,000, the withdrawal needed to fund a ₹5,00,000 dividend = 5,00,000 − 1,20,000 = **₹3,80,000**, which is within the ₹8,00,000 cap. (Constraint satisfied.)

**Ceiling 3 — Residual reserves after withdrawal must not fall below 15% of paid-up capital:**
Minimum reserves to retain = 15% × 50,00,000 = **₹7,50,000**.
Reserves after withdrawing ₹3,80,000 = 30,00,000 − 3,80,000 = **₹26,20,000** ≥ ₹7,50,000. (Constraint satisfied.)

**Conclusion.** All three tests are met at a dividend of **₹5,00,000** (10% of capital), funded by current profit ₹1,20,000 + reserve withdrawal ₹3,80,000. The **binding constraint is Ceiling 1 (the rate cap)** — it caps the dividend at ₹5,00,000 even though the withdrawal and residual-reserve rules would each permit more.

**What if the examiner tweaks it?** Suppose free reserves were only ₹10,00,000 (not ₹30,00,000). Then Ceiling 2 withdrawal cap = 10% × (50,00,000 + 10,00,000) = ₹6,00,000 (still enough for the ₹3,80,000 draw), **but** Ceiling 3 now requires residual ≥ ₹7,50,000, and reserves after a ₹3,80,000 draw = 10,00,000 − 3,80,000 = ₹6,20,000, which is **below ₹7,50,000 — fails**. The maximum permissible withdrawal then = 10,00,000 − 7,50,000 = **₹2,50,000**, so the maximum dividend = current profit 1,20,000 + 2,50,000 = **₹3,70,000** (a rate of 7.4%). Here **Ceiling 3 becomes binding**. The lesson: always test all three and let the smallest win; which one binds depends on the reserve cushion.

## 6. Presentation & Disclosure Formats

**Rounding-off (Schedule III General Instruction):** where turnover is **less than ₹100 crore**, figures may be rounded to the nearest **hundreds, thousands, lakhs or millions**; where turnover is **₹100 crore or more**, to the nearest **lakhs, millions or crores**. The **same unit** must be used throughout. *(These are the thresholds after the 2019 amendment substituting "turnover" for the older "total income" trigger — verify against the latest ICAI material / AY.)*

**Comparatives:** every line item must show the **corresponding figure for the immediately preceding reporting period**, including in the notes. A new Schedule III addition requires that if a company changes the presentation, the previous year is reclassified with an explanation.

**Cross-referencing:** each line on the face of the Balance Sheet / P&L carries a **note number**; the note repeats the head, gives the current and previous year figures, and its total ties exactly to the face.

**Skeleton Notes format (illustrative):**

```
Note 2 — Reserves and Surplus                As at 31.03.26   As at 31.03.25
  Capital Redemption Reserve                       xxx            xxx
  Securities Premium                               xxx            xxx
  General Reserve
    Opening balance                                xxx
    Add: transfer from surplus                     xxx            xxx
  Surplus (Statement of Profit and Loss)
    Opening balance                                xxx
    Add: Profit for the period                     xxx
    Less: Appropriations (dividend, transfers)    (xxx)           xxx
  Total                                            ===            ===
```

**Additional mandated disclosures (a checklist):**
- **Contingent liabilities and commitments** (to the extent not provided for): claims against the company not acknowledged as debts; guarantees; other money for which the company is contingently liable; estimated capital commitments; other commitments — **disclosed in notes, not on the face**.
- **Dividends proposed** (post AS 4 revision) — disclosed, not provided.
- **Arrears of fixed cumulative dividends** on preference shares.
- **Value of imports (CIF), foreign currency expenditure and earnings.**
- **Auditor's remuneration** split by service.
- **Related party disclosures** (AS 18), **segment disclosures** (AS 17), **leases** (AS 19), **EPS** (AS 20) — driven by the respective Accounting Standard but presented within these financial statements.

**Newer Schedule III disclosure additions worth flagging** (introduced by the March 2021 amendment — *verify applicability to your AY / ICAI syllabus cut-off*): ageing schedules for **Trade Receivables, Trade Payables, Capital Work-in-Progress and Intangible Assets under Development**; disclosure of **promoter shareholding and its changes**; details of **loans to related parties**; **title deeds of immovable property not held in the company's name**; and ratios such as **current ratio, debt-equity, return on equity** with explanations for variances above a threshold. The exam emphasis in the AS/Intermediate stream stays on the classic disclosures above, but knowing these exist prevents surprise in objective questions.

**The face-vs-notes rule restated as a test you can apply:** anything the distant reader needs as a *headline number to make the two sides reconcile* goes on the **face** (a single figure per line item); everything that is *breakup, movement, or narrative* goes in the **notes**. Contingent liabilities, being amounts *not* recognised (they never enter the two totals), can only live in notes — putting them on the face would corrupt the reconciliation.

## 7. Connections

Schedule III is the terminal where almost every other Advanced Accounting topic arrives:

- **AS 4 (Events after the Balance Sheet date)** decides that **proposed dividend is not a liability** — directly changing what appears under Short-term Provisions.
- **AS 3 (Cash Flow Statement)** is the third mandatory statement for non-small companies; its closing cash ties to "Cash and Cash Equivalents."
- **Schedule II (Depreciation)** feeds the depreciation line and accumulated depreciation in PPE.
- **Redemption of Preference Shares / Buy-back** create **Capital Redemption Reserve**, shown under Reserves and Surplus.
- **Debentures** and their **Debenture Redemption Reserve** sit in borrowings and reserves respectively; current maturities move to Other Current Liabilities.
- **Bonus issue** and **rights issue** change Share Capital and Securities Premium and require the 5-year disclosure in the Share Capital note.
- **Section 198 net profit** links the P&L to **managerial remuneration** and to **divisible profits / dividend** decisions.
- **Amalgamation and internal reconstruction** ultimately present the merged entity's position in this very format.
- **AS 22 (Deferred Tax)** produces the DTL/DTA (net) line — always non-current — and splits the tax line in the P&L into current and deferred.
- **AS 5** governs how **exceptional and extraordinary items** and prior-period items are surfaced separately on the P&L face, protecting the sustainable-profit reading.

```mermaid
flowchart LR
    AS3["AS 3 Cash Flow"] --> SF["Schedule III Financial Statements"]
    AS4["AS 4 Events after BS date"] --> SF
    SCH2["Schedule II Depreciation"] --> SF
    CRR["CRR from redemption / buyback"] --> SF
    SEC198["Sec 198 net profit"] --> SF
    SF --> REM["Sec 197 Managerial Remuneration"]
    SF --> DIV["Sec 123 Dividend / Divisible Profits"]
```
*Figure 4 — Schedule III as the convergence point of standards and provisions, and the launchpad for remuneration and dividend decisions.*

```mermaid
flowchart TD
    PL["Profit as per Statement of P and L"] --> ADJ["Section 198 adjustments"]
    ADJ --> A1["Add back remuneration and tax and excess depreciation and capital losses"]
    ADJ --> A2["Exclude capital profits and premium and profit on asset above cost"]
    A1 --> NP["Net profit under Section 198"]
    A2 --> NP
    NP --> R197["Section 197 remuneration ceiling 11 percent overall"]
    NP --> BASE["Base for reasonableness of dividend policy"]
```
*Figure 5 — How the accounting profit is transformed into the Section 198 base before the remuneration percentages bite.*

## 8. Traps & Examiner Tricks

1. **Current maturities of long-term debt** go to **Other Current Liabilities**, never to Short-term Borrowings or Long-term Borrowings. Examiners love a term loan with an instalment due next year.
2. **Proposed dividend** — post revised AS 4, do **not** create a provision; **disclose** in notes. Old textbooks (and habit) will tempt you to deduct it from Surplus and show it as a current liability. Wrong under current law.
3. **Calls-in-arrears** are a **deduction from Subscribed Capital**, not an asset. **Calls-in-advance** are a liability (Other Current Liabilities), not capital.
4. **Debit balance of Surplus (accumulated loss)** is shown as a **negative figure under Reserves and Surplus** — never as an asset ("Miscellaneous Expenditure not written off" was the old, now-abolished treatment).
5. **Trade vs non-trade:** amount receivable on **sale of a fixed asset** is NOT a Trade Receivable; it is "Other Current/Non-Current Assets." Same for a payable on purchase of machinery.
6. **Loose tools, stores and spares, packing material** are **Inventories**, not PPE.
7. **Provision for tax vs Advance tax / TDS** — do not net them unless the question says a right of set-off exists; show provision under Short-term Provisions and advance tax under Short-term Loans and Advances.
8. **Section 198 profit ≠ P&L profit.** Do not apply the 11%/5% remuneration cap on the reported net profit; recompute per Section 198 (exclude capital profits, add back the remuneration itself before applying the percentage).
9. **Profit on sale of fixed asset** enters Section 198 only up to **original cost** (i.e. depreciation write-back); the capital-profit excess is excluded.
10. **Bank overdraft / cash credit** = Short-term Borrowings (current), even though it may roll over for years — because there is no unconditional right to defer.
11. **Securities Premium** can only be used for the purposes in **Section 52** (bonus shares, writing off preliminary expenses / share issue expenses, premium on redemption of debentures/preference shares, buy-back). It is **not a free reserve** available for dividend.
12. **Rounding:** using two different units in the same set of statements is a presentation error; the threshold turns on turnover (₹100 crore).
13. **Same profit both sides:** the number added to Surplus on the Balance Sheet must be exactly the "Profit for the period" on the P&L. A mismatch is the number-one cause of a non-balancing sheet.
14. **Long production cycle:** inventory realisable *after* 12 months but *within* the operating cycle is **current** — do not mechanically apply the 12-month test first; the operating-cycle branch is checked first.
15. **Changes in inventories** covers only finished goods / WIP / stock-in-trade — **never raw materials** (raw-material movement is inside "cost of materials consumed"). Slotting raw-material stock here double-counts.
16. **Appropriation within Reserves and Surplus** (transfer to General Reserve) does **not** change the Reserves and Surplus total or the grand totals — a candidate who changes only one leg unbalances the sheet.
17. **Capital advance for a fixed asset** is **Long-term Loans and Advances (non-current)**, not a current advance — it follows the asset it will become.
18. **Section 197 applies to public companies;** a **private company** is not bound by the 11% ceiling. Also, **sitting fees are outside** the 11% cap.
19. **Depreciation for Section 198** is the **Schedule II** amount, not the books figure — add back any excess book depreciation, deduct any shortfall.
20. **Dividend out of reserves — three ceilings, lowest binds.** Do not stop at the rate cap; also test the 10%-of-(capital+free-reserves) withdrawal cap and the 15%-of-capital residual-reserve floor. The binding constraint shifts with the size of the reserve cushion.
21. **Share application money:** the refundable portion is a **current liability**, only the allottable portion sits on the "Share Application Money Pending Allotment" line — one figure can split across both.
22. **Interest accrued (due or not due)** on a long-term loan is a **current liability (Other Current Liabilities)**, even though the loan principal is non-current.

## 9. First-Principles Recap

Strip everything away and rebuild it from the single problem: *thousands of distant readers must extract the same facts from every company with no ability to ask questions.* From that one constraint, the entire chapter follows by necessity:

- Because readers are distant and many → a **prescribed, uniform format** (Schedule III) so the same fact lives in the same box everywhere.
- Because the deepest question is *timing of cash* → a **current vs non-current** split governed by the **operating cycle / 12-month** test, with the operating-cycle branch checked *first*.
- Because a headline and the fine print serve different readers → a **short face** plus **detailed Notes**, with unrecognised items (contingencies) confined to notes so the two totals stay clean.
- Because substance beats form → **Accounting Standards and the Act override** the template where they differ, and a **true and fair view** sits above the format as a floor of disclosure.
- Because different regimes exist → **three Divisions** (AS / Ind AS / NBFC Ind AS) share the same DNA but differ in headings; Division I is the AS-regime template you draft in.
- Because managers and owners draw money out of the company → **Section 197** caps remuneration (on **Section 198** profit) and **Section 123** governs the **divisible profit** available for dividend, with reserves and depreciation as gatekeepers.
- Because a distributable decision must not ride on a non-distributable number → **Section 198 redefines profit**, stripping out capital gains and adding back remuneration and tax, so the percentage caps bite on a sustainable base.
- Because every transaction has two effects → the statements **self-check**: the two grand totals must reconcile, and the profit must be identical on both statements.

If you remember only the constraint and the two-legged self-check, you can reconstruct every rule rather than recall it.

## 10. Quick-Revision Sheet

**Statements (Sec 2(40)):** Balance Sheet + Statement of P&L + Cash Flow (except OPC/small/dormant/startup private) + notes. True and fair view (Sec 129), Schedule III **Division I** form (AS regime). FY ends 31 March. SOCE is Ind AS only.

**Balance Sheet order — Equity & Liabilities:** Shareholders' Funds (Share Capital; Reserves & Surplus; Warrants) → Share Application Money Pending Allotment → Non-Current Liabilities (Long-term Borrowings; DTL net; Other LT Liab; LT Provisions) → Current Liabilities (Short-term Borrowings; Trade Payables; Other Current Liab; Short-term Provisions).

**Balance Sheet order — Assets:** Non-Current (PPE & Intangibles incl. CWIP; Non-Current Investments; DTA net; LT Loans & Advances; Other NCA) → Current (Current Investments; Inventories; Trade Receivables; Cash & Cash Equivalents; ST Loans & Advances; Other CA).

**Current test (any one):** within operating cycle / held for trading / due within 12 months / cash equivalent (assets) or no unconditional right to defer 12 months (liabilities). Operating cycle unknown → **12 months**. Operating-cycle branch is tested **first** — long-cycle inventory realisable after 12 months is still current.

**P&L sequence:** Revenue from Operations + Other Income = Total Income; less Expenses (Materials consumed; Purchases of stock-in-trade; **Changes in inventories = Opening − Closing**, FG/WIP/stock-in-trade only; Employee benefits; Finance costs; Depreciation; Other) = PBT before exceptional/extraordinary; ± exceptional/extraordinary → PBT; less tax (current + deferred) → Profit for the period; then EPS.

**Key placements:** current maturities of LT debt → **Other Current Liabilities**; calls-in-arrears → deduct from capital; calls-in-advance → OCL; accumulated loss → negative Surplus; loose tools/stores/spares → Inventories; capital advance → LT Loans & Advances (NC); unclaimed dividend & interest accrued → OCL; bank OD → Short-term Borrowings; DTL/DTA → non-current, shown net.

**Managerial remuneration (Sec 197, public co.):** overall **11%**; one MD/WTD **5%**; more than one **10%**; other directors **1%** (with MD) / **3%** (without). On **Section 198** profit (exclude capital profits; add back remuneration itself, income tax, excess book depreciation, capital losses, voluntary compensation; profit on sale of asset only up to original cost; depreciation allowed = Schedule II). Excess → **special resolution**; inadequate profit → **Schedule V**. Sitting fees are outside the cap; private companies not bound.

**Dividend (Sec 123):** out of current profit (after depreciation) / accumulated reserves / govt money. Inadequate-profit dividend from reserves — test all three, lowest binds: rate ≤ **3-yr average**; draw ≤ **10% of (paid-up + free reserves)**; residual reserve ≥ **15% of paid-up capital**; set off current loss first; no dividend if in default on deposits/debentures. Unpaid dividend → separate account in **7 days**; unclaimed **7 years** → **IEPF**. Proposed dividend → **disclose only** (AS 4).

**Disclosures to never forget:** contingent liabilities & commitments (notes only); shareholders holding >5%; 5-year history of bonus/other-than-cash/buy-back shares; receivables > 6 months; default in loan repayment; auditor's remuneration; CIF imports and foreign currency dealings; rounding-off (₹100 crore turnover threshold); comparatives for every line; (newer) ageing schedules, promoter holding, key ratios — *verify AY*.

**Golden self-check:** the profit added to Surplus (Balance Sheet) = Profit for the period (P&L); every adjustment has two legs; appropriations move *within* a head and never change the total; the two grand totals **must** be equal — no Suspense in a company Balance Sheet.
