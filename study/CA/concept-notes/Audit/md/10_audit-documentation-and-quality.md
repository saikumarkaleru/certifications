<!-- v2-deep -->

# Chapter 10 — Audit Documentation & Quality Control

## 1. The Problem

Imagine an auditor signs a report on a company's financial statements. The report is one page. It says, in effect, *"I looked; the numbers are true and fair."* Two years later something goes wrong — a fraud surfaces, a bank that lent on the strength of those accounts loses money, a regulator opens an inquiry. Everyone now turns to the auditor and asks a single, brutal question:

> **"Prove you actually did the work."**

Here is the trap. Auditing is invisible. Unlike a builder who leaves a bridge, or a surgeon who leaves a scar, the auditor leaves almost nothing physical behind. The *judgement* happened inside the auditor's head. The *procedures* happened across weeks, spread over a team of juniors, seniors and a partner. The *conversations* with management evaporated the moment they ended. If the auditor cannot reconstruct what was done, then from the outside there is **no difference between a diligent audit and a lazy one** — both produce the same one-page report.

This is the first problem: **the work product is invisible, so its quality is unverifiable.**

The second problem sits on top of it. An audit is never done by one person in one sitting. A junior tests bank reconciliations, a senior reviews the junior, the manager reviews the senior, the engagement partner signs. Each layer must be able to *check* the layer below. But you cannot review what you cannot see. If the junior's work lives only in the junior's memory, the senior is reviewing nothing — merely trusting.

The third problem is the deepest. A firm may have a brilliant partner and a reckless one working under the same letterhead. The client, the shareholder, the regulator cannot tell them apart before the fact — they all buy "an audit by XYZ & Co." So the *firm itself* becomes the unit of trust, and the firm must somehow guarantee that **every** engagement, done by **anyone** in its name, meets a minimum standard. One weak audit stains the whole firm's signature.

So we have three linked failures of trust waiting to happen:

- The individual auditor cannot **prove** the work (evidence problem).
- The team cannot **review** the work (supervision problem).
- The firm cannot **guarantee** consistency across engagements (quality problem).

Every rule in this chapter exists to close one of these three gaps.

**A fourth, quieter problem — the passage of time.** Even a perfect audit, perfectly documented, is useless if the record vanishes before anyone needs it. Memory decays, staff leave the firm, laptops are wiped, and disputes surface *years* after the report. So beyond making the work visible, the architecture must make it *durable and retrievable* on demand. This is why "retention" and "safe custody" are not clerical afterthoughts but first-class rules — they answer the question *"and will the proof still exist when it is finally demanded?"* Keep this fourth gap in mind; the 7-year and 60-day numbers in Section 4 are its direct answer.

**Why this problem is uniquely acute for auditing (and not, say, for a bookkeeper).** A bookkeeper's output *is* the record — the ledger they produce is itself the evidence of their work. An auditor's output is an *opinion*, and an opinion is a mental state. The entire value of the profession rests on the reliability of an invisible mental act performed on someone else's records. That structural feature — a high-stakes conclusion with no natural physical trace — is what forces auditing, uniquely, to *manufacture* its own evidence of diligence. Documentation is that manufactured evidence. Understanding this makes the whole chapter feel inevitable rather than arbitrary.

## 2. The Core Idea

The core idea is disarmingly simple and worth stating as a single sentence you can carry through the whole chapter:

> **An audit opinion is only as good as the evidence that the audit was properly done — so the "record of the audit" is itself part of the audit.**

Two words do the heavy lifting: **documentation** and **quality control**. They are not two separate topics that happen to share a chapter. They are the *same* answer to the *same* problem, applied at two different levels.

- **Documentation** (SA 230) is how a single engagement makes its invisible work **visible and permanent**. It converts memory, judgement and conversation into a durable file that a stranger could pick up and understand.

- **Quality control** (SA 220 at the engagement level, and **SQC 1** at the firm level) is the system that makes sure the documented work is actually *good* — that competent people did it, that it was reviewed, that independence was protected, that difficult judgements got a second set of eyes.

The mental model to hold: **documentation is the evidence; quality control is the process that the evidence must record.** Quality control says *"a review must happen."* Documentation says *"and here is the proof it happened."* They interlock. A review that is not documented might as well not have occurred (nobody can prove it). Documentation of a process that has no quality-control requirement is just paperwork. Together they answer *"prove you did the work, and prove the work was good."*

Notice the recurring auditing DNA here: audit exists to solve the **trust/agency problem** between management (who prepare the accounts) and users (who rely on them). The auditor is the trusted intermediary. But *who audits the auditor?* Documentation and quality control are the profession's answer — they make the auditor's own work reviewable, so that the chain of trust does not simply dead-end at "trust me."

**A sharper way to see the interlock — the four-way "prove it" matrix.** The exam rewards students who can place any rule on this grid instantly:

| What must be proved | Whose job | Instrument |
|---|---|---|
| *That* the work was done | Individual auditor | SA 230 (documentation) |
| That *this* engagement's work was good | Engagement partner | SA 220 |
| That *every* engagement's work is consistently good | The firm | SQC 1 |
| That a *high-stakes* opinion was independently checked | An outside-the-team reviewer | EQCR |

Every requirement in Section 4 drops into exactly one of these rows. When a problem statement confuses you, ask "*which row is this testing?*" and the applicable standard resolves itself.

**The "documentation is a verb, then a noun" idea.** Beginners think documentation is filing paper *after* the audit. It is not. It is a *contemporaneous act* — you document *as* you perform, because the standard of proof it must meet (an outsider reconstructing your reasoning) can only be met while the reasoning is fresh. The noun (the audit file) is merely the accumulated residue of the verb. This distinction underlies the whole "assembly is not new work" rule later: by assembly time, the *documenting* is essentially over; only the *collating* remains.

## 3. Why It's Built This Way

Before the technical content, understand *why* the architecture looks the way it does. Every design choice is a response to a specific risk.

**Why not just trust the auditor's word?**
Because the auditor has a subtle conflict. The auditor is *paid by the audited* (the company pays the audit fee), and the auditor's own reputation is on the line. When something goes wrong, there is every incentive to say *"of course I checked that"* after the fact. A contemporaneous, dated, un-editable-after-assembly file removes the temptation and the ambiguity. The file speaks; the auditor's later memory does not have to.

**Why demand a specific standard of documentation ("experienced auditor with no prior connection")?**
Because a private shorthand only the preparer understands proves nothing to a reviewer or a court. The benchmark forces the file to be self-explanatory to an *outsider*. This is the single most tested idea in SA 230 and the reason for its exact wording.

**Why put quality control at *two* levels (firm and engagement)?**
Because the two risks are different. A single engagement can go wrong because *that* team cut corners — so you need engagement-level control (SA 220): a partner responsible for *this* audit. But engagements can *systematically* go wrong because the *firm* hires badly, trains badly, or tolerates independence breaches — so you need firm-level control (SQC 1): policies that apply to *all* engagements. Fixing one level cannot fix the other. A great partner cannot save a rotten firm; great firm policies cannot save an engagement where the partner ignores them.

