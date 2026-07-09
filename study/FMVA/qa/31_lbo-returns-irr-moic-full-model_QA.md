# Q&A — LBO Returns — IRR, MOIC and the Full Model

Work every problem on paper or in Excel *before* reading the answer. The numbers are chosen to reconcile exactly; if your figures differ, find the arithmetic slip rather than rounding it away.

---

## Section A — Concept Check

**A1. Define MOIC and IRR in one sentence each, and state how they differ.**

MOIC (Multiple of Invested Capital, also "cash-on-cash" or "the multiple") is total cash returned to the equity investor divided by total cash invested — a pure ratio that ignores timing. IRR (Internal Rate of Return) is the annualised discount rate that sets the net present value of the equity cash flows to zero — it is timing-sensitive. MOIC tells you *how much* you made; IRR tells you *how fast* you made it.

**A2. Why can two deals have the same MOIC but very different IRRs?**

Because IRR compounds the multiple over the holding period. A 2.0x MOIC earned in 3 years is roughly a 26% IRR (2^(1/3) − 1); the same 2.0x earned in 7 years is roughly 10% IRR (2^(1/7) − 1). Same money multiple, but time destroys or magnifies the annualised rate. This is why sponsors prize early cash returns (dividend recaps, quick bolt-on exits).

**A3. Write the shortcut formula linking IRR and MOIC when there are no interim cash flows.**

IRR = MOIC^(1/n) − 1, where n is the holding period in years. Equivalently MOIC = (1 + IRR)^n. This exact relationship holds *only* when the sole cash flows are the entry outflow and a single exit inflow. Any interim distribution breaks it, and you must use the full XIRR/IRR calculation.

**A4. What are the three primary levers of LBO equity returns?**

(1) EBITDA growth — increasing the operating profit between entry and exit (via revenue growth and margin expansion). (2) Multiple expansion (or contraction) — selling at a higher/lower EV/EBITDA multiple than you paid. (3) Debt paydown / deleveraging — using the company's free cash flow to repay debt, which transfers enterprise value from creditors to equity. A fourth, often listed separately, is cash generation / dividend recaps.

**A5. In a returns attribution ("value creation bridge"), which lever is considered highest quality by LPs, and why?**

EBITDA growth (especially organic revenue growth) is highest quality because it is within the sponsor's operational control and is repeatable. Multiple expansion is lowest quality because it depends on market conditions at exit that the sponsor does not control — it can reverse. Deleveraging is financial engineering: reliable but available to any buyer, so it is not a differentiated skill.

**A6. What is entry equity, and how is it calculated from the sources & uses?**

Entry equity is the sponsor's cash investment — the plug in the sources of funds after all debt is raised. From uses: Entry EV + transaction fees + financing fees + minimum cash − existing cash used. From sources: total uses − total debt raised = sponsor equity. It is the denominator of MOIC and the t=0 outflow for IRR.

**A7. Distinguish gross returns from net returns.**

Gross returns are measured at the deal/asset level before fund-level fees. Net returns are what the LP actually receives after the GP's management fee (typically ~2% of committed capital) and carried interest (typically 20% of profits above a hurdle, often 8%). Net IRR is always lower than gross IRR. FMVA deal models compute gross returns; fund models apply the fee waterfall.

**A8. Why does a dividend recapitalisation increase IRR even if it does not change the exit equity value proportionally?**

A recap returns cash to the sponsor *early*. IRR weights early cash flows heavily. Pulling forward a distribution shortens the effective duration of the invested capital, lifting IRR even though the additional debt may slightly reduce the eventual exit equity. MOIC may rise modestly, but IRR rises sharply.

**A9. What does a negative or "not meaningful" IRR indicate, and when does the IRR function fail?**

A negative IRR means the equity returned less than invested (MOIC < 1.0x). Excel's IRR/XIRR can fail (return #NUM! or a spurious root) when the cash-flow sign changes more than once, because such streams can have multiple mathematical roots. Provide a guess argument, or use MOIC as the primary sanity check.

**A10. State the exit equity waterfall — how you get from exit enterprise value to sponsor proceeds.**

Exit EV = Exit EBITDA × Exit multiple. Then: Exit EV − Net debt at exit = Exit equity value. Net debt at exit = remaining gross debt − cash balance at exit. Exit equity value × sponsor's fully-diluted ownership % = sponsor exit proceeds. (If there is a management option pool or rollover equity, sponsor takes less than 100%.)

