# The AML Framework & Regulation: FATF, PMLA, RBI KYC Direction, 3 Lines of Defence

## What you'll be able to do

Explain, from memory, how the global-to-India AML rulebook stacks up — FATF → PMLA → RBI Master Direction — and translate that into an operating model: who does KYC, who owns the risk, who files the STR, and who the regulator holds personally accountable. You'll be able to draw the compliance org chart, name the statutory roles (Principal Officer, Designated Director, MLRO), state the exact reporting timelines to FIU-IND, and answer "walk me through your AML framework" in an interview without reaching for notes. This is the map every AML/GCC compliance analyst is assumed to carry.

## The essentials

**The money-laundering cycle — three stages:**

| Stage | What happens | Typical India example |
|---|---|---|
| Placement | Dirty cash enters the financial system | Structured cash deposits below ₹50,000 to dodge PAN; buying pre-paid instruments |
| Layering | Transactions obscure the trail | Shell-company invoicing, round-tripping via Mauritius/Dubai, rapid fund movement across accounts |
| Integration | "Clean" money re-enters as legitimate wealth | Real-estate purchase, share buy-backs, loans to self |

**FATF** — the Financial Action Task Force (Paris, inter-governmental). It sets **40 Recommendations** (the global AML/CFT/CPF standard, last major revision incorporating virtual assets and beneficial ownership). It does **not** regulate you directly; it evaluates countries via **Mutual Evaluations** and maintains the **grey list** (increased monitoring) and **black list** (Iran, DPRK, Myanmar as of 2026). India underwent its Mutual Evaluation and is a full FATF member; the 2024 assessment placed India in **regular follow-up** — the top-tier outcome. Key Recommendations to know: R.10 (CDD), R.12 (PEPs), R.16 (wire transfers / "travel rule"), R.20 (STR reporting), R.24/25 (beneficial ownership of legal persons/arrangements).

**PMLA 2002** — the Prevention of Money Laundering Act is India's primary statute. Section 3 defines the offence; Section 4 sets punishment (rigorous imprisonment 3–7 years, up to 10 for scheduled offences). **Section 12** is the operative compliance obligation: every "reporting entity" (banks, NBFCs, brokers, insurers, payment operators, crypto/VDA providers) must **maintain records, verify identity, identify beneficial owners, and furnish information to FIU-IND**. The **Enforcement Directorate (ED)** investigates and attaches proceeds of crime; **FIU-IND** (Financial Intelligence Unit) receives reports.

**Reports to FIU-IND (via the FINnet 2.0 gateway):**

| Report | Trigger | Timeline |
|---|---|---|
| CTR | Cash transactions > ₹10 lakh (or series integrally connected in a month) | 15th of following month |
| STR | Suspicion of ML/TF — **no threshold** | Within 7 working days of establishing suspicion |
| CCR | Counterfeit currency | 15th of following month |
| NTR | Non-profit org receipts > ₹10 lakh | 15th of following month |
| CBWTR | Cross-border wire transfers > ₹5 lakh | 15th of following month |

**RBI Master Direction – KYC (2016, as amended through 2025)** operationalises PMLA for RBI-regulated entities. It mandates a Board-approved **KYC policy** with four pillars: Customer Acceptance Policy, Risk Management, Customer Identification Procedures (CIP), and ongoing **Transaction Monitoring**. It defines **OVDs** (Officially Valid Documents — passport, driving licence, Voter ID, Aadhaar, NREGA card), **V-CIP** (video-KYC), **CKYC** (Central KYC Registry — a 14-digit KYC identifier), and periodic re-KYC cadence (high risk every 2 years, medium 8, low 10).

**Risk-Based Approach (RBA)** — the spine of modern AML. You don't apply the same friction to everyone; you allocate scrutiny in proportion to risk across four vectors: **customer, product/service, geography, and delivery channel**. Low risk → Simplified Due Diligence; high risk → Enhanced Due Diligence.

**Three Lines of Defence (3LoD):**

| Line | Who | Owns |
|---|---|---|
| 1st | Business / front office / operations | Owns and manages the risk; does KYC at onboarding, first-level alert review |
| 2nd | Compliance / AML function (MLRO) | Sets policy, independent oversight, files STRs, advises |
| 3rd | Internal Audit | Independent assurance the first two work |

External auditors and the regulator sit outside as a notional "4th line."

**Roles:** The **Principal Officer (PO)** is the PMLA-designated person responsible for filing reports to FIU-IND. The **Designated Director** is Board-level, personally liable under PMLA. Globally the equivalent title is **MLRO** (Money Laundering Reporting Officer) — the person to whom internal suspicion reports flow and who decides whether to file to the FIU. In a GCC you'll often see PO/MLRO combined.

## Hands-on — step by step

