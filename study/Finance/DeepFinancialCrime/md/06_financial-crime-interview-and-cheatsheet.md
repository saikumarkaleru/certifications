# Financial-Crime Interview Drills + ACAMS & Cheat-Sheet

## What you'll be able to do

Walk into an AML/financial-crime interview (analyst, GCC KYC/transaction-monitoring, compliance, treasury-facing) and answer the questions that actually get asked — CDD vs EDD, red-flag case reasoning, why an alert is a false positive, the SAR/STR lifecycle — with crisp, structured answers. You'll also know the **ACAMS/CAMS** certification pathway and its India relevance, and you'll have a one-page cheat-sheet of terms, lists, tools and the SAR process to revise the night before.

## The essentials — the ACAMS/CAMS pathway

**ACAMS** (Association of Certified Anti-Money Laundering Specialists) runs **CAMS** — the most widely-requested AML credential in GCC and Indian bank job posts.

| Item | Detail (mid-2026) |
|---|---|
| Flagship cert | **CAMS** (Certified Anti-Money Laundering Specialist) |
| Eligibility | Points system: education + AML/related work experience (~40 qualifying credits) |
| Exam | ~120 multiple-choice, 3.5 hrs, computer-based (Pearson VUE) or online-proctored |
| Cost | ~USD 1,000–1,700 (member vs non-member bundle); ACAMS membership ~USD 300/yr |
| Renewal | Recertify every 3 years via CAMS credits (CPE) |
| Other ACAMS certs | **CGSS** (sanctions), **CKYCA** (KYC), **CTMA** (transaction monitoring), **CCAS** (crypto) |
| India-relevant alternatives | **IIBF** AML/KYC certificate (cheap, bank-recognised), NISM, ICA (UK) diplomas |

**Positioning tip for the user:** with MBA-Finance + NISM RA + trading-desk experience, **CKYCA or CTMA** are faster, cheaper wins that map directly to GCC KYC/monitoring roles; **CAMS** is the resume centrepiece to target once you have AML work credits. Mention IIBF as the low-cost India-domestic signal.

## Hands-on — interview drills with model answers

**Drill 1 — "Explain CDD vs EDD."**
> "CDD — Customer Due Diligence — is the baseline every customer gets: verify identity with reliable documents, identify the beneficial owner, understand the nature and purpose of the relationship, and monitor ongoing. **EDD — Enhanced Due Diligence — is CDD-plus for higher-risk customers**: PEPs, high-risk jurisdictions, correspondent banking, complex ownership, or cash-intensive businesses. EDD adds source-of-funds and source-of-wealth verification, senior-management sign-off, and more frequent review. The opposite end is **SDD (simplified)** for low-risk, e.g. a salaried resident with a small savings account. It's a **risk-based approach** — you spend diligence where the risk is."

**Drill 2 — "Give me a red-flag case and how you'd handle it."**
> "A garment wholesaler makes six cash deposits of ~₹49,000 each in a month — all just under the ₹50,000 ID trigger — then sweeps 95% out to a UAE free-zone entity with no invoice or shipping docs. Red flags: **structuring** on the way in, an **unsupported cross-border wire**, and behaviour inconsistent with the declared profile — signs of layering, possibly trade-based ML. I'd pull KYC and 90 days of history, compare to expected activity, raise an RFI for source-of-funds and trade docs, and if unresolved, escalate to the Principal Officer to file an STR to FIU-IND within 7 working days — no tipping-off, then enhanced monitoring."

**Drill 3 — "Why might an alert be a false positive?"**
> "Because rule-based monitoring is deliberately over-sensitive — it flags patterns, not intent. A large round-number transfer might be a genuine property purchase; repeated same-amount payments might be a legitimate EMI or salary; a 'new counterparty' alert might just be a customer paying a new but legitimate vendor. It's a false positive when, after review, the activity is **consistent with the customer's KYC profile and supported by documentation** — a salaried customer's ₹5 lakh transfer matched to a home-loan disbursement, say. I'd still document the rationale and close it; and if I see the same benign pattern flooding the queue, I'd recommend **tuning the rule threshold** so analysts spend time on real risk. Typical AML false-positive rates run 90%+, which is exactly why disposition quality and tuning matter."

**Drill 4 — "What's the difference between an STR and a CTR?"**
> "A **CTR** is threshold-driven and objective — in India, cash transactions aggregating over ₹10 lakh in a month get reported automatically, no suspicion needed. An **STR** is suspicion-driven — any amount, including attempted transactions, when there are reasonable grounds to suspect proceeds of crime. CTR is a filter; STR is a judgement."

**Drill 5 — "Walk me through the three stages of money laundering."**
> "**Placement** — getting dirty cash into the system (structured deposits, casinos, cash-heavy fronts). **Layering** — moving it through many accounts, entities and jurisdictions to break the trail. **Integration** — bringing it back as apparently clean wealth (property, luxury goods, business investment). Detection is easiest at placement, hardest at integration."