---

## Section B — Build / Computational Problems

*Each problem is fully reproducible in Excel. Set up the labelled cells, then check against the reconciliation.*

**B1. Simple no-interim-cash IRR and MOIC.**

A sponsor invests $400m of equity at close. Five years later the equity is worth $1,000m. No dividends were paid. Compute MOIC and IRR.

*Answer.*
- MOIC = 1,000 / 400 = **2.50x**.
- IRR = MOIC^(1/n) − 1 = 2.50^(1/5) − 1.
- 2.50^(0.2): ln 2.50 = 0.916291; × 0.2 = 0.183258; e^0.183258 = 1.20114.
- IRR = **20.11%**.
- Excel check: `=IRR({-400,0,0,0,0,1000})` → 20.11%. `=(1000/400)^(1/5)-1` → 20.11%. Both agree because there are no interim flows.

**B2. Sources & Uses → entry equity.**

Acquire a target at 10.0x entry EV/EBITDA on LTM EBITDA of $150m. Debt raised: $750m term loan. Transaction fees $30m; financing fees $20m. Target has $0 existing cash and the buyer funds a $10m minimum cash balance. Build sources & uses and solve for sponsor equity.

*Answer.*
- Entry EV = 10.0 × 150 = **$1,500m**.
- Uses: EV 1,500 + minimum cash 10 + transaction fees 30 + financing fees 20 = **$1,560m**.
- Sources: term loan 750 + sponsor equity (plug).
- Sponsor equity = 1,560 − 750 = **$810m**.
- Reconciliation: Sources 750 + 810 = 1,560 = Uses. ✓
- Entry leverage = 750 / 150 = 5.0x EBITDA; equity = 810/150 = 5.4x; total 10.4x (includes fees & min cash, so above the 10.0x purchase multiple — expected).

**B3. Full five-year model — debt schedule and exit equity.**

Continue B2. Assumptions:
- EBITDA grows from $150m at 5% per year (Year 1 EBITDA is $157.5m, ... Year 5 EBITDA $191.44m).
- Cash interest = 8% on the *opening* term-loan balance each year.
- Capex, working capital and taxes leave a **cash flow available for debt repayment (before interest)** equal to EBITDA − $40m each year (a simplifying constant for capex + WC + tax + other). All excess cash after interest sweeps the term loan (100% cash sweep); no minimum-cash build beyond the $10m already funded.
- Exit at end of Year 5 at 10.0x EV/EBITDA (flat multiple). Sponsor owns 100%.

Build the debt schedule, then compute exit equity, MOIC and IRR on the $810m.

*Answer — step by step.*

First, EBITDA and cash-before-interest (CBI = EBITDA − 40):

| Year | EBITDA | CBI (EBITDA−40) |
|---|---|---|
| 1 | 157.50 | 117.50 |
| 2 | 165.38 | 125.38 |
| 3 | 173.64 | 133.64 |
| 4 | 182.33 | 142.33 |
| 5 | 191.44 | 151.44 |

Debt schedule (open → interest at 8% of open → cash sweep = CBI − interest → close = open − sweep):

- **Y1:** open 750.00; interest 60.00; sweep 117.50 − 60.00 = 57.50; close 692.50.
- **Y2:** open 692.50; interest 55.40; sweep 125.38 − 55.40 = 69.98; close 622.52.
- **Y3:** open 622.52; interest 49.80; sweep 133.64 − 49.80 = 83.84; close 538.68.
- **Y4:** open 538.68; interest 43.09; sweep 142.33 − 43.09 = 99.24; close 439.44.
- **Y5:** open 439.44; interest 35.16; sweep 151.44 − 35.16 = 116.28; close 323.16.

(Interest checks: 750×.08=60.00; 692.50×.08=55.40; 622.52×.08=49.80; 538.68×.08=43.09; 439.44×.08=35.16. ✓)

Exit at end of Year 5:
- Exit EBITDA = 191.44; Exit EV = 10.0 × 191.44 = **1,914.42m**.
- Net debt at exit = remaining term loan 323.16 − cash 10 (minimum cash still on balance sheet) = 313.16m.
- Exit equity value = 1,914.42 − 313.16 = **1,601.26m**.
- MOIC = 1,601.26 / 810 = **1.977x** ≈ **1.98x**.
- IRR (no interim distributions) = 1.977^(1/5) − 1. ln 1.977 = 0.68155; ×0.2 = 0.13631; e^0.13631 = 1.14604. IRR = **14.60%**.
- Excel: `=IRR({-810,0,0,0,0,1601.26})` → 14.60%. ✓

