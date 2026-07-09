# Q&A — DCF — Terminal Value and the Full Model

Practice bank for Chapter 24. Work each question before reading the answer. The chapter's spine is one idea: a firm outlives any forecast, so value = the cash you *can* project (explicit FCFF) + a defensible stand-in for the cash you *cannot* (terminal value), both pulled to today, then handed down from enterprise to shareholder as a *range*, not a point. Every computation below runs on the chapter's Section 4.1 dataset so you can reproduce each figure cell-for-cell in Excel and watch it reconcile.

**Base dataset.** FCFF (₹ cr) years 1–5: 100, 115, 130, 142, 150. WACC (r) = 10.0%. Terminal growth (g) = 3.0%. Year-5 EBITDA = ₹250 cr. Exit EV/EBITDA = 8.0x. Total debt = ₹400 cr. Cash = ₹60 cr. Minority interest = ₹20 cr. Diluted shares = 50 cr.

---

## Section A — Concept Checks (test the WHY)

**A1. Why is a five-year FCFF forecast, discounted on its own, a badly incomplete valuation?**

Because companies do not stop at year 5. A going concern generates cash for decades beyond any forecast window, and discounting only five years typically captures just 30–50% of a healthy firm's value. The rest — the majority — lives in the post-forecast tail. You cannot model year 37 line by line, so you need a single figure, the terminal value, that legitimately stands in for the entire infinite tail. Omit it and you have not been conservative; you have simply left half the answer uncounted.

**A2. Why is `TV = CF / (r − g)` exact arithmetic rather than a hand-waving approximation?**

Because an infinite stream growing at a constant rate `g`, discounted at a constant rate `r > g`, converges to a *finite* sum. Each future rupee is discounted more heavily than it grows, so the terms shrink geometrically and the series has a closed-form total. The only judgement lies in the inputs (`g` and `r`); the collapse of the infinite stream itself is genuine, exact mathematics. That is why the requirement `r > g` is not a preference but a mathematical necessity — if `g ≥ r`, the series diverges and the formula returns garbage.

**A3. Why must the Gordon numerator be `FCFF₅ × (1 + g)` and not bare `FCFF₅`?**

Because the perpetuity formula values a stream whose *first* cash flow arrives *one period after* the valuation date. Your last explicit year is year 5, so the perpetuity's first cash flow is year 6 — which is `FCFF₅ × (1 + g)`. The TV computed at year 5 therefore uses the year-6 numerator. Drop the `(1 + g)` and you understate the terminal value, and hence the whole valuation, by a factor of `(1 + g)` — the single most-forgotten detail in DCF.

**A4. Why is it acceptable — and simultaneously dangerous — that the terminal value is often 60–80% of enterprise value?**

Acceptable because it faithfully reflects reality: most of a going concern's value lies in its long future, not its next five years. Dangerous because it means the final answer is *hypersensitive* to two numbers you cannot observe and must assume — the terminal growth `g` and the WACC. When the majority of your value rests on two guesses, sensitivity analysis stops being decoration and becomes the core of the deliverable. A TV above ~90% of EV is a red flag that the explicit forecast is doing almost nothing and the horizon should be reconsidered.

**A5. Why does the Gordon terminal value get discounted with the year-5 factor, not the year-6 factor?**

Because the Gordon formula already expresses the entire perpetuity as a single lump sum *as of* year 5 — that is what "terminal value at year 5" means. The `(1 + g)` in the numerator handles the shift to the year-6 cash flow; the division by `(r − g)` values it back to year 5. So you discount that year-5 lump sum with the year-5 factor. Discounting it an extra period (year-6 factor) or forgetting to discount it at all are both common, large errors.

**A6. Why does the mid-year convention raise the valuation, and by roughly how much?**

The year-end convention pretends every rupee of a year lands on 31 December. In reality cash trickles in through the year, arriving on average around mid-year — about six months earlier. Money received earlier is worth more, so shaving half a period off every exponent (`t − 0.5`) lifts every present value. The uplift is approximately `(1 + WACC)^0.5 − 1` ≈ half the WACC, so about 5% at a 10% WACC. It is standard practice for going-concern DCFs and is real money, not rounding.

