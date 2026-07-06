# Q&A — Corporate Finance Fundamentals

> Practice bank for Chapter 04. Every question is followed by a full answer. Numbers are self-verified and reproducible in Excel. Sections: **A** concept-check (the *why*), **B** build/computational, **C** interview-style, **D** common-error spotting.

---

## Section A — Concept Check (test the WHY)

**A1. Why must future cash flows be discounted before you can compare them to a price on the table today?**

Because a rupee arriving in the future is worth strictly less than a rupee in your hand now, for three stacking reasons: (1) **opportunity cost** — today's rupee can be invested to earn a return, so giving it up has a cost; (2) **inflation** — future rupees buy fewer goods; (3) **risk** — promised future cash may not fully arrive. Discounting converts every future cash flow into its "today-equivalent" so all amounts sit on the same time axis and can be summed and compared to a purchase price. Without it you would be adding apples (year-20 rupees) to oranges (today's rupees).

**A2. Why does a higher discount rate *mechanically* produce a lower present value?**

Present value is $CF/(1+r)^t$. The discount rate $r$ sits in the denominator, raised to a power. Increasing $r$ inflates the denominator, and because it compounds with $t$, distant cash flows shrink fastest. Since risk enters valuation only through the discount rate ($r = R_f + \text{risk premium}$), "riskier" and "worth less today" are the same statement viewed from two ends. This inverse link between risk and value is the spine of every DCF.

**A3. Why do we discount unlevered free cash flow (FCFF) at WACC but levered free cash flow (FCFE) at the cost of equity?**

The rule is *match the cash flow to the capital it belongs to.* FCFF is the cash available to **all** providers of capital (debt and equity) before financing, so it must be discounted at the blended cost of **all** that capital — WACC — and yields enterprise value. FCFE is what remains for **equity holders only** after debt is served, so it is discounted at the return equity holders require, the cost of equity $R_e$, and yields equity value directly. Crossing them (FCFF at $R_e$, or FCFE at WACC) silently corrupts the valuation.

**A4. Why is the after-tax cost of debt, not the coupon rate, used in WACC?**

Interest expense is tax-deductible, so each rupee of interest reduces the firm's tax bill by $T$ rupees. The true economic cost of debt to the firm is therefore $R_d(1-T)$, not $R_d$. This "tax shield" is the entire reason debt is a cheaper funding source than equity and the reason adding leverage can lower WACC.

**A5. Modigliani–Miller says capital structure doesn't matter — so why do firms agonise over the debt/equity mix?**

MM Proposition I holds only in a frictionless world (no taxes, no bankruptcy costs, no information gaps). It is a *baseline*, telling us value comes from assets, not financial packaging. Reality adds frictions: taxes make debt valuable (a shield worth ~$T \times D$), while distress and bankruptcy costs make *too much* debt dangerous. The **trade-off theory** balances these, giving a U-shaped WACC and an interior optimum. So MM is the reference point that tells you *why* frictions — not the mix itself in a vacuum — create the optimum.

**A6. Why does the market reward only systematic (beta) risk and not company-specific risk?**

Diversified investors can eliminate company-specific (idiosyncratic) risk essentially for free by holding many assets whose shocks cancel. Because it can be shed at no cost, no one pays a premium to avoid it. Only **systematic** risk — the co-movement with the whole market, measured by beta — cannot be diversified away, so that is the only risk the market prices. This is the intuition behind CAPM: $R_e = R_f + \beta(R_m - R_f)$.

**A7. When NPV and IRR disagree on mutually exclusive projects, why does NPV win?**

IRR is a *rate* and ignores scale; NPV measures *value created in currency*. A 40% IRR on a ₹1 project creates ₹0.40; a 15% IRR on a ₹1bn project creates far more absolute value. IRR can also misbehave with non-conventional cash flows (multiple sign changes → multiple IRRs) and implicitly assumes reinvestment at the IRR itself. Since the goal is to maximise shareholder wealth measured in money, choose the project with the higher **NPV**.

---

## Section B — Build / Computational Problems

**B1. Compute the NPV of a project.** Cost ₹1,200 at t0; after-tax inflows of ₹300, ₹400, ₹500, ₹400, ₹300 at the ends of years 1–5. WACC = 11%. Should you accept it? Cross-check with IRR intuition.

*Step-by-step (build a discount-factor schedule):*

| Year t | Cash flow | Discount factor $1/1.11^t$ | Present value |
|---|---:|---:|---:|
| 0 | −1,200.00 | 1.000000 | −1,200.00 |
| 1 | 300 | 0.900901 | 270.27 |
| 2 | 400 | 0.811622 | 324.65 |
| 3 | 500 | 0.731191 | 365.60 |
| 4 | 400 | 0.658731 | 263.49 |
| 5 | 300 | 0.593451 | 178.04 |
| | | **PV of inflows** | **1,402.04** |

