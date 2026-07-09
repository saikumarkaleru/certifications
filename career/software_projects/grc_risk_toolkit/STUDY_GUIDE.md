# Study Guide — GRC Control & Risk-Register Toolkit

## 1. The 30-second pitch
> "I built a small GRC toolkit in Python that does the three things a risk analyst
> does day to day: it maintains a risk register scoring each risk by likelihood x
> impact, it maps those risks to ISO 27001 Annex A controls and flags coverage
> gaps, and it scores a vendor security questionnaire into a risk tier for
> third-party due diligence. It outputs an Excel workbook and a risk heat-map."

## 2. What GRC is (and why this matters)
Governance, Risk & Compliance = making sure an organisation identifies its risks,
puts controls in place, and can prove it to auditors. The risk register is the
central artifact; control frameworks (ISO 27001, SOC 2) are the checklist of
controls; vendor risk extends that to third parties who touch your data.

## 3. THE key answer — how you score a risk
> "Risk = Likelihood x Impact, each on a 1-5 scale, giving a 1-25 score I bucket
> into Low/Medium/High/Critical. That's the *inherent* risk. Controls reduce it to
> *residual* risk. Each risk has an owner, a treatment (mitigate / transfer /
> accept / avoid), and a remediation status I track to closure."

## 4. Walkthrough
- **Risk register** — a list of risks, each scored L x I, rated, and tagged with an
  owner, treatment and the ISO 27001 control it relates to; sorted by score.
- **Control coverage** — counts how many open High/Critical risks touch each Annex
  A theme (A.5 Organizational, A.6 People, A.7 Physical, A.8 Technological) and
  shows each theme's control status — a gap view for auditors.
- **Vendor questionnaire** — weighted yes/no security questions (MFA, encryption,
  ISO/SOC cert, incident response, pen testing...) scored to a % and a risk tier.
- **Heat map** — a 5x5 likelihood-vs-impact grid of risk counts.

## 5. Interview Q&A
**Q: What's the difference between inherent and residual risk?**
A: "Inherent is the risk before controls; residual is what's left after controls
are applied. GRC is about driving residual risk down to the organisation's
appetite."

**Q: What are the four risk treatments?**
A: "Mitigate (add controls), Transfer (insurance/contract), Accept (within
appetite), Avoid (stop the activity)."

**Q: What is ISO 27001 / SOC 2?**
A: "ISO 27001 is an international standard for an Information Security Management
System — Annex A lists the controls. SOC 2 is an attestation report on controls
around security, availability, confidentiality, etc. Both are how you demonstrate
security to customers and auditors."

**Q: How would you assess a third-party vendor?**
A: "Send a security questionnaire, weight the answers by importance (MFA,
encryption, certifications, breach SLA), score it into a tier, and require
remediation or contractual controls for gaps — that's the due-diligence review."

**Q: What is a risk register and who owns it?**
A: "A living inventory of risks with scores, owners, treatments and status. The
risk/GRC team maintains it; each risk has a business owner accountable for
remediation."

## 6. Vocabulary to know cold
Risk register, likelihood/impact, inherent vs residual risk, risk appetite, risk
treatment (mitigate/transfer/accept/avoid), ISO 27001 & Annex A, SOC 2, IAM /
least privilege / MFA, vendor/third-party risk, remediation, control.
