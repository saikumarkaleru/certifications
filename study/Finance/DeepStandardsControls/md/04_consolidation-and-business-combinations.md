# Consolidation & Business Combinations: IFRS 10 / IFRS 3

## What you'll be able to do

Decide whether one entity **controls** another (IFRS 10 / Ind AS 110), then actually *build the consolidated balance sheet* — add the parent and subsidiary line by line, **eliminate** the investment against equity, carve out **non-controlling interest (NCI)**, and compute **goodwill**. Perform the **purchase price allocation (PPA)** in a business combination (IFRS 3 / Ind AS 103): fair-value the assets and liabilities acquired and land the residual as goodwill. And apply the **equity method** (IAS 28 / Ind AS 28) for associates where you have significant influence but not control. You'll do a full worked consolidation with the elimination entries a reviewer will check.

## The essentials

**Control (IFRS 10) — all three:** (1) **power** over the investee (usually >50% voting, but substance matters — potential voting rights, contractual power), (2) **exposure to variable returns**, and (3) **ability to use power to affect those returns**. Control → **full consolidation**.

**Influence spectrum:**

| Holding / relationship | Standard | Treatment |
|---|---|---|
| **Control** | IFRS 10 / Ind AS 110 | Line-by-line consolidation + NCI |
| **Significant influence** (usually 20–50%) | IAS 28 / Ind AS 28 | **Equity method** |
| **Joint control** | IFRS 11 / Ind AS 111 | JV: equity method; JO: share of assets |
| **< 20%, no influence** | IFRS 9 / Ind AS 109 | Financial asset (FVTPL/FVOCI) |

**Business combination (IFRS 3) — acquisition method, 4 steps:** (1) identify the acquirer; (2) determine acquisition date; (3) recognise and **fair-value** identifiable assets acquired, liabilities assumed (including previously unrecognised intangibles — brands, customer relationships); (4) recognise **goodwill or a bargain-purchase gain**.

**Goodwill formula:**
```
Goodwill = Consideration transferred
         + NCI (at fair value OR at % of net identifiable assets — a policy choice)
         + fair value of any previously held interest
         − fair value of net identifiable assets acquired
```
Negative result = **bargain purchase**, recognised as a **gain in P&L** (after a reassessment).

**NCI measurement — two allowed methods (IFRS 3):**
- **Full goodwill** — NCI at fair value; goodwill includes NCI's share.
- **Partial goodwill** — NCI at its proportionate share of net identifiable assets; goodwill = parent's share only.

**Goodwill is not amortised** under IFRS/Ind AS — it's tested annually for impairment (IAS 36 / Ind AS 36). (US GAAP private-company relief allows amortisation; the default public model is also impairment-only.)

**Ind AS 103 carve-out:** **common-control** combinations use **pooling-of-interests** (book values, no goodwill) — IFRS 3 scopes those out entirely.

## Hands-on — step by step

**Facts.** On 1 Jan, ParentCo buys **80%** of SubCo for **₹8,00,000 cash**. SubCo's equity on that date: share capital ₹5,00,000, retained earnings ₹3,00,000 (book net assets ₹8,00,000). Fair-value review: SubCo's land is worth **₹1,00,000 more** than book. Use the **full-goodwill** method; NCI fair value = **₹1,90,000**.

**Step 1 — Fair-value the net identifiable assets.**
```
Book net assets                    8,00,000
+ Land fair-value uplift           1,00,000
Fair value of net identifiable     9,00,000
```

