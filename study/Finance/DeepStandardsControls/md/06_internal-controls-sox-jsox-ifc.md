# Internal Controls: SOX, J-SOX, IFC — RCM, Testing, Deficiencies

## What you'll be able to do
Walk into a GCC controls team and immediately be useful: read a process narrative, build a **Risk & Control Matrix (RCM)** row, distinguish **design effectiveness** from **operating effectiveness**, run a **walkthrough**, pick a **sample size** and perform a **test of controls**, document the results, and **evaluate a deficiency** — deciding whether it's a control deficiency, a **significant deficiency (SD)**, or a **material weakness (MW)**. You'll understand how the same machinery is labelled **SOX** in the US, **J-SOX** in Japan, and **IFC / IFCoFR** in India, and what management's attestation actually asserts.

## The essentials

**The frameworks.** Internal Control over Financial Reporting (ICFR) is assessed against a recognised framework — globally that's **COSO 2013**, with its **five components** and **17 principles**:
1. **Control Environment** — tone at the top, ethics, competence.
2. **Risk Assessment** — identify what could go wrong (WCGW) in each assertion.
3. **Control Activities** — the actual controls (approvals, reconciliations, segregation of duties).
4. **Information & Communication** — data flows, reporting.
5. **Monitoring** — ongoing/periodic evaluation.

**The regimes.**
| Regime | Jurisdiction | Legal basis | Auditor opinion on ICFR? |
|---|---|---|---|
| **SOX** (s.302 CEO/CFO certify; s.404 ICFR) | US (SEC filers) | Sarbanes-Oxley 2002; PCAOB AS 2201 | Yes for accelerated filers (404b) |
| **J-SOX** | Japan | FIEA 2006 | Yes (internal control audit) |
| **IFC / IFCoFR** | India | Companies Act 2013 s.134(5)(e), 143(3)(i); Rule 8(5) | Auditor reports on IFC adequacy & operating effectiveness |

In India the **auditor** reports on IFCoFR (SA 315/330 + ICAI Guidance Note), the **Board** states responsibility, and **independent directors/audit committee** oversee.

