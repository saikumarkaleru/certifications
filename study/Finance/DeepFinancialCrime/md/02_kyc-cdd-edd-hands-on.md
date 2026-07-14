# KYC / CDD / EDD Hands-On

## What you'll be able to do

Onboard a customer end-to-end: verify identity against Officially Valid Documents, unwind an ownership structure to find the true **beneficial owner (UBO)**, run a **customer risk-rating model** that produces a numeric score and a Low/Medium/High band, know exactly when **Enhanced Due Diligence (EDD)** kicks in, document **source of funds/wealth**, and schedule the next periodic review. You'll carry a worked scoring spreadsheet you can rebuild in Excel in five minutes — the single most useful artefact an AML analyst brings to an interview.

## The essentials

**KYC vs CDD vs EDD:**

| Term | What it is |
|---|---|
| KYC | The whole "Know Your Customer" programme — identify + verify + risk-rate + monitor |
| CDD | Customer Due Diligence — the standard baseline: identify the customer & UBO, understand purpose/nature, monitor |
| SDD | Simplified DD — reduced measures for demonstrably low-risk customers (e.g., a salaried resident with a small savings account) |
| EDD | Enhanced DD — extra scrutiny for high-risk: SoW/SoF evidence, senior sign-off, closer monitoring |

**CIP (Customer Identification Procedure)** for an individual in India: name, address, PAN (mandatory for most financial relationships), and an **OVD** — Aadhaar, passport, driving licence, Voter ID, or NREGA card. **V-CIP** (video KYC) is RBI-permitted for remote onboarding. Records go to the **CKYC Registry** (14-digit KYC Identifier).

**Beneficial Owner (UBO)** — the natural person who ultimately owns or controls the customer. RBI/PMLA thresholds:

| Entity type | UBO threshold (ownership/control) |
|---|---|
| Company | > 10% shares or controlling interest |
| Partnership / LLP | > 10% of capital or profits |
| Trust | Author, trustee, beneficiaries with ≥10% interest, and any controlling person |

You must **look through** layers. If Client Ltd is 60% owned by Holdco, and Holdco is 80% owned by Mr X, then Mr X's effective stake = 60% × 80% = **48% > 10% → Mr X is a UBO.**

**EDD triggers:** PEP (Politically Exposed Person) or their family/close associate; customer from a FATF grey/black-list or high-risk jurisdiction; complex/opaque ownership; correspondent banking; high-risk products (private banking, bearer instruments, crypto); adverse media; non-face-to-face onboarding without adequate controls; unusually large or unexplained wealth.

**Source of Funds (SoF)** = origin of the specific money in this transaction (salary credit, sale of property, loan). **Source of Wealth (SoW)** = origin of the customer's total net worth (inherited business, decades of professional income). EDD needs both, with evidence (bank statements, sale deed, tax returns, audited accounts).

**Periodic review cadence** (RBI): High every **2 years**, Medium **8**, Low **10** — or sooner on a trigger event (adverse media, transaction anomaly, PEP status change).

## Hands-on — step by step

**Case:** Onboarding **Sunrise Trading Pvt Ltd** for a broking account.

**Step 1 — Identify the entity.** Collect Certificate of Incorporation, PAN, GST registration, board resolution authorising account opening, and list of directors/authorised signatories. Verify PAN on the income-tax portal and CIN on the MCA21 master data.

**Step 2 — Unwind ownership for UBO.** Shareholding: Mr Rao 55%, Meridian Holdings LLP 45%. Meridian LLP profit-share: Mr Rao 30%, Ms Iyer 70%.
- Mr Rao effective = 55% + (45% × 30%) = 55% + 13.5% = **68.5% → UBO**.
- Ms Iyer effective = 45% × 70% = **31.5% > 10% → UBO**.
Record both UBOs, verify each with PAN + OVD, and screen both names (Chapter 3).

**Step 3 — Screen.** Run entity + both UBOs + directors through sanctions/PEP/adverse-media lists. Assume Ms Iyer returns a **PEP** hit — she's on a state-level statutory board. → **EDD triggered.**

**Step 4 — Risk-rate.** Build the scoring model. Each factor scored 1 (low) / 2 (med) / 3 (high), multiplied by a weight; sum = weighted score.