**A7. Why must FCFF be discounted to reach enterprise value, and why is that not equity value?**

FCFF is struck *before* interest, so it is the cash available to *all* capital providers — lenders and shareholders jointly. Discounting it therefore yields the value of the whole operating enterprise. Shareholders own only the residual after lenders are paid, so you must bridge: subtract net debt (and minority, preferred, other senior claims) and add non-operating assets the operating FCFF never captured. Reporting EV as if it were equity value overstates the share price by the entire net-debt claim.

**A8. Why does the exit-multiple method require no debt subtraction at the terminal step?**

Because EV/EBITDA is already an *enterprise-level* multiple: `Year-5 EBITDA × multiple` produces an enterprise value at year 5, not an equity value. The capital-structure bridge happens exactly once, at the very end of the model, after both explicit and terminal cash flows are summed. Subtracting debt at the terminal step and again at the bridge would double-count the lenders' claim.

**A9. Why should the exit multiple reflect a *seasoned* business rather than today's trading multiple for a high-growth firm?**

Because a firm growing 30% today commands a rich multiple *for that growth*, but by the terminal year it is assumed to be mature and slow-growing. A mature business does not trade at a growth multiple. Applying today's rich multiple to a future seasoned company systematically overstates the terminal value — the exit multiple must reflect what comparable *mature* firms trade at, or the firm's own long-run average.

**A10. Why compute the terminal value two independent ways when you only need one number?**

Because the disagreement between them *is* the finding. Back out the implied EV/EBITDA of your Gordon TV and compare it to your comparable-based exit multiple. A small gap means intrinsic and market views broadly agree — the answer is robust. A large gap (say Gordon implies 15x against an 8x comp) screams that your terminal growth is too rich or your multiple is stale. Reconciling the two methods is how you pressure-test the terminal value rather than trust it blindly.

---

## Section B — Build / Computational Problems

All builds use the base dataset. Arithmetic is shown so each answer self-checks. Year-end discount factors are `1/(1.10)^t`: 0.9091, 0.8264, 0.7513, 0.6830, 0.6209 for t = 1…5.

**B1. Compute the Gordon terminal value at year 5.**

```
TV = FCFF₅ × (1 + g) / (WACC − g)
   = 150 × 1.03 / (0.10 − 0.03)
   = 154.5 / 0.07
   = ₹2,207.14 cr
```

Verify `g < WACC` first (3% < 10%, safe). Excel: `=G10*(1+$B$4)/($B$3-$B$4)`.

**B2. Full year-end DCF to per-share value.**

PV of explicit FCFF:

| Year | FCFF | Factor | PV |
|---|---:|---:|---:|
| 1 | 100 | 0.9091 | 90.91 |
| 2 | 115 | 0.8264 | 95.04 |
| 3 | 130 | 0.7513 | 97.67 |
| 4 | 142 | 0.6830 | 96.99 |
| 5 | 150 | 0.6209 | 93.14 |
| | | **Sum** | **473.75** |

PV of TV = 2,207.14 × 0.6209 = ₹1,370.42 cr.
Enterprise value = 473.75 + 1,370.42 = **₹1,844.17 cr**.
Equity bridge = 1,844.17 − 400 (debt) + 60 (cash) − 20 (minority) = **₹1,484.17 cr**.
Per share = 1,484.17 / 50 = **₹29.68**.

Check: TV is 1,370.42 / 1,844.17 = **74% of EV** — textbook proof of where the value and risk sit.

**B3. Rebuild B2 with the mid-year convention.**

Mid-year factors `1/(1.10)^(t−0.5)`: 0.9535, 0.8668, 0.7880, 0.7164, 0.6512.

PV of explicit FCFF: 95.35 + 99.68 + 102.44 + 101.72 + 97.68 = **496.88**.
PV of TV (Gordon perpetuity treated as a mid-year flow, exponent 4.5) = 2,207.14 × 0.6512 = **1,437.29**.
EV = 496.88 + 1,437.29 = **₹1,934.17 cr**.
Equity = 1,934.17 − 400 + 60 − 20 = **₹1,574.17 cr**.
Per share = 1,574.17 / 50 = **₹31.48**.

