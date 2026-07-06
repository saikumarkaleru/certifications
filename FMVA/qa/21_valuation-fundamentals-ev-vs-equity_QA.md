# Q&A — Valuation Fundamentals — Enterprise vs Equity Value

Practice bank for Chapter 21. Attempt every question before reading the answer. The single idea running underneath the whole chapter: **value the whole machine first (Enterprise Value), then subtract everyone who gets paid before the common shareholder (the bridge) to reach Equity Value.** Because the bridge is arithmetic, it is exact and reversible — that reversibility is your built-in error check.

**The reference company (every Section B problem uses it).** *Meridian Corp*, all figures in $ millions unless stated:

- Share price: $30.00 — Diluted shares: 250 — so **Equity Value = 7,500**
- Total debt: 2,000 — Cash & equivalents: 500 — so **Net Debt = 1,500**
- Preferred equity: 200 — Minority interest: 300 — Investments in associates: 100
- LTM EBITDA: 1,175 — LTM Net income: 500

Correctly bridged: **EV = 7,500 + 2,000 + 200 + 300 − 500 − 100 = 9,400.** Sanity multiples: EV/EBITDA = 9,400 / 1,175 = **8.0×**; P/E = 7,500 / 500 = **15.0×**. Keep these anchors in view — most B problems perturb one input and ask what moves.

---

## Section A — Concept Checks (test the WHY)

**A1. In one sentence each, what does Enterprise Value measure and what does Equity Value measure?**

Enterprise Value is the value of the core operating business to *all* capital providers combined — lenders, preferred holders, minority holders, and common shareholders. Equity Value is what remains for *common shareholders alone* after every more senior claim is accounted for. The distance between them is net debt plus other senior claims: the bridge.

**A2. Why is Enterprise Value described as "capital-structure neutral" while Equity Value is not?**

Because EV values the operating engine *before* proceeds are split among financiers, so how the business was funded does not change it. Two identical businesses financed differently have the same EV but very different Equity Values, because a levered firm's shareholders stand behind a lender in the queue. Equity Value moves with leverage; EV does not. This is the whole reason EV exists: it lets you compare businesses without financing choices polluting the comparison.

**A3. Why is cash *subtracted* to move from Equity Value to Enterprise Value?**

Because cash is a non-operating financial asset, not part of the machine that produces operating cash flow. If you buy a company for its EV and it holds surplus cash, you effectively get that cash back the instant you own it — it could immediately repay debt or be distributed — so it reduces the true price paid for the *operations*. Net debt (debt minus cash) is what genuinely stands between the enterprise and the equity holder.

**A4. Minority interest is *added* and associates are *subtracted*. Explain the opposite signs from first principles.**

They come from opposite accounting treatments. When a parent owns more than 50% of a subsidiary it *fully consolidates* it: 100% of that subsidiary's EBITDA appears in the parent's P&L even though the parent does not own all of it. So EV (built on that 100% EBITDA) must **add** minority interest to stay consistent with the metric. When a company owns 20–50% of an associate it uses the *equity method*: **none** of the associate's EBITDA appears in operating lines, only a single "share of profit" line below EBIT. That value sits outside the operating engine, so like cash it is **subtracted**. MI corrects for EBITDA you *over*-counted; associates correct for value *not in* EBITDA — opposite problems, opposite signs.

**A5. What single income-statement line is the pivot that decides whether a metric pairs with EV or with Equity Value?**

Interest expense. Everything *above* interest (revenue, EBITDA, EBIT) is pre-financing and belongs to all investors → pair with **EV**. Everything *below* interest (net income, book equity, FCFE) is post-financing — lenders have been paid — so it belongs to shareholders alone → pair with **Equity Value**. Cross this pivot and the multiple becomes nonsensical.

**A6. Why is EV/EBITDA the workhorse comparison multiple, more so than P/E?**

Because EBITDA is *before interest* (capital-structure neutral) and *before D&A* (accounting-policy neutral), so EV/EBITDA strips out both financing and depreciation choices, letting you compare the underlying operations of dissimilar firms. P/E uses net income — after interest and tax — so it is contaminated by leverage and tax structure; identical operating businesses can show very different P/Es purely because of how they are financed.

**A7. FCFF discounted at WACC gives EV; FCFE discounted at cost of equity gives Equity Value. Why must the cash flow, discount rate, and output "speak the same language"?**

