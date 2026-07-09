# Q&A — Liquidity Risk

A practice bank for the Liquidity Risk chapter. Work each question before reading the answer. Numerical answers self-check against the master identities **LCR = HQLA / Net 30-day outflows ≥ 100%**, with **Net outflows = Outflows − min(Inflows, 75% × Outflows)**, and **NSFR = ASF / RSF ≥ 100%**.

---

## Section A — Concept-Check (short answer)

**A1. Define liquidity risk and distinguish it from insolvency.**

Liquidity risk is the risk that a firm cannot meet its obligations *as they fall due* without incurring unacceptable losses. It is a **cash-flow** condition: cannot-pay-now. Insolvency is a **balance-sheet** condition: assets worth less than liabilities. The distinction is load-bearing — a firm can be perfectly solvent (assets exceed liabilities) yet fail overnight because its assets are locked in illiquid loans while its liabilities come due today. Northern Rock and, arguably, early-stage SVB died of illiquidity, not insolvency.

**A2. Name the two faces of liquidity risk and state which side of the balance sheet each concerns.**

**Funding liquidity risk** — the inability to raise cash to pay one's own obligations; it concerns the **liability** side (deposits fleeing, wholesale funders refusing to roll over). The question is *"Can I get cash to pay what I owe?"* **Market liquidity risk** — the inability to sell an asset quickly near fair value; it concerns the **asset** side (thin markets, wide bid–ask). The question is *"Can I turn what I own into cash without a fire-sale loss?"*

**A3. What is the liquidity spiral?**

A self-reinforcing loop that joins the two faces: a **funding** shortfall forces the firm to sell assets; if those assets are **market-illiquid**, the sale is at a fire-sale discount; the loss erodes capital; the loss frightens more funders, who flee; that deepens the funding shortfall — and round again. A manageable cash-flow wobble becomes a death spiral. It is why funding and market liquidity, though distinct, must be managed together.

**A4. Why is maturity transformation both essential and dangerous?**

Essential because society wants it: savers want instant access, borrowers want long, patient loans, and banks bridge the two by borrowing short and lending long. It works because of the **law of large numbers** — on a normal day only a small, predictable net fraction of demand deposits is withdrawn, since withdrawals and deposits roughly cancel across many independent customers. Dangerous because depositor behaviour is not always independent: **fear is correlated.** When depositors believe others will withdraw, withdrawing first becomes rational, and the belief becomes self-fulfilling (the Diamond–Dybvig "bad equilibrium").

**A5. What is a liquidity gap, and what is the difference between the marginal and cumulative gap?**

The **liquidity gap** in a time bucket = cash inflows − cash outflows (equivalently, assets maturing − liabilities maturing) for that bucket. The **marginal (period) gap** is the gap *within* a single bucket. The **cumulative gap** is the running sum of marginal gaps up to horizon *T*. The cumulative gap is what matters, because a firm can carry cash forward: survival requires **cumulative gap + liquid buffer ≥ 0 at every horizon.**

**A6. Why must demand deposits be slotted by behavioural, not contractual, maturity in a gap ladder?**

