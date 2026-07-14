# R2R Interview Drills + T-Code & Close Cheat-Sheet

## What you'll be able to do

After this chapter you can sit a real R2R / month-end-close interview and answer the standard rounds without hesitation: **"walk me through month-end," journal-entry and reconciliation questions, GR/IR, accruals vs provisions, a SAP T-code quiz, SOX questions, and a case ("how would you clear an aged open item")**. You'll also have a **one-page cheat-sheet** — key FICO T-codes, the WD close sequence, recon types, SOX terms — to revise the night before. These are the exact question shapes used across Genpact, Accenture, HP, Dentsu and Cromwell R2R panels.

## The drill — step by step (Q&A)

**Q1 — "Walk me through month-end close."**
> "I work a WD calendar. Pre-close I confirm cut-off and sub-ledgers are ready. WD1: AP/AR sub-ledgers close, I raise accruals and run FX revaluation (FAGL_FC_VAL). WD2: intercompany postings and matching, depreciation run (AFAB), payroll JE. WD3: GL close — recurring, allocation and reclass journals. WD4: reconciliations and BS flux/review, clearing aged items. WD5: management reporting / BPC submission, controller sign-off, then I lock the ledger (OB52). Throughout I'm hitting SLAs — on-time close, accuracy, aging."

**Q2 — "Accruals vs provisions — difference?"**
> "An **accrual** is a known expense incurred but not yet invoiced — timing certain, amount fairly certain (e.g. July electricity used, bill comes August). A **provision** is a liability of uncertain timing or amount recognised because a present obligation is probable and estimable (e.g. warranty, bad-debt/ECL, restructuring — IAS 37). Both increase expense and a liability, but a provision carries genuine estimation uncertainty; an accrual is mostly a timing bridge. Both reverse — the accrual on invoice receipt, the provision on utilisation or reassessment."

**Q3 — "What is GR/IR and how do you clear it?"**
> "GR/IR (Goods Receipt / Invoice Receipt) is a clearing account in the P2P–GL bridge. On goods receipt: **Dr Inventory/Expense, Cr GR/IR**. On invoice receipt: **Dr GR/IR, Cr Vendor**. When both match, GR/IR nets to zero. A non-zero balance means a mismatch — goods received not invoiced, or invoiced not received, or a quantity/price gap. I analyse it with **MB5S** or **FBL3N**, chase the missing side, and clear via **F.13** (auto-clearing) or **MR11** for genuine GR/IR maintenance write-offs."

**Q4 — Journal-entry quiz. "Book a ₹1,20,000 annual insurance paid 1-Jul, and the July expense."**
> "On payment: **Dr Prepaid Insurance 1,20,000 / Cr Bank 1,20,000**. Monthly amortisation: **Dr Insurance Expense 10,000 / Cr Prepaid Insurance 10,000** (1,20,000 ÷ 12). By June next year prepaid is nil and full expense is recognised."

**Q5 — SAP T-code quiz (rapid fire).**
> FB50 — GL document entry; F-02 — general posting; FB03 — display document; FBL3N — GL line items; FS10N — GL balances; FAGL_FC_VAL — foreign currency valuation; AFAB — depreciation run; F.13 — automatic clearing; OB52 — open/close posting periods; F-04 — post with clearing; FBL1N/FBL5N — vendor/customer line items; MIRO — invoice receipt; FBRA — reset cleared items.

**Q6 — SOX question. "What makes a good management-review control?"**
> "It must be performed with **precision** and **evidenced**: an independent reviewer (not the preparer — segregation of duties), documented review notes/challenge, dated after the close, tied to a control in the RCM, with the underlying support attached. Signing a recon without evidence of what you checked is a deficiency. Deficiencies escalate to significant deficiency and material weakness by magnitude and likelihood."

**Q7 — Case. "There's a ₹1,20,000 unidentified bank credit open for 95 days. Clear it."**
> "First, investigate — pull the bank line (FBL3N/FF67) and the statement narration; check if it's a customer receipt not applied, a duplicate, a wrong-account posting, or a genuine unknown. I'd match it against open AR (FBL5N) by amount/date and contact the customer/treasury. If it's an unapplied customer receipt, apply it (F-28/F-04). If a mis-post, reclass with a corrected JE. If truly unidentifiable after reasonable effort and below policy threshold, I'd propose a write-off with controller approval and documentation. Then I'd log the root cause — a 95-day aged item usually signals a broken applied-cash process, so I'd fix upstream, not just this line."

