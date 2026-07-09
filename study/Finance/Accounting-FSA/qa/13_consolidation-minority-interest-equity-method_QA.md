# Q&A — Consolidation, Minority Interest & the Equity Method

A practice bank mixing conceptual questions (with model answers and interview phrasing) and fully-solved numerical problems. Every number is self-verified and reconciles.

---

## Section A — Conceptual / theory

### Q1. What determines whether you use cost/fair value, the equity method, or full consolidation?

**Model answer.** The **degree of influence or control**, for which ownership percentage is the usual proxy. No significant influence (typically < 20%) → fair value or cost, holding a financial asset. Significant influence but not control (typically 20–50%) → equity method, one line. Control (typically > 50%, but really the IFRS 10 control test: power, exposure to variable returns, ability to use power) → full consolidation.

**How to say it in an interview:** "The accounting follows substance — influence, not a raw percentage. The thresholds are rebuttable presumptions."

---

### Q2. Why is non-controlling interest classified as equity and not a liability?

**Model answer.** Consolidated statements adopt the single-entity view: the group controls 100% of the subsidiary's net assets. NCI is the residual claim of shareholders *outside* the parent on those net assets. A liability is an obligation to transfer economic resources; the group has no repayable obligation to the minority. So NCI is a component of total equity, presented separately from equity attributable to the parent.

**Interview line:** "NCI is other people's equity in something you control — it's a claim, not a debt."

---

### Q3. Why does enterprise value add minority interest but subtract associates?

**Model answer.** EV must be consistent with the operating flows it's compared against. Full consolidation puts **100%** of a subsidiary's EBITDA into the numerator, but market cap only reflects the parent's share — so you **add** minority interest to capture the full ownership matching the full EBITDA. Associates are the mirror image: their profit is a single equity-method line *below* EBITDA (not in it), while the investment's value is *inside* market cap — so you **subtract** the associate value to keep numerator and denominator aligned.

**Interview line:** "Match 100% of the flows with 100% of the claims; anything not in EBITDA shouldn't be in EV."

---

### Q4. A company owns 45% of another and consolidates it fully. How is that possible?

**Model answer.** Control isn't purely arithmetic. Under IFRS 10, control = power over relevant activities + exposure to variable returns + ability to use power to affect returns. With 45% and the remaining shares widely dispersed among passive holders, the 45% holder can have **de facto control** — effectively winning every vote. Potential voting rights (options, convertibles) can also confer control. If control exists, consolidate 100% and recognize 55% as NCI.

---

### Q5. Under the equity method, why isn't a dividend received treated as income?

**Model answer.** The equity method already recognizes your share of the associate's *earnings* as income (added to the investment's carrying value) when the associate earns them. A subsequent dividend is simply the associate distributing profits you've already recognized — a **return of capital**. Booking it as income too would double-count. So the dividend *reduces* the carrying value of the investment.

**Interview line:** "You take the earnings when they're earned; the dividend just converts investment into cash."

---

### Q6. What intercompany items must be eliminated on consolidation, and why?

