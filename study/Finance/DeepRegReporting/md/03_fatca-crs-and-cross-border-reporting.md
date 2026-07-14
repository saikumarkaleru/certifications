# FATCA, CRS & Cross-Border Reporting

## What you'll be able to do

You will be able to take a real customer onboarding pack, classify the account holder and the entity, decide whether the account is "reportable," identify the reportable jurisdiction(s), run the due-diligence tests, and assemble the fields that go into the annual reporting file. You'll know the difference between FATCA and CRS, when US withholding bites, and how the Indian rules (Income-tax Rules 114F, 114G, 114H) map onto the global framework. You'll finish with a worked classification of a genuinely tricky entity account.

## The essentials

**FATCA** (Foreign Account Tax Compliance Act, US, 2010) forces non-US financial institutions to identify accounts held by **US persons** and report them — via their local tax authority under an Inter-Governmental Agreement (IGA) — to the IRS. India signed a Model 1 IGA: Indian FIs report to the CBDT, which passes data to the IRS. Non-compliance risks 30% US withholding on US-source income.

**CRS** (Common Reporting Standard, OECD, 2014) is the multilateral cousin — over 100 jurisdictions automatically exchange financial-account information about each other's tax residents. There is no single "CRS country"; you report an account to *every* jurisdiction where the holder is tax-resident (other than India). No withholding mechanism — it's pure information exchange.

| Feature | FATCA | CRS |
|---|---|---|
| Origin | US law | OECD multilateral |
| Who's reported | US persons | Tax residents of any partner jurisdiction |
| Threshold | Pre-existing individual accounts < US$50,000 may be exempt | No de-minimis for new accounts; limited for pre-existing |
| Enforcement | 30% withholding | Peer pressure / local penalties |
| India rule | Rule 114F–H | Rule 114F–H (same machinery) |

**India's legal hook:** Income-tax Rules **114F** (definitions — Financial Institution, Financial Account, Reportable Account), **114G** (information to be maintained and reported — Form 61B), **114H** (due-diligence procedures). Reporting Financial Institutions file **Form 61B** annually by **31 May** on the income-tax Reporting Portal.

**Entity classification** is the hard part. Every account holder is either an **individual** or an **entity**. Entities split into:
- **Financial Institutions (FIs):** depository, custodial, investment entity, or specified insurance company. Generally not reportable themselves (they report their own accounts).
- **Non-Financial Entities (NFEs):**
  - **Active NFE** — mostly operating business (<50% passive income and <50% passive assets), or listed/govt/etc. Only the entity's own residence matters.
  - **Passive NFE** — everything else (holding companies, family investment vehicles). Here you must **look through** to the **controlling persons** (typically ≥25% beneficial owners) and test *their* residence.

**Due diligence** differs by account:
- **New accounts:** collect a **self-certification** at onboarding (residence, TIN). Must be reasonable vs other KYC.
- **Pre-existing accounts:** apply **indicia** searches — for individuals, look for US/foreign place of birth, address, phone, standing instructions, power of attorney, "hold mail" address. High-value pre-existing accounts get an enhanced relationship-manager enquiry.

## Hands-on — step by step

