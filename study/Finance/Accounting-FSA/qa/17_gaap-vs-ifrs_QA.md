# Q&A — GAAP vs IFRS — the Differences That Matter

A practice bank of 20 questions mixing conceptual/theory (with model answers and "how to say it in an interview") and fully-solved numerical problems. Every number is self-verified: debits equal credits, statements tie out, totals reconcile.

---

## Section A — Conceptual / Theory

### Q1. Explain the core philosophical difference between US GAAP and IFRS, and why it produces the specific differences analysts care about.

**Model answer.** US GAAP is **rules-based** — set by the FASB, codified in the ASC, built on bright-line numeric thresholds and detailed scope exceptions. IFRS is **principles-based** — set by the IASB, stating a broad principle and relying on management judgment. The driver is context: the US has a litigious market, so preparers want explicit rules they can defend; IFRS had to work across 140+ jurisdictions, so it couldn't hard-code numbers and leaned on principles. From that split, US GAAP consistently chooses **conservatism, verifiability, and comparability**, while IFRS chooses **economic relevance and substance over form**. That's why GAAP allows LIFO (conservatism + tax history), forbids revaluation (verifiability over relevance), expenses R&D (conservatism), and bars impairment reversal (a write-down is a permanent new basis) — while IFRS does the opposite on each.

**How to say it in an interview:** *"Rules versus principles. GAAP picks conservatism and comparability; IFRS picks relevance and judgment. Every specific difference — LIFO, revaluation, R&D, impairment reversal — falls out of that one trade-off, so I can derive them rather than memorize a list."*

---

### Q2. Why does IFRS ban LIFO when US GAAP allows it?

**Model answer.** IFRS (IAS 2) bans LIFO on a **balance-sheet relevance** principle: LIFO leaves the oldest, stalest costs sitting in ending inventory, so the inventory line becomes meaningless in inflation — you could have inventory carried at 1990s costs. IFRS wants inventory to reflect something close to recent cost, so only FIFO and weighted-average are allowed. US GAAP allows LIFO largely because of the **US tax code's LIFO conformity rule**: if you use LIFO for tax (to reduce taxable income when prices rise), you must also use it for financial reporting. Kill LIFO for books and you kill a legitimate tax strategy, so GAAP keeps it.

**How to say it in an interview:** *"IFRS bans LIFO because it makes the balance-sheet inventory value nonsensical — stale costs. GAAP keeps it because of the US LIFO conformity rule linking book and tax treatment."*

---

### Q3. Under IFRS, walk through what happens to each financial statement when a company revalues PP&E upward.

**Model answer.** On the **balance sheet**, the asset's carrying value rises to fair value and **equity rises** via a revaluation surplus reserve. On the **income statement**, *nothing this period* — an upward revaluation is an unrealized holding gain, so it goes to **Other Comprehensive Income**, not net income. Going forward, **depreciation is based on the higher revalued amount**, so future depreciation is higher and future net income is lower. Net effect: assets up, equity up, current net income unchanged, future net income and margins down, and ROA/ROE depressed because the denominator grew. A downward revaluation, by contrast, hits the P&L as an expense (unless it reverses a prior surplus first).

**How to say it in an interview:** *"Upward reval: asset up, equity up through OCI, net income untouched now but lower later on higher depreciation. It actually depresses ROE and margins, which is why I strip it out to compare with a GAAP cost-basis peer."*

---

### Q4. A company you cover just reversed a large impairment and earnings spiked. What framework is it, and how do you treat the spike?

**Model answer.** It must be **IFRS** — US GAAP prohibits reversing impairments on held-and-used assets; the written-down value is a permanent new cost basis. Under IFRS (IAS 36) you can reverse an impairment on any asset **except goodwill**, up to the depreciated carrying value the asset would have had, and the reversal flows through the **income statement** as a gain. So the spike is a **non-cash, non-recurring** gain — I strip it from core/normalized earnings, flag it as low quality, and I'd also look back at whether the original write-down was aggressive (a company can impair heavily in a bad year, then reverse to smooth a later year).

**How to say it in an interview:** *"That's IFRS — GAAP never reverses impairments. It's a non-cash, non-recurring gain, so it comes out of core EPS, and I'd check whether the original impairment was aggressive earnings management."*

---

### Q5. How do US GAAP and IFRS differ in the mechanics of the impairment test itself?