NPV = 1,402.04 − 1,200.00 = **+₹202.04**. Positive → **accept**; the project earns more than its 11% cost of capital.

*Excel (best practice — keep CF0 outside NPV):* `=-1200 + NPV(0.11, 300,400,500,400,300)` → **202.04**. Because inflows already exceed cost even after discounting, IRR must exceed 11% (it is ≈17.6%), confirming the accept decision.

**B2. Compute WACC.** Market value of equity = ₹750m, market value of debt = ₹250m. Cost of equity = 13%, pre-tax cost of debt = 8%, tax rate = 30%.

*Weights:* $V = 750 + 250 = 1{,}000$; $E/V = 0.75$; $D/V = 0.25$.

| Component | Weight | Cost | After-tax cost | Contribution |
|---|---:|---:|---:|---:|
| Equity | 0.75 | 13% | 13% | 9.750% |
| Debt | 0.25 | 8% | 8%×(1−0.30) = 5.60% | 1.400% |
| | | | **WACC** | **11.15%** |

$$WACC = 0.75(13\%) + 0.25(8\%)(1-0.30) = 9.75\% + 1.40\% = \mathbf{11.15\%}$$

Interpretation: any project returning above 11.15% creates value; below it, destroys value.

**B3. Terminal value via growing perpetuity, then discount it home.** Year-5 free cash flow = ₹200m, growing at 2.5% forever; WACC = 9%.

