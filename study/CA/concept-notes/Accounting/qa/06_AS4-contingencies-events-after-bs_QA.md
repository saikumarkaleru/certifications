# Q&A — AS 4 — Contingencies & Events After the Balance Sheet Date

> Companion question bank to the concept chapter. Indian ICAI Accounting Standards, all amounts in Rupees (₹). AS 4 (revised) governs **Contingencies** (partly superseded by AS 29 — only the *disclosure of contingencies in financial statements approved by approving authority* survives) and **Events Occurring After the Balance Sheet Date**. Keep the two dates clear: **Balance Sheet date** (e.g., 31 March) and the **date of approval** of financial statements by the Board/approving authority.

---

## Section A — Concept-Check Questions (test the WHY)

**A1. What is the exact "window" that AS 4 calls the events-after-the-balance-sheet-date period?**
Model answer: The period between the **balance sheet date** and the **date on which the financial statements are approved** by the Board of Directors (or corresponding approving authority for other entities). Events in this window are the only ones considered under AS 4. Anything after approval is outside scope.

**A2. Distinguish "adjusting" and "non-adjusting" events on first principles.**
Model answer: An **adjusting event** provides *additional evidence of conditions that already existed at the balance sheet date* — so the balance sheet was, in effect, incomplete; we adjust assets/liabilities. A **non-adjusting event** arises from *conditions that came into existence after the balance sheet date* — the balance sheet was correct as it stood, so we do **not** adjust; we only disclose if material. The test is the **date the underlying condition arose**, not the date the information reached us.