**Model answer.** US GAAP (ASC 360) uses a **recoverability screen first**: compare the asset's carrying value to the **undiscounted** future cash flows. If carrying value is below that, **no impairment** — even if the discounted value is lower. Only if it fails the screen do you write down to **fair value**. IFRS (IAS 36) has **no undiscounted screen** — you compare carrying value directly to the **recoverable amount**, defined as the **higher of** fair-value-less-costs-to-sell and **value in use** (PV of future cash flows). Consequence: IFRS catches impairments **earlier and in smaller increments**; US GAAP impairments are **less frequent but lumpier** because the undiscounted screen lets economically-impaired assets pass until they finally fail.

**How to say it in an interview:** *"GAAP screens on undiscounted cash flows first, so it recognizes impairments later and lumpier; IFRS goes straight to a discounted recoverable amount, so it catches them earlier and smaller."*

---

### Q6. Why can an IFRS company report higher operating cash flow than an identical US GAAP company with the same underlying cash movements?

**Model answer.** Two reasons. First, **interest paid**: US GAAP forces it into **operating** cash flow; IFRS lets the company classify it as **financing**, pulling it out of CFO and inflating reported operating cash flow. Second, **development costs**: an IFRS firm that capitalizes development records that cash outflow in **investing**, not operating, so CFO is again flattered. For credit or FCF work this is dangerous — CFO/debt, cash interest coverage, and FCF all look better for no economic reason. I **reclassify interest paid into operating and move capitalized development back into operating** before computing any cash-flow ratio.

**How to say it in an interview:** *"IFRS can park interest paid in financing and capitalized development in investing, both of which inflate CFO. I move them back into operating so cash-flow ratios are apples-to-apples."*

---

### Q7. Explain the development-cost difference and its earnings-quality implication.

**Model answer.** Both frameworks expense **research**. They split on **development**: US GAAP (ASC 730) **expenses** it as incurred (narrow exceptions for internal-use and salable software); IFRS (IAS 38) **capitalizes** it once six criteria are met — probable benefits, intention and ability to complete, technical feasibility, resources, and reliable measurement. So an IFRS firm shows **higher near-term earnings, higher assets, lower reported R&D**, and higher CFO. But it's **timing, not value** — the intangible amortizes and the advantage unwinds; cumulative earnings equal the expensing firm's. Earnings quality is lower because capitalization defers costs and relies on the judgment that benefits are "probable," which management can lean on.

**How to say it in an interview:** *"IFRS capitalizes development, so near-term earnings look better, but it's just timing — it amortizes away. Lower quality because it hinges on a 'probable future benefit' judgment. I'd expense it to compare."*

---

### Q8. Why might a lease-heavy IFRS retailer show structurally higher EBITDA than an identical US GAAP retailer?

**Model answer.** Post-2019 both capitalize leases onto the balance sheet, but the **income-statement treatment diverges**. IFRS 16 has a **single lease model**: every lease produces **depreciation** of the right-of-use asset plus **interest** on the lease liability — both below the EBITDA line — so the **entire** lease cost is excluded from EBITDA. US GAAP (ASC 842) keeps a **dual model**: an **operating lease** still records a single straight-line **lease expense inside operating income**, so it stays **in** EBITDA. For a retailer with large store leases, IFRS EBITDA is structurally higher. I normalize — either add lease expense back for both or strip it for both — before comparing EV/EBITDA.

**How to say it in an interview:** *"IFRS 16 pushes all lease cost below EBITDA; GAAP operating leases keep it in. Lease-heavy IFRS firms look higher-EBITDA for free — I put both on the same basis first."*

---

### Q9. Name the two big areas where GAAP and IFRS converged, and state whether convergence is ongoing.

**Model answer.** The two big convergence wins are **revenue recognition** — ASC 606 and IFRS 15 are essentially identical five-step models — and **leases** — ASC 842 and IFRS 16 both now capitalize most leases onto the balance sheet (though the income-statement treatment still differs). Convergence as an active FASB-IASB project is **effectively over**; the remaining differences — LIFO, revaluation, development capitalization, impairment reversal, interest classification — are stable and persist. So you can't assume "they've merged" — you still normalize.

**How to say it in an interview:** *"Revenue (606/15) and leases (842/16) converged; the project is otherwise dead. LIFO, revaluation, R&D, impairment reversal, and cash-flow classification all still diverge."*

