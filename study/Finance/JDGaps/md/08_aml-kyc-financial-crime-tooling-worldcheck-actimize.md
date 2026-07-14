# AML/KYC & Financial-Crime Tooling: World-Check, Actimize, SAS, Quantexa, Napier

## The gap

The career bundle decoded *what* a KYC/AML analyst role is and why banks hire for it. What it does **not** teach is the actual **tooling and casework** — the screening engines, transaction-monitoring platforms, alert and case managers, and the regulatory filing chain that every JD names by product. When Luxoft asks for "NICE Actimize, SAS AML, Oracle FCCM, Quantexa, Napier AI, ComplyAdvantage, Refinitiv World-Check" and Citi asks for "screening, negative news, ACAMS," they are asking whether you can *operate the machinery*, not whether you understand the concept. That machinery is the gap.

## Why companies ask for it

> Real posting (Luxoft, Bangalore): "AML Transaction Monitoring, CDD, KYC, Sanctions Screening, Fraud Detection, Case Management, Customer Risk Rating." Named tools: "NICE Actimize, FICO TONBELLER, SAS AML, Quantexa, Oracle FCCM, Napier AI, ComplyAdvantage, Refinitiv World-Check."

> Real posting (Citi, KYC): "screening, negative news, ACAMS."

These roles sit in three buckets: (1) **KYC/CDD analysts** at banks and GCCs (Citi, HSBC, Deutsche, Standard Chartered's Chennai/Bangalore hubs) who onboard and periodically review customers; (2) **AML transaction-monitoring / investigations analysts** who work alerts and file suspicious-transaction reports; and (3) **financial-crime technology / RegTech** roles (Luxoft, Cognizant, TCS BaNCS) who *configure and tune* the detection engines rather than clear alerts. India is the global back-office for all three — most Tier-1 banks run their financial-crime operations from GCCs here.

## What "proficient" looks like

An employer tests whether you can:

- Run a **name screen** against a sanctions/PEP list, read a hit, and clear it as a true or false positive with a documented rationale (fuzzy-match logic, secondary identifiers like DOB/nationality).
- Take a **transaction-monitoring alert**, pull the customer's profile and transaction history, decide "clear vs escalate," and write a defensible investigation narrative.
- Build a **Customer Risk Rating (CRR)** from the standard factors: geography, product, channel, customer type, PEP status.
- Know the **CDD → EDD** trigger points and the **SAR/STR filing** chain end-to-end.
- Speak the vocabulary of at least one named platform (Actimize, SAS, FCCM) — screens, alert queues, case lifecycle.

## How to actually learn/do it

**1. The CDD/EDD spine (RBI, free).** Read the **RBI Master Direction – KYC (2016, updated 2024)**. Learn the three tiers of due diligence:
- **CDD** — identity, beneficial ownership, purpose of relationship, on every customer.
- **EDD** — extra scrutiny for high-risk: PEPs, high-risk geographies, correspondent banking, complex ownership. Triggered by CRR or a red flag.
- **Ongoing monitoring** — periodic review, frequency driven by risk band (high-risk yearly, low-risk every 8–10 yrs).

**2. Sanctions & PEP screening — the logic.** Screening tools (**Refinitiv World-Check**, **Dow Jones Risk & Compliance**, **FircoSoft/Fircosoft Continuity**) hold curated lists: OFAC SDN, UN, EU, UK HMT, MHA India, plus PEP and adverse-media databases. The engine does **fuzzy matching** — phonetic (Soundex/Metaphone), edit-distance, transliteration — so "Mohammed" matches "Muhamad." Your job on a hit: compare **secondary identifiers** (DOB, nationality, passport) to discount false positives. Worked example: an alert fires on customer *Rajesh Kumar* against a World-Check PEP *Rajesh Kumar* — you check DOB (1978 vs 1955) and country (India vs Fiji) → **discount as false positive**, document, close.

**3. Transaction monitoring.** Engines (**NICE Actimize SAM**, **SAS AML**, **Oracle FCCM/Mantas**, **Quantexa**, **Napier AI**, **ComplyAdvantage**) run **scenarios/rules** against transaction data: structuring (many sub-threshold cash deposits), rapid movement of funds, round-tripping, dormant-then-active accounts. Each hit becomes an **alert** in a queue. **Quantexa** and **Napier** add **entity resolution / network analytics** — linking accounts by shared phone/address/device to surface hidden networks, the "next-gen" pitch vs rule-based legacy. Your workflow: pick up alert → review triggering transactions + customer KYC → decide **clear / escalate to case** → if escalated, investigate and recommend a filing.

**4. Case management & filing.** Escalated alerts become **cases**. In India, a suspicious transaction goes as an **STR (Suspicious Transaction Report)** to **FIU-IND** (Financial Intelligence Unit) via the **FINnet/FINGate** portal, under the **PMLA 2002**. Also know **CTR** (cash > ₹10 lakh) and **CCR** (counterfeit currency). Globally the equivalent is a **SAR** to FinCEN (US) or the NCA (UK). Learn the **narrative discipline**: who, what, when, how much, why suspicious, what action recommended.

**5. Free ways to practise.**
- **FATF** 40 Recommendations + the India Mutual Evaluation Report (2024) — the global rulebook, free.
- **RBI KYC Master Direction** and **FIU-IND** website (STR/CTR formats, red-flag indicators) — free.
- **ACAMS** publishes free webinars and a glossary; the **CAMS** certification (~USD 1,995) is the resume gold standard — self-study the syllabus even if you delay the exam.
- **ComplyAdvantage** and **Napier** run free blogs/webinars that walk their screens — good for vocabulary.
- Build a mock CRR scorecard in Excel (you already know Excel) — weight geography/product/channel/customer, output Low/Med/High.

## How it shows up in interviews

**Q: "You get a sanctions screening hit on a customer. Walk me through what you do."**
A: "First I confirm it's a *potential* match, not a confirmed one — screening is fuzzy. I compare secondary identifiers: full name, date of birth, nationality, and any ID numbers against the list entry. If they diverge — different DOB, different country — I discount it as a false positive with a documented rationale and close it. If they align, I don't clear it; I escalate to L2/compliance, freeze or hold the transaction per policy, and it may lead to an STR. The golden rule is never clear a true sanctions hit at analyst level."

**Q: "Difference between CDD and EDD, and what triggers EDD?"**
A: "CDD is the baseline done on every customer — verifying identity, beneficial ownership, and purpose. EDD is deeper scrutiny for higher-risk relationships: source of funds/wealth, senior-management sign-off, more frequent review. It's triggered by the customer risk rating — PEP status, high-risk jurisdiction, correspondent banking, cash-intensive business, or complex/opaque ownership structures."

**Q: "What's a false positive and why do they matter in AML?"**
A: "A false positive is an alert or screening hit that turns out not to be genuinely suspicious. They matter because monitoring systems generate huge volumes — often 90%+ of alerts are false positives — so the operational challenge is tuning scenarios and thresholds to cut noise without missing true risk. That's where entity-resolution tools like Quantexa or Napier add value over pure rules."

## ATS keywords to add

KYC, CDD, EDD, AML, sanctions screening, PEP screening, adverse media / negative news, transaction monitoring, Customer Risk Rating (CRR), name screening, false-positive reduction, alert investigation, case management, SAR, STR, CTR, FIU-IND, PMLA, FATF, RBI KYC Master Direction, OFAC, NICE Actimize, SAS AML, Oracle FCCM, Quantexa, Napier AI, ComplyAdvantage, Refinitiv World-Check, Dow Jones Risk & Compliance, FircoSoft, entity resolution, ACAMS / CAMS.