**Control taxonomy.** By purpose: **preventive** (stops error before it happens — e.g. system blocks a PO over limit) vs **detective** (catches after — e.g. bank reconciliation). By operation: **manual** vs **automated** vs **IT-dependent manual** (a person reviews a system report — you must test *both* the report's integrity and the review). **Entity-Level Controls (ELCs)** vs **Process-Level Controls**. Frequency: annual, quarterly, monthly, daily, per-transaction.

**Design vs operating effectiveness.**
- **Design effectiveness** — *if* the control operates as intended, would it prevent/detect a material misstatement? Tested via **walkthrough** (trace one transaction end-to-end).
- **Operating effectiveness** — is it *actually* operating consistently over the period? Tested via **test of controls** on a sample.

**Sample sizes (typical, AICPA/PCAOB guidance):**
| Control frequency | Population | Sample |
|---|---|---|
| Annual | 1 | 1 |
| Quarterly | 4 | 2 |
| Monthly | 12 | 2–5 |
| Weekly | 52 | 5–15 |
| Daily | ~250 | 20–40 |
| Multiple/day (transactional) | thousands | 25–60 |

**Deficiency evaluation.** A **deficiency** exists when a control is missing or doesn't operate so as to prevent/detect a misstatement on a timely basis. Grade by **severity = likelihood × magnitude of potential misstatement** (not the actual error found):
- **Control deficiency** — minor; managed internally.
- **Significant deficiency (SD)** — important enough to merit attention of those charged with governance.
- **Material weakness (MW)** — a **reasonable possibility** that a **material** misstatement won't be prevented/detected. Requires disclosure; sinks the ICFR opinion.

## Hands-on — step by step

Take **procure-to-pay (P2P)**, purchase-order approval.

1. **Understand the process (narrative).** "All POs above ₹5,00,000 require Finance Head e-approval in SAP before the PO is released to the vendor."
2. **Identify the risk / WCGW.** Unauthorised or over-budget purchases are committed → overstated expenses/liabilities; assertions hit = **occurrence, authorisation, accuracy**.
3. **Identify the control.** "SAP configuration blocks release of any PO > ₹5,00,000 until the Finance Head applies electronic approval (release strategy)." This is **preventive, automated (IT-dependent), transactional**.
4. **Test design — walkthrough.** Pick one PO for ₹6,20,000. Trace: requisition → SAP flags for release → Finance Head approves → PO released. Confirm the config threshold in SAP (t-code OMGS / release strategy). Conclusion: **designed effectively**.
5. **Test operating effectiveness.** Transactional automated control, so if configuration is stable you can test the **automated logic once** plus a sample of approvals. Pull the population of FY26 POs > ₹5,00,000 (say 480). For the *manual approval* element sample **25**; for the *automated block* attempt to release **1** unapproved test PO in a QA client and confirm the system blocks it.
6. **Perform the test.** For each of the 25: agree approver = Finance Head (not the requisitioner — **segregation of duties**), approval **before** release date, amount matches. Record attributes in a testing workpaper.
7. **Note exceptions.** Suppose 1 of 25 was approved by a delegate whose delegation lapsed. That's an **exception** — investigate: was it a one-off or systemic? Extend sample if needed.
8. **Evaluate the deficiency.** One lapsed-delegate approval on a ₹5,80,000 PO. Magnitude below materiality, compensating monthly budget-variance review exists → grade **control deficiency** (not SD/MW). Document rationale.

## The output

**Sample RCM row:**

| Ref | Process | Risk / WCGW | Assertion | Control description | Type | Freq | Owner | Design test | Operating test | Result |
|---|---|---|---|---|---|---|---|---|---|---|
| P2P-03 | Procure-to-Pay | Unauthorised PO > ₹5L released | Occurrence, Authorisation | SAP release strategy blocks PO >₹5,00,000 until Finance Head e-approval | Preventive / Automated (IT-dependent) | Per transaction | Finance Head | Walkthrough of PO #45012345 (₹6.2L) | 25 approvals + 1 QA block test | 1 exception (lapsed delegate) → control deficiency |

**Testing workpaper conclusion (extract):** "Design: Effective. Operating: 24/25 attributes passed; 1 exception due to expired delegation. Root cause: delegation register not updated. Severity: Control Deficiency — magnitude < materiality (₹X), compensating budget-variance review operating. Remediation: automate delegation expiry alerts. Retest Q3."

**Management attestation (India IFC):** Directors' Responsibility Statement, s.134(5)(e): "…the directors had laid down internal financial controls to be followed by the company and that such internal financial controls are **adequate and were operating effectively**." Auditor issues a separate IFCoFR opinion under s.143(3)(i).

## Checks, gotchas & red flags
- **Severity is based on *potential*, not the error you happened to find.** A clean sample doesn't downgrade a badly designed control.
- **IT-dependent manual controls need both halves tested** — the report/GITC integrity *and* the human review. Testing only the review is the #1 miss.
- **Segregation of duties (SoD):** the approver must not be the initiator, and the preparer must not be the reviewer. An approver approving their own request voids the control.
- **General IT Controls (GITCs)** — access, change management, backups — underpin every automated control. Weak GITCs can escalate an application-control finding to pervasive.
- Don't confuse **SD vs MW**: MW = *reasonable possibility of a material misstatement*. If it could hide something material, it's MW regardless of whether anything was actually misstated.
- **Rollover / roll-forward:** interim testing needs roll-forward procedures to year-end.

## Interview drill
**Q1. Difference between design and operating effectiveness — and how you test each?** Design asks whether the control, *if operating*, would prevent or detect a material misstatement; you test it with a **walkthrough** (trace one item end to end). Operating asks whether it *actually functioned consistently over the period*; you test a **sample** of occurrences against defined attributes. A control can be well-designed but fail operationally, or operate perfectly yet be poorly designed — both must pass.

**Q2. When does a deficiency become a material weakness?** When there's a **reasonable possibility** that a **material** misstatement of the financials would not be prevented or detected on a timely basis. It's about potential magnitude and likelihood, not the actual error size — and compensating controls can reduce severity. An SD merely warrants governance attention; an MW must be disclosed and negates a clean ICFR opinion.

**Q3. You're testing a control where a manager reviews a system-generated exception report. What must you test?** Both layers: (1) the **integrity of the report** — that it's complete and accurate, which depends on GITCs and the report logic; and (2) the **review itself** — evidence the manager investigated exceptions and followed up, not just signed. Testing only the signature misses that the underlying data could be wrong.

## Learn/practise (free)
- **COSO 2013 Framework executive summary** (free PDF) — memorise the 5 components/17 principles.
- **PCAOB AS 2201** and **SEC/PCAOB** guidance — free online; the definitive US source on ICFR and deficiency severity.
- **ICAI Guidance Note on Audit of Internal Financial Controls over Financial Reporting** — free, India-specific, with sample RCMs and test formats.
- Rehearse by building an **RCM in Excel** for one process you know (P2P, O2C, R2R): columns = process, risk, assertion, control, type, frequency, test procedure, sample, result. Then write a mock testing workpaper with a planted exception and grade its severity — that's exactly the deliverable a controls team wants to see.
