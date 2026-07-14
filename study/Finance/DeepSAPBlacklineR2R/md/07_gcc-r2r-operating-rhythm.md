# The GCC R2R Operating Rhythm: WD Calendar, SLAs, DTP/SOP, RPA

## What you'll be able to do

After this chapter you can describe — like someone who has actually sat on the desk — **how an offshore R2R team runs**: the **working-day (WD) close calendar**, the **SLAs and KPIs** you're measured on, how work is documented in a **DTP/SOP**, how requests flow through **ticket queues (ServiceNow)**, how a process gets **transitioned/knowledge-transferred** from an onshore team, and where **RPA bots (UiPath / Automation Anywhere)** fit in. This is the operating-model knowledge that Genpact, Accenture, HP and Cromwell R2R JDs implicitly test — and it's often what separates a candidate who "knows accounting" from one who "can run in a GCC from day one."

## The drill — step by step

**Step 1 — Learn the WD calendar.** Close is measured in **working days from period-end (WD1, WD2…)**, not calendar dates, so it's consistent across months. A typical mid-market R2R close:

| Day | Activity |
|---|---|
| WD-1 (pre-close) | Cut-off comms, ensure sub-ledgers ready, freeze non-essential postings |
| WD1 | Sub-ledger close (AP/AR), accruals raised, FX revaluation (SAP **FAGL_FC_VAL**) |
| WD2 | Intercompany postings & matching, depreciation run (**AFAB**), payroll JE |
| WD3 | GL close, recurring/allocation journals, reclasses |
| WD4 | Reconciliations & flux/BS review |
| WD5 | Management reporting / BPC submission, sign-off, ledger lock |

Knowing "I owned WD1–WD2 accruals and FX, WD4 recons" is exactly how you narrate experience in interviews.

**Step 2 — Know your SLAs and KPIs.** Offshore work is governed by a **Service Level Agreement**. The metrics you're graded on:

| KPI | Typical target | What it measures |
|---|---|---|
| Timeliness / on-time close | ≥ 98% tasks by WD deadline | Did you hit the calendar |
| Recon completed on time | ≥ 95% by due date | Recons signed off |
| Accuracy / rework rate | ≤ 2% error | JEs/recons redone |
| Aging of open items | ↓ trend, nil >90d | Clean-up discipline |
| Ticket SLA adherence | ≥ 95% within SLA | Query turnaround |
| Auto-cert % (Blackline) | ↑ trend | Automation maturity |

**Step 3 — Work the DTP/SOP.** Every task has a **Desktop Procedure (DTP)** / Standard Operating Procedure — a step-by-step doc: purpose, systems, T-codes, screenshots, frequency, upstream/downstream dependencies, and the control point. In a GCC you *work to the DTP and keep it current*; an out-of-date DTP is an audit and transition risk. When you learn a new task you often *write or update* the DTP — that's a concrete deliverable to mention.

**Step 4 — Run the ticket queue.** Business queries (a cost-centre owner questioning a charge, a vendor mis-posting, a manual JE request) arrive as **ServiceNow tickets** in a shared queue. Drill: pick up ticket → acknowledge within SLA (e.g. 4 business hours) → investigate (FBL3N/FB03) → act or route → document resolution → close. You're measured on **SLA adherence** and **first-time resolution**.

**Step 5 — Understand transition / KT.** New scope moves offshore through a structured **transition**: **knowledge transfer** (shadowing onshore), **reverse-shadow** (you do it, they watch), **go-live**, then **stabilisation** (hypercare). Deliverables: DTPs signed off, a **RACI**, a cutover plan. Being able to say "I was reverse-shadowed for 3 weeks before taking ownership" signals you understand the model.

**Step 6 — Spot the RPA opportunities.** Bots (**UiPath, Automation Anywhere, Blue Prism**) handle high-volume, rules-based, no-judgement steps in R2R: downloading bank statements, running recurring uploads, triggering FX/depreciation runs, pulling reports, doing first-pass recon matching, sending reminder emails. You feed the bot a **PDD (Process Definition Document)**. Judgement (why an accrual, is this provision reasonable) stays human. In interviews, framing "I identified the bank-recon download as a bot candidate and wrote the PDD" shows **continuous-improvement** mindset.