**A3. Why are proposed dividends treated specially, and what changed after the Companies (Accounting Standards) Amendment 2016?**
Model answer: Declaration/proposal of dividend for the period is an event after the balance sheet date. Post-amendment, a dividend proposed/declared **after** the balance sheet date but **before** approval of financial statements is a **non-adjusting event** — it is **not** recognised as a liability at the balance sheet date (aligning with AS 4's general logic and the Companies Act 2013, where dividend is a liability only when *approved by shareholders*). It is instead **disclosed in the notes**.

**A4. Why does AS 4 require adjustment even for a non-adjusting event in the case of "going concern"?**
Model answer: If an event after the balance sheet date indicates the **going concern assumption is no longer appropriate** (e.g., the entity decides to liquidate or has no realistic alternative), the *entire basis of accounting changes* from going concern to break-up/realisable values. This is a fundamental accounting assumption (AS 1), so the accounts **must** be recast — it is an exception where a "post-date condition" still forces adjustment.

**A5. A contingency existing at the balance sheet date is resolved before approval. Adjust or disclose?**
Model answer: **Adjust.** Resolution of a contingency (that existed at the balance sheet date) by an event after the date provides evidence of conditions existing at that date — it is an adjusting event. Example: a debtor declared insolvent after year-end confirms the debt was doubtful at year-end.

**A6. Why is "statutory disclosure of dividends in the Companies Act" still relevant to AS 4?**
Model answer: AS 4 requires disclosure of the amount and nature of events after the balance sheet date. Proposed dividend, being non-adjusting, must be disclosed; the Companies Act separately mandates dividend disclosure in the Board's report/notes. AS 4 and the Act operate together: no liability recognised, but full transparency in notes.

**A7. Which part of "Contingencies" under AS 4 is still live after AS 29?**
Model answer: Almost all recognition/measurement of contingencies moved to **AS 29 (Provisions, Contingent Liabilities and Contingent Assets)**. AS 4 retains only paragraphs dealing with **events after the balance sheet date** and the residual requirement that **contingencies existing at the balance sheet date must be considered up to the date of approval** for adjustment/disclosure.

---

## Section B — Graded Computational / Practical Problems

### B1 (Easy) — Insolvency of a debtor
A Ltd's balance sheet at 31 March 2026 shows Sundry Debtors ₹8,00,000, including ₹1,20,000 due from X. On 20 April 2026 (accounts approved 15 May 2026), X is declared insolvent; only 25 paise in the rupee is expected. Advise treatment and pass the entry.

Solution:
- Condition (X's financial weakness) existed at 31 March 2026; insolvency after year-end is *evidence* of that condition → **adjusting event**.
- Recoverable = 25% × ₹1,20,000 = ₹30,000. Loss/provision = ₹1,20,000 − ₹30,000 = **₹90,000**.
- Entry (31 March 2026):

```
Bad Debts / Provision for Doubtful Debts A/c   Dr.  90,000
      To Sundry Debtors (X) A/c                              90,000
(Being loss on debt from X, insolvent after B/S date, adjusted)
```
Debtors now carried at ₹8,00,000 − ₹90,000 = **₹7,10,000**.

### B2 (Easy–Moderate) — Proposed dividend
B Ltd, at 31 March 2026, has profits of ₹50,00,000. On 25 April 2026 the Board proposes a dividend of ₹6,00,000; accounts approved 30 April 2026. How is this treated?

Solution:
- Dividend proposed after balance sheet date but before approval = **non-adjusting event** (post-2016 amendment).
- **No liability** for ₹6,00,000 is recognised at 31 March 2026; reserves/surplus are **not** reduced.
- **Disclosure** in notes: "The Board of Directors has proposed a dividend of ₹6,00,000 for the year ended 31 March 2026, which is subject to approval of shareholders and has not been recognised as a liability." The provision is made in the year of shareholder approval.

### B3 (Moderate) — Fire after the balance sheet date
C Ltd's factory (carrying amount ₹40,00,000) is destroyed by fire on 12 April 2026. Accounts for the year ended 31 March 2026 are approved on 28 May 2026. The loss is material and impairs going concern of that division only (entity as a whole is a going concern).

Solution:
- The fire is a **new condition** arising after 31 March 2026 → **non-adjusting event**. Assets are **not** written down in the 2025–26 accounts.
- Going concern of the *entity* is intact, so no recast.
- **Disclosure** required (nature + estimate of financial effect): "A fire on 12 April 2026 destroyed factory assets of carrying amount ₹40,00,000; the loss, partly covered by insurance, will be accounted for in 2026–27." If the estimate cannot be made, state that fact.

### B4 (Moderate–Hard) — Court judgment: adjusting vs non-adjusting
D Ltd is defending two suits at 31 March 2026:
(i) Suit A (relating to a defective product sold in Feb 2026) — court decrees ₹5,00,000 against D Ltd on 18 April 2026.
(ii) Suit B — arises from a contract breach that D Ltd committed on 10 April 2026 (after year-end); claim ₹3,00,000.
Accounts approved 20 May 2026. Treat each.

Solution:
- **Suit A:** the obligating event (defective sale) existed at 31 March 2026; judgment confirms a present obligation at year-end → **adjusting event**. Recognise a **provision of ₹5,00,000**:

```
Legal Claim (P&L) A/c        Dr.  5,00,000
      To Provision for Legal Claim A/c        5,00,000
```
- **Suit B:** the breach occurred *after* the balance sheet date — the condition did not exist at 31 March 2026 → **non-adjusting event**. No provision; **disclose** nature and estimated effect (₹3,00,000) if material.

### B5 (Exam-Hard) — Multiple events, combined statement
E Ltd, year ended 31 March 2026, accounts approved by Board on 10 June 2026. Consider each independent event and state treatment with amounts:

1. Inventory costing ₹10,00,000 (at 31 March) sold on 5 May 2026 for ₹7,50,000 (net realisable value fall due to market conditions existing at year-end).
2. A debtor of ₹2,00,000 paid in full on 15 April 2026 (previously provided 50% as doubtful).
3. Board decides on 20 May 2026 to close a major division and liquidate the whole company; no realistic alternative.
4. Proposed dividend ₹4,00,000 on 12 May 2026.
5. Acquisition of another company announced 1 June 2026 for ₹90,00,000.

Solution:
1. **Adjusting.** NRV condition (obsolescence/market) existed at year-end; the sale confirms NRV < cost. Write inventory down to ₹7,50,000 → loss **₹2,50,000** charged to P&L. AS 2 (lower of cost/NRV) reinforced by AS 4 evidence.
2. **Adjusting.** Full recovery is evidence the debt was good at year-end. **Reverse** the 50% provision (₹1,00,000); debtor carried at full ₹2,00,000.
3. **Fundamental — going concern lost.** Even though the decision is post-date, the going concern assumption is no longer appropriate → **recast entire accounts** on break-up/net realisable value basis; disclose the fact and basis. This overrides the "non-adjusting" default.
4. **Non-adjusting.** No liability; disclose proposed dividend ₹4,00,000 in notes.
5. **Non-adjusting.** New condition after year-end; **disclose** nature and estimated financial effect (₹90,00,000) — material acquisition affecting users' decisions.

Presentation note: only items 1, 2 and 3 change the numbers in the balance sheet/P&L; items 4 and 5 are notes-only.

---

## Section C — Past-Paper-Style Full Questions (ICAI pattern)

### C1 (5 marks) — State with reasons
"An event occurring after the balance sheet date should be adjusted only if it provides evidence of conditions existing at the balance sheet date." In light of AS 4, discuss the following in the books of P Ltd for the year ended 31 March 2026 (accounts approved 15 July 2026):
(a) A major customer became insolvent on 10 May 2026; ₹3,50,000 receivable now irrecoverable.
(b) The company's warehouse was flooded on 2 June 2026; goods worth ₹6,00,000 destroyed.
(c) Wage revision agreement signed 20 June 2026, effective retrospectively from 1 January 2026, additional liability ₹2,80,000.

Model answer:
- (a) **Adjusting event.** Insolvency after year-end confirms the receivable was doubtful at 31 March 2026 (condition existed). Write off / provide **₹3,50,000** against P&L; debtors reduced accordingly.
- (b) **Non-adjusting event.** Flood is a new condition arising after year-end. No adjustment to accounts. Since material, **disclose** the nature of the event and estimated financial effect of ₹6,00,000 (net of insurance) in the notes.
- (c) **Adjusting event.** Although the agreement was signed after year-end, it is effective from 1 January 2026, so an obligation for the period 1 Jan–31 Mar 2026 existed at the balance sheet date. Provide the **proportionate additional liability** for that quarter (the ₹2,80,000 relating to the post-year-end period, if any, is expensed in 2026–27). Recognise a provision for the pre-year-end portion.

### C2 (5 marks) — Dividend and going concern
Q Ltd's draft accounts for the year ended 31 March 2026 show net profit ₹80,00,000. Before approval of accounts on 5 August 2026:
(i) The Board proposes a dividend of ₹12,00,000 on 30 June 2026.
(ii) A fraud of ₹9,00,000 committed by an employee during 2025–26 is detected on 20 July 2026.
(iii) The company loses its principal manufacturing licence on 25 July 2026 and has no means to continue operations.
Discuss treatment under AS 4.

Model answer:
- (i) **Non-adjusting** (post-2016 amendment): proposed dividend of ₹12,00,000 is **not** provided as a liability at 31 March 2026; **disclose** in notes.
- (ii) **Adjusting event.** The fraud occurred *during* 2025–26, so the loss condition existed at the balance sheet date; detection after year-end is merely evidence. Adjust accounts: recognise loss/expense of **₹9,00,000** and reduce the related asset/recognise receivable from employee as appropriate.
- (iii) **Going concern lost.** Loss of the principal licence with no ability to continue means the going concern assumption is inappropriate. **Recast the entire financial statements** on a liquidation/realisable value basis and disclose the fact — an adjusting outcome by exception, even though the trigger is post-date.

### C3 (4 marks) — Theory
Explain the disclosure requirements of AS 4 for a non-adjusting event that is material.

Model answer: For a material non-adjusting event, no amounts in the financial statements are adjusted, but the entity must **disclose in the notes**: (a) the **nature** of the event; and (b) an **estimate of its financial effect**, or a statement that such an estimate **cannot be made**. The purpose is to prevent users from being misled — omission of a material post-date event would affect their ability to make proper evaluations and decisions. (Reference: AS 4 disclosure clause; proposed dividends and material acquisitions are common examples.)

---

## Section D — MCQs / Case Scenarios (≈30% weight pattern)

**D1.** The "events after the balance sheet date" period ends on the date:
(a) of the balance sheet (b) of the AGM (c) financial statements are approved by the approving authority (d) of filing with ROC.
**Ans: (c).** AS 4 defines the window as B/S date to date of approval by Board/approving authority.

**D2.** Settlement of a court case (relating to a pre-year-end obligation) after the balance sheet date but before approval is:
(a) non-adjusting (b) adjusting (c) ignored (d) disclosed only.
**Ans: (b).** Confirms a condition existing at the balance sheet date.

**D3.** Dividend proposed by the Board after the balance sheet date (post-2016 amendment) is:
(a) a liability at B/S date (b) a non-adjusting event disclosed in notes (c) an adjusting event (d) a prior period item.
**Ans: (b).** Not recognised as liability; disclosed only, provided when shareholders approve.

**D4.** A destruction of assets by earthquake occurring after the balance sheet date is normally:
(a) adjusting (b) non-adjusting, disclose if material (c) prior period item (d) contingent asset.
**Ans: (b).** New condition after year-end; disclose nature and financial effect if material.

**D5.** If an event after the balance sheet date indicates the entity is no longer a going concern, the correct action is:
(a) disclose only (b) ignore (c) recast the accounts on a non-going-concern basis (d) treat as contingent liability.
**Ans: (c).** Fundamental assumption change forces adjustment regardless of the post-date trigger.

**D6.** Sale of inventory after year-end below cost, due to conditions existing at year-end, is:
(a) non-adjusting (b) adjusting — write down to NRV (c) contingent (d) disclosure only.
**Ans: (b).** Confirms NRV < cost at year-end (AS 2 + AS 4).

**D7.** Which of the following is a **non-adjusting** event?
(a) Insolvency of a debtor confirming year-end doubt (b) A merger/acquisition announced after year-end (c) Fraud during the year detected later (d) Retrospective wage revision covering the year.
**Ans: (b).** A post-date announcement of a new transaction — disclose only.

**D8.** Case scenario: R Ltd (year ended 31 March 2026, approved 30 June 2026) receives, on 10 April 2026, evidence that inventory valued at ₹5,00,000 at year-end was already damaged (NRV ₹1,50,000) at 31 March 2026. Correct treatment:
(a) disclose ₹5,00,000 (b) write down by ₹3,50,000 (c) no action (d) provide ₹5,00,000.
**Ans: (b).** Adjusting event; carry at NRV ₹1,50,000, loss ₹3,50,000.

**D9.** After AS 29, the portion of AS 4 dealing with contingencies that survives relates to:
(a) measurement of provisions (b) contingent assets recognition (c) contingencies considered up to date of approval / events after B/S date (d) onerous contracts.
**Ans: (c).** Recognition/measurement of contingencies shifted to AS 29.

**D10.** Case scenario: S Ltd proposes dividend ₹10,00,000 on 5 May 2026 and, on 8 May 2026, a major customer (debtor ₹4,00,000, doubtful at year-end) is declared insolvent. Accounts approved 31 May 2026. Correct combined treatment:
(a) provide both (b) disclose both (c) provide ₹4,00,000 loss (adjusting); disclose dividend (non-adjusting) (d) ignore both.
**Ans: (c).** Insolvency is adjusting (provide ₹4,00,000); proposed dividend is non-adjusting (notes only).

**D11.** The estimate of financial effect of a non-adjusting event, if it cannot be made, should be:
(a) omitted (b) assumed nil (c) stated as a fact that it cannot be estimated (d) provided at a nominal ₹1.
**Ans: (c).** AS 4 requires disclosure of the fact that an estimate cannot be made.

**D12.** Which body's approval date is relevant for a company under AS 4?
(a) Statutory auditors (b) Board of Directors (c) Shareholders in AGM (d) Registrar.
**Ans: (b).** The Board (approving authority) approval date closes the AS 4 window.

---

### Examiner traps recap
- Watch **date the condition arose**, not the date information was received — that alone decides adjusting vs non-adjusting.
- **Proposed dividend = non-adjusting** (notes only) after the 2016 amendment; a very common trap still using the old "provide it" rule.
- **Going concern failure** always forces a recast even if the trigger is post-date.
- Retrospective agreements/settlements relating to the reporting period create **adjusting** obligations even if signed later — apportion pre- and post-year-end portions.
- For non-adjusting events, marks are earned for stating **both** nature **and** estimated financial effect (or that it cannot be estimated).
