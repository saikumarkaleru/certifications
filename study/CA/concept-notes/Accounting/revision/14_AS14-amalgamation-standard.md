# AS 14: Accounting for Amalgamations

## Snapshot
Governs how a transferor company's assets, liabilities and reserves enter the transferee's books when two companies combine. Two methods — pooling (merger) vs purchase — decided by a 5-condition test on the facts, not the label. Applies to companies under the Companies Act; NOT where the acquired company keeps separate existence (that is AS 21 consolidation).

## Core concepts
- **Facts drive method, never the label.** The same deal can be merger or purchase depending on how you paid, what you transferred, whether you revalued.
- **Transferor** = company amalgamated into another (ceases to exist). **Transferee** = surviving/new company.
- **Reserve** = surplus not intended to meet any liability, contingency, commitment or diminution in asset value.
- **Consideration** = aggregate of shares + other securities + cash/other assets given by transferee to the **shareholders** of the transferor. NOT payment to debenture-holders or settlement of liabilities.
- **Fair value** = arm's-length exchange amount between knowledgeable willing parties.
- **Absorption** = existing company takes over existing companies (no new company). **External reconstruction** = new company floated to take over a loss-making company (= purchase by design). **Internal reconstruction** = reorganising own capital, no new entity — OUTSIDE AS 14.

## Key provisions / rules

**Two categories only:** merger (pooling) or purchase (purchase method). No third.

**Five merger conditions — ALL must be met (any one fails → PURCHASE):**
1. ALL assets and liabilities of transferor become those of transferee.
2. Shareholders holding **≥ 90% of face value of equity shares** (excluding shares already held by transferee/its subsidiaries/nominees) become equity shareholders of transferee.
3. Consideration to those equity shareholders discharged **wholly by equity shares** in transferee (cash ONLY for fractional shares).
4. Business of transferor **intended to be carried on** by transferee.
5. **No adjustment** to book values of transferor's assets/liabilities, except to achieve uniformity of accounting policies (routed through reserves).

Condition 2 nuances: measured on **face value** (not market value, not number of shareholders); excludes transferee's existing holding from both numerator and base; concerns **equity** only.

**Method 1 — Pooling of Interests (merger):**
- Assets, liabilities AND reserves recorded at **book value**.
- All reserves survive with identity (General, Capital, Statutory, P&L). Statutory reserves keep status naturally — no Amalgamation Adjustment Reserve.
- **No goodwill / no capital reserve** arises.
- Balancing figure adjusted in **reserves**, never goodwill:
  Reserve adjustment = (Equity share capital issued + cash for fractions) − (Equity share capital of transferor).
  Positive → reduce reserves; negative → increase reserves. Only relabels capital vs reserves; total net assets unchanged.
- Order when reducing: first debit capital/free reserves, then revenue reserves; statutory reserves untouched.

**Method 2 — Purchase Method:**
- Assets/liabilities recorded at existing carrying amounts or (more commonly) **fair values** at date of amalgamation. Only assets/liabilities acquired — NOT reserves.
- Reserves do NOT carry over. **Exception:** statutory reserves required by law are retained by debiting **Amalgamation Adjustment Reserve** (shown as negative figure under Reserves & Surplus) and crediting the statutory reserve; reversed when the statutory need lapses.
- Balancing figure:

| PC vs Net assets acquired (fair value) | Result |
|---|---|
| PC > Net assets | **Goodwill** (asset) |
| PC < Net assets | **Capital Reserve** |