Because a discount rate is the required return of a specific set of investors and must be applied to the cash flow belonging to exactly those investors. FCFF is cash for *all* financiers, so it is discounted at the blended all-investor rate (WACC) and yields EV. FCFE is cash left for shareholders after debt service, so it is discounted at the cost of equity and yields Equity Value. Mixing them — discounting FCFF at cost of equity — values an all-investor stream as if only shareholders had a claim: a fatal inconsistency.

**A8. Two firms report the same EV/EBITDA of 8.0×. Does that prove they are equally valued for a shareholder?**

Not necessarily. Equal EV/EBITDA means the market values their *operations* identically. But a shareholder buys Equity Value, and the two firms may have very different net debt, preferred, and minority claims sitting between EV and equity. The more leveraged firm delivers less equity value per dollar of EV. EV multiples say the businesses are twins; the bridge determines what each shareholder actually owns.

---

## Section B — Build / Computational Problems

Convention: in the "build EV from Equity" direction, enter **cash and associates as negatives** and use a single `=SUM()` so a sign error cannot hide. Every result below is reproducible cell-for-cell.

**B1. Build Meridian's Enterprise Value from market data.** Lay out the vertical bridge and give the Excel formula.

| Cell | Line item | Value | Sign |
|---|---|---:|---|
| B3 | Equity Value (`=B1*B2` = 30×250) | 7,500 | start |
| B4 | (+) Total debt | 2,000 | + |
| B5 | (+) Preferred equity | 200 | + |
| B6 | (+) Minority interest | 300 | + |
| B7 | (−) Cash (entered negative) | (500) | − |
| B8 | (−) Associates (entered negative) | (100) | − |
| B9 | **Enterprise Value** `=SUM(B3:B8)` | **9,400** | result |

Running total: 7,500 → 9,500 → 9,700 → 10,000 → 9,500 → **9,400**. `=SUM(B3:B8)` returns **9,400**.

**B2. Build the same EV using the net-debt form** `EV = Equity + Net Debt + MI + Preferred − Associates`, and confirm it ties to B1.

Net Debt = 2,000 − 500 = 1,500. Then EV = 7,500 + 1,500 + 300 + 200 − 100 = **9,400.** Identical to B1 — netting cash against debt first, or listing them separately, must give the same answer. This agreement is a free internal check.

**B3. Reverse the bridge.** A FCFF-DCF outputs an Enterprise Value of 9,400. Recover Equity Value and the implied share price by flipping every sign below the anchor.

| Line | Amount | Running |
|---|---:|---:|
| Enterprise Value (from DCF) | 9,400 | 9,400 |
| (−) Total debt | (2,000) | 7,400 |
| (−) Preferred equity | (200) | 7,200 |
| (−) Minority interest | (300) | 6,900 |
| (+) Cash | 500 | 7,400 |
| (+) Associates | 100 | **7,500** |

Equity Value = **7,500**; implied share price = 7,500 / 250 = **$30.00**. Every sign flipped versus B1 and we recovered the exact starting inputs — the round-trip error check passes.

**B4. Sanity-check the multiples.** Compute EV/EBITDA and P/E and state which value each uses.

EV/EBITDA = 9,400 / 1,175 = **8.0×** (uses **EV** — EBITDA is pre-interest, an all-investor metric). P/E = 7,500 / 500 = **15.0×** (uses **Equity Value / price** — net income is post-interest, a shareholders-only metric). Using EV for P/E, or Equity Value for EV/EBITDA, would compare mismatched claims.

**B5. Perturb leverage, hold operations constant.** Suppose Meridian raises 1,000 of new debt and immediately pays it out as a special dividend (cash unchanged, operations unchanged). What happens to EV and to Equity Value?

Total debt rises to 3,000; net debt rises to 2,500. The *operating business is unchanged*, so a DCF of FCFF still yields **EV = 9,400** (capital-structure neutral). But Equity Value = EV − net debt − MI − preferred + associates = 9,400 − 2,500 − 300 − 200 + 100 = **6,500**, down exactly 1,000 — the value that left the firm as the dividend, now sitting with lenders' claim ahead of shareholders. EV flat, Equity Value down: the defining behaviour of the two measures.

**B6. Diluted shares via the Treasury Stock Method.** Meridian has 246m basic shares and 12m in-the-money options struck at $20; the current price is $30. Show that diluted shares = 250m, and why using basic shares would overstate value per share.

Option proceeds = 12 × $20 = $240m. Shares repurchasable with proceeds = 240 / 30 = 8m. Net new shares = 12 − 8 = **4m**. Diluted shares = 246 + 4 = **250m**. Equivalently, net dilution = 12 × (1 − 20/30) = 12 × ⅓ = 4m. Using basic 246m would give price = 7,500 / 246 = $30.49 — overstating per-share value by ignoring the claims of option holders.