**B4. Value-creation bridge (attribution) for B3.**

Decompose the $791.26m of equity value gain (1,601.26 − 810) into EBITDA growth, multiple change, and debt paydown / cash. Use entry multiple held constant on the EBITDA-growth leg.

*Answer.* A standard three-lever bridge:

- **EBITDA growth** = ΔEBITDA × entry multiple = (191.44 − 150.00) × 10.0 = 41.44 × 10 = **+414.42m**.
- **Multiple expansion** = ΔMultiple × exit EBITDA = (10.0 − 10.0) × 191.44 = **0** (flat multiple by assumption).
- **Debt paydown + cash** = reduction in net debt from entry to exit. Entry net debt = 750 − 10 = 740; exit net debt = 313.16; reduction = 740 − 313.16 = **+426.84m**.
- Sum of levers = 414.42 + 0 + 426.84 = **841.26m**.
- But equity actually grew only 791.26m. The 50.00m gap = the fees & min-cash wedge: sponsor paid 810 for entry equity while entry-EV-implied equity was EV − net debt = 1,500 − 740 = 760. The 810 − 760 = 50m of transaction + financing fees is dead-weight that the levers must overcome. Bridge: 760 (entry equity at EV multiple) + 414.42 + 0 + 426.84 = 1,601.26 exit equity. ✓ (Attribute the −50 fee drag as a separate bar so the bridge foots to the *actual* 810 cost basis.)

Takeaway: with a flat multiple, essentially all value here came from operations (EBITDA growth) and deleveraging in roughly equal measure.

**B5. Sensitivity — the effect of multiple expansion.**

Re-run B3's exit assuming the exit multiple is **11.0x** instead of 10.0x (everything else identical). New MOIC and IRR? Then re-attribute the multiple leg.

*Answer.*
- Exit EV = 11.0 × 191.44 = **2,105.86m**.
- Exit equity = 2,105.86 − 313.16 = **1,792.70m**.
- MOIC = 1,792.70 / 810 = **2.213x** ≈ **2.21x**.
- IRR = 2.213^(1/5) − 1. ln 2.213 = 0.79427; ×0.2 = 0.158855; e^0.158855 = 1.17217. IRR = **17.22%**.
- Multiple-expansion leg = (11.0 − 10.0) × 191.44 = **+191.44m**, which is exactly the increase in exit equity vs B3 (1,792.70 − 1,601.26 = 191.44). ✓ One turn of multiple = one turn × exit EBITDA of equity value. IRR jumped from 14.60% to 17.22% — the "market gift" of buying at 10x and selling at 11x.

**B6. Dividend recap and its IRR effect.**

Return to B3 (flat 10x exit, MOIC 1.98x, IRR 14.60%). Now suppose at the end of Year 3 the sponsor raises incremental debt and pays itself a **$150m dividend**. To fund it, exit-year net debt rises by $150m (assume the recap debt is never repaid and carries no incremental modelled interest, for simplicity). Compute the new equity cash-flow stream, MOIC and IRR.

*Answer.*
- Exit equity now = 1,601.26 − 150 (extra debt at exit) = **1,451.26m**.
- Cash flows to sponsor: −810 at t0; +150 at t3; +1,451.26 at t5.
- Total cash in = 150 + 1,451.26 = 1,601.26; MOIC = 1,601.26 / 810 = **1.977x** — *identical* to B3 (total cash unchanged; we merely moved 150 of it from t5 to t3 by borrowing against it).
- IRR: solve −810 + 150/(1+r)^3 + 1,451.26/(1+r)^5 = 0.
  - Try r = 15%: 150/1.520875 = 98.63; 1,451.26/2.011357 = 721.54; sum 820.17; NPV = +10.17.
  - Try r = 16%: 150/1.560896 = 96.10; 1,451.26/2.100342 = 690.96; sum 787.06; NPV = −22.94.
  - Interpolate: 15% + 10.17/(10.17+22.94) × 1% ≈ 15% + 0.307% = **~15.31%**.