**Model answer.** Because parent + subsidiaries are one economic entity, internal dealings must be removed: (1) intercompany revenue and COGS, (2) unrealized profit in inventory (and PP&E) still held within the group, (3) intercompany receivables and payables, (4) intercompany dividends, (5) intercompany loans and the related interest, and (6) the parent's investment account against the subsidiary's equity (replaced by the sub's actual net assets plus goodwill). A single entity can't earn revenue from itself, owe itself, or pay itself income.

---

### Q7. Full-goodwill vs partial-goodwill method — what's the difference?

**Model answer.** Both start from consideration paid. Under **full goodwill** (US GAAP mandatory; IFRS optional), NCI is measured at its **fair value**, so goodwill includes the minority's share of goodwill: Goodwill = Consideration + FV of NCI + FV of prior stake − FV of net identifiable assets. Under **partial goodwill** (IFRS option), NCI = NCI% × FV of net identifiable assets, and **no goodwill is attributed to NCI**: Goodwill = Consideration − Parent% × FV of net identifiable assets. Full goodwill produces higher goodwill and higher NCI on the balance sheet.

---

### Q8. Distinguish a joint venture from a joint operation.

**Model answer.** Both involve **joint control** (unanimous consent among the sharing parties for key decisions). In a **joint venture** the parties have rights to the *net assets* — accounted for with the **equity method** (one line, like an associate). In a **joint operation** the parties have direct rights to the *assets* and obligations for the *liabilities* — each party recognizes **its own share of each asset, liability, revenue and expense**, line by line (its share only, unlike full consolidation's 100% + NCI).

---

### Q9. How does buying above book value affect future profit under the equity method?

**Model answer.** Paying more than your share of the associate's book net assets means the excess is fair-value uplifts on identifiable assets plus embedded goodwill. Fair-value uplifts on *depreciable/amortizable* assets generate **extra depreciation/amortization**, which reduces your "share of profit of associate" in subsequent years — even though it's all buried in the single investment line. Embedded goodwill isn't amortized but the whole investment is tested for impairment.

---

### Q10. On the cash flow statement, how are an acquisition and subsequent minority dividends shown?

**Model answer.** The cash paid to acquire the subsidiary, **net of cash acquired**, is an **investing** outflow in the year of acquisition. Thereafter the subsidiary's operating cash flows are consolidated in full within operating activities. Dividends the subsidiary pays to its **minority** shareholders are a **financing** outflow (cash leaving the group to outside parties) and reduce NCI on the balance sheet; the portion paid to the parent is eliminated intragroup.

---

### Q11. A firm trades at 6x EV/EBITDA and looks cheap. What would make you cautious?

**Model answer.** Two consolidation issues can distort the multiple. First, large **associate earnings** sit below EBITDA (one equity-method line), so reported EBITDA understates the true earnings base and the multiple looks artificially low — I'd carve out the associate value from EV and value it separately. Second, if there's material **minority interest** I must add it to EV; failing to do so understates EV and flatters the multiple. Also check for one-offs and off-balance-sheet items. The clean comparison strips associates and adds minorities.

---

## Section B — Numerical problems (fully solved)

### Q12. Equity method roll-forward.

**Problem.** InvestCo buys 25% of AssocCo on 1 Jan for $500. AssocCo earns net profit of $240 for the year, records $20 of OCI gains, and pays total dividends of $80. No impairment. Compute the year-end carrying value and the P&L pickup.

**Solution.**
- Share of profit = 25% × 240 = **$60** (to P&L "share of profit of associate").
- Dividend received = 25% × 80 = **$20** (return of capital, reduces investment).
- Share of OCI = 25% × 20 = **$5** (to OCI, increases investment).

Roll-forward:
```
Opening                 500
+ Share of profit       +60
+ Share of OCI           +5
− Dividend received     −20
Closing                 545
```
**Answers:** carrying value = **$545**; P&L impact = **$60**; OCI impact = **$5**. Check: 500 + 60 + 5 − 20 = 545 ✓.

---

### Q13. Fair value vs equity method — same investee, contrast the P&L.

**Problem.** Two independent scenarios. Investee earns $200 net profit and pays $50 dividends; investee shares end the year 8% above the $400 cost. (a) You own 10% (FVTPL). (b) You own 25% (equity method). Compare income statement impact and closing investment.

**Solution.**
(a) **10% FVTPL:** dividend income = 10% × 50 = **$5**; FV gain = 8% × 400 = **$32** to P&L. **P&L = $37.** Closing investment = 400 × 1.08 = **$432**. (Share of earnings $20 is *not* recognized.)

(b) **25% equity method:** share of profit = 25% × 200 = **$50** to P&L; dividend = 25% × 50 = **$12.50** reduces investment; FV change ignored. **P&L = $50.** Closing investment = 400 + 50 − 12.5 = **$437.50**.

**Teaching point:** crossing 20% changes P&L income from $37 (dividend + mark-to-market) to $50 (share of earnings) and switches the balance-sheet driver from market price to the equity roll-forward. Both internally consistent ✓.

---

### Q14. Goodwill under full and partial methods.

**Problem.** Acquirer pays $960 cash for 75% of Target. Fair value of Target's net identifiable assets = $1,000. Fair value of the 25% NCI = $340. Compute goodwill and NCI under (a) full-goodwill and (b) partial-goodwill methods.

**Solution.**
(a) **Full goodwill:** Goodwill = 960 + 340 − 1,000 = **$300**. NCI = **$340**.
(b) **Partial goodwill:** NCI = 25% × 1,000 = **$250**. Goodwill = 960 − (75% × 1,000) = 960 − 750 = **$210**.

**Check the difference:** full − partial goodwill = 300 − 210 = **$90**; full − partial NCI = 340 − 250 = **$90**. They differ by the same $90 — the NCI's share of goodwill — confirming consistency ✓.

---

### Q15. Full consolidation balance sheet with NCI.

**Problem.** Parent pays $700 cash for 90% of Sub. Sub's net identifiable assets fair value = $700 (assets $1,100, liabilities $400). NCI measured at fair value = $80. Parent standalone before deal: cash $900, other assets $1,600, liabilities $500, equity $2,000. Build the consolidated balance sheet at acquisition.

**Solution.**
Goodwill = 700 + 80 − 700 = **$80**.
Parent cash after payment = 900 − 700 = **$200**.
Eliminate investment $700 against Sub equity $700, recognize goodwill $80 and NCI $80:
```
Dr Sub net equity 700
Dr Goodwill        80
   Cr Investment      700
   Cr NCI               80
(700 + 80 = 780 = 700 + 80 ✓)
```

Consolidated balance sheet:

| Line | Working | $ |
|---|---|---|
| Cash | Parent 200 (Sub's cash sits inside its assets) | 200 |
| Other assets | Parent 1,600 + Sub 1,100 | 2,700 |
| Goodwill | | 80 |
| **Total assets** | | **2,980** |
| Liabilities | Parent 500 + Sub 400 | 900 |
| Equity — parent | Parent's own equity (Sub's eliminated) | 2,000 |
| Non-controlling interest | | 80 |
| **Total equity + liabilities** | | **2,980** |

**Check:** assets 2,980 = 900 + 2,000 + 80 = **2,980** ✓. Sub's $1,100 assets came in 100%; the 10% we don't own is the $80 NCI, not an asset haircut.

---

### Q16. Splitting net income between parent and NCI.

**Problem.** Continue Q15. In Year 1, Sub earns net profit $200 and pays $60 total dividends. Parent's own standalone net profit is $500. Compute consolidated net income, its split, and the closing NCI.

**Solution.**
- Group net income = Parent 500 + Sub 200 = **$700** (eliminate the intra-group portion of dividends; none affect income here as dividends aren't income to the group).
- NCI share of Sub profit = 10% × 200 = **$20**.
- Parent share = 500 + 90% × 200 = 500 + 180 = **$680**.
- Check split: 680 + 20 = **700** ✓.

NCI roll-forward:
```
Opening NCI                 80
+ NCI share of profit      +20
− Dividends to NCI (10%×60) −6
Closing NCI                 94
```
**Answers:** consolidated net income **$700** (parent **$680**, NCI **$20**); closing NCI **$94**. Check: 80 + 20 − 6 = 94 ✓.

---

### Q17. Intercompany sale with unrealized profit in inventory.

**Problem.** Parent owns 100% of Sub. Parent sells goods to Sub for $400 (Parent's cost $250). By year-end Sub has sold 60% of them externally for $330; 40% remain in Sub's inventory. Parent also has external sales of $600 (cost $360). Sub has no other activity. Compute consolidated revenue, COGS, and gross profit.

**Solution.**
- Parent gross profit on intragroup sale = 400 − 250 = $150; margin = 37.5%.
- Unrealized profit in ending stock = 40% × 150 = **$60**.

Aggregate then eliminate:
```
Revenue: Parent (600 + 400) + Sub (330)          = 1,330
Eliminate intragroup sale                         − 400
Consolidated revenue                              = 930

COGS: Parent (360 + 250) + Sub (60% × 400 = 240)  = 850
Eliminate intragroup COGS                         − 400
Add back unrealized profit (increase COGS)        + 60
Consolidated COGS                                 = 510

Consolidated gross profit = 930 − 510            = 420
```

**Independent verification (group view):** external sales = Parent 600 (GP 240) + Sub's external 330. Cost of that 330 batch to the *group* = 60% × 250 = $150 → GP = 330 − 150 = $180. Total group GP = 240 + 180 = **$420** ✓. The remaining 40% (group cost 40% × 250 = $100) sits in inventory with zero profit recognized. Matches exactly ✓.

---

### Q18. Upstream sale — sharing unrealized profit with NCI.

**Problem.** Parent owns 80% of Sub. This year **Sub sells** goods to Parent (upstream) for $500 at a $100 profit; Parent still holds 30% of those goods at year-end. How much unrealized profit is eliminated, and how is it split between parent and NCI?

**Solution.**
- Unrealized profit in stock = 30% × 100 = **$30**.
- The seller is the 80%-owned Sub, so under IFRS the elimination is shared by ownership: Parent's share = 80% × 30 = **$24**; NCI's share = 20% × 30 = **$6**.
- Consolidated profit is reduced by the full $30; the reduction attributable to NCI is $6, so **NCI profit falls by $6** and parent profit by $24.

**Check:** 24 + 6 = 30 ✓. Full $30 removed from group inventory and profit; the split preserves the 80/20 attribution of the subsidiary's earnings.

---

### Q19. Enterprise value bridge with minority interest and associates.

**Problem.** A company has: share price $50, 100m shares; total debt $1,800m; cash $300m; minority interest (fair value) $400m; preferred equity $150m; investments in associates $250m. Consolidated EBITDA is $900m. Compute EV and EV/EBITDA.

**Solution.**
- Equity value (market cap) = 50 × 100 = **$5,000m**.
```
Equity value              5,000
+ Total debt              1,800
− Cash                     −300
+ Minority interest         400
+ Preferred equity          150
− Associates               −250
Enterprise value          6,800
```
- EV/EBITDA = 6,800 / 900 = **7.6x**.

**Sense-check:** MI is added ($400) because EBITDA of $900 is 100%-consolidated; associates subtracted ($250) because their profit isn't in that EBITDA but their value is in the $5,000 market cap. If you wrongly omitted MI and left associates in, EV = 5,000 + 1,800 − 300 + 150 = $6,650 → 7.4x — understated by mismatching flows and claims.

---

### Q20. Associate profit distorts the EBITDA multiple.

**Problem.** Company X reports net income $300m, of which **$120m** is "share of profit of associates." Consolidated EBITDA is $500m. EV (before adjusting for associates) = $4,000m and the associate stake's fair value is $900m. Show how ignoring the associate flatters EV/EBITDA.

**Solution.**
- **Naive:** EV/EBITDA = 4,000 / 500 = **8.0x**.
- **Correct:** subtract associate value from EV → adjusted EV = 4,000 − 900 = $3,100m. The $120m associate profit was never in the $500m EBITDA, so EBITDA stays $500m. Adjusted EV/EBITDA = 3,100 / 500 = **6.2x**.

**Point:** the operating business is actually valued at **6.2x**, not 8.0x. The associate ($900m of value throwing off $120m of profit ≈ 7.5x on earnings) should be valued as a separate stake. Lumping it in overstates the operating multiple by ~1.8 turns.

---

### Q21. Deconsolidation intuition — loss of control.

**Problem.** Parent owns 70% of Sub (fully consolidated). It sells a 30% stake, dropping to 40%, and **loses control**. Conceptually, what changes in the financial statements?

**Model answer.** On losing control, the parent **deconsolidates** Sub: it removes 100% of Sub's assets, liabilities, and the related NCI, and stops consolidating Sub's revenue/expenses line by line. The **retained 40%** is re-measured to **fair value** and thereafter accounted for under the **equity method** (significant influence) as "Investment in associate." Any gain or loss — the difference between (proceeds + fair value of retained stake) and (carrying amount of Sub's net assets + goodwill + NCI derecognized) — is recognized in **P&L**. Going forward only "share of profit of associate" appears, not Sub's full revenue and EBITDA.

**Interview line:** "Crossing back below control flips you from 100%-line-by-line to a single equity-method line, with a remeasurement gain or loss on the way out."

---

### Q22. Step acquisition — crossing from associate to subsidiary.

**Problem.** Parent already owns 30% of Target (equity method, carrying value $300; fair value now $360). It buys another 40% for $520 cash, reaching 70% and gaining control. Target's net identifiable assets fair value = $1,000; NCI (30%) fair value = $300. Compute goodwill (full method).

**Solution.** On gaining control, the previously held 30% is **remeasured to fair value** ($360), and the $60 uplift (360 − 300 carrying) is recognized in **P&L**.
```
Goodwill = Consideration for new stake     520
         + FV of previously held stake     360
         + FV of NCI                       300
         − FV of net identifiable assets  1,000
         = 180
```
**Answers:** remeasurement gain to P&L = **$60**; goodwill = **$180**. Check: 520 + 360 + 300 = 1,180; less 1,000 = **180** ✓.

**Point:** a step acquisition treats reaching control as a *significant economic event* — you're deemed to dispose of the old stake at fair value and re-acquire the whole business, hence the remeasurement gain and fresh goodwill on 100%.