**Q8 — "Difference between reconciliation and flux?"**
> "A **reconciliation** proves a GL balance is *supported* — GL vs sub-ledger/bank/schedule, with reconciling items explained. **Flux** explains the *movement* period-over-period. Recon = 'is this balance real and backed?'; flux = 'why did it change?'. Both are month-end controls; recon is completeness/accuracy, flux is analytical review."

## The output — one-page cheat-sheet

**Key FICO T-codes**

| T-code | Use |
|---|---|
| FB50 / F-02 | GL journal entry |
| FB03 | Display document |
| FBL1N / FBL5N / FBL3N | Vendor / Customer / GL line items |
| FS10N | GL account balances |
| FAGL_FC_VAL | Foreign currency revaluation |
| AFAB | Depreciation run |
| F.13 | Automatic clearing |
| F-04 / F-28 | Post with clearing / incoming payment |
| FBRA | Reset cleared items |
| OB52 | Open/close posting periods |
| MIRO / MR11 | Invoice receipt / GR-IR clearing |
| F.01 / S_ALR_87012284 | Financial statement / BS report |

**WD close sequence**

| WD | Task |
|---|---|
| WD1 | Sub-ledger close, accruals, FX reval |
| WD2 | Intercompany, depreciation, payroll |
| WD3 | GL close, allocations, reclasses |
| WD4 | Reconciliations, BS flux/review |
| WD5 | Reporting / BPC submission, sign-off, lock |

**Recon types:** bank; sub-ledger-to-GL (AP/AR); balance-sheet schedule (accruals, prepaids, provisions, fixed assets); intercompany; suspense/clearing (GR/IR). Categories: *auto-certified* (system-matched) vs *manual*; risk-rated high/medium/low.

**SOX terms:** RCM (Risk & Control Matrix); preventive vs detective control; management-review control; segregation of duties; preparer/reviewer sign-off; control evidence; deficiency → significant deficiency → material weakness; J-SOX (Japan), SOX 404.

**Accruals vs provisions:** accrual = timing (incurred, not invoiced); provision = uncertain timing/amount (IAS 37, probable + estimable).

## Checks & gotchas

- **Don't recite T-codes without the journal logic** — panels probe "what does F.13 actually clear?" Know the postings behind the code.
- **GR/IR direction** trips people: goods first credits GR/IR, invoice debits it — get the Dr/Cr the right way round.
- **Never say "I'd just write it off"** on the aged-item case — investigate first, write-off is last with approval.
- **Segregation of duties** is the SOX answer graders wait for — say it explicitly.
- **Reversal:** every accrual/provision answer should mention *when it reverses* — omitting it reads as shaky.

## Interview drill (meta)

**Q: What's the single most common R2R interview opener and how long should your answer be?**
A: "Walk me through month-end close." Keep it 60–90 seconds, structured by WD, and name the controls (recon, flux, sign-off, lock) and one or two T-codes — enough to show you've done it without narrating every keystroke.

**Q: How do you show seniority beyond just doing tasks?**
A: Tie your work to metrics and improvement — "close 100% on-time, aging nil >90 days, rework 1.2%, and I automated the bank-recon download saving 8 hours a month." That shifts you from processor to owner.

## Practise free

- **Flashcard the T-code table** (Anki) — cover the "Use" column and recall the code, then reverse it.
- **Mock the "walk me through close"** out loud on a 90-second timer until it's smooth; record yourself.
- **JE drills:** invent 10 scenarios (prepaid, accrual, provision, FX gain, depreciation, GR/IR clearing) and write the double entry cold; check against a free ICAI/accounting-basics reference.
- **SAP T-codes without SAP:** the public **SAP Help Portal** and **SAP Learning Hub free tier** describe every T-code's screen and fields; read the FBL3N and F.13 pages so you can talk them convincingly.
- **Pull real interview questions** from Genpact/Accenture threads on Glassdoor/AmbitionBox (free) and answer each in writing, then out loud — the aged-item case and accruals-vs-provisions come up almost every time.