**Scenario:** "Sunrise Holdings Pvt Ltd" opens a demat + custody account with an Indian broker (a Reporting FI). Onboarding facts:
- Sunrise is India-incorporated, unlisted.
- 90% of its income last year was dividends and capital gains (it's an investment holding company).
- Shareholders: Mr A (India-resident, 40%), Ms B (US citizen resident in Dubai, 35%), a trust (25%) whose settlor is UK-resident.

**Step 1 — Is the holder an entity?** Yes, Sunrise is an entity, not an individual.

**Step 2 — FI or NFE?** Sunrise doesn't accept deposits, hold assets for others, or act as an investment manager for clients — it invests its own money. It's an **NFE**, not an FI. (If it were professionally managed by another FI, it could be an "investment entity"; here assume self-managed by directors → NFE.)

**Step 3 — Active or Passive NFE?** >50% of income is passive (dividends, gains) → **Passive NFE**. This is the trigger to look through.

**Step 4 — Identify controlling persons (≥25% or control).**
- Mr A, 40% — India-resident → not reportable.
- Ms B, 35% — US citizen (FATCA person) and Dubai (UAE) tax-resident (CRS) → reportable under **both** FATCA (US) and CRS (UAE).
- Trust, 25% — look through to controlling persons of the trust: settlor is UK-resident → **UK is a reportable jurisdiction** under CRS.

**Step 5 — Collect self-certifications and TINs.** Ms B's US TIN (SSN/ITIN) for FATCA, UAE TIN for CRS; UK settlor's UK UTR. Validate reasonableness against passports/KYC.

**Step 6 — Determine account balance / values.** Report year-end account balance or value; for custody accounts also gross proceeds and income paid/credited during the year.

**Step 7 — Assemble the report.** Sunrise's account becomes a reportable account with **three** controlling-person reports: Ms B to the US (FATCA) and to the UAE (CRS), and the UK settlor to the UK (CRS). Mr A generates no report.

## The output

The finished artefact is the **Form 61B / CRS-FATCA XML record** (shown here in readable form; the portal ingests schema-validated XML):

```
REPORTING FI: Sunrise's Broker (GIIN: XXXXXX.99999.SL.356)  Period: CY2025
ACCOUNT: Custody A/C 356-Sunrise Holdings Pvt Ltd
  Account Holder: Sunrise Holdings Pvt Ltd — Passive NFE
  Year-end balance: INR 4,20,00,000
  Controlling Person 1: Ms B
     Residence: US (FATCA) + AE/UAE (CRS)
     US TIN: 123-45-6789 | UAE TIN: 784-xxxx
     Reportable to: IRS (via CBDT), UAE tax authority
  Controlling Person 2: Trust — look-through settlor
     Residence: GB (UK)  | UK TIN (UTR): 1234567890
     Reportable to: HMRC (via CBDT)
  Controlling Person 3: Mr A — IN resident — NOT reported
  Payments during year: Dividends INR 22,00,000; Gross proceeds INR 1,10,00,000
```

The broker submits Form 61B by 31 May; CBDT routes each controlling-person record to the correct foreign authority.

## Checks, gotchas & red flags

- **US citizenship = US person regardless of where they live.** Ms B lives in Dubai but her US citizenship makes her FATCA-reportable. This is the single most-missed rule.
- **Passive NFE ⇒ look through.** The commonest error is reporting only the entity's residence (India) and stopping. If it's a passive NFE, you must test the controlling persons — that's the whole point.
- **A person can be reportable to multiple jurisdictions.** Dual residence/citizenship means multiple records for the same person. Don't deduplicate away a valid second jurisdiction.
- **Self-certification must be reasonable.** If KYC shows a US birthplace but the self-cert says "no US person," you have an unresolved indicium — you cannot just accept the form.
- **Nil reporting is required.** If you have no reportable accounts, you still file a nil statement in India.
- **TIN missing ≠ skip.** Report with a documented reason; don't silently drop the record.
- **Investment entity vs passive NFE.** A professionally-managed investment vehicle in a non-participating jurisdiction can flip classification — check who manages the entity.

## Interview drill

**Q: An Indian resident holding a US green card opens an account. Reportable? Under what?**
A: Yes, under FATCA. A green-card holder is a US person for US tax purposes regardless of Indian residence, so the account is FATCA-reportable to the IRS via CBDT. It's generally not CRS-reportable to the US (the US isn't a CRS participant), and not reportable to any other jurisdiction unless she's also tax-resident elsewhere. So this is a FATCA-only case — a good test of whether you know the US sits outside CRS.

**Q: What's the practical difference between an Active and a Passive NFE for reporting?**
A: For an Active NFE you only care about the entity's own tax residence — if it's India-resident and not otherwise reportable, you're done, no look-through. For a Passive NFE you must identify the controlling persons (typically ≥25% beneficial owners) and test each one's residence/citizenship, then report the account against every reportable controlling person. Misclassifying a passive holding company as active is the way real reporting failures happen, because it suppresses the look-through entirely.

## Learn/practise (free)

- **OECD Automatic Exchange Portal** (oecd.org, free): the CRS Standard, the CRS-by-jurisdiction status table, and the official commentary with worked entity-classification examples.
- **IRS FATCA pages** (irs.gov, free): the IGA list, entity classification flowcharts, and the W-8BEN-E / W-9 forms you'll actually collect.
- **Income-tax India Reporting Portal → Resources** (free): the Form 61B schema, the Guidance Note on FATCA and CRS (a genuinely excellent 100-page free PDF with Indian examples), and Rules 114F–H.
- Rehearse by taking five fictional entities (a listed company, a family trust, a holding co, a fund, an individual with a US birthplace) and classifying each end-to-end. Build the decision tree once and the classifications become mechanical.