| Factor | Weight | Assessment | Raw (1-3) | Weighted |
|---|---|---|---|---|
| Customer type | 25% | Pvt Ltd, has a PEP UBO | 3 | 0.75 |
| Geography | 20% | India (domestic), no high-risk link | 1 | 0.20 |
| Product/service | 20% | Margin trading account | 2 | 0.40 |
| Channel | 15% | Non-face-to-face (V-CIP) | 2 | 0.30 |
| Occupation/business | 20% | Commodity trading (cash-intensive) | 2 | 0.40 |
| **Total** | 100% | | | **2.05** |

**Banding:** 1.00–1.66 = Low, 1.67–2.33 = Medium, 2.34–3.00 = High. Score **2.05 → Medium** by model — **but the PEP UBO is an automatic override to High.** Overrides always beat the arithmetic.

**Step 5 — Apply EDD** (because High / PEP): obtain **senior management approval** to onboard; document **SoW** (Ms Iyer's wealth from a family textile business — obtain audited accounts + IT returns) and **SoF** (₹50 lakh initial funding traced to Sunrise's audited turnover); set **enhanced transaction monitoring** thresholds; schedule review in **2 years**.

**Step 6 — Record & register.** File CKYC records, store the UBO declaration, the risk score sheet, EDD approvals, and SoW/SoF evidence in the customer file.

## The output

**Customer Risk Assessment — Sunrise Trading Pvt Ltd**

```
Entity PAN/CIN: verified (MCA21, IT portal)
UBOs: Mr Rao 68.5% (verified, no hits)
      Ms Iyer 31.5% (verified, PEP — state board)
Screening: 1 PEP hit confirmed; no sanctions/adverse media
Model score: 2.05  → model band MEDIUM
Override: PEP UBO → FINAL RATING: HIGH
EDD: Senior approval [signed], SoW [audited a/cs], SoF [turnover trace]
Enhanced TM: ON | Next review: 2 years (Jul 2028)
Decision: ACCEPT with EDD
```

## Checks, gotchas & red flags

- **Effective ownership, not direct** — multiply through the chain. Missing an indirect UBO is the classic UBO failure.
- **Overrides beat scores** — a PEP, a sanctions near-match, or a high-risk-country nexus forces High regardless of the weighted number.
- **SoF ≠ SoW.** Confusing them is a frequent interview slip: funds = this money; wealth = overall net worth.
- Don't treat **V-CIP / non-face-to-face** as automatically fine — it's a higher-risk *channel* and scores accordingly.
- **PEP status doesn't mean criminal** — it means higher risk, so EDD, not refusal (unless policy says decline).
- The UBO **10% threshold** is control *or* ownership — someone with 5% shares but a controlling agreement is still a UBO.
- Periodic review is **risk-driven** (2/8/10 yrs) but any trigger event resets it immediately.

## Interview drill

**Q1: Walk me through identifying the UBO of a company owned by other companies.**
Start with the immediate shareholder register, then look through each corporate shareholder to the natural persons behind it, multiplying stakes down each chain. Anyone whose *effective* ownership exceeds 10%, or who exercises control by other means (voting agreements, board control), is a UBO. If no natural person meets the threshold, you fall back to the senior managing official. You verify each identified UBO with PAN and an OVD and screen them.

**Q2: When does CDD become EDD, and what extra do you actually do?**
EDD triggers on PEPs and their associates, high-risk jurisdictions, opaque structures, high-risk products, adverse media, or unexplained wealth. The extra measures are: senior management sign-off to onboard/continue, documented and evidenced Source of Wealth and Source of Funds, more frequent review (typically 2-yearly), and tighter transaction-monitoring thresholds.

**Q3: Your model scores a client Medium but they're a PEP. Final rating?**
High. A qualitative override — PEP status, a sanctions nexus, or a high-risk-country link — supersedes the arithmetic score. The model is a floor for scrutiny, not a ceiling; you always take the more conservative outcome and apply EDD.

## Learn/practise (free)

- Rebuild the weighted risk model above in **Excel or Google Sheets** — factors, weights, 1-3 scale, SUMPRODUCT, and IF-based banding with a PEP override flag. This is the single best portfolio piece.
- **RBI Master Direction on KYC** — the UBO thresholds, OVD list, and V-CIP rules are all there verbatim.
- **CKYC Registry** and **Wolfsberg Group** CDD/private-banking papers (free) for the global standard.
- Practise UBO look-through with public **MCA21** filings — pick any listed subsidiary and trace it up.
- Free courses: IIBF AML-KYC module, ACAMS free resources, and FATF guidance on PEPs (R.12) and beneficial ownership (R.24/25).