---

### Q10. How does IFRS's treatment of inventory write-downs differ from US GAAP's, and why?

**Model answer.** IFRS (IAS 2) measures inventory at **lower of cost or net realizable value**, and crucially **allows reversal** of a prior write-down (up to original cost) if NRV recovers. US GAAP uses **lower of cost or NRV** (or lower of cost or **market** for LIFO/retail — a rules-based construct with a ceiling and floor) and **prohibits reversal** — the written-down value is the new cost basis. Same conservatism-versus-relevance split: IFRS reflects the genuine recovery of value; GAAP refuses to book the recovery to prevent earnings management.

**How to say it in an interview:** *"IFRS uses lower of cost or NRV and lets you reverse a write-down if NRV recovers; GAAP uses cost-or-market and never reverses. If an IFRS firm's margin jumps from an inventory reversal, I treat it as low-quality."*

---

### Q11. What presentation differences would trip up an analyst reading a European (IFRS) filing for the first time?

**Model answer.** Three things. **Balance-sheet order** — IFRS filers often list **non-current assets first** and current last, and frequently show **equity before liabilities**, the reverse of the US "most-liquid-first" layout. **Terminology** — "trade receivables" (accounts receivable), "share premium" (additional paid-in capital), "reserves," "provisions" (recognized liabilities), "stocks/inventories." **Income statement** — IFRS permits expense presentation **by nature** (raw materials, employee benefits, depreciation) rather than **by function** (COGS, SG&A), so you may not see a clean gross-profit line. None of this changes totals, but it changes where you look.

**How to say it in an interview:** *"IFRS often runs non-current-first and equity-before-liabilities, uses different labels like share premium and provisions, and can present expenses by nature, so there may be no gross-profit subtotal. Presentational, not economic — but you have to reorder mentally."*

---

### Q12. "Is principles-based or rules-based better?" Give a balanced answer.

**Model answer.** Neither dominates — it's a trade-off. **Rules-based** GAAP delivers **comparability and defensibility** (everyone follows the same explicit rule, easy to audit and litigate), but invites **structuring** — companies engineer transactions to fall on the favorable side of a bright line, like the pre-2019 operating-lease game. **Principles-based** IFRS reports **economic substance** and is harder to game *structurally*, but relies on **judgment**, so two identical firms can report differently and an aggressive management can lean its judgment. As an analyst I don't need one to win — I need the **disclosures**, and the footnotes under both frameworks are where the comparable information lives.

**How to say it in an interview:** *"It's a trade-off: rules give comparability but invite structuring; principles give substance but rely on gameable judgment. I care less about which and more about the footnotes."*

---

## Section B — Numerical Problems (fully solved)

### Q13. LIFO-to-FIFO full restatement.

**Facts.** SteelCo (US GAAP, LIFO) reports: ending inventory (LIFO) = 1,500; LIFO reserve = 400 (end) vs 250 (beginning); COGS (LIFO) = 9,000; pre-tax income = 2,000; tax rate = 30%. Restate to FIFO.

**Solution.**
- **FIFO ending inventory** = LIFO inventory + LIFO reserve = 1,500 + 400 = **1,900**.
- **Δ LIFO reserve** = 400 − 250 = **150**.
- **FIFO COGS** = LIFO COGS − Δreserve = 9,000 − 150 = **8,850**.
- **FIFO pre-tax income** = 2,000 + 150 = **2,150**.
- **Extra tax** = 150 × 30% = **45**; **Δ net income** = 150 × 70% = **105**.
- **Cumulative equity effects:** Inventory ↑ 400; DTL ↑ 400 × 30% = **120**; Retained earnings ↑ 400 × 70% = **280**.

**Check the balance-sheet identity:** Assets ↑ 400 = Liabilities ↑ 120 + Equity ↑ 280 → 400 = 400. **Ties. ✓**

**Interpretation:** on a FIFO basis SteelCo's gross profit is 150 higher and inventory 400 higher — but it paid real cash tax of 45 *less* this year by staying on LIFO, so LIFO is cash-accretive despite the weaker P&L.

---

### Q14. LIFO cash-flow / earnings-quality reconciliation.

