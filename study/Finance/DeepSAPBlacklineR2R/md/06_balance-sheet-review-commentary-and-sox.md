# Balance-Sheet Review, Commentary (BS Calls) & SOX Evidence

## What you'll be able to do

After this chapter you can run a **flux (variance) analysis** on a balance sheet and P&L, write the **commentary** that gets read aloud on a monthly "BS review call", triage and clean up **aged reconciling items**, and justify **provisions/accruals** with real drivers. You'll also be able to speak **SOX / J-SOX** fluently: what a **RCM (Risk & Control Matrix)** is, what counts as **control evidence**, how **preparer/reviewer sign-off** works, and what a **control deficiency** is. This maps directly onto the Dentsu (J-SOX) and HP (SOX) R2R JDs, both of which list "balance-sheet reviews, flux commentary, SOX control evidence" as core duties.

## The drill — step by step

**Step 1 — Pull the two-period balances.** For each BS account, get current-month closing and prior-month (and often prior-year and budget) balances. In SAP that's **FS10N** (GL balance display) or **FBL3N** (line items); export to Excel.

**Step 2 — Compute the flux.** Add columns: **₹ change** and **% change**. Apply a **materiality threshold** — a common rule is *explain any movement > ₹5,00,000 AND > 10%* (dual threshold so you don't chase tiny-base swings). Flag every breach.

Worked example — Accrued Expenses:

| Account | Jun-26 | Jul-26 | Δ ₹ | Δ % | Explain? |
|---|---|---|---|---|---|
| Accrued marketing spend | 42,00,000 | 68,00,000 | +26,00,000 | +62% | Yes |
| Prepaid insurance | 9,00,000 | 8,25,000 | −75,000 | −8% | No |
| IC receivable – GB01 | 8,00,000 | 8,00,000 | 0 | 0% | No |

**Step 3 — Find the driver, not the number.** Don't write "accruals went up ₹26L." Open **FBL3N**, sort by posting date, and identify *what* posted: e.g. a Q3 brand-campaign accrual of ₹28L raised, partly offset by ₹2L of June accruals reversing. Now you have a *reason*.

**Step 4 — Test the account against its reconciliation.** Tie the GL balance to the supporting recon (from the Blackline chapter). Check the **aging** of open reconciling items:

| Item | Amount ₹ | Age (days) | Status | Action |
|---|---|---|---|---|
| Unidentified bank credit | 1,20,000 | 95 | Aged >90d | Escalate, likely customer receipt to apply |
| GR/IR mismatch PO 45001 | 3,40,000 | 22 | Open | Chase goods receipt |
| Duplicate accrual | 60,000 | 130 | Aged | **Write off — reverse** |

Aged items (>90 days) are a red flag on BS calls; the drill is *clean them up*, not just report them.

**Step 5 — Justify provisions & accruals.** For each, state (a) the driver, (b) the calculation basis, (c) evidence. Example — bad-debt provision: "ECL model, 5% on >180-day receivables = ₹12,00,000; supported by the aged debtors report dated 31-Jul-26." A provision without a documented basis fails both the BS review and SOX.

**Step 6 — Write the commentary.** One tight paragraph per flagged account: *what moved, by how much, why, and whether it's expected/one-off/reversing.* This is what you read on the call.

**Step 7 — SOX evidence for the control.** The BS review *is itself a SOX control* ("Management review of balance-sheet reconciliations, monthly"). To evidence it:
- **Preparer** signs/dates the recon and flux.
- **Reviewer** (independent, more senior) signs/dates, with review notes.
- Attach the source reports (FBL3N export, aging, bank statement) as evidence.
- Map the control to the **RCM**: risk → control → frequency → owner → evidence.

## The output

A sample BS-call commentary (what actually gets circulated):

> **Account: Accrued Expenses (2100100) — Jul-26**
> Balance ₹68,00,000, up ₹26,00,000 (+62%) MoM. **Driver:** ₹28,00,000 accrual raised for the Q3 brand campaign (IO #4471, media plan approved 5-Jul), partly offset by ₹2,00,000 June accruals reversing on invoice receipt. Movement is **expected and one-off**; accrual will reverse on vendor invoicing in Aug–Sep. **Recon:** tied to accrual schedule v3, no unexplained items. **Aged items:** one duplicate accrual of ₹60,000 (130 days) identified — reversing this period. Prepared: A. Rao 4-Aug; Reviewed: S. Mehta 5-Aug.

A slice of the **RCM (Risk & Control Matrix):**

| Risk | Control | Type | Freq | Owner | Evidence |
|---|---|---|---|---|---|
| BS balances misstated | Monthly recon prepared & independently reviewed | Detective | Monthly | R2R Lead | Signed recon + flux |
| Unauthorised journals | JE approval workflow before posting | Preventive | Per JE | GL Accountant | FB03 + approval log |
| Aged items not cleared | >90-day items escalated to controller | Detective | Monthly | Controller | Aging report + email |

## Checks & gotchas

- **Flux without a driver is worthless** — "up 62%" is not commentary; the *why* is.
- **Dual threshold** matters: a ₹4,000 account can swing 300% and mean nothing; a ₹2cr account can move 3% and be huge.
- **Sign-off dates must be after the close date and preparer ≠ reviewer** — same person on both is an instant SOX deficiency (segregation of duties).
- **Evidence must be dated and version-controlled**; "I reviewed it" verbally is not evidence.
- **Aged items you keep re-explaining** each month is the tell that clean-up isn't happening — auditors notice repeats.
- **Provisions must have a policy basis**; a round-number "management estimate" with no calc is a finding.

## Interview drill

**Q: What is flux analysis and how do you decide what to explain?**
A: Flux (fluctuation/variance) analysis compares each account's current balance to a baseline — prior month, prior year, or budget — and explains material movements. I apply a dual threshold, e.g. > ₹5L and > 10%, so I focus on genuinely significant swings rather than small-base noise. For each flagged item I go to the line-item detail (FBL3N) to find the actual driver — a specific accrual, reclass, or timing — and state whether it's expected, one-off, or reversing.

**Q: What's a control deficiency, and give an example from R2R.**
A: A deficiency is a control that isn't designed or operating well enough to prevent or detect a material misstatement on a timely basis. Example: a BS reconciliation signed by the same person as preparer and reviewer — that's a segregation-of-duties failure. It escalates from a deficiency to a *significant deficiency* to a *material weakness* depending on the magnitude and likelihood of misstatement it could allow.

**Q: How do you evidence a management-review control for SOX?**
A: The reviewer must show what they actually did, not just that they signed. So: the recon and flux with preparer name/date, an independent reviewer name/date, documented review notes or challenge, and the underlying support (GL export, aging, bank statement) attached. The key SOX expectation is "review with precision" — evidence of the questions asked and items followed up, tied to the RCM control description and frequency.

## Practise free

- **Build a flux workbook** from any public company's two consecutive balance sheets (annual report PDFs are free): add Δ₹ and Δ% columns, set a threshold with conditional formatting, and write one commentary paragraph per flagged line — force yourself to hypothesise the *driver* from the notes.
- **Aging drill:** make a fake open-items list with random dates, use `=TODAY()-postingdate` to age them into 0-30/31-60/61-90/>90 buckets with `IF`, and decide an action per bucket.
- **RCM practice:** download the free **COSO 2013 framework** summary and **PCAOB AS 2201** overview; for one process (say, accruals) write 3 risks, 3 controls, and the evidence each would produce. For J-SOX specifics, the Japanese FSA's internal-control standard summaries are public.
- Rehearse the **BS call** out loud: read your commentary in 60 seconds per account as if a controller is challenging you — that's the real test.
