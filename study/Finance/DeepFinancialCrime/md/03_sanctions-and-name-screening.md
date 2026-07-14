# Sanctions & Name Screening

## What you'll be able to do

Screen a name against sanctions, PEP and adverse-media lists; understand which lists bind an Indian entity and which bind a global GCC; read a **fuzzy-match** score and decide **true hit vs false positive**; write a clean **alert disposition** with a documented rationale; and know the **escalation path** when a real match surfaces. You'll work a live screening hit end-to-end — the exact task a Level-1 screening analyst does hundreds of times a day.

## The essentials

**The lists that matter:**

| List | Owner | Binds whom |
|---|---|---|
| **OFAC SDN** | US Treasury | Anyone touching USD/US persons/US nexus — de facto global |
| **UN Consolidated** | UN Security Council | All member states, incl. India (binding under UNSC resolutions) |
| **EU Consolidated** | European Union | EU nexus |
| **UK OFSI** | UK Treasury | UK nexus |
| **MHA / UAPA lists** | India Ministry of Home Affairs | India — designated terrorist individuals/orgs under UAPA |
| **MEA / UNSC 1267** | India via UN 1267 Committee | India — Al-Qaida/ISIL/Taliban regime |

An India-based GCC serving US/EU clients must screen against **all** of these, not just Indian lists — because the *client's* jurisdiction reaches into your process (extraterritoriality, esp. OFAC).

**PEP screening** — flags Politically Exposed Persons (heads of state, ministers, senior judiciary/military, SOE executives, senior party officials) plus **family members and close associates (RCAs)**. PEP ≠ sanctioned; it's a risk flag driving EDD (Chapter 2).

**Adverse media (negative news)** — screening open-source/news for links to fraud, corruption, terrorism, trafficking. Automated tools categorise by crime type and recency.

**Screening tools (paid):**

| Tool | Strength |
|---|---|
| **Refinitiv World-Check One** | The market-standard sanctions/PEP/adverse-media database; deep, well-curated records |
| **Dow Jones Risk & Compliance** | Strong PEP and adverse-media coverage, state-ownership data |
| **FircoSoft (Accuity/LexisNexis)** | Real-time **payment/transaction filtering** engine — screens SWIFT messages inline; strong fuzzy-matching |
| **Bridger / LexisNexis, ComplyAdvantage** | Real-time API screening, ComplyAdvantage strong on live data |

**Fuzzy matching** — because names are transliterated, misspelled and reordered, screening can't be exact-match only. Engines use algorithms: **Levenshtein/edit distance**, **Jaro-Winkler**, **Soundex/Metaphone** (phonetic), plus token/n-gram scoring and secondary-identifier matching (DOB, nationality, passport). Each candidate gets a **match score (0–100%)**; a configurable **threshold** (say 85%) decides whether an alert generates. Lower threshold = more alerts = more false positives = fewer missed true hits (fewer false negatives). Tuning this trade-off is the whole game.

## Hands-on — step by step

**Scenario:** You onboard **"Mohammed Ali Rahman"**, DOB 1979, nationality UAE, for a corporate account. Screening fires an alert.

**Step 1 — Read the alert.** The engine matched the customer to an OFAC SDN entry:
```
Customer:  Mohammed Ali Rahman | DOB 12-03-1979 | UAE
SDN hit:   Muhammad Ali RAHMAN  | DOB 1979      | UAE | SDGT program
Match score: 92%  | Matched on: name (fuzzy) + YOB + nationality
```

**Step 2 — Compare identifiers (the "4-eyes" discipline).** Don't stop at the name. Check every available secondary identifier:
- Name: "Mohammed" vs "Muhammad", "Ali" vs "Ali", "Rahman" vs "RAHMAN" — a classic transliteration variant; phonetically identical. **Not discriminating.**
- **DOB**: customer 12-March-1979; SDN "1979" (year only) — **consistent, not contradictory.**
- **Nationality**: UAE = UAE — **consistent.**
- Passport/ID number: customer has passport ending 4471; SDN record lists a passport ending 4471 → **strong corroboration.**

**Step 3 — Decide.** Name variant + matching DOB year + matching nationality + **matching passport number** = this is **not** a coincidental namesake. **True positive.**