**Step 7 — Continuous improvement (Kaizen/Lean).** GCCs run CI programs — **FTE savings, cycle-time reduction, error reduction**. You're expected to log ideas, sometimes with a **green-belt** framing (DMAIC). A quantified idea ("reduced WD4 recon time 30% by templating the flux") is gold.

## The output

A one-page **process ownership summary** (the artefact you'd keep, and effectively narrate in interviews):

| Element | Detail |
|---|---|
| Process | R2R — GL close & BS recons, 12 entities |
| My WD ownership | WD1 accruals+FX, WD2 IC, WD4 recons/flux |
| SLA | On-time close 98%, rework ≤2%, ticket SLA 95% |
| Tools | SAP FICO, Blackline, BPC, ServiceNow, UiPath |
| DTPs owned | 14, all reviewed within 6 months |
| CI delivered | Bank-recon bot (PDD written) → 8 hrs/month saved |
| KPI last quarter | Close 100% on-time, aging >90d nil, rework 1.2% |

## Checks & gotchas

- **WD calendar drives everything** — miss WD2 depreciation and WD3/WD4 cascade; dependencies are unforgiving.
- **SLA green ≠ quality green:** you can hit timeliness while pushing errors downstream — accuracy and aging are the honest metrics.
- **Stale DTPs** are the most common audit/transition finding; "current within 6 months" is a real control.
- **Ticket dumping:** routing a ticket without investigating just resets the clock and tanks first-time-resolution.
- **Over-automating judgement:** bots must not "decide" provisions or approve JEs — that breaks SOX and creates unmonitored risk.
- **Transition risk:** taking scope live before reverse-shadow completes is how errors spike in month one (hypercare exists for a reason).

## Interview drill

**Q: What does a working-day close calendar look like and why WD not dates?**
A: Close tasks are scheduled by working days from period-end — WD1 sub-ledger close and accruals, WD2 intercompany and depreciation, WD3 GL close and allocations, WD4 recons and flux, WD5 reporting and lock. We use WD rather than calendar dates because month-ends fall on different weekdays, so WD keeps the sequence and deadlines consistent every month and lets us measure on-time performance apples-to-apples.

**Q: How are you measured in a GCC R2R role?**
A: Against SLAs and KPIs: on-time close (~98% of tasks by their WD deadline), recon completion rate, rework/accuracy (errors kept ≤ ~2%), aging of open reconciling items trending down with nothing over 90 days, and ticket SLA adherence with strong first-time resolution. Quality and clean-up matter as much as speed — you can be on-time but pushing errors downstream, so accuracy and aging keep you honest.

**Q: Where does RPA fit in R2R, and where must it not?**
A: Bots suit high-volume, rules-based, judgement-free steps — statement downloads, recurring uploads, triggering standard runs, first-pass recon matching, reminders — driven by a Process Definition Document. They must not make accounting judgements or give final approval on journals or provisions; that stays human for SOX segregation-of-duties and because judgement isn't rules-based. Good CI is spotting the right bot candidates, not automating everything.

## Practise free

- **Draw your own WD calendar** in Excel for a fictional 10-entity group; add a dependency column so you can see what breaks if a day slips. This alone makes you sound experienced.
- **Write one real DTP:** pick a task you know (bank recon, accrual JE), document purpose → systems → steps → control point → frequency, with screenshots. That's a portfolio piece.
- **Simulate a ticket queue:** in a free Trello/Notion board, create 10 mock queries with SLA timers and practise triage/route/close notes.
- **RPA free tier:** **UiPath Community Edition** and **Automation Anywhere Community** are free — automate downloading a file and dropping data into Excel to genuinely understand bot mechanics. **UiPath Academy** and Automation Anywhere University are free and give shareable certificates.
- Read free **Genpact/Accenture "R2R operating model" and SSC/GBS** whitepapers to absorb the transition/KT/CI vocabulary before you're asked about it.