- Excel: `=XIRR({-810,150,1451.26},{entry, +3yr, +5yr})` → ≈15.3%.
- **Conclusion:** identical MOIC (1.98x) but IRR rose from 14.60% to ~15.31% purely from pulling cash forward. This is the textbook demonstration of IRR's timing sensitivity.

**B7. Reconciling XIRR with the shortcut.**

For B1 (invest 400, exit 1,000, 5 years, no interim flows), confirm that `XIRR` with actual dates equals the `MOIC^(1/n)−1` shortcut, and explain when they would diverge.

*Answer.* With dates exactly 5 years (1,826 days including one leap year) apart and only two cash flows, XIRR returns 20.11%, matching 2.50^(1/5)−1 = 20.11%. They diverge whenever (a) there are interim cash flows, or (b) the period is not an integer number of years — XIRR uses actual/365 day-count, so a 5-year-and-40-day hold gives a slightly lower XIRR than the clean 5-year shortcut. Always prefer XIRR with real dates in a live model; use the shortcut only for quick mental checks.

---

## Section C — Interview-Style Questions (with model answers)

**C1. "Walk me through how an LBO generates returns."**

*Model answer.* "A sponsor buys a company mostly with debt, putting in a slice of equity. Three things drive the equity value up. First, we grow EBITDA — since enterprise value is a multiple of EBITDA, each dollar of EBITDA growth is worth roughly the entry multiple in EV. Second, we use free cash flow to pay down debt; as net debt falls, more of a fixed enterprise value accrues to equity — deleveraging. Third, if we exit at a higher multiple than we paid, we capture multiple expansion, though we don't bank on it. Returns are measured two ways: MOIC (the cash multiple) and IRR (the annualised rate). Leverage magnifies all of it — a smaller equity base makes a given EV gain a larger percentage return on equity."

**C2. "If I told you a deal returns 2.5x over 5 years, what's the IRR? Do it in your head."**

*Model answer.* "2.5x over 5 years is about 20%. Quick logic: doubling in 5 years is roughly 15% (the rule of 72 says 72/5 ≈ 14.4%), and going from 2.0x to 2.5x adds a few points, landing right around 20%. The precise figure is 2.5^(1/5) − 1 = 20.1%."

**C3. "Which is more important to a PE firm, IRR or MOIC?"**

*Model answer.* "Both, and they can conflict. IRR drives the headline fund return and carry, and LPs benchmark on net IRR, so GPs are highly IRR-focused — which is why quick flips and dividend recaps are attractive. But MOIC measures absolute dollars of profit, which is what actually compounds an LP's capital. A 3x over eight years (about 15% IRR) can be worth more in dollars than a 1.6x flipped in one year (60% IRR) because you can't always redeploy that fast. Sophisticated LPs watch both, plus DPI — realised cash returned. The honest answer: IRR wins beauty contests, MOIC pays the bills."

**C4. "A management team says they'll double EBITDA but the entry and exit multiples are the same and there's no debit paydown. What's your equity MOIC?"**

*Model answer.* "If enterprise value scales one-for-one with EBITDA and multiples are flat, doubling EBITDA doubles enterprise value. With no debt paydown, net debt is unchanged, so the *equity* value goes up by the full increase in enterprise value. Because equity is the smaller, levered slice, equity more than doubles — the MOIC is above 2x, and the more leverage at entry, the higher it goes. That's the magnifying effect of leverage: the equity return exceeds the EBITDA growth rate whenever the company is levered and the multiple holds."

**C5. "Why do sponsors love a cash sweep?"**

*Model answer.* "A cash sweep forces all excess free cash flow to repay debt automatically. It maximises deleveraging, which is one of the three return levers, and it reduces interest expense in future years — a compounding benefit. It also de-risks the deal: lower debt means more cushion on covenants and a lower chance of distress. The trade-off is that swept cash can't be reinvested or distributed, so in high-growth situations sponsors sometimes prefer a partial sweep to keep dry powder for bolt-ons."

**C6. "How does higher entry leverage affect IRR — and what's the catch?"**

*Model answer.* "Higher leverage means a smaller equity check, so the same enterprise-value gain is spread over less equity — that mechanically lifts IRR and MOIC. But there are three catches. First, more debt means more interest, which eats the free cash flow available to deleverage and to grow. Second, it raises default risk — a modest EBITDA miss can breach covenants. Third, lenders cap leverage, and pricing steps up at higher multiples. So leverage boosts returns in the base case but fattens the left tail. The art is levering enough to juice returns without threatening solvency in a downturn."