**Step 4 — Act (do NOT onboard / freeze).** For a genuine sanctions match:
- **Do not proceed** with the account or transaction; **freeze/hold** any funds.
- **Escalate immediately** to the MLRO/sanctions officer — sanctions hits bypass normal L1 disposition.
- File the required report: in India, report to **FIU-IND** and comply with **UAPA/MHA freezing** obligations; for OFAC nexus, a **blocking report** to OFAC.
- **Do not tip off** the customer about the sanctions match/report.

**Contrast — a false positive.** Same customer, but the SDN record shows DOB 1955, nationality Yemen, different passport. Name matches 92% but **DOB, nationality and passport all contradict** → **false positive**. Disposition: "Name-only fuzzy match; DOB (1979 vs 1955), nationality (UAE vs Yemen) and passport all mismatch. Coincidental namesake. Cleared." Record rationale, close alert, whitelist the pair to suppress future re-alerts on the same entity.

## The output

**Screening Alert Disposition**

```
Alert ID: SCR-2026-04412
Customer: Mohammed Ali Rahman | UAE | DOB 12-Mar-1979 | Passport …4471
List hit: OFAC SDN — Muhammad Ali RAHMAN | SDGT | passport …4471
Score: 92% (name fuzzy + YOB + nationality + passport)

Secondary-ID review:
  Name         MATCH (transliteration variant)
  DOB (year)   MATCH (1979)
  Nationality  MATCH (UAE)
  Passport     MATCH (…4471)  ← decisive

DISPOSITION: TRUE POSITIVE — confirmed sanctions match
ACTION: Account NOT opened; funds blocked; escalated to MLRO;
        blocking/STR filed; customer NOT tipped off.
Analyst: [id]  Reviewer (4-eyes): [id]  Date: 15-Jul-2026
```

## Checks, gotchas & red flags

- **Never clear on name alone** — always work the secondary identifiers (DOB, nationality, passport, place).
- **Passport/ID match is decisive** — a matching document number turns a "maybe" into a true positive fast.
- A **year-only DOB** on the list that's consistent with your customer is **not** exculpatory — absence of contradiction ≠ evidence of difference.
- **Sanctions hits escalate immediately** and freeze — they do not sit in a routine L1 queue like a PEP alert.
- **Do not tip off** — freezing/reporting is confidential.
- Threshold tuning is a governed change: lowering it floods false positives, raising it risks **false negatives** (missed true hits) — the dangerous error. Document any change.
- **Whitelisting** must be per specific customer-vs-record pair, time-stamped and reviewed — never a blanket name suppression.
- OFAC's **50% Rule**: an entity ≥50% owned by SDN parties is itself blocked even if not separately listed — screen ownership, not just the named entity.

## Interview drill

**Q1: You get a 95% name match to an SDN entry. Is it a hit?**
Not yet — 95% is only the name-similarity score. I compare secondary identifiers: date of birth, nationality, place of birth, and any passport/ID number. If those corroborate (especially a matching passport number), it's a true positive — I stop the transaction, freeze, and escalate to the MLRO. If DOB and nationality clearly contradict, it's a coincidental namesake and I clear it with a documented rationale.

**Q2: Which is worse in screening — a false positive or a false negative, and how does threshold setting relate?**
A false negative — a genuine sanctioned party passing through — is far worse; it's a direct sanctions breach with legal and reputational consequences. False positives are costly in analyst time but safe. Lowering the match threshold reduces false negatives at the cost of more false positives; raising it does the reverse. You tune to keep false negatives near zero while managing false-positive volume, and you document the trade-off.

**Q3: An India-based team screens a US client's payment. Which lists apply?**
All relevant ones: UN and India's MHA/UAPA and UNSC-1267 lists bind us domestically, and because there's a US and USD nexus, OFAC SDN applies extraterritorially; EU/UK lists apply if there's an EU/UK leg. Sanctions screening follows the transaction's jurisdictional touchpoints, not just the screening team's home country.

## Learn/practise (free)

- **OFAC Sanctions List Search** (free web tool) — screen real names against the live SDN list and see the record fields.
- **UN Consolidated List**, **EU Consolidated List**, **UK OFSI list**, and India's **MHA UAPA** designated lists — all free downloads; practise manual matching.
- Refinitiv/Dow Jones publish free methodology papers on fuzzy matching and PEP definitions.
- Build a mini screening engine in **Python** (`fuzzywuzzy`/`rapidfuzz`, `jellyfish` for Jaro-Winkler/Soundex) to score a customer list against the OFAC CSV — the best way to *feel* how thresholds behave.
- **Wolfsberg Group** guidance on sanctions screening and the ACAMS sanctions primers (free).