- **Goodwill on amalgamation** amortised over useful life, **normally not exceeding 5 years** (NOT AS 26's 10-year ceiling).
- Fair-value step-up creates NO revaluation reserve/profit — absorbed into the goodwill/capital reserve figure.

**Purchase Consideration methods:**
- **Net Assets method:** PC = agreed value of assets taken over − agreed value of liabilities taken over.
- **Net Payments method:** PC = total payments (shares + cash + securities) to shareholders. Exclude payments to debenture-holders/creditors.
- **Lump-sum method:** single stated figure, use directly.
- **Intrinsic value / exchange-ratio method:** Exchange ratio = intrinsic value per share of transferor ÷ intrinsic value per share of transferee; × transferor's shares = transferee shares issued.

Net assets acquired = FV of assets taken over − FV of liabilities taken over. **Exclude fictitious assets** (preliminary expenses, discount on issue, debit balance of P&L). Existing goodwill included only if specifically taken over. Shares issued recorded at agreed/issue value (may include securities premium).

## Journal entries

**Purchase method (transferee books):**
```
(1) Business Purchase A/c            Dr.  (= PC)
        To Liquidator of Transferor Co.
(2) Assets A/c (individual, fair value)  Dr.
    Goodwill A/c (balancing, if any)     Dr.
        To Liabilities A/c (fair value)
        To Business Purchase A/c
        To Capital Reserve A/c (balancing, if any)
(3) Liquidator of Transferor Co.     Dr.
        To Equity Share Capital A/c
        To Securities Premium A/c (if at premium)
        To Bank A/c (cash component)
(4) Settle debentures / liabilities not in PC; amalgamation expenses
```

**Pooling (transferee books):**
```
(1) Business Purchase A/c            Dr.  (= consideration, wholly equity)
        To Liquidator of Transferor Co.
(2) Assets A/c (BOOK value)          Dr.
        To Liabilities A/c (BOOK value)
        To Reserves A/c (General, Statutory, P&L at BOOK value)
        To Business Purchase A/c
   (Balancing difference ADJUSTED IN RESERVES — never goodwill)
(3) Liquidator of Transferor Co.     Dr.
        To Equity Share Capital A/c
        To Bank A/c (cash for fractions only)
```
Transferor's books use a **Realisation A/c** route (transfer assets/liabilities, credit PC receivable, distribute to shareholders).

## Worked mini-example
Purchase: PC = 60,000 shares × ₹12 = ₹7,20,000 (₹6,00,000 capital + ₹1,20,000 premium). Assets taken over at FV ₹11,80,000 (excl. preliminary exp), liabilities ₹3,00,000 → net assets ₹8,80,000. PC ₹7,20,000 < ₹8,80,000 → **Capital Reserve ₹1,60,000**. If PC were ₹10,80,000 → **Goodwill ₹2,00,000**, amortise ~₹40,000 p.a. over 5 yrs.

**Pre-existing holding:** transferee owns 20% already. Pay consideration only to outside (80%) shareholders; add cancelled investment (carrying value) to cost. Cost of acquisition = new consideration + old investment; compare with net assets → goodwill/capital reserve.

## Disclosures
**All amalgamations:** names & nature of business of amalgamating companies; effective date; method of accounting; particulars of the scheme.
**Pooling adds:** description & number of shares issued + % of each company's equity exchanged; difference between consideration and value of net identifiable assets and its treatment (adjustment to reserves).
**Purchase adds:** consideration and description of components; amount of goodwill/capital reserve and treatment (goodwill amortisation period).
- Amalgamation Adjustment Reserve → negative amount under Reserves & Surplus.
- **Scheme contrary to AS 14:** follow the scheme, but disclose the fact, deviation and financial effect.
- **Amalgamation after B/S date but before accounts approved:** disclose only (non-adjusting event); not incorporated.

## Exam traps & must-remember
- "90% became shareholders → merger" is WRONG: condition 2 necessary but not sufficient; condition 3 still needs wholly-equity consideration. Cash to a minority (beyond fractions) → purchase.
- Do NOT include debenture discharge / creditor settlement in PC (paid to owners only).
- Exclude fictitious assets from net assets acquired.
- No reserves brought in under purchase (except statutory via Amalgamation Adjustment Reserve).
- Pooling NEVER produces goodwill/capital reserve — writing "Goodwill" in a merger answer is wrong.
- Direction: PC > net assets → Goodwill; PC < net assets → Capital Reserve.
- Fair value = purchase; book value = pooling.
- Goodwill amortisation normally ≤ 5 years (not 10).
- Split share consideration above par into Share Capital + Securities Premium.
- Amalgamation Adjustment Reserve only under purchase, only for statutory reserves.
- Cancel inter-company balances; strip unrealised profit in unsold stock before combined B/S.
- Amalgamation expenses are **expensed**, never capitalised into goodwill.

## One-line recall
- Facts (not label) → all 5 conditions met = merger/pooling; any fail = purchase.
- Pooling: book value, reserves survive, no goodwill, difference to reserves.
- Purchase: fair value, reserves lost (statutory via Amalgamation Adjustment Reserve), goodwill or capital reserve.
- PC = to shareholders only; exclude debentures/creditors/fictitious assets.
- Goodwill amortise normally ≤ 5 yrs; expenses written off.
- Transferor keeps separate existence → AS 21, not AS 14.