**B7. FCFF, FCFE, and WACC in one pass.** For a forecast year: EBIT 800, tax rate 25%, D&A 200, CapEx 250, ΔWorking Capital 50, interest 120, net new borrowing 30. Cost of equity 10%, pre-tax cost of debt 5%; market weights E = 7,500, D = 2,000. Compute FCFF, FCFE, and WACC, and state which value each is used to reach.

- FCFF = EBIT×(1−t) + D&A − CapEx − ΔWC = 800×0.75 + 200 − 250 − 50 = 600 + 200 − 250 − 50 = **500** → discount at WACC → **EV**.
- FCFE = FCFF − Interest×(1−t) + Net borrowing = 500 − 120×0.75 + 30 = 500 − 90 + 30 = **440** → discount at cost of equity → **Equity Value**.
- V = 7,500 + 2,000 = 9,500. WACC = (7,500/9,500)×10% + (2,000/9,500)×5%×(1−0.25) = 7.895% + 0.789% = **8.68%**.

Cross-check CAPM if r_f = 4%, β = 1.2, ERP = 5%: r_e = 4% + 1.2×5% = **10%**, consistent with the cost of equity used.

**B8. Minority-interest consistency.** Meridian's 1,175 EBITDA fully consolidates a 70%-owned subsidiary that contributes 175 of that EBITDA; the 300 minority interest is the 30% Meridian does not own. Explain why the 8.0× EV/EBITDA is only correct *because* MI was added.

EBITDA of 1,175 reflects **100%** of the subsidiary. If MI had been omitted, EV would be 9,400 − 300 = 9,100 and EV/EBITDA = 9,100 / 1,175 = 7.75× — dividing a 100%-EBITDA into an EV that captured only Meridian's *share* of the subsidiary. Adding MI restores the match: the numerator (EV, whole enterprise) and denominator (EBITDA, whole enterprise) both represent 100%, giving the correct 8.0×.

---

## Section C — Interview-Style Questions (model answers)

**C1. "Walk me through the bridge from Equity Value to Enterprise Value."**

Start with Equity Value — share price times diluted shares. Add total debt, because lenders have a claim on the operating business senior to shareholders. Add preferred equity and minority interest for the same reason — both sit ahead of common equity in the waterfall. Subtract cash and cash equivalents, because cash is a non-operating asset you effectively receive when you buy the business. Subtract investments in associates, because that value sits outside the operating EBITDA the enterprise is built on. What remains is Enterprise Value — the value of the core operations to all capital providers. Reverse every sign to go back from EV to Equity Value.

**C2. "Why would a company have a higher Enterprise Value than Equity Value — or vice versa?"**

EV exceeds Equity Value whenever net debt (plus preferred and minority interest) is positive — the normal case for a leveraged company. Equity Value exceeds EV when the company holds more cash than debt: a net-cash business, common among mature tech firms. In that case cash dominates the bridge, so subtracting net debt (a negative number) *raises* nothing and the cash pulls EV below Equity Value. Neither ordering is "good" or "bad" on its own — it just reports the net financing position.

**C3. "You have a company's EV/EBITDA and a peer's P/E. Can you convert one to the other?"**

Not directly — they measure different claims — but you can move between them via the bridge. Apply the peer EV/EBITDA to your EBITDA to get EV, cross the bridge (subtract net debt, preferred, minority; add associates) to Equity Value, then divide by net income for an implied P/E. They reconcile only after both the bridge and the interest/tax gap between EBITDA and net income are accounted for. Quoting them as interchangeable is the classic mismatch error.

**C4. "Two identical businesses, one levered and one not. Which multiple do you trust to compare them, and why?"**

EV/EBITDA. Because EBITDA is pre-interest, both firms show the same EV/EBITDA — correctly revealing them as operational twins. P/E, which uses post-interest net income, makes the levered firm look different purely because of financing. Concretely: both have EBITDA 500 and EV 4,000, so both are 8.0× on EV/EBITDA. But at the same EBIT of 350, the levered firm (interest 120) has net income 172.5 versus 262.5 for the unlevered firm at 25% tax, giving P/Es of 11.6× versus 15.2× — a spurious 30% gap driven only by capital structure. EV/EBITDA neutralises that; P/E does not.

**C5. "A company holds a 30% stake in another business. How does that affect your valuation?"**