**Why an *independent* second review (EQCR) for high-risk engagements?**
Because the engagement partner is the very person whose judgement is under stress on a tough call — self-review bias means the person who made a decision is the worst-placed to spot its flaw. For listed companies and other high-risk cases, the profession inserts a reviewer who was *not* on the engagement, precisely so the second opinion is genuinely second.

**Why fixed retention periods?**
Because disputes surface *late*. Litigation, regulatory inquiry, tax reassessment — these often arrive years after the report. If the file is destroyed, the auditor is defenceless and the public-interest record is gone. But keeping everything forever is costly and pointless. So the profession fixes a period long enough to cover the realistic tail of disputes and no longer.

**Why a fixed *assembly* window (and why so short — 60 days)?**
Because an "open" file is a dangerous file. As long as the file can still be added to freely, the auditor can retroactively strengthen weak areas after seeing how things played out — the essence of hindsight-driven backdating. Yet slamming the file shut the instant the report is signed is impractical: real administrative collation (indexing, cross-referencing, discarding superseded drafts, obtaining final signed representations already agreed) genuinely takes days. So the profession grants a *short, bounded* window for administration only, then locks the file. Sixty days is long enough to collate, short enough that no meaningful "new audit" can masquerade as "assembly."

**Why make the file the auditor's *property* rather than the client's, when the client pays?**
Because the file's whole function is to let the auditor defend an *independent* opinion — potentially *against* the client. If the client owned the file, the client could withhold or destroy the very evidence the auditor needs to answer a regulator, and could pressure the auditor by threatening file access. Ownership by the auditor keeps the accountability instrument in the hands of the accountable party. (This is also why the client's payment of the fee does *not* transfer ownership — the fee buys an opinion, not the auditor's private evidence of diligence.)

**Why house documentation, assembly and retention *inside* SQC 1's Element 5 rather than leaving them to individual auditors?**
Because a rule that depends on each individual's discipline fails silently and invisibly. By making it *firm policy*, the obligation acquires an owner (firm leadership), a monitoring mechanism (Element 6), and consequences. The firm — an institution that outlives any individual — becomes the guarantor that files survive staff turnover.

Hold this frame: **documentation and quality control are risk-management architecture, not bureaucracy.** Each rule below maps to a risk you can now name.

## 4. Full Technical Content

This is the exam-complete core. Every requirement is wrapped in the risk it counters. The four pillars are: **SA 230** (documentation), **SA 220** (engagement quality control), **SQC 1** (firm quality control), and **EQCR** (the independent review).

### 4.1 SA 230 — Audit Documentation

**What "audit documentation" means.** SA 230 defines it as the record of (a) audit procedures performed, (b) relevant audit evidence obtained, and (c) conclusions the auditor reached. The old term was "working papers"; the file as a whole is the **audit file**. This tri-part definition is deliberate — it forces the file to answer *what did you do, what did you find, and what did you conclude*, which are exactly the three things a sceptic will interrogate.

**Two defined terms the examiner separates.** SA 230 distinguishes:
- **Audit documentation** — the *record* (working papers) of procedures, evidence and conclusions.
- **Audit file** — one or more folders or storage media, *physical or electronic*, containing the records that comprise the documentation for a *specific* engagement.

The distinction matters because "audit file" is the *unit* to which the assembly and retention deadlines attach. The medium is explicitly technology-neutral: a fully electronic file is as valid as paper, provided integrity, safe custody and retrievability are preserved (which is exactly why SQC 1 lists those attributes — see 4.3).

**The purpose (the "why" is examinable).** SA 230 lists why documentation matters, and each maps to a Section-1 problem:

| Purpose of documentation | Risk it counters |
|---|---|
| Evidence of the basis for the auditor's opinion | "Prove you did the work" — defends the opinion |
| Evidence the audit was planned and performed per SAs and law | Regulatory/peer-review challenge |
| Enables the engagement team to be directed, supervised, reviewed | Supervision problem — the team can check itself |
| Retains a record of matters of continuing significance to future audits | Efficiency and continuity across years |
| Enables quality control reviews and inspections (internal and external) | Firm-level and regulatory oversight |
| Enables the conduct of external inspections per legal/regulatory requirements | NFRA / peer review / QRB inspection |
| Assists in defending against litigation | The late-dispute problem |
| Assists in planning and performing the audit efficiently | Duplication and re-work avoided |
| Discharges accountability of the engagement team | Fixes responsibility on named individuals |

**The governing standard — the benchmark of "enough."** This is the heart of SA 230 and the most common exam hook. Documentation must be sufficient to enable an **experienced auditor, having no previous connection with the audit, to understand**:

- (a) the **nature, timing and extent** of the audit procedures performed (the "what and how much");
- (b) the **results** of those procedures and the audit evidence obtained;
- (c) **significant matters** arising, the **conclusions** reached, and **significant professional judgements** made in reaching those conclusions.

Unpack why each phrase exists. *"Experienced auditor"* — so the standard is not "understandable to the person who wrote it" (that proves nothing) but understandable to a competent peer. *"No previous connection"* — strips away all the context that lived in the original auditor's head; the file must stand alone. *"Nature, timing and extent"* — the three dimensions of any procedure; a file that says "checked sales" without saying *how, when, and how much* is worthless. This benchmark is the operational meaning of "sufficient documentation."

**Who exactly is the "experienced auditor"?** SA 230 defines this hypothetical person precisely — an individual (whether internal or external to the firm) who has **practical audit experience** *and* a **reasonable understanding** of (i) audit processes, (ii) the SAs and applicable legal/regulatory requirements, (iii) the business environment in which the entity operates, and (iv) auditing and financial reporting issues relevant to the entity's industry. Note two subtleties the examiner exploits. First, "no previous connection with *this* audit" does **not** mean "knows nothing about the industry" — the benchmark reader is a *skilled* stranger, not an ignorant one. So you need not spell out generic professional knowledge the reader already has; you need only supply what is *specific to this engagement*. Second, this dual nature (skilled but disconnected) is what lets the file be *concise yet complete* — you calibrate detail to what a competent peer would *not* already know.

**What must be recorded to identify the work (the identifiability rule).** Because the file must be reconstructable, SA 230 requires the auditor to record:

- **who performed** the work and the **date** it was completed;
- **who reviewed** the work, the **date**, and the **extent** of review.

Reason: this is the audit trail of the *supervision* itself. It proves not just that testing happened but that the review layers actually operated. Note the subtle "extent" requirement on review — recording *that* it was reviewed is not enough; the file shows *how much* was reviewed, because a rubber-stamp signature and a substantive review look identical without it.

**Documenting identifying characteristics of items tested.** When recording procedures, the auditor records the **identifying characteristics** of the items tested — e.g., for a sample of purchase orders, the specific PO numbers and range; for a walkthrough, the specific transaction reference. Reason: it must be possible to *re-perform* or *trace back* to the exact items, otherwise "we tested a sample" is unfalsifiable. Worked micro-examples of "identifying characteristics" the examiner may expect:

