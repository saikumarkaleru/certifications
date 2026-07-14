# Investigations, SAR/STR & Case Management

## What you'll be able to do

Take a system-generated AML alert (or a law-enforcement/internal referral), work it end-to-end into a documented investigation, decide whether it is a false positive or a genuine suspicion, and — if suspicious — **draft and file a Suspicious Transaction Report (STR) to FIU-IND** using the FINnet 2.0 portal with a defensible narrative. You'll manage the case inside a case-management system (CMS) with the right evidence, disposition codes, and SLAs, and you'll recognise the three typologies interviewers always test: **structuring, layering, and trade-based money laundering (TBML)**.

## The essentials

An **alert** is a machine hit (rule or model). It is *not* suspicion — it is a prompt to look. Investigation is the human process that converts alerts and referrals into a **reasoned disposition**: *close (no further action)*, *escalate/keep monitoring*, or *file an STR*.

India-specific mechanics you must know:

| Item | India (PMLA / FIU-IND) |
|---|---|
| Regulator/intelligence unit | **FIU-IND** (Financial Intelligence Unit – India), under Dept. of Revenue |
| Governing law | Prevention of Money Laundering Act, 2002 (PMLA) + PML (Maintenance of Records) Rules, 2005 |
| Report type for suspicion | **STR** (Suspicious Transaction Report) — the Indian equivalent of a SAR |
| Other prescribed reports | CTR (cash > ₹10 lakh/month aggregated), CCR (counterfeit currency), NTR (non-profit), CBWTR (cross-border wire ≥ ₹5 lakh) |
| Filing timeline | STR **within 7 working days** of a Principal Officer forming suspicion |
| Portal | **FINnet 2.0** (replaced FINGate); XML/structured upload |
| "No threshold" rule | STR has **no minimum amount** — an attempted transaction that never completes is still reportable |
| Tipping-off | Prohibited — you must **not** tell the customer an STR was filed |
| Record retention | 5 years from transaction / end of relationship |

"SAR" is the US/UK term (filed to FinCEN / the NCA). The user's roles are India-first, so the deliverable is an **STR**, but interviewers use "SAR" and "STR" interchangeably — know both.

The three exam-critical typologies:

- **Structuring (smurfing):** breaking one large transaction into many small ones to dodge a reporting threshold — e.g. nine cash deposits of ₹95,000 to stay under the ₹10 lakh CTR aggregate and the ₹50,000 PAN/ID trigger.
- **Layering:** the middle stage of laundering — moving placed funds through many accounts, entities, jurisdictions and instruments to break the audit trail.
- **Trade-based ML (TBML):** moving value through trade by **mis-invoicing** — over/under-invoicing, over/under-shipment, multiple invoicing of the same goods, or phantom shipments.

## Hands-on — step by step

**Worked example.** Alert fires on *Ravi Textiles Pvt Ltd*, a current account at a Mumbai branch. Rule: "structuring — multiple sub-threshold cash deposits." Period under review: 1–30 Jun 2026.

**Step 1 — Triage and scope.** Read the alert. Note the rule logic, the trigger amount, the account, and the look-back window. Set your review period a little wider than the alert (say 90 days) to see pattern vs. one-off.

**Step 2 — Pull the evidence.** Assemble in the CMS:
- KYC/CDD file: incorporation docs, PAN, GST registration, declared business (readymade garments), declared turnover (~₹3 cr/yr), expected cash intensity.
- Transaction dump for Mar–Jun 2026.
- Prior alerts/STRs on this customer or connected parties.
- Adverse-media / sanctions / PEP screening refresh.

**Step 3 — Analyse the transactions.** In the dump you find, in June alone:

| Date | Type | Amount (₹) |
|---|---|---|
| 03 Jun | Cash deposit | 49,000 |
| 05 Jun | Cash deposit | 48,500 |
| 09 Jun | Cash deposit | 49,500 |
| 14 Jun | Cash deposit | 48,000 |
| 19 Jun | Cash deposit | 49,000 |
| 24 Jun | Cash deposit | 48,500 |
| 26 Jun | Outward RTGS to *Gemstar FZE, Dubai* | 2,80,000 |

Six cash deposits totalling **₹2,92,500**, each just under the ₹50,000 ID/PAN trigger, followed by a near-full sweep out to a UAE entity. Two red flags stacked: **structuring** on the way in, and a **cross-border wire to a free-zone entity** with no trade documents on file — a classic **layering + potential TBML** hop.

**Step 4 — Compare to expected behaviour.** A garment wholesaler *would* see cash, but you'd expect it deposited in normal lots and paired with supplier payments inside India, GST-matched sales, and inventory. Here the cash is engineered under thresholds and immediately exported to a related-looking overseas party with **no invoice, no bill of lading, no LC**. Behaviour is inconsistent with the declared profile.

**Step 5 — Resolve open questions (RFI).** Raise a documented Request-For-Information to the relationship manager: source of cash, purpose of the Dubai remittance, supporting trade docs. Suppose the RM returns vague answers and no documents. That *strengthens* suspicion.