The 30% stake is an equity-method associate, so *none* of its revenue or EBITDA appears in the parent's operating lines — only a "share of profit of associates" line below EBIT. So it contributes nothing to the EBITDA the EV multiple is built on. To avoid understating value, I subtract the associate's value from EV as a non-operating asset (like cash), and I do **not** include its earnings in the EBITDA I apply the multiple to. Including its earnings while also subtracting its value would double-count.

**C6. "If a company issues equity and uses the cash to repay debt, what happens to Enterprise Value?"**

Nothing, to a first approximation. The operating business is unchanged, and the transaction just swaps debt for equity: net debt falls, Equity Value rises by roughly the same amount, and EV — the sum of all claims on unchanged operations — stays flat. This is capital-structure neutrality in action. Second-order effects (distress risk, tax shield, signaling) can nudge operating value slightly, but the mechanical first-order effect on EV is zero.

---

## Section D — Common-Error Spotting

For each, identify the error and give the correction.

**D1.** An analyst writes: `EV / Net Income = 9,400 / 500 = 18.8×` and calls it the P/E.

Error: numerator (EV, all-investor value) is divided by a shareholders-only metric (net income). This is the cardinal mismatch. P/E must use **Equity Value / net income = 7,500 / 500 = 15.0×**. Rule: net income is below interest → pair with Equity Value, never EV.

**D2.** Building EV, the analyst writes `EV = Equity + Debt + Cash + Preferred + MI`.

Error: cash has the wrong sign — it is *added* instead of *subtracted*. Cash is a non-operating asset that reduces the net price of operations, so EV = Equity + Debt + Preferred + MI **− Cash** − Associates. The safe habit is to pre-sign cash as negative and `=SUM()` the block.

**D3.** For a company with a 70%-owned consolidated subsidiary, the analyst computes `EV = Equity + Net Debt − Cash` and stops, ignoring the 300 minority interest.

Error: minority interest is omitted. Because the subsidiary is fully consolidated, EBITDA reflects 100% of it, so EV must **add** the 300 MI to stay consistent. Omitting it understates EV and produces a too-low EV/EBITDA. Also note "Net Debt − Cash" double-subtracts cash — net debt already nets cash.

**D4.** The analyst adds minority interest and *also* adds associates when building EV.

Error: associates have the wrong sign. MI is added (corrects EBITDA over-counted under full consolidation); associates are **subtracted** (their value sits outside operating EBITDA under the equity method). Opposite treatments → opposite signs.

**D5.** A DCF discounts **FCFF at the cost of equity** and calls the result Enterprise Value.

Error: the discount rate does not match the cash flow. FCFF belongs to all investors and must be discounted at **WACC** to give EV. Discounting FCFF at cost of equity treats an all-investor cash stream as if only shareholders had a claim, overstating the discount rate's specificity and corrupting the value. Either discount FCFF at WACC → EV, or discount FCFE at cost of equity → Equity Value.

**D6.** Valuing a distressed firm, the analyst uses the **book value** of debt in the bridge even though its bonds trade at 60 cents on the dollar.

Error: for distressed debt, book value overstates the true claim. The market value of the debt is 60% of face, so the real senior claim standing ahead of equity is smaller — using book value understates Equity Value. Use **market value of debt** when it diverges materially from book (distressed situations); book value is only a fair proxy for a healthy issuer.

**D7.** The analyst compares today's market EV against an EBITDA figure from three years ago, and against a peer that excludes capitalised leases from debt.

Two errors. First, a time mismatch: today's EV must pair with a trailing (LTM) or forward (NTM) metric labelled consistently, not a stale three-year-old number. Second, a definitional mismatch: under IFRS 16 / ASC 842 most leases are debt; if the peer excludes lease liabilities its EV understates the enterprise and its EV/EBITDA is not comparable. Align both time periods and debt definitions before comparing multiples.

**D8.** The analyst values Equity Value using **basic shares** of 246m rather than diluted.

Error: in-the-money options and convertibles dilute existing holders, so basic shares overstate value per share. Run the Treasury Stock Method: here 12m options at a $20 strike against a $30 price add 4m net shares, giving 250m diluted. Equity Value per share is 7,500 / 250 = $30.00, not 7,500 / 246 = $30.49. Always use diluted.

---

*Mastery check:* build Meridian's EV both ways (B1, B2), reverse it to recover $30.00 (B3), explain every sign from first principles (A3–A4, C1), and spot each Section D mismatch without notes — the foundation on which DCF, comps, precedent transactions, and LBO all rest.
