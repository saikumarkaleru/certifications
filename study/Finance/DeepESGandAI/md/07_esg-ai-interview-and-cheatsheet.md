# ESG & AI Interview Drills + Cheat-Sheet

## What you'll be able to do

You'll be able to put your ESG and AI knowledge on a resume **honestly** (no inflated "AI/ML expert" claims that collapse in five minutes), and answer the exact ESG/AI questions an India analyst / GCC / compliance / treasury interviewer throws in 2026: explain BRSR and its Core, define Scope 1/2/3 with a worked example, describe a concrete finance AI use case end-to-end, and enumerate AI risks with controls. You'll walk out with a one-page cheat-sheet — frameworks, emission scopes, tools, and certifications — you can revise the night before.

## The essentials

**Positioning honestly.** Match the claim to the evidence:

| If you did… | Say this | Don't say |
|---|---|---|
| Read BRSR, built a disclosure map | "Familiar with BRSR structure and BRSR Core KPIs" | "Led ESG reporting" |
| Built a RAG demo / used Copilot | "Built a RAG proof-of-concept; use Copilot for FP&A drafting" | "AI/ML engineer" |
| Computed a carbon estimate in Excel | "Can compute Scope 1/2 from activity data" | "Carbon accounting specialist" |

Interviewers respect a precise junior claim over a vague senior one. State the tool, the task, the dataset, and that you verify outputs.

**ESG core facts (India, 2026):**
- **BRSR** = Business Responsibility & Sustainability Report; mandatory for the **top 1,000 listed companies by market cap** (SEBI), filed with the annual report. Structured on the **9 NGRBC principles**.
- **BRSR Core** = a subset of key ESG KPIs with **reasonable assurance** required, being phased by market-cap tranche; includes **value-chain** disclosures (phased, comply-or-explain).
- **Greenhouse-gas Scopes (GHG Protocol):**
  - **Scope 1** — direct emissions you own/control (company boilers, vehicles, generators).
  - **Scope 2** — indirect from **purchased** electricity/heat/steam.
  - **Scope 3** — all other value-chain emissions (purchased goods, business travel, product use, investments) — usually the largest and hardest.