*Terminal value at end of year 5* (use next year's cash flow, $CF_6 = CF_5(1+g)$):
$$TV_5 = \frac{200 \times 1.025}{0.09 - 0.025} = \frac{205}{0.065} = ₹3{,}153.85\text{m}$$

*Discount back 5 years* at 9% ($1.09^5 = 1.538624$, factor 0.649931):
$$PV = 3{,}153.85 \times 0.649931 = ₹2{,}049.78\text{m}$$

Note $g < WACC$ (2.5% < 9%) so the denominator is positive and the formula is valid.

**B4. Build a loan amortisation schedule and prove it reconciles.** Loan ₹100,000 at 10% annual interest, repaid in 4 equal year-end instalments.

*Payment:* $PMT = \dfrac{P \cdot r}{1-(1+r)^{-n}} = \dfrac{100{,}000 \times 0.10}{1-1.10^{-4}} = \dfrac{10{,}000}{0.316987} = ₹31{,}547.08$. Excel: `=PMT(0.10,4,-100000)` → 31,547.08.

| Year | Opening balance | Interest (10%) | Payment | Principal repaid | Closing balance |
|---|---:|---:|---:|---:|---:|
| 1 | 100,000.00 | 10,000.00 | 31,547.08 | 21,547.08 | 78,452.92 |
| 2 | 78,452.92 | 7,845.29 | 31,547.08 | 23,701.79 | 54,751.13 |
| 3 | 54,751.13 | 5,475.11 | 31,547.08 | 26,071.97 | 28,679.16 |
| 4 | 28,679.16 | 2,867.92 | 31,547.08 | 28,679.16 | 0.00 |

**Reconciliation:** closing balance hits exactly ₹0.00 in year 4 — the schedule is internally consistent. Total interest paid = 10,000 + 7,845.29 + 5,475.11 + 2,867.92 = ₹26,188.32; total paid = 4 × 31,547.08 = ₹126,188.32 = principal (100,000) + interest (26,188.32). ✔

**B5. Cost of equity via CAPM.** Risk-free rate 4%, beta 1.2, equity risk premium $(R_m - R_f)$ = 5.5%.

$$R_e = R_f + \beta(R_m - R_f) = 4\% + 1.2 \times 5.5\% = 4\% + 6.6\% = \mathbf{10.6\%}$$

A beta above 1 means the stock is more volatile than the market, so it earns a premium above the market's own required return.

---

## Section C — Interview-Style Questions (with model answers)

**C1. "Walk me through the components of WACC and why each is weighted."**

WACC blends the cost of every source of capital by its market-value weight: $WACC = \frac{E}{V}R_e + \frac{D}{V}R_d(1-T)$. Cost of equity $R_e$ comes from CAPM and is highest because equity holders are paid last and bear residual risk. Cost of debt is the borrowing rate, taken after-tax because interest is deductible. We weight by **market values** (not book) because we want the current opportunity cost of capital, and we use it as both the hurdle rate for new projects and the discount rate for unlevered firm cash flows.

**C2. "If a company increases its leverage, what happens to WACC?"**

Initially WACC tends to **fall**: debt is cheaper than equity (lower base rate plus the tax shield), so shifting weight toward debt lowers the blended cost. But leverage also raises the riskiness of both the equity (higher beta, higher $R_e$) and eventually the debt itself (higher $R_d$ as default risk rises). Beyond an optimal point, those rising costs plus expected distress costs dominate and WACC turns back **up** — the U-shape of the trade-off theory. So the honest answer is "it falls, then rises; there's an optimum."

**C3. "A project has a positive NPV but an IRR below another project's IRR. Which do you pick?"**

If the projects are independent, take both if each has NPV > 0. If they are **mutually exclusive**, pick the higher **NPV**, because NPV measures absolute value created in currency while IRR ignores scale and can be distorted by timing or non-conventional cash flows. I'd also check *why* they diverge — usually a difference in project size or cash-flow timing — and confirm the discount rate used is the correct risk-adjusted hurdle.

**C4. "Why can't terminal growth exceed the discount rate — or GDP — forever?"**

Mathematically, in $TV = CF_1/(r-g)$, if $g \ge r$ the denominator is zero or negative, giving an infinite or nonsensical value. Economically, if a company grew faster than the whole economy forever it would eventually *become* the entire economy — impossible. So terminal growth is capped below WACC and, as a practical matter, at or below long-run nominal GDP growth (~2–3%).

**C5. "What are the three core decisions of corporate finance?"**

Investment (which assets/projects to fund — decided by NPV > 0, equivalently IRR > WACC), financing (the debt/equity mix — chosen to minimise WACC at tolerable distress risk), and distribution (whether to reinvest cash or return it via dividends/buybacks — return it whenever the firm has no project that beats its cost of capital). Every financial model is just the quantification of these three decisions.

**C6. "Retained earnings are 'free' internal cash, so projects funded from them have no capital cost — true or false?"**

False. Retained earnings belong to shareholders, who still demand their required return $R_e$ on that money — they could have received it as a dividend and invested elsewhere. Using it below the cost of equity destroys value even though no cash "leaves." There is no such thing as free equity capital.

---

## Section D — Common-Error Spotting (what's wrong with this?)

**D1. Broken formula:** cells `A1:A6` hold `−1000, 300, 300, 300, 300, 300` (A1 is the time-0 outflow). The analyst writes `=NPV(10%, A1:A6)`.

**What's wrong:** Excel's `NPV` discounts its *first* argument by one full period, so the time-0 outflow gets wrongly discounted by one year — the classic off-by-one that overstates NPV. **Fix:** keep CF0 outside the function: `=A1 + NPV(10%, A2:A6)`, or use `=XNPV(10%, A1:A6, dates)` which treats the first date as time 0.

**D2. Broken formula:** `WACC = E/V * Re + D/V * Rd`.

**What's wrong:** the cost of debt is not tax-adjusted. Interest is deductible, so the debt term must be `Rd*(1-T)`. As written, WACC is overstated and the firm will reject value-creating projects. **Fix:** `= E/V*Re + D/V*Rd*(1-T)`.

**D3. Broken model:** analyst computes WACC's after-tax cost of debt correctly, then *also* adds the interest tax savings back into the FCFF line as extra cash.

**What's wrong:** the tax shield is counted **twice** — once inside WACC (the $(1-T)$ term) and again in the cash flows. In an FCFF/WACC framework interest and its tax effect must **never** appear in the cash flows; FCFF is a pre-financing number. **Fix:** remove interest and its tax shield from FCFF; let WACC capture it.

**D4. Broken formula:** terminal value `=CF1/(WACC-g)` with `WACC = 8%` and `g = 10%`, returning a large negative number the analyst reports as value.

**What's wrong:** $g > WACC$, so $r - g$ is negative and the formula is invalid (a negative "value" is meaningless here). The growing-perpetuity model requires $g < r$. **Fix:** cap terminal growth below WACC and below long-run GDP (~2–3%); a perpetual 10% growth rate is economically impossible anyway.

**D5. Broken formula:** discount factor entered as `=1/(1+$B$2)*C1` where `$B$2` is the rate and `C1` is the period number.

**What's wrong:** the period exponent is a **multiplication**, not a power — `*C1` instead of `^C1`. Every year past year 1 is under-discounted, inflating PV. **Fix:** `=1/(1+$B$2)^C1`.

**D6. Broken model:** the analyst discounts **FCFF** (unlevered) at the **cost of equity** to get enterprise value.

**What's wrong:** mismatched cash flow and rate. FCFF belongs to all capital providers and must be discounted at **WACC**; the cost of equity applies only to FCFE. Using $R_e$ (which is higher than WACC) over-discounts and understates enterprise value. **Fix:** discount FCFF at WACC, or switch to FCFE if you insist on $R_e$.

**D7. Broken model:** WACC weights are taken from the **book** balance sheet — book equity of ₹200m though the company's market cap is ₹900m.

**What's wrong:** book weights misstate the true capital mix, especially for equity where market and book values diverge sharply. This distorts WACC (usually overweighting debt) and every valuation built on it. **Fix:** use **market values** — market cap for equity, market/fair value for debt.

---

*All computed figures verified: B1 NPV = +202.04; B2 WACC = 11.15%; B3 TV = 3,153.85 (PV 2,049.78); B4 loan amortises to 0.00; B5 $R_e$ = 10.6%.*
