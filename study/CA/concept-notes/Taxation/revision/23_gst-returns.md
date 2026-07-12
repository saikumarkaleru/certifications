# GST — Returns

> Secs 37–48 + Rules 59–68. Most amendment-prone area — verify all due dates, QRMP threshold, late-fee caps, interest rates and 3-year bars against ICAI material.

## Snapshot
Self-assessed tax needs periodic returns to (a) capture liability in a ledger, and (b) **weld each buyer's credit to a specific seller's declaration** (anti-fake-ITC engine). Pipeline: Seller **GSTR-1** → system → Buyer **GSTR-2B** (static, 14th) → Buyer **GSTR-3B** (claim + pay) → **GSTR-9** (annual truth-up). GSTR-2/3 (two-sided matching) were scrapped for one-directional auto-population. Sec 16(2)(aa) = credit gate.

## Core concepts
- Seller's outward statement = raw material of buyer's credit. Credit is **system-communicated**, not self-declared.
- Data flows **one way**; rules protect the pipeline's **direction** (16(2)(aa) blocks credit never entering) or **order** (sequential filing).
- No revised returns in GST — corrections only **prospectively** via amendment tables (protects data already fed to buyers).
- Two-speed: invoice-level for credit (GSTR-1), summary-level for cash (GSTR-3B).

## Key provisions / rules

### Section map
Sec 37 outward (GSTR-1); 38 communicated ITC (GSTR-2B); 39 returns (GSTR-3B); 40 first return; 44 annual (GSTR-9/9C); 45 final (GSTR-10); 46 defaulter notice (GSTR-3A); 47 late fee; 48 practitioners; 50 interest. **Sec 42/43/43A (old matching machinery) omitted.**