Uplift = 31.48 / 29.68 − 1 = **+6.1%**, close to the `(1.10)^0.5 − 1 = 4.9%` rule of thumb (slightly higher because the heavily-weighted TV gained a full half-period of relief). On a ₹1,900 cr enterprise that is ~₹90 cr — never dismiss it as rounding.

**B4. Exit-multiple terminal value and the implied-multiple cross-check (year-end).**

```
TV = Year-5 EBITDA × multiple = 250 × 8.0 = ₹2,000 cr
PV of TV = 2,000 × 0.6209 = ₹1,241.80 cr
EV = 473.75 (explicit PV) + 1,241.80 = ₹1,715.55 cr
Equity = 1,715.55 − 400 + 60 − 20 = ₹1,355.55 cr
Per share = 1,355.55 / 50 = ₹27.11
```

Cross-check — back out the implied multiple of the Gordon TV:

```
Implied multiple = TV(Gordon) / Year-5 EBITDA = 2,207.14 / 250 = 8.83x
```

The Gordon assumptions (g = 3%, r = 10%) are equivalent to selling at 8.83x versus the 8.0x comp — a coherent, small gap (the intrinsic view is modestly more optimistic than the market view). A 15x-vs-8x gap would instead flag terminal growth as too rich.

**B5. What percentage of EV is the terminal value under each method, and what does the spread tell you?**

Gordon (B2): 1,370.42 / 1,844.17 = **74%**. Exit-multiple (B4): 1,241.80 / 1,715.55 = **72%**. Both sit in the normal 60–80% band, so neither method leans pathologically on the tail; the explicit forecast still carries a meaningful ~26–28%. Because both land in the same zone and the implied multiples (8.83x vs 8.0x) are close, the valuation is internally consistent and the terminal assumptions are mutually corroborating.

**B6. Two-way sensitivity of per-share value (year-end, Gordon).**

Recompute per share = `(EV − 360) / 50` across WACC and `g`. Verified grid:

| g \ WACC | 9.0% | 10.0% | 11.0% |
|---|---:|---:|---:|
| **2.0%** | 30.95 | 26.03 | 22.20 |
| **3.0%** | 36.01 | **29.68** | 24.94 |
| **4.0%** | 43.10 | 34.56 | 28.47 |

The base case (g = 3%, WACC = 10%) sits at **₹29.68**, matching B2. Worked check on the top-left corner (g = 2%, WACC = 9%): TV = 150 × 1.02 / 0.07 = 2,185.71; at 9% the year-5 factor is 0.6499 so PV of TV = 1,420.55 and explicit PV = 487.01, giving EV = 1,907.56, equity = 1,547.56, per share = **₹30.95**. The full block spans **₹22.20 to ₹43.10** — a wide band that *is* the honest output of the model. Quoting ₹29.68 to the paisa without this table sells false precision.

**B7. Fresh dataset — reproduce the full pipeline.** FCFF: 80, 92, 105, 116, 124. WACC 11%, g 3.5%. Year-5 EBITDA 210, exit 7.5x. Debt 300, cash 45, minority 15, preferred 25, non-op investments 40. Shares 40. Compute per share (year-end, Gordon).

```
TV = 124 × 1.035 / (0.11 − 0.035) = 128.34 / 0.075 = ₹1,711.2 cr
Factors 1/1.11^t: 0.9009, 0.8116, 0.7312, 0.6587, 0.5935
PV explicit = 72.07 + 74.67 + 76.78 + 76.41 + 73.59 = ₹373.5 cr
PV of TV = 1,711.2 × 0.5935 = ₹1,015.6 cr
EV = 373.5 + 1,015.6 = ₹1,389.1 cr
Equity = 1,389.1 − 300 + 45 − 15 − 25 + 40 = ₹1,134.1 cr
Per share = 1,134.1 / 40 = ₹28.35
```