## The output — one-page cheat-sheet

**Acronyms**
- AML / CFT — Anti-Money Laundering / Countering Financing of Terrorism
- KYC / CDD / EDD / SDD — Know Your Customer / Customer, Enhanced, Simplified Due Diligence
- UBO — Ultimate Beneficial Owner (usually ≥10% or ≥25% ownership/control)
- PEP — Politically Exposed Person
- STR / SAR — Suspicious Transaction / Activity Report
- CTR / CCR / NTR / CBWTR — Cash / Counterfeit-currency / Non-profit / Cross-Border-Wire Transaction Report
- TBML — Trade-Based Money Laundering
- RBA — Risk-Based Approach

**Key India facts**
- Law: **PMLA 2002** + PML (Maintenance of Records) Rules 2005
- Intelligence unit: **FIU-IND**; portal: **FINnet 2.0**; regulator (banks): **RBI Master Direction on KYC**
- STR: **any amount, file within 7 working days** of forming suspicion
- CTR: cash **> ₹10 lakh/month** aggregated; ID/PAN trigger commonly at **₹50,000**
- Record retention: **5 years**; **tipping-off prohibited**

**Global bodies & lists**
- **FATF** — 40 Recommendations, grey/black lists; **Egmont Group** — FIU network
- **Wolfsberg Group** — industry standards; **OFAC** (US), **UN**, **EU**, **UK HMT/OFSI**, **MHA/UAPA** (India) — sanctions lists

**The three typologies:** Structuring · Layering · TBML (mis-invoicing / over-under shipment / phantom shipment)

**SAR/STR process (memorise):**
1. Alert / referral → **triage & scope**
2. Gather **KYC + transaction history + screening**
3. **Analyse** vs expected profile → raise **RFI**
4. **Disposition:** close (false positive, with rationale) OR escalate
5. If suspicious → draft **5W narrative** → Principal Officer approval
6. **File to FIU-IND on FINnet 2.0** (≤7 working days)
7. **No tipping-off** → enhanced monitoring / exit → record & retain 5 yrs

**Tools you may be asked about:** Actimize (NICE), SAS AML, Oracle Mantas/FCCM, Verafin, Napier, ComplyAdvantage, Refinitiv World-Check / LSEG, Dow Jones RiskCenter (screening); ServiceNow / bespoke CMS for case management.

## Checks, gotchas & red flags

- Don't confuse **STR (suspicion, any amount)** with **CTR (threshold, automatic)** — the single most common slip.
- **EDD is not "more documents for everyone"** — it's triggered by risk; say "risk-based approach" and you signal maturity.
- Naming **tipping-off** and the **7-working-day** clock unprompted marks you as India-fluent.
- For false positives, always add the **tuning** point — interviewers want to hear you improve the system, not just clear the queue.
- Don't overclaim CAMS if you haven't sat it — say "targeting CAMS; CKYCA/IIBF in progress."

## Interview drill

**Q1. Which AML cert should someone with your background pursue and why?** "CAMS is the market standard for GCC and Indian bank compliance roles, but it needs qualifying AML credits. Given my finance and monitoring exposure, I'd start with ACAMS **CKYCA/CTMA** or the low-cost **IIBF KYC/AML** certificate for immediate India signal, then target **CAMS** as I accumulate AML work experience for recertifiable, globally-recognised weight."

**Q2. A PEP wants to open an account — what happens?** "PEPs are inherently higher-risk, so **mandatory EDD**: verify identity and beneficial ownership, establish **source of funds and source of wealth**, screen against sanctions and adverse media, obtain **senior-management approval** to onboard, and set enhanced ongoing monitoring with more frequent review. Being a PEP isn't a reason to refuse — it's a reason to look harder."

**Q3. How would you reduce a flood of false positives without missing real risk?** "Measure it first — bucket alerts by rule and disposition. Where a rule generates high volume and near-zero true positives, **tune the threshold or add segmentation** (e.g. different limits for cash-intensive vs salaried customers), pilot the change on historical data to confirm no known STRs would have been missed, document it, and get model-governance sign-off. The goal is fewer alerts, same detection."

## Learn/practise (free)

- **ACAMS free resources** — Today's AML news, webinars, sample CAMS questions; the **CAMS study guide** table of contents shows the exam scope even before you buy.
- **FATF** 40 Recommendations and typologies reports; **Wolfsberg** FAQs — free and authoritative.
- **FIU-IND** and **RBI KYC Master Direction** — read the actual Indian rules once, end to end.
- **IIBF** AML/KYC exam syllabus — cheap, India-recognised, good structured revision.
- **Rehearse out loud:** record yourself answering each drill above in under 90 seconds, structured (definition → example → what you'd do). Build a personal deck of 10 red-flag scenarios and practise reaching a disposition and narrative for each.