**Step 2 — Goodwill (full method).**
```
Consideration                      8,00,000
+ NCI at fair value                1,90,000
                                  ----------
Total                              9,90,000
− FV of net identifiable assets   (9,00,000)
Goodwill                             90,000
```
*(Check under partial method: NCI = 20% × 9,00,000 = 1,80,000; goodwill = 8,00,000 + 1,80,000 − 9,00,000 = 80,000. Difference ₹10,000 = NCI's share of goodwill.)*

**Step 3 — Elimination entry (on consolidation, day 1):**
```
Dr Share capital (SubCo)        5,00,000
Dr Retained earnings (SubCo)    3,00,000
Dr Land (FV uplift)             1,00,000
Dr Goodwill                       90,000
   Cr Investment in SubCo               8,00,000
   Cr NCI                               1,90,000
```
This removes the parent's investment and the sub's pre-acquisition equity, brings in the FV uplift and goodwill, and sets up NCI. (Debits 9,90,000 = credits 9,90,000.)

**Step 4 — Intercompany elimination (example).** If ParentCo sold goods to SubCo for ₹50,000 (cost ₹40,000) and SubCo still holds them, eliminate the **unrealised profit ₹10,000** and the intra-group receivable/payable:
```
Dr Revenue (or COGS)   10,000
   Cr Inventory               10,000
Dr Payables (intra)    <amt>
   Cr Receivables (intra)     <amt>
```

**Step 5 — Post-acquisition NCI share.** If SubCo earns ₹1,00,000 profit in Year 1, NCI gets 20% = **₹20,000** added to NCI, and the group's consolidated retained earnings include 80% = ₹80,000.

**Step 6 — Equity method (if it were an associate instead).** Say ParentCo instead held **30%** of AssocCo bought for ₹3,00,000; AssocCo earns ₹2,00,000 and pays ₹50,000 dividend:
```
Dr Investment in associate   60,000   (30% × 2,00,000 share of profit)
   Cr Share of profit (P&L)         60,000
Dr Bank                      15,000   (30% × 50,000 dividend)
   Cr Investment in associate       15,000
```
Carrying value = 3,00,000 + 60,000 − 15,000 = **₹3,45,000**. No line-by-line consolidation — one net line.

## The output

**Consolidated balance sheet build (day 1 extract, ₹):**

| Line | Parent | Sub | Adj | Consolidated |
|---|---|---|---|---|
| Investment in SubCo | 8,00,000 | — | (8,00,000) | 0 |
| Goodwill | — | — | +90,000 | 90,000 |
| Land | (incl. below) | book | +1,00,000 | book + 1,00,000 |
| Net assets (other) | … | … | — | added across |
| **Equity — parent** | share cap + RE | eliminated | | parent only |
| **NCI** | — | — | +1,90,000 (+20k Yr1) | 1,90,000 → 2,10,000 |

**Goodwill note:** "Goodwill of ₹90,000 arose on the 80% acquisition of SubCo; NCI measured at fair value (full-goodwill method); goodwill tested annually for impairment, not amortised."

**Equity-method line (associate alternative):** "Investment in associate ₹3,45,000 — cost ₹3,00,000 + share of profit ₹60,000 − dividend ₹15,000."

## Checks, gotchas & red flags

- **Goodwill uses fair-valued net assets**, not book — forgetting the land uplift (here ₹1,00,000) over-states goodwill. Fair-value first, then compute the residual.
- **Full vs partial goodwill changes only goodwill and NCI**, never the sub's assets. Know which method the policy uses before you compute.
- **Eliminate the *full* investment against the *full* pre-acquisition equity** — NCI absorbs its share; don't consolidate only 80% of the sub's assets. You add **100%** of the subsidiary's assets and liabilities and *then* show NCI in equity.
- **Unrealised intra-group profit** in closing inventory/PP&E must be eliminated — leaving it inflates consolidated profit and assets.
- **Dividends from a subsidiary** are eliminated in full (intra-group); from an **associate** they *reduce the investment carrying amount*, not income (income is the share of profit).
- **Bargain purchase** (negative goodwill) is a **P&L gain**, not a liability — but reassess the fair values first; a real bargain is rare and reviewers probe it.
- **Common control (Ind AS 103):** don't compute goodwill — use **pooling of interests** at book values. Applying acquisition method to a group reshuffle is wrong under Ind AS.
- **NCI must roll forward:** opening NCI + NCI's share of post-acquisition profit − NCI dividends. Static NCI across years is a red flag.

## Interview drill

**Q1: "Parent buys 80% for ₹8L; sub's fair-valued net assets are ₹9L; NCI fair value ₹1.9L. Goodwill?"**
A: Full-goodwill: consideration ₹8L + NCI ₹1.9L − net identifiable assets ₹9L = **₹90,000**. Under partial goodwill, NCI = 20% × ₹9L = ₹1.8L, giving goodwill ₹80,000 — the ₹10,000 gap is NCI's share of goodwill. Note the sub's net assets are **fair-valued** (including the land uplift) before taking the residual.

**Q2: "When do you consolidate vs use the equity method?"**
A: Consolidate when you have **control** (IFRS 10) — power, exposure to variable returns, and the ability to use power to affect them, usually >50% voting but substance can override. Use the **equity method** (IAS 28) for **significant influence**, typically 20–50%, where you get a single net line — cost plus share of post-acquisition profit less dividends received — not line-by-line consolidation.

**Q3: "Is goodwill amortised, and how is NCI's share of profit handled?"**
A: Under IFRS/Ind AS goodwill is **not amortised** — it's tested annually for impairment under IAS 36; impairment is irreversible. NCI's share of the subsidiary's **post-acquisition** profit is added to NCI each period (e.g., 20% of ₹1L profit = ₹20,000), and NCI is presented **within equity**, separate from the parent's owners.

## Learn/practise (free)

- **IFRS 3 / IFRS 10 / IAS 28 illustrative examples** — free on the IFRS Foundation site; the goodwill and NCI examples map straight to interview questions.
- **ICAI Ind AS 103 / 110 / 28 educational material** — free PDFs, with the common-control pooling carve-out worked out.
- **Any listed group's annual report** — read the "basis of consolidation," goodwill, and NCI notes; reverse-engineer the elimination logic.
- **Rehearse in Excel:** build a three-column consolidation worksheet (Parent | Sub | Adjustments → Consolidated), post the elimination entry, prove debits = credits and that NCI + parent equity ties to total group equity. Then flip the same facts to an associate and show it collapses to one equity-method line.