### GSTR-1 (Sec 37, Rule 59) — invoice-level outward
- **B2B** invoice-by-invoice always (feeds buyer's 2B). **B2C Large** (inter-State, unregistered, value > ₹2,50,000 — verify) invoice-wise. **B2C Small** consolidated rate-wise/State-wise. Exports/SEZ separate (refunds). Credit/debit notes; amendment tables; nil/exempt/non-GST.
- Due: **11th** monthly / **13th** quarterly (QRMP). **IFF** — optional, B2B only, first two months, by 13th.
- **Sequential (Sec 37(4))**: can't file if any previous GSTR-1 pending. **Time-bar (37(5))**: not after **3 years** from due date.
- **GSTR-1A**: optional same-period seller amendment before filing 3B (≠ old defunct buyer-side GSTR-1A).

### GSTR-2B (Sec 38, Rule 60) — auto-drafted, STATIC
- Generated **14th** from all suppliers' GSTR-1/IFF + GSTR-5/6 + ICEGATE imports. Frozen once generated.
| | GSTR-2A | GSTR-2B |
|---|---|---|
| Nature | **Dynamic** | **Static** (frozen 14th) |
| Basis for ITC | No | **Yes** (Sec 16(2)(aa)) |
| Late supplier invoice | retro to original period | period supplier **actually filed** |
- 2B flags eligible/ineligible (Sec 17(5) blocked stay blocked — presence necessary not sufficient).
- **Sec 16(2)(aa)** gate: ITC only if supplier furnished in GSTR-1 AND communicated (appears in 2B).
- Amended **Sec 38**: system can flag credit "restricted" (new/defaulting/risky suppliers) — gate tightening from "did supplier file" to "is supplier trustworthy".

### GSTR-3B (Sec 39, Rule 61) — summary + payment
- Output tax − eligible ITC (capped at 2B) = net payable → credit ledger then cash ledger.
- **Furnished only when tax actually paid** (submitting figures without payment ≠ filed).
- Due: **20th** monthly / **22nd or 24th** QRMP (State-staggered).
- **Sequential (Sec 39(10))**: can't file 3B unless same-period GSTR-1 filed; can't skip prior 3B. **Time-bar (39(11))**: 3 years.

### QRMP (turnover ≤ ₹5 crore preceding FY — verify)
- Quarterly **return**, monthly **payment** via **PMT-06**. **FSM**: 35% of last quarter's net cash (or 100% of last month if previously monthly) — **interest-free safe harbour** if paid on time AND quarterly 3B filed on time. **SAM**: actual liability. Nil month → no challan.
- Opt-in **GSTIN-wise**, **continuous**. Crossing ₹5cr mid-year → monthly from next quarter. IFF cap historically ₹50L/month (verify).

### Other returns
CMP-08 (composition pay, quarterly 18th); GSTR-4 (composition annual, 30 June); GSTR-5 (NR, 13th); GSTR-5A (OIDAR); GSTR-6 (ISD, 13th); **GSTR-7 (TDS, 10th)**; **GSTR-8 (TCS, 10th)**; GSTR-9/9C (annual, 31 Dec); GSTR-10 (final, within 3 months); GSTR-11 (UIN refund). First return (Sec 40) = first GSTR-1/3B covering pre-registration gap (not a separate form).

### GSTR-9/9C (Sec 44) — annual truth-up
- GSTR-9 optional ≤ ₹2 cr; GSTR-9C (**self-certified** recon vs audited accounts) above ~₹5 cr. Old mandatory CA/GST audit (Sec 35(5)) **omitted**. Composition → GSTR-9A (waived, verify). Additional liability → **DRC-03**; **cannot claim fresh ITC** via GSTR-9. Due 31 Dec; 3-year bar.

### Late fee (Sec 47) & interest (Sec 50)
- Late fee: **₹100 CGST + ₹100 SGST = ₹200/day** (nil return ₹10+₹10 = ₹20/day), turnover-slabbed cap. Per-day because harm grows with delay.
- Interest: **50(1) = 18%** on net **cash** tax (proviso, if return filed); **50(3) = 24%** on wrong ITC **availed AND utilised** (reversed-before-use = no interest). Both late fee and interest from **cash ledger only**.

### Default → stick
Non-filing → **GSTR-3A** notice (Sec 46, **15 days**) → **best-judgement assessment (Sec 62)** → **withdrawn if valid return filed within 30 days** (late fee + interest survive).

## Worked mini-example
Beta buys April: from Alpha (monthly, files GSTR-1 on 10 May) ₹1,80,000 IGST; from Gamma (QRMP, no IFF, files 13 July) ₹72,000 IGST.
- April GSTR-2B (generated 14 May): Alpha's ₹1,80,000 appears; Gamma's ₹72,000 does NOT.
- Sec 16(2)(aa): Beta's April ITC = **₹1,80,000** only. Gamma's ₹72,000 → claimable in **July** 2B (subject to Sec 16(4)).
- If Gamma used IFF by 13 May → both appear → April ITC = ₹2,52,000.

## Exam traps & must-remember
1. GSTR-2A (dynamic) ≠ GSTR-2B (static, basis for ITC).
2. Credit ledger pays tax only — interest/late fee/penalty from **cash**.
3. Interest 50(1) on **net cash**, not gross.
4. Sequential filing — GSTR-1 before 3B; no skipping prior periods.
5. QRMP = quarterly return, **monthly payment** (not deferred tax).
6. IFF optional, B2B only, first two months, by 13th.
7. Nil return still needs filing (blocks sequential filing).
8. 3-year filing bar (37(5)/39(11)/44) ≠ Sec 16(4) ITC time limit.
9. Late fee is CGST + SGST both = ₹200/day (candidates halve it).
10. First return (Sec 40) covers pre-registration gap; not a separate form.
11. Late-filed supplier invoice → buyer's **later** month 2B (static).
12. Sec 50(3) needs availed **AND utilised**; reversed before use = no interest.
13. GSTR-7 (TDS, govt on payments) vs GSTR-8 (TCS, ECO on platform supplies) — both 10th, both credit third party's **cash** ledger.
14. 9C now **self-certified**; old mandatory GST audit omitted.
15. Cannot claim missed ITC first time in GSTR-9.
16. GSTR-3B "furnished" only on payment.
17. QRMP opt-in GSTIN-wise and continuous.

## One-line recall
- Pipeline: GSTR-1 (11th) → GSTR-2B (static, 14th) → GSTR-3B (20th, claim+pay) → GSTR-9 (31 Dec).
- Sec 16(2)(aa): no ITC unless invoice in your GSTR-2B (seller filed GSTR-1).
- Sequential: GSTR-1 before 3B; no leapfrogging; 3-year bar; no revised returns (amend prospectively).
- QRMP ≤ ₹5cr: quarterly return, monthly PMT-06 (FSM 35% = interest-free safe harbour), optional IFF.
- Interest 18% net cash / 24% wrong ITC availed+utilised; late fee ₹200/day; credit ledger never pays these.
- Default → GSTR-3A (15 days) → Sec 62 best-judgement (withdrawn if filed within 30 days).