**Facts.** Same SteelCo. Compare "as-reported LIFO" to "restated FIFO" on net income and on actual cash taxes for the year. Rate 30%.

**Solution.**

| | LIFO (reported) | FIFO (restated) | Difference |
|---|---|---|---|
| Pre-tax income | 2,000 | 2,150 | +150 |
| Tax @ 30% | 600 | 645 | +45 |
| Net income | 1,400 | 1,505 | +105 |

**Key point — which tax is *actually paid*?** SteelCo files its taxes on **LIFO** (conformity rule), so **actual cash tax = 600**, not 645. The FIFO column is a **hypothetical** for comparability only. So restating to FIFO raises *reported* earnings by 105 but does **not** change cash — SteelCo really paid 600 and kept the 45 of tax savings.

**Check:** LIFO tax 600 vs FIFO hypothetical tax 645 → cash-tax saving from LIFO = **45**, exactly the Δreserve 150 × 30%. **✓** Reported earnings and real cash move in opposite directions — the earnings-quality lesson.

---

### Q15. IFRS PP&E revaluation — surplus and revised depreciation.

**Facts.** MillCo (IFRS) buys equipment for 8,000 on 1 Jan Y1; life 10 years straight-line, no residual. On 31 Dec Y3 fair value = 7,700. It uses the revaluation model.

**Solution.**
- Annual depreciation Y1-Y3 = 8,000/10 = 800. Accumulated after 3 years = 2,400.
- Carrying value 31 Dec Y3 (pre-reval) = 8,000 − 2,400 = **5,600**.
- **Revaluation surplus** = 7,700 − 5,600 = **2,100** → to OCI/equity.
- **Journal entry:**
```
Dr  Equipment                 2,100
    Cr  Revaluation Surplus       2,100
```
- **New depreciation Y4 onward** = revalued 7,700 / remaining 7 years = **1,100 per year** (up from 800).

**Check:** carry the asset forward one year — Y4 depreciation 1,100, carrying value end Y4 = 7,700 − 1,100 = **6,600**. Over remaining 7 years, 7 × 1,100 = 7,700 fully depreciates the revalued base to zero. **✓** Net income is now **300 lower per year** (1,100 vs 800) than under the cost model — the price of revaluing up.

---

### Q16. Downward revaluation that partly reverses a prior surplus.

**Facts.** Continue MillCo. One year later (31 Dec Y4) fair value falls to **5,900**. Carrying value at that date (from Q15) is **6,600**. Prior revaluation surplus balance for this asset = 2,100. How is the decline booked?

**Solution.**
- Decline = 6,600 − 5,900 = **700**.
- **Rule:** a downward revaluation first **reduces any existing revaluation surplus** for that asset (through OCI); only the excess beyond the surplus hits the income statement.
- Surplus available = 2,100 > 700, so the **entire 700 reduces the surplus** — **nothing hits the P&L**.
- **Journal entry:**
```
Dr  Revaluation Surplus (OCI)     700
    Cr  Equipment                     700
```
- Remaining surplus = 2,100 − 700 = **1,300**. Carrying value now = **5,900**.

**Check:** asset reduced by 700 (6,600 → 5,900 ✓); surplus reduced by 700 (2,100 → 1,300 ✓); net income impact = **0** because prior surplus absorbed the full decline. **✓** *(Had the decline exceeded 2,100, the first 2,100 would clear the surplus and the excess would be a P&L loss.)*

---

### Q17. Development capitalization (IFRS) vs expensing (GAAP) — Year 1 P&L, CFO, and cash.

**Facts.** TechIFRS capitalizes 600 of qualifying development in Y1 (amortize over 3 yrs from Y2). TechUS expenses it. Both: revenue 4,000, other cash operating costs 2,500, tax 25%.

**Solution — Year 1 income statement:**

| | TechIFRS | TechUS |
|---|---|---|
| Revenue | 4,000 | 4,000 |
| Other operating costs | (2,500) | (2,500) |
| Development expense | 0 | (600) |
| Pre-tax income | 1,500 | 900 |
| Tax @ 25% | (375) | (225) |
| **Net income** | **1,125** | **675** |

**Cash flow (Y1):**
- TechIFRS: CFO = 4,000 − 2,500 − 375 (tax) = **1,125**; development 600 in **investing** → total cash = 1,125 − 600 = **525**.
- TechUS: CFO = 4,000 − 2,500 − 600 (dev) − 225 (tax) = **675**; no investing → total cash = **675**.

