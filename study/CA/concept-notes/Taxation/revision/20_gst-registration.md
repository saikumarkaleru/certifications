# Registration — Secs 22–30, Rules 8–23

## Snapshot
Registration is the turnstile of the credit chain: only a registered person can (a) collect GST and (b) claim ITC. Identity = GSTIN (15 chars, PAN-based, State-wise). Test order: Relief (Sec 23) → Compulsion (Sec 24) → Threshold (Sec 22) → Voluntary (25(3)).

## Core concepts
- GSTIN = State code(2) + PAN(10) + entity code(1) + Z + checksum. PAN-based & State-wise; one PAN can hold many GSTINs; each GSTIN = distinct person.
- "Taxable person" [2(107)] = registered OR liable to be registered → liability precedes the certificate.
- Registration is State-wise because dual GST needs each State to police its own SGST.
- Distinct persons [25(4)/(5)]: same-PAN establishments in different States → stock transfer between them is a taxable supply.

## Key provisions / rules

### Aggregate turnover [Sec 2(6)]
All-India, same-PAN. INCLUDE: taxable + exempt (incl nil-rated & non-taxable) + exports + inter-State supplies. EXCLUDE: CGST/SGST/IGST/UTGST/cess; inward RCM supplies.
Distinguish "turnover in State" [2(112)] used for composition levy. Threshold test always uses all-India aggregate.

### Thresholds [Sec 22] — "exceeds" (exactly at limit ≠ liable)
| Category (normal States) | Threshold p.a. |
|---|---|
| Supplier of GOODS exclusively (clean) | ₹40 lakh |
| Services or goods+services | ₹20 lakh |
| Special-category — services/mixed | ₹10 lakh |
| Special-category — goods | ₹20 lakh |

₹40L needs ALL: exclusively goods; no inter-State; not Sec 24 person; not specified goods (ice cream, pan masala, tobacco, fly-ash bricks etc.); not voluntarily registered. Any service element → drops to ₹20L.
Interest carve-out: interest/discount on deposits/loans/advances is IGNORED for the "exclusively goods" test → ₹40L survives despite bank interest income.
Special-category registration list ≠ Article 279A list (a notified opted-in sub-set — verify basket for attempt).

### Not liable [Sec 23] (overrides even Sec 22/24 for these)
- Exclusively exempt/nil-rated/non-taxable supplies.
- Agriculturist [2(7): individual/HUF cultivating personally] — only produce out of cultivation.
- Wholly-RCM SUPPLIERS (they collect nothing).

### Compulsory [Sec 24] — threshold irrelevant (from Rupee One)
Inter-State taxable supply of GOODS; casual taxable person (CTP); RCM RECIPIENT; Sec 9(5) ECO; non-resident (NRTP); TDS deductor (51); TCS/ECO (52); suppliers via TCS-ECO; ISD; agents; OIDAR from abroad.
Carve-outs (relief): small inter-State supply of SERVICES ≤₹20L; small services via ECO ≤₹20L; notified handicraft goods ≤₹20L (₹10L special) with PAN + e-way bill.
RCM trap: wholly-RCM SUPPLIER → Sec 23 (relieved); RCM RECIPIENT → Sec 24 (compelled).

### Special persons
| | CTP | NRTP |
|---|---|---|
| Who | PAN in India, supplies where no fixed place | No fixed place/residence in India |
| PAN / form | PAN; REG-01 | Usually no PAN; REG-09 |
| ITC | Normal | NONE except own imports |
| Validity | 90 days (+90) | 90 days (+90) |
Both: apply 5 days prior; advance deposit of estimated tax → cash ledger; extension via REG-11 with fresh deposit; excess refundable only after all returns filed.
Voluntary [25(3)]: all provisions apply; cancellable if no business in 6 months.

### Procedure & timelines [Sec 25, Rules 8–11]
Apply within 30 days of becoming liable (CTP/NRTP: 5 days prior).
REG-01 Part A (PAN/mobile/email OTP → TRN) → Part B (details/docs, DSC/EVC) → REG-02 ack → Aadhaar authentication → approve. Deficiency: REG-03 notice → reply REG-04 (7 working days) → reject REG-05. Deemed approval on officer inaction. Certificate REG-06 with GSTIN.
Deemed-approval clock:
| Situation | Window |
|---|---|
| Aadhaar authenticated, no risk | 7 working days |
| Aadhaar not opted / failed | 30 days (physical verification, report REG-30) |
| High-risk flagged | Extended, physical verification |
Suo-motu temp registration by officer = REG-12 (apply properly in 90 days).
Effective date: applied ≤30 days → from date of liability (ITC on opening stock allowed); applied late → from date of grant (gap ITC lost, gap output tax still due + interest).