| Procedure / population | Identifying characteristic to record |
|---|---|
| Sample of purchase orders selected for testing | The PO numbers *and* the range from which selected (e.g., "POs raised 1 Apr–31 Mar, nos. 10001–14567; sample nos. …") |
| Systematic sample with a random start | The *source*, the *starting point*, and the *sampling interval* (e.g., "every 125th voucher from receipt no. 4051") |
| Inquiry procedure | The *date* of the inquiry, the *name and designation* of the person, and the topic |
| Observation of a process | The process observed, the *date*, and *who* was performing it when observed |

**Significant matters and professional judgement.** The auditor must document discussions of significant matters with management, TCWG and others, including *when* and *with whom*. Reason: oral discussions evaporate; the significant, contentious, judgemental parts of an audit are exactly where later disputes cluster, so those are the parts that most need a written record. SA 230 also flags examples of *significant matters*: matters giving rise to significant risks; results of procedures indicating a possible material misstatement or a need to revise the auditor's prior risk assessment; circumstances causing significant difficulty in applying necessary procedures; and findings that could lead to a modification of the opinion or an Emphasis of Matter paragraph.

**Oral explanations are not documentation.** A precise, examinable point: oral explanations by the auditor, *on their own*, do **not** represent adequate support for the work performed or conclusions reached — but they **may** be used to *explain or clarify* information contained in the documentation. In other words, talking cannot *substitute* for the file, though it can *illuminate* it. A file that "would have been fine if the auditor had been available to explain it" fails, because the whole point is that the file must stand without the auditor present.

**Departure from a relevant requirement (the exception log).** If, in exceptional circumstances, the auditor departs from a *relevant requirement* of an SA, the auditor must document **how the alternative procedures performed achieve the aim of that requirement, and the reasons for the departure.** Reason: SAs are mandatory; a documented, reasoned departure is accountable, an undocumented one is a violation. Note the tight scope: this concerns a *relevant* requirement (one that applies because the circumstances it addresses exist) that the auditor judges *not relevant* or impossible to meet — it is **not** a licence to skip requirements at will. If a requirement is *conditional* and the condition is absent, the requirement simply does not apply and no "departure" documentation is triggered at all.

**Matters arising *after* the date of the auditor's report.** If, in exceptional circumstances, the auditor performs new or additional procedures or draws new conclusions *after* the report date, the auditor documents: the circumstances, the new procedures/evidence/conclusions, and *when and by whom* the file changes were made and reviewed. Reason: this is the anti-backdating rule — it prevents silently "fixing" the file after signing. Link this to SA 560 (Subsequent Events): the *trigger* for such after-the-fact work is usually a fact that becomes known after the report date that, had it been known then, might have changed the report. SA 230 governs the *documentation* of that work; SA 560 governs *whether and how* the auditor must act.

**Assembly of the final audit file.** SQC 1 (and SA 230 by reference) requires the auditor to **assemble the final audit file on a timely basis after the date of the auditor's report.** The time limit fixed by SQC 1 is **ordinarily not more than 60 days** after the date of the auditor's report. Reason: assembly is an *administrative* completion — collating, sorting, discarding superseded drafts — **not** a window to do new audit work. Fixing 60 days prevents the file from staying "open" indefinitely (which would let the auditor keep changing conclusions).

**What "administrative" assembly actually includes (and excludes).** Permissible during the ≤60-day window: deleting or discarding superseded documentation; sorting, collating and cross-referencing working papers; signing off on completion checklists relating to the assembly process; and documenting evidence the auditor *obtained, discussed and agreed with relevant team members before the date of the report*. **Not** permissible: performing new audit procedures, drawing new conclusions, or obtaining fresh evidence about matters not resolved before the report date. The bright line is the *report date*, not the assembly deadline — anything substantive must have been *concluded* by the report date; assembly only tidies its record.

> **Critical distinction (heavily tested):** *before* the report date the auditor can still do audit work; the **assembly period (≤60 days after)** is only for administrative completion. After assembly, the auditor **must not delete or discard** documentation before the end of the retention period, and any change/addition must be documented with who, when, why (as above).

**Retention period.** SQC 1 requires that the retention period for audit engagements is **ordinarily no shorter than seven years from the date of the auditor's report** (or, if later, the date of the group auditor's report). Reason: covers the realistic tail of litigation, regulatory inquiry and inspection. (Note the interaction with law — see Section 7; **confirm the exact interplay with Companies Act record-retention in current ICAI material.**)

**Ownership and confidentiality (a precise, examinable rule).** Working papers are the **property of the auditor**, not the client — even though the client pays the fee. The auditor may, at their discretion, make portions or extracts available to the client, but this is a courtesy, not a right; the client cannot demand them. Simultaneously, the auditor owes a duty of **confidentiality** over the file (client information within it must not be disclosed without authority or legal compulsion) and must keep it in **safe custody**. Hold both halves together: the file belongs to the auditor *and* the auditor must guard the client's confidences inside it.

**Form, contents and extent — what drives "how much."** SA 230 says the extent of documentation is a matter of professional judgement influenced by: size and complexity of the entity, nature of procedures, identified risks of material misstatement, significance of evidence obtained, nature and extent of exceptions identified, and the need to document a conclusion not readily determinable from the work itself. The guiding principle: **document enough for the "experienced auditor" benchmark to be met — no more, no less.** Reason: over-documentation wastes cost and buries the significant; under-documentation fails the proof test.

**What need NOT be documented (a favourite trap).** The auditor need not document *every* matter considered or *every* professional judgement made — only the significant ones. Superseded drafts, notes reflecting incomplete or preliminary thinking, duplicate documents, and copies of documents corrected for typographical errors need not be retained in the final file. Reason: the file records *conclusions and their basis*, not the messy scaffolding used to reach them. A related nuance: the auditor also need not include *superseded* versions of documents once the final version is on file — but must not discard the final documentation of a *significant matter* merely because it is unflattering.

### 4.2 SA 220 — Quality Control for an Audit of Financial Statements (Engagement Level)

SA 220 sits *inside* the firm's overall system (SQC 1) and asks: for **this specific engagement**, how is quality delivered? The unifying idea: **the engagement partner is responsible for the overall quality of the engagement** and must take the lead on it. Each requirement below is the partner discharging a specific quality risk.

**The reliance principle (structural link to SQC 1).** SA 220 is built on a foundational assumption: *the firm already operates an SQC 1 system.* Therefore the engagement partner is generally **entitled to rely** on the firm's system (e.g., that HR policies produced competent staff, that independence-monitoring caught firm-level threats) **unless information indicates otherwise.** This "rely unless red-flagged" rule is heavily testable — it explains why the partner does not personally re-verify every firm policy, yet remains accountable the moment contrary information appears.

- **Leadership responsibility for quality on the engagement.** The engagement partner sets the tone; quality is not delegated away. Risk: without a single accountable owner, quality falls between chairs.

- **Relevant ethical requirements, including independence.** The partner must remain alert, throughout the engagement, to evidence of non-compliance with ethics, and specifically form a conclusion on **independence** — considering threats, safeguards, and the firm's independence information. Risk: an audit by a non-independent auditor is worthless (the whole point of audit is an *independent* check).