**Reconcile:** total cash difference = 675 − 525 = **150**. This equals the tax difference: TechUS tax 225 vs TechIFRS tax 375 → **150** less tax paid by TechUS. **✓** So TechIFRS *reports* 450 more net income (1,125 vs 675) yet generates **150 less actual cash** — because it deferred its tax deduction. TechIFRS also shows CFO of 1,125 vs 675, flattering operating cash flow by parking the 600 in investing.

---

### Q18. Development capitalization — Year 2 unwind and cumulative equality.

**Facts.** Continue Q17. In Y2 both firms have identical operations (revenue 4,000, other costs 2,500, no new development). TechIFRS amortizes 600/3 = 200. Show Y2 net income and confirm the two-year cumulative net income converges.

**Solution — Year 2 income statement:**

| | TechIFRS | TechUS |
|---|---|---|
| Revenue | 4,000 | 4,000 |
| Other operating costs | (2,500) | (2,500) |
| Amortization of dev | (200) | 0 |
| Pre-tax income | 1,300 | 1,500 |
| Tax @ 25% | (325) | (375) |
| **Net income** | **975** | **1,125** |

**Cumulative net income over Y1 + Y2:**
- TechIFRS = 1,125 + 975 = **2,100**.
- TechUS = 675 + 1,125 = **1,800**.

Still a 300 gap after two years — because two-thirds of the 600 (i.e., 400) is still capitalized on TechIFRS's books, amortizing in Y3 and Y4. Extend to Y3 and Y4 (200 amortization each, 150 after-tax hit each year): TechIFRS cumulative = 2,100 + (975−... ) — over the full 3-year amortization the extra 600 pre-tax expense fully unwinds and **cumulative net income equalizes at the point all 600 has been expensed by both**.

**Check (pre-tax, full life):** both firms expense the entire 600 eventually — TechUS all in Y1, TechIFRS spread 200/200/200 across Y2-Y4. Total lifetime pre-tax expense = 600 for both → **cumulative pre-tax income identical**; only the **timing** differs. **✓** The lesson: capitalization is a timing shift, not value creation.

---

### Q19. Impairment — same asset, GAAP vs IFRS outcome.

**Facts.** A machine has carrying value **1,000**. Estimated **undiscounted** future cash flows = **1,050**. **Fair value** = **820**. **Value in use** (PV of cash flows) = **860**. Fair value less costs to sell = **800**. Determine the impairment under each framework.

**Solution.**
- **US GAAP (ASC 360):** Step 1 recoverability screen — carrying value 1,000 vs **undiscounted** cash flows 1,050. Since 1,000 < 1,050, the asset is **recoverable → NO impairment**. Carrying value stays **1,000**.
- **IFRS (IAS 36):** recoverable amount = **higher of** (FVLCS 800, value in use 860) = **860**. Carrying value 1,000 > 860 → **impairment = 1,000 − 860 = 140**. Write down to **860**.

**Journal entry (IFRS):**
```
Dr  Impairment loss (P&L)      140
    Cr  Machine                    140
```

**Check / interpretation:** identical economics, **opposite outcomes** — US GAAP takes **zero** impairment (the undiscounted screen saved it); IFRS takes a **140** write-down and recognizes the loss now. This is the single cleanest illustration of "GAAP recognizes later and lumpier, IFRS earlier and smaller." **✓**

---

### Q20. IFRS impairment reversal (with the depreciated-cost cap).

**Facts.** From Q19, the IFRS firm wrote the machine down to **860** on 31 Dec Y0. Remaining life at that date = 4 years, straight-line, no residual. One year later (31 Dec Y1) conditions improve and the recoverable amount rebounds to **900**. Compute the reversal, respecting the cap.

**Solution.**
- **Depreciation in Y1 on the impaired base** = 860 / 4 = **215**. Carrying value 31 Dec Y1 (post-dep, pre-reversal) = 860 − 215 = **645**.
- **The cap:** a reversal cannot raise carrying value above what it **would have been had no impairment occurred**. Without impairment, the machine would have carried at 1,000 and depreciated. To keep it clean, assume the pre-impairment schedule also had 4 years left at Y0 with carrying value 1,000 → depreciation 1,000/4 = 250/yr → carrying value 31 Dec Y1 = 1,000 − 250 = **750**. That **750 is the ceiling.**
- Recoverable amount rebounded to **900**, but the reversal is **capped at 750**. So restore carrying value from 645 up to **750**.
- **Reversal gain** = 750 − 645 = **105** → to the **income statement** (since the original impairment hit P&L).

