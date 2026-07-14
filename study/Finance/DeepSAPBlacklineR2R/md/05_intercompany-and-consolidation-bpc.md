# Intercompany & the Consolidation Submission (SAP BPC / Group Reporting)

## What you'll be able to do

After this chapter you can explain — and walk an interviewer through — how a group with 40+ legal entities turns entity-level trial balances into **one consolidated financial statement**: how intercompany (IC) balances are matched and eliminated, how a foreign subsidiary's numbers get translated into the group currency, what a "BPC submission" actually is at the button level, and what a consolidation elimination journal or minority-interest calculation looks like. This is the exact domain the Dentsu "BPC Analyst" JD asks for ("intercompany matching, elimination, currency translation, monthly group submission in SAP BPC"). Be honest in interviews: the *hands-on clicking* needs employer access — but the **logic** is fully learnable, and that logic is what gets tested.

## The drill — step by step

Consolidation runs on a **hierarchy**. Learn the vocabulary first because every tool (SAP BPC, SAP Group Reporting/S4HANA, Oracle HFM/FCCS) uses the same shape, only different button names.

**The reporting hierarchy (dimensions):**
- **Entity** — each legal entity submits (e.g. IN01 India, GB01 UK, US01 US). Entities roll up to sub-groups → group total.
- **Account** — the group chart of accounts (mapped from each entity's local GL).
- **Time** — 2026.07 (period).
- **Category / Version** — Actual, Budget, Forecast.
- **Flow / Movement** — opening, additions, disposals, closing (needed for FX and fixed-asset roll-forwards).
- **Intercompany (Trading Partner)** — *who* the balance is with. This is the dimension that makes elimination possible.

**Step 1 — The package / submission.** Each entity's controller loads its trial balance into BPC (the "**data package**" — an upload from SAP ECC/S4 via a data manager package, or a manual input schedule in EPM add-in for Excel). The controller runs **validation** (does the local TB balance to zero? do control accounts tie?) and then **submits/locks** the entity for the period. "Doing the BPC submission" = load → validate → run currency translation → confirm IC → lock. That's the monthly ritual.

**Step 2 — Currency translation.** A foreign sub reports in local currency; the group reports in, say, INR or USD. Apply the standard (IAS 21 / current-rate) method:
- **P&L** items → **average rate** for the month.
- **Assets & liabilities** (balance sheet) → **closing rate**.
- **Equity / share capital** → **historical rate**.
- The plug that makes the translated balance sheet balance is booked to **Currency Translation Adjustment (CTA)** / FCTR in equity (OCI).

Worked example — UK sub GB01, month 2026.07:

| Item | GBP | Rate | INR (₹) |
|---|---|---|---|
| Revenue | 1,000,000 | 105 (avg) | 105,000,000 |
| Net assets (BS) | 500,000 | 106 (close) | 53,000,000 |
| Share capital | 200,000 | 100 (hist) | 20,000,000 |

The difference between the closing-rate net assets and the historical-rate equity + retained earnings flows to **CTA in equity**. BPC does this with a **rate table** + a translation logic script; you just load rates and hit "Run Currency Translation."

**Step 3 — Intercompany matching.** GB01 sold services to IN01. GB01 books **IC Receivable ₹8,00,000 (TP = IN01)**; IN01 books **IC Payable ₹8,00,000 (TP = GB01)**. The **IC matching report** pairs them by trading partner and flags **mismatches** (timing, FX, one side missed the invoice). Chasing and clearing those mismatches before lock is the analyst's real job — a ₹5,000 gap between the two sides holds up the whole consolidation.

**Step 4 — Elimination.** Once matched, the system posts **elimination entries** at the group level so intragroup items don't inflate the group:
- **IC receivable ↔ IC payable** → eliminate.
- **IC revenue ↔ IC cost** → eliminate.
- **IC profit in closing inventory** (unrealised profit) → eliminate.
- **Investment in subsidiary ↔ subsidiary's share capital** → eliminate at acquisition, recognise **goodwill** on the difference.

**Step 5 — Minority / non-controlling interest (NCI).** If the group owns 80% of a sub, 100% of the sub is consolidated line-by-line, then **20% of the sub's net assets and 20% of its profit are carved out to NCI**. Example: sub profit ₹1,00,00,000 → NCI ₹20,00,000 shown separately in equity and in the P&L split.

**Step 6 — Group reports.** Run the consolidated P&L, BS, and the movement/flow reports; controllers review; the submission is signed off and the group set is locked.

## The output

A consolidation elimination journal (group level, 2026.07):

| Line | Account | Entity | Trading Partner | Dr (₹) | Cr (₹) |
|---|---|---|---|---|---|
| 1 | IC Payable | IN01 | GB01 | 8,00,000 | |
| 2 | IC Receivable | GB01 | IN01 | | 8,00,000 |
| 3 | IC Revenue | GB01 | IN01 | 8,00,000 | |
| 4 | IC Cost of services | IN01 | GB01 | | 8,00,000 |

NCI carve-out (80%-owned sub, profit ₹1,00,00,000):

| Description | ₹ |
|---|---|
| Sub net profit (100% consolidated) | 1,00,00,000 |
| Attributable to parent (80%) | 80,00,000 |
| **Non-controlling interest (20%)** | **20,00,000** |

Plus a translated, eliminated, consolidated set: Group Revenue, Group EBIT, Group Net Profit split parent/NCI, and CTA sitting in OCI.

## Checks & gotchas

- **IC must net to zero after elimination.** If group IC receivables ≠ IC payables, a mismatch is unresolved — the classic close-blocker.
- **Translation gotcha:** using closing rate on the P&L (should be average) or average on the balance sheet is the most common error; CTA absorbs the mistake silently, so the balance still "balances" while being wrong.
- **Flow dimension:** FX movement and asset roll-forwards break if opening + movements ≠ closing.
- **Investment elimination** must use the *acquisition-date* rate for goodwill, not the current rate.
- **Rounding:** consolidated statements are often in thousands/millions — rounding differences need a defined tolerance, not manual fudging.
- **Locked periods:** once submitted and locked, changes need a **re-open + re-submit**, which is audited.

## Interview drill

**Q: What's the difference between elimination and translation?**
A: Translation converts a foreign entity's local-currency numbers into the group currency (P&L at average, BS at closing, equity at historical, difference to CTA in OCI). Elimination removes *intragroup* transactions and balances (IC receivable/payable, IC revenue/cost, investment vs share capital, unrealised profit) so the group isn't double-counting internal activity. They're sequential: translate each entity first, then eliminate at group level.

**Q: How is minority/non-controlling interest handled in consolidation?**
A: For a partly-owned subsidiary you still consolidate 100% of assets, liabilities, income and expenses line-by-line (control, not ownership %, drives consolidation). Then you carve out the non-controlling shareholders' share of net assets and of profit — say 20% for an 80%-owned sub — presented separately within equity and as a split of profit for the year.

**Q: Walk me through a BPC monthly submission.**
A: Load the entity trial balance via the data manager package (or EPM Excel input), run validation to confirm it balances and control accounts tie, load rates and run currency translation, review the IC matching report and clear mismatches with counterparties, submit and lock the entity. At group level, controllers run eliminations, review the consolidated set, and lock the group version.

## Practise free

You can't get a free SAP BPC tenant, so **rebuild the logic in Excel** — which is exactly how many analysts prototype anyway:
- Build three entity tabs (IN01, GB01, US01), each a mini trial balance with a **Trading Partner** column.
- A **rates tab** (avg/closing/historical); use `SUMPRODUCT`/lookup to translate each entity to a group-currency tab; plug the difference to a CTA line.
- An **IC matching tab**: `SUMIFS` each entity's IC receivable against the counterparty's IC payable, flag non-zero gaps with conditional formatting.
- An **elimination tab** that posts the reversing group journals, then a **consolidation tab** = sum of entities + eliminations, with an NCI carve-out row.
- Free reading to ground the vocabulary: **IAS 21** (translation), **IFRS 10** (consolidation/control), **IFRS 3** (goodwill/NCI) — the ICAI Advanced Accounting module and the IFRS Foundation summaries are free. Oracle's public **FCCS/HFM** admin guides describe the same package/journal/elimination flow if you want a second vendor's vocabulary.