- **Acceptance and continuance of the client relationship.** The partner must be satisfied that appropriate procedures were followed and that the conclusions reached (about integrity of the client, competence and capabilities, and ability to comply with ethics) are appropriate. If the partner obtains information that would have caused the firm to decline the engagement had it been available earlier, the partner must communicate it promptly to the firm so that necessary action is taken. Risk: some clients should never be accepted; taking on a dishonest or infeasible client poisons the engagement from the start.

- **Assignment of engagement teams.** The partner must be satisfied the team (including any auditor's experts *not* part of the team) collectively has the **competence and capabilities** to perform the engagement and prepare an appropriate report. Risk: putting unqualified staff on a complex audit guarantees failure.

- **Engagement performance — direction, supervision and review.** The partner directs the team, supervises the work, and reviews it. The rule: **review by more experienced team members of work done by less experienced members.** The partner need not review *all* documentation but must review — on a timely basis at appropriate stages — significant judgements, significant risks, and other matters the partner considers important. Risk: the supervision problem from Section 1 — unreviewed junior work is unverified.

- **Consultation.** For difficult or contentious matters, the team must consult (internally or externally), and the partner must be satisfied that consultation happened, that the conclusion was agreed with the party consulted, and that the conclusion was **implemented**. Risk: a lone auditor over-confident on a hard technical point. Note the two-part test: agreement *and* implementation — consulting an expert and then ignoring the advice fails the requirement as surely as not consulting at all.

- **Engagement quality control review (EQCR).** For audits of listed entities (and other engagements the firm decides), the partner must ensure an EQCR is appointed, discuss significant matters with the reviewer, and **not date the report until the EQCR is completed** (detail in 4.4). Risk: self-review bias on high-stakes judgements.

- **Differences of opinion.** Within the team, or with the EQC reviewer or those consulted, differences must be resolved per firm policy, and the **report must not be dated until the matter is resolved.** Risk: unresolved dissent buried under a signature.

- **Monitoring.** The partner considers the results of the firm's monitoring process (and any deficiencies flagged) and whether they affect this engagement. Risk: firm-wide problems silently recurring on this file.

- **Documentation (SA 220's own doc requirements — links back to SA 230).** The partner documents: issues on ethical requirements and how resolved; conclusion on independence; conclusions on acceptance/continuance; and the nature, scope and conclusions of consultations. Risk: none of the above is provable unless recorded.

### 4.3 SQC 1 — Quality Control for Firms (Firm Level)

SQC 1 applies to **firms** performing audits, reviews of historical financial information, and other assurance and related services engagements. Its objective: the firm establishes and maintains a **system of quality control** giving reasonable assurance that (a) the firm and its personnel comply with professional standards and legal/regulatory requirements, and (b) reports issued are appropriate in the circumstances. The system rests on **six elements** — each answering a firm-wide risk.

**"Reasonable assurance," not absolute — and why.** SQC 1 promises *reasonable*, not *absolute*, assurance. This mirrors the inherent-limitations idea from SA 200: a system operated by humans, using judgement and sampling, cannot guarantee that no engagement will ever go wrong. The examiner tests whether students overclaim — a firm that fully complies with SQC 1 can *still* have an occasional deficient engagement, and that alone is not proof the system failed.

| # | SQC 1 element | Firm-level risk it addresses |
|---|---|---|
| 1 | **Leadership responsibilities for quality within the firm** (the "tone at the top") | If leadership prizes fees over quality, everyone follows; quality must be led from the top and not undercut by commercial pressure |
| 2 | **Ethical requirements** (integrity, objectivity, professional competence, confidentiality, professional behaviour) including **independence** | Firm-wide independence breaches — the firm must gather independence data, identify threats, apply safeguards, and enforce **rotation** where required |
| 3 | **Acceptance and continuance of client relationships and specific engagements** | Taking on clients the firm cannot serve competently, ethically, or that lack integrity |
| 4 | **Human resources** (recruitment, competence, career development, capabilities, performance evaluation, assignment of engagement teams) | Incompetent or under-resourced staff doing audits in the firm's name |
| 5 | **Engagement performance** (consistent quality, supervision, review, consultation, EQCR, differences of opinion, documentation, assembly & retention) | Inconsistent quality across engagements; this element *houses* the documentation/assembly/retention rules |
| 6 | **Monitoring** (ongoing consideration and evaluation of the firm's system, including periodic inspection of completed engagements) | The system decaying unnoticed — someone must audit the quality-control system itself |

**Leadership (Element 1) has a specific anti-commercial-pressure rule.** SQC 1 requires the firm's leadership to establish policies ensuring that its *commercial considerations do not override the quality of work performed*, and to assign management responsibilities so that commercial priorities cannot compromise quality. The examiner phrases this as scenarios where a managing partner ties promotions purely to fees generated — that arrangement breaches Element 1 because it structurally subordinates quality to revenue.

**Ethics (Element 2) — the specific machinery.** Beyond stating the five fundamental principles, SQC 1 requires the firm to obtain **written confirmation of compliance with independence** from all personnel required to be independent, **at least annually**. It also requires policies to identify and evaluate **familiarity threats** from long association, addressed via safeguards including **rotation** of senior personnel. Note the interaction: statutory rotation under the Companies Act (s.139(2)) is a *legal* overlay on top of this *professional* requirement.

Two of these elements deserve emphasis because they carry the specific rules examiners love:

**Element 5 (Engagement performance) is where the file lives.** SQC 1 mandates the firm to set policies on: completion of engagement documentation in a timely basis, the **assembly of the final file (≤60 days)**, the **confidentiality, safe custody, integrity, accessibility and retrievability** of documentation, and the **retention of documentation (≥7 years)**. Reason: the firm — not just the individual — must guarantee the file survives, stays confidential, and can be produced. A file that is lost, leaked, or tampered with fails its purpose. Memorise the five custody attributes as a set: **confidentiality, safe custody, integrity, accessibility, retrievability** — the examiner asks for them by name.

**Element 6 (Monitoring) is the "audit of the audit system."** The firm must appoint someone competent and with sufficient authority to take responsibility for monitoring, and must perform **cyclical inspection of at least one completed engagement per engagement partner.** Reason: without monitoring, a quality-control *system* is just a document nobody checks; the periodic inspection is how the firm discovers its own weak spots before a regulator does. Deficiencies found must be **evaluated** to determine whether they are (i) isolated instances or (ii) *systemic, repetitive or otherwise significant* requiring prompt corrective action — and then **communicated** to the relevant engagement partners with recommended remedial action. A single monitoring finding does not automatically mean an issued report was wrong; the firm must assess the *nature and pervasiveness* of the deficiency.

**Complaints and allegations — a monitoring sub-rule.** SQC 1 also requires the firm to establish policies to deal with **complaints and allegations** that work performed fails to comply with standards, or of non-compliance with the firm's own quality-control system. This is the "whistle-blowing / feedback" channel of the monitoring element and is occasionally tested as a distinct requirement.

**Documentation of the *system itself*.** Distinct from documenting engagements, SQC 1 requires the firm to *document* its quality-control policies and procedures and communicate them to personnel, and to retain documentation providing evidence of the *operation* of each element (e.g., independence confirmations, monitoring inspection results). A firm can breach SQC 1 not by acting badly but by failing to *evidence* that its system operates — the same "prove it" logic, one level up.

### 4.4 Engagement Quality Control Review (EQCR)

The EQCR is the sharpest instrument in the toolkit, so it gets its own treatment.

**What it is.** An EQCR is an **objective evaluation, by a reviewer who is *not* part of the engagement team**, of the significant judgements the team made and the conclusions reached in formulating the report. The reviewer is the **engagement quality control reviewer (EQC reviewer)** — a partner, other person in the firm, a suitably qualified external person, or a team of such persons, with sufficient and appropriate experience and authority, and who meets the required objectivity/independence.

**When it is mandatory.** For all audits of financial statements of **listed entities**. The firm's policies must also require an EQCR for **other engagements that meet the firm's criteria** for review (e.g., high public interest, unusual risk, unusual nature/circumstances). Reason: EQCR is expensive; it is targeted at the engagements where a wrong opinion does the most public damage.

**What the reviewer does.** The EQC reviewer performs an **objective evaluation** of: the significant judgements made by the team; the conclusions reached (especially the appropriateness of the report); discussion of significant matters with the engagement partner; review of the financial statements and the proposed report; review of selected working papers relating to significant judgements; and evaluation of the conclusions on independence.

**Criteria for *who* may be the reviewer (the objectivity safeguards).** SQC 1 sets guardrails so the review is genuinely independent:
- The EQC reviewer is **not selected by the engagement partner** in a way that compromises objectivity.
- The reviewer **does not participate** in the engagement during the period under review (beyond the review itself).
- The reviewer **does not make decisions for the engagement team** — the responsibility for the opinion stays with the engagement partner; the reviewer *evaluates*, it does not *take over*.
- The engagement partner may **consult** the reviewer, but consultation must **not compromise** the reviewer's eligibility to perform the review objectively.

This last point is a subtle exam favourite: heavy pre-review consultation can *disqualify* the intended reviewer, because they end up reviewing conclusions they helped form — recreating the very self-review bias EQCR exists to break.

**The timing rule (the key control).** The engagement partner **must not date the auditor's report until the EQCR is complete.** Reason: the whole value of a second review is that it happens *before* the opinion is locked in. A review after the report is signed cannot change the opinion and is therefore worthless as a control.

**Why the reviewer must be independent of the team.** Because the reviewer's job is to catch the *self-review bias* of the very people who made the judgements. If the reviewer were on the team, they would be reviewing their own decisions — the exact conflict the mechanism exists to break.

**EQCR is a *check on*, not a *replacement for*, the partner's own review.** The engagement partner must *already* have concluded that sufficient appropriate evidence supports the opinion *before* the EQC reviewer's work concludes. EQCR does not relieve the partner of responsibility — it adds a second gate, it does not substitute for the first. A scenario where a partner "leaves the hard judgements for the EQC reviewer to sort out" inverts the mechanism and is wrong.

```mermaid
flowchart TD
    A["Engagement is an audit of a listed entity or meets firm EQCR criteria"] --> B["Appoint an EQC reviewer who was NOT on the engagement team"]
    B --> C["Reviewer objectively evaluates significant judgements and conclusions"]
    C --> D["Reviewer reviews financial statements, proposed report and selected working papers"]
    D --> E["Reviewer evaluates the team conclusion on independence"]
    E --> F{"Are significant matters resolved and conclusions appropriate"}
    F -->|"No"| G["Resolve differences per firm policy and revisit the work"]
    G --> F
    F -->|"Yes"| H["EQCR complete"]
    H --> I["Only now may the engagement partner date the auditor report"]
```
*Figure 10.1 — The EQCR gate: the report cannot be dated until the independent review is complete.*

## 5. Applied Scenarios

Work these the way the exam frames them: identify the risk, then the requirement that answers it, then the conclusion.

**Scenario A — The confident senior with an empty file.**
CA Raghav, a senior on the audit of Meridian Ltd, tested the entire revenue cycle himself. His working paper says: *"Revenue tested, found correct."* Two years later NFRA inspects the file. The engagement partner insists the testing was thorough. *Was the documentation adequate?*

**Analysis.** No. Apply the SA 230 benchmark: could an **experienced auditor with no previous connection** understand the **nature, timing and extent** of procedures, their **results**, and the **conclusions**? "Revenue tested, found correct" reveals none of these — not *which* transactions (identifying characteristics), not *how* they were tested, not *how many*, not *what results* supported the conclusion. The work may well have been done, but SA 230's whole point is that undocumented work is *unprovable* work. The file fails, and the partner cannot defend the opinion. Additionally, there is no record of **who reviewed** the senior's work and **when** — the supervision trail is missing too. Note the trap variation: if Raghav offers to *explain verbally* what he did, that does **not** cure the defect — oral explanation cannot *substitute* for documentation (it may only *clarify* an already-adequate file).

**Scenario B — Fixing the file after signing.**
The auditor of Vault Finance Ltd signed the report on 15 May. On 10 July (56 days later), while assembling the file, a manager realises a key going-concern discussion with the CFO was never written up. She adds a memo dated 10 July recording the May conversation. Separately, on 20 August the auditor *learns of a new fact* about a lawsuit and performs additional procedures. *What are the documentation rules?*

**Analysis.** Two different things are happening. (1) The 10 July memo falls **within the ≤60-day assembly period** and is an **administrative completion** of documentation — permissible, provided it records the discussion that actually occurred *before the report date* and is not new audit work. It should note who added it and when. (2) The 20 August work is *after* the report date and involves **new procedures/conclusions after the report** — SA 230 requires documenting the **circumstances, the new procedures and evidence and conclusions reached, and when and by whom the changes were made and reviewed.** The auditor must **never delete** the original file contents. This is the anti-backdating architecture in action: the file grows transparently; it is never silently rewritten.

**Scenario C — The listed client and the tight deadline.**
Sterling Industries Ltd is listed. The engagement partner, under pressure from the audit committee to release results, wants to date and issue the report on 28 June. The EQC reviewer has raised a question on the impairment of goodwill and has not finished her review. The partner argues the EQCR can be "wrapped up next week." *Is this acceptable?*

**Analysis.** No — and this is the single hardest control in the chapter. Because Sterling is **listed**, an **EQCR is mandatory** (SA 220 / SQC 1). The rule is absolute: **the engagement partner must not date the auditor's report until the EQCR is complete.** Dating on 28 June with an open EQCR defeats the purpose of an independent pre-issuance review — a review that cannot change the opinion is no control at all. Moreover, the reviewer's open question on goodwill is precisely a **significant judgement**; if it amounts to a **difference of opinion**, firm policy for resolving differences applies and, again, the report is not dated until resolved. The deadline pressure is real but the sequence is non-negotiable: EQCR complete → then date the report.

**Scenario D — The firm with no monitoring (firm-level).**
A small firm has excellent partners but has never inspected any completed engagement, arguing "our partners are experienced, we don't need to." *Does the firm comply with SQC 1?*

**Analysis.** No. SQC 1 **Element 6 (Monitoring)** requires ongoing evaluation of the quality-control system, including **cyclical inspection of at least one completed engagement per engagement partner.** Competence of partners does not substitute for monitoring — monitoring is the mechanism by which the *firm* discovers whether its system is actually working. "Trust the partners" is exactly the un-checked trust the whole architecture is designed to replace.

**Scenario E — The retention shortcut (numerical).**
Orbit Textiles Ltd's audit report is dated **20 August 2021**. In **November 2027** — a little over six years later — the firm, short on storage, destroys the audit file. In **January 2028** a regulator opens an inquiry and demands the file. *Has the firm breached SQC 1, and by how much time?*

**Analysis and reconciliation.** Yes. Retention runs **≥ 7 years from the date of the auditor's report**, i.e., from 20 Aug 2021. Seven years ends on **20 August 2028**. The file was destroyed in November 2027 — roughly **9 months before** the minimum period expired. Self-check the arithmetic: 20 Aug 2021 + 7 yrs = 20 Aug 2028; Nov 2027 < Aug 2028, so destruction was premature. The consequence is exactly the Section-1 "late dispute" nightmare: the inquiry (Jan 2028) arrives *inside* the retention window, the auditor is now defenceless, and the destruction itself is a standalone SQC 1 breach independent of whether the original audit was good. **Examiner tweak:** if the report had instead been dated 20 Aug 2019 and the file destroyed in Nov 2027, count again — 20 Aug 2019 + 7 = 20 Aug 2026; Nov 2027 > Aug 2026, so retention would have been *satisfied* and no breach on that ground. The lesson: always anchor the count to the **report date**, not the financial-year-end or the date of destruction.

**Scenario F — Assembly window arithmetic and a substantive intruder (numerical).**
Nimbus Software Pvt Ltd's report is dated **30 September 2026**. The firm's SQC 1 policy adopts the "ordinarily not more than 60 days" assembly limit. (i) By what date must the final file be assembled? (ii) On **the 45th day** the engagement manager, while collating, discovers that the *revenue cut-off testing was never actually performed* and quietly performs it now, filing the results as part of "assembly." Is that valid?

**Analysis and reconciliation.** (i) 60 days from 30 Sep 2026: September has 30 days, so 30 Sep + 60 days lands on **29 November 2026** (October 31 + November 29 = 60 days after 30 Sep; verify: 1 Oct is day 1, 31 Oct is day 31, 29 Nov is day 60). So the file must be assembled **on or before 29 November 2026**. (ii) **Invalid.** Cut-off testing is a *substantive audit procedure*, not administrative collation. It should have been *concluded before the report date* of 30 Sep. Performing it on day 45 is **new audit work masquerading as assembly** — a direct breach of the assembly rule. Worse, it reveals the report may have been dated *without sufficient appropriate evidence* on revenue cut-off, so the real problem is that the opinion was issued prematurely. Correct treatment: this is not "assembly"; if a genuinely new matter emerged, it must be documented under the **after-the-report-date** rule (circumstances, new work, who/when), and the auditor must consider the implications for the *already-issued* opinion under SA 560. **The trap:** the 60-day window tempts students to treat *anything done within 60 days* as fine. The bright line is the *report date* for substance, the *60-day date* only for administration.

**Scenario G — Reviewer who consulted too much (EQCR eligibility).**
Zenith Pharma Ltd is listed. During the audit, the engagement partner repeatedly consults Partner K on the accounting for a complex licensing arrangement, and K effectively co-develops the team's conclusion. At year-end, the firm proposes to appoint **K as the EQC reviewer** because "K already knows the issue best." *Is this appropriate?*

**Analysis.** No. The efficiency argument is exactly backwards. Because K helped *form* the very conclusion on the licensing arrangement, appointing K as EQC reviewer would have K **reviewing K's own judgement** — reconstructing the self-review bias EQCR exists to eliminate. SQC 1's objectivity safeguards say consultation with the intended reviewer must **not compromise** the reviewer's eligibility; here it plainly does, at least on the significant licensing judgement. The firm should appoint a *different* eligible partner (or a suitably qualified external reviewer) who did not participate in forming the engagement's conclusions. **Tweak:** had K's consultation been on a *minor, non-significant* matter, K's eligibility might survive — the disqualifier bites where the consulted matter is one of the *significant judgements* the EQCR must evaluate.

## 6. Procedure & Documentation Summary

A compact operational walkthrough — the lifecycle of the file and the quality gates around it.

```mermaid
flowchart LR
    A["Perform procedures and record nature timing extent results and conclusions"] --> B["Record who performed and date and who reviewed and date and extent"]
    B --> C["Document significant matters judgements and discussions with management and TCWG"]
    C --> D["More experienced members review less experienced members work"]
    D --> E["Consult on difficult or contentious matters and implement conclusions"]
    E --> F{"Listed entity or meets firm criteria"}
    F -->|"Yes"| G["Complete EQCR before dating the report"]
    F -->|"No"| H["Engagement partner concludes on quality"]
    G --> H
    H --> I["Date and issue the auditor report"]
    I --> J["Assemble final audit file within 60 days administrative only"]
    J --> K["Retain file for at least 7 years with safe custody confidentiality and retrievability"]
```
*Figure 10.2 — Lifecycle of the audit file from procedure to retention, with the quality gates in sequence.*

The next diagram isolates the single most error-prone part of the timeline — the events *around and after* the report date — because the examiner concentrates fire there. Notice that the report date is the true bright line for *substance*, while the 60-day and 7-year marks govern only *administration* and *survival*.

```mermaid
flowchart TD
    A["All substantive audit work concluded"] --> B["Engagement partner satisfied sufficient appropriate evidence exists"]
    B --> C["EQCR complete if applicable and differences resolved"]
    C --> D["Report DATED — the bright line for substance"]
    D --> E["Assembly window opens — administrative collation only"]
    E --> F{"New fact learned or new procedure needed after report date"}
    F -->|"No"| G["Assemble final file within 60 days of report date"]
    F -->|"Yes"| H["Document circumstances new work and who did and reviewed it and when"]
    H --> I["Consider effect on the already issued opinion under SA 560"]
    I --> G
    G --> J["File locked — no deletion before retention ends"]
    J --> K["Retain at least 7 years from report date in safe custody"]
```
*Figure 10.3 — The report date is the bright line for substance while assembly and retention govern only administration and survival.*

**Documentation checklist (what a strong file contains):**

| Item | Requirement source | The "why" |
|---|---|---|
| Nature, timing, extent of procedures | SA 230 | Reconstructable by an outsider |
| Identifying characteristics of items tested | SA 230 | Re-traceable to exact items |
| Results and evidence obtained | SA 230 | Supports the conclusion |
| Significant matters, judgements, conclusions | SA 230 | Where disputes cluster |
| Discussions with management/TCWG — when, with whom | SA 230 | Oral record made durable |
| Who performed / who reviewed — names, dates, extent | SA 230 | Supervision trail |
| Departures from a relevant SA requirement — how alternative met the aim, why | SA 230 | Accountable, not a violation |
| Post-report changes — circumstances, new work, who/when | SA 230 | Anti-backdating |
| Conclusion on independence; ethics issues and resolution | SA 220 | Independence is the point of audit |
| Consultation nature, scope, conclusions | SA 220 | Proof hard calls got expert input |
| EQCR completion before report date (where applicable) | SA 220 / SQC 1 | Independent pre-issuance check |
| Final file assembled ≤ 60 days | SQC 1 | Administrative closure, not new work |
| Retention ≥ 7 years; safe custody, confidentiality, retrievability | SQC 1 | Survives the late dispute |
| Annual written independence confirmations from personnel | SQC 1 (firm) | Evidence the ethics element operates |
| Monitoring/inspection results and remedial actions | SQC 1 (firm) | Evidence the system audits itself |

## 7. Connections

Documentation and quality control are not an island — they thread through the entire syllabus.

- **SA 200 (Overall objectives).** SA 200 establishes professional scepticism, professional judgement, and sufficient appropriate audit evidence. Documentation is where scepticism and judgement leave a *trace*, and where "sufficient appropriate evidence" becomes provable. SA 230 is SA 200 made auditable. The "reasonable assurance, not absolute" idea in SQC 1 is the firm-level echo of SA 200's inherent limitations.

- **SA 220 ⇄ SQC 1.** These are the same subject at two scales. SQC 1 sets *firm* policy; SA 220 requires the *engagement* to operate within it. SA 220 repeatedly says "the engagement partner may rely on the firm's system (SQC 1) unless information indicates otherwise." Learn them as a pair, not as rivals.

- **Ethics / Independence (Code of Ethics & Companies Act s.141 disqualifications).** Both SA 220 and SQC 1 make **independence** a first-order quality element. The rotation of auditors (**Companies Act s.139(2)**) and the firm-level independence policies of SQC 1 are two enforcement arms of the same idea — familiarity threatens objectivity, so the system forces fresh eyes. SQC 1's annual written independence confirmation is the professional layer beneath the statutory rotation rule.

- **Companies Act 2013 record-keeping.** The Act (e.g., books-of-account retention, and the auditor's own reporting under **s.143**) interacts with SQC 1's seven-year retention. The audit *file* (auditor's record) and the *books of account* (company's record) are distinct but both are subject to statutory retention regimes. **Confirm the exact company-law retention interaction in current ICAI/RTP material.**

- **SA 240 (Fraud) and SA 260/265 (Communication with TCWG / deficiencies).** These generate specific documentation obligations — fraud discussions, communicated deficiencies — that flow into the SA 230 file. Documentation is the common downstream repository of nearly every other SA.

- **SA 315 / SA 330 (Risk assessment and responses).** The *extent* of documentation is driven by *assessed risk* — SA 230 explicitly lists identified risks of material misstatement as a factor. Higher-risk areas (significant risks under SA 315) demand fuller documentation, tying the file's shape directly to the risk model.

- **SA 560 (Subsequent Events).** The trigger for "facts known after the report date" that drive SA 230's after-the-report documentation rule comes from SA 560. SA 560 decides *whether to act*; SA 230 governs *how to record* the action.

- **SA 580 (Written Representations) and SA 505 (External Confirmations).** These are specific *forms* of documentation/evidence that populate the file — reminding you that the "file" is an aggregation of evidence gathered under many standards.

- **NFRA / Peer Review / Quality Review Board.** External inspection regimes are the *reason* the file must satisfy the "experienced auditor with no previous connection" standard. The stranger in SA 230 is, in practice, an NFRA or peer-review inspector.

- **SA 230 ⇄ SA 500 (Audit Evidence).** SA 500 says *obtain* sufficient appropriate evidence; SA 230 says *record* it. Evidence not documented is, for accountability purposes, evidence not obtained.

## 8. Traps & Examiner Tricks

The examiner mines this chapter for precise-number and precise-wording questions. Guard against these:

- **60 days vs 7 years — never confuse them.** **60 days** is the *assembly* period (administrative completion, *after* the report). **7 years** is the *retention* period (how long the assembled file is kept). Both run *from the date of the auditor's report*. Mixing these up is the classic slip.

- **Everything counts from the *report date*, not the year-end or the destruction date.** In numerical questions, anchor both the 60-day and 7-year counts to the **date of the auditor's report**. Students routinely miscount from the balance-sheet date and get the answer wrong.

- **"Assembly" is administrative, not substantive.** A favourite trap: a scenario where, during the 60-day window, the auditor performs *new audit procedures*. That is **not** assembly. Assembly = collating, sorting, discarding superseded drafts. New procedures after the report date trigger the "changes after the report date" documentation rule, not a free extension of the audit.

- **The SA 230 benchmark wording.** The examiner wants the exact phrase: **"experienced auditor, having no previous connection with the audit."** Answers that paraphrase it as "any reader" or "a knowledgeable person" lose the point. And it must understand **nature, timing and extent + results + significant matters/conclusions/judgements** — list all three limbs.

- **The "experienced auditor" is skilled, not ignorant.** Trap: assuming the file must spell out *everything* including generic professional knowledge. The benchmark reader already understands audit processes, the SAs and the industry — so the file supplies what is *specific to this engagement*, not a textbook. Over-documentation is itself a fault (it buries the significant).

- **Oral explanation cannot substitute for documentation.** Trap: "the auditor can explain the gaps if asked." Oral explanations may *clarify* an adequate file; they can never *replace* missing documentation. A file that only works with the auditor standing beside it has already failed.

- **"You must document everything" — FALSE.** You document *significant* matters and judgements, not every thought. Superseded drafts and preliminary notes need **not** be retained. A question that pushes "the auditor failed because he didn't document every single consideration" is testing whether you know the *significance* filter.

- **EQCR is not for every audit.** It is mandatory for **listed entities** and firm-defined high-risk engagements — *not* every client. A trap scenario applies EQCR to a small private company with no such trigger.

- **The EQCR timing rule is absolute.** "The report was dated first and the EQCR finished a few days later" is *always* wrong for a listed entity. Report date **cannot precede** EQCR completion.

- **EQCR does not shift responsibility.** Trap: "the EQC reviewer is responsible for the opinion / the partner can offload hard calls to the reviewer." False — the reviewer *evaluates*; the *engagement partner remains responsible* for the opinion. The reviewer must not make the team's decisions.

- **Consulting the intended reviewer can disqualify them.** Trap: appointing as EQC reviewer the very partner who helped form a significant judgement, "because they know it best." That recreates self-review bias and breaches the objectivity safeguards.

- **SA 220 vs SQC 1 level confusion.** If the question is about *firm* policies (recruitment, monitoring, tone at the top, retention policy), it's **SQC 1**. If it's about *this engagement* (this partner, this team, this independence conclusion), it's **SA 220**. Answering "SA 220" for a firm-monitoring question is a level error.

- **Ownership of working papers.** Trap: "the working papers belong to the client because the client paid." **False.** Working papers are the **property of the auditor.** The auditor may, at discretion, make portions available to the client, but the client has no right to them; the auditor must keep them confidential and in safe custody (SQC 1). (Confirm the precise treatment in ICAI's SA 230 guidance.)

- **Departure from an SA requirement.** Trap answer: "the auditor can never depart from an SA." Reality: in *exceptional* circumstances the auditor may perform *alternative* procedures, **provided** he documents how the alternative achieves the requirement's aim and the reasons. The sin is undocumented departure, not departure itself. Sub-trap: a *conditional* requirement whose condition is absent is simply *inapplicable* — that is not a "departure" and triggers no departure-documentation.

- **Monitoring inspection frequency.** The "at least one completed engagement per engagement partner on a cyclical basis" detail is examinable — vague answers ("the firm should review some files sometimes") lose marks.

- **A monitoring deficiency ≠ a wrong report.** Trap: "monitoring found a deficiency, therefore the audit opinion was wrong and must be withdrawn." The firm must first *evaluate* whether the deficiency is isolated or systemic and whether it actually affects an issued report. Not every finding invalidates an opinion.

- **"Reasonable" not "absolute" assurance.** Trap: stating SQC 1 *guarantees* every engagement is correct. It provides *reasonable* assurance only; an occasional deficient engagement does not, by itself, prove the system failed.

- **Independence confirmation timing.** SQC 1 requires written independence confirmations *at least annually* from relevant personnel — a specific, occasionally-tested detail; "whenever convenient" is wrong.

## 9. First-Principles Recap

Strip everything back and rebuild it from the original problems:

1. **The work is invisible → make it visible and permanent.** That is **SA 230 documentation**. The test of "enough" is not the writer's satisfaction but a *stranger's* comprehension — the experienced auditor with no prior connection (skilled, but disconnected). Record what you did (nature, timing, extent), what you found (results, evidence), and what you concluded (significant matters, judgements). Record who did it and who reviewed it. Because memory and conversation evaporate — and oral explanation can never substitute for the file — only the written record survives to prove the audit happened.

2. **A team must review itself → build the review into the process and the record.** That is **SA 220 engagement quality control**: one accountable partner, competent staff, more-experienced reviewing less-experienced, consultation on hard calls (agreed *and* implemented), independence concluded, and — for high-stakes engagements — an *independent* second reviewer (EQCR) whose review must finish *before* the opinion is locked. Self-review bias is broken by putting the second opinion in genuinely different hands — which is also why consulting the intended reviewer too heavily can disqualify them.

3. **A firm's signature must mean the same thing every time → govern quality at the firm level.** That is **SQC 1**: six elements (leadership, ethics/independence, acceptance/continuance, human resources, engagement performance, monitoring) that make quality a *system*, not a personal virtue — offering *reasonable*, not absolute, assurance. And the system audits itself through **monitoring** (cyclical inspection of at least one completed engagement per partner) and through complaint channels.

4. **Disputes and the record's own mortality arrive late → keep the proof, and lock it.** Assemble the file promptly (**≤60 days**, administrative only) and retain it long enough to cover the tail (**≥7 years**), in safe custody, confidential, with integrity, accessible and retrievable — and *never* silently rewritten; post-report changes are documented in the open. The report date is the bright line for *substance*; assembly and retention govern only *administration* and *survival*.

The unifying sentence again: **documentation is the evidence that the work was done; quality control is the process that the evidence must show was good.** One proves *that* you worked; the other proves the work was *worth trusting*. Together they answer the profession's own agency problem — *who audits the auditor?* — with: the file does, the reviewer does, the firm's system does, and the inspector can.

## 10. Quick-Revision Sheet

**Four pillars**

| Pillar | Level | One-line purpose |
|---|---|---|
| SA 230 | Engagement | Record the audit so it is provable and reviewable |
| SA 220 | Engagement | Deliver quality on *this* audit; partner is responsible |
| SQC 1 | Firm | System giving reasonable assurance of quality across *all* engagements |
| EQCR | Engagement (high-risk) | Independent objective review of significant judgements before the report is dated |

**SA 230 must-knows**
- Definition: record of **procedures performed + evidence obtained + conclusions reached** (formerly "working papers"; whole = **audit file**, physical or electronic).
- Benchmark: understandable by an **experienced auditor, no previous connection** (skilled but disconnected) — the **nature, timing, extent**; the **results**; the **significant matters, conclusions, judgements**.
- Record **who performed/date** and **who reviewed/date/extent**; record **identifying characteristics** of items tested.
- Document **significant discussions** (when, with whom); document **departures** from a *relevant* SA requirement (how alternative met the aim + why).
- **Oral explanation** may *clarify* but never *substitute* for documentation.
- **Post-report changes:** document circumstances, new work, who/when; **never delete** original contents.
- Need **not** document every judgement; need **not** retain superseded drafts/preliminary notes.

**Numbers (from the auditor's report date)**
- **Assembly of final file: ≤ 60 days** (administrative completion only — no new audit work).
- **Retention: ≥ 7 years** (safe custody, confidentiality, integrity, accessibility, retrievability).
- **Independence written confirmations: at least annually** (SQC 1 firm level).
- **Monitoring: cyclical inspection of ≥ 1 completed engagement per engagement partner.**
- **Working papers = auditor's property** (client has no right; auditor may share portions at discretion, subject to confidentiality).

**SA 220 — engagement partner's responsibilities**
Leadership on quality · ethics + **independence conclusion** · acceptance/continuance · competent team · **direction, supervision, review** (senior reviews junior) · **consultation** (agreed + implemented) · **EQCR where applicable** · resolve **differences of opinion** before dating report · consider **monitoring** results · rely on SQC 1 *unless information indicates otherwise* · document all of it.

**SQC 1 — six elements**
1. Leadership (tone at the top; commercial pressure must not override quality) · 2. Ethical requirements + independence (incl. **rotation**, annual confirmations) · 3. Acceptance & continuance · 4. Human resources · 5. Engagement performance (houses **assembly, retention, EQCR, consultation, differences, custody attributes**) · 6. **Monitoring** (cyclical inspection of **≥ 1 completed engagement per engagement partner**; complaints channel).

**EQCR — the sharp control**
- Mandatory for **listed entities** + firm-defined high-risk engagements.
- Reviewer is **NOT** on the engagement team (breaks self-review bias); heavy prior consultation can disqualify.
- Reviews significant judgements, conclusions, the report, selected working papers, independence.
- Evaluates, does **not** decide — the *partner* remains responsible for the opinion.
- **Report must NOT be dated until EQCR is complete.**

**The one sentence:** *Documentation is the evidence the work was done; quality control is the process the evidence must prove was good — together they answer "who audits the auditor?"*

> **Confirm in current ICAI material:** exact interaction of SQC 1's 7-year retention with Companies Act 2013 record-retention; any migration references to the newer quality-management framework (SQM 1 / SQM 2 / SA 220 (Revised)) if adopted for your attempt — this chapter states the SQC 1 / SA 220 position per the extant CA Intermediate syllabus.