Note the bridge here is fuller: preferred stock is subtracted (senior to common) and non-operating investments are added back (value the operating FCFF never captured). Per share ≈ **₹28.3**.

---

## Section C — Interview-Style Questions (model answers)

**C1. "Walk me through how you get from FCFF to a share price."**

I forecast unlevered free cash flow for the explicit period, usually five to ten years, and discount each year at the WACC. Then I compute a terminal value at the final year — either a Gordon perpetuity, `FCFF₅ × (1 + g) / (WACC − g)`, or an exit EV/EBITDA multiple — and discount that back with the final-year factor. Summing the discounted explicit flows and the discounted terminal value gives enterprise value. From there I bridge to equity: subtract net debt, minority interest, and preferred, add back non-operating assets, and divide by diluted shares. Finally I run a WACC-versus-growth sensitivity grid, because the terminal value dominates and the answer is really a range, not a single number.

**C2. "Your terminal value is 80% of enterprise value. Is your model broken?"**

Not necessarily — 60–80% is normal, because most of a going concern's value genuinely lies beyond a short forecast window. What it does mean is that my answer hinges on the two terminal inputs, WACC and `g`, so I lean hard on the sensitivity table and I cross-check the Gordon TV against an exit multiple by backing out the implied EV/EBITDA. If the TV were above ~90%, I would worry that the explicit forecast is doing no work, and I would extend the horizon until the business reaches a genuine steady state before applying the perpetuity.

**C3. "Should you use the mid-year convention? Defend your choice."**

For a going-concern DCF, yes. Cash arrives throughout the year, not on 31 December, so discounting at `t − 0.5` corrects a systematic downward bias — roughly a 5% understatement at a 10% WACC, which is real money on any sizeable deal. The one nuance is the terminal value: if it is a Gordon perpetuity of mid-year flows I discount it at `t − 0.5` for consistency; if it is an exit multiple representing a sale crystallising on a single date, many practitioners discount it at the full `t`, because a sale is a point event, not a flow. The rule is to pick a convention, state it, and apply it consistently — reviewers will check.

**C4. "What's the right terminal growth rate and how do you defend it?"**

It has to be below the WACC, mathematically, and below long-run nominal GDP growth, economically — typically 2–4% in nominal terms for a mature market. A perpetual growth rate above GDP is a claim that the firm eventually becomes larger than the whole economy, which is impossible. I anchor `g` to expected long-run inflation plus modest real growth, and I sanity-check it by backing out the implied exit multiple: if `g` produces a terminal EV/EBITDA far above what mature comparables trade at, the growth assumption is too aggressive regardless of how reasonable the percentage looks.

**C5. "You have two terminal values from two methods that disagree by 30%. What do you do?"**

The disagreement is information, not noise. I back out the implied exit multiple of the Gordon TV and compare it directly to the comparable-company multiple driving the exit-multiple TV. A 30% gap usually means either the terminal growth is too rich or the exit multiple is stale — for instance an old-cycle multiple applied to a firm that will be mature. I investigate the assumption driving the divergence, reconcile the two, and present both TVs in the output so the committee sees the intrinsic and market views side by side rather than a single reconciled number that hides the tension.

**C6. "Why not just use Excel's NPV function on the whole cash-flow row?"**

Because `NPV` assumes the first cash flow is one full period away and discounts every flow at year-end timing, so it cannot handle the mid-year convention or a terminal value that is timed separately. It is also a black box — a reviewer cannot see the discount factors. I build an explicit period row and discount-factor row instead, so every factor is visible and auditable, the terminal value takes the correct final-year factor, and I can flip mid-year on or off by editing one exponent. Control and transparency beat the one-cell shortcut every time.

---

## Section D — Common-Error Spotting

For each, identify the error and give the correct treatment.

**D1.** An analyst writes `TV = 150 / (0.10 − 0.03) = ₹2,142.86 cr`.