### Amendment [Sec 28, Rule 19] — intimate REG-14 within 15 days
- Core (legal name w/o PAN change, principal/additional place, partners/directors/karta) → officer approves REG-15 within 15 working days (else deemed).
- Non-core → auto on portal.
- PAN-changing constitution change → FRESH registration, not amendment.

### Cancellation [Sec 29, Rules 20–22]
Voluntary (REG-16) or suo-motu (fraud, non-filing, no business in 6 months (voluntary registrant), bill-trading). SCN REG-17 → reply REG-18 → order REG-19 (or drop REG-20).
Sec 29(5) clawback: pay HIGHER of ITC on inputs (stock + finished/semi-finished) + capital goods vs output tax on such goods. CG = higher of [ITC − 5%/qtr of use] or [tax on transaction value]. Inputs = actual ITC on stock.
Suspension [Rule 21A] pending cancellation — no taxable supply/invoice. Past dues survive [29(3)]. Back-dated cancellation can strip recipient's ITC. File Final Return GSTR-10 within 3 months.

### Revocation [Sec 30, Rule 23]
Only vs officer (suo-motu) cancellation. File all pending returns + pay all dues first. Apply REG-21 within 30 days (extendable by officer then Commissioner — verify) → order REG-22 (or reject REG-23/reply REG-24). Keeps same GSTIN + history.

## Worked mini-example
Mehta Traders (Maharashtra, goods-only, clean): taxable ₹28L + exempt ₹9L + nil-rated ₹4L = ₹41L aggregate (RCM ₹1.5L excluded). ₹41L > ₹40L → registration required. (Dropping ₹13L exempt/nil wrongly gives ₹28L → wrong answer.)

Cancellation clawback: inputs ITC 1,20,000 + finished-goods ITC 80,000 = 2,00,000. Machine 13 months = 5 quarters → ITC 3,00,000 × 75% = 2,25,000 vs tax on value 1,90,000 → higher 2,25,000. Total = ₹4,25,000; file GSTR-10 in 3 months.

## Exam traps & must-remember
- Exempt + nil-rated COUNT for threshold (commonest error); RCM inward EXCLUDED.
- ₹40L is goods-only-and-clean; any service → ₹20L; special-category → ₹10L.
- Sec 24 overrides threshold — one ₹50,000 inter-State GOODS supply forces registration on ₹19L firm; inter-State SERVICES ≤₹20L is carved out.
- Late application → registration from grant date → gap ITC lost, gap output tax still due.
- Cancellation: pay back ITC on stock AND CG (higher-of on CG); file GSTR-10.
- Revocation only vs officer cancellation, after curing all defaults.
- Core amendment inaction 15 working days → deemed approved; PAN change → fresh registration.
- Deemed-approval clock conditional on Aadhaar: no Aadhaar → 30 days, not 7.
- NRTP: REG-09, usually no PAN, no ITC (except own imports); CTP uses PAN, claims ITC.
- Bank interest ignored in "exclusively goods" test (keeps ₹40L); real supplied service breaks it.
- Cancellation ≠ clean exit: past dues survive [29(3)]; retrospective cancellation strips recipient ITC.
- "Exceeds" — exactly ₹40,00,000 does NOT trigger.

## One-line recall
- Only registered persons collect GST and claim ITC; liability precedes the certificate.
- Aggregate turnover = all outward supplies (incl exempt) all-India same PAN, minus taxes & RCM inward.
- Thresholds 40/20/10; services always ₹20L; Sec 24 overrides threshold, Sec 23 relieves.
- Apply ≤30 days → effective from liability date; late → from grant (gap ITC lost).
- Cancellation clawback: ITC on stock + CG (CG higher-of); revocation only vs officer cancellation.
- Deemed approval = 7 wd if Aadhaar authenticated, else 30 days.