---

## Section D — Common-Error Spotting

*Each item states a mistake. Identify it and give the correct treatment.*

**D1. "MOIC is 2.0x over 4 years, so IRR is 2.0/4 = 50%."**

*Error.* IRR is not the multiple divided by years — returns compound, they don't average linearly. Correct: IRR = 2.0^(1/4) − 1 = **18.9%**, not 50%. Dividing by years grossly overstates the annualised return.

**D2. "Exit equity = Exit EV − *entry* net debt."**

*Error.* You must subtract net debt *at exit*, after several years of paydown (and cash build), not entry net debt. Using entry net debt ignores all deleveraging and understates exit equity — deleting one of the three core return levers. Correct: Exit equity = Exit EV − (remaining debt at exit − cash at exit).

**D3. "I put the transaction fees into enterprise value, so entry equity = EV − debt."**

*Error.* Transaction and financing fees are a *use of funds* on top of EV; they inflate the sponsor's equity check but are not part of the price paid for the business (they don't recur at exit at the exit multiple). Folding them into EV and then computing equity as EV − debt double-counts and misstates entry multiple. Correct: keep fees as separate uses; equity = total uses − total debt.

**D4. "The deal pays a dividend in Year 3, so I'll just add it to the exit-year cash flow and use the simple IRR shortcut."**

*Error.* Dumping the interim dividend into the terminal flow destroys its timing value and breaks the MOIC^(1/n) shortcut (which assumes a single terminal inflow). The recap's whole point is that early cash lifts IRR. Correct: model the dividend at its actual date and use XIRR (or a dated IRR) on the full stream.

**D5. "Interest each year = 8% × closing debt balance."**

*Error.* Cash interest accrues on the balance *outstanding during* the period — conventionally the **opening** balance (or an average of opening and closing to avoid circularity issues). Using the closing balance understates interest, because closing is already net of the year's paydown. Correct: interest = rate × opening balance (or an average-balance convention, handled with an iterative/circular switch).

**D6. "The exit multiple must equal the entry multiple — that's the conservative assumption."**

*Partly right, but mislabelled.* A flat multiple is the *neutral* modelling convention, not automatically "conservative." Conservative underwriting often assumes **multiple contraction** (e.g., exit 0.5–1.0x below entry) to stress the return without relying on a favourable market. Presenting a flat multiple as conservative can flatter the base case. Correct: state the assumption explicitly and sensitise exit multiple both ways.

**D7. "Gross IRR is 25%, so the LP earns 25%."**

*Error.* Gross IRR is before management fees and carried interest. After a ~2% fee and 20% carry over an 8% hurdle, net IRR to the LP is materially lower — often 4–8 points below gross. Correct: report **net** IRR/MOIC for LP-facing returns, and be explicit about the fee-and-carry drag.

**D8. "I forgot the minimum cash on the balance sheet at exit, so I set net debt = gross debt."**

*Error.* Cash reduces net debt dollar-for-dollar. Ignoring the exit cash balance overstates net debt and understates exit equity. Correct: Net debt at exit = gross debt at exit − cash and equivalents at exit (including any minimum cash and any un-swept build-up).

**D9. "Sponsor owns 100%, so exit proceeds = full exit equity value."**

*Error (context-dependent).* If there is a management incentive pool, rollover equity, or preferred/common split, the sponsor's *common* stake is below 100% on a fully-diluted basis. Correct: apply the sponsor's fully-diluted ownership percentage (net of the option pool and any rollover) to the exit equity value, and respect any preferred waterfall before common splits.

**D10. "IRR returned #NUM!, so the deal has no return — I'll leave it blank."**

*Error.* #NUM! usually means the algorithm couldn't converge from its default guess, or the sign of the cash flows changes more than once (multiple roots), *not* that returns are zero. Correct: supply a guess (e.g., `IRR(range, 0.1)`), switch to XIRR with dates, and cross-check with MOIC — if MOIC > 1.0x the deal is profitable regardless of the solver hiccup.

---

*End of Q&A bank. If any computed figure above did not reconcile in your own build, re-check the opening-balance interest convention (D5) and the exit net-debt bridge (D2, D8) first — those are the two most common sources of a few-basis-point drift.*