**Scenario:** You're building the AML operating model for "Meridian Capital," a new India-based broker-dealer within a GCC.

1. **Register as a reporting entity** with FIU-IND on FINnet 2.0; obtain the entity's registration and set up user credentials for report submission.
2. **Draft the Board-approved KYC/AML policy** covering the four RBI pillars. Get the Board to formally **appoint a Designated Director and a Principal Officer** — record the resolution; these names are filed with FIU-IND.
3. **Map the RBA.** Build a customer-risk model (see Chapter 2), classify products (a margin trading account is higher risk than a cash equity account), tag geographies against FATF grey/black lists and India's own high-risk list.
4. **Wire the 3LoD.** Front office runs onboarding KYC in the system; a 2nd-line AML analyst independently reviews high-risk onboardings and all screening/TM alerts; Internal Audit schedules an annual AML review.
5. **Set the reporting workflow.** Any staff suspicion → internal Suspicious Activity Report → MLRO/PO reviews → decide file/no-file → if file, submit STR on FINnet within **7 working days**, and **do not tip off** the customer (Section 8 / general prohibition; tipping-off is an offence).
6. **Set cadence:** monthly CTR by the 15th; periodic re-KYC per risk band; annual policy refresh and staff training.

**Worked timing example:** A client deposits ₹4 lakh cash on 3 July, ₹4 lakh on 10 July, ₹3.5 lakh on 20 July into the same account. Individually each is below ₹10 lakh, but they are **integrally connected** and aggregate to ₹11.5 lakh in a calendar month → **CTR triggered**, file by **15 August**. The structuring pattern itself also raises suspicion → assess for **STR** independently.

## The output

A one-page **AML Operating Model**:

```
BOARD ── appoints ── Designated Director (personally liable, PMLA)
   │
   └── Principal Officer / MLRO ── files STR/CTR ──► FIU-IND (FINnet 2.0)

LINE 1  Business & Ops      → onboarding KYC, L1 alert review
LINE 2  AML Compliance/MLRO → policy, screening, TM, STR decision
LINE 3  Internal Audit      → independent assurance

RBA lens: Customer × Product × Geography × Channel → Low/Med/High
Reports: CTR ₹10L (15th) | STR no-threshold (7 wd) | CCR | NTR | CBWTR ₹5L
```

## Checks, gotchas & red flags

- **STR has NO monetary threshold** — a ₹5,000 transaction can trigger one. Candidates who say "STR above ₹10 lakh" fail instantly; that's the **CTR** threshold.
- **7 working days** for STR vs **15th of next month** for CTR — don't swap them.
- **Tipping-off** the customer that an STR was filed is itself an offence — never tell the client.
- FATF **grey list ≠ black list**: grey = increased monitoring (do EDD), black = countermeasures (India: Iran, DPRK, Myanmar).
- The **Designated Director is personally liable** — this is why AML is a Board matter, not a back-office chore.
- RBA is not an excuse to do *less* — it's proportionate; high-risk customers still need EDD, not a waiver.

## Interview drill

**Q1: Difference between a CTR and an STR?**
A CTR is objective and threshold-driven — any cash transaction over ₹10 lakh (or connected series in a month), filed by the 15th of the following month regardless of suspicion. An STR is subjective and threshold-free — filed within 7 working days of forming a suspicion of money laundering or terror financing, at any value. One is a bright-line rule; the other is judgement.

**Q2: Explain the three lines of defence and who files the STR.**
First line is the business — they own the risk and do onboarding KYC and first-level alert review. Second line is AML Compliance, headed by the MLRO/Principal Officer, who sets policy and independently oversees. Third line is Internal Audit, providing assurance. The STR is filed by the Principal Officer/MLRO in the second line — the business flags internally, but only the PO decides and files to FIU-IND.

**Q3: What is the risk-based approach and why does FATF mandate it?**
RBA means allocating AML resources in proportion to assessed risk across customer, product, geography, and channel — Simplified DD for low risk, EDD for high risk. FATF mandates it (R.1) because uniform controls waste resources on low-risk clients while under-scrutinising genuine threats; risk-weighting concentrates scrutiny where laundering is actually likely.

## Learn/practise (free)

- **FATF** website — read the 40 Recommendations and India's 2024 Mutual Evaluation Report (free PDFs).
- **FIU-IND** site — the FINnet 2.0 user guides, STR/CTR formats and XML schemas are public; download and read a blank STR to see the actual fields.
- **RBI Master Direction on KYC** — read it end-to-end once; it's the single most-quoted document in Indian AML interviews.
- **PMLA bare act** — Sections 3, 4, 12, and the definition of "reporting entity."
- Free training: ACAMS "Today" articles, the Egmont Group typology papers, and the ICAI/IIBF AML modules. Rehearse by writing the operating-model diagram above from a blank page until it's automatic.