- **Global frameworks:** **GRI** (impact/stakeholder view), **ISSB IFRS S1 (general) & S2 (climate)** — the converging global baseline, **TCFD** (folded into ISSB), **CDP** (disclosure platform), **SASB** (industry metrics, now under ISSB), **EU CSRD/ESRS** (EU's mandatory regime — relevant to Indian firms in EU supply chains).

**AI facts:** LLM = language engine, not calculator; **RAG** grounds answers in your documents with citations; **agents** plan and call tools (keep humans on money-moving steps); **governance** = model risk, hallucination control, data privacy (DPDP Act), and the **EU AI Act** risk tiers (unacceptable / high / limited / minimal).

## Hands-on — step by step (a worked Scope 1+2 calc)

A small unit's FY26 activity data:
- Diesel in generators: **10,000 litres**
- Company cars petrol: **5,000 litres**
- Grid electricity: **200,000 kWh**

Emission factors (illustrative — always use the current CEA/India GHG Program / DEFRA factor):
- Diesel ≈ **2.68 kg CO₂e / litre**
- Petrol ≈ **2.31 kg CO₂e / litre**
- India grid ≈ **0.71 kg CO₂e / kWh** (CEA average — verify the year's value)

**Scope 1** (direct combustion):
- Diesel: 10,000 × 2.68 = **26,800 kg**
- Petrol: 5,000 × 2.31 = **11,550 kg**
- Scope 1 = 26,800 + 11,550 = **38,350 kg = 38.35 tCO₂e**

**Scope 2** (purchased electricity, location-based):
- 200,000 × 0.71 = **142,000 kg = 142.0 tCO₂e**

**Total Scope 1+2 = 180.35 tCO₂e.** Scope 3 (say business travel, purchased goods) would be estimated separately and typically dwarfs this.

In Excel: one column of activity data × a factor column, `=SUMPRODUCT(activity, factor)/1000` to get tonnes. That's the whole mechanic — the difficulty is sourcing correct factors and complete activity data, and getting assurance-ready evidence.

## The output

A resume ESG/AI block that survives scrutiny:

> **ESG & AI (finance):** Familiar with SEBI BRSR structure and BRSR Core KPIs; can compute Scope 1 & 2 emissions from activity data in Excel and map disclosures to GHG Protocol / ISSB S2. Working knowledge of GenAI for FP&A — Copilot-assisted variance commentary and DAX; built a RAG proof-of-concept answering questions over a policy PDF with source citations. Aware of AI-governance and EU AI Act risk tiers; verify all AI outputs against source.

And the interview cheat-sheet (below) folded into your revision.

## Cheat-sheet

**ESG frameworks**

| Framework | Owner | Point |
|---|---|---|
| BRSR / BRSR Core | SEBI | India mandatory (top 1,000); Core = assured KPIs + value chain |
| NGRBC (9 principles) | MCA | The backbone BRSR maps to |
| GRI | GRI | Impact on stakeholders/environment |
| ISSB IFRS S1/S2 | IFRS Foundation | Global baseline; S2 = climate (absorbs TCFD) |
| CSRD / ESRS | EU | EU mandatory; double materiality |
| CDP | CDP | Disclosure platform (climate/water/forests) |

**GHG Scopes:** 1 = own combustion; 2 = bought energy; 3 = value chain (up + downstream).

**AI toolkit:** LLM (draft/summarise, not calculate) · Copilot (Excel/Power BI/M365) · RAG (grounded, cited answers) · Agents (plan + act, human-in-loop) · Vector DB (embeddings store).

**AI risks → controls:** hallucination → RAG + citations + verify · privacy (DPDP/MNPI) → enterprise instance + residency · model risk → validation/monitoring/owner · autonomy → maker-checker + least privilege · regulation → EU AI Act risk tiers.

**Certifications worth naming:** GARP **SCR** (Sustainability & Climate Risk); CFA Institute **Certificate in ESG Investing**; **GRI Certified**; for AI, Microsoft **AI-900 / DP-900**, and vendor GenAI badges. Your **NISM RA** and CA-inter already signal core finance rigour.

## Checks, gotchas & red flags

- **Wrong emission factor / year.** Factors change annually and by region; a stale India grid factor is the classic error. Cite the source and year.
- **Unit slips.** kg vs tonnes (÷1000), kWh vs MWh — mislabelled units are the most common Scope-2 mistake.
- **Scope 2 double-count / method.** Location-based vs market-based are different methods; don't mix them.
- **Over-claiming AI skill.** Saying "ML engineer" invites a coding grill you'll fail. Claim exactly what you built.
- **BRSR scope error.** It's the top 1,000 *listed* firms — not all companies, not by turnover. Know Core's assurance and value-chain phasing.
- **Confusing ISSB/TCFD/GRI.** ISSB serves investors (enterprise value); GRI serves broader stakeholders (impact). Different lenses, not rivals.

## Interview drill

**Q1: "Explain BRSR and BRSR Core."**
A: BRSR is SEBI's mandatory Business Responsibility & Sustainability Report for the top 1,000 listed companies, filed with the annual report and structured on the nine NGRBC principles covering ESG performance. BRSR Core is a defined subset of key ESG KPIs that require *reasonable assurance*, phased in by market-cap tranche, and it extends to value-chain disclosures on a comply-or-explain basis. The intent is comparable, assured, decision-useful ESG data rather than narrative-only reporting.

**Q2: "What's the difference between Scope 1, 2 and 3? Give an example."**
A: Scope 1 is direct emissions from sources you own or control — say diesel burned in our generators. Scope 2 is indirect emissions from energy we purchase — our grid electricity. Scope 3 is everything else in the value chain, upstream and downstream — purchased goods, business travel, product use, investments. For our unit, 10,000 L diesel at ~2.68 kg/L is ~27 tonnes of Scope 1; 200,000 kWh at ~0.71 kg/kWh is ~142 tonnes of Scope 2. Scope 3 is usually the biggest and hardest to measure because it depends on suppliers and customers.

**Q3: "Give me one AI use case in finance and its main risks."**
A: A RAG assistant over our policy library — employees ask "is lounge access reimbursable?" and it answers only from the policy with the clause cited. Risks: hallucination if retrieval misses the right section (mitigate with citation + a "not specified" fallback and accuracy testing), data privacy since policies may touch personal data (keep it on an enterprise, data-resident instance under the DPDP Act), and governance — an owner, monitoring, and logs so it passes audit. If we ever let it *act*, like drafting a claim, the human still submits — no autonomous money movement.

## Learn/practise (free)

- **BRSR:** read a real filing — download any top-500 company's BRSR from BSE/NSE and trace the 9 principles and Core KPIs.
- **GHG Protocol:** the free Corporate Standard PDF + free GHG calculation tools; India GHG Program / CEA CO₂ baseline database for factors.
- **ISSB:** IFRS Foundation's free IFRS S1/S2 overview pages.
- **EU AI Act:** the EU "AI Act Explorer" (free) for risk tiers.
- **AI:** Microsoft Learn AI-900 path (free); build the policy-RAG demo from Chapter 6.
- **Rehearsal:** record yourself answering the three drills in under 90 seconds each; do the Scope 1+2 Excel calc from scratch until units and factors are automatic. That combination — a clean carbon calc plus an honest AI story with a working demo — is exactly what differentiates a credible 2026 finance candidate.