**Error:** the `(1 + g)` is missing from the numerator. The perpetuity's first cash flow is year 6, so the numerator must be `150 × 1.03 = 154.5`. Correct TV = 154.5 / 0.07 = **₹2,207.14 cr** — the omission understates TV by exactly 3% (the growth rate), and hence understates the whole valuation.

**D2.** A model sets terminal growth `g = 11%` against a WACC of 10%.

**Error:** `g ≥ WACC`. The denominator `(WACC − g)` is negative, so the formula returns a nonsensical negative TV, and economically it claims the firm grows faster than the discount rate forever — eventually exceeding the whole economy. Cap `g` strictly below WACC and at or below long-run nominal GDP growth (2–4%).

**D3.** After computing TV at year 5, the analyst discounts it using the year-6 factor `1/(1.10)^6`.

**Error:** off-by-one discounting. The Gordon TV is already a lump sum *at* year 5, so it takes the **year-5** factor `1/(1.10)^5 = 0.6209`. Using the year-6 factor discounts it one period too far and understates EV; forgetting to discount it at all overstates EV massively. Correct PV of TV = 2,207.14 × 0.6209 = ₹1,370.42 cr.

**D4.** A model applies the mid-year convention to the explicit FCFF (exponents `t − 0.5`) but discounts the Gordon TV at the full `t = 5`.

**Error:** inconsistent timing. If the TV is a Gordon perpetuity of mid-year flows, it should be discounted at `t − 0.5 = 4.5` to match the FCFF it grows out of. Mixing conventions within one method understates the TV relative to the flows feeding it. Decide once, document it, apply it everywhere. (The exit-multiple TV is the *only* legitimate case for full-`t` discounting, because a sale is a dated point event.)

**D5.** The output reports enterprise value of ₹1,844.17 cr as "the equity value," then divides by shares.

**Error:** the equity bridge was skipped. EV belongs to all capital providers; shareholders own only the residual. Correct: 1,844.17 − 400 (debt) + 60 (cash) − 20 (minority) = ₹1,484.17 cr equity, giving ₹29.68 per share, not ₹1,844.17 / 50 = ₹36.88. The skipped bridge overstates the share price by 24% here.

**D6.** In the bridge, the analyst subtracts total debt of ₹400 cr but forgets to add cash of ₹60 cr.

**Error:** net debt applied inconsistently. The firm's own cash could repay debt, so the correct adjustment is *net* debt = 400 − 60 = ₹340 cr. Forgetting the cash understates equity value by ₹60 cr (₹1.20 per share here). Always pair the debt subtraction with the cash addition.

**D7.** For a firm with in-the-money options, the model divides equity value by *basic* shares of 48 cr instead of diluted 50 cr.

**Error:** using basic instead of diluted shares. In-the-money options and convertibles will become shares and dilute per-share value, so the treasury-stock-method diluted count must be used. Basic shares here overstate per share to 1,484.17 / 48 = ₹30.92 versus the correct ₹29.68.

**D8.** A high-growth firm's exit-multiple TV uses today's trading multiple of 20x EV/EBITDA.

**Error:** applying a growth multiple to a future *mature* business. By the terminal year the firm is assumed seasoned and slow-growing, so it should trade at a mature comparable's multiple (say 8–10x), not today's 20x. Using 20x roughly doubles the terminal value and inflates the whole valuation on an assumption that contradicts the very premise of a terminal year.

**D9.** The final deliverable is a single line: "Value per share = ₹29.68."

**Error:** false precision — no range. Because the TV dominates and depends on two unobservable inputs, the honest output is a WACC-versus-`g` grid. On the base dataset that grid spans roughly ₹22 to ₹43 per share (see B6). A point estimate to the paisa hides exactly the uncertainty the decision-maker is paid to manage.

---

*Self-verification note:* every figure above was recomputed from the base dataset. The Gordon base case reconciles at EV ₹1,844.17 cr → ₹29.68/share; mid-year at ₹31.48 (+6.1%); exit-multiple at ₹27.11 with an implied 8.83x; and the sensitivity grid base cell ties back to ₹29.68 with a verified span of ₹22.20–₹43.10.