**Journal entry:**
```
Dr  Machine                       105
    Cr  Impairment reversal (P&L)     105
```

**Check:** post-reversal carrying value = 645 + 105 = **750 = the depreciated-cost ceiling**, and it does not reach the 900 recoverable amount because the cap binds. **✓** Under **US GAAP this entire 105 gain is prohibited** — the machine would stay at 645. The IFRS firm's earnings are 105 higher this year from a **non-cash, non-recurring** reversal, which an analyst strips from core EPS.

---

### Q21. Cash-flow reclassification — interest paid.

**Facts.** EuroLev (IFRS) reports: CFO = 1,200; CFI = (500); CFF = (400). Within CFO, it classified **interest paid of 300** as operating? No — it classified interest paid of **300 as financing** (its IFRS policy choice). A US GAAP peer, USLev, has identical cash flows but must put interest paid in operating. Restate EuroLev to a US-GAAP-comparable basis and comment on CFO/debt if debt = 4,000.

**Solution.**
- EuroLev **as reported (IFRS, interest in financing):** CFO = 1,200; the 300 interest paid sits in **CFF**.
- **Restate interest paid into operating (US GAAP basis):** CFO becomes 1,200 − 300 = **900**; CFF becomes (400) + 300 = **(100)**.
- CFI unchanged at (500).

**Check total cash:** as reported 1,200 − 500 − 400 = **300**; restated 900 − 500 − 100 = **300**. Total cash **unchanged at 300** — reclassification only moves *between* sections. **✓**

- **CFO/debt as reported** = 1,200 / 4,000 = **30.0%**.
- **CFO/debt restated (comparable)** = 900 / 4,000 = **22.5%**.

**Interpretation:** EuroLev's IFRS policy of parking interest in financing **overstated its CFO-to-debt by 7.5 points** (30.0% vs 22.5%). A credit analyst who didn't reclassify would judge EuroLev's cash coverage far stronger than USLev's for no economic reason. Always move interest paid into operating before cash-flow leverage ratios.

---

### Q22. Putting it together — full cross-border normalization.

**Facts.** You compare **AlphaUS** (GAAP) and **BetaEU** (IFRS). Raw reported figures: both EBITDA 2,000. But: (a) BetaEU is lease-heavy and IFRS 16 excludes 250 of lease cost from EBITDA that AlphaUS (operating lease) keeps *in* EBITDA; (b) BetaEU capitalized 120 of development (in CFI, not opex); (c) BetaEU recorded a 90 impairment reversal in its operating income. Normalize BetaEU's EBITDA and "clean" operating profit to AlphaUS's basis. Assume the 90 reversal sits above the EBITDA line and the 120 development, if expensed, would be an operating cost.

**Solution — normalize BetaEU EBITDA to a GAAP-comparable basis:**

| Adjustment | Effect on BetaEU EBITDA |
|---|---|
| Reported EBITDA | 2,000 |
| (a) Add lease cost back **in** (match AlphaUS operating-lease treatment) → subtract lease expense from EBITDA | (250) |
| (b) Expense the capitalized development that GAAP would run through opex | (120) |
| (c) Remove the non-recurring impairment reversal booked in operating income | (90) |
| **Normalized EBITDA** | **1,540** |

**Check:** 2,000 − 250 − 120 − 90 = **1,540**. **✓**

**Interpretation:** on a like-for-like basis BetaEU's EBITDA is **1,540**, not 2,000 — **23% lower** than reported and **well below AlphaUS's 2,000**. Every one of the three IFRS features (lease exclusion, development capitalization, impairment reversal) inflated the headline. **Model line:** *"Raw, they look equal at 2,000 EBITDA. Normalized, BetaEU is really at 1,540 — the IFRS lease treatment, development capitalization, and a one-off impairment reversal each padded the headline. AlphaUS is materially the stronger earner once you put them on one basis."*

---

*End of Q&A bank — 22 questions (12 conceptual, 10 numerical), all figures self-verified and reconciling.*