**Step 6 — Decide.** Reasonable grounds to suspect that funds may represent proceeds of crime / value being moved abroad. Disposition = **File STR**. (Had the RM produced genuine invoices and the deposits matched daily till takings, disposition would be **false positive — close with rationale**.)

**Step 7 — Draft the narrative.** Use the **5W + 1H** discipline and the **who/what/when/where/why-suspicious/what-next** skeleton (see output).

**Step 8 — File on FINnet 2.0.** Principal Officer reviews, approves, and uploads the STR in the prescribed XML schema through the FINnet 2.0 portal within **7 working days** of forming suspicion. Log the acknowledgement number in the CMS.

**Step 9 — Close the case.** Record disposition, attach the filed STR and ack, apply post-filing action (enhanced monitoring / exit review), and set a review tickler. **Do not tip off the customer.**

## The output

**STR narrative (the finished artefact):**

> **Subject:** Ravi Textiles Pvt Ltd — Current A/c 0091xxxx1234, Mumbai (Andheri) branch. Director: Mr R. K. Sharma (PAN ABCDE1234F).
>
> **Reason for report / typology:** Structuring of cash deposits followed by an unsupported cross-border remittance — suspected layering / trade-based money laundering.
>
> **Activity (What/When/Where):** Between 03 Jun and 24 Jun 2026, six cash deposits of ₹48,000–₹49,500 (aggregate ₹2,92,500) were made into the account, each individually below the ₹50,000 identity-capture threshold. On 26 Jun 2026, ₹2,80,000 (95.7% of deposits) was remitted by RTGS/SWIFT to Gemstar FZE, a UAE free-zone entity, with **no invoice, shipping or LC documentation** on file.
>
> **Why suspicious:** The deposit pattern is consistent with deliberate structuring to avoid ID/reporting thresholds. The value is not consumed in the declared domestic garment trade but swept overseas to an entity for which no trade nexus is evidenced. On RFI, the customer provided no source-of-funds or purpose documentation. The behaviour is inconsistent with the KYC-declared profile (domestic wholesale, ~₹3 cr turnover).
>
> **Amount involved:** ₹2,92,500 in / ₹2,80,000 out. **Period:** 03–26 Jun 2026.
>
> **Action taken:** STR filed to FIU-IND via FINnet 2.0 (Ack. FINnetXXXXXXXX). Account placed under enhanced monitoring; exit review initiated. No disclosure made to the customer.

## Checks, gotchas & red flags

- **Alert ≠ suspicion.** Never file "just because it alerted," and never close without a written rationale — your disposition must survive a regulator's file review.
- **STR has no threshold** and covers **attempted** transactions. A remittance the bank *declined* is still reportable.
- **7 working days** runs from when the Principal Officer forms suspicion, not from the transaction date — don't let cases age in the queue.
- **Tipping-off is an offence.** Keep STR existence out of any customer-facing note or RFI wording.
- **Narrative must stand alone** — a reader with no access to your screens must understand who, what, how much, and why suspicious. Vague ("transactions looked odd") gets rejected in QA.
- **Tie-outs:** amounts in the narrative must equal the transaction schedule; the subject's ID must match KYC; the typology label must match the facts.
- Watch **round-tripping** and **connected parties** — investigate the counterparty, not just your customer.

## Interview drill

**Q1. Walk me from alert to STR.** "Triage and scope the alert; pull KYC and a wider transaction history; analyse behaviour against the customer's expected profile; raise an RFI to close gaps; reach a documented disposition. If suspicion is reasonable, I draft a stand-alone 5W narrative, the Principal Officer approves, and we file to FIU-IND on FINnet 2.0 within 7 working days — no tipping-off, then enhanced monitoring."

**Q2. Difference between structuring and layering?** "Structuring is *placement-stage* — deliberately breaking transactions below reporting/ID thresholds. Layering is the *next stage* — moving already-placed funds through multiple accounts, entities and jurisdictions to obscure the trail. My worked case had both: sub-₹50,000 cash deposits (structuring) swept to a UAE entity with no trade docs (layering, possibly TBML)."

**Q3. What makes a good SAR/STR narrative?** "It answers who, what, when, where, how much, and *why it's suspicious*, plus action taken — and it reads coherently without any attachments. Facts and figures tie to the transaction schedule, the typology is named, and speculation is avoided. Regulators judge the file on the narrative."

## Learn/practise (free)

- **FIU-IND website** — read the PMLA, PML Rules, and the STR/CTR reporting-format guides; the FINnet 2.0 user manuals are public.
- **FATF typologies reports** and **Egmont Group** case studies — free, and the source of most interview scenarios.
- **Wolfsberg Group** FAQs and the **ACAMS** free resource library / webinars for narrative-writing templates.
- **Practise without a live CMS:** take any anonymised bank-statement CSV, invent a red-flag pattern in Excel, and write the full STR narrative to the skeleton above. Rehearse the 7-day-clock and no-tipping-off rules until they're reflexive.