Demand deposits are contractually repayable overnight but behaviourally sticky for years. If you slot them at their contractual (overnight) maturity, every bank shows a massive negative gap in the first bucket and looks instantly insolvent. Behavioural modelling assigns them to the buckets in which they are actually expected to leave. (Note the nuance: LCR and NSFR *deliberately* override the bank's optimistic behavioural assumptions with conservative regulatory run-off rates.)

**A7. State the LCR formula, its threshold, and what it tests.**

$$\text{LCR} = \frac{\text{Stock of High-Quality Liquid Assets (HQLA)}}{\text{Total Net Cash Outflows over 30 days}} \geq 100\%$$

It tests whether a firm holds enough high-quality liquid assets to survive a **severe 30-day acute liquidity stress** without any new funding — the short-term sprint.

**A8. State the NSFR formula, its threshold, and what it tests.**

$$\text{NSFR} = \frac{\text{Available Stable Funding (ASF)}}{\text{Required Stable Funding (RSF)}} \geq 100\%$$

It tests whether a firm funds its illiquid assets with sufficiently **stable** money over a **one-year** horizon — the structural marathon. ASF weights liabilities by stability; RSF weights assets by illiquidity. Its explicit purpose is to curb over-reliance on short-term wholesale funding.

**A9. Explain the 75% inflow cap in the LCR and why it exists.**

Net outflows = Outflows − min(Inflows, 75% × Outflows). A firm may offset its stressed outflows with expected inflows only up to **75% of gross outflows.** This forces it to hold HQLA covering at least **25% of gross outflows** no matter how much money it expects to receive — you can never assume you will be fully rescued by incoming cash, because in a stress your counterparties may not pay you either.

**A10. Why is short-term wholesale funding the recurring villain across both ratios?**

In the LCR it carries a **100% run-off** (assumed to flee entirely in the 30-day stress); in the NSFR it carries a **0% ASF factor** (counts as zero stable funding). The regulators are telling you, from both the 30-day and the 1-year angle, that this is the funding that kills you. Every modern bank failure — Northern Rock, Bear Stearns, Lehman, SVB, Credit Suisse — was funded by hot, flighty money and died fast; firms funded by insured retail deposits and long-term debt survive.

**A11. What is HQLA, and what makes an asset qualify?**

High-Quality Liquid Assets: unencumbered assets convertible to cash in stress with little or no loss, because they are what everyone flies *to* rather than *from*. Level 1 (cash, central-bank reserves, top-rated sovereigns) has a 0% haircut and no cap. Level 2A (high-grade sovereign/agency, AA– corporates) has a 15% haircut; Level 2B (A+ to BBB– corporates, some equities) has 25–50% haircuts. Level 2 total is capped at 40% of HQLA and Level 2B at 15%. Crucially the assets must be **unencumbered** — bonds already pledged as collateral are not the liquidity you think you have.

**A12. What is a Contingency Funding Plan (CFP)?**

A pre-agreed, board-approved crisis playbook that specifies **early-warning indicators** (widening CDS, rising funding costs, deposit outflows, share-price falls) and graduated actions (draw committed lines, sell HQLA, pledge collateral, activate central-bank facilities) triggered at defined thresholds — so the firm acts *on plan* rather than in panic.

---

## Section B — Numerical / Applied (full solutions)

**B1. Marginal and cumulative liquidity gap.** A bank reports the following contractual flows (₹ crore). Compute the marginal and cumulative gaps and, with a ₹150 crore opening buffer, find the survival horizon.

| Bucket | Inflows | Outflows |
|---|---:|---:|
| 0–7d | 100 | 300 |
| 8–30d | 220 | 180 |
| 31–90d | 160 | 130 |

Marginal gaps: 100−300 = **−200**; 220−180 = **+40**; 160−130 = **+30**.
Cumulative gaps: −200; −200+40 = **−160**; −160+30 = **−130**.
Buffer overlay (150 + cumulative gap): 150−200 = **−50**; 150−160 = **−10**; 150−130 = **+20**.

**Self-check:** sum of marginal gaps = −200+40+30 = −130 = final cumulative gap ✓.
**Interpretation:** the ₹150 cr buffer is exhausted inside the first week (short by ₹50 cr) and remains negative through the 8–30d bucket. **Survival horizon is under 7 days.** The bank needs the buffer above ₹200 cr, or must cut first-week outflows. Classic maturity transformation: fine over the quarter, dead in the first week.

**B2. Basic LCR.** HQLA (after haircuts) = ₹600 cr. Gross stressed outflows = ₹500 cr. Gross expected inflows = ₹300 cr. Compute the LCR.

Inflow cap = 75% × 500 = 375. Capped inflows = min(300, 375) = **300** (uncapped, since 300 < 375).
Net outflows = 500 − 300 = **200**.
$$\text{LCR} = \frac{600}{200} = 3.00 = \mathbf{300\%}$$
Comfortably above the 100% minimum.

**B3. LCR with the inflow cap binding.** Same HQLA = ₹600 cr and outflows = ₹500 cr, but gross inflows are now ₹450 cr. Recompute.

Inflow cap = 75% × 500 = **375**. Capped inflows = min(450, 375) = **375** (now capped, since 450 > 375).
Net outflows = 500 − 375 = **125**.
$$\text{LCR} = \frac{600}{125} = 4.80 = \mathbf{480\%}$$
**Teaching point:** the extra ₹150 cr of expected inflows above B2 did *not* all count — only ₹75 cr of it flowed through, because the cap holds recognised inflows at 375. The firm is forced to self-insure at least 25% of gross outflows (₹125 cr here) with HQLA regardless of what it expects to receive.

**B4. LCR from raw components with HQLA caps.** Compute HQLA and the LCR.

HQLA before caps: Cash (L1) ₹300, sovereign bonds (L1) ₹200, AA– corporates (L2A) ₹200 at 15% haircut, BBB corporates (L2B) ₹120 at 50% haircut.

- L1 = 300 + 200 = 500.
- L2A after haircut = 200 × 0.85 = 170.
- L2B after haircut = 120 × 0.50 = 60.
- Pre-cap total = 500 + 170 + 60 = 730. Level 2 = 170 + 60 = 230 → 230/730 = 31.5% ≤ 40% cap ✓. Level 2B = 60 → 60/730 = 8.2% ≤ 15% cap ✓.
- **HQLA = 730.**

Outflows: stable retail ₹2,000 @ 5% = 100; less-stable retail ₹500 @ 10% = 50; operational corporate ₹800 @ 25% = 200; unsecured wholesale ₹400 @ 100% = 400. **Total outflows = 750.**
Inflows: maturing interbank ₹200 @ 100% = 200; retail loan repayments ₹300 @ 50% = 150. **Total inflows = 350.**
Cap = 75% × 750 = 562.5; capped inflows = min(350, 562.5) = 350. Net outflows = 750 − 350 = **400**.
$$\text{LCR} = \frac{730}{400} = 1.825 = \mathbf{182.5\%}$$
Compliant.

**B5. Level 2B cap binding.** A firm holds L1 = ₹100 cr and L2B (after haircut) = ₹30 cr and nothing else. How much L2B actually counts toward HQLA?

Let total HQLA = H. L2B may be at most 15% of H. If all 30 counted, H = 130 and L2B share = 30/130 = 23.1% > 15% — breach. The binding condition: L2B ≤ 0.15 × (L1 + eligible L2B). Solve L2B_elig = 0.15(100 + L2B_elig) → L2B_elig = 15 + 0.15·L2B_elig → 0.85·L2B_elig = 15 → L2B_elig = **17.65**. So only **₹17.65 cr** of the ₹30 cr counts; HQLA = 100 + 17.65 = **117.65 cr**. The excess ₹12.35 cr is disallowed. **Lesson:** low-grade "liquid" assets are capped precisely because they are the ones that gap down in a fire sale.

**B6. NSFR.** Compute the NSFR.

ASF: equity ₹800 @ 100% = 800; long-term debt ≥1yr ₹600 @ 100% = 600; stable retail deposits ₹2,500 @ 95% = 2,375; operational corporate deposits ₹1,000 @ 50% = 500; short-term wholesale ₹800 @ 0% = 0. **ASF = 4,275.**
RSF: cash ₹400 @ 0% = 0; L1 sovereigns ₹800 @ 5% = 40; L2A ₹400 @ 15% = 60; residential mortgages ≥1yr ₹2,500 @ 65% = 1,625; corporate loans ≥1yr ₹1,800 @ 85% = 1,530; fixed assets ₹300 @ 100% = 300. **RSF = 3,555.**
$$\text{NSFR} = \frac{4,275}{3,555} = 1.203 = \mathbf{120.3\%}$$
Compliant — illiquid assets (mortgages, corporate loans) are funded by stable money (equity, long debt, sticky retail).

**B7. NSFR under a funding-mix shock.** Take B6 and replace ₹1,500 cr of stable retail deposits (95% ASF) with short-term wholesale funding (0% ASF). Recompute and comment.

ASF falls: the ₹1,500 cr that contributed 1,500 × 0.95 = 1,425 now contributes 0. New ASF = 4,275 − 1,425 = **2,850**. RSF unchanged at 3,555.
$$\text{NSFR} = \frac{2,850}{3,555} = 0.802 = \mathbf{80.2\%}$$
A severe breach — same assets, same size, but funding the identical book with hot money instead of sticky deposits blows the ratio apart. **Funding quality, not asset quality, drives the liquidity ratios.**

**B8. Loan-to-Deposit Ratio.** A bank has loans ₹4,200 cr and deposits ₹3,500 cr. Compute the LDR and interpret.

$$\text{LDR} = \frac{4{,}200}{3{,}500} = 1.20 = \mathbf{120\%}$$
Above 100%, so the loan book is funded partly by non-deposit (usually flightier, wholesale) sources — a crude early flag of structural funding stress. It says nothing about loan *credit quality*; those are separate risks.

**B9. Survival horizon from stressed flows.** Opening buffer = ₹100 cr. Stressed net outflows: Day 1–2 total ₹40 cr, Day 3–5 total ₹45 cr, Day 6–10 total ₹30 cr. When does the buffer hit zero?

Running buffer: after D1–2: 100 − 40 = 60; after D3–5: 60 − 45 = 15; after D6–10: 15 − 30 = **−15**. The buffer covers all outflows through Day 5 (₹15 cr remaining) but not the ₹30 cr of Days 6–10. **Survival horizon lies between Day 5 and Day 10** — the firm runs dry partway through the 6–10 window (with ₹15 cr it covers half of the ₹30 cr, roughly Day 7–8 at an even daily rate). It must arrange funding before then.

**B10. LCR shock — flighty funding.** In B4, suppose unsecured wholesale funding rises from ₹400 to ₹1,000 cr (still 100% run-off), all else equal. Recompute the LCR.

New outflows = 100 + 50 + 200 + 1,000 = **1,350**. Inflow cap = 75% × 1,350 = 1,012.5; capped inflows = min(350, 1,012.5) = 350. Net outflows = 1,350 − 350 = **1,000**.
$$\text{LCR} = \frac{730}{1{,}000} = 0.73 = \mathbf{73\%}$$
Now **non-compliant.** The same HQLA that gave 182.5% comfort in B4 collapses below 100% the instant the funding mix tilts toward hot money — the quantitative signature of the villain in A10.

---

## Section C — Interview-style (model answers)

**C1. "A bank can be solvent and still fail. Explain."**

Solvency and liquidity are two independent ways a firm can die. Solvency is a balance-sheet condition — assets worth more than liabilities. Liquidity is a cash-flow condition — the ability to pay obligations *when they fall due*. A bank's assets are mostly illiquid long-dated loans; its liabilities are mostly short-dated deposits. If depositors demand cash faster than the bank can convert assets to cash, it fails — even though, on paper, its assets comfortably exceed its liabilities. That is exactly how Northern Rock went down in 2007: solvent, but unable to roll over its short-term funding. Capital defends against insolvency; the liquid buffer defends against illiquidity, and you need both.

**C2. "Walk me through how a modern liquidity crisis unfolds."**

It is a cascade. (1) **Trigger** — bad news: a loss, a downgrade, a failed capital raise, a peer's collapse. (2) **Wholesale flight** — sophisticated counterparties move first, silently and fast: interbank lenders won't roll over, repo haircuts jump, commercial paper won't reprice. (3) **Retail run** — depositors follow, now amplified by mobile banking and social media; SVB lost \$42 billion — a quarter of its deposits — in a single day. (4) **Fire sales** — to raise cash the firm dumps assets, and selling in size and distress crushes prices. (5) **Solvency contagion** — those fire-sale losses now make the firm *actually* insolvent, and mark-to-market losses spread to peers holding the same assets. (6) **Resolution** — lender-of-last-resort support, a forced acquisition, or failure. The lesson: the disease is always maturity mismatch plus flighty funding; what changed by 2023 was *speed*.

**C3. "How would you actually manage liquidity risk at a bank?"**

Four levers plus a plan. First, hold a **liquid-asset buffer** of unencumbered HQLA sized to survive the plausible worst 30 days without new funding — never encumber the whole buffer, because the point of a buffer is to be usable in a storm. Second, **diversify funding** across sources, tenors, currencies and geographies, and cap reliance on any single counterparty or the overnight market. Third, **term out the funding** so the roll-over cliff is small and spread over time. Fourth, **model behaviour** — actual deposit stickiness, prepayments, and drawdowns of committed lines — not just contractual dates. Over the top of all this sits a **Contingency Funding Plan** with early-warning triggers and pre-positioned central-bank collateral, and a **stress-testing** programme that deliberately models catastrophe and checks the survival horizon. The recurring discipline is to assume your best-case assumptions all fail simultaneously, because in a panic they do.

**C4. "LCR and NSFR — aren't they the same thing?"**

No — different horizons and different purposes, and a firm can pass one while failing the other. The **LCR** is a 30-day acute-stress survival test on the *buffer*: do you hold enough high-quality liquid assets to survive a severe month-long stress with no new funding? It's the sprint. The **NSFR** is a one-year structural test on *funding stability*: are you funding your illiquid assets with sufficiently stable money? It's the marathon. LCR asks "can you survive next month's storm?"; NSFR asks "is your business model structurally funded?" They attack the same villain — short-term wholesale money — from two angles: it gets a 100% run-off in the LCR and a 0% ASF factor in the NSFR.

**C5. "Why did the 2023 failures — SVB, Credit Suisse — happen so fast?"**

Same disease as 2008, faster transmission. The underlying vulnerability was classic: maturity mismatch (SVB held long-dated bonds funded by concentrated, uninsured, tech-sector deposits) plus flighty funding. What changed was the *speed of the run*. In Northern Rock's era a run meant physical queues over three days. By 2023, mobile banking and social media let panic and money move instantly — SVB lost \$42 billion in one day, 25% of deposits. The buffer and the resolution machinery, both designed around slower runs, could not keep pace. It's a reminder that liquidity risk is reflexive: the fear of failure *causes* the failure, and technology has compressed the timeline to hours.

**C6. "Your treasurer says 'we hold plenty of bonds, so we're liquid.' Push back."**

Two problems. First, only *unencumbered* bonds are liquidity — bonds already pledged as collateral for repo or derivatives are spoken for and cannot be sold or re-pledged. Second, only genuinely high-quality bonds stay liquid *in stress*; lower-grade bonds gap down in a fire sale, so their stressed value is far below the marked value. SVB is the cautionary tale: it held plenty of bonds, but they were long-dated and sitting on large unrealised losses, so *selling* them to raise cash crystallised the loss that triggered the run. "We hold bonds" is not the same as "we hold usable, unencumbered, stress-resilient liquidity." I'd want the buffer measured as unencumbered HQLA after haircuts, not gross bond holdings.

---

## Section D — MCQs (with reasoning)

**D1. A bank whose assets exceed its liabilities but which cannot meet a deposit withdrawal today is best described as:**
A. Insolvent B. Illiquid C. Both D. Neither

**Answer: B.** Assets exceeding liabilities means solvent; the inability to pay now despite solvency is illiquidity — a cash-flow, not balance-sheet, condition.

**D2. The LCR requires HQLA to cover net cash outflows over a horizon of:**
A. 7 days B. 30 days C. 90 days D. 1 year

**Answer: B.** The LCR is the 30-day acute-stress sprint. (The one-year structural test is the NSFR.)

**D3. Under the LCR, expected inflows may offset outflows only up to:**
A. 50% of outflows B. 75% of outflows C. 100% of outflows D. No cap

**Answer: B.** The 75% inflow cap forces the firm to self-insure at least 25% of gross outflows with HQLA, since you cannot assume full rescue by incoming cash.

**D4. Which funding source carries a 100% run-off in the LCR and a 0% ASF factor in the NSFR?**
A. Insured stable retail deposits B. Regulatory capital C. Short-term wholesale funding D. Long-term debt (≥1yr)

**Answer: C.** Both ratios penalise short-term wholesale money maximally — the recurring villain of liquidity failures.

**D5. A negative liquidity gap in the shortest time bucket indicates that in that period the bank:**
A. Has surplus cash to invest B. Must refinance a shortfall C. Is insolvent D. Has too much HQLA

**Answer: B.** More liabilities than assets mature, so the shortfall must be refinanced — the signature of borrowing short and lending long.

**D6. Level 2 assets are capped at what proportion of total HQLA?**
A. 15% B. 25% C. 40% D. 50%

**Answer: C.** Total Level 2 ≤ 40% of HQLA; the sub-cap of 15% applies specifically to Level 2B.

**D7. The NSFR is designed primarily to:**
A. Ensure a 30-day cash buffer B. Curb over-reliance on short-term wholesale funding C. Set minimum equity capital D. Measure credit losses

**Answer: B.** It forces illiquid assets to be funded with stable money over one year, directly attacking hot-money dependence. (A is the LCR; C is capital adequacy; D is credit risk.)

**D8. The liquidity spiral describes:**
A. Rising deposit rates over time B. A funding shortfall forcing fire sales whose losses deepen the shortfall C. Central-bank rate cuts D. Diversification of funding sources

**Answer: B.** The self-reinforcing loop linking funding and market liquidity risk.

**D9. A loan-to-deposit ratio above 100% signals that:**
A. All loans are funded by deposits B. The loan book is partly funded by non-deposit (flightier) sources C. The bank is insolvent D. The bank holds excess HQLA

**Answer: B.** Loans exceed deposits, so the gap is filled by usually-flightier wholesale funding — a crude structural-funding flag.

**D10. In the LCR, a demand deposit that is insured and stable receives a run-off rate closest to:**
A. 3–5% B. 25% C. 40% D. 100%

**Answer: A.** Insured, sticky, diversified retail deposits are assumed to flee only marginally (3–5%); unsecured wholesale and financial-institution funding get the 40–100% treatment.

**D11. Which asset qualifies as Level 1 HQLA with a 0% haircut?**
A. BBB corporate bonds B. Listed equities C. Central-bank reserves and top-rated sovereign bonds D. Residential mortgages

**Answer: C.** Level 1 = cash, central-bank reserves, top-rated sovereigns, no haircut, no cap. The others are lower-tier or non-HQLA.

**D12. The single most important reason 2023's runs (SVB) were faster than 2007's (Northern Rock) was:**
A. Higher interest rates B. Mobile banking and social media compressing the run timeline C. Weaker capital D. Larger HQLA buffers

**Answer: B.** The disease (maturity mismatch + flighty funding) was identical; digital banking turned a multi-day branch-queue run into a one-day \$42bn digital run.

---

*Self-verification note:* Every LCR figure above uses Net outflows = Outflows − min(Inflows, 75% × Outflows) and checks the 40%/15% Level 2 caps; every NSFR uses ASF/RSF with the stated factors; every gap ladder reconciles the final cumulative gap against the sum of marginal gaps. All computed ratios were recomputed independently and agree.
